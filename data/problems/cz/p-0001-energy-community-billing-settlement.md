---
id: p-0001
region: cz
title: Czech energy communities lose up to half the value of shared electricity to bad allocation
  and settlement
fix: 'Settlement software for electricity-sharing communities: recompute each member''s
  share from the national electricity data hub, issue the monthly bills, and show in
  crowns what bad allocation was costing.'
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
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'EDC and DSO data integration plus member billing is real engineering, but the buyers
    — communities already paying ~1M CZK for manual sharing administration — are reachable
    without certification or enterprise procurement.'
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
  evidence: 'sells energy-community administration — automated member onboarding, invoicing
    and full EDC integration. Czech electricity sharing over EDC opened only in 2024, so
    nothing here has been on sale for three years; the site''s testimonial block still carries
    placeholder names and its community counters render empty. No limb of the established
    test is on file.'
- name: Softlink CEM
  url: https://www.softlink.cz/
  ico: '27109682'
  since: 2024
  competes: direct
  maturity: early
  evidence: 'allocation-key setup and invoicing for shared electricity, from a Czech
    metering-software house trading since 2003; the sharing module itself belongs to the
    2024 EDC regime. Marketing copy only — no limb of the established test is on file, and no
    public contract for this IČO appears in the Czech contracts register.'
- name: EnerCA (EnerCo Solutions)
  url: https://enerca.cz/
  ico: '19753691'
  since: 2024
  competes: direct
  maturity: early
  evidence: 'allocation-key optimisation, automated EDC data transfer and a complete billing
    solution. EnerCo Solutions, s.r.o. was incorporated in September 2023 and the sharing
    regime it sells into opened in 2024. No limb of the established test is on file.'
- name: ENERGOMETR (DEKSOFT)
  url: https://deksoft.eu/
  since: 2024
  competes: direct
  maturity: early
  evidence: 'a dedicated community-energy module inside the DEKSOFT metering product, issuing
    invoices for shared energy off EDC production and consumption data; the module belongs to
    the 2024 sharing regime. No limb of the established test is on file.'
- name: CANCOM Czech Republic
  url: https://www.cancom.cz/
  ico: '06343970'
  since: 2024
  competes: direct
  maturity: early
  evidence: 'end-to-end community management — onboarding, contracts, sharing data, settlement
    and billing — from a systems house incorporated in 2017; the community-energy offer belongs
    to the 2024 sharing regime. No limb of the established test is on file.'
- name: Delta Green
  url: https://www.deltagreen.cz/
  competes: adjacent
  maturity: early
  evidence: 'sells spot-price electricity supply and household flexibility aggregation — a
    virtual power plant that pays households for the flexibility of their solar, batteries,
    heat pumps and EVs. That is generation and grid services, not a community''s books: no
    member billing, no allocation keys and no EDC settlement appears on its site or in its
    press. It raised EUR 2M in October 2025 after EUR 2.2M in May 2024, neither round carrying
    a stage letter, and it publishes no launch year, so no limb of the established test is on
    file. Worth watching rather than worth discounting: vyhláška 132/2026 Sb. opens EDC rules
    for flexibility and storage from August 2026, which makes it the most plausible local
    entrant into this niche.'
sources:
- type: arbitrage
  name: "Exnaton"
  why: "ETH Zurich spin-off selling white-label energy-community billing and settlement to utilities across DACH and the Nordics — the closest template for this product."
  url: https://exnaton.com/
  note: 'de-exnaton: DACH/Nordics-proven white-label billing/settlement SaaS for energy communities
    (ETH spin-off, used by utilities); Austrian peers eFriends/OurPower validate the category
    in a CEE-adjacent market. Absence check 2026-08-13 found no CZ equivalent.'
  date: '2026-08-13'
  signal: de-exnaton
- type: complaint
  name: "Hospodářské noviny — value lost in sharing"
  why: "The reporting behind this record's headline claim: Czech communities lose up to roughly half the value of shared electricity to bad allocation and settlement."
  url: https://exnaton.com/
  note: 'HN (2025) report cited in de-exnaton: CZ communities reportedly lose up to ~50% of
    shared electricity value to bad allocation/settlement; municipalities founding společenství
    have zero software.'
  date: '2026-08-13'
