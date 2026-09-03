You are the ingest loop for the localproblems repo at
~/Documents/CODE/localproblems. There is no REGION here: ingest is
region-blind and carries NO judgment. Work autonomously; do not ask
questions. If a step fails, note it in data/raw/<today>/manifest.md and
continue with what you have.
Read SPEC.md and data/CONVENTIONS.md before step 1. You do not need
SCORING.md — nothing in this loop touches a problem score.

Two entry points exist. This one (INGEST) runs hourly-ish and produces
evidence. pipeline/PROCESS.md runs on demand and produces judgment.
INGEST NEVER COMMITS AND NEVER PUSHES: it leaves new lines in the working
tree, and PROCESS commits them alongside the problems they produced. The
handoff is the git working tree, not a queue. Nothing polls, nothing
waits, nothing serves.

You are running in one of two modes. Know which:
  ATTENDED   — a Claude session executes this file as a prompt. Needs no
               API key. WORKS TODAY, and is how every record in the
               corpus was produced. Do all steps, model passes included.
  UNATTENDED — scripts/ingest.sh runs `claude -p "$(cat pipeline/INGEST.md)"`
               from a scheduler. UNPROVEN — ships wired, never yet
               observed to work. ANTHROPIC_API_KEY EXISTS in the
               vault, so this is NOT a missing-key problem; it is a
               plumbing problem — handing that value to a nested `claude -p`
               without an interpreter touching it (see the secrets rule in
               step 1). Nobody has yet measured a nested `claude -p`
               actually authenticating, so do not describe this mode as
               working until someone has. If the model passes cannot run,
               the wrapper stages the mechanical half and prints
               SKIP model passes. Do not work around it; do not invent a
               key; do not append a record the model never scored.
               There is NO scheduler installed and no launchd plist in this
               repo; `scripts/ingest.sh` is what one would call.

THE ATTENDED LOOP, WRITTEN DOWN AS THE PROCEDURE IT ACTUALLY IS. The split
is not a degraded mode — the mechanical half is a script precisely because
it carries no judgment, and the model half is a session precisely because
it does:

  1.  /bin/bash scripts/ingest.sh
      Prune, fetch, contract check, arithmetic normalize, fetch_log, health
      export, db.py rebuild. Appends NOTHING to the ledgers. Exit codes:
        0 clean · 1 some feeds failed (audited, NOT fatal) · 2 UNAUDITED.
  2.  Read data/raw/<today>/staged.jsonl. Every record carries `_needs` —
      the exact list of fields a model still owes it, derived from the same
      rule --complete refuses on, so filling `_needs` is sufficient by
      construction. Fill them IN PLACE (steps 3b and 3d below are what
      "filling" means). Never invent a value to clear the list.
  3.  python3 scripts/normalize.py --raw data/raw/<today> --complete
      Applies materiality, appends survivors to the ledgers + seen.txt.
      It REFUSES the whole run if any record is still incomplete; add
      --allow-incomplete only when you intend to append the complete ones
      and leave the rest staged.
  4.  python3 scripts/db.py upsert data/signals/<type>/<run-date>.jsonl
      Once per file --complete named, and read those names off --complete's
      own output rather than assuming today. <run-date> is the date in the
      data/raw/<date>/ directory you completed, NOT the day you are sitting
      here: step 2 routinely happens a session after step 1, and the ledger
      is named for the run, so that a fetch and its records agree on when
      they happened. --complete takes it from the --raw path; pass --today
      only to override it deliberately.
  5.  STOP. Do not commit (step 6).

Steps 1, 3, 4 and 5 are mechanical. Step 2 is the entire judgment surface of
this loop, and it is the only step that needs you.

0. PREFLIGHT: confirm the artifacts this loop drives exist —
   data/feeds.json, scripts/ingest.sh, scripts/fetch_all.sh,
   scripts/normalize.py, scripts/db.py. Any that is missing is a build gap, not
   something to improvise around: record it in the manifest by name and
   run only the steps whose tooling is present. Never hand-roll a
   replacement for a missing script — a one-off parser writes
   unreproducible records into an append-only ledger.

