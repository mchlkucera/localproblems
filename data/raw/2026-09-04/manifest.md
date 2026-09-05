
## sweep pass — 2026-09-04 (written 2026-09-05) — municipal wastewater under UWWTD 2024/3019

**Topic as given:** municipal wastewater — treatment-plant energy assessment, micropollutant
(quaternary) treatment and stormwater charging under Directive (EU) 2024/3019 and the Czech
transpositions (draft amendments to zákon 254/2001 Sb. and 274/2001 Sb., VeKLEP KORNDXBH65S3).

**Why this sweep ran:** the 2026-09-03 weekly run staged five signals on this cluster and
deferred a record because it failed two limbs — proof (no foreign comparable on file) and gap
(no Czech check with queries and a positive control). This pass has two jobs, in order:
(1) the arb-scan leg — established foreign vendors for the three obligations; (2) a controlled
Czech gap check, plus MS2021+ price evidence for the manual equivalent. Then a MATCH decision.

**Files:** arb-scan records `data/raw/2026-09-04/staged-sweep-wastewater.jsonl` · this manifest.
Nothing appended to `data/signals/**`, `seen.txt` untouched, no build, no commit — the
orchestrator completes the run. NOTE: `.gitignore` un-ignores only `data/raw/*/manifest.md`;
this file is named as the launcher asked and is gitignored until folded into manifest.md.

### 1. FRAME — decomposition

| leg | who |
|---|---|
| **buyer** | (a) the OWNER of a plant ≥ 10,000 PE — the municipality or the regional VaK company (Ministry RIA: "více než 200 čistíren"), which under the 274/2001 draft must commission an energy assessment of plant + sewer network every four years, approve it and report; (b) the PLANT OPERATOR / owner facing quaternary (fourth-stage) treatment, funded by the pharma/cosmetics EPR scheme under the 254/2001 draft; (c) the SEWERAGE OPERATOR that from 07/2027 must invoice stormwater from surfaces it never invoiced — roads (state, kraje, obce), railways, households on combined sewers. |
| **user** | the plant's process engineer / energy manager; the VaK billing department (zákaznický informační systém, ZIS); the municipality's road-asset officer who suddenly owes stočné for every local road. |
| **regulator** | Ministry of Agriculture (MZe, act 274/2001) and Ministry of Environment (MŽP, act 254/2001), ČIŽP for discharge enforcement; the EU layer is Directive (EU) 2024/3019, transposition deadline 31 July 2027; energy-neutrality path to 2045 with energy audits every four years (Art. 11) and quaternary treatment for plants ≥ 150,000 PE by 2039/2045 (Art. 8); EPR under Art. 9. |
| **money** | SFŽP call 2/2026 FN ČOV: 1,355.2m CZK of 1% loans for plants ≥ 10,000 PE (dotace-sfzp-2-2026-fn-cov, intake 2 July 2026 – 31 March 2027); RIA: 8–15bn CZK sector investment for energy neutrality; ~120bn CZK quaternary treatment total; ~5.5bn CZK/yr newly charged stormwater (reg-vak-srazkove-vody-poplatek). Plus MS2021+ (OPŽP) grants to named utilities for ČOV upgrades — queried below as price evidence. |

### 2. FRAME — search vocabulary

**Czech:** energetický audit ČOV · energetické posouzení čistírny odpadních vod · energetická
neutralita ČOV · optimalizace spotřeby energie ČOV software · digitální dvojče ČOV · řízení
procesu ČOV online · čtvrtý stupeň čištění mikropolutanty · odstraňování mikropolutantů
ozonizace aktivní uhlí ČOV · dodavatel technologie mikropolutanty ČOV · regenerace aktivního
uhlí služba · srážkové vody poplatek výpočet plochy · odvodňovaná plocha srážkové vody
software · zákaznický informační systém vodárny fakturace srážkové vody · zpevněné plochy
letecké snímky GIS obec.

**English / German:** wastewater treatment plant energy optimisation software · WWTP digital
twin SaaS · Energieanalyse Kläranlage Software · Energiecheck DWA-A 216 · Spurenstoffelimination
vierte Reinigungsstufe Anbieter · Aktivkohle Reaktivierung Service Kläranlage · gesplittete
Abwassergebühr Flächenermittlung Luftbild · Niederschlagswassergebühr Software · impervious
area mapping stormwater fee · stormwater utility billing software.

