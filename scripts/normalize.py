#!/usr/bin/env python3
"""
scripts/normalize.py — raw payloads -> staged records -> canonical ledger.

THREE MODES, and the split between them is the whole design:

  --mechanical-only   THE ARITHMETIC PATH. Runs with NO model, NO secrets and NO
                      network. Evaluates every feed's contract, mints canonical
                      ids, dedups against seen.txt, computes scores.money and
                      dated scores.urgency, extracts and VERIFIES the quote, and
                      writes:
                          <raw>/staged.jsonl    mechanical records + what each
                                                still needs from a model
                          <raw>/contract.json   the fetch_log seam for db.py
                          <raw>/manifest.md     the committed human record
                      It appends NOTHING to the ledgers. That is deliberate.

  --complete          THE ATTENDED COMPLETION. Reads a staged.jsonl whose model
                      fields an agent has filled in, applies the materiality
                      filter, and appends survivors to
                      data/signals/<type>/<date>.jsonl + seen.txt. Needs no
                      model of its own — the judgment already happened. It does
                      NOT touch data/register.db: it prints the `db.py upsert`
                      lines for the caller to run, because the ledgers are
                      canonical and the DB is rebuildable from them.

  (default)           The UNATTENDED path: mechanical, then model passes A and B.
                      LIVE since 2026-08-20 — see the model_passes() docstring.
                      It never makes the model call itself. It drives ONE of two
                      drivers and says which: SUBAGENT (default, no API credit —
                      scripts/model_pass_agent.py, filled by a session's
                      subagents) or API (--model-driver api — scripts/
                      model_pass.sh, which SPENDS the credit balance). It still
                      appends NOTHING: it fills staged.jsonl and hands over to
                      --complete.

WHY MECHANICAL-ONLY APPENDS NOTHING. Every record needs `scale` and
`recurrence`, and both are model judgments. The law is that unscored records are
never appended with default scores: losing freshness is recoverable, writing
vibes into an append-only canonical ledger is not. So the mechanical pass STAGES
and the manifest lists the staged records as pending — which is exactly what the
wrapper means when it prints "Mechanical records staged; run ATTENDED mode".
"""

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEEDS_JSON = os.path.join(ROOT, "data", "feeds.json")
DEFAULT_SIGNALS_DIR = os.path.join(ROOT, "data", "signals")

# ── the sibling extractor modules ────────────────────────────────────────────
# Four feeds are big enough to own a file: their payloads are ZIPs and monthly
# bulk dumps that get reduced to aggregates, and inlining that here would double
# this file. They are imported, not re-implemented, so there is exactly one
# definition of each feed's shape.
#
# THE sys.path LINE IS NOT DECORATION. `sys.path[0]` is the SCRIPT'S directory
# only when normalize.py is the entry point. scripts/model_pass.py imports
# normalize precisely so the two halves of the model seam cannot drift, and a
# future importer may sit somewhere else entirely — at which point a bare
# `import coi_extract` raises ImportError at module load and takes the whole
# pipeline down. Deriving the path from __file__ makes the import work from any
# cwd and any importer.
_SCRIPTS = os.path.join(ROOT, "scripts")
if _SCRIPTS not in sys.path:
    sys.path.insert(0, _SCRIPTS)
import coi_extract    # noqa: E402
import nen_extract    # noqa: E402
import sukl_extract   # noqa: E402
from mpsv_extract import extract_mpsv  # noqa: E402
# The two `asks` feeds (2026-09-03). Each owns a file for the nen reason: the
# fetcher's payload reader, the MODE-A guards and the extractor share one module
# so the self-test drives the same code the run does.
import hack_extract   # noqa: E402
import tacr_extract   # noqa: E402

# A FIXED, STATED ASSUMPTION, not a live rate. Ingest must run with no network,
# so money_eur derived from a CZK figure uses this constant and money_note says
# so. A record whose EUR value matters to a decision is re-checked by a human,
# not silently re-derived from whatever the rate was that morning.
CZK_PER_EUR = 25.0

# CPV_SECTOR IS DEAD — selection law, owner mandate 2026-08-24. A fetch script
# selects only by a uniform numeric threshold and/or a complete taxonomy, never
# by invented keywords, and keywords/categories become LABELS applied in the
# model half. The dict that stood here mapped fetch_ted.sh's five hand-picked
# CPV groups (it/health/bizserv/energy/construction) to sectors — mechanical
# classification riding on a judgment-shaped group list. fetch_ted.sh now
# issues one all-CPV jurisdiction query (ted-all.json), so there is no group
# key to map: `sector` on a ted record is None at staging, lands in `_needs`
# like every other model field, and is filled by model pass A alongside scale
# and recurrence. (hlidac records always worked this way — their extractor
# never set a sector.)

# Payload filename -> registry feed key. THIS IS A SEAM with the fetchers, which
# a different worker owns: they choose filenames, this table reads them.
#
# TOKEN MATCHING, NOT ANCHORED PATTERNS — and that is a correction, not a
# preference. The first draft anchored on exact names (`^(yc|yc-oss|all)\.json$`,
# `^(cc-cz|czechcrunch).*`) and was MEASURED against the fetchers' real output on
# 2026-08-20: both live payloads, `yc-all.json` and `feed-czechcrunch.xml`, fell
# through as UNMAPPED. A filename convention agreed across a program boundary is
# exactly the kind of shape that drifts, so this matches a distinctive TOKEN
# anywhere in the name and is ordered specific-before-generic.
#
# An unmapped payload is still never silently dropped — it is named in the
# manifest, because a file nobody parsed is indistinguishable from a feed that
# produced nothing.
FILE_FEED_TOKENS = [
    ("hlidac", "hlidac"),
    # `smlouvy-<date>.jsonl`, written by scripts/fetch_smlouvy.sh from the
    # OFFICIAL registr smluv bulk dump. Placed here rather than appended at the
    # end because this list is FIRST-MATCH-WINS and the token has to be checked
    # before any shorter token that could appear inside the same filename;
    # verified 2026-08-21 that "smlouvy" contains none of the tokens below and
    # no other fetcher writes a filename containing it.
    ("smlouvy", "smlouvy"),
    ("czechcrunch", "cc-cz"), ("cc-cz", "cc-cz"),
    ("vestbee", "vestbee"),
    ("suggest", "suggest"),
    # The two ENRICHMENT marketplaces. Mapped on purpose rather than left to
    # fall through as unmapped: an unmapped payload is parsed by NOBODY, so its
    # transport receipt and its contract are never checked and the file is
    # merely named in the manifest. Mapping them puts `shoptet-addons.jsonl` and
    # `upgates-addons.jsonl` under their own registry rows, exactly as `ares`
    # already is, and their `items_kept: 0` is then the DECLARED enrichment
    # outcome (role: enrichment, id_prefixes: []) instead of an unexplained zero.
    # See the enrichment exemption in the extraction loop below.
    ("shoptet", "shoptet"), ("upgates", "upgates"),
    # `coi` MUST be here and not only in EXTRACTORS. Without the token,
    # `coi-<period>.json` is an UNMAPPED payload and the feed fails a DIFFERENT
    # way from a missing extractor — no contract is evaluated at all, so the
    # manifest shows the file as unclaimed rather than showing the feed as
    # broken. Verified 2026-08-21 that no other fetcher writes a filename
    # containing `coi`, and that `coi-*.json` contains none of the tokens above.
    # `veklep` sits ABOVE the short generic tokens on the first-match-wins rule.
    # Verified 2026-08-25: `veklep-p<N>.json` (the only name fetch_veklep.sh
    # writes) contains none of the tokens below, and no other fetcher writes a
    # filename containing `veklep`.
    ("veklep", "veklep"),
    # The two `asks` payloads, `tacr-needs.jsonl` and `hack-challenges.jsonl`.
    # Above the short generic tokens on the first-match-wins rule. Verified
    # 2026-09-03: neither name contains nen / ted / yc / hys / ares / coi, and
    # no other fetcher writes a filename containing `tacr` or `hack`.
    ("tacr", "tacr"), ("hack", "hackathon"),
    ("nku", "nku"), ("sukl", "sukl"), ("mpsv", "mpsv"), ("ares", "ares"),
    ("coi", "coi"),
    ("hys", "ec-hys"),
    ("nen", "nen"),
    ("ted", "ted"),
    ("yc", "yc-oss"),
]

# Reddit is the one filename shape the flat table above cannot decide, and the
# reason is measured, not theoretical. scripts/fetch_reddit.sh emits
# `reddit-<sub>-new.rss` for the firehose and `reddit-<sub>-q-<term>.rss` for
# the pain search — READ OFF THE SCRIPT, not assumed. Neither name contains the
# string `reddit-search`, so the three `reddit*search*` tokens the table used to
# carry matched NOTHING the fetcher writes, every search payload fell through to
# the generic `reddit` token, and all four subs' search results were filed under
# `reddit-new`. That misattribution is silent: both keys parse identically, so
# the only symptoms are a yield anomaly charged to the wrong contract and a
# `reddit-search` row that reads PENDING forever while its fetcher runs fine.
REDDIT_SEARCH_MARKERS = ("-q-", "search")

# ==========================================================================
# AC-GDPR1 — the contact-field gate. A SAFETY GATE, NOT A FEATURE.
# ==========================================================================
#
# Our ledgers are PUBLIC, APPEND-ONLY and on GitHub. A personal-data leak is
# permanent, irreversible and published; there is no quiet cleanup, no force-push
# that un-rings the bell. So this runs BEFORE anything is written to JSONL or the
# DB, never as a post-hoc scrub.
#
# ALLOWLIST, NEVER DENYLIST. Only the fields named below may enter a ledger
# record; everything else is dropped, whether or not anyone anticipated it. A
# denylist fails OPEN the day a source adds a field — which is precisely how this
# would break, because MPSV's own DCAT record declares `obsahuje-osobní-údaje`
# (contact names, emails, phones) and its field set is not ours to freeze. An
# allowlist fails CLOSED: an unknown field is dropped by default, so a new
# contact column is a no-op instead of a disclosure.
#
# The mechanism is FEED-AGNOSTIC even though MPSV is the trigger. Any future feed
# carrying personal data gets the same protection without anyone remembering to
# ask for it.
#
# The safe field set is the signal record schema itself (CONVENTIONS.md) plus the
# four receipt fields. For MPSV specifically these are the named-safe inputs that
# survive into it: IČO, CZ-ISCO, salary floor, NUTS-3, employer name, posting
# date, change type — all of which are organisational, none personal.
LEDGER_ALLOWLIST = (
    "id", "source", "url", "date", "title", "sector", "geo_origin",
    "money_eur", "money_note", "summary", "scores", "notes",
    "quote", "http_status", "fetched_at", "extraction",
)

# The second layer. The allowlist governs FIELDS; this governs CONTENT, because
# personal data can arrive inside a field that is itself legitimate — an email
# quoted in a `summary`, a phone number inside a verbatim `quote`.
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

# Deliberately NOT a bare 9-digit run. An 8-digit IČO, a 6-digit EUR figure and a
# CZK contract value would all match a naive \d{9} pattern, and a gate that fires
# on every tender value gets switched off within a fortnight. This requires an
# explicit country prefix or an explicit tel/mobil label.
PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)


# OPTIONAL KEYS ARE OMITTED WHEN EMPTY, never written as "" or null.
#
# SignalSchema declares these `.optional()`, and in zod that accepts UNDEFINED —
# not null, and not the empty string. `quote` additionally carries `.min(1)`.
# CONVENTIONS.md states the rule in words ("an empty `quote` is not a quote, it
# is the shape that looks present and says nothing, and the schema rejects it");
# this line is what makes it true in code.
#
# NOT HYPOTHETICAL, and today's corpus is the only reason it has not fired:
# `quote` is set to "" whenever no candidate snippet verifies against the
# payload — normalize counts exactly those as `quote_failures`, so it expects
# them — and `http_status` is None for any feed whose fetcher left no receipt,
# which is the documented UNKNOWN case. Either value reaching a ledger is a red
# build on the next deploy, and the ledgers are append-only: there is no quiet
# cleanup. Measured: 0 of 4,788 staged records currently carry an empty quote,
# which is luck about this corpus, not a property of the code.
OPTIONAL_RECEIPTS = ("quote", "http_status", "fetched_at", "extraction", "notes")


def apply_allowlist(rec):
    """Return (clean_record, dropped_field_names). Unknown fields never survive."""
    clean = {k: v for k, v in rec.items()
             if k in LEDGER_ALLOWLIST
             and not (k in OPTIONAL_RECEIPTS and v in (None, "", []))}
    # `dropped` reports UNKNOWN fields — the thing the allowlist exists to catch.
    # An omitted-because-empty optional receipt is not a drop, it is the schema
    # being honoured, and conflating the two would bury the signal.
    dropped = sorted(k for k in rec if k not in LEDGER_ALLOWLIST)
    return clean, dropped


def gdpr_violations(rec):
    """
    Personal-data hits in an already-allowlisted record. Returns
    [(field, kind, snippet)] — empty means the record may be written.
    """
    out = []
    for field, value in rec.items():
        for s in item_strings(value):
            for kind, rx in (("email", EMAIL_RE), ("phone", PHONE_RE)):
                m = rx.search(s)
                if m:
                    out.append((field, kind, m.group(0)[:60]))
    return out


_WS = re.compile(r"\s+")


def log(m):
    print(m, file=sys.stderr)


def collapse(s):
    """Whitespace-collapsed text — the form every quote check compares against."""
    return _WS.sub(" ", str(s or "")).strip()


def sha1_8(s):
    return hashlib.sha1(str(s).encode("utf-8")).hexdigest()[:8]


def slugify(s):
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:48] or "x"


ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# SignalSchema's `isoTimestamp` (web/lib/data.ts), transcribed. A receipt is
# written by a fetcher we do not own, so its `started_at` is checked against the
# shape the ledger will demand BEFORE it is copied onto a record — a receipt
# that fails this is dropped to "unknown", never passed through to become a red
# build in an append-only log.
ISO_TS_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(\.\d+)?(Z|[+-]\d{2}:\d{2})$")


