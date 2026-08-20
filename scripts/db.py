#!/usr/bin/env python3
"""
scripts/db.py — the working store driver for data/register.db.

    THE LAW (architecture-v3 §3): the JSONL ledgers, the problem markdown,
    data/feeds.json and data/feed_health.json are CANONICAL. This database is a
    derived working store. It is gitignored, it is deterministically rebuildable,
    and the web build never opens it.

Two tables are projections of committed files and are DROPPED and recreated by
`rebuild`: `signals` and `meta`.

Two tables are HISTORY THAT EXISTS NOWHERE ELSE and are NEVER dropped:
`fetch_log` (the health spine — liveness, yield, contract results) and
`match_log` (link AND dismissal decisions; the dismissals are irrecoverable
memory). Losing them loses information no rebuild can reconstruct.

sqlite-vec is NOT installed on this host (`CREATE VIRTUAL TABLE ... USING vec0`
-> `no such module: vec0`). Every vec path is guarded: its absence sets
`meta.vec = 'off'` and DEGRADES the match shortlist to IČO / domain / name
joins, which need no extension. It must never fail a rebuild.

Commands
    rebuild             DROP + recreate signals & meta from the committed JSONL.
                        Asserts jsonl_lines == signals_count and exits non-zero
                        on mismatch (a duplicate id or a parse failure).
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

Phase 3, gated on the sqlite-vec install — NOT built, and they say so when called:
    embed               id-set difference -> embed the missing set
    shortlist           KNN shortlist for MATCH
"""

import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import unicodedata
from datetime import date, datetime, timedelta, timezone

SCHEMA_VERSION = "3"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(ROOT, "data", "register.db")
SIGNALS_DIR = os.path.join(ROOT, "data", "signals")
FEEDS_JSON = os.path.join(ROOT, "data", "feeds.json")
HEALTH_JSON = os.path.join(ROOT, "data", "feed_health.json")


def log(msg):
    print(msg, file=sys.stderr)


# --------------------------------------------------------------------------
# schema
# --------------------------------------------------------------------------

# Projections of committed files. Dropped and rebuilt at will.
DDL_PROJECTIONS = """
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
        h.update(repr(row).encode("utf-8"))
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
    row = con.execute("SELECT value FROM meta WHERE key = ?", (k,)).fetchone()
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
    con.executescript("DROP TABLE IF EXISTS signals; DROP TABLE IF EXISTS meta;")
    con.executescript(DDL_PROJECTIONS)

    seen_ids = {}
    total_lines = 0
    per_file = []
    for path, rel, typ in ledger_files():
        lines, rows = insert_records(con, path, rel, typ, seen_ids)
        total_lines += lines
        per_file.append((rel, lines))

    signals_count = con.execute("SELECT COUNT(*) FROM signals").fetchone()[0]

    set_meta(con,
             schema_version=SCHEMA_VERSION,
             rebuilt_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             git_head=git_head(),
             jsonl_lines=total_lines,
             signals_count=signals_count,
             vec=vec)
    con.commit()

    # THE SINGLE INTEGRITY ASSERTION. A mismatch means a duplicate id or a parse
    # failure, and it exits non-zero rather than leaving a quietly short database.
    if total_lines != signals_count:
        log(f"db: FAIL — jsonl_lines ({total_lines}) != signals_count ({signals_count})")
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
    ico = con.execute("SELECT COUNT(*) FROM signals WHERE entity_ico IS NOT NULL").fetchone()[0]
    dom = con.execute("SELECT COUNT(*) FROM signals WHERE entity_domain IS NOT NULL").fetchone()[0]
    nam = con.execute("SELECT COUNT(*) FROM signals WHERE entity_name_norm IS NOT NULL").fetchone()[0]
    fl = con.execute("SELECT COUNT(*) FROM fetch_log").fetchone()[0]
    ml = con.execute("SELECT COUNT(*) FROM match_log").fetchone()[0]
    con.close()

    if args.verbose:
        for rel, lines in per_file:
            print(f"  {rel:44s} {lines:6d}")
    print(f"rebuild OK  jsonl_lines={total_lines} == signals_count={signals_count}")
    print(f"  entity keys : ico={ico}  domain={dom}  name={nam}")
    print(f"  preserved   : fetch_log={fl} rows  match_log={ml} rows")
    print(f"  vec         : {vec}")
    print(f"  digest      : {digest}")
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
    for k in ("schema_version", "rebuilt_at", "git_head", "jsonl_lines", "signals_count", "vec"):
        print(f"  meta.{k:15s} {get_meta(con, k, '(unset)')}")
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


def cmd_deferred(args):
    log(f"db: `{args.command}` is Phase 3 and is NOT built. It is gated on the sqlite-vec\n"
        f"    install (`no such module: vec0` on this host). Phase 2 matching uses the\n"
        f"    IČO / domain / name entity keys, which need no extension — see `dupes --report`.")
    return 2


# --------------------------------------------------------------------------

def main():
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

    for name in ("embed", "shortlist"):
        x = sub.add_parser(name, help="Phase 3 — gated on the sqlite-vec install")
        x.add_argument("rest", nargs="*")
        x.set_defaults(fn=cmd_deferred)

    args = p.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