1. FETCH: mkdir data/raw/<today>. Drive the fetchers from the registry
   (data/feeds.json), running only entries with role: feed and status:
   active. THE FETCHERS DO NOT SHARE A SIGNATURE — a generic dispatcher
   that calls "$script" "$RAW" hands TED a directory path as its
   since-date and gets a silently wrong window back. The call shapes are
   explicit, never conventional:
     ted      scripts/fetch_ted.sh     <SINCE YYYYMMDD>   <rawdir>
     hlidac   scripts/fetch_hlidac.sh  <SINCE YYYY-MM-DD> <rawdir>
     veklep   scripts/fetch_veklep.sh  <SINCE YYYY-MM-DD> <rawdir>
     coi      scripts/fetch_coi.sh     <SINCE YYYY-MM-DD> <rawdir>
     nen      scripts/fetch_nen.sh     <SINCE YYYY-MM-DD> <rawdir>
     smlouvy  scripts/fetch_smlouvy.sh <SINCE YYYY-MM-DD> <rawdir>
     cc-cz    scripts/fetch_feeds.sh   <rawdir>
     yc-oss   scripts/fetch_feeds.sh   <rawdir>
     suggest  scripts/fetch_suggest.sh <rawdir>
     reddit-* scripts/fetch_reddit.sh  <rawdir>
     nku      scripts/fetch_nku.sh     <rawdir> [year ...]
     ec-hys   scripts/fetch_ec_hys.sh  <rawdir>
     vestbee  scripts/fetch_vestbee.sh <rawdir>
     sukl     scripts/fetch_sukl.sh    <rawdir>          (full snapshot;
                                                          takes no since-date)
     mpsv     scripts/fetch_mpsv.sh    <rawdir> [YYYY-MM]
     tacr     scripts/fetch_tacr.sh    <rawdir>          (asks; RSS + HTML)
     hackathon scripts/fetch_hackathons.sh <rawdir>      (asks; six pages)
     ---- role: enrichment. ZERO signals; never in a feed total ----------
     ares     scripts/fetch_ares.sh    <rawdir>
     shoptet  scripts/fetch_shoptet.sh <rawdir>
     upgates  scripts/fetch_upgates.sh <rawdir>
   Verify a signature against the script before adding a new row here
   rather than copying the shape of its neighbour — that is the exact
   mistake this table exists to prevent.
   ARES HAS AN ORDER DEPENDENCY, NOT JUST A SIGNATURE. fetch_ares.sh
   resolves the IČO worklist fetch_mpsv.sh leaves in the SAME rawdir, so
   it MUST run after mpsv, into that dir:
     scripts/fetch_all.sh data/raw/<today> mpsv ares
   Run alone it finds no worklist, resolves nothing and exits clean — a
   zero indistinguishable from "no employer candidates this month".
   fetch_all.sh now CHECKS this and logs a `skipped` manifest row instead
   of running; do not work around it by calling the script directly.
   THE ENRICHMENT ROWS ARE NOT IN THE DEFAULT RUN. A bare
   `fetch_all.sh <rawdir>` skips role: enrichment entirely — they are
   monthly lookup refreshes and ares is meaningless before mpsv. Naming
   one explicitly runs it.
   THE PAYLOAD FILENAME IS ALSO A CROSS-FILE CONTRACT, and it broke once
   already. normalize.py maps <raw>/<file> back to a registry feed key by
   matching a distinctive token in the name, so a fetcher renaming its
   output silently reassigns records to another feed's contract. The two
   shapes that are decided by name rather than by directory:
     fetch_reddit.sh   reddit-<sub>-new.rss     -> reddit-new
                       reddit-<sub>-q-<term>.rss -> reddit-search
     fetch_hlidac.sh   hlidac-<query>-p<N>.json  -> hlidac (all pages)
   Change a fetcher's output names and fix FILE_FEED_TOKENS /
   feed_for_file() in the same commit.
   A FEED THAT PARSES CLEANLY AND KEEPS NOTHING IS NOW AN ERROR. `ok=1
   items_kept=0` was this pipeline's signature failure — a live fetcher, a
   200, a clean contract, and no EXTRACTORS entry, so the extraction loop
   broke on the first item and the run looked like a quiet week. Two feeds
   sat there for weeks. normalize.py now fails the contract for any row
   with `signal_source` set and `role != enrichment` that has no
   extractor, and names the missing key. The enrichment rows above are the
   only ones for which items_kept 0 is a legal outcome, and they declare
   it: `signal_source: null`, `id_prefixes: []`.
   SECRETS NEVER TRANSIT THE SHELL. Do NOT use `direnv exec .` for them:
   the direnv->sops hook prints "using sops .env.enc", exits clean, and
   exports nothing but DIRENV_* bookkeeping. That silent no-op — not a
   missing key — is why the Hlídač feed has been failing quietly. The
   authenticated request carries the secret itself:
     with-secrets curl --variable '%HLIDAC_STATU_TOKEN' \
       --expand-header 'Authorization: Token {{HLIDAC_STATU_TOKEN}}' "$API/..."
   A SCRIPT CANNOT BE WRAPPED WHOLESALE. with-secrets refuses bash, node,
   python, jq, awk, sed and every other interpreter — by allowlist, not
   denylist, because an interpreter can encode a secret past the output
   scrubber and a previous denylist missed one. ONLY THE INDIVIDUAL curl
   CALL IS WRAPPED. This is non-obvious and a future author will try to
   simplify it back into a wrapped script; do not let them.
   THE HLÍDAČ TOKEN IS PRESENT. The name is HLIDAC_STATU_TOKEN. The
   ABSENT name is HLIDAC_TOKEN, and this file used to assert the opposite
   — "genuinely absent from the vault, so hlidac stays BROKEN until the
   owner adds it" — which parked a working feed behind an owner action
   nobody needed to take. Re-measured 2026-08-20 with a negative control,
   presence only, no value printed: %HLIDAC_TOKEN -> curl exit 2
   "variable expansion failure"; %HLIDAC_STATU_TOKEN -> HTTP 200, 25
   contracts. scripts/fetch_hlidac.sh probes both names in that order and
   now reports an INCONCLUSIVE probe as unknown rather than as presence.
   Write data/raw/<today>/manifest.md: per feed, item count or FAILED +
   error, plus the health summary from step 5. The manifest is the one
   file under data/raw/ that is committed; everything else there is
   gitignored and pruned. PRUNE: scripts/ingest.sh step 0 deletes every
   payload under a data/raw/<date>/ dated more than 28 days back and KEEPS
   that run's manifest.md — the payloads are the cache, the manifest is the
   committed record, so pruning the folder wholesale would stage a deletion
   of tracked files on every run.
   Google Suggest is capped at ONE run per day — the cap is the whole
   mitigation against a ban; never re-run it to "top up" a thin result.

