---
id: p-0001
region: cz
title: 'Czech schools sharing electricity can pay 3 times its price in admin fees'
solution: 'Build billing software that pulls sharing data from the national hub and bills each member, as 1 company already does in Switzerland.'
brief: 'One Czech energy community charges schools and care homes an admin fee 3 times the electricity price [S6,S7,S18]. It covers billing, but also accounting and legal advice [S18].'
good_for: 'Someone who builds software and would like to work with energy communities.'
price_search: 'Each energy community''s published price list (ceník), and the state contracts register full-text for "Smlouva o zajištění sdílení elektřiny" or "správa sdílení", for what a member pays per shared kWh.'
category: energy
geo: CZ-national
score: 9
scores:
  proof: 3
  money: 2
  urgency: 1
  demand: 2
  gap: 1
status: candidate
entry:
  level: hard
  buyer: public
  permission: none
  incumbents: open
  integration: national-system
  money: bootstrap
  why: 'Easier: no licence is needed, members already pay a community an admin fee for this work, and no Czech rival names a customer yet. Harder: the buyers so far are public bodies, so a first contract is a public purchase, and the software has to read and settle from the national electricity data hub.'
comps:
- name: Exnaton
  url: https://exnaton.com/
  geo: CH
  since: 2020
  traction: '$10M Series A, Oct 2025 (The SaaS News); 50+ utility customers incl. TotalEnergies,
    eprimo, Bayernwerk (tech.eu, 2025)'
  signal: de-exnaton
  markets: [DE, AT, DK, SE, NO, FI]
- name: eFriends Energy
  url: https://www.efriends.at/
  geo: AT
  since: 2015
  traction: '500+ household P2P sharing community, Austria''s largest (Trending Topics, 2020);
    investors Wienerberger, VERBUND X Ventures, RWA, Rockstart (2024 round undisclosed)'
- name: OurPower
  url: https://www.ourpower.coop/
  geo: AT
  since: 2018
  traction: '850 co-op members, 400+ electricity producers selling on its marketplace (ourpower.coop,
    2026)'
- name: Pionierkraft
  url: https://pionierkraft.de/
  geo: DE
  since: 2019
  traction: 'High-seven-figure EUR Series A, Oct 2024 (First Imagine!, company release); HW+SW
    energy sharing for small multi-family buildings'
locals:
- name: Enerio
  url: https://enerio.cz/
  since: 2024
  competes: direct
  maturity: early
  evidence: 'Sells energy-community administration: automated member onboarding, invoicing and
    full integration with the national electricity data hub (EDC). Czech electricity sharing
    over that hub opened only in 2024, and the site still shows placeholder testimonial names
    and empty community counters, so it names nobody it has signed up.'
- name: Softlink CEM
  url: https://www.softlink.cz/
  ico: '27109682'
  since: 2024
  competes: direct
  maturity: early
  evidence: 'Sets up allocation keys and issues invoices for shared electricity; the vendor is a
    Czech metering-software house trading since 2003, but this sharing module belongs to the
    2024 rules. Only marketing copy is published — nobody using it is named, and no public
    contract for the IČO appears in the state contracts register.'
- name: EnerCA (EnerCo Solutions)
  url: https://enerca.cz/
  ico: '19753691'
  since: 2024
  competes: direct
  maturity: early
  evidence: 'Sells allocation-key optimisation, automated data transfer from the national
    electricity data hub and a complete billing solution. EnerCo Solutions, s.r.o. was
    incorporated in September 2023 and the sharing regime it sells into opened in 2024; it
    names no community running on it.'
- name: ENERGOMETR (DEKSOFT)
  url: https://deksoft.eu/
  since: 2024
  competes: direct
  maturity: early
  evidence: 'A community-energy module inside the DEKSOFT metering product that issues invoices
    for shared energy off production and consumption data from the national electricity data
    hub. The module belongs to the 2024 sharing regime and no buyer of it is named anywhere.'
- name: CANCOM Czech Republic
  url: https://www.cancom.cz/
  ico: '06343970'
  since: 2024
  competes: direct
  maturity: early
  evidence: 'End-to-end community management — onboarding, contracts, sharing data, settlement
    and billing — from a systems house incorporated in 2017. The community-energy offer itself
    belongs to the 2024 sharing regime, and it names no community running on it.'
- name: Delta Green
  url: https://www.deltagreen.cz/
  competes: adjacent
  maturity: early
  evidence: 'Sells spot-price electricity supply and household flexibility aggregation — a
    virtual power plant that pays households for the flexibility of their solar, batteries,
    heat pumps and EVs. That is generation and grid services, not a community''s books: no
    member billing, no allocation keys and no settlement appears on its site or in its press.
    It raised EUR 2M in October 2025 after EUR 2.2M in May 2024 and publishes no launch year;
    worth watching, because vyhláška 132/2026 Sb. opens the data hub to flexibility and storage
    from August 2026, which makes it the most plausible local entrant into this niche.'
sources:
- type: arbitrage
  name: "Exnaton"
  gist: "the closest foreign template"
  why: "ETH Zurich spin-off selling white-label energy-community billing and settlement to utilities across DACH and the Nordics — the closest template for this product."
  url: https://exnaton.com/
  note: 'de-exnaton: DACH/Nordics-proven white-label billing/settlement SaaS for energy communities
    (ETH spin-off, used by utilities); Austrian peers eFriends/OurPower validate the category
    in a CEE-adjacent market. Absence check 2026-08-13 found no CZ equivalent.'
  date: '2026-08-13'
  signal: de-exnaton
