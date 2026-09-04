#!/usr/bin/env python3
"""
ms21_index.py — the MS2021+ approved-project export, reduced to a QUERYABLE
INDEX OF PUBLIC BUYERS. Stdlib only. Reader + MODE-A guard for
scripts/fetch_ms21.sh, and the entry points scripts/ms21_selftest.py drives.

WHAT THE SOURCE IS
==================
`https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml` — MMR's open-data export
of every approved 2021-27 EU-cofinanced project in Czechia. CC BY 4.0,
AUTOR="Ministerstvo pro místní rozvoj". MEASURED 2026-09-04: HTTP 200,
146,410,196 bytes, 40,988 <PRJ> records, default namespace
`https://ms21xsd.mssf.cz/OpenData/v_1`.

Each <PRJ> carries something almost nothing else in this repo's sources does:
the beneficiary's OWN <PROBLEM> statement, next to the money that was approved
against it and the IČO of who spent it. That is the register's weakest
question — WHO PAID HOW MUCH, and what problem did that buyer say it solved —
answerable in one grep.

WHY A LOOKUP TABLE AND NOT A FEED
=================================
40,988 projects each carrying real money would flood `data/signals/**` (16,237
records today) and nearly all of them would pass materiality. That is exactly
the trap `smlouvy` is parked for, in data/feeds.json's own words: "a PER-ITEM
feed whose items each score money 1 or 0 … walks straight into the trap
CONVENTIONS.md names for `hiring`". The fix there is aggregation before
materiality; the fix HERE is to not make it evidence at all. This is the
`data/lookup/` tree (CONVENTIONS.md "Lookup layer"): committed, never pruned,
no evidence type, no score, not walked by db.py or the build gate. It gets NO
row in data/feeds.json, because it is not a feed.

WHY iterparse AND NOT ET.parse
==============================
The file is 146 MB; ET.parse builds the whole tree in memory (~1.5 GB for this
document) before the first row is written. iterparse streams it, and root.clear()
after each </PRJ> keeps the retained set at one project. Peak RSS measured under
60 MB.

WHICH BENEFICIARIES ARE "PUBLIC" — MEASURED, NOT ASSUMED
========================================================
The filter is ZAD/HPF, the ČSÚ legal-form code. Counts and the example names
behind each decision are from the live file, 2026-09-04:

  ADMITTED (26,048 rows)
    331 16,237  příspěvková organizace — "Nemocnice Tišnov, p.o.", "Správa a
                údržba silnic Plzeňského kraje". Schools, hospitals, road
                authorities: the single biggest public buyer population here.
    801  6,826  obec/město — "Město Hranice", "Obec Žichlínek"
    641    742  školská právnická osoba — SEE THE CAVEAT BELOW
    804    628  kraj — "Jihočeský kraj", "Olomoucký kraj"
    601    387  veřejná vysoká škola — "Masarykova univerzita"
    325    378  organizační složka státu — "Ministerstvo vnitra", "Krajské
                ředitelství policie Jihomoravského kraje"
    332    309  státní příspěvková organizace — "Fakultní nemocnice Plzeň"
    771    241  dobrovolný svazek obcí — "Mikroregion Šternbersko"
    661    126  veřejná výzkumná instituce — "Ústav fyziky plazmatu AV ČR"
    301     90  státní podnik — "Povodí Labe, s.p."
    811     50  městská část — "Městská část Praha 4"
    352     24  státní organizace — "Správa železnic"
    382     10  státní fond — "Státní fond životního prostředí ČR"

  REFUSED, and each for a stated reason — this is where an earlier list of
  "public forms" was wrong and the names in the file say so:
    100    941  podnikající fyzická osoba — the measured names are people:
                "Zdeněk Jaroš", "Martin Fabián Rusek". A sole trader is not a
                public body, whatever the grant programme.
    141    976  obecně prospěšná společnost and 722 (428) evidovaná církevní
                právnická osoba — "Magdaléna, o.p.s.", "Oblastní charita
                Jičín". Nonprofits and church bodies are CONTRACTORS for public
                money, not the buyer of it. Admitting them would make "public"
                mean two things at once, which is CLAUDE.md rule 1.
    112/121/111/113/205/932  business forms — the counterparty side.
    706/161/736/745/751/…    spolky, ústavy, chambers, unions.
    P01…P54   24  Polish partner bodies in the Interreg programmes ("Gmina
                Radków", "Powiat Zgorzelecki"). Public, and not Czech; a
                Czech register citing them as a Czech buyer would be wrong.

  THE ONE MIXED FORM, stated out loud: 641 (školská právnická osoba) is a
  legal form for SCHOOLS, and its founder may be a municipality, a private
  person or a diocese — "Základní škola ZaHRAda", "Biskupské gymnázium v
  Ostravě". It is admitted because the school delivers a public service on
  public money, but a record citing a 641 row must name the founder and must
  not call it "the state". Every row carries `legal_form`, so the caller can
  see which one it got.

THE MONEY IS IN THE T=1 BLOCK, AND THE OTHER ONE IS NOT THE SAME NUMBER
=======================================================================
Every <PRJ> carries two <PF> financial blocks, distinguished only by <T>.
MEASURED over the 26,048 public rows: both blocks are present on 100% of them,
and CV (total cost) DIFFERS BETWEEN THEM ON 553. So "take whichever PF comes
first" is not a harmless shortcut — it is 553 wrong prices, in a tool whose only
job is prices. This reader takes T=1 and, when there is no T=1 block, writes NO
money at all rather than silently falling back to T=0.

WHAT THE PROBLEM FIELD ACTUALLY HOLDS (the surprise, measured)
==============================================================
<PROBLEM> is present on all 40,988 records, but on public bodies it is a
NON-ANSWER more often than not: of 26,048 rows, 7,885 say "-" and 7,328 say
"nerelevantní" — 15,213 placeholders, 58%. Only 10,835 carry a real statement.
Writing "-" into a field called `problem` would be the same defect as an empty
`quote`: the shape that looks present and says nothing. So a placeholder is
OMITTED (CONVENTIONS.md: optional keys are omitted when empty, never written as
"" or null) and counted in the summary. The row survives, because it still
answers the money half of the question.

Usage:
    python3 scripts/ms21_index.py guard <file.xml>
    python3 scripts/ms21_index.py index <file.xml> --out data/lookup/ms21-public-projects.jsonl
"""
import argparse
import json
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

