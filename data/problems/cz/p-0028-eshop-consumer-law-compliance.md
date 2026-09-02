---
id: p-0028
region: cz
title: Most inspected Czech e-shops break consumer law
fix: 'A weekly scanner for Czech online shops that checks the checkout, the prices and the
  product claims against consumer law and hands the merchant a fix list — on subscription,
  not as a one-off legal audit.'
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
build:
  capital: kiosk
  first_revenue: weeks
  builder: solo
  note: 'The wedge is a checkout scanner plus subscription legal texts sold self-serve
    at DE-proven price points (€9.90–24.90/mo); a solo builder with a partnered e-shop
    lawyer ships it from a laptop and rides Shoptet for distribution.'
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
  why: "From 27 September 2026 generic green claims, unverified sustainability labels and unsubstantiated durability promises are blacklisted, and ČOI enforces it through the consumer-protection act."
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
created: '2026-08-13'
updated: '2026-09-02'
---

ČOI — the Czech trade inspection authority — walked the checkout flows of 751 e-shops in 2025 and found 639 breaking the law: 2,399 violations, from missing complaint-handling and pre-contractual information to non-compliant order buttons [S1]. That 85% is the baseline, not a tail — targeted inspections in Q2 2026 found violations in 94 of 103 shops [S9].

Why now: from 27 September 2026 the green-claims rules blacklist generic environmental claims, unverified sustainability labels and unsubstantiated durability promises, and ČOI enforces them [S2]. Every shop running an "eko" or climate-neutral badge must substantiate it or strip it. Its own inspections fell from ~29,000 a year to ~20,000 on a flat budget [S6], so it targets rather than samples.

Who pays: the merchants, because the alternative is a fine and inspectors now target the worst shops. Shoptet, a platform merchants rent their storefront from, hosts about 30,000 [S5]. Czech compliance add-ons charge 19 to 200 CZK a month [S8,S10]; the German subscriptions this copies run €9.90–24.90. Thirty thousand merchants, a €12 bundle over the uncovered duties, one in ten buying: about €430,000 a year, against ~13.0M CZK of ČOI fines in 2025 [S1].

Existing non-solutions: Právo e-shopů, eLegal and AZ LEGAL — three law firms — sell one-off audits per engagement [S5]. Discount labelling is taken twice: Hlídač Slev and Slevy správně both rewrite reference prices for the 30-day lowest-price rule and keep three years of ČOI-exportable history, at ~19 CZK and a flat 200 Kč a month [S8,S10]. Pravoid generates terms and privacy policies, with alerts when the law moves [S8]; its proprietor and Hlídač Slev's vendor both registered in 2025, and neither publishes a customer count [S8]. Nobody covers the rest of ČOI's map: green claims, information duties, order buttons [S8,S10].

Solved elsewhere: three German firms have lasted decades on this. Trusted Shops has sold certification with buyer protection since 1999 to 17,000+ European shops, Zalando and Obi among them, across eleven markets including Austria and Poland. IT-Recht Kanzlei has sold subscription legal texts since 2004, from €9.90 a month, with plugins for the major shop platforms. Händlerbund, trading since 2008, counts 30,000 members and some 92,000 digital presences [S4]. All three grew on fear of a warning letter; here the regulator supplies it. None carries a fresh funding round [S4] — two decades of paying customers is the receipt.

## First moves

