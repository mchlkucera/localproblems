#!/usr/bin/env bash
# fetch_nen.sh — NEN below-TED-threshold Czech tenders, via the MMR open-data
#                bulk files (Registr veřejných zakázek), no auth.
#
# Usage: scripts/fetch_nen.sh [YYYY-MM-DD-since] [outdir]
#   ARGV SHAPE: $1 = SINCE (ISO date), $2 = outdir.
#   This is the ted/hlidac shape ($1 SINCE, $2 outdir), NOT the
#   feeds/suggest/reddit/nku shape ($1 outdir). It is written here because
#   fetch_all.sh REFUSES a key with no declared argv shape, and because a
#   dispatcher that guesses hands this script a directory path as its since-date
#   and gets a silently wrong window back (§5.3).
#
# WHY THIS INTERFACE AND NOT nen.nipez.cz's LISTING — the full reasoning, with
# the measurements behind it, is at the top of scripts/nen_extract.py. In brief:
# the listing is same-day fresh but is an unversioned HTML template with no
# declared field names; these ZIPs are documented, carry their own interface
# version inside the payload ("verze":"2.10.1"), serve ETag/Last-Modified, and
# hold the below-threshold slice in bulk (18,403 VZMR + 3,838 podlimitní in
# VZ-07-2026) with the buyer IČO on every record. What we gave up is freshness:
# the file for month M is published on the 5th of M+1.
set -euo pipefail
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

SINCE="${1:-$(date -v-90d +%Y-%m-%d 2>/dev/null || date -d '90 days ago' +%Y-%m-%d)}"
TODAY="$(date +%Y-%m-%d)"
OUTDIR="${2:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

BASE="https://isvz.nipez.cz/sites/default/files/content/opendata-rvz"

# The conditional-GET cache. It MUST outlive the run directory: data/raw/<date>/
# is pruned at 28 days, and an ETag pruned with it turns every run into a full
# 63 MB re-download. `data/raw/.cache/` is gitignored by `data/raw/*` and is
# invisible to ingest.sh's pruner, which only ever touches directories whose
# NAME IS AN ISO DATE (scripts/ingest.sh:75-79). Verified against that loop, not
# assumed.
CACHE="${NEN_CACHE:-data/raw/.cache/nen}"
mkdir -p "$CACHE"

# ── run manifest ── same schema as scripts/fetch_ted.sh, deliberately verbatim ──
# One appended row per REGISTRY FEED KEY per run; columns map 1:1 onto the
# fetch_log DDL. See fetch_ted.sh for why the machine seam under
# <raw>/.fetch/receipts.jsonl exists: normalize.py otherwise reconstructs
# `http_status = 200 if nbytes > 0`, which cannot tell a 404 from a 403 from a
# feed that never ran. The true status code, byte count and transfer time exist
# only here, at fetch time.
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

# Months from SINCE to today, oldest first, as YYYY-MM. Computed in python3
# rather than with `date -v`/`date -d` because those two disagree across
# macOS and GNU and this loop must not silently produce a different window on
# the machine that runs it unattended. python3 is already a hard dependency
# (fetch_ted.sh:146 shells out to it mid-loop).
MONTHS="$(python3 - "$SINCE" "$TODAY" <<'PY'
import sys
from datetime import date
s = date.fromisoformat(sys.argv[1]); t = date.fromisoformat(sys.argv[2])
y, m = s.year, s.month
while (y, m) <= (t.year, t.month):
    print(f"{y:04d}-{m:02d}")
    m += 1
    if m == 13: y, m = y + 1, 1
PY
)"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TOT_ITEMS=0; TOT_BYTES=0; TOT_MS=0
ERRS=""; NOTES=""; MONTHS_OK=0; MONTHS_304=0; MONTHS_PENDING=0

# TWO CODES, NOT ONE, AND THE DIFFERENCE IS LOAD-BEARING.
#   LAST_CODE — the code of the last request made. Useful only when nothing
#               worked, to say what went wrong.
#   DATA_CODE — the code of the last request that actually produced a stored
#               payload. THIS is what goes on the receipt.
# One code is not enough because this feed makes several requests per run and
# the LAST one is routinely a legitimate 404 (the current month is published on
# the 5th of the next). Reporting that 404 is not a cosmetic error: normalize.py
# fails the transport check on `http_status is not None and http_status != 200`
# (normalize.py:802), so a clean 4,442-item run would be recorded BROKEN, and
# every record it produced would carry `http_status: 404` against a URL that
# serves 200. MEASURED on the first run of this script, which did exactly that.
LAST_CODE=000
DATA_CODE=""

