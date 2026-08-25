---
id: p-0027
region: cz
title: Complaints about Czech consumer loans have quadrupled, all handled by hand
fix: 'Case software for lenders answering complaints at the Financial Arbitrator: pull the
  loan file, draft the response, hold every deadline, and flag which cases to settle.'
category: fintech
geo: CZ-national
score: 6
scores:
  proof: 2
  money: 0
  urgency: 1
  demand: 2
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Respondent-side dispute-workflow software needs no licence — a dev plus a consumer-credit lawyer can pilot with one non-bank lender facing the ~20,000-filing wave and 167-day proceedings.'
comps:
- name: ClaimSorted
  url: https://www.claimsorted.com/
  geo: GB
  since: 2024
  traction: '$13.3M seed led by Atomico (Forbes, 2025); 20+ insurer clients across US/UK/EU; tech-enabled claims TPA'
  signal: yc-claimsorted
  markets: [US]
- name: Casap
  url: https://www.casaphq.com/
  geo: US
  since: 2023
  traction: '$25M Series A led by Emergence at $105M valuation (BusinessWire, 2025); automates bank and credit-union payment-dispute lifecycle'
- name: Audun
  url: https://www.getaudun.com/
  geo: NO
  since: 2026
  traction: 'YC S26, 4-person Oslo team (YC directory, 2026); AI-native debt collection; no public funding or customer figures yet'
  signal: yc-audun
locals:
- name: aCompliance
  url: https://www.acompliance.cz/klienti/nebankovni-poskytovatele-uveru/
  status: early
  evidence: 'EARLY on receipts only — the closest Czech offering, marketing the handling of
    client complaints and out-of-court disputes at the financial arbiter to non-bank lenders,
    but sold as a service with no product behind it; no customer count, no public-buyer pair
    in data/lookup/cz-contract-parties.jsonl, no round and no state listing on file [S5]'
- name: ePohledávky.cz (SoftGate Systems)
  url: https://www.epohledavky.cz/
  ico: '28859685'
  since: 2013
  status: early
  evidence: 'EARLY for this space — a receivables and collections platform, automating the creditor
    pursuing the debtor rather than the creditor defending a consumer claim [S5]; ARES
    registration 2013-01-01. No limb of the established test is met by anything on file
    here: nothing names who has bought it, no published tally exists, there is no pairing in
    data/lookup/cz-contract-parties.jsonl, no round at Series stage, and no state listing.'
- name: Barrister (ASW)
  url: https://www.asw.cz/
  status: early
  evidence: 'EARLY on receipts only — collections and receivables software on the pursuit side
    of the same relationship [S5]; no customer count, public-buyer pair, round or state listing
    on file'
- name: SingleCase
  url: https://www.singlecase.cz/
  status: early
  evidence: 'EARLY on receipts only — law-practice case management, generic firm tooling with
    no financial-arbiter docket in it [S5]; no customer count, public-buyer pair, round or
    state listing on file'
- name: Aptien
  url: https://www.aptien.com/
  ico: '26397668'
  since: 2005
  status: early
  evidence: 'EARLY for this space — generic case and record management with no financial-arbiter docket
    in it [S5]; ARES registration 2005-08-30. No limb of the established test is met by
    anything on file here: nothing names who has bought it, no published tally exists, there
    is no pairing in data/lookup/cz-contract-parties.jsonl, no round at Series stage, and no
    state listing.'
sources:
- type: complaint
  name: "Financial arbiter — 2025 annual report"
  why: "The caseload receipt: 2,660 new proceedings in 2023, 5,683 in 2024, 12,050 in 2025 and 8,200 more filed by May 2026, with consumer credit at ~92% of the running docket and proceedings averaging 167 days."
  url: https://finarbitr.gov.cz/cs/informace-pro-verejnost/aktuality/vyrocni-zprava-financniho-arbitra-za-rok-2025-425.html
  note: 'fa-spotrebitelske-uvery: the financial arbiter''s 2025 annual report documents 12,050
    new proceedings in 2025 (vs 5,683 in 2024 and 2,660 in 2023, +113% YoY), consumer-credit
    disputes at ~92% of the 15,446 running proceedings, 8,200 new filings by the May 2026
    report date (~20,000 projected for 2026), average proceeding 167 days, 83% of concluded
    cases settled. Creditworthiness-assessment (úvěruschopnost) claims dominate — a mass-scale
    claims industry is industrializing filings.'
  date: '2026-05-29'
  signal: fa-spotrebitelske-uvery