- type: gap-check
  name: "First Czech market scan"
  why: "An early sweep that returned only EDC itself, ministry guidance and ASITIS-style consultancies — superseded by the five Czech vendors found later and listed below."
  url: https://exnaton.com/
  note: 'Absence check 2026-08-13: searches return only EDC itself, ministry PR and ASITIS
    (consulting/services); no dedicated CZ community-energy billing/settlement SaaS.'
  date: '2026-08-13'
- type: round
  name: "Pstryk"
  why: "Polish dynamic-pricing app for households and SMEs, €7M Series A in July 2026 — CEE investors are funding consumer and SME energy software next door."
  url: https://www.vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-july-2026
  note: 'round-pstryk: Pstryk (PL, dynamic electricity pricing for households/SMEs) raised
    EUR 7M Series A led by Future Energy Ventures, Jul 2026 — CEE investor appetite for consumer/SME
    energy tooling.'
  date: '2026-08-04'
  signal: round-pstryk
- type: tender
  name: "TED — Petrovice u Karviné (~€278k)"
  why: "A municipality awarded a design-and-build community-energy project in June 2026 — public budgets are paying for the generation that later needs settling."
  url: https://ted.europa.eu/en/notice/-/detail/385664-2026
  note: 'ted-385664-2026: obec Petrovice u Karviné awarded ~€278k design-and-build for ''Komunitní
    energetika'' (TED, closed award, Jun 2026) — municipal budgets are flowing into community-energy
    delivery; each completed build becomes a settlement/billing customer. Money scored 1 at
    creation; upgraded to 2 on 2026-08-13 by the sharing-series receipts below.'
  date: '2026-06-05'
  signal: ted-385664-2026
- type: contract
  name: "Registr smluv — Dům seniorů Františkov (~1.0M CZK)"
  why: "A Liberec care home paid about 1.0M CZK for a sharing-administration contract numbered č. 58 — what this work costs today, done by hand."
  url: https://smlouvy.gov.cz/smlouva/38899662
  note: 'hlidac-38899662: Dům seniorů Františkov (Liberec) signed ''Smlouva o zajištění sdílení
    elektřiny č. 58'' (~1.0M CZK, registr smluv) — public institutions are paying for sharing
    services and the provider''s numbering implies a contract series; 37 komunitní-energetika
    contracts in registr smluv since Jun 2026.'
  date: '2026-07-01'
  signal: hlidac-38899662
- type: contract
  name: "Registr smluv — Liberec schools sharing series"
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
  why: "A regional hospital group contracted a community for electricity sharing (~200k CZK) — the Liberec enrolment pattern repeating in a second region and a new buyer type."
  url: https://smlouvy.gov.cz/smlouva/38404378
  note: 'hlidac-38404378: Nemocnice Pardubického kraje contracted Energetické společenství
    východních Čech for electricity sharing (~200k CZK vč. DPH, registr smluv, Jun 2026) —
    the Liberec enrolment pattern repeating in a second region and a healthcare buyer type,
    extending the sharing-contract wave beyond schools.'
  date: '2026-06-16'
  signal: hlidac-38404378
- type: subsidy
  name: "Modernizační fond — KOMUNERG 1/2025"
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
created: '2026-08-13'
updated: '2026-08-25'
---

Czech energy communities (energetická společenství) and groups sharing electricity under Lex OZE II have been legally able to share power via EDC since August 2024, but they run member administration, allocation keys and settlement by hand [S1]. Per Hospodářské noviny reporting on file, communities lose up to roughly half of the value of shared electricity to bad allocation and settlement [S2].

Why now: the regulatory window opened in 2024 (Lex OZE II, EDC data exchange live) and the first cohort of communities is now operating long enough to feel the settlement losses. EDC handles data exchange between market participants but explicitly does not do community administration, member billing or optimization [S1], so the pain sits with the community operator, unaddressed by state infrastructure.

Who pays: community founders (municipalities, housing cooperatives, groups of firms) and — following the Exnaton go-to-market — utilities and the service firms around the regional grid operators, which want a white-label product to offer communities [S1]. The value proposition is direct: recovered settlement value, which the reporting on file quantifies at up to ~50% of shared electricity [S2].

