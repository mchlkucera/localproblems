---
id: p-0026
region: cz
title: Small Czech water utilities each buy smart metering alone
category: environment
geo: CZ-national
score: 3
scores:
  proof: 0
  money: 2
  urgency: 1
  demand: 0
  gap: 0
status: watching
build:
  capital: funded
  first_revenue: year-plus
  builder: funded-team
  note: 'Utility-grade metering, telemetry and data infrastructure sold to small public utilities through tenders against named incumbents — procurement cycles and integration depth put payroll well before revenue.'
comps: []
locals:
- name: Softlink (CEM Smart)
  url: https://www.softlink.cz/nase-sluzby-vyuzivaji/vodarenske-spolecnosti
  ico: '27109682'
  since: 2003
  status: established
  evidence: 'named customers — softlink.cz lists vodárenské společnosti as a served segment
    and states CEM Smart has read Pražské vodovody a kanalizace meters remotely since 2016 at
    ~1M transactions a day, verified live 2026-08-24 [S7]; ARES registration 2003-12-10'
- name: VODÁRENSKÁ AKCIOVÁ SPOLEČNOST
  url: https://www.vodarenska.cz/
  ico: '49455842'
  since: 1993
  status: established
  evidence: 'named customers — data/lookup/cz-contract-parties.jsonl pairs it as supplier with
    Vodovody a kanalizace Židlochovicko as buyer, the operates-metering-as-a-service
    relationship the scan asserted [S6,S7]; ARES registration 1993-12-01'
- name: Popron Systems (SMG Water)
  url: https://www.popron.cz/
  ico: '61855162'
  since: 1994
  status: established
  evidence: 'named customers — VaK Pardubice amended its Smart Metering licence agreement with
    Popron Systems in June 2026 [S5]; ARES registration 1994-09-06'
- name: SUEZ Water CZ
  url: https://www.suez.cz/
  ico: '11901403'
  since: 2021
  status: established
  evidence: 'named customers — VaK Břeclav signed amendment No. 1 to its framework contract
    with SUEZ Water CZ for remote-readout devices and support [S4]; ARES registration
    2021-10-01, so the three-year limb is met'
- name: Severočeské vodovody a kanalizace
  url: https://www.scvk.cz/
  ico: '49099451'
  since: 1993
  status: established
  evidence: 'named customers — město Most bought a Smart Metering supplementary service from
    it as incumbent operator in August 2026 [S5]; ARES registration 1993-10-01'
- name: Techem CZ
  url: https://www.techem.cz/
  ico: '61852121'
  since: 1994
  status: early
  evidence: 'EARLY on receipts only — named in the supply scan as serving the housing tier
    [S6], but no named Czech customer, no public-buyer pair in
    data/lookup/cz-contract-parties.jsonl, no round and no state listing is on file here'
sources:
- type: tender
  name: "TED — Ivančice water association smart metering (~€1.2M)"
  why: "A municipal water association opened a competition for smart metering across its network in summer 2026."
  url: https://ted.europa.eu/en/notice/-/detail/430180-2026
  note: 'ted-430180-2026: Svazek vodovodů a kanalizací Ivančice — OPEN competition ~€1.2M
    (~29M CZK) for smart-metering installation on the water network (Jun–Jul 2026). Open tender
    ≥5M CZK: money 2.'
  date: '2026-06-24'
  signal: ted-430180-2026
- type: tender
  name: "TED — VaK Kroměříž smart metering (~€1.3M)"
  why: "Kroměříž built network smart metering and Bruntál tendered a water data dispatch in the same ten weeks; the signed Kroměříž contract runs ~21.4M CZK."
  url: https://ted.europa.eu/en/notice/-/detail/372049-2026
  note: 'ted-372049-2026: VaK Kroměříž awarded ~€1.3M to build water-network smart metering
    (Jun 2026); VaK Bruntál tendered a water data dispatch (~€0.5M, Jul 2026) — three small-utility
    metering/telemetry buys in ten weeks. Signed Kroměříž contract in registr smluv: ~21.4M
    CZK (smlouvy.gov.cz/smlouva/38292247).'
  date: '2026-06-01'
  signal: ted-372049-2026
