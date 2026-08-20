---
id: p-0002
region: cz
title: Hundreds of small Czech heat-pump and solar installation firms drown in quoting, heat-load
  calculation and NZÚ subsidy paperwork with no vertical software
category: energy
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 1
  urgency: 1
  demand: 1
  gap: 2
status: candidate
build:
  capital: garage
  first_revenue: weeks
  builder: small-team
  note: 'Per-seat SMB SaaS with no procurement gate — an NZÚ-paperwork wedge can sell consulting-led
    within weeks, though heat-load calculation and workflow depth take a small team (autarc
    started with 3 founders).'
comps:
- name: autarc
  url: https://www.autarc.energy/
  geo: DE
  since: 2023
  traction: '~$9.3M raised over 3 rounds (Tracxn, 2026); 380 German installer customers and
    7-digit ARR at YC S24 launch (Y Combinator, 2024)'
  signal: yc-autarc
- name: Reonic
  url: https://reonic.com/
  geo: DE
  since: 2021
  traction: '€13M Series A led by Northzone, €16M total (TechCrunch, 2024); installer sales/planning/ops
    software live in DACH, FR, IT'
  markets: [AT, CH, FR, IT]
sources:
- type: arbitrage
  url: https://www.ycombinator.com/companies/autarc
  note: 'yc-autarc: autarc (YC S24, Berlin, ~30 people) — agentic OS for heat-pump/solar installers:
    heat-load calc, quoting, subsidy paperwork, project management. Germany-proven where installer
    workflows and subsidy bureaucracy mirror CZ. No CZ player found (absence check 2026-08-13).
    Demand point: hundreds of small montážní firmy drowning in NZÚ paperwork per the signal
    — evidence carried here, hence the dims tag.'
  date: '2026-08-13'
  signal: yc-autarc
  dims:
  - proof
  - demand
- type: subsidy
  url: https://www.ycombinator.com/companies/autarc
  note: Signal note references Nová zelená úsporám driving tens of thousands of heat-pump/FVE
    installs per year — the subsidy program whose application handling is part of the workflow
    burden.
  date: '2026-08-13'
- type: gap-check
  url: https://www.ycombinator.com/companies/autarc
  note: 'Absence check 2026-08-13: CZ searches surface only manufacturer configurators (Master
    Therm) and installation companies themselves; no installer-ops SaaS. Woltair is a vertically
    integrated installer, not a software vendor to the long tail.'
  date: '2026-08-13'
- type: subsidy
  url: https://novazelenausporam.cz/
  note: 'dotace-nzu-2026-zranitelne-domacnosti: the redesigned Nová zelená úsporám opened
    25.6.2026 — advance grants up to 400k CZK now target low-income/vulnerable households
    (insulation, heat sources), other owners are shifted to zero-interest loans, and
    a renovation pass becomes mandatory; applications run until 31.10.2029 or fund
    exhaustion.'
  date: '2029-10-31'
  signal: dotace-nzu-2026-zranitelne-domacnosti
- type: subsidy
  url: https://planobnovy.gov.cz/vyhlasene-vyzvy/
  note: 'dotace-npo-2-2026-renovacni-pas: NPO call 2/2026 funds building renovation
    passports — up to 50k CZK per family house / 100k CZK per apartment building for
    a professional renovation assessment delivered by SFZP-accredited specialists,
    deadline 30.11.2026. The renovation pass is newly the gate to NZÚ 2026+ retrofit
    support.'
  date: '2026-11-30'
  signal: dotace-npo-2-2026-renovacni-pas
created: '2026-08-13'
updated: '2026-08-20'
---

Hundreds of small Czech montážní firmy execute the tens of thousands of heat-pump and photovoltaic installations driven each year by Nová zelená úsporám [S1,S2]. Per the yc-autarc signal they are drowning in the surrounding paperwork: digital site survey, heat-load calculation, quote generation, subsidy application handling and install project tracking are done with spreadsheets, manufacturer configurators and manual NZÚ form-filling [S1].

Why now: NZÚ volumes keep the long tail of installers at capacity [S2], and the German comparison is direct — autarc (YC S24, Berlin) built exactly this stack for a market whose installer workflows and subsidy bureaucracy mirror the Czech setup, and reached ~30 people on it [S1]. The workflow is subsidy-shaped, so a CZ product must be built around NZÚ specifically; foreign tools do not transfer without localization, which protects a local entrant.

Who pays: the installation firms themselves (per-seat or per-project SaaS), for whom faster quoting and correctly filed subsidy applications convert directly to revenue; secondarily manufacturers and distributors who want their long-tail installer channel to be more productive.

Existing non-solutions: manufacturer sizing configurators (e.g. Master Therm), generic project tools, and Woltair — which is a vertically integrated installer competing with the long tail, not selling software to it [S3]. The 2026-08-13 absence check found no Czech installer-ops SaaS [S3].

Solved elsewhere: autarc in Germany is the funded, directly adjacent analog; no Czech player was found [S1], which under the scoring rubric is a clean DE-analog-plus-no-CZ-player arbitrage. Money point reflects the NZÚ subsidy program referenced in the signal note as the workflow's economic engine [S2].

## First moves

1. Interview ten small heat-pump/FVE montážní firmy — the long tail executing the tens of thousands of NZÚ-driven installs per year [S2] — and time two numbers per firm: hours per quote and hours per NZÚ subsidy application, both done today with spreadsheets, manufacturer configurators and manual form-filling per the record.
2. Build the NZÚ-paperwork wedge first: generate the complete subsidy-application package from the data already captured in a quote — correctly filed applications convert directly to installer revenue, and the subsidy-shaped workflow is exactly the localization moat that keeps foreign tools out.
3. Verify the volume assumption before scaling: the redesigned [NZÚ 2026+](/sources/tenders#dotace-nzu-2026-zranitelne-domacnosti) (opened 25.6.2026, applications until **2029-10-31**) narrows direct grants to vulnerable households (advance grants up to 400k CZK) and shifts other owners to zero-interest loans plus a newly mandatory renovation pass [S4] — confirm with the interviewed firms that application volume and paperwork burden survive the pivot.
4. Then displace the manufacturer configurators: add heat-load calculation and digital site survey so a firm quotes from one tool instead of Master Therm-style sizing tools plus spreadsheets [S3] — the depth that carried autarc (~$9.3M raised, 380 DE customers) and Reonic (€13M Series A) to installer scale in Germany.
5. Funding reality: the open calls on file fund the buyer's order book, not the software — NZÚ 2026+ keeps the long tail at capacity, and the [NPO 2/2026 Renovační pas call](/sources/tenders#dotace-npo-2-2026-renovacni-pas) (grants up to 50k/100k CZK per building, deadline **2026-11-30**) makes renovation passports the gate to NZÚ retrofit money [S5] — new mandatory paperwork the product can automate. The software itself is commercial revenue only.
6. Competition on file: **Master Therm**-style manufacturer configurators (sizing only) and **Woltair** (vertically integrated installer competing with the long tail, not selling software to it); the 2026-08-13 absence check found no CZ installer-ops SaaS [S3].
