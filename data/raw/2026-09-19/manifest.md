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
| 2026-09-19T0815 | ted | ok | 200 | 74207493 | 8962 | 44936 | 2026-09-19T08:15:47Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | hlidac | ok | 200 | 2028943 | 845 | 18583 | 2026-09-19T08:16:39Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | veklep | ok | 200 | 1717846 | 138 | 5286 | 2026-09-19T08:18:44Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | tacr | ok | 200 | 264248 | 14 | 2188 | 2026-09-19T08:19:05Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | hackathon | ok | 200 | 4930138 | 14 | 33709 | 2026-09-19T08:19:08Z | data/raw/2026-09-19 | partial: hackjakbrno:mode-a upol:yield-zero |
| 2026-09-19T0815 | nen-ptk | ok | 200 | 45513311 | 138 | 323249 | 2026-09-19T08:19:43Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | edesky | skipped | 000 | 0 | 0 | 0 | 2026-09-19T09:14:44Z |  | registry status=planned |
| 2026-09-19T0815 | cc-cz | ok | 200 | 18130 |  | 890 | 2026-09-19T09:14:45Z | data/raw/2026-09-19/feed-czechcrunch.xml |  |
| 2026-09-19T0815 | yc-oss | ok | 200 | 10487745 |  | 3610 | 2026-09-19T09:14:46Z | data/raw/2026-09-19/yc-all.json |  |
| 2026-09-19T0815 | vestbee | ok | 200 | 1065432 | 48 | 1951 | 2026-09-19T09:14:50Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | suggest | ok | 200 | 11881 | 42 | 44982 | 2026-09-19T09:15:59Z | data/raw/2026-09-19/suggest-pain.jsonl |  |
| 2026-09-19T0815 | reddit-new | ok | 200 | 179540 | 100 | 1726 | 2026-09-19T09:20:29Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | reddit-search | ok | 200 | 333173 | 100 | 1945 | 2026-09-19T09:20:29Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | nku | ok | 200 | 76638 | 126 | 1349 | 2026-09-19T09:21:05Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | sukl | ok | 200 | 1624029 | 15 | 3238 | 2026-09-19T09:21:07Z | data/raw/2026-09-19 | validity=2026-09-19 rows_in_file=83294 aggregates=15 |
| 2026-09-19T0815 | ec-hys | ok | 200 | 133579 | 34 | 5207 | 2026-09-19T09:21:11Z | data/raw/2026-09-19 |  |
| 2026-09-19T0815 | nen | skipped | 000 | 0 | 0 | 0 | 2026-09-19T09:21:43Z |  | registry status=planned |
| 2026-09-19T0815 | mpsv | skipped | 000 | 0 | 0 | 0 | 2026-09-19T09:21:44Z | data/raw/2026-09-19 | month 2026-08 already present in seen.txt |
| 2026-09-19T0815 | coi | skipped | 200 | 39676640 | 0 | 11680 | 2026-09-19T09:21:44Z | data/raw/2026-09-19 | no completed half-year to emit: None |
| 2026-09-19T0815 | smlouvy | skipped | 000 | 0 | 0 | 0 | 2026-09-19T09:21:57Z |  | registry status=planned |

---

# Ingest run 2026-09-19T1121
Run date: 2026-09-19  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 18130 | 10 | 10 | — | structured | yes |  |
| `coi` | 200 | 39676640 | 0 | 0 | — | none | yes | no completed half-year to emit: None |
| `ec-hys` | 200 | 133579 | 34 | 15 | — | structured | yes |  |
| `hackathon` | 200 | 4930138 | 14 | 11 | below-range | structured | yes | partial: hackjakbrno:mode-a upol:yield-zero |
| `hlidac` | 200 | 2028943 | 845 | 138 | — | structured | yes |  |
| `mpsv` | — | 0 | 0 | 0 | — | none | yes | month 2026-08 already present in seen.txt |
| `nen-ptk` | 200 | 45513311 | 138 | 67 | above-range | structured | yes |  |
| `nku` | 200 | 76638 | 126 | 124 | — | structured | yes |  |
| `reddit-new` | 200 | 179540 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 333173 | 100 | 78 | — | structured | yes |  |
| `suggest` | 200 | 11881 | 42 | 27 | — | structured | yes |  |
| `sukl` | 200 | 1624029 | 15 | 2 | — | structured | yes | validity=2026-09-19 rows_in_file=83294 aggregates=15 |
| `tacr` | 200 | 264248 | 14 | 7 | — | structured | yes |  |
| `ted` | 200 | 74207493 | 8962 | 3906 | — | structured | yes |  |
| `veklep` | 200 | 1717846 | 138 | 18 | — | structured | yes |  |
| `vestbee` | 200 | 1065432 | 48 | 21 | — | structured | yes |  |
| `yc-oss` | 200 | 10487745 | 6237 | 993 | — | structured | yes |  |

## Staged records — PENDING, not appended

5470 records carry their mechanical fields and are waiting on a model. 11306 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 5470 |
| `scores.recurrence` | 5470 |
| `geo_origin` | 5470 |
| `sector` | 5468 |
| `title` | 4479 |
| `summary` | 4479 |
| `scores.urgency` | 240 |
| `pain` | 205 |
| `stated_need` | 84 |

**Transport status UNKNOWN for 1 feed(s):** `mpsv`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 5470 staged record(s) passed the field allowlist and the email/phone content scan.

## Republication candidates — same quote and value, new notice id

**365 staged tender record(s) repeat the verbatim quote and the value of a record already on file.** TED re-notifies the same procurement under a new number and neither dedup axis can see it. They are KEPT — a re-issued tender can be evidence (p-0031) — each carries the earlier id in `notes`, and MATCH decides dup or distinct.

