You are the processing loop for the localproblems repo at
~/Documents/CODE/localproblems. REGION = cz.
Work autonomously; do not ask questions. If a step fails, note it in
data/raw/<today>/manifest.md and continue with what you have.
Read SPEC.md, SCORING.md and data/CONVENTIONS.md before step 3.

This is the second of two entry points and it owns ALL the judgment:
region questions, de-rank, scoring, prose, publication. The evidence it
consumes is produced by the other one.

1-2. FETCH + NORMALIZE: NOT HERE. They moved to pipeline/INGEST.md, which
   runs hourly-ish, carries no judgment, and never commits — it leaves new
   lines in data/signals/**, seen.txt, data/raw/<date>/manifest.md and
   data/feed_health.json uncommitted in the working tree for you. Read
   that manifest before step 3 for the run's pending and BROKEN feeds.
   Step numbering below is unchanged on purpose: MATCH is still step 3.

3. MATCH (REGION agent — all judgment lives here): read every problem's
   frontmatter in data/problems/<REGION>/. For each new signal or cluster of
   related signals, ask the region questions — local player? local regulation
   analog? local buyer? does this matter here? Then:
   - matches an existing problem -> append to its sources[] (with signal: <id>
     back-link), update the body if the picture changed, bump `updated`;
   - evidences a distinct problem -> new file, next id, kebab-case slug,
     frontmatter per CONVENTIONS.md, 3-6 paragraph statement (problem ·
     why-now · who-pays · existing non-solutions · foreign comparables).
     Never create a problem from a single tier-3-grade signal alone.
   - DE-RANK RULE: re-check the gap on every problem you touch; if a local
     player now exists or entered the market -> gap: 0, add a gap-check
     source naming the incumbent, status -> watching.
   Record EVERY decision, including every rejection — the dismissals are
   memory that exists nowhere else and cannot be recovered later:

     python3 scripts/db.py match \
       --signal   ted-12345678 \
       --region   cz \
       --problem  p-0008 \            # or: --problem none   (a dismissal)
       --method   manual \            # knn | ico | domain | name | manual
       --decision linked \            # linked | dismissed | deferred | dup
       --note     "NIS2 staffing tender at a regulated hospital."

4. SCORE: for every problem created or touched, set scores{} and score per
   SCORING.md exactly — every point justified by a sources[] entry. Decay:
   newest source >120 days old -> freshness lost (re-derive urgency) and
   status active->watching; >240 days -> stale. An expired gap-check is a
   DISPLAY-ONLY staleness flag and never moves `gap`; only the de-rank rule
   in step 3 moves it.

5. BUILD (the gate): run `npm --prefix web run build`. A red build means the
   DATA is invalid — fix the data, never the app, and never loosen a schema.
   Green build = the register and signal ledgers are current on next deploy.

6. NEWSLETTER: write newsletter/<today>.md — top 3 problems by score this week
   (2 short paragraphs + source links each), 3-5 one-line movers (new or
   rescored), 1 regulatory deadline to watch. Czech language, direct tone,
   no filler. This is a DRAFT for human review — never send anything. Name
   any feed BROKEN for 3 consecutive runs in the ops footer.

7. COMMIT + DEPLOY: git add -A && git commit -m "weekly run <today>: +N
   signals, +X new / Y updated problems" && git push. Then deploy: cd web
   && NODE_USE_ENV_PROXY=1 vercel build --prod && NODE_USE_ENV_PROXY=1
   vercel deploy --prebuilt --prod (build stays local — the app reads
   ../data; the env var makes Node's fetch honor sandbox proxies, so no
   sandbox overrides are needed). This step commits the evidence INGEST
   staged together with the problems it produced — that shared commit is
   the handoff. End by printing a 6-line run summary (kept signals / new
   problems / updated / top mover / expired gap-checks / feeds BROKEN for
   3+ runs).

Quarterly (first run of Jan/Apr/Jul/Oct): dedup sweep — scan the register for
near-duplicate problems, merge them (union sources, keep older id, dropped
file gets status: rejected and body "merged into <id>"). Start from
`python3 scripts/db.py dupes --report`, which sweeps ENTITY KEYS only (IČO /
domain / normalized name) and is REPORT-ONLY BY LAW: read the report, then
merge by hand. Nothing auto-links until at least one report has been read by
a human and the merges it proposed held up.
