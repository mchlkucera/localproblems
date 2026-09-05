---
id: p-0024
region: cz
title: Czech building owners must plan costly renovations, with no way to compare them
fix: 'Portfolio software for building owners: score every building, rank the renovation
  measures by cost and payback, and turn the EU energy-performance rules into a dated
  capital plan.'
price_search: 'Registr smluv full-text for "energetický management" or "energetický audit" —
  what a kraj (region) or statutory city pays a consultancy to survey and rank its building
  stock is the manual equivalent of the product; the MS2021+ index under "energetického
  managementu" names the owners (Statutární město Liberec, Středočeský kraj) but funds only
  their retrofit delivery, so ask the energy manager (energetický manažer) of either what the
  portfolio triage behind those projects cost.'
category: housing
geo: CZ-national
score: 7
scores:
  proof: 3
  money: 1
  urgency: 2
  demand: 0
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Analytics SaaS over energy-certificate and portfolio data with no certification gate — a dev plus an energy-domain expert can pilot with a mid-size landlord; the real cost is B2B integration and sales effort.'
comps:
- name: 'Fuchs & Eule'
  url: https://fuchs-eule.de/
  geo: DE
  since: 2021
  traction: '€10M round led by GET Fund (TechFundingNews, 2026); 10,000 building analyses; serves commercial landlords and asset managers'
  signal: de-fuchs-eule
- name: Predium
  url: https://en.predium.de/
  geo: DE
  since: 2021
  traction: '€13M Series A led by Norrsken VC (Tech.eu, 2024); ~$21M total raised; customers incl. Colliers, Baloise, Deutsche Investment'
- name: Deepki
  url: https://www.deepki.com/
  geo: FR
  since: 2014
  traction: '€150M Series C (One Peak/Highland, 2022); 500+ clients, 50,000 users, €4T AUM monitored in 80 countries (PR Newswire, 2025)'
  markets: [GB, DE, ES, IT, NL, DK, CH, US, SG, AU]
locals:
- name: PKV BUILD (Enmon, PENB certificates)
  url: https://www.pkv.cz/en/energeticky-management
  ico: '28149785'
  since: 2013
  competes: adjacent
  maturity: established
  evidence: It sells single-building energy-performance assessments and the Enmon monitoring platform,
    which collects consumption every 15 minutes and reports sustainability — no renovation roadmap,
    no ranking of measures and no capex modelling, so it does not sell portfolio retrofit planning
    [S2,S5]. Trading since 2013, with customers including the property group CTP, where Enmon
    is installed [S5].
- name: DEKSOFT (ENERGOMETR)
  url: https://deksoft.eu/programy/energometr
  ico: '27636801'
  since: 2006
  competes: adjacent
  maturity: early
  evidence: It sells ENERGOMETR, which consolidates consumption across many buildings into tables,
    graphs and reports [S5] — monitoring, one product over from the retrofit planning this space
    is about. Parent DEK a.s. has traded since 18 December 2006, but nothing names who runs ENERGOMETR
    and no count is published, so its reach is unknown.
- name: EnergySim (renovacnipas.cz)
  url: https://renovacnipas.cz/
  competes: direct
  maturity: early
  evidence: It sells a renovation-pass calculator to homeowners and energy specialists [S5] —
    the same retrofit-planning job, one building at a time rather than ranked across a portfolio.
    No start year, no buyer names and no count are published, so its reach is unknown.
sources:
- type: arbitrage
  name: "Fuchs & Eule"
  gist: "the Berlin €10M template"
  why: "Berlin, €10M raised in July 2026 for AI building-retrofit analytics that screen landlord and asset-manager portfolios — 10,000 building analyses done. The closest template."
  url: https://techfundingnews.com/fuchs-eule-raises-10m-commercial-landlords-esg/
  note: 'de-fuchs-eule: Fuchs & Eule (Berlin) raised €10M (GET Fund, 8 Jul 2026) for AI building-retrofit
    analytics — screens landlord/asset-manager portfolios for ESG and energy-retrofit needs;
    10,000 building analyses done. Funded DE analog, CEE-adjacent: arbitrage 2.'
  date: '2026-07-08'
  signal: de-fuchs-eule
