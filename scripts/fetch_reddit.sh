#!/usr/bin/env bash
# fetch_reddit.sh — Reddit demand search via RSS (CZ subreddits). No auth.
# Ported from the demand-signals project.
#
# ══ THE 429, MEASURED 2026-08-21 — AND WHY THE OLD SHAPE COULD NOT WIN ═══════
#
# data/feed_health.json said "transport: HTTP 429 — 3 of 4 failed". The doc
# docs/feeds-status.md said "the `.rss` + descriptive-UA mitigation works; no
# 429 seen". THE LEDGER WAS RIGHT AND THE DOC WAS WRONG, and the doc was wrong
# in an instructive way: it probed ONE URL at a time, and one URL at a time is
# exactly the workload that never trips this limiter.
#
# Reddit states its budget in the response, on every reply including the 429:
#     x-ratelimit-used: 1
#     x-ratelimit-remaining: 0.0
#     x-ratelimit-reset: <seconds>
# MEASURED, four back-to-back .rss GETs with the descriptive UA:
#     czech/new.rss    -> 200   used=1 remaining=0.0 reset=34
#     Brno/new.rss     -> 429   used=1 remaining=0.0 reset=34
#     Prague/new.rss   -> 429   used=1 remaining=0.0 reset=33
#     czechia/new.rss  -> 429   used=1 remaining=0.0 reset=33
# The budget for an unauthenticated client on www.reddit.com is ONE REQUEST PER
# WINDOW, and the window is clock-aligned to the minute (a probe at 11:39:56
# reported reset=4; one at 11:40:26 reported reset=34 — both point at the next
# :00 boundary).
#
# That single fact explains the whole failure arithmetic. The old script issued
# 4 subs x (1 firehose + 4 pain queries) = 20 requests with `sleep 10` between
# them: ~200 s of wall clock, ~4 windows, so ~4 requests could ever succeed.
# The ledger recorded 1 of 4 firehose + 3 of 16 search = exactly 4 successes.
# The model predicts the observed failure to the request.
#
# `curl --retry 3 --retry-delay 35` could not save it either: 35 s is shorter
# than a window when the request lands early in one, so the retries burned
# themselves against the same closed door.
#
# NOT A WORKAROUND — MEASURED AND REJECTED: a shared cookie jar changes nothing
# (req1 200, req2 429, req3 429 with -c/-b), so the bucket is per-IP, not
# per-session. There is no client-side trick here; the only winning move is to
# ASK FOR LESS AND OBEY THE STATED RESET.
#
# ══ WHAT CHANGED ═════════════════════════════════════════════════════════════
#
# 1. FEWER REQUESTS, NOT LONGER SLEEPS. Reddit serves a merged multireddit:
#    `/r/czech+Brno+Prague+czechia/new.rss?limit=100` is ONE request that
#    returns 100 entries across all four subs (MEASURED: 76 czech / 16 Prague /
#    8 Brno). 20 requests collapse to 2. At the registry's 6h cadence these
#    subs produce far fewer than 100 posts per window, so recall is unharmed.
# 2. THE SERVER SETS THE PACE. After every reply the script reads
#    `x-ratelimit-reset` and waits exactly that long (+ a small margin) instead
#    of guessing a sleep. If Reddit changes its window, this follows without an
#    edit — which is the least-fragile shape available on an undeclared limit.
# 3. A 429 IS RETRIED AGAINST THE STATED RESET, not against a fixed delay.
#
# Serves TWO registry feed keys: `reddit-new` (new.rss) and `reddit-search`
# (search.rss) — hence two manifest rows, one per key, not one per HTTP call.
# Usage: scripts/fetch_reddit.sh [outdir]          <-- outdir is $1 (see §5.3)
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

# ONE merged multireddit instead of one request per sub — see header note 1.
SUBS_PATH="${REDDIT_SUBS:-czech+Brno+Prague+czechia}"
QUERIES="nefunguje|problém|byrokracie|proč neexistuje"
LIMIT="${REDDIT_LIMIT:-100}"
# `combined` = one OR query for all pain terms (1 request). `per-term` = one
# request per term (4 requests, ~4 more minutes) — see the recall note at the
# search block below.
SEARCH_MODE="${REDDIT_SEARCH_MODE:-combined}"
MAX_RETRIES="${REDDIT_MAX_RETRIES:-3}"
RESET_MARGIN="${REDDIT_RESET_MARGIN:-3}"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
NEW_OK=0;  NEW_FAIL=0;  NEW_BYTES=0;  NEW_MS=0;  NEW_CODE=000;  NEW_ITEMS=0; NEW_ERRS=""
SRCH_OK=0; SRCH_FAIL=0; SRCH_BYTES=0; SRCH_MS=0; SRCH_CODE=000; SRCH_ITEMS=0; SRCH_ERRS=""
HDR="${TMPDIR:-/tmp}/reddit-hdr.$$"
cleanup() { [ -f "$HDR" ] && find "$HDR" -type f -delete 2>/dev/null; }
trap cleanup EXIT

