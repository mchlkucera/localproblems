#!/usr/bin/env python3
"""
hack_extract.py — the hackathon-challenge page parser, and the normalize.py
extractor for the `hackathon` feed (`asks` ledger, prefix `hack-`).

WHAT THIS FEED IS
=================
Six Czech hackathons publish challenges that a hospital, a city or a ministry
SET — a named institution stating a problem it wants solved, before any
procurement money exists. That statement and its owner are the record. Prizes,
team counts and winners are never staged; see
docs/superpowers/specs/2026-09-03-asks-ledger-design.md.

WHY ONE RULE TABLE AND NOT SIX PARSERS
======================================
All six pages reduce to the same walk: bound the section, then read title /
paragraph / owner-label elements in source order. Only the regexes and the
bounding markers differ, so a site is one row in SITES and the walker is
shared. A seventh site is a seventh row, not a seventh function.

MEASURED 2026-09-03 (browser-style UA; hackjakbrno 403s curl's default one):
  hackjakbrno   181 kB Elementor. <h2>Výzvy 2025</h2>, then 15 icon boxes of
                which 9 are challenges ("N. Title" + description) and 6 are
                prize boxes ("1. místo: 25 000 Kč") in the SAME markup after a
                "Hlavní ceny" heading. Every challenge box is followed by a
                heading "Zadavatel: <owner>" — the owner is explicit.
  rakathon      860 kB Squarespace. <h2>Výzvy</h2>, <h4>"Příklady výzev z
                minulého ročníku…", 4 × <h3> whose paragraph PRECEDES the
                heading in source order (grid layout). Hospitals appear only
                as logos and one prose sentence, never per challenge.
  upol          3.6 MB Elementor, base64 figma blobs inside span attributes.
                Two "letošní témata k řešení:" headings: the first sits in a
                container classed elementor-hidden-desktop/tablet/mobile and
                holds last year's topic lines (bare heading spans, no
                paragraph; "cena EnCLOD" prize badges; "Vlastní nápad" last);
                the second, visible, says "Právě pro vás vymýšlíme nová témata".
  idea13        171 kB WordPress/Elementor. 4 × <h3>"Výzva č. N: Title" + <p>.
  aimtec         69 kB. <p>"Do kterých výzev se hackeři v roce 2026 pustili?"
                then promo__col blocks of <h3> + first non-empty <p>; the list
                ends at promo__col--green (a "Technologie" CTA with two <h3>).
                No event date anywhere on the page.
  nakopniprahu   95 kB. <h2>VÝZVY NAKOPNI PRAHU 2026</h2>; 3 points-item (area
                <h3>) each holding 2 × <p><strong>sub-topic</strong></p> + <p>.
                Titles are split across inline spans ("Cirkul|á|r|ní město"),
                which is why strip_tags() deletes inline tags rather than
                replacing them with a space.

PERSONAL DATA
=============
Challenge pages name garants, mentors and contacts. cut_contacts() drops any
sentence carrying an email, a phone, or a Garant/Kontakt/Mentor label BEFORE
the text is staged; normalize.py's allowlist + EMAIL_RE/PHONE_RE gate then runs
unchanged on top. The two regexes are transcribed from normalize.py because
normalize imports this module and importing back would be circular.

CLI (driven by scripts/fetch_hackathons.sh):
    hack_extract.py sites               -> "key<TAB>url" per site, from SITES
    hack_extract.py guard KEY FILE      -> exit 0 = page we contracted for,
                                           exit 3 = MODE-A refused (reason on stdout)
    hack_extract.py parse KEY FILE      -> one JSON row per challenge on stdout
"""

import hashlib
import html
import json
import re
import sys

# --------------------------------------------------------------------------
# the rule table — one row per site
# --------------------------------------------------------------------------
# Every regex captures its payload in a group named `v`. Fields:
#   url / host / owner   page fetched, `site` staged, owner when the page names none
#   marker               MODE-A contract: a 200 whose body lacks it is not this page
#   start / end          the section; `end` is optional (to end of document)
#   title / para         the challenge name and its text, in source order
#   owner_label          an explicit per-challenge owner element (hackjakbrno)
#   area                 a grouping heading prefixed to the title (nakopniprahu)
#   para_before          the paragraph precedes its heading (rakathon)
#   drop_title           titles that share the markup but are not challenges
#   strip_title          an ordinal to remove so re-numbering keeps ids stable
#   owner_hints          (regex, owner) tried on the block text, first wins
#   edition_re           a year in the section heading; else the event year
#   prev_edition_re      the section is last year's — edition = event year − 1
#   date_re              where the event date is; default = first date in <body>
#   text_fallback_title  bare topic lines: text mirrors the title, never ""
MONTHS = ("ledna|února|března|dubna|května|června|července|srpna|září|října|"
          "listopadu|prosince")