| staged id | repeats | seen in |
|---|---|---|
| `hlidac-37106769` | `hlidac-37064793` | ledger |
| `ted-505034-2026` | `ted-567791-2026` | ledger |
| `ted-509261-2026` | `ted-585863-2026` | ledger |
| `ted-512419-2026` | `ted-588567-2026` | ledger |
| `ted-512670-2026` | `ted-563450-2026`, `ted-616997-2026` | ledger |
| `ted-514163-2026` | `ted-567618-2026`, `ted-594090-2026` | ledger |
| `ted-514916-2026` | `ted-514493-2026` | batch |
| `ted-515178-2026` | `ted-587084-2026` | ledger |
| `ted-520051-2026` | `ted-504761-2026` | batch |
| `ted-520572-2026` | `ted-557909-2026` | ledger |
| `ted-520836-2026` | `ted-503369-2026` | batch |
| `ted-521185-2026` | `ted-564088-2026` | ledger |
| `ted-522170-2026` | `ted-503608-2026` | batch |
| `ted-522603-2026` | `ted-508734-2026` | batch |
| `ted-524293-2026` | `ted-571033-2026`, `ted-578486-2026` | ledger |
| `ted-527994-2026` | `ted-515784-2026` | batch |
| `ted-529528-2026` | `ted-504717-2026` | batch |
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
| `ted-595209-2026` | `ted-506720-2026` | batch |
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
| `ted-619295-2026` | `ted-526780-2026`, `ted-527415-2026`, `ted-527946-2026`, `ted-529184-2026`, `ted-560693-2026`, `ted-561677-2026`, `ted-562280-2026`, `ted-563055-2026` | ledger |
| `ted-619336-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-619410-2026` | `ted-526780-2026`, `ted-527415-2026`, `ted-527946-2026`, `ted-529184-2026`, `ted-560693-2026`, `ted-561677-2026`, `ted-562280-2026`, `ted-563055-2026` | ledger |
| `ted-619596-2026` | `ted-581077-2026` | ledger |
| `ted-619642-2026` | `ted-582904-2026` | ledger |
| `ted-619830-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-619843-2026` | `ted-570436-2026` | ledger |
| `ted-619867-2026` | `ted-600583-2026` | ledger |
| `ted-619912-2026` | `ted-476872-2026`, `ted-557258-2026` | ledger |
| `ted-620083-2026` | `ted-566928-2026`, `ted-574453-2026` | ledger |
| `ted-620085-2026` | `ted-581636-2026` | ledger |
| `ted-620155-2026` | `ted-553984-2026`, `ted-563630-2026`, `ted-584842-2026` | ledger |
| `ted-620333-2026` | `ted-526780-2026`, `ted-527415-2026`, `ted-527946-2026`, `ted-529184-2026`, `ted-560693-2026`, `ted-561677-2026`, `ted-562280-2026`, `ted-563055-2026` | ledger |
| `ted-620340-2026` | `ted-533142-2026`, `ted-593389-2026` | ledger |
| `ted-620380-2026` | `ted-590480-2026` | ledger |
| `ted-620440-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-620449-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-620509-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-620574-2026` | `ted-610550-2026` | ledger |
| `ted-620669-2026` | `ted-498370-2026`, `ted-551264-2026`, `ted-578691-2026`, `ted-584275-2026`, `ted-613065-2026` | ledger |
| `ted-620705-2026` | `ted-549308-2026`, `ted-594098-2026`, `ted-604569-2026` | ledger |
| `ted-620746-2026` | `ted-588738-2026`, `ted-615753-2026` | ledger |
| `ted-620784-2026` | `ted-549344-2026` | ledger |
| `ted-620795-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026`, `ted-607320-2026`, `ted-615022-2026` | ledger |
| `ted-620801-2026` | `ted-579752-2026` | ledger |
| `ted-620817-2026` | `ted-539476-2026`, `ted-548770-2026`, `ted-565313-2026`, `ted-573848-2026`, `ted-594704-2026` | ledger |
| `ted-620866-2026` | `ted-618697-2026` | ledger |
| `ted-620933-2026` | `ted-573498-2026` | ledger |
| `ted-621080-2026` | `ted-580642-2026`, `ted-614675-2026` | ledger |
| `ted-621151-2026` | `ted-582057-2026` | batch |
| `ted-621196-2026` | `ted-550596-2026` | ledger |
| `ted-621211-2026` | `ted-526780-2026`, `ted-527415-2026`, `ted-527946-2026`, `ted-529184-2026`, `ted-560693-2026`, `ted-561677-2026`, `ted-562280-2026`, `ted-563055-2026` | ledger |
| `ted-621287-2026` | `ted-619553-2026` | batch |
| `ted-621320-2026` | `ted-526780-2026`, `ted-527415-2026`, `ted-527946-2026`, `ted-529184-2026`, `ted-560693-2026`, `ted-561677-2026`, `ted-562280-2026`, `ted-563055-2026` | ledger |
| `ted-621447-2026` | `ted-556622-2026` | ledger |
| `ted-621504-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-621507-2026` | `ted-502499-2026`, `ted-583423-2026` | ledger |
| `ted-621552-2026` | `ted-621368-2026` | batch |
| `ted-621597-2026` | `ted-581225-2026` | ledger |
| `ted-621616-2026` | `ted-472954-2026` | ledger |
| `ted-621987-2026` | `ted-528464-2026` | ledger |
| `ted-622002-2026` | `ted-526780-2026`, `ted-527415-2026`, `ted-527946-2026`, `ted-529184-2026`, `ted-560693-2026`, `ted-561677-2026`, `ted-562280-2026`, `ted-563055-2026` | ledger |
| `ted-622039-2026` | `ted-472954-2026` | ledger |
| `ted-622067-2026` | `ted-621214-2026` | batch |
| `ted-622094-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-622118-2026` | `ted-552858-2026` | ledger |
| `ted-622166-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-622187-2026` | `ted-536370-2026` | ledger |
| `ted-622336-2026` | `ted-564208-2026`, `ted-575552-2026`, `ted-579550-2026`, `ted-604354-2026`, `ted-610001-2026` | ledger |
| `ted-622374-2026` | `ted-564407-2026` | ledger |
| `ted-622416-2026` | `ted-593026-2026` | ledger |
| `ted-622435-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-622441-2026` | `ted-478035-2026` | ledger |
| `ted-622650-2026` | `ted-526780-2026`, `ted-527415-2026`, `ted-527946-2026`, `ted-529184-2026`, `ted-560693-2026`, `ted-561677-2026`, `ted-562280-2026`, `ted-563055-2026` | ledger |
| `ted-622707-2026` | `ted-596198-2026` | ledger |
| `ted-622711-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026`, `ted-616255-2026`, `ted-617149-2026`, `ted-617683-2026`, `ted-617935-2026`, `ted-618764-2026`, `ted-619223-2026` | ledger |
| `ted-622763-2026` | `ted-568539-2026` | ledger |
| `ted-622827-2026` | `ted-524252-2026`, `ted-575891-2026` | ledger |
| `ted-622847-2026` | `ted-549644-2026` | ledger |
| `ted-622890-2026` | `ted-566505-2026` | ledger |
| `ted-623065-2026` | `ted-506329-2026`, `ted-584655-2026`, `ted-591678-2026` | ledger |
| `ted-623243-2026` | `ted-509271-2026`, `ted-540308-2026`, `ted-554542-2026`, `ted-572170-2026` | ledger |
| `ted-623295-2026` | `ted-621929-2026` | batch |
| `ted-623347-2026` | `ted-622944-2026` | batch |
| `ted-623384-2026` | `ted-599539-2026` | ledger |
| `ted-623589-2026` | `ted-578250-2026`, `ted-609713-2026` | ledger |
| `ted-623773-2026` | `ted-525777-2026`, `ted-581836-2026`, `ted-617589-2026` | ledger |
| `ted-623837-2026` | `ted-604165-2026` | ledger |
| `ted-623961-2026` | `ted-602131-2026`, `ted-606455-2026` | ledger |
| `ted-624024-2026` | `ted-620275-2026` | batch |
| `ted-624244-2026` | `ted-528227-2026`, `ted-555065-2026` | ledger |
| `ted-624348-2026` | `ted-542879-2026`, `ted-612734-2026` | ledger |
| `ted-624360-2026` | `ted-566505-2026` | ledger |
| `ted-624602-2026` | `ted-565692-2026` | ledger |
| `ted-624669-2026` | `ted-623222-2026` | batch |
| `ted-624670-2026` | `ted-549344-2026` | ledger |
| `ted-624737-2026` | `ted-487706-2026`, `ted-558632-2026` | ledger |
| `ted-624750-2026` | `ted-621929-2026` | batch |
| `ted-624766-2026` | `ted-621659-2026` | batch |
| `ted-624809-2026` | `ted-618127-2026` | ledger |
| `ted-625063-2026` | `ted-472954-2026` | ledger |
| `ted-625081-2026` | `ted-578736-2026` | ledger |
| `ted-625193-2026` | `ted-625060-2026` | batch |
| `ted-625251-2026` | `ted-588762-2026`, `ted-609303-2026` | ledger |
| `ted-625324-2026` | `ted-566370-2026`, `ted-566898-2026` | ledger |
| `ted-625487-2026` | `ted-528024-2026` | ledger |
| `ted-625493-2026` | `ted-547014-2026` | ledger |
| `ted-625529-2026` | `ted-563059-2026` | ledger |
| `ted-625543-2026` | `ted-515998-2026` | ledger |
| `ted-625735-2026` | `ted-555036-2026` | ledger |
| `ted-625746-2026` | `ted-576997-2026` | ledger |
| `ted-625751-2026` | `ted-616779-2026` | ledger |
| `ted-625848-2026` | `ted-471761-2026`, `ted-479736-2026`, `ted-490749-2026`, `ted-505800-2026`, `ted-532517-2026`, `ted-555812-2026`, `ted-565673-2026`, `ted-576774-2026`, `ted-585277-2026`, `ted-596315-2026`, `ted-611059-2026` | ledger |
| `ted-625909-2026` | `ted-554010-2026` | ledger |
| `ted-626084-2026` | `ted-568436-2026` | ledger |
| `ted-626107-2026` | `ted-487559-2026`, `ted-530334-2026` | ledger |
| `ted-626318-2026` | `ted-519027-2026` | ledger |
| `ted-626356-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026`, `ted-607320-2026`, `ted-615022-2026` | ledger |
| `ted-626387-2026` | `ted-591785-2026` | ledger |
| `ted-626401-2026` | `ted-472422-2026`, `ted-494241-2026`, `ted-517185-2026`, `ted-535160-2026`, `ted-551220-2026`, `ted-561906-2026` | ledger |
| `ted-626410-2026` | `ted-583095-2026` | ledger |
| `ted-626433-2026` | `ted-623908-2026` | batch |
| `ted-626435-2026` | `ted-554275-2026`, `ted-589691-2026` | ledger |
| `ted-626448-2026` | `ted-580642-2026`, `ted-614675-2026` | ledger |
| `ted-626453-2026` | `ted-510532-2026`, `ted-516697-2026`, `ted-546315-2026` | ledger |
| `ted-626498-2026` | `ted-574740-2026` | ledger |
| `ted-626765-2026` | `ted-594680-2026` | ledger |
| `ted-626798-2026` | `ted-525777-2026`, `ted-581836-2026`, `ted-617589-2026` | ledger |
| `ted-626950-2026` | `ted-612025-2026` | ledger |
| `ted-627045-2026` | `ted-578736-2026` | ledger |
| `ted-627127-2026` | `ted-601039-2026` | ledger |
| `ted-627178-2026` | `ted-580929-2026` | ledger |
| `ted-627190-2026` | `ted-590307-2026` | ledger |
| `ted-627353-2026` | `ted-574236-2026` | ledger |
| `ted-627382-2026` | `ted-592165-2026` | ledger |
| `ted-627492-2026` | `ted-626397-2026` | batch |
| `ted-627511-2026` | `ted-626397-2026` | batch |
| `ted-627727-2026` | `ted-615050-2026` | ledger |
| `ted-627896-2026` | `ted-543957-2026`, `ted-583079-2026`, `ted-590399-2026`, `ted-598886-2026`, `ted-605495-2026`, `ted-608251-2026`, `ted-614775-2026` | ledger |
| `ted-628024-2026` | `ted-488911-2026`, `ted-533408-2026`, `ted-540928-2026`, `ted-550874-2026`, `ted-555408-2026`, `ted-568835-2026`, `ted-590021-2026`, `ted-593753-2026`, `ted-600559-2026`, `ted-618373-2026` | ledger |
| `ted-628111-2026` | `ted-589830-2026`, `ted-610006-2026` | ledger |
| `ted-628247-2026` | `ted-599842-2026` | ledger |
| `ted-628425-2026` | `ted-568576-2026`, `ted-609876-2026` | ledger |
| `ted-628548-2026` | `ted-596347-2026` | ledger |
| `ted-628611-2026` | `ted-628156-2026` | batch |
| `ted-628640-2026` | `ted-526246-2026` | ledger |
| `ted-628709-2026` | `ted-551853-2026` | ledger |
| `ted-628728-2026` | `ted-586749-2026` | ledger |
| `ted-628817-2026` | `ted-477579-2026`, `ted-507989-2026`, `ted-519602-2026`, `ted-538178-2026`, `ted-558024-2026`, `ted-581728-2026`, `ted-603543-2026`, `ted-606067-2026` | ledger |
| `ted-628921-2026` | `ted-543079-2026`, `ted-587212-2026` | ledger |
| `ted-629000-2026` | `ted-521393-2026`, `ted-551519-2026`, `ted-587670-2026`, `ted-602191-2026` | ledger |
| `ted-629039-2026` | `ted-560823-2026` | ledger |
| `ted-629086-2026` | `ted-566370-2026`, `ted-566898-2026` | ledger |
| `ted-629160-2026` | `ted-541568-2026`, `ted-543083-2026` | ledger |
| `ted-629262-2026` | `ted-578250-2026`, `ted-609713-2026` | ledger |
| `ted-629355-2026` | `ted-589525-2026`, `ted-618801-2026` | ledger |
| `ted-629623-2026` | `ted-588762-2026`, `ted-609303-2026` | ledger |
| `ted-629638-2026` | `ted-567576-2026` | ledger |
| `ted-629778-2026` | `ted-596347-2026` | ledger |
| `ted-629788-2026` | `ted-611042-2026` | ledger |
| `ted-629940-2026` | `ted-561484-2026` | ledger |
| `ted-630176-2026` | `ted-574507-2026` | ledger |
| `ted-630247-2026` | `ted-596617-2026` | ledger |
| `ted-630402-2026` | `ted-530977-2026`, `ted-599338-2026`, `ted-609548-2026` | ledger |
| `ted-630702-2026` | `ted-555251-2026` | ledger |
| `ted-631100-2026` | `ted-630804-2026` | batch |
| `ted-631151-2026` | `ted-575233-2026` | ledger |
| `ted-631300-2026` | `ted-570753-2026` | ledger |
| `ted-631428-2026` | `ted-597605-2026` | ledger |
| `ted-631526-2026` | `ted-586924-2026` | ledger |
| `ted-631562-2026` | `ted-579805-2026` | ledger |
| `ted-631663-2026` | `ted-630649-2026` | batch |
| `ted-631759-2026` | `ted-581057-2026` | ledger |
| `ted-631802-2026` | `ted-534000-2026` | batch |
| `ted-631809-2026` | `ted-572969-2026` | ledger |
| `ted-631877-2026` | `ted-531756-2026`, `ted-560017-2026`, `ted-580549-2026` | ledger |
| `ted-631915-2026` | `ted-570302-2026` | ledger |
| `ted-632248-2026` | `ted-471761-2026`, `ted-479736-2026`, `ted-490749-2026`, `ted-505800-2026`, `ted-532517-2026`, `ted-555812-2026`, `ted-565673-2026`, `ted-576774-2026`, `ted-585277-2026`, `ted-596315-2026`, `ted-611059-2026` | ledger |
| `ted-632439-2026` | `ted-574919-2026` | ledger |
| `ted-632471-2026` | `ted-541568-2026`, `ted-543083-2026` | ledger |
| `ted-632625-2026` | `ted-544821-2026` | ledger |
| `ted-632656-2026` | `ted-581398-2026` | ledger |
| `ted-632683-2026` | `ted-631407-2026` | batch |
| `ted-632699-2026` | `ted-588257-2026` | ledger |
| `ted-632723-2026` | `ted-470387-2026` | ledger |
| `ted-632787-2026` | `ted-630804-2026` | batch |
| `ted-632855-2026` | `ted-580004-2026` | ledger |
| `ted-633183-2026` | `ted-555036-2026` | ledger |
| `ted-633374-2026` | `ted-461180-2026`, `ted-477824-2026`, `ted-522836-2026`, `ted-560780-2026`, `ted-568558-2026`, `ted-617274-2026` | ledger |
| `ted-633463-2026` | `ted-609630-2026` | ledger |
| `ted-633645-2026` | `ted-580691-2026` | ledger |
| `ted-633648-2026` | `ted-587847-2026` | ledger |
| `ted-633846-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026`, `ted-607320-2026`, `ted-615022-2026` | ledger |
| `ted-633902-2026` | `ted-501624-2026`, `ted-548085-2026`, `ted-565547-2026`, `ted-573544-2026` | ledger |
| `ted-633995-2026` | `ted-599764-2026`, `ted-618677-2026` | ledger |
| `ted-634211-2026` | `ted-573011-2026` | ledger |
| `ted-634522-2026` | `ted-580642-2026`, `ted-614675-2026` | ledger |
| `ted-634730-2026` | `ted-490911-2026`, `ted-531770-2026`, `ted-558714-2026` | ledger |
| `ted-634932-2026` | `ted-612350-2026` | ledger |
| `ted-634994-2026` | `ted-609844-2026` | ledger |
| `ted-635241-2026` | `ted-474256-2026`, `ted-476658-2026` | ledger |
| `ted-635334-2026` | `ted-625066-2026` | batch |
| `ted-635478-2026` | `ted-583736-2026` | ledger |
| `ted-635589-2026` | `ted-596674-2026` | ledger |
| `ted-635634-2026` | `ted-536370-2026` | ledger |
| `ted-635731-2026` | `ted-563945-2026` | ledger |
| `ted-635761-2026` | `ted-520860-2026` | ledger |
| `ted-635857-2026` | `ted-536674-2026`, `ted-557056-2026` | ledger |
| `ted-635923-2026` | `ted-472646-2026`, `ted-472926-2026`, `ted-473245-2026`, `ted-474329-2026`, `ted-475305-2026` | ledger |
| `ted-636018-2026` | `ted-482102-2026`, `ted-482381-2026`, `ted-483079-2026`, `ted-483582-2026`, `ted-483771-2026`, `ted-514443-2026`, `ted-610802-2026` | ledger |
| `ted-636102-2026` | `ted-491535-2026` | ledger |
| `ted-636149-2026` | `ted-482102-2026`, `ted-482381-2026`, `ted-483079-2026`, `ted-483582-2026`, `ted-483771-2026`, `ted-514443-2026`, `ted-610802-2026` | ledger |
| `ted-636167-2026` | `ted-574236-2026` | ledger |
| `ted-636353-2026` | `ted-487634-2026`, `ted-503215-2026`, `ted-543649-2026`, `ted-595167-2026` | ledger |
| `ted-636454-2026` | `ted-462205-2026`, `ted-506264-2026`, `ted-575036-2026`, `ted-596380-2026` | ledger |
| `ted-636481-2026` | `ted-482102-2026`, `ted-482381-2026`, `ted-483079-2026`, `ted-483582-2026`, `ted-483771-2026`, `ted-514443-2026`, `ted-610802-2026` | ledger |
| `ted-636507-2026` | `ted-501380-2026` | ledger |
| `ted-636609-2026` | `ted-539476-2026`, `ted-548770-2026`, `ted-565313-2026`, `ted-573848-2026`, `ted-594704-2026` | ledger |
| `ted-636731-2026` | `ted-472646-2026`, `ted-472926-2026`, `ted-473245-2026`, `ted-474329-2026`, `ted-475305-2026` | ledger |
| `ted-636732-2026` | `ted-524356-2026`, `ted-587652-2026` | ledger |
| `ted-636746-2026` | `ted-554275-2026`, `ted-589691-2026` | ledger |
| `ted-636960-2026` | `ted-472646-2026`, `ted-472926-2026`, `ted-473245-2026`, `ted-474329-2026`, `ted-475305-2026` | ledger |
| `ted-636992-2026` | `ted-636061-2026` | batch |
| `ted-637003-2026` | `ted-614651-2026` | ledger |
| `ted-637019-2026` | `ted-599832-2026` | ledger |
| `ted-637063-2026` | `ted-635928-2026` | batch |
| `ted-637208-2026` | `ted-472646-2026`, `ted-472926-2026`, `ted-473245-2026`, `ted-474329-2026`, `ted-475305-2026` | ledger |
| `ted-637291-2026` | `ted-472422-2026`, `ted-494241-2026`, `ted-517185-2026`, `ted-535160-2026`, `ted-551220-2026`, `ted-561906-2026` | ledger |
| `ted-637361-2026` | `ted-567342-2026` | ledger |
| `ted-637497-2026` | `ted-471761-2026`, `ted-479736-2026`, `ted-490749-2026`, `ted-505800-2026`, `ted-532517-2026`, `ted-555812-2026`, `ted-565673-2026`, `ted-576774-2026`, `ted-585277-2026`, `ted-596315-2026`, `ted-611059-2026` | ledger |
| `ted-637509-2026` | `ted-634041-2026` | batch |
| `ted-637562-2026` | `ted-615135-2026` | ledger |
| `ted-637656-2026` | `ted-586634-2026` | ledger |
| `ted-637796-2026` | `ted-524356-2026`, `ted-587652-2026` | ledger |
| `ted-637847-2026` | `ted-597559-2026`, `ted-605940-2026` | ledger |
| `ted-637856-2026` | `ted-559580-2026` | ledger |
| `ted-637982-2026` | `ted-617218-2026` | ledger |
| `ted-638011-2026` | `ted-627221-2026` | batch |
| `ted-638058-2026` | `ted-595964-2026` | ledger |
| `ted-638301-2026` | `ted-466905-2026`, `ted-548527-2026`, `ted-573412-2026`, `ted-606562-2026` | ledger |
| `ted-638323-2026` | `ted-478897-2026`, `ted-504125-2026`, `ted-517249-2026`, `ted-521152-2026`, `ted-552744-2026`, `ted-558447-2026`, `ted-604816-2026` | ledger |
| `ted-638604-2026` | `ted-583857-2026`, `ted-613727-2026` | ledger |
| `ted-638649-2026` | `ted-580642-2026`, `ted-614675-2026` | ledger |
| `ted-638707-2026` | `ted-568386-2026`, `ted-591617-2026` | ledger |
| `ted-638764-2026` | `ted-553426-2026` | ledger |
| `ted-638766-2026` | `ted-515641-2026`, `ted-601067-2026` | ledger |
| `ted-638862-2026` | `ted-574737-2026` | ledger |
| `ted-638941-2026` | `ted-482102-2026`, `ted-482381-2026`, `ted-483079-2026`, `ted-483582-2026`, `ted-483771-2026`, `ted-514443-2026`, `ted-610802-2026` | ledger |
| `ted-638952-2026` | `ted-602413-2026` | ledger |
| `ted-638990-2026` | `ted-508349-2026`, `ted-543828-2026`, `ted-555974-2026`, `ted-574625-2026` | ledger |
| `ted-639240-2026` | `ted-494524-2026` | ledger |
| `ted-639270-2026` | `ted-596347-2026` | ledger |
| `ted-639283-2026` | `ted-482102-2026`, `ted-482381-2026`, `ted-483079-2026`, `ted-483582-2026`, `ted-483771-2026`, `ted-514443-2026`, `ted-610802-2026` | ledger |
| `ted-639338-2026` | `ted-530977-2026`, `ted-599338-2026`, `ted-609548-2026` | ledger |
| `ted-639398-2026` | `ted-482102-2026`, `ted-482381-2026`, `ted-483079-2026`, `ted-483582-2026`, `ted-483771-2026`, `ted-514443-2026`, `ted-610802-2026` | ledger |
| `ted-639412-2026` | `ted-598739-2026` | ledger |
| `ted-639549-2026` | `ted-600583-2026` | ledger |
| `ted-639550-2026` | `ted-577044-2026` | ledger |
| `ted-639838-2026` | `ted-542663-2026`, `ted-564075-2026` | ledger |
| `ted-640013-2026` | `ted-549644-2026` | ledger |
| `ted-640251-2026` | `ted-620298-2026` | batch |
| `ted-640258-2026` | `ted-538958-2026` | ledger |
| `ted-640381-2026` | `ted-606988-2026` | ledger |
| `ted-640431-2026` | `ted-617617-2026` | ledger |
| `ted-640438-2026` | `ted-539476-2026`, `ted-548770-2026`, `ted-565313-2026`, `ted-573848-2026`, `ted-594704-2026` | ledger |
| `ted-640562-2026` | `ted-597982-2026` | ledger |
| `ted-640568-2026` | `ted-563059-2026` | ledger |
| `ted-640580-2026` | `ted-528227-2026`, `ted-555065-2026` | ledger |
| `ted-640693-2026` | `ted-471282-2026` | ledger |
| `ted-640810-2026` | `ted-591418-2026` | ledger |
| `ted-640862-2026` | `ted-634041-2026` | batch |
| `ted-640981-2026` | `ted-499305-2026` | ledger |
| `ted-641001-2026` | `ted-531076-2026`, `ted-531435-2026` | ledger |
| `ted-641271-2026` | `ted-543957-2026`, `ted-583079-2026`, `ted-590399-2026`, `ted-598886-2026`, `ted-605495-2026`, `ted-608251-2026`, `ted-614775-2026` | ledger |
| `ted-641320-2026` | `ted-591590-2026` | ledger |
| `ted-641354-2026` | `ted-554184-2026`, `ted-576756-2026` | ledger |
| `ted-641404-2026` | `ted-524356-2026`, `ted-587652-2026` | ledger |
| `ted-641424-2026` | `ted-602131-2026`, `ted-606455-2026` | ledger |
| `ted-641475-2026` | `ted-590480-2026` | ledger |
| `ted-641532-2026` | `ted-637037-2026` | batch |
| `ted-641794-2026` | `ted-641323-2026` | batch |
| `ted-642250-2026` | `ted-640647-2026` | batch |
| `ted-642266-2026` | `ted-574737-2026` | ledger |
| `ted-642362-2026` | `ted-610377-2026` | ledger |
| `ted-642384-2026` | `ted-557774-2026` | ledger |
| `ted-642641-2026` | `ted-573542-2026` | ledger |
| `ted-642806-2026` | `ted-554010-2026` | ledger |
| `ted-642813-2026` | `ted-473036-2026` | ledger |
| `ted-642898-2026` | `ted-637714-2026` | batch |
| `ted-642982-2026` | `ted-577131-2026` | ledger |
| `ted-643111-2026` | `ted-610263-2026` | ledger |
| `ted-643165-2026` | `ted-591418-2026` | ledger |
| `ted-643203-2026` | `ted-491841-2026` | ledger |
| `ted-643276-2026` | `ted-514239-2026` | ledger |
| `ted-643414-2026` | `ted-472797-2026` | ledger |
| `ted-643450-2026` | `ted-596690-2026` | ledger |
| `ted-643575-2026` | `ted-472422-2026`, `ted-494241-2026`, `ted-517185-2026`, `ted-535160-2026`, `ted-551220-2026`, `ted-561906-2026` | ledger |
| `ted-643610-2026` | `ted-488911-2026`, `ted-533408-2026`, `ted-540928-2026`, `ted-550874-2026`, `ted-555408-2026`, `ted-568835-2026`, `ted-590021-2026`, `ted-593753-2026`, `ted-600559-2026`, `ted-618373-2026` | ledger |
| `ted-643781-2026` | `ted-500909-2026` | ledger |
| `ted-644086-2026` | `ted-615006-2026` | ledger |
| `ted-644102-2026` | `ted-543957-2026`, `ted-583079-2026`, `ted-590399-2026`, `ted-598886-2026`, `ted-605495-2026`, `ted-608251-2026`, `ted-614775-2026` | ledger |
| `ted-644156-2026` | `ted-591740-2026` | ledger |
| `ted-644247-2026` | `ted-576655-2026` | ledger |
| `ted-644284-2026` | `ted-515998-2026` | ledger |
| `ted-644301-2026` | `ted-539598-2026`, `ted-563658-2026`, `ted-586240-2026`, `ted-601708-2026`, `ted-614413-2026` | ledger |
| `ted-644325-2026` | `ted-588762-2026`, `ted-609303-2026` | ledger |
| `ted-644400-2026` | `ted-612337-2026` | ledger |
| `ted-644544-2026` | `ted-587950-2026` | ledger |
| `ted-644697-2026` | `ted-563956-2026` | ledger |
| `ted-644708-2026` | `ted-567340-2026` | ledger |
| `ted-644728-2026` | `ted-474463-2026`, `ted-592499-2026` | ledger |
| `ted-644804-2026` | `ted-596617-2026` | ledger |
| `ted-644838-2026` | `ted-635588-2026` | batch |
| `ted-644930-2026` | `ted-472373-2026` | ledger |
| `ted-645037-2026` | `ted-639046-2026` | batch |
| `ted-645052-2026` | `ted-617344-2026` | ledger |
| `ted-645080-2026` | `ted-498930-2026` | ledger |
| `ted-645157-2026` | `ted-607500-2026` | batch |
| `ted-645232-2026` | `ted-505333-2026`, `ted-528288-2026`, `ted-546074-2026` | ledger |
| `ted-645328-2026` | `ted-644891-2026` | batch |
| `ted-645454-2026` | `ted-478517-2026` | ledger |
| `ted-645471-2026` | `ted-581754-2026` | ledger |
| `ted-645549-2026` | `ted-480818-2026` | ledger |
| `ted-645570-2026` | `ted-573523-2026` | ledger |
| `ted-645625-2026` | `ted-574737-2026` | ledger |
| `ted-645657-2026` | `ted-579175-2026` | ledger |
| `ted-645794-2026` | `ted-610550-2026` | ledger |
| `ted-645808-2026` | `ted-477579-2026`, `ted-507989-2026`, `ted-519602-2026`, `ted-538178-2026`, `ted-558024-2026`, `ted-581728-2026`, `ted-603543-2026`, `ted-606067-2026` | ledger |
| `ted-645942-2026` | `ted-577636-2026` | ledger |
| `ted-646181-2026` | `ted-462999-2026` | ledger |
| `ted-646352-2026` | `ted-596347-2026` | ledger |

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

