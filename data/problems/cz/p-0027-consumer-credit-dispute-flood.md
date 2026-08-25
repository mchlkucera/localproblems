---
id: p-0027
region: cz
title: Consumer-credit disputes at the Czech financial arbiter quadrupled in two years toward
  ~20,000 filings a year, and neither lenders nor the arbiter run anything but manual case
  handling
category: fintech
geo: CZ-national
score: 5
scores:
  proof: 1
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
created: '2026-08-13'
updated: '2026-08-25'
---

The Kancelář finančního arbitra — the out-of-court forum for consumer disputes with banks and non-bank lenders — is absorbing a caseload explosion: 2,660 new proceedings in 2023, 5,683 in 2024, 12,050 in 2025, and 8,200 already filed by the time the 2025 annual report was published in May 2026, projecting toward ~20,000 for the year [S1]. Roughly 92% of all running proceedings are consumer-credit disputes, dominated by claims that lenders failed to properly assess creditworthiness (úvěruschopnost) [S1].

Why now: the growth is industrial, not organic. The arbiter's own reporting describes claims driven at mass scale, which means every consumer lender in the market now faces a professionalized adversary filing standardized claims, while the average proceeding takes 167 days and 83% of concluded cases end in settlement [S1].

Who pays: non-bank lenders and banks first — each incoming FA proceeding demands document production, a legal position, and a settlement decision, and at 2026 volumes that is tens of thousands of case-handling cycles a year across the sector [S1], run today by legal departments and external advokáti by hand [S4]. The claimant side already has industrial tooling economics (standardized filings at scale) [S1]; the response side does not. The arbiter itself, drowning at 167 days per case [S1], is the third affected party and a plausible govtech buyer.

Existing non-solutions: manual legal departments, outsourced law firms billing per case, and the arbiter's static information pages [S4]. A 2026-08-13 market search found no Czech product for dispute-response operations, docket management against the FA, or settlement workflow — only information portals and services [S4].

Solved elsewhere, weakly: no funded analog exists for consumer-credit dispute operations specifically; the nearest proven models are AI claims-operations companies in insurance (ClaimSorted, Avallon, Basepilot, Amera) and AI-native debt collection (Audun, Norway) [S3]. This record is carried by its documented demand — the first Czech mover would be productizing a workflow that provably exists at scale rather than importing a proven product.

Solved elsewhere: dispute handling is funded on both sides of the Atlantic. Casap (US) raised a $25M Series A to automate the bank payment-dispute lifecycle, ClaimSorted (UK) raised $13.3M serving twenty-plus insurers as a tech-enabled claims handler, and Audun (Oslo) is building AI-native collections out of YC [S3]. The Czech arbiter's caseload is the same shape of work, still handled by hand.

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed.
2026-08-20 · evidence audit — Three legal-status claims removed, none of which the register ever checked. The arbiter's forum was described as mandatory: neither S1's note nor the underlying signal says so. The interest-voiding doctrine ("a failed assessment can void the credit contract's interest") is gone — the corpus records only that creditworthiness-assessment claims dominate the docket, nothing about the remedy. And "Free proceedings with no lawyer requirement remove any natural brake on volume": both procedural facts had no receipt. The caseload figures, the settlement rate and the proceeding length are unaffected; they are receipted [S1].
