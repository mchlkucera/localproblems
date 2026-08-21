#!/usr/bin/env python3
"""
sukl_extract.py — the SÚKL medicine-supply payload reader, and the normalize.py
                  extractor for it.

THE INTERFACE
=============
One URL, no auth, no pagination, no query language:

    https://opendata.sukl.cz/soubory/MR/mr.zip      (1.6 MB)

It is the "hlášení o uvedení / přerušení / ukončení / obnovení dodávek léčivého
přípravku na trh" register — every notice a marketing-authorisation holder is
legally required to file about a medicine's supply to the Czech market. There is
no richer interface to prefer over it and nothing to scrape: this IS the
declared one. What it serves, MEASURED 2026-08-21:

    ETag: "18a64e-65982336cc958"
    Last-Modified: Thu, 20 Aug 2026 22:40:03 GMT
    Content-Length: 1615438        Accept-Ranges: bytes

Last-Modified moved by exactly 24 h and 1 s between the 2026-08-20 and
2026-08-21 probes (…19 Aug 22:40:02 -> …20 Aug 22:40:03), so the refresh is a
nightly job at 22:40 UTC. That makes the conditional GET real rather than
decorative: outside one window a day, the correct answer is 304.

Two members, both CSV:
    mr_hlaseni.csv            82,837 data rows, ; -delimited, quoted, CP1250
    mr_hlaseni_platnost.csv   one cell — the dataset's own validity date

CP1250 IS THE FIRST REASON THIS FILE EXISTS. The registry contract says
`parse: csv`, and normalize.py's csv branch is
`csv.DictReader(raw.splitlines())` over a file opened as UTF-8 with
errors="replace" — comma-delimited. Pointed at this CSV it yields ONE column per
row, named `"POSLEDNI_PLATNE_HLASENI";"KOD_SUKL";…`, with every Czech diacritic
replaced by U+FFFD. It would not raise; it would parse, and the FIELDS check
would then find every required field missing from every item and mark a healthy
feed BROKEN. So the decode, the delimiter and the date format are settled here,
at fetch time, next to the bytes — and what reaches data/raw/ is JSON.

AGGREGATION IS NOT AN OPTIMISATION HERE, IT IS THE ONLY CORRECT GRAIN
=====================================================================
CONVENTIONS.md: "For any aggregating feed, AGGREGATE BEFORE THIS FILTER: a
per-item feed whose items each score money 1 is filtered out of existence while
looking like it ran correctly."

Run the arithmetic on one row of this file. A single interrupted presentation
carries no money at all, so `money` = 0. Its DATUM_HLASENI is in the past, so
score_urgency() returns None and `urgency` = 0. One drug out of stock at one
manufacturer is one org, so a truthful `scale` is 0-1. Materiality drops
`money <= 1 AND scale <= 1 AND urgency == 0` — so a per-row feed would fetch
82,837 items a week and write approximately none of them, while every counter in
the manifest read green. That is the `hiring` trap verbatim, and it is why the
ids below are keyed on (month × ATC group), never on KOD_SUKL.

The id shape follows the `mpsv-` rule for the same reason it was written:
"Reposting is the whole problem — the same vacancy reappears for months, so any
id derived from the posting itself defeats the dedup index." A SÚKL interruption
sits in this file until it is resolved; MEASURED, 22,356 of 82,837 rows are the
currently-valid notice and the oldest still-valid one dates to 2010. An id
derived from KOD_SUKL would re-propose the same shortage every single day.

TWO FAMILIES, BOTH MONTHLY:
  sukl-<YYYY-MM>-preruseni-<ATC1>   STOCK. Presentations whose supply is
                                    interrupted right now, by ATC anatomical
                                    group. 14 groups populated in the 2026-08
                                    snapshot; N (nervous system) alone is 408.
  sukl-<YYYY-MM>-ukonceni           FLOW. Permanent market exits notified in
                                    that month — products leaving for good,
                                    which is what narrows the substitute list
                                    the stock records depend on.

USED FROM TWO PLACES:
  scripts/fetch_sukl.sh   — `python3 scripts/sukl_extract.py read …`
  scripts/normalize.py    — `extract_sukl()` as EXTRACTORS["sukl"] (HAND-OFF —
                            see the note on extract_sukl below)
"""

