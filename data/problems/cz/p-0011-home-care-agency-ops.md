---
id: p-0011
region: cz
title: Czech home-care agencies burn scarce nurse time on phone-and-paper intake, scheduling
  and coordination
fix: 'Czech-speaking voice intake for home-care agencies — the calls that book, move and
  confirm visits answered automatically, on top of the scheduling system the agency
  already runs.'
category: health
geo: CZ-national
score: 6
scores:
  proof: 2
  money: 1
  urgency: 1
  demand: 2
  gap: 0
status: watching
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Czech-language intake and scheduling automation that coexists with Cygnus
    DP is real integration work for a dev plus care-domain pair, and small agencies
    buy on demonstrated capacity gains after a pilot, not self-serve.'
comps:
- name: Sage Care
  url: https://www.sagecare.ai/
  geo: US
  since: 2024
  traction: 'YC S24; AI intake/CRM for home-care agencies; claims 100+ min saved
    per intake (company site, 2026)'
  signal: yc-sagecare
- name: TakeCareOS
  url: https://www.ycombinator.com/companies/takecareos
  geo: US
  since: 2026
  traction: 'YC Spring 2026; 6 agencies with 200+ employees running ops on it (YC
    launch post, 2026)'
  signal: yc-takecareos
- name: Birdie
  url: https://www.birdie.care/
  geo: GB
  since: 2017
  traction: '$30M Series B led by Sofina (Sifted, 2022); $52M total; 700+ care providers'
- name: AlayaCare
  url: https://alayacare.com/
  geo: CA
  since: 2014
  traction: 'CAD $225M Series D (Businesswire, 2021); ~$274M total raised; 500+ care
    organizations'
  markets: [US, AU]
locals:
- name: IRESOFT (Cygnus DP)
  url: https://iresoft.cz/
  ico: '26297850'
  since: 2002
  competes: adjacent
  maturity: established
  evidence: 'Cygnus DP is the documentation and billing record system Czech home-care agencies
    already run: it is where the care that happened gets written down and invoiced. It is not
    the intake and coordination layer — it does not answer the phone, book or move a visit, or
    rebuild a day when a client cancels — so it is the seat an entrant would sit beside or
    integrate with; IRESOFT s.r.o. has traded since 2002, and the state contracts register
    shows 2 public buyers paying it, Domov pro seniory Horní Stropnice and Domov sociální péče
    Tmavý Důl.'
- name: e-Sestřička
  url: https://www.e-sestricka.cz/
  ico: '05752779'
  since: 2017
  competes: direct
  maturity: established
  evidence: 'A cloud system for home and palliative care covering the nursing billing codes 925,
    720 and 926, used by Sestřička, Most k Domovu and AHC. SESTŘIČKA.CZ s.r.o. has traded since
    2017.'
- name: pecovatelska.cz (Petr Zajíc software)
  url: https://pecovatelska.cz/
  since: 1998
  competes: direct
  maturity: established
  evidence: 'An information system for community social-care services under the social services
    act (zák. 108/2006 Sb.), deployed at more than 200 sites across Czechia and sold as a
    one-off licence rather than a subscription; it has been trading since 1998.'
- name: VeruApp
  url: https://veruapp.cz/
  since: 2023
  competes: direct
  maturity: early
  evidence: 'Builds each caregiver''s chronological daily plan automatically from the client''s
    digital record, with a field app for logging delivered tasks, re-planning around sudden
    events, client billing and statutory reporting. The site dates itself to 2023 and names no
    agency using it.'
- name: E-péče
  url: https://www.epece.cz/
  since: 2024
  competes: adjacent
  maturity: early
  evidence: 'A publicly funded Ústecký-kraj project, co-financed from the EU just-transition
    programme, putting a field mobile app into 39 care providers including Město Bílina, Město
    Kadaň and Diecézní charita Litoměřice. It is a grant project rather than a vendor — there
    is nothing an agency outside the region can buy — and it started only in 2024.'
sources:
- type: arbitrage
  name: "Sage Care"
  gist: "the closest US template"
  why: "AI intake and client records for US home-care agencies (YC S24), claiming over 100 minutes saved per intake — exactly the operations layer this record is about."
  url: https://www.ycombinator.com/companies/sagecare
  note: 'yc-sagecare: Sage Care (YC S24) automates home-care agency operations with AI — intake,
    communication, scheduling busywork; Cova (S26, AI-native home care agency) shows the model
    being replicated. US-only, scored as one analog.'
  date: '2026-08-13'
  signal: yc-sagecare
