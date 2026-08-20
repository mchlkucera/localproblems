# localproblems — architecture v3 (ingest)

*2026-08-20 · The proposed amendment set to `SPEC.md` v2 and the build order for
Phase 2. SPEC stays authoritative: nothing here is in effect until §11 is applied to
SPEC itself. Rule of this file: every factual claim carries a receipt — a `file:line`,
a Phase-1 probe, or a named command. Where something is unverified it says so in
those words: **UNTESTED**, **UNMEASURED**, **UNDECIDABLE**, **UNPROVEN**.*

> **THE RECEIPTS RULE — cite mechanisms, not figures that rot. And verify the shape you are
> told to preserve, BEFORE you preserve it.**
>
> **This binds every Phase 2 worker, not just this document.** Repeatedly in this program, an
> assertion has travelled further than anyone's check of it:
>
> - a "sha256" that was really bare `shasum`'s SHA-1 — a real number under a false label;
> - a receipt count still reading "two" after the list had grown to four (§7.1);
> - a `note:` prefix relayed down the chain as *the* canonical shape when it covers 7 of 22
>   entries — **and then a "correction" to it that was itself wrong** (§8.4);
> - a five-record retrofit scope in which one record had **nothing to retrofit** (§8.4);
> - an entity-key design that assumed `entity_domain` worked uniformly, when **92% of
>   `funded` URLs are six aggregator domains** because harvests cite the investor's page,
>   not the company's (§2.3);
> - a `MAX(date)` freshness aggregate, obvious and wrong: 145 records are legitimately
>   future-dated and the corpus max is **2030-08-01** (§7.4).
>
> Every one was settled by a single command. Every one arrived from **further up the chain
> than the person who checked it.** (The list is deliberately not numbered: the receipt-count
> failure above was caused by exactly such a hardcoded total, and a count of failures is no
> more immune to rotting than any other figure in this document.)
>
> **AND THE ERRORS HAVE A DIRECTION: WE OVER-CLAIM BLOCKERS.** The blockers register has now
> been wrong in **four rows, every one of them in the same direction** — Hlídač (live, called
> blocked), row 0 (the vault called empty when only the hook was broken), row 12 (two invented
> 403/301 reasons), §7.3 (a 404 path on a host that never 404s). **That is a systematic bias,
> not four coincidences: we check positive claims harder than negative ones.** Nobody demands
> a positive control for "it's broken".
>
> **A false blocker costs as much as a false capability — it parks work that could have
> shipped.** This one parked our best CZ contract feed for a day and generated an
> owner-action instruction for a problem that did not exist. So: **an unmeasured negative is
> not a finding.** Either measure it, or label it `UNVERIFIED` in the register where a reader
> can see the difference (§10 rows 0a and 2 are labelled that way for exactly this reason).
>
> **AND A PASSING CHECK THAT HAS NEVER BEEN SHOWN ABLE TO FAIL IS NOT EVIDENCE.** W1 set the
> standard worth copying: before trusting AC-GDPR1's zero-match result across 6,181 records,
> it **planted an email address and watched the checker match it** — proving the check was
> capable of failing before reading its silence as success. **Contrast AC-F1, which passed for
> weeks while 116 records sat unowned**: it was never shown able to fail, so its green meant
> nothing. A green check and a broken check look identical from the outside; the only thing
> that distinguishes them is having seen the check go red on purpose.
>
> **So every acceptance check in §12 must state how it is proven capable of failing**, not
> merely what it asserts. If you cannot describe the input that makes it red, you do not have
> a check — you have a comment.
>
> **Corollary: text search over code is not proof about code.** W1's grep for a fabricated
> `http_status` matched **its own docstring**, reporting a problem that did not exist. Where
> the question is "does this code do X", inspect the **AST**, not the characters.
>
> **Authority is not a receipt. AN ASSERTION'S AUTHORITY IS UNRELATED TO ITS AUTHOR'S
> POSITION IN THE CHAIN.** The failures above were authored by an architect, a coordinator, a
> program lead, and a worker's own blocklist design — **every one of them by someone entitled
> to be right about that thing.** Seniority does not correlate with correctness on a
> question of fact; it correlates only with how few people re-check. The more confident the
> source, the less likely anyone re-measures — which is exactly why a wrong fact from a lead
> travels further than a wrong fact from a peer. So: before you preserve, match, normalize to, or iterate over a stated
> shape, **run the grep that proves it exists**, and check that the set you were handed is
> the set that is actually there.
>
> **AND A CORRECTION IS AN ASSERTION TOO — it inherits no authority from having corrected
> something.** The `Gap check` prefix above was "corrected" in this document to a two-value
> vocabulary derived from a `head -4` over 22 entries: a sample of four, generalized, and
> presented with the credibility of a measurement. The real census is **four prefixes**
> (§8.4), and the correction would have mis-aimed the identical rewrite risk at a different
> 10 entries. **Incomplete sampling looks exactly like complete sampling** — the output of
> `head -4` is indistinguishable from the output of a census until you count. So: state the
> denominator, make the command reproduce the *whole* set, and prefer a **prohibition**
> ("do not touch this field") over an enumeration ("these are the shapes"), because a
> prohibition survives the variant you did not sample.
>
> **And when you cite, prefer the thing that stays true:** the *assertion*
> (`check-css.mjs:12-19` proves two files are identical) over the hash it computes; the
> *quoted text* over the line number carrying it; the *command* over the number it printed.
> **A stale receipt is worse than no receipt, because it still reads as authoritative.** So
> where a figure is genuinely load-bearing (§0), the command that regenerates it is printed
> beside it — re-derive rather than trust. And where a line number is cited (**§11 in
> particular, whose targets are being edited by a parallel program**), **re-anchor on the
> quoted text**; assume the number has moved.

*Revision 2 (2026-08-20, post-critic): corrects a false "TED is script-only" claim (§1),
a mislabelled hash (§9), and a scorer that was priced for one pass but needs two (§6);
applies eight cut-list rulings (§2, §7); and adds the two new owner mandates —
**feed fragility and the admin space (§7, the most important section in this doc)** and
**the hiring seam (§13)**.*

The v3 thesis in one line: **the moat is acquisition + normalization**, so the weekly
judgment loop is split away from a continuous, objective, mostly-scripted ingest loop,
every record gains a receipt that can be checked mechanically, and **every feed gains a
contract that makes its silence visible**.

---

## 0. What is actually true today (baseline)

| Fact | Receipt |
|---|---|
| 31 problems; **6,181 signals** — 2,403 funded · 3,515 tenders · 137 demand · 126 regulation | `data/problems/cz/` file count; `wc -l data/signals/*/*.jsonl`, `data/signals/seen.txt` |
| **Corpus mix by source** (measured this session): `ted` 3,052 (**49.4%**) · `yc` 1,814 (**29.3%**) · `hlidac` 463 (7.5%) · `round` 414 (6.7%) · `arb-scan` 175 (2.8%) · `demand-scan` 137 (2.2%) · `reg-scan` 126 (2.0%). **Non-`yc` share: 70.7%** | `cat data/signals/*/*.jsonl` piped through a python3 `Counter` on `source` |
| Whole corpus is **3.63 MB** (3,625,573 bytes) across 8 files | `cat data/signals/*/*.jsonl \| wc -c` |
| **Only two run-dates exist**: 2026-08-13 (4,910 records) and 2026-08-14 (1,271). There is **no observed weekly ingest rate** — see the UNMEASURED label in §6 | per-file `wc -l` over `data/signals/*/*.jsonl` |
| The site is public and deploys as a LOCAL prebuilt upload | `SPEC.md:179-185` |
| A git remote EXISTS: `github.com/mchlkucera/localproblems`; no `.github/` yet | digest §B (corrects the older "no remote" note) |
| Raw payloads ignored at **two levels**, dated dirs kept traversable, manifests un-ignored, `register.db*` ignored | `.gitignore:14-21` (raw trees) + `:24-26` (working store) — **already landed and MEASURED, do not re-narrow** (§9.1) |
| **`data/feeds.json` and `data/feed_health.json` are TRACKED** — which is what §4 and the §7.5 admin space both require | coordinator-measured with `git check-ignore` across seven cases: `data/raw/ingest.out.log` IGNORED · `data/raw/<date>/ted-it.json` IGNORED · `data/raw/<date>/reddit.rss` IGNORED · `data/raw/<date>/manifest.md` TRACKED · `data/feeds.json` TRACKED · `data/feed_health.json` TRACKED · `data/register.db` IGNORED |
| `web/shared.css` is byte-locked to the skill stylesheet by a build gate | `web/scripts/check-css.mjs:12-19` (sha256 equality asserted at prebuild) |
| **sqlite-vec is NOT INSTALLED**: `find_spec('sqlite_vec')` → False, `CREATE VIRTUAL TABLE … USING vec0` → `no such module: vec0`, no dylib on the box. `enable_load_extension` itself works | measured this session with python3 + `sqlite3` |
| `suggest`, `reddit`, `feed` have **ZERO records** — the demand feeds have never landed a signal, and nobody noticed | digest §F, confirmed by the corpus mix above (no such `source` values exist) |

---

## 1. The split

Two loops, two entry points, one shared wrapper — and, inside INGEST, **two invocation
modes** (§1.2) that determine what can actually run today.

| | INGEST | PROCESSING |
|---|---|---|
| Entry point | `pipeline/INGEST.md` (**new**) | `pipeline/PROCESS.md` (slimmed; was `TASK.md`, `af63331`) |
| Cadence | hourly-ish / continuous, per-feed (§4) | on-demand (weekly Mon 06:00 stays the default) |
| Judgment | **none.** Region-blind, objective, mechanical | **all of it.** Region questions, de-rank, prose, scoring |
| Writes | `data/raw/`, `data/signals/**`, `seen.txt`, `data/feed_health.json`, DB | `data/problems/**`, `newsletter/`, DB `match_log` |
| Commits | **no** — leaves a clean working tree for PROCESSING | yes (`pipeline/PROCESS.md` step 7) |

### 1.1 Data flow

```
data/feeds.json ─┐
                 ├─► fetch (curl, pure script) ─► data/raw/<today>/<feed>.<ext>   [gitignored]
                 │                                data/raw/<today>/manifest.md     [COMMITTED]
                 │                                        │
                 │                        contract check ─┤  (§7.2 — a 200 with garbage
                 │                                        │   is LOUDER than a non-200)
                 │                                        ├─► fetch_log            [DB only, never git]
                 │                                        ▼
                 └──────────────────────────────► normalize  (scripts/normalize.py)
                        1. mechanical: id · seen.txt dedup · money · dated urgency · quote
                        2. MODEL pass A — scale, recurrence, urgency grade-3, pain bar
                        3. materiality drop  (money<=1 AND scale<=1 AND urgency==0)
                        4. MODEL pass B — EN title + summary, SURVIVORS ONLY  (§6)
                                                          ▼
                          data/signals/<type>/<today>.jsonl   [COMMITTED — canonical]
                          data/signals/seen.txt               [COMMITTED — canonical]
                          data/feed_health.json               [COMMITTED — the admin space, §7.5]
                                                          │
                                                          └─► db.py upsert ─► signals + entity keys
══════════════════════════════════ handoff: git working tree ══════════════════════════
[PROCESSING]  db.py shortlist (IČO / domain; KNN in Phase 3)
                     └─► MATCH agent ─► data/problems/cz/*.md   [COMMITTED]
                            └─────────► match_log (links AND dismissals) [DB only, §2]
                     ─► SCORE ─► BUILD GATE `npm --prefix web run build`
                                    └─► newsletter draft ─► commit ─► vercel prebuilt deploy
```

The handoff is the git working tree, not a queue. INGEST leaves new JSONL lines
uncommitted; PROCESSING picks them up on its next run and commits them together with the
problems they produced. Nothing polls, nothing waits, nothing serves.

**Ordering note (ruling 8).** The materiality filter moved *ahead* of the expensive pass.
Two of its three conjuncts are mechanical — `money` from `money_eur` and dated `urgency`
(`data/CONVENTIONS.md:51,52-53`) — so only `scale` requires the model. Running the cheap
scoring pass, dropping, and *then* generating English prose means **we never pay to write
a summary for a record we are about to discard**. Accuracy-neutral: the filter's inputs
are identical, only the order changed.

### 1.2 The two invocation modes (this is the difference between a plan and a plan that runs on Monday)

The owner's mandate that AI scoring happens **at normalization** stands. What was left
implicit in revision 1 — and is the reason the scorer looked simultaneously essential and
unbuildable — is that INGEST has two invocation modes:

| | **ATTENDED** | **UNATTENDED** |
|---|---|---|
| How | a Claude agent executes `pipeline/INGEST.md` as a prompt | `claude -p "$(cat pipeline/INGEST.md)"` in `scripts/ingest.sh`, secrets via **`with-secrets`** (never `direnv exec` — §10 row 0) |
| Driver | a human or the coordinator starting a session | launchd / GitHub Actions (§5) |
| Needs `ANTHROPIC_API_KEY` | **no** | **yes — present and verified (§10 row 2); must be passed explicitly, as ambient CLI auth fails** |
| Status | **WORKS TODAY** | **UNBLOCKED — the key is present and authenticating** (§10 rows 0a, 2). What remains is **plumbing, not permission**: handing the value to the nested `claude -p` without an interpreter touching it. Previously recorded as INERT; that rested on the discredited direnv probe |
| Can normalize the 70.7% of the corpus needing generated EN prose | **yes** | not until the key lands |

**The Phase 3 proof run will be performed in ATTENDED mode.** This matters: it means the
ingest path is demonstrable on Monday without waiting on any owner action, and the missing
API key downgrades automation, not capability.

### 1.3 Which steps need a model

`scripts/normalize.py` (§12 item 4) owns every cell marked **script**. It reads
`data/raw/<date>/` + `data/feeds.json` and writes JSONL + `seen.txt` + `fetch_log` rows;
the model cells are handed to whichever mode is running.

| Step | Model? | Note |
|---|---|---|
| fetch every feed | **script** | curl only |
| contract check + `manifest.md` + `fetch_log` rows | **script** | §7.2 |
| canonical id + `seen.txt` dedup | **script** | prefix rules are literal (`data/CONVENTIONS.md:29-34`) |
| structured field extraction: url, date, money_eur, geo_origin | **script** for TED / Hlídač / yc-oss / NEN / suggest · **model** for prose and PDF feeds | |
| `sector` | **script** for TED (CPV group → sector is a lookup; groups exist at `scripts/fetch_ted.sh:17-21`) · **model** elsewhere | |
| **`title` + `summary` in English** | **model for every feed except `yc-oss`** | see the ceiling below |
| `scores.money` | **script** | pure arithmetic on `money_eur` (`data/CONVENTIONS.md:51`) |
| `scores.urgency` | **script** when a machine-readable date exists · **model** only for the grade-3 "in force + actively enforced" branch | |
| `scores.scale`, `scores.recurrence` | **model** | |
| materiality drop | **script** | runs between the two model passes (§1.1) |
| pain-language bar (suggest/reddit) | **model** | `pipeline/PROCESS.md:24-26` |
| `quote` extraction | **script** | per-feed literal rules (§7.8) |
| liveness `http_status`/`fetched_at` | **script** | |
| LLM-fallback extraction on contract violation | **model** | §7.3 — sets `extraction: llm-fallback` |
| **STAGE** to `data/raw/<date>/staged.jsonl` | **script** | the script-only path stops here — see below |
| JSONL append + seen.txt + DB upsert | **script**, but **only for records that already carry model scores** | |

> ### ⚠ THE SCRIPT-ONLY PATH CANNOT LAND A RECORD. IT STAGES.
>
> Every signal needs `scale` and `recurrence`, both **model** cells above, and §6.2 forbids
> writing default scores for a record the model did not score. Therefore
> **`--mechanical-only` produces STAGED, UNSCORED records — never ledger lines.**
>
> | Path | Produces |
> |---|---|
> | `normalize.py --mechanical-only` (unattended, no key) | `data/raw/<date>/staged.jsonl` — ids minted, `seen.txt` checked, `money`/dated-`urgency` computed, `quote` extracted, liveness recorded. **Nothing appended to `data/signals/`. Nothing in `seen.txt` yet.** |
> | ATTENDED mode, or unattended **with** `ANTHROPIC_API_KEY` | complete records: the staged set plus `scale`, `recurrence`, EN `title`/`summary` → appended to `data/signals/<type>/<date>.jsonl` + `seen.txt` + DB |
>
> **Say this plainly wherever the pure-script path is described**, because the tempting
> misreading — "the script path keeps the ledgers fresh on its own" — is false. What the
> script path actually buys is that **the fetch, the receipts and the raw payload are
> captured while they still exist** (raw is pruned at 28 days, §7.8), so a later attended
> pass can complete records that would otherwise have been unrecoverable. That is a real and
> substantial win. It is not ingestion.
>
> `seen.txt` is written **only on append**, never at staging — otherwise a staged-then-failed
> record would be permanently deduped out of existence.
| MATCH / SCORE / problem prose | **model** | PROCESSING, unchanged |
| build + deploy | **script** | unchanged |

#### The honest ceiling on the pure-script path — corrected

**Revision 1 claimed TED could be normalized by script. That was false, and the corpus
proves it.** Committed TED records carry *agent-authored English titles* with the Czech
original quoted inside the summary:

```
TITLE  : Kroměříž water utility — smart-metering system
SUMMARY: Vodovody a kanalizace Kroměříž awarded ~€1.3M to build a smart-metering system…
TITLE  : Motol + Homolka hospitals — cyber threat detection
SUMMARY: …awarded ~€6.1M for a cyber-threat detection & response tool ('Výzva č. 113 –
         Nástroj pro detekci a reakci na kybernetické hrozby', dynamic purchasing system…)
```

No script produced "Kroměříž water utility — smart-metering system" from a CPV-coded
notice. The schema demands an EN title and a ≤2-sentence EN summary
(`data/CONVENTIONS.md:39,43`), and TED is **49.4% of the corpus**.

> **The ceiling, stated properly: exactly one feed is genuinely script-only end to end —
> `yc-oss`, at 29.3% of records** (English `one_liner`, structured JSON, no generated
> prose). **The other 70.7% needs a model for the title and summary.** A pure-script
> ingest is therefore a real but minority path, and any plan that assumes otherwise
> under-provisions the model budget by roughly 3×.

This propagates: the runner cannot be curl-only (§5), and the cost model must price a
*generation* pass alongside the scoring pass (§6).

---

## 2. DB design

`data/register.db` — SQLite, gitignored, deterministically rebuildable. Driver:
`scripts/db.py` (python3 + stdlib `sqlite3`). **All DB tooling stays out of `web/`** so the
publish path keeps a zero-DB dependency.

Revision 2 cuts this schema roughly in half on the critic's ruling: **no table survives
that nothing queries.**

### 2.1 Why gitignored + rebuildable, not committed

1. **It keeps SPEC §2's promise.** "No servers, no database server, no queue" — a file that
   nothing serves and no build step reads is not a database server. `SPEC.md:37-38`
   survives verbatim; §7's ban is amended, not deleted (§11).
2. **The publication spine stays legible.** Commits are the publication mechanism
   (`SPEC.md:150-154`). A committed binary makes every ingest run an opaque diff and makes
   concurrent runs conflict unresolvably.
3. **Canonical-by-construction.** If the DB were authoritative for anything, losing it would
   lose data. Making it rebuildable makes that structurally impossible.

### 2.2 What was cut, and what would bring it back

| Cut | Ruling | Re-add trigger |
|---|---|---|
| **`feeds` table** | `data/feeds.json` is the registry; nothing queries a mirrored copy. **This deviates from the owner's literal table list in the brief** — stated plainly rather than quietly. The mandate's *intent* was a machine-readable feeds registry, and `feeds.json` delivers exactly that; a SQL mirror added a sync obligation for zero readers. | The first query that needs to **join `fetch_log` to feed metadata** in SQL (e.g. "yield per cadence class"). Until then `jq` reads the registry. |
| **`problem_sources` table** | No consumer in Phase 2 — the web build reads frontmatter directly (`web/lib/data.ts:138-148`). | Phase 3, landing **together with its consumer** (the KNN match shortlist). |
| **most `signals` columns** | Eleven columns kept (below). The rest is reachable through JSON1 over `raw` in milliseconds on a **3.63 MB** corpus. | A measured slow query. Not before. |
| **`rebuild --check`** | Replaced by one in-rebuild assertion. AC-DB1 already proves idempotency with zero extra code. | — |
| **`fragile` column + archive.org** | Protects **zero live records today** (§7.9). | The first record landed by a feed we would have flagged fragile. |
| **`signal_vec` / `problem_vec`** | **sqlite-vec is not installed** (§0). Deferred to Phase 3 behind an install step (§12). | The extension being installed *and* MATCH consuming a shortlist. |

