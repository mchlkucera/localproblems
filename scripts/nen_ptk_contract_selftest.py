#!/usr/bin/env python3
"""
nen_ptk_contract_selftest.py — proof that the `nen-ptk` source contract refuses
a WRONG BODY rather than a bad status code, and that a right body yields the
`asks` row and the `asks` record the ledger expects.

Same doctrine as tacr_contract_selftest.py: a 200 carrying a login form, a
maintenance notice or NEN's own shell for a number nobody assigned is bytes
with a healthy transport receipt, and the only thing between it and the ledger
is a contract nobody has ever watched fail. So this file makes every guard fail
ON PURPOSE, then drives the good bodies through the SAME entry points
fetch_nen_ptk.sh uses — nen_ptk_extract.guard_detail / guard_subject / fold /
extract_nen_ptk — and checks what comes out.

    python3 scripts/nen_ptk_contract_selftest.py

Exit 0 = every wrong body refused, every good body accepted, every extraction
assertion true. Offline: no fixture is fetched, so this runs in a sandbox and
in CI, and it costs the site nothing at a Crawl-delay of 10.

THE FIXTURES ARE REAL, AND TRIMMED TO THE ALLOWLIST
===================================================
PTK_OBJ and PRUZKUM_OBJ are the live `detailObjectStore` objects of
N006/26/P00000122 (Statutární město Jablonec nad Nisou) and N006/26/P00000002
(Katastrální úřad pro Ústecký kraj), captured 2026-09-04, reduced to
nen_ptk_extract.FIELDS. SUBJECT_OBJ is the buyer page of subject 96530994, cut
to `ico`. Every value in those three is verbatim. The four fixtures derived
from them (SHORT_OBJ, CONTACT_OBJ, NO_BUYER_OBJ and the wrong-kod page) each
say in a comment what was changed and why.

The trim is not only about file size. The live detail object carries 63 keys
and the subject object 40, among them `osobaJmeno`, `osobaPrijmeni`, `osobaEmail` and `osobaTelefon` — a
named civil servant's mailbox and phone. Measured on the 2026-09-04 walk of
P00000001–P00000025: all 22 detail bodies carry both, and on P00000122 exactly
`osobaEmail` and `osobaTelefon` match normalize.EMAIL_RE / normalize.PHONE_RE
and no other field does. A fixture is a committed file in a public repository,
so those values do not exist here in any form.

WHICH MEANS THE CONTACT TEST HAD TO BE BUILT, NOT COPIED
========================================================
The allowlist must still be PROVED to cut them, and a test that only asserts
"no email in the output" passes trivially when the input never had one — the
register's own evidence doctrine: a negative result needs a positive control.
So CONTACT_OBJ re-adds the contact fields with RFC 2606 reserved placeholders,
assembled from fragments so that this file itself contains no email address and
no phone number to leak or to trip the repo's gitleaks hook. `contact_control()`
asserts the placeholders DO match the two patterns before any check relies on
their absence downstream.
"""
import contextlib
import datetime
import io
import json
import os
import re
import sys
import tempfile
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import nen_ptk_extract as X  # noqa: E402

# normalize.py's REQUIRED_OUT, minus what the MODEL fills. Held as a literal so
# this file is self-contained, and cross-checked against the live tuple in
# cross_check_normalize() so drift is a failure rather than a surprise.
REQUIRED_OUT = ("id", "source", "url", "date", "title", "sector", "geo_origin",
                "money_eur", "money_note", "summary", "scores")
MODEL_FIELDS = ("sector", "geo_origin", "title", "summary", "scores")
MECHANICAL_KEYS = tuple(k for k in REQUIRED_OUT if k not in MODEL_FIELDS)
# The extract_nku shape this extractor mirrors, plus the `asks` ledger's own
# top-level `owner` (data/CONVENTIONS.md: REQUIRED on every asks record).
SHAPE_KEYS = ("evidence_type", "title_native", "entity_native", "owner",
              "urgency_date", "quote_parts", "excerpt")
ID_RE = re.compile(r"^[a-z]{2,10}-[\w.-]+$")

