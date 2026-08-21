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
   INGEST's mechanical half is scripts/ingest.sh, and its exit code is
   worth reading before you trust the manifest: 0 clean · 1 some feeds
   failed but the run IS audited · 2 the run is UNAUDITED, meaning
   normalize, fetchlog, health or rebuild did not complete and this
   manifest may be describing a run that never finished. On a 2, re-run
   ingest before matching rather than matching over a hole.

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

   RECORDS ARE BORN SHORT. A reader arrives asking two questions — what is
   the problem, and could I build it — and must be able to answer both
   without reading an audit trail. Binding shape, full rules in
   data/CONVENTIONS.md ("Body shape and length"):
     · SECTION ORDER, exactly: lead paragraph(s) · `Why now:` · `Who pays:` ·
       `Existing non-solutions:` · `Solved elsewhere:` · `## First moves`
       (score >= 7 only) · `## Revisions`. The lead-ins are LITERAL — the
       site keys its rendered sections off them (web/lib/sections.ts), and
       an orphaned lead-in silently dumps a paragraph into the wrong
       section. Never invent a seventh section.
     · LENGTH TARGET: <= 60 words per argument paragraph, <= 300 words of
       argument prose, <= 80 words per revision entry. First moves is 4-6
       numbered steps. If a record exceeds this, cut connective tissue and
       repetition — NEVER a sentence carrying an [Sn] marker.
     · THE ARGUMENT STATES THE PICTURE AS IT IS NOW. "The 2026-08-13 check
       found X, the 2026-08-20 re-check overturned it" is revision-list
       prose, not argument prose. In the body, say what is true and cite it.
     · ONE REVISION ENTRY PER DATE. A new correction MERGES into that date's
       existing entry — it never appends a new block. Two entries that say
       the same thing are folded into one that says it once, and the entry
       says that it is a merge. Format, oldest first:
         2026-08-20 · evidence audit — <what changed and why, with [Sn]s>
       The tag is short, has no em dash, and names the kind of change
       (evidence audit · gap re-check · de-rank · title sweep · fact check ·
       money receipted · regulation added). No `**CORRECTION (…):**` blocks,
       no `---` separators, no backticks and no single-asterisk italics —
       the body renderer supports only **strong**, links and lists, so any
       other markdown ships to the reader as literal punctuation.
     · A REVISION IS NEVER DELETED OR SILENTLY SHRUNK. Merging and
       compressing are allowed; dropping a fact one of them asserts is not.
       A silent deletion is the same sin as the invention it corrected.
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
   Then `python3 scripts/db.py rebuild`. You just edited problem markdown,
   and `problems` is a PROJECTION of those files exactly as `signals` is a
   projection of the ledgers — without this the working store keeps serving
   the register as it stood before your edits, which is what "the DB is
   7+ commits stale" meant in practice. ingest.sh rebuilds on its own runs;
   this line is what covers a PROCESS run that lands new problems and never
   touches ingest. It is a rebuild, not a migration: fetch_log and match_log
   are history and are never dropped.

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