- type: contract
  name: "Registr smluv — VaK Židlochovicko (~8.4M CZK)"
  why: "One utility signed two contracts the same day — meters and readers, then system operation and support — the supply-plus-managed-operation split this record is about."
  url: https://smlouvy.gov.cz/smlouva/39041762
  note: 'hlidac-39041762: VaK Židlochovicko signed two contracts on 30 Jul 2026 — meter/reader
    supply (~4.8M CZK) plus system operation & support (~3.6M CZK) — a FOURTH distinct small-utility
    buyer, procuring exactly the supply+managed-operation split the record predicts; Pražská
    vodohospodářská společnost signed ~12M CZK in June.'
  date: '2026-07-30'
  signal: hlidac-39041762
- type: contract
  name: "Registr smluv — VaK Břeclav / SUEZ framework"
  why: "A fifth utility with a live smart-metering relationship, running remote-readout devices and support off a supplier framework."
  url: https://smlouvy.gov.cz/smlouva/38219601
  note: 'hlidac-38219601: VaK Břeclav signed amendment No. 1 to a framework contract with
    SUEZ Water CZ for remote-readout devices and support (Jun 2026) — a FIFTH distinct utility
    with a live smart-metering relationship, running on a supplier framework.'
  date: '2026-06-02'
  signal: hlidac-38219601
- type: contract
  name: "Registr smluv — VaK Pardubice / Popron licence"
  why: "A sixth utility amending its Smart Metering licence, and the town of Most adding a Smart Metering service from its incumbent operator — seven distinct buyers, each contracting alone."
  url: https://smlouvy.gov.cz/smlouva/38618416
  note: 'hlidac-38618416: VaK Pardubice amended its Smart Metering licence agreement with
    Popron Systems (Jun 2026) — sixth distinct utility; město Most added a Smart Metering
    supplementary service from its incumbent operator Severočeské vodovody a kanalizace in
    August (hlidac-39039418) — seventh. The pattern the record predicted is now receipted
    across seven buyers: supply, licence, and managed-operation contracts, each utility alone.'
  date: '2026-06-30'
  signal: hlidac-38618416
- type: gap-check
  name: "Softlink CEM Smart and the Czech metering-service field"
  why: "Names who already sells this here: Softlink's metering-data platform with water-utility references, VODÁRENSKÁ AKCIOVÁ SPOLEČNOST operating metering as a service, Popron's SMG Water, and SUEZ and Techem."
  url: https://www.softlink.cz/reseni/cem-smart/
  note: 'Gap check 2026-08-13: the managed-service position is NOT empty — Softlink (CZ) sells
    the CEM Smart metering-data platform with water-utility references, VODÁRENSKÁ AKCIOVÁ
    SPOLEČNOST operates metering as a service (it runs Židlochovicko''s system per hlidac-39041590),
    Popron Systems sells SMG Water, and SUEZ/Techem serve the utility and housing tiers. Local
    players named: gap stays 0 and status moves to watching per the de-rank rule.'
  date: '2026-08-13'
- type: gap-check
  name: "Softlink — water utilities served"
  why: "Softlink's own segment page, taken live: it states CEM Smart has read Pražské vodovody a kanalizace meters remotely since 2016 at roughly a million transactions a day."
  url: https://www.softlink.cz/nase-sluzby-vyuzivaji/vodarenske-spolecnosti
  note: 'Incumbent re-verify 2026-08-24: the S6 product URL (/reseni/cem-smart/) now returns
    404 after a softlink.cz restructure, so the de-rank receipt was re-taken live. Softlink
    is still selling: the site lists vodárenské společnosti as a served segment, states the
    CEM Smart platform has run remote water-meter readouts for Pražské vodovody a kanalizace
    since 2016 at ~1M daily transactions, and the CEM software family now lives under /software-cem.
    Mechanical cross-check: data/lookup/cz-contract-parties.jsonl pairs VODÁRENSKÁ AKCIOVÁ
    SPOLEČNOST as supplier with Vodovody a kanalizace Židlochovicko as buyer — the exact
    operates-as-a-service relationship the S6 note asserted. Gap stays 0, incumbents unchanged.'
  date: '2026-08-24'
