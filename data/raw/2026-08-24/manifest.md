# run manifest — 2026-08-24

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-08-24`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-08-24T2148 | ted | ok | 200 | 22889710 | 2654 | 20994 | 2026-08-24T21:48:59Z | data/raw/2026-08-24 |  |
| 2026-08-24T2148 | hlidac | error | 000 | 0 | 0 | 0 | 2026-08-24T21:49:31Z |  | auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| 2026-08-24T2148 | cc-cz | ok | 200 | 18119 |  | 3142 | 2026-08-24T21:49:32Z | data/raw/2026-08-24/feed-czechcrunch.xml |  |
| 2026-08-24T2148 | yc-oss | ok | 200 | 10406318 |  | 5829 | 2026-08-24T21:49:35Z | data/raw/2026-08-24/yc-all.json |  |
| 2026-08-24T2148 | vestbee | ok | 200 | 1049871 | 50 | 6763 | 2026-08-24T21:49:41Z | data/raw/2026-08-24 |  |
| 2026-08-24T2148 | suggest | ok | 200 | 11883 | 42 | 50602 | 2026-08-24T21:50:58Z | data/raw/2026-08-24/suggest-pain.jsonl |  |
| 2026-08-24T2148 | reddit-new | ok | 200 | 200817 | 100 | 1525 | 2026-08-24T21:55:32Z | data/raw/2026-08-24 |  |
| 2026-08-24T2148 | reddit-search | ok | 200 | 332854 | 100 | 1775 | 2026-08-24T21:55:32Z | data/raw/2026-08-24 |  |
| 2026-08-24T2148 | nku | ok | 200 | 76693 | 122 | 4002 | 2026-08-24T21:56:06Z | data/raw/2026-08-24 |  |
| 2026-08-24T2148 | sukl | skipped | 000 | 0 | 0 | 0 | 2026-08-24T21:56:10Z |  | registry status=planned |
| 2026-08-24T2148 | ec-hys | error | 000 | 0 | 0 | 2216 | 2026-08-24T21:56:10Z | data/raw/2026-08-24 | no records: page0:HTTP-000 |
| 2026-08-24T2148 | nen | skipped | 000 | 0 | 0 | 0 | 2026-08-24T21:56:12Z |  | registry status=planned |
| 2026-08-24T2148 | mpsv | ok | 200 | 19433907 | 18 | 37227 | 2026-08-24T21:56:13Z | data/raw/2026-08-24/mpsv-hiring-2026-07.json | coverage: 27 of 31 days (4 absent); 46716 rows -> 6597 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| 2026-08-24T2148 | coi | skipped | 000 | 0 | 0 | 0 | 2026-08-24T21:56:53Z |  | registry status=planned |
| 2026-08-24T2148 | smlouvy | skipped | 000 | 0 | 0 | 0 | 2026-08-24T21:56:53Z |  | registry status=planned |

---

# Ingest run 2026-08-24T2356
Run date: 2026-08-24  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 18119 | 10 | 10 | — | structured | yes |  |
| `ec-hys` | — | 0 | 0 | 0 | — | none | **NO** | transport: no records: page0:HTTP-000 |
| `hlidac` | — | 0 | 0 | 0 | — | none | **NO** | transport: auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| `mpsv` | 200 | 19433907 | 18 | 18 | — | structured | yes | coverage: 27 of 31 days (4 absent); 46716 rows -> 6597 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| `nku` | 200 | 76693 | 122 | 122 | — | structured | yes |  |
| `reddit-new` | 200 | 200817 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 332854 | 100 | 98 | — | structured | yes |  |
| `suggest` | 200 | 11883 | 42 | 27 | — | structured | yes |  |
| `ted` | 200 | 22889710 | 2654 | 293 | above-range | structured | yes |  |
| `vestbee` | 200 | 1049871 | 50 | 43 | — | structured | yes |  |
| `yc-oss` | 200 | 10406318 | 6191 | 1419 | — | structured | yes |  |

**2 feed(s) failed their contract this run.** A contract violation is a first-class error: a 200 carrying the wrong body is a lie, where a 500 is honest.

## Staged records — PENDING, not appended

2098 records carry their mechanical fields and are waiting on a model. 7157 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 2098 |
| `scores.recurrence` | 2098 |
| `geo_origin` | 2098 |
| `sector` | 1787 |
| `title` | 681 |
| `summary` | 681 |
| `pain` | 225 |
| `scores.urgency` | 27 |

**Transport status UNKNOWN for 2 feed(s):** `ec-hys`, `hlidac`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 2098 staged record(s) passed the field allowlist and the email/phone content scan.

## Dedup by identity key — same resource, different id

**32 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

| staged id | already in the ledger as | key | feed | url |
|---|---|---|---|---|
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
| `nku-k25017` | `nku-dia-ucetnictvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25017.pdf |
| `nku-k24024` | `nku-uspory-energie` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24024.pdf |
| `nku-k25012` | `nku-letecka-sluzba` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25012.pdf |
| `nku-k25011` | `nku-cista-mobilita` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25011.pdf |
| `nku-k25005` | `nku-etcs` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25005.pdf |
| `nku-k25008` | `nku-srazkove-vody` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25008.pdf |
| `nku-k25007` | `nku-react-eu-nemocnice` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25007.pdf |
| `nku-k25009` | `nku-vrt` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25009.pdf |
| `nku-k25004` | `nku-mistni-komunikace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25004.pdf |
| `nku-k25006` | `nku-protipovodnova-ochrana` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25006.pdf |
| `nku-k24028` | `nku-statni-sluzba` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24028.pdf |
| `nku-k25002` | `nku-rizeni-skolstvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25002.pdf |
| `nku-k24031` | `nku-justicni-pohledavky` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24031.pdf |
| `nku-k24030` | `nku-doprava2020` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24030.pdf |
| `nku-k24026` | `nku-viza-it` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24026.pdf |
| `yc-d-model` | `yc-d_model` | `url` | `yc-oss` | https://www.ycombinator.com/companies/d_model |
| `yc-galactic-resource-utilization-space-inc-gru-spac` | `yc-galactic-resource-utilization-space-inc-gru-space` | `url` | `yc-oss` | https://www.ycombinator.com/companies/galactic-resource-utilization-space-inc-gru-space |

