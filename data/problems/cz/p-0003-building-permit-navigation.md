---
id: p-0003
region: cz
title: Czech developers and builders navigate one of the OECD's slowest building-permit processes
  through a still-dysfunctional state portal
category: housing
geo: CZ-national
score: 4
scores:
  proof: 1
  money: 0
  urgency: 1
  demand: 2
  gap: 0
status: watching
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
- type: news
  url: https://www.worldbank.org/en/news/statement/2021/09/16/world-bank-group-to-discontinue-doing-business-report
  note: 'World Bank Group statement, 16 Sep 2021 — the Doing Business report is DISCONTINUED
    following the investigation into data irregularities in the Doing Business 2018 and 2020
    editions. Traced by the 2026-08-20 evidence audit as the primary source for the discontinuation
    half of this record''s CORRECTION block. The specific "246 days / 157th" figures the correction
    attributes to Doing Business 2020 were NOT traced to a primary source and stay flagged as
    untraced in the block. No evidence-layer signal covers this statement (Doing Business returns
    zero hits corpus-wide); correction receipt only, backs no score dimension.'
  date: '2021-09-16'
  dims: []
- type: gap-check
  url: https://pruvodka.cz/o-nas
  note: 'Gap re-check 2026-08-20: looked for a Czech product automating permit preparation
    or navigation for stavebníci, developers or projektanti — the absence this record has
    claimed since 2026-08-13. FOUND, and the claim does not survive it. Průvodka (pruvodka.cz,
    live and priced) sells exactly that: the buyer uploads the dokumentace, AI checks it and
    recommends which dotčené orgány and správci sítí (ČEZ, GasNet, vodárny, CETIN) to approach,
    the requests go out through datová schránka, and the service tracks each authority''s
    30/60/90-day lhůta and generates the doklad o fikci souhlasu when one lapses; 12,900 CZK
    per project one-off or 29,900 CZK/month (Studio, up to 5 new projects), Stripe checkout,
    14-day money-back. Its own about page states it serves "projektantům i stavebníkům" and is
    "postaveno pro české stavební řízení". A second CZ player, Efektivia (efektivia.eu), sells
    AI document triage into municipal offices — the authority side of the same counter, live at
    MČ Brno-střed and MěÚ Neratovice. De-ranked under SPEC §4: gap 2 -> 0, score 6 -> 4, status
    -> watching. Method note: our own funded ledger holds no CZ permitting entrant, and would
    not have — both incumbents are unfunded, so a capital-shaped ledger cannot see them.'
  date: '2026-08-20'
  queries:
    - "software automatizace stavebního povolení příprava dokumentace stavební řízení"
    - "startup AI povolování staveb portál stavebníka pomoc developerům software"
    - "\"stavební povolení\" AI asistent aplikace vyřízení online startup česká firma"
    - "Efektivia AI stavební úřad žádosti o stavební povolení kontrola úplnosti podkladů"
    - "Průvodka.cz vyjádření dotčených orgánů online služba stavebníci firma"
    - "Czech startup permitting software construction permits automation Czechia proptech"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
created: '2026-08-13'
updated: '2026-08-20'
---

Czech stavebníci — from housing developers to firms building industrial capacity — face one of the slowest building-permit processes in the OECD [S2]. The July 2024 launch of the digitalized permitting system (DSŘ / portál stavebníka) made things acutely worse [S2]: a year on, trade press (archiweb, cited in the yc-permitportal signal) describes the system as stabilized "but still facing complications." Both applicants and úřady lost throughput during the transition to the new stavební zákon procedures [S2].

Why now: the new building act changed procedures, the state portal remains unreliable [S2], and every month of permitting delay carries direct financing cost for developers. The pain is documented in national press rather than inferred.

Who pays: developers and larger stavebníci, for whom shaving months off entitlement and permit preparation is worth meaningful fees; architecture/engineering offices preparing dokumentace; potentially municipalities buying triage tooling, though the private side is the realistic first buyer.

