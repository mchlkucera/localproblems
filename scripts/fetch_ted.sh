#!/usr/bin/env bash
# fetch_ted.sh — TED Search API v3, no auth. CZ place of performance.
# Usage: scripts/fetch_ted.sh [YYYYMMDD-since] [outdir]
#   ARGV SHAPE: $1 = SINCE, $2 = outdir.  This script and fetch_hlidac.sh are
#   the TWO that take outdir as $2; the other four take it as $1 (§5.3).
# Writes ted-all.json into outdir (default data/raw/<today>/) — one all-CPV
# jurisdiction firehose; per-group files only under a TED_CPV_GROUPS backfill.
set -euo pipefail
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

SINCE="${1:-$(date -v-60d +%Y%m%d 2>/dev/null || date -d '60 days ago' +%Y%m%d)}"
TODAY="$(date +%Y-%m-%d)"
OUTDIR="${2:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

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

API="https://api.ted.europa.eu/v3/notices/search"

# ── THE WINNER FIELDS ── added 2026-08-21 ────────────────────────────────────
# 55% of what this fetcher already downloads is an AWARD notice naming the
# company that won (measured: 1,480 of 2,678 notices in data/raw/2026-08-20/
# carry `form-type: result`), and none of it reached data/raw/ because the
# FIELDS list never asked for a winner. `entity_ico` was populated on 0 of
# 3,200 committed TED signals as a direct result.
#
# THE TRAP THIS LIST IS BUILT AROUND: the TED v3 API SILENTLY DROPS an unknown
# field name from `fields` rather than erroring, so a typo returns a notice with
# the key simply absent — indistinguishable from "this notice has no winner".
# Every name below was therefore validated through the QUERY parser instead,
# which DOES reject unknowns:
#     POST /v3/notices/search  {"query": "(<field> = \"ZZQQXX\")"}
#       unknown name -> HTTP 400 "Unknown search field '<field>' found in
#                       expert query"
#       real name    -> HTTP 200 (0 hits), or a 400 naming a VALUE/pattern
#                       problem, which also proves the FIELD exists
# Measured verdicts: winner-name, winner-identifier, winner-country, winner-size,
# winner-decision-date, organisation-name-tenderer, organisation-identifier-
# tenderer, organisation-name-buyer, organisation-identifier-buyer are all REAL;
# organisation-identifier, tenderer-name, contractor-name, winner-national-id,
# winner-ico are NOT (all four spellings a reasonable person would try first).
#
# WHY BOTH THE `winner-*` AND THE `*-tenderer` PAIR. They carry the same ids
# (identical arrays on 299 of 300 sampled notices) but only the tenderer pair
# can be zipped: over 300 CZ result notices the `winner-name`/`winner-identifier`
# array LENGTHS disagreed on 51 (17%) — winner-name repeats a name per lot and
# winner-identifier does not — so pairing them by position attaches one
# company's name to another company's IČO. normalize.py's ted_parties() prefers
# the tenderer pair and treats `winner-*` as the fallback; both are fetched so
# that decision is reviewable from the payload instead of being baked in here.
FIELDS='["publication-number","publication-date","notice-title","buyer-name","buyer-city","classification-cpv","notice-type","form-type","contract-nature","estimated-value-lot","estimated-value-cur-lot","estimated-value-glo","estimated-value-cur-glo","total-value","total-value-cur","deadline-receipt-tender-date-lot","winner-name","winner-identifier","winner-country","winner-decision-date","organisation-name-tenderer","organisation-identifier-tenderer","organisation-name-buyer","organisation-identifier-buyer"]'

# ── THE FIREHOSE ── selection law, owner mandate 2026-08-24 ──────────────────
# A fetch script selects only by a UNIFORM NUMERIC THRESHOLD and/or a complete
# taxonomy — NEVER by invented keywords or a hand-picked category subset. The
# five CPV groups that stood here (it/health/bizserv/energy/construction) were
# a judgment call wearing a taxonomy's clothes: CPV itself is complete, but
# picking five branches of it is exactly the keyword mistake, and it was
# MEASURED to cost most of the corpus — probed 2026-08-24, a 30-day CZ window
# returns ~4,754 notices with NO classification-cpv clause vs 1,208 under the
# old 5-group subset, i.e. the subset silently discarded ~75% of the
# jurisdiction. The jurisdiction (place-of-performance CZE) IS the complete
# taxonomy this feed selects by; CPV codes stay in FIELDS below as free labels
# on each notice, and `sector` is filled by the model half (`_needs`).
#
# The default is therefore ONE group, `all`, carrying no CPV list and hence no
# classification-cpv clause. TED_CPV_GROUPS survives as the attended-backfill
# override (added mid-flight by a concurrent backfill run and preserved):
# setting it, e.g. TED_CPV_GROUPS="health:85*" scripts/fetch_ted.sh 20251101
# data/raw/<d>, restores the old "key:cpv-list" grouped behaviour for that one
# run — a deliberate narrowing for a scoped backfill, never the daily default
# (fetch_all.sh never sets it). Same pairs, newline-separated.
CPV_GROUPS="${TED_CPV_GROUPS:-all}"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TOT_ITEMS=0; TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""