import argparse
import collections
import csv
import datetime
import io
import json
import re
import sys
import zipfile

# --------------------------------------------------------------------------
# 1. THE SOURCE CONTRACT — MODE A, evaluated at FETCH time.
# --------------------------------------------------------------------------
#
# Everything asserted here was measured against the real 2026-08-21 payload.
# The point is not that these values are pretty; it is that each one is a thing
# a wrong body cannot have. An Apache error page, a maintenance notice or a
# truncated transfer fails the first or second assertion and never reaches disk.
ZIP_MAGIC = b"PK\x03\x04"
MEMBER_DATA = "mr_hlaseni.csv"
MEMBER_VALIDITY = "mr_hlaseni_platnost.csv"
DELIM = ";"
ENCODING = "cp1250"
REQUIRED_COLUMNS = (
    "POSLEDNI_PLATNE_HLASENI", "KOD_SUKL", "NAZEV", "DOPLNEK", "REG", "ATC",
    "TYP_OZNAMENI", "PLATNOST_OD", "DATUM_HLASENI", "NAHRAZUJICI_LP",
    "NAHRAZUJICI_LP_POZNAMKA", "DUVOD_PRERUSENI_UKONCENI", "TERMIN_OBNOVENI",
)
# The register held 82,837 rows on 2026-08-21 and only ever grows — notices are
# never deleted, the oldest still-valid one is from 2010. A file under 50,000
# rows is a different file, not a quiet week.
CONTRACT_MIN_ROWS = 50_000
# The four values TYP_OZNAMENI is allowed to take. Measured counts:
# preruseni 29,374 · obnoveni 22,338 · zahajeni 17,050 · ukonceni 14,075.
KNOWN_TYPES = {"zahajeni", "preruseni", "obnoveni", "ukonceni"}


class ContractViolation(Exception):
    """A 200 carrying the wrong body. Louder than a non-200, by design."""


def assert_zip(path):
    with open(path, "rb") as fh:
        magic = fh.read(4)
    if magic != ZIP_MAGIC:
        head = open(path, "rb").read(200).decode("utf-8", "replace")
        raise ContractViolation(
            f"not a zip (magic {magic!r}); first 200 bytes: {head[:200]!r}")
    try:
        zf = zipfile.ZipFile(path)
    except zipfile.BadZipFile as e:
        raise ContractViolation(f"corrupt zip: {e}") from e
    names = [i.filename for i in zf.infolist()]
    if MEMBER_DATA not in names:
        raise ContractViolation(f"no {MEMBER_DATA} in zip; members: {names[:8]}")
    return zf


def read_csv(zf, member, required=()):
    raw = zf.read(member)
    try:
        text = raw.decode(ENCODING)
    except UnicodeDecodeError as e:
        raise ContractViolation(f"{member} is not {ENCODING}: {e}") from e
    rows = list(csv.DictReader(io.StringIO(text), delimiter=DELIM))
    if required:
        cols = set(rows[0].keys()) if rows else set()
        missing = [c for c in required if c not in cols]
        if missing:
            # This is the check that catches a login page saved as .csv: an HTML
            # body decodes fine and "parses" as a one-column CSV, so only the
            # column names can tell the difference.
            raise ContractViolation(
                f"{member}: columns {missing} missing; got {sorted(cols)[:6]}")
    return rows


# --------------------------------------------------------------------------
# 2. READING
# --------------------------------------------------------------------------

DATE_RE = re.compile(r"^(\d{2})\.(\d{2})\.(\d{4})$")


def iso(cz_date):
    """`22.03.2019` -> `2019-03-22`. The ONLY date format in this source."""
    m = DATE_RE.match(str(cz_date or "").strip())
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else None


# ATC level 1 — the WHO anatomical main groups. Kept as a literal table rather
# than derived, because the label is what a reader needs and the letter alone
# says nothing. Names are English; the source ships codes only.
ATC1 = {
    "A": "alimentary tract and metabolism", "B": "blood and blood-forming organs",
    "C": "cardiovascular system", "D": "dermatologicals",
    "G": "genito-urinary system and sex hormones",
    "H": "systemic hormonal preparations", "J": "anti-infectives for systemic use",
    "L": "antineoplastic and immunomodulating agents",
    "M": "musculo-skeletal system", "N": "nervous system",
    "P": "antiparasitic products", "R": "respiratory system",
    "S": "sensory organs", "V": "various",
}