Existing non-solutions: the state's own portál stavebníka (the source of much of the pain), law firms and inženýring service providers who navigate permits manually per project. The 2026-08-13 absence check found no Czech software automating permit preparation or navigation [S3] — a finding the 2026-08-20 gap re-check overturns. **Průvodka** sells that product to projektanti and stavebníci: upload the dokumentace, AI checks it and recommends which dotčené orgány and správci sítí (ČEZ, GasNet, vodárny, CETIN) to approach, the žádosti go out by datová schránka, and the service tracks each 30/60/90-day lhůta and issues the doklad o fikci souhlasu when one lapses — 12,900 CZK per project or 29,900 CZK a month on the Studio plan [S7]. On the authority side of the same counter, **Efektivia** sells AI document triage into Czech municipal offices, live at MČ Brno-střed and MěÚ Neratovice [S7].

Solved elsewhere: PermitPortal (YC F24), Permitify (YC W25) and Verdant (YC S26) show a funded US cluster around AI permit/zoning navigation [S1]. Arbitrage is scored conservatively at 1 because all analogs are US-based [S1,S4] and permitting is jurisdiction-specific; with gap de-ranked to 0 [S7], documented demand is now the only dimension carrying this record.

---
**CORRECTION (2026-08-13, post-run fact check):** The "OECD's slowest / 246 days / 157th in the world" framing traces to World Bank Doing Business 2020 — an index discontinued in 2021 after a data-manipulation scandal [S6], and it measured the full administrative cycle, not permitting alone. Replace with: ČKAIT survey (Jan 2024, n≈1,100): typical proceedings **6–12 months** [S5]. Source: https://zpravy.ckait.cz/vydani/2024-01/delka-povolovani-staveb-v-cr-nikoliv-roky-ale-mesice-ukazal-pruzkum-inzenyrske-komory/

*Checked by the 2026-08-20 evidence audit. **Verified:** the ČKAIT survey (Z+i 2024/01, published 20 Feb 2024) reports that for nearly 1,100 authorized persons "délka trvání většiny povolovacích řízení staveb v ČR, a to včetně související inženýrské činnosti, je obvykle šest měsíců až jeden rok" [S5]; and the World Bank Group discontinued Doing Business on 16 Sep 2021 following its investigation into data irregularities in the 2018 and 2020 editions [S6]. **Still open:** the specific "246 days / 157th" figures attributed to Doing Business 2020 — the archived country profile publishes them only inside downloadable figures, and `Doing Business` returns zero hits across all 6,181 signals. (figure not yet traced to a primary source on file — flagged by the 2026-08-20 evidence audit)*

---
**CORRECTION (2026-08-20, gap re-check):** De-ranked. The absence this record was built on — "no CZ startup automating permit preparation or navigation" [S3] — was never checked against Czech-language surfaces; it was recorded against a YC company page. Checked properly on 2026-08-20, it does not hold: **Průvodka** (pruvodka.cz) is a live, priced Czech AI product that assembles the vyjadřovačky and stanoviska a stavebník needs before applying, and **Efektivia** (efektivia.eu) sells the mirror-image triage tool to stavební úřady [S7]. `scores.gap` 2 -> 0 and `score` 6 -> 4 under the SPEC §4 de-rank rule, `status` -> watching; the existing-non-solutions and comparables paragraphs are rewritten so the prose no longer contradicts the score. Neither incumbent appears in `data/signals/funded/`, and neither would: both are unfunded, so a capital-shaped ledger is structurally blind to them and only a live Czech-language search could surface them. The **title** carried the same disproved absence — "with no tooling of their own" — and has been cut. NOTE, still unresolved and left for MATCH: the title also keeps the "one of the OECD's slowest" framing that this record's own 2026-08-13 CORRECTION retracts as tracing to the discontinued World Bank Doing Business index. S2 appears to carry the OECD claim independently, so resolving it is a judgment about that source, not an audit fix, and it has not been made here.
