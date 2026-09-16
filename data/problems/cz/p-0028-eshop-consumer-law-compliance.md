---
id: p-0028
region: cz
title: 'Czech e-shops were fined 13M CZK last year for breaking consumer law'
solution: 'Build an e-shop add-on that scans a shop''s checkout and "eco" claims weekly and sends the owner a fix list.'
brief: 'Inspectors found breaches in 85% of e-shops they checked, like missing complaint information or illegal order buttons [S1]. A Czech ban on vague "eco" claims is also moving through parliament [S13].'
good_for: 'Someone who''d like to work with small online shops and consumer law.'
category: retail-services
geo: CZ-national
score: 9
scores:
  proof: 3
  money: 0
  urgency: 3
  demand: 2
  gap: 1
status: candidate
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: open
  integration: software
  money: bootstrap
  why: 'Shops buy this themselves off the Shoptet add-on shelf, nothing licences a compliance scanner, and it runs as ordinary software. Every Czech seller found — Hlídač Slev, Slevy správně, Pravoid — has been trading under three years.'
comps:
- name: Trusted Shops
  url: https://www.trustedshops.com/
  geo: DE
  since: 1999
  traction: 'Trustmark + buyer protection on 17,000+ European shops incl. Zalando
    and Obi (Wikipedia); certification + legal-protection subscriptions'
  markets: [AT, CH, NL, ES, IT, FR, BE, PT, PL, GB]
- name: IT-Recht Kanzlei
  url: https://www.it-recht-kanzlei.de/
  geo: DE
  since: 2004
  traction: 'Subscription legal texts from €9.90/mo, Premium €24.90/mo for 5 presences
    (it-recht-kanzlei.de); Shopware/JTL/PrestaShop plugins'
- name: Händlerbund
  url: https://www.haendlerbund.de/
  geo: DE
  since: 2008
  traction: '30,000 members, ~92,000 digital presences (own data Mar 2026, via Wikipedia);
    legal texts, Abmahnung defense, Käufersiegel seal'
locals:
- name: Hlídač Slev (JARABOT)
  url: https://doplnky.shoptet.cz/hlidac-slev
  ico: '22571299'
  since: 2025
  competes: direct
  maturity: early
  evidence: It sells reference-price rewriting for the 30-day discount rule, keeping three years
    of history a shop can export for the trade inspectorate [S8,S10] — the same compliance job
    as this space, one duty wide. JARABOT s.r.o. has traded only since 10 February 2025 and publishes
    no count of shops using it; its five Shoptet ratings average 3.4 [S10].
- name: Slevy správně (Cenový automat)
  url: https://doplnky.shoptet.cz/slevy-spravne
  ico: '07641346'
  since: 2023
  competes: direct
  maturity: early
  evidence: It sells the same reference-price correction for the 30-day rule, at a flat 200 Kč
    a month [S8,S10]. The product dates to the 6 Jan 2023 rule it corrects for, it publishes no
    count of shops using it, and its four Shoptet ratings average 4.0 [S10].
- name: Pravoid
  url: https://www.pravoid.cz/
  ico: '23683368'
  since: 2025
  competes: direct
  maturity: early
  evidence: It sells generated legal texts at 199–499 CZK with a subscription that watches the
    e-Sbírka law gazette for changes [S8] — the monitoring shape this space calls for, aimed at
    the texts rather than the checkout. The proprietor Bc. Filip Krechler registered on 3 September
    2025, and no count of buyers is published.
- name: Právo e-shopů
  url: https://www.pravoeshopu.cz/pravni-audit-eshopu
  competes: adjacent
  maturity: early
  evidence: It sells one-off legal audits priced per engagement — a law firm doing the check by
    hand, which is the legacy service a subscription would replace rather than something a shop
    runs every week [S5]. No start year, no named buyers and no count are published.
- name: eLegal
  url: https://www.elegal.cz/
  ico: '03153398'
  since: 2014
  competes: adjacent
  maturity: early
  evidence: It sells one-off audits and terms drafting per engagement, as a law firm [S5] — the
    legacy service, not the monitoring product itself. Trading since 30 June 2014; it names nobody
    who has bought it and publishes no count, so how many shops it covers is unknown.
- name: AZ LEGAL
  url: https://www.azlegal.cz/
  ico: '05030323'
  since: 2016
  competes: adjacent
  maturity: early
  evidence: It sells one-off audits and terms drafting per engagement, as a law firm [S5] — the
    legacy service, not the monitoring product itself. Trading since 27 April 2016; it names nobody
    who has bought it and publishes no count, so how many shops it covers is unknown.