SITES = {
    "hackjakbrno": dict(
        url="https://www.hackjakbrno.cz/", host="www.hackjakbrno.cz",
        owner="Hack jak Brno (FN Brno, FNUSA, MOÚ, JINAG)",
        marker=r"<h\d[^>]*>\s*V[ýy]zvy\s*20\d\d",
        start=r"<h\d[^>]*>\s*V[ýy]zvy\s*20\d\d", end=r"Hlavn[ií] ceny",
        title=r"<h\d[^>]*elementor-icon-box-title[^>]*>(?P<v>.*?)</h\d>",
        para=r"<p[^>]*elementor-icon-box-description[^>]*>(?P<v>.*?)</p>",
        # The label is a link inside the heading (<h6><a>Zadavatel: …</a></h6>),
        # so any run of inline open tags may sit before the word.
        owner_label=(r"<(?:h\d|span|p)[^>]*elementor-heading-title[^>]*>(?:\s*<[^>]+>)*\s*"
                     r"Zadavatel:\s*(?P<v>.*?)</(?:h\d|span|p)>"),
        drop_title=r"^\d+\.\s*m[íi]sto\b",
        strip_title=r"^\d+\.\s*",
        edition_re=r"V[ýy]zvy\s*(20\d\d)",
    ),
    "rakathon": dict(
        url="https://www.rakathon.cz/", host="www.rakathon.cz",
        owner="Rakathon (FN Motol, MOÚ, FN Ostrava)",
        # idea13 carries an identical bare <h2>Výzvy</h2>; the Squarespace text
        # block wrapping it is what makes the body THIS page (self-test: a
        # misrouted idea13 page must be refused here).
        marker=r"sqs-html-content[^>]*>\s*<h2[^>]*>\s*V[ýy]zvy\s*</h2>",
        start=r"sqs-html-content[^>]*>\s*<h2[^>]*>\s*V[ýy]zvy\s*</h2>", end=r"<h2[^>]*>\s*Ceny\s*</h2>",
        title=r"<h3[^>]*>(?P<v>.*?)</h3>",
        para=r"<p[^>]*>(?P<v>.*?)</p>",
        para_before=True,
        owner_hints=(
            (r"\bFN Motol\b", "FN Motol"),
            (r"Masaryk[ůu]v onkologick[ýy]|\bMO[UÚ]\b", "Masarykův onkologický ústav"),
            (r"FN Ostrava|Fakultn[ií] nemocnice Ostrava", "FN Ostrava"),
        ),
        prev_edition_re=r"minul[ée]ho ro[čc]n[ií]ku|lo[ňn]sk[ée]ho ro[čc]n[ií]ku",
    ),
    "upol": dict(
        url="https://hackathon.upol.cz/", host="hackathon.upol.cz",
        owner="Olomoucký kraj a město Olomouc",
        marker=r"leto[šs]n[ií] t[ée]mata k [řr]e[šs]en[ií]",
        start=r"<h\d[^>]*>\s*leto[šs]n[ií] t[ée]mata k [řr]e[šs]en[ií]",
        end=r"p[řr]i [řr]e[šs]en[ií] projekt[ůu] podporujeme|leto[šs]n[ií] t[ée]mata k [řr]e[šs]en[ií]|T[řr][ií]denn[ií] hackathon",
        # The widget wrapper, not the span: the span nests figma-blob spans,
        # so a non-greedy `<span>…</span>` would stop at the first nested close.
        title=(r"<div[^>]*elementor-widget-heading[^>]*>\s*"
               r"<span[^>]*elementor-heading-title[^>]*>(?P<v>.*?)</div>"),
        para=None,
        drop_title=r"^Vlastn[ií] n[áa]pad$|^cena EnCLOD$",
        strip_title=r"^cena EnCLOD\s*",
        prev_edition_re=r"elementor-hidden-desktop",
        text_fallback_title=True,
    ),
    "idea13": dict(
        url="https://www.idea13.cz/", host="www.idea13.cz",
        owner="MČ Praha 13",
        marker=r"V[ýy]zva\s*č\.\s*\d",
        start=r"<h2[^>]*>\s*V[ýy]zvy\s*</h2>", end=r"[ČC]ast[ée] dotazy",
        title=r"<h3[^>]*>(?P<v>.*?)</h3>",
        para=r"<p[^>]*>(?P<v>.*?)</p>",
        strip_title=r"^V[ýy]zva\s*č\.\s*\d+\s*:\s*",
    ),
    "aimtec": dict(
        url="https://www.aimtechackathon.cz/hackathon/", host="www.aimtechackathon.cz",
        owner="AimtecHackathon (Plzeň)",
        marker=r"Do kter[ýy]ch v[ýy]zev se hacke[řr]i v roce 20\d\d pustili",
        start=r"Do kter[ýy]ch v[ýy]zev se hacke[řr]i v roce 20\d\d pustili",
        end=r"promo__col--green",
        title=r"<h3[^>]*>(?P<v>.*?)</h3>",
        para=r"<p[^>]*>(?P<v>.*?)</p>",
        owner_hints=(
            (r"Astrum Mobility", "Astrum Mobility"),
            (r"m[ěe]sta Plzn[ěe]|m[ěe]sto Plze[ňn]|m[ěe]stsk[ýy]ch senzor", "město Plzeň"),
            (r"Ottobock", "Ottobock"),
        ),
        edition_re=r"v roce (20\d\d) pustili",
    ),
    "nakopniprahu": dict(
        url="https://www.nakopniprahu.cz/", host="www.nakopniprahu.cz",
        owner="Hlavní město Praha (MHMP, OICT)",
        marker=r"V[ÝY]ZVY NAKOPNI PRAHU\s*20\d\d",
        start=r"<h2[^>]*>\s*V[ÝY]ZVY NAKOPNI PRAHU\s*20\d\d", end=r"<h2[^>]*>\s*TIMELINE",
        area=r"<h3[^>]*points-item__title[^>]*>(?P<v>.*?)</h3>",
        title=r"<p>\s*<strong>(?P<v>.*?)</strong>\s*</p>",
        para=r"<p[^>]*>(?P<v>.*?)</p>",
        edition_re=r"NAKOPNI PRAHU\s*(20\d\d)",
        # The timeline lists registration and semifinal dates first; the
        # finále is the event a challenge is answered at.
        date_re=r"\d{1,2}\.\s*(?:" + MONTHS + r")\s*20\d\d(?=\s*Nakopni Fin[áa]le)",
    ),
}

