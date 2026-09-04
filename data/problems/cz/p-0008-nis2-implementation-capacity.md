---
id: p-0008
region: cz
title: Six thousand Czech firms must meet new security rules, and most are not ready
category: legal-compliance
geo: CZ-national
score: 11
scores:
  proof: 3
  money: 2
  urgency: 3
  demand: 2
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Ready-made packages already sell at ~91k CZK a time (Lexnova receipts), so a small
    team can start as a service. The product demands Act 264/2025 and Vyhláška 409/2025
    expertise, ISMS and audit basics, and patient public-sector sales — pilot-to-invoice
    cycles with towns and hospitals run months.'
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
locals:
- name: NIS2 Průvodce
  url: https://nis2pruvodce.cz/
  ico: '88635783'
  since: 2025
  competes: direct
  maturity: early
  evidence: 'A full Czech platform at 3,000 CZK a month per company: twelve modules across
    vyhláška 409/2025 and 410/2025, an asset register, a 52-measure risk catalogue, a supplier
    register wired to the state business register, incident forms for the national cyber agency
    (NÚKIB) with their 24- and 72-hour deadlines, training and an AI assistant over the
    statute. It is run by one person, Ondřej Šitler, is not VAT-registered, sells against an
    obligation that only took effect in November 2025, and names nobody who has bought it.'
- name: Compligen
  url: https://www.compligen.cz/
  since: 2026
  competes: direct
  maturity: early
  evidence: 'An online guided generator producing 20+ documents against vyhláška 410/2025 for the
    lighter-obligations regime, 29,900 CZK one-off before VAT, with a page aimed at
    municipalities. Founder Lukáš Vencálek publishes no company number and no company of that
    trade name is on the state business register; its own reference line claims 30+ firem a
    obcí, while the product still carries a Q3 2026 roadmap.'
- name: NIS2 Doku
  url: https://nis2doku.cz/
  since: 2025
  competes: direct
  maturity: early
  evidence: 'A documentation pack — Start 4,900 CZK, Pro 11,900 CZK one-off before VAT, 10+
    documents per vyhláška 410/2025 plus Excel asset, incident and supplier tools — sold by
    David Mikulec against an obligation that took effect in November 2025. Nobody who has
    bought it is named.'
- name: Lexnova Energy
  url: https://www.lexnova.cz/
  ico: '22530649'
  since: 2025
  competes: direct
  maturity: early
  evidence: 'Sells a productised "NIS 2 package" at about 91k CZK a time, with repeat orders
    visible in the state contracts register. Lexnova Energy s.r.o. was incorporated in January
    2025 and the sibling Lexnova Services s.r.o. in July 2026, so the seller is younger than
    the obligation it packages.'
- name: ICZ Risk*Guide
  url: https://www.iczgroup.com/riskguide/
  ico: '25145444'
  since: 1997
  competes: adjacent
  maturity: established
  evidence: 'A modular information-security and risk-assessment platform deployed at the state
    digital agency (Digitální a informační agentura), the police presidium and the Plzeň city
    IT authority, put in over a one-to-three-month implementation with a 24/7 advisory service
    attached. It is a security programme bought as a project by ministries, regions, cities and
    large organisations — municipalities are among its buyers — rather than the fixed-price
    product a small obliged firm buys off a web page; ICZ a.s. has traded since July 1997 and
    the product is now sold by the group company ICZ.Services a.s. (IČO 22183809, incorporated
    October 2024).'
sources:
- type: regulation
  name: "Act No. 264/2025 Coll. (new cybersecurity act)"
  gist: "the law and its deadlines"
  why: "The Czech NIS2 transposition, effective 1 Nov 2025 — registration was due end-2025, security measures fall due within one year of registration, and fines reach 2% of global turnover or CZK 250m."
  url: https://www.zakonyprolidi.cz/cs/2025-264
  note: 'reg-nis2-cz-zkb: Act No. 264/2025 Coll. (NIS2 transposition), effective 1 Nov 2025;
    registration with NÚKIB was due ~31 Dec 2025 and security measures must be implemented
    within 1 year of registration — most deadlines land Q4 2026 - H1 2027 (<18 months). Fines
    up to 2% of global turnover / CZK 250m.'
  date: '2026-12-31'
  signal: reg-nis2-cz-zkb
- type: complaint
  name: "SME UNION — the deadlines are running"
  gist: "the 6,000-firm alarm"
  why: "The business association's alarm: 6,000+ firms affected across energy, manufacturing, food, logistics and digital services — and many SMEs still unaware they are in scope."
  url: https://www.sme-union.cz/zakon-o-kyberneticke-bezpecnosti-plati-lhuty-bezi/
  note: 'SME UNION: 6,000+ firms affected across energy, manufacturing, food, logistics, digital
    services; many SMEs still unaware they are in scope — documented association-level alarm
    about capacity and awareness.'
  date: '2026-12-31'
