---
id: p-0010
region: cz
title: Small Czech trucking firms still run dispatch, documents and invoicing
  on phones, e-mail and paper
category: mobility
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 0
  urgency: 3
  demand: 1
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Hemut runs the same stack with a 3-person team, but Czech phone-agent quality
    plus legacy-TMS and factoring integrations demand a real build, and per-truck
    SMB sales run a pilot cycle measured in months.'
comps:
- name: Hemut
  url: https://hemut.com/
  geo: US
  since: 2024
  traction: 'YC Spring 2025, 3-person team (Y Combinator); ~$1.8M raised at $30M
    valuation (Startup Intros); AI phone agents + document ingestion'
  signal: yc-hemut
- name: Cargofy
  url: https://cargofy.com/
  geo: UA
  since: 2017
  traction: '$11M Series A incl. $5M secondary, led by Movens (EU-Startups, Jun 2026);
    AI digital workers for shippers, carriers and 3PLs'
  signal: round-cargofy
- name: Nexcade
  url: https://nexcade.ai/
  geo: GB
  since: 2025
  traction: '$8.5M total incl. $6M seed led by Project A (nexcade.ai, Jul 2026);
    customers incl. XPO, Zencargo, Cardinal Global Logistics'
  signal: round-nexcade
- name: cargo.one
  url: https://www.cargo.one/
  geo: DE
  since: 2017
  traction: '€17.2M growth round (Vestbee, Mar 2026) atop $42M Series B (cargo.one,
    2020); 28,000+ users across 172 countries'
  signal: round-cargo-one
sources:
- type: arbitrage
  name: "Hemut"
  why: "AI back office for small trucking firms (YC 2025) — the closest template: a small team shipping phone agents, document ingestion and automated accounting."
  url: https://www.ycombinator.com/companies/hemut
  note: 'yc-hemut: Hemut (YC Spring 2025) — AI operating system for trucking companies: AI
    phone agents, document ingestion, load sourcing, automated accounting; Dayjob (S26) and
    Peer (S26) confirm the cluster. US-only, scored as one analog.'
  date: '2026-08-13'
  signal: yc-hemut
- type: gap-check
  name: "Market scan — Czech hauliers"
  why: "Roughly 40,000 haulier firms, most under ten trucks, still run dispatch, documents and invoicing on phones, e-mail and legacy TMS — while margins thin and drivers stay scarce."
  url: https://www.ycombinator.com/companies/hemut
  note: 'Absence check 2026-08-13: searches return only US AI-dispatch tools; CZ side shows
    legacy dispatch/TMS products, no AI-native ops player. Demand point: signal documents
    ~40k dopravci mostly <10 trucks running on phones/e-mail/legacy TMS, with driver shortage
    and thin margins; Timocom/Trans.eu cover load boards, not ops.'
  date: '2026-08-13'
- type: regulation
  name: "eFTI Regulation (EU) 2020/1056"
  why: "From 9 July 2027 authorities across the EU must accept electronic freight documents — the paper CMR workflow gets a dated expiry."
  url: https://transport.ec.europa.eu/news-events/news/towards-paperless-freight-transport-eu-takes-step-forward-efti-regulation-implementation-2025-01-09_en
  note: 'reg-efti-freight: eFTI Regulation (EU) 2020/1056 — from 9 Jul 2027 authorities in
    every Member State must accept electronic freight transport information via certified
    eFTI platforms; paper can no longer be demanded when a compliant digital record exists.
    Deadline <18 months: the paper-based back office acquires a regulatory expiry date. Commission
    estimates up to €1bn/yr sector savings.'
  date: '2027-07-09'
  signal: reg-efti-freight
- type: round
  name: "Cargofy"
  why: "Kyiv-based, ~$11M raised (Polish-led) for AI freight-operations workers — proof the model funds in Central Europe, not only the US."
  url: https://www.vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-june-2026
  note: 'round-cargofy: Cargofy (Kyiv) raised ~€9.5M Series A + secondary (Jun 2026, led by
    Movens — a Polish fund) for AI digital workers automating freight operations. First funded
    freight-ops-AI analog with CEE origin and CEE lead investor; the model transfers directly
    to CZ/PL freight firms. With Hemut (US) this makes funded analogs in multiple markets
    — proof upgraded 1→2, held below 3 because Cargofy/Nexcade sell into freight forwarders,
    an adjacent buyer to the small hauliers this record centers on.'
  date: '2026-06-30'
  signal: round-cargofy
  dims:
  - proof
