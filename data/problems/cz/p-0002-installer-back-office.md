---
id: p-0002
region: cz
title: Hundreds of small Czech heat-pump and solar installation firms drown in quoting, heat-load
  calculation and NZÚ subsidy paperwork
fix: 'One tool for small heat-pump and solar firms: size the system, price the job and
  fill in the state renovation-subsidy forms from the same quote, instead of a
  manufacturer''s sizing tool plus spreadsheets.'
category: energy
geo: CZ-national
score: 5
scores:
  proof: 2
  money: 1
  urgency: 1
  demand: 1
  gap: 0
status: watching
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
  name: "autarc"
  why: "Berlin's operating system for heat-pump and solar installers (YC S24) — heat-load calculation, quoting, subsidy paperwork and project tracking in one tool, in a market whose installer workflows mirror Czechia's."
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
  name: "Nová zelená úsporám"
  why: "The subsidy programme behind tens of thousands of Czech heat-pump and photovoltaic installs a year — and behind the application paperwork the installers carry."
  url: https://www.ycombinator.com/companies/autarc
  note: Signal note references Nová zelená úsporám driving tens of thousands of heat-pump/FVE
    installs per year — the subsidy program whose application handling is part of the workflow
    burden.
  date: '2026-08-13'
- type: gap-check
  name: "First Czech market scan"
  why: "An early sweep that surfaced only manufacturer sizing configurators and Woltair — superseded by the four Czech installer-software vendors found later."
  url: https://www.ycombinator.com/companies/autarc
  note: 'Absence check 2026-08-13: CZ searches surface only manufacturer configurators (Master
    Therm) and installation companies themselves; no installer-ops SaaS. Woltair is a vertically
    integrated installer, not a software vendor to the long tail.'
  date: '2026-08-13'
- type: subsidy
  name: "Nová zelená úsporám 2026 redesign"
  why: "From 25 June 2026 advance grants up to 400k CZK narrow to vulnerable households, other owners shift to zero-interest loans, and a renovation pass becomes mandatory; applications run to 31 Oct 2029."
  url: https://novazelenausporam.cz/
  note: 'dotace-nzu-2026-zranitelne-domacnosti: the redesigned Nová zelená úsporám opened
    25.6.2026 — advance grants up to 400k CZK now target low-income/vulnerable households
    (insulation, heat sources), other owners are shifted to zero-interest loans, and
    a renovation pass becomes mandatory; applications run until 31.10.2029 or fund
    exhaustion.'
  date: '2029-10-31'
  signal: dotace-nzu-2026-zranitelne-domacnosti
- type: subsidy
  name: "NPO call 2/2026 — renovation passport"
  why: "Up to 50k CZK per family house and 100k per apartment building for a professional renovation assessment, deadline 30 Nov 2026 — newly the gate to NZÚ retrofit money, and new paperwork to automate."
  url: https://planobnovy.gov.cz/vyhlasene-vyzvy/
  note: 'dotace-npo-2-2026-renovacni-pas: NPO call 2/2026 funds building renovation
    passports — up to 50k CZK per family house / 100k CZK per apartment building for
    a professional renovation assessment delivered by SFZP-accredited specialists,
    deadline 30.11.2026. The renovation pass is newly the gate to NZÚ 2026+ retrofit
    support.'
  date: '2026-11-30'
  signal: dotace-npo-2-2026-renovacni-pas
- type: gap-check
  name: "Wue and three Czech rivals"
  why: "Wue sells per-seat quoting plus NZÚ documentation to installers at 650 Kč per user a month (200 Kč more for heat pumps); RAYNET, AutoERP and Infina sell into the same firms."
  url: https://wue.cz/
  note: 'Gap re-check 2026-08-20: looked for CZ vertical software selling quoting, design and
    NZÚ subsidy paperwork to heat-pump/FVE montážní firmy. Found, and the NZÚ-paperwork wedge
    this record proposes building first is already occupied. Wue (wue.cz) "urychluje a automatizuje
    tvorbu cenových nabídek pro fotovoltaické elektrárny", generates contracts, handover protocols
    and NZÚ subsidy documentation, bundles a PV roof configurator via Fohet and a heat-pump
    extension, and is priced per seat at 650 Kč/user/month plus 200 Kč for the TČ module —
    per-seat vertical SaaS sold to installers, not a manufacturer configurator. RAYNET, a CZ
    CRM vendor, ships a photovoltaics vertical that auto-generates "dotační formuláře a dokumenty
    distributorů přímo z CRM" for NZÚ, ČEZ, PRE and EG.D, plus a field mobile app for montážní
    týmy and a dispatcher calendar; Bubble Development reports implementing it at ~20 PV companies.
    AutoERP (Apertia Tech) sells three CRM/ERP variants for FVE installation firms and Infina
    sells a CRM with a payback calculator for HP/FVE dealers. Note the method finding: the
    English-language query returned no CZ vendor at all while the Czech queries returned four,
    which is how the 2026-08-13 check missed them. Local players named: gap 2 -> 0 and status
    moves to watching per the de-rank rule.'
  date: '2026-08-20'
  queries:
    - "software pro montážní firmy tepelná čerpadla fotovoltaika nabídky zakázky dotace"
    - "software pro fotovoltaické firmy návrh cenová nabídka řízení zakázek CRM montáže"
    - "program výpočet tepelné ztráty návrh tepelného čerpadla nabídka pro montážní firmy software"
    - "Czech software for heat pump and solar installers quoting subsidy paperwork field service"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
created: '2026-08-13'
updated: '2026-08-25'
---