NS = "https://ms21xsd.mssf.cz/OpenData/v_1"
Q = "{%s}" % NS
DATASET_URL = "https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml"

# See the header. Set, not a range test: a legal-form code is a label, and
# "everything above 300" would admit the next form MMR invents without anyone
# looking at what it names.
PUBLIC_FORMS = frozenset(
    ("301", "325", "331", "332", "352", "382", "601", "641", "661", "771",
     "801", "804", "811")
)

# ── contact-shaped text is cut here, at the reader ──────────────────────────
# COPIED VERBATIM from scripts/normalize.py (EMAIL_RE / PHONE_RE, "The second
# layer" block), not imported: normalize.py is the ledger's gate and this file
# has no business being on its import graph — data/lookup/ is not a ledger and
# must never grow a dependency that makes it look like one. Same call
# tacr_extract.py made and for the same reason. If normalize.py's patterns
# change, change them here too; the selftest proves this copy still bites.
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)

# Diacritic-folded placeholder problem statements. Kept as an explicit set
# rather than a length test: "nekvalitní pitnou vodu." is 23 characters and is
# a real answer, while "nerelevantní" is 12 and is not.
PLACEHOLDERS = frozenset(("-", "--", "---", "nerelevantni", "n/a", "na", "x", "xxx"))

PROBLEM_MAX = 600
GOAL_MAX = 300
HEAD_BYTES = 4096
_WS = re.compile(r"\s+")
_LETTER = re.compile(r"[^\W\d_]", re.UNICODE)


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
    """
    Truncate at a WORD boundary and mark it. Cutting mid-word produces text a
    reader silently mis-reads ('digitaliz'), and an unmarked truncation is a
    quote you cannot trust — this index is read by a pass that writes citations.
    """
    if len(s) <= limit:
        return s
    cut = s[:limit]
    sp = cut.rfind(" ")
    if sp > limit * 0.6:
        cut = cut[:sp]
    return cut.rstrip(" ,;:.") + "…"


def is_placeholder(s):
    """'-' and 'nerelevantní' are not problem statements. Neither is punctuation."""
    f = fold(s).strip().rstrip(".")
    return (not f) or (f in PLACEHOLDERS) or (not _LETTER.search(f))


def money(text):
    """
    '1564798.35' -> 1564798 (whole crowns, rounded).

    Halves are dropped on purpose: this index feeds `amount_czk` on a price
    source and a CZK-heller precision claim on a 4-million-crown grant is false
    precision. Returns None — never 0 — when the field is absent, because
    CONVENTIONS.md makes `amount_czk: 0` a REAL receipt ("a free incumbent sets
    the price"), so a missing number must not arrive wearing that meaning.
    """
    t = (text or "").strip().replace(",", ".")
    if not t:
        return None
    try:
        return int(round(float(t)))
    except ValueError:
        return None


def isodate(text):
    """'2024-02-28T00:00:00.000+01:00' -> '2024-02-28'."""
    t = (text or "").strip()
    return t[:10] if len(t) >= 10 and t[4] == "-" and t[7] == "-" else ""


