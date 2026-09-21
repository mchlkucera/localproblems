# run manifest — 2026-09-21

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-09-21`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-21T0805 | ted | ok | 200 | 70403500 | 8524 | 36845 | 2026-09-21T08:05:09Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | hlidac | ok | 200 | 2029553 | 847 | 16976 | 2026-09-21T08:05:52Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | veklep | ok | 200 | 1717848 | 138 | 4759 | 2026-09-21T08:07:56Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | tacr | ok | 200 | 264246 | 14 | 2102 | 2026-09-21T08:08:17Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | hackathon | ok | 200 | 5887361 | 14 | 37986 | 2026-09-21T08:08:20Z | data/raw/2026-09-21 | partial: hackjakbrno:mode-a upol:yield-zero |
| 2026-09-21T0805 | nen-ptk | ok | 200 | 46838184 | 138 | 323247 | 2026-09-21T08:08:59Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | edesky | skipped | 000 | 0 | 0 | 0 | 2026-09-21T09:02:58Z |  | registry status=planned |
| 2026-09-21T0805 | cc-cz | ok | 200 | 17996 |  | 715 | 2026-09-21T09:02:59Z | data/raw/2026-09-21/feed-czechcrunch.xml |  |
| 2026-09-21T0805 | yc-oss | ok | 200 | 10493832 |  | 2640 | 2026-09-21T09:02:59Z | data/raw/2026-09-21/yc-all.json |  |
| 2026-09-21T0805 | vestbee | ok | 200 | 1065432 | 43 | 2265 | 2026-09-21T09:03:02Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | suggest | ok | 200 | 11395 | 41 | 42714 | 2026-09-21T09:04:11Z | data/raw/2026-09-21/suggest-pain.jsonl | partial: 1 of 144 queries failed |
| 2026-09-21T0805 | reddit-new | ok | 200 | 191946 | 100 | 1637 | 2026-09-21T09:08:37Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | reddit-search | ok | 200 | 329586 | 100 | 1709 | 2026-09-21T09:08:37Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | nku | ok | 200 | 77219 | 127 | 1248 | 2026-09-21T09:09:05Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | sukl | ok | 200 | 1624040 | 15 | 1566 | 2026-09-21T09:09:07Z | data/raw/2026-09-21 | validity=2026-09-21 rows_in_file=83295 aggregates=15 |
| 2026-09-21T0805 | ec-hys | ok | 200 | 133579 | 34 | 5350 | 2026-09-21T09:09:09Z | data/raw/2026-09-21 |  |
| 2026-09-21T0805 | nen | skipped | 000 | 0 | 0 | 0 | 2026-09-21T09:09:42Z |  | registry status=planned |
| 2026-09-21T0805 | mpsv | skipped | 000 | 0 | 0 | 0 | 2026-09-21T09:09:42Z | data/raw/2026-09-21 | month 2026-08 already present in seen.txt |
| 2026-09-21T0805 | coi | skipped | 200 | 39676640 | 0 | 10629 | 2026-09-21T09:09:42Z | data/raw/2026-09-21 | no completed half-year to emit: None |
| 2026-09-21T0805 | smlouvy | skipped | 000 | 0 | 0 | 0 | 2026-09-21T09:09:54Z |  | registry status=planned |

---

# Ingest run 2026-09-21T1109
Run date: 2026-09-21  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 17996 | 10 | 10 | — | structured | yes |  |
| `coi` | 200 | 39676640 | 0 | 0 | — | none | yes | no completed half-year to emit: None |
| `ec-hys` | 200 | 133579 | 34 | 8 | — | structured | yes |  |
| `hackathon` | 200 | 5887361 | 14 | 11 | below-range | structured | yes | partial: hackjakbrno:mode-a upol:yield-zero |
| `hlidac` | 200 | 2029553 | 847 | 6 | — | structured | yes |  |
| `mpsv` | — | 0 | 0 | 0 | — | none | yes | month 2026-08 already present in seen.txt |
| `nen-ptk` | 200 | 46838184 | 138 | 63 | above-range | structured | yes |  |
| `nku` | 200 | 77219 | 127 | 125 | — | structured | yes |  |
| `reddit-new` | 200 | 191946 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 329586 | 100 | 75 | — | structured | yes |  |
| `suggest` | 200 | 11395 | 41 | 26 | — | structured | yes | partial: 1 of 144 queries failed |
| `sukl` | 200 | 1624040 | 15 | 0 | — | structured | yes | validity=2026-09-21 rows_in_file=83295 aggregates=15 |
| `tacr` | 200 | 264246 | 14 | 6 | — | structured | yes |  |
| `ted` | 200 | 70403500 | 8524 | 2871 | — | structured | yes |  |
| `veklep` | 200 | 1717848 | 138 | 11 | — | structured | yes |  |
| `vestbee` | 200 | 1065432 | 43 | 9 | — | structured | yes |  |
| `yc-oss` | 200 | 10493832 | 6241 | 950 | — | structured | yes |  |

## Staged records — PENDING, not appended

4224 records carry their mechanical fields and are waiting on a model. 12115 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 4224 |
| `scores.recurrence` | 4224 |
| `sector` | 4224 |
| `geo_origin` | 4224 |
| `title` | 3276 |
| `summary` | 3276 |
| `pain` | 201 |
| `scores.urgency` | 183 |
| `stated_need` | 79 |

**Transport status UNKNOWN for 1 feed(s):** `mpsv`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 4224 staged record(s) passed the field allowlist and the email/phone content scan.

## Republication candidates — same quote and value, new notice id

**105 staged tender record(s) repeat the verbatim quote and the value of a record already on file.** TED re-notifies the same procurement under a new number and neither dedup axis can see it. They are KEPT — a re-issued tender can be evidence (p-0031) — each carries the earlier id in `notes`, and MATCH decides dup or distinct.

| staged id | repeats | seen in |
|---|---|---|
| `ted-509261-2026` | `ted-585863-2026` | ledger |
| `ted-512419-2026` | `ted-588567-2026` | ledger |
| `ted-512670-2026` | `ted-563450-2026`, `ted-616997-2026` | ledger |
| `ted-514163-2026` | `ted-567618-2026`, `ted-594090-2026` | ledger |
| `ted-514916-2026` | `ted-514493-2026` | batch |
| `ted-515178-2026` | `ted-587084-2026` | ledger |
| `ted-520572-2026` | `ted-557909-2026` | ledger |
| `ted-521185-2026` | `ted-564088-2026` | ledger |
| `ted-522603-2026` | `ted-508734-2026` | batch |
| `ted-524293-2026` | `ted-571033-2026`, `ted-578486-2026` | ledger |
| `ted-527994-2026` | `ted-515784-2026` | batch |
| `ted-536808-2026` | `ted-547009-2026` | ledger |
| `ted-536828-2026` | `ted-560207-2026` | ledger |
| `ted-541036-2026` | `ted-557909-2026` | ledger |
| `ted-543982-2026` | `ted-515784-2026` | batch |
| `ted-545152-2026` | `ted-521757-2026` | batch |
| `ted-545908-2026` | `ted-532795-2026` | batch |
| `ted-552739-2026` | `ted-528999-2026` | batch |
| `ted-555462-2026` | `ted-554061-2026` | batch |
| `ted-556897-2026` | `ted-521757-2026` | batch |
| `ted-556949-2026` | `ted-554061-2026` | batch |
| `ted-557720-2026` | `ted-599397-2026` | ledger |
| `ted-565027-2026` | `ted-553142-2026` | batch |
| `ted-565384-2026` | `ted-566023-2026` | ledger |
| `ted-566552-2026` | `ted-533014-2026` | batch |
| `ted-567143-2026` | `ted-559126-2026` | ledger |
| `ted-571334-2026` | `ted-570329-2026` | batch |
| `ted-573735-2026` | `ted-596228-2026` | ledger |
| `ted-580531-2026` | `ted-585863-2026` | ledger |
| `ted-584625-2026` | `ted-553308-2026` | batch |
| `ted-602172-2026` | `ted-600285-2026` | batch |
| `ted-602795-2026` | `ted-599397-2026` | ledger |
| `ted-603768-2026` | `ted-521757-2026` | batch |
| `ted-605581-2026` | `ted-596494-2026` | batch |
| `ted-606337-2026` | `ted-533174-2026` | batch |
| `ted-607161-2026` | `ted-522335-2026` | batch |
| `ted-609008-2026` | `ted-588567-2026` | ledger |
| `ted-610027-2026` | `ted-514493-2026` | batch |
| `ted-611301-2026` | `ted-514493-2026` | batch |
| `ted-611847-2026` | `ted-608668-2026` | batch |
| `ted-612086-2026` | `ted-610856-2026` | batch |
| `ted-612438-2026` | `ted-540209-2026` | ledger |
| `ted-614696-2026` | `ted-535070-2026` | ledger |
| `ted-614985-2026` | `ted-521757-2026` | batch |
| `ted-615079-2026` | `ted-612286-2026` | batch |
| `ted-615443-2026` | `ted-471282-2026` | ledger |
| `ted-615618-2026` | `ted-544133-2026` | ledger |
| `ted-620340-2026` | `ted-533142-2026`, `ted-593389-2026` | ledger |
| `ted-621151-2026` | `ted-582057-2026` | batch |
| `ted-621196-2026` | `ted-550596-2026` | ledger |
| `ted-621214-2026` | `ted-622067-2026` | ledger |
| `ted-621287-2026` | `ted-619553-2026` | batch |
| `ted-621552-2026` | `ted-621368-2026` | batch |
| `ted-621987-2026` | `ted-528464-2026` | ledger |
| `ted-622336-2026` | `ted-564208-2026`, `ted-575552-2026`, `ted-579550-2026`, `ted-604354-2026`, `ted-610001-2026` | ledger |
| `ted-622890-2026` | `ted-566505-2026` | ledger |
| `ted-623347-2026` | `ted-622944-2026` | batch |
| `ted-624360-2026` | `ted-566505-2026` | ledger |
| `ted-625324-2026` | `ted-566370-2026`, `ted-566898-2026` | ledger |
| `ted-625487-2026` | `ted-528024-2026` | ledger |
| `ted-625493-2026` | `ted-547014-2026` | ledger |
| `ted-629086-2026` | `ted-566370-2026`, `ted-566898-2026` | ledger |
| `ted-631802-2026` | `ted-534000-2026` | batch |
| `ted-633463-2026` | `ted-609630-2026` | ledger |
| `ted-640693-2026` | `ted-471282-2026` | ledger |
| `ted-642898-2026` | `ted-637714-2026` | batch |
| `ted-645157-2026` | `ted-607500-2026` | batch |
| `ted-646429-2026` | `ted-575145-2026`, `ted-617323-2026` | ledger |
| `ted-646476-2026` | `ted-522361-2026`, `ted-583303-2026` | ledger |
| `ted-646538-2026` | `ted-540382-2026` | ledger |
| `ted-646553-2026` | `ted-591418-2026`, `ted-640810-2026`, `ted-643165-2026` | ledger |
| `ted-646586-2026` | `ted-627304-2026` | ledger |
| `ted-646592-2026` | `ted-642768-2026` | ledger |
| `ted-646698-2026` | `ted-307565-2026` | ledger |
| `ted-646805-2026` | `ted-488033-2026`, `ted-516010-2026`, `ted-547691-2026`, `ted-565387-2026`, `ted-576952-2026`, `ted-579054-2026`, `ted-583339-2026`, `ted-609049-2026` | ledger |
| `ted-646826-2026` | `ted-588738-2026`, `ted-615753-2026`, `ted-620746-2026` | ledger |
| `ted-647236-2026` | `ted-499943-2026`, `ted-521650-2026`, `ted-526018-2026` | ledger |
| `ted-647324-2026` | `ted-538104-2026` | ledger |
| `ted-647347-2026` | `ted-621276-2026` | ledger |
| `ted-647388-2026` | `ted-575233-2026`, `ted-631151-2026` | ledger |
| `ted-647530-2026` | `ted-481203-2026`, `ted-547430-2026`, `ted-579199-2026` | ledger |
| `ted-647548-2026` | `ted-586634-2026`, `ted-637656-2026` | ledger |
| `ted-647743-2026` | `ted-646780-2026` | batch |
| `ted-647969-2026` | `ted-568576-2026`, `ted-609876-2026`, `ted-628425-2026` | ledger |
| `ted-648007-2026` | `ted-599498-2026` | ledger |
| `ted-648033-2026` | `ted-570520-2026` | ledger |
| `ted-648241-2026` | `ted-572969-2026`, `ted-631809-2026` | ledger |
| `ted-648504-2026` | `ted-498370-2026`, `ted-551264-2026`, `ted-578691-2026`, `ted-584275-2026`, `ted-613065-2026`, `ted-620669-2026` | ledger |
| `ted-648568-2026` | `ted-571543-2026` | ledger |
| `ted-648695-2026` | `ted-563996-2026` | ledger |
| `ted-648742-2026` | `ted-598409-2026` | ledger |
| `ted-648765-2026` | `ted-605206-2026` | ledger |
| `ted-648933-2026` | `ted-581645-2026` | ledger |
| `ted-649004-2026` | `ted-574507-2026`, `ted-630176-2026` | ledger |
| `ted-649043-2026` | `ted-603562-2026` | ledger |
| `ted-649047-2026` | `ted-592165-2026`, `ted-627382-2026` | ledger |
| `ted-649223-2026` | `ted-647337-2026` | batch |
| `ted-649464-2026` | `ted-542663-2026`, `ted-564075-2026`, `ted-639838-2026` | ledger |
| `ted-649616-2026` | `ted-612687-2026` | ledger |
| `ted-649652-2026` | `ted-563468-2026` | ledger |
| `ted-649829-2026` | `ted-613469-2026` | ledger |
| `ted-649987-2026` | `ted-626770-2026` | ledger |
| `ted-650074-2026` | `ted-572276-2026`, `ted-606181-2026` | ledger |
| `ted-650137-2026` | `ted-591785-2026`, `ted-626387-2026` | ledger |
| `ted-650186-2026` | `ted-525777-2026`, `ted-581836-2026`, `ted-617589-2026`, `ted-623773-2026`, `ted-626798-2026` | ledger |

## Dedup by identity key — same resource, different id

**47 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

| staged id | already in the ledger as | key | feed | url |
|---|---|---|---|---|
| `echys-14628` | `consult-cloud-ai-act` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14628 |
| `echys-14638` | `consult-europol-mandate` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14638 |
| `echys-15252` | `consult-territorial-supply-constraints` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15252 |
| `echys-16413` | `consult-horizon-partnerships` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16413 |
| `echys-17172` | `consult-dual-use-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17172 |
| `echys-17912` | `consult-mica-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17912 |
| `echys-18194` | `consult-victims-rights-strategy` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18194 |
| `echys-18658` | `consult-housing-simplification` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18658 |
| `hack-ebca5de0` | `hack-c5c10e91` | `url` | `hackathon` | https://www.aimtechackathon.cz/hackathon/ |
| `hlidac-36459536` | `hlidac-38795752` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38795752 |
| `nku-k24032` | `nku-urad-prace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24032.pdf |
| `nku-k24008` | `nku-rsc-sport` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24008.pdf |
| `nku-k25001` | `nku-dph-ecommerce` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25001.pdf |
| `nku-k24018` | `nku-odpocivky` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24018.pdf |
| `nku-k24025` | `nku-erecept-sms` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24025.pdf |
| `nku-k24016` | `nku-lesnictvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24016.pdf |
| `nku-k24009` | `nku-fakultni-nemocnice` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24009.pdf |
| `nku-k24014` | `nku-nelegalni-prace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24014.pdf |
| `nku-k24017` | `nku-gacr-tacr` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24017.pdf |
| `nku-k24007` | `nku-dtm` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24007.pdf |
| `nku-k24006` | `nku-modernizacni-fond` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24006.pdf |
| `nku-k24012` | `nku-vycvik-acr` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24012.pdf |
| `nku-k24004` | `nku-esbirka` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24004.pdf |
| `nku-k24001` | `nku-pesi-komunikace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24001.pdf |
| `nku-k23031` | `nku-pozemkove-upravy` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K23031.pdf |
| `nku-k25014` | `nku-ikem-hospodareni` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25014.pdf |
| `nku-k25013` | `nku-zdravotnicky-vyzkum` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25013.pdf |
| `nku-k25021` | `nku-up-ucetni-zaverka-2025` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25021.pdf |
| `nku-k25017` | `nku-dia-ucetnictvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25017.pdf |
| `nku-k24024` | `nku-uspory-energie` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24024.pdf |
| `nku-k25012` | `nku-letecka-sluzba` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25012.pdf |
| `nku-k25011` | `nku-cista-mobilita` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25011.pdf |
| `nku-k25005` | `nku-etcs` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25005.pdf |
| `nku-k25008` | `nku-srazkove-vody` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25008.pdf |
| `nku-k25007` | `nku-react-eu-nemocnice` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25007.pdf |
| `nku-k25009` | `nku-vrt` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25009.pdf |
| `nku-k25003` | `nku-majetkove-ucasti` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25003.pdf |
| `nku-k25004` | `nku-mistni-komunikace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25004.pdf |
| `nku-k25006` | `nku-protipovodnova-ochrana` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25006.pdf |
| `nku-k24028` | `nku-statni-sluzba` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24028.pdf |
| `nku-k24029` | `nku-msmt-horizont-kontroly` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24029.pdf |
| `nku-k25002` | `nku-rizeni-skolstvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25002.pdf |
| `nku-k24031` | `nku-justicni-pohledavky` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24031.pdf |
| `nku-k24030` | `nku-doprava2020` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24030.pdf |
| `nku-k24026` | `nku-viza-it` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24026.pdf |
| `yc-d-model` | `yc-d_model` | `url` | `yc-oss` | https://www.ycombinator.com/companies/d_model |
| `yc-galactic-resource-utilization-space-inc-gru-spac` | `yc-galactic-resource-utilization-space-inc-gru-space` | `url` | `yc-oss` | https://www.ycombinator.com/companies/galactic-resource-utilization-space-inc-gru-space |

