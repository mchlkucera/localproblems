// THE DATA GATE. Production reads `data/register.db` (lib/data.ts `source()`
// defaults to "db"), and the database is gitignored. That combination has one
// obvious failure mode — a build on a machine whose working store is missing or
// older than the journal — and this script closes it in the only way that
// cannot be forgotten: it runs INSIDE `npm run build`, before `next build`.
//
// TWO STEPS, AND THEY ARE INDEPENDENT ON PURPOSE.
//
//   1. REGENERATE. `python3 scripts/db.py rebuild` projects the committed
//      journal (`data/signals/ ** /*.jsonl` + `data/problems/ ** /*.md`) into
//      `data/register.db`. It costs ~0.4s over today's 6,181 records, which is
//      cheap enough that it runs unconditionally: a store that is rewritten
//      immediately before every build cannot be stale, so staleness stops being
//      a thing anyone has to remember to check.
//
//   2. VERIFY, against the tree rather than against step 1's own report.
//      Step 1 is the writer vouching for itself; this repo has already been
//      burned by exactly that (`meta.git_head` was found 7+ commits behind
//      while every command reported success). So step 2 re-reads the journal
//      off disk — ledger line counts, record-file count, and the sha256 of
//      every problem markdown — and compares it against what the database says
//      it holds. It is a witness, not an echo, and it still runs when step 1 is
//      skipped.
//
// WHY THERE IS NO FALLBACK. If either step fails, this exits non-zero and
// `npm run build` stops. It never quietly reverts to LP_SOURCE=jsonl. A silent
// fallback would build a green site from the journal while the flip to the
// database was broken, and nobody would find out — the exact failure class this
// repo keeps catching (a 200 carrying a login page; a fetch that "works" while
// zero records land). A red build is the point.
//
// LP_SKIP_DB_REBUILD=1 skips STEP 1 ONLY — never step 2. It exists for the
// negative tests that prove this gate can fail, and for anyone deliberately
// building against a store they produced themselves. Because verification still
// runs, the hatch cannot be used to smuggle a stale database into a build.
import { createHash } from "node:crypto";
import { spawnSync } from "node:child_process";
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";

// `lib/db.ts` derives DB_PATH from `process.cwd()`. npm runs scripts with cwd
// set to the package directory, but a human running
// `node web/scripts/db-gate.mjs` from the repo root does not — and a gate that
// inspects a different file than the build reads is worse than no gate. Pin it.
const WEB = resolve(import.meta.dirname, "..");
const ROOT = resolve(WEB, "..");
const DATA = join(ROOT, "data");
const DB_REL = "data/register.db";
process.chdir(WEB);

const say = (s) => console.log(`db-gate: ${s}`);

/** Every message names the command that fixes it. An error that only says what
    is wrong makes the reader guess; this build has exactly one remedy. */
const REMEDY =
  "    Fix:  python3 scripts/db.py rebuild        (run from the repo root)\n" +
  "    The journal in data/signals/** and data/problems/** is canonical and committed;\n" +
  "    data/register.db is the gitignored projection of it and is always rebuildable.";

function die(headline, detail = []) {
  process.stderr.write(`\ndb-gate: FAIL — ${headline}\n`);
  for (const d of detail) process.stderr.write(`    ${d}\n`);
  process.stderr.write(`${REMEDY}\n\n`);
  process.exit(1);
}

// ---- step 1: regenerate --------------------------------------------------

if (process.env.LP_SKIP_DB_REBUILD === "1") {
  say("LP_SKIP_DB_REBUILD=1 — skipping the rebuild; verification below still runs");
} else {
  const r = spawnSync("python3", ["scripts/db.py", "rebuild"], {
    cwd: ROOT,
    encoding: "utf8",
    maxBuffer: 64 * 1024 * 1024,
  });
  // stderr FIRST: db.py writes its diagnostics there and its receipt to stdout,
  // so this is the order the two streams actually happened in.
  const log = `${r.stderr ?? ""}${r.stdout ?? ""}`.trimEnd();
  if (r.error) {
    die(`could not run \`python3 scripts/db.py rebuild\` (${r.error.message}).`, [
      "The production build projects the committed journal into data/register.db,",
      "so python3 must be on PATH wherever the site is built.",
    ]);
  }
  if (r.status !== 0) {
    process.stderr.write(`${log}\n`);
    die(`\`python3 scripts/db.py rebuild\` exited ${r.status} — the working store was not regenerated.`, [
      "Read db.py's output above: it names the offending ledger line or record file.",
      "`database is locked` means an ingest run holds the write lock — wait for it and retry.",
    ]);
  }
  // db.py's own receipt lines, indented so the build log shows who said what.
  for (const line of log.split("\n")) if (line.trim()) say(`  ${line}`);
}

// ---- step 2: verify against the tree -------------------------------------

if (!existsSync(join(DATA, "register.db"))) {
  die(`${DB_REL} does not exist after step 1.`, [
    "The build reads the database and will NOT fall back to the JSONL journal.",
  ]);
}

// THE BUILD'S OWN READER, not a second implementation of it. Importing
// lib/db.ts means the schema version this gate enforces is the same constant
// lib/db.ts enforces — they cannot drift — and "the gate opened it" is
// literally "the build can open it". Node strips the types (v25 is already
// required for node:sqlite); --disable-warning in package.json keeps the
// typeless-package notice out of an otherwise clean build log.
const { rows, REQUIRED_SCHEMA_VERSION } = await import("../lib/db.ts");

