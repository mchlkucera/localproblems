#!/usr/bin/env python3
"""
tacr_extract.py — the TA ČR payload reader, and the normalize.py extractor for it.

WHAT ONE RECORD IS
==================
TA ČR's BETA2/BETA3 programmes buy applied research for ministries. Before a
need is tendered, TA ČR posts a public consultation — "Konzultace k možnostem
řešení výzkumné potřeby: TTMD0001 …" — naming the resort and the meeting date.
That post is an ASK in the sense of
docs/superpowers/specs/2026-09-03-asks-ledger-design.md: a named owner, a
stated problem, no money attached yet. One record = one need code.

TWO SURFACES, ONE READER (measured 2026-09-03)
==============================================
  RSS   https://tacr.gov.cz/kategorie/beta{3,2}/feed/  200, application/rss+xml,
        content:encoded carries the full post body; WordPress caps a feed at
        10 posts. PRIMARY — a declared interface.
  HTML  https://tacr.gov.cz/kategorie/beta{3,2}/       200, one div.posts__item
        per post with a date and a truncated excerpt, 5 posts per page, no
        pagination (/page/2/ is 404). BACKFILL — it cannot carry more than the
        feed does; it exists for the day the feed breaks, not for reach.

"TT-CODED" IS HALF RIGHT
========================
The design spec says needs are TT…-coded. Measured on the live feeds: the five
BETA3 needs are TT-coded (TTMD0001, TTMZP0002, TTXMSMT502, TTMV0001, TTMPO0001)
and all nine BETA2 needs are TI-coded (TITXMPO140, TIMD0028, TIERU0015,
TIRXMD041, TIRXMSMT015, …) — 0 of 10 BETA2 posts match a TT-only pattern. A
TT-only rule would fetch the BETA2 surface and drop it by construction. The
second letter is the programme (TI = BETA2, TT = BETA3), so DEFAULT_NEED_RE
takes both; fetch_tacr.sh passes TACR_NEED_RE through when the owner wants it
narrower.

WHAT IS CUT AT THE FETCHER
==========================
One live BETA2 post carries a work mailbox in its body. The ledger's AC-GDPR1
gate refuses any record carrying an email or phone, so the sentence carrying
one is cut HERE, with the two patterns normalize.py uses. They are copied, not
imported: normalize.py imports this file, and an import back would close a
cycle (the mpsv_extract precedent). tacr_contract_selftest.py checks the copies
still match.

`ministry` is what the post names, in nominative. BETA3 posts write "resortu
Ministerstva dopravy"; BETA2 posts write "resortu MD". The abbreviation table
below is the fixed official one — a lookup, not a judgement — and anything it
does not know is kept verbatim ("Energetický regulační úřad"). A post naming no
resort gets "" and extract_tacr() falls back to TA ČR itself; it never decodes
the ministry from the need code, because then the field would carry two
provenances (MATCH.md §0).

Signature and return shape of extract_tacr() are normalize.py's, not ours.
"""
import argparse
import html
import json
import re
import sys
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree as ET

DEFAULT_NEED_RE = r"\bT[IT][A-Z]{2,8}\d{3,4}\b"
# What the RSS channel's own <link> must carry: the right site AND a BETA
# category. A redirect to the whole-site feed would still be tacr.gov.cz.
SOURCE_HOST = "tacr.gov.cz/kategorie/beta"
FALLBACK_ENTITY = "Technologická agentura ČR"

_CONTENT = "{http://purl.org/rss/1.0/modules/content/}encoded"
_WS = re.compile(r"\s+")
_TAG = re.compile(r"<[^>]+>")
# WordPress appends "The post <a>…</a> appeared first on <a>…</a>." to every
# feed body. Syndication furniture, not the post.
_TRAILER = re.compile(r"\s*The post\b.*?\bappeared first on\b.*$", re.S)

# AC-GDPR1's two patterns, verbatim from scripts/normalize.py.
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)

_UP = "A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ"
_LO = "a-záčďéěíňóřšťúůýž"
# A ministry name is a run of lowercase words after the stem; it ends at the
# first preposition that opens the next clause ("… tělovýchovy K výzkumné
# potřebě"). `pro` is not a stop: "Ministerstvo pro místní rozvoj".
_STOP = {"k", "ke", "na", "v", "ve", "o", "s", "se", "z", "ze", "do", "od", "při",
         "za", "dne", "je", "bude", "byl", "byla", "bylo", "která", "který", "které"}