# ── the positive control ────────────────────────────────────────────────────
# Assembled, never written whole: this file must contain no email and no phone
# number. example.org is RFC 2606 reserved and the number is all zeros, so
# neither is anybody's. See the header.
CONTACT_MAIL = "podatelna" + "@" + "example" + "." + "org"
CONTACT_TEL = "tel" + ": +420 " + "000 " + "000 " + "000"
CONTACT_SENTENCE = "Dotazy zasílejte na " + CONTACT_MAIL + " nebo " + CONTACT_TEL + "."


# ══ FIXTURES ════════════════════════════════════════════════════════════════
# Real objects, trimmed to nen_ptk_extract.FIELDS. `zadavatelID` is an int on
# the live surface (measured) and is left an int here on purpose — the row
# builder collapses it to a string and the IČO map is keyed by that string, so
# a fixture that "helpfully" quoted it would stop testing the join.

PTK_OBJ = {
    "kod": "N006/26/P00000122",
    "nazev": "Předběžné tržní konzultace k zakázce: „Kantorova vila v Jablonci nad Nisou“",
    "druhZRNazev": "Předběžná tržní konzultace",
    "zadavatelNazev": "Statutární město Jablonec nad Nisou",
    "zadavatelID": 74603670,
    "popisPredmet": (
        "Zadavatel se rozhodl s ohledem na charakter a složitost předmětu veřejné "
        "zakázky využít možnosti vést předběžnou tržní konzultaci ve smyslu § 33 "
        "zákona. Zadavatel dne 17. 3. 2026 vyhlásil v režimu zjednodušeného "
        "podlimitní řízení zadávací řízení „Kantorova vila v Jablonci nad Nisou“ s "
        "předpokládanou hodnotou 40 mil. Kč bez DPH. Do konce lhůty pro podání "
        "nabídek byla doručena pouze jedna nabídka, která výrazně převyšuje "
        "předpokládanou hodnotu zakázky. Zadavatel toto zadávací řízení zrušil v "
        "souladu s ustanovením § 127 odst. 2 písm. h zákona.\n\n"
        "<p>Předmětem plnění plánované veřejné zakázky je rekonstrukce památkově "
        "chráněné významné funkcionalistické stavby rodinného domu.</p>"
        "<p>Předmětem PKT je získání informací o objektivní schopnosti budoucích "
        "dodavatelů splnit podmínky veřejné zakázky a získat informace, proč se do "
        "původního řízení přihlásil pouze jeden účastník.</p>"
    ),
    "cpvPredmetuKod": "45212300-9",
    "datumProfil": "2026-05-15T15:19:55",
    "podaniInformaceLhuta": "2026-05-27T10:00:00",
}

# The ~20% of the P series that is a PRICE CHECK, not a consultation. Verbatim
# from the live page: the buyer already knows what it wants and is shopping.
PRUZKUM_OBJ = {
    "kod": "N006/26/P00000002",
    "nazev": "Dodání drogistického zboží",
    "druhZRNazev": "Průzkum trhu",
    "zadavatelNazev": "Katastrální úřad pro Ústecký kraj",
    "zadavatelID": 96530994,
    "popisPredmet": ("Dodání drogistického zboží - toaletního papíru, prostředku na "
                     "nádobí, gel do WC a gel na čištění WC.\n\nPožadujeme náhradní "
                     "plnění dle zákona o zaměstnanosti."),
    "cpvPredmetuKod": "33761000-2",
    "datumProfil": "2026-01-08T15:04:23",
    "podaniInformaceLhuta": "2026-01-16T08:00:00",
}

# The buyer page, cut to the one key it is read for: subject id 96530994 is the
# Průzkum trhu buyer above and its IČO is 71185194 — the id and the IČO are
# DIFFERENT numbers, which is the whole reason the extra hop exists. The live
# object carries 40 keys, among them a bank account and a second mailbox.
SUBJECT_OBJ = {"ico": "71185194"}
SUBJECT_SID = "96530994"

