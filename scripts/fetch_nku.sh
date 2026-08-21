#!/usr/bin/env bash
# fetch_nku.sh — NKÚ (Czech Supreme Audit Office): Věstník + audit findings.
#
# ══ WHAT THIS FEED IS ════════════════════════════════════════════════════════
# NKÚ publishes documented state failure with the state's own evidence behind
# it: audit conclusions naming a body, a sum and a finding. That is a problem
# statement that arrives pre-sourced.
#
# ══ THE REGISTRY'S PREMISE FOR THIS FEED IS FACTUALLY WRONG ══════════════════
# data/feeds.json calls nku "THE LLM-FALLBACK PROOF FEED" and sets
# `contract.parse = "html-table"` on the reasoning that "its HTML is expected
# to resist structured parsing, so a parse violation here is the designed path
# to extraction: llm-fallback, not a defect".
#
# MEASURED 2026-08-21, both halves of that premise fail:
#
#   1. NKÚ PUBLISHES A DECLARED RSS FEED. `https://nku.cz/cz/rss.xml` ->
#      HTTP 200, application/xml, 14,379 bytes, 30 well-formed RSS 2.0 <item>s
#      with title/link/pubDate. The registry never named it. A declared,
#      versioned interface existed the whole time.
#   2. THE VĚSTNÍK HTML DOES NOT RESIST PARSING. It is a single
#      `<table class="table table-list" id="myTable">` with four fixed columns
#      (Datum zveřejnění · Obsah · Zařazeno do částky věstníku · Detail
#      kontroly) and one <tr> per item. 23 rows for 2026, 29 for 2025, parsed
#      mechanically below with zero ambiguity.
#
# So this feed needs NO LLM fallback and never did. `contract.parse` should be
# `jsonl` and the llm-fallback rationale should come out of the registry row —
# reported, not edited here (data/feeds.json is shared).
#
# ══ THE TRANSPORT SHAPE, AND THE TRADEOFF ════════════════════════════════════
# PRIMARY = the declared RSS. It is the least-fragile surface available: a
# stated contract, stable field names, and it cannot be broken by a CSS change.
# Its limit is recall — a rolling 30-item window over the WHOLE site, so it
# mixes Věstník items with press releases, job ads and asset sales, and it
# carries no history.
#
# BACKFILL = the Věstník year pages. Full year of audit conclusions with their
# PDF links, but it is scraped HTML and therefore the fragile half.
#
# They are deliberately NOT equal partners: the RSS alone is enough to keep the
# feed alive at a daily cadence, and a total failure of the HTML backfill
# degrades recall without failing the run. That is the owner's tradeoff made
# explicit — the valuable thing (a year of conclusions) is the fragile thing,
# so it is isolated where it cannot take the feed down with it.
#
# Usage: scripts/fetch_nku.sh [outdir] [year ...]  <-- outdir is $1 (see §5.3)
set -uo pipefail   # no -e: one failed year must not kill the rest
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
shift 2>/dev/null || true
YEARS="${*:-$(date +%Y) $(( $(date +%Y) - 1 ))}"

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

