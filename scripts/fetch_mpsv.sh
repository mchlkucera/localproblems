#!/usr/bin/env bash
# fetch_mpsv.sh — MPSV/ÚP `volna-mista` open data, no auth. CZ vacancies.
#
# Usage: scripts/fetch_mpsv.sh <rawdir> [YYYY-MM]
#   ARGV SHAPE: $1 = outdir, $2 = optional target month. This is the four-script
#   shape (outdir first), NOT the ted/hlidac shape (§5.3). Verify against this
#   header before adding a row to INGEST.md's call-shape table.
#
# Writes ONE file into <rawdir>:  mpsv-hiring-<YYYY-MM>.json
# and the ARES worklist into     <rawdir>/.fetch/ares-worklist.txt
#
# ── WHICH INTERFACE, AND WHAT IT COST ────────────────────────────────────────
# THE FULL DATASET IS NOT FETCHABLE ON A SCHEDULE. `volna-mista.json` measured
# content-length 185,271,163 (185 MB) — a daily full pull is 5.4 GB/month for a
# corpus that changes by ~2,000 rows a day. It is also a SNAPSHOT of live stock,
# so it cannot tell a new posting from a repost, which is the one thing this feed
# must know (`data/CONVENTIONS.md`: "reposting is the whole problem").
#
# THE INCREMENT PATH EXISTS AND IS DECLARED. `/od/soubory/volna-mista-prirustek/`
# publishes one file per day, named by date, back to 2024-10-31 (479 files
# measured 2026-08-21). One day = 12,076,717 bytes as .json, 904,274 bytes as
# .json.gz — and the .gz is BYTE-IDENTICAL after decompression (verified by
# sha256 on 2026-08-20: both 2a24984139...64af), so the .gz is a transport
# optimisation and not a different snapshot, despite carrying a later mtime.
# A whole month is ~19 MB on the wire. That is a 10,000x reduction against the
# naive route, on a DECLARED, DATE-ADDRESSED interface — no HTML scraping, no
# undocumented query API, no session.
#
# WHAT WE GAVE UP by choosing the increment over the snapshot: the increment is a
# CHANGELOG, so it cannot answer "how many vacancies exist right now" — only
# "what changed". The register wants flow, not stock, so this is the right trade;
# it is stated because it is a real limitation, not because it is free.
#
# WHY A WHOLE MONTH PER RUN AND NO LOCAL ACCUMULATOR. The aggregate id is
# `mpsv-<YYYY-MM>-<theme>`, so the unit of work is a MONTH; and every day of that
# month is still on MPSV's server. Re-fetching the month from the source is
# therefore idempotent and stateless, where an accumulator under data/raw/ would
# be silently destroyed by ingest.sh's 28-day prune. No state to corrupt, no
# state to prune, re-runnable at any time, same answer.
#
# ── THE TWO FAILURE MODES (docs/architecture-v3.md §7.1) ─────────────────────
# MODE A — a good transfer carrying the wrong body. MEASURED, and MPSV has an
#   unusually nasty version of it: a GET for an absent day returns 404 with a
#   57,871-BYTE HTML PAGE, and `curl -sL` without `-f` would store that as the
#   day's payload. Worse, **a HEAD on the same absent URL returns HTTP 200**
#   (measured 2026-08-15 and 2026-08-21: HEAD 200 text/html, GET 404). So an
#   existence probe by HEAD is a lie here. This script therefore: uses -f,
#   --remove-on-error, an EXPLICIT `code = 200` test, and never probes by HEAD.
# MODE B — silent absence. Nothing here can catch that; the health view does
#   (§7.5), which is why every path below writes a receipt even when it skips.
#
# ── PERSONAL DATA ────────────────────────────────────────────────────────────
# The dataset's own DCAT record declares `obsahuje-osobní-údaje`, and the payload
# earns it: 2,471 of 2,473 postings in one day carry a contact person's surname,
# 2,243 an email, 1,676 a phone. The raw increments are therefore downloaded to a
# WORK DIRECTORY OUTSIDE THE REPOSITORY and deleted at the end of the run — they
# never enter data/raw/, gitignored or not. scripts/mpsv_reduce.py applies the
# field allowlist and refuses to write anything if a contact string survives.
set -euo pipefail
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

# Default target = the LAST COMPLETE month. A month still in progress would be
# aggregated once, written under `mpsv-<YYYY-MM>-*`, and then blocked by
# data/signals/seen.txt for the rest of the month — a permanently partial record.
MONTH="${2:-$(python3 -c "
import datetime
t = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
print(t.strftime('%Y-%m'))")}"
case "$MONTH" in
  [0-9][0-9][0-9][0-9]-[0-9][0-9]) : ;;
  *) echo "fetch_mpsv: month must be YYYY-MM, got '$MONTH'" >&2; exit 3 ;;
