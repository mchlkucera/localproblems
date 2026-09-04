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
score: 6
scores:
  proof: 3
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
locals:
- name: Wue
  url: https://wue.cz/
  ico: '17824427'
  since: 2022
  competes: direct
  maturity: early
  evidence: 'Software for solar installers at 650 Kč a month per seat plus 200 Kč for the
    heat-pump module, generating quotes, contracts, handover protocols and the paperwork for
    the state renovation subsidy (NZÚ). Wue Technologies s.r.o. was incorporated in December
    2022 and names no installer running on it.'
- name: RAYNET
  url: https://raynet.cz/
  ico: '26843820'
  since: 2004
  competes: direct
  maturity: established
  evidence: 'Its photovoltaics vertical runs at roughly 20 Czech solar installer firms, per its
    implementation partner Bubble Development, and generates state-subsidy and distributor
    forms straight out of the CRM, with a field app for fitting crews. RAYNET s.r.o. has traded
    since 2004; the year the photovoltaics vertical itself launched is not published, so the
    year shown is the company''s.'
- name: AutoERP (Apertia Tech)
  url: https://autoerp.cz/
  ico: '27117758'
  since: 2004
  competes: direct
  maturity: early
  evidence: 'Three CRM and ERP variants sold to photovoltaic installation firms. Apertia Tech
    s.r.o. has traded since 2004, but for this product nothing is published: no deployment
    figure, no public contract for the IČO in the state contracts register and no funding.'
- name: Infina
  url: https://infina.cz/
  ico: '06904424'
  since: 2018
  competes: direct
  maturity: early
  evidence: 'A CRM with a payback calculator sold to heat-pump and photovoltaic dealers. Infina
    company s.r.o. has traded since 2018 but names no dealer running it and publishes no
    funding.'
sources:
- type: arbitrage
  name: "autarc"
  gist: "the German installer template"
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
  gist: "the subsidy behind the volume"
  why: "The subsidy programme behind tens of thousands of Czech heat-pump and photovoltaic installs a year — and behind the application paperwork the installers carry."
  url: https://www.ycombinator.com/companies/autarc
  note: Signal note references Nová zelená úsporám driving tens of thousands of heat-pump/FVE
    installs per year — the subsidy program whose application handling is part of the workflow
    burden.
  date: '2026-08-13'
- type: gap-check
  name: "First Czech market scan"
  gist: "the superseded first sweep"
  why: "An early sweep that surfaced only manufacturer sizing configurators and Woltair — superseded by the four Czech installer-software vendors found later."
  url: https://www.ycombinator.com/companies/autarc
  note: 'Absence check 2026-08-13: CZ searches surface only manufacturer configurators (Master
    Therm) and installation companies themselves; no installer-ops SaaS. Woltair is a vertically
    integrated installer, not a software vendor to the long tail.'
  date: '2026-08-13'
- type: subsidy
  name: "Nová zelená úsporám 2026 redesign"
  gist: "the 2026 subsidy redesign"
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
  gist: "the renovation-passport grant"
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
  gist: "the four Czech incumbents"
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
- type: arbitrage
  url: https://www.ycombinator.com/companies/jasmine-energy
  note: 'yc-jasmine-energy: YC-funded US company selling AI-drafted solar incentive claims —
    the subsidy-filing half of this record''s thesis (the NZÚ paperwork), funded in a second
    market. YC listing carries no founding year or traction, so it lands as an arbitrage
    source only, per the 2026-08-20 revision''s rule — no comps entry without receipts.'
  date: '2022-08-15'
  signal: yc-jasmine-energy
