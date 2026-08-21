# run manifest — 2026-08-21

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-08-21`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-08-21T1152 | reddit-new | ok | 200 | 194495 | 100 | 1530 | 2026-08-21T11:52:46Z | data/raw/2026-08-21 |  |
| 2026-08-21T1152 | reddit-search | ok | 200 | 326148 | 100 | 1535 | 2026-08-21T11:52:46Z | data/raw/2026-08-21 |  |
| 2026-08-21T1152 | ec-hys | ok | 200 | 748165 | 45 | 27809 | 2026-08-21T11:52:49Z | data/raw/2026-08-21 |  |
| 2026-08-21T1153 | nku | ok | 200 | 62314 | 52 | 3184 | 2026-08-21T11:53:59Z | data/raw/2026-08-21 |  |
| 2026-08-21T1157 | nku | ok | 200 | 76693 | 122 | 931 | 2026-08-21T11:57:29Z | data/raw/2026-08-21 |  |
| 2026-08-21T1200 | mpsv | ok | 200 | 19433907 | 18 | 23049 | 2026-08-21T12:00:07Z | data/raw/2026-08-21/mpsv-hiring-2026-07.json | coverage: 27 of 31 days (4 absent); 46716 rows -> 6597 novy -> 18 aggregates |
| 2026-08-21T1200 | ares | error | 200 | 38745 | 0 | 2403 | 2026-08-21T12:00:36Z | data/raw/2026-08-21 | AC-GDPR1 REFUSED: contact data survived the ARES allowlist — nothing written |
| 2026-08-21T1201 | ares | ok | 200 | 38745 | 9 | 2246 | 2026-08-21T12:01:16Z | data/raw/2026-08-21/ares-lookups-2026-07.json | resolved 9 of 9 (404 0, bad-checksum 0); named 6 employer record(s) |
| 2026-08-21T1201 | vestbee | ok | 200 | 1046472 | 47 | 794 | 2026-08-21T12:01:36Z | data/raw/2026-08-21 |  |
| 2026-08-21T1204 | mpsv | ok | 200 | 19433907 | 18 | 19602 | 2026-08-21T12:04:50Z | data/raw/2026-08-21/mpsv-hiring-2026-07.json | coverage: 27 of 31 days (4 absent); 46716 rows -> 6597 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| 2026-08-21T1205 | ares | ok | 200 | 35575 | 8 | 2829 | 2026-08-21T12:05:12Z | data/raw/2026-08-21/ares-lookups-2026-07.json | resolved 8 of 8 (404 0, bad-checksum 0); named 6 employer record(s) |
| 2026-08-21T1208 | mpsv | ok | 200 | 19433907 | 18 | 27901 | 2026-08-21T12:08:29Z | data/raw/2026-08-21/mpsv-hiring-2026-07.json | coverage: 27 of 31 days (4 absent); 46716 rows -> 6597 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| 2026-08-21T1208 | ares | ok | 200 | 35575 | 8 | 5028 | 2026-08-21T12:08:59Z | data/raw/2026-08-21/ares-lookups-2026-07.json | resolved 8 of 8 (404 0, bad-checksum 0); named 6 employer record(s) |
| 2026-08-21T1208 | ec-hys | ok | 200 | 169012 | 45 | 6625 | 2026-08-21T12:08:37Z | data/raw/2026-08-21 |  |
| 2026-08-21T1210 | vestbee | skipped | 304 | 0 | 0 | 528 | 2026-08-21T12:10:19Z | data/raw/2026-08-21 | 304 Not Modified (If-None-Match) |
| 2026-08-21T1210 | vestbee | ok | 200 | 1046472 | 47 | 694 | 2026-08-21T12:10:33Z | data/raw/2026-08-21 |  |
| 2026-08-21T1212 | mpsv | ok | 200 | 19433907 | 18 | 24455 | 2026-08-21T12:12:26Z | data/raw/2026-08-21/mpsv-hiring-2026-07.json | coverage: 27 of 31 days (4 absent); 46716 rows -> 6597 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| 2026-08-21T1212 | ares | ok | 200 | 35575 | 8 | 4169 | 2026-08-21T12:12:53Z | data/raw/2026-08-21/ares-lookups-2026-07.json | resolved 8 of 8 (404 0, bad-checksum 0); named 6 employer record(s) |
| 2026-08-21T1232 | shoptet | ok | 200 | 126274 | 4 | 3422 | 2026-08-21T12:32:33Z | data/raw/2026-08-21 |  |
| 2026-08-21T1234 | shoptet | ok | 200 | 126274 | 404 | 1682 | 2026-08-21T12:34:12Z | data/raw/2026-08-21 |  |
| 2026-08-21T1247 | upgates | ok | 200 | 102039 | 221 | 4199 | 2026-08-21T12:47:31Z | data/raw/2026-08-21 |  |
| 2026-08-21T1303 | shoptet | ok | 200 | 126274 | 28 | 3985 | 2026-08-21T13:03:45Z | data/raw/2026-08-21 |  |
| 2026-08-21T1305 | upgates | error | 200 | 102039 | 83 | 2637 | 2026-08-21T13:05:06Z | data/raw/2026-08-21 | yield: 0 records from 83 fetches |
| 2026-08-21T1309 | upgates | ok | 200 | 102039 | 83 | 2389 | 2026-08-21T13:09:48Z | data/raw/2026-08-21 |  |
| 2026-08-21T1315 | upgates | ok | 200 | 102039 | 31 | 2359 | 2026-08-21T13:15:23Z | data/raw/2026-08-21 |  |
| 2026-08-21T1318 | upgates | ok | 200 | 102039 | 15 | 2355 | 2026-08-21T13:18:30Z | data/raw/2026-08-21 |  |
| 2026-08-21T1320 | shoptet | error | 200 | 126274 | 12 | 4112 | 2026-08-21T13:20:05Z | data/raw/2026-08-21 | yield: 0 records from 12 fetches |
| 2026-08-21T1321 | shoptet | ok | 200 | 126274 | 12 | 3045 | 2026-08-21T13:21:39Z | data/raw/2026-08-21 | yield: 0 new; 2 contract-rejected, 10 gdpr-dropped, corpus holds 392 |
| 2026-08-21T1322 | shoptet | ok | 200 | 126274 | 12 | 2912 | 2026-08-21T13:22:40Z | data/raw/2026-08-21 | yield: 0 new; 2 contract-rejected, 10 gdpr-dropped, corpus holds 392 |
| 2026-08-21T1559 | smlouvy | ok | 200 | 12753541 | 7735 | 187271 | 2026-08-21T15:59:51Z | data/raw/2026-08-21 |  |

---

# Ingest run 2026-08-21T1803
Run date: 2026-08-21  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `ares` | 200 | 35575 | 8 | 0 | — | structured | yes | resolved 8 of 8 (404 0, bad-checksum 0); named 6 employer record(s) |
| `cc-cz` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `ec-hys` | 200 | 169012 | 45 | 45 | — | structured | yes |  |
| `hlidac` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `mpsv` | 200 | 19433907 | 16 | 16 | — | structured | yes | coverage: 27 of 31 days (4 absent); 46716 rows -> 6597 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| `nku` | 200 | 76693 | 122 | 122 | — | structured | yes |  |
| `reddit-new` | 200 | 194495 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 326148 | 100 | 98 | — | structured | yes |  |
| `shoptet` | 200 | 126274 | 179 | 0 | — | structured | yes | yield: 0 new; 2 contract-rejected, 10 gdpr-dropped, corpus holds 392 |
| `smlouvy` | 200 | 12753541 | 7735 | 7649 | — | structured | yes |  |
| `suggest` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `ted` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `upgates` | 200 | 102039 | 8 | 0 | — | structured | yes |  |
| `vestbee` | 200 | 1046472 | 47 | 36 | — | structured | yes |  |
| `yc-oss` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |

**5 feed(s) failed their contract this run.** A contract violation is a first-class error: a 200 carrying the wrong body is a lie, where a 500 is honest.

## Staged records — PENDING, not appended

8016 records carry their mechanical fields and are waiting on a model. 99 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 8016 |
| `scores.recurrence` | 8016 |
| `title` | 8016 |
| `geo_origin` | 8016 |
| `summary` | 8016 |
| `sector` | 8000 |
| `pain` | 198 |

**Transport status UNKNOWN for 5 feed(s):** `cc-cz`, `hlidac`, `suggest`, `ted`, `yc-oss`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 8016 staged record(s) passed the field allowlist and the email/phone content scan.

## Dedup by identity key — same resource, different id

**50 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

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

**1 key(s) were EXEMPTED from dedup**, because a key naming more than one record is a listing page, a dataset landing page or a roundup — not an identity. Merging on one would delete distinct records. Measured over the committed corpus: 67 urls are shared by 571 records (6.1%), one Vestbee roundup being the url of 32 funding rounds.

| key | why it was not used |
|---|---|
| `url:vestbee.com/insights/articles/top-cee-funding-rounds-closed-in-july-2026` | carried by 10 ledger records — a listing or dataset page, not an identity |
