#!/usr/bin/env python3
"""
edesky_contract_selftest.py — proof that the `edesky` source contract refuses
a WRONG BODY rather than a bad status code, redacts the registrant and the
key before a byte is stored, admits a title BOTH WAYS by rule, cuts contact
lines with a positive control, and yields the `asks` row and the `asks`
record the ledger expects.

Same doctrine as nen_ptk_contract_selftest.py: an Anubis bot-check page, the
API's own "Chyba: nepřihlášen" text, a JSON body or a foreign XML are bytes
with a healthy transport receipt, and the only thing between them and the
ledger is a contract nobody has ever watched fail. So this file makes every
guard fail ON PURPOSE, then drives the good bodies through the SAME entry
points fetch_edesky.sh uses — edesky_extract.guard_file / redact / fold /
extract_edesky and the `guard` / `fold` CLI — and checks what comes out.

    python3 scripts/edesky_contract_selftest.py

Exit 0 = every wrong body refused, every good body accepted, every
assertion true. Offline: nothing is fetched, no key is needed, and it runs
in a sandbox and in CI.

THE FIXTURES ARE SYNTHETIC, AND SAY SO
======================================
No API key existed when this feed was written (the vault holds none and the
terms are unsettled — see scripts/fetch_edesky.sh), so no live page was ever
captured. The page SHAPE is the published one — attributes and element
names from documents.xsd and apiary.apib in github.com/edesky/edesky_api,
percent-encoded attachment text as on the 2015 sample response — and the
two desks are the two the published example names (528 Město Horní Planá,
506 Město Vyšší Brod, with their xs:int-stripped IČOs). The DOCUMENTS are
written for this test. The first real run must be read against these, not
the other way round.

THE CONTACT AND KEY TESTS ARE BUILT, NOT COPIED
===============================================
A negative result needs a positive control (the register's own evidence
doctrine): "no email in the output" proves nothing when the input never had
one. So the registrant mailbox, the phone and the key are RFC 2606 / all-
zero / obviously-fake placeholders, assembled from fragments so that this
file itself carries no email address, no phone number and no `api_key=…`
literal to leak or to trip the repo's gitleaks hook, and `controls()`
asserts each placeholder DOES trip its pattern before any check relies on
its absence downstream.
"""
import contextlib
import datetime
import io
import json
import os
import re
import sys
import tempfile
from urllib.parse import quote, unquote
from xml.sax.saxutils import quoteattr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import edesky_extract as X  # noqa: E402

# normalize.py's REQUIRED_OUT, minus what the MODEL fills. Held as a literal
# so this file is self-contained, and cross-checked against the live tuple
# in cross_check_normalize() so drift is a failure rather than a surprise.
REQUIRED_OUT = ("id", "source", "url", "date", "title", "sector", "geo_origin",
                "money_eur", "money_note", "summary", "scores")
MODEL_FIELDS = ("sector", "geo_origin", "title", "summary", "scores")
MECHANICAL_KEYS = tuple(k for k in REQUIRED_OUT if k not in MODEL_FIELDS)
SHAPE_KEYS = ("evidence_type", "title_native", "entity_native", "owner",
              "urgency_date", "quote_parts", "excerpt")
ID_RE = re.compile(r"^[a-z]{2,10}-[\w.-]+$")
ROW_KEYS = {"id", "title", "municipality", "ico", "category", "dashboard_id",
            "url", "orig_url", "date", "intent", "text"}
PAYLOAD_NAME = "edesky-zamery.jsonl"

# ── the positive controls ───────────────────────────────────────────────────
# Assembled, never written whole — see the header.
REG_MAIL = "registrant" + "@" + "example" + "." + "org"
CLERK_MAIL = "podatelna" + "@" + "example" + "." + "org"
CLERK_TEL = "tel" + ": +420 " + "000 " + "000 " + "000"
CONTACT_LINE = "Kontakt: " + CLERK_MAIL + ", " + CLERK_TEL
FAKE_KEY = "placeholder" + "-not-a-real-" + "key" + "-0000"
FAKE_PARAMS = ('{"keywords"=>"záměr", "created_from"=>"2026-08-22", "api_'
               + 'key"=>"' + FAKE_KEY + '", "include_texts"=>"1", "format"=>"xml"}')


# ══ FIXTURES ════════════════════════════════════════════════════════════════
# Desk attributes as the published example carries them: IČO xs:int-stripped
# ("245895" is 00245895), the zkratka / ruian / text_url attributes present
# so the allowlist has something to cut, an attachment `url` under
# /attachments/ so the row can be shown never to carry one.

def desk_hp():
    return {"dashboard_id": "528", "dashboard_name": "Město Horní Planá",
            "dashboard_ovm_ico": "245895", "dashboard_ovm_zkratka": "HORNPLAN",
            "dashboard_ruian_kod": "545511", "dashboard_category": "samosprava"}