`match_log` **survives**, conditionally — see §2.5.

### 2.3 DDL

```sql
PRAGMA journal_mode = WAL;        -- concurrent ingest reads while PROCESS writes
PRAGMA synchronous  = NORMAL;
PRAGMA foreign_keys = OFF;        -- soft FKs ONLY: the DB is derived, never the arbiter

CREATE TABLE meta (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
-- seeded rows: schema_version · rebuilt_at · git_head · jsonl_lines · signals_count

-- Eleven columns. source/type/date are the three axes every ops query uses (per-feed
-- counts for /sources, freshness, health); the entity keys are the match shortlist;
-- jsonl_file/line point back at the canonical log; `raw` carries everything else and is
-- JSON1-queryable at milliseconds over 3.63 MB.
CREATE TABLE signals (
  id               TEXT PRIMARY KEY,
  source           TEXT NOT NULL,      -- data/CONVENTIONS.md:35-36
  type             TEXT NOT NULL,      -- funded|regulation|tenders|demand (= directory)
  date             TEXT NOT NULL,
  entity_name_norm TEXT,               -- DERIVED-ONLY (NFKD, diacritics stripped, suffixes cut)
  entity_ico       TEXT,               -- DERIVED-ONLY (8-digit + mod-11 checksum, MANDATORY)
  entity_domain    TEXT,               -- DERIVED-ONLY (eTLD+1 minus the platform blocklist).
                                       -- NULL for most `funded` records BY DESIGN — see the
                                       -- measured note under §2.3.
  dup_of           TEXT,               -- DERIVED-ONLY
  jsonl_file       TEXT NOT NULL,      -- data/signals/<type>/<date>.jsonl
  jsonl_line       INTEGER NOT NULL,
  raw              TEXT NOT NULL       -- the verbatim JSONL line
);
CREATE INDEX signals_date   ON signals(date DESC);
CREATE INDEX signals_source ON signals(source, date DESC);
CREATE INDEX signals_type   ON signals(type, date DESC);
CREATE INDEX signals_ico    ON signals(entity_ico)       WHERE entity_ico IS NOT NULL;
CREATE INDEX signals_domain ON signals(entity_domain)    WHERE entity_domain IS NOT NULL;
CREATE INDEX signals_ename  ON signals(entity_name_norm) WHERE entity_name_norm IS NOT NULL;

-- THE HEALTH SPINE (§7.4). NEVER dropped by rebuild — this history exists nowhere else.
CREATE TABLE fetch_log (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id        TEXT NOT NULL,          -- <date>T<HHMM>, one per ingest cycle
  feed_key      TEXT NOT NULL,
  started_at    TEXT NOT NULL,
  finished_at   TEXT,
  http_status   INTEGER,
  bytes         INTEGER,
  items_fetched INTEGER,
  items_kept    INTEGER,
  yield_anomaly TEXT,                   -- NULL | 'zero' | 'below-range' | 'above-range'
  parse_method  TEXT,                   -- structured | llm-fallback | manual | none
  runtime_ms    INTEGER,
  ok            INTEGER NOT NULL DEFAULT 0,
  error         TEXT,
  raw_path      TEXT
);
CREATE INDEX fetch_log_feed ON fetch_log(feed_key, started_at DESC);
CREATE INDEX fetch_log_run  ON fetch_log(run_id);

-- KEPT CONDITIONALLY (§2.5). NEVER dropped: the dismissals are irrecoverable memory.
CREATE TABLE match_log (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  at         TEXT NOT NULL,
  signal_id  TEXT NOT NULL,
  region     TEXT NOT NULL,
  problem_id TEXT,
  method     TEXT NOT NULL CHECK (method IN ('knn','ico','domain','name','manual')),
  similarity REAL,
  decision   TEXT NOT NULL CHECK (decision IN ('linked','dismissed','deferred','dup')),
  note       TEXT
);
CREATE INDEX match_log_signal  ON match_log(signal_id);
CREATE INDEX match_log_problem ON match_log(region, problem_id);
```

### ⚠ MEASURED: `entity_domain` IS NOT AN ENTITY KEY FOR `funded` RECORDS

The matching design rests on three entity keys. One of them does not work uniformly, and the
doc must not imply it does.

**Measured over all 2,403 `funded` records: just 49 distinct URL domains.**

| Domain | Records | Share |
|---|---|---|
| `ycombinator.com` | 1,814 | **75.5%** |
| `vestbee.com` | 246 | **10.2%** |
| `eic.ec.europa.eu` | 53 | 2.2% |
| `tech.eu` | 52 | 2.2% |
| `techstars.com` | 20 | 0.8% |
| `inovo.vc` | 20 | 0.8% |
| **top six combined** | | **91.8%** |

**The cause is structural, not a data-quality accident:** funded harvests cite the
**investor's or aggregator's page** as `url` — the YC directory entry, the Vestbee round
write-up — **not the company's own site.** The URL identifies *who reported the round*, never
*which company raised it*.

**Consequences, worked through rather than noted:**

1. **After the platform blocklist (digest §F) does its job, `entity_domain` is NULL for
   ~92%+ of `funded` records.** That is the blocklist working correctly, not failing —
   without it, `entity_domain` would collapse into a **feed key wearing an entity key's
   name**, silently clustering 1,814 unrelated companies under "same domain".
2. **`entity_domain` is a `tenders`/`regulation` key.** There it is meaningful: a buyer's or
   regulator's domain genuinely identifies the entity.
3. **Funded matching therefore leans on `entity_name_norm` + `entity_ico`** — which is why
   `entity_name_norm`'s NFKD/diacritic/legal-suffix normalization (digest §G) is load-bearing
   for the funded stream specifically, and why the near-dup rule requires **corroboration**
   rather than trusting any single key.
4. **This raises the value of the hiring feed's 99.90% IČO coverage (§13.0):** it supplies a
   primary-key join for a stream where the domain key is structurally unavailable.

**ARGUED ALTERNATIVE (not adopted, recorded so it is not re-proposed blind):** derive
`entity_domain` for `funded` from a different field — a company homepage in the harvest
payload. Rejected for now because the committed records do not carry one; adding it means
re-harvesting, and the corroboration rule already covers the gap. If a future funded feed
does carry a company URL, populate it from that field and this note becomes obsolete for that
feed only.

**sqlite-vec — status corrected from "syntax unverified" to ABSENT.** Measured this
session: `importlib.util.find_spec('sqlite_vec')` → `False`; `CREATE VIRTUAL TABLE t USING
vec0(...)` → **`no such module: vec0`**; no dylib present. `enable_load_extension` works,
so the *host* is capable — there is simply nothing to load. The vec tables and every KNN
path are **Phase 3, gated on an install step** (§12). `db.py` must probe for the extension
and set `meta.vec = off` when absent; shortlists then fall back to IČO/domain/name joins,
which need no extension at all.

### 2.4 Rebuild semantics

```
# NOW — Phase 2
python3 scripts/db.py rebuild        # DROP + recreate: signals, meta. Asserts jsonl_lines == signals_count
python3 scripts/db.py upsert <jsonl> # single-run path used by INGEST
python3 scripts/db.py fetchlog <dir> # manifest + contract results -> fetch_log rows
python3 scripts/db.py health         # fetch_log -> data/feed_health.json  (§7.5)
python3 scripts/db.py match ...      # append one match_log row  (§2.5)
python3 scripts/db.py dupes --report # report-only sweep over ENTITY KEYS only (IČO/domain/name)

# LATER — Phase 3, gated on the sqlite-vec install (§10 row 7). Listed here so the
# deferral is explicit at the point of use; a reader should not have to reach §12 to
# discover these exist and do not work yet.
python3 scripts/db.py embed          # LATER: id-set difference -> embed the missing set
python3 scripts/db.py shortlist ...  # LATER: KNN shortlist for MATCH
```

| Table | On `rebuild` | Why |
|---|---|---|
| `signals`, `meta` | **DROP + recreate** from git | pure projections of committed files |
| `fetch_log` | **never dropped** | liveness + health history exists nowhere else |
| `match_log` | **never dropped** | dismissals are irrecoverable memory |

The single integrity assertion, inside `rebuild`: **`jsonl_lines == signals_count`** — the
number of non-blank lines read from `data/signals/**` must equal the rows inserted. A
mismatch means a duplicate id or a parse failure and exits non-zero. That is the whole
check; `rebuild --check` was scaffolding around a property AC-DB1 already proves.

### 2.5 `match_log` — kept only because the write is specified

The "dismissals are irrecoverable" argument is only worth anything **if the agent actually
writes them**. So the append is a literal, copy-pasteable command that goes into
`pipeline/PROCESS.md` step 3, to be run once per decision — including every *rejection*:

```bash
# After EVERY match decision, including dismissals. region is always the region agent's REGION.
python3 scripts/db.py match \
  --signal   ted-12345678 \
  --region   cz \
  --problem  p-0008 \            # or: --problem none   (for a dismissal)
  --method   manual \            # knn | ico | domain | name | manual
  --decision linked \            # linked | dismissed | deferred | dup
  --note     "NIS2 staffing tender at a regulated hospital — same wave as p-0008."
```

If Phase 2 lands without that block in `pipeline/PROCESS.md`, `match_log` is dead weight
and should be cut with the rest.

### 2.6 Simplicity-law accounting

SPEC §10's SQLite tripwire is ">~400 problems per region, or match dedup gets sloppy"
(`SPEC.md:253`). **That tripwire has NOT fired** — the register is at 31 problems. The
SQLite case rests entirely on the owner's explicit 2026-08-20 decision, not on a threshold
being crossed. Stated plainly so no one later reads a justification into the data that
isn't there.

The *second* tripwire — ">~10 sources, or silent fetch failures" → move fetch to GitHub
Actions cron (`SPEC.md:254`) — **has fired, twice over**: the registry seeds 14 feeds, and
`scripts/fetch_feeds.sh:11` is a documented silent 404-as-success. The runner work in §5
and the health work in §7 are justified on SPEC's own terms; the DB is justified by owner
decision. Different warrants, kept distinct.

---

## 3. The JSONL⇄DB contract

**Law:** JSONL + markdown + `feeds.json` + `feed_health.json` are canonical. The DB is a
working store. The web build never opens the DB.

| Data element | Written by | Canonical home | In DB | Web build reads? |
|---|---|---|---|---|
| signal core fields (id, source, url, date, title, sector, geo_origin, money_eur, money_note, summary, scores, notes) | INGEST | `data/signals/<type>/<date>.jsonl` | 4 columns + `raw` | **YES** (`web/lib/data.ts:173-184`) |
| `quote`, `http_status`, `fetched_at`, **`extraction`** (**new**) | INGEST | same JSONL line | in `raw` only | **YES — only after SignalSchema is extended** (below) |
| `seen.txt` | INGEST | `data/signals/seen.txt` | no | **YES** (`web/lib/data.ts:186-191`) |
| run manifest | INGEST | `data/raw/<date>/manifest.md` (committed via `.gitignore:14-15`) | no | no |
| raw payloads | fetch | `data/raw/<date>/*` (gitignored, pruned at 28 days) | path only | no |
| problem frontmatter + body | PROCESSING | `data/problems/<region>/*.md` | no (deferred, §2.2) | **YES** (`web/lib/data.ts:138-148`) |
| gap-check `queries`/`checked`/`expires` | PROCESSING | problem frontmatter | no | **YES** (§8) |
| feeds registry + per-feed contract | human / architect | `data/feeds.json` | no (cut, §2.2) | **YES** (`/sources`, §4) |
| **feed health summary** | INGEST (`db.py health`) | `data/feed_health.json` | derived from `fetch_log` | **YES** (`/sources` status ledger, §7.5) |
| **fetch_log** (per-run http/bytes/yield/parse/error) | INGEST | **DB only** | yes | **NO** |
| **entity_name_norm / entity_ico / entity_domain** | `db.py` | **DB only** | yes | **NO** |
| **dup_of / near-dup links** | `db.py dupes` | **DB only** | yes | **NO** |
| **match_log** (links *and* dismissals) | PROCESSING | **DB only** | yes | **NO** |
| **embeddings** | Phase 3 | **DB only** | Phase 3 | **NO** |

**Confirmed: no derived-only element is needed by the web build.** Proof by enumeration —
`web/lib/data.ts` opens exactly `data/problems/**` (`:138-143`), `data/signals/<type>/*.jsonl`
(`:173-184`) and `data/signals/seen.txt` (`:186`); `web/lib/scorecard.ts:109` additionally
reads `../SCORING.md`. `data/feeds.json` and `data/feed_health.json` become the fourth and
fifth. Both are **MEASURED as TRACKED** by `git check-ignore` (§0) — the ignore rules
(`.gitignore:14-21,24-26`) reach into `data/sources/`, `data/raw/` and `data/register.db*`,
none of which match a file sitting directly in `data/`.

**Acceptance test AC-DB1 (enforceable):** `trash data/register.db && npm --prefix web run
build` exits 0. A fresh clone with no DB must build the site.

### THE ZOD TRAP — hard acceptance item

`web/lib/data.ts:23-41` defines `SignalSchema` as **`z.object`**, which in zod 4 **silently
STRIPS unknown keys**. It does *not* fail. Consequence, spelled out:

> If ingest starts writing `quote` / `http_status` / `fetched_at` / `extraction` into JSONL
> and `SignalSchema` is not extended in the same change, the fields land in the canonical
> ledgers, are stripped at build time, never reach the site — and the "**validation failure
> = build failure = deploy blocked**" law (`SPEC.md:156-157`, `web/lib/data.ts:1-2`)
> **never fires**. The receipt work would appear to succeed while producing nothing
> visible. This is the single most likely way Phase 2 quietly fails.

Contrast, so nobody generalizes the wrong rule: **`SourceSchema` is `z.looseObject`**
(`web/lib/data.ts:48`) — extra keys on problem `sources[]` already pass untouched. That is
why the gap-check fields in §8 "already work" and the signal receipt fields do not.
Different schemas, opposite behaviours, **seven lines apart** (`SignalSchema` closes at
`web/lib/data.ts:41`; `SourceSchema` opens at `:48`).

- **AC-Z1 (mandated):** every optional field ingest writes appears inside `SignalSchema`
  (`web/lib/data.ts:23-41`) in the same commit that ingest starts writing it. Verify:
  `git grep -n 'quote\|http_status\|fetched_at\|extraction' web/lib/data.ts` returns lines
  in the 23–41 range.
- **AC-Z2 (the mechanism that makes AC-Z1 self-enforcing):** change `SignalSchema` from
  `z.object` to **`z.strictObject`**, so an unknown JSONL key is a build failure exactly as
  the law promises. `z.looseObject` is already in use seven lines below, so the
  strict/loose API family is confirmed available in the pinned zod (`web/package.json:17`,
  `zod ^4.4.3`).
  **`z.strictObject` applies to the TOP LEVEL ONLY. The nested `scores: z.object({…})` at
  `web/lib/data.ts:34-39` keeps stripping unknown keys** — so a stray `scores.confidence`
  from a future scorer would vanish silently. **The inner object must be made strict in the
  same edit.** Both, or the trap simply moves one level down.
- **AC-Z3:** one signal visible on the deployed site with a non-empty `quote` rendered.
  Fields that reach the JSONL but not the page have not shipped.

> **The useful asymmetry — one field in this file already behaves correctly.** The `source`
> field at `web/lib/data.ts:25` is a **`z.enum`**, which **fails LOUDLY on an unknown value**.
> So when §13 adds `"mpsv"`, forgetting the schema edit turns the build red immediately —
> the law fires exactly as promised, with no discipline required. That is the opposite of
> the `z.object` silent strip seven lines above. **Same file, two opposite failure modes:**
> enums self-enforce, object shapes do not. AC-Z2 exists to give the object shapes the
> enum's behaviour.

---

## 4. Feeds registry — `data/feeds.json`

Committed, machine-readable, the single source of truth for *what we ingest from*, *what
we are allowed to ingest from*, and *what a healthy fetch looks like*. It feeds the new
`/sources` page at build time. Chosen over YAML/TOML because `web/lib/data.ts` already does
`readFileSync` + zod from `../data`, it is jq-friendly for the shell fetchers, and no
`.gitignore` pattern can match it (digest §D).

### 4.1 Schema

```jsonc
{
  "version": 1,
  "feeds": [
    {
      "key": "ted",                        // stable feed key, kebab-case
      "name": "TED — EU tender notices",   // display name on /sources
      "yields": "EU-threshold public tenders with CZ place of performance; CPV-grouped notices carrying buyer, value and tender deadline.",
      "role": "feed",                      // feed | enrichment. `enrichment` sources (ARES) have
                                           // their health tracked but produce NO signals, are
                                           // exempt from AC-F1, and never inflate the feed count (§13.5)
      "id_prefixes": ["ted"],              // AUTHORITATIVE provenance key (§4.5). AC-F1 asserts
                                           // every prefix in the ledgers maps to exactly one row.
                                           // Many-to-one is normal: arb-scan owns cz-/pl-/de-/dk-.
      "signal_source": "ted",              // LEGACY DISPLAY FIELD (§4.5) — unreliable for nen/dotace
                                           // on pre-2026-08-20 records. Never key attribution on it.
      "evidence_type": "tenders",          // funded | regulation | tenders | demand | hiring (§13)
      "cadence": "daily",                  // 6h | daily | weekly | monthly | quarterly | annual
                                           //   | manual | null  (null ONLY for status:dead)
                                           // No 1h/3h value exists: the local runner cannot
                                           // deliver sub-6h (§4.2). Add a value only when a
                                           // runner can actually meet it.
                                           // RECOMMENDED, not measured — see §4.2.
                                           // This vocabulary must admit EVERY row §4.4 seeds;
                                           // a schema its own seed data violates is the same
                                           // defect class as a stale count.
      "runner": "local",                   // cloud | local | attended | none
      "url": "https://api.ted.europa.eu/v3/notices/search",
      "script": "scripts/fetch_ted.sh",    // null when no fetcher exists yet
      "status": "active",                  // active | blocked | dead | planned  = INTENT (§7.5)
      "blocker": null,                     // one sentence, present iff status != active
      // TIMESTAMP, not a date — a date cannot gate a 3h or 6h cadence. Defined ONCE,
      // here, as: the last run that produced a payload PASSING THE CONTRACT (§7.2).
      // Fetch success alone is not good enough — 200-with-garbage is the dangerous case.
      "last_known_good": "2026-08-19T19:17:04Z",

      // ToS / access verdict — LAW. We never build against a source whose terms forbid it.
      "access": {
        "verdict": "allowed",              // allowed | conditional | forbidden | unknown
        "basis": "Public API, no auth, no rate terms published; EU open-data licence.",
        "checked": "2026-08-20"
      },

      // THE CONTRACT (§7.2) — what a healthy fetch looks like.
      "contract": {
        "parse": "json",                   // json | jsonl | rss | csv | html-table | pdf-text
        "required_fields": ["publication-number", "notice-title", "publication-date"],
        "expected_yield": { "min": 40, "max": 900, "basis": "rolling median ±60% over 6 runs" },
        "allow_missing": false             // true for CALENDAR-KEYED sources: a 404 on a day that
                                           // simply does not exist is EXPECTED, not BROKEN (§7.2)
      }
    }
  ]
}
```

Two changes from revision 1 on rulings: **`fragile` is gone** (archive.org is cut from
Phase 2, §7.9), and **`planned` joins the status vocabulary** — which the CEO adopted from
revision 1's ARGUED ALTERNATIVE, so "no fetcher written yet" no longer has to masquerade as
an external blocker.

### 4.2 Cadence honesty