**2 key(s) were EXEMPTED from dedup**, because a key naming more than one record is a listing page, a dataset landing page or a roundup — not an identity. Merging on one would delete distinct records. Measured over the committed corpus: 67 urls are shared by 571 records (6.1%), one Vestbee roundup being the url of 32 funding rounds.

| key | why it was not used |
|---|---|
| `url:idea13.cz/` | carried by 4 records in THIS batch — undecidable, so no merge |
| `url:nakopniprahu.cz/` | carried by 6 records in THIS batch — undecidable, so no merge |

---

# Attended scan passes — 2026-09-21

Four attended feeds ran in parallel as subagents, each staging only into its own
`data/raw/2026-09-21/<feed>/` directory. The coordinator ran `normalize.py --complete`
once per feed, sequentially, and appended to `seen.txt` once at the end.

| feed | records appended | ledger |
|---|---|---|
| demand-scan | 2 | `data/signals/demand/2026-09-21.jsonl` |
| reg-scan | 4 | `data/signals/regulation/2026-09-21.jsonl` |
| dotace-scan | 0 | — (no new call; MS2021+ diff was +0/−0) |
| arb-scan | 5 | `data/signals/funded/2026-09-21.jsonl` |

**Coordinator fix before append:** the `funded` and `demand` staged records carried no
`evidence_type`, and `normalize.py --complete` routes an untyped record to the `demand`
ledger by default. The five arb-scan records would have landed in `demand/`. The field was
set explicitly on both files before the real append; `regulation` already carried it.


## demand-scan pass — 2026-09-21 (weekly delta pass)

This is the weekly delta pass of feed `demand-scan` (evidence_type `demand`), run two days
after the pass of 2026-09-19 (`data/raw/2026-09-19/manifest.md`, demand section), which
itself followed the monthly BROAD pass of 2026-09-18. It follows pipeline/SCANS.md: every
checklist source was walked. The window it looked for was **items published or newly
surfaced since 2026-09-19**, plus everything the 2026-09-19 pass named as owed.

Other agents and a scripted ingest write the same raw date, so this pass kept to its own
paths: payloads under `data/raw/2026-09-21/demand/pages/`, `staged.jsonl` under
`data/raw/2026-09-21/demand/`, plus this file. It made no ledger write, no seen.txt write,
no DB write, no feeds.json edit and no git state change.

### Hand-off

- `data/raw/2026-09-21/demand/staged.jsonl` holds **2 records**. Two days produced two
  genuinely new documents, one per source (NKÚ and the ombudsman); the other two checklist
  sources are expected absences.
- A dry run against a SCRATCH COPY of `data/signals` (`$TMPDIR/demand-sim-0921/signals`,
  same corpus, seen.txt 18,420 ids) printed:
  `normalize --complete --dry-run: would append 2 records across 1 file(s); 0 dropped by
  materiality; 0 incomplete; 0 refused by AC-GDPR1.` →
  `signals/demand/2026-09-21.jsonl: +2`; `dedup by identity key (append): 0 skipped`.
  `git status --porcelain data/signals` was empty afterwards.
- The coordinator therefore owes this feed one `--complete` over
  `data/raw/2026-09-21/demand` and one `db.py upsert data/signals/demand/2026-09-21.jsonl`.

### Checklist source 1 — NKÚ kontrolní závěry (parse the PDFs)

**Visited. ONE NEW CONCLUSION, parsed and minted.**

- RSS `https://nku.cz/cz/rss.xml`: **200**, 13,475 B (`pages/nku-rss.xml`), 30 items. It
  grew by one item since the 2026-09-19 capture (13,142 B): **id15918, 21 Sep 2026**,
  *"Více než 3 miliardy na zemědělský výzkum: ministerstvo nezná přínosy podpořených
  projektů"*. Everything below it is unchanged: job adverts of 15 Sep, the IKEM press
  release of 14 Sep (id15897, already held as `nku-ikem-hospodareni`), the 13th Kolegium
  of 7 Sep (id15884).
- Press release `.../tiskove-zpravy/…-id15918/`: **200**, 26,683 B (`pages/nku-15918.html`).
  Note the access change: the press-release LISTING page still refuses curl, but this
  ITEM page answered 200 with a browser user-agent. It names **kontrolní akce 25/18** and
  links `assets/kon-zavery/k25018.pdf`.
- **Conclusion PDF k25018.pdf: 200**, 657,286 B, `Last-Modified: Mon, 21 Sep 2026 04:26:37
  GMT`. On 2026-09-19 this same URL was **404**. Saved as `pages/nku-k25018.pdf` with
  `pdftotext -layout` output `pages/nku-k25018.txt` (105,868 B) and plain
  `pages/nku-k25018-raw.txt`. The ZÁVĚR itself was parsed, not the headline:
  Kolegium X. jednání, 22 June 2026, usnesení 11/X/2026; 3.29bn CZK drawn of 3.56bn
  budgeted; 266 projects; sample of 14 projects at 8 recipients worth 187.70m CZK;
  175.96m CZK judged at a reduced degree of purposefulness/economy; contract breaches in
  8 of 14, suspected budget-discipline breaches in 4; 1,113 duplicate results (12.91 %)
  in IS VaVaI; ZEMĚ II running since 2023 with ZEMĚ never evaluated.
  **Minted as `nku-zemedelsky-vyzkum`.**
- Conclusion-PDF existence re-probe `https://www.nku.cz/assets/kon-zavery/kNNNNN.pdf`:
  - 200: **k25018 (new)**; k25015, k25016, k25020, k25021 unchanged from 2026-09-19 and
    not re-read — their decisions stand (25/21 held as `nku-up-ucetni-zaverka-2025`;
    25/15, 25/16, 25/20 dropped by the pain-language bar on 2026-09-03).
  - 404: k25019, k25022, k25023, **k25024**, k25025, k25026, k25027, k26001, k26002.
- Věstník index `https://www.nku.cz/cz/publikace-a-dokumenty/vestnik/`: **200**, 41,328 B
  (`pages/nku-vestnik.html`), byte-identical in size to the 2026-09-19 capture. The newest
  issue is still **částka 3/2026** (13 Aug 2026), whose contents list (24/24, 25/03, 25/05,
  25/07, 25/08, 25/09, 25/11, 25/12, 25/15) does **not** include 25/18. There is no 4/2026.
- **Owed, still open:** k25024.pdf (revitalisation of public spaces, approved by the 13th
  Kolegium on 7 Sep 2026) is still 404 — carried for a third pass. Věstník 4/2026 when it
  appears; it should carry 25/18 among others.
- **For the coordinator, scripted `nku` feed.** The scripted feed still has not run since
  2026-09-08 (no `nku-*` payload in `data/raw/2026-09-21/`, and `nku-15872` is still
  absent from seen.txt and still pending in `data/raw/2026-09-08/staged.jsonl`). There are
  now **two** headline twins waiting: id15897 (IKEM → `nku-ikem-hospodareni`) and
  **id15918 (agricultural research → `nku-zemedelsky-vyzkum`)**. Both carry a different
  url from the conclusion PDF, so identity-key dedup will not catch either.

### Checklist source 2 — European Semester CZ package

**Visited. Nothing new this pass.**

- Landing page
  `https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages-including-country-reports/country-report-czechia_en`:
  **200**, 74,780 B (`pages/ecsem-landing.html`) — the same byte count as the 2026-09-18
  and 2026-09-19 captures, and its stripped text is unchanged. The newest item is still the
  **2026 Country Report of 3 June 2026**, already held as `ecsem-cz2026-housing`,
  `-admin-burden` and `-ltc-mix`. The listing below it (2025, 2024, 2023) is unchanged.
- One Semester cycle runs per year; the Council CSR half of the current cycle was adopted
  10 July 2026 and its OJ C reference (**CELEX 32026H03916, C/2026/3916, OJ C of
  2026-09-01**) was found and closed by the 2026-09-19 pass via the CELLAR SPARQL
  endpoint. That finding is a **note owed on `ecsem-cz2026-csr`**, which only the
  coordinator can write; this pass did not re-query CELLAR because nothing can have been
  published into the CZ Semester package in two days that the landing page does not show.
  **Nothing minted.**

### Checklist source 3 — MPSV Statistická ročenka, chapter 5 "Sociální služby"

**Visited. EXPECTED ABSENCE (not yet published) — not a coverage gap.**

- `https://mpsv.gov.cz/statisticka-rocenka-z-oblasti-prace-a-socialnich-veci-archiv`:
  **200**, 1,325,956 B (`pages/mpsv-rocenka-archiv.html`), the same byte count as the
  2026-09-19 capture. The string `v roce 2025` appears **0** times; `v roce 2024` appears
  **4** times, which is the positive control that the page parses and that the 2024
  edition is still the newest. No 2025 edition, so no chapter 5 XLSX to diff.
- **Owed:** the next pass re-checks it. When the 2025 edition lands, compare tab 5.9
  against 70,209 DS / 37,849 DZR / 4,043 (`civic-mpsv-rocenka-neuspokojene-2024`).
  Remember the mpsv- trap: file it under `civic-`.

### Checklist source 4 — Ombudsman ESO (HTML walk, no RSS)

**Visited. ONE NEW DOCUMENT, minted. The positive control passed.**

- `https://www.ochrance.cz/eso/zpravy/`: **200**, 14,386 B (`pages/ombud-eso-zpravy.html`).
  Still the taxonomy explainer, same byte count as 2026-09-19.
- Search app `https://eso.ochrance.cz/`: **200**, 83,474 B (`pages/eso-home.html`). Walked
  with the session-bound method the 2026-09-18 pass documented (cookie jar →
  `POST /Vyhledavani/Search` → `POST /Nalezene/GetPocetVysledku` with an explicit empty
  body → `POST /Nalezene/GetTableContent`). Confirmed again: `GetPocetVysledku` needs
  `--data ""`, and `GetTableContent` serves whatever search the SESSION last ran, so each
  window must be re-searched immediately before its table is read.
  - **Positive control** `FormaZjisteni=22` (§ 21c summary visit reports): **41 hits**,
    identical to 2026-09-18 and 2026-09-19.
  - **`DatumVydaniOd=01.06.2026`: 44 hits**, against **43** on 2026-09-19. All four result
    pages were paged and the item ids compared: the set is the same 43 plus exactly one
    addition, **ESO item 15082**.
  - **`DatumVydaniOd=18.09.2026`: 2 hits** — 6160/2025/VOP (Odložení, 21.10.2026) and
    4474/2025/VOP (Zpráva o šetření § 17, 25.09.2026). These are the two future-dated
    single-case items already in the 2026-09-18 set; neither is new and neither is minted
    (scale 0).
  - **Item-id frontier:** `/Nalezene/Edit/15082` → **200** (170,655 B). 15083, 15084,
    15086, 15088, 15090, 15092, 15096, 15100 and 15110 all → **500**. The previous
    frontier, 15064, is unchanged below it.