- type: gap-check
  name: "First Czech market scan"
  gist: "the first market sweep"
  why: "An early sweep that returned only care providers and IRESOFT's Cygnus DP, and documented hundreds of agencies running on phone and paper under a chronic nurse shortage."
  url: https://www.ycombinator.com/companies/sagecare
  note: 'Absence check 2026-08-13: CZ searches return only care providers themselves and IRESOFT
    Cygnus DP (documentation/billing records, no AI ops automation). Demand point: signal
    documents hundreds of agentury domácí péče running on phone + paper + Cygnus DP under
    a chronic nurse shortage.'
  date: '2026-08-13'
- type: arbitrage
  name: "TakeCareOS"
  gist: "the third US entrant"
  why: "YC Spring 2026, with six agencies of 200+ employees running operations on it — a third US company on care operations inside two years."
  url: https://www.ycombinator.com/companies/takecareos
  note: 'yc-takecareos: TakeCareOS (YC Spring 2026) — AI-native operating system for long-term
    care providers; third US company on care-ops within two years. Still US-only: arbitrage
    stays 1.'
  date: '2026-08-13'
  signal: yc-takecareos
- type: gap-check
  name: "VeruApp and three Czech rivals"
  gist: "the four Czech incumbents"
  why: "VeruApp builds each caregiver's day automatically from the client's digital record; e-Sestřička, the pecovatelska.cz system (200+ deployments) and the publicly funded E-péče sell into the same agencies."
  url: https://veruapp.cz/
  note: 'Gap re-check 2026-08-20: OCCUPIED. The record claimed Cygnus DP was the only thing helping
    and that no Czech player automated agency operations; a Czech-language search of the operations
    layer returns domestic vendors immediately. VeruApp is a Czech multiplatform cloud application
    for terénní pečovatelské služby that builds each caregiver''s chronological daily work plan
    automatically from parameters in the client''s digital record, carries a field mobile app for
    logging delivered tasks, lets managers re-plan around sudden events and coordinate joint home
    visits, and runs client billing and statutory reporting off the same data — intake, scheduling
    and coordination, which is exactly the layer this record said was unbuilt. e-Sestřička sells a
    cloud system for domácí a paliativní péče covering odbornosti 925, 720 and 926, with Sestřička,
    Most k Domovu and AHC on its reference list; ARES resolves SESTŘIČKA.CZ s.r.o. (IČO 05752779,
    Praha, 2017) alongside a chain of regional SESTŘIČKA.CZ — DOMÁCÍ PÉČE s.r.o. entities. The
    information system at pecovatelska.cz, from Petr Zajíc software (trading since 1998), serves
    terénní sociální služby under zák. 108/2006 Sb. and is deployed in more than 200 locations
    across Czechia, sold one-time rather than as SaaS. E-péče adds a publicly funded fourth: an
    Ústecký-kraj project co-financed from OP Spravedlivá transformace, putting a field mobile app
    into 39 care providers including Město Bílina, Město Kadaň and Diecézní charita Litoměřice.
    POSITIVE CONTROL passed first — the same method surfaced Softlink CEM Smart and Ringil at the
    top of their queries, and ARES resolved IRESOFT s.r.o. (this record''s own named incumbent),
    SOFTLINK s.r.o. and Ringil s.r.o. by name. De-rank rule applied: gap 1 to 0 with incumbents
    named, score 4 to 3, status watching.'
  date: '2026-08-20'
  queries:
    - "software pro agentury domácí péče plánování směn pečovatelská služba"
    - "agentura domácí péče software plánování návštěv sester mobilní aplikace"
    - "Chytrá péče aplikace pro pečující rodiny česká sociální dávky"
  checked: [ares, google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: regulation
  name: "Social services amendment 92/2026 Sb."
  gist: "the law widening care tasks"
  why: "Since 1 July 2026 pečovatelské services may take on routine health-adjacent tasks — the agencies this record covers absorb more work per scarce nurse."
  url: https://e-sbirka.gov.cz/sb/2026/92
  note: 'reg-soc-sluzby-92-2026: zákon č. 92/2026 Sb., main provisions in force 1 Jul 2026 —
    care services may help with taking medication (without breaking skin integrity) and with
    stoma/urine-bag handling; ÚP branches gain a hardship clause for cross-border allowance
    cases. Widens the task set flowing through the same scarce staff and the same
    phone-and-paper coordination this record describes.'
  date: '2026-07-01'
  signal: reg-soc-sluzby-92-2026
- type: hiring
  name: "Labour Office — July 2026 nurse hiring wave"
  gist: "the 380-vacancy hiring month"
  why: "262 employers posted 380 new general-nurse vacancies in one month — the shortage this record's capacity argument rests on, now measured monthly by a state dataset."
  url: https://data.mpsv.cz/od/soubory/volna-mista-prirustek/
  note: 'mpsv-2026-07-health-care: 380 new general-nurse vacancies across 262 employers (651
    seats), annualised wage floor €10.8M, July 2026 — among the first records of the hiring
    ledger. Hiring evidence backs demand and money, never proof. Demand 1→2: the nurse
    shortage was previously documented only through the yc-sagecare signal note; it is now a
    recurring state-published measurement.'
  date: '2026-07-31'
  signal: mpsv-2026-07-health-care
  dims: [demand]