sources:
- type: complaint
  name: "ČOI — 2025 distance-selling inspection results"
  gist: "the 85% violation baseline"
  why: "751 e-shop inspections, violations in 639 of them, 2,399 individual breaches and ~13.0M CZK in fines — the Czech compliance baseline, itemised by failure type."
  url: https://www.sos-msk.cz/z-751-kontrol-e-shopu-porusilo-zakon-85-z-nich-padly-pokuty-za-temer-13-milionu-korun/
  note: 'coi-eshopy-2025: ČOI''s 2025 distance-selling results — 751 e-shop inspections, violations
    in 639 (85%), 2,399 individual breaches, ~13.0M CZK in fines across 646 closed cases.
    Top failures: missing complaint-handling information (363), unfair commercial practices
    (318), missing pre-contractual information (488), non-compliant order buttons (107). Enforcement
    continues as a 2026 priority: Q2/2026 risk-targeted inspections found a 91% violation
    rate; Q1/2026 discount-labelling checks ~40%. Recurring, annually documented non-compliance:
    demand 2.'
  date: '2026-02-26'
  signal: coi-eshopy-2025
- type: regulation
  name: "Empowering Consumers for the Green Transition — Directive (EU) 2024/825"
  gist: "the green-claims ban and its date"
  why: "The EU directive that blacklists generic green claims, unverified sustainability labels and unsubstantiated durability promises, which member states must apply from 27 September 2026. In Czechia it arrives through an amendment to the consumer-protection act that has not yet passed."
  url: https://eur-lex.europa.eu/eli/dir/2024/825/oj/eng
  note: 'reg-green-claims-ecgt: Empowering Consumers for the Green Transition Directive (2024/825)
    applies from 27 Sep 2026 — generic green claims (''eco'', offset-based ''climate neutral''),
    unverified sustainability labels and unsubstantiated durability claims are blacklisted;
    ČOI enforces via zákon o ochraně spotřebitele. Every e-shop making environmental claims
    must substantiate or strip them within weeks of this record''s creation. Deadline <18mo
    and the wider UCP regime is already in active enforcement: deadline sub-score 2, urgency
    3 with freshness.'
  date: '2026-09-27'
  signal: reg-green-claims-ecgt
- type: complaint
  name: "MPO — consumer disputes over goods and warranties"
  gist: "the 18,000 consumer disputes"
  why: "~18,000 out-of-court dispute filings with ČOI between 2020 and mid-2025 — the consumer-side receipt that the violations inspectors find correspond to real-world harm."
  url: https://mpo.gov.cz/assets/cz/ochrana-spotrebitele/aktualni-informace/2026/3/Zprava-o-prubeznem-plneni-Strategie-spotrebitelske-politiky-2025.pdf
  note: 'mpo-adr-vyuziti: MPO''s consumer-policy report tabulates ~18,000 ČOI out-of-court
    dispute filings 2020-H1/2025 (defective goods and warranties) — the consumer-side receipt
    that the violations ČOI finds correspond to recurring real-world harm. The same report
    documents ČOI running ~20,000 inspections/yr on an inflation-eroded budget: enforcement
    is risk-targeted, so violation rates in targeted sweeps keep rising.'
  date: '2026-03-31'
  signal: mpo-adr-vyuziti
- type: arbitrage
  name: "Trusted Shops and IT-Recht Kanzlei"
  gist: "the two German templates"
  why: "Two durable German businesses built on productised e-commerce legal compliance — certification with buyer protection, and subscription legal texts kept current for tens of thousands of shops."
  url: https://www.trustedshops.com/
  note: 'Named analogs: Trusted Shops (Cologne) built a durable DE/EU business productizing
    e-commerce trust and legal compliance (certification + Abmahnschutz legal-text service),
    and IT-Recht Kanzlei runs subscription legal-text compliance for tens of thousands of
    DE shops — the productized model is proven in the CEE-adjacent market where enforcement
    pressure (Abmahnung culture) preceded Czechia''s. Named analogs without a fresh funding
    receipt: proof 1.'
  date: '2026-08-13'
- type: gap-check
  name: "Czech e-shop compliance scan (first pass)"
  gist: "the first Czech field scan"
  why: "The early look at the Czech field: supply was legal services priced per audit — Právo e-shopů, eLegal, AZ LEGAL — with Shoptet's merchant base treated as a distribution channel."
  url: https://www.pravoeshopu.cz/pravni-audit-eshopu
  note: 'Gap check 2026-08-13: the CZ supply side is legal services priced per audit — Právo
    e-shopů, eLegal, AZ LEGAL and peers sell one-off právní audity and terms drafting; no
    Czech compliance-monitoring SaaS mapped to ČOI enforcement priorities (information duties,
    buttons, discount labelling, green claims) was found. Shoptet''s ~30k-merchant ecosystem
    is a distribution channel, not a compliance product. Gap 1 (quick search, services-only
    incumbents named).'
  date: '2026-08-13'