- type: tender
  name: "TED — Motol & Homolka award (~€6.1M)"
  gist: "the €6.1M hospital award"
  why: "Prague's biggest hospitals bought cyber threat detection and response for ~€6.1M in June 2026 — the top of the public buying wave, with smaller hospital awards in the same window."
  url: https://ted.europa.eu/en/notice/-/detail/373331-2026
  note: 'ted-373331-2026: FN Motol + Homolka awarded ~€6.1M for cyber threat detection & response
    tooling (TED, Jun 2026); smaller hospital awards in the same window (Hustopeče ~€1.4M,
    Třebíč ~€1.2M, Národní knihovna ~€1.4M) show the buying pattern.'
  date: '2026-06-01'
  signal: ted-373331-2026
- type: tender
  name: "TED — Prague SIEM award (~€5.3M)"
  gist: "the €5.3M city award"
  why: "The city of Prague bought a SIEM across the city hall, city police and districts — two security awards from one buyer in six weeks."
  url: https://ted.europa.eu/en/notice/-/detail/472636-2026
  note: 'ted-472636-2026: Hl. m. Praha awarded ~€5.3M for a SIEM across MHMP, city police
    and districts (Jul 2026), plus ~€1.9M central cyber platform for městské části (ted-542109-2026,
    Aug 2026) — two security awards from one buyer in six weeks. Recurring public spend ≥5M
    CZK per award: money scored 2.'
  date: '2026-07-09'
  signal: ted-472636-2026
- type: regulation
  name: "Act No. 266/2025 Coll. (critical infrastructure)"
  gist: "the parallel resilience law"
  why: "The CER transposition puts a parallel physical-resilience compliance stack on an overlapping entity set — designations from July 2026, resilience plans and incident reporting through 2027."
  url: https://rowan.legal/aktualne/cr-novy-zakon-o-kriticke-infrastrukture-je-ucinny/
  note: 'reg-cer-zakon-266: zákon č. 266/2025 Sb. (CER transposition) — critical-entity designations
    by 17 Jul 2026, resilience plans and incident reporting through 2026–2027; the same under-capacity
    entities now owe a parallel physical-resilience stack, compliance cost estimated in tens
    of millions CZK per firm (PORTOS).'
  date: '2026-07-17'
  signal: reg-cer-zakon-266
- type: contract
  name: "Registr smluv — Český Brod (~9M CZK)"
  gist: "the 9M CZK small town"
  why: "A town of 7,000 signed ~9M CZK for municipal cyber security — one of 341 cyber contracts in the contract registry since June 2026."
  url: https://smlouvy.gov.cz/smlouva/39084314
  note: 'hlidac-39084314: město Český Brod (~7k inhabitants) signed ''Kybernetická bezpečnost
    města'' for ~9.0M CZK (registr smluv, 11 Aug 2026); 341 cyber contracts in registr smluv
    since June, incl. NPO výzva č. 41 subsidy-funded audits (ZZS Středočeského kraje, Jaroměř)
    — the small-municipality tier is buying and a subsidy stream funds it, answering this
    record''s open follow-up on NPO funding.'
  date: '2026-08-11'
  signal: hlidac-39084314
- type: contract
  name: "Registr smluv — Lexnova 'NIS 2 package' (~91k CZK)"
  gist: "the 91k CZK package"
  why: "A care home bought a productised NIS2 package off the shelf, with a repeat order weeks later — the smallest obligated tier pays ~91k CZK a time for packaged compliance."
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
  name: "Registr smluv — Boskovice grant application (~121k CZK)"
  gist: "the paid grant application"
  why: "Towns pay consultants just to write their IROP cyber-security subsidy applications — a queue forms before the compliance work even starts."
  url: https://smlouvy.gov.cz/smlouva/38438158
  note: 'hlidac-38438158: Boskovice paid enovation to write its IROP 21-27 call No. 120 ''Cyber
    security'' subsidy application (~121k CZK, Jun 2026) — one of a grant-application cluster
    with České Budějovice (hlidac-38351500, incl. mandatory OHA/Archimate paperwork) and PN
    Jihlava (hlidac-38824338). A dedicated EU subsidy channel funds the municipal compliance
    market, and towns pay consultants just to enter the queue.'
  date: '2026-06-19'
  signal: hlidac-38438158
