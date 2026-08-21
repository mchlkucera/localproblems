#!/usr/bin/env bash
# fetch_shoptet.sh — the Shoptet add-on marketplace, over its DECLARED SITEMAP.
#
# ══ WHY THIS SOURCE EXISTS AT ALL ════════════════════════════════════════════
# `gap` is the register's weakest score — 9 of 62 points, 23 of 31 records at
# zero — and the 2026-08-20 re-check found HALF the absence claims false. The
# reason is stated in data/CONVENTIONS.md: the corpus cannot see the
# competition. The nine incumbents that caused those de-ranks return zero hits
# across all 9,324 signals, because they are bootstrapped SMB software vendors
# who never raised and never bid for a public contract.
#
# No Czech state register maps "product category -> vendor list". ARES is
# IČO -> legal facts, carries no website and no product text, and refuses above
# 1,000 results with no pagination. The one surface that names a PRODUCT and
# its VENDOR in Czech is the e-commerce add-on marketplace.
#
# THIS IS NOT SPECULATIVE. p-0028 was de-ranked on 2026-08-20 by Hlídač Slev
# (JARABOT), found BY HAND at https://doplnky.shoptet.cz/hlidac-slev — a page
# in the sitemap this script reads.
#
# ══ ROBOTS.TXT, READ 2026-08-21 12:16 UTC, VERBATIM ══════════════════════════
#   User-agent: *
#   Disallow:
#   Disallow: /prihlaseni
#   Sitemap: https://doplnky.shoptet.cz/sitemap.xml
#
# The first `Disallow:` is empty — crawling is explicitly permitted. NOTE the
# SECOND LINE, which the brief did not carry: `/prihlaseni` (the login page) IS
# disallowed. Nothing here requests it, and the check below re-reads robots.txt
# on every run and ABORTS if any path we are about to fetch has become
# disallowed. Permission can change; it is the basis for the whole build, so it
# is verified rather than remembered.
#
# ══ WHAT THE SITEMAP DECLARES (measured 2026-08-21, 57,698 bytes) ════════════
#   593 <url> entries =  404 add-on detail pages
#                     +  179 /katalog?partner=<id> vendor pages
#                     +    9 /category/<slug> pages
#                     +    1 homepage
# The brief expected "~584 add-on pages"; the true split is 404 add-ons and 179
# vendors, and the 404 matches the homepage's own "~402 active add-ons" counter
# far better. Install counts are NOT published anywhere and none is invented.
#
# ══ CONDITIONAL GET: WHAT THE SERVER ACTUALLY OFFERS ═════════════════════════
# MEASURED: https://doplnky.shoptet.cz/sitemap.xml returns NO ETag and NO
# Last-Modified (server: openresty; only content-type, x-frame-options,
# set-cookie, vary, alt-svc). If-None-Match therefore has nothing to send. The
# header is still sent when a cached ETag exists — free, and correct the day
# they add one — but the working mechanism is a CONTENT HASH: the sitemap is
# 57 KB, so one cheap request settles whether anything changed. A quiet day
# costs that one request and exits `skipped`. Stated plainly rather than
# claiming a conditional GET that this host does not support.
#
# ══ MODE-A ══════════════════════════════════════════════════════════════════
# MEASURED on this host: an unknown path returns HTTP 404 with a 37,997-byte
# HTML body — the ~38,000 bytes the brief warned about, but at a HONEST status.
# The 200-shaped version of this trap is real and lives on the OTHER
# marketplace (see fetch_upgates.sh), so the body contract is enforced here
# too, and step 3 below PROVES it live on every run by fetching a deliberately
# bad slug and requiring the contract to reject it. A status check is never the
# gate.
#
# Usage: scripts/fetch_shoptet.sh [outdir]
set -uo pipefail
export LC_NUMERIC=C

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
UA="localproblems-register/1.0 (public register; corrections@localproblems.org)"
HOST="https://doplnky.shoptet.cz"

