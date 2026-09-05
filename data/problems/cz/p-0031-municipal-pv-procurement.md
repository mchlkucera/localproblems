---
id: p-0031
region: cz
title: Czech towns buy rooftop solar one by one, and overpay for it
fix: 'An aggregator that pools many towns'' rooftop-solar projects into one fixed-price
  contract, so the lots stop being too small for a supplier to bid on.'
price_search: 'Registr smluv full-text for "administrace zadávacího řízení" with "fotovoltaick"
  — what a town pays a procurement administrator to run one rooftop-solar tender is the manual
  equivalent of a pooling fee — and for "společný nákup energií" to see what SMS ČR members or
  eCENTRE customers pay for pooled commodity buying; otherwise ask the town clerk (tajemník) of
  Špindlerův Mlýn what its repeated tenders cost in administrator fees; the MS2021+ index under
  "fotovoltaick" returns only installation grants.'
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
  evidence: 'A municipal waste company that ran its own solar tender: it operates the "36 FVE"
    multi-district photovoltaic framework for the city districts of Brno [S4], aggregating for
    its own owner. It is a buyer of this service, not a seller of it, and it does not offer pooling
    to towns that have no framework of their own. SAKO Brno, a.s. has traded since 1 July 1994,
    and two separate public bodies pair with it as buyers on the state contracts register, verified
    live 2026-08-25.'
- name: SMS ČR (společný nákup energií)
  url: https://www.smscr.cz/benefity/spolecny-nakup-energii-na-burze/
  ico: '75130165'
  since: 2013
  competes: adjacent
  maturity: established
  evidence: It sells joint purchasing to towns and has done since 2013 — but what it pools is
    ENERGY bought on the exchange, not solar arrays, so it does not hold the pooled-procurement
    position a town without a framework would hire [S6]. Its July 2025 procedure ran for more
    than 200 participating customers covering 1 Jan 2026 to 31 Dec 2027, is open to non-member
    obce and their schools and sports grounds, and absorbs the administrative work while the town
    invoices the supplier directly [S6]. The association itself dates from 2008; the joint purchasing
    started in 2013.
- name: eCENTRE
  url: https://ecentre.cz/
  ico: '27149862'
  since: 2006
  competes: adjacent
  maturity: established
  evidence: 'It is the aggregation operator this problem is shaped like, selling the wrong commodity:
    it runs electronic auctions that pool the demand of many municipalities, households and firms
    into one negotiated contract, and it is the machinery behind the SMS ČR joint purchase. What
    it pools is electricity and gas — a meter reading, not a roof — and its own site offers no
    photovoltaic procurement of any kind [S7]. Its site names customers including Ostrava, Svitavy
    and Frýdlant nad Ostravicí, which dates the aggregated purchasing to 2006; eCENTRE, a.s. has
    traded since 12 May 2004 [S7].'
- name: iKomunita
  url: https://ikomunita.cz/fotovoltaika-mesta-obce/
  competes: adjacent
  maturity: early
  evidence: It sells one town a turnkey project — a feasibility study, then panels and a battery
    wired into a single managed system across that town's own buildings, aimed at self-sufficiency
    and a future energy community [S7]. It is a supplier answering a tender, which is the side
    of the table this problem is not on; it publishes no start year and names no town that has
    bought it.
- name: ADS Energy
  url: https://www.ads-energy.cz/cs/fotovoltaika/pro-obce/
  competes: adjacent
  maturity: early
  evidence: 'It sells design-build to municipalities and comes closest of the installers: it offers
    to build "solární elektrárny sdílené více obcemi", a plant several towns share [S7]. That
    is one shared ASSET, contracted the ordinary way — it does not pool many towns'' separate
    roof projects into one tendered fixed-price contract, which is the position nobody holds.
    It claims more than 200 completed projects but names no municipality and publishes no start
    year, so how much of that is municipal is unknown.'
- name: Enado
  url: https://www.enado.cz/fotovoltaika-obec/
  competes: adjacent
  maturity: early
  evidence: It sells photovoltaics and heat pumps to households, apartment buildings, firms and
    towns, and packages energy sharing for a municipality [S7] — a supply-and-install business
    selling into one town at a time, not procurement pooled across towns. It publishes no start
    year and names no town that has bought it.
