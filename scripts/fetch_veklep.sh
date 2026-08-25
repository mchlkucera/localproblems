#!/usr/bin/env bash
# fetch_veklep.sh — VeKLEP (Elektronická knihovna legislativního procesu) via
# the Hlídač státu dataset mirror. Every Czech legislative draft here carries a
# mandatory RIA whose first section is "Definice problému" — a state-authored
# problem statement. This script is MECHANICAL ONLY: it fetches recent items'
# METADATA + LINKS (window on datumPosledniUpravy, so new drafts AND stage
# changes both surface). The RIA PDFs hang off each item's `prilohy` and are
# read later by the model half / reg-scan — never fetched-and-judged here.
# Auth: the token NEVER transits this shell. See "SECRET HANDLING" below.
# Usage: scripts/fetch_veklep.sh [YYYY-MM-DD-since] [outdir]
#   ARGV SHAPE: $1 = SINCE, $2 = outdir — the ted/hlidac shape (§5.3).
set -euo pipefail
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

SINCE="${1:-$(date -v-70d +%Y-%m-%d 2>/dev/null || date -d '70 days ago' +%Y-%m-%d)}"
TODAY="$(date +%Y-%m-%d)"
OUTDIR="${2:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# One appended row per REGISTRY FEED KEY per run. These columns are the
# FETCH-SIDE half of the `fetch_log` schema (§2.3); `db.py fetchlog <dir>` reads
# this table and normalize.py fills items_kept / yield_anomaly / parse_method
# afterwards. Identical block to the sibling fetchers — see fetch_hlidac.sh for
# the column semantics; this copy exists because each fetcher must be runnable
# alone and still leave a receipt.
#   result=ok      -> fetch_log.ok = 1
#   result=skipped -> fetch_log.ok = 1, parse_method='none' (expected absence)
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
  # The true status code, byte count and transfer time exist ONLY here, at
  # fetch time. normalize.py reads this file (load_receipts) and records
  # `http_status: null` when a feed has no receipt rather than synthesizing
  # one. Field names are exactly db.py's FETCHLOG_FIELDS. Lives in a
  # subdirectory on purpose: normalize.py's payload scan keeps only
  # os.path.isfile entries, so a directory can never be mistaken for a payload.
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

# P_ITEMS is what LANDED ON DISK, P_TOTAL is what the API says exists.
# Keeping them apart is the fix fetch_hlidac.sh paid for — see its history.
parse_counts() { # "<results_len> <api_total>"
  set -- ${1:-}
  P_ITEMS="${1:-ERR}"; P_TOTAL="${2:-ERR}"
}

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# ── SECRET HANDLING ── coordinator ruling 2026-08-20, same as fetch_hlidac.sh ─
# The token NEVER transits this shell's environment: with-secrets decrypts the
# vault and execs ONE allow-listed curl; curl imports the value itself with
# --variable and interpolates it with --expand-header. DO NOT reintroduce
# `direnv exec .` (broken no-op) and DO NOT wrap this script wholesale
# (interpreters are refused by with-secrets' allowlist, by design).
# The full probe rationale — why the message is read, not the exit code, and
# why the bogus scheme never touches the network — lives in fetch_hlidac.sh;
# this is a verbatim clone of that measured mechanism, not a re-derivation.
token_present() { # NAME -> 0 only on POSITIVE EVIDENCE the vault holds it.
  probe_out="$(with-secrets -- curl -sS --variable "%$1" \
                 --expand-header "H: {{$1}}" 'lpnoscheme://x' 2>&1)"
  case "$probe_out" in
    *"variable expansion failure"*) return 1 ;;
    *"not supported"*)              return 0 ;;
    *) PROBE_BROKEN=1
       echo "== auth probe INCONCLUSIVE for \$$1: with-secrets never reached curl." >&2
       echo "   Not evidence of absence — the probe itself did not run." >&2
       return 1 ;;
  esac
}

TOKEN_VAR=""
PROBE_BROKEN=0
if command -v with-secrets >/dev/null 2>&1; then
  for cand in HLIDAC_TOKEN HLIDAC_STATU_TOKEN; do
    if token_present "$cand"; then TOKEN_VAR="$cand"; break; fi
  done
else
  PROBE_BROKEN=1
  echo "== with-secrets is not on PATH — no authenticated call is possible." >&2
fi

