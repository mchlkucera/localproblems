---
id: p-0025
region: cz
title: Czech home insulation runs through one-man firms nobody can vet
fix: 'An insulation contractor that actually turns up: own trained crews, a fixed price
  per house, and the state renovation subsidy handled for the homeowner.'
category: energy
geo: CZ-national
score: 6
scores:
  proof: 2
  money: 1
  urgency: 2
  demand: 0
  gap: 1
status: candidate
build:
  capital: funded
  first_revenue: months
  builder: funded-team
  note: 'Physical-ops model — installer training, crews and blowing equipment are payroll and capex before revenue, though each ~€5k fixed-price job pays out within the NZÚ-subsidized homeowner cycle once a crew is live.'
comps:
- name: VARM
  url: https://www.varm.earth/
  geo: DE
  since: 2023
  traction: '€17.5M Series A led by ABN AMRO fund (Tech.eu, 2026); one-day ~€5k fixed-price insulation; 7 DE sites, thousands of projects (TFN)'
  signal: de-varm
- name: dsb Deutsche Sanierungsberatung
  url: https://deutsche-sanierungsberatung.de/
  geo: DE
  since: 2024
  traction: '€10M+ Series A after €3.6M seed (EU-Startups, 2026); ~300 partner trade firms; founded by three ex-Enpal employees'
  signal: round-dsb-sanierung
- name: Enter
  url: https://www.enter.de/
  geo: DE
  since: 2020
  traction: '€20M Series B, €40M total raised (Tech.eu, 2025); digital energy audits, subsidy handling and renovation delivery for homeowners'
locals:
- name: CIUR
  url: https://www.ciur.cz/
  ico: '40612724'
  status: early
  evidence: 'EARLY for this space — CIUR makes insulation material and sells it through its own
    application centre and a partner-firm network for Climatizer Plus [S6], a manufacturer
    channel rather than the trained-crew, fixed-price installed job this record proposes;
    ARES registration 1991-07-11. No limb of the established test is met by anything on file
    here: nothing names who has bought it, no published tally exists, there is no pairing in
    data/lookup/cz-contract-parties.jsonl, no round at Series stage, and no state listing.'
- name: dotacenarenovace.cz
  url: https://dotacenarenovace.cz/
  status: early
  evidence: 'EARLY for this space — turnkey renovation covering assessment, the state subsidy application
    and the building work, delivered by a 25-year-old construction firm paired with a
    subsidy agency [S6]. That is a general contractor with a subsidy desk, not the
    standardised crew-and-fixed-price operator this record proposes. No limb of the
    established test is met by anything on file here: nothing names who has bought it, no
    published tally exists, there is no pairing in data/lookup/cz-contract-parties.jsonl, no
    round at Series stage, and no state listing.'
sources:
- type: arbitrage
  name: "VARM"
  why: "Berlin, €17.5M Series A in June 2026 — trains career-changers as certified installers, insulates a family home in one day at a fixed ~€5k price and runs the whole operation on software."
  url: https://tech.eu/2026/06/23/berlins-varm-bags-eur175m-to-scale-insulation-across-europe/
  note: 'de-varm: VARM (Berlin) raised €17.5M Series A (ABN AMRO Sustainable Impact Fund,
    23 Jun 2026) as a tech-enabled insulation installer — trains career-changers as certified
    installers, insulates a family home in one day at a fixed ~€5k price, software-driven
    ops. Funded DE analog, CEE-adjacent: arbitrage 2.'
  date: '2026-06-23'
  signal: de-varm
- type: subsidy
  name: "Nová zelená úsporám"
  why: "The standing Czech subsidy programme that co-pays insulation alongside heat pumps and photovoltaics — it pre-validates household demand and funds part of every ticket."
  url: https://novazelenausporam.cz/
  note: Nová zelená úsporám funds zateplení (insulation) alongside heat pumps/PV — the standing
    subsidy program that pre-validates household demand and co-pays the ticket. Money 1 (relevant
    grant program exists).
  date: '2026-08-13'
- type: gap-check
  name: "Czech insulation-trade scan (first pass)"
  why: "The early look at the Czech field: Woltair proved the vertical-installer model here for heat pumps and photovoltaics but does not do insulation, which stays a long tail of small firms."
  url: https://tech.eu/2026/06/23/berlins-varm-bags-eur175m-to-scale-insulation-across-europe/
  note: 'Quick check 2026-08-13: Woltair proved the CZ vertical-installer model for heat pumps/PV
    but does not do insulation; the insulation trade remains a long tail of small firms with
    no tech-enabled consolidator. Gap 1 (quick search only).'
  date: '2026-08-13'
