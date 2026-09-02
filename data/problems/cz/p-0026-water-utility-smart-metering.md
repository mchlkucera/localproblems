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
  competes: direct
  maturity: established
  evidence: It sells CEM Smart, a remote meter-reading platform, and names water utilities as
    a segment it serves — with customers including Pražské vodovody a kanalizace, whose meters
    it has read remotely since 2016 at roughly a million transactions a day, verified live 2026-08-24
    [S7]. Trading since 10 December 2003.
- name: VODÁRENSKÁ AKCIOVÁ SPOLEČNOST
  url: https://www.vodarenska.cz/
  ico: '49455842'
  since: 1993
  competes: direct
  maturity: established
  evidence: It runs metering as a service for smaller water companies, with customers including
    Vodovody a kanalizace Židlochovicko, which pairs with it as buyer on the state contracts register
    [S6,S7]. Trading since 1 December 1993.
- name: Popron Systems (SMG Water)
  url: https://www.popron.cz/
  ico: '61855162'
  since: 1994
  competes: direct
  maturity: established
  evidence: It sells the SMG Water metering platform under licence, with customers including VaK
    Pardubice, which amended its Smart Metering licence agreement in June 2026 [S5]. Trading since
    6 September 1994.
- name: SUEZ Water CZ
  url: https://www.suez.cz/
  ico: '11901403'
  since: 2021
  competes: direct
  maturity: established
  evidence: It supplies remote-readout devices and the support behind them, with customers including
    VaK Břeclav, which signed amendment No. 1 to its framework contract for them [S4]. Trading
    since 1 October 2021.
- name: Severočeské vodovody a kanalizace
  url: https://www.scvk.cz/
  ico: '49099451'
  since: 1993
  competes: direct
  maturity: established
  evidence: It operates water systems and sells metering alongside, with customers including město
    Most, which bought a Smart Metering supplementary service from it as incumbent operator in
    August 2026 [S5]. Trading since 1 October 1993.
- name: Techem CZ
  url: https://www.techem.cz/
  ico: '61852121'
  since: 1994
  competes: adjacent
  maturity: early
  evidence: It sells heat and water submetering and billing into the housing tier — apartment
    buildings and the firms that manage them [S6] — not the utility-side managed metering service
    a small water company buys. It has traded since 1994, but nothing on file names a Czech buyer,
    no public body pairs with it on the state contracts register and no funding or state listing
    is on record, so how much it sells here is unknown.
sources:
- type: tender
  name: "TED — Ivančice water association smart metering (~€1.2M)"
  gist: "the open €1.2M tender"
  why: "A municipal water association opened a competition for smart metering across its network in summer 2026."
  url: https://ted.europa.eu/en/notice/-/detail/430180-2026
  note: 'ted-430180-2026: Svazek vodovodů a kanalizací Ivančice — OPEN competition ~€1.2M
    (~29M CZK) for smart-metering installation on the water network (Jun–Jul 2026). Open tender
    ≥5M CZK: money 2.'
  date: '2026-06-24'
  signal: ted-430180-2026
- type: tender
  name: "TED — VaK Kroměříž smart metering (~€1.3M)"
  gist: "three buys in ten weeks"
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
  gist: "supply plus operation, same day"
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
  gist: "the fifth utility's framework"
  why: "A fifth utility with a live smart-metering relationship, running remote-readout devices and support off a supplier framework."
  url: https://smlouvy.gov.cz/smlouva/38219601
  note: 'hlidac-38219601: VaK Břeclav signed amendment No. 1 to a framework contract with
    SUEZ Water CZ for remote-readout devices and support (Jun 2026) — a FIFTH distinct utility
    with a live smart-metering relationship, running on a supplier framework.'
  date: '2026-06-02'
  signal: hlidac-38219601
- type: contract
  name: "Registr smluv — VaK Pardubice / Popron licence"
  gist: "buyers six and seven"
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
  gist: "the incumbents, named"
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
  gist: "Prague meters read since 2016"
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
  gist: "the €5,987 village pilot"
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
  gist: "the Czech supplier sweep"
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
updated: '2026-09-02'
---

Czech water supply runs on hundreds of municipal utilities and water associations — the VaK companies and svazky, most of them small [S2]. Each digitizes metering one infrastructure tender at a time. Three bought inside ten weeks of 2026: Kroměříž about €1.3M for network smart metering, Bruntál a water data dispatch [S2], Ivančice a €1.2M competition [S1] — each buying its own hardware, radio links, platform and integration.

Why now: these associations cannot staff a data platform, and buy one anyway — Benešov's Společná voda paid €5,987 in July 2026 for a 112-sensor pilot, one of about fifteen small municipal meter orders on file [S8]. Each buy embeds years of dependence on whichever integrator won.

Who pays: the utilities themselves, out of public budgets and on the public record. Seven buyers contracted supply, licences and operation separately by August 2026; Židlochovicko alone signed 8.4M CZK across two contracts in one day [S3,S5].

Existing non-solutions: the managed-service position is taken, and not by newcomers. Softlink has sold since 2003; its CEM Smart platform — remote meter reading as a service — has read Pražské vodovody a kanalizace meters since 2016, about a million transactions a day [S6,S7]. VODÁRENSKÁ AKCIOVÁ SPOLEČNOST, trading since 1993, runs Židlochovicko's metering as a service [S6,S7]. Popron Systems licenses SMG Water — its metering platform — to VaK Pardubice; Severočeské vodovody a kanalizace sold the town of Most a Smart Metering service [S5]. SUEZ Water CZ supplies VaK Břeclav's remote-readout devices — a framework amended June 2026 [S4]. Techem sells submetering to apartment buildings, not to utilities [S6].

