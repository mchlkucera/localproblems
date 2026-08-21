#!/usr/bin/env python3
"""
mpsv_reduce.py — the MPSV privacy gate and the hiring aggregator, in that order.

CALLED BY scripts/fetch_mpsv.sh. Not a fetcher: it never opens a socket. It reads
the daily `volna-mista-prirustek` increments that fetch_mpsv.sh downloaded into a
WORK DIRECTORY OUTSIDE THE REPO, reduces them to one aggregate payload, and
deletes the work directory. The upstream payload never enters data/raw/ at all.

WHY A SEPARATE FILE FROM THE FETCHER. Two reasons, both structural:

  1. THE PRIVACY GATE IS PYTHON-SHAPED. `docs/architecture-v3.md` §13.6 requires a
     FIELD ALLOWLIST, and an allowlist over a 39-key nested JSON document is not
     something jq-in-bash expresses honestly. Measured on one day of the real
     feed (2026-08-20, 2,473 postings): 2,471 items carry a contact person's
     SURNAME, 2,243 an EMAIL, 1,676 a PHONE — and 778 carry an email inside the
     free-text field `upresnujiciInformace.cs`, which no field-name denylist
     would ever have named. The allowlist below is a list of PATHS THAT MAY BE
     READ; nothing else is copied, so a new contact column MPSV adds tomorrow is
     a no-op instead of a disclosure.
  2. AGGREGATION MUST HAPPEN BEFORE MATERIALITY (`data/CONVENTIONS.md`,
     architecture §13.4). Aggregation is a pure-script step — group by theme,
     sum the wage floors — so it belongs in the mechanical phase, ahead of the
     filter. Doing it here rather than in normalize.py keeps normalize's mpsv
     extractor to one item -> one record, exactly like every other feed.

THE THREE GATES, in the order they run. Each is capable of refusing the whole
run; none of them redacts, because a silent redaction hides that the feed started
emitting contact data at all:

  GATE 1  STRUCTURAL   only SOURCE_ALLOWLIST paths are ever read out of a posting
  GATE 2  KEY SCAN     the produced payload may not contain a contact-shaped KEY
  GATE 3  CONTENT SCAN the produced payload text is scanned with normalize.py's
                       OWN EMAIL_RE / PHONE_RE — imported, never re-typed, so the
                       ledger gate and this gate cannot drift into disagreement

Usage:
  mpsv_reduce.py --work DIR --month YYYY-MM --out FILE --isco FILE --kraje FILE
                 --worklist FILE [--days-absent d,d,...] [--keep-work]
Exit codes: 0 ok · 2 a privacy gate refused (nothing written) · 3 bad input.
"""
import argparse
import calendar
import collections
import glob
import gzip
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# ONE definition of "what personal data looks like", shared with the ledger gate.
# scripts/normalize.py is import-safe (scripts/model_pass.py already imports it
# for the same anti-drift reason). If this import ever fails, the run must FAIL,
# not fall back to a local copy of the regexes — a second copy is exactly the
# drift this import exists to prevent.
from normalize import EMAIL_RE, PHONE_RE, collapse  # noqa: E402

CZK_PER_EUR = 25.0  # normalize.CZK_PER_EUR, restated so the money_note can quote it

# ==========================================================================
# GATE 1 — THE SOURCE FIELD ALLOWLIST (architecture-v3.md §13.6)
# ==========================================================================
# Dotted paths into ONE `polozky[]` posting. `[]` means "a list — take every
# element". A path not named here is never read, never copied, never serialised.
#
# WHAT IS DELIBERATELY ABSENT, and why each one matters:
#   prvniKontaktSeZamestnavatelem.*   the contact person: jmeno, prijmeni,
#                                     titulPredJmenem, titulZaJmenem,
#                                     poziceVeSpolecnosti, email, telefon
#   mistoVykonuPrace.pracoviste[].email / .telefon / .nazev
#   upresnujiciInformace              free text — 778 emails in one day's file
#   pozadovanaProfese.cs              ALSO free text, and it looks safe, which is
#                                     the trap: 19,204 DISTINCT values across one
#                                     month's 46,716 rows, 2 of them containing an
#                                     email address. The occupation label is taken
#                                     from MPSV's own cz-isco codelist instead —
#                                     a declared, versioned vocabulary with no
#                                     employer-authored text in it.
#   pozadovanaDovednost[].popis       free text
#   pozadovanaJazykovaZnalost[].popis free text
#   urlAdresa                         free text; one email observed in a day
#   referencniCislo                   an ÚP file number; no analytical value
SOURCE_ALLOWLIST = (
    "portalId",                                       # dedup key ONLY, never emitted
    "typZmenyOpenData.id",                            # the changelog branch
    "zamestnavatel.ico",                              # the entity-graph join
    "profeseCzIsco.id",                               # occupation, coded
    "mesicniMzdaOd",
    "mesicniMzdaDo",
    "typMzdy.id",                                     # mesic | hod — the money branch
    "pocetHodinTydne",
    "pocetMist",
    "datumVlozeni",
    "mistoVykonuPrace.pracoviste[].adresa.kraj.id",   # NUTS-3-equivalent region
)

