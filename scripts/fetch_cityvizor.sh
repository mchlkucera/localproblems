#!/usr/bin/env bash
# fetch_cityvizor.sh — CityVizor public invoice API -> data/lookup/, NOT a feed.
#
# ══ WHAT THIS IS ═════════════════════════════════════════════════════════════
# CityVizor (cityvizor.cz, AGPL-3.0, written at the Ministry of Finance, run by
# Otevřená města z.s.) publishes the ACCOUNTING LEDGER of every municipality
# that uploads one: one row per invoice line with the counterparty's IČO, the
# amount, the free-text description and the budget paragraph/item. MEASURED
# 2026-09-05: 338 profiles, 35 with payments, 26 of them `status: visible`.
# That is the register's executed-spend question — what did a named Czech
# public buyer ACTUALLY PAY for a thing, below every tender threshold — and
# the counterpart of the MS2021+ lookup (what they were APPROVED to spend).
#
# ══ IT WRITES A LOOKUP TABLE AND GETS NO REGISTRY ROW, ON PURPOSE ════════════
# ~80,000 purchase lines a year, every one carrying real money, would pass
# materiality and bury data/signals/** many times over — the `smlouvy` trap
# data/feeds.json names. Output is data/lookup/cityvizor-invoices.jsonl
# (CONVENTIONS.md "Lookup layer": committed, never pruned, no evidence type,
# no score, not walked by db.py or the build gate), read on demand by
# scripts/cityvizor_query.py. So: NO row in data/feeds.json, and nothing is
# ever written into the run directory's root where normalize.py would find it
# and try to parse it as an unknown feed (the fetch_tacr.sh rule). Raw JSON
# lives under $OUTDIR/.fetch/cityvizor/ — a subdirectory, invisible to
# normalize.py's isfile-only payload scan.
#
# ══ THE 10,000-ROW CAP AND HOW THIS SCRIPT GETS PAST IT HONESTLY ═════════════
# The router (server/src/routers/public/profile-payments.ts) clamps `limit`
# to 10,000 and offers no page token; `year`/`month` are not read at all. It
# DOES honour `dateFrom` (>=) and `dateTo` (<, exclusive). So each body is
# walked through DISJOINT date windows — the whole range, then calendar
# years, then months, then days — and a window is split only when it comes
# back holding exactly the cap. Disjoint windows never overlap, so no row is
# fetched twice and none is deduplicated away. A single DAY over the cap
# would need `offset` paging, where Postgres gives no stable order across
# pages: such windows are accepted with paged=1 and COUNTED, never hidden.
# Every request carries `sort=date`, exactly what the site's own invoices
# page sends (client/…/profile-invoices.component.ts), so this walk looks to
# the host like a patient reader of its own UI.
#
# No rate limit is stated anywhere (no robots.txt, no RateLimit headers,
# nothing in README/CONTRIBUTING), so CITYVIZOR_SLEEP seconds (default 1)
# pass between calls, and curl retries 429/5xx twice with a 5 s delay.
#
# ══ THE WINDOW, AND WHY IT IS SHORTER THAN TWO YEARS ═════════════════════════
# Default fetch range: the first day of the month 24 months ago, up to and
# including today (CITYVIZOR_FROM / CITYVIZOR_TO override). But data/lookup/
# is committed and never pruned and the ms21 ceiling (30 MB) is the owner's
# stop rule; MEASURED, two years of purchase lines is ~45 MB. So the indexer
# keeps whole months, newest first, and drops the OLDEST month across ALL
# bodies until the file fits, and this script PRINTS the kept window and
# writes it into the receipt. Everything fetched stays under .fetch/ for the
# life of the run directory (28 days), so a wider index is one re-run of the
# indexer away, not a re-fetch.
#
# Usage: scripts/fetch_cityvizor.sh [outdir]      <-- outdir is $1 (the nku/tacr shape)
set -uo pipefail   # no -e: a failed transfer must still write its receipt
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
INDEXER="$HERE/cityvizor_index.py"