# A consultation whose `popisPredmet` is a LABEL, not a need. Measured range of
# the field is 43–4,477 chars (median 345), so the short end is real; this is
# the P00000122 record with its description cut to one, 33 characters long.
SHORT_OBJ = dict(PTK_OBJ, kod="N006/26/P00000131",
                 popisPredmet="Rekonstrukce vily – dotaz na trh.")

# The same consultation as it actually arrives: a contact person on the object
# AND a contact sentence the buyer typed into the free-text description. The
# person is the Czech John Doe and the mailbox and number are the placeholders
# above — the real ones belong to a named civil servant and are not in this
# repository.
CONTACT_OBJ = dict(
    PTK_OBJ,
    kod="N006/26/P00000132",
    popisPredmet=PTK_OBJ["popisPredmet"] + "\n\n" + CONTACT_SENTENCE,
    osobaJmeno="Jan", osobaPrijmeni="Novák",
    osobaEmail=CONTACT_MAIL, osobaTelefon=CONTACT_TEL,
    predpokladHodnota=None, mistoPlneni="Jablonec nad Nisou",
)

NO_BUYER_OBJ = dict(PTK_OBJ, kod="N006/26/P00000133", zadavatelNazev="")


# ══ THE PAGE THE FIXTURES ARE WRAPPED IN ════════════════════════════════════
# NEN ships the whole redux state as encodeURI'd JSON inside a <meta> content
# attribute, then renders the same object as `gov-grid-tile` blocks. Both are
# reproduced, because guard_detail reads BOTH: the meta for the object and the
# rendered tile label as the marker that the template rendered a procedure at
# all.
_URI_SAFE = "!#$&'()*+,/:;=?@~"   # what encodeURI leaves alone — measured on the live page

_TILE = ('<div title="{label}" class="gov-grid-tile">'
         '<h3 class="gov-title--delta">{label}</h3>'
         '<p class="text gov-note">{value}</p></div>')


def _meta(state):
    body = json.dumps(state, ensure_ascii=False, separators=(",", ":"))
    return '<meta name="initialReduxState" content="%s">' % quote(body, safe=_URI_SAFE)


def _chrome(head, body):
    return ('<!DOCTYPE html><html lang="cs"><head>'
            '<title>Detail zakázky - Národní elektronický nástroj</title>'
            + head + '</head><body><div class="gov-container">' + body
            + '</div></body></html>').encode("utf-8")


def detail_page(obj, key_kod=None, marker=True, meta=True, null_object=False):
    """A NEN detail page carrying `obj`, or a deliberately broken one."""
    kod = key_kod or str(obj.get("kod") or "")
    entry = {"id": kod, "isFetching": False, "evaluatedConditions": {},
             "object": None if null_object else obj}
    state = {"breadcrumb": {"items": [{"href": "/", "title": "Úvod"}]},
             "detailObjectStore": {"objects": {X.OBJ_PREFIX + kod: entry}},
             "errorStore": {}, "router": {}}
    head = _meta(state) if meta else ""
    tiles = _TILE.format(label="Systémové číslo NEN", value=kod)
    if marker:
        tiles += _TILE.format(label=X.HTML_MARKER,
                              value=str(obj.get("druhZRNazev") or ""))
    return _chrome(head, tiles)


def subject_page(obj, sid, meta=True):
    entry = {"id": sid, "isFetching": False, "object": obj}
    state = {"detailObjectStore": {"objects": {X.SUBJ_PREFIX + str(sid): entry}}}
    return _chrome(_meta(state) if meta else "",
                   _TILE.format(label="IČO", value=str(obj.get("ico") or "")))


LOGIN_HTML = (
    '<!DOCTYPE html><html lang="cs"><head><title>Přihlášení do NEN</title></head>'
    '<body><h1>Přihlášení</h1><form method="post" action="/login">'
    '<input name="username"><input name="password" type="password">'
    '<button>Přihlásit</button></form></body></html>'
).encode("utf-8")

