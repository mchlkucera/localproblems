#!/usr/bin/env python3
"""
cityvizor_index.py — CityVizor's public invoice API, reduced to a QUERYABLE
INDEX OF WHAT CZECH PUBLIC BODIES ACTUALLY PAID. Stdlib only. Reader + MODE-A
guard for scripts/fetch_cityvizor.sh, and the entry points
scripts/cityvizor_selftest.py drives.

WHAT THE SOURCE IS
==================
`https://cityvizor.cz/api/public/…` — the public, unauthenticated JSON API of
CityVizor, the open-source (AGPL-3.0) municipal-budget viewer written at the
Ministry of Finance and run by Otevřená města z.s. Municipalities upload their
accounting ledgers voluntarily. MEASURED 2026-09-05 against the live host and
read against the server source (github.com/cityvizor/cityvizor, branch
`staging`, server/src/routers/public/profile-payments.ts):

  GET /api/public/profiles
      338 profiles, 35 with `hasPayments: true`, 26 of those `status: visible`.
      Fields: id, url (the page slug), name, ico, status, type, parent,
      hasPayments. The 9 non-visible ones are test profiles ("Testicek",
      "aaaaa", "bbb", "Úvaly-test", "Ostrava-test", "test_po"), Kladno (no
      dated month at all) and Hlavní město Praha (`pending`, no IČO, data
      2007-2019 only). `status: visible` is therefore the population.
  GET /api/public/profiles/{id}/payments
      One row per accounting line. Fields: profileId, year (the BUDGET year),
      paragraph (rozpočtový paragraf), item (rozpočtová položka), unit, event,
      incomeAmount, expenditureAmount, date, counterpartyId (IČO),
      counterpartyName, description.
      Query params THE SOURCE HONOURS: `limit` (parseAndLimitNumber, hard
      cap 10,000 — asking for more silently gives 10,000), `offset`, `sort`
      ("date" / "-date"; adds `date IS NOT NULL`), `dateFrom` (>=), `dateTo`
      (<, EXCLUSIVE). `year` and `month` are NOT read by the router — the
      earlier probe that saw them "silently ignored" was right, and this file
      is why: they are not in the code.
  GET /api/public/profiles/{id}/payments/months
      Distinct (year, month) pairs that hold rows — the extent per body.

THE 10,000-ROW CAP, AND THE HONEST WAY PAST IT
==============================================
There is no page token. The fetcher walks each body through DISJOINT DATE
WINDOWS — the whole range first, then calendar years, then months, then days —
and splits a window only when it comes back holding exactly the cap (a window
of 10,000 rows is a truncated window by definition). Disjoint windows cannot
overlap, so nothing is fetched twice and nothing is deduplicated away. Only a
single DAY holding 10,000+ lines would need `offset` paging, where Postgres
gives no stable order across pages; such windows are flagged `paged=1` in the
window list and counted in the summary as `paged_windows`. MEASURED
2026-09-05: zero of them.

WHY A LOOKUP TABLE AND NOT A FEED
=================================
The same reason scripts/ms21_index.py gives, only more so: ~80,000 invoice
lines a YEAR across 26 bodies, every one carrying real money, would pass
materiality and bury data/signals/** many times over — the `smlouvy` trap in
data/feeds.json's own words. There is no aggregate that keeps the useful part
(one buyer, one counterparty, one price, one description), so it is not
evidence at all: data/lookup/cityvizor-invoices.jsonl (CONVENTIONS.md "Lookup
layer": committed, never pruned, no evidence type, no score, not walked by
db.py or the build gate), searched on demand by scripts/cityvizor_query.py.
NO row in data/feeds.json.

WHICH LINES ARE "A PRICE FOR A THING" — BY BUDGET ITEM, MEASURED
================================================================
The ledger holds everything the body paid, and most of it is not a price.
Over six 2024 samples (72 Středočeský kraj, 37 Ostrava, 71 Karlovarský kraj,
1 Nové Město na Moravě, 63 Ostrava-Poruba, 44 Kroměříž; 35,709 expenditure
lines) the rozpočtová položka classes were:

  ADMITTED (purchases — a counterparty was paid for goods, services or IP)
    51xx  29,034  neinvestiční nákupy: 5169 služby, 5154 elektřina, 5171
                  opravy, 5139 materiál, 5168 IT služby, 5172 programové
                  vybavení, 5137 DDHM …
    61xx   2,293  investiční nákupy: 6121 stavby, 6111 programové vybavení,
                  6122 stroje, 6125 výpočetní technika …
    504x     ~30  odměny za užití duševního vlastnictví — 5042 is where a
                  SOFTWARE LICENCE RENEWAL is booked ("prodloužení licence
                  ESET PROTECT", item 5042). Excluding 50xx wholesale would
                  drop exactly the rows a software record wants.
  REFUSED, each for a stated reason
    50xx (rest)   platy, OOV, pojistné — payroll to people, not a purchase
    52xx   1,015  transfery podnikatelům a neziskovkám — a grant, not a price
    53xx   1,087  transfery veřejným rozpočtům: 5331 příspěvek own PBO, 5362
                  daně — money moved between public pockets, no subject
    54xx-57xx     transfery obyvatelstvu, abroad, loans
    58xx   1,689  náhrady: every one in the sample is "Ubytování uprchlíků"
                  paid at the government-decree rate — a compensation, not a
                  negotiated price; arguable, and it is OUT so that `basis:
                  signed-contract` never lands on a decree rate
    59xx, 62xx-69xx  reserves, shares, investment transfers

Every kept row carries `budget_item`, so the caller can see which code it got.
Refused classes are counted in the summary under `non_purchase_skipped`.

Also refused, counted: income lines (`incomeAmount` set, `expenditureAmount`
0), negative expenditures (credit notes — a refund is not a price), and
lines that round to 0 Kč (CONVENTIONS.md makes `amount_czk: 0` a REAL receipt,
"a free incumbent sets the price", so a rounded-away heller must not arrive
wearing that meaning).

THE 30 MB CEILING, AND WHAT IT DID TO THE WINDOW
=================================================
data/lookup/ is committed and never pruned, so the ms21 ceiling (30 MB) is the
owner's stop rule here too. MEASURED: the 26 bodies produce ~80,000 purchase
lines a year at ~280 bytes each — two years is ~45 MB, over the ceiling even
after the brief's own fallback. So the index keeps whole calendar months,
newest first, and drops the OLDEST month across ALL bodies until the file fits;
the summary reports `kept_from`, `kept_to` and `months_trimmed`, and the
fetcher prints them. The window is uniform across bodies so that "who paid
what for X in the last N months" compares like with like.

ROW IDENTITY
============
The public view exposes no row id. `id` is `cv-<profileId>-<sha1[:12]>` over
the RAW source values (date, paragraph, item, event, amount, counterparty
IČO, description) — raw, so a change to this file's scrubbing rules cannot
move an id — with `-2`, `-3` … appended to the second and later IDENTICAL
lines of the same body (the ledgers really do hold identical lines: one
invoice split across two events, two receipts of the same fee). Rows are
written sorted by (date, profileId, id), so a rebuild over unchanged data is
byte-identical and `git status` stays a signal that the source moved.

Usage:
    python3 scripts/cityvizor_index.py guard-profiles <profiles.json>
    python3 scripts/cityvizor_index.py bodies <profiles.json>
    python3 scripts/cityvizor_index.py guard <payments.json>
    python3 scripts/cityvizor_index.py years|months|days --from D --to D
    python3 scripts/cityvizor_index.py index --profiles <profiles.json> \\
            --windows <windows.tsv> --out data/lookup/cityvizor-invoices.jsonl
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import unicodedata

API_URL = "https://cityvizor.cz/api/public"
SITE_URL = "https://cityvizor.cz"
CAP = 10000  # parseAndLimitNumber(req.query.limit, 10000) in the router

# The budget-item classes admitted as "a counterparty was paid for a thing".
# An explicit admit-list, not a range: see the header — 5042 (software
# licences) sits inside a class that is otherwise payroll.
PURCHASE_ITEM_PREFIXES = ("504", "51", "61")

# ── contact-shaped text is cut here, at the reader ──────────────────────────
# COPIED VERBATIM from scripts/normalize.py (EMAIL_RE / PHONE_RE), not
# imported, for the reason scripts/ms21_index.py states: normalize.py is the
# ledger's gate and data/lookup/ must never grow a dependency that makes it
# look like a ledger. The selftest proves this copy still bites.
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)

DESCRIPTION_MAX = 300
COUNTERPARTY_MAX = 200
HEAD_BYTES = 4096
_WS = re.compile(r"\s+")
_HTMLISH_RE = re.compile(r"<\s*(?:!doctype\s+html|html|head|body|form)\b", re.I)
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

PROFILE_KEYS = ("id", "url", "name", "status", "hasPayments")
PAYMENT_KEYS = ("profileId", "year", "item", "incomeAmount", "expenditureAmount",
                "date", "counterpartyId", "counterpartyName", "description")


def fold(s):
    """Case- and diacritic-insensitive form. 'Kódování' -> 'kodovani'."""
    return "".join(c for c in unicodedata.normalize("NFKD", str(s or ""))
                   if not unicodedata.combining(c)).casefold()


def collapse(s):
    return _WS.sub(" ", str(s or "")).strip()


def scrub(s):
    """Whitespace-collapsed, with any contact-shaped run removed."""
    s = collapse(s)
    s = EMAIL_RE.sub("", s)
    s = PHONE_RE.sub("", s)
    return collapse(s)


def clip(s, limit):
    """Truncate at a WORD boundary and mark it (ms21_index.clip, verbatim)."""
    if len(s) <= limit:
        return s
    cut = s[:limit]
    sp = cut.rfind(" ")
    if sp > limit * 0.6:
        cut = cut[:sp]
    return cut.rstrip(" ,;:.") + "…"


def money(v):
    """
    1357453.32 -> 1357453 (whole crowns, rounded). None when absent or not a
    number — never 0, for the CONVENTIONS.md reason in the header.
    """
    if v is None or isinstance(v, bool):
        return None
    try:
        return int(round(float(v)))
    except (TypeError, ValueError):
        return None


def isodate(v):
    """'2024-03-01T00:00:00.000Z' -> '2024-03-01'; '' when not a date."""
    t = collapse(v)
    return t[:10] if len(t) >= 10 and _DATE_RE.match(t[:10]) else ""


def is_purchase(item):
    """Budget item (rozpočtová položka) admitted as a purchase — see header."""
    if item is None or isinstance(item, bool):
        return False
    s = str(item).strip()
    return s.isdigit() and s.startswith(PURCHASE_ITEM_PREFIXES)


def item_class(item):
    s = str(item).strip() if item is not None else ""
    return (s[:2] + "xx") if len(s) >= 2 and s.isdigit() else "none"


# ──────────────────────────────────────────────────────────────────────────────
# MODE A — the source contract, evaluated before anything is parsed further
# ──────────────────────────────────────────────────────────────────────────────
def _load_json_array(raw, what):
    """Return (list, None) or (None, reason)."""
    if not raw or not raw.strip():
        return None, "empty body"
    head = raw[:HEAD_BYTES].decode("utf-8", "replace")
    h = _HTMLISH_RE.search(head)
    if h:
        return None, "body is HTML (%r), not the %s JSON" % (h.group(0), what)
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as e:
        return None, "body is not JSON (%s): %r" % (e, head[:80])
    if not isinstance(data, list):
        keys = sorted(data.keys())[:8] if isinstance(data, dict) else type(data).__name__
        return None, "%s body is not a JSON array (got %s)" % (what, keys)
    return data, None


def guard_payments_bytes(raw):
    """
    None when `raw` is a CityVizor payments response, else a REASON string.

    A 200 proves the transport, not the body: nginx in front of this host
    serves the Angular shell for any unknown path as 200 text/html, and a
    maintenance page or an error object would index to zero rows and read as
    a healthy empty month. An EMPTY ARRAY IS VALID — a month with no invoices
    is a real answer — but every element present must carry the field set
    the public view exposes, or the shape moved and nothing downstream can
    tell.
    """
    data, why = _load_json_array(raw, "payments")
    if why:
        return why
    for i, row in enumerate(data):
        if not isinstance(row, dict):
            return "row %d is not an object" % i
        missing = [k for k in PAYMENT_KEYS if k not in row]
        if missing:
            return "row %d lacks %s — the payments view changed shape" % (i, ", ".join(missing))
    return None


def guard_profiles_bytes(raw):
    """None when `raw` is the profiles list, else a REASON string."""
    data, why = _load_json_array(raw, "profiles")
    if why:
        return why
    if not data:
        return "profiles list is empty — 338 expected"
    for i, row in enumerate(data):
        if not isinstance(row, dict):
            return "profile %d is not an object" % i
        missing = [k for k in PROFILE_KEYS if k not in row]
        if missing:
            return "profile %d lacks %s — the profiles endpoint changed shape" % (i, ", ".join(missing))
    return None


def _read(path):
    with open(path, "rb") as fh:
        return fh.read()


def guard_file(path):
    return guard_payments_bytes(_read(path))


def guard_profiles_file(path):
    return guard_profiles_bytes(_read(path))


def bodies(profiles):
    """
    The population to walk: `status: visible` AND `hasPayments`. Sorted by id
    so the walk order — and therefore the receipts — is stable.
    """
    out = []
    for p in profiles:
        if p.get("status") != "visible" or not p.get("hasPayments"):
            continue
        out.append({
            "id": int(p["id"]),
            "profile": collapse(p.get("url")),
            "name": collapse(p.get("name")),
            "ico": collapse(p.get("ico")),
            "type": collapse(p.get("type")),
        })
    out.sort(key=lambda b: b["id"])
    return out


# ──────────────────────────────────────────────────────────────────────────────
# Date windows — [from, to) with `to` EXCLUSIVE, exactly as the router's
# dateTo (`<`) is, so adjacent windows never share a day.
# ──────────────────────────────────────────────────────────────────────────────
def _d(s):
    return dt.date.fromisoformat(s)


def years(frm, to):
    a, b = _d(frm), _d(to)
    out = []
    y = a.year
    while dt.date(y, 1, 1) < b:
        lo = max(a, dt.date(y, 1, 1))
        hi = min(b, dt.date(y + 1, 1, 1))
        if lo < hi:
            out.append((lo.isoformat(), hi.isoformat()))
        y += 1
    return out


def months(frm, to):
    a, b = _d(frm), _d(to)
    out = []
    y, m = a.year, a.month
    while dt.date(y, m, 1) < b:
        nxt = dt.date(y + (m == 12), (m % 12) + 1, 1)
        lo = max(a, dt.date(y, m, 1))
        hi = min(b, nxt)
        if lo < hi:
            out.append((lo.isoformat(), hi.isoformat()))
        y, m = nxt.year, nxt.month
    return out


def days(frm, to):
    a, b = _d(frm), _d(to)
    out = []
    while a < b:
        out.append((a.isoformat(), (a + dt.timedelta(days=1)).isoformat()))
        a += dt.timedelta(days=1)
    return out


# ──────────────────────────────────────────────────────────────────────────────
# The index pass
# ──────────────────────────────────────────────────────────────────────────────
# Field order is fixed and the writer uses it (the ms21 rule): a lookup
# rewritten in place every run must diff byte-stably when nothing changed.
FIELDS = ("id", "body", "body_ico", "profile", "year", "date", "counterparty",
          "counterparty_ico", "amount_czk", "description", "budget_paragraph",
          "budget_item")


def row_key(profile_id, p):
    """The identity of a source line, over RAW values. See ROW IDENTITY."""
    parts = (str(profile_id), collapse(p.get("date")), str(p.get("paragraph")),
             str(p.get("item")), str(p.get("event")), repr(p.get("expenditureAmount")),
             collapse(p.get("counterpartyId")), str(p.get("description") or ""))
    return hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:12]


def row_from_payment(body, p, stats):
    """One API line -> one index row, or None (and a counted reason)."""
    exp = p.get("expenditureAmount")
    inc = p.get("incomeAmount")
    if (money(inc) or 0) != 0 and (money(exp) or 0) == 0:
        stats["income_skipped"] += 1
        return None
    amt = money(exp)
    if amt is None:
        stats["no_amount"] += 1
        return None
    if amt < 0:
        stats["negative_skipped"] += 1
        return None
    if amt == 0:
        stats["zero_skipped"] += 1
        return None
    if not is_purchase(p.get("item")):
        c = item_class(p.get("item"))
        stats["non_purchase_skipped"][c] = stats["non_purchase_skipped"].get(c, 0) + 1
        return None
    date = isodate(p.get("date"))
    if not date:
        stats["no_date"] += 1
        return None
    desc_raw = p.get("description") or ""
    cp_raw = p.get("counterpartyName") or ""
    if EMAIL_RE.search(desc_raw) or PHONE_RE.search(desc_raw) \
            or EMAIL_RE.search(cp_raw) or PHONE_RE.search(cp_raw):
        stats["contact_cut"] += 1
    year = p.get("year")
    try:
        year = int(year)
    except (TypeError, ValueError):
        year = int(date[:4])
    row = {
        "id": "",  # filled by the caller once duplicates are counted
        "body": body["name"],
        "body_ico": body["ico"],
        "profile": body["profile"],
        "year": year,
        "date": date,
        "counterparty": clip(scrub(cp_raw), COUNTERPARTY_MAX),
        "counterparty_ico": collapse(p.get("counterpartyId")),
        "amount_czk": amt,
        "description": clip(scrub(desc_raw), DESCRIPTION_MAX),
        "budget_paragraph": p.get("paragraph") if isinstance(p.get("paragraph"), int) else None,
        "budget_item": p.get("item") if isinstance(p.get("item"), int) else None,
    }
    return row


def read_windows(path):
    """windows.tsv: id \\t from \\t to \\t file \\t paged — written by the fetcher."""
    out = []
    with open(path, "r", encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) != 5:
                raise ValueError("%s:%d: expected 5 tab-separated fields, got %d" % (path, ln, len(parts)))
            out.append({"id": int(parts[0]), "from": parts[1], "to": parts[2],
                        "file": parts[3], "paged": parts[4].strip() == "1"})
    return out


def build_index(profiles_path, windows_path, out_path, max_mb=30.0):
    """Read every accepted window, write the JSONL, return a summary dict."""
    with open(profiles_path, "rb") as fh:
        raw = fh.read()
    why = guard_profiles_bytes(raw)
    if why:
        raise ValueError("profiles: " + why)
    by_id = {b["id"]: b for b in bodies(json.loads(raw.decode("utf-8")))}

    stats = {"bodies": 0, "windows": 0, "paged_windows": 0, "lines": 0,
             "kept": 0, "income_skipped": 0, "negative_skipped": 0,
             "zero_skipped": 0, "no_amount": 0, "no_date": 0,
             "non_purchase_skipped": {}, "contact_cut": 0, "duplicate_lines": 0,
             "no_body_ico": 0, "by_body": {}, "fetched_from": "", "fetched_to": ""}

    rows = []
    seen_bodies = set()
    windows = read_windows(windows_path)
    for w in windows:
        body = by_id.get(w["id"])
        if body is None:
            raise ValueError("window for profile %d, which is not a visible body with payments" % w["id"])
        stats["windows"] += 1
        if w["paged"]:
            stats["paged_windows"] += 1
        stats["fetched_from"] = min(stats["fetched_from"] or w["from"], w["from"])
        stats["fetched_to"] = max(stats["fetched_to"], w["to"])
        seen_bodies.add(w["id"])
        raw = _read(w["file"])
        why = guard_payments_bytes(raw)
        if why:
            raise ValueError("%s: MODE-A refused at index time: %s" % (w["file"], why))
        for p in json.loads(raw.decode("utf-8")):
            stats["lines"] += 1
            row = row_from_payment(body, p, stats)
            if row is None:
                continue
            row["_key"] = row_key(w["id"], p)
            row["_pid"] = w["id"]
            rows.append(row)
    stats["bodies"] = len(seen_bodies)

    # Identical lines of the same body get -2, -3 … in encounter order.
    counts = {}
    for r in rows:
        k = (r["_pid"], r["_key"])
        n = counts.get(k, 0) + 1
        counts[k] = n
        r["id"] = "cv-%d-%s" % (r["_pid"], r["_key"]) + ("-%d" % n if n > 1 else "")
        if n > 1:
            stats["duplicate_lines"] += 1

    rows.sort(key=lambda r: (r["date"], r["_pid"], r["id"]))

    # ── the ceiling: whole months, oldest dropped first, uniformly ──────────
    ceiling = int(max_mb * 1048576)
    lines = {}
    for r in rows:
        line = json.dumps({k: r[k] for k in FIELDS if r[k] not in (None, "")},
                          ensure_ascii=False, sort_keys=False) + "\n"
        lines[r["id"]] = line.encode("utf-8")
    total = sum(len(v) for v in lines.values())
    trimmed = []
    while rows and total > ceiling:
        oldest = min(r["date"][:7] for r in rows)
        keep = []
        for r in rows:
            if r["date"][:7] == oldest:
                total -= len(lines.pop(r["id"]))
            else:
                keep.append(r)
        rows = keep
        trimmed.append(oldest)

    d = os.path.dirname(out_path)
    if d:
        os.makedirs(d, exist_ok=True)
    tmp = out_path + ".part"
    with open(tmp, "wb") as out:
        for r in rows:
            out.write(lines[r["id"]])
            stats["kept"] += 1
            stats["by_body"][r["body"]] = stats["by_body"].get(r["body"], 0) + 1
            if not r["body_ico"]:
                stats["no_body_ico"] += 1
    os.replace(tmp, out_path)

    stats["bytes"] = os.path.getsize(out_path)
    stats["mb"] = round(stats["bytes"] / 1048576.0, 2)
    stats["months_trimmed"] = trimmed
    stats["kept_from"] = (min(r["date"] for r in rows)[:7] + "-01") if rows else ""
    stats["kept_to"] = max(r["date"] for r in rows) if rows else ""
    return stats


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    sub = ap.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("guard", help="MODE-A: refuse a body that is not a payments response")
    g.add_argument("file")
    gp = sub.add_parser("guard-profiles", help="MODE-A: refuse a body that is not the profiles list")
    gp.add_argument("file")
    b = sub.add_parser("bodies", help="TSV of the bodies to walk: id, slug, name, ico")
    b.add_argument("file")
    for name in ("years", "months", "days"):
        w = sub.add_parser(name, help="disjoint [from,to) %s windows, one per line" % name[:-1])
        w.add_argument("--from", dest="frm", required=True)
        w.add_argument("--to", required=True)
    i = sub.add_parser("index", help="build data/lookup/ from the accepted windows")
    i.add_argument("--profiles", required=True)
    i.add_argument("--windows", required=True)
    i.add_argument("--out", default="data/lookup/cityvizor-invoices.jsonl")
    # The owner's stop rule: data/lookup/ is committed and never pruned.
    i.add_argument("--max-mb", type=float, default=30.0,
                   help="keep whole months, newest first, under this (default 30)")
    args = ap.parse_args(argv)

    if args.cmd == "guard":
        reason = guard_file(args.file)
        if reason:
            print("MODE-A REFUSED: %s" % reason, file=sys.stderr)
            return 65
        with open(args.file, "rb") as fh:
            print(json.dumps({"rows": len(json.loads(fh.read().decode("utf-8")))}))
        return 0

    if args.cmd == "guard-profiles":
        reason = guard_profiles_file(args.file)
        if reason:
            print("MODE-A REFUSED: %s" % reason, file=sys.stderr)
            return 65
        with open(args.file, "rb") as fh:
            profiles = json.loads(fh.read().decode("utf-8"))
        print(json.dumps({"profiles": len(profiles),
                          "with_payments": sum(1 for p in profiles if p.get("hasPayments")),
                          "walk": len(bodies(profiles))}))
        return 0

    if args.cmd == "bodies":
        with open(args.file, "rb") as fh:
            profiles = json.loads(fh.read().decode("utf-8"))
        for bd in bodies(profiles):
            print("%d\t%s\t%s\t%s" % (bd["id"], bd["profile"], bd["name"], bd["ico"]))
        return 0

    if args.cmd in ("years", "months", "days"):
        fn = {"years": years, "months": months, "days": days}[args.cmd]
        for lo, hi in fn(args.frm, args.to):
            print("%s %s" % (lo, hi))
        return 0

    try:
        stats = build_index(args.profiles, args.windows, args.out, args.max_mb)
    except ValueError as e:
        print("cityvizor_index: %s" % e, file=sys.stderr)
        return 65
    stats["out"] = args.out
    print(json.dumps(stats, ensure_ascii=False, sort_keys=True))
    if stats["kept"] == 0:
        print("cityvizor_index: ZERO rows kept from %d lines — the item filter or the "
              "source shape changed; not a healthy empty index." % stats["lines"],
              file=sys.stderr)
        return 66
    return 0


if __name__ == "__main__":
    sys.exit(main())
