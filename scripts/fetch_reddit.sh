#!/usr/bin/env bash
# fetch_reddit.sh — Reddit demand search via RSS (CZ subreddits). No auth.
# Ported from the demand-signals project; REWORKED 2026-08-15: Reddit now 403s
# all public .json endpoints regardless of UA, but .rss serves fine with a
# descriptive UA. Rate limit is tight (~1 req then 429) — curl --retry with a
# 35s delay honors it; keep sleeps generous.
# Usage: scripts/fetch_reddit.sh [outdir]          <-- outdir is $1 (see §5.3)
# Serves TWO registry feed keys: `reddit-new` (new.rss) and `reddit-search`
# (search.rss) — hence two manifest rows, one per key, not one per HTTP call.
set -uo pipefail   # no -e: one failed fetch must not kill the rest
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
UA="localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# One appended row per REGISTRY FEED KEY per run. These columns are the
# FETCH-SIDE half of the `fetch_log` schema (§2.3); `db.py fetchlog <dir>` reads
# this table and normalize.py fills items_kept / yield_anomaly / parse_method
# afterwards. NOTE: architecture-v3.md specifies the fetch_log COLUMNS but never
# specifies a manifest.md SCHEMA — this table IS that schema, named after the
# DDL columns so the mapping is 1:1 and needs no translation table.
#   result=ok      -> fetch_log.ok = 1
#   result=skipped -> fetch_log.ok = 1, parse_method='none'. EXPECTED ABSENCE
#                     (§7.2 step 0): a 404 on a calendar-keyed feed whose
#                     registry contract sets allow_missing:true. It MUST NOT
#                     increment consecutive_failures and MUST NOT move the feed
#                     toward BROKEN (§7.5).
#   result=error   -> fetch_log.ok = 0, `error` non-empty.
MANIFEST="$OUTDIR/manifest.md"
RUN_ID="${RUN_ID:-$(date -u +%Y-%m-%dT%H%M)}"
mf() { # feed_key result http bytes items ms started_at raw_path error
  if [ ! -f "$MANIFEST" ]; then
    { printf '# run manifest — %s\n\n' "$TODAY"
      printf 'Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/%s`.\n' "$TODAY"
      printf 'Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).\n'
      printf '`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,\n'
      printf '§7.2 step 0, never counts as a failure) · `error` (ok=0).\n\n'
      printf '| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |\n'
      printf '|---|---|---|---|---|---|---|---|---|---|\n'
    } > "$MANIFEST"
  fi
  printf '| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n' \
    "$RUN_ID" "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" \
    "$(printf '%s' "${9:-}" | tr '\n|' '  ' | cut -c1-200)" >> "$MANIFEST"

  # ── the MACHINE seam ── <raw>/.fetch/receipts.jsonl ─────────────────────────
  # WHY THIS EXISTS. scripts/normalize.py reconstructs the transport receipt as
  # `http_status = 200 if nbytes > 0 else None` (normalize.py:586) — it infers
  # the status code from whether a payload file exists on disk. That cannot tell
  # a 404 from a 403 from a feed that never ran, and it is precisely the
  # transport check §7.2 step 1 is supposed to perform. The true status code,
  # byte count and transfer time exist ONLY here, at fetch time, and are gone by
  # the time normalize runs. So each fetcher records them verbatim.
  #
  # Field names are exactly db.py's FETCHLOG_FIELDS (db.py:592-594) so a merge
  # into contract.json needs no translation. normalize.py should prefer these
  # values over its inferred ones and leave items_kept/yield_anomaly to itself.
  #
  # Lives in a SUBDIRECTORY on purpose: normalize.py's payload scan keeps only
  # os.path.isfile entries (normalize.py:556-558), so a directory is invisible
  # to it and can never be mistaken for a feed payload. `data/raw/*/*` also
  # gitignores it, which is correct — transport facts belong in the DB, not git
  # (§3). The committed human record stays manifest.md.
  if command -v jq >/dev/null 2>&1; then
    mkdir -p "$OUTDIR/.fetch"
    jq -nc --arg run_id "$RUN_ID" --arg feed_key "$1" --arg result "$2" \
           --arg http "$3" --arg bytes "$4" --arg items "$5" --arg ms "$6" \
           --arg started "$7" --arg raw "$8" --arg err "${9:-}" \
      '{run_id:$run_id, feed_key:$feed_key, started_at:$started,
        finished_at:(now|todateiso8601),
        http_status:(if ($http|length)==0 or $http=="000" then null else ($http|tonumber) end),
        bytes:(if ($bytes|length)==0 then null else ($bytes|tonumber) end),
        items_fetched:(if ($items|length)==0 then null else ($items|tonumber) end),
        items_kept:null,
        yield_anomaly:null,
        parse_method:(if $result=="skipped" then "none" else null end),
        runtime_ms:(if ($ms|length)==0 then null else ($ms|tonumber) end),
        ok:(if $result=="error" then 0 else 1 end),
        error:(if ($err|length)==0 then null else $err end),
        raw_path:(if ($raw|length)==0 then null else $raw end),
        result:$result}' >> "$OUTDIR/.fetch/receipts.jsonl" 2>/dev/null
  fi
}

