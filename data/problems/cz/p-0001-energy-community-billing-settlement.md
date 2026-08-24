---
id: p-0001
region: cz
title: Czech energy communities lose up to half the value of shared electricity to bad allocation
  and settlement
category: energy
geo: CZ-national
score: 8
scores:
  proof: 3
  money: 2
  urgency: 1
  demand: 2
  gap: 0
status: watching
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
sources:
- type: arbitrage
  url: https://exnaton.com/
  note: 'de-exnaton: DACH/Nordics-proven white-label billing/settlement SaaS for energy communities
    (ETH spin-off, used by utilities); Austrian peers eFriends/OurPower validate the category
    in a CEE-adjacent market. Absence check 2026-08-13 found no CZ equivalent.'
  date: '2026-08-13'
  signal: de-exnaton
- type: complaint
  url: https://exnaton.com/
  note: 'HN (2025) report cited in de-exnaton: CZ communities reportedly lose up to ~50% of
    shared electricity value to bad allocation/settlement; municipalities founding společenství
    have zero software.'
  date: '2026-08-13'
- type: gap-check
  url: https://exnaton.com/
  note: 'Absence check 2026-08-13: searches return only EDC itself, ministry PR and ASITIS
    (consulting/services); no dedicated CZ community-energy billing/settlement SaaS.'
  date: '2026-08-13'
- type: round
  url: https://www.vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-july-2026
  note: 'round-pstryk: Pstryk (PL, dynamic electricity pricing for households/SMEs) raised
    EUR 7M Series A led by Future Energy Ventures, Jul 2026 — CEE investor appetite for consumer/SME
    energy tooling.'
  date: '2026-08-04'
  signal: round-pstryk
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/385664-2026
  note: 'ted-385664-2026: obec Petrovice u Karviné awarded ~€278k design-and-build for ''Komunitní
    energetika'' (TED, closed award, Jun 2026) — municipal budgets are flowing into community-energy
    delivery; each completed build becomes a settlement/billing customer. Money scored 1 at
    creation; upgraded to 2 on 2026-08-13 by the sharing-series receipts below.'
  date: '2026-06-05'
  signal: ted-385664-2026
- type: contract
  url: https://smlouvy.gov.cz/smlouva/38899662
  note: 'hlidac-38899662: Dům seniorů Františkov (Liberec) signed ''Smlouva o zajištění sdílení
    elektřiny č. 58'' (~1.0M CZK, registr smluv) — public institutions are paying for sharing
    services and the provider''s numbering implies a contract series; 37 komunitní-energetika
    contracts in registr smluv since Jun 2026.'
  date: '2026-07-01'
  signal: hlidac-38899662
- type: contract
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
  url: https://smlouvy.gov.cz/smlouva/38760740
  note: 'hlidac-38760740: Jihomoravská energetická agentura signed a sharing-administration
    contract covering Sonnentor within the sdílEjme community (Jun 2026) — the first private-company
    participant in the evidence bucket, and a public regional agency acting as the administration-service
    provider. Extends who-pays beyond public institutions; also names JMEA on the services
    (not SaaS) side of the gap.'
  date: '2026-06-29'
  signal: hlidac-38760740
- type: gap-check
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
  url: https://smlouvy.gov.cz/smlouva/38404378
  note: 'hlidac-38404378: Nemocnice Pardubického kraje contracted Energetické společenství
    východních Čech for electricity sharing (~200k CZK vč. DPH, registr smluv, Jun 2026) —
    the Liberec enrolment pattern repeating in a second region and a healthcare buyer type,
    extending the sharing-contract wave beyond schools.'
  date: '2026-06-16'
  signal: hlidac-38404378
- type: subsidy
  url: https://sfzp.gov.cz/dotace-a-pujcky/modernizacni-fond/vyzvy/
  note: 'dotace-mf-komunerg-1-energeticka-spolecenstvi: Modernizační fond KOMUNERG 1/2025 —
    1bn CZK (~€40.8M) for energy communities, municipalities and their associations building
    shared renewable generation, applications open until 31.12.2027; directly funds community
    PV, grid connection and administration after the energy-community legislation.'
  date: '2027-12-31'
  signal: dotace-mf-komunerg-1-energeticka-spolecenstvi
- type: regulation
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
created: '2026-08-13'
updated: '2026-08-24'
---

Czech energy communities (energetická společenství) and groups sharing electricity under Lex OZE II have been legally able to share power via EDC since August 2024, but they run member administration, allocation keys and settlement by hand [S1]. Per Hospodářské noviny reporting on file, communities lose up to roughly half of the value of shared electricity to bad allocation and settlement [S2].

Why now: the regulatory window opened in 2024 (Lex OZE II, EDC data exchange live) and the first cohort of communities is now operating long enough to feel the settlement losses. EDC handles data exchange between market participants but explicitly does not do community administration, member billing or optimization [S1], so the pain sits with the community operator, unaddressed by state infrastructure.

Who pays: community founders (municipalities, housing cooperatives, groups of firms) and — following the Exnaton go-to-market — utilities and DSO-adjacent service firms that want a white-label product to offer communities [S1]. The value proposition is direct: recovered settlement value, which the reporting on file quantifies at up to ~50% of shared electricity [S2].

Existing non-solutions: EDC (data exchange only), ministry guidance, and ASITIS-style consultancies selling services rather than product [S3]; Jihomoravská energetická agentura administers sharing for the sdílEjme community as a manual regional service [S8]. The software position is occupied too — Enerio, Softlink CEM, EnerCA, ENERGOMETR and CANCOM already sell community administration, allocation keys and member billing over EDC data [S13]. The earlier finding that no such software existed [S1,S3] searched the wrong places and is superseded.

