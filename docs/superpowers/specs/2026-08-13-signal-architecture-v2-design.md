# Signal architecture v2 — design spec

Date: 2026-08-13 · Status: draft for review

## 1. Problem

The v1 pipeline smears region judgment into the normalize step: of ~3,000
TED notices fetched per run, only ~11 survive because the keep-criterion is
"plausible CZ problem angle". This throws away the objective record, makes
the register CZ-only by construction, and anchors discovery to a keyword map
derived from problems that already exist. Separately, the site renders a
rundown page for only one problem (p-0001) out of 26, and problem frontmatter
is mid-migration (SCORING.md defines v2 `sources[]` / proof-money-urgency-
demand-gap, while problem files still use v1 `receipts[]` / `signals{}`).

## 2. Goals

- Split the pipeline into an **objective evidence layer** (region-blind,
  near-complete, scored at normalize time) and **per-region match agents**
  (all judgment lives here).
- Reorganize signals by **evidence type**, not fetch source.
- Make region a path-level concept so adding PL/DE later is "run another
  agent", zero migration.
- Render a site rundown page for **every** problem.
- Finish the v1→v2 problem-frontmatter migration.

Non-goals: adding a second region now; the `bootstrapped` evidence type
(reserved, no reliable source yet); changing SCORING.md semantics; any
visual/CSS change to the site.

## 3. Evidence layer

### 3.1 Layout

```
data/signals/
  funded/2026-08-13.jsonl       # was normalized/{yc,round,de,dk,pl}
  regulation/2026-08-13.jsonl   # was normalized/reg
  tenders/2026-08-13.jsonl      # was normalized/ted
```

One JSONL file per evidence type per run date, append-only, committed to
git. `bootstrapped/` is documented in CONVENTIONS.md as a reserved fourth
type and created only when a fetchable source exists.

### 3.2 Record schema (one JSON object per line)

| field       | type         | notes                                          |
|-------------|--------------|------------------------------------------------|
| id          | string       | canonical: `<source>-<nativeid>` (unchanged v1 rule) |
| source      | string       | fetch provenance: ted, yc, round, reg-scan, arb-scan, feed |
| url         | string       | primary source URL                             |
| date        | ISO date     | native date of the signal                      |
| title       | string       | native title, translated to EN if needed       |
| sector      | enum         | the fixed category list in CONVENTIONS.md      |
| geo_origin  | string       | where the signal comes FROM (ISO2 or EU)       |
| money_eur   | number\|null | best-effort EUR value                          |
| money_note  | string       | how money_eur was derived                      |
| summary     | string       | max 2 sentences, EN                            |
| scores      | object       | see 3.3                                        |

### 3.3 Objective scores (set at normalize time, region-blind)

Each 0–3, integers, mechanical definitions — no opportunity judgment:

- **scale** — how many entities the underlying need touches:
  0 one org · 1 niche segment · 2 a sector · 3 economy-wide/cross-sector
- **money** — attached EUR: 0 none/unknown · 1 <200k · 2 200k–2M · 3 >2M
- **urgency** — 0 none · 1 dated event >18mo out · 2 <18mo ·
  3 <6mo or already in force with active enforcement
- **recurrence** — 0 one-off event · 1 probably repeatable ·
  2 recurring need (annual/continuous) · 3 structural (mandated forever)

### 3.4 Materiality filter (the ONLY normalize-time filter)

Drop a deduped item only if `money <= 1 AND scale <= 1 AND urgency == 0`.
Everything else is kept. Expected volume: hundreds to low-thousands per run.
Region agents do all further selection.

### 3.5 Dedup

`data/signals/seen.txt` — one canonical id per line, sorted, updated each
run. Normalize checks it before writing; grep across `*.jsonl` is the
fallback audit.

## 4. Region layer

### 4.1 Layout

```
data/problems/cz/
  INDEX.md
  p-0001-energy-community-billing-settlement.md
  ...
```

