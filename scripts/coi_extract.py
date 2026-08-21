#!/usr/bin/env python3
"""
coi_extract.py — the ČOI enforcement payload reader, and the normalize.py
                 extractor for it.

WHAT THIS TALKS TO
==================
Česká obchodní inspekce (the Czech Trade Inspection Authority) has published
open data since 27 October 2013 under an explicit open licence. Nine datasets;
this feed reads two of them, both plain CSV at fixed, unversioned-in-the-path
URLs that have not moved:

    https://coi.gov.cz/userdata/files/dokumenty-ke-stazeni/open-data/sankce.csv
    https://coi.gov.cz/userdata/files/dokumenty-ke-stazeni/open-data/kontroly.csv

MEASURED 2026-08-21, with a plain descriptive User-Agent, no auth:

    sankce.csv    200  12,159,176 B  text/csv  ETag "b988c8-6584d2662d000"
                                               Last-Modified Wed 05 Aug 2026 13:57:20 GMT
    kontroly.csv  200  27,517,464 B  text/csv  ETag "1a3e218-6584d18ea5380"
                                               Last-Modified Wed 05 Aug 2026 13:53:34 GMT

    sankce.csv     176,945 rows, UTF-8 with BOM, comma-delimited
      Id Sankce | ID kontroly | Vyse pokuty | Zakon | § | Datum nabyti Pravni Moci
    kontroly.csv 288,962 rows, same encoding
      Id kontroly | Datum kontroly | IC subjektu | NUTS 3 | Kraj | NUTS 4 | Okres
      | NUTS 5 | Obec | Ulice | C. popisne | C. orientacni | PSC

`docs/feeds-status.md` describes ČOI as an "HTML scrape … annual PDF". That is
wrong, and it is wrong in the direction that matters: this is a structured
quarterly CSV with a twelve-year history in one file, which makes it both the
least-fragile shape available AND self-sufficient for growth rates — the file
carries its own comparison periods, so no state has to be kept between runs.

WHY IT IS `demand` AND NOT SOMETHING ELSE
=========================================
A legally-final fine is the state's own record that a market failed a consumer
in a way serious enough to survive appeal. It is documented, quantified,
dated, and attributable to a named act. That is the `demand` ledger's
definition — "bottom-up documented complaints and unmet needs" evidenced by an
institution — and it is what the audit that redirected this build measured as
the highest-yield source class in the corpus.

THE GRAIN — (LAW x HALF-YEAR), NEVER ONE ROW PER FINE
=====================================================
The same arithmetic that governs `mpsv` and `sukl` governs this. The MEDIAN
fine in the file is 3,000 CZK — €120. One fine scores `money` 0, `urgency` 0
(its date is in the past, so score_urgency() returns None), and `scale` 0: one
shop. Materiality drops `money <= 1 AND scale <= 1 AND urgency == 0`, so a
per-fine feed would carry 176,945 items and write approximately none of them,
with every counter reading green. AGGREGATE BEFORE THE FILTER.

Half-years rather than quarters because the register wants signals, not a time
series: ~12 laws carry real volume, so a half-year grain yields 10-15 records
per period instead of 25-30, and the demand ledger is explicitly not to be
dominated by one feed.

The id is `coi-<period>-<law-slug>` — keyed on the PERIOD, never on the fine or
the inspection, for the reason CONVENTIONS.md gives for `mpsv-`: the same rows
sit in this file for eleven years, so any id derived from a row re-proposes the
same fines on every run and defeats seen.txt.

COMPLETENESS — THE ONE PLACE THIS COULD QUIETLY LIE
===================================================
A half-year is only emitted once the file demonstrably covers all of it.
Otherwise the first run after a quarterly refresh would record a half-finished
period as final, and the ledger is append-only: the undercount could never be
corrected.

The naive test — "the newest fine date is at or past the period end" — FAILS on
the real file. MEASURED: the newest date in the 2026-08-05 edition is
2026-06-29, one day short of the 30 June boundary the publisher declares,
because no fine happened to gain legal force on the last day. So completeness is
decided by the QUARTER the newest date falls in, which is what the publisher
actually updates on. The rule is safe because it was measured, not assumed:
across the last ten quarters the newest fine date sat 0 or 1 days before the
quarter end every single time (2024-Q1 1, Q2 1, Q3 0, Q4 0, 2025 Q1-Q4 all 0,
2026-Q1 0, Q2 1). `QUARTER_TAIL_DAYS` keeps a 21-day margin on that, and if ČOI
ever publishes mid-quarter the margin is exceeded and the period is held back —
which loses freshness for one quarter and records nothing false. It fails safe
in the only direction an append-only ledger allows.

USED FROM TWO PLACES:
  scripts/fetch_coi.sh   — `python3 scripts/coi_extract.py read …`
  scripts/normalize.py   — `extract_coi()` as EXTRACTORS["coi"] (HAND-OFF — see
                           the note on extract_coi below)
"""