# --------------------------------------------------------------------------
# text
# --------------------------------------------------------------------------
_WS = re.compile(r"\s+")
_BLOCK_CLOSE = re.compile(r"<(?:br|hr|/p|/div|/h[1-6]|/li|/tr|/td|/th|/section|/article|/table)\b[^>]*>", re.I)
_DROP_ELEMENTS = re.compile(r"<(script|style|noscript|svg|template)\b[^>]*>.*?</\1\s*>", re.S | re.I)


def collapse(s):
    return _WS.sub(" ", str(s or "")).strip()


def strip_tags(s):
    """HTML -> text. Block closers become newlines, inline tags vanish
    (nakopniprahu splits one word across spans), entities are decoded last so
    an encoded `&lt;` can never re-open a tag."""
    s = _DROP_ELEMENTS.sub(" ", s or "")
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = _BLOCK_CLOSE.sub("\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return s.replace("\xa0", " ").replace("\u200b", "").replace("\ufeff", "")


def sha1_8(s):
    return hashlib.sha1(str(s).encode("utf-8")).hexdigest()[:8]


# Transcribed from scripts/normalize.py EMAIL_RE / PHONE_RE — keep identical.
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)
# A contact label with a separator, or a capitalised label followed by what
# reads as a two-word name. "s podporou mentorů" mid-sentence is left alone.
CONTACT_LABEL_RE = re.compile(
    r"\b(?i:garant|kontakt|mentor)\w*\s*[:–—-]"
    r"|\b(?:Garant|Kontakt|Mentor)\w*\s+[A-ZÁ-Ž][a-zá-ž]+\s+[A-ZÁ-Ž]"
)
_SENTENCE = re.compile(r"(?<=[.!?…])\s+|\n+")


def is_contact(sentence):
    return bool(EMAIL_RE.search(sentence) or PHONE_RE.search(sentence)
                or CONTACT_LABEL_RE.search(sentence))


def cut_contacts(text):
    """Drop every sentence/line that carries contact data. Cutting the whole
    sentence, not the token, is deliberate: "Garant: Jan Novák" minus the email
    is still a name."""
    kept = [s for s in _SENTENCE.split(text or "") if s.strip() and not is_contact(s)]
    return collapse(" ".join(kept))