1. Crawl Czech e-shops for green-claims language — "eko", "šetrné k přírodě", climate-neutral badges. That list is your prospect list: from 27 September 2026 the directive blacklists unsubstantiated versions of exactly those claims [S2].
2. Pitch those merchants before 27 September 2026 with a claim-by-claim fix report, priced at the German subscription points listed under Proven abroad. Whether a merchant buys before the fine arrives is the assumption everything here rests on — at 85–91% violation rates, ignoring the risk is what most of them already do [S1,S9].
3. Extend the scanner to the four failures ČOI writes up most: missing pre-contractual information (488 breaches in 2025), missing complaint-handling information (363), unfair commercial practices (318), non-compliant order buttons (107) [S1]. Those four are 1,276 of the 2,399 recorded violations, and each one is a checklist item.
4. Ship into the Shoptet add-on store, and expect company. Hlídač Slev sells there at ~19 CZK a month per 1,000 products, on five middling public ratings, with reviewers citing support and export accuracy [S8]; Slevy správně sells at a flat 200 Kč a month on Shoptet and Upgates [S10]. One integration still reaches tens of thousands of obligated shops [S5], and the catalogue has no legal-compliance category yet [S8,S10].
5. Let public money halve the price outside the cities: shops in MAS areas — the state's rural local-action-group territories, outside Prague and towns over 25,000 people — get software co-funded at 50%, grants up to 1.49M CZK, from [OP TAK Technologie pro MAS II](/sources/tenders#dotace-optak-technologie-mas-2) — the state's business-support programme — €22M allocated, applications 2026-09-01 to 2027-09-01 [S7].
6. Aim at the duties nobody sells. **Právo e-shopů, eLegal and AZ LEGAL** leave a shop compliant only until the next legislative wave [S5], and the three Czech products each cover one duty — **Hlídač Slev** and **Slevy správně** on discount labelling, **Pravoid** on legal texts with alerts from e-Sbírka, the state law gazette [S8,S10]. Both those vendors registered during 2025 [S8], so this is a race, not an entrenchment. The open ground is coverage: pre-contractual and complaint-handling information, order buttons, and the green claims blacklisted from 27 September 2026 [S1,S2,S8,S10].

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-20 · de-rank, gap re-check and evidence audit — Three blocks recorded on this date, merged here; the de-rank was written down twice and is stated once. The absence claim was re-run in Czech against google-cz, the Shoptet add-on catalogue and ARES, and it fails. Hlídač Slev (JARABOT s.r.o., IČO 22571299) sells automated discount-labelling compliance with ČOI-exportable price history on the Shoptet store — the very store this record described as carrying no compliance product — and Pravoid (IČO 23683368) sells generated legal texts with e-Sbírka change alerts across five e-shop platforms [S8]. Gap 1 → 0, score 7 → 6, status candidate → watching. Two specific sentences were rewritten rather than deleted, because their factual halves survive: first move 4 asserted the Shoptet ecosystem had "no compliance product on it" — it has one, whose public ratings are middling — and first move 6 asserted no ČOI-mapped monitoring SaaS existed. The unbuilt part is now specific rather than total: the green-claims wave landing 27 Sep 2026, pre-contractual and complaint-handling information, and order-button texts still have nothing Czech on them [S8], against an 85–91% violation baseline that has not moved [S1]. The enforcement evidence is untouched — the 85% and 91% violation rates, the 2,399 breaches and the capacity numbers are all receipted and unaffected [S1,S6]. Method control: the same search method was run first at Wultra (p-0017) and Softlink (p-0026); the funded-ledger grep returned round-wultra and a plain descriptive Czech query surfaced softlink.cz unprompted, so the method is known to produce positives before any negative here was trusted. The title carried the same disproved absence, "who have no compliance tooling", and has been cut: Hlídač Slev is compliance tooling, sold on the very platform this record described as carrying none. Cut in the same pass: the IT-Recht Kanzlei subscription price points in the second first move. Those figures exist only in the comps ledger — neither IT-Recht Kanzlei nor Trusted Shops appears in any signal, and the source note that names both companies gives no prices — and a comparable's traction line cannot back a body claim. The move now points at the ledger, which still prints the prices in full, and nothing removed by that audit has been reintroduced.

2026-08-24 · gap re-check and fact check — The mechanical sweep of the add-on lookup corpus found a second discount-labelling product this record did not name: Slevy správně by Cenový automat s.r.o., flat 200 Kč/month, 6-hour snapshots, 3-year ČOI history, on Shoptet and Upgates [S10]; the body and first moves 4 and 6 now carry it beside Hlídač Slev. The 91% risk-targeted rate had been cited to the 2025 results page, which carries only 2025 figures; the ČOI Q2/2026 release (103 inspections, 94 with violations) is now on the ledger and the claim re-cited [S9]. Cut in the same pass: "one of Europe's densest e-commerce markets", a density claim with no receipt in the corpus, and the clause tying this record to an accessibility "enforcement wave" at p-0020 — that record's enforcement claim failed verification on this date and it is rejected. The green-claims, pre-contractual, complaint-handling and order-button absences were re-confirmed against all 606 add-ons in both marketplaces [S10]. Gap stays 0; nothing rescored.