- type: contract
  name: "Benešov — 112-sensor remote-reading pilot"
  why: "A small utility association pilots remote water-meter reading with 2 antennas and 112 sensors — one more utility solving telemetry alone, at pilot scale."
  url: https://smlouvy.gov.cz/smlouva/38735844
  note: 'hlidac-36402144: Společná voda d.s.o., Benešov, €5,987 pilot, Jul 2026. One of ~15
    small municipal meter orders and frameworks in the 2026-08-24 run alone (e.g.
    hlidac-36650670 Říčany, hlidac-36306864 and -36810238 Hlučín, hlidac-36785330 Turnov,
    ted-581645-2026 Brno Nový Lískovec, Brno-střed framework pacts hlidac-36737750 and
    -36785954) — the one-tender-at-a-time pattern this record describes, continuing. Backs
    no score point; money already rests on the open Ivančice tender.'
  date: '2026-07-01'
  signal: hlidac-36402144
  dims: []
- type: gap-check
  name: "Czech water-metering supply — coverage recorded"
  why: "The earlier checks named the incumbents but never wrote down what was searched. This one does, and it widens the picture: VAS sells remote meter reading as a published service, ČEVAK runs eMR Fusion 2.0, and AQUA SERVIS, VODÁRNA PLZEŇ, OVAK and KAPKA vodoměry all operate the same thing."
  note: 'Coverage receipt 2026-08-25. [S6] and [S7] named real incumbents but recorded no
    queries, so gap 0 rested on a check whose reach nobody could judge; this entry supplies the
    coverage rather than a new verdict. A plain descriptive Czech query for remote water-meter
    reading run as a service returned, on the first page: VODÁRENSKÁ AKCIOVÁ SPOLEČNOST''s own
    "SMART vodoměry" and "VAS nově nabízí dálkové odečty vodoměrů" pages, stating it sells the
    service with online consumption, leak detection and alerting; ČEVAK''s remote-readout page,
    which states it has standardised on the eMR Fusion 2.0 software for managing the data; AQUA
    SERVIS running radio collection into its own dispatch for billing; VODÁRNA PLZEŇ piloting an
    IoT-based system; Ostravské vodárny a kanalizace on smart meters in Ostrava; and KAPKA
    vodoměry supplying NB-IoT and wMBus 169 MHz readout. POSITIVE CONTROL PASSED: VODÁRENSKÁ,
    the incumbent [S6] and [S7] already name, surfaced first and unprompted. NOTHING RESCORED.
    gap was already 0 and stays 0 on the established players in locals[]; ČEVAK, AQUA SERVIS,
    VODÁRNA PLZEŇ, OVAK and KAPKA are added to the picture, not to the score, and are left out
    of locals[] because no limb of the established test is receipted for them here.'
  url: https://vodarenska.cz/smart-vodomery/
  date: '2026-08-25'
  queries:
    - "provozování dálkových odečtů vodoměrů jako služba pro vodárny český dodavatel smart metering platforma"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-23'
created: '2026-08-13'
updated: '2026-08-25'
---

Czech water supply is run by hundreds of VaK companies and municipal svazky, most of them small [S2], and they are digitizing metering the only way they know: one infrastructure tender at a time. Three buyers did exactly that inside a single ten-week window. Kroměříž awarded about €1.3M for network smart metering and Bruntál tendered a water data dispatch [S2]. The Ivančice association opened a competition of about €1.2M for the same thing [S1]. Each is procuring hardware, telemetry, a data platform and integration as its own bespoke project.

Why now: a svazek with three employees cannot run a data platform; each project embeds years of operational dependence on whichever integrator won.

Who pays: the utilities themselves via documented public procurement — today an integrator/dev-shop market in which each small utility contracts supply, licences and operation separately (seven distinct buyers documented by August 2026) [S3,S5].

Existing non-solutions: the managed-service position is not empty, and the firms holding it are not new. Softlink has sold since 2003, and its CEM Smart platform has read Pražské vodovody a kanalizace meters remotely since 2016 at around a million transactions a day [S6,S7]. VODÁRENSKÁ AKCIOVÁ SPOLEČNOST, trading since 1993, operates metering as a service and runs Židlochovicko's system [S6,S7]. Popron Systems licenses SMG Water to VaK Pardubice, and Severočeské vodovody a kanalizace sold Most its Smart Metering service [S5]; SUEZ Water CZ holds VaK Břeclav's readout framework [S4]; Techem serves the housing tier [S6].

Solved elsewhere: no foreign comparable is on file at all, so there is no proven model to import here. The evidence is domestic and points the other way — the managed-service position small utilities would buy is already held by Czech suppliers that have sold for two and three decades [S6,S7].

