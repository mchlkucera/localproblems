#!/usr/bin/env python3
"""
edesky_extract.py — the eDesky.cz `záměr` reader, and the normalize.py
extractor for it.

WHAT ONE RECORD IS
==================
A Czech municipality that means to ACQUIRE something — buy a plot, commission
a plan, place a small-scale contract, carry out a project — publishes that
intention on its official noticeboard (úřední deska) as a `záměr` before any
tender exists. A named owner (the desk), a stated intention, sometimes a sum:
an ASK in the sense of docs/superpowers/specs/2026-09-03-asks-ledger-design.md.
One record = one noticeboard document whose title carries an intention to
acquire.

THE SURFACE
===========
eDesky.cz aggregates 6,346 noticeboards and offers a keyed HTTP API
(https://github.com/edesky/edesky_api — apiary.apib and documents.xsd, the
only specification; the site's own /api page sits behind an Anubis
proof-of-work gate and its 2025-11-15 Wayback copy says the same thing):

  GET https://edesky.cz/api/v1/documents
      ?api_key=…            the key, a QUERY parameter (the API's design)
      &keywords=záměr       REQUIRED; there is NO document-category filter
      &search_with=sql      sql = keyword in the document NAME; es = fulltext
      &created_from=DATE    documents LOADED by eDesky after this date
      &include_texts=1      the OCR/extracted text of each attachment
      &order=date&page=N    200 documents a page; meta carries total_pages

The body is XML: <edesky_search_api><meta>…</meta><documents><document …
attributes …><attachments><attachment …>PERCENT-ENCODED TEXT</attachment>.
The percent-encoding is measured on the published 2015 sample
(gist aufi/e077f6a308840347fc4a): `Zmmeo%20me%C4%8D%2Fa…`, `%0A` newlines.
`created_at` is when eDesky loaded the document, not the desk's own posting
date — the two are usually the same day. `dashboard_ovm_ico` is declared
xs:int, so IČO leading zeros are gone ("245895" is Horní Planá's 00245895);
it is zero-padded back to eight digits here.

THE ONLY CATEGORY THE API HAS IS THE DESK'S. `dashboard_category` is
`samosprava` | `instituce` — the publisher's kind, not the document's — and
that is what the payload's `category` field carries. The document kind is
read off the title, below.

WHAT `záměr` MEANS ON A NOTICEBOARD, AND WHY THE TITLE IS FILTERED BOTH WAYS
============================================================================
§39 of the municipalities act (128/2000 Sb.) REQUIRES a municipality to
publish its intention to SELL, EXCHANGE, DONATE, LEASE OUT, LET or LEND its
real property — the disposal side. There is no such duty for buying. So the
bulk of `záměr` documents are the municipality OFFERING an asset, which is
the opposite of an ask, and two other families share the word: EIA notices
("oznámení záměru", a private developer's project the office must post) and
permit proceedings (územní/stavební řízení on somebody else's stavba). All
three are dropped BY THE TITLE and counted by reason; what is kept is a title
carrying `záměr` and an acquiring verb — pořídit · koupit / nakoupit / odkup /
výkup · pronajmout · zadat · realizovat. Direction is the caveat: "záměr
pronajmout" is kept as instructed, but on a noticeboard it is more often the
desk LETTING its own space than renting somebody else's; every kept row
carries `intent` (the verb that admitted it) so the ratio is measurable on
the first real run, never assumed.

WHAT IS CUT, AND WHY IT IS AN ALLOWLIST
=======================================
Two layers, both fail-closed:

  1. THE BODY ECHOES THE KEY AND THE REGISTRANT. <meta> carries
     <user>registrant@…</user> and <requested_params>{… "api_key"=>"…" …}
     (measured on the 2015 sample). The fetcher stores every body under
     .fetch/ as MODE-A evidence, so `redact()` blanks both elements and any
     `api_key=` value BEFORE a byte is stored — always, even for a body the
     guard then refuses. The un-redacted download is truncated by the fetcher
     the moment the guard returns.
  2. DOC_FIELDS is an ALLOWLIST over the <document> attributes; nothing else
     is read. Attachment `url` is an /attachments/ path robots.txt disallows,
     and edesky_text_url / ovm_zkratka / ruian_kod are not needed. The
     attachment TEXT is OCR of a letterhead document: it carries the desk's
     switchboard and mailbox in the first lines, and sometimes a clerk's.
     `cut_contacts()` drops every LINE or sentence carrying an email or phone
     with normalize.py's own two patterns (copied, not imported — normalize
     imports this file and an import back would close a cycle). Lines, not
     only sentences: OCR letterheads rarely end in a full stop.

THE OWNER IS THE DESK, OR THERE IS NO RECORD
============================================
`dashboard_name` is the institution whose noticeboard carried the document.
It is the `owner` — the fact this ledger exists for (CONVENTIONS.md: REQUIRED
on every `asks` record, gated in db.py check_owner()). No fallback to
"eDesky": the aggregator is not the asker.

THE TERMS, STATED
=================
edesky.cz/vop (Wayback 2026-06-11), which the sign-up form makes the
registrant accept: VI.1 forbids passing data obtained from the service to
third parties and VI.4(e) forbids publishing it in any form, VI.5 attaches a
100,000 CZK penalty per breach, VI.6 reserves covert watermarking. A public
register is publication. The fetcher therefore refuses to write into
data/raw/ until data/feeds.json records `access.verdict: allowed` on the
strength of the provider's WRITTEN consent (VI.4 names written permission as
the route); a private measurement run into a scratch directory is VI.1
own-use and is allowed. See scripts/fetch_edesky.sh, header.

Signature and return shape of extract_edesky() are normalize.py's, not ours.
"""
import argparse
import json
import os
import re
import sys
import unicodedata
from urllib.parse import unquote
from xml.etree import ElementTree as ET