API="${CITYVIZOR_API:-https://cityvizor.cz/api/public}"
LOOKUP="${CITYVIZOR_LOOKUP:-$ROOT/data/lookup/cityvizor-invoices.jsonl}"
MAX_MB="${CITYVIZOR_MAX_MB:-30}"
SLEEP="${CITYVIZOR_SLEEP:-1}"
CAP=10000   # parseAndLimitNumber(req.query.limit, 10000) — the router's clamp
UA="localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

command -v jq >/dev/null 2>&1 || { echo "fetch_cityvizor: jq is required" >&2; exit 2; }
command -v python3 >/dev/null 2>&1 || { echo "fetch_cityvizor: python3 is required" >&2; exit 2; }
[ -f "$INDEXER" ] || { echo "fetch_cityvizor: $INDEXER missing" >&2; exit 2; }

# [FROM, TO) — TO is EXCLUSIVE like the router's dateTo, so "tomorrow" means
# "through today". Date arithmetic in python3: bash 3.2 has no portable
# month maths and BSD `date -v` is not GNU `date -d`.
FROM="${CITYVIZOR_FROM:-$(python3 -c 'import datetime as d;t=d.date.today();print(d.date(t.year-2,t.month,1))')}"
TO="${CITYVIZOR_TO:-$(python3 -c 'import datetime as d;print(d.date.today()+d.timedelta(days=1))')}"

RAW="$OUTDIR/.fetch/cityvizor"
mkdir -p "$RAW"
WINDOWS="$RAW/windows.tsv"
ERRORS="$RAW/errors.log"
: > "$WINDOWS"
: > "$ERRORS"

# No `rm` in this script. `find <path> -maxdepth 0 -delete` removes exactly the
# named path and nothing else, and a missing file is not news.
rmf() {
  for f in "$@"; do
    [ -e "$f" ] && find "$f" -maxdepth 0 -delete 2>/dev/null
  done
  return 0
}

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# Verbatim from fetch_tacr.sh / fetch_ms21.sh — the manifest is a cross-file
# contract, not a place for local taste.
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
  # Field names are db.py's FETCHLOG_FIELDS. MEASURED (fetch_ms21.sh):
  # normalize.py consults receipts as `receipts.get(feed_key)` per REGISTERED
  # feed only, so a `cityvizor` key it does not know is inert — a record for
  # humans, not an orphan feed.
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

