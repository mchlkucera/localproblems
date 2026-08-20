---
id: p-0021
region: cz
title: Czech device manufacturers must ship 'access by design' data APIs from Sep 2026 and
  every SaaS must abolish switching charges by Jan 2027 under the EU Data Act — two waves
  most affected firms haven't started
category: b2b
geo: CZ-national
score: 3
scores:
  proof: 0
  money: 0
  urgency: 3
  demand: 0
  gap: 0
status: candidate
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
  url: https://digital-strategy.ec.europa.eu/en/policies/data-act
  note: 'reg-data-act-waves: EU Data Act (2023/2854), applicable since 12 Sep 2025; 12 Sep
    2026 — access-by-design for connected products newly placed on the EU market; 12 Jan 2027
    — cloud/SaaS switching charges fully abolished. Both waves <18 months (the first, one
    month from record creation).'
  date: '2026-09-12'
  signal: reg-data-act-waves
- type: news
  url: https://www.lw.com/en/insights/eu-data-act-what-businesses-need-to-know
  note: 'Law-firm compliance guidance confirming scope: IoT/device manufacturers must expose
    product data to users and third parties via APIs; cloud providers must remove switching
    charges and support exit.'
  date: '2026-08-13'
created: '2026-08-13'
updated: '2026-08-20'
---

The EU Data Act has been applicable since September 2025, but its two hardest engineering obligations land inside the next five months: from 12 September 2026, connected products newly placed on the EU market must be designed so users can access the data they generate — directly or via APIs — and from 12 January 2027, cloud and SaaS providers must abolish switching charges entirely and support customer exit [S1,S2]. Czechia's industrial base makes the first wave heavy: the reg-data-act signal names CZ IoT and device manufacturers — industrial equipment, appliances, vehicles — as the who [S1].

Why now: "access by design" is a product-engineering requirement, not a policy — it must ship in firmware and cloud backends of products entering the market in weeks [S1]. The switching-charge wave forces every Czech SaaS to build export and portability paths [S2].

Who pays: device manufacturers buying data-API layers, consent management and contract remediation; SaaS providers buying exit/portability tooling [S1]; both segments buying legal-technical gap analyses. The overlap with Machinery Regulation work (p-0014) means industrial manufacturers face compounding product-compliance stacks with the same thin engineering teams.

Existing non-solutions: law-firm advisories and one-off consulting [S2]; nothing verified for the Czech mid-market OEM segment (gap unchecked, scored 0).

Next moves: demand receipts from Czech industry associations (SP ČR, AutoSAP) on Data Act readiness, and a gap check on productized data-access tooling; either would lift the score toward newsletter range.

---
**CORRECTION (2026-08-20, evidence audit):** Three unbacked claims removed. That Czech machinery, appliance and vehicle-component manufacturers "have never built user-facing data access" — the **who-list** is real and is carried by the reg-data-act signal, so it stays and is now cited to [S1]; the absence claim about what those firms have built is not, and is gone. That the switching-charge wave hits export paths "most have deferred indefinitely" — an empirical claim about Czech SaaS vendors with no receipt anywhere. And "some enterprise IoT platforms advertise Data Act modules" — the Data Act appears in exactly one signal, which names no vendor and makes no such claim.