# Parse curl's -w receipt into W_CODE / W_BYTES / W_SECS / W_MS / W_CT.
parse_w() { # "<http_code> <size_download> <time_total> <content_type>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_CT="${4:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

command -v jq >/dev/null 2>&1 || { echo "fetch_nku: jq is required" >&2; exit 2; }

# EXPECTED ABSENCE (§7.2 step 0). The registry's contract.allow_missing is the
# source of truth; fetch_all.sh reads it from data/feeds.json and exports it.
ALLOW_MISSING="${ALLOW_MISSING:-0}"

# HOST: non-www, per blockers register row 12.
# HONEST RE-MEASUREMENT, 2026-08-20 — the doc's row 12 does NOT reproduce:
#   * it claims www.nku.cz "403s generic fetchers". Measured with curl's DEFAULT
#     UA: www -> 200, non-www -> 200, byte-identical (28,795). No 403 observed.
#   * it claims "uppercase 301s to http". Measured: /rka/VESTNIK.asp -> 200, no
#     redirect at all.
# Non-www is kept because it is what the doc mandates and it demonstrably works;
# the row's stated REASONS are unverified. Re-measure before relying on either.
BASE="${NKU_BASE:-https://nku.cz/scripts/rka/vestnik.asp?rok=}"
RSS_URL="${NKU_RSS:-https://nku.cz/cz/rss.xml}"

# The RSS is a WHOLE-SITE feed. These two link categories are administrative
# and carry no audit substance — job adverts and surplus-equipment sales. They
# are dropped by URL PATH, never by title text, so the rule cannot silently
# start matching a real finding. NKU_KEEP_ALL=1 disables the filter.
DROP_PATHS="${NKU_DROP_PATHS:-o-nas/kariera otevreny-urad/nepotrebny-majetek}"
KEEP_ALL="${NKU_KEEP_ALL:-0}"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
OUT="$OUTDIR/nku-vestnik.jsonl"
# RAW originals live under .fetch/ — NOT in the outdir root. normalize.py groups
# every file whose name carries the `nku` token into ONE feed and parses them
# all with the SAME contract kind, so leaving .html beside .jsonl would
# guarantee a parse violation. .fetch/ is a directory and therefore invisible
# to normalize.py's isfile-only payload scan.
RAWD="$OUTDIR/.fetch/nku"; mkdir -p "$RAWD"

TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""; SKIPPED=0
RSS_ITEMS=0; HTML_ITEMS=0; HTML_YEARS=0
TMPD="${TMPDIR:-/tmp}/nku.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT
: > "$TMPD/rows.jsonl"

# ── 1. PRIMARY: the declared RSS interface ───────────────────────────────────
rss_raw="$RAWD/nku-rss.xml"
parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                -A "$UA" -o "$rss_raw" \
                -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                "$RSS_URL" 2>/dev/null || true)"
LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))
if [ "$W_CODE" = "200" ]; then
  # ── MODE-A GUARD ── 200 carrying the wrong body. An ASP error page or a
  # maintenance notice is served as text/html at status 200; stored as an RSS
  # payload it would read as a healthy empty feed.
  if head -c 300 "$rss_raw" 2>/dev/null | grep -q '<rss\|<feed\|<?xml'; then
    TOT_BYTES=$((TOT_BYTES + W_BYTES))
    RSS_ITEMS=$(grep -o '<item>' "$rss_raw" | wc -l | tr -d ' ')
    echo "OK  rss: $RSS_ITEMS items ($W_BYTES bytes)"
  else
    echo "FAILED rss — MODE-A: HTTP 200 but body is not XML."
    echo "       first 120 bytes: $(head -c 120 "$rss_raw" | tr -d '\n')"
    ERRS="$ERRS rss:mode-a-not-xml"; RSS_ITEMS=0
  fi
else
  echo "FAILED rss (HTTP $W_CODE)"
  ERRS="$ERRS rss:HTTP-$W_CODE"
fi

