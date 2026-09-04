# run manifest — 2026-09-03 (attended agent harvests)

Monthly broad passes of the four scan feeds per pipeline/SCANS.md plus one topic sweep per pipeline/SWEEP.md. Records staged per agent into staged-<feed>.jsonl, merged into staged.jsonl by the orchestrator and appended through a single `normalize.py --complete`.

## arb-scan pass — 2026-09-03

Monthly BROAD pass (pipeline/SCANS.md), evidence_type `funded`, source `arb-scan`,
id prefix = ISO2 of the origin country. 12 records staged to
`data/raw/2026-09-03/staged-arb-scan.jsonl`. No commits, no normalize run, no
ledger touched by this agent.

### Registry changes needed

- **`data/feeds.json` → `arb-scan.id_prefixes`: add `"us"`.** Two records this pass
  are United States comps — `us-polimorphic` and `us-prepared` — and `us` is not in
  arb-scan's array today. Checked against every registry row: `us` is claimed by
  **nobody**, so widening arb-scan creates no second claimant and no AC-F3
  UNATTRIBUTED risk. The records are written with the correct prefix per the brief;
  the widening must land **before** the append.
- Nothing else. `de`, `fr` and `gb` are already claimed by arb-scan; no scripted
  prefix (`ted-`, `hlidac-`, `nen-`, `smlouvy-`, `mpsv-`, `veklep-`, `coi-`,
  `sukl-`, `echys-`, `nku-`, `round-`, `yc-`) was minted.

### The checklist source for this feed: THE CATEGORY-ROTATION DUTY

arb-scan's checklist in `pipeline/SCANS.md` is not a URL list — it is the duty to
cover all 12 categories of the `data/CONVENTIONS.md` taxonomy over N passes,
recording per pass which categories were covered and the rotation state. Every one
of the 12 is named below, as the checklist law requires.

**Rotation state read at the start of this pass — and how it was read.** The
2026-08-24 and 2026-08-25 manifests contain **no arb-scan section and no rotation
state at all** (`grep -in 'arb-scan\|rotation'` over both returns nothing). That is
expected rather than a defect: the rotation duty was written into `SCANS.md` on
2026-08-25, so no prior pass was ever asked to record state, and **this is the
first pass to record it.** State was therefore derived from the committed ledger
instead — every `source: arb-scan` record in `data/signals/funded/*.jsonl`, grouped
by sector and by run date. Two arb-scan harvests exist: `2026-08-13` (8 records)
and `2026-08-14` (167 records). **All 12 categories carry the same last-swept date,
2026-08-14**, so "longest-unswept" could not be resolved on dates. The tie-break
used, and stated here so the next pass can reproduce or reject it, is **cumulative
depth**: the thinnest categories were treated as the least swept.

| category | last swept BEFORE this pass | records before | covered this pass | records added | last swept AFTER |
|---|---|---|---|---|---|
| govtech | 2026-08-14 | 1 | **YES** (thinnest) | 3 | 2026-09-03 |
| other | 2026-08-14 | 4 | **YES** | 1 | 2026-09-03 |
| mobility | 2026-08-14 | 6 | **YES** | 2 | 2026-09-03 |
| education | 2026-08-14 | 7 | **YES** | 1 | 2026-09-03 |
| environment | 2026-08-14 | 7 | **YES** | 3 | 2026-09-03 |
| housing | 2026-08-14 | 8 | **YES** | 2 | 2026-09-03 |
| legal-compliance | 2026-08-14 | 9 | no — next in line | 0 | 2026-08-14 |
| retail-services | 2026-08-14 | 14 | no | 0 | 2026-08-14 |
| energy | 2026-08-14 | 16 | no | 0 | 2026-08-14 |
| fintech | 2026-08-14 | 19 | no | 0 | 2026-08-14 |
| health | 2026-08-14 | 22 | no | 0 | 2026-08-14 |
| b2b | 2026-08-14 | 62 | no | 0 | 2026-08-14 |

**The next pass starts at `legal-compliance`, then `retail-services`, `energy`,
`fintech`, `health`, `b2b`** — the six still sitting at 2026-08-14, in ascending
depth. The six swept today are the youngest and go to the back of the queue.

### What each covered category found

**govtech — 3 records** (was the single thinnest category in the whole taxonomy at
one record, `cz-munipolis`).
- `de-vialytics` — AI road-condition assessment for municipalities, EUR 8M led by
  Acton Capital, 2024-12-18, 500+ partner municipalities in 7 countries. CZ check
  found only static `pasport komunikaci` vendors (T-MAPY, GisOnline, Pasportujeme,
  PORTAL OBCE) — adjacent, not the continuous AI re-scan model. No direct player.
- `us-polimorphic` — AI front desk + CRM + payments for local government, USD 18.6M
  Series A led by General Catalyst, 2025-07-09. CZ check found **direct but early**
  players on the chatbot slice only: Citymind (Tessa, live at Mokra-Horakov and on
  the Prague 6 site), Galileo Corporation, sefbot. Recorded as contested, not absent.
- `us-prepared` — AI transcription, translation and triage for emergency call
  centres, USD 80M Series C, 2025-05-30. **No Czech vendor found**, and the demand is
  documented: the Fire Rescue Service of the Czech Republic is one of eight European
  public-safety answering points piloting exactly this in the EENA AI special
  project, with four foreign suppliers and no Czech one.

**mobility — 2 records.** Both checks found a Czech player; both are recorded as
contested rather than absent, and that is the finding.
- `fr-padam-mobility` — demand-responsive transport for rural and peri-urban
  networks; acquired by Siemens Mobility 2021-05-11, terms confidential, 70+
  localities at acquisition. CZ check found **CITYA mobility s.r.o.** (ICO 13975471,
  since 2021) running the same model — Ricany 2022, FlexOK for the Olomoucky region,
  SaaS licensing to municipalities, plus tests in the Pardubicky and Liberecky
  regions.
- `de-peter-park` — barrier-free AI parking management sold to operators, Great Hill
  Partners growth investment 2025-06-03, total funding stated above EUR 100M, ~250
  cities. CZ check found **Parkum s.r.o.** (ICO 19584903, since 2023) direct but
  early, and Cross Zlin as an adjacent hardware integrator.

**education — 1 record, and the second slot is a named gap (below).**
- `gb-zen-educate` — marketplace matching schools directly with supply teachers,
  USD 37M Series B 2024-05-21 alongside the Aquinas Education acquisition. **CZ check
  found nothing in either language**: the Czech query returns only the shortage
  itself (several thousand missing teachers, worst in physics, informatics and
  mathematics, filled by unqualified staff) and the state SYPO project; the English
  query returns only American and British platforms.

**environment — 3 records.**
- `de-dryad-networks` — ultra-early wildfire detection sensor mesh, EUR 6.3M
  2024-10-22, ~EUR 22M total. **No Czech vendor found.** What exists is state demand:
  the WEDS feasibility study with the Fire Rescue Service closed on 2026-06-10 with
  60+ experts, and every vendor the English query returns is foreign.
- `de-resourcify` — enterprise waste and recycling management platform, EUR 14M
  Series A 2023-09-27, users include McDonald's, REWE, Hornbach, Frankfurt Airport.
  CZ check found **CYRKL Zdrojova platforma s.r.o.** (ICO 07565305) direct on the
  marketplace half; INISOFT, JRK DIGITAL, Tectronik and Sensoneo adjacent on
  statutory evidence and bin IoT.
- `de-recyda` — packaging compliance and recyclability software, EUR 6.3M led by
  Cusp Capital 2024-10-24, customers Beiersdorf, Kao, Trolli. CZ check found ELO's
  PPWR module (direct, early) and otherwise only advisory firms. **The only record
  this pass carrying urgency 3** — the EU packaging regulation applies from
  12 August 2026, so the conformity-documentation duty is in force now.

**housing — 2 records.**
- `de-hallo-theo` — takes the management mandate for residential buildings and runs
  it with AI, EUR 10M seed from Insight Partners 2025-02-03, 9,000+ apartments. CZ
  check found software vendors (Bydloo, BYTYO, STARLIT) and traditional service
  firms, but nobody doing both halves. Czech SVJ are legally obliged to be
  administered, so the buyer set is fixed.
- `de-aedifion` — cloud optimisation of building HVAC on top of the existing control
  system, EUR 17M Series B led by Eurazeo 2025-06-24, ~500 buildings / 5.8M m². CZ
  check found BUILDSYS, HGS FLOWBOX, Novatec EAS and the international vendors as
  adjacent; the taxonomy/ESG reporting layer is sold by consultancies, not by a
  building-operations product.

**other — 1 record.**
- `de-arx-robotics` — software-defined unmanned ground vehicles plus Mithra OS,
  EUR 42M Series A including the July 2025 extension. CZ check found a **populated
  hardware field** — VOP CZ (TAROS, state enterprise), VTU (UGV-Pz), LPP Holding
  (Hornet, 2025), MRAZ Robotics — and **no Czech supplier of the vehicle-agnostic
  autonomy OS or a retrofit kit**. Dated demand: a UGV fielding concept approved
  June 2026 and a dedicated test range at Lipnik nad Becvou.

### Categories NOT covered this pass — stated, not silent

`legal-compliance`, `retail-services`, `energy`, `fintech`, `health`, `b2b` were
not swept. Reason: they are the six deepest-covered categories in the ledger
(9 to 62 arb-scan records each) and the rotation duty says to start from the
longest-unswept, which on the depth tie-break is the other six. They carry the
oldest last-swept date in the register from now on and **the next pass owes them
first**, in the order given above.

### Coverage gaps

1. **Education second record — screened and refused, not skipped.** Two candidates
   were examined and neither was staged. *Multiverse* (GB, USD 70M at a USD 2.1B
   valuation, early 2026, 22,000+ apprentices, 1,500+ employers) was rejected on
   transfer logic: the model is built on the UK apprenticeship levy, a tax mechanism
   with no Czech analogue, so a Czech version would have no funding rail. *Knowunity*
   (DE, EUR 27M Series B) sits in the consumer study-help slice, which is crowded in
   Czechia — **but that was not absence-checked, so no absence and no presence is
   claimed here.** A future pass owes education a second candidate.
2. **Listing-page walks were not possible.** `eu-startups.com/category/funding/` →
   HTTP 403; `vestbee.com/insights/articles` → 404; `tech.eu/category/funding/` →
   404 to WebFetch. Candidate discovery therefore ran through web search rather than
   a systematic sweep of the European funding listings. A future pass with a working
   fetch of those indexes would find candidates this one could not see — this is the
   most likely source of misses in this manifest.
3. **Publisher blocks cost four records their `quote`.** `businesswire.com`,
   `finsmes.com`, `techfundingnews.com` and `bebeez.eu` returned 403/404 to
   WebFetch. `us-polimorphic`, `us-prepared`, `de-resourcify`, `de-aedifion` and
   `de-arx-robotics` are therefore staged **with the `quote` key omitted entirely**
   rather than with an unverifiable snippet; their funding facts come from search
   result text plus, where reachable, an alternative page. Seven records carry a
   verbatim quote read directly off the cited page.
4. **Surfaces not searched.** Every note states only what was actually checked —
   `google-cz`, `ares` (live ARES REST lookups) and `own-funded-ledger` on all
   twelve, plus `app-stores` on the Padam check only (FlexOK on Google Play).
   `cz-saas-directories`, `eshop-addon-marketplaces` and `startupjobs` were **not**
   searched this pass, so no note claims them. An absence written here is an absence
   against those three surfaces and nothing wider.
5. **`de-resourcify` and `fr-padam-mobility` predate the "funded since 2024"
   preference** (2023-09-27 and 2021-05-11). Both were kept because the model and its
   traction are proven and the Czech picture they document is current; noted so the
   date is not read as an error.

### Positive control — passed

Run before any absence was written, and re-runnable. `google-cz`: the query
"Wultra mobilni bankovni autentizace zabezpeceni ceska firma" surfaced Wultra on the
first page (Euro.cz, CzechCrunch, Lupa, Forbes, Hrot24); "Ringil dopravni software
TMS pro prepravce ceska firma" surfaced Ringil on the first page (ringil.com,
Podnikatel.cz, LinkedIn). `ares`: the REST name search returned **Wultra s.r.o.,
ICO 03643174, since 2014-12-15** and **Ringil s.r.o., ICO 09194673, since
2020-05-27**. The method finds the register's standing controls, so a negative from
it is evidence rather than a vibe. The ARES surface also positively identified every
Czech player named above, which is the same method producing positives inside this
pass.

### COVERAGE — already in the corpus, deliberately not re-minted

Grepped `data/signals/*/*.jsonl` (16,144 ids in `seen.txt`) for every candidate
before minting. Existing ids that stopped a record being written:

- `round-dwelly` — Dwelly (GB), AI-first lettings and property management, USD 170M
  Series B July 2026. Was the strongest housing candidate; already held via the
  `round` feed.
- `round-mobility-signage` — Mobility Signage (DE), unified IT for public transport
  operators, EUR 1.8M, April 2026. Was a mobility candidate; already held.
- `yc-verdant` — Verdant, AI-native land-use permit management for local government —
  and `yc-permitportal`, PermitPortal, AI pre-construction and permits. The govtech
  permit-review slice is already covered, so CivCheck- and Symbium-style candidates
  were dropped rather than duplicated.
- `reg-mzp-557-2025-odpady` — vyhlaska 557/2025 Sb on waste evidence; cited inside
  the `de-resourcify` note as the Czech regulatory context rather than re-stated as a
  new record.
- `cz-munipolis` — the register's only pre-existing arb-scan govtech record; distinct
  model (municipal citizen messaging), no overlap with the three staged today.

No candidate collided with an id in `seen.txt`; all 12 staged ids are new. None is
dropped by the materiality filter (`money <= 1 AND scale <= 1 AND urgency == 0`) —
the two with `money: 0` (`fr-padam-mobility`, `de-peter-park`, both undisclosed
amounts, no estimate made) survive on `scale: 2`.

### Pass summary

1. Feed: **arb-scan** (evidence_type `funded`, monthly broad pass, attended).
2. Checklist sources visited: **12 of 12 categories named**; 6 of 12 swept this pass
   (govtech, other, mobility, education, environment, housing), 6 explicitly deferred
   with reason.
3. Records staged: **12** in `data/raw/2026-09-03/staged-arb-scan.jsonl` — govtech 3,
   environment 3, mobility 2, housing 2, education 1, other 1. Seven carry a verbatim
   quote; five omit the key.
4. Coverage gaps named: **5** — education's second slot, the blocked funding-listing
   indexes, the publisher 403s that cost five records their quote, the three
   `checked` surfaces not searched, and two records older than the 2024 funding
   preference.
5. Rotation state: govtech · other · mobility · education · environment · housing →
   **2026-09-03**; legal-compliance · retail-services · energy · fintech · health ·
   b2b → **2026-08-14**, and the next pass starts there in that order.

## demand-scan pass — 2026-09-03

Monthly BROAD pass (pipeline/SCANS.md), feed `demand-scan`, evidence_type
`demand`, records staged to `data/raw/2026-09-03/staged-demand-scan.jsonl`
(8 records, all `extraction: manual`). No commit, no normalize.py, no db.py,
no edits to feeds.json / signals / seen.txt.

### Registry changes needed

**One prefix widening is required before the append, or the build fails on
AC-F3 (every `source` value and id prefix in `data/signals/**` must be claimed
by a registry row).**

