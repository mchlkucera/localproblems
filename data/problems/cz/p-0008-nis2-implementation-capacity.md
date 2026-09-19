---
id: p-0008
region: cz
title: '6,000 Czech towns and firms have months left to meet a new cybersecurity law'
brief: 'Many small firms don''t even know the law covers them, and the first deadlines hit in late 2026 [S1,S2]. A firm that misses its deadline can be fined up to 2% of its turnover (which is A LOT of money) [S1].'
solution: 'Build a small security agency that does the security work, and writes EU grant applications for the towns that qualify.'
good_for: 'Someone with cybersecurity skills who''s interested in grants and public-sector sales.'
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
entry:
  level: hard
  buyer: public
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: the law''s deadlines push towns and firms to buy now, an EU grant pays half for towns, and no licence is needed to do the work. Harder: the buyers are public bodies, so each sale goes through their slow purchasing rules and tenders, and they want references a new provider does not have yet.'
comps:
- name: Secfix
  url: https://www.secfix.com/
  geo: DE
  since: 2021
  traction: 'Raised €10.2M in a Series A round, Feb 2026 (Vestbee); hundreds of small-business
    customers in 15+ European countries (Tech Funding News, 2026)'
  signal: round-secfix
- name: Copla
  url: https://cyberupgrade.net/
  geo: LT
  since: 2023
  traction: 'Raised €6M in a Series A round, Feb 2026, after a €2.5M seed round, Nov 2024 (Vestbee);
    software that automates compliance with EU security rules (NIS2, DORA) and the ISO 27001
    standard, formerly called CyberUpgrade (EU-Startups, 2026)'
  signal: round-copla
locals:
- name: NIS2 Průvodce
  url: https://nis2pruvodce.cz/
  ico: '88635783'
  since: 2025
  competes: direct
  maturity: early
  evidence: 'A Czech compliance platform, sold by monthly subscription per company. Twelve modules
    cover both decrees that set out the security measures (vyhláška 409/2025 and 410/2025): an
    asset register, a 52-item risk catalogue, a supplier register linked to the state business
    register, incident reports to the national cyber-security agency within its 24- and 72-hour
    deadlines, training, and an AI assistant that answers questions about the law. One person,
    Ondřej Šitler, runs it. He is not VAT-registered, the law it sells against only took effect
    in November 2025, and no buyer is named.'
- name: Compligen
  url: https://www.compligen.cz/
  since: 2026
  competes: direct
  maturity: early
  evidence: 'An online tool that generates the documents the law requires. It produces 20+
    documents for organisations under the lighter set of rules (vyhláška 410/2025), for 29,900
    CZK one-off before VAT, and has a page aimed at towns. It claims more than 30 firms and towns
    as clients. But founder Lukáš Vencálek publishes no company number, no company of that trade
    name is in the state business register, and the product still shows a Q3 2026 roadmap.'
- name: NIS2 Doku
  url: https://nis2doku.cz/
  since: 2025
  competes: direct
  maturity: early
  evidence: 'A pack of ready-made compliance documents. It holds 10+ documents for the lighter set
    of rules (vyhláška 410/2025), plus Excel tools for assets, incidents and suppliers, at 4,900
    CZK (Start) or 11,900 CZK (Pro), one-off before VAT. It is sold by David Mikulec, and no
    buyer is named.'
- name: Lexnova Energy
  url: https://www.lexnova.cz/
  ico: '22530649'
  since: 2025
  competes: direct
  maturity: early
  evidence: 'A ready-made "NIS 2 package" for public buyers, with repeat orders in the state
    contracts register. Lexnova Energy s.r.o. was founded in January 2025, and its sister
    company Lexnova Services s.r.o. in July 2026.'
- name: ICZ Risk*Guide
  url: https://www.iczgroup.com/riskguide/
  ico: '25145444'
  since: 1997
  competes: adjacent
  maturity: established
  evidence: 'A security and risk-management platform, bought as a large project. It is deployed
    at the state digital agency, the police presidium and the Plzeň city IT authority. Ministries,
    regions, towns and large organisations buy it with one to three months of setup and a 24/7
    advisory service, not as the fixed-price product a small organisation buys off a web page.
    ICZ a.s. has traded since July 1997, and the product is now sold by the group company
    ICZ.Services a.s. (IČO 22183809, founded October 2024).'