- type: subsidy
  name: "IROP call 120 — Kybernetická bezpečnost II"
  gist: "the €99.6M subsidy pot"
  why: "2.44bn CZK (~€99.6M) at a 50% support rate for municipalities, regions and hospitals regulated under Act 264/2025. Applications 30 Apr – 17 Dec 2026."
  url: https://irop.gov.cz/cs/vyzvy-2021-2027/vyzvy/120vyzvairop
  note: 'dotace-irop-120-kyberbezpecnost: IROP 21-27 call No. 120 ''Kybernetická bezpečnost
    II'' — 2.44bn CZK (1.798bn EU + 643M state, ~€99.6M) at a 50% EU support rate for
    municipalities, regions, hospitals and other providers of regulated services under
    Act 264/2025 Sb.; applications 30.4.2026–17.12.2026.'
  date: '2026-12-17'
  signal: dotace-irop-120-kyberbezpecnost
- type: subsidy
  name: "HORIZON — ECCC cybersecurity calls (€56.2M)"
  gist: "the €56.2M builder money"
  why: "EU money for building security tooling itself — consortia, Czech firms eligible, deadline 15 Sep 2026. Funds the vendors, not the obligated buyers."
  url: https://cybersecurity-centre.europa.eu/funding-opportunities/calls-proposals/cybersecurity-horizon-cl3-2026-02-cs-eccc_en
  note: 'dotace-horizon-eccc-cyber-2026: HORIZON-CL3-2026-02-CS-ECCC — €56.2M across
    secure software/hardware development (€20M), AI model security (€21.2M) and advanced
    cryptography (€15M); consortia of companies and research organisations, CZ eligible,
    deadline 15.9.2026. Builder-side money — it funds the tooling vendors, not the
    obligated buyers.'
  date: '2026-09-15'
  signal: dotace-horizon-eccc-cyber-2026
- type: round
  name: "Secfix"
  gist: "the Berlin €10.2M round"
  why: "Berlin, €10.2M Series A (Feb 2026) for AI-driven security-compliance automation for SMEs — the closest funded template for a productised NIS2 offer."
  url: https://www.vestbee.com/insights/articles/top-european-funding-rounds-closed-in-february-2026
  note: 'round-secfix: Berlin''s Secfix raised €10.2M Series A (Feb 2026) for AI-driven
    end-to-end security-compliance automation aimed at SMEs — the comps-ledger traction
    figure, now on the ledger.'
  date: '2026-02-28'
  signal: round-secfix
- type: round
  name: "Copla"
  gist: "the Vilnius €6M round"
  why: "Vilnius, €6M Series A (Feb 2026) for real-time compliance monitoring — a second funded compliance-automation player next door, covering NIS2, DORA and ISO 27001."
  url: https://www.vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-february-2026
  note: 'round-copla: Vilnius'' Copla raised €6M Series A (Feb 2026) for real-time compliance-monitoring
    infrastructure for fintechs and banks. Backs the funding figure only; the NIS2/DORA/ISO-27001
    product descriptor comes from the comps ledger''s EU-Startups attribution, not
    from this round record.'
  date: '2026-02-28'
  signal: round-copla
- type: statistic
  name: "NÚKIB — registration tally"
  gist: "the 4,825 registration count"
  why: "The regulator's own count: 4,825 of ~6,000 expected entities had reported a regulated service by 8 Feb 2026 — verifying the 6,000 figure, with over a thousand obligated organisations not yet even registered."
  url: https://nukib.gov.cz/cs/infoservis/aktuality/2372-ohlaseni-podle-noveho-zakona-o-kyberneticke-bezpecnosti-provedlo-pres-4800-organizaci/
  note: 'Research 2026-08-24: NÚKIB news item reports 4,825 organisations had reported a
    regulated service by 8 Feb 2026 (over 4,500 by 1 Jan 2026, "75 procent z očekávaného
    počtu"), against approximately 6,000 expected; unregistered entities face administrative
    proceedings, sanctions up to CZK 250m or 2% of net global annual turnover, and the length
    of non-compliance is stated as an aggravating circumstance. Verifies the 6,000+ population
    figure this record has carried from SME UNION.'
  date: '2026-02-08'
- type: statistic
  name: "Reglyze — NIS2 tooling price survey"
  gist: "the per-firm price band"
  why: "Named annual prices for NIS2 compliance software: Reglyze from €490/yr, Secfix ~€500 a month, Vanta and Drata ~$7,500 a year, OneTrust $30k+ — what a per-firm product can realistically charge."
  url: https://reglyze.com/en/best-nis2-compliance-software
  note: 'Research 2026-08-24: vendor comparison (Reglyze — itself a vendor, prices for
    competitors quoted from public sources) names per-firm NIS2 tooling prices: Reglyze from
    €490/org/yr degressive; Secfix ~€500/mo (~€6k/yr); Vanta and Drata ~USD 7,500/yr; ComplyCloud
    €310/mo per 100 FTE; OneTrust $30k+/yr enterprise. Grounds the bottom-up market math;
    not a receipt for this record''s money score.'
  date: '2026-08-24'
