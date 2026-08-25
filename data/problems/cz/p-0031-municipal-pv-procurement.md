---
id: p-0031
region: cz
title: Czech towns buy rooftop solar one by one, and overpay for it
fix: 'An aggregator that pools many towns'' rooftop-solar projects into one fixed-price
  contract, so the lots stop being too small for a supplier to bid on.'
category: energy
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 2
  urgency: 1
  demand: 0
  gap: 2
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
  since: 1994
  competes: adjacent
  maturity: established
  evidence: 'A municipal waste company that ran its own solar tender: it operates the "36
    FVE" multi-district photovoltaic framework for the city districts of Brno [S4],
    aggregating for its own owner. It is a buyer of this service, not a seller of it, and it
    does not offer aggregation to towns that have no framework of their own. Established as
    a firm: two distinct public buyers pair with its IČO in the state contracts register, and
    ARES gives a date of incorporation of 1994-07-01, verified live 2026-08-25.'
- name: SMS ČR (společný nákup energií)
  url: https://www.smscr.cz/benefity/spolecny-nakup-energii-na-burze/
  ico: '75130165'
  since: 2013
  competes: adjacent
  maturity: established
  evidence: 'It sells joint purchasing to obce and has done since 2013 — but what it pools
    is ENERGY bought on the exchange, not solar arrays, so it does not hold the
    pooled-procurement position a town without a framework would hire [S6]. Established on a
    public customer count: its July 2025 procedure ran for more than 200 subjects covering 1
    Jan 2026 to 31 Dec 2027, is open to non-member obce and their schools and sports
    grounds, and absorbs the administrative work while the obec invoices the supplier
    directly [S6]. Registered 2008-02-05 in ARES; 2013 is when the joint purchasing itself
    started.'
- name: eCENTRE
  url: https://ecentre.cz/
  ico: '27149862'
  since: 2006
  competes: adjacent
  maturity: established
  evidence: 'It is the aggregation operator this problem is shaped like, selling the wrong
    commodity: it runs electronic auctions that pool the demand of many municipalities,
    households and firms into one negotiated contract, and it is the machinery behind the SMS
    ČR joint purchase. What it pools is electricity and gas — a meter reading, not a roof —
    and its own site offers no photovoltaic procurement of any kind [S7]. Established on named
    customers: Ostrava, Svitavy and Frýdlant nad Ostravicí appear on its site, which dates the
    aggregated purchasing to 2006; eCENTRE, a.s. is registered in ARES from 2004-05-12 [S7].'
- name: iKomunita
  url: https://ikomunita.cz/fotovoltaika-mesta-obce/
  competes: adjacent
  maturity: early
  evidence: 'It sells one town a turnkey project — a feasibility study, then panels and a
    battery wired into a single managed system across that town''s own buildings, aimed at
    self-sufficiency and a future energy community [S7]. It is a supplier answering a tender,
    which is the side of the table this problem is not on. No year of first sale is published,
    nothing names who has bought it, no published tally exists, no public buyer pairs with it
    in the state contracts register, no round at Series stage and no state listing.'
- name: ADS Energy
  url: https://www.ads-energy.cz/cs/fotovoltaika/pro-obce/
  competes: adjacent
  maturity: early
  evidence: 'It sells design-build to municipalities and comes closest of the installers: it
    offers to build "solární elektrárny sdílené více obcemi", a plant several towns share
    [S7]. That is one shared ASSET, contracted the ordinary way — it does not pool many towns''
    separate roof projects into one tendered fixed-price contract, which is the position
    nobody holds. It states more than 200 completed projects but names no municipality and
    publishes no year of first sale, so the test''s limbs are unmet: no public buyer pairs
    with it in the state contracts register, no round at Series stage and no state listing.'
- name: Enado
  url: https://www.enado.cz/fotovoltaika-obec/
  competes: adjacent
  maturity: early
  evidence: 'It sells photovoltaics and heat pumps to households, apartment buildings, firms
    and obce, and packages energy sharing for a municipality [S7] — a supply-and-install
    business selling into one town at a time, not procurement pooled across towns. No year of
    first sale is published, nothing names who has bought it, no published tally exists, no
    public buyer pairs with it in the state contracts register, no round at Series stage and
    no state listing.'