2026-08-25 · board-brief rewrite — The argument was cut from 529 words to the board-brief shape, one claim per sentence and at most two markers to a sentence, with no claim added beyond its sources and none removed: the 85% and 91% violation rates, the 2,399 breaches, the ČOI capacity numbers, the two discount-labelling incumbents and Pravoid all survive in shorter form. "How big" now states a bottom-up figure instead of gesturing at the long tail — ~30,000 Shoptet merchants [S5] against Czech add-on pricing of 19–200 CZK/month [S8,S10] and the German €9.90–24.90 subscription points, giving roughly €430k/yr at a €12 bundle and 10% penetration, set beside ~13.0M CZK of 2025 fines [S1]. The "Solved elsewhere:" lead-in was already present and is unchanged in function; the German analogs now state what each proves rather than being named in passing. Every source gained a public name and why line. Scores, status and internal notes untouched. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker were untouched by those passes. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, and both dimensions moved. `scores.proof` 1 → 3. The v1 answer, 1, was reasoned as "named analogs without a fresh funding receipt" — but a fresh round was never what proof measures, and under the maturity test all three German analogs pass on the customer limb without needing one: Trusted Shops selling since 1999 across 17,000+ European shops with Zalando and Obi named and eleven markets on its ledger including Austria and Poland, IT-Recht Kanzlei since 2004 with tens of thousands of shops on subscription, Händlerbund since 2008 with 30,000 members and ~92,000 digital presences [S4]. Established in two-plus markets with Germany, Austria and Poland all CEE-adjacent is rung 3. `scores.gap` 0 → 1, which is the correction that matters here. The 2026-08-20 pass dropped gap to 0 on the strength of finding two Czech products, and the 2026-08-24 pass found a third — but the new ladder asks how mature they are, and ARES answers plainly. JARABOT s.r.o., which sells Hlídač Slev, was registered 2025-02-10; Bc. Filip Krechler, the proprietor behind Pravoid, on 2025-09-03; both dates read live from ARES on this date against the IČOs [S8] already carried. Cenový automat's Slevy správně only just clears the three-year limb, dating to the January 2023 reference-price rule it corrects for, and clears no other: none of the three publishes a customer count, pairs with a public buyer in `data/lookup/cz-contract-parties.jsonl`, or carries a round or a state listing. An early local player does not close a space. The law firms behind the one-off audits — Právo e-shopů, eLegal (ARES 2014), AZ LEGAL (ARES 2016) — are the "weak or legacy incumbents" half of the same rung. Gap does not rise past 1: [S8] and [S10] found local players, not none, so rung 2 is unavailable however the check was run. All six were lifted from the [S5], [S8] and [S10] scan prose into a structured `locals[]` ledger. `score` 6 → 9. The non-solutions paragraph, the Proven-abroad paragraph and first move 6 now state the incumbents' ages, because that is the fact carrying the gap score, and the Proven-abroad paragraph stops treating an absent round as an absent proof. Nothing found in the earlier passes was removed: the coverage gaps that remain unbuilt — green claims from 27 Sep 2026, pre-contractual and complaint-handling information, order buttons — are unchanged and still cited [S8,S10]. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved. FLAGGED, NOT CHANGED: `status` is still `watching`, set by the SPEC §4 de-rank rule when gap went to 0 on 2026-08-20. The condition that triggered it no longer holds.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. Three entries stay `direct`, three move to `adjacent`, and no maturity changes. Hlídač Slev, Slevy správně and Pravoid each sell a slice of the same automated compliance job to the same shops, so they are direct, and each fails the established test on its own receipts. The three law firms — Právo e-shopů, eLegal and AZ LEGAL — move to `adjacent`: they sell one-off audits and terms drafting priced per engagement, which is the legacy service a subscription scanner would replace rather than the monitoring product itself. All three read early on receipts, so the relabel touches nothing. `scores.gap` stays 1 and now says the rung's own words: direct competitors exist here and every one of them is early. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 6 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

2026-09-02 · plain-language pass — Trade terms glossed at first use in the rendered prose: ČOI as the Czech trade inspection authority, Shoptet as a platform merchants rent their storefront from, MAS as the state's rural local-action-group territories, OP TAK Technologie pro MAS II as the state's business-support programme [S7], and e-Sbírka as the state law gazette [S8]. The argument tightened from 441 words to 390 with every [Sn] marker, figure, price and named company kept, First moves rewritten in the plain house voice, and a short gist added beside all ten sources' public why lines. No score, status, ledger entry or source note touched.
