---
id: p-0024
region: cz
title: Czech building owners face the EPBD retrofit wave with no portfolio analytics — the
  implementing law is overdue, infringement pressure is on, and Berlin already has a funded
  product
category: housing
geo: CZ-national
score: 6
scores:
  proof: 2
  money: 1
  urgency: 2
  demand: 0
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Analytics SaaS over energy-certificate and portfolio data with no certification gate — a dev plus an energy-domain expert can pilot with a mid-size landlord; the real cost is B2B integration and sales effort.'
comps:
- name: 'Fuchs & Eule'
  url: https://fuchs-eule.de/
  geo: DE
  since: 2021
  traction: '€10M round led by GET Fund (TechFundingNews, 2026); 10,000 building analyses; serves commercial landlords and asset managers'
  signal: de-fuchs-eule
- name: Predium
  url: https://en.predium.de/
  geo: DE
  since: 2021
  traction: '€13M Series A led by Norrsken VC (Tech.eu, 2024); ~$21M total raised; customers incl. Colliers, Baloise, Deutsche Investment'
- name: Deepki
  url: https://www.deepki.com/
  geo: FR
  since: 2014
  traction: '€150M Series C (One Peak/Highland, 2022); 500+ clients, 50,000 users, €4T AUM monitored in 80 countries (PR Newswire, 2025)'
  markets: [GB, DE, ES, IT, NL, DK, CH, US, SG, AU]
sources:
- type: arbitrage
  name: "Fuchs & Eule"
  why: "Berlin, €10M raised in July 2026 for AI building-retrofit analytics that screen landlord and asset-manager portfolios — 10,000 building analyses done. The closest template."
  url: https://techfundingnews.com/fuchs-eule-raises-10m-commercial-landlords-esg/
  note: 'de-fuchs-eule: Fuchs & Eule (Berlin) raised €10M (GET Fund, 8 Jul 2026) for AI building-retrofit
    analytics — screens landlord/asset-manager portfolios for ESG and energy-retrofit needs;
    10,000 building analyses done. Funded DE analog, CEE-adjacent: arbitrage 2.'
  date: '2026-07-08'
  signal: de-fuchs-eule
- type: gap-check
  name: "Czech retrofit-analytics scan (first pass)"
  why: "The early look at the Czech field: certificate consultancies work building by building, with PKV Build the scale player, and no self-serve portfolio retrofit-analytics software was found."
  url: https://techfundingnews.com/fuchs-eule-raises-10m-commercial-landlords-esg/
  note: 'Quick check 2026-08-13: CZ side shows certificate consultancies (PKV Build does energy
    certificates at scale) but no self-serve portfolio retrofit-analytics software. Gap 1
    (quick search only).'
  date: '2026-08-13'
- type: regulation
  name: "EPBD recast — Commission infringement notice"
  why: "Transposition of Directive 2024/1275 was due 29 May 2026; on 15 July 2026 the Commission opened infringement procedures against all 27 Member States including Czechia."
  url: https://energy.ec.europa.eu/news/commission-calls-eu-countries-transpose-reinforced-rules-energy-performance-buildings-2026-07-15_en
  note: 'reg-epbd-recast: EPBD recast (2024/1275) transposition was due 29 May 2026; on 15
    Jul 2026 the Commission opened infringement procedures against all 27 Member States incl.
    CZ. Obligations (BACS for large non-residential, zero-emission new builds, renovation
    passports, solar-readiness) phase in from a compressed CZ implementing law. Deadline 1
    (dates not yet fixed in CZ law).'
  date: '2026-07-15'
  signal: reg-epbd-recast
- type: tender
  name: "TED — the Czech energy-performance-contracting wave (~€58M)"
  why: "Klatovy hospital's ~€8.3M award is one of 15 records from 11 distinct public buyers between June and August 2026 — the retrofit spend a portfolio-analytics layer would front-end."
  url: https://ted.europa.eu/en/notice/-/detail/384935-2026
  note: 'ted-384935-2026: Klatovská nemocnice awarded ~€8.3M for energy performance contracting
    (Jun 2026) — part of an EPC wave of 15 TED records from 11 distinct public buyers (~€58M
    distinct value) in Jun–Aug 2026: three Plzeň-kraj hospitals in one week (Stod ~€3.3M,
    Domažlice ~€5.3M, Klatovy), Praha 6 ~€15.7M, Praha 16/18, Hodonín, Kuřim, ČD. Public
    owners are paying for retrofit triage-plus-delivery through ESCOs — adjacent execution
    spend, so money scored 1 (relevant tenders exist), not 2: the tenders buy EPC delivery,
    not the portfolio-analytics layer this record is about.'
  date: '2026-06-04'
  signal: ted-384935-2026