if [ -z "$TOKEN_VAR" ]; then
  if [ "$PROBE_BROKEN" -eq 1 ]; then
    mf veklep error 000 0 0 0 "$STARTED" "" \
       "auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent."
    echo "FAILED: could not probe the vault at all — token presence is UNKNOWN." >&2
  else
    mf veklep error 000 0 0 0 "$STARTED" "" \
       "no Hlidac token in the vault: HLIDAC_TOKEN and HLIDAC_STATU_TOKEN both fail curl variable expansion"
    echo "FAILED: neither HLIDAC_TOKEN nor HLIDAC_STATU_TOKEN is in the sops vault." >&2
    echo "        Free key at hlidacstatu.cz/api, then: sops-edit .env.enc" >&2
  fi
  exit 1
fi
echo "== auth: using \$$TOKEN_VAR via with-secrets (value never enters this shell)"

API="https://api.hlidacstatu.cz/api/v2/datasety/veklep/hledat"

# ── THE WINDOW ── one query, no keywords — the selection law of 2026-08-24 ───
# The dataset IS the complete taxonomy (every material in the government's
# legislative e-library, 8,708 records measured 2026-08-25), so the only
# selection is the date window: datumPosledniUpravy:[$SINCE TO *] catches new
# drafts and stage changes alike. MEASURED 2026-08-25: 80 items touched in the
# trailing 30 days; 27-36 NEW items/month by datumAutorizace (May 36, Jun 33,
# Jul 27). Paging is the Hlídač dataset default of 25/page (`strana`); the
# default 8 pages = 200 items covers the 70-day default window (~190 touched)
# with headroom. Raise VEKLEP_PAGES for a backfill.
QUERY="datumPosledniUpravy:[$SINCE TO *]"
PAGE_SIZE=25
PAGES="${VEKLEP_PAGES:-8}"

TOT_ITEMS=0; TOT_AVAIL=0; TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""
q_total=0; p=1

while [ "$p" -le "$PAGES" ]; do
  out="$OUTDIR/veklep-p$p.json"

  # -f stops a 4xx/5xx body being stored as a .json payload; the explicit
  # `code = 200` test below catches the 302-login-page shape -f cannot see.
  parse_w "$(with-secrets -- curl -fsSG -m 60 "$API" \
                  --data-urlencode "dotaz=$QUERY" \
                  --data-urlencode "strana=$p" \
                  --variable "%$TOKEN_VAR" \
                  --expand-header "Authorization: Token {{$TOKEN_VAR}}" \
                  -o "$out" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))

  if [ "$W_CODE" != "200" ]; then
    echo "== veklep p$p: FAILED (HTTP $W_CODE)"
    ERRS="$ERRS p$p:HTTP-$W_CODE"
    break
  fi
  TOT_BYTES=$((TOT_BYTES + W_BYTES))

  # ITEMS ON DISK first, api total second — reading `total` alone was the
  # fetch_hlidac.sh over-count bug, and this clone keeps its fix.
  parse_counts "$(python3 -c "import json,sys;d=json.load(sys.stdin);print(len(d.get('results') or []), d.get('total', -1))" < "$out" 2>/dev/null || true)"
  case "$P_ITEMS" in
    ''|*[!0-9]*) echo "== veklep p$p: unparseable payload"
                 ERRS="$ERRS p$p:unparseable"; break ;;
  esac
  case "$P_TOTAL" in ''|*[!0-9]*) : ;; *) q_total="$P_TOTAL" ;; esac
  TOT_ITEMS=$((TOT_ITEMS + P_ITEMS))
  echo "== veklep p$p: +$P_ITEMS on disk (api total $q_total) -> $out"

  # Stop on a short page or once the set is covered. WRITTEN AS `if`, NOT
  # `[ … ] && break` — under `set -e` a false one-line test is a non-zero
  # statement (the fetch_hlidac.sh lesson, kept).
  if [ "$P_ITEMS" -lt "$PAGE_SIZE" ]; then break; fi
  if [ "$q_total" -gt 0 ] && [ "$TOT_ITEMS" -ge "$q_total" ]; then break; fi
  p=$((p + 1))
  sleep 3   # free-tier rate limit
done

if [ "$q_total" -lt "$TOT_ITEMS" ]; then q_total="$TOT_ITEMS"; fi
TOT_AVAIL="$q_total"

# ONE row for the registry key `veklep`. A page cap that under-fetches is
# REPORTED on the row, never rounded away.
COVER=""
if [ "$TOT_AVAIL" -gt "$TOT_ITEMS" ]; then
  COVER="coverage: $TOT_ITEMS of $TOT_AVAIL available (page cap VEKLEP_PAGES=$PAGES x $PAGE_SIZE)"
fi
if [ -n "$ERRS" ]; then
  mf veklep error "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" "page failures:$ERRS${COVER:+ · $COVER}"
else
  mf veklep ok "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" "$COVER"
fi
echo "== veklep: $TOT_ITEMS materials on disk of $TOT_AVAIL available, $TOT_BYTES bytes"