- type: complaint
  name: "MPO — ČOI enforcement capacity"
  gist: "the shrinking inspectorate"
  why: "Inspections fell from ~29,000 in 2018 to ~20,000 in 2023 on an inflation-eroded budget with staff down 9% — the reason enforcement went risk-targeted, and hit rates rose."
  url: https://mpo.gov.cz/assets/cz/ochrana-spotrebitele/aktualni-informace/2026/3/Zprava-o-prubeznem-plneni-Strategie-spotrebitelske-politiky-2025.pdf
  note: 'mpo-dozor-kapacita: the same MPO progress report (p.24-25) documents ČOI inspections
    falling from ~29,000 (2018) to ~20,000 (2023) on a nominally flat budget (~408M CZK in
    2023 against 411M CZK in 2018) eroded by inflation, with staff down 9% while complaint
    volume and new duties grew; the European Commission is cited naming underfunding the main
    barrier to effective enforcement, with CZ below the EU average in inspectors per 1M inhabitants.
    The capacity receipt behind the shift to risk-targeted sweeps.'
  date: '2026-03-31'
  signal: mpo-dozor-kapacita
- type: subsidy
  name: "OP TAK — Technologie pro MAS II"
  gist: "the 50% software grant"
  why: "50% co-funding for software and IT at rural SMEs, 540M CZK allocated, applications 1 Sep 2026 to 1 Sep 2027 — a channel to halve the price for merchants outside the big cities."
  url: https://apiagentura.gov.cz/cs/podporovane-aktivity-optak/technologie-pro-mas-optak/technologie-pro-mas-clld-vyzva-ii/
  note: 'dotace-optak-technologie-mas-2: OP TAK Technologie pro MAS II funds new machinery,
    software and IT for small rural firms via local action groups — 540M CZK (~€22M) allocated,
    grants up to 1.49M CZK at a 50% rate on eligible costs of 250k-3M CZK, for SMEs in MAS
    territories outside Prague and cities over 25,000 inhabitants; applications run 2026-09-01
    to 2027-09-01. The co-funding channel against the merchant-side price objection, not a
    receipt for this record''s money score.'
  date: '2026-09-01'
  signal: dotace-optak-technologie-mas-2
- type: gap-check
  name: "Hlídač Slev and Pravoid"
  gist: "the Czech products already selling"
  why: "The Czech-language sweep that found productised compliance already selling on Shoptet: Hlídač Slev on discount labelling with ČOI-exportable price history, and Pravoid on generated legal texts with legislative alerts."
  url: https://doplnky.shoptet.cz/hlidac-slev
  note: 'Gap re-check 2026-08-20: OCCUPIED. Looked for a Czech productized (not per-audit)
    offering mapped to the ČOI enforcement buckets this record lists — information duties,
    order buttons, discount labelling, green claims — and for subscription legal texts on
    the IT-Recht Kanzlei model. Found two Czech products. Hlídač Slev, by JARABOT s.r.o.
    (IČO 22571299, Praha 9, confirmed in ARES), is a Shoptet add-on that monitors prices
    daily, rewrites the reference price so discounts satisfy the 30-day lowest-price rule,
    keeps a 3-year price history and exports it for ČOI inspections, at roughly 19 CZK per
    month per 1,000 products — a compliance product sitting on the Shoptet store this record
    called a distribution channel with nothing on it. Pravoid (Bc. Filip Krechler, IČO 23683368,
    confirmed in ARES) generates terms and conditions, a privacy policy and a cookie policy
    from a questionnaire for Shoptet, WooCommerce, Shopify, PrestaShop and others, at 199 CZK
    per document or 499 CZK for the bundle, with a Pravoid Guard subscription that watches
    e-Sbírka for legislative changes and alerts when a document needs reissuing. NOT found:
    any Czech product covering the green-claims wave of 27 Sep 2026, missing pre-contractual
    or complaint-handling information, or order-button texts, and the Shoptet catalogue still
    has no legal-compliance category. Verdict: the claim "no Czech compliance-monitoring SaaS
    mapped to ČOI enforcement priorities" does not survive — discount labelling is exactly
    such a priority and is covered. De-rank rule applied: gap 0 with incumbents named, status
    watching.'
  date: '2026-08-20'
  queries:
    - "software hlídání právní compliance e-shopu obchodní podmínky kontrola ČOI monitoring"
    - "generátor obchodních podmínek pro e-shop předplatné právní texty aktualizace Shoptet doplněk"
    - "právní texty pro e-shop předplatné hlídání legislativy aktualizace obchodních podmínek služba Česko"
    - "nástroj kontrola e-shopu soulad se zákonem tlačítko objednávky sleva nejnižší cena 30 dní zelená tvrzení"
    - "Czech e-commerce legal compliance SaaS terms generator subscription Shoptet merchants"
  checked: [google-cz, cz-saas-directories, ares, own-funded-ledger]
  expires: '2026-11-18'
- type: complaint
  name: "ČOI — Q2/2026 e-shop inspection results"
  gist: "the 91% quarter"
  why: "103 inspections, violations in 94 of them, 414 breaches and 4.88M CZK of fines in a single quarter — the 2025 baseline has not moved."
  url: https://www.itbiz.cz/ceska-obchodni-inspekce-uskutecnila-ve-druhem-ctvrtleti-103-kontrol-internetovych-obchodu-poruseni-predpisu-zjistila-v-94-kontrolach/
  note: 'ČOI Q2/2026 e-shop results (release carried 12 Aug 2026): 103 inspections 1 Apr-30
    Jun 2026, violations in 94 (91.26%), 414 individual breaches, 159 fines totalling 4,878,500
    CZK legally binding in the quarter; top failures again complaint-handling information (61)
    and unfair commercial practices (52). Appended by the 2026-08-24 audit as the direct receipt
    for the 91% risk-targeted rate, which the body had cited to the 2025 results page — a page
    that carries only 2025 figures.'
  date: '2026-08-12'