- **`ecsem`** — 4 records (`ecsem-cz2026-housing`, `ecsem-cz2026-admin-burden`,
  `ecsem-cz2026-ltc-mix`, `ecsem-cz2026-csr`). Add `"ecsem"` to the
  `demand-scan` row's `id_prefixes` in `data/feeds.json`. `source` stays
  `demand-scan`; no new source value, no schema change, no new feed.
  **Why a new prefix rather than an existing one:** demand-scan's prefixes are
  reporting bodies, and none of the fifteen names the European Commission or
  the Council. `consult-` was the tempting fit and is the wrong one — all 34
  committed `consult-` records are Have-your-say consultations/initiatives
  (`ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/NNNNN`),
  and a Country Report and a Council Recommendation are neither. Filing them
  under `consult-` would put a false reporting body on the record, which is the
  one thing the prefix is for.
- **`nku` — NO WIDENING WANTED, deliberately.** 3 records this pass carry the
  `nku-` prefix, which the `nku` FEED row claims (`id_prefixes: ["nku"]`) and
  demand-scan's row does not. That is correct as it stands and must be left
  alone: the `nku` row's `signal_source` is already `demand-scan`, so the
  records wear no false receipt, and `db.py attribute_prefixes` sends `nku-` to
  the single capable claimant. Adding `nku` to demand-scan.id_prefixes would
  create TWO capable claimants and send every `nku-` record in the corpus to
  UNATTRIBUTED — the exact failure the `coi` and `sukl` rows warn about in their
  own blockers, citing the `nku` precedent. CONVENTIONS.md's schema line already
  lists `nku-` among the demand-scan reporting-body prefixes, so the prefix is
  sanctioned; only the registry attribution is (rightly) exclusive.

### Checklist source 1 — NKÚ kontrolní závěry (PARSE THE PDFs)

Visited. Věstník index `https://www.nku.cz/cz/publikace-a-dokumenty/vestnik/`
(200) and RSS `https://nku.cz/cz/rss.xml` (200) both resolve. Věstník 3/2026 of
13 August 2026 carries nine conclusions (24/24, 25/03, 25/05, 25/07, 25/08,
25/09, 25/11, 25/12, 25/15); Věstník 1/2026 of 8 April 2026 carries ten
(24/22, 24/26, 24/28, 24/29, 24/30, 24/31, 24/33, 25/02, 25/04, 25/06).

Method: `curl` each `https://nku.cz/assets/kon-zavery/kNNNNN.pdf` (the https
form 301s to a lower-case http path; the `www.nku.cz` form serves 200 directly
and is what the records cite), then `pdftotext -layout`, then read the ZJIŠTĚNÉ
SKUTEČNOSTI and I. Shrnutí a vyhodnocení sections for the quantified failure and
the named responsible body. Existence probe run over k25013–k25025 and
k26001–k26005 to find anything newer than the last pass.

**3 records minted** (all conclusion PDFs, none from an RSS headline):

| id | action | responsible body | quantified failure |
|---|---|---|---|
| `nku-majetkove-ucasti` | 25/03 | MF, MPO, MZe | 7 of 21 State Ownership Policy Strategy measures unmet; 37 companies, 127bn CZK; 235.6bn CZK budget money in 2020–2024 |
| `nku-msmt-horizont-kontroly` | 24/29 | MŠMT (recipient breaches at DZS) | zero public-administration controls at any recipient 2016–2024 over 604.2m CZK; no measurable indicators for CZELO/CZERA |
| `nku-up-ucetni-zaverka-2025` | 25/21 | Úřad práce ČR (under MPSV) | 3.5bn CZK of bookkeeping defects, corrected only after NKÚ raised them; systemic weaknesses |

**Read and DROPPED, with the reason** — silence is forbidden, so these are named:

- **24/33 (ochrana měkkých cílů)** — read (k24033.pdf, 200). NOT minted: the
  corpus already holds `nku-mekke-cile` for the same audit, cited from the NKÚ
  press release of 9 February 2026. A second record on the same conclusion is
  the differently-worded duplicate CONVENTIONS.md warns about; the deeper PDF
  reading is handed to MATCH rather than re-minted.
- **24/22 (National Sports Agency), 25/15 (ÚOOÚ), 25/16 (ČSÚ), 25/20 (Akademie
  věd)** — all four read. All four conclude *bez významných nesprávností* after
  corrections: clean financial-statement audits with no pain language. 25/20's
  370.2m CZK and 25/15's 120.2m CZK were corrected pre-closing with no systemic
  finding, unlike 25/21. Not minted, by the pain-language bar.
- **24/29's headline verdict is POSITIVE** and is recorded as such in the record's
  own `notes`: proposal success rose 40 → 60 percent and cost per assist halved.
  The record exists for the control-system gap, not for a failed programme.
  Stated here so nobody later reads the record as a verdict on the programme.

**Named coverage item — 25/14 (IKEM), approved but unpublished.** The 12th
Kolegium session of 17 August 2026 approved the conclusion of audit 25/14,
*Majetek a peněžní prostředky, se kterými je příslušný hospodařit Institut
klinické a experimentální medicíny*. Its PDF is not published:
`https://nku.cz/assets/kon-zavery/k25014.pdf` → **404**, and there is no
Věstník 4/2026 yet. Also 404: k25013, k25018, k25019, k25022–k25025,
k26001–k26005. What a future pass owes it: re-probe k25014.pdf and the Věstník
index; this is the newest substantive conclusion in the pipeline and the only
one this pass could not read.

**Broken URL noted, not fatal:** `https://www.nku.cz/cz/kontrola/kontrolni-akce/`
and `https://www.nku.cz/cz/kontrola/kontrolni-zavery/` both return **404** — the
per-action listing pages named in older notes no longer resolve. The Věstník
index plus direct `assets/kon-zavery/kNNNNN.pdf` probing is the working route and
is what this pass used.

### Checklist source 2 — European Semester CZ package

Visited, and it was **an empty stream in the corpus until this pass**: a grep of
all six ledgers for `semester`, `country report` and `country-specific
recommend` returned exactly one hit, `reg-csrd-post-omnibus`, which is an
unrelated CSRD record. Nine years of Semester packages had never produced a
signal.

- **2026 Country Report — Czechia**, SWD(2026) 203 final, 3 June 2026. Landing
  page `country-report-czechia_en` (200), PDF fetched (200, 4.2 MB) and read
  with `pdftotext -raw`. **3 records minted** — `ecsem-cz2026-housing`,
  `ecsem-cz2026-admin-burden`, `ecsem-cz2026-ltc-mix`. All three quotes verified
  verbatim against the fetched PDF text after whitespace collapse.
- **Council CSR**, document **11115/26** (ECOFIN 905) of 3 July 2026, adopted by
  the Council **10 July 2026**; Commission proposal COM(2026) 203 final of
  3 June 2026. Both fetched (200) and read. **1 record minted** —
  `ecsem-cz2026-csr`. Diff worth carrying: the Council **dropped** the
  Commission's *"through property and income tax reforms"* from the housing
  recommendation and softened *"reforming municipal tax assignment rules"* to
  *"adjust municipal tax assignment rules, if relevant"*.
- **Partial gap, named:** no **OJ C** reference for the adopted 2026 CSR could be
  found. The Commission's own Semester-documents page for Czechia lists the
  country report and the Commission recommendation and **no Council-adopted
  CSR**. The record therefore cites the Council document rather than an OJ
  citation. A future pass owes an OJ C lookup for the Czechia recommendation of
  10 July 2026 and, if found, a `notes` addition on `ecsem-cz2026-csr` — not a
  new record.

### Checklist source 3 — MPSV Statistická ročenka, chapter 5 "Sociální služby"

Visited. `https://mpsv.gov.cz/statisticka-rocenka-z-oblasti-prace-a-socialnich-veci-archiv`
fetched (200, 1.3 MB). **Newest edition listed is "Statistická ročenka z oblasti
práce a soc. věcí v roce 2024"** (a `.7z` bundle under `/cms/documents/`); no
2025 edition, and no 2025 chapter-5 XLSX anywhere on the page. The non-archive
path `.../statisticka-rocenka-z-oblasti-prace-a-socialnich-veci` returns **404**,
so the archive page is the canonical location and was searched in full.

**EXPECTED ABSENCE, not a coverage gap**, exactly as SCANS.md item 3 provides
for: the edition lands around September and today is 3 September 2026. Zero
records. The 2024 edition's tab 5.9 is already held as
`civic-mpsv-rocenka-neuspokojene-2024` (70,209 unmet domovy pro seniory
applications), so there is nothing unharvested in the newest published edition
either. Next pass: re-check for the 2025 edition and diff tab 5.9 against 70,209
DS / 37,849 DZR / 4,043.

### Checklist source 4 — Ombudsman ESO (HTML walk, no RSS)

Visited, and this source **splits into two halves with two different outcomes**.

**Quarterly reports — COVERED, 1 record minted.** The Q2 2026 report to the
Chamber of Deputies (`.../zpravy_pro_poslaneckou_snemovnu_2026/2026-ii-q.pdf`,
200, file number KVOP-40911/2026/S) fetched and read: 2,509 complaints, up 132
year on year, 79.8 percent in mandate, social security 523 / health 205 /
building 192, 107 unequal-treatment claims, 7 facility visits, 1 deportation
monitored. Minted as `ombud-q2-2026`, continuing `ombud-q1-2026`. Q3 2026 is not
due until after 30 September 2026.

**Systematic-visit reports — NAMED COVERAGE GAP, with a FAILED POSITIVE CONTROL.**
`https://www.ochrance.cz/eso/zpravy/` resolves (200) but is a **taxonomy
explainer**, not a report list: it names the eleven ESO document types
(including *Souhrnná zpráva z návštěv zařízení — § 21c*) and links to the search
app. The app at `https://eso.ochrance.cz/` is a POST-driven search
(`/Vyhledavani/Search`, no anti-forgery token). The POST **succeeds** — HTTP 200,
"Nalezené" results page — but returns **zero rows**, and the same POST for
`Rok=2024, Agenda=NZ`, a year that certainly holds systematic-visit reports,
returns the **byte-identical 13,448-byte empty page**. The control fails, so by
the register's own rule the method has found a broken method and not an absence:
**no absence is written and no record is minted from this half.** The results are
almost certainly loaded by a session-scoped or AJAX call this pass did not
reproduce. What a future pass owes it: drive the ESO search from a real browser
session (or find its JSON endpoint), verify against a known 2024
*Souhrnná zpráva*, and only then read 2026 systematic-visit output.

**Aktuálně stream walked as well** (`https://www.ochrance.cz/aktualne/`, 200,
page 1 of 103), covering everything published since the newest committed
`ombud-` record (`ombud-vek-diskriminace`, 13 August 2026). Nothing new minted,
with reasons:

- 5 August 2026, pay-transparency transposition missed — **already covered** by
  `reg-pay-transparency-cz`, which records the 7 June 2026 deadline as missed.
  Handed to reg-scan rather than duplicated in `demand`.
- 19 August 2026, police press releases and mental-health privacy — a change the
  office **obtained**, not a standing unmet need.
- 27 August 2026, health-insurer debt-notification failure — a single case,
  scale 0.
- 9 July 2026, dignity in elder care and unregistered facilities — **already
  covered** by `ombud-nelegalni-domovy` (23 June 2026).

### Dedup done before minting

- `grep -c '' data/signals/seen.txt` → **16,144** ids indexed.
- All 8 minted ids probed against `seen.txt`: **0 hits**, none pre-existing.
- Existing corpus enumerated per prefix before writing: 38 `nku-`, 14 `ombud-`,
  34 `civic-`, 34 `consult-`, 3 `chamber-`, 2 `ngo-`, 0 `uni-`, plus
  `cnb-`/`ctu-`/`eru-`/`fa-`/`mpo-`/`smo-`/`spcr-` singletons.
- COVERAGE found and therefore NOT re-minted: `nku-mekke-cile` (= audit 24/33),
  `nku-urad-prace` (= audit 24/32, distinct from 25/21),
  `nku-dia-ucetnictvi` (same failure class as 25/21, different body),
  `civic-mpsv-rocenka-neuspokojene-2024` and `civic-mpsv-ltc-predikce-2035`
  (the bed-count half of the long-term-care picture; `ecsem-cz2026-ltc-mix` is
  the spending-mix half and says so in its notes), `ombud-detsky-q2-2026` plus
  `ombud-autismus-sluzby`, `ombud-detske-domovy-budovy` and `ombud-svepravnost`
  (three thematic records already citing the Q2 2026 PDF, which makes that url a
  shared key and correctly EXEMPT from identity-key dedup),
  `reg-pay-transparency-cz`.

### Receipts

Every `url` returned **200** on a final liveness check at harvest time and every
record carries `http_status: 200` and `fetched_at: 2026-09-03T17:45:00Z`. All 8
`quote` values were machine-verified as literal substrings of the fetched payload
after whitespace collapse (`pdftotext` output for the seven PDFs) — recorded
because an agent-harvest quote degrades to a manifest warning rather than a hard
refusal, so the check is only worth anything if it is stated. Money is converted
at **24.5 CZK/EUR**, the rate the committed `nku-` records already use; three
records carry `money_eur: null` with a note saying the source publishes no
figure, rather than a guess.

### Pass summary

```
feed:                     demand-scan (monthly broad pass, evidence_type demand)
checklist sources:        4 of 4 visited (NKU / European Semester / MPSV rocenka / ombudsman ESO)
records staged:           8  (3 nku- · 4 ecsem- · 1 ombud-)
coverage gaps named:      2  (NKU 25/14 conclusion PDF unpublished — 404;
                              ESO systematic-visit search — positive control FAILED, no absence written)
                          + 1 expected absence (MPSV rocenka 2025 edition not yet published)
                          + 1 partial (no OJ C reference for the adopted 2026 CSR)
rotation state:           n/a — category rotation is arb-scan's duty
registry change needed:   add "ecsem" to demand-scan.id_prefixes; do NOT add "nku"
```

## dotace-scan pass — 2026-09-03

Monthly broad pass of the `dotace-scan` feed (`data/feeds.json` key `dotace-scan`,
`signal_source: dotace`, `evidence_type: tenders`, `id_prefixes: ["dotace"]`).
Records: `data/raw/2026-09-03/staged-dotace-scan.jsonl`, 14 lines, every one
`source: dotace`, `evidence_type: tenders`, prefix `dotace-`, `extraction: manual`.
No commit, no `normalize.py`, no `db.py`, no edits to `data/feeds.json`,
`data/signals/**` or `seen.txt` — the orchestrator concatenates and completes.

### Registry changes needed

**None.** Every id minted this pass uses the `dotace-` prefix that this feed's
registry row already claims, and every record carries `source: dotace`, which the
`SignalSchema.source` enum already accepts (54 committed records use it).

### Checklist source 1 — MS2021+ open-data call list (SCANS.md dotace-scan item 1)

`https://ms21opendata.mssf.cz/SeznamVyzev_21_27.xml` — **HTTP 200, 1,666,518 bytes,
fetched 2026-09-03**. Payload `DATE` attribute `2026-09-02T20:45:00.000+02:00`;
author Ministerstvo pro místní rozvoj; licence CC BY 4.0. Snapshot kept at
`data/raw/2026-09-03/ms21-SeznamVyzev_21_27.xml` (gitignored, pruned at 28 days).
817 `VYZVA` entries, 817 distinct `KOD` values.

**THE DIFF HAD NO LEFT-HAND SIDE, AND THIS IS THE FIRST PASS TO SAY SO PLAINLY.**
Neither `data/raw/2026-08-24/manifest.md` nor `data/raw/2026-08-25/manifest.md`
carries a dotace-scan call-id list. What 2026-08-24 does carry is a single measured
line — *"MS2021+ open data SeznamVyzev_21_27.xml (816 entries) carries only ESIF
programmes 01-14 — zero 31_* NPO calls"* — a count and a negative result, not the
ids. A count is not a diffable left-hand side: 816 → 817 is consistent with one
call added, and equally with nine added and eight retired. So this pass did two
things instead of one:

1. **Reconstructed a proxy left-hand side from the payload's own date fields.** A
   call counts as newly opened here when its `DATUMOTEVRENI` or its
   `DATUMZPRISTUPNENI` falls after **2026-08-25**, the date of that recorded
   measurement. This is weaker than an id diff and is labelled as such in every
   record's `notes`; it cannot see a call that was added to the XML with an older
   opening date, and that limitation is a named gap below.
2. **Recorded the full 817-code list as the new left-hand side** (below), so the
   next pass runs a real id diff and this reconstruction never has to happen again.

**Newly opened or newly announced since 2026-08-25 — 11 calls, 9 minted.**

| KOD | programme | opened | closes | allocation | outcome |
|---|---|---|---|---|---|
| `12_26_050` | 12 OP AMIF | 2026-08-28 | 2026-10-16 | 285,000,000 CZK | minted `dotace-amif-50-informace-cizincum-2` |
| `12_26_051` | 12 OP AMIF | 2026-08-31 | 2026-10-23 | 200,000,000 CZK | minted `dotace-amif-51-rekonstrukce-suz` |
| `12_26_052` | 12 OP AMIF | 2026-08-31 | 2026-10-30 | 110,000,000 CZK | minted `dotace-amif-52-vyuka-cj-ukrajina` |
| `13_26_020` | 13 OP FVB | 2026-08-31 | 2026-10-30 | 40,000,000 CZK | minted `dotace-fvb-20-prum` |
| `12_26_049` | 12 OP AMIF | 2026-09-01 | 2026-09-22 | 70,000,000 CZK | minted `dotace-amif-49-asistence-oamp` |
| `03_26_112` | 03 OP Z+ | 2026-09-02 | 2026-11-23 | 100,000,000 CZK | minted `dotace-opz-112-pas` |
| `01_26_091` | 01 OP TAK | 2026-09-04 (announced 08-21) | 2027-02-01 | 50,000,000 CZK | minted `dotace-optak-poradenstvi-3` |
| `04_26_044` | 04 OPD | 2026-09-14 (published 08-31) | 2026-11-30 | 100,000,000 CZK | minted `dotace-opd-44-rychlodobijeci-prioritni` |
| `04_26_045` | 04 OPD | 2026-09-14 (published 08-31) | 2026-11-30 | 150,000,000 CZK | minted `dotace-opd-45-bezne-dobijeci-mesta` |
| `01_26_086` | 01 OP TAK | 2026-09-01 | 2027-09-01 | 345,000,000 CZK | **COVERAGE — not re-minted** |
| `01_26_093` | 01 OP TAK | 2026-09-01 | 2027-09-01 | 195,000,000 CZK | **COVERAGE — not re-minted** |

`01_26_086` and `01_26_093` are the less-developed-region and transition-region
halves of *Technologie pro MAS (CLLD) — výzva II.*, and the corpus already holds
them as one record: **`dotace-optak-technologie-mas-2`** in
`data/signals/tenders/2026-08-14.jsonl`, money 22,000,000 EUR from "540M CZK",
which is exactly 345 + 195. Re-minting either half would have been a
differently-worded duplicate that the identity-key dedup could not catch, because
the urls differ (apiagentura.gov.cz vs optak.gov.cz).

**Excluded, with the reason stated:** `03_00_094` and `03_00_095` — both named
"Testovací (1)" and "Testovací (2)", state `Rozpracovaná`, allocation 0, dates
`2099-12-31`. These are the publisher's own test rows, not calls.

**Announced but not yet public — carried to the next pass, not minted:**
`05_26_107` (MŽP 107. výzva, SC 1.3, opatření 1.3.9, 162,500,000 CZK, opens
2026-10-14) carries a `DATUMZPRISTUPNENI` of **2026-09-30**, i.e. the publisher
says it is not accessible yet. `02_25_044` *Vzdělávání pro praxi a život*
(500,000,000 CZK, opens 2026-11-23), `02_25_045` *Výzkumné infrastruktury II*
(1,900,000,000 CZK, opens 2026-12-10) and `02_26_046` *Výzkumné e-infrastruktury
II* (600,000,000 CZK, opens 2026-12-10) are `Plánovaná` with no call text on
opjak.cz. Without a left-hand side this pass cannot tell whether they are new to
the XML, so it asserts nothing about them and hands them to the next pass.

### The call-id list to keep — MS2021+ `SeznamVyzev_21_27.xml`, 2026-09-03, 817 codes

Programme spread: 01 OP TAK 96 · 02 OP JAK 48 · 03 OP Z+ 112 · 04 OPD 48 ·
05 OP ŽP 109 · 06 IROP 122 · 07 OP TP 5 · 08 OP Rybářství 39 ·
10 OP ST 118 · 11 Interreg CZ-PL 22 · 12 OP AMIF 56 · 13 OP FVB 20 ·
14 OP NSHV 22. This block is the left-hand side for the next pass: diff it against
the next fetch's `KOD` set and the "newly opened" question answers itself.

```
01_22_001 01_22_002 01_22_003 01_22_004 01_22_005 01_22_006 01_22_007 01_22_008 01_23_009
01_23_010 01_23_011 01_23_012 01_23_013 01_23_014 01_23_015 01_23_016 01_23_017 01_23_018
01_23_019 01_23_020 01_23_021 01_23_022 01_23_023 01_23_024 01_23_025 01_23_026 01_23_027
01_23_028 01_23_029 01_23_030 01_23_031 01_23_032 01_23_033 01_23_034 01_23_035 01_23_036
01_23_037 01_23_039 01_23_040 01_23_041 01_24_038 01_24_042 01_24_043 01_24_044 01_24_045
01_24_046 01_24_047 01_24_048 01_24_049 01_24_050 01_24_051 01_24_052 01_24_053 01_24_054
01_24_055 01_24_056 01_24_059 01_24_060 01_24_061 01_24_062 01_24_063 01_24_065 01_24_073
01_25_057 01_25_058 01_25_064 01_25_066 01_25_067 01_25_068 01_25_069 01_25_070 01_25_071
01_25_072 01_25_074 01_25_075 01_25_076 01_25_077 01_25_078 01_25_079 01_25_080 01_25_081
01_25_082 01_25_083 01_26_084 01_26_085 01_26_086 01_26_087 01_26_088 01_26_089 01_26_090
01_26_091 01_26_092 01_26_093 01_26_094 01_26_095 01_26_096 02_22_001 02_22_002 02_22_003
02_22_004 02_22_005 02_22_006 02_22_007 02_22_008 02_22_009 02_22_010 02_22_011 02_22_012
02_23_013 02_23_014 02_23_015 02_23_016 02_23_017 02_23_018 02_23_019 02_23_020 02_23_021
02_23_022 02_23_023 02_23_024 02_23_025 02_23_026 02_23_027 02_23_028 02_23_029 02_24_030
02_24_031 02_24_032 02_24_033 02_24_034 02_24_035 02_24_036 02_24_037 02_24_038 02_25_039
02_25_040 02_25_041 02_25_042 02_25_043 02_25_044 02_25_045 02_26_046 02_26_047 02_26_048
03_00_094 03_00_095 03_22_001 03_22_002 03_22_003 03_22_004 03_22_005 03_22_006 03_22_007
03_22_008 03_22_009 03_22_010 03_22_011 03_22_012 03_22_013 03_22_014 03_22_015 03_22_016
03_22_017 03_22_018 03_22_019 03_22_020 03_22_021 03_22_022 03_22_023 03_22_024 03_22_025
03_22_026 03_22_027 03_22_028 03_22_029 03_22_030 03_22_031 03_22_032 03_22_033 03_22_034
03_22_035 03_22_036 03_22_037 03_22_038 03_22_039 03_22_040 03_22_041 03_22_042 03_22_043
03_22_044 03_22_045 03_22_046 03_22_099 03_22_100 03_22_101 03_23_047 03_23_048 03_23_049
03_23_050 03_23_051 03_23_052 03_23_053 03_23_054 03_23_055 03_23_056 03_23_057 03_23_058
03_23_093 03_23_096 03_24_059 03_24_060 03_24_061 03_24_062 03_24_063 03_24_064 03_24_065
03_24_066 03_24_067 03_24_068 03_24_069 03_24_070 03_24_071 03_24_072 03_24_073 03_24_074
03_24_075 03_24_076 03_24_077 03_24_078 03_24_079 03_25_080 03_25_081 03_25_082 03_25_083
03_25_084 03_25_085 03_25_086 03_25_087 03_25_088 03_25_089 03_25_097 03_25_102 03_25_103
03_25_104 03_25_105 03_25_106 03_25_108 03_25_109 03_25_110 03_26_090 03_26_091 03_26_107
03_26_111 03_26_112 03_27_092 03_27_098 04_22_001 04_22_002 04_22_003 04_22_004 04_22_005
04_22_006 04_22_007 04_22_008 04_22_009 04_22_010 04_23_011 04_23_012 04_23_013 04_23_014
04_23_015 04_23_016 04_23_017 04_23_018 04_23_019 04_23_020 04_23_021 04_23_022 04_23_023
04_24_024 04_24_025 04_24_026 04_24_027 04_24_028 04_24_029 04_24_030 04_24_031 04_24_032
04_24_033 04_24_034 04_24_035 04_25_036 04_25_037 04_25_038 04_25_039 04_25_040 04_25_041
04_25_042 04_25_043 04_26_044 04_26_045 04_26_046 04_26_047 04_26_048 05_22_001 05_22_002
05_22_003 05_22_004 05_22_005 05_22_006 05_22_007 05_22_008 05_22_009 05_22_010 05_22_011
05_22_012 05_22_013 05_22_014 05_22_015 05_22_016 05_22_017 05_22_018 05_22_019 05_22_020
05_22_021 05_22_022 05_22_023 05_22_024 05_22_025 05_22_026 05_22_027 05_22_028 05_22_029
05_22_030 05_22_031 05_23_032 05_23_033 05_23_034 05_23_035 05_23_036 05_23_037 05_23_038
05_23_039 05_23_040 05_23_041 05_23_042 05_23_043 05_23_044 05_23_045 05_23_046 05_23_047
05_23_048 05_23_049 05_23_050 05_23_051 05_23_052 05_23_053 05_23_054 05_23_055 05_23_056
05_23_057 05_23_058 05_23_059 05_23_060 05_23_061 05_23_062 05_24_063 05_24_064 05_24_065
05_24_066 05_24_067 05_24_068 05_24_069 05_24_070 05_24_071 05_24_072 05_24_073 05_24_074
05_24_075 05_24_076 05_24_077 05_24_078 05_24_080 05_24_083 05_25_079 05_25_081 05_25_082
05_25_084 05_25_085 05_25_086 05_25_087 05_25_088 05_25_089 05_25_090 05_25_091 05_25_092
05_25_093 05_25_094 05_25_095 05_25_096 05_25_097 05_25_098 05_25_099 05_25_100 05_26_101
05_26_102 05_26_103 05_26_104 05_26_105 05_26_106 05_26_107 05_26_108 05_26_109 06_22_001
06_22_002 06_22_003 06_22_004 06_22_005 06_22_006 06_22_007 06_22_008 06_22_009 06_22_010
06_22_011 06_22_012 06_22_013 06_22_014 06_22_015 06_22_016 06_22_017 06_22_018 06_22_019
06_22_020 06_22_021 06_22_022 06_22_023 06_22_024 06_22_025 06_22_026 06_22_027 06_22_028
06_22_029 06_22_030 06_22_031 06_22_032 06_22_033 06_22_034 06_22_035 06_22_036 06_22_037
06_22_038 06_22_039 06_22_040 06_22_041 06_22_042 06_22_043 06_22_044 06_22_045 06_22_046
06_22_047 06_22_048 06_22_049 06_22_050 06_22_051 06_22_052 06_22_053 06_22_054 06_22_055
06_22_056 06_22_057 06_22_058 06_22_059 06_22_060 06_22_061 06_22_062 06_22_063 06_22_064
06_22_065 06_22_066 06_22_067 06_22_068 06_22_069 06_22_070 06_22_111 06_22_112 06_23_071
06_23_072 06_23_073 06_23_074 06_23_075 06_23_076 06_23_077 06_23_078 06_23_079 06_23_080
06_23_081 06_23_082 06_23_083 06_23_084 06_23_085 06_23_086 06_23_087 06_23_088 06_23_089
06_23_090 06_23_091 06_23_092 06_23_093 06_23_094 06_23_095 06_23_096 06_23_097 06_23_098
06_23_099 06_23_100 06_23_101 06_23_102 06_23_103 06_23_104 06_23_105 06_23_106 06_23_107
06_23_108 06_23_109 06_23_110 06_23_113 06_23_114 06_24_115 06_24_116 06_25_117 06_25_118
06_26_119 06_26_120 06_26_121 06_26_122 07_22_001 07_22_002 07_22_003 07_22_004 07_22_005
08_22_001 08_22_002 08_22_003 08_23_004 08_23_005 08_23_006 08_23_007 08_23_008 08_23_009
08_23_010 08_23_011 08_23_012 08_23_013 08_23_014 08_24_015 08_24_016 08_24_017 08_24_018
08_24_019 08_24_020 08_24_021 08_24_022 08_24_023 08_25_024 08_25_025 08_25_026 08_25_027
08_25_028 08_25_029 08_25_030 08_26_031 08_26_032 08_26_033 08_26_034 08_26_035 08_26_036
08_26_037 08_26_038 08_26_039 10_22_001 10_22_002 10_22_003 10_22_004 10_23_005 10_23_006
10_23_007 10_23_008 10_23_009 10_23_010 10_23_011 10_23_012 10_23_013 10_23_014 10_23_015
10_23_016 10_23_017 10_23_018 10_23_019 10_23_020 10_23_021 10_23_022 10_23_023 10_23_024
10_23_025 10_23_026 10_23_027 10_23_028 10_23_029 10_23_030 10_23_031 10_23_032 10_23_033
10_23_034 10_23_035 10_23_036 10_23_037 10_23_038 10_23_039 10_23_040 10_23_041 10_23_042
10_23_043 10_23_044 10_23_045 10_23_046 10_24_047 10_24_048 10_24_049 10_24_050 10_24_051
10_24_052 10_24_053 10_24_054 10_24_055 10_24_056 10_24_057 10_24_058 10_24_059 10_24_060
10_24_061 10_24_062 10_24_063 10_24_064 10_24_065 10_24_066 10_24_067 10_24_068 10_24_069
10_24_070 10_24_071 10_24_072 10_25_073 10_25_074 10_25_075 10_25_076 10_25_077 10_25_078
10_25_079 10_25_080 10_25_081 10_25_082 10_25_083 10_25_084 10_25_085 10_25_086 10_25_087
10_25_088 10_25_089 10_25_090 10_25_091 10_25_092 10_25_093 10_25_094 10_25_095 10_25_096
10_25_097 10_25_098 10_25_099 10_25_100 10_25_101 10_25_102 10_25_103 10_25_104 10_26_105
10_26_106 10_26_107 10_26_108 10_26_109 10_26_110 10_26_111 10_26_112 10_26_113 10_26_114
10_26_115 10_26_116 10_26_117 10_26_118 11_22_001 11_22_002 11_23_003 11_23_004 11_23_005
11_23_006 11_23_007 11_23_008 11_23_009 11_23_010 11_23_011 11_24_012 11_24_013 11_24_014
11_24_015 11_24_016 11_24_017 11_25_018 11_25_019 11_25_020 11_25_021 11_26_022 12_22_001
12_22_002 12_22_003 12_22_004 12_23_005 12_23_006 12_23_007 12_23_008 12_23_009 12_23_010
12_23_011 12_23_012 12_23_013 12_23_014 12_23_015 12_23_016 12_23_017 12_24_018 12_24_019
12_24_020 12_24_021 12_24_022 12_24_023 12_24_024 12_25_025 12_25_026 12_25_027 12_25_028
12_25_029 12_25_030 12_25_031 12_25_032 12_25_033 12_25_034 12_25_035 12_25_036 12_25_037
12_25_038 12_26_039 12_26_040 12_26_041 12_26_042 12_26_043 12_26_044 12_26_045 12_26_046
12_26_047 12_26_048 12_26_049 12_26_050 12_26_051 12_26_052 12_26_053 12_26_054 12_26_055
12_26_056 13_22_001 13_23_002 13_23_003 13_23_004 13_23_005 13_23_006 13_23_007 13_23_008
13_24_009 13_24_010 13_24_011 13_24_012 13_25_013 13_25_014 13_26_015 13_26_016 13_26_017
13_26_018 13_26_019 13_26_020 14_22_001 14_22_002 14_23_003 14_23_004 14_23_005 14_23_006
14_23_007 14_23_008 14_24_009 14_24_010 14_24_011 14_25_012 14_25_013 14_25_014 14_25_015
14_25_016 14_26_017 14_26_018 14_26_019 14_26_020 14_26_021 14_26_022
```