# ── the surface's own constants ────────────────────────────────────────────
DOC_URL = "https://edesky.cz/dokument/{id}"
ROOT_TAG = "edesky_search_api"
PAGE_SIZE = 200          # apiary.apib: "každá stránka má 200 dokumentů"

# Under this many characters after the contact cut, the attachment text is a
# label or a scan nobody OCR'd, not a need a builder could start on. The same
# bar nen_ptk_extract.MIN_POPIS and hack_extract.MIN_STATEMENT set, for the
# same reason; independent bars, not a shared constant.
MIN_TEXT = 80
MAX_TEXT = 1500

# THE ALLOWLIST over <document> attributes. Adding one is a deliberate act;
# eDesky adding one is not. `edesky_id` is absent on the 2015 sample and
# present since 2017 (repo issue #3); the trailing number of edesky_url is
# the fallback identity.
DOC_FIELDS = (
    "edesky_id", "name", "created_at",
    "dashboard_id", "dashboard_name", "dashboard_ovm_ico", "dashboard_category",
    "edesky_url", "orig_url",
)

# Drop reasons. Strings, because the fetcher prints them and the summary
# counts per reason — a bare total would say "most vanished" and not why.
NO_ZAMER = "no-zamer"                 # the title does not carry záměr at all
DISPOSAL = "disposal"                 # §39: sell / exchange / donate / let / lend
EIA_NOTICE = "eia-notice"             # a developer's project the office posted
PROCEEDINGS = "proceedings"           # a permit proceeding on somebody's stavba
NO_ACQUIRE = "no-acquire-intent"      # záměr, but no acquiring verb
NO_ID = "no-id"
NO_TITLE = "no-title"
NO_OWNER = "no-owner"
NO_TEXT = "no-text"                   # no OCR text at all (contains_text=0)
NO_STATED_NEED = "no-stated-need"     # text under MIN_TEXT after the cut

