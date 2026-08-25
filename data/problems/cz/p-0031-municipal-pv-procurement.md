---
id: p-0031
region: cz
title: Czech towns buy rooftop solar one by one, and overpay for it
fix: 'An aggregator that pools many towns'' rooftop-solar projects into one fixed-price
  contract, so the lots stop being too small for a supplier to bid on.'
category: energy
geo: CZ-national
score: 6
scores:
  proof: 2
  money: 2
  urgency: 1
  demand: 0
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: year-plus
  builder: small-team
  note: 'An aggregation operator needs campaign ops, procurement-law expertise and a light platform rather than heavy capital, but municipal joint-purchasing decisions and ZZVZ frameworks run on public-sector clocks — the record''s own lots fail repeatedly.'
comps:
- name: iChoosr
  url: https://ichoosr.com/
  geo: NL
  since: 2008
  traction: '2.5M+ households served via group-buying auctions (company site, 2026); 200+ UK councils have run Solar Together (Sunsave, 2026)'
  markets: [GB, BE, DE, FR, AT, PL, US, CA, JP]
locals:
- name: SAKO Brno ("36 FVE" framework)
  url: https://zakazky.sako.cz/contract_display_128.html
  ico: '60713470'
  status: early
  evidence: 'EARLY for this space — SAKO runs the "36 FVE" multi-district photovoltaic framework for the
    city districts of Brno [S4], but it aggregates for its own owner: it is not a supplier
    selling aggregation to towns that do not already have a framework of their own, which is
    the position this record describes as open. On that service no limb of the established
    test is met by anything on file here: nothing names who has bought it, no published
    tally exists, there is no pairing in data/lookup/cz-contract-parties.jsonl, no round at
    Series stage, and no state listing.'
sources:
- type: tender
  name: "TED — South Moravia rooftop PV (~€1.0M), and the wave around it"
  why: "One of ~80 photovoltaic procurement records from 53 distinct public buyers (~€60M) between June and August 2026 — most lots €120k to €1M, each tendered as bespoke design-build."
  url: https://ted.europa.eu/en/notice/-/detail/450591-2026
  note: 'ted-450591-2026: Jihomoravský kraj — OPEN ~€1.0M (~24M CZK) competition for PV plants
    with battery storage on regional buildings (Jul 2026). Open tender ≥5M CZK: money 2. One
    of ~80 PV procurement records from 53 distinct public buyers (~€60M) in the Jun–Aug TED
    window — towns, school districts, zoos, WWTPs, regional governments — most lots between
    €120k and €1M, each tendered as bespoke design-build.'
  date: '2026-07-01'
  signal: ted-450591-2026
- type: tender
  name: "TED — Špindlerův Mlýn, the same tender published three times"
  why: "One town republished an identical wastewater-plant PV tender three times in ten weeks, and Hrabová and Nymburk re-ran their own lots — the transaction-cost receipt for fragmentation."
  url: https://ted.europa.eu/en/notice/-/detail/427895-2026
  note: 'ted-427895-2026: Town of Špindlerův Mlýn published the same WWTP-building PV tender
    for the THIRD time in ten weeks (ted-417514, ted-421736, ted-427895); Hrabová and Nymburk
    also re-ran identical lots in the window. Small municipal PV lots repeatedly fail to close
    — the transaction-cost receipt for procurement fragmentation.'
  date: '2026-06-22'
  signal: ted-427895-2026
- type: contract
  name: "Registr smluv — Jindřichův Hradec municipal PV (~2.5M CZK)"
  why: "The layer below the TED threshold: a town bundling build and ongoing servicing for photovoltaics on one municipal building."
  url: https://smlouvy.gov.cz/smlouva/38371366
  note: 'hlidac-38371366: Jindřichův Hradec signed a ~2.5M CZK works-and-service contract
    for PV on a municipal building (Jun 2026) — the below-TED-threshold layer of the same
    wave, bundling build with ongoing servicing town by town.'
  date: '2026-06-11'
  signal: hlidac-38371366
- type: gap-check
  name: "Brno's '36 FVE' framework and the aggregation channels"
  why: "The aggregation answer partly exists and is named here: Brno pools its districts through SAKO, kraje package their own buildings, and RES+ explicitly funds joint multi-site municipal projects."
  url: https://zakazky.sako.cz/contract_display_128.html
  note: 'Gap check 2026-08-13: aggregation mechanisms already exist — Brno runs a "36 FVE"
    multi-district framework via SAKO, SFŽP''s RES+ / Modernizační fond calls explicitly fund
    joint multi-site municipal PV projects, and kraje package design-builds (Královéhradecký
    packages 3-5, Vysočina IV in this window). The supply side (ESCOs, installers) is dense.
    Field not empty: gap 0 with channels named — the residual problem is that the long tail
    of municipalities does not use them.'
  date: '2026-08-13'
