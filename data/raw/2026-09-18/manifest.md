# Run manifest, 2026-09-18 — monthly broad scans (four attended feeds, run in parallel)

Folded from the four per-feed manifests written by the parallel scan agents.


---

## demand-scan pass — 2026-09-18

Monthly BROAD pass (pipeline/SCANS.md), feed `demand-scan`, evidence_type
`demand`. Run in parallel with three other scan agents, so this pass kept to
its own paths: payloads and `staged.jsonl` under `data/raw/2026-09-18/demand/`,
this manifest, and the ledger `data/signals/demand/2026-09-18.jsonl`.
No commit, no feeds.json edit, no problem files, no shared DB write.

### How the records reached the ledger (parallel-safe variant of the SCANS.md hand-off)

- Staged 5 records to `data/raw/2026-09-18/demand/staged.jsonl`, all
  `extraction: manual`, each carrying `evidence_type: demand`.
- `normalize.py --raw data/raw/2026-09-18/demand --complete --dry-run --today 2026-09-18`
  against the REAL tree: would append 5 to `data/signals/demand/2026-09-18.jsonl`;
  0 materiality drops, 0 incomplete, 0 identity-key duplicates, 0 AC-GDPR1
  refusals (`evidence_type` stripped by the allowlist, as designed).
- The real `--complete` ran against a SCRATCH COPY of `data/signals/` (same
  corpus, so the id and identity-key dedup saw everything), because its
  seen.txt write rewrites the whole shared file and three other agents were
  appending to it. The resulting 5-line file was copied to
  `data/signals/demand/2026-09-18.jsonl`, and the 5 ids were appended to
  `data/signals/seen.txt` in one `>>` after re-reading it. **seen.txt is
  therefore not sorted after this pass**; the next `normalize.py --complete`
  run re-sorts it on write.
- Validation without the shared DB: `scripts/db.py rebuild` and
  `db.py prefixes` in a scratch mirror of the repo (scripts, feeds.json, the
  scratch ledgers, problems). `rebuild OK jsonl_lines=17126 ==
  signals_count=17126`; `AC-F3 OK — every prefix claimed; 0 ambiguous, 0
  undeclared` (`nku-` goes to the `nku` row, `ombud-` to `demand-scan`).
  **Not run:** `web/scripts/db-gate.mjs` (the zod SignalSchema check), because it
  rebuilds `data/register.db` in place. The five records use exactly the
  field set of the 2026-09-03 demand-scan records already in the ledger.
- `db.py upsert` NOT run: it writes the shared `data/register.db`. The
  coordinator runs `python3 scripts/db.py upsert data/signals/demand/2026-09-18.jsonl`.

### Checklist source 1 — NKÚ kontrolní závěry (PARSE THE PDFs)

Visited. Věstník index `https://www.nku.cz/cz/publikace-a-dokumenty/vestnik/`
(200): newest issue is still částka 3/2026 of 13 August 2026, no 4/2026. RSS
`https://nku.cz/cz/rss.xml` (200) read for everything since 3 September.
Existence probe over `assets/kon-zavery/kNNNNN.pdf`: **k25013 200, k25014 200**
(both 404 on 2026-09-03), k25017 200 (already held as `nku-dia-ucetnictvi`);
404: k25018, k25019, k25022–k25026, k26001–k26006.

**2 records minted, both from the conclusion PDFs** (`pdftotext -layout`, the
ZÁKLADNÍ FAKTA and I. Shrnutí a vyhodnocení sections):

| id | action | responsible body | quantified failure |
|---|---|---|---|
| `nku-zdravotnicky-vyzkum` | 25/13 | MZd (AZV selects projects) | 9bn CZK of health R&D 2020–2024; 0 MZd controls of 3.6bn CZK institutional support ever; no programme evaluation; the 2019 government task left undone |
| `nku-ikem-hospodareni` | 25/14 | IKEM; MZd as founder | law broken in 15 of 30 contracts (380.1m CZK); 59.5m CZK IT services via ≥345 orders with no tender; 182.2m CZK suspected budget-discipline breaches |

- **25/14 closes the named coverage item from 2026-09-03** (IKEM, approved
  17 August 2026, PDF then 404).
- **25/13's headline verdict is partly POSITIVE** (transparent selection, 37 of
  41 checked projects used in practice) and the record's `notes` say so; it
  exists for the evaluation and control gap.
- **Headline twins, for MATCH:** the scripted `nku` feed staged the 25/13 press
  release as `nku-15872` in `data/raw/2026-09-08/staged.jsonl`, still pending
  and in no ledger. The IKEM press release (id15897, 14 September) is not yet
  fetched by that feed. If either lands later it is the same audit as the
  record here, under a different url, so identity-key dedup will not catch it.
- **Read and not minted:** the 31 August state-closing-account opinion and its
  press release are already held as `nku-15849` / `nku-15851` (scripted feed).
- **New named coverage item — 25/24, approved but unpublished.** The 13th
  Kolegium (7 September 2026) approved the conclusion of audit 25/24,
  *Peněžní prostředky určené na podporu revitalizace veřejných prostranství
  měst a obcí*; `k25024.pdf` → 404. A future pass owes it a re-probe.

### Checklist source 2 — European Semester CZ package

Visited. Landing page `.../country-report-czechia_en` (200): the newest item is
still the 2026 Country Report of 3 June 2026, harvested on 2026-09-03 as
`ecsem-cz2026-housing` / `-admin-burden` / `-ltc-mix`, with the Council CSR as
`ecsem-cz2026-csr`. **Nothing new this pass, 0 records.**

**Partial gap carried forward, still open:** the OJ C reference for the
Council's Czechia recommendation of 10 July 2026. EUR-Lex quick search
returned **HTTP 202 with a 0-byte body** (a bot challenge). This pass did not
try to get round it. A future pass owes it a lookup from a real browser
session. If an OJ reference turns up, it belongs in a note on `ecsem-cz2026-csr`,
not in a new record.

### Checklist source 3 — MPSV Statistická ročenka, chapter 5 "Sociální služby"

Visited. `https://mpsv.gov.cz/statisticka-rocenka-z-oblasti-prace-a-socialnich-veci-archiv`
(200, 1.3 MB): newest edition listed is still *… v roce 2024* (`.7z`), and the
page has no "v roce 2025" string at all. **EXPECTED ABSENCE**, per SCANS.md
item 3 (the edition lands around September). 0 records. The next pass should
check again and compare tab 5.9 with 70,209 DS, 37,849 DZR and 4,043
(`civic-mpsv-rocenka-neuspokojene-2024`).

### Checklist source 4 — Ombudsman ESO (HTML walk, no RSS)

Visited. `https://www.ochrance.cz/eso/zpravy/` (200) is still the taxonomy
explainer. The search app is `https://eso.ochrance.cz/`.

**THE 2026-09-03 FAILED CONTROL IS FIXED. The method now works, with a passed
positive control.** The results page is only a shell. The rows come from a
second, session-bound call:
1. `GET https://eso.ochrance.cz/` with a cookie jar;
2. `POST /Vyhledavani/Search` with the form fields. Let curl follow the 302 to
   `/Nalezene` as a GET: `-X POST` with `-L` re-POSTs with no body and gets
   HTTP 411;
3. `POST /Nalezene/GetPocetVysledku` gives the hit count;
4. `POST /Nalezene/GetTableContent` with
   `page=N&rows=50&sidx=SpisovaZnacka&sord=desc` returns the table.
   `sidx=DatumVydani` returns zero rows.

**Positive control:** `FormaZjisteni=22` (Souhrnná zpráva z návštěv zařízení,
§ 21c) → 41 hits, including the known 27/2023/NZ (19.07.2024) and 51/2021/NZ
(13.12.2023). The method finds reports that are known to exist, so its
negatives below mean something.

