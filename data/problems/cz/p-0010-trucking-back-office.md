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
created: '2026-08-13'
updated: '2026-08-20'
---

Road freight is one of the largest Czech sectors: roughly 40,000 dopravci, mostly firms with fewer than ten trucks [S1,S2]. Their back office — dispatcher phone calls, POD and document data entry, invoicing and factoring paperwork — runs on phones, e-mail and legacy TMS/dispečink software [S2]. With thin margins and a chronic driver shortage [S2], admin overhead per truck is a first-order cost these firms cannot hire their way out of.

Why now: AI phone agents and document ingestion have matured to the point where a US cluster is forming around exactly this buyer — Hemut (YC Spring 2025) as the AI back office for small/mid trucking firms, with Dayjob (S26, AI scheduling for short-haul) and Peer (S26, AI freight brokerage) replicating adjacent wedges within a year [S1].

The regulatory trigger is dated: the eFTI Regulation makes electronic freight documents (eCMR and kin) the accepted standard EU-wide from 9 July 2027 [S3]. Every paper CMR workflow in those 40,000 dopravci acquires an expiry date [S3], and the certified-platform ecosystem — eFTI platforms, trust services, TMS integrations — becomes the distribution rail an AI back-office product can ride into the segment.

Who pays: the hauliers themselves, priced per truck or per dispatcher seat; savings show up as dispatcher capacity and faster invoicing/cash collection. Factoring providers serving small hauliers are a plausible distribution channel since cleaner documents speed their own operations.

Existing non-solutions: legacy Czech dispatch/TMS products that record rather than automate — TruckManager/TruckAgenda, Transfer Manager, AutoCRM and OLTIS Group's LORI are what a Czech search returns [S8]; load boards (Timocom, Trans.eu) covering freight sourcing but not operations [S2]; and Ringil, which digitizes transport procurement between shippers and carriers, with Notino and Škoda among its named clients [S6] — but sells its four modules to the shipper and gives that shipper's carriers only free counterparty access, so it is not a haulier back office [S8]. No AI-native Czech ops player sells to hauliers [S2,S8]; how that was checked, contradicted and re-checked is in the revisions below.

Solved elsewhere: the US YC trucking-ops cluster above [S1], joined by two freight-ops rounds closed a month apart in Europe — Cargofy (Kyiv, ~€9.5M, Polish lead investor) [S4] and Nexcade (London, ~€5.2M) [S5], both building AI agents for freight operations. Proof is 2: funded in multiple markets including a CEE-origin player, but the European pair targets freight forwarders, an adjacent buyer to the small hauliers here. Czech and Central European language handling for AI phone agents is both the barrier for foreign entrants and the moat for a local one, and the forwarder wedge (spedice) and the haulier wedge land in the same document/dispatch workflows.

## First moves

1. Shadow five dispatchers at dopravci running fewer than ten trucks — recruited through the load boards they already use (Timocom, Trans.eu) — and log one week of phone calls, POD/CMR data entry and invoicing paperwork per truck to price the admin overhead the record documents.
2. Build the document wedge first: Czech-language ingestion that turns a delivered load's POD/CMR into a ready-to-send invoice — dispatcher capacity and faster invoicing/cash collection are where the record says the savings surface — and make the pipeline eFTI-ready, because from 2027-07-09 authorities must accept electronic freight documents and every paper CMR workflow acquires an expiry date [S3].
3. Verify the moat assumption before betting on it: run an AI phone-agent prototype against recorded Czech dispatcher calls — the record names Czech and Central European language handling as both the barrier for foreign entrants and the moat for a local player.
4. Pitch two factoring providers serving small hauliers as the distribution channel — the record notes cleaner documents speed their own operations, so a per-truck bundle gives them a reason to sell for you.
5. Let public money halve the buyer's price: hauliers based in MAS territories — outside Prague and cities over 25,000 inhabitants — can co-fund software and IT purchases at 50% (grants up to 1.49M CZK) from [OP TAK Technologie pro MAS II](/sources/tenders#dotace-optak-technologie-mas-2), €22M allocated, applications open 2026-09-01 to 2027-09-01 [S7].
6. Competition, per the record's own checks: **Hemut, Dayjob and Peer** (US cluster, same buyer, no CZ presence) [S1], **Cargofy and Nexcade** (funded, but selling to freight forwarders — an adjacent buyer) [S4,S5], **Ringil** (CZ, transport procurement between shippers and carriers — flagged by its own signal as a de-rank candidate [S6], flag not upheld on 2026-08-20 because Ringil bills the shipper and gives carriers free counterparty access [S8]), and legacy TMS/dispečink — TruckManager/TruckAgenda, Transfer Manager, AutoCRM, LORI [S8] — plus the Timocom/Trans.eu load boards (records and load sourcing, not ops automation) [S2].

## Revisions

2026-08-13 · regulation added — The eFTI Regulation was appended as this record's dated trigger [S3]; its substance now sits in The window above rather than here.

2026-08-20 · evidence audit and gap re-check — Two blocks recorded on this date, merged here; the second answers the first. The audit found that the S6 note asserted facts appearing nowhere in the signal it cites (cz-ringil, data/signals/funded/2026-08-14.jsonl): a founding year of 2020, "800+ companies on platform", Plzeňský Prazdroj as a client (the signal names Škoda; "Prazdroj" returns zero hits across all 6,181 signals), and a product-surface verification that Ringil "sells no haulier back-office" — the signal carries no product breakdown at all [S6]. The note then concluded "gap 1 stands", which reverses the signal's own finding: cz-ringil flags Ringil as occupying a register niche ("p-0010 claims no CZ player — Ringil is evidence to the contrary") and marks it a de-rank candidate for this record. The note, the existing-non-solutions sentence and the First moves competition line were rewritten to what the signal actually supports, and gap was deliberately left at 1 and score at 7 — moving them is a MATCH judgment under SPEC §4, not an audit one — with the gap score resting on a withdrawn note and flagged as requiring re-judgment. That re-judgment was then made in the same pass, against Ringil's own site rather than against a signal summary, and the de-rank candidacy is not upheld. Ringil s.r.o. (IČ 09194673) sells four modules — TMS, Avizace, Timesloty, Yard management — under the headline "Systém pro kompletní řízení logistiky ve výrobních a prodejních firmách", i.e. to the shipper; its carrier page opens "Zveme do Ringilu všechny dopravce našich zákazníků. Máte přístup zdarma" and offers those carriers an RFQ inbox, one-click bidding, a record of that shipper's transports and a driver app [S8]. Nothing there is the small haulier's own back office — no dispatch automation across its own book, no POD/CMR ingestion into invoicing, no invoicing or factoring — and nothing there is sold to the haulier at all: Ringil belongs with the load boards this record already excludes, on the other side of the same trade. The wider sweep found Czech haulier-side software, all of it the legacy dispatch/TMS the body already discounts, and no AI-native Czech ops player [S8]. Gap stays 1 and score stays 7. The check that was missing has now been run and recorded with its queries; it did not find an absence, it failed to find a player, and that pass had no authority to convert the second into the first by raising a score.
