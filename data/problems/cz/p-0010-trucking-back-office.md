---
id: p-0010
region: cz
title: Tens of thousands of small Czech road hauliers run dispatch, documents and invoicing
  on phones, e-mail and legacy TMS while margins thin and drivers stay scarce
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
  url: https://www.ycombinator.com/companies/hemut
  note: 'yc-hemut: Hemut (YC Spring 2025) — AI operating system for trucking companies: AI
    phone agents, document ingestion, load sourcing, automated accounting; Dayjob (S26) and
    Peer (S26) confirm the cluster. US-only, scored as one analog.'
  date: '2026-08-13'
  signal: yc-hemut
- type: gap-check
  url: https://www.ycombinator.com/companies/hemut
  note: 'Absence check 2026-08-13: searches return only US AI-dispatch tools; CZ side shows
    legacy dispatch/TMS products, no AI-native ops player. Demand point: signal documents
    ~40k dopravci mostly <10 trucks running on phones/e-mail/legacy TMS, with driver shortage
    and thin margins; Timocom/Trans.eu cover load boards, not ops.'
  date: '2026-08-13'
- type: regulation
  url: https://transport.ec.europa.eu/news-events/news/towards-paperless-freight-transport-eu-takes-step-forward-efti-regulation-implementation-2025-01-09_en
  note: 'reg-efti-freight: eFTI Regulation (EU) 2020/1056 — from 9 Jul 2027 authorities in
    every Member State must accept electronic freight transport information via certified
    eFTI platforms; paper can no longer be demanded when a compliant digital record exists.
    Deadline <18 months: the paper-based back office acquires a regulatory expiry date. Commission
    estimates up to €1bn/yr sector savings.'
  date: '2027-07-09'
  signal: reg-efti-freight
- type: round
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
  url: https://ringil.com/en
  note: 'Incumbent re-check 2026-08-14 (cz-ringil flag): Ringil (CZ, founded 2020; 800+ companies
    on platform, clients incl. Notino and Plzeňský Prazdroj) verified as a shipper-side logistics
    platform — transport procurement (poptávky broadcast to carriers), timeslot/yard management,
    inbound tracking for manufacturers and retailers. Hauliers use it free as bidding counterparties;
    it sells no haulier back-office (own-fleet dispatch, POD/CMR document automation, invoicing).
    Adjacent player on the buyer side of the same freight market — gap 1 stands for haulier
    ops tooling.'
  date: '2026-08-14'
  signal: cz-ringil
- type: subsidy
  url: https://apiagentura.gov.cz/cs/podporovane-aktivity-optak/technologie-pro-mas-optak/technologie-pro-mas-clld-vyzva-ii/
  note: 'dotace-optak-technologie-mas-2: OP TAK Technologie pro MAS II — co-funds new machinery,
    software and IT for SMEs in MAS territories (outside Prague and cities over 25,000 inhabitants)
    at a 50% rate, grants up to 1.49M CZK on eligible costs of 250k–3M CZK; €22M (540M CZK)
    allocated, applications 2026-09-01 to 2027-09-01. Buyer-side co-funding channel for the
    per-truck software purchase the first moves propose, not a receipt for this record''s
    money score.'
  date: '2026-09-01'
  signal: dotace-optak-technologie-mas-2
created: '2026-08-13'
updated: '2026-08-20'
---

Road freight is one of the largest Czech sectors: roughly 40,000 dopravci, mostly firms with fewer than ten trucks [S1,S2]. Their back office — dispatcher phone calls, POD and document data entry, invoicing and factoring paperwork — runs on phones, e-mail and legacy TMS/dispečink software [S2]. With thin margins and a chronic driver shortage [S2], admin overhead per truck is a first-order cost these firms cannot hire their way out of.