2. CONTRACT CHECK (a contract violation is a FIRST-CLASS ERROR, louder
   than a non-200): a 500 is honest and self-healing; a 200 carrying a
   login page is a lie that quietly poisons the corpus. For each feed
   evaluate its data/feeds.json contract IN THIS ORDER:
   0. EXPECTED ABSENCE, before everything else. A calendar-keyed source
      has days that simply do not exist. Feeds with allow_missing: true
      treat a 404 on a calendar-keyed URL as `skipped`: it logs ok = 1
      with parse_method 'none', does NOT increment consecutive_failures,
      and does NOT move the feed toward BROKEN. This is not leniency —
      an alarm that cries wolf weekly is ignored within a month, and then
      the one real outage is invisible too.
   1. TRANSPORT — non-200, timeout, or zero bytes -> error, feed BROKEN.
   2. PARSE — payload does not parse as contract.parse -> error, BROKEN.
   3. FIELDS — a required_fields key missing from every item -> error,
      BROKEN. This is the check that catches a login page saved as .json.
   4. YIELD — count outside expected_yield -> yield_anomaly zero /
      below-range / above-range. `zero` is BROKEN; the others warn on
      /sources and escalate at 3 consecutive runs.
   Until 6 runs of history exist there is no rolling median, so
   expected_yield is the author's estimate and its `basis` says so; a
   feed with no history warns on `zero` only.
   On a PARSE or FIELDS violation, attempt LLM-fallback extraction over
   the raw payload and set extraction: llm-fallback on anything it
   recovers (see step 3). Under UNATTENDED mode with no key there is no
   model, so the violation cannot be rescued: the feed degrades to a LOUD
   ERROR and goes BROKEN, and recovery waits for an ATTENDED run. That is
   correct behaviour, not a gap — writing a degraded record and calling it
   success is the exact failure this check exists to catch.