- **The new document: ESO 15082, sp. zn. 1/2026/SZD, č. j. KVOP-49494/2026,
  "Výzkumná zpráva 2026", forma zjištění Výzkumná zpráva (činnost úřadů), datum vydání
  14.09.2026** (podání 14.01.2026). This is a research report of the kind the 2026-09-18
  pass swept (type 29) and the 2026-09-19 pass found none of; it was issued on 14 Sep but
  only entered ESO after the 2026-09-19 walk. A questionnaire survey on how authorities
  apply the správní řád: 1,422 returns from 1,126 authorities, collected March–May 2026,
  return rate 55–100 % (±4.0 points at 95 % confidence), across all seven office types.
  **Minted as `ombud-spravni-rad-praxe`.** Payload `pages/eso-edit-15082.html`; the full
  report PDF is linked from it at
  `https://www.ochrance.cz/uploads-import/ESO/1-26-SZD-Výzkum_postup_úřadů_sř.pdf`.
- Quarterly reports: Q3 2026 is not due until after 30 Sep 2026. Expected absence;
  `ombud-q2-2026` is still the newest.
- Aktuálně `https://www.ochrance.cz/aktualne/`: **200**, 47,389 B
  (`pages/ombud-aktualne-1.html`), same byte count as 2026-09-19. The newest item is still
  **15 September 2026**, a job advert. Nothing dated 16–21 September. Nothing minted.
- Payloads: `pages/eso-home.html`, `pages/eso-search-{ctrl22,since0918,since0601}.html`,
  `pages/eso-pocet-{ctrl22,since0918,since0601}.txt`,
  `pages/eso-table-since0918.html`, `pages/eso-table-since0601-p{2,3,4,5}.html`,
  `pages/eso-table-since0918-real.html`, `pages/eso-edit-15082.html`,
  `pages/ombud-eso-zpravy.html`, `pages/ombud-aktualne-1.html`.

### Records

| id | source doc | sector | scores (sc/mo/ur/re) | money |
|---|---|---|---|---|
| `nku-zemedelsky-vyzkum` | NKÚ conclusion 25/18, k25018.pdf, published 2026-09-21 | education | 2/3/0/3 | €134,285,714 (3.29bn CZK @ 24.5) |
| `ombud-spravni-rad-praxe` | Ombudsman research report 1/2026/SZD, ESO 15082, issued 2026-09-14 | govtech | 2/0/0/3 | null |

Scoring notes, so the coordinator can check the calibration rather than trust it:

- `nku-zemedelsky-vyzkum` is scored against **`nku-gacr-tacr`** (the 24/17 audit of GAČR
  and TAČR competitive research funding), which is `education` / scale 2 / money 3 /
  urgency 0 / recurrence 3. Sector follows that precedent — the object is competitive
  research funding and its outcome tracking, not agriculture. Scale 2 because the need
  (evidence that publicly funded applied research is used) is shared across the Czech
  research-funding system, not by MZe alone.
- `ombud-spravni-rad-praxe` is scored against the two sibling ombudsman questionnaire
  surveys already held, **`ombud-male-obce-statni-sprava`** (ESO 14378, govtech / 2/0/0/3)
  and **`ombud-cizojazycna-podani`** (ESO 13882, govtech / 2/0/0/2). Recurrence 3 because
  the správní řád is mandated and applies indefinitely.

Both quotes were verified MECHANICALLY before the records were written: each is a literal
substring of its own fetched payload after whitespace collapse (`normalize.py`'s
`collapse()` rule, `\s+` → single space), ≤300 chars, Czech preserved —
`nku-zemedelsky-vyzkum` 263 chars against `pages/nku-k25018.txt`,
`ombud-spravni-rad-praxe` 200 chars against `pages/eso-edit-15082.html`.

### Dedup

- seen.txt holds 18,420 ids. Both new ids were checked against it verbatim:
  `nku-zemedelsky-vyzkum` → 0 matches, `ombud-spravni-rad-praxe` → 0 matches.
- Neither url appears anywhere under `data/signals/`; the identity-key pass in the scratch
  dry run also skipped 0.
- Adjacent ids checked so the coordinator can see the near-misses were considered:
  `nku-zdravotnicky-vyzkum` (25/13, health research) and `nku-gacr-tacr` (24/17, GAČR and
  TAČR) are different audits of different programmes; `ombud-male-obce-statni-sprava`
  (2025, state administration in small municipalities) and `ombud-cizojazycna-podani`
  (2025, foreign-language submissions) are different surveys with different samples.

### Candidates for MATCH

- **NEW candidate, a cluster of pain with a named buyer: `ombud-spravni-rad-praxe`.** The
  authorities themselves name the want — an external methodology, from the Interior
  Ministry or a superior body — and the ombudsman says the survey will be used to initiate
  the missing methodologies. Demand is majority-level in six of eight areas (70 % for
  querulous submissions, 69 % abusive communication, 68 % repeated submissions, 68 %
  remote file inspection, 63 % unsigned submissions, 62 % § 42 notifications), and the
  constraint named underneath it by type-I municipalities is staffing and capacity, not
  will. It sits directly beside the two carried candidates below and may be the same
  problem seen from the other end.
- `nku-zemedelsky-vyzkum` is **evidence for an existing shape**, not a new candidate: the
  outcome-blindness of Czech competitive research funding is already evidenced by
  `nku-gacr-tacr` and `nku-zdravotnicky-vyzkum`. Three audits of three different funders
  finding the same defect is what MATCH should weigh.
- Carried from 2026-09-18/19, still open for MATCH:
  - The delegated-agenda burden in small municipalities (`ombud-male-obce-statni-sprava`
    with `reg-verejne-opatrovnictvi-prenos-2027`).
  - Healthcare complaint investigation capacity (`ombud-stiznosti-zdravotnictvi`).

### Coverage gaps

- **Carried, still open — NKÚ 25/24 (revitalisation of public spaces).** Approved by the
  13th Kolegium on 7 Sep 2026; `k25024.pdf` is still 404 as of this pass (third
  consecutive miss). A future pass owes it a re-probe, and owes Věstník 4/2026 when it
  appears.
- **Expected absences, not gaps:**
  - MPSV Statistická ročenka 2025: not yet published (2024 is still newest; positive
    control passed).
  - Ombudsman Q3 2026 quarterly report: not due until after 30 Sep 2026.
  - European Semester: one cycle per year, both halves of the 2026 cycle already held.
- **Not visited, and why it is not owed:** the CELLAR SPARQL endpoint was not re-queried
  this pass. It was queried on 2026-09-19, the CZ Semester landing page is unchanged, and
  no EU document can enter that package in two days without the landing page moving. A
  future MONTHLY broad pass should re-query it regardless.
- **Outside this feed's remit, flagged for the coordinator:** the scripted `nku` feed has
  not run since 2026-09-08. `nku-15872` is still pending and unheld, and the two press
  releases that twin this pass's and the 2026-09-18 pass's conclusion records (id15918,
  id15897) are unfetched.

### Pass summary

```
feed:                     demand-scan (weekly delta pass, evidence_type demand, 2 days after the 2026-09-19 pass)
checklist sources:        4 of 4 visited (NKU / European Semester / MPSV rocenka / ombudsman ESO); ESO positive control passed (41), MPSV positive control passed (2024 edition found)
records staged:           2  (nku-zemedelsky-vyzkum, ombud-spravni-rad-praxe; scratch dry run: +2, 0 dropped, 0 incomplete, 0 refusals, 0 identity-key skips)
coverage gaps named:      1 carried (NKU 25/24, k25024.pdf 404 for a third pass) · 3 expected absences (MPSV 2025, ombudsman Q3 2026, Semester cycle) · 1 deliberate non-visit (CELLAR SPARQL, queried 2026-09-19)
rotation state:           n/a — category rotation is arb-scan's duty
```


## reg-scan pass — 2026-09-21 (weekly delta)

Weekly DELTA pass of `reg-scan` (feed row: `evidence_type` regulation, `source` `reg-scan`,
`id_prefixes` ["reg"], runner attended), two days after the 2026-09-19 weekly delta
(`data/raw/2026-09-19/manifest.md`, section "reg-scan pass — 2026-09-19"). Operating file:
`pipeline/SCANS.md`, reg-scan checklist items 1–4, under THE CHECKLIST LAW. Cut-off for
"new": anything published, changed or re-dated after the 2026-09-19 pass's own reads.

Run alongside the scripted ingest on the same raw date. This pass wrote ONLY
`data/raw/2026-09-21/regulation/` (staged.jsonl, manifest-regulation.md, pages/) and read
nothing at the top level of `data/raw/2026-09-21/`. **Nothing was written to
`data/signals/**`, `seen.txt`, `register.db`, `data/problems/**` or `feeds.json`.** No
`db.py` call. No `normalize.py --complete`. No git operation.

**Records staged: 4**, all `reg-` prefixed, `source: reg-scan`, `extraction: manual`, each
quote verified mechanically as a literal substring of the whitespace-collapsed payload and
≤300 chars. File: `data/raw/2026-09-21/regulation/staged.jsonl`. They are NOT appended; the
coordinator runs the real `--complete`.

| id | instrument | status | date | payload |
|---|---|---|---|---|
| `reg-agri-pisemne-smlouvy-2028` | Reg. (EU) 2026/1739, Art. 168 of Reg. 1308/2013 rewritten | **ENACTED** (OJ L 29 Jul 2026, in force 18 Aug 2026) | 2028-08-19 | `eu/32026R1739-en.html` |
| `reg-esrs-value-chain-cap-2027` | Del. Reg. (EU) 2026/1560, voluntary standard + value chain cap | **ENACTED** (OJ L 21 Sep 2026, in force 24 Sep 2026) | 2027-01-01 | `eu/32026R1560-en.html` |
| `reg-esrs-revize-2027` | Del. Reg. (EU) 2026/1563, ESRS Annexes I and II replaced | **ENACTED** (OJ L 21 Sep 2026, in force 10 Nov 2026) | 2027-01-01 | `eu/32026R1563-en.html` |
| `reg-ehds-metadata-drzitele-dat-2029` | Impl. Reg. (EU) 2026/2098, EHDS minimum metadata | **ENACTED** (OJ L 21 Sep 2026, in force 11 Oct 2026) | 2029-03-26 | `eu/32026R2098-en.html` |

All four are ENACTED. **No draft was staged this pass**, so the draft ceiling on a record's
Why now is not engaged by anything here.

### Registry changes needed

**None.** `reg-` prefix and `source: reg-scan` only. No `veklep-` id minted, no feeds.json row
touched.

### Access notes (measured today, 2026-09-21)

- **vlada.gov.cz** — both checklist pages HTTP 200 with the descriptive UA
  `localproblems-reg-scan/1.0 (+https://localproblems.vercel.app)`.
- **The vlada RSS URL in the 2026-09-19 notes is not a working URL on its own.** `/cz/rss.aspx`
  and `/rss/` both return HTTP 404. The feed is at
  `https://vlada.gov.cz/cs/urad/RSS/rss.xml` (HTTP 200, 9,370 bytes, 10 items), linked from
  `/cz/urad-vlady/rss/rss-21080/`. Recorded here so the next pass does not re-derive it.
- **ODok host move confirmed again.** `https://www.odok.cz/portal/zvlady/jednani-detail/2026-09-21`
  answers HTTP 302 → `https://www.odok.gov.cz/portal/zvlady/jednani-detail/2026-09-21/` and
  serves 52,128 bytes on `-L --http1.1`. Unchanged from the 2026-09-19 finding.
- **e-Sbírka ELI open data** (`https://opendata.eselpoint.gov.cz/esel-esb/eli/cz/sb/2026/<n>`,
  `Accept: text/turtle`) worked on every probe, single-threaded, no proxy errors.
- **EUR-Lex** was again not fetched directly (the WAF challenge documented on 2026-09-18). The
  CELLAR SPARQL endpoint `https://publications.europa.eu/webapi/rdf/sparql` and CELEX content
  negotiation at `http://publications.europa.eu/resource/celex/<CELEX>` both returned HTTP 200.
- **psp.cz** serves windows-1250; decoding it as UTF-8 silently mangles the bill history. Both
  bill pages were decoded as cp1250 before reading.

---

### Checklist source 1 — Programové prohlášení vlády + semi-annual fulfilment evaluations

**Visited, nothing new since 2026-09-19.**
`https://vlada.gov.cz/cz/vlada/programove-prohlaseni/programove-prohlaseni-vlady-224629/` —
**HTTP 200, 181,238 bytes**. Attachment diff: still exactly one attachment,
`/assets/vlada/programove-prohlaseni/programove-prohlaseni-vlady.pdf`, page dated 5. 1. 2026.
No fulfilment evaluation is attached or linked.

The government RSS (`https://vlada.gov.cz/cs/urad/RSS/rss.xml`, HTTP 200, 10 items, newest
21 Sep 2026) carries **two items new since the 2026-09-19 read**, both pointing at today's
cabinet meeting: "Program schůze vlády dne" and "Dodatek č. 1 programu schůze vlády dne".
Both were read through the ODok agenda (`vlada/odok-jednani-2026-09-21.html`). The 21 Sep 2026
agenda is 17 items: the 2027 state budget (671/26) and the SFDI (708/26), SFPI (658/26) and
R&D (709/26) budgets; the sport-support act amendment (675/26 = `veklep-ALBSDW3HDEWG`, which
the 2026-09-19 pass already read and did not record); **691/26, the government regulation on
the 2027 assessment base for health insurance paid by the state** — the input the 2027
reimbursement decree already assumes, recorded as context in
`reg-uhradova-2027-centrove-leky-slevy`; the National Climate Adaptation Action Plan 2026–2030
(674/26); the general programme document for ETS revenue (611/26); five council-statute
changes; the NÚKIB/Microsoft Government Security Program mandate (677/26); a hydrogen
flexibility study (702/26); quality-policy and wiretap reports; the supported-energy-sources
budget resolution for 2027 (712/26); and an Italy–Czechia action plan (713/26).

**No record staged from source 1.** The meeting is today and nothing on the agenda carries a
dated duty on businesses that the corpus does not already hold. **Carried gap, unchanged:
there is still no machine-readable fulfilment evaluation of the programme.** The programme
itself is a January 2026 PDF; the next semi-annual evaluation is expected around January 2027.

