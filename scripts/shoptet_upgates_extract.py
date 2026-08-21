#!/usr/bin/env python3
"""
shoptet_upgates_extract.py — the mechanical half of scripts/fetch_shoptet.sh and
scripts/fetch_upgates.sh. Turns a saved marketplace page into a VENDOR-LOOKUP row.

═══ WHAT THIS PRODUCES, AND WHY IT IS NOT A SIGNAL ═══════════════════════════
An e-commerce add-on listing is not a dated event. It has no money attached, no
deadline, no counterparty, no publication date — it is a standing commercial
offer. Run one through `data/CONVENTIONS.md`'s objective rubric and every row
scores `money 0`, `urgency 0`, `scale 0-1`, which the materiality filter
(`money <= 1 AND scale <= 1 AND urgency == 0`) deletes. A signal-ledger feed
built on this surface would fetch ~625 items a run and write approximately
zero — SCRIPTED-SILENT by construction, not by accident.

So this is ENRICHMENT, the role `data/feeds.json` already carries for `ares`:
`role: enrichment`, `signal_source: null`, `evidence_type: null`,
`id_prefixes: []`, produces ZERO signals, exempt from AC-F1 totality. Its
consumer is the `gap` check, not the ledger — it is what finally makes
`checked: [app-stores]` (already in the closed CONVENTIONS.md vocabulary, used
0 times to date) a claim we can back.

Consequence worth stating: because nothing here reaches `data/signals/**`,
this program needs NO change to `scripts/normalize.py`'s LEDGER_ALLOWLIST and
puts NOTHING into an append-only public log that would need a quiet cleanup.

═══ GDPR — THE PART THAT MUST NOT BE GOT WRONG ═══════════════════════════════
Both marketplaces print a named individual's PHONE NUMBER and E-MAIL on every
add-on detail page. doplnky.shoptet.cz/hlidac-slev carries `+420 777 002 493`
and `info@jarabot.com`; doplnky.upgates.cz/detail/balikuj carries
`+420 739 338 337` and `info@balikuj.cz`. Reviews name the reviewer and their
own e-shop domain.

WE NEED THE VENDOR AND THE PRODUCT. WE DO NOT NEED A PERSON'S CONTACT DETAILS.
Three layers, all fail-closed:

  1. STRUCTURAL — the prose slice stops at the contact table. On Shoptet the
     text region is cut at the first of `<h3>Podpora</h3>`, `service-info-table`,
     `id="section-ratings"`, `rating-review`; on Upgates at `Poskytovatel`.
     The phone/e-mail rows and every review sit outside the slice, so the
     personal data is never read into a field in the first place.
  2. CONTENT — EMAIL_RE / PHONE_RE (transcribed verbatim from normalize.py so
     the two gates cannot drift) scan every string of the finished record.
  3. FAIL-CLOSED — a record with a surviving hit is DROPPED and counted, never
     written with the hit redacted. A redaction is a judgement; a drop is not.

REVIEWS ARE NOT EXTRACTED AT ALL. The brief called the reviewer's own e-shop
domain "a bonus customer-discovery signal" and it would be — but a review is
a named individual's published opinion tied to their business, and harvesting
those into a permanent table is a different product with a different legal
posture. Declined deliberately, not overlooked.

VENDOR NAMES. `scripts/normalize.py` publishes a counterparty name only when
LEGAL_FORM_RE proves it is a legal person, because 21.3% of registr-smluv
counterparties were natural persons. That exact test is WRONG for this corpus
and would break the deliverable: the marketplace prints trading names, so
`JARABOT` (JARABOT s.r.o. in ARES) carries no legal-form marker and would be
suppressed — losing the single vendor this whole build exists to prove it can
find. The field here is also different in kind: it is the name a business
publicly trades under on a public marketplace, not a contract counterparty.

So the test is INVERTED and made specific: publish unless the name looks like
a natural person. A name is suppressed when it carries no legal-form marker
AND (its first token is a Czech given name OR it carries an academic title).
Measured against the live author list (see --selftest): brand names survive,
`Adam Zátopek`, `Vít Michalek`, `Vojtěch Fárek`, `Zdeněk Dušátko`,
`Jakub Grác - JG-Media` and peers are suppressed. A suppressed vendor keeps
`vendor_id` and `vendor_url` — the join key and the clickable address survive,
exactly as normalize.py keeps the IČO when it drops the name.

Usage:
  shoptet_upgates_extract.py shoptet-catalog  <katalog.html> <out.jsonl>
  shoptet_upgates_extract.py shoptet-detail   <page.html> <url> <vendors.jsonl>
  shoptet_upgates_extract.py upgates-listing  <dir-of-listing-html> <out.jsonl>
  shoptet_upgates_extract.py upgates-detail   <page.html> <url>
  shoptet_upgates_extract.py merge            <out.jsonl> <in.jsonl>...
  shoptet_upgates_extract.py search           <lookup.jsonl> <czech terms...>
  shoptet_upgates_extract.py --selftest       [fixture-dir]
"""
import hashlib
import html as htmllib
import json
import os
import re
import sys
import unicodedata

# ── GDPR layer 2 ── TRANSCRIBED VERBATIM from scripts/normalize.py (which this
# program does not own and does not touch). Copied rather than imported on
# purpose: normalize.py is being edited by another agent, and a gate this
# important must not acquire a moving dependency mid-flight. If they diverge,
# normalize.py is authoritative and this copy is the one that is wrong.
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(
    r"(?:\+420\s?\d{3}\s?\d{3}\s?\d{3})"
    r"|(?:\+\d{1,3}\s?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{3,4})"
    r"|(?:\b(?:tel|phone|mobil|gsm|telefon)\.?\s*:?\s*\+?\d[\d\s.-]{7,})",
    re.I,
)