# The reset the server asked for on the LAST reply. 0 = no wait owed yet.
RL_RESET=0

# Read the rate-limit budget off the header dump. The FIRST status line in the
# dump can be the proxy's `HTTP/1.1 200 Connection Established`, so the reset
# header is read by name (tail -1 = the real response's, not the CONNECT's).
read_rl() {
  RL_RESET=$(grep -i '^x-ratelimit-reset:' "$HDR" 2>/dev/null \
             | tr -d '\r' | awk '{print $2}' | tail -1)
  case "${RL_RESET:-}" in ''|*[!0-9.]*) RL_RESET=0 ;; esac
  RL_RESET=$(awk -v r="${RL_RESET:-0}" 'BEGIN{printf "%d", r}')
}

# Wait out the window the server declared. This replaces the old fixed
# `sleep 10`, which was shorter than the window and therefore guaranteed a 429.
rl_wait() {
  w=$((RL_RESET + RESET_MARGIN))
  [ "$w" -gt 0 ] || w="$RESET_MARGIN"
  echo "    …waiting ${w}s for the rate-limit window the server declared (reset=$RL_RESET)"
  sleep "$w"
}

# One fetch, retried against the server's own reset until it lands or the retry
# budget runs out. Sets R_CODE / R_BYTES / R_MS / R_ITEMS.
rfetch() { # outfile url
  fname="$1"; furl="$2"
  R_CODE=000; R_BYTES=0; R_MS=0; R_ITEMS=0
  attempt=0
  while [ "$attempt" -le "$MAX_RETRIES" ]; do
    [ "$attempt" -gt 0 ] && rl_wait
    : > "$HDR"
    # -f prevents the 403/429 BODY being written to $OUTDIR as a .rss file.
    # --remove-on-error clears any partial file. The explicit `code = 200` test
    # is NOT redundant with -f: --fail only trips at HTTP >= 400, so a 3xx that
    # lands bytes still needs catching. -D still captures the response headers
    # on a failed transfer (MEASURED), which is what makes the backoff possible.
    parse_w "$(curl -fsS -m 60 -A "$UA" -D "$HDR" \
                    -o "$OUTDIR/$fname" --remove-on-error \
                    -w '%{http_code} %{size_download} %{time_total}' "$furl" 2>/dev/null || true)"
    read_rl
    R_CODE="$W_CODE"; R_MS=$((R_MS + W_MS))
    if [ "$W_CODE" = "200" ]; then
      # ── MODE-A GUARD ── a 200 carrying the wrong body. Reddit answers some
      # blocks with an HTML interstitial at status 200; an HTML page stored as
      # a .rss payload is the §7.1 failure this repo has already been bitten by.
      if ! head -c 400 "$OUTDIR/$fname" 2>/dev/null | grep -q '<feed\|<rss\|<?xml'; then
        echo "FAILED $fname — MODE-A: HTTP 200 but body is not XML."
        echo "       first 120 bytes: $(head -c 120 "$OUTDIR/$fname" 2>/dev/null | tr -d '\n')"
        find "$OUTDIR" -name "$fname" -type f -delete 2>/dev/null
        R_CODE="200-not-xml"
        return 1
      fi
      # `grep -o | wc -l`, NOT `grep -c`: -c counts matching LINES and Reddit
      # ships the whole feed on ONE line, so -c reports 1 where the real count
      # is 100. A silently-wrong item count is the yield check lying to itself.
      R_ITEMS=$(grep -o '<entry' "$OUTDIR/$fname" 2>/dev/null | wc -l | tr -d ' ')
      [ -n "$R_ITEMS" ] || R_ITEMS=0
      R_BYTES="$W_BYTES"
      echo "OK  $fname (HTTP 200, $W_BYTES bytes, $R_ITEMS entries)"
      return 0
    fi
    if [ "$W_CODE" = "429" ]; then
      echo "    429 on $fname (attempt $((attempt+1))/$((MAX_RETRIES+1))) — server says reset=$RL_RESET"
      attempt=$((attempt + 1))
      continue
    fi
    echo "FAILED $fname (HTTP $W_CODE)"
    return 1
  done
  echo "FAILED $fname — still 429 after $((MAX_RETRIES+1)) attempts"
  return 1
}

# ── 1. the firehose: ONE request for all four subs ───────────────────────────
# Filename must NOT contain a REDDIT_SEARCH_MARKER ("-q-" or "search"), or
# normalize.py files it under reddit-search (normalize.py:350-352).
if rfetch "reddit-cz4-new.rss" \
          "https://www.reddit.com/r/$SUBS_PATH/new.rss?limit=$LIMIT"; then
  NEW_OK=1; NEW_ITEMS="$R_ITEMS"; NEW_BYTES="$R_BYTES"