def desk_vb():
    return {"dashboard_id": "506", "dashboard_name": "Město Vyšší Brod",
            "dashboard_ovm_ico": "246191", "dashboard_ovm_zkratka": "VYSSIBROD",
            "dashboard_ruian_kod": "545848", "dashboard_category": "samosprava"}


def document(doc_id, name, text, desk=None, created="2026-08-28 09:12:31 +0200",
             contains_text="1", with_id=True, **over):
    d = dict(desk or desk_hp())
    d.update({
        "name": name, "created_at": created,
        "edesky_url": f"https://edesky.cz/dokument/{doc_id}",
        "edesky_text_url": f"https://edesky.cz/dokument/{doc_id}.txt",
        "orig_url": f"http://www.example.org/deska/{doc_id}.pdf",
        "attachments": [{
            "contains_text": contains_text, "mimetype": "application/pdf",
            "name": name,
            "url": f"https://edesky.cz/attachments/2026_w35/528_{doc_id}/open-uri-x",
            "text": text,
        }],
    })
    if with_id:
        d["edesky_id"] = str(doc_id)
    d.update(over)
    return d


TEXT_KOUPIT = (
    "Město Horní Planá\nNáměstí 54, 382 26 Horní Planá\n"
    "ZÁMĚR OBCE KOUPIT POZEMEK\n"
    "Město Horní Planá zveřejňuje záměr koupit pozemek parc. č. 123/4 o výměře "
    "1 250 m2 v k. ú. Horní Planá od soukromého vlastníka za účelem výstavby "
    "chodníku podél silnice II/163 a odvodnění křižovatky.\n"
    "Zastupitelstvo města záměr projednalo dne 12. 8. 2026 usnesením č. 45/2026. "
    "Kupní cena bude stanovena znaleckým posudkem, nejvýše však 350 Kč za m2.\n"
    "Vyvěšeno dne 28. 8. 2026. Sejmuto dne:"
)
TEXT_PORIDIT = (
    "Město Vyšší Brod\nZÁMĚR POŘÍDIT ZMĚNU Č. 3 ÚZEMNÍHO PLÁNU\n"
    "Zastupitelstvo města schválilo záměr pořídit změnu č. 3 územního plánu "
    "zkráceným postupem. Předmětem změny je vymezení plochy pro novou mateřskou "
    "školu a úprava regulativů v lokalitě Pod Hrází.\n"
    "Návrhy na změnu lze podávat do 30. 9. 2026 na podatelnu městského úřadu."
)
TEXT_ZADAT = (
    "Město Horní Planá\nZÁMĚR ZADAT VEŘEJNOU ZAKÁZKU MALÉHO ROZSAHU\n"
    "Rada města schválila záměr zadat veřejnou zakázku malého rozsahu na opravu "
    "chodníku v ulici Nádražní v délce 420 m včetně výměny obrubníků a "
    "bezbariérových úprav přechodů. Předpokládaná hodnota 1,9 mil. Kč bez DPH.\n"
    "Zahájení prací se předpokládá v říjnu 2026."
)
TEXT_REALIZOVAT = (
    "Město Horní Planá\nZÁMĚR REALIZOVAT REKONSTRUKCI MATEŘSKÉ ŠKOLY\n"
    "Město zveřejňuje záměr realizovat rekonstrukci mateřské školy v ulici "
    "Jiráskova: zateplení obvodového pláště, výměnu oken a instalaci "
    "rekuperačního větrání ve všech třídách. Projektová dokumentace je hotova.\n"
    "Realizace je plánována na letní prázdniny 2027."
)
TEXT_PRODEJ = (
    "Město Vyšší Brod\nZÁMĚR PRODEJE POZEMKU\n"
    "Město Vyšší Brod zveřejňuje podle § 39 odst. 1 zákona č. 128/2000 Sb. "
    "záměr prodat pozemek parc. č. 55/2 o výměře 640 m2 v k. ú. Vyšší Brod. "
    "Nabídky lze podávat do 15 dnů od vyvěšení."
)
TEXT_GENERIC = (
    "Město Horní Planá\nDokument vyvěšený na úřední desce města. Obsah dokumentu "
    "je uveden v příloze, která je k dispozici na podatelně městského úřadu v "
    "úředních hodinách. Vyvěšeno dne 28. 8. 2026."
)

DOC_KOUPIT = document(69057, "Záměr obce koupit pozemek p. č. 123/4 v k. ú. Horní Planá", TEXT_KOUPIT)
DOC_PORIDIT = document(69101, "Záměr města pořídit změnu č. 3 územního plánu", TEXT_PORIDIT,
                       desk=desk_vb(), created="2026-08-27 14:03:00 +0200")
DOC_ZADAT = document(69102, "Záměr zadat veřejnou zakázku malého rozsahu – oprava chodníku Nádražní",
                     TEXT_ZADAT, created="2026-08-26 08:00:00 +0200")