def cap(text, n):
    """≤ n chars, preferably at a sentence end."""
    if len(text) <= n:
        return text
    cut = text[:n]
    i = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
    return cut[:i + 1] if i > n // 2 else cut.rstrip() + "…"


# --------------------------------------------------------------------------
# dates — Czech, first match wins, a range yields its first day
# --------------------------------------------------------------------------
_MONTH_NO = {m: i + 1 for i, m in enumerate(MONTHS.split("|"))}
_RANGE = r"(?:[–—-]|až)"
CZ_DATE_RE = re.compile(
    r"(?P<d1>\d{1,2})\.\s*" + _RANGE + r"\s*\d{1,2}\.\s*(?P<m1>\d{1,2})\.\s*(?P<y1>20\d\d)"   # 18. - 19.9.2026
    r"|(?P<d2>\d{1,2})\.\s*" + _RANGE + r"\s*\d{1,2}\.\s*(?P<m2>" + MONTHS + r")\s*(?P<y2>20\d\d)"  # 16. až 18. října 2026
    r"|(?P<d3>\d{1,2})\.\s*(?P<m3>\d{1,2})\.\s*(?P<y3>20\d\d)"                                     # 27.5.2026
    r"|(?P<d4>\d{1,2})\.\s*(?P<m4>" + MONTHS + r")\s*(?P<y4>20\d\d)",                              # 27. května 2026
    re.I,
)


def cz_date_iso(text):
    m = CZ_DATE_RE.search(text or "")
    if not m:
        return ""
    for k in ("1", "2", "3", "4"):
        if m.group("d" + k):
            d, mo, y = m.group("d" + k), m.group("m" + k), m.group("y" + k)
            break
    mo = int(mo) if mo.isdigit() else _MONTH_NO.get(mo.lower(), 0)
    d = int(d)
    if not (1 <= mo <= 12 and 1 <= d <= 31):
        return ""
    return f"{y}-{mo:02d}-{d:02d}"


def event_date(rule, body):
    if rule.get("date_re"):
        m = re.search(rule["date_re"], strip_tags(body), re.I)
        return cz_date_iso(m.group(0)) if m else ""
    # Default: the first date the VISIBLE page states. <head> carries stale
    # og:descriptions (hackjakbrno's still says 2024), so the scan starts at <body>.
    i = body.find("<body")
    return cz_date_iso(strip_tags(body[i if i >= 0 else 0:]))


# --------------------------------------------------------------------------
# the guard and the walker
# --------------------------------------------------------------------------

def guard(key, body):
    """MODE-A. None when the body is the page we contracted for, else the
    reason. A login page, a maintenance notice or a redesign all arrive as a
    200 with bytes; only the section marker separates them from data."""
    rule = SITES[key]
    if not body or not body.strip():
        return "empty body"
    if not re.search(rule["marker"], body, re.S | re.I):
        return f"MODE-A: HTTP 200 but the section marker /{rule['marker']}/ is absent"
    return None


def _section(rule, body):
    m = re.search(rule["start"], body, re.S | re.I)
    if not m:
        return -1, ""
    a = m.end()
    if rule.get("end"):
        e = re.search(rule["end"], body[a:], re.S | re.I)
        if e:
            return m.start(), body[a:a + e.start()]
    return m.start(), body[a:]


def _tokens(rule, sec):
    toks = []
    for kind in ("area", "title", "para", "owner_label"):
        rx = rule.get(kind)
        if not rx:
            continue
        for m in re.finditer(rx, sec, re.S | re.I):
            toks.append((m.start(), m.end(), kind, m.group("v")))
    toks.sort(key=lambda t: (t[0], t[2] != "title"))
    # A paragraph that contains a title element IS that title's markup
    # (nakopniprahu's <p><strong>), not challenge text.
    starts = [t[0] for t in toks if t[2] == "title"]
    return [t for t in toks
            if not (t[2] == "para" and any(t[0] <= s < t[1] for s in starts))]


def _edition(rule, body, start_at, first_title_at, ev):
    if start_at < 0:
        return ""
    lo = max(0, start_at - 800)
    hi = first_title_at if first_title_at > start_at else start_at + 3000
    window = body[lo:hi]
    year = ""
    if rule.get("edition_re"):
        m = re.search(rule["edition_re"], window, re.S | re.I)
        year = m.group(1) if m else ""
    if not year and ev:
        year = ev[:4]
    if year and rule.get("prev_edition_re") and re.search(rule["prev_edition_re"], window, re.S | re.I):
        year = str(int(year) - 1)
    return year


