#!/usr/bin/env bash
# fetch_feeds.sh — RSS + yc-oss fetches. No auth.
# Usage: scripts/fetch_feeds.sh [outdir]           <-- outdir is $1 (see §5.3)
# Writes raw payloads into outdir (default data/raw/<today>/).
set -uo pipefail   # no -e: one failed feed must not kill the rest
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

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

fetch() { # feed_key filename url min_bytes
  key="$1"; name="$2"; url="$3"; min="$4"
  out="$OUTDIR/$name"
  started="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  # -f IS LOAD-BEARING. Without it curl writes the 4xx/5xx BODY to disk and
  # exits 0, so the script prints OK over a payload containing nothing we want.
  # That is the vestbee moat leak (§7.1 receipt 1, §10 row 4).
  # Reproduce rather than trust a number — the byte count is not stable (the
  # dead URL served a 313KB HTML 404 and a 189-byte JSON 404 minutes apart on
  # 2026-08-20; only the STORED-LIE mechanism is durable):
  #   curl -sL  -m 30 https://www.vestbee.com/blog/rss.xml -o /tmp/x; echo $?  -> 0, file written
  #   curl -fsSL -m 30 --remove-on-error … -o /tmp/x; echo $?                  -> 22, no file
  # --remove-on-error (curl >= 7.83; this box has 8.7.1) additionally guarantees
  # no truncated file survives for normalize.py to mistake for a real payload.
  # The explicit `code = 200` test below is NOT redundant with -f: --fail only
  # trips at HTTP >= 400, so a 3xx that lands (e.g. an auth redirect served as
  # the terminal response) passes -f cleanly. Both checks are required.
  parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                  -A "$UA" -o "$out" \
                  -w '%{http_code} %{size_download} %{time_total}' "$url" 2>/dev/null || true)"

  if [ "$W_CODE" = "200" ] && [ "$W_BYTES" -ge "$min" ]; then
    echo "OK  $name (HTTP $W_CODE, $W_BYTES bytes)"
    mf "$key" ok "$W_CODE" "$W_BYTES" "" "$W_MS" "$started" "$out" ""
  elif [ "$W_CODE" = "200" ]; then
    # A 200 under the floor is the Mode-A failure with a good status line.
    echo "FAILED $name (HTTP 200 but $W_BYTES bytes < min $min) <- $url"
    mf "$key" error "$W_CODE" "$W_BYTES" "" "$W_MS" "$started" "$out" \
       "under-min-bytes: $W_BYTES < $min"
  else
    echo "FAILED $name (HTTP $W_CODE) <- $url"
    mf "$key" error "$W_CODE" "$W_BYTES" "" "$W_MS" "$started" "" "transport: HTTP $W_CODE"
  fi
}

# min_bytes floors are measured, not guessed (probed 2026-08-20):
#   cc.cz/feed/ = 18,080 bytes · yc-oss all.json = 10,402,545 bytes.
fetch cc-cz  feed-czechcrunch.xml "https://cc.cz/feed/"                                            1000
fetch yc-oss yc-all.json          "https://raw.githubusercontent.com/yc-oss/api/main/companies/all.json" 100000

# REMOVED 2026-08-20 — `vestbee` is DEAD (§10 row 3, registry status: dead).
#   https://www.vestbee.com/blog/rss.xml -> 301 -> /insights/rss.xml -> 404.
# Re-measured before removal: final=404, 313,275 bytes of HTML. Do not re-add
# without a fresh probe; the registry row carries status:dead and the reason.