- name: Grantex
  url: https://grantex.cz/
  competes: adjacent
  maturity: early
  evidence: 'It sells subsidy work: reading the RES+ and Modernizační fond calls for a town and
    getting its application through, including the joint-project rule that lets one applicant
    cover several connection points [S7]. It moves the paper, not the purchase — each town still
    runs its own tender at the end of it; no start year is published and it names no town that
    has hired it.'
sources:
- type: tender
  name: "TED — South Moravia rooftop PV (~€1.0M), and the wave around it"
  gist: "the €60M summer tender wave"
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
  gist: "three re-runs in ten weeks"
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
  gist: "the 2.5M CZK town contract"
  why: "The layer below the TED threshold: a town bundling build and ongoing servicing for photovoltaics on one municipal building."
  url: https://smlouvy.gov.cz/smlouva/38371366
  note: 'hlidac-38371366: Jindřichův Hradec signed a ~2.5M CZK works-and-service contract
    for PV on a municipal building (Jun 2026) — the below-TED-threshold layer of the same
    wave, bundling build with ongoing servicing town by town.'
  date: '2026-06-11'
  signal: hlidac-38371366
- type: gap-check
  name: "Brno's '36 FVE' framework and the aggregation channels"
  gist: "the channels that already pool"
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
  gist: "the Dutch group-buying operator"
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
  gist: "the Czech supply-side sweep"
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
  gist: "the third sweep, reconciled"
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
- type: tender
  name: "TED — Špindlerův Mlýn, still not built two months later"
  gist: "the saga continues into August"
  why: "The same wastewater-plant PV project that republished three times in June now needs its
    own building modified before the solar can go on — a fourth procurement action on one site,
    ten weeks turned two months."
  url: https://ted.europa.eu/en/notice/-/detail/568275-2026
  note: 'ted-568275-2026: Město Špindlerův Mlýn tendered construction work to modify its WWTP
    building so it can host the FVE plant (17 Aug 2026) — the same site as the triple-republished
    tender in [S2], still generating separate procurement actions two months on. No contract
    value published. Corroborates the procurement-friction claim already on file; does not move
    a score.'
  date: '2026-08-17'
  signal: ted-568275-2026
  dims: []
- type: tender
  name: "TED — Jince re-tenders its own solar, one day later"
  gist: "a second named town's repeat tender"
  why: "A second named town joins Špindlerův Mlýn, Hrabová and Nymburk in the repeat-tender
    pattern: Jince's own notice is titled 'opakované zadání' — re-issued tendering — one day
    after its first attempt."
  url: https://ted.europa.eu/en/notice/-/detail/591378-2026
  note: 'ted-591378-2026: Městys Jince re-issued its own municipal-building FVE tender
    ("opakované zadání", ~EUR 760k, 27 Aug 2026), one day after the first attempt on the same
    buildings (ted-589208-2026, same buyer, ~EUR 680k, 26 Aug 2026 — not separately linked, same
    underlying fact). A second named town in the repeat-tender pattern documented in [S2] for
    Špindlerův Mlýn/Hrabová/Nymburk. Corroborates the procurement-friction claim already on file;
    does not move a score.'
  date: '2026-08-27'
  signal: ted-591378-2026
  dims: []
- type: regulation
  name: "Zákon o obcích novela — společenství obcí as a shared-services platform"
  gist: "the buying vehicle, deepened"
  why: "The interior ministry's bill widens the společenství obcí — the municipal union this record's pooled tender would run through — into a shared-services platform with state-budget support behind it, proposed to take effect on 1 January 2027."
  url: https://odok.gov.cz/portal/services/download/attachment/KORNDWGFEZO3/
  note: 'reg-obce-spolecenstvi-sdilene-agendy: Závěrečná zpráva RIA to the interior ministry
    bill amending act 128/2000 (obce), the draft the scripted feed holds as
    veklep-ALBSDRFEKCIO; the RIA attachment is cited rather than the material page. Authorised
    2026-02-19, government-approved package dated 2026-07-30, proposed effective 01/2027, ex-post
    RIA after five years. Substance used here: the společenství obcí is deepened into a platform
    for pooling agendas a small municipality cannot run alone, with state-budget support, plus a
    new register of voluntary municipal associations (3–5m CZK to build, ~1.2m CZK a year to run)
    and a public register of mayors. RIA facts: 6,254 municipalities averaging 1,710 inhabitants
    against an OECD average of 10,250 and an EU average of 5,960; median 442; 96% under 5,000;
    average area 13 km2 against an OECD 234; public-administration costs 63.1bn CZK in 2022; a
    TAČR DEA analysis (TL01000463) puts peak relative efficiency at 10,000–50,000 inhabitants and
    the společenství formed so far average 21,700, inside that band. This dates and strengthens
    the buying vehicle First moves step 2 already names off [S7]; it is a change to the pooling
    instrument, not a compliance duty on the buyer, so it is filed as context and moves no score.
    Runner-up considered and rejected: p-0029, whose product is the attested records system, not
    joint procurement.'
  date: '2027-01-01'
  signal: reg-obce-spolecenstvi-sdilene-agendy
  dims: []