def _owner(rule, block):
    if block["owners"]:
        return " / ".join(dict.fromkeys(block["owners"]))
    for rx, owner in rule.get("owner_hints") or ():
        if re.search(rx, block["title"] + " " + " ".join(block["paras"])):
            return owner
    return rule["owner"]


def parse_site(key, body):
    """The rows for one site's page, in page order. Empty when the section
    holds no challenge (UPOL between editions) — the caller reports that."""
    rule = SITES[key]
    start_at, sec = _section(rule, body)
    toks = _tokens(rule, sec)
    blocks, cur, pending, area = [], None, [], ""
    for s, e, kind, raw in toks:
        text = collapse(strip_tags(raw))
        if kind == "area":
            area = text[:1].upper() + text[1:].lower() if text else ""
            continue
        if kind == "title":
            if not text or (rule.get("drop_title") and re.search(rule["drop_title"], text, re.I)):
                cur = None            # a prize box: nothing after it attaches
                continue
            title = re.sub(rule["strip_title"], "", text).strip() if rule.get("strip_title") else text
            cur = {"title": title, "paras": pending if rule.get("para_before") else [],
                   "owners": [], "area": area, "at": s}
            pending = []
            blocks.append(cur)
        elif kind == "para":
            if not text:
                continue
            if rule.get("para_before"):
                pending = [text]      # nearest paragraph before the next heading
            elif cur is not None:
                cur["paras"].append(text)
        elif kind == "owner_label" and cur is not None and text:
            cur["owners"].append(text)

    ev = event_date(rule, body)
    first_at = -1
    if blocks:   # blocks[].at is relative to `sec`; map it back onto `body`
        first_at = re.search(rule["start"], body, re.S | re.I).end() + blocks[0]["at"]
    edition = _edition(rule, body, start_at, first_at, ev)

    rows = []
    for b in blocks:
        text = cap(cut_contacts(" ".join(b["paras"])), 1500)
        title = f"{b['area']} · {b['title']}" if b["area"] else b["title"]
        if not text and rule.get("text_fallback_title"):
            text = title
        if not text:
            continue
        rows.append({"site": rule["host"], "owner": _owner(rule, b), "page_url": rule["url"],
                     "title": title, "text": text, "event_date": ev, "edition": edition})
    return rows


# --------------------------------------------------------------------------
# the normalize.py extractor
# --------------------------------------------------------------------------

def extract_hack(item, payload_key, today):
    """Signature and return shape are normalize.py's (extract_nku), not ours.

    `date` is first-seen: the page carries no publication date and the id is
    sha1(site|title), stable across runs, so seen.txt dedupes re-fetches.
    `urgency_date` is the event date — the same reasoning as ec-hys: a real
    date the world imposes, which is what keeps a money-0 record material.
    """
    site = collapse(item.get("site"))
    title = collapse(item.get("title"))
    owner = collapse(item.get("owner"))
    url = (item.get("page_url") or "").strip()
    if not site or not title or not owner or not url:
        return None
    text = collapse(item.get("text"))
    quote = text[:200]
    if len(text) > 200 and " " in quote:
        quote = quote[:quote.rfind(" ")]
    return {
        "id": f"hack-{sha1_8(site + '|' + title)}",
        "source": "hackathon",
        "evidence_type": "asks",
        "url": url,
        "date": today.isoformat(),
        "title_native": title,
        "entity_native": owner,
        "sector": None,
        "money_eur": None,
        "money_note": "",
        "urgency_date": (item.get("event_date") or "").strip() or None,
        "quote_parts": [p for p in (title, quote) if p],
        "excerpt": collapse(f"{title} — {owner}: {text}")[:400],
        # WHO ASKED is the fact this ledger exists for, and `entity_native` is a
        # staging field the allowlist drops before append. `notes` is the one
        # allowlisted free-text receipt (ted carries its counterparties there),
        # so the owner rides on it and survives to the ledger.
        "notes": f"owner: {owner}",
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def main(argv):
    if len(argv) >= 1 and argv[0] == "sites":
        for key, rule in SITES.items():
            print(f"{key}\t{rule['url']}")
        return 0
    if len(argv) == 3 and argv[0] == "guard":
        reason = guard(argv[1], _read(argv[2]))
        print(reason or "ok")
        return 0 if reason is None else 3
    if len(argv) == 3 and argv[0] == "parse":
        for row in parse_site(argv[1], _read(argv[2])):
            print(json.dumps(row, ensure_ascii=False))
        return 0
    print(__doc__.split("CLI", 1)[1] if "CLI" in __doc__ else __doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