**The `cadence` values are RECOMMENDATIONS (digest §C), not measured refresh rates.** Only
one was actually measured: **SÚKL** — `opendata.sukl.cz/soubory/MR/mr.zip` returned HEAD 200
with ETag + Last-Modified, and the content had changed **less than 9 hours** before the
probe, which proves refresh is *at least* daily and shows the catalog's "weekly" understates
it (digest §A). Every other cadence is a defensible guess pending `fetch_log` history. The
`/sources` page must therefore label the column *Cadence (target)*, not *Cadence*, and the
7-day yield column next to it (§7.5) is the number that will eventually correct it.

**Print the runner's ACTUAL fire times beside the targets.** A target buried in a plist
nobody opens is how a "3h" promise quietly becomes a 12-hour gap. The prepared launchd
plist (§5.4) fires at **07:17, 13:17, 19:17** — three times a day, with gaps of **6h, 6h
and 12h overnight**. Against the seeded targets that means:

| Feed | Cadence (target, from §4.4) | Actually achievable on the local runner | Gap |
|---|---|---|---|
| `reddit-new` | **6h** | 6h daytime, 12h overnight | met by day, missed overnight |
| `cc-cz` | 6h | 6h daytime, 12h overnight | met by day, missed overnight |
| `ted`, `hlidac`, `suggest`, everything daily | daily | 3×/day | comfortably met |

**`reddit-new` is 6h — RULED, and §4.4 is the single place that number lives.** This section
previously carried a competing "recommendation" of its own, which meant one feed's cadence
was stated twice in one document and a worker had to guess which won. That is the same class
of defect as the receipt-count rot: **one number, one home.** Read cadences from §4.4 only;
this table exists to compare them against the runner, never to set them.

The ruling's reason, recorded once: the binding constraint is Reddit's rate limit
(`fetch_reddit.sh:19`), not our scheduler — a 3h target needs 8 fires/day and would push it.
If the §5.2 probe comes back green, the cloud runner has no overnight gap and could carry
`reddit-new` faster; that would be a change to §4.4, not to this table.

### 4.3 Two build-time assertions

- **AC-F1 — totality, KEYED ON THE ID PREFIX.** Every distinct **id prefix** present in
  `data/signals/**` must map to exactly one registry entry via its `id_prefixes[]`. **Not
  the `source` field** — see the ruling in §4.5. **The rebuild and the health export FAIL and
  NAME THE ORPHANS** when a prefix is unclaimed. Enforced in `scripts/db.py` and in
  `web/lib/data.ts` beside the existing `seen.txt` membership check (`:191`).
  **Scale warning, measured: the corpus contains 49 distinct id prefixes** mapping to ~16
  registry rows (many-to-one is normal — `arb-scan` owns the ISO2 prefixes `cz-`/`pl-`/`de-`/
  `dk-`, `demand-scan` owns the reporting-body prefixes `nku-`/`ombud-`/`civic-`/`consult-`/
  `chamber-`/`uni-`/`ngo-`, per `data/CONVENTIONS.md:29-34`). **Turning this assertion on will
  surface a large orphan cohort in one go. That is the point** — it converts a class of
  silent omission into one loud, enumerable failure instead of a discovery-by-accident every
  few weeks.
- **AC-F2 — no orphan links.** Every non-null `script` path must exist on disk.

`/sources` reads **committed data only**: `feeds.json` + `feed_health.json`. It does not
read the DB — that would break "the site is a pure function of `data/`" (`SPEC.md:150-154`).

### 4.4 Seed — 14 feeds (+ 2 agent harvests, + 1 enrichment source)

| key | yields | source | type | cadence (target) | runner | status | access | note |
|---|---|---|---|---|---|---|---|---|
| `ted` | EU tender notices, CZ place of performance | `ted` | tenders | daily | local | active | allowed | `scripts/fetch_ted.sh`. Cloud viability UNDECIDABLE (§10). `scope` must be `"ALL"` |
| `hlidac` | registr smluv contracts below the TED threshold | `hlidac` | tenders | daily | local | **blocked** | allowed (free key) | token absent — §10 row 1 |
| `cc-cz` | CzechCrunch RSS: CZ funding rounds and launches | `feed` | funded | 6h | cloud | active | allowed | `fetch_feeds.sh:18`. **ZERO records to date** |
| `vestbee` | CEE VC rounds | `feed` | funded | `null` (dead) | none | **dead** | n/a | 301 → `/insights/rss.xml` → 404 (digest §A). Remove `fetch_feeds.sh:19` |
| `yc-oss` | YC company directory (`companies/all.json`) | `yc` | funded | daily | cloud | active | allowed | **the only script-only feed (§1.3)**; 29.3% of the corpus |
| `suggest` | Google Suggest CZ pain completions | `suggest` | demand | daily (**≤1×/day, hard cap**) | local | active | conditional | 144 queries/run = 24 seeds × 6 patterns (`fetch_suggest.sh:17,21`). **ZERO records** |
| `reddit-new` | 4 CZ subs `new.rss` firehose | `reddit` | demand | **6h** | local | active | conditional | `fetch_reddit.sh:29`. **ZERO records.** 6h is RULED, not aspirational: the binding constraint is Reddit's rate limit (`fetch_reddit.sh:19`), and the launchd runner fires 07:17/13:17/19:17 — 6h/6h/12h — regardless |
| `reddit-search` | same subs, `search.rss` pain terms | `reddit` | demand | daily | local | active | conditional | `fetch_reddit.sh:32-33`. **ZERO records** |
| `nku` | NKÚ audit conclusions (`vestnik.asp?rok=YYYY`) | `demand-scan` | demand | daily | local | **planned** | allowed | **the LLM-fallback proof feed (§7.3)**. Non-www host only |
| `sukl` | drug availability open data (`MR/mr.zip`) | `demand-scan` | demand | daily | cloud | **planned** | allowed | **cadence measured** (§4.2). Conditional GET on ETag |
| `ec-hys` | EC Have Your Say consultations + feedback counts | `reg-scan` | regulation | daily | cloud | **planned** | allowed | `ec.europa.eu` needs a sandbox override locally (§10) |
| **`reg-scan`** | **agent regulatory-deadline harvests — the owner of the 126 `reg-` records already in the ledgers** | `reg-scan` | regulation | monthly | **attended** | active | varies | **id_prefixes: `["reg"]`. Added because 116 of those records were ORPHANED** — measured: 126 `reg-` records, of which only **10** touch an EC consultation URL. The only row claiming them was `ec-hys` (`planned`, no fetcher), so **116 had no feed key, no contract and no health check.** Contract states: agent-produced, **no automated yield check**. The ~10 EC records migrate to `ec-hys` when that fetcher exists |
| `nen` | NEN below-threshold tenders, SSR listing | `hlidac` | tenders | daily | local | **planned** | unknown | 50 rows/page; ISO dates in `datumPrvniUver` |
| `demand-scan` | monthly agent research harvests | `demand-scan` | demand | monthly | attended | active | varies | not a script — `pipeline/PROCESS.md:10-14` |
| **`mpsv`** | **MPSV/ÚP `volna-mista` open data — CZ vacancies with IČO, CZ-ISCO, salary floor, NUTS-3** | `mpsv` | **`hiring`** | daily | local | **planned** | **allowed** (licence disclaims copyright **and** sui-generis DB right) | **99.90% IČO coverage — the entity-graph join (§13.0).** `allow_missing: true` (calendar-keyed, §13.7); `typZmenyOpenData` in `required_fields` (the changelog trap). Fetcher is a parallel worker that may slip to Phase 3 (§13.5) |

Plus two registry rows required for AC-F1 totality, both agent harvests: `arb-scan`
(175 records) and `round` (414 records) — funded, monthly, `runner: attended`.

> **Why the orphan mattered, and what it teaches about AC-F1.** `reg-scan` has **126
> committed records** (measured, §0) and, before this row, the only registry entry claiming
> that `signal_source` was `ec-hys` — status `planned`, no fetcher, zero records ever
> produced. AC-F1's totality check **passed** the whole time, because it asks only whether
> *some* row claims each `source`. It does not ask whether that row is **capable of producing
> anything.**
>
> The consequence is exactly the failure `/sources` exists to prevent: **the health view
> would have implied coverage that does not exist.** A reader would see `regulation` backed
> by a registered feed and conclude the stream is maintained; in reality nothing was
> accountable for refreshing 116 of those 126 records. An honest `attended`/monthly row makes
> the real refresh mechanism visible — and if it stops running, the health view now says so.
>
> **This failed BY OMISSION, and omission is invisible on the page.** A broken feed shows up
> as BROKEN; an unowned cohort shows up as nothing at all — no row, no red, no gap a reader
> could notice. That asymmetry is why §7.10's assertion has to run at build time rather than
> relying on anyone eyeballing `/sources`.
>
> **AC-F1 should be read as necessary, not sufficient.** A registry row claiming a `source`
> proves the corpus is explained; it does not prove the stream is alive. That is the health
> view's job (§7.5), which is why `status` (intent) and `state` (observed) are kept separate.

### 4.5 RULED: attribution keys off the ID PREFIX, never the `source` field

**Measured — `source` is not a provenance key.** `source: "hlidac"` holds **463 records from
three unrelated provenances**:

| id prefix | records | share of `source: hlidac` |
|---|---|---|
| `nen-` | **296** | 63.9% |
| `hlidac-` | **114** | 24.6% |
| `dotace-` | **53** | 11.4% |

**Every published yield count for `hlidac` over-credits it by 4.06×** — 463 claimed against
114 real — including numbers already rendered on `/sources`. And because `nen` also declares
`signal_source: hlidac`, the moment NEN goes active `days_since_last_signal` becomes
ambiguous for **both** feeds, silently.

**The ruling: attribution — yield counts, freshness, health state, `/sources` rows — keys off
the id prefix. Three reasons, recorded so this is not relitigated:**

1. **The prefix is already canonical.** `data/CONVENTIONS.md:29-34` defines ids as
   `<prefix>-<nativeid>` with a prefix per feed. We are not inventing a key; we are using the
   one the conventions already specify and the `source` field only approximates.
2. **It requires NO rewrite of committed JSONL.** The ledgers are append-only. Retro-editing
   349 historical lines to "fix" a field would violate that law **and destroy the evidence
   the error ever happened.** A documented discrepancy beats a silent history rewrite.
3. **It fixes all three provenances at once** rather than patching `nen` and waiting to
   rediscover `dotace`.

> **Recorded honestly: `source` is now a LEGACY DISPLAY FIELD.** It is **unreliable for
> `nen` and `dotace` on every record written before 2026-08-20**, and the id prefix is
> authoritative. Going forward new records carry a correct `source`, which requires **`nen`
> and `dotace` added to `SignalSchema`'s `source` enum** (`web/lib/data.ts:25`, §11) — and
> that enum **fails loudly on unknown values**, so the addition self-enforces the moment a
> record tries to use one.

Each registry row therefore carries `id_prefixes: ["hlidac"]`, `["nen"]`, `["dotace"]` and so
on — the field AC-F1 asserts against.

And one **enrichment** row, which is deliberately NOT a feed: **`ares`** —
`role: "enrichment"`, IČO → company name / NACE / founding date / region. Its health is
tracked like any other source, it is exempt from AC-F1 totality, it produces **zero
signals**, and it must never be counted in the feed total (§13.5).

---

## 5. Runner topology

| Class | Runs where | Feeds |
|---|---|---|
| Cloud-OK | GitHub Actions | `cc-cz`, `yc-oss`, `sukl`, `ec-hys` (digest §B) |
| Local-only | this Mac (launchd) | anything needing a secret (`hlidac`), anything UNDECIDABLE (`ted`, `suggest`, `reddit-*`, `nku`, `nen`) |
| Attended | a Claude session | the model passes for the 70.7% needing generated prose, until `ANTHROPIC_API_KEY` lands (§1.2) |

**Consequence of §1.3 that must not be lost:** neither automated runner can produce a
complete record for anything but `yc-oss` today. What they *can* do unattended — fetch,
contract-check, log, prune, and score the mechanical half — is still the majority of the
freshness win, and it degrades loudly rather than silently (§7.7).

### 5.1 "Prepared but not enabled" — the chosen mechanism

**On GitHub, merging a workflow with an `on: schedule:` block to the default branch IS
enabling it** (digest §B). There is no prepared-but-dormant state for cron. Two ways out;
**we pick the first**:

1. **Ship `workflow_dispatch`-only with the `schedule:` block commented out.** ← CHOSEN
2. Commit the schedule and immediately `gh workflow disable ingest.yml`.

Why (1): option (2) has a live window between push and disable, and a disabled workflow is
one UI click away from re-enabling with no commit and no review. A commented cron has a
zero-length enabled window, and turning it on later is a one-line commit — exactly the
audit trail this repo wants.

```yaml
# .github/workflows/ingest.yml
name: ingest

# PREPARED, NOT ENABLED. Merging an `on: schedule:` block to the default branch IS
# enabling it on GitHub — there is no dormant state for cron. The schedule below stays
# COMMENTED until the owner uncomments it in a commit of its own.
# See docs/architecture-v3.md §5.
on:
  workflow_dispatch:
    inputs:
      mode:
        description: "probe = egress decision experiment (writes nothing) | fetch = cloud-OK feeds"
        default: probe
        type: choice
        options: [probe, fetch]
# schedule:
#   - cron: "17 * * * *"    # hourly at :17 — DO NOT UNCOMMENT without reading §5

permissions:
  contents: read            # raised to write only when `fetch` mode starts committing

concurrency:
  group: ingest
  cancel-in-progress: false

jobs:
  probe:
    if: inputs.mode == 'probe'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - name: egress decision experiment
        run: |
          set -u
          UA='localproblems-register/1.0 (+https://localproblems.vercel.app)'
          probe() {  # name method url [json]
            if [ "$2" = POST ]; then
              code=$(curl -s -o /tmp/b -w '%{http_code}' -m 30 -X POST "$3" \
                     -H 'Content-Type: application/json' -d "$4")
            else
              code=$(curl -s -o /tmp/b -w '%{http_code}' -m 30 -A "$UA" "$3")
            fi
            printf '%-14s HTTP %s  %8s bytes\n' "$1" "$code" "$(wc -c </tmp/b | tr -d ' ')"
          }
          probe ted POST 'https://api.ted.europa.eu/v3/notices/search' \
            '{"query":"(place-of-performance IN (CZE))","fields":["publication-number"],"limit":1,"scope":"ALL"}'
          probe reddit  GET 'https://www.reddit.com/r/czech/new.rss'
          probe suggest GET 'https://suggestqueries.google.com/complete/search?client=firefox&hl=cs&ie=utf-8&oe=utf-8&q=datov%C3%A1%20schr%C3%A1nka%20nefunguje'
          probe nku     GET 'https://nku.cz/scripts/rka/vestnik.asp?rok=2026'
          probe nen     GET 'https://nen.nipez.cz/en/verejne-zakazky'
```

### 5.2 The TED decision experiment (owner-approved)

**The question is not answerable from this Mac.** Every Phase-1 probe was a 200 from a Czech
residential IP (digest §A). The one known TED 403 came from Claude-cloud egress — a
different network from GitHub's Azure ranges — so it proves nothing either way (digest §B).
Five cells are genuinely UNDECIDABLE: TED, Reddit, Google Suggest, NKÚ, NEN.

One `workflow_dispatch` run settles all five in ~5 minutes, writes nothing, costs one
Actions minute:

```
gh workflow run ingest.yml -f mode=probe   # after the coordinator pushes .github/
gh run watch
```

Decision rule, applied straight into `data/feeds.json`: **200 → `runner: cloud`**;
**403/429/timeout → `runner: local`**, with `blocker` recording the code and date.

### 5.3 `scripts/fetch_all.sh` — the argument-position landmine

**The five fetchers do not share a signature.** A generic dispatcher that calls
`"$script" "$RAW"` will hand TED a directory path as its *since-date*:

| Script | `$1` | `$2` |
|---|---|---|
| `scripts/fetch_ted.sh` | `SINCE` (`YYYYMMDD`) | **outdir** (`:9`) |
| `scripts/fetch_hlidac.sh` | `SINCE` (`YYYY-MM-DD`) | **outdir** (`:9`) |
| `scripts/fetch_feeds.sh` | **outdir** (`:7`) | — |
| `scripts/fetch_suggest.sh` | **outdir** (`:11`) | — |
| `scripts/fetch_reddit.sh` | **outdir** (`:11`) | — |

So the dispatcher must carry an explicit per-feed call shape, not a convention. Add an
`argv` template to each registry entry, or hard-code the switch — either way, **write it
down**; this is a Phase 2 landmine that fails silently (TED would query with a garbage
since-date and return an empty or wrong window, then look like a yield anomaly rather than
a bug):

```bash
case "$key" in
  ted)              scripts/fetch_ted.sh    "$SINCE_YYYYMMDD" "$RAW" ;;
  hlidac)           scripts/fetch_hlidac.sh "$SINCE_ISO"      "$RAW" ;;
  cc-cz|yc-oss)     scripts/fetch_feeds.sh  "$RAW"                    ;;
  suggest)          scripts/fetch_suggest.sh "$RAW"                   ;;
  reddit-*)         scripts/fetch_reddit.sh "$RAW"                    ;;
esac
```

bash 3.2 — no associative arrays; iterate the registry with
`jq -r '.feeds[] | [.key,.status,.cadence] | @tsv'`.

### 5.4 Local runner — launchd

Prepared, committed, **not loaded**. Location: `pipeline/launchd/org.localproblems.ingest.plist`
(repo-lean law respected by the §11 amendment to SPEC §9.5, landing in the same change).
Installed by the owner, never by an agent.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>org.localproblems.ingest</string>

  <!-- ABSOLUTE paths only: launchd's PATH resolves bash to 3.2.57. The bash-3.2 discipline
       (no associative arrays) stays load-bearing.
       NO `direnv exec` WRAPPER: it fires the sops hook, exits clean, and exports NOTHING
       (§10 row 0). Secrets are fetched inside the script via `with-secrets`, per
       scripts/ingest.sh:7-20. Do not reintroduce direnv here — it would look like it works. -->
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>/Users/michalkucera/Documents/CODE/localproblems/scripts/ingest.sh</string>
  </array>
  <key>WorkingDirectory</key>
  <string>/Users/michalkucera/Documents/CODE/localproblems</string>

  <key>RunAtLoad</key><false/>

  <!-- StartCalendarInterval, NOT StartInterval: it coalesces a missed run after laptop
       sleep, while StartInterval silently skips it (digest §B). -->
  <key>StartCalendarInterval</key>
  <array>
    <dict><key>Hour</key><integer>7</integer><key>Minute</key><integer>17</integer></dict>
    <dict><key>Hour</key><integer>13</integer><key>Minute</key><integer>17</integer></dict>
    <dict><key>Hour</key><integer>19</integer><key>Minute</key><integer>17</integer></dict>
  </array>

  <!-- Log path is explicit and OUTSIDE the repo. A stray runner log written into the tree
       is no longer a leak: .gitignore now ignores at TWO levels (`data/raw/*` catches
       files written straight into the tree, `!data/raw/*/` keeps dated dirs traversable,
       `data/raw/*/*` catches payloads) — measured, `data/raw/ingest.out.log` IGNORED.
       The path is still named here because a reader must know where the runner writes. -->
  <key>StandardOutPath</key><string>/Users/michalkucera/Library/Logs/localproblems/ingest.out.log</string>
  <key>StandardErrorPath</key><string>/Users/michalkucera/Library/Logs/localproblems/ingest.err.log</string>
