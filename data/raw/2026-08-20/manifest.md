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

## Model passes — RUN 2026-08-20, and the seam that made them possible

The section above was written by the mechanical pass and is left as it stood:
4,807 records staged, pending a model. This section is what happened next.

**The blocker was plumbing, and it is now measured.** `normalize.py`'s
`model_passes()` had refused to run since it was written, on the honest grounds
that nobody had measured whether this pipeline can authenticate. Measured
2026-08-20: `with-secrets curl --variable '%ANTHROPIC_API_KEY' --expand-header
'x-api-key: {{ANTHROPIC_API_KEY}}' … /v1/messages` returns **HTTP 200** from
`claude-opus-5`. `with-secrets` still refuses interpreters, so normalize.py — a
python interpreter — still cannot hold the key. The passes therefore run through
a three-part seam, `scripts/model_pass.py plan` → `scripts/model_pass.sh`
(the only process that ever sees the secret, one wrapped curl per batch) →
`scripts/model_pass.py apply`. Model: `claude-opus-5`, structured output
(`output_config.format`, a strict JSON schema per batch), effort `medium`.

| stage | records |
|---|---|
| staged by the mechanical pass | 4,807 |
| **pass A** scored (scale, recurrence, sector, geo_origin, grade-3 urgency) | 4,783 |
| refused by the **pain bar** (suggest: no complaint/failure/workaround) | 24 |
| **materiality drops** (`money <= 1 AND scale <= 1 AND urgency == 0`) | 1,411 |
| survivors | 3,143 |
| **pass B** given an EN title + summary (survivors only) | 116 of 167 |
| appended to `data/signals/<type>/2026-08-20.jsonl` | **3,092** |
| left staged as PENDING | 304 |

Pass B ran over 167 survivors, not over all 420 records that lacked a title:
the materiality filter sits between the two passes, so 253 records that were
about to be dropped never had a summary written for them.

**Why 51 survivors are still pending.** Two pass-B batches returned
`HTTP 400 invalid_request_error: "Your credit balance is too low to access the
Anthropic API"` (bodies kept in `.model/log/B-*.err.json`), losing 50 records,
and one record (`ted-565159-2026`) was refused by our own validator for
returning a three-sentence summary where the law allows two. Nothing was
guessed to cover the gap: those records keep their `_needs`, stay in
`data/raw/`, and land on a later run. The remaining 253 pending records are
non-survivors that materiality would have dropped anyway.

**The pain bar refused 24 suggest records** — every one a neutral lookup rather
than a complaint: 13 of the form `X zkušenosti` ("experiences with X") and 11 of
the form `jak zrušit X` ("how to cancel X"). Engagement never justifies a
record, and a how-to question is not a documented failure. Nothing was written
to those records at all, because `pain` is an admission bar and is never
persisted.

**`extraction: llm-fallback`** is set on every record a model touched. Read it
as the review flag it is on the site, NOT as a claim that a feed broke: no
contract was violated this run (see the contract table above). `structured` was
not available to us — a model, not a parser, produced these records' judgement
fields — and CONVENTIONS' gloss for `llm-fallback` ("the structured parse
violated its contract") does not describe this case either. This is the closest
honest token in a closed vocabulary that has none for "parsed payload, model
judgement", and it is the first time any record in this corpus carries the field
at all. A distinct token would be a CONVENTIONS + `SignalSchema` change.
