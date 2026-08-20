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
                      data/signals/<type>/<date>.jsonl + seen.txt, then upserts
                      into the DB. Needs no model of its own — the judgment
                      already happened.

  (default)           The UNATTENDED path: mechanical, then model passes A and B.
                      WIRED BUT INERT — see the model_passes() docstring. It
                      refuses to run rather than pretending.

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
from xml.etree import ElementTree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEEDS_JSON = os.path.join(ROOT, "data", "feeds.json")
DEFAULT_SIGNALS_DIR = os.path.join(ROOT, "data", "signals")

# A FIXED, STATED ASSUMPTION, not a live rate. Ingest must run with no network,
# so money_eur derived from a CZK figure uses this constant and money_note says
# so. A record whose EUR value matters to a decision is re-checked by a human,
# not silently re-derived from whatever the rate was that morning.
CZK_PER_EUR = 25.0

# CPV group -> sector. The group keys come from the CPV_GROUPS table in
# scripts/fetch_ted.sh, which is also what names the ted-<key>.json payloads.
# TED buyers are public bodies, so IT and business-services tenders land in
# govtech / b2b rather than a vertical.
CPV_SECTOR = {
    "it": "govtech",
    "health": "health",
    "bizserv": "b2b",
    "energy": "energy",
    "construction": "housing",
}

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
    ("czechcrunch", "cc-cz"), ("cc-cz", "cc-cz"),
    ("vestbee", "vestbee"),
    ("suggest", "suggest"),
    ("reddit-search", "reddit-search"), ("reddit_search", "reddit-search"),
    ("redditsearch", "reddit-search"),
    ("reddit", "reddit-new"),
    ("nku", "nku"), ("sukl", "sukl"), ("mpsv", "mpsv"), ("ares", "ares"),
    ("hys", "ec-hys"),
    ("nen", "nen"),
    ("ted", "ted"),
    ("yc", "yc-oss"),
]

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


def apply_allowlist(rec):
    """Return (clean_record, dropped_field_names). Unknown fields never survive."""
    clean = {k: v for k, v in rec.items() if k in LEDGER_ALLOWLIST}
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
    for token, key in FILE_FEED_TOKENS:
        if token in n:
            return key
    return None


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
    if not raw.strip():
        return [], False, "zero bytes"

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
        "date": str(d)[:10],
        "title_native": title,
        "entity_native": buyer,
        "sector": CPV_SECTOR.get(payload_key, "other"),
        "money_eur": money,
        "money_note": note,
        "urgency_date": str(deadline)[:10] if deadline else None,
        "quote_parts": [p for p in (title, (f"{val} {cur}" if val is not None else "")) if p],
        "excerpt": collapse(f"{title} — {buyer}"),
    }