- type: round
  name: "Nexcade"
  why: "London-based, $8.5M for AI freight-ops agents (customers include XPO) — the same thesis funded independently a month after Cargofy."
  url: https://www.vestbee.com/insights/articles/top-european-funding-rounds-closed-in-july-2026
  note: 'round-nexcade: Nexcade (London) raised ~€5.2M seed (Jul 2026, Project A + Inovia)
    for AI agents automating the freight-forwarder back office — the same thesis funded in
    Kyiv a month earlier, independently. Freight-ops AI is racing across markets while CZ/SK
    hauliers and forwarders stay unserved; eFTI (2027) is the shared regulatory tailwind.'
  date: '2026-07-31'
  signal: round-nexcade
  dims:
  - proof
- type: gap-check
  name: "Ringil"
  why: "The one Czech logistics platform in the space — but it sells to shippers (Škoda, Notino) and gives their carriers only free counterparty access, so the haulier's own back office stays open."
  url: https://ringil.com/en
  note: 'Incumbent re-check 2026-08-14 (cz-ringil flag): Ringil (CZ) — a Czech platform digitizing
    transport procurement and logistics workflows between shippers and carriers; the signal names
    Notino and Škoda (Škodovka) as clients and records no public funding round. The signal flags
    Ringil as OCCUPYING A REGISTER NICHE — "p-0010 claims no CZ player, Ringil is evidence to the
    contrary" — and marks it a DE-RANK CANDIDATE for this record. The signal carries no product
    breakdown, so nothing is asserted here about which side of the back office Ringil sells to.
    Gap requires re-judgment at the next MATCH run; see the correction on this record.'
  date: '2026-08-14'
  signal: cz-ringil
- type: subsidy
  name: "OP TAK — Technologie pro MAS II"
  why: "A 50% co-funding grant for software and IT at rural SMEs — a channel to halve the per-truck price. Applications 1 Sep 2026 to 1 Sep 2027."
  url: https://apiagentura.gov.cz/cs/podporovane-aktivity-optak/technologie-pro-mas-optak/technologie-pro-mas-clld-vyzva-ii/
  note: 'dotace-optak-technologie-mas-2: OP TAK Technologie pro MAS II — co-funds new machinery,
    software and IT for SMEs in MAS territories (outside Prague and cities over 25,000 inhabitants)
    at a 50% rate, grants up to 1.49M CZK on eligible costs of 250k–3M CZK; €22M (540M CZK)
    allocated, applications 2026-09-01 to 2027-09-01. Buyer-side co-funding channel for the
    per-truck software purchase the first moves propose, not a receipt for this record''s
    money score.'
  date: '2026-09-01'
  signal: dotace-optak-technologie-mas-2
