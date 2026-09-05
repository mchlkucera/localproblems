# New signal sources — catalog (source-discovery run 2026-08-13)

Scope: bottom-up demand evidence (documented complaints, unmet needs) and
institutional problem statements, to complement the existing feeds (TED,
Hlídač, reg-scan, YC/rounds, arb-scan). Ranked by expected value to the weekly
pipeline. Fetchability is stated honestly — several of the best sources are
PDFs or 403 generic fetchers and need a real UA header or manual reads.

Harvested today → `demand-scan.jsonl` (27 records). Prefixes minted beyond the
suggested set, same convention: `fa-`, `mpo-`, `coi-`, `sukl-`, `smo-`, `eru-`.

---

## Tier 1 — add to weekly pipeline first

### 1. NKÚ — kontrolní závěry + tiskové zprávy
- URL: https://www.nku.cz/cz/pro-media/tiskove-zpravy/ (listing also at https://www.nku.cz/scripts/modules/column/default.php?categid=29&dlid=1; Věstník: https://www.nku.cz/scripts/rka/vestnik.asp)
- Yields: audited, quantified systemic state failures — per-audit press releases with CZK amounts, failure rates, missed legal deadlines (e.g. 73bn CZK road repairs vs ~1% of overload violations fined; 30bn CZK university funding with no outcome tracking; e-health 6 years late).
- Fetchability: HTML scrape. `www.nku.cz` returns 403 to generic fetchers; **non-www `nku.cz` works**. No usable RSS found. ~2–6 releases/month.
- Cadence: weekly.
- Verdict: highest signal density of institutional problem statements in CZ — every release is a pre-verified problem record.

### 2. Veřejný ochránce práv (ombudsman) — news + quarterly reports + ESO database
- URL: https://www.ochrance.cz/aktualne/ · quarterly PDFs at https://www.ochrance.cz/zpravy_o_cinnosti/ · opinions database https://eso.ochrance.cz/
- Yields: complaint counts by agenda every quarter (Q1/2026: 2,341 total — social security 477, health 190, building law 156), research reports (age discrimination, harassment), systemic warnings (illegal senior homes). One-off gem: the March 2026 systemic-problem inventory — ~200 topics + 800 public submissions.
- Fetchability: news HTML fetches cleanly; quarterly reports are PDFs (parse 1 page of stats); ESO is a searchable web DB (scrapeable).
- Cadence: weekly news, quarterly PDF.
- Verdict: the single best bottom-up complaint aggregate in the country; the agenda counts give the register a standing demand index.

### 3. EC Have Your Say — consultations + feedback
- URL: https://have-your-say.ec.europa.eu/ (JSON backend: `ec.europa.eu/info/law/better-regulation/brpapi/` search endpoints)
- Yields: EU-level problem statements (calls for evidence state the problem being fixed) and countable public feedback per initiative — documented stakeholder pain (DFA consultation: dark patterns, cancellation friction; Digital Omnibus: 25–35% admin-burden cut target; CSDDD guidelines closing 2026-08-14).
- Fetchability: undocumented but stable JSON API used by researchers; site itself is a JS SPA (WebFetch gets nothing — use the API).
- Cadence: weekly.
- Verdict: programmatic EU demand feed that complements reg-scan's deadline feed; feedback counts are an objective demand proxy.

### 4. SÚKL — drug availability (open data)
- URL: https://sukl.gov.cz/pacientske-organizace/dostupnost-leciv/ · https://opendata.sukl.cz/
- Yields: live supply-interruption reports (mandatory for marketing-authorisation holders) and the "omezená dostupnost" flag = machine-readable unmet need in health, drug by drug.
- Fetchability: open data / structured DB — the only true API-grade source in this catalog.
- Cadence: weekly.
- Verdict: best fetchability-to-value ratio; third parties (GLP-1 trackers) already prove the demand.

### 5. ČOI — press releases + annual report
- URL: https://coi.gov.cz/ (press archive by month, e.g. /2026/04/; annual report PDF each April)
- Yields: violation rates per inspected segment (2025 e-shops: 85% of 751 inspected broke the law, 2,399 breaches itemized; Q1/2026 discount checks: ~40%), fines, complaint (podání) counts — a compliance-gap map of consumer-facing business.
- Fetchability: HTML scrape (some paths 404 — use the dated archive); annual PDF.
- Cadence: weekly-to-monthly.
- Verdict: enforcement stats double as product checklists for compliance tooling; already feeds one register record (accessibility act).

## Tier 2 — monthly/quarterly additions

### 6. Finanční arbitr — annual report + press releases
- URL: https://finarbitr.gov.cz/cs/informace-pro-verejnost/aktuality/ (VZ 2025: 2026-05-29)
- Yields: dispute counts by financial product with growth rates — currently documenting a genuine crisis (12,050 new proceedings 2025, +113% YoY; consumer-credit disputes 2,097→11,386 in two years; ~20,000 projected 2026).
- Fetchability: HTML news + annual PDF.
- Cadence: quarterly check (annual report each May).
- Verdict: sharpest live demand signal in consumer finance; one page of numbers a year, all load-bearing.