// lib/db.ts throws on its own for an unopenable file or a schema it does not
// know, and those messages already name the remedy — but thrown out of a build
// script they arrive as an unhandled rejection with a stack trace over them.
// Catch and re-emit through `die`, so every way this gate can stop the build
// looks the same in the log.
const meta = new Map();
let version;
try {
  for (const r of rows("SELECT key, value FROM meta")) meta.set(String(r.key), String(r.value));
  version = meta.get("schema_version") ?? "(absent)";
} catch (e) {
  die(`${DB_REL} cannot be read by the build's own loader (lib/db.ts).`, String(e.message).split("\n"));
}

// Belt and braces: lib/db.ts asserts this on open, so reaching here with a
// mismatch would mean that assertion had been weakened. Keep both.
if (version !== REQUIRED_SCHEMA_VERSION)
  die(`${DB_REL} is schema_version ${version}, this build requires ${REQUIRED_SCHEMA_VERSION}.`);

// ---- the journal, measured off disk --------------------------------------

// Directories under data/signals/ ARE the evidence types — discovered, never
// hard-coded, matching db.py `evidence_types()` so `hiring/` counts the day it
// lands. Blank lines are skipped, matching db.py `iter_jsonl()`; `trim()` and
// Python's `str.strip()` agree on U+00A0, which is the one character that could
// make these two counters disagree about a line that exists.
function ledgerLines() {
  const signals = join(DATA, "signals");
  let lines = 0;
  let files = 0;
  for (const type of readdirSync(signals, { withFileTypes: true })) {
    if (!type.isDirectory() || type.name.startsWith(".")) continue;
    for (const f of readdirSync(join(signals, type.name)).sort()) {
      if (!f.endsWith(".jsonl")) continue;
      files += 1;
      for (const line of readFileSync(join(signals, type.name, f), "utf8").split("\n"))
        if (line.trim()) lines += 1;
    }
  }
  return { lines, files };
}

/** (repo-relative path, sha256) for every problem markdown, mirroring
    db.py `problem_files()` and the site's own directory walk. */
function problemFiles() {
  const dir = join(DATA, "problems");
  const out = [];
  for (const region of readdirSync(dir, { withFileTypes: true }).sort((a, b) => (a.name < b.name ? -1 : 1))) {
    if (!region.isDirectory() || region.name.startsWith(".")) continue;
    for (const f of readdirSync(join(dir, region.name)).sort()) {
      if (!f.endsWith(".md")) continue;
      const rel = `data/problems/${region.name}/${f}`;
      out.push([rel, createHash("sha256").update(readFileSync(join(dir, region.name, f))).digest("hex")]);
    }
  }
  return out;
}

const drift = [];

// (a) the ledgers. A line count is cheap and catches the way data/signals/**
//     actually changes: an ingest run appends to it.
const { lines: diskLines, files: diskFiles } = ledgerLines();
const dbSignals = Number(rows("SELECT COUNT(*) AS n FROM signals")[0].n);
if (dbSignals !== diskLines)
  drift.push(
    `data/signals/** — ${diskLines} ledger line(s) across ${diskFiles} file(s) on disk, ` +
    `but the signals table holds ${dbSignals} row(s)`
  );
// meta is the rebuild's own receipt; disagreeing with the table it describes is
// its own defect, and it is what `db.py audit` reads.
if (meta.get("jsonl_lines") !== String(diskLines))
  drift.push(
    `meta.jsonl_lines = ${meta.get("jsonl_lines") ?? "(absent)"}, but ${diskLines} ledger line(s) are on disk ` +
    `— the journal grew since the last rebuild`
  );

// (b) the record files, by content and not by count. A count alone passes an
//     edit that changes a score without adding a file, which is the edit this
//     register makes every week.
const disk = problemFiles();
const dbProblems = new Map(
  rows("SELECT md_file, md_sha256 FROM problems").map((r) => [String(r.md_file), String(r.md_sha256)])
);
for (const [rel, sha] of disk) {
  const recorded = dbProblems.get(rel);
  if (recorded === undefined) drift.push(`${rel} — on disk, NOT in the database`);
  else if (recorded !== sha)
    drift.push(`${rel} — changed on disk since the last rebuild (${recorded.slice(0, 12)}… -> ${sha.slice(0, 12)}…)`);
  dbProblems.delete(rel);
}
for (const rel of [...dbProblems.keys()].sort()) drift.push(`${rel} — in the database, NOT on disk`);

if (drift.length)
  die(`${DB_REL} is STALE — ${drift.length} discrepancy(ies) against the committed journal.`, [
    ...drift,
    "",
    "Everything the site would render comes from this database, so it would publish an older corpus.",
  ]);

say(
  `${DB_REL} schema_version=${version}  fresh: ${dbSignals} signal(s) == ${diskLines} ledger line(s) ` +
  `across ${diskFiles} file(s); ${disk.length} record file(s) hash to what was recorded ` +
  `(rebuilt_at=${meta.get("rebuilt_at") ?? "?"})`
);
say("the build reads the database — LP_SOURCE defaults to 'db' (lib/data.ts)");