# See the identical block in scripts/nen_extract.py for why these are duplicated
# rather than imported from normalize.py: this module must be able to refuse
# contact data while running inside fetch_sukl.sh, where normalize.py is not
# loaded at all. SÚKL's free-text columns (DUVOD_PRERUSENI_UKONCENI,
# NAHRAZUJICI_LP_POZNAMKA) are written by manufacturers, and "no personal data
# has appeared there yet" is a fact about today's file, not a property of it.
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)


def contact_free(s):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    cut = len(s)
    for rx in (_EMAIL_RE, _PHONE_RE):
        m = rx.search(s)
        if m:
            cut = min(cut, m.start())
    return s if cut == len(s) else s[:cut].rstrip(" ,;:-")


def _reasons(rows):
    c = collections.Counter(contact_free(r.get("DUVOD_PRERUSENI_UKONCENI") or "")
                            for r in rows)
    c.pop("", None)
    return c


def _sample(rows):
    """One verbatim, contact-free specimen line for the `quote`.

    Built here rather than in the extractor so the exact string the ledger will
    carry is a literal value in the payload on disk. normalize.py verifies a
    quote as a substring of the fetched payload, and a string assembled
    downstream from two payload fields is NOT one — item_strings() joins the
    item's values in dict order with single spaces, which is a different
    sequence of bytes than "NAZEV DOPLNEK — DUVOD". Composing it at fetch time
    makes the substring test true by construction rather than by luck.
    """
    best = None
    for r in rows:
        duvod = contact_free(r.get("DUVOD_PRERUSENI_UKONCENI") or "")
        if not duvod:
            continue
        name = contact_free(f"{r.get('NAZEV', '')} {r.get('DOPLNEK', '')}".strip())
        cand = f"{name} — {duvod}"
        if len(cand) <= 300 and (best is None or len(cand) > len(best)):
            best = cand
    if best:
        return best
    for r in rows:
        name = contact_free(f"{r.get('NAZEV', '')} {r.get('DOPLNEK', '')}".strip())
        if name:
            return name[:300]
    return None


def aggregate(rows, validity):
    """Rows -> the monthly aggregate items. AGGREGATION BEFORE MATERIALITY."""
    ym = validity[:7]
    out = []

    # ---- FAMILY A: STOCK. Supply interrupted right now, by ATC group. --------
    # `POSLEDNI_PLATNE_HLASENI == "ANO"` is the source's own flag for "this is
    # the notice currently in force for this presentation"; without it the same
    # medicine is counted once per notice it has ever attracted since 2010.
    live = [r for r in rows
            if (r.get("POSLEDNI_PLATNE_HLASENI") or "").strip() == "ANO"
            and (r.get("TYP_OZNAMENI") or "").strip() == "preruseni"]
    by_group = collections.defaultdict(list)
    for r in live:
        by_group[(r.get("ATC") or "?")[:1] or "?"].append(r)
    for g, rs in sorted(by_group.items()):
        no_date = [r for r in rs if not (r.get("TERMIN_OBNOVENI") or "").strip()]
        reasons = _reasons(rs)
        out.append({
            "latest_notice": max((iso(r.get("DATUM_HLASENI")) or "" for r in rs),
                                 default=""),
            "kind": "preruseni",
            "atc1": g,
            "atc1_label": ATC1.get(g, "unclassified"),
            "period": ym,
            "validity": validity,
            "presentations": len(rs),
            "distinct_atc": len({r.get("ATC") for r in rs if r.get("ATC")}),
            "no_restock_date": len(no_date),
            "reasons": [{"duvod": k, "n": v} for k, v in reasons.most_common(5)],
            "example": _sample(rs),
            "url": "https://opendata.sukl.cz/?q=katalog/"
                   "hlaseni-o-uvedeni-preruseni-ukonceni-obnoveni-dodavek-"
                   "leciveho-pripravku-na-trh",
        })

    # ---- FAMILY B: FLOW. Permanent market exits notified this month. ---------
    exits = [r for r in rows
             if (r.get("TYP_OZNAMENI") or "").strip() == "ukonceni"
             and (iso(r.get("DATUM_HLASENI")) or "")[:7] == ym]
    if exits:
        reasons = _reasons(exits)
        out.append({
            "latest_notice": max((iso(r.get("DATUM_HLASENI")) or "" for r in exits),
                                 default=""),
            "kind": "ukonceni",
            "atc1": None,
            "atc1_label": None,
            "period": ym,
            "validity": validity,
            "presentations": len(exits),
            "distinct_atc": len({r.get("ATC") for r in exits if r.get("ATC")}),
            "no_restock_date": len(exits),   # a termination never has one
            "reasons": [{"duvod": k, "n": v} for k, v in reasons.most_common(5)],
            "example": _sample(exits),
            "url": "https://opendata.sukl.cz/?q=katalog/"
                   "hlaseni-o-uvedeni-preruseni-ukonceni-obnoveni-dodavek-"
                   "leciveho-pripravku-na-trh",
        })
    return out


