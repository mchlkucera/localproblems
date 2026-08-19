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
status: watching
build:
  capital: funded
  first_revenue: year-plus
  builder: funded-team
  note: 'Bank-grade eIDAS2 trust infrastructure with ARF/OIDC4VCI conformance and bank-length
    sales cycles — Wultra needed a €6.8M Series A and Lissi a €3.5M seed to sell this wave.'
comps:
- name: Lissi
  url: https://www.lissi.id/
  geo: DE
  since: 2019
  traction: '€3.5M seed led by Ventech (tech.eu, Jul 2026); EUDI-wallet connectivity for banks;
    German EUDI Wallet Challenge winner 2025'
  signal: round-lissi
- name: Gataca
  url: https://www.gataca.io/
  geo: ES
  since: 2018
  traction: '750k+ wallet transactions in 2025; undisclosed round for EUDI expansion (Biometric
    Update, Jul 2026); advised the EC'
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
- type: gap-check
  url: https://www.wultra.com/products/digital-identity-wallet-gateway
  note: 'Gap check 2026-08-14 (round-wultra flag): OCCUPIED. Wultra (Prague, EUR 6.8M Series
    A Jun 2026 — Seventure, J&T Ventures, Elevator Ventures) sells the Digital ID Wallet Gateway:
    banks and regulated firms accept and verify EUDI wallet credentials (OIDC4VCI, SD-JWT per
    the ARF) through one gateway instead of integrating dozens of national wallets, alongside
    identity-verification and qualified e-signature products, positioned on the end-2027 acceptance
    obligation. This is exactly the relying-party integration path the record claimed missing.
    De-rank rule applied: gap 0 with incumbent named, status watching.'
  date: '2026-08-14'
  signal: round-wultra
created: '2026-08-13'
updated: '2026-08-19'
---

Czechia must offer an EU Digital Identity Wallet to citizens and businesses by the end of 2026, and within 36 months of the December 2024 implementing acts — i.e. during 2027 — banks, telcos, large platforms and other regulated businesses must accept it wherever strong user authentication is required. The state's deadline creates the private sector's problem: every Czech relying party needs wallet-acceptance flows, and the reg-eidas2 signal notes that banks, utilities, e-shops with KYC obligations and municipalities currently have no integration path beyond following eDoklady's evolution.

Why now: the wallet launch is months away and the acceptance obligation lands within the scoring horizon. KYC-heavy businesses that rebuild onboarding around wallet-presented attestations early can cut verification cost; the rest will scramble against a legal obligation.

Who pays: relying parties — banks and payment institutions first (strong-authentication obligations under PSD2 make them the clearest obligated acceptors), then telcos, utilities and e-commerce with age/identity checks. Product surfaces named in the signal: relying-party registration and integration SDKs, KYC-flow rebuilds, QES and attribute-attestation services.

Existing non-solutions and the incumbent: current bank-ID schemes (Bankovní identita) solve Czech-domestic identity but do not discharge the EUDI acceptance obligation, and eDoklady is the state wallet precursor, not an integration product. The relying-party integration niche itself, however, is occupied: Wultra (Prague) sells the Digital ID Wallet Gateway — accept and verify EUDI wallet credentials (OIDC4VCI, SD-JWT per the ARF) through one gateway instead of integrating dozens of national wallet implementations — plus identity verification and qualified e-signatures, and raised a €6.8M Series A in June 2026 explicitly on the eIDAS2/EUDI acceptance wave. Bankovní identita remains the quasi-incumbent that could absorb the broader market from the scheme side.

Money receipted 2026-08-13: DIA put the national wallet's client part out as an open ~€78M competition in July 2026 — the state is spending seriously and on schedule, which both funds an SI/dev-shop opportunity today and confirms the 2027 relying-party clock.

Updated 2026-08-14: the gap check this record was waiting on ran against the funded-CZ sweep and found the niche taken. Wultra's wallet gateway is precisely the relying-party acceptance product for banks and KYC-bound businesses that the title claims does not exist, sold from Prague with fresh Series A capital. De-rank rule applied: gap stays 0 — now as a checked score with a named incumbent rather than an unchecked one — and the record moves to watching. The acceptance obligation still lands on thousands of relying parties in 2027, so residual room exists downstream of Wultra (sector-specific integrations, non-bank verticals, SI delivery), but the register cannot claim the integration path is missing.
