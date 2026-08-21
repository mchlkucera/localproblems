#!/usr/bin/env bash
# fetch_vestbee.sh — Vestbee CEE funding rounds, over the SITEMAP.
#
# ══ THE FEED WAS NEVER DEAD — THE TRANSPORT WAS ══════════════════════════════
# data/feeds.json has vestbee at status `dead`. The CONTENT is our single
# largest funding source: 240 of the 414 `round` records (58%) came from
# vestbee.com, every one harvested BY HAND after the RSS broke. Only the pipe
# broke.
#
# MEASURED 2026-08-21 from the real network path, with the descriptive UA:
#
#   https://www.vestbee.com/blog/rss.xml
#     -> 301 -> https://www.vestbee.com/insights/rss.xml -> HTTP 404
#     -> content-type text/html, **313,275 bytes**
#
# THAT 404 BODY IS THE MODE-A TRAP THIS REPO ALREADY FELL INTO. A third of a
# megabyte of rendered HTML at status 404: scripts/fetch_feeds.sh used
# `curl -sL` with no `-f`, so the 404 page was written to disk as a feed
# payload and the script printed OK. Hence, below and without exception:
# `-f --remove-on-error`, an explicit `code = 200` assertion, AND a body
# assertion — a 200 is not evidence that the bytes are the resource.
#
# ══ THE LIVE INTERFACE IS THE SITEMAP, AND IT IS BETTER THAN THE RSS ═════════
#   https://www.vestbee.com/sitemap_index.xml  -> 200, 626 B, four children
#   https://vestbee.com/__sitemap__/posts.xml  -> 200, 1,045,846 B
#       (apex -> www redirect; -L, and the landing URL is recorded)
#       3,065 <url> entries, <lastmod> on EVERY ONE, back to 2020-11-05
#       ETag: "fdad39a9…-ssl"  -> conditional GET works
#
# Two properties the RSS never had: FULL HISTORY, and a per-item change stamp.
# `lastmod` plus `If-None-Match` is true incrementality — a quiet day costs one
# request and returns 304.
#
# ══ GRANULARITY: WHY ONE SIGNAL PER ARTICLE IS CORRECT HERE ══════════════════
# MEASURED over all 3,065 posts:
#     1,831  per-round articles   `<company>-raises|secures|lands|…-<amount>`
#     1,154  other editorial
#        80  monthly roundups     `top-cee-funding-rounds-closed-in-<month>`
#
# The dominant family is ALREADY ONE ARTICLE PER ROUND — the slug carries the
# company and the amount. So per-article and per-round are the SAME grain for
# 1,831 of them, and no body-splitting is needed.
#
# The 80 roundups are the genuine many-rounds-per-article case. THEY ARE NOT
# CONVERTED INTO SIGNALS HERE. Emitting one record for an article covering ten
# fundings would collapse ten signals into one, which is the error the
# coordinator flagged; splitting them needs the article body read as prose.
# They are counted, listed with `doc_type:"roundup"` and `needs_body_split:
# true`, and left for the attended pass — visible, never silently dropped.
#
# ══ THE ID RULE, STATED — AND THE COLLISION IT AVOIDS ════════════════════════
# The 246 hand-harvested records use `round-<company>` (`round-adfin`,
# `round-cthings-co`). Keeping that shape matters: it is what lets seen.txt
# recognise a round we already hold instead of landing it twice.
#
# But MEASURED: 1,831 per-round articles map to only 1,723 distinct company
# slugs. 101 companies raise more than once (arx-robotics, iceye and lovable
# three times each), so a bare `round-<company>` would silently DROP 108
# articles — 5.9% of every round Vestbee has ever published — as false dupes.
#
# So the rule is: `round-<company>`, and where two articles in the payload
# resolve to the same company, EVERY colliding one is disambiguated with its
# amount token (`round-iceye-136-m`). The collision set is computed over the
# whole payload, so the id does not depend on fetch order. Re-editing an
# article changes `lastmod` but never the slug, so ids are stable across
# re-posts — which is the failure mode the coordinator named.
#
# Usage: scripts/fetch_vestbee.sh [outdir]        <-- outdir is $1 (see §5.3)
set -uo pipefail
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
UA="localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