- type: arbitrage
  name: "dsb Deutsche Sanierungsberatung"
  why: "Berlin, €10M Series A in July 2026 — packages renovation consulting, subsidy applications and contractor delivery for homeowners. The demand-side half of the model, funded a month after VARM."
  url: https://www.vestbee.com/insights/articles/top-european-funding-rounds-closed-in-july-2026
  note: 'round-dsb-sanierung: dsb Deutsche Sanierungsberatung (Berlin) raised €10M Series
    A (Jul 2026, IBB Ventures + Vireo + FJ Labs) packaging energy-renovation consulting, subsidy
    applications and contractor delivery for homeowners — a SECOND funded DE company on home-renovation
    execution within a month of VARM, attacking the demand-side wedge (subsidy navigation
    + delivery packaging) that maps directly onto NZÚ. Same market as VARM, so proof stays
    2; the wedge coverage now spans install labor AND homeowner navigation.'
  date: '2026-07-31'
  signal: round-dsb-sanierung
- type: regulation
  name: "EPBD recast — Commission infringement notice"
  why: "Transposition overdue since May 2026 and infringement opened against Czechia on 15 July 2026; residential renovation trajectories dated 2030 and 2033 put a legal driver behind household insulation."
  url: https://energy.ec.europa.eu/news/commission-calls-eu-countries-transpose-reinforced-rules-energy-performance-buildings-2026-07-15_en
  note: 'reg-epbd-recast: EPBD recast (2024/1275) — transposition overdue since May 2026,
    infringement procedure opened against CZ on 15 Jul 2026; residential renovation trajectories
    and MEPS timelines dated 2030/2033 put a dated regulatory driver behind household insulation
    demand. Deadline sub-score 1 (>18mo, CZ dates pending): urgency 1→2.'
  date: '2026-07-15'
  signal: reg-epbd-recast
- type: gap-check
  name: "Czech insulation supply — a second, deeper sweep"
  why: "Looked for a scaled tech-enabled insulation consolidator and found the long tail instead: regional directories, individual applicators, CIUR's manufacturer-partner network, and dotacenarenovace.cz — a 25-year construction firm with a subsidy desk."
  url: https://dotacenarenovace.cz/
  note: 'Gap re-check 2026-08-20: looked for a Czech tech-enabled insulation consolidator —
    either the VARM shape (trained crews, standardised fixed-price one-day job, software-run
    ops) or the dsb/Enter shape (homeowner acquisition plus subsidy handling plus packaged
    delivery). No scaled tech-enabled player found. Every surface returned the long tail this
    record already describes: regional directories listing zateplení firms kraj by kraj
    (izolace-info.cz), individual applicators (FOUKNUTO, Bezvaizolace, Magmarelax), and CIUR
    a.s., a material manufacturer running its own application centre plus a partner-firm network
    for Climatizer Plus — the manufacturer-channel model, not a consolidator. Closest to the
    dsb wedge is dotacenarenovace.cz: turnkey renovation covering assessment, NZÚ application
    (10k CZK deposit plus 40k on approval, claimed 99% success) and the building work including
    facade insulation — but it is a 25-year construction firm paired with a subsidy agency,
    500+ renovations lifetime, which is a general contractor with a subsidy desk and is already
    accounted for in this record''s existing-non-solutions paragraph. Corroborating the other
    half of the claim: Schlieger, a CZ installer with 23,000+ installations and in-house NZÚ
    handling, sells fotovoltaika, tepelná čerpadla and solární ohřev only — no zateplení, the
    same skip the record attributes to Woltair. Woltair itself is NOT VERIFIED either way: a
    direct fetch of woltair.cz was refused (ECONNREFUSED), search summaries conflict, and every
    purchasable service URL found is heat pumps, photovoltaics, boilers or servis against a
    self-description of "Experti na tepelná čerpadla a fotovoltaiku". NOT FOUND IS NOT ABSENT:
    gap stays 1 and score stays 6 — a search returning nothing never raises a score. The record''s
    own next-evidence question, whether Woltair expands into insulation, stays open and should
    be settled by asking Woltair, not by searching.'
  date: '2026-08-20'
  queries:
    - "zateplení rodinného domu na klíč fixní cena foukaná izolace vyřídíme dotaci celá ČR"
    - "zateplení izolace na klíč franšíza síť montážních týmů standardizovaná fixní cena za den Česko"
    - "komplexní energetická renovace domu na klíč vyřízení dotace NZÚ projekt realizace jedna firma"
    - "český startup renovace domů zateplení na klíč platforma investice miliony korun"
    - "Woltair zateplení izolace domu služba nabídka rozšíření"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
created: '2026-08-13'
updated: '2026-08-25'
---

Insulating a Czech family home means finding one of thousands of small zateplení firms, waiting for a quote, and hoping the NZÚ subsidy paperwork gets handled. The trade is a fragmented long tail of small regional firms [S3,S6]. Meanwhile the subsidy program that co-pays the work — Nová zelená úsporám — runs continuously, pre-validating household demand [S2].