Why now: AI phone agents and document ingestion have matured to the point where a US cluster is forming around exactly this buyer — Hemut (YC Spring 2025) as the AI back office for small/mid trucking firms, with Dayjob (S26, AI scheduling for short-haul) and Peer (S26, AI freight brokerage) replicating adjacent wedges within a year [S1].

Who pays: the hauliers themselves, priced per truck or per dispatcher seat; savings show up as dispatcher capacity and faster invoicing/cash collection. Factoring providers serving small hauliers are a plausible distribution channel since cleaner documents speed their own operations.

Existing non-solutions: legacy Czech dispatch/TMS products (records, not automation), load boards (Timocom, Trans.eu) that cover freight sourcing but not operations [S2], and Ringil — the largest Czech logistics platform, verified 2026-08-14 as shipper-side transport procurement (Notino, Plzeňský Prazdroj digitize their inbound logistics on it) [S6]; hauliers appear on it free as bidding counterparties, their own back office untouched [S6]. The 2026-08-13 absence check found no AI-native CZ ops player selling to hauliers [S2], and the Ringil re-check did not change that [S6].

Solved elsewhere: the US YC trucking-ops cluster above [S1], now joined by two independent freight-ops rounds closed a month apart in Europe — Cargofy (Kyiv, ~€9.5M, Polish lead investor) [S4] and Nexcade (London, ~€5.2M) [S5], both building AI agents for freight operations. Proof upgraded to 2: the model is funded in multiple markets including a CEE-origin player, though the European pair targets freight forwarders — an adjacent buyer to the small hauliers here, which keeps proof below 3. Czech and Central European language handling for AI phone agents remains both the barrier for foreign entrants and the moat for a local one, and the forwarder wedge (spedice) and the haulier wedge land in the same document/dispatch workflows.

Regulatory trigger added 2026-08-13: the eFTI Regulation makes electronic freight documents (eCMR and kin) the accepted standard EU-wide from 9 July 2027 — eleven months out [S3]. Every paper CMR workflow in those 40,000 dopravci acquires an expiry date [S3], and the certified-platform ecosystem (eFTI platforms, trust services, TMS integrations) becomes the distribution rail an AI back-office product can ride into the segment.

## First moves

1. Shadow five dispatchers at dopravci running fewer than ten trucks — recruited through the load boards they already use (Timocom, Trans.eu) — and log one week of phone calls, POD/CMR data entry and invoicing paperwork per truck to price the admin overhead the record documents.
2. Build the document wedge first: Czech-language ingestion that turns a delivered load's POD/CMR into a ready-to-send invoice — dispatcher capacity and faster invoicing/cash collection are where the record says the savings surface — and make the pipeline eFTI-ready, because from 2027-07-09 authorities must accept electronic freight documents and every paper CMR workflow acquires an expiry date [S3].
3. Verify the moat assumption before betting on it: run an AI phone-agent prototype against recorded Czech dispatcher calls — the record names Czech and Central European language handling as both the barrier for foreign entrants and the moat for a local player.
4. Pitch two factoring providers serving small hauliers as the distribution channel — the record notes cleaner documents speed their own operations, so a per-truck bundle gives them a reason to sell for you.
5. Let public money halve the buyer's price: hauliers based in MAS territories — outside Prague and cities over 25,000 inhabitants — can co-fund software and IT purchases at 50% (grants up to 1.49M CZK) from [OP TAK Technologie pro MAS II](/sources/tenders#dotace-optak-technologie-mas-2), €22M allocated, applications open 2026-09-01 to 2027-09-01 [S7].
6. Competition, per the record's own checks: **Hemut, Dayjob and Peer** (US cluster, same buyer, no CZ presence) [S1], **Cargofy and Nexcade** (funded, but selling to freight forwarders — an adjacent buyer) [S4,S5], **Ringil** (CZ, shipper-side transport procurement — adjacent) [S6], and legacy TMS/dispečink plus the Timocom/Trans.eu load boards (records and load sourcing, not ops automation) [S2].
