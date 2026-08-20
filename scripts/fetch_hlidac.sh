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
  # WHY THIS EXISTS. The true status code, byte count and transfer time exist
  # ONLY here, at fetch time, and are gone by the time normalize runs. Without
  # this file normalize could only infer transport from whether a payload landed
  # on disk, which cannot tell a 404 from a 403 from a feed that never ran — and
  # an inferred 200 is WORSE than a missing status, because it reads as
  # evidence. normalize.py now READS this file (load_receipts) and records
  # `http_status: null` when a feed has no receipt rather than synthesizing one.
  #
  # Field names are exactly db.py's FETCHLOG_FIELDS so a merge into
  # contract.json needs no translation. normalize.py prefers these values and
  # leaves items_kept / yield_anomaly to itself. `error` is carried through even
  # on an `ok` result, so a note like a partial fetch or a capped page window
  # reaches /sources instead of being dropped by the contract verdict.
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

# Same trick for the per-page counts: P_ITEMS is what LANDED ON DISK, P_TOTAL is
# what the API says exists. Keeping them apart is the whole fix below.
parse_counts() { # "<results_len> <api_total>"
  set -- ${1:-}
  P_ITEMS="${1:-ERR}"; P_TOTAL="${2:-ERR}"
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
# RE-MEASURED 2026-08-20 by review, same negative control:
#     %HLIDAC_TOKEN        -> curl exit 2, "variable expansion failure"
#     %HLIDAC_STATU_TOKEN  -> curl exit 1, "Protocol lpnoscheme not supported"
# and a real paged fetch under $HLIDAC_STATU_TOKEN returned 7/7 HTTP 200.
#
# THE STALE CLAIM THIS COMMENT USED TO CARRY, struck and recorded because the
# shape recurs: it said 'architecture-v3.md blockers row 1 asserts BOTH names
# are "genuinely ABSENT — coordinator-verified"'. That string appears NOWHERE in
# architecture-v3.md — grep it — and blockers row 1 says the opposite today:
# "RESOLVED — THE FEED IS LIVE … the token exists under HLIDAC_STATU_TOKEN, not
# HLIDAC_TOKEN". A comment that quotes another file is a claim about that file
# and goes stale the moment the file is fixed. Do not restate a second
# document's contents here; name the section and let the reader open it.
token_present() { # NAME -> 0 only on POSITIVE EVIDENCE the vault holds it.
  # 'lpnoscheme://' is an unsupported protocol ON PURPOSE: curl parses options
  # and expands variables BEFORE touching the network, so presence resolves with
  # ZERO transmission of the secret to anywhere.
  #
  # THIS READS CURL'S MESSAGE, NOT ITS EXIT CODE, and that is a correction paid
  # for by a measurement. The previous version was `[ $? -ne 2 ]` — "anything
  # that is not "variable expansion failure" means present". MEASURED
  # 2026-08-20: run this probe where with-secrets itself cannot start (a
  # sandboxed shell, a locked vault, a wrong --dir) and it exits 1 with
  # `mktemp: mkstemp failed … Operation not permitted` — never reaching curl at
  # all. 1 is not 2, so the old test reported the ABSENT name HLIDAC_TOKEN as
  # PRESENT, printed a confident auth banner, and then took seven HTTP 000s.
  # A probe that turns "the method did not run" into "the thing exists" is the
  # exact failure this repo keeps writing down: a negative result is evidence
  # only when the method is known to produce positives.
  #
  # So each outcome must be named by its own evidence:
  #   "variable expansion failure"  -> the name is genuinely not in the vault
  #   "not supported"               -> expansion SUCCEEDED, curl then rejected
  #                                    the bogus scheme: the name exists
  #   anything else                 -> INCONCLUSIVE, reported as such
  # Nothing here prints $out; with-secrets scrubs its own stderr besides.
  #
  # DELIBERATELY NO -f ON THIS ONE CURL, and it is the only such exemption in
  # scripts/. --fail governs how an HTTP RESPONSE is treated, and this call
  # never makes a request: the bogus scheme is rejected during option parsing.
  # There is no response to fail on, no body, and no -o, so -f cannot change
  # any outcome here. Every curl that actually fetches a payload carries -f.
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
  # This guard is the reason this feed fails LOUDLY instead of storing an
  # auth-error body (§7.1 receipt 4). It also leaves a manifest row: a blocked
  # feed that writes no fetch_log row is invisible to db.py health, which is
  # exactly the Mode-B silence §7.5 exists to make visible. The two causes are
  # kept apart on that row, because "no key" is an owner action and "the probe
  # could not run" is an environment one.
  if [ "$PROBE_BROKEN" -eq 1 ]; then
    mf hlidac error 000 0 0 0 "$STARTED" "" \
       "auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Token presence UNKNOWN, not absent."
    echo "FAILED: could not probe the vault at all — token presence is UNKNOWN." >&2
    echo "        with-secrets must be able to write a temp file and exec curl." >&2
  else
    mf hlidac error 000 0 0 0 "$STARTED" "" \
       "no Hlidac token in the vault: HLIDAC_TOKEN and HLIDAC_STATU_TOKEN both fail curl variable expansion"
    echo "FAILED: neither HLIDAC_TOKEN nor HLIDAC_STATU_TOKEN is in the sops vault." >&2
    echo "        Free key at hlidacstatu.cz/api, then: sops-edit .env.enc" >&2
  fi
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

# ── PAGING ── measured 2026-08-20 against three authenticated 200s ───────────
# The API page is FIXED AT 25: `strana=1` and `strana=2` on a query whose `total`
# is 477 each returned exactly 25 results with ZERO id overlap. There is no page
# -size parameter to raise.
#
# THE BUG THIS REPLACES, and it is the interesting kind — a wrong number that
# reads as a good one. The old loop fetched `strana=1` only, wrote 25 contracts
# to disk, and then reported the API's `total` (477 for the nis2 query alone) as
# items_fetched. So the manifest, fetch_log and /sources all showed a feed
# fetching roughly 4x MORE than it really did, and the ~92% of the result set
# nobody was paging through was invisible precisely because the over-count
# filled the gap. Two independent facts have to be kept apart to see it:
# P_ITEMS (what landed on disk) and P_TOTAL (what exists).
#
# The cap is a real cap, not a fix: 4 pages x 25 = 100 contracts per query. When
# a query has more than that, the shortfall is REPORTED on the manifest row
# rather than rounded away. Raise it with HLIDAC_PAGES if the free-tier rate
# limit allows; each extra page costs one request and one 3s sleep.
PAGE_SIZE=25
PAGES="${HLIDAC_PAGES:-4}"

TOT_ITEMS=0; TOT_AVAIL=0; TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""

# HERE-STRING, not `echo … | while`: a piped while runs in a SUBSHELL and would
# discard every total accumulated below, leaving the manifest row reading 0.
while IFS='|' read -r key q; do
  [ -n "${key:-}" ] || continue
  full="($q) AND datumUzavreni:[$SINCE TO *]"
  q_items=0; q_total=0; p=1

  while [ "$p" -le "$PAGES" ]; do
    out="$OUTDIR/hlidac-$key-p$p.json"

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
                    --data-urlencode "strana=$p" \
                    --variable "%$TOKEN_VAR" \
                    --expand-header "Authorization: Token {{$TOKEN_VAR}}" \
                    -o "$out" --remove-on-error \
                    -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
    LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))

    if [ "$W_CODE" != "200" ]; then
      echo "== $key p$p: FAILED (HTTP $W_CODE)"
      ERRS="$ERRS $key/p$p:HTTP-$W_CODE"
      break
    fi
    TOT_BYTES=$((TOT_BYTES + W_BYTES))

    # ITEMS ON DISK first, api total second. Reading `total` alone is the bug.
    parse_counts "$(python3 -c "import json,sys;d=json.load(sys.stdin);print(len(d.get('results') or []), d.get('total', -1))" < "$out" 2>/dev/null || true)"
    case "$P_ITEMS" in
      ''|*[!0-9]*) echo "== $key p$p: unparseable payload"
                   ERRS="$ERRS $key/p$p:unparseable"; break ;;
    esac
    case "$P_TOTAL" in ''|*[!0-9]*) : ;; *) q_total="$P_TOTAL" ;; esac
    q_items=$((q_items + P_ITEMS))
    echo "== $key p$p: +$P_ITEMS on disk (api total $q_total) -> $out"

    # Stop on a short page (the result set ended) or once the set is covered —
    # both avoid spending a request on a page we already know is empty.
    # WRITTEN AS `if`, NOT `[ … ] && break`: under `set -e` a false one-line
    # test-and-command is a non-zero statement, and this script has already been
    # bitten once by a control-flow subtlety (the subshell `while`).
    if [ "$P_ITEMS" -lt "$PAGE_SIZE" ]; then break; fi
    # Only when the API told us a real total — an unreadable `total` must mean
    # "keep paging until a short page", never "stop after page 1".
    if [ "$q_total" -gt 0 ] && [ "$q_items" -ge "$q_total" ]; then break; fi
    p=$((p + 1))
    sleep 3   # free-tier rate limit
  done

  if [ "$q_total" -lt "$q_items" ]; then q_total="$q_items"; fi
  TOT_ITEMS=$((TOT_ITEMS + q_items))
  TOT_AVAIL=$((TOT_AVAIL + q_total))
  sleep 3   # free-tier rate limit
done <<EOF
$QUERIES
EOF

# ONE row for the registry key `hlidac` — the seven queries are internal fan-out.
# items_fetched is TOT_ITEMS: the contracts actually on disk, which is what
# normalize will parse and what expected_yield is bounded against.
COVER=""
if [ "$TOT_AVAIL" -gt "$TOT_ITEMS" ]; then
  COVER="coverage: $TOT_ITEMS of $TOT_AVAIL available (page cap HLIDAC_PAGES=$PAGES x $PAGE_SIZE)"
fi
if [ -n "$ERRS" ]; then
  mf hlidac error "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" "query failures:$ERRS${COVER:+ · $COVER}"
else
  # An `ok` row carrying a coverage note: the run succeeded AND under-fetched.
  # Both facts survive — result=ok keeps fetch_log.ok=1 and the feed out of
  # BROKEN, while the note reaches /sources through normalize's error passthrough.
  mf hlidac ok "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" "$COVER"
fi
echo "== hlidac: $TOT_ITEMS contracts on disk of $TOT_AVAIL available, $TOT_BYTES bytes"
