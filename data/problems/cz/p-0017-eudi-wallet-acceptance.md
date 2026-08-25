---
id: p-0017
region: cz
title: Czech banks must accept the EU digital identity wallet from 2027
category: govtech
geo: CZ-national
score: 6
scores:
  proof: 1
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
locals:
- name: Bank iD
  url: https://bankid.cz/eudiw/
  ico: '09513817'
  since: 2021
  competes: direct
  maturity: established
  evidence: 'public customer count: Bank iD is used by more than 5.3 million Czechs and by
    named state services — katastr nemovitostí, Portál veřejné správy, the tax portals and
    ePortál ČSSZ. Bankovní identita, a.s. has sold relying-party identity acceptance since
    2021 and now sells the wallet leg of it: "Vaši firmu napojíme na EUDIW přes standardní
    Bank iD strukturu", an EUDIW CONNECTOR for firms that want the other attestations, and
    help with the compulsory first registration.'
- name: Wultra
  url: https://www.wultra.com/products/digital-identity-wallet-gateway
  ico: '03643174'
  since: 2026
  competes: direct
  maturity: early
  evidence: 'the Digital ID Wallet Gateway — accept and verify EUDI wallet attestations
    (OIDC4VCI, SD-JWT per the ARF) through one gateway instead of integrating dozens of
    national wallets. Wultra s.r.o. has traded since 2014 and raised a €6.8M Series A in June
    2026, but the gateway itself is a 2026 product against an acceptance obligation that lands
    in 2027.'
sources:
- type: regulation
  name: "eIDAS 2.0 — Regulation (EU) 2024/1183"
  why: "The law behind the deadline: Czechia must offer an EU Digital Identity Wallet by the end of 2026, and regulated sectors must accept it within 36 months of the implementing acts — during 2027."
  url: https://eur-lex.europa.eu/eli/reg/2024/1183/oj
  note: 'reg-eidas2-eudi-wallet: eIDAS 2.0 (Reg. 2024/1183) — Czechia must offer at least
    one EUDI Wallet by end-2026 (24 months after Dec 2024 implementing acts); relying-party
    acceptance obligations for regulated sectors follow within 36 months of the implementing
    acts, i.e. during 2027. Deadlines <18 months.'
  date: '2026-12-31'
  signal: reg-eidas2-eudi-wallet
- type: news
  name: "European Commission — EU Digital Identity Wallet"
  why: "The Commission's own programme page: every Member State offers at least one wallet, launching at the end of 2026, with Czechia building on eDoklady."
  url: https://ec.europa.eu/digital-building-blocks/sites/display/EUDIGITALIDENTITYWALLET/EU+Digital+Identity+Wallet+Home
  note: Commission EUDI page confirms each Member State will offer at least one wallet by
    2026, launch at the end of 2026; CZ builds on eDoklady.
  date: '2025-12-31'
- type: tender
  name: "TED — DIA wallet client tender (~€78M)"
  why: "The Digital and Information Agency put the Czech wallet's client application out to open competition in July 2026 — the largest open Czech IT tender in the window, and proof the state is building on schedule."
  url: https://ted.europa.eu/en/notice/-/detail/453265-2026
  note: 'ted-453265-2026: DIA tendered the client part of the Czech EUDI Wallet (''KLIENTSKÁ
    ČÁST EVROPSKÉ PENĚŽENKY DIGITÁLNÍ IDENTITY'') — open competition, estimated ~€78.2M (~1.9bn
    CZK), published 2 Jul 2026. Largest open IT tender in the CZ TED window; money scored
    2 (open tender far above 5M CZK).'
  date: '2026-07-02'
  signal: ted-453265-2026
- type: gap-check
  name: "Wultra Digital ID Wallet Gateway"
  why: "Prague-based, €6.8M Series A in June 2026 — sells banks and regulated firms one gateway for accepting and verifying EUDI wallet credentials, which is exactly the integration this record is about."
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
- type: contract
  name: "Registr smluv — EUDIW ICS platform signed with MONET+ (~€8.85M)"
  why: "The state trust-services authority signed delivery, development and operation of the ICS system for the European Digital Identity Wallet — the state side is being built under contract, on the clock this record describes."
  url: https://smlouvy.gov.cz/smlouva/38738584
  note: 'hlidac-36404756: Správa státních služeb vytvářejících důvěru contracted MONET+, a.s.
    (IČO 26217783) for "Dodání, rozvoj a provoz systému ICS pro EUDIW", 221,248,500 CZK
    (~€8.85M), signed 10 Jul 2026 (registr smluv 38738584; 2026-08-25 retrospective harvest).
    A second, distinct procurement beside the DIA client-app tender [S3]: the state wallet
    stack is being built, and MONET+ takes a named supplier position in it. Context receipt;
    money already 2 on the open DIA tender [S3], no score moved.'
  date: '2026-07-10'
  signal: hlidac-36404756
  dims: []