Walked this pass:
- **Systematic-visit summary reports (§ 21c, type 22):** the newest is still
  27/2023/NZ of 19 July 2024. **Nothing issued in 2025–2026.** Individual 2026
  visit reports (type 11, since 1 January 2026): 5 (police cells 41/2025/NZ and
  42/2025/NZ, prison 28/2025/NZ, children's homes 18/2025/NZ and 20/2025/NZ).
  Each is a single facility, so scale 0; none minted.
- **Everything issued since 1 June 2026 (all types):** 43 documents. Individual
  inquiry reports (§ 17/§ 18) and dismissals: single cases, scale 0, not
  minted. 10/2026/SZD (a Constitutional Court statement on social services for
  a child with autism) is already covered by `ombud-autismus-sluzby`.
  45315/2026/S (28 August 2026) is the ombudsman's analysis of the
  *bezpečnostní novela*. It was submitted without an inter-ministerial comment
  round and would make temporary protection lapse automatically. That is
  legislative commentary, so it is **handed to reg-scan** and not minted as
  demand.
- **Research reports (Výzkumná zpráva, činnost úřadů, type 29) since 2025:**
  4 found. None was in the corpus, because ESO could not be read before this
  pass. **3 minted**, each quote checked against the PDF text:
  - `ombud-male-obce-statni-sprava`, 3626/2024/VOP (10 March 2026): state
    administration in small municipalities. 2,191 type-I and 140 type-II
    municipalities answered; 69% name misdemeanour proceedings and 61% public
    guardianship as the heaviest agendas; 90% of municipalities over 10,000
    say the state contribution does not cover the cost.
  - `ombud-stiznosti-zdravotnictvi`, 12344/2022/VOP (13 January 2025): how
    regional authorities handle complaints about healthcare. 7% upheld (147 of
    2,115, 2018–2022); 53% struggle to find independent experts; experts earn
    409 CZK/h on average.
  - `ombud-cizojazycna-podani`, 3572/2023/VOP (14 July 2025): foreign-language
    e-submissions. 336 respondents (90% return); 59% of the offices of
    municipalities with extended powers (ORP) answer only in Czech; 49% lack
    language staff.
  - **Not minted:** 1827/2025/VOP (15 April 2025), a survey of what troubles
    children and young people (271 + 145 respondents). The themes are broad,
    the sample is not representative by region, and it names no failure of a
    body.
- **Quarterly reports:** Q3 2026 is not due until after 30 September 2026. The
  expected absence stands; `ombud-q2-2026` is the newest.
- **Aktuálně stream** (`https://www.ochrance.cz/aktualne/`, 200), everything
  since the 2026-09-03 pass. 15 September is a job advert. 3 September explains
  students' health insurance: information, not a pain. The 27 August single
  case was already seen on 2026-09-03. **Nothing minted.**

### Dedup done before minting

- `data/signals/seen.txt` held 17,121 ids at the start of the pass; none of the
  5 ids was in it.
- Topic greps across all ledgers: small-municipality agendas, foreign-language
  submissions, healthcare complaint handling, IKEM and health research. The
  only neighbour is `reg-verejne-opatrovnictvi-prenos-2027`, which is related
  (the guardianship agenda transfer) but a different record, and the notes say
  so. IKEM appears only in scripted tender and pre-tender consultation records
  (`ted-…`, `nenptk-…`), never as an audit finding.
- Identity-key dedup at `--complete`: 0 skipped.

### Receipts

Every `url` returned 200 at harvest. Records carry `http_status: 200` and
`fetched_at: 2026-09-18T15:30:00Z`. All 5 `quote` values are **machine-checked
literal substrings of the `pdftotext` output after whitespace collapse**. One
first choice for `ombud-stiznosti-zdravotnictvi` failed that check, because the
PDF breaks "2018– 2022" across a line. It was replaced with a sentence that
passes, not shortened with an ellipsis. Money is converted at 24.5 CZK/EUR,
the corpus rate. The three ombudsman records carry `money_eur: null`, with a
note saying no figure is published.

### New problem candidates for MATCH (no match run here, by rule)

- **Delegated-agenda burden in small municipalities** (`ombud-male-obce-statni-sprava`,
  with `reg-verejne-opatrovnictvi-prenos-2027`): misdemeanour proceedings and
  public guardianship are the two named agendas.
- **Healthcare complaint investigation capacity** (`ombud-stiznosti-zdravotnictvi`):
  a shortage of independent experts at the second-instance authorities.
- Weaker, as corroboration: foreign-language handling at authorities
  (`ombud-cizojazycna-podani`), and state health-R&D evaluation
  (`nku-zdravotnicky-vyzkum`).

### Pass summary

```
feed:                     demand-scan (monthly broad pass, evidence_type demand)
checklist sources:        4 of 4 visited (NKU / European Semester / MPSV rocenka / ombudsman ESO)
records staged:           5  (2 nku- · 3 ombud-) -> 5 appended, 0 materiality drops
coverage gaps named:      1 new (NKU 25/24 conclusion approved 7 Sep, PDF 404)
                          + 1 partial carried (OJ C ref for 2026 CZ CSR — EUR-Lex bot challenge)
                          + 1 expected absence (MPSV rocenka 2025 not yet published)
                          closed: NKU 25/14 (IKEM) now read; ESO search method fixed, control passed
rotation state:           n/a — category rotation is arb-scan's duty
```

---

## reg-scan pass — 2026-09-18

Monthly BROAD pass of `reg-scan` (feed row: `evidence_type` regulation, `source`
`reg-scan`, `id_prefixes` ["reg"], runner attended, cadence monthly). Operating file:
`pipeline/SCANS.md`, reg-scan checklist items 1–4. Previous pass: 2026-09-03
(`data/raw/2026-09-03/manifest-reg-scan.md`); this pass starts from what that one owed.

Run in parallel with the demand, dotace and arb scans, so it wrote only to its own paths:
raw captures under `data/raw/2026-09-18/regulation/`, the ledger
`data/signals/regulation/2026-09-18.jsonl`, and a single append to `data/signals/seen.txt`.

**Records: 25, all `reg-` prefixed, all `extraction: manual`, all carrying a verified
`quote`.** Staged in `data/raw/2026-09-18/regulation/staged.jsonl` and passed through
`normalize.py --complete` (details under Hand-off). 0 materiality drops, 0 id duplicates,
0 identity-key duplicates, 0 AC-GDPR1 refusals.

### Registry changes needed

**None.** Every record uses the `reg-` prefix and `source: reg-scan`. No `veklep-`,
`echys-` or other feed's prefix was minted.

### Access notes (measured today — read these before the next pass)

- **EUR-Lex** (`eur-lex.europa.eu`) answers curl with **HTTP 202, an empty body and
  `x-amzn-waf-action: challenge`**. That is an AWS WAF bot challenge. It was **not** bypassed.
  The EU half of this pass used the Publications Office's official machine route instead:
  the CELLAR SPARQL endpoint `https://publications.europa.eu/webapi/rdf/sparql`
  (`cdm:official-journal-act_date_publication` enumerates OJ L acts by publication date)
  and CELEX content negotiation `http://publications.europa.eu/resource/celex/<CELEX>`
  (`Accept: application/xhtml+xml`, `Accept-Language: eng`), which returns the full text.
  Record urls still cite the canonical `eur-lex.europa.eu/eli/...` address.
- **VeKLEP / ODok** (`odok.gov.cz`, `www.odok.cz`) returns a **"Požadavek byl zablokován"
  page to curl's default User-Agent**, for material pages and attachments alike. An honest,
  descriptive UA (`localproblems-reg-scan/1.0 (+https://localproblems.vercel.app)`, the same
  practice `fetch_reddit.sh` uses) gets **HTTP 200 with the real `.docx`/`.pdf`**. No browser
  was impersonated. Material **metadata** came from the Hlídač dataset API
  (`api.hlidacstatu.cz/api/v2/datasety/veklep/hledat`, token via
  `with-secrets … curl --variable %HLIDAC_STATU_TOKEN`). **Scripted-feed implication:**
  if `fetch_veklep.sh` or any future RIA fetcher downloads from ODok with a bare curl, it
  will save the block page as the payload. That is the 200-with-a-login-page shape
  INGEST.md warns about.
- **e-Sbírka: the gap the last pass named is now CLOSED.** The ELI open-data endpoint
  `https://opendata.eselpoint.gov.cz/esel-esb/eli/cz/sb/<year>/<n>` (with
  `Accept: text/turtle`) returns each act's versions and effective dates. The promulgated
  text is readable fragment by fragment: take the version's `…/dokument/…` fragments, then
  `esel-esb/právní-akt-fragment/<id>` → `text-fragmentu`. A binary search on `<n>` found the
  newest 2026 act, and acts 140–167/2026 were enumerated with titles and dates. Script and
  payloads: `data/raw/2026-09-18/regulation/esbirka/` (`enum.py`, `fulltext.py`,
  `esbirka-2026-140-167.json`, `sb-2026-{150,152,164}.txt`). **Positive control:** 270/2025,
  the act the last pass proved live, returns its known versions 2025-08-05, 2026-01-01,
  2026-07-01 and 2027-01-01. A number with no act returns the 768-byte prefix-only shell,
  so "absent" is measurable.

---

### Checklist source 1 — Programové prohlášení vlády + semi-annual fulfilment evaluations

**Visited.** https://vlada.gov.cz/cz/vlada/programove-prohlaseni/programove-prohlaseni-vlady-224629/
returned HTTP 200 and is **unchanged**: one PDF (January 2026) and no evaluation attachment.
The vlada.gov.cz RSS (`https://vlada.gov.cz/cs/urad/RSS/rss.xml`, 17 items, 14–18 Sep 2026)
and the news listing were read for evaluation items. The listing renders by JS and shows
only its "Nepřehlédněte" box, so the RSS was the working surface.

- **No new fulfilment evaluation exists.** The only one is still the press event of
  9 July 2026 that the last pass recorded. The next is expected around January 2027.
- **Programme-derived item found and recorded:** the 14 September 2026 government meeting
  approved **Lex Kratom**. The PM framed it as delivering a programme promise ("Pokračujeme
  v tom, co jsme řekli a co jsme slíbili"). Its dated substance was read from the approved
  VeKLEP bill text (see source 4): **`reg-lex-kratom-2027`**.
- **Read, not recorded:** at the same meeting the government discussed its criminal-policy
  priorities "plynoucí z programového prohlášení". **No dates.** It also set up the
  construction-law implementation panel GRIP, which is an institution and imposes no duty.
- **Still-open gap (carried):** there is no published, machine-readable fulfilment
  evaluation. The limit belongs on the feed row. A future pass owes a check around
  January 2027.

### Checklist source 2 — Plán legislativních prací vlády 2026

**Visited.** The plan page (HTTP 200, 23. 3. 2026) is unchanged: two annexes.

- **Annex 2 ("Výhled … na léta 2027 až 2029") — READ IN FULL this pass**, closing the last
  pass's named gap. **69 tasks** in total: 43 in the 2027 section, 18 in 2028 and 8 in 2029.
  Government deadlines run 2027 Q1 to 2029 Q4 and planned effect runs 01.2028 to 01.2031.
  **9 tasks name an EU act.** The enumeration is in
  `regulation/plan/annex2-tasks.tsv`.
  **Records (9):** `reg-jednotne-inkaso-samovymereni-2028` (MF-2),
  `reg-adr-spotrebitelske-spory-2028` (MPO-2 + MF-3, directive 2025/2647),
  `reg-dph-dovoz-platformy-2028` (MF-6, directive 2025/1539 + ViDA Art 3–4),
  `reg-taxi-cestina-platformy-2028` (MD-1), `reg-kamiony-parkovani-13-1997-2028` (MD-2),
  `reg-zakon-humanni-leciva-2028` (MZd-2), `reg-predkupni-pravo-puda-2028` (MZe-1, 2027 section),
  `reg-zpf-vynimani-2029` (MŽP-1), `reg-zdrav-sluzby-kvalita-2029` (MZd-1, 2028 section).
  **Annex-2 items not recorded because the corpus already carries them:** CSDDD →
  `reg-csddd-stop-clock`; the 2029 VAT digital-reporting task → `reg-vida-timeline`; the social
  services act → `reg-soc-sluzby-novy-zakon-2031`; the 2029–2030 minimum-wage coefficient →
  `reg-min-mzda-koeficient-2027-2028`; early retirement for demanding work → `reg-mpsv-narocne-profese`.
- **Annex 1 backlog the last pass named, "read, in scope, NOT recorded":** it was worked
  through this pass.
  **Recorded (5):** `reg-irz-portal-emisi-2028` (MŽP-9, Reg 2024/1244),
  `reg-ovzdusi-aaqd-2026` (MŽP-3, directive 2024/2881, transposition deadline 11 Dec 2026,
  infringement footnote), `reg-e-povinny-vytisk-2027` (MK-1, already in the Chamber as sněmovní
  tisk 192), `reg-zbrane-konec-koncesi-2028` (MV-4), `reg-prumyslove-vzory-oprava-2027`
  (MPO-15, directive 2024/2823).
  **Recorded from VeKLEP instead of the plan text:** MMR-1 → `reg-eturista-registr-ubytovani-2028`,
  and the startup act → `reg-startup-evidence-odpocet-2027` (see source 4).
  **Not recorded, one reason each:**
  - MF-11: already in `reg-ekon-ochrana-statu`.
  - MMR-2 (procurement): loosens rules, no dated duty.
  - MMR-3 (housing cooperatives): relief, no duty.
  - MPO-14 (FDI screening): no EU act named, small population.
  - MF-6 (DPS): pension companies only, already in the Chamber as tisk 285.
  - MF-15 (MTPL): no substance stated.
  - MV-3 (110/2019): the regulator's own procedure.
  - MZd-4: simplification only.
  - MZe-1 (pozemkové úpravy): procedure. The bill is VeKLEP KORNDUAFXG1S; its RIA was
    downloaded to `regulation/veklep/ria_KORNDXHECEFH.docx` but not recorded.
  - MZe-5: widens a visa route, no duty.
  - MPS-1: framework only.
- **Plan records share the annex PDF url.** `--complete` exempted it from identity dedup as a
  listing, as intended: annex 1 is carried by 16 ledger records, annex 2 by 9 in this batch.

### Checklist source 3 — e-Sbírka and EUR-Lex

**e-Sbírka — visited, FULL enumeration of 140–167/2026 via ELI open data.** The newest
act is **167/2026 Sb.** (NV of 17 Aug 2026 on direct payments, in force 2026-10-01).
- **Recorded (2):**
  - `reg-min-mzda-2027-164-2026`: **164/2026 Sb.** (coefficients 0.446 for 2027 and 0.458
    for 2028, in force 16 Sep 2026) plus **150/2026 Sb.** (MF predicted average wage for
    2027: 55,627 CZK). This is the enactment of what the corpus held only as a proposal
    (`reg-min-mzda-koeficient-2027-2028`, `veklep-KORNDV4MNCNT`).
  - `reg-superdavka-normativni-najemne-okresy`: **152/2026 Sb.** Superdávka normative rent
    set by district from 1 Oct 2026; parental-allowance change from 1 Jan 2027.
- **Seen, not recorded (with reason):**
  - 141/2026 (housing-support accounting decree): procedural, under `reg-podpora-bydleni-2026`.
  - 143/2026 (toys NV): administrative alignment.
  - 144/2026 (carbon-leakage compensation conditions, effect 1 Jan 2027): the last pass
    deferred it to its CZK amounts, and none are in the text read.
  - 145/2026 (RUD shares) and 149/2026 (budget reporting): state-internal.
  - **147/2026 (ČNB decrees after Act 130/2026 on investment companies and funds, versions
    2026-09-01 and 2027-07-01).** Act 130/2026 is **not in the corpus**. A future pass owes it
    a read, to find out whether it is the AIFMD II transposition and what its dates are.
  - 151/2026 (trade-licence contents), 153/2026 (MZd IS access decree), 158 and 165 (nature
    protection), 160 (banknotes), and the notices and treaties 140, 142, 148, 156, 161, 162, 163.
- **Named gap:** 154, 155, 157, 159 and 166/2026 return the "právě digitalizujeme" stub, so no
  text is available yet. 156/2026 records the Chamber overriding the Senate on "některé
  zákony v oblasti veřejných rozpočtů", so one of the stubs is probably that act.
  **A future pass owes those five numbers a re-read.**

**EUR-Lex — visited via CELLAR (see Access notes).** Every OJ L act published
2026-09-04..2026-09-18 was enumerated (82 distinct CELEX, `regulation/cellar-ojL-pub-2026-09-04_18.csv`).
Material ones were read in full (`regulation/eu/`).
- **Recorded (3 from the window):**
  - `reg-eudr-annex-i-scope-2027`: Delegated Reg 2026/2102, in force 18 Sep 2026. The EUDR
    product list is rewritten. Additions apply from 30 Dec 2027; the removals (leather,
    rubber articles, used tyres, seats and others) apply at once.
  - `reg-mifid-issuer-sponsored-research`: Delegated Reg 2026/1092.
  - `reg-crr3-frtb-market-risk-2027`: Delegated Reg 2026/1221. FRTB applies from 1 Jan 2027,
    with relief to 2029.
- **Not recorded:**
  - 2026/2048: publishes harmonised standard EN 18060:2025 for batteries; no new duty.
  - 2026/1970 (ETIAS): addressed to authorities; no start date.
  - 2026/2031 (ATM/ANS): a handful of certified providers.
  - 2026/1423 (chlorpyrifos POPs limit): the substance is already unapproved.
  - 2026/1975: an F-gas **exemption** for compressed-air dryers ≤50 kW, 2027–2030.
  - The SAF aviation-allocation decision and 2026/1470 (projects list): no duty.
  - The routine families (biocides, feed additives, GIs, SPS emergency measures, trade defence,
    CFSP).
- **No new directive** was published 2026-07-01..2026-09-18, and **no new EP/Council
  regulation** 2026-08-15..2026-09-18 (SPARQL, with a positive control: the same query
  unfiltered returns 32026L1472 and 32026R1818).
- **Back-window catch-up (published 2026-07-01..2026-08-14, missed by earlier passes):**
  - `reg-dogs-cats-welfare-traceability`: Reg 2026/1818, staggered 2028–2041.
  - `reg-elv-vehicle-circularity`: Reg 2026/1738, staggered 2028–2036.
  - **Drafted and then dropped:** Reg 2026/1703. It removes Switzerland from the ban on
    exporting mixed municipal waste; it narrows a ban rather than adding a duty, which is the
    same reason 2026/1975 was dropped.
  - Borderline, **not read (named gap):** 32026R1739 (farmers' position in the food supply
    chain).
  - Not material: 32026R1881 (CSAM derogation), 32026R1768 (EAFRD funding).

### Checklist source 4 — VeKLEP RIA "Definice problému" for items the scripted feed surfaced

Input: the scripted feed's newest ledger, `data/signals/regulation/2026-09-08.jsonl`,
**4 `veklep-*` records**. All 4 were opened through Hlídač metadata plus ODok attachments.

| veklep id | material | RIA? | outcome |
|---|---|---|---|
| `veklep-KORNDXPG8PUE` | MPs' bill, Police Act 273/2008, tisk 297: police may close a shop for up to 14 days over a product posing a serious risk | No (MPs' bill); materiál PDF read | No separate record. Effect is "first day of the second month after promulgation", so there is **no fixed date**. The government backed it on 14 Sep 2026; it is folded into `reg-lex-kratom-2027` notes |
| `veklep-KORNDXKCNG9P` | NV 347/2016, SÚJB expert-activity fees | No RIA ("není proveden"); zd read | No record. Inflation indexation of fees effective 1 Jan 2027, unchanged since 2017 (cumulative CPI 55.05 % since 2016). No new duty |
| `veklep-KORNDXP9W6EW` | Decree 298/2014, agricultural-land base prices per cadastre | No RIA; zd read | No record. Routine update of the property-tax price table, effective 1 Jan 2027 |
| `veklep-KORNDTUBDJRM` | Decree on the critical-infrastructure portal (§ 20 of Act 266/2025) | No RIA; materiál read | No record. Effect "first day of the month after promulgation" gives **no fixed date**; the duty itself is under `reg-cer-zakon-266` |

**Beyond the floor, and the reason it was needed:** the scripted `veklep` feed **has not
run since 2026-09-08**, so the drafts touched since then are in no ledger. The Hlídač
dataset was queried for `datumPosledniUpravy:[2026-09-01 TO *]`: **65 items, 55 on the 3
pages read. 26 of those 55 are not in `seen.txt`** (list in
`regulation/veklep/hl-veklep-since0901-all.json`). The RIAs of the material ones were read,
which produced these records:
- `reg-startup-evidence-odpocet-2027` (ALBSDXTKB4NK / KORNDXY8B5OY): the draft startup act.
  **Effect 1 July 2027, six months earlier than the plan-based `reg-startupy-zakon` says.**
  The RIA's cost estimate is used as money (lower bound 65M CZK/yr).
- `reg-eturista-registr-ubytovani-2028` (ALBSDXWJ7VQX): the Tourism Act / eTurista /
  STR single entry point. **Effect now 1 January 2028, a year later than the 1 Jan 2027 in
  `reg-str-registr-pronajmu`.**
- `reg-nucena-prace-dozor-cz-2027` (KORNDXQH4G02): Czech enforcement of the Forced Labour
  Regulation (labour inspectorate, market surveillance, customs, fines to 5M CZK). Effect
  14 Dec 2027.
- `reg-lex-kratom-2027` (KORNDVEC8EF8, already a `veklep-` record with metadata only): the
  government-approved bill, effective 1 Jan 2027.

Not recorded among the unseen items:
- Tax-form and customs-form decrees (KORNDXRB97TP, KORNDXRBYXXJ).
- The 2026 travel-allowance rate decree KORNDXWQDTHG: a routine mid-year change.
- Vignette and toll decrees KORNDY2BWJMB and KORNDY2BX7OK (2026-09-18): the valorisation
  topic is already `reg-dalnicni-znamka-valorizace`; a future pass owes the new rates.
- Sport-support act ALBSDW3HDEWG: stage 8, going to government.
- Various service and uniform decrees.

**The scripted feed owes a run:** the next INGEST `fetch_veklep.sh` will surface those
26 items as `veklep-` records. No `veklep-` id was minted here.

---

### Evidence-bar compliance

- **Enacted vs draft is stated on every record**, as `STATUS:` in `notes`.
  - **Enacted instruments recorded directly (7):** 2 Czech Sbírka acts (164+150/2026,
    152/2026) and 5 EU acts (EUDR 2026/2102, MiFID RTS 2026/1092, CRR3 2026/1221,
    dogs/cats 2026/1818, ELV 2026/1738).
  - **Czech drafts (18):** 4 government bills from VeKLEP (Lex Kratom was approved by the
    government; the startup act, eTurista and the forced-labour act are in comment
    procedure) and 14 plan items. Several of the drafts implement an EU act that is already
    enacted: the ADR directive 2025/2647, the import-VAT directive 2025/1539, IRZ Reg
    2024/1244, AAQD 2024/2881, the designs directive 2024/2823 and FLR 2024/3015. Each such
    record's notes carry the EU deadline.
  - Plan-item urgency is capped at 2 because the date is a ministry target. Lex Kratom
    scores urgency 3 because its 1 Jan 2027 date is in the approved bill text, less than
    6 months out. That follows the precedent of `reg-min-mzda-koeficient-2027-2028`.
- **Every record has dates.** `date` holds the application or effective date, and every
  surrounding date (authorisation, comment deadline, government meeting, transposition
  deadline, phase-in) is in `notes` with its source.
- **Money:** one record carries money. `reg-startup-evidence-odpocet-2027` uses the RIA's
  own lower-bound public cost of 65M CZK at **24.5 CZK/EUR**, the corpus rate. Every other
  `money_eur` is null with a `money_note`. The Lex Kratom tax-revenue estimate is **not**
  scored as money, because it is fiscal yield and not budget attached to the need.
- **Quotes:** **25 of 25 were verified as literal substrings of the whitespace-collapsed
  fetched payload.** Mine were checked against the extracted `.docx` and e-Sbírka fragment
  text; the EU and plan sets were checked by their drafting agents against the CELLAR xhtml
  and the `pdftotext -layout` text. Some plan quotes keep PDF line-break hyphenation
  ("envi- ronmentálních"). That is verbatim to the payload, and was not "cleaned" into a
  non-verbatim string.
- **No absence claim** is made anywhere, so no positive control was owed for gaps. The two
  "none found" enumerations (directives, EP/Council regulations) each carry a positive
  control, as does the e-Sbírka route.
- **No personal data.** The VeKLEP `adresaPripominek` field (a civil servant's email) was
  not written. Ministers and MPs appear only in office. A grep of the output for email and
  phone patterns returned zero.

### Facts in existing records this pass found stale (for MATCH/PROCESS — ledgers are append-only, so nothing was edited)

- `reg-str-registr-pronajmu`: effect 1 Jan 2027 → the published draft says **1 Jan 2028**
  (see `reg-eturista-registr-ubytovani-2028`).
- `reg-startupy-zakon`: planned effect Jan 2028 → the published draft says **1 Jul 2027**
  (see `reg-startup-evidence-odpocet-2027`).
- `reg-eudr-deforestation`: Annex I **narrowed** from 18 Sep 2026 (leather, rubber articles,
  used tyres and seats out) and extended from 30 Dec 2027 (see `reg-eudr-annex-i-scope-2027`).
- `reg-fgas-2027-bans`: compressed-air dryers ≤50 kW are exempt 2027–2030 (Reg 2026/1975).
- `reg-ai-act-milestones`: its notes say the Digital Omnibus binds "upon OJ publication".
  It **was published as Reg 2026/1744 on 2026-07-24**.
- `reg-min-mzda-koeficient-2027-2028`: the proposal is now **enacted** as 164/2026 Sb.

### Hand-off

Staged `data/raw/2026-09-18/regulation/staged.jsonl` (25 records: 6 from my own reading,
5 EU, 14 plan). The shared `data/raw/2026-09-18/staged.jsonl` was **not** used, because
three other scans write into this raw date concurrently. The ledger is this feed's own file.

```
python3 scripts/normalize.py --raw data/raw/2026-09-18/regulation --complete --dry-run --today 2026-09-18 \
    --out-dir $TMPDIR/regscan-sim/signals --seen $TMPDIR/regscan-sim/signals/seen.txt
  -> would append 25 across 1 file; 0 materiality drops; 0 incomplete; 0 AC-GDPR1 refusals;
     identity-key dedup: 0 skipped, 2 listing urls exempted (plan annex 1 and annex 2 PDFs)
python3 scripts/normalize.py … --complete (same args, fresh scratch copy of data/signals)
  -> appended 25 records to <scratch>/signals/regulation/2026-09-18.jsonl
```

`--complete` ran against a **scratch copy** of `data/signals`, so that it could not
rewrite the shared `seen.txt`, which it re-sorts in place. Its output file was then copied
verbatim to `data/signals/regulation/2026-09-18.jsonl` (the file did not exist before). The
25 new ids were appended to `data/signals/seen.txt` in **one** `>>` append, after a re-read
of the file (17,126 lines at that moment) confirmed that none of them was present.
**`seen.txt` is therefore no longer fully sorted**; the next `--complete` or a coordinator
`sort -u` restores the order. The output was also checked against `SignalSchema`'s rules
(key allowlist, id regex, source enum, url, ISO date, sector enum, geo regex, integer scores
0–3, quote ≤300), and every record passes.

**NOT run, by the parallel-safety rule of this pass (the coordinator owes it):**
`python3 scripts/db.py upsert data/signals/regulation/2026-09-18.jsonl`. No commit. No build.

### 5-line pass summary

```
feed:                reg-scan (evidence_type regulation, prefix reg-, monthly broad pass)
checklist sources:   4 of 4 visited (programme + evaluations · plan 2026 annex 1 AND annex 2 · e-Sbírka (ELI enumeration 140–167/2026) + EUR-Lex (via CELLAR) · VeKLEP RIAs for all 4 surfaced veklep ids + 4 unsurfaced drafts)
records staged:      25 → appended to data/signals/regulation/2026-09-18.jsonl (0 registry changes needed)
coverage gaps named: 5 — no published fulfilment evaluation (carried) · 5 e-Sbírka numbers still "digitalizujeme" · Act 130/2026 + 32026R1739 unread · scripted veklep feed not run since 09-08 (26 unseen items) · EUR-Lex WAF (worked around via CELLAR, not bypassed)
rotation state:      n/a (category rotation is an arb-scan duty)
```

---

## dotace-scan pass — 2026-09-18

Monthly broad pass of the `dotace-scan` feed (`data/feeds.json` key `dotace-scan`,
`signal_source: dotace`, `evidence_type: tenders`, `id_prefixes: ["dotace"]`), run under
`pipeline/SCANS.md`, in parallel with the demand-, reg- and arb-scan passes.
Raw captures: `data/raw/2026-09-18/dotace/` (gitignored, pruned at 28 days).
Staged: `data/raw/2026-09-18/dotace/staged.jsonl`. No commit, no `db.py`, no edits to
`data/feeds.json`, `data/problems/**` or other ledgers.

### Registry changes needed

**None.** Every id uses the `dotace-` prefix this feed's row claims and every record
carries `source: dotace`, which `SignalSchema.source` already accepts.

### Ledger file name

The coordinator offered `data/signals/tenders/2026-09-18-dotace.jsonl`. **Not used, because
the convention forbids a suffix in practice:** `SPEC.md` §3 and `data/CONVENTIONS.md` fix the
ledger as `<type>/<run-date>.jsonl`, and `scripts/db.py` reads the run date off the filename
with `(\d{4}-\d{2}-\d{2})\.jsonl$` — a `-dotace` suffix would match nothing, so the feed's
freshness would silently stop advancing. Records land in `data/signals/tenders/2026-09-18.jsonl`;
the file did not exist when this pass started or when it wrote, and no other pass writes
`tenders` today (demand, regulation and funded are the other three scans' ledgers).

### Exchange rate

Czech allocations convert at **24.340 CZK/EUR**, the ČNB daily rate of 18.09.2026 (list #181),
fetched this pass from
`https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=18.09.2026`
(HTTP 200, saved as `cnb-denni_kurz-2026-09-18.txt`). The 2026-09-03 pass used 24.215 from
opd3.opd.cz; the central bank's own fixing is the better receipt and is used from here on.

### Checklist source 1 — MS2021+ open-data call list

`https://ms21opendata.mssf.cz/SeznamVyzev_21_27.xml` — **HTTP 200, 1,669,847 bytes, fetched
2026-09-18**, payload `DATE="2026-09-17T20:45:00.000+02:00"`, CC BY 4.0, MMR. Snapshot kept at
`data/raw/2026-09-18/dotace/ms21-SeznamVyzev_21_27.xml`.

**THE FIRST REAL ID DIFF.** Left-hand side: the 2026-09-03 snapshot
(`data/raw/2026-09-03/ms21-SeznamVyzev_21_27.xml`, 817 codes, also listed in
`manifest-dotace-scan.md` of that day). Right-hand side: 817 codes. **Added 0, removed 0.**
A code diff alone would therefore have reported a quiet fortnight — which is false. Every
announced call in this programme period is pre-registered in the XML as `Rozpracovaná` or
`Plánovaná` long before it opens, so **the diff that finds new calls is a STATE and DATE diff on
the existing codes**, not a code diff. This pass ran both and recommends the next pass does too
(the 817-code list from 2026-09-03 still stands as the code-level left-hand side; the snapshot
file itself is the state-level one, and it is pruned 28 days after 2026-09-03 — the next pass
must diff against THIS snapshot, dated 2026-09-18).

State/date changes between the two snapshots (38 codes), sorted by what they mean:

| KOD | change | outcome |
|---|---|---|
| `08_26_035` | Rozpracovaná → Vyhlášená, accessible 2026-09-14, opens 2026-10-20, closes 2026-11-09, 15 M CZK | minted `dotace-oprybarstvi-35-intenzivni-akvakultura` |
| `08_26_036` | same, 50 M CZK | minted `dotace-oprybarstvi-36-investice-akvakultura` |
| `08_26_037` | same, 10 M CZK | minted `dotace-oprybarstvi-37-zpracovani-produktu` |
| `08_26_038` | same, 2 M CZK | minted `dotace-oprybarstvi-38-propagacni-kampane` |
| `08_23_010` | Uzavřená → Otevřená, new 2026 round 2026-10-20 → 2026-11-09, 45 M CZK | minted `dotace-oprybarstvi-10-vysazovani-uhore-2026` |
| `14_26_021` | Plánovaná → Otevřená, opened 2026-09-14, closes 2026-11-27, 55 M CZK | minted `dotace-nshv-21-hranicni-kontrola-2` |
| `14_26_022` | Plánovaná → Otevřená, opened 2026-09-14, closes 2026-11-30, 10 M CZK | minted `dotace-nshv-22-biometrie-zastupitelske-urady` |
| `08_23_009` | Uzavřená → Otevřená, closes 2029-12-31, 20 M CZK | **not minted** — the only applicants are the Agriculture Ministry and its own allowance organisations: the programme owner's own promotion budget, the same reason Technická pomoc calls are never minted |
| `01_26_091` | Vyhlášená → Otevřená | already `dotace-optak-poradenstvi-3` (2026-09-03) |
| `06_26_119` | close 2026-09-10 → **2027-03-31**, allocation 365.0 → **651.0 M CZK** | **ledger now stale** — `dotace-irop-119-cyklodoprava` carries date 2026-09-10 |
| `06_26_121` / `06_26_122` | close 2026-09-30 → **2027-03-31**, allocations 787.5 → **1,370.1** and 827.8 → **1,598.9 M CZK** | **ledger now stale** — `dotace-irop-121-122-bezemisni-vozidla` carries date 2026-09-30 |
| `06_23_105` | close 2026-09-21 → **2026-11-20** | **ledger now stale** for the ČR leg of `dotace-irop-103-105-urgentni-prijmy` (103/104 still close 2026-09-21) |
| `05_26_109` | allocation 2.0 → **2.6 bn CZK** | **ledger now stale** — `dotace-opzp-109-protipovodnova-ochrana` money |
| `05_26_107` | allocation 162.5 → **125 M CZK**; still Rozpracovaná in the XML, accessible 2026-09-30, opens 2026-10-14 | minted from the opzp.cz call page (status Plánovaná, dated window) as `dotace-opzp-107-environmentalni-centra` — see OPŽP below |
| `06_24_116` | allocation 142.9 M → **1,242.2 M CZK**, closed 2026-08-31 | closed; not minted. Note for matching: IROP 116 *Sociální bydlení II* grew almost ninefold before it closed |
| `03_25_085`, `12_26_048`, `13_26_015` | Otevřená → Uzavřená | closed; nothing to mint |
| the other allocation-only moves (`03_23_050/051`, `03_24_059`, `05_25_092/093/099/100`, `06_22_011/016/020/030/037/050/062`, `06_23_090/094/102`) | allocation re-counts on long-running calls | no new call; not minted |
| `04_25_039`, `10_26_112` | opening date corrected (to 2025-09-10 and to 2026-10-14) | no new call |

The four "ledger now stale" rows are the ledger's append-only nature showing: the records are
true as of their run and wrong today. **Owed (coordinator):** an errata line or a successor
record for each; this pass did not write one because `data/errata.jsonl` is outside its remit,
and a second record for the same call under a new id would be a differently-worded duplicate.

**Carried forward, again not minted:** the three OPJAK `Plánovaná` calls `02_25_044`
*Vzdělávání pro praxi a život* (500 M CZK, opens 2026-11-23), `02_25_045` *Výzkumné
infrastruktury II* (1.9 bn CZK, opens 2026-12-10), `02_26_046` *Výzkumné e-infrastruktury II*
(600 M CZK, opens 2026-12-10) — unchanged in the XML since 2026-09-03; see the OPJAK portal
entry below for whether opjak.cz publishes them yet.

**Beyond the floor — the open-but-never-minted calls.** The XML lists **145 calls open on
2026-09-18** (Otevřená or Vyhlášená, closing on or after today). The ledger holds 54 CZ
`dotace-` records dated on or after today, and many of those are SFŽP, Modernizační fond, NPO,
NZÚ and TAČR calls that the XML does not carry — so well over half of the 145 have no record. Most of the rest are long-running continuous calls opened in 2022–2024 that
no pass ever minted, because every pass so far diffed for *new* openings only. This pass minted
the largest builder-relevant one, **`dotace-irop-78-79-ehealth`** (2.1 bn CZK, closes
2026-12-02). **Owed to a future pass (named so the omission is a decision):** IROP
`06_22_010` eGovernment + cyber (Prague, 725 M CZK, to 2026-12-31), `06_22_056/057` acute
psychiatric care (XML closes 2026-11-13; the IROP portal says 14 Jan 2027), `06_23_097/098` community psychiatric care (to 2026-12-17),
`06_23_106/107/108` public-transport charging stations (to 2026-12-15 / 2027-12-31),
`06_22_067` public-transport telematics (ITI, to 2027-12-31); OPD `04_25_038` ITS ve městech
(921.7 M CZK, to 2027-03-31); OP Z+ `03_24_062` social-health borderline services (273 M CZK,
to 2026-12-15), `03_24_059` *Politiky, které fungují* (to 2026-09-30), `03_22_012` diverse and
flexible work culture (360 M CZK, to 2026-11-30); OP ST `10_25_095` public-infrastructure
energy savings, Ústí region (400 M CZK, to 2026-12-09), `10_25_089` circular economy, Ústí
(to 2026-09-30), `10_26_110` university vouchers+, Moravian-Silesian region (100 M CZK, to
2026-11-30); OP AMIF `12_26_046` accommodation containers (100 M CZK, to 2026-09-23); OP NSHV
`14_26_018` security screening and escort vehicles (290 M CZK, to 2026-09-30), `14_26_019`
ETIAS appeal body (14 M CZK, to 2026-12-31). Three helper workers were briefed to enrich these
with support rates; the session's concurrent-agent cap refused them, so they are owed, not done.


### Checklist source 2 — the portals the feeds.json row names

All seven visited on 2026-09-18; every page HTTP 200. The Czech portal walk was run by one
helper worker under this pass's brief (captures in `data/raw/2026-09-18/dotace/pages/`, quotes
re-verified by this pass as literal substrings of those captures).

**IROP** — `https://irop.gov.cz/cs/vyzvy-2021-2027` plus its load-more feed
(`/Systemove-stranky/Ajax-pages/VyzvyAJAX2021New`, pages 2–18; page 12 is the last with new
items): 120 calls, 58 open, 62 closed. The Planned / Announced / Declared filters are empty.
Newest opening is still call 120 (30 Apr 2026). **Nothing opened after 2026-09-03; nothing
minted from the listing.** Open and in the ledger: 85, 103/104, 105, 117, 119, 120, 121/122.
Stale ledger records confirmed from the call pages: 119 (now 31 Mar 2027), 121/122 (now
31 Mar 2027), 105 (now 20 Nov 2026) — see the MS2021+ table. Open, pre-2025, never minted:
see "Beyond the floor" above, plus 95/96 school counselling, 31/32 follow-up health care,
58/59 deinstitutionalisation, 65 green infrastructure (Prague) and ~30 ITI/CLLD envelope calls.
Call 113 is technical assistance and is never minted. The one beyond-floor IROP record this
pass minted, `dotace-irop-78-79-ehealth`, was receipted from the call-79 text PDF on
irop.gov.cz.

**OPŽP** — `https://opzp.cz/nabidka-dotaci/` plus the POST API `/wp-json/opzp/v1/call/html`:
13 live calls and 1 planned. Live and in the ledger: 72, 73, 79, 101, 102, 103, 104, 105, 106,
108, 109 and SFŽP 2/2026 FN ČOV. **Minted: `dotace-opzp-107-environmentalni-centra`** — the
opzp.cz call page (status *Plánovaná*) publishes a dated window (14 Oct – 25 Nov 2026),
100 M CZK and the applicant list; the OPŽP call schedule of 10 Sep 2026 (v9 XLSX) gives max.
80 % and 125 M CZK total. **Caveat carried in the record:** MS2021+ still says
*Rozpracovaná* (accessible from 30 Sep 2026) and no call text exists yet; the next pass
confirms it was declared. `dotace-opzp-98` is no longer listed (closed 2026-08-28).

**OPJAK** — `https://opjak.cz/vyzvy/`: five substantive open calls, all in the ledger (Open
Science III, Poradím se s AI, Teaming-CZ III, Smart Akcelerátor+ II, MAP II); two technical-
assistance calls never minted. The announcements filter is empty and the site search finds
nothing for `02_25_044`, `02_25_045`, `02_26_046`; the call schedule is still v2 of
20 Feb 2026. **Nothing minted**; the three planned calls stay owed.
`dotace-opjak-msca-fellowships-cz` is no longer listed (closed 2026-08-31).

**SFŽP** — hub `https://sfzp.gov.cz/dotace-a-pujcky/`; Modernisation Fund list (7 current
calls: RES+ 6/2025, TRANSCom 1/2025 and 2/2025, TRANSGov 1/2024 II and 2/2025, KOMUNERG 1/2025,
ELEGRID 1/2025 — all in the ledger, nothing new); financial instruments list and call pages.
**Minted: `dotace-sfzp-1-2025-fn-odpady`** (owed by 2026-09-03: 930 M CZK, guarantee plus
grant, project intents to 6 Jan 2027) and **`dotace-sfzp-1-2026-nzu-fn-kompenzace`** (new,
published 16 Sep 2026: SFŽP compensates banks that lend zero-interest Nová zelená úsporám
renovation loans, cap 50 bn CZK of loan volume, 16 Sep 2026 – 31 Dec 2031). The owed "1/2024
FN" is HOUSEnerg 1/2024 FN and is now on the closed-calls list, so **`dotace-mf-housenerg-fn-pujcky`
(date 2026-12-31) is stale**; the NZÚ FN call is a different call, not a duplicate of it.

**NPO** — `https://planobnovy.gov.cz/vyhlasene-vyzvy/`: the same four calls as 2026-09-03, all
in the ledger (`dotace-npo-nrb-najemni-bydleni`, `-14-2025-secap-poradenstvi`,
`-16-2025-energeticke-seminare`, `-2-2026-renovacni-pas`); the call schedule XLSX is dated
16 Jun 2026. **Nothing new, nothing minted.**

**TAČR** — `https://tacr.gov.cz/` and `/programy-a-souteze/`. Open and in the ledger:
Water4All, THÉTA 2 (4th), RAMP, CET. **Minted:** `dotace-tacr-sigma-18vs-dc1-komercializace`
(the owed SIGMA 18th competition DC1, announced 9 Sep 2026: 10 M CZK, 70 %, small firms only,
10 Sep – 27 Oct 2026), `dotace-tacr-forest-call-2026` (new, opened 15 Sep 2026: 500,000 EUR
Czech envelope, 80 %, to 2 Dec 2026) and `dotace-tacr-biodiversa-call-2026` (new, opened
9 Sep 2026: 1,000,000 EUR, 80 %, to 10 Nov 2026, the partnership's last call). **Stale:**
`dotace-tacr-dut-call-2026` carries date 2026-09-01 (the opening) and `money_eur: 0`; the page now
shows 1 Sep – 17 Nov 2026 and a 600,000 EUR Czech envelope. BETA3 is a procurement
programme for state bodies, not a call — not minted.


**CINEA / HaDEA** — `https://cinea.ec.europa.eu/funding-opportunities/calls-proposals_en`
(pages 0–3 read, `?page=1..3`, all HTTP 200; 29 calls) and
`https://hadea.ec.europa.eu/calls-proposals_en` (HTTP 200; 5 calls). **Nothing opened after
2026-09-03 on either agency.** Newest CINEA opening 2026-08-04; newest HaDEA opening
2026-06-23. The owed items from 2026-09-03, one by one:

- **CINEA "EUR 131.5 million available for Horizon Europe energy call"** (HORIZON-CL5-2026-11,
  opened 2026-08-04, deadline 2026-12-01) — the budget is on the call's own page, so it is
  **minted: `dotace-horizon-cl5-2026-11-energy`**. The per-topic funding rate and eligibility
  sit in the Funding & Tenders topic conditions and were not read; the record says so.
- **SMP Food — food-waste prevention** (HaDEA, opened 2026-06-16, deadline 2026-10-15) — the
  call page states "Total budget: € 4 000 000", so it is **minted:
  `dotace-smp-food-2026-food-waste-prevention`**. Funding rate not on the page; owed.
- **LIFE-2026-CET-ENERCOM / -ENERPOV and the whole LIFE-2026-CET family** — resolved via the
  F&T topic JSON (`ec.europa.eu/info/funding-tenders/opportunities/data/topicDetails/life-2026-cet-enercom.json`,
  HTTP 200): 13 topics, budgets 3.0–10.0 M EUR each (ENERCOM 7.0 M, ENERPOV 6.0 M), **all
  closed 2026-09-16** (status `Closed`). Not minted — the deadline passed before this pass. The
  previous pass's deferral cost these records: they were live on 2026-09-03.
- **CEF-DIG-2026-CABLE-REPAIR-CAPACITIES** (emergency submarine-cable repair modules, opened
  2026-06-23, deadline 2026-10-08) — the topic-details JSON under that id answers **404**, and
  the F&T search API returns only FAQ entries for it (one FAQ names a sibling id
  `…-CABLE-REPAIR-CAPACITIES-PILOT`). No budget receipted, so **not minted**; still owed, and of
  low relevance to a landlocked register.
- **The LIFE-2026 SAP / TA / PLP calls** on the CINEA listing close **2026-09-22** — four days
  out; their budgets are not on the listing pages and were not resolved. Named, not minted.
- `HORIZON-CID-2026-01`, `HORIZON-MISS-2026-02-CANCER`, `HORIZON-CL4-2026-03 (SPACE)` — not
  resolved this pass; still owed (F&T topic JSON is the working route, measured above).

Note for the next pass: `ec.europa.eu` fails TLS verification through the sandbox proxy
(curl exit 60); the F&T JSON fetches ran outside the sandbox. cinea/hadea hosts work inside it.


### Records — 16, in `data/signals/tenders/2026-09-18.jsonl`

Every record: `source: dotace`, `extraction: manual`, `http_status: 200`, a `fetched_at`, and a
`notes` field giving allocation, support rate, eligible applicants and the dated window, each
with the page it came from (where a rate is not published on anything this pass read, the
record says so rather than guessing: HORIZON-CL5-2026-11, SMP food, and the applicant-level
rate of IROP 78/79).

| id | sector | money EUR | closes | scale/money/urgency/recurrence | how found |
|---|---|---|---|---|---|
| `dotace-oprybarstvi-35-intenzivni-akvakultura` | other | 616,270 | 2026-11-09 | 1/2/3/2 | MS2021+ state diff |
| `dotace-oprybarstvi-36-investice-akvakultura` | other | 2,054,232 | 2026-11-09 | 1/3/3/2 | MS2021+ state diff |
| `dotace-oprybarstvi-37-zpracovani-produktu` | other | 410,846 | 2026-11-09 | 1/2/3/2 | MS2021+ state diff |
| `dotace-oprybarstvi-38-propagacni-kampane` | other | 82,169 | 2026-11-09 | 1/1/3/2 | MS2021+ state diff |
| `dotace-oprybarstvi-10-vysazovani-uhore-2026` | environment | 1,848,809 | 2026-11-09 | 1/2/3/2 | MS2021+ state diff |
| `dotace-nshv-21-hranicni-kontrola-2` | govtech | 2,259,655 | 2026-11-27 | 0/3/3/1 | MS2021+ state diff |
| `dotace-nshv-22-biometrie-zastupitelske-urady` | govtech | 410,846 | 2026-11-30 | 0/2/3/1 | MS2021+ state diff |
| `dotace-horizon-cl5-2026-11-energy` | energy | 131,500,000 | 2026-12-01 | 2/3/3/2 | CINEA (owed) |
| `dotace-smp-food-2026-food-waste-prevention` | environment | 4,000,000 | 2026-10-15 | 2/3/3/1 | HaDEA (owed) |
| `dotace-irop-78-79-ehealth` | health | 86,566,931 | 2026-12-02 | 2/3/3/1 | MS2021+ open-call walk |
| `dotace-tacr-sigma-18vs-dc1-komercializace` | b2b | 410,846 | 2026-10-27 | 1/2/3/2 | TAČR (owed) |
| `dotace-tacr-forest-call-2026` | environment | 500,000 | 2026-12-02 | 1/2/3/1 | TAČR (new) |
| `dotace-tacr-biodiversa-call-2026` | environment | 1,000,000 | 2026-11-10 | 1/2/3/0 | TAČR (new) |
| `dotace-opzp-107-environmentalni-centra` | education | 4,108,463 | 2026-11-25 | 1/3/3/1 | OPŽP call page (planned) |
| `dotace-sfzp-1-2025-fn-odpady` | environment | 38,208,710 | 2027-01-06 | 2/3/3/1 | SFŽP (owed) |
| `dotace-sfzp-1-2026-nzu-fn-kompenzace` | housing | 2,054,231,717 | 2031-12-31 | 2/3/1/2 | SFŽP (new) |


**Money method.** No estimates. CZK allocations convert at 24.340 (ČNB, 18 Sep 2026); EUR
calls carry the agency's own figure. Two money values are not grant budgets and say so in
`money_note`: `dotace-sfzp-1-2026-nzu-fn-kompenzace` is a 50 bn CZK cap on subsidised LOAN
volume (the compensation outlay is unpublished), and `dotace-sfzp-1-2025-fn-odpady` is the
930 M CZK guarantee-plus-grant instrument — the same convention the ledger already uses for
`dotace-sfzp-2-2026-fn-cov`.

**Quote verification.** Every `quote` was checked programmatically as a literal substring of a
whitespace-collapsed capture saved under `data/raw/2026-09-18/dotace/`: 5 from the MS2021+ XML,
3 from pdftotext extractions of call PDFs (mv.gov.cz ×2, irop.gov.cz), 8 from HTML pages
(cinea, hadea, tacr ×3, opzp, sfzp ×2 — one also matches its call PDF). All ≤300 characters.

**Dedup.** None of the 16 ids was in `data/signals/seen.txt` or any ledger before writing.
`normalize.py --complete` (identity-key dedup) was run against a scratch copy of
`data/signals/` and a scratch `seen.txt`: 16 appended, 0 skipped, 0 materiality drops,
0 incomplete, 0 AC-GDPR1 refusals (only `evidence_type`, the routing key, stripped). The ledger
file is that run's output, byte for byte. A Python mirror of `SignalSchema` (strict keys, id
regex, url, ISO date/timestamp, score ranges, money-score-vs-rubric) passed on all 16 lines,
and the file has zero email or phone-number matches. **`db.py upsert` was NOT run** — the
coordinator keeps the shared DB; the line to run is
`python3 scripts/db.py upsert data/signals/tenders/2026-09-18.jsonl`.

**`seen.txt`.** The 16 ids were appended once, at the end of the pass, with `>>`, after
re-reading the file to drop any id another agent had already added (none had). Because the
parallel passes append rather than rewrite, `seen.txt` is no longer sorted after today; the
coordinator's completion owes it one sort.

### Coverage gaps (named, not silent)

1. **The four stale IROP/OPŽP ledger records plus `dotace-mf-housenerg-fn-pujcky` and
   `dotace-tacr-dut-call-2026`** carry deadlines or money that the publisher has since changed
   (tables above). Owed: an errata decision by the coordinator; this pass does not write
   `data/errata.jsonl`.
2. **The never-minted open-call backlog** (about 20 builder-relevant MS2021+ calls named under
   "Beyond the floor", plus ~30 IROP ITI/CLLD envelope calls). Three helper workers briefed to
   receipt their support rates were refused by the session's concurrent-agent cap; owed to the
   next pass or a SWEEP.
3. **EU per-topic conditions not read**: funding rates for HORIZON-CL5-2026-11 and the SMP
   food call; the CEF-DIG cable-repair budget (topic JSON 404); HORIZON-CID-2026-01,
   HORIZON-MISS-2026-02-CANCER, HORIZON-CL4-2026-03 (SPACE); the LIFE-2026 SAP/TA/PLP family
   (closes 2026-09-22). `ec.europa.eu` needs fetches outside the sandbox (TLS through the proxy
   fails).
4. **LIFE-2026-CET closed 2026-09-16 before this pass** — ENERCOM (7.0 M EUR) and ENERPOV
   (6.0 M EUR) were owed on 2026-09-03 and are now lost to the ledger as live calls.
5. **OPŽP 107 minted from a *Plánovaná* page** — the next pass confirms it was declared on or
   after 2026-09-30 and reads the call text; OPJAK 044/045/046 stay owed until opjak.cz
   publishes them.
6. **`08_23_009` (OP Rybářství promotion, MZe-only) deliberately not minted** — the programme
   owner's own budget.

### Pass summary (5 lines)

```
feed:              dotace-scan (monthly broad pass, 2026-09-18)
checklist sources: 8 of 8 visited — MS2021+ XML + IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO, CINEA/HaDEA
records:           16 written to data/signals/tenders/2026-09-18.jsonl (7 MS2021+ state-diff hits,
                   1 MS2021+ open-call walk, 8 portal catches: 5 owed-by-last-pass, 3 new); 0 dropped
coverage gaps:     6 named — stale ledger records; open-call backlog; EU topic conditions;
                   LIFE-CET lost to closure; OPŽP 107 not yet declared; 08_23_009 by decision
rotation state:    n/a — category rotation is arb-scan's duty
```

---

## arb-scan pass — 2026-09-18

Monthly BROAD pass (pipeline/SCANS.md), evidence_type `funded`, source `arb-scan`,
id prefix = ISO2 of the origin country. Run in parallel with three other scan feeds and
several record-rewrite agents, so this pass wrote ONLY: `data/signals/funded/2026-09-18.jsonl`,
this manifest, raw captures under `data/raw/2026-09-18/funded/`, and one final append to
`data/signals/seen.txt`. No commit, no build, no `db.py upsert` (the shared DB was not written —
see "Hand-off" below).

### How the pass ran

Four category agents in parallel (legal-compliance + retail-services, energy + fintech,
health + b2b, education + govtech), one shared brief (evidence bar, id-prefix allowlist, dedup,
Czech absence check with a positive control, established/early per the CONVENTIONS test), plus
the coordinator's own discovery walk of the funding news listings (below) and two feed picks.
Every staged line was re-validated by the coordinator: a strict re-implementation of
`SignalSchema` (web/lib/data.ts), the arb-scan prefix allowlist from `data/feeds.json`, money-score
arithmetic, the materiality filter, the GDPR email/phone screen, and a re-check that every `quote`
is a literal substring of the saved raw page. Then `normalize.py --complete --dry-run` against the
real ledgers and `seen.txt` for both dedup axes.

### Discovery listings (the pass's source walk)

| listing | result 2026-09-18 | what it gave |
|---|---|---|
| `eu-startups.com/category/funding/` | **HTTP 403** (same as 2026-09-03) | nothing — coverage gap |
| `eu-startups.com/feed/` (RSS) | 200, 10 items, 2026-09-18 only | 3 funding items read |
| `eu-startups.com/category/funding/feed/?paged=N` | **HTTP 404** on every page | nothing — no paging |
| EU-Startups weekly round-up 2026-09-14…18 | 200 but **CLUB-members paywall** — body not served | nothing — coverage gap; the 2026-09-10, 09-04, 08-28 round-ups are the same product |
| `tech.eu/category/funding/` | **HTTP 404** (same as 2026-09-03) | nothing |
| `tech.eu/feed/` (RSS) | 200, 20 items, 2026-09-16…18 (`?paged=` returns the same page) | syte, Integral, Arcos, Logibot, Magentic read as candidates |
| `vestbee.com/insights/articles` | **HTTP 404** (same as 2026-09-03) | nothing |
| `sifted.eu/feed` | 200, 24 items, 2026-09-15…18 | editorial, few rounds with a Czech transfer |

The RSS windows are three days deep, so the listings are a thin discovery surface: most
candidates came from category-targeted web search by the agents. **This remains the pass's most
likely source of misses** — a month of European rounds exists in the paywalled round-ups and the
404ing category archives, and none of it could be walked mechanically.

### The checklist source for this feed: THE CATEGORY-ROTATION DUTY

All 12 categories are named below, as the checklist law requires. **Rotation state at the
start of this pass was read from the 2026-09-03 manifest and re-derived from the ledger** (every
`source: arb-scan` record in `data/signals/funded/*.jsonl`, grouped by sector and run date). The
2026-09-03 health records and the 2026-09-04 environment records came from topic SWEEPS
(hospital drug procurement, wastewater); per SCANS.md a sweep never advances the rotation, so
health and environment keep their broad-pass dates. The six categories the 2026-09-03 manifest
said the next pass owes — legal-compliance, retail-services, energy, fintech, health, b2b — were
all swept here, plus education and govtech for the two debts that manifest carried.

| category | last BROAD sweep before | arb records before | covered this pass | records added | last swept AFTER |
|---|---|---|---|---|---|
| legal-compliance | 2026-08-14 | 9 | **YES** (owed) | 2 | 2026-09-18 |
| retail-services | 2026-08-14 | 14 | **YES** (owed) | 2 | 2026-09-18 |
| energy | 2026-08-14 | 16 | **YES** (owed) | 2 | 2026-09-18 |
| fintech | 2026-08-14 | 19 | **YES** (owed) | 2 | 2026-09-18 |
| health | 2026-08-14 | 27 | **YES** (owed) | 2 | 2026-09-18 |
| b2b | 2026-08-14 | 62 | **YES** (owed) | 3 | 2026-09-18 |
| education | 2026-09-03 | 8 | **YES** (carried debt: "owes a second candidate") | 1 | 2026-09-18 |
| govtech | 2026-09-03 | 4 | **YES** (thinnest category) | 2 | 2026-09-18 |
| housing | 2026-09-03 | 10 | touched only — one feed pick (de-syte), no category search | 1 | 2026-09-03 (unchanged) |
| other | 2026-09-03 | 5 | no | 0 | 2026-09-03 |
| mobility | 2026-09-03 | 8 | no | 0 | 2026-09-03 |
| environment | 2026-09-03 | 16 | no | 0 | 2026-09-03 |

**The next pass starts at `other`, then `mobility`, `housing`, `environment`** — the four still
at 2026-09-03, in ascending depth (5, 8, 11, 16 arb records). Every category now has a broad
sweep dated 2026-09-03 or later.

### Records — 17 appended to `data/signals/funded/2026-09-18.jsonl`

CZ verdict vocabulary: **absent** = no Czech player selling this found, with queries and a passed
positive control; **contested** = direct Czech players exist but all EARLY; **taken** = a direct,
ESTABLISHED Czech player. Maturity abroad per the CONVENTIONS established test, each limb sourced
in the record's `notes`.

| id | what | money | abroad | CZ verdict |
|---|---|---|---|---|
| `fr-tremau` | Digital Services Act compliance and moderation software for online platforms | EUR 3M (2025-04) | established | **absent** (elv.ai, SK, adjacent/early). Urgency 2: the Czech DSA adaptation act naming ČTÚ as coordinator (sněmovní tisk 69) passed second reading 2026-07-01 — page saved as `legal-compliance/support-psp-tisk69.html` |
| `at-prewave` | AI supplier-risk monitoring and LkSG/CSDDD due diligence | EUR 63M Series B (2024-06) | established | contested — dReport direct, maturity unproven (no ARES match, site unreachable); D&B is foreign. Urgency 1 (CSDDD moved to 2028-07-26 by Directive 2025/794) |
| `fr-veesion` | AI shoplifting-gesture detection on existing store CCTV | EUR 38M Series B (2025-05) | established | taken — M2C / Mark2 Corporation Czech a.s. (IČO 25719751, since 1998) |
| `de-foodforecast` | AI intra-day production/ordering forecasts for bakeries and fresh retail | EUR 8M Series A (2026-02) | established | taken for chain forecasting — Logio s.r.o. (IČO 27161871); no Czech intra-day bakery planner found |
| `nl-gradyent` | digital twin optimising district-heating networks | EUR 28M Series B (2025-04) | established | taken — ORTEP s.r.o. (IČO 60491680, DYMOS), Feramat Energies (IČO 27619371) |
| `ee-fusebox` | white-label virtual-power-plant software for aggregators | EUR 2.6M (2025-01) | early | contested — Czech aggregators sell the service (Nano Energies, ČEZ ESCO, Delta Green, Powertica); none found selling the software; aggregator role opened 2026-08-01 |
| `fr-algoan` | open-banking credit scoring / affordability checks for lenders and BNPL | none published | established | **absent** (Finbricks IČO 10669205 adjacent — raw account data only). Urgency 3: CCD2 applies 2026-11-20 |
| `gb-sprout-ai` | AI claims-document checking for insurers | GBP 5.4M ≈ EUR 6.21M (2023-10) | established | taken — The MAMA AI (IČO 09767223, Kooperativa), BigHub (IČO 05388066, Direct, UNIQA) |
| `at-flinn` | AI for medical-device regulatory and quality work (MDR) | EUR 17M Series A (2026-02) | early (founding year 2022 vs 2023 by source) | contested — QMS software and consultancies (EffiChem, Aptien, Regulatory House, 4Med) cover parts; no MDR automation product. Urgency 2: legacy-device MDR deadline 2027-12-31 (Reg. 2023/607) |
| `nl-luscii` | remote patient monitoring for hospitals and GPs, bought by OMRON | undisclosed (2024-04) | established | contested — in-house projects at FN Ostrava / FN Olomouc, a VZP pilot since July 2026, Medical Data Transfer (maturity unknown) |
| `de-plancraft` | office software for small trade businesses (quotes, time, site records, invoicing) | EUR 38M Series B (2025-08) | established, 20,000+ customers | contested — Timoty, DoneBy, Remesel, Bidmio, none shown established |
| `us-maintainx` | mobile CMMS for industrial maintenance teams | USD 150M Series D ≈ EUR 128M (2025-07) | established | taken — TESCO SW, Act-in, POSYS, Q-LanYs, PROFYLAX, Aptien. Comparison point only |
| `de-integral` | AI-native accounting/tax/payroll firm for SMEs (agents do, licensed staff sign) | EUR 18M Series A (2026-09-16) | early (founded 2024) | taken — Trivi a.s. and Účtárna.ai, direct/established on p-0023; Adconta, UcetniAi.cz, E-Consulting early. Fresh comp for **p-0023** |
| `us-parallel-learning` | remote special-education assessments and therapy sold to schools | USD 20M Series B ≈ EUR 17.2M (2025-12) | established | **absent** (Vyslovuj, Medevio, Hedepy, Terap.io adjacent/early) |
| `gb-beam-up` | Magic Notes — AI case-note drafting for council social workers | none published for the cited event | established (Kent, Swindon, Angus councils) | **absent** (IRESOFT/CYGNUS, NEWTON Technologies, Česky.AI, OKsystem adjacent) |
| `de-polyteia` | data platform and dashboards for public administrations | EUR 5M (2023-03) | established | taken — Golemio / Operátor ICT (IČO 02795281) |
| `de-syte` | AI buildability and viability analysis per parcel for developers and banks | EUR 9M Series A (2026-09-17) | established, 200+ customers | contested — devcheck, Pozemkov (Daturing s.r.o., IČO 22203770, since 2024-10-29), JEDNOTKA.PRO, AIkatastr all early; CleverMaps a.s. adjacent |

Verdicts: absent 4 · contested 6 · taken 7. All 17 carry a verbatim `quote` read off the saved
page at `data/raw/2026-09-18/funded/<category>/<id>.html` (coordinator re-check: 17/17 literal
substrings), `http_status` 200 and `fetched_at`. None dropped by materiality; no id collided
with `seen.txt`; identity-key dedup against the live ledgers: 0 skipped.

**Older than the 2024 preference, kept on purpose:** `gb-sprout-ai` (2023-10-31) and
`de-polyteia` (2023-03-01) — the model and traction are proven and the Czech check is current.

### New-problem candidates for MATCH (no Czech equivalent found)

1. `gb-beam-up` — AI documentation for municipal social work and child protection (OSPOD at 205
   extended-power municipalities, zákon 359/1999 and 108/2006). Nearest register record is
   p-0036 (hospital clinical documentation), but the buyer is municipal, not a hospital.
2. `us-parallel-learning` — outsourced remote capacity for special-needs assessments; counselling
   centres run months-long waiting lists while MŠMT has funded school psychologist and special
   educator posts from the state budget since 2025-01-01.
3. `fr-algoan` — affordability checks for BNPL and small non-bank loans under CCD2 (applies
   2026-11-20); the register already holds `reg-ccd2-consumer-credit` and `reg-ccd2-bnpl-2026`.
4. `fr-tremau` — DSA compliance tooling for Czech platforms as ČTÚ gains enforcement powers.

Contested-early and worth a look: `at-flinn` (MDR automation for Czech device makers, dated
urgency), `nl-luscii` (remote monitoring, VZP pilot live). Comps for existing records:
`de-integral` → p-0023; `de-syte` sits upstream of p-0003.

### Candidates screened and NOT staged — stated, not silent

- **Already held (not re-minted):** e-invoicing (`round-a-cube`, `round-ddd-invoices`,
  `yc-invopop`); MDR second example `round-certhub` (cited inside `at-flinn`); `round-hedepy`,
  `round-delta-green`, `yc-sagecare` cited inside notes as corpus context. `yc-beam` is a
  different company from Beam Up Ltd.
- **Czech presence found, no record:** Knowunity (operates in Czech itself — knowunity.cz, Czech
  App Store listing; this **clears the 2026-09-03 education debt** as "present", not a gap); Little
  Bird (kindergarten allocation — taken by zapisdoskol.cz, Zápisy Online, city portals; unfunded);
  Schüttflix (own Czech subsidiary since 2022, IČO 14205408; Metrák competes); Munch (merged with
  the Czech app Nesnězeno); Thirdfort (Czech estate-agent AML tools exist: AutoDetect, AML PROOF,
  AML Basic, eAML); Tante Enso (unstaffed village shops exist: Contio, COOP 24/7); Waat (apartment
  EV charging taken: PRE, Chytré nabíjení, Elmobi).
- **No transfer / below bar:** envelio (2019 round, owned by E.ON, three Czech DSO buyers);
  packaging-fee compliance for e-shops (key requirement proposed for suspension to 2035, no funded
  startup); green-claims tooling (already p-0028 territory); Arcos (DE, EUR 5.5M 2026-09-18,
  24/7 infrastructure monitoring — screened from the feed, NOT absence-checked, so no claim either
  way).
- **Rejected in error — owed to the next pass:** Klinik (Finnish AI GP triage, CE-marked) was
  dropped by the health agent as "prefix `fi` not allowed", but **`fi` IS claimed by arb-scan** in
  `data/feeds.json`. No funding figure was found in the coordinator's follow-up search. The next
  health pass owes Klinik a proper record and a check against Medevio (IČO 09675400).

### Coverage gaps

1. **Listing walks** — see the discovery table: EU-Startups category archive 403 and weekly
   round-ups paywalled; tech.eu category 404; Vestbee 404; the RSS feeds reach back only three
   days. The pass is most likely to have missed rounds from 2026-08-15 to 2026-09-15.
2. **Publisher fetch failures:** citybiz.co 403 (Parallel Learning sourced from pulse2.com
   instead); digitalhealth.net 403 (not needed); a vzp.cz news URL 404 (cnews.cz cited instead);
   dreport.cz no response (dReport maturity unproven); finbricks.com unreachable from the sandbox;
   data-api.ecb.europa.eu blocked (FX rates from api.frankfurter.dev, which republishes ECB
   reference rates); Prewave's release body is JavaScript-rendered, so its quote comes from the
   page title/description markup.
3. **Surfaces searched:** `google-cz` (Czech-language queries through the session web-search tool),
   `ares` (live REST name and IČO lookups) and `own-funded-ledger` on every record. `app-stores`,
   `cz-saas-directories`, `startupjobs` and `eshop-addon-marketplaces` were **not** searched; no
   note claims them.
4. **Maturity limbs not verified:** several Czech players are marked established "by years
   only" in notes (CleverMaps, IRESOFT, NEWTON Technologies, Medevio) — the second limb was not
   checked. Those rows are adjacent and move nothing; they are recorded so MATCH does not read
   them as verified.
5. **`seen.txt` is appended, not re-sorted.** The coordinator's parallel-safety rule forbids
   rewriting the shared file, so the 17 ids were appended in one `>>` at the end. The next
   `normalize.py --complete` rewrites it sorted.

### Positive control — passed, with recorded misses

Run by every agent before any absence was written. ARES returned **Wultra s.r.o., IČO 03643174,
since 2014-12-15** in all five runs. Czech-language web search surfaced Wultra (4 of 5 runs;
Lupa.cz, CzechCrunch) and Ringil (3 of 4 runs where tried). **Recorded misses:** SOFTLINK did not
surface on descriptive energy-management queries (two agents), the education agent's Ringil query
returned other Czech TMS vendors (TruckManager, TruckAgenda) but not Ringil, and the fintech
agent's descriptive Wultra query missed Wultra by name while surfacing other Czech vendors. The
method produces positives, but the misses say descriptive queries do not reliably surface a
named firm — the four absence verdicts rest on queries plus ARES, not on a clean sweep.

### Hand-off

- Staged: `data/raw/2026-09-18/funded/staged.jsonl` (17 lines).
- `python3 scripts/normalize.py --raw data/raw/2026-09-18/funded --complete --dry-run --today
  2026-09-18` against the live ledgers and `seen.txt`: would append 17, 0 materiality drops,
  0 incomplete, 0 identity-key skips, 0 AC-GDPR1 refusals.
- The real `--complete` ran with `--out-dir` and `--seen` pointed at scratch copies (so the
  shared `seen.txt` was not rewritten); its output file was copied verbatim to
  `data/signals/funded/2026-09-18.jsonl`. `python3 scripts/db.py prefixes` (read-only): AC-F3 OK,
  every prefix claimed.
- **Not run, on purpose:** `python3 scripts/db.py upsert data/signals/funded/2026-09-18.jsonl`
  (writes the shared `data/register.db`). The coordinator runs it, or the next build rebuilds it.
- No commit, no build.

### Pass summary

1. Feed: **arb-scan** (evidence_type `funded`, monthly broad pass, attended, run 2026-09-18).
2. Checklist sources: **12 of 12 categories named**; 8 swept (the 6 owed + education, govtech),
   1 touched (housing), 3 deferred with reason (other, mobility, environment); 8 discovery listings
   visited, 5 blocked or paywalled.
3. Records: **17** appended to `data/signals/funded/2026-09-18.jsonl` — b2b 3, legal-compliance 2,
   retail-services 2, energy 2, fintech 2, health 2, govtech 2, education 1, housing 1.
4. Coverage gaps named: **5** (listing walks, publisher fetch failures, unsearched surfaces,
   unverified second limbs, unsorted `seen.txt` append) + Klinik owed after a prefix misread.
5. Rotation: legal-compliance · retail-services · energy · fintech · health · b2b · education ·
   govtech → **2026-09-18**; other · mobility · housing · environment → **2026-09-03**, and the next
   pass starts there in that order.