- type: gap-check
  name: "Czech retrofit-analytics scan (first pass)"
  gist: "the first Czech scan"
  why: "The early look at the Czech field: certificate consultancies work building by building, with PKV Build the scale player, and no self-serve portfolio retrofit-analytics software was found."
  url: https://techfundingnews.com/fuchs-eule-raises-10m-commercial-landlords-esg/
  note: 'Quick check 2026-08-13: CZ side shows certificate consultancies (PKV Build does energy
    certificates at scale) but no self-serve portfolio retrofit-analytics software. Gap 1
    (quick search only).'
  date: '2026-08-13'
- type: regulation
  name: "EPBD recast — Commission infringement notice"
  gist: "the missed May 2026 deadline"
  why: "Transposition of Directive 2024/1275 was due 29 May 2026; on 15 July 2026 the Commission opened infringement procedures against all 27 Member States including Czechia."
  url: https://energy.ec.europa.eu/news/commission-calls-eu-countries-transpose-reinforced-rules-energy-performance-buildings-2026-07-15_en
  note: 'reg-epbd-recast: EPBD recast (2024/1275) transposition was due 29 May 2026; on 15
    Jul 2026 the Commission opened infringement procedures against all 27 Member States incl.
    CZ. Obligations (BACS for large non-residential, zero-emission new builds, renovation
    passports, solar-readiness) phase in from a compressed CZ implementing law. Deadline 1
    (dates not yet fixed in CZ law).'
  date: '2026-07-15'
  signal: reg-epbd-recast
- type: tender
  name: "TED — the Czech energy-performance-contracting wave (~€58M)"
  gist: "the €58M retrofit wave"
  why: "Klatovy hospital's ~€8.3M award is one of 15 records from 11 distinct public buyers between June and August 2026 — the retrofit spend a portfolio-analytics layer would front-end."
  url: https://ted.europa.eu/en/notice/-/detail/384935-2026
  note: 'ted-384935-2026: Klatovská nemocnice awarded ~€8.3M for energy performance contracting
    (Jun 2026) — part of an EPC wave of 15 TED records from 11 distinct public buyers (~€58M
    distinct value) in Jun–Aug 2026: three Plzeň-kraj hospitals in one week (Stod ~€3.3M,
    Domažlice ~€5.3M, Klatovy), Praha 6 ~€15.7M, Praha 16/18, Hodonín, Kuřim, ČD. Public
    owners are paying for retrofit triage-plus-delivery through ESCOs — adjacent execution
    spend, so money scored 1 (relevant tenders exist), not 2: the tenders buy EPC delivery,
    not the portfolio-analytics layer this record is about.'
  date: '2026-06-04'
  signal: ted-384935-2026