Solved elsewhere: Exnaton (ETH spin-off) sells exactly this to utilities across DACH and the Nordics; Austrian community-energy players eFriends and OurPower prove tooling demand under EU RED II in a market bordering Czechia [S1]. The July 2026 Pstryk round in Poland shows CEE investors funding adjacent consumer/SME energy software [S4].

## First moves

1. Call the operator of **Energetické společenství Liberec** first — the community that signed ~14 near-identical sharing contracts with Liberec schools and kindergartens in Jun–Jul 2026 (series numbering observed up to č. 58) [S7]: ask to walk through how allocation keys and member settlement are run today, and turn that manual process into the product spec.
2. Second call: **Jihomoravská energetická agentura**, which manually administers sharing for the sdílEjme community including Sonnentor [S8] — administration providers like JMEA are exactly the white-label customer the Exnaton model sells to [S1].
3. Build the settlement-reconciliation wedge first: ingest one community's real EDC sharing data, recompute allocation and member billing, and put a CZK figure on the recovered value — the reporting on file claims up to ~50% of shared-electricity value is lost to bad allocation and settlement [S2]. The same exercise verifies the risky assumption that EDC data exchange gives an outside operator enough data to automate settlement.
4. Price under the documented spend: Dům seniorů Františkov paid ~1.0M CZK for a sharing-service contract [S6] — SaaS priced below that manual-service level has documented willingness-to-pay on file.
5. Funding channel: [Modernizační fond KOMUNERG 1/2025](/sources/tenders#dotace-mf-komunerg-1-energeticka-spolecenstvi) — 1bn CZK (~€40.8M) for energy communities and municipalities building shared renewable generation, applications open until **2027-12-31** [S11]; every funded community build becomes a settlement/billing customer.
6. Competition on file — the niche is occupied, so treat the first moves above as competitive research, not a greenfield plan: **Enerio**, **Softlink CEM**, **EnerCA**, **ENERGOMETR** (DEKSOFT) and **CANCOM** all ship Czech community administration with allocation keys, member invoicing and EDC integration [S13]. Also on file: **Delta Green** (adjacent — spot-price supply and flexibility aggregation, no sharing-administration product [S9]), **ASITIS** (consulting/services, not product) [S3], **EDC** itself (data exchange only, explicitly no member billing) [S1,S3], and **JMEA** (manual regional service) [S8].

## Revisions

2026-08-13 · money re-score — The registr smluv shows the spend is structural, not anecdotal [S6,S7]: the Liberec community alone signed ~14 near-identical sharing contracts with city schools and kindergartens in June–July 2026 (series numbering to č. 58) [S7], Pardubice-region institutions follow the same pattern [S10], and Sonnentor became the first private company in the bucket, administered by a public energy agency [S8]. Recurring, multi-organisation service spend on sharing administration is receipted: money 1 → 2, and the record entered PRIME territory.

2026-08-14 · incumbent re-check — Delta Green (Prague, ~€4.2M raised across 2024–25) was flagged by the funded-CZ sweep as a possible occupier and verified adjacent rather than occupying: it sells spot-price supply and household flexibility aggregation, with no community-sharing administration, member billing, allocation-key or EDC-settlement product on its site or in press [S9]. It was named because vyhláška 132/2026 Sb. adds EDC rules for evaluating technical flexibility and storage, configurable from August 2026 [S12], which made it the most credible potential entrant. That framing was wrong about where the competition was — see below.

2026-08-20 · de-rank and evidence audit — Three blocks recorded on this date, merged here; the de-rank was written down twice and is stated once. The central absence claim was false: Czech-language search found five CZ vendors selling community-energy administration with allocation keys, member billing and EDC integration — Enerio, Softlink CEM, EnerCA, ENERGOMETR (DEKSOFT) and CANCOM [S13] — so gap moved 2 → 0, score 10 → 8, status candidate → watching per the SPEC §4 de-rank rule. Three general failure modes, recorded because they recur: the 2026-08-13 check and the 2026-08-14 Delta Green re-check both cited a foreign company's page (exnaton.com) or a funded-company sweep as the receipt for a Czech absence, which is no evidence at all; the incumbent search was aimed at funded startups, and none of the five appears anywhere in this register's 6,181-signal corpus because they are bootstrapped SMB software companies no funding feed will ever surface; and Softlink was already named as a Czech incumbent on p-0026, so the register held the disproof of its own claim. Also cut: the invented Delta Green product names "Proteus" and "DELTA SPOT/FLEX" (zero hits across all 6,181 signals; round-delta-green carries no product breakdown), from the body and the S9 note; the Exnaton traction parenthetical "$10M Series A, 50+ utility customers" in First moves #2, comps-ledger evidence that cannot back a body claim and that "Where it works" already states; and "Lex OZE III", which exists nowhere in the corpus — the substance it carried is real and is now cited to vyhláška 132/2026 Sb., appended as [S12]. The title carried the same disproved absence, "and have no software to run member billing", and was cut to what still stands: it renders on the register, the category pages and this page, so leaving it would have contradicted this record's own ledger in its most-read line. Untouched: the demand and money receipts [S2,S6,S7,S8,S10]. The open question is no longer whether a product exists but whether these vendors reach the long tail of small komunity — a competitive question, not an absence.

2026-08-24 · evidence audit — The lead still asserted that municipalities founding společenství "have no software at all for the task" — the same absence the 2026-08-20 de-rank disproved by naming five CZ vendors [S13]. Cut: a lead cannot assert what the record's own ledger refutes. The de-rank receipt was re-verified live on this date: enerio.cz still sells automated member onboarding, invoicing automation and EDC integration [S13]. Nothing else changed; scores untouched.
