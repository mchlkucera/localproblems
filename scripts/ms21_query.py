#!/usr/bin/env python3
"""
ms21_query.py — the tool the MATCH and SWEEP passes actually run. Stdlib only.

THE QUESTION IT ANSWERS
=======================
"Who in Czechia has already PAID for this, how much, and what did they say the
problem was?" The register's weakest claim is money: `pipeline/MATCH.md` scores
MONEY as "is public budget nearby?", which never says whose pocket it left.
data/CONVENTIONS.md's `type: price` receipt exists to fix that and needs four
things — payer, amount_czk, unit, basis. This tool hands you all four, plus the
buyer's own problem statement, from one grep over
data/lookup/ms21-public-projects.jsonl (26,048 public-body projects, built by
scripts/ms21_index.py).

    python3 scripts/ms21_query.py --keyword dokumentace --min-czk 5000000
    python3 scripts/ms21_query.py --keyword kódování --region Jihomoravský
    python3 scripts/ms21_query.py --ico 00292311 --json

Matching is case- AND diacritic-insensitive over name + problem + goal + theme,
because a MATCH pass types "kodovani" and the register is in Czech; a query tool
that needs the right háčky to find a 40-million-crown contract is a tool nobody
uses twice.

RESULTS ARE ORDERED BY MONEY, LARGEST FIRST
===========================================
Not by relevance score and not by date. The question is who pays MOST; a
ranked-by-text-relevance list buries the 800-million-crown ministry project
under twelve village ones that repeat the keyword more often per character.

THE CITATION LINE, AND WHY ITS URL IS A CONSTANT
================================================
Every hit prints a ready `sources[]` entry. Its `url` is the WHOLE-DATASET url,
identical on every project, and that is BY DESIGN — there is no per-project
permalink in this export. data/CONVENTIONS.md already blesses the shape: "`coi`
/ `sukl` / `mpsv` emit whole aggregate families under one constant dataset url
BY DESIGN. Merging on url alone would delete 504 real records." The project KOD
in `note` is what makes the row identifiable. The note says so in-line, so the
next person to run a dedupe pass does not "fix" it.
"""
import argparse
import json
import os
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_INDEX = os.path.join(ROOT, "data", "lookup", "ms21-public-projects.jsonl")
DATASET_URL = "https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml"
SOURCE_NAME = "MS2021+ — seznam schválených operací (MMR, CC BY 4.0)"

# The note every citation carries. It exists to stop a future dedupe pass from
# "fixing" the constant url — see the module docstring.
NOTE_TMPL = (
    "MS2021+ approved-project open data, project {kod}"
    "{call} — beneficiary's own PROBLEM statement and the approved total. "
    "The url is the WHOLE DATASET and is the same on every project: this export "
    "has no per-project permalink, and a constant dataset url is the shape "
    "coi/sukl/mpsv already use by design (data/CONVENTIONS.md). The KOD here is "
    "the identifying key — do not 'fix' the url to a per-project link, there is none."
)


def fold(s):
    """Case- and diacritic-insensitive form. 'Kódování' -> 'kodovani'."""
    return "".join(c for c in unicodedata.normalize("NFKD", str(s or ""))
                   if not unicodedata.combining(c)).casefold()


def czk(n):
    """1234567 -> '1 234 567'. Grouping done by hand: locale grouping would
    depend on the shell that ran this, and LC_NUMERIC=C is the house rule."""
    if n is None:
        return "?"
    s = str(abs(int(n)))
    out = []
    while len(s) > 3:
        out.insert(0, s[-3:])
        s = s[:-3]
    out.insert(0, s)
    return ("-" if n < 0 else "") + " ".join(out)


def load(path):
    rows = []
    with open(path, "r", encoding="utf-8") as fh:
        for ln, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError as e:
                print("ms21_query: %s:%d is not JSON (%s)" % (path, ln, e),
                      file=sys.stderr)
    return rows


def haystack(r):
    return fold(" ".join((r.get("name", ""), r.get("problem", ""),
                          r.get("goal", ""), r.get("theme", ""))))


def citation(r):
    """
    The `sources[]` entry a record should paste. Five fields are REQUIRED on a
    price source (data/CONVENTIONS.md): payer, amount_czk, unit, basis, date.

    `date` is the project's ACTUAL START — when the money was committed against
    the stated problem. 5,070 of the 26,048 rows report no actual start and no
    actual end, and those get an EMPTY date on purpose: an empty one fails
    scripts/check-records.py loudly, where a substituted export-publication date
    would pass the build while claiming a commitment that never happened on
    that day.

    `basis: signed-contract` — an approved MS2021+ operation is a signed grant
    agreement (rozhodnutí/smlouva o poskytnutí dotace), not a list price and not
    a tender line. `unit: one-off` — a project total, not a rate.
    """
    return {
        "type": "price",
        "url": DATASET_URL,
        "name": SOURCE_NAME,
        "note": NOTE_TMPL.format(
            kod=r.get("kod", "?"),
            call=(", výzva %s" % r["call_id"]) if r.get("call_id") else ""),
        "date": r.get("start") or r.get("end") or "",
        "payer": r.get("beneficiary", ""),
        "amount_czk": r.get("total_czk"),
        "unit": "one-off",
        "basis": "signed-contract",
    }


