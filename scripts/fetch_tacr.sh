#!/usr/bin/env bash
# fetch_tacr.sh — TA ČR research needs (BETA2/BETA3 consultations) -> the asks ledger.
#
# ══ WHAT THIS FEED IS ════════════════════════════════════════════════════════
# A ministry states a research need; TA ČR posts a public consultation before
# it tenders the answer. That is an ASK — a named owner, a stated problem, no
# money attached yet (docs/superpowers/specs/2026-09-03-asks-ledger-design.md).
# One record per need code; posts without one (budget notices, outages) are
# dropped and counted.
#
# ══ THE TRANSPORT SHAPE, AND THE TRADEOFF ════════════════════════════════════
# PRIMARY = the two WordPress category feeds. Declared RSS 2.0, and
# content:encoded carries the FULL post body, so the resort sentence and the
# consultation date travel with the item. Limit: WordPress caps a feed at 10.
#
# BACKFILL = the two category HTML pages. Measured 2026-09-03: 5 posts a page,
# an excerpt instead of a body, no pagination (/page/2/ is 404). So — unlike
# nku, where the HTML half is the valuable half — this HTML can never carry
# MORE than the feed. It is here for the day the feed breaks; its failure
# degrades the run without failing it, and its rows lose the dedupe to the
# feed's fuller body.
#
# The need-code rule, both MODE-A guards and the fold live in
# scripts/tacr_extract.py so tacr_contract_selftest.py drives the SAME entry
# points (the nen_extract shape). Its header says why "TT-coded" is half right.
#
# Usage: scripts/fetch_tacr.sh [outdir]      <-- outdir is $1 (the nku shape)
set -uo pipefail   # no -e: one failed surface must not kill the rest
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
HERE="$(cd "$(dirname "$0")" && pwd)"
EXTRACT="$HERE/tacr_extract.py"

UA="localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# One appended row per REGISTRY FEED KEY per run; columns are the fetch-side
# half of the `fetch_log` schema (§2.3). Verbatim from fetch_nku.sh — the
# manifest is a cross-file contract, not a place for local taste.
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
parse_w() { # "<http_code> <size_download> <time_total> <content_type>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_CT="${4:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

command -v jq >/dev/null 2>&1 || { echo "fetch_tacr: jq is required" >&2; exit 2; }
[ -f "$EXTRACT" ] || { echo "fetch_tacr: $EXTRACT missing" >&2; exit 2; }

RSS_URLS="${TACR_RSS_URLS:-https://tacr.gov.cz/kategorie/beta3/feed/ https://tacr.gov.cz/kategorie/beta2/feed/}"
HTML_URLS="${TACR_HTML_URLS:-https://tacr.gov.cz/kategorie/beta3/ https://tacr.gov.cz/kategorie/beta2/}"
# Empty = tacr_extract.py's default (TI and TT codes). Set to narrow, e.g.
# TACR_NEED_RE='\bTT[A-Z]{2,8}\d{3,4}\b' for BETA3 only.
TACR_NEED_RE="${TACR_NEED_RE:-}"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
OUT="$OUTDIR/tacr-needs.jsonl"
# RAW originals live under .fetch/ — NOT in the outdir root. normalize.py groups
# every file carrying the `tacr` token into ONE feed and parses them all with
# the same contract, so .xml/.html beside the .jsonl would be a parse violation.
RAWD="$OUTDIR/.fetch/tacr"; mkdir -p "$RAWD"

TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""
RSS_ITEMS=0; HTML_ITEMS=0; RSS_FILES=""; HTML_FILES=""
TMPD="${TMPDIR:-/tmp}/tacr.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT

cat_of() { printf '%s' "$1" | sed -e 's#/feed/*$##' -e 's#/*$##' -e 's#.*/##'; }  # …/beta3/feed/ -> beta3

fetch() { # url raw_path -> W_*; true only on HTTP 200
  # -f: a non-2xx must not be stored as if it were a page. The explicit 200
  # test is NOT redundant with -f: --fail only trips at HTTP >= 400.
  parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                  -A "$UA" -o "$2" \
                  -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                  "$1" 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))
  [ "$W_CODE" = "200" ]
}

