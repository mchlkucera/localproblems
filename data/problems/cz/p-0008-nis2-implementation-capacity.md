---
id: p-0008
region: cz
title: 6,000+ Czech firms and municipalities must implement NIS2 security measures on rolling
  deadlines through late 2026-2027 and most lack the capacity — many don't know they're in
  scope
category: legal-compliance
geo: CZ-national
score: 7
scores:
  proof: 0
  money: 2
  urgency: 3
  demand: 2
  gap: 0
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Productised packages already sell off the shelf at ~91k CZK (Lexnova receipts), but
    the compelled-yet-unaware buyer base and IROP procurement channels make an outbound pilot-to-invoice
    cycle of months the honest default.'
comps:
- name: Secfix
  url: https://www.secfix.com/
  geo: DE
  since: 2021
  traction: '€10.2M Series A, Feb 2026 (Vestbee); hundreds of SMB customers across 15+ European
    countries (Tech Funding News, 2026)'
  signal: round-secfix
- name: Copla
  url: https://cyberupgrade.net/
  geo: LT
  since: 2023
  traction: '€6M Series A, Feb 2026, after €2.5M seed, Nov 2024 (Vestbee); NIS2/DORA/ISO 27001
    compliance automation, rebranded from CyberUpgrade (EU-Startups, 2026)'
  signal: round-copla
sources:
- type: regulation
  url: https://www.zakonyprolidi.cz/cs/2025-264
  note: 'reg-nis2-cz-zkb: Act No. 264/2025 Coll. (NIS2 transposition), effective 1 Nov 2025;
    registration with NÚKIB was due ~31 Dec 2025 and security measures must be implemented
    within 1 year of registration — most deadlines land Q4 2026 - H1 2027 (<18 months). Fines
    up to 2% of global turnover / CZK 250m.'
  date: '2026-12-31'
  signal: reg-nis2-cz-zkb
- type: complaint
  url: https://www.sme-union.cz/zakon-o-kyberneticke-bezpecnosti-plati-lhuty-bezi/
  note: 'SME UNION: 6,000+ firms affected across energy, manufacturing, food, logistics, digital
    services; many SMEs still unaware they are in scope — documented association-level alarm
    about capacity and awareness.'
  date: '2026-12-31'
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/373331-2026
  note: 'ted-373331-2026: FN Motol + Homolka awarded ~€6.1M for cyber threat detection & response
    tooling (TED, Jun 2026); smaller hospital awards in the same window (Hustopeče ~€1.4M,
    Třebíč ~€1.2M, Národní knihovna ~€1.4M) show the buying pattern.'
  date: '2026-06-01'
  signal: ted-373331-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/472636-2026
  note: 'ted-472636-2026: Hl. m. Praha awarded ~€5.3M for a SIEM across MHMP, city police
    and districts (Jul 2026), plus ~€1.9M central cyber platform for městské části (ted-542109-2026,
    Aug 2026) — two security awards from one buyer in six weeks. Recurring public spend ≥5M
    CZK per award: money scored 2.'
  date: '2026-07-09'
  signal: ted-472636-2026
- type: regulation
  url: https://rowan.legal/aktualne/cr-novy-zakon-o-kriticke-infrastrukture-je-ucinny/
  note: 'reg-cer-zakon-266: zákon č. 266/2025 Sb. (CER transposition) — critical-entity designations
    by 17 Jul 2026, resilience plans and incident reporting through 2026–2027; the same under-capacity
    entities now owe a parallel physical-resilience stack, compliance cost estimated in tens
    of millions CZK per firm (PORTOS).'
  date: '2026-07-17'
  signal: reg-cer-zakon-266
- type: contract
  url: https://smlouvy.gov.cz/smlouva/39084314
  note: 'hlidac-39084314: město Český Brod (~7k inhabitants) signed ''Kybernetická bezpečnost
    města'' for ~9.0M CZK (registr smluv, 11 Aug 2026); 341 cyber contracts in registr smluv
    since June, incl. NPO výzva č. 41 subsidy-funded audits (ZZS Středočeského kraje, Jaroměř)
    — the small-municipality tier is buying and a subsidy stream funds it, answering this
    record''s open follow-up on NPO funding.'
  date: '2026-08-11'
  signal: hlidac-39084314
- type: contract
  url: https://smlouvy.gov.cz/smlouva/38911766
  note: 'hlidac-38911766: Domov pro seniory Napajedla ordered an ''NIS 2 package — cyber security''
    from Lexnova Energy (~91k CZK, Jun 2026); a second Lexnova package order followed within
    weeks (Zlín-region disability services, hlidac-38723900) and Týn nad Vltavou bought a
    NIS2 scope analysis (hlidac-38370127) — the smallest obligated tier is buying productised
    compliance packages off the shelf. The 2026-08-13 TED run adds scale: ~77 cyber-security
    records from ~45 distinct public buyers (~€33M) in the Jun–Aug window alone.'
  date: '2026-06-22'
  signal: hlidac-38911766
- type: subsidy
  url: https://smlouvy.gov.cz/smlouva/38438158
  note: 'hlidac-38438158: Boskovice paid enovation to write its IROP 21-27 call No. 120 ''Cyber
    security'' subsidy application (~121k CZK, Jun 2026) — one of a grant-application cluster
    with České Budějovice (hlidac-38351500, incl. mandatory OHA/Archimate paperwork) and PN
    Jihlava (hlidac-38824338). A dedicated EU subsidy channel funds the municipal compliance
    market, and towns pay consultants just to enter the queue.'
  date: '2026-06-19'
  signal: hlidac-38438158