### 3. MINE THE CORPUS FIRST — coverage, not re-minted

`grep -il` over `data/signals/*/*.jsonl` for čistír|ČOV|odpadní vod|wastewater|stormwater|srážkov|mikropolut|kanalizac.

- **REGULATION held:** reg-vak-srazkove-vody-poplatek · reg-vak-energeticke-posouzeni-cov ·
  reg-vodni-zakon-epr-mikropolutanty · veklep-KORNDXBH65S3 · reg-uwwtd-epr (the directive, 2027-07-31).
- **TENDERS held (scripted feeds, read not re-fetched):** dotace-sfzp-2-2026-fn-cov (1,355.2M CZK loans) ·
  dotace-opzp-105-srazkove-sede-vody · plant works and concessions: hlidac-33820213 (Kolín 2026-2035
  sewerage concession, Město Kolín → Energie AG Kolín a.s.), hlidac-36573846 / ted-584883-2026 (Dobruška),
  hlidac-33881281 / hlidac-36853754 / ted-583604-2026 (Jindřichův Hradec), hlidac-36405676 (Rakovník),
  hlidac-36536058 (Slaný), hlidac-36966759 (Jihlava aeration), ted-537436-2026 (Kolovraty), ted-541099-2026 /
  ted-602453-2026 (Brno-Modřice sludge), ted-478249-2026 / ted-557119-2026 (VaK Břeclav control systems),
  ted-568275-2026 (Špindlerův Mlýn plant PV), ted-566557-2026 (VAS PV), ted-493364-2026 (Klatovy stormwater
  basins), ted-480045-2026 (motorway drainage cleaning), hlidac-38604660 (SSHR stormwater retention design),
  seven nen- village sewer works. **None is a software, audit, mapping or billing contract.**
- **DEMAND held:** nku-srazkove-vody (NKÚ 25/08, rainwater adaptation subsidies reached 3% of municipalities —
  adaptation money, not the charge; considered for p-0037 and not cited).
- **FUNDED held:** round-metal-morph (industrial wastewater resource recovery), yc-biobot-analytics (wastewater
  epidemiology) — neither on topic. No comp for any of the three obligations was on file, which is the proof
  limb the 2026-09-03 run failed.
- **PROBLEMS re-read:** p-0026 (same VaK buyer; its locals[] are metering-service vendors — none sells surface
  mapping, energy audits or fourth-stage treatment, so p-0037 does not collide: different product, different
  side of the meter). p-0031, p-0011, p-0033, p-0036 matched only on the word "kanalizace"/"čistír" in passing.

### 3a. FUNDED via arb-scan — 6 records staged (`staged-sweep-wastewater.jsonl`)

| id | company | geo | since | receipt (url · date) | traction | obligation |
|---|---|---|---|---|---|---|
| `de-caigos` | CAIGOS GmbH (VIVAVIS group) | DE | 1987 | caigos.de GAG service page · read 2026-09-04; business-geomatics.com 2017-08-15 (founding); vivavis.com (1,200+ customers) | "mehr als 40 Kommunen" surveyed for the split charge since 2010; >1,200 customers; logos Meissen, Zwickau, Speyer, Ludwigshafen, Lübeck, Regensburg | stormwater surface billing |
| `de-phoenics` | Phoenics GmbH | DE | 1994 | phoenics.de Versiegelungskataster page · read 2026-09-04; LinkedIn (founded 1994, 11-50 staff) | update procedure applied to Hamburg and Frankfurt; "Marktführer ... seit über 25 Jahren" | stormwater surface billing |
| `de-aquabench` | aquabench GmbH | DE | 2003 | aquabench.de · read 2026-09-04 ("über 800 Betriebe"); news page ("seit der Gründung 2003") | 800+ operators; runs Benchmarking Abwasser Bayern and the Schnelltest Energie Kläranlagen | plant energy assessment |
| `dk-envidan` | Envidan A/S | DK | 1995 | ramboll.com completion release · 2026-05-11 | ~500 specialists, 21 offices DK/NO/SE; Proces+ names Tønder Spildevand; bought by Ramboll | plant energy optimisation |
| `nl-haskoning-aquasuite` | Royal HaskoningDHV (Aquasuite) | NL | 1881 (firm) | consultancy.eu · 2021-04-15; haskoning.com/aquasuite/pure read 2026-09-04 | WBL: 17 plants, all 149 pumping stations under Aquasuite; Pure tunes aeration and dosing | plant energy optimisation |
| `be-desotec` | DESOTEC | BE | 1990 | eqtgroup.com release · 2025-11-21 | >2,000 customers EU+NA; world's largest mobile reactivated-carbon filter fleet; EQT Future buying majority from Blackstone | micropollutant treatment as a service |