Solved elsewhere: no foreign comparable is on file, so there is nothing to import. The domestic evidence runs the other way: Czech suppliers selling for two and three decades already hold the position a small utility would buy [S6,S7].

## Revisions


2026-08-25 · rewrite, then re-scoring — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed by that pass. Second pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, and both dimensions held. `scores.proof` stays 0 for the plainest possible reason — `comps` is empty, no foreign player of any maturity is on file, and rung 0 is exactly that. `scores.gap` stays 0, and now says TAKEN rather than the v1 rung's "check not done": six local players were lifted out of the [S6] and [S7] scan prose into a structured `locals[]` ledger and five are established on the named-customer limb, each with the customer named in a receipt already on this page — Softlink (IČO 27109682, ARES 2003) at Pražské vodovody a kanalizace since 2016, VODÁRENSKÁ AKCIOVÁ SPOLEČNOST (IČO 49455842, ARES 1993) at Židlochovicko, Popron Systems (IČO 61855162, ARES 1994) at VaK Pardubice, SUEZ Water CZ at VaK Břeclav and Severočeské vodovody a kanalizace at Most. Only Techem reads early, on receipts alone: it is named as serving the housing tier but no Czech customer, public-buyer pair, round or state listing is on file for it here. One established seller would settle this dimension; there are five. Founding years were verified in ARES on this date. `score` unchanged at 3. The non-solutions paragraph now states each incumbent's trading age and the customer that proves it, because under the new ladder maturity is the fact carrying the score, and the Proven-abroad paragraph says plainly that an empty comps ledger means no model to import. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. Five entries convert to `direct` + `established` with their evidence unchanged — Softlink, VODÁRENSKÁ AKCIOVÁ SPOLEČNOST, Popron Systems, SUEZ Water CZ and Severočeské vodovody a kanalizace all sell the managed metering position to water utilities. Techem CZ moves to `competes: adjacent` at `early`: it sells heat and water submetering and billing into the housing tier — apartment buildings and the firms that manage them — not the utility-side service a small vodárna buys. Its `early` is a statement about receipts rather than about the firm's age: ARES 1994 clears the years limb comfortably, but nothing on file names a Czech customer of it, no public-buyer pair exists, and there is no round or state listing. `scores.gap` stays 0 on five direct established sellers, so nothing here turned on Techem either way. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

2026-08-13 · de-rank — The gap check found the managed-service position occupied: Softlink sells its CEM Smart metering-data platform to Czech water utilities, VODÁRENSKÁ AKCIOVÁ SPOLEČNOST operates remote metering as a service for small utilities (it runs Židlochovicko's system), Popron Systems licenses SMG Water, and SUEZ and Techem hold framework and housing-tier positions [S6]. The original framing — "no shared platform, nobody operates a neutral managed service" — does not survive it: the buying is fragmented, but the supply side is present and winning these contracts [S4,S5,S6]. Gap stays 0 with incumbents named; status moves to watching. What would re-rank this: evidence the incumbents fail the smallest svazky on price or capability, or a below-threshold tender count showing the long tail remains unserved.

2026-08-20 · evidence audit — Three corrections, merged. (1) The "Why now" sentence removed in full; none of its three claims has support in the 6,181-signal corpus. "Price regulation via ERSO oversight": ERSO returns zero hits corpus-wide, case-sensitively and case-insensitively, and no Czech water-price regulator appears anywhere in the evidence. There is no such body — the Czech energy regulator is ERÚ and it does not regulate water — and no substitute name was inserted, because we hold no receipt for one. "EU funding streams (OPŽP) co-finance the projects": eleven OPŽP calls are on file and none funds metering; they fund public-building energy retrofits, renewables, landscape and water-landscape measures, rain/greywater capture, slope stability, flood prevention, contaminated-site remediation, food banks and air-quality monitoring. The drought and water-loss driver was likewise uncited. Money is untouched — it never rested on OPŽP but on the receipted tenders and contracts already on this ledger [S1,S2,S3,S4,S5]. (2) The "Existing non-solutions" sentence removed in full — proprietary head-end systems, one-off SCADA/dispatch integrations, and the large VaKs' in-house solutions attributed to Veolia-operated utilities. Veolia returns no hits anywhere in the signal corpus, in either case, and appears in no source note here; the head-end and SCADA characterisations have no receipt either. The paragraph now states what this record's own gap check found: the managed-service position is occupied by named local players [S6]. The lead's "hundreds of VaK companies and municipal svazky" is not an invention — it is carried by the signal behind [S2], and is now cited there rather than left bare. (3) The title clause "with no shared platform" is gone: the body already recorded that this exact framing does not survive the check [S6].

2026-08-24 · gap re-check — The S6 receipt URL died in a softlink.cz restructure (404); the incumbent did not. Re-verified live: Softlink still lists water utilities as a served segment and states CEM Smart has read Pražské vodovody a kanalizace meters remotely since 2016, ~1M transactions a day [S7]. The registr-smluv lookup corpus independently pairs VODÁRENSKÁ AKCIOVÁ SPOLEČNOST as supplier with VaK Židlochovicko as buyer, corroborating the operates-as-a-service claim [S7]. Nothing rescored; the de-rank stands on a live receipt again.

THE LEDGER NOTES, IN PLAIN LANGUAGE. All 6 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

2026-09-02 · plain-language pass — Glossed three trade terms at first use — CEM Smart, SMG Water and SUEZ Water CZ — and put plain words beside VaK and svazky; telemetry replaced outright. Argument went 291 to 299 words as the glosses landed; every figure, date and named company kept, and the window sentence now cites the Benešov pilot [S8], previously uncited. A gist added to all nine sources. No score, status, note or marker touched.