# The same consultation as it actually arrives: a clerk's mailbox and phone
# typed into the notice. The line is the placeholder above.
DOC_CONTACT = document(69103, "Záměr realizovat rekonstrukci mateřské školy Jiráskova",
                       TEXT_REALIZOVAT + "\n" + CONTACT_LINE + "\nVyvěšeno dne 25. 8. 2026.",
                       created="2026-08-25 10:00:00 +0200")
DOC_PRODEJ = document(69104, "Záměr prodeje pozemku parc. č. 55/2 v k. ú. Vyšší Brod", TEXT_PRODEJ,
                      desk=desk_vb())
DOC_BYT = document(69105, "Záměr pronajmout obecní byt č. 5 v čp. 12", TEXT_GENERIC)
DOC_EIA = document(69106, "Oznámení záměru „Areál skleníků“ – posuzování vlivů na životní prostředí (EIA)",
                   TEXT_GENERIC, dashboard_category="instituce")
DOC_PROCEED = document(69107, "Veřejná vyhláška – oznámení zahájení územního řízení (záměr „Chodník podél II/163“)",
                       TEXT_GENERIC)
DOC_NOZAMER = document(69108, "Informace o konání zasedání zastupitelstva města", TEXT_GENERIC)
DOC_NOINTENT = document(69109, "Záměr obce – informace pro občany", TEXT_GENERIC)
DOC_SHORT = document(69110, "Záměr obce koupit pozemek parc. č. 9/1", "Záměr obce koupit pozemek. Bližší informace na úřadě.")
DOC_NOTEXT = document(69111, "Záměr obce koupit budovu čp. 77", "", contains_text="0")
DOC_NOOWNER = document(69112, "Záměr obce koupit pozemek parc. č. 10/3", TEXT_KOUPIT, dashboard_name="")
# No edesky_id AND an edesky_url with no number: no identity, no row.
DOC_NOID = document(0, "Záměr obce koupit pozemek parc. č. 11/1", TEXT_KOUPIT, with_id=False,
                    edesky_url="https://edesky.cz/dokument/")
# The 2015 shape: no edesky_id attribute at all — the trailing number of
# edesky_url is the identity then.
DOC_URLID = document(69113, "Záměr obce nakoupit komunální techniku", TEXT_ZADAT, with_id=False)

ALL_DOCS = [DOC_KOUPIT, DOC_PORIDIT, DOC_ZADAT, DOC_CONTACT, DOC_PRODEJ, DOC_BYT, DOC_EIA,
            DOC_PROCEED, DOC_NOZAMER, DOC_NOINTENT, DOC_SHORT, DOC_NOTEXT, DOC_NOOWNER,
            DOC_NOID, DOC_URLID]
KEPT_IDS = {"69057", "69101", "69102", "69103", "69113"}


# ══ THE PAGE THE FIXTURES ARE WRAPPED IN ════════════════════════════════════

def _attrs(d, skip=()):
    return " ".join(f"{k}={quoteattr(str(v))}" for k, v in d.items()
                    if k not in skip and not isinstance(v, list))


def page_xml(docs, page=1, total_pages=1, total=None, user=REG_MAIL, params=FAKE_PARAMS,
             meta=True, documents=True):
    """An eDesky documents page carrying `docs`, or a deliberately broken one.
    Attachment text is percent-encoded exactly as the live API ships it."""
    out = ["<?xml version='1.0' encoding='utf-8' ?>", f"<{X.ROOT_TAG} version='1.0'>"]
    if meta:
        n = len(docs) if total is None else total
        out += ["<meta>", "<timestamp>2026-09-05 07:46:14 +0200</timestamp>",
                f"<user>{user}</user>", f"<requested_params>{params}</requested_params>",
                f"<documents_count total=\"{n}\">{len(docs)}</documents_count>",
                f"<page total_pages=\"{total_pages}\">{page}</page>", "</meta>"]
    if documents:
        out.append("<documents>")
        for d in docs:
            out.append(f"<document {_attrs(d)}>")
            out.append("<attachments>")
            for att in d.get("attachments", []):
                out.append(f"<attachment {_attrs(att, skip=('text',))}>")
                out.append(quote(att.get("text") or "", safe=""))
                out.append("</attachment>")
            out.append("</attachments></document>")
        out.append("</documents>")
    out.append(f"</{X.ROOT_TAG}>")
    return "\n".join(out).encode("utf-8")


ANUBIS_HTML = (
    '<!doctype html><html lang="en"><head><title>Making sure you&#39;re not a bot!</title>'
    '</head><body><div class="centered-div"><h1>Making sure you\'re not a bot!</h1>'
    '<p>Anubis is protecting this site.</p></div></body></html>'
).encode("utf-8")

