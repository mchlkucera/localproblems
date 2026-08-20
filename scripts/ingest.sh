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
# and needs no secret at all. That is the whole point — the mechanical half of
# ingest is the majority of the freshness win, and it degrades loudly instead of
# silently.
# ------------------------------------------------------------------------------
#
# bash 3.2 on this Mac: no associative arrays, no mapfile. Keep it that way —
# launchd resolves bash to 3.2.57.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

TODAY="$(date +%Y-%m-%d)"
RAW="data/raw/$TODAY"
export TODAY RAW
mkdir -p "$RAW"

rc=0

# 1. FETCH — pure script, registry-driven, per-feed argv.
#    The five fetchers DO NOT share a signature: fetch_ted.sh and fetch_hlidac.sh
#    take SINCE as $1 and the outdir as $2, while fetch_feeds.sh, fetch_suggest.sh
#    and fetch_reddit.sh take the outdir as $1. A generic dispatcher that calls
#    "$script" "$RAW" hands TED a directory path as its since-date and it queries
#    a garbage window — which then looks like a yield anomaly rather than a bug.
#    That dispatch table lives in fetch_all.sh, which a different worker owns.
if [ -x scripts/fetch_all.sh ]; then
  scripts/fetch_all.sh "$RAW" "$@" || rc=$?
else
  echo "ingest: scripts/fetch_all.sh not present or not executable — SKIPPING FETCH." >&2
  echo "ingest: normalize will run over whatever already sits in $RAW." >&2
fi

# 2. NORMALIZE — THE ARITHMETIC PATH. No model, no secrets, no network.
#    Evaluates every feed contract, mints ids, dedups against seen.txt, computes
#    scores.money and dated scores.urgency, extracts and verifies quotes, and
#    STAGES records. It appends nothing: every record still owes scale and
#    recurrence to a model, and unscored records are never written with default
#    scores.
python3 scripts/normalize.py --raw "$RAW" --mechanical-only || rc=$?

# 3. HEALTH SPINE — contract results into fetch_log, then the admin space.
python3 scripts/db.py fetchlog "$RAW" || rc=$?
python3 scripts/db.py health || rc=$?

# 4. MODEL PASSES — WIRED BUT INERT.
#    ANTHROPIC_API_KEY exists in the vault, so this is no longer a missing-key
#    problem. It is a plumbing problem: nobody has measured a nested `claude -p`
#    authenticating from this pipeline, and the mechanism that would carry the
#    secret refuses interpreters. Until that probe is run and reported, this
#    branch stays off rather than pretending.
echo "ingest: SKIP model passes — no measured proof that a nested 'claude -p'" >&2
echo "ingest: authenticates from this pipeline. Mechanical records are STAGED in" >&2
echo "ingest: $RAW/staged.jsonl. Complete them in ATTENDED mode:" >&2
echo "ingest:   python3 scripts/normalize.py --raw $RAW --complete" >&2

# Deliberately no git: INGEST never commits or pushes. It leaves a clean working
# tree and PROCESSING picks the new lines up on its next run.
exit $rc
