# localproblems — v2 spec

*2026-08-13 · The authoritative system spec. Consolidates the founder vision, the
approved signal-architecture v2, and the site direction into one document; supersedes
everything in `docs/archive/`. Rule of this file: if it is not written here, it is not
in v2.*

---

## 1. What this is

The age of AI makes solvers abundant and well-stated problems scarce. **localproblems.org
is an open, evidence-backed register of problems worth solving, per region.** It
intersects four streams:

1. **Arbitrage** — proven abroad, absent locally (companies founded/funded elsewhere with no local player)
2. **Top-down** — where governments put money: tenders, grants, regulation with compliance deadlines
3. **Bottom-up** — what people demonstrably complain about and want
4. **Capital** — where investors put money (confirmation only, never discovery)

Every claim carries a source. If someone local already solves a problem, it gets
de-ranked. Output: a ranked public register + a weekly newsletter draft.

**v2 region: Czech Republic** — but region is a parameter, not an assumption: evidence
is collected region-blind, and all region judgment lives in a per-region match agent.
Adding Brno-only, PL, CEE, or EU later means running another match agent, zero migration.

## 2. The loop

One weekly scheduled Claude agent run (Mon 06:00). The whole system must be launchable
by Claude end to end from TASK.md alone:

```
fetch → normalize (objective, region-blind) → match (per region) → score → build site → newsletter draft → commit
```

No servers, no database server, no queue, no client-side app. A git repo, a few fetch
scripts, one statically-generated site, one agent.

## 3. Evidence layer (region-blind)

### Layout

```
data/signals/
  funded/<run-date>.jsonl       # companies founded/funded: yc, rounds, foreign-market scans
  regulation/<run-date>.jsonl   # regulatory triggers with dates
  tenders/<run-date>.jsonl      # tenders, grants, public contracts (ted, hlidac)
  demand/<run-date>.jsonl       # bottom-up documented complaints & unmet needs (demand-scan)
  seen.txt                      # one canonical id per line, sorted — the dedup index
```

One JSONL file per **evidence type** per run date, append-only, committed to git.
`demand` records bottom-up documented complaints and unmet needs — NKÚ audit findings,
ombudsman reports, civic complaint data, chamber/NGO surveys, consultations — fed by
research harvests (source `demand-scan`). `bootstrapped/` stays reserved
(indie-hacker/revenue signals) — created only when a fetchable source exists.

### Record schema (one JSON object per line)

```
id          canonical <prefix>-<nativeid>; v1 ids grandfathered unchanged
source      fetch provenance: ted | hlidac | yc | round | reg-scan | arb-scan | demand-scan | feed
url, date   primary source URL, native ISO date
title       native title, EN
sector      the fixed category list in CONVENTIONS.md
geo_origin  where the signal comes FROM (ISO2 or EU)
money_eur   number|null + money_note (how derived)
summary     ≤2 sentences, EN
scores      {scale 0-3, money 0-3, urgency 0-3, recurrence 0-3}   ← objective, see below
notes       optional free text: absence checks, transfer logic, quotes (kept from v1 bodies)
```

### Objective scores + the only filter

Scores are **mechanical, no opportunity judgment**: scale (one org → economy-wide),
money (none → >2M EUR), urgency (none → <6mo or in force with enforcement), recurrence
(one-off → structurally mandated). The only normalize-time filter is **materiality**:
drop only if `money ≤ 1 AND scale ≤ 1 AND urgency = 0`. Everything else is kept —
hundreds to low-thousands of records per run, not eleven. Region agents do all further
selection. (This kills the v1 mistake: "plausible CZ angle" at normalize time threw
away the objective record and made the register CZ-only by construction.)

## 4. Region layer (all judgment lives here)

### Problems

```
data/problems/cz/
  p-0001-energy-community-billing-settlement.md
  ...
```

One markdown file per problem — prose humans read, GitHub renders, corrections diff
legibly. Future regions get their own directory and p-NNNN namespace (a problem is
`<region>/<id>`). Frontmatter:

```
id, region, title, category, geo, score (0-12),
scores {proof 0-3, money 0-2, urgency 0-3, demand 0-2, gap 0-2},
status (candidate|active|watching|stale|claimed|solved|rejected),
sources[] {type, url, note, date, signal?: <evidence-layer id>, dims?},
created, updated
```

Body: 3–6 paragraphs — problem · why-now · who-pays · existing non-solutions ·
foreign comparables. Appended CORRECTION blocks are rendered prominently.