import argparse
import collections
import csv
import datetime
import io
import json
import os
import re
import sys
import unicodedata

# --------------------------------------------------------------------------
# 1. THE SOURCE CONTRACT — MODE A, evaluated at FETCH time.
# --------------------------------------------------------------------------
#
# Mode A is a good transfer carrying the wrong body. Every assertion here is a
# thing a WordPress error page, a cookie wall or a truncated transfer cannot
# have, and every threshold is a measured fact about the real file rather than a
# round number someone liked.
SANKCE_COLUMNS = ("Id Sankce", "ID kontroly", "Vyse pokuty", "Zakon", "§",
                  "Datum nabyti Pravni Moci")
KONTROLY_COLUMNS = ("Id kontroly", "Datum kontroly", "IC subjektu", "NUTS 3",
                    "Kraj", "NUTS 4", "Okres", "NUTS 5", "Obec")
# The file held 176,945 / 288,962 rows on 2026-08-21 and only grows — it is a
# cumulative register back to 2015-01-01, never a window.
MIN_SANKCE_ROWS = 100_000
MIN_KONTROLY_ROWS = 150_000
# The file must still start where the publisher says it starts. A silently
# re-scoped export is a wrong body that every count-based check would pass.
EXPECTED_FIRST_DATE = "2015-01-01"
QUARTER_TAIL_DAYS = 21
ENCODING = "utf-8-sig"


class ContractViolation(Exception):
    """A 200 carrying the wrong body. Louder than a non-200, by design."""


def read_csv(path, required, min_rows, label):
    raw = open(path, "rb").read()
    if not raw.strip():
        raise ContractViolation(f"{label}: zero bytes")
    # A WordPress 404/cookie page is valid UTF-8 and "parses" as a one-column
    # CSV, so the decode succeeding proves nothing. The column names are the
    # only thing that separates data from a page.
    head = raw[:200].lstrip()
    if head[:1] == b"<":
        raise ContractViolation(
            f"{label}: body is markup, not CSV — first 200 bytes: "
            f"{head[:200].decode('utf-8', 'replace')!r}")
    try:
        text = raw.decode(ENCODING)
    except UnicodeDecodeError as e:
        raise ContractViolation(f"{label}: not {ENCODING}: {e}") from e
    rows = list(csv.DictReader(io.StringIO(text)))
    cols = set(rows[0].keys()) if rows else set()
    missing = [c for c in required if c not in cols]
    if missing:
        raise ContractViolation(
            f"{label}: columns {missing} missing; got {sorted(cols)[:8]}")
    if len(rows) < min_rows:
        raise ContractViolation(
            f"{label}: {len(rows):,} rows, below the {min_rows:,} floor — this "
            "register is cumulative back to 2015 and only grows, so a file this "
            "short is a wrong body, not a quiet quarter")
    return rows


# --------------------------------------------------------------------------
# 2. PERIODS
# --------------------------------------------------------------------------

CZ_DATE = re.compile(r"^(\d{2})\.(\d{2})\.(\d{4})$")


def iso(d):
    """`01.04.2016` -> `2016-04-01`. The only date format in these files."""
    m = CZ_DATE.match(str(d or "").strip())
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else None


def half_of(iso_date):
    return f"{iso_date[:4]}-H1" if iso_date[5:7] <= "06" else f"{iso_date[:4]}-H2"


def half_bounds(period):
    y, h = period[:4], period[-1]
    return (f"{y}-01-01", f"{y}-06-30") if h == "1" else (f"{y}-07-01", f"{y}-12-31")


def prev_half(period):
    y, h = int(period[:4]), period[-1]
    return f"{y}-H1" if h == "2" else f"{y - 1}-H2"