def iso_date(value):
    """Any feed's published date -> 'YYYY-MM-DD', or None if it cannot be read.

    NEVER A TRUNCATION, and that is the point. Every extractor used to do
    `str(d)[:10]`, which is only correct if you already know the format — and
    the four live feeds use four different ones. MEASURED on the committed
    2026-08-20 payloads, before this existed:

      cc-cz   RSS pubDate 'Thu, 20 Aug 2026 08:00:30 +0000'  -> 'Thu, 20 Au'
      yc-oss  launched_at 1322045523 (UNIX epoch seconds)    -> '1322045523'

    That was 4,397 of 4,397 staged records carrying an unusable date, and the
    damage did not stop at the field: run_complete() named the ledger file after
    it, so a completed run would have written
    `data/signals/funded/Thu, 20 Au.jsonl` and then failed the next site build on
    SignalSchema's ISO-date rule. Nobody had seen it because the geo_origin
    defect above refused every record one step earlier.

    Handled, in order: ISO date or datetime · compact YYYYMMDD (TED) ·
    RFC-2822 (RSS) · UNIX epoch seconds or milliseconds (yc-oss). Anything else
    returns None, which puts `date` into the record's model debt and names it in
    the manifest — an unread date is reported, never guessed.
    """
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    s = collapse(value)
    if not s:
        return None
    if ISO_DATE_RE.match(s[:10]):
        return s[:10]
    if re.match(r"^(19|20)\d{6}$", s):            # TED-style 20260601
        return f"{s[0:4]}-{s[4:6]}-{s[6:8]}"
    if re.match(r"^\d{9,13}$", s):                # epoch seconds or millis
        n = int(s)
        if len(s) >= 12:
            n //= 1000
        try:
            return datetime.fromtimestamp(n, timezone.utc).date().isoformat()
        except (OverflowError, OSError, ValueError):
            return None
    try:
        return parsedate_to_datetime(s).date().isoformat()
    except (TypeError, ValueError, IndexError):
        return None


# --------------------------------------------------------------------------
# the arithmetic scorers
# --------------------------------------------------------------------------

def score_money(money_eur):
    """0 none/unknown · 1 <200k · 2 200k-2M · 3 >2M. Pure arithmetic."""
    if money_eur is None:
        return 0
    v = float(money_eur)
    if v < 200_000:
        return 1
    if v <= 2_000_000:
        return 2
    return 3


def months_between(d0, d1):
    return (d1.year - d0.year) * 12 + (d1.month - d0.month) + (d1.day - d0.day) / 30.0


def score_urgency(event_date, today):
    """
    0 none · 1 dated event >18mo out · 2 <=18mo · 3 <6mo.

    Grade 3's OTHER branch — "already in force with active enforcement" — is a
    judgement about enforcement and is NOT decided here; it stays a model field.
    A past date returns None so the model can rule on it rather than having this
    function quietly assert enforcement it cannot observe.
    """
    if not event_date:
        return 0
    try:
        d = date.fromisoformat(str(event_date)[:10])
    except ValueError:
        return 0
    m = months_between(today, d)
    if m < 0:
        return None  # in the past: enforcement is a model call, not arithmetic
    if m < 6:
        return 3
    if m <= 18:
        return 2
    return 1


def is_material(scores):
    """Drop only if money <= 1 AND scale <= 1 AND urgency == 0."""
    return not (scores.get("money", 0) <= 1
                and scores.get("scale", 0) <= 1
                and scores.get("urgency", 0) == 0)


# --------------------------------------------------------------------------
# payload parsing
# --------------------------------------------------------------------------

def feed_for_file(fname):
    n = fname.lower()
    if "reddit" in n:
        return ("reddit-search"
                if any(m in n for m in REDDIT_SEARCH_MARKERS) else "reddit-new")
    for token, key in FILE_FEED_TOKENS:
        if token in n:
            return key
    return None


# The SUB-FEED key inside one feed's payload set — `ted-all.json` -> `all`,
# `hlidac-firehose-p3.json` -> `firehose`. Since 2026-08-24 NO extractor derives
# a field from it (the CPV-group->sector mapping is dead; see the CPV_SECTOR
# obituary above), but the key is still passed to every extractor and still
# names the payload file an item came from. The optional `-p<N>` tail is a
# fetcher's page number and is not part of the key. Returns None for any other
# filename.
PAYLOAD_KEY_RE = re.compile(r"^(?:ted|hlidac)-(.+?)(?:-p\d+)?\.json$", re.I)


def payload_key_of(fname):
    m = PAYLOAD_KEY_RE.match(fname)
    return m.group(1) if m else None


def run_date_from_raw(raw):
    """The run date a `data/raw/<date>/` directory names, or None.

    The directory name IS the run date — ingest.sh creates it as
    `data/raw/$(date +%Y-%m-%d)` and db.py reads the same string back off the
    ledger filenames. Anything else (a scratch dir, a path with no date) returns
    None so the caller can fall back rather than invent one."""
    name = os.path.basename(os.path.normpath(str(raw or "")))
    return name if ISO_DATE_RE.match(name) else None


def parse_payload(path, parse_kind):
    """
    Returns (items, parse_ok, err). Never raises: a parse failure is a contract
    result, not a crash — the run must still produce a manifest and a fetch_log
    row saying what happened.
    """
    try:
        raw = open(path, "r", encoding="utf-8", errors="replace").read()
    except OSError as e:
        return [], False, f"unreadable: {e}"
    # AN EMPTY FILE IS NOT A PARSE FAILURE. It used to be, and that was wrong
    # for every feed that writes MORE THAN ONE file — one empty member poisoned
    # the whole feed's contract while its other files carried perfectly good
    # data. MEASURED 2026-08-21: `shoptet` writes `shoptet-addons.jsonl` AND
    # `shoptet-vendors.jsonl`, and its STEADY STATE is an unchanged marketplace
    # -> 0 new add-on rows -> a 0-byte addons file beside 179 good vendor rows.
    # That read as `parse: shoptet-addons.jsonl: zero bytes`, i.e. the feed
    # reported BROKEN on the day it worked exactly as designed. The same shape
    # exists on `hlidac-<query>-p<N>.json` the moment a query has fewer pages
    # than the fetcher asks for.
    #
    # NOTHING IS LOST BY THIS. "The feed produced no bytes at all" is already
    # checked one level up and at the right granularity — evaluate_contract
    # step 1 fails on `nbytes == 0` summed across the feed's files, with the
    # `zero` yield anomaly. This check was a second, per-file copy of that rule
    # applied where the rule does not hold.
    if not raw.strip():
        return [], True, None

    try:
        if parse_kind == "json":
            doc = json.loads(raw)
            if isinstance(doc, list):
                return doc, True, None
            for k in ("notices", "results", "items", "data", "companies"):
                if isinstance(doc.get(k), list):
                    return doc[k], True, None
            return [doc], True, None
        if parse_kind == "jsonl":
            out = []
            for line in raw.splitlines():
                if line.strip():
                    out.append(json.loads(line))
            return out, True, None
        if parse_kind == "rss":
            root = ElementTree.fromstring(raw)
            items = []
            for tag in (".//item", ".//{http://www.w3.org/2005/Atom}entry"):
                items.extend(root.findall(tag))
            out = []
            for it in items:
                d = {}
                for child in it:
                    name = child.tag.split("}")[-1]
                    val = (child.text or "").strip()
                    if not val and name == "link":
                        val = child.attrib.get("href", "")
                    d.setdefault(name, val)
                out.append(d)
            return out, True, None
        if parse_kind in ("csv",):
            import csv as _csv
            return list(_csv.DictReader(raw.splitlines())), True, None
        # html-table / pdf-text / manual: no structured parser here. This is the
        # designed entry point to LLM-fallback extraction, not a defect.
        return [], False, f"no structured parser for parse={parse_kind}"
    except Exception as e:  # noqa: BLE001
        return [], False, f"{type(e).__name__}: {e}"


def get_first(d, *keys):
    for k in keys:
        v = d.get(k)
        if v not in (None, "", []):
            return v
    return None


def item_strings(obj, depth=0):
    """Every string reachable inside one parsed payload item — the haystack a
    quote is checked against, in the same decoded form the extractor read it."""
    if depth > 6:
        return []
    if isinstance(obj, str):
        return [obj]
    if isinstance(obj, dict):
        out = []
        for v in obj.values():
            out.extend(item_strings(v, depth + 1))
        return out
    if isinstance(obj, (list, tuple)):
        out = []
        for v in obj:
            out.extend(item_strings(v, depth + 1))
        return out
    return []


# --------------------------------------------------------------------------
# per-feed record extraction — the mechanical half
# --------------------------------------------------------------------------

def money_from_czk(czk):
    try:
        return round(float(czk) / CZK_PER_EUR)
    except (TypeError, ValueError):
        return None


def flat(v):
    """TED returns many fields as lists or {lang: [..]} maps. Take the first scalar."""
    while isinstance(v, (list, tuple)) and v:
        v = v[0]
    if isinstance(v, dict):
        for k in ("eng", "en", "ces", "cs"):
            if k in v:
                return flat(v[k])
        vals = list(v.values())
        return flat(vals[0]) if vals else None
    return v


# ==========================================================================
# THE COUNTERPARTY — who actually WINS the contract
# ==========================================================================
#
# Every tender feed we fetch names two sides, and until now we kept one. The
# buyer reaches `title` (house convention: "Buyer — what it is") and the
# SUPPLIER was dropped on the floor in three separate places:
#   · Hlídač returns `prijemce[]` with ico; extract_hlidac read `platce` only.
#   · TED exposes `winner-name` / `winner-identifier`; fetch_ted.sh never asked.
#   · data.smlouvy.gov.cz carries <smluvniStrana><ico>; we did not fetch it.
# MEASURED consequence, 2026-08-21: entity_ico populated on 55 of 9,324 signals
# (0.6%), and 0 of 3,200 TED records. The joined database was never built.
#
# WHY `notes` AND NOT A NEW FIELD. `SignalSchema` (web/lib/data.ts) is a
# z.strictObject and CONVENTIONS.md makes any new optional field a same-change
# schema edit — in a file this program does not own. `notes` is already
# allowlisted, already optional, already free text ("absence checks, transfer
# logic"), and NO mechanical extractor writes it today, so there is nothing to
# collide with. The line below is therefore additive with ZERO schema risk, and
# it is deliberately a stable one-line grammar rather than prose, because
# db.py's `parse_parties` has to read it back deterministically. A model pass
# that later appends to `notes` cannot break it: the parser matches per line.
#
# THE HAND-OFF this leaves open is stated in the report — when a first-class
# `parties` field is added to SignalSchema and LEDGER_ALLOWLIST, db.py already
# prefers it (see parse_parties) and this line becomes redundant, not wrong.

PARTIES_PREFIX = "parties: "

# Legal-form and institution markers. A name matching one of these is a LEGAL
# PERSON and may be published; anything else is treated as a possible
# fyzická osoba (sole trader) and its NAME IS SUPPRESSED — the IČO still lands,
# because the IČO is what the entity graph joins on and the name is display
# sugar recoverable from ARES at read time.
#
# MEASURED 2026-08-19 over one full data.smlouvy.gov.cz daily dump (4,169
# counterparty names): 21.3% carry no legal-form marker, and the residue is
# exactly what you fear — "Jana Vítková", "Karel Dreveňák", "Ing. Tomáš Koutný",
# "Josef Janeček". Those are natural persons' names, and our ledgers are public,
# append-only and on GitHub. Hlídač's own `identifikace: "PO"` flag CANNOT be
# used instead: it was null on 19 of 27 recipients in the probe payload, so
# trusting it would suppress most legal persons and, worse, read as authority.
#
# The list errs toward SUPPRESSION on purpose. A missed legal person loses a
# display name (recoverable); a missed natural person publishes someone's name
# forever (not recoverable). That asymmetry is the whole design.
# 1. Legal-form abbreviations. Boundary-anchored, because `as` and `se` are
#    ordinary Czech words and an unanchored match would pass almost anything.
LEGAL_FORM_RE = re.compile(
    r"(?:^|[\s,.(\"])(?:"
    r"s\.?\s?r\.?\s?o|a\.?\s?s|spol|v\.?\s?o\.?\s?s|k\.?\s?s|s\.?\s?p"
    r"|o\.?\s?p\.?\s?s|z\.?\s?s|z\.?\s?ú|v\.?\s?v\.?\s?i|o\.?\s?s"
    r"|gmbh|a\.?\s?g|s\.?\s?e|s\.?\s?a|n\.?\s?v|b\.?\s?v|oy|ab|as"
    r"|sp\.?\s?z\.?\s?o\.?\s?o|kft|srl|sarl|s\.?\s?p\.?\s?a|oü|d\.?\s?o\.?\s?o"
    r"|plc|ltd|llc|l\.?\s?p|inc|corp|limited|holding|group|company|co"
    r")(?:$|[\s,.)\"])", re.I)

# 2. Institution STEMS, matched as substrings. Czech inflects, so `vysoká` does
#    not match "VYSOKÉ UČENÍ TECHNICKÉ" and `příspěvková organizace` has to be
#    caught by its stem. These are matched WITHOUT a trailing boundary for
#    exactly that reason. MEASURED against one daily dump: without this list
#    1,002 of 4,026 contracts lost a party name, and the losses were public
#    bodies — "Městská část Praha 8", "Dopravní podnik hl. m. Prahy",
#    "Krajská správa a údržba silnic ... příspěvková organizace",
#    "Policejní prezidium České republiky".
INSTITUTION_RE = re.compile(
    r"(?:příspěvkov|akciová\s+spole|obecně\s+prospěš|veřejná\s+výzkumn"
    r"|městská\s+část|statutární|magistrát|ministerstv|prezidi|ředitelstv"
    r"|úřad|správa|inspek|komise|agentur|podnik|služby|závod|dráhy|dopravní"
    r"|univerzit|fakult|vysok[áéý]|škol|gymnázi|učiliště|akademi|ústav"
    r"|institut|knihovn|muzeum|divadl|galeri|filharmoni|observatoř"
    r"|nemocnic|poliklinik|zdravotn|lékárn|hospic|ozdravovn|léčebn"
    r"|domov|dětský\s+dom|jesle|mateřsk|základní\s+škol|středisk|centrum"
    r"|družstv|nadac|nadační|spolek|sdružen|svaz|unie|asociac|komora|klub"
    r"|farnost|církev|diecéz|arcibiskup|biskupstv|kongregac|klášter|obec\b"
    r"|město\b|městys|kraj\b|krajsk|obecní|lesy|povodí|vodovod|kanaliz"
    r"|teplárn|elektrárn|energetik|plynárn|technick[áéý]\s+služ"
    r"|banka|bankovní|pojišťovn|fond\b|burza|spořiteln|záložn"
    r"|česk[áéýo]|národní|státní|republik|zoolog|botanick|arboret"
    r"|sportovní|tělovýchovn|tělocvičn|sokol|hasič|charita|diakoni"
    r"|zahraničn|spolupráce|rozvoj|výzkum|laboratoř|hvězdárn"
    r")", re.I)

