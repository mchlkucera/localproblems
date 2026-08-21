#!/usr/bin/env python3
"""
nen_extract.py — the NEN payload reader, and the normalize.py extractor for it.

WHAT THIS TALKS TO, AND WHY IT IS NOT THE HTML LISTING
======================================================
`docs/feeds-status.md` probed NEN through the rendered listing at
`https://nen.nipez.cz/verejne-zakazky` (200, 50 rows/page, 5,545 pages). That
route works and is same-day fresh, but it is an unversioned HTML template with
no declared field names, dates rendered as `24. 08. 2026`, and a matrix-parameter
URL shape (`p:vz:typVZ=…`) that nobody publishes a contract for.

MEASURED 2026-08-21, there is a better one. MMR publishes the Registr veřejných
zakázek as documented open data at

    https://isvz.nipez.cz/sites/default/files/content/opendata-rvz/VZ-<MM>-<YYYY>.zip

and the page that lists it says, in as many words, that NEN is one of its four
sources (VVZ, NEN, Tender arena, TENDERMARKET). What that buys us:

  * A VERSION NUMBER INSIDE THE PAYLOAD. The JSON opens
    `{"obdobi_od":…,"obdobi_do":…,"verze":"2.10.1","data":[…]}`. The interface
    version travels with the bytes, so a format change announces itself instead
    of being inferred from a parse that started returning nothing.
  * A PUBLISHED SCHEMA, versioned alongside it
    (`/centrum-podpory/napoveda/webovy-portal-isvz/open-data/nova-open-data-dokumentace-json-formatu`
    currently ships dokumentace_2.10.1.zip back to 2.4.0).
  * ETag + Last-Modified on the ZIP, so the fetch is a conditional GET.
  * Stable machine field names and ISO-8601 timestamps — no `24. 08. 2026`.
  * The below-threshold slice IS there. Measured on VZ-07-2026: 33,855
    contracts, 20,286 carrying a NEN identifier, 18,403 `Veřejná zakázka malého
    rozsahu` and 3,838 `Podlimitní` — i.e. the small-contract layer TED does not
    publish is the MAJORITY of this file, not a fringe of it.
  * The buyer IČO is present on 100% of sampled records
    (`zadavatele[].subjekt.ico`, 1500/1500). feeds-status.md credits NEN with no
    join axis; through this interface it has one.

WHAT WE TRADED AWAY: FRESHNESS, AND IT IS NOT A SMALL TRADE.
The files are published monthly, on the 5th of the following month (measured:
VZ-07-2026 Last-Modified 2026-08-02, VZ-08-2026 still 404 on 2026-08-21). A
tender that opens on the 2nd of a month is therefore visible here ~34 days
later, by which time a below-threshold bid deadline has usually passed. This
feed records that a need EXISTED and what it cost — with the awarded price and
the winning supplier, which the live listing does not carry — and it cannot be
used to bid. If someone later wants bid-time alerting, that is a SECOND fetcher
against the HTML listing with its own registry key, not a change to this one:
the two have different contracts, different failure modes and different yields,
and folding them together would hide which one broke.

PERSONAL DATA — THE REASON THIS FILE BUILDS ITS OUTPUT FIELD BY FIELD.
The source carries the name and e-mail of the natural person who submitted each
bid: `…ucastnici[].podani[].osoba_ktera_provedla_podani[].{jmeno,prijmeni,email}`
appears on 2,995 of the first 3,000 records, plus the same three under
`zpetvzeti_podani[].osoba_ktera_provedla_zpetvzeti[]`. So `select()` NEVER
copies a source object. It names every field it keeps, one at a time — an
allowlist by construction, which fails closed when MMR adds a column, whereas
anything shaped like "copy the record then delete the bad keys" fails open on
exactly the release nobody read the changelog for. data/raw/ is gitignored, but
that is not the safeguard: `quote` is captured from this payload and the ledgers
are public and append-only.

USED FROM TWO PLACES:
  scripts/fetch_nen.sh    — `python3 scripts/nen_extract.py read …` to turn a
                            downloaded ZIP into <raw>/nen-<YYYY-MM>.json
  scripts/normalize.py    — `extract_nen()` as EXTRACTORS["nen"] (HAND-OFF: two
                            lines, see the note on extract_nen below)
"""

import argparse
import collections
import json
import os
import re
import sys
import zipfile