# HERE-STRING, not `echo … | while`: a piped while runs in a SUBSHELL, so the
# totals accumulated below would be discarded when the loop ended and the
# manifest row would always read 0 items. bash 3.2 has no `mapfile`; a
# here-string keeps the loop in the current shell and needs no array.
while IFS=: read -r key cpv; do
  [ -n "${key:-}" ] || continue
  out="$OUTDIR/ted-$key.json"
  # The classification-cpv clause exists ONLY under a TED_CPV_GROUPS backfill
  # override. The default `all` group carries no cpv list, so the query is the
  # bare jurisdiction window — the whole point of the firehose.
  q="(place-of-performance IN (CZE)) AND (publication-date >= $SINCE)"
  if [ -n "${cpv:-}" ]; then q="$q AND (classification-cpv IN ($cpv))"; fi
  echo "== $key${cpv:+ (CPV $cpv)} since $SINCE"
  page=1
  : > "$out.tmp"
  while :; do
    # THE REQUEST BODY IS BUILT INTO A VARIABLE FIRST — DO NOT INLINE IT.
    # A multi-line `-d "{ … , … }"` written directly inside a command
    # substitution that is itself double-quoted (`parse_w "$( curl … )"`) gets
    # BRACE-EXPANDED: bash splits `{a,b,c,d}` at the top-level commas, strips the
    # braces, and runs curl once per fragment. Measured on this exact script:
    # four curl calls per page, each with a syntactically invalid body -> HTTP
    # 400, silently, on 49.4% of the corpus. The old `resp=$(curl …)` form did
    # NOT have this bug (an assignment does not word-split), so the quoting the
    # receipt plumbing needs is precisely what introduces it. A single-line
    # variable has no braces to expand and no line continuations to mis-parse.
    body="{\"query\": \"$q\", \"fields\": $FIELDS, \"limit\": 250, \"page\": $page}"
    # -f: a non-2xx from TED must NOT be stored as if it were a notice page.
    # The explicit `code = 200` test below is NOT redundant with -f: --fail only
    # trips at HTTP >= 400, so a 3xx served as the terminal response passes -f.
    # --retry covers TED's 429s, which fire readily across five CPV groups.
    parse_w "$(curl -fsS -m 60 --retry 3 --retry-delay 5 -X POST "$API" \
                    -H "Content-Type: application/json" \
                    -d "$body" \
                    -o "$out.page" --remove-on-error \
                    -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
    LAST_CODE="$W_CODE"
    TOT_MS=$((TOT_MS + W_MS))
    if [ "$W_CODE" != "200" ]; then
      echo "   page $page: FAILED (HTTP $W_CODE)"
      ERRS="$ERRS $key:HTTP-$W_CODE"
      break
    fi
    TOT_BYTES=$((TOT_BYTES + W_BYTES))
    n=$(python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d.get('notices',[])))" < "$out.page" 2>/dev/null || echo 0)
    total=$(python3 -c "import json,sys; print(json.load(sys.stdin).get('totalNoticeCount',0))" < "$out.page" 2>/dev/null || echo 0)
    cat "$out.page" >> "$out.tmp"
    printf '\n' >> "$out.tmp"
    echo "   page $page: $n notices (total $total)"
    [ "$n" -lt 250 ] && break
    page=$((page+1))
    [ "$page" -gt 60 ] && break   # safety: 60 x 250 = 15,000 notices, ~3x the
                                  # measured 30-day all-CPV volume (4,754)
  done
  rm -f "$out.page"
  # merge pages into one array
  got=$(python3 - "$out.tmp" "$out" <<'PY'
import json, sys
notices = []
for line in open(sys.argv[1]):
    line = line.strip()
    if not line: continue
    try: notices += json.loads(line).get('notices', [])
    except json.JSONDecodeError: pass
json.dump({"fetched": len(notices), "notices": notices}, open(sys.argv[2], 'w'), ensure_ascii=False)
print(len(notices))
PY
)
  echo "   -> $out: $got notices"
  TOT_ITEMS=$((TOT_ITEMS + got))
  rm -f "$out.tmp"
  sleep 2   # TED rate-limits consecutive queries (observed 429); one query in
            # the default run, several only under a TED_CPV_GROUPS backfill
done <<EOF
$CPV_GROUPS
EOF

# ONE row for the registry key `ted`. The default run is one `all` group and
# one ted-all.json; a TED_CPV_GROUPS backfill fans out into per-group files,
# which normalize.py maps back to `ted` by filename token either way.
if [ -n "$ERRS" ]; then
  mf ted error "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" "query failures:$ERRS"
else
  mf ted ok "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "== ted: $TOT_ITEMS notices, $TOT_BYTES bytes"
