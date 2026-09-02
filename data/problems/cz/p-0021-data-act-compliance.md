---
id: p-0021
region: cz
title: Czech device manufacturers must ship 'access by design' data APIs from Sep 2026 and
  every SaaS must abolish switching charges by Jan 2027 under the EU Data Act
category: b2b
geo: CZ-national
score: 3
scores:
  proof: 0
  money: 0
  urgency: 3
  demand: 0
  gap: 0
status: rejected
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'No certification gate and no productized comp found — legal-technical gap analyses
    and data-access API work for mid-market OEMs is consulting-led engineering a dev-plus-lawyer
    team can sell against the 12 Sep 2026 access-by-design wave.'
comps: []
sources:
- type: regulation
  name: "EU Data Act (Regulation 2023/2854)"
  gist: "the law and its two deadlines"
  why: "The Commission's own page for the Data Act: applicable since 12 September 2025, access by design for newly placed connected products from 12 September 2026, cloud switching charges abolished from 12 January 2027."
  url: https://digital-strategy.ec.europa.eu/en/policies/data-act
  note: 'reg-data-act-waves: EU Data Act (2023/2854), applicable since 12 Sep 2025; 12 Sep
    2026 — access-by-design for connected products newly placed on the EU market; 12 Jan 2027
    — cloud/SaaS switching charges fully abolished. Both waves <18 months (the first, one
    month from record creation).'
  date: '2026-09-12'
  signal: reg-data-act-waves
- type: news
  name: "Latham & Watkins — Data Act briefing"
  gist: "the law-firm scope briefing"
  why: "A law firm's client briefing on who the duties bind: device makers must expose product data to users and third parties through an API, cloud providers must drop switching charges and support exit."
  url: https://www.lw.com/en/insights/eu-data-act-what-businesses-need-to-know
  note: 'Law-firm compliance guidance confirming scope: IoT/device manufacturers must expose
    product data to users and third parties via APIs; cloud providers must remove switching
    charges and support exit.'
  date: '2026-08-13'
created: '2026-08-13'
updated: '2026-09-02'
---

The EU Data Act (Regulation 2023/2854) has applied since 12 September 2025; the hard engineering deadlines are still ahead [S1]. From 12 September 2026, connected products newly placed on the EU market must let users reach the data they generate, directly or through an API [S1,S2]. From 12 January 2027, cloud and SaaS providers must abolish switching charges and help customers leave [S1,S2]. The first wave hits Czech makers of connected equipment: industrial machinery, appliances, vehicles [S1].

Why now: access by design is firmware and backend work, not paperwork, and it has to ship in products placed on the market from 12 September 2026 [S1]. January 2027 then forces every Czech SaaS vendor to build a working export and exit path [S2].

Who pays: device makers buying data-access layers, consent handling and contract rewrites, and SaaS vendors buying export and exit tooling [S1]. Both also buy the legal-and-engineering review that says what to build. Czech industrial manufacturers carry it on top of the [Machinery Regulation cutover of 20 January 2027](/problem/cz/p-0014), on the same thin engineering teams.

Existing non-solutions: law-firm advisories and one-off consulting [S2]. No product sold to mid-sized Czech equipment makers is known, and no market search has been run to find one.

Next moves: search the Czech market for data-access tooling sold as a product. Ask the industry confederation Svaz průmyslu a dopravy and the car-industry association AutoSAP what their members have done; a readiness statement from either is the first demand receipt.

## Revisions

2026-08-20 · evidence audit — Three unbacked claims removed. That Czech machinery, appliance and vehicle-component manufacturers "have never built user-facing data access": the who-list is real and is carried by the reg-data-act signal, so it stays and is now cited to [S1], but the absence claim about what those firms have built is not, and is gone. That the switching-charge wave hits export paths "most have deferred indefinitely" — an empirical claim about Czech SaaS vendors with no receipt anywhere. And "some enterprise IoT platforms advertise Data Act modules" — the Data Act appears in exactly one signal, which names no vendor and makes no such claim.

2026-08-24 · rejected — Owner review. One regulation signal and one law-firm advisory carry the whole record; on every other dimension there is nothing Czech — no tender, no demand receipt, no money, gap never checked, no comparable on the ledger. The two compliance dates are real and correctly stated [S1,S2], and the title's own closing claim, that most affected firms "haven't started", was never receipted at all. A record whose entire content is an EU deadline plus scope framing does not meet the register's bar. Rejected, not deleted — the trail stays.

2026-09-02 · plain-language pass — OEM, IoT and SP ČR replaced at first use: mid-sized Czech equipment makers, connected equipment, Svaz průmyslu a dopravy. AutoSAP named as the car-industry association. Argument 236 → 245 words, markers 7 → 8: Regulation 2023/2854, 12 September 2025 and the 20 January 2027 machinery cutover added to the body. Next moves rewritten verbs-first, the register self-reference gone. Name, gist and why added to both sources. No score, status, note or marker touched.