- type: gap-check
  name: "Slevy správně — the add-on marketplace sweep"
  gist: "the 606-add-on sweep"
  why: "A pass over 606 Shoptet and Upgates add-ons. It found a second discount-labelling product at 200 Kč a month, and confirmed nothing in either marketplace covers green claims, information duties or order buttons."
  url: https://doplnky.shoptet.cz/slevy-spravne
  note: 'Mechanical re-check 2026-08-24 against the add-on lookup corpus (data/lookup/cz-eshop-addons.jsonl,
    606 add-ons across Shoptet and Upgates): the discount-labelling slot holds a SECOND Czech
    product this record did not name — Slevy správně by Cenový automat s.r.o. (cenovyautomat.cz),
    200 Kč/month flat for unlimited products, records prices every 6 hours, keeps a 3-year
    history as podklady pro ČOI, auto-corrects reference prices per the 6 Jan 2023 rule including
    the postupné-snižování variants, listed on Shoptet (4 ratings, 4.0) AND Upgates. The same
    sweep re-confirms the residual absences: no add-on in either marketplace covers green claims,
    pre-contractual or complaint-handling information, or order buttons, and Hlídač Slev''s
    corpus entry reads 5 ratings at 3.4. Gap already 0; occupancy deepened, nothing rescored.'
  date: '2026-08-24'
  queries:
    - "sleva nejnižší cena 30 dní hlídání referenční ceny ČOI"
    - "obchodní podmínky právní texty přístupnost zelená tvrzení tlačítko objednávky doplněk"
  checked: [eshop-addon-marketplaces]
  expires: '2026-11-22'
- type: price
  url: https://doplnky.shoptet.cz/hlidac-slev
  name: "Hlídač Slev — the discount-labelling add-on"
  gist: "about 19 Kč a month"
  why: "A Czech online shop pays about 19 CZK a month for every 1,000 products to keep its discount labelling legal and exportable for inspectors."
  note: 'Price receipt lifted from the 2026-08-20 gap re-check already on this ledger, which
    read the Shoptet listing: roughly 19 CZK per month per 1,000 products. The seat is a
    1,000-product block, which payer and why both state. Pravoid at 199 CZK per document or
    499 CZK for the bundle sits in the same note but its own url is not on this record, so it
    is not written as a receipt here. dims omitted: backs no score.
    Verified 2026-09-04: the Shoptet listing still states Za 1 000 produktů (včetně
    variant) zaplatíte 19 Kč měsíčně, with 100 Kč of credit given free to try it.'
  date: '2026-08-20'
  payer: 'A Czech online shop, per 1,000 products'
  amount_czk: 19
  unit: per-seat-month
  basis: list-price
- type: price
  url: https://doplnky.shoptet.cz/slevy-spravne
  name: "Slevy správně — the flat-rate rival"
  gist: "200 Kč a month, flat"
  why: "A second Czech add-on charges an online shop 200 CZK a month flat, whatever the number of products, for the same discount-labelling duty."
  note: 'Price receipt lifted from the 2026-08-24 add-on marketplace sweep already on this
    ledger, which read the Shoptet listing for Slevy správně by Cenový automat s.r.o.:
    200 Kč/month flat for unlimited products. Flat monthly, so the seat is the shop.
    dims omitted: backs no score.
    Verified 2026-09-04: the Shoptet listing still states Jednotná cena 200 Kč /m pro
    neomezený počet produktů, billed alongside the Shoptet tarif.'
  date: '2026-08-24'
  payer: 'A Czech online shop, any number of products'
  amount_czk: 200
  unit: per-seat-month
  basis: list-price
- type: regulation
  name: "Sněmovní tisk 53 — the Czech green-claims bill"
  gist: "the Czech law, not yet passed"
  why: "The government bill amending the consumer-protection act and the civil code to bring in the EU green-claims rules. It passed second reading on 24 June 2026; since then only a committee position has followed, with no third reading, Senate vote or publication."
  url: https://www.psp.cz/sqw/historie.sqw?o=10&T=53
  note: 'psp.cz bill history for sněmovní tisk 53, Novela z. o ochraně spotřebitele - EU, status
    page dated 16 Sep 2026, read 2026-09-16. Government submitted 8 Dec 2025; first reading 25 Mar
    2026; Hospodářský výbor resolutions 17 Apr 2026 (53/1, adjourned) and 18 May 2026 (53/2,
    amendments); second reading, general and detailed debate, 24 Jun 2026, amendments printed as
    53/3 on 26 Jun 2026; committee position 53/4 delivered 4 Sep 2026, further debate possible from
    5 Sep 2026. No third reading, no Senate stage, not published. The government draft (53/0,
    EU-compatibility table) set general effect on 31 Jul 2026 and 27 Sep 2026 for the Directive
    2024/825 provisions; whether 53/2 or 53/3 moved those dates was not read. The same table quotes
    Directive 2024/825 Art. 4(1): adopt and publish by 27 Mar 2026, apply from 27 Sep 2026.'
  date: '2026-09-04'