_PARTY_STRIP_RE = re.compile(r"[;\[\]|\r\n]+")


def party_name_public(name):
    """The name if it is provably a legal person, else None (IČO-only).

    THE ASYMMETRY IS THE DESIGN. A missed legal person loses a display name,
    which `scripts/fetch_ares.sh` can resolve from the IČO at read time. A
    missed NATURAL person publishes someone's name into a public, append-only,
    on-GitHub ledger where there is no quiet cleanup. So this is an ALLOWLIST
    (CONVENTIONS.md: "ALLOWLIST, NEVER DENYLIST"), and the residue it suppresses
    is accepted cost rather than a bug to tune away.

    Not a denylist of person-shapes, which was the tempting alternative: a Czech
    sole trader is `Jana Vítková` or `Ing. Tomáš Koutný` and a two-plain-words
    pattern catches most of them — but it FAILS OPEN on the first name shaped
    unusually, and failing open here is the one outcome that cannot be undone.
    """
    n = collapse(_PARTY_STRIP_RE.sub(" ", str(name or "")))
    if not n:
        return None
    if LEGAL_FORM_RE.search(n) or INSTITUTION_RE.search(n):
        return n
    return None


def party_line(parties):
    """One `notes` line for a contract's parties, or "" when there is nothing.

    Grammar (stable, parsed by db.py parse_parties):
        parties: buyer=NAME [ICO]; supplier=NAME [ICO]; supplier=NAME [ICO]
    A party with a suppressed name renders `role=[ICO]`; a party with no IČO
    renders `role=NAME`. A party with neither is not a party and is skipped.
    """
    out = []
    for role, name, ico in parties:
        pub = party_name_public(name)
        ico = collapse(str(ico or ""))
        ico = ico if re.fullmatch(r"\d{8}", ico) else ""
        if not pub and not ico:
            continue
        if pub and ico:
            out.append(f"{role}={pub} [{ico}]")
        elif ico:
            out.append(f"{role}=[{ico}]")
        else:
            out.append(f"{role}={pub}")
    return (PARTIES_PREFIX + "; ".join(out)) if out else ""


def hlidac_parties(item):
    """(role, name, ico) tuples from a Hlídač / registr-smluv shaped item.

    `platce` is the PAYER and `prijemce[]` the RECIPIENTS — money-flow roles,
    not procurement roles, and they are NOT always buyer/supplier. Measured in
    the probe payload: `KMM net, s.r.o. -> Domov seniorů Vratislavice` pays a
    public body. So the roles are recorded as `payer` / `recipient` and the
    interpretation is left to the reader, rather than asserting a "supplier"
    the payload does not actually claim.
    """
    out = []
    p = item.get("platce")
    if isinstance(p, dict):
        out.append(("payer", p.get("nazev"), p.get("ico")))
    r = item.get("prijemce")
    if isinstance(r, dict):
        r = [r]
    for one in (r or []):
        if isinstance(one, dict):
            out.append(("recipient", one.get("nazev"), one.get("ico")))
    return out


def ted_list(v):
    """TED multi-valued field as a flat list. `{lang: [..]}` maps take the
    Czech/English branch; scalars become one-element lists."""
    if isinstance(v, dict):
        for k in ("ces", "eng", "en", "cs"):
            if k in v:
                return ted_list(v[k])
        vals = list(v.values())
        return ted_list(vals[0]) if vals else []
    if isinstance(v, (list, tuple)):
        return list(v)
    return [] if v in (None, "") else [v]


def ted_parties(item):
    """(role, name, ico) tuples from one TED notice.

    THE FIELD NAMES ARE MEASURED, NOT GUESSED — and the obvious pair is the
    wrong one. Probed 2026-08-21 against 300 CZ `form-type: result` notices:

      organisation-name-tenderer / organisation-identifier-tenderer
          name↔id array lengths ALIGNED on 300 of 300 (100%)
      winner-name / winner-identifier
          name↔id array lengths MISMATCHED on 51 of 300 (17%) — winner-name
          repeats a name once per lot, winner-identifier does not, so zipping
          them pairs company A's name to company B's IČO. SILENTLY.
      organisation-name-buyer / organisation-identifier-buyer
          present on 300 of 300; every id an 8-digit checksum-valid IČO.

    So the tenderer pair carries the pairing and `winner-*` is the fallback for
    a notice that has one but not the other. `winner-identifier` and
    `organisation-identifier-tenderer` held identical arrays on 299 of 300, so
    this loses no coverage — it only refuses to guess the alignment.

    Non-Czech ids arrive here too (`DE124727617`, `BE0826207990` are VAT
    numbers, 7 of 642 winner ids). They are passed through as-is; db.py's IČO
    checksum is what decides whether one becomes an entity key.
    """
    out = []
    bn = ted_list(item.get("organisation-name-buyer")) or \
        ted_list(item.get("buyer-name"))
    bi = ted_list(item.get("organisation-identifier-buyer"))
    if bi and len(bn) == len(bi):
        out += [("buyer", n, i) for n, i in zip(bn, bi)]
    elif bi:
        # Lengths disagree (2 of 300 sampled notices, where a notice lists
        # several buying organisations but one name). Same rule as suppliers:
        # keep the IDENTIFIERS and drop the names rather than pair them by
        # position. An unpaired IČO is a usable entity key; a mispaired name is
        # a lie, and it is the kind of lie nothing downstream can detect.
        out += [("buyer", None, i) for i in bi]
    else:
        out += [("buyer", n, None) for n in bn[:1]]

    sn = ted_list(item.get("organisation-name-tenderer"))
    si = ted_list(item.get("organisation-identifier-tenderer"))
    if not (sn and si and len(sn) == len(si)):
        sn2, si2 = ted_list(item.get("winner-name")), ted_list(item.get("winner-identifier"))
        if len(sn2) == len(si2):
            sn, si = sn2, si2
        else:
            # Lengths disagree: keep the IDENTIFIERS, drop the names. An
            # unpaired IČO is a usable entity key; a mispaired name is a lie.
            sn, si = [], (si or si2)
    if len(sn) == len(si):
        pairs = list(zip(sn, si))
    else:
        pairs = [(None, i) for i in si]
    for n, i in pairs:
        out.append(("supplier", n, i))

    # De-duplicate WITHIN a role, not across roles. TED repeats an organisation
    # once per lot, so one three-lot award to one company arrives three times;
    # and an organisation legitimately appears as BOTH buyer and supplier on the
    # same notice (measured on 1762-2025, where Dopravní podnik hl. m. Prahy is
    # a listed buying organisation AND the winner). Collapsing across roles
    # would delete exactly that fact, which is the interesting one.
    seen, uniq = set(), []
    for role, n, i in out:
        k = (role, collapse(str(n or "")), str(i or ""))
        if k in seen:
            continue
        seen.add(k)
        uniq.append((role, n, i))
    return uniq


def extract_ted(item, payload_key, today):
    pub = flat(get_first(item, "publication-number", "publicationNumber"))
    if not pub:
        return None
    title = collapse(flat(get_first(item, "notice-title", "noticeTitle")))
    buyer = collapse(flat(get_first(item, "buyer-name", "buyerName"))) or ""
    d = flat(get_first(item, "publication-date", "publicationDate")) or ""
    val = flat(get_first(item, "total-value", "estimated-value-glo", "estimated-value-lot"))
    cur = flat(get_first(item, "total-value-cur", "estimated-value-cur-glo",
                         "estimated-value-cur-lot")) or "EUR"
    money, note = None, ""
    if val is not None:
        try:
            v = float(val)
            if str(cur).upper() == "CZK":
                money = money_from_czk(v)
                note = f"{v:,.0f} CZK converted at a fixed {CZK_PER_EUR} CZK/EUR (ingest runs offline)"
            else:
                money = round(v)
                note = f"{v:,.0f} {cur} as published"
        except (TypeError, ValueError):
            pass
    deadline = flat(get_first(item, "deadline-receipt-tender-date-lot", "deadline"))
    return {
        "id": f"ted-{pub}",
        "source": "ted",
        "evidence_type": "tenders",
        "url": f"https://ted.europa.eu/en/notice/-/detail/{pub}",
        "date": iso_date(d) or "",
        "title_native": title,
        "entity_native": buyer,
        # None ON PURPOSE (2026-08-24): sector is a model label now that the
        # feed is an all-CPV firehose — see the CPV_SECTOR obituary above.
        # None puts `sector` into `_needs` via missing_required(), same as
        # every other feed whose extractor carries no sector judgment.
        "sector": None,
        "money_eur": money,
        "money_note": note,
        "urgency_date": iso_date(deadline),
        "quote_parts": [p for p in (title, (f"{val} {cur}" if val is not None else "")) if p],
        "excerpt": collapse(f"{title} — {buyer}"),
        # The counterparty. Empty string on a notice with no award (a
        # `competition`/`planning` form has no winner yet) and apply_allowlist
        # drops an empty optional receipt, so nothing is written that says
        # nothing. 55% of the committed CZ payload is `form-type: result`.
        "notes": party_line(ted_parties(item)),
    }


# The money fields Hlídač actually returns, best first. MEASURED 2026-08-20
# against three authenticated 200s (75 items): `calculatedPriceWithVATinCZK` is
# non-null on 75/75 and is the API's own normalisation to CZK including VAT, so
# it also resolves the foreign-currency contracts `ciziMena` marks;
# `hodnotaVcetneDph` is non-null on 14/25 and `hodnotaBezDph` on 17/25.
#
# `cenaSDph` — the name this extractor used to read first — appears on 0 of 75
# items. It is REAL, but it is a QUERY-LANGUAGE field (the `it-large` query
# filters on `cenaSDph:>10000000` and returns 37 hits), not a response field.
# Copying a search-DSL name into a response reader is how it got here, and the
# same mistake put it in the feed contract's required_fields.
HLIDAC_MONEY_FIELDS = ("calculatedPriceWithVATinCZK", "hodnotaVcetneDph",
                       "hodnotaBezDph")


def hlidac_money(item):
    """(czk, field_name) for the first PUBLISHED figure, or (None, None).

    Zero is treated as absent, not as a free contract: Hlídač returns 0.0 with a
    `cenaNeuvedenaDuvod` reason when no price was disclosed, and passing that
    through would score `money` 1 (<200k) on a contract whose value is unknown,
    which the rubric grades 0.
    """
    for f in HLIDAC_MONEY_FIELDS:
        v = item.get(f)
        try:
            if v is not None and float(v) != 0.0:
                return float(v), f
        except (TypeError, ValueError):
            continue
    return None, None


def extract_hlidac(item, payload_key, today):
    nid = get_first(item, "identifikator", "id", "idVerze")
    if isinstance(nid, dict):
        nid = get_first(nid, "idSmlouvy", "id")
    if not nid:
        return None
    predmet = collapse(get_first(item, "predmet", "popis") or "")
    cena, cena_field = hlidac_money(item)
    money = money_from_czk(cena) if cena is not None else None
    dt = get_first(item, "datumUzavreni", "datum") or ""
    return {
        "id": f"hlidac-{nid}",
        "source": "hlidac",
        "evidence_type": "tenders",
        "url": get_first(item, "odkaz", "url") or f"https://smlouvy.gov.cz/smlouva/{nid}",
        "date": iso_date(dt) or "",
        "title_native": predmet,
        "entity_native": collapse((item.get("platce") or {}).get("nazev", "")
                                  if isinstance(item.get("platce"), dict) else ""),
        "sector": None,
        "money_eur": money,
        "money_note": (f"{cena:,.0f} CZK ({cena_field}) at a fixed {CZK_PER_EUR} CZK/EUR"
                       if money is not None else ""),
        "urgency_date": None,
        "quote_parts": [p for p in (predmet, str(cena) if cena is not None else "") if p],
        "excerpt": predmet,
        # THE COUNTERPARTY, which this extractor used to discard. `platce` was
        # read for its `nazev` alone and `prijemce[]` — the party that WINS the
        # contract, with its IČO — was never touched. Measured on an
        # authenticated probe payload (25 contracts): 25 of 25 carry a
        # checksum-valid IČO on BOTH sides.
        "notes": party_line(hlidac_parties(item)),
    }


def extract_smlouvy(item, payload_key, today):
    """The official registr smluv dump. Reuses extract_hlidac's field reading —
    fetch_smlouvy.sh emits the Hlídač item shape on purpose — and overrides only
    the two things that are genuinely different: the id namespace and the
    provenance.

    WHY NOT JUST REUSE `hlidac-` IDS. It is tempting, and it would be free
    deduplication: both feeds read the SAME register and both ids would embed
    the same registr-smluv `idVerze`, so one contract fetched twice would
    collapse in `seen.txt` by itself. It is still wrong twice over.
      · `source` is defined by CONVENTIONS.md as FETCH PROVENANCE. A record
        pulled from data.smlouvy.gov.cz that says `hlidac` is a false receipt,
        and receipts are the point.
      · db.py's `attribute_prefixes` resolves a prefix claimed by TWO capable
        registry rows to UNATTRIBUTED — deliberately, so nothing is credited to
        whichever row sorts first. Sharing the `hlidac-` prefix would therefore
        make BOTH feeds' records unattributable on /sources.

    THE COST IS REAL AND IS NOT PAPERED OVER: a contract that both feeds see
    lands twice, under two ids, and the ledgers are append-only. The two ids
    embed the same `idVerze` and both records carry the same
    `smlouvy.gov.cz/smlouva/<idVerze>` url, so the overlap is one query away —
    but nothing here prevents it. Running both fetchers against overlapping
    windows is an operational choice for the registry owner, not a decision this
    extractor can make.
    """
    rec = extract_hlidac(item, payload_key, today)
    if not rec:
        return None
    nid = rec["id"].split("-", 1)[1]
    rec["id"] = f"smlouvy-{nid}"
    rec["source"] = "smlouvy"
    return rec


def extract_yc(item, payload_key, today):
    slug = get_first(item, "slug", "id", "name")
    if not slug:
        return None
    one = collapse(get_first(item, "one_liner", "oneLiner", "description") or "")
    name = collapse(item.get("name") or str(slug))
    return {
        "id": f"yc-{slugify(slug)}",
        "source": "yc",
        "evidence_type": "funded",
        "url": get_first(item, "url", "website") or f"https://www.ycombinator.com/companies/{slugify(slug)}",
        # launched_at is UNIX EPOCH SECONDS in the yc-oss payload (1322045523),
        # not a date string — see iso_date().
        "date": iso_date(get_first(item, "launched_at", "batch_date")) or today.isoformat(),
        # yc-oss is the ONE feed whose title and summary need no model: the
        # one_liner is already English prose written by the company.
        "title": f"{name} — {one}" if one else name,
        "summary": one or name,
        "title_native": name,
        "entity_native": name,
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": None,
        "quote_parts": [one] if one else [name],
        "excerpt": one or name,
    }


