---
id: p-0013
region: cz
title: Czech banks and payment institutions must receive instant euro payments by 9 Jan 2027
  and send them with Verification of Payee by 9 Jul 2027
category: fintech
geo: CZ-national
score: 2
scores:
  proof: 0
  money: 0
  urgency: 2
  demand: 0
  gap: 0
status: rejected
build:
  capital: funded
  first_revenue: year-plus
  builder: funded-team
  note: 'Selling 24/7 SEPA Instant rails, sanctions-screening rework and EPC-scheme
    VoP to regulated banks and PSPs means certification, security reviews and bank
    procurement cycles, so payroll runs long before first revenue.'
comps:
- name: SurePay
  url: https://www.surepay.eu/
  geo: NL
  since: 2016
  traction: '10bn+ payments verified; 200+ banks, 750+ business customers (IRIS.vc,
    2025); €12.2M round 2021; Carlyle invested 2025'
  markets: [GB]
- name: Numeral
  url: https://www.numeral.io/
  geo: FR
  since: 2021
  traction: '€13M seed led by Balderton (Tech.eu, 2021); acquired by Mambu Dec 2024
    to power SEPA Instant and VoP'
sources:
- type: regulation
  url: https://eur-lex.europa.eu/eli/reg/2024/886/oj
  note: 'reg-instant-payments-cz: Instant Payments Regulation (Reg. 2024/886) — non-eurozone
    PSPs must receive instant EUR transfers by 9 Jan 2027, send + run Verification of Payee
    by 9 Jul 2027, out-of-hours sending by 9 Jun 2028. Fees capped at standard credit transfer
    level. Deadlines <18 months.'
  date: '2027-01-09'
  signal: reg-instant-payments-cz
- type: news
  url: https://worldline.com/en/home/main-navigation/resources/blogs/2025/instant-payments-regulation-a-key-development-for-non-eurozone-eu-countries
  note: 'Non-eurozone deadline verification; eurozone PSPs already live since Jan/Oct 2025,
    meaning reference implementations exist but CZK-centric institutions have not built SEPA
    Instant rails. Demand point: signal documents that smaller PSPs/EMIs lack in-house capability.'
  date: '2025-12-31'
created: '2026-08-13'
updated: '2026-08-24'
---

Czech banks, payment institutions and e-money institutions — CZK-centric by history — must be able to receive instant euro credit transfers by 9 January 2027 and to send them, plus run Verification of Payee (name-IBAN matching), by 9 July 2027 under the Instant Payments Regulation [S1].

Why now: the receive deadline is under five months away at record creation; the send+VoP deadline is under eleven [S1]. Eurozone PSPs went live in 2025 [S2], so the technical patterns are proven, but each Czech institution still needs core-banking integration, screening rework for 24/7 operation, and liquidity management for continuous settlement — and the regulation caps instant-payment fees at standard transfer levels [S1], so cost recovery must come from efficiency, not pricing.

Who pays: the obligated institutions — the market the signal names is VoP APIs, instant-payment gateway integration and real-time screening sold as services [S1].

Existing non-solutions: in-house projects at large banks; for the long tail, nothing verified — the Czech market has not been searched yet, and eurozone VoP/gateway vendors (the natural suppliers) may or may not be selling into CZ, so no open local field is claimed.

Recommended follow-up: verify which VoP scheme providers cover Czech PSPs and whether ČBA is coordinating a shared utility; a shared-service gap here would sharpen the problem considerably.

## Revisions

2026-08-24 · rejected — Removed from the register per the owner's quality mandate. One regulation signal is the entire evidence base; the second source is a URL copied from that signal's own notes, and the 9,324-signal corpus holds no Czech tender, contract or complaint touching SEPA Instant readiness. The demand receipt failed verification: the cited Worldline post says nothing about smaller PSPs lacking capability — it omits implementation challenges entirely and notes CZ is fast-tracking payment innovation [S2] — so the capability sentence and title clause are cut, demand 1 → 0, score 3 → 2. What remains is an EU deadline restated from memory-grade material, not a confirmed Czech problem.