# `zamestnavatel.nazev` IS NOT ON THE ALLOWLIST, even though §13.6 names
# "employer name" among the safe fields. Two reasons, and the second is why the
# first is not merely tidiness:
#   1. NOTHING HERE USES IT. Distinct employers are counted by IČO, which is the
#      join key; the name added no information.
#   2. For a sole trader the registered company name IS a natural person's name.
#      Reading it into memory when no computation wants it is a surface with no
#      benefit — and the version of this file that DID read it never used the
#      value, which is exactly how such a field survives to the day someone
#      "helpfully" puts it on a record.
# The employer name reaches a record only through scripts/fetch_ares.sh, which
# emits it only for an IČO ARES resolves to a NON-natural-person legal form.
# Fail closed: no ARES answer -> no name -> no employer record at all.

# Contact-shaped KEYS (gate 2). Not a privacy mechanism on their own — gate 1
# already makes them unreachable — but a cheap assertion that gate 1 still holds.
FORBIDDEN_KEY_RE = re.compile(
    r"(email|mail|telefon|phone|mobil|gsm|jmeno|prijmeni|titul|kontakt|osoba|adresa|ulice|psc)",
    re.I)

# ...and the exemption list, which exists because THIS GATE FIRED ON ITS FIRST
# LIVE RUN, on ARES's `obchodniJmeno` — the registered TRADE name of a company,
# which contains the substring "jmeno" and is deliberately carried. That is a
# false positive, and a fail-closed check with false positives is the check
# people switch off (§7.8 makes the same argument about the lints). So the
# exemption is EXACT-MATCH and NAMED, never a loosened pattern: a key has to be
# designed in, by name, to be allowed past a contact-shaped name. Anything the
# design did not name still refuses the run.
KEY_GATE_EXEMPT = frozenset({
    "obchodniJmeno",   # ARES: a company's registered trade name. Whether it may
                       # be PUBLISHED is decided by ares_fold.nameable(), which
                       # drops sole traders — not by this substring test.
})

# ==========================================================================
# THEME TABLE — ordered, first prefix match wins on the CZ-ISCO code
# ==========================================================================
# CZ-ISCO, not the posting's own profession text. The code is present on 100.00%
# of postings (measured: 2,473/2,473 on 2026-08-20) and is a published
# classification with a published codelist; `pozadovanaProfese.cs` is
# employer-authored free text with 19,204 distinct values a month. Choosing the
# coded field over the text field is the same call TED's CPV->sector table makes,
# and it is what keeps this mapping mechanical rather than a judgement.
THEMES = (
    ("it",            "b2b",             ("25", "35", "133")),
    ("health-care",   "health",          ("22", "32", "53")),
    ("education",     "education",       ("23",)),
    ("back-office",   "b2b",             ("4", "241", "242", "331", "334", "335", "121")),
    ("engineering",   "b2b",             ("21", "31")),
    ("logistics",     "mobility",        ("83", "933")),
    # 54 = protective services (police, fire, prison, security). Split out of
    # group 5 because ISCO puts it there and the register would not: the first
    # run without this row filed the Prison Service and the Police under
    # "service and sales workers" / sector retail-services, which is
    # ISCO-correct and register-wrong.
    ("public-safety", "govtech",         ("54",)),
    ("sales-service", "retail-services", ("5", "332")),
    ("manual-trades", "other",           ("6", "7", "8", "9")),
)
THEME_FALLBACK = ("other", "other")