</dict>
</plist>
```

Owner install (one time, never run by an agent):

```
mkdir -p ~/Library/Logs/localproblems
cp pipeline/launchd/org.localproblems.ingest.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/org.localproblems.ingest.plist
launchctl kickstart -p gui/$(id -u)/org.localproblems.ingest
```

**TCC caveat:** launchd-spawned processes may be denied `~/Documents`. The first
`kickstart` either raises a consent prompt or fails with EPERM in `ingest.err.log`. Verify
with `log show --predicate 'process == "direnv"' --last 10m`.

### 5.5 Alternative: marduk (Ubuntu + Tailscale)

A systemd **user** timer with `Persistent=true` fixes laptop-sleep properly and has no TCC
layer:

```ini
# ~/.config/systemd/user/localproblems-ingest.timer
[Timer]
OnCalendar=*-*-* 07,13,19:17:00
Persistent=true
[Install]
WantedBy=timers.target
```

Needs from the owner: (1) a push credential on marduk (deploy key or `gh auth login`), (2) a
marduk age key added to `.sops.yaml` + `sops updatekeys .env.enc`, (3) checkout +
`direnv allow`. Deferred (§12).

### 5.6 The wrapper — `scripts/ingest.sh`

`pipeline/INGEST.md` is a **PROMPT, not a script**: neither launchd nor Actions can exec
markdown (digest §K5.2). Both runners exec one thin wrapper, and the wrapper is where
`ANTHROPIC_API_KEY` is picked up.

```bash
#!/usr/bin/env bash
# scripts/ingest.sh — the single entry point both runners exec.
# Invoked as: /bin/bash /abs/repo/scripts/ingest.sh [feed-key ...]
# NOT under `direnv exec`: it exports nothing (§10 row 0). Secrets come from `with-secrets`,
# which is invoked per-command inside this script. See scripts/ingest.sh:7-20 in the repo.
set -uo pipefail
cd "$(dirname "$0")/.."
TODAY="$(date +%Y-%m-%d)"; RAW="data/raw/$TODAY"; export TODAY RAW
mkdir -p "$RAW"

scripts/fetch_all.sh "$RAW" "$@"          # pure script: registry-driven, per-feed argv (§5.3)
python3 scripts/normalize.py --raw "$RAW" --mechanical-only   # ALWAYS runs: ids, money,
                                          # dated urgency, quote, contract results (§12 item 4)
python3 scripts/db.py fetchlog "$RAW"     # -> fetch_log
python3 scripts/db.py health              # -> data/feed_health.json  (§7.5)

# UNATTENDED model path. The key IS present and authenticating (§10 rows 0a, 2) — but it is
# NOT in this shell's environment, because the direnv hook exports nothing (§10 row 0).
# `with-secrets` refuses interpreters by design, so an unattended wrapper decrypts for itself:
#   ANTHROPIC_API_KEY="$(sops -d --input-type dotenv --output-type dotenv .env.enc | ...)"
# Never echo it, never pass it on a command line other processes can see.
if [ -n "${ANTHROPIC_API_KEY:-}" ]; then
  claude -p "$(cat pipeline/INGEST.md)" --output-format json > "$RAW/ingest.json"
  python3 scripts/envelope.py "$RAW/ingest.json" || exit 1   # branches on is_error, NOT exit code (§6)
else
  echo "SKIP model passes: ANTHROPIC_API_KEY unset. Records STAGED to $RAW/staged.jsonl —" >&2
  echo "NOT appended to data/signals/ and NOT in seen.txt. Run ATTENDED mode to complete." >&2
  echo "mode to complete them — see docs/architecture-v3.md §1.2." >&2
fi
# Deliberately no git: INGEST never commits or pushes (§1, §12).
```

---

## 6. AI scoring at ingest

### 6.1 Mechanical / model split

| Field | Rule | Model? |
|---|---|---|
| `scores.money` | pure arithmetic on `money_eur`: `null`→0 · `<200k`→1 · `200k–2M`→2 · `>2M`→3 (`data/CONVENTIONS.md:51`) | **no** |
| `scores.urgency` | arithmetic when a machine-readable date exists: none→0 · `>18mo`→1 · `≤18mo`→2 · `<6mo`→3 (`:52-53`) | **no** |
| `scores.urgency` grade 3 ("already in force with active enforcement") | a judgement about enforcement | **yes** |
| `scores.scale`, `scores.recurrence` | `data/CONVENTIONS.md:49-50,54-55` | **yes** |
| pain-language bar (suggest/reddit only) | `pipeline/PROCESS.md:24-26` | **yes** |
| materiality drop | `money<=1 AND scale<=1 AND urgency==0` | **no** — runs *between* the passes (§1.1) |
| **EN `title` + `summary`** | required by `data/CONVENTIONS.md:39,43` | **yes, for 70.7% of records** (§1.3) |

55.7% of the corpus carries `money_eur` (digest §F, critic-reconfirmed), so the arithmetic
half is real coverage, not a technicality.

### 6.2 Two passes, not one

Revision 1 priced only the scoring pass and silently omitted generation — the pass that
70.7% of records actually depend on.

**Pass A — scoring.** Batch 25 items, `claude-haiku-4-5` ($1/$5 per MTok), strict JSON out:

```
system: You score signals mechanically, per data/CONVENTIONS.md. No opportunity judgment.
        No region judgment. Output JSON only — no prose, no markdown fence.
user:   <rubric lines for scale + recurrence, verbatim from CONVENTIONS.md:49-56>
        <the grade-3 urgency test: "already in force AND actively enforced">
        <for suggest/reddit only: the pain-language bar, PROCESS.md:24-26>
        ITEMS: [{"i":0,"source":"ted","date":"2026-08-14","money_eur":412000,
                 "title_native":"…","excerpt":"…"}, …]
        OUTPUT (exactly this shape, one entry per input i, same order):
        {"scores":[{"i":0,"scale":0,"recurrence":2,
                    "urgency_enforced":false,"pain":null,"why":"<=12 words"}]}
```

**`pain` is TRANSPORT-ONLY and is NEVER PERSISTED.** It is a keep/drop verdict consumed by
the suggest/reddit admission bar and discarded; it is not a signal field, it never enters
JSONL, and it must not appear in `SignalSchema` — which, after the AC-Z2 strict flip, would
be a build failure if anyone tried. Same for `why`: it exists so a human can audit a batch
in `data/raw/`, and dies with the raw payload at 28 days.

**Pass B — generation.** EN title + ≤2-sentence summary, for every feed except `yc-oss`,
**over survivors only** (§1.1).

Runner-side validation before anything is written: array length equals batch length, every
`i` present exactly once, every score an integer in 0–3, `why` non-empty. A malformed batch
is retried **once**, then skipped and recorded in `fetch_log.error`. **Unscored records are
never appended with default scores** — they stay in `data/raw/` and are listed in the
manifest as pending. Losing freshness is recoverable; writing vibes into an append-only
canonical ledger is not.

### 6.3 Cost — both passes, assumptions stated

Inputs: the measured per-item batch payload is **294 chars** (critic-measured); assume
**3.5 chars/token** for mixed EN/CZ, and ~600 tokens of per-batch instructions amortized
over 25 items.

| | Arithmetic | Result |
|---|---|---|
| **Pass A** input/item | 294 ÷ 3.5 = 84 tok, + 600÷25 = 24 tok overhead | 108 tok |
| **Pass A** output/item | | 40 tok |
| **Pass A** $/item | 108e-6 × $1 + 40e-6 × $5 | $0.000108 + $0.0002 = **$0.00031** |
| Pass A per 100 signals | | **$0.031** |
| **Pass B** input/item | raw item + amortized instruction | 380 tok |
| **Pass B** output/item | EN title + 2-sentence summary | 80 tok |
| **Pass B** $/item | 380e-6 × $1 + 80e-6 × $5 | $0.00038 + $0.0004 = **$0.00078** |
| **Backfill** (6,181 existing records) | Pass A only — titles and summaries already exist | 6,181 × $0.00031 = **$1.92** |
| **Steady state ceiling** per pre-filter item | $0.00031 + ($0.00078 × 0.707) | **$0.00086** |
| at 500/week | 500 × $0.00086 | **$0.43/week** |
| at 2,000/week | 2,000 × $0.00086 | **$1.72/week** (≈ **$89/year**) |

The steady-state figure is a **ceiling**: it bills generation on the pre-filter set, whereas
§1.1 only generates for survivors. The true number is lower by the drop rate, which is
UNMEASURED. Embeddings, when Phase 3 enables them: ≈$0.011 backfill, ≈$0.002/week
(digest §G).

> **The 500–2,000 signals/week band is UNMEASURED.** The entire corpus is two run-dates —
> 4,910 records on 2026-08-13 and 1,271 on 2026-08-14 (§0) — which is a backfill and a
> follow-up, not a rate. No weekly ingest rate has ever been observed. **One week of
> `fetch_log` rows answers it exactly**, and that table is being built in Phase 2 (§7.4) —
> so this is a number that becomes measurable by the work this doc specifies. Until then it
> is an assumption carrying a cost estimate, and it is labelled as one.

### 6.4 Two hard-won operational facts

1. **The UNATTENDED scorer needs an explicit `ANTHROPIC_API_KEY` via `with-secrets` — NOT
   `direnv exec`, which exports nothing (§10 row 0). Ambient
   CLI auth FAILS.** Verified twice in Phase 1: nested `claude -p` returned "Not logged in"
   when sandboxed (keychain read denied), then hit expired OAuth unsandboxed (digest §H).
   ATTENDED mode has no such requirement (§1.2).
2. **Branch on the envelope's `is_error`, NOT on the exit code.** Phase 1 observed `exit=1`
   alongside a success-shaped JSON envelope (digest §H):

```python
# scripts/envelope.py — the ONLY sanctioned success test for a nested claude -p run.
import json, sys
env = json.load(open(sys.argv[1]))
if env.get("is_error"):
    print(f"ingest: model call failed: {env.get('result','(no result)')[:400]}", file=sys.stderr)
    sys.exit(1)
sys.exit(0)
```

### 6.5 Model OUTPUT quality is UNTESTED

Phase 1 verified the **invocation shape only** — flags, envelope, ~6s wall overhead
(digest §H). Nobody has inspected a single score this model produced. Do not let §6.3's
precision imply the outputs were checked; it prices a mechanism whose accuracy is unknown.

**AC-SCORE1 (Phase 3, before the model path is trusted):** sample **40 records** already in
the committed ledgers (stratified: 10 tenders, 10 funded, 10 demand, 10 regulation), strip
their scores, re-score blind, compare to committed values. Gates: `scale` and `recurrence`
exact match **≥70%**, `|Δ| ≤ 1` on **≥95%**, mean signed Δ within **±0.2** (no systematic
inflation), zero range violations, zero dropped/duplicated `i`. Result to
`data/raw/<date>/scorer-eval.md`.

**If it fails, the model path stays off and only the arithmetic path ships** — `money` and
dated `urgency` still give a usable record, and `scale`/`recurrence`/prose fall back to
ATTENDED normalization, which is how all 6,181 existing records were produced anyway.

---

## 7. Receipt discipline and feed health — **the fragility section**

*This is the most important section in the document. Everything else improves what we
collect; this is what stops the collection dying silently.*

Receipts and health are one discipline seen from two sides: a **receipt** proves a record
is real, and a **contract** proves a feed is still alive. Both fail the same way — quietly,
looking like success.

### 7.1 Why: four receipts, two distinct failure modes

| Receipt | What happened |
|---|---|
| **Vestbee** | `https://www.vestbee.com/blog/rss.xml` 301s to `/insights/rss.xml`, which 404s. `scripts/fetch_feeds.sh:11` uses `curl -sL` **without `-f`**, so the 404 body was saved to disk and the script printed **`OK`** (digest §A). |
| **Hlídač** | a 302 login page was saved as a `.json` payload — HTTP 200, valid JSON-ish file, zero contracts inside. |
| **suggest / reddit / cc-cz** | wired, scheduled, and at **ZERO records** since inception (§0). Nothing ever alerted, because nothing was watching for absence. |
| **the secrets path** | `.env.enc` contributes **ZERO environment variables** (§10 row 0). So every secret-dependent fetch is running **unauthenticated right now** — and an unauthenticated API returns a 401/redirect *body* with a successful-looking transfer. `scripts/fetch_hlidac.sh:13-16` is the sole survivor, and only because someone hand-wrote an explicit empty-token guard. **That guard is the counter-example that proves the point:** it protects one script, was written once, and nothing obliges the next fetcher to have one. |

**Four receipts, and the split between them matters — do not flatten it.**

**Mode A — the wrong body (rows 1, 2, 4): three independent causes, one identical symptom.**
Vestbee (a redirect chain into a 404 body, `fetch_feeds.sh:11`), Hlídač (a 302 login page
stored as `.json`), and the dead secrets path (unauthenticated fetches whose error bodies
would store cleanly) share nothing except the result: **a well-formed file that contains
nothing we wanted, on a transfer that reported success.** No amount of per-script care
generalizes across three unrelated causes — **a declared contract does, because it checks
the *payload* rather than the *transfer*** (§7.2). This is the strongest argument in the
document.

**Mode B — silent absence (row 3): nothing arrives at all.** `suggest`, `reddit-*` and
`cc-cz` have no bad payload to inspect, because they have no payload. A contract check
cannot catch this — there is nothing to check. **This is what the health view's STALE and
PENDING states exist for** (§7.5): the only way to see a feed that has quietly stopped
producing is to watch for the *absence* of records, on a page where the silence is visible.

Two failure modes, two mechanisms, and each is useless against the other. That is why §7
ships both the contract and the admin space rather than either alone.

> **The law: a contract violation is a FIRST-CLASS ERROR, louder than a non-200.** A 500 is
> honest and self-healing; a 200 carrying a login page is a lie that quietly poisons the
> moat. The contract is nothing more than the generalization of the three Mode-A receipts
> above; Mode B is the admin space's job, not the contract's.

### 7.2 The source contract

Per feed, in `data/feeds.json` (§4.1): `parse` method, `required_fields`, and an
`expected_yield` range (rolling median ± tolerance over the last 6 runs). After each fetch,
`scripts/normalize.py` evaluates, in order:

1. **transport** — non-200, timeout, or zero bytes → `error`, feed → BROKEN;
2. **parse** — payload does not parse as `contract.parse` → `error`, feed → BROKEN;
3. **fields** — any `required_fields` key missing from every item → `error`, feed → BROKEN
   (this is the one that catches the Hlídač login page);
4. **yield** — item count outside `expected_yield` → `yield_anomaly` = `zero` /
   `below-range` / `above-range`. `zero` is BROKEN; the others are warnings that show on
   `/sources` and escalate at 3 consecutive runs (§7.6).

**Step 0 — EXPECTED ABSENCE, which runs before all of the above.** A calendar-keyed source
has days that simply do not exist. **The honest example is MPSV: 180 of 658 calendar days are
missing** from the daily files, so a naive "fetch yesterday" fetcher would 404 **roughly once
a week, forever.** W2 implemented `ALLOW_MISSING` against a real 404 on that feed.

> **NKÚ was previously cited here as the expected-absence example. That was wrong.** W2
> measured `?rok=2027`, `?rok=2099` and `?rok=1990` all returning **200 with an 18,095-byte
> empty shell** — **NKÚ never 404s**, so it cannot exercise the expected-absence path at all.
>
> **NKÚ is instead a textbook §7.1 Mode-A case:** a 200 carrying no content. A year-keyed
> fetcher trusting HTTP status would happily record 1990 and 2099 as successful fetches
> forever. Its contract must therefore lean on `expected_yield` and `required_fields`, not on
> the status code — which is precisely why it remains the right feed to prove the
> LLM-fallback path (§7.3). Feeds with `contract.allow_missing: true` therefore treat a 404 on a
calendar-keyed URL as **`skipped`**, not as a failure: it logs a `fetch_log` row with
`ok = 1` and `parse_method = 'none'`, it does **not** increment `consecutive_failures`, and
it does **not** move the feed toward BROKEN.

> **This is not leniency — it is what makes the alarm worth having.** An alarm that cries
> wolf every week gets ignored within a month, and once it is ignored the one real outage is
> invisible too. A health view nobody trusts is strictly worse than no health view, because
> it costs the same and provides false assurance. Expected absence is how the signal-to-noise
> ratio stays high enough for BROKEN to still mean something.

Bootstrapping is honest: until 6 runs exist there is no rolling median, so `expected_yield`
starts as the author's estimate and `basis` says so. A feed with no history warns on `zero`
only.

### 7.3 Tiered extraction — and the `extraction` field

**Structured parse first** (jq / regex / CSV / RSS). On a *parse* or *fields* violation, an
**LLM extraction pass over the raw payload** attempts to recover records. This is also the
mechanism by which the many **PDF sources** in `docs/sources-catalog.md` (ombudsman
quarterlies, ČOI annual reports, MPO strategy reports, the government legislative plan)
finally become records at all — they have been catalogued as high-value and unfetchable for
exactly this reason.

Every signal records how it was extracted:

```
extraction   structured | llm-fallback | manual        (optional, new)
```

- **This is a new JSONL field, so §3's zod trap applies in full.** It must be added to
  `SignalSchema` (`web/lib/data.ts:23-41`) as optional in the same change (**AC-Z1**) and it
  must survive the `z.strictObject` flip (**AC-Z2**) — including the nested-object caveat.
- `llm-fallback` records are **counted in the run summary and marked on the ledger for
  review**. They keep a stream ALIVE while a selector is broken; they are never silently
  trusted. **The `extraction` value IS the review flag** — no second flag is introduced.
- `manual` covers agent harvests (`demand-scan`, `arb-scan`, `round`), which is honest
  labelling of what already happens today rather than a new mechanism.

**Phase 2 ships the LLM-fallback extractor for ONE feed as proof: `nku`** — CONFIRMED as the
right pick. Tier-1 value per `docs/sources-catalog.md:16-21`, probe-verified reachable on
the non-www host, HTML that genuinely resists clean structured parsing, ~2–6 items/month so
volume is safe, and **no existing fetcher, so nothing can regress**. One honest cost to
state: because there is no fetcher, Phase 2 must also write `scripts/fetch_nku.sh` — a
small script, but real scope. (The cheap alternative, `cc-cz`, was rejected: RSS parses
cleanly, so it would never exercise the fallback path it is meant to prove.)

### 7.4 `fetch_log` is the health spine

It already never gets dropped by `rebuild` (§2.4), so history accumulates from the first
run. Per run per feed it records `started_at`, `http_status`, `bytes`, `items_fetched`,
`items_kept`, `yield_anomaly`, `parse_method`, `runtime_ms`, `ok`, `error`, `raw_path`
(§2.3). From that, `db.py health` derives per feed:

`last_success` · `consecutive_failures` · `consecutive_zero_yield` · `days_since_last_signal`
· 7-day yield.

> ### ⚠ `days_since_last_signal` DERIVES FROM THE LEDGER FILENAME — **NEVER** FROM `MAX(date)`
>
> **`MAX(signals.date)` is measurably wrong for freshness.** Measured: **145 records are
> legitimately dated in the future**, and `MAX(date)` across the corpus is **2030-08-01** —
> because a `regulation` record carries its **EFFECTIVE date**, not its capture date. A
> compliance deadline in 2030 is correct data, and computing freshness from it yields
> `days_since_last_signal` of roughly **−1,400**: a feed that has produced nothing for a week
> would report as fresher than one that ran this morning.
>
> **Use the ledger filename** — `data/signals/<type>/<YYYY-MM-DD>.jsonl` — which **is the run
> date by construction** and cannot be contaminated by record semantics.
>
> **This note exists because `MAX(date)` is the obvious choice and someone will "fix" it
> back.** It looks like the right aggregate, it passes review, and it silently inverts the
> health view for the one evidence type whose whole purpose is future deadlines.

### 7.5 THE ADMIN SPACE — `data/feed_health.json`, rendered on `/sources`

The owner asked for "a simple space so I can see how it's going". This is it: **zero infra,
public, static, committed, and it makes SILENCE VISIBLE.**

`db.py health` exports the summary from the DB at the end of every ingest run; the `/sources`
page renders it as a status ledger.

```jsonc
{
  "generated": "2026-08-20",          // relative dates compute against THIS, never wall clock
  "run_id": "2026-08-20T0717",
  "feeds": [
    {
      "key": "ted",
      "state": "LIVE",                 // LIVE | STALE | BROKEN | PENDING  = OBSERVED REALITY
      "last_success": "2026-08-20",
      "items_last_run": 312,
      "yield_7d": 2104,
      "consecutive_failures": 0,
      "consecutive_zero_yield": 0,
      "days_since_last_signal": 0,
      "parse_method": "structured",
      "error": null
    }
  ]
}
```

**Two vocabularies, deliberately distinct — never merge them:**