# The API's own text for a missing key — measured 2026-09-04 (HTTP 401, but
# the body is what a saved payload would carry).
UNAUTH_TEXT = ("Chyba: nepřihlášen. Použijte svůj API klíč, který najdete pro přihlášení "
               "na https://edesky.cz/uzivatel/edit").encode("utf-8")

JSON_BODY = b'{"documents": [], "meta": {"documents_count": 0}}'

FOREIGN_XML = (b"<?xml version='1.0'?><rss version='2.0'><channel><title>x</title>"
               b"<item><title>Z\xc3\xa1m\xc4\x9br</title></item></channel></rss>")

# An error page that ECHOES THE REQUEST URL, key included — the case the
# api_key= redaction exists for.
ECHO_HTML = ("<!doctype html><html><body><h1>404</h1><p>No route matches "
             "/api/v1/documents?api_key=" + FAKE_KEY + "&amp;keywords=z%C3%A1m%C4%9Br</p>"
             "</body></html>").encode("utf-8")


# ══ CASES ═══════════════════════════════════════════════════════════════════

def write(tmp, name, data):
    p = os.path.join(tmp, name)
    with open(p, "wb") as fh:
        fh.write(data)
    return p


def guard_cases(tmp):
    """(label, must_reject, path)."""
    yield ("empty body", True, write(tmp, "g-empty.xml", b""))
    yield ("Anubis bot-check page served as the API", True, write(tmp, "g-anubis.xml", ANUBIS_HTML))
    yield ("the API's 'Chyba: nepřihlášen' text saved as a body", True,
           write(tmp, "g-401.xml", UNAUTH_TEXT))
    yield ("a JSON body", True, write(tmp, "g-json.xml", JSON_BODY))
    yield ("a foreign XML (RSS) with the keyword in it", True, write(tmp, "g-rss.xml", FOREIGN_XML))
    yield ("edesky_search_api root with meta but NO <documents>", True,
           write(tmp, "g-nodocs.xml", page_xml([DOC_KOUPIT], documents=False)))
    yield ("a page truncated mid-document", True,
           write(tmp, "g-trunc.xml", page_xml([DOC_KOUPIT])[:-120]))
    yield ("THE GOOD BODY — a documents page", False, write(tmp, "g-good.xml", page_xml(ALL_DOCS)))
    yield ("a page with ZERO documents (an empty window is not a wrong body)", False,
           write(tmp, "g-zero.xml", page_xml([])))
    yield ("a page with no <meta> at all (the 2015 sample has no <page>)", False,
           write(tmp, "g-nometa.xml", page_xml([DOC_KOUPIT], meta=False)))


def run_guard(path):
    try:
        _root, m = X.guard_file(path)
        return False, f"accepted page {m['page']}/{m['total_pages']}, {m['count']} on disk, api total {m['total']}"
    except X.ContractViolation as e:
        return True, str(e)


def has_contact(obj):
    """Any email or phone anywhere in a row/record, at any depth."""
    if isinstance(obj, dict):
        return has_contact(list(obj.keys()) + list(obj.values()))
    if isinstance(obj, (list, tuple)):
        return any(has_contact(v) for v in obj)
    s = obj if isinstance(obj, str) else ""
    return bool(X.EMAIL_RE.search(s) or X.PHONE_RE.search(s))


def controls():
    """THE POSITIVE CONTROLS. Every 'nothing survived' check below is a
    negative result, and a negative result over an input that never carried
    the thing proves nothing at all."""
    page = page_xml([DOC_CONTACT]).decode("utf-8")
    encoded_line = quote(CONTACT_LINE, safe="")
    yield "control: the registrant placeholder DOES match EMAIL_RE", bool(X.EMAIL_RE.search(REG_MAIL))
    yield "control: the clerk placeholder DOES match EMAIL_RE", bool(X.EMAIL_RE.search(CLERK_MAIL))
    yield "control: the phone placeholder DOES match PHONE_RE", bool(X.PHONE_RE.search(CLERK_TEL))
    yield "control: the raw page DOES carry the registrant and the key in <meta>", (
        REG_MAIL in page and FAKE_KEY in page)
    # The clerk line travels PERCENT-ENCODED ('@' is %40), so it is checked
    # the way the extractor will meet it: encoded on the page, plain after
    # unquote. A plain-substring test here would fail for the wrong reason.
    yield "control: the clerk line is on the page encoded, and decodes to an email + phone", (
        encoded_line in page and CLERK_MAIL in unquote(encoded_line)
        and bool(X.PHONE_RE.search(unquote(encoded_line))))
    yield "control: the contact-carrying document DOES trip has_contact()", has_contact(DOC_CONTACT)