- type: statistic
  name: "Mordor Intelligence — Europe cybersecurity"
  gist: "the $70B market size"
  why: "Sizes European cybersecurity spend at ~$69.8 billion in 2026, growing ~10.6% a year to ~$115.7 billion by 2031 — with NIS2 and DORA named as the anchor drivers."
  url: https://www.mordorintelligence.com/industry-reports/europe-cybersecurity-market
  note: 'Research 2026-08-24: Mordor Intelligence values the Europe cybersecurity market at
    USD 69.82B in 2026, forecast USD 115.66B by 2031 (10.62% CAGR), naming NIS2 and DORA
    enforcement among the primary growth drivers. Context for the market ceiling; not a
    receipt for this record''s money score.'
  date: '2026-08-24'
- type: gap-check
  name: "Czech NIS2 vendor scan"
  gist: "the Czech vendor sweep"
  why: "Czech products now sell the obligation directly to the mid-market — NIS2 Průvodce at 3,000 CZK a month, Compligen at 29,900 CZK once, NIS2 Doku from 4,900 CZK — so the field is no longer only consultancies."
  url: https://nis2pruvodce.cz/
  note: 'Czech-language vendor scan 2026-08-25. The productised Czech field is NOT empty and is
    wider than the Lexnova package already on file. Selling NIS2/ZoKB compliance as a product,
    with public prices: NIS2 Průvodce (nis2pruvodce.cz) — a full Czech SaaS platform, 12
    modules covering both vyhláška 409/2025 and 410/2025, asset register with 20 templates,
    52-measure risk catalogue, supplier register wired to ARES, supplier questionnaires (31
    questions higher regime / 12 lower), NÚKIB incident reporting with the 24/72h deadlines and
    a PDF generator, training with certificates, and an AI assistant over the statute; 7 days
    free then 3,000 CZK/month per IČO with volume discounts from the second IČO and 15% off
    annually; operator Ondřej Šitler, IČO 88635783, not VAT-registered — one person running the
    product shape Secfix and Copla raised Series A rounds for. Compligen (compligen.cz) —
    online guided generator producing 20+ documents against vyhláška 410/2025 for the
    lower-obligations regime (50-249 employees), 29,900 CZK one-off ex-VAT, founder Lukáš
    Vencálek, no IČO published and no ARES match for the trade name; carries a dedicated
    public-administration page (compligen.cz/nis2/verejna-sprava) aimed at obce, and prices
    itself against consultants at 80,000-200,000 CZK. NIS2 Doku (nis2doku.cz, David Mikulec) —
    documentation pack, Start 4,900 CZK / Pro 11,900 CZK one-off ex-VAT, 10+ documents per
    vyhláška 410/2025 plus Excel asset, incident and supplier tools. ICZ Risk*Guide
    (iczgroup.com/rgnis2) — modular ISMS and risk tool from a large Czech systems house, the
    enterprise end. ISMS Tools — ISMS and compliance tool covered by acresia.com. CYBER Manager
    (nis2-manager.cz) — incident evidence and classification per NIS2/ZoKB/DORA; site did not
    respond at check time, so it is named but unverified. CypherOn (cypheron.cz) publishes an
    interactive vyhláška-410 walkthrough. Aptien Labs s.r.o. (IČO 26397668) carries NIS2
    compliance content over its SME workplace-admin tool. Consultancy-only players seen
    alongside: Blue Partners, MT Legal, eLegal, Reactive, Argo22, EY, PwC. CORPUS BLINDNESS
    CONFIRMED exactly as CONVENTIONS predicts: Compligen, NIS2 Průvodce, NIS2 Doku, Risk*Guide
    and CypherOn return ZERO hits across all 11,330 signals in data/register.db — none raised,
    none sells through public tender, so neither the funded feed nor the tender feed can see
    them; only Czech-language search did. Surfaces: Czech web search (queries below), ARES for
    legal identity and IČO, a Czech vendor/press catalogue pass (systemonline.cz), the funded
    ledger via register.db, and data/lookup/cz-eshop-addons.jsonl (606 Shoptet and Upgates
    add-ons; one keyword hit and it was a TikTok warning inside an unrelated social-networks
    add-on — nothing NIS2 on either marketplace). POSITIVE CONTROL: the same Czech-search
    method run at Wultra, the Prague security vendor already named as an incumbent on p-0017,
    surfaced Wultra App Shielding — control PASSED, so the positives above are trustworthy. gap
    was already 0 and stays 0; status moves to watching under the SPEC §4 de-rank rule on the
    named Czech incumbents. Flagged, not changed: scores.proof is 0 while two funded comps sit
    on the ledger (Secfix €10.2M Series A, Copla €6M Series A) — scripts/check-records.py
    already errors on the contradiction.'
  date: '2026-08-25'
  queries:
    - "software pro NIS2 compliance český nástroj zákon o kybernetické bezpečnosti 264/2025 řízení bezpečnosti"
    - "nástroj pro řízení kybernetické bezpečnosti ISMS česká aplikace NIS2 dokumentace pro obce a firmy"
    - "NIS2 aplikace pro malé a střední firmy samoobslužný nástroj compliance předplatné české řešení"
    - "NIS2 dokumentace online generátor bezpečnostní politiky vyhláška 410/2025 nástroj cena Kč"
    - "kybernetická bezpečnost pro obce a města software NIS2 balíček pro veřejnou správu český dodavatel aplikace"
    - '"ISMS Tools" software kybernetická bezpečnost NIS2 cena předplatné česky'
    - "systemonline.cz katalog software NIS2 kybernetická bezpečnost GRC řešení přehled dodavatelů"
    - "české řešení pro zabezpečení mobilního bankovnictví silná autentizace podpisy v mobilu dodavatel"
  checked: [google-cz, ares, cz-saas-directories, own-funded-ledger, eshop-addon-marketplaces]
  expires: '2026-11-23'
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/557060-2026
  note: 'ted-557060-2026: ČEZ Distribuce, a. s. tendered "Nástroj pro bezpečnostní monitoring
    technologické sítě" (a security-monitoring tool for its technology network), ~€1.82M
    (45.5M CZK), published 12 Aug 2026 — an energy-sector essential entity (energy is named in
    this record''s scope) buying exactly the security-measures category Act 264/2025 requires.
    Adds a new named buyer to the buying wave; money and urgency dimensions already at ceiling,
    so no score moves.'
  date: '2026-08-12'
  signal: ted-557060-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/569596-2026
  note: 'ted-569596-2026: ČESKÁ TELEVIZE tendered network-security-monitoring equipment plus
    cyber-threat detection and response for its technology network, ~€930k, published 18 Aug
    2026 with a near-term deadline flagged — a major Czech public institution buying the same
    tooling category as the rest of the wave. Adds a new named buyer; money and urgency already
    at ceiling.'
  date: '2026-08-18'
  signal: ted-569596-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/587584-2026
  note: 'ted-587584-2026: Mendelova univerzita v Brně re-tendered ("opakované řízení") for an
    outsourced cybersecurity manager (manažer kybernetické bezpečnosti — the role Act 264/2025
    requires obligated entities to designate), published 26 Aug 2026, no value disclosed. Direct
    evidence for this record''s own claim that most of the 6,000 have nobody to do the work: an
    obligated public institution going back to market for the mandated role.'
  date: '2026-08-26'
  signal: ted-587584-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/590734-2026
  note: 'ted-590734-2026: Státní zdravotní ústav (the National Institute of Public Health)
    tendered an endpoint-security system at EPP/EDR/XDR level, ~€216k (5.4M CZK), published
    27 Aug 2026 — another health-sector essential entity buying security-measures tooling, a
    named institution not previously on this record. Money and urgency already at ceiling.'
  date: '2026-08-27'
  signal: ted-590734-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/595810-2026
  note: 'ted-595810-2026: Nemocnice Milosrdných bratří tendered a security software package
    under "Zvýšení kyberbezpečnosti v NMB" (raising the hospital''s cybersecurity), ~€3.36M
    (83.9M CZK), published 28 Aug 2026 — one of the largest single hospital awards on file
    alongside Motol, Homolka and Hustopeče [S3]. Adds scale to the buying wave; money and
    urgency already at ceiling.'
  date: '2026-08-28'
  signal: ted-595810-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/600605-2026
  note: 'ted-600605-2026: NAKIT (the state IT agency) opened a framework for ArcSight SIEM
    platform services, ~€11.6M, published 1 Sep 2026 — the largest single cyber figure in the
    2026-09-02 harvest and a new named public buyer in the buying wave. Money and urgency
    already at ceiling; no score moves.'
  date: '2026-09-01'
  signal: ted-600605-2026
