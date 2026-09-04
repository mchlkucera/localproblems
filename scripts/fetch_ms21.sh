#!/usr/bin/env bash
# fetch_ms21.sh — MS2021+ approved-project open data -> data/lookup/, NOT a feed.
#
# ══ WHAT THIS IS ═════════════════════════════════════════════════════════════
# MMR publishes every approved 2021-27 EU-cofinanced project in one XML export:
# CC BY 4.0, AUTOR="Ministerstvo pro místní rozvoj", 146,410,196 bytes,
# 40,988 <PRJ>, MEASURED 2026-09-04. Each project carries the beneficiary's OWN
# <PROBLEM> statement beside the money approved against it and the buyer's IČO.
# That is the register's weakest question — who paid how much, and what problem
# did that buyer say it solved — in one file.
#
# ══ IT WRITES A LOOKUP TABLE AND GETS NO REGISTRY ROW, ON PURPOSE ════════════
# 40,988 projects each carrying real money would flood data/signals/** (16,237
# records today) and nearly all of them would pass materiality. data/feeds.json
# already parked `smlouvy` for exactly this: "a PER-ITEM feed whose items each
# score money 1 or 0 … walks straight into the trap CONVENTIONS.md names for
# `hiring`", where the fix is aggregation before materiality. Here the fix is
# not to make it evidence at all. Output is data/lookup/ms21-public-projects.jsonl
# (CONVENTIONS.md "Lookup layer": committed, never pruned, no evidence type, no
# score, not walked by db.py or the build gate), read on demand by
# scripts/ms21_query.py. So: NO row in data/feeds.json, and nothing is ever
# written into the run directory's root where normalize.py would find it and
# try to parse it as an unknown feed (the fetch_tacr.sh rule).
#
# The manifest row and the receipt are still written, in the fetch_tacr.sh
# shape, because "did the 146 MB actually arrive today" is a transport question
# like any other. MEASURED: normalize.py consults receipts as
# `receipts.get(feed_key)` per REGISTERED feed only, so an `ms21` key it does
# not know is inert — it is a record for humans, not an orphan feed.
#
# Usage: scripts/fetch_ms21.sh [outdir]      <-- outdir is $1 (the nku/tacr shape)
set -uo pipefail   # no -e: a failed transfer must still write its receipt
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
INDEXER="$HERE/ms21_index.py"

URL="${MS21_URL:-https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml}"
LOOKUP="${MS21_LOOKUP:-$ROOT/data/lookup/ms21-public-projects.jsonl}"
UA="localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

# ── the conditional-GET cache, AND IT HOLDS THE BODY ─────────────────────────
# Same call fetch_coi.sh made, and for a stronger reason here. A 304 says the
# 146 MB we already have is current; if the cache held only the ETag, a 304
# would leave us with a validator and no bytes, and the only way to rebuild the
# index would be to poison the cache and re-download. It MUST outlive the run
# directory: data/raw/<date>/ is pruned at 28 days, and ingest.sh's pruner only
# touches directories WHOSE NAME IS AN ISO DATE, so data/raw/.cache/ survives —
# and `data/raw/*` in .gitignore keeps 146 MB out of git.
CACHE="${MS21_CACHE:-$ROOT/data/raw/.cache/ms21}"
mkdir -p "$CACHE"
BODY="$CACHE/SeznamOperaci_21_27.xml"
ETAG="$CACHE/SeznamOperaci_21_27.etag"

# No `rm` in this script. `find <path> -maxdepth 0 -delete` removes exactly the
# named path and nothing else, and a missing file is not news.
rmf() {
  for f in "$@"; do
    [ -e "$f" ] && find "$f" -maxdepth 0 -delete 2>/dev/null
  done
  return 0
}

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# Verbatim from fetch_tacr.sh — the manifest is a cross-file contract, not a
# place for local taste.
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
  # The true status, byte count and transfer time exist ONLY here, at fetch
  # time. Field names are db.py's FETCHLOG_FIELDS. Lives in a subdirectory so
  # normalize.py's payload scan (isfile only) can never mistake it for a feed.
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