- type: contract
  name: "ÚZIS — KOMPAS home-care data layer (~€5.4M)"
  gist: "the €5.4M state data contract"
  why: "The state health-statistics institute signed a €5.4M partnership to build classification, recommended practices and cost models for home and community nursing care — public money entering exactly the data layer these agencies run on."
  url: https://smlouvy.gov.cz/smlouva/38765500
  note: 'hlidac-36430740: Ústav zdravotnických informací a statistiky signed a partnership
    agreement implementing the KOMPAS project — classification, recommended practices and
    cost models for home and community nursing care — worth ~€5.44M (registr smluv, 14 Jul
    2026). Money 0→1: a relevant public contract now funds the domain''s data foundations;
    held below 2 because it is state project money, not an open tender a builder can win
    or agency purchasing budget.'
  date: '2026-07-14'
  signal: hlidac-36430740
  dims: [money]
created: '2026-08-13'
updated: '2026-09-02'
---

Hundreds of Czech home-care agencies — agentury domácí péče and pečovatelské služby, from Včelka to charity providers — book, move and confirm visits by phone and paper [S1,S2]. Under a chronic nurse shortage, time on intake calls is clinical capacity lost [S1]. Czech vendors already sell that coordination layer [S4].

Why now: the Labour Office logged 380 new general-nurse vacancies across 262 employers in July 2026 alone [S6]. Since 1 July 2026, amendment 92/2026 Sb. lets care services take on routine health-adjacent tasks — medication, stoma and urine bags — adding work per scarce nurse [S5]. Three US care-operations firms were funded in two years: Sage Care (YC S24), Cova (S26), TakeCareOS (Spring 2026) [S1,S3].

Who pays: the agencies buy capacity, not savings — automated intake and coordination lets the same nurses carry more reimbursed care. The state's health-statistics institute (ÚZIS) signed ~€5.4M for KOMPAS — classification, recommended practices and cost models for home nursing care [S7].

Existing non-solutions: Cygnus DP (IRESOFT) records and bills care already given, but does not answer the phone or rebuild a cancelled day [S2]. The layer above it is taken [S4]. VeruApp plans each caregiver's day from the client's digital record; e-Sestřička covers home and palliative care on nursing billing codes 925, 720 and 926; pecovatelska.cz (Petr Zajíc software) runs community social-care services at 200+ sites; and Ústecký kraj is putting the E-péče field app into 39 providers on EU money [S4].

Solved elsewhere: Birdie (Britain) and AlayaCare (Canada) have sold care-agency operations software for over a decade, and neither sells in continental Europe. The model is proven, but never under Czechia's reimbursement rules. The US cluster above them is newer and AI-native [S1,S3]. The opening is not the occupied operations layer [S4] but Czech-language voice intake above whoever holds the scheduling and records seat.

## Revisions