- type: arbitrage
  name: "iChoosr"
  why: "The Dutch operator of exactly this model: municipalities pool demand into one tendered contract, run as Solar Together by more than 200 UK councils."
  url: https://ichoosr.com/
  note: 'Comps receipt written 2026-08-25, because iChoosr sat on the comps ledger with no
    sources[] entry behind it and SCORING.md allows no point without one. Verified live on this
    date: ichoosr.com describes platforms that "match demand and supply for sustainable energy
    products" and lists ten operating countries — United States, United Kingdom, Netherlands,
    Japan, Poland, Belgium, Germany, France, Austria, Canada. NOT verified: the page publishes
    no participant or partner figures, so the comps traction line (2.5M+ households served, per
    the company site; 200+ UK councils running Solar Together, per Sunsave) stays
    secondary-reported and is cited as such. Founded 2008. ESTABLISHED under the SCORING.md
    test on the customer-count limb, with the receipted traction sitting in the Netherlands and
    the United Kingdom; the Polish, German and Austrian markets are a bare country list with no
    traction behind them, which is why proof is 2 here and not 3.'
  date: '2026-08-25'
- type: gap-check
  name: "Czech municipal-solar supply — who, if anyone, sells pooled procurement"
  why: "The first Czech-language sweep of the supply side. It found turnkey installers pitching towns one at a time, and SMS ČR pooling energy PURCHASES for 200+ member obce since 2013 — but no operator selling pooled solar procurement to towns that have no framework of their own."
  note: 'Czech-language supply-side sweep 2026-08-25, run because the 2026-08-13 check on this
    file recorded no queries at all and gap therefore rested on coverage nobody could judge.
    WHAT WAS LOOKED FOR: a company selling demand aggregation for municipal rooftop
    photovoltaics — the iChoosr shape, where many towns'' lots are pooled into one tendered
    fixed-price contract. NOT FOUND. What the surfaces returned instead, all of it selling
    something adjacent: turnkey design-build installers pitching municipalities individually
    (iKomunita, LAMBDA Energy, SVP Solar, Panomik Solar, Fotovolty, LAMA Solar, Energie Soláry,
    reWATT, SEFY), and the subsidy and dotace portals that route towns to them. The nearest
    aggregation that is genuinely SOLD is SMS ČR (Sdružení místních samospráv ČR), which has
    run a joint purchasing procedure on the exchange since 2013, took the last one in July 2025
    for more than 200 subjects covering 1 Jan 2026 to 31 Dec 2027, is open to non-member obce
    and their schools and sports grounds, and absorbs the administrative work while the obec
    invoices the supplier directly — but it buys ENERGY, not solar arrays, so it does not hold
    this position. The other aggregation on file is structural, not commercial: SFŽP''s RES+
    rules themselves permit a sdružený project spanning multiple connection points across up to
    three mutually neighbouring municipalities, which is a subsidy rule rather than a supplier.
    POSITIVE CONTROL PASSED, and run before any conclusion was drawn: the same method aimed at
    SAKO Brno''s "36 FVE" framework surfaced its own E-ZAK tender page
    (zakazky.sako.cz/contract_display_128.html, the URL [S4] already carries) plus trade
    coverage of the city solar programme behind it — so the method does surface a Czech
    municipal-solar player that is known to exist. NOT FOUND IS NOT ABSENT: this is recorded as
    coverage, and a negative never raises a gap score by itself. gap moves 0 to 1 on the
    positive finding instead — the players this sweep and [S4] name are all early or are buyers
    aggregating for themselves, so none of them closed the space, which is rung 1 and not
    rung 0.'
  url: https://www.smscr.cz/benefity/spolecny-nakup-energii-na-burze/
  date: '2026-08-25'
  queries:
    - "sdružené zadávání fotovoltaika pro obce společný nákup FVE agregace poptávky měst dodavatel na klíč"
    - "\"společný nákup\" OR \"hromadná poptávka\" fotovoltaika obce města platforma služba sdružení zadavatelů Česko"
    - "SAKO Brno rámcová dohoda 36 FVE fotovoltaické elektrárny městské části Brno zakázka"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-23'
created: '2026-08-13'
updated: '2026-08-25'
---

Between June and August 2026, 53 distinct Czech public buyers went to market for rooftop photovoltaics — towns, regional governments, school and hospital organisations, a zoo, wastewater plants — generating ~80 TED records worth roughly €60M [S1]. Almost every lot is a bespoke design-build tender for a standard product: panels on a public roof, sized €120k to €1M, with its own documentation, its own evaluation, its own contract administration [S1].

Why now: subsidy programs (RES+ under the Modernizační fond) keep pushing municipal PV money out on fixed call deadlines [S4], so the tenders keep coming — and the fragmentation cost is documented in the procurement record itself. Špindlerův Mlýn published the same WWTP PV tender three times in ten weeks; Hrabová and Nymburk re-ran identical lots [S2]. Small lots struggle to attract bidders at all [S2], while every re-run burns administrative months against subsidy clocks.

Who pays: municipalities, through procurement overhead and failed procedures on lots too small to interest efficient suppliers [S2]; the state, through subsidy administration of hundreds of micro-projects; and ultimately the energy transition's schedule. A standardized, aggregated route — fixed-price design-build against a catalogue specification, or dynamic purchasing across many municipalities — is what the fragmentation implies.