def redact_checks():
    page = page_xml([DOC_KOUPIT]).decode("utf-8")
    red = X.redact(page)
    yield "redact: the registrant mailbox is gone from the stored body", REG_MAIL not in red
    yield "redact: the key is gone from the stored body", FAKE_KEY not in red
    yield "redact: <user> and <requested_params> survive as elements, blanked", (
        f"<user>{X.REDACTED}</user>" in red and f"<requested_params>{X.REDACTED}</requested_params>" in red)
    yield "redact: the documents are untouched", (
        X.guard_page(red.encode("utf-8"))[1]["count"] == 1 and "Horní Planá" in red)
    echo = X.redact(ECHO_HTML.decode("utf-8"))
    yield "redact: an error page echoing api_key=… in a URL loses the value too", (
        FAKE_KEY not in echo and "api_key=" + X.REDACTED in echo)
    yield "redact: a body with nothing to redact is returned byte-identical", (
        X.redact(UNAUTH_TEXT.decode("utf-8")) == UNAUTH_TEXT.decode("utf-8"))


# The title rule, BOTH WAYS. (title, expected intent, expected reason).
TITLE_TABLE = (
    ("Záměr obce koupit pozemek p. č. 123/4 v k. ú. Horní Planá", "koupit", None),
    ("Záměr města pořídit změnu č. 3 územního plánu", "pořídit", None),
    ("Záměr zadat veřejnou zakázku malého rozsahu na opravu chodníku", "zadat", None),
    ("Záměr realizovat rekonstrukci mateřské školy", "realizovat", None),
    ("Záměr obce pronajmout si skladové prostory pro techniku", "pronajmout", None),
    ("Zamer obce nakoupit komunalni techniku", "koupit", None),          # no diacritics
    ("ZÁMĚR VÝKUPU POZEMKŮ POD KOMUNIKACÍ", "koupit", None),              # uppercase, noun
    ("Záměr odkoupení části pozemku od soukromého vlastníka", "koupit", None),
    ("Záměr prodeje pozemku parc. č. 55/2", None, X.DISPOSAL),
    ("Záměr obce prodat část pozemku", None, X.DISPOSAL),
    ("Záměr odprodeje nepotřebného majetku", None, X.DISPOSAL),
    ("Záměr pronajmout obecní byt č. 5 v čp. 12", None, X.DISPOSAL),
    ("Záměr pronájmu městského bytu", None, X.DISPOSAL),
    ("Záměr směny pozemků", None, X.DISPOSAL),
    ("Záměr výpůjčky nebytových prostor", None, X.DISPOSAL),
    ("Záměr propachtovat zemědělské pozemky", None, X.DISPOSAL),
    ("Záměr darovat pozemek kraji", None, X.DISPOSAL),
    ("Záměr zřízení věcného břemene – služebnosti inženýrské sítě", None, X.DISPOSAL),
    ("Záměr bezúplatného převodu pozemku", None, X.DISPOSAL),
    ("Záměr prodat a koupit pozemky (směna)", None, X.DISPOSAL),         # drop beats keep
    ("Oznámení záměru „Areál skleníků“ – posuzování vlivů na životní prostředí (EIA)", None, X.EIA_NOTICE),
    ("Záměr „Logistické centrum“ – zjišťovací řízení", None, X.EIA_NOTICE),
    ("Veřejná vyhláška – oznámení zahájení územního řízení (záměr)", None, X.PROCEEDINGS),
    ("Záměr stavby – oznámení o zahájení stavebního řízení", None, X.PROCEEDINGS),
    ("Informace o konání zasedání zastupitelstva", None, X.NO_ZAMER),
    ("Prodej pozemku – bez slova z.", None, X.NO_ZAMER),
    ("Záměr obce – informace pro občany", None, X.NO_ACQUIRE),
    ("Záměr uzavřít smlouvu o spolupráci", None, X.NO_ACQUIRE),
)


def title_checks():
    for title, intent, reason in TITLE_TABLE:
        got = X.classify_title(title)
        want = (intent, reason)
        yield f"title: {title[:58]!r:<60} -> {intent or reason}", got == want


