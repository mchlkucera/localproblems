#!/usr/bin/env bash
# scripts/ingest.sh — the single entry point both runners exec.
#
# Invoked as:  /bin/bash /abs/repo/scripts/ingest.sh [feed-key ...]
#
# ------------------------------------------------------------------------------
# WHY THIS IS NOT WRAPPED IN `direnv exec .`
#
# It was going to be. Measured instead: `direnv exec .` fires the sops hook,
# prints "direnv: using sops .env.enc", exits clean — and exports NOTHING but
# DIRENV_* variables. A wrapper built on it would look correct, run green, and
# authenticate nothing, which is the same failure shape as a 200 carrying a
# login page.
#
# The working path is `with-secrets`, which deliberately REFUSES bash, node and
# python: an interpreter can encode a secret past its output scrubber. So this
# script cannot be wrapped wholesale, and neither can normalize.py. Any
# authenticated call site has to be built individually, with the secret expanded
# into the request itself rather than into the environment — e.g.
#   with-secrets curl --variable '%TOKEN' --expand-header 'Authorization: {{TOKEN}}' ...
#
# Consequence, stated rather than hidden: everything below runs UNAUTHENTICATED
# except the one feed that builds its own authenticated curl (fetch_hlidac.sh).
# That is the whole point — the mechanical half of ingest is the majority of the
# freshness win, and it degrades loudly instead of silently.
# ------------------------------------------------------------------------------
#
# EXIT CODES, AND WHY THERE ARE THREE. A scheduler has to be able to tell "two
# feeds were down" from "I have no idea what happened", because the correct
# response differs: the first is normal weather for a 19-feed registry and must
# not page anyone, the second means the run left no audit trail and the next run
# will be reasoning from a fetch_log with a hole in it.
#
#   0  clean: every feed met its contract and the run is fully audited.
#   1  FEEDS FAILED, RUN AUDITED. At least one feed failed its contract or its
#      fetch. contract.json, fetch_log, feed_health.json and register.db are all
#      current, so the failure is visible on /sources. NOT fatal for a scheduler.
#   2  THE RUN IS UNAUDITED. normalize, fetchlog, health or rebuild did not
#      complete, so we cannot say what this run did. This is the one that
#      deserves attention, and it is deliberately the rarer code.
#
# bash 3.2 on this Mac: no associative arrays, no mapfile. Keep it that way —
# launchd resolves bash to 3.2.57.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

TODAY="$(date +%Y-%m-%d)"
RAW="data/raw/$TODAY"
export TODAY RAW
mkdir -p "$RAW"

FEED_RC=0    # a feed did not deliver. Expected weather.
AUDIT_RC=0   # we cannot say what this run did. Not weather.

