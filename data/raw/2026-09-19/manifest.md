# run manifest — 2026-09-19

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-09-19`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-19T0600 | veklep | ok | 200 | 1699950 | 137 | 5934 | 2026-09-19T06:00:47Z | data/raw/2026-09-19 |  |

---

# Ingest run 2026-09-19T1401
Run date: 2026-09-19  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `coi` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `ec-hys` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `hackathon` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `hlidac` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `mpsv` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `nen-ptk` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `nku` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `reddit-new` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `reddit-search` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `suggest` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `sukl` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `tacr` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `ted` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `veklep` | 200 | 1699950 | 137 | 29 | — | structured | yes |  |
| `vestbee` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |
| `yc-oss` | — | 0 | 0 | 0 | zero | none | **NO** | no fetch receipt and no payload — the feed did not run |

**16 feed(s) failed their contract this run.** A contract violation is a first-class error: a 200 carrying the wrong body is a lie, where a 500 is honest.

## Staged records — PENDING, not appended

29 records carry their mechanical fields and are waiting on a model. 108 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 29 |
| `scores.recurrence` | 29 |
| `title` | 29 |
| `sector` | 29 |
| `geo_origin` | 29 |
| `summary` | 29 |
| `scores.urgency` | 12 |

**Transport status UNKNOWN for 16 feed(s):** `cc-cz`, `coi`, `ec-hys`, `hackathon`, `hlidac`, `mpsv`, `nen-ptk`, `nku`, `reddit-new`, `reddit-search`, `suggest`, `sukl`, `tacr`, `ted`, `vestbee`, `yc-oss`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 29 staged record(s) passed the field allowlist and the email/phone content scan.

## Republication candidates — same quote and value, new notice id

No staged tender record repeats the quote and value of one already on file.

## Dedup by identity key — same resource, different id

No staged record matched an existing record on an identity key.

---

# Attended completion, 2026-09-19: the veklep feed (scoped run) + dotace errata

Two follow-ups owed by the 2026-09-18 scans: the scripted `veklep` feed had not run
since 2026-09-08, and the dotace-scan named six stale grant records for the errata
ledger. Nothing was committed.

## veklep: what ran, in INGEST.md order

`scripts/ingest.sh` was NOT run wholesale, because its step 4 is `db.py rebuild` and
the coordinator rebuilds once at the end. The same steps were run one by one, scoped
to this one feed:

1. `scripts/fetch_all.sh data/raw/2026-09-19 veklep` (SINCE = 70 days back, 2026-07-11,
   on `datumPosledniUpravy`).
2. `normalize.py --raw data/raw/2026-09-19 --mechanical-only`
3. Model passes A and B, ATTENDED: this session filled every `_needs` in place (rubric
   and writer rules of `scripts/model_pass.py`, judged from each card only).
4. `normalize.py --raw data/raw/2026-09-19 --complete`
5. `db.py fetchlog data/raw/2026-09-19` and `db.py health`
6. **NOT run:** `db.py upsert data/signals/regulation/2026-09-19.jsonl` and
   `db.py rebuild`. The coordinator's final rebuild covers both.

**A first attempt failed its auth probe and was discarded.** Inside the command
sandbox, `with-secrets` cannot read the sops age key, so the probe reported
"with-secrets never reached curl" for both key names. That is the INCONCLUSIVE branch
(token presence UNKNOWN, not absent). The failure came from the sandbox, not the feed,
so its manifest row and receipt were moved to the Trash before normalize or fetchlog
ever read them. No fetch_log row exists for it. The re-run outside the sandbox
authenticated with `HLIDAC_STATU_TOKEN`.

## veklep: result

| step | count |
|---|---|
| fetched | **137** materials on 6 pages (API total 137, no page cap hit), HTTP 200, 1,699,950 bytes |
| already in `seen.txt` | 108 |
| staged (new ids) | 29 (identity-key dedup 0, quote-unverified 0, AC-GDPR1 0) |
| dropped by materiality | **10** (money 0, scale ≤ 1, urgency 0) |
| **appended** | **19**, to `data/signals/regulation/2026-09-19.jsonl`. `seen.txt` +19, rewritten sorted (byte order, the same order `sort -u` gives: `LC_ALL=C sort -c` and `sort -c` both pass) |

The 2026-09-18 reg-scan estimated about 26 new drafts. 29 new ids landed, some of
them older materials (back to 2025-11) that were touched again inside the window.

**`ok=1 items_kept=0` silences: none.** The contract row for veklep is `ok=1`,
`items_fetched 137`, `items_kept 29`. normalize counts `items_kept` after the seen.txt
dedup and before materiality, so 19 were appended. The other 16 feeds carry "no fetch
receipt and no payload" because this was a scoped run. `db.py fetchlog` skipped them by
design (`not logged (did not run this scoped run, not a failure)`), so none of them
moved toward BROKEN.

**Urgency rulings (12 `urgency_pending` records):** every one was ruled **0**. Each is a
draft whose comment deadline has passed, and none is in force or enforced. Pass A
judged scale, recurrence, sector and geo_origin (CZ for all 29), and pass B wrote each
English title and summary from the card.

Appended (scale/money/urgency/recurrence):

| id | sector | s/m/u/r | draft |
|---|---|---|---|
| `veklep-ALBSDXTKB4NK` | b2b | 2/0/3/3 | MPO bill: act on innovative and scalable business |
| `veklep-KORNDXQH4G02` | legal-compliance | 2/0/3/3 | MPO bill adapting to Reg. (EU) 2024/3015 (foreign-trade regimes + labour inspection) |
| `veklep-ALBSDXRFYLM6` | health | 2/0/3/2 | 2027 health reimbursement decree (point values, limits) |
| `veklep-KORNDXRBTYB9` | govtech | 3/0/3/2 | 2027 tax-administration form decrees |
| `veklep-KORNDXRB97TP` | govtech | 2/0/3/3 | real estate tax form decree 388/2025 amendment |
| `veklep-KORNDXRBYXXJ` | govtech | 2/0/3/3 | Customs Administration filing forms decree |
| `veklep-KORNDXSH4PXO` | legal-compliance | 1/0/3/3 | workplace blood-lead limit (NV 361/2007) |
| `veklep-KORNDXY9WP89` | environment | 2/0/3/3 | plant protection products decree 132/2018 |
| `veklep-KORNDXYA7F6I` | govtech | 1/0/3/3 | state-administration qualification training decree |
| `veklep-KORNDXSCDDKR` | govtech | 2/0/3/3 | local-government officials' education decree 414/2024 |
| `veklep-KORNDXSF6SSH` | housing | 1/0/3/3 | radon remediation subsidy decree 362/2016 |
| `veklep-KORNDXRHZE97` | govtech | 0/0/3/3 | police markings decree 122/2015 |
| `veklep-KORNDXYB4T22` | govtech | 1/0/3/2 | examiner remuneration decrees |
| `veklep-KORNDY2BV728` | mobility | 1/0/3/3 | inland navigation crew competence (Del. Reg. (EU) 2026/118) |
| `veklep-KORNDY2BX7OK` | mobility | 2/0/3/2 | toll road sections decree 470/2012 (annual extension) |
| `veklep-KORNDY2BWJMB` | mobility | 2/0/3/2 | motorway vignette sections decree 480/2020 (annual extension) |
| `veklep-KORNDTKB9G50` | govtech | 2/0/0/3 | health-education admin information system decree (Act 95/2004) |
| `veklep-KORNDXQH9BRI` | govtech | 2/0/0/3 | deputies' bill on tax revenue sharing, Act 243/2000 (print 298) |
| `veklep-ALBSDW3HDEWG` | other | 2/0/0/3 | sport support act 115/2001, on the government agenda |

Dropped by materiality (not added to `seen.txt`, so they re-stage on the next run and
are dropped again unless their card changes): `veklep-KORNDV7FMSPN` (asylum decree
328/2015, scale 1), `veklep-KORNDVKKWEK9` (state property office act, 1),
`veklep-KORNDSAKSLEQ` (Interior Ministry schools decree, 1), `veklep-KORNDW7HRLI7`
(prison/custody orders, 0), `veklep-KORNDNSF3ZQ5` (Zlatý potok nature monument, 0),
`veklep-KORNDUEGPUWG` (overprinted 5,000 CZK banknote, 1), `veklep-KORNDVACDSIC`
(firearms medical-fitness regulation, 1, marked *skartováno*), `veklep-KORNDV4EB4WE`
(folk-architecture heritage reserves, 1), `veklep-KORNDV37RXI3` (inland navigation
medical fitness, 1), `veklep-KORNDXRHWVVT` (state awards regulations, 0).

**Owed to reg-scan (SCANS.md checklist 4):** the RIA "Definice problému" sections for
the 19 appended items, above all the innovative-business act, the Reg. 2024/3015 bill
and the RUD deputies' bill.

## Feed health (`db.py health`, generated 2026-09-19)

LIVE 11 · PENDING 6 · STALE 11 · BROKEN 0. `veklep`: LIVE, last_success 2026-09-19,
items_last_run 29, signals_total 242. Two things in the export that this run did not cause:

- **11 daily feeds moved LIVE → STALE** (ted, hlidac, hackathon, cc-cz, yc-oss, suggest,
  reddit-new, reddit-search, nku, sukl, ec-hys). None has run since 2026-09-08. Eleven
  days is more than three times a daily cadence, so this is observed reality. The
  previous export was simply 11 days old.
- **veklep's `error` field still shows the 2026-09-01 auth-probe failure.** `health`
  reports the newest non-null error in fetch_log, not this run's; this run's error is
  null and ok=1. Also pre-existing: the 2026-09-08 veklep run is logged twice in
  fetch_log (ids 117 and 134).

## Dotace errata: six `source-updated` lines appended to `data/errata.jsonl`

The ledgers are append-only, and the repo corrects a ledger value ON READ through
`data/errata.jsonl` (see `load_errata()` in `scripts/db.py`). The six records the
2026-09-18 dotace-scan named were each true when ingested (2026-08-14) and have since
been changed by their publishers. Neither existing class fits that, so a third class,
`source-updated`, is documented in `load_errata()`'s docstring, and `db.py errata` now
prints its `corrections`. Its `action` is `annotate-only`: money aggregates keep the
ingested value. Each line is one per id (the loader keys by id) and carries its receipt
and the date it was observed (2026-09-18). Every change below was re-verified in this
session from the 2026-09-18 captures (MS2021+ XML diffed against the 2026-09-03
snapshot, plus the IROP, SFŽP and TA ČR pages):

| id | what changed |
|---|---|
| `dotace-irop-119-cyklodoprava` | closes 2026-09-10 → **2027-03-31**; total allocation 365.0 → **651.0 M CZK** |
| `dotace-irop-121-122-bezemisni-vozidla` | closes 2026-09-30 → **2027-03-31**; allocations 787.5 + 827.8 → **1,370.1 + 1,598.9 M CZK** |
| `dotace-irop-103-105-urgentni-prijmy` | ČR leg (105) closes 2026-09-21 → **2026-11-20**; 103/104 unchanged |
| `dotace-opzp-109-protipovodnova-ochrana` | allocation 2.0 → **2.6 bn CZK** (≈ EUR 106.8 M at ČNB 24.340); close unchanged |
| `dotace-mf-housenerg-fn-pujcky` | HOUSEnerg 1/2024 FN now on SFŽP's **closed** loan-call list; the 2026-12-31 date is no longer live; close date unpublished |
| `dotace-tacr-dut-call-2026` | date was the opening: window **1 Sep – 17 Nov 2026**; money 0 ("unpublished") → **600,000 EUR** CZ envelope |

For the IROP allocations, the ledger's money figure was a co-financing share of the old
total, and no share of the new total is published, so no new EUR figure is derived. **None
of the six is cited by any record in `data/problems/**`** (grep, 2026-09-19), so no record
needed editing. This closes coverage gap 1 of the 2026-09-18 dotace-scan.

```
feeds fetched:        1 (veklep; scoped run)
items fetched:        137 (108 already seen, 29 new)
kept after materiality: 19 appended to data/signals/regulation/2026-09-19.jsonl (10 dropped)
pending (unscored):   0
feeds BROKEN:         0 (11 daily feeds STALE: not run since 2026-09-08)
```
