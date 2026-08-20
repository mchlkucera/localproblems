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
| 2026-08-20T1416 | ted | ok | 200 | 22122270 | 2678 | 10193 | 2026-08-20T14:16:27Z | data/raw/2026-08-20 |  |
| 2026-08-20T1416 | hlidac | error | 000 | 0 | 0 | 0 | 2026-08-20T14:16:49Z |  | auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| 2026-08-20T1416 | cc-cz | ok | 200 | 17661 |  | 802 | 2026-08-20T14:16:49Z | data/raw/2026-08-20/feed-czechcrunch.xml |  |
| 2026-08-20T1416 | yc-oss | ok | 200 | 10402545 |  | 2302 | 2026-08-20T14:16:50Z | data/raw/2026-08-20/yc-all.json |  |
| 2026-08-20T1416 | suggest | ok | 200 | 11883 | 42 | 25755 | 2026-08-20T14:16:53Z | data/raw/2026-08-20/suggest-pain.jsonl |  |
| 2026-08-20T1416 | reddit-new | ok | 429 | 54045 | 1 | 1450 | 2026-08-20T14:21:03Z | data/raw/2026-08-20 | partial: 3 of 4 failed: reddit-Brno-new.rss:HTTP-429 reddit-Prague-new.rss:HTTP-429 reddit-czechia-new.rss:HTTP-429 |
| 2026-08-20T1416 | reddit-search | ok | 429 | 29795 | 3 | 4445 | 2026-08-20T14:21:03Z | data/raw/2026-08-20 | partial: 13 of 16 failed: reddit-czech-q-nefunguje.rss:HTTP-429 reddit-czech-q-problm.rss:HTTP-429 reddit-czech-q-byrokracie.rss:HTTP-429 reddit-czech-q-pro_neexistuje.rss:HTTP-429 reddit-Brno-q-probl |
| 2026-08-20T1416 | nku | skipped | 000 | 0 | 0 | 0 | 2026-08-20T14:24:30Z |  | registry status=planned |

---

# Ingest run 2026-08-20T1624
Run date: 2026-08-20  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 17661 | 10 | 10 | — | structured | yes |  |
| `hlidac` | — | 0 | 0 | 0 | — | none | **NO** | transport: auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| `reddit-new` | 429 | 54045 | 25 | 0 | — | none | **NO** | transport: HTTP 429 — partial: 3 of 4 failed: reddit-Brno-new.rss:HTTP-429 reddit-Prague-new.rss:HTTP-429 reddit-czechia-new.rss:HTTP-429 |
| `reddit-search` | 429 | 29795 | 13 | 0 | — | none | **NO** | transport: HTTP 429 — partial: 13 of 16 failed: reddit-czech-q-nefunguje.rss:HTTP-429 reddit-czech-q-problm.rss:HTTP-429 reddit-czech-q-byrokracie.rss:HTTP-429 reddit-czech-q-pro_neexistuje.rss:HTTP-429 reddit-Brno-q-problm.rss:HTTP-429 reddit-Brno-q-byrokracie.rss:HTTP-429 reddit-Brno-q-pro_neexistuje.rss:HTTP-429 reddit-Prague-q-nefunguje.rss:HTTP-429 reddit-Prague-q-byrokracie.rss:HTTP-429 reddit-Prague-q-pro_neexistuje.rss:HTTP-429 reddit-czechia-q-nefunguje.rss:HTTP-429 reddit-czechia-q-problm.rss:HTTP-429 reddit-czechia-q-pro_neexistuje.rss:HTTP-429 |
| `suggest` | 200 | 11883 | 42 | 42 | — | structured | yes |  |
| `ted` | 200 | 22122270 | 2678 | 368 | above-range | structured | yes |  |
| `yc-oss` | 200 | 10402545 | 6189 | 4387 | — | structured | yes |  |

**3 feed(s) failed their contract this run.** A contract violation is a first-class error: a 200 carrying the wrong body is a lie, where a 500 is honest.

## Staged records — PENDING, not appended

4807 records carry their mechanical fields and are waiting on a model. 4112 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 4807 |
| `scores.recurrence` | 4807 |
| `geo_origin` | 4807 |
| `sector` | 4439 |
| `title` | 420 |
| `summary` | 420 |
| `pain` | 42 |
| `scores.urgency` | 30 |

**Transport status UNKNOWN for 1 feed(s):** `hlidac`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 4807 staged record(s) passed the field allowlist and the email/phone content scan.

---

# Ingest run 2026-08-20T1631
Run date: 2026-08-20  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 17661 | 10 | 10 | — | structured | yes |  |
| `hlidac` | — | 0 | 0 | 0 | — | none | **NO** | transport: auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent. |
| `reddit-new` | 429 | 54045 | 25 | 0 | — | none | **NO** | transport: HTTP 429 — partial: 3 of 4 failed: reddit-Brno-new.rss:HTTP-429 reddit-Prague-new.rss:HTTP-429 reddit-czechia-new.rss:HTTP-429 |
| `reddit-search` | 429 | 29795 | 13 | 0 | — | none | **NO** | transport: HTTP 429 — partial: 13 of 16 failed: reddit-czech-q-nefunguje.rss:HTTP-429 reddit-czech-q-problm.rss:HTTP-429 reddit-czech-q-byrokracie.rss:HTTP-429 reddit-czech-q-pro_neexistuje.rss:HTTP-429 reddit-Brno-q-problm.rss:HTTP-429 reddit-Brno-q-byrokracie.rss:HTTP-429 reddit-Brno-q-pro_neexistuje.rss:HTTP-429 reddit-Prague-q-nefunguje.rss:HTTP-429 reddit-Prague-q-byrokracie.rss:HTTP-429 reddit-Prague-q-pro_neexistuje.rss:HTTP-429 reddit-czechia-q-nefunguje.rss:HTTP-429 reddit-czechia-q-problm.rss:HTTP-429 reddit-czechia-q-pro_neexistuje.rss:HTTP-429 |
| `suggest` | 200 | 11883 | 42 | 42 | — | structured | yes |  |
| `ted` | 200 | 22122270 | 2678 | 368 | above-range | structured | yes |  |
| `yc-oss` | 200 | 10402545 | 6189 | 4387 | — | structured | yes |  |

**3 feed(s) failed their contract this run.** A contract violation is a first-class error: a 200 carrying the wrong body is a lie, where a 500 is honest.

## Staged records — PENDING, not appended

4807 records carry their mechanical fields and are waiting on a model. 4112 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 4807 |
| `scores.recurrence` | 4807 |
| `geo_origin` | 4807 |
| `sector` | 4439 |
| `title` | 420 |
| `summary` | 420 |
| `pain` | 42 |
| `scores.urgency` | 30 |

**Transport status UNKNOWN for 1 feed(s):** `hlidac`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 4807 staged record(s) passed the field allowlist and the email/phone content scan.
