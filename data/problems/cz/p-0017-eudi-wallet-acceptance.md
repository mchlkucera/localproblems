---
id: p-0017
region: cz
title: Czech banks, telcos and KYC-bound businesses must accept the EU Digital Identity Wallet
  for strong authentication from 2027 and have no integration path
category: govtech
geo: CZ-national
score: 5
scores:
  proof: 0
  money: 2
  urgency: 3
  demand: 0
  gap: 0
status: candidate
sources:
- type: regulation
  url: https://eur-lex.europa.eu/eli/reg/2024/1183/oj
  note: 'reg-eidas2-eudi-wallet: eIDAS 2.0 (Reg. 2024/1183) — Czechia must offer at least
    one EUDI Wallet by end-2026 (24 months after Dec 2024 implementing acts); relying-party
    acceptance obligations for regulated sectors follow within 36 months of the implementing
    acts, i.e. during 2027. Deadlines <18 months.'
  date: '2026-12-31'
  signal: reg-eidas2-eudi-wallet
- type: news
  url: https://ec.europa.eu/digital-building-blocks/sites/display/EUDIGITALIDENTITYWALLET/EU+Digital+Identity+Wallet+Home
  note: Commission EUDI page confirms each Member State will offer at least one wallet by
    2026, launch at the end of 2026; CZ builds on eDoklady.
  date: '2025-12-31'
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/453265-2026
  note: 'ted-453265-2026: DIA tendered the client part of the Czech EUDI Wallet (''KLIENTSKÁ
    ČÁST EVROPSKÉ PENĚŽENKY DIGITÁLNÍ IDENTITY'') — open competition, estimated ~€78.2M (~1.9bn
    CZK), published 2 Jul 2026. Largest open IT tender in the CZ TED window; money scored
    2 (open tender far above 5M CZK).'
  date: '2026-07-02'
  signal: ted-453265-2026
created: '2026-08-13'
updated: '2026-08-13'
---

Czechia must offer an EU Digital Identity Wallet to citizens and businesses by the end of 2026, and within 36 months of the December 2024 implementing acts — i.e. during 2027 — banks, telcos, large platforms and other regulated businesses must accept it wherever strong user authentication is required. The state's deadline creates the private sector's problem: every Czech relying party needs wallet-acceptance flows, and the reg-eidas2 signal notes that banks, utilities, e-shops with KYC obligations and municipalities currently have no integration path beyond following eDoklady's evolution.

Why now: the wallet launch is months away and the acceptance obligation lands within the scoring horizon. KYC-heavy businesses that rebuild onboarding around wallet-presented attestations early can cut verification cost; the rest will scramble against a legal obligation.

Who pays: relying parties — banks and payment institutions first (strong-authentication obligations under PSD2 make them the clearest obligated acceptors), then telcos, utilities and e-commerce with age/identity checks. Product surfaces named in the signal: relying-party registration and integration SDKs, KYC-flow rebuilds, QES and attribute-attestation services.

Existing non-solutions: current bank-ID schemes (Bankovní identita) solve Czech-domestic identity but do not discharge the EUDI acceptance obligation; eDoklady is the state wallet precursor, not an integration product for relying parties. No gap check was run this cycle (gap 0), and Bankovní identita is a meaningful quasi-incumbent that could absorb this market — the main risk to this problem.

Money receipted 2026-08-13: DIA put the national wallet's client part out as an open ~€78M competition in July 2026 — the state is spending seriously and on schedule, which both funds an SI/dev-shop opportunity today and confirms the 2027 relying-party clock. A gap check on CZ EUDI relying-party tooling is the remaining follow-up that would move the score.