# --------------------------------------------------------------------------
# 1. THE SOURCE CONTRACT — MODE A, evaluated at FETCH time.
# --------------------------------------------------------------------------
#
# Mode A is "a good transfer carrying the wrong body": a 200 serving a login
# page, an error document, a maintenance notice, an empty result that looks like
# a result. The transport receipt cannot see any of those — they are all 200s.
#
# Deliberately checked HERE and not only in the registry `contract`, which
# normalize.py evaluates. normalize runs a session later, against whatever is on
# disk; by then the wrong body has already been written into data/raw/ and
# recorded as a successful fetch. Checking at fetch time means a wrong body is
# never stored and never counted, and the receipt says `error`, not `ok`.
#
# Every assertion below is a MEASURED fact about the real payload, not a guess:
#   * ZIP magic PK\x03\x04              — isvz's 404 serves text/html, 158 kB of it
#   * exactly one .json member           — measured: 1 entry, VZ-07-2026.json
#   * a `verze` matching \d+\.\d+\.\d+   — measured "2.10.1"
#   * `obdobi_od`/`obdobi_do` naming the month we asked for — catches a silently
#     substituted or mis-linked file, which no byte count can catch
#   * a `data` array that is a JSON array
#   * at least MIN_RECORDS objects in it — catches the empty-result-set case
CONTRACT_MIN_RECORDS = 1000       # VZ-07-2026 held 33,855; a month under 1,000 is a lie
ZIP_MAGIC = b"PK\x03\x04"
VERZE_RE = re.compile(r"^\d+\.\d+(\.\d+)?$")


class ContractViolation(Exception):
    """A 200 carrying the wrong body. Louder than a non-200, by design."""


def assert_zip(path):
    """Cheapest possible Mode-A check: is this even a ZIP? Runs before unzip."""
    with open(path, "rb") as fh:
        magic = fh.read(4)
    if magic != ZIP_MAGIC:
        head = open(path, "rb").read(200).decode("utf-8", "replace")
        raise ContractViolation(
            f"not a zip (magic {magic!r}); first 200 bytes: {head[:200]!r}")
    try:
        zf = zipfile.ZipFile(path)
    except zipfile.BadZipFile as e:
        raise ContractViolation(f"corrupt zip: {e}") from e
    members = [i for i in zf.infolist() if i.filename.lower().endswith(".json")]
    if len(members) != 1:
        raise ContractViolation(
            f"expected exactly 1 .json member, found {len(members)}: "
            f"{[i.filename for i in zf.infolist()][:5]}")
    return zf, members[0].filename


def assert_header(header, want_period=None):
    """`header` is the {obdobi_od, obdobi_do, verze} prologue read off the stream."""
    verze = str(header.get("verze") or "")
    if not VERZE_RE.match(verze):
        raise ContractViolation(f"no interface version in payload (verze={verze!r})")
    od, do = str(header.get("obdobi_od") or ""), str(header.get("obdobi_do") or "")
    if not od[:7] or not do[:7]:
        raise ContractViolation(f"no period declared (obdobi_od={od!r} obdobi_do={do!r})")
    if want_period and od[:7] != want_period:
        raise ContractViolation(
            f"payload declares period {od[:7]}, we asked for {want_period} — "
            "wrong file served")
    return verze, od[:7]


# --------------------------------------------------------------------------
# 2. STREAMING READER
# --------------------------------------------------------------------------
#
# VZ-07-2026.json is 465 MB uncompressed from a 63 MB ZIP. json.load() on that
# costs several GB of RSS, and extracting it to data/raw/ would put 465 MB a
# month into a directory the repo treats as a 28-day cache. So the members are
# read from INSIDE the ZIP as a stream and never land on disk: brace-counting
# over the `"data":[` array yields one contract object at a time.
#
# Brace counting is string-aware and escape-aware. It has to be — `popis_predmetu`
# is free Czech prose that routinely contains `{`, `}` and escaped quotes, and a
# naive counter desynchronises on the first one and then silently truncates the
# rest of the month.
#
# Measured cost: 45 s and flat memory for a full 33,855-contract month.

def stream_header_and_records(fh):
    """Yield (header_dict, iterator-of-contract-objects) off an open byte stream."""
    buf = b""
    while True:
        chunk = fh.read(1 << 20)
        if not chunk:
            raise ContractViolation('payload ended before a "data" array appeared')
        buf += chunk
        i = buf.find(b'"data"')
        if i >= 0:
            j = buf.find(b"[", i)
            if j >= 0:
                header = json.loads(
                    (buf[:i].rstrip().rstrip(b",") + b"}").decode("utf-8"))
                rest = buf[j + 1:]
                return header, _objects(fh, rest)
        if len(buf) > (8 << 20):
            raise ContractViolation('no "data" array in the first 8 MB of the payload')