| | Vocabulary | Means | Lives in |
|---|---|---|---|
| **`status`** | `active` · `blocked` · `dead` · `planned` | **INTENT** — is this feed supposed to be running? | `data/feeds.json` |
| **`state`** | `LIVE` · `STALE` · `BROKEN` · `PENDING` | **OBSERVED REALITY** — is it actually producing? | `data/feed_health.json` |

A feed can be `active` + `BROKEN`. **That combination is the entire point** — it is exactly
what vestbee, suggest and reddit have been for weeks with nobody noticing.

State definitions: **LIVE** — produced within its cadence window. **STALE** — fetch still
200 but no new signal for >3× cadence. **BROKEN** — non-200, contract violation, or
`consecutive_zero_yield ≥ 3`. **PENDING** — registered, never produced a record (today:
`suggest`, `reddit-new`, `reddit-search`, `cc-cz`, and `mpsv` once registered).

**STALE and PENDING are the Mode-B mechanism** (§7.1): they are the only way to see a feed
that has quietly stopped producing, because a feed producing nothing offers no payload for
a contract to inspect. **A `skipped` run (expected absence, §7.2) never contributes to any
of these transitions** — it is recorded for the audit trail and is otherwise inert.

Sub-rulings, all binding:

- **It is a build input.** `web/lib/data.ts` zod-validates `feed_health.json`; **validation
  failure = build failure**, consistent with the existing law (`SPEC.md:156-157`). Confirmed
  not caught by any ignore rule — **measured**, not assumed: `git check-ignore` reports
  `data/feed_health.json` TRACKED alongside `data/feeds.json` (§0). The ignore rules
  (`.gitignore:14-21,24-26`) reach into `data/sources/`, `data/raw/` and
  `data/register.db*` only.
- **Relative dates compute against the health file's own `generated` date (falling back to
  `extractDate()`, `web/lib/data.ts:204-206`), NEVER wall clock** — the same determinism law
  as the gap-check expiry (§8). A build must be reproducible from a commit.
- **Design law is binding.** Whoever renders this MUST invoke the `design-language` skill.
  **Stamp red is the sanctioned alarm colour**; no new tokens, classes or components;
  `web/shared.css` stays byte-locked (`web/scripts/check-css.mjs:12-19`).
- **The same summary prints to the ingest run's terminal AND into `data/raw/<date>/manifest.md`** —
  which the coordinator specifically un-ignored in git (`.gitignore:14-15`) so it remains a
  committed record. Three surfaces, one source: DB → health file → page, and DB → manifest.

### 7.6 Escalation — deliberately boring

A feed **BROKEN for 3 consecutive runs** is named in the weekly `pipeline/PROCESS.md` run
summary and in the newsletter draft's ops footer. That is all. **No paging, no external
service, no webhook.** Email/push notification is a later tripwire, not Phase 2 — and if it
ever arrives it belongs in SPEC §10's tripwire table, not smuggled in here.

### 7.7 The unattended-mode consequence, stated honestly

**LLM-fallback needs a model.** The key is **present and authenticating** (§10 rows 0a, 2),
so this is no longer gated on an owner action — only on the wrapper plumbing. Until that
plumbing lands, a contract violation under the UNATTENDED runner **cannot be rescued**: the
feed degrades to a LOUD ERROR and goes BROKEN, and recovery waits for an ATTENDED run
(§1.2).

**That is correct behaviour, not a gap.** The alternative — writing a degraded record and
calling it success — is precisely the vestbee failure with better branding. But it must be
written down, because it means the automated runner's *self-healing* capability is gated on
the same owner action as the scorer.

### 7.8 The five record-level receipt mechanisms

| Mechanism | Verdict | Enforcement point | Blocks / warns |
|---|---|---|---|
| `quote` on every signal | **NOW** | INGEST, while raw is still on disk | **BLOCKS** the append for scripted feeds; WARNS for agent harvests |
| liveness `http_status` + `fetched_at` | **NOW** | INGEST fetch + periodic re-check sweep | WARNS; flips a display flag on 404/410. Never blocks the build |
| archive.org snapshot | **CUT from Phase 2** (§7.9) | — | — |
| claim lint (**ingest side only** — see the scope split) | **NOW, WARNING-ONLY** | INGEST, signal record vs the fetched payload | WARNS only, by design |
| provenance completeness | **NOW** (~free) | BUILD, reusing `dimRefs()` | WARNS with the offending `<region>/<id>:<dim>` |

**`quote` — per-feed extraction rules.** Capturable **only at ingest**: `data/raw/` is
gitignored and pruned at 28 days (`pipeline/PROCESS.md:16`), so the source text is gone by
the time anyone wants to verify a claim.

| Feed | Quote is |
|---|---|
| `ted` | `notice-title` — the single most informative span. **Not** joined with the value line |
| `hlidac` | the contract subject (`predmet`) alone. **Not** joined with `cenaSDph` |
| `nen` | the row's `Název` cell alone. **Not** joined with `Předpokládaná hodnota` |
| `suggest` | **the completion string IS the quote** — one line, verbatim, no framing |
| `reddit-*` | RSS `<entry><title>` + first 200 chars of the excerpt, whitespace-collapsed |
| `cc-cz` | RSS `<description>`, first sentence |
| `yc-oss` | the company's `one_liner` field |
| `nku` | the release headline + the first sentence containing a number |
| `sukl` | the CSV row: drug name + availability flag + report date |
| `ec-hys` | the initiative's problem-statement sentence from `groupInitiatives/{id}` |
| agent harvests | the sentence containing the number the record claims |

### RULED: a quote is ONE CONTIGUOUS SPAN, and the check runs on DECODED TEXT

Revision 9 was self-contradictory: it mandated a literal-substring check **and** specified
joined two-field quotes for `ted`/`hlidac`/`nen`. **A joined string is never a substring of
the payload**, so every one of those feeds would have failed its own check on every record.
Two rulings resolve it:

1. **`quote` is a single contiguous verbatim span from the payload.** That is what
   "verbatim" means, and it is what the citations program's reveal will display — a joined
   string shown as a quotation would be a fabricated quotation. **Never join fields.** Where
   one field looks thin, pick the **single most informative span** rather than assembling
   one. The value, the date and the buyer are already structured fields on the record; the
   quote does not need to restate them.
2. **The substring check runs on DECODED text, never raw bytes.** Testing against raw bytes
   produced **20 false negatives across 4,397** records, purely from JSON escaping. Decode
   the payload first (JSON unescaping, HTML entities, then whitespace collapse), then
   compare. A check that fails on correct data teaches people to disable it — the same
   argument that makes the lints warning-only (§7.8).

Format law: ≤300 chars, **one contiguous verbatim span**, native language preserved,
whitespace collapsed, no ellipsis inside a number. **Enforceable because** ingest refuses to
append a record whose `quote` is not a substring of the **decoded** payload — a `str.find`
against a file still on disk. For agent harvests the payload is prose the agent read, so it
degrades to a manifest warning; that asymmetry is stated, not hidden.

This leaves the external contract in §7.8 untouched: still a flat string, still retrievable
by signal id, still attributed by the record's own `url`.

> **`quote` HAS AN EXTERNAL CONSUMER — its shape is a contract, not an internal choice.**
> The inline-source-citations program is building the seam that reveals a signal's verbatim
> quote behind a citation, and will state that seam in `CONVENTIONS.md`. **They will not
> block on us**, so the shape has to be right the first time. The required shape is exactly:
>
> **a verbatim snippet, plus the source it came from, retrievable by signal id.**
>
> We satisfy all three with no added structure, and that is deliberate: `quote` is a **flat
> string field on the signal record**, so the record's own `id` supplies retrievability and
> its `url` supplies attribution — the snippet and its source travel together on one JSONL
> line, addressable by `getSignal(id)` (`web/lib/data.ts:197-199`). **No nested object, no
> quote array, no separate quote store.** Anything richer would be structure the consumer
> did not ask for and cannot rely on; anything flatter would lose the attribution. If a
> future feed needs multiple quotes per signal, that is a schema change negotiated with them,
> not a unilateral one.

**Liveness.** Re-check sweep costs ~2 min/run with `xargs -P8 curl -s -o /dev/null -w
'%{http_code}'` (digest §I), one `fetch_log` row per URL. A 404/410 sets a display flag and
never fails the build: **a dead link is a fact about the world, not an invalid record.**

**Claim lint — and the scope split with the citations program.** There are now two lints in
this repo that could each believe they own "is this number sourced?". **They must not
overlap, because two authorities on one question drift apart and then neither is trusted.**
One line each:

| Lint | Owner | Side | The question it answers |
|---|---|---|---|
| **marker→source resolution** (`[S3]` markers → the existing `.ref` device → the record's sources ledger, with URL-matching as a secondary trigger) — **now shipped** as `web/scripts/lint-citations.mjs`, a second prebuild pass, specified in SPEC under "A second prebuild pass" (`SPEC.md:164-167` at time of writing) | **inline-source-citations program** | REGISTER, at render/build | *Does this claim in a problem body point at a source on this record?* |
| **claim→quote** (this document) | **this program** | **INGEST**, before append | *Does this number in a signal record actually appear in the payload we fetched?* |

**Ours is the ingest half and nothing more.** Every number in a signal's `title`, `summary`
or `notes` must appear in the fetched payload — the same substring check the `quote` rule
already performs, widened from one snippet to every figure — or be on the allowlist: years
(1900–2100) · ISO dates · `p-NNNN` · `S<n>` · law citations (`NNN/YYYY`) · scores 0–12 ·
section numbers · list ordinals. **Problem-body claims are out of our scope entirely**; that
is the citations program's lint, and §12.1 records the boundary.

**Honest estimate: 20–40% false positives** (digest §I), driven mostly by CZK→EUR conversion
— a summary reading "awarded ~€1.3M" against a payload carrying only the CZK figure is a
correct record and a lint hit — and by prose rounding. Output: `data/raw/<date>/claim-lint.md`.

**Warning-only is a design choice, not timidity:** a check with a 30% FP rate that blocks
deploys gets disabled within two weeks, and a disabled check is worth nothing. A warning
printing a shrinking number every run is a metric someone actually drives to zero.

### RULED (coordinator): both lints stay WARNING-ONLY

**Both lints reached that posture independently** — theirs "always exits 0: a citation defect
is a finding to fix in the data, never a build failure" (`SPEC.md`, the `lint-citations.mjs`
block), ours for the reasons above. **That makes warning-only a convention, not either
program's preference.** The deciding argument: **a gate two independent programs can each
turn red is a gate neither owns.**

> **Promotion to blocking is a COORDINATOR decision, gated on all three of:**
>
> **(a)** the citations content pass has landed and a **baseline coverage number exists** —
> how many claims cite, register-wide;
> **(b)** the false-positive rate is **MEASURED against that baseline, not assumed** — the
> 20–40% figure above is an estimate and is labelled as one throughout this document;
> **(c)** both programs' leads agree the remaining findings are **anomalies rather than
> routine noise**.
>
> **Neither program may promote unilaterally, and neither may weaken the other's lint.**

**The operative reason, in one line: until all three hold, a red lint trains people to work
around it — which is worse than no lint at all.** A check that is routinely overridden has
negative value: it costs attention, and it converts every genuine finding into noise a
reviewer has already learned to dismiss.

**Provenance completeness.** Reuses `dimRefs()` (`web/lib/scorecard.ts:80-102`) — no new
machinery. Every dimension scoring >0 must have ≥1 resolvable ref.
`data/CONVENTIONS.md:109-111` already says an unresolvable ref "degrades the rendered
scorecard"; this makes that **visible and countable**.

### 7.10 THE ORPHAN ASSERTION — the enforceable mechanism for silent omission

Mode A is caught by the contract (§7.2). Mode B is caught by the health view (§7.5). **A
third failure has now been found by accident twice, and neither mechanism catches it: records
that no feed owns at all.**

> **THE ASSERTION: every signal id prefix in `data/signals/**` MUST map to exactly one
> registry entry's `id_prefixes[]`. On any unclaimed prefix, `scripts/db.py rebuild` and
> `db.py health` FAIL and NAME THE ORPHANS — prefix, record count, and the ledger files they
> live in.**

```
$ python3 scripts/db.py rebuild
FAIL: 2 id prefixes have no registry owner (AC-F1)
  reg-      126 records   data/signals/regulation/2026-08-13.jsonl, 2026-08-14.jsonl
  dotace-    53 records   data/signals/tenders/2026-08-13.jsonl
Add id_prefixes to data/feeds.json, or add a registry row. See docs/architecture-v3.md §4.5.
```

**Why this is the generalizable fix and not another checklist item:** both orphan cohorts —
116 `reg-` records and the `dotace-`/`nen-` misattribution — were found by a human happening
to look. Nothing was watching, because **omission has no symptom**: no error, no red row, no
missing page. The assertion converts an invisible class of failure into a loud, enumerable,
build-time one. It is the difference between "we should audit attribution periodically" and
"attribution cannot silently drift."

It also **cannot rot**: it derives its expectation from the ledgers themselves rather than a
number someone typed, so a new feed that starts emitting a new prefix fails the build on its
first record instead of quietly accumulating an unowned cohort.

### 7.9 archive.org — CUT from Phase 2

**It protects zero live records today.** The feeds it would guard (`nku`, `sukl`, `nen`) are
all `planned` — they have never landed a signal — and the two feeds with volatile URLs that
*are* wired (`reddit-*`) have **zero records**. Snapshotting is work that defends an empty
set, while anonymous Save-Page-Now throttling makes ~1,200 URLs/week an hours-long queue
(digest §I). The `fragile` registry column goes with it.

**Re-add trigger:** the first record actually landed by `nku`, `nen`, `sukl` or `reddit-*`.
At that moment snapshotting defends something real, and the column comes back with it.

---

## 8. Gap-check protocol

### 8.1 The YAML shape

`SourceSchema` is `z.looseObject` (`web/lib/data.ts:48`) so these keys validate **today** —
but "already passes" means "unvalidated": a typo'd `expiers` would sit in the frontmatter
forever, rendering nothing. So they get added as typed optionals.

```yaml
sources:
  - type: gap-check
    url: https://www.ares.gov.cz/ekonomicke-subjekty?obor=35.14
    note: "No CZ vendor offering settlement/billing for energy communities; nearest is
           X (metering only, no settlement)."
    date: 2026-08-19
    queries:
      - "komunitní energetika zúčtování software"
      - "energy community billing settlement CZ"
    checked: [ares, google-cz, cz-saas-directories]
    expires: 2026-11-17          # date + 90 days
```

`checked` vocabulary — into `data/CONVENTIONS.md` beside the source-type mapping (`:105-111`):

| token | means |
|---|---|
| `ares` | ARES business register searched by NACE/obor |
| `app-stores` | Apple/Google store search for a consumer app |
| `cz-saas-directories` | CZ SaaS/vendor directories |
| `google-cz` | Czech-language web search, `hl=cs` |
| `startupjobs` | StartupJobs.cz / hiring signals for a CZ player |
| `own-funded-ledger` | our own `data/signals/funded/` searched for a CZ entrant |

### 8.2 THE LAW

1. **Decay compares against `extractDate()`, never the wall clock.** `extractDate()` is the
   newest `updated` across the register (`web/lib/data.ts:204-206`) — the same deterministic
   anchor the existing freshness rule uses (`:213-219`). Wall-clock comparison would make one
   commit build differently on different days.
2. **Expiry NEVER changes `scores.gap` and never changes the total.** It is a
   **DISPLAY-ONLY staleness flag**. The de-rank rule (`SPEC.md:133-135`,
   `pipeline/PROCESS.md:41-43`) remains the only mechanism that moves `gap`.
   **`SCORING.md` semantics are untouched — not one line of it changes in v3.**
3. Expiry is `date + 90 days`, computed once when the gap-check source is written.

### 8.3 Where the staleness flag renders

Inside the existing **gap rundown drawer** on `/problem/[region]/[id]`, as one mono meta
line under the criterion:

```
gap-check S4 expired 2026-11-17 — recheck due
```

**No new CSS classes, colours or components** — the design-language skill is binding and
`web/shared.css` is byte-locked to it. The line reuses the drawer's existing mono meta
styling. The build additionally prints the count of expired gap-checks in the run summary.

### 8.4 AC-GAP1 — the retrofit must not move a single point

The retrofit adds `queries`/`checked`/`expires` to existing gap-check sources. It is a
**metadata addition, not a re-judgement**, and there is a named check to prove it.

**Scope — the top band, five records** (`p-0001` score 10; `p-0008`, `p-0010`, `p-0023`,
`p-0028` score 7). Scope and check are stated in **separate sentences on purpose**: if the
target set later grows, a check phrased around "the five" silently under-covers, while
AC-GAP1's "every touched record" cannot.

> **MEASURED BEFORE STARTING — the scope list contains a trap.** Per-record counts of
> `type: gap-check` entries:
>
> | Record | score | `gap` | gap-check entries |
> |---|---|---|---|
> | `p-0001` | 10 | 2 | 2 |
> | **`p-0008`** | 7 | **0** | **0 — NOTHING TO RETROFIT** |
> | `p-0010` | 7 | 1 | 2 |
> | `p-0023` | 7 | 1 | 1 |
> | `p-0028` | 7 | 1 | 1 |
>
> **The retrofit's real target is 4 records / 6 entries, not 5 records.** `p-0008` is
> in-scope and **vacuous**: it scores `gap: 0` — "CZ incumbent check not done"
> (`SCORING.md:34-35`) — so it correctly has no gap-check source to extend.
>
> **`p-0008` MUST NOT HAVE A GAP-CHECK ENTRY ADDED BY THE RETROFIT.** The intuitive
> "fix" — noticing the record has none and creating one — requires doing the incumbent
> research, which moves `gap` from 0 upward, **which is precisely the `SCORING.md` violation
> AC-GAP1 exists to catch.** If `p-0008` genuinely needs a gap check, that is a MATCH-agent
> research task under the de-rank rule (§8.2), performed deliberately and scored — never a
> side effect of a metadata pass. A vacuous record is the correct outcome here; leave it
> untouched and let AC-GAP1 confirm its `score` and `gap` are byte-identical.
>
> **THE INTUITIVE FIX IS THE VIOLATION — and here is the boundary test.** If you find
> yourself **researching incumbents** during a retrofit, you have left the retrofit and
> started a **de-rank**. De-ranks belong to the MATCH agent under `SPEC.md` §4, never to a
> schema migration. Stop, leave the record alone, and hand it back.

The check itself:

> **AC-GAP1** — after the retrofit, every touched record's `score` and `scores.gap` are
> **byte-identical** to their pre-retrofit values. Only `queries`, `checked`, `expires` and
> `updated` may differ. **The checker diffs the frontmatter NUMERICALLY. Never by prose
> review.**

**Why the numeric diff is mandatory and not fussiness.** `p-0008` carries **`gap: 0`
(UNCHECKED)** — measured, `grep -o 'gap: [0-9]' data/problems/cz/p-0008*.md`. That makes it
the protocol's sharpest test: a retrofit that silently promoted an UNCHECKED gap to LIKELY
would be **exactly the `SCORING.md` violation this protocol exists to prevent**, and it
would be **invisible in prose review** — because the freshly added `queries[]` evidence
would *look* like justification for the higher score. A reader would see a well-sourced
gap-check and nod. Only the number catches it.

This is §8.2's law with a checker attached: **expiry flags staleness for display; only the
de-rank rule moves `gap`.** A retrofit is not a de-rank.

### The `note:` field — a prohibition, not a shape to preserve

**THERE IS NO CANONICAL `note:` PREFIX. Four are in use and none is authoritative.** Full
census of all 22 entries across 20 records:

```
grep -h -A3 "type: gap-check" data/problems/cz/*.md | grep "note:" \
  | sed -E "s/^[[:space:]]*note: '?//" | awk '{print $1,$2,$3}' | sort | uniq -c | sort -rn
```

| Prefix | Entries |
|---|---|
| `Absence check <date>:` | **10** (including one `Absence checks` plural) |
| `Gap check <date>:` | **7** |
| `Quick check <date>:` | **3** |
| `Incumbent re-check <date> (<flag>):` | **2** |

