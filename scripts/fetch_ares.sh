#!/usr/bin/env bash
# fetch_ares.sh — ARES ekonomické subjekty, no auth. IČO -> legal identity.
#
# Usage: scripts/fetch_ares.sh <rawdir>
#   ARGV SHAPE: $1 = outdir. Takes no since-date: ARES is not a time series, it
#   is a lookup, and the thing it looks up is decided by the worklist below.
#
# MUST RUN AFTER scripts/fetch_mpsv.sh IN THE SAME <rawdir>. Not a convention —
# a data dependency: fetch_mpsv.sh writes <rawdir>/.fetch/ares-worklist.txt and
# this script has nothing to do without it. With no worklist it records `skipped`
# and exits 0, which is the correct reading of "MPSV had no employer candidate
# this month", not a failure.
#
# Reads:  <rawdir>/.fetch/ares-worklist.txt   (one IČO per line)
# Writes: <rawdir>/ares-lookups-<YYYY-MM>.json
#         and folds the resolved identities into <rawdir>/mpsv-hiring-<YYYY-MM>.json
#
# ── ROLE: ENRICHMENT, NOT A FEED ─────────────────────────────────────────────
# `data/feeds.json` gives ares `role: "enrichment"`, `evidence_type: null`,
# `id_prefixes: []`. It PRODUCES NO SIGNALS and must never be counted in the feed
# total (AC-F1 considers only role: feed). The payload it writes exists so the
# lookup has a receipt and a health row; normalize.py maps it to the `ares` key,
# finds no extractor and stages nothing. `expected_yield` on this feed counts
# LOOKUPS PERFORMED, not records.
#
# ── WHY THIS INTERFACE ───────────────────────────────────────────────────────
# `ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/<ico>` is a
# documented REST endpoint on the state register: no auth, no session, one
# subject per path segment, JSON out. Measured 2026-08-21: HTTP 200 in ~2.2 s,
# 5,091 bytes, carrying obchodniJmeno, pravniForma, datumVzniku, czNace and
# sidlo. The alternative — the ARES web UI at /ekonomicke-subjekty?ico= — is an
# HTML app and would have to be scraped. We took the declared interface.
#
# WHAT WE GAVE UP: the per-IČO route costs one request per subject, so it can
# only ever enrich a SHORTLIST. ARES also publishes bulk extracts (VREO/RES),
# which would resolve everything at once — that is the upgrade path if this
# register ever wants every IČO in the corpus resolved rather than the handful
# that reach a record. Not built, because a shortlist is what exists to resolve.
#
# ── THE MOD-11 CHECKSUM IS SPENT BEFORE THE REQUEST ─────────────────────────
# docs/architecture-v3.md §2.3/§13.0 make it MANDATORY. Applied here as an
# admission test rather than a post-hoc filter: a checksum-invalid IČO is not
# worth an HTTP request, and letting one through would mint a false entity key.
set -euo pipefail
export LC_NUMERIC=C

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

API="https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty"
WORKLIST="$OUTDIR/.fetch/ares-worklist.txt"
MAX_RECORDS="${ARES_MAX_RECORDS:-6}"

