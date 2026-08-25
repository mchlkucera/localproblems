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
  status: early
  evidence: 'a full Czech SaaS platform — twelve modules across vyhláška 409/2025 and 410/2025,
    an asset register, a 52-measure risk catalogue, a supplier register wired to ARES, NÚKIB
    incident forms with the 24/72h deadlines, training and an AI assistant over the statute —
    at 3,000 CZK a month per IČO. Operated by one person, Ondřej Šitler, not VAT-registered,
    against an obligation that only took effect in November 2025. No limb of the established
    test is on file.'
- name: Compligen
  url: https://www.compligen.cz/
  since: 2026
  status: early
  evidence: 'an online guided generator producing 20+ documents against vyhláška 410/2025 for
    the lower-obligations regime, 29,900 CZK one-off ex-VAT, with a page aimed at obce. Founder
    Lukáš Vencálek, no IČO published and no ARES match for the trade name; its own reference
    line claims 30+ firem a obcí, but the product carries a Q3 2026 roadmap and cannot have
    been selling for three years.'
- name: NIS2 Doku
  url: https://nis2doku.cz/
  since: 2025
  status: early
  evidence: 'a documentation pack — Start 4,900 CZK, Pro 11,900 CZK one-off ex-VAT, 10+
    documents per vyhláška 410/2025 plus Excel asset, incident and supplier tools — sold by
    David Mikulec against an obligation effective November 2025. No limb of the established
    test is on file.'
- name: Lexnova Energy
  url: https://www.lexnova.cz/
  ico: '22530649'
  since: 2025
  status: early
  evidence: 'sells a productised "NIS 2 package" at about 91k CZK a time, with repeat orders in
    registr smluv. Lexnova Energy s.r.o. was incorporated in January 2025 and the sibling
    Lexnova Services s.r.o. in July 2026, so the seller is younger than the obligation it
    packages.'
sources:
- type: regulation
  name: "Act No. 264/2025 Coll. (new cybersecurity act)"
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
  why: "The business association's alarm: 6,000+ firms affected across energy, manufacturing, food, logistics and digital services — and many SMEs still unaware they are in scope."
  url: https://www.sme-union.cz/zakon-o-kyberneticke-bezpecnosti-plati-lhuty-bezi/
  note: 'SME UNION: 6,000+ firms affected across energy, manufacturing, food, logistics, digital
    services; many SMEs still unaware they are in scope — documented association-level alarm
    about capacity and awareness.'
  date: '2026-12-31'
- type: tender
  name: "TED — Motol & Homolka award (~€6.1M)"
  why: "Prague's biggest hospitals bought cyber threat detection and response for ~€6.1M in June 2026 — the top of the public buying wave, with smaller hospital awards in the same window."
  url: https://ted.europa.eu/en/notice/-/detail/373331-2026
  note: 'ted-373331-2026: FN Motol + Homolka awarded ~€6.1M for cyber threat detection & response
    tooling (TED, Jun 2026); smaller hospital awards in the same window (Hustopeče ~€1.4M,
    Třebíč ~€1.2M, Národní knihovna ~€1.4M) show the buying pattern.'
  date: '2026-06-01'
  signal: ted-373331-2026
- type: tender
  name: "TED — Prague SIEM award (~€5.3M)"
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
  why: "Berlin, €10.2M Series A (Feb 2026) for AI-driven security-compliance automation for SMEs — the closest funded template for a productised NIS2 offer."
  url: https://www.vestbee.com/insights/articles/top-european-funding-rounds-closed-in-february-2026
  note: 'round-secfix: Berlin''s Secfix raised €10.2M Series A (Feb 2026) for AI-driven
    end-to-end security-compliance automation aimed at SMEs — the comps-ledger traction
    figure, now on the ledger.'
  date: '2026-02-28'
  signal: round-secfix
- type: round
  name: "Copla"
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
  why: "Sizes European cybersecurity spend at ~$69.8 billion in 2026, growing ~10.6% a year to ~$115.7 billion by 2031 — with NIS2 and DORA named as the anchor drivers."
  url: https://www.mordorintelligence.com/industry-reports/europe-cybersecurity-market
  note: 'Research 2026-08-24: Mordor Intelligence values the Europe cybersecurity market at
    USD 69.82B in 2026, forecast USD 115.66B by 2031 (10.62% CAGR), naming NIS2 and DORA
    enforcement among the primary growth drivers. Context for the market ceiling; not a
    receipt for this record''s money score.'
  date: '2026-08-24'