- type: news
  name: "Pravano — EmpCo in Czech law"
  gist: "the missed transposition deadline"
  why: "A Czech compliance publisher's explainer, cross-checked against primary sources on 28 July 2026: Czechia missed the 27 March 2026 deadline, the new bans do not yet apply in Czech law as such, and ČOI can already pursue green claims as misleading practices under the current act."
  url: https://pravano.cz/empco/baze/empco-transpozice-cr/
  note: 'pravano.cz EMPCO báze, "Směrnice EmpCo (2024/825) v českém právu: novela ZOS a dozor ČOI",
    published and modified 2026-07-28, read 2026-09-16. States: ČR transpoziční lhůtu 27. března
    2026 zmeškala; tisk 53 (novela 634/1992 Sb. and 89/2012 Sb.) prošel druhým čtením 24. června
    2026, third reading not held as of the Chamber status of 7 Aug 2026; zákon není platný ani
    účinný; the per-se blacklist bans zatím formálně neplatí as separate offences, but green claims
    can be pursued today under the general ban on misleading commercial practices, which ČOI
    actively uses. Pravano itself offers a free EmpCo compliance check (prověrka), so it is also a
    possible local player on green claims; not assessed here. dims empty: backs no score.'
  date: '2026-07-28'
  dims: []
created: '2026-08-13'
updated: '2026-09-04'
---

ČOI — the Czech trade inspection authority — walked the checkout flows of 751 e-shops in 2025 and found 639 breaking the law: 2,399 violations, from missing complaint-handling and pre-contractual information to non-compliant order buttons [S1]. That 85% is the baseline, not a tail — targeted inspections in Q2 2026 found violations in 94 of 103 shops [S9].

Why now: an EU directive blacklists generic environmental claims, unverified sustainability labels and unsubstantiated durability promises, and member states must apply it from 27 September 2026 [S2]. Czechia missed the March 2026 deadline to write it into law [S14]: the amendment to the consumer-protection act passed second reading in June 2026 and still awaits a third reading, the Senate and publication [S13]. Once it passes, every shop running an "eko" or climate-neutral badge must substantiate it or strip it [S2]; ČOI can already pursue misleading green claims under the current act [S14]. ČOI's own inspections fell from ~29,000 a year to ~20,000 on a flat budget [S6], so it targets rather than samples.

Who pays: the merchants, because the alternative is a fine and inspectors now target the worst shops. Shoptet, a platform merchants rent their storefront from, hosts about 30,000 [S5]. Czech compliance add-ons charge 19 to 200 CZK a month [S8,S10]; the German subscriptions this copies run €9.90–24.90. Thirty thousand merchants, a €12 bundle over the uncovered duties, one in ten buying: about €430,000 a year, against ~13.0M CZK of ČOI fines in 2025 [S1].

Existing non-solutions: Právo e-shopů, eLegal and AZ LEGAL — three law firms — sell one-off audits per engagement [S5]. Discount labelling is taken twice: Hlídač Slev and Slevy správně both rewrite reference prices for the 30-day lowest-price rule and keep three years of ČOI-exportable history, at ~19 CZK and a flat 200 Kč a month [S8,S10]. Pravoid generates terms and privacy policies, with alerts when the law moves [S8]; its proprietor and Hlídač Slev's vendor both registered in 2025, and neither publishes a customer count [S8]. Nobody covers the rest of ČOI's map: green claims, information duties, order buttons [S8,S10].

Solved elsewhere: three German firms have lasted decades on this. Trusted Shops has sold certification with buyer protection since 1999 to 17,000+ European shops, Zalando and Obi among them, across eleven markets including Austria and Poland. IT-Recht Kanzlei has sold subscription legal texts since 2004, from €9.90 a month, with plugins for the major shop platforms. Händlerbund, trading since 2008, counts 30,000 members and some 92,000 digital presences [S4]. All three grew on fear of a warning letter; here the regulator supplies it. None carries a fresh funding round [S4] — two decades of paying customers is the receipt.

## First moves

