#!/usr/bin/env python3
"""
nen_ptk_extract.py — the NEN pre-tender market consultation reader, and the
normalize.py extractor for it.

WHAT ONE RECORD IS
==================
A Czech public buyer that does not yet know how to specify what it needs runs a
*předběžná tržní konzultace* (§33 ZZVZ): it publishes the need, names itself,
and asks the market how the thing could be done — BEFORE it writes a
specification and before a koruna is attached. That is an ASK in the sense of
docs/superpowers/specs/2026-09-03-asks-ledger-design.md: a named owner, a
stated problem, no money. `predpokladHodnota` is null on every P-record
measured — 32/32 on 2026-09-03 and again 22/22 on the 2026-09-04 walk of
P00000001–P00000025 — "before money is attached", literally.

One record = one NEN P-series procedure that IS a market consultation.

THE SURFACE, AND WHY IT IS A COUNTER WALK
=========================================
Measured 2026-09-03 (see the route report): the ISVZ open-data bulk that
scripts/fetch_nen.sh reads carries ZERO of these — `druh_zadavaciho_postupu`
has no consultation value and `typ_formulare` never takes the one the schema
declares. The only surface that carries them is NEN's own detail page:

  https://nen.nipez.cz/verejne-zakazky/detail-zakazky/N006-<YY>-P<8 digits>

server-rendered, HTTP 200, with the whole record as a percent-encoded JSON
object in `<meta name="initialReduxState">` at
`detailObjectStore.objects["detail-verejne-zakazky-<kod>"].object`. No HTML
parsing is needed and none is done: the tiles are a rendering of that object.

The listing is ordered by LAST publication, so "walk until older than SINCE"
is unreliable there. P-numbers, by contrast, are assigned sequentially per
year from P00000001, so a counter walk is both complete and cheap — and a
missing number answers HTTP 404, an honest status with no login-page
ambiguity. fetch_nen_ptk.sh owns the walk; this file owns the contract.

WHAT IS CUT, AND WHY IT IS AN ALLOWLIST
=======================================
The object carries `osobaJmeno`, `osobaPrijmeni`, `osobaEmail`, `osobaTelefon`,
`osobaMobil`, `osobaFax`, `osobaFunkce`, `osobaTitPred`, `osobaTitZa`,
`osobaDalsiInfo` — a named civil servant with a work mailbox and a phone
(measured: N006/26/P00000122 carries both). The ledger's AC-GDPR1 gate refuses
any record carrying an email or phone, and our ledgers are public and
append-only, so a leak is not recoverable.

FIELDS is therefore an ALLOWLIST, never a denylist over `osoba*`: a denylist
protects against the fields NEN ships today and fails silently on the field it
ships next quarter. Only the nine named keys below are ever read off the
object; the live object carries 63.
`popisPredmet` is free text a buyer typed, so it gets the second layer too —
every sentence carrying an email or phone is dropped with normalize.py's own
two patterns (copied, not imported: normalize imports this file and an import
back would close a cycle, the mpsv_extract precedent). The subject page is read
for exactly one key, `ico` — it also carries the buyer's bank account, its
switchboard and a second named person's mailbox.

`Průzkum trhu` IS NOT A CONSULTATION
====================================
The same P-series carries `druhZRNazev: "Průzkum trhu"` — a price check ("MZe
prosí o nacenění …"): the buyer already knows what it wants and is shopping.
6 of 32 sampled P-records on 2026-09-03, and 6 of 22 on the 2026-09-04 walk
of P00000001–P00000025 — a fifth to a quarter of the series. Those are dropped
by the FIELD, not by judgement over the title, and counted under
`not-a-consultation`.

A ROW MUST STATE A NEED
=======================
`popisPredmet` runs 43–4,477 chars, median 345. Under MIN_POPIS characters
after collapse it is a label, not a need a builder could start on — the same
bar hack_extract.MIN_STATEMENT applies to hackathon challenge boxes, and for
the same reason. Counted under `no-stated-need`, never staged.

THE OWNER IS THE BUYER, OR THERE IS NO RECORD
=============================================
`zadavatelNazev` is the institution that asked. It is the `owner` — the fact
this ledger exists for (CONVENTIONS.md: REQUIRED on every `asks` record, gated
in db.py check_owner()). There is no fallback to "NEN" or to the ministry that
runs it: NEN is the noticeboard, not the asker. A row with no buyer is not
staged, and extract_nen_ptk() refuses it again, because a payload row is a file
anyone can edit.

Signature and return shape of extract_nen_ptk() are normalize.py's, not ours.
"""
import argparse
import html
import json
import os
import re
import sys
from urllib.parse import unquote