- type: price
  url: https://wue.cz/
  name: "Wue — the installer list price"
  gist: "650 Kč a seat a month"
  why: "A Czech solar and heat-pump installation firm pays 650 CZK per user a month for the back office this record describes, and 200 CZK more for the heat-pump module."
  note: 'Price receipt lifted from the 2026-08-20 gap re-check already on this ledger, which
    read wue.cz: priced per seat at 650 Kč/user/month plus 200 Kč for the TČ module. Recorded
    at the base seat price, with the module stated in why. dims omitted: backs no score.
    Verified 2026-09-04: wue.cz still prints 650 Kč Měsíčně at 1 uživatel with 200 Kč /
    uživatel for the Rozšíření pro TČ heat-pump module.'
  date: '2026-08-20'
  payer: 'A Czech solar or heat-pump installation firm'
  amount_czk: 650
  unit: per-seat-month
  basis: list-price
created: '2026-08-13'
updated: '2026-09-04'
---

Hundreds of small Czech installation firms fit the tens of thousands of heat pumps and solar arrays paid for each year by NZÚ — Nová zelená úsporám, the state home-renovation subsidy [S1,S2]. They run site survey, heat-load calculation, quoting, subsidy applications and project tracking on spreadsheets, manufacturer sizing tools and hand-filled NZÚ forms [S1].

Why now: subsidy volume keeps the long tail of installers at capacity [S2], and Germany already has the tool: autarc (Y Combinator, 2024) runs this stack in Berlin with about 30 people, for installers whose paperwork mirrors Czechia's [S1]. The forms are Czech, so no foreign tool transfers without being rebuilt around NZÚ, and that rebuild protects a local entrant.

Who pays: the installation firms themselves, per seat or per job, because faster quotes and correctly filed subsidy applications are billable work. Manufacturers and distributors are the second buyer — the long tail is their sales channel.

Existing non-solutions: the software position is taken. Wue sells quoting plus NZÚ documentation to solar and heat-pump firms at 650 Kč per seat a month, 200 Kč more for the heat-pump module [S6]. RAYNET — a Czech sales-software vendor trading since 2004 — generates NZÚ and distributor forms out of its solar vertical, adds a field app for fitting crews, and runs at about 20 installer firms, per its implementation partner [S6]. AutoERP and Infina sell customer and order software into the same firms [S6]. Manufacturer sizing tools (Master Therm) only size [S3]. Woltair installs rather than selling software — it competes with the long tail [S3].

Solved elsewhere: autarc in Germany is the funded analog [S1]. What it proves now is depth — heat-load calculation and digital site survey, which the Czech tools barely touch [S6] — not an open field. NZÚ volume is the engine underneath [S2].

## First moves