Hundreds of small Czech montážní firmy execute the tens of thousands of heat-pump and photovoltaic installations driven each year by Nová zelená úsporám [S1,S2]. The evidence on file shows them drowning in the surrounding paperwork: digital site survey, heat-load calculation, quote generation, subsidy application handling and install project tracking are done with spreadsheets, manufacturer configurators and manual NZÚ form-filling [S1].

Why now: NZÚ volumes keep the long tail of installers at capacity [S2], and the German comparison is direct — autarc (YC S24, Berlin) built exactly this stack for a market whose installer workflows and subsidy bureaucracy mirror the Czech setup, and reached ~30 people on it [S1]. The workflow is subsidy-shaped, so a CZ product must be built around NZÚ specifically; foreign tools do not transfer without localization, which protects a local entrant.

Who pays: the installation firms themselves (per-seat or per-project SaaS), for whom faster quoting and correctly filed subsidy applications convert directly to revenue; secondarily manufacturers and distributors who want their long-tail installer channel to be more productive.

Existing non-solutions: manufacturer sizing configurators (e.g. Master Therm), generic project tools, and Woltair — which is a vertically integrated installer competing with the long tail, not selling software to it [S3]. But the software position itself is not empty: Wue sells per-seat quoting-plus-NZÚ-documentation software to FVE and heat-pump firms at 650 Kč/user/month, RAYNET ships a photovoltaics CRM vertical that auto-generates NZÚ and distributor forms with a field app for installation crews, and AutoERP and Infina sell CRM/ERP into the same buyers [S6]. The earlier finding that no such software existed [S3] is superseded.

Solved elsewhere: autarc in Germany is the funded, directly adjacent analog [S1]. The case is no longer a German analog facing an empty Czech field, because CZ players exist [S6]; what the German comparison now describes is depth — heat-load calculation and digital site survey — rather than absence. The NZÚ subsidy program is the workflow's economic engine [S2].

## First moves

1. Interview ten small heat-pump/FVE montážní firmy — the long tail executing the tens of thousands of NZÚ-driven installs per year [S2] — and time two numbers per firm: hours per quote and hours per NZÚ subsidy application, both done today with spreadsheets, manufacturer configurators and manual form-filling per the record.
2. Do NOT build the NZÚ-paperwork wedge first — it is taken. Wue generates NZÚ subsidy documentation from quote data today, and RAYNET auto-generates NZÚ and distributor forms straight out of its PV CRM [S6]. Buy both, run a real quote through each, and find what they do badly before assuming there is room.
3. Verify the volume assumption before scaling: the redesigned [NZÚ 2026+](/sources/tenders#dotace-nzu-2026-zranitelne-domacnosti) (opened 25.6.2026, applications until **2029-10-31**) narrows direct grants to vulnerable households (advance grants up to 400k CZK) and shifts other owners to zero-interest loans plus a newly mandatory renovation pass [S4] — confirm with the interviewed firms that application volume and paperwork burden survive the pivot.
4. Then displace the manufacturer configurators: add heat-load calculation and digital site survey so a firm quotes from one tool instead of Master Therm-style sizing tools plus spreadsheets [S3] — the depth that carried autarc and Reonic to installer scale in Germany.
5. Funding reality: the open calls on file fund the buyer's order book, not the software — NZÚ 2026+ keeps the long tail at capacity, and the [NPO 2/2026 Renovační pas call](/sources/tenders#dotace-npo-2-2026-renovacni-pas) (grants up to 50k/100k CZK per building, deadline **2026-11-30**) makes renovation passports the gate to NZÚ retrofit money [S5] — new mandatory paperwork the product can automate. The software itself is commercial revenue only.
6. Competition on file — the category is occupied, so the moves above are competitive research rather than a greenfield plan: **Wue** (per-seat quoting plus NZÚ documentation for FVE/TČ firms, 650 Kč/user/month), **RAYNET** (photovoltaics CRM vertical with NZÚ and distributor form generation and a crew mobile app), **AutoERP** (Apertia Tech) and **Infina** [S6]; plus **Master Therm**-style manufacturer configurators (sizing only) and **Woltair** (vertically integrated installer competing with the long tail, not selling software to it) [S3].

## Revisions

2026-08-20 · gap re-check and evidence audit — Two blocks recorded on this date, merged here. The absence claim was false: Czech-language search found four CZ vendors selling installer-facing software to heat-pump and FVE firms — Wue, RAYNET's photovoltaics vertical, AutoERP and Infina [S6] — so gap moved 2 → 0, score 7 → 5, status candidate → watching per the SPEC §4 de-rank rule. The record's proposed first product move, the NZÚ-paperwork wedge, is the part most clearly already shipped. Two things made the original check miss this. It cited a foreign page (ycombinator.com/companies/autarc) as the receipt for a Czech absence, which proves nothing about Czechia; and the search appears to have run in English, where the same re-check returned no Czech vendor at all while the Czech-language queries returned four. None of the four appears anywhere in this register's signal corpus — they are bootstrapped SMB software companies that no funding feed surfaces. The title carried the same disproved absence, "with no vertical software", and has been cut to the part that still stands, for the same reason: the title is the most-read line on the record and it was asserting what the ledger below it now refutes. What survives is the demand claim [S1] and the observation that the CZ tools are quoting/CRM-shaped rather than autarc-depth — heat-load calculation and digital site survey remain genuinely thin here, but that is a product-differentiation argument, not an absence. Cut in the same pass: the autarc funding-and-customer parenthetical and the Reonic Series A parenthetical in the fourth first move. Both figures live only in the comps ledger — Reonic returns no hits anywhere in the signal corpus, and yc-autarc carries neither the raise nor the customer count — and a comparable's traction line cannot back a body claim. The "Where it works" ledger still prints both.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched.