_WORD = re.compile(r"\s*([" + _LO + r"]+)(,?)")
_MIN = re.compile(r"\bMinisterstv(?:o|a|em|u)\b")
_RESORT_ABBR = {
    "MD": "Ministerstvo dopravy", "MF": "Ministerstvo financí",
    "MK": "Ministerstvo kultury", "MMR": "Ministerstvo pro místní rozvoj",
    "MO": "Ministerstvo obrany", "MPO": "Ministerstvo průmyslu a obchodu",
    "MPSV": "Ministerstvo práce a sociálních věcí", "MSP": "Ministerstvo spravedlnosti",
    "MŠMT": "Ministerstvo školství, mládeže a tělovýchovy", "MV": "Ministerstvo vnitra",
    "MZ": "Ministerstvo zdravotnictví", "MZD": "Ministerstvo zdravotnictví",
    "MZE": "Ministerstvo zemědělství", "MZV": "Ministerstvo zahraničních věcí",
    "MŽP": "Ministerstvo životního prostředí", "ÚV": "Úřad vlády ČR",
}

_MONTHS = {"ledna": 1, "února": 2, "března": 3, "dubna": 4, "května": 5, "června": 6,
           "července": 7, "srpna": 8, "září": 9, "října": 10, "listopadu": 11,
           "prosince": 12}
_DATE = (r"(\d{1,2})\.\s*(\d{1,2}\.|ledna|února|března|dubna|května|června|července"
         r"|srpna|září|října|listopadu|prosince)\s*(\d{4})")
# "Dne 17. 12. 2025 od 10:00 hodin se uskuteční setkání…" is the announcement
# form. A lowercase "dne" is accepted only with a clock time after it: that is
# still a scheduled meeting ("informuje, že dne 29. června 2022 od 13:00"),
# while "Aktualizováno dne 17. 3. 2026" is an edit stamp and stays out.
_DNE_CAP = re.compile(r"\bDne\s+" + _DATE)
_DNE_LOW = re.compile(r"\bdne\s+" + _DATE + r"\s+od\s+\d{1,2}[:.]\d{2}")
_CZ_DATE = re.compile(r"^\s*(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})")

# Openers WordPress authors use for the need's name: „ “ " ,, '' ‚ ‘
_QUOTES = "„“\"'‚‘,"
_PREFIX = re.compile(
    r"^(?:důležité sdělení\b.*?:\s*"
    r"|(?:předběžná tržní )?konzultace k (?:možnostem řešení )?(?:výzkumné )?potřeby:?\s*"
    r"|předběžná tržní konzultace k projektu:?\s*)+",
    re.I)


class ContractViolation(Exception):
    """A 200 whose body is not the surface we asked for (MODE A)."""


# --------------------------------------------------------------------------
# text
# --------------------------------------------------------------------------

def collapse(s):
    return _WS.sub(" ", str(s or "")).strip()


def clean_text(s):
    """HTML -> whitespace-collapsed text, entities decoded, feed trailer gone."""
    s = _TAG.sub(" ", s or "")
    s = html.unescape(s).replace("\xa0", " ")
    s = _TRAILER.sub("", s)
    return collapse(s)


_SENT = re.compile(r"(?<=[.!?…])\s+")


def cut_contacts(text):
    """Drop every sentence carrying an email or phone. The text is already
    collapsed, so re-joining on one space is lossless for what is kept."""
    return " ".join(p for p in _SENT.split(text)
                    if not (EMAIL_RE.search(p) or PHONE_RE.search(p)))


def iso_from_rfc2822(s):
    try:
        return parsedate_to_datetime((s or "").strip()).date().isoformat()
    except (TypeError, ValueError, IndexError):
        return ""


def iso_from_cz(s):
    m = _CZ_DATE.match(s or "")
    return f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}" if m else ""


def consultation_date(text):
    for rx in (_DNE_CAP, _DNE_LOW):
        for m in rx.finditer(text):
            # A date the post itself withdraws is not a date the world imposes.
            if "neuskuteční" in text[m.end():m.end() + 120]:
                continue
            mon = m.group(2).rstrip(".")
            mon = int(mon) if mon.isdigit() else _MONTHS[mon]
            return f"{m.group(3)}-{mon:02d}-{int(m.group(1)):02d}"
    return ""


def _lower_run(s):
    out, pos = [], 0
    while True:
        m = _WORD.match(s, pos)
        if not m or m.group(1) in _STOP:
            break
        out.append(m.group(1) + m.group(2))
        pos = m.end()
    run = " ".join(out).rstrip(",")
    return re.sub(r"\s+a$", "", run)