def _objects(fh, buf):
    depth = 0
    in_str = False
    esc = False
    cur = bytearray()
    started = False
    while True:
        if not buf:
            buf = fh.read(1 << 20)
            if not buf:
                return
        for b in buf:
            c = b
            if started:
                cur.append(c)
            if in_str:
                if esc:
                    esc = False
                elif c == 0x5C:      # backslash
                    esc = True
                elif c == 0x22:      # "
                    in_str = False
                continue
            if c == 0x22:
                in_str = True
                continue
            if c == 0x7B:            # {
                if depth == 0:
                    started = True
                    cur = bytearray(b"{")
                depth += 1
            elif c == 0x7D:          # }
                depth -= 1
                if depth == 0:
                    yield json.loads(cur.decode("utf-8"))
                    started = False
                    cur = bytearray()
            elif c == 0x5D and depth == 0:   # ] closing "data"
                return
        buf = b""


# --------------------------------------------------------------------------
# 3. SELECTION + FIELD ALLOWLIST
# --------------------------------------------------------------------------

# Below the TED threshold is the whole point of this feed. `Nadlimitní` is
# EXCLUDED rather than merely deprioritised: those notices are already in the
# corpus as `ted-*` records, and carrying them here would double-count the same
# contract under two ids and two feeds — which is precisely the accounting bug
# feeds-status.md §6.2 documents on the `hlidac` source label.
BELOW_THRESHOLD = {
    "Veřejná zakázka malého rozsahu",
    "Podlimitní veřejná zakázka",
}

# CPV DIVISION (first two digits) -> CONVENTIONS.md sector. Same idea as
# normalize.py's CPV_SECTOR, but keyed on the code rather than on a payload
# filename: `payload_key_of()` only matches `^(ted|hlidac)-`, so an `nen-*.json`
# has no payload key and the sector has to come from the record itself.
CPV_DIVISION_SECTOR = {
    "09": "energy", "15": "retail-services", "18": "retail-services",
    "30": "b2b", "31": "energy", "32": "b2b", "33": "health",
    "34": "mobility", "35": "govtech", "39": "retail-services",
    "41": "environment", "42": "b2b", "44": "housing", "45": "housing",
    "48": "govtech", "50": "b2b", "51": "b2b", "55": "retail-services",
    "60": "mobility", "63": "mobility", "64": "b2b", "65": "energy",
    "66": "fintech", "70": "housing", "71": "housing", "72": "govtech",
    "73": "b2b", "75": "govtech", "76": "energy", "77": "environment",
    "79": "b2b", "80": "education", "85": "health", "90": "environment",
}


def sector_for_cpv(cpv):
    return CPV_DIVISION_SECTOR.get(str(cpv or "")[:2], "other")


def _first(seq):
    return seq[0] if isinstance(seq, list) and seq else {}


def _nen_code(vz):
    for t in vz.get("identifikatory_v_elektronickem_nastroji") or []:
        if (t or {}).get("kod_nastroje") == "NEN" and t.get("identifikator"):
            return t["identifikator"]
    return None


def _buyer(vz):
    """(nazev, ico, nuts) of the contracting authority. ORGANISATIONAL ONLY."""
    for zp in vz.get("zadavaci_postupy") or []:
        z = (zp.get("zadavatel_zadavaciho_postupu") or {}).get("zadavatele") or []
        for entry in z:
            s = entry.get("subjekt") or {}
            if s.get("nazev_subjektu"):
                return s.get("nazev_subjektu"), s.get("ico"), s.get("kod_NUTS")
    return None, None, None


def _procedures(vz):
    """Every zadávací postup on the contract, VZ-level and per-part."""
    out = list(vz.get("zadavaci_postupy") or [])
    for c in vz.get("casti_verejne_zakazky") or []:
        zp = c.get("zadavaci_postup_pro_cast")
        if zp:
            out.append(zp)
    return out


DEADLINE_KIND = "Lhůta pro podání nabídky"


def _bid_deadline(vz):
    best = None
    for zp in _procedures(vz):
        for l in zp.get("lhuty") or []:
            if (l or {}).get("druh_lhuty") == DEADLINE_KIND:
                d = str(l.get("datum_a_cas_konce_lhuty") or "")[:10]
                if d and (best is None or d > best):
                    best = d
    return best