def fold_checks(tmp):
    """(label, ok) over fold() — the entry point fetch_edesky.sh calls."""
    p1 = write(tmp, "f-p1.xml", X.redact(page_xml(ALL_DOCS, page=1, total_pages=2,
                                                  total=len(ALL_DOCS) + 1).decode("utf-8")).encode("utf-8"))
    # Page 2 repeats KOUPIT (the set shifted between requests) and adds nothing.
    p2 = write(tmp, "f-p2.xml", page_xml([DOC_KOUPIT], page=2, total_pages=2))
    out = os.path.join(tmp, PAYLOAD_NAME)
    s = X.fold([p1, p2], out)
    rows = {r["id"]: r for r in (json.loads(line) for line in open(out, encoding="utf-8"))}

    yield "fold: 2 pages, %d documents -> 5 kept, 10 dropped, 1 duplicate" % (len(ALL_DOCS) + 1), (
        s["pages"] == 2 and s["documents"] == len(ALL_DOCS) + 1 and s["kept"] == 5
        and s["dropped"] == 10 and s["duplicates"] == 1)
    yield "fold: exactly the five acquiring rows are kept", set(rows) == KEPT_IDS
    yield "fold: kept_by_intent counts every verb once", s["kept_by_intent"] == {
        "koupit": 2, "pořídit": 1, "zadat": 1, "realizovat": 1}
    yield "fold: the drops are counted BY REASON", s["dropped_by_reason"] == {
        X.DISPOSAL: 2, X.EIA_NOTICE: 1, X.PROCEEDINGS: 1, X.NO_ZAMER: 1, X.NO_ACQUIRE: 1,
        X.NO_STATED_NEED: 1, X.NO_TEXT: 1, X.NO_OWNER: 1, X.NO_ID: 1}
    yield "fold: the detail names the document and its reason", (
        any(d == "69104: " + X.DISPOSAL for d in s["dropped_detail"])
        and any(d == "69111: " + X.NO_TEXT for d in s["dropped_detail"]))
    yield "fold: two desks, none without an IČO", s["owners"] == 2 and s["no_ico"] == 0

    r = rows.get("69057", {})
    yield "row: exactly the payload keys — no zkratka, ruian, text_url or attachment url", set(r) == ROW_KEYS
    yield "row: id, title and owner are the document's", (
        r.get("id") == "69057" and r.get("title") == DOC_KOUPIT["name"]
        and r.get("municipality") == "Město Horní Planá")
    yield "row: the xs:int-stripped IČO 245895 is padded back to 00245895", r.get("ico") == "00245895"
    yield "row: category is the DESK's kind (samosprava), dashboard_id kept", (
        r.get("category") == "samosprava" and r.get("dashboard_id") == "528")
    yield "row: url is the eDesky document page, orig_url the desk's own file", (
        r.get("url") == "https://edesky.cz/dokument/69057"
        and r.get("orig_url", "").endswith("/69057.pdf"))
    yield "row: never an /attachments/ path anywhere in the row", not any(
        "/attachments/" in str(v) for v in r.values())
    yield "row: date is the ISO day of created_at", r.get("date") == "2026-08-28"
    yield "row: intent names the verb that admitted it", r.get("intent") == "koupit"
    yield "row: the percent-encoded text came back as Czech, newlines collapsed", (
        "záměr koupit pozemek parc. č. 123/4" in r.get("text", "")
        and "\n" not in r.get("text", "") and "%20" not in r.get("text", ""))
    yield "row: text <= %d chars" % X.MAX_TEXT, len(r.get("text", "")) <= X.MAX_TEXT
    yield "row: no email or phone in the plain row either", not has_contact(r)

    c = rows.get("69103", {})
    yield "row: the contact-carrying document IS staged (the need survives the cut)", bool(c)
    yield "row: no email and no phone anywhere in it", not has_contact(c)
    yield "row: the contact LINE is gone, the sentences around it are not", (
        "Kontakt:" not in c.get("text", "") and "rekuperačního větrání" in c.get("text", "")
        and "Vyvěšeno dne 25. 8. 2026" in c.get("text", ""))

    u = rows.get("69113", {})
    yield "row: a 2015-shape document (no edesky_id) takes its id off edesky_url", (
        u.get("id") == "69113" and u.get("url") == "https://edesky.cz/dokument/69113")

    yield "fold: rows are ordered newest first", [x["id"] for x in
                                                  sorted(rows.values(), key=lambda x: (x["date"], int(x["id"])), reverse=True)] \
        == [ln and json.loads(ln)["id"] for ln in open(out, encoding="utf-8").read().splitlines()]
    yield "fold: an unguardable body stops the fold rather than being folded", _raises(
        X.fold, [write(tmp, "f-anubis.xml", ANUBIS_HTML)], out)

    # A body big enough to exercise the cap: MAX_TEXT + a tail.
    long_doc = document(69200, "Záměr obce koupit lesní pozemky", TEXT_KOUPIT + (" Další odstavec o záměru. " * 120))
    X.fold([write(tmp, "f-long.xml", page_xml([long_doc]))], out)
    lr = json.loads(open(out, encoding="utf-8").readline())
    yield "row: a long text is capped at %d chars, at a sentence end" % X.MAX_TEXT, (
        len(lr["text"]) <= X.MAX_TEXT and lr["text"].endswith("."))
    return rows


def _raises(fn, *a, **kw):
    try:
        fn(*a, **kw)
        return False
    except X.ContractViolation:
        return True