# ──────────────────────────────────────────────────────────────────────────────
# MODE A — the source contract, evaluated on the FIRST BYTES, before parsing
# ──────────────────────────────────────────────────────────────────────────────
_ROOT_RE = re.compile(r"<\s*(?:[A-Za-z_][\w.-]*:)?EXPORT\b([^>]*)>", re.S)
_HTMLISH_RE = re.compile(r"<\s*(?:!doctype\s+html|html|head|body|form)\b", re.I)


def guard_head(head_bytes):
    """
    Return None when the head is the MS21 export, else a REASON string.

    A 200 proves the transfer, not the body. This host is IIS behind a proxy;
    a maintenance page, an SSO redirect landing page or a WAF block all arrive
    as 200 text/html, and 146 MB of nothing parses to zero rows and looks like
    a healthy empty dataset. The refusal happens on the first 4 KB so the
    fetcher never hands a wrong body to the parser at all.
    """
    if not head_bytes:
        return "empty body"
    head = head_bytes.decode("utf-8", "replace")
    m = _ROOT_RE.search(head)
    if not m:
        h = _HTMLISH_RE.search(head)
        if h:
            return "body is HTML (%r), not the <EXPORT> element" % h.group(0)
        return "no <EXPORT> root element in the first %d bytes" % len(head_bytes)
    if _HTMLISH_RE.search(head[:m.start()]):
        return "HTML markup precedes <EXPORT> — this is a page, not the export"
    attrs = m.group(1)
    if NS not in attrs:
        return "<EXPORT> declares no %s namespace (attrs: %s)" % (NS, collapse(attrs)[:160])
    if not re.search(r'xmlns(?::[\w.-]+)?\s*=\s*["\']%s["\']' % re.escape(NS), attrs):
        return "%s appears in <EXPORT> but not as an xmlns declaration" % NS
    return None


def guard_file(path):
    with open(path, "rb") as fh:
        return guard_head(fh.read(HEAD_BYTES))


def root_meta(path):
    """LICENCE / AUTOR / DATE off the root tag — the provenance a citation needs."""
    with open(path, "rb") as fh:
        head = fh.read(HEAD_BYTES).decode("utf-8", "replace")
    m = _ROOT_RE.search(head)
    out = {}
    if m:
        for k in ("LICENCE", "AUTOR", "DATE", "FILE"):
            a = re.search(r'\b%s\s*=\s*"([^"]*)"' % k, m.group(1))
            if a:
                out[k.lower()] = a.group(1)
    return out


# ──────────────────────────────────────────────────────────────────────────────
# The index pass
# ──────────────────────────────────────────────────────────────────────────────
# Field order is fixed and the writer uses it: a lookup rewritten in place every
# run must produce a byte-stable diff when nothing changed, or `git status`
# stops being a signal that the source moved.
FIELDS = ("kod", "name", "problem", "goal", "ico", "beneficiary", "legal_form",
          "region", "district", "municipality", "total_czk", "own_czk",
          "eu_czk", "start", "end", "call_id", "theme")


def row_from_prj(prj):
    """One <PRJ> -> one index row, or None when the beneficiary is not public."""
    zad = prj.find(Q + "ZAD")
    if zad is None:
        return None
    form = (zad.findtext(Q + "HPF") or "").strip()
    if form not in PUBLIC_FORMS:
        return None

    adr = zad.find(Q + "ADR")

    def a(tag):
        return scrub(adr.findtext(Q + tag)) if adr is not None else ""

    # THE T=1 BLOCK, and no fallback. See the header: T=0 disagrees on 553 rows.
    pf = None
    for cand in prj.findall(Q + "PF"):
        if (cand.findtext(Q + "T") or "").strip() == "1":
            pf = cand
            break

    problem_raw = scrub(prj.findtext(Q + "PROBLEM"))
    oi = prj.find(Q + "OI")

    row = {
        "kod": collapse(prj.findtext(Q + "KOD")),
        "name": clip(scrub(prj.findtext(Q + "NAZ")), 300),
        # Omitted, not "", when the beneficiary wrote a placeholder.
        "problem": "" if is_placeholder(problem_raw) else clip(problem_raw, PROBLEM_MAX),
        "goal": clip(scrub(prj.findtext(Q + "CIL")), GOAL_MAX),
        "ico": collapse(zad.findtext(Q + "IC")),
        "beneficiary": scrub(zad.findtext(Q + "NAZ")),
        "legal_form": form,
        "region": a("KNAZEV"),
        "district": a("OKNAZEV"),
        "municipality": a("OBNAZEV"),
        "total_czk": money(pf.findtext(Q + "CV")) if pf is not None else None,
        "own_czk": money(pf.findtext(Q + "S")) if pf is not None else None,
        "eu_czk": money(pf.findtext(Q + "EU")) if pf is not None else None,
        # DZRSKUT/DURSKUT are the ACTUAL dates. DURPRED (the planned end) is
        # NOT folded in as a fallback: one field carrying "when it ended" and
        # "when it was meant to end" is CLAUDE.md rule 1, and 13,491 of these
        # rows have no actual end because the project is still running.
        "start": isodate(prj.findtext(Q + "DZRSKUT")),
        "end": isodate(prj.findtext(Q + "DURSKUT")),
        "call_id": collapse(prj.findtext(Q + "ID_VYZVA")),
        "theme": clip(scrub(oi.findtext(Q + "KN")), 200) if oi is not None else "",
    }
    # Empty is omitted, never written as "" or null (CONVENTIONS.md).
    return {k: row[k] for k in FIELDS if row[k] not in (None, "")}


