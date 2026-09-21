#!/usr/bin/env python3
"""
scripts/replay_match_decisions.py — replay a committed decisions file into
`match_log`, idempotently.

WHY THIS EXISTS. MATCH.md step 3 says "Record EVERY decision, including every
rejection — the dismissals are memory that exists nowhere else and cannot be
recovered later." Those decisions go to `match_log` in data/register.db, and
data/register.db is GITIGNORED as "the working store: deterministically
rebuildable from the committed ledgers". `match_log` is the one table that is
NOT rebuildable from anything: it is pure history. So the file that says the
dismissals cannot be recovered writes them to the one place nothing can
recover them from.

MEASURED, 2026-09-21: a fresh worktree on this branch started with 0
`match_log` rows, and the 2026-09-19 run's ~60 decisions survived only because
that run's report happened to transcribe them into a prose block for manual
replay. That was luck, not a design.

THE CONVENTION THIS SCRIPT MAKES REAL. Every PROCESS run writes its decisions
to docs/weekly/match-decisions-<run-date>.jsonl — committed, one JSON object
per decision — AS WELL AS to `db.py match`. After any `db.py rebuild`, or in
any fresh checkout or worktree, this script replays them back. The JSONL is
canonical; `match_log` is a projection of it exactly as `signals` is a
projection of the ledgers.

  python3 scripts/replay_match_decisions.py --all
  python3 scripts/replay_match_decisions.py docs/weekly/match-decisions-2026-09-19.jsonl

ROW SHAPE (the keys docs/weekly/match-decisions-2026-09-21.jsonl already uses):
  signal    required, the signal id
  region    required, e.g. "cz"
  problem   "p-NNNN", or "none"/null for a dismissal
  method    knn | ico | domain | name | manual
  decision  linked | dismissed | deferred | dup
  note      free text; the judgment itself, and the half a count cannot carry
  similarity   optional float
  at           optional ISO timestamp; otherwise derived from the FILENAME date

WHAT IDEMPOTENCE MEANS HERE, EXACTLY. `match_log` has an AUTOINCREMENT primary
key and no unique constraint, so nothing in the schema stops a second replay
from doubling every row. This script dedups on the DECISION ITSELF —
(signal_id, region, problem_id, method, decision, note) — read out of the table
before it writes. `at` is deliberately NOT in that key: the same decision
replayed under a different timestamp is still the same decision, and a replay
must never depend on a clock it does not control. Two genuinely different
decisions about one signal differ in at least one of the six fields (the note
if nothing else), so the key cannot silently swallow a real second decision.

The timestamp defaults to the RUN DATE IN THE FILENAME, not to now(): a row
replayed in December must not claim the judgment was made in December. This is
the same rule normalize.py --complete follows for the ledger filename.

THIS SCRIPT NEVER EDITS scripts/db.py AND NEVER RESTATES ITS SCHEMA. It imports
db.connect() and db.ensure_history() so the DDL has exactly one definition.
"""

import argparse
import glob
import json
import os
import re
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)

import db  # noqa: E402  — the one definition of the schema and the DB path

WEEKLY_GLOB = os.path.join(ROOT, "docs", "weekly", "match-decisions-*.jsonl")
DATE_IN_NAME = re.compile(r"(\d{4}-\d{2}-\d{2})")
METHODS = ("knn", "ico", "domain", "name", "manual")
DECISIONS = ("linked", "dismissed", "deferred", "dup")


def log(m):
    print(m, file=sys.stderr)


def at_for(path, override):
    """The decision's timestamp: --at, else the run date in the filename at
    00:00:00Z, else a refusal. Never the clock — see the docstring."""
    if override:
        return override
    m = DATE_IN_NAME.search(os.path.basename(path))
    if m:
        return f"{m.group(1)}T00:00:00Z"
    return None


