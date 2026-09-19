---
id: p-0017
region: cz
title: 'Czech banks must accept the EU''s digital ID app by the end of 2027'
brief: 'Czechia launches the app at the end of 2026 [S1,S2]. Banks, phone companies and big platforms will have to accept it when customers prove who they are, and each needs a way to check it [S1].'
solution: 'Build a service inside a bank''s customer sign-up that checks the EU digital ID app, as 2 companies already do in 2 other countries.'
good_for: 'Engineers who know digital identity and can sell to banks.'
category: govtech
geo: CZ-national
score: 3
scores:
  proof: 1
  money: 0
  urgency: 2
  demand: 0
  gap: 0
status: watching
entry:
  level: very-hard
  buyer: large-firms
  permission: registration
  incumbents: direct
  integration: certified
  money: outside-money
  why: 'Easier: EU law makes regulated firms accept the app, the state is building it on schedule, and firms in Germany and Spain already sell the check. Harder: each firm must register and pass conformance testing; bank sales are slow, so outside money comes before revenue; and a Czech bank-identity service already sells it.'
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
  evidence: 'Used by more than 5.3 million Czechs and by state services including the land
    registry, the public administration portal, the tax portals and the social-security
    e-portal. Bankovní identita, a.s. has sold identity acceptance to relying parties since
    2021 and now sells the wallet leg of it: "Vaši firmu napojíme na EUDIW přes standardní Bank
    iD strukturu", a connector for firms that want the other attestations, and help with the
    compulsory first registration.'
- name: Wultra
  url: https://www.wultra.com/products/digital-identity-wallet-gateway
  ico: '03643174'
  since: 2026
  competes: direct
  maturity: early
  evidence: 'The Digital ID Wallet Gateway: accept and verify EU digital-identity wallet
    attestations (OIDC4VCI and SD-JWT, per the EU wallet reference framework) through one
    gateway instead of integrating dozens of national wallets. Wultra s.r.o. has traded since
    2014 and raised a €6.8M Series A in June 2026, but the gateway itself is a 2026 product
    against an acceptance obligation that lands in 2027.'
sources:
- type: regulation
  name: "eIDAS 2.0 — Regulation (EU) 2024/1183"
  gist: "the law and its 2027 clock"
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
  gist: "the end-2026 launch date"
  why: "The Commission's own programme page: every Member State offers at least one wallet, launching at the end of 2026, with Czechia building on eDoklady."
  url: https://ec.europa.eu/digital-building-blocks/sites/display/EUDIGITALIDENTITYWALLET/EU+Digital+Identity+Wallet+Home
  note: Commission EUDI page confirms each Member State will offer at least one wallet by
    2026, launch at the end of 2026; CZ builds on eDoklady.
  date: '2025-12-31'
- type: tender
  name: "TED — DIA wallet client tender (~€78M)"
  gist: "the €78M state tender"
  why: "The Digital and Information Agency put the Czech wallet's client application out to open competition in July 2026 — the largest open Czech IT tender in the window, and proof the state is building on schedule."
  url: https://ted.europa.eu/en/notice/-/detail/453265-2026
  note: 'ted-453265-2026: DIA tendered the client part of the Czech EUDI Wallet (''KLIENTSKÁ
    ČÁST EVROPSKÉ PENĚŽENKY DIGITÁLNÍ IDENTITY'') — open competition, estimated ~€78.2M (~1.9bn
    CZK), published 2 Jul 2026. Largest open IT tender in the CZ TED window; money scored
    2 (open tender far above 5M CZK). Superseded 2026-09-19: on the new ladder this is public
    money nearby. It buys the state''s own wallet, not a bank''s acceptance of it, and banks
    cannot bid for it as buyers, so it earns no point and money is 0.'
  date: '2026-07-02'
  signal: ted-453265-2026