# Also transcribed from normalize.py. Used here as the FIRST of two tests, not
# the only one — see the header. A hit means "provably a legal person".
LEGAL_FORM_RE = re.compile(
    r"(?:^|[\s,.(])(?:"
    r"s\.?\s?r\.?\s?o|a\.?\s?s|spol|v\.?\s?o\.?\s?s|k\.?\s?s|s\.?\s?p"
    r"|o\.?\s?p\.?\s?s|z\.?\s?s|z\.?\s?ú|v\.?\s?v\.?\s?i"
    r"|družstvo|nadace|nadační|spolek|sdružení|svaz|komora|unie|asociace"
    r"|ústav|institut|akademie|univerzita|vysoká|škola|gymnázium|učiliště"
    r"|nemocnice|poliklinika|lékárna|banka|pojišťovna|fond|agentura|centrum"
    r"|ministerstvo|úřad|obec|město|městys|kraj|státní|národní|česká|český"
    r"|gmbh|ag|se|sa|nv|bv|oy|ab|sp\.?\s?z\.?\s?o\.?\s?o|kft|srl|sarl"
    r"|plc|ltd|llc|inc|corp|limited|holding|group|company"
    r")(?:$|[\s,.)])", re.I)

# Academic / professional titles. Their presence is by itself proof the string
# names a human being.
TITLE_RE = re.compile(
    r"^(?:ing|bc|mgr|mudr|judr|rndr|phdr|paeddr|mvdr|thdr|doc|prof|dipl)\b\.?",
    re.I)

# Czech given names. A closed list is the right instrument here: the population
# of Czech given names is small and stable, whereas the population of brand
# names is unbounded — so testing "is the first token a given name" is decidable
# where "does this look like a brand" is not. Erring toward suppression: a
# missing given name publishes a name that may be a person's, so the list is
# deliberately broad, including diminutives and the female forms.
GIVEN_NAMES = {
    "adam", "adela", "ales", "alena", "alois", "andrea", "andrej", "aneta",
    "anna", "antonin", "arnost", "barbora", "bedrich", "blanka", "bohumil",
    "bohuslav", "bozena", "brandon", "bretislav", "cyril", "dagmar", "dalibor",
    "dana", "daniel", "daniela", "darina", "david", "denisa", "dominik",
    "dominika", "drahomira", "dusan", "edita", "eliska", "emil", "emilie",
    "erik", "eva", "filip", "frantisek", "frantiska", "gabriel", "gabriela",
    "hana", "helena", "honza", "hynek", "igor", "ilona", "irena", "ivan",
    "ivana", "iveta", "ivo", "jakub", "jan", "jana", "jaromir", "jaroslav",
    "jaroslava", "jindrich", "jiri", "jirina", "jitka", "josef", "jozef",
    "julie", "kamil", "kamila", "karel", "karolina", "katerina", "klara",
    "kristina", "kristyna", "ladislav", "lenka", "leos", "libor", "libuse",
    "lubomir", "lubos", "lucie", "ludmila", "ludek", "lukas", "magdalena",
    "marcel", "marek", "marketa", "marie", "marika", "martin", "martina",
    "matej", "matous", "michael", "michaela", "michal", "milada", "milan",
    "milos", "miloslav", "miroslav", "miroslava", "monika", "natalie",
    "nikola", "nikol", "norbert", "oldrich", "oldriska", "olga", "ondrej",
    "otakar", "otto", "patrik", "pavel", "pavla", "pavlina", "petr", "petra",
    "premysl", "radek", "radim", "radka", "radko", "radomir", "radoslav",
    "rene", "renata", "richard", "robert", "roman", "romana", "rostislav",
    "rudolf", "ruzena", "sarka", "silvie", "simon", "simona", "sona",
    "stanislav", "stanislava", "stepan", "stepanka", "svatopluk", "sylva",
    "tadeas", "tereza", "tomas", "vaclav", "veronika", "vilem", "viktor",
    "viktorie", "vit", "vitezslav", "vladimir", "vladimira", "vladislav",
    "vlasta", "vlastimil", "vojtech", "zbynek", "zdenek", "zdenka", "zdislav",
    "zuzana", "sarlota", "stepanka", "jindriska", "alzbeta", "anezka",
}

_WS = re.compile(r"\s+")


def collapse(s):
    return _WS.sub(" ", str(s or "")).strip()


def deaccent(s):
    s = unicodedata.normalize("NFKD", str(s or ""))
    return "".join(c for c in s if not unicodedata.combining(c))


