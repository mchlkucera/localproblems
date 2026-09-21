---
id: p-0002
region: cz
title: 'Czech heat-pump and solar installers do subsidy paperwork by hand while quoting jobs'
brief: 'Since June 2026, state heating and insulation grants go only to poorer households, and a renovation pass is now required [S4,S5]. Installers handle that paperwork while sizing and pricing each job [S1,S6].'
solution: 'Build an app for heat-pump and solar installers that sizes the system, prices the job and fills in the subsidy forms.'
good_for: 'Someone who''d like to work with heat-pump and solar installers.'
category: energy
geo: CZ-national
score: 5
scores:
  proof: 3
  money: 1
  urgency: 0
  demand: 1
  gap: 0
status: watching
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: direct
  integration: software
  money: bootstrap
  why: 'Easier: small installation firms buy per seat out of their own money, no licence gates the work, and the tool is ordinary software. Harder: four Czech vendors already sell installer software and the subsidy paperwork, one of them to about 20 solar firms, and the subsidy rules were redesigned in June 2026.'
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
- name: Coperniq
  url: https://www.ycombinator.com/companies/coperniq
  geo: US
  since: 2021
  traction: 'Y Combinator Winter 2023 batch; founded 2021, team of 6 in San Francisco; the YC
    company page cites a $4M seed announced in November 2023 and publishes no customer count
    (Y Combinator, read 2026-09-21)'
  signal: yc-coperniq
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
process:
  summary:
    today: 'An installer sizes each system, prices the job and prepares the subsidy paperwork, and a firm without installer software likely does these in a maker''s sizing tool, spreadsheets and forms filled in by hand [S1,S3].'
  steps:
  - who: The installer
    today: 'Sizes the system in a maker''s tool'
    known: inferred
    cites: [3]
    change: changes
    after: 'Sizes it in the same app'
  - who: The installer
    today: 'Writes the quote for the job'
    known: documented
    cites: [1, 6]
    change: changes
    after: 'Prices the job from the sizing'
  - who: The installer
    today: 'Prepares the subsidy forms'
    known: documented
    cites: [1, 6]
    change: changes
    after: 'Checks forms pre-filled from the quote'
  - who: An accredited specialist
    today: 'Writes the renovation pass'
    known: documented
    cites: [5]
    change: stays
    after: 'Unchanged: the pass stays a specialist''s job'
  - who: '?'
    today: 'Who files each application with the subsidy fund is not known'
    known: unknown
    cites: []
    change: stays
    after: 'Unchanged: the app prepares the forms, not the filing'
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
  name: "Jasmine Energy"
  gist: "the US incentive-claims company"
  why: "A US company backed by Y Combinator that sells solar incentive claims drafted by AI: the subsidy-filing half of the job, funded in a second market."
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
  why: "A Czech solar and heat-pump installation firm pays 650 CZK per user a month for installer back-office software, and 200 CZK more for the heat-pump module."
  note: 'Price receipt lifted from the 2026-08-20 gap re-check already on this ledger, which
    read wue.cz: priced per seat at 650 Kč/user/month plus 200 Kč for the TČ module. Recorded
    at the base seat price, with the module stated in why. dims omitted: backs no score.
    Verified 2026-09-04: wue.cz still prints 650 Kč Měsíčně at 1 uživatel with 200 Kč /
    uživatel for the Rozšíření pro TČ heat-pump module.
    Rescored 2026-09-19: tagged dims: [money], so the "dims omitted" above no longer holds. It
    prices this job, installer software that quotes the job and prepares the subsidy paperwork,
    for the buyer this record names. A list price is an asking receipt: money 1.'
  date: '2026-08-20'
  payer: 'A Czech solar or heat-pump installation firm'
  amount_czk: 650
  unit: per-seat-month
  basis: list-price
  dims: [money]
- type: arbitrage
  name: 'Coperniq — workflow software for solar and energy contractors'
  gist: 'a third funded foreign tool'
  why: 'A San Francisco company in Y Combinator''s Winter 2023 batch sells solar and energy contractors one tool that carries a job from the sale through to the field crew, the same position the two German tools hold.'
  url: https://www.ycombinator.com/companies/coperniq
  note: 'yc-coperniq (ledger). Y Combinator company page read 2026-09-21: "Workflow software for
    solar & energy contractors", Winter 2023 batch, founded 2021, team size 6, San Francisco. The
    page cites a $4M seed round announced in November 2023, attributed there to TechCrunch, and
    publishes no customer count. Product claims ON THE PAGE, and they are the company''s own, not
    ours: it replaces spreadsheets and general CRM across sales, operations and field install,
    integrates with the hardware makers Enphase and SolarEdge for system health and service
    tickets, and claims about $3,000 of soft cost saved an installation and 45 days off a project.
    MATURITY, on the SCORING.md established test: selling since 2021 clears the three-year limb,
    but the second limb fails on every branch — no named customer or public customer count, no
    Czech public buyer, funding at seed rather than Series A, no state certification. So it is an
    EARLY foreign player and it does not touch proof, which is 3 on the two established German
    sellers. It is recorded because a third funded foreign company selling the same thing is
    intelligence a builder wants, and because it is the first US instance on this record besides
    the subsidy-filing half [S7]. No Czech buyer, no price and no gap evidence in it.'
  date: '2026-09-21'
  signal: yc-coperniq
  dims: []