MAINTENANCE_HTML = (
    '<!DOCTYPE html><html lang="cs"><head><title>Odstávka</title></head>'
    '<body><h1>Probíhá plánovaná odstávka systému NEN</h1>'
    '<p>Omlouváme se, systém je dočasně nedostupný.</p></body></html>'
).encode("utf-8")

# A 200 that IS the NEN application shell — right site, right chrome, right
# tile labels, and NO state. The one an HTML-marker-only guard would wave
# through, and the reason parse_meta runs first.
NO_META_HTML = _chrome("", _TILE.format(label=X.HTML_MARKER, value=""))

BROKEN_META_HTML = _chrome(
    '<meta name="initialReduxState" content="%7B%22detailObjectStore%22:%7B">',
    _TILE.format(label=X.HTML_MARKER, value="x"))


# ══ CASES ═══════════════════════════════════════════════════════════════════

def write(tmp, name, data):
    p = os.path.join(tmp, name)
    with open(p, "wb") as fh:
        fh.write(data)
    return p


def guard_cases(tmp):
    """(kind, label, must_reject, path, kod_or_sid)."""
    yield ("detail", "login page served as the detail page", True,
           write(tmp, "d-login.html", LOGIN_HTML), None)
    yield ("detail", "maintenance notice served as the detail page", True,
           write(tmp, "d-503.html", MAINTENANCE_HTML), None)
    yield ("detail", "NEN's own shell, tiles rendered, NO meta JSON", True,
           write(tmp, "d-nometa.html", NO_META_HTML), None)
    yield ("detail", "meta present but truncated — does not parse as JSON", True,
           write(tmp, "d-broken.html", BROKEN_META_HTML), None)
    yield ("detail", "meta + object:null (the shell for an unassigned number)", True,
           write(tmp, "d-null.html", detail_page(PTK_OBJ, null_object=True)), None)
    yield ("detail", "meta object present but the tile label is missing", True,
           write(tmp, "d-notile.html", detail_page(PTK_OBJ, marker=False)), None)
    yield ("detail", "a healthy page for ANOTHER kod (redirect)", True,
           write(tmp, "d-other.html", detail_page(PTK_OBJ)), "N006/26/P00000999")
    yield ("detail", "THE GOOD BODY — a real consultation", False,
           write(tmp, "d-good.html", detail_page(PTK_OBJ)), "N006/26/P00000122")
    yield ("detail", "a real Průzkum trhu page — a procedure, so the GUARD accepts", False,
           write(tmp, "d-pruzkum.html", detail_page(PRUZKUM_OBJ)), "N006/26/P00000002")
    yield ("subject", "login page served as the buyer page", True,
           write(tmp, "s-login.html", LOGIN_HTML), None)
    yield ("subject", "buyer page whose object carries no ico", True,
           write(tmp, "s-noico.html", subject_page({"nazev": None}, SUBJECT_SID)), SUBJECT_SID)
    yield ("subject", "a healthy buyer page for ANOTHER subject id", True,
           write(tmp, "s-other.html", subject_page(SUBJECT_OBJ, SUBJECT_SID)), "12345678")
    yield ("subject", "THE GOOD BODY — the buyer page", False,
           write(tmp, "s-good.html", subject_page(SUBJECT_OBJ, SUBJECT_SID)), SUBJECT_SID)


def run_guard(kind, path, want):
    try:
        if kind == "detail":
            o = X.guard_detail(path, want)
            return False, f"accepted {X.collapse(o.get('kod'))} / {X.collapse(o.get('druhZRNazev'))}"
        return False, "accepted ico=" + X.guard_subject(path, want)["ico"]
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


def contact_control():
    """THE POSITIVE CONTROL. Every 'no contact survived' check below is a
    negative result, and a negative result over an input that never carried one
    proves nothing at all."""
    yield "control: the placeholder mailbox DOES match EMAIL_RE", bool(X.EMAIL_RE.search(CONTACT_MAIL))
    yield "control: the placeholder number DOES match PHONE_RE", bool(X.PHONE_RE.search(CONTACT_TEL))
    yield "control: the contact-carrying fixture DOES trip has_contact()", has_contact(CONTACT_OBJ)