def normalise(row, path, n, at):
    """One row -> the tuple match_log stores, or (None, complaint).

    A row that cannot be converted honestly is REFUSED and named. It is never
    coerced into a legal value: a dismissal logged against the wrong signal is
    worse than a dismissal that is visibly missing.
    """
    signal = (row.get("signal") or row.get("signal_id") or "").strip()
    region = (row.get("region") or "").strip()
    problem = row.get("problem", row.get("problem_id"))
    if isinstance(problem, str):
        problem = problem.strip()
    if problem in (None, "", "none", "None"):
        problem = None
    method = (row.get("method") or "").strip()
    decision = (row.get("decision") or "").strip()
    note = row.get("note")
    note = note.strip() if isinstance(note, str) else note
    sim = row.get("similarity")

    bad = []
    if not signal:
        bad.append("signal is empty")
    if not region:
        bad.append("region is empty")
    if method not in METHODS:
        bad.append(f"method {method!r} not in {METHODS}")
    if decision not in DECISIONS:
        bad.append(f"decision {decision!r} not in {DECISIONS}")
    if problem is not None and not re.fullmatch(r"p-\d{4}", problem):
        bad.append(f"problem {problem!r} is neither a p-NNNN id nor a dismissal")
    if decision == "linked" and problem is None:
        bad.append("decision 'linked' with no problem id")
    if bad:
        return None, f"{os.path.basename(path)}:{n}: " + "; ".join(bad)
    return (row.get("at") or at, signal, region, problem, method,
            float(sim) if sim is not None else None, decision, note), None


def replay(con, path, override_at, dry_run):
    at = at_for(path, override_at)
    rows, refused = [], []
    with open(path, "r", encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                refused.append(f"{os.path.basename(path)}:{n}: not JSON ({e})")
                continue
            if at is None and not row.get("at"):
                refused.append(f"{os.path.basename(path)}:{n}: no `at` in the row "
                               "and no date in the filename — pass --at")
                continue
            rec, why = normalise(row, path, n, at)
            (refused if why else rows).append(why or rec)

    # THE IDEMPOTENCE KEY, read out of the table, not assumed.
    existing = {
        tuple(r) for r in con.execute(
            "SELECT signal_id, region, problem_id, method, decision, note FROM match_log")
    }
    fresh, dupes = [], 0
    batch_keys = set()
    for rec in rows:
        key = (rec[1], rec[2], rec[3], rec[4], rec[6], rec[7])
        if key in existing or key in batch_keys:
            dupes += 1
            continue
        batch_keys.add(key)
        fresh.append(rec)

    if fresh and not dry_run:
        con.executemany(
            "INSERT INTO match_log (at, signal_id, region, problem_id, method,"
            " similarity, decision, note) VALUES (?,?,?,?,?,?,?,?)", fresh)
        con.commit()
    return len(rows), len(fresh), dupes, refused


def main():
    p = argparse.ArgumentParser(
        prog="replay_match_decisions.py",
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("files", nargs="*", help="decisions .jsonl files")
    p.add_argument("--all", action="store_true",
                   help=f"replay every {os.path.relpath(WEEKLY_GLOB, ROOT)}")
    p.add_argument("--at", default=None,
                   help="ISO timestamp for every row that carries none "
                        "(default: the run date in the filename, at 00:00:00Z)")
    p.add_argument("--dry-run", action="store_true", help="write nothing")
    args = p.parse_args()

    files = list(args.files)
    if args.all:
        files += sorted(glob.glob(WEEKLY_GLOB))
    files = sorted(dict.fromkeys(os.path.abspath(f) for f in files))
    if not files:
        log("replay_match_decisions: no files. Pass paths, or --all.")
        return 2
    missing = [f for f in files if not os.path.isfile(f)]
    if missing:
        for f in missing:
            log(f"replay_match_decisions: not found — {f}")
        return 2

    con = db.connect()
    db.ensure_history(con)
    before = con.execute("SELECT COUNT(*) FROM match_log").fetchone()[0]

    total_rows = total_new = total_dupes = 0
    all_refused = []
    for f in files:
        rows, new, dupes, refused = replay(con, f, args.at, args.dry_run)
        total_rows += rows
        total_new += new
        total_dupes += dupes
        all_refused += refused
        verb = "would insert" if args.dry_run else "inserted"
        print(f"{os.path.relpath(f, ROOT)}: {rows} decision(s), {verb} {new}, "
              f"{dupes} already present, {len(refused)} refused")

    after = con.execute("SELECT COUNT(*) FROM match_log").fetchone()[0]
    con.close()

    if all_refused:
        log(f"\n{len(all_refused)} row(s) REFUSED, not written:")
        for r in all_refused[:20]:
            log(f"  {r}")
        if len(all_refused) > 20:
            log(f"  ... and {len(all_refused) - 20} more")
        log("A decision that cannot be converted honestly is never coerced into a "
            "legal value. Fix the row and re-run — the replay is idempotent.")

    print(f"match_log: {before} -> {after} rows"
          + ("  (dry run — nothing written)" if args.dry_run else ""))
    # A refusal exits non-zero: a runner must not absorb a lost decision as a
    # green run. The rows that DID convert are already committed and are fine.
    return 1 if all_refused else 0


if __name__ == "__main__":
    sys.exit(main())
