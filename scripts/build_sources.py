#!/usr/bin/env python3
"""Build site/sources.html (hub) and site/source-<key>.html (one page per source)
from data/normalized/. Deterministic; run by the weekly pipeline after normalize.

Design: gazette v1.1 (skills/design-language). All signal tables are table.index
clones with one shared column layout so every table renders identical widths."""
import os, re, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
NORM = os.path.join(ROOT, "data", "normalized")
PROB = os.path.join(ROOT, "data", "problems")
SITE = os.path.join(ROOT, "site")

TODAY = datetime.date(2026, 8, 13) if os.environ.get("BUILD_FIXED_DATE") else datetime.date.today()

# origin groups, ranked by signal value (highest first)
ORIGINS = {
    "market":    ("The market — the operators", 1,
                  "Companies already operating a proven model in one market that is absent in another. The highest-value signal on the register: it pre-validates both demand and business model."),
    "top-down":  ("Top-down — the governments", 2,
                  "Deadlines and budgets written into law. Regulation creates a market on a date; tenders and public contracts show the money actually moving."),
    "bottom-up": ("Bottom-up — the users", 3,
                  "Problems stated directly by the people who have them: civic complaint platforms, participatory budgets, reviews, forums. The most authentic signal and the noisiest."),
    "capital":   ("The capital — the investors", 4,
                  "Where money already went. Capital signals never create a record on their own — they corroborate one."),
}

# source key -> (display name, origin, description, sort mode)
SOURCES = {
    "reg":    ("Regulatory triggers", "top-down",
               "EU regulations and national acts with compliance deadlines, verified against the primary legal text. The date on each signal is the operative deadline.", "deadline"),
    "ted":    ("Public tenders — TED", "top-down",
               "Awards and open competitions from the EU procurement journal. Public money already committed to a problem.", "money"),
    "hlidac": ("Public contracts — contract registry", "top-down",
               "Signed contracts from the national contract registry — buying below or beside the TED threshold.", "date"),
    "yc":     ("Accelerator batch — Y Combinator", "capital",
               "Recent accelerator companies whose model is proven elsewhere. Each signal records the model and a dated absence check.", "date"),
    "round":  ("Funding rounds — CEE", "capital",
               "Venture rounds in the region. A round proves investors fund the category, nothing more.", "money"),
}

COUNTRY = {"de": "Germany", "dk": "Denmark", "pl": "Poland", "at": "Austria", "ch": "Switzerland",
           "se": "Sweden", "nl": "Netherlands", "fr": "France", "uk": "United Kingdom", "us": "United States"}

def source_meta(key):
    if key in SOURCES:
        return SOURCES[key]
    if len(key) == 2:
        c = COUNTRY.get(key, key.upper())
        return ("Market scan — " + c, "market",
                "Direct scan of a foreign market: companies operating a proven model with no equivalent where the register's records sit. Each signal records the model and a dated absence check.", "date")
    return (key, "top-down", "Signal feed: " + key + ".", "date")

def parse(path):
    txt = open(path).read()
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^(\w+):\s*(.*)$", line)
            if mm:
                k, v = mm.group(1), mm.group(2).strip()
                if v.startswith('"') and v.endswith('"') and len(v) > 1:
                    v = v[1:-1]
                fm[k] = v
    return fm

def money_fmt(v):
    try:
        n = float(v)
    except (TypeError, ValueError):
        return None
    if n >= 1e6:
        s = "%.1f" % (n / 1e6)
        s = s.rstrip("0").rstrip(".")
        return "€" + s + "M"
    return "€%dk" % round(n / 1e3)

def esc(s):
    return html.escape(s, quote=True)

def load_signals():
    per = {}
    for key in sorted(os.listdir(NORM)):
        d = os.path.join(NORM, key)
        if not os.path.isdir(d):
            continue
        rows = []
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".md"):
                fm = parse(os.path.join(d, fn))
                fm.setdefault("id", fn[:-3])
                rows.append(fm)
        if rows:
            per[key] = rows
    return per