# Parse curl's -w receipt into W_CODE / W_BYTES / W_SECS / W_MS / W_CT.
parse_w() { # "<http_code> <size_download> <time_total> <content_type>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_CT="${4:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

# Running totals for the ONE receipt this run writes: the transport question
# is "did the ledgers arrive", and that is answered by the sum, per body.
CALLS=0; TOTAL_BYTES=0; TOTAL_MS=0; FAILED=0; LAST_CODE=000

get() { # url outfile
  parse_w "$(curl -fsS -m 300 --retry 2 --retry-delay 5 -A "$UA" \
                  -o "$2" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                  "$1" 2>/dev/null || true)"
  CALLS=$((CALLS + 1)); TOTAL_BYTES=$((TOTAL_BYTES + W_BYTES)); TOTAL_MS=$((TOTAL_MS + W_MS))
  LAST_CODE="$W_CODE"
  sleep "$SLEEP"
}

fail() { # message — a hole in the walk is recorded, never skipped past
  FAILED=$((FAILED + 1))
  echo "   FAILED $1" | tee -a "$ERRORS" >&2
}

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "== cityvizor  $API  window [$FROM, $TO)"

# ── 1. THE PROFILES LIST, GUARDED ────────────────────────────────────────────
PROFILES="$RAW/profiles.json"
get "$API/profiles" "$PROFILES"
if [ "$W_CODE" != "200" ]; then
  echo "   FAILED (HTTP $W_CODE) fetching the profiles list"
  mf cityvizor error "$W_CODE" "$TOTAL_BYTES" 0 "$TOTAL_MS" "$STARTED" "$RAW" "profiles: HTTP-$W_CODE ct=$W_CT"
  exit 1
fi
# MODE A — a 200 proves the transfer, not the body. nginx serves the Angular
# shell as 200 text/html for any path it does not know, and an error object is
# JSON too; the guard refuses both before a single body is walked.
if ! META="$(python3 "$INDEXER" guard-profiles "$PROFILES" 2>&1)"; then
  echo "   FAILED — MODE-A: $META"
  echo "          content-type: $W_CT"
  echo "          first 120 bytes: $(head -c 120 "$PROFILES" | tr -d '\n')"
  mf cityvizor error "$W_CODE" "$TOTAL_BYTES" 0 "$TOTAL_MS" "$STARTED" "$PROFILES" "MODE-A refused: $META (ct=$W_CT)"
  exit 1
fi
echo "   profiles: $META"

# ── 2. THE WALK ──────────────────────────────────────────────────────────────
# walk <id> <from> <to> <level>   level ∈ range|year|month|day
# Recursive, and every variable is `local`: bash 3.2 rebinds positional
# parameters per call, so the recursion is safe as long as nothing global is
# touched except the totals and the window list.
walk() {
  local id="$1" from="$2" to="$3" level="$4"
  local f n meta wf wt off f2 n2 next
  f="$RAW/$id/${from}_${to}.json"
  mkdir -p "$RAW/$id"
  get "$API/profiles/$id/payments?dateFrom=$from&dateTo=$to&limit=$CAP&sort=date" "$f"
  if [ "$W_CODE" != "200" ]; then
    fail "profile $id [$from,$to) HTTP $W_CODE"
    return 0
  fi
  if ! meta="$(python3 "$INDEXER" guard "$f" 2>&1)"; then
    fail "profile $id [$from,$to) MODE-A: $meta"
    return 0
  fi
  n="$(printf '%s' "$meta" | jq -r .rows)"
  case "$n" in ''|*[!0-9]*) n=0 ;; esac
  if [ "$n" -lt "$CAP" ]; then
    printf '%s\t%s\t%s\t%s\t0\n' "$id" "$from" "$to" "$f" >> "$WINDOWS"
    return 0
  fi
  # ── the window is CAPPED: it holds exactly 10,000 rows, i.e. truncated ──
  case "$level" in
    range) next=year ;;
    year)  next=month ;;
    month) next=day ;;
    *)     next="" ;;
  esac
  if [ -n "$next" ]; then
    # Superseded by its pieces. Kept beside them as `.capped` evidence, and
    # never listed in windows.tsv, so the indexer cannot double count it.
    mv "$f" "$f.capped"
    echo "   profile $id [$from,$to) capped at $CAP — splitting into ${next}s"
    while read -r wf wt; do
      [ -n "$wf" ] && walk "$id" "$wf" "$wt" "$next"
    done < <(python3 "$INDEXER" "${next}s" --from "$from" --to "$to")
    return 0
  fi
  # A single day over the cap. Nothing left to split: page by offset, and say
  # so — paged=1 on every piece, counted by the indexer as paged_windows.
  echo "   profile $id [$from,$to) is ONE DAY over $CAP rows — offset paging (order not stable)"
  printf '%s\t%s\t%s\t%s\t1\n' "$id" "$from" "$to" "$f" >> "$WINDOWS"
  off=$CAP
  while :; do
    f2="$RAW/$id/${from}_${to}.off$off.json"
    get "$API/profiles/$id/payments?dateFrom=$from&dateTo=$to&limit=$CAP&offset=$off&sort=date" "$f2"
    if [ "$W_CODE" != "200" ]; then
      fail "profile $id [$from,$to) offset $off HTTP $W_CODE"
      return 0
    fi
    if ! meta="$(python3 "$INDEXER" guard "$f2" 2>&1)"; then
      fail "profile $id [$from,$to) offset $off MODE-A: $meta"
      return 0
    fi
    n2="$(printf '%s' "$meta" | jq -r .rows)"
    case "$n2" in ''|*[!0-9]*) n2=0 ;; esac
    [ "$n2" -gt 0 ] && printf '%s\t%s\t%s\t%s\t1\n' "$id" "$from" "$to" "$f2" >> "$WINDOWS"
    [ "$n2" -lt "$CAP" ] && return 0
    off=$((off + CAP))
  done
}

BODIES=0
while IFS="$(printf '\t')" read -r pid slug name ico; do
  [ -n "$pid" ] || continue
  BODIES=$((BODIES + 1))
  echo "-- $pid  $name  (IČO ${ico:-—})  /$slug/faktury"
  walk "$pid" "$FROM" "$TO" range
