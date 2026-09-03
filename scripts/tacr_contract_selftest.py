#!/usr/bin/env python3
"""
tacr_contract_selftest.py — proof that the `tacr` source contract rejects a
WRONG BODY, not just a bad status code, and that a right body yields the rows
the asks ledger expects.

Same doctrine as nen_sukl_coi_contract_selftest.py: a 200 carrying a login
page, a maintenance notice or an empty channel is bytes with a good transport
receipt, and the only thing separating it from data is a contract nobody has
watched fail. This file makes each guard fail on purpose, then feeds the good
bodies through the SAME entry points fetch_tacr.sh uses (tacr_extract.guard_*,
read_sources, extract_tacr) and checks what comes out.

Fixtures are embedded miniatures of the live surfaces measured 2026-09-03 —
one BETA3-style post, one BETA2-style post with a contact sentence, one
non-need notice — so the test runs offline.

    python3 scripts/tacr_contract_selftest.py

Exit 0 = every wrong body refused, every good body accepted, every extraction
assertion true.
"""
import datetime
import os
import re
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tacr_extract  # noqa: E402

# normalize.py's REQUIRED_OUT (scripts/normalize.py, "REQUIRED_OUT = (...)"),
# minus what the model fills: sector, geo_origin, title, summary, scores. Held
# as a literal so the test is self-contained; cross-checked against the live
# tuple below when normalize imports, so drift is a failure and not a surprise.
REQUIRED_OUT = ("id", "source", "url", "date", "title", "sector", "geo_origin",
                "money_eur", "money_note", "summary", "scores")
MODEL_FIELDS = ("sector", "geo_origin", "title", "summary", "scores")
MECHANICAL_KEYS = tuple(k for k in REQUIRED_OUT if k not in MODEL_FIELDS)
# The extract_nku shape this extractor mirrors.
SHAPE_KEYS = ("evidence_type", "title_native", "entity_native", "urgency_date",
              "quote_parts", "excerpt")
ID_RE = re.compile(r"^[a-z]{2,10}-[\w.-]+$")

LOGIN_HTML = (
    "<!DOCTYPE html><html lang=\"cs\"><head><title>Přihlášení</title></head>"
    "<body><h1>Přihlášení do systému</h1><form method=\"post\">"
    "<input name=\"username\"><input name=\"password\" type=\"password\">"
    "<button>Přihlásit</button></form></body></html>"
).encode("utf-8")

MAINTENANCE_HTML = (
    "<!DOCTYPE html><html><head><title>503 Service Unavailable</title></head>"
    "<body><h1>Probíhá plánovaná odstávka</h1></body></html>"
).encode("utf-8")

RSS_HEAD = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">'
    '<channel><title>Beta3 Archives - Technologická agentura ČR</title>'
    '<link>{link}</link><description>Podporujeme výzkum a inovace</description>'
)
RSS_TAIL = "</channel></rss>"

NEED_TTMD = """<item>
<title>Konzultace k možnostem řešení výzkumné potřeby: TTMD0001 Výzkum možností integrace ETCS do drážních vozidel</title>
<link>https://tacr.gov.cz/konzultace-k-moznostem-reseni-vyzkumne-potreby-ttmd0001/</link>
<pubDate>Thu, 21 Aug 2025 09:12:00 +0000</pubDate>
<content:encoded><![CDATA[
<p class="wp-block-paragraph">Dne 26. září 2025 od 10:00 hodin se uskuteční setkání s dodavateli a zástupci resortu Ministerstva dopravy k výzkumné potřebě <strong>TTMD0001</strong> s&nbsp;názvem „Výzkum možností integrace ETCS do drážních vozidel“.</p>
<p class="wp-block-paragraph"><strong>Cílem výzkumné potřeby je:</strong> ověřit, zda lze historická drážní vozidla vybavit ETCS bez ztráty jejich provozuschopnosti.</p>
<p>The post <a href="https://tacr.gov.cz/x/">Konzultace k možnostem řešení výzkumné potřeby: TTMD0001</a> appeared first on <a href="https://tacr.gov.cz">Technologická agentura ČR</a>.</p>
]]></content:encoded>
</item>"""

