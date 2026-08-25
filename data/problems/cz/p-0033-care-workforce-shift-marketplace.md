---
id: p-0033
region: cz
title: Czech care providers are short thousands of workers and fill shifts by overtime and
  word of mouth — no staffing marketplace serves care
category: health
geo: CZ-national
score: 6
scores:
  proof: 1
  money: 1
  urgency: 1
  demand: 2
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'A two-sided shift marketplace needs supply-side recruiting, qualification vetting
    under zákon 108/2006 Sb. and an agency-employment (agenturní zaměstnávání) licence or a
    clean worker-status answer before it scales; liquidity in one region comes before revenue.'
comps:
- name: ShiftKey
  url: https://www.shiftkey.com/
  geo: US
  since: 2016
  traction: '$300M raised at a valuation above $2B, led by Lorient Capital (Crunchbase News,
    Jan 2023); licensed professionals bid on per-diem shifts at 10,000+ healthcare facilities,
    skilled-nursing first'
- name: Florence
  url: https://www.florence.co.uk/
  geo: GB
  since: 2017
  traction: '£28.5M ($35M) Series B led by AXA Venture Partners (company, Jun 2022); 90,000
    care professionals and 2,000+ care organisations; shift-matching plus training'
sources:
- type: arbitrage
  name: "ShiftKey"
  why: "The US proof at scale: licensed health workers bid on per-diem shifts at 10,000+ facilities, $300M raised at a valuation above $2 billion."
  url: https://news.crunchbase.com/health-wellness-biotech/employment-shiftkey-fundraise/
  note: 'ShiftKey (Dallas, founded 2016) raised $300M led by Lorient Capital at >$2B valuation,
    announced 2023-01-11; skilled-nursing and long-term-care facilities are the core market.
    US-only, so proof stays 1 despite the scale — no CEE-adjacent analog is on file.'
  date: '2023-01-11'
- type: arbitrage
  name: "Florence"
  why: "The UK version for exactly this buyer: care homes fill shifts directly from 90,000 vetted professionals, cutting out agency mark-ups, with training bundled in."
  url: https://www.florence.co.uk/resources/blog/series-b
  note: 'Florence (London, founded 2017 by an NHS doctor) raised £28.5M ($35M) Series B led by
    AXA Venture Partners, 2022-06-01; 90,000 care professionals, 2,000+ care organisations,
    100,000 e-learners per the company announcement. Verified 2026-08-25. Second market, still
    not DE/AT/PL/Nordics: proof 1.'
  date: '2022-06-01'
- type: complaint
  name: "APSS ČR — the staffing-shortage survey"
  why: "More than 3,000 workers are missing in Czech social services and over half of 625 surveyed facilities report shortage — and the gap deepened between 2023 and 2025."
  url: https://www.apsscr.cz/asociace/aktuality/nedostatek-pracovniku-v-socialnich-sluzbach-se-mezi-lety-2023-a-2025-prohloubil
  note: 'APSS ČR survey run 14–26 Jan 2025, 625 facilities responding. Verbatim: "Aktuálně v
    sociálních službách chybí více než 3 000 pracovníků, přičemž nedostatek pracovníků hlásí
    více než polovina organizací." Article undated on page; survey close date used. Recurring
    survey (2023 → 2025 comparison) — documented industry pressure.'
  date: '2025-01-26'
  dims: [demand]
- type: hiring
  name: "Labour Office — July 2026 nurse hiring wave"
  why: "262 employers posted 380 new general-nurse vacancies through the Labour Office in one month, an annualised wage floor of €10.8 million — the shortage, measured monthly."
  url: https://data.mpsv.cz/od/soubory/volna-mista-prirustek/
  note: 'mpsv-2026-07-health-care: 380 new general-nurse vacancies across 262 employers (651
    seats), July 2026, annualised wage floor €10,838,685 — among the first records of the
    hiring ledger. Sibling single-employer aggregates: mpsv-2026-07-26871068-health-care
    (7 specialist-nurse postings, 51 seats) and mpsv-2026-07-03593207-health-care (11
    practical-nurse postings). Hiring evidence backs demand and money, never proof.'
  date: '2026-07-31'
  signal: mpsv-2026-07-health-care
  dims: [demand, money]
- type: statistic
  name: "MPSV/ÚZIS long-term-care prediction"
  why: "Roughly 34,700 new long-term-care beds are needed by 2035 — every one of them staffed, in a sector already 3,000 workers short."
  url: https://mpsv.gov.cz/predikce-potreb-dlouhodobe-pece-cesko-ceka-jeden-z-nejvetsich-ukolu-pristich-desetileti
  note: 'civic-mpsv-ltc-predikce-2035: MPSV/ÚZIS models, published 2025-11-14 — residential
    clients 93,536 → 135,624 and beds 76,761 → 111,503 by 2035. The demand side of the
    workforce gap is structural, not cyclical.'
  date: '2025-11-14'
  signal: civic-mpsv-ltc-predikce-2035
  dims: [demand]
