#!/usr/bin/env bash
# fetch_coi.sh — Česká obchodní inspekce enforcement open data, no auth.
#
# Usage: scripts/fetch_coi.sh [YYYY-MM-DD-since] [outdir]
#   ARGV SHAPE: $1 = SINCE (ISO date), $2 = outdir.
#   That is the ted/hlidac shape ($1 SINCE, $2 outdir), NOT the
#   feeds/suggest/reddit/nku shape ($1 outdir). Stated because fetch_all.sh
#   REFUSES a key with no declared argv shape, and because a dispatcher that
#   guesses hands this script a directory path as its since-date and gets a
#   silently wrong window back (§5.3).
#   SINCE selects which completed half-years are emitted — it never changes what
#   is downloaded, because the source is one cumulative file per dataset.
#
# WHAT THIS READS AND WHY IT IS THE LEAST-FRAGILE SHAPE AVAILABLE:
# two plain CSVs at fixed URLs, quarterly-updated, cumulative back to
# 2015-01-01, both serving ETag and Last-Modified. The full measurement — row
# counts, column names, encodings, refresh dates — is at the top of
# scripts/coi_extract.py. `docs/feeds-status.md` calls this source an "HTML
# scrape … annual PDF"; it is neither, and that description is what kept a
# structured 12-year dataset out of the registry.
set -euo pipefail
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

SINCE="${1:-$(date -v-18m +%Y-%m-%d 2>/dev/null || date -d '18 months ago' +%Y-%m-%d)}"
TODAY="$(date +%Y-%m-%d)"
OUTDIR="${2:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

BASE="https://coi.gov.cz/userdata/files/dokumenty-ke-stazeni/open-data"
# A descriptive, contactable User-Agent. Not a disguise: coi.gov.cz answers 200
# to this, so there is nothing to work around, and a source that can see who is
# calling can ask us to stop.
UA="localproblems-register/1.0 (+https://localproblems.org)"

# THE CACHE HOLDS THE BODIES, NOT JUST THE ETAGS, and that is the difference
# between a conditional GET that helps and one that is decorative. This feed
# needs BOTH files to compute anything: sankce.csv carries the fines,
# kontroly.csv carries the IČO and the region they attach to. If only one
# changed, a body-less cache would force a full re-download of the other
# (27 MB) to do the join. With bodies cached, a 304 costs nothing and the join
# still runs.
# `data/raw/.cache/` is gitignored by `data/raw/*` and survives ingest.sh's
# pruner, which only touches directories whose NAME IS AN ISO DATE
# (scripts/ingest.sh:75-79).
CACHE="${COI_CACHE:-data/raw/.cache/coi}"
mkdir -p "$CACHE"

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
  # db.py's FETCHLOG_FIELDS verbatim; the subdirectory keeps it invisible to
  # normalize.py's payload scan, which keeps only top-level isfile entries.
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
TOT_BYTES=0; TOT_MS=0; FRESH=0; CACHED=0; ERRS=""; NOTES=""
LAST_CODE=000; DATA_CODE=""

# HERE-STRING, not `echo … | while`: a piped while runs in a SUBSHELL and every
# counter set below would be discarded when the loop ends, leaving the manifest
# row permanently reading 0. bash 3.2 has no `mapfile`.
while read -r name; do
  [ -n "${name:-}" ] || continue
  url="$BASE/$name.csv"
  etag="$CACHE/$name.etag"
  etagnew="$OUTDIR/.fetch/$name.etag.new"
  keep="$CACHE/$name.csv"
  tmp="$OUTDIR/.fetch/$name.csv.new"
  echo "== coi $name ($url)"

  # -o goes to a TEMP path, never straight to the cache. On a 304 curl writes an
  # empty body, and `-o "$keep"` would TRUNCATE the cached copy we are trying to
  # reuse — turning the optimisation into data loss on the very run it is
  # supposed to help. -f keeps a non-2xx from being stored as data;
  # --remove-on-error deletes the partial. The explicit code tests below are NOT
  # redundant with -f: --fail only trips at >= 400, and 304 is a 3xx.
  parse_w "$(curl -fsS -m 600 --retry 3 --retry-delay 5 -L -A "$UA" "$url" \
                  --etag-compare "$etag" --etag-save "$etagnew" \
                  -o "$tmp" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
  # --etag-save WRITES TO A TEMP PATH AND IS PROMOTED ONLY WHEN NON-EMPTY.
  # MEASURED 2026-08-21 against coi.gov.cz: the 304 response DOES carry
  # `ETag: "b988c8-6584d2662d000"`, and curl 8.7.1 TRUNCATES the --etag-save file
  # to 0 bytes anyway. Pointed straight at the durable cache entry, the first 304
  # therefore destroys the ETag that produced it, and every run after that
  # re-downloads all 40 MB while looking like it is using a conditional GET —
  # a self-disabling optimisation whose only symptom is a bandwidth bill.
  # This is a curl behaviour, not a server one, so it applies to every host.
  if [ -s "$etagnew" ]; then mv "$etagnew" "$etag"; else rm -f "$etagnew"; fi

  if [ "$W_CODE" = "200" ]; then
    mv "$tmp" "$keep"
    FRESH=$((FRESH + 1)); DATA_CODE="$W_CODE"
    echo "   200, $W_BYTES bytes -> cached"
  elif [ "$W_CODE" = "304" ]; then
    rm -f "$tmp"
    if [ -s "$keep" ]; then
      CACHED=$((CACHED + 1)); DATA_CODE="${DATA_CODE:-304}"
      NOTES="$NOTES $name:304"
      echo "   304 Not Modified — reusing the cached body"
    else
      # A 304 with no cached body is not a no-op, it is an inconsistency: the
      # ETag survived but the payload did not. Say so and force a full refetch
      # next run rather than silently proceeding with nothing.
      rm -f "$etag"
      ERRS="$ERRS $name:304-without-cached-body"
      echo "   304 but the cached body is GONE — dropped the ETag, will refetch"
    fi
  else
    rm -f "$tmp"
    ERRS="$ERRS $name:HTTP-$W_CODE"
    echo "   FAILED (HTTP $W_CODE)"
  fi