Existing non-solutions: EDC (data exchange only), ministry guidance, and ASITIS-style consultancies selling services rather than product [S3]; Jihomoravská energetická agentura administers sharing for the sdílEjme community as a manual regional service [S8]. The software position is contested rather than empty — Enerio, Softlink CEM, EnerCA, ENERGOMETR and CANCOM all market community administration, allocation keys and member billing over EDC data [S13]. Every one of them is young: sharing over EDC opened only in 2024, and none of the five publishes a customer, a public contract or a funding round [S13]. The earlier finding that no such software existed [S1,S3] searched the wrong places and is superseded.

Solved elsewhere: Exnaton (ETH spin-off) sells exactly this to utilities across DACH and the Nordics; Austrian community-energy players eFriends and OurPower prove tooling demand under EU RED II in a market bordering Czechia [S1]. The July 2026 Pstryk round in Poland shows CEE investors funding adjacent consumer/SME energy software [S4].

## First moves

1. Call **Energetické společenství Liberec** first. It signed ~14 near-identical sharing contracts with Liberec schools and kindergartens in June–July 2026 (series numbering observed up to č. 58) [S7]. Ask them to walk you through how they split the shared electricity and bill the members today — that manual routine is your product spec.
2. Then call **Jihomoravská energetická agentura**. It runs sharing by hand for the sdílEjme community, Sonnentor included [S8]. Agencies like this are exactly who Exnaton sells its white-label software to [S1].
3. First product: check one community's numbers. Take their real EDC sharing data, recompute who should have gotten what and who owes what, and show the money being lost — reporting on file claims up to ~50% of shared-electricity value is lost to bad allocation and settlement [S2]. This also tests the one risky assumption: that EDC's data is enough for an outsider to automate the settlement.
4. Price below what they already pay: Dům seniorů Františkov paid ~1.0M CZK for a manual sharing service [S6]. Software that costs less than that has a buyer on record.
5. Your customers' money: [Modernizační fond KOMUNERG 1/2025](/sources/tenders#dotace-mf-komunerg-1-energeticka-spolecenstvi) gives 1bn CZK (~€40.8M) to communities and municipalities building shared renewable generation, applications open until **2027-12-31** [S11]. Every community it funds will need billing and settlement.
6. Know who you're up against — the field is contested, not empty: **Enerio**, **Softlink CEM**, **EnerCA**, **ENERGOMETR** (DEKSOFT) and **CANCOM** all sell Czech community administration with allocation keys, member invoicing and EDC integration [S13]. Nearby but not competing: **Delta Green** (spot-price supply and flexibility, no sharing administration [S9]), **ASITIS** (consulting, not a product) [S3], **EDC** itself (data exchange only, no member billing) [S1,S3], and **JMEA** (a manual regional service) [S8].

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it. Same date, separate pass, merged here: First moves rewritten in plain language (owner: "full of fluff and jargon — make the ideas simple"); jargon like "settlement-reconciliation wedge" and "documented willingness-to-pay" replaced with plain sentences. Every [Sn] marker, ledger link and named competitor kept; no claim added or dropped; scores untouched.

2026-08-13 · money re-score — The registr smluv shows the spend is structural, not anecdotal [S6,S7]: the Liberec community alone signed ~14 near-identical sharing contracts with city schools and kindergartens in June–July 2026 (series numbering to č. 58) [S7], Pardubice-region institutions follow the same pattern [S10], and Sonnentor became the first private company in the bucket, administered by a public energy agency [S8]. Recurring, multi-organisation service spend on sharing administration is receipted: money 1 → 2, and the record entered PRIME territory.

2026-08-14 · incumbent re-check — Delta Green (Prague, ~€4.2M raised across 2024–25) was flagged by the funded-CZ sweep as a possible occupier and verified adjacent rather than occupying: it sells spot-price supply and household flexibility aggregation, with no community-sharing administration, member billing, allocation-key or EDC-settlement product on its site or in press [S9]. It was named because vyhláška 132/2026 Sb. adds EDC rules for evaluating technical flexibility and storage, configurable from August 2026 [S12], which made it the most credible potential entrant. That framing was wrong about where the competition was — see below.