def year_ago(period):
    return f"{int(period[:4]) - 1}-{period[-2:]}"


def quarter_end(iso_date):
    d = datetime.date.fromisoformat(iso_date)
    q_end_month = ((d.month - 1) // 3 + 1) * 3
    if q_end_month == 12:
        return datetime.date(d.year, 12, 31)
    return datetime.date(d.year, q_end_month + 1, 1) - datetime.timedelta(days=1)


def coverage_end(max_date):
    """How far this edition of the file actually covers. See the long note above.

    Returns None when the newest row sits more than QUARTER_TAIL_DAYS before its
    own quarter end — i.e. when the quarterly refresh evidently has not landed,
    so NO period may be treated as complete.
    """
    qe = quarter_end(max_date)
    gap = (qe - datetime.date.fromisoformat(max_date)).days
    return qe.isoformat() if gap <= QUARTER_TAIL_DAYS else None


# --------------------------------------------------------------------------
# 3. LAW LABELS AND SECTORS
# --------------------------------------------------------------------------
#
# EDITORIAL GLOSSES, AND LABELLED AS SUCH IN THE PAYLOAD (`zakon_gloss`).
# The citable fact is the CODE plus the ČOI dataset URL; the gloss exists so a
# model can write an English title without guessing what "Zák. 634/1992" is. It
# is deliberately restricted to the ~15 acts that carry real volume: 45 distinct
# codes appear in the file, 12 of them account for 98% of the rows, and a table
# that tried to cover the long tail would be a list of half-remembered names.
# A code with no entry gets NO gloss and NO sector — `sector` then lands in
# `_needs` and a model rules on it, which is the correct place for a judgement.
LAW_GLOSS = {
    "Zák. 634/1992": ("zákon o ochraně spotřebitele", "retail-services"),
    "Zák. 22/1997": ("zákon o technických požadavcích na výrobky", "retail-services"),
    "Zák. 102/2001": ("zákon o obecné bezpečnosti výrobků", "retail-services"),
    "Zák. 477/2001": ("zákon o obalech", "environment"),
    "Zák. 542/2020": ("zákon o výrobcích s ukončenou životností", "environment"),
    "Zák. 90/2016": ("zákon o posuzování shody stanovených výrobků", "retail-services"),
    "Zák. 65/2017": ("zákon o ochraně zdraví před škodlivými účinky návykových látek",
                     "health"),
    "Zák. 255/2012": ("kontrolní řád", "legal-compliance"),
    "Zák. 89/2012": ("občanský zákoník", "legal-compliance"),
    "Zák. 64/1986": ("zákon o České obchodní inspekci", "legal-compliance"),
    "Zák. 311/2006": ("zákon o pohonných hmotách", "energy"),
    "Zák. 257/2016": ("zákon o spotřebitelském úvěru", "fintech"),
    "Zák. 145/2010": ("zákon o spotřebitelském úvěru (do 2016)", "fintech"),
    "Zák. 253/2008": ("zákon proti legalizaci výnosů z trestné činnosti (AML)", "fintech"),
    "Zák. 223/2016": ("zákon o prodejní době v maloobchodě", "retail-services"),
    "Zák. 206/2015": ("zákon o pyrotechnických výrobcích", "retail-services"),
    "Nař. 1007/2011": ("nařízení EU o názvech textilních vláken", "retail-services"),
    "Nař. 2016/425": ("nařízení EU o osobních ochranných prostředcích", "b2b"),
    "Nař. 305/2011": ("nařízení EU o stavebních výrobcích", "housing"),
    "Nař. 524/2013": ("nařízení EU o online řešení spotřebitelských sporů", "legal-compliance"),
    "Nař. 2023/988": ("nařízení EU o obecné bezpečnosti výrobků (GPSR)", "retail-services"),
}


def law_slug(code):
    """`Zák. 634/1992` -> `zak-634-1992`. The id-safe half of the law code.

    DIACRITICS ARE TRANSLITERATED, NOT DROPPED. A naive `[^a-z0-9]+` strip turns
    `Zák.` into `z-k` and `Nař.` into `na`, which is both unreadable and
    ambiguous — and these strings become ids in an append-only ledger, so the
    first version is the permanent one.
    """
    s = unicodedata.normalize("NFKD", str(code or ""))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s)).strip("-") or "bez-zakona"