NEED_TIRX = """<item>
<title>Předběžná tržní konzultace k projektu: TIRXMSMT015 s názvem „Rámcová dohoda pro výzkum implementace strategických dokumentů vzdělávací politiky“</title>
<link>https://tacr.gov.cz/predbezna-trzni-konzultace-k-projektu-tirxmsmt015/</link>
<pubDate>Thu, 01 Oct 2020 08:00:00 +0000</pubDate>
<content:encoded><![CDATA[
<p>Dne 22. října 2020 od 10:00 hodin se formou videokonference uskuteční setkání s dodavateli a zástupci resortu MŠMT k projektu TIRXMSMT015 s názvem „Rámcová dohoda pro výzkum implementace strategických dokumentů vzdělávací politiky“.</p>
<p>Setkání je určeno především dodavatelům – možným řešitelům tohoto projektu. Dotazy zasílejte na dodatecne.informace.beta@tacr.cz nebo tel: +420 234 611 111. Registrace je otevřena do 20. října 2020.</p>
]]></content:encoded>
</item>"""

NON_NEED = """<item>
<title>Plánovaná odstávka systému ISTA, SISTA a ISRB</title>
<link>https://tacr.gov.cz/planovana-odstavka-systemu-ista-sista-a-isrb/</link>
<pubDate>Thu, 28 Mar 2024 10:00:00 +0000</pubDate>
<content:encoded><![CDATA[<p>TA ČR informuje uživatele ISTA, SISTA a ISRB, že dojde k plánované odstávce systémů v termínu 5. dubna 2024 od 9:00 do 17:00 hod.</p>]]></content:encoded>
</item>"""

GOOD_RSS = (RSS_HEAD.format(link="https://tacr.gov.cz/kategorie/beta3/")
            + NEED_TTMD + NEED_TIRX + NON_NEED + RSS_TAIL).encode("utf-8")
EMPTY_RSS = (RSS_HEAD.format(link="https://tacr.gov.cz/kategorie/beta3/") + RSS_TAIL).encode("utf-8")
WRONG_SITE_RSS = (RSS_HEAD.format(link="https://example.org/blog/") + NEED_TTMD + RSS_TAIL).encode("utf-8")

LISTING_HEAD = '<!DOCTYPE html><html lang="cs"><body><div class="posts">'
LISTING_TAIL = "</div></body></html>"


def listing_post(href, title, date, excerpt):
    return (
        '<div class="posts__item"><div class="posts__row"><div class="posts__left">'
        f'<a class="posts__title" href="{href}">{title}</a>'
        '<div class="posts__head"><div class="posts__badges">'
        '<a class="posts__badge" href="https://tacr.gov.cz/kategorie/beta3/">Beta3</a>'
        '</div></div><div class="posts__excerpt">'
        f'<div class="posts__date">{date}</div> - {excerpt}'
        '</div></div></div></div>'
    )


GOOD_LISTING = (LISTING_HEAD + listing_post(
    "https://tacr.gov.cz/konzultace-k-moznostem-reseni-vyzkumne-potreby-ttmd0001/",
    "Konzultace k možnostem řešení výzkumné potřeby: TTMD0001 Výzkum možností integrace ETCS do drážních vozidel",
    "20. 8. 2025",
    "Dne 26. září 2025 od 10:00 hodin se uskuteční setkání s dodavateli a zástupci resortu Ministerstva dopravy…",
) + listing_post(
    "https://tacr.gov.cz/konzultace-k-moznostem-reseni-vyzkumne-potreby-ttmv0001/",
    "Konzultace k možnostem řešení výzkumné potřeby: TTMV0001 Systém využívající AI pro měření výstrojních součástek",
    "30. 1. 2025",
    "Dne 17. února 2025 od 12:00 hodin se uskuteční setkání s dodavateli a zástupci resortu Ministerstva vnitra ČR k výzkumné potřebě TTMV0001…",
) + listing_post(
    "https://tacr.gov.cz/usneseni-predsednictva/",
    "Usnesení předsednictva TA ČR k situaci v rámci Programu BETA3",
    "17. 6. 2026",
    "Předsednictvo TA ČR reaguje na usnesení Rady pro výzkum, vývoj a inovace…",
) + LISTING_TAIL).encode("utf-8")

# WordPress renders an empty category with the page chrome and no loop.
NOTHING_FOUND = (LISTING_HEAD + '<p class="posts__empty">Nenalezeno.</p>' + LISTING_TAIL).encode("utf-8")


# --------------------------------------------------------------------------

def write(tmp, name, data):
    p = os.path.join(tmp, name)
    with open(p, "wb") as fh:
        fh.write(data)
    return p