## Unmapped payloads

No registry feed claims these files, so nothing parsed them. They are named here rather than dropped silently:

- `manifest-demand.md`
- `manifest-dotace.md`
- `manifest-funded.md`
- `manifest-regulation.md`

---

# Weekly attended scans, 2026-09-19 (four feeds, run in parallel)

Folded from the four per-feed manifests written by the parallel scan agents. Records landed by the coordinator with `normalize.py --complete` per feed subdirectory (regulation +4, tenders +1, funded +8, demand 0), committed in 060063d.

---

## demand-scan pass — 2026-09-19 (weekly delta pass)

This is the weekly delta pass of feed `demand-scan` (evidence_type `demand`), run one day
after the monthly BROAD pass of 2026-09-18 (`data/raw/2026-09-18/manifest.md`, demand
section). It follows pipeline/SCANS.md: every checklist source was walked. The window it
looked for was **items published since 2026-09-17**, plus everything the 2026-09-18 pass
named as owed.

Other agents and a scripted ingest write the same raw date, so this pass kept to its own
paths: payloads and `staged.jsonl` under `data/raw/2026-09-19/demand/`, plus this file.
It made no ledger write, no seen.txt write, no DB write, no feeds.json edit and no git
state change.

### Hand-off

- `data/raw/2026-09-19/demand/staged.jsonl` is **empty (0 records)**. Zero new records is
  the honest outcome of this checklist walk. Nothing in the demand remit was published
  between 2026-09-17 and 2026-09-19.
- The dry run against a SCRATCH COPY of `data/signals` (`$TMPDIR/demand-sim/signals`, same
  corpus, seen.txt 17,203 ids) printed:
  `normalize --complete --dry-run: would append 0 records across 0 file(s); 0 dropped by
  materiality; 0 incomplete; 0 refused by AC-GDPR1. dedup by identity key (append): 0 skipped`.
- The coordinator has no `--complete` or `db.py upsert` to run for this feed.

### Checklist source 1 — NKÚ kontrolní závěry (parse the PDFs)

**Visited. Nothing new since the 2026-09-18 pass.**

- RSS `https://nku.cz/cz/rss.xml`: **200**, 13,142 B (`demand/nku-rss.xml`). The newest item
  is **15 Sep 2026**, three job adverts (id15902/15908/15909). The newest audit item is
  still the IKEM press release of **14 Sep 2026** (id15897). The 2026-09-18 pass already
  read its conclusion (k25014) and minted it as `nku-ikem-hospodareni`. The RSS has
  **no item dated 16–19 September**.
- Věstník index `https://www.nku.cz/cz/publikace-a-dokumenty/vestnik/`: **200**, 41,328 B.
  The newest issue is still **částka 3/2026** (13 Aug 2026). There is no 4/2026.
- Conclusion-PDF existence probe `https://www.nku.cz/assets/kon-zavery/kNNNNN.pdf`:
  - 200: k25015, k25016, k25020, k25021.
  - 404: k25018, k25019, k25022–k25027, k26001–k26008.
  - **k25024 is still 404.** That is the item the 2026-09-18 pass named: the revitalisation
    of public spaces conclusion, approved by the 13th Kolegium on 7 Sep 2026.
