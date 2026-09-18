---
id: p-0004
region: cz
title: 'Czech families caring for a sick relative can miss out on state money in a confusing claim'
brief: 'A home visit sets the grade, and one grade higher can pay over 4 times as much a month [S7]. Guides describe the process as bureaucratic and opaque [S3].'
solution: 'Build an online service that files a family''s care-allowance claim, prepares them for the home visit and handles any appeal.'
good_for: 'Someone who''d like to help families caring for a sick or elderly relative.'
price_search: 'The MS2021+ index under "neformální péče" (Moravskoslezský kraj and Statutární
  město Brno are funded there for carer counselling — the same navigation done by hand, free,
  on public money) and registr smluv full-text for "odborné sociální poradenství" for what a
  town pays a counselling service per year; otherwise ask the head of a registered
  social-counselling service such as Rodinný průvodce what one care-allowance appeal costs in
  staff hours.'
category: health
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 1
  urgency: 1
  demand: 1
  gap: 2
status: candidate
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: nothing licences the work, the job is coaching and paperwork rather than a system to plug into, and families decide for themselves without a tender. Harder: free advisers already write appeals for nothing, so a paid service has to carry the whole claim; and no Czech family is yet known to pay for this help.'
comps:
- name: Oma Care
  url: https://www.omacare.com/
  geo: US
  since: 2024
  traction: 'YC W24, 2-person team (YC, 2026); automates enrolment in US Medicaid programs paying family caregivers up to $28/hr'
  signal: yc-oma-care
- name: Givers
  url: https://www.givers.com/
  geo: US
  since: 2021
  traction: '$3.5M seed led by CRV (Forbes, 2023); app used by 15,000 caregivers/month (Forbes, 2026)'
- name: KareHero
  url: https://www.karehero.com/
  geo: GB
  since: 2022
  traction: 'company raise undisclosed (Tracxn, 2025); £9M+ care funding unlocked for families, avg £27k each (company, 2026); employer channel'
locals:
- name: pece.cz (NN Životní pojišťovna)
  url: https://www.pece.cz/
  competes: adjacent
  maturity: early
  evidence: 'A free information site run by the insurer NN Životní pojišťovna: an entitlement
    calculator, articles and an advice column, after which the applicant is sent to the state
    office to file the claim themselves. Nobody there files, chases or appeals anything, and no
    tally of who has used it is published.'
- name: Rodinný průvodce (Centrum pro rodinu a sociální péči)
  url: https://www.prorodiny.cz/lide-se-zdravotnim-postizenim-a-pecujici/odborne-socialni-poradenstvi-rodinny-pruvodce/a-91/
  ico: '48804517'
  since: 1993
  competes: adjacent
  maturity: established
  evidence: 'It does write appeals, and it writes them free: Centrum pro rodinu a sociální péči
    z. s. of Ostrava, trading since 1993, runs Rodinný průvodce on the state register of social
    services. What a family gets is an adviser''s hour in the Moravskoslezský region, not
    somebody who carries the claim from application through the assessment visit to the appeal
    and is paid for the result.'
- name: Moravskoslezský kruh
  url: https://www.mskruh.cz/poradna/socialne-pravni-poradna-pro-pecujici/
  ico: '26618761'
  since: 2003
  competes: adjacent
  maturity: early
  evidence: 'It provides advice and nothing else, free: a legal helpline for carers answered by
    two lawyers and capped at an hour per enquirer, publishing its answers on care-allowance
    grades, assessment visits and appeals. The association has been going since 2003 but
    publishes no tally of who it has helped; it answers the question and never takes the claim
    over, which is the job somebody would be paid to do.'
- name: Chytrá Péče
  url: https://www.chytrapece.cz/
  ico: '27927946'
  since: 2007
  competes: adjacent
  maturity: established
  evidence: 'It sells the care, not the paperwork: an SOS button with a 24/7 response line, home
    assistance, equipment hire and counselling, with help on benefit forms folded into the
    counselling for free. The company has traded since 2007 and sits on the state register of
    social service providers under a labour-ministry authorisation.'
- name: Dostupný advokát
  url: https://dostupnyadvokat.cz/
  ico: '09788336'
  since: 2021
  competes: adjacent
  maturity: established
  evidence: 'An online law firm selling fixed-price legal work of every kind — 390 CZK for a
    consultation, representation quoted per case — trading since 2021 and reporting thousands
    of resolved cases and 150+ new customers a month. Its care-allowance page is an article
    that routes the reader to general representation in court; it does not file the
    application, attend the assessment visit or run the appeal as something a family can buy.'