def fold_checks(tmp):
    """(label, ok) over fold() — the entry point fetch_nen_ptk.sh calls."""
    paths = [write(tmp, "f-ptk.html", detail_page(PTK_OBJ)),
             write(tmp, "f-pruzkum.html", detail_page(PRUZKUM_OBJ)),
             write(tmp, "f-short.html", detail_page(SHORT_OBJ)),
             write(tmp, "f-contact.html", detail_page(CONTACT_OBJ)),
             write(tmp, "f-nobuyer.html", detail_page(NO_BUYER_OBJ))]
    out = os.path.join(tmp, "nenptk-consultations.jsonl")
    icos = {"74603670": "00262340", "96530994": "71185194"}
    s = X.fold(paths, out, icos)
    rows = {r["kod"]: r for r in
            (json.loads(line) for line in open(out, encoding="utf-8"))}

    yield "fold: 5 guarded pages -> 2 consultations, 3 dropped", (
        s["pages"] == 5 and s["consultations"] == 2 and s["dropped"] == 3)
    yield "fold: the Průzkum trhu row is dropped as not-a-consultation, and SAID SO", (
        s["dropped_by_reason"].get(X.NOT_CONSULTATION) == 1
        and any("N006/26/P00000002: " + X.NOT_CONSULTATION in d for d in s["dropped_detail"])
        and "N006/26/P00000002" not in rows)
    yield "fold: the drop names the druh that caused it", any(
        "Průzkum trhu" in d for d in s["dropped_detail"])
    yield "fold: the 33-char popis is dropped as no-stated-need (bar is %d)" % X.MIN_POPIS, (
        s["dropped_by_reason"].get(X.NO_STATED_NEED) == 1
        and "N006/26/P00000131" not in rows)
    yield "fold: the row naming no buyer is dropped as no-owner", (
        s["dropped_by_reason"].get(X.NO_OWNER) == 1
        and "N006/26/P00000133" not in rows)

    r = rows.get("N006/26/P00000122", {})
    yield "row: kod and buyer are the real ones", (
        r.get("kod") == "N006/26/P00000122"
        and r.get("buyer") == "Statutární město Jablonec nad Nisou")
    yield "row: buyer_id collapsed from the int, IČO joined off the fetcher's map", (
        r.get("buyer_id") == "74603670" and r.get("ico") == "00262340")
    yield "row: druh, cpv, date and deadline off the object", (
        r.get("druh") == X.PTK_DRUH and r.get("cpv") == "45212300-9"
        and r.get("date") == "2026-05-15" and r.get("deadline") == "2026-05-27")
    yield "row: url is the detail page, never a /file* path", (
        r.get("url") == "https://nen.nipez.cz/verejne-zakazky/detail-zakazky/N006-26-P00000122"
        and "/file" not in r.get("url", ""))
    yield "row: HTML stripped from popis, tags leave a space behind", (
        "<p>" not in r.get("popis", "") and "domu. Předmětem PKT" in r.get("popis", ""))
    yield "row: popis <= %d chars" % X.MAX_POPIS, len(r.get("popis", "")) <= X.MAX_POPIS
    yield "row: no email or phone in the real row either", not has_contact(r)
    yield "row: exactly the payload keys, no osoba* leaked through", set(r) == {
        "kod", "nazev", "druh", "buyer", "buyer_id", "ico", "popis", "cpv",
        "date", "deadline", "url"}

    c = rows.get("N006/26/P00000132", {})
    yield "row: the contact-carrying record IS staged (the need survives the cut)", bool(c)
    yield "row: no email and no phone anywhere in it", not has_contact(c)
    yield "row: the contact SENTENCE is gone, the need it sat next to is not", (
        "Dotazy zasílejte" not in c.get("popis", "")
        and "jeden účastník" in c.get("popis", ""))
    yield "row: the allowlist cut every osoba* key the object carried", not any(
        k.lower().startswith("osoba") for k in c) and "Novák" not in json.dumps(c, ensure_ascii=False)

    dup = X.fold(paths + [write(tmp, "f-dup.html", detail_page(PTK_OBJ))], out, icos)
    yield "fold: a body seen twice is written once and counted as a duplicate", (
        dup["consultations"] == 2 and dup["duplicates"] == 1)
    # Both kept rows are Jablonec — the same buyer, counted once, and both
    # joined to an IČO off the map the fetcher built.
    yield "fold: buyers deduped (both kept rows are one buyer), no_ico 0", (
        dup["buyers"] == 1 and dup["no_ico"] == 0)
    yield "fold: an unguardable body stops the fold rather than being folded", _raises(
        X.fold, [write(tmp, "f-login.html", LOGIN_HTML)], out, icos)

    return rows