- type: gap-check
  name: "Czech NIS2 vendor scan"
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
created: '2026-08-13'
updated: '2026-08-25'
---

Act No. 264/2025 Coll., the Czech NIS2 transposition, pulls roughly 6,000 firms and municipalities — energy, manufacturing, food, logistics, digital services — into a regulated cybersecurity regime [S1,S2]. NÚKIB counted 4,825 registered of ~6,000 expected by February 2026 [S13]; many SMEs do not know they are in scope [S2]. Security measures fall due within a year of registration — rolling deadlines through H1 2027, fines to 2% of global turnover or CZK 250m [S1] — and the typical obligated SME or town has nobody to do the work.

Existing non-solutions: consultancies and MSPs are no longer the whole field [S2]. Czech products now sell the obligation itself. NIS2 Průvodce covers both regimes — asset register, risk catalogue, supplier questionnaires, NÚKIB incident forms — at 3,000 CZK a month, built by one person; Compligen generates the lower-regime documentation for 29,900 CZK once, with a page aimed at towns; NIS2 Doku sells the same pack from 4,900 CZK; ICZ's Risk*Guide serves the large end [S16]. Lexnova Energy's ~91k CZK "NIS 2 package" still sells off the shelf below them [S7]. Every one of these sellers is younger than the obligation itself, which took effect in November 2025 [S1] — solo operators and one-off document packs rather than settled vendors [S16].

Why now: the one-year clocks are running [S1]; NÚKIB warns the unregistered that proceedings worsen with delay [S13]; Act No. 266/2025 (CER) stacks parallel physical-resilience duties on overlapping entities [S5]; and the IROP subsidy window closes 17 December 2026 [S9].

Who pays: the roughly 6,000 regulated entities themselves — compelled by law, not persuaded [S1,S13]. Public buyers alone placed ~77 cyber-security awards worth ~€33M in June–August 2026 [S7]. The receipts below run from Prague's biggest hospitals [S3,S4] down to a town of 7,000 people [S6]. Behind the awards sits a ~€99.6M IROP subsidy pot [S9], and towns pay consultants just to enter it [S8]. Compliance tooling sells at €500–6,000 per firm a year [S14], and the smallest Czech buyers already pay ~€3,700 for an off-the-shelf package [S7]. A €3,000-a-year product bought by a quarter of the 6,000 is ~€4.5M a year — a conservative floor before the implementation services where the €33M sits [S14]. The backdrop is European cybersecurity spend of ~$70 billion in 2026, growing ~11% a year on NIS2 and DORA [S15].

Solved elsewhere: Secfix (Berlin, €10.2M Series A) sells compliance automation to hundreds of SMBs across 15+ European countries [S11]; Copla (Vilnius, €6M Series A) covers NIS2, DORA and ISO 27001 [S12] — small teams already package exactly this obligation, neither of them found operating in Czechia.

## First moves