- type: complaint
  name: "Hospodářské noviny — value lost in sharing"
  gist: "the half-the-value claim"
  why: "Reporting that Czech communities lose up to roughly half the value of shared electricity to bad allocation and settlement."
  url: https://exnaton.com/
  note: 'HN (2025) report cited in de-exnaton: CZ communities reportedly lose up to ~50% of
    shared electricity value to bad allocation/settlement; municipalities founding společenství
    have zero software.'
  date: '2026-08-13'
- type: gap-check
  name: "First Czech market scan"
  gist: "the superseded first sweep"
  why: "An early sweep that returned only EDC itself, ministry guidance and ASITIS-style consultancies — superseded by the five Czech vendors found later and listed below."
  url: https://exnaton.com/
  note: 'Absence check 2026-08-13: searches return only EDC itself, ministry PR and ASITIS
    (consulting/services); no dedicated CZ community-energy billing/settlement SaaS.'
  date: '2026-08-13'
- type: round
  name: "Pstryk"
  gist: "the Polish €7M round"
  why: "Polish dynamic-pricing app for households and SMEs, €7M Series A in July 2026 — CEE investors are funding consumer and SME energy software next door."
  url: https://www.vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-july-2026
  note: 'round-pstryk: Pstryk (PL, dynamic electricity pricing for households/SMEs) raised
    EUR 7M Series A led by Future Energy Ventures, Jul 2026 — CEE investor appetite for consumer/SME
    energy tooling.'
  date: '2026-08-04'
  signal: round-pstryk
- type: tender
  name: "TED — Petrovice u Karviné (~€278k)"
  gist: "the €278k municipal award"
  why: "A municipality awarded a design-and-build community-energy project in June 2026 — public budgets are paying for the generation that later needs settling."
  url: https://ted.europa.eu/en/notice/-/detail/385664-2026
  note: 'ted-385664-2026: obec Petrovice u Karviné awarded ~€278k design-and-build for ''Komunitní
    energetika'' (TED, closed award, Jun 2026) — municipal budgets are flowing into community-energy
    delivery; each completed build becomes a settlement/billing customer. Money scored 1 at
    creation; upgraded to 2 on 2026-08-13 by the sharing-series receipts below.'
  date: '2026-06-05'
  signal: ted-385664-2026
- type: contract
  name: "Registr smluv — Dům seniorů Františkov (960,000 CZK)"
  gist: "the 960,000 CZK contract"
  why: "A Liberec care home's open-ended sharing contract č. 58 with Energetické společenství Liberec, valued at 960,000 CZK: it pays for the shared electricity, owed to the producers, plus a separate administration fee, both set by the community's price list."
  url: https://smlouvy.gov.cz/smlouva/38899662
  note: 'hlidac-38899662: Dům seniorů Františkov (Liberec) signed ''Smlouva o zajištění sdílení
    elektřiny č. 58'' (~1.0M CZK, registr smluv) — public institutions are paying for sharing
    services and the provider''s numbering implies a contract series; 37 komunitní-energetika
    contracts in registr smluv since Jun 2026.'
  date: '2026-07-01'
  signal: hlidac-38899662
- type: contract
  name: "Registr smluv — Liberec schools sharing series"
  gist: "fourteen near-identical contracts"
  why: "One community enrolled about fourteen Liberec schools and kindergartens on near-identical sharing contracts in two months, numbered up to č. 58 — recurring multi-organisation spend, not one-off projects."
  url: https://smlouvy.gov.cz/smlouva/38667544
  note: 'hlidac-38667544: MŠ Dětská, Liberec signed sharing contract č. 32 with Energetické
    společenství Liberec (Jun 2026) — representative of ~14 near-identical contracts by Liberec
    school/kindergarten organisations in Jun–Jul 2026, with series numbering observed up to
    č. 58. One community is systematically enrolling every city organisation: sharing administration
    is recurring, multi-org service spend, not one-off projects. Money upgraded to 2 (recurring
    annual spend, receipted across the series plus the 37-contract registr-smluv wave).'
  date: '2026-06-29'
  signal: hlidac-38667544
- type: contract
  name: "Registr smluv — sdílEjme / Sonnentor"
  gist: "the first private participant"
  why: "A public regional agency administers sharing for Sonnentor inside the sdílEjme community — the first private company in the evidence, with a public agency doing the paperwork."
  url: https://smlouvy.gov.cz/smlouva/38760740
  note: 'hlidac-38760740: Jihomoravská energetická agentura signed a sharing-administration
    contract covering Sonnentor within the sdílEjme community (Jun 2026) — the first private-company
    participant in the evidence bucket, and a public regional agency acting as the administration-service
    provider. Extends who-pays beyond public institutions; also names JMEA on the services
    (not SaaS) side of the gap.'
  date: '2026-06-29'
  signal: hlidac-38760740
- type: gap-check
  name: "Delta Green"
  gist: "the adjacent local supplier"
  why: "Prague spot-price supplier and household flexibility aggregator, ~€4.2M raised — no community administration or member billing on its site, but the most plausible local entrant to watch."
  url: https://www.deltagreen.cz/
  note: 'Incumbent re-check 2026-08-14 (round-delta-green flag): Delta Green (Prague, EUR 2M
    Oct 2025 after EUR 2.2M May 2024) is a spot-price electricity supplier and household flexibility
    aggregator — grid-balancing VPP. Site and
    press show no sdílení elektřiny product: no community administration, member billing, allocation
    keys or EDC settlement. Adjacent niche, gap 2 stands. Named because vyhláška 132/2026 Sb. adds
    EDC rules for evaluating technical flexibility and storage from Aug 2026 — Delta Green is the most plausible CZ
    entrant into this niche and the adjacency should be re-checked each cycle.'
  date: '2026-08-14'
  signal: round-delta-green