### MATCH (the region agent)

Per region, per run: read new evidence records (all types), cluster, and for each
candidate ask the region questions — *local player exists? local regulation analog?
local buyer? does this matter here?* Then:

- matches an existing problem → append to `sources[]`, update body if the picture
  changed, bump `updated`;
- distinct problem → new file, next id. Never from a single tier-3-grade signal.
- **De-rank rule (founder law):** re-check the gap on every touched problem; if a local
  player now exists or has entered the market → `gap: 0`, add a gap-check source naming
  the incumbent, status → `watching`.

### SCORE

Per `SCORING.md` exactly — binding and unchanged: `score = proof + money + urgency +
demand + gap`, every point justified by a `sources[]` entry, verdict words
(PRIME/STRONG/FAIR/FAINT), tie-break by (urgency.deadline, money). Decay: newest source
>120 days → freshness lost, `active→watching`; >240 days → `stale`.

## 5. The site (`web/` — Next.js, pure SSG)

**Minimal: list the problems, list the evidence.** A Next.js app (latest stable, App
Router, TypeScript) in `web/`, deployed on Vercel — chosen for owner familiarity.
Discipline keeps it exactly as simple as a static generator:

- **Pure SSG.** Server Components only — no client components, no hydration, no ISR,
  no runtime data reads. Every route statically generated (`generateStaticParams`,
  `dynamicParams = false`); only sanctioned inline JS (relative dates). The site is a
  pure function of `data/`: content arrives as git commits, commits trigger deploys —
  the register can never silently go stale (the v1 failure mode).
- **`web/lib/data.ts`** reads `../data` at build time, zod-validated: schemas, category
  list, `score == sum(scores)`, `sources[] ≥ 1`, ISO dates. **Validation failure =
  build failure = deploy blocked.** The rundown ref-resolution rules (source type →
  scorecard dimension, `dims:` overrides) carry over from docs/archive/05 §4.

| Route | Content |
|---|---|
| `/` | register table ranked by score: id · title · category · locality · score meter · updated. `rejected` excluded, `stale` greyed at the bottom. |
| `/problem/[region]/[id]` | one rundown page for **every** problem: docket · scorecard band · prose statement · sources ledger (S1…Sn, each linking its evidence record) · provenance footer. Score rundown dialogs embed the referenced source records (external links only, close cross). |
| `/sources/[type]` | the source ledgers (funded · regulation · tenders · demand): recent records per type, anchor per id — the provenance target (replace the v1 per-fetch-source pages) |
| 404 | house string: "Record not found. Either it never existed, or it was solved so thoroughly it disappeared." |

The problem register and the source ledgers are two clearly separated surfaces: site
nav reads `Problems` then `Sources: Funded · Regulation · Tenders · Demand`.