- type: gap-check
  name: "Wultra Digital ID Wallet Gateway"
  gist: "the Prague gateway vendor"
  why: "Prague-based, €6.8M Series A in June 2026 — sells banks and regulated firms one gateway for accepting and verifying EUDI wallet credentials, which is exactly the check this problem is about."
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
  gist: "the €8.85M state contract"
  why: "The state trust-services authority signed delivery, development and operation of the ICS system for the European Digital Identity Wallet — the state side is being built under contract, on the clock set out under Why now."
  url: https://smlouvy.gov.cz/smlouva/38738584
  note: 'hlidac-36404756: Správa státních služeb vytvářejících důvěru contracted MONET+, a.s.
    (IČO 26217783) for "Dodání, rozvoj a provoz systému ICS pro EUDIW", 221,248,500 CZK
    (~€8.85M), signed 10 Jul 2026 (registr smluv 38738584; 2026-08-25 retrospective harvest).
    A second, distinct procurement beside the DIA client-app tender [S3]: the state wallet
    stack is being built, and MONET+ takes a named supplier position in it. Context receipt;
    money already 2 on the open DIA tender [S3], no score moved. Superseded 2026-09-19: [S3] no
    longer earns a point either; money is 0, as no price for a firm accepting the wallet is on
    file.'
  date: '2026-07-10'
  signal: hlidac-36404756
  dims: []
- type: gap-check
  name: "Czech EUDI acceptance scan"
  gist: "the Czech acceptance sweep"
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
- type: contract
  name: "Registr smluv — support for the national identity system (~€5.43M)"
  gist: "the €5.43M identity-system support"
  why: "The Digital and Information Agency pays NAKIT, the state IT agency, about €5.43M to keep running the national identity system the wallet plugs into."
  url: https://smlouvy.gov.cz/smlouva/36243132
  note: 'hlidac-36243132: DIA contracted NAKIT for operational support of the NIA national
    identity information system, ~€5.43M — the state keeps funding the identity stack the
    wallet plugs into, context beside the MONET+ EUDIW ICS build [S5]. No score moves.'
  date: '2026-08-28'
  signal: hlidac-36243132
created: '2026-08-13'
updated: '2026-09-19'
---

Banks and other regulated firms must soon accept the EU's digital identity app wherever a customer proves who they are [S1].

- Czechia's app, a wallet for identity documents, launches at the end of 2026 [S1,S2].
- Each firm must build a check that verifies what the app shows [S1].
- The duty covers banks and payment firms, phone companies, utilities and big platforms [S1].

The law is Regulation (EU) 2024/1183, known as eIDAS 2.0, the EU's updated rules on electronic identity [S1]. The app it sets up is the EU Digital Identity Wallet, a phone app that holds identity documents the state issues [S1,S2].

- Banks and payment firms already have to check who a customer is under the EU's payment-services rules, known as PSD2 [S1].
- E-shops that must check a buyer's identity, and towns, need the same check [S1].
- How many businesses the duty covers is not published.

Existing non-solutions: The Czech field is taken: a bank-identity service already sells firms a connection to the app, and a Prague firm sells a gateway [S4,S6].

- The login Czech banks issue now sells firms a connection to the app [S6].
- The same service helps a firm with its compulsory first registration [S6].
- A Prague firm sells one gateway to the wallets of every EU country [S4].

The bank login also sells a connector for details beyond identity, and state services already run on it [S6]. The Prague firm's gateway lets a bank accept and verify wallets through one connection, instead of connecting to dozens of national wallets [S4].

