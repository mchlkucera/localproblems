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
