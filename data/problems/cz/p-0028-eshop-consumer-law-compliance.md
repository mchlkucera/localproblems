---
id: p-0028
region: cz
title: 'Many Czech e-shops break consumer rules without realising it, and any inspection can end in a fine'
solution: 'Build an e-shop add-on that scans a shop''s checkout and "eco" claims weekly and sends the owner a fix list.'
brief: 'Inspectors caught 639 e-shops last year, usually for missing notices a shopper must see, like how to complain [S1]. Fines average about 20,000 CZK, and nothing checks a shop before the inspectors do [S1,S10].'
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
  why: 'Easier: shops install add-ons themselves from the Shoptet store, the Czech sellers are young and publish no customer counts, no licence is needed, and it runs as ordinary software. Harder: most shops live with the risk of a fine rather than pay to remove it, and the Czech ban on vague "eco" claims has no start date.'
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
  since: 2023
  competes: direct
  maturity: early
  evidence: It sells reference-price rewriting for the 30-day discount rule, keeping three years
    of history a shop can export for the trade inspectorate [S8,S10] — the same compliance job
    as this space, one duty wide. Its Shoptet listing carries ratings from January 2023, so the
    add-on has sold since then, although the company now behind it, JARABOT s.r.o., was registered
    only on 10 February 2025 [S8]. It publishes no count of shops using it; its five Shoptet ratings
    average 3.4 [S10]. Its reviewers split over
    its support and the accuracy of its price export [S8].
- name: Slevy správně (Cenový automat)
  url: https://doplnky.shoptet.cz/slevy-spravne
  ico: '07641346'
  since: 2023
  competes: direct
  maturity: early
  evidence: It sells the same reference-price correction for the 30-day rule, at a flat 200 Kč
    a month [S8,S10]. The product dates to the 6 Jan 2023 rule it corrects for, it publishes no
    count of shops using it, and its four Shoptet ratings average 4.0 [S10]. It is also sold on
    Upgates, a second Czech shop platform [S10].
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
    demand 2.
    Corrected 2026-09-19: this page, dated 26 Feb 2026, carries only 2025 figures and the line that
    e-shops stay a ČOI priority in 2026. Neither 2026 rate above is on it: the Q2/2026 91% has its
    own receipt at S9, and the Q1/2026 ~40% (652 discount-labelling checks, per the signal) has no
    receipt on this record and is not claimed. Demand 2 stands on the 2025 results, S3 and S9.'
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

In 2025 Czech inspectors found breaches at 639 of the 751 e-shops they checked, 2,399 breaches in all [S1].

- 488 breaches were missing information a buyer must get before ordering [S1].
- 363 were missing information on how to make a complaint [S1].
- 318 were unfair practices, meaning misleading or aggressive selling [S1].

The inspectors work for ČOI (the Czech trade inspection authority) [S1]. They mostly checked shops already suspected of breaking the law, on a shopper's tip or from their own monitoring [S1]. So 85% is the rate among the shops they chose, not among all Czech e-shops [S1].