- type: gap-check
  name: "Enmon, ENERGOMETR and the Czech portfolio-software field"
  gist: "the Czech portfolio-software sweep"
  why: "A Czech-language sweep for portfolio retrofit planning. It found monitoring and ESG reporting — Enmon by PKV, ENERGOMETR by DEKSOFT — but no renovation roadmap, measure prioritisation or capex modelling."
  url: https://www.pkv.cz/en/energeticky-management
  note: 'Gap re-check 2026-08-20: looked for a Czech product that screens a PORTFOLIO of buildings
    for retrofit need and sequence — which building, which measure, in what order, at what capex
    — the Fuchs & Eule / Predium shape, as distinct from per-building certificates. Not found.
    What exists is adjacent, and was checked rather than assumed. Enmon (PKV) is a portfolio
    energy-management and sustainability platform, implemented at CTP, but its own pages describe
    automatic 15-minute consumption collection, carbon-footprint calculation and ESG/non-financial
    reporting, with no renovation roadmap, no measure prioritisation and no capex modelling.
    ENERGOMETR (DEKSOFT) likewise consolidates consumption across buildings and provides tables,
    graphs and reports. renovacnipas.cz (EnergySim), the SFŽP renovation-pass application and
    the ufae.cz calculation tool are all single-building and aimed at homeowners or energy
    specialists, and the renovation pass is an NZÚ application artifact rather than a portfolio
    product. Portfolio tools sold into CZ (IBM Envizi, Deepki) reach owners through CBRE-type
    advisory, not as a Czech product. NOT FOUND IS NOT ABSENT: gap stays 1 and score stays 6
    — a search that returns nothing is not evidence that nothing exists, and the surfaces listed
    below are the whole of the coverage claimed here. Flag for the next pass: PKV, named in this
    record as the per-building certificate scale player, also ships portfolio software, so the
    distinction this record rests on is monitoring-versus-retrofit-planning and is narrower than
    the body currently implies.'
  date: '2026-08-20'
  queries:
    - "software energetický management portfolia budov analýza renovace dekarbonizace ESG nemovitosti Česko"
    - "software renovační pas dekarbonizační plán budov portfolio CRREM analýza opatření úspor Česko"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: arbitrage
  name: "aedifion"
  gist: "the €17M controls layer"
  why: "Cologne's aedifion raised a €17M Series B for the cloud layer that sits on a building's existing control system and tunes heating, ventilation and cooling — the building-automation half the directive forces — reporting close to 500 buildings and over 5.8 million square metres under management."
  url: https://tech.eu/2025/06/24/aedifion-secures-eur17m-in-series-b-round/
  note: 'de-aedifion: EUR 17M oversubscribed Series B led by Eurazeo with World Fund, Drees
    und Sommer, BitStone Capital, Phoenix Contact Innovation Ventures, MOMENI Ventures, Bauwens
    Capital and LARTIS, reported 2025-06-24; ~500 buildings and 5.8M m2 across Europe, Britain
    and the United States. Cited as the ADJACENT European layer, not as proof of this record''s
    product: aedifion optimises how a building runs, where this record ranks which building to
    renovate and in what order. What makes it worth carrying is the Czech check attached to it,
    run 2026-09-03 on google-cz, ares and the own funded ledger: BUILDSYS a.s. (IČO 27690253,
    since 2006) integrates building-management systems, HGS a.s. sells the FLOWBOX energy
    orchestration software and Novatec EAS does commercial-building energy management, with
    Schneider Electric and Trane selling the international products here — and the EU-taxonomy
    and ESG reporting layer is served by consultancies such as PwC Czech Republic rather than by
    a building-operations product. No Czech vendor was found joining continuous cloud
    optimisation to taxonomy-grade reporting. Those three Czech names are NOT on this record''s
    ledger and are flagged for a content pass to adjudicate into locals[]; on the reading here
    each sells integration or monitoring rather than the renovation ranking this record names,
    so none is expected to move gap. dims empty: it is neither proof of this product nor a gap
    finding this pass is entitled to score.'
  date: '2025-06-24'
  signal: de-aedifion
  dims: []
created: '2026-08-13'
updated: '2026-09-03'
---

The recast Energy Performance of Buildings Directive obliges member states to force building-automation retrofits, renovation passports, zero-emission new builds and solar-readiness [S3]. Czechia, like all 27 member states, missed the 29 May 2026 transposition deadline and drew a Commission infringement procedure on 15 July 2026 [S3]. The implementing law arrives compressed, and with it the owner's question: which buildings need automated controls, which need insulation, in what order, at what cost.

Why now: the Czech implementing dates are unset [S3], and the infringement procedure is pressure to set them — the buyer's deadline arrives the day the law publishes. Berlin's Fuchs & Eule raised €10M in July 2026 for exactly this product, on 10,000 building analyses [S1]; the same directive drives both markets, Czechia trailing by its transposition lag. Nothing on the Czech shelf ranks measures and costs across a portfolio [S2,S5].