- type: contract
  name: "Registr smluv — Nemocnice Pardubického kraje"
  gist: "the 200k CZK membership order"
  why: "A regional hospital group's order to Energetické společenství východních Čech, headed as its membership contribution, for an annual volume of 200,000 CZK before VAT — a hospital joining a community in a second region; the order names neither electricity nor administration."
  url: https://smlouvy.gov.cz/smlouva/38404378
  note: 'hlidac-38404378: Nemocnice Pardubického kraje contracted Energetické společenství
    východních Čech for electricity sharing (~200k CZK vč. DPH, registr smluv, Jun 2026) —
    the Liberec enrolment pattern repeating in a second region and a healthcare buyer type,
    extending the sharing-contract wave beyond schools.'
  date: '2026-06-16'
  signal: hlidac-38404378
- type: subsidy
  name: "Modernizační fond — KOMUNERG 1/2025"
  gist: "the 1bn CZK fund"
  why: "1bn CZK (~€40.8M) for energy communities and municipalities building shared generation, open until 31 Dec 2027 — it funds the buyers, and every funded build needs settling afterwards."
  url: https://sfzp.gov.cz/dotace-a-pujcky/modernizacni-fond/vyzvy/
  note: 'dotace-mf-komunerg-1-energeticka-spolecenstvi: Modernizační fond KOMUNERG 1/2025 —
    1bn CZK (~€40.8M) for energy communities, municipalities and their associations building
    shared renewable generation, applications open until 31.12.2027; directly funds community
    PV, grid connection and administration after the energy-community legislation.'
  date: '2027-12-31'
  signal: dotace-mf-komunerg-1-energeticka-spolecenstvi
- type: regulation
  name: "ERÚ vyhláška 132/2026 Sb."
  gist: "the September 2026 rule change"
  why: "From 1 September 2026 the three-ORP territorial limit on energy communities is gone and sharing allocation extends to groups of up to 100 supply points — bigger groups, harder settlement."
  url: https://e-sbirka.gov.cz/sb/2026/132
  note: 'reg-eru-sdileni-132-2026: ERÚ vyhláška 132/2026 Sb. amends the electricity market
    rules — the 3-ORP territorial restriction on energy communities is removed, the five-round
    sharing allocation extends to groups of up to 100 EANs, and EDC gains rules for evaluating
    technical flexibility and storage; configurable in EDC from 2026-08-01, applied in practice
    from 2026-09-01. Appended by the 2026-08-20 evidence audit as the real instrument behind
    the flexibility/EDC claim this record previously attributed to an invented ''Lex OZE III''.
    The signal also names settlement SaaS as a created market.'
  date: '2026-09-01'
  signal: reg-eru-sdileni-132-2026
- type: gap-check
  name: "Enerio and four Czech rivals"
  gist: "the five Czech vendors"
  why: "Enerio sells automated member onboarding, invoicing and full EDC integration — one of five Czech products (with Softlink CEM, EnerCA, ENERGOMETR and CANCOM) already holding this position."
  url: https://enerio.cz/
  note: 'Gap re-check 2026-08-20: looked for Czech software that runs energy-community member
    administration, allocation keys and member billing over EDC data. The position is NOT empty
    — five CZ products sell exactly that. Enerio: "Automatizovaný onboarding členů", "Automatizace
    fakturace", "Plná integrace s EDC a soulad s českou legislativou". Softlink CEM: "Automatické
    rozdělení vyrobené elektřiny mezi členy na základě smluvených podílů... nastavení alokačních
    klíčů" and "Generování faktur za sdílenou elektřinu". EnerCA (EnerCo Solutions): "Optimalizace
    alokačních klíčů", "plně automatizovaný přenos dat z EDC", "kompletní fakturační řešení".
    ENERGOMETR (DEKSOFT): a "specializovaný modul pro komunitní energetiku" whose "nástroj pro
    fakturaci" issues invoices "za odběr nebo dodávku sdílené energie", reading production and
    consumption from EDC. CANCOM Czech Republic: end-to-end community management covering
    onboarding, contracts, sharing data, settlement and billing. Softlink is already named as
    a CZ incumbent elsewhere in this register (p-0026), so the 2026-08-13 absence check missed
    a player the register itself had on file. Local players named: gap 2 -> 0 and status moves
    to watching per the de-rank rule.'
  date: '2026-08-20'
  queries:
    - "software pro energetická společenství sdílení elektřiny rozúčtování členů"
    - "komunitní energetika software správa členů alokační klíč EDC vyúčtování"
    - "Czech energy community electricity sharing billing settlement software vendor EDC"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: contract
  name: "Energetické společenství Liberec — the schools wave"
  gist: "the Liberec schools wave"
  why: "Liberec schools and kindergartens signed a run of electricity-sharing contracts in summer 2026 — municipal energy communities are operating practice now, each needing allocation and settlement."
  url: https://smlouvy.gov.cz/smlouva/38642412
  note: 'hlidac-36312136 plus six sibling contracts from the same run (hlidac-36314220,
    -36334512, -36352144, -36360948, -36364860, -36394204): Liberec schools and kindergartens
    joining Energetické společenství Liberec under the LEX OZE II framework, Jun–Jul 2026.
    Corroborates operating municipal communities as buyers; backs no score point — money and
    demand already carry receipts.'
  date: '2026-06-26'
  signal: hlidac-36312136
  dims: []
- type: tender
  name: "TED — Elektroenergetické datové centrum, a new IT system (~€70M)"
  gist: "the data hub itself is being rebuilt"
  why: "EDC — the national electricity data hub every vendor here integrates with — tendered
    roughly €70M for a new IT system in August 2026. The notice names no function, so this is
    recorded as infrastructure context, not as a competing product."
  url: https://ted.europa.eu/en/notice/-/detail/587970-2026
  note: 'ted-587970-2026: Elektroenergetické datové centrum, a.s. [21020264] — the entity behind
    EDC — tendered design and implementation of a new IT system and related services, ~EUR 70M
    (~1.75bn CZK), published 26 Aug 2026. The notice gives no functional detail, so this is
    recorded as scale-of-investment context for the infrastructure this record''s vendors sit on
    top of, not as evidence of a competing feature. Backs no score point.'
  date: '2026-08-26'
  signal: ted-587970-2026
  dims: []