created: '2026-08-13'
updated: '2026-08-19'
---

Czech Act No. 264/2025 Coll. transposes NIS2 and pulls 6,000+ firms and municipalities into a regulated cybersecurity regime — energy, manufacturing, food, logistics and digital services among them. Registration with NÚKIB was due by roughly the end of 2025; security measures must be implemented within one year of registration, so the compliance wall lands on rolling deadlines from Q4 2026 through H1 2027. SME UNION documents that many affected SMEs are still unaware they are in scope at all.

Why now: the one-year implementation clocks are running, the implementing decrees (e.g. Vyhláška 409/2025 for the higher-obligations regime) are in force, and fines reach 2% of global turnover or CZK 250m. For a typical in-scope SME or small municipality there is no internal security function to absorb the work.

Who pays: the regulated entities themselves — SMEs and municipal IT budgets buying gap analyses, ISMS implementation, incident-reporting workflows and ongoing managed security (vCISO). The buyer is compelled, not persuaded: this is one of the cases where the compliance burden itself is the problem.

Existing non-solutions: the supply side exists (security consultancies, MSPs) but is a fragmented services market with no evidence of productized, SME-priced NIS2 compliance at the scale of 6,000 obligated entities; no arbitrage/gap search was run this cycle, so those dimensions score 0 rather than being asserted.

Money is now receipted from the first successful TED run (2026-08-13): hospitals and municipalities placed at least five cyber-security awards between June and August 2026, from Motol's ~€6.1M detection-and-response buy to Prague's ~€5.3M SIEM — recurring spend, multiple buyers, values above the 5M CZK bar. The demand side also widened: zákon č. 266/2025 Sb. (CER transposition) puts a parallel physical-resilience compliance stack on an overlapping entity set, with designations landing July 2026 and plan obligations running through 2027.

Updated 2026-08-13: the buying wave now runs the full size spectrum. TED shows ~77 cyber records from ~45 public buyers (~€33M) between June and August 2026; below the threshold, care homes and small towns order productised "NIS 2 packages" from Lexnova Energy repeatedly, Týn nad Vltavou paid to find out which parts of it are even regulated, and an IROP call-120 subsidy channel funds municipal projects — with towns hiring consultants just to write the applications. Note for the gap dimension: Lexnova's repeat package sales and Institut kybernetické bezpečnosti's scope-analysis product are evidence that productised CZ offerings for the small-entity tier are emerging — the supply side is no longer only fragmented consulting.

A structured gap check on productized CZ NIS2 offerings at the 6,000-entity scale is still the missing dimension; with money, deadline and demand all receipted and first productised sellers named, gap evidence is what separates this from newsletter-lead territory.

## First moves

1. Sell where buying is receipted: call social-care institutions and towns in the ~7k-inhabitant tier first — Domov pro seniory Napajedla bought a ~91k CZK "NIS 2 package" off the shelf (with a repeat Lexnova order in the Zlín region weeks later), Týn nad Vltavou paid just to learn its scope, Český Brod signed ~9.0M CZK for municipal cyber security, and 341 cyber contracts sit in registr smluv since June.
2. Build the productised implementation-gap package first: fixed-price mapping of one entity's state against Act 264/2025 and Vyhláška 409/2025 obligations, keyed to the one-year post-registration clock (deadlines rolling Q4 2026 – H1 2027, fines up to 2% of global turnover / CZK 250m) — the packaged, off-the-shelf form is what the smallest obligated tier demonstrably buys.
3. Ride the subsidy channel: [IROP 120 Kybernetická bezpečnost II](/sources/tenders#dotace-irop-120-kyberbezpecnost) — 2.44bn CZK (~€99.6M) for municipalities, regions and hospitals regulated under 264/2025, applications open **30.4.2026–17.12.2026**; towns already pay consultants just to write these applications (Boskovice paid enovation ~121k CZK), so application-writing plus implementation is a subsidy-funded entry offer. Builder-side, [HORIZON-CL3-2026-02-CS-ECCC](/sources/tenders#dotace-horizon-eccc-cyber-2026) (€56.2M, consortia, deadline **2026-09-15**) funds security tooling development itself.
4. Close the record's own missing dimension before committing: run the structured gap check on productised CZ NIS2 offerings at the 6,000-entity scale — Lexnova Energy's repeat packages and Institut kybernetické bezpečnosti's scope-analysis product already show the supply side is no longer only fragmented consulting, so verify whether the small-entity tier is genuinely underserved or merely early.
5. Same buyer, second product: zákon č. 266/2025 Sb. (CER) puts a parallel physical-resilience stack on an overlapping entity set — designations by 17 Jul 2026, resilience plans and incident reporting through 2026–2027, compliance cost estimated in tens of millions CZK per firm (PORTOS) — package it as the natural upsell to every NIS2 customer.
6. Competition on file: **Lexnova Energy** (repeat productised NIS 2 packages), **Institut kybernetické bezpečnosti** (scope-analysis product), **enovation** (subsidy-application consulting) and the fragmented security-consultancy/MSP field; foreign comps Secfix (€10.2M Series A) and Copla (€6M Series A, NIS2/DORA) prove the compliance-automation model abroad, while the structured CZ gap check remains open.