- eDoklady, the state's existing app for digital documents, is what the Czech wallet builds on; it is not a product a business buys [S2].
- Three more Czech firms are positioning on the same duty: Software602, Aisa International, and MONET+ (the cryptography firm building the app's core state system) [S5,S6].

Why now: Banks and other regulated firms run out of time at the end of 2027, a year after customers get the app [S1,S2].

- Each bank must build a new check into its customer sign-up [S1].
- Each must first register with Czech authorities to accept the app [S6].
- Without a gateway, a firm connects to dozens of national wallets [S4].

A firm that has not built its check by then misses a legal deadline [S1]. The dates come from the EU regulation and the European Commission's own plan [S1,S2]:

- In December 2024 the EU adopted the implementing acts that start both clocks [S1].
- By the end of 2026 Czechia must offer at least one wallet, and the Commission puts the launch at the end of 2026 [S1,S2].
- During 2027, within 36 months of those implementing acts, regulated firms must accept the app [S1].

Who pays: No firm is yet shown paying to accept the app, but the state is paying to build it [S3,S5].

- The state tendered the app's phone side at about €78M in July 2026 [S3].
- It signed about 221M CZK for the app's core system that month [S5].
- Online services have bought bank-identity checks from a Czech seller since 2021 [S6].

The firms that will pay are the ones that must accept the app, listed under [The opportunity](#opportunity) [S1]. The duty creates work in four places: registering as a firm that accepts the app, kits that connect it to the firm's systems, rebuilt customer sign-up checks, and qualified electronic signatures, the kind EU law treats as equal to a handwritten one [S1].

- The tender, an open competition, came from the Digital and Information Agency, the state's digital agency, and was the largest open Czech IT tender in the EU's tenders journal at the time [S3].
- The 221M CZK contract, about €8.85M, went from the state trust-services authority to MONET+, a Czech firm with 30 years in cryptography, to build and run the app's core system [S5,S6].
- The same agency also pays NAKIT (the state IT agency) about €5.43M to support the national identity system the app plugs into [S7].

Solved elsewhere: Two funded European firms, in Germany and Spain, already sell wallet acceptance, before the duty to accept the app lands in 2027 [S1].

- The German firm builds wallet connections for banks.
- The Spanish firm runs wallet checks at volume and has advised the European Commission.

Neither sells against a duty in force yet, so the model is still being proven [S1]. In Czechia the same position is already taken; see [Market gap](#competition).

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: the who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "relying parties" now reads "the businesses obliged to accept the wallet", and the bare "PSD2" is now "the EU payment-services rules (PSD2)". No `fix:` was authored here: the argument closes with the local position held by Wultra and names no product an entrant would build that Wultra does not already sell, so the field is left absent rather than filled with something vague — the template renders nothing when it is. Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: the 2026-08-25 retrospective harvest added the signed ICS-platform contract — the state trust-services authority contracted MONET+ for ~€8.85M to build and run the EUDIW ICS system [S5], a second procurement beside the DIA client tender [S3]. Context receipt; no score moved. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. A Czech-language check was run against this record for the first time and recorded with its queries, its surfaces and a passing positive control [S6]; the earlier gap check [S4] carried none, which the build gate now treats as a missing receipt. It found the niche occupied twice over, and by a name this record removed on 2026-08-20 for returning no hits in the signal corpus: Bank iD sells an EUDIW tile and an EUDIW CONNECTOR to relying parties, plus help with the compulsory first registration. Bankovní identita, a.s. (IČO 09513817) has sold relying-party identity acceptance since 2021, is used by more than 5.3 million people and carries the state's own portals, so it passes the established test and `scores.gap` stays 0 — now on the strongest local receipt on file rather than on Wultra alone. Wultra sits in `locals[]` as early, and the reason is worth recording: Wultra s.r.o. has traded since 2014 and raised a Series A in June 2026, but the Digital ID Wallet Gateway itself is a 2026 product against an obligation that lands in 2027, and SCORING.md defines `since` as the year a player started selling THIS product. `scores.proof` 0 → 1: Lissi and Gataca cite only a seed round and a transaction count, neither of which is a limb the test reads, so the foreign field here is early too — rung 1, which also clears the proof-0-above-a-funded-comp contradiction the checker was reporting. `score` 5 → 6. Fifth pass this date, merged here: `locals[]` converted from `status:` to the orthogonal `competes:` + `maturity:` pair. Both entries are `competes: direct` — Bank iD sells the wallet leg of relying-party acceptance and Wultra sells a gateway for accepting and verifying wallet attestations, which is this record's product for this record's buyer — with maturities unchanged. `scores.gap` stays 0 on Bank iD, direct and established. No player was ever excluded from this ledger, so there is nothing to restore. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed.
2026-08-13 · money receipted — DIA's ~€78M open competition for the national wallet's client part was put on the ledger [S3]; the state is spending seriously and on schedule. The substance now sits in How big above rather than here.

2026-08-14 · de-rank — The gap check this record was waiting on ran against the funded-CZ sweep and found the niche taken [S4]. Wultra's wallet gateway is precisely the relying-party acceptance product for banks and KYC-bound businesses that the title claimed does not exist, sold from Prague with fresh Series A capital [S4]. De-rank rule applied: gap stays 0 — now as a checked score with a named incumbent rather than an unchecked one — and the record moves to watching. The acceptance obligation still lands on thousands of relying parties in 2027, so residual room exists downstream of Wultra (sector-specific integrations, non-bank verticals, SI delivery), but the register cannot claim the integration path is missing.

2026-08-20 · evidence audit and title sweep — Two blocks recorded on this date, merged here. Removed the absence claim attributed to the reg-eidas2 signal — that banks, utilities, e-shops with KYC obligations and municipalities "currently have no integration path beyond following eDoklady's evolution". The signal says those parties need wallet-acceptance flows; it never says a path is missing, and the record's own gap check [S4] shows Wultra selling exactly that path. The who-list itself is supported and stays, now cited to [S1]. Also removed: both mentions of Bankovní identita, a name that returns no hits anywhere in the signal corpus and appears in no source note on this record, so neither the "solves domestic identity" clause nor the quasi-incumbent claim had anything behind it. The title still asserted that relying parties "have no integration path" — the very claim removed from the body in the same pass — and that clause is now gone too. A retraction that leaves the claim standing in the most-read line on the page is not a retraction.

2026-09-02 · plain-language pass — Six acronyms replaced with plain words at first use — KYC, QES, DIA, SI, EUDIW, EUDI — plus glosses on the wallet and MONET+; OIDC4VCI, SD-JWT and ARF are gone from the body. Argument 448 to 385 words, markers 12 to 14: the 221M CZK state contract [S5] is now cited in the body, with Lissi's and Gataca's figures. Gists added to all six sources. No score, status, note or marker touched.

2026-09-10 · likely solution — Added the one-sentence `solution:`, now required on every record and always shown as the likely solution, compressed from locals[], the who-pays paragraph and the solved-elsewhere paragraph. This reverses the deliberately absent `fix:` recorded on 2026-08-25. No claim, score or source changed.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as three lines under the headline: a `brief:` on who is stuck and what forces it now, the `solution:` as a call to action starting "Build", and a new `good_for:` line. Previous title, verbatim: "Czech banks must accept the EU digital identity wallet from 2027". Previous solution, verbatim: "One connection through which a bank or other regulated business accepts the EU digital identity wallet: it handles the compulsory registration as an accepting party, receives what the customer's wallet app presents, and verifies it whatever country issued it." There was no previous brief or good_for. Checked against the sources before writing: "from 2027" became "by the end of 2027", because the duty to accept runs 36 months from the December 2024 implementing acts rather than starting on 1 January 2027 [S1], and the headline now names the other regulated firms the duty covers, not banks alone [S1]. The brief names only the sectors the regulation signal names — banks, phone companies and large platforms [S1] — and the end-2026 launch is the Commission's own date [S2]. "As companies already do in Germany and Spain" rests on Lissi and Gataca, both young; the duty they build for has not landed yet [S1]. The compulsory registration step left the solution to keep it short; it is still in the body and in the Bank iD ledger line. No score, status, source, note, marker or body sentence changed. Simplified for the front page: Title before: "Czech banks and other regulated firms must accept the EU's new digital ID app by the end of 2027" After: "Czech banks must accept the EU's digital ID app by the end of 2027". Brief before: "Czechia launches the app at the end of 2026, and banks, phone companies and large online platforms must then accept it wherever customers prove who they are [S1,S2]. Each needs a way to receive and check what the app shows [S1]." After: "Czechia launches the app at the end of 2026 [S1,S2]. Banks, phone companies and big platforms will have to accept it when customers prove who they are, and each needs a way to check it [S1]." Solution before: "Build a service that plugs into a bank's customer sign-up and checks the EU digital ID app, as companies already do in Germany and Spain." After: "Build a service inside a bank's customer sign-up that checks the EU digital ID app, as companies already do abroad." The headline dropped "and other regulated firms" to stay short; the brief still names phone companies and big platforms [S1]. "As companies already do in Germany and Spain" became "as companies already do abroad", per the plural rule. No fact, number or claim was added; no score, status, source, note, marker in the body or body sentence changed. Same date, good-for opener (owner: "Good for should always start with a person"): "Security engineers who know digital identity and can sell to banks." became "Engineers who know digital identity and can sell to banks." — same meaning, person first. Same date, abroad count (owner: fill "do abroad" with "X companies do in Y countries"): solution "…checks the EU digital ID app, as companies already do abroad." became "…checks the EU digital ID app, as 2 companies already do in 2 other countries." Counted from comps[] only: Lissi (comps[0], geo DE), wallet connectivity for banks; Gataca (comps[1], geo ES), wallet verification with 750,000+ transactions in 2025, which the body counts as selling wallet acceptance but which is not recorded selling to banks specifically, so it is counted for the checking half. None excluded. Countries are where the two are based.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence and its three most important items, with the rest below as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity holds the duty, the app, the check each firm must build and the sectors covered, with the regulation's name, the PSD2 duty, e-shops and towns, and the unpublished count below [S1,S2]. Competition names no ledger company: the bank-identity service and the Prague gateway are described by what each sells, and their user count, start year, state customers, funding and product dates stay in their `locals[]` rows [S4,S6]; eDoklady and the three other Czech firms positioning on the duty stay in the detail [S2,S5,S6]. Why now opens on the end-2027 cut-off, then three pain items (the new sign-up check, the compulsory registration, dozens of national wallets), then the December 2024, end-2026 and 2027 dates as plain bullets [S1,S2,S4,S6]. Willing to pay now says whether anyone pays: no firm is yet shown paying to accept the app, the state pays to build it, and online services already buy bank-identity checks [S3,S5,S6]; the tender's buyer, the MONET+ contract and the national-identity support contract sit below [S3,S5,S7]. Validated abroad names neither foreign firm: their seed round, challenge win, transaction count and advisory role stay in their `comps[]` rows, which were already their only receipt (no source on file carries them). `entry.why` is now "Easier: … Harder: …" and names the gates the level derives from (registration, conformance testing, outside money) plus the established local seller; the seller's name and user count left it for its ledger row. Added from sources already on file: the NAKIT support contract for the national identity system, now cited in the body and given a public name, gist and why [S7]; "dozens of national wallets" as a pain [S4]; the compulsory registration as a pain [S6]. S4.why and S5.why said "this record" and now say "this problem" and "under Why now". Corrected against the sources rather than the old sentences: "They buy registration as an accepting party, integration kits, rebuilt sign-up checks and qualified electronic signatures" became "The duty creates work in four places", because [S1]'s signal lists these as the market the duty creates, not as purchases anyone has made; "banks and payment institutions first … then telcos" lost "first", because [S1] gives every regulated sector the same 36-month clock and no order; "Early movers cut verification cost" was cut, because no source on file supports it; the Prague gateway no longer verifies "every national wallet" but replaces connecting to dozens of them, the gateway's own words [S4]. Flagged as inference: that firms get about a year between the app's launch and their own deadline rests on the end-2026 launch [S2] and the 36-month clock from the December 2024 acts [S1]; that a firm without its check by then "misses a legal deadline" is our reading of [S1]; and that banks and payment firms already must check who a customer is under PSD2 is kept from the earlier text, though [S1]'s note does not state it and the regulation's page did not load for a check. No `process` block added: this is a new duty, and no source on file describes who does which step of a customer check today (data/RECORD-TEMPLATE.md, Figures). No score, status, `entry` gate value, `sources[]` order, `note:`, title, brief, solution or good_for changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 3 → 2, Willing to pay 2 → 0 and `score` 6 → 3, so the band moves FAIR → FAINT. Why now was 3 as deadline 2 plus the freshness point, which is retired. It is now 2 (a firm deadline): eIDAS 2.0 is an EU regulation, binding as published, and it obliges regulated firms such as banks to accept the wallet (REAL). Their deadline falls during 2027, 36 months after the December 2024 implementing acts, inside 18 months of this date (CLOSE) [S1]. It stops short of 3: the regulation leaves penalties to member states, and no Czech sanction or enforcement is on file (TEETH). Willing to pay was 2 on the open DIA tender above 5M CZK [S3], which is now public money nearby. Tagging pass, every source on file that might show someone paying for this job: the DIA wallet-client tender [S3], the MONET+ core-system contract [S5] and the NAKIT support contract [S7] all pay for the state's own wallet and identity system. None buys a bank's or a regulated firm's acceptance of the wallet, the payer is the state rather than the buyer, and banks are not eligible for that money. Online services have bought bank-identity checks from a Czech seller since 2021, but no amount is on file [S6]. No receipt could be written, so money is 0, as the worksheet had it. [S3]'s and [S5]'s notes named the old money rung and now carry the correction. Why now prose re-read: it names the end-2027 cut-off and says a late firm misses a legal deadline, with no fine claimed, which fits rung 2. Willing to pay already says no firm is yet shown paying, so it stands. `[Competition](#competition)` became `[Market gap](#competition)` in Solved elsewhere. No other score, status, entry or body sentence changed.
