# Unconventional sources — the buyer-intent run (2026-09-04)

**The single axis:** does the source *name a buyer who has money and an intention to spend
it, before that intention becomes a public tender?* Volume scores zero. This is the axis
`docs/who-pays-audit-2026-09-03.md` Part 1 proved the register fails: MONEY measures
proximity to a public budget, not whose pocket the money leaves.

All probed live 2026-09-04 unless marked UNVERIFIED. Anything already in
`docs/sources-catalog.md` or already scripted is not re-proposed.

---

## The candidates

| # | Source | What it yields that we lack | Fetchable? | Cadence | Effort | VALUE |
|---|---|---|---|---|---|---|
| A | **MS2021+ `SeznamOperaci`** | Every *approved* EU-fund project: beneficiary + IČO, a self-written `<PROBLEM>` statement, `<CIL>`, and the committed CZK — money already in that buyer's hands for that stated purpose | **curl**, no auth, CC BY 4.0 | daily | 6–10 h | **5** |
| B | **eDesky API** (6,346 noticeboards) | `záměr` documents — a municipality's legally-required published *intention* to buy, sell or lease; plus budget amendments and resolutions | **curl + free API key** | daily | 5–8 h | **4** |
| C | **CityVizor public API** | Itemized municipal invoices: counterparty IČO, amount, free-text description, budget code — what a Czech public buyer *actually paid*, below tender thresholds | **curl**, no auth | daily | 4–6 h + unsolved paging | **4** |
| D | **RVIS minutes + named coordinators** | Government IT council: PDF minutes and slide decks per session, and a public list of each ministry's digital-agenda coordinator — a lawful named recipient | **curl** (PDFs); role list human | ~quarterly | 3 h + ongoing | **4** |
| E | **usneseni.cz** | 359 municipalities × 151,645 council resolutions, full-text — "rada schvaluje záměr pořídit…" is intention, pre-tender | browser/scrape; **ToS UNVERIFIED** | daily | 8–12 h | **3** |
| F | Registr smluv by CPV/keyword | Category price discovery | **already built** — `fetch_smlouvy.sh` (bulk) + `fetch_hlidac.sh` (full-text) | — | ~2 h (query recipe only) | n/a |
| G | NEN předběžné tržní konzultace | Pre-tender consultations | **already built** — `scripts/fetch_nen_ptk.sh` | — | — | n/a |
| H | IROP applicant seminars | Call rules, not buyer intent | curl (4 PDFs verified) | per call | — | **1** |
| I | ISoSS | unreachable | **UNVERIFIED** | — | — | **1** |
| J | Centrální úřední deska API | Executor documents only | key required | — | — | **1** |
| K | SCSP | could not reproduce | — | — | — | **0** |

### Verification notes

**A.** `https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml` → HTTP 200, 146,410,196 B,
`LICENCE="Creative Commons (CC BY 4.0)"`, `AUTOR="Ministerstvo pro místní rozvoj"`,
`DATE="2026-09-03T18:55"`. Measured 2,402 `<PRJ>` in the first 9 MB → **~39,000 projects**.
Each carries `<ZAD><NAZ>/<IC>`, `<POPIS>`, `<PROBLEM>`, `<CIL>`, `<PF><CZV>` (approved
eligible cost), `<DZRSKUT>`/`<DURPRED>` (the window inside which they must spend), NUTS codes.
**`dotace-scan` already reads `SeznamVyzev` — the calls, i.e. the money on offer. Nobody
reads `SeznamOperaci` — the winners, i.e. the buyers who took it.** That is the gap.

**B.** `edesky.cz/api/v1/documents` → HTTP 401 *"nepřihlášen, použijte svůj API klíč"*.
Free registration. XML. The HTML site sits behind an **Anubis proof-of-work gate** — every
curl to `edesky.cz/*` returns *"Making sure you're not a bot!"*, so scraping is out and the
API is the sanctioned route. `robots.txt` disallows only `/attachments/`.

**C.** `cityvizor.cz/api/public/profiles` → 338 profiles (62 municipalities, 275 PBO),
**35 with `hasPayments`**. `…/profiles/1/payments` → 3.1 MB of invoice rows with
`counterpartyId` (IČO), `counterpartyName`, `expenditureAmount`, `description`.
**Named limitation, measured:** the response caps at **10,000 rows, oldest first**, and
`?year=` is *ignored* — `year=2024` and `year=2025` both returned 2013–2015 rows. Recent
data needs a paging route I did not find.

**D.** `uv.gov.cz/cz/ppov/rvis/zapisy_rvis/` — per-session pages carrying minutes and slides,
e.g. 11th plenary 2026-06-29 → `Zapis_RVIS_2026-06-29.pdf` (165 kB) +
`Prezentace_RVIS_2026-06-29.pdf` (5.2 MB). **UNVERIFIED: I did not read the PDF text**, so
whether the minutes name unmet needs is an open question, not a claim.

