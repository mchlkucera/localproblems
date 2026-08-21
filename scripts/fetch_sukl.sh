#!/usr/bin/env bash
# fetch_sukl.sh — SÚKL medicine supply-interruption register, open data, no auth.
#
# Usage: scripts/fetch_sukl.sh [outdir]
#   ARGV SHAPE: $1 = outdir. NO since-date — this source is a full snapshot, not
#   a window, so there is nothing for a since-date to mean. That puts it in the
#   feeds/suggest/reddit/nku family ($1 = outdir), NOT the ted/hlidac family
#   ($1 = SINCE, $2 = outdir). Stated because fetch_all.sh refuses a key with no
#   declared argv shape, and because a dispatcher that guesses is exactly how
#   TED once got a directory path as its since-date (§5.3).
#
# ONE URL, NO AUTH, NO PAGINATION. There is no richer interface to prefer here —
# this IS the declared one. Measured 2026-08-21: 200, 1,615,438 bytes,
# ETag "18a64e-65982336cc958", Last-Modified Thu 20 Aug 2026 22:40:03 GMT, which
# is exactly 24h01s after the value the 2026-08-20 probe saw. The refresh is a
# nightly 22:40 UTC job, so on all but one window a day the correct answer to a
# conditional GET is 304 — and this script asks for one.
#
# The decode (CP1250), the delimiter (`;`), the date format (`22.03.2019`) and
# the aggregation grain all live in scripts/sukl_extract.py, next to the bytes
# and next to the measurements that justify them. Read that file before changing
# anything here.
set -euo pipefail
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

URL="https://opendata.sukl.cz/soubory/MR/mr.zip"

# Survives the 28-day prune for the same reason as fetch_nen.sh's cache:
# ingest.sh only prunes directories whose NAME IS AN ISO DATE
# (scripts/ingest.sh:75-79), and `data/raw/*` gitignores this one.
CACHE="${SUKL_CACHE:-data/raw/.cache/sukl}"
mkdir -p "$CACHE"
ETAG="$CACHE/mr.zip.etag"

# ── run manifest ── same schema as scripts/fetch_ted.sh, deliberately verbatim ──
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

  # The MACHINE seam — see the long note in scripts/fetch_ted.sh. Field names are
  # db.py's FETCHLOG_FIELDS verbatim so a merge needs no translation, and the
  # subdirectory keeps it invisible to normalize.py's payload scan, which keeps
  # only os.path.isfile entries at the top level.
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