- type: price
  url: https://smlouvy.gov.cz/smlouva/38911766
  name: "Lexnova — the packaged order"
  gist: "about 91k CZK a package"
  why: "A care home paid about 91,000 CZK for a packaged cyber-security compliance order, and a second order of the same package followed within weeks."
  note: 'Price receipt drawn from the contract already on this ledger (hlidac-38911766, Domov
    pro seniory Napajedla, NIS 2 package, ~91k CZK, Jun 2026; the repeat order is
    hlidac-38723900, Zlín-region disability services, whose own url is not on this record).
    One receipt, the price stated once. dims omitted: backs no score.'
  date: '2026-06-22'
  payer: 'Domov pro seniory Napajedla, in the smallest obligated tier'
  amount_czk: 91000
  unit: one-off
  basis: signed-contract
- type: price
  url: https://smlouvy.gov.cz/smlouva/39084314
  name: "Český Brod — a town of 7,000 buys the whole job"
  gist: "about 9M CZK for one town"
  why: "A town of about 7,000 people signed roughly 9M CZK for municipal cyber security, the top end of what the smallest obligated buyers pay."
  note: 'Price receipt drawn from the contract already on this ledger (hlidac-39084314,
    Kybernetická bezpečnost města, ~9.0M CZK, 11 Aug 2026). No annual term stated, so one-off.
    dims omitted: money already rests on the open tenders and this adds no point.'
  date: '2026-08-11'
  payer: 'Město Český Brod, a town of about 7,000 people'
  amount_czk: 9000000
  unit: one-off
  basis: signed-contract
