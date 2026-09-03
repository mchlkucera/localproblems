#!/usr/bin/env bash
# fetch_hackathons.sh — owner-set hackathon challenges from six Czech organizer
# pages, staged for the `asks` ledger (feed key `hackathon`, id prefix `hack-`).
#
# ══ WHAT THIS FEED IS ════════════════════════════════════════════════════════
# A hospital, a city or a ministry states a problem it wants solved and invites
# solutions — before any procurement money exists. The six organizers below
# publish those statements with the owner's name on them. The record is the
# statement and its owner; prizes, team counts and winners are never staged
# (docs/superpowers/specs/2026-09-03-asks-ledger-design.md).
#
# ══ THE TRANSPORT SHAPE ══════════════════════════════════════════════════════
# Six plain-HTML pages, one GET each. MEASURED 2026-09-03: no site offers an
# API or a feed for its challenges; all six answer HTTP 200 to a browser-style
# User-Agent, and hackjakbrno.cz answers 403 to curl's default one (a WAF rule,
# not a ToS). So the UA below is browser-shaped AND still names us with a
# contact address — the site can tell who is asking; the WAF cannot.
#
# Each page is its own MODE-A contract. A 200 whose body lacks the site's
# section marker — a login page, a maintenance notice, a redesign — is refused
# and reported, never parsed. The marker lives in scripts/hack_extract.py's
# rule table beside everything else about the site, and this script learns the
# site list from that table (`hack_extract.py sites`): a seventh site is one
# Python row and zero bash edits.
#
# One site failing degrades recall, not the run. The manifest row is `ok` with
# `partial:` errors while at least one site yielded, `error` on zero yield.
#
# ══ FILENAME CONTRACT ════════════════════════════════════════════════════════
# normalize.py groups payloads by the feed token in the filename; `hack` in
# `hack-challenges.jsonl` is that token and is shared with data/feeds.json's
# `id_prefixes`. Raw originals go under .fetch/hackathon/ — a directory is
# invisible to normalize.py's isfile-only payload scan, so an .html can never
# be mistaken for a payload of the same feed.
#
# Usage: scripts/fetch_hackathons.sh [outdir]   <-- outdir is $1 (§5.3)
set -uo pipefail   # no -e: one failed site must not kill the rest
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"

HERE="$(cd "$(dirname "$0")" && pwd)"
EXTRACT="$HERE/hack_extract.py"

UA="Mozilla/5.0 (Macintosh) localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# One appended row per REGISTRY FEED KEY per run; same columns and same
# receipts.jsonl seam as scripts/fetch_nku.sh — see the comment there.
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
  # The true status, byte count and transfer time exist ONLY here, at fetch
  # time. Field names are db.py's FETCHLOG_FIELDS.
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

command -v jq >/dev/null 2>&1 || { echo "fetch_hackathons: jq is required" >&2; exit 2; }
[ -f "$EXTRACT" ] || { echo "fetch_hackathons: $EXTRACT is missing" >&2; exit 2; }

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
OUT="$OUTDIR/hack-challenges.jsonl"
RAWD="$OUTDIR/.fetch/hackathon"; mkdir -p "$RAWD"

TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""
SITES_SEEN=0; SITES_OK=""
TMPD="${TMPDIR:-/tmp}/hack.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT

# ── 1. one GET per site, each body guarded before it may be parsed ───────────
while IFS=$'\t' read -r key url; do
  [ -n "$key" ] || continue
  SITES_SEEN=$((SITES_SEEN + 1))
  out="$RAWD/$key.html"
  # -f: a non-2xx must not be stored as if it were the page. The explicit
  # `code = 200` test is NOT redundant with -f: --fail only trips at >= 400.
  parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                  -A "$UA" -o "$out" \
                  -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                  "$url" 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))
  if [ "$W_CODE" != "200" ]; then
    echo "FAILED $key (HTTP $W_CODE)"; ERRS="$ERRS $key:HTTP-$W_CODE"; continue
  fi
  # MODE-A: the body must carry the site's section marker. The refused body is
  # KEPT under .fetch/ so the next person can see what the host actually served.
  reason="$(python3 "$EXTRACT" guard "$key" "$out" 2>&1)"
  if [ $? -ne 0 ]; then
    echo "FAILED $key — $reason"
    echo "       first 120 bytes: $(head -c 120 "$out" 2>/dev/null | tr -d '\n')"
    ERRS="$ERRS $key:mode-a"; continue
  fi
  TOT_BYTES=$((TOT_BYTES + W_BYTES)); SITES_OK="$SITES_OK $key"
  echo "OK  $key ($W_BYTES bytes)"