**Registry change made in this change (SWEEP.md 3a):** `arb-scan.id_prefixes` in `data/feeds.json` gained
`"be"` (Belgium) for `be-desotec`. No other registry row claimed `be` (checked). No other prefix needed.

**Considered and NOT minted, with the reason:**
- **EFTAS Fernerkundung Technologietransfer GmbH (DE, Münster, founded 1988, ~30 staff)** — its flyer
  "Versiegelungskartierung Abwassergebührensplitting" (search snippet: >20 Kommunen since 2010) redirects
  eftas.de → eftas.com and returns 404; the eftas.com homepage does not mention the service. No live receipt,
  no record. A future pass could try the Wayback Machine.
- **Geoventis GmbH (DE, Aßlar)** — sells split-charge software (questionnaires, sealing categories, finance
  integration) but publishes no founding year and no customer count; nothing verifiable for `traction`.
- **Retencja.pl / RetencjaPL Sp. z o.o. (PL, Gdańsk)** — GIShub "Opłaty" automates the Polish retention fee
  (opłata za zmniejszenie naturalnej retencji, Wody Polskie), the nearest CEE analogue; homepage names no
  founding year and no customer, so no established-test limb — and therefore no second market for proof 3.
- **Ecopia AI (CA, Toronto)** — impervious-surface data for US stormwater utilities; `ca` is not an arb-scan
  prefix and its "2,500 municipalities" line describes US fee adopters, not its customers.
- **CarboTech AC GmbH (DE, Essen, since 1956; reactivation since 1974)** and **Donau Carbon / Donau Chemie
  (AT/DE; DONAU PAC AQUACLEAR "seit 2021 im Einsatz")** — real fourth-stage suppliers with a reactivation
  service, but no customer count or named plant on the pages read; established test unreceipted.
- **Xylem / Wedeco (US/DE)** — eight SMOevo ozone systems at Zürich Werdhölzli (434,000 people, CHF 50m upgrade,
  2016-2018); a conglomerate's equipment sale, not a service model. **Veolia Hubgrade Performance Plant (FR)** —
  ">100 installations", same reason. **DHI Group WEST (DK)** — sold in Czechia through DHI a.s. since 1996, so it
  is a local presence, not an arbitrage gap (see 3c-energy below).
- **Transcend Software (US/HU, Series B USD 20m 2023-08-03, 6,500 plant designs)** — generative design for
  new plants, not operation or assessment; off the three obligations.

### 3b. TENDERS via dotace-scan — NULL, by design of this pass

The launcher scoped the sweep to proof and gap. The call already on file (dotace-sfzp-2-2026-fn-cov) was
re-read and cited; no new call was searched for. No scripted prefix was hand-minted. **Coverage gap noted:**
the Kolín 2019 contract "pasport ploch podléhajících platbě za odvádění srážkových vod" (registr smluv
8041799) is exactly on topic and predates the hlidac feed; a fetcher query on "srážkových vod" + "pasport"
would catch the next one.

### 3c. GAP — the Czech check, with the positive control

Method: descriptive Czech queries on google-cz (WebSearch), ARES REST lookups by name, the
`data/lookup/cz-contract-parties.jsonl` buyer count per IČO, and a full-text search of registr smluv via the
Hlídač API (with-secrets curl; three queries). Surfaces recorded per the closed vocabulary:
`google-cz, ares, cz-contract-parties, own-funded-ledger`.

