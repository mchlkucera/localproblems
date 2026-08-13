---
id: p-0001
title: "Czech energy communities lose up to half the value of shared electricity to bad allocation and settlement, and have no software to run member billing"
category: energy
geo: CZ-national
score: 8
signals:
  arbitrage: 3
  money: 0
  deadline: 0
  demand: 2
  gap: 2
  freshness: 1
status: candidate
receipts:
  - type: arbitrage
    url: https://exnaton.com/
    note: "de-exnaton: DACH/Nordics-proven white-label billing/settlement SaaS for energy communities (ETH spin-off, used by utilities); Austrian peers eFriends/OurPower validate the category in a CEE-adjacent market. Absence check 2026-08-13 found no CZ equivalent."
    date: 2026-08-13
  - type: complaint
    url: https://exnaton.com/
    note: "HN (2025) report cited in de-exnaton: CZ communities reportedly lose up to ~50% of shared electricity value to bad allocation/settlement; municipalities founding společenství have zero software."
    date: 2026-08-13
  - type: gap-check
    url: https://exnaton.com/
    note: "Absence check 2026-08-13: searches return only EDC itself, ministry PR and ASITIS (consulting/services); no dedicated CZ community-energy billing/settlement SaaS."
    date: 2026-08-13
  - type: round
    url: https://www.vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-july-2026
    note: "round-pstryk: Pstryk (PL, dynamic electricity pricing for households/SMEs) raised EUR 7M Series A led by Future Energy Ventures, Jul 2026 — CEE investor appetite for consumer/SME energy tooling."
    date: 2026-08-04
created: 2026-08-13
updated: 2026-08-13
---

Czech energy communities (energetická společenství) and groups sharing electricity under Lex OZE II have been legally able to share power via EDC since August 2024, but they run member administration, allocation keys and settlement by hand. Per the HN reporting cited in the de-exnaton signal, communities lose up to roughly half of the value of shared electricity to bad allocation and settlement. Municipalities founding společenství — a core intended user of the regime — have no software at all for the task.

Why now: the regulatory window opened in 2024 (Lex OZE II, EDC data exchange live) and the first cohort of communities is now operating long enough to feel the settlement losses. EDC handles data exchange between market participants but explicitly does not do community administration, member billing or optimization, so the pain sits with the community operator, unaddressed by state infrastructure.

Who pays: community founders (municipalities, housing cooperatives, groups of firms) and — following the Exnaton go-to-market — utilities and DSO-adjacent service firms that want a white-label product to offer communities. The value proposition is direct: recovered settlement value, which the demand receipt quantifies at up to ~50% of shared electricity.

Existing non-solutions: EDC (data exchange only), ministry guidance, and ASITIS-style consultancies selling services rather than product. The absence check of 2026-08-13 found no dedicated Czech community-energy billing/settlement SaaS.

Solved elsewhere: Exnaton (ETH spin-off) sells exactly this to utilities across DACH and the Nordics; Austrian community-energy players eFriends and OurPower prove tooling demand under EU RED II in a market bordering Czechia. The July 2026 Pstryk round in Poland shows CEE investors funding adjacent consumer/SME energy software.