- type: complaint
  name: "MPO — consumer policy progress report"
  why: "A second official count: ~18,700 financial-arbiter filings between 2020 and mid-2025, inside 45,000+ out-of-court dispute filings across sectors. The caseload is structural, not a one-year spike."
  url: https://mpo.gov.cz/assets/cz/ochrana-spotrebitele/aktualni-informace/2026/3/Zprava-o-prubeznem-plneni-Strategie-spotrebitelske-politiky-2025.pdf
  note: 'mpo-adr-vyuziti: MPO''s consumer-policy progress report tabulates ~18,700 financial-arbiter
    filings 2020-H1/2025 (consumer credit, strongly rising) within 45k+ out-of-court dispute
    filings across sectors — a second official receipt that the caseload is recurring and
    structural, not a one-year spike. Demand scored 2: recurring documented dispute volume
    in two independent official sources.'
  date: '2026-03-31'
  signal: mpo-adr-vyuziti
- type: arbitrage
  name: "ClaimSorted"
  why: "A YC-backed London company productising claims processing for insurers — with Audun's AI debt collection in Norway, the nearest funded model to lender-side dispute operations, and still one vertical away."
  url: https://www.ycombinator.com/companies/claimsorted
  note: 'yc-claimsorted: ClaimSorted (YC S24, London) productizes claims processing for insurers;
    the funded claims-operations cluster (Avallon AI, Basepilot, Amera in US insurance; Audun,
    YC-backed AI-native debt collection in Norway) proves AI dispute/claims ops in adjacent
    verticals. No funded analog found for consumer-credit dispute operations specifically
    — proof scored 1 (weak adjacent analogs only).'
  date: '2026-08-13'
- type: gap-check
  name: "Czech dispute-tooling scan (first pass)"
  why: "Searches returned the arbiter's own information pages, consumer advisories and law firms handling cases by hand — no Czech product for lender-side dispute response was found."
  url: https://finarbitr.gov.cz/cs/informace-pro-verejnost/caste-otazky.html
  note: 'Gap check 2026-08-13: searches return only the arbiter''s own information pages,
    consumer advisories (obcanskeporadny.cz, dostupnyadvokat.cz) and law firms handling cases
    manually; no CZ product for lender-side dispute response, FA-docket management or settlement
    workflow was found. Gap 1 (quick search, no CZ player found).'
  date: '2026-08-13'
- type: gap-check
  name: "aCompliance and the Czech respondent-side field"
  why: "A deeper Czech sweep: receivables platforms point the other way, law-practice case management carries no arbiter docket, and aCompliance handles arbiter disputes as a service rather than a product."
  url: https://www.acompliance.cz/klienti/nebankovni-poskytovatele-uveru/
  note: 'Gap re-check 2026-08-20: NOT FOUND, score unchanged. Looked for a Czech product on
    the respondent side — dispute-response workflow for lenders, docket management against
    the financial arbiter, settlement decisioning. Nearest CZ supply is adjacent and points
    the other way: receivables and collections platforms (eDebit, ePohledávky.cz by SoftGate
    Systems, Evolio, Barrister by ASW) automate the creditor pursuing the debtor, not the
    creditor defending a consumer claim; law-practice case management (SingleCase, LegiSpace,
    Aptien) is generic firm tooling with no arbiter docket in it. The one offering aimed
    squarely at this need is a service, not a product — aCompliance markets handling of client
    complaints and out-of-court disputes at the financial arbiter to non-bank lenders. Our
    own funded ledger holds no CZ entrant either: the dispute cluster in it is the demand
    evidence plus foreign analogs. IMPORTANT: this is a not-found, not a proven absence, and
    per the register rule a negative never raises a gap score. Gap stays 1 with its coverage
    now recorded. Method control passed first at Wultra (p-0017) and Softlink (p-0026).'
  date: '2026-08-20'
  queries:
    - "software pro správu sporů finanční arbitr nebankovní poskytovatel úvěru reklamace klientů systém"
    - "český software správa právních sporů case management pro právní oddělení bank a věřitelů"
    - "software pro vymáhání a správu pohledávek spotřebitelské úvěry Česko platforma věřitelé"
    - "software evidence stížností a reklamací klientů banka pojišťovna poskytovatel úvěru Česko systém"
    - "Czech software lender-side complaint and dispute management financial arbiter consumer credit case workflow"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: regulation
  name: "VeKLEP — consumer credit act revision in draft"
  why: "The Finance Ministry is revising the Consumer Credit Act 257/2016 — the statute whose creditworthiness-assessment duties generate most of the arbiter's docket is itself being rewritten."
  url: https://odok.cz/portal/veklep/material/KORNDDVFVG8B/
  note: 'veklep-KORNDDVFVG8B: Finance Ministry draft amending zákon č. 257/2016 Sb. o
    spotřebitelském úvěru, in VeKLEP since 14 Feb 2025 (first VeKLEP harvest, 2026-08-25).
    Draft with no dated obligation on file: context receipt — the legal frame behind the
    dispute flood is in motion — backing no score dimension.'
  date: '2025-02-14'
  signal: veklep-KORNDDVFVG8B
  dims: []