2026-08-20 · gap re-check and evidence audit — Two blocks recorded on this date, merged here. De-ranked: the operations layer is occupied. The original absence check was run in the wrong language and concluded that Cygnus DP was the only tooling in the market. Searching Czech for the operations layer returns domestic vendors on the first page: VeruApp (automatic daily work planning per caregiver from the client's digital record, field mobile app, billing and statutory reporting), e-Sestřička (cloud system for domácí a paliativní péče, odbornosti 925/720/926; SESTŘIČKA.CZ s.r.o., IČO 05752779), pecovatelska.cz from Petr Zajíc software (terénní sociální služby under zák. 108/2006 Sb., 200+ deployments) and E-péče (Ústecký kraj, OP Spravedlivá transformace, 39 providers) [S4]. Per the SPEC §4 de-rank rule: gap 1 → 0, score 4 → 3, status candidate → watching. The title lost the clause "with only a legacy record-keeping system to help", which the re-check disproved, and the non-solutions and comparables paragraphs were rewritten so the body no longer asserts an absence its own score denies. The underlying problem — phone-and-paper coordination under a nurse shortage — is not withdrawn; what is withdrawn is the claim that nobody sells into it. Also removed in the same pass: the sentence "Larger charity networks (Charita ČR) offer multi-branch deals." Charita returns no hits anywhere in the signal corpus, and yc-sagecare supports only the generic phrase "charity providers", which the lead paragraph already carries — the named organisation and the multi-branch channel claim were both unbacked.

2026-08-25 · evidence added — The July 2026 Labour Office hiring aggregate (380 new general-nurse vacancies, 262 employers) and the in-force social-services amendment 92/2026 Sb. entered the evidence below [S5,S6]. Demand 1 → 2: the staffing pressure the capacity argument rests on is now documented by a recurring state dataset rather than one signal's note. Score 3 → 4; gap 0 and status watching untouched — the de-rank of 2026-08-20 stands. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched by that pass. Third pass this date, merged here: the ÚZIS KOMPAS partnership (~€5.44M for home-care classification, recommended practices and cost models) entered the evidence from the 2026-08-25 retrospective harvest [S7]. Money 0 → 1 — a relevant public contract now funds the domain's data foundations — and score 4 → 5; gap 0 and status watching still stand. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries IRESOFT, e-Sestřička, pecovatelska.cz, VeruApp and E-péče [S4]. Three pass the established test — IRESOFT on two distinct public buyers for IČO 26297850 in data/lookup/cz-contract-parties.jsonl, e-Sestřička on a named reference list, pecovatelska.cz on more than 200 deployments since 1998 — so `scores.gap` stays 0 and the 2026-08-20 de-rank now rests on receipts a machine can re-check. VeruApp and E-péče are early. `scores.proof` 1 → 2: Birdie and AlayaCare both pass the established test, but Britain, Canada, the US and Australia are none of them CEE-adjacent, so rung 3 is not met — and the body no longer says the model is proven in the US only, which its own ledger contradicted. `score` 5 → 6. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and two entries change column under the split. **IRESOFT (Cygnus DP)** becomes `competes: adjacent`: this record's own lead says Cygnus DP serves as documentation and billing record-keeping rather than operations automation [S1,S2], and what this record proposes is Czech voice intake on top of whatever system the agency already runs — so IRESOFT holds the records seat, not this one. It stays established on its two distinct public buyers. **E-péče** becomes `competes: adjacent` as well: it is a publicly funded Ústecký-kraj project putting a field app into 39 providers on EU money, a grant programme rather than a vendor selling to this record's buyer. e-Sestřička, pecovatelska.cz and VeruApp are `competes: direct` — each sells the planning, field-recording and coordination layer into these agencies — with maturities unchanged. `scores.gap` stays 0: e-Sestřička and pecovatelska.cz are both direct and established, so the 2026-08-20 finding still rests on receipts a machine can re-check even after IRESOFT moves out of the direct column. No player was ever excluded from this ledger. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Also cut from the IRESOFT entry: the phrase naming what "this record is about" — the entry now simply says what Cygnus DP does and does not do.

2026-09-02 · plain-language pass — Eight trade terms glossed or replaced at first use: agentury domácí péče, pečovatelské služby, Cygnus DP [S2], odbornosti (now nursing billing codes), domácí a paliativní péče, terénní sociální služby [S4], ÚZIS [S7], AI-ops. Argument tightened from 433 words to 300, keeping every figure, date, name and [Sn] marker. A gist added to all seven sources. The lead-in restored to the literal "Existing non-solutions:", which had been swallowing prose. No score, status, note or marker touched.