**1 key(s) were EXEMPTED from dedup**, because a key naming more than one record is a listing page, a dataset landing page or a roundup — not an identity. Merging on one would delete distinct records. Measured over the committed corpus: 67 urls are shared by 571 records (6.1%), one Vestbee roundup being the url of 32 funding rounds.

| key | why it was not used |
|---|---|
| `url:vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-july-2026` | carried by 10 ledger records — a listing or dataset page, not an identity |
| 2026-08-24T2157 | ted | ok | 200 | 1246756 | 141 | 4249 | 2026-08-24T21:57:46Z | data/raw/2026-08-24 |  |
| 2026-08-24T2158 | hlidac | ok | 200 | 965647 | 426 | 11055 | 2026-08-24T21:58:08Z | data/raw/2026-08-24 | coverage: 426 of 860 available (page cap HLIDAC_PAGES=4 x 25) |
| 2026-08-24T2158 | ec-hys | ok | 200 | 170419 | 44 | 6933 | 2026-08-24T21:59:27Z | data/raw/2026-08-24 |  |

---

# Ingest run 2026-08-25T0000
Run date: 2026-08-25  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 18119 | 10 | 10 | — | structured | yes |  |
| `ec-hys` | 200 | 170419 | 44 | 44 | — | structured | yes |  |
| `hlidac` | 200 | 965647 | 426 | 422 | — | structured | yes | coverage: 426 of 860 available (page cap HLIDAC_PAGES=4 x 25) |
| `mpsv` | 200 | 19433907 | 18 | 18 | — | structured | yes | coverage: 27 of 31 days (4 absent); 46716 rows -> 6597 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| `nku` | 200 | 76693 | 122 | 122 | — | structured | yes |  |
| `reddit-new` | 200 | 200817 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 332854 | 100 | 98 | — | structured | yes |  |
| `suggest` | 200 | 11883 | 42 | 27 | — | structured | yes |  |
| `ted` | 200 | 1246756 | 2753 | 385 | above-range | structured | yes |  |
| `vestbee` | 200 | 1049871 | 50 | 43 | — | structured | yes |  |
| `yc-oss` | 200 | 10406318 | 6191 | 1419 | — | structured | yes |  |