def extract_checks(rows):
    today = datetime.date(2026, 9, 5)
    row = rows["69057"]
    rec = X.extract_edesky(row, "zamery", today)
    yield "extract_edesky: returns a record", rec is not None
    if not rec:
        return
    missing = [k for k in MECHANICAL_KEYS + SHAPE_KEYS if k not in rec]
    yield f"extract: every mechanical REQUIRED_OUT + shape key present (missing: {missing})", not missing
    yield "extract: id is edesky-<document id> and matches ^[a-z]{2,10}-[\\w.-]+$", (
        rec["id"] == "edesky-69057" and bool(ID_RE.match(rec["id"])))
    yield "extract: source=edesky, evidence_type=asks", (
        rec["source"] == "edesky" and rec["evidence_type"] == "asks")
    yield "extract: top-level owner is the desk — the asks ledger's required field", (
        rec["owner"] == "Město Horní Planá" and rec["owner"] == rec["entity_native"])
    yield "extract: urgency_date is None, sector None, money_eur None, money_note ''", (
        rec["urgency_date"] is None and rec["sector"] is None
        and rec["money_eur"] is None and rec["money_note"] == "")
    yield "extract: date off the row, url off the row", (
        rec["date"] == "2026-08-28" and rec["url"] == row["url"])
    yield "extract: a row with no date falls back to the run date", (
        X.extract_edesky(dict(row, date=""), "zamery", today)["date"] == "2026-09-05")
    yield "extract: excerpt <= 400 and quote_parts verifiable against the row", (
        len(rec["excerpt"]) <= 400 and len(rec["quote_parts"]) == 2
        and all(q in (row["title"] + " " + row["text"]) for q in rec["quote_parts"]))
    yield "extract: the same input yields the same id twice", (
        X.extract_edesky(row, "zamery", today)["id"]
        == X.extract_edesky(row, "zamery", datetime.date(2027, 1, 1))["id"] == rec["id"])
    yield "extract: no email or phone anywhere in the record", not has_contact(rec)
    crec = X.extract_edesky(rows["69103"], "zamery", today)
    yield "extract: the contact-carrying record stays contact-free end to end", (
        crec is not None and not has_contact(crec))
    yield "extract: a row naming no desk is REFUSED — no 'eDesky' fallback owner", (
        X.extract_edesky(dict(row, municipality=""), "zamery", today) is None)
    yield "extract: a disposal title is refused again at the record", (
        X.extract_edesky(dict(row, title="Záměr prodeje pozemku parc. č. 1"), "zamery", today) is None)
    yield "extract: a row whose text is a label is refused again at the record", (
        X.extract_edesky(dict(row, text="Záměr obce koupit pozemek."), "zamery", today) is None)
    yield "extract: a row with no id, a non-numeric id, or no title is refused", all(
        X.extract_edesky(dict(row, **kv), "zamery", today) is None
        for kv in ({"id": ""}, {"id": "abc"}, {"title": ""}))
    yield "extract: a row with no url rebuilds it from the id", (
        X.extract_edesky(dict(row, url=""), "zamery", today)["url"] == row["url"])
    yield "extract: there is no fallback-owner constant to fall back to", not any(
        n for n in dir(X) if "FALLBACK" in n.upper())