# AC-GDPR1's two patterns, verbatim from scripts/normalize.py.
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)

_WS = re.compile(r"\s+")
# A fragment is a LINE or a sentence — see the header.
_FRAG = re.compile(r"\n+|(?<=[.!?…])\s+")
_ISO_DT = re.compile(r"^(\d{4}-\d{2}-\d{2})")
_TRAILING_INT = re.compile(r"(\d+)/?$")

# Redaction of the body BEFORE it is stored. Regex on the raw text, not on
# the parsed tree, so a body that does not parse is redacted all the same.
_USER_RE = re.compile(r"<user>.*?</user>", re.S)
_PARAMS_RE = re.compile(r"<requested_params>.*?</requested_params>", re.S)
_KEY_RE = re.compile(r"(api_key[\"']?\s*(?:=>|=|:)\s*[\"']?)[^&\"'\s<]+", re.I)
REDACTED = "[redacted]"

# ── the title rules, on diacritic-folded lowercase ─────────────────────────
# Folded so "Zamer obce prodat" (a desk that types without háčky) matches the
# same rule as "Záměr obce prodat". Patterns are written folded.
ZAMER_RE = re.compile(r"\bzamer")
DISPOSAL_RE = re.compile(
    r"\b(?:od)?prod[ae]"                        # prodat, prodej, odprodej
    r"|\bsmen"                                   # směna, směnit
    r"|\bdarov|\bdar\b|\bdaru\b|\bdarem\b"       # darování, dar
    r"|\bvypujc"                                 # výpůjčka, vypůjčit
    r"|\b(?:pro)?pacht"                          # pacht, propachtovat
    r"|\bvecn\w*\s+bremen|\bsluzebnost"          # věcné břemeno, služebnost
    r"|\bbezuplatn"                              # bezúplatný převod
    r"|\b(?:pro)?naj\w*\W+(?:\w+\W+){0,2}byt"    # pronajmout (obecní) byt, nájem bytu
    r"|\bbytov\w*\s+jednot"                      # bytová jednotka
)
EIA_RE = re.compile(
    r"\beia\b|posuzovan\w*\s+vliv|zjistovac\w*\s+rizen|vliv\w*\s+na\s+zivotni\s+prostred")
PROCEEDINGS_RE = re.compile(
    r"\buzemni\w*\s+rizen|\bstavebn\w*\s+rizen|\bstavebn\w*\s+povolen"
    r"|\bspolecn\w*\s+rizen|\bverejn\w*\s+vyhlask|\bkolaudac")
# The acquiring verbs, in the task's own list, each with the label the row
# carries as `intent`. Ordered; first match names the row.
KEEP = (
    ("pořídit", re.compile(r"\bpori[dz]")),
    ("koupit", re.compile(r"\bkoup|\bnakup|\bnakoup|\bodkup|\bodkoup|\bvykup|\bvykoup")),
    ("pronajmout", re.compile(r"\bpronaj")),
    ("zadat", re.compile(r"\bzada[tn]")),
    ("realizovat", re.compile(r"\brealiz")),
)


class ContractViolation(Exception):
    """A 200 whose body is not the surface we asked for (MODE A)."""


# --------------------------------------------------------------------------
# text
# --------------------------------------------------------------------------

def collapse(s):
    return _WS.sub(" ", str(s or "")).replace("\xa0", " ").strip()


def fold_ascii(s):
    s = unicodedata.normalize("NFKD", str(s or ""))
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def cut_contacts(text):
    """Drop every LINE or sentence carrying an email or phone, then collapse.
    Runs on the decoded text with its newlines still in it — an OCR'd
    letterhead is lines, not sentences."""
    keep = [p for p in _FRAG.split(str(text or "").replace("\xa0", " "))
            if p and not (EMAIL_RE.search(p) or PHONE_RE.search(p))]
    return collapse(" ".join(keep))