1. Crawl Czech e-shops for green-claims language — "eko", "šetrné k přírodě", climate-neutral badges. That list is your prospect list: the EU directive blacklists unsubstantiated versions of exactly those claims from 27 September 2026 [S2], and the Czech law that brings the ban in is past its second reading [S13].
2. Pitch those merchants now with a claim-by-claim fix report, priced at the German subscription points listed under Proven abroad. The Czech ban has no start date until the law passes [S13], but ČOI can already pursue a misleading green claim under the current act [S14]. Whether a merchant buys before the fine arrives is the assumption everything here rests on — at 85–91% violation rates, ignoring the risk is what most of them already do [S1,S9].
3. Extend the scanner to the four failures ČOI writes up most: missing pre-contractual information (488 breaches in 2025), missing complaint-handling information (363), unfair commercial practices (318), non-compliant order buttons (107) [S1]. Those four are 1,276 of the 2,399 recorded violations, and each one is a checklist item.
4. Ship into the Shoptet add-on store, and expect company. Hlídač Slev sells there at ~19 CZK a month per 1,000 products, on five middling public ratings, with reviewers citing support and export accuracy [S8]; Slevy správně sells at a flat 200 Kč a month on Shoptet and Upgates [S10]. One integration still reaches tens of thousands of obligated shops [S5], and the catalogue has no legal-compliance category yet [S8,S10].
5. Let public money halve the price outside the cities: shops in MAS areas — the state's rural local-action-group territories, outside Prague and towns over 25,000 people — get software co-funded at 50%, grants up to 1.49M CZK, from [OP TAK Technologie pro MAS II](/sources/tenders#dotace-optak-technologie-mas-2) — the state's business-support programme — €22M allocated, applications 2026-09-01 to 2027-09-01 [S7].
6. Aim at the duties nobody sells. **Právo e-shopů, eLegal and AZ LEGAL** leave a shop compliant only until the next legislative wave [S5], and the three Czech products each cover one duty — **Hlídač Slev** and **Slevy správně** on discount labelling, **Pravoid** on legal texts with alerts from e-Sbírka, the state law gazette [S8,S10]. Both those vendors registered during 2025 [S8], so this is a race, not an entrenchment. The open ground is coverage: pre-contractual and complaint-handling information, order buttons, and the green claims the EU blacklists from 27 September 2026, once Czech law brings the ban in [S1,S2,S8,S10,S13].

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-20 · de-rank, gap re-check and evidence audit — Three blocks recorded on this date, merged here; the de-rank was written down twice and is stated once. The absence claim was re-run in Czech against google-cz, the Shoptet add-on catalogue and ARES, and it fails. Hlídač Slev (JARABOT s.r.o., IČO 22571299) sells automated discount-labelling compliance with ČOI-exportable price history on the Shoptet store — the very store this record described as carrying no compliance product — and Pravoid (IČO 23683368) sells generated legal texts with e-Sbírka change alerts across five e-shop platforms [S8]. Gap 1 → 0, score 7 → 6, status candidate → watching. Two specific sentences were rewritten rather than deleted, because their factual halves survive: first move 4 asserted the Shoptet ecosystem had "no compliance product on it" — it has one, whose public ratings are middling — and first move 6 asserted no ČOI-mapped monitoring SaaS existed. The unbuilt part is now specific rather than total: the green-claims wave landing 27 Sep 2026, pre-contractual and complaint-handling information, and order-button texts still have nothing Czech on them [S8], against an 85–91% violation baseline that has not moved [S1]. The enforcement evidence is untouched — the 85% and 91% violation rates, the 2,399 breaches and the capacity numbers are all receipted and unaffected [S1,S6]. Method control: the same search method was run first at Wultra (p-0017) and Softlink (p-0026); the funded-ledger grep returned round-wultra and a plain descriptive Czech query surfaced softlink.cz unprompted, so the method is known to produce positives before any negative here was trusted. The title carried the same disproved absence, "who have no compliance tooling", and has been cut: Hlídač Slev is compliance tooling, sold on the very platform this record described as carrying none. Cut in the same pass: the IT-Recht Kanzlei subscription price points in the second first move. Those figures exist only in the comps ledger — neither IT-Recht Kanzlei nor Trusted Shops appears in any signal, and the source note that names both companies gives no prices — and a comparable's traction line cannot back a body claim. The move now points at the ledger, which still prints the prices in full, and nothing removed by that audit has been reintroduced.

2026-08-24 · gap re-check and fact check — The mechanical sweep of the add-on lookup corpus found a second discount-labelling product this record did not name: Slevy správně by Cenový automat s.r.o., flat 200 Kč/month, 6-hour snapshots, 3-year ČOI history, on Shoptet and Upgates [S10]; the body and first moves 4 and 6 now carry it beside Hlídač Slev. The 91% risk-targeted rate had been cited to the 2025 results page, which carries only 2025 figures; the ČOI Q2/2026 release (103 inspections, 94 with violations) is now on the ledger and the claim re-cited [S9]. Cut in the same pass: "one of Europe's densest e-commerce markets", a density claim with no receipt in the corpus, and the clause tying this record to an accessibility "enforcement wave" at p-0020 — that record's enforcement claim failed verification on this date and it is rejected. The green-claims, pre-contractual, complaint-handling and order-button absences were re-confirmed against all 606 add-ons in both marketplaces [S10]. Gap stays 0; nothing rescored.

