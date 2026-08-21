#!/usr/bin/env bash
# fetch_upgates.sh — the Upgates add-on marketplace. NO SITEMAP; the declared
# interface here is the category navigation, so that is what is read.
#
# Companion to scripts/fetch_shoptet.sh; the rationale for the whole surface is
# written up there and not repeated. What differs on this host is worth stating,
# because both differences are traps.
#
# ══ ROBOTS.TXT, READ 2026-08-21 12:16 UTC ════════════════════════════════════
#   HTTP/1.1 200 OK · Content-Length: 0 · Content-Type: text/plain
#   Last-Modified: Mon, 12 Jan 2026 05:49:41 GMT · ETag: "0-6482a70f20740"
#
# The file is EMPTY — zero bytes, no `User-agent`, no `Disallow`, and no
# `Sitemap:` line. An empty robots.txt is unrestricted by the standard, so
# crawling is permitted; it is recorded as "empty, therefore permitted" rather
# than "permitted", because the two are different facts and only the first is
# what was observed. The check below re-reads it every run and aborts if
# directives appear.
#
# ══ TRAP 1: THERE IS NO SITEMAP ══════════════════════════════════════════════
# MEASURED: https://doplnky.upgates.cz/sitemap.xml -> HTTP 404, 14,444 bytes of
# HTML. So the sitemap-first rule cannot be followed here and is not pretended
# at. The declared surface is the category nav rendered on every page. MEASURED
# across it: 10 category links, of which /ai-1 is a 404 (linked but dead), and
# the 9 live listings plus the homepage yield 221 distinct /detail/<slug> URLs
# — matching the "200+ integrations" the brief expected. Every tile is
# SERVER-RENDERED: no JS is needed for the enumeration.
#
# ══ TRAP 2: THE MODE-A TRAP IS REAL HERE, AND IT IS THE 200-SHAPED ONE ═══════
# MEASURED, and this is the finding that justifies the whole required_fields
# contract:
#
#   GET /detail/tento-doplnek-neexistuje-xyzzy-42
#     -> HTTP 200 · 102,039 bytes · text/html
#     -> sha256 3272a51e2079f26b0ef1f27b966ec2e0d3e5c32e4dbe64c33c7f3758b13d8123
#   GET /
#     -> HTTP 200 · 102,039 bytes
#     -> sha256 3272a51e2079f26b0ef1f27b966ec2e0d3e5c32e4dbe64c33c7f3758b13d8123
#
# BYTE-IDENTICAL. An unknown add-on slug silently serves the homepage at status
# 200. A fetcher checking the status code stores the homepage as an add-on. A
# fetcher that also reads `<h1 itemprop="name">` gets the string "Marketplace"
# and writes a plausible-looking record for every typo. What settles it is
# IDENTITY — the page's own og:url must be the resource we asked for — and the
# probe in step 3 re-proves that live on every run before anything is trusted.
#
# ══ CONDITIONAL GET ══════════════════════════════════════════════════════════
# The listing pages carry no ETag we can rely on, so the same content-hash
# mechanism as the Shoptet fetcher is used over the concatenated listings: an
# unchanged marketplace costs 10 listing requests and zero detail requests.
# That is more than the one request the brief asked for, and it is the floor
# this host allows without a sitemap. Said plainly rather than glossed.
#
# Usage: scripts/fetch_upgates.sh [outdir]
set -uo pipefail
export LC_NUMERIC=C

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
UA="localproblems-register/1.0 (public register; corrections@localproblems.org)"
HOST="https://doplnky.upgates.cz"

SLEEP="${UPGATES_SLEEP:-1.0}"
MAX_DETAILS="${UPGATES_MAX_DETAILS:-260}"
REFRESH_DAYS="${UPGATES_REFRESH_DAYS:-30}"
CACHE="${UPGATES_CACHE:-data/raw/.cache}"
LOOKUP_DIR="${LOOKUP_DIR:-data/lookup}"
mkdir -p "$CACHE" "$LOOKUP_DIR"

HERE="$(cd "$(dirname "$0")" && pwd)"
EXTRACT="$HERE/shoptet_upgates_extract.py"
[ -f "$EXTRACT" ] || { echo "fetch_upgates: missing $EXTRACT" >&2; exit 2; }
command -v jq >/dev/null 2>&1 || { echo "fetch_upgates: jq is required" >&2; exit 2; }

