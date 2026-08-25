---
id: p-0004
region: cz
title: Families caring for ~380,000 dependent Czechs must obtain and defend příspěvek na péči
  through an opaque, bureaucratic process
fix: 'A guided service that gets a family through the Czech care allowance (příspěvek na
  péči) — the application, the assessment visit and the appeal — for a flat or success
  fee.'
category: health
geo: CZ-national
score: 6
scores:
  proof: 1
  money: 1
  urgency: 1
  demand: 1
  gap: 2
status: candidate
build:
  capital: kiosk
  first_revenue: weeks
  builder: small-team
  note: 'A guided claim-and-appeal tool over public MPSV rules is solo-dev cheap and families
    pay flat or success fees immediately, but credible hodnocení stupně závislosti guidance
    needs a social-benefits practitioner alongside the dev.'
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
sources:
- type: arbitrage
  name: "Oma Care"
  why: "A two-person YC W24 team enrolling US family caregivers into Medicaid programmes that pay them up to $28 an hour — the template for getting families money they are already owed."
  url: https://www.ycombinator.com/companies/oma-care
  note: 'yc-oma-care: Oma Care (YC W24) builds infrastructure to train and get family caregivers
    paid (53M caregivers in the US); CareOasis (YC S23) is the same model — a validated US
    cluster. US-only, scored as one analog.'
  date: '2026-08-13'
  signal: yc-oma-care
- type: subsidy
  name: "Příspěvek na péči"
  why: "The Czech care allowance itself — four dependency levels, raised again in 2024-25, and the money a family wins or loses on how well it files."
  url: https://www.ycombinator.com/companies/oma-care
  note: Signal note references příspěvek na péči — four levels, raised again in 2024-25, flowing
    to ~380k dependent persons — the state benefit program the product would help families
    access.
  date: '2026-08-13'
- type: gap-check
  name: "First Czech market scan"
  why: "An early sweep that returned only advice articles and government pages, and documented the application, assessment and appeal as bureaucratic and opaque."
  url: https://www.ycombinator.com/companies/oma-care
  note: 'Absence check 2026-08-13: searches return only advice articles and government pages
    (pece.cz, mpsv.gov.cz); no player that files, tracks or optimizes claims for families.
    Demand point: signal documents that application, hodnocení stupně závislosti and appeals
    are bureaucratic and opaque.'
  date: '2026-08-13'
- type: tender
  name: "TED — MPSV 'IT delivery III' framework (~€74.7M)"
  why: "The ministry budgets tens of millions of euros a year for benefits back-office IT, while nothing is built on the side the citizen actually touches."
  url: https://ted.europa.eu/en/notice/-/detail/402149-2026
  note: 'ted-402149-2026 (context): MPSV ''IT delivery III'' framework ~€74.7M plus a dozen
    related awards (EKIS III ~€19.8M open, OKaplikace ~€65M) in Jun–Aug 2026 — the state demonstrably
    budgets tens of millions EUR/yr for benefits back-office IT while the citizen-facing navigation
    layer stays unbuilt. Adjacent spend: kept at money=1, not 2.'
  date: '2026-06-11'
- type: statistic
  name: "ČSÚ — the care allowance in numbers"
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
  why: "MPs filed a bill amending both the Social Services Act 108/2006 (the příspěvek na péči law) and the disability-benefits act 329/2011 — the rules families navigate are in motion again."
  url: https://odok.cz/portal/veklep/material/ALBSDS9BKZY8/
  note: 'veklep-ALBSDS9BKZY8: MPs'' bill no. 125 (Juchelka, Pastuchová, filed 17 Mar 2026)
    amending zákon č. 108/2006 Sb. — the act příspěvek na péči lives in — together with zákon
    č. 329/2011 Sb. o dávkách pro osoby se zdravotním postižením. Draft with no dated
    obligation: context receipt only, backs no score dimension.'
  date: '2026-03-17'
  signal: veklep-ALBSDS9BKZY8
  dims: []
created: '2026-08-13'
updated: '2026-08-25'
---

Roughly 380,000 dependent persons in Czechia receive příspěvek na péči [S2], and the care it funds is largely delivered informally by family members [S1]. To get the benefit — and the correct level of it — families must navigate the application, the hodnocení stupně závislosti assessment, and frequently appeals, in a process the evidence on file characterizes as bureaucratic and opaque [S3]. Families that misnavigate it leave state money on the table while providing the care anyway.

Why now: benefit levels keep rising — after the 2024-25 increases [S2], grades I and II rose again from 1 January 2026, adult grade I from 880 to 1,300 CZK monthly [S7] — increasing the money at stake per claim while the navigation layer remains nonexistent [S3]. Demographic aging steadily grows the claimant pool.

Who pays: families themselves (success-fee or flat-fee help with the claim, subscription support and caregiver training), the way Oma Care charges US families for caregiver support and training [S1]. Downstream, home-care providers and insurers are plausible channel partners since properly funded clients can afford services.

Existing non-solutions: static information portals (pece.cz, mpsv.gov.cz guides) [S3] and word-of-mouth from social workers. No Czech company files, tracks or optimizes claims for families [S3] — a finding a later market search confirmed and sharpened. Help exists, but as free social counselling rather than product: pece.cz, run by NN Životní pojišťovna, carries an entitlement calculator and a poradna, and registered odborné sociální poradenství services draft appeals for families [S6].

Solved elsewhere: Oma Care (YC W24) and CareOasis (YC S23) form a validated US cluster around getting family caregivers trained and paid from state programs [S1]. Validation is US-only so far; the money in the problem is the příspěvek na péči program itself [S2].

## Revisions

2026-08-13 · fact check — The recipient figure should read 374,000 (Dec 2024, ČSÚ/MPSV), with 41.3 bn CZK paid through the benefit in 2024 [S5]; the ~380k figure in this record is slightly above the latest confirmed official number. Source: https://csu.gov.cz/produkty/prispevek-na-peci-loni-vyuzivalo-vice-nez-370-tisic-lidi

2026-08-20 · evidence audit and title sweep — Two blocks recorded on this date, merged here. The fact check above is verified: the ČSÚ release of 2025-11-14 states "V prosinci 2024 pobíralo příspěvek na péči již 374 tisíc osob" and 41,3 mld. Kč paid out through the benefit in 2024, so both its figures check out against the primary source, which is now on the ledger as [S5]. Separately, the title claimed families have "no help beyond static info portals". The 2026-08-20 gap re-check found otherwise and the body says so: pece.cz carries an entitlement calculator and a poradna, and registered odborné sociální poradenství services draft appeals [S6]. What is absent is a product that files, tracks or optimizes a claim — which is what gap 2 records — not all help. The overstated clause is gone; the gap score is untouched.

2026-08-25 · regulation added — The 2026 care-allowance raise entered the evidence ledger (zákon č. 360/2025 Sb.: grades I/II up from 1 Jan 2026) and now receipts the why-now claim directly [S7], replacing the second-hand S2 note as its source. Scores unchanged. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "monetizes caregiver enablement" now reads "charges US families for caregiver support and training". Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: the first VeKLEP harvest put MPs' bill 125 on the ledger — it amends both framework acts behind the benefit (108/2006 and 329/2011) [S8]. A draft with no dated obligation: context only, no score moved.