# Parse curl's -w receipt into W_CODE / W_BYTES / W_SECS / W_MS / W_CT.
# `set --` rebinds only THIS function's positional params, so callers are safe.
parse_w() { # "<http_code> <size_download> <time_total> <content_type>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_CT="${4:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

command -v jq >/dev/null 2>&1 || { echo "fetch_ms21: jq is required" >&2; exit 2; }
[ -f "$INDEXER" ] || { echo "fetch_ms21: $INDEXER missing" >&2; exit 2; }

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
mkdir -p "$OUTDIR/.fetch"
NEW="$OUTDIR/.fetch/ms21-body.xml"
ETAGNEW="$OUTDIR/.fetch/ms21.etag.new"

echo "== ms21  $URL"

# ── 1. CONDITIONAL GET ───────────────────────────────────────────────────────
# BOTH validators are sent, because this host serves both (MEASURED 2026-09-04:
# ETag "c01136bc63bdd1:0" AND Last-Modified). --etag-compare sends
# If-None-Match; --time-cond sends If-Modified-Since from the cached BODY's
# mtime, which -R set to the server's Last-Modified on the download that
# produced it. Two validators cost nothing and either one alone can be dropped
# by an intermediary — and the thing being saved here is 146 MB per run.
#
# -f: a non-2xx must NOT be stored as if it were the export. --remove-on-error
# deletes the partial. The explicit code tests below are NOT redundant with -f:
# --fail only trips at HTTP >= 400, so 304 — the one we specifically want to
# see — passes it.
TIMECOND=""
[ -f "$BODY" ] && TIMECOND="$BODY"
# shellcheck disable=SC2086
parse_w "$(curl -fsS -m 1800 --retry 2 --retry-delay 10 -L -R \
                -A "$UA" \
                --etag-compare "$ETAG" --etag-save "$ETAGNEW" \
                ${TIMECOND:+--time-cond "$TIMECOND"} \
                -o "$NEW" --remove-on-error \
                -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                "$URL" 2>/dev/null || true)"

# --etag-save WRITES TO A TEMP PATH AND IS PROMOTED ONLY WHEN NON-EMPTY.
# A 304 from these hosts DOES carry an ETag header and curl 8.7.1 TRUNCATES the
# --etag-save file to 0 bytes regardless; pointed straight at the durable cache
# entry, the first 304 destroys the validator that produced it and every later
# run re-downloads all 146 MB while still looking like a conditional GET. A curl
# behaviour, not a server one — the same guard is in fetch_nen.sh, fetch_coi.sh
# and fetch_sukl.sh.
if [ -s "$ETAGNEW" ]; then mv "$ETAGNEW" "$ETAG"; else rmf "$ETAGNEW"; fi

REBUILD=0; NOTE=""; RESULT=""; SRC=""
if [ "$W_CODE" = "304" ]; then
  rmf "$NEW"
  echo "   304 Not Modified — the cached export is current"
  if [ ! -s "$BODY" ]; then
    # A validator with no body. Poison it: the next run must re-request in full
    # rather than get another 304 against bytes we do not hold.
    rmf "$ETAG"
    echo "   but the cache holds NO body — validator poisoned, re-run to download"
    mf ms21 error "$W_CODE" "$W_BYTES" 0 "$W_MS" "$STARTED" "" \
       "304 against an empty cache: ETag deleted, re-run to refetch in full"
    exit 1
  fi
  SRC="$BODY"
  if [ -s "$LOOKUP" ]; then
    NOTE="304 — export unchanged and the index is present, nothing to rebuild"
    RESULT=skipped
  else
    NOTE="304 — export unchanged but the index was missing, rebuilt from cache"
    REBUILD=1
  fi
elif [ "$W_CODE" = "200" ]; then
  # ── 2. MODE A — THE SOURCE CONTRACT, BEFORE ANYTHING IS PROMOTED ───────────
  # A 200 proves the transfer, not the body. This host is IIS behind a proxy: a
  # maintenance page, an SSO landing page or a WAF block all arrive as 200
  # text/html, and a wrong body promoted into the cache is WORSE than a failed
  # run — the ETag beside it would then certify it, and every later 304 would
  # keep it. ms21_index.py refuses anything whose first bytes are not <EXPORT>
  # carrying the https://ms21xsd.mssf.cz/OpenData/v_1 namespace. The refused
  # body stays under .fetch/ as evidence, never promoted, never parsed.
  if ! META="$(python3 "$INDEXER" guard "$NEW" 2>&1)"; then
    echo "   FAILED — MODE-A: $META"
    echo "          content-type: $W_CT"
    echo "          first 120 bytes: $(head -c 120 "$NEW" | tr -d '\n')"
    rmf "$ETAG"   # we hold no good bytes for this validator
    mf ms21 error "$W_CODE" "$W_BYTES" 0 "$W_MS" "$STARTED" "$NEW" \
       "MODE-A refused: $META (ct=$W_CT)"
    exit 1
  fi
  echo "   200 OK, $W_BYTES bytes — guard passed: $META"
  mv "$NEW" "$BODY"
  SRC="$BODY"
  REBUILD=1
  NOTE="fresh export"
else
  rmf "$NEW"
  echo "   FAILED (HTTP $W_CODE)"
  mf ms21 error "$W_CODE" "$W_BYTES" 0 "$W_MS" "$STARTED" "" "HTTP-$W_CODE ct=$W_CT"
  exit 1
fi

# ── 3. THE INDEX ─────────────────────────────────────────────────────────────
N=0
if [ "$REBUILD" = "1" ]; then
  if ! SUMMARY="$(python3 "$INDEXER" index "$SRC" --out "$LOOKUP" 2>&1)"; then
    echo "   INDEX FAILED: $SUMMARY"
    mf ms21 error "$W_CODE" "$W_BYTES" 0 "$W_MS" "$STARTED" "$LOOKUP" \
       "index failed: $(printf '%s' "$SUMMARY" | tail -c 180)"
    exit 1
  fi
  jf() { printf '%s' "$SUMMARY" | jq -r "$1" 2>/dev/null; }
  N="$(jf .public)"
  echo "   indexed $N public-body project(s) of $(jf .projects) in the export"
  echo "   -> $LOOKUP  ($(jf .mb) MB)  licence: $(jf .licence)"
  echo "   $(jf .placeholder_problem) row(s) carry no problem statement (\"-\" / \"nerelevantní\" in the source)"
  NOTE="$NOTE; $(jf .mb)MB placeholder_problem=$(jf .placeholder_problem) no_theme=$(jf .no_theme)"
  RESULT=ok
else
  N="$(wc -l < "$LOOKUP" | tr -d ' ')"
  echo "   index untouched: $N row(s) already in $LOOKUP"
fi
case "$N" in ''|*[!0-9]*) N=0 ;; esac

# ── ZERO YIELD IS AN ERROR, NOT A QUIET OK ───────────────────────────────────
# SCRIPTED-SILENT is a named failure in this repo: a fetcher that runs clean
# while nothing lands. 146 MB that arrive and index to nothing means the HPF
# filter or the source shape moved, and an `ok` row with items=0 is exactly the
# shape that gets skimmed past.
if [ "$N" -eq 0 ]; then
  mf ms21 error "$W_CODE" "$W_BYTES" 0 "$W_MS" "$STARTED" "$LOOKUP" \
     "ZERO YIELD: the export parsed and produced no public-body rows — $NOTE"
  echo "== ms21: ZERO YIELD — reported as an ERROR on purpose"
  exit 1
fi

mf ms21 "${RESULT:-ok}" "$W_CODE" "$W_BYTES" "$N" "$W_MS" "$STARTED" "$LOOKUP" \
   "lookup table, not a feed — no data/feeds.json row by design; $NOTE"
echo "== ms21: $N public-body project(s) in $LOOKUP  (${RESULT:-ok})"
exit 0
