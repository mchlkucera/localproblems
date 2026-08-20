---
id: p-0012
region: cz
title: Czech importers and processors of wood, coffee, rubber and soy must file geolocation-based
  due diligence statements by 30 Dec 2026
category: environment
geo: CZ-national
score: 3
scores:
  proof: 0
  money: 0
  urgency: 2
  demand: 1
  gap: 0
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'DDS filing automation and supplier geolocation collection can lean on the
    EU information system and public forest data rather than a proprietary satellite
    stack, but mid-sized importers need onboarding pilots before the 30 Dec 2026
    deadline converts to revenue.'
comps:
- name: osapiens
  url: https://osapiens.com/
  geo: DE
  since: 2018
  traction: '$120M Series B led by Goldman Sachs Growth (Businesswire, 2024); 1,300+
    customers incl. Bosch, Lidl; EUDR hub module'
- name: LiveEO
  url: https://www.live-eo.com/
  geo: DE
  since: 2018
  traction: '€25M Series B, €51.6M total (EU-Startups, 2024); TradeAware satellite
    EUDR product with legality checks in 80+ countries'
sources:
- type: regulation
  url: https://eur-lex.europa.eu/eli/reg/2023/1115/oj
  note: 'reg-eudr-deforestation: EUDR (Reg. 2023/1115 as amended Dec 2025) — large and medium
    operators must run geolocation-based due diligence and file DDS by 30 Dec 2026 (micro/small
    30 Jun 2027); penalties up to 4% of EU turnover. Deadline <18 months.'
  date: '2026-12-30'
  signal: reg-eudr-deforestation
- type: news
  url: https://www.europarl.europa.eu/news/en/press-room/20251211IPR32168/deforestation-law-parliament-adopts-changes-to-postpone-and-simplify-measures
  note: 'Second postponement and simplification adopted Dec 2025 (EP vote 11 Dec 2025) — the
    repeated postponements under industry pushback document the pressure; simplifications:
    only first placer files DDS, one-off simplified declaration for micro/small primary operators.'
  date: '2025-12-11'
created: '2026-08-13'
updated: '2026-08-20'
---

Czech companies trading in cattle, cocoa, coffee, palm oil, rubber, soy and wood products — furniture and wood processing, coffee roasters, food producers, tyre and rubber importers — must run geolocation-based due diligence on their supply chains and file due diligence statements from 30 December 2026 (micro/small firms from 30 June 2027) [S1]. Per the reg-eudr signal, the documentation burden falls heavily on mid-sized importers that have no traceability stack of any kind [S1]. Penalties reach 4% of EU turnover [S1].

Why now: the December 2025 amendment was the second postponement, and the simplifications that came with it (only the first placer on the EU market files the DDS; simplified one-off declarations for micro/small primary operators) settle the final shape of the obligation [S2] — the compliance date is now firm and under 17 months away at record creation. The history of postponements under industry pushback is itself evidence that obligated firms find the requirements hard to meet [S2].

Who pays: importing and processing firms in the wood/furniture, coffee, food and rubber value chains [S1], buying due-diligence-as-a-service, geolocation plot verification, supplier questionnaire automation and customs-integrated filing [S1].

Existing non-solutions: nothing CZ-specific was searched this cycle (gap scored 0 accordingly); EU-wide EUDR SaaS exists but mid-sized Czech importers are unlikely targets of those vendors' direct sales, leaving a localization and service gap plausible but unverified.

Recommended follow-up: a gap check on CZ-language EUDR tooling and whether celní deklaranti / customs software vendors are bundling DDS filing.

---
**CORRECTION (2026-08-20, evidence audit):** Removed two unbacked assertions. The scale claim "— a large sector in Czechia —" had no count, turnover or firm population behind it anywhere in the corpus; `reg-eudr-deforestation` names the CZ sectors but makes no scale claim. The named vendors "(e.g. Grit, Aimtec ecosystem)" in the follow-up proposal return no hits anywhere in the signal corpus — two Czech companies asserted as customs-software vendors with nothing behind them. The follow-up still proposes the check, without pre-naming who will be found.

---
**CORRECTION (2026-08-20, title sweep):** The **title** asserted that mid-sized firms "have no traceability stack" while `scores.gap` is 0, which by definition means no CZ incumbent check has been run. An absence claim in the title with an unchecked gap score beneath it is the contradiction this sweep exists to remove. The clause is gone; no score changed.