- type: gap-check
  name: "Czech EUDI acceptance scan"
  why: "A Czech-language sweep of who sells wallet acceptance to Czech businesses: Bank iD offers an EUDIW tile and an EUDIW CONNECTOR beside Wultra's gateway, and MONET+, Software602 and Aisa International are positioning on the same obligation."
  url: https://bankid.cz/eudiw/
  note: 'Czech-language gap check 2026-08-25, run because the 2026-08-14 check on this record
    recorded no queries[] at all. The Czech position is NOT open, and it is held by a name this
    record deleted on 2026-08-20 for returning zero corpus hits — the corpus blindness
    CONVENTIONS predicts. Bank iD (bankid.cz/eudiw): "Vaši firmu napojíme na EUDIW přes
    standardní Bank iD strukturu" — an EUDIW Dlaždice that connects a relying party through the
    existing Bank iD structure, an EUDIW CONNECTOR for firms wanting attributes beyond identity,
    registration with the Czech national authorities, data reception from EUDIW wallets,
    on-premise installation and ongoing conformance monitoring. Operator Bankovní identita, a.s.,
    IČO 09513817, Smrčkova 2485/4, Praha 8, incorporated 2020-09-15 (ARES), service live since
    2021; more than 5.3 million Czechs use bankovní identita (2026 press), and the most-used
    connected services are state ones — katastr nemovitostí (630k+ sign-ins in H1 2026, 90% of
    them via bank identity), Portál veřejné správy, the tax portals and ePortál ČSSZ. Eleven
    Czech banks issue it. Passes the established test on >= 3 years selling plus a public
    customer count. Also positioning on the same obligation, named but not scored: MONET+
    (already on this record as the ICS supplier, 30 years in applied cryptography, NBÚ and NÚKIB
    clearances), Software602 and Komerční banka as qualified trust service providers on the DIA
    list, and Aisa International. DIA publishes the Seznam udělených akreditací pro správu
    kvalifikovaného systému elektronické identifikace under § 19(1)(d) of Act 250/2017 Sb.
    POSITIVE CONTROL: the same method run at Wultra — this record''s previously sole named
    incumbent — returned the Digital ID Wallet Gateway product page on the first query, so the
    method finds CZ vendors in this niche when they are there; control PASSED. Consequence for
    the score: gap stays 0, now on Bank iD rather than on Wultra alone, because Wultra''s gateway
    is itself a 2026 product and early under the established test while Bank iD has sold
    relying-party identity acceptance since 2021.'
  date: '2026-08-25'
  queries:
    - "česká firma software pro přijímání evropské digitální peněženky EUDI ověření identity relying party"
    - "Bank iD EUDIW napojení poskytovatelů služeb evropská peněženka digitální identity 2026"
    - "český dodavatel řešení pro ověřování dokladů z digitální peněženky eIDAS 2 pro banky e-shopy povinnost 2027"
    - "Bank iD kvalifikovaný správce online identity akreditace zákon 250/2017 počet připojených firem služeb"
    - '"Bank iD" počet připojených služeb firem 2026 miliony uživatelů statistika bankovní identita'
    - "Wultra Digital Identity Wallet Gateway banky přijímání EUDI peněženky Praha"
  checked: [google-cz, ares, own-funded-ledger]
  expires: '2026-11-23'
created: '2026-08-13'
updated: '2026-08-25'
---

Czechia must offer an EU Digital Identity Wallet to citizens and businesses by the end of 2026 [S1,S2], and within 36 months of the December 2024 implementing acts — i.e. during 2027 — banks, telcos, large platforms and other regulated businesses must accept it wherever strong user authentication is required [S1]. The state's deadline creates the private sector's problem: every Czech relying party needs wallet-acceptance flows, and the regulation's own scope names banks, utilities, e-shops with KYC obligations and municipalities among them [S1].

Why now: the wallet launch is months away and the acceptance obligation lands within the scoring horizon [S1,S2]. Businesses that rebuild onboarding around wallet-presented attestations early can cut verification cost; the rest will scramble against a legal deadline.

Who pays: the businesses obliged to accept the wallet — banks and payment institutions first, since the EU payment-services rules (PSD2) already make them authenticate customers strongly, then telcos, utilities and online shops that must check age or identity [S1]. Product surfaces named in the signal: relying-party registration and integration SDKs, KYC-flow rebuilds, QES and attribute-attestation services [S1].

The state's own spend is documented: DIA put the national wallet's client part out as an open ~€78M competition in July 2026 [S3], which both funds an SI/dev-shop opportunity today and confirms the 2027 relying-party clock.