RAWD="$OUTDIR/.fetch/upgates"; mkdir -p "$RAWD"
LISTD="$RAWD/listings"; mkdir -p "$LISTD"
OUT="$OUTDIR/upgates-addons.jsonl"
LOOKUP="$LOOKUP_DIR/cz-eshop-addons.jsonl"
TMPD="${TMPDIR:-/tmp}/upgates.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT

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

parse_w() {
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_URL="${4:-}"; W_CT="${5:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

# The final status out of a `--retry` write-out. TWO traps, both measured here:
#   1. `--retry` emits one write-out PER ATTEMPT, so a retried request returns
#      "000000" and a `!= 200` test reads a code that never existed.
#   2. `tail -c 3` on a value that has passed through `cut` takes the trailing
#      NEWLINE as one of its three bytes and yields "00" — which is exactly how
#      an 83-of-83 zero-yield run happened after the fix for trap 1.
# Strip whitespace first, then take the last three characters.
last_code() {
  c="$(printf '%s' "${1:-}" | tr -d '[:space:]')"
  c="$(printf '%s' "$c" | tail -c 3)"
  printf '%s' "${c:-000}"
}

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TOT_BYTES=0; TOT_MS=0; ERRS=""
FETCHED=0; KEPT=0; REJECTED=0; GDPR_DROPPED=0

# ══ 1. robots.txt ═══════════════════════════════════════════════════════════
ROBOTS="$RAWD/robots.txt"
parse_w "$(curl -fsSL -m 30 --retry 2 --retry-delay 5 --remove-on-error -A "$UA" -o "$ROBOTS" \
  -w '%{http_code} %{size_download} %{time_total} %{url_effective} %{content_type}' \
  "$HOST/robots.txt" 2>/dev/null || true)"
TOT_MS=$((TOT_MS + W_MS)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
if [ "$W_CODE" != "200" ]; then
  echo "FAILED robots.txt (HTTP $W_CODE) — refusing to crawl without a readable policy."
  mf upgates error "$W_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "robots:HTTP-$W_CODE"
  exit 1
fi
RB=$(wc -c < "$ROBOTS" | tr -d ' ')
if [ "$RB" -eq 0 ]; then
  echo "OK  robots.txt: 0 bytes — no directives at all, therefore unrestricted."
else
  echo "OK  robots.txt ($RB bytes):"; sed 's/^/      | /' "$ROBOTS"
fi
BLOCKED=""
while IFS= read -r rule; do
  [ -n "$rule" ] || continue
  case "/detail/x" in "$rule"*) BLOCKED="$BLOCKED /detail($rule)";; esac
  [ "$rule" = "/" ] && BLOCKED="$BLOCKED everything($rule)"
done <<EOF
$(tr -d '\r' < "$ROBOTS" | awk 'tolower($1)=="user-agent:"{ua=($2=="*")} ua && tolower($1)=="disallow:" && NF>1 {print $2}')
EOF
if [ -n "$BLOCKED" ]; then
  echo "ABORT — robots.txt now disallows paths this fetcher uses:$BLOCKED"
  mf upgates error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "robots:disallowed:$BLOCKED"
  exit 1
fi

# ══ 2. enumerate over the DECLARED category nav ══════════════════════════════
# The category slugs are read out of the homepage's own navigation rather than
# hard-coded, so a renamed or added category is followed instead of missed. The
# homepage is fetched first for exactly that reason.
HOMEPG="$LISTD/home.html"
parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error -A "$UA" -o "$HOMEPG" \
  -w '%{http_code} %{size_download} %{time_total} %{url_effective} %{content_type}' \
  "$HOST/" 2>/dev/null || true)"