## Staged records — PENDING, not appended

2565 records carry their mechanical fields and are waiting on a model. 7168 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 2565 |
| `scores.recurrence` | 2565 |
| `geo_origin` | 2565 |
| `sector` | 2162 |
| `title` | 1148 |
| `summary` | 1148 |
| `pain` | 225 |
| `scores.urgency` | 65 |

## AC-GDPR1 — contact-field gate

No personal data detected. 2565 staged record(s) passed the field allowlist and the email/phone content scan.

## Dedup by identity key — same resource, different id

**123 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

| staged id | already in the ledger as | key | feed | url |
|---|---|---|---|---|
| `echys-14165` | `consult-grid-connection-code` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14165 |
| `echys-14628` | `consult-cloud-ai-act` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14628 |
| `echys-14638` | `consult-europol-mandate` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14638 |
| `echys-14709` | `consult-digital-networks-act` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14709 |
| `echys-14842` | `consult-chips-act-2` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14842 |
| `echys-14858` | `consult-battery-recycled-content` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14858 |
| `echys-15252` | `consult-territorial-supply-constraints` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15252 |
| `echys-15352` | `consult-packaging-epr-register` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15352 |
| `echys-16413` | `consult-horizon-partnerships` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16413 |
| `echys-16612` | `consult-learning-accounts-eval` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16612 |
| `echys-16795` | `consult-banking-competitiveness` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16795 |
| `echys-17172` | `consult-dual-use-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17172 |
| `echys-17912` | `consult-mica-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17912 |
| `echys-18194` | `consult-victims-rights-strategy` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18194 |
| `echys-18575` | `consult-employer-sanctions-eval` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18575 |
| `echys-18592` | `consult-ai-cultural-strategy` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18592 |
| `echys-18658` | `consult-housing-simplification` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18658 |
| `echys-18804` | `consult-wrc27-spectrum` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18804 |
| `echys-18872` | `consult-teachers-agenda` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18872 |
| `echys-18874` | `consult-school-basic-skills` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18874 |
| `hlidac-36096850` | `hlidac-38419110` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38419110 |
| `hlidac-36265728` | `hlidac-38594060` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38594060 |
| `hlidac-36441548` | `hlidac-38776744` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38776744 |
| `hlidac-36097122` | `hlidac-38419070` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38419070 |
| `hlidac-36172618` | `hlidac-38497426` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38497426 |
| `hlidac-36224920` | `hlidac-38551596` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38551596 |
| `hlidac-36264636` | `hlidac-38592936` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38592936 |
| `hlidac-36326552` | `hlidac-38657096` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38657096 |
| `hlidac-36169534` | `hlidac-38495494` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38495494 |
| `hlidac-36612490` | `hlidac-38954950` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38954950 |
| `hlidac-36108178` | `hlidac-38430694` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38430694 |
| `hlidac-36477690` | `hlidac-38814774` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38814774 |
| `hlidac-36514870` | `hlidac-38853502` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38853502 |
| `hlidac-36340312` | `hlidac-38671796` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38671796 |
| `hlidac-36530714` | `hlidac-38869946` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38869946 |
| `hlidac-36144270` | `hlidac-38467958` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38467958 |
| `hlidac-36172546` | `hlidac-38497354` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38497354 |
| `hlidac-36144266` | `hlidac-38467954` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38467954 |
| `hlidac-36620726` | `hlidac-38963422` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38963422 |
| `hlidac-36559502` | `hlidac-38899662` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38899662 |
| `hlidac-36612334` | `hlidac-38954798` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38954798 |
| `hlidac-36468764` | `hlidac-38805532` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38805532 |
| `hlidac-36142810` | `hlidac-38638676` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38638676 |
| `hlidac-36082938` | `hlidac-38404378` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38404378 |
| `hlidac-36336196` | `hlidac-38667544` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38667544 |
| `hlidac-36426100` | `hlidac-38760740` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38760740 |
| `hlidac-36153734` | `hlidac-38477810` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38477810 |
| `hlidac-36270796` | `hlidac-38599264` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38599264 |
| `hlidac-36141362` | `hlidac-38464906` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38464906 |
| `hlidac-36057798` | `hlidac-38378150` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38378150 |
| `hlidac-36086738` | `hlidac-38408294` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38408294 |
| `hlidac-36459536` | `hlidac-38795752` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38795752 |
| `hlidac-36736318` | `hlidac-39084314` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/39084314 |
| `hlidac-36727094` | `hlidac-39074938` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/39074938 |
| `hlidac-36160278` | `hlidac-38911766` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38911766 |
| `hlidac-36390424` | `hlidac-38723900` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38723900 |
| `hlidac-36316388` | `hlidac-38646756` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38646756 |
| `hlidac-36715870` | `hlidac-39063098` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/39063098 |
| `hlidac-36066522` | `hlidac-38387118` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38387118 |
| `hlidac-36066198` | `hlidac-38386786` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38386786 |
| `hlidac-36275028` | `hlidac-38603732` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38603732 |
| `hlidac-36115394` | `hlidac-38438158` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38438158 |
| `hlidac-36216084` | `hlidac-38542688` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38542688 |
| `hlidac-36486898` | `hlidac-38824338` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38824338 |
| `hlidac-36389864` | `hlidac-38723296` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38723296 |
| `hlidac-36438780` | `hlidac-38773860` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38773860 |
| `hlidac-36087018` | `hlidac-38408582` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38408582 |
| `hlidac-36463396` | `hlidac-38799792` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38799792 |
| `hlidac-36048274` | `hlidac-38368207` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38368207 |
| `hlidac-36422840` | `hlidac-38757328` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38757328 |
| `hlidac-36163462` | `hlidac-38488022` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38488022 |
| `hlidac-36454312` | `hlidac-38790216` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38790216 |
| `hlidac-36422812` | `hlidac-38757296` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38757296 |
| `hlidac-36505278` | `hlidac-38843522` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38843522 |
| `hlidac-36192774` | `hlidac-38518470` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38518470 |
| `hlidac-36275896` | `hlidac-38604660` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38604660 |
| `hlidac-36215268` | `hlidac-38541844` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38541844 |
| `hlidac-36300444` | `hlidac-38630268` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38630268 |
| `hlidac-36179994` | `hlidac-38505094` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38505094 |
| `hlidac-36454600` | `hlidac-38790512` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38790512 |
| `hlidac-36436576` | `hlidac-38771560` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38771560 |
| `hlidac-36695342` | `hlidac-39041762` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/39041762 |
| `hlidac-36695186` | `hlidac-39041590` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/39041590 |
| `hlidac-36289108` | `hlidac-38618416` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38618416 |
| `hlidac-36693166` | `hlidac-39039418` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/39039418 |
| `hlidac-36423748` | `hlidac-38758272` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38758272 |
| `hlidac-36535138` | `hlidac-38874606` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38874606 |
| `hlidac-36148962` | `hlidac-38472826` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38472826 |
| `hlidac-36171406` | `hlidac-38496174` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38496174 |
| `hlidac-36542462` | `hlidac-38882130` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38882130 |
| `hlidac-36523562` | `hlidac-38862574` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38862574 |
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
| `nku-k25017` | `nku-dia-ucetnictvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25017.pdf |
| `nku-k24024` | `nku-uspory-energie` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24024.pdf |
| `nku-k25012` | `nku-letecka-sluzba` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25012.pdf |
| `nku-k25011` | `nku-cista-mobilita` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25011.pdf |
| `nku-k25005` | `nku-etcs` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25005.pdf |
| `nku-k25008` | `nku-srazkove-vody` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25008.pdf |
| `nku-k25007` | `nku-react-eu-nemocnice` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25007.pdf |
| `nku-k25009` | `nku-vrt` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25009.pdf |
| `nku-k25004` | `nku-mistni-komunikace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25004.pdf |
| `nku-k25006` | `nku-protipovodnova-ochrana` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25006.pdf |
| `nku-k24028` | `nku-statni-sluzba` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24028.pdf |
| `nku-k25002` | `nku-rizeni-skolstvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25002.pdf |
| `nku-k24031` | `nku-justicni-pohledavky` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24031.pdf |
| `nku-k24030` | `nku-doprava2020` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24030.pdf |
| `nku-k24026` | `nku-viza-it` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24026.pdf |
| `yc-d-model` | `yc-d_model` | `url` | `yc-oss` | https://www.ycombinator.com/companies/d_model |
| `yc-galactic-resource-utilization-space-inc-gru-spac` | `yc-galactic-resource-utilization-space-inc-gru-space` | `url` | `yc-oss` | https://www.ycombinator.com/companies/galactic-resource-utilization-space-inc-gru-space |

**1 key(s) were EXEMPTED from dedup**, because a key naming more than one record is a listing page, a dataset landing page or a roundup — not an identity. Merging on one would delete distinct records. Measured over the committed corpus: 67 urls are shared by 571 records (6.1%), one Vestbee roundup being the url of 32 funding rounds.

| key | why it was not used |
|---|---|
| `url:vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-july-2026` | carried by 10 ledger records — a listing or dataset page, not an identity |

## Attended scan harvest — elder-care sector (session 2026-08-24/25)

Six records minted by the attended session (extraction: manual), appended
directly to the ledgers alongside this run's completion; every URL checked
HTTP 200 at harvest time; every `quote` verified as a verbatim substring
(whitespace-collapsed) of a fetched copy of the cited page or document —
recorded here because agent-harvest quotes degrade to a manifest warning
rather than a hard refusal:

| ledger | id | source | quote verified against |
|---|---|---|---|
| demand | civic-mpsv-ltc-predikce-2035 | demand-scan | mpsv.gov.cz predikce press page |
| demand | civic-mpsv-rocenka-neuspokojene-2024 | demand-scan | rocenka 2024 workbook 5_Socialni sluzby.xlsx, tab 5.9 header |
| regulation | reg-soc-sluzby-92-2026 | reg-scan | nrzp.cz information 46-2026 (act text summary) |
| regulation | reg-prispevek-na-peci-2026 | reg-scan | mpsv.gov.cz legislative-changes overview (30.12.2025) |
| regulation | reg-soc-sluzby-novy-zakon-2031 | reg-scan | nrzp.cz information 13-2026 |
| tenders | dotace-npo-31-24-138-pobytove-sluzby | dotace | Vyzva 31_24_138 PDF, verze platna od 13.5.2026 |

NEGATIVE RESULT (measured 2026-08-25): MS2021+ open data
SeznamVyzev_21_27.xml (816 entries) carries only ESIF programmes 01-14 —
zero 31_* NPO calls — so call 31_24_138 is receipted from the MPSV call
page and its call PDF, not from the open-data XML.

TED backfill: second `ted` manifest row above is the attended backfill
TED_CPV_GROUPS="health:85*" scripts/fetch_ted.sh 20251101 — 141 notices
since 2025-11-01, incl. 754888-2025 (Brno Kocianka concession) and
244129-2026 (Praha 14 concession), both now in data/signals/tenders/2026-08-24.jsonl.

Model half: 54 pass-A + 8 pass-B subagent batches; 19 hlidac records whose
batch summaries kept failing the 2-sentence validator (Czech "c. N" and
"D. M. YYYY" periods read as sentence breaks) were filled in place by the
attended session per INGEST.md step 2.