# ── 2. BACKFILL: the Věstník year pages ──────────────────────────────────────
for year in $YEARS; do
  case "$year" in ''|*[!0-9]*) continue ;; esac
  out="$RAWD/nku-vestnik-$year.html"
  # -f: a non-2xx must not be stored as if it were a Věstník page. The explicit
  # `code = 200` test is NOT redundant with -f: --fail only trips at HTTP >= 400.
  parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                  -A "$UA" -o "$out" \
                  -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                  "$BASE$year" 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))

  if [ "$W_CODE" = "404" ] && [ "$ALLOW_MISSING" = "1" ]; then
    echo "SKIP $year (HTTP 404, allow_missing) — expected absence, not a failure"
    SKIPPED=$((SKIPPED+1)); continue
  fi
  if [ "$W_CODE" != "200" ]; then
    echo "FAILED $year (HTTP $W_CODE)"; ERRS="$ERRS $year:HTTP-$W_CODE"; continue
  fi
  # MODE-A: the page must actually be the Věstník table, not a 200-status error
  # document. THIS FEED CANNOT DEMONSTRATE EXPECTED ABSENCE — measured
  # 2026-08-20, ?rok=2027, ?rok=2099 and ?rok=1990 all return HTTP 200 with an
  # 18,095-byte empty shell; NKÚ never 404s on a missing calendar key. So the
  # marker below is the only thing separating "no such year" from "the year is
  # there and empty", and the 404 branch above is dead code for THIS feed
  # (retained for the MPSV-shaped feeds that genuinely 404).
  if ! grep -q 'table-list' "$out" 2>/dev/null; then
    echo "FAILED $year — MODE-A: HTTP 200 but no Věstník table in the body."
    ERRS="$ERRS $year:mode-a-no-table"; continue
  fi
  TOT_BYTES=$((TOT_BYTES + W_BYTES)); HTML_YEARS=$((HTML_YEARS + 1))
  echo "OK  vestnik $year ($W_BYTES bytes)"
done

# ── 3. MECHANICAL EXTRACTION -> one JSONL payload ────────────────────────────
# Both surfaces are folded into ONE row shape and deduped on NKÚ's own numeric
# id, which both surfaces carry (`/scripts/detail.php?id=15841` in the table,
# `…-id15841/` in the RSS link). That id is the only stable key here: titles
# repeat across years and the PDF filename only exists for conclusions.
python3 - "$TMPD/rows.jsonl" "$rss_raw" "$RAWD" "$KEEP_ALL" "$DROP_PATHS" <<'PY' || ERRS="$ERRS extract:python-failed"
import json, os, re, sys
from xml.etree import ElementTree as ET

out_path, rss_path, rawd, keep_all, drop_paths = sys.argv[1:6]
drops = [d for d in drop_paths.split() if d]
rows, seen = [], set()

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = (s.replace("&nbsp;", " ").replace("&amp;", "&").replace("&quot;", '"')
          .replace("&#39;", "'").replace("&lt;", "<").replace("&gt;", ">")
          .replace("\xa0", " "))
    return re.sub(r"\s+", " ", s).strip()

def doc_type(title, url):
    t = (title or "").lower()
    if "kontrolní závěr" in t or "/assets/kon-zavery/" in (url or ""):
        return "kontrolni-zaver"          # the audit conclusion itself
    if "změna plánu" in t:
        return "zmena-planu"
    if "kontroly zahajované" in t or "zahajovane-kontroly" in (url or ""):
        return "zahajovana-kontrola"
    if "věstník nkú" in t:
        return "vestnik-castka"
    if "tiskove-zpravy" in (url or ""):
        return "tiskova-zprava"           # the finding in plain language
    if "jednani-kolegia" in (url or "") or "jednání kolegia" in t:
        return "kolegium"
    return "other"

def add(rec):
    if not rec.get("nku_id") or rec["nku_id"] in seen:
        return
    seen.add(rec["nku_id"]); rows.append(rec)

# ---- RSS (primary) ----
rss_seen = 0
if os.path.isfile(rss_path):
    try:
        ch = ET.parse(rss_path).getroot().find("channel")
        for it in (ch.findall("item") if ch is not None else []):
            link = (it.findtext("link") or "").strip()
            title = clean(it.findtext("title") or "")
            m = re.search(r"-id(\d+)/?$", link)
            if not m or not title:
                continue
            rss_seen += 1
            if keep_all != "1" and any(d in link for d in drops):
                continue
            pub = (it.findtext("pubDate") or "").strip()
            dm = re.search(r"(\d{1,2})\s+(\w{3})\s+(\d{4})", pub)
            MON = dict(zip("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(),
                           range(1, 13)))
            date = (f"{dm.group(3)}-{MON.get(dm.group(2), 1):02d}-{int(dm.group(1)):02d}"
                    if dm else "")
            am = re.search(r"č\.\s*(\d{2}/\d{2})", title)
            add({"nku_id": m.group(1), "title": title,
                 "link": link.replace("http://www.nku.cz", "https://nku.cz"),
                 "date": date, "doc_type": doc_type(title, link),
                 "audit_no": am.group(1) if am else "",
                 "bulletin_issue": "", "pdf_url": "", "iface": "rss"})
    except ET.ParseError as e:
        print(f"    rss parse error: {e}", file=sys.stderr)

