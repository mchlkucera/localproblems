---
id: p-0013
region: cz
title: Czech banks and payment institutions must receive instant euro payments by 9 Jan 2027
  and send them with Verification of Payee by 9 Jul 2027, and smaller PSPs lack the in-house
  capability
category: fintech
geo: CZ-national
score: 3
scores:
  proof: 0
  money: 0
  urgency: 2
  demand: 1
  gap: 0
status: candidate
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
updated: '2026-08-13'
---

Czech banks, payment institutions and e-money institutions — CZK-centric by history — must be able to receive instant euro credit transfers by 9 January 2027 and to send them, plus run Verification of Payee (name-IBAN matching), by 9 July 2027 under the Instant Payments Regulation. The reg-instant-payments-cz signal documents that smaller PSPs and EMIs lack the in-house capability to build SEPA Instant rails, 24/7 sanctions screening and VoP matching.

Why now: the receive deadline is under five months away at record creation; the send+VoP deadline is under eleven. Eurozone PSPs went live in 2025, so the technical patterns are proven, but each Czech institution still needs core-banking integration, screening rework for 24/7 operation, and liquidity management for continuous settlement — and the regulation caps instant-payment fees at standard transfer levels, so cost recovery must come from efficiency, not pricing.

Who pays: the obligated institutions — particularly the long tail of smaller banks, spořitelní družstva, payment institutions and EMIs that cannot staff this internally and will buy VoP APIs, instant-payment gateway integration and real-time screening as services.

Existing non-solutions: in-house projects at large banks; for the long tail, nothing verified — no CZ-specific gap check was run this cycle, and eurozone VoP/gateway vendors (the natural suppliers) may or may not be selling into CZ, so gap scores 0.

Recommended follow-up: verify which VoP scheme providers cover Czech PSPs and whether ČBA is coordinating a shared utility; a shared-service gap here would sharpen the problem considerably.