### 7. MPO — consumer-policy strategy reports + ADR platform stats
- URL: https://mpo.gov.cz/cz/ochrana-spotrebitele/ (this cycle: Zpráva o průběžném plnění Strategie spotřebitelské politiky 2025, March 2026)
- Yields: the only cross-sector ADR aggregate (FA ~18.7k, ČOI ~18k, ČTÚ ~4.2k postal, ERÚ ~2.2k filings 2020–H1/2025), plus institutional self-diagnosis (ČOI inspections 29k→20k on flat budget; SVS/SZPI understaffing) and the collective-redress usage gap (1 class action since 7/2024).
- Fetchability: infrequent dense PDFs (~annual); requires PDF read, worth it.
- Cadence: annual + ad-hoc.
- Verdict: one PDF yielded three records today; treat each edition as a mini harvest.

### 8. Hospodářská komora ČR — surveys + position papers
- URL: https://www.komora.cz/blog/tiskove-zpravy/ (also republished at businessinfo.cz)
- Yields: quantified SME pain each January (2026: 58% labor costs, 51% qualified-worker shortage, 48% admin burden; construction 70.9%), plus komora comment letters that preview compliance friction.
- Fetchability: HTML; no clean RSS found.
- Cadence: monthly.
- Verdict: the business-side complaint counterpart to the ombudsman's citizen side.

### 9. ČŠI (Czech School Inspectorate) — thematic reports
- URL: https://www.csicr.cz/cz/DOKUMENTY/Tematicke-zpravy
- Yields: institutional problem statements for education from thousands of inspections/hospitace (school-failure prevention report from the 2024/25 survey; resilience report from ~7,000 lesson observations).
- Fetchability: PDFs; **site 403s generic fetchers** (needs browser UA). Not harvested into records today for that reason.
- Cadence: monthly check.
- Verdict: high-quality, underused; deserves a fetch script with proper headers.

### 10. Mapa zadluženi / IPŘP + PAQ Research
- URL: https://mapazadluzeni.cz/ · https://www.institut-predluzeni.cz/
- Yields: annual municipal-granularity debt-enforcement data (end-2025: 596k people, 3M proceedings, 545bn CZK; Bílina 18.6% of adults) — the structural household-debt layer under several fintech/legal problems.
- Fetchability: web map + downloadable data, annual refresh.
- Cadence: annual.
- Verdict: one strong record a year plus a dataset the register can link per-region.

### 11. NÚKIB — monthly incident overviews + annual report
- URL: https://nukib.gov.cz/cs/infoservis/aktuality/ (monthly "přehled kybernetických incidentů"), annual reports at /zpravy-o-stavu-kb/
- Yields: incident counts and types (2024 record: 268 incidents; 2025: 12 significant + 2 very significant), sector targeting — pairs with the NIS2/nZKB wave already tracked in the register.
- Fetchability: clean HTML monthly posts.
- Cadence: monthly.
- Verdict: steady, quantified; modest novelty per month, good freshness source for cyber records.

### 12. Svaz měst a obcí ČR — press + position papers
- URL: https://www.smocr.cz/cs/media/tiskove-zpravy
- Yields: the municipal unfunded-mandate list (housing-law contact points without funding, delegated-powers financing gap, non-pedagogical staff shift) — each item is a govtech/housing product lead with a named payer problem.
- Fetchability: HTML.
- Cadence: monthly.
- Verdict: reliable institutional problem statements from 8,400+ municipalities' representative.

### 13. ČKAIT — Z+i magazine + statements (and ČLK, ČAK by analogy)
- URL: https://zpravy.ckait.cz/ · https://www.lkcr.cz/ (ČLK) · https://advokatnidenik.cz/ (ČAK)
- Yields: first-hand professional pain: DSŘ digital-permitting failures with survey numbers (43% delayed, 22% of municipalities report blocked key projects, ~200M CZK sunk); ČLK: physician aging/shortage; ČAK: justice-system friction.
- Fetchability: HTML magazines, monthly issues.
- Cadence: monthly.
- Verdict: chambers are slow but their complaints are pre-validated by membership; ČKAIT currently the hottest (DSŘ 2.0 coming).

## Tier 3 — annual / manual / watchlist

### 14. ERÚ + ČTÚ complaint & monitoring stats
- URL: https://eru.gov.cz/media · https://ctu.gov.cz/ (monthly monitoring PDF, e.g. mz-2026-02.pdf with "evidence dotazů a stížností")
- Yields: sector complaint patterns (ERÚ 2025: missing billing, unreturned overpayments, 622 formal disputes; ČTÚ ADR dominated by postal services).
- Fetchability: ERÚ HTML; ČTÚ monthly PDF.
- Cadence: monthly-quarterly.
- Verdict: modest but steady; mostly enriches existing energy/telecom records.