def _raises(fn, *a, **kw):
    try:
        fn(*a, **kw)
        return False
    except X.ContractViolation:
        return True


def extract_checks(rows):
    today = datetime.date(2026, 9, 4)
    row = rows["N006/26/P00000122"]
    rec = X.extract_nen_ptk(row, "nenptk", today)
    yield "extract_nen_ptk: returns a record", rec is not None
    if not rec:
        return
    missing = [k for k in MECHANICAL_KEYS + SHAPE_KEYS if k not in rec]
    yield f"extract: every mechanical REQUIRED_OUT + shape key present (missing: {missing})", not missing
    yield "extract: id is nenptk-<kod lowercased> and matches ^[a-z]{2,10}-[\\w.-]+$", (
        rec["id"] == "nenptk-n006-26-p00000122" and bool(ID_RE.match(rec["id"])))
    yield "extract: source=nen-ptk, evidence_type=asks", (
        rec["source"] == "nen-ptk" and rec["evidence_type"] == "asks")
    yield "extract: top-level owner is the buyer — the asks ledger's required field", (
        rec["owner"] == "Statutární město Jablonec nad Nisou"
        and rec["owner"] == rec["entity_native"])
    yield "extract: urgency_date is None though the row carries a deadline", (
        row["deadline"] == "2026-05-27" and rec["urgency_date"] is None)
    yield "extract: sector None, money_eur None, money_note ''", (
        rec["sector"] is None and rec["money_eur"] is None and rec["money_note"] == "")
    yield "extract: date off the row, url off the row", (
        rec["date"] == "2026-05-15" and rec["url"] == row["url"])
    # MEASURED, not hypothetical: N006/26/P00000006 (Vězeňská služba ČR) carries
    # `datumProfil: null` on the live surface, so `date` reaches the extractor
    # empty on roughly one row in sixteen. The run date is the honest fallback —
    # the day the register saw it — and it must never be left blank, because
    # `date` is a REQUIRED_OUT field.
    yield "extract: a row with no date falls back to the run date", (
        X.extract_nen_ptk(dict(row, date=""), "nenptk", today)["date"] == "2026-09-04")
    yield "extract: excerpt <= 400 and quote_parts verifiable against the row", (
        len(rec["excerpt"]) <= 400 and len(rec["quote_parts"]) == 2
        and all(q in (row["nazev"] + " " + row["popis"]) for q in rec["quote_parts"]))
    yield "extract: notes carries the CPV and nothing structured beyond it", (
        rec["notes"] == "CPV 45212300-9")
    yield "extract: the same input yields the same id twice", (
        X.extract_nen_ptk(row, "nenptk", today)["id"]
        == X.extract_nen_ptk(row, "nenptk", datetime.date(2027, 1, 1))["id"] == rec["id"])
    yield "extract: no email or phone anywhere in the record", not has_contact(rec)

    crec = X.extract_nen_ptk(rows["N006/26/P00000132"], "nenptk", today)
    yield "extract: the contact-carrying record stays contact-free end to end", (
        crec is not None and not has_contact(crec))
    yield "extract: notes empty when the row carries no CPV", (
        X.extract_nen_ptk(dict(row, cpv=""), "nenptk", today)["notes"] == "")
    yield "extract: a row naming no buyer is REFUSED — no 'NEN' fallback owner", (
        X.extract_nen_ptk(dict(row, buyer=""), "nenptk", today) is None)
    yield "extract: a row whose popis is a label is refused again at the record", (
        X.extract_nen_ptk(dict(row, popis="Rekonstrukce vily."), "nenptk", today) is None)
    yield "extract: a row with no kod or no title is refused", all(
        X.extract_nen_ptk(dict(row, **{k: ""}), "nenptk", today) is None
        for k in ("kod", "nazev"))
    # A payload row missing its url is not a missing record: the url is a
    # pure function of the kod, and the kod is the identity.
    yield "extract: a row with no url rebuilds it from the kod", (
        X.extract_nen_ptk(dict(row, url=""), "nenptk", today)["url"] == row["url"])
    yield "extract: there is no fallback-owner constant to fall back to", not any(
        n for n in dir(X) if "FALLBACK" in n.upper())