# ---- Věstník year tables (backfill) ----
# One <tr> per item, four <td>: date · content(link) · bulletin issue · audit no.
TR = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S | re.I)
TD = re.compile(r"<td[^>]*>(.*?)</td>", re.S | re.I)
HREF = re.compile(r'href="([^"]+)"', re.I)
html_seen = 0
for fn in sorted(os.listdir(rawd)):
    if not fn.endswith(".html"):
        continue
    body = open(os.path.join(rawd, fn), encoding="utf-8", errors="replace").read()
    for tr in TR.findall(body):
        tds = TD.findall(tr)
        if len(tds) < 4:
            continue
        html_seen += 1
        date_raw = clean(tds[0])
        dm = re.match(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", date_raw)
        date = f"{dm.group(3)}-{int(dm.group(2)):02d}-{int(dm.group(1)):02d}" if dm else ""
        hrefs = HREF.findall(tds[1])
        href = hrefs[0] if hrefs else ""
        title = clean(tds[1]).removesuffix(" (pdf)").strip()
        idm = re.search(r"[?&]id=(\d+)", href)
        pdf = ""
        if "/assets/kon-zavery/" in href:
            pdf = "https://nku.cz" + href if href.startswith("/") else href
        audit = clean(tds[3])
        # A conclusion row links straight to the PDF and carries no detail id;
        # its stable key is the PDF stem (K25021), which NKÚ does not reuse.
        nid = idm.group(1) if idm else (
            re.sub(r"\.pdf$", "", href.rsplit("/", 1)[-1]) if pdf else "")
        if not nid or not title:
            continue
        add({"nku_id": nid, "title": title,
             "link": (pdf or ("https://nku.cz" + href if href.startswith("/")
                              else f"https://nku.cz/scripts/rka/{href}")),
             "date": date, "doc_type": doc_type(title, href),
             "audit_no": audit, "bulletin_issue": clean(tds[2]),
             "pdf_url": pdf, "iface": "vestnik-html"})

with open(out_path, "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"    extracted: rss {rss_seen} seen -> kept after path filter; "
      f"html {html_seen} table rows; {len(rows)} unique after dedupe on nku_id")
PY

N=$(wc -l < "$TMPD/rows.jsonl" 2>/dev/null | tr -d ' '); [ -n "$N" ] || N=0
if [ "$N" -gt 0 ]; then
  mv "$TMPD/rows.jsonl" "$OUT"
  echo "    by doc_type: $(jq -r '.doc_type' "$OUT" | sort | uniq -c | tr '\n' ' ')"
fi

# ── ITEMS FETCHED vs ITEMS KEPT — a zero-yield run must be LOUD ──────────────
FETCHED=$((RSS_ITEMS + 0))
echo "== nku: rss $RSS_ITEMS items + $HTML_YEARS vestnik year page(s) -> $N unique records"
if [ "$N" -eq 0 ]; then
  if [ "$HTML_YEARS" -eq 0 ] && [ "$RSS_ITEMS" -eq 0 ] && [ "$SKIPPED" -gt 0 ]; then
    mf nku skipped "$LAST_CODE" 0 0 "$TOT_MS" "$STARTED" "$OUTDIR" ""
  else
    # Bytes arrived and parsed, and still nothing came out: the yield=zero
    # anomaly. Reported as an error so the feed cannot read LIVE landing nothing.
    mf nku error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
       "yield: zero records extracted${ERRS:+ —$ERRS}"
    exit 1
  fi
elif [ -n "$ERRS" ]; then
  mf nku ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS"
else
  mf nku ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
[ "$N" -gt 0 ] && echo "    wrote $OUT"
exit 0
