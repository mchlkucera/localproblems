---
id: p-0026
region: cz
title: Hundreds of small Czech water utilities are buying smart metering one tender at a time
  — each re-solving telemetry, data and dispatch with no shared platform
category: environment
geo: CZ-national
score: 3
scores:
  proof: 0
  money: 2
  urgency: 1
  demand: 0
  gap: 0
status: watching
sources:
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/430180-2026
  note: 'ted-430180-2026: Svazek vodovodů a kanalizací Ivančice — OPEN competition ~€1.2M
    (~29M CZK) for smart-metering installation on the water network (Jun–Jul 2026). Open tender
    ≥5M CZK: money 2.'
  date: '2026-06-24'
  signal: ted-430180-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/372049-2026
  note: 'ted-372049-2026: VaK Kroměříž awarded ~€1.3M to build water-network smart metering
    (Jun 2026); VaK Bruntál tendered a water data dispatch (~€0.5M, Jul 2026) — three small-utility
    metering/telemetry buys in ten weeks. Signed Kroměříž contract in registr smluv: ~21.4M
    CZK (smlouvy.gov.cz/smlouva/38292247).'
  date: '2026-06-01'
  signal: ted-372049-2026
- type: contract
  url: https://smlouvy.gov.cz/smlouva/39041762
  note: 'hlidac-39041762: VaK Židlochovicko signed two contracts on 30 Jul 2026 — meter/reader
    supply (~4.8M CZK) plus system operation & support (~3.6M CZK) — a FOURTH distinct small-utility
    buyer, procuring exactly the supply+managed-operation split the record predicts; Pražská
    vodohospodářská společnost signed ~12M CZK in June.'
  date: '2026-07-30'
  signal: hlidac-39041762
- type: contract
  url: https://smlouvy.gov.cz/smlouva/38219601
  note: 'hlidac-38219601: VaK Břeclav signed amendment No. 1 to a framework contract with
    SUEZ Water CZ for remote-readout devices and support (Jun 2026) — a FIFTH distinct utility
    with a live smart-metering relationship, running on a supplier framework.'
  date: '2026-06-02'
  signal: hlidac-38219601
- type: contract
  url: https://smlouvy.gov.cz/smlouva/38618416
  note: 'hlidac-38618416: VaK Pardubice amended its Smart Metering licence agreement with
    Popron Systems (Jun 2026) — sixth distinct utility; město Most added a Smart Metering
    supplementary service from its incumbent operator Severočeské vodovody a kanalizace in
    August (hlidac-39039418) — seventh. The pattern the record predicted is now receipted
    across seven buyers: supply, licence, and managed-operation contracts, each utility alone.'
  date: '2026-06-30'
  signal: hlidac-38618416
- type: gap-check
  url: https://www.softlink.cz/reseni/cem-smart/
  note: 'Gap check 2026-08-13: the managed-service position is NOT empty — Softlink (CZ) sells
    the CEM Smart metering-data platform with water-utility references, VODÁRENSKÁ AKCIOVÁ
    SPOLEČNOST operates metering as a service (it runs Židlochovicko''s system per hlidac-39041590),
    Popron Systems sells SMG Water, and SUEZ/Techem serve the utility and housing tiers. Local
    players named: gap stays 0 and status moves to watching per the de-rank rule.'
  date: '2026-08-13'
created: '2026-08-13'
updated: '2026-08-13'
---

Czech water supply is run by hundreds of VaK companies and municipal svazky, most of them small, and they are digitizing metering the only way they know: one infrastructure tender at a time. In a single ten-week TED window, Kroměříž awarded ~€1.3M for network smart metering, the Ivančice association opened a ~€1.2M competition for the same, and Bruntál tendered a water data dispatch — three buyers independently procuring hardware, telemetry, data platform and integration as bespoke projects.

Why now: water-loss pressure (droughts, price regulation via ERSO oversight) pushes utilities toward continuous metering, and EU funding streams (OPŽP) co-finance the projects — so the tenders keep coming. But a svazek with three employees cannot run a data platform; each project embeds years of operational dependence on whichever integrator won.

Who pays: the utilities themselves via receipted public procurement — today an integrator/dev-shop market in which each small utility contracts supply, licences and operation separately (seven distinct buyers receipted by August 2026).

Existing non-solutions: hardware vendors' proprietary head-end systems, one-off SCADA/dispatch integrations, and the large VaKs' in-house solutions (Veolia-operated utilities) that don't serve the small-utility tail.

Updated 2026-08-13 — de-rank applied: the gap check found the managed-service position occupied. Softlink sells its CEM Smart metering-data platform to Czech water utilities, VODÁRENSKÁ AKCIOVÁ SPOLEČNOST operates remote metering as a service for small utilities (it runs Židlochovicko's system), Popron Systems licenses SMG Water, and SUEZ and Techem hold framework and housing-tier positions. The original framing — "no shared platform, nobody operates a neutral managed service" — does not survive the check: the buying is fragmented, but the supply side is present and winning these contracts. Gap stays 0 with incumbents named; status moves to watching. What would re-rank this: evidence the incumbents fail the smallest svazky on price or capability, or a below-threshold tender count showing the long tail remains unserved.
