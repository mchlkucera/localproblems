// The DB read path: `data/register.db`, opened READ-ONLY at build time.
// **THIS IS WHAT PRODUCTION READS** — `lib/data.ts` `source()` defaults to
// "db", and `scripts/db-gate.mjs` regenerates and verifies the store inside
// `npm run build` before `next build` runs.
//
// WHY THIS EXISTS AT ALL. The journal (`data/signals/**.jsonl` +
// `data/problems/**/*.md`) stays canonical and append-only; this file is the
// other half of a migration whose whole proof is `npm run parity` — the
// DB-backed build must emit BYTE-IDENTICAL HTML to the JSONL-backed build.
// That gate is green and stays the regression test for every schema change;
// it is also the reason the journal keeps its own loader rather than being
// retired. Nothing here may "improve" what it reads.
// In particular the loader reads `signals.raw` and the projected problem
// columns and NOTHING ELSE: `data/errata.jsonl` is canonical and committed and
// the web build has never read it, so picking it up here would silently gain
// the site a correction ledger — a real improvement AND an instant parity
// failure. Applying errata is a deliberate content change with its own diff.
//
// THE MIGRATION STAYS REVERSIBLE: `LP_SOURCE=jsonl` still selects the journal
// loader, unchanged, and `npm run parity` still builds both ways and compares.
// What changed on 2026-08-20 is only which of the two you get by default.
import { existsSync } from "node:fs";
import { join, resolve } from "node:path";

/** The schema this reader understands. `db.py rebuild` writes it into `meta`.
    Asserted on open: a stale v3 database must be a loud failure, not a page of
    missing records. THE DB WAS MEASURED 7+ COMMITS STALE while reporting
    success, so "it opened" is not evidence that it is current. */
export const REQUIRED_SCHEMA_VERSION = "5";

const DB_PATH = join(resolve(process.cwd(), ".."), "data", "register.db");

// ---- node:sqlite ---------------------------------------------------------

/** Structural types over node:sqlite. Hand-written rather than imported so the
    experimental module is touched exactly once, inside `builtinSqlite()`. */
export type SqliteRow = Record<string, string | number | bigint | null | Uint8Array>;
interface SqliteStatement {
  all(...params: unknown[]): SqliteRow[];
  get(...params: unknown[]): SqliteRow | undefined;
}
interface SqliteDatabase {
  prepare(sql: string): SqliteStatement;
  close(): void;
}
interface SqliteModule {
  DatabaseSync: new (path: string, options?: { readOnly?: boolean }) => SqliteDatabase;
}

/** `node:sqlite` is EXPERIMENTAL and announces it on stderr at first load. The
 *  warning is correct and we are not hiding the risk — it is recorded in the
 *  migration's risk list and in this comment — but it must not appear once per
 *  build worker in an otherwise clean build log.
 *
 *  The suppression is SURGICAL: `process.emitWarning` is swapped for exactly
 *  the duration of the builtin lookup, filters on `ExperimentalWarning` + the
 *  word "SQLite", and is restored in a `finally`. Every other warning — from
 *  this module or any other — still reaches stderr. Proven able to fail: with
 *  the filter narrowed to a name that does not match, the warning prints again.
 *
 *  `process.getBuiltinModule` (Node >= 22.3) rather than `require`/`await
 *  import`: it is synchronous (the loaders are synchronous and called from
 *  synchronous render code) and it is invisible to the bundler, so Next never
 *  tries to trace or inline an experimental builtin. */
function builtinSqlite(): SqliteModule {
  const original = process.emitWarning;
  process.emitWarning = ((warning: unknown, ...rest: unknown[]) => {
    const type = typeof rest[0] === "string" ? rest[0] : (rest[0] as { type?: string } | undefined)?.type;
    if (type === "ExperimentalWarning" && String(warning).includes("SQLite")) return;
    return (original as (...a: unknown[]) => void).call(process, warning, ...rest);
  }) as typeof process.emitWarning;
  try {
    return process.getBuiltinModule("node:sqlite") as unknown as SqliteModule;
  } finally {
    process.emitWarning = original;
  }
}

// ---- the handle ----------------------------------------------------------

let _db: SqliteDatabase | null = null;

/** ONE HANDLE PER PROCESS. Next generates static pages across ~9 worker
 *  processes; each evaluates this module once and gets its own read-only
 *  handle, which is why no cross-process locking is involved. Never closed:
 *  the process exits at the end of the build and an explicit close would only
 *  create a use-after-close hazard between routes. */
export function db(): SqliteDatabase {
  if (_db) return _db;

  if (!existsSync(DB_PATH)) {
    throw new Error(
      `LP_SOURCE=db but ${DB_PATH} does not exist.\n` +
      "The working store is gitignored and rebuildable — run:  python3 scripts/db.py rebuild"
    );
  }

  const { DatabaseSync } = builtinSqlite();
  let handle: SqliteDatabase;
  try {
    handle = new DatabaseSync(DB_PATH, { readOnly: true });
  } catch (e) {
    // A WAL database opened read-only needs its -shm sidecar, which a fresh
    // clone will not have. Say so, rather than leaking `SQLITE_CANTOPEN`.
    throw new Error(
      `LP_SOURCE=db: cannot open ${DB_PATH} read-only (${(e as Error).message}).\n` +
      "If this is a fresh checkout, rebuild the working store:  python3 scripts/db.py rebuild"
    );
  }

  const version = handle.prepare("SELECT value FROM meta WHERE key = 'schema_version'").get();
  const got = version?.value === undefined ? null : String(version.value);
  if (got !== REQUIRED_SCHEMA_VERSION) {
    handle.close();
    throw new Error(
      `LP_SOURCE=db: data/register.db is schema_version ${got ?? "(absent)"}, ` +
      `this build requires ${REQUIRED_SCHEMA_VERSION}.\n` +
      "Rebuild the working store:  python3 scripts/db.py rebuild"
    );
  }

  _db = handle;
  return _db;
}

/** Every read goes through here. NOTE THE ABSENT `ORDER BY`, and keep it
 *  absent: SQLite's default collation is BINARY over UTF-8, JS `.sort()` is
 *  UTF-16 code-unit order. They agree on today's all-ASCII slugs, filenames and
 *  ids and would diverge silently on the first non-ASCII one — as a content
 *  change nobody made. All ordering happens in JS in lib/data.ts, mirroring the
 *  `readdirSync().sort()` the JSONL path uses. */
export function rows(sql: string, ...params: unknown[]): SqliteRow[] {
  return db().prepare(sql).all(...params);
}

/** SQLite gives back `null` for absent; the schemas want the key gone entirely.
    The three-state distinction on `dims_json` (absent / `[]` / populated) is
    load-bearing and is handled by the callers, not here. */
export const text = (v: SqliteRow[string]): string => String(v);
export const num = (v: SqliteRow[string]): number => Number(v);