2026-08-25 · board-brief rewrite — The argument was cut from 529 words to the board-brief shape, one claim per sentence and at most two markers to a sentence, with no claim added beyond its sources and none removed: the 85% and 91% violation rates, the 2,399 breaches, the ČOI capacity numbers, the two discount-labelling incumbents and Pravoid all survive in shorter form. "How big" now states a bottom-up figure instead of gesturing at the long tail — ~30,000 Shoptet merchants [S5] against Czech add-on pricing of 19–200 CZK/month [S8,S10] and the German €9.90–24.90 subscription points, giving roughly €430k/yr at a €12 bundle and 10% penetration, set beside ~13.0M CZK of 2025 fines [S1]. The "Solved elsewhere:" lead-in was already present and is unchanged in function; the German analogs now state what each proves rather than being named in passing. Every source gained a public name and why line. Scores, status and internal notes untouched. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker were untouched by those passes. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, and both dimensions moved. `scores.proof` 1 → 3. The v1 answer, 1, was reasoned as "named analogs without a fresh funding receipt" — but a fresh round was never what proof measures, and under the maturity test all three German analogs pass on the customer limb without needing one: Trusted Shops selling since 1999 across 17,000+ European shops with Zalando and Obi named and eleven markets on its ledger including Austria and Poland, IT-Recht Kanzlei since 2004 with tens of thousands of shops on subscription, Händlerbund since 2008 with 30,000 members and ~92,000 digital presences [S4]. Established in two-plus markets with Germany, Austria and Poland all CEE-adjacent is rung 3. `scores.gap` 0 → 1, which is the correction that matters here. The 2026-08-20 pass dropped gap to 0 on the strength of finding two Czech products, and the 2026-08-24 pass found a third — but the new ladder asks how mature they are, and ARES answers plainly. JARABOT s.r.o., which sells Hlídač Slev, was registered 2025-02-10; Bc. Filip Krechler, the proprietor behind Pravoid, on 2025-09-03; both dates read live from ARES on this date against the IČOs [S8] already carried. Cenový automat's Slevy správně only just clears the three-year limb, dating to the January 2023 reference-price rule it corrects for, and clears no other: none of the three publishes a customer count, pairs with a public buyer in `data/lookup/cz-contract-parties.jsonl`, or carries a round or a state listing. An early local player does not close a space. The law firms behind the one-off audits — Právo e-shopů, eLegal (ARES 2014), AZ LEGAL (ARES 2016) — are the "weak or legacy incumbents" half of the same rung. Gap does not rise past 1: [S8] and [S10] found local players, not none, so rung 2 is unavailable however the check was run. All six were lifted from the [S5], [S8] and [S10] scan prose into a structured `locals[]` ledger. `score` 6 → 9. The non-solutions paragraph, the Proven-abroad paragraph and first move 6 now state the incumbents' ages, because that is the fact carrying the gap score, and the Proven-abroad paragraph stops treating an absent round as an absent proof. Nothing found in the earlier passes was removed: the coverage gaps that remain unbuilt — green claims from 27 Sep 2026, pre-contractual and complaint-handling information, order buttons — are unchanged and still cited [S8,S10]. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved. FLAGGED, NOT CHANGED: `status` is still `watching`, set by the SPEC §4 de-rank rule when gap went to 0 on 2026-08-20. The condition that triggered it no longer holds.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. Three entries stay `direct`, three move to `adjacent`, and no maturity changes. Hlídač Slev, Slevy správně and Pravoid each sell a slice of the same automated compliance job to the same shops, so they are direct, and each fails the established test on its own receipts. The three law firms — Právo e-shopů, eLegal and AZ LEGAL — move to `adjacent`: they sell one-off audits and terms drafting priced per engagement, which is the legacy service a subscription scanner would replace rather than the monitoring product itself. All three read early on receipts, so the relabel touches nothing. `scores.gap` stays 1 and now says the rung's own words: direct competitors exist here and every one of them is early. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 6 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

2026-09-02 · plain-language pass — Trade terms glossed at first use in the rendered prose: ČOI as the Czech trade inspection authority, Shoptet as a platform merchants rent their storefront from, MAS as the state's rural local-action-group territories, OP TAK Technologie pro MAS II as the state's business-support programme [S7], and e-Sbírka as the state law gazette [S8]. The argument tightened from 441 words to 390 with every [Sn] marker, figure, price and named company kept, First moves rewritten in the plain house voice, and a short gist added beside all ten sources' public why lines. No score, status, ledger entry or source note touched.

2026-09-04 · price receipt — The two discount-labelling add-ons already on file are now recorded as prices: about 19 CZK a month per 1,000 products [S11] and 200 CZK a month flat [S12]. The document prices of the third product stay in the note, its own page not being on this ledger. No score, status, ledger entry or source note touched.

