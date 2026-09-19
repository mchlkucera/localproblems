---
id: p-0011
region: cz
title: 'Czech home-care agencies run on phones and paper while nurses are scarce'
brief: 'Agencies book, move and confirm visits by phone, while Czech employers posted 380 new nurse vacancies in one month [S1,S6]. Care services may now also help with medicines and stoma bags [S5].'
solution: 'Build a Czech-speaking phone assistant that books, moves and confirms visits in the home-care agency''s own scheduling software.'
good_for: 'Someone who''d like to work with home-care agencies.'
category: health
geo: CZ-national
score: 4
scores:
  proof: 2
  money: 0
  urgency: 0
  demand: 2
  gap: 0
status: watching
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: direct
  integration: software
  money: bootstrap
  why: 'Easier: agencies buy for themselves, no licence is needed to answer their calls, and the assistant plugs into software the agency already runs. Harder: two Czech vendors have sold planning and coordination software to these agencies for years, and the assistant must work with whichever system each agency runs.'
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
  why: "AI intake and client records for US home-care agencies (YC S24), claiming over 100 minutes saved per intake — exactly the operations layer this problem is about."
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
  why: "Since 1 July 2026 community care services (pečovatelské služby) may help clients take medicines and handle stoma and urine bags, so the same scarce staff carry more tasks."
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
  why: "262 employers posted 380 new general-nurse vacancies in July 2026 — the nurse shortage, now measured every month by a state dataset."
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
    or agency purchasing budget. Superseded 2026-09-19: on the new ladder this is public money
    nearby, the state paying for its own cost models, not an agency paying for this job, so it
    earns no point and money is 0.'
  date: '2026-07-14'
  signal: hlidac-36430740
  dims: [money]
- type: arbitrage
  name: "Evergrove"
  gist: "US voice agents for care"
  why: "A Y Combinator company, listed in August 2026, that sells voice agents to speed up care coordination in US workers' compensation insurance, on the insurer's side rather than the agency's."
  url: https://www.ycombinator.com/companies/evergrove
  note: 'yc-evergrove: YC-funded (13 Aug 2026) US company selling voice agents for care
    coordination — exactly the Czech-language voice-intake wedge this record names above the
    occupied scheduling layer, proven in the US payer setting. Listing carries no founding
    year or traction, so arbitrage source only, no comps entry.'
  date: '2026-08-13'
  signal: yc-evergrove
- type: subsidy
  name: "OPZ+ call 112 — autism-spectrum social services (100M CZK)"
  gist: "100M CZK to these providers"
  why: "The labour ministry opened 100 million CZK for services supporting people with autism spectrum disorder, applications from non-governmental organisations and registered social-service providers open until 23 November 2026."
  url: https://www.esfcr.cz/vyzva-112-opz-plus
  note: 'dotace-opz-112-pas: OP Zaměstnanost plus call 112, allocation 100,000,000 CZK
    (~EUR 4.13M at 24.215 CZK/EUR, the daily rate printed on opd3.opd.cz on 2026-09-03),
    applications 2026-09-02 to 2026-11-23; receipted from the esfcr.cz call page and the MMR
    open data agreeing. Cited for the buyer, not for the service line: the eligible-applicant
    class the call names — NNO and poskytovatelé sociálních služeb — is this record''s buyer,
    and the money is delivery capacity, which is what the intake wedge frees. It is NOT money
    for this product; nothing in the call pays for software, so money stays where the KOMPAS
    contract [S7] left it. Superseded 2026-09-19: public money nearby earns no point on the new
    ladder, and neither this call nor [S7] buys this job, so money is 0. Runner-up considered and rejected: p-0033, which already carries an
    equivalent care-capacity receipt in the Královéhradecký personal-assistance tender.'
  date: '2026-11-23'
  signal: dotace-opz-112-pas
  dims: [money]
created: '2026-08-13'
updated: '2026-09-19'
---

Czech home-care agencies still book and move visits by phone and on paper, while nurses are scarce [S1,S2].

- Hundreds of home-nursing agencies and community care services work this way [S1].
- Intake calls, new clients and visit changes run on phone and paper [S1].
- Their records software bills the care already given, and takes no calls [S2].

