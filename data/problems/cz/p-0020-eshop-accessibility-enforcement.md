---
id: p-0020
region: cz
title: Czech e-shops and digital services are in the European Accessibility Act's first enforcement
  year — ČOI is test-purchasing checkout flows while most sites remain non-compliant
category: retail-services
geo: CZ-national
score: 4
scores:
  proof: 0
  money: 0
  urgency: 3
  demand: 1
  gap: 0
status: candidate
build:
  capital: garage
  first_revenue: weeks
  builder: small-team
  note: 'ČOI is already test-purchasing checkout flows, so audits and remediation sell to obligated
    e-shops immediately; a dev plus accessibility auditor shipping zákon č. 424/2023 mapping
    and a Shoptet-channel app needs integration effort, not capital.'
comps:
- name: AudioEye
  url: https://www.audioeye.com/
  geo: US
  since: 2005
  traction: 'NASDAQ: AEYE; $38.7M ARR, ~123k customers (Q3 2025 results); EU push timed to
    EAA enforcement (PRNewswire, Jul 2025)'
- name: accessiBe
  url: https://accessibe.com/
  geo: IL
  since: 2018
  traction: '$58M raised (Crunchbase); ~110k customers, widget on 200k+ sites (2024); overlay
    model auditors contest'
sources:
- type: regulation
  url: https://coi.gov.cz/pro-podnikatele/pristupnost-vyrobku-a-sluzeb-pro-podnikatele/
  note: 'reg-accessibility-act-cz: European Accessibility Act as zákon č. 424/2023 Sb., in
    force since 28 Jun 2025; 2026 is the first full enforcement year — ČOI runs mystery-shopping
    test purchases across whole checkout flows and can order corrective measures and fines.
    Forcing function live: deadline 2.'
  date: '2026-06-28'
  signal: reg-accessibility-act-cz
- type: complaint
  url: https://www.shop5.cz/clanek/faq-pristupnost-e-shopu-a-zakon-c-424-2023-sb-na-koho-se-skutecne-vztahuje/
  note: E-commerce industry FAQ traffic (shop5.cz and peers) documents merchant confusion
    about scope and obligations — scattered but real industry pressure; demand scored 1.
  date: '2026-08-13'
created: '2026-08-13'
updated: '2026-08-19'
---

The European Accessibility Act became Czech law (zákon č. 424/2023 Sb.) in June 2025, and 2026 is its first full enforcement year: ČOI conducts mystery-shopping test purchases that walk entire e-shop checkout flows, with power to order corrective measures and levy fines. In scope: e-shops, banks, transport ticketing, e-book sellers and consumer-device makers — with an exemption only for micro-enterprises providing services. The Czech e-commerce sector, one of Europe's densest per capita, is largely non-compliant with WCAG-level accessibility.

Why now: the obligation is no longer approaching — it is live, and the enforcement mechanism is a regulator that shops your site. Merchant-facing FAQ content and industry confusion about scope show the market discovering the obligation only as enforcement starts.

Who pays: e-shops and digital-service providers buying audits, remediation and continuous monitoring; e-commerce platforms (Shoptet's ~30k+ merchants) are the structural channel — one platform integration reaches thousands of obligated shops at once.

Existing non-solutions: global accessibility-overlay vendors (accessiBe, UserWay) sell widgets of contested effectiveness and no Czech legal mapping; a handful of Czech agencies do manual audits at consulting prices. No productized CZ compliance offering with zákon č. 424/2023 mapping was verified this cycle (gap unchecked, scored 0).

Next moves: a gap check on Czech accessibility-tooling, a ČOI enforcement-statistics receipt (first fines would be a demand=2 upgrade), and a Shoptet-ecosystem probe to validate the platform channel.