done < <(python3 "$INDEXER" bodies "$PROFILES")

NWIN="$(wc -l < "$WINDOWS" | tr -d ' ')"
echo "   $BODIES bodies walked in $CALLS calls, $TOTAL_BYTES bytes, $NWIN window(s) accepted, $FAILED failure(s)"

# ── A HOLE IS AN ERROR, NOT A QUIET OK ───────────────────────────────────────
# One month missing from one body would sit in the index looking like "that
# body bought nothing that month". The previous index stays; the failures are
# in $ERRORS and in the receipt. Re-run.
if [ "$FAILED" -gt 0 ]; then
  mf cityvizor error "$LAST_CODE" "$TOTAL_BYTES" 0 "$TOTAL_MS" "$STARTED" "$RAW" \
     "$FAILED window(s) failed — index NOT rebuilt; see $ERRORS: $(head -c 150 "$ERRORS" | tr '\n' ' ')"
  echo "== cityvizor: $FAILED failed window(s) — index NOT rebuilt, reported as an ERROR on purpose"
  exit 1
fi

# ── 3. THE INDEX ─────────────────────────────────────────────────────────────
if ! SUMMARY="$(python3 "$INDEXER" index --profiles "$PROFILES" --windows "$WINDOWS" \
                        --out "$LOOKUP" --max-mb "$MAX_MB" 2>&1)"; then
  echo "   INDEX FAILED: $SUMMARY"
  mf cityvizor error "$LAST_CODE" "$TOTAL_BYTES" 0 "$TOTAL_MS" "$STARTED" "$LOOKUP" \
     "index failed: $(printf '%s' "$SUMMARY" | tail -c 180)"
  exit 1
fi
jf() { printf '%s' "$SUMMARY" | jq -r "$1" 2>/dev/null; }
N="$(jf .kept)"
case "$N" in ''|*[!0-9]*) N=0 ;; esac

echo "   $(jf .lines) ledger line(s) read from $(jf .windows) window(s) of $(jf .bodies) bodies"
echo "   kept $N purchase line(s) -> $LOOKUP  ($(jf .mb) MB)"
echo "   window kept: $(jf .kept_from) .. $(jf .kept_to)  (fetched [$(jf .fetched_from), $(jf .fetched_to)); months trimmed to fit ${MAX_MB} MB: $(jf '.months_trimmed | length') — $(jf '.months_trimmed | join(",")'))"
echo "   skipped: income $(jf .income_skipped) · negative $(jf .negative_skipped) · zero $(jf .zero_skipped) · non-purchase items $(jf '[.non_purchase_skipped[]] | add // 0') ($(jf '.non_purchase_skipped | to_entries | map("\(.key)=\(.value)") | join(" ")'))"
echo "   contact-shaped text cut on $(jf .contact_cut) line(s) · identical lines given -n suffixes: $(jf .duplicate_lines) · paged windows: $(jf .paged_windows) · rows whose body has no IČO in its profile: $(jf .no_body_ico)"

# ── ZERO YIELD IS AN ERROR, NOT A QUIET OK ───────────────────────────────────
if [ "$N" -eq 0 ]; then
  mf cityvizor error "$LAST_CODE" "$TOTAL_BYTES" 0 "$TOTAL_MS" "$STARTED" "$LOOKUP" \
     "ZERO YIELD: $(jf .lines) lines read and none kept — the item filter or the source shape moved"
  echo "== cityvizor: ZERO YIELD — reported as an ERROR on purpose"
  exit 1
fi

mf cityvizor ok 200 "$TOTAL_BYTES" "$N" "$TOTAL_MS" "$STARTED" "$LOOKUP" \
   "lookup table, not a feed — no data/feeds.json row by design; $(jf .bodies) bodies, kept $(jf .kept_from)..$(jf .kept_to), $(jf .mb)MB, trimmed $(jf '.months_trimmed | length') month(s), paged=$(jf .paged_windows)"
echo "== cityvizor: $N purchase line(s) from $(jf .bodies) bodies in $LOOKUP  (ok)"
exit 0