**POSITIVE CONTROL — PASSED.** Query "dálkové odečty vodoměrů jako služba pro vodárenské společnosti
platforma" (google-cz) surfaced VODÁRENSKÁ AKCIOVÁ SPOLEČNOST — a `competes: direct, maturity: established`
entry on p-0026 — first (vodarenska.cz/vas-nove-nabizi-dalkove-odecty-vodomeru/), then KAPKA vodoměry, ČEVAK
and AQUA SERVIS. Softlink (also on p-0026) did NOT surface on that query shape — recorded, not hidden; one
standing incumbent found is a pass, and the method is producing positives.

**(1) Stormwater surface billing — OPEN.** Queries (5 Czech + 1 English, listed in p-0037 S13) plus Hlídač
full text. Every player found:

| player | IČO | since | competes | maturity | what it sells |
|---|---|---|---|---|---|
| USYS / UTILITIES SYSTEMS s.r.o. | 17772796 (entity 2022; product 1992) | 1992 | adjacent | established | USYS.net customer/billing system; customers incl. PVK, BVK, OVAK; bills the charge from a keyed-in area |
| DATAINFO spol. s r.o. | 15046265 | 1991 | adjacent | established | ZIS Vodné a Stočné, bills "vodné, stočné, srážkové vody"; "stovky zákazníků" |
| Softbit software s.r.o. | 27473716 | 2005 | adjacent | early | water-company IS; no stormwater, no customer named |
| Energie AG Kolín a.s. (ex VODOS s.r.o.) | 47538457 | 1993 | adjacent | established | Kolín operator; made the 2019 pasport of liable surfaces for Město Kolín (1,449,918.80 CZK ex VAT, registr smluv 8041799); holds the 2026-2035 concession |
| T-MAPY 47451084 · GEOVAP 15049248 · TopGis 29182263 · ARCDATA PRAHA 14889749 | — | — | not entered | — | GIS/orthophoto vendors checked in ARES; surfaced on none of the stormwater queries, so no receipt that they sell this |

No Czech vendor sells impervious-surface mapping + owner statement + billing handover. Utilities' own pages
(VaK Vysoké Mýto, Moravská vodárenská, VHOS, ČESKOSKALICKÉ VODÁRNY) show the charge computed from
customer-declared areas. **Decision: gap 2.**