def ministry_of(text):
    """The resort the post names, nominative; "" when it names none."""
    m = re.search(r"\bresortu\s+", text)
    if m:
        rest = text[m.end():]
        mm = _MIN.match(rest)
        if mm:
            run = _lower_run(rest[mm.end():])
            if run:
                return "Ministerstvo " + run
        else:
            am = re.match(r"([" + _UP + r"]{2,4}[a-z]?)\b", rest)
            if am and am.group(1).upper() in _RESORT_ABBR:
                return _RESORT_ABBR[am.group(1).upper()]
            nm = re.match(r"([" + _UP + r"][" + _LO + r"]+)", rest)
            if nm:
                run = _lower_run(rest[nm.end():])
                return (nm.group(1) + (" " + run if run else "")).strip()
    mm = _MIN.search(text)
    if mm:
        run = _lower_run(text[mm.end():])
        if run:
            return "Ministerstvo " + run
    return ""


def _strip_name(s):
    s = s.strip(" \t:–-")
    s = re.sub(r"^s\s+názvem\s*", "", s)
    s = s.strip(" " + _QUOTES)
    return collapse(s.rstrip(" ." + _QUOTES))


def need_title(raw_title, need_id, body):
    """The need's own name. The code is its own field, so it leaves the title;
    so does every boilerplate prefix. When the title carries no code (a
    "Záměr zadání…" notice) the name is taken from `<code> s názvem „…“` in
    the body; the prefix-stripped title is the last resort."""
    t = collapse(raw_title)
    cands = []
    if need_id in t:
        cands.append(t.split(need_id, 1)[1])
    m = re.search(re.escape(need_id) + r"\s*(?:s\s+názvem)?\s*[" + re.escape(_QUOTES)
                  + r"]+\s*(.+?)\s*[“\"”]", body)
    if m:
        cands.append(m.group(1))
    cands.append(_PREFIX.sub("", t))
    for c in cands:
        c = _strip_name(c)
        if c:
            return c
    return t


def _row(need_re, title, link, date, body, iface):
    """One post -> one need row, or None when the post carries no need code."""
    title = collapse(title)
    m = need_re.search(title) or need_re.search(body)
    if not m or not link:
        return None
    nid = m.group(0).upper()
    body = cut_contacts(body)
    if len(body) > 2000:
        body = body[:2000].rsplit(" ", 1)[0]
    return {
        "need_id": nid,
        "title": need_title(title, nid, body),
        "link": link,
        "date": date,
        "ministry": ministry_of(body),
        "consultation_date": consultation_date(body),
        "body": body,
        "iface": iface,
    }


# --------------------------------------------------------------------------
# the two surfaces — MODE-A guard first, then the rows
# --------------------------------------------------------------------------

def _read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def guard_rss(path):
    """Refuse a 200 whose body is not one of TA ČR's BETA category feeds.
    Returns the <item> elements."""
    raw = _read_bytes(path)
    head = raw.lstrip(b"\xef\xbb\xbf \t\r\n")[:200]
    if not (head.startswith(b"<?xml") or head.startswith(b"<rss")):
        raise ContractViolation(
            f"body is not XML (starts {head[:60].decode('utf-8', 'replace')!r})")
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        raise ContractViolation(f"XML does not parse: {e}")
    ch = root.find("channel") if root.tag == "rss" else None
    if ch is None:
        raise ContractViolation("XML but not RSS 2.0 (no <rss><channel>)")
    link = (ch.findtext("link") or "").strip()
    if SOURCE_HOST not in link:
        raise ContractViolation(f"channel link is {link!r}, not a tacr.gov.cz BETA category")
    items = ch.findall("item")
    if not items:
        raise ContractViolation("well-formed feed, empty channel")
    return items


_ITEM = re.compile(r'<div class="posts__item">(.*?)(?=<div class="posts__item">|$)', re.S)
_A_TITLE = re.compile(r'<a class="posts__title" href="([^"]+)">(.*?)</a>', re.S)
_P_DATE = re.compile(r'<div class="posts__date">(.*?)</div>', re.S)
_P_EXCERPT = re.compile(r'class="posts__excerpt">(.*?)</div>\s*</div>', re.S)


def guard_listing(path):
    """Refuse a 200 whose body is not a category listing with posts in it.
    Returns the post chunks."""
    text = _read_bytes(path).decode("utf-8", "replace")
    if "posts__item" not in text:
        raise ContractViolation("HTML 200 but no posts__item loop in the body "
                                "(login page, error document, or empty category)")
    chunks = [c for c in _ITEM.findall(text) if _A_TITLE.search(c)]
    if not chunks:
        raise ContractViolation("posts__item present but no posts__title inside it")
    return chunks


def parse_rss(path, need_re):
    rows, dropped = [], {}
    items = guard_rss(path)
    for it in items:
        title = clean_text(it.findtext("title") or "")
        link = (it.findtext("link") or "").strip()
        body = clean_text(it.findtext(_CONTENT) or it.findtext("description") or "")
        r = _row(need_re, title, link, iso_from_rfc2822(it.findtext("pubDate")), body, "rss")
        if r:
            rows.append(r)
        else:
            dropped[link or title] = title
    return rows, len(items), dropped