They include home-nursing agencies, called agentury domácí péče in Czech, and community care services, called pečovatelské služby [S1]. They range from Včelka to charity providers [S1]. Czech vendors already sell planning software above the records system; see [Market gap](#competition).

Existing non-solutions: Czech vendors already sell planning and coordination software to these agencies, and two of them have done so for years [S4].

- One cloud system covers home and palliative nursing; three named providers use it [S4].
- One community-care system runs at 200+ sites, bought as a one-off licence [S4].
- A newer app builds each carer's daily plan from the client's digital record [S4].

What each does, and what else is in the field:

- The cloud system works under the insurers' nursing billing codes 925, 720 and 926 [S4].
- The community-care system runs at more than 200 sites across Czechia, sold once rather than as a subscription [S4].
- The newer app plans the day automatically, and adds a field app for logging tasks, re-planning around sudden events, client billing and statutory reporting [S4].
- A regional project in Ústecký kraj is putting a field app into 39 care providers on EU money; it is a grant project, not a product for sale [S4].
- The records and billing software the agencies run writes down and bills the care that happened; it does not answer the phone, book or move a visit, or rebuild a day when a client cancels [S2].

Why now: Agencies short of nurses lose care hours to phone admin, and since July 2026 their care staff may take on health tasks too [S1,S5].

- Czech employers posted 380 new general-nurse vacancies in July 2026 alone [S6].
- With nurses scarce, every hour of intake calls is care capacity lost [S1].
- Care services may now also help with medicines and stoma bags [S5].

The 380 vacancies cover 651 places at 262 employers [S6]. They count every Czech employer, not home-care agencies alone [S6].

The change behind the third item is Act No. 92/2026, an amendment to the social services act, in force since 1 July 2026 [S5]. Care services may now help a client take a medicine, as long as the skin is not broken, and handle stoma and urine bags [S5]. That widens the work flowing through the same scarce staff and the same phone-and-paper coordination [S5].

The labour ministry's grant for autism-spectrum services closes on 23 November 2026 [S9].

Who pays: Agencies already buy Czech care software, but no price for it is on file, and the public money nearby pays for other work [S4,S7,S9].

- More than 200 sites bought one Czech care system as a one-off licence [S4].
- The state health-statistics institute signed about €5.4M to model home-nursing care [S7].
- The labour ministry opened 100M CZK for autism-spectrum care, open to these providers [S9].

What an agency gains is capacity, not savings: time freed from intake and coordination lets the same nurses deliver more of the care the insurers pay for [S1,S4].

The state project is KOMPAS, run by ÚZIS (the state health-statistics institute) [S7]. It builds a classification, recommended practices and cost models for home and community nursing care, and its partnership agreement was signed on 14 July 2026 [S7].

The 100M CZK is call 112 of OPZ+ (the labour ministry's employment programme) [S9]. It is open to non-governmental organisations and registered social-service providers, and it pays for care services, not for software [S9]. Its closing date is under [Why now](#why-now).

Solved elsewhere: Care-agency software has sold for years in Britain and Canada, and US start-ups now add AI for intake and scheduling [S1,S3].

A British and a Canadian company sell operations software to care agencies; their rows give their funding and customer counts.

In the US, a Y Combinator company from the summer 2024 batch uses AI to handle a home-care agency's intake, client communication and scheduling [S1]. A second, from the spring 2026 batch, builds an AI operating system for long-term care providers [S3]. Cova, from the summer 2026 batch, runs a home-care agency built around AI [S1]. That makes three US companies on care operations in two years, so the model is being copied rather than tried once [S1,S3].

Evergrove, another Y Combinator company, sells voice agents that speed up care coordination in US workers' compensation insurance [S8]. It works for the insurer rather than the agency, but it is the closest template for voice intake [S8].

The opening left in Czechia is Czech-language voice intake on top of whichever planning and records system an agency already runs, since the planning layer is sold here already [S4].

## Revisions

2026-08-20 · gap re-check and evidence audit — Two blocks recorded on this date, merged here. De-ranked: the operations layer is occupied. The original absence check was run in the wrong language and concluded that Cygnus DP was the only tooling in the market. Searching Czech for the operations layer returns domestic vendors on the first page: VeruApp (automatic daily work planning per caregiver from the client's digital record, field mobile app, billing and statutory reporting), e-Sestřička (cloud system for domácí a paliativní péče, odbornosti 925/720/926; SESTŘIČKA.CZ s.r.o., IČO 05752779), pecovatelska.cz from Petr Zajíc software (terénní sociální služby under zák. 108/2006 Sb., 200+ deployments) and E-péče (Ústecký kraj, OP Spravedlivá transformace, 39 providers) [S4]. Per the SPEC §4 de-rank rule: gap 1 → 0, score 4 → 3, status candidate → watching. The title lost the clause "with only a legacy record-keeping system to help", which the re-check disproved, and the non-solutions and comparables paragraphs were rewritten so the body no longer asserts an absence its own score denies. The underlying problem — phone-and-paper coordination under a nurse shortage — is not withdrawn; what is withdrawn is the claim that nobody sells into it. Also removed in the same pass: the sentence "Larger charity networks (Charita ČR) offer multi-branch deals." Charita returns no hits anywhere in the signal corpus, and yc-sagecare supports only the generic phrase "charity providers", which the lead paragraph already carries — the named organisation and the multi-branch channel claim were both unbacked.

2026-08-25 · evidence added — The July 2026 Labour Office hiring aggregate (380 new general-nurse vacancies, 262 employers) and the in-force social-services amendment 92/2026 Sb. entered the evidence below [S5,S6]. Demand 1 → 2: the staffing pressure the capacity argument rests on is now documented by a recurring state dataset rather than one signal's note. Score 3 → 4; gap 0 and status watching untouched — the de-rank of 2026-08-20 stands. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched by that pass. Third pass this date, merged here: the ÚZIS KOMPAS partnership (~€5.44M for home-care classification, recommended practices and cost models) entered the evidence from the 2026-08-25 retrospective harvest [S7]. Money 0 → 1 — a relevant public contract now funds the domain's data foundations — and score 4 → 5; gap 0 and status watching still stand. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries IRESOFT, e-Sestřička, pecovatelska.cz, VeruApp and E-péče [S4]. Three pass the established test — IRESOFT on two distinct public buyers for IČO 26297850 in data/lookup/cz-contract-parties.jsonl, e-Sestřička on a named reference list, pecovatelska.cz on more than 200 deployments since 1998 — so `scores.gap` stays 0 and the 2026-08-20 de-rank now rests on receipts a machine can re-check. VeruApp and E-péče are early. `scores.proof` 1 → 2: Birdie and AlayaCare both pass the established test, but Britain, Canada, the US and Australia are none of them CEE-adjacent, so rung 3 is not met — and the body no longer says the model is proven in the US only, which its own ledger contradicted. `score` 5 → 6. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and two entries change column under the split. **IRESOFT (Cygnus DP)** becomes `competes: adjacent`: this record's own lead says Cygnus DP serves as documentation and billing record-keeping rather than operations automation [S1,S2], and what this record proposes is Czech voice intake on top of whatever system the agency already runs — so IRESOFT holds the records seat, not this one. It stays established on its two distinct public buyers. **E-péče** becomes `competes: adjacent` as well: it is a publicly funded Ústecký-kraj project putting a field app into 39 providers on EU money, a grant programme rather than a vendor selling to this record's buyer. e-Sestřička, pecovatelska.cz and VeruApp are `competes: direct` — each sells the planning, field-recording and coordination layer into these agencies — with maturities unchanged. `scores.gap` stays 0: e-Sestřička and pecovatelska.cz are both direct and established, so the 2026-08-20 finding still rests on receipts a machine can re-check even after IRESOFT moves out of the direct column. No player was ever excluded from this ledger. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Also cut from the IRESOFT entry: the phrase naming what "this record is about" — the entry now simply says what Cygnus DP does and does not do.

2026-09-02 · plain-language pass — Eight trade terms glossed or replaced at first use: agentury domácí péče, pečovatelské služby, Cygnus DP [S2], odbornosti (now nursing billing codes), domácí a paliativní péče, terénní sociální služby [S4], ÚZIS [S7], AI-ops. Argument tightened from 433 words to 300, keeping every figure, date, name and [Sn] marker. A gist added to all seven sources. The lead-in restored to the literal "Existing non-solutions:", which had been swallowing prose. No score, status, note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as three lines under the headline: a `brief:` on who is stuck and what forces it now, the `solution:` as a call to action starting "Build", and a new `good_for:` line. Previous title, verbatim: "Czech home-care agencies burn scarce nurse time on phone-and-paper intake, scheduling and coordination". Previous solution, verbatim: "Czech-speaking voice intake for home-care agencies — the calls that book, move and confirm visits answered automatically, on top of the scheduling system the agency already runs." There was no previous brief or good_for. Checked against the sources before writing: "burn scarce nurse time" left the headline, because no source says nurses are the ones answering the booking calls — the signal behind [S1] says agencies run on phone and paper under a nurse shortage, so the headline now puts those two facts side by side. The 380 vacancies are general-nurse vacancies posted by all Czech employers in July 2026, not by home-care agencies alone, and the brief says "Czech employers" for that reason [S6]. The July 2026 change is stated as already in force, never as upcoming [S5]. No urgency was added: the record has no dated deadline. "As companies already do in the US" rests on Sage Care and TakeCareOS [S1,S3]. No score, status, source, note, marker or body sentence changed. Simplified for the front page: title "Czech home-care agencies run on phone calls and paper while nurses are hard to find" → "Czech home-care agencies run on phones and paper while nurses are scarce"; brief "Agencies book, move and confirm visits by phone, while Czech employers posted 380 new nurse vacancies in July 2026 alone [S1,S6]. Since July 2026, care services may also help clients take medicines and handle stoma bags [S5]." → "Agencies book, move and confirm visits by phone, while Czech employers posted 380 new nurse vacancies in one month [S1,S6]. Care services may now also help with medicines and stoma bags [S5]."; solution "Build a Czech-speaking phone assistant that books, moves and confirms home-care visits in the agency's own scheduling software, as companies already do in the US." → "Build a Czech-speaking phone assistant that books, moves and confirms visits in the home-care agency's own scheduling software.". The July 2026 dates and the "alone" were cut; "380 new nurse vacancies in one month" keeps its marker [S6]; "as companies already do in the US" was cut.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the phone-and-paper booking under a nurse shortage, with the hundreds of agencies, the intake and visit work, and the records software as its first three items; the Czech names of the two kinds of provider and the Včelka-to-charity range are its detail [S1,S2]. Competition opens on the Czech vendors that already sell the planning layer, and describes each by what it sells, with short items first and the billing codes, the one-off licence, the newer app's features, the regional grant project and the records software's limits below [S2,S4]. Why now opens on the care hours lost to phone admin and the July 2026 change, with the vacancies, the lost capacity and the new health tasks as its first three items and the amendment's detail below [S1,S5,S6]. Willing to pay now answers whether anyone pays: agencies buy care software, and the state pays to cost home nursing care [S4,S7,S9]. Validated abroad became one answer sentence and short paragraphs [S1,S3,S8]. Every comps[] and locals[] company left the body (Cygnus DP and IRESOFT, VeruApp, e-Sestřička, pecovatelska.cz and Petr Zajíc software, E-péče, Sage Care, TakeCareOS, Birdie, AlayaCare); each is described by what it sells, and its name, year and customers stay in its row. Detail added from sources already on file, none of it new evidence: the 651 places behind the 380 vacancies, and that they count every Czech employer [S6]; what the amendment allows, medicines without breaking the skin and stoma and urine bags [S5]; KOMPAS's signing date and ÚZIS glossed [S7]; the OPZ+ call's number and applicants, and that it pays for care, not software [S9]; and Evergrove, whose source S8 the body never cited, as the closest template for voice intake [S8]. `entry.why` was rewritten as "Easier: … Harder: …" from the same gates, and it no longer names Cygnus DP, e-Sestřička or pecovatelska.cz. Four source lines changed: S1's, S5's and S6's why said "this record", and S8 gained a public name, gist and why, written from its note and signal. No `process:` block was added: the sources say agencies run intake and scheduling on phone, paper and a records system [S1,S2], but none says who takes the calls or books the visits (the 2026-09-16 headline pass already found no source saying nurses do), so the steps could not name who does what without inventing it. Corrected against the sources rather than against the old sentences: the amendment was said to add "work per scarce nurse", but it widens what care services, which are carers rather than nurses, may do, and S5's note says "the same scarce staff", so the body and S5's why now say that [S5]; "Birdie (Britain) and AlayaCare (Canada) have sold … for over a decade" was wrong for Birdie, founded in 2017, so it now says "for years"; "neither sells in continental Europe" and "the model is proven, but never under Czechia's reimbursement rules" had no source on file and were cut; "the agencies buy capacity" became "what an agency gains is capacity", since no source records an agency buying for that reason. Flagged as inference: that freed time lets nurses deliver more of the care the insurers pay for, which rests on S1's note that admin time converts to capacity and on the insurers' nursing billing codes [S1,S4]; and that the opening left in Czechia is Czech-language voice intake on top of an agency's existing system, since no search on file looked for a Czech voice-intake seller [S4]. No score, status, source order, `note:`, title, brief, solution or good_for changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 1 → 0, Willing to pay 1 → 0 and `score` 6 → 4, so the band moves FAIR → FAINT. Why now was 1 as deadline 0 plus the freshness point, which is retired. The only dated instrument on file, Act No. 92/2026, says care services may help with medicines and stoma bags from 1 July 2026 [S5]. That permits something and sets nothing due, so it is rung 0. The autism-services grant's closing date is a grant date, not a deadline [S9]. Willing to pay was 1 on the ÚZIS KOMPAS contract [S7], which is public money nearby: the state paying for its own cost models of home nursing care, not an agency paying for this job. It now earns nothing. Tagging pass, every source on file that might show someone paying for this job: more than 200 sites bought a Czech care system as a one-off licence, but no amount is on file [S4]; the OPZ+ call pays for care services, not software [S9]; the hiring data prices nurses' wages, not intake or scheduling [S6]. No receipt could be written, so money is 0, as the worksheet had it. [S7]'s and [S9]'s notes named the old money rung and now carry the correction. Their `dims: [money]` stay, because on the new ladder that tag is what shows them as public money nearby. Why now prose re-read: it describes lost care hours and the new tasks the amendment permits, and claims no deadline, so it stands. Willing to pay's answer sentence read as a yes. It now says agencies buy Czech care software, that no price for it is on file, and that the public money nearby pays for other work [S4,S7,S9]. `[Competition](#competition)` became `[Market gap](#competition)` in The opportunity. No other score, status, entry or body sentence changed.
