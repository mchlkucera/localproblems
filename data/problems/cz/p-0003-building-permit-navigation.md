---
id: p-0003
region: cz
title: Czech developers and builders navigate one of the OECD's slowest building-permit processes
  through a still-dysfunctional state portal, with no tooling of their own
category: housing
geo: CZ-national
score: 6
scores:
  proof: 1
  money: 0
  urgency: 1
  demand: 2
  gap: 2
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Software over public permitting rules has no license gate, but CZ-specific stavební
    zákon workflow content plus developer pilots need a dev-and-permitting-expert team and
    a months-long sales cycle.'
comps:
- name: PermitPortal
  url: https://permitportalapp.com/
  geo: US
  since: 2024
  traction: 'YC F24; AI pre-construction OS for US developers; funding beyond YC undisclosed (YC, 2024)'
  signal: yc-permitportal
- name: PermitFlow
  url: https://www.permitflow.com/
  geo: US
  since: 2021
  traction: '$54M Series B led by Accel (company, 2025) after $31M Series A (TechCrunch, 2024); 80-person team (YC, 2026)'
- name: GreenLite
  url: https://greenlite.com/
  geo: US
  since: 2022
  traction: '$49.5M Series B led by Insight Partners (PRNewswire, 2025); ~100 Fortune 500 customers; permits in 21-45 vs 90-120 days'
- name: Autositu
  url: https://autositu.com/
  geo: US
  since: 2025
  traction: 'YC W26, 2-person team (YC, 2026); AI plan-review workspace claiming 50-70% fewer city comments; funding undisclosed'
  signal: yc-autositu
sources:
- type: arbitrage
  url: https://www.ycombinator.com/companies/permitportal
  note: 'yc-permitportal: PermitPortal (YC F24) — AI OS for pre-construction: entitlements,
    zoning intelligence, permit navigation; adjacent YC analogs Permitify (W25) and Verdant
    (S26) confirm the cluster. All US-market, so scored as one weak (non-adjacent) analog.'
  date: '2026-08-13'
  signal: yc-permitportal
- type: complaint
  url: https://www.ycombinator.com/companies/permitportal
  note: Signal documents the July 2024 DSŘ digitalization fiasco (portál stavebníka) and archiweb
    reporting that digitalization 'stabilized after a year, but still faces complications';
    CZ among slowest building-permit processes in OECD.
  date: '2026-08-13'
- type: gap-check
  url: https://www.ycombinator.com/companies/permitportal
  note: 'Absence check 2026-08-13: searches return only news about the broken state system
    and US tools (CivCheck); no CZ startup automating permit preparation or navigation.'
  date: '2026-08-13'
- type: arbitrage
  url: https://www.ycombinator.com/companies/autositu
  note: 'yc-autositu: Autositu (YC W26) — AI-native workspace for development plan reviews;
    a fourth YC company on the permitting/plan-review problem within two years. Still US-only,
    so arbitrage stays 1.'
  date: '2026-08-13'
  signal: yc-autositu
- type: complaint
  url: https://zpravy.ckait.cz/vydani/2024-01/delka-povolovani-staveb-v-cr-nikoliv-roky-ale-mesice-ukazal-pruzkum-inzenyrske-komory/
  note: 'ČKAIT survey published in Z+i 2024-01 (n≈1,100): typical Czech building-permit
    proceedings run 6–12 months, not years. This is the replacement figure the record''s
    CORRECTION block puts in place of the discontinued World Bank Doing Business framing;
    the url was cited in the body from 2026-08-13 but was not on this ledger. No evidence-layer
    signal covers this article (the one ČKAIT signal on file, chamber-ckait-dsr, is
    a different 2026-03 piece about the DSŘ portal).'
  date: '2024-01-31'
created: '2026-08-13'
updated: '2026-08-20'
---

Czech stavebníci — from housing developers to firms building industrial capacity — face one of the slowest building-permit processes in the OECD [S2]. The July 2024 launch of the digitalized permitting system (DSŘ / portál stavebníka) made things acutely worse [S2]: a year on, trade press (archiweb, cited in the yc-permitportal signal) describes the system as stabilized "but still facing complications." Both applicants and úřady lost throughput during the transition to the new stavební zákon procedures [S2].

Why now: the new building act changed procedures, the state portal remains unreliable [S2], and every month of permitting delay carries direct financing cost for developers. The pain is documented in national press rather than inferred.

Who pays: developers and larger stavebníci, for whom shaving months off entitlement and permit preparation is worth meaningful fees; architecture/engineering offices preparing dokumentace; potentially municipalities buying triage tooling, though the private side is the realistic first buyer.

Existing non-solutions: the state's own portál stavebníka (the source of much of the pain), law firms and inženýring service providers who navigate permits manually per project. The 2026-08-13 absence check found no Czech software automating permit preparation or navigation [S3].

Solved elsewhere: PermitPortal (YC F24), Permitify (YC W25) and Verdant (YC S26) show a funded US cluster around AI permit/zoning navigation [S1]. Arbitrage is scored conservatively at 1 because all analogs are US-based [S1,S4] and permitting is jurisdiction-specific; demand and gap carry this problem.

---
**CORRECTION (2026-08-13, post-run fact check):** The "OECD's slowest / 246 days / 157th in the world" framing traces to World Bank Doing Business 2020 — an index discontinued in 2021 after a data-manipulation scandal, and it measured the full administrative cycle, not permitting alone. Replace with: ČKAIT survey (Jan 2024, n≈1,100): typical proceedings **6–12 months**. Source: https://zpravy.ckait.cz/vydani/2024-01/delka-povolovani-staveb-v-cr-nikoliv-roky-ale-mesice-ukazal-pruzkum-inzenyrske-komory/