2026-08-20 · de-rank and evidence audit — Three blocks recorded on this date, merged here; the de-rank was written down twice and is stated once. The central absence claim was false: Czech-language search found five CZ vendors selling community-energy administration with allocation keys, member billing and EDC integration — Enerio, Softlink CEM, EnerCA, ENERGOMETR (DEKSOFT) and CANCOM [S13] — so gap moved 2 → 0, score 10 → 8, status candidate → watching per the SPEC §4 de-rank rule. Three general failure modes, recorded because they recur: the 2026-08-13 check and the 2026-08-14 Delta Green re-check both cited a foreign company's page (exnaton.com) or a funded-company sweep as the receipt for a Czech absence, which is no evidence at all; the incumbent search was aimed at funded startups, and none of the five appears anywhere in this register's 6,181-signal corpus because they are bootstrapped SMB software companies no funding feed will ever surface; and Softlink was already named as a Czech incumbent on p-0026, so the register held the disproof of its own claim. Also cut: the invented Delta Green product names "Proteus" and "DELTA SPOT/FLEX" (zero hits across all 6,181 signals; round-delta-green carries no product breakdown), from the body and the S9 note; the Exnaton traction parenthetical "$10M Series A, 50+ utility customers" in First moves #2, comps-ledger evidence that cannot back a body claim and that "Where it works" already states; and "Lex OZE III", which exists nowhere in the corpus — the substance it carried is real and is now cited to vyhláška 132/2026 Sb., appended as [S12]. The title carried the same disproved absence, "and have no software to run member billing", and was cut to what still stands: it renders on the register, the category pages and this page, so leaving it would have contradicted this record's own ledger in its most-read line. Untouched: the demand and money receipts [S2,S6,S7,S8,S10]. The open question is no longer whether a product exists but whether these vendors reach the long tail of small komunity — a competitive question, not an absence.

2026-08-24 · evidence audit — The lead still asserted that municipalities founding společenství "have no software at all for the task" — the same absence the 2026-08-20 de-rank disproved by naming five CZ vendors [S13]. Cut: a lead cannot assert what the record's own ledger refutes. The de-rank receipt was re-verified live on this date: enerio.cz still sells automated member onboarding, invoicing automation and EDC integration [S13]. Nothing else changed; scores untouched.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "DSO-adjacent service firms" now reads "the service firms around the regional grid operators". Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. Local players moved out of gap-check prose into a structured `locals[]` ledger — Enerio, Softlink CEM, EnerCA, ENERGOMETR (DEKSOFT) and CANCOM, all five marked early [S13]. None passes the established test: Czech sharing over EDC opened only in 2024, so none has three years of selling behind it, and none publishes a customer, a public buyer, a round or a state listing — enerio.cz still runs placeholder testimonial names and empty counters. An early local player does not close a space, so `scores.gap` moves 0 → 1: contested, not taken. `scores.proof` holds at 3 — Exnaton, eFriends, OurPower and Pionierkraft all pass the test, across CH, AT and DE, two of them CEE-adjacent. `score` 8 → 9. The 2026-08-20 de-rank is not withdrawn; the five vendors are real and still named in the body. What changed is that a crowded young field is now scored as contested rather than closed. Fifth pass this date, merged here: the ledger's `status:` field was split into `competes:` (direct or adjacent) and `maturity:` (established or early), so it can now say the thing one field could not — that a real player nearby does not sell this record's product. All five vendors convert to `competes: direct` keeping the maturity they already carried: each sells community administration with allocation keys, member invoicing and EDC settlement to communities, which is this record's product to this record's buyer. **Delta Green** joins the ledger as `competes: adjacent`, reversing the 2026-08-14 decision above to keep it out: it sells spot-price supply and household flexibility aggregation and no sharing administration [S9], and under the split that is intelligence a builder needs rather than a name to drop. It publishes no launch year and neither of its rounds carries a stage letter, so it is early on the test's own terms. `scores.gap` stays 1 — an adjacent player never moves the score, and the direct field is still five young vendors. Deliberately NOT added, and the reasons are recorded so the next pass does not relitigate them: **EDC** is state data infrastructure rather than a vendor; **JMEA** is named in First moves #2 as a target customer, so filing it as competition would mislead the reader the ledger exists to inform; and **ASITIS** has no receipt on file beyond the fact that a 2026-08-13 search returned it [S3], with nothing recorded about what it sells.
