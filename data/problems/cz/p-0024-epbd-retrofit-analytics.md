---
id: p-0024
region: cz
title: 'Czech towns and hospitals face EU building-upgrade rules, and Czechia is already late'
brief: 'The EU has started proceedings against Czechia for missing its deadline, so Czech rules are coming [S3]. Owners with many buildings will have to decide which to fix first, and at what cost.'
solution: 'Build software that reads an owner''s energy data and ranks which building to renovate first and at what cost, as 3 companies already do in 2 other countries.'
good_for: 'Someone who understands building energy use and can sell to hospitals and towns through tenders.'
draft_law: 'Czech law for the EU building rules, not yet passed [S3]'
price_search: 'Registr smluv full-text for "energetický management" or "energetický audit" —
  what a kraj (region) or statutory city pays a consultancy to survey and rank its building
  stock is the manual equivalent of the product; the MS2021+ index under "energetického
  managementu" names the owners (Statutární město Liberec, Středočeský kraj) but funds only
  their retrofit delivery, so ask the energy manager (energetický manažer) of either what the
  portfolio triage behind those projects cost.'
category: housing
geo: CZ-national
score: 7
scores:
  proof: 3
  money: 2
  urgency: 1
  demand: 0
  gap: 1
status: candidate
entry:
  level: hard
  buyer: public
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: nothing licenses the work, the ranking runs on energy data and certificates the owner already holds, and public owners already pay for renovations. Harder: the owners with the money are hospitals, districts and regions, so each sale goes through a tender; and the Czech dates that force the choice are not set.'
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
  traction: '€150M Series C (One Peak/Highland, 2022); 500+ clients, 50,000 users, €4T AUM monitored in 80 countries (PR Newswire, 2025). Beyond monitoring, it sells CapEx planning and virtual retrofits that simulate the impact of renovation investments against CRREM and custom targets (https://www.deepki.com/, read 2026-09-16)'
  markets: [GB, DE, ES, IT, NL, DK, CH, US, SG, AU]
locals:
- name: PKV BUILD (Enmon, PENB certificates)
  url: https://www.pkv.cz/en/energeticky-management
  ico: '28149785'
  since: 2013
  competes: adjacent
  maturity: established
  evidence: It sells single-building energy-performance assessments and the Enmon monitoring platform,
    which collects consumption every 15 minutes and reports sustainability — no renovation roadmap,
    no ranking of measures and no capex modelling in the software [S2,S5]. As a consultant it does
    that ranking by hand, and the state development bank pays it to judge which of the Plzeň region's
    buildings suit an energy-savings contract [S9]. That is a paid study, not a product that ranks.
    Trading since 2013, with customers including the property group CTP, where Enmon is installed
    [S5].
- name: DEKSOFT (ENERGOMETR)
  url: https://deksoft.eu/programy/energometr
  ico: '27636801'
  since: 2006
  competes: adjacent
  maturity: early
  evidence: It sells ENERGOMETR, which consolidates consumption across many buildings into tables,
    graphs and reports [S5] — monitoring, one product over from the retrofit planning this space
    is about. Parent DEK a.s. has traded since 18 December 2006, but nothing names who runs ENERGOMETR
    and no count is published, so its reach is unknown.
- name: EnergySim (renovacnipas.cz)
  url: https://renovacnipas.cz/
  competes: direct
  maturity: early
  evidence: It sells a renovation-pass calculator to homeowners and energy specialists [S5] —
    the same retrofit-planning job, one building at a time rather than ranked across a portfolio.
    No start year, no buyer names and no count are published, so its reach is unknown.
- name: ENSYTRA (EnergyBroker)
  url: https://www.ensytra.cz/
  ico: '28582136'
  since: 2009
  competes: adjacent
  maturity: established
  evidence: An energy consultancy that sells the EnergyBroker web app, which records each site's
    energy use and costs, reports them and runs energy purchasing [S9]. It ranks buildings by hand
    — for a public university it writes a card on each building with measures, cost and payback,
    then sets priorities [S9]. That is a paid study, not software that ranks. Trading since 2009;
    named customers on its own offer include the City of Prague, the Olomouc region and Olomouc's
    faculty hospital [S9].
- name: EnMass (Vision)
  url: https://www.enmass.cz/
  ico: '13968050'
  since: 2021
  competes: adjacent
  maturity: early
  evidence: An Ostrava energy consultancy that also sells Vision, software showing a client's energy
    use, costs and operations in real time [S9]. It ranks buildings by hand — a hospital hired it in
    August 2026 to go through its buildings and say which belong in an energy-savings contract [S9].
    That is a paid study, not software that ranks. Registered in November 2021; its site names no
    customers, and one hospital contract is on file, so how much it sells is unknown [S9].
sources:
- type: arbitrage
  name: "Fuchs & Eule"
  gist: "the Berlin €10M template"
  why: "Berlin, €10M raised in July 2026 for AI building-retrofit analytics that screen landlord and asset-manager portfolios — 10,000 building analyses done. The closest template."
  url: https://techfundingnews.com/fuchs-eule-raises-10m-commercial-landlords-esg/
  note: 'de-fuchs-eule: Fuchs & Eule (Berlin) raised €10M (GET Fund, 8 Jul 2026) for AI building-retrofit
    analytics — screens landlord/asset-manager portfolios for ESG and energy-retrofit needs;
    10,000 building analyses done. Funded DE analog, CEE-adjacent: arbitrage 2.'
  date: '2026-07-08'
  signal: de-fuchs-eule
- type: gap-check
  name: "Czech retrofit-analytics scan (first pass)"
  gist: "the first Czech scan"
  why: "The early look at the Czech field: certificate consultancies work building by building, with PKV Build the scale player, and no self-serve portfolio retrofit-analytics software was found."
  url: https://techfundingnews.com/fuchs-eule-raises-10m-commercial-landlords-esg/
  note: 'Quick check 2026-08-13: CZ side shows certificate consultancies (PKV Build does energy
    certificates at scale) but no self-serve portfolio retrofit-analytics software. Gap 1
    (quick search only).'
  date: '2026-08-13'