### Checklist source 2 — Plán legislativních prací vlády 2026

**Visited, unchanged since 2026-09-19.**
`https://vlada.gov.cz/cz/ppov/lrv/dokumenty/plan-legislativnich-praci-vlady-na-rok-2026-226017/`
— **HTTP 200, 43,070 bytes**. Attachment diff: the same two annexes,
`1234_2026_priloha_c-_1.pdf` and `1234_2026_priloha_c-_2.pdf`, page still dated 23. 3. 2026
(with 20. 3. 2026 as the government-resolution date). Both annexes were read in full on
2026-09-18; no re-read was owed and none was performed. **No record staged from source 2.**
The 2027 plan is not published; a future pass owes the switch-over.

### Checklist source 3 — e-Sbírka and EUR-Lex (items since 2026-09-19)

**e-Sbírka — visited.** Probed 2026/166 through 2026/178 on the ELI open-data endpoint.

- **CARRIED DEBT PARTLY CLEARED: 166/2026 is no longer an empty shell.** On 2026-09-19 it
  returned the 768-byte prefix-only stub. Today `eli-2026-166.ttl` is **1,540 bytes** and
  carries `citace-právního-aktu "166/2026 Sb."` with one version, `0000-00-00`, whose resource
  (`eli-2026-166-znenie.ttl`) gives `má-typ-znění-právního-aktu` VYHLZNE and
  **`účinnost-znění-od "2026-09-15"`**. So: the act exists, is the promulgated version, and is
  in force from **15 September 2026**. The **text is still not digitised** — all three
  fragments under `.../dokument/prefix` (`frag_1248161289`, `frag_1248161291`, and the prefix
  node itself) return the 768-byte empty shell, and `.../dokument` and the year-level
  collection `.../eli/cz/sb/2026` do the same. **No record staged:** a record whose only
  content would be a number and a date is not a receipt. **The gap is narrowed, not closed**,
  and the next pass owes 166/2026 its title and subject.
- **Newest act is still 167/2026 Sb.** (versions 2026-09-16 and 2026-10-01, positive control
  passed in the same run). **168–178/2026 all return the 768-byte empty shell** —
  `eli-2026-168.ttl` … `eli-2026-178.ttl`. Eleven consecutive empties, three more numbers than
  the 2026-09-19 pass probed.