# Parse curl's -w receipt into W_CODE / W_BYTES / W_SECS / W_MS.
# `set --` rebinds only THIS function's positional params, so callers are safe.
parse_w() { # "<http_code> <size_download> <time_total>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

SUBS="czech Brno Prague czechia"
QUERIES="nefunguje|problém|byrokracie|proč neexistuje"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
NEW_OK=0;  NEW_FAIL=0;  NEW_BYTES=0;  NEW_MS=0;  NEW_CODE=000;  NEW_ERRS=""
SRCH_OK=0; SRCH_FAIL=0; SRCH_BYTES=0; SRCH_MS=0; SRCH_CODE=000; SRCH_ERRS=""

rfetch() { # feed_key outfile url
  fkey="$1"; fname="$2"; furl="$3"
  # -f prevents the 403/429 BODY being written to $OUTDIR as a .rss file. The
  # pre-existing `code = 200` test already stopped this script LYING about the
  # result, but without -f the garbage payload still landed on disk where
  # normalize.py would find it. --remove-on-error clears any partial file.
  # Both checks stay: -f catches >=400, the 200 test catches a 3xx that lands.
  parse_w "$(curl -fsS -m 60 --retry 3 --retry-delay 35 -A "$UA" \
                  -o "$OUTDIR/$fname" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' "$furl" 2>/dev/null || true)"
  if [ "$W_CODE" = "200" ]; then
    echo "OK  $fname (HTTP $W_CODE, $W_BYTES bytes)"
  else
    echo "FAILED $fname (HTTP $W_CODE)"
  fi
  case "$fkey" in
    reddit-new)
      NEW_CODE="$W_CODE"; NEW_MS=$((NEW_MS + W_MS))
      if [ "$W_CODE" = "200" ]; then
        NEW_OK=$((NEW_OK+1)); NEW_BYTES=$((NEW_BYTES + W_BYTES))
      else
        NEW_FAIL=$((NEW_FAIL+1)); NEW_ERRS="$NEW_ERRS $fname:HTTP-$W_CODE"
      fi ;;
    reddit-search)
      SRCH_CODE="$W_CODE"; SRCH_MS=$((SRCH_MS + W_MS))
      if [ "$W_CODE" = "200" ]; then
        SRCH_OK=$((SRCH_OK+1)); SRCH_BYTES=$((SRCH_BYTES + W_BYTES))
      else
        SRCH_FAIL=$((SRCH_FAIL+1)); SRCH_ERRS="$SRCH_ERRS $fname:HTTP-$W_CODE"
      fi ;;
  esac
  sleep 10
}

for sub in $SUBS; do
  rfetch reddit-new "reddit-$sub-new.rss" "https://www.reddit.com/r/$sub/new.rss"
  # HERE-STRING, not `echo … | tr … | while`: a piped while runs in a SUBSHELL
  # and every counter rfetch touches would be discarded when the loop ended.
  while IFS= read -r q; do
    [ -n "${q:-}" ] || continue
    enc="$(printf '%s' "$q" | jq -sRr @uri)"
    rfetch reddit-search "reddit-$sub-q-$(printf '%s' "$q" | tr ' ' '_' | tr -cd '[:alnum:]_').rss" \
      "https://www.reddit.com/r/$sub/search.rss?q=$enc&restrict_sr=1&sort=new&t=year"
  done <<EOF
$(printf '%s' "$QUERIES" | tr '|' '\n')
EOF
done

emit() { # feed_key ok_count fail_count bytes ms code errs
  if [ "$2" -eq 0 ]; then
    mf "$1" error "$6" "$4" "$2" "$5" "$STARTED" "$OUTDIR" "all $3 fetches failed:$7"
  elif [ "$3" -gt 0 ]; then
    mf "$1" ok "$6" "$4" "$2" "$5" "$STARTED" "$OUTDIR" "partial: $3 of $(($2+$3)) failed:$7"
  else
    mf "$1" ok "$6" "$4" "$2" "$5" "$STARTED" "$OUTDIR" ""
  fi
}
emit reddit-new    "$NEW_OK"  "$NEW_FAIL"  "$NEW_BYTES"  "$NEW_MS"  "$NEW_CODE"  "$NEW_ERRS"
emit reddit-search "$SRCH_OK" "$SRCH_FAIL" "$SRCH_BYTES" "$SRCH_MS" "$SRCH_CODE" "$SRCH_ERRS"
echo "== reddit-new: $NEW_OK ok / $NEW_FAIL failed · reddit-search: $SRCH_OK ok / $SRCH_FAIL failed"