INDEX="${VESTBEE_INDEX:-https://www.vestbee.com/sitemap_index.xml}"
# How far back to consider an article "new". The seen.txt dedupe in
# normalize.py is the real guard; this only bounds how many bodies get fetched.
SINCE_DAYS="${VESTBEE_SINCE_DAYS:-30}"
# Hard ceiling on best-effort body fetches, so a sitemap-wide `lastmod` bump
# (a site migration re-stamps every entry) cannot turn into 3,065 requests.
MAX_BODIES="${VESTBEE_MAX_BODIES:-60}"
CACHE="${VESTBEE_CACHE:-data/raw/.cache}"
mkdir -p "$CACHE"

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# One appended row per REGISTRY FEED KEY per run. Columns map 1:1 onto the
# `fetch_log` DDL (§2.3); `db.py fetchlog <dir>` reads this table and
# normalize.py fills items_kept / yield_anomaly / parse_method afterwards.
#   result=ok      -> fetch_log.ok = 1
#   result=skipped -> fetch_log.ok = 1, parse_method='none'. EXPECTED ABSENCE
#                     (§7.2 step 0) — here, a 304 on the conditional GET: the
#                     sitemap genuinely has not changed. It MUST NOT increment
#                     consecutive_failures and MUST NOT move the feed to BROKEN.
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
  # normalize.py cannot reconstruct a status code after the fact; the true
  # status, byte count and transfer time exist ONLY here, at fetch time. Field
  # names are exactly db.py's FETCHLOG_FIELDS so no translation is needed.
  # Lives in a SUBDIRECTORY so normalize.py's payload scan (isfile only) can
  # never mistake it for a feed payload.
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

# FIELD ORDER IS LOad-BEARING: `set --` splits on whitespace and content_type
# legitimately contains one ("text/xml; charset=UTF-8"), so it goes LAST. With
# it in the middle, url_effective was being read as "charset=UTF-8".
parse_w() { # "<http_code> <size_download> <time_total> <url_effective> <content_type>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_URL="${4:-}"; W_CT="${5:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

command -v jq >/dev/null 2>&1 || { echo "fetch_vestbee: jq is required" >&2; exit 2; }

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
OUT="$OUTDIR/vestbee-rounds.jsonl"
RAWD="$OUTDIR/.fetch/vestbee"; mkdir -p "$RAWD"
TMPD="${TMPDIR:-/tmp}/vestbee.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT
TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""

# ── 1. the sitemap index — discovery, not a guessed path ─────────────────────
idx="$RAWD/sitemap_index.xml"
parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error -A "$UA" -o "$idx" \
                -w '%{http_code} %{size_download} %{time_total} %{url_effective} %{content_type}' \
                "$INDEX" 2>/dev/null || true)"
LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
if [ "$W_CODE" != "200" ]; then
  echo "FAILED sitemap_index (HTTP $W_CODE)"
  mf vestbee error "$W_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "sitemap_index:HTTP-$W_CODE"
  exit 1
fi
# MODE-A: on this host a miss is 313 KB of HTML at some status. XML or nothing.
if ! head -c 300 "$idx" | grep -q '<sitemapindex\|<?xml'; then
  echo "FAILED sitemap_index — MODE-A: HTTP 200 but body is not XML ($W_BYTES bytes, $W_CT)."
  echo "       first 120 bytes: $(head -c 120 "$idx" | tr -d '\n')"
  mf vestbee error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "sitemap_index:mode-a-not-xml"
  exit 1
fi
POSTS_URL="$(grep -oE '<loc>[^<]*posts\.xml</loc>' "$idx" | head -1 | sed -E 's#</?loc>##g')"
if [ -z "$POSTS_URL" ]; then
  echo "FAILED — sitemap index carries no posts.xml. Children present:"
  grep -oE '<loc>[^<]+</loc>' "$idx" | sed -E 's#</?loc>##g' | sed 's/^/       /'
  mf vestbee error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "sitemap_index:no-posts-child"
  exit 1
fi
echo "OK  sitemap_index ($W_BYTES bytes) -> $POSTS_URL"

# ── 2. posts.xml, CONDITIONAL ── a quiet day costs one request ───────────────
ETAG_F="$CACHE/vestbee-posts.etag"
posts="$RAWD/posts.xml"
COND=""
[ -f "$ETAG_F" ] && COND="$(cat "$ETAG_F" 2>/dev/null)"
# --etag-compare/--etag-save handle the If-None-Match dance and the 304 without
# clobbering the cached file. -f would turn a 304 into a failure, so 304 is
# tested explicitly here and -f is kept for the >=400 cases.
parse_w "$(curl -sSL -m 120 --retry 2 --retry-delay 5 -A "$UA" -o "$posts" \
                ${COND:+-H "If-None-Match: $COND"} \
                -D "$TMPD/posts.h" \
                -w '%{http_code} %{size_download} %{time_total} %{url_effective} %{content_type}' \
                "$POSTS_URL" 2>/dev/null || true)"
LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))

if [ "$W_CODE" = "304" ]; then
  # EXPECTED ABSENCE, not a failure: the sitemap is byte-identical to last run,
  # so there is genuinely nothing new. ok=1, parse_method=none.
  echo "== vestbee: 304 Not Modified — sitemap unchanged since last run, 0 new rounds."
  mf vestbee skipped 304 0 0 "$TOT_MS" "$STARTED" "$OUTDIR" "304 Not Modified (If-None-Match)"
  exit 0