Existing non-solutions: the aggregation answer partly exists, but nobody sells it. Brno pools its city districts through SAKO's "36 FVE" framework, kraje package their own buildings (Královéhradecký ran design-build packages 3 through 5 in this window), and RES+ permits a joint project across up to three neighbouring municipalities [S4,S6]. Each of those is a buyer aggregating for itself, or a subsidy rule. What is actually sold is turnkey design-build, pitched to towns one at a time [S6]. The nearest pooling service is SMS ČR, running joint energy purchasing for obce since 2013 — but it buys electricity, not solar arrays [S6]. None of it reaches the long tail: 53 buyers still tendered alone in one summer [S1].

No buyer-side complaint is documented, so the case rests on ~€60M a quarter of duplicated small-lot procurement — a measured, recurring inefficiency [S1]. The supply side has now been searched in Czech, and the pooling operator a town without its own framework could hire does not appear to exist here [S6]. A documented complaint from the municipal side is the evidence still missing.

Solved elsewhere: iChoosr has run the group-buying model from the Netherlands since 2008 — demand pooled into one tendered contract, with more than 200 UK councils running it as Solar Together [S5]. Its own site lists ten operating countries, Poland, Germany and Austria among them, though with no participant figures for any [S5]. One proven operator, in Western Europe, doing precisely what Czech one-by-one municipal buying does not.

## Revisions


2026-08-25 · rewrite, then re-scoring — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker were untouched by those passes. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 0 → 2. iChoosr passes the maturity test — selling since 2008, with 2.5M+ households served and 200+ UK councils running Solar Together — so rung 0, "no foreign solution on file", was simply wrong while that comparable sat on the ledger. First, though, the comparable was given the receipt SCORING.md requires: it had NO `sources[]` entry at all, and no point may rest on the comps ledger alone, so ichoosr.com was fetched live on this date and [S5] appended with what it does and does not say. Rung 3 was considered and declined. It needs establishment in two-plus markets with one CEE-adjacent, and the receipted traction sits in the Netherlands and Britain; Poland, Germany and Austria appear only as entries in a country list on the company's own site, with no participant figure behind any of them. `scores.gap` stays 0, and this is the one dimension on this file where the new ladder does not fit cleanly — FLAGGED rather than forced. Rung 0 reads "an ESTABLISHED local player already sells this", and what [S4] actually found is not a seller: SAKO Brno runs the "36 FVE" framework for Brno\'s own city districts, the kraje package their own buildings, and RES+ is a subsidy line. SAKO was lifted into `locals[]` as established on the named-customer limb, with the evidence line saying outright that it aggregates for its owner rather than selling to anyone else. On the face of the ladder that reads like rung 1, contested. It is NOT scored there, because gap authority is asymmetric and [S4] is a thin check with no `queries[]`, no `checked[]` and no positive control — there is no evidence either way about whether a Czech aggregation vendor exists, and an unrun search can never raise a score. So that sweep was run on this same date, in Czech, and [S6] records it. It looked for the iChoosr shape — an operator pooling many towns' lots into one tendered fixed-price contract — and did not find one. What it found selling is turnkey design-build pitched to towns one at a time (iKomunita, LAMBDA Energy, SVP Solar, Panomik, Fotovolty, LAMA Solar, Energie Soláry, reWATT, SEFY), plus SMS ČR, which has genuinely aggregated since 2013 and took its last joint purchase in July 2025 for more than 200 subjects — but buys ENERGY, not solar arrays. RES+'s sdružený project, spanning up to three neighbouring municipalities, is a subsidy rule rather than a supplier. POSITIVE CONTROL PASSED before any conclusion was drawn: the same method aimed at SAKO's "36 FVE" framework returned its own E-ZAK tender page, the URL [S4] already carries. `scores.gap` 0 → 1, and NOT on the not-found. Gap authority is asymmetric and a failure to find can never raise a score, so the 1 rests on the positive finding instead: every local player now named — SAKO, the kraje, the installers, SMS ČR — is either a buyer aggregating for its own owner or a seller of something else, and none of them is an established local player that already sells this. That is rung 1, contested and still enterable, and rung 0 was simply the wrong reading of what [S4] found. Rung 2 was NOT taken even though the sweep was properly formed with recorded `queries[]`, `checked[]` and a passing positive control: rung 2 means no local player found, and [S6] found several. SAKO stays in `locals[]`, moved to `early` with its guessed 2018 `since` removed rather than invented — no sourced year for the start of the framework is on file. `score` 3 → 6. Money, urgency and demand untouched; no existing source note edited and no existing [Sn] marker moved — [S5] and [S6] are appended, not inserted.
2026-08-20 · evidence audit — Removed SMO ČR from the next-evidence proposal. Neither "Svaz měst" nor "SMO ČR" returns any hit in the signal corpus, and the association appears in no source note here — a named institution proposed as a demand source with nothing on file to say it is one. The proposal still stands, without pre-naming who would file the complaint.