### Checklist source 2 — the portals the feeds.json row names

The `dotace-scan` registry row names IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO and
CINEA/HaDEA. **All seven were visited on 2026-09-03.** Each is named below with
what it found, including "nothing new this pass" stated with what was checked.

**IROP** — `https://irop.gov.cz/cs/vyzvy-2021-2027`, HTTP 200. Ten calls listed on
the first page; the nine open ones are 120, 122, 121, 119, 117, 105, 104, 103 and
85, the newest of which opened **2026-04-30**. Nothing opened since 2026-08-25.
**COVERAGE — all nine are already in the ledger:**
`dotace-irop-120-kyberbezpecnost`, `dotace-irop-121-122-bezemisni-vozidla` (one
record covering both 121 and 122), `dotace-irop-119-cyklodoprava`,
`dotace-irop-117-izs-praha`, `dotace-irop-103-105-urgentni-prijmy` (one record
covering 103, 104 and 105) and `dotace-irop-85-verejne-zdravi`. Nothing minted.

**OPŽP** — `https://opzp.cz/nabidka-dotaci/`, HTTP 200 (the older
`opzp.cz/dotace/vyzvy/` path now 404s — noted, not a gap, the live path resolves).
Twelve entries with "Příjem žádostí probíhá": calls 109, 108, 106, 105, 104, 103,
102, 101, 79, 73, 72 and the SFŽP financial instrument 1/2025 FN — Odpady. The
newest opened **2026-07-16** (call 109). Nothing opened since 2026-08-25.
**COVERAGE — the eleven OPŽP calls are all in the ledger:**
`dotace-opzp-109-protipovodnova-ochrana`, `-108-antropogenni-rizika`,
`-106-svahove-nestability`, `-105-srazkove-sede-vody`, `-104-prirode-blizka-opatreni`,
`-103-oze-verejne-budovy`, `-101-102-uspory-energie` (one record for 101 and 102),
`-79-potravinove-banky`, `-73-vodni-prvky-krajina`, `-72-sanace-kontaminace`.
Nothing minted from OPŽP itself; the financial instruments are handled under SFŽP.

**OPJAK** — `https://opjak.cz/vyzvy/`, HTTP 200. Seven open calls: `02_25_043`
Open Science III, `02_26_048` Poradím se s AI, `02_24_036` Teaming-CZ III,
`02_25_042` Smart Akcelerátor+ II, `02_25_041` Akční plánování v území MAP II and
the two Technická pomoc calls `02_22_006` / `02_22_007`. Newest opening
**2026-07-20**. Nothing opened since 2026-08-25. **COVERAGE — the five
substantive ones are in the ledger:** `dotace-opjak-open-science-3`,
`-poradim-se-s-ai`, `-teaming-cz-3`, `-smart-akcelerator-2`, `-map-2`. The two
Technická pomoc calls are the programme's own administration budget, not a call a
builder can answer, and are deliberately not minted. Nothing minted.

**SFŽP** — `https://sfzp.gov.cz/dotace-a-pujcky/` plus the two live
financial-instrument call pages, all HTTP 200. Four financial instruments listed:
2/2026 FN — ČOV, 1/2026 FN — brownfieldy, 1/2025 FN — odpady, 1/2024 FN.
**Two are live, material and absent from the ledger, and both were minted:**
`dotace-sfzp-2-2026-fn-cov` (1,355.2 million CZK of 1 percent loans to intensify
wastewater plants of 10,000 population equivalent and above for Directive (EU)
2024/3019, applications 2026-07-02 to 2027-03-31) and
`dotace-sfzp-1-2026-fn-brownfieldy` (1,200 million CZK for the Ústí region plus
350 million CZK for Karlovy Vary, closing 2026-10-30). Neither is a diff hit —
both opened before the window — and each record's `notes` says so. `1/2025 FN —
odpady` and `1/2024 FN` were seen and not minted this pass: named here so the
omission is a decision rather than a silence, and owed to a future pass.

**TAČR** — `https://tacr.gov.cz/`, HTTP 200; the `vyhlasene-souteze/` and
`souteze/` paths 404, the live index is `programy-a-souteze/` and the front page
lists the current competitions. Six international-partnership calls surfaced.
**COVERAGE — two already in the ledger:** `dotace-tacr-dut-call-2026` (Driving
Urban Transitions) and `dotace-tacr-theta2-4vs` (THETA 2, fourth competition);
`dotace-tacr-water4all-2026` is in the ledger and no longer on the front page.
**Three live calls were absent from the ledger and were minted:**
`dotace-tacr-eurostars-3-call-11` (500,000 EUR, closes **2026-09-10**, seven days
out at harvest), `dotace-tacr-ramp-2026` (1,000,000 EUR, closes 2026-09-22) and
`dotace-tacr-cet-2026` (1,200,000 EUR, pre-proposals close 2026-10-08). All three
opened in June or July 2026, so they are portal-walk catches, not diff hits, and
each `notes` field says so. Also seen and not minted: the SIGMA eighteenth public
competition (DC1) page, which the front page links but which carries no allocation
figure on the listing — owed to a future pass.

**NPO** — `https://planobnovy.gov.cz/vyhlasene-vyzvy/`, HTTP 200 (note:
`planobnovycr.cz` redirects to `planobnovy.gov.cz`). Four distinct open calls:
Komponenta 2.10 Dostupné nájemní bydlení Výzva I (to 2026-12-31), NPO 14/2025
SECAP+ poradenství (to 2026-09-30), NPO 16/2025 základní poradenství — semináře
(to 2026-09-30) and NPO 2/2026 Renovační pas budovy (to 2026-11-30). Nothing new
this pass. **COVERAGE — all four are in the ledger:**
`dotace-npo-nrb-najemni-bydleni`, `dotace-npo-14-2025-secap-poradenstvi`,
`dotace-npo-16-2025-energeticke-seminare`, `dotace-npo-2-2026-renovacni-pas`.
Nothing minted. Confirming the 2026-08-24 negative result from the other
direction: the NPO portal's own call list and the MS2021+ XML do not overlap — the
XML carries only ESIF programmes 01-14, so NPO calls such as `31_24_138` are
receiptable from this portal and never from the open data.