created: '2026-08-13'
updated: '2026-08-25'
---

The Kancelář finančního arbitra — the out-of-court forum for consumer disputes with banks and non-bank lenders — is absorbing a caseload explosion: 2,660 new proceedings in 2023, 5,683 in 2024, 12,050 in 2025, and 8,200 already filed by the time the 2025 annual report was published in May 2026, projecting toward ~20,000 for the year [S1]. Roughly 92% of all running proceedings are consumer-credit disputes, dominated by claims that lenders failed to properly assess creditworthiness (úvěruschopnost) [S1].

Why now: the growth is industrial, not organic. The arbiter's own reporting describes claims driven at mass scale, which means every consumer lender in the market now faces a professionalized adversary filing standardized claims, while the average proceeding takes 167 days and 83% of concluded cases end in settlement [S1].

Who pays: non-bank lenders and banks first — each new case at the Financial Arbitrator demands document production, a legal position and a settlement decision, and at 2026 volumes that is tens of thousands of case-handling cycles a year across the sector [S1], run today by in-house legal departments and outside law firms by hand [S4]. The claimant side already has industrial tooling economics (standardized filings at scale) [S1]; the response side does not. The arbiter itself, drowning at 167 days per case [S1], is the third affected party and a plausible govtech buyer.

Existing non-solutions: manual legal departments, outsourced law firms billing per case, and the arbiter's static information pages [S4]. A 2026-08-13 market search found no Czech product for dispute-response operations, docket management against the FA, or settlement workflow — only information portals and services [S4].

Solved elsewhere: dispute handling is funded on both sides of the Atlantic, but only one of the three sellers has been at it long enough to prove anything. Casap has automated the bank payment-dispute lifecycle since 2023 and raised a $25M Series A at a $105M valuation [S3]. ClaimSorted opened in London in 2024 and handles claims for twenty-plus insurers on $13.3M; Audun is four people in Oslo building AI-native collections out of YC [S3]. So the proven model is Casap's, one vertical away in payments — nobody anywhere has been documented productising consumer-credit dispute response itself. The Czech arbiter's caseload is the same shape of work, still handled by hand, and the documented volume carries the case here more than the foreign template does.

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "each incoming FA proceeding" now reads "each new case at the Financial Arbitrator", and "external advokáti" now reads "outside law firms". Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: the first VeKLEP harvest put the Finance Ministry's pending revision of the Consumer Credit Act 257/2016 on the ledger as a context receipt [S6] — the statute generating the docket is being rewritten. No score moved by that pass. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 1 → 2. Casap passes the test outright — selling since 2023, so the three-year limb is met, on a $25M Series A at a $105M valuation — which is one established foreign player, rung 2. ClaimSorted and Audun do not: ClaimSorted opened in 2024 and Audun in 2026, both inside the three-year limb, so neither counts however well funded. Rung 3 was considered and declined: it needs establishment in two-plus markets with one CEE-adjacent, and Casap's United States is the only market with an established seller in it. `scores.gap` stays 1. The five Czech offerings the [S5] sweep found were lifted into a structured `locals[]` ledger and every one reads early on receipts — aCompliance sells the arbiter-dispute work as a service with no product behind it, ePohledávky.cz and Barrister automate the creditor pursuing the debtor rather than defending a claim, and SingleCase and Aptien are generic case management with no arbiter docket; none publishes a customer count, pairs with a public buyer in `data/lookup/cz-contract-parties.jsonl`, or carries a round or state listing. Early local players do not close a space, so gap does not fall to 0; and it does not rise to 2 either, because [S5] found local players rather than none. `score` 5 → 6. The two Proven-abroad paragraphs were merged into one. The first, "Solved elsewhere, weakly", asserted the old score in words — "no funded analog exists" — and, because it is not the literal lead-in, it was rendering inside the local-competition section rather than the foreign one. The merged paragraph keeps its honest limit intact: the only proven seller is one vertical away, and nobody anywhere has been documented productising consumer-credit dispute response. Avallon, Basepilot and Amera dropped out of the body with it; they remain in the [S3] source note, unedited. Money, urgency and demand untouched; no [Sn] marker moved.
2026-08-20 · evidence audit — Three legal-status claims removed, none of which the register ever checked. The arbiter's forum was described as mandatory: neither S1's note nor the underlying signal says so. The interest-voiding doctrine ("a failed assessment can void the credit contract's interest") is gone — the corpus records only that creditworthiness-assessment claims dominate the docket, nothing about the remedy. And "Free proceedings with no lawyer requirement remove any natural brake on volume": both procedural facts had no receipt. The caseload figures, the settlement rate and the proceeding length are unaffected; they are receipted [S1].
