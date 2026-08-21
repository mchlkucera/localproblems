#!/usr/bin/env python3
"""
scripts/db.py — the working store driver for data/register.db.

    THE LAW (architecture-v3 §3): the JSONL ledgers, the problem markdown,
    data/feeds.json and data/feed_health.json are CANONICAL. This database is a
    derived working store. It is gitignored, it is deterministically rebuildable,
    and the web build never opens it.

Six tables and six views are projections of committed files and are DROPPED and
recreated by `rebuild`: `signals`, `meta`, and — since schema_version 4 — the
register itself: `problems`, `problem_sources`, `problem_comps` and
`problem_source_dims`, rebuilt from `data/problems/**/*.md` exactly as `signals`
is rebuilt from the JSONL ledgers. Problems are deterministically rebuildable;
history is not, which is the whole reason for the split below.

Two tables are HISTORY THAT EXISTS NOWHERE ELSE and are NEVER dropped:
`fetch_log` (the health spine — liveness, yield, contract results) and
`match_log` (link AND dismissal decisions; the dismissals are irrecoverable
memory). Losing them loses information no rebuild can reconstruct.

sqlite-vec is NOT installed on this host (`CREATE VIRTUAL TABLE ... USING vec0`
-> `no such module: vec0`). Every vec path is guarded: its absence sets
`meta.vec = 'off'` and DEGRADES the match shortlist to IČO / domain / name
joins, which need no extension. It must never fail a rebuild.

Commands
    rebuild             DROP + recreate the projections from the committed
                        JSONL ledgers AND the problem markdown. Asserts
                        jsonl_lines == signals_count and md_files ==
                        problems_count, and exits non-zero on either mismatch
                        (a duplicate id, a parse failure, a lost record).
    audit               THE SCORE GATE. Fails and NAMES rows for the laws
                        nothing enforced before. In order:
                          * the DB still describes the tree (`md_sha256` per
                            record + ledger line count) — checked FIRST, because
                            every verdict after it is about the corpus this
                            database was built from and not the one on disk;
                          * SCORING.md's "no source, no point" over four
                            dimensions (`score_unbacked`);
                          * the same law over the urgency DEADLINE sub-score
                            (`deadline_unbacked`) — urgency is invisible to
                            `score_unbacked` because the freshness rule backs it
                            on every record;
                          * unresolvable sources[]/comps[] signal refs
                            (`dangling_signal_refs`).
                        Also prints an ADVISORY money divergence report — a
                        rule that agrees with the human 27/31, which is
                        consistency evidence and never a verdict.
    upsert <jsonl>      Single-run path used by INGEST for one ledger file.
    fetchlog <dir>      Read <dir>/contract.json (written by normalize.py) into
                        fetch_log rows.
    health              Derive data/feed_health.json from fetch_log + the corpus.
    prefixes            AC-F3 totality: every id prefix in the ledgers must be
                        claimed by a registry row. Exits non-zero and NAMES the
                        orphans. Runs inside `rebuild` and `health` too.
    match ...           Append one match_log row. Run after EVERY decision,
                        including dismissals.
    dupes --report      Report-only sweep over entity keys. Writes nothing:
                        a human reads one report before anything auto-links.
    stats               Inspection summary.
    money               Money per class and geography. Refuses to run without
                        data/errata.jsonl, and never prints a cross-class total —
                        `money_eur` carries four incompatible kinds of money and
                        summing them answers no question. See MONEY_CLASSES.
    errata              The disputed-value ledger with its evidence. An
                        append-only corpus is corrected ON READ, never in place.

Phase 3, gated on the sqlite-vec install — NOT built, and they say so when called:
    embed               id-set difference -> embed the missing set
    shortlist           KNN shortlist for MATCH
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import textwrap
import unicodedata
from datetime import date, datetime, timedelta, timezone

SCHEMA_VERSION = "4"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "data", "register.db")
SIGNALS_DIR = os.path.join(ROOT, "data", "signals")
PROBLEMS_DIR = os.path.join(ROOT, "data", "problems")
ERRATA_PATH = os.path.join(ROOT, "data", "errata.jsonl")
FEEDS_JSON = os.path.join(ROOT, "data", "feeds.json")
HEALTH_JSON = os.path.join(ROOT, "data", "feed_health.json")


def log(msg):
    print(msg, file=sys.stderr)


# --------------------------------------------------------------------------
# PyYAML — required by the problem loader, and NOT on every python3 here
# --------------------------------------------------------------------------
#
# MEASURED on this host, 2026-08-20, and the measurement is why this exists:
#
#     /opt/homebrew/bin/python3   3.14.2   NO PyYAML   <- what `python3` resolves to
#     /usr/local/bin/python3      3.12.x   yaml 6.0.2
#     /usr/bin/python3            3.9.6    yaml 6.0.3
#
# `python3 scripts/db.py rebuild` is written into SPEC.md §9 and into
# pipeline/, and on this machine that command selects the ONE interpreter
# without the dependency. Rather than convert a working command into a
# ModuleNotFoundError, `rebuild` and `audit` re-exec themselves under the first
# interpreter that can import yaml — LOUDLY, on stderr, once, and never in a
# loop (the guard variable below is set in the child's environment).
#
# THIS IS A SHIM, NOT A DESIGN. The clean fix is one host-level install
# (`/opt/homebrew/bin/python3 -m pip install pyyaml`) after which this code
# never fires. It is here because installing packages on the operator's machine
# is not this script's business.
_YAML = None
_REEXEC_GUARD = "LP_DB_YAML_REEXEC"
_YAML_NEEDED = ("rebuild", "audit")
# 3.12 before 3.9: prefer the newest interpreter that actually carries the
# dependency, because everything else in this file is written for a modern one.
_YAML_CANDIDATES = (
    "/usr/local/bin/python3", "/opt/homebrew/bin/python3.12",
    "/opt/homebrew/bin/python3.11", "/usr/bin/python3",
    "python3.13", "python3.12", "python3.11",
)


def yaml_mod():
    """PyYAML, imported once. Callers are past `ensure_yaml`, so this succeeds."""
    global _YAML
    if _YAML is None:
        import yaml  # noqa: PLC0415 — deliberately lazy; see the block above
        _YAML = yaml
    return _YAML


# --------------------------------------------------------------------------
# THE TWO PARSERS DO NOT AGREE, AND THE DIFFERENCE IS LIVE IN THE CORPUS
# --------------------------------------------------------------------------
#
# PyYAML implements YAML **1.1**. js-yaml — which `web/lib/data.ts` calls, and
# which is therefore the authority on what a record MEANS — implements YAML
# **1.2 core**. Feeding one plain scalar to both, MEASURED here on 2026-08-20
# with this repo's own `web/node_modules/js-yaml`:
#
#     scalar      js-yaml (THE SITE)   PyYAML 1.1 (unpatched)
#     NO/No/no    "NO" (string)        False          <- LIVE, 4 occurrences
#     YES/ON/OFF  "YES" (string)       True / False
#     2026-07-09  "2026-07-09"         datetime.date  <- LIVE hazard
#     1:30        "1:30"               90    (sexagesimal)
#     017         17                   15    (octal)
#     0o17        15                   "0o17"
#     1_000       "1_000"              1000
#     12e3        12000                "12e3"
#
# The first line was not hypothetical. `geo: NO` — Norway, unquoted — appears on
# `p-0027 comps[2]`, `p-0029 comps[0]`, and inside `markets` on `p-0001 comps[0]`
# and `p-0023 comps[2]`. Unpatched, this loader wrote Norway into the register as
# the integer 0, silently, while the site rendered NO.
#
# The second line is the opposite failure and it is just as bad: an unquoted ISO
# date is a plain STRING to js-yaml, so `data/CONVENTIONS.md`'s own documented
# gap-check example (`expires: 2026-11-17`, unquoted) builds green on the site —
# but PyYAML hands back a `datetime.date`, which then either trips a spurious
# "quote it in the YAML" rejection or leans on sqlite3's DEPRECATED default date
# adapter on its way into a TEXT column.
#
# So: patch the two implicit resolvers that are live or likely, and DO NOT patch
# the numeric ones, because none of them can occur in the four numeric fields the
# schema has (`score`, `scores.*` are 0-3; `since` is a 4-digit year) and a
# resolver this file invented would be a second dialect to keep in sync. They are
# tabulated above rather than silently left out.
_JS12 = None


def js_yaml_loader():
    """A SafeLoader whose plain-scalar resolution matches js-yaml's default schema.

    Built by REMOVING resolvers rather than adding them: every first character
    PyYAML maps to `tag:yaml.org,2002:bool` or `:timestamp` is filtered, then
    bool is re-registered with js-yaml's own accepted spellings. Anything not
    re-registered falls through to `:str`, which is exactly what js-yaml does.
    """
    global _JS12
    if _JS12 is not None:
        return _JS12
    yaml = yaml_mod()

    class Loader(yaml.SafeLoader):
        pass

    drop = ("tag:yaml.org,2002:bool", "tag:yaml.org,2002:timestamp")
    # copy-on-write: SafeLoader's map is shared, so never mutate it in place
    Loader.yaml_implicit_resolvers = {
        ch: [(tag, rx) for tag, rx in pairs if tag not in drop]
        for ch, pairs in yaml.SafeLoader.yaml_implicit_resolvers.items()
    }
    # js-yaml core bool: true|True|TRUE|false|False|FALSE, and nothing else.
    Loader.add_implicit_resolver(
        "tag:yaml.org,2002:bool",
        re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"),
        list("tTfF"))
    _JS12 = Loader
    return _JS12


def _candidates():
    """Interpreters to try, explicit list first, then EVERY python3 on PATH.

    THE HARDCODED LIST WAS THE BUG. It named `/usr/local/bin/python3` — which on
    this Apple Silicon host is the one interpreter carrying PyYAML, and is also an
    Intel-era path that a `brew cleanup`, a Python upgrade or a different operator's
    machine need not have at all. The build's data gate ran through that single
    absolute path: green here, `ModuleNotFoundError` on any host that happens to
    lay its interpreters out differently, with nothing in the list to fall back to.

    So the list is now a preference, not the whole search. Anything named python3*
    on PATH is probed after it. Ordering still matters and is deliberate — newest
    first — because `row_bytes()` was interpreter-dependent until it was fixed
    (repr() escapes by str.isprintable(), which reads the bundled Unicode database,
    and one signal carries a Unicode 14.0 codepoint unassigned in 3.9's tables).
    Which interpreter wins is therefore a correctness question, not just an
    availability one, and a stable preference order keeps it answerable.
    """
    seen, out = set(), []
    for c in _YAML_CANDIDATES:
        if c not in seen:
            seen.add(c); out.append(c)
    for d in os.environ.get("PATH", "").split(os.pathsep):
        if not d:
            continue
        try:
            names = sorted(os.listdir(d), reverse=True)  # python3.13 before python3.9
        except OSError:
            continue
        for n in names:
            # `python3`, `python3.12` — but NOT `python3.14-config`, `python3-build`
            # and friends, which sit in the same bin dir, are executable, and are not
            # interpreters. The probe below would reject them anyway; excluding them
            # here keeps the candidate list readable when it has to be debugged.
            if not re.fullmatch(r"python3(\.\d+)?", n):
                continue
            p = os.path.join(d, n)
            if p not in seen and os.path.isfile(p) and os.access(p, os.X_OK):
                seen.add(p); out.append(p)
    return out


def ensure_yaml(argv):
    """Guarantee the running interpreter has PyYAML, re-execing once if not."""
    try:
        import yaml  # noqa: F401,PLC0415
        return
    except ImportError:
        pass
    if os.environ.get(_REEXEC_GUARD):
        raise SystemExit(
            f"db: re-exec under {os.environ[_REEXEC_GUARD]} still has no PyYAML. "
            f"Install it: {sys.executable} -m pip install pyyaml")
    me = os.path.realpath(sys.executable)
    for cand in _candidates():
        exe = cand if os.path.isabs(cand) else shutil.which(cand)
        if not exe or not os.path.isfile(exe) or os.path.realpath(exe) == me:
            continue
        try:
            probe = subprocess.run([exe, "-c", "import yaml"], capture_output=True, timeout=30)
        except Exception:  # noqa: BLE001 — an unusable candidate is just skipped
            continue
        if probe.returncode != 0:
            continue
        log(f"db: {sys.executable} has no PyYAML — re-execing under {exe} "
            f"(install pyyaml for the default python3 to retire this shim)")
        env = dict(os.environ)
        env[_REEXEC_GUARD] = exe
        os.execve(exe, [exe, os.path.abspath(__file__)] + list(argv), env)
    raise SystemExit(
        "db: PyYAML is required to read data/problems/**/*.md and no interpreter on this "
        "host has it. Install it: python3 -m pip install pyyaml")


# --------------------------------------------------------------------------
# schema
# --------------------------------------------------------------------------

# Projections of committed files. Dropped and rebuilt at will.
DDL_SIGNALS = """
CREATE TABLE IF NOT EXISTS meta (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS signals (
  id               TEXT PRIMARY KEY,
  source           TEXT NOT NULL,
  type             TEXT NOT NULL,
  date             TEXT NOT NULL,
  entity_name_norm TEXT,
  entity_ico       TEXT,
  entity_domain    TEXT,
  dup_of           TEXT,
  jsonl_file       TEXT NOT NULL,
  jsonl_line       INTEGER NOT NULL,
  raw              TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS signals_date   ON signals(date DESC);
CREATE INDEX IF NOT EXISTS signals_source ON signals(source, date DESC);
CREATE INDEX IF NOT EXISTS signals_type   ON signals(type, date DESC);
CREATE INDEX IF NOT EXISTS signals_ico    ON signals(entity_ico)       WHERE entity_ico IS NOT NULL;
CREATE INDEX IF NOT EXISTS signals_domain ON signals(entity_domain)    WHERE entity_domain IS NOT NULL;
CREATE INDEX IF NOT EXISTS signals_ename  ON signals(entity_name_norm) WHERE entity_name_norm IS NOT NULL;
"""

# ===========================================================================
# schema_version 4 — THE REGISTER. Additive: no table above is altered.
#
# These join DDL_PROJECTIONS, NOT DDL_HISTORY, and the reason is a property
# rather than a preference: problems are deterministically rebuildable from
# data/problems/**, exactly like signals are from data/signals/**. fetch_log
# and match_log are not, which is why they are never dropped.
# ===========================================================================
DDL_PROBLEMS = """
-- ---- the register ---------------------------------------------------------
CREATE TABLE IF NOT EXISTS problems (
  region              TEXT    NOT NULL,
  id                  TEXT    NOT NULL,          -- 'p-0001'; IS the route param
  slug                TEXT    NOT NULL,          -- filename minus .md; read ORDER
  title               TEXT    NOT NULL,
  category            TEXT    NOT NULL,
  geo                 TEXT    NOT NULL,
  status              TEXT    NOT NULL,
  score               INTEGER NOT NULL,
  s_proof             INTEGER NOT NULL,
  s_money             INTEGER NOT NULL,
  s_urgency           INTEGER NOT NULL,
  s_demand            INTEGER NOT NULL,
  s_gap               INTEGER NOT NULL,
  build_capital       TEXT    NOT NULL,
  build_first_revenue TEXT    NOT NULL,
  build_builder       TEXT    NOT NULL,
  build_note          TEXT    NOT NULL,
  created             TEXT    NOT NULL,
  updated             TEXT    NOT NULL,
  body                TEXT    NOT NULL,          -- markdown after frontmatter, .trim()ed
  extra_json          TEXT,                      -- looseObject overflow, verbatim; NULL today
  md_file             TEXT    NOT NULL,          -- 'data/problems/cz/p-0001-....md'
  md_sha256           TEXT    NOT NULL,          -- provenance of this row's source file
  PRIMARY KEY (region, id),
  CHECK (score = s_proof + s_money + s_urgency + s_demand + s_gap),
  CHECK (s_proof   BETWEEN 0 AND 3),
  CHECK (s_money   BETWEEN 0 AND 2),
  CHECK (s_urgency BETWEEN 0 AND 3),
  CHECK (s_demand  BETWEEN 0 AND 2),
  CHECK (s_gap     BETWEEN 0 AND 2),
  CHECK (status IN ('candidate','active','watching','stale','claimed','solved','rejected'))
);
CREATE UNIQUE INDEX IF NOT EXISTS problems_slug ON problems(region, slug);
CREATE INDEX IF NOT EXISTS problems_rank ON problems(status, score DESC, id);
CREATE INDEX IF NOT EXISTS problems_cat  ON problems(category, score DESC, id);
CREATE INDEX IF NOT EXISTS problems_upd  ON problems(updated DESC);

-- ---- sources: `position` IS the S-number, and it is immutable --------------
-- CONVENTIONS.md forbids mid-list insertion because 480 live [Sn] citation
-- markers key off array position (scorecard.ts:85, md.ts:153, page.tsx:411).
-- Any ORDER BY id / natural row order silently renumbers all of them.
CREATE TABLE IF NOT EXISTS problem_sources (
  region       TEXT    NOT NULL,
  problem_id   TEXT    NOT NULL,
  position     INTEGER NOT NULL,      -- 1-based, = S-number, NEVER reassigned
  type         TEXT    NOT NULL,      -- free text today: 'round'/'statistic' are live
  url          TEXT    NOT NULL,
  note         TEXT    NOT NULL,
  date         TEXT    NOT NULL,
  signal_id    TEXT,                  -- ref into signals(id); 101/160 populated
  -- THREE-STATE, and the third state is load-bearing.  NULL = key absent
  -- (fall through to the type map).  '[]' = key present and empty = the
  -- deliberate "attach to nothing" opt-out on 4 live sources.  '["money"]' =
  -- explicit override on 4 more.  A dims join table CANNOT hold this: it
  -- represents absent and empty identically and would re-attach those 4
  -- sources to Demand (proven by HTML diff on /problem/cz/p-0018).
  dims_json    TEXT,
  queries_json TEXT,                  -- 16/160
  checked_json TEXT,                  -- 16/160
  expires      TEXT,                  -- 16/160. DISPLAY-ONLY. Never reaches a number.
  extra_json   TEXT,                  -- looseObject overflow, verbatim
  PRIMARY KEY (region, problem_id, position),
  FOREIGN KEY (region, problem_id) REFERENCES problems(region, id),
  CHECK (position >= 1),
  CHECK (dims_json IS NULL OR json_valid(dims_json))
);
-- THE REVERSE INDEX THAT DOES NOT EXIST TODAY: signal -> problems citing it.
CREATE INDEX IF NOT EXISTS problem_sources_signal
  ON problem_sources(signal_id) WHERE signal_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS problem_sources_type ON problem_sources(type);

-- ---- comparables ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS problem_comps (
  region       TEXT    NOT NULL,
  problem_id   TEXT    NOT NULL,
  position     INTEGER NOT NULL,
  name         TEXT    NOT NULL,
  url          TEXT    NOT NULL,
  geo          TEXT    NOT NULL,      -- ISO2
  since        INTEGER NOT NULL,      -- YAML unquoted int -> must return a JS number
  traction     TEXT    NOT NULL,
  signal_id    TEXT,                  -- 31/76
  markets_json TEXT,                  -- 14/76
  PRIMARY KEY (region, problem_id, position),
  FOREIGN KEY (region, problem_id) REFERENCES problems(region, id),
  CHECK (position >= 1),
  CHECK (markets_json IS NULL OR json_valid(markets_json))
);
CREATE INDEX IF NOT EXISTS problem_comps_signal
  ON problem_comps(signal_id) WHERE signal_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS problem_comps_geo ON problem_comps(geo);

-- ---- the scoring graph ----------------------------------------------------
-- This is the MATERIALISED OUTPUT of web/lib/scorecard.ts dimRefs(), not a
-- projection of the raw `dims` field.  The distinction matters: dimRefs()
-- EARLY-RETURNS on any present `dims` key, so a source with dims:[] yields
-- ZERO rows here and the type map is never consulted for it — which is the
-- behaviour proven correct by HTML diff.  dims_json above stays the authority
-- for round-trip; this table exists so "no source, no point" becomes queryable.
CREATE TABLE IF NOT EXISTS problem_source_dims (
  region     TEXT    NOT NULL,
  problem_id TEXT    NOT NULL,
  position   INTEGER NOT NULL,
  dim        TEXT    NOT NULL CHECK (dim IN ('proof','money','urgency','demand','gap')),
  origin     TEXT    NOT NULL CHECK (origin IN ('explicit','type-map','demand-convention','freshness')),
  PRIMARY KEY (region, problem_id, position, dim),
  FOREIGN KEY (region, problem_id, position)
    REFERENCES problem_sources(region, problem_id, position)
);
CREATE INDEX IF NOT EXISTS problem_source_dims_dim ON problem_source_dims(dim, region, problem_id);

-- ---- synthesis views (cost nothing, rebuilt with the projections) ---------

-- Per-dimension long form: the shape every score query wants.
CREATE VIEW IF NOT EXISTS problem_dim_scores AS
  SELECT region, id AS problem_id, 'proof'   AS dim, s_proof   AS points FROM problems
  UNION ALL SELECT region, id, 'money',   s_money   FROM problems
  UNION ALL SELECT region, id, 'urgency', s_urgency FROM problems
  UNION ALL SELECT region, id, 'demand',  s_demand  FROM problems
  UNION ALL SELECT region, id, 'gap',     s_gap     FROM problems;

-- SCORING.md's central law, made queryable for the first time:
-- "every point must be justified by a sources[] entry — no source, no point."
-- Empty today (0/31 violations) — that is discipline, not a gate. `db.py audit`
-- turns it into one.
CREATE VIEW IF NOT EXISTS score_unbacked AS
SELECT d.region, d.problem_id, d.dim, d.points
FROM problem_dim_scores d
WHERE d.points > 0
  AND NOT EXISTS (
    SELECT 1 FROM problem_source_dims x
     WHERE x.region = d.region AND x.problem_id = d.problem_id AND x.dim = d.dim);

-- ---- the hole score_unbacked cannot see ----------------------------------
-- score_unbacked covers FOUR of the five dimensions. Urgency is exempt by
-- construction, and it is exempt on every record: `dimRefs` unconditionally
-- attaches an urgency ref to the newest source whenever `urgency > 0` and that
-- source is <90 days before extractDate(). Freshness is 1 on 31 of 31 records —
-- and cannot be otherwise while anyone is editing, because extractDate() IS the
-- register's own newest `updated`. So urgency always has a backing row, and
-- MEASURED: p-0002 urgency 1 -> 3 with ZERO urgency-typed sources rebuilds
-- clean, audits "0 unbacked dimensions over 31 records", and renders 3/3
-- FORCING on the site.
--
-- SCORING.md splits urgency: deadline (0-2) + freshness (0-1). Freshness earns
-- its ONE point from the newest-source rule and needs no other evidence. The
-- deadline points do — so the law applies to the deadline sub-score, and that
-- is what this view checks.
--
-- freshness is recomputed here rather than read off `origin`: a source the type
-- map already claimed for urgency keeps origin 'type-map' under the first-writer
-- dedup, so a missing origin='freshness' row does NOT mean freshness was 0.
-- julianday() over ISO dates is exact-integer day arithmetic, matching
-- data.ts daysBetween(); meta.extract_date is the register's own newest
-- `updated` and NEVER the wall clock.
CREATE VIEW IF NOT EXISTS urgency_deadline AS
SELECT p.region, p.id AS problem_id, p.s_urgency,
       MIN(CASE WHEN p.s_urgency > 0
                 AND julianday((SELECT value FROM meta WHERE key = 'extract_date'))
                   - julianday((SELECT MAX(date) FROM problem_sources s
                                 WHERE s.region = p.region AND s.problem_id = p.id)) < 90
                THEN 1 ELSE 0 END, p.s_urgency) AS freshness
  FROM problems p;

CREATE VIEW IF NOT EXISTS deadline_unbacked AS
SELECT u.region, u.problem_id, u.s_urgency, u.freshness,
       MIN(u.s_urgency - u.freshness, 2) AS deadline
  FROM urgency_deadline u
 WHERE MIN(u.s_urgency - u.freshness, 2) > 0
   AND NOT EXISTS (
     SELECT 1 FROM problem_source_dims x
      WHERE x.region = u.region AND x.problem_id = u.problem_id
        AND x.dim = 'urgency' AND x.origin <> 'freshness');

-- The provenance graph, both directions, sources and comps together.
CREATE VIEW IF NOT EXISTS signal_citations AS
  SELECT s.id AS signal_id, s.source, s.type, s.date,
         ps.region, ps.problem_id, ps.position, 'source' AS via
    FROM signals s JOIN problem_sources ps ON ps.signal_id = s.id
  UNION ALL
  SELECT s.id, s.source, s.type, s.date,
         pc.region, pc.problem_id, pc.position, 'comp'
    FROM signals s JOIN problem_comps pc ON pc.signal_id = s.id;

-- 6,181 signals, ~132 cited. This view is the synthesis backlog.
CREATE VIEW IF NOT EXISTS signals_uncited AS
SELECT id, source, type, date, entity_ico, entity_domain, entity_name_norm
  FROM signals
 WHERE id NOT IN (SELECT signal_id FROM signal_citations);

-- problem <-> problem adjacency, derived from shared evidence. Not a guessed
-- link table: it is a fact about what the register already cites.
CREATE VIEW IF NOT EXISTS problem_adjacency AS
SELECT a.region AS a_region, a.problem_id AS a_id,
       b.region AS b_region, b.problem_id AS b_id,
       COUNT(DISTINCT a.signal_id) AS shared_signals
  FROM signal_citations a
  JOIN signal_citations b ON a.signal_id = b.signal_id
   AND (a.region || '/' || a.problem_id) < (b.region || '/' || b.problem_id)
 GROUP BY 1,2,3,4;

-- Closes the H2 defect: today an unresolvable sources[].signal ref crashes the
-- build as `TypeError: Cannot read properties of undefined (reading 'type')`
-- at page.tsx:429, naming no record and no field. 101 of 132 refs are
-- unvalidated (getProblems validates comp refs only). Here they are named rows.
CREATE VIEW IF NOT EXISTS dangling_signal_refs AS
  SELECT region, problem_id, position, signal_id, 'source' AS via
    FROM problem_sources
   WHERE signal_id IS NOT NULL AND signal_id NOT IN (SELECT id FROM signals)
  UNION ALL
  SELECT region, problem_id, position, signal_id, 'comp'
    FROM problem_comps
   WHERE signal_id IS NOT NULL AND signal_id NOT IN (SELECT id FROM signals);
"""

DDL_PROJECTIONS = DDL_SIGNALS + DDL_PROBLEMS

# Everything `rebuild` drops. Views first: a stale view body survives
# `CREATE VIEW IF NOT EXISTS`, so recreating without dropping would silently
# keep yesterday's definition and make a schema edit a no-op.
PROJECTION_VIEWS = ("dangling_signal_refs", "problem_adjacency", "signals_uncited",
                    "signal_citations", "deadline_unbacked", "urgency_deadline",
                    "score_unbacked", "problem_dim_scores")
PROJECTION_TABLES = ("problem_source_dims", "problem_comps", "problem_sources",
                     "problems", "signals", "meta")

# THE HEALTH SPINE and THE MATCH MEMORY. Created if absent, NEVER dropped.
DDL_HISTORY = """
CREATE TABLE IF NOT EXISTS fetch_log (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id        TEXT NOT NULL,
  feed_key      TEXT NOT NULL,
  started_at    TEXT NOT NULL,
  finished_at   TEXT,
  http_status   INTEGER,
  bytes         INTEGER,
  items_fetched INTEGER,
  items_kept    INTEGER,
  yield_anomaly TEXT,
  parse_method  TEXT,
  runtime_ms    INTEGER,
  ok            INTEGER NOT NULL DEFAULT 0,
  error         TEXT,
  raw_path      TEXT
);
CREATE INDEX IF NOT EXISTS fetch_log_feed ON fetch_log(feed_key, started_at DESC);
CREATE INDEX IF NOT EXISTS fetch_log_run  ON fetch_log(run_id);

CREATE TABLE IF NOT EXISTS match_log (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  at         TEXT NOT NULL,
  signal_id  TEXT NOT NULL,
  region     TEXT NOT NULL,
  problem_id TEXT,
  method     TEXT NOT NULL CHECK (method IN ('knn','ico','domain','name','manual')),
  similarity REAL,
  decision   TEXT NOT NULL CHECK (decision IN ('linked','dismissed','deferred','dup')),
  note       TEXT
);
CREATE INDEX IF NOT EXISTS match_log_signal  ON match_log(signal_id);
CREATE INDEX IF NOT EXISTS match_log_problem ON match_log(region, problem_id);
"""


def connect():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA journal_mode = WAL")
    con.execute("PRAGMA synchronous  = NORMAL")
    con.execute("PRAGMA foreign_keys = OFF")  # soft FKs only: derived, never the arbiter
    return con


def ensure_history(con):
    """fetch_log and match_log. Idempotent, and the only way they are ever created."""
    con.executescript(DDL_HISTORY)


def probe_vec(con):
    """
    Probe for sqlite-vec. Returns 'on' or 'off'.

    ABSENCE IS NOT AN ERROR. The extension is not installed on this host; the
    shortlist degrades to entity-key joins, which need no extension. Any failure
    here — missing module, missing dylib, a host that forbids extension loading —
    resolves to 'off' and the rebuild continues.
    """
    try:
        import importlib.util

        if importlib.util.find_spec("sqlite_vec") is None:
            return "off"
        import sqlite_vec  # noqa: F401

        con.enable_load_extension(True)
        sqlite_vec.load(con)
        con.enable_load_extension(False)
        con.execute("CREATE VIRTUAL TABLE IF NOT EXISTS signal_vec USING vec0(id TEXT PRIMARY KEY, embedding float[1536])")
        con.execute("CREATE VIRTUAL TABLE IF NOT EXISTS problem_vec USING vec0(id TEXT PRIMARY KEY, embedding float[1536])")
        return "on"
    except Exception as e:  # noqa: BLE001 — every failure mode means the same thing
        log(f"db: sqlite-vec unavailable ({type(e).__name__}: {e}) — vec=off, "
            f"shortlist degrades to IČO/domain/name joins")
        return "off"


# --------------------------------------------------------------------------
# entity keys — DERIVED-ONLY, DB-only, never written back to the ledgers
# --------------------------------------------------------------------------

# Domains where the URL names the PUBLISHER, INVESTOR or REGISTER — not the
# entity the signal is about. entity_domain exists to feed the match shortlist,
# so a false positive (two unrelated companies sharing a press domain) is far
# worse than a null: a null costs one missed candidate, a false key silently
# merges two companies.
#
# MEASURED, 2026-08-20, and the measurement overturned the first draft of this
# list: before the investor/press entries below were added, 478 of 524 domain
# keys (91%) sat in shared clusters — 246 of them on vestbee.com alone. The
# `round` and `arb-scan` agent harvests overwhelmingly cite the INVESTOR'S
# portfolio page or a trade-press article as `url`, not the company's own site,
# so an un-blocked list produces its worst keys on exactly the funded records
# where an entity match matters most. Re-derive the clusters with:
#     python3 scripts/db.py dupes --report
PLATFORM_DOMAINS = {
    # press / trade media
    "czechcrunch.cz", "tech.eu", "sifted.eu", "techcrunch.com", "forbes.cz",
    "hn.cz", "ihned.cz", "idnes.cz", "ceskatelevize.cz", "denik.cz", "e15.cz",
    "seznamzpravy.cz", "novinky.cz", "aktualne.cz", "irozhlas.cz", "lupa.cz",
    "zive.cz", "root.cz", "respekt.cz", "ekonom.cz", "euro.cz", "tribune.cz",
    "zdravotnickydenik.cz", "businessinfo.cz", "eurozpravy.cz", "ct24.cz",
    # social / publishing platforms
    "reddit.com", "twitter.com", "x.com", "linkedin.com", "facebook.com",
    "youtube.com", "youtu.be", "medium.com", "substack.com", "github.com",
    "github.io", "wordpress.com", "blogspot.com", "notion.site", "google.com",
    "petice.com", "e-petice.cz", "change.org",
    # registers, state portals and aggregators — the URL is the register
    "europa.eu", "ted.europa.eu", "hlidacstatu.cz", "nipez.cz", "justice.cz",
    "gov.cz", "zakonyprolidi.cz", "mvcr.cz", "psp.cz", "nku.cz", "sukl.cz",
    "mpsv.cz", "ochrance.cz", "uohs.cz", "cnb.cz", "czso.cz", "coi.gov.cz",
    "crunchbase.com", "pitchbook.com", "dealroom.co", "ycombinator.com",
    # accelerators / investor portfolio pages (measured in this corpus)
    "startupyard.com", "reflexcapital.com", "vestbee.com", "techstars.com",
    "rockstart.com", "seedcamp.com", "eithealth.eu", "eiturbanmobility.eu",
    "prestoventures.com", "palefirecapital.com", "dayonecapital.com",
    "invencapital.cz", "crowdberry.eu", "miton.cz", "superscout.co",
    "strata.team", "jtventures.cz",
    # startup / funding trade press (measured in this corpus)
    "cc.cz", "eu-startups.com", "arcticstartup.com", "therecursive.com",
    "techfundingnews.com", "ceskenoviny.cz", "datacenterdynamics.com",
    # EU operational-programme and civic portals — the programme, not a company
    "opzp.cz", "opjak.cz", "rozhodnetesami.cz",
    # advisory firms writing ABOUT a regulation; the entity is the regulation
    "ey.com", "clearygottlieb.com",
}

# A PROHIBITION rather than an enumeration, because it survives the variant the
# corpus did not happen to contain: .vc and .ventures are investor TLDs almost
# by definition. Measured hits in this corpus — inovo.vc, otb.vc, zaka.vc,
# kaya.vc, 11.vc, moc.vc, tensor.ventures — were every single .vc/.ventures
# domain present, with zero operating companies among them.
BLOCKED_TLDS = {"vc", "ventures"}

# Public-suffix shortcuts. .cz has no registered second level, so the default
# last-two-labels rule is right for the overwhelming majority of this corpus;
# these are the multi-part suffixes that rule would get wrong.
MULTI_SUFFIXES = {
    "co.uk", "org.uk", "ac.uk", "gov.uk", "me.uk", "net.uk", "sch.uk",
    "com.au", "net.au", "org.au", "co.nz", "co.jp", "co.kr", "com.br",
    "com.mx", "co.za", "com.tr", "com.sg", "com.hk", "co.il", "com.cn",
    "co.in", "com.ar", "com.pl", "gov.cz",
}

# Legal-form suffixes cut from entity_name_norm before comparison.
NAME_SUFFIXES = [
    "spol s r o", "s r o", "a s", "z s", "o p s", "z u", "s p", "k s",
    "v o s", "p o", "gmbh", "ag", "sa", "nv", "bv", "oy", "ab", "as",
    "sp z o o", "kft", "srl", "sarl", "plc", "ltd", "llc", "inc", "corp",
    "co", "limited", "holding", "group", "se",
]

_WORD_RE = re.compile(r"[^\w\s]", re.UNICODE)
_WS_RE = re.compile(r"\s+")


def norm_name(name):
    """
    NFKD, diacritics stripped, punctuation dropped, legal-form suffixes cut,
    lowercased and whitespace-collapsed. Returns None when nothing survives.
    """
    if not name:
        return None
    s = unicodedata.normalize("NFKD", str(name))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = _WORD_RE.sub(" ", s)
    s = _WS_RE.sub(" ", s).strip()
    if not s:
        return None
    # Cut trailing legal-form suffixes, longest first, repeatedly.
    changed = True
    while changed:
        changed = False
        for suf in sorted(NAME_SUFFIXES, key=len, reverse=True):
            if s.endswith(" " + suf):
                s = s[: -(len(suf) + 1)].strip()
                changed = True
                break
    return s or None


def valid_ico(s):
    """
    Czech IČO: 8 digits, the last a mod-11 check digit over weights 8..2.
    The checksum is MANDATORY — without it every 8-digit run in a summary
    (a price, a year range, a postcode pair) would mint a false entity key,
    and a false key silently corrupts the match shortlist.
    """
    if not s or len(s) != 8 or not s.isdigit():
        return False
    digits = [int(c) for c in s]
    total = sum(d * w for d, w in zip(digits[:7], range(8, 1, -1)))
    r = total % 11
    if r == 0:
        check = 1
    elif r == 1:
        check = 0
    else:
        check = 11 - r
    return check == digits[7]


_ICO_RE = re.compile(r"(?<!\d)(\d{8})(?!\d)")


def extract_ico(*texts):
    """First checksum-valid 8-digit run across the given texts, else None."""
    for t in texts:
        if not t:
            continue
        for m in _ICO_RE.finditer(str(t)):
            if valid_ico(m.group(1)):
                return m.group(1)
    return None


def etld1(url):
    """
    eTLD+1 from a URL, or None. Deliberately small: a known multi-part suffix
    table plus a last-two-labels default. Platform domains resolve to None.
    """
    if not url:
        return None
    m = re.match(r"^[a-zA-Z][\w+.-]*://([^/?#]+)", str(url))
    host = (m.group(1) if m else str(url).split("/")[0]).lower()
    host = host.split("@")[-1].split(":")[0].strip(".")
    if not host or re.match(r"^[\d.]+$", host):
        return None
    parts = [p for p in host.split(".") if p]
    if len(parts) < 2:
        return None
    if len(parts) >= 3 and ".".join(parts[-2:]) in MULTI_SUFFIXES:
        dom = ".".join(parts[-3:])
    else:
        dom = ".".join(parts[-2:])
    if parts[-1] in BLOCKED_TLDS:
        return None
    if dom in PLATFORM_DOMAINS or ".".join(parts[-2:]) in PLATFORM_DOMAINS:
        return None
    if host in PLATFORM_DOMAINS:
        return None
    return dom


def entity_from_title(title):
    """
    CONVENTIONS.md specifies the title field as a `short English display name,
    "Thing — what it is"`, so the segment before the em dash is the entity.

    MEASURED over the committed corpus, 2026-08-20: 6,174 of 6,181 titles carry
    ' — ' (99.9%); 7 do not. Re-derive with:
        python3 -c "import json,glob;ts=[json.loads(l)['title'] for f in
        glob.glob('data/signals/*/*.jsonl') for l in open(f) if l.strip()];
        print(sum(' — ' in t for t in ts), len(ts))"
    The 7 without a separator fall back to the whole title, which is the honest
    degradation — a slightly noisier key, never a wrong one.
    """
    if not title:
        return None
    for sep in (" — ", " – ", " -- "):
        if sep in title:
            return title.split(sep, 1)[0].strip()
    return title.strip()


def derive_entity_keys(rec):
    """Compute the three DERIVED-ONLY entity keys for one signal record."""
    name = entity_from_title(rec.get("title"))
    return (
        norm_name(name),
        extract_ico(rec.get("notes"), rec.get("summary"), rec.get("money_note"), rec.get("url")),
        etld1(rec.get("url")),
    )


# --------------------------------------------------------------------------
# reading the canonical ledgers
# --------------------------------------------------------------------------

def evidence_types():
    """Directories under data/signals/ ARE the evidence types (the DDL says so).
    Discovered, never hard-coded, so `hiring/` works the day it lands."""
    if not os.path.isdir(SIGNALS_DIR):
        return []
    return sorted(
        d for d in os.listdir(SIGNALS_DIR)
        if os.path.isdir(os.path.join(SIGNALS_DIR, d)) and not d.startswith(".")
    )


def iter_jsonl(path, rel):
    """Yield (line_no, raw_line, record). line_no is 1-based, matching the
    build's own error reporting. Blank lines are skipped and not counted."""
    with open(path, "r", encoding="utf-8") as fh:
        for n, line in enumerate(fh, start=1):
            raw = line.rstrip("\n")
            if not raw.strip():
                continue
            try:
                rec = json.loads(raw)
            except json.JSONDecodeError as e:
                raise SystemExit(f"db: {rel}:{n}: not valid JSON — {e}")
            yield n, raw, rec


def ledger_files():
    """Every committed JSONL ledger, as (abs_path, repo_relative_path, type)."""
    out = []
    for typ in evidence_types():
        d = os.path.join(SIGNALS_DIR, typ)
        for f in sorted(os.listdir(d)):
            if f.endswith(".jsonl"):
                out.append((os.path.join(d, f), f"data/signals/{typ}/{f}", typ))
    return out


def insert_records(con, path, rel, typ, seen_ids):
    """Insert every record of one ledger file. Returns (lines_read, rows_written)."""
    lines = 0
    rows = []
    for n, raw, rec in iter_jsonl(path, rel):
        lines += 1
        sid = rec.get("id")
        if not sid:
            raise SystemExit(f"db: {rel}:{n}: record has no id")
        if sid in seen_ids:
            raise SystemExit(
                f"db: {rel}:{n}: duplicate signal id '{sid}' (first seen in {seen_ids[sid]}). "
                f"The ledgers are append-only and ids must be unique across the whole corpus."
            )
        seen_ids[sid] = f"{rel}:{n}"
        ename, ico, domain = derive_entity_keys(rec)
        rows.append((sid, rec.get("source"), typ, rec.get("date"),
                     ename, ico, domain, None, rel, n, raw))
    con.executemany(
        "INSERT INTO signals (id, source, type, date, entity_name_norm, entity_ico,"
        " entity_domain, dup_of, jsonl_file, jsonl_line, raw)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?)", rows)
    return lines, len(rows)


def row_bytes(row):
    """Serialise one result row for a digest, IDENTICALLY ON EVERY INTERPRETER.

    `repr(row)` is NOT a stable serialisation, and the corpus already contains
    the counter-example. `repr()` escapes any character `str.isprintable()`
    calls unprintable, and that verdict is read out of the bundled Unicode
    database — which moves with the Python version. MEASURED on this host:
    signal `yc-neoncoral` carries U+1FAB8 CORAL, assigned in Unicode 14.0, so

        Python 3.9.6  (Unicode 13.0)  repr -> '\\U0001fab8'
        Python 3.12.1 (Unicode 15.0)  repr -> '🪸'

    and `db.py rebuild` on ONE unchanged tree produced signals_digest
    68bf2849… under 3.12 and da22d307… under 3.9. That falsifies the property
    the digest exists to assert, and it does it silently: an operator on the
    other interpreter reads "the content changed" off a tree that did not.
    It matters more since `rebuild` re-execs under whichever interpreter on the
    host happens to carry PyYAML.

    json.dumps with ensure_ascii=True emits pure ASCII \\uXXXX escapes decided by
    code point alone, and covers every type these columns hold (str/int/None).
    """
    return json.dumps(list(row), ensure_ascii=True).encode("ascii")


def signals_digest(con):
    """
    Deterministic content digest of the signals table, ordered by id. Two
    rebuilds of the same tree produce the same digest — which is what makes
    idempotency checkable without diffing a binary. `meta.rebuilt_at` is a
    timestamp and is deliberately excluded.
    """
    h = hashlib.sha256()
    for row in con.execute(
        "SELECT id, source, type, date, entity_name_norm, entity_ico,"
        " entity_domain, dup_of, jsonl_file, jsonl_line, raw"
        " FROM signals ORDER BY id"
    ):
        h.update(row_bytes(row))
    return h.hexdigest()


# --------------------------------------------------------------------------
# reading the canonical register — data/problems/<region>/*.md
# --------------------------------------------------------------------------
#
# This is a PORT, not a reimplementation. Every function below mirrors a named
# function in web/lib/, and where the JS does something surprising the port
# does the same surprising thing on purpose:
#
#   parse_frontmatter   <- data.ts parseFrontmatter   (the "\n---\n" scan, .trim())
#   problem_files       <- data.ts getProblems        (region dirs, files sorted)
#   extract_date        <- data.ts extractDate        (max `updated`, no wall clock)
#   urgency_split       <- data.ts urgencySplit
#   dim_refs            <- scorecard.ts dimRefs       (INCLUDING the early return)
#
# The site is the authority on what these mean. If the two ever disagree, the
# port is wrong, not the page.

PROBLEM_KEYS = frozenset((
    "id", "region", "title", "category", "geo", "score", "scores", "status",
    "build", "comps", "sources", "created", "updated"))
SOURCE_KEYS = frozenset((
    "type", "url", "note", "date", "signal", "dims", "queries", "checked", "expires"))
COMP_KEYS = frozenset(("name", "url", "geo", "since", "traction", "signal", "markets"))
BUILD_KEYS = frozenset(("capital", "first_revenue", "builder", "note"))
SCORE_KEYS = frozenset(("proof", "money", "urgency", "demand", "gap"))

DIMS = ("proof", "money", "urgency", "demand", "gap")

# scorecard.ts:69-75, verbatim. `news` mapping to demand is the live behaviour
# and is ported as-is: five records carry a demand-resolving `news` source while
# scoring demand 0, which is a CONTENT contradiction for the owner to rule on,
# not a licence for this port to quietly disagree with the page.
TYPE_TO_DIM = {
    "arbitrage": "proof",
    "tender": "money", "contract": "money", "subsidy": "money",
    "regulation": "urgency",
    "complaint": "demand", "news": "demand",
    "gap-check": "gap",
}

# ECMAScript String.prototype.trim() strips WhiteSpace + LineTerminator, which
# is NOT Python's str.strip() set (Python also strips e.g. U+001C-U+001F and
# treats U+0085 as space; JS does not). The body column has to match the string
# the site renders byte for byte, so the set is spelled out rather than assumed.
_JS_WS = (
    "\t\n\v\f\r\u0020\u00a0\u1680"
    "\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a"
    "\u2028\u2029\u202f\u205f\u3000\ufeff"
)


def js_trim(s):
    """String.prototype.trim(), exactly."""
    return s.strip(_JS_WS)


def parse_frontmatter(raw, rel):
    """data.ts parseFrontmatter — the same scan, the same failure messages."""
    if not raw.startswith("---\n"):
        raise SystemExit(f"db: {rel}: missing frontmatter")
    end = raw.find("\n---\n", 4)
    if end == -1:
        raise SystemExit(f"db: {rel}: unterminated frontmatter")
    fm = yaml_mod().load(raw[4:end], Loader=js_yaml_loader())
    if not isinstance(fm, dict):
        raise SystemExit(f"db: {rel}: frontmatter is not a mapping")
    return fm, js_trim(raw[end + 5:])


def problem_files():
    """(abs_path, repo_relative, region, slug) for every problem markdown.

    Mirrors getProblems(): REGION DIRECTORIES under data/problems/, and inside
    each, `.md` files in filename order. `.claude/` and any other non-.md entry
    is skipped exactly as the site skips it.

    Sorting happens HERE, in Python, and never with an ORDER BY. Python orders
    str by code point and SQLite's default collation is BINARY over UTF-8; they
    agree on today's all-ASCII slugs and would diverge silently on the first
    non-ASCII one. Same hazard the web loader has, resolved the same way.
    """
    out = []
    if not os.path.isdir(PROBLEMS_DIR):
        return out
    for region in sorted(os.listdir(PROBLEMS_DIR)):
        rdir = os.path.join(PROBLEMS_DIR, region)
        if not os.path.isdir(rdir) or region.startswith("."):
            continue
        for f in sorted(os.listdir(rdir)):
            if not f.endswith(".md"):
                continue
            out.append((os.path.join(rdir, f), f"data/problems/{region}/{f}",
                        region, f[:-3]))
    return out


# data.ts:19 — `const isoDate = z.string().regex(/^\d{4}-\d{2}-\d{2}$/)`. Applied
# to created, updated, sources[].date and sources[].expires.
_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _require_date(rel, where, value):
    """A frontmatter date must be what `isoDate` accepts — SAME test as the site.

    THE EARLIER VERSION OF THIS CHECK ASSERTED SOMETHING FALSE. It required a
    `str` on the grounds that "js-yaml resolves an unquoted date to a Date and
    the web build fails zod's z.string()". Measured: js-yaml returns the plain
    STRING "2026-07-09", the site builds green, and `db.py rebuild` was the only
    thing rejecting the record — a gate failing on data the register accepts.
    With `js_yaml_loader()` in place the type question is gone (both parsers now
    return a string), so what is left is the check the site actually performs.

    It also converts the one crash this loader could still produce into a named
    one: `date.fromisoformat()` on a non-ISO string raised a bare
    `ValueError: Invalid isoformat string` from inside `urgency_split`, naming no
    record and no field — and it raised it on ONE interpreter and not another,
    because 3.11 widened `fromisoformat` to accept `20260709` and `2026-W28-1`
    while 3.9 accepts neither. The regex is the same on every interpreter.
    """
    if isinstance(value, str) and _ISO_DATE.match(value):
        return value
    shown = f"{value!r}" if not isinstance(value, str) else f"'{value}'"
    raise SystemExit(
        f"db: {rel}: {where} is {shown} — data.ts requires /^\\d{{4}}-\\d{{2}}-\\d{{2}}$/ "
        f"(zod `isoDate`), so the web build rejects this record too.")


def _overflow(obj, known):
    """looseObject overflow, verbatim and deterministic. NULL when there is none."""
    extra = {k: v for k, v in obj.items() if k not in known}
    return json.dumps(extra, ensure_ascii=False, sort_keys=True) if extra else None


def _jsonl_or_none(obj, key):
    """json.dumps of the parsed value, NULL when the key is ABSENT.

    The distinction is the whole point on `dims`: absent means "fall through to
    the type map", present-and-empty means "attach to nothing". `not in` is the
    test, never truthiness — `[]` is falsy in Python and TRUTHY in JS, and that
    single asymmetry is what a naive port gets wrong.
    """
    if key not in obj:
        return None
    return json.dumps(obj[key], ensure_ascii=False)


def extract_date(problems):
    """data.ts extractDate(): the register's own newest `updated`. Never the
    wall clock — one commit must produce one database on any day it is built."""
    if not problems:
        return "1970-01-01"
    return max(p["fm"]["updated"] for p in problems)


def urgency_split(fm, extract):
    """data.ts urgencySplit(). Returns (deadline, freshness).

    daysBetween() is Math.round over exact UTC midnights, i.e. an exact day
    count, so date arithmetic reproduces it without rounding.
    """
    urgency = fm["scores"]["urgency"]
    if urgency == 0:
        return 0, 0
    newest = max(s["date"] for s in fm["sources"])
    days = (date.fromisoformat(extract) - date.fromisoformat(newest)).days
    fresh = 1 if days < 90 else 0
    freshness = min(fresh, urgency)
    return min(urgency - freshness, 2), freshness


def newest_source_index(sources):
    """The index scorecard.ts:97 picks for the freshness ref.

    JS: `[...sources.entries()].sort((a,b) => a[1].date.localeCompare(b[1].date)).at(-1)`.
    Array.prototype.sort is STABLE, so on a tie for the newest date the LAST
    source in file order wins. Python's max() returns the FIRST maximum, which
    is the opposite — hence the explicit `>=` scan rather than max().
    """
    best = 0
    for i, s in enumerate(sources):
        if s["date"] >= sources[best]["date"]:
            best = i
    return best


def dim_refs(fm, extract):
    """scorecard.ts dimRefs(), materialised as (position, dim, origin) rows.

    THE EARLY RETURN IS THE WHOLE TRICK. `if (s.dims)` is a TRUTHINESS test in
    JS and an empty array is truthy there, so a source carrying `dims: []`
    takes the branch, iterates nothing, and RETURNS — the type map is never
    consulted for it and it backs zero dimensions. Four live sources depend on
    that (p-0003 S?, p-0004 S?, p-0018 S3 and S4); deleting their `dims: []`
    keys measurably ADDS rows here, which is the falsification test for this
    function.

    `dims: null` (a bare `dims:` key) is falsy in JS and must fall THROUGH, so
    the test below is `is not None` and not `in fm`.

    `origin` records which of the four rules put the row here, and the dedup
    mirrors the JS `add` closure exactly: first writer wins, so a source the
    type map already attached to urgency keeps origin 'type-map' when freshness
    would have attached it again.
    """
    seen = set()
    rows = []

    def add(dim, n, origin):
        if (dim, n) in seen:
            return
        seen.add((dim, n))
        rows.append((n, dim, origin))

    for i, s in enumerate(fm["sources"]):
        n = i + 1
        dims = s.get("dims")
        if dims is not None:                     # <- the early return
            for d in dims:
                add(d, n, "explicit")
            continue
        dim = TYPE_TO_DIM.get(s.get("type"))
        if dim:
            add(dim, n, "type-map")
        if s.get("type") == "gap-check" and "Demand point" in s["note"]:
            add("demand", n, "demand-convention")

    _, freshness = urgency_split(fm, extract)
    if freshness:
        add("urgency", newest_source_index(fm["sources"]) + 1, "freshness")
    return rows


def read_problems():
    """Parse every problem markdown. Returns (records, warnings)."""
    records, warnings = [], []
    for path, rel, region, slug in problem_files():
        with open(path, "rb") as fh:
            blob = fh.read()
        fm, body = parse_frontmatter(blob.decode("utf-8"), rel)

        missing = sorted(k for k in PROBLEM_KEYS if k not in fm)
        if missing:
            raise SystemExit(f"db: {rel}: frontmatter missing {', '.join(missing)}")
        if fm["region"] != region:
            raise SystemExit(f"db: {rel}: region '{fm['region']}' != directory '{region}'")
        for k in ("created", "updated"):
            _require_date(rel, k, fm[k])
        if not isinstance(fm["sources"], list) or not fm["sources"]:
            raise SystemExit(f"db: {rel}: sources[] must be a non-empty list")
        if not isinstance(fm["comps"], list):
            raise SystemExit(f"db: {rel}: comps must be a list")

        for n, s in enumerate(fm["sources"], 1):
            for k in ("type", "url", "note"):
                if k not in s:
                    raise SystemExit(f"db: {rel}: sources[{n}] missing {k}")
            _require_date(rel, f"sources[{n}].date", s.get("date"))
            # `expires` is optional, but when present the site types it `isoDate`
            # too — and it lands in a TEXT column, so a non-string here used to
            # ride in on sqlite3's deprecated default date adapter.
            if "expires" in s:
                _require_date(rel, f"sources[{n}].expires", s["expires"])
            # SourceSchema is z.looseObject: an unknown key PASSES, unvalidated,
            # and renders NOTHING. That is the opposite of the z.object cases
            # below — there zod strips the key, here it keeps it — and it is the
            # dangerous direction, because a typo'd receipt (`expiers`,
            # `chekced`, `dimms`) then sits in the frontmatter looking like data
            # while backing no score, flagging no staleness and printing no
            # coverage. Nothing else in the repo says a word about it: measured,
            # all three of those typos build green through `rebuild`, `audit` and
            # `npm run build`. This is the only place that holds both the record
            # and the key list, so it is the only place that can say so.
            extra = sorted(set(s) - SOURCE_KEYS)
            if extra:
                warnings.append(
                    f"{rel}: sources[{n}] carries unknown key(s) {', '.join(extra)} — "
                    f"z.looseObject PASSES them unvalidated and the site renders "
                    f"nothing for them. Misspelling of {', '.join(sorted(SOURCE_KEYS))}?")
        for n, c in enumerate(fm["comps"], 1):
            for k in ("name", "url", "geo", "since", "traction"):
                if k not in c:
                    raise SystemExit(f"db: {rel}: comps[{n}] missing {k}")
            if not isinstance(c["since"], int) or isinstance(c["since"], bool):
                raise SystemExit(
                    f"db: {rel}: comps[{n}].since is {c['since']!r} — CONVENTIONS.md "
                    f"requires an UNQUOTED integer year (the site reads it as a number)")

        # ProblemSchema is z.looseObject as well — same pass-through, same silence.
        extra = sorted(set(fm) - PROBLEM_KEYS)
        if extra:
            warnings.append(
                f"{rel}: frontmatter carries unknown top-level key(s) {', '.join(extra)} — "
                f"z.looseObject PASSES them unvalidated; kept verbatim in problems.extra_json")

        # z.object STRIPS unknown keys on build / scores / comps, so an extra key
        # there never reaches the site and has no column here. Say so out loud
        # rather than dropping it the way zod does, silently.
        for label, obj, known in (("build", fm["build"], BUILD_KEYS),
                                  ("scores", fm["scores"], SCORE_KEYS)):
            extra = sorted(set(obj) - known)
            if extra:
                warnings.append(f"{rel}: {label} carries {', '.join(extra)} — z.object "
                                f"strips it, so it reaches neither the site nor this DB")
        for n, c in enumerate(fm["comps"], 1):
            extra = sorted(set(c) - COMP_KEYS)
            if extra:
                warnings.append(f"{rel}: comps[{n}] carries {', '.join(extra)} — z.object "
                                f"strips it, so it reaches neither the site nor this DB")

        records.append({
            "fm": fm, "body": body, "rel": rel, "region": region, "slug": slug,
            "sha256": hashlib.sha256(blob).hexdigest(),
        })

    ids = {}
    for r in records:
        key = (r["region"], r["fm"]["id"])
        if key in ids:
            raise SystemExit(f"db: duplicate problem id {key[0]}/{key[1]} "
                             f"({ids[key]} and {r['rel']})")
        ids[key] = r["rel"]
    return records, warnings


def _insert_named(con, sql, rows, describe):
    """executemany, but a constraint failure NAMES THE ROW that caused it.

    A bare executemany raises `sqlite3.IntegrityError: CHECK constraint failed:
    score = s_proof + ...` naming no record and no file — the same
    unactionable-error defect as the page.tsx:429 TypeError this schema exists
    to close. On failure the batch is replayed one row at a time, which costs a
    few hundred inserts exactly once, on the run that was going to fail anyway.
    """
    try:
        con.executemany(sql, rows)
        return
    except sqlite3.IntegrityError as e:
        # Rebound deliberately: Python DELETES the `as` name at the end of the
        # except block, so referring to it in the fallback raise below is a
        # NameError that only fires on the rarest path — the failure mode this
        # whole helper exists to prevent.
        batch_err = str(e)
    # Replay into a THROWAWAY in-memory database, never into `con`. The failed
    # executemany left part of the batch behind, so replaying against the real
    # table hits a UNIQUE violation on an already-inserted row and names the
    # wrong record — measured, and it named p-0001 for a defect planted in
    # p-0012. A clean schema reproduces the row-level constraint honestly.
    scratch = sqlite3.connect(":memory:")
    scratch.executescript(DDL_PROJECTIONS)
    for row in rows:
        try:
            scratch.execute(sql, row)
        except sqlite3.IntegrityError as e:
            scratch.close()
            raise SystemExit(f"db: FAIL — {describe(row)}: {e}")
    scratch.close()
    raise SystemExit(f"db: FAIL — batch insert failed ({batch_err}) but no single row "
                     f"reproduces it against a clean schema. Suspect a duplicate key "
                     f"BETWEEN batches rather than a CHECK violation.")


def insert_problems(con, records):
    """Write problems / problem_sources / problem_comps / problem_source_dims."""
    extract = extract_date(records)
    prows, srows, crows, drows = [], [], [], []
    for r in records:
        fm, region, pid = r["fm"], r["region"], r["fm"]["id"]
        sc = fm["scores"]
        b = fm["build"]
        prows.append((
            region, pid, r["slug"], fm["title"], fm["category"], fm["geo"],
            fm["status"], fm["score"],
            sc["proof"], sc["money"], sc["urgency"], sc["demand"], sc["gap"],
            b["capital"], b["first_revenue"], b["builder"], b["note"],
            fm["created"], fm["updated"], r["body"],
            _overflow(fm, PROBLEM_KEYS), r["rel"], r["sha256"]))

        for i, s in enumerate(fm["sources"]):
            srows.append((
                region, pid, i + 1, s["type"], s["url"], s["note"], s["date"],
                s.get("signal"), _jsonl_or_none(s, "dims"),
                _jsonl_or_none(s, "queries"), _jsonl_or_none(s, "checked"),
                s.get("expires"), _overflow(s, SOURCE_KEYS)))

        for i, c in enumerate(fm["comps"]):
            crows.append((
                region, pid, i + 1, c["name"], c["url"], c["geo"], c["since"],
                c["traction"], c.get("signal"), _jsonl_or_none(c, "markets")))

        for position, dim, origin in dim_refs(fm, extract):
            drows.append((region, pid, position, dim, origin))

    _insert_named(con,
                  "INSERT INTO problems (region, id, slug, title, category, geo, status,"
                  " score, s_proof, s_money, s_urgency, s_demand, s_gap, build_capital,"
                  " build_first_revenue, build_builder, build_note, created, updated, body,"
                  " extra_json, md_file, md_sha256)"
                  " VALUES (" + ",".join("?" * 23) + ")", prows,
                  lambda r: f"{r[21]} ({r[0]}/{r[1]})")
    _insert_named(con,
                  "INSERT INTO problem_sources (region, problem_id, position, type, url,"
                  " note, date, signal_id, dims_json, queries_json, checked_json, expires,"
                  " extra_json) VALUES (" + ",".join("?" * 13) + ")", srows,
                  lambda r: f"{r[0]}/{r[1]} sources[{r[2]}]")
    _insert_named(con,
                  "INSERT INTO problem_comps (region, problem_id, position, name, url, geo,"
                  " since, traction, signal_id, markets_json)"
                  " VALUES (" + ",".join("?" * 10) + ")", crows,
                  lambda r: f"{r[0]}/{r[1]} comps[{r[2]}] '{r[3]}'")
    _insert_named(con,
                  "INSERT INTO problem_source_dims (region, problem_id, position, dim, origin)"
                  " VALUES (?,?,?,?,?)", drows,
                  lambda r: f"{r[0]}/{r[1]} sources[{r[2]}] dim={r[3]} origin={r[4]}")
    return extract, len(prows), len(srows), len(crows), len(drows)


def problems_digest(con):
    """Deterministic content digest over problems + sources + comps + dims,
    ordered by (region, id, position). Mirrors signals_digest(): two rebuilds of
    the same tree produce the same hex, and `rebuilt_at` is excluded because a
    timestamp would make every rebuild look like a content change.

    The section label goes into the hash so a row cannot migrate between tables
    without moving the digest.
    """
    h = hashlib.sha256()
    for label, sql in (
        ("problems", "SELECT region, id, slug, title, category, geo, status, score,"
                     " s_proof, s_money, s_urgency, s_demand, s_gap, build_capital,"
                     " build_first_revenue, build_builder, build_note, created, updated,"
                     " body, extra_json, md_file, md_sha256"
                     " FROM problems ORDER BY region, id"),
        ("sources", "SELECT region, problem_id, position, type, url, note, date, signal_id,"
                    " dims_json, queries_json, checked_json, expires, extra_json"
                    " FROM problem_sources ORDER BY region, problem_id, position"),
        ("comps", "SELECT region, problem_id, position, name, url, geo, since, traction,"
                  " signal_id, markets_json"
                  " FROM problem_comps ORDER BY region, problem_id, position"),
        ("dims", "SELECT region, problem_id, position, dim, origin FROM problem_source_dims"
                 " ORDER BY region, problem_id, position, dim"),
    ):
        h.update(("\x00" + label + "\x00").encode("utf-8"))
        for row in con.execute(sql):
            h.update(row_bytes(row))     # NOT repr() — see row_bytes
    return h.hexdigest()


def git_head():
    try:
        out = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"],
                             capture_output=True, text=True, timeout=10)
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:  # noqa: BLE001 — a missing git is not a rebuild failure
        pass
    return "unknown"


def set_meta(con, **kv):
    con.executemany("INSERT OR REPLACE INTO meta (key, value) VALUES (?,?)",
                    [(k, str(v)) for k, v in kv.items()])


def get_meta(con, k, default=None):
    """A missing `meta` table means "never rebuilt", not a crash. connect()
    CREATES an empty register.db on first touch, so every read path has to
    survive one — otherwise `audit` on a fresh checkout tracebacks instead of
    telling the operator to run `rebuild`."""
    try:
        row = con.execute("SELECT value FROM meta WHERE key = ?", (k,)).fetchone()
    except sqlite3.OperationalError:
        return default
    return row[0] if row else default


# --------------------------------------------------------------------------
# rebuild
# --------------------------------------------------------------------------

def cmd_rebuild(args):
    con = connect()
    ensure_history(con)          # BEFORE the drop: history is created, never destroyed
    vec = probe_vec(con)

    # DROP + recreate ONLY the projections. fetch_log and match_log are untouched
    # — this is the line that protects history no rebuild could reconstruct.
    con.executescript("".join(f"DROP VIEW IF EXISTS {v};" for v in PROJECTION_VIEWS))
    con.executescript("".join(f"DROP TABLE IF EXISTS {t};" for t in PROJECTION_TABLES))
    con.executescript(DDL_PROJECTIONS)

    seen_ids = {}
    total_lines = 0
    per_file = []
    for path, rel, typ in ledger_files():
        lines, rows = insert_records(con, path, rel, typ, seen_ids)
        total_lines += lines
        per_file.append((rel, lines))

    signals_count = con.execute("SELECT COUNT(*) FROM signals").fetchone()[0]

    # THE REGISTER, after the signals pass — problem_sources.signal_id points
    # into signals(id), and `dangling_signal_refs` can only name a broken ref
    # once the target table is populated.
    records, warnings = read_problems()
    md_files = len(records)
    for w in warnings:
        log(f"db: WARN — {w}")
    extract, n_problems, n_sources, n_comps, n_dims = insert_problems(con, records)

    set_meta(con,
             schema_version=SCHEMA_VERSION,
             rebuilt_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             git_head=git_head(),
             jsonl_lines=total_lines,
             signals_count=signals_count,
             md_files=md_files,
             problems_count=n_problems,
             problem_sources_count=n_sources,
             problem_comps_count=n_comps,
             problem_source_dims_count=n_dims,
             extract_date=extract,
             vec=vec)
    con.commit()

    # THE INTEGRITY ASSERTIONS — one per canonical corpus, each of the same
    # shape: files read == rows written. A mismatch means a duplicate id or a
    # parse failure, and it exits non-zero rather than leaving a quietly short
    # database. Neither is pinned to a literal count (31 today, 32 next week):
    # a magic number would fail on the first new record, which is the one thing
    # the register is FOR.
    if total_lines != signals_count:
        log(f"db: FAIL — jsonl_lines ({total_lines}) != signals_count ({signals_count})")
        con.close()
        return 1
    if md_files != n_problems:
        log(f"db: FAIL — md_files ({md_files}) != problems_count ({n_problems})")
        con.close()
        return 1

    # AC-F3 — TOTALITY. Every id prefix in the ledgers must be claimed by a
    # registry row, or this rebuild fails and names the orphans. A record with
    # no feed key has no contract and no health check, so /sources would imply
    # coverage that does not exist — which is the failure that page exists to
    # prevent. Enforced here, at the point every record is read.
    if cmd_prefixes(argparse.Namespace(verbose=False)) != 0:
        con.close()
        return 1

    digest = signals_digest(con)
    pdigest = problems_digest(con)
    set_meta(con, signals_digest=digest, problems_digest=pdigest)
    con.commit()
    ico = con.execute("SELECT COUNT(*) FROM signals WHERE entity_ico IS NOT NULL").fetchone()[0]
    dom = con.execute("SELECT COUNT(*) FROM signals WHERE entity_domain IS NOT NULL").fetchone()[0]
    nam = con.execute("SELECT COUNT(*) FROM signals WHERE entity_name_norm IS NOT NULL").fetchone()[0]
    fl = con.execute("SELECT COUNT(*) FROM fetch_log").fetchone()[0]
    ml = con.execute("SELECT COUNT(*) FROM match_log").fetchone()[0]
    cited = con.execute("SELECT COUNT(DISTINCT signal_id) FROM signal_citations").fetchone()[0]
    con.close()

    if args.verbose:
        for rel, lines in per_file:
            print(f"  {rel:44s} {lines:6d}")
        for r in records:
            print(f"  {r['rel']:44s} {len(r['fm']['sources']):3d} src "
                  f"{len(r['fm']['comps']):3d} comp")
    print(f"rebuild OK  jsonl_lines={total_lines} == signals_count={signals_count}")
    print(f"            md_files={md_files} == problems_count={n_problems}")
    print(f"  entity keys : ico={ico}  domain={dom}  name={nam}")
    print(f"  register    : sources={n_sources}  comps={n_comps}  dim rows={n_dims}"
          f"  extract_date={extract}")
    print(f"  provenance  : {cited} distinct signal(s) cited by the register")
    print(f"  preserved   : fetch_log={fl} rows  match_log={ml} rows")
    print(f"  vec         : {vec}")
    print(f"  digest      : signals={digest}")
    print(f"                problems={pdigest}")
    return 0


# --------------------------------------------------------------------------
# upsert — the single-run path INGEST uses
# --------------------------------------------------------------------------

def cmd_upsert(args):
    path = os.path.abspath(args.jsonl)
    if not os.path.isfile(path):
        log(f"db: no such ledger file: {args.jsonl}")
        return 1
    rel = os.path.relpath(path, ROOT)
    parts = rel.split(os.sep)
    typ = parts[2] if len(parts) >= 4 and parts[0] == "data" and parts[1] == "signals" else "unknown"
    if typ == "unknown":
        log(f"db: {rel} is not under data/signals/<type>/ — cannot infer evidence type")
        return 1

    con = connect()
    ensure_history(con)
    con.executescript(DDL_PROJECTIONS)

    n_up = 0
    for n, raw, rec in iter_jsonl(path, rel):
        sid = rec.get("id")
        if not sid:
            raise SystemExit(f"db: {rel}:{n}: record has no id")
        ename, ico, domain = derive_entity_keys(rec)
        con.execute(
            "INSERT INTO signals (id, source, type, date, entity_name_norm, entity_ico,"
            " entity_domain, dup_of, jsonl_file, jsonl_line, raw)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?)"
            " ON CONFLICT(id) DO UPDATE SET source=excluded.source, type=excluded.type,"
            " date=excluded.date, entity_name_norm=excluded.entity_name_norm,"
            " entity_ico=excluded.entity_ico, entity_domain=excluded.entity_domain,"
            " jsonl_file=excluded.jsonl_file, jsonl_line=excluded.jsonl_line,"
            " raw=excluded.raw",
            (sid, rec.get("source"), typ, rec.get("date"), ename, ico, domain,
             None, rel, n, raw))
        n_up += 1

    total = con.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    set_meta(con, signals_count=total,
             upserted_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    con.commit()
    con.close()
    print(f"upsert OK  {rel}: {n_up} records  (signals table now {total})")
    return 0


# --------------------------------------------------------------------------
# fetchlog — contract results into the health spine
# --------------------------------------------------------------------------

FETCHLOG_FIELDS = ("run_id", "feed_key", "started_at", "finished_at", "http_status",
                   "bytes", "items_fetched", "items_kept", "yield_anomaly",
                   "parse_method", "runtime_ms", "ok", "error", "raw_path")


def cmd_fetchlog(args):
    """
    Read <dir>/contract.json — written by normalize.py — into fetch_log.

    Shape (the seam between normalize.py and this file):
        {"run_id": "2026-08-20T1042",
         "raw_dir": "data/raw/2026-08-20",
         "results": [ {feed_key, started_at, finished_at, http_status, bytes,
                       items_fetched, items_kept, yield_anomaly, parse_method,
                       runtime_ms, ok, error, raw_path}, ... ]}
    """
    d = os.path.abspath(args.dir)
    cpath = os.path.join(d, "contract.json")
    if not os.path.isfile(cpath):
        log(f"db: {os.path.relpath(cpath, ROOT)} not found — nothing to log. "
            f"normalize.py writes it; if a fetch ran and this is missing, the run is unaudited.")
        return 1

    with open(cpath, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    run_id = payload.get("run_id") or datetime.now().strftime("%Y-%m-%dT%H%M")
    results = payload.get("results", [])

    con = connect()
    ensure_history(con)
    rows = []
    for r in results:
        if not r.get("feed_key"):
            log("db: skipping a contract result with no feed_key")
            continue
        rec = dict(r)
        rec["run_id"] = rec.get("run_id") or run_id
        rec.setdefault("started_at", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
        rec["ok"] = int(bool(rec.get("ok", 0)))
        rows.append(tuple(rec.get(f) for f in FETCHLOG_FIELDS))
    con.executemany(
        f"INSERT INTO fetch_log ({','.join(FETCHLOG_FIELDS)}) "
        f"VALUES ({','.join('?' * len(FETCHLOG_FIELDS))})", rows)
    con.commit()
    total = con.execute("SELECT COUNT(*) FROM fetch_log").fetchone()[0]
    con.close()
    print(f"fetchlog OK  run_id={run_id}  +{len(rows)} rows  (fetch_log now {total})")
    return 0


# --------------------------------------------------------------------------
# health — the admin space
# --------------------------------------------------------------------------

CADENCE_DAYS = {"3h": 0.125, "6h": 0.25, "12h": 0.5, "daily": 1.0,
                "2d": 2.0, "weekly": 7.0, "monthly": 30.0}


def load_feeds():
    if not os.path.isfile(FEEDS_JSON):
        raise SystemExit("db: data/feeds.json not found — the registry is the input to health")
    with open(FEEDS_JSON, "r", encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------
# provenance — THE ID PREFIX IS THE PROVENANCE KEY, NOT THE `source` FIELD
# --------------------------------------------------------------------------
#
# MEASURED, 2026-08-20, and the measurement is the whole reason this section
# exists: `source: "hlidac"` covers 463 committed records drawn from THREE
# unrelated provenances —
#
#     296  nen-*     nen.nipez.cz         (NEN below-threshold tenders)
#     114  hlidac-*  smlouvy.gov.cz       (registr smluv — the actual feed)
#      53  dotace-*  13 grant portals     (EU/CZ subsidy calls)
#
# so every corpus number attributed through `source` over-credited `hlidac` by
# 4.06x. Worse, the three cohorts landed on different run dates: real hlidac-*
# records last landed 2026-08-13, while the 2026-08-14 date came entirely from
# nen-* and dotace-*. Freshness attributed through `source` therefore reported
# hlidac as a day fresher than it is — a feed credited with another feed's
# arrival date.
#
# WHY THE PREFIX AND NOT A `source` MIGRATION. data/CONVENTIONS.md already
# defines every id as `<prefix>-<nativeid>` with the prefix naming provenance,
# so the prefix is DERIVABLE and DETERMINISTIC on lines already committed. The
# ledgers are append-only; retro-editing 349 historical lines to correct a
# display field would violate that law and destroy the evidence that the error
# existed. `source` is retained as a LEGACY DISPLAY FIELD and is documented as
# unreliable for nen/dotace on records written before 2026-08-20.
#
# WHY A LIST PER ROW, NOT ONE PREFIX PER FEED. Many-to-one is correct and
# already documented: CONVENTIONS.md gives arb-scan the ISO2 of the origin
# country (27 distinct prefixes in the corpus) and demand-scan the reporting
# body (nku-, ombud-, civic-, chamber-, uni-, ngo-, consult-, 15 in the corpus).
# 49 distinct prefixes map onto 19 registry rows. A 1:1 mapping is contradicted
# by the corpus.


def prefix_of(sid):
    """Provenance prefix of a signal id: the token before the FIRST hyphen.
    Returns None for an id with no hyphen, which is a malformed id rather than
    a prefix of its own — the caller reports it, never guesses one."""
    if not sid:
        return None
    head, sep, _ = str(sid).partition("-")
    return head if sep and head else None


def feed_prefixes(f):
    """Declared prefixes for one registry row. A MISSING key and an EMPTY list
    mean different things and are kept apart: missing = undeclared (reported),
    empty = declared to produce none (ec-hys, ares)."""
    v = f.get("id_prefixes")
    if v is None:
        return None
    return [str(x) for x in v]


def _capable(f):
    """A feed that could actually have produced a record: `planned` has no
    fetcher and `dead` has no live URL. Enrichment rows produce no signals."""
    return f.get("role") != "enrichment" and f.get("status") not in ("planned", "dead")


def prefix_owners(feeds):
    """prefix -> ([every claiming key], [claiming keys that are capable])."""
    owners, capable = {}, {}
    for f in feeds:
        for p in feed_prefixes(f) or []:
            owners.setdefault(p, []).append(f["key"])
            if _capable(f):
                capable.setdefault(p, []).append(f["key"])
    return owners, capable


def attribute_prefixes(feeds):
    """
    prefix -> feed key that the corpus records under it belong to, or None when
    the registry cannot decide. Returns (attribution, ambiguous).

    The resolution order, and why each step exists:
      1. Exactly ONE row claims the prefix -> that row, even if it is `planned`.
         This is what makes `nen`'s 296 committed records VISIBLE against the
         row that owns them instead of inflating `hlidac`. A planned feed's
         `state` still says PENDING, so "records exist, nothing produces them"
         renders as the honest pair it is.
      2. Otherwise exactly one CAPABLE row claims it -> that row. Covers `nku-`
         and `sukl-`: both are claimed by a planned fetcher row AND by the
         attended `demand-scan` harvest that actually wrote them.
      3. Otherwise UNATTRIBUTED (None). Two capable rows claiming one prefix is
         a genuine ambiguity — `reddit-new` and `reddit-search` both write
         `reddit-<postid>` and no id can separate them. The value is recorded
         as unknown and named in the warning. It is never split, and never
         credited to whichever row happens to sort first.
    """
    owners, capable = prefix_owners(feeds)
    attribution, ambiguous = {}, []
    for p, keys in owners.items():
        if len(keys) == 1:
            attribution[p] = keys[0]
        elif len(capable.get(p, [])) == 1:
            attribution[p] = capable[p][0]
        else:
            attribution[p] = None
            ambiguous.append((p, sorted(keys)))
    return attribution, sorted(ambiguous)


def corpus_prefixes():
    """
    prefix -> (record count, newest RUN DATE) straight from the committed
    ledgers. Deliberately reads the files, not the DB, so the assertion holds
    even when register.db is stale or absent — the ledgers are canonical (§3).

    The run date is the LEDGER FILENAME, never MAX(date): 145 records are
    legitimately dated in the future (a `regulation` record carries its
    EFFECTIVE date), and deriving freshness from the record would report a
    dead feed as fresher than a live one (§7.4).
    """
    rx = re.compile(r"(\d{4}-\d{2}-\d{2})\.jsonl$")
    counts, newest, malformed = {}, {}, []
    for path, rel, _typ in ledger_files():
        m = rx.search(os.path.basename(path))
        run_date = m.group(1) if m else None
        for n, _raw, rec in iter_jsonl(path, rel):
            p = prefix_of(rec.get("id"))
            if p is None:
                malformed.append(f"{rel}:{n}: id {rec.get('id')!r} has no `<prefix>-` head")
                continue
            counts[p] = counts.get(p, 0) + 1
            if run_date and (p not in newest or run_date > newest[p]):
                newest[p] = run_date
    return counts, newest, malformed


def check_prefix_totality(feeds, counts):
    """
    AC-F3 — TOTALITY. Every id prefix present in data/signals/** must be
    claimed by a registry row.

    AC-F1 (web/app/sources/registry.ts) asks the same question of the `source`
    FIELD and passed for weeks while 126 `reg-*` records sat unowned: the only
    row claiming `source: reg-scan` was `ec-hys`, `planned`, no fetcher, zero
    records ever. A `source` value shared by three provenances cannot detect
    that. The prefix can, so this assertion is keyed on the prefix and converts
    a silent omission into a build-time failure that NAMES the orphans.
    """
    owners, _ = prefix_owners(feeds)
    return sorted((p, counts[p]) for p in counts if p not in owners)


def cmd_prefixes(args):
    feeds = load_feeds().get("feeds", [])
    counts, newest, malformed = corpus_prefixes()
    attribution, ambiguous = attribute_prefixes(feeds)
    orphans = check_prefix_totality(feeds, counts)

    total = sum(counts.values())
    print(f"prefixes: {len(counts)} distinct id prefixes over {total} committed records"
          f"  |  {len(feeds)} registry rows")
    if args.verbose:
        for p in sorted(counts):
            owner = attribution.get(p, "(ORPHAN)")
            print(f"  {p:9} {counts[p]:6d}  {newest.get(p) or '—':10}  -> {owner or '(AMBIGUOUS)'}")

    rc = 0
    if malformed:
        log("db: FAIL — malformed signal id(s), no `<prefix>-` head:")
        for m in malformed[:20]:
            log(f"    {m}")
        rc = 1
    if orphans:
        log(f"db: FAIL — AC-F3 totality: {len(orphans)} id prefix(es) in data/signals/** "
            f"are claimed by NO registry row in data/feeds.json:")
        for p, c in orphans:
            log(f"    {p + '-':12} {c:6d} record(s) — no feed key, no contract, no health check")
        log("    Every record must have an owner. Add a row to data/feeds.json declaring")
        log("    the prefix in `id_prefixes`, or correct the id. See architecture-v3 §4.3.")
        rc = 1
    if ambiguous:
        # A warning, not a failure: it costs a number, not a record. Nothing is
        # silently lost — the prefix's records are reported as unattributed.
        for p, keys in ambiguous:
            log(f"db: WARN — prefix '{p}-' is claimed by {len(keys)} capable feeds "
                f"({', '.join(keys)}); its {counts.get(p, 0)} record(s) are UNATTRIBUTED "
                f"(recorded as unknown, never split or guessed)")
    undeclared = [f["key"] for f in feeds
                  if f.get("role") != "enrichment" and feed_prefixes(f) is None]
    if undeclared:
        log(f"db: WARN — registry row(s) with no `id_prefixes` key: {', '.join(undeclared)}")
    if rc == 0:
        print(f"  AC-F3 OK — every prefix claimed; {len(ambiguous)} ambiguous, "
              f"{len(undeclared)} undeclared")
    return rc


def cmd_health(args):
    """
    Derive data/feed_health.json from fetch_log plus the committed corpus.

    Two vocabularies, never merged: feeds.json carries `status` (INTENT), this
    file carries `state` (OBSERVED REALITY). A feed can be active + BROKEN, and
    that combination is the entire point.
    """
    reg = load_feeds()
    feeds = reg.get("feeds", [])
    con = connect()
    ensure_history(con)

    generated = date.today().isoformat()
    row = con.execute("SELECT run_id FROM fetch_log ORDER BY id DESC LIMIT 1").fetchone()
    run_id = row[0] if row else None

    # Corpus attribution is keyed on the ID PREFIX, never on the `source` field.
    # `source: "hlidac"` covers three unrelated provenances (296 nen-, 114
    # hlidac-, 53 dotace-), so attributing through it over-credited one feed by
    # 4.06x and handed it another feed's arrival date. See the provenance
    # section above for the measurement.
    #
    # The run date is the LEDGER FILENAME, not the record's `date` field. 145 of
    # 6,181 committed records are legitimately dated in the FUTURE, because a
    # `regulation` signal carries its effective date (laws in force from 2029 and
    # 2030). Deriving freshness from MAX(date) produced days_since_last_signal of
    # -1168 for hlidac — a feed reporting itself fresher than fresh (§7.4).
    counts, newest_by_prefix, malformed = corpus_prefixes()

    # AC-F3 gate. The health export is the file /sources renders; exporting a
    # view that silently omits records is the exact failure that page exists to
    # prevent, so an orphan prefix stops the export rather than shipping a
    # number that implies coverage nobody owns.
    orphans = check_prefix_totality(feeds, counts)
    if malformed or orphans:
        con.close()
        return cmd_prefixes(argparse.Namespace(verbose=False))

    attribution, ambiguous = attribute_prefixes(feeds)
    for p, keys in ambiguous:
        log(f"db: WARN — prefix '{p}-' claimed by {len(keys)} capable feeds "
            f"({', '.join(keys)}); its {counts.get(p, 0)} record(s) are UNATTRIBUTED")

    # Roll prefixes up to the feed that owns them.
    owned = {f["key"]: [p for p in (feed_prefixes(f) or []) if attribution.get(p) == f["key"]]
             for f in feeds}

    out = []
    for f in feeds:
        k = f["key"]
        rows = con.execute(
            "SELECT started_at, http_status, items_fetched, items_kept, yield_anomaly,"
            " parse_method, ok, error FROM fetch_log WHERE feed_key = ?"
            " ORDER BY started_at DESC, id DESC", (k,)).fetchall()

        consecutive_failures = 0
        consecutive_zero = 0
        for r in rows:
            if r[6]:  # ok
                break
            consecutive_failures += 1
        for r in rows:
            if r[3] is None or r[3] > 0:
                break
            consecutive_zero += 1

        last_success = next((r[0][:10] for r in rows if r[6]), None)
        items_last_run = rows[0][3] if rows else None
        parse_method = rows[0][5] if rows else None
        error = next((r[7] for r in rows if r[7]), None)

        cutoff = (date.today() - timedelta(days=7)).isoformat()
        yield_7d = sum((r[3] or 0) for r in rows if r[0][:10] >= cutoff) if rows else 0

        # signals_total — the corpus census for this feed, attributed by id
        # prefix. It counts COMMITTED RECORDS and is a different question from
        # yield_7d, which counts what fetch_log saw a fetcher keep. Both are
        # reported because they disagree in the informative direction: a feed
        # with records and no fetch_log is one nothing automated maintains.
        # A `planned` feed is credited here on purpose — that is what makes
        # nen's 296 records visible rather than hidden inside hlidac.
        mine = owned.get(k, [])
        signals_total = sum(counts.get(p, 0) for p in mine)

        # days_since_last_signal: fetch_log first (it is per-feed and
        # unambiguous). Fall back to the corpus only when this feed OWNS the
        # prefix outright AND could actually have produced it — otherwise the
        # attribution is a guess, and a guess here would read as a measurement.
        # The capability guard stays: without it a `planned` feed with committed
        # records would report a fresh date and render LIVE while having no
        # fetcher at all.
        dsls = None
        produced_ever = any((r[3] or 0) > 0 for r in rows)
        if produced_ever:
            newest = max(r[0][:10] for r in rows if (r[3] or 0) > 0)
            dsls = (date.fromisoformat(generated) - date.fromisoformat(newest)).days
        elif _capable(f) and signals_total > 0:
            runs = [newest_by_prefix[p] for p in mine if newest_by_prefix.get(p)]
            if runs:
                newest = max(runs)
                dsls = max(0, (date.fromisoformat(generated) - date.fromisoformat(newest)).days)
                produced_ever = True

        cad = CADENCE_DAYS.get(f.get("cadence") or "", None)
        stale_after = max(1, int(round(3 * cad))) if cad else None

        # State precedence. PENDING means "registered, never produced a record",
        # which is definitionally true of every `planned` feed.
        if f.get("status") == "planned" or f.get("role") == "enrichment":
            state = "PENDING"
        elif f.get("status") == "dead":
            state = "BROKEN"
        elif consecutive_failures > 0 or consecutive_zero >= 3:
            state = "BROKEN"
        elif not produced_ever:
            state = "PENDING"
        elif stale_after is not None and dsls is not None and dsls > stale_after:
            state = "STALE"
        else:
            state = "LIVE"

        out.append({
            "key": k,
            "state": state,
            "last_success": last_success,
            "items_last_run": items_last_run,
            "yield_7d": yield_7d,
            "signals_total": signals_total,
            "consecutive_failures": consecutive_failures,
            "consecutive_zero_yield": consecutive_zero,
            "days_since_last_signal": dsls,
            "parse_method": parse_method,
            "error": error,
        })

    con.close()
    doc = {"generated": generated, "run_id": run_id, "feeds": out}
    with open(HEALTH_JSON, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    tally = {}
    for f in out:
        tally[f["state"]] = tally.get(f["state"], 0) + 1
    print(f"health OK  data/feed_health.json  generated={generated} run_id={run_id}")
    print("  " + "  ".join(f"{s}={n}" for s, n in sorted(tally.items())))
    broken = [f["key"] for f in out if f["state"] == "BROKEN"]
    if broken:
        print(f"  BROKEN: {', '.join(broken)}")
    return 0


# --------------------------------------------------------------------------
# match — one row per decision, dismissals included
# --------------------------------------------------------------------------

def cmd_match(args):
    con = connect()
    ensure_history(con)
    problem = None if args.problem in (None, "none", "None", "") else args.problem
    con.execute(
        "INSERT INTO match_log (at, signal_id, region, problem_id, method, similarity,"
        " decision, note) VALUES (?,?,?,?,?,?,?,?)",
        (datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), args.signal,
         args.region, problem, args.method, args.similarity, args.decision, args.note))
    con.commit()
    total = con.execute("SELECT COUNT(*) FROM match_log").fetchone()[0]
    con.close()
    print(f"match OK  {args.signal} -> {problem or 'none'} ({args.decision}, {args.method})"
          f"  (match_log now {total})")
    return 0


# --------------------------------------------------------------------------
# dupes — REPORT ONLY. Writes nothing.
# --------------------------------------------------------------------------

def cmd_dupes(args):
    con = connect()
    print("dupes: report-only sweep over ENTITY KEYS (IČO / domain / name). "
          "Nothing is written — dup_of stays NULL until a human reads a report.")
    total = 0
    for col, label in (("entity_ico", "IČO"), ("entity_domain", "domain"),
                       ("entity_name_norm", "name")):
        groups = con.execute(
            f"SELECT {col}, COUNT(*) c, GROUP_CONCAT(id, ' ') FROM signals"
            f" WHERE {col} IS NOT NULL GROUP BY {col} HAVING c > 1 ORDER BY c DESC"
        ).fetchall()
        print(f"\n== {label}: {len(groups)} keys shared by more than one signal")
        for key, c, ids in groups[: args.limit]:
            shown = ids.split(" ")[:6]
            more = f" (+{c - len(shown)} more)" if c > len(shown) else ""
            print(f"  {key}  x{c}: {' '.join(shown)}{more}")
        if len(groups) > args.limit:
            print(f"  ... {len(groups) - args.limit} more groups (--limit to widen)")
        total += len(groups)
    con.close()
    print(f"\ndupes: {total} shared keys total. No rows modified.")
    return 0


# --------------------------------------------------------------------------
# stats
# --------------------------------------------------------------------------

def cmd_stats(args):
    con = connect()
    ensure_history(con)
    print(f"db: {os.path.relpath(DB_PATH, ROOT)}")
    for k in ("schema_version", "rebuilt_at", "git_head", "jsonl_lines", "signals_count",
              "md_files", "problems_count", "problem_sources_count", "problem_comps_count",
              "problem_source_dims_count", "extract_date", "problems_digest", "vec"):
        print(f"  meta.{k:25s} {get_meta(con, k, '(unset)')}")
    try:
        print("\n  by type:")
        for t, c in con.execute("SELECT type, COUNT(*) FROM signals GROUP BY type ORDER BY 2 DESC"):
            print(f"    {t:12s} {c:6d}")
        print("  by source:")
        for s, c in con.execute("SELECT source, COUNT(*) FROM signals GROUP BY source ORDER BY 2 DESC"):
            print(f"    {s:12s} {c:6d}")
    except sqlite3.OperationalError:
        print("  (no signals table — run rebuild)")
    print(f"\n  fetch_log rows: {con.execute('SELECT COUNT(*) FROM fetch_log').fetchone()[0]}")
    print(f"  match_log rows: {con.execute('SELECT COUNT(*) FROM match_log').fetchone()[0]}")
    con.close()
    return 0


def load_errata():
    """The disputed-value ledger, data/errata.jsonl.

    An append-only corpus cannot be retro-edited, so a value we dispute is
    corrected ON READ instead: the ledger line stays exactly as ingested and the
    dispute is recorded beside it. Two distinct classes live here and they are
    NOT the same thing:

      our-attribution      the published value is right and OUR handling is
                           wrong (e.g. a 13-country envelope attributed whole to
                           whichever country matched the query).
      disputed-source-value  the publisher's own figure looks wrong to us and we
                           have NOT refuted it at source. Recorded as disputed,
                           never as a known error, because we hold no correction.

    Raises rather than returning a partial list: an aggregate computed from a
    half-loaded errata file is indistinguishable from a correct one.
    """
    out = {}
    if not os.path.exists(ERRATA_PATH):
        raise FileNotFoundError(
            f"{os.path.relpath(ERRATA_PATH, ROOT)} is missing. Money aggregates are "
            f"refused without it — an uncorrected total reads exactly like a corrected one.")
    with open(ERRATA_PATH, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"{os.path.relpath(ERRATA_PATH, ROOT)}:{n}: {e}") from None
            if "id" not in rec or "action" not in rec:
                raise ValueError(f"{os.path.relpath(ERRATA_PATH, ROOT)}:{n}: needs `id` and `action`")
            out[rec["id"]] = rec
    return out


# `money_eur` is one column carrying FOUR incompatible kinds of money. Summing
# across them produces a number that means nothing — the first draft of this
# command printed a confident EUR 510bn "money mass" built from committed Czech
# contracts, a US debt programme, and a railway whose own note says it has no
# financing source. The classes, keyed by signal type:
MONEY_CLASSES = {
    "tenders": ("committed procurement",
                "a named public buyer contracting for a stated value"),
    "funded": ("private capital raised",
               "money raised BY a company, not money available to spend against it"),
    "demand": ("stated need or macro statistic",
               "NOT money that exists — includes multi-decade investment needs and "
               "whole-sector spend totals, some explicitly unfinanced"),
    "regulation": ("incidental figures", "amounts mentioned in regulatory text"),
}


def cmd_money(args):
    """Money per class and geography, errata ALWAYS applied.

    Two deliberate refusals:

    NO CROSS-CLASS TOTAL. See MONEY_CLASSES above — the classes answer different
    questions and a single sum answers none of them. `nku-vrt` alone contributes
    EUR 30bn of high-speed rail that its own note records as having no financing
    source; adding that to awarded contracts would inflate the register's headline
    by an amount no reader could detect.

    NO --raw FLAG. The uncorrected figure is not a view we support: two records
    carried 46.7% of the CZ procurement mass between them, so a raw number would
    be wrong by nearly half while looking exactly as authoritative as a right one.
    What was excluded prints every time, so a number always arrives with its own
    subtraction shown.
    """
    try:
        errata = load_errata()
    except (FileNotFoundError, ValueError) as e:
        log(f"db: {e}")
        return 2
    con = connect()
    try:
        # money_eur and geo_origin are NOT columns — the table keeps four entity
        # columns plus the verbatim `raw` payload (architecture-v3 §2.3), so both
        # are read out of the JSON rather than selected.
        rows = con.execute("SELECT id, type, raw FROM signals").fetchall()
    except sqlite3.OperationalError:
        log("db: no signals table — run `rebuild` first.")
        return 2
    finally:
        con.close()

    mass, cnt, dropped = {}, {}, []
    for sid, stype, raw in rows:
        try:
            rec = json.loads(raw)
        except json.JSONDecodeError:
            continue
        money = rec.get("money_eur")
        if not isinstance(money, (int, float)):
            continue
        geo = rec.get("geo_origin")
        e = errata.get(sid)
        if e and e.get("action", "").startswith("exclude"):
            dropped.append((sid, geo, money, e))
            continue
        key = (stype, geo or "MISSING")
        mass[key] = mass.get(key, 0) + money
        cnt[key] = cnt.get(key, 0) + 1

    for stype in sorted({k[0] for k in mass}, key=lambda t: -sum(
            v for k, v in mass.items() if k[0] == t)):
        label, caveat = MONEY_CLASSES.get(stype, (stype, ""))
        sub = {k[1]: v for k, v in mass.items() if k[0] == stype}
        subn = {k[1]: v for k, v in cnt.items() if k[0] == stype}
        print(f"\n{stype} — {label}")
        print(f"  {caveat}")
        for geo in sorted(sub, key=lambda g: -sub[g])[:8]:
            print(f"    {geo:<8}{subn[geo]:>7} rec {sub[geo]:>20,.0f} EUR")
        if len(sub) > 8:
            rest = sum(v for g, v in sub.items() if g not in sorted(sub, key=lambda g: -sub[g])[:8])
            print(f"    {'(rest)':<8}{'':>7}     {rest:>20,.0f} EUR")

    print("\nNo cross-class total is printed, deliberately — see MONEY_CLASSES in this file.")

    if dropped:
        print(f"\nexcluded by data/errata.jsonl ({len(dropped)}):")
        for sid, geo, money, e in sorted(dropped, key=lambda r: -r[2]):
            print(f"  {sid:<24} {geo or '?':<4} EUR {money:>16,.0f}  [{e.get('class', '?')}]")
            for chunk in textwrap.wrap(str(e.get("note", "")).strip(), 84)[:3]:
                print(f"    {chunk}")
    return 0


def cmd_errata(args):
    """List the disputed-value ledger with its evidence."""
    try:
        errata = load_errata()
    except (FileNotFoundError, ValueError) as e:
        log(f"db: {e}")
        return 2
    if not errata:
        print("errata: none recorded.")
        return 0
    for sid, e in errata.items():
        print(f"\n{sid}  [{e.get('class', '?')}]  recorded {e.get('recorded', '?')}")
        print(f"  action:   {e.get('action')}")
        print(f"  source:   {e.get('source_value')} {e.get('source_currency', '')}"
              f"   value_is_correct={e.get('value_is_correct')}")
        print(f"  verified: {e.get('verified_against', '(unverified)')}")
        for label in ("evidence", "impact", "note"):
            if e.get(label):
                print(f"  {label}:")
                for chunk in textwrap.wrap(str(e[label]), 88):
                    print(f"    {chunk}")
    return 0


# --------------------------------------------------------------------------
# audit — THE SCORE GATE
# --------------------------------------------------------------------------
#
# Two laws that were written down and enforced by NOTHING until this command
# existed, plus one number that is deliberately NOT a law.
#
# LAW 1 — SCORING.md, verbatim: "every point must be justified by a sources[]
# entry — no source, no point. Subjective vibes-scores are forbidden."
# dimRefs() already computed exactly the mapping this needs; it was used only to
# render the drawers. PROVEN UNENFORCED by planting: p-0012 gap 0 -> 2 with zero
# gap-check sources builds GREEN on the live site. `score_unbacked` names it.
#
# LAW 2 — a sources[].signal that resolves to nothing. getProblems() validates
# COMP refs only (data.ts:206-212); the 101 source refs are unvalidated, and a
# broken one crashes the build with `Cannot read properties of undefined
# (reading 'type')` naming no record and no field. `dangling_signal_refs` names
# record, position and id.
#
# NOT A LAW — the money rule. It agrees with the human on 27 of 31 records, and
# the 4 disagreements are the rubric's "RELEVANT tender" test, which no field
# records. 87% agreement between a rule and a human is CONSISTENCY evidence, not
# correctness evidence, so this prints as advisory divergence and never as a
# verdict. The errata ids are excluded because ted-529135-2026 alone carries a
# EUR 10bn 13-country envelope misattributed to CZ and would dominate anything
# it touched.
MONEY_RULE_EUR = 204000  # ~5M CZK — SCORING.md's level-2 threshold


def _audit_rows(con, view):
    try:
        return con.execute(f"SELECT * FROM {view}").fetchall()
    except sqlite3.OperationalError as e:
        raise SystemExit(f"db: cannot read {view} ({e}) — run `python3 scripts/db.py rebuild`")


def money_divergence(con):
    """ADVISORY. Returns (rows, excluded_ids) — never a verdict.

    Rule: no money-dim source -> 0; a money-dim source whose linked signal
    carries money_eur >= MONEY_RULE_EUR -> 2; else 1.
    """
    errata = load_errata()
    excluded = sorted(sid for sid, e in errata.items()
                      if str(e.get("action", "")).startswith("exclude"))
    money_eur = {}
    for sid, raw in con.execute("SELECT id, raw FROM signals"):
        if sid in excluded:
            continue
        try:
            v = json.loads(raw).get("money_eur")
        except json.JSONDecodeError:
            continue
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            money_eur[sid] = v

    rows = []
    for region, pid, s_money in con.execute(
            "SELECT region, id, s_money FROM problems ORDER BY region, id"):
        linked = con.execute(
            "SELECT ps.position, ps.signal_id FROM problem_source_dims d"
            " JOIN problem_sources ps ON ps.region = d.region"
            "   AND ps.problem_id = d.problem_id AND ps.position = d.position"
            " WHERE d.region = ? AND d.problem_id = ? AND d.dim = 'money'"
            " ORDER BY ps.position", (region, pid)).fetchall()
        if not linked:
            rule, best = 0, None
        else:
            figs = [money_eur[s] for _, s in linked if s and s in money_eur]
            best = max(figs) if figs else None
            rule = 2 if best is not None and best >= MONEY_RULE_EUR else 1
        if rule != s_money:
            rows.append((region, pid, s_money, rule, len(linked), best))
    return rows, excluded


def stale_against_tree(con):
    """Rows whose source file no longer hashes to what was recorded. Returns a
    list of human-readable strings; empty means the DB still describes the tree.

    WHY THIS EXISTS. `md_sha256` was being WRITTEN on every row and READ by
    nothing — a receipt recorded and never checked, which is the same shape of
    defect as a receipt that was never recorded at all. The consequence is not
    theoretical: MEASURED, planting `gap: 0 -> 2` with zero gap-check sources in
    a file and running `audit` WITHOUT `rebuild` printed
    "score_unbacked OK — 0 unbacked dimensions over 31 records" and exited 0.
    The gate was reporting on a corpus that no longer existed.

    That is exactly the standing hazard in this repo: PROCESS.md step 7 commits
    and deploys without calling `rebuild`, and `meta.git_head` was 7 commits
    behind at the time this schema was written. A gate that cannot tell it is
    reading a snapshot is a gate that can be bypassed by forgetting one command.
    """
    problems = {}
    for rel, sha in con.execute("SELECT md_file, md_sha256 FROM problems"):
        problems[rel] = sha
    out = []
    for path, rel, _region, _slug in problem_files():
        with open(path, "rb") as fh:
            actual = hashlib.sha256(fh.read()).hexdigest()
        recorded = problems.pop(rel, None)
        if recorded is None:
            out.append(f"{rel} — on disk, NOT in the database")
        elif recorded != actual:
            out.append(f"{rel} — changed on disk since the last rebuild "
                       f"({recorded[:12]}… -> {actual[:12]}…)")
    for rel in sorted(problems):
        out.append(f"{rel} — in the database, NOT on disk")

    # The ledger side, cheaply: a raw line count, no JSON parsing. It catches an
    # appended run, which is the way data/signals/** actually changes.
    recorded_lines = get_meta(con, "jsonl_lines")
    if recorded_lines is not None:
        actual_lines = 0
        for path, _rel, _typ in ledger_files():
            # text mode and `.strip()`, to be the SAME blank-line rule as
            # iter_jsonl() — bytes.strip() and str.strip() disagree on a line
            # made only of U+00A0, and a rule that disagrees with the counter it
            # is checking reports a stale database that is not stale.
            with open(path, "r", encoding="utf-8") as fh:
                actual_lines += sum(1 for line in fh if line.strip())
        if str(actual_lines) != str(recorded_lines):
            out.append(f"data/signals/** — {actual_lines} ledger lines on disk, "
                       f"{recorded_lines} recorded at the last rebuild")
    return out


def cmd_audit(args):
    con = connect()
    if get_meta(con, "schema_version") != SCHEMA_VERSION:
        log(f"db: register.db is schema_version {get_meta(con, 'schema_version', '(unset)')}, "
            f"expected {SCHEMA_VERSION} — run `python3 scripts/db.py rebuild` first.")
        con.close()
        return 2

    rc = 0
    n_problems = con.execute("SELECT COUNT(*) FROM problems").fetchone()[0]

    # FIRST, because every verdict below is only about the tree this DB was
    # built from. An audit of a stale snapshot is worse than no audit: it is a
    # green light for a corpus nobody looked at.
    stale = stale_against_tree(con)
    if stale:
        rc = 1
        log(f"db: FAIL — register.db is STALE: {len(stale)} discrepancy(ies) against "
            f"the working tree. Everything below describes an older corpus.")
        for s in stale:
            log(f"    {s}")
        log("    Run `python3 scripts/db.py rebuild`, then audit again.")
    else:
        print(f"  tree_fresh          OK — {n_problems} record file(s) hash to what was "
              f"recorded; ledger line count matches")

    # AC-F3 totality, on the judgment path too. `rebuild` already runs it at the
    # point every ledger line is read; running it here means the score gate and
    # the provenance gate cannot pass while a record has no owning feed.
    if cmd_prefixes(argparse.Namespace(verbose=False)) != 0:
        rc = 1

    unbacked = _audit_rows(con, "score_unbacked")
    if unbacked:
        rc = 1
        log(f"db: FAIL — SCORING.md 'no source, no point': {len(unbacked)} scored "
            f"dimension(s) with NO sources[] entry resolving to them:")
        for region, pid, dim, points in sorted(unbacked):
            log(f"    {region}/{pid}  {dim:8} = {points}  — no source resolves to {dim}")
        log("    Either add a sources[] entry that backs the dimension (its `type` maps,")
        log("    or set an explicit `dims: [...]`), or lower the score. SCORING.md:47.")
    else:
        print(f"  score_unbacked      OK — 0 unbacked dimensions over {n_problems} records")

    # THE FIFTH DIMENSION. score_unbacked structurally cannot fail on urgency —
    # the freshness rule backs it on every record — so the law is applied to the
    # deadline sub-score instead. See the `deadline_unbacked` view.
    dl = _audit_rows(con, "deadline_unbacked")
    if dl:
        rc = 1
        log(f"db: FAIL — SCORING.md 'no source, no point' on the urgency DEADLINE "
            f"sub-score: {len(dl)} record(s) score deadline points with no urgency "
            f"source other than the automatic freshness ref:")
        for region, pid, urg, fresh, deadline in sorted(dl):
            log(f"    {region}/{pid}  urgency = {urg} (deadline {deadline} + freshness "
                f"{fresh})  — the only urgency ref is the newest-source freshness rule")
        log("    Add a regulation-typed source (or an explicit `dims: [urgency]`) that")
        log("    carries the forcing date, or lower urgency to the freshness point alone.")
    else:
        print(f"  deadline_unbacked   OK — every deadline point has a non-freshness source")

    dangling = _audit_rows(con, "dangling_signal_refs")
    if dangling:
        rc = 1
        log(f"db: FAIL — {len(dangling)} signal ref(s) resolve to nothing in the "
            f"evidence layer:")
        for region, pid, position, sid, via in sorted(dangling):
            log(f"    {region}/{pid}  {via}[{position}]  signal '{sid}' not in data/signals/**")
        log("    On the site this is a TypeError at page.tsx:429 naming no record.")
    else:
        n_refs = con.execute("SELECT COUNT(*) FROM ("
                             " SELECT signal_id FROM problem_sources WHERE signal_id IS NOT NULL"
                             " UNION ALL"
                             " SELECT signal_id FROM problem_comps WHERE signal_id IS NOT NULL)"
                             ).fetchone()[0]
        print(f"  dangling_refs       OK — all {n_refs} signal refs resolve")

    # ---- ADVISORY. Prints under any outcome; changes no verdict. ----------
    try:
        rows, excluded = money_divergence(con)
    except (FileNotFoundError, ValueError) as e:
        log(f"db: money advisory SKIPPED — {e}")
        rows, excluded = None, []
    if rows is not None:
        print(f"\n  ADVISORY — money rule (>= EUR {MONEY_RULE_EUR:,} on a linked money-dim "
              f"source -> 2)")
        print(f"  This is NOT a verdict. It agrees with the human on "
              f"{n_problems - len(rows)}/{n_problems}; the disagreements are the rubric's")
        print("  'RELEVANT tender' test, which no field records. Read them, do not apply them.")
        print(f"  excluded by data/errata.jsonl: {', '.join(excluded) or '(none)'}")
        if not rows:
            print("    (no divergence)")
        for region, pid, human, rule, n_src, best in rows:
            fig = f"EUR {best:,.0f}" if best is not None else "no linked figure"
            print(f"    {region}/{pid}  money={human}  rule={rule}  "
                  f"({n_src} money-dim source(s), {fig})")

    con.close()
    if rc == 0:
        print("\naudit OK — freshness, prefix totality, score, deadline and provenance "
              "gates all green.")
    return rc


def cmd_deferred(args):
    log(f"db: `{args.command}` is Phase 3 and is NOT built. It is gated on the sqlite-vec\n"
        f"    install (`no such module: vec0` on this host). Phase 2 matching uses the\n"
        f"    IČO / domain / name entity keys, which need no extension — see `dupes --report`.")
    return 2


# --------------------------------------------------------------------------

def main():
    # Before argparse, because a re-exec replaces the process and re-parses.
    if len(sys.argv) > 1 and sys.argv[1] in _YAML_NEEDED:
        ensure_yaml(sys.argv[1:])

    p = argparse.ArgumentParser(prog="db.py", description=__doc__,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)

    r = sub.add_parser("rebuild", help="DROP + recreate signals & meta from the ledgers")
    r.add_argument("-v", "--verbose", action="store_true", help="per-file line counts")
    r.set_defaults(fn=cmd_rebuild)

    u = sub.add_parser("upsert", help="upsert one data/signals/<type>/<date>.jsonl")
    u.add_argument("jsonl")
    u.set_defaults(fn=cmd_upsert)

    fl = sub.add_parser("fetchlog", help="read <dir>/contract.json into fetch_log")
    fl.add_argument("dir")
    fl.set_defaults(fn=cmd_fetchlog)

    pf = sub.add_parser("prefixes",
                        help="AC-F3 totality: every ledger id prefix must be claimed by a registry row")
    pf.add_argument("-v", "--verbose", action="store_true",
                    help="per-prefix count, newest run date and owning feed")
    pf.set_defaults(fn=cmd_prefixes)

    h = sub.add_parser("health", help="export data/feed_health.json")
    h.set_defaults(fn=cmd_health)

    m = sub.add_parser("match", help="append one match_log row (run after EVERY decision)")
    m.add_argument("--signal", required=True)
    m.add_argument("--region", required=True)
    m.add_argument("--problem", default=None, help="p-NNNN, or 'none' for a dismissal")
    m.add_argument("--method", required=True, choices=["knn", "ico", "domain", "name", "manual"])
    m.add_argument("--decision", required=True, choices=["linked", "dismissed", "deferred", "dup"])
    m.add_argument("--similarity", type=float, default=None)
    m.add_argument("--note", default=None)
    m.set_defaults(fn=cmd_match)

    d = sub.add_parser("dupes", help="report-only entity-key sweep")
    d.add_argument("--report", action="store_true", help="accepted and implied; this command never writes")
    d.add_argument("--limit", type=int, default=15)
    d.set_defaults(fn=cmd_dupes)

    s = sub.add_parser("stats", help="inspection summary")
    s.set_defaults(fn=cmd_stats)

    au = sub.add_parser("audit", help="THE SCORE GATE: tree freshness + score_unbacked + "
                                      "deadline_unbacked + dangling_signal_refs (fail), "
                                      "money divergence (advisory)")
    au.set_defaults(fn=cmd_audit)

    mo = sub.add_parser("money", help="money mass per geo, errata ALWAYS applied")
    mo.set_defaults(fn=cmd_money)

    er = sub.add_parser("errata", help="list the disputed-value ledger with its evidence")
    er.set_defaults(fn=cmd_errata)

    for name in ("embed", "shortlist"):
        x = sub.add_parser(name, help="Phase 3 — gated on the sqlite-vec install")
        x.add_argument("rest", nargs="*")
        x.set_defaults(fn=cmd_deferred)

    args = p.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