done < <(python3 "$EXTRACT" sites)

if [ "$SITES_SEEN" -eq 0 ]; then
  # The rule table itself failed to load — nothing was even attempted.
  mf hackathon error "$LAST_CODE" 0 0 "$TOT_MS" "$STARTED" "$OUTDIR" "sites: hack_extract.py listed no sites"
  exit 1
fi

# ── 2. MECHANICAL EXTRACTION -> one JSONL payload ────────────────────────────
# The parser is imported, not re-implemented: hack_extract.py is also what
# normalize.py imports, so there is exactly one definition of a row. This
# heredoc only decides WHICH files, counts them, and hands zero-yield sites
# back to bash — a page that passed the guard and still produced nothing is a
# partial error (UPOL between editions), never a silent zero.
: > "$TMPD/rows.jsonl"; : > "$TMPD/zero.txt"
python3 - "$EXTRACT" "$RAWD" "$TMPD/rows.jsonl" "$TMPD/zero.txt" $SITES_OK <<'PY' || ERRS="$ERRS extract:python-failed"
import json, os, sys
extract, rawd, out_path, zero_path, *sites = sys.argv[1:]
sys.path.insert(0, os.path.dirname(extract))
import hack_extract as hx

zero, total = [], 0
with open(out_path, "w", encoding="utf-8") as fh:
    for key in sites:
        with open(os.path.join(rawd, key + ".html"), encoding="utf-8", errors="replace") as f:
            rows = hx.parse_site(key, f.read())
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        owners = sorted({r["owner"] for r in rows})
        print(f"    {key:14s} {len(rows):3d} challenge(s)"
              + (f"  edition {rows[0]['edition'] or '?'}  event {rows[0]['event_date'] or '-'}"
                 f"  owner(s): {'; '.join(owners)}" if rows else "  <- zero yield"))
        total += len(rows)
        if not rows:
            zero.append(key)
with open(zero_path, "w") as fh:
    fh.write(" ".join(zero))
print(f"    extracted: {total} challenge(s) from {len(sites)} site(s)")
PY
for z in $(cat "$TMPD/zero.txt" 2>/dev/null); do ERRS="$ERRS $z:yield-zero"; done

N=$(wc -l < "$TMPD/rows.jsonl" 2>/dev/null | tr -d ' '); [ -n "$N" ] || N=0
if [ "$N" -gt 0 ]; then
  mv "$TMPD/rows.jsonl" "$OUT"
  echo "    by site: $(jq -r '.site' "$OUT" | sort | uniq -c | awk '{print $2"="$1}' | tr '\n' ' ')"
fi

# ── ITEMS FETCHED vs ITEMS KEPT — a zero-yield run must be LOUD ──────────────
SITES_OK_N=$(printf '%s' "$SITES_OK" | wc -w | tr -d ' ')
echo "== hackathon: $SITES_OK_N/$SITES_SEEN site(s) passed the guard -> $N challenge(s)"
if [ "$N" -eq 0 ]; then
  # Bytes arrived (or nothing did) and nothing came out: reported as an error
  # so the feed cannot read LIVE while landing nothing.
  mf hackathon error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "yield: zero records extracted${ERRS:+ —$ERRS}"
  exit 1
elif [ -n "$ERRS" ]; then
  mf hackathon ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS"
else
  mf hackathon ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "    wrote $OUT"
exit 0
