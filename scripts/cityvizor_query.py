#!/usr/bin/env python3
"""
cityvizor_query.py — the executed-spend counterpart of ms21_query.py. Stdlib only.

THE QUESTION IT ANSWERS
=======================
"What did a named Czech public body ACTUALLY PAY for this, to whom, and when?"
ms21_query.py answers what a buyer was APPROVED to spend on a project;
this tool answers what a body's accounting ledger says left its account for a
thing — invoice by invoice, below every tender threshold, with the
counterparty's IČO beside it. data/CONVENTIONS.md's `type: price` receipt
needs payer, amount_czk, unit, basis and date; every hit here hands you all
five, from one grep over data/lookup/cityvizor-invoices.jsonl (built by
scripts/fetch_cityvizor.sh + scripts/cityvizor_index.py).

    python3 scripts/cityvizor_query.py --keyword software
    python3 scripts/cityvizor_query.py --keyword "spisová služba" --min-czk 100000
    python3 scripts/cityvizor_query.py --keyword licence --body ostrava --year 2025 --json

Matching is case- AND diacritic-insensitive over description + counterparty
name, because a MATCH pass types "spisova sluzba" and the ledgers are in
Czech; a tool that needs the right háčky to find a 400,000-crown licence is a
tool nobody uses twice.

RESULTS ARE ORDERED BY MONEY, LARGEST FIRST
===========================================
The ms21 rule, for the ms21 reason. And because a ledger repeats — twelve
monthly instalments of the same licence are twelve rows — the footer prints
the MEDIAN beside the total: the one number an honest "what does this cost"
should quote when the hits are many.

THE CITATION LINE, AND WHY ITS URL IS PER BODY AND PER MONTH
============================================================
The public view exposes no invoice id, so there is NO per-invoice permalink
anywhere on cityvizor.cz. The closest public page is the body's invoice
table for one month — `https://cityvizor.cz/<slug>/faktury;rok=YYYY;mesic=M`
(Angular matrix params; the same link the site's own date picker builds,
client/…/date-picker.component.ts `getMonthLink`), which lists every line of
that month with date, IČO, counterparty, description and amount, so the reader
can find the row by eye. The url is therefore SHARED by every invoice of that
body in that month, by design — the shape data/CONVENTIONS.md already blesses
for coi/sukl/mpsv and ms21 ("a constant dataset url … merging on url alone
would delete 504 real records"). The row `id` in `note` is the identifying
key. The note says so in-line, so the next dedupe pass does not "fix" it.
"""
import argparse
import json
import os
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_INDEX = os.path.join(ROOT, "data", "lookup", "cityvizor-invoices.jsonl")
SITE_URL = "https://cityvizor.cz"
SOURCE_NAME = "CityVizor — faktury (účetní deník obce, Otevřená města z.s.)"

NOTE_TMPL = (
    "CityVizor invoice line {id}: {body} paid {counterparty}{cp_ico} "
    "{amount} Kč on {date}, rozpočtová položka {item}{paragraph} — \"{description}\". "
    "The url is the body's invoice page for that MONTH and is shared by every "
    "line of that month: the public API exposes no invoice id, so there is no "
    "per-invoice permalink; a per-body, per-month url is the constant-url shape "
    "coi/sukl/mpsv/ms21 already use by design (data/CONVENTIONS.md). The id here "
    "is the identifying key — do not 'fix' the url to a per-invoice link, there is none."
)


def fold(s):
    """Case- and diacritic-insensitive form. 'Kódování' -> 'kodovani'."""
    return "".join(c for c in unicodedata.normalize("NFKD", str(s or ""))
                   if not unicodedata.combining(c)).casefold()


def czk(n):
    """1234567 -> '1 234 567'. Grouping by hand: LC_NUMERIC=C is the house rule."""
    if n is None:
        return "?"
    s = str(abs(int(n)))
    out = []
    while len(s) > 3:
        out.insert(0, s[-3:])
        s = s[:-3]
    out.insert(0, s)
    return ("-" if n < 0 else "") + " ".join(out)


def median(values):
    v = sorted(values)
    if not v:
        return None
    m = len(v) // 2
    return v[m] if len(v) % 2 else (v[m - 1] + v[m]) // 2


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
                print("cityvizor_query: %s:%d is not JSON (%s)" % (path, ln, e),
                      file=sys.stderr)
    return rows


def haystack(r):
    return fold(" ".join((r.get("description", ""), r.get("counterparty", ""))))


def page_url(r):
    """The body's invoice table for the month of this line — see the header."""
    d = r.get("date") or ""
    if len(d) >= 7 and r.get("profile"):
        return "%s/%s/faktury;rok=%s;mesic=%d" % (SITE_URL, r["profile"], d[:4], int(d[5:7]))
    if r.get("profile"):
        return "%s/%s/faktury" % (SITE_URL, r["profile"])
    return ""