def slugify(s):
    s = deaccent(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "x"


def vendor_group(brand, public):
    """The join key. OPAQUE when the name is suppressed.

    THE BUG THIS EXISTS TO PREVENT, found by reading the finished corpus: the
    key was `slugify(brand)` unconditionally, so a suppressed vendor shipped as
    `"vendor": null, "vendor_group": "dominik-martini"`. Slugifying a name does
    not conceal it — it publishes it in lower case with hyphens, and the whole
    suppression was theatre.

    The key still has to GROUP: all add-ons by one vendor must share it, or the
    "which vendor sells what" question stops being answerable for exactly the
    small vendors this corpus is aimed at. A hash of the slug does both. It is
    taken over the SLUG rather than the raw name so that the value a later
    crawl computes matches the value already on disk.
    """
    s = slugify(brand)
    if public:
        return s
    return "x-" + hashlib.sha1(s.encode("utf-8")).hexdigest()[:12]


def log(m):
    print(m, file=sys.stderr)


# ══════════════════════════════════════════════════════════════════════════
# GDPR
# ══════════════════════════════════════════════════════════════════════════

def gdpr_violations(rec):
    """[(field, kind, snippet)] over every string in the record. Empty = safe."""
    out = []

    def walk(field, v):
        if isinstance(v, str):
            for kind, rx in (("email", EMAIL_RE), ("phone", PHONE_RE)):
                m = rx.search(v)
                if m:
                    out.append((field, kind, m.group(0)[:60]))
        elif isinstance(v, (list, tuple)):
            for x in v:
                walk(field, x)
        elif isinstance(v, dict):
            for k, x in v.items():
                walk(f"{field}.{k}", x)

    for k, v in rec.items():
        walk(k, v)
    return out


REDACTED = "[kontakt odstraněn]"
NAME_REDACTED = "[jméno odstraněno]"


def redact_names(text, names, keep_if_in=""):
    """Remove names from a CLOSED, DECLARED set out of free prose.

    FOUND BY READING THE FINISHED CORPUS, not by design: suppressing the vendor
    field is not enough, because vendors write each other's names into their own
    marketing copy. Three template listings carried "O nakódování šablony se pak
    postaral Petr Páral" and similar — Petr Páral is on the marketplace's own
    author list and had already been suppressed as a vendor, then walked back in
    through somebody else's prose.

    The set is CLOSED and DECLARED: it is exactly the authors that
    vendor_name_public() suppressed on this run's /katalog page. That keeps this
    mechanical — no judgement about who is a person — and it is passed in at
    runtime and never written to disk, so closing the hole does not create a
    file of suppressed names.

    `keep_if_in` is the add-on's own slug. EXCEPTION, and a necessary one:
    `Pohoda by Dominik Prajzler` is a product whose NAME, SLUG and canonical
    marketplace URL all contain the author's name, because he trades under it.
    Redacting it from the prose while `product` and `url` still carry it would
    produce an incoherent record and conceal nothing.

    STATED LIMIT: this closes the closed set and nothing else. Prose written by
    third parties can name anyone — the same three listings also credit "Radek
    Schramhauser", who is on no author list and is not touched here. A prose
    corpus free of all incidental personal names needs named-entity recognition,
    which is a different piece of work and is NOT claimed by this program.
    """
    keep = deaccent(keep_if_in).lower()
    for n in names:
        d = deaccent(n).lower()
        if not d or d in keep or d.replace(" ", "-") in keep:
            continue
        text = re.sub(r"(?<![\w-])" + r"\s+".join(re.escape(t) for t in n.split()) +
                      r"(?![\w-])", NAME_REDACTED, text, flags=re.I)
    return text


def redact_contacts(text):
    """(clean_text, n_email, n_phone). Unconditional and mechanical.

    LAYER 1 STOPS AT THE CONTACT BLOCK; THIS IS FOR WHAT IS INSIDE THE PROSE.
    MEASURED on the first four Shoptet pages crawled: `Recommender od ui42`
    prints `recommender@ui42.com` in the middle of its own product description,
    where no structural slice can reach it. Dropping every such record would
    have cost a quarter of that sample — a real hole in the corpus this build
    exists to fill — so the address is REMOVED and the product kept.

    Removal, not judgement: every match of the same expressions the gate uses
    is replaced, with no attempt to decide whether a given address is a role
    account or a person's. Deciding that is exactly the kind of call that gets
    made wrong at 3am on record 300.

    PHONES ARE NOT KEPT UNDER REDACTION. The brief is explicit that a record
    which would carry a private individual's phone number must not be written
    at all, so the callers treat n_phone > 0 as a DROP and this function only
    reports it. The two are handled differently on purpose: an address in
    marketing copy is usually a role account, a number in marketing copy is
    usually somebody's mobile.
    """
    n_e = len(EMAIL_RE.findall(text))
    n_p = len(PHONE_RE.findall(text))
    if n_e:
        text = EMAIL_RE.sub(REDACTED, text)
    if n_p:
        text = PHONE_RE.sub(REDACTED, text)
    return text, n_e, n_p


def vendor_name_public(name):
    """The trading name if it is not a natural person's, else None.

    INVERTED relative to normalize.py's party_name_public, and the header
    explains why. Returns None for anything that looks like a human being.
    """
    n = collapse(re.sub(r"[;\[\]|\r\n]+", " ", str(name or "")))
    if not n:
        return None
    if LEGAL_FORM_RE.search(n):
        return n                      # provably a legal person
    if TITLE_RE.match(n):
        return None                   # "Ing. Tomáš Koutný"
    tokens = [t for t in re.split(r"[\s,]+", n) if t]
    if tokens:
        first = re.sub(r"[^A-Za-zÀ-ž]", "", deaccent(tokens[0])).lower()
        if first in GIVEN_NAMES:
            return None               # "Adam Zátopek", "Jakub Grác - JG-Media"
    return n


# ══════════════════════════════════════════════════════════════════════════
# HTML → text
# ══════════════════════════════════════════════════════════════════════════

_BLOCK = re.compile(r"</(?:p|div|li|ul|ol|h[1-6]|tr|section|article)>|<br\s*/?>",
                    re.I)


def to_text(fragment, limit=6000):
    t = re.sub(r"<script.*?</script>", " ", fragment, flags=re.S | re.I)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S | re.I)
    t = _BLOCK.sub("\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = htmllib.unescape(t)
    t = re.sub(r"[ \t ]+", " ", t)
    t = re.sub(r"\s*\n\s*", "\n", t)
    t = re.sub(r"\n{2,}", "\n", t).strip()
    return t[:limit]


def first_index(hay, needles, default=None):
    """Index of the earliest needle present, or `default`."""
    hits = [hay.find(n) for n in needles]
    hits = [i for i in hits if i >= 0]
    return min(hits) if hits else default


# Czech price sentences. Verbatim, because a derived number would be a claim we
# cannot receipt: these pages price per product, per order, per month and per
# "credit", and normalising them into one figure would invent precision.
PRICE_RE = re.compile(
    r"[^.\n]*?(?:\d[\d\s.,]*\s*(?:Kč|CZK|,-|€|EUR)|zdarma|zadarmo|měsíčně"
    r"|měsíc|ročně|kredit)[^.\n]*\.?", re.I)


AMOUNT_RE = re.compile(r"\d[\d\s.,]*\s*(?:Kč|CZK|,-|€|EUR)", re.I)


def price_note(text, limit=300):
    """Verbatim price sentences, AMOUNT-BEARING ONES FIRST.

    Ordering matters more than it looks: these pages open with a free-trial
    line ("Vyzkoušení zdarma …") and bury the actual tariff ("Za 1 000 produktů
    zaplatíte 19 Kč měsíčně") hundreds of words later. Document order would
    therefore fill the whole budget with the trial offer and drop the price —
    which is the one number a gap check wants.
    """
    priced, free, seen = [], [], set()
    for m in PRICE_RE.finditer(text):
        s = collapse(m.group(0))
        if len(s) < 12 or s.lower() in seen:
            continue
        seen.add(s.lower())
        (priced if AMOUNT_RE.search(s) else free).append(s)
    out, n = [], 0
    for s in priced + free:
        if n + len(s) > limit and out:
            break
        out.append(s)
        n += len(s) + 3
    return " · ".join(out)[:limit]


# ══════════════════════════════════════════════════════════════════════════
# CONTRACTS — required_fields, the Mode-A gate
# ══════════════════════════════════════════════════════════════════════════
#
# MEASURED 2026-08-21, both hosts, with the descriptive UA:
#
#   doplnky.shoptet.cz/<unknown>            -> HTTP 404, 37,997 bytes of HTML
#   doplnky.shoptet.cz/katalog?partner=9e9  -> HTTP 404, 37,997 bytes
#   doplnky.upgates.cz/detail/<unknown>     -> HTTP 200, 102,039 bytes,
#                                              sha256-IDENTICAL to the homepage
#
# The second one is the trap in its purest form. A fetcher checking only the
# status code stores the homepage as an add-on record; a fetcher additionally
# reading `<h1 itemprop="name">` gets the string "Marketplace" and writes a
# plausible-looking row. What actually settles it is IDENTITY: the page must
# claim, in its own og:url, to be the resource we asked for.

SHOPTET_REQUIRED = ("og:url==requested", "schema.org/Product",
                    'meta itemprop="brand"', '<h1 itemprop="name">')
UPGATES_REQUIRED = ("og:url==requested", "Poskytovatel",
                    '<h1 itemprop="name">', "tarif-product")


def og_url(h):
    m = re.search(r'<meta property="og:url" content="([^"]*)"', h)
    return m.group(1).strip() if m else ""


def _same_resource(a, b):
    n = lambda u: re.sub(r"[?#].*$", "", (u or "").strip()).rstrip("/").lower()
    return bool(n(a)) and n(a) == n(b)


def contract_shoptet_detail(h, url):
    """(ok, reason, fields). `reason` names the FIRST required field missing."""
    f = {}
    o = og_url(h)
    if not _same_resource(o, url):
        return False, f"og:url mismatch (page claims {o or '<none>'})", f
    if not re.search(r'itemtype="https?://schema\.org/Product"', h):
        return False, "no schema.org/Product itemscope", f
    m = re.search(r'<meta itemprop="brand" content="([^"]*)"', h)
    if not m or not m.group(1).strip():
        return False, 'no meta itemprop="brand"', f
    f["brand"] = htmllib.unescape(m.group(1)).strip()
    # `[^>]*` around itemprop is NOT decoration. MEASURED: the ordinary template
    # emits `<h1 itemprop="name">` but the Premium one emits
    # `<h1 class="premium-title" itemprop="name">`, and an exact-match regex
    # silently rejected the whole Premium family — 5 real add-ons including
    # PriceKit PREMIUM (Smart Trade Applications) — as if they were not-found
    # pages. A contract that is too tight fails the same way one that is too
    # loose does: quietly, in the direction nobody checks.
    m = re.search(r'<h1[^>]*itemprop="name"[^>]*>([^<]*)</h1>', h)
    if not m or not m.group(1).strip():
        return False, 'no <h1 itemprop="name">', f
    f["name"] = htmllib.unescape(m.group(1)).strip()
    return True, "", f


MARKETPLACE_ROOT = "https://doplnky.upgates.cz"


def contract_upgates_detail(h, url, expected_name=None):
    """Identity here is proved by EITHER of two independent witnesses.

    og:url equality alone was measured to be wrong in both directions:
      · TOO STRICT — /detail/zakeke 302s to webklient.cz and /detail/
        vlastni-konverzni-kody to upgates.cz/a/…, so a real catalogue entry
        carries somebody else's og:url.
      · Still necessary — the soft-404 body IS the homepage, whose og:url is
        the marketplace root, so `og:url == root` must always be fatal.

    So: the root is always rejected, and identity is satisfied by og:url
    matching the request OR the h1 matching the name the LISTING declared for
    this slug. The listing is a separately fetched surface, which makes the
    second witness a genuine cross-check rather than the page vouching for
    itself. The soft-404's h1 is the string "Marketplace" and matches no tile.
    """
    f = {}
    o = og_url(h)
    if _same_resource(o, MARKETPLACE_ROOT):
        return False, "og:url is the marketplace root (soft-404 homepage)", f
    m = re.search(r'<h1[^>]*itemprop="name"[^>]*>([^<]*)</h1>', h)
    if not m or not m.group(1).strip():
        return False, 'no <h1 itemprop="name">', f
    f["name"] = htmllib.unescape(m.group(1)).strip()
    id_ok = _same_resource(o, url)
    if not id_ok and expected_name:
        id_ok = deaccent(f["name"]).lower() == deaccent(expected_name).lower()
    if not id_ok:
        return False, f"identity unproven (og:url={o or '<none>'}, h1={f['name']!r})", f
    if "tarif tarif-product" not in h:
        return False, "no tarif-product price card", f
    # MEASURED: the provider is a LINK for partner add-ons
    # (`Poskytovatel <a href="https://balikuj.cz">PROGRAMATORI s.r.o.</a>`) and
    # BARE TEXT for Upgates' own (`Poskytovatel\n\t\t\t\t\tUpgates`). Requiring
    # the link rejected 76 legitimate first-party add-ons — a 38% reject rate
    # that looked like a hostile site and was our regex.
    # The provider is OPTIONAL, and that is a fact about the source rather than
    # a relaxation for convenience. MEASURED: /detail/abra-flexi, /detail/mrp,
    # /detail/helios-inuvio and 13 more are real detail pages — og:url matching,
    # h1 present, price card present — on which the marketplace simply declares
    # no provider. Requiring one threw away sixteen named ERP and accounting
    # integrations. The identity and price-card checks above are what keep the
    # soft-404 out; the provider row was never doing that work.
    m = re.search(r"Poskytovatel\s*<a href=\"([^\"]*)\"[^>]*>([^<]*)</a>", h)
    if m:
        f["vendor_url"] = m.group(1).strip()
        f["brand"] = htmllib.unescape(m.group(2)).strip()
    else:
        m = re.search(r"Poskytovatel\s*([^<]+?)\s*</span>", h)
        f["brand"] = htmllib.unescape(m.group(1)).strip() if m else ""
    return True, "", f


# ══════════════════════════════════════════════════════════════════════════
# EXTRACTORS
# ══════════════════════════════════════════════════════════════════════════

def load_names(path):
    """The runtime-only suppressed-name list. Absent file = empty list."""
    if not path or not os.path.exists(path):
        return []
    return [l.strip() for l in open(path, encoding="utf-8") if l.strip()]


def shoptet_catalog(path, out, names_out=None):
    """The DECLARED vendor table and category taxonomy, from one /katalog page.

    <select name="partnerId"> is the marketplace's own list of its partners and
    <select name="labelIndexName"> its own category tree. Reading a declared
    control beats crawling 179 partner pages to infer the same thing.
    """
    h = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r'<select[^>]*name="partnerId"[^>]*>(.*?)</select>', h, re.S)
    if not m:
        return None, None, 'no <select name="partnerId">'
    vendors, suppressed, suppressed_names = [], 0, []
    for vid, label in re.findall(r'<option value="([^"]*)"[^>]*>(.*?)</option>',
                                 m.group(1), re.S):
        name = collapse(htmllib.unescape(re.sub(r"<[^>]+>", "", label)))
        if not vid or not name or name.lower().startswith("všichni"):
            continue
        pub = vendor_name_public(name)
        if pub is None:
            suppressed += 1
            suppressed_names.append(name)
        row = {"id": f"shoptet-partner-{vid}", "marketplace": "shoptet",
               "vendor_id": f"shoptet-partner-{vid}",
               "catalog_url": f"https://doplnky.shoptet.cz/katalog?partnerId={vid}",
               "vendor_public": pub is not None}
        if pub is not None:
            row["vendor"] = pub
        vendors.append(row)
    cats = []
    m2 = re.search(r'<select[^>]*name="labelIndexName"[^>]*>(.*?)</select>', h, re.S)
    if m2:
        cats = [c for c in re.findall(r'<option value="([^"]*)"', m2.group(1)) if c]
    with open(out, "w", encoding="utf-8") as fh:
        for v in vendors:
            fh.write(json.dumps(v, ensure_ascii=False) + "\n")
    # RUNTIME ONLY. The caller writes this under $TMPDIR and the trap wipes it
    # on exit; closing the prose hole must not create a durable file of the very
    # names the rest of this program exists to keep out of durable files.
    if names_out:
        with open(names_out, "w", encoding="utf-8") as fh:
            fh.write("\n".join(suppressed_names) + "\n")
    return vendors, cats, ""