- 107 breaches were order buttons that were missing or not labelled as an order with a duty to pay [S1].
- Those four kinds make up 1,276 of the 2,399 breaches [S1].
- Breaking the law is the norm among the shops inspectors check, and 2026 has been no better; see [Why now](#why-now) [S9].
- Shoppers also took about 18,000 disputes over faulty goods and warranties to ČOI's out-of-court process between 2020 and mid-2025 [S3].

Existing non-solutions: Czech products each cover one duty and law firms audit a shop once, and no add-on checks green claims, order buttons or missing information [S5,S8,S10].

Two add-ons on the Shoptet store keep a shop's discounts legal under the 30-day rule, which says a discount is counted from the lowest price of the previous 30 days [S8,S10]. Each rewrites the price a discount is measured from, and keeps three years of price history a shop can export for inspectors [S8,S10]. Their prices are under [Willing to pay](#willing-to-pay).

- A third product writes a shop's terms and conditions, privacy policy and cookie policy from a questionnaire [S8]. Its subscription watches e-Sbírka, the state law gazette, and tells the shop when a change in the law means a document must be redone [S8].
- The companies behind two of the three were registered in 2025, and none of the three says how many shops use it [S8,S10]. So the field is still a race, not a settled market.
- Three Czech law firms sell one-off legal audits and terms drafting, priced per job [S5]. An audit checks a shop once, so it goes out of date at the next change in the law.
- None of the 606 add-ons listed on Shoptet and Upgates, two Czech shop platforms, checks green claims, order buttons, or the information a shop must give before an order or about complaints [S10].
- Shoptet's add-on store has no legal-compliance category [S8,S10].
- Outside the add-on stores, a Czech publisher of an explainer on the new green-claims rules offers a free check against them; whether it sells more is not known [S14].

Why now: E-shop owners pay fines now, and a Czech ban on vague "eco" claims is making its way through parliament [S9,S13].

- E-shops took 159 final fines, 4.88M CZK in all, in April–June 2026 alone [S9].
- Inspectors target suspected shops, and 94 of 103 checked then broke the law [S9].
- Shops with "eco" badges must prove or remove them once the bill passes [S2,S13].

Those 94 shops had 414 breaches between them, most often missing complaint information, 61 times, and unfair practices, 52 times [S9]. ČOI says checking e-shops stays a priority in 2026 [S1].

- ČOI can already act against a misleading green claim under today's consumer-protection act, before the ban [S14].
- ČOI's inspections fell from about 29,000 in 2018 to about 20,000 in 2023, and its staff shrank by 9% [S6]. Its budget stayed at about 410M CZK while prices rose [S6].
- So the inspectors now pick the shops most likely to be in breach, and more of the shops they check are caught [S6].

The ban comes from an EU directive, No. 2024/825, which the Czech bill writes into the consumer-protection act and the civil code [S2,S13]. It bans generic green claims such as "eco", "climate neutral" claims that rest on offsetting, sustainability labels nobody has verified, and durability promises without proof [S2]. The dates:

- On 27 March 2026 Czechia missed the EU's deadline to adopt the rules [S14].
- On 24 June 2026 the Czech bill, number 53 in the Chamber of Deputies, passed its second reading [S13].
- On 1 September 2026 the state's software grant for rural small firms opened for applications [S7].
- On 4 September 2026 a committee gave its position on the bill, and no third reading, Senate vote or publication has followed [S13].
- On 27 September 2026 every EU member state must start applying the ban [S2].
- On 1 September 2027 the rural software grant stops taking applications [S7].
- Until the bill passes, no Czech start date for the ban is binding [S13].

Who pays: Some shops already pay for single fixes: a monthly add-on for the discount rule, or a law firm's one-off audit [S5,S10].

- Two Czech add-ons charge shops a monthly fee to keep discounts legal [S8,S10].
- E-shops were handed 646 final fines worth about 13.0M CZK in 2025 [S1].
- Tens of thousands of German shops pay monthly for legal texts kept current [S4].

The add-ons' prices are in the table of what one buyer pays. Law firms charge per job for one-off audits; see [Competition](#competition) [S5].

- Shoptet, a platform shops rent their storefront from, hosts about 30,000 of them, so one add-on there can reach many [S5].
- A rough estimate: if one in ten of those 30,000 shops paid €12 a month for one bundle covering the duties no add-on covers, that would bring about €430,000 a year [S5]. The €12 sits inside the German subscription prices under [Validated abroad](#validated-abroad), and the sum compares with the 13.0M CZK of fines in 2025 [S1].
- Shops outside the big cities can get half the cost of new software paid by a state grant, OP TAK Technologie pro MAS II (a call of the state's business-support programme) [S7].

The grant holds 540M CZK, about €22M, for machinery, software and IT at small firms [S7]. It pays 50% of eligible costs, up to 1.49M CZK per grant [S7]. Only projects with eligible costs of 250,000 CZK to 3M CZK qualify, so a monthly add-on alone is too small [S7]. Only firms in the areas of rural local action groups, called MAS, can apply, outside Prague and outside towns of more than 25,000 people [S7]. Its dates are under [Why now](#why-now).

Solved elsewhere: German firms have sold e-shop legal compliance as a product for decades, one of them to tens of thousands of shops [S4].

One sells a trust mark with buyer protection, plus legal texts that guard a shop against warning letters [S4]. Another sells legal texts by subscription and keeps them current as the law changes [S4]. Their years, prices, markets and customer counts are in their rows.

In Germany the pressure is the warning letter, a lawyer's formal demand to stop a breach; in Czechia the state inspectors supply it [S4]. None of them has raised a recent funding round, and the proof is their years of paying customers [S4].

## First moves

1. Build a scanner that lists every "eco" or climate-neutral claim on a Czech e-shop that the coming ban would forbid unless proven. Run it across Czech shops for words like "eko" and "šetrné k přírodě" and for climate-neutral badges, and the shops it flags are your first prospects. The EU requires its member states to ban such claims, and the Czech law that does it is on its way through parliament; see [Why now](#why-now). Inspectors can already treat a misleading green claim as a misleading practice under today's law, so the list is useful before the ban starts.
2. Send each flagged shop owner a claim-by-claim report of what to prove or remove, and offer to keep it current for a monthly fee. The Czech ban has no start date until the bill passes, but inspectors can already act against a misleading green claim, as [Why now](#why-now) explains. Price it near what German shops pay for legal texts kept current, listed under [Validated abroad](#validated-abroad). This move tests the assumption everything here rests on: that a shop owner pays before a fine arrives, when most shops inspectors check already live with the risk; see [The opportunity](#opportunity).
3. Add checks for the breaches inspectors find most often: missing pre-order information, missing complaint information, unfair selling practices and non-compliant order buttons. Together they make up more than half of all breaches found, as [The opportunity](#opportunity) shows, and each is a checklist item a weekly scan can test. No add-on checks them, and a law firm's audit checks a shop once and goes out of date at the next change in the law; see [Competition](#competition). The Czech add-ons each cover one duty and their makers are young, so this is a race, not a settled market.
4. Publish the scanner in the Shoptet add-on store, where Czech shops already install tools that keep their discounts legal. One listing there reaches tens of thousands of shops, as [Willing to pay](#willing-to-pay) shows. Expect company: two add-ons already sell the discount rule there, and one has middling ratings, with reviewers split over its support and its export; see [Competition](#competition). The store has no legal-compliance category yet, so there is room for a scanner that covers the rest of the law.
5. For shops outside the big cities, include the scanner in a larger software project that the state's rural software grant pays half of. The grant is for small firms in rural areas and funds only projects above a minimum size, so a monthly add-on alone is too small to qualify; see [Willing to pay](#willing-to-pay). Applications stay open for a year, with the dates under [Why now](#why-now). A shop already planning new software can put the compliance scan into the same application.

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

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the three sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on 639 of 751 shops and 2,399 breaches, with the three commonest breach kinds as its items and the order buttons, the 1,276-breach total of the four kinds and the 18,000 out-of-court disputes as detail [S1,S3]; the breach counts came there from old move 3. Competition opens on "one duty each" and describes the three Czech products and the three law firms by what they sell; their names, prices, ages and ratings stay in their `locals[]` rows, and two facts from old move 4 moved into those rows: Hlídač Slev's reviewers splitting over its support and its price export [S8], and Slevy správně also selling on Upgates [S10]. The 19 CZK and 200 CZK prices left the body for their receipts [S11,S12]; the German €9.90–24.90 subscription prices, Trusted Shops' 17,000+ shops, Zalando, Obi and eleven markets, and the three German founding years left it for their `comps[]` rows. Why now opens on the fines shops pay now and the coming "eco" ban, with the Q2 2026 fines, the targeted checks and the badge duty as its three items, and the law and grant dates below as plain bullets [S2,S7,S9,S13,S14]. Willing to pay answers whether shops pay now, with the rural software grant's terms as detail and its dates under Why now [S7]. Six moves became five: old moves 3 and 6 merged, the moves lost every marker and figure for links, and old move 5's link to the private /sources page became the [S7] marker in the body. `entry.why` was rewritten as "Easier: … Harder: …" and names no company. Detail added from sources already on file, none of it new evidence: the 2025 checks' targeting, the order-button wording and the 2026 priority, read on the [S1] page; 414 breaches with 61 complaint and 52 unfair-practice findings [S9]; staff down 9% and the flat budget [S6]; the grant's 540M CZK and its 250,000–3M CZK eligible-cost band [S7]; what the directive bans [S2]; the two acts the bill amends and its 4 September committee position [S13]; the 27 March 2026 date of the missed deadline [S14]; and a Czech publisher's free green-claims check [S14]. Corrected against the sources rather than the old sentences: "That 85% is the baseline, not a tail" — the [S1] page says the 2025 checks were aimed mainly at shops already suspected, on shoppers' tips or ČOI's own monitoring, and the [S9] release says the same of Q2 2026, so the body now says 85% is the rate among the shops chosen, not among all Czech e-shops. The 2025 fines are 646 fines that became final, 12,978,500 CZK in all, per the [S1] page, not "646 closed cases" as the note has it (note untouched). Händlerbund's 30,000 members and ~92,000 presences had been cited to [S4], whose note names only the other two German firms; they now live only in Händlerbund's row. The old `entry.why` said every Czech seller had traded under three years, but Slevy správně dates to the January 2023 rule [S10] and Hlídač Slev's listing carries ratings from January 2023 [S8], so it now says the sellers are young and publish no customer counts. Old move 5 said public money halves the price, but the grant funds only projects with eligible costs of 250,000–3M CZK [S7], so move 5 now puts the scanner inside a larger software project. "Nobody covers the rest" became "no add-on checks" [S10], since a Czech publisher offers a free green-claims check [S14]. Flagged as inference: that an audit goes out of date at the next change in the law, and that the field is a race, rest on the audits being one-off [S5] and on two sellers registering in 2025 with no customer counts [S8,S10]; "some shops already pay" rests on the add-ons' public ratings by named shops [S8,S10], and no source names a paying shop; "a monthly add-on alone is too small" for the grant is our reading of its minimum [S7]; "most shops live with the risk of a fine", in `entry.why`, rests on the 85% and 91% rates among targeted shops [S1,S9]; the €430,000 estimate is arithmetic on Shoptet's 30,000 shops [S5] and a €12 price inside the German range, carried from 2026-08-25. FLAGGED, NOT CHANGED: Hlídač Slev's `since: 2025` is JARABOT's registration date, but its Shoptet listing shows ratings from 26 and 27 January 2023, so the product may be older than its company; Slevy správně's listing now shows five ratings, not the four its row cites [S10]; and the [S1] note's "Q1/2026 discount-labelling checks ~40%" is not on the [S1] page, so it stays out of the body. No score, status, source, `note:`, `sources[]` order, entry gate value, title, brief, solution or good_for changed.

2026-09-19 · headline copy — Owner-approved title and brief, written verbatim with the markers checked against the ledger. Before, verbatim — title: "Czech e-shops were fined 13M CZK last year for breaking consumer law"; brief: "Inspectors found breaches in 85% of e-shops they checked, like missing complaint information or illegal order buttons [S1]. A Czech ban on vague "eco" claims is also moving through parliament [S13].". After, verbatim — title: "Many Czech e-shops break consumer rules without realising it, and any inspection can end in a fine"; brief: "Inspectors caught 639 e-shops last year, usually for missing notices a shopper must see, like how to complain [S1]. Fines average about 20,000 CZK, and nothing checks a shop before the inspectors do [S1,S10].". Markers checked: the 639 caught shops are the 639 of 751 checked in 2025, and the two commonest breaches, missing pre-order information (488) and missing complaint information (363), are on the same results page [S1]; the fine average is [S1]'s 646 final fines worth 12,978,500 CZK; "nothing checks a shop" rests on the sweep of 606 Shoptet and Upgates add-ons, none of which covers the pre-order or complaint information, order buttons or green claims [S10]. FLAGGED as our reading, not a source's: "without realising it", since no source measures what shop owners know (the owner approved it as such); and "about 20,000 CZK", which is our division of [S1]'s two figures, not a published average. FLAGGED for the owner: "nothing checks a shop" is broader than [S10]'s finding, since two add-ons check discount labelling [S8,S10] and a Czech publisher offers a free green-claims check [S14]; the markers stay on [S1,S10], which carry what the line claims about the notices. The "eco" bill left the brief and stays under Why now [S13]. Solution and good_for unchanged. No score, status, source, `note:`, `sources[]` order or body sentence changed. Same date, a source note corrected and one ledger year fixed (owner-approved): [S1]'s note said "Q2/2026 risk-targeted inspections found a 91% violation rate; Q1/2026 discount-labelling checks ~40%". [S1]'s page, re-read on this date, is dated 26 February 2026 and carries only the 2025 results and the line that e-shop checks stay a ČOI priority in 2026; neither 2026 figure is on it. No rendered sentence rests on the ~40%: the body cites the 91% to its own receipt [S9] since the 2026-08-24 audit, and "ČOI says checking e-shops stays a priority in 2026 [S1]" is on the page. Because the note is the claim, and the owner approved correcting it, a dated correction line was appended to [S1]'s note; the original text was left as written, the same way the 2026-09-04 price checks appended "Verified" lines. Demand 2 does not rest on the ~40% and does not move. Hlídač Slev's `since` 2025 → 2023: its Shoptet listing, [S8]'s URL, read on this date, shows ratings dated 26 and 27 January 2023 and 20 August 2023, one of them praising "Hlídač slev" by name, so the add-on was on sale by January 2023. 2025 was the registration year of JARABOT s.r.o., the company now behind it, which `since` uses only when no product year is known. The evidence line now says both. `maturity` stays early: three years of selling meets the first limb of the established test, but the listing names no customer count, the state contracts register shows no public buyer, and there is no funding round or state listing, so no second limb is met. `competes` and gap are unchanged. No score, status, other note, marker, headline field or body sentence changed.