2026-09-16 · headline copy — The headline was rewritten for a general builder as three lines under the title: a `brief:` on what is happening and why it matters now, the `solution:` as a call to action, and a new `good_for:` line. New copy, verbatim — title: "Most e-shops Czech inspectors check are breaking consumer law"; brief: "Last year inspectors fined e-shops about 13M CZK over breaches like missing complaint information and illegal order buttons [S1]."; solution: "Build an e-shop add-on that scans a shop's checkout and "eco" claims weekly and sends the owner a fix list."; good_for: "Someone who'd like to work with small online shops and consumer law.". Previous title, verbatim: "Most inspected Czech e-shops break consumer law". Previous solution, verbatim: "A weekly scanner for Czech online shops that checks the checkout, the prices and the product claims against consumer law and hands the merchant a fix list — on subscription, not as a one-off legal audit.". There was no previous brief or good_for. Corrected against the evidence before it was written, from the owner-reviewed draft, then cut to the owner's length limits. The draft title and brief said new "eco" claim rules "start 27 September" and that unproven claims "have to come down" from that day. The only source on file for the date is Directive (EU) 2024/825, which obliges member states to apply the ban from 27 September 2026 [S2]; no source on this record names a Czech law that brings it in. Checked on 2026-09-16: the Czech transposition is sněmovní tisk 53, amending zákon 634/1992 Sb. and the civil code; it passed second reading on 24 June 2026 and had not had its third reading, reached the Senate or been published (psp.cz bill history, latest event 4 September 2026; pravano.cz reports the 27 March 2026 transposition deadline missed). The date is therefore out of the copy entirely. "Millions of crowns" became the figure behind it, about 13M CZK in 2025 [S1]; ČOI does not break its fines down by breach type, so the breaches are named as examples found, not as what each fine was for. FLAGGED, NOT CHANGED: the body's Why-now paragraph and First moves 1, 2 and 6 still state that the green-claims rules apply and are enforced by ČOI from 27 September 2026 [S2]; with the Czech amendment still in the Chamber that reads as a Czech date it is not, and a source for the bill belongs on this ledger before the body is reworded. No score, status, source, note, marker or body sentence changed. Same date, body correction: the flagged lines are corrected. What was wrong, verbatim: Why now said "from 27 September 2026 the green-claims rules blacklist generic environmental claims … and ČOI enforces them" and "Every shop running an "eko" or climate-neutral badge must substantiate it or strip it"; First move 1 said "from 27 September 2026 the directive blacklists"; First move 2 said "Pitch those merchants before 27 September 2026"; First move 6 said "the green claims blacklisted from 27 September 2026"; and the public line of [S2] said the claims "are blacklisted, and ČOI enforces it". All of that reads as a date binding Czech shops. It binds member states [S2]. Evidence, read on this date: the psp.cz history of sněmovní tisk 53 shows second reading on 24 June 2026 and, as the last step, a committee position delivered on 4 September 2026, with no third reading, Senate vote or publication [S13]; the government draft set 27 September 2026 for these provisions, which the process can no longer meet. Pravano's explainer reports the 27 March 2026 transposition deadline missed, the new bans not yet in force in Czech law as such, and ČOI already able to pursue green claims as misleading practices under the current act [S14]. Both appended as [S13] and [S14]; [S14] backs no score. Changed: Why now gives the EU date as the member states' date, the bill's stage and the existing-act route, and the badge sentence is conditional on the law passing; First move 2 pitches now rather than before a date; First moves 1 and 6 attach the date to the EU and cite the bill; the why line of [S2] rewritten to match; its note left as written. Urgency stays 3, checked: its deadline half, 2, rested on the 27 September 2026 date [S2]. That date still stands as the EU compliance date, inside 18 months, and the Czech bill carrying it is at its last Chamber stage [S13]; rung 1, a date more than 18 months out, and rung 0, no trigger, would both be false. The ladder has no rung for a national date not yet set, so the prose now says it. Freshness holds on [S9] and [S13]. The updated date is not moved: only these sources were re-read. Same date, pain-point pass: the owner's new rule, that each headline names who is hurting and how, in plain words. Before, verbatim — title: "Most e-shops Czech inspectors check are breaking consumer law"; brief: "Last year inspectors fined e-shops about 13M CZK over breaches like missing complaint information and illegal order buttons [S1].". After, verbatim — title: "Czech e-shops were fined 13M CZK last year for breaking consumer law"; brief: "Inspectors found breaches in 85% of e-shops they checked, like missing complaint information or illegal order buttons [S1]. A Czech ban on vague "eco" claims is also moving through parliament [S13].". Why: the old title stated a violation rate, which is the inspectors' finding, not the shop owner's pain; the owner, who is the buyer of what `solution:` describes, feels the fine. The figure moves up from the old brief into the title: about 13.0M CZK of fines across the 2025 inspections, and 2025 is last year as of this pass [S1]. It is rounded to 13M and says "for breaking consumer law", not which breach, because ČOI does not split its fines by breach type. The brief then carries the one number the title lost, 85%, 639 of 751 inspections [S1], with the same two example breaches, and replaces the repeated fine with what is coming: the Czech green-claims bill, sněmovní tisk 53, is past second reading and still awaits a third reading, the Senate and publication [S13]. "Moving through parliament" states that stage and no Czech start date, because none is set. Solution and good_for unchanged. No score, status, source, note, marker or body sentence changed.
