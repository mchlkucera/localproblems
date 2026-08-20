# run manifest — 2026-08-20

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-08-20`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-08-20T0909 | cc-cz | ok | 200 | 18080 |  | 4056 | 2026-08-20T09:09:29Z | data/raw/2026-08-20/feed-czechcrunch.xml |  |
| 2026-08-20T0909 | yc-oss | ok | 200 | 10402545 |  | 1069 | 2026-08-20T09:09:33Z | data/raw/2026-08-20/yc-all.json |  |
| 2026-08-20T0910 | hlidac | skipped | 000 | 0 | 0 | 0 | 2026-08-20T09:10:57Z |  | registry status=blocked |
| 2026-08-20T0911 | hlidac | skipped | 000 | 0 | 0 | 0 | 2026-08-20T09:11:23Z |  | registry status=blocked |
| 2026-08-20T0919 | cc-cz | ok | 200 | 18080 |  | 2807 | 2026-08-20T09:19:56Z | data/raw/2026-08-20/feed-czechcrunch.xml |  |
| 2026-08-20T0919 | yc-oss | ok | 200 | 10402545 |  | 885 | 2026-08-20T09:19:59Z | data/raw/2026-08-20/yc-all.json |  |
| 2026-08-20T0920 | hlidac | skipped | 000 | 0 | 0 | 0 | 2026-08-20T09:20:19Z |  | registry status=blocked |