> **THE OPERATIVE INSTRUCTION IS A PROHIBITION: the retrofit adds `queries`/`checked`/
> `expires` as sibling keys and MUST NOT TOUCH `note:` AT ALL.** Not to normalize it, not to
> reformat it, not to "fix" the single `Absence checks` plural.
>
> **Why a prohibition rather than a shape to preserve:** a prohibition cannot be misapplied
> by a worker who encounters a fifth variant nobody has found yet. A shape-to-preserve can —
> and twice already would have. Any instruction of the form "preserve prefix X" invites
> normalizing everything that is not X.

**`p-0028` is a retrofit target and uses `Gap check`** — so a worker acting on any
two-prefix rule would hit it inside the write window.

### 8.5 A measured absence, recorded for the MATCH agent — not acted on here

The hiring probe produced a publishable absence check: **0 of 38,735 live CZ vacancies
mention accessibility or WCAG** (§13.3). It bears directly on `p-0020` (Czech e-shops and
digital services in the European Accessibility Act's first enforcement wave, with ČOI
enforcing).

**It reads two ways, and this document asserts neither:**

| Reading | Effect on `p-0020` |
|---|---|
| **An unstaffed obligation.** The duty is live and nobody has hired to meet it — the compliance gap is real and unaddressed. | **Supports** the problem: demand exists, supply does not |
| **Enforcement is not biting yet.** If nobody is staffing it, perhaps nothing is actually forcing anyone. | **Weakens urgency**: the forcing function may be theoretical |

**This is a MATCH-agent judgment call, which is precisely where SPEC §4 says region
judgment belongs.** It is recorded here as evidence with both interpretations attached so
the agent that eventually weighs it inherits the ambiguity rather than a conclusion someone
smuggled in. An absence is a strong receipt and a weak argument: it constrains what can be
claimed without settling which claim is right.

Zero is also a number that must be re-measured, not remembered — the correct citation is the
query, not the figure (see THE RECEIPTS RULE at the top of this document).

---

## 9. Naming migration map

**The vocabulary, everywhere: SIGNALS = the records. SOURCES = the feeds we ingest from.**
Two exceptions keep their names deliberately: problem frontmatter `sources[]` (those are
*citations*) and the signal field `source` (it names a feed key).

### 9.1 `data/sources/` → `data/raw/`

| File:line | Current |
|---|---|
| `scripts/fetch_ted.sh:4` | comment `(default data/sources/<today>/)` |
| `scripts/fetch_ted.sh:9` | `OUTDIR="${2:-data/sources/$TODAY}"` |
| `scripts/fetch_hlidac.sh:9` | `OUTDIR="${2:-data/sources/$TODAY}"` |
| `scripts/fetch_feeds.sh:7` | `OUTDIR="${1:-data/sources/$TODAY}"` |
| `scripts/fetch_suggest.sh:11` | `OUTDIR="${1:-data/sources/$TODAY}"` |
| `scripts/fetch_reddit.sh:11` | `OUTDIR="${1:-data/sources/$TODAY}"` |
| `pipeline/PROCESS.md:4,7,15,16` | manifest path · `mkdir` · extracts path · 28-day prune |
| `SPEC.md:235` | acceptance §9.2 — **reword, do not path-swap** (§11) |
| `.gitignore` | **DO NOT TOUCH THIS FILE.** See the standing instruction below. |

Nothing is tracked under `data/sources/` and all five scripts `mkdir -p`, so the new path
self-creates: a 12-line `sed`, no `git mv`. **`pipeline/PROCESS.md:4,7,15,16` must move in
the SAME commit as the scripts**, or hourly ingest and weekly processing write to different
trees and the prune deletes the wrong one.

> ### ⚠ STANDING INSTRUCTION TO EVERY PROGRAM AND EVERY WORKER: **DO NOT EDIT `.gitignore`.**
>
> **This file is owned by nobody and is off-limits to all programs** — this one, the
> inline-source-citations program, and anything spawned later (§12.1). It is **already
> correct for BOTH trees** — `data/sources/` *and* `data/raw/` — at two levels, verified by
> the coordinator with `git check-ignore` across seven cases (§0). The rename lands with
> **zero** ignore-file changes.
>
> This is called out as a bolded do-not rather than a footnote because it is exactly the
> file an eager builder "tidies" while renaming: the old rules mention `data/sources`, the
> tree is moving, so narrowing them to `data/raw` looks like cleanup. **It is not.** It
> would re-open a ~19 MB/day payload leak into git (`fetch_reddit` alone writes 20 files/run
> at ~43 KB) and it would un-ignore stray runner logs. If you believe `.gitignore` needs a
> change, you have found a bug in this document — stop and report it instead.

Keep the directory **date-granular** (`data/raw/<today>/`), hourly runs writing into the same
day's folder (digest §K5.1) — this keeps the 28-day prune at `PROCESS.md:16` working and
avoids 24 directories a day.

### 9.2 Site route `/sources/[type]` → `/signals/[type]`

| File:line | Change |
|---|---|
| `web/app/sources/[type]/page.tsx` → `web/app/signals/[type]/page.tsx` | move the route directory |
| `…/signals/[type]/page.tsx:54` | `SiteNav current={`/signals/${type}`}` |
| `web/lib/chrome.tsx:25-28` | the four nav hrefs → `/signals/…` |
| `web/lib/chrome.tsx:24` **and** `:38` | rename the const `SOURCE_NAV` → `SIGNAL_NAV`. The declaration is at **`:24`** (not `:25-28`, which are its array entries) and the single use at **`:38`** — those are the only two references. It is **exported**, so grep the whole tree before renaming; nothing imports it today, but the export makes that a check rather than an assumption |
| `web/lib/chrome.tsx:37` | nav label `"  ·  Sources: "` → `"  ·  Signals: "` |
| `web/app/page.tsx:75` | `<a href={`/sources/${t}`}>` — the per-type counts |
| **`web/app/page.tsx:81`** | `<a href={`/sources/regulation#${s.nextDeadline.id}`}>` — **the next-deadline deep link; missed in revision 1** |
| `web/app/page.tsx:88` | `/sources/funded` |
| `web/app/about/page.tsx:30,31,33,35` | four ledger links |
| `web/app/category/[slug]/page.tsx:80` | `/sources/funded` |
| `web/app/problem/[region]/[id]/page.tsx:286,340` | **NOT OURS — CROSS-PROGRAM HANDOFF, see §9.5.** Do not assign this to a Phase 2 worker. |
| `skills/design-language/SKILL.md:85,86` | the skill still documents `/sources/[type]` (and at `:86` records the *earlier* move from `/signals/`) — update in the same change |
| `web/shared.css:375` | **DO NOT EDIT.** It is a CSS *comment* mentioning `href="/sources/…"`. `web/shared.css` is byte-locked to `skills/design-language/assets/style.css`, and the prebuild gate `web/scripts/check-css.mjs:12-19` recomputes sha256 over both files and fails on drift. Either leave the stale comment (harmless) or edit **both** files byte-identically in one commit. Never one alone. |

> **Correction to revision 1.** That row previously quoted a specific hash as the files'
> "sha256". It was not: it was the SHA-1 that bare `shasum` emits, mislabelled. The true
> sha256 differs. **In a document whose opening rule is that every claim carries a receipt, a
> receipt written from memory is worse than no receipt** — it lends borrowed credibility to
> the claims around it. The row now cites the *mechanism* (`check-css.mjs:12-19` asserts
> equality at prebuild), which is the durable fact; a hash is a snapshot that goes stale the
> next time either file legitimately changes. The rest of this document was re-read for
> unmeasured numbers on the same pass — §0's corpus figures, the 49.4%/29.3%/70.7% split, the
> 3.63 MB size and the two run-dates were measured this session; the 500–2,000/week band was
> found unmeasured and is now labelled (§6.3).

### 9.3 Redirects — `web/next.config.ts`

```ts
const nextConfig: NextConfig = {
  async redirects() {
    return [
      // The site is publicly deployed; retired routes must not 404 (SPEC §5, amended).
      { source: "/sources/:type", destination: "/signals/:type", permanent: true },
    ];
  },
};
```

- **The pattern is `/sources/:type` — one segment — so it does NOT match `/sources` itself**,
  leaving that path free for the new feeds + health page (§4, §7.5). A bare `/sources/:path*`
  would swallow it.
- **Fragments survive.** Browsers re-apply the original fragment across a 301/308 when the
  `Location` header carries none, so `/sources/tenders#dotace-…` lands on
  `/signals/tenders#dotace-…` intact. **Do not put a fragment in the destination** — it would
  override the incoming one.

### 9.4 In-body deep links — swept anyway

The redirect keeps old links working; the sweep keeps the canonical URL correct in the data.
**9 links across 7 lines in 6 problem files**, all in `## First moves` sections (verified:
`grep -ro '/sources/tenders#' data/problems/ | wc -l` → 9):

```
data/problems/cz/p-0001-energy-community-billing-settlement.md:146
data/problems/cz/p-0002-installer-back-office.md:81, :83
data/problems/cz/p-0008-nis2-implementation-capacity.md:127          (2 links)
data/problems/cz/p-0010-trucking-back-office.md:131
data/problems/cz/p-0023-ai-accounting-capacity.md:122                (2 links)
data/problems/cz/p-0028-eshop-consumer-law-compliance.md:114
```

`SPEC.md:122` carries the same pattern in prose and moves with them.

### 9.5 CROSS-PROGRAM HANDOFF — two lines on the problem page

`web/app/problem/[region]/[id]/page.tsx` is owned by the **inline-source-citations
program**, not by this one (§12.1). Two of its lines still point at the retired route. This
is written as a handoff, with the exact edit, so whoever holds the write-lock applies it in
one pass — **no worker of ours touches this file.**

| Line | Current | Replacement |
|---|---|---|
| `:286` | ``{c.signal && <a className="ref" href={`/sources/${sig?.type ?? "funded"}#${c.signal}`}>{c.signal}</a>}`` | `/sources/` → `/signals/` |
| `:340` | ``return <span key={sid}>{i > 0 && ", "}<a href={`/sources/${sig.type}#${sid}`}>{sid}</a></span>;`` | `/sources/` → `/signals/` |

**Urgency: low, and stated honestly.** Both are **non-breaking either way** — the permanent
redirect at §9.3 catches them, fragment intact. The cost of leaving them stale is a
**redirect round-trip on every source link of every rundown page**, which is the most-used
provenance path on the site. Worth fixing, not worth a collision.

**Timing is free-running:** it can land before, during, or after our rename, because the
redirect covers the window in both directions.

### 9.6 The new `/sources` page

`web/app/sources/page.tsx` — the feeds registry **and** the health ledger in one table
(§4, §7.5): name · yields · type · cadence (target) · runner · status (intent) · **state
(observed)** · last success · items last run · 7-day yield · blocker/error. Reuses
`table.index` and the existing chrome; stamp red for BROKEN; no new design vocabulary. **A
public page that admits which of its own feeds are broken is the receipt discipline applied
to ourselves.**

---

## 10. BLOCKERS REGISTER

| # | Feed / capability | What blocks it TODAY | Workaround in place | Owner action — exact command |
|---|---|---|---|---|
| **0** | **THE direnv → sops HOOK** — narrowed, and it STILL STANDS | **The hook exports nothing.** Coordinator-measured, names only: `env \| cut -d= -f1 \| sort -u` vs `direnv exec . env \| cut -d= -f1 \| sort -u`, then `comm -13` — the **only** keys added are `DIRENV_DIFF`, `DIRENV_DIR`, `DIRENV_FILE`, `DIRENV_IN_ENVRC`, `DIRENV_WATCHES`. The `.envrc` hook fires and prints "direnv: using sops .env.enc" **with no error**, so it fails **silently**. **CORRECTED SCOPE: the VAULT IS FINE — `with-secrets` reads it and Hlídač is live (row 1). What is broken is the HOOK, not the secrets.** The earlier "empty vault" reading was the discredited negative (row 1a). | **YES, and it is already in the code:** every script routes secrets through **`with-secrets`**, never the shell — see `scripts/ingest.sh:7-20`, which documents the abandonment of `direnv exec`. | Fixing the hook is optional, not blocking. **Do NOT read this row as vindicating direnv:** `direnv exec .` remains a broken path and must not be reintroduced into any runner, wrapper or plist. |
| 0a | **RESOLVED — the two unverified claims are now measured** | Row 0a previously flagged `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` as UNVERIFIED, because both were declared ABSENT by the same direnv probe that reported `HLIDAC_STATU_TOKEN` missing when it was present (row 1a) — a probe with no positive control. Both have now been tested through the **working** path. **`ANTHROPIC_API_KEY`: PRESENT and authenticating** (row 2). **`OPENAI_API_KEY`: genuinely ABSENT** — confirmed without decrypting anything, since sops keeps key names in plaintext and the full key list for this project is exactly `HLIDAC_STATU_TOKEN` and `ANTHROPIC_API_KEY`: `grep -oE '^[A-Za-z_][A-Za-z0-9_]*=' .env.enc \| grep -v '^sops_'`. **So one false absence and one true absence — the probe was wrong about Anthropic and right about OpenAI, which is exactly why it needed a control.** | The embeddings backfill (§6.3, §12) remains genuinely blocked on OpenAI. | **Add `OPENAI_API_KEY` via `sops-edit .env.enc`** if the backfill is wanted. Nothing to do for Anthropic. |
| 1 | **Hlídač** (`hlidac`, tenders) | **RESOLVED — THE FEED IS LIVE.** W2 ran it end to end: **7/7 queries HTTP 200, 1,061 contracts, zero login pages**; coordinator independently confirmed with `with-secrets curl --variable '%HLIDAC_STATU_TOKEN' --expand-header …` → HTTP 200. **The token exists under `HLIDAC_STATU_TOKEN`, not `HLIDAC_TOKEN`** — recorded here so nobody re-derives it. | n/a — **the earlier "tenders ledger is TED-only" consequence was FALSE and is struck.** | **None.** |
| 1a | **How row 1 was wrong — the shape recurs, so it is recorded** | `HLIDAC_TOKEN` was tested through the **working** path (`with-secrets`) and genuinely failed to expand. `HLIDAC_STATU_TOKEN` was tested only through the **broken** path (direnv, which exports nothing), and its emptiness was read as absence. **Two half-tests, each valid alone, combined into a false conclusion.** | — | **THE RULE: a negative result is only evidence when the method is known to produce positives.** The direnv probe had **no positive control**, so its "MISSING" meant nothing — it would have reported every name in the vault as missing, including the ones that are there. |
| 2 | **UNATTENDED model passes** — scoring, generation, **and LLM-fallback recovery (§7.7)** | **RESOLVED — THE KEY IS PRESENT AND AUTHENTICATES.** Re-tested via `with-secrets` exactly as row 0a demanded: `curl --variable '%ANTHROPIC_API_KEY' --expand-header 'x-api-key: {{…}}'` → `GET /v1/models` **HTTP 200**, and a live `POST /v1/messages` (claude-haiku-4-5, max_tokens 4) → **HTTP 200** with a real completion. The ABSENT reading was the discredited direnv probe, precisely as row 1a predicted. What still stands: ambient CLI auth fails (sandboxed keychain denied; unsandboxed OAuth expired, digest §H), so the key must be passed **explicitly**. | ATTENDED mode needs no key and works today (§1.2); the mechanical path stages records and prints `SKIP model passes` (§1.3). | **Do NOT add a second key — the vault already has one.** What remains is plumbing only: hand the value to the nested `claude -p` without an interpreter touching it. Note `with-secrets` refuses bash/node/python by design, so an unattended wrapper should call `sops -d --input-type dotenv --output-type dotenv .env.enc` itself — that allow-list constrains Claude, not your automation. |
| 3 | **Vestbee** (`vestbee`, funded) | **DEAD** — measured: 301 → `/insights/rss.xml` → 404 (digest §A). **Claim verified, not relayed.** | **REMEDIATED IN CODE:** removed from `scripts/fetch_feeds.sh:133-134` with the reason recorded inline; `status: dead` in the registry. | **None.** |
| 4 | **All RSS/JSON feeds** (`cc-cz`, `yc-oss`) | **FIXED.** The bug was real and measured — `curl -sL` without `-f` saved the 404 body and printed `OK`. **Silent data loss dressed as success: the moat leaking.** Still the first Mode-A receipt in §7.1. | **REMEDIATED IN CODE:** `scripts/fetch_feeds.sh:110` now uses `curl -fsSL --retry 2 --remove-on-error`, with `:97-105` recording *why* `-f` is load-bearing and the exact reproduction. `--remove-on-error` additionally guarantees no partial file survives. | **None.** |
| 5 | **EC Have Your Say** (`ec-hys`) | `ec.europa.eu` fails locally with **curl exit 60 — TLS interception by the sandbox proxy**, NOT a remote refusal (digest §A). Only host needing an override. | Run that fetch with the sandbox disabled, or from the cloud runner (EC is cloud-OK). | **None** required. To keep it sandboxed, allowlist `ec.europa.eu` via `/sandbox`. |
| 6 | **TED · Reddit · Suggest · NKÚ · NEN** — cloud viability | **UNDECIDABLE.** All 200 from this Mac; the known TED 403 came from Claude-cloud egress, a different network from GitHub's Azure ranges. **Not answerable from this machine.** | All five default to `runner: local`, `blocker` = "cloud viability unmeasured". | `gh workflow run ingest.yml -f mode=probe && gh run watch` (§5.2) |
| 7 | **sqlite-vec / KNN shortlisting** | **Extension NOT INSTALLED**: `find_spec('sqlite_vec')` → False; `USING vec0` → `no such module: vec0`; no dylib. (`enable_load_extension` works, so the host is capable.) | IČO / domain / name joins need no extension and cover Phase 2 matching. | Phase 3 prerequisite: install into a project venv (e.g. `uv pip install sqlite-vec`) and re-run `python3 scripts/db.py embed`. |
| 8 | **Google Suggest** (`suggest`) | Ban risk, not freshness: 144 queries/run (24 seeds × 6 patterns, `fetch_suggest.sh:17,21`). | Cadence capped **≤1×/day** — the cap IS the mitigation. Requires `ie=utf-8&oe=utf-8` or the body is non-UTF-8 (already at `fetch_suggest.sh:28`). | **None.** |
| 9 | **`suggest`, `reddit`, `cc-cz`** — end-to-end proof | **ZERO records since inception** (§0). Nothing is technically blocked; the path has simply never completed, and **nothing was watching for the silence**. | None today. §7.5 makes it visible as `PENDING` on a public page. | **None.** Phase 3's sharpest target. |
| 10 | **GitHub Actions** | No `.github/` directory yet. Remote exists: `github.com/mchlkucera/localproblems`. | None. | **None** — coordinator commits the workflow at CP2. |
| 11 | **launchd local runner** | macOS **TCC** may deny a launchd-spawned process access to `~/Documents`, silently, with EPERM. | Plist ships committed and **not loaded**. | Install per §5.4, approve the prompt on first `kickstart`, verify with `log show --predicate 'process == "direnv"' --last 10m` |
| 12 | **NKÚ** (`nku`) | **NOT BLOCKED. Both stated reasons were FALSE and are struck.** W2 measured `www.nku.cz` returning **200** with curl's default UA — **byte-identical 28,795 B** to non-www, **no 403** — and uppercase `VESTNIK.asp` returning **200 with no redirect**. "www 403s generic fetchers" and "uppercase 301s to http" were relayed from the feeds research and are wrong. **Deleted rather than left as folklore a future worker would trust** (`scripts/fetch_nku.sh:105` already records the measurement). | **Keep non-www** — it works and is mandated (`scripts/fetch_nku.sh:113`); it simply is not a workaround for a 403 that does not exist. | **None.** |
| 13 | **Reddit** (`reddit-*`) | All public `.json` endpoints 403 for non-browser clients. | **In place:** `.rss` + descriptive UA + `--retry --retry-delay 35` (`fetch_reddit.sh:19`). | **None.** |
| 14 | **HIRING stream** (§13) | **RESOLVED — not a blocker.** The probe answered the decisive test: **99.90% IČO coverage** on MPSV/ÚP `volna-mista`, ARES join verified live, licence disclaims copyright and the sui-generis DB right (§13.0). What remains is build scope, not an unknown. | The Phase 2 cheap half ships regardless; the fetcher is a parallel worker that may slip to Phase 3 without blocking CP2 (§13.5). | **None.** |
| 15 | **Job boards** — StartupJobs · jobs.cz · prace.cz · LinkedIn | **RESOLVED as NOT AVAILABLE**, with clauses on file: StartupJobs VOP *"je výslovně zakázáno databázi vytěžovat"*; jobs.cz/prace.cz Alma Career terms §4.11; LinkedIn `robots.txt: Disallow: /`. **This is a clean negative, which is worth more than a vague maybe** — recorded as `access.verdict: forbidden` in the registry so it is not re-litigated (§13.8). | **We never build against a source whose terms forbid it.** MPSV supersedes all of them anyway, with better data. | **None. Closed.** |
| 16 | **MPSV personal data** (`mpsv`) | The dataset's DCAT record declares **`obsahuje-osobní-údaje`** — contact names, emails, phones. MPSV's site-wide terms say otherwise but are stale (2022) and contradicted by the per-dataset metadata; **trust the metadata**. Our ledgers are append-only and public, so a leak is permanent and public. | **Blocking by construction:** AC-GDPR1's allowlist + checker ship in Phase 2 **before** any fetcher can write a record (§12 item 15, §13.6). | **None** — engineering obligation, not an owner action. |
| 17 | **marduk runner** | No marduk age key in `.sops.yaml`; no push credential. | None — launchd is primary. | (a) `gh auth login` or a deploy key; (b) add marduk's age public key to `.sops.yaml`, then `sops updatekeys .env.enc`; (c) clone + `direnv allow`. |