created: '2026-08-13'
updated: '2026-09-03'
---

Between June and August 2026, 53 Czech public buyers — towns, regions, schools, hospitals, a zoo, wastewater plants — ran about 80 separate rooftop-solar tenders worth roughly €60M [S1]. Almost every lot is a bespoke design-build tender for a standard product: panels on a public roof, €120k to €1M, each with its own documentation, evaluation and contract [S1].

Why now: RES+ (the state's renewable-energy subsidy line, from the Modernizační fond) pays municipal solar money out on fixed call deadlines, so the tenders keep coming [S4]. Špindlerův Mlýn published the same wastewater-plant solar tender three times in ten weeks; Hrabová and Nymburk re-ran identical lots [S2]. Small lots struggle to attract bidders, and every re-run burns months against a subsidy clock [S2].

Who pays: municipalities pay in procurement overhead and failed procedures on lots too small to interest an efficient supplier [S2]. The state pays again, administering subsidies for hundreds of micro-projects.

Existing non-solutions: towns do get pooled, but nobody sells the pooling. Brno pools its city districts through one framework for 36 photovoltaic plants ("36 FVE"), run by SAKO — the city's waste company; regions package their own buildings; RES+ permits a joint project across up to three neighbouring municipalities [S4,S6]. Each is a buyer aggregating for itself, or a subsidy rule. iKomunita, ADS Energy and Enado each sell one town a turnkey installation (design, panels, battery); Grantex sells the subsidy paperwork [S7]. eCENTRE pools hundreds of towns into one electricity and gas auction, including the purchase run for SMS ČR — the small-municipalities association — but sells no solar procurement [S6,S7]. 53 buyers still tendered alone in one summer [S1].

No buyer-side complaint is documented, so the case rests on ~€60M a quarter of duplicated small-lot procurement [S1]. No company sells that pooling to a town without a framework of its own [S6,S7].

Solved elsewhere: iChoosr has pooled demand into single tendered contracts from the Netherlands since 2008, and more than 200 British councils run it as Solar Together [S5]. Its site lists ten operating countries — Poland, Germany and Austria among them — with no participant figures for any [S5].

## First moves

1. Sell first to the towns whose tenders have already failed. Špindlerův Mlýn published the same wastewater-plant solar tender three times in ten weeks; Hrabová and Nymburk re-ran identical lots [S2]. Each has a subsidy clock running and a lot too small to interest a supplier. They are the cheapest first customers in the wave.
2. Build the pooled tender, not an installation business. One catalogue specification, one fixed price per installed kilowatt, many towns' roofs inside a single procedure — the model iChoosr has run from the Netherlands since 2008 and more than 200 British councils buy as Solar Together [S5]. No new law is needed. RES+ already permits a joint project spanning up to three neighbouring municipalities, and the společenství obcí — municipal unions created by the 2024 amendment to the municipalities act — may buy centrally for their members, through a framework agreement or a dynamic purchasing system (a standing list of pre-qualified suppliers) [S7]. That vehicle is about to get stronger: a further amendment, proposed to take effect on 1 January 2027, turns the společenství into a shared-services platform with state-budget support, in a country of 6,254 municipalities averaging 1,710 inhabitants against an average of 10,250 across the OECD — the club of developed economies [S10].
3. Open the first conversation with the size of the duplication. Between June and August 2026, 53 public buyers ran about 80 separate rooftop-solar procurements worth roughly €60M, most lots between €120k and €1M, each carrying its own documentation, its own evaluation and its own contract administration [S1].
4. Watch eCENTRE, and move first. It pools municipalities, households and firms into one negotiated contract, runs the SMS ČR joint purchase, names Ostrava, Svitavy and Frýdlant nad Ostravicí as customers, and has aggregated buying since 2006 [S7]. What it pools is electricity and gas, and its site offers no solar procurement at all [S7]. It is one product decision away.

## Revisions


2026-08-25 · rewrite, then re-scoring — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker were untouched by those passes. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 0 → 2. iChoosr passes the maturity test — selling since 2008, with 2.5M+ households served and 200+ UK councils running Solar Together — so rung 0, "no foreign solution on file", was simply wrong while that comparable sat on the ledger. First, though, the comparable was given the receipt SCORING.md requires: it had NO `sources[]` entry at all, and no point may rest on the comps ledger alone, so ichoosr.com was fetched live on this date and [S5] appended with what it does and does not say. Rung 3 was considered and declined. It needs establishment in two-plus markets with one CEE-adjacent, and the receipted traction sits in the Netherlands and Britain; Poland, Germany and Austria appear only as entries in a country list on the company's own site, with no participant figure behind any of them. `scores.gap` stays 0, and this is the one dimension on this file where the new ladder does not fit cleanly — FLAGGED rather than forced. Rung 0 reads "an ESTABLISHED local player already sells this", and what [S4] actually found is not a seller: SAKO Brno runs the "36 FVE" framework for Brno\'s own city districts, the kraje package their own buildings, and RES+ is a subsidy line. SAKO was lifted into `locals[]` as established on the named-customer limb, with the evidence line saying outright that it aggregates for its owner rather than selling to anyone else. On the face of the ladder that reads like rung 1, contested. It is NOT scored there, because gap authority is asymmetric and [S4] is a thin check with no `queries[]`, no `checked[]` and no positive control — there is no evidence either way about whether a Czech aggregation vendor exists, and an unrun search can never raise a score. So that sweep was run on this same date, in Czech, and [S6] records it. It looked for the iChoosr shape — an operator pooling many towns' lots into one tendered fixed-price contract — and did not find one. What it found selling is turnkey design-build pitched to towns one at a time (iKomunita, LAMBDA Energy, SVP Solar, Panomik, Fotovolty, LAMA Solar, Energie Soláry, reWATT, SEFY), plus SMS ČR, which has genuinely aggregated since 2013 and took its last joint purchase in July 2025 for more than 200 subjects — but buys ENERGY, not solar arrays. RES+'s sdružený project, spanning up to three neighbouring municipalities, is a subsidy rule rather than a supplier. POSITIVE CONTROL PASSED before any conclusion was drawn: the same method aimed at SAKO's "36 FVE" framework returned its own E-ZAK tender page, the URL [S4] already carries. `scores.gap` 0 → 1, and NOT on the not-found. Gap authority is asymmetric and a failure to find can never raise a score, so the 1 rests on the positive finding instead: every local player now named — SAKO, the kraje, the installers, SMS ČR — is either a buyer aggregating for its own owner or a seller of something else, and none of them is an established local player that already sells this. That is rung 1, contested and still enterable, and rung 0 was simply the wrong reading of what [S4] found. Rung 2 was NOT taken even though the sweep was properly formed with recorded `queries[]`, `checked[]` and a passing positive control: rung 2 means no local player found, and [S6] found several. SAKO stays in `locals[]`, moved to `early` with its guessed 2018 `since` removed rather than invented — no sourced year for the start of the framework is on file. `score` 3 → 6. Money, urgency and demand untouched; no existing source note edited and no existing [Sn] marker moved — [S5] and [S6] are appended, not inserted.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. SAKO Brno moves `early` → `established` at `competes: adjacent`, and gains the `since` an earlier pass had to delete. That pass removed a guessed 2018 rather than invent one, which was right; a sourced year is now on file instead of a guess — ARES gives SAKO Brno, a.s. a date of incorporation of 1994-07-01, fetched live on this date — and the maturity limb is machine-counted rather than asserted, with two distinct public buyers for IČO 60713470 in `data/lookup/cz-contract-parties.jsonl`. The evidence line keeps saying the thing a builder needs: SAKO aggregates for its own owner, so it is a buyer of this service and not a seller of it. SMS ČR was ADDED under the no-exclude ruling. [S6] already named it as the nearest thing to a pooling operator — joint purchasing for obce since 2013, more than 200 subjects in the July 2025 procedure, open to non-members — and it sat in the argument while the ledger showed a single row. It records as adjacent because what it pools is electricity, not solar arrays, which is precisely why it does not hold this position. `scores.gap` stays 1: an adjacent player never moves it, at any maturity. The checker's warning that nothing on the ledger is `competes: direct` is correct and is left standing — rung 2 is the arguable score here and belongs to the owner, not to a content pass. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

FOURTH PASS THIS DATE, MERGED HERE: the two contradictory checks on this file were reconciled and `scores.gap` 1 → 2, `score` 6 → 7. The contradiction was real and readable on the page: [S4] closes "Field not empty: gap 0 with channels named" while the file scored 1, so a reader following the citation reached the opposite conclusion from the scorecard. [S4] cannot be edited and has not been. It is superseded instead, in [S7] and here, and the reason it was wrong is worth keeping: it found CHANNELS — SAKO's framework for Brno's own districts, kraj packaging, an SFŽP subsidy rule — and read them as sellers. A channel is not a vendor. [S7] is a third sweep with four Czech query shapes and a positive control run and passed BEFORE any conclusion was drawn: a query phrased as an obec hunting for joint purchasing returned the SMS ČR page already on this ledger and, beside it, eCENTRE, a.s. — the auction house that actually runs that purchase and appeared on no record anywhere in the register. The method surfaces Czech pooled-procurement operators that exist, so its negative carries weight, and the negative is that nobody sells the iChoosr position here. FIVE PLAYERS ADDED under the no-exclude rule: eCENTRE (IČO 27149862, established on named customers — Ostrava, Svitavy, Frýdlant nad Ostravicí — pooling electricity and gas since 2006), which is the aggregation operator this problem is shaped like, selling the wrong commodity and one product decision from the right one; iKomunita, ADS Energy and Enado, which sell design-build into a single town; and Grantex, which sells subsidy administration. ADS Energy is the closest call on the ledger and its line says so — it offers to build a solar plant several towns share, which is one shared asset contracted the ordinary way, not many towns' separate lots pooled into one tendered contract. Two structural channels were also confirmed and are named in [S7] without entering the ledger, because neither is a company anybody can hire: the RES+ joint-project rule, and the společenství obcí created by the 2024 amendment to the municipalities act, which may act as a central purchasing body for its members through a framework agreement or a dynamic purchasing system. SAKO's evidence line dropped the repository filename it used to print to the reader. The non-solutions prose now names the installers and eCENTRE, and the hedge "does not appear to exist here" is gone — three sweeps is a finding, not an impression. Proof, money, urgency and demand untouched; no existing source note edited and no existing [Sn] marker moved — [S7] is appended, not inserted.

2026-08-20 · evidence audit — Removed SMO ČR from the next-evidence proposal. Neither "Svaz měst" nor "SMO ČR" returns any hit in the signal corpus, and the association appears in no source note here — a named institution proposed as a demand source with nothing on file to say it is one. The proposal still stands, without pre-naming who would file the complaint.

THE LEDGER NOTES, IN PLAIN LANGUAGE. All 7 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

FIRST MOVES WRITTEN. `data/RECORD-TEMPLATE.md` reserves the section for records scoring >= 7 and this file scores 7; it was simply missing, which cost the reader the most actionable thing on the page. Four moves, each drawn from evidence already on the record: the towns whose lots have already failed to close as the first customers [S2], a pooled tender run on the two vehicles that already exist in Czech law [S5,S7], the 53 buyers and ~80 duplicate procurements as the opening fact [S1], and eCENTRE named as the aggregation operator one commodity away [S7]. No new fact was introduced, no source note was edited and no [Sn] marker was moved.

2026-09-02 · plain-language pass — Glossed at first use: SAKO as Brno's waste company, "36 FVE" as its 36-plant framework [S4], SMS ČR as the small-municipalities association [S6], RES+ as the state's renewable-energy subsidy line. TED, WWTP, PV, obce, kraje and UK replaced with plain words. Argument cut 448 to 352 words, every [Sn] marker, figure and company kept. First moves rewritten verbs-first; a gist added to all seven sources. No score, status, note: field or marker touched.