def extract_suggest(item, payload_key, today):
    q = collapse(item.get("query") or "")
    comps = item.get("completions") or []
    if not q or not comps:
        return None
    first = collapse(comps[0])
    return {
        "id": f"suggest-{sha1_8(q)}",
        "source": "suggest",
        "evidence_type": "demand",
        "url": ("https://www.google.com/search?q=" +
                re.sub(r"\s+", "+", q)),
        "date": iso_date(item.get("date")) or today.isoformat(),
        "title_native": q,
        "entity_native": "",
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": None,
        # The completion string IS the quote — one line, verbatim, no framing.
        "quote_parts": [first],
        "excerpt": " | ".join(collapse(c) for c in comps[:8]),
    }


def extract_reddit(item, payload_key, today):
    pid = get_first(item, "id", "guid") or get_first(item, "link") or ""
    pid = str(pid).rstrip("/").split("/")[-1] or sha1_8(str(item))
    title = collapse(get_first(item, "title") or "")
    if not title:
        return None
    body = collapse(get_first(item, "content", "summary", "description") or "")
    body = re.sub(r"<[^>]+>", " ", body)
    body = collapse(body)[:200]
    dt = iso_date(get_first(item, "updated", "published", "pubDate")) or today.isoformat()
    return {
        "id": f"reddit-{slugify(pid)}",
        "source": "reddit",
        "evidence_type": "demand",
        "url": get_first(item, "link") or "",
        "date": dt,
        "title_native": title,
        "entity_native": "",
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": None,
        "quote_parts": [p for p in (title, body) if p],
        "excerpt": collapse(f"{title} {body}"),
    }


def extract_feed(item, payload_key, today):
    title = collapse(get_first(item, "title") or "")
    link = get_first(item, "link", "guid") or ""
    if not title or not link:
        return None
    desc = collapse(re.sub(r"<[^>]+>", " ", get_first(item, "description", "summary") or ""))
    first_sentence = re.split(r"(?<=[.!?])\s", desc)[0] if desc else ""
    # RSS `pubDate` is RFC-2822 ('Thu, 20 Aug 2026 08:00:30 +0000') — see iso_date().
    dt = iso_date(get_first(item, "pubDate", "published", "updated")) or today.isoformat()
    return {
        "id": f"feed-{sha1_8(link)}",
        "source": "feed",
        "evidence_type": "funded",
        "url": link,
        "date": dt,
        "title_native": title,
        "entity_native": "",
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": None,
        "quote_parts": [first_sentence or title],
        "excerpt": collapse(f"{title} {desc}")[:400],
    }


def extract_ec_hys(item, payload_key, today):
    """EC Have Your Say — one Commission initiative open for feedback.

    `feedback_end` becomes `urgency_date`: a consultation deadline is a real
    date the world imposes on us, which is exactly what score_urgency() is for.
    """
    iid = str(item.get("initiative_id") or "").strip()
    title = collapse(item.get("title") or "")
    link = (item.get("link") or "").strip()
    if not iid or not title or not link:
        return None
    summary = collapse(item.get("summary") or "")
    cs = collapse(item.get("title_cs") or "")
    end = (item.get("feedback_end") or "")[:10].replace("/", "-")
    return {
        "id": f"echys-{slugify(iid)}",
        # `reg-scan`, NOT a new `ec-hys` source. CONVENTIONS defines `source` as
        # fetch provenance at the granularity the corpus already uses, and the
        # 34 committed `consult-*` records are the SAME Commission initiatives
        # harvested by hand under `reg-scan`. Minting a fourth name for one
        # source would split the provenance and force a SignalSchema edit for
        # no gain.
        "source": "reg-scan",
        "evidence_type": "regulation",
        "url": link,
        "date": (item.get("feedback_start") or "")[:10].replace("/", "-") or today.isoformat(),
        "title_native": cs or title,
        "entity_native": "European Commission",
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": end or None,
        "quote_parts": [p for p in (title, summary[:280]) if p],
        "excerpt": collapse(f"{title} {summary}")[:400],
    }


def extract_veklep(item, payload_key, today):
    """VeKLEP — one legislative draft in the government's e-library, via the
    Hlídač mirror of the ODok portal (api.hlidacstatu.cz/api/v2/datasety/veklep).

    WHY THIS FEED EXISTS: every Czech legislative draft carries a mandatory RIA
    whose first section is "Definice problému" — a state-authored problem
    statement. The script is MECHANICAL ONLY: it stages the draft's metadata
    and its portal link. The RIA PDFs hang off the item's `prilohy` and are
    read later by the model half / the reg-scan pass, never fetched-and-judged
    here — a script that downloaded and summarized a RIA would be judgment in
    the mechanical half.

    PERSONAL DATA, STATED: the payload's `adresaPripominek` is a named civil
    servant's work email (measured 2026-08-25 on the live dataset). It is
    simply never read — only the named-safe fields below enter the record —
    and the AC-GDPR1 content scan would refuse any record it leaked into.

    Field presence measured 2026-08-25 on a live 25-item page: PID,
    nazevMaterialu, url, typMaterialu, datumAutorizace, datumPosledniUpravy,
    stavMaterialuText on 25/25; predkladatel only 15/25, so it degrades to ""
    rather than gating the record.
    """
    pid = collapse(item.get("PID") or item.get("Id") or "")
    title = collapse(item.get("nazevMaterialu") or "")
    url = (item.get("url") or "").strip()
    if not pid or not title or not url:
        return None
    predkladatel = collapse(item.get("predkladatel") or "")
    typ = collapse(item.get("typMaterialu") or "")
    stav = collapse(item.get("stavMaterialuText") or "")
    duvod = collapse(item.get("duvodPredlozeni") or "")
    # A comment deadline is a real date the world imposes — score_urgency's
    # job. Routinely in the past by fetch time, which score_urgency hands to
    # the model as urgency_pending rather than asserting enforcement.
    deadline = iso_date(item.get("terminPripominekDoData"))
    return {
        "id": f"veklep-{pid}",
        "source": "veklep",
        "evidence_type": "regulation",
        "url": url,
        "date": iso_date(get_first(item, "datumAutorizace", "datumPosledniUpravy")) or "",
        "title_native": title,
        "entity_native": predkladatel,
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": deadline,
        "quote_parts": [p for p in (title, duvod[:280]) if p],
        "excerpt": collapse(f"{title} — {predkladatel} [{typ}; {stav}]")[:400],
    }


def extract_nku(item, payload_key, today):
    """NKÚ Věstník / press release — one documented state-audit item."""
    nid = str(item.get("nku_id") or "").strip()
    title = collapse(item.get("title") or "")
    link = (item.get("link") or "").strip()
    if not nid or not title or not link:
        return None
    return {
        "id": f"nku-{slugify(nid)}",
        "source": "demand-scan",
        "evidence_type": "demand",
        "url": link,
        "date": (item.get("date") or "") or today.isoformat(),
        "title_native": title,
        "entity_native": "Nejvyšší kontrolní úřad",
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": None,
        "quote_parts": [title],
        "excerpt": collapse(
            f"{title} [{item.get('doc_type','')}"
            f"{' ' + item['audit_no'] if item.get('audit_no') else ''}]")[:400],
    }


def extract_vestbee(item, payload_key, today):
    """Vestbee — one CEE funding round (or a flagged roundup awaiting a split).

    The id is minted by the FETCHER (`signal_id`), because the collision rule
    needs to see the whole per-round family at once — see fetch_vestbee.sh.
    Money is carried only when the published figure is already in EUR; a USD or
    GBP figure keeps its note and leaves money_eur null rather than inventing
    an FX rate for a date nobody recorded.
    """
    sid = (item.get("signal_id") or "").strip()
    link = (item.get("link") or "").strip()
    title = collapse(item.get("title") or item.get("slug") or "")
    if not sid or not link or not title:
        return None
    cur = (item.get("amount_currency") or "").upper()
    val = item.get("amount_value")
    summary = collapse(item.get("summary") or "")
    return {
        "id": slugify(sid),
        "source": "round",
        "evidence_type": "funded",
        "url": link,
        "date": (item.get("date") or "")[:10] or today.isoformat(),
        "title_native": title,
        "entity_native": "",
        "sector": None,
        "money_eur": int(val) if (val and cur == "EUR") else None,
        "money_note": (item.get("amount_note") or ""),
        "urgency_date": None,
        "quote_parts": [p for p in (title, summary[:280]) if p],
        "excerpt": collapse(f"{title} {summary}")[:400],
    }


EXTRACTORS = {
    # `smlouvy` delegates to extract_hlidac for every field because
    # fetch_smlouvy.sh emits the Hlídač ITEM SHAPE from the official XML dump
    # (identifikator / odkaz / predmet / datumUzavreni / hodnotaVcetneDph /
    # platce / prijemce[]). The XML->item mapping lives in the fetcher, where
    # the XML is; only id and provenance differ, and extract_smlouvy overrides
    # exactly those two rather than forking a near-identical extractor that
    # would drift.
    "ted": extract_ted, "hlidac": extract_hlidac,
    "smlouvy": extract_smlouvy,
    "yc-oss": extract_yc, "suggest": extract_suggest,
    "reddit-new": extract_reddit, "reddit-search": extract_reddit,
    "cc-cz": extract_feed,
    # `nen` NO LONGER DELEGATES TO extract_hlidac. It used to, and that was a
    # live attribution defect rather than a shortcut: extract_hlidac stamps
    # `hlidac-<id>` and `source: "hlidac"`, so every NEN record the feed
    # produced would have been filed under the WRONG feed's prefix — invisible,
    # because a hlidac- id is a perfectly valid id and AC-F3 would pass. The
    # `nen` row is PARKED (see its blocker), so this mapping is not live today;
    # it is corrected now so that un-parking cannot re-open the defect.
    "nen": nen_extract.extract_nen,
    # `vestbee` NO LONGER DELEGATES TO extract_feed either. The dead RSS is
    # gone; scripts/fetch_vestbee.sh reads the sitemap and emits a per-round
    # jsonl item (signal_id / link / lastmod), which extract_feed cannot read —
    # it looks for `title` + `link|guid` and would have returned None for every
    # item, i.e. ok=1 items_kept=0, the exact silent state below.
    "vestbee": extract_vestbee,
    "ec-hys": extract_ec_hys, "nku": extract_nku,
    "veklep": extract_veklep,
    "coi": coi_extract.extract_coi, "sukl": sukl_extract.extract_sukl,
    "mpsv": extract_mpsv,
    # `asks` — direct asks from problem owners. Both stamp evidence_type "asks"
    # and put the owner in entity_native; neither carries money, and urgency
    # comes from the consultation / event date exactly as ec-hys reads its
    # feedback deadline.
    "tacr": tacr_extract.extract_tacr, "hackathon": hack_extract.extract_hack,
}

# Feeds that legitimately keep ZERO records from a healthy payload. `ares`,
# `shoptet` and `upgates` are `role: enrichment` in data/feeds.json: they resolve
# lookups, they declare `id_prefixes: []`, and nothing they fetch is ever meant
# to reach data/signals/**. This set is DERIVED FROM THE REGISTRY at run time
# (see extractor_missing() below), never hand-maintained here — a hardcoded list
# would drift from feeds.json the first time a role changed, and the drift would
# fail silent in exactly the direction this whole guard exists to prevent.

# --------------------------------------------------------------------------
# WHAT A RECORD OWES BEFORE IT MAY REACH A LEDGER — ONE DEFINITION, TWO USERS.
# --------------------------------------------------------------------------
#
# REQUIRED_OUT is the gate --complete refuses on. `_needs` is the list an agent
# reads to know what to fill. THEY WERE TWO HAND-MAINTAINED LISTS AND THEY
# DRIFTED: REQUIRED_OUT demanded `geo_origin`, the old model_debt() never named
# it, and NO extractor sets it — so an agent that filled exactly what `_needs`
# listed was still REFUSED, on every feed, with no hint in the staging output
# that the field was ever wanted.
#
# MEASURED on the committed 2026-08-20 payloads before the fix: 4,397 staged
# records, `geo_origin` present on 0 of them and named in `_needs` on 0 of them;
# a three-record --complete over records filled exactly to `_needs` exited 1
# printing "geo_origin" three times. That is the whole reason the six working
# fetchers have never landed a record.
#
# The fix is structural rather than a second list entry: model_debt() is now
# DERIVED from REQUIRED_OUT through the same predicate --complete uses, so the
# question "what does this record still owe?" has exactly one answer in this
# file and the pair cannot drift apart again.
#
# `geo_origin` is deliberately left to the model rather than guessed here. It
# records where the signal comes FROM, and a Czech-language feed carrying a
# story about a German company makes that a judgement, not arithmetic — and the
# mechanical pass carries no judgement by law.
REQUIRED_OUT = ("id", "source", "url", "date", "title", "sector", "geo_origin",
                "money_eur", "money_note", "summary", "scores")

# `scores` has its own per-key integer check; `money_eur`/`money_note` are pure
# arithmetic and are legitimately null/empty when no figure was published.
_NOT_MODEL_DEBT = ("scores", "money_eur", "money_note")


def missing_required(rec):
    """REQUIRED_OUT fields this record does not carry yet. The single predicate
    behind both `_needs` (what to ask a model for) and --complete's refusal
    (what to reject on)."""
    return [f for f in REQUIRED_OUT
            if f not in _NOT_MODEL_DEBT and rec.get(f) in (None, "")]


def model_debt(feed_key, rec):
    """What a model still owes for one mechanically-extracted record.

    Every feed owes scale and recurrence — which is why NOTHING can be appended
    by the mechanical pass alone. Everything else is derived: yc-oss ships an
    English one_liner, so its records already carry `title` and `summary` and
    neither appears here, with no feed name hard-coded to say so.
    """
    debt = ["scores.scale", "scores.recurrence"]
    debt += missing_required(rec)
    if rec.get("urgency_pending"):
        debt.append("scores.urgency")
    if feed_key in ("suggest", "reddit-new", "reddit-search"):
        debt.append("pain")  # transport-only admission bar; NEVER persisted
    return debt