---

## 11. SPEC amendments

Applied to `SPEC.md` by a Phase-2 agent.

> ### ⚠ THE LINE NUMBERS BELOW HAVE ALREADY DRIFTED. USE THE QUOTED TEXT.
>
> `SPEC.md` grew **277 → 287 lines** while this document was being written — the
> inline-source-citations program landed its `[Sn]` spec (now `SPEC.md:120-122`) and a
> `lint-citations.mjs` prebuild block (now `:164-167`). **Every anchor below shifted, and NOT
> by a uniform amount:** two insertion points produced a +5 zone and a +10 zone, so "just add
> 10" is wrong.
>
> **Do not trust any number in this table. Locate each target with:**
> ```
> grep -n "<the quoted text from the row>" SPEC.md
> ```
>
> Measured mapping at time of writing (doc value → actual), kept so a reader can confirm the
> drift is real — not as something to rely on:
>
> | doc says | actual | doc says | actual |
> |---|---|---|---|
> | `28-38` | **30** | `180-185` | **189** |
> | `44-51` | **45** | `199` | **209** |
> | `62-73` | **63** | `232-234` | **242** |
> | `108` | **108** (unmoved) | `235` | **245** |
> | `122` | **127** | `242` | **252** |
> | `156-157` | **161** | `253` | **263** |
> | `166` | **176** | `254` | **264** |
> | `170` / `172` | **180** / **182** | `267-277` | **281** |
>
> This is THE RECEIPTS RULE firing on this document's own citations, inside a day, from one
> parallel checkpoint. It is the concrete case for *cite the quoted text, not the line
> number* — and it will happen again before Phase 2 lands.

| Target | Current | Amendment |
|---|---|---|
| `SPEC.md:199` (§7) | "**SQLite / Postgres / servers / embeddings** — tripwires only (§10)." | "**Postgres, database servers, queues, client-side apps** — banned. **SQLite + embeddings** are sanctioned (owner, 2026-08-20) as a **gitignored, rebuildable working store** only: `data/register.db`. Never a publication dependency — `trash data/register.db && npm --prefix web run build` must stay green." |
| `SPEC.md:253` (§10) | ">~400 problems … \| SQLite + embeddings" | Mark **graduated by owner decision 2026-08-20, not by threshold** — 31 problems / 6,181 signals, far under >~400. Keep the row visible with that note. |
| `SPEC.md:254` (§10) | ">~10 sources, or silent fetch failures \| GitHub Actions cron" | Mark **FIRED**: 14 feeds; `scripts/fetch_feeds.sh:11` is a documented silent 404-as-success. Warrants §5 and §7. |
| `SPEC.md:28-38` (§2) | one weekly loop | Split into **INGEST** (hourly-ish, objective, `pipeline/INGEST.md`) and **PROCESSING** (on-demand judgment, `pipeline/PROCESS.md`). **Keep `SPEC.md:37-38` verbatim** and append: "a gitignored SQLite working store is not a database server: nothing serves it and nothing reads it at publish time." |
| `SPEC.md:44-51` (§3 layout) | `data/signals/…` | Add `data/raw/<run-date>/   # raw payloads; gitignored except manifest.md; pruned at 28 days`. Add `hiring/` to the evidence-type list when §13 lands. |
| `SPEC.md:62-73` (§3 schema) | record schema | Add optional `quote`, `http_status`, `fetched_at`, **`extraction`**; note they must be added to `SignalSchema` in the same change. |
| `SPEC.md:108` (§4 frontmatter) | `sources[] {type,url,note,date,signal?,dims?}` | Add `queries?[]`, `checked?[]`, `expires?` for gap-check sources; expiry is display-only and never moves `gap`. |
| `SPEC.md:122` (§4) | "(`/sources/tenders#dotace-...`)" | → `/signals/tenders#dotace-...` |
| `SPEC.md:166` (§5 route table) | `/sources/[type]` row | → `/signals/[type]`; **add a row** for `/sources` — the feeds registry **and feed-health status ledger** (§7.5). |
| `SPEC.md:170` (§5) | "nav reads `Problems` then `Sources: Funded · …`" | → "`Problems` then `Signals: Funded · Regulation · Tenders · Demand`" |
| `SPEC.md:172` (§5) | "Nothing else: **no redirects (v1 was never publicly deployed)**, …" | **The redirects clause must go.** → "permanent redirects for retired routes only (the site is publicly deployed), no test suite, no OG images, no middleware, no API routes." |
| `SPEC.md:180-185` (§5 deploy) | "(Git-driven deploys become possible once a GitHub remote exists…)" | The remote **now exists**. Reword: the remote exists; local-prebuilt stays because the app reads `../data`, which remote builders cannot see. |
| **`SPEC.md:232-234` (§9.1)** | "A fresh Claude session given only **pipeline/PROCESS.md** runs **fetch → normalize** → match → score → build → newsletter → commit" | **False after the split** — fetch and normalize move to `pipeline/INGEST.md`. → "A fresh Claude session given only `pipeline/INGEST.md` runs fetch → contract-check → normalize; given only `pipeline/PROCESS.md` runs match → score → build → newsletter → commit. Neither asks questions; failures land in the run manifest, never fatal." |
| `SPEC.md:235` (§9.2) | "re-run against the existing `data/sources/2026-08-13/` snapshot" | **REWORD OR RETIRE — not a path swap.** That snapshot was deleted in `96fd405`, and `data/raw/` is pruned every 28 days, so a path swap leaves it unrunnable. Replacement: "**Normalize is objective:** a re-run over the newest `data/raw/<date>/` payloads keeps hundreds of TED records (vs 11 in v1); `jq` parses every JSONL line; ids unique against `seen.txt`; a second run is append-only (git diff proves it); `python3 scripts/db.py rebuild` exits 0 with `jsonl_lines == signals_count`." |
| `SPEC.md:242` (§9.5) | "only SPEC / SCORING / **TASK** / CONVENTIONS / FOUNDER VISION + `data/` `scripts/` `web/` `newsletter/` `skills/` + `docs/archive/`" | `TASK` no longer exists (`af63331`). → "only SPEC / SCORING / CONVENTIONS / FOUNDER VISION + `pipeline/` (both entry points + the prepared launchd plist) + `data/` `scripts/` `web/` `newsletter/` `skills/` + `docs/` (sources catalog, architecture, `archive/`)." The list already fails as written — `docs/sources-catalog.md` and `docs/FOUNDER VISION.md` sit outside `docs/archive/` today. |
| `SPEC.md:267-277` (§12 doc map) | five document rows | Add: **`pipeline/`** as a **FOLDER** row (both entry points); `data/feeds.json` — "the feeds registry + per-feed contracts — binding"; `data/feed_health.json` — "observed feed health, generated"; `docs/architecture-v3.md`; `docs/sources-catalog.md` — advisory. |

### 11.1 Outside SPEC, same pass

| Target | Current | Amendment |
|---|---|---|
| `pipeline/PROCESS.md:60-61` | "git push **(skip push while no remote exists)**" | **Stale** — `origin` exists. Remove the parenthetical. |
| `pipeline/PROCESS.md:4,7,15,16` | `data/sources/…` | → `data/raw/…` — **same commit as the scripts** (§9.1) |
| `pipeline/PROCESS.md:18-29` | step 2 NORMALIZE | Moves to `pipeline/INGEST.md`; PROCESS keeps a one-line pointer. Steps 3–7 unchanged, **plus** the `match_log` append command (§2.5) in step 3 and the BROKEN-feed escalation line (§7.6) in the run summary. |
| **`README.md:15`** | "the whole **pipeline is launchable by Claude from this file alone**" | **False after the split** — name both entry points: `pipeline/INGEST.md` (fetch + normalize) and `pipeline/PROCESS.md` (match → deploy). Same correction at `README.md:14,24,30`. |
| `data/CONVENTIONS.md:27-46` | record schema | Add optional `quote`, `http_status`, `fetched_at`, `extraction` |
| `data/CONVENTIONS.md:105-111` | source type → dimension | Add the `checked` vocabulary (§8), the gap-check expiry law, and `hiring` → demand/money, **never proof** (§13.9) |
| `web/lib/data.ts:16` | `EVIDENCE_TYPES = ["funded","regulation","tenders","demand"]` | Gains `"hiring"` — **in the same checkpoint as the first hiring record, not before** (§13.5). Lights up `/signals/hiring` via `generateStaticParams`, and forces `TITLES`/`DESCRIPTIONS` entries by TypeScript exhaustiveness |
| `web/lib/data.ts:25` | `source: z.enum([…])` | Gains **`"nen"`, `"dotace"`** (§4.5 — so new records can carry a correct `source` instead of the legacy `hlidac`) and **`"mpsv"`** (§13). **Self-enforcing: `z.enum` fails loudly**, unlike the `z.object` strip (§3). **Do NOT retro-edit the 349 committed records** whose `source` is legacy-wrong — append-only is law, and the discrepancy is documented in §4.5 |
| `SPEC.md:170` + `skills/design-language/SKILL.md:86` | nav lists **four** ledgers | The nav gains a **fifth**: `Signals: Funded · Regulation · Tenders · Demand · Hiring`. Both files state the four explicitly and must move together; the skill is binding, so `SKILL.md` is not optional |
| `web/lib/data.ts:23-41` | `SignalSchema = z.object` | → **`z.strictObject`** + the four optional receipt fields. **Also make the nested `scores: z.object` at `:34-39` strict** — `strictObject` is top-level only, so the trap otherwise just moves one level down (§3, AC-Z2). |
| `web/lib/data.ts:48` | `SourceSchema = z.looseObject` | Add typed optionals `queries`, `checked`, `expires` — keep it loose |
| `web/lib/data.ts` (new) | — | Load + zod-validate `data/feeds.json` and `data/feed_health.json`; assertions AC-F1/AC-F2 (§4.3) |
| `skills/design-language/SKILL.md:85,86` | `/sources/[type]` route names | → `/signals/[type]`; nav label `Signals:`; add the `/sources` feeds + health page |

**`SCORING.md`: zero changes.** Stated explicitly because §8 touches gap display.

---

## 12. Now / Later

### 12.1 File ownership — read this BEFORE assigning any Phase 2 work

A second program runs in parallel in this repo: **inline source citations on problem
records**. A Phase 2 worker must not discover this boundary by colliding with it.

| Owned by the **citations program** — we do not touch | Owned by **this program** |
|---|---|
| `data/problems/cz/*.md` | `pipeline/` |
| `web/lib/md.ts` | `scripts/` |
| `web/app/problem/[region]/[id]/page.tsx` | `data/signals/` · `data/feeds.json` |
| the **citation-related** sections of `CONVENTIONS.md`, `SPEC.md`, and the design skill | `web/app/sources/` (and `web/app/signals/` after the rename) |
| | the **`SignalSchema` portion** of `web/lib/data.ts` |
| | uncontested, needed for the rename: `web/next.config.ts` · `web/lib/chrome.tsx` · `web/app/page.tsx` · `web/app/about/page.tsx` · `web/app/category/[slug]/page.tsx` |

> ### ⚠ THREE FILES ARE OWNED **IN PART BY BOTH PROGRAMS, CONCURRENTLY**
>
> **`SPEC.md`, `data/CONVENTIONS.md` and `skills/design-language/SKILL.md`** are being edited
> by **both** programs at the same time: we own the non-citation sections, they own the
> citation sections — **inside the same files.**
>
> **"We own part of a file" is a sharper hazard than "we own a file", and a worker will not
> infer it from the table above** — a table that lists a file under one owner reads as
> whole-file ownership. Hence the required working method:
>
> - **Small, surgical edits against unique text anchors.** Never a whole-file write, never a
>   bulk reformat, never a "while I'm in here" tidy.
> - **Re-read the file immediately before each edit.** Not at the start of the task — before
>   *each* edit. `SPEC.md` moved 277 → 287 lines mid-task (§11); anything you read ten
>   minutes ago may already be wrong.
> - **If an anchor no longer matches, STOP and re-locate it** with `grep -n` on the quoted
>   text. A failed match means the file moved under you, not that the anchor was wrong.
>
> This is the same discipline §11's drift warning demands, applied to writes instead of
> citations.

**`.gitignore` is owned by NOBODY and is off-limits to EVERY program.** See §9.1.

**Two cross-program handoffs are open:**

1. **The problem-page line sweep** (§9.5) — `web/app/problem/[region]/[id]/page.tsx:286,340`
   still point at `/sources/`. Specified there with the exact replacement, assigned to
   whoever holds that file's write-lock. **Not ours to apply.** Non-breaking either way; the
   cost of delay is a redirect round-trip on every rundown page's source links.
2. **The gap-check retrofit** (§8) — **ARBITRATED AND RESOLVED: option B, a sequential
   write window.** The schema half (`SourceSchema` typed optionals, `web/lib/data.ts:48`) is
   ours and ships in Phase 2. The data half — writing `queries`/`checked`/`expires` into
   problem frontmatter — is **gated on the citations program's checkpoint landing**, after
   which this program takes an **exclusive write window on `data/problems/cz/`**.

   **Why sequential rather than handing them a specified diff** — this generalizes to every
   future collision, so it is worth the line: *a specified diff crossing a program boundary
   means one team writes semantics that another team applies without understanding them, and
   the applying team's checker cannot catch a semantic error it was never briefed on.*
   AC-GAP1 (§8.4) is exactly such a checker: it only works in the hands of someone who knows
   why `gap` must not move.

   **The latency is nearly free.** Phase 2's DB layer, ingest path, feeds registry, naming
   migration, health view and `INGEST.md` touch **none** of `data/problems/` — so the entire
   NOW list except this one item proceeds in parallel with the wait.

   > **VINDICATED BY A NEAR-MISS WITH A TIMESTAMP — this is not a hypothetical.** While this
   > section was being written (2026-08-20), `p-0001`, `p-0023`, `p-0028` and `p-0024` all
   > changed on disk. **Three of those four are retrofit targets.** The citations program was
   > inside those exact files at that moment. Had we shipped the rejected route — a specified
   > diff applied by the other team — **two programs would have been writing the same three
   > files simultaneously, that day.** A rule with a receipt behind it survives contact with a
   > future worker who thinks the rule is bureaucratic; this is that receipt.
   >
   > **AND THE LOCK RULE THAT FOLLOWS FROM IT: an absence of collisions in our own tree is
   > NOT evidence the lock is free.** The only valid signal to open the window is **the
   > coordinator confirming the citations checkpoint is committed.** Not a quiet
   > `git status`. Not four hours without a change. Not "it looks idle." Quiet means nothing
   > — the near-miss above happened during a window that looked exactly like quiet from our
   > side.

**Two lints, one question, deliberately split** (§7.8): theirs resolves marker→source on the
register side; ours checks claim→quote on the ingest side. Neither may grow into the other's
half.

**`quote` is a shared contract, not an internal field** (§7.8): the citations program is
building a reveal on top of it and will not block on us, so its shape — verbatim snippet +
source, retrievable by signal id — is fixed.

### 12.2 Every acceptance check must be PROVEN CAPABLE OF FAILING

Per the receipts rule: a green check that has never been shown red is not evidence. Each
check below names **the input that makes it fail** — run that first, watch it go red, then
trust the green.

| Check | Proven capable of failing by |
|---|---|
| **AC-DB1** (fresh clone builds with no DB) | point `data.ts` at a non-existent `data/` path; the build must fail. Then restore and confirm green |
| **AC-Z1/Z2** (strict schema) | add a scratch key to one JSONL line; `z.strictObject` must fail the build. **Also test the NESTED case** — a key inside `scores` — since that is the half that silently passed before |
| **AC-Z3** (`quote` reaches the page) | blank one record's `quote`; the rendered page must visibly lose it. A field that renders identically when empty is not being rendered |
| **AC-F1** (prefix totality) | invent a `zzz-` id in a scratch ledger line; rebuild must FAIL and name `zzz-`. **This check passed for weeks while 116 records sat unowned — it is the reason this table exists** |
| **AC-F2** (no orphan scripts) | point one registry `script` at a deleted path |
| **AC-GAP1** (retrofit moves no points) | hand-edit one record's `scores.gap` by +1 in a scratch copy; the numeric diff must catch it. Prose review must NOT be the detector |
| **AC-GDPR1** (no personal data) | **the standard-setter — plant an email address and watch the checker match it**, exactly as W1 did, before trusting a zero-match run |
| **AC-SCORE1** (scorer accuracy) | feed it a record with a known-wrong score and confirm the comparison flags it; a harness that cannot detect a planted error cannot validate the model |
| **contract checks** (§7.2) | point one feed at a URL returning a 200 with an empty body — the `dotace`/vestbee shape. It must go BROKEN, not LIVE |

**Where a check cannot be shown to fail, say so and treat its green as unverified** rather
than as a pass.

### NOW — Phase 2 (CP2: `npm --prefix web run build` green)

1. **Naming migration** — `data/sources/`→`data/raw/` across 5 scripts + `PROCESS.md` (one
   commit); `/sources/[type]`→`/signals/[type]`; nav label; **10** in-code link sites incl.
   `web/app/page.tsx:81`; the 9 in-body deep links; permanent redirect; skill doc. (§9)
2. **`data/feeds.json`** — registry + **per-feed `contract` and `access` (ToS) fields** +
   the new `/sources` page + AC-F1/AC-F2. (§4)
3. **Bug fixes that stop the moat leaking** — `fetch_feeds.sh:11` gains `-f`; Vestbee removed
   and marked dead. (§10 rows 3–4)
4. **`scripts/normalize.py`** — the missing artifact revision 1 assumed. Inputs:
   `data/raw/<date>/` + `data/feeds.json`. Outputs: `data/signals/<type>/<date>.jsonl`,
   `seen.txt`, contract results for `fetch_log`, and a pending-list in the manifest. **Owns
   every cell marked `script` in §1.3**: id minting, `seen.txt` dedup, structured field
   extraction, TED CPV→sector, `scores.money`, dated `scores.urgency`, the materiality
   filter, `quote` extraction, liveness. **`--mechanical-only` STAGES to
   `data/raw/<date>/staged.jsonl`; it does NOT append to `data/signals/` and does NOT touch
   `seen.txt`** (§1.3) — every record still needs model-scored `scale` + `recurrence`, and
   §6.2 forbids defaults. A second invocation completes staged records once a model is
   available, which is what makes the degraded unattended mode (§5.6) and the AC-SCORE1
   fallback (§6.5) buildable.
5. **`scripts/db.py`** — DDL, `rebuild` (with the `jsonl_lines == signals_count` assertion),
   `upsert`, `fetchlog`, `health`, `match`, entity keys, WAL. No vec tables. (§2)