created: '2026-08-13'
updated: '2026-09-21'
---

Small Czech installation firms size, price and file the subsidy paperwork for the heat pumps and solar panels the state subsidises [S1,S2].

- The state subsidy drives tens of thousands of these installs a year [S2].
- Hundreds of small installation firms fit them [S1].
- The installers carry the subsidy paperwork for subsidised jobs [S1,S6].

The subsidy is Nová zelená úsporám, or NZÚ (the state home-renovation subsidy) [S2]. Its paperwork is part of the installer's job, beside the work of sizing and pricing the system [S1].

- The work runs from a site survey and a heat-load calculation, which says how much heat a house needs, to the quote, the subsidy application and tracking the job [S1].
- Heat-pump makers such as Master Therm offer sizing tools, and those only size the system [S3].
- A firm without installer software likely does all of this with a maker's sizing tool, spreadsheets and forms filled in by hand [S1,S3].

Existing non-solutions: Four Czech vendors already sell installer software, including the subsidy paperwork, and one of them is well established [S6].

- One sells quoting and the subsidy documents per seat [S6].
- One, trading since 2004, builds the subsidy forms from its solar module [S6].
- Two more sell customer and order software to the same firms [S6].

The first also writes contracts and handover papers, bundles a roof configurator for solar panels and charges extra for a heat-pump module; its price is under [Willing to pay](#willing-to-pay) [S6]. The second is a Czech sales-software vendor, and it also builds the grid operators' forms, with a field app for fitting crews and a dispatcher calendar [S6]. One of the last two adds a payback calculator [S6].

- None of the four is described as doing a heat-load calculation or a digital site survey [S6].
- Woltair installs heat pumps itself rather than selling software, so it competes with the small installers instead of serving them [S3].

The subsidy forms are Czech, so a foreign tool would have to be rebuilt around them before it could compete here.

Why now: Since June 2026 only poorer households get the state's advance grant, and retrofit money now needs a renovation pass first [S4,S5].

- Homeowners who are not low-income now get a loan, not a grant [S4].
- Retrofit money now needs a renovation pass, a paid expert assessment [S4,S5].
- Installers handle that paperwork while sizing and pricing each job [S1,S6].

The dates behind the change come from the redesigned subsidy and a recovery-plan grant for the pass [S4,S5]:

- On 25 June 2026 the redesigned subsidy opened [S4]. Advance grants of up to 400,000 CZK now go to low-income and vulnerable households, for insulation and heat sources, and other owners get zero-interest loans instead [S4].
- On 30 November 2026 the recovery-plan grant for renovation passes stops taking applications [S5].
- Until 31 October 2029, or until the money runs out, the redesigned subsidy takes applications [S4].
- None of these dates is a legal deadline for the installers: they are a grant's rules and closing dates [S4,S5].

Who pays: Czech installer firms already buy installer software, sold per seat, and the state pays for renovation passes [S5,S6].

- One Czech tool sells per seat, per month, with the heat-pump module extra [S6].
- About 20 solar installer firms run another vendor's solar module [S6].
- The state pays up to 50,000 CZK toward a family house's renovation pass [S5].

The count of 20 comes from that vendor's implementation partner, Bubble Development [S6].

The pass grant is call 2/2026 of the national recovery plan [S5]. It pays up to 50,000 CZK per family house and 100,000 CZK per apartment building for the assessment, which specialists accredited by the State Environmental Fund carry out [S5]. Neither the pass grant nor the redesigned subsidy pays for installer software [S4,S5].

Firms would pay per seat or per job, because faster quotes and correctly filed applications are work they bill for. Heat-pump makers and distributors could be a second buyer, since the small installers are how they sell.

Solved elsewhere: A Berlin company sells heat-pump and solar installers one tool, from heat-load calculation to the subsidy paperwork [S1].

It has about 30 people and joined Y Combinator in 2024 [S1]. Its funding and customer count are in its row above, beside a second German company that sells installers sales, planning and operations software in several countries. Installer work and subsidy paperwork in Germany are described as mirroring Czechia's [S1].

Jasmine Energy, a US company backed by Y Combinator, sells solar incentive claims drafted by AI: the subsidy-filing half alone, funded in a second market [S7].

A San Francisco company, also backed by Y Combinator, sells solar and energy contractors one tool for the whole job, from the sale to the crew in the field [S9]. It is six people on seed money and names no customer, so it shows the model being built rather than proven [S9].

What the German tool shows now is depth, a heat-load calculation and a digital site survey, not an open field here [S1,S6].

## First moves

1. Sit with ten small heat-pump and solar installers and time how long one quote and one subsidy application take each. That time is the admin cost you price against. Ask each firm, too, whether its paperwork changed when the subsidy was redesigned this summer, and whether the new renovation pass has added work; see [Why now](#why-now).
2. Buy the two leading Czech installer tools, push one real job through each, and write down what they do badly. The subsidy paperwork is already sold to these firms, so don't start there; see [Market gap](#competition). What they do badly is where a new tool can win.
3. Build the heat-load calculation and the digital site survey first, so a firm can size, price and file from one tool. The Czech tools barely touch those steps, while the German company sells them; see [Market gap](#competition) and [Validated abroad](#validated-abroad). Today a firm sizes the system in a maker's tool and prices it somewhere else, so one tool saves it a step on every job.
4. Add the renovation pass next, because it now stands between a homeowner and the retrofit money. The state pays for the assessment, which accredited specialists carry out, as [Willing to pay](#willing-to-pay) shows, but no state money pays for the software, so the firm itself is the customer.

## Revisions

2026-08-20 · gap re-check and evidence audit — Two blocks recorded on this date, merged here. The absence claim was false: Czech-language search found four CZ vendors selling installer-facing software to heat-pump and FVE firms — Wue, RAYNET's photovoltaics vertical, AutoERP and Infina [S6] — so gap moved 2 → 0, score 7 → 5, status candidate → watching per the SPEC §4 de-rank rule. The record's proposed first product move, the NZÚ-paperwork wedge, is the part most clearly already shipped. Two things made the original check miss this. It cited a foreign page (ycombinator.com/companies/autarc) as the receipt for a Czech absence, which proves nothing about Czechia; and the search appears to have run in English, where the same re-check returned no Czech vendor at all while the Czech-language queries returned four. None of the four appears anywhere in this register's signal corpus — they are bootstrapped SMB software companies that no funding feed surfaces. The title carried the same disproved absence, "with no vertical software", and has been cut to the part that still stands, for the same reason: the title is the most-read line on the record and it was asserting what the ledger below it now refutes. What survives is the demand claim [S1] and the observation that the CZ tools are quoting/CRM-shaped rather than autarc-depth — heat-load calculation and digital site survey remain genuinely thin here, but that is a product-differentiation argument, not an absence. Cut in the same pass: the autarc funding-and-customer parenthetical and the Reonic Series A parenthetical in the fourth first move. Both figures live only in the comps ledger — Reonic returns no hits anywhere in the signal corpus, and yc-autarc carries neither the raise nor the customer count — and a comparable's traction line cannot back a body claim. The "Where it works" ledger still prints both.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` now carries Wue, RAYNET, AutoERP (Apertia Tech) and Infina [S6]. RAYNET passes the established test — trading since 2004, with its photovoltaics vertical reported live at roughly 20 installer firms by its implementation partner — so `scores.gap` stays 0 and the 2026-08-20 de-rank now rests on a receipt a machine can re-check. The other three are early: Wue Technologies was incorporated in December 2022 and publishes nothing the test reads, and neither AutoERP nor Infina publishes a deployment figure. `scores.proof` 2 → 3: autarc and Reonic both pass the established test on the comps ledger, and Reonic sells the same stack across DACH, France and Italy, so the model is established in more than one market with a CEE-adjacent one among them. `score` 5 → 6. The retired rung 2 read 'funded analog in DE/AT/PL/Nordics + no CZ player found', which docked this record for the very Czech vendors named below it; that gap condition is gone from the proof ladder. Fifth pass this date, merged here: `locals[]` converted from `status:` to the orthogonal `competes:` + `maturity:` pair. All four entries are `competes: direct` — Wue, RAYNET's photovoltaics vertical, AutoERP and Infina each sell quoting, subsidy paperwork and installer CRM to Czech heat-pump and solar firms, which is this record's product and this record's buyer — and each keeps the maturity it already carried. `scores.gap` stays 0: RAYNET is direct and established, so the space is taken on exactly the receipt it was taken on before. No player was ever excluded from this ledger, so there is nothing to restore. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Also cut from the RAYNET entry: the aside explaining which fallback year the scoring rule permits — a reader does not have a rule to fall back under.

2026-09-02 · plain-language pass — NZÚ and RAYNET glossed at first use; FVE, PV, CRM and ERP replaced with plain words. Argument tightened 322 → 299 words, every [Sn] marker, figure, price and named company kept, plus two ledger receipts pulled into the body: RAYNET at about 20 installer firms and Wue's 200 Kč heat-pump module [S6]. First moves rewritten in the plain house voice. A gist added to all six sources. No score, status, note or marker touched.

2026-09-04 · price receipt — The seat price already read in the 2026-08-20 sweep is now recorded as a price of its own: 650 CZK per user a month, 200 CZK more for the heat-pump module [S8]. No score, status, note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` on who is stuck and what is happening, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Hundreds of small Czech heat-pump and solar installation firms drown in quoting, heat-load calculation and NZÚ subsidy paperwork". Previous solution, verbatim: "One tool for small heat-pump and solar firms: size the system, price the job and fill in the state renovation-subsidy forms from the same quote, instead of a manufacturer's sizing tool plus spreadsheets." The record carried no brief and no good_for before this pass. Every claim was checked against this record's sources first. The old title's "drown in" paperwork and the "hundreds of small firms" count rest only on the harvest note behind [S1], which carries no receipt of its own, so neither is repeated; the headline now says what the firms do, which the Czech installer software already on sale confirms [S6], and that manufacturer sizing tools only size [S3]. The redesigned subsidy opened on 25 June 2026 [S4], a date already past, so it is stated as a change and not as a deadline; the renovation pass as the new gate to the money is [S5]. Four Czech vendors already sell installer software, one of them established [S6]; the solution describes the product neutrally. No score, status, source, note, marker or body sentence changed. Simplified for the front page: title "Small Czech heat-pump and solar firms size jobs, price them and file subsidy forms in separate tools" → "Czech solar and heat-pump installers quote jobs and file subsidies in separate tools"; brief "Since June 2026, state grants for home heating and insulation go only to poorer households, other owners get interest-free loans, and a renovation pass is now required [S4,S5]. Installers handle that subsidy paperwork alongside sizing and pricing their jobs [S1,S6]." → "Since June 2026, state heating and insulation grants go only to poorer households, and a renovation pass is now required [S4,S5]. Installers handle that paperwork while sizing and pricing each job [S1,S6]."; solution "Build an app for heat-pump and solar installers that sizes the system, prices the job and fills in the subsidy forms, as companies already do in Germany." → "Build an app for heat-pump and solar installers that sizes the system, prices the job and fills in the subsidy forms.". Headline "quote jobs" stands for the sizing and pricing the old headline named; the loans half of the June change, and "as companies already do in Germany", were cut for length. Same date, pain-point pass: title "Czech solar and heat-pump installers quote jobs and file subsidies in separate tools" → "Czech heat-pump and solar installers do subsidy paperwork by hand while quoting jobs". Why: the old headline named two tools and no one hurting. The new one names the installers and the manual paperwork, which is the body's own sourced claim (hand-filled subsidy forms beside quoting [S1]) and what the unchanged brief already tells [S1,S6]. Brief unchanged. No score, status, source, note or body sentence changed.

2026-09-18 · body rewritten to the writing rules, process figure added — Every section now opens with ONE answer sentence, each first list carries its three most important items, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on what the installers do for the subsidised installs, with the install volume, the firm count and the paperwork as its items [S1,S2,S6], and the workflow, the makers' sizing tools and Master Therm (from move 6) as detail [S1,S3]. Competition opens on the four Czech vendors and describes each by what it sells; their names, years and IČOs stay in their `locals[]` rows, the seat price stays in its receipt [S8], and the non-ledger names (Master Therm, Woltair, Bubble Development) stay named [S3,S6]. Why now no longer opens on the German comparable, which moved to Validated abroad; it opens on the pain of the June 2026 redesign, a loan instead of a grant for better-off homeowners and a renovation pass before retrofit money, with the dates below as plain bullets [S4,S5]. Willing to pay now says what is spent: firms buy installer software per seat, one vendor's solar module runs at about 20 firms, and the state pays for renovation passes [S5,S6]. Validated abroad opens on the Berlin company without naming it, keeps its size and batch [S1], and gains the US incentive-claims company that sat only in the sources [S7]. The moves went from six to four: old moves 1 and 3 (time the firms, test the redesign) merged, old move 6 (the named competitors) folded into move 2, old move 5's figures moved to Why now and Willing to pay, and every marker, figure, company name and bold was dropped for links. Old move 3 and move 5 linked to `/sources/tenders#…`, the private sources page; those links are gone and their facts are in the body [S4,S5]. `entry.why` was rewritten as "Easier: … Harder: …" with the same gates, and no longer names the established vendor. `S8.why` said "the back office this record describes", which a reader sees; it now says "installer back-office software". [S7] gained the public name, gist and why it lacked; its note is untouched. PROCESS FIGURE ADDED, five steps: the installer sizes the system in a maker's tool (inferred from [S3], which found makers' configurators and no installer tool, so it is drawn dashed); writes the quote [S1,S6]; prepares the subsidy forms [S1,S6]; an accredited specialist writes the renovation pass, unchanged [S5]; and who files each application with the subsidy fund is marked unknown. No actor or system was invented. Corrected against the sources rather than against the old sentences: "they run … on spreadsheets, manufacturer sizing tools and hand-filled NZÚ forms [S1]" — [S1] names the tasks and the paperwork burden, not spreadsheets or hand-filled forms, so it is now written as a likely picture for a firm without installer software [S1,S3]; "subsidy volume keeps the long tail of installers at capacity [S2]" — [S2] gives tens of thousands of installs a year and says nothing of capacity, so the capacity claim is cut; "that rebuild protects a local entrant" had no source and now reads only that a foreign tool would have to be rebuilt around the Czech forms; "manufacturers and distributors are the second buyer" had no source and now reads "could be"; and old move 1 cited [S2] for hours per quote, which [S2] does not measure. Flagged as inference: the likely spreadsheets and hand-filled forms [S1,S3]; the foreign-tool rebuild; that firms would pay per seat or per job; the makers and distributors as a possible second buyer; the sizing step in the figure [S3]; and "what the German tool shows now is depth", read from no Czech vendor being described as doing a heat-load calculation or a site survey [S6]. "Hundreds of small installation firms" is kept with [S1], whose note carries it from the funding signal, as the 2026-09-16 entry already noted. Added from sources already on file: the dispatcher calendar, the roof configurator and the payback calculator [S6], the loans for other owners and the 31 October 2029 end date [S4], the 100,000 CZK apartment-building cap and the State Environmental Fund's accreditation [S5], and the US company [S7]. No score, status, source, `note:`, `sources[]` order, title, brief, solution, good_for or `entry` gate value changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 1 → 0; Willing to pay stays 1; score 6 → 5, still FAIR. Why now: the old 1 was the retired freshness point on a deadline part of 0. No regulation is on file: the redesigned subsidy [S4] and the renovation-pass call closing on 30 November 2026 [S5] are a grant's rules and closing date, which put no dated duty on an installer, and this ladder does not read a grant's date. Willing to pay, tagging pass first: every source on file was read for someone paying for this exact job, installer software that sizes and prices the job and prepares the subsidy forms, or that work bought in. Counted: Wue's list price, 650 CZK per seat a month for quoting, contracts and the state subsidy paperwork, with the heat-pump module extra [S8]. It was already a price receipt, untagged; it now carries `dims: [money]`. A list price is an asking receipt, rung 1. Not counted: the roughly 20 installer firms running another vendor's solar module, which name no amount [S6]; the state subsidy and its 2026 redesign [S2,S4], which pay households; and the renovation-pass grant, which pays for an accredited specialist's assessment, not installer software [S5]. None of the three grants names installers as eligible, so there is no public-money lift. S8's note, which said it backs no score, gained a rescore line. Body: Why now gained a bullet saying none of its dates is a legal deadline for the installers [S4,S5]. The two links to the section now named Market gap carry that name. Same result as the worksheet.

2026-09-21 · evidence audit — Weekly match over the week's energy signals. Appended one foreign comparable: a San Francisco company in Y Combinator's Winter 2023 batch selling solar and energy contractors one workflow tool, its page read the same day [S9]. It is a repeat of what this record already says — the same product exists abroad and is funded — and it moves nothing. On the established test it is EARLY: selling since 2021 clears the years, but it names no customer, publishes no count and has raised seed money only, so proof stays 3 on the two German sellers [S1]. Its own page's savings claims are recorded in the source note as the company's claims and are used in no sentence here [S9]. Not linked, and why: a US company selling microgrids in a box sells hardware, not the installer's back office; nothing in the week's haul names a Czech installer, a Czech price or a new Czech vendor. Gap re-checked against the week's signals: no new Czech seller of installer software surfaced, so gap stays 0 on the established Czech vendor already on the ledger, and the record stays watching [S6]. No score moved.