**CINEA / HaDEA** — `https://cinea.ec.europa.eu/funding-opportunities/calls-proposals_en`
(40 calls, pages 1-3 read) and `https://hadea.ec.europa.eu/calls-proposals_en`
(10 calls), both HTTP 200. **Nothing opened after 2026-08-25 on either agency.**
The newest CINEA opening is 2026-08-04 ("EUR 131.5 million available for Horizon
Europe energy call", deadline 2026-12-01); the newest HaDEA opening is 2026-06-23
(`CEF-DIG-2026-CABLE-REPAIR-CAPACITIES`, deadline 2026-10-08). **COVERAGE — the
HaDEA calls the ledger already holds:** `dotace-digital-2026-edtech`,
`-health-ai-skills`, `-skills-coalitions` (all under `DIGITAL-2026-SKILLS-10`),
`dotace-digital-2026-ehds`, `-safer-internet` (both under
`DIGITAL-2026-BESTUSE-10`), plus `dotace-cef-transport-2026` and
`dotace-horizon-eccc-cyber-2026`. **Named and NOT minted, owed to a future pass:**
`CEF-DIG-2026-CABLE-REPAIR-CAPACITIES`, the SMP Food waste-prevention call
(deadline 2026-10-15), `HORIZON-CID-2026-01`, `HORIZON-MISS-2026-02-CANCER`, the
four `HORIZON-CL4-2026-03 (SPACE)` calls, and the LIFE-2026-CET family — of which
`LIFE-2026-CET-ENERCOM` (energy communities) and `LIFE-2026-CET-ENERPOV` (energy
poverty) are the two most relevant to this register. None of them is newly opened,
and **neither agency's listing page publishes a per-call budget**, so minting them
from these pages would have meant either `money_eur: null` on a call whose budget
is published elsewhere, or an estimate. Neither is acceptable; the Funding and
Tenders portal per-call budget lookup is the work a future pass owes them.

### Coverage gaps (named, not silent)

1. **No left-hand side existed for the MS2021+ diff.** The 2026-08-24 manifest
   recorded a count (816 entries) and a negative result, not the call ids, so a
   true id diff was impossible this pass. Mitigated with a date-field proxy and
   fixed forward by recording all 817 codes above. **What it cannot see:** a call
   added to the XML in the last week carrying an older `DATUMOTEVRENI` — that call
   would read as pre-window and be missed. The next pass, running a real id diff,
   will catch any such call retroactively.
2. **`optak.gov.cz` answers HTTP 403 to both WebFetch and Bash curl** with a
   browser user agent (measured twice: `optak.gov.cz/vyzvy/` and
   `optak.gov.cz/poradenstvi/a-29/`, both 403, 552-byte body). Worked around for
   `dotace-optak-poradenstvi-3` by using the implementing agency's own site,
   `apiagentura.gov.cz` (HTTP 200), which carries the same call. **A future pass
   owes:** a check of whether the block is user-agent, geography or rate related,
   and a decision on whether apiagentura.gov.cz becomes the standing OP TAK surface.
3. **The Interior Ministry call PDFs are not retrievable.** The AMIF and FVB call
   pages resolve HTTP 200 and name their PDFs, but the documents sit behind
   `merkur.mv.gov.cz/backend/api/file/documents/<id>`, which returns **HTTP 401
   with a 25-byte JSON body** both with and without the page's own `ts` query
   parameter. The four AMIF/FVB records therefore take allocation and deadline
   from the MMR open-data XML, and their `quote` is the XML record rather than the
   call text. Stated on each record. **A future pass owes:** the call PDFs, for
   the eligible-activity detail the open data does not carry.
4. **CINEA and HaDEA per-call budgets are not on their listing pages.** Ten
   ledger-absent live EU calls are named above and left unminted rather than
   receipted with a null or an estimate. **A future pass owes:** the Funding and
   Tenders portal budget lookup for at least `CEF-DIG-2026-CABLE-REPAIR-CAPACITIES`
   and `LIFE-2026-CET-ENERCOM`.
5. **Four live Czech calls seen and deliberately not minted this pass:** SFŽP
   `1/2025 FN — odpady` and `1/2024 FN`, TAČR SIGMA eighteenth public competition
   (DC1), and the OPJAK Technická pomoc pair. Recorded so the omission is auditable.

### Records staged — 14

| id | sector | money EUR | deadline | scale/money/urgency/recurrence |
|---|---|---|---|---|
| `dotace-amif-50-informace-cizincum-2` | govtech | 11,769,564 | 2026-10-16 | 2/3/3/2 |
| `dotace-amif-51-rekonstrukce-suz` | housing | 8,259,343 | 2026-10-23 | 0/3/3/1 |
| `dotace-amif-52-vyuka-cj-ukrajina` | education | 4,542,639 | 2026-10-30 | 2/3/3/2 |
| `dotace-fvb-20-prum` | govtech | 1,651,869 | 2026-10-30 | 1/2/3/1 |
| `dotace-amif-49-asistence-oamp` | govtech | 2,890,770 | 2026-09-22 | 2/3/3/2 |
| `dotace-opz-112-pas` | health | 4,129,672 | 2026-11-23 | 2/3/3/1 |
| `dotace-optak-poradenstvi-3` | b2b | 2,064,836 | 2027-02-01 | 2/3/3/2 |
| `dotace-opd-44-rychlodobijeci-prioritni` | mobility | 4,129,672 | 2026-11-30 | 2/3/3/2 |
| `dotace-opd-45-bezne-dobijeci-mesta` | mobility | 6,194,508 | 2026-11-30 | 2/3/3/2 |
| `dotace-sfzp-2-2026-fn-cov` | environment | 55,965,311 | 2027-03-31 | 2/3/2/3 |
| `dotace-sfzp-1-2026-fn-brownfieldy` | environment | 64,009,911 | 2026-10-30 | 2/3/3/1 |
| `dotace-tacr-eurostars-3-call-11` | b2b | 500,000 | 2026-09-10 | 1/2/3/2 |
| `dotace-tacr-ramp-2026` | environment | 1,000,000 | 2026-09-22 | 1/2/3/2 |
| `dotace-tacr-cet-2026` | energy | 1,200,000 | 2026-10-08 | 1/2/3/2 |

**Money method — no estimates.** Every `money_eur` derives from a published
allocation and nothing else. The nine Czech-programme calls convert their
published CZK allocation at **24.215 CZK/EUR**, the daily rate printed on
`opd3.opd.cz` on 2026-09-03 ("Aktuální kurz eura: 24,215 Kč") — a state-published
rate on a page fetched in this pass, not a rate looked up elsewhere. The rate and
the source CZK figure are written into every `money_note`. The three TAČR records
carry TAČR's own EUR figure with no conversion at all. No record on this pass
carries a derived, inferred or rounded-up allocation, and no record was written
whose allocation is unpublished.

**Quote verification.** Every `quote` was checked **programmatically** as a literal
substring of the whitespace-collapsed fetched payload before the record was
written — the build script asserts it and refuses to emit otherwise. Nine quotes
come from the MS2021+ XML, one from `esfcr.cz`, one from `apiagentura.gov.cz`, two
from `opd3.opd.cz`, two from `sfzp.gov.cz` and three from `tacr.gov.cz`. All are
≤300 characters, Czech preserved, whitespace collapsed. Agent-harvest quotes
degrade to a manifest warning rather than a hard refusal at ingest, which is
exactly why the check was run here instead.

**Dedup.** All 54 committed `dotace-` ids were listed and compared before minting;
none of the 14 new ids appears in `data/signals/seen.txt` (16,144 lines). The one
near-collision — `01_26_086` / `01_26_093` against the existing
`dotace-optak-technologie-mas-2` — was caught by reading the ledger's own titles
rather than by id, and is recorded above as COVERAGE rather than minted.

### Pass summary (5 lines)

```
feed:              dotace-scan (monthly broad pass, 2026-09-03)
checklist sources: 8 of 8 visited — MS2021+ XML + IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO, CINEA/HaDEA
records staged:    14 (9 MS2021+ diff hits, 5 portal-walk catches) in staged-dotace-scan.jsonl
coverage gaps:     5 named — no prior call-id list; optak.gov.cz 403; mv.gov.cz doc API 401;
                   CINEA/HaDEA per-call budgets off-page; 4 live CZ calls seen and not minted
rotation state:    n/a — category rotation is arb-scan's duty, not this feed's
```

## reg-scan pass — 2026-09-03

Monthly BROAD pass of `reg-scan` (feed row: `evidence_type` regulation, `source`
value `reg-scan`, `id_prefixes` ["reg"], runner attended, cadence monthly).
Operating file: `pipeline/SCANS.md`, reg-scan checklist, items 1–4. Records:
`data/raw/2026-09-03/staged-reg-scan.jsonl` — **15 records, all `reg-` prefixed,
all `extraction: manual`.**

### Registry changes needed

**None.** Every record written this pass carries the `reg-` prefix, which is the
only prefix `reg-scan`'s `data/feeds.json` row claims. No `veklep-`, `echys-`,
`nku-`, `dotace-`, `smlouvy-` or any other feed's prefix was minted.

---

### Checklist source 1 — Programové prohlášení vlády + semi-annual fulfilment evaluations

**Visited.** https://vlada.gov.cz/cz/vlada/programove-prohlaseni/programove-prohlaseni-vlady-224629/
resolves (HTTP 200). The declaration is the Babiš government's, approved
**5 January 2026**, 18 policy chapters. Full text read from
https://vlada.gov.cz/assets/vlada/programove-prohlaseni/programove-prohlaseni-vlady.pdf
(2,115 lines via `pdftotext -layout`).

**Semi-annual evaluation — FOUND, but as an event, not a document.** The first
evaluation was held **9 July 2026** at Kramářova vila
(https://vlada.gov.cz/cz/media-centrum/aktualne/vlada-andreje-babise-bilancovala-prvni-pulrok--sve-programove-prohlaseni-uspesne-plni-227967/,
published 9. 7. 2026 19:32). Ministers submitted written evaluations to the prime
minister; **no evaluation document, table or dataset is published on
vlada.gov.cz** — only the press release, the press-conference page and per-minister
video summaries on YouTube. The full page text was pulled and searched: there is no
PDF/XLSX attachment and no item-level fulfilment status.

- **Record written:** `reg-pp-doprava-terminy-2029` — the programme's dated
  transport commitments (D3 across South Bohemia and the Prague ring to Černý Most
  by 2027; the remaining ring section started by 2028 at the latest; by 2029 D11
  joined to Poland, D6, D35 to Mohelnice, Praha–Ruzyně–Kladno, ETCS on main
  corridors, 5G on every rail corridor; up to 400 level crossings upgraded;
  liniový zákon reopened). Scored as the political commitment it is —
  `urgency: 2`, `recurrence: 1` — not as an enacted obligation.
- **Read and deliberately NOT recorded:** the digitalisation chapter (18) carries
  no dates at all — "jednou a dost", the propojený datový fond, a single digital
  gateway, AI in state administration, vendor-lock-in rules, an audit of state IT
  organisations — so it produces no dated regulation record. Stated here rather
  than silently dropped: a future pass owes it a re-read once the Digitální Česko
  implementation plan attaches dates.
- **Already in the corpus, not re-minted:** the EET 2.0 commitment ("Od roku 2027
  zavedeme EET 2.0", programme line 183) → `reg-eet2-2027` and
  `reg-mf-eet2-2027`; the startup act commitment → `reg-startupy-zakon`; the
  migration law the PM named as delivered → `reg-cizinecky-zakon-2029`; the ETS
  price positions → `reg-ets2-2028-cz`, `reg-ets2-carbon-price`.

**Partial coverage gap (named):** there is no published, machine-readable
fulfilment evaluation of the programme declaration. What exists is a press event.
**A future pass owes:** a re-check around January 2027 for the second semi-annual
evaluation, and a check of whether the ministries' individual written evaluations
are ever published; if they are not, this checklist item can only ever be walked
via the programme text plus press coverage, and that limit should be recorded on
the feed row rather than rediscovered each month.

---

### Checklist source 2 — Plán legislativních prací vlády 2026

**Visited.** https://vlada.gov.cz/cz/ppov/lrv/dokumenty/plan-legislativnich-praci-vlady-na-rok-2026-226017/
resolves (HTTP 200), page dated 23. 3. 2026 15:44, two PDF annexes. Annex 1
("Plán legislativních prací vlády na zbývající část roku 2026", 91 pages,
1,055 kB, annex to **usnesení vlády 175 of 23 March 2026**) downloaded and read in
full via `pdftotext -layout`; **112 legislative tasks** extracted across 17
submitters. Annex 2 (the 2027–2029 outlook, 707 kB) was NOT read this pass — see
the gap note below.

- **Record written:** `reg-plan2026-eu-infringement` — the plan-level finding.
  **21 of the 112 tasks carry an EU-infringement footnote**, counted mechanically
  from the resort sections: 16 read "Předložení návrhu v daném termínu je spojeno
  s hrozbou zahájení řízení…", 4 read "Implementační lhůta u předpisu EU nebyla
  dodržena a hrozí zahájení řízení…", and **1 says proceedings have already been
  opened with a real prospect of an Article 260(3) TFEU financial sanction** — the
  capital-market act transposing directive 2022/2381, implementation due 12.2024.
  The 21 tasks and their planned effective dates are listed in the record's `notes`.
- **Cross-checked against the corpus before minting:** 15 records already cite this
  same plan PDF (`reg-cizinecky-zakon-2029`, `reg-company-law-digital`,
  `reg-dalnicni-znamka-valorizace`, `reg-dph-vida-2027`, `reg-ekon-ochrana-statu`,
  `reg-energ-zakon-vodik`, `reg-irrd-pojistovny`, `reg-katastr-omezeni-dat`,
  `reg-kriticke-suroviny`, `reg-nature-restoration-cz`, `reg-skolsky-asistenti`,
  `reg-startupy-zakon`, `reg-str-registr-pronajmu`, `reg-vnitrni-sprava-egov`,
  `reg-zakon-o-bankach-2028`). Those are per-bill records; this one is the
  plan-level infringement count and duplicates none of them. The shared url is a
  listing page carried by >1 record and will be EXEMPTED by the identity-key dedup
  at `--complete`, not merged (CONVENTIONS.md, "A key is identifying only where it
  is unique").
- **Also cross-checked and NOT re-minted** (already in the corpus, EU-instrument
  side): `reg-ai-act-cz-dozor`, `reg-data-act-waves`, `reg-cra-reporting`,
  `reg-cpr-construction-products`, `reg-epbd-recast`, `reg-pld-software-liability`,
  `reg-platform-work`, `reg-pay-transparency-cz`, `reg-ppwr-packaging`,
  `reg-ied2-permits`, `reg-eu-disability-card`, `reg-media-financovani`.
- **Read, in scope, and NOT recorded this pass** (a floor, not a ceiling — named so
  the next pass starts here rather than rediscovering them): MF-11 zákon o
  Finančním analytickém úřadu (07.2027), MMR-2 novela zákona o zadávání veřejných
  zakázek (01.2028, RIA + RVKBK), MMR-3 bytová družstva (01.2028), MMR-1 zákon
  159/1999 cestovní ruch (01.2027), MPO-14 prověřování zahraničních investic
  (10.2027), MPO-15 průmyslové vzory (12.2027), MF-6 doplňkové penzijní spoření
  (01.2027), MF-15 pojištění odpovědnosti z provozu vozidla (01.2028), MV-3 zákon
  110/2019 o zpracování osobních údajů (04.2027), MV-4 zbraně a střelivo (01.2028),
  MZd-4 specifické zdravotní služby (07.2027), MZe-1 pozemkové úpravy (01.2027),
  MZe-5 mimořádné pracovní vízum (01.2027), MŽP-3 ochrana ovzduší (12.2026),
  MŽP-9 integrovaný registr znečišťování (01.2028), MPS-1 zákon o sportu a pohybu
  (01.2027), MK-1 zákon o knihovnách (01.2027), MSp-LRV-1 ústavní zákon o
  celostátním referendu (01.2029).

**Coverage gap (named):** **annex 2, "Výhled legislativních prací vlády na léta
2027 až 2029"** (https://vlada.gov.cz/assets/media-centrum/dulezite-dokumenty/1234_2026_priloha_c-_2.pdf,
707 kB), was not read. Reason: the pass budget went to annex 1 plus the 21 VeKLEP
RIAs, and the 2027–2029 outlook carries later dates than annex 1 throughout.
**A future pass owes it a full read** — it is where the 2028 and 2029 compliance
waves are first dated, and nothing else in the checklist surfaces them.

---

### Checklist source 3 — e-Sbírka and EUR-Lex

**e-Sbírka — visited, PARTIAL.** https://www.e-sbirka.cz/rejstriky-a-vyhledavani/vyhledavani-v-nove-vyhlasenych-predpisech
308-redirects to https://e-sbirka.gov.cz/… , which resolves HTTP 200 but serves an
**empty Angular shell** (`<esel-app></esel-app>`) — the "newly promulgated acts"
listing exists only after client-side JavaScript runs, so neither WebFetch nor curl
can read it. Two API probes against the paths advertised in
`https://e-sbirka.gov.cz/assets/configs/env.js` (`sbr-externi`, `leg-externi`)
returned structured 404s from `esel-esbir-dasex`, i.e. the service answers but the
public search route is not the one guessed.

**What DID work, and is now a usable receipt for this feed:** the ELI linked-data
endpoint `https://opendata.eselpoint.gov.cz/esel-esb/eli/cz/sb/<year>/<number>`
returns HTTP 200 and, with `Accept: text/turtle`, machine-readable versioning —
proved live on Act 270/2025:
`citace-právního-aktu "270/2025 Sb."`, `má-poslední-znění …/2027-01-01`, plus
versions 2025-08-05, 2026-01-01 and 2026-07-01. So a staged effective date can be
CHECKED rather than trusted.

- **Record written:** `reg-detsky-certifikat-2027` — Act 270/2025 creates the
  *evidence skutečností důležitých pro práci s dětmi* inside the criminal records
  register and the special extract known as the *dětský certifikát*, effective
  **1 January 2027**. A record bars work as a teacher, in institutional and
  protective-care facilities, as a paediatrician or health worker, in child
  social-legal protection and in social services with direct regular contact with
  children; a clean extract becomes a condition of four licensed trades (sport and
  physical-education services, day care of children under three, psychological
  counselling and diagnostics, massage/reconditioning/regeneration). Entries run
  100 years for offences carrying an upper limit of ≥5 years and 20 years
  otherwise, not shortenable.
- **This record carries NO `quote` key**, deliberately. The e-Sbírka act text is
  served by the same JavaScript application, so no verbatim payload was retrieved,
  and a quote lifted from secondary legal commentary would be a false receipt. The
  key is omitted rather than filled (CONVENTIONS.md: "an empty `quote` is not a
  quote"). **A future pass owes** the section numbers straight from the
  consolidated text once a text endpoint is found.
- **Not a duplicate of `reg-cz-psilocybin-2026`**, which records the cannabis and
  psilocybin limbs of the same act: different duty, different duty-holders,
  different effective date. Stated because a same-act pair is exactly the shape
  that reads as a duplicate from the id alone.

**Partial coverage gap (named):** e-Sbírka's own "nově vyhlášené předpisy" browse
surface is unreadable without a JavaScript runtime, so **this pass could not
enumerate the acts promulgated in August–September 2026** and worked from named
acts instead. **A future pass owes:** either a headless-browser read of that page,
or the correct `sbr-externi` search route (recoverable by grepping
`main-es2015.*.js` for `verejne/v1`), or a documented fallback to the ELI
open-data endpoint for enumeration. This is a real limit on the feed, not a
one-off.

**EUR-Lex — visited, OK.** https://eur-lex.europa.eu/oj/direct-access.html resolves
and reports the L-series volumes (3 Sep: 21 acts, 2 Sep: 7, 1 Sep: 8, 31 Aug: 1,
28 Aug: 2). Daily-view issues for 1 and 3 September 2026 read in full; a 2026
directive search was run (135 hits, overwhelmingly corrigenda — no new
transposition-bearing directive surfaced in the visible pages).

- **Records written:**
  - `reg-crr3-oprisk-business-indicator` — Delegated Regulation (EU) 2026/1167 and
    Implementing Regulation (EU) 2026/1166, published 3 September 2026, **in force
    23 September 2026**: the business-indicator components behind the CRR3
    operational-risk charge and their cell-by-cell mapping to FINREP templates
    (Annex I to Implementing Regulation 2024/3117). Directly applicable, no Czech
    transposition step. Dedup: `grep` of `data/signals/**` for "operational risk"
    and "business indicator" returns **zero** — nothing in the corpus covers CRR3
    operational risk.
  - `reg-trestni-zakonik-kybernasili-2027` — Directive (EU) 2024/1385, Article 49(1)
    transposition deadline **14 June 2027**, read verbatim from the Czech text on
    EUR-Lex, requiring criminalisation of non-consensual intimate material
    (including deepfakes), cyberstalking, cyberharassment (cyberflashing, doxing)
    and gender-based online incitement. Crossed with checklist source 4: the Czech
    transposing bill is the one the scripted feed surfaced as `veklep-ALBSDXDLCV5W`.
- **Checked and NOT re-minted** (topic already in the corpus): Delegated Regulation
  2026/1119 (ESG rating provider authorisation RTS) → `reg-esg-ratings`; Delegated
  Regulation 2026/1214 (brake particle emission testing) → `reg-euro7`; Pay
  Transparency directive 2023/970 → `reg-pay-transparency-cz`; CSDDD one-year
  postponement to 26 July 2027 → `reg-csddd-stop-clock`; EmpCo directive 2024/825 →
  `reg-green-claims-ecgt`.

---

### Checklist source 4 — VeKLEP RIA "Definice problému" for the drafts the scripted feed surfaced

Input: `data/signals/regulation/2026-09-02.jsonl`, **21 `veklep-*` records**. All
21 material pages were opened. **`odok.cz/portal/veklep/material/<PID>/` 302-redirects
to `odok.gov.cz/portal/veklep/material/<PID>/`** — the ledger urls still resolve,
but a future fetcher change should follow the redirect rather than treat it as a
failure.

**No `veklep-` id was re-minted.** Where a record was written it carries a `reg-`
id and, wherever an attachment exists, cites the **RIA or důvodová zpráva
attachment url** rather than the material page — better provenance, and it keeps
the identity-key dedup from seeing a same-url collision with the veklep record.

| # | veklep id | material | RIA present? | outcome |
|---|---|---|---|---|
| 1 | `veklep-KORNDXBH65S3` | Water act 254/2001 + water-supply act 274/2001, UWWTD transposition | **Yes**, 1,853 kB joint Závěrečná zpráva RIA | **3 records**: `reg-vodni-zakon-epr-mikropolutanty`, `reg-vak-energeticke-posouzeni-cov`, `reg-vak-srazkove-vody-poplatek` |
| 2 | `veklep-ALBSDRFEKCIO` | Obce act 128/2000 amendment | **Yes**, 4,544 kB | **1 record**: `reg-obce-spolecenstvi-sdilene-agendy` |
| 3 | `veklep-KORNDTFC490H` | Civil code — public guardianship | **Yes**, 390 kB | **1 record**: `reg-verejne-opatrovnictvi-prenos-2027` |
| 4 | `veklep-KORNDXCGU8JB` | Top-up tax act 416/2023 amendment | **Yes** (4 separate Definice problému sections) | **1 record**: `reg-dorovnavaci-dan-oznameni-2027` |
| 5 | `veklep-KORNDVEAJNTM` | Radio spectrum fees, nv 154/2005 | No RIA; důvodová zpráva read | **1 record**: `reg-ctu-poplatky-spektrum-2027` |
| 6 | `veklep-KORNDVYGNA4F` | Health insurance fund decree 418/2003 | No RIA; důvodová zpráva read | **1 record**: `reg-zdrav-pojistovny-limit-nakladu-2027` |
| 7 | `veklep-KORNDXAMWBJD` | Professional qualification recognition, act 18/2004 | No RIA; důvodová zpráva read | **1 record**: `reg-uznavani-kvalifikace-treti-zeme-2028` |
| 8 | `veklep-ALBSDXDLCV5W` | Criminal code + victims act, directive 2024/1385 | No RIA listed | **1 record**: `reg-trestni-zakonik-kybernasili-2027` (cited to EUR-Lex, the dated obligation) |
| 9 | `veklep-KORNDVKJ9GKB` | DIA remit omnibus | **No RIA — waiver granted by the LRV chair**, stated on the page | No record: nothing dated beyond what `reg-vnitrni-sprava-egov` already carries |
| 10 | `veklep-KORNDHZJL58I` | Digital technical map decree 393/2020 | No RIA; odůvodnění folded into zd | No record: duty already held by `reg-cuzk-dtm-editace`; this is a format/version update |
| 11 | `veklep-KORNDTRGAQDS` | Criminal-record request forms, decree 356/2024 | No RIA; důvodová zpráva only | No separate record — it implements the forms for `reg-detsky-certifikat-2027` (same 1 January 2027 date) and is named in that record's notes |
| 12 | `veklep-KORNDXGKDRP9` | State budget bill 2027 + full budget documentation | No RIA (budget bills carry none) | No record: an appropriation act, not a dated compliance obligation |
| 13 | `veklep-KORNDXAPCPV1` | Institutional-care allowances, nv 460/2013 | No RIA | No record: no effective date published on the page, and a regulation record without dates is not a regulation record |
| 14 | `veklep-KORNDT6DNLSS` | Sport medical-fitness decree 391/2013 | No RIA | No record: no effective date published; follows act 290/2025 |
| 15 | `veklep-KORNDVTBZKV2` | Civil-procedure flat-rate reimbursement, decree 254/2015 | No RIA | No record: no effective date published; substance is a 300→450 CZK fee change |
| 16 | `veklep-KORNDJ5LHNHI` | School hazardous-substances decree (replaces 61/2018) | No RIA | No record: no effective date published |
| 17 | `veklep-KORNDUFHSKGR` | Sites of European importance decree | No RIA; approved by government 17 Aug 2026 | No record: implements Commission Decision 2026/401 list update, no new duty-holder obligation dated |
| 18 | `veklep-KORNDTTFZCC9` | Carbon-leakage compensation amounts for 2025 | No RIA; signed | No record: no CZK amounts published on the page; a future pass owes the materiál attachment |
| 19 | `veklep-KORNDTTFZDQD` | Carbon-leakage conditions, nv 565/2020 (Commission communication C/2026/196) | No RIA | No record: no CZK amounts, no effective date published |
| 20 | `veklep-ALBSDUV954AH` | Soudní řád správní 150/2002, MPs' bill (sněmovní tisk 215) | No RIA (MPs' bill) | No record: no effective date published; government resolution 413/2026 of 29 June 2026, now in Parliament |
| 21 | `veklep-ALBSDUW89Q2L` | Conflict-of-interest act 159/2006, MPs' bill (tisk 221) | No RIA (MPs' bill) | **No record, and this one is a judgement call worth naming**: the substance is material — a ban on non-entitlement subsidies and investment incentives where the provider is headed by a public official who is the recipient's beneficial owner, plus procurement exclusion — but **no effective date is published**, so it fails the evidence bar. A future pass owes psp.cz tisk 221 for the proposed effectiveness. |

**One extra dedup finding, recorded because it changes a score:**
`veklep-KORNDV4MNCNT` (minimum-wage coefficient 2027/2028) already sits in
`data/signals/regulation/2026-08-25.jsonl` — but with `urgency: 0`, no dates, no
coefficients and no glide-path target. This pass wrote
`reg-min-mzda-koeficient-2027-2028` from the MPSV press release of 18 June 2026
(coefficients **0.446** for 2027 and **0.458** for 2028; statutory target 47 % by
2029; MF wage projection due 31 August 2026; amount published in the Sbírka).
That id is deliberately not re-minted and the relationship is stated in the
record's `notes`. **Flagged for MATCH/PROCESS:** the existing veklep record's
`urgency: 0` understates a live, economy-wide, dated obligation.

---

### Evidence-bar compliance

- **No money was estimated.** Every `money_eur` is either `null` with a
  `money_note` saying what is and is not published, or a state-published CZK figure
  converted at **24.5 CZK/EUR** — the rate the committed corpus already uses
  (measured: `dotace-mf-elegrid-1-distribucni-soustava` 10bn CZK → 408,200,000 EUR
  = 24.50; `dotace-irop-117-izs-praha` 901M → 36,800,000 = 24.48). Where the state
  published a range (8–15bn CZK for wastewater energy neutrality) the **lower bound**
  is used and the upper bound is named in the note.
- **Every record has dates.** All 15 carry an adopted / in-force / compliance date
  in `date`, and the `notes` carry the surrounding dates (authorisation, comment
  procedure, government meeting, transposition deadline).
- **No absence claim is made anywhere in this pass**, so no positive control was run
  and none was owed: regulation records assert what a published instrument says,
  never that no local player exists. Stated explicitly so the omission is not read
  as a skipped check.
- **Quotes:** 14 of 15 records carry a `quote`; **all 14 were verified as literal
  substrings of the fetched payload after whitespace collapse** (10 against locally
  extracted `.docx`/PDF text, 4 by re-fetching and re-checking). The 15th
  (`reg-detsky-certifikat-2027`) omits the key — see checklist source 3.
- **No personal data.** RIA payloads were read for problem definitions only;
  VeKLEP's `adresaPripominek` field (a named civil servant's work email) was never
  read or written. Public officials are named only in office (the prime minister,
  the labour minister) and only in `notes`.