6. **`pipeline/INGEST.md`** (the ATTENDED path, works today) + `scripts/ingest.sh` +
   `scripts/fetch_all.sh` with **explicit per-feed argv** (§5.3); PROCESS slimmed. (§1, §5)
7. **Receipt fields** — `quote`, `http_status`, `fetched_at`, `extraction` in JSONL **and**
   `SignalSchema` (`z.strictObject`, inner object too) in the same commit. (§3, §7.8)
8. **THE FRAGILITY TIER (bounded)** — contract fields + `fetch_log` health columns +
   `data/feed_health.json` + the `/sources` status ledger + escalation at 3 BROKEN runs.
   **LLM-fallback extraction ships for ONE feed only: `nku`** (plus its small
   `scripts/fetch_nku.sh`). (§7)
9. **Gap-check retrofit — SPLIT, SEQUENCED (see §12.1 handoff 2).** Ships now: the typed
   optionals on `SourceSchema` (`web/lib/data.ts:48`) and the `checked` vocabulary in
   `CONVENTIONS.md`. **Gated on the citations program's checkpoint**, then an exclusive write
   window on `data/problems/cz/`: the frontmatter fields and the expiry line in the gap
   drawer. **Gated by AC-GAP1** (§8.4) — `score` and `scores.gap` byte-identical afterwards,
   diffed numerically, never by prose review. (§8)
10. **Prepared runners** — `.github/workflows/ingest.yml` (`workflow_dispatch` only, cron
    commented) + `pipeline/launchd/…plist` (committed, not loaded). (§5)
11. **Warning-only checks** — the **ingest-side** claim lint (claim→quote only; the
    marker→source lint is the citations program's, §7.8) + provenance completeness. (§7.8)
12. **Amendments** — SPEC / PROCESS / CONVENTIONS / README / SKILL.md. (§11)
13. **The evidence-type checklist** (§13.2) written into `data/CONVENTIONS.md` — reusable
    for any fifth type.
14. **The hiring stream, cheap half only** (§13.5): `hiring` type registration, the `mpsv`
    and `ares` registry rows with contracts and ToS verdicts, and the expected-absence
    concept. **The MPSV fetcher is a separate parallel worker and MAY SLIP TO PHASE 3
    WITHOUT BLOCKING CP2** — `web/lib/data.ts:175` renders a registered-but-empty ledger
    correctly, so a late fetcher costs nothing, while a rushed one writing personal data
    into an append-only public log costs everything.
15. **AC-GDPR1 — the contact-field allowlist and its dedicated checker** (§13.6). Allowlist,
    never denylist: a denylist fails OPEN the day MPSV adds a field. The checker greps the
    produced JSONL for email and phone patterns and requires **zero matches**; it runs in the
    ingest path before append **and** in the build gate. This ships in Phase 2 even though
    the fetcher may not — **the rule must exist before the first record can be written**,
    not alongside it.

### LATER — deferred, each with its reason

| Deferred | Reason | Re-add trigger |
|---|---|---|
| **sqlite-vec + KNN shortlisting** | **The extension is not installed** (§0) and MATCH has no consumer yet. IČO/domain/name joins cover Phase 2. | Install (`uv pip install sqlite-vec`) **and** a MATCH consumer — both, Phase 3 |
| DB `feeds` table | Nothing queries a mirrored registry | first SQL join of `fetch_log` to feed metadata |
| DB `problem_sources` table | No Phase 2 consumer | Phase 3, with the KNN shortlist |
| archive.org + `fragile` | **Protects zero live records today** (§7.9) | first record landed by `nku` / `nen` / `sukl` / `reddit-*` |
| Near-duplicate **auto**-linking | Report-only first; a human reads one report before anything auto-links | one reviewed report |
| **Claim lint as a build failure** — and the citations lint with it | **RULED: both lints stay warning-only** (§7.8). A gate two independent programs can each turn red is a gate neither owns; until the conditions hold, **a red lint trains people to work around it, which is worse than no lint at all** | **A COORDINATOR decision, gated on all three** of §7.8's conditions: (a) citations content pass landed with a baseline coverage number, (b) FP rate **measured** against that baseline — the 20–40% here is an estimate, (c) both leads agree the findings are anomalies, not routine noise. **Neither program may promote unilaterally, nor weaken the other's lint** |
| **Provenance completeness** as a build failure | Ours alone — no cross-program constraint, so this one is not covered by the lint ruling | 100% for two consecutive runs |
| INGEST committing / pushing | A bot writing to the publication spine is a bigger promise than freshness buys | ten clean cycles |
| Anthropic **Batch API** | Halves an already-small cost in exchange for a polling state machine | >5,000 new signals/week |
| Escalation beyond the run summary (email/push) | §7.6 is deliberately boring; alerting is infra | belongs in SPEC §10's tripwire table first |
| marduk runner | Needs owner credential + age-key work (§10 row 16) | owner does (a)(b)(c) |
| New fetchers — SÚKL, EC HYS, NEN | Phase 3; the registry carries them as `planned` so `/sources` tells the truth meanwhile. **Priority is the catalog's own list** (`docs/sources-catalog.md:154-159`): NKÚ → ochrance.cz → Have Your Say → SÚKL → ČOI. **NKÚ is pulled forward into Phase 2** as the LLM-fallback proof feed (§7.3). **NEN is NOT on that list** — it comes from the wave-2 additions (`docs/sources-catalog.md:170-172`) and has no assigned priority | — |
| Enabling the Actions cron | One-line uncomment, deliberately human | probe green + one clean local cycle |
| **The MPSV fetcher + aggregation pass** | **Not blocked — deliberately parallelized.** The probe came back positive (§13.0), so this is scope, not uncertainty. It is a separate worker precisely so it **cannot block CP2**: a registered-but-empty `hiring` ledger renders correctly (`web/lib/data.ts:175`), so a late fetcher costs nothing. The Phase 2 half that must not slip is the **GDPR allowlist + checker** — the rule has to exist before the first record can be written (§12 item 15) | fetcher lands whenever it lands; schema edits ride with the first record |
| **ARES enrichment beyond the IČO join** | The join is verified (§13.0), but NACE/size/region enrichment has no consumer until MATCH uses it | a MATCH pass that reads entity attributes |
| `bootstrapped` type · second region · `demand_score` diversity multiplier | Untouched by v3 (`SPEC.md:206,260-261`) | — |

### The three things that would make Phase 3 a real win

1. **Prove one demand feed end to end** — `suggest` or `reddit`, fetch to rendered signal.
   Both at zero records; a feed that has never landed a record is not a feed.
2. **Run AC-SCORE1** (§6.5) and publish the numbers, including if they are bad.
3. **Run the egress probe** (§5.2) — five UNDECIDABLE registry cells become measured.

---

## 13. Adding an evidence type — and the hiring seam

Owner mandate M1. The deliverable is **both** the reusable checklist (§13.2) and — since
the decisive test came back positive — a scoped hiring build (§13.5).

### 13.0 The decisive test: ANSWERED, and it passed

§13.4 of revision 2 said one fact should size the whole investment: **does the source carry
IČO?** The probe answered it.

| Field | Coverage on MPSV/ÚP `volna-mista` open data |
|---|---|
| **`ICO`** | **2,088 of 2,090 records — 99.90%** |
| CZ-ISCO occupation code | 100% |
| salary floor | 100% |
| NUTS-3 region | 94% |

The join was verified live end to end: **IČO 27462889 → ARES 200 → company name, 14 NACE
codes, founding date, region.** No auth, daily-ish refresh, 38,735 live vacancies, and the
licence **explicitly disclaims both copyright and the sui-generis database right**.

> **Consequence: hiring is the first feed that joins NATIVELY to the `entity_ico` graph
> designed in §2.3** — no fuzzy name matching, no eTLD+1 heuristics. A hiring record and a
> tender award resolve to the same legal entity by primary key. That is a structurally
> different class of feed from everything currently in the corpus, and it is why §13 is
> promoted from "reserved seam" to a scoped build.

The mod-11 checksum validation in §2.3 stays **mandatory** — it was introduced because
Hlídač URLs embed 8-digit contract ids that would otherwise flood the column with false
IČOs, and a second high-volume IČO producer raises the cost of getting that wrong.

### 13.1 Ruling: `hiring` is a fifth type, not a fold-in

It is neither a complaint (`demand`), nor public procurement (`tenders`), nor a funding
round (`funded`). And folding it into `demand` would let one high-volume feed dominate that
ledger — which `data/CONVENTIONS.md:21-23` already forbids **as a lesson learned**
("no single feed may dominate the ledger"; the source-imbalance failure is recorded at
`docs/sources-catalog.md:199-201`, where one loud feed made every "cross-source" cluster
single-source). A separate type is the structural version of that rule.

### 13.2 The checklist — how to add ANY evidence type

The seam is **already half-built**: `web/lib/data.ts:175` skips a missing type directory
with the comment *"a pending feed is a registered fact — its page renders empty"*. **A type
can therefore be registered before a single record exists.**

1. **`data/CONVENTIONS.md`** — add the type to the evidence-type list (`:13-25`), name its
   feeds, and add id-prefix rules (`:29-34`).
2. **`data/feeds.json`** — add the feed(s) with `evidence_type: <new>`, an `access` verdict
   (§4.1) and a `contract` (§7.2).
3. **`data/signals/<type>/`** — nothing to do; created on first append.
4. **`web/lib/data.ts:16`** — add to `EVIDENCE_TYPES`. **This one line lights up the route**
   via `generateStaticParams` (`web/app/sources/[type]/page.tsx:10-12`).
5. **`web/app/signals/[type]/page.tsx:16-33`** (post-rename path; `web/app/sources/[type]/`
   today) — add `TITLES` and `DESCRIPTIONS` entries. **The build enforces this for you:**
   both are `Record<EvidenceType, string>`, so adding to `EVIDENCE_TYPES` without adding the
   explainer prose is a TypeScript error. The gate makes the checklist self-policing.
6. **`web/lib/data.ts:25`** — add the new `source` key(s) to `SignalSchema`'s `source` enum,
   or every record fails validation.
7. **`SPEC.md`** §3 layout + §5 route table + §5 nav line; **`skills/design-language/SKILL.md:85-86`**.
8. **`data/feed_health.json`** — the feed appears with `state: PENDING` on its first health
   export (§7.5), so a registered-but-silent type is visible from day one rather than
   forgotten.

Eight steps, **three of them enforced by the build rather than by memory**: step 5 (the
`Record<EvidenceType, string>` types make a missing explainer a TypeScript error), step 6
(`z.enum` fails loudly on an unknown `source`), and step 2 (AC-F1 totality fails the build
if a corpus `source` has no registry row). **That is the actual deliverable of M1** — the
checklist is reusable whether the fifth type is hiring or something nobody has proposed yet.

### 13.3 The value thesis — CORRECTED by the probe

Revision 2 (following the mandate as written) said hiring "validates compliance waves: who
is actually STAFFING NIS2". **The data says that is mostly false, and the correction belongs
to the probe, not to a change of opinion.** Across the full live stock of 38,735 vacancies:

| Theme | Live postings | Verdict |
|---|---|---|
| accessibility / WCAG | **0** | no staffing signal exists at all |
| cyber / NIS2 | 28 | too thin to discover anything |
| GDPR | 25 | too thin |
| ESG | 51 | too thin |
| **back-office / administration** | **960 postings across 717 distinct employers** | **the actual product** |
| AI / automation | 169 | secondary, and a useful trend line |

So the real products are:

1. **Automation-target evidence.** **717 named employers currently paying humans to do
   back-office work** is the strongest "who would buy this" list this register could hold —
   and every one of them arrives with an IČO that resolves through ARES to size, sector and
   region (§13.0).
2. **Sector-expansion mapping.** Which sectors are adding which roles, over time, keyed to
   entities we already track.

**Compliance detection is CORROBORATING evidence, never a discovery engine.** 28 cyber
postings cannot find a problem; they can confirm one already evidenced by a tender and a
regulation.

**The first MATCH pass has a ready-made target set.** Verified in the register: four problem
files name back-office work explicitly — `p-0004` (family-caregiver benefit navigation),
`p-0006` (investment-intermediary compliance), `p-0007` (construction subcontractor
management), `p-0010` (trucking back-office) — and `p-0002`, `p-0005`, `p-0011`, `p-0023`
are back-office-shaped by title. Hiring's first run has somewhere obvious to land.

### 13.4 Aggregation is not a preference — it is the only shape that survives materiality

Revision 2 argued for aggregates on volume and link-rot grounds. The probe supplies the
harder reason: **individual postings are mechanically filtered out of existence.**

| | Money | `scores.money` | Materiality filter |
|---|---|---|---|
| **median cyber posting** | €15,918/yr | **1** (`<200k`) | `money<=1 AND scale<=1 AND urgency==0` → **DROPPED** |
| cyber postings **aggregated** | €507,469 | **2** (`200k–2M`) | survives |
| back-office **aggregated** | **€19.1M** | **3** (`>2M`) | survives comfortably |

A per-posting feed would fetch 2,000 items a week and write approximately none of them.
Aggregated: **~2,000 raw postings/week → 8–15 records/month.**

> **Ordering law, interlocking with §1.1: AGGREGATION HAPPENS BEFORE MATERIALITY.**
> Aggregation is a pure-script step (group by theme/IČO, sum the salary floors), so it sits
> in the mechanical phase ahead of the filter — exactly where the materiality reorder put
> the cheap work. Get this order wrong and the feed produces nothing at all, while looking
> like it ran correctly.

Individual postings are recorded **only when the posting itself is the evidence** — a named
employer staffing a specific compliance wave — which is the corroborating case in §13.3.

**Dedup keys** (deliberately NOT a URL or content hash, because **reposting is the whole
problem** — the same vacancy reappears for months):

```
mpsv-<YYYY-MM>-<theme>              e.g. mpsv-2026-08-back-office
mpsv-<YYYY-MM>-<ico>-<theme>        e.g. mpsv-2026-08-27462889-back-office
```

Verified: `mpsv-` has **zero collisions** in `data/signals/seen.txt`, and both shapes match
the id regex at `web/lib/data.ts:24` (`/^[a-z]{2,10}-[\w.-]+$/`).

### 13.5 Scope — deliberately bounded, and it cannot block CP2

| Phase 2 (cheap half) | Separate parallel worker, may slip to Phase 3 |
|---|---|
| `hiring` type registration (the §13.2 checklist) | **the MPSV fetcher itself** |
| `data/feeds.json` rows: `mpsv` + `ares`, with contracts (§7.2) and ToS verdicts (§13.8) | the aggregation pass |
| the GDPR allowlist rule + its checker (§13.6) | the first real records |
| the expected-absence concept (§7.2, a general M2 addition) | |

**Why the fetcher may slip without blocking CP2:** `web/lib/data.ts:175` skips a missing
type directory with the comment *"a pending feed is a registered fact — its page renders
empty"*. A registered-but-empty `hiring` ledger renders correctly, and `/sources` shows the
feed as `PENDING` (§7.5). **A late fetcher costs nothing; a rushed one writing personal data
into an append-only public log costs everything.**

**Two schema edits must land in the SAME checkpoint as the first hiring record** — not
before, not after:

- `web/lib/data.ts:16` — `EVIDENCE_TYPES` gains `"hiring"`
- `web/lib/data.ts:25` — the `source` enum gains `"mpsv"`

> **A useful asymmetry, worth naming:** the `source` field is `z.enum`, which **fails LOUDLY
> on an unknown value** — unlike the `z.object` silent strip that §3 is built around. This
> one edit self-enforces: forget it, and every hiring record fails validation and the build
> goes red, exactly as the law intends. Contrast `quote`/`extraction`, where forgetting the
> schema edit produces silence. Same file, two opposite failure modes.

**ARES is an ENRICHMENT source, not a signal feed.** It gets a registry entry carrying
`role: "enrichment"` so its health is tracked like anything else, but **it never produces
signals and must not inflate the feed count** — AC-F1's totality check considers only
`role: "feed"` entries, and `/sources` lists enrichment sources in their own short section.

### 13.6 GDPR — a hard, checked obligation

The dataset's DCAT record declares **`obsahuje-osobní-údaje`**: contact names, emails,
phones. MPSV's site-wide terms page says otherwise, but it is stale (2022) and contradicted
by the per-dataset metadata — **trust the metadata.** Our ledgers are **append-only and
public on GitHub**, so a mistake here is permanent *and* public; there is no quiet cleanup.

Contact fields MUST be stripped at ingest, **before anything reaches the ledger**. Two hard
requirements:

1. **ALLOWLIST, never denylist.** Only named-safe fields enter the record — IČO, CZ-ISCO,
   salary floor, NUTS-3, employer name, posting date, change type. **A denylist fails OPEN
   the day MPSV adds a field; an allowlist fails CLOSED.** This is receipt discipline applied
   to privacy: enumerate what is permitted, never what is forbidden.
2. **AC-GDPR1 — a named acceptance item with its own dedicated checker**, not a sentence
   inside a paragraph: grep the produced JSONL for email and phone patterns and require
   **zero matches**. It runs in the ingest path before append and again in the build gate.

### 13.7 Two MPSV contract checks that generalize (see §7.2)

Both came out of the probe and both are now general contract features, not MPSV quirks:

- **Expected absence.** 180 of 658 calendar days are simply missing from the daily files, so
  a naive "fetch yesterday" fetcher 404s roughly weekly. `mpsv` sets `allow_missing: true`
  (§7.2) and a skipped day logs as `skipped` — it does **not** increment
  `consecutive_failures` and does **not** move the feed to BROKEN.
- **The changelog trap.** The increment file is a **changelog, not a list of new items**: on
  2026-08-19 it carried 287 `novy`, 817 `zmeneny`, 986 `zruseny`. A parser ignoring
  `typZmenyOpenData` records **2,090 "new" postings when 287 are new — a ~7× flood into an
  append-only, permanent log.** So `typZmenyOpenData` is in the contract's `required_fields`,
  and **"parser branches on change type" is an explicit contract check.**

### 13.8 ToS verdicts — recorded with their quoted clauses

Every feed carries `access: {verdict, basis, checked}` (§4.1). **A clean negative is worth
more than a vague maybe**, and this is exactly what the field is for.

| Source | Verdict | Quoted basis |
|---|---|---|
| **MPSV/ÚP `volna-mista`** | **`allowed`** | licence explicitly disclaims copyright **and** the sui-generis database right |
| **ARES** | **`allowed`** (enrichment only) | public register API |
| StartupJobs | **`forbidden`** | VOP: *"je výslovně zakázáno databázi vytěžovat"* |
| jobs.cz · prace.cz | **`forbidden`** | Alma Career terms §4.11 |
| LinkedIn | **`forbidden`** | `robots.txt`: `Disallow: /` |
| EURES | **`allowed`, BUILD LATER** | the CZ rows **are** the MPSV data, and IČO/salary would need ~39k per-vacancy requests — strictly worse than the source |
| ATS boards (Greenhouse, Lever, …) | **`allowed`, BUILD LATER** | needs a hand-built company→token map; no discovery path |

**We never build against a source whose terms forbid it.** Recording the three `forbidden`
verdicts with their clauses is what stops this being re-litigated every quarter.

### 13.9 The SPEC §7 tension, addressed rather than ignored

`SPEC.md:204` bans *"VC/capital signals as a discovery source (hierarchy law: confirmation
stamp only)"*. Hiring sits close enough to that line to deserve an explicit answer.

**It does not breach the hierarchy law**, for a specific reason: the ban exists because VC
money signals *investor consensus*, and using it for discovery imports someone else's thesis
about a market instead of observing the market. A job posting is the opposite — **a named
local employer committing their own budget to a dated, specific need**, which is the same
evidential class as a tender, not the same class as a funding round. "Three CZ firms are
hiring NIS2 compliance officers" is local demand observed directly.

Where the tension is real: a posting at a VC-funded startup *is* downstream of a round, and
counting both would double-count the same capital event. **Rule: hiring records may back
`demand` and `money`; they may never lift `proof`.** That slots into the existing source
type → dimension table at `data/CONVENTIONS.md:105-111` as one new row, and keeps the
hierarchy law intact by construction rather than by good intentions.