Who pays: commercial and institutional building owners deciding which renovations to fund first, and in what order. Municipal building stock, obligated early under the directive's public-building rules, is the procurement channel. Eleven public buyers awarded about €58M of energy-performance contracting — retrofit work repaid out of the energy it saves — between June and August 2026, three Plzeň-region hospitals among them in a single week [S4]. That is the spend a ranking product sits in front of [S4]. Those tenders buy the delivery, not the ranking.

Existing non-solutions: energy specialists issue energy-performance certificates one building at a time, and PKV Build — a Czech energy consultancy — does that at scale [S2]. Enmon (PKV Build) and ENERGOMETR (DEKSOFT) monitor consumption and report sustainability across a portfolio, with no renovation roadmap, no ranking of measures and no cost modelling [S5]. Nobody sells the owner's plan: which building, which measure, in what order, as distinct from doing the work [S2,S5]. That line — monitoring versus planning — is narrower than an empty field [S5]. Beside it sits the controls layer the directive forces: BUILDSYS integrates building-management systems, HGS (a Czech energy-software vendor) sells the FLOWBOX orchestration platform and Novatec EAS (energy management for commercial buildings) works the same ground, while Cologne's aedifion raised €17M for the cloud optimisation layer above the same equipment, across close to 500 buildings [S6].

Solved elsewhere: three European sellers are past prototype. Predium (Munich, since 2021) raised a €13M Series A and counts Colliers and Baloise as customers; Fuchs & Eule (Berlin, since 2021) raised €10M on 10,000 building analyses; Deepki (Paris, since 2014) monitors €4 trillion of assets in 80 countries after a €150M Series C [S1]. Germany next door, France one market over — each selling the owner-side layer Czech owners lack.

## First moves

1. Sell to the public owners already spending. Eleven public buyers awarded about €58M of energy-performance contracting between June and August 2026 — Klatovy hospital at ~€8.3M, three Plzeň-region hospitals in one week, Praha 6 at ~€15.7M [S4]. They hold many buildings and are obligated early under the directive's public-building rules [S3]. They pay for delivery. Nobody sells them the ranking that decides which building goes first.
2. Build the ranking, not more monitoring. Take the consumption data a building already produces plus its energy certificate. Answer four questions in order: which building, which measure, in what sequence, at what capital cost. Fuchs & Eule raised €10M for that product, on 10,000 building analyses [S1]. The Czech shelf stops at consumption graphs and sustainability reports [S5].
3. Open with the deadline the buyer does not have yet. Czechia missed the 29 May 2026 transposition date and drew a Commission infringement procedure on 15 July 2026 [S3]. The implementing law lands compressed, and its duties — building automation, renovation passports, solar-readiness — with less notice than a portfolio takes to survey.
4. Watch the two vendors closest to this. PKV Build sells single-building assessments plus the Enmon monitoring platform — installed at CTP, an industrial-park landlord — and has traded since 2013 [S5]. DEKSOFT's ENERGOMETR consolidates the same consumption data across buildings [S5]. Either can add ranking, and both read the implementing law the day you do.

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "triaging retrofit capex" now reads "deciding which renovations to fund first, and in what order". Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 2 → 3. All three comparables pass the maturity test — Predium selling since 2021 with Colliers, Baloise and Deutsche Investment named and a €13M Series A; Fuchs & Eule since 2021 with 10,000 building analyses behind a €10M round; Deepki since 2014 with 500+ clients and a €150M Series C [S1] — and they are established in two markets, Germany and France, with Germany CEE-adjacent. That is rung 3 as written; the v1 rung 2 was capped by a clause that has been struck from the ladder. `scores.gap` stays 1 and the reason is now explicit rather than implied: the three Czech products the [S5] sweep found were lifted into a structured `locals[]` ledger, and only one is established — PKV BUILD (IČO 28149785, ARES 2013) on the named-customer limb, Enmon implemented at CTP. DEKSOFT's ENERGOMETR and EnergySim's renovacnipas.cz publish no customer count, pair with no public buyer and carry no round or state listing, so both read early on receipts. An early local player does not close a space, so nothing here supports gap 0; and nothing here raises it either, because rung 2 needs a check that found no local player and this one found three. `score` 6 → 7. The state-side tools in the [S5] note — the SFŽP renovation-pass application and ufae.cz — were deliberately not lifted: they are subsidy-application artifacts, not players selling a product. The Proven-abroad paragraph now states each seller's trading age, because that is the fact carrying the score. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. PKV BUILD moves `early` → `established` and takes `competes: adjacent`. The `early` was never a reading of PKV: this file's own re-score entry, written earlier the same day, calls it the one established player on the named-customer limb with Enmon implemented at CTP, and then the ledger said early anyway, because under the one-field schema an established local forced gap to 0. With `competes` carrying eligibility, PKV records its true maturity and still moves nothing — what it sells is single-building energy-performance assessments plus consumption monitoring, not the portfolio retrofit planning this file is about. DEKSOFT is adjacent for the same reason and stays `early`, no limb being on file for it. EnergySim is the one `competes: direct` entry: a renovation-pass calculator is the same planning job, one building at a time rather than ranked across a portfolio, and it is early. `scores.gap` stays 1, CONTESTED, and now on the rung's literal words — locals sell this and all of them are early. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