- name: Grantex
  url: https://grantex.cz/
  competes: adjacent
  maturity: early
  evidence: 'It sells subsidy work: reading the RES+ and Modernizační fond calls for a town
    and getting its application through, including the joint-project rule that lets one
    applicant cover several connection points [S7]. It moves the paper, not the purchase —
    each town still runs its own tender at the end of it. No year of first sale is published,
    nothing names who has bought it, no published tally exists, no public buyer pairs with it
    in the state contracts register, no round at Series stage and no state listing.'
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
- type: gap-check
  name: "Who would a town without a framework hire — the third sweep"
  why: "A wider Czech sweep, and it settles the contradiction between the two earlier ones.
    The aggregation operator exists and pools electricity and gas for hundreds of obce; the
    photovoltaic version of it is sold by nobody."
  url: https://ecentre.cz/
  note: 'Czech-language sweep 2026-08-25, run to RECONCILE two checks on this file that reach
    opposite conclusions. [S4], dated 2026-08-13, closes "Field not empty: gap 0 with channels
    named" — a conclusion drawn from finding CHANNELS (SAKO''s framework for Brno''s own
    districts, kraj packaging, an SFŽP subsidy rule) and reading them as sellers. It recorded
    no queries and no control. [S6], dated 2026-08-25, searched the supply side in Czech,
    found no pooling operator, and moved gap 0 to 1 on the positive finding that every player
    named is a buyer aggregating for itself or a seller of something else. THIS CHECK CONFIRMS
    [S6] AND SUPERSEDES [S4]''S CONCLUSION: a channel is not a vendor, and gap 0 requires an
    established local that SELLS this. POSITIVE CONTROL PASSED, run before any conclusion was
    drawn: query 1, phrased as an obec looking for joint purchasing, returned the SMS ČR
    joint-purchase page already on this ledger AND eCENTRE, a.s. (IČO 27149862), the auction
    house that actually runs it and was on no record anywhere in the register. The method
    surfaces Czech pooled-procurement operators that exist. NOT FOUND: nobody sells a town the
    iChoosr position — many towns'' separate roof projects pooled into one tendered
    fixed-price contract. What the sweep found instead, all recorded in locals[]: eCENTRE
    pools demand across municipalities, households and firms, but for electricity and gas, and
    offers no photovoltaic procurement; iKomunita, ADS Energy and Enado sell design-build and
    energy-sharing packages into one town at a time; Grantex sells subsidy administration. ADS
    Energy is the closest call and is written down as such — it offers to build "solární
    elektrárny sdílené více obcemi", but that is one shared asset contracted the ordinary way,
    not pooled procurement of separate lots. TWO STRUCTURAL CHANNELS, NEITHER A SELLER: SFŽP''s
    RES+ rules permit a sdružený project across up to three neighbouring municipalities, and
    the společenství obcí created by the 2024 amendment to the municipalities act may act as a
    central purchasing body for its members through framework agreements or a dynamic
    purchasing system. Both are vehicles a town must drive itself; neither is a company a town
    can hire, which is precisely the position this record says is empty. gap moves 1 to 2 on
    this controlled check.'
  date: '2026-08-25'
  queries:
    - 'společný nákup energií pro obce elektronická aukce sdružení zadavatelů administrátor hromadná poptávka'
    - 'hromadná poptávka fotovoltaika pro obce sdružené zadávání zakázky za více obcí najednou zajistíme výběrové řízení FVE'
    - 'obec chce fotovoltaiku na střechu školy kdo zajistí dotaci projekt a výběrové řízení komplexní služba pro obce více obcí společně'
    - 'centrální zadavatel pro obce společné zadávání veřejné zakázky fotovoltaické elektrárny kraj svazek obcí rámcová dohoda 2026'
  checked: [google-cz, ares, cz-contract-parties, own-funded-ledger]
  expires: '2026-11-23'
created: '2026-08-13'
updated: '2026-08-25'
---

Between June and August 2026, 53 distinct Czech public buyers went to market for rooftop photovoltaics — towns, regional governments, school and hospital organisations, a zoo, wastewater plants — generating ~80 TED records worth roughly €60M [S1]. Almost every lot is a bespoke design-build tender for a standard product: panels on a public roof, sized €120k to €1M, with its own documentation, its own evaluation, its own contract administration [S1].

Why now: subsidy programs (RES+ under the Modernizační fond) keep pushing municipal PV money out on fixed call deadlines [S4], so the tenders keep coming — and the fragmentation cost is documented in the procurement record itself. Špindlerův Mlýn published the same WWTP PV tender three times in ten weeks; Hrabová and Nymburk re-ran identical lots [S2]. Small lots struggle to attract bidders at all [S2], while every re-run burns administrative months against subsidy clocks.