- **k25015 / k25016 / k25020 / k25021 were re-read, and none was minted.** They are the
  2025 closing-account audits:
  - ÚOOÚ: Last-Modified 27 Jul 2026.
  - ČSÚ: Last-Modified 3 Aug 2026.
  - AV ČR: Last-Modified 3 Aug 2026.
  - Úřad práce: Last-Modified 10 Aug 2026.

  All four predate the window. The 2026-09-03 demand pass already decided them (see
  `data/raw/2026-09-03/manifest-demand-scan.md`). 25/21 is held as
  `nku-up-ucetni-zaverka-2025`. 25/15, 25/16 and 25/20 were dropped by the pain-language
  bar: clean audits, errors corrected before closing, no systemic finding. This pass
  keeps that decision. PDFs and `pdftotext -layout` output are saved as
  `demand/nku-k250{15,16,20,21}.{pdf,txt}`.
- Access note: the press-release listing `https://www.nku.cz/cz/pro-media/tiskove-zpravy/`
  answers **403** to curl, and `.../pro-media/jednani-kolegia/` answers **404**. The RSS
  carries the same items and was the working surface, so this is not a gap.
- **Owed, still open:** k25024.pdf. A future pass owes it a re-probe, and the Věstník
  4/2026 when it appears.
- **For the coordinator, scripted `nku` feed.** Today's run manifest shows the scripted
  `nku` feed has not run since 2026-09-08. The headline twins the 2026-09-18 pass flagged
  are therefore still unheld:
  - `nku-15872` (25/13 press release) is still pending in
    `data/raw/2026-09-08/staged.jsonl`.
  - The IKEM press release id15897 has not been fetched.

  If either lands, it is the same audit as `nku-zdravotnicky-vyzkum` or
  `nku-ikem-hospodareni`. Its url is different, so identity-key dedup will not catch it.

### Checklist source 2 — European Semester CZ package

**Visited. Nothing new. The gap carried from 2026-09-18 is now CLOSED.**

- Landing page
  `https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages-including-country-reports/country-report-czechia_en`:
  **200**, 74,780 B (`demand/ecsem-landing.html`). Its stripped text is byte-identical to
  the 2026-09-18 capture. The newest item is still the **2026 Country Report of 3 June 2026**,
  already held as `ecsem-cz2026-housing`, `-admin-burden` and `-ltc-mix`.
- **OJ C reference for the Council's Czechia CSR of 10 July 2026: FOUND.** The route was
  the Publications Office CELLAR SPARQL endpoint
  `https://publications.europa.eu/webapi/rdf/sparql` (200), which is the official machine
  route the reg-scan pass documented, not the EUR-Lex WAF challenge. Result:
  - CELEX **32026H03916**, "Council Recommendation of 10 July 2026 on the economic,
    social, employment, structural and budgetary policies of Czechia".
  - ELI `http://data.europa.eu/eli/C/2026/3916/oj`.
  - **Published in OJ C on 2026-09-01** (C/2026/3916).

  Receipts: `demand/ecsem-cellar-cz-2026h2.{rq,json}` and
  `demand/ecsem-cellar-32026H03916.json`. As the 2026-09-18 pass directed, this belongs
  in a **note on `ecsem-cz2026-csr`**, not in a new record. The ledger is append-only and
  this pass does not write it, so the coordinator decides whether a note is added. The
  source url stays as it is.
- The same query found two more CZ Semester-framework documents. Neither is a demand pain
  signal and neither was minted:
  - 52026DC0414 (23 Jul 2026), the Commission recommendation endorsing CZ's medium-term
    fiscal-structural plan 2027–2030 and the national escape clause.
  - 52026SC0903 (17 Jul 2026), the Rule of Law Report CZ chapter.

  Both predate the window. The fiscal-plan item is fiscal-policy content and is noted
  for reg-scan's attention.

### Checklist source 3 — MPSV Statistická ročenka, chapter 5 "Sociální služby"

**Visited. EXPECTED ABSENCE (not yet published).**

- `https://mpsv.gov.cz/statisticka-rocenka-z-oblasti-prace-a-socialnich-veci-archiv`:
  **200**, 1,325,956 B (`demand/mpsv-rocenka-archiv.html`). The newest edition is still
  *Statistická ročenka z oblasti práce a soc. věcí v roce 2024* (`.7z`). That listing is
  the positive control that the page parses. The string "v roce 2025" appears **0** times.
- The non-archive URL `.../statisticka-rocenka-z-oblasti-prace-a-socialnich-veci` → 404,
  so the archive page is the only surface.
- **Owed:** the next pass re-checks it. When the 2025 edition lands, compare tab 5.9
  against 70,209 DS / 37,849 DZR / 4,043 (`civic-mpsv-rocenka-neuspokojene-2024`).
  Remember the mpsv- trap: file it under `civic-`.

### Checklist source 4 — Ombudsman ESO (HTML walk, no RSS)

**Visited. Nothing new since the 2026-09-18 pass. The positive control passed.**

- `https://www.ochrance.cz/eso/zpravy/`: **200**, 14,386 B. The page is still the taxonomy
  explainer. Its stripped text is identical to the 2026-09-18 capture.
- Search app `https://eso.ochrance.cz/`, using the session-bound method the 2026-09-18
  pass documented (cookie jar → `POST /Vyhledavani/Search` → `POST
  /Nalezene/GetPocetVysledku` → `POST /Nalezene/GetTableContent`). New note:
  GetPocetVysledku needs an explicit empty body (`--data ""`). A bare `-X POST` gets
  **HTTP 411**.
  - **Positive control** `FormaZjisteni=22` (§ 21c summary visit reports): **41 hits**,
    the same as 2026-09-18. The newest is still 27/2023/NZ (19.07.2024).
  - **Everything with DatumVydaniOd=01.06.2026**: **43 hits**. That is the **same 43
    documents** as the 2026-09-18 capture, compared by ESO item id, with zero additions.
    Two rows carry future issue dates (6160/2025/VOP Odložení 21.10.2026 and
    4474/2025/VOP § 17 25.09.2026). Both were already in yesterday's set, both are
    single-case items (scale 0), and neither is minted.
  - **Item-id frontier:** `/Nalezene/Edit/15064` → 200 (1177/2025/VOP, the newest
    document yesterday as well). 15065, 15066, 15068, 15070, 15075, 15080 and 15090 all
    → **500**. **No document has been added to ESO since the 2026-09-18 pass.**
- Research reports (type 29): none new. The 2026-09-18 pass minted the 4 found since 2025
  (3 minted, 1 dropped).
- Quarterly reports: Q3 2026 is not due until after 30 Sep 2026. Expected absence;
  `ombud-q2-2026` is still the newest.
- Aktuálně `https://www.ochrance.cz/aktualne/`: **200**, 47,389 B. The newest item is
  **15 Sep 2026**, a job advert. **Nothing dated 16–19 September.** Nothing minted.
- Payloads: `demand/eso-search-{ctrl22,since0601}.html`,
  `demand/eso-table-{ctrl22,since0601}-p{1,2}.html`, `demand/eso-edit-15064.html`,
  `demand/eso-edit-15065-500.html`, `demand/ombud-eso-zpravy.html`,
  `demand/ombud-aktualne-1.html`.

### Records

None. `staged.jsonl` is empty.

### Dedup

- seen.txt holds 17,203 ids. No id was minted, so there was nothing to collide.
- Checked for the re-read items:
  - k25021 is held (`nku-up-ucetni-zaverka-2025`).
  - k25015, k25016 and k25020 are in no ledger, by the recorded 2026-09-03 decision.
  - The OJ C/2026/3916 reference appears in no ledger (the grep hits were unrelated
    numbers in tenders ledgers).

### Candidates for MATCH

- No new candidates this pass.
- Carried from 2026-09-18, still open for MATCH:
  - The delegated-agenda burden in small municipalities (`ombud-male-obce-statni-sprava`
    with `reg-verejne-opatrovnictvi-prenos-2027`).
  - Healthcare complaint investigation capacity (`ombud-stiznosti-zdravotnictvi`).

### Coverage gaps

- **Carried, still open:** NKÚ 25/24 (revitalisation of public spaces). Approved
  7 Sep 2026; k25024.pdf is still 404.
- **Closed this pass:** the OJ C reference for the 2026 CZ CSR (C/2026/3916, OJ C
  2026-09-01, via CELLAR SPARQL).
- **Expected absences, not gaps:**
  - MPSV ročenka 2025: not yet published.
  - Ombudsman Q3 2026 quarterly report: not due.
- **Outside this feed's remit, flagged:** the scripted `nku` feed has not run since
  2026-09-08. The IKEM press release id15897 is unfetched and `nku-15872` is still
  pending.

### Pass summary

```
feed:                     demand-scan (weekly delta pass, evidence_type demand, 1 day after the 2026-09-18 broad pass)
checklist sources:        4 of 4 visited (NKU / European Semester / MPSV rocenka / ombudsman ESO); ESO positive control passed (41)
records staged:           0  (nothing in the remit published 2026-09-17..19; dry run 0 incomplete / 0 refusals)
coverage gaps named:      1 carried (NKU 25/24, k25024.pdf 404) · 1 closed (OJ C/2026/3916 for the CZ CSR) · 2 expected absences (MPSV 2025, Q3)
rotation state:           n/a — category rotation is arb-scan's duty
```

---

## reg-scan pass — 2026-09-19 (weekly delta)

Weekly DELTA pass of `reg-scan` (feed row: `evidence_type` regulation, `source` `reg-scan`,
`id_prefixes` ["reg"], runner attended), one day after the monthly BROAD pass of 2026-09-18
(`data/raw/2026-09-18/manifest-regulation.md`). Operating file: `pipeline/SCANS.md`, reg-scan
checklist items 1–4. The main job this pass was checklist item 4: the RIA "Definice problému"
reading owed for the 19 `veklep-` records the scripted feed appended today
(`data/signals/regulation/2026-09-19.jsonl`).

Run in parallel with other scans on the same raw date, so it wrote only to
`data/raw/2026-09-19/regulation/` and this file. **Nothing was written to `data/signals/**`,
`seen.txt`, `register.db`, `data/problems/**` or `feeds.json`.** No `db.py` call. No git.

**Records staged: 4, all `reg-` prefixed, `source: reg-scan`, `extraction: manual`, each with a
quote verified as a literal substring of the whitespace-collapsed payload text.** File:
`data/raw/2026-09-19/regulation/staged.jsonl`. They are NOT appended; the coordinator runs the
real `--complete`.

| id | instrument | status | date | payload |
|---|---|---|---|---|
| `reg-uhradova-2027-centrove-leky-slevy` | MZd reimbursement decree for 2027 (VeKLEP ALBSDXRFYLM6) | draft, comment procedure | 2027-01-01 | `veklep/zd_ALBSDXRFYLM6.docx` (+ `ma_` for the effect clause) |
| `reg-rud-bytova-vystavba-2028` | MPs' bill, tax revenue sharing act 243/2000, tisk 298 (VeKLEP KORNDXQH9BRI) | draft, MPs' bill | 2028-01-01 | `veklep/ma_KORNDXQH9BRI.pdf` |
| `reg-odstoupit-tlacitko-159-2026` | Act 159/2026 Sb. (Dir. 2023/2673 transposition) | ENACTED | 2027-01-01 | `esbirka/sb-2026-159.txt` |
| `reg-eu-customs-code-2026-2108` | Regulation (EU) 2026/2108, new Union Customs Code | ENACTED (OJ 19 Sep 2026) | 2027-09-21 | `eu/32026R2108-en.html` |

### Registry changes needed

**None.** `reg-` prefix and `source: reg-scan` only. No `veklep-` id minted.

### Access notes (measured today)

- **ODok moved host.** `https://www.odok.cz/portal/services/download/attachment/<ID>/` now
  answers **HTTP 302 to `https://www.odok.gov.cz/...`**. A sandboxed curl that only allows
  `www.odok.cz` gets the 302 and an empty body. The descriptive UA from 2026-09-18
  (`localproblems-reg-scan/1.0 (+https://localproblems.vercel.app)`) still gets HTTP 200 with the
  real `.docx`/`.pdf` from `www.odok.gov.cz`. Two downloads failed once with "Error in the HTTP2
  framing layer" and succeeded on retry with `--http1.1`. **Scripted-feed implication:** any
  fetcher that pins `www.odok.cz` without following redirects will save a 0-byte payload.
  Record urls keep the `www.odok.cz` form that the corpus already uses; it still resolves.
- **VeKLEP metadata** was read from the scripted feed's own payload
  (`data/raw/2026-09-19/veklep-p1..p6.json` in the main checkout), not re-fetched, as SCANS.md
  item 4 requires. 125 distinct materials; the 19 appended ids were matched by `Id`.
- **e-Sbírka ELI open data** worked as on 2026-09-18. The fragment fetcher hit a transient
  proxy `BadStatusLine` on a 6-thread run; 2 threads worked.
- **EUR-Lex** was not tried directly (the WAF challenge is documented on 2026-09-18). The
  CELLAR SPARQL endpoint and CELEX content negotiation both worked.

---

### Checklist source 1 — Programové prohlášení vlády + semi-annual fulfilment evaluations