## Revisions


2026-08-25 · rewrite, then re-scoring — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed by that pass. Second pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, and both dimensions held. `scores.proof` stays 0 for the plainest possible reason — `comps` is empty, no foreign player of any maturity is on file, and rung 0 is exactly that. `scores.gap` stays 0, and now says TAKEN rather than the v1 rung's "check not done": six local players were lifted out of the [S6] and [S7] scan prose into a structured `locals[]` ledger and five are established on the named-customer limb, each with the customer named in a receipt already on this page — Softlink (IČO 27109682, ARES 2003) at Pražské vodovody a kanalizace since 2016, VODÁRENSKÁ AKCIOVÁ SPOLEČNOST (IČO 49455842, ARES 1993) at Židlochovicko, Popron Systems (IČO 61855162, ARES 1994) at VaK Pardubice, SUEZ Water CZ at VaK Břeclav and Severočeské vodovody a kanalizace at Most. Only Techem reads early, on receipts alone: it is named as serving the housing tier but no Czech customer, public-buyer pair, round or state listing is on file for it here. One established seller would settle this dimension; there are five. Founding years were verified in ARES on this date. `score` unchanged at 3. The non-solutions paragraph now states each incumbent's trading age and the customer that proves it, because under the new ladder maturity is the fact carrying the score, and the Proven-abroad paragraph says plainly that an empty comps ledger means no model to import. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.
2026-08-13 · de-rank — The gap check found the managed-service position occupied: Softlink sells its CEM Smart metering-data platform to Czech water utilities, VODÁRENSKÁ AKCIOVÁ SPOLEČNOST operates remote metering as a service for small utilities (it runs Židlochovicko's system), Popron Systems licenses SMG Water, and SUEZ and Techem hold framework and housing-tier positions [S6]. The original framing — "no shared platform, nobody operates a neutral managed service" — does not survive it: the buying is fragmented, but the supply side is present and winning these contracts [S4,S5,S6]. Gap stays 0 with incumbents named; status moves to watching. What would re-rank this: evidence the incumbents fail the smallest svazky on price or capability, or a below-threshold tender count showing the long tail remains unserved.

2026-08-20 · evidence audit — Three corrections, merged. (1) The "Why now" sentence removed in full; none of its three claims has support in the 6,181-signal corpus. "Price regulation via ERSO oversight": ERSO returns zero hits corpus-wide, case-sensitively and case-insensitively, and no Czech water-price regulator appears anywhere in the evidence. There is no such body — the Czech energy regulator is ERÚ and it does not regulate water — and no substitute name was inserted, because we hold no receipt for one. "EU funding streams (OPŽP) co-finance the projects": eleven OPŽP calls are on file and none funds metering; they fund public-building energy retrofits, renewables, landscape and water-landscape measures, rain/greywater capture, slope stability, flood prevention, contaminated-site remediation, food banks and air-quality monitoring. The drought and water-loss driver was likewise uncited. Money is untouched — it never rested on OPŽP but on the receipted tenders and contracts already on this ledger [S1,S2,S3,S4,S5]. (2) The "Existing non-solutions" sentence removed in full — proprietary head-end systems, one-off SCADA/dispatch integrations, and the large VaKs' in-house solutions attributed to Veolia-operated utilities. Veolia returns no hits anywhere in the signal corpus, in either case, and appears in no source note here; the head-end and SCADA characterisations have no receipt either. The paragraph now states what this record's own gap check found: the managed-service position is occupied by named local players [S6]. The lead's "hundreds of VaK companies and municipal svazky" is not an invention — it is carried by the signal behind [S2], and is now cited there rather than left bare. (3) The title clause "with no shared platform" is gone: the body already recorded that this exact framing does not survive the check [S6].

2026-08-24 · gap re-check — The S6 receipt URL died in a softlink.cz restructure (404); the incumbent did not. Re-verified live: Softlink still lists water utilities as a served segment and states CEM Smart has read Pražské vodovody a kanalizace meters remotely since 2016, ~1M transactions a day [S7]. The registr-smluv lookup corpus independently pairs VODÁRENSKÁ AKCIOVÁ SPOLEČNOST as supplier with VaK Židlochovicko as buyer, corroborating the operates-as-a-service claim [S7]. Nothing rescored; the de-rank stands on a live receipt again.