def _cli(argv):
    """Run the extractor's CLI in-process. Returns (rc, stdout)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = X.main(argv)
    return rc, buf.getvalue().strip()


def cli_checks(tmp):
    """THE SEAM THE FETCHER ACTUALLY USES. fetch_edesky.sh never imports this
    module — it shells out to `guard` and `fold`, reads their exit status,
    the four tab-separated counts, and specific jq paths of the summary."""
    good = write(tmp, "c-good.xml", page_xml(ALL_DOCS, page=1, total_pages=3, total=555))
    stored = os.path.join(tmp, "c-good-stored.xml")
    rc, out = _cli(["guard", good, "--redact-to", stored])
    yield "cli guard: rc 0 and 'page\\ttotal_pages\\tcount\\ttotal' on stdout", (
        rc == 0 and out == "1\t3\t%d\t555" % len(ALL_DOCS))
    kept = open(stored, encoding="utf-8").read()
    yield "cli guard: the stored copy carries neither the registrant nor the key", (
        REG_MAIL not in kept and FAKE_KEY not in kept and X.REDACTED in kept)
    yield "cli guard: the stored copy still guards as a documents page", (
        X.guard_file(stored)[1]["count"] == len(ALL_DOCS))

    anubis = write(tmp, "c-anubis.xml", ANUBIS_HTML)
    stored2 = os.path.join(tmp, "c-anubis-stored.xml")
    rc, out = _cli(["guard", anubis, "--redact-to", stored2])
    yield "cli guard: a wrong body exits non-zero and says why", (
        rc != 0 and out.startswith("CONTRACT VIOLATION:"))
    yield "cli guard: the refused body is STILL stored (as evidence), redacted", (
        os.path.exists(stored2) and "not a bot" in open(stored2, encoding="utf-8").read())
    echo = write(tmp, "c-echo.xml", ECHO_HTML)
    stored3 = os.path.join(tmp, "c-echo-stored.xml")
    rc, out = _cli(["guard", echo, "--redact-to", stored3])
    yield "cli guard: a refused error page echoing the key is stored WITHOUT it", (
        rc != 0 and FAKE_KEY not in open(stored3, encoding="utf-8").read())

    out_jsonl = os.path.join(tmp, "cli-" + PAYLOAD_NAME)
    listfile = write(tmp, "good with space.list", (stored + "\n").encode("utf-8"))
    rc, out = _cli(["fold", "--out", out_jsonl, "--paths-from", listfile])
    summary = json.loads(out) if rc == 0 else {}
    yield "cli fold: rc 0 and one JSON object on stdout", rc == 0 and bool(summary)
    yield "cli fold: carries every key fetch_edesky.sh reads with jq", set(summary) >= {
        "pages", "documents", "kept", "dropped", "duplicates", "owners", "no_ico",
        "dropped_by_reason", "dropped_detail", "kept_by_intent"}
    yield "cli fold: wrote the payload the fetcher moves into place", (
        summary.get("kept") == 5
        and len(open(out_jsonl, encoding="utf-8").read().splitlines()) == 5)


def cross_check_normalize():
    """Drift detection against the file that will import us."""
    try:
        import normalize  # noqa: F401
    except Exception as e:  # noqa: BLE001
        print(f"[warn] normalize.py not importable here ({e.__class__.__name__}: {e}); "
              "REQUIRED_OUT / GDPR patterns checked against the literal copies only")
        return 0
    bad = 0
    tokens = [t for t, _ in normalize.FILE_FEED_TOKENS]
    live = normalize.FILE_FEED_TOKENS
    try:
        normalize.FILE_FEED_TOKENS = live + [("edesky", "edesky")]
        with_token = normalize.feed_for_file(PAYLOAD_NAME)
    finally:
        normalize.FILE_FEED_TOKENS = live
    for label, ok in (
        ("normalize.REQUIRED_OUT equals the literal held here",
         tuple(normalize.REQUIRED_OUT) == REQUIRED_OUT),
        ("EMAIL_RE copy matches normalize.EMAIL_RE",
         X.EMAIL_RE.pattern == normalize.EMAIL_RE.pattern),
        ("PHONE_RE copy matches normalize.PHONE_RE",
         X.PHONE_RE.pattern == normalize.PHONE_RE.pattern),
        ("`owner` is on normalize's ledger allowlist",
         "owner" in normalize.LEDGER_ALLOWLIST),
        # THE TOKEN PROOF. FILE_FEED_TOKENS is FIRST-MATCH-WINS: no existing
        # token may sit inside `edesky-zamery.jsonl` (or another feed would
        # claim the payload), and the reddit markers must not either.
        ("no existing token is a substring of " + PAYLOAD_NAME,
         not [t for t in tokens if t in PAYLOAD_NAME]),
        ("no reddit marker is a substring of " + PAYLOAD_NAME,
         not [m for m in normalize.REDDIT_SEARCH_MARKERS if m in PAYLOAD_NAME]),
        ("with (edesky, edesky) registered the payload resolves to edesky",
         with_token == "edesky"),
    ):
        print(f"[{'ok  ' if ok else 'FAIL'}] xchk  {label}")
        bad += 0 if ok else 1
    print(f"[info] xchk  feed_for_file({PAYLOAD_NAME!r}) resolves to "
          f"{normalize.feed_for_file(PAYLOAD_NAME)!r} as normalize.py stands right now")
    return bad


def main():
    bad = total = 0

    def run(section, gen):
        nonlocal bad, total
        for label, ok in gen:
            bad += 0 if ok else 1
            total += 1
            print(f"[{'ok  ' if ok else 'FAIL'}] {section:7s} {label}")
        print()

    with tempfile.TemporaryDirectory() as tmp:
        cases = list(guard_cases(tmp))
        width = max(len(c[0]) for c in cases)
        for label, must_reject, path in cases:
            rejected, msg = run_guard(path)
            ok = (rejected == must_reject)
            bad += 0 if ok else 1
            total += 1
            print(f"[{'ok  ' if ok else 'FAIL'}] guard   {label:<{width}}  -> "
                  f"{'REFUSED' if rejected else 'accepted'}: {msg[:90]}")
        print()
        run("ctrl", controls())
        run("redact", redact_checks())
        run("title", title_checks())
        rows = None
        gen = fold_checks(tmp)
        while True:
            try:
                label, ok = next(gen)
            except StopIteration as stop:
                rows = stop.value
                break
            bad += 0 if ok else 1
            total += 1
            print(f"[{'ok  ' if ok else 'FAIL'}] fold    {label}")
        print()
        run("extract", extract_checks(rows))
        run("cli", cli_checks(tmp))
    bad += cross_check_normalize()
    print()
    if bad:
        print(f"SELFTEST FAILED — {bad} check(s) did not behave as the contract promises")
        return 1
    print(f"SELFTEST PASSED — {total} checks: every wrong body refused, every good body "
          "accepted, registrant and key redacted, titles ruled both ways, every "
          "extraction assertion true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