- type: gap-check
  name: "Czech market search"
  why: "A Czech-language sweep found only legacy dispatch/TMS — TruckManager, LORI, Transfer Manager, AutoCRM — and no AI-native player selling to hauliers."
  url: https://ringil.com/funkce-pro-dopravce
  note: 'Gap re-check 2026-08-20 — the re-judgment the 2026-08-20 audit correction demanded.
    Question put to the evidence: does Ringil, or any other Czech player, sell the small
    haulier''s own back office — dispatcher calls, POD/CMR capture, invoicing, factoring
    paperwork — priced per truck or per dispatcher seat? RINGIL: NO, and the de-rank-candidate
    flag on `cz-ringil` is NOT UPHELD on the product surface. Ringil s.r.o. (Na hřebenech II
    1718/8, Praha 4, IČ 09194673) headlines itself "Systém pro kompletní řízení logistiky ve
    výrobních a prodejních firmách" and sells four modules — TMS, Avizace, Timesloty, Yard
    management — to manufacturers and retailers, i.e. to the SHIPPER. Its carrier page is
    explicit about the other side: "Zveme do Ringilu všechny dopravce našich zákazníků. Máte
    přístup zdarma" — carriers of Ringil''s own customers, free of charge, getting an RFQ inbox,
    one-click bidding, a record of the transports agreed with that shipper, and a driver app.
    That is a counterparty portal, not a haulier back office: no dispatch automation across the
    haulier''s own book, no POD/CMR ingestion into its invoicing, no invoicing or factoring, no
    phone agents. Structurally Ringil sits with the load boards this record already excludes.
    WIDER SWEEP: Czech search does return haulier-side software, all of it legacy dispatch/TMS
    of the kind the body already calls records-not-automation — TruckManager/TruckAgenda,
    Transfer Manager, AutoCRM, LORI (OLTIS Group, e-CMR) — plus EDITEL FreightLogs on eCMR and
    Dachser''s in-house platform. No Czech AI-native ops player selling to hauliers was found;
    the English-language search returns only US vendors (Transflo, Datatruck, BeyondTrucks), and
    the one AI logistics-document vendor marketing in Czech, Virtual Workforce, is Rotterdam-based
    with no named CZ customer. Positive control before trusting any of that: the same method,
    run at a company we know exists, surfaced Ringil''s own site and press on the first Czech
    query — the method finds CZ vendors when they are there. NOTHING MOVED: `scores.gap` stays 1
    and `score` stays 7. A thorough search that finds nothing is still only a search.'
  date: '2026-08-20'
  queries:
    - "česká platforma digitalizace přepravy poptávky dopravci odesílatelé"
    - "software pro dopravce dispečink fakturace CMR automatizace"
    - "Ringil platforma logistika přeprava Notino Škoda"
    - "platforma výběrová řízení na přepravu spotové poptávky dopravci česká firma"
    - "AI agent pro dopravní firmy dispečink hlasový asistent zpracování CMR POD faktur dopravce"
    - "umělá inteligence dispečink dopravní firmy česká aplikace pro dopravce automatizace administrativy 2026"
    - "Czech startup AI back office trucking carriers dispatch invoicing Czechia hauliers software"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: statistic
  name: "Mordor Intelligence — CZ road freight"
  why: "Sizes Czech road-freight transport at about $6.6 billion in 2026 — the pie the back-office admin cost sits inside."
  url: https://www.mordorintelligence.com/industry-reports/czech-republic-road-freight-transport-market
  note: 'market-size-cz-road-freight: Mordor Intelligence values the Czech road freight transport
    market at ~$6.59B in 2026, growing ~3%/yr. Context for the market floor, not a receipt
    for this record''s money score.'
  date: '2026-05-15'
- type: statistic
  name: "Datatruck — TMS pricing"
  why: "Small-fleet trucking software runs about $99–500 per month (Datatruck starts at $99 for 1–6 trucks) — what a per-firm product can realistically charge."
  url: https://www.datatruck.io/blog/how-much-does-tms-software-actually-cost
  note: 'tms-pricing-smb: Datatruck documents small-fleet TMS pricing at ~$99–500/mo (e.g. $99
    for 1–6 trucks). Grounds the bottom-up market math; not a receipt for this record''s money
    score.'
  date: '2026-05-15'
created: '2026-08-13'
updated: '2026-08-20'
---

Road freight is one of Czechia's biggest sectors — roughly 40,000 haulier firms, most with fewer than ten trucks [S2]. Their back office is manual: a dispatcher on the phone arranging loads, someone re-typing delivery notes and CMR paperwork, invoices and factoring chased by hand [S2]. Margins are thin and drivers scarce [S2], so the admin cost per truck is one these firms cannot hire their way out of. It is repetitive, document-heavy and in Czech — exactly the shape AI phone agents and document ingestion now handle [S1].

Existing non-solutions: a Czech-language search returns only legacy dispatch and TMS software that records the work rather than automating it — TruckManager/TruckAgenda, Transfer Manager, AutoCRM and OLTIS Group's LORI [S8]. Load boards (Timocom, Trans.eu) find freight but do not touch operations [S2]. Ringil is the one name worth clearing up: a Czech logistics platform, but it sells to shippers — Škoda and Notino among its clients — and gives their carriers only free counterparty access [S6], so it is not a haulier's own back office [S8]. No AI-native Czech operations product sells to the hauliers themselves [S8].

Why now: two things line up. AI phone agents and document ingestion have matured — a US cluster is already forming around exactly this buyer, led by Hemut (YC 2025) [S1]. And the regulatory trigger is dated: from 9 July 2027 the EU's eFTI Regulation makes electronic freight documents (eCMR and kin) a standard authorities must accept EU-wide [S3]. Every paper CMR workflow in those 40,000 firms gets an expiry date, and the certified e-document rail becomes the channel an AI back-office product rides in on [S3].

Who pays: the hauliers themselves — around 40,000 firms, most under ten trucks — priced per truck or per dispatcher seat, with a dated reason to buy from 9 July 2027 when their paper freight documents stop being enough [S3].