Why now: VARM in Berlin just raised €17.5M for the answer: train career-changers into certified insulation installers, standardize the job to one day at a fixed ~€5k price, and run the whole operation on software [S1]. It is Woltair's Czech playbook — vertical integration of a subsidized energy trade — applied to a trade Woltair skipped [S3]. The model attacks labor supply rather than selling software to firms that are too small to buy it [S1].

Who pays: homeowners, part-funded by the state renovation subsidy Nová zelená úsporám [S2], and later the apartment-owner associations and housing cooperatives that run multi-unit buildings. The fixed-price, one-day product is the wedge [S1]; subsidy handling in-house removes the paperwork objection that suppresses demand today.

EPBD gives the same work a dated regulatory driver: transposition is overdue, the Commission opened infringement against CZ in July 2026, and residential MEPS trajectories (2030/2033) mean household insulation stops being optional [S5]. [EPBD pressure](/problem/cz/p-0024) is upstream demand for the same work: as renovation obligations firm up [S5], execution capacity becomes the bottleneck this model builds.

Existing non-solutions: the fragmented installer long tail [S3]; general contractors for whom insulation is a side line; energy-consulting firms that specify but don't build. Woltair is the proof the CZ market rewards this model — and the proof it's unoccupied for insulation [S3]. Next evidence: NZÚ zateplení application/backlog statistics to document demand, and a check on whether Woltair has insulation expansion plans (the competitive risk).

Solved elsewhere: Berlin funded the second half of the model within a month of the first — dsb Deutsche Sanierungsberatung (€10M Series A) packages renovation consulting, subsidy applications and contractor delivery for homeowners, the demand-side navigation wedge to VARM's supply-side installer wedge [S4]. VARM has been installing since 2023 across seven German sites, and Enter has sold homeowner audits and delivery since 2020 on €40M raised; dsb only opened in 2024 [S1,S4]. It is all one country. The full stack — find the homeowner, handle the subsidy, deliver the retrofit at a fixed price — is proven next door and nowhere else yet.

## Revisions

2026-08-13 · proof and deadline receipted — The dsb Deutsche Sanierungsberatung round [S4] and the EPBD infringement and MEPS trajectory [S5] were added; the substance now sits in Where it works and The window above rather than here.

2026-08-20 · evidence audit — Removed ENBRA from the next-evidence proposal. The name returns no hits anywhere in the signal corpus and appears in no source note on this record — a named competitive risk with nothing behind it. Woltair is receipted [S3] and stays.

2026-08-24 · fact check — Three unreceipted clauses cut from the lead and window: "quality is unverifiable", "capacity is capped by the same labor shortage as every other building trade", and labor as "the actual constraint" — none carried by any source here (S1 is a German funding note, and the Czech receipts document fragmentation, not workforce data). Fragmentation stays, cited to the Czech checks [S3,S6], and "demand the supply side cannot serve" lost its unreceipted second half. A live re-check of woltair.cz on this date again surfaced only heat-pump and photovoltaics service pages, with insulation appearing only as blog content — consistent with [S3]; the S6 open question, whether Woltair expands into insulation, stands.

2026-08-25 · plain-language pass, then re-scoring — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "NZÚ co-payment" now reads "part-funded by the state renovation subsidy Nová zelená úsporám", and "SVJ/bytová družstva" now reads "the apartment-owner associations and housing cooperatives". Scores, status, source notes and every [Sn] marker are untouched by that pass. Second pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, and both dimensions held. `scores.proof` stays 2, but on a different and better reason than before. The v1 answer was "both rounds are German"; the maturity test gives the same number for a sharper cause — VARM has sold since 2023 across seven sites and Enter since 2020 on €40M raised, so both are established, while dsb only opened in 2024 and is early. Established sellers in ONE market is rung 2; rung 3 needs two, and Germany is the only one on file. `scores.gap` stays 1. The two Czech players the [S6] sweep found were lifted into a structured `locals[]` ledger, and both are established — CIUR (IČO 40612724, ARES 1991) on the named-customer limb via its Karviná contract in `data/lookup/cz-contract-parties.jsonl`, and dotacenarenovace.cz on a stated 500+ renovations over 25 years. Neither sells what this record proposes: CIUR sells material through a partner channel and dotacenarenovace.cz is a general contractor with a subsidy desk, which is the "weak or legacy incumbents" wording of rung 1 exactly, not the "already sells this" of rung 0. Nothing raises it either — rung 2 requires a check that found no local player, and this one found several. `score` unchanged at 6. Deliberately not lifted into `locals[]`: Woltair and Schlieger, because the checks on this record establish that neither sells zateplení at all [S3,S6], and the individual applicators and regional directories, because they are the long tail this record is about rather than incumbents holding the position. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.