SLEEP="${SHOPTET_SLEEP:-1.0}"          # between detail requests
MAX_DETAILS="${SHOPTET_MAX_DETAILS:-450}"
REFRESH_DAYS="${SHOPTET_REFRESH_DAYS:-30}"
CACHE="${SHOPTET_CACHE:-data/raw/.cache}"
LOOKUP_DIR="${LOOKUP_DIR:-data/lookup}"
mkdir -p "$CACHE" "$LOOKUP_DIR"

HERE="$(cd "$(dirname "$0")" && pwd)"
EXTRACT="$HERE/shoptet_upgates_extract.py"
[ -f "$EXTRACT" ] || { echo "fetch_shoptet: missing $EXTRACT" >&2; exit 2; }
command -v jq >/dev/null 2>&1 || { echo "fetch_shoptet: jq is required" >&2; exit 2; }

RAWD="$OUTDIR/.fetch/shoptet"; mkdir -p "$RAWD"
OUT="$OUTDIR/shoptet-addons.jsonl"
VOUT="$OUTDIR/shoptet-vendors.jsonl"
LOOKUP="$LOOKUP_DIR/cz-eshop-addons.jsonl"
LOOKUP_V="$LOOKUP_DIR/cz-eshop-vendors.jsonl"
TMPD="${TMPDIR:-/tmp}/shoptet.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT

# ── run manifest ── identical seam to scripts/fetch_vestbee.sh ───────────────
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
  mkdir -p "$OUTDIR/.fetch"
  jq -nc --arg run_id "$RUN_ID" --arg feed_key "$1" --arg result "$2" \
         --arg http "$3" --arg bytes "$4" --arg items "$5" --arg ms "$6" \
         --arg started "$7" --arg raw "$8" --arg err "${9:-}" \
    '{run_id:$run_id, feed_key:$feed_key, started_at:$started,
      finished_at:(now|todateiso8601),
      http_status:(if ($http|length)==0 or $http=="000" then null else ($http|tonumber) end),
      bytes:(if ($bytes|length)==0 then null else ($bytes|tonumber) end),
      items_fetched:(if ($items|length)==0 then null else ($items|tonumber) end),
      items_kept:null, yield_anomaly:null,
      parse_method:(if $result=="skipped" then "none" else null end),
      runtime_ms:(if ($ms|length)==0 then null else ($ms|tonumber) end),
      ok:(if $result=="error" then 0 else 1 end),
      error:(if ($err|length)==0 then null else $err end),
      raw_path:(if ($raw|length)==0 then null else $raw end),
      result:$result}' >> "$OUTDIR/.fetch/receipts.jsonl" 2>/dev/null
}

# FIELD ORDER IS LOAD-BEARING — content_type contains a space, so it goes LAST.
parse_w() {
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_URL="${4:-}"; W_CT="${5:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

# The final status out of a `--retry` write-out. TWO traps, both measured here:
#   1. `--retry` emits one write-out PER ATTEMPT, so a retried request returns
#      "000000" and a `!= 200` test reads a code that never existed.
#   2. `tail -c 3` on a value that has passed through a pipe stage which appends
#      a newline takes that newline as one of its three bytes and yields "00" —
#      which is exactly how an 83-of-83 zero-yield run happened in this repo
#      after the fix for trap 1. Strip whitespace first, then take three.
last_code() {
  c="$(printf '%s' "${1:-}" | tr -d '[:space:]')"
  c="$(printf '%s' "$c" | tail -c 3)"
  printf '%s' "${c:-000}"
}

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TOT_BYTES=0; TOT_MS=0; ERRS=""
FETCHED=0; KEPT=0; REJECTED=0; GDPR_DROPPED=0

# ══ 1. robots.txt — the permission this whole build rests on ═════════════════
ROBOTS="$RAWD/robots.txt"
parse_w "$(curl -fsSL -m 30 --retry 2 --retry-delay 5 --remove-on-error -A "$UA" -o "$ROBOTS" \
  -w '%{http_code} %{size_download} %{time_total} %{url_effective} %{content_type}' \
  "$HOST/robots.txt" 2>/dev/null || true)"
TOT_MS=$((TOT_MS + W_MS)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
if [ "$W_CODE" != "200" ]; then
  echo "FAILED robots.txt (HTTP $W_CODE) — refusing to crawl without a readable policy."
  mf shoptet error "$W_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "robots:HTTP-$W_CODE"
  exit 1
fi
echo "OK  robots.txt ($W_BYTES bytes):"
sed 's/^/      | /' "$ROBOTS"
# Every non-empty Disallow under `User-agent: *` is a real prohibition. We fetch
# /, /sitemap.xml, /katalog and /<addon-slug>; a rule matching any of those
# stops the run. `/prihlaseni` matches none of them.
BLOCKED=""
while IFS= read -r rule; do
  [ -n "$rule" ] || continue
  case "/katalog" in "$rule"*) BLOCKED="$BLOCKED /katalog($rule)";; esac
  case "/sitemap.xml" in "$rule"*) BLOCKED="$BLOCKED /sitemap.xml($rule)";; esac
  [ "$rule" = "/" ] && BLOCKED="$BLOCKED everything($rule)"