# --------------------------------------------------------------------------
# contract evaluation
# --------------------------------------------------------------------------

def produces_signals(feed):
    """True when this registry row is supposed to write records to a ledger.

    Both halves are load-bearing and are checked together on purpose.
    `role: enrichment` is db.py's own `_capable` test (db.py:1913) and is what
    exempts `ares` / `shoptet` / `upgates`; `signal_source` is the field
    CONVENTIONS makes null for exactly those rows. Requiring both means a row
    that is half-converted — role flipped but signal_source left set, or the
    reverse — still counts as a signal feed and still trips the guard, rather
    than silently buying an exemption from a one-word edit.
    """
    return feed.get("role") != "enrichment" and feed.get("signal_source") is not None


def evaluate_contract(feed, items, parse_ok, parse_err, nbytes, receipt):
    """
    Order matters and is the whole point: a 200 carrying a login page must be
    LOUDER than a 500, because the 500 is honest and self-healing.

    Transport facts come from the FETCHER'S OWN RECEIPT, never from inference.

    Returns (ok, error, yield_anomaly, parse_method).
    """
    c = feed.get("contract") or {}
    http_status = (receipt or {}).get("http_status")
    result = (receipt or {}).get("result")
    rerr = (receipt or {}).get("error")

    # Step 0a — the fetcher already ruled this an EXPECTED ABSENCE (a
    # calendar-keyed day that does not exist, or a feed it declined to run).
    # It logs, it does not fail, and it must not move the feed toward BROKEN.
    if result == "skipped":
        return True, rerr, None, "none"
    # Step 0b — a calendar-keyed 404 on a feed that allows it.
    if c.get("allow_missing") and http_status == 404:
        return True, None, None, "none"
    # Step 0c — NO RECEIPT AT ALL. Say unknown; never synthesize a status.
    if receipt is None:
        if nbytes == 0:
            return False, "no fetch receipt and no payload — the feed did not run", "zero", "none"
        # A payload with no receipt is usable but UNATTRIBUTED: we parse it and
        # the http_status stays None, because "there are bytes" is not evidence
        # of a 200.
        if not parse_ok:
            return False, f"parse: {parse_err} (no fetch receipt; transport UNKNOWN)", None, "none"
    # 1 transport
    if result == "error":
        return False, f"transport: {rerr or 'fetcher reported an error'}", None, "none"
    if http_status is not None and http_status != 200:
        return False, f"transport: HTTP {http_status}{(' — ' + rerr) if rerr else ''}", None, "none"
    if nbytes == 0:
        return False, f"transport: zero bytes{(' — ' + rerr) if rerr else ''}", "zero", "none"
    # 2 parse
    if not parse_ok:
        return False, f"parse: {parse_err}", None, "none"
    # 3 fields — the check that catches a login page stored as .json
    req = c.get("required_fields") or []
    if req and items:
        missing = [f for f in req if not any(f in (it or {}) for it in items)]
        if missing:
            return False, f"fields: {', '.join(missing)} missing from every item", None, "structured"
    # 4 yield
    ey = c.get("expected_yield") or {}
    n = len(items)
    anomaly = None
    if n == 0:
        return False, "yield: zero items", "zero", "structured"
    if ey.get("min") is not None and n < ey["min"]:
        anomaly = "below-range"
    elif ey.get("max") is not None and n > ey["max"]:
        anomaly = "above-range"
    return True, None, anomaly, "structured"


# --------------------------------------------------------------------------
# the mechanical pass
# --------------------------------------------------------------------------

def load_registry():
    with open(FEEDS_JSON, "r", encoding="utf-8") as fh:
        return {f["key"]: f for f in json.load(fh)["feeds"]}


def load_receipts(raw_dir):
    """
    THE TRUE TRANSPORT RECEIPTS, written by the fetchers to
    <raw>/.fetch/receipts.jsonl using db.py's exact fetch_log field names.

    THIS REPLACED A FABRICATED RECEIPT. The previous code inferred
    `http_status = 200 if nbytes > 0 else None`, which cannot tell a 404 from a
    403 from a fetch that never ran — and because a failed fetch now leaves no
    file at all, it recorded `None` for every real failure while stamping a
    confident 200 on anything that happened to land bytes. An inferred 200 is
    WORSE than a missing status, because it reads as evidence. Fabricating a
    receipt is the exact failure this program exists to prevent.

    Returns {feed_key: receipt}, keeping the LATEST receipt per feed by
    started_at. A feed with no receipt gets None, and the caller records that
    honestly as unknown rather than guessing.
    """
    path = os.path.join(raw_dir, ".fetch", "receipts.jsonl")
    out = {}
    if not os.path.isfile(path):
        return out
    try:
        for line in open(path, "r", encoding="utf-8"):
            if not line.strip():
                continue
            r = json.loads(line)
            k = r.get("feed_key")
            if not k:
                continue
            prev = out.get(k)
            if prev is None or str(r.get("started_at") or "") >= str(prev.get("started_at") or ""):
                out[k] = r
    except (OSError, json.JSONDecodeError) as e:
        log(f"normalize: could not read {path} ({e}) — transport status will be UNKNOWN, "
            f"never synthesized")
    return out


def load_seen(path):
    if not os.path.isfile(path):
        return set()
    with open(path, "r", encoding="utf-8") as fh:
        return {l.strip() for l in fh if l.strip()}


# ==========================================================================
# THE SECOND DEDUP AXIS — same resource, different id
# ==========================================================================
#
# `seen.txt` is ID-KEYED and that is the only dedup this program had. It cannot
# see the case it was most likely to meet: the SAME resource harvested twice
# under two different id conventions. MEASURED 2026-08-21 against the committed
# corpus and one staged run of the four newly-wired feeds:
#
#   · 20 `echys-<initiative-id>` records point at the identical
#     ec.europa.eu/.../initiatives/<n> URL as an existing `consult-<slug>`
#     record from the attended harvest. Same page, two ids.
#   · 30 `nku-k<code>` records are the SAME NKÚ audit conclusion as an existing
#     `nku-<topic-slug>` record — and THEIR URLS DO NOT MATCH AT ALL. The hand
#     harvest linked the PDF (`/assets/kon-zavery/k25011.pdf`); the fetcher
#     links the Věstník landing page. A url-keyed pass alone catches 0 of 30.
#
# So the axis is not "url". It is ANY key that identifies the resource, and
# `url` is only the most common one.
#
# ── WHY THIS IS NOT JUST `if url in ledger: skip` ─────────────────────────────
# BECAUSE URL EQUALITY IS NOT IDENTITY, AND THE COUNTEREXAMPLE IS ALREADY IN
# THE LEDGER. MEASURED over data/signals/**: 67 URLs are carried by MORE THAN
# ONE record, covering 571 records — 6.1% of the corpus. One Vestbee roundup
# article is the cited URL for 32 DISTINCT funding rounds; one EIC press release
# is the URL for 25. A naive url-keyed merge would collapse those 571 records
# into 67 and destroy 504 legitimately distinct ones.
#
# It is not a legacy quirk either — three of the feeds landing in this same
# change are built that way BY DESIGN. `coi`, `sukl` and `mpsv` emit AGGREGATES
# (act x half-year, ATC group x month, theme x month) and every aggregate in a
# family carries the same constant dataset URL: coi_extract.py:394 and
# sukl_extract.py:275 are literal string constants. Url-keyed dedup without the
# gate below would keep 1 of 32 ČOI aggregates and 1 of 15 SÚKL aggregates,
# every run, for ever, and the manifest would read green.
#
# ── THE GATE: A KEY EARNS IDENTITY BY BEING UNIQUE, AND IS MEASURED, NOT TRUSTED
# A key value is IDENTIFYING only where it maps to exactly one record. If it
# maps to two or more — on either side, ledger or batch — it is by construction
# a listing page, a dataset landing page or a roundup, and it is EXEMPT. The
# same applies within one record: a page yielding two conclusion codes is an
# index of two audits, not either of them, so it contributes no key.
#
# ── WHY EXEMPT RATHER THAN MERGE, WHEN IT IS GENUINELY UNDECIDABLE ────────────
# Two batch records sharing a key and the ledger holding none is the one case
# the data cannot settle. It resolves to EXEMPT because the errors are not
# symmetric IN PRACTICE: a wrong skip leaves a record out of a run that can be
# re-ingested, while a wrong merge deletes a distinct record from a corpus that
# never fetches that window again. And the exemption is LOGGED, so it is a
# decision a human can overturn rather than a silence nobody can see.
#
# ── NOTHING IS EVER DROPPED QUIETLY ──────────────────────────────────────────
# Every skip prints BOTH ids and the URL, and every exemption prints its reason.
# A silent drop and a silent duplicate are equally invisible, and this file's
# whole subject is the difference between "produced nothing" and "said nothing".

_KCODE_RE = re.compile(r"\bk(\d{5})\b", re.I)

# Feeds whose records are AGGREGATES OVER A PERIOD, for which the url is the
# dataset and never the record. The `url` key is not computed for these at all.
#
# THE MULTIPLICITY GATE ALONE IS NOT ENOUGH HERE, and the gap is narrow enough
# to be worth stating. It exempts a key once TWO records carry it — so a month
# in which one of these feeds emits exactly ONE aggregate produces a unique url,
# which then looks like an identity and merges against next period's aggregate.
# MEASURED on the proof run: `coi` emitted exactly 1 item and `sukl` exactly 1.
# `mpsv` is worse than a narrow window: its employer aggregates carry
# `ares.gov.cz/ekonomicke-subjekty?ico=<ico>` (mpsv_reduce.py:589), which
# identifies a COMPANY, so the same employer hiring again in September would be
# merged into its July record and silently lost.
#
# DECLARED RATHER THAN DERIVED, because it is not derivable: the grain lives in
# the extractor's choice of id, and the url is a constant string three files
# away (coi_extract.py:394, sukl_extract.py:275, mpsv_reduce.py:547). A feed
# joins this list when its id encodes a period — which is the same rule
# CONVENTIONS.md already states for `hiring`.
#
# KEYED ON THE ID PREFIX, not the feed key or `source`, so ONE test works on
# both shapes this function sees. A staged record carries `_feed_key`; a ledger
# record does not, and the 4 committed `sukl-` and 3 committed `coi-` rows say
# `source: demand-scan` because a human harvested them. The prefix is the one
# field CONVENTIONS.md binds to the feed on every record, whoever wrote it.
AGGREGATE_PREFIXES = frozenset({"coi", "sukl", "mpsv"})


def _norm_url(u):
    """A URL reduced to the resource it names, for EQUALITY ONLY.

    Scheme and a leading `www.` are dropped and a trailing slash is stripped,
    because the attended harvests and the fetchers disagree on all three for the
    same page (`www.nku.cz` vs `nku.cz` is in the committed corpus today). The
    QUERY IS KEPT: `?q=katalog/...` and `?partnerId=104` are the resource on
    two of these hosts, and folding it would merge a whole marketplace into one
    row. The fragment is dropped — it addresses a position within a resource,
    never a different one.
    """
    s = str(u or "").strip()
    if not s:
        return ""
    s = s.split("#", 1)[0]
    s = re.sub(r"^[a-z][a-z0-9+.-]*://", "", s, flags=re.I)
    host, _, rest = s.partition("/")
    host = host.lower()
    if host.startswith("www."):
        host = host[4:]
    path, q, query = rest.partition("?")
    path = re.sub(r"/+$", "", path)
    return host + "/" + path + (("?" + query) if q else "")


def record_keys(rec):
    """Identity keys for one record, as `kind:value` strings.

    Reads BOTH field vocabularies on purpose — staged records carry
    `title_native`, ledger records carry `title` — so the same function indexes
    the ledger and screens a batch, and the two can never drift apart.
    """
    keys = set()
    prefix = str(rec.get("id") or "").split("-", 1)[0]

    # An aggregate's url is its dataset, not itself. No url key at all — see
    # AGGREGATE_PREFIXES. This is a REFUSAL TO FORM A KEY, deliberately, rather
    # than forming one and exempting it later: an exemption is decided by how
    # many records happen to share the value THIS run, and the whole point here
    # is that one aggregate in a quiet period would look unique.
    u = "" if prefix in AGGREGATE_PREFIXES else _norm_url(rec.get("url"))
    if u:
        keys.add("url:" + u)

    # `nku-kzaver` — the NKÚ conclusion code, the identity the two nku harvests
    # actually share. Read from the URL and the TITLE only, never the excerpt or
    # summary: a press release that mentions a neighbouring audit in its body
    # would otherwise claim that audit's identity. EXACTLY ONE code required —
    # a Věstník issue page listing several conclusions is an index of them, not
    # any one of them, and contributes no key at all. Measured over the corpus:
    # 0 of 52 staged nku records carry two codes, and 0 of the 30 ledger codes
    # is claimed twice, so this rule is unambiguous on today's data — which is
    # why the ambiguity gate re-checks it every run instead of assuming it.
    if prefix == "nku":
        text = f"{rec.get('url') or ''} {rec.get('title_native') or rec.get('title') or ''}"
        codes = {m.lower() for m in _KCODE_RE.findall(text)}
        if len(codes) == 1:
            keys.add("nku-kzaver:" + codes.pop())
    return keys


def build_key_index(signals_dir):
    """`kind:value` -> [ledger ids carrying it], over the committed ledgers.

    DERIVED FROM THE LEDGER ON EVERY RUN, never persisted. A `seen_urls.txt`
    beside `seen.txt` would be a second source of truth that can drift from the
    corpus it claims to describe, and a dedup index that is quietly wrong is
    worse than none: it drops real records and says nothing. The ledger is the
    canonical corpus (SPEC §3), so it is what gets read — 9,324 lines, ~0.4 s.
    """
    idx = {}
    if not os.path.isdir(signals_dir):
        return idx
    for typ in sorted(os.listdir(signals_dir)):
        d = os.path.join(signals_dir, typ)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".jsonl"):
                continue
            try:
                with open(os.path.join(d, fn), "r", encoding="utf-8") as fh:
                    for line in fh:
                        if not line.strip():
                            continue
                        r = json.loads(line)
                        for k in record_keys(r):
                            idx.setdefault(k, []).append(r.get("id"))
            except (OSError, json.JSONDecodeError) as e:
                log(f"normalize: dedup index could not read {typ}/{fn} ({e}) — "
                    f"NOT skipping the pass on a partial index would silently "
                    f"under-dedup, so this is reported and the run continues with "
                    f"what was readable.")
    return idx