process:
  summary:
    today: 'A covered town or care home buys help in pieces: one seller checks what it owes, another writes the grant application, a third sells paperwork [S7,S8,S16].'
    after: 'One provider does the check, the application and the security work, so the organisation buys once instead of three times.'
  steps:
  - who: A consultant who checks what the law requires
    today: 'Checks whether the new cybersecurity law covers the organisation, and what it owes'
    known: documented
    cites: [2, 7]
    change: changes
    after: 'One fixed-price provider makes the same check, before the organisation''s deadline'
  - who: The town or care home
    today: 'Registers with the national cyber-security agency, which starts its one-year deadline for security measures'
    known: documented
    cites: [1, 13]
    change: stays
    after: 'Unchanged: registering is the organisation''s own duty'
  - who: A consultant who writes grant applications
    today: 'Writes the EU grant application for the organisations that can get one'
    known: documented
    cites: [8]
    change: changes
    after: 'The same provider writes the application, inside the fixed price'
  - who: A seller of ready-made compliance documents
    today: 'Sells the required documents as a package, without doing the security work'
    known: documented
    cites: [16]
    change: changes
    after: 'The documents describe security work the provider has actually done'
  - who: Nobody in-house, at most of these organisations
    today: 'Nobody carries out the security measures; one university had to re-run its tender for an outside security manager'
    known: inferred
    cites: [2, 19]
    change: changes
    after: 'The provider does the security work itself, at the same fixed price'
  - who: '?'
    today: 'Who checks the measures after the deadline, and when, is not known'
    known: unknown
    cites: []
    change: stays
    after: 'Unchanged: the provider prepares the organisation for that check but does not perform it'
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
    CZK per award scored money 2 on the v1 ladder; since the 2026-09-19 rescore it is public
    money nearby (security tooling, not the security work this problem sells) and earns no
    point.'
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
    One receipt, the price stated once. Tagged dims: [money] on 2026-09-19: a paid receipt for
    this job (packaged compliance for the smallest obligated tier, from a seller the ledger
    lists as direct), within 24 months.'
  date: '2026-06-22'
  payer: 'Domov pro seniory Napajedla, in the smallest obligated tier'
  amount_czk: 91000
  unit: one-off
  basis: signed-contract
  dims: [money]
- type: price
  url: https://smlouvy.gov.cz/smlouva/39084314
  name: "Český Brod — a town of 7,000 buys the whole job"
  gist: "about 9M CZK for one town"
  why: "A town of about 7,000 people signed roughly 9M CZK for municipal cyber security, the top end of what the smallest obligated buyers pay."
  note: 'Price receipt drawn from the contract already on this ledger (hlidac-39084314,
    Kybernetická bezpečnost města, ~9.0M CZK, 11 Aug 2026). No annual term stated, so one-off.
    Tagged dims: [money] on 2026-09-19: a town paying for its whole cyber-security job is a
    paid receipt for this job, within 24 months; with the Napajedla order it is what Willing
    to pay now rests on, where the v1 score rested on the open tenders.'
  date: '2026-08-11'
  payer: 'Město Český Brod, a town of about 7,000 people'
  amount_czk: 9000000
  unit: one-off
  basis: signed-contract
  dims: [money]
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
    Tagged dims: [money] on 2026-09-19: an asking price for this job from a seller the ledger
    lists as direct.
    Verified 2026-09-04: nis2pruvodce.cz still states 7 dní plný přístup zdarma, poté
    3 000 Kč/měsíc za IČO, with volume slevy from the second IČO and 15% off on annual
    payment.'
  date: '2026-08-25'
  payer: 'An obligated Czech company'
  amount_czk: 3000
  unit: per-seat-month
  basis: list-price
  dims: [money]
- type: price
  url: https://smlouvy.gov.cz/smlouva/38438158
  name: "Boskovice — a consultant paid to write the grant application"
  gist: "about 121k CZK an application"
  why: "A town paid a consultant about 121,000 CZK to write its EU cyber-security grant application, one piece of the job a single provider would take on."
  note: 'Price receipt drawn from the contract already on this ledger [S8] (hlidac-38438158:
    Boskovice paid enovation to write its IROP 21-27 call No. 120 cyber-security subsidy
    application, ~121k CZK, Jun 2026), added in the 2026-09-19 tagging pass. Writing the grant
    application is named in solution: and in the process figure, so this is a consultant paid
    to do a piece of this job by hand, within 24 months. No term stated, so one-off. The České
    Budějovice and PN Jihlava applications in the same note carry no amount, so they are not
    written as receipts.'
  date: '2026-06-19'
  payer: 'Město Boskovice, a town applying for the EU cyber-security grant'
  amount_czk: 121000
  unit: one-off
  basis: signed-contract
  dims: [money]
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/632864-2026
  name: "TED — Prague 5 outsources the running of its security tools"
  gist: "a city district buys the work"
  why: "A Prague city district tenders two years of outside administration, monitoring and evaluation of its cyber-security tools, including handling security incidents, at an estimated 11.8M CZK."
  note: 'ted-632864-2026: Městská část Praha 5, contract notice, open procedure, issued 14 Sep
    2026, bids due 21 Oct 2026. "Správa, nastavení a dohled nad vybranými nástroji kybernetické
    bezpečnosti": professional services to administer, configure, monitor and evaluate selected
    cyber-security tools, incl. LAN and network-service administration, support for its Bitdefender
    security platform, and monitoring, evaluation and handling of security incidents; duration 24
    months; estimated value 11,827,200 CZK excl. VAT. TED XML read 2026-09-19. Unlike the tooling
    tenders on file, this buys security work itself, from a town-level public buyer. It is an
    open tender with no award, so it stays public money nearby and backs no score; once awarded,
    the winning line is a tender-line price receipt for this job. The notice does not cite Act
    264/2025.'
  date: '2026-09-14'
  signal: ted-632864-2026
  dims: []