# --------------------------------------------------------------------------
# 4. AGGREGATION
# --------------------------------------------------------------------------

# See the identical block in nen_extract.py / sukl_extract.py for why these are
# duplicated rather than imported: this module refuses contact data while running
# inside fetch_coi.sh, where normalize.py is not loaded. `kontroly.csv` carries
# STREET ADDRESSES of inspected premises, and for a sole trader a business
# address is a home address — so nothing from those columns is ever copied into
# a payload item. Only NUTS/Kraj (regional) and IČO COUNTS leave this file.
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


def _money(v):
    try:
        return int(float(str(v).replace(" ", "").replace(",", ".") or 0))
    except (TypeError, ValueError):
        return 0


def _pct(now, before):
    if not before:
        return None
    return round((now - before) / before * 100.0, 1)


def aggregate(sankce, kontroly, since, min_fines):
    """Rows -> (items, meta). AGGREGATION BEFORE MATERIALITY."""
    kmap = {r["Id kontroly"]: r for r in kontroly}

    dated = []
    for r in sankce:
        d = iso(r.get("Datum nabyti Pravni Moci"))
        if not d:
            continue
        dated.append((d, r))
    if not dated:
        raise ContractViolation("no parsable legal-force dates in sankce.csv")
    max_date = max(d for d, _ in dated)
    min_date = min(d for d, _ in dated)
    if min_date != EXPECTED_FIRST_DATE:
        raise ContractViolation(
            f"sankce.csv starts at {min_date}, publisher declares "
            f"{EXPECTED_FIRST_DATE} — the export has been re-scoped and the "
            "history this feed's growth rates depend on is not what it was")
    cov = coverage_end(max_date)

    buckets = collections.defaultdict(list)
    for d, r in dated:
        buckets[(r.get("Zakon", "").strip(), half_of(d))].append(r)

    items = []
    if cov is None:
        return items, {"max_date": max_date, "coverage_end": None,
                       "periods_emitted": [], "held_back": "quarterly refresh "
                       "has not landed: newest fine is more than "
                       f"{QUARTER_TAIL_DAYS} days before its own quarter end"}

    emitted = set()
    for (law, period), rows in sorted(buckets.items()):
        if not law:
            continue
        _, p_end = half_bounds(period)
        if p_end > cov:          # period not yet fully covered by this edition
            continue
        if p_end < since:        # outside the requested window
            continue
        if len(rows) < min_fines:
            continue

        prev = buckets.get((law, prev_half(period)), [])
        yoy = buckets.get((law, year_ago(period)), [])
        czk = sum(_money(r["Vyse pokuty"]) for r in rows)
        czk_prev = sum(_money(r["Vyse pokuty"]) for r in prev)
        czk_yoy = sum(_money(r["Vyse pokuty"]) for r in yoy)

        insp = {r["ID kontroly"] for r in rows}
        joined = [kmap[i] for i in insp if i in kmap]
        icos = {k["IC subjektu"] for k in joined if k.get("IC subjektu")}
        regions = collections.Counter(k.get("Kraj") for k in joined if k.get("Kraj"))
        paras = collections.Counter(contact_free(r.get("§")) for r in rows)
        paras.pop("", None)

        gloss, sector = LAW_GLOSS.get(law, (None, None))
        top_par = paras.most_common(1)[0][0] if paras else None
        # Composed at FETCH time from two verbatim cells so the exact string the
        # ledger will carry is a literal value in the payload on disk.
        # normalize.py verifies a quote as a substring of the fetched payload,
        # and a string assembled downstream from two payload fields is not one.
        citace = f"{law} — {top_par}" if top_par else law

        items.append({
            "kind": "sankce",
            "zakon": law,
            "zakon_gloss": gloss,          # EDITORIAL, see LAW_GLOSS
            "zakon_slug": law_slug(law),
            "sector": sector,
            "period": period,
            "period_start": half_bounds(period)[0],
            "period_end": p_end,
            "coverage_end": cov,
            "fines": len(rows),
            "inspections": len(insp),
            "businesses": len(icos),
            "join_rate": round(len(joined) / len(insp), 4) if insp else None,
            "czk_total": czk,
            "czk_median": sorted(_money(r["Vyse pokuty"]) for r in rows)[len(rows) // 2],
            "prev_period": prev_half(period),
            "prev_fines": len(prev),
            "prev_czk_total": czk_prev,
            "yoy_period": year_ago(period),
            "yoy_fines": len(yoy),
            "yoy_czk_total": czk_yoy,
            "growth_czk_vs_prev_pct": _pct(czk, czk_prev),
            "growth_czk_vs_yoy_pct": _pct(czk, czk_yoy),
            "growth_fines_vs_yoy_pct": _pct(len(rows), len(yoy)),
            "top_paragraphs": [{"par": p, "n": n} for p, n in paras.most_common(5)],
            "top_regions": [{"kraj": r, "n": n} for r, n in regions.most_common(5)],
            "citace": citace,
            "url": "https://coi.gov.cz/pro-spotrebitele/otevrena-data/ulozene-pokuty/",
        })
        emitted.add(period)

    return items, {"max_date": max_date, "coverage_end": cov,
                   "periods_emitted": sorted(emitted), "held_back": None}


def read_files(sankce_path, kontroly_path, out, since, min_fines=10):
    sankce = read_csv(sankce_path, SANKCE_COLUMNS, MIN_SANKCE_ROWS, "sankce.csv")
    kontroly = read_csv(kontroly_path, KONTROLY_COLUMNS, MIN_KONTROLY_ROWS, "kontroly.csv")
    items, meta = aggregate(sankce, kontroly, since, min_fines)
    doc = {
        "feed": "coi",
        "source_interface": "coi.gov.cz open data (sankce.csv + kontroly.csv)",
        "sankce_rows": len(sankce),
        "kontroly_rows": len(kontroly),
        "since": since,
        "fetched": len(items),
        "items": items,
        **meta,
    }
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False)
    return doc


