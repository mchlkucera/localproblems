---
id: p-0001
region: cz
title: Czech energy communities lose up to half the value of shared electricity to bad allocation
  and settlement, and have no software to run member billing
category: energy
geo: CZ-national
score: 10
scores:
  proof: 3
  money: 2
  urgency: 1
  demand: 2
  gap: 2
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
    aggregator — DELTA SPOT/FLEX tariffs, Proteus smart control, grid-balancing VPP. Site and
    press show no sdílení elektřiny product: no community administration, member billing, allocation
    keys or EDC settlement. Adjacent niche, gap 2 stands. Named because Lex OZE III links sharing
    with flexibility aggregation at EDC from Aug 2026 — Delta Green is the most plausible CZ
    entrant into this niche and the adjacency should be re-checked each cycle.'
  date: '2026-08-14'
  signal: round-delta-green
created: '2026-08-13'
updated: '2026-08-19'
---

Czech energy communities (energetická společenství) and groups sharing electricity under Lex OZE II have been legally able to share power via EDC since August 2024, but they run member administration, allocation keys and settlement by hand. Per the HN reporting cited in the de-exnaton signal, communities lose up to roughly half of the value of shared electricity to bad allocation and settlement. Municipalities founding společenství — a core intended user of the regime — have no software at all for the task.

Why now: the regulatory window opened in 2024 (Lex OZE II, EDC data exchange live) and the first cohort of communities is now operating long enough to feel the settlement losses. EDC handles data exchange between market participants but explicitly does not do community administration, member billing or optimization, so the pain sits with the community operator, unaddressed by state infrastructure.

Who pays: community founders (municipalities, housing cooperatives, groups of firms) and — following the Exnaton go-to-market — utilities and DSO-adjacent service firms that want a white-label product to offer communities. The value proposition is direct: recovered settlement value, which the demand receipt quantifies at up to ~50% of shared electricity.

Existing non-solutions: EDC (data exchange only), ministry guidance, and ASITIS-style consultancies selling services rather than product; Jihomoravská energetická agentura now administers sharing for the sdílEjme community as a manual regional service. The absence check of 2026-08-13 found no dedicated Czech community-energy billing/settlement SaaS — the emerging administration providers are exactly the white-label customer base the Exnaton model sells into.

Solved elsewhere: Exnaton (ETH spin-off) sells exactly this to utilities across DACH and the Nordics; Austrian community-energy players eFriends and OurPower prove tooling demand under EU RED II in a market bordering Czechia. The July 2026 Pstryk round in Poland shows CEE investors funding adjacent consumer/SME energy software.

Updated 2026-08-13: the registr smluv now shows the spend is structural, not anecdotal. The Liberec community alone signed ~14 near-identical sharing contracts with city schools and kindergartens in June–July 2026 (series numbering to č. 58), Pardubice-region institutions follow the same pattern, and Sonnentor became the first private company in the evidence bucket, administered by a public energy agency. Recurring, multi-organisation service spend on sharing administration is receipted — money moves 1→2 and the record enters PRIME territory: every operating community is a billing/settlement customer paying for a manual service today.

Updated 2026-08-14: incumbent re-check against the funded-CZ sweep. Delta Green (Prague, ~€4.2M raised across 2024–25) was flagged as a possible occupier — verified adjacent, not occupying: it sells spot-price supply and household flexibility aggregation (Proteus, grid balancing), with no community-sharing administration, member billing, allocation-key or EDC-settlement product on its site or in press. The gap claim survives. It is named here because Lex OZE III ties sharing to flexibility aggregation at EDC from August 2026, which makes Delta Green the most credible potential entrant — the strongest current threat to this gap, worth re-checking every cycle.

## First moves

1. Call the operator of **Energetické společenství Liberec** first — the community that signed ~14 near-identical sharing contracts with Liberec schools and kindergartens in Jun–Jul 2026 (series numbering observed up to č. 58): ask to walk through how allocation keys and member settlement are run today, and turn that manual process into the product spec.
2. Second call: **Jihomoravská energetická agentura**, which manually administers sharing for the sdílEjme community including Sonnentor — administration providers like JMEA are exactly the white-label customer the Exnaton model sells to ($10M Series A, 50+ utility customers).
3. Build the settlement-reconciliation wedge first: ingest one community's real EDC sharing data, recompute allocation and member billing, and put a CZK figure on the recovered value — the record's demand receipt claims up to ~50% of shared-electricity value is lost to bad allocation and settlement. The same exercise verifies the risky assumption that EDC data exchange gives an outside operator enough data to automate settlement.
4. Price under the receipts: Dům seniorů Františkov paid ~1.0M CZK for a sharing-service contract — SaaS priced below that manual-service level has documented willingness-to-pay on file.
5. Funding channel: [Modernizační fond KOMUNERG 1/2025](/sources/tenders#dotace-mf-komunerg-1-energeticka-spolecenstvi) — 1bn CZK (~€40.8M) for energy communities and municipalities building shared renewable generation, applications open until **2027-12-31**; every funded community build becomes a settlement/billing customer.
6. Competition on file: **Delta Green** (adjacent, not occupying — spot-price supply and flexibility aggregation, no sharing-administration product; the most credible entrant once Lex OZE III links sharing with flexibility at EDC from Aug 2026), **ASITIS** (consulting/services, not product), **EDC** itself (data exchange only, explicitly no member billing), and **JMEA** (manual regional service — a prospective customer more than a rival).