### 5-line pass summary

```
feed:                reg-scan (evidence_type regulation, prefix reg-, monthly broad pass)
checklist sources:   4 of 4 visited (1 programové prohlášení + evaluations · 2 plán legislativních prací ·
                     3 e-Sbírka + EUR-Lex · 4 VeKLEP RIA problem definitions for all 21 veklep-* ids)
records staged:      15 in data/raw/2026-09-03/staged-reg-scan.jsonl (0 registry changes needed)
coverage gaps named: 3 — plan annex 2 (2027–2029 outlook) unread · e-Sbírka new-acts browse is a JS SPA,
                     no public search route found · no published fulfilment-evaluation document exists
rotation state:      n/a (category rotation is an arb-scan duty)
```

## sweep pass — 2026-09-03

**Topic as given:** hospital drug procurement — Czech public hospitals each run their own
parallel purchasing systems (dynamické nákupní systémy) per therapeutic group.

**Why this sweep ran:** the 2026-09-02 match pass held the contract leg (the drug-DPS
notices already in the tenders ledger) but failed the register bar for want of a WHY-NOW
and a DOCUMENTED PAIN. This pass was asked to find or rule out exactly those two things.

**Files:** records `data/raw/2026-09-03/staged-sweep.jsonl` (12 lines) · this section.
Nothing was appended, committed, normalized or built by this agent.

### Registry changes needed

- **`arb-scan.id_prefixes` must gain `"us"`** before the append. One record, `us-trulla`,
  is a United States comp (Trulla, Draper, Utah). `SWEEP.md` step 3a names this exact case
  and requires the registry widening in the same change as the record; the concurrency
  rules for this run forbid the agent editing `data/feeds.json`, so it is listed here.
  No other prefix is needed: `dk`, `gb`, `de`, `nl` are already claimed by arb-scan, and
  `civic`, `ngo`, `reg` by demand-scan / reg-scan.
- **No new source values, evidence types, ledgers or schema keys.** All 12 records use
  `arb-scan`, `demand-scan` and `reg-scan`, which the registry already claims.

### 1. FRAME — decomposition

| leg | who |
|---|---|
| **buyer** | the individual public hospital, procuring on its own account: directly-managed fakultní nemocnice (MZ ČR is the founder), regional joint-stock hospitals (Krajská zdravotní, Karlovarská krajská nemocnice), military hospitals (Vojenská nemocnice Olomouc), psychiatric hospitals (PN Dobřany), state institutes (IKEM, ÚHKT), and regions buying for their own emergency services (Moravskoslezský kraj, ZZS JMK). The procuring unit inside the buyer is the oddělení veřejných zakázek plus the nemocniční lékárna. |
| **user** | the hospital pharmacist who runs the minitender per ATC group and the primář who requests the molecule. On the sell side, the wholesalers that answer nearly every call — PHOENIX lékárenský velkoobchod, Alliance Healthcare, Fresenius Kabi, BAXTER — and the originator and generic manufacturers behind them. |
| **regulator** | ÚOHS supervises the procedure; ZZVZ (zákon 134/2016 Sb.) is the legal basis for the dynamic purchasing system; SÚKL sets maximum prices and reimbursements under zákon 48/1997 Sb.; MZ ČR issues the úhradová vyhláška and the annual cenové výměry; the EU layer is Directive 2014/24/EU (dynamic purchasing systems, joint and cross-border procurement). |
| **money** | hospital drug spend, reimbursed out of public health insurance. The visible numbers are the system ceilings on the notices themselves — a single VFN system is advertised at 2,000,000,000 CZK — and the payer's own figure of 22.5 billion CZK of centre-drug spend at VZP alone in one year. There is **no budget line anywhere for "hospital drug procurement software"**: it is bought out of each hospital's own provozní budget, which is a material finding for the money leg. |

### 2. FRAME — search vocabulary actually used

**Czech:** dynamický nákupní systém léčiv · DNS na léčivé přípravky · průběžné a opakované
nákupy léčivých přípravků · sdružený nákup nemocnic · sdružené nákupy léků · centrální
nákup léčiv · cenová soutěž léčiv · referenční ceny léků · společný nákup nemocnic ·
elektronická aukce léčiva · nemocniční lékárna nákup software · úspory při nákupu léků
nemocnice · rozdílné ceny léků nemocnice · benchmarking nákupních cen léčiv nemocnice ·
kontrolní závěr NKÚ nákup léčiv · e-tržiště zdravotnictví · profil zadavatele nemocnice
elektronický nástroj · novela zákona o zadávání veřejných zakázek 2026 · centrální zadávání
veřejných zakázek na nákup léčivých přípravků · cenový výměr léčivé přípravky 2026.

**English:** hospital group purchasing organisation software · GPO healthcare Europe ·
hospital pharmacy procurement platform · drug tender aggregation · e-tendering
pharmaceuticals hospitals · joint procurement of medicines EU · hospital procurement
Germany Netherlands Poland Nordics · medicine price dispersion between hospitals ·
EU pharmaceutical package 2026 dates · EU4Health joint procurement call.

**German / Dutch / Polish:** Krankenhaus Einkaufsgemeinschaft Arzneimittel · Klinikapotheke
Einkauf · zorginkoop coöperatie ziekenhuizen geneesmiddelen · geneesmiddelenbenchmark ·
szpitalna grupa zakupowa leki · wspólne zakupy szpitali.

### 3. MINE THE CORPUS FIRST — coverage, not to be re-minted

`grep -il` over `data/signals/*/*.jsonl` plus a scripted pass with the regex
`(dynamic purchasing|dynamick|\bDPS\b|\bDNS\b)` AND
`(léčiv|léků|léky|medicin|drug|pharmac|antineoplas|antithromb|immunosuppress)`.

**TENDERS — the contract leg is already committed and was READ, never re-fetched.**
106 drug-object dynamic-purchasing records from **15 distinct buyers** sit in
`data/signals/tenders/2026-09-02.jsonl`. Their `money_eur` sums to €4,166,758,092, but
**that total is not spend** — several rows carry the system CEILING (80,000,000 and
2,000,000,000 CZK appear repeatedly) rather than a call-off value, and a downstream reader
must not add them up.

- **Všeobecná fakultní nemocnice v Praze (38)** — ted-461139-2026, ted-463504-2026, ted-463656-2026, ted-463916-2026, ted-464041-2026, ted-464666-2026, ted-475679-2026, ted-481556-2026, ted-482214-2026, ted-483671-2026, ted-484172-2026, ted-484412-2026, ted-487428-2026, ted-491952-2026, ted-493463-2026, ted-494036-2026, ted-502862-2026, ted-503241-2026, ted-504621-2026, ted-520642-2026, ted-544845-2026, ted-547899-2026, ted-550358-2026, ted-550427-2026, ted-551502-2026, ted-560980-2026, ted-562802-2026, ted-563168-2026, ted-572990-2026, ted-575343-2026, ted-578146-2026, ted-581118-2026, ted-592160-2026, ted-592492-2026, ted-593604-2026, ted-594193-2026, ted-596112-2026, ted-598907-2026
- **Fakultní nemocnice Olomouc (24)** — ted-472200-2026, ted-475151-2026, ted-486548-2026, ted-489078-2026, ted-489258-2026, ted-489350-2026, ted-489918-2026, ted-494093-2026, ted-494549-2026, ted-503943-2026, ted-504259-2026, ted-520128-2026, ted-520990-2026, ted-534377-2026, ted-544389-2026, ted-548496-2026, ted-551469-2026, ted-562837-2026, ted-569463-2026, ted-570561-2026, ted-570733-2026, ted-571306-2026, ted-584802-2026, ted-593088-2026
- **Fakultní nemocnice Bulovka (16)** — ted-489593-2026, ted-489685-2026, ted-510013-2026, ted-522233-2026, ted-527908-2026, ted-528706-2026, ted-546249-2026, ted-554180-2026, ted-555052-2026, ted-555277-2026, ted-555343-2026, ted-555932-2026, ted-555952-2026, ted-556327-2026, ted-573152-2026, ted-591696-2026
- **Fakultní nemocnice Motol a Homolka (10)** — ted-495094-2026, ted-497088-2026, ted-525233-2026, ted-527970-2026, ted-549437-2026, ted-555898-2026, ted-575513-2026, ted-575898-2026, ted-587665-2026, ted-603888-2026
- **Krajská zdravotní (3)** — hlidac-36891494, ted-525454-2026, ted-591805-2026
- **Moravskoslezský kraj (3)** — ted-520732-2026, ted-561222-2026, ted-562057-2026
- **Psychiatrická nemocnice v Dobřanech (2)** — ted-471340-2026, ted-471481-2026
- **Ústav hematologie a krevní transfuze (2)** — ted-476022-2026, ted-557012-2026
- **Karlovarská krajská nemocnice (2)** — ted-491024-2026, ted-491551-2026
- **one each** — Vojenská nemocnice Olomouc ted-461401-2026 · Úrazová nemocnice v Brně ted-471555-2026 · ZZS Jihomoravského kraje ted-472021-2026 · IKEM ted-495420-2026 · Fakultní nemocnice Ostrava ted-519711-2026 · Ministerstvo vnitra ted-566642-2026