def screen_duplicates(records, ledger_idx, id_of=lambda r: r.get("id"),
                      feed_of=lambda r: r.get("_feed_key") or ""):
    """Split `records` into (kept, skipped, exempt) on the identity keys above.

    Returns
      kept    — records whose keys are new, in input order
      skipped — [(new_id, existing_id, key, feed)] — every one of these is
                printed by the caller with BOTH ids and the URL
      exempt  — [(key, reason, n)] — keys that were NOT used for dedup, and why
    """
    batch_counts = {}
    for r in records:
        for k in record_keys(r):
            batch_counts[k] = batch_counts.get(k, 0) + 1

    exempt, seen_exempt = [], set()
    def _exempt(k, reason, n):
        if k not in seen_exempt:
            seen_exempt.add(k)
            exempt.append((k, reason, n))

    kept, skipped, taken = [], [], {}
    for r in records:
        hit = None
        for k in sorted(record_keys(r)):
            led = ledger_idx.get(k) or []
            if len(led) > 1:
                _exempt(k, "carried by %d ledger records — a listing or dataset "
                           "page, not an identity" % len(led), len(led))
                continue
            if batch_counts.get(k, 0) > 1:
                _exempt(k, "carried by %d records in THIS batch — undecidable, so "
                           "no merge" % batch_counts[k], batch_counts[k])
                continue
            if led:
                hit = (led[0], k)
                break
            if k in taken:
                hit = (taken[k], k)
                break
        if hit:
            skipped.append((id_of(r), hit[0], hit[1], feed_of(r)))
            continue
        for k in record_keys(r):
            taken.setdefault(k, id_of(r))
        kept.append(r)
    return kept, skipped, exempt


def report_duplicates(records_by_id, skipped, exempt, where):
    """Print every skip with BOTH ids and the URL, and every exemption."""
    if exempt:
        print(f"  dedup exemptions ({where}): {len(exempt)} key(s) NOT used — a key "
              f"that names more than one record is a listing, not an identity")
        for k, reason, _n in exempt[:8]:
            print(f"    · {k[:96]}\n        {reason}")
        if len(exempt) > 8:
            print(f"    ... and {len(exempt) - 8} more")
    if not skipped:
        print(f"  dedup by identity key ({where}): 0 skipped")
        return
    print(f"  dedup by identity key ({where}): {len(skipped)} record(s) already in "
          f"the ledger under a DIFFERENT id — skipped, never appended:")
    for new_id, old_id, key, feed in skipped:
        url = (records_by_id.get(new_id) or {}).get("url") or ""
        print(f"    · {feed or '-'}: {new_id}  ==  {old_id}   [{key.split(':', 1)[0]}]")
        print(f"        {url}")