### 15. Participatory budgets — Brno "Dáme na vás" (+ Praha per-district)
- URL: https://paro.damenavas.cz/ ; Praha: per-district portals + Změňte.to app (no central portal)
- Yields: repeated citizen asks with vote counts; Brno delivery gap (~1,200 proposals, 65 completed in 9 years) documents municipal execution as the bottleneck.
- Fetchability: Brno portal scrapeable per cycle; Praha fragmented (>20 sources) — laborious.
- Cadence: annual cycle (Brno proposals spring, voting Nov 1–30).
- Verdict: genuine bottom-up demand, low frequency; harvest Brno once per cycle, skip Praha until a central source exists.

### 16. NGO service-gap reports — Život 90, Člověk v tísni, IPŘP, Hestia
- URL: https://www.zivot90.cz/ · https://www.clovekvtisni.cz/ · https://www.hest.cz/
- Yields: service-gap numbers inside annual reports (Senior telefon: 13k+ callers/yr, loneliness in ~1 of 4 calls; >30% of 65+ live alone); debt-advisory caseloads.
- Fetchability: annual PDFs + occasional stat pages; numbers often undated on-site.
- Cadence: annual.
- Verdict: valuable for the who-suffers layer; verify every number against the PDF, sites recycle old stats.

### 17. Munipolis (ZmapujTo + Lepší místo merged) — civic defect reports
- URL: https://www.munipolis.cz/ (ZmapujTo/Lepší místo merged into it 2018–2023)
- Yields: in principle the largest citizen-complaint dataset in CZ (1,500 municipalities, 40k+ resolved defects) — in practice **closed**: no public API, no open stats, only PR aggregates.
- Fetchability: LOW. Annual PR harvest only, or a data partnership.
- Cadence: annual watchlist.
- Verdict: the data everyone wants and nobody can fetch; keep on watchlist, do not build against it.

