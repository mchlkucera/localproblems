#!/usr/bin/env bash
# fetch_hlidac.sh — Hlídač státu smlouvy API (registr smluv; catches sub-TED-threshold contracts).
# Auth: the token NEVER transits this shell. See "SECRET HANDLING" below.
# Usage: scripts/fetch_hlidac.sh [YYYY-MM-DD-since] [outdir]
#   ARGV SHAPE: $1 = SINCE, $2 = outdir.  This script and fetch_ted.sh are the
#   TWO that take outdir as $2; the other four take it as $1 (§5.3).
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

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# ── SECRET HANDLING ── coordinator ruling 2026-08-20 ─────────────────────────
# The token NEVER transits this shell's environment. `with-secrets` decrypts the
# vault and execs ONE allow-listed command; curl imports the value itself with
# --variable and interpolates it into the header with --expand-header, so no
# process we control ever holds it and it cannot be dumped from this script's
# env. Requires curl >= 8.3 for --variable/--expand-* (this box: 8.7.1).
#
# DO NOT reintroduce `direnv exec .`: the direnv -> sops export path is BROKEN.
# It prints "using sops .env.enc", exits clean, and exports nothing but DIRENV_*
# bookkeeping. That broken hook — not a missing key — is why this feed went
# quiet. Correspondingly, this script CANNOT be wrapped wholesale:
# `with-secrets bash fetch_hlidac.sh` is refused by design (an interpreter can
# encode a secret past the output scrubber), so only the curl calls are wrapped.
#
# Which name holds the token is MEASURED, not assumed. Probed 2026-08-20 with a
# negative control, presence only, no value ever printed:
#     HLIDAC_TOKEN        -> ABSENT
#     HLIDAC_STATU_TOKEN  -> PRESENT
# Both names are tried in that order, exactly as the pre-rewrite guard did.
# NOTE: architecture-v3.md blockers row 1 asserts BOTH names are "genuinely
# ABSENT — coordinator-verified". That is wrong for the second name; re-measure
# rather than trusting either this comment or the doc.
token_present() { # NAME -> 0 if the vault holds it. Never prints/stores the value.
  # 'lpnoscheme://' is an unsupported protocol ON PURPOSE: curl parses options
  # and expands variables BEFORE touching the network, so presence resolves with
  # ZERO transmission of the secret to anywhere.
  #   exit 2 = "variable expansion failure" = name not in the vault
  #   anything else = expansion succeeded (curl then rejected the bogus scheme)
  #
  # DELIBERATELY NO -f ON THIS ONE CURL, and it is the only such exemption in
  # scripts/. --fail governs how an HTTP RESPONSE is treated, and this call
  # never makes a request: the bogus scheme is rejected during option parsing.
  # There is no response to fail on, no body, and no -o, so -f cannot change
  # any outcome here. Every curl that actually fetches a payload carries -f.
  with-secrets -- curl -sS --variable "%$1" --expand-header "H: {{$1}}" \
                          'lpnoscheme://x' >/dev/null 2>&1
  [ "$?" -ne 2 ]
}

TOKEN_VAR=""
if command -v with-secrets >/dev/null 2>&1; then
  for cand in HLIDAC_TOKEN HLIDAC_STATU_TOKEN; do
    if token_present "$cand"; then TOKEN_VAR="$cand"; break; fi
  done
fi

if [ -z "$TOKEN_VAR" ]; then
  # This guard is the reason this feed fails LOUDLY instead of storing an
  # auth-error body (§7.1 receipt 4). It now also leaves a manifest row: a
  # blocked feed that writes no fetch_log row is invisible to db.py health,
  # which is exactly the Mode-B silence §7.5 exists to make visible.
  mf hlidac error 000 0 0 0 "$STARTED" "" \
     "no Hlidac token in the vault: HLIDAC_TOKEN and HLIDAC_STATU_TOKEN both fail curl variable expansion (blockers row 1)"
  echo "FAILED: neither HLIDAC_TOKEN nor HLIDAC_STATU_TOKEN is in the sops vault." >&2
  echo "        Free key at hlidacstatu.cz/api, then:" >&2
  echo "        sops edit --input-type dotenv --output-type dotenv .env.enc" >&2
  exit 1
fi
echo "== auth: using \$$TOKEN_VAR via with-secrets (value never enters this shell)"

API="https://api.hlidacstatu.cz/api/v2/smlouvy/hledat"

# bash 3.2 compatible: "key|query" pairs; date-range keeps results current
QUERIES='nis2|"kybernetická bezpečnost"
energycom|"komunitní energetika" OR "energetické společenství"
stavebni|"portál stavebníka" OR "stavební řízení"
ehealth|"nemocniční informační systém" OR ehealth
watermeter|"smart metering" OR "chytré vodoměry" OR vodoměrů
eudi|"digitální identita" OR edoklady
it-large|oblast:it AND cenaSDph:>10000000'

TOT_ITEMS=0; TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""

# HERE-STRING, not `echo … | while`: a piped while runs in a SUBSHELL and would
# discard every total accumulated below, leaving the manifest row reading 0.
while IFS='|' read -r key q; do
  [ -n "${key:-}" ] || continue
  full="($q) AND datumUzavreni:[$SINCE TO *]"
  out="$OUTDIR/hlidac-$key.json"

  # -f stops a 4xx/5xx body being stored as a .json payload.
  # THE `code = 200` TEST IS NOT REDUNDANT WITH -f, AND THIS FEED IS EXACTLY WHY:
  # §7.1 receipt 2 is a 302 LOGIN PAGE that was saved as a .json payload. curl's
  # --fail only trips at HTTP >= 400, so a 302 passes -f untouched. Without -L
  # the 302 is the terminal response, so only an explicit 200 assertion catches
  # it. -f alone would NOT have caught the Hlídač receipt.
  # with-secrets' scrubber is VERIFIED not to corrupt this: it filters stderr,
  # and curl's -w receipt arrives on stdout intact (measured: "200 18080 0.717520").
  parse_w "$(with-secrets -- curl -fsSG -m 60 "$API" \
                  --data-urlencode "dotaz=$full" \
                  --data-urlencode "razeni=0" \
                  --data-urlencode "strana=1" \
                  --variable "%$TOKEN_VAR" \
                  --expand-header "Authorization: Token {{$TOKEN_VAR}}" \
                  -o "$out" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))

  if [ "$W_CODE" != "200" ]; then
    echo "== $key: FAILED (HTTP $W_CODE)"
    ERRS="$ERRS $key:HTTP-$W_CODE"
  else
    TOT_BYTES=$((TOT_BYTES + W_BYTES))
    n=$(python3 -c "import json,sys;print(json.load(sys.stdin).get('total','ERR'))" < "$out" 2>/dev/null || echo PARSE-ERR)
    echo "== $key: total $n -> $out"
    case "$n" in
      ''|*[!0-9]*) ERRS="$ERRS $key:unparseable-total" ;;
      *)           TOT_ITEMS=$((TOT_ITEMS + n)) ;;
    esac
  fi
  sleep 3   # free-tier rate limit
done <<EOF
$QUERIES
EOF

# ONE row for the registry key `hlidac` — the seven queries are internal fan-out.
if [ -n "$ERRS" ]; then
  mf hlidac error "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" "query failures:$ERRS"
else
  mf hlidac ok "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "== hlidac: $TOT_ITEMS contracts across 7 queries, $TOT_BYTES bytes"
