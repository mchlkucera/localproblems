#!/usr/bin/env bash
# fetch_all.sh — the registry-driven fetch dispatcher (docs/architecture-v3.md §5.3).
# Usage: scripts/fetch_all.sh <outdir> [feed-key ...]
#   No feed keys  -> every `active` feed in data/feeds.json that has a script.
#   Feed keys     -> exactly those, regardless of status (except `dead`, never).
# Invoked by scripts/ingest.sh as: scripts/fetch_all.sh "$RAW" "$@"
set -uo pipefail   # NOT -e: one failing feed must never abort the rest
export LC_NUMERIC=C

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
shift 2>/dev/null || true
WANT="$*"

cd "$(dirname "$0")/.." || exit 1
REGISTRY="data/feeds.json"

# One run id shared by every fetcher this dispatcher starts, so all their
# manifest rows join into a single `fetch_log.run_id` (§2.3).
RUN_ID="${RUN_ID:-$(date -u +%Y-%m-%dT%H%M)}"
export RUN_ID

# ══════════════════════════════════════════════════════════════════════════════
#  THE ARGUMENT-POSITION LANDMINE — docs/architecture-v3.md §5.3
# ══════════════════════════════════════════════════════════════════════════════
#  THE FIVE ORIGINAL FETCHERS DO NOT SHARE A SIGNATURE. A generic dispatcher
#  that calls `"$script" "$OUTDIR"` hands TED a DIRECTORY PATH as its since-date:
#
#    scripts/fetch_ted.sh      $1 = SINCE (YYYYMMDD)    $2 = OUTDIR
#    scripts/fetch_hlidac.sh   $1 = SINCE (YYYY-MM-DD)  $2 = OUTDIR
#    scripts/fetch_feeds.sh    $1 = OUTDIR              --
#    scripts/fetch_suggest.sh  $1 = OUTDIR              --
#    scripts/fetch_reddit.sh   $1 = OUTDIR              --
#    scripts/fetch_nku.sh      $1 = OUTDIR              $2.. = years  (new; joins
#                                                        the majority shape)
#
#  VERIFIED 2026-08-20 by reading all six scripts, not by trusting the table.
#  This fails SILENTLY: TED would query with a garbage since-date and return an
#  empty or wrong window, which looks like a yield anomaly rather than a bug.
#  Therefore the call shape is an EXPLICIT PER-FEED SWITCH, never a convention.
#  If you add a fetcher, add its case here and state its argv shape above.
# ══════════════════════════════════════════════════════════════════════════════
SINCE_YYYYMMDD="$(date -v-60d +%Y%m%d 2>/dev/null || date -d '60 days ago' +%Y%m%d)"
SINCE_ISO="$(date -v-70d +%Y-%m-%d 2>/dev/null || date -d '70 days ago' +%Y-%m-%d)"

# ── run manifest ── see the identical block in each fetcher ──────────────────
# The dispatcher writes rows ONLY for feeds it declines to run. A feed that is
# skipped without leaving a fetch_log row is invisible to `db.py health`, which
# is precisely the Mode-B silence §7.5 exists to make visible.
MANIFEST="$OUTDIR/manifest.md"
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

