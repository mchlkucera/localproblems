#!/usr/bin/env bash
# scripts/model_pass.sh — the AUTHENTICATED HALF of the model seam.
#
# Usage:  /bin/bash scripts/model_pass.sh <raw-dir> <A|B> [shard] [nshards]
#
# ------------------------------------------------------------------------------
# WHY A BASH SCRIPT SITS BETWEEN TWO PYTHON HALVES
#
# `with-secrets` is the only working path to the vault — `direnv exec .` fires
# the sops hook, prints "using sops .env.enc", exits clean and exports NOTHING
# but DIRENV_* bookkeeping — and it refuses bash, node, python, jq, awk and sed
# BY ALLOWLIST, because an interpreter can encode a secret past its output
# scrubber. So normalize.py (a python interpreter) can never be the process that
# holds ANTHROPIC_API_KEY, and THIS SCRIPT CANNOT BE WRAPPED WHOLESALE EITHER.
# Only the individual curl is wrapped, and the secret goes from the vault into
# the request without transiting any environment we control:
#
#     --variable '%ANTHROPIC_API_KEY'                imported by curl itself
#     --expand-header 'x-api-key: {{ANTHROPIC_API_KEY}}'   expanded by curl itself
#
# This is the same shape scripts/fetch_hlidac.sh uses for the Hlídač token, and
# it is deliberately NOT simplified into `with-secrets bash model_pass.sh`, which
# is refused by design. A future author will try. Do not let them.
#
# MEASURED 2026-08-20 before this file existed: the probe above returned HTTP 200
# from claude-opus-5. That measurement is why model_passes() in normalize.py is
# no longer inert.
# ------------------------------------------------------------------------------
#
# WHAT IT DOES: for every request file named in <raw>/.model/plan-<PASS>.list,
# POST it to /v1/messages and save the response under <raw>/.model/resp/<name>.json.
# A batch is DONE when its response file exists, so re-running skips finished
# work and a crash costs at most one in-flight batch. This script NEVER touches
# staged.jsonl — only `model_pass.py apply` does, and it writes temp+rename.
#
# SHARDING: shard i of n processes every batch whose position in the list is
# congruent to i (mod n), so n copies can run concurrently over one plan with no
# shared state and no write contention. Each writes only its own response files.
#
# bash 3.2 (launchd resolves bash to 3.2.57 on this box): no associative arrays,
# no mapfile. The batch loop reads the list on FD 3, not on stdin — curl and
# with-secrets both inherit stdin, and a loop reading its worklist from stdin
# loses the rest of that list the moment a child consumes it. Same class of bug
# as a piped `while` losing its counters to a subshell.

set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT" || exit 2

RAW="${1:?usage: model_pass.sh <raw-dir> <A|B> [shard] [nshards]}"
PASS="${2:?usage: model_pass.sh <raw-dir> <A|B> [shard] [nshards]}"
SHARD="${3:-0}"
NSHARD="${4:-1}"

MDIR="$RAW/.model"
LIST="$MDIR/plan-$PASS.list"
[ -f "$LIST" ] || { echo "model_pass.sh: no $LIST — run 'model_pass.py plan' first" >&2; exit 2; }
mkdir -p "$MDIR/resp" "$MDIR/log" || exit 2

command -v with-secrets >/dev/null 2>&1 || {
  echo "model_pass.sh: with-secrets not on PATH. The model pass CANNOT run." >&2
  echo "  Do not work around this and do not export the key by hand." >&2
  exit 2; }

API="https://api.anthropic.com/v1/messages"
LOG="$MDIR/log/driver-$PASS-$SHARD.log"
i=0; sent=0; skipped=0; failed=0

echo "== model_pass $PASS shard $SHARD/$NSHARD started $(date -u +%Y-%m-%dT%H:%M:%SZ)" >>"$LOG"

while read -r req <&3; do
  [ -n "$req" ] || continue
  idx=$i
  i=$((i + 1))
  [ $((idx % NSHARD)) -eq "$SHARD" ] || continue

  name="$(basename "$req" .json)"
  resp="$MDIR/resp/$name.json"
  if [ -s "$resp" ]; then skipped=$((skipped + 1)); continue; fi
  tmp="$MDIR/resp/.$name.part"
  codef="$MDIR/resp/.$name.code"

  attempt=0
  while [ "$attempt" -lt 4 ]; do
    attempt=$((attempt + 1))
    # TRUNCATE THE STATUS FILE FIRST. If curl never runs — with-secrets refused,
    # the vault is locked, the sandbox blocked its mktemp — nothing writes this
    # file, and a leftover "200" from the previous attempt would be read as this
    # attempt's result. That is the same failure this repo already paid for once
    # in fetch_hlidac.sh's auth probe: a method that did not run must never read
    # as a success.
    printf '' > "$codef"
    # THE CURL RUNS ALONE — no pipe, no &&, no shell redirection. Its exit
    # status and the HTTP code are read from files afterwards, because piping it
    # anywhere would put the response (and with-secrets' scrubber) on the wrong
    # side of a subshell. `%output{...}` writes the status code straight to a
    # file, which is why no command substitution is needed around a call that
    # handles a secret.
    #
    # DELIBERATELY NO -f: on a 4xx the API's own JSON error body is the only
    # diagnostic there is, and -f would throw it away. Every curl in scripts/
    # that FETCHES A PAYLOAD carries -f; this one is a control-plane call whose
    # error body is the payload.
    with-secrets curl -sS -m 600 --variable '%ANTHROPIC_API_KEY' \
      --expand-header "x-api-key: {{ANTHROPIC_API_KEY}}" \
      -H 'anthropic-version: 2023-06-01' \
      -H 'content-type: application/json' \
      -d @"$req" -o "$tmp" -w "%output{$codef}%{http_code}" "$API"
    rc=$?
    code=""
    [ -f "$codef" ] && read -r code < "$codef"
    case "$code" in
      200)
        mv "$tmp" "$resp"
        sent=$((sent + 1))
        echo "$(date -u +%H:%M:%S) $name 200 (attempt $attempt)" >>"$LOG"
        break
        ;;
      429|500|502|503|504|529|"")
        # Retryable: rate limit, overload, or curl never got a response at all.
        echo "$(date -u +%H:%M:%S) $name HTTP '${code:-none}' rc=$rc attempt $attempt — backing off" >>"$LOG"
        sleep $((attempt * 20))
        ;;
      *)
        # A 4xx that is not 429 is our bug, not weather. Keep the body: it is
        # the only description of what the API objected to.
        echo "$(date -u +%H:%M:%S) $name HTTP $code rc=$rc — NOT retried" >>"$LOG"
        [ -f "$tmp" ] && mv "$tmp" "$MDIR/log/$name.err.json"
        failed=$((failed + 1))
        break
        ;;
    esac
    if [ "$attempt" -ge 4 ]; then
      failed=$((failed + 1))
      echo "$(date -u +%H:%M:%S) $name GIVING UP after $attempt attempts" >>"$LOG"
    fi
  done
done 3< "$LIST"

echo "model_pass $PASS shard $SHARD/$NSHARD: ok=$sent skipped=$skipped failed=$failed"
echo "== finished $(date -u +%Y-%m-%dT%H:%M:%SZ) ok=$sent skipped=$skipped failed=$failed" >>"$LOG"
[ "$failed" -eq 0 ] || exit 1
exit 0
