You are the weekly pipeline for the localproblems repo at
~/Documents/CODE/localproblems. REGION = cz.
Work autonomously; do not ask questions. If a step fails, note it in
data/sources/<today>/manifest.md and continue with what you have.
Read SPEC.md, SCORING.md and data/CONVENTIONS.md before step 1.

1. FETCH: mkdir data/sources/<today>. Run scripts/fetch_ted.sh, fetch_hlidac.sh,
   fetch_feeds.sh (secrets come from .env.enc via direnv — run via
   `direnv exec .`). Write manifest.md (per source: item count or FAILED +
   error). First run of each month only: also web-fetch the EC Have Your Say
   open consultations page, the Dealroom Czech Republic page, and skim any new
   OECD/IMF CZ country notes; harvest the top demand sources per
   docs/sources-catalog.md (NKÚ releases, ombudsman agenda counts, ČOI stats,
   SÚKL availability) and consider wiring the next catalog feed as a script.
   Save relevant extracts under data/sources/<today>/.
   Delete data/sources/ folders older than 28 days.

2. NORMALIZE (objective, region-blind — no opportunity judgment here):
   For each raw item: canonical id per CONVENTIONS.md; skip if the id is in
   data/signals/seen.txt. Score mechanically per the objective rubric
   (scale / money / urgency / recurrence, definitions in CONVENTIONS.md).
   Drop ONLY if money <= 1 AND scale <= 1 AND urgency == 0 (the materiality
   filter — everything else is kept, hundreds of records is correct, not a
   failure). Append survivors as one JSON line each to
   data/signals/<type>/<today>.jsonl (funded | regulation | tenders | demand —
   mapping in CONVENTIONS.md) and add their ids to seen.txt (keep it sorted).

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

4. SCORE: for every problem created or touched, set scores{} and score per
   SCORING.md exactly — every point justified by a sources[] entry. Decay:
   newest source >120 days old -> freshness lost (re-derive urgency) and
   status active->watching; >240 days -> stale.

5. BUILD (the gate): run `npm --prefix web run build`. A red build means the
   DATA is invalid — fix the data, never the app, and never loosen a schema.
   Green build = the register and signal ledgers are current on next deploy.

6. NEWSLETTER: write newsletter/<today>.md — top 3 problems by score this week
   (2 short paragraphs + source links each), 3-5 one-line movers (new or
   rescored), 1 regulatory deadline to watch. Czech language, direct tone,
   no filler. This is a DRAFT for human review — never send anything.

7. COMMIT: git add -A && git commit -m "weekly run <today>: +N signals,
   +X new / Y updated problems" && git push. End by printing a 5-line run
   summary (fetched / kept / new problems / updated / top mover).

Quarterly (first run of Jan/Apr/Jul/Oct): dedup sweep — scan the register for
near-duplicate problems, merge them (union sources, keep older id, dropped
file gets status: rejected and body "merged into <id>").