THEME_LABEL = {
    "it": "ICT professionals and technicians",
    "health-care": "Health professionals, associates and personal-care workers",
    "education": "Teaching professionals",
    "back-office": "Clerical, administrative, finance and compliance support",
    "engineering": "Science and engineering professionals and technicians",
    "logistics": "Drivers, mobile-plant operators and transport labourers",
    "public-safety": "Protective-service workers (police, fire, prison, security)",
    "sales-service": "Service and sales workers",
    "manual-trades": "Craft, plant-operator, agricultural and elementary occupations",
    "other": "Managers and occupations outside the mapped themes",
}

# ── HOW MANY EMPLOYER-LEVEL RECORDS, AND WHY THESE TWO NUMBERS ──────────────
# Both are MEASURED against 2026-07 rather than chosen, and both are stated
# because a threshold nobody can re-derive is a magic number.
#
# THE BAR. At the materiality band boundary (>= EUR 200k = scores.money 2) the
# month produced 147 employer aggregates — an order of magnitude past the 8-15
# records/month `docs/architecture-v3.md` §13.4 sizes this feed at, and enough
# for one feed to dominate the `hiring` ledger, which `data/CONVENTIONS.md`
# forbids as a lesson learned. At >= EUR 2M (scores.money 3) it produced ZERO:
# the largest single employer-theme aggregate in the month was EUR 1,846,397, so
# a money-3 bar would have made this record type unreachable while looking like a
# principled choice. EUR 1M is the bar that exists: 9 aggregates in 2026-07.
EMPLOYER_MIN_EUR = 1_000_000
# THE CAP. 9 theme records are structural (one per mapped theme that produced
# anything), so the employer half is what decides whether the month lands inside
# the 8-15 band. 6 is the number that keeps it there. The cap is NOT silent: the
# employers it excludes are still counted inside their theme aggregate, and
# `employer_candidates` on the payload records how many cleared the bar, so the
# gap between "qualified" and "named" is always readable.
EMPLOYER_MAX_RECORDS = 6
# ARES is asked about more than we can name, because it is ARES that decides
# which candidates are nameable at all: an IČO belonging to a sole trader is
# dropped rather than named (its "company name" is a natural person's name).
EMPLOYER_WORKLIST_MAX = 2 * EMPLOYER_MAX_RECORDS

CHANGE_TYPES = ("novy", "zmeneny", "zruseny")
DATASET_URL = "https://data.mpsv.cz/od/soubory/volna-mista-prirustek/"
DOC_URL = "https://data.mpsv.cz/web/data/volna-mista-za-celou-cr"


def die(msg, code=3):
    print(f"mpsv_reduce: {msg}", file=sys.stderr)
    sys.exit(code)


# --------------------------------------------------------------------------
# gate 1 — read ONLY the allowlisted paths
# --------------------------------------------------------------------------

def _walk(node, parts):
    """Yield every value reachable by the remaining path `parts`. `[]` fans out."""
    if not parts:
        yield node
        return
    head, rest = parts[0], parts[1:]
    if head.endswith("[]"):
        key = head[:-2]
        seq = (node or {}).get(key) if isinstance(node, dict) else None
        for el in seq or []:
            yield from _walk(el, rest)
        return
    val = (node or {}).get(head) if isinstance(node, dict) else None
    yield from _walk(val, rest)


def pick(posting):
    """The allowlisted view of one posting. Flat, keyed by the dotted path.

    THE ONLY FUNCTION IN THIS FILE THAT TOUCHES A RAW POSTING. Everything
    downstream reads this dict, so an unlisted field is not merely dropped later
    — it is never in memory under our own key at all.
    """
    out = {}
    for path in SOURCE_ALLOWLIST:
        vals = [v for v in _walk(posting, path.split(".")) if v not in (None, "", [])]
        if not vals:
            continue
        out[path] = vals if path.endswith("[]") or "[]" in path else vals[0]
    return out


# --------------------------------------------------------------------------
# gates 2 and 3 — the produced payload must be clean
# --------------------------------------------------------------------------