Nothing else: no redirects (v1 was never publicly deployed), no test suite (the
build's validation IS the gate), no OG images, no middleware, no API routes.

- **Design:** the `design-language` skill is binding. `web/shared.css` is a verbatim
  copy of the skill stylesheet — the build asserts checksum equality and fails on
  drift; no new classes, colors, or components; fonts load exactly as the skill
  specifies.
- **Deploy:** Vercel project rooted at `web/`; push to `main` = production; wire
  `localproblems.org` when registered. **The local build is the gate:** the weekly
  agent runs `npm --prefix web run build` before committing — a red build means bad
  data; fix the data, never the app. Vercel runs the same build, so a green local
  build is a green deploy.

## 6. Newsletter

Draft `newsletter/<date>.md` every run: top 3 by score (2 short paragraphs + source
links each), 3–5 one-line movers, 1 regulatory deadline to watch. Czech, direct, no
filler. **Draft only — a human reviews and sends. Nothing is ever auto-sent.**

## 7. Non-goals (cut, explicitly)

- **Claiming** — cut entirely (owner, 2026-08-13). No claim UI. Revisit only if the
  register earns an audience. Lifecycle statuses live in data frontmatter only.
- **Client-side JavaScript** beyond the sanctioned relative-dates snippet — no client
  components, no hydration-dependent UI.
- **SQLite / Postgres / servers / embeddings** — tripwires only (§10).
- Map page (GeoJSON asset stays; page cut), per-category pages, search, alerts, API,
  B2B radar, automated sending, dark mode, i18n of chrome, OG images.
- VC/capital signals as a discovery source (hierarchy law: confirmation stamp only).
- `bootstrapped` evidence type — reserved until a fetchable source exists.
- A second region — after one clean CZ cycle on v2 (PL likely first).

## 8. Migration & repo cleanup (one afternoon, in order)

1. **Backfill evidence layer:** convert all `data/normalized/**/*.md` (re-glob at
   execution — concurrent editors) into their evidence type (funded ← yc/round/de/dk/pl ·
   regulation ← reg · tenders ← ted/hlidac), deriving objective scores from existing
   frontmatter. Seed `seen.txt`. Delete `data/normalized/`.
2. **Move problems** to `data/problems/cz/`; frontmatter migration: add `region`,
   `receipts→sources`, `signals{}→scores{}` per the SCORING.md mapping (1:1 point
   carry-over, no re-judgment). Delete `INDEX.md` (derived at build).
3. **Scaffold `web/`** — data layer + the routes in §5, structural fidelity checked
   against the current hand-built `site/` pages; then delete `site/` and
   `scripts/build_sources.py`. Create the Vercel project rooted at `web/`.
4. **Rewrite `TASK.md`** to the v2 step order (§2); update the scheduled task.
5. **Rewrite `CONVENTIONS.md`** (evidence types, record schema, objective rubric,
   reserved type) and `README.md` (short: vision → loop → layout → pointer here).
6. **Lean the repo:** docs/01–05 + the superpowers spec → `docs/archive/`; delete
   `site-v1/`; no duplicate documents — each fact lives in exactly one file (§12).
7. Update session memory after landing.

Ops notes that survive: TED API works locally only (cloud egress 403s); Hlídač token in
`.env.enc` via sops/direnv; macOS bash 3.2 (no associative arrays).

## 9. Definition of done (v2 acceptance)

1. **Launchable by Claude, end to end.** A fresh Claude session given only TASK.md runs
   fetch → normalize → match → score → build → newsletter → commit with no questions and
   no interactive input; failures land in the run manifest, never fatal.
2. **Normalize is objective:** re-run against the existing `data/sources/2026-08-13/`
   snapshot yields hundreds of kept TED records (vs 11 in v1); `jq` parses every JSONL;
   ids unique vs `seen.txt`; a second run is append-only (git diff proves it).
3. **The landing page updates itself:** every push to `main` redeploys the register;
   a rundown page exists for every problem (26 at time of writing); every score point
   in a spot-checked problem maps to a `sources[]` entry.
4. **A newsletter draft exists after every run**, ready for human send.
5. **The repo is lean:** only SPEC / SCORING / TASK / CONVENTIONS / FOUNDER VISION +
   `data/` `scripts/` `web/` `newsletter/` `skills/` + `docs/archive/`. No normalized/
   tree, no site-v1, no hand-built `site/`, no INDEX.md, no duplicated information
   between documents.
6. **The build is the gate:** `npm --prefix web run build` exits 0 on a clean checkout
   and fails loudly on any invalid record — zod validates every problem and signal.

## 10. Tripwires (when to un-simplify)

| Trigger | Graduation |
|---|---|
| >~400 problems per region, or match dedup gets sloppy | SQLite + embeddings for shortlisting |
| >~10 sources, or silent fetch failures | move fetch to GitHub Actions cron |
| >100 newsletter subs or alert demand | paid Buttondown + small worker |
| a page genuinely needs client-side JS | one client component at a time, explicit sign-off |

## 11. Later / open

- `bootstrapped` sources (indie-hacker lists, revenue milestones) — when fetchable.
- Second region (PL) — after one clean CZ cycle.
- **Claiming** — cut entirely (owner, 2026-08-13). No claim UI. Revisit only if the
  register earns an audience.
- Monetization ladder (newsletter → Pro → B2B radar) and the month-9 fork (CEE English
  expansion vs B2B data product) — recorded in `docs/archive/02`, revisit after launch.

## 12. Document map (each fact lives in exactly one place)

| File | Role |
|---|---|
| `FOUNDER VISION.md` | the why — canonical |
| `SPEC.md` | **the how — authoritative (this file)** |
| `SCORING.md` | the problem-scoring rubric — binding |
| `data/CONVENTIONS.md` | vocab: categories, id rules, schemas — binding |
| `TASK.md` | the weekly agent prompt (operational form of §2) |
| `skills/design-language/` | the design system — binding |
| `docs/archive/` | superseded research & drafts — read-only history |