def guard_cases(tmp):
    yield ("rss", "login page served as the feed", True, write(tmp, "rss-login.xml", LOGIN_HTML))
    yield ("rss", "maintenance notice served as the feed", True, write(tmp, "rss-503.xml", MAINTENANCE_HTML))
    yield ("rss", "well-formed RSS, EMPTY channel", True, write(tmp, "rss-empty.xml", EMPTY_RSS))
    yield ("rss", "well-formed RSS from another site (redirect)", True, write(tmp, "rss-wrong.xml", WRONG_SITE_RSS))
    yield ("rss", "THE GOOD BODY — two needs and one notice", False, write(tmp, "rss-good.xml", GOOD_RSS))
    yield ("html", "login page served as the listing", True, write(tmp, "list-login.html", LOGIN_HTML))
    yield ("html", "maintenance notice served as the listing", True, write(tmp, "list-503.html", MAINTENANCE_HTML))
    yield ("html", "page chrome, no posts loop (empty category)", True, write(tmp, "list-empty.html", NOTHING_FOUND))
    yield ("html", "THE GOOD BODY — three posts, two of them needs", False, write(tmp, "list-good.html", GOOD_LISTING))


def run_guard(kind, path):
    try:
        n = len(tacr_extract.guard_rss(path) if kind == "rss" else tacr_extract.guard_listing(path))
        return False, f"accepted, {n} posts"
    except tacr_extract.ContractViolation as e:
        return True, str(e)


def has_contact(obj):
    for s in (obj.values() if isinstance(obj, dict) else obj):
        if isinstance(s, (list, tuple)):
            if has_contact(s):
                return True
        elif isinstance(s, str) and (tacr_extract.EMAIL_RE.search(s) or tacr_extract.PHONE_RE.search(s)):
            return True
    return False


def extraction_checks(tmp):
    """(label, ok) pairs over the good bodies, through read_sources + extract_tacr."""
    rss = write(tmp, "x-rss.xml", GOOD_RSS)
    lst = write(tmp, "x-list.html", GOOD_LISTING)
    out = os.path.join(tmp, "tacr-needs.jsonl")

    s = tacr_extract.read_sources([rss], [], out)
    rows = {r["need_id"]: r for r in map(__import__("json").loads, open(out, encoding="utf-8"))}
    yield "rss: exactly two needs extracted", s["needs"] == 2 and len(rows) == 2
    yield "rss: one non-need post dropped and counted", s["dropped"] == 1 and s["dropped_titles"] == ["Plánovaná odstávka systému ISTA, SISTA a ISRB"]
    yield "rss: ids are TTMD0001 and TIRXMSMT015 (TT and TI both kept)", set(rows) == {"TTMD0001", "TIRXMSMT015"}
    a, b = rows.get("TTMD0001", {}), rows.get("TIRXMSMT015", {})
    yield "TTMD0001: title is the need's name, prefix and code gone", a.get("title") == "Výzkum možností integrace ETCS do drážních vozidel"
    yield "TTMD0001: ministry from 'resortu Ministerstva dopravy'", a.get("ministry") == "Ministerstvo dopravy"
    yield "TTMD0001: date from pubDate", a.get("date") == "2025-08-21"
    yield "TTMD0001: consultation_date from 'Dne 26. září 2025'", a.get("consultation_date") == "2025-09-26"
    yield "TTMD0001: feed trailer dropped from body", "appeared first on" not in a.get("body", "")
    yield "TIRXMSMT015: title from 's názvem „…“'", b.get("title") == "Rámcová dohoda pro výzkum implementace strategických dokumentů vzdělávací politiky"
    yield "TIRXMSMT015: ministry from the abbreviation 'resortu MŠMT'", b.get("ministry") == "Ministerstvo školství, mládeže a tělovýchovy"
    yield "TIRXMSMT015: consultation_date from 'Dne 22. října 2020'", b.get("consultation_date") == "2020-10-22"
    yield "TIRXMSMT015: contact sentence cut, no email/phone in the row", not has_contact(b) and "Registrace je otevřena" in b.get("body", "")

    s2 = tacr_extract.read_sources([rss], [lst], out)
    rows2 = {r["need_id"]: r for r in map(__import__("json").loads, open(out, encoding="utf-8"))}
    yield "rss+html: three unique needs (TTMV0001 only on the listing)", s2["needs"] == 3 and "TTMV0001" in rows2
    m = rows2.get("TTMD0001", {})
    yield "rss+html dedupe: the fuller (rss) body wins", m.get("iface") == "rss" and "Cílem výzkumné potřeby" in m.get("body", "")
    yield "rss+html dedupe: the earliest date is kept (listing's 2025-08-20)", m.get("date") == "2025-08-20"
    yield "rss+html: both surfaces' non-need posts counted once each", s2["dropped"] == 2

    s3 = tacr_extract.read_sources([rss], [lst], out, need_re=r"\bTT[A-Z]{2,8}\d{3,4}\b")
    yield "TACR_NEED_RE override to TT-only keeps 2 of 3", s3["needs"] == 2

    today = datetime.date(2026, 9, 3)
    rec = tacr_extract.extract_tacr(a, "tacr", today)
    yield "extract_tacr: returns a record", rec is not None
    if rec:
        missing = [k for k in MECHANICAL_KEYS + SHAPE_KEYS if k not in rec]
        yield f"extract_tacr: every mechanical REQUIRED_OUT key present (missing: {missing})", not missing
        yield "extract_tacr: id 'tacr-ttmd0001' matches ^[a-z]{2,10}-[\\w.-]+$", rec["id"] == "tacr-ttmd0001" and bool(ID_RE.match(rec["id"]))
        yield "extract_tacr: source=tacr, evidence_type=asks", rec["source"] == "tacr" and rec["evidence_type"] == "asks"
        yield "extract_tacr: entity_native is the ministry", rec["entity_native"] == "Ministerstvo dopravy"
        yield "extract_tacr: urgency_date is the consultation date", rec["urgency_date"] == "2025-09-26"
        yield "extract_tacr: sector/money_eur None, money_note ''", rec["sector"] is None and rec["money_eur"] is None and rec["money_note"] == ""
        yield "extract_tacr: excerpt <= 400 and quote_parts non-empty", len(rec["excerpt"]) <= 400 and len(rec["quote_parts"]) == 2
        yield "extract_tacr: no email/phone anywhere in the record", not has_contact(rec)
    rec2 = tacr_extract.extract_tacr(dict(a, ministry=""), "tacr", today)
    yield "extract_tacr: unknown ministry falls back to TA ČR", rec2["entity_native"] == tacr_extract.FALLBACK_ENTITY
    yield "extract_tacr: refuses a row without need_id/title/link", tacr_extract.extract_tacr({"title": "x", "link": "y"}, "tacr", today) is None