def key_violations(node, path=""):
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            if str(k) not in KEY_GATE_EXEMPT and FORBIDDEN_KEY_RE.search(str(k)):
                out.append(f"{path}.{k}")
            out.extend(key_violations(v, f"{path}.{k}"))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            out.extend(key_violations(v, f"{path}[{i}]"))
    return out


def content_violations(text):
    out = []
    for kind, rx in (("email", EMAIL_RE), ("phone", PHONE_RE)):
        for m in rx.finditer(text):
            out.append((kind, m.group(0)[:60]))
            if len(out) >= 25:
                return out
    return out


# --------------------------------------------------------------------------
# arithmetic
# --------------------------------------------------------------------------

def theme_of(isco_code):
    for theme, sector, prefixes in THEMES:
        for p in prefixes:
            if isco_code.startswith(p):
                return theme, sector
    return THEME_FALLBACK


HOURS_DEFAULT = 40.0
_hours_defaulted = [0]   # counted, so the assumption is a number on the payload


def annual_czk(rec):
    """Annualised wage FLOOR for one posting, in CZK, or None if unpriced.

    BRANCHES ON typMzdy AND THAT BRANCH IS LOAD-BEARING. `mesicniMzdaOd` is named
    'monthly' but carries an HOURLY rate whenever typMzdy is `hod` — measured
    258 of 2,473 postings on 2026-08-20, with values of 135-250 (CZK/hour)
    sitting in the same field as 22,400 (CZK/month). Multiplying an hourly rate
    by 12 understates a job by ~99%, silently, and the aggregate is a sum.
    """
    floor = rec.get("mesicniMzdaOd")
    kind = str(rec.get("typMzdy.id") or "").split("/")[-1]
    seats = rec.get("pocetMist") or 1
    try:
        floor = float(floor)
        seats = int(seats)
    except (TypeError, ValueError):
        return None
    if floor <= 0:
        return None
    if kind == "mesic":
        per_seat = floor * 12
    elif kind == "hod":
        # pocetHodinTydne is NOT always present, and an hourly posting without it
        # cannot be annualised without an assumption. The assumption is a full
        # week, it is stated, and every use of it is COUNTED onto the payload as
        # `hours_defaulted` — an unstated default inside a money figure is how a
        # register ends up defending a number nobody can re-derive.
        hours = rec.get("pocetHodinTydne")
        try:
            hours = float(hours)
            if hours <= 0:
                raise ValueError
        except (TypeError, ValueError):
            hours = HOURS_DEFAULT
            _hours_defaulted[0] += 1
        per_seat = floor * hours * 52
    else:
        return None  # unknown wage type: counted as unpriced, never guessed
    return per_seat * seats