- type: contract
  url: https://smlouvy.gov.cz/smlouva/39447877
  name: "Registr smluv — Jihlava psychiatric hospital, grant-funded purchase (~22.9M CZK)"
  gist: "a grant turned into a purchase"
  why: "A psychiatric hospital signed about 22.9M CZK for security hardware and software with installation and five years of support, part-paid by the EU's regional-development programme."
  note: 'hlidac-37086957: Psychiatrická nemocnice Jihlava signed "Kupní smlouva - Zvýšení
    kyberbezpečnosti PNJ" (SML-0093/26) with S A L T O spol. s r.o. (IČO 44016336) on 8 Sep 2026,
    22,932,485 CZK excl. VAT / 27,748,306.85 CZK incl. VAT (registr smluv, published 9 Sep 2026).
    Contract text read 2026-09-19: supply of infrastructure elements (HW + SW) per annex 1, with
    implementation, connection to the hospital''s infrastructure, training of administrators and
    users, and technical support for the 5-year sustainability period; co-financed from the IROP
    project "Zvýšení kyberbezpečnosti PNJ", reg. no. CZ.06.01.01/00/22_004/0000349 (the contract
    does not name the IROP call). A purchase of kit, not the security measures and paperwork this
    problem sells, so not restated as a price receipt and no dims. Same hospital as the grant
    application in the [S8] note (hlidac-38824338). The TED award notice for the same purchase
    (ted-626646-2026, 22,932,485 CZK, SALTO) is a duplicate and is not cited.'
  date: '2026-09-08'
  signal: hlidac-37086957
  dims: []
created: '2026-08-13'
updated: '2026-09-19'
---

The new cybersecurity law makes each covered organisation register, then put security measures in place within a year [S1].

- About 6,000 towns and firms are covered, in energy, manufacturing, food, logistics and digital services [S1,S2].
- Many small firms do not yet know the law covers them [S2].
- The top fine is CZK 250m or 2% of global turnover [S1,S13].
- 4,825 had registered by February 2026, so over a thousand had not [S13].
- One university had to re-run its tender for an outside security manager [S19].

The law is Act No. 264/2025, the Czech version of the EU's NIS2 directive (its common cybersecurity rules) [S1]. Each organisation registers with NÚKIB (the national cyber-security agency), telling it that it runs a covered service, and its year for security measures runs from that registration [S1].

- The agency counts a long delay against an organisation when it sets a fine [S13].
- The security measures are concrete steps set out in two decrees, No. 409/2025 and No. 410/2025 [S16]. They include a list of the organisation's computers and data, a risk assessment, supplier checks, staff training, and reporting an attack to the agency within 24 hours [S16].
- The university is Mendel University in Brno. In August 2026 it went back to market for an outsourced security manager, a role the law requires [S19].

Existing non-solutions: Four Czech sellers offer the paperwork the law requires, and none sells the security work itself [S7,S16].