def citation(r):
    """
    The `sources[]` entry a record should paste. Five fields are REQUIRED on a
    price source (data/CONVENTIONS.md): payer, amount_czk, unit, basis, date.

    `basis: signed-contract` — an invoice line in a public body's ledger is
    money paid under an order or contract already performed, not a list price
    and not a tender line. `unit: one-off` — one invoice, not a rate; twelve
    monthly instalments are twelve rows and the caller sums or medians them.
    `date` is the ledger's booking date for the line.
    """
    return {
        "type": "price",
        "url": page_url(r),
        "name": SOURCE_NAME,
        "note": NOTE_TMPL.format(
            id=r.get("id", "?"),
            body=r.get("body", "?"),
            counterparty=r.get("counterparty") or "(counterparty not named)",
            cp_ico=(" (IČO %s)" % r["counterparty_ico"]) if r.get("counterparty_ico") else "",
            amount=czk(r.get("amount_czk")),
            date=r.get("date", "?"),
            item=r.get("budget_item", "?"),
            paragraph=(", paragraf %s" % r["budget_paragraph"]) if r.get("budget_paragraph") else "",
            description=(r.get("description") or "").replace('"', "'")),
        "date": r.get("date", ""),
        "payer": r.get("body", ""),
        "amount_czk": r.get("amount_czk"),
        "unit": "one-off",
        "basis": "signed-contract",
    }


def human(r, i, out):
    out.append("[%d] %s%s · %s · %s Kč"
               % (i, r.get("body", "?"),
                  (" · IČO %s" % r["body_ico"]) if r.get("body_ico") else " · (IČO not in the CityVizor profile)",
                  r.get("date", "?"), czk(r.get("amount_czk"))))
    out.append("    dodavatel: %s%s"
               % (r.get("counterparty") or "(neuveden)",
                  (" · IČO %s" % r["counterparty_ico"]) if r.get("counterparty_ico") else ""))
    out.append("    popis:     %s" % (r.get("description") or "(bez popisu)"))
    out.append("    položka %s%s · rozpočtový rok %s · %s"
               % (r.get("budget_item", "?"),
                  (" · paragraf %s" % r["budget_paragraph"]) if r.get("budget_paragraph") else "",
                  r.get("year", "?"), r.get("id", "?")))
    cite = citation(r)
    # THE SUBJECT TEST — the same warning ms21_query.py prints, because the
    # citation JSON below is copy-pasteable and nothing downstream can re-check
    # the judgement. A paid invoice for X is a price for X only: "služby IT
    # 12/2025" is a price for that body's IT services, not for a product that
    # happens to share a word with it.
    out.append("    NEŽ TOHLE POUŽIJETE: cituj jen tehdy, když PŘEDMĚT projektu je "
               "produkt záznamu (nebo jeho ruční ekvivalent). Stavba pavilonu není "
               "cena za software. Jinak je to peníze v cizí kapse — a záznam má "
               "zůstat bez ceny.")
    out.append("    cite: %s" % json.dumps(cite, ensure_ascii=False))
    out.append("")


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="What a named Czech public body actually paid, to whom, for what.",
        epilog="Index built by: scripts/fetch_cityvizor.sh <outdir>")
    ap.add_argument("--keyword", help="case- and diacritic-insensitive text over "
                                      "description + counterparty name")
    ap.add_argument("--body", help="substring of the paying body's name, diacritic-insensitive")
    ap.add_argument("--min-czk", type=float, default=None,
                    help="drop lines whose amount is below this")
    ap.add_argument("--year", type=int, default=None,
                    help="the ledger's BUDGET year (the `year` field), not the date's year")
    ap.add_argument("--ico", help="exact IČO of the counterparty (who was paid)")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--json", action="store_true", dest="as_json",
                    help="machine output: one JSON array, each hit + its citation")
    ap.add_argument("--index", default=DEFAULT_INDEX)
    args = ap.parse_args(argv)

    if not os.path.isfile(args.index):
        print("cityvizor_query: no index at %s — build it with:\n"
              "  scripts/fetch_cityvizor.sh data/raw/$(date +%%F)" % args.index,
              file=sys.stderr)
        return 2
    if not any((args.keyword, args.body, args.ico, args.min_czk, args.year)):
        print("cityvizor_query: give at least one filter (--keyword / --body / "
              "--ico / --min-czk / --year). Printing the first 20 of ~100k "
              "ledger lines answers nobody's question.", file=sys.stderr)
        return 2

    kw = fold(args.keyword) if args.keyword else None
    body = fold(args.body) if args.body else None
    hits = []
    for r in load(args.index):
        if kw and kw not in haystack(r):
            continue
        if body and body not in fold(r.get("body", "")):
            continue
        if args.ico and r.get("counterparty_ico") != args.ico:
            continue
        if args.year is not None and r.get("year") != args.year:
            continue
        if args.min_czk is not None and (r.get("amount_czk") or 0) < args.min_czk:
            continue
        hits.append(r)

    # Money first; a missing amount cannot happen in this index, but sorts last anyway.
    hits.sort(key=lambda r: (r.get("amount_czk") is None, -(r.get("amount_czk") or 0),
                             r.get("date", ""), r.get("id", "")))
    shown = hits[:max(0, args.limit)]

    if args.as_json:
        json.dump([dict(r, citation=citation(r)) for r in shown],
                  sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        print("cityvizor_query: %d hit(s), showing %d" % (len(hits), len(shown)),
              file=sys.stderr)
        return 0

    out = []
    for i, r in enumerate(shown, 1):
        human(r, i, out)
    sys.stdout.write("\n".join(out))
    amounts = [r.get("amount_czk") for r in hits if isinstance(r.get("amount_czk"), int)]
    bodies = sorted(set(r.get("body", "") for r in hits))
    print("== %d invoice line(s) matched across %d bodies; %s Kč in total, median %s Kč; showing %d"
          % (len(hits), len(bodies), czk(sum(amounts)), czk(median(amounts)), len(shown)))
    if len(hits) > len(shown):
        print("   (--limit %d to see more)" % (len(hits)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