done <<EOF
$(tr -d '\r' < "$ROBOTS" | awk 'tolower($1)=="user-agent:"{ua=($2=="*")} ua && tolower($1)=="disallow:" && NF>1 {print $2}')
EOF
if [ -n "$BLOCKED" ]; then
  echo "ABORT — robots.txt now disallows paths this fetcher uses:$BLOCKED"
  mf shoptet error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "robots:disallowed:$BLOCKED"
  exit 1
fi

# ══ 2. the sitemap — the declared interface ══════════════════════════════════
SM="$RAWD/sitemap.xml"
ETAG_F="$CACHE/shoptet-sitemap.etag"
HASH_F="$CACHE/shoptet-sitemap.sha256"
COND=""; [ -f "$ETAG_F" ] && COND="$(cat "$ETAG_F" 2>/dev/null)"
parse_w "$(curl -sSL -m 90 --retry 2 --retry-delay 5 -A "$UA" -o "$SM" \
  ${COND:+-H "If-None-Match: $COND"} -D "$TMPD/sm.h" \
  -w '%{http_code} %{size_download} %{time_total} %{url_effective} %{content_type}' \
  "$HOST/sitemap.xml" 2>/dev/null || true)"
TOT_MS=$((TOT_MS + W_MS))
if [ "$W_CODE" = "304" ]; then
  echo "== shoptet: 304 Not Modified — sitemap unchanged, nothing to crawl."
  mf shoptet skipped 304 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "304 Not Modified"
  exit 0
fi
if [ "$W_CODE" != "200" ]; then
  echo "FAILED sitemap.xml (HTTP $W_CODE)"
  mf shoptet error "$W_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "sitemap:HTTP-$W_CODE"
  exit 1
fi
if ! head -c 300 "$SM" | grep -q '<urlset\|<?xml'; then
  echo "FAILED sitemap.xml — MODE-A: HTTP 200 but the body is not XML ($W_BYTES bytes, $W_CT)."
  echo "       first 120 bytes: $(head -c 120 "$SM" | tr -d '\n')"
  mf shoptet error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "sitemap:mode-a-not-xml"
  exit 1
fi
TOT_BYTES=$((TOT_BYTES + W_BYTES))
grep -i '^etag:' "$TMPD/sm.h" | tail -1 | tr -d '\r' | awk '{print $2}' > "$ETAG_F" 2>/dev/null || true
# MEASURED: this host sends no ETag, so the file lands empty. An empty
# If-None-Match header is worse than none (some origins answer it with a 412),
# hence the truncate-to-nothing plus the `${COND:+...}` guard above. `rm` is
# blocked in this environment; `: >` is the same effect for a cache file.
[ -s "$ETAG_F" ] || : > "$ETAG_F"

grep -oE '<loc>[^<]+</loc>' "$SM" | sed -E 's#</?loc>##g' > "$TMPD/urls.txt"
NURL=$(wc -l < "$TMPD/urls.txt" | tr -d ' ')
grep -vE '/category/|[?]partner|^https://doplnky\.shoptet\.cz/$' "$TMPD/urls.txt" > "$TMPD/addons.txt"
NADDON=$(wc -l < "$TMPD/addons.txt" | tr -d ' ')
NPARTNER=$(grep -cE '[?]partner' "$TMPD/urls.txt" | tr -d ' ')
NCAT=$(grep -cE '/category/' "$TMPD/urls.txt" | tr -d ' ')
echo "OK  sitemap.xml ($W_BYTES bytes): $NURL urls = $NADDON add-ons + $NPARTNER vendors + $NCAT categories"