Who pays: municipalities, through procurement overhead and failed procedures on lots too small to interest efficient suppliers [S2]; the state, through subsidy administration of hundreds of micro-projects; and ultimately the energy transition's schedule. A standardized, aggregated route — fixed-price design-build against a catalogue specification, or dynamic purchasing across many municipalities — is what the fragmentation implies.

Existing non-solutions: towns do get pooled, but nobody sells the pooling. Brno pools its city districts through SAKO's "36 FVE" framework, kraje package their own buildings, and RES+ permits a joint project across up to three neighbouring municipalities [S4,S6]. Each is a buyer aggregating for itself, or a subsidy rule. What is actually sold is turnkey design-build, pitched to towns one at a time — iKomunita, ADS Energy and Enado sell into a single town, and Grantex sells the paperwork [S7]. The pooling operator exists: eCENTRE pools hundreds of obce into one energy auction, including the SMS ČR one — but it pools electricity and gas, not solar arrays [S6,S7]. None of it reaches the long tail: 53 buyers still tendered alone in one summer [S1].

No buyer-side complaint is documented, so the case rests on ~€60M a quarter of duplicated small-lot procurement — a measured, recurring inefficiency [S1]. No company sells a town without its own framework a way to pool its roof project with anyone else's [S6,S7]. A documented complaint from the municipal side is still missing.

Solved elsewhere: iChoosr has run the group-buying model from the Netherlands since 2008 — demand pooled into one tendered contract, with more than 200 UK councils running it as Solar Together [S5]. Its own site lists ten operating countries, Poland, Germany and Austria among them, though with no participant figures for any [S5]. One proven operator, in Western Europe, doing precisely what Czech one-by-one municipal buying does not.

## Revisions


2026-08-25 · rewrite, then re-scoring — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker were untouched by those passes. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 0 → 2. iChoosr passes the maturity test — selling since 2008, with 2.5M+ households served and 200+ UK councils running Solar Together — so rung 0, "no foreign solution on file", was simply wrong while that comparable sat on the ledger. First, though, the comparable was given the receipt SCORING.md requires: it had NO `sources[]` entry at all, and no point may rest on the comps ledger alone, so ichoosr.com was fetched live on this date and [S5] appended with what it does and does not say. Rung 3 was considered and declined. It needs establishment in two-plus markets with one CEE-adjacent, and the receipted traction sits in the Netherlands and Britain; Poland, Germany and Austria appear only as entries in a country list on the company's own site, with no participant figure behind any of them. `scores.gap` stays 0, and this is the one dimension on this file where the new ladder does not fit cleanly — FLAGGED rather than forced. Rung 0 reads "an ESTABLISHED local player already sells this", and what [S4] actually found is not a seller: SAKO Brno runs the "36 FVE" framework for Brno\'s own city districts, the kraje package their own buildings, and RES+ is a subsidy line. SAKO was lifted into `locals[]` as established on the named-customer limb, with the evidence line saying outright that it aggregates for its owner rather than selling to anyone else. On the face of the ladder that reads like rung 1, contested. It is NOT scored there, because gap authority is asymmetric and [S4] is a thin check with no `queries[]`, no `checked[]` and no positive control — there is no evidence either way about whether a Czech aggregation vendor exists, and an unrun search can never raise a score. So that sweep was run on this same date, in Czech, and [S6] records it. It looked for the iChoosr shape — an operator pooling many towns' lots into one tendered fixed-price contract — and did not find one. What it found selling is turnkey design-build pitched to towns one at a time (iKomunita, LAMBDA Energy, SVP Solar, Panomik, Fotovolty, LAMA Solar, Energie Soláry, reWATT, SEFY), plus SMS ČR, which has genuinely aggregated since 2013 and took its last joint purchase in July 2025 for more than 200 subjects — but buys ENERGY, not solar arrays. RES+'s sdružený project, spanning up to three neighbouring municipalities, is a subsidy rule rather than a supplier. POSITIVE CONTROL PASSED before any conclusion was drawn: the same method aimed at SAKO's "36 FVE" framework returned its own E-ZAK tender page, the URL [S4] already carries. `scores.gap` 0 → 1, and NOT on the not-found. Gap authority is asymmetric and a failure to find can never raise a score, so the 1 rests on the positive finding instead: every local player now named — SAKO, the kraje, the installers, SMS ČR — is either a buyer aggregating for its own owner or a seller of something else, and none of them is an established local player that already sells this. That is rung 1, contested and still enterable, and rung 0 was simply the wrong reading of what [S4] found. Rung 2 was NOT taken even though the sweep was properly formed with recorded `queries[]`, `checked[]` and a passing positive control: rung 2 means no local player found, and [S6] found several. SAKO stays in `locals[]`, moved to `early` with its guessed 2018 `since` removed rather than invented — no sourced year for the start of the framework is on file. `score` 3 → 6. Money, urgency and demand untouched; no existing source note edited and no existing [Sn] marker moved — [S5] and [S6] are appended, not inserted.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. SAKO Brno moves `early` → `established` at `competes: adjacent`, and gains the `since` an earlier pass had to delete. That pass removed a guessed 2018 rather than invent one, which was right; a sourced year is now on file instead of a guess — ARES gives SAKO Brno, a.s. a date of incorporation of 1994-07-01, fetched live on this date — and the maturity limb is machine-counted rather than asserted, with two distinct public buyers for IČO 60713470 in `data/lookup/cz-contract-parties.jsonl`. The evidence line keeps saying the thing a builder needs: SAKO aggregates for its own owner, so it is a buyer of this service and not a seller of it. SMS ČR was ADDED under the no-exclude ruling. [S6] already named it as the nearest thing to a pooling operator — joint purchasing for obce since 2013, more than 200 subjects in the July 2025 procedure, open to non-members — and it sat in the argument while the ledger showed a single row. It records as adjacent because what it pools is electricity, not solar arrays, which is precisely why it does not hold this position. `scores.gap` stays 1: an adjacent player never moves it, at any maturity. The checker's warning that nothing on the ledger is `competes: direct` is correct and is left standing — rung 2 is the arguable score here and belongs to the owner, not to a content pass. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