- type: contract
  url: https://smlouvy.gov.cz/smlouva/38899662
  name: "Dům seniorů Františkov — the sharing contract"
  gist: "electricity plus administration"
  why: "The same care-home contract read clause by clause: its 960,000 CZK pays for the shared electricity and the community's administration fee together, and nothing on it splits the two."
  note: 'Price receipt drawn from the contract already on this ledger (hlidac-38899662,
    registr smluv, Smlouva o zajištění sdílení elektřiny č. 58, ~1.0M CZK). The register
    entry states a contract value and no annual term, so the unit is one-off rather than
    per-year. dims omitted deliberately: this backs no score and moves nothing.'
  date: '2026-07-01'
  dims: []
- type: contract
  url: https://smlouvy.gov.cz/smlouva/38404378
  name: "Nemocnice Pardubického kraje — the membership order"
  gist: "the membership-contribution order"
  why: "The same hospital-group document read in full: a one-page order for 200,000 CZK before VAT, headed as a membership contribution for an annual volume, naming no service it buys."
  note: 'Price receipt drawn from the contract already on this ledger (hlidac-38404378,
    registr smluv, ~200k CZK vč. DPH, Jun 2026). No annual term is stated in the register
    entry, so the unit is one-off. dims omitted: backs no score.'
  date: '2026-06-16'
  dims: []
- type: contract
  url: https://energetika.liberec.cz/uploads/Vnit%C5%99n%C3%AD%20p%C5%99edpis%20%C4%8D.%204_Cen%C3%ADk.pdf
  name: "Energetické společenství Liberec — price list for 2026"
  gist: "the administration fee per kWh"
  why: "The Liberec community's published 2026 price list, part of every member's sharing contract: members pay an administration fee of 1.516 CZK per shared kWh, covering the data-hub paperwork, data processing and billing but also accounting, legal advice and a reserve, and 0.484 CZK per kWh for the electricity, passed to the producers."
  note: 'Vnitřní předpis č. 4/2026, Ceník pro rok 2026, Energetické společenství Liberec, z.s.
    (IČO 22448225): approved by the Výbor 11 May 2026, effective 1 Jul 2026, listed 14 Jul 2026
    under energetika.liberec.cz/energeticke-spolecenstvi/dokumenty; PDF read 2026-09-16. Čl. II:
    Poplatek za administraci 1,516 Kč/kWh of shared electricity consumed by the odebírající člen,
    the same for every supply point; the community is not a VAT payer, so it is a final price.
    Purpose per II.1: zajištění administrace v EDC, zpracování dat, provádění vyúčtování; per I.6
    the fee and contributions also cover operating, accounting and legal costs, running an interface
    for EDC data and a reserve for technical and software infrastructure. Čl. IV: Cena sdílení
    0,484 Kč/kWh, owed to the producing member. Separate předpis č. 3/2026: quarterly membership
    contribution 100 Kč per EAN. The Františkov contract č. 58 names this Ceník an integral part
    (clause 1.5). A real price for the administration service, but NOT written as type: price,
    because the price-receipt unit list has no per-kWh unit. dims empty: backs no score.'
  date: '2026-07-01'
  dims: []
created: '2026-08-13'
updated: '2026-09-04'
---

Czech energy communities must bill each member for shared electricity themselves, because the national data hub only moves the data [S1,S6].

- Up to half of shared electricity's value is reportedly lost to bad settlement [S2].
- Schools, a care home and a hospital group joined communities in mid-2026 [S6,S7,S10].
- 37 community-energy contracts have entered the state contracts register since June 2026 [S6].

The hub is called EDC (Elektroenergetické datové centrum, Czech for electricity data centre). It moves data between market participants, and it does no member administration, member billing or optimisation [S1]. It divides the shared electricity between connections itself [S12]. The rest is the community's work:

- It signs up the members and keeps their allocation keys, the shares that say who gets what [S1,S13].
- It bills each member. In the one contract read in full, the community sends every member an invoice each quarter, from the hub's data, and does not say how it makes them [S6].
- It loses value when that work goes wrong. Hospodářské noviny, a Czech business daily, reported in 2025 that communities lose up to half the value of shared electricity to bad allocation and settlement [S2].

The members' contracts are under [Willing to pay](#willing-to-pay).

Existing non-solutions: Five young Czech firms already sell community billing over the national data hub, and none names a customer [S13].

- All five sell member sign-up, allocation keys and invoicing from the hub's data [S13].
- All five started selling it in 2024, when sharing over the hub opened [S13].
- None publishes a customer, a public contract or a funding round [S13].

Everything else on offer is a service, not software:

- The hub itself exchanges data and bills no members [S1,S3].
- A first market scan in August 2026 found only the hub, ministry guidance and consultancies such as ASITIS — services, not software. The five firms turned up in a later Czech-language search [S3,S13].
- The South Moravian energy agency, a public regional agency, administers sharing for Sonnentor, a private firm in the sdílEjme community [S8]. Their three-party contract states no value [S8].
- A Prague electricity supplier pays households for the flexibility of their solar panels, batteries, heat pumps and electric cars, and bills no community members [S9]. It is the likeliest local entrant, because the new hub rules add flexibility and storage [S9,S12].

Why now: Since July 2026, schools in one Czech city pay an admin fee three times the price of their shared electricity [S7,S18].

- The fee covers accounting, legal advice and a reserve, not just billing [S18].
- One community signed about 14 schools in two months, and bills each quarterly [S6,S7].
- Groups can now hold up to 100 connections, so more members need bills [S12].