def run_mechanical(args):
    raw_dir = os.path.abspath(args.raw)
    if not os.path.isdir(raw_dir):
        log(f"normalize: no such raw dir: {args.raw}")
        return 1
    registry = load_registry()
    receipts = load_receipts(raw_dir)
    no_receipt = []
    seen = load_seen(args.seen)
    today = date.fromisoformat(args.today) if args.today else date.today()
    run_id = datetime.now().strftime("%Y-%m-%dT%H%M")

    files = sorted(f for f in os.listdir(raw_dir)
                   if os.path.isfile(os.path.join(raw_dir, f))
                   and f not in ("manifest.md", "contract.json", "staged.jsonl", "ingest.json"))
    by_feed, unmapped = {}, []
    for f in files:
        k = feed_for_file(f)
        if k is None:
            unmapped.append(f)
        else:
            by_feed.setdefault(k, []).append(f)

    staged, results = [], []
    dupes = 0
    quote_failures = []
    gdpr_refused = []

    for feed_key, fnames in sorted(by_feed.items()):
        feed = registry.get(feed_key)
        if not feed:
            unmapped.extend(fnames)
            continue
        started = datetime.now(timezone.utc)
        items_all, nbytes, parse_ok, parse_err = [], 0, True, None
        # ONE PAYLOAD KEY PER ITEM, recorded as the items are read. It used to
        # be recomputed inside the extraction loop from `fnames` with a `break`
        # on the first match, which means every item of a multi-file feed took
        # the FIRST file's key. MEASURED 2026-08-20 on five synthetic CPV
        # payloads (ted-it / ted-health / ted-energy / ted-bizserv /
        # ted-construction, 10 notices each): all 50 records came out
        # `sector: b2b` — ted-bizserv sorts first. The damage was silent twice
        # over: the then-live CPV_SECTOR table was the only thing that gave a
        # TED record its sector, and a wrongly-filled sector is non-empty, so
        # it never appeared in `_needs` and no model was ever asked to correct
        # it. (2026-08-24: that table is dead and ted sector is a model field,
        # but the lockstep zip stays — the bug class it closed is about ANY
        # per-file fact, not that one mapping.)
        pkeys_all = []
        for fn in fnames:
            p = os.path.join(raw_dir, fn)
            nbytes += os.path.getsize(p)
            its, ok, err = parse_payload(p, (feed.get("contract") or {}).get("parse", "json"))
            if not ok:
                parse_ok, parse_err = False, f"{fn}: {err}"
            items_all.extend(its)
            pkeys_all.extend([payload_key_of(fn)] * len(its))

        # THE TRANSPORT RECEIPT IS READ, NEVER INFERRED. A feed with no receipt
        # carries http_status None — unknown — and the manifest says so.
        receipt = receipts.get(feed_key)
        http_status = (receipt or {}).get("http_status")
        fetched_at = str((receipt or {}).get("started_at") or "")
        fetched_at = fetched_at if ISO_TS_RE.match(fetched_at) else None
        if receipt is None:
            no_receipt.append(feed_key)
        ok, error, anomaly, parse_method = evaluate_contract(
            feed, items_all, parse_ok, parse_err, nbytes, receipt)

        # ══════════════════════════════════════════════════════════════════
        #  THE SCRIPTED-SILENT TRAP, CLOSED. THIS REPO'S NAMED FAILURE MODE.
        # ══════════════════════════════════════════════════════════════════
        # Twelve lines below, the extraction loop opens `if not extractor:
        # break`. A feed with a live fetcher, a 200, a clean parse and a
        # passing contract, but NO EXTRACTORS entry, therefore breaks on its
        # first item and keeps nothing — and the run reports `ok=1
        # items_kept=0`, which is indistinguishable from a quiet week. TWO
        # FEEDS SAT IN EXACTLY THAT STATE FOR WEEKS (`nku`, `ec-hys`), and
        # nothing anywhere said so, because every single check they pass IS
        # passing: transport, parse, required_fields and yield are all
        # measured on items FETCHED, never on records KEPT.
        #
        # The fix is to make the one thing nobody measured into a contract
        # failure. `ok=1 items_kept=0` remains a legal state for exactly the
        # rows that DECLARE it — `role: enrichment`, `signal_source: null`,
        # `id_prefixes: []` (ares, shoptet, upgates) — and is a first-class
        # error for every row that claims to produce signals.
        #
        # DERIVED FROM THE REGISTRY, never from a list kept here. A hardcoded
        # exemption list drifts from feeds.json the first time a role changes,
        # and drifts silent — which is the failure this guard exists to end.
        if ok and EXTRACTORS.get(feed_key) is None and produces_signals(feed):
            ok = False
            anomaly = anomaly or "zero"
            error = (f"no extractor: scripts/normalize.py EXTRACTORS has no "
                     f"`{feed_key}` entry, so all {len(items_all)} fetched item(s) "
                     f"were discarded and this feed can never write a record. The "
                     f"payload, the transport and the contract are all FINE — this "
                     f"is the wiring. Add an extractor, or set `role: enrichment` "
                     f"in data/feeds.json if the feed is genuinely not meant to "
                     f"produce signals.")

        kept = 0
        if ok:
            payload_text = ""
            for fn in fnames:
                try:
                    payload_text += collapse(open(os.path.join(raw_dir, fn), "r",
                                                  encoding="utf-8", errors="replace").read())
                except OSError:
                    pass
            extractor = EXTRACTORS.get(feed_key)
            # zip, not enumerate-and-index: pkeys_all is built in lockstep with
            # items_all above, so item i always carries the key of the file it
            # was actually read from.
            for it, pkey in zip(items_all, pkeys_all):
                if not extractor:
                    break
                try:
                    rec = extractor(it if isinstance(it, dict) else {}, pkey, today)
                except Exception as e:  # noqa: BLE001
                    log(f"normalize: {feed_key}: extractor error on one item — {type(e).__name__}: {e}")
                    continue
                if not rec or not rec.get("id"):
                    continue
                if rec["id"] in seen:
                    dupes += 1
                    continue
                seen.add(rec["id"])

                # -------- the arithmetic --------
                rec["money_eur"] = rec.get("money_eur")
                u = score_urgency(rec.get("urgency_date"), today)
                rec["urgency_pending"] = (u is None)
                rec["scores"] = {"money": score_money(rec.get("money_eur")),
                                 "urgency": 0 if u is None else u}
                # fetched_at IS THE FETCH'S CLOCK, NOT OURS — same rule as
                # http_status one line down, and it was being broken in the same
                # loop that fixed that one. CONVENTIONS.md defines the field as
                # "ISO timestamp of the payload this record came from" and
                # SPEC §3 as "when the payload this record came from was
                # fetched". `started` is when NORMALIZE started, which is a
                # different event: MEASURED 2026-08-20 on the committed payloads
                # — receipt started_at 09:19:56Z, record fetched_at 14:08:15Z,
                # 4h48m of drift on a same-day re-normalize. The attended loop
                # completes a raw dir a session later, so the drift is days, and
                # `fetched_at` is precisely the field someone reads to ask how
                # old this evidence is.
                #
                # No receipt -> the key is OMITTED (apply_allowlist drops empty
                # optional receipts), never back-filled from our clock. A
                # synthesized timestamp is worse than a missing one, because it
                # reads as evidence.
                rec["fetched_at"] = fetched_at
                rec["http_status"] = http_status
                rec["extraction"] = "structured"

                # -------- quote, VERIFIED against the payload still on disk --------
                # Checked against the parsed item's own text FIRST, then the raw
                # file bytes. Both are "the payload we fetched"; the two differ
                # only by serialization escaping, and that difference is real:
                # a newline inside a JSON string is the two characters \ and n
                # on disk but one character once parsed, so a substring test
                # against raw bytes alone rejects a perfectly verbatim quote.
                # MEASURED: raw-bytes-only rejected 20 of 4,397 real YC records
                # (0.45%), every one of them a false negative from an escape.
                parts = [collapse(p) for p in (rec.pop("quote_parts", []) or []) if collapse(p)]
                item_text = collapse(" ".join(item_strings(it)))
                verified = [p for p in parts if p and (p in item_text or p in payload_text)]
                rec["_quote_unverified"] = [p for p in parts if p not in verified]
                quote = " — ".join(verified)[:300]
                if not quote:
                    quote_failures.append(rec["id"])
                rec["quote"] = quote

                # AC-GDPR1, first enforcement point. Scanned on the ALLOWLISTED
                # view, so a hit means personal data reached a field that is
                # itself legitimate. Fail CLOSED: refuse the record rather than
                # redacting it, because a silent redaction mangles a verbatim
                # quote AND hides that a feed is emitting contact data at all.
                ledger_view, _ = apply_allowlist(rec)
                viols = gdpr_violations(ledger_view)
                if viols:
                    gdpr_refused.append((rec["id"], feed_key, viols))
                    continue

                rec["_feed_key"] = feed_key
                rec["_needs"] = model_debt(feed_key, rec)
                staged.append(rec)
                kept += 1

        finished = datetime.now(timezone.utc)
        rc = receipt or {}
        # Transport columns come from the receipt; item counts are ours, because
        # the fetcher does not parse. Where the receipt is absent the value stays
        # None rather than being back-filled from a normalize-side guess.
        results.append({
            "run_id": rc.get("run_id") or run_id, "feed_key": feed_key,
            "started_at": rc.get("started_at") or started.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "finished_at": rc.get("finished_at") or finished.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "http_status": http_status,
            "bytes": rc.get("bytes") if rc.get("bytes") is not None else nbytes,
            "items_fetched": len(items_all), "items_kept": kept,
            "yield_anomaly": anomaly, "parse_method": parse_method,
            "runtime_ms": rc.get("runtime_ms"),
            "ok": 1 if ok else 0,
            # THE FETCHER'S NOTE SURVIVES A CLEAN CONTRACT VERDICT. A fetcher
            # can succeed and still have something to say — "partial: 2 of 16
            # failed", "coverage: 175 of 2,431 available". Those notes ride on
            # an ok=1 receipt, and overwriting `error` with our own None
            # silently deleted every one of them on the way to fetch_log and
            # /sources. Our verdict wins when we have one; otherwise theirs
            # stands.
            "error": error or (rc.get("error") or None),
            "raw_path": rc.get("raw_path") or os.path.relpath(
                os.path.join(raw_dir, fnames[0]), ROOT),
        })

    # Registered feeds with no payload at all: recorded, because silence is the
    # failure mode a contract cannot see.
    #
    # But NOT the attended harvests. `demand-scan`, `arb-scan` and `round` are
    # monthly agent passes, not part of an automated fetch cycle, so their
    # absence from any given hourly run is expected — flagging them would fire
    # an alarm on every single run forever. An alarm that cries wolf weekly gets
    # ignored within a month, and once it is ignored the one real outage is
    # invisible too. Their staleness is a health-view question (STALE against a
    # monthly cadence), not a per-run contract failure.
    for key, feed in registry.items():
        if key in by_feed or feed.get("role") == "enrichment":
            continue
        if feed.get("status") in ("planned", "dead"):
            continue
        if feed.get("runner") == "attended":
            continue
        rc = receipts.get(key)
        if rc:
            # The fetcher ran and produced no parseable file. Its own verdict is
            # the truth — a `skipped` here is an expected absence, not a failure,
            # and calling it one would be the cry-wolf alarm §7.2 warns about.
            ok_r, err_r, anom_r, pm_r = evaluate_contract(feed, [], True, None,
                                                          rc.get("bytes") or 0, rc)
            results.append({
                "run_id": rc.get("run_id") or run_id, "feed_key": key,
                "started_at": rc.get("started_at"),
                "finished_at": rc.get("finished_at"),
                "http_status": rc.get("http_status"), "bytes": rc.get("bytes") or 0,
                "items_fetched": rc.get("items_fetched") or 0, "items_kept": 0,
                "yield_anomaly": anom_r, "parse_method": pm_r,
                "runtime_ms": rc.get("runtime_ms"),
                "ok": 1 if ok_r else 0, "error": err_r,
                "raw_path": rc.get("raw_path"),
            })
            continue
        no_receipt.append(key)
        results.append({
            "run_id": run_id, "feed_key": key,
            "started_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "finished_at": None, "http_status": None, "bytes": 0,
            "items_fetched": 0, "items_kept": 0, "yield_anomaly": "zero",
            "parse_method": "none", "runtime_ms": None, "ok": 0,
            "error": "no fetch receipt and no payload — the feed did not run",
            "raw_path": None,
        })

    # ── the SECOND dedup axis, run here as well as at --complete ─────────────
    # Screening at STAGING is not redundant with screening at append: a record
    # that will be skipped anyway must not be handed to the model pass first.
    # That pass is the expensive half (one subagent or one API call per batch),
    # and asking it to write a sector and a scale for 50 records that are about
    # to be thrown away is the whole cost of the run spent on nothing.
    by_id = {r.get("id"): r for r in staged}
    staged, dup_skipped, dup_exempt = screen_duplicates(staged, build_key_index(
        os.path.abspath(args.out_dir)))

    with open(os.path.join(raw_dir, "contract.json"), "w", encoding="utf-8") as fh:
        json.dump({"run_id": run_id,
                   "raw_dir": os.path.relpath(raw_dir, ROOT),
                   "results": results}, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    with open(os.path.join(raw_dir, "staged.jsonl"), "w", encoding="utf-8") as fh:
        for r in staged:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    write_manifest(raw_dir, run_id, today, results, staged, unmapped, dupes,
                   quote_failures, gdpr_refused, dup_skipped, dup_exempt, by_id)

    print(f"normalize --mechanical-only  run_id={run_id}")
    print(f"  feeds with payloads : {len(by_feed)}   unmapped files: {len(unmapped)}")
    print(f"  staged records      : {len(staged)}   deduped against seen.txt: {dupes}")
    report_duplicates(by_id, dup_skipped, dup_exempt, "staging")
    print(f"  quote not verified  : {len(quote_failures)}")
    print(f"  contract failures   : {sum(1 for r in results if not r['ok'])}")
    print(f"  AC-GDPR1 refused    : {len(gdpr_refused)}")
    if gdpr_refused:
        log(f"AC-GDPR1: {len(gdpr_refused)} record(s) carried personal data and were "
            f"REFUSED before staging — they are not in staged.jsonl and cannot reach a ledger.")
        for sid, fk, viols in gdpr_refused[:5]:
            for field, kind, snip in viols[:1]:
                log(f"  {fk}/{sid}: {kind} in `{field}` -> {snip!r}")
    print(f"  wrote {os.path.relpath(raw_dir, ROOT)}/{{staged.jsonl,contract.json,manifest.md}}")
    print("  APPENDED NOTHING to the ledgers — every record still owes scale and")
    print("  recurrence to a model. Complete them in ATTENDED mode, then run --complete.")
    return 0


def write_manifest(raw_dir, run_id, today, results, staged, unmapped, dupes,
                   quote_failures, gdpr_refused=(), dup_skipped=(), dup_exempt=(),
                   staged_by_id=None):
    L = []
    L.append(f"# Ingest run {run_id}\n")
    L.append(f"Run date: {today.isoformat()}  ·  mode: mechanical-only (no model, no secrets, no network)\n")
    L.append("\n## Feed contracts\n\n")
    L.append("| feed | http | bytes | fetched | kept | yield | parse | ok | error |\n")
    L.append("|---|---|---|---|---|---|---|---|---|\n")
    for r in sorted(results, key=lambda x: x["feed_key"]):
        L.append(f"| `{r['feed_key']}` | {r['http_status'] or '—'} | {r['bytes']} | "
                 f"{r['items_fetched']} | {r['items_kept']} | {r['yield_anomaly'] or '—'} | "
                 f"{r['parse_method']} | {'yes' if r['ok'] else '**NO**'} | {r['error'] or ''} |\n")
    bad = [r for r in results if not r["ok"]]
    if bad:
        L.append(f"\n**{len(bad)} feed(s) failed their contract this run.** A contract violation is a "
                 f"first-class error: a 200 carrying the wrong body is a lie, where a 500 is honest.\n")
    L.append(f"\n## Staged records — PENDING, not appended\n\n")
    L.append(f"{len(staged)} records carry their mechanical fields and are waiting on a model. "
             f"{dupes} were dropped as already present in `seen.txt`.\n\n")
    if quote_failures:
        L.append(f"**{len(quote_failures)} staged records have no verifiable quote** — no candidate "
                 f"snippet was found as a literal substring of the payload. These must not be "
                 f"appended for a scripted feed.\n\n")
    need = {}
    for r in staged:
        for n in r.get("_needs", []):
            need[n] = need.get(n, 0) + 1
    if need:
        L.append("| still owed by a model | records |\n|---|---|\n")
        for k, v in sorted(need.items(), key=lambda kv: -kv[1]):
            L.append(f"| `{k}` | {v} |\n")
    unknown = [r["feed_key"] for r in results if r["http_status"] is None]
    if unknown:
        L.append(f"\n**Transport status UNKNOWN for {len(unknown)} feed(s):** "
                 f"{', '.join('`' + u + '`' for u in sorted(set(unknown)))}. No fetch receipt "
                 f"was found in `.fetch/receipts.jsonl`, so no status is recorded. This is "
                 f"deliberately blank rather than inferred: bytes on disk are not evidence of "
                 f"a 200, and an invented status reads as proof.\n")
    L.append(f"\n## AC-GDPR1 — contact-field gate\n\n")
    if gdpr_refused:
        L.append(f"**{len(gdpr_refused)} record(s) REFUSED for carrying personal data.** They "
                 f"were dropped before staging and cannot reach a ledger. The ledgers are "
                 f"public and append-only, so this gate fails closed rather than redacting.\n\n")
        L.append("| record | feed | field | kind |\n|---|---|---|---|\n")
        for sid, fk, viols in gdpr_refused[:25]:
            for field, kind, _snip in viols[:1]:
                L.append(f"| `{sid}` | `{fk}` | `{field}` | {kind} |\n")
        L.append("\nSnippets are deliberately NOT printed here: this manifest is committed, "
                 "and writing the offending value into it would publish exactly what the gate "
                 "just prevented.\n")
    else:
        L.append(f"No personal data detected. {len(staged)} staged record(s) passed the "
                 f"field allowlist and the email/phone content scan.\n")
    # ── the identity-key dedup, ON THE COMMITTED RECORD ─────────────────────
    # This section is the point of the pass. A record that was skipped is a
    # record that will never appear in a ledger, and the ONLY place that fact
    # survives is here — so it names both ids and the URL. A silent drop and a
    # silent duplicate are equally invisible.
    L.append("\n## Dedup by identity key — same resource, different id\n\n")
    if dup_skipped:
        L.append(f"**{len(dup_skipped)} staged record(s) name a resource the ledger "
                 f"already holds under a DIFFERENT id.** They were removed before "
                 f"staging, so no model was asked to complete them and nothing was "
                 f"appended. `seen.txt` is id-keyed and cannot see this case.\n\n")
        L.append("| staged id | already in the ledger as | key | feed | url |\n|---|---|---|---|---|\n")
        for new_id, old_id, key, feed in dup_skipped:
            url = ((staged_by_id or {}).get(new_id) or {}).get("url") or ""
            L.append(f"| `{new_id}` | `{old_id}` | `{key.split(':', 1)[0]}` | "
                     f"`{feed or '—'}` | {url} |\n")
    else:
        L.append("No staged record matched an existing record on an identity key.\n")
    if dup_exempt:
        L.append(f"\n**{len(dup_exempt)} key(s) were EXEMPTED from dedup**, because a key "
                 f"naming more than one record is a listing page, a dataset landing page "
                 f"or a roundup — not an identity. Merging on one would delete distinct "
                 f"records. Measured over the committed corpus: 67 urls are shared by 571 "
                 f"records (6.1%), one Vestbee roundup being the url of 32 funding rounds.\n\n")
        L.append("| key | why it was not used |\n|---|---|\n")
        for k, reason, _n in dup_exempt[:40]:
            L.append(f"| `{k[:120]}` | {reason} |\n")
        if len(dup_exempt) > 40:
            L.append(f"| … and {len(dup_exempt) - 40} more | |\n")
    if unmapped:
        L.append(f"\n## Unmapped payloads\n\nNo registry feed claims these files, so nothing "
                 f"parsed them. They are named here rather than dropped silently:\n\n")
        for f in unmapped:
            L.append(f"- `{f}`\n")
    # APPEND, NEVER TRUNCATE. manifest.md is deliberately un-ignored in
    # .gitignore so it survives as the committed human-readable record of what
    # each fetch did — and the FETCH-side rows are written by the fetchers, not
    # by us. Opening it "w" destroyed their table and every other feed's entry
    # from the same run. We append our normalize-side section and leave
    # everything already there untouched.
    path = os.path.join(raw_dir, "manifest.md")
    existing = ""
    if os.path.isfile(path):
        try:
            existing = open(path, "r", encoding="utf-8").read()
        except OSError:
            existing = ""
    body = "".join(L)
    with open(path, "w", encoding="utf-8") as fh:
        if existing:
            fh.write(existing.rstrip("\n") + "\n\n---\n\n")
        fh.write(body)


# --------------------------------------------------------------------------
# --complete: the attended append path
# --------------------------------------------------------------------------

# REQUIRED_OUT and its predicate live beside model_debt() above, because the two
# are one rule with two readers. Do not restate the list here.
SECTORS = {"fintech", "health", "housing", "energy", "mobility", "govtech",
           "retail-services", "b2b", "legal-compliance", "education",
           "environment", "other"}


def run_complete(args):
    raw_dir = os.path.abspath(args.raw)
    staged_path = os.path.join(raw_dir, "staged.jsonl")
    if not os.path.isfile(staged_path):
        log(f"normalize: {staged_path} not found — run --mechanical-only first")
        return 1
    signals_dir = os.path.abspath(args.out_dir)
    seen_path = args.seen
    seen = load_seen(seen_path)

    records, incomplete, dropped, appended = [], [], 0, 0
    gdpr_refused, allowlist_drops = [], {}
    with open(staged_path, "r", encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if not line.strip():
                continue
            r = json.loads(line)
            sc = r.get("scores") or {}
            # Same predicate model_debt() asks, so a record filled to exactly
            # what `_needs` listed cannot be refused here for a field nobody
            # was told about.
            missing = missing_required(r)
            for k in ("scale", "recurrence", "money", "urgency"):
                if not isinstance(sc.get(k), int):
                    missing.append(f"scores.{k}")
            if r.get("sector") not in SECTORS:
                missing.append("sector(valid)")
            # The same rule SignalSchema applies in web/lib/data.ts, applied
            # HERE so a bad date is refused before it enters an append-only
            # ledger rather than turning up as a red build afterwards. An
            # append-only log has no quiet cleanup.
            if r.get("date") and not ISO_DATE_RE.match(str(r["date"])):
                missing.append("date(ISO YYYY-MM-DD)")
            if missing:
                incomplete.append((r.get("id", f"line {n}"), missing))
                continue
            records.append(r)

    if incomplete and not args.allow_incomplete:
        log(f"normalize --complete: {len(incomplete)} staged records are still missing model fields.")
        for sid, m in incomplete[:10]:
            log(f"  {sid}: {', '.join(sorted(set(m)))}")
        if len(incomplete) > 10:
            log(f"  ... and {len(incomplete) - 10} more")
        log("Refusing to append. Unscored records are NEVER written with default scores —")
        log("losing freshness is recoverable; writing vibes into an append-only ledger is not.")
        return 1

    # THE LEDGER FILE IS NAMED BY THE RUN DATE, NEVER BY THE RECORD'S OWN DATE.
    # SPEC §3 and CONVENTIONS both say "one JSONL file per evidence type per RUN
    # DATE", the committed corpus is exactly that (two files per type, dated
    # 2026-08-13 and 2026-08-14, holding 98 distinct record dates between them),
    # and db.py reads the FILENAME as the run date on purpose — 145 records are
    # legitimately dated in the future because a regulation signal carries its
    # effective date. Naming the file after `record.date` would have scattered
    # one run across a file per record date, dated a yc-oss batch to 2011, and
    # made every feed's freshness read off the wrong number.
    #
    # AND THE RUN DATE IS THE RUN'S, NOT THE CLOCK'S. `--complete` is the
    # ATTENDED half: it is run by a session that reads staged.jsonl and fills
    # `_needs`, which routinely happens after midnight relative to the fetch.
    # Reading date.today() there names the ledger for the day the human sat
    # down, so the SAME staged file completed on two days lands in two
    # differently-named files, and ingest.sh's own printed hand-off
    # (`db.py upsert data/signals/<type>/$TODAY.jsonl`, $TODAY = the FETCH day)
    # points at a path that does not exist. `data/raw/<date>/` already carries
    # the run date in its name — that is the same string db.py reads back — so
    # take it from there. --today still wins for a deterministic re-run, and a
    # raw dir not named for a date falls through to the clock as before.
    run_date = args.today or run_date_from_raw(args.raw) or date.today().isoformat()

    # ── THE LAST GATE BEFORE AN IRREVERSIBLE APPEND ─────────────────────────
    # Run here as well as at staging, and NOT because staging might have missed
    # it. A staged.jsonl is completed by a human session that routinely runs
    # hours or days after the mechanical pass, and the ledger moves in between —
    # another run may have appended the very record this batch is about to
    # duplicate. The staging screen is an economy; THIS one is the gate. The
    # ledgers are append-only: a wrong append has no quiet cleanup.
    dup_by_id = {r.get("id"): r for r in records}
    records, dup_skipped, dup_exempt = screen_duplicates(
        records, build_key_index(signals_dir))

    by_file = {}
    id_dupes = []
    for r in records:
        if not is_material(r["scores"]):
            dropped += 1
            continue
        if r["id"] in seen:
            # WAS A BARE `continue` — the one drop in this file that told
            # nobody. An id already in seen.txt is the ordinary re-run case and
            # is not alarming, but it is still a record that will not appear,
            # and "did not appear" must never be something the output leaves the
            # reader to infer from a count that does not add up.
            id_dupes.append(r["id"])
            continue
        typ = r.get("evidence_type") or "demand"
        out = os.path.join(signals_dir, typ, f"{run_date}.jsonl")

        # AC-GDPR1, THE HARD GATE — the last code between a record and a public,
        # append-only, permanent log.
        #
        # This is an ALLOWLIST, and that is the whole point: it replaced a
        # denylist that stripped a fixed set of internal staging keys. The
        # denylist worked only for the fields someone had thought of, so the
        # first feed to emit `contact_email` would have sailed straight through
        # it. The allowlist drops that field without anyone having predicted it.
        # NB: `dropped_fields`, deliberately NOT `dropped` — that name is the
        # materiality counter a few lines above, and shadowing it turned the
        # count into a list and would have raised TypeError on the next
        # materiality drop.
        clean, dropped_fields = apply_allowlist(r)
        viols = gdpr_violations(clean)
        if viols:
            gdpr_refused.append((r.get("id"), viols))
            continue
        if dropped_fields:
            allowlist_drops[r.get("id")] = dropped_fields

        by_file.setdefault(out, []).append(clean)
        seen.add(r["id"])
        appended += 1

    def report_gdpr():
        if allowlist_drops:
            n = sum(len(v) for v in allowlist_drops.values())
            fields = sorted({f for v in allowlist_drops.values() for f in v})
            print(f"  AC-GDPR1 allowlist: dropped {n} non-allowlisted field(s) across "
                  f"{len(allowlist_drops)} record(s): {', '.join(fields[:12])}")
        if gdpr_refused:
            log(f"\nAC-GDPR1 VIOLATION — {len(gdpr_refused)} record(s) REFUSED, not written.")
            log("Personal data reached an allowlisted field. The ledgers are public and")
            log("append-only, so this fails CLOSED: the record is dropped, never redacted.")
            for sid, viols in gdpr_refused[:10]:
                for field, kind, snip in viols[:2]:
                    log(f"  {sid}: {kind} in `{field}` -> {snip!r}")
            if len(gdpr_refused) > 10:
                log(f"  ... and {len(gdpr_refused) - 10} more")

    def report_dedup():
        report_duplicates(dup_by_id, dup_skipped, dup_exempt, "append")
        if id_dupes:
            print(f"  already in seen.txt (id-keyed): {len(id_dupes)} skipped — "
                  f"{', '.join(id_dupes[:6])}{' …' if len(id_dupes) > 6 else ''}")

    if args.dry_run:
        print(f"normalize --complete --dry-run: would append {appended} records "
              f"across {len(by_file)} file(s); {dropped} dropped by materiality; "
              f"{len(incomplete)} incomplete; {len(gdpr_refused)} refused by AC-GDPR1.")
        for f, rs in sorted(by_file.items()):
            print(f"  {os.path.relpath(f, ROOT)}: +{len(rs)}")
        report_dedup()
        report_gdpr()
        return 1 if gdpr_refused else 0

    for out, rs in sorted(by_file.items()):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "a", encoding="utf-8") as fh:
            for r in rs:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(seen_path, "w", encoding="utf-8") as fh:
        for sid in sorted(seen):
            fh.write(sid + "\n")

    print(f"normalize --complete: appended {appended} records across {len(by_file)} file(s)")
    print(f"  materiality drops: {dropped}   incomplete skipped: {len(incomplete)}")
    for f, rs in sorted(by_file.items()):
        print(f"  {os.path.relpath(f, ROOT)}: +{len(rs)}")
    report_dedup()
    report_gdpr()
    print("  Next: python3 scripts/db.py upsert <each file above>")
    # A GDPR refusal exits non-zero even though the clean records were written.
    # The written records are fine; what must not happen is a runner absorbing a
    # personal-data event as a green run.
    return 1 if gdpr_refused else 0


# --------------------------------------------------------------------------
# the model path — WIRED AND LIVE, through a seam this file cannot cross alone
# --------------------------------------------------------------------------

MODEL_PASS_PY = os.path.join(ROOT, "scripts", "model_pass.py")
MODEL_PASS_SH = os.path.join(ROOT, "scripts", "model_pass.sh")
MODEL_PASS_AGENT = os.path.join(ROOT, "scripts", "model_pass_agent.py")

# `model_passes` returns this when the SUBAGENT driver has planned work that only
# a session's subagents can do. It is a HANDOFF, not a failure, and it is its own
# code precisely so a caller cannot confuse the two: 0 would claim the records are
# filled when they are not, and 2 would claim the seam is broken when it is
# waiting. ingest.sh maps it to a message, not to a non-zero exit.
RC_AGENT_PENDING = 3


def _run(cmd):
    """Run one child, streaming its output. Returns its exit code."""
    import subprocess
    log("  $ " + " ".join(cmd[-6:] if len(cmd) > 6 else cmd))
    return subprocess.call(cmd, cwd=ROOT)


def _short(path):
    """Repo-relative when the path is inside the repo, absolute otherwise. A blind
    os.path.relpath turns a scratch dir into ../../../../../private/tmp/... , which
    is a copy-pasteable command only by accident."""
    rel = os.path.relpath(path, ROOT)
    return path if rel.startswith("..") else rel


def _agent_pending(raw, pass_):
    """How many batches of this pass still await a subagent, per the worklist the
    agent driver just wrote. -1 if the worklist is unreadable."""
    path = os.path.join(raw, ".model", "agent", f"worklist-{pass_}.json")
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return len(json.load(fh).get("pending") or [])
    except Exception:                                  # noqa: BLE001
        return -1


def model_passes(args):
    """
    Pass A (scoring: scale, recurrence, grade-3 urgency, sector, geo_origin and
    the suggest/reddit pain bar), then the MATERIALITY FILTER, then pass B
    (EN title + summary over survivors only).

    THIS FUNCTION DRIVES THE PASSES; IT DOES NOT MAKE THE CALL. It never could:
    `with-secrets` REFUSES bash, node, python, jq, awk and sed by allowlist,
    because an interpreter can encode a secret past its output scrubber, and
    normalize.py IS a python interpreter. What changed on 2026-08-20 is WHICH
    driver sits in the middle, and there are now two:

      SUBAGENT (the default, --model-driver agent). Costs NO API credit. The
        owner's ruling after the balance ran out mid-run — HTTP 400, "Your credit
        balance is too low", 51 material survivors stranded — was: "instead of
        running Claude thru api credits, can you run the logic thru subagents?"
        So: plan -> scripts/model_pass_agent.py worklist -> a session's subagents
        fill one answer file per batch -> collect -> apply.

        THIS PATH CANNOT COMPLETE ITSELF FROM A SCRIPT, and that is measured, not
        assumed. `claude -p` was tried twice on 2026-08-20: sandboxed it printed
        "Not logged in · Please run /login" (the Keychain read is denied), and
        unsandboxed "401 OAuth access token has expired". No shell script on this
        box can spawn an agent. So when batches are still pending this returns
        RC_AGENT_PENDING and prints the handoff — it does NOT quietly fall back
        to the API path, because a silent fallback between a free driver and a
        paid one is indistinguishable from either working. Re-running after the
        agents have written their answers resumes exactly where it stopped.

      API (--model-driver api). SPENDS the credit balance. Kept because it costs
        nothing to keep and it is proven: `with-secrets curl --variable
        '%ANTHROPIC_API_KEY' --expand-header 'x-api-key: {{…}}' … /v1/messages`
        returns HTTP 200 from claude-opus-5, and 3,092 records landed through it.
        The authenticated call lives in scripts/model_pass.sh, which wraps ONLY
        the individual curl — the same rule fetch_hlidac.sh follows for the
        Hlídač token.

    Either way `apply` is the QA gate and staged.jsonl is written by `apply`
    alone, temp + os.replace, so a crash anywhere leaves a whole file and the
    next run resumes from it.

    STILL NOTHING WRITES DEFAULTS. Every field is validated against the closed
    vocabularies before it is written; a record whose fields did not validate
    keeps its `_needs` and stays staged. Losing freshness is recoverable, writing
    vibes into an append-only canonical ledger is not.
    """
    driver = getattr(args, "model_driver", "agent")
    needed = [MODEL_PASS_PY] + ([MODEL_PASS_AGENT] if driver == "agent" else [MODEL_PASS_SH])
    missing = [p for p in needed if not os.path.isfile(p)]
    if missing:
        log("normalize: missing " + ", ".join(os.path.relpath(p, ROOT) for p in missing))
        log("  — the model seam is not installed. Refusing to improvise a")
        log("  replacement (INGEST.md step 0).")
        return 2

    raw = os.path.abspath(args.raw)
    shards = max(1, int(getattr(args, "model_shards", 1)))
    # SAY WHICH DRIVER RAN, EVERY TIME AND BEFORE IT RUNS. One of these spends
    # money and one does not; an output that does not distinguish them would read
    # identically whichever ran.
    if driver == "agent":
        log("normalize: model driver = SUBAGENT — no API credit is spent.")
    else:
        log("normalize: model driver = API (--model-driver api) — this SPENDS the")
        log("  Anthropic credit balance, one request per batch.")

    for pass_ in ("A", "B"):
        rc = _run([sys.executable, MODEL_PASS_PY, "plan", "--raw", raw,
                   "--pass", pass_, "--batch", str(args.model_batch),
                   "--effort", args.model_effort])
        if rc != 0:
            log(f"normalize: model pass {pass_} could not be planned (rc={rc}).")
            return 2

        if driver == "agent":
            # collect FIRST: a previous round's subagents may already have left
            # answers on disk, and those become response files before we decide
            # what is still outstanding. This is what makes the whole loop
            # resumable by simply running the command again.
            if _run([sys.executable, MODEL_PASS_AGENT, "collect",
                     "--raw", raw, "--pass", pass_]) != 0:
                log(f"normalize: could not collect pass {pass_} agent answers.")
                return 2
            if _run([sys.executable, MODEL_PASS_AGENT, "worklist",
                     "--raw", raw, "--pass", pass_]) != 0:
                log(f"normalize: could not build the pass {pass_} worklist.")
                return 2
            n = _agent_pending(raw, pass_)
            if n != 0:
                rel = _short(raw)
                log("")
                log(f"normalize: PASS {pass_} AWAITS {n} SUBAGENT(S). Nothing is wrong and")
                log("  nothing was written. Each pending batch has a self-contained prompt")
                log(f"  listed in {rel}/.model/agent/worklist-{pass_}.json; give each one to")
                log("  its own subagent, which writes the matching .answer.json. Then:")
                # --model-only, NOT the bare default path: this raw dir is already
                # staged, and re-running the mechanical pass over it is not what
                # "resume" means. Same --model-batch too — the batch name encodes
                # the batch's POSITION as well as its members, so re-planning at a
                # different size renames every batch and orphans the responses
                # already on disk.
                log(f"    python3 scripts/normalize.py --raw {rel} --model-only "
                    f"--model-batch {args.model_batch}")
                log("  A batch is done when its response file exists, so an abandoned")
                log("  agent costs only its own batch. To spend credit instead, add")
                log("  --model-driver api.")
                return RC_AGENT_PENDING
        else:
            # THE SHARDS ARE SEQUENTIAL HERE ON PURPOSE. Running them concurrently
            # is supported by the driver (each shard writes only its own response
            # files) but a scheduler-driven run has nobody watching a rate limit,
            # so the unattended path takes the slow, safe lane. An attended
            # operator runs the same script N times in parallel by hand.
            for shard in range(shards):
                rc = _run(["/bin/bash", MODEL_PASS_SH, raw, pass_, str(shard), str(shards)])
                if rc == 2:
                    log("normalize: the model driver could not run (rc=2). NOTHING was")
                    log("  written. Do not work around this and do not export the key by hand.")
                    return 2

        rc = _run([sys.executable, MODEL_PASS_PY, "apply", "--raw", raw, "--pass", pass_])
        if rc != 0:
            log(f"normalize: model pass {pass_} could not be applied (rc={rc}).")
            return 2

    log(f"normalize: model passes A and B complete via the "
        f"{'SUBAGENT' if driver == 'agent' else 'API'} driver. staged.jsonl now")
    log("  carries the model fields. Nothing has been appended to a ledger yet —")
    log("  that is --complete:")
    log(f"    python3 scripts/normalize.py --raw {_short(raw)} --complete")
    return 0


def main():
    p = argparse.ArgumentParser(prog="normalize.py", description=__doc__,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--raw", required=True, help="data/raw/<date>/")
    p.add_argument("--mechanical-only", action="store_true",
                   help="the arithmetic path: no model, no secrets, no network")
    p.add_argument("--model-only", action="store_true",
                   help="the model passes ALONE, over an already-staged raw dir "
                        "(ingest.sh has already run --mechanical-only; re-running "
                        "it there would re-stage an already-staged run)")
    p.add_argument("--complete", action="store_true",
                   help="append a model-completed staged.jsonl to the ledgers")
    p.add_argument("--out-dir", default=DEFAULT_SIGNALS_DIR,
                   help="signals root (override for testing; default data/signals)")
    p.add_argument("--seen", default=os.path.join(DEFAULT_SIGNALS_DIR, "seen.txt"),
                   help="dedup index (override for testing)")
    p.add_argument("--today", default=None, help="YYYY-MM-DD, for deterministic runs")
    p.add_argument("--dry-run", action="store_true", help="--complete: write nothing")
    p.add_argument("--allow-incomplete", action="store_true",
                   help="--complete: append the complete records and skip the rest")
    p.add_argument("--model-driver", default="agent", choices=["agent", "api"],
                   help="default path: 'agent' (DEFAULT, subagents, no API credit) "
                        "or 'api' (curl to /v1/messages, SPENDS credit)")
    p.add_argument("--model-batch", type=int, default=50,
                   help="default path: records per model request/prompt. 50 is the "
                        "measured subagent knee — see AGENT_BATCH in "
                        "scripts/model_pass_agent.py for the experiment. Changing it "
                        "between runs RENAMES every batch and orphans responses "
                        "already on disk, so keep it fixed across a resume.")
    p.add_argument("--model-effort", default="medium",
                   choices=["low", "medium", "high", "xhigh", "max"],
                   help="default path: output_config.effort for the model passes")
    p.add_argument("--model-shards", type=int, default=1,
                   help="default path: driver shards, run one after another")
    args = p.parse_args()

    if sum(bool(x) for x in (args.mechanical_only, args.model_only, args.complete)) > 1:
        log("normalize: --mechanical-only, --model-only and --complete are separate passes")
        sys.exit(2)
    if args.complete:
        sys.exit(run_complete(args))
    if args.mechanical_only:
        sys.exit(run_mechanical(args))
    if args.model_only:
        sys.exit(model_passes(args))
    rc = run_mechanical(args)
    if rc != 0:
        sys.exit(rc)
    sys.exit(model_passes(args))


if __name__ == "__main__":
    main()