def load_codelist(path, want_prefix):
    try:
        doc = json.load(open(path, "r", encoding="utf-8"))
    except (OSError, ValueError) as e:
        die(f"codelist {path}: {e}")
    out = {}
    for it in doc.get("polozky") or []:
        cid = str(it.get("id") or "")
        if not cid.startswith(want_prefix):
            continue
        nm = it.get("nazev")
        if isinstance(nm, dict):
            nm = nm.get("cs") or ""
        out[cid] = collapse(nm)
    return out


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--month", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--isco", required=True)
    ap.add_argument("--kraje", required=True)
    ap.add_argument("--worklist", required=True)
    ap.add_argument("--days-absent", default="")
    ap.add_argument("--days-expected", type=int, default=0)
    ap.add_argument("--upstream-bytes", type=int, default=0)
    ap.add_argument("--keep-work", action="store_true")
    ap.add_argument("--plant-personal-data", action="store_true",
                    help="TEST ONLY: copy one posting's contact block into the "
                         "payload to prove the privacy gates refuse it.")
    a = ap.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}", a.month):
        die(f"--month must be YYYY-MM, got {a.month!r}")

    isco_names = load_codelist(a.isco, "CzIsco/")
    kraj_names = load_codelist(a.kraje, "Kraj/")

    files = sorted(glob.glob(os.path.join(a.work, "*.json.gz")))
    if not files:
        die(f"no day payloads in {a.work}")

    # ---- read + gate 1 ---------------------------------------------------
    # `latest` keeps the LAST row seen for a portalId (its current state);
    # `is_new` records whether that posting was ever announced as `novy`.
    # THE CHANGELOG TRAP (architecture §13.7): the increment is a changelog, not
    # a list of new items. Measured over 2026-07: 46,716 rows -> 35,921 distinct
    # postings -> 6,597 novy. Counting rows instead of novy postings is a 7.1x
    # flood into an append-only public log.
    latest, is_new = {}, set()
    change_rows = collections.Counter()
    change_postings = collections.Counter()
    row_ct = collections.Counter()      # (portalId, change type) -> row count
    rows = 0
    planted = None
    for f in files:
        try:
            doc = json.load(gzip.open(f, "rt", encoding="utf-8"))
        except (OSError, ValueError) as e:
            die(f"{os.path.basename(f)}: unreadable increment — {e}")
        for posting in doc.get("polozky") or []:
            rows += 1
            ct = str((posting.get("typZmenyOpenData") or {}).get("id") or "").split("/")[-1]
            change_rows[ct] += 1
            pid = posting.get("portalId")
            if pid is None:
                continue
            if a.plant_personal_data and planted is None:
                planted = (posting.get("prvniKontaktSeZamestnavatelem") or {}).get("komuSeHlasit")
            if ct == "novy":
                is_new.add(pid)
            row_ct[(pid, ct)] += 1
            latest[pid] = (ct, pick(posting))     # <-- GATE 1: nothing else survives
    for pid, (ct, _) in latest.items():
        change_postings[ct] += 1

    # ---- aggregate (BEFORE materiality, by law) --------------------------
    def blank():
        return {"postings": 0, "seats": 0, "czk": 0.0, "unpriced": 0,
                "icos": set(), "iscos": collections.Counter(),
                "kraje": collections.Counter(),
                "change": collections.Counter()}

    by_theme = collections.defaultdict(blank)
    by_emp = collections.defaultdict(blank)

    # THE CHANGE CENSUS IS PER THEME, over EVERY ROW in the window — not just the
    # new ones. It is what makes `typZmenyOpenData` a real number on the record
    # instead of a token that satisfies the contract check: a theme with 405 new
    # and 2,088 cancelled rows is telling you something `novy` alone cannot.
    #
    # ROWS, attributed to the theme of the posting's LATEST state. That pairing is
    # deliberate: a posting carries at most one `novy` row (verified over 2026-07
    # — 6,597 novy rows, 6,597 distinct postings with a novy row), so counting
    # rows this way makes `typZmenyOpenData.novy` EQUAL `postings` on every
    # record. Counting distinct postings by their last state instead produced
    # employer records reading `novy: 0` next to `postings: 7`, because a posting
    # announced on the 3rd and edited on the 20th ends the window as `zmeneny` —
    # a contradiction on the face of the record.
    for (pid, ct), n in row_ct.items():
        row = latest.get(pid)
        if not row:
            continue
        rec = row[1]
        isco = str(rec.get("profeseCzIsco.id") or "").split("/")[-1]
        theme, _s = theme_of(isco)
        by_theme[theme]["change"][ct] += n
        ico = str(rec.get("zamestnavatel.ico") or "")
        if ico:
            by_emp[(ico, theme)]["change"][ct] += n

    ico_present = 0
    for pid in is_new:
        row = latest.get(pid)
        if not row:
            continue
        rec = row[1]
        isco = str(rec.get("profeseCzIsco.id") or "").split("/")[-1]
        theme, _sector = theme_of(isco)
        ico = str(rec.get("zamestnavatel.ico") or "")
        if ico:
            ico_present += 1
        czk = annual_czk(rec)
        seats = int(rec.get("pocetMist") or 1)
        targets = [by_theme[theme]]
        if ico:
            targets.append(by_emp[(ico, theme)])
        for t in targets:
            t["postings"] += 1
            t["seats"] += seats
            if czk is None:
                t["unpriced"] += 1
            else:
                t["czk"] += czk
            if ico:
                t["icos"].add(ico)
            if isco:
                t["iscos"][isco] += 1
            for k in rec.get("mistoVykonuPrace.pracoviste[].adresa.kraj.id") or []:
                t["kraje"][str(k)] += 1

    new_total = len(is_new)
    # The record's `date` is the LAST DAY OF THE AGGREGATED MONTH — the day the
    # window closed. Not the run date (the ledger FILENAME carries that) and not
    # any posting's own date (an aggregate has thousands).
    _y, _m = (int(x) for x in a.month.split("-"))
    month_end = f"{a.month}-{calendar.monthrange(_y, _m)[1]:02d}"

    def money_eur(t):
        return int(round(t["czk"] / CZK_PER_EUR)) if t["czk"] else None

    def top_iscos(t, n=4):
        return [{"code": c, "label": isco_names.get(f"CzIsco/{c}", ""), "postings": v}
                for c, v in t["iscos"].most_common(n)]

    def regions(t, n=4):
        return [{"kraj": k, "label": kraj_names.get(k, ""), "postings": v}
                for k, v in t["kraje"].most_common(n)]

    def quote_for(t):
        """ONE CONTIGUOUS VERBATIM SPAN (architecture §7.8 'a quote is ONE
        CONTIGUOUS SPAN ... Never join fields'). The span is the official Czech
        name of the single most-posted CZ-ISCO occupation in the aggregate, taken
        verbatim from MPSV's own cz-isco codelist. It is a literal substring of
        the payload this reducer writes, so normalize.py's substring check
        verifies it rather than waving it through."""
        top = t["iscos"].most_common(1)
        if not top:
            return ""
        return isco_names.get(f"CzIsco/{top[0][0]}", "")[:300]

    items = []
    for theme, sector, _p in THEMES + ((THEME_FALLBACK[0], THEME_FALLBACK[1], ()),):
        t = by_theme.get(theme)
        if not t or t["postings"] == 0:
            continue
        items.append({
            "id": f"mpsv-{a.month}-{theme}",
            "kind": "theme",
            "month": a.month,
            "date": month_end,
            "theme": theme,
            "theme_label": THEME_LABEL[theme],
            "sector": sector,
            "ico": None,
            "employer": None,
            # THE CHANGELOG BRANCH, CARRIED ONTO EVERY ITEM ON PURPOSE.
            # data/feeds.json lists `typZmenyOpenData` in required_fields, so
            # normalize's FIELDS check (§7.2 step 3) fails the feed the moment a
            # future edit stops branching on change type. "The parser branches on
            # change type" becomes a mechanically enforced contract term instead
            # of a sentence in a doc.
            "typZmenyOpenData": {
                "counted": "novy",
                "novy": t["change"].get("novy", 0),
                "zmeneny": t["change"].get("zmeneny", 0),
                "zruseny": t["change"].get("zruseny", 0),
            },
            "postings": t["postings"],
            "seats": t["seats"],
            "employers": len(t["icos"]),
            "unpriced_postings": t["unpriced"],
            "money_eur": money_eur(t),
            "money_note": (
                f"{t['postings']} new ÚP vacancies ({t['seats']} seats) in {a.month}, "
                f"annualised wage FLOOR (mesicniMzdaOd x 12 monthly / x hours x 52 hourly, "
                f"x pocetMist), summed and converted at a fixed {CZK_PER_EUR} CZK/EUR; "
                f"{t['unpriced']} posting(s) carried no usable floor and contribute 0"),
            "isco_top": top_iscos(t),
            "regions": regions(t),
            "quote": quote_for(t),
            "url": DATASET_URL,
        })

    employer_items = []
    for (ico, theme), t in by_emp.items():
        m = money_eur(t)
        if m is None or m < EMPLOYER_MIN_EUR:
            continue
        sector = dict((k, s) for k, s, _ in THEMES).get(theme, "other")
        employer_items.append({
            "id": f"mpsv-{a.month}-{ico}-{theme}",
            "kind": "employer",
            "month": a.month,
            "date": month_end,
            "theme": theme,
            "theme_label": THEME_LABEL[theme],
            "sector": sector,
            "ico": ico,
            # FILLED BY scripts/fetch_ares.sh, AND ONLY FOR A NON-NATURAL-PERSON
            # LEGAL FORM. Left null here so that an MPSV run without ARES cannot
            # publish a sole trader's personal name: fetch_ares.sh DROPS every
            # employer item it could not clear.
            "employer": None,
            "employer_cleared": False,
            "typZmenyOpenData": {
                "counted": "novy",
                "novy": t["change"].get("novy", 0),
                "zmeneny": t["change"].get("zmeneny", 0),
                "zruseny": t["change"].get("zruseny", 0),
            },
            "postings": t["postings"],
            "seats": t["seats"],
            "employers": 1,
            "unpriced_postings": t["unpriced"],
            "money_eur": m,
            "money_note": (
                f"{t['postings']} new ÚP vacancies ({t['seats']} seats) posted by IČO {ico} "
                f"in {a.month}, annualised wage FLOOR summed and converted at a fixed "
                f"{CZK_PER_EUR} CZK/EUR"),
            "isco_top": top_iscos(t),
            "regions": regions(t),
            "quote": quote_for(t),
            "url": f"https://ares.gov.cz/ekonomicke-subjekty?ico={ico}",
        })
    employer_items.sort(key=lambda r: -r["money_eur"])
    employer_candidates = len(employer_items)
    employer_items = employer_items[:EMPLOYER_WORKLIST_MAX]
    for i, r in enumerate(employer_items):
        # The rank fetch_ares.sh keeps against EMPLOYER_MAX_RECORDS once it knows
        # which of these IČOs are nameable at all.
        r["candidate_rank"] = i + 1
    items.extend(employer_items)

    absent = [d for d in a.days_absent.split(",") if d]
    payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "mpsv",
        "dataset": "volna-mista-prirustek",
        "documentation": DOC_URL,
        "month": a.month,
        "window": {
            "days_expected": a.days_expected or len(files) + len(absent),
            "days_present": len(files),
            "days_absent": absent,
        },
        "upstream_bytes": a.upstream_bytes,
        "raw_rows": rows,
        "distinct_postings": len(latest),
        "new_postings": new_total,
        "ico_coverage": round(ico_present / new_total, 4) if new_total else None,
        "change_rows": {k: change_rows.get(k, 0) for k in CHANGE_TYPES},
        "change_postings": {k: change_postings.get(k, 0) for k in CHANGE_TYPES},
        "hours_defaulted": _hours_defaulted[0],
        "hours_default": HOURS_DEFAULT,
        "employer_bar_eur": EMPLOYER_MIN_EUR,
        "employer_candidates": employer_candidates,
        "employer_max_records": EMPLOYER_MAX_RECORDS,
        # `items` is one of the list keys scripts/normalize.py's generic JSON
        # parser already recognises, so this payload needs no parser change.
        "items": items,
    }
    if a.plant_personal_data:
        if not planted:
            die("--plant-personal-data: no contact block found to plant", 3)
        payload["items"][0]["_planted_contact"] = planted

    # ---- gates 2 and 3 ---------------------------------------------------
    text = json.dumps(payload, ensure_ascii=False, indent=1)
    bad_keys = key_violations(payload)
    bad_content = content_violations(text)
    if bad_keys or bad_content:
        print("AC-GDPR1 REFUSED — nothing written to " + a.out, file=sys.stderr)
        print("The MPSV payload is PUBLIC-ADJACENT and the ledgers it feeds are "
              "append-only and public. Fail closed.", file=sys.stderr)
        for k in bad_keys[:10]:
            print(f"  contact-shaped key : {k}", file=sys.stderr)
        for kind, snip in bad_content[:10]:
            print(f"  contact content    : {kind}: {snip}", file=sys.stderr)
        if not a.keep_work:
            shutil.rmtree(a.work, ignore_errors=True)
        sys.exit(2)

    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(text)

    os.makedirs(os.path.dirname(os.path.abspath(a.worklist)) or ".", exist_ok=True)
    with open(a.worklist, "w", encoding="utf-8") as fh:
        for r in employer_items:
            fh.write(r["ico"] + "\n")

    # ---- the work directory carried the personal data. It goes now. ------
    if not a.keep_work:
        shutil.rmtree(a.work, ignore_errors=True)

    print(f"mpsv_reduce: {a.month}: {len(files)} day file(s), {rows} rows -> "
          f"{len(latest)} distinct postings -> {new_total} novy -> "
          f"{len(items)} aggregate(s) "
          f"({len(items) - len(employer_items)} theme + {len(employer_items)} employer)")
    print(f"mpsv_reduce: privacy gates PASSED (allowlist {len(SOURCE_ALLOWLIST)} paths, "
          f"0 contact keys, 0 contact strings in {len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