The dates behind this:

- In August 2024 sharing over the national data hub opened, under Lex OZE II — the law that made energy communities legal [S1].
- On 11 May 2026 the Liberec community's committee approved its 2026 price list, which took effect on 1 July 2026 [S18].
- On 1 August 2026 the hub could be set up for new sharing rules, which also add rules for flexibility and storage [S12].
- On 1 September 2026 those rules applied: a sharing group can hold up to 100 supply points, and a community is no longer limited to three administrative districts [S12].
- Until 31 December 2027 the state fund for energy communities takes applications, and every community it funds will need its members billed [S11].

Who pays: Members already pay for this work: one community charges an admin fee on every shared kWh, set in a published price list [S18].

- 1.516 CZK per shared kWh goes to administration, 0.484 CZK to producers [S18].
- 960,000 CZK is one care home's open-ended contract, for electricity and fee together [S6].
- 200,000 CZK a year is a hospital group's membership contribution to a community [S10].

The price list is Energetické společenství Liberec's, for 2026 [S18].

- The fee pays for the hub paperwork, data processing and billing. It also pays for running costs, accounting, legal advice and a reserve for software and equipment [S18].
- The fee is the same for every supply point. The community is not a VAT payer, so it is the final price [S18].
- Each supply point also pays a membership contribution of 100 CZK a quarter [S18].

The contracts behind the other two figures:

- The care home is Dům seniorů Františkov in Liberec. Its contract, č. 58, pays for the shared electricity, owed to the producers, plus the admin fee, and names the price list as part of it [S6,S16]. It states no volume, so how the 960,000 CZK splits between the two is unknown [S16].
- About 14 Liberec schools and kindergartens signed near-identical contracts with the same community in June and July 2026, numbered up to č. 58 [S7,S14].
- The hospital group is Nemocnice Pardubického kraje. Its one-page order, in June 2026, went to Energetické společenství východních Čech, a community in a second region [S10,S17]. The 200,000 CZK is before VAT, and the order names neither electricity nor administration [S17].

Public money is there too. KOMUNERG 1/2025, a call of the state's Modernisation Fund, holds 1bn CZK, about €40.8M, for communities, towns and their associations building shared renewable generation [S11]. It also pays for the grid connection and for administration [S11]. Its closing date is under [Why now](#why-now).

The software's likely buyers are the communities and the towns that found them [S11]. Abroad, it is sold to energy suppliers, energy service firms and grid operators, which offer it to communities under their own name [S1].

Solved elsewhere: A Swiss company sells this billing to utilities across German-speaking Europe and the Nordics, and two Austrian firms run sharing communities [S1].

The Swiss company is a spin-off of ETH Zurich — a Swiss university. It sells white-label billing and settlement, which a utility offers under its own name [S1]. Its site names energy suppliers, energy service firms, grid operators and large property firms as the buyers it is for [S1].

The two Austrian firms run sharing communities under the same EU renewables directive [S1].

Next door, Poland's Pstryk, which sells dynamic electricity pricing to households and small firms, raised a €7M Series A led by Future Energy Ventures in July 2026 [S4]. Investors in Central Europe are funding energy software for households and small firms [S4].

## First moves