def shoptet_detail(path, url, vendors_path=None, names_path=None):
    h = open(path, encoding="utf-8", errors="replace").read()
    ok, reason, f = contract_shoptet_detail(h, url)
    if not ok:
        return None, reason

    # ── GDPR layer 1: the text slice STOPS at the contact table ──────────────
    start = h.find('class="content-box main-content"')
    # Past the end of the opening tag, or the attribute string itself lands in
    # the text. `+ 1` because find() returns the '>' position.
    start = (h.find(">", start) + 1) if start >= 0 else 0
    stop = first_index(h, ["<h3>Podpora</h3>", 'class="service-info-table"',
                           'id="section-ratings"', 'class="rating-review'],
                       default=len(h))
    if stop <= start:
        stop = len(h)
    slug = re.sub(r"^https?://[^/]+/", "", url).strip("/")
    prose = redact_names(to_text(h[start:stop]), load_names(names_path), slug)
    text, n_e, n_p = redact_contacts(prose)
    if n_p:
        m = PHONE_RE.search(prose)
        return None, f"gdpr:phone-in-prose ({m.group(0)[:24] if m else '?'})"

    rec = {
        "id": f"shoptet-{slug}",
        "marketplace": "shoptet",
        "slug": slug,
        "url": url,
        "product": f["name"],
        "vendor_id": None,
        "vendor_public": False,
        "text_cs": text,
        "extraction": "structured",
    }
    pub = vendor_name_public(f["brand"])
    rec["vendor_public"] = pub is not None
    if pub is not None:
        rec["vendor"] = pub
    # Groups the vendor's add-ons together; opaque when the name is suppressed.
    rec["vendor_group"] = vendor_group(f["brand"], pub is not None)

    m = re.search(r'Vytvořil.*?<a href="([^"]*)"', h, re.S)
    if m and m.group(1).startswith("http"):
        rec["vendor_url"] = m.group(1).strip()
    # Primary category — the `Název` row of the info table links to it. Read as
    # a plain href so a redesign of the table costs the category, not the row.
    m = re.search(r'<a href="/category/([a-z0-9\-]+)"[^>]*><span itemprop="label">', h)
    if m:
        rec["category"] = m.group(1)
    for key, rx in (("rating_value", r'<meta itemprop="ratingValue" content="([^"]*)"'),
                    ("rating_count", r'<meta itemprop="ratingCount" content="([^"]*)"')):
        mm = re.search(rx, h)
        if mm and mm.group(1).strip():
            try:
                rec[key] = float(mm.group(1)) if key == "rating_value" else int(mm.group(1))
            except ValueError:
                pass
    pn = price_note(text)
    if pn:
        rec["price_note"] = pn
    if n_e:
        rec["redactions"] = n_e

    if vendors_path and os.path.exists(vendors_path):
        want = slugify(f["brand"])
        with open(vendors_path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    v = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if v.get("vendor") and slugify(v["vendor"]) == want:
                    rec["vendor_id"] = v["vendor_id"]
                    break
    if rec["vendor_id"] is None:
        rec.pop("vendor_id")
    return rec, ""


UP_TILE = re.compile(r"<article\b[^>]*addon-item[^>]*>.*?</article>", re.S)


def upgates_listing(paths):
    """slug -> {name, categories} from the homepage + category pages."""
    rows = {}
    for p in paths:
        h = open(p, encoding="utf-8", errors="replace").read()
        # fetch_upgates.sh writes `home.html` and `cat-<slug>.html`.
        cat = re.sub(r"\.html$", "", os.path.basename(p))
        cat = re.sub(r"^(?:upgates-)?(?:cat-)?", "", cat)
        for a in UP_TILE.findall(h):
            s = re.search(r'href="/detail/([a-z0-9\-]+)"', a)
            if not s:
                continue
            n = re.search(r'class="h5 mb-1 p-i-header">([^<]*)</a>', a)
            r = rows.setdefault(s.group(1), {"slug": s.group(1), "name": "",
                                             "categories": []})
            if n and not r["name"]:
                r["name"] = collapse(htmllib.unescape(n.group(1)))
            if cat not in r["categories"] and cat != "home":
                r["categories"].append(cat)
    return rows


def upgates_detail(path, url, expected_name=None):
    h = open(path, encoding="utf-8", errors="replace").read()
    ok, reason, f = contract_upgates_detail(h, url, expected_name)
    if not ok:
        return None, reason

    # ── GDPR layer 1 ── everything from `Poskytovatel` on is the contact block.
    stop = first_index(h, ["Poskytovatel"], default=len(h))
    start = h.find('<h1 class="text-center')
    if start < 0:
        start = h.find('itemprop="name"')
    if start < 0 or start >= stop:
        start = 0
    text = to_text(h[start:stop], 1200)
    # The prose body lives in the description tab, which sits AFTER the contact
    # block in source order — so it is appended from its own bounded slice
    # rather than by widening the cut above.
    #
    # MEASURED on /detail/balikuj: the id `tab-description` appears TWICE — a
    # 515-byte tip box at 18,776 and the real 9,434-byte body at 19,304. A
    # non-greedy match takes the first and yields a 370-character record that
    # looks extracted and contains no product vocabulary, so the LONGEST match
    # is taken rather than the first.
    ds = re.findall(r'<section id="tab-description".*?</section>', h, re.S)
    if ds:
        text = text + "\n" + to_text(max(ds, key=len), 5000)
    text, n_e, n_p = redact_contacts(text)
    if n_p:
        return None, "gdpr:phone-in-prose"

    slug = url.rstrip("/").rsplit("/", 1)[-1]
    rec = {
        "id": f"upgates-{slug}",
        "marketplace": "upgates",
        "slug": slug,
        "url": url,
        "product": f["name"],
        "vendor_public": False,
        "text_cs": text[:6000],
        "extraction": "structured",
    }
    pub = vendor_name_public(f["brand"]) if f["brand"] else None
    if f["brand"]:
        rec["vendor_group"] = vendor_group(f["brand"], pub is not None)
    rec["vendor_public"] = pub is not None
    if pub is not None:
        rec["vendor"] = pub
    if f.get("vendor_url", "").startswith("http"):
        rec["vendor_url"] = f["vendor_url"]
    pn = price_note(text)
    if pn:
        rec["price_note"] = pn
    if n_e:
        rec["redactions"] = n_e
    return rec, ""


# ══════════════════════════════════════════════════════════════════════════
# WRITE PATH — every record passes the GDPR content scan or is dropped
# ══════════════════════════════════════════════════════════════════════════

def write_checked(rows, out):
    kept, dropped = [], []
    for r in rows:
        v = gdpr_violations(r)
        if v:
            dropped.append((r.get("id", "?"), v))
            continue
        kept.append(r)
    kept.sort(key=lambda r: r["id"])
    with open(out, "w", encoding="utf-8") as fh:
        for r in kept:
            fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    return kept, dropped


def search(lookup, terms, limit=10):
    """Czech-word search over the lookup table — the query a gap check runs.

    THE WHOLE CORPUS EXISTS FOR THIS CALL. `data/CONVENTIONS.md` is explicit
    that a gap check must be run IN CZECH ("for p-0002 the English query
    returned no Czech vendor and the Czech queries returned four"), so the
    ranking is over Czech product vocabulary, diacritics folded because a
    searcher types `hlidac` as often as `hlídač`.

    Scoring is TF-IDF, and the IDF half is not decoration — it is the whole
    difference between a working gap check and a broken one. MEASURED on the
    376-row Shoptet corpus with p-0028's own query:

        cen        376/376 docs      zákonem      3/376
        dní        368/376           ČOI          4/376
        cena       364/376           nejnižší     9/376
        e-shopu    314/376           zákon       10/376

    Flat term counting put Hlídač Slev — the incumbent this build exists to
    prove it can find — outside the top 10, because four generic e-commerce
    words swamped the four that carry the meaning. A term present in every
    document carries no information about which document you want, and
    weighting by log(N/df) says exactly that. Field weights (8x name, 3x price
    line) sit on top.
    """
    want = sorted({deaccent(t).lower().strip(".,;:!?\"'()") for t in terms
                   if len(t) > 2})
    docs = []
    with open(lookup, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            docs.append((r,
                         deaccent(r.get("product", "")).lower(),
                         deaccent(r.get("price_note", "")).lower(),
                         deaccent(r.get("text_cs", "")).lower()))
    n_docs = max(len(docs), 1)
    import math
    idf = {}
    for t in want:
        df = sum(1 for _, name, price, body in docs
                 if t in name or t in price or t in body)
        # +1 inside the log so a term in EVERY document scores 0, not negative.
        idf[t] = math.log(n_docs / (df + 1)) + 1e-9 if df else 0.0
        idf[t] = max(idf[t], 0.0)

    rows = []
    for r, name, price, body in docs:
        score, hits = 0.0, []
        for t in want:
            if not idf[t]:
                continue
            tf = 8 * name.count(t) + 3 * price.count(t) + min(body.count(t), 5)
            if tf:
                score += tf * idf[t]
                hits.append(t)
        if score > 0:
            rows.append((score, len(hits), r, hits))
    rows.sort(key=lambda x: (-x[0], -x[1], x[2]["id"]))
    return rows[:limit], len(rows)


def merge(out, inputs):
    """Union by id, newest input wins, sorted — a stable committed table."""
    byid = {}
    for p in inputs:
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if r.get("id"):
                    byid[r["id"]] = r
    kept, dropped = write_checked(list(byid.values()), out)
    return kept, dropped


# ══════════════════════════════════════════════════════════════════════════
# SELFTEST — the contract must be shown to reject a not-found page
# ══════════════════════════════════════════════════════════════════════════

def selftest(fixdir):
    fails = []

    def check(label, got, want):
        ok = got == want
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}: {got!r}")
        if not ok:
            fails.append(label)

    print("== vendor_name_public — suppression of natural persons")
    for name, want in [
        ("JARABOT", "JARABOT"),
        ("PROGRAMATORI s.r.o.", "PROGRAMATORI s.r.o."),
        ("Seyfor, a.s.", "Seyfor, a.s."),
        ("Marketing Hub", "Marketing Hub"),
        ("AI Studio", "AI Studio"),
        ("Data connection", "Data connection"),
        ("honzabartos.cz", "honzabartos.cz"),
        ("Zásilkovna", "Zásilkovna"),
        ("Adam Zátopek", None),
        ("Vít Michalek", None),
        ("Vojtěch Fárek", None),
        ("Zdeněk Dušátko", None),
        ("Jakub Grác - JG-Media", None),
        ("Ing. Tomáš Koutný", None),
        ("Jana Vítková", None),
    ]:
        check(f"vendor_name_public({name!r})", vendor_name_public(name), want)

    print("== vendor_group — a suppressed name must not survive as a slug")
    check("public key is the slug", vendor_group("JARABOT", True), "jarabot")
    k = vendor_group("Dominik Martini", False)
    check("suppressed key is opaque", k.startswith("x-") and "martini" not in k
          and "dominik" not in k, True)
    check("suppressed key is stable", vendor_group("Dominik Martini", False), k)
    check("distinct people, distinct keys",
          vendor_group("Jan Klubus", False) != vendor_group("Marek Bastl", False), True)

    print("== redact_names — a suppressed author walking back in via someone else's prose")
    NAMES = ["Petr Páral", "Dominik Prajzler", "Jan Klubus"]
    t = redact_names("O nakódování šablony se postaral Petr Páral, specialista.",
                     NAMES, "sablona-jupiter")
    check("third-party credit removed", "Páral" not in t and "Petr" not in t, True)
    check("surrounding prose kept", "nakódování šablony" in t, True)
    t = redact_names("Pohoda by Dominik Prajzler propojí Shoptet.", NAMES,
                     "pohoda-by-dominik-prajzler")
    check("own trading name kept (slug carries it)", "Dominik Prajzler" in t, True)
    check("unlisted person untouched (STATED LIMIT)",
          "Radek Schramhauser" in redact_names("kóder Radek Schramhauser", NAMES, ""), True)

    print("== gdpr_violations — the content gate")
    check("clean record", gdpr_violations({"text_cs": "Doplněk hlídá slevy."}), [])
    got = gdpr_violations({"text_cs": "Napište na info@jarabot.com"})
    check("email caught", bool(got), True)
    got = gdpr_violations({"text_cs": "Telefon +420 777 002 493"})
    check("phone caught", bool(got), True)

    print("== redact_contacts — prose that no structural slice can reach")
    t, ne, np_ = redact_contacts("Napište na recommender@ui42.com a rádi pomůžeme.")
    check("email counted", (ne, np_), (1, 0))
    check("email gone", gdpr_violations({"text_cs": t}), [])
    check("text survives", "rádi pomůžeme" in t, True)
    t, ne, np_ = redact_contacts("Volejte +420 777 002 493 kdykoli.")
    check("phone counted", (ne, np_), (0, 1))
    check("phone gone", gdpr_violations({"text_cs": t}), [])

    if not fixdir or not os.path.isdir(fixdir):
        print("\n(no fixture dir given — contract tests skipped)")
        return 1 if fails else 0

    print("== Mode-A contract — saved not-found pages must be REJECTED")
    cases = [
        ("shoptet 404 body", "shoptet-notfound.html",
         "https://doplnky.shoptet.cz/tento-doplnek-neexistuje-xyzzy-42",
         contract_shoptet_detail, False),
        ("shoptet real add-on", "shoptet-hlidac-slev.html",
         "https://doplnky.shoptet.cz/hlidac-slev",
         contract_shoptet_detail, True),
        ("shoptet listing page as detail", "shoptet-katalog.html",
         "https://doplnky.shoptet.cz/hlidac-slev",
         contract_shoptet_detail, False),
        ("upgates SOFT-404 (HTTP 200, = homepage)", "upgates-notfound.html",
         "https://doplnky.upgates.cz/detail/tento-doplnek-neexistuje-xyzzy-42",
         contract_upgates_detail, False),
        ("upgates real add-on", "upgates-balikuj.html",
         "https://doplnky.upgates.cz/detail/balikuj",
         contract_upgates_detail, True),
        ("upgates homepage as detail", "upgates-home.html",
         "https://doplnky.upgates.cz/detail/balikuj",
         contract_upgates_detail, False),
        # The widened contracts, each pinned by the page that broke the tight
        # one. Without these two the regressions are invisible until a run.
        ("shoptet PREMIUM template (h1 has a class attr)", "shoptet-premium.html",
         "https://doplnky.shoptet.cz/pricekit-premium",
         contract_shoptet_detail, True),
        ("upgates first-party (Poskytovatel is bare text)", "upgates-first-party.html",
         "https://doplnky.upgates.cz/detail/upgates-pay",
         contract_upgates_detail, True),
        ("upgates real page with NO provider row", "upgates-no-provider.html",
         "https://doplnky.upgates.cz/detail/abra-flexi",
         contract_upgates_detail, True),
        ("upgates category listing as detail", "upgates-category.html",
         "https://doplnky.upgates.cz/informacni-systemy",
         contract_upgates_detail, False),
    ]
    for label, fn, url, contract, want in cases:
        p = os.path.join(fixdir, fn)
        if not os.path.exists(p):
            print(f"  [SKIP] {label}: fixture {fn} absent")
            continue
        h = open(p, encoding="utf-8", errors="replace").read()
        ok, reason, _ = contract(h, url)
        good = ok == want
        if not good:
            fails.append(label)
        print(f"  [{'PASS' if good else 'FAIL'}] {label}: "
              f"{len(h):,} chars -> {'ACCEPT' if ok else 'REJECT: ' + reason}")

    print("== identity via the LISTING witness, and the adversarial case")
    p = os.path.join(fixdir, "upgates-first-party.html")
    if os.path.exists(p):
        h = open(p, encoding="utf-8", errors="replace").read()
        # A URL we did NOT request, rescued by the tile name — the /detail/zakeke
        # shape, where og:url points at the partner's own docs.
        ok, why, _ = contract_upgates_detail(
            h, "https://doplnky.upgates.cz/detail/some-other-slug", "Upgates Pay")
        check("tile name proves identity", ok, True)
        ok, why, _ = contract_upgates_detail(
            h, "https://doplnky.upgates.cz/detail/some-other-slug", "Something Else")
        check("wrong tile name still rejects", ok, False)
    p = os.path.join(fixdir, "upgates-notfound.html")
    if os.path.exists(p):
        h = open(p, encoding="utf-8", errors="replace").read()
        # ADVERSARIAL: hand the soft-404 the very name its own h1 carries. The
        # root check must fire BEFORE the name check, or a slug called
        # "Marketplace" would let the homepage in through the front door.
        ok, why, _ = contract_upgates_detail(
            h, "https://doplnky.upgates.cz/detail/marketplace", "Marketplace")
        check("soft-404 rejected even when the h1 'matches'", ok, False)

    print("== GDPR structural gate — real pages carry a phone; records must not")
    for label, fn, url, fn_extract in [
        ("shoptet/hlidac-slev", "shoptet-hlidac-slev.html",
         "https://doplnky.shoptet.cz/hlidac-slev", "shoptet"),
        ("upgates/balikuj", "upgates-balikuj.html",
         "https://doplnky.upgates.cz/detail/balikuj", "upgates"),
    ]:
        p = os.path.join(fixdir, fn)
        if not os.path.exists(p):
            print(f"  [SKIP] {label}")
            continue
        raw = open(p, encoding="utf-8", errors="replace").read()
        raw_hits = gdpr_violations({"page": raw})
        rec, why = (shoptet_detail(p, url, None) if fn_extract == "shoptet"
                    else upgates_detail(p, url))
        if rec is None:
            fails.append(label)
            print(f"  [FAIL] {label}: contract rejected a real page ({why})")
            continue
        rec_hits = gdpr_violations(rec)
        good = bool(raw_hits) and not rec_hits
        if not good:
            fails.append(label)
        print(f"  [{'PASS' if good else 'FAIL'}] {label}: page has "
              f"{len(raw_hits)} personal-data hit(s) "
              f"{sorted({k for _, k, _ in raw_hits})}, record has {len(rec_hits)}")
    return 1 if fails else 0


# ══════════════════════════════════════════════════════════════════════════

def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd = argv[1]

    if cmd == "--selftest":
        return selftest(argv[2] if len(argv) > 2 else "")

    if cmd == "shoptet-catalog":
        vendors, cats, err = shoptet_catalog(argv[2], argv[3],
                                             argv[4] if len(argv) > 4 else None)
        if err:
            log(f"shoptet-catalog: {err}")
            return 1
        pub = sum(1 for v in vendors if v["vendor_public"])
        print(json.dumps({"vendors": len(vendors), "vendors_named": pub,
                          "vendors_suppressed": len(vendors) - pub,
                          "categories": len(cats)}))
        return 0

    if cmd == "shoptet-detail":
        rec, why = shoptet_detail(argv[2], argv[3],
                                  argv[4] if len(argv) > 4 else None,
                                  argv[5] if len(argv) > 5 else None)
        if rec is None:
            log(f"REJECT {argv[3]}: {why}")
            # A GDPR drop is not a contract rejection and must not be counted
            # as one: exit 3 is the callers' signal to tally it separately, so
            # a run that loses records to personal data says so in those words.
            return 3 if why.startswith("gdpr:") else 1
        v = gdpr_violations(rec)
        if v:
            log(f"GDPR-DROP {argv[3]}: {v[:2]}")
            return 3
        print(json.dumps(rec, ensure_ascii=False, sort_keys=True))
        return 0

    if cmd == "upgates-listing":
        rows = upgates_listing(sorted(
            os.path.join(argv[2], f) for f in os.listdir(argv[2])
            if f.endswith(".html")))
        with open(argv[3], "w", encoding="utf-8") as fh:
            for k in sorted(rows):
                fh.write(json.dumps(rows[k], ensure_ascii=False) + "\n")
        print(json.dumps({"addons": len(rows)}))
        return 0

    if cmd == "upgates-detail":
        rec, why = upgates_detail(argv[2], argv[3],
                                  argv[4] if len(argv) > 4 else None)
        if rec is None:
            log(f"REJECT {argv[3]}: {why}")
            return 3 if why.startswith("gdpr:") else 1
        v = gdpr_violations(rec)
        if v:
            log(f"GDPR-DROP {argv[3]}: {v[:2]}")
            return 3
        print(json.dumps(rec, ensure_ascii=False, sort_keys=True))
        return 0

    if cmd == "search":
        rows, total = search(argv[2], re.split(r"\s+", " ".join(argv[3:])))
        print(f"{total} add-on(s) match; top {len(rows)}:\n")
        for rank, (score, nh, r, hits) in enumerate(rows, 1):
            v = r.get("vendor") or f"[suppressed · {r.get('vendor_group', '?')}]"
            print(f"{rank:2d}. [{score:6.1f}] {r['product']}  —  {v}")
            print(f"      {r['url']}")
            if r.get("price_note"):
                print(f"      price: {r['price_note'][:110]}")
            print(f"      matched: {', '.join(hits)}\n")
        return 0

    if cmd == "merge":
        kept, dropped = merge(argv[2], argv[3:])
        for i, v in dropped:
            log(f"GDPR-DROP {i}: {v[:2]}")
        print(json.dumps({"merged": len(kept), "gdpr_dropped": len(dropped)}))
        return 0

    log(f"unknown command: {cmd}")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