def cross_check_normalize():
    """Drift detection against the file that will import us. A missing
    normalize is a warning (the orchestrator may be mid-edit); a mismatch is
    a failure."""
    try:
        import normalize  # noqa: F401
    except Exception as e:  # noqa: BLE001
        print(f"[warn] normalize.py not importable here ({e.__class__.__name__}: {e}); "
              "REQUIRED_OUT / GDPR patterns checked against the literal copies only")
        return 0
    bad = 0
    for label, ok in (
        ("normalize.REQUIRED_OUT equals the literal held here", tuple(normalize.REQUIRED_OUT) == REQUIRED_OUT),
        ("EMAIL_RE copy matches normalize.EMAIL_RE", tacr_extract.EMAIL_RE.pattern == normalize.EMAIL_RE.pattern),
        ("PHONE_RE copy matches normalize.PHONE_RE", tacr_extract.PHONE_RE.pattern == normalize.PHONE_RE.pattern),
    ):
        print(f"[{'ok  ' if ok else 'FAIL'}] xchk  {label}")
        bad += 0 if ok else 1
    return bad


def main():
    bad = 0
    total = 0
    with tempfile.TemporaryDirectory() as tmp:
        cases = list(guard_cases(tmp))
        width = max(len(c[1]) for c in cases)
        for kind, label, must_reject, path in cases:
            rejected, msg = run_guard(kind, path)
            ok = (rejected == must_reject)
            bad += 0 if ok else 1
            total += 1
            verdict = "REFUSED" if rejected else "accepted"
            print(f"[{'ok  ' if ok else 'FAIL'}] {kind:5s} {label:<{width}}  -> {verdict}: {msg[:100]}")
        print()
        for label, ok in extraction_checks(tmp):
            bad += 0 if ok else 1
            total += 1
            print(f"[{'ok  ' if ok else 'FAIL'}] fold  {label}")
    print()
    bad += cross_check_normalize()
    print()
    if bad:
        print(f"SELFTEST FAILED — {bad} check(s) did not behave as the contract promises")
        return 1
    print(f"SELFTEST PASSED — {total} checks: every wrong body refused, every good body "
          "accepted, every extraction assertion true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