1. Sell where buying is already documented: social-care institutions and towns around the 7,000-inhabitant tier. A care home bought a ~91k CZK "NIS 2 package" off the shelf, with a repeat order weeks later, and Týn nad Vltavou paid just to learn its scope [S7]; Český Brod signed ~9M CZK, and 341 cyber contracts sit in the registry since June [S6].
2. Package the gap analysis first: a fixed price for mapping one entity against Act 264/2025 and Vyhláška 409/2025, keyed to its one-year clock [S1] — the off-the-shelf form is what the smallest obligated tier demonstrably buys [S7].
3. Ride the subsidy channel: [IROP 120 Kybernetická bezpečnost II](/sources/tenders#dotace-irop-120-kyberbezpecnost) offers ~€99.6M for municipalities, regions and hospitals, applications open to 17 December 2026 [S9] — towns already pay consultants just to write the applications [S8], so application-writing plus implementation is a subsidy-funded entry offer. Builder-side, [HORIZON-CL3-2026-02-CS-ECCC](/sources/tenders#dotace-horizon-eccc-cyber-2026) (€56.2M, deadline 15 September 2026) funds the tooling itself [S10].
4. Enter against named Czech products, not an empty field: the small-entity tier is already served at 3,000 CZK a month (NIS2 Průvodce), 29,900 CZK once (Compligen) and 4,900 CZK once (NIS2 Doku) [S16]. What none of them sells is the implementation labour the ~€33M of public awards actually buys [S7] — the documentation is productised, the doing is not.
5. Same buyer, second product: the CER law's physical-resilience obligations land on an overlapping entity set through 2027 [S5] — the natural upsell to every NIS2 customer.
6. Competition on file: NIS2 Průvodce, Compligen, NIS2 Doku and ICZ Risk*Guide sell the compliance product [S16]; Lexnova Energy sells repeat packages, Institut kybernetické bezpečnosti scope analysis and enovation the subsidy applications [S7,S8]; the consultancy and MSP field sits behind them. Abroad, Secfix [S11] and Copla [S12] prove the same model at Series A scale.

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-13 · money and demand receipted — The first successful TED run put the buying wave on the record across the full size spectrum, from Motol and Prague at the top to care homes and small towns ordering productised "NIS 2 packages" below the threshold, with an IROP subsidy channel behind the municipal projects [S3,S4,S7,S8]. That substance now sits in How big rather than here. Noted for the gap dimension at the time: Lexnova's repeat package sales and Institut kybernetické bezpečnosti's scope-analysis product are the first evidence that productised CZ offerings for the small-entity tier are emerging [S7].

2026-08-24 · board-brief rewrite — The body was rewritten to the builder-first template (problem → proven abroad → local competition → how big → why now), cutting the argument from 440 to ~335 words with no claim added beyond its source. Market research joined the record: NÚKIB's own registration tally (4,825 of ~6,000 expected, Feb 2026) [S13], per-firm NIS2 tooling prices (Reglyze from €490/yr, Secfix ~€500/mo, Vanta/Drata ~$7,500/yr) [S14], and the ~$70bn 2026 European cybersecurity market with NIS2/DORA as named drivers [S15] — grounding a bottom-up floor of ~€4.5M/yr for a productised Czech offer (6,000 entities × €3,000/yr × 25%). Every source gained a public name and why line; internal notes, scores and status untouched.

2026-08-25 · market check — The Czech field was searched in Czech for the first time and it is not empty: four named products sell NIS2 compliance to the obligated mid-market, from a one-person SaaS at 3,000 CZK a month to a documentation pack at 4,900 CZK, plus ICZ's Risk*Guide at the enterprise end [S16]. `scores.gap` was already 0 and stays 0 — nothing here can raise it — but `status` moves candidate → watching under the SPEC §4 de-rank rule, and "Existing non-solutions" and First moves 4 and 6 now name the incumbents instead of asking for the survey that has now been run. `score` is unchanged at 7. Method note for the next check: none of the four products appears anywhere in the 11,330-signal corpus — none raised and none sells through public tender — so only Czech-language search could find them. Positive control: the same method run at Wultra (the incumbent named on p-0017) surfaced it, so the negatives in this pass are worth something. Flagged, NOT changed: `scores.proof` is 0 while Secfix (€10.2M Series A) and Copla (€6M Series A) sit on the comps ledger — the recommended value is 3 (funded analogs in two markets, one of them CEE-adjacent), and `scripts/check-records.py` already reports the contradiction as an error. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries NIS2 Průvodce, Compligen, NIS2 Doku and Lexnova Energy, all four early [S16,S7]. NIS2 Průvodce is one person — Ondřej Šitler, IČO 88635783, not VAT-registered — selling against an obligation that only took effect in November 2025; Compligen publishes no IČO and carries a Q3 2026 roadmap; NIS2 Doku is a one-off document pack; Lexnova Energy s.r.o. was incorporated in January 2025 and its sibling Lexnova Services in July 2026. None has three years of selling behind it, so none closes the space: `scores.gap` 0 → 1. The de-rank recorded above was therefore too harsh — it read 'a Czech product exists' as 'the space is taken', which is the v1 test the rewrite retires. ICZ Risk*Guide is deliberately not in `locals[]`, and it is the one entry the ladder cannot represent: ICZ a.s. has traded since 1997 and is plainly not an early company, but the register holds no limb receipt for Risk*Guide and ICZ sells at the enterprise end rather than to the SME and municipal tier this record's buyers occupy — listing it would either force gap 0 on a segment it does not serve or label a 1997 systems house early. It stays named in the body. `scores.proof` 0 → 3, resolving the contradiction flagged above: Secfix (Berlin) and Copla (Vilnius) both pass the established test, in two markets, both CEE-adjacent. `score` 7 → 11.