Eight further notices matched the DPS-plus-drug regex but buy something else under a
hospital's purchasing system and are **excluded from the 106** so nobody double-counts
them: ted-474256-2026 and ted-476658-2026 (cleaning products), ted-489689-2026 (dry ice),
ted-495247-2026 (flour and bakery), ted-498449-2026 (training simulators), ted-517766-2026
(MPSV cleaning), ted-546170-2026 (drugstore goods), ted-546710-2026 (stoma devices).

**REGULATION — already held:** reg-mzd-289-2025-pojisteni · reg-mzd-uhradova-432-2025 ·
reg-mzd-290-2025-sluzby · reg-sukl-422-2025-boxy · reg-mzd-236-2025-ezdrav ·
veklep-ALBSDUMBLGK4 (bill 206, the pending ZZVZ amendment) · veklep-ALBSD65EF6FP (an
earlier ZZVZ draft) · veklep-KORNDVLDLD32, veklep-KORNDUAA6SOP, veklep-KORNDVYGNA4F
(health-insurance implementing rules).

**DEMAND — already held:** sukl-vypadky-leku · sukl-preruseni-stav-2026 ·
sukl-ukonceni-trhu · sukl-cns-vypadky (the shortage family — the OTHER drug-supply problem,
deliberately not re-minted here) · nku-fakultni-nemocnice (audit 24/09, hospital
investment) · nku-react-eu-nemocnice · nku-erecept-sms (audit 24/25, SÚKL ICT tenders) ·
nku-ehealth-delay.

**FUNDED — already held, nearest neighbours:** yc-floracene (US, device purchasing for
independent providers) · yc-vetcove (US, animal-health supply chain) · yc-kaso (AE, group
purchasing for restaurants) · yc-bonfire (CA, gov RFP) · yc-hazel-2 (US, gov procurement) ·
round-cato-ai (IT, bid management) · round-pivot (FR, procurement OS) · yc-lio (DE,
procurement agents) · round-definic (SK, IT procurement) · yc-unstatiq (US, clinic finance
and supply chain). **None is hospital drug procurement**, which is why 3a minted new ones.

**PROBLEMS — prior claims re-read:** `p-0031-municipal-pv-procurement` (the closest
analogue: pooled municipal procurement, and it already names **eCENTRE**, IČO 27149862, as
an established adjacent Czech joint-purchasing operator) and `p-0022-hospital-ehealth-
interoperability`. No existing problem record asserts anything about hospital drug buying,
so no prior absence claim was contradicted.

### 3a. FUNDED via arb-scan — 5 records

| id | company | geo | date | what it proves |
|---|---|---|---|---|
| `dk-amgros` | Amgros | DK | 2026-09-03 | one national body buys almost all Danish public-hospital medicines for the five regions that own it; nearly DKK 10bn of 2024 savings |
| `gb-vamstar` | Vamstar | GB | 2022-06-22 | USD 9.5m Series A for an AI sourcing platform matching hospital, insurer and GPO drug tenders to suppliers |
| `de-vivecti-prospitalia` | Vivecti Group (Prospitalia + Sana Einkauf) | DE | 2025-09-19 | a private buying group of 6,000+ providers and >€7bn annual volume, explicitly covering Klinikapotheken |
| `nl-intrakoop` | Intrakoop | NL | 2026-09-03 | a 1959 care purchasing cooperative that runs a **medicine price benchmark** and extended it from care homes to hospitals |
| `us-trulla` | Trulla (SpendMend) | US | 2022-08-16 | buyer-side pharmacy procurement software across a hospital system's sites; 300+ pharmacies served; needs the `us` prefix |

**Considered and NOT minted, with the reason:**
- **TRiBECA Knowledge (GB, SmartTender)** — supplier-side pharma tender management. No
  founding year, no funding and no customer count are published; a record would have had
  nothing verifiable in `traction`, so none was written.
- **Sykehusinnkjøp HF (NO)** and **Tendium (SE)** — both on topic, both blocked on the
  prefix: `no` and `se` are not in arb-scan's `id_prefixes`. Widening the array for two
  companies this pass did not fully research would be a registry change made on a guess.
  **Named here as owed work for a future pass**, not as a silent skip.
- **Medyczna Grupa Zakupowa and the Polish hospital buying groups** — Polish group
  purchasing is documented as having *failed* (prawo.pl: group buying "się nie udały",
  only isolated cases; Termedia: ~70% of Polish health tenders end with a single bid
  against ~4% across the EU). That is a demand-shaped finding about Poland, not a funded
  comp, and the only sources are trade press rather than a reporting body, so no record.
- **Faks (FR, €6m, Speedinvest)** — community-pharmacy purchasing, not hospital. Off topic.
- **P.E.G. eG, AGKAMED, EKK plus, EK UNICO (DE)** — real GPOs, but each would restate what
  `de-vivecti-prospitalia` already records. One record, not five.

### 3b. TENDERS via dotace-scan — **NULL. No record minted.**

No open Czech or EU subsidy call was found that funds hospital procurement digitisation or
joint purchasing. This is stated with what was checked, per SWEEP step 3:

| call / programme | checked | why no record |
|---|---|---|
| IROP 78/79/80 "eHealth" | irop.gov.cz call 79 page read in full | Call 79 is open (announced 26 October 2023, intake 28 November 2023 to **2 December 2026 14:00**, projects to complete by 31 December 2027, ~1.15bn CZK EFRR, extended because the allocation was under-drawn). But the supported activity is "zlepšení způsobu vedení zdravotnické dokumentace umožňující její interoperabilní výměnu, sdílení, bezpečné uložení a interpretaci" — **clinical documentation, not procurement**. Hospital logistics, warehouse, pharmacy or purchasing systems are not among the eligible activities. Minting it would have been a false positive for this topic. |
| NPO call 22 (Služby elektronického zdravotnictví) | ncez.mzcr.cz | intake closed 14 November 2024; physical completion ends 31 May 2026. Closed, and interoperability-scoped. |
| OP TAK "Digitální podnik" výzva I | optak.gov.cz, narodni-plan-obnovy.cz | 1bn CZK, intake 20 October 2025 to 18 February 2026 — but eligible applicants are enterprises. Public hospitals cannot apply. |
| MZ ČR national grant programmes | mzd.gov.cz dotace pages | "Podpora zdraví, zvyšování efektivity a kvality zdravotní péče" is **no longer announced from 2025**. |
| OPZ+ (efektivní veřejná správa) | esfcr.cz call list and harmonogram | no call matching procurement digitisation or joint purchasing found. |
| EU4Health / HaDEA 2026 | hadea.ec.europa.eu | the 2026 procurement calls are medical-countermeasure R&D — HADEA/2026/OP/0015 next-generation therapeutics (€244m, request to participate by 2 September 2026), HADEA/2026/OP/0020 EU FAB+ PPE (€34m, 10 September 2026), HADEA/2026/OP/0021 API stockpiling. **Joint procurement of countermeasures, not of hospital purchasing systems.** Off topic; recorded here so the next pass need not re-derive it. |
| Technical Support Instrument (DG REFORM) | reform-support.ec.europa.eu | TSI 2026 flagship does cover streamlining public procurement, and Czechia has taken 81 TSI/SRSP projects — but TSI funds a member-state authority's reform, has no published call with an allocation and deadline of the kind this stream records, and no Czech health-procurement TSI project was found. |

**SCRIPTED-PREFIX PROHIBITION honoured:** no `ted-`, `hlidac-`, `nen-` or `smlouvy-`
record was hand-minted. **No fetcher-coverage gap to report on this topic** — the TED
fetcher's jurisdiction-complete query is plainly catching this cluster (106 records from
15 buyers over nine weeks), which is the reason the contract leg needed nothing from this
pass.

### 3c. DEMAND via demand-scan — 6 records

| id | body | date | the pain |
|---|---|---|---|
| `civic-nku-1719-nakup-leciv` | NKÚ, audit 17/19 | 2018-09-03 | three university hospitals bought medicines very often without any tender, by direct order; MEROPENEM KABI at 956 CZK a pack in one and 3,300 CZK in another; PIPERACILLIN/TAZOBACTAM KABI at 385 CZK against 2,103 CZK; ~1bn CZK of supplier bonuses |
| `ngo-ti-zdravotnictvi-zakazky-2024` | Transparency International CZ | 2024-10-10 | NKÚ on the record: the biggest failings it finds are in medicines and medicine purchasing, bought "bez řádné soutěže, tedy napřímou"; ~60% of pharma purchases tendered |
| `civic-vzp-centrove-leky-bonusy` | VZP | 2025-03-10 | 22.5bn CZK of centre drugs in a year at VZP alone, over a "šedá zóna zpětných bonusů" estimated at 3.5bn CZK |
| `civic-mz-aifp-cenova-databaze` | MZ ČR + AIFP | 2018-11-23 | the ministry had to build a database to learn what its own hospitals pay; unit prices are contractually barred from wider publication |
| `civic-mz-spolecne-nakupy-fn-2026` | MZ ČR | 2026-07-29 | the second attempt at the same fix in eight years — a memorandum with six university hospitals to *start analysing* what could be pooled, led by facility management rather than medicines, with no dated deadline |
| `civic-uohs-metodika-nakup-leciv` | ÚOHS | 2022-04-06 | the competition authority meets drug-buying problems "stále častěji" and has to reconcile a procurement procedure with delivery clocks measured in hours — the mechanism that produces the DPS pattern in the first place |

**PREFIX DISCIPLINE:** none of these minted `nku-`, `mpsv-`, `sukl-` or `coi-`, all of which
are claimed by scripted feed rows. NKÚ, VZP, MZ ČR and ÚOHS are all state or public-law
bodies, so they are filed under `civic-` exactly as SWEEP step 3c directs for the `mpsv-`
trap, and each record says so in its own `notes`. Transparency International is a
nongovernmental organisation, hence `ngo-`.