# 0. PRUNE — INGEST.md step 1, and it existed in NO script until now.
#    data/raw/ is a 28-day cache, not a record: `quote` is captured at ingest
#    precisely because the payload it was verified against is gone by the time
#    anyone wants to re-check it. Left unpruned this directory grows without
#    bound (one yc-oss pull alone is 10.4 MB, re-fetched daily).
#
#    manifest.md IS KEPT. It is the one file under data/raw/ that is committed —
#    the human-readable record of what each fetch did — so pruning the folder
#    wholesale would stage a deletion of tracked files on every run. Payloads
#    are the cache; the manifest is the record. `find -delete` implies -depth,
#    so files go before the directories holding them and `.fetch/` disappears
#    with its receipts.
CUTOFF="$(date -v-28d +%Y-%m-%d 2>/dev/null || date -d '28 days ago' +%Y-%m-%d)"
pruned=0
for d in data/raw/*/; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  # Only ever touch a directory whose name IS a run date. A typo elsewhere in
  # this loop can then delete nothing that is not a dated payload cache.
  case "$name" in
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
    *) continue ;;
  esac
  [ "$name" \< "$CUTOFF" ] || continue
  find "$d" -mindepth 1 ! -name manifest.md -delete 2>/dev/null
  pruned=$((pruned + 1))
done
echo "ingest: pruned payloads from $pruned run dir(s) dated before $CUTOFF (manifest.md kept)"

# 1. FETCH — pure script, registry-driven, per-feed argv.
#    The fetchers DO NOT share a signature: fetch_ted.sh and fetch_hlidac.sh
#    take SINCE as $1 and the outdir as $2, while fetch_feeds.sh, fetch_suggest.sh,
#    fetch_reddit.sh and fetch_nku.sh take the outdir as $1. A generic dispatcher
#    that calls "$script" "$RAW" hands TED a directory path as its since-date and
#    it queries a garbage window — which then looks like a yield anomaly rather
#    than a bug. That dispatch table lives in fetch_all.sh, which a different
#    worker owns.
if [ -x scripts/fetch_all.sh ]; then
  scripts/fetch_all.sh "$RAW" "$@" || FEED_RC=1
else
  echo "ingest: scripts/fetch_all.sh not present or not executable — SKIPPING FETCH." >&2
  echo "ingest: normalize will run over whatever already sits in $RAW." >&2
  FEED_RC=1
fi

# 2. NORMALIZE — THE ARITHMETIC PATH. No model, no secrets, no network.
#    Evaluates every feed contract, mints ids, dedups against seen.txt, computes
#    scores.money and dated scores.urgency, extracts and verifies quotes, and
#    STAGES records. It appends nothing: every record still owes scale and
#    recurrence to a model, and unscored records are never written with default
#    scores.
#
#    A non-zero here is an AUDIT failure, not a feed failure: normalize is what
#    writes contract.json, and without contract.json step 3 has nothing to log.
python3 scripts/normalize.py --raw "$RAW" --mechanical-only || AUDIT_RC=2

# 2b. CONTRACT VERDICTS — read back what normalize decided, so the exit code
#     reflects the feeds and not just the exit codes of the scripts. A feed can
#     fail its contract while every command in this file exits 0; that is the
#     whole point of having contracts.
if [ -f "$RAW/contract.json" ]; then
  failed="$(python3 -c "
import json,sys
try:
    r = json.load(open(sys.argv[1]))['results']
except Exception:
    print('ERR'); raise SystemExit(0)
print(sum(1 for x in r if not x.get('ok')))
" "$RAW/contract.json" 2>/dev/null || echo ERR)"
  case "$failed" in
    ''|ERR|*[!0-9]*) echo "ingest: could not read $RAW/contract.json — the run is UNAUDITED." >&2
                     AUDIT_RC=2 ;;
    0)               echo "ingest: all feeds met their contract." ;;
    *)               echo "ingest: $failed feed(s) failed their contract — see $RAW/manifest.md." >&2
                     FEED_RC=1 ;;
  esac
else
  echo "ingest: $RAW/contract.json was not written — the run is UNAUDITED." >&2
  AUDIT_RC=2
fi

# 3. HEALTH SPINE — contract results into fetch_log, then the admin space.
#    Both are audit steps: without them nothing on /sources moves and the next
#    run's consecutive-failure counts are computed off a gap.
python3 scripts/db.py fetchlog "$RAW" || AUDIT_RC=2
python3 scripts/db.py health || AUDIT_RC=2

# 4. REBUILD — the DB is what synthesis reads, and until this line existed
#    NOTHING in the automated chain ever called it. PROCESS.md step 7 commits
#    and deploys and never rebuilds, so `meta.git_head` sat at a commit from
#    before the errata ledger and the title sweep landed: "the DB is what
#    production reads" meant "production reads a stale snapshot".
#    It is safe to run here every time: rebuild DROPS and recreates only the
#    projections (signals, problems and friends), and never fetch_log or
#    match_log, which are history that exists nowhere else.
python3 scripts/db.py rebuild || AUDIT_RC=2

# 5. MODEL PASSES — WIRED, WORKING, AND OFF BY DEFAULT. All three matter.
#    This used to print "no measured proof that a nested `claude -p`
#    authenticates from this pipeline", and that reason is now WRONG: measured
#    2026-08-20, `with-secrets curl --variable '%ANTHROPIC_API_KEY'
#    --expand-header 'x-api-key: {{…}}' … /v1/messages` returns HTTP 200 from
#    claude-opus-5, and scripts/model_pass.{py,sh} run the two passes on that
#    seam. 3,092 records landed through it the same day.
#
#    IT STILL DOES NOT RUN HERE UNLESS ASKED. This script is what a scheduler
#    calls, and a scheduled run that silently spends money on every fetch is a
#    different program from the one anyone reviewed — the passes cost real
#    credit per record and the balance is finite (a run on 2026-08-20 ended on
#    HTTP 400 "credit balance is too low" mid-pass). So the capability is
#    opt-in, by an env flag an operator sets deliberately, and the default path
#    still stages and hands off. That is a budget decision, NOT a doubt about
#    whether it works.
if [ "${INGEST_MODEL_PASSES:-0}" = "1" ]; then
  echo "ingest: model passes ENABLED (INGEST_MODEL_PASSES=1) — this SPENDS API credit." >&2
  python3 scripts/model_pass.py plan  --raw "$RAW" --pass A --batch 50 || AUDIT_RC=2
  /bin/bash scripts/model_pass.sh "$RAW" A                              || FEED_RC=1
  python3 scripts/model_pass.py apply --raw "$RAW" --pass A || AUDIT_RC=2
  python3 scripts/model_pass.py plan  --raw "$RAW" --pass B --batch 25 || AUDIT_RC=2
  /bin/bash scripts/model_pass.sh "$RAW" B                              || FEED_RC=1
  python3 scripts/model_pass.py apply --raw "$RAW" --pass B || AUDIT_RC=2
  echo "ingest: model passes done. Records are FILLED but not appended:" >&2
  echo "ingest:   python3 scripts/normalize.py --raw $RAW --complete" >&2
else
  echo "ingest: model passes NOT run (INGEST_MODEL_PASSES is not 1). This is a" >&2
  echo "ingest: budget default, not a broken seam: the auth path is measured and" >&2
  echo "ingest: scripts/model_pass.{py,sh} work. Mechanical records are STAGED in" >&2
  echo "ingest: $RAW/staged.jsonl. Complete them with either:" >&2
  echo "ingest:   a. INGEST_MODEL_PASSES=1 /bin/bash scripts/ingest.sh   (spends credit)" >&2
  echo "ingest:   b. an ATTENDED session filling each record's \`_needs\` fields" >&2
  echo "ingest: then:" >&2
  echo "ingest:   python3 scripts/normalize.py --raw $RAW --complete" >&2
  echo "ingest:   python3 scripts/db.py upsert data/signals/<type>/$TODAY.jsonl" >&2
fi

# Deliberately no git: INGEST never commits or pushes. It leaves a clean working
# tree and PROCESSING picks the new lines up on its next run.
if [ "$AUDIT_RC" -ne 0 ]; then
  echo "ingest: EXIT 2 — the run is UNAUDITED (a normalize/fetchlog/health/rebuild step did not complete)." >&2
  exit 2
fi
if [ "$FEED_RC" -ne 0 ]; then
  echo "ingest: EXIT 1 — some feeds failed; the run is audited and visible on /sources." >&2
  exit 1
fi
echo "ingest: EXIT 0 — every feed met its contract and the run is fully audited."
exit 0