3. NORMALIZE (objective, region-blind — no opportunity judgment here).
   THE ORDER OF THE FOUR SUB-STEPS IS LOAD-BEARING. The materiality
   filter sits BETWEEN the two model passes so we never pay to write a
   summary for a record we are about to discard. Accuracy is unaffected;
   only the order changes.
   3a. MECHANICAL (script, always runs — `--mechanical-only` is this pass
       on its own): canonical id per CONVENTIONS.md; skip if the id is in
       data/signals/seen.txt; structured field extraction (url, date,
       money_eur, geo_origin); scores.money as pure arithmetic on
       money_eur; scores.urgency by arithmetic wherever a machine-readable
       date exists; the verbatim `quote`; liveness http_status +
       fetched_at; extraction: structured. (2026-08-24: "TED CPV group ->
       sector" is GONE from this list — the scripted tender feeds are
       threshold firehoses now, mechanical keyword/category selection is
       dead, and `sector` is model pass A's duty in 3b.)
   3b. MODEL PASS A — scoring: scores.scale, scores.recurrence, the
       urgency grade-3 branch only ("already in force AND actively
       enforced"), and — since 2026-08-24 — `sector` for every scripted
       feed whose extractor carries no sector judgment (ted, hlidac,
       veklep among them): the fetchers select by uniform threshold or
       complete taxonomy only, so classification is model judgment here,
       never a keyword list in a fetch script. Also for suggest/reddit
       the PAIN LANGUAGE bar — record
       only complaints, failures, workarounds; engagement metrics never
       justify a record, and neither feed may dominate the demand ledger.
       For the two `asks` feeds (hackathon, tacr) the admission bar is
       `stated_need`, a SIBLING of `pain` with its own rubric sentence
       (scripts/model_pass.py RUBRIC): does the owner name a concrete need
       a builder could start on — not a theme, an open call for ideas, a
       bare topic line or a vendor's pitch. Not `pain`: an ask is not a
       complaint, and grading it as one refused 29 of 39 real hospital and
       city asks on 2026-09-03. Like `pain` it is transport-only, never
       persisted, and a false verdict keeps the record staged.
       READ `_needs` ON EACH STAGED RECORD RATHER THAN THIS PARAGRAPH.
       It is derived from the same rule --complete refuses on, so a record
       filled to exactly its `_needs` is accepted by construction. That was
       NOT true until 2026-08-20: `geo_origin` was demanded by --complete,
       named by no `_needs` list, and set by no extractor, so an agent that
       did everything this file asked was still refused on every feed — the
       single defect standing between six working fetchers and a growing
       ledger. `geo_origin` is a model field on purpose: a Czech-language
       feed carrying a story about a German company makes "where the signal
       comes FROM" a judgment, and the mechanical pass carries none.
       Validate before anything is written: one entry per input, every
       score an integer 0-3. Retry a malformed batch ONCE, then skip it
       and record the error. UNSCORED RECORDS ARE NEVER APPENDED WITH
       DEFAULT SCORES — they stay in data/raw/ and are listed in the
       manifest as pending. Losing freshness is recoverable; writing vibes
       into an append-only canonical ledger is not.
   3c. MATERIALITY DROP (script, the ONLY normalize-time filter): drop
       ONLY if money <= 1 AND scale <= 1 AND urgency == 0. For `asks` the
       scale bar is one rung lower — drop only at scale 0 — because a named
       owner stating a niche problem is the material fact, and one body's
       own internal need is not a market (owner, 2026-09-03; the rule lives
       in normalize.is_material, keyed on evidence_type). Everything else
       is kept — hundreds of records is correct, not a failure. For any
       aggregating feed, AGGREGATE BEFORE THIS FILTER: a per-item feed
       whose items each score money 1 is filtered out of existence while
       looking like it ran correctly.
   3d. MODEL PASS B — generation, SURVIVORS ONLY: the English title
       ("Thing — what it is") and the <=2-sentence English summary. Every
       feed needs this except yc-oss, which ships English one_liners and
       is the only script-only feed end to end.
   `quote` is a FLAT STRING on the signal record: a verbatim snippet
   <=300 chars, native language preserved, whitespace collapsed, no
   ellipsis inside a number. It is capturable ONLY here, while the raw
   payload is still on disk — data/raw/ is pruned at 28 days. For scripted
   feeds, REFUSE TO APPEND a record whose quote is not a literal substring
   of the fetched payload after whitespace collapse; for agent harvests
   the payload is prose you read, so it degrades to a manifest warning.
   The shape has an external consumer and is not ours to change alone —
   see CONVENTIONS.md.
   PERSONAL DATA: any feed whose source declares it carries personal data
   (mpsv does) is ALLOWLIST-ONLY — only the named-safe fields enter the
   record. A denylist fails open the day the publisher adds a field. Grep
   the produced JSONL for email and phone patterns and require ZERO
   matches before append. The ledgers are append-only and public, so a
   mistake here is permanent and public; there is no quiet cleanup.

4. APPEND + UPSERT: append survivors as one JSON line each to
   data/signals/<type>/<run-date>.jsonl (funded | regulation | tenders |
   demand | hiring — mapping in CONVENTIONS.md) and add their ids to
   data/signals/seen.txt, keeping it sorted. THE FILENAME IS THE RUN DATE,
   NEVER THE RECORD'S OWN `date`: db.py reads the filename as the run date
   because 145 committed records are legitimately dated in the future (a
   regulation signal carries its effective date), and yc-oss records carry
   a launch date as far back as 2010. Naming files after record dates would
   scatter one run across dozens of files and report every feed's freshness
   off the wrong number.
   THE RUN DATE IS ALSO NOT `date.today()`. It is the date naming the
   data/raw/<date>/ directory being completed — the same string db.py reads
   back — because this step is ATTENDED and routinely runs a session after
   the fetch. --complete derives it from --raw for exactly that reason;
   --today overrides it. Then:
     python3 scripts/db.py upsert data/signals/<type>/<run-date>.jsonl
     python3 scripts/db.py fetchlog data/raw/<run-date>
   The JSONL and seen.txt are canonical; data/register.db is a gitignored
   working store that is rebuildable from them and is never the arbiter.
   If you write a NEW field that SignalSchema does not already declare,
   the build will FAIL — the schema is strict on purpose, at the top level
   and on the nested scores object. That is the correct outcome: add the
   field to SignalSchema in the same change, or do not write it. Never
   loosen the schema to make a record fit.

5. HEALTH EXPORT: python3 scripts/db.py health -> data/feed_health.json.
   The file is COMMITTED and is a build input. Its `state` vocabulary
   (LIVE | STALE | BROKEN | PENDING) records OBSERVED REALITY and is
   never merged with the registry's `status` vocabulary (active | blocked
   | dead | planned), which records INTENT. A feed can be `active` and
   BROKEN — that combination is the entire point, and it is what several
   feeds have been for weeks with nobody noticing. A `skipped` run never
   contributes to any state transition. Print the same summary to the
   terminal and into data/raw/<today>/manifest.md, and name any feed that
   has been BROKEN for 3 consecutive runs so PROCESS.md can carry it into
   the weekly run summary. No paging, no webhook, no external service.

6. HAND OFF: STOP. Do not run git add, git commit, git push, the web
   build, or a deploy. Leave the new JSONL lines, seen.txt, manifest and
   feed_health.json uncommitted in the working tree; pipeline/PROCESS.md
   picks them up on its next run. End by printing a 5-line run summary:
   feeds fetched / items fetched / kept after materiality / pending
   (unscored) / feeds BROKEN.