Existing 26 problems move here keeping their IDs. Future regions get their
own directory and their own p-NNNN namespace (a problem is uniquely
identified by `<region>/<id>`).

### 4.2 Frontmatter (completes the v1→v2 migration)

- add `region: cz`
- rename `receipts:` → `sources:` (matches SCORING.md v2 wording)
- rescore `signals{arbitrage,money,deadline,demand,gap,freshness}` →
  `scores{proof,money,urgency,demand,gap}` per the mapping already defined
  in SCORING.md (deadline+freshness fold into urgency; arbitrage→proof).
  Point values carry over 1:1 per that mapping; no re-judgment of evidence.
- source entries gain optional `signal: <id>` linking back to the evidence
  layer.

### 4.3 MATCH step (new, replaces normalize-time judgment)

Per region, per run: read new signal records (all types), and for each
candidate cluster ask the region questions — local player exists? local
regulation analog? local buyer? — then append to an existing problem's
`sources[]` or draft a new problem file. Rules preserved from v1: never
create a problem from a single tier-3-grade signal; every score point needs
a source entry.

## 5. Pipeline (TASK.md v2 step order)

1. FETCH — unchanged (TED, feeds, yc-oss, research scans; Hlídač pending
   token; re-probe Vestbee).
2. NORMALIZE — objective: dedup → materiality filter → score → append JSONL.
   No region judgment.
3. MATCH — one pass per region (CZ only for now), as §4.3.
4. SCORE — per SCORING.md, unchanged semantics.
5. INDEX + SITE — regenerate `data/problems/cz/INDEX.md`; run site build
   (§6); validate YAML on touched files.
6. NEWSLETTER — unchanged.
7. COMMIT — unchanged.

## 6. Site build

`scripts/build_site.py` — no dependencies beyond stdlib + PyYAML if
available (else a minimal frontmatter parser). Reads `data/problems/*/`,
renders:

- one rundown page per problem: `site/problem-<region>-<id>.html`,
  using the existing `problem-p-0001.html` as the template to extract
  (structure, classes, scorecard band markup);
- the register index with links to every rundown.

Constraints: follows the design-language skill; reuses `shared.css` /
existing markup patterns; `style.css` and the visual system are untouched;
no new visual elements. Existing `problem-p-0001.html` is regenerated by
the script (URL may change to `problem-cz-p-0001.html` with the old path
left as a redirect stub).

## 7. Migration plan

1. Convert 61 `data/normalized/**/*.md` files → backfill JSONL records under
   their evidence type (funded ← yc/round/de/dk/pl; regulation ← reg;
   tenders ← ted), deriving scores from existing frontmatter
   (tier/money_eur/summary). Delete `data/normalized/` afterward.
2. Move problems to `data/problems/cz/`, apply frontmatter migration (§4.2).
3. Rewrite CONVENTIONS.md (evidence types, record schema, score rubric,
   reserved `bootstrapped`), TASK.md (§5), and the sources page copy.
4. Seed `seen.txt` from backfill.
5. Update auto-memory note about repo layout after landing.

## 8. Verification

- Re-run normalize against the existing `data/sources/2026-08-13/` snapshot:
  TED must yield hundreds of kept records (vs 11 in v1); spot-check 10
  records for score correctness against the rubric.
- `jq` parse check over all JSONL; uniqueness check of ids vs `seen.txt`.
- Site build renders 26 rundown pages; frontmatter of every problem parses;
  every score point in a spot-checked problem maps to a `sources[]` entry.
- Git diff of a second normalize run shows append-only behavior (no
  rewrites of prior runs' files).

## 9. Open questions / later

- `bootstrapped` sources (indie-hacker lists, revenue-milestone scrapes) —
  revisit when a fetchable source is identified.
- Second region (PL likely) — after one clean CZ cycle on v2.
- Hlídač státu token still missing (README checklist #3).