else
  NEW_FAIL=1; NEW_ERRS=" reddit-cz4-new.rss:HTTP-$R_CODE"
fi
NEW_CODE="$R_CODE"; NEW_MS="$R_MS"

# ── 2. the pain search ───────────────────────────────────────────────────────
# RECALL TRADEOFF, STATED. `combined` sends ONE OR-query for all four terms and
# takes the 100 newest matches. MEASURED: it returns a full page of 100, i.e.
# it TRUNCATES — over a year of history that loses older matches. At the
# registry's daily cadence that is harmless (these subs do not produce 100
# pain-matching posts a day and everything older is already in seen.txt), but a
# COLD START or a long outage would silently under-read. REDDIT_SEARCH_MODE=
# per-term spends 4 requests (≈4 more minutes) to restore full-history recall.
if [ "$SEARCH_MODE" = "per-term" ]; then
  # HERE-STRING, not `echo … | while`: a piped while runs in a SUBSHELL and
  # every counter rfetch touches would be discarded when the loop ended.
  while IFS= read -r q; do
    [ -n "${q:-}" ] || continue
    rl_wait
    enc="$(printf '%s' "$q" | jq -sRr @uri)"
    slug="$(printf '%s' "$q" | tr ' ' '_' | tr -cd '[:alnum:]_')"
    if rfetch "reddit-cz4-q-$slug.rss" \
              "https://www.reddit.com/r/$SUBS_PATH/search.rss?q=$enc&restrict_sr=1&sort=new&t=year&limit=$LIMIT"; then
      SRCH_OK=$((SRCH_OK+1)); SRCH_ITEMS=$((SRCH_ITEMS + R_ITEMS)); SRCH_BYTES=$((SRCH_BYTES + R_BYTES))
    else
      SRCH_FAIL=$((SRCH_FAIL+1)); SRCH_ERRS="$SRCH_ERRS reddit-cz4-q-$slug.rss:HTTP-$R_CODE"
    fi
    SRCH_CODE="$R_CODE"; SRCH_MS=$((SRCH_MS + R_MS))
  done <<EOF
$(printf '%s' "$QUERIES" | tr '|' '\n')
EOF
else
  rl_wait
  orq="$(printf '%s' "$QUERIES" | sed 's/|/ OR /g')"
  enc="$(printf '%s' "$orq" | jq -sRr @uri)"
  if rfetch "reddit-cz4-q-pain.rss" \
            "https://www.reddit.com/r/$SUBS_PATH/search.rss?q=$enc&restrict_sr=1&sort=new&t=year&limit=$LIMIT"; then
    SRCH_OK=1; SRCH_ITEMS="$R_ITEMS"; SRCH_BYTES="$R_BYTES"
  else
    SRCH_FAIL=1; SRCH_ERRS=" reddit-cz4-q-pain.rss:HTTP-$R_CODE"
  fi
  SRCH_CODE="$R_CODE"; SRCH_MS="$R_MS"
fi

emit() { # feed_key ok_count fail_count bytes ms code items errs
  if [ "$2" -eq 0 ]; then
    mf "$1" error "$6" "$4" "$7" "$5" "$STARTED" "$OUTDIR" "all $3 fetches failed:$8"
  elif [ "$7" -eq 0 ]; then
    # A clean 200 that carried zero entries is the yield=zero anomaly, not a
    # success — it must be LOUD rather than read as a healthy empty day.
    mf "$1" error "$6" "$4" 0 "$5" "$STARTED" "$OUTDIR" "yield: 200 OK but zero entries parsed"
  elif [ "$3" -gt 0 ]; then
    mf "$1" ok "$6" "$4" "$7" "$5" "$STARTED" "$OUTDIR" "partial: $3 of $(($2+$3)) failed:$8"
  else
    mf "$1" ok "$6" "$4" "$7" "$5" "$STARTED" "$OUTDIR" ""
  fi
}
emit reddit-new    "$NEW_OK"  "$NEW_FAIL"  "$NEW_BYTES"  "$NEW_MS"  "$NEW_CODE"  "$NEW_ITEMS"  "$NEW_ERRS"
emit reddit-search "$SRCH_OK" "$SRCH_FAIL" "$SRCH_BYTES" "$SRCH_MS" "$SRCH_CODE" "$SRCH_ITEMS" "$SRCH_ERRS"
echo "== reddit-new: $NEW_OK ok / $NEW_FAIL failed, $NEW_ITEMS entries fetched"
echo "== reddit-search: $SRCH_OK ok / $SRCH_FAIL failed, $SRCH_ITEMS entries fetched (mode=$SEARCH_MODE)"