# HERE-STRING, not `echo … | while`: a piped while runs in a SUBSHELL, so every
# counter below would be discarded when the loop ended and the manifest row
# would always read 0 items. bash 3.2 has no `mapfile`.
while read -r ym; do
  [ -n "${ym:-}" ] || continue
  yyyy="${ym%%-*}"; mm="${ym##*-}"
  file="VZ-$mm-$yyyy.zip"
  url="$BASE/$file"
  etag="$CACHE/$file.etag"
  tmpzip="$OUTDIR/.fetch/$file"
  out="$OUTDIR/nen-$ym.json"
  mkdir -p "$OUTDIR/.fetch"
  echo "== nen $ym  ($url)"

  # -f: a non-2xx must NOT be stored as if it were a data file. --remove-on-error
  # deletes the partial. The explicit `code` test below is NOT redundant with -f:
  # --fail only trips at HTTP >= 400, so a 3xx served as the terminal response
  # passes -f, and 304 is a 3xx we specifically want to see.
  # --etag-compare sends If-None-Match; --etag-save records the new one only on
  # a 200, so a failed run never poisons the cache with an ETag for bytes we do
  # not hold.
  etagnew="$OUTDIR/.fetch/$file.etag.new"
  parse_w "$(curl -fsS -m 900 --retry 2 --retry-delay 5 -L "$url" \
                  --etag-compare "$etag" --etag-save "$etagnew" \
                  -o "$tmpzip" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
  # --etag-save WRITES TO A TEMP PATH AND IS PROMOTED ONLY WHEN NON-EMPTY.
  # MEASURED 2026-08-21: a 304 from these hosts DOES carry an ETag header, and
  # curl 8.7.1 TRUNCATES the --etag-save file to 0 bytes regardless. Pointed
  # straight at the durable cache entry, the first 304 destroys the ETag that
  # produced it and every later run re-downloads all 97 MB while still looking
  # like a conditional GET. A curl behaviour, not a server one — same guard is in
  # fetch_coi.sh and fetch_sukl.sh.
  if [ -s "$etagnew" ]; then mv "$etagnew" "$etag"; else rm -f "$etagnew"; fi

  # ── EXPECTED ABSENCE (§7.2 step 0), and it is a CALENDAR fact, not leniency ──
  # The file for month M is published on the 5th of M+1: measured 2026-08-21,
  # VZ-07-2026 exists (Last-Modified 2026-08-02) and VZ-08-2026 returns 404. So
  # the newest one or two months in any window legitimately DO NOT EXIST YET.
  # Treating that as a failure would put this feed in a permanent BROKEN state
  # for the first days of every month, and an alarm that cries wolf monthly is
  # ignored inside a quarter — at which point the one real outage is invisible
  # too. It is only expected for the CURRENT and PREVIOUS month; a 404 on an
  # older month is a genuine error, because that file was published and has now
  # gone missing.
  if [ "$W_CODE" = "404" ]; then
    rm -f "$tmpzip"
    prev="$(python3 -c "