1. Call Energetické společenství Liberec, the community that signed up the city's schools this summer, and ask how it bills its members today. Ask who works out each member's share, how the quarterly invoices get made, and what the admin fee pays for; its contracts and price list are under [Willing to pay](#willing-to-pay). That routine is your product spec.
2. Next, call the South Moravian energy agency, which already runs sharing for a private firm in another community. It sells that work as a service, not as software; see [Competition](#competition). Abroad, energy service firms like it buy white-label billing software and offer it under their own name; see [Validated abroad](#validated-abroad). Ask how it does the work today, and whether it would run its communities on your software.
3. Recompute one community's month of sharing from the hub's data before building anything else. Work out who should have got what and who owes what, and show the gap in crowns; the loss the press reported is under [The opportunity](#opportunity). This also tests the risky assumption: that the hub's data is enough for an outsider to bill on.
4. Price your software below the admin fee members already pay, and show which part of that fee it replaces. The fee also pays for accounting, legal advice and a reserve, so software replaces only part of it; see [Willing to pay](#willing-to-pay). Several young Czech firms already sell this billing without a named customer, and a local flexibility supplier could join them; see [Competition](#competition). So win on a named first customer and a recomputed month, not on features.
5. Point new communities at the state fund that pays for their build and their administration. It pays communities, towns and their associations to build shared generation, and it stays open until the end of next year; see [Willing to pay](#willing-to-pay) and [Why now](#why-now). Every community it funds will need its members billed.

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it. Same date, separate pass, merged here: First moves rewritten in plain language (owner: "full of fluff and jargon — make the ideas simple"); jargon like "settlement-reconciliation wedge" and "documented willingness-to-pay" replaced with plain sentences. Every [Sn] marker, ledger link and named competitor kept; no claim added or dropped; scores untouched.

2026-08-13 · money re-score — The registr smluv shows the spend is structural, not anecdotal [S6,S7]: the Liberec community alone signed ~14 near-identical sharing contracts with city schools and kindergartens in June–July 2026 (series numbering to č. 58) [S7], Pardubice-region institutions follow the same pattern [S10], and Sonnentor became the first private company in the bucket, administered by a public energy agency [S8]. Recurring, multi-organisation service spend on sharing administration is receipted: money 1 → 2, and the record entered PRIME territory.

2026-08-14 · incumbent re-check — Delta Green (Prague, ~€4.2M raised across 2024–25) was flagged by the funded-CZ sweep as a possible occupier and verified adjacent rather than occupying: it sells spot-price supply and household flexibility aggregation, with no community-sharing administration, member billing, allocation-key or EDC-settlement product on its site or in press [S9]. It was named because vyhláška 132/2026 Sb. adds EDC rules for evaluating technical flexibility and storage, configurable from August 2026 [S12], which made it the most credible potential entrant. That framing was wrong about where the competition was — see below.

2026-08-20 · de-rank and evidence audit — Three blocks recorded on this date, merged here; the de-rank was written down twice and is stated once. The central absence claim was false: Czech-language search found five CZ vendors selling community-energy administration with allocation keys, member billing and EDC integration — Enerio, Softlink CEM, EnerCA, ENERGOMETR (DEKSOFT) and CANCOM [S13] — so gap moved 2 → 0, score 10 → 8, status candidate → watching per the SPEC §4 de-rank rule. Three general failure modes, recorded because they recur: the 2026-08-13 check and the 2026-08-14 Delta Green re-check both cited a foreign company's page (exnaton.com) or a funded-company sweep as the receipt for a Czech absence, which is no evidence at all; the incumbent search was aimed at funded startups, and none of the five appears anywhere in this register's 6,181-signal corpus because they are bootstrapped SMB software companies no funding feed will ever surface; and Softlink was already named as a Czech incumbent on p-0026, so the register held the disproof of its own claim. Also cut: the invented Delta Green product names "Proteus" and "DELTA SPOT/FLEX" (zero hits across all 6,181 signals; round-delta-green carries no product breakdown), from the body and the S9 note; the Exnaton traction parenthetical "$10M Series A, 50+ utility customers" in First moves #2, comps-ledger evidence that cannot back a body claim and that "Where it works" already states; and "Lex OZE III", which exists nowhere in the corpus — the substance it carried is real and is now cited to vyhláška 132/2026 Sb., appended as [S12]. The title carried the same disproved absence, "and have no software to run member billing", and was cut to what still stands: it renders on the register, the category pages and this page, so leaving it would have contradicted this record's own ledger in its most-read line. Untouched: the demand and money receipts [S2,S6,S7,S8,S10]. The open question is no longer whether a product exists but whether these vendors reach the long tail of small komunity — a competitive question, not an absence.

2026-08-24 · evidence audit — The lead still asserted that municipalities founding společenství "have no software at all for the task" — the same absence the 2026-08-20 de-rank disproved by naming five CZ vendors [S13]. Cut: a lead cannot assert what the record's own ledger refutes. The de-rank receipt was re-verified live on this date: enerio.cz still sells automated member onboarding, invoicing automation and EDC integration [S13]. Nothing else changed; scores untouched.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "DSO-adjacent service firms" now reads "the service firms around the regional grid operators". Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. Local players moved out of gap-check prose into a structured `locals[]` ledger — Enerio, Softlink CEM, EnerCA, ENERGOMETR (DEKSOFT) and CANCOM, all five marked early [S13]. None passes the established test: Czech sharing over EDC opened only in 2024, so none has three years of selling behind it, and none publishes a customer, a public buyer, a round or a state listing — enerio.cz still runs placeholder testimonial names and empty counters. An early local player does not close a space, so `scores.gap` moves 0 → 1: contested, not taken. `scores.proof` holds at 3 — Exnaton, eFriends, OurPower and Pionierkraft all pass the test, across CH, AT and DE, two of them CEE-adjacent. `score` 8 → 9. The 2026-08-20 de-rank is not withdrawn; the five vendors are real and still named in the body. What changed is that a crowded young field is now scored as contested rather than closed. Fifth pass this date, merged here: the ledger's `status:` field was split into `competes:` (direct or adjacent) and `maturity:` (established or early), so it can now say the thing one field could not — that a real player nearby does not sell this record's product. All five vendors convert to `competes: direct` keeping the maturity they already carried: each sells community administration with allocation keys, member invoicing and EDC settlement to communities, which is this record's product to this record's buyer. **Delta Green** joins the ledger as `competes: adjacent`, reversing the 2026-08-14 decision above to keep it out: it sells spot-price supply and household flexibility aggregation and no sharing administration [S9], and under the split that is intelligence a builder needs rather than a name to drop. It publishes no launch year and neither of its rounds carries a stage letter, so it is early on the test's own terms. `scores.gap` stays 1 — an adjacent player never moves the score, and the direct field is still five young vendors. Deliberately NOT added, and the reasons are recorded so the next pass does not relitigate them: **EDC** is state data infrastructure rather than a vendor; **JMEA** is named in First moves #2 as a target customer, so filing it as competition would mislead the reader the ledger exists to inform; and **ASITIS** has no receipt on file beyond the fact that a 2026-08-13 search returned it [S3], with nothing recorded about what it sells. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed.

2026-09-02 · plain-language pass — Glossed at first use: EDC, Lex OZE II, Softlink CEM, CANCOM. Replaced with plain words: DACH, ETH, RED II, CEE, SME, ASITIS and JMEA. Argument 336 → 299 words, every figure and named vendor kept, with two on-file receipts now cited in the body: the 1 September 2026 rule change [S12] and the ~200k CZK hospital contract [S10]. First moves rewritten verbs-first; a gist added to all 14 sources. No score, status, note or marker touched.

2026-09-04 · price receipt — The two sharing-administration contracts already on file are now also recorded as prices: about 1.0M CZK at a Liberec care home [S16] and about 200,000 CZK at a Pardubice-region hospital group [S17]. Same urls, same dates and same figures as the contracts they come from. No score, status, note or marker touched.

2026-09-16 · headline copy — The headline was rewritten for a general builder as three lines under the title: a `brief:` on what is happening and why it matters now, the `solution:` as a call to action, and a new `good_for:` line. New copy, verbatim — title: "Czech energy communities can now share electricity among up to 100 connections"; brief: "Hospitals, schools and care homes already buy shared electricity from these communities [S6,S7,S10]. The state data hub only moves the data, and each community bills every member itself [S1,S6]."; solution: "Build billing software that pulls sharing data from the national hub and bills each member, as companies already do abroad."; good_for: "Software builders who'd like to work with energy data, towns and hospitals.". Previous title, verbatim: "Czech energy communities lose up to half the value of shared electricity to bad allocation and settlement". Previous solution, verbatim: "Settlement software for electricity-sharing communities: recompute each member's share from the national electricity data hub, issue the monthly bills, and show in crowns what bad allocation was costing.". There was no previous brief or good_for. The owner-reviewed draft title, "Czech hospitals and care homes pay up to 1M CZK just to have shared electricity split and billed", was NOT used, because the contract behind the figure says otherwise. Read on 2026-09-16 from the registr smluv entry [S6]: Dům seniorů Františkov's 960,000 CZK contract with Energetické společenství Liberec is open-ended, and the home pays the price of the shared electricity itself, owed to the producers, plus a separate administration fee (clauses 2.2, 2.3 and 3.1), both set by a price list not attached. The 1M CZK is therefore mostly electricity, and no source on file states the administration fee alone. The draft brief's "every member's share is still worked out and billed by hand" was also not used: five Czech vendors sell community billing software [S13], and the one contract read shows the community invoicing each member quarterly from the hub's data without saying how [S6]. What stands is written instead: since 1 September 2026 sharing groups reach 100 connections with no territorial limit [S12]; public hospitals, schools and care homes already buy shared electricity from communities [S6,S7,S10]; the hub does no member billing [S1]; the community bills each member [S6]. The solution says "bills each member" rather than "splits each member's share", because the hub itself runs the allocation between connections [S12]. FLAGGED, NOT CHANGED: the body's Who-pays paragraph, First move 4 and the price receipts [S16,S17] describe the 1.0M CZK and 200k CZK contracts as paying for a sharing-administration service done by hand; the Františkov contract shows the value covers the electricity too, so those lines and receipts need correcting in a separate pass. No score, status, source, note, marker or body sentence changed. Same date, body correction: the flagged lines are corrected. What was wrong, verbatim: Who pays said Dům seniorů Františkov "paid about 1.0M CZK for one sharing-administration contract" [S6] and Nemocnice Pardubického kraje "pays about 200k CZK for the same service" [S10]; First move 4 called both "a manual sharing service" to undercut; the public lines of [S6] and [S10] said "what this work costs today, done by hand" and "contracted a community for electricity sharing"; and [S16] and [S17] recorded both figures as price receipts for administration done by hand. Evidence, read on this date. The Františkov contract č. 58 is valued at 960,000 CZK including VAT, is open-ended, and charges the shared electricity, owed to the producers, plus a separate administration fee, both by the community's price list (clauses 1.5, 2.2, 2.3, 3.1 and 4.1) [S6]. That price list is published: Energetické společenství Liberec's Ceník for 2026, effective 1 July 2026, sets the administration fee at 1.516 CZK per shared kWh, for data-hub administration, data processing and billing but also accounting, legal advice and a reserve, and the electricity at 0.484 CZK per kWh [S18]. The earlier sentence of this entry, "The 1M CZK is therefore mostly electricity, and no source on file states the administration fee alone", is therefore withdrawn on both halves: per kWh the fee is about three times the electricity, and the fee is now on file. What is still unknown is the crown split of the 960,000 CZK, since no volume is stated. The Pardubice document [S10] is a one-page order headed "Členský příspěvek ESVČ", a membership contribution to Energetické společenství východních Čech, with the line "Roční objem" (annual volume) at 200,000 CZK before VAT; it names neither electricity nor administration, so "the same service" had no receipt. Changed: the three Who-pays sentences after the dek and First move 4 now state only those facts; the name, gist and why of [S6] and [S10] rewritten; [S16] and [S17] converted from type price to type contract, their payer, amount, unit and basis removed and dims set empty so they still back no score, notes left as written; the price list appended as [S18], backing no score. It prices the very administration a builder would automate, but the price-receipt unit list has no per-kWh unit, so it is not written as a receipt, and the page now carries none. Scores untouched, checked: money 2 needs recurring annual public spend or an open grant of about 5M CZK or more; the open-ended, quarterly-invoiced contracts [S6,S7] are still recurring public spend near the problem whatever they buy, and KOMUNERG's 1bn CZK, open until 31 December 2027 [S11], meets the rung by itself. What falls is only the 2026-08-13 wording that this spend buys sharing administration. FLAGGED, NOT CHANGED: the brief cites [S10] for hospitals buying shared electricity, which a membership order does not show. The updated date is not moved: only these sources were re-read. Same date, pain-point pass: the owner's new rule, that each headline names who is hurting and how, in plain words. Before, verbatim — title: "Czech energy communities can now share electricity among up to 100 connections"; brief: "Hospitals, schools and care homes already buy shared electricity from these communities [S6,S7,S10]. The state data hub only moves the data, and each community bills every member itself [S1,S6].". After, verbatim — title: "Czech schools sharing electricity can pay 3 times its price in admin fees"; brief: "One Czech energy community charges schools and care homes an admin fee 3 times the electricity price [S6,S7,S18]. It covers billing, but also accounting and legal advice [S18].". Why: the old title stated a capacity, not a pain. The pain now on file is the price list [S18]: an administration fee of 1.516 CZK per shared kWh against 0.484 CZK per kWh for the electricity, about 3.1 times, charged to every consuming member at the same rate. Its members include the schools and kindergartens of the contract series [S7] and the care home whose contract names the price list as an integral part [S6]. Kept honest in three ways: it is ONE community's price list, so the headline says "can pay" and the brief says "One Czech energy community" rather than stating it of all communities; the fee is not called a billing cost, because the price list also charges it for accounting, legal advice and a reserve, and the brief names accounting and legal advice beside billing; and no crown total is given, because the split of the 960,000 CZK contract is still unknown. The flagged [S10] claim is resolved: the old brief cited [S10] for hospitals buying shared electricity, but [S10] is an order headed as a membership contribution that names neither electricity nor administration, so hospitals and [S10] are out of the brief. The second old sentence, on the data hub moving data only, was dropped for length, not for being wrong; the body still carries it [S1]. Solution and good_for unchanged: billing software that pulls from the national hub automates the data-hub work and billing the fee pays for, and makes no claim about the fee. No score, status, source, note, marker or body sentence changed. Same date, good-for opener (owner: "Good for should always start with a person"): "Software builders who'd like to work with energy data, towns and hospitals." became "Someone who builds software and would like to work with energy communities." — same meaning, person first. Same date, abroad count (owner: fill "do abroad" with "X companies do in Y countries"): solution "…bills each member, as companies already do abroad." became "…bills each member, as 1 company already does in Switzerland." Counted from comps[] only, by what each one sells and not by being on the ledger: Exnaton (comps[0], geo CH), which sells white-label energy-community billing and settlement to utilities [S1]. Excluded: eFriends Energy (comps[1]) and OurPower (comps[2]), because both RUN a sharing community or co-op marketplace for their own members and are not recorded selling billing software to anyone; Pionierkraft (comps[3]), because its traction line records hardware and software for sharing inside multi-family buildings and nothing on member billing. The country is where Exnaton is based, not its markets.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the community, not the hub, billing each member [S1,S6], with the reported loss [S2], the public bodies that joined [S6,S7,S10] and the 37 contracts [S6] as its items, and what the hub does and does not do below them [S1,S12,S13]. Competition opens on the five young Czech vendors [S13] and holds the hub, the first scan with ASITIS, the South Moravian agency and the adjacent flexibility supplier as plain bullets [S1,S3,S8,S9,S12], moved from the old sixth move. Why now opens on the admin fee schools pay since July 2026 [S7,S18], with the dates (August 2024 opening, the price list's approval and start, the hub rules of 1 August and 1 September 2026, the fund's 31 December 2027 close) below its three items [S1,S11,S12,S18]. Willing to pay answers that members already pay, with the per-kWh fee, the care home's contract and the hospital group's order as its items, then what the fee covers, the three contracts read in full and the state fund [S6,S7,S10,S11,S14,S16,S17,S18]. Validated abroad became one answer sentence and three short paragraphs [S1,S4]. Every comps[] and locals[] company (Exnaton, eFriends Energy, OurPower, Enerio, Softlink CEM, EnerCA, ENERGOMETR and DEKSOFT, CANCOM, Delta Green) left the body and the moves and is described by what it does; its name stays in its row. Six moves became five: the old move 6 (expect competition) now lives in Competition and in move 4, the moves lost every [Sn] marker and figure for links to the sections holding them, and move 5's link to the private sources page became a link to Willing to pay. `entry.why` rewritten as "Easier: … Harder: …" with the same gates (no licence, the public buyer, the national data hub). `S2.why` lost "this record's headline claim", which the title no longer carries. `price_search` added, naming where to look and no amount, since the per-kWh fee cannot be written as a price receipt. Added from sources already on file, none of it new evidence: the price list's approval on 11 May 2026, the fee being the same for every supply point and free of VAT, and the 100 CZK quarterly membership contribution per supply point [S18]; the hub's 1 August 2026 set-up date [S12]; the fund also paying for grid connection and administration [S11]; Pstryk's lead investor [S4]; and the Swiss company's own list of the buyers it is for, read on exnaton.ai on this date [S1]. Corrected against the sources rather than against the old sentences: (1) communities "run member administration, allocation keys and settlement by hand [S1]" — no source on file says how communities do the work, five Czech vendors sell software for it [S13], and the one contract read in full shows quarterly invoices from the hub's data without saying how [S6]; it now says the community, not the hub, has to do it [S1,S6]. (2) The South Moravian energy agency "runs sharing by hand" and "as a manual service" [S8] — the contract, read on smlouvy.gov.cz on this date, is a three-party "Smlouva o správě sdílení" between the agency, Sonnentor and sdílEjme z.s. with no value stated, and says nothing of how the work is done; it now "administers sharing", a service rather than software, as the S8 note puts it. (3) Who pays named "municipalities, housing cooperatives, groups of firms" and service firms "which want a white-label product" [S1] — S1 names none of these as Czech buyers and records no Czech firm wanting anything; exnaton.ai lists energy providers, energy service providers, grid operators, electricity suppliers, independent power producers and large real-estate firms as the buyers it is for. It now reads: the likely buyers are the communities and the towns that found them [S11], and abroad the software is sold to energy suppliers, service firms and grid operators [S1]. Housing cooperatives and groups of firms are cut: no source on file names them. (4) Move 2's "Agencies like it are who Exnaton sells its white-label software to [S1]" now says energy service firms abroad buy white-label billing software, which is what the site's buyer list supports. Flagged as inference: that bigger groups mean "more members need bills" rests on the 100-connection limit [S12] and on the community billing each member [S6]; that the schools pay the price list's fee and are billed quarterly rests on their contracts being near-identical to the care home's, which names the price list and quarterly invoices [S6,S7,S18], the same basis as the 2026-09-16 headline; that every community the fund pays for will need its members billed rests on [S11] and [S6]; and move 4's "software replaces only part of" the fee rests on the price list's own account of what the fee covers [S18]. No score, status, entry gate value, source, `sources[]` order, `note:`, title, brief, solution or good_for changed; the record has no `process` block.
