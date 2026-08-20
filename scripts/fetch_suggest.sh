#!/usr/bin/env bash
# fetch_suggest.sh — Google Suggest pain-miner (CZ). No auth.
# Ported from the demand-signals project (src/ingesters/google_suggest.py):
# feed pain-phrased prefixes, record the autocompletions — live consumer
# search pain the institutional demand sources (NKÚ, ombudsman, ČOI) can't see.
# Rate care: ~1 req/1.5s (the endpoint tolerates ~50/min).
# HARD CAP: <=1 run/day. 144 queries/run (24 seeds x 6 patterns) — the cap IS
# the ban mitigation (blockers register row 8).
# Usage: scripts/fetch_suggest.sh [outdir]         <-- outdir is $1 (see §5.3)
set -uo pipefail   # no -e: one failed query must not kill the rest
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
OUT="$OUTDIR/suggest-pain.jsonl"
: > "$OUT"

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

# Register-adjacent CZ seeds (edit freely; keep the list boring and concrete).
SEEDS="datová schránka|stavební povolení|účetnictví|faktura|dotace|pojišťovna|banka|exekuce|energie|fotovoltaika|tepelné čerpadlo|e-shop|lékař|nemocnice|úřad|katastr|daňové přiznání|živnost|hypotéka|nájem|školka|důchod|recyklace|vodárna"

# Pain phrasings — the prefix IS the filter: complaints, failures, workarounds.
# (Lesson from demand-signals: pain language, never engagement metrics.)
PATTERNS="proč je %s tak|%s nefunguje|alternativa k %s|%s problém|jak zrušit %s|%s zkušenosti"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
ASKED=0; GOT=0; FAILED=0; TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; TMP="$OUT.resp"

# HERE-STRINGS, not `echo … | tr … | while`: a piped while runs in a SUBSHELL,
# so every counter below would reset to 0 when the loop ended. The pre-existing
# `n=$((n+1))` in this script was already dead for exactly that reason.
while IFS= read -r seed; do
  [ -n "${seed:-}" ] || continue
  while IFS= read -r pat; do
    [ -n "${pat:-}" ] || continue
    q="$(printf "$pat" "$seed")"
    enc="$(printf '%s' "$q" | jq -sRr @uri)"
    ASKED=$((ASKED+1))
    # -f: without it a 4xx body (a block page, a captcha) is captured into $resp
    # and fed to jq, which is the Mode-A "wrong body on a good transfer" failure.
    # ie=utf-8&oe=utf-8 is REQUIRED or the body is non-UTF-8 (blockers row 8).
    parse_w "$(curl -fsS -m 20 -o "$TMP" --remove-on-error \
                    -w '%{http_code} %{size_download} %{time_total}' \
                    "https://suggestqueries.google.com/complete/search?client=firefox&hl=cs&ie=utf-8&oe=utf-8&q=$enc" \
                    2>/dev/null || true)"
    LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))
    if [ "$W_CODE" = "200" ] && [ -s "$TMP" ]; then
      TOT_BYTES=$((TOT_BYTES + W_BYTES))
      if jq -c --arg q "$q" --arg d "$TODAY" \
           '{query: $q, date: $d, completions: (.[1] // [])} | select(.completions | length > 0)' \
           < "$TMP" >> "$OUT" 2>/dev/null; then
        GOT=$((GOT+1))
      else
        FAILED=$((FAILED+1))
        echo "FAILED suggest (unparseable body): $q"
      fi
    else
      FAILED=$((FAILED+1))
      echo "FAILED suggest (HTTP $W_CODE): $q"
    fi
    sleep 1.5
  done <<EOF
$(printf '%s' "$PATTERNS" | tr '|' '\n')
EOF
done <<EOF
$(printf '%s' "$SEEDS" | tr '|' '\n')
EOF
rm -f "$TMP"

WITH="$(grep -c . "$OUT" | tr -d ' ')"
echo "OK  suggest-pain.jsonl ($WITH queries with completions, $ASKED asked, $FAILED failed)"

# ZERO completions on a clean transport is the yield=zero anomaly (§7.2 step 4),
# and it is what this feed has silently produced since inception (blockers row 9).
if [ "$FAILED" -gt 0 ] && [ "$GOT" -eq 0 ]; then
  mf suggest error "$LAST_CODE" "$TOT_BYTES" "$WITH" "$TOT_MS" "$STARTED" "$OUT" \
     "all $ASKED queries failed"
elif [ "$FAILED" -gt 0 ]; then
  mf suggest ok "$LAST_CODE" "$TOT_BYTES" "$WITH" "$TOT_MS" "$STARTED" "$OUT" \
     "partial: $FAILED of $ASKED queries failed"
else
  mf suggest ok "$LAST_CODE" "$TOT_BYTES" "$WITH" "$TOT_MS" "$STARTED" "$OUT" ""
fi