SM_HASH="$(shasum -a 256 "$SM" | awk '{print $1}')"
OLD_HASH=""; [ -f "$HASH_F" ] && OLD_HASH="$(cat "$HASH_F" 2>/dev/null)"

# ══ 3. LIVE MODE-A ASSERTION — before a single record is trusted ═════════════
# The contract is not a comment; it is executed against a page we KNOW is not an
# add-on. If it ever accepts one, the run stops rather than filling the lookup
# table with not-found bodies.
BADURL="$HOST/tento-doplnek-neexistuje-xyzzy-42"
BADCODE=$(curl -sSL -m 30 -A "$UA" -o "$TMPD/mode-a.html" -w '%{http_code}' "$BADURL" 2>/dev/null || echo 000)
BADBYTES=$(wc -c < "$TMPD/mode-a.html" | tr -d ' ')
if python3 "$EXTRACT" shoptet-detail "$TMPD/mode-a.html" "$BADURL" >/dev/null 2>&1; then
  echo "ABORT — the required_fields contract ACCEPTED a known not-found page"
  echo "        ($BADURL -> HTTP $BADCODE, $BADBYTES bytes). Refusing to crawl."
  mf shoptet error "$BADCODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "mode-a:contract-accepted-notfound"
  exit 1
fi
echo "OK  mode-A probe: $BADURL -> HTTP $BADCODE, $BADBYTES bytes, contract REJECTS it"
sleep "$SLEEP"

# ══ 4. /katalog — the DECLARED vendor table, in one request ══════════════════
# <select name="partnerId"> is the marketplace's own list of its partners.
# Reading a declared control beats crawling 179 partner pages to infer it.
KAT="$RAWD/katalog.html"
parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error -A "$UA" -o "$KAT" \
  -w '%{http_code} %{size_download} %{time_total} %{url_effective} %{content_type}' \
  "$HOST/katalog" 2>/dev/null || true)"