def scrub_line(s):
    """A one-line field (the title): the contact is removed, the line stays."""
    return collapse(PHONE_RE.sub(" ", EMAIL_RE.sub(" ", str(s or ""))))


def iso_day(s):
    """'2026-08-28 09:12:31 +0200' -> '2026-08-28'; anything else -> ''."""
    m = _ISO_DT.match(collapse(s))
    return m.group(1) if m else ""


def cap(text, n):
    """<= n chars, preferably at a sentence end — a need cut mid-clause reads
    as a different claim from the one the desk made."""
    if len(text) <= n:
        return text
    cut = text[:n]
    i = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
    return (cut[:i + 1] if i > n // 2 else cut.rsplit(" ", 1)[0]).strip()


def pad_ico(s):
    """xs:int stripped the leading zeros off an 8-digit IČO; put them back.
    Anything that is not 1–8 digits is not an IČO and becomes ''."""
    s = collapse(s)
    return s.zfill(8) if s.isdigit() and len(s) <= 8 else ""


def doc_url(doc_id):
    return DOC_URL.format(id=doc_id)


def classify_title(title):
    """(intent, None) when the title carries an intention to acquire;
    (None, reason) otherwise. Drop rules run BEFORE keep rules, so a title
    naming both a sale and a purchase is a disposal."""
    t = fold_ascii(collapse(title))
    if not ZAMER_RE.search(t):
        return None, NO_ZAMER
    if DISPOSAL_RE.search(t):
        return None, DISPOSAL
    if EIA_RE.search(t):
        return None, EIA_NOTICE
    if PROCEEDINGS_RE.search(t):
        return None, PROCEEDINGS
    for label, rx in KEEP:
        if rx.search(t):
            return label, None
    return None, NO_ACQUIRE


# --------------------------------------------------------------------------
# the body — redaction first, MODE-A guard second
# --------------------------------------------------------------------------

def _read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def redact(text):
    """The stored form of a body: registrant and key blanked, whatever the
    body turns out to be."""
    text = _USER_RE.sub("<user>%s</user>" % REDACTED, text)
    text = _PARAMS_RE.sub("<requested_params>%s</requested_params>" % REDACTED, text)
    return _KEY_RE.sub(r"\g<1>" + REDACTED, text)


def _int(s, default=None):
    s = collapse(s)
    return int(s) if s.isdigit() else default


def guard_page(data):
    """Refuse a 200 whose body is not an eDesky documents page.
    `data` is bytes. Returns (root, meta) with meta = {page, total_pages,
    count, total}: `count` is what LANDED (document elements on the page),
    `total` what the API says exists — kept apart on purpose."""
    head = collapse(data[:200].decode("utf-8", "replace"))
    if not data.strip():
        raise ContractViolation("empty body")
    low = head.lower()
    if low.startswith("<!doctype html") or low.startswith("<html"):
        raise ContractViolation(f"HTML, not the API (starts {head[:80]!r})")
    if low.startswith("{") or low.startswith("["):
        raise ContractViolation(f"JSON, not XML (starts {head[:80]!r})")
    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        raise ContractViolation(f"does not parse as XML ({e}; starts {head[:80]!r})")
    if root.tag != ROOT_TAG:
        raise ContractViolation(f"root is <{root.tag}>, not <{ROOT_TAG}>")
    docs = root.find("documents")
    if docs is None:
        raise ContractViolation("no <documents> element in the body")
    meta = root.find("meta")
    count_el = meta.find("documents_count") if meta is not None else None
    page_el = meta.find("page") if meta is not None else None
    count = len(docs.findall("document"))
    total = _int(count_el.get("total") if count_el is not None else None)
    if total is None:
        total = _int(count_el.text if count_el is not None else None, count)
    return root, {
        "page": _int(page_el.text if page_el is not None else None, 1),
        "total_pages": _int(page_el.get("total_pages") if page_el is not None else None, 1),
        "count": count,
        "total": max(total, count),
    }


def guard_file(path):
    return guard_page(_read_bytes(path))


# --------------------------------------------------------------------------
# the payload row
# --------------------------------------------------------------------------

def _texts_of(doc):
    """Every attachment's text, percent-decoded, in order. An attachment
    with contains_text=0 contributes nothing — a scan nobody OCR'd."""
    out = []
    for att in doc.findall("attachments/attachment"):
        if collapse(att.get("contains_text")) in ("0", "false"):
            continue
        out.append(unquote((att.text or "").strip()))
    return "\n".join(t for t in out if t)


def row_from_document(doc):
    """One <document> element -> (row, drop_reason). Exactly one is None."""
    a = {k: doc.get(k) for k in DOC_FIELDS}
    doc_id = collapse(a.get("edesky_id"))
    if not doc_id.isdigit():
        m = _TRAILING_INT.search(collapse(a.get("edesky_url")))
        doc_id = m.group(1) if m else ""
    if not doc_id:
        return None, NO_ID
    title = scrub_line(a.get("name"))
    if not title:
        return None, NO_TITLE
    owner = scrub_line(a.get("dashboard_name"))
    if not owner:
        return None, NO_OWNER
    intent, why = classify_title(title)
    if why:
        return None, why
    raw_text = _texts_of(doc)
    if not raw_text.strip():
        return None, NO_TEXT
    text = cut_contacts(raw_text)
    if len(text) < MIN_TEXT:
        return None, NO_STATED_NEED
    return {
        "id": doc_id,
        "title": title,
        "municipality": owner,
        "ico": pad_ico(a.get("dashboard_ovm_ico")),
        "category": collapse(a.get("dashboard_category")),
        "dashboard_id": collapse(a.get("dashboard_id")),
        "url": collapse(a.get("edesky_url")) or doc_url(doc_id),
        "orig_url": collapse(a.get("orig_url")),
        "date": iso_day(a.get("created_at")),
        "intent": intent,
        "text": cap(text, MAX_TEXT),
    }, None


def fold(paths, out_path):
    """Every guarded (and already redacted) page body -> one
    edesky-zamery.jsonl. Returns the counts the fetcher prints. Deduped on
    `id`: a document can sit on two pages when the set shifts between
    requests. A body that fails its guard is a CONTRACT VIOLATION and stops
    the fold — the fetcher never hands one over."""
    rows, drops, seen, documents = {}, {}, [], 0
    for p in paths:
        root, _meta = guard_file(p)
        for doc in root.find("documents").findall("document"):
            documents += 1
            row, why = row_from_document(doc)
            if row is None:
                key = collapse(doc.get("edesky_id")) or collapse(doc.get("edesky_url")) \
                    or f"{os.path.basename(p)}#{documents}"
                drops[key] = why
                continue
            seen.append(row["id"])
            rows[row["id"]] = row
    ordered = sorted(rows.values(), key=lambda r: (r["date"], int(r["id"])), reverse=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        for r in ordered:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    by_reason, by_intent = {}, {}
    for why in drops.values():
        by_reason[why] = by_reason.get(why, 0) + 1
    for r in ordered:
        by_intent[r["intent"]] = by_intent.get(r["intent"], 0) + 1
    detail = sorted(f"{k}: {v}" for k, v in drops.items())
    return {
        "pages": len(paths),
        "documents": documents,
        "kept": len(ordered),
        "duplicates": len(seen) - len(rows),
        "dropped": len(drops),
        "dropped_by_reason": by_reason,
        "dropped_detail": detail[:60] + ([f"… {len(detail) - 60} more"] if len(detail) > 60 else []),
        "kept_by_intent": by_intent,
        "owners": len({r["municipality"] for r in ordered}),
        "no_ico": sum(1 for r in ordered if not r["ico"]),
    }


# --------------------------------------------------------------------------
# the normalize.py extractor
# --------------------------------------------------------------------------

def extract_edesky(item, payload_key, today):
    """One payload row -> one asks record, or None when the row names no
    desk, carries no acquiring intention, or states no need. Shape is
    extract_nku's, plus the top-level `owner`."""
    doc_id = collapse(item.get("id"))
    title = collapse(item.get("title"))
    owner = collapse(item.get("municipality"))
    url = collapse(item.get("url")) or (doc_url(doc_id) if doc_id else "")
    # The owner gate, restated against the payload FILE rather than the page:
    # data/raw is writable and a row is not a page. CONVENTIONS.md makes
    # `owner` required on every asks record and db.py check_owner() refuses
    # one without it — better to stage nothing than a record the ledger will
    # red-build on.
    if not doc_id.isdigit() or not title or not owner or not url:
        return None
    intent, why = classify_title(title)
    if why:
        return None
    text = collapse(item.get("text"))
    if len(text) < MIN_TEXT:
        return None
    return {
        "id": "edesky-" + doc_id,
        "source": "edesky",
        "evidence_type": "asks",
        "url": url,
        "date": iso_day(item.get("date")) or today.isoformat(),
        "title_native": title,
        "entity_native": owner,
        # WHO ASKED, as the top-level schema'd field the ledger keeps and
        # db.py gates. `entity_native` is a staging field the append
        # allowlist drops, so this is the only copy that reaches a page.
        "owner": owner,
        "sector": None,
        # No money staged. A záměr sometimes names a sum in its OCR text, but
        # reading crowns out of free text is the model pass's judgment, not a
        # mechanical field — and a stated ceiling is not a budget line.
        "money_eur": None,
        "money_note": "",
        # A NOTICEBOARD POSTING WINDOW IS NOT URGENCY. Owner ruling 2026-09-03,
        # the one tacr, hackathon and nen-ptk carry: the 15-day display period
        # is logistics, not a deadline the world imposes on the PROBLEM.
        # Materiality for asks is decided by scale, in normalize.py.
        "urgency_date": None,
        "quote_parts": [p for p in (title, text[:200]) if p],
        "excerpt": collapse(f"{title} — {owner}: {text}")[:400],
    }


# --------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("guard", help="redact the body (ALWAYS, when --redact-to is "
                                     "given), then MODE-A: refuse a 200 that is not a "
                                     "documents page; prints "
                                     "'<page>\\t<total_pages>\\t<count>\\t<total>'")
    g.add_argument("path")
    g.add_argument("--redact-to", default=None,
                   help="where the stored (registrant- and key-free) copy goes")
    f = sub.add_parser("fold", help="guarded page bodies -> one edesky-zamery.jsonl; "
                                    "prints a JSON summary")
    f.add_argument("--out", required=True)
    f.add_argument("--paths-from", default=None,
                   help="file of page-body paths, one per line — how the fetcher "
                        "passes them, so a path with a space in it survives the shell")
    f.add_argument("paths", nargs="*")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "guard":
            data = _read_bytes(a.path)
            if a.redact_to:
                # Before the guard, unconditionally: a refused body is stored
                # as evidence too, and evidence must not carry the key.
                with open(a.redact_to, "w", encoding="utf-8") as fh:
                    fh.write(redact(data.decode("utf-8", "replace")))
            _root, m = guard_page(data)
            print(f"{m['page']}\t{m['total_pages']}\t{m['count']}\t{m['total']}")
            return 0
        paths = list(a.paths)
        if a.paths_from:
            with open(a.paths_from, encoding="utf-8") as fh:
                paths += [ln.rstrip("\n") for ln in fh if ln.strip()]
        print(json.dumps(fold(paths, a.out), ensure_ascii=False))
        return 0
    except ContractViolation as e:
        print(f"CONTRACT VIOLATION: {e}")
        return 65


if __name__ == "__main__":
    sys.exit(main())