**Visited, nothing new since 2026-09-18.** The programme page (HTTP 200) still carries one
attachment (the January 2026 PDF); an attachment diff against yesterday's capture found no new
file. The vlada.gov.cz RSS (16 items to 18 Sep 15:4x) holds no fulfilment evaluation. New
items since yesterday's read: the **21 Sep 2026 government meeting** notice (`vlada-228883.html`:
2027 state budget, SFDI/SFPI budgets, the sport-support act amendment `veklep-ALBSDW3HDEWG`,
and the 2027 state-insured-person payment). The payment it names is the input the 2027
reimbursement decree already assumes, a 13bn CZK one-off raise plus 3bn CZK from more insured
persons (see `reg-uhradova-2027-centrove-leky-slevy` notes). **No dated duty, so no record.**
The carried gap is unchanged: there is no machine-readable fulfilment evaluation; the next one is
expected around January 2027.

### Checklist source 2 — Plán legislativních prací vlády 2026

**Visited, nothing new since 2026-09-18.** The plan page (HTTP 200) is unchanged: the same
2 annexes, dated 23. 3. 2026 (attachment diff against yesterday's capture). Annex 1 and
annex 2 were read in full on 2026-09-18. No re-read was owed.

### Checklist source 3 — e-Sbírka and EUR-Lex (items since 2026-09-18)

**e-Sbírka — visited.**
- **Newest act is still 167/2026 Sb.** Numbers 168–175 return the 768-byte prefix-only shell
  (`esbirka/esbirka-2026-168-175-empty.json`, `eli-2026-168.ttl`, `eli-2026-170.ttl`).
  Positive control: 167/2026 returns its versions 2026-09-16 and 2026-10-01 in the same run.
- **Yesterday's named gap: the 5 "právě digitalizujeme" stubs were re-read. 4 of 5 are now closed.**
  - **159/2026 is RECORDED** as `reg-odstoupit-tlacitko-159-2026`. It is the Czech
    transposition of Directive 2023/2673, in force 1 Jan 2027. The new Civil Code § 1830a
    sits in the **general** distance-contract rules, so the withdrawal button applies to every
    e-shop and not only to finance. A missing button becomes a consumer-protection offence.
  - **155/2026** ("některé zákony v oblasti veřejných rozpočtů", in force 2026-08-29 and
    2027-01-01) was read in full. **Not recorded, as state-internal.** It covers the NKÚ act,
    budget rules, RUD, the fiscal-responsibility act, the conflict-of-interest act and defence
    financing. It also moves state financing for the new nuclear source (Act 367/2021 § 4)
    to per-investment off-budget accounts at ČNB, with a 2 % minimum rate.
  - **154/2026** is an MZd decree on sports medical fitness. **157/2026** is the Chamber's rules
    of procedure. Neither is recorded, as neither puts a duty on businesses.
  - **166/2026 is still a stub.** A future pass owes it one more re-read.
- **Status change, not recorded:** the EET 2.0 act (sněmovní tisk 189, senátní tisk 270) was
  **signed by the President on 17 Sep 2026** (psp.cz history, `psp-tisk189.html`). The
  Chamber overrode the Senate on 9 Sep. It has **no Sbírka number yet**, since 168 is still
  empty. The corpus already holds it as `reg-eet2-2027` and `reg-mf-eet2-2027`. **The next
  pass owes it its Sbírka number and in-force date.**
- **Yesterday's named gap: Act 130/2026 (investment companies and funds).** Enumerated today:
  versions 2026-07-23, 2026-09-01 and **2027-04-16**. The 16 Apr 2027 date matches AIFMD II's
  (Dir. 2024/927) second application date. The full text confirms it is the AIFMD II
  transposition; see "Act 130/2026" below.

**EUR-Lex — visited via CELLAR.** Every 32026R/L/D act published 2026-09-17..2026-09-19 was
enumerated (`eu/ojL-pub-2026-09-17_19.rq` / `.csv`, 18 CELEX). New since yesterday's enumeration:
the OJ issues of 18 and 19 Sep.
- **RECORDED: `reg-eu-customs-code-2026-2108`.** Regulation (EU) 2026/2108 of 16 Sep 2026
  establishes the new Union Customs Code and the EU Customs Authority, and repeals Reg.
  952/2013. It was published 19 Sep, enters into force 20 Sep 2026 and applies from
  21 Sep 2027. The per-item e-commerce handling fee applies 10 days after its delegated act.
  Data Hub provisions and Trust and Check self-release apply from 1 Jul 2028. The Data Hub is
  voluntary from 1 Mar 2031 and mandatory by 1 Mar 2034. **Nothing in the corpus covered the
  customs reform:** signals were searched for customs code, customs authority, data hub, deemed
  importer, EUR 150 and IOSS.
- **Not recorded:**
  - Implementing Reg 2026/2133: a provisional safeguard on grain-oriented electrical steel.
    It is trade defence, not a business duty.
  - 2026/2057 (fishing quotas).
  - Feed-additive authorisations: 2026/2061, 2072, 2074, 2076, 2077, 2079.
  - Anti-dumping amendment 2026/2064.
  - 2026/2070: a correction on 2-chloroethanol.
  - 2026/2104: the animal-health entries for the United States.
  - 2026/2106: the PDO Segarcea.
  - Decisions 2026/2059 (rail), 2026/2109 (avian-flu emergency), 2026/2065 (EU–Japan
    agreement) and the EEAS seconded-experts decision.
  - The corrigendum to Delegated Reg 2026/1061 (prospectus format).
  - 2026/2102 was already recorded yesterday as `reg-eudr-annex-i-scope-2027`.
- **No directive** was published in the window: no 32026L rows.
- **Carried gap:** 32026R1739 (farmers' position in the food supply chain) is still unread.

### Checklist source 4 — VeKLEP RIA "Definice problému" for today's 19 scripted-feed items

Input: `data/signals/regulation/2026-09-19.jsonl`, 19 `veklep-*` records. All 19 were opened.
Attachment lists came from the scripted feed's own payload. **Only one of the 19 carries a
separate "Závěrečná zpráva RIA"** (ALBSDXTKB4NK). For the others, the problem statement is the
RIA chapter inside the důvodová zpráva ("Definice problému" appears only in ALBSDXRFYLM6), or
the důvodová zpráva's "Zhodnocení platného právního stavu" / "nezbytnost" sections. The
MPs' bill has no RIA at all. Each důvodová zpráva (`zd_`) was downloaded and read. For
KORNDXQH9BRI, the materiál PDF (bill plus DZ) was read instead.

| veklep id | what the RIA / DZ states | quantified problem? | outcome |
|---|---|---|---|
| `veklep-ALBSDXTKB4NK` innovative & scalable business act | Definice problému: 972 startups with external investment since 2015 (89.2 per million vs Estonia 681), VC 25 USD/capita; 73 % of surveyed startups name tax and financial burden | yes, **already recorded** | **No new record.** The RIA docx is **byte-identical** (`cmp`) to the 2026-09-18 capture, and its Definice problému was recorded yesterday in `reg-startup-evidence-odpocet-2027` (effect 1 Jul 2027, 65M CZK/yr cost floor) |
| `veklep-KORNDXQH4G02` Reg. (EU) 2024/3015 adaptation bill | DZ: labour inspection as competent authority, fines up to 5M CZK, customs pass EORI data | no new quantity | **No new record.** The DZ docx is byte-identical to yesterday's; it is recorded in `reg-nucena-prace-dozor-cz-2027` (effect 14 Dec 2027) |
| `veklep-KORNDXQH9BRI` tax revenue sharing MPs' bill (tisk 298) | DZ 1.3: no direct fiscal reward for completed housing; transfer 8.12–9.90bn CZK/yr on 2024 data; 30,274 flats completed in 2024 | **yes** | **RECORDED: `reg-rud-bytova-vystavba-2028`** |
| `veklep-ALBSDXRFYLM6` 2027 reimbursement decree | Definice problému: no agreement in 3 of 15 segments; system balance +0.2bn on 604.8bn costs; centre-drug purchase gap 4bn (weighted) to 7bn (best practice), indices save 2.2bn | **yes** | **RECORDED: `reg-uhradova-2027-centrove-leky-slevy`** |
| `veklep-KORNDXRBTYB9` 2027 tax-form decrees | forms follow the EET 2.0 act (tisk 189), the VAT amendment (tisk 218), JMHZ and ViDA SVR (partly from 1 Jan 2027) | no | No record. Its parents are already in the corpus (`reg-eet2-2027`, `reg-vida-timeline`, `reg-dph-vida-2027`). This DZ is how the EET signature was spotted (source 3) |
| `veklep-KORNDXRB97TP` property-tax form decree | wording changes only; "nemění rozsah daňové povinnosti" | no | No record |
| `veklep-KORNDXRBYXXJ` customs-administration forms decree | follows the excise changes in Lex Kratom | no | No record (`reg-lex-kratom-2027`) |
| `veklep-KORNDXSH4PXO` NV 361/2007 blood-lead limit | Dir. 2024/869: lets exposed staff keep working under a falling blood-lead trend (≤400 µg/l to 2028, ≤300 from 2029); adds pilots' psychological load; "no new types of duty" | no | No record. It relaxes an existing limit; the population is niche |
| `veklep-KORNDXY9WP89` plant-protection products decree 132/2018 | Implementing Reg. (EU) 2023/564 electronic PPP-use records; 4M CZK for MZe IS changes; effect tied to the plant-health act amendment (tisk 48) | no problem size | No record. **Candidate for a future pass:** the corpus has nothing on the 2023/564 digital spray-record duty for professional users. It needs the tisk 48 act text for a date |
| `veklep-KORNDXYA7F6I` state-administration training decree (ÚKZÚZ) | new route to professional competence; financed from the institute's budget | no | No record |
| `veklep-KORNDXSCDDKR` decree 414/2024, equivalence of officials' education | widens the list of recognised programmes; effect 1 Nov 2026 | no | No record (relief, no duty) |
| `veklep-KORNDXSF6SSH` radon subsidy decree 362/2016 | widens eligibility (radon >500 Bq/m³ plus building-material dose); "units to low tens of thousands" of buildings, only a part eligible; effect 1 Jan 2027 | loose estimate only | No record. It widens a subsidy and imposes no duty; the scale is stated only as an order of magnitude |
| `veklep-KORNDXRHZE97` police-markings decree | new chip ID card model 2026 (cyber-security, NPO-funded) | no | No record |
| `veklep-KORNDXYB4T22` examiner-pay decrees | the 130 CZK/h fee is below the 134.40 CZK/h minimum wage; raised to 1.7× (228.48); cost about 25.5M CZK a year across all founders | yes, but state-internal | No record. It is a public-pay correction with no market problem |
| `veklep-KORNDY2BV728` inland-navigation crew decree 48/2023 | adapts to Del. Reg. (EU) 2026/118 (applies from 1 Jan 2026, published late); removes duplicated rules | no | No record |
| `veklep-KORNDY2BX7OK` toll-section decree 470/2012 | new D3/D6/D7/D35 sections; SFDI +198,549,750 CZK/yr; EC objection on the zero-emission HDV definition | fiscal yield only | No record. The zero-emission HDV redefinition affects a small population |
| `veklep-KORNDY2BWJMB` vignette-section decree 480/2020 | 3 sections added from 1 Jan 2027; RIA waived as parametric | no | No record. **Carried:** yesterday's note that the new vignette *rates* are owed stands. This decree sets sections, not rates |
| `veklep-KORNDTKB9G50` health-education IS decree | access and data scope for a system live since 1 Jan 2026 | no | No record |
| `veklep-ALBSDW3HDEWG` sport-support act | extends the anti-doping committee to match-fixing, safeguarding and spectator violence; CZ has not signed the CoE match-fixing convention (approved for signature in 2016); effect 1 Jan 2027; on the government agenda for 21 Sep | no | No record. It creates an institutional mandate with no dated duty on businesses |

---

### Act 130/2026 (yesterday's named gap): now identified, not recorded

The full text (`regulation/esbirka/sb-2026-130.txt`, 147 kB) cites Directive (EU) 2024/927 twice, so
it **is the AIFMD II / UCITS transposition** into Act 240/2013. Its effect clause reads: first day of
the second month after promulgation (hence 1 Sep 2026), except the points of Art. I listed there,
which take effect on 16 Apr 2027. Open-ended fund managers must also bring their affairs into line
with the new § 37b(1)-(2) and § 465(1) by 16 Apr 2027. **Not recorded this pass.** The duty falls on
a niche population (Czech fund managers and their depositaries), and turning it into a record would
first require reading which duties sit in the 16 Apr 2027 points (liquidity-management tools and loan
origination are the likely ones). **A candidate for the next pass;** the corpus has no AIFMD II
record (searched: AIFMD, 2024/927, 130/2026). This closes yesterday's "unread" gap, and a new, narrower
recording gap takes its place.

### Evidence-bar compliance

- **Enacted vs draft** is stated as `STATUS:` in every record's notes. 2 are ENACTED (159/2026 Sb.,
  Reg. (EU) 2026/2108). 2 are DRAFTS: the reimbursement decree, which the ministry must issue
  every year, and an MPs' bill with no government opinion yet.
- **Dates:** every record's `date` is the effect or application date. Every other date is in
  `notes` with its clause quoted: promulgation, comment deadline, phase-ins, and the Data Hub
  2031/2034 dates.
- **Urgency:**
  - The enacted act in force 1 Jan 2027 scores 3, since it takes effect in under 6 months.
  - The reimbursement decree scores 3 on the same 1 Jan 2027 date. The ministry must issue it
    every year, so the date is not a planning target. This follows the precedent of
    `reg-mzd-uhradova-432-2025` and `reg-lex-kratom-2027`.
  - The RUD bill (1 Jan 2028) and the customs code (21 Sep 2027) score 2, since both dates are
    under 18 months out.
- **Money:** `money_eur` is null on all 4, each with a `money_note`. The RUD transfer range, the
  reimbursement savings estimates and the SFDI toll yield are not budgets attached to the need,
  so none is scored. Nothing was estimated.
- **Quotes:** 4 of 4 are literal substrings of the whitespace-collapsed payload text: the `.docx`
  text extracted with the 2026-09-18 `docx2txt.py`, `pdftotext -layout` of the ODok PDF, the
  e-Sbírka fragment text, and the CELLAR xhtml text. The clauses quoted inside `notes` (effect
  dates) were checked the same way.
- **No absence claim** is made. The one "not in corpus" statement (customs reform) names the
  terms searched.
- **No personal data.** The VeKLEP `adresaPripominek` field was not read into any record. One
  MP appears by name as the bill's first signatory, in office only. A grep of `staged.jsonl`
  for email and phone patterns returned 0.

### Facts in existing records this pass found stale (for MATCH/PROCESS; nothing was edited)

- `reg-dmfsd-distance-finance`: it frames Dir. 2023/2673 as financial-services-only and dates it
  19 Jun 2026. The Czech transposition (159/2026 Sb.) applies **from 1 Jan 2027**, and its
  withdrawal button covers **all online distance contracts** (see `reg-odstoupit-tlacitko-159-2026`).
- `reg-eet2-2027` / `reg-mf-eet2-2027`: the act is now **passed (Chamber override 9 Sep 2026) and
  signed (17 Sep 2026)**. It has no Sbírka number yet.
- `reg-mzd-uhradova-432-2025`: its 2026 decree is superseded from 1 Jan 2027 by the 2027 draft
  (`reg-uhradova-2027-centrove-leky-slevy`).

### Dry run (validation only)

```
cp -R data/signals $TMPDIR/reg-sim/signals
python3 scripts/normalize.py --raw data/raw/2026-09-19/regulation --complete --dry-run --today 2026-09-19 \
    --out-dir $TMPDIR/reg-sim/signals --seen $TMPDIR/reg-sim/signals/seen.txt
  -> would append 4 records across 1 file(s); 0 dropped by materiality; 0 incomplete;
     0 refused by AC-GDPR1; identity-key dedup 0 skipped; allowlist strips evidence_type (routing only)
```

**Owed to the coordinator:** the real `normalize.py --raw data/raw/2026-09-19/regulation --complete`
(it appends to `data/signals/regulation/2026-09-19.jsonl`, the same file the veklep feed wrote
today) and the `db.py upsert` it prints. Nothing was committed.

### Coverage gaps named

1. No machine-readable fulfilment evaluation of the government programme exists (carried; recheck
   around January 2027).
2. e-Sbírka 166/2026 is still a digitisation stub (4 of yesterday's 5 are closed).
3. EET 2.0: signed 17 Sep 2026, but has no Sbírka number yet. The next pass owes it the enactment
   number and in-force date.
4. 32026R1739 (farmers' position in the food supply chain) is still unread (carried).
5. Act 130/2026 (AIFMD II transposition, phase 16 Apr 2027): identified, not yet recorded.
6. Implementing Reg. (EU) 2023/564 digital spray records: no corpus record. It needs the plant-health
   act (sněmovní tisk 48) for its Czech date.
7. The 2027 motorway-vignette rates are still unrecorded (carried; today's decree covers sections only).

### 5-line pass summary

```
feed:                reg-scan (evidence_type regulation, prefix reg-, weekly delta pass)
checklist sources:   4 of 4 visited (programme + evaluations: nothing new · plan 2026: unchanged · e-Sbírka (168–175 empty, 4 stubs re-read, 130/2026) + EUR-Lex via CELLAR 09-17..19 · VeKLEP: all 19 surfaced ids read)
records staged:      4 (1 RIA-derived, 1 MPs'-bill DZ-derived, 1 e-Sbírka, 1 EU), dry-run clean, not appended
coverage gaps named: 7 (see list above)
rotation state:      n/a (arb-scan duty)
```

---

## dotace-scan pass: weekly delta, 2026-09-19

This is the weekly delta for the `dotace-scan` feed (`data/feeds.json` key `dotace-scan`,
`signal_source: dotace`, `evidence_type: tenders`, `id_prefixes: ["dotace"]`). It runs one
day after the monthly broad pass of 2026-09-18 and follows `pipeline/SCANS.md` (CHECKLIST
LAW). Worktree: `localproblems-weekly-2026-09-19`, branch `weekly/2026-09-19`.
Raw captures are in `data/raw/2026-09-19/dotace/` (27 page captures under `pages/`). The
staged record is in `data/raw/2026-09-19/dotace/staged.jsonl`.
This pass did not write `data/signals/**`, `seen.txt`, `data/errata.jsonl`,
`data/problems/**`, `feeds.json` or `register.db`. It ran no `db.py` and no state-changing git.

### Exchange rate

**24.340 CZK/EUR**, ČNB list **#181 of 18.09.2026**. Both
`denni_kurz.txt?date=18.09.2026` and `?date=19.09.2026` returned HTTP 200. The 19.09 request
returns the 18.09 list, because 19 September is a Saturday and has no fixing. Both payloads
are saved as `cnb-denni_kurz-18.09.2026.txt` and `cnb-denni_kurz-19.09.2026.txt`, and both
contain `EMU|euro|1|EUR|24,340`. This is the rate the 2026-09-18 pass used.

### Checklist source 1: MS2021+ open-data call list

- **Fetch.** `https://ms21opendata.mssf.cz/SeznamVyzev_21_27.xml` returned **HTTP 200,
  1,669,848 bytes** at 2026-09-19T08:17:32Z. The payload carries
  `DATE="2026-09-18T20:45:00.000+02:00"`, one nightly export after yesterday's.
- **Snapshot.** Today's file is saved as `data/raw/2026-09-19/dotace/ms21-SeznamVyzev_21_27.xml`
  (sha256 prefix `2a518771ad6f3229`). **The next pass diffs against this file.**
- **Left-hand side.** The 2026-09-18 snapshot at
  `localproblems/data/raw/2026-09-18/dotace/ms21-SeznamVyzev_21_27.xml` (payload DATE
  2026-09-17T20:45, 817 codes). Note that it lives in the main checkout, which is uncommitted
  there. This worktree has no `data/raw/2026-09-18/dotace/`.
- **Method.** A per-call field diff: every leaf field of every `<VYZVA>`, keyed by `KOD`. It
  covers both the code diff and the state/date/allocation diff that the 2026-09-18 pass said
  is the one that finds new calls. The output is saved as `ms21-diff-2026-09-18-vs-19.txt`.

**Result: 817 → 817 codes. Added 0, removed 0. Five codes changed:**

| KOD | change | in the ledger? | outcome |
|---|---|---|---|
| `06_22_056` | DATUMUZAVRENI 2026-11-13 → **2027-01-14** | no, it was on the 2026-09-18 owed backlog | **minted** `dotace-irop-56-57-akutni-psychiatrie` |
| `06_22_057` | DATUMUZAVRENI 2026-11-13 → **2027-01-14** | no, same backlog | folded into the same record |
| `06_22_070` | STAV Otevřená → **Pozastavená** (IROP 70, culture: monuments and museums, CLLD) | no | not minted: CLLD heritage envelope, not builder-relevant. irop.gov.cz still shows *Otevřená* today, so the XML is ahead of the portal |
| `06_24_116` | ALOKACECELKEM 1,242,210,050 → **124,210,050** (IROP 116, Sociální bydlení II, closed 2026-08-31) | no | not minted (closed). **Corrects the 2026-09-18 manifest**, see "Errata candidates" |
| `08_26_036` | NAZEV: a line break inside the title became a space | yes, `dotace-oprybarstvi-36-investice-akvakultura` | whitespace only. The record's quote (whitespace-collapsed) is unaffected. Nothing to do |

**Newly opened calls: none.** No code changed state to Otevřená or Vyhlášená, and none is new.
None of the calls the ledger holds had its dates or allocation changed overnight. Every code
the 2026-09-18 pass minted or flagged is otherwise unchanged. This includes `05_26_107`
(OPŽP 107), which is still *Rozpracovaná*, and the three OPJAK *Plánovaná* calls
`02_25_044/045`, `02_26_046`.

**Why IROP 56/57 was minted in a delta pass.** The deadline move is a dated publisher action.
Both call pages list "Akutní psychiatrie - text 56. výzvy k 18. 9. 2026", and the change note
reads *Přehled změn účinných k 18. 9. 2026*: "Posun data z 13.11.2026 nově do 14.1.2027". The
call was already an owed item from the 2026-09-18 pass ("`06_22_056/057` acute psychiatric
care (XML closes 2026-11-13; the IROP portal says 14 Jan 2027)"). Today the XML and the call
text agree with the portal, so every published fact is now consistent and receipted.

### Checklist source 2: the portals the feeds.json row names

Each page below was fetched on 2026-09-19 (all HTTP 200) and compared with its 2026-09-18
capture in `localproblems/data/raw/2026-09-18/dotace/pages/`. The comparison was
tag-stripped, whitespace-collapsed visible text, diffed line by line. Byte differences come
from nonces and cache tokens. "Text-identical" means no visible line changed.

- **IROP.** Checked `https://irop.gov.cz/cs/vyzvy-2021-2027` (page 1, newest calls first):
  text-identical, so **nothing new since 2026-09-18** on the listing. Also read three call
  pages found by the XML diff: `…/vyzvy/56vyzvairop`, `…/57vyzvairop` and `…/70vyzvairop`.
  From these, downloaded the 18.9.2026 and 6.8.2026 call-text PDFs for 56 and 57 and ran
  pdftotext on them. Found: the 56/57 deadline change, minted as above. Load-more pages 2–18
  and the Planned/Announced/Declared filters were **not re-fetched**. Page 1 carries the
  newest openings and is unchanged, and the XML diff shows no new IROP code. This is a minor
  gap, named under "Coverage gaps".
- **OPŽP.** Checked `https://opzp.cz/nabidka-dotaci/` and `https://opzp.cz/dotace/107-vyzva/`:
  both text-identical. **Nothing new since 2026-09-18.** Call 107 is still *Plánovaná*, and
  the XML's accessible-from date is 2026-09-30. The POST API
  (`/wp-json/opzp/v1/call/html`) was not re-queried because the rendered listing is unchanged.
- **OPJAK.** Checked `https://opjak.cz/vyzvy/` and `https://opjak.cz/harmonogram-vyzev/`:
  both text-identical. **Nothing new since 2026-09-18.** The call schedule is still v2 of
  20 Feb 2026, and 02_25_044/045 and 02_26_046 are still unpublished as calls.
- **SFŽP.** The hub `https://sfzp.gov.cz/dotace-a-pujcky/` is byte-identical. The
  financial-instruments list (`…/financni-nastroje-a-pujcky/`) and the Modernisation Fund
  call list (`…/modernizacni-fond/vyzvy/`) are text-identical. **Nothing new since
  2026-09-18.**
- **NPO.** Checked `https://planobnovy.gov.cz/vyhlasene-vyzvy/`: text-identical. It shows the
  same four calls, all in the ledger. **Nothing new since 2026-09-18.**
- **TAČR.** Checked `https://tacr.gov.cz/` (news on the home page) and
  `https://tacr.gov.cz/programy-a-souteze/`: both text-identical. **Nothing new since
  2026-09-18.**
- **CINEA / HaDEA.** Checked `https://cinea.ec.europa.eu/funding-opportunities/calls-proposals_en`
  pages 0–3 (`?page=1..3`) and `https://hadea.ec.europa.eu/calls-proposals_en`: all
  text-identical. **Nothing new since 2026-09-18** (no new call cards and no new opening
  dates). F&T topic JSON on `ec.europa.eu` was not queried, see "Coverage gaps".

**Checklist: 8 of 8 sources visited**, each named above.

### Record staged: 1

| id | title | sector | money EUR | closes | scale/money/urgency/recurrence |
|---|---|---|---|---|---|
| `dotace-irop-56-57-akutni-psychiatrie` | IROP calls 56/57 — 1.6 billion CZK for new acute and forensic psychiatric beds | health | 65,410,503 | 2027-01-14 | 1/3/3/1 |

- **Money.** The two XML allocations, 1,009,803,920 + 582,287,720 CZK, converted at 24.340.
  For call 57, the call text's ERDF-plus-state split sums to 582,469,720 CZK, which is
  182,000 CZK more than the XML total. The record uses the XML figure and says so in `notes`.
- **Support rate.** The call text does not state the applicant-level support rate. The record
  gives only the EU share of public funds by arithmetic (85 % for 56, 70 % for 57) and says
  the specific rules were not read.
- **Receipt.** `url` is the IROP call-56 page. `quote` is 275 characters of the MS2021+ XML
  for `06_22_056`, and it was checked programmatically as a literal substring of the
  whitespace-collapsed saved payload (exactly 1 occurrence).
- **PII scan.** The email/phone grep over `staged.jsonl` has one hit, and it is the digit run
  `1009803920` in the allocation tag. That is not personal data.
- **Dedup.** Neither the id nor the url is in `seen.txt` or any `data/signals/tenders/*.jsonl`.
  No `dotace-` record covers calls 56/57. The psychiatric-hospital hits in the ledger are
  ted/hlidac/nen contracts, not this call.
- **Validation.** `data/signals` was copied to `$TMPDIR/dotace-sim/signals`, then:
  ```
  python3 scripts/normalize.py --raw data/raw/2026-09-19/dotace --complete --dry-run \
    --today 2026-09-19 --out-dir $TMPDIR/dotace-sim/signals --seen $TMPDIR/dotace-sim/signals/seen.txt
  → would append 1 records across 1 file(s); 0 dropped by materiality; 0 incomplete;
    0 refused by AC-GDPR1.  tenders/2026-09-19.jsonl: +1; identity-key dedup 0 skipped;
    AC-GDPR1 dropped evidence_type (routing key) only.
  ```
- **Hand-off for the coordinator.** Run `normalize.py --raw data/raw/2026-09-19/dotace
  --complete` for real, then
  `python3 scripts/db.py upsert data/signals/tenders/2026-09-19.jsonl`.

**Likely problem matches (`data/problems/cz/`).** None is strong. This is capital money for
psychiatric bed capacity, which the register does not track as a problem.
- **Weak, for context:** `p-0022-hospital-ehealth-interoperability`. It already cites
  psychiatric-hospital IS contracts and the IROP 78/79 eHealth grant. New wards funded here
  will need hospital-IS and documentation fit-out, but the call does not pay for IT as such.
- **Weak, for context:** `p-0036-hospital-clinical-documentation-automation`, for the same
  reason.
- **Tangential:** `p-0032-residential-care-placement`. The call's OP Z+ companion activities
  cover deinstitutionalisation, but this call is inpatient psychiatry, not residential care.
- Recommend: attach to no record as proof. At most, add it as a "public money nearby" context
  line on p-0022 if the coordinator judges it relevant.

### Errata candidates (for the coordinator; this pass did not write `data/errata.jsonl`)

- **No ledger record changed overnight.** The six `source-updated` lines the attended
  completion appended today already cover every stale record the 2026-09-18 pass found.
  Today's diff touches none of them again.
- **A correction to a manifest, not a ledger.** The 2026-09-18 dotace manifest says IROP 116
  *Sociální bydlení II* "grew almost ninefold before it closed" (142.9 M → 1,242.2 M CZK).
  Today's XML reads **124,210,050 CZK**. The 1,242,210,050 figure was evidently a one-night
  data-entry error: an extra digit, corrected in the next export. The net change since
  2026-09-03 is therefore a **cut** from 142.9 M to 124.2 M CZK, not a ninefold rise. No
  ledger record or problem cites 116 (grep over `data/signals` and `data/problems`), so
  nothing needs an errata line. Anyone matching on the 2026-09-18 manifest note should
  disregard "ninefold".
- **FYI, not an erratum.** `dotace-oprybarstvi-36-investice-akvakultura`: the XML title lost a
  line break. The quote is still a substring after whitespace collapse.

### Coverage gaps (named, not silent)

1. **IROP deep listing not re-walked.** Load-more pages 2–18 and the status filters were
   skipped this pass. They are covered indirectly: page 1 (newest first) is unchanged and the
   XML shows no new IROP code. The next monthly pass walks them.
2. **EU topic conditions are still owed**, carried from 2026-09-18 gap 3:
   - funding rates for HORIZON-CL5-2026-11 and SMP-Food;
   - the CEF-DIG cable-repair budget;
   - HORIZON-CID-2026-01, HORIZON-MISS-2026-02-CANCER and HORIZON-CL4-2026-03;
   - the **LIFE-2026 SAP/TA/PLP family, which closes 2026-09-22**. Unless a pass resolves
     their budgets through F&T topic JSON (`ec.europa.eu`, which must be fetched outside the
     sandbox because TLS fails through the proxy) before Tuesday, they will be lost to the
     ledger the same way LIFE-CET was. This pass did not query `ec.europa.eu`.
3. **The open-call backlog is still owed** (2026-09-18 "Beyond the floor"), minus IROP 56/57,
   which this pass discharged. Still owed:
   - IROP: `06_22_010`, `06_23_097/098`, `06_23_106/107/108`, `06_22_067`;
   - OPD `04_25_038`;
   - OP Z+ `03_24_062`, `03_24_059` (closes 2026-09-30) and `03_22_012`;
   - OP ST `10_25_095`, `10_25_089` (closes 2026-09-30) and `10_26_110`;
   - OP AMIF `12_26_046` (**closes 2026-09-23**);
   - OP NSHV `14_26_018` (closes 2026-09-30) and `14_26_019`.
4. **OPŽP 107 is not yet declared.** It is due to become accessible on 2026-09-30, and the
   next pass confirms the declaration and the call text.
5. **OPJAK 02_25_044/045 and 02_26_046** remain *Plánovaná* in the XML and unpublished on
   opjak.cz.
6. **IROP 70.** The XML says *Pozastavená* and irop.gov.cz says *Otevřená*. It is not in the
   ledger and was not minted, but the next pass should see which side the other converges to.
7. **Left-hand-side location.** The 2026-09-18 snapshot exists only in the main checkout's
   untracked `data/raw/2026-09-18/dotace/`, not in this worktree. Today's snapshot is here.
   Whoever merges should keep one copy reachable for the next diff: `data/raw` is pruned at
   28 days.

### Pass summary (5 lines)

```
feed:              dotace-scan (weekly delta, 2026-09-19; left-hand side = 2026-09-18 snapshot)
checklist sources: 8 of 8 visited — MS2021+ XML + IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO, CINEA/HaDEA
records:           1 staged (dotace-irop-56-57-akutni-psychiatrie); dry-run 1 appendable, 0 incomplete, 0 refused
coverage gaps:     7 named — IROP deep walk; EU topic conditions (LIFE SAP/TA/PLP closes 09-22);
                   open-call backlog; OPŽP 107; OPJAK planned; IROP 70 XML/portal mismatch; LHS location
rotation state:    n/a — category rotation is arb-scan's duty
```

---

## arb-scan pass — 2026-09-19

Monthly BROAD pass (pipeline/SCANS.md), evidence_type `funded`, source `arb-scan`, id prefix =
ISO2 of the origin country. Run inside the weekly worktree `weekly/2026-09-19`. This pass wrote ONLY
`data/raw/2026-09-19/funded/` (payloads, per-category staged files, the merged `staged.jsonl`) and
this manifest. Nothing written to `data/signals/**`, `seen.txt`, `register.db`, `data/problems/**`
or `feeds.json`; no `db.py`, no git state change.

### How the pass ran

Four category agents in parallel (other, mobility, housing, environment: the four categories the
2026-09-18 rotation table left at 2026-09-03), one shared brief (evidence bar, arb-scan prefix
allowlist from `data/feeds.json`, dedup against `seen.txt` and every `data/signals/funded/*.jsonl`
line, Czech absence check with a positive control, established/early per the CONVENTIONS test),
plus the coordinator's own discovery walk of the funding listings (below) and one feed pick
(`de-arcos`). The coordinator re-validated every merged line: exact key set, prefix allowlist,
`geo_origin` = prefix, money-score arithmetic, `seen.txt` collision, and a mechanical re-check that
every `quote` is a literal substring of the saved page (html-unescaped, whitespace collapsed):
**8/8 pass**.

### Discovery listings (the pass's source walk, items since 2026-09-18)

| listing | result 2026-09-19 | what it gave |
|---|---|---|
| `eu-startups.com/feed/` (RSS) | 200, 10 items, all 2026-09-18 (no 09-19 items yet, it is a Saturday) | Arcos (feed pick, staged); Penelope Health, Cycloid, Big Picture Bio, Phosphoenix, TUSK IC are health/b2b/hardware, out of this pass's categories |
| `eu-startups.com/category/funding/` | **HTTP 403** (third pass running) | nothing, coverage gap |
| `eu-startups.com/category/funding/feed/` | **HTTP 404** | nothing |
| EU-Startups weekly round-up 2026-09-14…18 | RSS body says "visible for CLUB members only" | nothing, coverage gap (paywall) |
| `tech.eu/feed/` (RSS) | 200, 20 items, 2026-09-16…18 | Arcos; Kuva Space (screened, below); syte and Integral already staged 2026-09-18; the rest out of category |
| tech.eu weekly round-up 2026-09-18 (`/2026/09/18/open-cosmos-secures-eur300m/`) | 200, saved `feed-picks/techeu-weekly-2026-09-18.html` | "more than 70 deals" named only as headline links; in-category: Fever (screened); Mama Insurance is fintech |
| `tech.eu/category/funding/` | **HTTP 404** | nothing |
| `vestbee.com/insights/articles` | **HTTP 404** | nothing |
| `sifted.eu/feed` | 200, 24 items, 2026-09-15…18 | editorial and big-AI rounds; nothing in the four categories |

Saved as `funded/listing-*.{xml,html}`. As on 2026-09-18, the RSS windows are about three days deep,
so most candidates came from category-targeted web search by the agents. The feeds carried nothing
dated 2026-09-19.

### The checklist source for this feed: THE CATEGORY-ROTATION DUTY

All 12 categories are named. The rotation state at the start was read from the 2026-09-18 manifest
("the next pass starts at `other`, then `mobility`, `housing`, `environment`"). This pass covered
exactly those four. Arb-record counts are from the ledger index (5,994 funded lines) before this pass.

| category | last BROAD sweep before | arb records before | covered this pass | records staged | last swept AFTER |
|---|---|---|---|---|---|
| other | 2026-09-03 | 5 | **YES** (owed, first) | 2 (`us-belfry`, `de-arcos`) | 2026-09-19 |
| mobility | 2026-09-03 | 8 | **YES** (owed) | 2 | 2026-09-19 |
| housing | 2026-09-03 | 11 | **YES** (owed; 2026-09-18 had only one feed pick) | 2 | 2026-09-19 |
| environment | 2026-09-03 | 16 | **YES** (owed) | 2 | 2026-09-19 |
| legal-compliance | 2026-09-18 | 11 | no (swept yesterday) | 0 | 2026-09-18 |
| retail-services | 2026-09-18 | 16 | no | 0 | 2026-09-18 |
| energy | 2026-09-18 | 18 | no | 0 | 2026-09-18 |
| fintech | 2026-09-18 | 21 | no | 0 | 2026-09-18 |
| health | 2026-09-18 | 29 | no (still owes Klinik, see Carried debts) | 0 | 2026-09-18 |
| b2b | 2026-09-18 | 65 | no | 0 | 2026-09-18 |
| education | 2026-09-18 | 9 | no | 0 | 2026-09-18 |
| govtech | 2026-09-18 | 6 | no | 0 | 2026-09-18 |

**Every category now has a broad sweep dated 2026-09-18 or 2026-09-19.** The next pass starts from
the eight at 2026-09-18, thinnest first: **govtech (6), education (9), legal-compliance (11),
retail-services (16), energy (18), fintech (21), health (29), b2b (65)**, then the four swept today.

### Records — 8 staged in `data/raw/2026-09-19/funded/staged.jsonl`

CZ verdict vocabulary as on 2026-09-18: **absent** = no Czech player selling this found, with
queries and a passed positive control; **contested** = direct players exist but none established;
**taken** = a direct, ESTABLISHED Czech player.

| id | what | money | abroad | CZ verdict |
|---|---|---|---|---|
| `us-belfry` (other) | back office for security-guard firms: scheduling, timesheets, payroll by contract rules, client billing | USD 12M Series A ≈ EUR 11.59M (2025-01-21) | early (3-years-selling limb unproven) | **absent** — TOUCHGUARD (IČO 19403429) and DOBRÁ AGENTURA (IČO 26453118) adjacent (patrol/attendance, no payroll or billing) |
| `de-arcos` (other, feed pick) | sensor-fusion security platform plus its own control centre for property and critical infrastructure | EUR 5.5M seed (2026-09-18) | early (founded ~2025) | taken — WESTPOINT a. s. (IČO 25635603, since 1998, 2,500+ connected sites), SECURITAS ČR (IČO 43872026); comparison point only |
| `gb-zenobe` (mobility) | e-bus and e-truck fleets as a service: vehicle and battery finance plus depot charging built and run | EUR 325M **debt** facility (2025-07-24) | established (since 2017, National Express, Go-Ahead) | **absent** for the bundle — E.ON Energie (IČO 26078201) adjacent (depot charging only). Urgency 2: zákon 360/2022 Sb. 60 % clean-bus quota in force since 2026-01-01 |
| `fr-ecov` (mobility) | carpooling lines run as public transport for rural authorities | EUR 11.75M Series A (2023-05-10, older than preferred, no later round) | established (~2015, 55 lines) | contested — JedemeSpolu.cz direct/early; Yedem (IČO 07831901) adjacent/established |
| `de-ecoworks` (housing) | industrial serial renovation of apartment blocks with prefab facade and roof modules | EUR 23M project capital (2026-03-31); last equity EUR 40M Series A 2023 | established | taken for the outcome — HOLBORN GROUP (IČO 26429403, 850+ buildings); the prefab method itself is absent |
| `us-deckard` (housing) | software for towns that finds unregistered short-term rentals and recovers tourist tax | USD 3.9M credit facility ≈ EUR 3.34M (2025-09-26) | established (400+ jurisdictions) | **absent** on the town side — ODP-software SněžníkPass (IČO 61683809) and Ubytovačka adjacent; the state eTurista register (2027/28) may absorb part of it. Founded in Australia, HQ US, so `us-` |
| `nl-orbisk` (environment) | AI camera-and-scale food-waste monitor for professional kitchens | EUR 8M+ Series A (2024-12-09), floor recorded | established (since 2019, 40+ countries) | contested — foreign Winnow (IKEA Zličín) and KITRO (Andaz Prague) direct; no Czech-owned vendor; canteen segment unserved |
| `gb-naturemetrics` (environment) | eDNA biodiversity monitoring and nature-impact reporting | EUR 24.3M Series B (2025-01-14) | established (since 2014, 600+ clients) | contested — SEQme s.r.o. (IČO 24312819) direct on the lab step, maturity unshown |

Verdicts: absent 3 · contested 3 · taken 2. All 8 carry a verbatim `quote` read off the saved page
at `funded/<category>/<id>.html` (`feed-picks/` for Arcos), `http_status` 200, `fetched_at`,
`extraction: manual`, and the full CZ check with queries, surfaces and control in `notes`.

**Money-type caveats (in each `money_note`):** Zenobē and Deckard are debt facilities, ecoworks is
project capital; none is an equity round. `nl-orbisk` records the stated floor of "€8+ million".
`fr-ecov` (2023-05) is older than the 2024 preference; kept because the model and traction are
proven and the Czech check is current.

**Orbisk duplicate resolved:** the `other` agent also found Orbisk and screened it out as
environment. Only the environment copy is staged.

### New-problem candidates for MATCH (foreign-funded solution, documented Czech gap)

1. `us-belfry` — security-guard agencies (6,698 trade licences, 44,216 staff at 2023-12-31) run shifts,
   payroll and client billing in separate tools on thin margins. No register record fits (nearest
   p-0033 care-shift marketplace, p-0007 construction subcontractors, both off).
2. `gb-zenobe` — bus operators must electrify PSO fleets under zákon 360/2022 Sb. while depending on
   claw-back-prone IROP subsidies; no Czech fleet-as-a-service offer. No register record.
3. `us-deckard` — towns losing short-term-rental stay fees. Touches **p-0040** (guest reporting), on
   the town side that p-0040 notes but does not claim as open; could be its own record.

Contested and worth a look: `nl-orbisk` (canteen food waste; no Czech-owned vendor), `fr-ecov`
(rural capacity under the driver shortage), `gb-naturemetrics` (biodiversity measurement for EIA,
soft demand). Comps: `de-ecoworks` → **p-0025** and **p-0024**; `de-arcos` → no record (taken).

### Candidates screened and NOT staged — stated, not silent

- **Czech player present:** Empathy (US, bereavement admin), Aura Funerals (GB) and Solace Care
  (Goodbye.cz, IČO 08319588); Tellia (FR, farm spray records; state Portál farmáře and Czech
  software); sports-club software (EOS, Tymka, Sport-Club.cz); co-parenting apps (App2Us); school
  panic alerts (Bezpečná škola 2.0); non-profit association software (AssoConnect, also no round
  after 2020); reev (DE, EV charging billing: MyBox, ČEZ futurego, PRE); Aviloo (AT, EV battery
  checks sold in CZ; AAA Auto, EV Check); Tchek and ProovStation (FR, vehicle damage AI: 3DCARSCAN,
  InstaCover, Cebia); van tachograph compliance (TAGRA, TDT; p-0010 ground); senior-taxi dispatch
  (Senior Taxi system); Matera (FR, SVJ software: SVJ Aplikace, Bydloo); Keyzy and Libeen (rent-to-own:
  Ownest, BYX); Klim (DE, farm carbon: Agreena, Carboneg); Arbonics (EE, forest carbon: Beleaf,
  Lesy ČR; round 2023); small-landlord software, developer handover, heat-cost allocation, PENB and
  renovation financing (Czech vendors named by search, not researched to record depth).
- **Already held:** Prepared (`us-prepared`), Dryad (`de-dryad-networks`), Veesion (`fr-veesion`),
  EverSettled (`round-eversettled`), Beam (`gb-beam-up`), Recyda, Resourcify, Vytal, Padam; Chekin
  and Enter already named in p-0040 and p-0025; fleet-electrification planners (Volteum, Nelson,
  Flott, Curo).
- **Prefix not claimed:** xFarm Technologies (CH, EUR 36M Series C 2024-10). `ch` is not in arb-scan's
  `id_prefixes`; widening it is owner work.
- **Below bar / weak transfer / old round:** Breedr (beef-cattle data, weak Czech fit); OroraTech
  (wildfire satellites, overlaps Dryad); Farmdok, Agrivi, Airly, Breeze, Concular, Railnova,
  Ampcontrol (no round in 2024+ or overlapping); WALLROUND (founded 2024, overlaps ecoworks);
  Housing Connector (nonprofit); Keyway and Pronto (depend on US vouchers); textile sorters (no
  fitting EU round).
- **From the listings:** Kuva Space (FI) — the tech.eu item is a pilot story, not a funding receipt,
  and illicit-crop monitoring has no Czech buyer. Fever (ES, USD 250M) — already operates in Prague
  (Candlelight concerts), so not an arbitrage; not researched further. The social-housing allocation
  lead (the housing support act in force since 2026-01-01) found no transferable funded foreign model.

### Positive controls — passed, with recorded misses

| run by | control | query / method | result |
|---|---|---|---|
| coordinator (Arcos) | Wultra | ARES name search | Wultra s.r.o., IČO 03643174, 2014-12-15 — PASS |
| coordinator (Arcos) | Ringil | google-cz "česká platforma pro řízení přepravy a tendrování dopravců pro výrobní firmy" | Ringil surfaced — PASS |
| other | Ringil, Wultra | Czech transport-tendering query; ARES | both PASS |
| mobility | Ringil | "systém pro řízení přeprav a rezervaci časových oken na rampách česká firma" | PASS |
| mobility | MyBox (in-category) | "správa a účtování nabíjecích stanic pro firmy a bytové domy platforma Česko" + ARES (IČO 07750471) | PASS |
| housing | Wultra | "česká firma zabezpečení mobilního bankovnictví ochrana aplikace banky" + ARES | PASS |
| housing | Ringil | "software pro řízení nákladní dopravy přeprava zakázky česká firma TMS" | **MISS** (fireTMS, WinSped, TruckManager instead) |
| housing | Ubyport vendors (in-market) | "hotelový systém automatické hlášení cizinecké policii Ubyport česká firma" | Best Guest, Trevlix etc. PASS; **Previo MISS** |
| environment | Ringil, Wultra | Czech TMS query; ARES | both PASS |
| environment | Softlink | "informační systém pro vodárenské společnosti fakturace vodného a stočného…" | **MISS** (SOFTbit, Datainfo, QI, Munis instead) |

Every agent had at least one passing control before writing an absence. The misses repeat the
2026-09-18 finding: descriptive queries surface *a* Czech vendor of the kind, not reliably a named
one. The three **absent** verdicts rest on queries plus ARES plus a passed control. They are not a
clean sweep, and by the asymmetric-authority rule they cannot raise any `gap`.

### Coverage gaps

1. **Listing walks:** EU-Startups category 403 and round-up paywall; tech.eu category 404; Vestbee
   404; RSS three days deep, nothing dated 2026-09-19. Rounds from mid-August to mid-September in
   these four categories are most likely under-sampled.
2. **Publisher fetch failures:** eu-startups.com 403 to curl and WebFetch for article pages on the
   `other` run (Tellia and Breedr receipts unsaved; neither staged); Wayback 429 (Belfry's pre-2023-09
   selling not verifiable); BusinessWire 403 (FinSMEs used for Deckard 2019); an energyhub.eu page 404.
3. **Surfaces searched:** `google-cz` (Czech-language queries through the session WebSearch tool,
   which is US-based and is not literally Google with `hl=cs`), `ares` and `own-funded-ledger` only.
   `app-stores`, `cz-saas-directories`, `startupjobs` and `eshop-addon-marketplaces` were **not**
   searched; no note claims them.
4. **Maturity limbs not fully verified:** SECURITAS ČR (years only), KITRO (years not sourced),
   SEQme (no second limb), DOBRÁ AGENTURA (age only). The Aktuálně.cz item on Prague's data exchange
   with the tax authority (Deckard note) came from a search snippet and was not fetched.
5. **Legal status not re-checked:** active enforcement of zákon 360/2022 Sb.; the status of a Czech
   private-security-services bill after the SECURITAS release of 2024-01-30.

### Carried debts (from 2026-09-18, not in this pass's categories)

- **Klinik** (FI, AI GP triage): still owed a proper health record and a check against Medevio.
  It was rejected on 2026-09-18 over a `fi` prefix misread. Health was not in this pass's rotation.

### Hand-off

- Staged: `data/raw/2026-09-19/funded/staged.jsonl` (8 lines), merged from
  `feed-picks/staged-feed-picks.jsonl`, `environment/`, `mobility/`, `housing/`, `other/`.
- Validation: `cp -R data/signals $TMPDIR/arb-sim/signals`, then
  `python3 scripts/normalize.py --raw data/raw/2026-09-19/funded --complete --dry-run --today 2026-09-19 --out-dir $TMPDIR/arb-sim/signals --seen $TMPDIR/arb-sim/signals/seen.txt`
  → **would append 8 records to funded/2026-09-19.jsonl; 0 dropped by materiality; 0 incomplete;
  0 refused by AC-GDPR1; identity-key dedup 0 skipped**. The only allowlist drop is the routing field
  `evidence_type`, as designed.
- **Not run, on purpose:** the real `--complete`, `db.py upsert`, any `seen.txt` or ledger write,
  and any commit. These belong to the coordinator/PROCESS.

### Pass summary

1. Feed: **arb-scan** (evidence_type `funded`, broad pass, attended, run 2026-09-19).
2. Checklist sources: **12 of 12 categories named**; 4 swept (other, mobility, housing,
   environment); 9 discovery listings visited, 5 blocked, 404 or paywalled.
3. Records: **8** staged — other 2, mobility 2, housing 2, environment 2 (absent 3 · contested 3 · taken 2).
4. Coverage gaps named: **5**, plus the Klinik debt carried.
5. Rotation: other · mobility · housing · environment → **2026-09-19**; the other eight at
   **2026-09-18**. The next pass starts at govtech, education, legal-compliance.

---

# Scripted ingest, 2026-09-19T0815 — attended completion (weekly run)

`scripts/ingest.sh` (all active feeds) exited **0**: every feed met its contract and the run is fully
audited. It ran outside the command sandbox, because inside it `with-secrets` cannot read the sops key
(see the veklep section above). The 11 feeds that were STALE (not run since 2026-09-08) ran.

- Staged 5,470 new records (ted 3,906 · yc 991 · reddit 178 · hlidac 137 · nku 89 · nen-ptk 67 ·
  suggest 27 · round 20 · veklep 18 · feed 10 · hackathon 10 · ec-hys 7 · tacr 7 · sukl 2 · roundup 1).
- Model pass A (SUBAGENT driver, no API credit): 112 batches by 14 subagents; 5,280 filled,
  190 refused by the pain / stated-need bar (166 pain, 24 stated_need) and left staged.
- Model pass B over the 1,157 material survivors: 1,089 filled first time; 68 rejected by the validator
  (summary longer than 2 sentences), re-issued as 2 batches and filled.
- `normalize.py --complete --allow-incomplete`: **appended 1,204** (tenders 1,113 · funded 60 ·
  regulation 14 · demand 12 · asks 5); 944 materiality drops. 3,322 left staged: the 190 bar refusals
  and the non-material records pass B never titles (they drop at materiality on any later run).
- `db.py upsert` for the five ledgers; `db.py health`: LIVE 22 · PENDING 6 · STALE 0 · BROKEN 0.
- Known judgement calls from the workers: about 25 yc- cards with no location were given
  `geo_origin: US` because the vocabulary has no "unknown"; reddit posts from Czech subreddits were
  all given CZ. `veklep-KORNDXY8B5OY` is a second VeKLEP card for the innovative-business act
  already held as `veklep-ALBSDXTKB4NK`; identity-key dedup does not catch two VeKLEP ids for one act.
- Silent feeds (`ok=1 items_kept=0`): none named by the contract check. NKÚ: 89 staged, none material
  and new, so the IKEM duplicate the demand-scan warned about did not land.
- NOTE: this run's `fetch_log` rows live in the WORKTREE's `data/register.db` (gitignored). Replay
  `python3 scripts/db.py fetchlog data/raw/2026-09-19` in the main checkout at ship time.