def record_map():
    """signal id -> [problem ids] by scanning problem files."""
    out = {}
    texts = {}
    for fn in sorted(os.listdir(PROB)):
        if fn.startswith("p-") and fn.endswith(".md"):
            texts[fn[:6].upper()] = open(os.path.join(PROB, fn)).read()
    def find(sid):
        return [pid for pid, t in sorted(texts.items()) if sid in t]
    return find

CHROME_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s — localproblems.org</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet">
<!-- localproblems.org design system v1.1 — see design-language skill. Content runs never edit shared.css. -->
<!-- GENERATED by scripts/build_sources.py — edit the data or the script, not this file. -->
<link rel="stylesheet" href="shared.css">
<style>
/* generated pages — one shared column layout so every signal table has identical widths.
   FLAGGED for incorporation into the reference stylesheet: table-layout lock. */
table.index { table-layout: fixed; }
.index col.c-name { width: 44%%; }
.index col.c-cat { width: 13%%; }
.index col.c-geo { width: 9%%; }
.index col.c-val { width: 11%%; }
.index col.c-rec { width: 10%%; }
.index col.c-date { width: 13%%; }
.index .t-title { width: auto; max-width: 0; }
.index td { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
</style>
</head>
<body>

<header class="masthead">
  <a class="brand" href="index.html">localproblems.org</a>
  <span class="issue">vol. %(vol)s · no. %(no)s</span>
</header>

<nav class="filters">
  <a href="index.html">List</a> ·
  <a href="map.html">Map</a> ·
  <a href="sources.html"%(cur)s>Sources</a> ·
  <a href="#">About</a> ·
  <a href="#">Newsletter</a>
</nav>
"""

FOOTER = """
<footer>
  Signals as recorded at intake, no warranty; every signal links to its origin.<br>
  Extract no. %(no)s/%(vol)s, generated automatically · <a href="sources.html">all sources</a> · <a href="index.html">the list</a>
</footer>

</body>
</html>
"""

COLGROUP = ('<colgroup><col class="c-name"><col class="c-cat"><col class="c-geo">'
            '<col class="c-val"><col class="c-rec"><col class="c-date"></colgroup>')
THEAD = ('<thead><tr><th>Name</th><th>Category</th><th>Geo</th>'
         '<th class="t-num">Value</th><th>Record</th><th class="t-num">Date</th></tr></thead>')

def geo_short(g):
    if not g or g == "EU":
        return g or "—"
    if g.startswith("CZ-") and g != "CZ-national":
        return "CZ · " + g[3:]
    return g.split("-")[0]

def value_for(fm, sort_mode):
    m = money_fmt(fm.get("money_eur"))
    if m:
        return m
    if sort_mode == "deadline":
        try:
            d = datetime.date.fromisoformat(fm.get("date", ""))
            if d > TODAY:
                return "T−%d" % (d - TODAY).days
        except ValueError:
            pass
    return "—"

def row_html(fm, sort_mode, find_records):
    name = fm.get("title") or fm.get("id")
    note = esc(fm.get("summary_en", ""))
    url = esc(fm.get("url", "#"))
    cat = (fm.get("category") or "—").replace("legal-compliance", "legal").replace("retail-services", "retail")
    recs = find_records(fm.get("id", ""))
    if recs:
        parts = []
        for pid in recs[:2]:
            page = os.path.join(SITE, "problem-%s.html" % pid.lower())
            parts.append('<a href="problem-%s.html">%s</a>' % (pid.lower(), pid) if os.path.exists(page) else pid)
        rec = " ".join(parts)
    else:
        rec = "—"
    return ('<tr><td class="t-title"><a href="%s" title="%s">%s</a></td>'
            '<td class="t-cat">%s</td><td class="mono">%s</td>'
            '<td class="t-num mono">%s</td><td class="t-id">%s</td>'
            '<td class="t-num t-date"><time>%s</time></td></tr>'
            % (url, note, esc(name), esc(cat), esc(geo_short(fm.get("geo", ""))),
               value_for(fm, sort_mode), rec, fm.get("date", "")))

def sort_rows(rows, mode):
    if mode == "money":
        return sorted(rows, key=lambda f: -(float(f.get("money_eur") or 0) if str(f.get("money_eur", "")).replace(".", "").isdigit() else 0))
    if mode == "deadline":
        return sorted(rows, key=lambda f: f.get("date", ""))
    return sorted(rows, key=lambda f: (f.get("date", ""), f.get("id", "")), reverse=True)

def sort_caption(mode):
    return {"money": "Sorted by value, descending",
            "deadline": "Sorted by deadline, ascending",
            "date": "Sorted by date, newest first"}[mode]

def build():
    vol, no = str(TODAY.year), "%02d" % TODAY.isocalendar()[1]
    per = load_signals()
    find_records = record_map()
    chrome = lambda title, cur: CHROME_TOP % {"title": title, "vol": vol, "no": no,
                                              "cur": ' aria-current="page"' if cur else ""}
    # order sources by origin rank, then count desc
    ordered = sorted(per.items(), key=lambda kv: (ORIGINS[source_meta(kv[0])[1]][1], -len(kv[1]), kv[0]))

    # ---- per-source pages ----
    for key, rows in ordered:
        name, origin, desc, mode = source_meta(key)
        o_name = ORIGINS[origin][0]
        latest = max(f.get("date", "") for f in rows)
        body = [chrome("Sources · " + name, True)]
        body.append('\n<nav class="crumb"><a href="sources.html">Sources</a> / %s / %s</nav>\n' % (esc(o_name), esc(name)))
        body.append("<h2>%s</h2>\n" % esc(name))
        body.append('<p class="crumb">%02d signals · data/normalized/%s/ · updated <time>%s</time></p>\n' % (len(rows), key, latest))
        body.append("<p>%s</p>\n" % esc(desc))
        body.append('<table class="index">\n%s\n<caption>%s · extract generated <time>%s</time> · hover a name for the recorded note</caption>\n%s\n<tbody>\n'
                    % (COLGROUP, sort_caption(mode), TODAY.isoformat(), THEAD))
        for fm in sort_rows(rows, mode):
            body.append(row_html(fm, mode, find_records) + "\n")
        body.append("</tbody>\n</table>\n")
        body.append(FOOTER % {"vol": vol, "no": no})
        open(os.path.join(SITE, "source-%s.html" % key), "w").write("".join(body))

    # ---- hub ----
    body = [chrome("Sources", True)]
    body.append("""
<p>The register's inputs. Every problem record is synthesized from normalized signals — one file per signal, public in the repo. One page per source; sources grouped by who stated the problem, highest signal value first.</p>

<p class="crumb">updated <time>%s</time></p>
""" % TODAY.isoformat())
    for origin, (o_name, _rank, o_desc) in sorted(ORIGINS.items(), key=lambda kv: kv[1][1]):
        srcs = [(k, r) for k, r in ordered if source_meta(k)[1] == origin]
        body.append("\n<h2>%s</h2>\n<p>%s</p>\n" % (esc(o_name), esc(o_desc)))
        if not srcs:
            body.append('<p class="crumb">No signals on record in this category. As of <time>%s</time>. Feed pending.</p>\n' % TODAY.isoformat())
            continue
        body.append('<table class="index">\n<colgroup><col class="c-name"><col class="c-cat"><col class="c-val"><col class="c-date"></colgroup>\n'
                    '<thead><tr><th>Source</th><th>Feed</th><th class="t-num">Signals</th><th class="t-num">Latest</th></tr></thead>\n<tbody>\n')
        for k, rows in srcs:
            name, _o, desc, _m = source_meta(k)
            latest = max(f.get("date", "") for f in rows)
            body.append('<tr><td class="t-title"><a href="source-%s.html" title="%s">%s</a></td>'
                        '<td class="t-id">data/normalized/%s/</td>'
                        '<td class="t-num mono">%02d</td>'
                        '<td class="t-num t-date"><time>%s</time></td></tr>\n'
                        % (k, esc(desc), esc(name), k, len(rows), latest))
        body.append("</tbody>\n</table>\n")
    body.append(FOOTER % {"vol": vol, "no": no})
    open(os.path.join(SITE, "sources.html"), "w").write("".join(body))

    print("built sources.html + %d source pages: %s" % (len(per), ", ".join("source-%s.html" % k for k, _ in ordered)))

if __name__ == "__main__":
    build()
