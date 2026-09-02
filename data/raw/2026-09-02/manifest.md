# run manifest — 2026-09-02

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-09-02`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-01T2245 | ted | ok | 200 | 78928725 | 9497 | 95642 | 2026-09-01T22:45:07Z | data/raw/2026-09-02 |  |
| 2026-09-01T2245 | hlidac | error | 000 | 0 | 0 | 0 | 2026-09-01T22:46:50Z |  | auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| 2026-09-01T2245 | veklep | error | 000 | 0 | 0 | 0 | 2026-09-01T22:46:50Z |  | auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| 2026-09-01T2245 | cc-cz | ok | 200 | 18539 |  | 2251 | 2026-09-01T22:46:50Z | data/raw/2026-09-02/feed-czechcrunch.xml |  |
| 2026-09-01T2245 | yc-oss | ok | 200 | 10422540 |  | 5622 | 2026-09-01T22:46:53Z | data/raw/2026-09-02/yc-all.json |  |
| 2026-09-01T2245 | vestbee | ok | 200 | 1054936 | 47 | 7080 | 2026-09-01T22:46:58Z | data/raw/2026-09-02 |  |
| 2026-09-01T2245 | suggest | ok | 200 | 11856 | 42 | 43025 | 2026-09-01T22:48:23Z | data/raw/2026-09-02/suggest-pain.jsonl | partial: 1 of 144 queries failed |
| 2026-09-01T2245 | reddit-new | ok | 200 | 189193 | 100 | 2510 | 2026-09-01T22:52:51Z | data/raw/2026-09-02 |  |
| 2026-09-01T2245 | reddit-search | ok | 200 | 330655 | 100 | 1659 | 2026-09-01T22:52:51Z | data/raw/2026-09-02 |  |
| 2026-09-01T2245 | nku | ok | 200 | 76650 | 125 | 2364 | 2026-09-01T22:53:05Z | data/raw/2026-09-02 |  |
| 2026-09-01T2245 | sukl | skipped | 000 | 0 | 0 | 0 | 2026-09-01T22:53:07Z |  | registry status=planned |
| 2026-09-01T2245 | ec-hys | error | 000 | 0 | 0 | 2106 | 2026-09-01T22:53:08Z | data/raw/2026-09-02 | no records: page0:HTTP-000 |
| 2026-09-01T2245 | nen | skipped | 000 | 0 | 0 | 0 | 2026-09-01T22:53:10Z |  | registry status=planned |
| 2026-09-01T2245 | mpsv | ok | 200 | 17043418 | 18 | 24683 | 2026-09-01T22:53:10Z | data/raw/2026-09-02/mpsv-hiring-2026-08.json | coverage: 28 of 31 days (3 absent); 40094 rows -> 5471 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| 2026-09-01T2245 | coi | skipped | 000 | 0 | 0 | 0 | 2026-09-01T22:53:37Z |  | registry status=planned |
| 2026-09-01T2245 | smlouvy | skipped | 000 | 0 | 0 | 0 | 2026-09-01T22:53:37Z |  | registry status=planned |

---

# Ingest run 2026-09-02T0053
Run date: 2026-09-02  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 18539 | 10 | 10 | — | structured | yes |  |
| `ec-hys` | — | 0 | 0 | 0 | — | none | **NO** | transport: no records: page0:HTTP-000 |
| `hlidac` | — | 0 | 0 | 0 | — | none | **NO** | transport: auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| `mpsv` | 200 | 17043418 | 18 | 18 | — | structured | yes | coverage: 28 of 31 days (3 absent); 40094 rows -> 5471 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| `nku` | 200 | 76650 | 125 | 124 | — | structured | yes |  |
| `reddit-new` | 200 | 189193 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 330655 | 100 | 79 | — | structured | yes |  |
| `suggest` | 200 | 11856 | 42 | 27 | — | structured | yes | partial: 1 of 144 queries failed |
| `ted` | 200 | 78928725 | 9497 | 7635 | — | structured | yes |  |
| `veklep` | — | 0 | 0 | 0 | — | none | **NO** | transport: auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| `vestbee` | 200 | 1054936 | 47 | 18 | — | structured | yes |  |
| `yc-oss` | 200 | 10422540 | 6200 | 1240 | — | structured | yes |  |

**3 feed(s) failed their contract this run.** A contract violation is a first-class error: a 200 carrying the wrong body is a lie, where a 500 is honest.

## Staged records — PENDING, not appended

9219 records carry their mechanical fields and are waiting on a model. 6888 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 9219 |
| `scores.recurrence` | 9219 |
| `geo_origin` | 9219 |
| `sector` | 9201 |
| `title` | 7981 |
| `summary` | 7981 |
| `scores.urgency` | 1038 |
| `pain` | 206 |

**Transport status UNKNOWN for 3 feed(s):** `ec-hys`, `hlidac`, `veklep`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 9219 staged record(s) passed the field allowlist and the email/phone content scan.

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
| 2026-09-01T2258 | hlidac | ok | 200 | 2213689 | 946 | 13374 | 2026-09-01T22:58:41Z | data/raw/2026-09-02 |  |
| 2026-09-01T2258 | veklep | ok | 200 | 1772879 | 130 | 5271 | 2026-09-01T23:00:54Z | data/raw/2026-09-02 |  |
| 2026-09-01T2258 | ec-hys | ok | 200 | 179726 | 45 | 7722 | 2026-09-01T23:01:15Z | data/raw/2026-09-02 |  |
| 2026-09-01T2258 | ares | ok | 200 | 33346 | 8 | 8177 | 2026-09-01T23:02:20Z | data/raw/2026-09-02/ares-lookups-2026-08.json | resolved 8 of 8 (404 0, bad-checksum 0); named 6 employer record(s) |
| 2026-09-01T2258 | shoptet | ok | 200 | 128347 | 16 | 2884 | 2026-09-01T23:02:33Z | data/raw/2026-09-02 |  |
| 2026-09-01T2258 | upgates | ok | 200 | 102600 | 8 | 692 | 2026-09-01T23:03:10Z | data/raw/2026-09-02 |  |

---

# Ingest run 2026-09-02T0103
Run date: 2026-09-02  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `ares` | 200 | 33346 | 8 | 0 | — | structured | yes | resolved 8 of 8 (404 0, bad-checksum 0); named 6 employer record(s) |
| `cc-cz` | 200 | 18539 | 10 | 10 | — | structured | yes |  |
| `ec-hys` | 200 | 179726 | 45 | 27 | — | structured | yes |  |
| `hlidac` | 200 | 2213689 | 946 | 273 | — | structured | yes |  |
| `mpsv` | 200 | 17043418 | 16 | 16 | — | structured | yes | coverage: 28 of 31 days (3 absent); 40094 rows -> 5471 novy -> 18 aggregates written, of which 8 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| `nku` | 200 | 76650 | 125 | 124 | — | structured | yes |  |
| `reddit-new` | 200 | 189193 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 330655 | 100 | 79 | — | structured | yes |  |
| `shoptet` | 200 | 128347 | 183 | 0 | — | structured | yes |  |
| `suggest` | 200 | 11856 | 42 | 27 | — | structured | yes | partial: 1 of 144 queries failed |
| `ted` | 200 | 78928725 | 9497 | 7635 | — | structured | yes |  |
| `upgates` | 200 | 102600 | 1 | 0 | — | structured | yes |  |
| `veklep` | 200 | 1772879 | 130 | 41 | — | structured | yes |  |
| `vestbee` | 200 | 1054936 | 47 | 18 | — | structured | yes |  |
| `yc-oss` | 200 | 10422540 | 6200 | 1240 | — | structured | yes |  |

## Staged records — PENDING, not appended

9537 records carry their mechanical fields and are waiting on a model. 7668 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 9537 |
| `scores.recurrence` | 9537 |
| `geo_origin` | 9537 |
| `sector` | 9521 |
| `title` | 8299 |
| `summary` | 8299 |
| `scores.urgency` | 1071 |
| `pain` | 206 |

## AC-GDPR1 — contact-field gate

No personal data detected. 9537 staged record(s) passed the field allowlist and the email/phone content scan.

## Dedup by identity key — same resource, different id

**53 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

| staged id | already in the ledger as | key | feed | url |
|---|---|---|---|---|
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
| `hlidac-36459536` | `hlidac-38795752` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38795752 |
| `hlidac-36224920` | `hlidac-38551596` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38551596 |
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

## Match phase — run 2026-09-02 (executed 2026-09-03, attended)

10 session agents (6 screen + 4 discovery), match_log +4,814 rows — every
appended signal carries a decision: **23 linked** across 12 problems, 4,774
dismissed with per-cluster notes, 13 dup, 4 deferred. No new problem records
and no rescores: every new receipt landed on a dimension already at its
evidenced rung.

Linked: p-0008 +6 (ted-557060, ted-569596, ted-587584, ted-590734, ted-595810,
ted-600605) · p-0022 +6 (ted-589279, ted-592268, ted-598479, ted-599893,
ted-604583, echys-16155) · p-0031 +2 (ted-568275, ted-591378) · p-0001
(ted-587970) · p-0007 (mpsv-2026-08-manual-trades) · p-0033
(mpsv-2026-08-health-care) · p-0023 (mpsv-2026-08-back-office) · p-0017
(hlidac-36243132) · p-0002 (yc-jasmine-energy) · p-0005 (yc-asakana) ·
p-0011 (yc-evergrove) · p-0025 (yc-craftwork).

New-problem leads left below the bar (recorded so the next pass does not
re-derive them): hospital drug-DPS fragmentation (14 buyers, 49 notices, no
why-now); public-building energy-retrofit fragmentation (~20 tenders, p-0024/
p-0031 adjacent); UWWTD transposition veklep-KORNDXBH65S3 (one signal — becomes
proposable on a second, e.g. a ČOV tender or OPŽP call).

Deferred: ted-594464 (ČEPS 80M CZK AI-development DPS), hlidac-36284652 (DIA
Register of Persons framework), veklep-KORNDXAMWBJD (qualification-recognition
amendment, re-check when material text lands).

### Data-quality flags (for fixes OUTSIDE this run — ledgers are append-only)

1. **MPSV wage parse**: mpsv-2026-08-21919461 pushes a monthly salary through
   the hourly branch (28,500 CZK/h → €2.37M/seat), inflating the August
   health-care aggregate ~21%. The July figure already rendered in p-0011 and
   p-0033 prose came from the same extractor — re-check. Both August links are
   cited on counts, not euros.
2. **TED republication**: the same procurement re-notified under a new native
   id (≥10 confirmed pairs this run) is invisible to id- and identity-key
   dedup; handled manually at match. Candidate: buyer+value fingerprint at
   normalize.
3. **Sector tags** (pass A) unreliable on tenders — buyer-name bleed (ČNB HVAC
   → fintech; NÚKIB car in a cyber screen). Screens must match on object, not
   sector.
4. **veklep urgency** encodes stage freshness, not compliance deadlines
   (inverts on KORNDTRGAQDS: hard 2027-01-01 duty scored 0); veklep quotes
   truncate the operative clause (~300 chars) — read data/raw payloads when
   judging.
5. **roundup-*** index pages reached a shortlist as signals; filter or split
   before matching.
6. **money_eur null on USD/GBP rounds** ("figure as published; not converted")
   — a $240M round reads as no money.
7. hlidac-36299252: payer == recipient on a donation contract (source-data
   artifact).