None of the four puts the security measures in place, and that work is what the public contracts under [Who pays](#how-big) buy [S7,S16]. They sell the documents as ready-made packs or online tools [S16]. Other firms sell single pieces of the job:

- Institut kybernetické bezpečnosti sells scope analysis: whether the law applies, and what is owed [S7].
- enovation writes the EU grant applications that towns pay for [S8].

Why now: Towns, care homes and firms under the new law run out of time in late 2026, and first steps already cost about [100,000 CZK](#willing-to-pay) [S1,S8].

- A firm's owner has one year from registering with the national cyber-security agency to put the required security in place, so the first deadlines fall in late 2026 [S1]. A firm that misses its deadline can be fined up to 2% of its turnover [S1,S13].
- A town's director who wants the EU to pay half of the work first pays a consultant about 121,000 CZK just to write the grant application [S8,S9]. The grant stops taking applications on 17 December 2026, so a town that has not applied by then pays the full cost itself [S9].
- Hiring someone to do the work is hard. Mendel University in Brno had to run its tender for an outside security manager, the person the law requires to be in charge of security, a second time in August 2026 [S19]. A care home bought a ready-made package instead, at the price shown under [Willing to pay](#willing-to-pay) [S7].
- Many small firms do not yet know the law covers them [S2]. An organisation that has not registered already faces proceedings and a fine [S13].

The dates behind these deadlines come from the law itself, and from a second law on critical infrastructure [S1,S5]:

- On 1 November 2025 the new cybersecurity law took effect [S1].
- By 17 July 2026 the state had to name the organisations covered by the second law, on critical infrastructure [S5].
- In late 2026 the first one-year deadlines for security measures run out [S1].
- On 17 December 2026 the EU grant for towns, regions and hospitals stops taking applications [S9].
- By mid 2027 most of the remaining deadlines have run out [S1].
- The top fine is CZK 250m or 2% of global turnover, and the agency counts a long delay against an organisation when it sets the fine [S1,S13].

The second law is Act No. 266/2025, the Czech version of the EU's CER directive (its rules for critical entities) [S5]. It puts physical-resilience duties on many of the same organisations: resilience plans, meaning how they keep essential services running through physical threats, and incident reporting, through 2027 [S5]. Many customers for the first law will need this work too [S5].

Who pays: The covered organisations pay, and towns, regions and hospitals can get half back from an EU grant [S1,S9].

- About €33M in public cyber-security tenders and awards landed in June–August 2026 alone [S7].
- About 121,000 CZK is what one town paid a consultant just to write its grant application [S8].
- €500–6,000 a year is what compliance software costs one organisation [S14].

The €33M is spread over about 77 tenders and awards [S7]. Buyers range from large hospitals to small towns:

- Motol and Homolka, two large Prague hospitals, bought threat detection and response for about €6.1M [S3].
- The city of Prague bought security monitoring across the city for about €5.3M [S4].
- Český Brod, a town of about 7,000, bought its whole cyber-security job; its price is in the table of what one buyer pays [S6].
- The smallest buyers choose ready-made packages. A care home in Napajedla bought one, and social-care services in the Zlín region ordered the same package within weeks; its price is in the same table [S7].
- 341 cyber-security contracts have entered the state contracts register since June 2026 [S6].
- The town of Týn nad Vltavou paid just to find out whether the law applied to it [S7].
- Prague 5, a city district, is tendering two years of outside running of its security tools, including handling attacks, estimated at 11.8M CZK [S27].
- Jihlava's psychiatric hospital, one of the grant applicants, signed about 22.9M CZK in September 2026 for security hardware and software, part-paid by the EU's regional-development programme [S8,S28].

The EU grant is IROP call 120 (the cyber-security call of the EU's regional-development programme). It holds about €99.6M and pays 50% of the cost [S9].

A rough estimate from the software price range: if a quarter of the 6,000 paid €3,000 a year, software alone would bring about €4.5M a year [S14]. That is before the security work itself, which is what the public contracts buy [S7].

Across Europe, cybersecurity spending is about $70 billion in 2026, growing about 11% a year [S15].

Money for building security tools, rather than buying them, also existed. The ECCC (the EU's cybersecurity competence centre) offered €56.2M from the HORIZON research programme to groups of firms and research bodies, Czech ones included. That call closed on 15 September 2026 [S10].

Solved elsewhere: Two funded European companies sell software that automates security compliance [S11,S12].

## First moves

1. Build a simple, fixed-price check that tells a small town exactly what the new cybersecurity law requires of it and by when. The check answers three questions. First, does [the new law](#opportunity) cover the town at all? Second, has the town registered, meaning told the national cyber-security agency that it runs a covered service, which is the step that starts its one-year clock? Third, which security measures is it still missing? The measures are the concrete steps the law's decrees set out, such as a list of the town's computers and data, a risk assessment, supplier checks, staff training and reporting an attack quickly; they are listed under [The opportunity](#opportunity). The town gets a short report: what is done, what is missing, and the date each missing piece is due, before [its deadline](#why-now). Give it one price agreed up front, because the smallest buyers already choose ready-made packages, as [Willing to pay](#willing-to-pay) shows.
2. Call the directors of care homes and small towns that are already paying for help with this law, and offer them the check. They are easy to find, because public bodies must publish their contracts in the state contracts register. Start with the care homes, social-care services and small towns listed under [Willing to pay](#willing-to-pay), which bought ready-made packages or paid just to learn whether the law applies to them. These people have already shown they will spend money on this, and their deadline is close, as [Why now](#why-now) explains. Ask each one what they have done so far and what worries them, and use the answers to improve the check.
3. For each town that can get the EU grant, write its grant application, so the EU pays half of the security work that follows. The grant is EU money for towns, regions and hospitals covered by the law, described under [Willing to pay](#willing-to-pay). Towns already pay consultants a fee just to write this application, as [Why now](#why-now) shows. If you write it as part of your price, the town saves that fee and deals with one provider instead of two. Start early, because the grant stops taking applications on a fixed date, also under [Why now](#why-now).
4. Do the security work the check found missing, rather than only writing the documents that describe it. The work means putting the measures in place for real: making the list of computers and data, setting up supplier checks, training the staff, and being ready to report an attack in time. Several Czech sellers already sell the documents, as ready-made packs or online tools, but none of them does the work itself; see [Market gap](#competition). The public contracts pay for the work, and even a small town has signed a large contract for it; see [Willing to pay](#willing-to-pay). Hiring their own person is hard, too, since one university had to run its tender for an outside security manager again, as [Why now](#why-now) tells. So one provider that does the check, the application and the work, at a fixed price, saves the buyer from buying three times.
5. Once a town or care home trusts you, help it meet a second new law on critical infrastructure, which binds many of the same organisations. That law is the Czech version of the EU's rules for critical entities. It asks the organisations the state names to write resilience plans, meaning how they keep their essential services running through physical threats, and to report serious incidents. Its dates are under [Why now](#why-now). You already know these customers and their systems, so this is the natural next job to offer them.

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it. Same date, separate pass, merged here: First moves rewritten in plain language (owner: "full of fluff and jargon — make the ideas simple"); "subsidy-funded entry offer" and "the documentation is productised, the doing is not" replaced with plain sentences. Every [Sn] marker, ledger link and named competitor kept; no claim added or dropped; scores untouched.

2026-08-13 · money and demand receipted — The first successful TED run put the buying wave on the record across the full size spectrum, from Motol and Prague at the top to care homes and small towns ordering productised "NIS 2 packages" below the threshold, with an IROP subsidy channel behind the municipal projects [S3,S4,S7,S8]. That substance now sits in How big rather than here. Noted for the gap dimension at the time: Lexnova's repeat package sales and Institut kybernetické bezpečnosti's scope-analysis product are the first evidence that productised CZ offerings for the small-entity tier are emerging [S7].

2026-08-24 · board-brief rewrite — The body was rewritten to the builder-first template (problem → proven abroad → local competition → how big → why now), cutting the argument from 440 to ~335 words with no claim added beyond its source. Market research joined the record: NÚKIB's own registration tally (4,825 of ~6,000 expected, Feb 2026) [S13], per-firm NIS2 tooling prices (Reglyze from €490/yr, Secfix ~€500/mo, Vanta/Drata ~$7,500/yr) [S14], and the ~$70bn 2026 European cybersecurity market with NIS2/DORA as named drivers [S15] — grounding a bottom-up floor of ~€4.5M/yr for a productised Czech offer (6,000 entities × €3,000/yr × 25%). Every source gained a public name and why line; internal notes, scores and status untouched.

2026-08-25 · market check — The Czech field was searched in Czech for the first time and it is not empty: four named products sell NIS2 compliance to the obligated mid-market, from a one-person SaaS at 3,000 CZK a month to a documentation pack at 4,900 CZK, plus ICZ's Risk*Guide at the enterprise end [S16]. `scores.gap` was already 0 and stays 0 — nothing here can raise it — but `status` moves candidate → watching under the SPEC §4 de-rank rule, and "Existing non-solutions" and First moves 4 and 6 now name the incumbents instead of asking for the survey that has now been run. `score` is unchanged at 7. Method note for the next check: none of the four products appears anywhere in the 11,330-signal corpus — none raised and none sells through public tender — so only Czech-language search could find them. Positive control: the same method run at Wultra (the incumbent named on p-0017) surfaced it, so the negatives in this pass are worth something. Flagged, NOT changed: `scores.proof` is 0 while Secfix (€10.2M Series A) and Copla (€6M Series A) sit on the comps ledger — the recommended value is 3 (funded analogs in two markets, one of them CEE-adjacent), and `scripts/check-records.py` already reports the contradiction as an error. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries NIS2 Průvodce, Compligen, NIS2 Doku and Lexnova Energy, all four early [S16,S7]. NIS2 Průvodce is one person — Ondřej Šitler, IČO 88635783, not VAT-registered — selling against an obligation that only took effect in November 2025; Compligen publishes no IČO and carries a Q3 2026 roadmap; NIS2 Doku is a one-off document pack; Lexnova Energy s.r.o. was incorporated in January 2025 and its sibling Lexnova Services in July 2026. None has three years of selling behind it, so none closes the space: `scores.gap` 0 → 1. The de-rank recorded above was therefore too harsh — it read 'a Czech product exists' as 'the space is taken', which is the v1 test the rewrite retires. ICZ Risk*Guide is deliberately not in `locals[]`, and it is the one entry the ladder cannot represent: ICZ a.s. has traded since 1997 and is plainly not an early company, but the register holds no limb receipt for Risk*Guide and ICZ sells at the enterprise end rather than to the SME and municipal tier this record's buyers occupy — listing it would either force gap 0 on a segment it does not serve or label a 1997 systems house early. It stays named in the body. `scores.proof` 0 → 3, resolving the contradiction flagged above: Secfix (Berlin) and Copla (Vilnius) both pass the established test, in two markets, both CEE-adjacent. `score` 7 → 11. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and **ICZ Risk\*Guide is restored to the ledger** as `competes: adjacent` + `maturity: established`. It is the entry the pass above called the one the ladder could not represent, and the split resolves exactly that bind. ICZ a.s. (IČO 25145444) has traded since July 1997 and is named as a public supplier in this register's own contract signals — Digitální a informační agentura, the police presidium and Správa informačních technologií města Plzně — so it is established on a limb anyone can check, while `competes: adjacent` records that it does not sell this record's product to this record's buyer. Two corrections come with the restoration. First, the claim above that ICZ does not serve the municipal tier was wrong: the Risk\*Guide page names obce and kraje among its buyers. The real distinction is how it is bought — a modular ISMS and risk-assessment platform put in over a one-to-three-month implementation with a 24/7 advisory service attached, rather than the fixed-price product the long tail of obligated entities buys off a web page. Second, Risk\*Guide is now sold by **ICZ.Services a.s. (IČO 22183809)**, a group company incorporated in October 2024, which is why the entry carries the parent's IČO and year rather than the seller's. The four Czech NIS2 products convert to `competes: direct`, all still early. `scores.gap` stays 1 — an adjacent player never moves it — and `score` stays 11. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed.

2026-09-02 · plain-language pass — NIS2, NÚKIB, CER, IROP and ICZ glossed at first use; SME, SMB, MSP, SIEM and DORA replaced with ordinary words. Argument 424 → 376 words with every [Sn] marker, price, date and company kept, and five figures added from sources already on file: ~€6.1M Motol/Homolka [S3], ~€5.3M Prague [S4], ~121k CZK per subsidy application [S8], over a thousand entities still unregistered [S13], ICZ trading since 1997 [S16]. Corrected while tightening: "every one of these sellers is younger than the obligation itself" had swept in ICZ — the claim now names the four Czech products it is actually true of [S1,S16]. Lexnova keeps its price, repeat order and buyer type; only the quoted product name moved to the ledger and source name. First moves rewritten verbs-first with every marker and both tender links kept; a gist added beside all 16 sources. No score, status, note: field, locals[] entry or [Sn] marker touched.

2026-09-04 · price receipt — Three figures already on file are now recorded as prices: the packaged Lexnova order at about 91,000 CZK [S23], Český Brod at about 9M CZK [S24] and the NIS2 Průvodce subscription at 3,000 CZK a month per company [S25]. Compligen and NIS2 Doku are priced in the same scan, but their own pages are not on this ledger, so they stay in the note. No score, status, note, locals[] entry or marker touched.

2026-09-10 · likely solution — Added the one-sentence `solution:`, now required on every record and always shown as the likely solution, compressed from First moves 1–4 and build.note. No claim, score or source changed.

2026-09-16 · process figure and headline copy — The pieces a covered organisation buys separately are now carried as data: the scope check, the registration and its one-year clock, the paid subsidy application, the paperwork package, and the security work nobody is doing [S1,S2,S7,S8,S13,S16,S19]. Who inspects once a deadline passes is marked unknown. No score, source, note or marker changed. Same date, separate pass, merged here: headline copy — The headline was rewritten for a general builder as at most three lines under the title: a `brief:` sentence on what is happening and why it is urgent, the `solution:` as a call to action, and a new `good_for:` line. New copy, verbatim — title: "6,000 Czech towns and firms have one year to meet a new cybersecurity law"; brief: "Most deadlines fall between late 2026 and mid-2027, fines reach 2% of turnover, and a university has re-tendered for a security manager [S1,S19]."; solution: "Build a small security agency that writes their EU grant applications and does the security work."; good_for: "Cybersecurity people interested in grants and public-sector sales." Previous title, verbatim: "Six thousand Czech firms must meet new security rules, and most are not ready". Previous solution, verbatim: "A fixed-price service for the towns and care homes covered by the new Czech cybersecurity law: check what each one owes before its deadline, write the EU subsidy application where one applies, then do the security work itself rather than only the documents." Two claims in the approved draft brief were corrected against the evidence before it was written. "Must comply by 31 Dec 2026" became "between late 2026 and mid-2027": the Act starts each one-year clock on delivery of NÚKIB's registration decision, not on the notification that was due by 31 December 2025, and this record's own reading of the law puts most deadlines in Q4 2026 – H1 2027 [S1]. "Most have nobody who can do it" became the receipt behind it, a university re-tendering for the security manager the Act requires [S19]: no source on file counts how many of the 6,000 lack the people, which is why the process figure already marks that step inferred. The fine keeps the top of the scale, 2% of global turnover (or CZK 250m, whichever is higher, in the higher-obligations regime; 1.4% or CZK 175m in the lower one) [S1,S13]. No score, status, source, note, marker or body sentence changed. Second pass this date, merged here: the owner's final copy, approved after several rounds of review, replaced that draft. New copy, verbatim — title: "6,000 Czech towns and firms have months left to meet a new cybersecurity law"; brief: "Many small firms don't even know the law covers them, and the first deadlines hit in late 2026 [S1,S2]. A firm that misses its deadline can be fined up to 2% of its turnover (which is A LOT of money) [S1]."; solution and good_for unchanged. Previous title, verbatim: "6,000 Czech towns and firms have one year to meet a new cybersecurity law". Previous brief, verbatim: "Most deadlines fall between late 2026 and mid-2027, fines reach 2% of turnover, and a university has re-tendered for a security manager [S1,S19]." Previous solution, verbatim: "Build a small security agency that writes their EU grant applications and does the security work." Previous good_for, verbatim: "Cybersecurity people interested in grants and public-sector sales." "One year" became "months left" because the deadlines this record's reading of the Act places in Q4 2026 – H1 2027 are now between about three and nine months away [S1]. Each claim in the new brief was checked against the sources before it was written: that many small firms do not know the law covers them is the business association's own finding [S2]; the first deadlines fall in late 2026 because the Act took effect on 1 November 2025 and each security-measures clock runs one year from registration [S1]; and 2% of turnover is the top of the fine scale, a turnover-based fine that applies to firms [S1,S13]. The university re-tender [S19] left the brief and stays in the body. No score, status, source, note or body sentence changed. Simplified for the front page: solution "Build a small security agency that writes their EU grant applications and does the security work." → "Build a small security agency that does the security work, and writes EU grant applications for the towns that qualify.". Solution corrected, not only shortened: the EU grants this record carries go to towns, regions and hospitals, not to private firms, so the line no longer says the agency writes grant applications for the firms it serves. Title, brief and good_for unchanged. Same date, good-for opener (owner: "Good for should always start with a person"): "Cybersecurity people interested in grants and public-sector sales." became "Someone with cybersecurity skills who's interested in grants and public-sector sales." — same meaning, person first. Same date, plain-prose pilot (owner: "complex language, unstructured walls of texts … full of fluff"; spec now data/RECORD-TEMPLATE.md, "Writing the body"): every body section now opens with one answer sentence followed by one short list, with the numbers and dates people scan for set as list keys. Company names, receipt prices and Act numbers left the body, since each company now lives only in its row and each price only in its receipt, and the moves link to the section holding their evidence and carry no markers or figures. Move 1 builds a readiness check instead of selling. Cut as fluff or stale: the Europe-wide market size [S15]; the unsourced "a quarter of the 6,000 at €3,000" estimate; "Neither sells in Czechia", which no source on file supports (Secfix sells in 15+ European countries [S11]); the individual award figures for Motol, Homolka, Prague and Český Brod, which stay on the money ledger [S3,S4,S6]; and the EU fund for building security tools, which closed on 15 September 2026 [S10]. Two claims were corrected against their sources while rewriting. Copla serves fintechs and banks [S12], so "compliance software for small firms" now describes only what both companies share. And Lexnova Energy was incorporated in January 2025, before the law took effect in November 2025, so its entry no longer calls the seller younger than the obligation. The `process` step text was rewritten in plain words, with its summary now citing the evidence for each piece [S7,S8,S16]. The `comps[]` and `locals[]` lines were shortened, and every date, company number, customer claim and funding figure was kept, except the 3,000 CZK and 91k CZK prices, which live in their receipts [S23,S25]. No score, status, source, note or `entry` changed. Same date, content restored (owner: "Dont remove econtent just make it scanneable and readable"): every fact the pilot cut is back after its section's short list, cited as before, including the Act numbers, the award figures, the rough €4.5M software estimate, the Europe-wide market size and the now-closed EU fund for security tools, with The problem's list set as plain bullets and each move opening with a short lead line, and nothing stays cut except the claims corrected above.

2026-09-17 · story pass — Why now now opens on who loses what and when (a firm's fine, a town's 121,000 CZK grant application and its December cut-off, the university re-tender, the 91,000 CZK package) with the law dates moved below as plain bullets, Who pays' keyed list became plain sentences led by the number, First moves were rewritten as a five-step story whose lead sentences stand alone and explain registration and the security measures [S16], and `entry.why` now says what makes entry easier and harder (ICZ stays named in `locals[]`), with one inference marked here: that a town missing the 17 December grant deadline pays the full cost itself rests on [S9] naming no later call, and no score, status, source or entry level changed. Same date, waivers cleared: the Why now answer was cut from 32 to 24 words with its meaning kept, the care home's package price left Why now for a link to its Willing to pay receipt [S7], the moves lost every marker and figure for links to the sections holding them, and the move-only facts (the two decrees and their measures [S16], what registering means [S1], the smallest buyers' ready-made packages [S7], the documents sold as packs or online tools [S16], what a resilience plan is [S5]) now live in their home sections, with no score, status, source or entry changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now stays 3 and Willing to pay stays 2, so `score` stays 11 and the band stays PRIME; what changed is the evidence each number rests on. Why now was 3 as deadline 2 plus the freshness point, which is retired; it is now 3 as a deadline with penalties: Act No. 264/2025 is enacted and binds the towns, care homes and firms this problem sells to (REAL), their one-year deadlines fall between late 2026 and mid 2027 (CLOSE), and the Act fines up to 2% of turnover or CZK 250m, with proceedings already counted against the unregistered (TEETH) [S1,S13]. Willing to pay was 2 on recurring public spend above 5M CZK (the Prague and hospital tooling tenders), which is now public money nearby and earns nothing [S3,S4]; it is now 2 on paid receipts for this job. Tagging pass, every source on file that shows someone paying: the Napajedla care home's packaged compliance order, about 91,000 CZK in June 2026 [S23], and Český Brod's whole cyber-security job, about 9M CZK in August 2026 [S24], both signed contracts within 24 months, now tagged `dims: [money]`; the NIS2 Průvodce subscription, 3,000 CZK a month, tagged as an asking price because the ledger lists that seller as direct [S25]; and one receipt added, [S26], restating the Boskovice contract [S8] (a town paying a consultant about 121,000 CZK to write its IROP grant application, a piece of this job the solution names) as a signed-contract price. Not restated, and why: the Motol and Homolka, Prague, ČEZ Distribuce, Česká televize, Státní zdravotní ústav, Nemocnice Milosrdných bratří and NAKIT tenders buy security tooling or equipment, not the security measures and paperwork this problem sells [S3,S4,S17,S18,S20,S21,S22]; Mendel University's re-tender for an outsourced security manager is this job but names no value and no award [S19]; Týn nad Vltavou's scope analysis and the other grant applications in the [S7] and [S8] notes carry no amount and no url of their own; the Reglyze prices are foreign vendors' [S14]. The IROP call stays on file as public money nearby; its lift is not needed [S9]. Stale notes fixed: [S4] said the tenders scored money 2; [S23], [S24] and [S25] said they backed no score. `[Competition](#competition)` became `[Market gap](#competition)` in move 4. Why now and Willing to pay prose re-read against the numbers and left as written: the deadlines, the fine and the paid orders it describes are the evidence the scores now read. The 121,000 CZK figure stays in Why now and Who pays, cited to [S8], because the Why now sentence is the template's approved example. No other score, status, entry or body sentence changed. Same date, evidence audit, merged here: two new signals linked. Prague 5 is tendering two years of outside running of its security tools, estimated at 11.8M CZK, the security work itself rather than tooling; open, so public money nearby with no dims [S27]. Jihlava's psychiatric hospital, a grant applicant in [S8], signed about 22.9M CZK for security kit, IROP co-financed, not this job [S28]. Both added as Who pays detail bullets. Gap re-checked: no new local player. No score moved.