PAYLOAD_NAME = "nenptk-consultations.jsonl"


def _nen_at(normalize):
    """Index of the ("nen", "nen") row in FILE_FEED_TOKENS."""
    return [t for t, _ in normalize.FILE_FEED_TOKENS].index("nen")


def _resolves_with_token(normalize):
    """feed_for_file() with the token inserted where the fetcher's footer says
    it must go. In memory only — this test edits no file, and normalize.py is
    the orchestrator's to change."""
    live = normalize.FILE_FEED_TOKENS
    at = _nen_at(normalize)
    try:
        normalize.FILE_FEED_TOKENS = live[:at] + [("nenptk", "nen-ptk")] + live[at:]
        return normalize.feed_for_file(PAYLOAD_NAME)
    finally:
        normalize.FILE_FEED_TOKENS = live


def _cli(argv):
    """Run the extractor's CLI in-process. Returns (rc, stdout)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = X.main(argv)
    return rc, buf.getvalue().strip()


def cli_checks(tmp):
    """THE SEAM THE FETCHER ACTUALLY USES. fetch_nen_ptk.sh never imports this
    module — it shells out to four subcommands and reads their exit status,
    their stdout and, for `fold`, six specific jq paths. A library-only test
    would pass with the argv wiring broken."""
    good = write(tmp, "c-good.html", detail_page(PTK_OBJ))
    subj = write(tmp, "c-subj.html", subject_page(SUBJECT_OBJ, SUBJECT_SID))
    login = write(tmp, "c-login.html", LOGIN_HTML)

    rc, out = _cli(["guard", good, "--kod", "N006/26/P00000122"])
    yield "cli guard: rc 0 and '<kod>\\t<druh>' on stdout", (
        rc == 0 and out == "N006/26/P00000122\tPředběžná tržní konzultace")
    rc, out = _cli(["guard", login])
    # The fetcher branches on the STATUS (`if ! g="$(… guard …)"`), so a
    # non-zero rc is the whole contract; the message is what it echoes.
    yield "cli guard: a wrong body exits non-zero and says why", (
        rc != 0 and out.startswith("CONTRACT VIOLATION:"))
    rc, out = _cli(["buyer", good])
    yield "cli buyer: prints the digits the fetcher's case-guard accepts", (
        rc == 0 and out == "74603670")
    rc, out = _cli(["ico", subj, "--sid", SUBJECT_SID])
    yield "cli ico: prints the IČO", rc == 0 and out == "71185194"
    rc, out = _cli(["ico", login])
    # fetch_nen_ptk.sh: `case "$ico" in CONTRACT*|*[!0-9]*) ico="" ;;` — the
    # refusal must start with CONTRACT so a login page never becomes an IČO.
    yield "cli ico: a wrong body exits non-zero AND starts with CONTRACT", (
        rc != 0 and out.startswith("CONTRACT"))

    out_jsonl = os.path.join(tmp, "cli-nenptk-consultations.jsonl")
    imap = write(tmp, "icos.json", b'{"74603670": "00262340"}')
    pruzkum = write(tmp, "c-pruzkum.html", detail_page(PRUZKUM_OBJ))
    # --paths-from is how the fetcher hands the guarded bodies over; a path
    # with a space in it is the case an unquoted $(cat …) used to break.
    listfile = write(tmp, "good with space.list",
                     ("%s\n%s\n" % (good, pruzkum)).encode("utf-8"))
    rc, out = _cli(["fold", "--out", out_jsonl, "--ico-map", imap,
                    "--paths-from", listfile])
    summary = json.loads(out) if rc == 0 else {}
    yield "cli fold: rc 0 and one JSON object on stdout", rc == 0 and bool(summary)
    yield "cli fold: carries every key fetch_nen_ptk.sh reads with jq", set(summary) >= {
        "pages", "consultations", "dropped", "buyers", "no_ico",
        "dropped_by_reason", "dropped_detail"}
    yield "cli fold: wrote the payload the fetcher moves into place", (
        summary.get("consultations") == 1
        and len(open(out_jsonl, encoding="utf-8").read().splitlines()) == 1)


def cross_check_normalize():
    """Drift detection against the file that will import us."""
    try:
        import normalize  # noqa: F401
    except Exception as e:  # noqa: BLE001
        print(f"[warn] normalize.py not importable here ({e.__class__.__name__}: {e}); "
              "REQUIRED_OUT / GDPR patterns checked against the literal copies only")
        return 0
    bad = 0
    for label, ok in (
        ("normalize.REQUIRED_OUT equals the literal held here",
         tuple(normalize.REQUIRED_OUT) == REQUIRED_OUT),
        ("EMAIL_RE copy matches normalize.EMAIL_RE",
         X.EMAIL_RE.pattern == normalize.EMAIL_RE.pattern),
        ("PHONE_RE copy matches normalize.PHONE_RE",
         X.PHONE_RE.pattern == normalize.PHONE_RE.pattern),
        ("`owner` is on normalize's ledger allowlist",
         "owner" in normalize.LEDGER_ALLOWLIST),
        # THE ORDERING PROOF. FILE_FEED_TOKENS is FIRST-MATCH-WINS and
        # `nenptk-consultations.jsonl` CONTAINS the existing `nen` token, so
        # ("nenptk", "nen-ptk") has to sit ABOVE ("nen", "nen"). Both halves are
        # checked: that nothing already above `nen` claims the name (so the
        # insertion point is free), and that the insertion actually wins.
        ("no token above `nen` claims nenptk-consultations.jsonl",
         not [t for t, _ in normalize.FILE_FEED_TOKENS[:_nen_at(normalize)]
              if t in PAYLOAD_NAME]),
        ("with (nenptk, nen-ptk) above (nen, nen) the payload resolves to nen-ptk",
         _resolves_with_token(normalize) == "nen-ptk"),
    ):
        print(f"[{'ok  ' if ok else 'FAIL'}] xchk  {label}")
        bad += 0 if ok else 1
    print(f"[info] xchk  feed_for_file({PAYLOAD_NAME!r}) resolves to "
          f"{normalize.feed_for_file(PAYLOAD_NAME)!r} as normalize.py stands right now")
    return bad


def main():
    bad = total = 0
    with tempfile.TemporaryDirectory() as tmp:
        cases = list(guard_cases(tmp))
        width = max(len(c[1]) for c in cases)
        for kind, label, must_reject, path, want in cases:
            rejected, msg = run_guard(kind, path, want)
            ok = (rejected == must_reject)
            bad += 0 if ok else 1
            total += 1
            print(f"[{'ok  ' if ok else 'FAIL'}] {kind:7s} {label:<{width}}  -> "
                  f"{'REFUSED' if rejected else 'accepted'}: {msg[:96]}")
        print()
        for label, ok in contact_control():
            bad += 0 if ok else 1
            total += 1
            print(f"[{'ok  ' if ok else 'FAIL'}] ctrl    {label}")
        print()
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
        for label, ok in extract_checks(rows):
            bad += 0 if ok else 1
            total += 1
            print(f"[{'ok  ' if ok else 'FAIL'}] extract {label}")
        print()
        for label, ok in cli_checks(tmp):
            bad += 0 if ok else 1
            total += 1
            print(f"[{'ok  ' if ok else 'FAIL'}] cli     {label}")
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