Czech road freight turns over about $6.6 billion a year [S9], and back-office admin is a real slice of every firm's cost. The software line is smaller but concrete: small-fleet trucking software runs roughly $100–500 per firm a month [S10], so 40,000 firms at about €150 a month is on the order of €70M a year if every one bought — call it a conservative floor of about €18M a year reachable if a quarter are software-ready [S10]. The point is not the exact figure: it is that 40,000 near-identical small buyers each spend real money here today, on worse tools.

Solved elsewhere: four funded companies already build this back office for small hauliers in other markets, and none operates in Czechia. Hemut (US, YC 2025) is the closest template — AI phone agents, document ingestion and automated accounting from a three-person team [S1]. Cargofy (Kyiv, about $11M) and Nexcade (London, $8.5M) each raised a month apart for AI freight-operations agents [S4,S5], proof the model funds in Central Europe too — though that pair aims one buyer over, at freight forwarders. cargo.one (Germany, €17M growth round, 28,000+ users) shows the category scales. Czech and Central European language handling for the phone agents is both the barrier for foreign entrants and the moat for a local one.

## First moves

1. Shadow five dispatchers at firms running fewer than ten trucks — reachable through the load boards they already use (Timocom, Trans.eu) — and log a week of phone calls, POD/CMR data entry and invoicing per truck, to price the admin overhead the record documents.
2. Build the document wedge first: Czech-language ingestion that turns a delivered load's POD/CMR into a ready-to-send invoice, and make the pipeline eFTI-ready — from 9 July 2027 authorities must accept electronic freight documents and every paper CMR workflow gets an expiry date [S3].
3. Prove the moat before betting on it: run an AI phone-agent prototype against recorded Czech dispatcher calls. Czech and Central European language handling is what keeps foreign entrants out.
4. Pitch two factoring providers that serve small hauliers as a distribution channel — cleaner documents speed their own work, so a per-truck bundle gives them a reason to sell it for you.
5. Let public money halve the price: firms in MAS territories (outside Prague and cities over 25,000 people) can co-fund software at 50%, grants up to 1.49M CZK, from [OP TAK Technologie pro MAS II](/sources/tenders#dotace-optak-technologie-mas-2), applications open 2026-09-01 to 2027-09-01 [S7].

## Revisions

2026-08-13 · regulation added — The eFTI Regulation was appended as this record's dated trigger [S3]; its substance now sits in The window above rather than here.

2026-08-20 · evidence audit and gap re-check — Two blocks recorded on this date, merged here; the second answers the first. The audit found that the S6 note asserted facts appearing nowhere in the signal it cites (cz-ringil, data/signals/funded/2026-08-14.jsonl): a founding year of 2020, "800+ companies on platform", Plzeňský Prazdroj as a client (the signal names Škoda; "Prazdroj" returns zero hits across all 6,181 signals), and a product-surface verification that Ringil "sells no haulier back-office" — the signal carries no product breakdown at all [S6]. The note then concluded "gap 1 stands", which reverses the signal's own finding: cz-ringil flags Ringil as occupying a register niche ("p-0010 claims no CZ player — Ringil is evidence to the contrary") and marks it a de-rank candidate for this record. The note, the existing-non-solutions sentence and the First moves competition line were rewritten to what the signal actually supports, and gap was deliberately left at 1 and score at 7 — moving them is a MATCH judgment under SPEC §4, not an audit one — with the gap score resting on a withdrawn note and flagged as requiring re-judgment. That re-judgment was then made in the same pass, against Ringil's own site rather than against a signal summary, and the de-rank candidacy is not upheld. Ringil s.r.o. (IČ 09194673) sells four modules — TMS, Avizace, Timesloty, Yard management — under the headline "Systém pro kompletní řízení logistiky ve výrobních a prodejních firmách", i.e. to the shipper; its carrier page opens "Zveme do Ringilu všechny dopravce našich zákazníků. Máte přístup zdarma" and offers those carriers an RFQ inbox, one-click bidding, a record of that shipper's transports and a driver app [S8]. Nothing there is the small haulier's own back office — no dispatch automation across its own book, no POD/CMR ingestion into invoicing, no invoicing or factoring — and nothing there is sold to the haulier at all: Ringil belongs with the load boards this record already excludes, on the other side of the same trade. The wider sweep found Czech haulier-side software, all of it the legacy dispatch/TMS the body already discounts, and no AI-native Czech ops player [S8]. Gap stays 1 and score stays 7. The check that was missing has now been run and recorded with its queries; it did not find an absence, it failed to find a player, and that pass had no authority to convert the second into the first by raising a score.