TOT_MS=$((TOT_MS + W_MS)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
VSUM='{"vendors":0}'
# RUNTIME ONLY, under $TMPD, wiped by the trap: the suppressed-author names, so
# the prose redactor can strip them out of OTHER vendors' marketing copy. It
# must never become a durable file — see redact_names() for why the hole exists.
NAMES="$TMPD/suppressed-names.txt"
if [ "$W_CODE" = "200" ]; then
  VSUM=$(python3 "$EXTRACT" shoptet-catalog "$KAT" "$VOUT" "$NAMES" 2>/dev/null) || {
    ERRS="$ERRS katalog:parse-failed"; VSUM='{"vendors":0}'; }
  echo "OK  /katalog ($W_BYTES bytes): $VSUM"
else
  ERRS="$ERRS katalog:HTTP-$W_CODE"
  echo "WARN /katalog HTTP $W_CODE — vendor ids will be absent, add-ons still crawl."
fi
sleep "$SLEEP"

# ══ 5. incremental selection ════════════════════════════════════════════════
# Only slugs the durable lookup table does not already carry (or whose row is
# older than REFRESH_DAYS) are fetched. First run pays for all of them; every
# later run pays for the delta.
CUT="$(python3 -c "import datetime,sys;print((datetime.date.today()-datetime.timedelta(days=int(sys.argv[1]))).isoformat())" "$REFRESH_DAYS")"
: > "$TMPD/have.txt"
if [ -f "$LOOKUP" ]; then
  jq -r --arg cut "$CUT" 'select(.marketplace=="shoptet")
    | select((.fetched_at // "0000")[0:10] >= $cut) | .url' "$LOOKUP" \
    2>/dev/null | sort -u > "$TMPD/have.txt" || : > "$TMPD/have.txt"
fi
sort -u "$TMPD/addons.txt" > "$TMPD/want.txt"
comm -23 "$TMPD/want.txt" "$TMPD/have.txt" > "$TMPD/todo.txt"
NHAVE=$(wc -l < "$TMPD/have.txt" | tr -d ' ')
NTODO=$(wc -l < "$TMPD/todo.txt" | tr -d ' ')
head -n "$MAX_DETAILS" "$TMPD/todo.txt" > "$TMPD/todo.capped.txt"
NCAP=$(wc -l < "$TMPD/todo.capped.txt" | tr -d ' ')
echo "    incremental: $NADDON declared · $NHAVE fresh in $LOOKUP (>= $CUT) · $NTODO to fetch · $NCAP after cap $MAX_DETAILS"

if [ "$NCAP" -eq 0 ]; then
  if [ "$SM_HASH" = "$OLD_HASH" ]; then
    echo "== shoptet: sitemap byte-identical to last run and every add-on is fresh — 0 fetches."
    mf shoptet skipped 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "sitemap unchanged (sha256) + lookup table fresh"
  else
    echo "== shoptet: sitemap changed but every add-on row is still within ${REFRESH_DAYS}d — 0 fetches."
    mf shoptet ok 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "yield: 0 new slugs"
  fi
  printf '%s' "$SM_HASH" > "$HASH_F"
  : > "$OUT"
  exit 0
fi

# ══ 6. detail crawl ═════════════════════════════════════════════════════════
: > "$TMPD/rows.jsonl"
: > "$TMPD/rejects.txt"
NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# A here-string, not a pipe: a piped `while` runs in a subshell on bash 3.2 and
# every counter below would be discarded at the end of the loop.
while IFS= read -r url; do
  [ -n "$url" ] || continue
  slug="$(printf '%s' "$url" | sed -E 's#^https?://[^/]+/##; s#/$##')"
  page="$TMPD/page.html"
  # MEASURED: 7 Upgates and 1 Shoptet add-on were logged as `HTTP-000000` on
  # the first full run — see last_code() above for both halves of that trap.
  dcode=$(last_code "$(curl -sSL -m 45 --retry 1 --retry-delay 5 -A "$UA" \
          -o "$page" -w '%{http_code}' "$url" 2>/dev/null)")
  FETCHED=$((FETCHED + 1))
  if [ "$dcode" != "200" ] || [ ! -s "$page" ]; then
    printf '%s\tHTTP-%s\n' "$slug" "$dcode" >> "$TMPD/rejects.txt"
    REJECTED=$((REJECTED + 1))
    sleep "$SLEEP"; continue
  fi
  if rec=$(python3 "$EXTRACT" shoptet-detail "$page" "$url" "$VOUT" "$NAMES" 2>"$TMPD/err.txt"); then
    printf '%s' "$rec" | jq -c --arg t "$NOW" --argjson s "$dcode" \
      '. + {fetched_at:$t, http_status:$s}' >> "$TMPD/rows.jsonl"
    KEPT=$((KEPT + 1))
  else
    rc=$?
    why="$(tr -d '\n' < "$TMPD/err.txt" | cut -c1-160)"
    printf '%s\t%s\n' "$slug" "$why" >> "$TMPD/rejects.txt"
    if [ "$rc" -eq 3 ]; then GDPR_DROPPED=$((GDPR_DROPPED + 1)); else REJECTED=$((REJECTED + 1)); fi
  fi
  sleep "$SLEEP"
done < "$TMPD/todo.capped.txt"

# The extractor's own GDPR gate runs again over the whole batch on the way out —
# belt and braces, because this is the write path into a committed file. FAIL
# CLOSED: `merge` is the only thing that writes $OUT, so a failed merge leaves
# an EMPTY file rather than a batch that skipped the gate.
: > "$OUT"
MSUM=$(python3 "$EXTRACT" merge "$OUT" "$TMPD/rows.jsonl" 2>"$TMPD/merr.txt") || ERRS="$ERRS out:merge-failed"
BATCH_GDPR=$(printf '%s' "$MSUM" | jq -r '.gdpr_dropped // 0' 2>/dev/null || echo 0)
GDPR_DROPPED=$((GDPR_DROPPED + BATCH_GDPR))
[ -s "$TMPD/merr.txt" ] && sed 's/^/    /' "$TMPD/merr.txt"

# ══ 7. the durable lookup table ═════════════════════════════════════════════
# data/raw/ is gitignored and pruned at 28 days, so a corpus that lives only
# there evaporates a month after it is built. The merged table is committed.
python3 "$EXTRACT" merge "$LOOKUP.tmp" "$LOOKUP" "$OUT" > "$TMPD/lsum.txt" 2>&1 \
  && mv "$LOOKUP.tmp" "$LOOKUP" \
  || { ERRS="$ERRS lookup:merge-failed"; mv "$LOOKUP.tmp" "$TMPD/lookup.failed" 2>/dev/null || true; }
if [ -s "$VOUT" ]; then
  cat "$VOUT" > "$TMPD/v.jsonl"
  [ -f "$LOOKUP_V" ] && cat "$LOOKUP_V" >> "$TMPD/v.jsonl"
  sort -u "$TMPD/v.jsonl" > "$LOOKUP_V"
fi
printf '%s' "$SM_HASH" > "$HASH_F"

# ══ 8. items FETCHED vs items KEPT — a zero-yield run must be LOUD ═══════════
LTOT=$(wc -l < "$LOOKUP" 2>/dev/null | tr -d ' '); [ -n "$LTOT" ] || LTOT=0
echo "== shoptet: $NADDON declared -> $NCAP selected -> $FETCHED fetched -> $KEPT kept"
echo "    rejected by contract: $REJECTED · dropped by GDPR gate: $GDPR_DROPPED"
echo "    lookup table now holds $LTOT rows -> $LOOKUP"
if [ -s "$TMPD/rejects.txt" ]; then
  # The reject list is EVIDENCE, not console noise: the first full run's 28
  # Shoptet rejects turned out to be one over-tight regex and one real family
  # of pages, and that was only visible because the reasons were readable. The
  # console prints the top 8; the file keeps all of them.
  cp "$TMPD/rejects.txt" "$OUTDIR/.fetch/shoptet-rejects.tsv"
  echo "    reject reasons (full list: $OUTDIR/.fetch/shoptet-rejects.tsv):"
  awk -F'\t' '{sub(/^REJECT [^ ]+: /,"",$2); print $2}' "$TMPD/rejects.txt" \
    | sed -E 's/\(.*\)//' | sort | uniq -c | sort -rn | head -8 | sed 's/^/      /'
fi
# ZERO YIELD IS NOT ALWAYS SILENCE, and conflating the two costs the alarm its
# credibility. Once the corpus is built, every later run re-offers the same
# handful of permanently-rejected slugs — 2 CMS pages in the sitemap and 10
# add-ons whose prose prints a phone number — so `KEPT == 0` becomes the STEADY
# STATE and a fetcher that exits 1 on it cries wolf every single run.
# SCRIPTED-SILENT is the case where the corpus itself is empty.
LMKT=$(grep -c '"marketplace": "shoptet"' "$LOOKUP" 2>/dev/null | tr -d ' '); [ -n "$LMKT" ] || LMKT=0
if [ "$KEPT" -eq 0 ] && [ "$LMKT" -eq 0 ]; then
  echo "    SCRIPTED-SILENT: the fetch worked, nothing landed, and the corpus is EMPTY."
  mf shoptet error 200 "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" "yield: 0 records from $FETCHED fetches, corpus empty"
  exit 1
fi
if [ "$KEPT" -eq 0 ]; then
  echo "    0 new records: all $FETCHED selected slugs are permanent rejects; $LMKT shoptet rows already held."
  mf shoptet ok 200 "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" \
     "yield: 0 new; $REJECTED contract-rejected, $GDPR_DROPPED gdpr-dropped, corpus holds $LMKT"
  echo "    wrote $OUT and $VOUT"
  exit 0
fi
if [ -n "$ERRS" ]; then
  mf shoptet ok 200 "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS"
else
  mf shoptet ok 200 "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "    wrote $OUT and $VOUT"