esac

BASE="https://data.mpsv.cz/od/soubory"
INC="$BASE/volna-mista-prirustek"
SEEN="${SEEN_TXT:-data/signals/seen.txt}"
OUT="$OUTDIR/mpsv-hiring-$MONTH.json"

# ── run manifest ── same table and same columns as scripts/fetch_ted.sh ──────
# result=ok      -> fetch_log.ok = 1
# result=skipped -> fetch_log.ok = 1, parse_method='none'. EXPECTED ABSENCE
#                   (§7.2 step 0) — mpsv sets contract.allow_missing:true, and it
#                   needs it: 180 of 659 calendar days have no increment file
#                   (re-measured 2026-08-21 off the directory index, 479 files
#                   over a 659-day span = 27.3% absent). It MUST NOT increment
#                   consecutive_failures and MUST NOT move the feed to BROKEN.
# result=error   -> fetch_log.ok = 0, `error` non-empty.
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

  # ── the MACHINE seam ── <raw>/.fetch/receipts.jsonl ───────────────────────
  # THE TRANSPORT FACTS RECORDED HERE ARE THE UPSTREAM ONES — the real status
  # code, the real byte count and the real transfer time of the MPSV increments,
  # not of the reduced file this script leaves on disk. normalize.py would
  # otherwise infer `http_status = 200 if nbytes > 0`, which is a fabricated
  # receipt: it cannot tell a 404 from a 403 from a feed that never ran.
  # Field names are exactly db.py's FETCHLOG_FIELDS so the merge needs no
  # translation. Lives in a SUBDIRECTORY because normalize.py's payload scan
  # keeps only os.path.isfile entries, so a directory can never be mistaken for
  # a feed payload.
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
parse_w() { # "<http_code> <size_download> <time_total>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# ── IDEMPOTENCE GATE ─────────────────────────────────────────────────────────
# The ledger's own dedup index is the "already produced" flag. A monthly
# aggregate is written once; re-running the fetcher must not re-download 19 MB to
# have normalize discard every record as a duplicate. Logged as `skipped`, which
# is the honest contract result: ok=1, parse_method none, no move toward BROKEN.
if [ -f "$SEEN" ] && grep -q "^mpsv-$MONTH-" "$SEEN" 2>/dev/null; then
  echo "== mpsv $MONTH: already in $SEEN — nothing to do"
  mf mpsv skipped 000 0 0 0 "$STARTED" "$OUTDIR" "month $MONTH already present in seen.txt"
  exit 0
fi

# ── WORK DIR: OUTSIDE THE REPO, AND IT IS DELETED ────────────────────────────
# This is where the personal data lives for the duration of the run. Not under
# data/raw/ — gitignored is not the same as absent, and data/raw/ is only pruned
# at 28 days. The trap covers the crash path; mpsv_reduce.py deletes it on the
# success path too.
WORK="$(mktemp -d "${TMPDIR:-/tmp}/lp-mpsv-$MONTH-XXXXXX")"
cleanup() { [ -n "${WORK:-}" ] && [ -d "$WORK" ] && rm -rf "$WORK"; }
trap cleanup EXIT INT TERM

TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; PRESENT=0; ABSENT=""; ERRS=""

# ── the two codelists ────────────────────────────────────────────────────────
# Occupation and region LABELS come from MPSV's published codelists, never from
# the postings' own free text. `pozadovanaProfese.cs` looks like a controlled
# vocabulary and is not: 19,204 distinct values across one month's 46,716 rows,
# two of them containing an email address.
for cl in cz-isco kraje; do
  parse_w "$(curl -fsSL -m 90 "$BASE/ciselniky/$cl.json" \
                  -o "$WORK/$cl.json" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))
  if [ "$W_CODE" != "200" ]; then
    echo "== codelist $cl: FAILED (HTTP $W_CODE)" >&2
    mf mpsv error "$W_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
       "codelist $cl: HTTP $W_CODE"
    exit 1
  fi
  TOT_BYTES=$((TOT_BYTES + W_BYTES))
done

# ── the month's daily increments ─────────────────────────────────────────────
DAYS="$(python3 -c "
import calendar, datetime, sys
y, m = (int(x) for x in '$MONTH'.split('-'))
for d in range(1, calendar.monthrange(y, m)[1] + 1):
    print(datetime.date(y, m, d).isoformat())")"
DAYS_EXPECTED="$(printf '%s\n' "$DAYS" | grep -c .)"

# HERE-STRING, not `echo … | while`: a piped while runs in a SUBSHELL, so every
# counter below would be discarded when the loop ended and the manifest row would
# read 0 bytes and 0 days. bash 3.2 has no `mapfile`.
while read -r d; do
  [ -n "${d:-}" ] || continue
  # `-f` refuses to store a non-2xx body; `--remove-on-error` deletes the partial
  # file; the explicit code test below is NOT redundant with either, because
  # --fail only trips at >= 400 and a 3xx served as the terminal response passes
  # it. MPSV redirects http->https and adds a trailing slash, so 3xx is live here.
  parse_w "$(curl -fsSL -m 120 "$INC/volna-mista-prirustek-$d.json.gz" \
                  -o "$WORK/$d.json.gz" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' 2>/dev/null || true)"
  TOT_MS=$((TOT_MS + W_MS))
  if [ "$W_CODE" = "200" ]; then
    LAST_CODE=200
    TOT_BYTES=$((TOT_BYTES + W_BYTES))
    PRESENT=$((PRESENT + 1))
  elif [ "$W_CODE" = "404" ]; then
    # EXPECTED ABSENCE, not a failure. 27.3% of calendar days have no file.
    ABSENT="${ABSENT:+$ABSENT,}$d"
  else
    LAST_CODE="$W_CODE"
    ERRS="$ERRS $d:HTTP-$W_CODE"
  fi
done <<EOF
$DAYS
EOF

ABSENT_N="$(printf '%s' "$ABSENT" | awk -F, 'BEGIN{n=0} {n=NF} END{print (length($0)?n:0)}')"
echo "== mpsv $MONTH: $PRESENT/$DAYS_EXPECTED day file(s), $ABSENT_N absent, $TOT_BYTES bytes"

if [ -n "$ERRS" ]; then
  mf mpsv error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "increment failures:$ERRS"
  exit 1
fi
if [ "$PRESENT" -eq 0 ]; then
  # Every day of the month absent is NOT expected absence — it is the whole
  # window gone, which is Mode B arriving all at once. Loud.
  mf mpsv error 404 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "no increment file for any of $DAYS_EXPECTED days in $MONTH"
  exit 1
fi

# ── reduce: privacy gates, then aggregate BEFORE materiality ────────────────
if python3 "$HERE/mpsv_reduce.py" \
     --work "$WORK" --month "$MONTH" --out "$OUT" \
     --isco "$WORK/cz-isco.json" --kraje "$WORK/kraje.json" \
     --worklist "$OUTDIR/.fetch/ares-worklist.txt" \
     --days-absent "$ABSENT" --days-expected "$DAYS_EXPECTED" \
     --upstream-bytes "$TOT_BYTES"; then
  ITEMS="$(python3 -c "
import json, sys
print(len(json.load(open('$OUT')).get('items', [])))" 2>/dev/null || echo 0)"
  NOVY="$(python3 -c "
import json
d = json.load(open('$OUT')); print(d.get('new_postings', 0))" 2>/dev/null || echo 0)"
  RAWROWS="$(python3 -c "
import json
d = json.load(open('$OUT')); print(d.get('raw_rows', 0))" 2>/dev/null || echo 0)"
  # `items` is the AGGREGATE count, because that is what normalize.py's yield
  # check counts. The raw-posting numbers ride on the note column instead of
  # being smuggled into items_fetched — fetch_hlidac.sh set the same precedent
  # after reporting the API's `total` instead of what landed on disk (§6.6b).
  CAND="$(python3 -c "
import json
d = json.load(open('$OUT'))
print(sum(1 for i in d.get('items', []) if i.get('kind') == 'employer'))" 2>/dev/null || echo 0)"
  # ITEMS IS WHAT THIS SCRIPT WROTE, and the note says which part of it is still
  # provisional. scripts/fetch_ares.sh removes any employer aggregate it cannot
  # clear, so the file can legitimately shrink after this row is written —
  # normalize.py counts the payload on disk for fetch_log, so the two never
  # disagree there. Saying it here stops the manifest reading like the
  # over-count fetch_hlidac.sh used to log (§6.6b).
  mf mpsv ok "$LAST_CODE" "$TOT_BYTES" "$ITEMS" "$TOT_MS" "$STARTED" "$OUT" \
     "coverage: $PRESENT of $DAYS_EXPECTED days ($ABSENT_N absent); $RAWROWS rows -> $NOVY novy -> $ITEMS aggregates written, of which $CAND are employer CANDIDATES pending scripts/fetch_ares.sh clearance"
  echo "== mpsv: $ITEMS aggregate(s) -> $OUT"
else
  rc=$?
  if [ "$rc" = "2" ]; then
    mf mpsv error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
       "AC-GDPR1 REFUSED: contact data survived the field allowlist — nothing written"
  else
    mf mpsv error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
       "mpsv_reduce.py exit $rc"
  fi
  exit 1
fi