parse_w() { # "<http_code> <size_download> <time_total>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
mkdir -p "$OUTDIR/.fetch"
TMPZIP="$OUTDIR/.fetch/mr.zip"

echo "== sukl ($URL)"
# -f so a non-2xx is never stored as if it were data; --remove-on-error deletes
# the partial. The explicit code tests below are NOT redundant with -f: --fail
# only trips at >= 400, and 304 — the response we most expect — is a 3xx.
ETAGNEW="$OUTDIR/.fetch/mr.zip.etag.new"
parse_w "$(curl -fsS -m 300 --retry 3 --retry-delay 5 -L "$URL" \
                --etag-compare "$ETAG" --etag-save "$ETAGNEW" \
                -o "$TMPZIP" --remove-on-error \
                -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"

# --etag-save WRITES TO A TEMP PATH AND IS PROMOTED ONLY WHEN NON-EMPTY.
# MEASURED 2026-08-21: opendata.sukl.cz's 304 response DOES carry
# `ETag: "18a64e-65982336cc958"`, and curl 8.7.1 TRUNCATES the --etag-save file
# to 0 bytes anyway. Pointed straight at the durable cache entry, the first 304
# destroys the ETag that produced it, and every run after that re-downloads the
# whole file while still looking like a conditional GET. It is a curl behaviour,
# not a server one, so the same guard is in fetch_coi.sh and fetch_nen.sh.
if [ -s "$ETAGNEW" ]; then mv "$ETAGNEW" "$ETAG"; else rm -f "$ETAGNEW"; fi

OUT="$OUTDIR/sukl-unknown.json"

if [ "$W_CODE" = "304" ]; then
  # EXPECTED ABSENCE (§7.2 step 0), and here it is the NORMAL case rather than
  # an edge: the file is rewritten once a night at 22:40 UTC, so most runs in a
  # day legitimately have nothing new. `skipped` logs ok=1 with parse_method
  # 'none', does not increment consecutive_failures and does not move the feed
  # toward BROKEN — which is the whole reason that state exists. Calling it an
  # error instead would put this feed in a permanent alarm nobody reads, and
  # then the one real outage would be invisible too.
  rm -f "$TMPZIP"
  mf sukl skipped 304 0 0 "$W_MS" "$STARTED" "$OUTDIR" \
     "304 Not Modified — payload byte-identical to the last run (source refreshes ~22:40 UTC)"
  echo "== sukl: SKIPPED — 304 Not Modified, nothing new since the last run"
  exit 0
fi

if [ "$W_CODE" != "200" ]; then
  rm -f "$TMPZIP"
  mf sukl error "$W_CODE" "$W_BYTES" 0 "$W_MS" "$STARTED" "$OUTDIR" \
     "transport: HTTP $W_CODE from $URL"
  echo "== sukl: FAILED (HTTP $W_CODE)"
  exit 1
fi

# ── MODE A — THE SOURCE CONTRACT, BEFORE ANYTHING IS STORED ──────────────────
# A 200 proves the transfer, not the body. sukl_extract.py asserts ZIP magic, the
# presence of mr_hlaseni.csv, a clean CP1250 decode, all thirteen declared column
# names, >= 50,000 rows, a closed TYP_OZNAMENI vocabulary, and at least one
# `preruseni` notice. The column check is the one that catches a login page: an
# HTML body decodes fine and "parses" as a one-column CSV, so only the column
# NAMES can tell data from a page that merely looks like a successful fetch.
#
# Checked here rather than only in the registry contract because normalize.py
# evaluates that a session later, by which time the wrong body is already on disk
# and already counted as a successful fetch.
if ! READ_JSON="$(python3 scripts/sukl_extract.py read "$TMPZIP" "$OUTDIR/sukl.tmp.json" 2>&1)"; then
  rm -f "$TMPZIP" "$OUTDIR/sukl.tmp.json"
  # Drop the cached ETag: we hold no good bytes for it, so the next run must
  # re-request in full rather than take a 304 against a body we rejected.
  rm -f "$ETAG"
  mf sukl error 200 "$W_BYTES" 0 "$W_MS" "$STARTED" "$OUTDIR" \
     "CONTRACT VIOLATION (200 carrying the wrong body): $READ_JSON"
  echo "== sukl: CONTRACT VIOLATION — $READ_JSON"
  exit 1
fi
rm -f "$TMPZIP"

VALIDITY="$(printf '%s' "$READ_JSON" | python3 -c 'import json,sys; print(json.loads(sys.stdin.read()).get("validity",""))' 2>/dev/null || echo "")"
N_ROWS="$(printf '%s' "$READ_JSON"  | python3 -c 'import json,sys; print(json.loads(sys.stdin.read()).get("rows_in_file",0))' 2>/dev/null || echo 0)"
N_ITEMS="$(printf '%s' "$READ_JSON" | python3 -c 'import json,sys; print(json.loads(sys.stdin.read()).get("fetched",0))' 2>/dev/null || echo 0)"

# The filename carries the dataset's OWN validity date, not our clock. The
# aggregates are statements about a specific edition of the file, and a run that
# re-reads yesterday's edition after midnight would otherwise name it today.
# THE `sukl` TOKEN IN THE NAME IS ALSO A CROSS-FILE CONTRACT: normalize.py maps
# a payload back to a registry feed key by matching a distinctive token anywhere
# in the filename (FILE_FEED_TOKENS, normalize.py:97). Rename this output and the
# records silently reassign to another feed's contract.
OUT="$OUTDIR/sukl-${VALIDITY:-$TODAY}.json"
mv "$OUTDIR/sukl.tmp.json" "$OUT"

# ── MODE B — SILENT ABSENCE, MADE LOUD AT THE SOURCE ────────────────────────
# A fetch that works while zero records reach the ledger is a named failure in
# this repo (`SCRIPTED-SILENT`), and it is invisible from here unless the fetcher
# says so: the transport was fine, the contract passed, the manifest would read
# ok. Reported as an ERROR rather than a warning, because an `ok` row with
# items=0 is exactly the shape that gets skimmed past.
if [ "${N_ITEMS:-0}" -eq 0 ]; then
  mf sukl error 200 "$W_BYTES" 0 "$W_MS" "$STARTED" "$OUTDIR" \
     "ZERO-YIELD: contract passed over $N_ROWS rows and aggregation produced 0 items — \
aggregation is broken; a clean fetch with no items is SCRIPTED-SILENT"
  echo "== sukl: ZERO YIELD over $N_ROWS rows — reported as an ERROR on purpose"
  exit 1
fi

mf sukl ok 200 "$W_BYTES" "$N_ITEMS" "$W_MS" "$STARTED" "$OUTDIR" \
   "validity=$VALIDITY rows_in_file=$N_ROWS aggregates=$N_ITEMS"
echo "== sukl: $N_ITEMS aggregates from $N_ROWS notice rows (validity $VALIDITY), $W_BYTES bytes"
echo "   -> $OUT"