- type: price
  url: https://nis2pruvodce.cz/
  name: "NIS2 Průvodce — the Czech subscription"
  gist: "3,000 CZK a month"
  why: "An obligated Czech company pays 3,000 CZK a month for the Czech compliance platform, one subscription per company number, after a seven-day free trial."
  note: 'Price receipt lifted from the 2026-08-25 Czech vendor scan already on this ledger,
    which read nis2pruvodce.cz: 7 days free, then 3,000 CZK/month per IČO, volume discounts
    from the second IČO and 15% off annually. The seat here is the subscribing company, which
    why states. Compligen (29,900 CZK one-off) and NIS2 Doku (from 4,900 CZK) sit in the same
    note but their own urls are not on this record, so they are not written as receipts here.
    dims omitted: backs no score.
    Verified 2026-09-04: nis2pruvodce.cz still states 7 dní plný přístup zdarma, poté
    3 000 Kč/měsíc za IČO, with volume slevy from the second IČO and 15% off on annual
    payment.'
  date: '2026-08-25'
  payer: 'An obligated Czech company'
  amount_czk: 3000
  unit: per-seat-month
  basis: list-price
created: '2026-08-13'
updated: '2026-09-04'
---

Act No. 264/2025 Coll., the Czech transposition of the EU's NIS2 security directive, puts roughly 6,000 firms and municipalities under a cybersecurity regime: energy, manufacturing, food, logistics, digital services [S1,S2]. NÚKIB (the national cyber agency) had 4,825 registered by February 2026, over a thousand short [S13]; many small firms do not know they are in scope [S2]. Measures fall due a year after registration — deadlines through H1 2027, fines to 2% of global turnover or CZK 250m [S1]. Most of the 6,000 have nobody to do the work — Mendel University re-tendered in August 2026 after its first attempt to hire an outsourced security manager [S19].

Existing non-solutions: consultancies are no longer alone — four Czech products now sell the obligation itself: NIS2 Průvodce at 3,000 CZK a month, built by one person; Compligen at 29,900 CZK once, aimed at towns; NIS2 Doku from 4,900 CZK; Lexnova Energy's ~91k CZK package, ordered twice by care providers in weeks [S2,S7,S16]. All four are younger than the obligation, in force since November 2025 — they sell the paperwork, not the work [S1,S16]. Only ICZ (a systems house trading since 1997) works the enterprise end, and sells a project [S16].

Why now: the one-year clocks are running, and NÚKIB counts delay against the unregistered [S1,S13]. Act No. 266/2025 adds CER — the EU's critical-entity law — with physical-resilience duties on the same entities from 17 July 2026 [S5]. IROP (the EU regional-development programme) stops taking applications on 17 December 2026 [S9].

Who pays: the roughly 6,000 regulated entities themselves — compelled by law, not persuaded [S1,S13]. Public buyers placed ~77 cyber-security awards worth ~€33M in June–August 2026 [S7]. Awards run from ~€6.1M at Motol and Homolka [S3] to ~9M CZK at Český Brod, a town of 7,000 [S6]; Prague bought city-wide monitoring for ~€5.3M [S4]. A ~€99.6M subsidy pot sits behind them [S9]; towns pay ~121k CZK for the application alone [S8]. Tooling sells at €500–6,000 per firm a year [S14]: a quarter of the 6,000 at €3,000 is ~€4.5M a year, before the implementation the €33M buys. European cybersecurity spend runs ~$70 billion in 2026, up ~11% a year [S15].

