#!/usr/bin/env bash
# fetch_nku.sh — NKÚ Věstník: audit conclusions (kontrolní závěry). No auth.
# THE LLM-FALLBACK PROOF FEED (docs/architecture-v3.md §7.3): the HTML resists
# clean structured parsing, volume is ~2-6 items/month, and there was no prior
# fetcher, so nothing can regress. This script only FETCHES and receipts;
# extraction (structured-first, then llm-fallback) is normalize.py's half.
# Usage: scripts/fetch_nku.sh [outdir] [year ...]  <-- outdir is $1 (see §5.3)
set -uo pipefail   # no -e: one failed year must not kill the rest
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
shift 2>/dev/null || true
YEARS="${*:-$(date +%Y) $(( $(date +%Y) - 1 ))}"

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

# EXPECTED ABSENCE (§7.2 step 0). The registry's contract.allow_missing is the
# source of truth; fetch_all.sh reads it from data/feeds.json and exports it.
# A calendar-keyed URL for a period that simply does not exist is `skipped`:
# ok=1, parse_method=none, and it MUST NOT increment consecutive_failures.
ALLOW_MISSING="${ALLOW_MISSING:-0}"

# HOST: non-www, per blockers register row 12.
# HONEST RE-MEASUREMENT, 2026-08-20 — the doc's row 12 does NOT reproduce:
#   * it claims www.nku.cz "403s generic fetchers". Measured with curl's DEFAULT
#     UA: www -> 200, non-www -> 200, byte-identical (28,795). No 403 observed.
#   * it claims "uppercase 301s to http". Measured: /rka/VESTNIK.asp -> 200, no
#     redirect at all.
# Non-www is kept because it is what the doc mandates and it demonstrably works;
# the row's stated REASONS are unverified. Re-measure before relying on either.
# NKU_BASE is overridable ONLY so the expected-absence branch below can be
# exercised against a real 404 in testing; production never sets it.
BASE="${NKU_BASE:-https://nku.cz/scripts/rka/vestnik.asp?rok=}"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TOT_ITEMS=0; TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""; SKIPPED=0; FETCHED=0

for year in $YEARS; do
  case "$year" in ''|*[!0-9]*) continue ;; esac
  out="$OUTDIR/nku-vestnik-$year.html"
  # -f: a non-2xx must not be stored as if it were a Věstník page. The explicit
  # `code = 200` test is NOT redundant with -f: --fail only trips at HTTP >= 400.
  parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                  -A "$UA" -o "$out" \
                  -w '%{http_code} %{size_download} %{time_total}' "$BASE$year" 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))

  if [ "$W_CODE" = "404" ] && [ "$ALLOW_MISSING" = "1" ]; then
    echo "SKIP $year (HTTP 404, allow_missing) — expected absence, not a failure"
    SKIPPED=$((SKIPPED+1))
    continue
  fi
  if [ "$W_CODE" != "200" ]; then
    echo "FAILED $year (HTTP $W_CODE)"
    ERRS="$ERRS $year:HTTP-$W_CODE"
    continue
  fi

  # Item count at fetch time. MEASURED discriminator: audit conclusions are
  # linked as /assets/kon-zavery/<id>.pdf — 2026 -> 23, 2025 -> 29, and a year
  # that does not exist -> 0.
  #
  # THIS FEED CANNOT DEMONSTRATE EXPECTED ABSENCE, and pretending otherwise
  # would be the §7.1 Mode-A failure in our own tooling. Measured 2026-08-20:
  # ?rok=2027, ?rok=2099 and ?rok=1990 all return HTTP **200** with an 18,095-byte
  # empty shell — NKÚ never 404s on a missing calendar key. So the branch above
  # is dead code for THIS feed and exists for the MPSV-shaped feeds that do 404
  # (§13.7: 180 of 658 days genuinely missing). For NKÚ the real contract check
  # is the item count below: a 200 carrying zero items is the yield=zero anomaly.
  # `grep -o | wc -l`, NOT `grep -c`: -c counts matching LINES, and this page
  # ships the whole list on very few lines, so -c reported 1 where the real
  # count is 23. A silently-wrong item count is the yield check lying to itself.
  n=$(grep -oE '/assets/kon-zavery/[^"]+\.pdf' "$out" 2>/dev/null | wc -l | tr -d ' ')
  [ -n "$n" ] || n=0
  TOT_BYTES=$((TOT_BYTES + W_BYTES)); TOT_ITEMS=$((TOT_ITEMS + n)); FETCHED=$((FETCHED+1))
  echo "OK  $year: $n audit conclusions ($W_BYTES bytes) -> $out"
  if [ "$n" -eq 0 ]; then
    ERRS="$ERRS $year:zero-items-on-200"
  fi
done

if [ "$FETCHED" -eq 0 ] && [ "$SKIPPED" -gt 0 ]; then
  # Every requested period was an expected absence: ok=1, parse_method=none.
  mf nku skipped "$LAST_CODE" 0 0 "$TOT_MS" "$STARTED" "$OUTDIR" ""
elif [ -n "$ERRS" ]; then
  mf nku error "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" "year failures:$ERRS"
else
  mf nku ok "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "== nku: $TOT_ITEMS audit conclusions across $FETCHED year(s), $SKIPPED skipped"