**(2) Plant energy assessment — CONTESTED, not open.** Queries: "energetický audit ČOV čistírna odpadních vod
energetické posouzení dodavatel"; "optimalizace spotřeby energie ČOV software řízení procesu čistírna
digitální dvojče"; "energetický audit čistírny odpadních vod firma reference energetický specialista
vodárenská společnost úspory ČOV studie"; "VDT Technology digitální dvojče vodárenství ČOV řízení energie";
"DHI a.s. Praha WEST digitální dvojče ČOV ...". Found: the manual equivalent (energy audit by a licensed
energetický specialista, zákon 406/2000 Sb.) is already sold — Veolia's Czech engineers presented the
four-yearly audit at SOVAK VOD-KA 2025 (Rosenbergová: >100k PE by 2028, >10k PE by 2032; "oprávněných auditorů
je pouze omezený počet") and the MPO specialist list is the buyer's reference (direct, established on
the service side). Software: VDT Technology a.s. (06957021, 2018; En-Key energy management, Twin Skin twin on
Siemens Insights Hub; no customer named — direct, early), DHI a.s. (64948200, 1996; WEST; 1 public buyer in
the lookup), SEWACO s.r.o. (62584260, 1994; SIMBA# distributor for 19 CEE countries, TZB-info 2025-12-04),
ASIO TECH (48910848, 1993), ProjectSoft HK (25286668, 1998). Benchmark-as-a-service (the aquabench shape): not
found; SOVAK runs a members' benchmark. **Not written as a record:** gap would be 0/1 with the audit
incumbents, the buyer is p-0026's, and the SFŽP money funds intensification, not audits. Comps staged for the
next pass.

**(3) Micropollutant / fourth-stage treatment — ADJACENT players present, capex-shaped.** Queries: "čtvrtý
stupeň čištění mikropolutanty ČOV dodavatel technologie aktivní uhlí ozonizace"; "mikropolutanty ČOV
ozonizace realizace Česko pilotní provoz dodavatel čtvrtý stupeň čistírna 2025 2026"; "regenerace aktivního
uhlí služba Česká republika dodavatel granulované aktivní uhlí čistírna odpadních vod". Found: RESORBENT
s.r.o. (25830694, 1999) and EWAC spol. s r.o. (25172956, 1998) regenerate activated carbon as a service;
ENVI-PUR distributes reactivatable GAC; ProMinent Systems spol. s r.o. (48363448, Blovice, 1993; ozone) and
WILO CS (62579207, 1994) are the equipment branches; the only Czech quaternary installation found is the
Thomayerova nemocnice hospital pilot with PVK (ozone + GAC, 2024). **Not written as a record:** the
obligation is 120bn-CZK-class plant construction bought by tender from equipment makers with Czech
branches; nothing a garage builder starts.

### 3d. MS2021+ price evidence (`scripts/ms21_query.py`)

- `--keyword "čistírna" --limit 10`: 15 projects, 734.4M CZK approved — all new village ČOV + sewer
  construction (Žichovice 116.2M, Zemětice 102.6M, Dřetovice 100.4M, Maleč 95.1M, Kolinec 92.1M, Rohozec
  66.6M, Drahotín 49.1M, Jeneč intensification 48.2M, Spálené Poříčí 35.4M, Bohumilice 19.4M). **Subject
  test fails for every hit** — construction, not assessment, treatment stage or billing. Not cited.
- `--keyword "ČOV" --limit 10`: 3,662 matches because the diacritic fold turns "ČOV" into the substring
  "cov" (motorways, railways, hospitals). Useless as a keyword; use "intenzifikace" instead.
- `--keyword "intenzifikace"`: 28 projects, 1,347.8M CZK — Jindřichův Hradec 315.3M, Škvorec 159.2M, Týnec
  nad Sázavou 140.9M, Dolní Dunajovice 116.0M, Litovel sludge + biogas 91.4M, Zaječov 85.8M, Jaroslavice
  80.0M. Plant capex; subject test fails. `--keyword "mikropolut"`: 2 research grants (MBÚ AV ČR 99.9M,
  TU Liberec 0.95M). `--keyword "srážkov"`: 119 adaptation/retention projects, none a billing or mapping
  buy. **No MS2021+ row is cited on p-0037**; its price receipt is the Kolín registr smluv contract.

### 4. DECISION (MATCH.md)

**Record written: `data/problems/cz/p-0037-stormwater-surface-billing.md`** — on obligation (1) only.
Scores: proof 2 (CAIGOS + Phoenics, one market) · money 1 (the Kolín contract, price receipt tagged money) ·
urgency 2 (deadline 1 — July 2027 is a DRAFT's date and the same deletion died in 2006; freshness 1 — the
bill authorised 2026-08-27) · demand 2 (SOVAK's Barák 2020 + MZe's Chaloupka 2006: recurring, documented) ·
gap 2 (this check, control passed) = **9, STRONG**, status candidate. The five existing signals are cited
by id; the two new comps carry NO `signal:` ref on purpose so the record builds whether or not the staged
rows have landed — provenance is in each source note.

Obligations (2) and (3): no record — reasons above; comps staged so the next pass does not repeat the
search. Collision with p-0026: none — same buyer, different product (billing-side surface mapping vs.
metering-as-a-service); p-0037 says so in its notes.

**Owed to the orchestrator:** complete `staged-sweep-wastewater.jsonl` (6 rows, `evidence_type: funded`)
through normalize `--complete`; the `be` prefix widening in `data/feeds.json` is already in the working
tree; `check-records.py --strict` result is recorded below; no web build and no commit were run.

### 5. Checks run

- `python3 scripts/check-records.py --strict` after the record: **records: 37 · clean: 28 · errors: 0 · warnings: 9  (established test run against 2026)** (p-0037: 0 errors, 0 warnings after glossing CAIGOS and dropping the ČÚZK/RÚIAN acronyms from First moves). Argument prose 407 words.
- `node web/scripts/lint-citations.mjs`: p-0037 markers 31, paras 7/7 cited, uncited-numeric 0.
- Staged file parses: 6 rows, all `source: arb-scan`, `evidence_type: funded`.
- Not run, by instruction: `npm --prefix web run build`, any commit, any append to `data/signals/**`, any edit to `seen.txt`.