- type: regulation
  name: "Social services amendment 92/2026 Sb."
  why: "Since 1 July 2026 care services may take on routine health-adjacent tasks — widening what a qualified flexible worker may legally cover per shift."
  url: https://e-sbirka.gov.cz/sb/2026/92
  note: 'reg-soc-sluzby-92-2026: zákon č. 92/2026 Sb., main provisions in force 1 Jul 2026 —
    pečovatelské services may help with medication (without breaking skin integrity) and
    stoma/urine-bag handling. In force and applied; treated here as a widening of the
    qualified-work pool per shift, not as a compliance deadline forcing this product.'
  date: '2026-07-01'
  signal: reg-soc-sluzby-92-2026
- type: tender
  name: "Královéhradecký kraj — personal-assistance development (€2.19M)"
  why: "A region is paying €2.19 million to develop personal-assistance capacity — public money already flows into getting more care hours delivered."
  url: https://ted.europa.eu/en/notice/-/detail/14888-2026
  note: 'ted-14888-2026: Královéhradecký kraj tender, 2026-01-12, €2,189,774, development of
    personal assistance services in the region. Relevant public money for care capacity;
    adjacent to a staffing product, so money held at 1, not 2.'
  date: '2026-01-12'
- type: gap-check
  name: "Market scan — who fills a care shift"
  why: "Czech searches found scheduling software for staff a provider already employs, a hospitality-born gig app, an events crew platform and classic agencies — no marketplace matching vetted care workers to facility shifts."
  url: https://www.grason.cz/
  note: 'Checked 2026-08-25: two Czech-language searches for care/nursing shift marketplaces.
    Found: Směny.cz and Chytrá organizace (internal shift planning), VeruApp (care-agency ops,
    the p-0011 incumbent), Grason (shift-work marketplace grown out of hospitality staffing —
    a healthcare or social-care vertical could NOT be confirmed on its site, which loads
    client-side; claim left open rather than asserted), Domelie (household caregivers for
    families, B2C), classic staffing agencies (e.g. Zdravotní sestry a pečovatelky s.r.o.)
    placing employees, not shifts. Own funded ledger holds cz-onsinch — a Czech workforce
    platform for EVENT crew staffing — adjacent model, not care. POSITIVE CONTROL passed:
    the same method surfaced Ringil at the top of its own Czech query. One-pass search only,
    and Grason''s verticals unresolved: gap stays 1, not 2.'
  date: '2026-08-25'
  queries:
    - 'aplikace platforma směny brigády pečovatelé zdravotní sestry "sociální služby" marketplace Česko'
    - '"zdravotní sestra" OR pečovatelka najdi směnu aplikace přivýdělek nemocnice domov seniorů platforma flexibilní směny'
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-23'
created: '2026-08-25'
updated: '2026-08-25'
---

Czech social services are short more than 3,000 workers, and over half of 625 surveyed facilities report unfilled positions [S3]. In July 2026 alone, 262 employers posted 380 new general-nurse vacancies through the Labour Office [S4]. Providers cover the holes with overtime, agency mark-ups and word of mouth; every shift that stays empty is care not delivered.

Why now: the demand side is structural — the ministry's models add roughly 34,700 long-term-care beds by 2035, each needing staff [S5]. Since 1 July 2026, care services may legally take on routine health-adjacent tasks such as medication help, widening what a qualified flexible worker can cover in a shift [S6]. And regions are already paying to develop care capacity outright [S7].

Who pays: care providers pay per filled shift, out of the agency mark-up they already pay today. The July 2026 nurse postings alone carry an annualised wage floor of €10.8 million [S4] — a fraction of that flow, taken as a matching fee, is the business. Workers come for the flexibility premium; regional buyers show public money reaches care capacity too [S7].

Existing non-solutions: Czech tooling plans the staff a provider already employs — Směny.cz, Chytrá organizace and VeruApp schedule internal shifts [S8]. Grason runs a shift marketplace grown out of hospitality, with no healthcare vertical visible on its site; OnSinch staffs event crews; Domelie brokers household caregivers; classic agencies place full-time employees [S8]. Nobody matches vetted care workers to facility shifts on demand [S8].

Solved elsewhere: ShiftKey (US) raised $300M at a valuation above $2 billion letting licensed professionals bid on per-diem shifts at more than 10,000 facilities, skilled nursing first [S1]. Florence (GB, £28.5M Series B) runs shift-matching plus training for 90,000 care professionals and 2,000+ care organisations [S2]. Both monetize the spread agencies charge today; neither operates in Central Europe [S1,S2].

## Revisions

2026-08-25 · record created — Minted from the first records of the hiring ledger (July 2026 Labour Office aggregates [S4]) joined with the APSS staffing survey [S3] and the elder-care sweep's regulation and capacity evidence [S5,S6]. Hiring evidence backs demand and money, never proof; proof rests on the US and GB comparables alone [S1,S2] and stays at 1 with no DE/AT/PL/Nordics analog on file. Grason's possible healthcare vertical could not be confirmed and is recorded as unresolved rather than asserted either way [S8].