def extract_hlidac(item, payload_key, today):
    nid = get_first(item, "identifikator", "id", "idVerze")
    if isinstance(nid, dict):
        nid = get_first(nid, "idSmlouvy", "id")
    if not nid:
        return None
    predmet = collapse(get_first(item, "predmet", "popis") or "")
    cena = get_first(item, "cenaSDph", "hodnotaSDph", "cenaBezDph")
    money = money_from_czk(cena) if cena is not None else None
    dt = get_first(item, "datumUzavreni", "datum") or ""
    return {
        "id": f"hlidac-{nid}",
        "source": "hlidac",
        "evidence_type": "tenders",
        "url": get_first(item, "odkaz", "url") or f"https://smlouvy.gov.cz/smlouva/{nid}",
        "date": str(dt)[:10],
        "title_native": predmet,
        "entity_native": collapse((item.get("platce") or {}).get("nazev", "")
                                  if isinstance(item.get("platce"), dict) else ""),
        "sector": None,
        "money_eur": money,
        "money_note": (f"{float(cena):,.0f} CZK (cenaSDph) at a fixed {CZK_PER_EUR} CZK/EUR"
                       if money is not None else ""),
        "urgency_date": None,
        "quote_parts": [p for p in (predmet, str(cena) if cena is not None else "") if p],
        "excerpt": predmet,
    }


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
        "date": str(get_first(item, "launched_at", "batch_date") or today.isoformat())[:10],
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
        "date": str(item.get("date") or today.isoformat())[:10],
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
    dt = get_first(item, "updated", "published", "pubDate") or today.isoformat()
    return {
        "id": f"reddit-{slugify(pid)}",
        "source": "reddit",
        "evidence_type": "demand",
        "url": get_first(item, "link") or "",
        "date": str(dt)[:10],
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
    dt = get_first(item, "pubDate", "published", "updated") or today.isoformat()
    return {
        "id": f"feed-{sha1_8(link)}",
        "source": "feed",
        "evidence_type": "funded",
        "url": link,
        "date": str(dt)[:10],
        "title_native": title,
        "entity_native": "",
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": None,
        "quote_parts": [first_sentence or title],
        "excerpt": collapse(f"{title} {desc}")[:400],
    }


EXTRACTORS = {
    "ted": extract_ted, "hlidac": extract_hlidac, "nen": extract_hlidac,
    "yc-oss": extract_yc, "suggest": extract_suggest,
    "reddit-new": extract_reddit, "reddit-search": extract_reddit,
    "cc-cz": extract_feed, "vestbee": extract_feed,
}

# Which fields a model still owes for a given feed, once the arithmetic is done.
# yc-oss is the only feed carrying English prose already, so it owes no title or
# summary; every feed owes scale and recurrence, which is why NOTHING can be
# appended by the mechanical pass alone.
def model_debt(feed_key, rec):
    debt = ["scores.scale", "scores.recurrence"]
    if feed_key != "yc-oss":
        debt += ["title", "summary"]
    if not rec.get("sector"):
        debt.append("sector")
    if rec.get("urgency_pending"):
        debt.append("scores.urgency")
    if feed_key in ("suggest", "reddit-new", "reddit-search"):
        debt.append("pain")  # transport-only admission bar; NEVER persisted
    return debt


# --------------------------------------------------------------------------
# contract evaluation
# --------------------------------------------------------------------------

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
        for fn in fnames:
            p = os.path.join(raw_dir, fn)
            nbytes += os.path.getsize(p)
            its, ok, err = parse_payload(p, (feed.get("contract") or {}).get("parse", "json"))
            if not ok:
                parse_ok, parse_err = False, f"{fn}: {err}"
            items_all.extend(its)

        # THE TRANSPORT RECEIPT IS READ, NEVER INFERRED. A feed with no receipt
        # carries http_status None — unknown — and the manifest says so.
        receipt = receipts.get(feed_key)
        http_status = (receipt or {}).get("http_status")
        if receipt is None:
            no_receipt.append(feed_key)
        ok, error, anomaly, parse_method = evaluate_contract(
            feed, items_all, parse_ok, parse_err, nbytes, receipt)

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
            for it in items_all:
                if not extractor:
                    break
                # A payload key like ted-it.json carries the CPV group.
                pkey = None
                for fn in fnames:
                    m = re.match(r"^(?:ted|hlidac)-(.+?)\.json$", fn, re.I)
                    if m:
                        pkey = m.group(1)
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
                rec["fetched_at"] = started.strftime("%Y-%m-%dT%H:%M:%SZ")
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
            "ok": 1 if ok else 0, "error": error,
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

    with open(os.path.join(raw_dir, "contract.json"), "w", encoding="utf-8") as fh:
        json.dump({"run_id": run_id,
                   "raw_dir": os.path.relpath(raw_dir, ROOT),
                   "results": results}, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    with open(os.path.join(raw_dir, "staged.jsonl"), "w", encoding="utf-8") as fh:
        for r in staged:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    write_manifest(raw_dir, run_id, today, results, staged, unmapped, dupes,
                   quote_failures, gdpr_refused)

    print(f"normalize --mechanical-only  run_id={run_id}")
    print(f"  feeds with payloads : {len(by_feed)}   unmapped files: {len(unmapped)}")
    print(f"  staged records      : {len(staged)}   deduped against seen.txt: {dupes}")
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
                   quote_failures, gdpr_refused=()):
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

REQUIRED_OUT = ("id", "source", "url", "date", "title", "sector", "geo_origin",
                "money_eur", "money_note", "summary", "scores")
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
            missing = [f for f in REQUIRED_OUT if r.get(f) in (None, "")
                       and f not in ("money_eur", "money_note")]
            for k in ("scale", "recurrence", "money", "urgency"):
                if not isinstance(sc.get(k), int):
                    missing.append(f"scores.{k}")
            if r.get("sector") not in SECTORS:
                missing.append("sector(valid)")
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

    by_file = {}
    for r in records:
        if not is_material(r["scores"]):
            dropped += 1
            continue
        if r["id"] in seen:
            continue
        typ = r.get("evidence_type") or "demand"
        d = r.get("date") or date.today().isoformat()
        out = os.path.join(signals_dir, typ, f"{d[:10]}.jsonl")

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

    if args.dry_run:
        print(f"normalize --complete --dry-run: would append {appended} records "
              f"across {len(by_file)} file(s); {dropped} dropped by materiality; "
              f"{len(incomplete)} incomplete; {len(gdpr_refused)} refused by AC-GDPR1.")
        for f, rs in sorted(by_file.items()):
            print(f"  {os.path.relpath(f, ROOT)}: +{len(rs)}")
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
    report_gdpr()
    print("  Next: python3 scripts/db.py upsert <each file above>")
    # A GDPR refusal exits non-zero even though the clean records were written.
    # The written records are fine; what must not happen is a runner absorbing a
    # personal-data event as a green run.
    return 1 if gdpr_refused else 0


# --------------------------------------------------------------------------
# the model path — WIRED, INERT, and it says so
# --------------------------------------------------------------------------

def model_passes(args):
    """
    Pass A (scoring: scale, recurrence, grade-3 urgency, the pain bar) and
    Pass B (EN title + summary over materiality survivors only).

    INERT ON PURPOSE. Two things are true at once and both matter:

      * ANTHROPIC_API_KEY EXISTS in the vault. The blocker is no longer a
        missing key.
      * NOBODY HAS MEASURED a nested `claude -p` authenticating from this
        pipeline. The `direnv exec .` path that earlier designs assumed exports
        nothing but DIRENV_* variables, and the working alternative
        (`with-secrets`) deliberately REFUSES bash, node and python, because an
        interpreter can encode a secret past the output scrubber. So this
        script — a python interpreter — cannot be wrapped wholesale, and the
        authenticated call site has to be designed on its own.

    Until someone runs that probe and reports the result either way, this
    function refuses rather than pretending. An honest negative is worth more
    than a plausible design: a scorer that looks wired and silently writes
    nothing is the vestbee failure with better branding.
    """
    log("normalize: the model passes are WIRED BUT INERT and were not run.")
    log("  Reason: no measured proof that a nested `claude -p` authenticates from this")
    log("  pipeline. ANTHROPIC_API_KEY exists, but `direnv exec .` exports nothing and")
    log("  `with-secrets` refuses interpreters (bash/node/python) by design.")
    log("  Use ATTENDED mode instead — it needs no key and it is how all 6,181 existing")
    log("  records were produced:")
    log("    1. python3 scripts/normalize.py --raw <dir> --mechanical-only")
    log("    2. an agent fills scale/recurrence/title/summary into <dir>/staged.jsonl")
    log("    3. python3 scripts/normalize.py --raw <dir> --complete")
    return 2


def main():
    p = argparse.ArgumentParser(prog="normalize.py", description=__doc__,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--raw", required=True, help="data/raw/<date>/")
    p.add_argument("--mechanical-only", action="store_true",
                   help="the arithmetic path: no model, no secrets, no network")
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
    args = p.parse_args()

    if args.mechanical_only and args.complete:
        log("normalize: --mechanical-only and --complete are separate passes")
        sys.exit(2)
    if args.complete:
        sys.exit(run_complete(args))
    if args.mechanical_only:
        sys.exit(run_mechanical(args))
    rc = run_mechanical(args)
    if rc != 0:
        sys.exit(rc)
    sys.exit(model_passes(args))


if __name__ == "__main__":
    main()