### 18. CVVM / STEM / Eurobarometer — dissatisfaction surveys
- URL: https://cvvm.soc.cas.cz/ · https://www.stem.cz/ · europa.eu Eurobarometer
- Yields: trend-grade documented dissatisfaction (institutional trust, housing, healthcare access).
- Fetchability: monthly PDFs (CVVM is clean and regular).
- Cadence: monthly, low priority.
- Verdict: tier-3 context only — rarely record-grade alone. Caution: media recycle stale "surveys" (today's check exposed a March-2023 insurer poll circulating as current news).

### 19. University tech-transfer offices — CUIP, ČVUT, JIC (honest negative)
- URL: https://www.cuip.cz/ · https://www.jic.cz/
- Yields: checked for "problem calls" / industry challenges — what they actually publish is licensing offers, startup programs and events, not documented unmet needs.
- Fetchability: fine, but nothing to fetch for this register.
- Verdict: skip for the pipeline; revisit only if a TTO starts publishing industry problem statements.

---

## Next fetch scripts (in order)
1. **NKÚ press-release scraper** (non-www host, monthly diff) — highest record yield per run.
2. **ochrance.cz news + quarterly-PDF parser** (agenda-count table) — standing demand index.
3. **Have Your Say API poller** (open consultations + feedback counts, filter DG/topic).
4. **SÚKL open-data pull** (omezená dostupnost flags → health records).
5. **ČOI monthly archive scraper** (violation-rate extraction from TZ text).

Honorable mention: a one-page-per-year manual read of the MPO consumer-policy
report and the FA annual report — 30 minutes each, several records guaranteed.

---

## Wave-2 additions (expansion run 2026-08-14) — proven fetch routes

Discovered and used by the 13-collector expansion; each is script-ready:

- **NEN below-threshold tenders** — the "otevřená data" page 404s, but the portal is fully SSR:
  `nen.nipez.cz/en/verejne-zakazky/p:vz:typVZ=Maly_rozsah,Zjednoduseny,Podlimitni,Podlimitni_mimo_ZVZ&datumPrvniUver=<from>,<to>&page=N`
  (50 rows/page, matrix-param filters; `/vysledek` subpages carry actual price + supplier). ~5,000 notices/10 weeks, 697 buyers.
- **TED API v3 cross-country** — `scope` MUST be `"ALL"`; the default `LATEST` silently returns only today's OJ S edition.
- **EC Have Your Say backend** — `ec.europa.eu/info/law/better-regulation/brpapi/searchInitiatives?size=50&language=EN&feedbackStatus=OPEN` (the working filter; `receivingFeedbackStatus` is ignored) + `groupInitiatives/{id}` for feedback counts and problem statements. ec.europa.eu needs the sandbox network allowlist.
- **NKÚ audit conclusions** — press listing 403s, but `nku.cz/scripts/rka/vestnik.asp?rok=YYYY` lists every conclusion with PDF links (lowercase filenames; uppercase 301s to http). ~2/month.
- **SÚKL drug availability** — `opendata.sukl.cz` dataset `MR/mr.zip`, weekly-refreshed CSV with ATC codes; trivially diffable for outage trends.
- **Ombudsman quarterlies** — predictable URLs: `ochrance.cz/dokument/zpravy_pro_poslaneckou_snemovnu_YYYY/YYYY-N-q.pdf`.
- **EIC Accelerator winners** — EC publishes per-cutoff PDF lists (WebFetch can't decode them; download + local pdftotext works).
- **Government legislative plan** — the annual *Plán legislativních prací vlády* PDF is the single best CZ pipeline index (91 pp, text-extractable), paired with psp.cz tisky for stage tracking.

## Wave-3 additions (2026-08-15) — consumer search & community demand

Ported from the owner's prior `demand-signals` project (~/Documents/CODE/demand-signals,
Mar 2026) — the one demand channel institutional sources can't see: live consumer pain.

- **Google Suggest pain-miner** — `scripts/fetch_suggest.sh`. CZ pain-phrased prefixes
  ("proč je X tak", "X nefunguje", "alternativa k X", …) against
  `suggestqueries.google.com/complete/search?client=firefox&hl=cs`. Free, no auth,
  ~1 req/1.5s. Source key `suggest`, id `suggest-<sha1-8 of query>`.
- **Reddit search via RSS** — `scripts/fetch_reddit.sh`. r/czech, r/Brno, r/Prague,
  r/czechia: `/search.rss?q=…&restrict_sr=1` for pain terms + `/new.rss` firehose.
  Verified 2026-08-15: the public `.json` endpoints now 403 for ANY non-browser client —
  `.rss` serves with a descriptive User-Agent, rate limit ~1 req then 429 (curl
  `--retry --retry-delay 35` honors it). Source key `reddit`, id `reddit-<post id>`
  (post id from the entry link).
- **Lessons carried from demand-signals' real runs** (encoded in pipeline/PROCESS.md step 2):
  *engagement ≠ pain* — a Show HN launch once scored pain 100 and a news cycle
  clustered as a fake opportunity; record pain language only, never upvotes.
  *Source imbalance kills analysis* — one loud feed (HN 332 vs Reddit 3) made every
  "cross-source" cluster single-source; cap any one feed's share of the demand ledger.
  A `demand_score` with a source-diversity multiplier lives in that project's
  `src/analyze.py` — candidate for a future SCORING.md revision.

## Wave-4 additions (2026-09-03) — direct asks from problem owners

The sixth evidence type, `asks` (design: `docs/superpowers/specs/2026-09-03-asks-ledger-design.md`).
An ask is a named institution publicly stating a problem it wants solved, before any
procurement money is attached. The record is the statement and who made it; prizes,
team counts and winners are never recorded. Everything below was probed live on 2026-09-03.

**Admitted — two feeds, both `planned` until the fetchers land:**

- **TA ČR BETA2/BETA3 research needs** — `scripts/fetch_tacr.sh`, source `tacr`, id
  `tacr-<TT need id, lowercased>`. The only standing government problem bank in CZ: a
  ministry states a research need (TT-coded), TA ČR posts it with a supplier-consultation
  date, and a tender follows months later through NEN/TED. Feeds:
  `tacr.gov.cz/kategorie/beta3/feed/` (7 items, 4 with a TT-coded need) and
  `…/beta2/feed/` (10 items); category HTML has no pagination. Measured rate ~4 needs in
  14 months, and RVVI cut BETA3's budget in June 2026 — low volume is structural, not a
  fetch defect. Posts without a need (budget notices, outages) are dropped and counted.
- **Owner-set hackathon challenges** — `scripts/fetch_hackathons.sh`, source `hackathon`,
  id `hack-<sha1-8 of site|title>`. Six organizer sites whose challenges are set by a
  hospital, a city or a ministry — all plain HTML, HTTP 200 with a browser User-Agent,
  no auth, no ToS restriction found:
  `hackjakbrno.cz` (FN Brno, FNUSA, MOÚ, JINAG — 15 challenge boxes) ·
  `rakathon.cz` (FN Motol, MOÚ, FN Ostrava — 4 named challenges) ·
  `hackathon.upol.cz` (Olomoucký kraj + město Olomouc — "letošní témata", a 3.6 MB page) ·
  `idea13.cz` (MČ Praha 13 — 4 "Výzva č. N") ·
  `aimtechackathon.cz/hackathon` (City of Plzeň, Ottobock, NGOs — 5 challenges) ·
  `nakopniprahu.cz` (MHMP + OICT — 3 areas with sub-topics).
  About 35–45 statements per full pass; the pages are re-read every run and the ids are
  stable, so steady state is near zero new per run. Garant and contact lines are cut at
  the fetcher — the pages name people, and the ledger is public.

**Researched and NOT admitted to `asks`:**

- **Hackathon aggregators** — Devpost, Devfolio, HackTrack EU, lu.ma, MLH, hackathon.com,
  hackmania.cz. All fetchable, but between them they list ~5–15 CZ events a year and carry
  NO owner problem statements — an event title and a date, never the challenge. A pointer
  feed to pages we already read directly.
- **#hackujstát** — the state's own hackathon, but the topics are picked by the student
  teams, not stated by a ministry. Student-picked is the opposite of owner-set.
- **Petitions** — petice.com (7-day signature velocity is measurable) and e-petice.cz
  (the addressee is named). A petition is the public asking the institution, not the
  institution stating its problem; it stays `demand` evidence, where petitions already live.

**Documented follow-up, not built:**

- **NEN předběžné tržní konzultace** (preliminary market consultations) — the formal step
  between a stated need and a tender, and the natural third `asks` feed. The listing name
  filter `nen.nipez.cz/verejne-zakazky/p:vz:nazev=konzultace` returns 45 rows, but whether
  the bulk ISVZ files the NEN fetcher reads carry the procedure kind is UNVERIFIED, so
  nothing is built on it yet.

## Wave-5 additions (2026-09-04) — MS2021+ approved projects, as a LOOKUP not a feed

The first source admitted to answer the register's weakest question — **who paid how
much, and what problem did that buyer say it solved** — and the first one admitted
*without* a `data/feeds.json` row. Everything below was measured live on 2026-09-04.

**What it is.** `https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml` — MMR's open-data
export of every approved 2021-27 EU-cofinanced project in Czechia.
`LICENCE="Creative Commons (CC BY 4.0)"`, `AUTOR="Ministerstvo pro místní rozvoj"`,
default namespace `https://ms21xsd.mssf.cz/OpenData/v_1`. HTTP 200, **146,410,196 bytes**,
**40,988 `<PRJ>` records**, ETag *and* Last-Modified both served, no auth, no page cap.
Every project carries the beneficiary's own `<PROBLEM>` statement beside the approved
money and the buyer's IČO — a pairing nothing else in this catalog offers.

**WHY IT IS A LOOKUP AND NOT A FEED.** 40,988 projects each carrying real money would
flood `data/signals/**` (16,237 records today) and nearly all of them would pass
materiality. That is precisely the trap `smlouvy` is parked for, in the registry's own
words: *"a PER-ITEM feed whose items each score money 1 or 0 … walks straight into the
trap CONVENTIONS.md names for `hiring`"*, where the fix is aggregation before materiality.
Here the fix is stronger — **do not make it evidence at all**. There is no natural
aggregate that keeps the useful part (one buyer, one price, one problem statement), so
aggregating would destroy the very thing worth having. It lands in `data/lookup/`
(CONVENTIONS.md "Lookup layer": committed, never pruned, no evidence type, no date, no
score, not walked by `db.py`, `web/lib/data.ts` or the build gate) and is *queried on
demand* by the MATCH and SWEEP passes. **It gets no registry row, and that is the design,
not an omission.**

**What was built (four files, no edits to any shared file):**

- `scripts/fetch_ms21.sh` — argv `$1 = outdir` (the nku/tacr shape). Conditional GET into
  `data/raw/.cache/ms21/` sending BOTH validators (`--etag-compare` + `--time-cond` on the
  cached body's Last-Modified mtime); the cache holds the **body**, not just the ETag, so a
  304 can still rebuild the index. MODE-A guard before anything is promoted. Manifest row +
  `.fetch/receipts.jsonl` in the `fetch_tacr.sh` shape — verified inert, since `normalize.py`
  consults receipts as `receipts.get(feed_key)` per *registered* feed only.
- `scripts/ms21_index.py` — stdlib, `iterparse` (never `ET.parse` — the file is 146 MB),
  writes `data/lookup/ms21-public-projects.jsonl`: **26,048 rows, 24,030,188 bytes
  (22.9 MB)**, built in 4.4 s. Contact-shaped text is cut with `normalize.py`'s EMAIL_RE /
  PHONE_RE (copied, with the comment saying so).
- `scripts/ms21_query.py` — `--keyword` (case- and diacritic-insensitive over
  name+problem+goal+theme), `--region`, `--min-czk`, `--ico`, `--limit`, `--json`. Prints
  the buyer, the money, the buyer's own problem statement, and a paste-ready citation.
  Results are ordered by money, largest first.
- `scripts/ms21_selftest.py` — 54 offline checks, all passing.

**Four measurements that changed the design:**

1. **`<PROBLEM>` is a non-answer on 58% of public rows.** It is present on all 40,988
   records, but of the 26,048 public ones **7,885 say `-`, 7,328 say `nerelevantní`** and
   one says `nerelevantní.` — 15,214 placeholders; only 10,834 carry a real statement. A placeholder is OMITTED
   rather than written into a field called `problem` (the empty-`quote` rule), and the
   query tool says so out loud on those rows.
2. **Two money blocks, and they disagree.** Every `<PRJ>` carries two `<PF>` blocks
   distinguished only by `<T>`; both are present on 100% of public rows and **the totals
   differ on 553 of them**. The reader takes `T=1` and, with no `T=1` block, writes no
   money at all rather than falling back.
3. **`<S>` (own/private share) exists on only 510 of 26,048 public rows.** Public bodies
   book their non-EU part under `CNV` instead. `own_czk` therefore means exactly "the `S`
   element" and nothing else; the query tool shows `total − EU` separately and labels it
   *(dopočet)*, because folding a subtraction into `own_czk` would be one field carrying
   two questions.
4. **5,070 rows report no actual start and no actual end.** Their citation gets an EMPTY
   `date`, which fails `check-records.py` loudly — better than a substituted
   export-publication date that would pass the build while claiming a commitment that
   never happened on that day.

**Which beneficiaries count as public — by `ZAD/HPF`, measured, 26,048 rows:** 331
příspěvková organizace (16,237) · 801 obec (6,826) · 641 školská právnická osoba (742) ·
804 kraj (628) · 601 veřejná vysoká škola (387) · 325 organizační složka státu (378) ·
332 státní příspěvková organizace (309) · 771 dobrovolný svazek obcí (241) · 661 veřejná
výzkumná instituce (126) · 301 státní podnik (90) · 811 městská část (50) · 352 státní
organizace (24) · 382 státní fond (10).
**Refused, each for a stated reason:** 100 (941) is *podnikající fyzická osoba* and the
measured names are people ("Zdeněk Jaroš"); 141 o.p.s. (976) and 722 církevní právnická
osoba (428) are contractors *for* public money, not the buyer of it; business forms
(112/121/…) are the counterparty side; the `P01…P54` codes (24) are Polish partner bodies
in Interreg — public, and not Czech. **One admitted form is mixed:** 641 is a legal form
for *schools* whose founder may be a municipality, a private person or a diocese, so a
record citing a 641 row must name the founder and must not call it "the state". Every row
carries `legal_form` so the caller can see which one it got.

**THE CITATION RULE — and the url is a constant on purpose.** A record cites a project as
a `type: price` source: `url` = `https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml`
(the whole dataset), the project `KOD` in `note`, `payer` = the beneficiary,
`amount_czk` = `total_czk`, `unit: one-off`, `basis: signed-contract` (an approved
MS2021+ operation is a signed grant agreement, not a list price and not a tender line),
`date` = the project's actual start. **The same url on every project is BY DESIGN — this
export has no per-project permalink — and it is the shape `coi`, `sukl` and `mpsv` already
use**, which data/CONVENTIONS.md states outright: *"`coi` / `sukl` / `mpsv` emit whole
aggregate families under one constant dataset url BY DESIGN. Merging on url alone would
delete 504 real records."* The KOD in `note` is the identifying key. `ms21_query.py` prints
this in the note of every citation it emits, so the next dedupe pass does not "fix" it.

**Follow-up, not built:** `data/CONVENTIONS.md`'s "Lookup layer" paragraph still lists only
the two e-shop files as the tree's contents; it needs a third line naming this one. Left to
the owner because that file is shared.

## Wave-5b additions (2026-09-05) — CityVizor invoices, as a LOOKUP not a feed

The executed-spend counterpart of Wave-5: where MS2021+ says what a public buyer was
*approved* to spend, CityVizor says what its accounting ledger *actually paid*, invoice
line by invoice line, with the counterparty's IČO — below every tender threshold. Same
shape as the ms21 lookup on purpose (`data/CONVENTIONS.md` "Lookup layer"). Everything
below was measured live on 2026-09-05 and read against the server source
(github.com/cityvizor/cityvizor, branch `staging`, AGPL-3.0; the data are published
voluntarily by the bodies, the app is run by Otevřená města z.s.).

**Verified endpoints and fields.** `GET https://cityvizor.cz/api/public/profiles` — 338
profiles (`id`, `url` = page slug, `name`, `ico`, `status`, `type`, `parent`,
`hasPayments`), **35 with payments, 26 of them `status: visible`**. `GET
…/profiles/{id}/payments` — one row per ledger line: `profileId`, `year` (the BUDGET
year), `paragraph`, `item` (rozpočtová položka), `event`, `incomeAmount`,
`expenditureAmount`, `date`, `counterpartyId` (IČO), `counterpartyName`, `description`.
`GET …/profiles/{id}/payments/months` — the distinct (year, month) pairs a body holds. No
auth, no robots.txt, no rate-limit header, no licence statement beyond the app's AGPL.

**The 10,000-row cap, and the honest way past it.** `server/src/routers/public/
profile-payments.ts` clamps `limit` with `parseAndLimitNumber(req.query.limit, 10000)`,
honours `offset`, `sort` (`date`/`-date`, which adds `date IS NOT NULL`), `dateFrom` (`>=`)
and `dateTo` (`<`, **exclusive**) — and reads **no `year` and no `month` parameter at
all**, which is why the 2026-09-04 probe saw them "silently ignored". There is no page
token. The fetcher therefore walks each body through DISJOINT date windows — the whole
range, then calendar years, then months, then days — splitting a window only when it comes
back holding exactly 10,000 rows (a capped window is a truncated window by definition).
Disjoint windows never overlap, so nothing is fetched twice and nothing is deduplicated
away. Only a single DAY over the cap would need `offset` paging, where Postgres gives no
stable order across pages; such windows are flagged `paged=1` and counted. **Measured run:
72 calls, 93,177,726 bytes, 48 s of transfer, 62 windows accepted, 0 failures, 0 paged
windows** — five bodies capped at the two-year range and split into years, two (Ostrava 37,
Královéhradecký kraj 364) capped at 2025 and split into months. Every request carries
`sort=date`, exactly what the site's own invoices page sends. Rows with a NULL date are
unreachable through date windows and are not fetched — a dateless line could not carry a
dated receipt anyway.

**Which bodies — 26 walked, 25 with rows in the window.** `status: visible` AND
`hasPayments`: Nové Město na Moravě, Černošice, Uherský Brod, Úvaly, Mariánské Lázně,
Kroměříž, Brno-Medlánky, Moravská Třebová, Bystřice, Benešov, Lysá nad Labem, Karlovarský
kraj, Středočeský kraj, Královéhradecký kraj, and Ostrava with eleven of its obvody
(Moravská Ostrava a Přívoz, Hošťálkovice, Mariánské Hory a Hulváky, Martinov,
Michálkovice, Plesná, Poruba, Slezská Ostrava, Svinov, Třebovice, Vítkovice). **Refused,
each for a stated reason:** the 9 non-visible profiles with payments are six test profiles
("Testicek", "aaaaa", "bbb", "Úvaly-test", "Ostrava-test", "test_po"), Kladno (not one
dated month), Ostrava-Jih (`pending`, 2019–2020 only) and **Hlavní město Praha (`pending`,
no IČO, ledger ends 2019)** — so the "profile 5 = Praha" of the 2026-09-04 note is not
reachable as a citable page. Mariánské Lázně is walked but its ledger ends 2022, hence 25
bodies with rows. Ostrava's parent profile is the magistrát alone (0 lines shared with
Poruba in March 2024 — measured), so all twelve Ostrava profiles are needed. **The twelve
Ostrava profiles carry no IČO** (34,919 rows, 43%): `body_ico` is omitted there, never
invented, and the citation's `payer` is the profile name.

**What was built (four files, no edits to any shared script):**

- `scripts/fetch_cityvizor.sh` — argv `$1 = outdir` (the nku/tacr shape). Profiles list,
  guarded; the window walk; raw JSON under `<outdir>/.fetch/cityvizor/<id>/`, a
  `windows.tsv` of accepted windows (capped windows renamed `.capped`, kept as evidence,
  never indexed); one manifest row + `.fetch/receipts.jsonl` for feed_key `cityvizor`
  (inert to `normalize.py`, which reads receipts per registered feed only). A failed window
  is an ERROR and the index is NOT rebuilt — a missing month would read as "bought nothing".
  1 s sleep between calls; curl retries 429/5xx twice. No `rm`, bash 3.2, `LC_NUMERIC=C`.
- `scripts/cityvizor_index.py` — stdlib. MODE-A guards for the profiles list and for every
  payments response (the Angular shell as 200 text/html, an error object, and a reshaped
  view all refused; an EMPTY ARRAY accepted — a month with no invoices is a real answer).
  Writes `data/lookup/cityvizor-invoices.jsonl`: **80,286 rows, 30,149,595 bytes (28.75
  MiB)**, sorted by (date, body, id), byte-stable across rebuilds.
- `scripts/cityvizor_query.py` — `--keyword` (case- and diacritic-insensitive over
  description + counterparty), `--body`, `--min-czk`, `--year` (budget year), `--ico`
  (counterparty), `--limit`, `--json`. Money first; the footer prints total AND median,
  because a ledger repeats (twelve instalments are twelve rows).
- `scripts/cityvizor_selftest.py` — **84 offline checks, all passing.**

**Five measurements that changed the design:**

1. **Most of a ledger is not a price.** Over six 2024 samples (35,709 expenditure lines)
   the rozpočtová položka classes were 51xx 29,034 · 61xx 2,293 · 53xx 1,087 · 52xx 1,015 ·
   58xx 1,689 · 50xx 389. The index admits **504x + 51xx + 61xx** only: 5331 (příspěvek to
   an own PBO), 52xx grants, 5011 payroll and 5362 taxes are money moved, not a thing
   bought; 58xx is entirely "Ubytování uprchlíků" at the decree rate — a compensation, not
   a negotiated price, and it is out so that `basis: signed-contract` never lands on a
   decree rate. **504x is admitted on purpose: 5042 is where a software licence renewal is
   booked** ("prodloužení licence ESET PROTECT", Středočeský kraj) — "51xx and 61xx" would
   have silently dropped exactly the rows a software record wants. Run totals: 192,383
   lines read; skipped income 20,794 · negative 7,406 · rounds-to-zero 34 · non-purchase
   12,801 (53xx 6,146 · 52xx 3,509 · 54xx 1,031 · 50xx 793 · 58xx 774 · 63xx 375 …).
2. **Two years does not fit under 30 MB, and the brief's fallback is not enough.** The
   two-year range yields 151,348 purchase lines at 375 bytes each ≈ **54 MB**. So the
   indexer keeps whole months, newest first, and drops the OLDEST month across ALL bodies
   until the file fits: **kept 2025-07-01 … 2026-08-31 (14 months), ten months trimmed
   (2024-09 … 2025-06)**. The fetcher prints the kept window and writes it into the
   receipt; everything fetched stays under `.fetch/` for the run directory's 28 days, so a
   wider index is a re-run of the indexer, not a re-fetch.
3. **Identical lines are real.** 6,582 rows are byte-identical to another line of the same
   body (one invoice split across two `event`s, two receipts of the same fee) — and the
   site's own page shows them twice too. The public view exposes no row id, so `id` is
   `cv-<profileId>-<sha1[:12]>` over the RAW source values, with `-2`, `-3` … on the second
   and later identical lines. Content-hash dedupe would have deleted 6,582 payments.
4. **Counterparty IČO is present on 99.4% of rows** — the field a price receipt most
   needs is the one this source fills best. Contact-shaped text (8 lines) is cut with
   `normalize.py`'s EMAIL_RE/PHONE_RE, copied with the comment saying so.
5. **Bodies upload monthly, in arrears.** The latest line on 2026-09-05 is dated
   2026-08-31; September is empty for every body. A run is never "current to today".

**THE CITATION RULE — a url per body per month, on purpose.** A record cites a line as a
`type: price` source: `url` = `https://cityvizor.cz/<slug>/faktury;rok=YYYY;mesic=M` (the
body's invoice table for that month — Angular matrix params, the very link the site's own
date picker builds in `client/…/date-picker.component.ts`), the row `id` in `note`,
`payer` = the body, `amount_czk` = the line's expenditure in whole crowns, `unit: one-off`,
`basis: signed-contract` (a ledger line is money paid under an order or contract already
performed — not a list price, not a tender line), `date` = the booking date. **There is no
per-invoice permalink anywhere on cityvizor.cz** — the public view has no invoice id — so
every line of one body in one month shares a url, which is the constant-url shape `coi`,
`sukl`, `mpsv` and `ms21` already use by design. Verified in a headless browser
2026-09-05: `cityvizor.cz/nmnm/faktury;rok=2026;mesic=8` renders the month's table with
date, §, #, IČO, counterparty, description and amount, matching the API rows. The query
tool prints the ms21 subject-test warning on every hit: a paid invoice for X is a price
for X only.

**Three real hits for `software`** (341 lines across 18 bodies, 39,530,214 Kč in total,
median 20,569 Kč): Ostrava paid SoftwareONE Czech Republic s.r.o. (IČO 24207519)
**20,745,750 Kč** on 2026-01-23 for "podpora produktů Microsoft pro rok 2026" (položka
5168); Ostrava paid the same SoftwareONE **3,265,693 Kč** on 2026-01-20 for "poskytování
licencí a podpor k produktům Microsoft, pro rok 2026"; Středočeský kraj (IČO 70891095)
paid ESET software spol. s r.o. (IČO 26467593) **1,924,506 Kč** on 2026-04-27 for
"Prodloužení licence ESET PROTECT Elite 11.5.2026–11.5.2029". And one for the register's
own vocabulary: `spisova sluzba` typed without diacritics finds Královéhradecký kraj paying
Axians Czech Republic s.r.o. **48,352 Kč a month** for "hostovaná spisová služba".

**Follow-ups, not built:** the twelve Ostrava profiles' missing IČO could be resolved from
ARES by name, but that is an enrichment step with its own receipt, not a fetch; Praha
would be the largest ledger in the country and is `pending` with data to 2019 — worth an
email to cityvizor@otevrenamesta.cz asking whether the city still uploads.