process:
  summary:
    today: 'The family files the claim at the labour office itself, goes through the assessment that sets the grade, and appeals with a free adviser''s help where it finds one [S3,S9].'
    after: 'An online service files the claim with the family, prepares it for the home visit and runs any appeal.'
  steps:
  - who: Family
    today: 'Files the claim at the labour office'
    known: documented
    cites: [6, 9]
    change: changes
    after: 'Has the service file the claim'
  - who: Family
    today: 'Goes through the assessment that sets the grade'
    known: documented
    cites: [3]
    change: changes
    after: 'Is coached for the home visit first'
  - who: Family
    today: 'Appeals a grade with a free adviser''s help'
    known: documented
    cites: [6, 9]
    change: changes
    after: 'Hands the appeal to the service'
  - who: '?'
    today: 'How often a grade is appealed, and how often an appeal wins, is not known'
    known: unknown
    cites: []
    change: stays
    after: 'Unknown: nothing on file counts appeals'
sources:
- type: arbitrage
  name: "Oma Care"
  gist: "the closest US template"
  why: "A two-person YC W24 team enrolling US family caregivers into Medicaid programmes that pay them up to $28 an hour — the template for getting families money they are already owed."
  url: https://www.ycombinator.com/companies/oma-care
  note: 'yc-oma-care: Oma Care (YC W24) builds infrastructure to train and get family caregivers
    paid (53M caregivers in the US); CareOasis (YC S23) is the same model — a validated US
    cluster. US-only, scored as one analog.'
  date: '2026-08-13'
  signal: yc-oma-care
- type: subsidy
  name: "Příspěvek na péči"
  gist: "the benefit itself"
  why: "The Czech care allowance itself — four dependency levels, raised again in 2024-25, and the money a family wins or loses on how well it files."
  url: https://www.ycombinator.com/companies/oma-care
  note: Signal note references příspěvek na péči — four levels, raised again in 2024-25, flowing
    to ~380k dependent persons — the state benefit program the product would help families
    access.
  date: '2026-08-13'
- type: gap-check
  name: "First Czech market scan"
  gist: "the first Czech sweep"
  why: "An early sweep that returned only advice articles and government pages, and documented the application, assessment and appeal as bureaucratic and opaque."
  url: https://www.ycombinator.com/companies/oma-care
  note: 'Absence check 2026-08-13: searches return only advice articles and government pages
    (pece.cz, mpsv.gov.cz); no player that files, tracks or optimizes claims for families.
    Demand point: signal documents that application, hodnocení stupně závislosti and appeals
    are bureaucratic and opaque.'
  date: '2026-08-13'
- type: tender
  name: "TED — MPSV 'IT delivery III' framework (~€74.7M)"
  gist: "the €74.7M ministry IT framework"
  why: "The ministry budgets tens of millions of euros a year for benefits back-office IT, while nothing is built on the side the citizen actually touches."
  url: https://ted.europa.eu/en/notice/-/detail/402149-2026
  note: 'ted-402149-2026 (context): MPSV ''IT delivery III'' framework ~€74.7M plus a dozen
    related awards (EKIS III ~€19.8M open, OKaplikace ~€65M) in Jun–Aug 2026 — the state demonstrably
    budgets tens of millions EUR/yr for benefits back-office IT while the citizen-facing navigation
    layer stays unbuilt. Adjacent spend: kept at money=1, not 2.'
  date: '2026-06-11'
- type: statistic
  name: "ČSÚ — the care allowance in numbers"
  gist: "374,000 recipients, 41.3bn CZK"
  why: "374,000 people drew příspěvek na péči in December 2024, and 41.3bn CZK was paid out through it that year — the size of the pot families are navigating for."
  url: https://csu.gov.cz/produkty/prispevek-na-peci-loni-vyuzivalo-vice-nez-370-tisic-lidi
  note: 'ČSÚ release published 2025-11-14, traced by the 2026-08-20 evidence audit as the primary
    source for this record''s CORRECTION block: "V prosinci 2024 pobíralo příspěvek na péči již
    374 tisíc osob" — 374,000 recipients in December 2024 — and "V roce 2024 bylo ze státního
    rozpočtu prostřednictvím příspěvku na péči vydáno 41,3 mld. Kč". Both figures in the correction
    are confirmed. No evidence-layer signal covers this release, so no signal ref; it is a correction
    receipt and backs no score dimension.'
  date: '2025-11-14'
  dims: []