def _started(vz):
    best = None
    for zp in _procedures(vz):
        d = str(zp.get("datum_zahajeni_zadavaciho_postupu") or "")[:10]
        if d and (best is None or d > best):
            best = d
    return best


def _state(vz):
    for zp in _procedures(vz):
        if zp.get("stav"):
            return zp["stav"]
    return None


def _estimated_czk(vz):
    """(czk, source_field). CZK is published pre-normalised by MMR."""
    v = vz.get("predpokladana_hodnota_bez_DPH_v_CZK")
    if v is not None:
        return v, "predpokladana_hodnota_bez_DPH_v_CZK"
    for c in vz.get("casti_verejne_zakazky") or []:
        v = c.get("predpokladana_hodnota_casti_bez_DPH_v_CZK")
        if v is not None:
            return v, "predpokladana_hodnota_casti_bez_DPH_v_CZK"
    return None, None


def _awarded(vz):
    """(czk, supplier_name, supplier_ico, contract_date) for the signed contract."""
    total, name, ico, when = None, None, None, None
    for zp in _procedures(vz):
        vys = zp.get("vysledek") or {}
        for sml in vys.get("smlouva") or []:
            v = sml.get("hodnota_smluvni_ceny_bez_DPH")
            cur = str(sml.get("hodnota_smluvni_ceny_mena") or "CZK").upper()
            if v is not None and cur == "CZK":
                total = (total or 0) + float(v)
            when = when or str(sml.get("datum_uzavreni_smlouvy") or "")[:10] or None
        for vyb in vys.get("vybrani_dodavatele_zadavaciho_postupu") or []:
            s = vyb.get("subjekt") or {}
            if s.get("nazev_subjektu") and not name:
                name, ico = s.get("nazev_subjektu"), s.get("ico")
    return total, name, ico, when


QUOTE_MAX = 300

# THE SECOND PERSONAL-DATA LAYER, AND IT IS NOT HYPOTHETICAL HERE.
# The field allowlist above governs WHICH fields we keep. This governs what is
# INSIDE one of them, because `popis_predmetu` is free prose written by a
# municipal officer and they put their colleagues in it. MEASURED on the 3,868
# selected contracts of VZ-07-2026: 0 e-mail addresses, but 8 records carrying a
# named person and a phone number mid-sentence, e.g.
#   "…osoba oprávněná k převzetí dodávky: <name>, tel.: 498 016 160, 777 324 448."
#
# Left alone this is not a leak — normalize.py's gdpr_violations() scans the
# allowlisted view and REFUSES the whole record, failing closed exactly as
# designed. But refusing 8 otherwise-good tenders to avoid 8 phone numbers is a
# worse outcome than not offering the phone numbers in the first place, and the
# refusal happens a session later where nobody connects it to this field. So the
# snippet is cut at the first contact match and the tender survives with a
# shorter, still-verbatim quote. A PREFIX OF A VERBATIM STRING IS VERBATIM, which
# is why truncating is legitimate here and redacting mid-string would not be.
#
# Patterns are copied from normalize.py:150-161 ON PURPOSE rather than imported:
# this module must be able to refuse contact data while running inside
# fetch_nen.sh, where normalize.py is not in play at all. Keep them in step.
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)


def contact_free(s):
    """The longest leading run of `s` that contains no e-mail and no phone."""
    s = str(s or "")
    cut = len(s)
    for rx in (_EMAIL_RE, _PHONE_RE):
        m = rx.search(s)
        if m:
            cut = min(cut, m.start())
    if cut == len(s):
        return s
    # Back off to the last sentence break before the match so the snippet ends
    # somewhere a reader would end it, not mid-clause.
    head = s[:cut]
    stop = max(head.rfind(". "), head.rfind("? "), head.rfind("! "))
    return (head[:stop + 1] if stop > 40 else head).rstrip(" ,;:-")