done <<EOF
sankce
kontroly
EOF

REPORT_CODE="${DATA_CODE:-$LAST_CODE}"

if [ -n "$ERRS" ]; then
  mf coi error "$REPORT_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "transport failures:$ERRS"
  echo "== coi: FAILED —$ERRS"
  exit 1
fi

# BOTH FILES UNCHANGED = EXPECTED ABSENCE, and this is the common case: the
# source is quarterly, so on most days the honest answer is "nothing new". A
# `skipped` row logs ok=1 with parse_method 'none', never increments
# consecutive_failures and never moves the feed toward BROKEN (§7.2 step 0). Any
# other treatment would put this feed in a permanent alarm nobody reads, and then
# the one real outage would be invisible too.
if [ "$FRESH" -eq 0 ]; then
  mf coi skipped "$REPORT_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "both datasets 304 Not Modified — quarterly source, nothing new since the last run:$NOTES"
  echo "== coi: SKIPPED — both datasets unchanged ($NOTES)"
  exit 0
fi

# ── MODE A — THE SOURCE CONTRACT, BEFORE ANYTHING IS STORED ──────────────────
# A 200 proves the transfer, not the body. coi_extract.py asserts: the body does
# not start with markup; it decodes as UTF-8-BOM; every declared column name is
# present; >= 100,000 sanction and >= 150,000 inspection rows; and the register
# still starts on 2015-01-01. The column check is the one that catches the
# WordPress error page these hosts serve — it is valid UTF-8 and "parses" as a
# one-column CSV, so only the column NAMES can tell data from a page.
#
# Checked here rather than only in the registry contract because normalize.py
# evaluates that a session later, by which time the wrong body is on disk and
# already counted as a successful fetch.
if ! READ_JSON="$(python3 scripts/coi_extract.py read \
                    "$CACHE/sankce.csv" "$CACHE/kontroly.csv" \
                    "$OUTDIR/coi.tmp.json" --since "$SINCE" 2>&1)"; then
  rm -f "$OUTDIR/coi.tmp.json"
  # We hold no good bytes for these ETags, so the next run must re-request in
  # full rather than take a 304 against a body we rejected.
  rm -f "$CACHE/sankce.etag" "$CACHE/kontroly.etag"
  mf coi error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "CONTRACT VIOLATION (200 carrying the wrong body): $READ_JSON"
  echo "== coi: CONTRACT VIOLATION — $READ_JSON"
  exit 1
fi

jqget() { printf '%s' "$READ_JSON" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('$1',''))" 2>/dev/null || echo ""; }
N_ITEMS="$(jqget fetched)"; COV="$(jqget coverage_end)"
S_ROWS="$(jqget sankce_rows)"; K_ROWS="$(jqget kontroly_rows)"
HELD="$(jqget held_back)"

# THE FILENAME IS A CROSS-FILE CONTRACT: normalize.py maps a payload back to a
# registry feed key by matching a distinctive token anywhere in the name
# (FILE_FEED_TOKENS, normalize.py:92). Rename this and the records silently
# reassign to another feed's contract — or, since no `coi` token exists there
# yet, fall through as an unmapped payload. Adding ("coi","coi") to that table is
# a required hand-off; see the note in scripts/coi_extract.py.
OUT="$OUTDIR/coi-${COV:-$TODAY}.json"
mv "$OUTDIR/coi.tmp.json" "$OUT"

# ── MODE B — SILENT ABSENCE, MADE LOUD AT THE SOURCE ────────────────────────
# `SCRIPTED-SILENT` is a named failure here: a fetcher that runs clean while zero
# records reach the ledger. It is invisible from this end unless the fetcher says
# so — the transport was fine, the contract passed, the manifest would read `ok`.
# Reported as an ERROR rather than a warning, because an `ok` row with items=0 is
# exactly the shape that gets skimmed past.
#
# A zero yield here has ONE benign explanation and the script distinguishes it:
# `held_back` means the quarterly refresh has not landed, so no half-year is
# provably complete and emitting nothing is correct.
if [ "${N_ITEMS:-0}" -eq 0 ]; then
  if [ -n "$HELD" ]; then
    mf coi skipped 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
       "no completed half-year to emit: $HELD"
    echo "== coi: SKIPPED — $HELD"
    exit 0
  fi
  mf coi error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "ZERO-YIELD: contract passed over $S_ROWS sanction rows (coverage to $COV) and \
aggregation produced 0 items for since=$SINCE — the window is wrong or aggregation is broken"
  echo "== coi: ZERO YIELD over $S_ROWS rows — reported as an ERROR on purpose"
  exit 1
fi

mf coi ok 200 "$TOT_BYTES" "$N_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" \
   "coverage_end=$COV sankce_rows=$S_ROWS kontroly_rows=$K_ROWS aggregates=$N_ITEMS fresh=$FRESH cached=$CACHED${NOTES:+ ;$NOTES}"
echo "== coi: $N_ITEMS aggregates from $S_ROWS fines / $K_ROWS inspections (coverage to $COV), $TOT_BYTES bytes"
echo "   -> $OUT"