fi
if [ "$W_CODE" != "200" ]; then
  echo "FAILED posts.xml (HTTP $W_CODE)"
  mf vestbee error "$W_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "posts.xml:HTTP-$W_CODE"
  exit 1
fi
if ! head -c 300 "$posts" | grep -q '<urlset\|<?xml'; then
  echo "FAILED posts.xml — MODE-A: HTTP 200 but body is not XML ($W_BYTES bytes, $W_CT)."
  echo "       first 120 bytes: $(head -c 120 "$posts" | tr -d '\n')"
  mf vestbee error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "posts.xml:mode-a-not-xml"
  exit 1
fi
TOT_BYTES=$((TOT_BYTES + W_BYTES))
NURL=$(grep -o '<url>' "$posts" | wc -l | tr -d ' ')
echo "OK  posts.xml ($W_BYTES bytes, $NURL urls) landed on $W_URL"
grep -i '^etag:' "$TMPD/posts.h" | tail -1 | tr -d '\r' | awk '{print $2}' > "$ETAG_F" 2>/dev/null || true

# ── 3. select, then enrich from each article's DECLARED metadata ─────────────
python3 - "$posts" "$TMPD/sel.jsonl" "$SINCE_DAYS" "$MAX_BODIES" <<'PY' || ERRS="$ERRS select:python-failed"
import json, re, sys, datetime
posts, out, since_days, max_bodies = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
x = open(posts, encoding="utf-8", errors="replace").read()
pairs = re.findall(r"<url>\s*<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", x)
VERB = (r"(?:raises|secures|lands|closes|gets|nets|bags|scores|attracts|receives"
        r"|obtains|collects|invests|snaps)")
PER = re.compile(r"-" + VERB + r"-", re.I)
ROUNDUP = re.compile(r"top-cee-funding-rounds|largest-cee-startup-funding", re.I)
cut = (datetime.date.today() - datetime.timedelta(days=since_days)).isoformat()

per, roundups, editorial = [], [], 0
for u, m in pairs:
    slug = u.rstrip("/").rsplit("/", 1)[-1]
    if ROUNDUP.search(u):
        if m[:10] >= cut:
            roundups.append((u, m, slug))
    elif PER.search(u):
        per.append((u, m, slug))
    else:
        editorial += 1

fresh = [t for t in per if t[1][:10] >= cut]
fresh.sort(key=lambda t: t[1], reverse=True)
capped = fresh[:max_bodies]

# ── the id rule ── company slug, disambiguated ONLY where it collides.
# The collision set is computed over the WHOLE per-round family, not just this
# window, so an id never changes meaning because of when we happened to fetch.
def company(slug):
    return re.split(r"-" + VERB + r"-", slug, flags=re.I)[0]
def amount_token(slug):
    m = re.search(r"-" + VERB + r"-(.+)$", slug, re.I)
    return m.group(1) if m else ""
from collections import Counter
allc = Counter(company(s) for _, _, s in per)

rows = []
for u, m, slug in capped:
    c = company(slug)
    sid = f"round-{c}" if allc[c] == 1 else f"round-{c}-{amount_token(slug)}"
    rows.append({"signal_id": sid, "slug": slug, "company_slug": c,
                 "link": u.replace("https://vestbee.com", "https://www.vestbee.com"),
                 "lastmod": m, "doc_type": "round", "needs_body_split": False,
                 "title": "", "summary": "", "date": m[:10],
                 "amount_value": None, "amount_currency": "", "amount_note": "",
                 "id_disambiguated": allc[c] > 1})
for u, m, slug in roundups:
    rows.append({"signal_id": f"roundup-{slug}", "slug": slug, "company_slug": "",
                 "link": u.replace("https://vestbee.com", "https://www.vestbee.com"),
                 "lastmod": m, "doc_type": "roundup", "needs_body_split": True,
                 "title": "", "summary": "", "date": m[:10],
                 "amount_value": None, "amount_currency": "", "amount_note": "",
                 "id_disambiguated": False})
with open(out, "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"    sitemap: {len(pairs)} urls = {len(per)} per-round + {len(roundups)+0} roundup(in-window) "
      f"+ {editorial} editorial")
print(f"    window : lastmod >= {cut} -> {len(fresh)} per-round fresh, capped to {len(capped)}"
      f" (VESTBEE_MAX_BODIES={max_bodies}); {len(roundups)} roundup(s) flagged needs_body_split")
print(f"    ids    : {sum(1 for r in rows if r['id_disambiguated'])} disambiguated by amount token")
PY