TOT_MS=$((TOT_MS + W_MS)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
if [ "$W_CODE" != "200" ] || [ ! -s "$HOMEPG" ]; then
  echo "FAILED homepage (HTTP $W_CODE) — no sitemap exists, so this is the only entry point."
  mf upgates error "$W_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "home:HTTP-$W_CODE"
  exit 1
fi
if ! grep -q 'addon-item' "$HOMEPG"; then
  echo "FAILED homepage — MODE-A: HTTP 200 but no addon tiles ($W_BYTES bytes, $W_CT)."
  mf upgates error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "home:mode-a-no-tiles"
  exit 1
fi
echo "OK  homepage ($W_BYTES bytes)"

grep -oE 'href="/[a-z0-9][a-z0-9\-]{3,}"' "$HOMEPG" \
  | sed -E 's#href="/##; s#"##' \
  | grep -vE '^(detail|images|css|js|favicon)' | sort -u > "$TMPD/cats.txt"
NCATS=$(wc -l < "$TMPD/cats.txt" | tr -d ' ')
echo "    category nav declares $NCATS listing slugs"
sleep "$SLEEP"

CAT_OK=0; CAT_BAD=0
while IFS= read -r c; do
  [ -n "$c" ] || continue
  ccode=$(curl -sSL -m 60 --retry 1 --retry-delay 5 -A "$UA" -o "$LISTD/cat-$c.html" \
          -w '%{http_code}' "$HOST/$c" 2>/dev/null || echo 000)
  if [ "$ccode" = "200" ] && grep -q 'addon-item' "$LISTD/cat-$c.html"; then
    CAT_OK=$((CAT_OK + 1))
  else
    # A dead nav link is a fact about the site, not a failure of the run:
    # MEASURED, /ai-1 is linked in the nav and returns 404.
    : > "$LISTD/cat-$c.html"
    CAT_BAD=$((CAT_BAD + 1))
    echo "    listing /$c -> HTTP $ccode (no tiles) — skipped"
  fi
  sleep "$SLEEP"
done < "$TMPD/cats.txt"
echo "OK  listings: $CAT_OK usable, $CAT_BAD dead"

python3 "$EXTRACT" upgates-listing "$LISTD" "$TMPD/tiles.jsonl" > "$TMPD/lsum.txt" 2>&1 \
  || { echo "FAILED listing parse"; cat "$TMPD/lsum.txt"; \
       mf upgates error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "listing:parse-failed"; exit 1; }
NADDON=$(wc -l < "$TMPD/tiles.jsonl" | tr -d ' ')
echo "    tiles: $NADDON distinct add-ons across $CAT_OK listings"

LIST_HASH="$(cat "$LISTD"/*.html 2>/dev/null | shasum -a 256 | awk '{print $1}')"
HASH_F="$CACHE/upgates-listings.sha256"
OLD_HASH=""; [ -f "$HASH_F" ] && OLD_HASH="$(cat "$HASH_F" 2>/dev/null)"

# ══ 3. LIVE MODE-A ASSERTION ════════════════════════════════════════════════
BADURL="$HOST/detail/tento-doplnek-neexistuje-xyzzy-42"
BADCODE=$(curl -sSL -m 30 -A "$UA" -o "$TMPD/mode-a.html" -w '%{http_code}' "$BADURL" 2>/dev/null || echo 000)
BADBYTES=$(wc -c < "$TMPD/mode-a.html" | tr -d ' ')
BADSHA=$(shasum -a 256 "$TMPD/mode-a.html" | awk '{print $1}')
HOMESHA=$(shasum -a 256 "$HOMEPG" | awk '{print $1}')
if python3 "$EXTRACT" upgates-detail "$TMPD/mode-a.html" "$BADURL" >/dev/null 2>&1; then
  echo "ABORT — the required_fields contract ACCEPTED a known not-found page"
  echo "        ($BADURL -> HTTP $BADCODE, $BADBYTES bytes). Refusing to crawl."
  mf upgates error "$BADCODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "mode-a:contract-accepted-notfound"
  exit 1
fi
echo "OK  mode-A probe: HTTP $BADCODE, $BADBYTES bytes, contract REJECTS it"
if [ "$BADSHA" = "$HOMESHA" ]; then
  echo "    (and the body is sha256-identical to the homepage — the 200-shaped trap, live)"
fi
sleep "$SLEEP"

# ══ 4. incremental selection ════════════════════════════════════════════════
CUT="$(python3 -c "import datetime,sys;print((datetime.date.today()-datetime.timedelta(days=int(sys.argv[1]))).isoformat())" "$REFRESH_DAYS")"
jq -r '"'"$HOST"'/detail/" + .slug' "$TMPD/tiles.jsonl" | sort -u > "$TMPD/want.txt"
: > "$TMPD/have.txt"
if [ -f "$LOOKUP" ]; then
  jq -r --arg cut "$CUT" 'select(.marketplace=="upgates")
    | select((.fetched_at // "0000")[0:10] >= $cut) | .url' "$LOOKUP" \
    2>/dev/null | sort -u > "$TMPD/have.txt" || : > "$TMPD/have.txt"
fi
comm -23 "$TMPD/want.txt" "$TMPD/have.txt" > "$TMPD/todo.txt"
NHAVE=$(wc -l < "$TMPD/have.txt" | tr -d ' ')
NTODO=$(wc -l < "$TMPD/todo.txt" | tr -d ' ')
head -n "$MAX_DETAILS" "$TMPD/todo.txt" > "$TMPD/todo.capped.txt"
NCAP=$(wc -l < "$TMPD/todo.capped.txt" | tr -d ' ')
echo "    incremental: $NADDON declared · $NHAVE fresh (>= $CUT) · $NTODO to fetch · $NCAP after cap $MAX_DETAILS"

if [ "$NCAP" -eq 0 ]; then
  if [ "$LIST_HASH" = "$OLD_HASH" ]; then
    echo "== upgates: listings byte-identical to last run and every add-on is fresh — 0 detail fetches."
    mf upgates skipped 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "listings unchanged (sha256) + lookup table fresh"
  else
    echo "== upgates: listings changed but every add-on row is still within ${REFRESH_DAYS}d — 0 detail fetches."
    mf upgates ok 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "yield: 0 new slugs"
  fi
  printf '%s' "$LIST_HASH" > "$HASH_F"
  : > "$OUT"
  exit 0
fi

# ══ 5. detail crawl ═════════════════════════════════════════════════════════
: > "$TMPD/rows.jsonl"; : > "$TMPD/rejects.txt"
NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# here-string, not a pipe — bash 3.2 subshells discard the counters.
while IFS= read -r url; do
  [ -n "$url" ] || continue
  slug="${url##*/}"
  page="$TMPD/page.html"
  wout=$(curl -sSL -m 45 --retry 1 --retry-delay 5 -A "$UA" -o "$page" \
         -w '%{http_code}\t%{url_effective}\n' "$url" 2>/dev/null)
  dcode=$(last_code "$(printf '%s' "$wout" | tail -1 | cut -f1)")
  deff=$(printf '%s' "$wout" | tail -1 | cut -f2)
  FETCHED=$((FETCHED + 1))
  # The listing is the other witness: the tile's declared name proves identity
  # for pages whose og:url points at the partner's own documentation.
  tile=$(jq -c --arg s "$slug" 'select(.slug==$s)' "$TMPD/tiles.jsonl" | head -1)
  tname=$(printf '%s' "$tile" | jq -r '.name // ""' 2>/dev/null)
  cats=$(printf '%s' "$tile" | jq -c '.categories // []' 2>/dev/null)
  [ -n "$cats" ] || cats='[]'
  # THE OFF-SITE TEST COMES BEFORE THE STATUS TEST, and the order is the whole
  # point. MEASURED: 24 catalogue entries 302 straight off the marketplace —
  # /detail/zakeke to webklient.cz, /detail/adulto to adulto.cz, /detail/symmy
  # to a 401-protected staging host. There is no detail page to parse and the
  # third party's status says nothing about whether the add-on exists; the
  # MARKETPLACE listed it, and that is the fact worth recording. Testing the
  # status first buried 8 of these as `HTTP-000` connection failures.
  case "$deff" in
    "$HOST"/*) ;;
    *)
      if [ -n "$tname" ]; then
        jq -nc --arg s "$slug" --arg n "$tname" --arg u "$url" --arg d "$deff" \
               --arg t "$NOW" --argjson c "$cats" \
          # No vendor_group at all: the marketplace names no provider for these,
          # and an empty string is the shape that looks present and says
          # nothing — the same rule normalize.py applies to optional receipts.
          '{id:("upgates-"+$s), marketplace:"upgates", slug:$s, url:$u,
            product:$n, text_cs:$n, vendor_public:false,
            vendor_url:$d, categories:$c, fetched_at:$t, http_status:200,
            extraction:"listing-only"}' >> "$TMPD/rows.jsonl"
        KEPT=$((KEPT + 1))
      else
        printf '%s\toff-site redirect, no tile name\n' "$slug" >> "$TMPD/rejects.txt"
        REJECTED=$((REJECTED + 1))
      fi
      sleep "$SLEEP"; continue;;
  esac
  if [ "$dcode" != "200" ] || [ ! -s "$page" ]; then
    printf '%s\tHTTP-%s\n' "$slug" "$dcode" >> "$TMPD/rejects.txt"
    REJECTED=$((REJECTED + 1)); sleep "$SLEEP"; continue
  fi
  if rec=$(python3 "$EXTRACT" upgates-detail "$page" "$url" "$tname" 2>"$TMPD/err.txt"); then
    # Categories come from the LISTING, not the detail page: the detail page
    # shows one breadcrumb category while an add-on legitimately appears under
    # several, and the tiles already record every one.
    printf '%s' "$rec" | jq -c --arg t "$NOW" --argjson s "$dcode" --argjson c "$cats" \
      '. + {fetched_at:$t, http_status:$s, categories:$c}' >> "$TMPD/rows.jsonl"
    KEPT=$((KEPT + 1))
  else
    rc=$?
    why="$(tr -d '\n' < "$TMPD/err.txt" | cut -c1-160)"
    printf '%s\t%s\n' "$slug" "$why" >> "$TMPD/rejects.txt"
    if [ "$rc" -eq 3 ]; then GDPR_DROPPED=$((GDPR_DROPPED + 1)); else REJECTED=$((REJECTED + 1)); fi
  fi
  sleep "$SLEEP"
done < "$TMPD/todo.capped.txt"

# FAIL CLOSED — `merge` is the only writer of $OUT, so a failed merge leaves it
# empty rather than leaving a batch that skipped the GDPR gate.
: > "$OUT"
MSUM=$(python3 "$EXTRACT" merge "$OUT" "$TMPD/rows.jsonl" 2>"$TMPD/merr.txt") || ERRS="$ERRS out:merge-failed"
BATCH_GDPR=$(printf '%s' "$MSUM" | jq -r '.gdpr_dropped // 0' 2>/dev/null || echo 0)
GDPR_DROPPED=$((GDPR_DROPPED + BATCH_GDPR))
[ -s "$TMPD/merr.txt" ] && sed 's/^/    /' "$TMPD/merr.txt"

python3 "$EXTRACT" merge "$LOOKUP.tmp" "$LOOKUP" "$OUT" > "$TMPD/msum.txt" 2>&1 \
  && mv "$LOOKUP.tmp" "$LOOKUP" \
  || { ERRS="$ERRS lookup:merge-failed"; mv "$LOOKUP.tmp" "$TMPD/lookup.failed" 2>/dev/null || true; }
printf '%s' "$LIST_HASH" > "$HASH_F"

# ══ 6. items FETCHED vs items KEPT ══════════════════════════════════════════
LTOT=$(wc -l < "$LOOKUP" 2>/dev/null | tr -d ' '); [ -n "$LTOT" ] || LTOT=0
echo "== upgates: $NADDON declared -> $NCAP selected -> $FETCHED fetched -> $KEPT kept"
echo "    rejected by contract: $REJECTED · dropped by GDPR gate: $GDPR_DROPPED"
echo "    lookup table now holds $LTOT rows -> $LOOKUP"
if [ -s "$TMPD/rejects.txt" ]; then
  cp "$TMPD/rejects.txt" "$OUTDIR/.fetch/upgates-rejects.tsv"
  echo "    reject reasons (full list: $OUTDIR/.fetch/upgates-rejects.tsv):"
  awk -F'\t' '{sub(/^REJECT [^ ]+: /,"",$2); print $2}' "$TMPD/rejects.txt" \
    | sed -E 's/\(.*\)//' | sort | uniq -c | sort -rn | head -8 | sed 's/^/      /'
fi
# See the same block in fetch_shoptet.sh: zero yield is SCRIPTED-SILENT only
# when the corpus is empty. Once built, the permanently-rejected residue makes
# `KEPT == 0` the steady state, and an alarm that fires every run is no alarm.
LMKT=$(grep -c '"marketplace": "upgates"' "$LOOKUP" 2>/dev/null | tr -d ' '); [ -n "$LMKT" ] || LMKT=0
if [ "$KEPT" -eq 0 ] && [ "$LMKT" -eq 0 ]; then
  echo "    SCRIPTED-SILENT: the fetch worked, nothing landed, and the corpus is EMPTY."
  mf upgates error 200 "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" "yield: 0 records from $FETCHED fetches, corpus empty"
  exit 1
fi
if [ "$KEPT" -eq 0 ]; then
  echo "    0 new records: all $FETCHED selected slugs are permanent rejects; $LMKT upgates rows already held."
  mf upgates ok 200 "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" \
     "yield: 0 new; $REJECTED contract-rejected, $GDPR_DROPPED gdpr-dropped, corpus holds $LMKT"
  echo "    wrote $OUT"
  exit 0
fi
if [ -n "$ERRS" ]; then
  mf upgates ok 200 "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS"
else
  mf upgates ok 200 "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "    wrote $OUT"
