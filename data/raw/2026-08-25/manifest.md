# run manifest — 2026-08-25

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-08-25`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-08-25T0542 | veklep | ok | 200 | 3627020 | 296 | 6311 | 2026-08-25T05:42:07Z | data/raw/2026-08-25 |  |
| 2026-08-25T0542 | hlidac | ok | 200 | 1708539 | 669 | 11286 | 2026-08-25T05:42:57Z | data/raw/2026-08-25 |  |
| 2026-08-25T0544 | hlidac | ok | 200 | 1555719 | 694 | 8313 | 2026-08-25T05:44:38Z | data/raw/2026-08-25 |  |

---

# Ingest run 2026-08-25T0746
Run date: 2026-08-25  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `ec-hys` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `hlidac` | 200 | 1555719 | 1363 | 1291 | — | structured | yes |  |
| `mpsv` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `nku` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `reddit-new` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `reddit-search` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `suggest` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `ted` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `veklep` | 200 | 3627020 | 296 | 296 | above-range | structured | yes |  |
| `vestbee` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `yc-oss` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |

**10 feed(s) failed their contract this run.** A contract violation is a first-class error: a 200 carrying the wrong body is a lie, where a 500 is honest.

## Staged records — PENDING, not appended

1586 records carry their mechanical fields and are waiting on a model. 71 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 1586 |
| `scores.recurrence` | 1586 |
| `title` | 1586 |
| `sector` | 1586 |
| `geo_origin` | 1586 |
| `summary` | 1586 |
| `scores.urgency` | 242 |

**Transport status UNKNOWN for 10 feed(s):** `cc-cz`, `ec-hys`, `mpsv`, `nku`, `reddit-new`, `reddit-search`, `suggest`, `ted`, `vestbee`, `yc-oss`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

**1 record(s) REFUSED for carrying personal data.** They were dropped before staging and cannot reach a ledger. The ledgers are public and append-only, so this gate fails closed rather than redacting.

| record | feed | field | kind |
|---|---|---|---|
| `hlidac-34432137` | `hlidac` | `quote` | phone |

Snippets are deliberately NOT printed here: this manifest is committed, and writing the offending value into it would publish exactly what the gate just prevented.

## Dedup by identity key — same resource, different id

**1 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

| staged id | already in the ledger as | key | feed | url |
|---|---|---|---|---|
| `hlidac-36459536` | `hlidac-38795752` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38795752 |

## Coverage notes — attended retrospective run 2026-08-25 (backfill session)

This run is a TARGETED RETROSPECTIVE, not the hourly loop: only `veklep` and
`hlidac` were fetched, deliberately. The 10 "did not run" rows above are that
choice, not an outage — every one of those feeds ran and completed on
2026-08-24 (see that run's manifest and commit 0490d6e).

**VeKLEP backfill window — the probe and the choice.** The fetcher windows on
`datumPosledniUpravy`; the candidate alternative for a backfill was
`datumAutorizace`. Probed live 2026-08-25 (strana=1, totals only):
`datumAutorizace:[2026-01-01 TO *]` = 228 · `datumPosledniUpravy:[2026-01-01 TO *]`
= 296 · the cross-window `datumAutorizace:[2026-01-01 TO *] AND
datumPosledniUpravy:[* TO 2026-01-01]` = **0**. So the script's native window is
a strict SUPERSET of the autorizace window for the same SINCE: it catches every
draft authored since 2026-01-01 (228) PLUS 68 older drafts whose process stage
changed since January — which the backfill wants anyway. The script ran
unmodified: `VEKLEP_PAGES=14 scripts/fetch_veklep.sh 2026-01-01`, 296/296 on
disk. The `above-range` yield row is this deliberate 8-month window against a
contract sized for the 70-day default; not an anomaly.

**Hlídač backfill — chosen thresholds and windows, and what was EXCLUDED.**
Volumes were measured before choosing (probes 2026-08-25, totals only):
`cenaSDph:>20000000 AND datumUzavreni:[2026-06-01 TO *]` = 1,164 ·
`[2026-07-01 TO *]` = 694 · `cenaSDph:>50000000 AND
datumUzavreni:[2025-11-01 TO 2026-06-01]` = 1,269 · `cenaSDph:>100000000`
same window = 669. Chosen, to keep the model half near the ~1,000-1,500
completion budget for this session:
- run 1 `hlidac-bigdeep-p*.json`: **>100M CZK, datumUzavreni [2025-11-01 TO
  2026-06-01]** — 669/669 on disk. Invoked via the new `HLIDAC_QUERIES` env
  override (added to scripts/fetch_hlidac.sh this session, sibling of
  HLIDAC_PAGES; same uniform-numeric-threshold law, never keywords), with the
  bounded end carried in the query half and SINCE=2025-11-01 supplying the start.
- run 2 `hlidac-firehose-p*.json`: **>20M CZK, datumUzavreni [2026-07-01 TO *]**
  — 694/694 on disk, the standard firehose threshold, script unmodified.

NAMED EXCLUSIONS (not silent truncation): contracts of 20-100M CZK closed
2025-11-01..2026-06-30 were NOT fetched — that band is covered only from
2026-07-01 forward (plus whatever the 2026-08-24 keyword-era fetches caught
from mid-June). A future backfill session can close the gap with
`HLIDAC_QUERIES='midband|cenaSDph:>20000000 AND cenaSDph:<100000000 AND
datumUzavreni:[* TO 2026-07-01]'` and SINCE=2025-11-01 (~2,600 contracts at
the measured volumes — it needs its own completion budget).

Model half for this run: session subagent batches per
scripts/model_pass_agent.py (no API credit spent).

## Health export note — run 2026-08-25T0746

`db.py health` after this run: LIVE=7, PENDING=7, BROKEN=10 (ted, cc-cz,
vestbee, yc-oss, suggest, reddit-new, reddit-search, nku, ec-hys, mpsv).
ALL TEN "BROKEN" states are the targeted-retrospective artifact described
above: each carries consecutive_failures=1 from a synthetic "no fetch receipt
and no payload — the feed did not run" contract row, not from a failed fetch.
Every one of them fetched OK on 2026-08-24 (see that manifest), none is at the
3-consecutive-run escalation threshold, and the next full `scripts/ingest.sh`
run will return them to LIVE. No feed has been BROKEN for 3 consecutive runs.
`veklep` and `hlidac` are LIVE with today's authenticated 200s.

## Model half — run 2026-08-25 (attended, subagent driver)

Pass A: 32 batches (1,586 records) via session subagents; apply filled
1,586/1,586, 0 rejected, 0 pain-refused. Pass B: materiality kept 1,488 of
1,586 (98 veklep records dropped as non-material — money 0/unknown, scale <=1,
urgency 0 — and correctly left staged without title/summary); 30 batches
filled 1,181, 307 rejected on the known Czech-abbreviation sentence-split
("c. N", "Sb.", dotted dates); the documented single retry (7 re-planned
batches, splitter trap named in the brief) filled all 307 with 0 rejects.
Completion: 1,488 appended (regulation +198 veklep, tenders +1,290 hlidac),
0 materiality drops at --complete, 98 incomplete skipped (the same
non-material veklep set), identity-key dedup at append: 0.