def read_zip(path, out):
    zf = assert_zip(path)
    rows = read_csv(zf, MEMBER_DATA, REQUIRED_COLUMNS)
    if len(rows) < CONTRACT_MIN_ROWS:
        raise ContractViolation(
            f"{len(rows)} rows in {MEMBER_DATA} — below the {CONTRACT_MIN_ROWS} "
            "floor; this register only grows, so a file this short is a wrong body")
    types = collections.Counter((r.get("TYP_OZNAMENI") or "").strip() for r in rows)
    unknown = set(types) - KNOWN_TYPES - {""}
    if unknown:
        raise ContractViolation(
            f"unknown TYP_OZNAMENI values {sorted(unknown)} — the source's "
            "vocabulary changed; scoring and aggregation are not safe to run blind")
    if not types.get("preruseni"):
        raise ContractViolation(
            "no `preruseni` notices anywhere in the file — the one thing this "
            "feed exists to observe is absent, which is a wrong body, not news")

    validity = None
    if MEMBER_VALIDITY in [i.filename for i in zf.infolist()]:
        vr = read_csv(zf, MEMBER_VALIDITY)
        if vr:
            validity = iso(list(vr[0].values())[0])
    if not validity:
        # Fall back to the newest notice date rather than to our own clock: a
        # synthesized "as of" reads as evidence and would silently mis-date every
        # aggregate if the validity member ever disappears.
        validity = max((iso(r.get("DATUM_HLASENI")) or "" for r in rows), default="")
    if not validity:
        raise ContractViolation("no dataset validity date and no parsable notice dates")

    items = aggregate(rows, validity)
    doc = {
        "feed": "sukl",
        "source_interface": "opendata.sukl.cz/soubory/MR/mr.zip",
        "validity": validity,
        "period": validity[:7],
        "rows_in_file": len(rows),
        "notice_types": dict(types),
        "fetched": len(items),
        "items": items,
    }
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False)
    return doc


# --------------------------------------------------------------------------
# 3. THE normalize.py EXTRACTOR
# --------------------------------------------------------------------------
#
# HAND-OFF (scripts/normalize.py is not this worker's file). Two lines:
#
#     from sukl_extract import extract_sukl        # sys.path[0] is scripts/
#     EXTRACTORS = {…, "sukl": extract_sukl, …}
#
# WITHOUT THAT EDIT THIS FEED IS BORN SCRIPTED-SILENT AND LOOKS FINE.
# normalize.py:957 does `extractor = EXTRACTORS.get(feed_key)` and :962-963
# `if not extractor: break` — no log line, no manifest note. The contract check
# has already passed by then, so the run records ok=1, items_fetched=15,
# items_kept=0 and moves on. That is the exact shape of the failure that sat on
# five feeds for weeks. There is no key `sukl` in EXTRACTORS today.

def _past(iso_date, today):
    """`iso_date` guaranteed strictly earlier than `today`, or None.

    See the long note at `urgency_date` below for why a strictly-past anchor is
    what routes urgency to a model instead of to arithmetic.
    """
    if not iso_date:
        return None
    yesterday = (today - datetime.timedelta(days=1)).isoformat()
    return iso_date if iso_date < today.isoformat() else yesterday