# ── the feed table ───────────────────────────────────────────────────────────
# Read from data/feeds.json when it exists (W1 owns that file; we only read it).
# The built-in fallback keeps this script runnable before the registry lands and
# is deliberately identical in shape: "key<TAB>status<TAB>script<TAB>allow_missing".
# `vestbee` appears in NEITHER: it is DEAD (301 -> /insights/rss.xml -> 404,
# re-measured 2026-08-20 at 313,275 bytes of 404 HTML) and its fetch line is gone.
feed_table() {
  if [ -f "$REGISTRY" ] && command -v jq >/dev/null 2>&1; then
    jq -r '
      .feeds[]
      | select((.role // "feed") != "enrichment")
      | select((.script // "") != "")
      | [ .key,
          (.status // "active"),
          .script,
          (if (.contract.allow_missing // false) then "1" else "0" end)
        ] | @tsv' "$REGISTRY" 2>/dev/null && return 0
  fi
  printf 'ted\tactive\tscripts/fetch_ted.sh\t0\n'
  printf 'hlidac\tactive\tscripts/fetch_hlidac.sh\t0\n'
  printf 'cc-cz\tactive\tscripts/fetch_feeds.sh\t0\n'
  printf 'yc-oss\tactive\tscripts/fetch_feeds.sh\t0\n'
  printf 'suggest\tactive\tscripts/fetch_suggest.sh\t0\n'
  printf 'reddit-new\tactive\tscripts/fetch_reddit.sh\t0\n'
  printf 'reddit-search\tactive\tscripts/fetch_reddit.sh\t0\n'
  printf 'nku\tactive\tscripts/fetch_nku.sh\t0\n'
}

wanted() { # key -> 0 if this run should include it
  [ -z "$WANT" ] && return 0
  for w in $WANT; do [ "$w" = "$1" ] && return 0; done
  return 1
}

# DRY_RUN=1 prints the exact argv each fetcher would receive and executes
# nothing. This exists so the §5.3 landmine stays AUDITABLE without spending a
# live fetch: `DRY_RUN=1 scripts/fetch_all.sh data/raw/X` shows at a glance that
# ted/hlidac get SINCE first and everything else gets the outdir first.
# bash 3.2 has indexed arrays (only ASSOCIATIVE arrays are missing), so "$@"
# passing here is safe and keeps every argument quoted exactly once.
run_feed() { # script arg...
  s="$1"; shift
  if [ "${DRY_RUN:-0}" = "1" ]; then
    printf '   DRY-RUN argv: %s' "$s"
    for a in "$@"; do printf ' [%s]' "$a"; done
    printf '\n'
    return 0
  fi
  "$s" "$@"
}

FEEDS_DONE=0   # fetch_feeds.sh serves BOTH cc-cz and yc-oss; run it exactly once
RAN=""; FAILED=""

# HERE-STRING, not a pipe: a piped while runs in a SUBSHELL and FEEDS_DONE /
# RAN / FAILED would all be discarded when the loop ended. bash 3.2 — no
# associative arrays, no mapfile (§ hard constraints).
while IFS=$'\t' read -r key status script allow_missing; do
  [ -n "${key:-}" ] || continue
  wanted "$key" || continue

  if [ "$status" = "dead" ]; then
    echo "-- $key: DEAD, never fetched"
    continue
  fi
  if [ -z "$WANT" ] && [ "$status" != "active" ]; then
    echo "-- $key: status=$status, not fetched this run"
    mf "$key" skipped 000 0 0 0 "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "" "registry status=$status"
    continue
  fi
  if [ ! -f "$script" ]; then
    echo "!! $key: script missing: $script"
    mf "$key" error 000 0 0 0 "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "" "script not found: $script"
    FAILED="$FAILED $key"
    continue
  fi

  # contract.allow_missing (§7.2 step 0) travels to the fetcher as an env var so
  # the REGISTRY stays the source of truth and no policy is hardcoded in a fetcher.
  export ALLOW_MISSING="${allow_missing:-0}"

  echo "══ $key ($script)"
  case "$key" in
    # ---- outdir is $2, SINCE is $1 -----------------------------------------
    ted)              run_feed "$script" "$SINCE_YYYYMMDD" "$OUTDIR" ;;
    hlidac)           run_feed "$script" "$SINCE_ISO"      "$OUTDIR" ;;
    # ---- outdir is $1 -------------------------------------------------------
    cc-cz|yc-oss)     if [ "$FEEDS_DONE" -eq 0 ]; then
                        run_feed "$script" "$OUTDIR"; FEEDS_DONE=1
                      else
                        echo "-- $key: already covered by this run's fetch_feeds.sh"
                        continue
                      fi ;;
    suggest)          run_feed "$script" "$OUTDIR" ;;
    reddit-new|reddit-search)
                      # Both keys are served by ONE fetch_reddit.sh run, which
                      # emits a manifest row per key. Guarded like fetch_feeds.
                      if [ "${REDDIT_DONE:-0}" -eq 0 ]; then
                        run_feed "$script" "$OUTDIR"; REDDIT_DONE=1
                      else
                        echo "-- $key: already covered by this run's fetch_reddit.sh"
                        continue
                      fi ;;
    nku)              run_feed "$script" "$OUTDIR" ;;
    *)                echo "!! $key: no argv shape defined in fetch_all.sh — REFUSING to guess."
                      echo "   Add an explicit case above; a wrong argv position fails silently (§5.3)."
                      mf "$key" error 000 0 0 0 "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "" \
                         "no argv shape defined in fetch_all.sh"
                      FAILED="$FAILED $key"; continue ;;
  esac
  rc=$?
  RAN="$RAN $key"
  [ "$rc" -ne 0 ] && FAILED="$FAILED $key(rc=$rc)"
done <<EOF
$(feed_table)
EOF

echo
echo "══ fetch_all done — run_id=$RUN_ID outdir=$OUTDIR"
echo "   ran:   ${RAN:-（none）}"
echo "   failed:${FAILED:- none}"
echo "   manifest: $MANIFEST"
[ -z "$FAILED" ]