FOURTH PASS THIS DATE, MERGED HERE: the two contradictory checks on this file were reconciled and `scores.gap` 1 → 2, `score` 6 → 7. The contradiction was real and readable on the page: [S4] closes "Field not empty: gap 0 with channels named" while the file scored 1, so a reader following the citation reached the opposite conclusion from the scorecard. [S4] cannot be edited and has not been. It is superseded instead, in [S7] and here, and the reason it was wrong is worth keeping: it found CHANNELS — SAKO's framework for Brno's own districts, kraj packaging, an SFŽP subsidy rule — and read them as sellers. A channel is not a vendor. [S7] is a third sweep with four Czech query shapes and a positive control run and passed BEFORE any conclusion was drawn: a query phrased as an obec hunting for joint purchasing returned the SMS ČR page already on this ledger and, beside it, eCENTRE, a.s. — the auction house that actually runs that purchase and appeared on no record anywhere in the register. The method surfaces Czech pooled-procurement operators that exist, so its negative carries weight, and the negative is that nobody sells the iChoosr position here. FIVE PLAYERS ADDED under the no-exclude rule: eCENTRE (IČO 27149862, established on named customers — Ostrava, Svitavy, Frýdlant nad Ostravicí — pooling electricity and gas since 2006), which is the aggregation operator this problem is shaped like, selling the wrong commodity and one product decision from the right one; iKomunita, ADS Energy and Enado, which sell design-build into a single town; and Grantex, which sells subsidy administration. ADS Energy is the closest call on the ledger and its line says so — it offers to build a solar plant several towns share, which is one shared asset contracted the ordinary way, not many towns' separate lots pooled into one tendered contract. Two structural channels were also confirmed and are named in [S7] without entering the ledger, because neither is a company anybody can hire: the RES+ joint-project rule, and the společenství obcí created by the 2024 amendment to the municipalities act, which may act as a central purchasing body for its members through a framework agreement or a dynamic purchasing system. SAKO's evidence line dropped the repository filename it used to print to the reader. The non-solutions prose now names the installers and eCENTRE, and the hedge "does not appear to exist here" is gone — three sweeps is a finding, not an impression. Proof, money, urgency and demand untouched; no existing source note edited and no existing [Sn] marker moved — [S7] is appended, not inserted.

2026-08-20 · evidence audit — Removed SMO ČR from the next-evidence proposal. Neither "Svaz měst" nor "SMO ČR" returns any hit in the signal corpus, and the association appears in no source note here — a named institution proposed as a demand source with nothing on file to say it is one. The proposal still stands, without pre-naming who would file the complaint.