Solved elsewhere: Secfix (Berlin, €10.2M Series A) sells compliance automation to hundreds of small firms in 15+ European countries [S11]. Copla (Vilnius, €6M Series A) automates the same compliance next door [S12]. Neither sells in Czechia.

## First moves

1. Sell to the buyers already paying: small towns and social-care homes. A care home bought Lexnova's ~91k CZK package off the shelf, then ordered again weeks later; Týn nad Vltavou paid just to find out whether the law applied to it [S7]. Český Brod, 7,000 people, signed ~9M CZK, and 341 cyber contracts have landed in the state contracts register since June [S6].
2. Start with a fixed-price readiness check: where one town or institution stands against Act 264/2025 and Vyhláška 409/2025 — the decree setting out the security measures — and what it owes before its one-year deadline runs out [S1]. Fixed price is what the smallest obliged buyers demonstrably choose [S7].
3. Let the state pay for it. [IROP 120 Kybernetická bezpečnost II](/sources/tenders#dotace-irop-120-kyberbezpecnost) — the cyber call — holds ~€99.6M at a 50% rate for municipalities, regions and hospitals, open until 17 December 2026 [S9]. Towns already pay consultants to write those applications [S8]: write the application, then do the work it funds. To fund the tool itself, [HORIZON-CL3-2026-02-CS-ECCC](/sources/tenders#dotace-horizon-eccc-cyber-2026) (€56.2M) closes 15 September 2026 [S10].
4. Sell the doing, not the documents. NIS2 Průvodce (3,000 CZK a month), Compligen (29,900 CZK once) and NIS2 Doku (4,900 CZK) already sell the paperwork [S16]. None of them implements anything, and implementation is what the ~€33M of public awards buys [S7].
5. Come back for the second law. Act No. 266/2025 puts physical-resilience duties on many of the same organisations through 2027 [S5]. Every NIS2 customer will need that too.
6. Know who else is in the room. NIS2 Průvodce, Compligen, NIS2 Doku and ICZ Risk*Guide sell the compliance product [S16]; Lexnova Energy sells repeat packages, Institut kybernetické bezpečnosti sells scope analysis, and enovation writes the subsidy applications [S7,S8]. Abroad, Secfix [S11] and Copla [S12] do it at Series A scale.

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it. Same date, separate pass, merged here: First moves rewritten in plain language (owner: "full of fluff and jargon — make the ideas simple"); "subsidy-funded entry offer" and "the documentation is productised, the doing is not" replaced with plain sentences. Every [Sn] marker, ledger link and named competitor kept; no claim added or dropped; scores untouched.

2026-08-13 · money and demand receipted — The first successful TED run put the buying wave on the record across the full size spectrum, from Motol and Prague at the top to care homes and small towns ordering productised "NIS 2 packages" below the threshold, with an IROP subsidy channel behind the municipal projects [S3,S4,S7,S8]. That substance now sits in How big rather than here. Noted for the gap dimension at the time: Lexnova's repeat package sales and Institut kybernetické bezpečnosti's scope-analysis product are the first evidence that productised CZ offerings for the small-entity tier are emerging [S7].

2026-08-24 · board-brief rewrite — The body was rewritten to the builder-first template (problem → proven abroad → local competition → how big → why now), cutting the argument from 440 to ~335 words with no claim added beyond its source. Market research joined the record: NÚKIB's own registration tally (4,825 of ~6,000 expected, Feb 2026) [S13], per-firm NIS2 tooling prices (Reglyze from €490/yr, Secfix ~€500/mo, Vanta/Drata ~$7,500/yr) [S14], and the ~$70bn 2026 European cybersecurity market with NIS2/DORA as named drivers [S15] — grounding a bottom-up floor of ~€4.5M/yr for a productised Czech offer (6,000 entities × €3,000/yr × 25%). Every source gained a public name and why line; internal notes, scores and status untouched.

2026-08-25 · market check — The Czech field was searched in Czech for the first time and it is not empty: four named products sell NIS2 compliance to the obligated mid-market, from a one-person SaaS at 3,000 CZK a month to a documentation pack at 4,900 CZK, plus ICZ's Risk*Guide at the enterprise end [S16]. `scores.gap` was already 0 and stays 0 — nothing here can raise it — but `status` moves candidate → watching under the SPEC §4 de-rank rule, and "Existing non-solutions" and First moves 4 and 6 now name the incumbents instead of asking for the survey that has now been run. `score` is unchanged at 7. Method note for the next check: none of the four products appears anywhere in the 11,330-signal corpus — none raised and none sells through public tender — so only Czech-language search could find them. Positive control: the same method run at Wultra (the incumbent named on p-0017) surfaced it, so the negatives in this pass are worth something. Flagged, NOT changed: `scores.proof` is 0 while Secfix (€10.2M Series A) and Copla (€6M Series A) sit on the comps ledger — the recommended value is 3 (funded analogs in two markets, one of them CEE-adjacent), and `scripts/check-records.py` already reports the contradiction as an error. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries NIS2 Průvodce, Compligen, NIS2 Doku and Lexnova Energy, all four early [S16,S7]. NIS2 Průvodce is one person — Ondřej Šitler, IČO 88635783, not VAT-registered — selling against an obligation that only took effect in November 2025; Compligen publishes no IČO and carries a Q3 2026 roadmap; NIS2 Doku is a one-off document pack; Lexnova Energy s.r.o. was incorporated in January 2025 and its sibling Lexnova Services in July 2026. None has three years of selling behind it, so none closes the space: `scores.gap` 0 → 1. The de-rank recorded above was therefore too harsh — it read 'a Czech product exists' as 'the space is taken', which is the v1 test the rewrite retires. ICZ Risk*Guide is deliberately not in `locals[]`, and it is the one entry the ladder cannot represent: ICZ a.s. has traded since 1997 and is plainly not an early company, but the register holds no limb receipt for Risk*Guide and ICZ sells at the enterprise end rather than to the SME and municipal tier this record's buyers occupy — listing it would either force gap 0 on a segment it does not serve or label a 1997 systems house early. It stays named in the body. `scores.proof` 0 → 3, resolving the contradiction flagged above: Secfix (Berlin) and Copla (Vilnius) both pass the established test, in two markets, both CEE-adjacent. `score` 7 → 11. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and **ICZ Risk\*Guide is restored to the ledger** as `competes: adjacent` + `maturity: established`. It is the entry the pass above called the one the ladder could not represent, and the split resolves exactly that bind. ICZ a.s. (IČO 25145444) has traded since July 1997 and is named as a public supplier in this register's own contract signals — Digitální a informační agentura, the police presidium and Správa informačních technologií města Plzně — so it is established on a limb anyone can check, while `competes: adjacent` records that it does not sell this record's product to this record's buyer. Two corrections come with the restoration. First, the claim above that ICZ does not serve the municipal tier was wrong: the Risk\*Guide page names obce and kraje among its buyers. The real distinction is how it is bought — a modular ISMS and risk-assessment platform put in over a one-to-three-month implementation with a 24/7 advisory service attached, rather than the fixed-price product the long tail of obligated entities buys off a web page. Second, Risk\*Guide is now sold by **ICZ.Services a.s. (IČO 22183809)**, a group company incorporated in October 2024, which is why the entry carries the parent's IČO and year rather than the seller's. The four Czech NIS2 products convert to `competes: direct`, all still early. `scores.gap` stays 1 — an adjacent player never moves it — and `score` stays 11. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed.

2026-09-02 · plain-language pass — NIS2, NÚKIB, CER, IROP and ICZ glossed at first use; SME, SMB, MSP, SIEM and DORA replaced with ordinary words. Argument 424 → 376 words with every [Sn] marker, price, date and company kept, and five figures added from sources already on file: ~€6.1M Motol/Homolka [S3], ~€5.3M Prague [S4], ~121k CZK per subsidy application [S8], over a thousand entities still unregistered [S13], ICZ trading since 1997 [S16]. Corrected while tightening: "every one of these sellers is younger than the obligation itself" had swept in ICZ — the claim now names the four Czech products it is actually true of [S1,S16]. Lexnova keeps its price, repeat order and buyer type; only the quoted product name moved to the ledger and source name. First moves rewritten verbs-first with every marker and both tender links kept; a gist added beside all 16 sources. No score, status, note: field, locals[] entry or [Sn] marker touched.

2026-09-04 · price receipt — Three figures already on file are now recorded as prices: the packaged Lexnova order at about 91,000 CZK [S23], Český Brod at about 9M CZK [S24] and the NIS2 Průvodce subscription at 3,000 CZK a month per company [S25]. Compligen and NIS2 Doku are priced in the same scan, but their own pages are not on this ledger, so they stay in the note. No score, status, note, locals[] entry or marker touched.