MANIFEST="$OUTDIR/manifest.md"
RUN_ID="${RUN_ID:-$(date -u +%Y-%m-%dT%H%M)}"
mf() { # feed_key result http bytes items ms started_at raw_path error
  if [ ! -f "$MANIFEST" ]; then
    { printf '# run manifest — %s\n\n' "$TODAY"
      printf 'Fetch-side rows consumed by `python3 scripts/db.py fetchlog %s`.\n' "$OUTDIR"
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

  # The MACHINE seam — real transport facts, recorded here because they do not
  # survive to normalize time. Same schema as every other fetcher in this repo.
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

if [ ! -s "$WORKLIST" ]; then
  echo "== ares: no worklist at $WORKLIST — nothing to resolve"
  mf ares skipped 000 0 0 0 "$STARTED" "$OUTDIR" \
     "no ares-worklist.txt (run scripts/fetch_mpsv.sh first, or MPSV had no employer candidate)"
  exit 0
fi

# The aggregate this run enriches. One per rawdir by construction.
AGG="$(ls "$OUTDIR"/mpsv-hiring-*.json 2>/dev/null | head -1 || true)"
if [ -z "$AGG" ]; then
  mf ares error 000 0 0 0 "$STARTED" "$OUTDIR" \
     "worklist present but no mpsv-hiring-*.json to fold into"
  exit 1
fi
MONTH="$(basename "$AGG" .json | sed 's/^mpsv-hiring-//')"
LOOKUPS="$OUTDIR/ares-lookups-$MONTH.json"

WORK="$(mktemp -d "${TMPDIR:-/tmp}/lp-ares-$MONTH-XXXXXX")"
cleanup() { [ -n "${WORK:-}" ] && [ -d "$WORK" ] && rm -rf "$WORK"; }
trap cleanup EXIT INT TERM

TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; OK_N=0; MISS_N=0; BAD_ICO=0; ERRS=""

# HERE-STRING, not a pipe: the counters must survive the loop (bash 3.2, no
# `mapfile`, and a piped `while` runs in a subshell).
while read -r ico; do
  ico="$(printf '%s' "$ico" | tr -d '[:space:]')"
  [ -n "$ico" ] || continue
  # THE CHECKSUM, BEFORE THE REQUEST. One implementation of mod-11 lives in
  # scripts/db.py; this calls it rather than transcribing it.
  if ! python3 -c "
import sys; sys.path.insert(0, '$HERE')
from db import valid_ico
sys.exit(0 if valid_ico('$ico') else 1)" 2>/dev/null; then
    echo "   $ico: FAILS the mod-11 checksum — not requested"
    BAD_ICO=$((BAD_ICO + 1))
    continue
  fi
  # -f keeps a 4xx/5xx body off disk; --remove-on-error deletes the partial; the
  # explicit code test catches the 3xx that -f lets through.
  parse_w "$(curl -fsSL -m 45 --retry 2 --retry-delay 3 "$API/$ico" \
                  -H 'Accept: application/json' \
                  -o "$WORK/$ico.json" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
  TOT_MS=$((TOT_MS + W_MS))
  if [ "$W_CODE" = "200" ]; then
    LAST_CODE=200
    TOT_BYTES=$((TOT_BYTES + W_BYTES))
    OK_N=$((OK_N + 1))
    echo "   $ico: 200 ($W_BYTES B)"
  elif [ "$W_CODE" = "404" ]; then
    # An IČO that is not in the register is a FACT ABOUT THAT IČO, not a feed
    # outage. Counted, never fatal — ares_fold.py drops the employer record.
    MISS_N=$((MISS_N + 1))
    echo "   $ico: 404 (not in the register)"
  else
    LAST_CODE="$W_CODE"
    ERRS="$ERRS $ico:HTTP-$W_CODE"
    echo "   $ico: FAILED (HTTP $W_CODE)"
  fi
  sleep 0.4   # a public register, resolved a handful at a time. Be a good guest.
done <<EOF
$(cat "$WORKLIST")
EOF

REQUESTED=$((OK_N + MISS_N + BAD_ICO))
if [ "$OK_N" -eq 0 ]; then
  # Every lookup failing is not "these companies do not exist" — it is the feed.
  mf ares error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "0 of $REQUESTED lookups resolved${ERRS:+; errors:$ERRS}"
  exit 1
fi

if python3 "$HERE/ares_fold.py" \
     --work "$WORK" --month "$MONTH" --lookups "$LOOKUPS" \
     --aggregate "$AGG" --max-records "$MAX_RECORDS"; then
  NAMED="$(python3 -c "
import json
print(json.load(open('$AGG')).get('ares', {}).get('employers_named', 0))" 2>/dev/null || echo 0)"
  # items_fetched counts LOOKUPS RESOLVED, which is what this row's
  # expected_yield is defined against. It is not a record count; ARES has none.
  mf ares ok "$LAST_CODE" "$TOT_BYTES" "$OK_N" "$TOT_MS" "$STARTED" "$LOOKUPS" \
     "resolved $OK_N of $REQUESTED (404 $MISS_N, bad-checksum $BAD_ICO); named $NAMED employer record(s)${ERRS:+; errors:$ERRS}"
  echo "== ares: $OK_N resolved -> $LOOKUPS; $NAMED employer record(s) named in $(basename "$AGG")"
else
  rc=$?
  if [ "$rc" = "2" ]; then
    mf ares error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
       "AC-GDPR1 REFUSED: contact data survived the ARES allowlist — nothing written"
  else
    mf ares error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
       "ares_fold.py exit $rc"
  fi
  exit 1
fi