# ── 1. PRIMARY: the two category feeds ───────────────────────────────────────
for url in $RSS_URLS; do
  cat="$(cat_of "$url")"; raw="$RAWD/tacr-$cat-rss.xml"
  if ! fetch "$url" "$raw"; then
    echo "FAILED rss $cat (HTTP $W_CODE)"; ERRS="$ERRS rss-$cat:HTTP-$W_CODE"; continue
  fi
  # ── MODE-A GUARD ── a login page or a maintenance notice arrives as a 200
  # too; stored as a feed it would read as a healthy empty one. The guard
  # wants XML, an <rss><channel> whose <link> is a tacr.gov.cz BETA category,
  # and at least one <item>. The refused body stays under .fetch/ as evidence.
  if ! n="$(python3 "$EXTRACT" guard rss "$raw" 2>&1)"; then
    echo "FAILED rss $cat — MODE-A: $n"
    echo "       first 120 bytes: $(head -c 120 "$raw" | tr -d '\n')"
    ERRS="$ERRS rss-$cat:mode-a"; continue
  fi
  TOT_BYTES=$((TOT_BYTES + W_BYTES)); RSS_ITEMS=$((RSS_ITEMS + n)); RSS_FILES="$RSS_FILES $raw"
  echo "OK  rss $cat: $n posts ($W_BYTES bytes)"
done

# ── 2. BACKFILL: the two category listings ───────────────────────────────────
for url in $HTML_URLS; do
  cat="$(cat_of "$url")"; raw="$RAWD/tacr-$cat-list.html"
  if ! fetch "$url" "$raw"; then
    echo "FAILED html $cat (HTTP $W_CODE)"; ERRS="$ERRS html-$cat:HTTP-$W_CODE"; continue
  fi
  # MODE-A: the page must be the posts loop (div.posts__item with a title in
  # it), not a 200-status error document or an empty category.
  if ! n="$(python3 "$EXTRACT" guard html "$raw" 2>&1)"; then
    echo "FAILED html $cat — MODE-A: $n"
    echo "       first 120 bytes: $(head -c 120 "$raw" | tr -d '\n')"
    ERRS="$ERRS html-$cat:mode-a"; continue
  fi
  TOT_BYTES=$((TOT_BYTES + W_BYTES)); HTML_ITEMS=$((HTML_ITEMS + n)); HTML_FILES="$HTML_FILES $raw"
  echo "OK  html $cat: $n posts ($W_BYTES bytes)"
done

# ── 3. MECHANICAL EXTRACTION -> one JSONL payload ────────────────────────────
# Both surfaces fold into one row shape, deduped on the need code (the only
# stable key: a cancelled consultation is re-posted under the same slug with a
# new title). Only bodies that passed their guard are handed over.
N=0; DROPPED=0
if [ -n "$RSS_FILES$HTML_FILES" ]; then
  # The file lists are space-separated on purpose: bash 3.2 has no arrays, and
  # the paths are ours (under OUTDIR/.fetch/tacr/, no spaces).
  # shellcheck disable=SC2086
  if summary="$(python3 "$EXTRACT" fold --out "$TMPD/rows.jsonl" \
                  --rss $RSS_FILES --html $HTML_FILES --need-re "$TACR_NEED_RE" 2>&1)"; then
    jf() { printf '%s' "$summary" | jq -r "$1"; }
    N="$(jf .needs)"; DROPPED="$(jf .dropped)"
    echo "    extracted: rss $(jf .rss_seen) + html $(jf .html_seen) posts -> $(jf .candidates) need-coded," \
         "$N unique after dedupe on need_id; $DROPPED non-need post(s) dropped"
    jf '.dropped_titles[] | "      dropped: " + .'
  else
    echo "    extract failed: $summary"; ERRS="$ERRS extract:python-failed"
  fi
fi
case "$N" in ''|*[!0-9]*) N=0 ;; esac
if [ "$N" -gt 0 ]; then
  mv "$TMPD/rows.jsonl" "$OUT"
  echo "    by iface: $(jq -r '.iface' "$OUT" | sort | uniq -c | tr '\n' ' ')"
fi

# ── ITEMS FETCHED vs ITEMS KEPT — a zero-yield run must be LOUD ──────────────
echo "== tacr: rss $RSS_ITEMS post(s) + html $HTML_ITEMS post(s) -> $N unique need(s); $DROPPED non-need post(s) dropped"
if [ "$N" -eq 0 ]; then
  # No expected-absence branch: neither surface is calendar-keyed, so a 404
  # here is a failure, never an absence. Bytes that arrived and yielded nothing
  # is the yield=zero anomaly — an error, so the feed cannot read LIVE while
  # landing nothing.
  mf tacr error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "yield: zero records extracted${ERRS:+ —$ERRS}"
  exit 1
elif [ -n "$ERRS" ]; then
  mf tacr ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS"
else
  mf tacr ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "    wrote $OUT"
exit 0