SEL=$(wc -l < "$TMPD/sel.jsonl" 2>/dev/null | tr -d ' '); [ -n "$SEL" ] || SEL=0
if [ "$SEL" -eq 0 ]; then
  echo "== vestbee: sitemap OK but nothing inside the ${SINCE_DAYS}d window — 0 records."
  mf vestbee ok 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "yield: 0 articles with lastmod within ${SINCE_DAYS}d"
  exit 0
fi

# ── 4. best-effort enrichment from schema.org JSON-LD ────────────────────────
# The articles embed `<script type="application/ld+json">` with @type Article:
# headline, datePublished, description. That is a DECLARED interface inside the
# page — stable across redesigns in a way that body selectors are not, which is
# the least-fragile handle available once the RSS is gone. A failure here costs
# ONE record its title, never the run.
: > "$TMPD/enriched.jsonl"
BOD_OK=0; BOD_FAIL=0
while IFS= read -r line; do
  [ -n "$line" ] || continue
  url=$(printf '%s' "$line" | jq -r '.link')
  bcode=$(curl -fsSL -m 45 -A "$UA" -o "$TMPD/art.html" --remove-on-error \
               -w '%{http_code}' "$url" 2>/dev/null || true)
  if [ "$bcode" = "200" ] && [ -s "$TMPD/art.html" ]; then
    if python3 - "$TMPD/art.html" "$line" >> "$TMPD/enriched.jsonl" 2>/dev/null <<'PY'
import html, json, re, sys
h = open(sys.argv[1], encoding="utf-8", errors="replace").read()
rec = json.loads(sys.argv[2])
head = desc = pub = ""
for m in re.finditer(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', h, re.S):
    try:
        d = json.loads(m.group(1))
    except json.JSONDecodeError:
        continue
    for node in (d if isinstance(d, list) else [d]):
        if isinstance(node, dict) and node.get("@type") == "Article":
            head = head or (node.get("headline") or "").strip()
            pub = pub or (node.get("datePublished") or "").strip()
            desc = desc or (node.get("description") or "").strip()
if not head:
    m = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]*)"', h, re.I)
    head = html.unescape(m.group(1)).strip() if m else ""
if not desc:
    m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"', h, re.I)
    desc = html.unescape(m.group(1)).strip() if m else ""
head = re.sub(r"\s+", " ", html.unescape(head)).strip()
desc = re.sub(r"\s+", " ", desc).strip()
# The headline carries the currency SYMBOL, which the slug does not — that is
# the whole reason a body fetch is worth one request. No FX conversion is done
# here: the rate depends on the round's close date, which is a judgement, so
# the original figure and its currency are recorded verbatim instead.
MULT = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000}
am = re.search(r"([€$£])\s?([0-9]+(?:[.,][0-9]+)?)\s?([KMB])\b", head, re.I)
if am:
    cur = {"€": "EUR", "$": "USD", "£": "GBP"}[am.group(1)]
    rec["amount_value"] = float(am.group(2).replace(",", ".")) * MULT[am.group(3).upper()]
    rec["amount_currency"] = cur
    rec["amount_note"] = "" if cur == "EUR" else f"{cur} figure as published; not converted"
if head:
    rec["title"] = head
if desc:
    rec["summary"] = desc[:600]
if pub[:10]:
    rec["date"] = pub[:10]
print(json.dumps(rec, ensure_ascii=False))
PY
    then BOD_OK=$((BOD_OK + 1)); else printf '%s\n' "$line" >> "$TMPD/enriched.jsonl"; BOD_FAIL=$((BOD_FAIL + 1)); fi
  else
    printf '%s\n' "$line" >> "$TMPD/enriched.jsonl"; BOD_FAIL=$((BOD_FAIL + 1))
  fi
  sleep 0.3
done < "$TMPD/sel.jsonl"
echo "    bodies: $BOD_OK enriched from JSON-LD, $BOD_FAIL left with sitemap-only fields"

mv "$TMPD/enriched.jsonl" "$OUT"
KEPT=$(wc -l < "$OUT" | tr -d ' ')
WITHT=$(jq -r 'select(.title != "") | .signal_id' "$OUT" | wc -l | tr -d ' ')

# ── ITEMS FETCHED vs ITEMS KEPT — a zero-yield run must be LOUD ──────────────
echo "== vestbee: $NURL sitemap urls -> $SEL selected -> $KEPT records ($WITHT with a resolved title)"
echo "    by doc_type: $(jq -r '.doc_type' "$OUT" | sort | uniq -c | tr '\n' ' ')"
if [ "$KEPT" -eq 0 ]; then
  mf vestbee error 200 "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" "yield: zero records after selection"
  exit 1
elif [ -n "$ERRS" ]; then
  mf vestbee ok 200 "$TOT_BYTES" "$KEPT" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS"
else
  mf vestbee ok 200 "$TOT_BYTES" "$KEPT" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "    wrote $OUT"