- type: gap-check
  name: "Enmon, ENERGOMETR and the Czech portfolio-software field"
  why: "A Czech-language sweep for portfolio retrofit planning. It found monitoring and ESG reporting — Enmon by PKV, ENERGOMETR by DEKSOFT — but no renovation roadmap, measure prioritisation or capex modelling."
  url: https://www.pkv.cz/en/energeticky-management
  note: 'Gap re-check 2026-08-20: looked for a Czech product that screens a PORTFOLIO of buildings
    for retrofit need and sequence — which building, which measure, in what order, at what capex
    — the Fuchs & Eule / Predium shape, as distinct from per-building certificates. Not found.
    What exists is adjacent, and was checked rather than assumed. Enmon (PKV) is a portfolio
    energy-management and sustainability platform, implemented at CTP, but its own pages describe
    automatic 15-minute consumption collection, carbon-footprint calculation and ESG/non-financial
    reporting, with no renovation roadmap, no measure prioritisation and no capex modelling.
    ENERGOMETR (DEKSOFT) likewise consolidates consumption across buildings and provides tables,
    graphs and reports. renovacnipas.cz (EnergySim), the SFŽP renovation-pass application and
    the ufae.cz calculation tool are all single-building and aimed at homeowners or energy
    specialists, and the renovation pass is an NZÚ application artifact rather than a portfolio
    product. Portfolio tools sold into CZ (IBM Envizi, Deepki) reach owners through CBRE-type
    advisory, not as a Czech product. NOT FOUND IS NOT ABSENT: gap stays 1 and score stays 6
    — a search that returns nothing is not evidence that nothing exists, and the surfaces listed
    below are the whole of the coverage claimed here. Flag for the next pass: PKV, named in this
    record as the per-building certificate scale player, also ships portfolio software, so the
    distinction this record rests on is monitoring-versus-retrofit-planning and is narrower than
    the body currently implies.'
  date: '2026-08-20'
  queries:
    - "software energetický management portfolia budov analýza renovace dekarbonizace ESG nemovitosti Česko"
    - "software renovační pas dekarbonizační plán budov portfolio CRREM analýza opatření úspor Česko"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
created: '2026-08-13'
updated: '2026-08-25'
---

The recast Energy Performance of Buildings Directive obliges member states to drive building automation retrofits, renovation passports, zero-emission new construction and solar-readiness — and Czechia, like all 27 member states, missed the May 2026 transposition deadline and received a Commission infringement procedure in July [S3]. The implementing law now arrives compressed and retroactively urgent [S3], and with it a rolling obligation wave for building owners: which buildings need BACS, which need envelope work, in what order, at what capex.

Why now: portfolio owners cannot answer those questions with what is on the Czech shelf — portfolio platforms here do consumption monitoring and ESG reporting (Enmon by PKV, ENERGOMETR by DEKSOFT), certificate consultancies work one building at a time, and the search found no product that plans and sequences retrofit measures with capex across a portfolio [S2,S5]. In Berlin, Fuchs & Eule just raised €10M for exactly this product and has run 10,000 building analyses [S1]; the regulatory driver (EPBD + ESG reporting) is identical in Czechia, offset by roughly the transposition lag.

The Czech implementing dates are not yet fixed [S3] — the infringement procedure makes acceleration likely, and the moment the law publishes with dates, this record's urgency and rank should jump.

Who pays: commercial and institutional building owners triaging retrofit capex. Municipal building stock — obligated early under EPBD's public-building provisions — is a procurement channel. The money side is documented in the EPC market: 11 public buyers awarded ~€58M of energy-performance contracting between June and August 2026, including three Plzeň-region hospitals in a single week [S4]. That is exactly the spend a portfolio-analytics layer front-ends — which buildings, in what order, at what capex — documented in adjacent tenders [S4].

Existing non-solutions: energy specialists issuing PENB certificates one building at a time (PKV Build the scale player) [S2], and portfolio energy-management platforms that monitor consumption and report ESG but carry no renovation roadmap, measure prioritisation or capex modelling — Enmon (PKV) and ENERGOMETR (DEKSOFT) [S5]. The position this record tracks is the owner-side retrofit-planning product, not retrofit delivery [S2,S5] — and the distinction is monitoring versus retrofit planning, narrower than an empty field [S5].

Solved elsewhere: building-portfolio decarbonisation analytics is a well-funded European category. Predium (Munich) raised a €13M Series A and counts Colliers and Baloise as customers, Fuchs & Eule (Germany) raised €10M on the back of 10,000 building analyses, and Deepki (Paris) monitors €4 trillion of assets across 80 countries after a €150M Series C [S1]. Each sells the owner-side analytics layer Czech owners still lack.

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed.
2026-08-13 · money receipted — The EPC award wave was put on the ledger — 11 public buyers, ~€58M between June and August 2026 [S4] — carrying money to 1. The substance now sits in How big above rather than here.

2026-08-20 · evidence audit — Removed the EPC supplier-side sentence: the four named companies and associations (ENESA, ČEZ ESCO, MVV, APES) return no hits anywhere in the signal corpus and appear in no source note on this record, and the maturity verdict attached to them had nothing behind it either. The clause that survives, that the unoccupied position is the owner-side analytics product, is the record's own gap check and is now cited to [S2]. Also removed from "Who pays": the claim that banks pricing green mortgages and sustainability-linked loans are a second buyer, since no green-mortgage receipt exists in the corpus.

2026-08-24 · fact check — The window paragraph claimed owners have "no analytics layer, only per-building energy-certificate consultancies"; the record's own re-check found two Czech portfolio energy-management platforms (Enmon by PKV, ENERGOMETR by DEKSOFT) and flagged that the real distinction is monitoring versus retrofit planning, "narrower than the body currently implies" [S5]. The body now names both and claims only what was checked: no retrofit-planning product found, gap unchanged at 1. Enmon's own page was re-verified live on this date — 15-minute consumption collection and ESG reporting, no renovation planning [S5]. The unreceipted "ESG consultancies producing PDFs, and spreadsheets" flourish is gone.
