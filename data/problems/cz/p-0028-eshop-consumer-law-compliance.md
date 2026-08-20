---
id: p-0028
region: cz
title: 85% of inspected Czech e-shops broke consumer law in 2025, enforcement keeps finding
  ~90% violation rates, and the green-claims rules landing 27 Sep 2026 stack another layer
  on merchants who have no compliance tooling
category: retail-services
geo: CZ-national
score: 7
scores:
  proof: 1
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
sources:
- type: complaint
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
  url: https://mpo.gov.cz/assets/cz/ochrana-spotrebitele/aktualni-informace/2026/3/Zprava-o-prubeznem-plneni-Strategie-spotrebitelske-politiky-2025.pdf
  note: 'mpo-adr-vyuziti: MPO''s consumer-policy report tabulates ~18,000 ČOI out-of-court
    dispute filings 2020-H1/2025 (defective goods and warranties) — the consumer-side receipt
    that the violations ČOI finds correspond to recurring real-world harm. The same report
    documents ČOI running ~20,000 inspections/yr on an inflation-eroded budget: enforcement
    is risk-targeted, so violation rates in targeted sweeps keep rising.'
  date: '2026-03-31'
  signal: mpo-adr-vyuziti
- type: arbitrage
  url: https://www.trustedshops.com/
  note: 'Named analogs: Trusted Shops (Cologne) built a durable DE/EU business productizing
    e-commerce trust and legal compliance (certification + Abmahnschutz legal-text service),
    and IT-Recht Kanzlei runs subscription legal-text compliance for tens of thousands of
    DE shops — the productized model is proven in the CEE-adjacent market where enforcement
    pressure (Abmahnung culture) preceded Czechia''s. Named analogs without a fresh funding
    receipt: proof 1.'
  date: '2026-08-13'
- type: gap-check
  url: https://www.pravoeshopu.cz/pravni-audit-eshopu
  note: 'Gap check 2026-08-13: the CZ supply side is legal services priced per audit — Právo
    e-shopů, eLegal, AZ LEGAL and peers sell one-off právní audity and terms drafting; no
    Czech compliance-monitoring SaaS mapped to ČOI enforcement priorities (information duties,
    buttons, discount labelling, green claims) was found. Shoptet''s ~30k-merchant ecosystem
    is a distribution channel, not a compliance product. Gap 1 (quick search, services-only
    incumbents named).'
  date: '2026-08-13'
- type: complaint
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
  url: https://apiagentura.gov.cz/cs/podporovane-aktivity-optak/technologie-pro-mas-optak/technologie-pro-mas-clld-vyzva-ii/
  note: 'dotace-optak-technologie-mas-2: OP TAK Technologie pro MAS II funds new machinery,
    software and IT for small rural firms via local action groups — 540M CZK (~€22M) allocated,
    grants up to 1.49M CZK at a 50% rate on eligible costs of 250k-3M CZK, for SMEs in MAS
    territories outside Prague and cities over 25,000 inhabitants; applications run 2026-09-01
    to 2027-09-01. The co-funding channel against the merchant-side price objection, not a
    receipt for this record''s money score.'
  date: '2026-09-01'
  signal: dotace-optak-technologie-mas-2
created: '2026-08-13'
updated: '2026-08-20'
---

When the Czech trade inspection walked the checkout flows of 751 e-shops in 2025, 85% were breaking the law — 2,399 individual violations, from missing complaint-handling and pre-contractual information to non-compliant order buttons and unfair commercial practices [S1]. This is not a tail of rogue merchants: it is the compliance baseline of one of Europe's densest e-commerce markets, confirmed again in 2026 when risk-targeted inspections found a 91% violation rate [S1].

Why now: the obligation stack is still growing. On 27 September 2026 the green-claims rules (directive 2024/825, enforced by ČOI through the consumer-protection act) blacklist generic environmental claims, unverified sustainability labels and unsubstantiated durability promises — every e-shop using "eko", "šetrné k přírodě" or a climate-neutral badge must substantiate or strip it within weeks [S2]. This lands on top of the 2023 button/labelling rules merchants already fail [S1], and beside the accessibility enforcement wave tracked separately as p-0020. ČOI's capacity is shrinking (inspections down from ~29,000 to ~20,000 a year on a flat budget per MPO) [S6], which pushes it toward exactly the risk-targeted sweeps that produce 90%+ hit rates and fines [S1,S3].

Who pays: the merchants — roughly the whole Czech e-commerce long tail plus the platforms that host it. The 2,399 documented breaches are checklistable items: information duties, terms clauses, button texts, price-history display, claims language [S1]. A merchant today can either ignore the risk (the majority position, per the numbers) [S1] or buy a one-off legal audit at law-firm prices that is stale by the next legislative wave [S5]. Platform-level distribution (Shoptet and peers) means one integration could reach tens of thousands of obligated shops [S5].

Existing non-solutions: per-audit legal services (Právo e-shopů, eLegal, AZ LEGAL), generic terms templates of uncertain provenance, and — for the green-claims wave specifically — nothing yet [S5]. The 2026-08-13 gap check found no Czech compliance-monitoring product mapped to ČOI's enforcement priorities [S5].

Solved elsewhere: Germany productized exactly this under harsher enforcement pressure — Trusted Shops (certification plus legal-protection subscription) and IT-Recht Kanzlei (subscription legal texts kept current for tens of thousands of shops) are durable businesses built on merchants' fear of Abmahnung [S4]. Czechia now gets the enforcement pressure (regulator sweeps and fines rather than competitor warnings) without the productized answer; proof is scored 1 because the analogs, while proven, carry no fresh funding receipt.

## First moves

1. Crawl the Czech e-shop long tail for green-claims language — "eko", "šetrné k přírodě", climate-neutral badges — and build the list of exposed merchants: directive 2024/825 blacklists unsubstantiated versions of exactly these claims from 2026-09-27 [S2].
2. Cold-pitch the flagged merchants before 2026-09-27 with a claim-by-claim fix report, priced at the German subscription points the comps prove (€9.90–24.90/mo at IT-Recht Kanzlei) — conversion doubles as the test of the riskiest assumption, that merchants pay before they are fined (ignoring the risk is the majority position at 85–91% violation rates) [S1].
3. Extend the scanner to ČOI's four documented failure buckets — missing pre-contractual information (488 breaches in 2025), missing complaint-handling information (363), unfair commercial practices (318), non-compliant order buttons (107) — the checklistable core of the 2,399 recorded violations [S1].
4. Pitch Shoptet an app-store compliance integration: the record's gap check calls its ~30k-merchant ecosystem a distribution channel with no compliance product on it, and one integration reaches tens of thousands of obligated shops [S5].
5. Soften the price objection for the rural long tail: merchants based in MAS territories — outside Prague and cities over 25,000 inhabitants — can co-fund software purchases at 50% (grants up to 1.49M CZK) from [OP TAK Technologie pro MAS II](/sources/tenders#dotace-optak-technologie-mas-2), €22M allocated, applications 2026-09-01 to 2027-09-01 [S7].
6. Competition, per the record's gap check: **Právo e-shopů, eLegal and AZ LEGAL** sell one-off právní audity at law-firm prices that go stale by the next legislative wave; no Czech compliance-monitoring SaaS mapped to ČOI's enforcement priorities was found — continuous monitoring against the one-off audit price is the wedge [S5].