def parse_listing(path, need_re):
    rows, dropped = [], {}
    chunks = guard_listing(path)
    for c in chunks:
        a = _A_TITLE.search(c)
        link, title = a.group(1).strip(), clean_text(a.group(2))
        d = _P_DATE.search(c)
        date = iso_from_cz(clean_text(d.group(1))) if d else ""
        e = _P_EXCERPT.search(c)
        body = clean_text(e.group(1)) if e else ""
        # The excerpt opens with the date and a dash the template puts there.
        body = re.sub(r"^\d{1,2}\.\s*\d{1,2}\.\s*\d{4}\s*[-–]\s*", "", body)
        r = _row(need_re, title, link, date, body, "html")
        if r:
            rows.append(r)
        else:
            dropped[link or title] = title
    return rows, len(chunks), dropped


def fold(rows):
    """Dedupe on need_id: the fuller body wins, the earliest date is kept, and
    an empty ministry/consultation_date/title is filled from the loser."""
    best = {}
    for r in rows:
        k = r["need_id"]
        cur = best.get(k)
        if cur is None:
            best[k] = dict(r)
            continue
        win, lose = (r, cur) if len(r.get("body", "")) > len(cur.get("body", "")) else (cur, r)
        merged = dict(win)
        dates = [d for d in (cur.get("date"), r.get("date")) if d]
        merged["date"] = min(dates) if dates else ""
        for f in ("ministry", "consultation_date", "title"):
            if not merged.get(f):
                merged[f] = lose.get(f, "")
        best[k] = merged
    return sorted(best.values(), key=lambda r: (r.get("date") or "", r["need_id"]),
                  reverse=True)


def read_sources(rss_paths, html_paths, out_path, need_re=None):
    """Every surface -> one tacr-needs.jsonl. Returns the counts the fetcher
    prints; raises ContractViolation on a body that fails its guard."""
    rx = re.compile(need_re or DEFAULT_NEED_RE)
    rows, dropped = [], {}
    seen = {"rss": 0, "html": 0}
    for p in rss_paths:
        r, n, d = parse_rss(p, rx)
        rows += r
        seen["rss"] += n
        dropped.update(d)
    for p in html_paths:
        r, n, d = parse_listing(p, rx)
        rows += r
        seen["html"] += n
        dropped.update(d)
    needs = fold(rows)
    with open(out_path, "w", encoding="utf-8") as fh:
        for r in needs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return {"rss_seen": seen["rss"], "html_seen": seen["html"],
            "candidates": len(rows), "needs": len(needs),
            "dropped": len(dropped), "dropped_titles": sorted(dropped.values())}


# --------------------------------------------------------------------------
# the normalize.py extractor
# --------------------------------------------------------------------------

def extract_tacr(item, payload_key, today):
    """One need -> one asks record. Shape is extract_nku's."""
    nid = collapse(item.get("need_id")).upper()
    title = collapse(item.get("title"))
    link = (item.get("link") or "").strip()
    if not nid or not title or not link:
        return None
    ministry = collapse(item.get("ministry")) or FALLBACK_ENTITY
    body = collapse(item.get("body"))
    # The consultation date is a real date the world imposes — score_urgency's
    # job, on the same reasoning ec-hys uses for a feedback deadline.
    cdate = (item.get("consultation_date") or "")[:10]
    return {
        "id": f"tacr-{nid.lower()}",
        "source": "tacr",
        "evidence_type": "asks",
        "url": link,
        "date": (item.get("date") or "") or today.isoformat(),
        "title_native": title,
        "entity_native": ministry,
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": cdate or None,
        "quote_parts": [p for p in (title, body[:200]) if p],
        "excerpt": collapse(f"{title} — {ministry}: {body}")[:400],
    }


# --------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("guard", help="MODE-A: refuse a 200 whose body is not the surface asked for; prints the post count")
    g.add_argument("kind", choices=("rss", "html"))
    g.add_argument("path")
    f = sub.add_parser("fold", help="RSS + listing bodies -> one tacr-needs.jsonl; prints a JSON summary")
    f.add_argument("--out", required=True)
    f.add_argument("--rss", nargs="*", default=[])
    f.add_argument("--html", nargs="*", default=[])
    f.add_argument("--need-re", default=None)
    a = ap.parse_args(argv)
    try:
        if a.cmd == "guard":
            print(len(guard_rss(a.path)) if a.kind == "rss" else len(guard_listing(a.path)))
            return 0
        print(json.dumps(read_sources(a.rss, a.html, a.out, a.need_re), ensure_ascii=False))
        return 0
    except ContractViolation as e:
        print(f"CONTRACT VIOLATION: {e}")
        return 65


if __name__ == "__main__":
    sys.exit(main())