def trim_quote(s):
    """<=300 chars, whitespace collapsed, cut on a word boundary.

    CONVENTIONS.md forbids an ellipsis inside a number, and normalize.py verifies
    the quote as a literal substring BEFORE truncating the join to 300. Trimming
    here, on a word boundary, means the string that lands in the payload is the
    string that lands in the ledger — so the substring test and the format law
    are satisfied by the same bytes rather than by two hopeful halves.
    """
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    if len(s) <= QUOTE_MAX:
        return s
    cut = s[:QUOTE_MAX]
    sp = cut.rfind(" ")
    return (cut[:sp] if sp > QUOTE_MAX // 2 else cut).rstrip(" ,;:-")


def select(vz, since=None):
    """One source contract -> one allowlisted payload item, or None.

    EVERY OUTPUT KEY IS NAMED. Nothing is copied wholesale from `vz`; see the
    personal-data note at the top of this file.
    """
    code = _nen_code(vz)
    if not code:
        return None
    typ = vz.get("typ_verejne_zakazky_dle_vyse_predpokladane_hodnoty")
    if typ not in BELOW_THRESHOLD:
        return None
    started = _started(vz)
    # The monthly file is a CHANGEFEED, not a month of new tenders: it carries
    # every contract RVZ touched in that period, including 2024 procedures that
    # merely gained a document. MEASURED on VZ-07-2026, the first VZMR in the
    # file started 2024-02. Without this window the feed re-proposes years of old
    # contracts on every run; they would all be dropped by seen.txt after the
    # first pass, but the run would report a yield it did not really produce.
    if since and (not started or started < since):
        return None

    predmet = vz.get("predmet") or {}
    cpv = predmet.get("hlavni_kod_CPV")
    if not cpv:
        for c in vz.get("casti_verejne_zakazky") or []:
            cpv = ((c.get("predmet") or {}).get("hlavni_kod_CPV"))
            if cpv:
                break
    nuts = None
    for m in predmet.get("mista_plneni") or []:
        if (m or {}).get("nuts"):
            nuts = m["nuts"]
            break

    buyer, buyer_ico, buyer_nuts = _buyer(vz)
    est, est_field = _estimated_czk(vz)
    awarded, supplier, supplier_ico, signed = _awarded(vz)
    nazev = contact_free(re.sub(r"\s+", " ", str(vz.get("nazev_verejne_zakazky") or "")).strip())
    popis = trim_quote(contact_free(predmet.get("popis_predmetu") or ""))

    return {
        # identity
        "nen_kod": code,
        "rvz_id": vz.get("identifikator_NIPEZ"),
        "odkaz": f"https://nen.nipez.cz/verejne-zakazky/detail-zakazky/{code.replace('/', '-')}",
        # subject
        "nazev": nazev,
        "popis": popis,
        "cpv": cpv,
        "nuts": nuts or buyer_nuts,
        "druh": vz.get("druh_verejne_zakazky"),
        "typ": typ,
        "rezim": vz.get("rezim_verejne_zakazky"),
        "stav": _state(vz),
        # buyer — organisational identifiers only
        "zadavatel": buyer,
        "zadavatel_ico": buyer_ico,
        # dates
        "datum_zahajeni": started,
        "lhuta_nabidky": _bid_deadline(vz),
        "casova_znacka": str(vz.get("casova_znacka") or "")[:10] or None,
        # money
        "hodnota_czk": est,
        "hodnota_zdroj": est_field,
        "smluvni_cena_czk": awarded,
        "datum_smlouvy": signed,
        "dodavatel": supplier,
        "dodavatel_ico": supplier_ico,
        # the verbatim snippet, already format-legal — see trim_quote()
        "citace": trim_quote(popis or nazev),
    }


# --------------------------------------------------------------------------
# 4. THE normalize.py EXTRACTOR
# --------------------------------------------------------------------------
#
# HAND-OFF (scripts/normalize.py is not this worker's file). Two lines:
#
#     from nen_extract import extract_nen          # sys.path[0] is scripts/
#     EXTRACTORS = {…, "nen": extract_nen, …}
#
# WHY IT CANNOT KEEP THE CURRENT WIRING. normalize.py:699 maps
# `"nen": extract_hlidac`. extract_hlidac hard-codes `id = f"hlidac-{nid}"` and
# `source = "hlidac"`, so every record this feed produced would be filed under
# Hlídač — which is EXACTLY the live defect feeds-status.md §6.2 measures: 296
# `nen-*` records carrying `source: "hlidac"`, making the one auth-blocked feed
# look like the healthiest tenders source in the repo at 4x its true yield.
# Leaving the mapping in place would grow that error rather than stop it. The
# existing 296 are NOT retro-edited — the ledgers are append-only.

def extract_nen(item, payload_key, today):
    """Signature and return shape are normalize.py's, not ours."""
    code = item.get("nen_kod")
    if not code:
        return None
    czk = item.get("smluvni_cena_czk")
    src = "smluvni_cena_czk (awarded, excl. VAT)"
    if czk is None:
        czk = item.get("hodnota_czk")
        src = f"{item.get('hodnota_zdroj')} (estimated, excl. VAT)"
    money, note = None, ""
    try:
        if czk is not None and float(czk) != 0.0:
            money = round(float(czk) / 25.0)   # CZK_PER_EUR, normalize.py:64
            note = f"{float(czk):,.0f} CZK — {src} — at a fixed 25.0 CZK/EUR"
    except (TypeError, ValueError):
        pass

    nazev = item.get("nazev") or ""
    buyer = item.get("zadavatel") or ""
    return {
        "id": f"nen-{str(code).replace('/', '-')}",
        "source": "nen",
        "evidence_type": "tenders",
        "url": item.get("odkaz") or
               f"https://nen.nipez.cz/verejne-zakazky/detail-zakazky/{str(code).replace('/', '-')}",
        "date": item.get("datum_zahajeni") or item.get("casova_znacka") or "",
        "title_native": nazev,
        "entity_native": buyer,
        "sector": sector_for_cpv(item.get("cpv")),
        "money_eur": money,
        "money_note": note,
        # The bid deadline where the procedure is still open; otherwise no
        # mechanical urgency date at all and normalize hands urgency to the
        # model. A PAST deadline already returns None from score_urgency(), so
        # this only avoids proposing a date that means nothing.
        "urgency_date": item.get("lhuta_nabidky"),
        "quote_parts": [p for p in (item.get("citace"), nazev) if p],
        "excerpt": re.sub(r"\s+", " ", f"{nazev} — {buyer}").strip(),
    }


# --------------------------------------------------------------------------
# 5. CLI — driven by scripts/fetch_nen.sh
# --------------------------------------------------------------------------

def read_zip(path, out, want_period=None, since=None, limit=0):
    zf, member = assert_zip(path)
    kept, seen_total = [], 0
    tools = collections.Counter()
    with zf.open(member) as fh:
        header, records = stream_header_and_records(fh)
        verze, period = assert_header(header, want_period)
        for obj in records:
            vz = obj.get("verejna_zakazka") or {}
            if not vz:
                continue
            seen_total += 1
            for t in vz.get("identifikatory_v_elektronickem_nastroji") or []:
                tools[(t or {}).get("kod_nastroje")] += 1
            rec = select(vz, since=since)
            if rec:
                kept.append(rec)
                if limit and len(kept) >= limit:
                    break
    if seen_total < CONTRACT_MIN_RECORDS and not limit:
        raise ContractViolation(
            f"{seen_total} contracts in {os.path.basename(path)} — below the "
            f"{CONTRACT_MIN_RECORDS} floor; a month this thin is a wrong body, "
            "not a quiet month")
    if not tools.get("NEN"):
        raise ContractViolation(
            f"no NEN identifiers anywhere in {os.path.basename(path)} "
            f"(tools seen: {dict(tools)}) — this file is not carrying NEN")
    doc = {
        "feed": "nen",
        "source_interface": "isvz-rvz-opendata",
        "interface_version": verze,
        "period": period,
        "since": since,
        "contracts_in_file": seen_total,
        "nen_identifiers_in_file": tools.get("NEN", 0),
        "fetched": len(kept),
        "items": kept,
    }
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False)
    return doc


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("read", help="ZIP -> allowlisted <raw>/nen-<period>.json")
    r.add_argument("zip")
    r.add_argument("out")
    r.add_argument("--period", default=None, help="YYYY-MM the file must declare")
    r.add_argument("--since", default=None, help="drop procedures started before this ISO date")
    r.add_argument("--limit", type=int, default=0, help="stop after N kept (probe only)")
    c = sub.add_parser("check", help="run the source contract against a file and exit")
    c.add_argument("zip")
    c.add_argument("--period", default=None)
    a = ap.parse_args(argv)
    try:
        if a.cmd == "read":
            doc = read_zip(a.zip, a.out, a.period, a.since, a.limit)
            # items_fetched / items_kept, on one machine-readable line, because a
            # fetch that works while zero records reach the ledger is the failure
            # this project keeps finding.
            print(json.dumps({k: v for k, v in doc.items() if k != "items"},
                             ensure_ascii=False))
            return 0
        zf, member = assert_zip(a.zip)
        with zf.open(member) as fh:
            header, _ = stream_header_and_records(fh)
            verze, period = assert_header(header, a.period)
        print(json.dumps({"ok": True, "verze": verze, "period": period}))
        return 0
    except ContractViolation as e:
        print(f"CONTRACT VIOLATION: {e}", file=sys.stderr)
        return 65


if __name__ == "__main__":
    sys.exit(main())