from datetime import date
t=date.today(); y,m=t.year,t.month-1
if m==0: y,m=y-1,12
print(f'{y:04d}-{m:02d}')")"
    if [ "$ym" \> "$prev" ] || [ "$ym" = "$prev" ]; then
      echo "   not published yet (404) — expected, publishes on the 5th of the next month"
      MONTHS_PENDING=$((MONTHS_PENDING + 1))
      NOTES="$NOTES $ym:not-yet-published"
      continue
    fi
    echo "   404 on an ALREADY-PUBLISHED month — real error"
    ERRS="$ERRS $ym:HTTP-404-on-published-month"
    continue
  fi

  if [ "$W_CODE" = "304" ]; then
    rm -f "$tmpzip"
    echo "   304 Not Modified — byte-identical to the last run, nothing new to read"
    MONTHS_304=$((MONTHS_304 + 1))
    # A 304 is a HEALTHY interaction, so it may stand as the reported code when
    # no month produced bytes. Without this the receipt of an all-304 run reports
    # the trailing not-yet-published 404 instead, which reads as an outage.
    DATA_CODE="${DATA_CODE:-$W_CODE}"
    NOTES="$NOTES $ym:304"
    continue
  fi

  if [ "$W_CODE" != "200" ]; then
    rm -f "$tmpzip"
    echo "   FAILED (HTTP $W_CODE)"
    ERRS="$ERRS $ym:HTTP-$W_CODE"
    continue
  fi

  # ── MODE A — THE SOURCE CONTRACT, EVALUATED BEFORE ANYTHING IS STORED ───────
  # A 200 proves the transfer, not the body. nen_extract.py asserts ZIP magic,
  # exactly one JSON member, a semver `verze`, a declared period that MATCHES THE
  # MONTH WE ASKED FOR, >= 1000 contracts, and at least one NEN identifier. Any
  # of those failing exits 65 and this month is recorded as an error rather than
  # written into data/raw/ — which matters because normalize.py runs a session
  # later and by then a login page on disk is indistinguishable from data.
  if ! read_json="$(python3 scripts/nen_extract.py read "$tmpzip" "$out" \
                      --period "$ym" --since "$SINCE" 2>&1)"; then
    rm -f "$tmpzip" "$out"
    # Poison the cache entry: we hold no good bytes for this ETag, so the next
    # run must re-request in full rather than get a 304 against a body we
    # rejected.
    rm -f "$etag"
    echo "   CONTRACT VIOLATION: $read_json"
    ERRS="$ERRS $ym:CONTRACT"
    continue
  fi
  rm -f "$tmpzip"

  n_in="$(printf '%s' "$read_json"  | python3 -c 'import json,sys; print(json.loads(sys.stdin.read()).get("contracts_in_file",0))' 2>/dev/null || echo 0)"
  n_out="$(printf '%s' "$read_json" | python3 -c 'import json,sys; print(json.loads(sys.stdin.read()).get("fetched",0))' 2>/dev/null || echo 0)"
  echo "   -> $out: $n_out below-threshold NEN contracts kept of $n_in in file"
  TOT_ITEMS=$((TOT_ITEMS + n_out))
  MONTHS_OK=$((MONTHS_OK + 1))
  DATA_CODE="$W_CODE"
done <<EOF
$MONTHS
EOF

# ── MODE B — SILENT ABSENCE, MADE LOUD AT THE SOURCE ────────────────────────
# `SCRIPTED-SILENT` is a named failure in this repo: a fetcher that runs clean
# while zero records reach the ledger, which two feeds sat in for weeks. The
# health view catches it eventually, from the other end; this catches the half
# the health view cannot distinguish — a run that fetched a payload and selected
# nothing out of it. It is reported as an ERROR row, not a warning, because an
# `ok` row with items=0 is exactly the shape that gets skimmed past.
REPORT_CODE="${DATA_CODE:-$LAST_CODE}"
if [ "$MONTHS_OK" -eq 0 ] && [ -z "$ERRS" ] && [ "$MONTHS_PENDING" -gt 0 ] && [ "$MONTHS_304" -eq 0 ]; then
  # Every month in the window is legitimately unpublished. Nothing is wrong.
  mf nen skipped "$REPORT_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "no published month in window since=$SINCE:$NOTES"
  echo "== nen: SKIPPED — nothing published in the window yet ($NOTES)"
elif [ "$MONTHS_OK" -eq 0 ] && [ -z "$ERRS" ] && [ "$MONTHS_304" -gt 0 ]; then
  # Every published month was byte-identical to last run. Honest no-op.
  mf nen skipped "$REPORT_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "all months 304 Not Modified:$NOTES"
  echo "== nen: SKIPPED — all months unchanged since last run ($NOTES)"
elif [ -n "$ERRS" ]; then
  mf nen error "$REPORT_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" \
     "month failures:$ERRS${NOTES:+ ;}$NOTES"
  echo "== nen: $TOT_ITEMS items, ERRORS:$ERRS"
elif [ "$TOT_ITEMS" -eq 0 ]; then
  mf nen error "$REPORT_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "ZERO-YIELD: $MONTHS_OK month(s) parsed clean and selected 0 contracts since=$SINCE — \
selection is broken or the window is wrong; a clean fetch with no items is SCRIPTED-SILENT"
  echo "== nen: ZERO YIELD over $MONTHS_OK parsed month(s) — reported as an ERROR on purpose"
else
  mf nen ok "$REPORT_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" \
     "${NOTES:+months:$NOTES}"
  echo "== nen: $TOT_ITEMS below-threshold contracts from $MONTHS_OK month(s), $TOT_BYTES bytes"
fi