Existing non-solutions and the incumbents: eDoklady is the state wallet precursor, not an integration product [S2]. The relying-party integration niche itself is occupied twice over. Bank iD has connected Czech businesses to bank-issued identity since 2021 — five million people use it, and the state's own portals run on it — and now sells the wallet leg of the same product: an EUDIW tile connecting a firm through the existing Bank iD structure, an EUDIW CONNECTOR for firms wanting more than identity, and help with the compulsory first registration [S6]. Beside it, Wultra (Prague) sells the Digital ID Wallet Gateway — accept and verify wallet attestations (OIDC4VCI, SD-JWT per the ARF) through one gateway instead of integrating dozens of national wallets — and raised a €6.8M Series A in June 2026 on the eIDAS2/EUDI acceptance wave [S4]. MONET+, Software602 and Aisa are positioning on the same obligation [S6].

Solved elsewhere: two funded European vendors already build the acceptance layer — Lissi (Germany) makes EUDI-wallet connectivity for banks, and Gataca (Spain) runs wallet transactions at volume. Neither is settled: the obligation they build for has not landed yet, so this is a market being proven now rather than one already proven — a good moment to join, and a thin basis for betting a company. The Czech position is not open either — Bank iD and Wultra both sell a relying-party path today [S4,S6].

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: the who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "relying parties" now reads "the businesses obliged to accept the wallet", and the bare "PSD2" is now "the EU payment-services rules (PSD2)". No `fix:` was authored here: the argument closes with the local position held by Wultra and names no product an entrant would build that Wultra does not already sell, so the field is left absent rather than filled with something vague — the template renders nothing when it is. Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: the 2026-08-25 retrospective harvest added the signed ICS-platform contract — the state trust-services authority contracted MONET+ for ~€8.85M to build and run the EUDIW ICS system [S5], a second procurement beside the DIA client tender [S3]. Context receipt; no score moved. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. A Czech-language check was run against this record for the first time and recorded with its queries, its surfaces and a passing positive control [S6]; the earlier gap check [S4] carried none, which the build gate now treats as a missing receipt. It found the niche occupied twice over, and by a name this record removed on 2026-08-20 for returning no hits in the signal corpus: Bank iD sells an EUDIW tile and an EUDIW CONNECTOR to relying parties, plus help with the compulsory first registration. Bankovní identita, a.s. (IČO 09513817) has sold relying-party identity acceptance since 2021, is used by more than 5.3 million people and carries the state's own portals, so it passes the established test and `scores.gap` stays 0 — now on the strongest local receipt on file rather than on Wultra alone. Wultra sits in `locals[]` as early, and the reason is worth recording: Wultra s.r.o. has traded since 2014 and raised a Series A in June 2026, but the Digital ID Wallet Gateway itself is a 2026 product against an obligation that lands in 2027, and SCORING.md defines `since` as the year a player started selling THIS product. `scores.proof` 0 → 1: Lissi and Gataca cite only a seed round and a transaction count, neither of which is a limb the test reads, so the foreign field here is early too — rung 1, which also clears the proof-0-above-a-funded-comp contradiction the checker was reporting. `score` 5 → 6. Fifth pass this date, merged here: `locals[]` converted from `status:` to the orthogonal `competes:` + `maturity:` pair. Both entries are `competes: direct` — Bank iD sells the wallet leg of relying-party acceptance and Wultra sells a gateway for accepting and verifying wallet attestations, which is this record's product for this record's buyer — with maturities unchanged. `scores.gap` stays 0 on Bank iD, direct and established. No player was ever excluded from this ledger, so there is nothing to restore.
2026-08-13 · money receipted — DIA's ~€78M open competition for the national wallet's client part was put on the ledger [S3]; the state is spending seriously and on schedule. The substance now sits in How big above rather than here.

2026-08-14 · de-rank — The gap check this record was waiting on ran against the funded-CZ sweep and found the niche taken [S4]. Wultra's wallet gateway is precisely the relying-party acceptance product for banks and KYC-bound businesses that the title claimed does not exist, sold from Prague with fresh Series A capital [S4]. De-rank rule applied: gap stays 0 — now as a checked score with a named incumbent rather than an unchecked one — and the record moves to watching. The acceptance obligation still lands on thousands of relying parties in 2027, so residual room exists downstream of Wultra (sector-specific integrations, non-bank verticals, SI delivery), but the register cannot claim the integration path is missing.

2026-08-20 · evidence audit and title sweep — Two blocks recorded on this date, merged here. Removed the absence claim attributed to the reg-eidas2 signal — that banks, utilities, e-shops with KYC obligations and municipalities "currently have no integration path beyond following eDoklady's evolution". The signal says those parties need wallet-acceptance flows; it never says a path is missing, and the record's own gap check [S4] shows Wultra selling exactly that path. The who-list itself is supported and stays, now cited to [S1]. Also removed: both mentions of Bankovní identita, a name that returns no hits anywhere in the signal corpus and appears in no source note on this record, so neither the "solves domestic identity" clause nor the quasi-incumbent claim had anything behind it. The title still asserted that relying parties "have no integration path" — the very claim removed from the body in the same pass — and that clause is now gone too. A retraction that leaves the claim standing in the most-read line on the page is not a retraction.