# --------------------------------------------------------------------------
# 5. THE normalize.py EXTRACTOR
# --------------------------------------------------------------------------
#
# HAND-OFF (scripts/normalize.py is not this worker's file). Two lines:
#
#     from coi_extract import extract_coi          # sys.path[0] is scripts/
#     EXTRACTORS = {…, "coi": extract_coi, …}
#
# AND ONE MORE IN normalize.py: FILE_FEED_TOKENS (normalize.py:92) has no `coi`
# entry, so `coi-2026-H1.json` maps to NO feed key and is reported as an unmapped
# payload — parsed by nobody, silently absent from the ledger. Add ("coi", "coi")
# to that table, ORDERED BEFORE the generic tokens.
#
# WITHOUT THE EXTRACTOR THIS FEED IS BORN SCRIPTED-SILENT AND LOOKS FINE:
# normalize.py:957 does `extractor = EXTRACTORS.get(feed_key)` and :962-963
# `if not extractor: break` — no log line, no manifest note. The contract check
# has already passed, so the run records ok=1, items_fetched=13, items_kept=0.

def extract_coi(item, payload_key, today):
    """Signature and return shape are normalize.py's, not ours."""
    law, period = item.get("zakon"), item.get("period")
    if not law or not period:
        return None
    czk = item.get("czk_total") or 0
    fines = item.get("fines") or 0
    biz = item.get("businesses") or 0
    gloss = item.get("zakon_gloss")

    money = round(float(czk) / 25.0) if czk else None      # CZK_PER_EUR, normalize.py:64
    # THE NOTE IS DOING REAL WORK HERE, NOT DECORATION. `scores.money` is pure
    # arithmetic on this figure, and this figure is PENALTY VOLUME PAID BY
    # BUSINESSES — not a procurement budget and not revenue anyone can win. A
    # reader ranking this beside a tender must be able to see that from the
    # record itself, so the distinction travels in money_note rather than in a
    # convention someone has to remember.
    note = (f"{czk:,.0f} CZK in {fines} legally-final fines levied by ČOI under "
            f"{law} in {period}, at a fixed 25.0 CZK/EUR. This is penalty volume "
            f"paid by businesses, NOT a procurement budget or an addressable "
            f"contract value.") if czk else ""

    growth = item.get("growth_czk_vs_yoy_pct")
    native = (f"ČOI: {fines} pravomocných pokut podle {law}"
              + (f" ({gloss})" if gloss else "")
              + f" v období {period}, {biz} kontrolovaných subjektů")
    parts = [
        f"Half-year aggregate over ČOI open data (sankce.csv + kontroly.csv), "
        f"coverage to {item.get('coverage_end')}.",
        f"{fines} fines / {item.get('inspections')} inspections / {biz} distinct "
        f"IČO; median fine {item.get('czk_median'):,} CZK; join rate to kontroly "
        f"{item.get('join_rate')}.",
        f"Previous half {item.get('prev_period')}: {item.get('prev_fines')} fines / "
        f"{item.get('prev_czk_total'):,} CZK. Year-ago {item.get('yoy_period')}: "
        f"{item.get('yoy_fines')} fines / {item.get('yoy_czk_total'):,} CZK.",
        f"Growth CZK vs prev {item.get('growth_czk_vs_prev_pct')}%, vs year-ago "
        f"{growth}%; fines vs year-ago {item.get('growth_fines_vs_yoy_pct')}%.",
        "Top §: " + "; ".join(f"{p['par']} ({p['n']})"
                              for p in item.get("top_paragraphs") or []),
        "Top kraj: " + "; ".join(f"{r['kraj']} ({r['n']})"
                                 for r in item.get("top_regions") or []),
    ]
    return {
        "id": f"coi-{period}-{item.get('zakon_slug')}",
        "source": "coi",
        "evidence_type": "demand",
        "url": item.get("url"),
        # The period's own end date, never our clock: the aggregate is a
        # statement about a closed half-year and must be datable to it.
        "date": item.get("period_end"),
        "title_native": native,
        "entity_native": "Česká obchodní inspekce",
        # Mechanical where it is a lookup on the breached act, and None where it
        # is not — see LAW_GLOSS. A None here puts `sector` in `_needs` and a
        # model rules on it, which is where a judgement belongs.
        "sector": item.get("sector"),
        "money_eur": money,
        "money_note": note,
        # THE ROUTING FIELD FOR URGENCY, AND `None` IS THE WRONG VALUE FOR IT.
        # score_urgency() returns 0 for a falsy date and None only for a PAST one
        # (normalize.py: `if not event_date: return 0` … `if m < 0: return None`),
        # and `urgency_pending` — what puts `scores.urgency` into `_needs` — is
        # set from `u is None`. So passing None does not hand urgency to a model:
        # it silently STAMPS urgency 0 and never asks. Measured on the first
        # staged run of this feed: 32 of 32 records came out `urgency_pending:
        # false` with no `scores.urgency` in `_needs`.
        #
        # `period_end` is the honest anchor and is ALWAYS strictly in the past:
        # only completed half-years are emitted, and completeness requires the
        # quarterly file to already cover the period, which lags it by five weeks
        # or more. score_urgency() therefore returns None and the model rules on
        # the "already in force AND actively enforced" branch — the branch
        # INGEST.md §3b reserves for exactly this, and which a register of
        # legally-final fines is the clearest possible case of.
        "urgency_date": item.get("period_end"),
        "quote_parts": [item.get("citace")] if item.get("citace") else [],
        "excerpt": native,
        "notes": " ".join(parts),
    }