def human(r, i, out):
    eu = r.get("eu_czk")
    total = r.get("total_czk")
    # The remainder is ARITHMETIC and is labelled as such. It is NOT `own_czk`:
    # that field is the export's <S> element (own/private share), which MEASURED
    # 2026-09-04 is present on only 510 of 26,048 public rows — public-body
    # projects book their non-EU part under CNV instead. Writing the subtraction
    # into own_czk would be one field carrying two different questions.
    rest = (total - eu) if (isinstance(total, int) and isinstance(eu, int)) else None
    loc = " · ".join(x for x in (r.get("municipality"), r.get("district") and
                                 "okres " + r["district"], r.get("region")) if x)
    out.append("[%d] %s · IČO %s · právní forma %s"
               % (i, r.get("beneficiary", "?"), r.get("ico", "?"),
                  r.get("legal_form", "?")))
    if loc:
        out.append("    %s" % loc)
    line = "    %s Kč celkem" % czk(total)
    if eu is not None:
        line += " · z toho EU %s" % czk(eu)
    if rest is not None:
        line += " · mimo EU %s (dopočet)" % czk(rest)
    if r.get("own_czk") is not None:
        line += " · vlastní/soukromý podíl %s" % czk(r["own_czk"])
    out.append(line)
    out.append("    %s%s · %s → %s"
               % (r.get("kod", "?"),
                  (" · výzva %s" % r["call_id"]) if r.get("call_id") else "",
                  r.get("start") or "(bez data zahájení)",
                  r.get("end") or "(běží / bez data ukončení)"))
    out.append("    projekt: %s" % r.get("name", "?"))
    if r.get("theme"):
        out.append("    téma:    %s" % r["theme"])
    if r.get("problem"):
        out.append("    problém (slovy příjemce): %s" % r["problem"])
    else:
        # 15,214 rows say "-" or "nerelevantní"; ms21_index.py omits those
        # rather than write a placeholder into a field called `problem`.
        out.append("    problém: — příjemce žádný neuvedl (v exportu \"-\" / "
                   "\"nerelevantní\"); tento řádek dokládá jen kdo a kolik zaplatil")
    cite = citation(r)
    if not cite["date"]:
        out.append("    POZOR: projekt neuvádí skutečné datum zahájení ani ukončení — "
                   "`date` je prázdné a build to odmítne. Doplňte datum z výzvy, "
                   "nebo tento projekt necitujte jako price source.")
    # THE SUBJECT TEST, and it is the one that stops this tool being misused.
    # An approved total is a price for WHAT THAT PROJECT BOUGHT. Most rows here
    # are capital works — a police building at 3.25bn, a hospital pavilion at
    # 2.17bn — and pasting such a figure onto a software record would claim a
    # buyer priced something it never bought. A price receipt is only honest
    # where the project's SUBJECT is the record's product or the manual
    # equivalent of it. Printed on every hit because the citation JSON below is
    # copy-pasteable and nothing downstream can re-check the judgement.
    out.append("    NEŽ TOHLE POUŽIJETE: cituj jen tehdy, když PŘEDMĚT projektu je "
               "produkt záznamu (nebo jeho ruční ekvivalent). Stavba pavilonu není "
               "cena za software. Jinak je to peníze v cizí kapse — a záznam má "
               "zůstat bez ceny.")
    out.append("    cite: %s" % json.dumps(cite, ensure_ascii=False))
    out.append("")


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Who paid how much, and what problem did they say it solved.",
        epilog="Index built by: scripts/ms21_index.py index <export.xml>")
    ap.add_argument("--keyword", help="case- and diacritic-insensitive text over "
                                      "name + problem + goal + theme")
    ap.add_argument("--region", help="substring of the kraj name, diacritic-insensitive")
    ap.add_argument("--min-czk", type=float, default=None,
                    help="drop projects whose approved total is below this")
    ap.add_argument("--ico", help="exact IČO of the beneficiary")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--json", action="store_true", dest="as_json",
                    help="machine output: one JSON array, each hit + its citation")
    ap.add_argument("--index", default=DEFAULT_INDEX)
    args = ap.parse_args(argv)

    if not os.path.isfile(args.index):
        print("ms21_query: no index at %s — build it with:\n"
              "  scripts/fetch_ms21.sh data/raw/$(date +%%F)" % args.index,
              file=sys.stderr)
        return 2
    if not any((args.keyword, args.region, args.ico, args.min_czk)):
        print("ms21_query: give at least one filter (--keyword / --region / "
              "--ico / --min-czk). Printing the first 20 of 26k rows answers "
              "nobody's question.", file=sys.stderr)
        return 2

    kw = fold(args.keyword) if args.keyword else None
    reg = fold(args.region) if args.region else None
    hits = []
    for r in load(args.index):
        if kw and kw not in haystack(r):
            continue
        if reg and reg not in fold(r.get("region", "")):
            continue
        if args.ico and r.get("ico") != args.ico:
            continue
        if args.min_czk is not None and (r.get("total_czk") or 0) < args.min_czk:
            continue
        hits.append(r)

    # Money first. A missing total sorts last rather than as zero-and-mixed-in.
    hits.sort(key=lambda r: (r.get("total_czk") is None, -(r.get("total_czk") or 0)))
    shown = hits[:max(0, args.limit)]

    if args.as_json:
        json.dump([dict(r, citation=citation(r)) for r in shown],
                  sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        print("ms21_query: %d hit(s), showing %d" % (len(hits), len(shown)),
              file=sys.stderr)
        return 0

    out = []
    for i, r in enumerate(shown, 1):
        human(r, i, out)
    sys.stdout.write("\n".join(out))
    total = sum(r.get("total_czk") or 0 for r in hits)
    print("== %d project(s) matched, %s Kč approved in total; showing %d"
          % (len(hits), czk(total), len(shown)))
    if len(hits) > len(shown):
        print("   (--limit %d to see more)" % (len(hits)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