def build_index(xml_path, out_path):
    """Stream the export, write the JSONL, return a summary dict."""
    stats = {"projects": 0, "public": 0, "placeholder_problem": 0,
             "no_pf1": 0, "no_money": 0, "no_theme": 0, "contact_cut": 0,
             "by_form": {}}
    tmp = out_path + ".part"
    d = os.path.dirname(out_path)
    if d:
        os.makedirs(d, exist_ok=True)

    root = None
    with open(tmp, "w", encoding="utf-8") as out:
        for event, el in ET.iterparse(xml_path, events=("start", "end")):
            if event == "start":
                if root is None:
                    root = el
                continue
            if el.tag != Q + "PRJ":
                continue
            stats["projects"] += 1
            row = row_from_prj(el)
            if row is not None:
                stats["public"] += 1
                form = row.get("legal_form", "?")
                stats["by_form"][form] = stats["by_form"].get(form, 0) + 1
                if "problem" not in row:
                    stats["placeholder_problem"] += 1
                if "total_czk" not in row:
                    stats["no_money"] += 1
                if "theme" not in row:
                    stats["no_theme"] += 1
                if any(EMAIL_RE.search(t) or PHONE_RE.search(t)
                       for t in (el.findtext(Q + "PROBLEM") or "",
                                 el.findtext(Q + "CIL") or "")):
                    stats["contact_cut"] += 1
                out.write(json.dumps(row, ensure_ascii=False, sort_keys=False) + "\n")
            # One project retained at a time. Clearing the element is not
            # enough — the root keeps every cleared child, which is 40,988
            # empty elements by the end.
            el.clear()
            if root is not None:
                root.clear()

    os.replace(tmp, out_path)
    stats["bytes"] = os.path.getsize(out_path)
    return stats


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    sub = ap.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("guard", help="MODE-A: refuse a body that is not the MS21 export")
    g.add_argument("xml")

    i = sub.add_parser("index", help="stream the export into data/lookup/")
    i.add_argument("xml")
    i.add_argument("--out", default="data/lookup/ms21-public-projects.jsonl")
    # The owner's stop rule: data/lookup/ is committed and never pruned, so a
    # runaway index is a permanent repo weight problem, not a disk one.
    i.add_argument("--max-mb", type=float, default=30.0,
                   help="refuse to leave an index larger than this (default 30)")

    args = ap.parse_args(argv)

    if args.cmd == "guard":
        reason = guard_file(args.xml)
        if reason:
            print("MODE-A REFUSED: %s" % reason, file=sys.stderr)
            return 65
        meta = root_meta(args.xml)
        print(json.dumps(meta, ensure_ascii=False))
        return 0

    reason = guard_file(args.xml)
    if reason:
        print("MODE-A REFUSED: %s" % reason, file=sys.stderr)
        return 65
    stats = build_index(args.xml, args.out)
    stats["out"] = args.out
    stats["mb"] = round(stats["bytes"] / 1048576.0, 2)
    stats.update(root_meta(args.xml))
    print(json.dumps(stats, ensure_ascii=False, sort_keys=True))
    if stats["public"] == 0:
        print("ms21_index: ZERO public rows from %d projects — the filter or the "
              "source shape changed; not a healthy empty index."
              % stats["projects"], file=sys.stderr)
        return 66
    if stats["bytes"] > args.max_mb * 1048576:
        print("ms21_index: index is %.1f MB, over the %.0f MB ceiling for a "
              "COMMITTED, NEVER-PRUNED tree. Left on disk, not blessed — trim "
              "PROBLEM_MAX or narrow PUBLIC_FORMS before committing it."
              % (stats["mb"], args.max_mb), file=sys.stderr)
        return 67
    return 0


if __name__ == "__main__":
    sys.exit(main())