**E.** `usneseni.cz` is a **vendor** selling meeting software to municipalities, not an open
aggregator. No API documented. `robots.txt` advertises `sitemap.xml.gz`, which is an explicit
crawl invitation, but the terms of use were not read. Treat as ToS-UNVERIFIED, like
`startupgraveyard.io` in the catalog.

**H.** The 29-10-2024 "83./84./85. výzva Veřejné zdraví" seminar page publishes four decks
under `/getmedia/…` (verified). They cover eligible expenses, evaluation criteria and how to
submit in MS2021+. **Not one names what a hospital intends to buy.** The brief's hunch was
half right: the seminar is worthless, but it pointed at IROP, and the intent is in (A).

**I.** `isoss.gov.cz`, `www.isoss.gov.cz`, `isoss.cz`, `isoss.digitalniaustan.gov.cz` — all
four returned **proxy 502 on CONNECT**. Unreachable from here; host unconfirmed.

**J.** `api.centralnideska.cz` covers OHL-56a/56b, U29, V49, P50, P52 — **bailiff notices
only**, not `záměry` or resolutions.

**K.** "SCSP" resolves to nothing verifiable (nearest: SCHP, chemicals; SOCR, retail). The
interrupted run's "SCSP verified" could not be reproduced.

---

## Browser vs curl — the honest ToS position

Only one real case appeared: **eDesky**. A human browser solves the Anubis proof-of-work;
curl cannot. But the operator publishes an API behind a free key — so driving a headless
browser through the PoW gate would circumvent an access control deliberately erected, to get
data offered freely by another door. **Use the key.** Elsewhere the gap is smaller than
folklore suggests: A–D all yielded to plain curl with a browser User-Agent.

---

## THE TOP 5

**1 · MS2021+ `SeznamOperaci` — the approved-project ledger.**
*This week:* `curl -o ops.xml https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml`, stream
it, and pull every project since 2026-01-01 whose `<ZAD><IC>` is a hospital or municipality.
*Cannot give:* buyers outside EU funding, and the crowns are grant money, not own-pocket
budget — so it proves intent and a deadline, not unsubsidised willingness to pay.

**2 · eDesky API — 6,346 noticeboards, and `záměr` means intention.**
*This week:* register at `edesky.cz/uzivatel/edit` for the free key, then pull one week of
documents and count how many are `záměry`. *Cannot give:* structured amounts — most documents
are PDFs, so every CZK figure costs an extraction step.

**3 · CityVizor payments — what a Czech public buyer actually pays.**
*This week:* `GET cityvizor.cz/api/public/profiles/5/payments` (Praha) and grep the
`description` field for a category the register already has a record on. *Cannot give:*
intention — this is executed spend, and only 35 of 338 bodies expose it.

**4 · RVIS — the minutes, and the one named role worth emailing.**
*This week:* read `Zapis_RVIS_2026-06-29.pdf` and decide in 20 minutes whether it names unmet
needs; if it does, the standing channel is a quarterly, plainly-identified email to a named
ministry **koordinátor digitální agendy**. *Cannot give:* any guarantee of a reply — an
officer's answer is a courtesy, never a feed, and must never be scored as one.

**5 · usneseni.cz — 151,645 council resolutions.**
*This week:* fetch `sitemap.xml.gz`, count how many of the 359 municipalities are publicly
readable, and read the terms of use before writing a single line of scraper.
*Cannot give:* legal certainty — it is a vendor's property, and the ToS is unread.

---

## What in the brief is NOT worth doing

**Sending people to events.** The brief's most expensive idea and its weakest. A person in a
room converts one day into a handful of unciteable impressions, and this register's whole
discipline is that every claim carries a source. `SeznamOperaci` names ~39,000 buyers with
committed amounts for the cost of one curl; a conference badge names perhaps five, off the
record. If an event ever matters, attend for the *relationship*, and never let the trip
produce a record.

**IROP applicant seminars.** Verified and killed: the decks explain the rules, not the needs.

**A cultivated officer as a private back-channel.** Worth doing as (4) — a named public role
emailed quarterly, in the open. Not as a private channel: unciteable evidence cannot enter a
public register, and a source who can be embarrassed by publication is one you will
eventually protect instead of publish.

**Rebuilding price discovery.** The brief asked for the query route to what a Czech buyer
pays. It already exists — `fetch_smlouvy.sh` reads the official registr smluv bulk dump
(97.1% of contracts with both IČOs resolved) and `fetch_hlidac.sh` adds full-text. What is
missing is not a source but a **two-hour query recipe**: full-text the dump for a category's
keywords, take the median signed value, and file it against the record. Do that instead of
adding a feed.

**ISoSS, Centrální úřední deska, SCSP.** One unreachable, one wrong scope, one unreproducible.