1. Interview ten small heat-pump and solar firms and time two numbers each: hours per quote, hours per NZÚ application [S2]. That number is the admin cost you price against.
2. Do not start with the subsidy paperwork. It is taken: Wue builds the NZÚ documents out of quote data, and RAYNET builds the NZÚ and distributor forms out of its solar vertical [S6]. Buy both, push a real job through each, and write down what they do badly.
3. Test the volume assumption with the same ten firms. The redesigned [NZÚ 2026+](/sources/tenders#dotace-nzu-2026-zranitelne-domacnosti) opened 25 June 2026: advance grants up to 400k CZK now go to vulnerable households only, every other owner gets a zero-interest loan and a mandatory renovation pass, and applications close **2029-10-31** [S4]. Ask whether their paperwork survives that.
4. Then go where the Czech tools are thin — heat-load calculation and digital site survey — so a firm quotes from one tool instead of a Master Therm-style sizing tool plus spreadsheets [S3].
5. Automate the renovation pass next. The state's recovery-plan [call 2/2026](/sources/tenders#dotace-npo-2-2026-renovacni-pas) pays up to 50k CZK per family house and 100k per apartment building for the assessment, deadline **2026-11-30**, and the pass now gates NZÚ retrofit money [S5]. No call on file pays for the software itself — that is commercial revenue.
6. Expect competition, not a green field. **Wue**, **RAYNET**, **AutoERP** (Apertia Tech) and **Infina** all sell into these firms [S6]; **Master Therm**-style sizing tools size only, and **Woltair** installs rather than selling software [S3].

## Revisions

2026-08-20 · gap re-check and evidence audit — Two blocks recorded on this date, merged here. The absence claim was false: Czech-language search found four CZ vendors selling installer-facing software to heat-pump and FVE firms — Wue, RAYNET's photovoltaics vertical, AutoERP and Infina [S6] — so gap moved 2 → 0, score 7 → 5, status candidate → watching per the SPEC §4 de-rank rule. The record's proposed first product move, the NZÚ-paperwork wedge, is the part most clearly already shipped. Two things made the original check miss this. It cited a foreign page (ycombinator.com/companies/autarc) as the receipt for a Czech absence, which proves nothing about Czechia; and the search appears to have run in English, where the same re-check returned no Czech vendor at all while the Czech-language queries returned four. None of the four appears anywhere in this register's signal corpus — they are bootstrapped SMB software companies that no funding feed surfaces. The title carried the same disproved absence, "with no vertical software", and has been cut to the part that still stands, for the same reason: the title is the most-read line on the record and it was asserting what the ledger below it now refutes. What survives is the demand claim [S1] and the observation that the CZ tools are quoting/CRM-shaped rather than autarc-depth — heat-load calculation and digital site survey remain genuinely thin here, but that is a product-differentiation argument, not an absence. Cut in the same pass: the autarc funding-and-customer parenthetical and the Reonic Series A parenthetical in the fourth first move. Both figures live only in the comps ledger — Reonic returns no hits anywhere in the signal corpus, and yc-autarc carries neither the raise nor the customer count — and a comparable's traction line cannot back a body claim. The "Where it works" ledger still prints both.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` now carries Wue, RAYNET, AutoERP (Apertia Tech) and Infina [S6]. RAYNET passes the established test — trading since 2004, with its photovoltaics vertical reported live at roughly 20 installer firms by its implementation partner — so `scores.gap` stays 0 and the 2026-08-20 de-rank now rests on a receipt a machine can re-check. The other three are early: Wue Technologies was incorporated in December 2022 and publishes nothing the test reads, and neither AutoERP nor Infina publishes a deployment figure. `scores.proof` 2 → 3: autarc and Reonic both pass the established test on the comps ledger, and Reonic sells the same stack across DACH, France and Italy, so the model is established in more than one market with a CEE-adjacent one among them. `score` 5 → 6. The retired rung 2 read 'funded analog in DE/AT/PL/Nordics + no CZ player found', which docked this record for the very Czech vendors named below it; that gap condition is gone from the proof ladder. Fifth pass this date, merged here: `locals[]` converted from `status:` to the orthogonal `competes:` + `maturity:` pair. All four entries are `competes: direct` — Wue, RAYNET's photovoltaics vertical, AutoERP and Infina each sell quoting, subsidy paperwork and installer CRM to Czech heat-pump and solar firms, which is this record's product and this record's buyer — and each keeps the maturity it already carried. `scores.gap` stays 0: RAYNET is direct and established, so the space is taken on exactly the receipt it was taken on before. No player was ever excluded from this ledger, so there is nothing to restore. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Also cut from the RAYNET entry: the aside explaining which fallback year the scoring rule permits — a reader does not have a rule to fall back under.

2026-09-02 · plain-language pass — NZÚ and RAYNET glossed at first use; FVE, PV, CRM and ERP replaced with plain words. Argument tightened 322 → 299 words, every [Sn] marker, figure, price and named company kept, plus two ledger receipts pulled into the body: RAYNET at about 20 installer firms and Wue's 200 Kč heat-pump module [S6]. First moves rewritten in the plain house voice. A gist added to all six sources. No score, status, note or marker touched.

2026-09-04 · price receipt — The seat price already read in the 2026-08-20 sweep is now recorded as a price of its own: 650 CZK per user a month, 200 CZK more for the heat-pump module [S8]. No score, status, note or marker touched.