- type: gap-check
  name: "Market scan — who helps a Czech family claim"
  gist: "the free-counselling sweep"
  why: "Five Czech searches and an ARES sweep found free counselling and calculators only — pece.cz, the NRZP poradna, Rodinný průvodce — and no company that files, tracks or appeals a claim for a fee."
  url: https://pece.cz/prispevek-peci/
  note: 'Gap re-check 2026-08-20: looked for the specific product this record claims missing —
    a Czech company that files, tracks, optimizes or appeals příspěvek na péči claims on behalf
    of families. Five Czech-language searches plus an ARES sweep surfaced information and free
    counselling only: pece.cz (run by NN Životní pojišťovna) offers a free entitlement calculator
    and a poradna but directs applicants to the Úřad práce; MPSV/ÚP publish the forms; registered
    odborné sociální poradenství services (NRZP poradna, Rodinný průvodce, Moravskoslezský kruh)
    do help draft appeals, for free and as a social service rather than a product; Chytrá péče is
    a family care-planning app with SOS-watch alerts that does not touch the benefit at all. ARES
    on "pečující" returns two nonprofits (ALARP Oplenka z.s., Pro pečující z.ú.) and no commercial
    claims navigator. POSITIVE CONTROL passed before this negative was trusted: the same method put
    Softlink CEM Smart and Ringil — both register-confirmed CZ incumbents — at the top of their own
    queries, and ARES resolved IRESOFT s.r.o., SOFTLINK s.r.o. and Ringil s.r.o. by name. Verdict:
    NOT FOUND. No incumbent, so no de-rank; a negative never raises a score, so gap stays 2 and the
    total is unchanged.'
  date: '2026-08-20'
  queries:
    - "pomoc s žádostí o příspěvek na péči odvolání poradenství pro rodiny služba"
    - "vyřídíme za vás příspěvek na péči zvýšení stupně závislosti služba poradce"
    - "\"příspěvek na péči\" online aplikace pomůže s žádostí startup pečující rodiny"
    - "Chytrá péče aplikace pro pečující rodiny česká sociální dávky"
    - "placená služba sociální poradce vyřízení dávek pro seniory příspěvek na péči firma"
  checked: [ares, google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: regulation
  name: "Care allowance raised from 1 January 2026"
  gist: "the January 2026 raise"
  why: "Grades I and II rise — adult grade I from 880 to 1,300 CZK monthly — so the money a family wins or loses on a correct filing grew again."
  url: https://mpsv.gov.cz/prehledne-legislativni-zmeny-z-gesce-mpsv-ucinne-od-1-ledna-2026
  note: 'reg-prispevek-na-peci-2026: zákon č. 360/2025 Sb. raises příspěvek na péči for
    dependency grades I and II from 2026-01-01 — adults I 880→1,300 CZK and II 4,900→5,400 CZK
    monthly; children I 3,300→4,900 and II 7,400→8,200 (grades III/IV unchanged). Primary
    receipt for the body''s "raised again" claim, which previously leaned on the S2 note.'
  date: '2026-01-01'
  signal: reg-prispevek-na-peci-2026
- type: regulation
  name: "VeKLEP — bill amending the benefit's two framework acts"
  gist: "the pending amendment bill"
  why: "MPs filed a bill amending both the Social Services Act 108/2006 (the příspěvek na péči law) and the disability-benefits act 329/2011 — the rules families navigate are in motion again."
  url: https://odok.cz/portal/veklep/material/ALBSDS9BKZY8/
  note: 'veklep-ALBSDS9BKZY8: MPs'' bill no. 125 (Juchelka, Pastuchová, filed 17 Mar 2026)
    amending zákon č. 108/2006 Sb. — the act příspěvek na péči lives in — together with zákon
    č. 329/2011 Sb. o dávkách pro osoby se zdravotním postižením. Draft with no dated
    obligation: context receipt only, backs no score dimension.'
  date: '2026-03-17'
  signal: veklep-ALBSDS9BKZY8
  dims: []
- type: gap-check
  name: "Market scan — what a family can actually buy"
  gist: "the paid-side sweep"
  why: "A second Czech sweep, this time for anything sold for money: an insurer's free calculator, free registered counselling that writes appeals, and law firms selling representation by the case — still nobody selling a family the claim itself."
  url: https://dostupnyadvokat.cz/blog/odvolani-prispevek-na-peci
  note: 'Gap re-check 2026-08-25, run to build this record''s locals[] ledger and to test the
    2026-08-20 verdict from the paid side: is there a Czech provider a family can HIRE to win or
    raise a příspěvek na péči award? POSITIVE CONTROL FIRST, and it passed: descriptive Czech
    queries carrying no vendor name ("pomoc s žádostí o příspěvek na péči placená služba poradce
    zvýšení stupně závislosti 2026"; "vyřídíme příspěvek na péči za vás služba poplatek odvolání
    firma") put pece.cz, Mapa péče, Vysočina pečuje and Dostupný advokát on the first page —
    known-existing Czech providers in exactly this domain — and ARES resolved every organisation
    named below by name (Centrum pro rodinu a sociální péči z. s. 48804517, Moravskoslezský kruh
    z. s. 26618761, Chytrá Péče s.r.o. 27927946, Dostupný advokát s.r.o. 09788336, NRZP ČR
    70856478). WHAT IT FOUND, all now on the ledger as adjacent: pece.cz (run by NN Životní
    pojišťovna) — calculator, articles, advice column, then "go to the office"; Rodinný průvodce
    (Centrum pro rodinu a sociální péči z. s., Ostrava) — writes appeals for families FREE as a
    registered social service in one region; Moravskoslezský kruh — free advice line, two
    lawyers, one hour per enquirer, answering care-allowance and appeal questions; Chytrá Péče
    s.r.o. — SOS button, home assistance and equipment hire, an MPSV-registered provider, benefit
    help folded into free counselling; Dostupný advokát s.r.o. — fixed-price online legal
    services (390 CZK consultation), whose care-allowance page is an article routing to general
    court representation. NOT FOUND: any company that files, tracks, escalates or wins the claim
    for a fee, which is what this record proposes. NOT CLAIMED AS PLAYERS: ALARP Oplenka z. s.
    (06236120) and Pro pečující z.ú. (08091986), the two nonprofits the 2026-08-20 ARES sweep
    returned — neither has a reachable site and nothing published says what either offers a
    family, and naming a competitor on a company name alone would be a guess. Also seen and not
    lifted: Mapa péče, Dávky.cz and Umírání.cz are editorial portals rather than providers.
    Verdict: NOT FOUND. gap stays 2 and the total is unchanged; adjacent players never move it.'
  date: '2026-08-25'
  queries:
    - "pomoc s žádostí o příspěvek na péči placená služba poradce zvýšení stupně závislosti 2026"
    - "vyřídíme OR zařídíme příspěvek na péči za vás služba poplatek odvolání firma"
    - "\"Rodinný průvodce\" poradna pečující rodiny příspěvek na péči odvolání sociální poradenství"
  checked: [ares, google-cz]
  expires: '2026-11-23'
- type: complaint
  name: "European Commission — 2026 Country Report for Czechia"
  gist: "100,000 carers held back"
  why: "Around 100,000 Czech informal carers, mostly women, report being unable to work full-time because of care duties, and only 8.3 percent of public long-term-care spending goes to home care against an EU average of 28.8 percent."
  url: https://economy-finance.ec.europa.eu/document/download/3f5af374-4872-4b57-ac99-8507c5420083_en?filename=CZ_SWD_2026_203_1_EN_autre_document_travail_service_part1_v3.pdf
  note: 'ecsem-cz2026-ltc-mix: Commission Staff Working Document SWD(2026) 203 final, 2026
    Country Report — Czechia, 3 June 2026 (main text and Annex), the spending-mix and access
    half of the long-term-care picture. 2022 figures: residential 60.2% against EU 46.2%, home
    care 8.3% against EU 28.8%; 16.2% of over-65s with severe difficulties receive home care
    against EU 28.6%; 63% of working-age people with disabilities do not use field services for
    reasons of capacity, inflexibility and cost rather than preference; ~100,000 informal carers
    constrained at work. Cited here for the informal-carer finding, which is the first
    non-arbitrage receipt on this record for the claim that families deliver the care the
    allowance funds — until now that sentence rested on [S1], a US comparable. Distinct from
    civic-mpsv-ltc-predikce-2035, the bed-count half. Runner-up considered and rejected: p-0011,
    whose buyer is the home-care agency, where this is about the family that gets no service.'
  date: '2026-06-03'
  signal: ecsem-cz2026-ltc-mix
  dims: [demand]
created: '2026-08-13'
updated: '2026-09-03'
---

Families caring for a sick relative must win the state care allowance through an application, a home assessment and sometimes an appeal [S3].

- 374,000 people drew the allowance in December 2024 [S5].
- The assessment sets one of four grades, and the grade sets the money [S2,S7].
- The application, the assessment and the appeal are described as bureaucratic and opaque [S3].

The allowance is příspěvek na péči, and it is paid to the person who needs care, not to the carer [S2]. The home assessment is the hodnocení stupně závislosti, the dependency grading [S3]. A family whose relative lands on too low a grade still gives the care, with less state money for it [S7].

Existing non-solutions: The help a Czech family gets is free advice, and no company files, chases or appeals the claim for a fee [S6,S9].

- An insurer's free site has a calculator, then sends families to file alone [S6].
- The labour ministry and labour office publish guides and forms, and stop there [S3,S6].
- Registered counselling services help draft appeals for free, as a social service [S6].

The insurer's site also carries articles and an advice column, and the family then files at the labour office itself [S9]. The counselling services are odborné sociální poradenství, social counselling registered with the state, and they help as a social service rather than as a product [S6].

- One of them writes appeals in a single region, and a carers' association runs a free legal helpline [S9].
- A home-care company folds help with benefit forms into its free counselling [S9].
- An online law firm's care-allowance page points to court representation rather than to the claim [S9].

Why now: A family on too low a grade can lose thousands of crowns a month, and the two lowest grades pay more since January 2026 [S7].

- Adults get 5,400 CZK monthly on the second grade, 1,300 on the lowest [S7].
- Around 100,000 carers, mostly women, say they cannot work full-time because of care [S10].
- Home care gets 8.3% of public long-term-care money; the EU average is 28.8% [S10].

The dates behind this:

- In 2024–25 the allowance was raised [S2].
- On 1 January 2026 Act No. 360/2025 raised the two lowest grades again: for adults from 880 to 1,300 CZK and from 4,900 to 5,400 CZK a month, for children from 3,300 to 4,900 CZK and from 7,400 to 8,200 CZK [S7]. The two highest grades stayed the same [S7].
- On 17 March 2026 MPs filed a bill amending both the social-services act the allowance lives in and the disability-benefits act, so the rules families work through are moving again [S8].
- On 3 June 2026 the European Commission published the carer figures in its country report on Czechia; the home-care share is for 2022 [S10].

Who pays: No family is known to pay for this yet: the help on offer is free, though a higher grade is worth thousands a month [S9,S7].

- An online law firm sells fixed-price consultations, but not the claim itself [S9].
- The state paid out 41.3bn CZK through the allowance in 2024 [S5].
- The labour ministry's June 2026 benefits IT framework is worth about €74.7M [S4].

A flat or success fee on the award is the suggested model, and no source on file shows one charged in Czechia [S9]. The US start-ups on file help carers get paid by state programmes, and how they charge is not on file [S1].

- An insurer already runs a free information site on the allowance, and a home-care firm helps with benefit forms for free, so both could be a sales channel [S9].
- The ministry's framework buys back-office IT for benefits, with related notices of about €19.8M and about €65M in June–August 2026, and none of it is built for the family filing the claim [S4].

Solved elsewhere: US start-ups already help family carers get paid from state programmes, and nobody sells that help in Czechia yet [S1,S9].

The closest, from Y Combinator's winter 2024 intake, enrols US family carers into Medicaid programmes that pay them up to $28 an hour [S1]. Medicaid is the US public health programme for people on low incomes, and Y Combinator is a US programme that funds start-ups. CareOasis, from its summer 2023 intake, works on the same model [S1]. The US has 53 million family carers, by the first start-up's count [S1].

The Czech version would be paid from a state benefit rather than from Medicaid: the money at stake is the care allowance itself [S2].

## First moves

1. Build a short guide that prepares a family for the home assessment that sets its relative's care-allowance grade. The grade decides the money, and one grade up is worth much more each month; see [Why now](#why-now). Coach the family on what the assessment covers and what to note down before the visit, because the process is described as bureaucratic and opaque; see [The opportunity](#opportunity). Build no portal until the coaching works.
2. Contact the free carers' advice services and ask them to pass on the families whose claims they cannot carry through. They give advice or write an appeal, and stop there; see [Competition](#competition). The claim still has to be filed, chased and defended, which is the work a family would pay someone to do, and the advisers are glad to have somewhere to send them.
3. Open each sales conversation with how much the allowance pays out and how much one grade is worth. The state pays out billions through it every year, as [Willing to pay](#willing-to-pay) shows, and the lower grades were raised again this year; see [Why now](#why-now). The family in front of you is either on the right grade or paying the difference itself.
4. Charge for the outcome, a flat or success fee on the award, because nobody in Czechia sells a family the claim itself. An online law firm already sells fixed-price consultations but sends care-allowance cases to court representation; see [Competition](#competition). What no one sells is the whole claim, from the application through the home visit to the appeal, so price that.

## Revisions

2026-08-13 · fact check — The recipient figure should read 374,000 (Dec 2024, ČSÚ/MPSV), with 41.3 bn CZK paid through the benefit in 2024 [S5]; the ~380k figure in this record is slightly above the latest confirmed official number. Source: https://csu.gov.cz/produkty/prispevek-na-peci-loni-vyuzivalo-vice-nez-370-tisic-lidi

2026-08-20 · evidence audit and title sweep — Two blocks recorded on this date, merged here. The fact check above is verified: the ČSÚ release of 2025-11-14 states "V prosinci 2024 pobíralo příspěvek na péči již 374 tisíc osob" and 41,3 mld. Kč paid out through the benefit in 2024, so both its figures check out against the primary source, which is now on the ledger as [S5]. Separately, the title claimed families have "no help beyond static info portals". The 2026-08-20 gap re-check found otherwise and the body says so: pece.cz carries an entitlement calculator and a poradna, and registered odborné sociální poradenství services draft appeals [S6]. What is absent is a product that files, tracks or optimizes a claim — which is what gap 2 records — not all help. The overstated clause is gone; the gap score is untouched.

2026-08-25 · regulation added — The 2026 care-allowance raise entered the evidence ledger (zákon č. 360/2025 Sb.: grades I/II up from 1 Jan 2026) and now receipts the why-now claim directly [S7], replacing the second-hand S2 note as its source. Scores unchanged. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "monetizes caregiver enablement" now reads "charges US families for caregiver support and training". Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: the first VeKLEP harvest put MPs' bill 125 on the ledger — it amends both framework acts behind the benefit (108/2006 and 329/2011) [S8]. A draft with no dated obligation: context only, no score moved. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `scores.proof` 1 → 2: of the three comparables only Givers passes the established test — Oma Care is two years old and KareHero cites no limb the test reads — so one established foreign player, rung 2, and the US-only reading in the body still stands. `scores.gap` stays 2: the 2026-08-20 scan found free counselling and nonprofits rather than a company selling the claim, and it recorded its queries, its surfaces and a passing positive control [S6], which is exactly what rung 2 requires. No `locals[]` key is written — there is no local player selling this, and an empty list is refused by the schema. `score` 6 → 7. Fifth pass this date, merged here: **this record gains a `locals[]` ledger for the first time**, and the pass above is wrong where it says there is no local player — it says so because the ledger the gap ladder reads is a ledger of players who SELL THIS, and the split now has a place for everybody else. Five entries, all `competes: adjacent`, every one of them named in this record's own prose or in the [S6] scan and none of them recorded until now: **pece.cz** (run by NN Životní pojišťovna — calculator, articles, advice column, then the applicant goes to the office alone), **Rodinný průvodce** (Centrum pro rodinu a sociální péči z. s., IČO 48804517, ARES-dated 1993 — it writes appeals for families free, on the state register of social services, in one region), **Moravskoslezský kruh** (IČO 26618761, ARES-dated 2003 — a free advice line, two lawyers, an hour per enquirer), **Chytrá Péče** (IČO 27927946, ARES-dated 2007, an MPSV-registered provider — it sells the care, and folds benefit help into free counselling) and **Dostupný advokát** (IČO 09788336, ARES-dated 2021 — fixed-price online legal work, thousands of cases, 150+ new customers a month, whose care-allowance page routes to general court representation) [S9]. `scores.gap` stays 2 and `score` stays 7, which is the point of the split: a mature firm selling something next door never moves this score, and every one of these five sells something next door. A second check was run before relying on that, with a positive control first — descriptive Czech queries carrying no vendor name surfaced pece.cz and Dostupný advokát, and ARES resolved all five organisations by name — and it still found nobody who will file, chase or win the claim for a fee [S9]. Two names from the earlier ARES sweep, ALARP Oplenka z. s. and Pro pečující z.ú., are deliberately NOT on the ledger: neither has a reachable site and nothing published says what either offers a family, and a URL or a product claim would have had to be invented to record them. They stay named in the check. The non-solutions paragraph gains one sentence for the paid route [S9]; no existing source note was touched and no [Sn] marker moved. Same pass, prose hygiene: ledger lines that talked about this file rather than about the market were reworded — they render under each entry on the public page, where a reader has no idea a register exists. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Same date, separate pass, merged here: `## First moves` written for the first time. The template reserves the section for records scoring 7 or more, which this one has since the fourth pass above, and it had none. Four moves off receipts already on the record — the free advice services and their limits [S9], the assessment visit that sets the grade [S3] and the January 2026 grade amounts [S7], the ČSÚ recipient and spend figures [S5], and the scan that found nobody selling the claim for a fee [S9]. No new claim was introduced and no score moved.

2026-09-02 · plain-language pass — Four terms glossed at first use in the body: příspěvek na péči, hodnocení stupně závislosti, odborné sociální poradenství, and NN Životní pojišťovna, named as an insurer. Argument tightened 307 → 299 words with every figure, named company and [Sn] marker kept; How big now states the ČSÚ recipient and spend figures [S5]. First moves rewritten verbs-first. A gist added to all nine sources. No score, status, source note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` on who is stuck and what is happening, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Families caring for ~380,000 dependent Czechs must obtain and defend příspěvek na péči through an opaque, bureaucratic process". Previous solution, verbatim: "A guided service that gets a family through the Czech care allowance (příspěvek na péči) — the application, the assessment visit and the appeal — for a flat or success fee." The record carried no brief and no good_for before this pass. Every claim was checked against this record's sources first. 374,000 is the statistics office's count for December 2024, the latest on file [S5]; the old title's ~380,000 came from a harvest note the 2026-08-13 fact check had already corrected. The grade amounts are the adult rates in force since 1 January 2026, and "over 4 times" is 5,400 against 1,300 CZK [S7]. "No Czech company handles the whole claim for a fee" is the 2026-08-25 check with a passing positive control [S9], and the free advisers who draft appeals are stated beside it [S6]. The body's "usually an appeal" and "families deliver most of the care" were not used: no source on file counts appeals or measures the share of care families give. There is no dated trigger on this record, so the headline states the problem without one. No score, status, source, note, marker or body sentence changed. Simplified for the front page: brief "For an adult, grade II pays 5,400 CZK a month, over 4 times as much as grade I, so the grade matters a lot [S7]. Free advisers help with appeals, but no Czech company handles the whole claim for a fee [S6,S9]." → "One grade higher can pay an adult over 4 times as much a month [S7]. Free advisers help families appeal, but no Czech company handles the whole claim for a fee [S6,S9]."; solution "Build an online service that files a family's care-allowance claim, prepares them for the assessment and runs any appeal, as companies already do abroad." → "Build an online service that files a family's care-allowance claim, prepares them for the assessment and runs any appeal."; good_for "Someone who'd like to work with families caring for a sick or elderly relative." → "Someone who'd like to work with families caring for a relative.". "One grade higher can pay over 4 times as much" is the grade I to grade II adult step, 1,300 against 5,400 CZK [S7]; the headline was already short and is unchanged. Same date, pain-point pass: title "374,000 Czechs get a state care allowance, and an assessment decides how much" → "About 100,000 Czech family carers can't work full-time, and one assessment sets their relative's allowance". Why: the old headline was a count of recipients, with no one hurting. The new pain is the European Commission's own finding that around 100,000 Czech informal carers cannot work full-time because of care duties [S10]; "their relative's allowance" because the allowance is paid to the person cared for, not the carer [S2]. The unchanged brief carries the money at stake, one grade worth over 4 times as much [S7]. The 374,000 figure stays in the body [S5]. No score, status, source, note or body sentence changed. Same date, owner-approved card: title "About 100,000 Czech family carers can't work full-time, and one assessment sets their relative's allowance" became "Czech families caring for a sick relative can miss out on state money in a confusing claim"; brief "One grade higher can pay an adult over 4 times as much a month [S7]. Free advisers help families appeal, but no Czech company handles the whole claim for a fee [S6,S9]." became "A home visit sets the grade, and one grade higher can pay over 4 times as much a month [S7]. Guides describe the process as bureaucratic and opaque [S3]."; solution "Build an online service that files a family's care-allowance claim, prepares them for the assessment and runs any appeal." became "Build an online service that files a family's care-allowance claim, prepares them for the home visit and handles any appeal."; good_for "Someone who'd like to work with families caring for a relative." became "Someone who'd like to help families caring for a sick or elderly relative.". Two words of the approved draft were corrected before writing because no source backs them: "a social worker's home visit" became "a home visit" (S3 documents a home assessment; who performs it is not on file), and "Families describe the process" became "Guides describe the process" (S3 is a sweep of advice articles and government pages, not families' own words).

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the three sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the claim a family has to win, with the recipient count, the four grades and the "bureaucratic and opaque" finding as its items [S2,S3,S5,S7]. Competition opens on the free help and the missing paid service, and describes pece.cz, Rodinný průvodce, Moravskoslezský kruh, Chytrá Péče and Dostupný advokát by what each does, leaving their names, owners, prices and customer counts to their `locals[]` rows [S6,S9]. Why now opens on the money a family loses on too low a grade, with the grade amounts, the Commission's 100,000 carers and the 8.3 against 28.8 percent home-care share as its items, and the raises and the bill below as dated bullets [S2,S7,S8,S10]. Willing to pay answers that no family is known to pay yet, then holds the law firm's fixed-price consultations, the 41.3bn CZK paid out in 2024 and the ministry's IT framework [S4,S5,S9]. Validated abroad lost the ledger name Oma Care for a description; CareOasis, not on the ledger, stays named [S1]. The moves lost every [Sn] marker and figure for links, and the move-only facts now live in their sections: the free services' limits in Competition and their rows [S9], the adult grade amounts in Why now [S7], the recipient count and the spend under The opportunity and Willing to pay [S5], and the law firm's price and customer count in its row [S9]. Move 1 now builds the home-assessment guide (it was move 2); the old move 1, taking the cases the free services turn away, is move 2 and now contacts them. `entry.why` was rewritten as "Easier: … Harder: …" and no longer names Rodinný průvodce, whose row carries it. Detail added from sources already on file, none of it new evidence: the four grades [S2]; the grade raise's Act number, both adult steps, both children's steps and the unchanged top two grades [S7]; MPs' bill of 17 March 2026 [S8]; the date of the Commission's report and the 2022 year of its spending figure [S10]; and the ministry's €74.7M framework and its related €19.8M and €65M notices, which the body had never cited [S4]. Grades are written as "the two lowest" and "the second" rather than in Roman numerals. Process block added (none before): the family files the claim at the labour office, goes through the assessment that sets the grade and appeals with a free adviser's help (all three change), and an unknown fourth step, how often a grade is appealed and how often an appeal wins; each drawn step is backed by S3, S6 or S9, and who carries out the assessment is not written in, because no source on file says. Corrected against the sources rather than against the old sentences: "Roughly 380,000 dependent Czechs" became 374,000 in December 2024, the figure the 2026-08-13 fact check and the statistics office confirm [S5]; "families deliver most of the care it funds, unpaid" and "usually an appeal" were cut, as the 2026-09-16 entry already found that no source on file measures the share of care families give or counts appeals, and the body now says "sometimes an appeal" and states only what S10 measures; "the way Oma Care charges US families for caregiver support and training" is not in S1 or its signal, which say only that it gets carers trained and paid, so the body now says how the US start-ups charge is not on file [S1]; "Validation is US-only" contradicted the ledger, which lists a British firm, so it was cut and the answer now says only what S1 and S9 support; "Nobody has built the layer that carries a family through it [S3]" moved to Competition, cited to the later paid-side check [S9]; and the insurer site's articles and advice column are now cited to S9, which lists them, rather than S6. Flagged as inference: that a family on too low a grade still gives the care with less state money, which rests on the grade amounts [S7]; that an insurer and a home-care firm could be a sales channel, which rests on S9 showing each already giving this help for free, and replaces the unsourced "Home-care providers and insurers are the channel"; that a flat or success fee is the model, which is our suggestion, not a source's; and, in move 2, that the free advisers would be glad to refer families on. No score, status, source, `note:`, `sources[]` order, entry level, title, brief, solution or good_for changed.