- type: regulation
  name: "EPBD recast — Commission infringement notice"
  gist: "the missed May 2026 deadline"
  why: "Transposition of Directive 2024/1275 was due 29 May 2026; on 15 July 2026 the Commission opened infringement procedures against all 27 Member States including Czechia."
  url: https://energy.ec.europa.eu/news/commission-calls-eu-countries-transpose-reinforced-rules-energy-performance-buildings-2026-07-15_en
  note: 'reg-epbd-recast: EPBD recast (2024/1275) transposition was due 29 May 2026; on 15
    Jul 2026 the Commission opened infringement procedures against all 27 Member States incl.
    CZ. Obligations (BACS for large non-residential, zero-emission new builds, renovation
    passports, solar-readiness) phase in from a compressed CZ implementing law. Deadline 1
    (dates not yet fixed in CZ law).
    Rescored 2026-09-19: the deadline sub-score and freshness are retired. On the 2026-09-19
    ladder an untransposed directive fails REAL (it binds the state, not the owner, and the
    record carries draft_law:), so this backs urgency 1; the infringement case targets Czechia.'
  date: '2026-07-15'
  signal: reg-epbd-recast
- type: tender
  name: "TED — the Czech energy-performance-contracting wave (~€58M)"
  gist: "the €58M retrofit wave"
  why: "Klatovy hospital's ~€8.3M award is one of 15 records from 11 distinct public buyers between June and August 2026 — the retrofit spend a portfolio-analytics layer would front-end."
  url: https://ted.europa.eu/en/notice/-/detail/384935-2026
  note: 'ted-384935-2026: Klatovská nemocnice awarded ~€8.3M for energy performance contracting
    (Jun 2026) — part of an EPC wave of 15 TED records from 11 distinct public buyers (~€58M
    distinct value) in Jun–Aug 2026: three Plzeň-kraj hospitals in one week (Stod ~€3.3M,
    Domažlice ~€5.3M, Klatovy), Praha 6 ~€15.7M, Praha 16/18, Hodonín, Kuřim, ČD. Public
    owners are paying for retrofit triage-plus-delivery through ESCOs — adjacent execution
    spend, so money scored 1 (relevant tenders exist), not 2: the tenders buy EPC delivery,
    not the portfolio-analytics layer this record is about.
    Rescored 2026-09-19: "money scored 1 (relevant tenders exist)" names the retired rung. On
    the 2026-09-19 ladder these awards are public money nearby: they buy renovation delivery,
    with the choice of measures bundled into it and not priced, so none is restated as a price
    receipt for the ranking. No price for this job is on file, so money is 0.
    Willing to pay search 2026-09-19: the choice of WHICH buildings go into such a contract is also
    bought on its own, before it, from consultants: a hospital (S7), a public university (S8) and the
    state development bank''s EPC advisory programme (S9). Money is 2 on S7 and S8; this row stays
    public money nearby, and the choice of measures inside these awards is still unpriced.'
  date: '2026-06-04'
  signal: ted-384935-2026
- type: gap-check
  name: "Enmon, ENERGOMETR and the Czech portfolio-software field"
  gist: "the Czech portfolio-software sweep"
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
- type: arbitrage
  name: "aedifion"
  gist: "the €17M controls layer"
  why: "Cologne's aedifion raised a €17M Series B for the cloud layer that sits on a building's existing control system and tunes heating, ventilation and cooling — the building-automation half the directive forces — reporting close to 500 buildings and over 5.8 million square metres under management."
  url: https://tech.eu/2025/06/24/aedifion-secures-eur17m-in-series-b-round/
  note: 'de-aedifion: EUR 17M oversubscribed Series B led by Eurazeo with World Fund, Drees
    und Sommer, BitStone Capital, Phoenix Contact Innovation Ventures, MOMENI Ventures, Bauwens
    Capital and LARTIS, reported 2025-06-24; ~500 buildings and 5.8M m2 across Europe, Britain
    and the United States. Cited as the ADJACENT European layer, not as proof of this record''s
    product: aedifion optimises how a building runs, where this record ranks which building to
    renovate and in what order. What makes it worth carrying is the Czech check attached to it,
    run 2026-09-03 on google-cz, ares and the own funded ledger: BUILDSYS a.s. (IČO 27690253,
    since 2006) integrates building-management systems, HGS a.s. sells the FLOWBOX energy
    orchestration software and Novatec EAS does commercial-building energy management, with
    Schneider Electric and Trane selling the international products here — and the EU-taxonomy
    and ESG reporting layer is served by consultancies such as PwC Czech Republic rather than by
    a building-operations product. No Czech vendor was found joining continuous cloud
    optimisation to taxonomy-grade reporting. Those three Czech names are NOT on this record''s
    ledger and are flagged for a content pass to adjudicate into locals[]; on the reading here
    each sells integration or monitoring rather than the renovation ranking this record names,
    so none is expected to move gap. dims empty: it is neither proof of this product nor a gap
    finding this pass is entitled to score.'
  date: '2025-06-24'
  signal: de-aedifion
  dims: []