2026-08-13 · money receipted — The EPC award wave was put on the ledger — 11 public buyers, ~€58M between June and August 2026 [S4] — carrying money to 1. The substance now sits in How big above rather than here.

2026-08-20 · evidence audit — Removed the EPC supplier-side sentence: the four named companies and associations (ENESA, ČEZ ESCO, MVV, APES) return no hits anywhere in the signal corpus and appear in no source note on this record, and the maturity verdict attached to them had nothing behind it either. The clause that survives, that the unoccupied position is the owner-side analytics product, is the record's own gap check and is now cited to [S2]. Also removed from "Who pays": the claim that banks pricing green mortgages and sustainability-linked loans are a second buyer, since no green-mortgage receipt exists in the corpus.

2026-08-24 · fact check — The window paragraph claimed owners have "no analytics layer, only per-building energy-certificate consultancies"; the record's own re-check found two Czech portfolio energy-management platforms (Enmon by PKV, ENERGOMETR by DEKSOFT) and flagged that the real distinction is monitoring versus retrofit planning, "narrower than the body currently implies" [S5]. The body now names both and claims only what was checked: no retrofit-planning product found, gap unchanged at 1. Enmon's own page was re-verified live on this date — 15-minute consumption collection and ESG reporting, no renovation planning [S5]. The unreceipted "ESG consultancies producing PDFs, and spreadsheets" flourish is gone.

THE LEDGER NOTES, IN PLAIN LANGUAGE. All 3 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

FIRST MOVES WRITTEN. `data/RECORD-TEMPLATE.md` reserves the section for records scoring >= 7 and this file scores 7; it was simply missing, which cost the reader the most actionable thing on the page. Four moves, each drawn from evidence already on the record: the eleven public energy-performance-contracting buyers as the first customers [S4], measure-ranking rather than monitoring as the first build [S1,S5], the missed 29 May 2026 transposition and the July infringement procedure as the opening fact [S3], and PKV Build and DEKSOFT named as the two vendors one product decision away [S5]. No new fact was introduced, no source note was edited and no [Sn] marker was moved.

2026-09-02 · plain-language pass — Five trade terms replaced with plain words at first use — BACS, EPBD, EPC, PENB, ESG — and PKV Build and CTP given appositives. The argument tightened from 447 to 384 words, keeping every [Sn] marker, figure and named company. First moves rewritten verbs-first, the register-voice opener on move 4 gone. A gist added to all five sources. No score, status, note or marker touched.
