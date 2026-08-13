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