# --------------------------------------------------------------------------
# 6. CLI — driven by scripts/fetch_coi.sh
# --------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("read", help="CSVs -> <raw>/coi-<period>.json aggregates")
    r.add_argument("sankce")
    r.add_argument("kontroly")
    r.add_argument("out")
    r.add_argument("--since", default="2025-01-01",
                   help="drop periods that ended before this ISO date")
    r.add_argument("--min-fines", type=int, default=10)
    c = sub.add_parser("check", help="run the source contract and exit")
    c.add_argument("sankce")
    c.add_argument("kontroly")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "read":
            doc = read_files(a.sankce, a.kontroly, a.out, a.since, a.min_fines)
            print(json.dumps({k: v for k, v in doc.items() if k != "items"},
                             ensure_ascii=False))
            return 0
        s = read_csv(a.sankce, SANKCE_COLUMNS, MIN_SANKCE_ROWS, "sankce.csv")
        k = read_csv(a.kontroly, KONTROLY_COLUMNS, MIN_KONTROLY_ROWS, "kontroly.csv")
        print(json.dumps({"ok": True, "sankce_rows": len(s), "kontroly_rows": len(k)}))
        return 0
    except ContractViolation as e:
        print(f"CONTRACT VIOLATION: {e}", file=sys.stderr)
        return 65


if __name__ == "__main__":
    sys.exit(main())