def extract_sukl(item, payload_key, today):
    """Signature and return shape are normalize.py's, not ours."""
    period = item.get("period")
    kind = item.get("kind")
    if not period or not kind:
        return None
    atc = item.get("atc1")
    rid = f"sukl-{period}-{kind}-{atc}" if atc else f"sukl-{period}-{kind}"
    n = item.get("presentations") or 0
    label = item.get("atc1_label")
    reasons = item.get("reasons") or []
    top = reasons[0]["duvod"] if reasons else None

    if kind == "preruseni":
        native = (f"{n} léčivých přípravků skupiny ATC {atc} "
                  f"({label}) má přerušené dodávky")
        notes = (f"SÚKL MR dataset, platnost {item.get('validity')}: "
                 f"POSLEDNI_PLATNE_HLASENI=ANO & TYP_OZNAMENI=preruseni, ATC-1 {atc}; "
                 f"{n} balení, {item.get('distinct_atc')} odlišných ATC kódů; "
                 f"bez TERMIN_OBNOVENI: {item.get('no_restock_date')}; "
                 + "; ".join(f"{r['duvod']}: {r['n']}" for r in reasons))
    else:
        native = f"{n} léčivých přípravků s ukončenými dodávkami ohlášeno v {period}"
        notes = (f"SÚKL MR dataset, platnost {item.get('validity')}: "
                 f"TYP_OZNAMENI=ukonceni, DATUM_HLASENI v {period}; {n} balení, "
                 f"{item.get('distinct_atc')} odlišných ATC kódů; "
                 + "; ".join(f"{r['duvod']}: {r['n']}" for r in reasons))

    return {
        "id": rid,
        "source": "sukl",
        "evidence_type": "demand",
        "url": item.get("url"),
        # The dataset's OWN validity date, never our clock — the aggregate is a
        # statement about the file, and it must be datable to the file.
        "date": item.get("validity"),
        "title_native": native,
        "entity_native": "Státní ústav pro kontrolu léčiv",
        # Mechanical, not a judgement: the source is the state medicines agency
        # and every row is a medicine. Set here for the same reason extract_ted
        # sets sector from CPV — leaving it None would put `sector` in `_needs`
        # and pay a model to answer a question with one possible answer.
        "sector": "health",
        "money_eur": None,
        "money_note": "",
        # THE ROUTING FIELD FOR URGENCY, AND `None` IS THE WRONG VALUE FOR IT.
        # This looked right and was measured wrong. score_urgency() returns
        # 0 for a falsy date and None only for a PAST one (normalize.py:
        # `if not event_date: return 0` … `if m < 0: return None`), and
        # `urgency_pending` — the thing that puts `scores.urgency` into `_needs`
        # — is set from `u is None`. So `urgency_date: None` did not hand
        # urgency to a model at all: it silently STAMPED urgency 0 on every
        # record and never asked. Measured on the first staged run: 15 of 15
        # SÚKL records carried `urgency_pending: false` and no `scores.urgency`
        # in `_needs`.
        #
        # A live shortage has no future event to count down to, so the anchor is
        # the newest notice in the group — a real date from the data. It is
        # clamped to strictly before `today` so score_urgency() cannot fall into
        # its `m < 6 -> 3` branch and assert active enforcement by arithmetic;
        # that is the model's call under INGEST.md §3b. Clamping falsifies
        # nothing published: `urgency_date` is not in normalize.py's
        # LEDGER_ALLOWLIST and never reaches a record.
        "urgency_date": _past(item.get("latest_notice"), today),
        "quote_parts": [p for p in (item.get("example"), top) if p],
        "excerpt": (f"{native}. Nejčastější uvedený důvod: {top}." if top
                    else f"{native}."),
        "notes": notes,
    }


# --------------------------------------------------------------------------
# 4. CLI — driven by scripts/fetch_sukl.sh
# --------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("read", help="ZIP -> <raw>/sukl-<validity>.json aggregates")
    r.add_argument("zip")
    r.add_argument("out")
    c = sub.add_parser("check", help="run the source contract against a file and exit")
    c.add_argument("zip")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "read":
            doc = read_zip(a.zip, a.out)
            print(json.dumps({k: v for k, v in doc.items() if k != "items"},
                             ensure_ascii=False))
            return 0
        zf = assert_zip(a.zip)
        rows = read_csv(zf, MEMBER_DATA, REQUIRED_COLUMNS)
        print(json.dumps({"ok": True, "rows": len(rows)}))
        return 0
    except ContractViolation as e:
        print(f"CONTRACT VIOLATION: {e}", file=sys.stderr)
        return 65


if __name__ == "__main__":
    sys.exit(main())