# ── the surface's own constants ────────────────────────────────────────────
DETAIL_URL = "https://nen.nipez.cz/verejne-zakazky/detail-zakazky/{ref}"
SUBJECT_URL = "https://nen.nipez.cz/registr-zadavatelu/detail-subjektu/{sid}"

# The kind that IS a market consultation. Exact, from `druhZRNazev`.
PTK_DRUH = "Předběžná tržní konzultace"

# Under this many characters after collapse, `popisPredmet` names a thing
# rather than stating a need. hack_extract.MIN_STATEMENT is the same number for
# the same reason; the two are independent bars on two feeds, not a shared
# constant, because either owner may move theirs without moving the other.
MIN_POPIS = 80

# The HTML marker the fetcher's MODE-A guard also greps for: the detail
# template renders "Druh zadávacího postupu" as a tile label on every real
# procedure page and on no error document.
HTML_MARKER = "Druh zadávacího postupu"

OBJ_PREFIX = "detail-verejne-zakazky-"
SUBJ_PREFIX = "detail-subjektu-"

# THE ALLOWLIST. Every key read off the meta object, and no other — see the
# header. Adding a key here is a deliberate act; NEN adding one is not.
FIELDS = (
    "kod",                    # N006/26/P00000122 — the identity
    "nazev",                  # the consultation's own title
    "druhZRNazev",            # the procedure kind; the drop rule reads this
    "zadavatelNazev",         # the buyer = the owner
    "zadavatelID",            # NEN's internal subject id; the IČO hop's key
    "popisPredmet",           # the need text
    "cpvPredmetuKod",         # CPV, for the sector pass downstream
    "datumProfil",            # first publication on the profile
    "podaniInformaceLhuta",   # the consultation's own deadline
)
# The one key read off a subject page. The rest of that object is a bank
# account, a switchboard and a named person's mailbox.
SUBJECT_FIELDS = ("ico",)

# Drop reasons. Strings, because they are printed by the fetcher and counted
# per reason in the summary — a bare total would say "20% vanished" and not why.
NOT_CONSULTATION = "not-a-consultation"
NO_STATED_NEED = "no-stated-need"
NO_OWNER = "no-owner"

# AC-GDPR1's two patterns, verbatim from scripts/normalize.py.
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)

_WS = re.compile(r"\s+")
_TAG = re.compile(r"<[^>]+>")
_SENT = re.compile(r"(?<=[.!?…])\s+")
_META_RE = re.compile(
    r'<meta\s+name="initialReduxState"\s+content="([^"]*)"', re.I | re.S)
_ISO_DT = re.compile(r"^(\d{4}-\d{2}-\d{2})")
_NONALNUM = re.compile(r"[^a-z0-9]+")

MAX_POPIS = 1500


class ContractViolation(Exception):
    """A 200 whose body is not the surface we asked for (MODE A)."""


# --------------------------------------------------------------------------
# text
# --------------------------------------------------------------------------

def collapse(s):
    return _WS.sub(" ", str(s or "")).replace("\xa0", " ").strip()


def clean_text(s):
    """HTML -> whitespace-collapsed text. `popisPredmet` is a rich-text field:
    buyers paste <p>/<br>/<strong> into it, and a stripped tag must leave a
    SPACE behind or two sentences fuse into one word."""
    s = _TAG.sub(" ", str(s or ""))
    s = html.unescape(s).replace("\xa0", " ")
    return collapse(s)