- type: price
  url: https://smlouvy.gov.cz/smlouva/39161854
  name: "Nemocnice Kyjov — which of 28 buildings to renovate, August 2026"
  gist: "a hospital pays for the ranking"
  why: "What a regional hospital paid a consultant, after its own small tender, to go through 28 of its buildings, cost the savings measures in each and say which belong in its energy-savings contract."
  note: 'Registr smluv 39161854 (idSmlouvy 36811042), concluded 14 August 2026, signed electronically:
    Nemocnice Kyjov, příspěvková organizace (IČO 00226912) and EnMass s.r.o. (IČO 13968050),
    smlouva o dílo 0195-26 after the small public contract "Analýza vhodnosti EPC 2026 budov
    Nemocnice Kyjov" (VZ202633). Clause I.1: "vypracování analýzy metody EPC pro přípravu energeticky
    úsporného projektu anebo projektů, která musí obsahovat detailní analýzu i celkové závěrečné
    doporučení/nedoporučení ohledně vhodnosti použití metody EPC ... pro jednotlivé vybrané objekty a
    budovy". Annex 1 lists 28 buildings (27 pavilions in Kyjov and the Veselí nad Moravou outpatient
    site) and asks for, per building, measures "včetně opatřeních na obálkách budov", "Stanovení
    předpokládaných investičních nákladů a stanovení přínosů", then "Doporučení, které z vybraných
    objektů je vhodné zařadit do připravovaného projektu EPC", "Návrh optimální skladby objektů" and a
    table "Potenciál energeticky úsporných opatření – souhrn hodnocených budov"; delivery within 4
    months. Clause VI.3: "cena bez DPH 349 000,- Kč", 422,290 CZK incl. VAT, a maximum price, on the
    supplier''s offer of 1 July 2026. Contract text read through the Hlídač státu API, 2026-09-19.
    This is THE JOB: deciding which of an owner''s buildings to renovate, with the cost of each, bought
    on its own and by hand before the renovation is tendered. basis signed-contract, one month before
    updated: a PAID receipt, money 2.'
  date: '2026-08-14'
  payer: 'Nemocnice Kyjov, a regional hospital'
  amount_czk: 349000
  unit: per-project
  basis: signed-contract
  dims: [money]
- type: price
  url: https://smlouvy.gov.cz/smlouva/36133585
  name: "Univerzita Palackého — building cards and priorities, December 2025"
  gist: "a university pays for the ranking"
  why: "What a public university paid an energy consultancy to survey its buildings, cost the savings measures in each and name which buildings to do first."
  note: 'Registr smluv 36133585 (idSmlouvy 33905857): order 4590019406 of 16 December 2025, accepted
    by the supplier on 18 December 2025, Univerzita Palackého v Olomouci (IČO 61989592), a public
    university, to ENSYTRA s.r.o. (IČO 28582136), "Zpracování pasportu budov a energetické koncepce
    univerzity". The attached offer of 21 November 2025: stage 1, "Karty budov (Technicko-energetické
    posouzení objektů)", a survey of each building ending in "Návrh úsporných opatření, včetně
    orientačního odhadu investičních nákladů a návratnosti" and "přehledná databáze všech hodnocených
    objektů"; stage 2, the university''s energy concept, including "Komplexní vyhodnocení zjištění z
    karet budov – identifikace objektů s nejvyšším potenciálem úspor a návrh priorit", an economic
    evaluation of the measures and an energy action plan; within 4 months. Order total "379 940,00"
    CZK incl. VAT, 314,000 CZK excl. VAT (the registry value). The offer''s price table, as its text
    layer reads, lists 12,000 CZK per building card without a solar design, 22,000 CZK with one and
    280,000 CZK for the concept; how the 314,000 CZK splits between cards and concept cannot be read
    from the text layer, so the order total is the amount here. Contract text read through the Hlídač
    státu API, 2026-09-19. The payer is a public owner of many buildings, `entry.buyer: public`, though
    not a town or a hospital. basis signed-contract, nine months before updated: a PAID receipt.'
  date: '2025-12-18'
  payer: 'Univerzita Palackého v Olomouci, a public university'
  amount_czk: 314000
  unit: per-project
  basis: signed-contract
  dims: [money]