- **CARRIED DEBT NOT CLEARED: EET 2.0 still has no Sbírka number.** Re-measured at source:
  `https://www.psp.cz/sqw/historie.sqw?o=10&t=189` (HTTP 200, 49,770 bytes, "Stav projednávání
  ke dni: 21. září 2026") ends at "Prezident zákon podepsal 17. 9. 2026. Rozhodnutí doručeno do
  Sněmovny 17. 9. 2026." — **no promulgation line, and 168+ are empty in e-Sbírka**, which are
  two independent receipts for the same answer. `reg-eet2-2027` and `reg-mf-eet2-2027` still
  owe their enactment number and in-force date.
- **CARRIED DEBT MEASURED, NOT CLEARED: sněmovní tisk 48** (novela zákona o rostlinolékařské
  péči), the act the 2026-09-19 pass needed to date the Implementing Reg. (EU) 2023/564 digital
  spray-record duty. `https://www.psp.cz/sqw/historie.sqw?o=10&t=48` (HTTP 200, 37,983 bytes):
  the bill **was sent back from third reading into the general debate of the second reading on
  5 June 2026** (hlasování č. 72, usnesení č. 204), and the newest document on it is an
  amendment filed 10 September 2026. **There is therefore still no Czech date** for the
  2023/564 duty, and now a reason why: the carrier bill is stalled and carries unrelated
  hunting-law amendments. The gap stands with its cause named.

**EUR-Lex — visited via CELLAR.** Every act with an OJ publication date in
**2026-09-19 .. 2026-09-21** was enumerated: `eu/ojL-pub-2026-09-19_21.rq` and
`.json`, **78 distinct CELEX**. The 2026-09-19 pass covered 09-17..09-19, so the delta is the
OJ of **21 September 2026** (plus `32026C04922`, a Commission statement on the budgetary
treatment of the customs handling fee, which belongs to the already-recorded
`reg-eu-customs-code-2026-2108`). 41 of the 78 are court documents (CELEX starting `6`), 12 are
corrigenda (`…R(0n)`), and the remaining 25 are listed below.

**RECORDED — three acts from the OJ L of 21 September 2026:**

- **`reg-esrs-value-chain-cap-2027`** — Del. Reg. (EU) 2026/1560 of 3 July 2026 establishes the
  voluntary sustainability reporting standard **and the value chain cap**: an Art 19a/29a
  reporter may not demand more from a value-chain undertaking under 1,000 employees than the
  Annex II datapoints. In force 24 Sep 2026; the cap applies from financial years beginning on
  or after **1 Jan 2027**.
- **`reg-esrs-revize-2027`** — Del. Reg. (EU) 2026/1563 of 3 July 2026 **replaces Annexes I and
  II of Del. Reg. (EU) 2023/2772** (the ESRS). In force **10 Nov 2026**, applies to financial
  years beginning on or after **1 Jan 2027**, with an Art 2 optional-version regime plus eight
  named reliefs for financial years starting in 2026.
- **`reg-ehds-metadata-drzitele-dat-2029`** — Impl. Reg. (EU) 2026/2098 of 18 Sep 2026 fixes the
  **minimum metadata every health data holder must publish** for dataset descriptions under
  Art 77(4) EHDS, expressed in HealthDCAT-AP. In force 11 Oct 2026, applies **26 Mar 2029**.

**CARRIED DEBT CLEARED, and it produced the fourth record:**

- **`reg-agri-pisemne-smlouvy-2028`** — **32026R1739 has been read.** Named unread by the
  2026-09-18 pass and again by the 2026-09-19 pass, it was fetched today in full by CELEX
  content negotiation (270,928 bytes). It is Regulation (EU) 2026/1739 of 8 July 2026
  strengthening the position of farmers in the food supply chain, published 29 Jul 2026, in
  force 18 Aug 2026 (both dates confirmed independently through the CELLAR properties
  `official-journal-act_date_publication` and `resource_legal_date_entry-into-force`, file
  `eu/probe.json`). Its point (9) **replaces Article 168 of Reg. (EU) No 1308/2013**: from
  **19 August 2028**, deliveries of agricultural products in all sectors other than milk and
  sugar, by farmers, farmers' associations and producer organisations to processors,
  distributors or retailers, **must be covered by a written contract concluded in advance**
  with a prescribed content. This converts what was a Member-State option into a directly
  applicable EU duty. Point (4) does the same for milk (Art 148), point (14) for sugar-beet
  delivery contracts (Annex X), point (13) applies from 19 Aug 2029, and Art 4 lets
  non-conforming products be sold down until 19 Aug 2032.

**Not recorded, stated rather than silent:**

- **32026R2083, MyHealth@EU** (applies 26 Mar 2027) — its duties fall on national contact
  points for digital health and on the Commission. State infrastructure, not a market duty;
  Art 18 grandfathers existing eHDSI contact points. It is noted inside
  `reg-ehds-metadata-drzitele-dat-2029` so the next pass does not re-discover it.
- **32026R2096 / 32026R2097** (epidemiological surveillance network procedures; the
  communicable-disease list replacing Impl. Dec. (EU) 2018/945) — public-health administration.
- **32026R2135** (African swine fever control zones) and **32026R2105** (a Hungarian
  geographical indication) — no Czech duty-holder.
- **Feed-additive authorisations** 32026R2084, 2086, 2087, 2090, 2091, 2128, 2130 — the same
  class the 2026-09-19 pass excluded.
- **Trade defence** 32026R2088 and 32026R2089 (definitive anti-dumping duties), **32026R2085**
  (a Mediterranean fishing derogation) and **32026R2143** (the 361st amendment of the
  Al-Qaida sanctions list).
- **32026C04922**, the Commission statement on the budgetary treatment of the handling fee —
  it belongs to `reg-eu-customs-code-2026-2108`, recorded on 2026-09-19.
- **No directive** was published in the window: no `32026L…` rows in the enumeration.

### Checklist source 4 — VeKLEP RIA "Definice problému"

**Visited, and the honest answer is that there was nothing for this pass to read.**

SCANS.md item 4 makes this pass read the RIA problem statements **for the items the scripted
`veklep` feed surfaced**, never re-fetching what the script fetched. State as measured today:

- The scripted `veklep` fetch for 2026-09-21 completed at 08:08:17Z — `ok=1`, HTTP 200,
  1,717,848 bytes, **138 items fetched** (`data/raw/2026-09-21/.fetch/receipts.jsonl`). Its
  payloads are at the top level of `data/raw/2026-09-21/`, which this pass was instructed not
  to read, and did not.
- **`data/raw/2026-09-21/staged.jsonl` does not exist.** `normalize.py` has not yet run over
  that fetch, so **no draft has been surfaced as a signal yet** and there is no id list to read
  RIA sections against. Checked at 10:14Z.
- The previous input, `data/signals/regulation/2026-09-19.jsonl`, holds 19 `veklep-` ids, and
  the 2026-09-19 pass opened **all 19** and read each RIA chapter or důvodová zpráva. That debt
  is discharged; re-reading the same documents two days later would be make-work, and `cmp`
  showed two of them byte-identical to the prior day's capture even then.

**NAMED COVERAGE GAP (new this pass):** the RIA "Definice problému" sections for whatever the
2026-09-21 `veklep` fetch surfaces are **owed to the next pass**, and cannot be read until the
coordinator runs `normalize.py` over `data/raw/2026-09-21/`. This is a sequencing gap, not a
source failure: the script is LIVE and returned 138 items today.

Two item-level debts from 2026-09-19 were carried forward and worked on anyway, both reported
under source 3 above: **tisk 48** for `veklep-KORNDXY9WP89` (measured: stalled in second
reading) and the **sport-support act** `veklep-ALBSDW3HDEWG` (confirmed on today's cabinet
agenda, still with no dated duty on businesses, so still not recorded).

---

### Evidence-bar compliance

- **Enacted vs draft** is stated as `STATUS:` in the first clause of every record's `notes`.
  **4 of 4 are ENACTED**, each with its OJ publication date and its entry-into-force date.
  No draft was staged.
- **Dates:** each record's `date` is the application/compliance date the duty bites on
  (2028-08-19, 2027-01-01, 2027-01-01, 2029-03-26). Every other date — publication, entry into
  force, phase-ins, transitional windows — is in `notes` with the clause quoted.
- **Urgency:**
  - `reg-esrs-value-chain-cap-2027` and `reg-esrs-revize-2027` score **3**: both bite on
    financial years beginning on or after 1 Jan 2027, under six months out, and both are in
    force as instruments.
  - `reg-agri-pisemne-smlouvy-2028` scores **1**: 19 Aug 2028 is about 23 months out, over the
    18-month line.
  - `reg-ehds-metadata-drzitele-dat-2029` scores **1**: 26 Mar 2029.
- **Money:** `money_eur` is null on all 4, each with a `money_note` saying why. The CAP
  co-financing percentages in 2026/1739 are Member-State allocations, not budget attached to
  the need, so nothing was scored and nothing was estimated.
- **Quotes:** 4 of 4 verified **mechanically**, in one script, as literal substrings of the
  whitespace-collapsed payload text (`re.sub(r'\s+',' ', payload)`), each ≤300 chars — measured
  lengths 227, 282, 251, 184. Typographic quotation marks and apostrophes were preserved
  exactly as the payload carries them.
- **No absence claim without a search:** each "nothing in the corpus" statement in `notes` names
  the terms searched across all 18,420 signal lines (1308/2013, 2026/1739, food supply chain,
  written contract, producer organisation, unfair trading; VSME, value chain cap, 2023/2772,
  ESRS, 2026/470; HealthDCAT-AP, Article 77(4)).
- **No personal data.** A regex grep of `staged.jsonl` for email and phone patterns returns 0.
  No natural person is named in any record.

### Facts in existing records this pass found stale (for MATCH/PROCESS; nothing was edited)

- **`reg-csrd-post-omnibus`** says "Final Omnibus I text pending formal adoption — treat
  scope/dates as agreed but not yet in OJ". Today's payloads show this is stale: **Directive
  (EU) 2026/470 of 24 February 2026** amending Directives 2006/43/EC, 2013/34/EU, (EU) 2022/2464
  and (EU) 2024/1760 is cited as adopted law by both 2026/1560 and 2026/1563, and it is the act
  that re-scopes Arts 19a/29a "from financial years beginning on or after 1 January 2027". The
  same record's VSME prose is now superseded by an instrument with an ELI
  (`reg-esrs-value-chain-cap-2027`).
- **`reg-ehds`** dates the secondary-use start at 2029-03-26 and says "implementing acts due
  Mar 2027". The first implementing acts are now out ahead of that: 2026/2083 and 2026/2098,
  both published 21 Sep 2026.
- **`reg-eet2-2027` / `reg-mf-eet2-2027`** are unchanged from the 2026-09-19 finding: passed,
  signed 17 Sep 2026, still no Sbírka number as of today.

### New problem candidate for the register (for MATCH, not staged as a problem)

**Contract paperwork for the Czech agri-food chain, dated 19 August 2028.** Every Czech farmer,
farming cooperative and producer organisation selling anything other than milk or sugar to a
processor, wholesaler or grocery chain will need a written contract agreed **before delivery**
carrying a price formula tied to objective cost indicators, quantities, quality, duration with
a farmer-triggerable revision clause on anything over 12 months, payment terms, collection
arrangements and force-majeure rules. Today much of that trade runs on purchase orders and
spot agreement. The derogation for deliveries inside a member's own cooperative makes
cooperative statutes the alternative compliance route, which is itself work. Nothing in the
corpus covers it. The complement, `reg-esrs-value-chain-cap-2027`, is the other half of the
same shape: a finite, published dataset a Czech SME supplier can be asked for, which is what a
supplier-side tool is built against.

### Dry run (validation only, nothing written to the ledgers)

```
cp -R data/signals $TMPDIR/reg-sim/signals
python3 scripts/normalize.py --raw data/raw/2026-09-21/regulation --complete --dry-run --today 2026-09-21 \
    --out-dir $TMPDIR/reg-sim/signals --seen $TMPDIR/reg-sim/signals/seen.txt
  -> would append 4 records across 1 file(s); 0 dropped by materiality; 0 incomplete;
     0 refused by AC-GDPR1
     $TMPDIR/reg-sim/signals/regulation/2026-09-21.jsonl: +4
     dedup by identity key (append): 0 skipped
     AC-GDPR1 allowlist: dropped 4 non-allowlisted field(s) across 4 record(s): evidence_type
```

`evidence_type: "regulation"` is carried on each staged line for routing only and is stripped
on append, exactly as on 2026-09-19. The first dry run of this pass, written without it,
routed all four to `demand/2026-09-21.jsonl` — worth recording, because that misrouting is
silent and the staged file looks correct either way.

**Owed to the coordinator:** the real
`python3 scripts/normalize.py --raw data/raw/2026-09-21/regulation --complete` (it appends to
`data/signals/regulation/2026-09-21.jsonl`, the same file the scripted `veklep` run will write
once it is normalized) and the `db.py upsert` line it prints. Nothing was committed.

### Coverage gaps named

1. **No machine-readable fulfilment evaluation of the government programme exists** (carried
   from 2026-09-18/19; recheck around January 2027). The programme page carries one January 2026
   PDF and nothing else.
2. **e-Sbírka 166/2026: narrowed, not closed.** It now has an ELI record and an in-force date of
   2026-09-15, but every text fragment is still an empty shell, so its subject is unknown. The
   next pass owes it a title.
3. **EET 2.0 has no Sbírka number** (carried). Signed 17 Sep 2026; e-Sbírka 168–178 are all
   empty and psp.cz shows no promulgation line as of 21 Sep 2026.
4. **Act 130/2026 (AIFMD II transposition, 16 Apr 2027 phase) is identified but not recorded**
   (carried from 2026-09-19). Untouched this pass.
5. **Implementing Reg. (EU) 2023/564 digital spray records has no Czech date** (carried). Cause
   now measured: the carrier bill, sněmovní tisk 48, was sent back into second reading on
   5 Jun 2026 and has not moved since 10 Sep 2026.
6. **The 2027 motorway-vignette rates are still unrecorded** (carried from 2026-09-18/19).
   Untouched this pass.
7. **VeKLEP RIA sections for the 2026-09-21 fetch are unread** (new, sequencing). The script
   fetched 138 items at 08:08Z, but `normalize.py` has not run, no `staged.jsonl` exists and no
   draft has been surfaced as a signal, so there was no id list to read against.
8. **Directive (EU) 2026/470 (Omnibus I) is not in the corpus** (new). It is the parent of both
   ESRS acts recorded today and it re-scopes CSRD from FY2027. It was published before this
   pass's delta window, so recording it is a broad-pass job, not a delta one.
9. **The 2027 Plán legislativních prací is not yet published** (new, expected absence). The 2026
   plan is the current one; a future pass owes the switch-over.

### 5-line pass summary

```
feed:                reg-scan (evidence_type regulation, prefix reg-, weekly delta pass)
checklist sources:   4 of 4 visited (programme + evaluations: HTTP 200, unchanged, no evaluation · plan 2026: HTTP 200, same 2 annexes of 23.3.2026 · e-Sbírka 166 partly digitised / 167 newest / 168-178 empty + EUR-Lex via CELLAR 09-19..21, 78 CELEX · VeKLEP: script fetched 138 items but no staged.jsonl exists yet, nothing surfaced to read)
records staged:      4 (all ENACTED EU acts: 2026/1739 agri contracts, 2026/1560 value chain cap, 2026/1563 ESRS rewrite, 2026/2098 EHDS metadata), dry-run clean, not appended
coverage gaps named: 9 (3 carried unchanged, 2 carried and narrowed with a measured cause, 1 carried untouched, 3 new)
rotation state:      n/a (arb-scan duty)
```


## dotace-scan pass: weekly delta, 2026-09-21

Weekly delta for the `dotace-scan` feed (`data/feeds.json` key `dotace-scan`, `signal_source:
dotace`, `evidence_type: tenders`, `id_prefixes: ["dotace"]`), run under `pipeline/SCANS.md`
(THE CHECKLIST LAW). Worktree: `localproblems-weekly-2026-09-21`. Two days after the
2026-09-19 delta pass, which is this pass's left-hand side.

Raw captures: `data/raw/2026-09-21/dotace/` — the MS2021+ snapshot, three ČNB lists, the
per-call diff, the sorted call-id list, and 45 page captures under `pages/`.
Staged records: `data/raw/2026-09-21/dotace/staged.jsonl` — **zero lines**.

This pass wrote ONLY the two files its brief names plus those raw captures. It did NOT write
`data/signals/**`, `seen.txt`, `data/errata.jsonl`, `data/problems/**`, `data/feeds.json` or
`data/register.db`; it ran no `normalize.py --complete`, no `db.py`, and changed no git state.

### Exchange rate

**24.340 CZK/EUR**, ČNB list **#181 of 18.09.2026** — verified, not assumed. Three requests
were made against
`https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=…`
for `18.09.2026`, `19.09.2026` and `21.09.2026`. All three returned **HTTP 200** and all three
returned the **same payload**, whose first line is `18.09.2026 #181` and which contains
`EMU|euro|1|EUR|24,340`. 20 and 21 September 2026 are Saturday and Sunday, so Friday 18
September is the last fixing, as expected. Saved as `cnb-denni_kurz-18.09.2026.txt`,
`cnb-denni_kurz-19.09.2026.txt`, `cnb-denni_kurz-21.09.2026.txt`. Same rate as the 2026-09-18
and 2026-09-19 passes. No record this pass needed a conversion.

### Checklist source 1: MS2021+ open-data call list

- **Fetch.** `https://ms21opendata.mssf.cz/SeznamVyzev_21_27.xml` → **HTTP 200, 1,669,846
  bytes**, fetched at **2026-09-21T08:08:01Z**. The payload carries
  `DATE="2026-09-20T20:45:00.000+02:00"` — Saturday night's export, the freshest one
  available on a Sunday morning; there is no Sunday-morning export.
- **Snapshot.** `data/raw/2026-09-21/dotace/ms21-SeznamVyzev_21_27.xml`,
  sha256 `626dfc43b14cdf586750373e5e6b55f5f10249cc9a5c78a37e7750de4b1bfd89`.
- **Left-hand side.** The 2026-09-19 snapshot (payload DATE 2026-09-18T20:45, 817 codes), at
  `localproblems/data/raw/2026-09-19/dotace/ms21-SeznamVyzev_21_27.xml` in the MAIN checkout.
  It was still on disk, so 2026-09-19 coverage gap 7 ("left-hand-side location") did not bite.
  **This pass fixes that class of gap for good**: the full call-id list is written into this
  manifest below, so the next pass has a left-hand side even if every payload is pruned.
- **Method.** Per-call field diff: every leaf field of every `<VYZVA>`, keyed by `KOD`,
  namespace-aware. It catches code additions/removals AND state/date/allocation changes on
  existing codes — the latter is how a newly opened call actually shows up here. Output saved
  as `ms21-diff-2026-09-19-vs-21.txt`.

**Result: 817 → 817 codes. Added 0, removed 0. One code changed:**

| KOD | change | in the ledger? | outcome |
|---|---|---|---|
| `06_22_070` | STAV **Pozastavená → Otevřená** (IROP 70, Kultura — památky a muzea, SC 5.1 CLLD) | no | not minted — see below |

**Newly opened call ids: `06_22_070`, and that is a re-opening, not a new call.** No code is
new to the list, none moved into *Vyhlášená*, and no call the ledger holds changed its dates
or allocation. `05_26_107` (OPŽP 107) is still *Rozpracovaná*; `02_25_044`, `02_25_045` and
`02_26_046` (OPJAK) are still *Plánovaná*; the open-call backlog items with September
deadlines (`12_26_046` closes 2026-09-23, `03_24_059` / `10_25_089` / `14_26_018` close
2026-09-30) are unchanged in state, date and allocation.

**Why `06_22_070` was not minted.** This is the **discharge of 2026-09-19 coverage gap 6**, the
XML-versus-portal contradiction. The XML has converged to the portal, not the other way round:
`irop.gov.cz/cs/Vyzvy-2021-2027/Vyzvy/70vyzvaIROP` (HTTP 200, saved as
`pages/irop-70-vyzva.html`) reads `Stav výzvy: Otevřená`, `Číslo výzvy: 06_22_070`, `Ukončení
příjmu žádostí: 31. 12. 2027`, exactly as it did on 2026-09-19. So the two-day *Pozastavená*
in the XML was a transient export state and the portal was right throughout. **The
contradiction is resolved; the debt is closed.** The call itself is unchanged since 2023 —
a CLLD envelope for monument and municipal-museum revitalisation, allocation 973,985,258.02
CZK, open 19 July 2023 to 31 December 2027. The 2026-09-19 judgment stands: heritage
construction money routed through local action groups, no builder-facing need, not minted.

**This pass's full MS2021+ call-id list — the next pass's left-hand side.**
817 codes, sorted. sha256 of the sorted newline-joined list:
`ac83c80814d4f9414369f044e0f939fc1c672c01981bb71f6f4bef41206e13aa`.
Also written to `data/raw/2026-09-21/dotace/ms21-kody-2026-09-21.txt` (one code per line),
which is a pruned-at-28-days payload — the list below is the durable copy.

```
01_22_001 01_22_002 01_22_003 01_22_004 01_22_005 01_22_006 01_22_007 01_22_008
01_23_009 01_23_010 01_23_011 01_23_012 01_23_013 01_23_014 01_23_015 01_23_016
01_23_017 01_23_018 01_23_019 01_23_020 01_23_021 01_23_022 01_23_023 01_23_024
01_23_025 01_23_026 01_23_027 01_23_028 01_23_029 01_23_030 01_23_031 01_23_032
01_23_033 01_23_034 01_23_035 01_23_036 01_23_037 01_23_039 01_23_040 01_23_041
01_24_038 01_24_042 01_24_043 01_24_044 01_24_045 01_24_046 01_24_047 01_24_048
01_24_049 01_24_050 01_24_051 01_24_052 01_24_053 01_24_054 01_24_055 01_24_056
01_24_059 01_24_060 01_24_061 01_24_062 01_24_063 01_24_065 01_24_073 01_25_057
01_25_058 01_25_064 01_25_066 01_25_067 01_25_068 01_25_069 01_25_070 01_25_071
01_25_072 01_25_074 01_25_075 01_25_076 01_25_077 01_25_078 01_25_079 01_25_080
01_25_081 01_25_082 01_25_083 01_26_084 01_26_085 01_26_086 01_26_087 01_26_088
01_26_089 01_26_090 01_26_091 01_26_092 01_26_093 01_26_094 01_26_095 01_26_096
02_22_001 02_22_002 02_22_003 02_22_004 02_22_005 02_22_006 02_22_007 02_22_008
02_22_009 02_22_010 02_22_011 02_22_012 02_23_013 02_23_014 02_23_015 02_23_016
02_23_017 02_23_018 02_23_019 02_23_020 02_23_021 02_23_022 02_23_023 02_23_024
02_23_025 02_23_026 02_23_027 02_23_028 02_23_029 02_24_030 02_24_031 02_24_032
02_24_033 02_24_034 02_24_035 02_24_036 02_24_037 02_24_038 02_25_039 02_25_040
02_25_041 02_25_042 02_25_043 02_25_044 02_25_045 02_26_046 02_26_047 02_26_048
03_00_094 03_00_095 03_22_001 03_22_002 03_22_003 03_22_004 03_22_005 03_22_006
03_22_007 03_22_008 03_22_009 03_22_010 03_22_011 03_22_012 03_22_013 03_22_014
03_22_015 03_22_016 03_22_017 03_22_018 03_22_019 03_22_020 03_22_021 03_22_022
03_22_023 03_22_024 03_22_025 03_22_026 03_22_027 03_22_028 03_22_029 03_22_030
03_22_031 03_22_032 03_22_033 03_22_034 03_22_035 03_22_036 03_22_037 03_22_038
03_22_039 03_22_040 03_22_041 03_22_042 03_22_043 03_22_044 03_22_045 03_22_046
03_22_099 03_22_100 03_22_101 03_23_047 03_23_048 03_23_049 03_23_050 03_23_051
03_23_052 03_23_053 03_23_054 03_23_055 03_23_056 03_23_057 03_23_058 03_23_093
03_23_096 03_24_059 03_24_060 03_24_061 03_24_062 03_24_063 03_24_064 03_24_065
03_24_066 03_24_067 03_24_068 03_24_069 03_24_070 03_24_071 03_24_072 03_24_073
03_24_074 03_24_075 03_24_076 03_24_077 03_24_078 03_24_079 03_25_080 03_25_081
03_25_082 03_25_083 03_25_084 03_25_085 03_25_086 03_25_087 03_25_088 03_25_089
03_25_097 03_25_102 03_25_103 03_25_104 03_25_105 03_25_106 03_25_108 03_25_109
03_25_110 03_26_090 03_26_091 03_26_107 03_26_111 03_26_112 03_27_092 03_27_098
04_22_001 04_22_002 04_22_003 04_22_004 04_22_005 04_22_006 04_22_007 04_22_008
04_22_009 04_22_010 04_23_011 04_23_012 04_23_013 04_23_014 04_23_015 04_23_016
04_23_017 04_23_018 04_23_019 04_23_020 04_23_021 04_23_022 04_23_023 04_24_024
04_24_025 04_24_026 04_24_027 04_24_028 04_24_029 04_24_030 04_24_031 04_24_032
04_24_033 04_24_034 04_24_035 04_25_036 04_25_037 04_25_038 04_25_039 04_25_040
04_25_041 04_25_042 04_25_043 04_26_044 04_26_045 04_26_046 04_26_047 04_26_048
05_22_001 05_22_002 05_22_003 05_22_004 05_22_005 05_22_006 05_22_007 05_22_008
05_22_009 05_22_010 05_22_011 05_22_012 05_22_013 05_22_014 05_22_015 05_22_016
05_22_017 05_22_018 05_22_019 05_22_020 05_22_021 05_22_022 05_22_023 05_22_024
05_22_025 05_22_026 05_22_027 05_22_028 05_22_029 05_22_030 05_22_031 05_23_032
05_23_033 05_23_034 05_23_035 05_23_036 05_23_037 05_23_038 05_23_039 05_23_040
05_23_041 05_23_042 05_23_043 05_23_044 05_23_045 05_23_046 05_23_047 05_23_048
05_23_049 05_23_050 05_23_051 05_23_052 05_23_053 05_23_054 05_23_055 05_23_056
05_23_057 05_23_058 05_23_059 05_23_060 05_23_061 05_23_062 05_24_063 05_24_064
05_24_065 05_24_066 05_24_067 05_24_068 05_24_069 05_24_070 05_24_071 05_24_072
05_24_073 05_24_074 05_24_075 05_24_076 05_24_077 05_24_078 05_24_080 05_24_083
05_25_079 05_25_081 05_25_082 05_25_084 05_25_085 05_25_086 05_25_087 05_25_088
05_25_089 05_25_090 05_25_091 05_25_092 05_25_093 05_25_094 05_25_095 05_25_096
05_25_097 05_25_098 05_25_099 05_25_100 05_26_101 05_26_102 05_26_103 05_26_104
05_26_105 05_26_106 05_26_107 05_26_108 05_26_109 06_22_001 06_22_002 06_22_003
06_22_004 06_22_005 06_22_006 06_22_007 06_22_008 06_22_009 06_22_010 06_22_011
06_22_012 06_22_013 06_22_014 06_22_015 06_22_016 06_22_017 06_22_018 06_22_019
06_22_020 06_22_021 06_22_022 06_22_023 06_22_024 06_22_025 06_22_026 06_22_027
06_22_028 06_22_029 06_22_030 06_22_031 06_22_032 06_22_033 06_22_034 06_22_035
06_22_036 06_22_037 06_22_038 06_22_039 06_22_040 06_22_041 06_22_042 06_22_043
06_22_044 06_22_045 06_22_046 06_22_047 06_22_048 06_22_049 06_22_050 06_22_051
06_22_052 06_22_053 06_22_054 06_22_055 06_22_056 06_22_057 06_22_058 06_22_059
06_22_060 06_22_061 06_22_062 06_22_063 06_22_064 06_22_065 06_22_066 06_22_067
06_22_068 06_22_069 06_22_070 06_22_111 06_22_112 06_23_071 06_23_072 06_23_073
06_23_074 06_23_075 06_23_076 06_23_077 06_23_078 06_23_079 06_23_080 06_23_081
06_23_082 06_23_083 06_23_084 06_23_085 06_23_086 06_23_087 06_23_088 06_23_089
06_23_090 06_23_091 06_23_092 06_23_093 06_23_094 06_23_095 06_23_096 06_23_097
06_23_098 06_23_099 06_23_100 06_23_101 06_23_102 06_23_103 06_23_104 06_23_105
06_23_106 06_23_107 06_23_108 06_23_109 06_23_110 06_23_113 06_23_114 06_24_115
06_24_116 06_25_117 06_25_118 06_26_119 06_26_120 06_26_121 06_26_122 07_22_001
07_22_002 07_22_003 07_22_004 07_22_005 08_22_001 08_22_002 08_22_003 08_23_004
08_23_005 08_23_006 08_23_007 08_23_008 08_23_009 08_23_010 08_23_011 08_23_012
08_23_013 08_23_014 08_24_015 08_24_016 08_24_017 08_24_018 08_24_019 08_24_020
08_24_021 08_24_022 08_24_023 08_25_024 08_25_025 08_25_026 08_25_027 08_25_028
08_25_029 08_25_030 08_26_031 08_26_032 08_26_033 08_26_034 08_26_035 08_26_036
08_26_037 08_26_038 08_26_039 10_22_001 10_22_002 10_22_003 10_22_004 10_23_005
10_23_006 10_23_007 10_23_008 10_23_009 10_23_010 10_23_011 10_23_012 10_23_013
10_23_014 10_23_015 10_23_016 10_23_017 10_23_018 10_23_019 10_23_020 10_23_021
10_23_022 10_23_023 10_23_024 10_23_025 10_23_026 10_23_027 10_23_028 10_23_029
10_23_030 10_23_031 10_23_032 10_23_033 10_23_034 10_23_035 10_23_036 10_23_037
10_23_038 10_23_039 10_23_040 10_23_041 10_23_042 10_23_043 10_23_044 10_23_045
10_23_046 10_24_047 10_24_048 10_24_049 10_24_050 10_24_051 10_24_052 10_24_053
10_24_054 10_24_055 10_24_056 10_24_057 10_24_058 10_24_059 10_24_060 10_24_061
10_24_062 10_24_063 10_24_064 10_24_065 10_24_066 10_24_067 10_24_068 10_24_069
10_24_070 10_24_071 10_24_072 10_25_073 10_25_074 10_25_075 10_25_076 10_25_077
10_25_078 10_25_079 10_25_080 10_25_081 10_25_082 10_25_083 10_25_084 10_25_085
10_25_086 10_25_087 10_25_088 10_25_089 10_25_090 10_25_091 10_25_092 10_25_093
10_25_094 10_25_095 10_25_096 10_25_097 10_25_098 10_25_099 10_25_100 10_25_101
10_25_102 10_25_103 10_25_104 10_26_105 10_26_106 10_26_107 10_26_108 10_26_109
10_26_110 10_26_111 10_26_112 10_26_113 10_26_114 10_26_115 10_26_116 10_26_117
10_26_118 11_22_001 11_22_002 11_23_003 11_23_004 11_23_005 11_23_006 11_23_007
11_23_008 11_23_009 11_23_010 11_23_011 11_24_012 11_24_013 11_24_014 11_24_015
11_24_016 11_24_017 11_25_018 11_25_019 11_25_020 11_25_021 11_26_022 12_22_001
12_22_002 12_22_003 12_22_004 12_23_005 12_23_006 12_23_007 12_23_008 12_23_009
12_23_010 12_23_011 12_23_012 12_23_013 12_23_014 12_23_015 12_23_016 12_23_017
12_24_018 12_24_019 12_24_020 12_24_021 12_24_022 12_24_023 12_24_024 12_25_025
12_25_026 12_25_027 12_25_028 12_25_029 12_25_030 12_25_031 12_25_032 12_25_033
12_25_034 12_25_035 12_25_036 12_25_037 12_25_038 12_26_039 12_26_040 12_26_041
12_26_042 12_26_043 12_26_044 12_26_045 12_26_046 12_26_047 12_26_048 12_26_049
12_26_050 12_26_051 12_26_052 12_26_053 12_26_054 12_26_055 12_26_056 13_22_001
13_23_002 13_23_003 13_23_004 13_23_005 13_23_006 13_23_007 13_23_008 13_24_009
13_24_010 13_24_011 13_24_012 13_25_013 13_25_014 13_26_015 13_26_016 13_26_017
13_26_018 13_26_019 13_26_020 14_22_001 14_22_002 14_23_003 14_23_004 14_23_005
14_23_006 14_23_007 14_23_008 14_24_009 14_24_010 14_24_011 14_25_012 14_25_013
14_25_014 14_25_015 14_25_016 14_26_017 14_26_018 14_26_019 14_26_020 14_26_021
14_26_022
```

### Checklist source 2: the portals the `feeds.json` row names

Every page below was fetched on 2026-09-21 and compared with its 2026-09-19 capture in
`localproblems/data/raw/2026-09-19/dotace/pages/`. The comparison strips tags, scripts, styles
and comments, collapses whitespace and diffs visible text line by line, so nonces and cache
tokens do not register. "Text-identical" means no visible line changed.

- **IROP** — `https://irop.gov.cz/cs/vyzvy-2021-2027` (page 1, newest first): **HTTP 200,
  text-identical, nothing new since 2026-09-19**. `…/Vyzvy-2021-2027/Vyzvy/70vyzvaIROP`:
  HTTP 200, still *Otevřená* (see above); the only visible changes on it are the call's own
  statistics box (`Statistiky k výzvě – 18. 9. 2026` → `20. 9. 2026`, 632,543,194 Kč →
  633,543,544 Kč requested, 360 → 361 applications, 73.0 % → 73.1 % of the allocation), which
  is project traffic, not a call change. **NOTE the URL shape**: the lower-case
  `…/cs/vyzvy/70vyzvairop` path the 2026-09-19 pass used now returns **HTTP 404**; the live
  shape is `…/cs/Vyzvy-2021-2027/Vyzvy/70vyzvaIROP`. Saved as `pages/irop-vyzvy-p1.html`,
  `pages/irop-70-vyzva.html`.
  **The deep listing was walked this pass — see "Carried debts cleared" below.**
- **OPŽP** — `https://opzp.cz/nabidka-dotaci/` and `https://opzp.cz/dotace/107-vyzva/`: both
  **HTTP 200, text-identical. Nothing new since 2026-09-19.** Call 107 is still *Plánovaná* on
  the portal and *Rozpracovaná* in the XML, accessible from 2026-09-30, close 2026-11-25,
  allocation 125,000,000 CZK. The POST API `/wp-json/opzp/v1/call/html` was not re-queried:
  the rendered listing is unchanged. Saved as `pages/opzp-nabidka-dotaci.html`,
  `pages/opzp-107-vyzva.html`.
- **OPJAK** — `https://opjak.cz/vyzvy/` and `https://opjak.cz/harmonogram-vyzev/`: both
  **HTTP 200. Nothing new since 2026-09-19.** `/vyzvy/` has exactly one changed visible line,
  a dashboard statistic (`Podpořené žádosti 48 %` → `55 %`); no call row changed and no call
  was added. `/harmonogram-vyzev/` is text-identical — still schedule v2 of 20 Feb 2026, and
  `02_25_044` / `02_25_045` / `02_26_046` are still unpublished as calls. Saved as
  `pages/opjak-vyzvy.html`, `pages/opjak-harmonogram-vyzev.html`.
- **SFŽP** — `https://sfzp.gov.cz/dotace-a-pujcky/`,
  `…/dotace-a-pujcky/financni-nastroje-a-pujcky/` and
  `…/dotace-a-pujcky/modernizacni-fond/vyzvy/`: all three **HTTP 200, all three
  text-identical. Nothing new since 2026-09-19.** Saved as `pages/sfzp-dotace-a-pujcky.html`,
  `pages/sfzp-fn.html`, `pages/sfzp-mf-vyzvy.html`.
- **NPO** — `https://planobnovy.gov.cz/vyhlasene-vyzvy/`: **HTTP 200, text-identical. Nothing
  new since 2026-09-19.** Same four declared calls, all already in the ledger. Saved as
  `pages/npo-vyhlasene-vyzvy.html`.
- **TAČR** — `https://tacr.gov.cz/` (home-page news): **HTTP 200, text-identical. Nothing new.**
  `https://tacr.gov.cz/programy-a-souteze/`: **HTTP 200, CHANGED.** Two changes, neither a new
  call:
  1. A **FOREST** programme card appeared in the programme list (status `v přípravě`,
     "Lesy, lesnictví a sektor založený na lesích: Výzkum a inovace pro udržitelnou
     transformaci", linking to `https://tacr.gov.cz/program/forest/`). Followed it: HTTP 200,
     saved as `pages/tacr-forest.html`. The programme page shows `Seznam soutěží: Call 2026 —
     Běží lhůta pro podávání návrhů projektů`, i.e. the call that opened 15 Sep 2026.
     **This is already in the ledger**: `dotace-tacr-forest-call-2026`, minted by the
     2026-09-18 broad pass (500,000 EUR Czech envelope, window 15. 9. – 2. 12. 2026,
     `data/signals/tenders/2026-09-18.jsonl`, id present in `seen.txt`). What changed is only
     the programme's visibility on the index page; no new call, **nothing to mint**. The card
     saying `v přípravě` while its own call page says the submission window is running is a
     publisher inconsistency on TAČR's side, noted, not material.
  2. The `Harmonogram VEŘEJNÝCH SOUTĚŽÍ` calendar rotated: the ŘÍJEN/LISTOPAD/PROSINEC slots
     dropped `Program TREND` (*Uzavřen*) and two `Program SIGMA` rows and now show
     `Program PRODEF` (*Probíhá hodnocení návrhů projektů*). Evaluation-phase bookkeeping on
     already-closed competitions — **no new call**. `Harmonogram pro období 2026-2027 (PDF)`
     is unchanged.
  Saved as `pages/tacr-home.html`, `pages/tacr-programy-a-souteze.html`, `pages/tacr-forest.html`.
- **CINEA / HaDEA** — `https://cinea.ec.europa.eu/funding-opportunities/calls-proposals_en`
  pages 0–3 and `https://hadea.ec.europa.eu/calls-proposals_en`: **all five HTTP 200, all five
  text-identical. Nothing new since 2026-09-19** — no new call cards, no new opening dates.
  (CINEA `?page=2` and `?page=3` first returned **HTTP 429**; both were re-fetched after a
  delay and returned 200. The 429s are recorded here rather than passed off as content.)
  Saved as `pages/cinea-calls-p0..p3.html`, `pages/hadea-calls.html`.

**Checklist: 8 of 8 sources visited**, each named above with its URL and HTTP status.

### Records staged: 0

`data/raw/2026-09-21/dotace/staged.jsonl` has **zero lines**, and that is the correct result
for this pass, not a silence. Two days after the last delta, the MS2021+ list added nothing,
removed nothing, and changed one call's state back to what the portal always said; the seven
named portals produced no new call between them. Nothing was minted and nothing was invented.
No `normalize.py` dry-run was needed, because there is nothing to validate.

The one candidate the portals surfaced — TAČR **FOREST Call 2026** — was checked against
`data/signals/seen.txt` and `data/signals/tenders/*.jsonl` and is **already held** as
`dotace-tacr-forest-call-2026`. Minting it again would have been a duplicate dressed as a
find.

Recording it here because SCANS.md asks for what was checked, not only for what was kept:
the register's URGENCY rule (`SCORING.md`, "NOT A DEADLINE ON THIS LADDER") means a grant's
closing date never by itself justifies a record or a score, so the LIFE family closing
2026-09-22 (below) created no pressure to mint anything today.

### Carried debts cleared this pass

**1. IROP deep listing walked — 2026-09-19 coverage gap 1 is CLOSED.** The listing's
load-more control is an AJAX endpoint,
`https://irop.gov.cz/cs/systemove-stranky/ajax-pages/vyzvyajax2021new?page=<N>&count=10`
(the page markup exposes it as `data-target` + `data-page`; the capitalised path 301s to the
lower-case one). Pages 2–20 were fetched, all HTTP 200; the listing saturates at **page 12**
(pages 13–20 return page 12's ten rows again). Saved as `pages/irop-vyzvy-p2.html` …
`pages/irop-vyzvy-p20.html`. **This is the recipe the next pass should use instead of
skipping the deep walk.**

Result of the walk, cross-checked against today's XML:
- **120 unique call rows on the portal; 122 IROP codes (`06_*`) in the XML.**
- **On the portal but not in the XML: none.**
- **In the XML but not on the portal: `06_23_099` and `06_23_100`** (99. and 100. výzva IROP —
  Podpora integrované onkologické péče, MRR and PR). Both are **`Zrušená`** in the XML, so the
  portal is right to delist them and there is no gap. Not minted: a cancelled call is not an
  opportunity.
- **Status mismatches: two, both immaterial.** `06_22_023` and `06_22_024` (23./24. výzva
  IROP — Základní školy, 2022) read *Uzavřená* on the portal and *Zrušená* in the XML. Both
  closed in November 2022, neither is in the ledger, neither is actionable.
- **58 IROP calls are `Otevřená` in the XML today.** Nothing among them is new since
  2026-09-19.

So the deep walk found **no call the XML diff had missed** — which is the useful result: it
converts "page 1 is unchanged and the XML shows nothing new, so probably fine" into a
measured statement about all 120 rows.

**2. IROP 70 XML/portal contradiction resolved — 2026-09-19 coverage gap 6 is CLOSED.**
Detailed under checklist source 1. The XML converged to the portal.

**3. The EU Funding & Tenders portal is reachable after all — 2026-09-19 coverage gap 2 is
SUBSTANTIALLY discharged, and the access blocker it named is SOLVED.** The gap said the F&T
topic JSON "must be fetched outside the sandbox because TLS fails through the proxy". That is
half right and the half that is wrong has cost three passes. Measured today:
- Through the sandbox, `https://ec.europa.eu/…` fails with `curl: (60) SSL certificate
  problem: unable to get local issuer certificate` — a **certificate-chain** failure, not a
  network deny. `cinea.ec.europa.eu` and `hadea.ec.europa.eu` are unaffected and return 200
  through the sandbox; only the `ec.europa.eu` host is intercepted.
- **The working path is a headless browser outside the sandbox**, which uses the system trust
  store: `agent-browser open <json-url> --headless` then
  `agent-browser eval "document.body.innerText"`. Verified on eight topic URLs.
  **Next pass: use this, do not re-name the gap as unresolvable.**

What that recovered — the **LIFE-2026 SAP family budgets**, which the 2026-09-19 pass warned
would "be lost to the ledger the same way LIFE-CET was". All are **Open**, all single-stage,
all with deadline **2026-09-22**, all captured as `pages/ft-topic-life-2026-sap-*.json`:

| Call | Topic | Budget 2026 (EUR) |
|---|---|---|
| `LIFE-2026-SAP-NAT` | `LIFE-2026-SAP-NAT-NATURE` (Nature and Biodiversity) | **173,500,000 shared** |
| `LIFE-2026-SAP-NAT` | `LIFE-2026-SAP-NAT-GOV` (Nature Governance and Information) | *(same budget line 114290)* |
| `LIFE-2026-SAP-ENV` | `LIFE-2026-SAP-ENV-ENVIRONMENT` (Circular Economy and Zero Pollution) | 79,000,000 |
| `LIFE-2026-SAP-ENV` | `LIFE-2026-SAP-ENV-GOV` (Environment governance) | 6,500,000 |
| `LIFE-2026-SAP-CLIMA` | `LIFE-2026-SAP-CLIMA-CCM` (Climate Change Mitigation) | 28,000,000 |
| `LIFE-2026-SAP-CLIMA` | `LIFE-2026-SAP-CLIMA-CCA` (Climate Change Adaptation) | 28,000,000 |
| `LIFE-2026-SAP-CLIMA` | `LIFE-2026-SAP-CLIMA-GOV` (Climate Governance and Information) | 4,000,000 |

**Read the NAT line carefully.** `budgetTopicActionMap` key `114290` lists BOTH NAT topics
under ONE `budgetYearMap` of 173,500,000. That is one shared envelope for the two topics, not
173.5 M each. ENV and CLIMA topics sit on separate budget ids and their figures add up.
Family total: **319,000,000 EUR** across the three SAP calls.
`LIFE-2026-TA-PP` returned **HTTP 404** under that identifier — the TA/PLP identifiers were
not resolved, and are named as still owed below.

**Why no LIFE record was staged despite having the money.** Three reasons, in order:
(a) this is a weekly delta and the LIFE family is not new — it was open on 2026-09-18 and the
XML/portal delta since 2026-09-19 is empty; (b) the brief for this pass is staging only and
says not to manufacture records, and minting a seven-topic family the evening before it closes
is exactly that; (c) the closing date is not a deadline on this register's urgency ladder, so
"it closes tomorrow" is not an argument for writing a record today. The budgets, the deadline
and the receipts are now **on disk and in this manifest**, so the next broad pass can mint from
evidence rather than from a rediscovered blocker. The **access method** was the debt worth
clearing, and it is cleared.

### Errata candidates (for the coordinator; this pass did not write `data/errata.jsonl`)

- **None.** No ledger record's source facts changed between 2026-09-19 and 2026-09-21. The
  only XML change, `06_22_070`, touches no record; the only portal changes are a statistics
  box, a dashboard percentage, a programme card and an evaluation calendar.
- **Not an erratum, a manifest correction.** The 2026-09-19 manifest records the IROP call-70
  page as `https://irop.gov.cz/cs/vyzvy/70vyzvairop`. That path returns **404** today. Anyone
  re-fetching it should use `https://irop.gov.cz/cs/Vyzvy-2021-2027/Vyzvy/70vyzvaIROP`.

### Coverage gaps (named, not silent)

1. **EU topic conditions are still partly owed**, carried and narrowed from 2026-09-19 gap 2.
   The access blocker is solved (see above); what is still unread is:
   - **funding rates / support intensities** for `HORIZON-CL5-2026-11`, `SMP-FOOD` and the
     LIFE SAP family. These are **not in the topic JSON** — the JSON's `conditions` field
     points at "section 10 of the call document", a PDF. Reading those PDFs is a broad-pass
     job, not a delta job. The two affected ledger records
     (`dotace-horizon-cl5-2026-11-energy`, `dotace-smp-food-2026-food-waste-prevention`)
     already carry their allocations and already say in `notes` that the rate was not read, so
     nothing in the ledger is wrong — only thin.
   - the **CEF-DIG** cable-repair budget;
   - `HORIZON-CID-2026-01`, `HORIZON-MISS-2026-02-CANCER`, `HORIZON-CL4-2026-03` — none of
     these is in the ledger;
   - the **LIFE-2026 TA and PLP** identifiers, which `life-2026-ta-pp` does not resolve (404).
2. **The open-call backlog is still owed** (2026-09-18 "Beyond the floor", minus IROP 56/57
   which 2026-09-19 discharged). Every item below was re-checked against today's XML and is
   **unchanged in state, date and allocation** since 2026-09-19:
   - IROP: `06_22_010`, `06_23_097/098`, `06_23_106/107/108`, `06_22_067`;
   - OPD `04_25_038`;
   - OP Z+ `03_24_062`, `03_24_059` (*Otevřená*, closes 2026-09-30, 171,959,000 CZK) and
     `03_22_012`;
   - OP ST `10_25_095`, `10_25_089` (*Otevřená*, closes 2026-09-30, 166,666,666.67 CZK) and
     `10_26_110`;
   - OP AMIF `12_26_046` (*Otevřená*, **closes 2026-09-23**, 100,000,000 CZK);
   - OP NSHV `14_26_018` (*Otevřená*, closes 2026-09-30, 290,000,000 CZK) and `14_26_019`.
   Four of these close within nine days. The next broad pass either mints them or states why
   not — and, per the urgency rule, "it closed" is not by itself a reason it should not have
   been recorded.
3. **OPŽP 107 is not yet declared.** *Rozpracovaná* in the XML, *Plánovaná* on the portal,
   accessible from 2026-09-30, close 2026-11-25, allocation 125,000,000 CZK. The next pass
   after 30 September confirms the declaration and reads the call text.
4. **OPJAK `02_25_044`, `02_25_045`, `02_26_046`** remain *Plánovaná* in the XML and
   unpublished as calls on opjak.cz. Allocations 500 M, 1,900 M and 600 M CZK; indicative
   closes in March 2027.
5. **OPŽP POST API not queried.** `https://opzp.cz/wp-json/opzp/v1/call/html` was not
   re-queried, because the rendered listing it backs is text-identical. Carried from
   2026-09-19 on the same reasoning.
6. **IROP status filters not exercised.** The deep walk covered the default listing in full
   (all 120 rows, gap 1 of 2026-09-19 closed), but the Planned/Announced/Declared filters were
   not driven separately. The XML carries `STAVNAZEV` for every code, so the filters are
   redundant as a discovery surface; naming it so a future pass does not re-open it as a doubt.
7. **CINEA rate limiting.** Two of the five EU listing fetches returned HTTP 429 before
   succeeding on retry. A future pass that walks more CINEA pages should pace itself rather
   than read a 429 body as an empty listing.

### Pass summary (5 lines)

```
feed:              dotace-scan (weekly delta, 2026-09-21; left-hand side = 2026-09-19 snapshot, 817 codes)
checklist sources: 8 of 8 visited — MS2021+ XML (200, 817→817, +0/-0, 1 state change) + IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO, CINEA/HaDEA
records:           0 staged — no new call in the XML and none on the seven portals; the one portal candidate (TAČR FOREST) is already in the ledger
coverage gaps:     7 named — EU topic conditions (narrowed: access SOLVED, LIFE SAP budgets recovered); open-call backlog; OPŽP 107; OPJAK planned; OPŽP POST API; IROP status filters; CINEA 429s
                   3 debts CLEARED — IROP deep listing walked (120 rows, recipe recorded); IROP 70 contradiction resolved (XML converged to portal); ec.europa.eu TLS blocker solved
rotation state:    n/a — category rotation is arb-scan's duty
```


## arb-scan — `evidence_type: funded` — pass of 2026-09-21

Attended pass, worktree `localproblems-weekly-2026-09-21`. Staging only: nothing was appended to
`data/signals/**`, `seen.txt` or `data/register.db`, `normalize.py --complete` was not run, and git
state was not touched. Output is exactly two files plus raw captures:

- `data/raw/2026-09-21/funded/staged.jsonl` — 5 records
- `data/raw/2026-09-21/funded/manifest-funded.md` — this file
- `data/raw/2026-09-21/funded/pages/` — every payload quoted or cited below

**Window.** The previous pass ran 2026-09-19, two days ago. The strict window (rounds announced
2026-09-19, 09-20, 09-21) fell across a weekend and contained **no new round in any of this pass's
four categories**: the tech.eu feed jumps from 2026-09-18 to 2026-09-21 and carries only Metris
Energy (energy) and Unit1 Studio (other); the EU-Startups feed carries the same two. Both are
outside this pass's rotation slice and neither was staged. The records below therefore come from
the **category sweep**, as on 2026-09-18 and 2026-09-19 (which staged rounds dated 2023–2026):
four rounds from the week of 2026-09-14 to 09-18 that the 2026-09-18 pass did not capture, and one
(`ie-octostar`) from 2026-04-06 that no pass has captured at all. Every record states its round
date in `date` and its provenance in `money_note`.

### The checklist source for this feed: THE CATEGORY-ROTATION DUTY

Walked: 1 of 1. All 12 categories are named in the table below.

Rotation state at the start was read from `data/raw/2026-09-19/manifest.md`: every category swept at
2026-09-18 or 2026-09-19, with the next pass to start from the eight at 2026-09-18, thinnest first —
govtech (6), education (9), legal-compliance (11), retail-services (16), energy (18), fintech (21),
health (29), b2b (65). **This pass covered the first four, as instructed, and went no further**: the
four were not thin (each yielded at least one record), and the two-day window gave no reason to
reach into a category that was swept three days ago. Arb-record counts are `source: arb-scan` lines
in `data/signals/funded/*.jsonl` (223 in total) before this pass.

| category | last BROAD sweep before | arb records before | covered this pass | records staged | last swept AFTER |
|---|---|---|---|---|---|
| govtech | 2026-09-18 | 6 | **YES** (owed, thinnest first) | 1 (`ie-octostar`) | 2026-09-21 |
| education | 2026-09-18 | 9 | **YES** (owed) | 1 (`gb-academyai`) | 2026-09-21 |
| legal-compliance | 2026-09-18 | 11 | **YES** (owed) | 2 (`lt-enforceshield`, `it-iusful`) | 2026-09-21 |
| retail-services | 2026-09-18 | 16 | **YES** (owed) | 1 (`pt-deskamigo`) | 2026-09-21 |
| energy | 2026-09-18 | 18 | no (not owed this pass) | 0 | 2026-09-18 |
| fintech | 2026-09-18 | 21 | no (not owed this pass) | 0 | 2026-09-18 |
| health | 2026-09-18 | 29 | no — **still owes Klinik** (carried debt, not chased: no cheap route appeared this pass) | 0 | 2026-09-18 |
| b2b | 2026-09-18 | 65 | no (not owed this pass) | 0 | 2026-09-18 |
| other | 2026-09-19 | 7 | no (swept two days ago) | 0 | 2026-09-19 |
| mobility | 2026-09-19 | 10 | no (swept two days ago) | 0 | 2026-09-19 |
| housing | 2026-09-19 | 13 | no (swept two days ago) | 0 | 2026-09-19 |
| environment | 2026-09-19 | 18 | no (swept two days ago) | 0 | 2026-09-19 |

**The next pass starts from the four still at 2026-09-18, thinnest first: `energy` (18), `fintech` (21),
`health` (29, and it still owes Klinik), `b2b` (65).** After those, the four at 2026-09-19, thinnest
first: `other` (7), `mobility` (10), `housing` (13), `environment` (18). The four swept today go last.

### Sources walked, each named with what it gave

| source | result |
|---|---|
| **tech.eu RSS** `https://tech.eu/feed/` | HTTP 200, 145 KB, 20 items back to 2026-09-16. Saved `pages/listing-tech_eu_feed_`. Nothing dated 2026-09-19 or 09-20 (weekend); the 2026-09-21 items are energy and other. |
| **tech.eu weekly recap** `.../2026/09/21/european-tech-weekly-recap-over-eur17b-invested-across-70-deals/` | HTTP 200, 102 KB. **The single most productive source this pass**: 70+ deals for 2026-09-14 to 09-18 with outbound links. Four of five staged records were found here. Saved `pages/techeu-weekly-recap-0921.html`. |
| **tech.eu article pages** | HTTP 200 for every one requested (EnforceShield, AcademyAI, Complir). The 2026-09-19 note that tech.eu category pages 404 holds for `/category/government/` (404) but **not** for tag pages: `https://tech.eu/tag/govtech/` returned 200 and was read. |
| **EU-Startups RSS** `https://www.eu-startups.com/feed/` | HTTP 200, 80 KB, 10 items back to 2026-09-18. Saved `pages/listing-www_eu-startups_com_feed_`. Same weekend gap. |
| **EU-Startups article pages** | HTTP 200 with a desktop user-agent (Octostar article, 504 KB, read in full). **This corrects the 2026-09-19 note**: EU-Startups *article* pages are reachable; it is search and tag pages that are not (below). |
| **Sifted RSS** `https://sifted.eu/feed` | HTTP 200, 24 items back to 2026-09-15. Read; **nothing new this pass** — every item is AI/deeptech funding, VC-ecosystem commentary or opinion, none in govtech, education, legal-compliance or retail-services. Saved `pages/listing-sifted_eu_feed`. |
| **Vestbee** | `sitemap_index.xml` HTTP 200; `https://vestbee.com/__sitemap__/posts.xml` HTTP 200, 1.06 MB. **Nothing new this pass**: the index was generated 2026-09-09 and its newest post is dated 2026-09-09, all of which the 2026-09-19 pass already harvested as `round-*` ids. See COVERAGE GAP 3. |
| **ARES** (`ekonomicke-subjekty/vyhledat`) | HTTP 200 on every query. 14 name searches run; IČO + datumVzniku recorded on every Czech player where a company name resolved. |
| **Own ledgers** | `data/signals/funded/*.jsonl` (6,062 lines) and `data/signals/seen.txt` (18,420 ids) checked per candidate; `data/lookup/cz-contract-parties.jsonl` checked by name and by IČO. |
| **Category-targeted Czech and English web search** | 10 searches run (4 English category sweeps, 6 Czech absence checks). Every Czech query string is recorded verbatim in the record's `notes`. |

### COVERAGE GAPS (named, with what a future pass owes them)

1. **EU-Startups weekly funding round-up is paywalled — unchanged from 2026-09-19.**
   `https://www.eu-startups.com/2026/09/weekly-funding-round-up-...-sept-14-sept-18/` returns HTTP 200
   and 512 KB, but the body is replaced by *"This article is visible for CLUB members only."* Saved as
   `pages/eustartups-roundup-0918.html` so the block is on the record. **Owed:** either a CLUB session,
   or accept the tech.eu weekly recap as the standing substitute — it covered the same week fully this
   pass and is not paywalled.
2. **EU-Startups search and tag pages return 403.** `?s=<term>` (six attempts) and `/tag/govtech/` all
   403 with a desktop UA; saved as `pages/search-eustartups-*.html`. **Owed:** reach EU-Startups
   articles through the tech.eu recap's outbound links (what this pass did) or through web search,
   never through its own site search.
3. **Vestbee's post sitemap is stale.** It resolves, but was generated 2026-09-09 and lists nothing
   newer, so Vestbee contributed zero candidates in a window it should have covered. Vestbee *category*
   pages (404 on 2026-09-19) were **not retried** this pass — the sitemap route was used instead.
   **Owed:** a check of whether the sitemap regenerates, and a retry of the category pages.
4. **brutkasten.com returns 403.** This blocked the one Austrian legal-compliance candidate in the
   week's deals: **signteq** (Vienna, seven-figure round, regtech building a "Know Your Agent"
   verification layer for AI agents, investors incl. Peter Steinberger). Saved `pages/cand-signteq.html`
   (the 403 body). Not staged: neither the amount nor the date could be receipted, and MATCH §3 forbids
   inventing either. **Owed:** another route to this round (trendingtopics.eu, derbrutkasten mirror, or
   the company's own release).
5. **ey.com is unreachable by curl** (exit 000, no bytes). The AI Act dates used by `gb-academyai` and
   `ie-octostar` were instead receipted from epravo.cz ID 120133 (saved `pages/cz-epravo-ai-gramotnost.html`),
   which states them directly. No claim rests on the EY page.
6. **policie.gov.cz redirects to archiv.policie.gov.cz**, which failed on the first attempt and
   succeeded on retry (HTTP 200, saved `pages/cz-policie-analyticke-nastroje.html`). Noted so a future
   pass does not read a single 000 as "the police publish nothing".
7. **RSS depth is ~3 days, as on 2026-09-18 and 09-19.** Neither the EU-Startups (10 items) nor the
   tech.eu (20 items) feed reaches past 2026-09-16. Wayback was **not** attempted this pass (429 on
   2026-09-19); the weekly recap made it unnecessary. **Owed:** nothing, as long as the recap holds.

### Dedup suppressions — candidates found, NOT staged because the company is already in the ledger

Both are enrichment candidates, not duplicates to create.

- **Complir** (Copenhagen, $11M seed announced 2026-09-16, General Catalyst; AI product-compliance for
  retailers and brands — regulatory mapping per SKU, documentation generation). Already in
  `data/signals/funded/2026-08-13.jsonl` as **`yc-complir`** — *"Complir — Vanta for physical products"*,
  YC Spring 2026, sector `retail-services`, a one-line summary and **no CZ check**. Article saved as
  `pages/cand-complir.html`. **Owed:** `yc-complir` deserves the newer round, a `legal-compliance`
  re-read, and a CZ absence check; it should not get a second record.
- **Avendar** (Eindhoven, €2.2M seed, LUMO Labs + Brabant Development Agency; AI investigation platform,
  deployed by the Dutch National Police and the Municipality of Amsterdam). Already in
  `data/signals/funded/2026-08-14.jsonl` as **`round-avendar`** (2026-04-27, `govtech`, notes: one line,
  no CZ check). Article saved as `pages/cand-avendar-aiinsider.html`. **Owed:** nothing new to harvest —
  but the full Czech absence check for that exact space (LikPik, JAN, Profinit, DATASYS, register
  link-analysis) was done this pass and is written out on `ie-octostar`, and applies to `round-avendar`
  unchanged.

### Candidates examined and rejected (so the selection is not silent)

- **Sportano** (PL, €15M EBRD minority, 2026-09-14) — an online sports retailer taking growth capital to
  expand across Europe. It is a retailer's balance sheet, not a transferable product model, and Czech
  sports e-commerce is a mature, owned market. Saved `pages/cand-sportano.html`.
- **retoflow** (DE, seven-figure from BMH/HessenFonds, 2026-09-16) — reads as retail from the name; it is
  a Fraunhofer spin-off selling a computable digital twin of power, gas and heat networks to grid
  operators. That is `energy`, which this pass does not own.
- **Scalera** (CH, $6.5M / €5.7M seed, 2025-05) — AI for public construction procurement. The buyer is
  the bidding contractor, not the state, so it is `b2b` rather than `govtech`, and the space is already
  held by `round-cato` and `round-cato-ai` in the ledger.
- **Fever** (ES, $250M) — consumer events marketplace; `other`, not this pass's slice, and Czech events
  discovery is held by an established local player.

### Records — 5 staged in `data/raw/2026-09-21/funded/staged.jsonl`

Verdict vocabulary is unchanged from 2026-09-18 and 2026-09-19: **absent** = no Czech player found
selling this, with the queries recorded and a passing positive control; **contested** = direct players
exist but none is established, or only part of the job is held; **taken** = a direct, ESTABLISHED
Czech player sells this.

| id | category | what | money | maturity abroad | CZ verdict |
|---|---|---|---|---|---|
| `lt-enforceshield` | legal-compliance | finds counterfeit listings, clone storefronts, impersonation and phishing pages for a brand, then runs the takedowns itself; lawyers review outcomes rather than routine cases | €1.7M seed (2026-09-15) | early (founded 2024; traction limb met — 20+ enterprise customers, 33,500+ removals/month) | **absent** — Patentoid s.r.o. (IČO 04821645) and Hlídač ochranných známek do registry *watching*; SGS Czech Republic s.r.o. (IČO 48589241) sells brand protection as an inspection service; ČOI protects the consumer; IP law firms bill per case. Nobody sells detection-to-takedown. |
| `it-iusful` | legal-compliance | a subscribed, AI-assisted legal partner for SMEs instead of a lawyer called once it is too late | €2M pre-seed (2026-09-16) | early (pre-seed, no customer count) | **taken** — Dostupný advokát s.r.o. (IČO 09788336, since 2021-01-01) sells exactly this and publishes "150+ nových zákazníků každý měsíc"; Advokát Beneš sells the monthly paušál from 6 600 Kč/měsíc. Comparison point only. |
| `gb-academyai` | education | measures whether employees can actually use AI on a six-axis framework, then trains the gaps in five-minute role-specific modules, with manager dashboards | £1.65M pre-seed ≈ €1.92M (2026-09-15) | early (pre-seed) | **contested** — the training half is taken (TAYLLORCOX s.r.o. IČO 27902587, Skřivánek, Digitrix, coalbrain, ai-profirmy, PwC ČR); no Czech vendor found selling the *measurement* layer. |
| `ie-octostar` | govtech | air-gapped investigation platform — link analysis, communications and document intelligence, GenAI agents — for police, judiciary and financial-crime teams | €6.1M total after a seed extension (2026-04-06) | early on the test (founded 2023) but with 3 EU national law-enforcement/judicial deployments in Q1 2026 and BAE Systems work | **contested** — LikPik (Masaryk University ICS, with Policie ČR since autumn 2023) is direct but has no seller; the police president announced **JAN**, an in-house unified analytical tool; Profinit EU (IČO 04434081) and DATASYS (IČO 61249157) are adjacent integrators. The opponent is the buyer's own programme. |
| `pt-deskamigo` | retail-services | marketplace listing cafés', hotels' and gyms' idle daytime space as workspace booked by the half or full day, priced by the venue | €350k pre-seed (2026-09-15) | early (pre-seed, Portugal only) | **absent** for the aggregator — Kavárna 6,33 in Prague 8 already sells a seat at 100 Kč/hod and a day at 633 Kč, one venue at a time; WorkLounge s.r.o. (IČO 05204984) and Spaces sell memberships in their own space; WHATSPOT s.r.o. (IČO 17855047) is desk-booking software for an employer's own rooms. No Czech marketplace pools third-party capacity. |

**Mechanical checks run before writing, all passing:** every `quote` is a literal substring of the saved
payload after whitespace collapse and ≤300 chars; every `id` prefix is the lowercase ISO2 of its
`geo_origin`; no `id` appears in `seen.txt` or in any `data/signals/funded/*.jsonl`; every score is an
integer 0–3; `scores.money` matches the arithmetic ladder against `money_eur`; no record is dropped by
the materiality filter (`money <= 1 AND scale <= 1 AND urgency == 0`); every key is one `SignalSchema`
already declares.

**Positive control (MATCH §4), run 2026-09-21 by this pass, recorded on all five records, two limbs:**
(a) ARES name search `Wultra` → Wultra s.r.o., IČO 03643174, datumVzniku 2014-12-15 — the ARES method
surfaces a known small Czech software vendor. (b) The descriptive Czech query *"právní podpora pro firmy
předplatné advokát online paušál pro malé a střední podniky"* surfaced Dostupný advokát s.r.o. (IČO
09788336) and advokatbenes.cz's právní paušál priced from 6 600 Kč/měsíc — the Czech-language descriptive
method does surface real Czech vendors where they exist. **PASSED.** The `ie-octostar` check carries a
third, in-domain confirmation: the same method surfaced LikPik and JAN, two Czech positives, in the very
category where a naive English query returns nothing Czech at all.

### New problem candidates for the register

1. **Czech brands and e-shops fight cloned storefronts and fake listings by hand.** The strongest of the
   three. There is a named institution on the record: MPO warned in 2026 that links to fraudulent e-shops
   copying the sites of well-known Czech retailers were circulating, and Alza publishes its own account of
   pursuing a copycat shop by commissioning an expert report documenting 33 identically described products.
   The Czech supply side is registry watching (Patentoid, Hlídač ochranných známek), a global inspection
   group's service (SGS), and law firms billing per case — nothing that detects and takes down at volume.
   Gap check done and recorded on `lt-enforceshield`; what it still lacks for a record is a **price
   receipt** — what a Czech brand actually pays today to have one clone shop removed.
2. **A priced hole in hourly workspace.** `pt-deskamigo`'s check found a Czech venue selling exactly this
   at 100 Kč/hod and 633 Kč/day, and no aggregator. Smaller, and the pain is a convenience rather than a
   loss, so it would need a sourced loss before it could carry a headline (MATCH §9, rule 1).
3. **AI-literacy duty with no measurement.** AI Act čl. 4 binds Czech employers since 2025-02-02, with the
   sanctions and supervisory-authority provisions since 2025-08-02 and the remaining provisions since
   2026-08-02 (epravo.cz ID 120133). Recorded against our own case on `gb-academyai`: the same analysis
   states the AI Act does **not** require measuring the level of knowledge, so a record built on this would
   be selling a recommended practice, not a duty — which is exactly the kind of overreach MATCH §9 warns
   about. Flagged, not recommended.

### PASS SUMMARY

```
feed:               arb-scan (evidence_type funded), attended, 2026-09-21
checklist sources:  1 of 1 walked (THE CATEGORY-ROTATION DUTY); 12 of 12 categories named;
                    4 of 4 owed categories swept; 6 funding listings visited, each named above
records staged:     5 (data/raw/2026-09-21/funded/staged.jsonl) — 2 legal-compliance,
                    1 education, 1 govtech, 1 retail-services; 2 further candidates
                    suppressed as already in the ledger (yc-complir, round-avendar)
coverage gaps:      7 named — EU-Startups round-up paywalled (unchanged); EU-Startups search
                    and tag pages 403; Vestbee sitemap stale at 2026-09-09 and its category
                    pages not retried; brutkasten 403 (costs us the signteq round); ey.com
                    unreachable; policie.gov.cz needed a retry; RSS depth still ~3 days
rotation state:     govtech, education, legal-compliance, retail-services now swept 2026-09-21;
                    energy, fintech, health (still owes Klinik) and b2b remain at 2026-09-18 and
                    are next, thinnest first; other, mobility, housing, environment at 2026-09-19
```