def cut_contacts(text):
    """Drop every sentence carrying an email or phone. The text is already
    collapsed, so re-joining on one space is lossless for what is kept."""
    return " ".join(p for p in _SENT.split(text)
                    if not (EMAIL_RE.search(p) or PHONE_RE.search(p))).strip()


def iso_day(s):
    """'2026-05-15T15:19:55' -> '2026-05-15'; anything else -> ''."""
    m = _ISO_DT.match(collapse(s))
    return m.group(1) if m else ""


def cap(text, n):
    """<= n chars, preferably at a sentence end — a need cut mid-clause reads
    as a different claim from the one the buyer made."""
    if len(text) <= n:
        return text
    cut = text[:n]
    i = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
    return (cut[:i + 1] if i > n // 2 else cut.rsplit(" ", 1)[0]).strip()


def ref_of(kod):
    """'N006/26/P00000122' -> 'N006-26-P00000122', the URL form."""
    return collapse(kod).replace("/", "-")


def detail_url(kod):
    return DETAIL_URL.format(ref=ref_of(kod))


# --------------------------------------------------------------------------
# the meta JSON — MODE-A guards first, then the object
# --------------------------------------------------------------------------

def _read_text(path):
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8", "replace")


def parse_meta(text):
    """The `initialReduxState` object, or a ContractViolation saying why not.

    The content attribute is PERCENT-ENCODED JSON (measured: `%7B%22breadcrumb…`),
    HTML-escaped on top. Both layers come off, in that order, before json."""
    m = _META_RE.search(text)
    if not m:
        head = collapse(text)[:80]
        raise ContractViolation(
            f"no initialReduxState meta in the body (starts {head!r})")
    try:
        return json.loads(unquote(html.unescape(m.group(1))))
    except ValueError as e:
        raise ContractViolation(f"initialReduxState does not parse as JSON: {e}")


def _store_object(state, prefix, want=None):
    objs = ((state.get("detailObjectStore") or {}).get("objects") or {})
    if not isinstance(objs, dict) or not objs:
        raise ContractViolation("meta JSON carries no detailObjectStore.objects")
    keys = [k for k in objs if str(k).startswith(prefix)]
    if not keys:
        raise ContractViolation(
            f"no {prefix}* object in the store (keys: {sorted(objs)[:3]})")
    if want:
        # The page we asked for is the page we must parse. A redirect to
        # another procedure would still be a 200 with a valid object in it.
        exact = [k for k in keys if k[len(prefix):] == want]
        if not exact:
            raise ContractViolation(
                f"store holds {keys[0]!r}, not {prefix + want!r} (redirect?)")
        keys = exact
    obj = (objs[keys[0]] or {}).get("object")
    if not isinstance(obj, dict) or not obj:
        # A 404 page still ships the meta with `object: null` (measured on
        # P00009999). Refusing it here means a body stored despite the status
        # can never be parsed as if it were a record.
        raise ContractViolation(f"{keys[0]}.object is empty — no such record")
    return obj


def guard_detail(path, kod=None):
    """Refuse a 200 whose body is not a NEN procedure detail page.
    Returns the allowlisted object. `kod` is the slashed form when the caller
    wants the identity checked against what it asked for."""
    text = _read_text(path)
    state = parse_meta(text)
    if HTML_MARKER not in text:
        # The tile label. Its absence means the template rendered something
        # other than a procedure — an error document, a maintenance notice, or
        # the shell a 404 serves.
        raise ContractViolation(
            f"HTML 200 with meta but no {HTML_MARKER!r} tile in the body")
    obj = _store_object(state, OBJ_PREFIX, kod)
    if not collapse(obj.get("druhZRNazev")):
        raise ContractViolation("procedure object carries no druhZRNazev")
    if not collapse(obj.get("kod")):
        raise ContractViolation("procedure object carries no kod")
    return {k: obj.get(k) for k in FIELDS}


def guard_subject(path, sid=None):
    """Refuse a 200 whose body is not a NEN subject (buyer) page.
    Returns {'ico': …} and nothing else — see the header."""
    obj = _store_object(parse_meta(_read_text(path)), SUBJ_PREFIX,
                        str(sid) if sid else None)
    ico = collapse(obj.get("ico"))
    if not ico:
        raise ContractViolation("subject object carries no ico")
    return {k: collapse(obj.get(k)) for k in SUBJECT_FIELDS}


# --------------------------------------------------------------------------
# the payload row
# --------------------------------------------------------------------------

def row_from_object(obj, icos=None):
    """One guarded object -> (row, drop_reason). Exactly one of the two is None.

    `icos` maps zadavatelID (str) -> IČO; a buyer the fetcher could not resolve
    degrades to "" rather than gating the record — the owner is the NAME, and
    the IČO is a join key the entity pass can recover from ARES."""
    druh = collapse(obj.get("druhZRNazev"))
    kod = collapse(obj.get("kod"))
    if druh != PTK_DRUH:
        # By the field, never by the title. A title regex would start matching
        # a real consultation the quarter someone writes "průzkum" in one.
        return None, f"{NOT_CONSULTATION} ({druh or 'no druh'})"
    buyer = collapse(obj.get("zadavatelNazev"))
    if not buyer:
        return None, NO_OWNER
    popis = cut_contacts(clean_text(obj.get("popisPredmet")))
    if len(popis) < MIN_POPIS:
        return None, NO_STATED_NEED
    sid = collapse(obj.get("zadavatelID"))
    return {
        "kod": kod,
        "nazev": collapse(obj.get("nazev")),
        "druh": druh,
        "buyer": buyer,
        "buyer_id": sid,
        "ico": collapse((icos or {}).get(sid, "")),
        "popis": cap(popis, MAX_POPIS),
        "cpv": collapse(obj.get("cpvPredmetuKod")),
        "date": iso_day(obj.get("datumProfil")),
        "deadline": iso_day(obj.get("podaniInformaceLhuta")),
        "url": detail_url(kod),
    }, None


def fold(paths, out_path, icos=None):
    """Every guarded detail body -> one nenptk-consultations.jsonl.

    Returns the counts the fetcher prints. Deduped on `kod`: the walk visits
    each number once, but a re-run into the same outdir must not double a row.
    A body that fails its guard is a CONTRACT VIOLATION and stops the fold —
    the fetcher never hands one over, because it guards before it keeps."""
    rows, drops, seen = {}, {}, []
    for p in paths:
        obj = guard_detail(p)
        row, why = row_from_object(obj, icos)
        if row is None:
            drops[collapse(obj.get("kod")) or os.path.basename(p)] = why
            continue
        seen.append(row["kod"])
        rows[row["kod"]] = row
    ordered = sorted(rows.values(), key=lambda r: (r["date"], r["kod"]), reverse=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        for r in ordered:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    by_reason = {}
    for why in drops.values():
        # The parenthesised druh is detail; the reason is the key.
        by_reason[why.split(" (")[0]] = by_reason.get(why.split(" (")[0], 0) + 1
    return {
        "pages": len(paths),
        "consultations": len(ordered),
        "duplicates": len(seen) - len(rows),
        "dropped": len(drops),
        "dropped_by_reason": by_reason,
        "dropped_detail": sorted(f"{k}: {v}" for k, v in drops.items()),
        "buyers": len({r["buyer"] for r in ordered}),
        "no_ico": sum(1 for r in ordered if not r["ico"]),
    }


# --------------------------------------------------------------------------
# the normalize.py extractor
# --------------------------------------------------------------------------

def extract_nen_ptk(item, payload_key, today):
    """One consultation -> one asks record, or None when the row names no
    buyer or states no need. Shape is extract_nku's, plus the top-level
    `owner`."""
    kod = collapse(item.get("kod"))
    title = collapse(item.get("nazev"))
    buyer = collapse(item.get("buyer"))
    url = collapse(item.get("url")) or (detail_url(kod) if kod else "")
    # The owner gate, restated against the payload FILE rather than the page:
    # data/raw is writable and a row is not a page. CONVENTIONS.md makes
    # `owner` required on every asks record and db.py check_owner() refuses one
    # without it — better to stage nothing than to stage a record the ledger
    # will red-build on.
    if not kod or not title or not buyer or not url:
        return None
    popis = collapse(item.get("popis"))
    if len(popis) < MIN_POPIS:
        return None
    cpv = collapse(item.get("cpv"))
    return {
        "id": "nenptk-" + _NONALNUM.sub("-", kod.lower()).strip("-"),
        "source": "nen-ptk",
        "evidence_type": "asks",
        "url": url,
        "date": collapse(item.get("date")) or today.isoformat(),
        "title_native": title,
        "entity_native": buyer,
        # WHO ASKED, as the top-level schema'd field the ledger keeps and
        # db.py gates. `entity_native` is a staging field the append allowlist
        # drops, so this is the only copy that reaches a page.
        "owner": buyer,
        "sector": None,
        # NO MONEY, AND THAT IS THE POINT. `predpokladHodnota` is null on every
        # P-record measured — a consultation runs before the value exists. The
        # tender that may follow carries the money and arrives through nen/ted.
        "money_eur": None,
        "money_note": "",
        # THE CONSULTATION DEADLINE IS NOT URGENCY. Owner ruling 2026-09-03,
        # the same one tacr and hackathon carry: `podaniInformaceLhuta` is when
        # the buyer stops taking phone calls about its meeting — logistics, not
        # a deadline the world imposes on the PROBLEM, and letting it score
        # urgency would be one field carrying two meanings (MATCH.md §0).
        # Materiality for asks is decided by scale, in normalize.py; the
        # payload row keeps `deadline` as context.
        "urgency_date": None,
        "quote_parts": [p for p in (title, popis[:200]) if p],
        "excerpt": collapse(f"{title} — {buyer}: {popis}")[:400],
        # CPV only. The IČO stays on the payload row: `notes` is free text, and
        # a structured key riding inside free text is the defect the `owner`
        # field was created to end (CONVENTIONS.md).
        "notes": f"CPV {cpv}" if cpv else "",
    }


# --------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("guard", help="MODE-A: refuse a 200 whose body is not a "
                                     "NEN detail page; prints '<kod>\\t<druh>'")
    g.add_argument("path")
    g.add_argument("--kod", default=None, help="the slashed kod the fetcher asked for")
    b = sub.add_parser("buyer", help="print zadavatelID off a guarded detail page")
    b.add_argument("path")
    s = sub.add_parser("ico", help="MODE-A: refuse a 200 that is not a subject "
                                   "page; prints the IČO")
    s.add_argument("path")
    s.add_argument("--sid", default=None)
    f = sub.add_parser("fold", help="guarded detail bodies -> one "
                                    "nenptk-consultations.jsonl; prints a JSON summary")
    f.add_argument("--out", required=True)
    f.add_argument("--ico-map", default=None,
                   help="JSON object {zadavatelID: ico} built by the fetcher")
    f.add_argument("--paths-from", default=None,
                   help="file of guarded body paths, one per line — how the "
                        "fetcher passes them, so a path with a space in it "
                        "survives the shell")
    f.add_argument("paths", nargs="*")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "guard":
            o = guard_detail(a.path, a.kod)
            print(f"{collapse(o.get('kod'))}\t{collapse(o.get('druhZRNazev'))}")
            return 0
        if a.cmd == "buyer":
            print(collapse(guard_detail(a.path).get("zadavatelID")))
            return 0
        if a.cmd == "ico":
            print(guard_subject(a.path, a.sid)["ico"])
            return 0
        paths = list(a.paths)
        if a.paths_from:
            with open(a.paths_from, encoding="utf-8") as fh:
                paths += [ln.rstrip("\n") for ln in fh if ln.strip()]
        icos = {}
        if a.ico_map and os.path.exists(a.ico_map):
            with open(a.ico_map, encoding="utf-8") as fh:
                icos = {str(k): collapse(v) for k, v in (json.load(fh) or {}).items()}
        print(json.dumps(fold(paths, a.out, icos), ensure_ascii=False))
        return 0
    except ContractViolation as e:
        print(f"CONTRACT VIOLATION: {e}")
        return 65


if __name__ == "__main__":
    sys.exit(main())
