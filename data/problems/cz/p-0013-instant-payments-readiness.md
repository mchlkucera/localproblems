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
  name: "Instant Payments Regulation (EU) 2024/886"
  gist: "the law and its 2027 dates"
  why: "Sets both dates — receive instant euro payments by 9 January 2027, send them with Verification of Payee by 9 July 2027 — and caps the fee at what an ordinary transfer costs."
  url: https://eur-lex.europa.eu/eli/reg/2024/886/oj
  note: 'reg-instant-payments-cz: Instant Payments Regulation (Reg. 2024/886) — non-eurozone
    PSPs must receive instant EUR transfers by 9 Jan 2027, send + run Verification of Payee
    by 9 Jul 2027, out-of-hours sending by 9 Jun 2028. Fees capped at standard credit transfer
    level. Deadlines <18 months.'
  date: '2027-01-09'
  signal: reg-instant-payments-cz
- type: news
  name: "Worldline — the non-euro-area deadlines"
  gist: "euro-area live since 2025"
  why: "Confirms the dates that fall on non-euro-area countries, and records euro-area providers already running instant euro payments since 2025."
  url: https://worldline.com/en/home/main-navigation/resources/blogs/2025/instant-payments-regulation-a-key-development-for-non-eurozone-eu-countries
  note: 'Non-eurozone deadline verification; eurozone PSPs already live since Jan/Oct 2025,
    meaning reference implementations exist but CZK-centric institutions have not built SEPA
    Instant rails. Demand point: signal documents that smaller PSPs/EMIs lack in-house capability.'
  date: '2025-12-31'
created: '2026-08-13'
updated: '2026-09-02'
---

Czech banks, payment institutions and e-money institutions — built around the koruna, not the euro — must receive instant euro payments by 9 January 2027 and send them by 9 July 2027 under the Instant Payments Regulation [S1]. Sending also means Verification of Payee — the payee's name checked against the account number before the money leaves [S1].

Why now: the two deadlines land six months apart, on 9 January and 9 July 2027 [S1]. Euro-area banks and payment firms have run instant euro payments since 2025, so the build is proven [S2]. Each Czech institution still has to wire it into core banking, run sanctions screening nights and weekends, and hold cash ready round the clock. The regulation caps the fee at what an ordinary transfer costs [S1], so the payback is efficiency, not price.

Who pays: Czech banks, payment institutions and e-money issuers, buying payee checking, instant-payment gateway integration and round-the-clock screening as services [S1].

Existing non-solutions: the large banks build it in house. For everyone smaller, nothing is verified: the Czech market has not been searched, and the euro-area payee-checking and gateway vendors — the natural suppliers — may or may not sell here. Whether the Czech Banking Association is coordinating one shared service is unknown.

## Revisions

2026-08-24 · rejected — Removed from the register per the owner's quality mandate. One regulation signal is the entire evidence base; the second source is a URL copied from that signal's own notes, and the 9,324-signal corpus holds no Czech tender, contract or complaint touching SEPA Instant readiness. The demand receipt failed verification: the cited Worldline post says nothing about smaller PSPs lacking capability — it omits implementation challenges entirely and notes CZ is fast-tracking payment innovation [S2] — so the capability sentence and title clause are cut, demand 1 → 0, score 3 → 2. What remains is an EU deadline restated from memory-grade material, not a confirmed Czech problem.

2026-09-02 · plain-language pass — Five trade terms glossed or replaced at first use: Verification of Payee, IBAN, VoP, PSPs, ČBA. Argument 214 → 209 words, every date and [Sn] marker kept. The stray Recommended follow-up paragraph folded into Existing non-solutions, where it already rendered. A public name, gist and why added to both sources. No score, status, note or marker touched.