- type: contract
  url: https://smlouvy.gov.cz/smlouva/36385285
  name: "Registr smluv — public owners paying to have their buildings ranked, 2025 to 2026"
  gist: "the paying owners"
  why: "The public contracts register shows a hospital and a university paying consultants to rank their buildings, and a state advisory programme that buys the same analysis for regions, towns and hospitals."
  note: 'Hlídač státu API full-text search of the contracts register, 2026-09-19, every query limited
    to contracts concluded from 2024-09-19: "pasportizace budov" AND energetick* (10 hits); "energetického
    managementu" AND budov (682); "energetická koncepce" AND budov (74); prioritizace AND budov AND
    energetick* (45); "karty budov" AND energetick* (4); EPC AND ("výběr objektů" OR "vhodnosti
    objektů" OR "vhodných objektů" OR "analýza objektů") (0); pasport budov AND úsporných opatření (5);
    "energetický audit" AND (nemocnice OR kraj OR "statutární město") AND (objektů OR budov) (84); plán
    renovace / renovační strategie / plán obnovy budov AND energetick* (4); ("analýza vhodnosti" OR
    "posouzení vhodnosti" OR "studie vhodnosti" OR "studie proveditelnosti") AND EPC (123); EPC AND
    poradenství/příprava projektu AND budov/objektů under 3M CZK (102). First pages read by title;
    texts read where the title could be this job.
    PAID BY THE OWNER, texts read, restated as receipts: Nemocnice Kyjov, 14 August 2026, 28 buildings,
    EnMass s.r.o. (S7); Univerzita Palackého v Olomouci, 18 December 2025, ENSYTRA s.r.o. (S8).
    THE STATE PROGRAMME, texts read: Národní rozvojová banka (IČO 44848943) holds a framework agreement
    of 9 December 2024 for EPC advisory and places each client with an adviser by mini-tender. Minitendr
    24, Plzeňský kraj, NRB and PKV BUILD s.r.o., 7 January 2026 (this URL, 3,039,300 CZK excl. VAT):
    "Analýza vhodnosti metody EPC – zpracování vstupní analýzy vhodnosti využití metody EPC" 759,825 CZK
    excl. VAT, beside the grant application 759,825, the ESCO tender documents 607,860 and tender
    assistance 911,790. Client contract 2025-4398, Statutární město Jablonec nad Nisou with NRB, 4
    September 2025 (registr smluv 34755853): advice "Spolufinancováno z programu Evropské unie Invest EU,
    z technické asistence ELENA ... Evropské investiční banky"; clause 4.1, the client pays a fee of
    at least 10 % of the adviser''s price and "maximálně 90 %" is paid from ELENA; maximum price
    1,935,000 CZK excl. VAT, of which "Analýza vhodnosti metody EPC" 638,550 CZK; the analysis visits
    every building and must hold "Způsob výběru objektů vhodných pro projekt EPC - určení a popis
    kritérií, na základě kterých došlo k rozdělení (vyřazení) objektů", "Celkový seznam objektů/(budov)
    s uvedením vhodnosti, nebo nevhodnosti" and every measure per building with its investment cost.
    Other NRB adviser contracts, by metadata only: ENVIROS for FN Brno (34062325), Šumperk (34345657),
    Univerzita Hradec Králové (34345661) and Jablonec I and II; PKV BUILD for VFN (33739273), Liberecký
    kraj (33188956) and Středočeský kraj (36033565); PORSENNA ENERGY for Těrlicko, Praha 5 and Slaný;
    VŠB-TU Ostrava for Pardubický kraj, Opava and the Liberec regional police; SEVEn Energy for AMU;
    LOYD GROUP for the Hradec Králové regional police. WHY THIS ROW IS NOT A PRICE RECEIPT: the bank
    pays the adviser and the owner pays the bank a fee of at least 10 %, so what the owner itself pays
    for the analysis is not on file; it is public money nearby, and it is not needed as a lift, S7 and
    S8 being paid.
    THE SELLERS, read on their own sites 2026-09-19: ENSYTRA (ensytra.cz, energybroker.cz), an
    independent energy consultancy "od roku 2009", sells the EnergyBroker web app for energy
    management (consumption and cost records per supply point, reports, supplier auctions, gradual
    purchasing) and KUBIA facility software; its UP offer names clients incl. Hlavní město Praha,
    Olomoucký kraj, Karlovarský kraj and Fakultní nemocnice Olomouc. EnMass (enmass.cz, IČO 13968050,
    ARES: registered 11 November 2021, Ostrava) sells advisory and "Software Vision", data "o
    spotřebě, nákladech i provozu v reálném čase"; its site names no customers. Neither page offers a
    ranking of renovations; both sell the ranking as consultancy.
    NEXT DOOR, READ AND NOT COUNTED: (a) energy-management systems under ISO 50001 — Město Ústí nad
    Orlicí and PORSENNA ENERGY, 19 December 2024 (31577440), 367,500 CZK excl. VAT, 36 buildings,
    funded under call NPO 2/2024: a baseline review, an action plan and monitoring software, where
    "stanovení priorit" means the system''s targets; Hlavní město Praha and Gatum Group, 11 May 2025
    (33240436), 890,000 CZK, an implementation plan whose "prioritizace" is the order of rolling out
    the system across building groups; statutární město Plzeň and Gatum Group, 10 June 2026 (38328907),
    767,000 CZK, the same. (b) The statutory energy audit of a whole estate under § 9 of Act 406/2000
    and decree 140/2021 — Město Ivančice and Středisko pro úspory energie s.r.o., 26 March 2025
    (32658848), 690,000 CZK, a type 1 audit to map consumption and recommend measures; Muzeum hlavního
    města Prahy and EnergySim s.r.o. (IČO 01512129), 3 April 2025 (32817856), 350,000 CZK, the
    museum''s buildings and vehicles; by metadata, Jaroměř (32717592), Náchod with PKV BUILD (31525636),
    Karlovarská krajská nemocnice (38908346) and FN Královské Vinohrady with PKV BUILD (35550977). The
    law requires these audits whether or not anyone ranks buildings, so they are not this job. (c)
    Local energy concepts for whole towns (Chomutov 30502220, Týn nad Vltavou 31143020, Praha-Čakovice
    31203516), metadata only. (d) Olomoucký kraj''s 68.93M CZK public-service contract with its
    regional energy centre for energy advice (35965461), title only, not opened. (e) The renovation awards on S4.'
  date: '2026-01-07'
created: '2026-08-13'
updated: '2026-09-19'
---

New EU building rules require minimum energy standards for buildings such as hospitals and town halls, and Czechia is late adopting them [S3].

- The rules also cover building automation, renovation passports and solar readiness [S3].
- An owner of many buildings then has to choose which to fix first.
- No Czech tool that ranks renovations across an owner's buildings has been found [S5].

The rules are the EU's recast Energy Performance of Buildings Directive, Directive 2024/1275 [S3]. It binds the member states, and each must write it into its own law [S3].

- The standards are minimum energy performance for non-residential buildings, with a path of step-by-step renovation for homes [S3].
- The automation duty covers large non-residential buildings, and new buildings must be zero-emission [S3].
- The directive also asks for one-stop shops that advise owners on renovation, and for infrastructure for sustainable transport [S3].
- The Czech law that adopts it will arrive compressed [S3].
- The owner's question is concrete: which buildings need automated controls, which need insulation, in what order, and at what cost.

Existing non-solutions: Consultants rank an owner's buildings by hand, and no Czech software was found that does the ranking [S5,S9].

Czech tools certify, monitor or plan one building at a time, and none found ranks renovations across an owner's buildings [S2,S5]:

- Energy specialists issue energy-performance certificates one building at a time, and one Czech energy consultancy does this at scale [S2].
- That consultancy and a building-software firm both sell platforms that collect consumption across many buildings and report on sustainability [S5]. Neither offers a renovation roadmap, a ranking of measures or cost modelling [S5].
- A renovation-pass calculator sells to homeowners and energy specialists, one building at a time [S5].
- The State Environmental Fund's renovation-pass application, part of its home-renovation subsidy, and the ufae.cz calculator also work one building at a time [S5].
- Foreign portfolio tools, such as IBM Envizi (a US product for building sustainability data), reach Czech owners through large property advisers, not as a Czech product [S5].
- No Czech product was found that sells the owner's plan: which building, which measure, in what order, as distinct from doing the work [S2,S5].
- Energy consultancies write that plan by hand, as a one-off study for each owner [S9].
- Some of them also sell software, which tracks energy use and costs [S9].

Next to this sits building automation, which the directive also requires [S3]. BUILDSYS integrates building-management systems [S6]. HGS (a Czech energy-software vendor) sells the FLOWBOX orchestration software [S6]. Novatec EAS (energy management for commercial buildings) works the same ground [S6]. Schneider Electric and Trane sell the international products here, and consultancies such as PwC write the sustainability reports the EU's green-finance rules ask for [S6]. No Czech vendor was found joining continuous tuning of a building to that reporting [S6].

Why now: Hospitals and towns are paying for renovations now, and the overdue Czech rules may land with little notice [S3,S4].

- Owners pick which building goes first; no Czech ranking tool has been found [S5].
- Three Plzeň-region hospitals awarded renovation contracts in a single week [S4].
- When Czech dates are set, owners must survey many buildings at short notice [S3].

The dates so far come from the EU, because the Czech ones are not set [S3]:

- By 29 May 2026 every EU country had to write the directive into its own law [S3].
- On 15 July 2026 the European Commission opened infringement proceedings, its formal case against a country that misses such a deadline, against all 27 member states, Czechia among them [S3].
- The Czech dates for the new duties are still unset, and the proceedings press the government to set them [S3]. An owner's own deadlines start only once the Czech law is published [S3].

Who pays: Public owners already pay consultants to rank their buildings by hand, and pay energy-service firms to renovate from the savings [S4,S9].

- A hospital paid a consultant to pick which of 28 buildings to renovate [S9].
- A public university paid a consultant to set priorities across its buildings [S9].
- About €58M of renovation contracts went to 11 public buyers in June–August 2026 [S4].
- Prague 6 awarded about €15.7M, and Klatovy hospital about €8.3M [S4].
- The hospitals in Stod and Domažlice awarded about €3.3M and €5.3M [S4].

The ranking is bought as its own study, before the renovation is put out to tender [S9].

- Kyjov's hospital signed in August 2026 for a consultant to visit each building, propose measures and estimate their cost and savings [S9].
- The consultant then says which buildings belong in an energy-savings contract, with a table of every building assessed [S9].
- Olomouc's university signed in December 2025 for a card on each building, with measures, cost and payback, and then a list of priorities [S9].
- The state development bank runs an advisory programme that prices the same analysis as its own line, for regions, towns and hospitals [S9].
- An EU fund for local energy projects, run by the European Investment Bank, pays up to 90% of that advice, and the owner pays the rest [S9].

This way of paying is energy-performance contracting: a firm renovates, and is repaid out of the energy the building then saves [S4].

- The contracts are 15 notices from 11 buyers, among them Hodonín, Kuřim and the state railway [S4].
- The three Plzeň-region hospitals, Klatovy, Stod and Domažlice, all awarded theirs in one week [S4].
- The choice of measures comes bundled with the work, through the energy-service firm [S4]. Choosing which buildings go in can be a separate study, bought first [S9]. That renovation spend is what a ranking product would sit in front of [S4].
- Commercial and institutional owners with many buildings face the same choice of which renovation to fund first. Public owners are the route in, through their tenders.

Solved elsewhere: Three funded companies in Germany and France sell owners software that ranks which building to renovate, and at what cost [S1].

A Berlin company raised €10M in July 2026 for software that screens landlords' and asset managers' buildings for energy-renovation needs, and has run 10,000 building analyses [S1]. A Munich company, selling since 2021, is Series A funded and names large property and insurance firms among its customers. A Paris company, selling since 2014, monitors buildings for hundreds of clients in many countries, and also sells investment planning and virtual renovations that simulate a measure's effect.

Germany is next door and France one market further, and each sells the owner-side layer that no Czech product was found selling [S5]. The same directive applies in both countries, and both also missed its deadline [S3].

On the building-automation side, Cologne's aedifion raised a €17M Series B in 2025 for a cloud layer that tunes heating, ventilation and cooling through a building's existing controls, across close to 500 buildings [S6]. It runs buildings rather than ranking them, so it is a neighbour to this product, not a template [S6].

## First moves

1. Build a ranking that reads an owner's energy data and certificates and says which building to renovate first, with which measure, at what cost. Answer four questions in order: which building, which measure, in what sequence, at what capital cost. A Berlin company raised money for exactly that product; see [Validated abroad](#validated-abroad). The Czech tools stop at consumption graphs and sustainability reports, as [Market gap](#competition) shows, so do not build more monitoring.
2. Contact the energy managers of the hospitals and towns that awarded energy-saving renovation contracts this summer, and offer to rank the rest of their buildings. They hold many buildings and already pay firms to renovate some of them; see [Willing to pay](#willing-to-pay). Public owners like them already pay consultants to rank buildings by hand, so price against that study. Start with the region whose three hospitals awarded theirs in the same week.
3. Open each conversation with the deadline the owner does not have yet: the Czech law for the EU building rules is overdue. It will arrive compressed, and the EU has already opened proceedings against Czechia; see [Why now](#why-now). When the law lands, its duties on automation, renovation passports and solar readiness will come with less notice than surveying many buildings takes. A ranking done now is ready when they do.
4. Watch the two Czech vendors closest to this product, because either could add a ranking to what it already sells. One is an energy consultancy that sells single-building assessments and a monitoring platform used by a large industrial-park landlord; the other sells software that gathers consumption across many buildings; see [Market gap](#competition). Both will read the Czech law the day you do, so ship the ranking before they add one.

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "triaging retrofit capex" now reads "deciding which renovations to fund first, and in what order". Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 2 → 3. All three comparables pass the maturity test — Predium selling since 2021 with Colliers, Baloise and Deutsche Investment named and a €13M Series A; Fuchs & Eule since 2021 with 10,000 building analyses behind a €10M round; Deepki since 2014 with 500+ clients and a €150M Series C [S1] — and they are established in two markets, Germany and France, with Germany CEE-adjacent. That is rung 3 as written; the v1 rung 2 was capped by a clause that has been struck from the ladder. `scores.gap` stays 1 and the reason is now explicit rather than implied: the three Czech products the [S5] sweep found were lifted into a structured `locals[]` ledger, and only one is established — PKV BUILD (IČO 28149785, ARES 2013) on the named-customer limb, Enmon implemented at CTP. DEKSOFT's ENERGOMETR and EnergySim's renovacnipas.cz publish no customer count, pair with no public buyer and carry no round or state listing, so both read early on receipts. An early local player does not close a space, so nothing here supports gap 0; and nothing here raises it either, because rung 2 needs a check that found no local player and this one found three. `score` 6 → 7. The state-side tools in the [S5] note — the SFŽP renovation-pass application and ufae.cz — were deliberately not lifted: they are subsidy-application artifacts, not players selling a product. The Proven-abroad paragraph now states each seller's trading age, because that is the fact carrying the score. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. PKV BUILD moves `early` → `established` and takes `competes: adjacent`. The `early` was never a reading of PKV: this file's own re-score entry, written earlier the same day, calls it the one established player on the named-customer limb with Enmon implemented at CTP, and then the ledger said early anyway, because under the one-field schema an established local forced gap to 0. With `competes` carrying eligibility, PKV records its true maturity and still moves nothing — what it sells is single-building energy-performance assessments plus consumption monitoring, not the portfolio retrofit planning this file is about. DEKSOFT is adjacent for the same reason and stays `early`, no limb being on file for it. EnergySim is the one `competes: direct` entry: a renovation-pass calculator is the same planning job, one building at a time rather than ranked across a portfolio, and it is early. `scores.gap` stays 1, CONTESTED, and now on the rung's literal words — locals sell this and all of them are early. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

2026-08-13 · money receipted — The EPC award wave was put on the ledger — 11 public buyers, ~€58M between June and August 2026 [S4] — carrying money to 1. The substance now sits in How big above rather than here.

2026-08-20 · evidence audit — Removed the EPC supplier-side sentence: the four named companies and associations (ENESA, ČEZ ESCO, MVV, APES) return no hits anywhere in the signal corpus and appear in no source note on this record, and the maturity verdict attached to them had nothing behind it either. The clause that survives, that the unoccupied position is the owner-side analytics product, is the record's own gap check and is now cited to [S2]. Also removed from "Who pays": the claim that banks pricing green mortgages and sustainability-linked loans are a second buyer, since no green-mortgage receipt exists in the corpus.

2026-08-24 · fact check — The window paragraph claimed owners have "no analytics layer, only per-building energy-certificate consultancies"; the record's own re-check found two Czech portfolio energy-management platforms (Enmon by PKV, ENERGOMETR by DEKSOFT) and flagged that the real distinction is monitoring versus retrofit planning, "narrower than the body currently implies" [S5]. The body now names both and claims only what was checked: no retrofit-planning product found, gap unchanged at 1. Enmon's own page was re-verified live on this date — 15-minute consumption collection and ESG reporting, no renovation planning [S5]. The unreceipted "ESG consultancies producing PDFs, and spreadsheets" flourish is gone.

THE LEDGER NOTES, IN PLAIN LANGUAGE. All 3 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

FIRST MOVES WRITTEN. `data/RECORD-TEMPLATE.md` reserves the section for records scoring >= 7 and this file scores 7; it was simply missing, which cost the reader the most actionable thing on the page. Four moves, each drawn from evidence already on the record: the eleven public energy-performance-contracting buyers as the first customers [S4], measure-ranking rather than monitoring as the first build [S1,S5], the missed 29 May 2026 transposition and the July infringement procedure as the opening fact [S3], and PKV Build and DEKSOFT named as the two vendors one product decision away [S5]. No new fact was introduced, no source note was edited and no [Sn] marker was moved.

2026-09-02 · plain-language pass — Five trade terms replaced with plain words at first use — BACS, EPBD, EPC, PENB, ESG — and PKV Build and CTP given appositives. The argument tightened from 447 to 384 words, keeping every [Sn] marker, figure and named company. First moves rewritten verbs-first, the register-voice opener on move 4 gone. A gist added to all five sources. No score, status, note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as three lines under the headline: a `brief:` on who is stuck and what forces it now, the `solution:` as a call to action starting "Build", and a new `good_for:` line. Previous title, verbatim: "Czech building owners must plan costly renovations, with no way to compare them". Previous solution, verbatim: "Portfolio software for building owners: score every building, rank the renovation measures by cost and payback, and turn the EU energy-performance rules into a dated capital plan." There was no previous brief or good_for. Checked against the sources before writing: "must plan costly renovations" left the headline, because the Czech implementing law is not written and no Czech duty or date yet binds an owner [S3]; the headline now states what is receipted, 11 public buyers awarding about €58M of energy-performance contracting between June and August 2026 [S4], beside the overdue rules [S3]. "With no way to compare them" is gone too: a Czech renovation-pass calculator already ranks measures one building at a time, and the checks found no portfolio ranking product, which is not proof none exists [S5]. The brief does not say the contracts skip triage, because the tender note records owners paying for triage and delivery together; it says only that they buy the work rather than a ranking across all of an owner's buildings [S4]. The headline says "hospitals, towns and other public owners" because one of the 11 buyers is the state railway. No urgency was invented: the Czech dates are unset [S3]. "As companies already do in Germany" rests on Fuchs & Eule [S1] and on Predium in the comparables ledger. No score, status, source, note, marker or body sentence changed. Simplified for the front page: Title before: "Czech hospitals, towns and other public owners awarded €58M of energy-saving renovations this summer. New EU building rules are overdue in Czech law." After: "Czech public bodies awarded €58M in energy-saving renovation contracts this summer". Brief before: "Public owners pay firms to renovate out of the energy saved, but those contracts buy the work, not a ranking of all their buildings [S4]. Czechia missed the May 2026 deadline to adopt the new EU building rules [S3]." After: "Hospitals and towns pay firms to renovate from the energy saved, but that buys the work, not a ranking of which building comes first [S4]. Czechia is late on new EU building rules [S3]." Solution before: "Build software that reads an owner's energy data and ranks which building to renovate first and at what cost, as companies already do in Germany." After: "Build software that reads an owner's energy data and ranks which building to renovate first, and at what cost." The headline's second sentence moved into the brief as "Czechia is late on new EU building rules" [S3], dropping the May 2026 date to keep one number, the €58M in the headline [S4]. "Awarded" stays: these are awarded contracts, not finished work. "As companies already do in Germany" was cut for length. No fact, number or claim was added; no score, status, source, note, marker in the body or body sentence changed. Same date, owner-approved final copy, written verbatim with only the [Sn] marker added (owner on the title before: "I don't understand" — a raw spend figure is not a pain; on the good-for line before: "too generic"). Title "Czech public bodies awarded €58M in energy-saving renovation contracts this summer" became "Czech towns and hospitals face EU building-upgrade rules, and Czechia is already late". Brief "Hospitals and towns pay firms to renovate from the energy saved, but that buys the work, not a ranking of which building comes first [S4]. Czechia is late on new EU building rules [S3]." became "The EU has started proceedings against Czechia for missing its deadline, so Czech rules are coming [S3]. Owners with many buildings will have to decide which to fix first, and at what cost." Marker checked against the ledger and re-read live on this date: [S3] is the Commission's 15 July 2026 notice, which names Directive (EU) 2024/1275, its 29 May 2026 transposition deadline, and letters of formal notice to all 27 member states, Czechia among them; its note records that the obligations phase in through a Czech implementing law, which is what "Czech rules are coming" says. The second sentence carries no marker on purpose: it is this record's framing of the owner's question (the body's first paragraph), and no source on file states it, so [S3] was not stretched over it. Solution "Build software that reads an owner's energy data and ranks which building to renovate first, and at what cost." became "Build software that reads an owner's energy data and ranks which building to renovate first and at what cost, as 3 companies already do in 2 other countries." The count is taken from comps[] only, and each comp was checked on its own site on this date for portfolio renovation ranking rather than monitoring alone: Predium (comps[1], geo DE) sells prioritisation across the whole building portfolio and calculates the costs and savings of investment scenarios (predium.de); Fuchs & Eule (comps[0], geo DE) screens portfolios and writes asset-specific renovation strategies with economic-viability analyses [S1] (fuchs-eule.de); Deepki (comps[2], geo FR) was the doubtful one, because its traction line on this record reads as monitoring, but its own site sells "CapEx Planning & Decarbonization" and virtual retrofits that simulate the impact of investments (deepki.com), so it counts. None excluded: 3 companies, based in 2 countries (DE, FR). Good for "Someone who'd like to work with hospitals and towns, through public tenders." became "Someone who understands building energy use and can sell to hospitals and towns through tenders." The generic form is kept for records anyone could enter; here `entry` gates the sale through public procurement and the product rests on reading energy data, so both are named. No score, status, source, note, body marker or body sentence changed. Same date, ledger: Deepki's `comps[]` traction line now also states the CapEx-planning and virtual-retrofit product read on https://www.deepki.com/ on 2026-09-16, so the solution's count of 3 companies in 2 countries can be read from the ledger itself; no other comp, score, source or marker changed. Same date, draft law: added `draft_law:` for the "Draft law" badge. The EU buildings directive is in force, which alone would not qualify, but it binds member states, not owners: the renovation, automation and passport duties reach Czech towns and hospitals only through the Czech law transposing it, which is overdue — the Commission opened infringement proceedings against Czechia on 15 July 2026 [S3] — and the brief already says the Czech rules are still coming. No other field changed.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the new EU standards and Czechia being late, with the directive's duties and the owner's question as detail [S3,S5]. Why now opens on owners paying for renovations now and the overdue rules, with its three pain items first and the 29 May and 15 July 2026 dates below them as plain bullets [S3,S4,S5]. Willing to pay answers that owners pay for the work but not for a ranking, and now holds the award figures that lived only in move 1, Klatovy about €8.3M and Prague 6 about €15.7M, plus Stod about €3.3M, Domažlice about €5.3M and three more named buyers from the same note [S4]. Competition describes the Czech sellers by what they sell and gained from its note the state renovation-pass application, the ufae.cz calculator and the foreign portfolio tools sold through advisers [S5]. The Berlin company's raise moved from Why now to Validated abroad, and aedifion from Competition to Validated abroad, since both are foreign [S1,S6]. Every comps[] and locals[] name left the body and the moves; each company is described by what it sells, and its funding, customers and counts stay in its ledger row. The moves lost every [Sn] marker and figure for links; move 1 now builds the ranking, and the old "Sell to the public owners" became move 2, a contact with their energy managers. `entry.why` was rewritten as "Easier: … Harder: …" with the same gates. Corrected against the sources: "obligated early under the directive's public-building rules [S3]" (Who pays and old move 1) is not in [S3]'s note, and the Commission notice at its URL, re-read on 2026-09-18, names no earlier duty for public buildings, so the claim is gone; the same page names minimum energy performance standards for non-residential buildings, renovation paths for homes, one-stop advice shops and sustainable-transport infrastructure, which now back The opportunity [S3]. "Czechia trailing by its transposition lag" behind Germany was cut: the notice went to all 27 member states, Germany and France included [S3]. "Nobody sells the owner's plan [S2,S5]" became "No Czech product was found that sells the owner's plan", since [S5]'s note says a search that finds nothing is not proof of absence. Flagged as inference: that an owner of many buildings has to choose which to fix first (unmarked, as in the brief); that owners' deadlines start only once the Czech law is published, and that owners must then survey many buildings at short notice [S3]; and that the renovation spend is what a ranking product would sit in front of [S4]. No `process:` block was added: no source on file says who ranks an owner's buildings today, only that owners buy the survey and the work together from an energy-service firm [S4]. No score, status, source, `note:`, `sources[]` order, title, brief, solution, good_for or draft_law changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Tagging pass first: every source on file was read for someone paying for this job, a ranking of which of an owner's buildings to renovate first and at what cost, or a consultant paid to draw it up by hand. None is. The energy-performance contracts [S4], about €58M from 11 public buyers, buy renovation delivered by an energy-service firm, with the choice of measures bundled into the work and never priced on its own, so they are adjacent spend and are not restated as a price; the record already said so in its own words. The Czech consultancy that sells single-building certificates and a monitoring platform has a named customer but no price on file [S5]. `scores.money` 1 → 0: no price receipt for this job, and public money nearby earns no point on its own. `scores.urgency` 2 → 1: the freshness point is retired, and the EU buildings directive [S3] is not yet Czech law, binds the state rather than the owner, and the record carries `draft_law:`, so it fails REAL and stops at rung 1. `score` 7 → 5, FAIR unchanged. The notes on S3 ("Deadline 1") and S4 ("money scored 1 (relevant tenders exist)") named retired rungs and gained a dated rescore line; their original text is left as written. Two `[Competition](#competition)` links now read `[Market gap](#competition)`. Why now and Willing to pay were re-read against the new numbers and left as written: Why now already says the Czech dates are unset and an owner's own deadlines start only once the Czech law is published [S3], and Willing to pay already says the contracts buy the work, not a ranking [S4]. The `price_search:` line stays: a consultancy's ranking of a region's or city's buildings is still the receipt to look for. No other score, status, source order, marker or headline field changed.

2026-09-19 · Willing to pay search, owner-approved — `scores.money` 0 → 2, `score` 5 → 7, band FAIR unchanged, `status` candidate unchanged. The rescore above found no price for this job, only energy-performance contracts that buy the renovation [S4] (worksheet call 9). This search looked for a public owner that paid, within 24 months, for the ranking itself: a building survey with priorities, an energy concept that ranks buildings, an energy-management study, or an audit across many buildings. Eleven full-text queries of the contracts register through the Hlídač státu API, each limited to contracts concluded from 19 September 2024, found them, and the contract texts were read [S9]. Two are restated as price receipts tagged money. Nemocnice Kyjov paid 349,000 CZK excluding VAT, under a contract of 14 August 2026 after its own small tender, for a consultant to go through 28 of its buildings, propose measures with their investment and savings, and recommend which belong in its planned energy-savings contract, with a summary table of every building [S7]. Univerzita Palackého v Olomouci paid 314,000 CZK excluding VAT, under an order accepted on 18 December 2025, for a card on each building with measures, cost and payback, followed by an energy concept that names the buildings with the most savings potential and proposes priorities [S8]. Both are signed contracts within 24 months of `updated`, so money is 2 on its own and the public-money lift is not needed. The university is not a town or a hospital; it counts because the buyer here is a public owner of many buildings (`entry.buyer: public`), and the hospital receipt alone carries rung 2. Both buy the ranking done by hand, which SCORING.md names as a paid receipt ("a consultant paid to do it by hand").

Found and not restated as a price: the state development bank, Národní rozvojová banka, runs an EPC advisory programme co-financed by the European Investment Bank's ELENA facility. Under a framework of consultants, it buys for regions, towns, hospitals and universities an input analysis of which buildings suit an energy-savings contract, priced as its own line: 759,825 CZK excluding VAT for the Plzeň region in January 2026, and at most 638,550 CZK in Jablonec nad Nisou's client contract of September 2025 [S9]. The bank pays the consultant and the owner pays it a fee of at least 10 %, so the owner's own price is not on file; the row is public money nearby, and S4's note gained a dated line saying the choice of buildings can be bought on its own.

Next door, read and not counted [S9]: energy-management systems under ISO 50001 (Ústí nad Orlicí, 36 buildings, NPO grant; Prague's implementation plan; Plzeň), whose "priorities" are the system's targets or the order of rolling it out, not which building to renovate; the statutory energy audit of a whole estate under § 9 of Act 406/2000 (Ivančice and the Prague City Museum read; Jaroměř, Náchod, Karlovy Vary's regional hospital and FN Královské Vinohrady by title), which the law requires whether or not anyone ranks buildings; local energy concepts for whole towns, by title; and the renovation awards already on file [S4]. No positive control is recorded because the same queries returned the positives.

Gap: unchanged at 1. The sellers found are consultancies doing the job by hand, which SCORING.md reads as adjacent ("a service firm rather than a product vendor"), and adjacent moves nothing. ENSYTRA (IČO 28582136, trading since 2009, named customers on its own offer) joins locals[] as adjacent and established; it also sells the EnergyBroker energy-management web app, whose page describes consumption and cost records, reports and energy purchasing, not a ranking of renovations. EnMass (IČO 13968050, registered 11 November 2021 in ARES) joins as adjacent and early: its site names no customers and one hospital contract is on file. PKV BUILD's evidence line said it "does not sell portfolio retrofit planning"; the bank pays it to write that analysis for the Plzeň region, so the line now says its software does not rank and that it ranks by hand as a consultant [S9]; still adjacent and established. EnergySim appears in the register only for statutory audits (the Prague City Museum, 350,000 CZK, April 2025), not for the renovation-pass calculator its row describes, so its row, its `competes: direct` and its `maturity: early` are unchanged. The other consultancies in the bank's framework, PORSENNA ENERGY, ENVIROS, SEVEn Energy, VŠB-TU Ostrava and LOYD GROUP, are named in the S9 note and not lifted into locals[]; each would be adjacent and move nothing. Flagged for a content pass.

Body: Willing to pay now opens on owners paying consultants to rank their buildings by hand as well as paying firms to renovate [S4,S9]. Its first two items are the hospital and university purchases, and the €58M item moved to third. A new paragraph says the ranking is bought as its own study before the renovation is tendered, with the bank's programme and its EU co-funding [S9]. "Owners pay for choosing the measures together with the work" now reads that the choice of measures comes bundled with the work, and that choosing which buildings go in can be a separate study bought first [S4,S9]. Market gap now opens on consultants ranking by hand with no Czech software found that does it [S5,S9]; the old answer sentence became the line under it, and two items on the consultancies were added. Move 2 said "nobody sells them the ranking that decides which building goes first", which the receipts make false; it now says public owners like them already pay consultants to rank buildings by hand, so price against that study; it does not claim that these particular owners did. Not changed: title, brief, solution, good_for, draft_law, `price_search`, `entry`, urgency, proof, demand and gap. The headline block stays true: the solution is software, and what owners pay for today is the ranking done by hand.