**Considered and NOT minted:** the ARROWS law-firm note on healthcare procurement
(arws.cz, 9 February 2026, updated 14 August 2026) is advisory rather than a complaint —
it recommends DNS and framework agreements — so it is cited inside
`civic-uohs-metodika-nakup-leciv`'s notes instead of taking a row. The Zdravotnický deník
piece of 17 July 2026 on device-cost reporting ("Some report the maximum value per the VZP
catalogue, others the actual purchase prices") documents fragmentation in **medical device**
accounting, not drugs, and was left out to keep the topic clean.

### 3d. REGULATION via reg-scan — 1 record, and one important non-mint

**Minted:** `reg-cz-cenovy-vymer-1-2026-olzp` — MZ ČR price ruling 1/2026/OLZP of
24 October 2025, published in Věstník 18/2025 on 31 October 2025, **in force 1 January
2026**, which stops applying the split trade margin to purely hospital medicinal products.
Companions 2/2026/OLZP (ATC groups with special availability price rules) and 3/2026/OLZP
(devices) share the date and are named in the record's notes rather than given rows of
their own.

**NOT MINTED, AND THIS IS THE PASS'S MOST IMPORTANT FINDING:**

> **The register already holds this topic's why-now and cannot see it.**

Zákon **289/2025 Sb.** — the comprehensive amendment to zákon 48/1997 Sb., bill 849, third
reading 23 April 2025, Senate 12 June 2025, published in the collection **12 August 2025**,
**in force 1 January 2026** — carries the power for health insurers to run **centrally
awarded public contracts for medicinal products** destined for specialised-care centres
(§ 40d of zákon 48/1997 Sb., "Centrální zadávání veřejných zakázek na nákup léčivých
přípravků pro poskytovatele"). That is a dated, in-force, statutory move of drug tendering
off the individual hospital and onto the payer, and it is precisely the why-now the
2026-09-02 match pass could not find.

A record was drafted for it and then **withdrawn before staging**, because
`scripts/normalize.py`'s identity-key index matched it against an existing ledger row:

    COLLISION  reg-cz-289-2025-centralni-zadavani-leciv
               url:e-sbirka.gov.cz/sb/2025/289 -> ['reg-mzd-289-2025-pojisteni']

`reg-mzd-289-2025-pojisteni` (committed 2026-08-14) is the same act at the same URL with
the same in-force date, but its title and summary describe **cross-border provider
contracts, dental reimbursement, cashless insurers and benefit funds** and say nothing
about drug procurement. So a MATCH pass grepping the regulation ledger for `léčiv`,
`nákup` or `procurement` will not find the provision that makes this topic urgent.

Staging a second row would have been the differently-worded duplicate the dedup rules
forbid, and the ledgers are append-only, so **the enrichment is owner or MATCH work, not
sweep work.** What this pass owes the next one is written down here instead:

- the provision is described verbatim by kmvs.cz (16 January 2025) as *"centralizovaně
  zadávané veřejné zakázky ze strany pojišťoven v případě přípravků určených do center
  specializované péče, které se účtují spolu s výkonem nebo se jedná o přípravky použitelné
  pouze v lůžkové péči a jedná se o jediný registrovaný přípravek s obsahem dané léčivé
  látky"*;
- the demand-side twin is `civic-vzp-centrove-leky-bonusy`, where the national insurer
  argues for exactly this power and puts the spend at 22.5bn CZK a year;
- **OPEN VERIFICATION ITEM, stated rather than glossed:** this pass confirmed that bill 849
  contained the provision, that bill 849 became 289/2025 Sb. in force 1 January 2026, and
  that § 40d now exists in the consolidated act — but it never read the amending article
  that inserts § 40d, because e-sbirka, zakonyprolidi (HTTP 403), fulsoft, mesec and
  podnikatel all failed to return the paragraph body. The 289/2025 ↔ § 40d link is
  inference from three verified facts. A future pass owes that read.

**Also checked, no record:**
- **The pending ZZVZ amendment** (zákon 134/2016 Sb.): a ministry draft went to
  inter-ministerial comment in late March 2026 and a compromise MPs' bill passed the
  Chamber on 23 July 2026 and went to the Senate. **No Sbírka number and no in-force date**,
  so under SWEEP 3d it is not a regulation record. The corpus already holds the draft as
  `veklep-ALBSDUMBLGK4` and `veklep-ALBSD65EF6FP`.
- **The EU pharmaceutical package**: compromise texts confirmed by COREPER and published
  6 March 2026, expected entry into force in 2026 with transition to 2028. Real and dated,
  but it replaces the Community Code and the EMA Regulation — marketing authorisation, data
  protection, supply-security duties on marketing-authorisation holders. It says nothing
  about how a hospital buys. Off topic, recorded so the next pass need not re-derive it.
- **§ 32c / § 32d of zákon 48/1997 Sb.** (extraordinary measures for medicine availability,
  version in force 12 June 2026) — shortage regulation, which is the corpus's *other* drug
  problem and already covered by the `sukl-` demand family. Not this topic.

### 4. ABSENCE CHECKS — the headline is that there is NO absence

Every arb record carries its own check in `notes`. The consolidated result:

**Queries run (Czech):** dynamický nákupní systém léčiv · sdružený nákup léků nemocnice ·
centrální nákup léčiv nemocnice · sdružené nákupy nemocnic · software pro nákup léčiv
nemocnice · elektronický nástroj zadávání veřejných zakázek nemocnice · e-aukce léčiva
nemocnice · benchmarking nákupních cen léčiv nemocnice · srovnání cen léků mezi nemocnicemi ·
databáze jednotkových cen léčiv nemocnice · nemocniční lékárna objednávání léčiv software ·
profil zadavatele Všeobecná fakultní nemocnice dynamický nákupní systém.
**(English):** hospital drug tender aggregation Czech · group purchasing organisation
hospitals Czech Republic.

**Surfaces checked:** `google-cz`, `own-funded-ledger`. **NOT checked, and therefore not
claimed:** `ares`, `cz-saas-directories`, `startupjobs`, `app-stores`,
`eshop-addon-marketplaces`.

**POSITIVE CONTROL — PASSED.** The same method (Czech-language search plus a read of the
vendor's own site) surfaced two of the register's three standing controls:
**Wultra** (Praha, IČO 03643174 — PowerAuth mobile authentication, the Talisman FIDO2
device, App Shielding) and **SOFTLINK** (Kralupy nad Vltavou, founded 1993, the CEM energy
application, more than 100,000 metered devices, acquired by Quantcom on 30 June 2022).
The method produces positives; a negative from it would have been evidence. It produced no
negative.

**WHAT WAS FOUND — recorded as evidence, with no gap judgment, which stays with MATCH
under the asymmetric-authority law:**

- **The tool layer is occupied by established Czech vendors, and the corpus's own notices
  point at them.** PROEBIZ (Moravská Ostrava) sells JOSEPHINE and TENDERBOX and publishes
  live dynamic-purchasing procedures for Czech health buyers; FN Brno runs its DNS on
  **E-ZAK** at `ezak.fnbrno.cz` (the QCM product); VFN Praha's contracting-authority profile
  sits on **Tender arena** and **eGordion**. Anyone claiming "no Czech player runs hospital
  drug DPS software" is contradicted by the hospitals named in this sweep's own tender ids.
- **The aggregation layer is contested rather than empty.** **eCENTRE** (IČO 27149862,
  already recorded as an established adjacent player on p-0031) sells coordinated purchasing
  with e-auctions to Czech hospitals — Ostrava city hospital reports 21% savings on suture
  material, 34% on anaesthesia and oxygen-therapy supplies, 25% on infusion solutions.
  **Nemocnice Pardubického kraje** runs a "Centrální nákup" function for the region.
  **MZ ČR** runs its own joint purchasing across directly-managed hospitals (2018 pilot,
  2026 memorandum).
- **The price-intelligence layer is the thinnest.** MZ ČR and AIFP hold real unit prices for
  directly-managed hospitals since 2019, but the database is industry-hosted, covers only
  the founder's own hospitals, and its unit prices may not be published or handed to parties
  without access. ÚZIS's reference-hospital benchmark at `drg.uzis.cz/benchmarking` compares
  performance, not purchase prices. No commercial Czech cross-hospital medicine price
  benchmark was found — but per the asymmetric-authority law, **not finding one is not
  evidence that none exists**, and no absence is asserted.

### 5. COVERAGE GAPS

1. **`intrakoop.nl` unreachable** — WebFetch failed twice with "unable to verify the first
   certificate" (TLS chain) on `/over-ons` and on the 2018-11-27 benchmark article. The
   `nl-intrakoop` record is therefore anchored on `cooperatie.nl`, which was fetched and is
   quoted verbatim. A future pass owes a direct read of
   `intrakoop.nl/diensten/medisch-en-farmacie` and of the geneesmiddelenbenchmark pages.
2. **§ 40d text not read** — `zakonyprolidi.cz` returned HTTP 403; e-sbirka, fulsoft, mesec
   and podnikatel all returned the table of contents without the paragraph body. See 3d.
3. **`ted.europa.eu` notice pages return no body to WebFetch** (JavaScript-rendered), so the
   buyer's `profil zadavatele` URL could not be read straight off a notice. The
   e-procurement platform attribution above therefore comes from the hospitals' own portals
   (`ezak.fnbrno.cz`, `api.tenderarena.cz/ta/profil/.../vfn`, `josephine.proebiz.com`)
   rather than from the notices. A future pass wanting a per-buyer platform census should
   fetch `vhodne-uverejneni.cz` / `nen.nipez.cz` profiles instead of TED.
4. **IROP call 79 text PDF unreadable** — `Text-79-vyzvy-eHealth-k-26-5-2026.pdf` came back
   as binary. The call parameters above are from the HTML call page, which was readable; the
   eligible-activity list is therefore the page's summary, not the PDF's full annex.
5. **`no` and `se` comps left unresearched** because their prefixes are unclaimed (3a).
   Sykehusinnkjøp HF and Tendium are named so the next pass has the leads.
6. **Poland** produced trade-press evidence only (group purchasing failed; ~70% single-bid
   tenders). No reporting-body source was found, so nothing was minted. A PL sweep would
   want NIK (the Polish audit office) and UZP rather than Termedia.

### 6. HAND OFF

No `git add`, no commit, no `normalize.py`, no `db.py`, no web build, no edits to
`data/feeds.json`, `data/signals/**`, `seen.txt` or any problem file. `staged-sweep.jsonl`
and this section are left uncommitted for the orchestrator.

Pre-flight checks the agent DID run, read-only: JSON parse on all 12 lines; required-field
presence; exactly one `" — "` per title; sector against the fixed list; ISO dates; scores
integer 0–3; ids absent from `seen.txt`; quotes ≤300 chars; materiality simulated (none of
the 12 would be dropped); and `normalize.py`'s own `record_keys` / `build_key_index` run
against the committed ledgers — **0 identity-key collisions remain** after the 289/2025
withdrawal described in 3d.

### 5-line sweep summary

1. **Topic:** hospital drug procurement — Czech public hospitals each run their own parallel dynamic purchasing systems per therapeutic group.
2. **Records staged per stream:** funded 5 · demand 6 · regulation 1 · tenders 0 (12 total, `data/raw/2026-09-03/staged-sweep.jsonl`).
3. **Appended after materiality:** none by this agent — the orchestrator runs `normalize.py --complete` once; simulated locally, all 12 pass materiality and 0 collide on identity key.
4. **Absence checks:** 5 run, 0 absences written — the Czech tool layer (PROEBIZ, E-ZAK/QCM, Tender arena, eGordion) and aggregation layer (eCENTRE, MZ ČR, Nemocnice Pardubického kraje) are occupied; positive control PASSED on Wultra and SOFTLINK.
5. **Coverage gaps:** 6 named — intrakoop.nl TLS failure · § 40d text unreadable on five sources · TED notice bodies unreachable · IROP 79 PDF binary · `no`/`se` prefixes unclaimed · Poland trade-press only. **Registry change needed: add `"us"` to `arb-scan.id_prefixes`.** **Verdict on the brief: the WHY-NOW exists and is dated 1 January 2026 (§ 40d central tendering by insurers, plus cenový výměr 1/2026/OLZP); the DOCUMENTED PAIN exists and is the state's own (NKÚ 17/19, ÚOHS, VZP, TI); what does NOT exist is an empty Czech market.**

## Match phase — harvest 2026-09-03 (attended, same day)

Two agents over the 61 appended records, match_log +61 (+5 re-decisions on
older ids): **20 linked, 34 dismissed, 7 deferred**. One new record:
**p-0035 hospital drug procurement** (score 9, status watching — gap 0, eCENTRE
direct and established), authored from the sweep: all 12 sweep records cited,
plus four 2026-09-02 TED notices (ted-461139, ted-472200, ted-489593,
ted-495094 — their 2026-09-02 bulk dismissals are superseded by later linked
rows) and the committed reg-mzd-289-2025-pojisteni, whose ledger title hides
§ 40d of zákon 48/1997 Sb. (enrichment carried in p-0035 [S5]; a future pass
owes a read of the amending article).

Other links: p-0003 ← ecsem-cz2026-admin-burden, ombud-q2-2026 · p-0004 ←
ecsem-cz2026-ltc-mix · p-0009 ← reg-uznavani-kvalifikace-treti-zeme-2028 ·
p-0011 ← dotace-opz-112-pas · p-0024 ← de-aedifion · p-0031 ←
reg-obce-spolecenstvi-sdilene-agendy · p-0034 ← reg-plan2026-eu-infringement.
p-0033 additionally received Directive (EU) 2024/2831 (platform work,
transposition 2 December 2026) as a context source after the who-pays audit
(docs/who-pays-audit-2026-09-03.md) found its worker-status precondition
undated.

**Deferred — the wastewater cluster now has its second signal and is the next
SWEEP topic**, not a record yet: dotace-sfzp-2-2026-fn-cov (1,355.2M CZK,
Directive 2024/3019 compliance loans) + reg-vak-energeticke-posouzeni-cov +
reg-vodni-zakon-epr-mikropolutanty + reg-vak-srazkove-vody-poplatek + the
committed veklep-KORNDXBH65S3. Not authored this run because no gap check with
queries and a positive control exists for it (MATCH agents run without web
access), and because who-pays needs the sweep: ~200 plants above 10,000 PE and
their VaK owners on the energy-assessment duty; pharma/cosmetics producers on
the micropollutant EPR; ~5.5bn CZK/yr of newly charged stormwater. Also
deferred: ecsem-cz2026-housing, gb-zen-educate (no CZ supply-teacher platform
found, unverified), de-recyda (ELO direct but early).

Registry widened in this run, before the append: arb-scan id_prefixes + `us`
(us-polimorphic, us-prepared, us-trulla); demand-scan id_prefixes + `ecsem`
(the European Semester records). Data-quality flags from the harvest agents:
odok.cz → odok.gov.cz redirect (fetch_veklep.sh should follow it);
veklep-KORNDV4MNCNT scored urgency 0 on a dated economy-wide duty (the reg-
record carries the substance); dotace-optak-technologie-mas-2 committed with
`source: hlidac` on a dotace- id (pre-existing provenance mismatch); MS2021+ had
no prior call-id list — this manifest's dotace section is the new left-hand side;
ombudsman ESO search returns an identical empty page for 2024 and 2026, so its
positive control failed and no absence was written.

Addendum from the match agent's report: the wastewater cluster fails TWO limbs,
not one — proof (the corpus holds no foreign comparable for plant energy
assessment or stormwater-surface billing, so comps[] would be empty at proof 0)
and gap (unchecked) — and it collides with p-0026's buyer, where Softlink CEM,
VODÁRENSKÁ, Popron SMG Water, SČVK and SUEZ hold the managed-service seat. The
sweep it needs is an arb-scan leg plus a controlled Czech gap check. Possible
de-rank evidence recorded, not applied: de-aedifion's Czech check names
BUILDSYS a.s. (IČO 27690253, since 2006), HGS a.s. (FLOWBOX) and Novatec EAS
against p-0024 — each reads adjacent (integration and monitoring, not
renovation ranking); a content pass owes the locals[] adjudication. Two FX
rates were used in one run (dotace-scan 24.215 CZK/EUR, demand/reg-scan 24.5).
p-0035 post-build fix: Intrakoop (founded 1959) removed from comps[] because
CompSchema floors `since` at 1980 — it stays as arbitrage source S16; proof 3
rests on Vivecti (DE), Vamstar (GB) and Trulla (US).

## asks run — 2026-09-03 (session localproblems-80, private raw dir /tmp/claude-501/asks-run/2026-09-03)

First run of the two `asks` feeds. Fetched and staged in a private raw dir because this directory held the weekly harvest's staged.jsonl at the time; completed into data/signals/asks/2026-09-03.jsonl with `--complete --allow-incomplete`. 48 staged: pass A by 4 session subagents; the 15 tacr cards were rebuilt to quote the need's stated goal and re-graded by two independent graders (lower grade per field); pass B by 2 subagents over the 32 material survivors. 16 immaterial (scale <= 1, money 0, urgency 0: one body's own study or an undated niche challenge) left staged, never appended.

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-03T1805 | tacr | ok | 200 | 264232 | 15 | 3340 | 2026-09-03T18:05:58Z | /tmp/claude-501/asks-run/2026-09-03 |  |
| 2026-09-03T1808 | hackathon | ok | 200 | 4982327 | 33 | 26587 | 2026-09-03T18:08:08Z | /tmp/claude-501/asks-run/2026-09-03 |  |

### asks first run REWRITTEN under the owner's admission rules (same night, session localproblems-80)

The 32 rows appended earlier tonight were retired from data/signals/asks/2026-09-03.jsonl and seen.txt (first cut kept as a file in the session scratchpad, ids listed below) and the run was repeated from a fresh fetch () under the rules the owner set after the critique: `owner` required and read from the page (no organizer fallback; Rakathon = the three hospitals the page names); a row must state a problem (no bare topic lines: 5 UPOL rows); an event or consultation date is not urgency; materiality for asks drops only at scale 0; and a new `stated_need` admission bar (scripts/model_pass.py RUBRIC) instead of the Reddit `pain` bar, which had refused 29 of 39 inconsistently. Pass A was graded three times: round 1 under `pain` (refused 29), round 2 under `stated_need` by three graders (12 hospital asks scored scale 0 as "one organisation"), round 3 by ONE grader after the asks scale rule was written into the rubric — round 3 stands. 39 staged -> 16 landed (11 challenges, 5 needs): 19 refused by the stated-need bar, 4 dropped at scale 0. Retired ids: hack-5d646892, hack-582e2346, hack-02917635, hack-cf9cd96f, hack-45597a87, hack-e9384233, hack-3a3e4c27, hack-9c4350df, hack-9249a038, hack-22a5dac4, hack-055f015b, hack-d4596b29, hack-759d66ad, hack-22dabb10, hack-36e05628, hack-72b8309a, hack-11bca729, hack-f8ecbbeb, hack-e3d48b98, hack-7dcd7aea, hack-de436281, hack-72133fa5, hack-c5c10e91, hack-20c85264, hack-0ad82a4b, hack-fe987c15, hack-33d5ed0b, hack-0ed2ef9d, hack-9e938f0f, hack-8420e8a8, tacr-ttxmsmt502, tacr-tieru0015


| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-03T1959 | tacr | ok | 200 | 264232 | 14 | 3651 | 2026-09-03T19:59:23Z | /tmp/claude-501/asks-run2/2026-09-03 |  |
| 2026-09-03T1959 | hackathon | ok | 200 | 4982327 | 25 | 22404 | 2026-09-03T19:59:27Z | /tmp/claude-501/asks-run2/2026-09-03 | partial: upol:yield-zero |

### parked feeds activated — sukl + coi (session localproblems-80)

Three feeds had been fully wired since 2026-08-21 and had never produced a record. Run tonight from a private raw dir. SUKL: 15 aggregates over 83,016 supply-notification rows. COI: 17 aggregates over 176,945 final fines and 288,962 inspections. Both scored by ONE grader across all batches, 16 of 32 survived materiality, appended to the demand ledger. Their id prefixes moved from demand-scan.id_prefixes to their own registry rows in the same change (the AC-F3 instruction both blockers carried).

SMLOUVY IS RE-PARKED, and the reason is now measured rather than assumed: the fetcher works (7 daily dumps, 25,587 contracts) but it is a PER-ITEM feed whose items each score money 0 or 1, so 25,192 staged records would cost a full model pass to land a few hundred, and the >20M CZK slice of the same register is already covered by `hlidac`. It needs aggregation before materiality — the rule CONVENTIONS.md states for `hiring` — which is a script that does not exist yet.

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-03T2112 | sukl | ok | 200 | 1618666 | 15 | 3239 | 2026-09-03T21:12:22Z | /tmp/claude-501/parked/2026-09-03 | validity=2026-09-03 rows_in_file=83016 aggregates=15 |
| 2026-09-03T2112 | coi | ok | 200 | 39676640 | 17 | 10603 | 2026-09-03T21:12:26Z | /tmp/claude-501/parked/2026-09-03 | coverage_end=2026-06-30 sankce_rows=176945 kontroly_rows=288962 aggregates=17 fresh=2 cached=0 |
| 2026-09-03T2112 | smlouvy | ok | 200 | 34557957 | 25587 | 59781 | 2026-09-03T21:12:38Z | /tmp/claude-501/parked/2026-09-03 | coverage: capped at 7 day(s) (SMLOUVY_MAX_DAYS) |
