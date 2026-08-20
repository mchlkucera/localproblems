// THE MIGRATION'S PROOF: the DB-backed build must emit BYTE-IDENTICAL HTML to
// the JSONL-backed build. Nothing switches until this is green.
//
//   npm --prefix web run parity
//
// ONE TREE, TWO LOADERS — and that is the whole design. Both builds run from
// the same working tree, the same CSS, the same fonts, the same node_modules,
// the same commit. The ONLY thing that differs between them is `LP_SOURCE`.
// So a byte difference can only have come from the loader, which makes this a
// property of the READ PATH rather than of the commit. (Comparing a DB build
// against a stored pre-migration baseline would instead fold in every unrelated
// change: deleting 4 dead CSS lines moves the emitted chunk from
// 3f4zgajdc78df.css to 40612qe1j4_49.css, and that filename is embedded in all
// 55 HTML files — a cosmetic edit would read as "the database changed
// everything".)
//
// PRECONDITION, already in place: next.config.ts pins `generateBuildId`.
// Without it two builds of an UNCHANGED tree differ — measured, aggregate sha
// 11682db4… vs 3c701c90… — and this gate is red before it can say anything.
//
// PROVEN ABLE TO FAIL. Not assumed:
//   * change one problem's `geo` in the markdown but not the DB  -> RED
//     (re-measured on p-0007: 3 of 55 — app/index.html, the record page
//      app/problem/cz/p-0007.html, and its category page
//      app/category/housing.html. An earlier revision of this comment said
//      "6 of 55"; that number does not reproduce and has been corrected.)
//   * whitespace-only reflow of a YAML block scalar             -> GREEN
//     (the harness measures rendered MEANING, not source bytes — which is why
//      the DB loader re-parses frontmatter values instead of needing a
//      verbatim-markdown column)
//   * a `dims: []` collapsed to key-absent in the DB            -> RED
//     (measured: /problem/cz/p-0018 differs — the three-state distinction is
//      load-bearing and this harness sees it)
//
// WHAT BYTE-IDENTICAL HTML DOES *NOT* PROVE, AND WHY STAGE 1 EXISTS.
// The HTML comparison certifies RENDERED OUTPUT. It is blind, by construction,
// to any loaded value that no page prints — and two such classes are live here:
//
//   * looseObject overflow. `SourceSchema`/`ProblemSchema` are z.looseObject,
//     so an unrecognised frontmatter key (the repo's named trap: a misspelled
//     `expiers` for `expires`) is carried in the object and rendered nowhere.
//     MEASURED: plant `expiers:` on one p-0007 source, let db.py capture it in
//     `problem_sources.extra_json`, then blank that column — the db loader now
//     returns a demonstrably different object and this harness reported
//     "PARITY OK — all 55 HTML files byte-identical", exit 0.
//   * a short corpus. Deleting one row from `signals` also built GREEN: the
//     `seen.txt` check in lib/data.ts asserts loaded-implies-seen, never the
//     converse, so a projection that silently loses rows passes it.
//
// So stage 1 compares the LOADED VALUES, not the pixels: it runs `lib/data.ts`
// in-process under each LP_SOURCE and diffs the fully-parsed `getProblems()` +
// `getSignals()`. It costs ~2s against ~2 builds, so it runs FIRST and fails
// fast. Both holes above are red under it — verified by planting each.
import { createHash } from "node:crypto";
import { spawnSync } from "node:child_process";
import { readFileSync, readdirSync, rmSync, existsSync, writeFileSync, mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, relative, resolve, sep } from "node:path";
import { pathToFileURL } from "node:url";

const WEB = resolve(import.meta.dirname, "..");
const NEXT = join(WEB, "node_modules", ".bin", "next");
const OUT = join(WEB, ".next", "server");

const sha = (buf) => createHash("sha256").update(buf).digest("hex");

// ---- stage 1: value parity ------------------------------------------------

/** The probe program, written to a temp dir rather than into web/scripts: it is
 *  a fixture of this harness, not a source file of the site, and leaving it
 *  untracked keeps `git status` honest about what the migration added.
 *
 *  `registerHooks` maps TypeScript's extensionless `./db` onto `./db.ts` so
 *  Node's own type stripping can import `lib/data.ts` directly. That needs
 *  Node >= 23.6 (stripping on by default); the build already requires v25.x for
 *  `node:sqlite`, so this adds no new floor. It deliberately imports THE SAME
 *  module the build imports — a re-implementation here would prove nothing.
 *
 *  CANONICAL FORM: keys sorted, so the gate is on key PRESENCE and VALUE and
 *  ARRAY ORDER (array order is the S-numbering and IS meaning) but not on key
 *  insertion order, which nothing renders. `undefined` is serialised to a
 *  sentinel so present-but-undefined can never be mistaken for absent — that
 *  distinction is the same three-state hazard `dims` carries. */
const PROBE = `
import { registerHooks } from "node:module";
import { existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
registerHooks({
  resolve(spec, ctx, next) {
    if (spec.startsWith(".") && !/\\.[a-z]+$/i.test(spec)) {
      const u = new URL(spec + ".ts", ctx.parentURL);
      if (existsSync(fileURLToPath(u))) return next(spec + ".ts", ctx);
    }
    return next(spec, ctx);
  },
});
const canon = (v) => {
  if (v === undefined) return { "\\u0000undefined": true };
  if (v === null || typeof v !== "object") return v;
  if (Array.isArray(v)) return v.map(canon);
  const out = {};
  for (const k of Object.keys(v).sort()) out[k] = canon(v[k]);
  return out;
};
const data = await import(process.argv[2]);
const payload = { problems: data.getProblems(), signals: data.getSignals() };
process.stdout.write(JSON.stringify({
  counts: { problems: payload.problems.length, signals: payload.signals.length },
  canonical: canon(payload),
  keyOrder: JSON.stringify(payload),
}));
`;

/** First differing paths between two canonical trees, deepest-named. */
function firstDiffs(a, b, path = "", acc = [], limit = 8) {
  if (acc.length >= limit) return acc;
  const prim = (v) => v === null || typeof v !== "object";
  if (prim(a) || prim(b)) {
    if (JSON.stringify(a) !== JSON.stringify(b))
      acc.push(`  ${path || "(root)"}\n      jsonl ${JSON.stringify(a)}\n      db    ${JSON.stringify(b)}`);
    return acc;
  }
  if (Array.isArray(a) !== Array.isArray(b)) {
    acc.push(`  ${path}: array vs object`);
    return acc;
  }
  if (Array.isArray(a)) {
    if (a.length !== b.length) acc.push(`  ${path}: length ${a.length} (jsonl) vs ${b.length} (db)`);
    for (let i = 0; i < Math.min(a.length, b.length) && acc.length < limit; i++)
      firstDiffs(a[i], b[i], `${path}[${i}]`, acc, limit);
    return acc;
  }
  for (const k of [...new Set([...Object.keys(a), ...Object.keys(b)])].sort()) {
    if (acc.length >= limit) break;
    if (!(k in a)) { acc.push(`  ${path}.${k}: ABSENT in jsonl, present in db = ${JSON.stringify(b[k])}`); continue; }
    if (!(k in b)) { acc.push(`  ${path}.${k}: present in jsonl = ${JSON.stringify(a[k])}, ABSENT in db`); continue; }
    firstDiffs(a[k], b[k], `${path}.${k}`, acc, limit);
  }
  return acc;
}

function loadValues(src, probePath) {
  const r = spawnSync(process.execPath, [probePath, pathToFileURL(join(WEB, "lib", "data.ts")).href], {
    cwd: WEB,
    env: { ...process.env, LP_SOURCE: src },
    encoding: "utf8",
    maxBuffer: 512 * 1024 * 1024,
  });
  if (r.status !== 0) {
    process.stderr.write(`${r.stdout ?? ""}${r.stderr ?? ""}`);
    throw new Error(`parity(values): loading with LP_SOURCE=${src} exited ${r.status}`);
  }
  // Same anti-tautology control the build stage uses: if LP_SOURCE never
  // reached the loader, this compared jsonl against jsonl.
  if (!(r.stderr ?? "").includes(`[lp-data] LP_SOURCE=${src}`))
    throw new Error(`parity(values): loader never announced '[lp-data] LP_SOURCE=${src}'`);
  return JSON.parse(r.stdout);
}

function valueParity() {
  const dir = mkdtempSync(join(tmpdir(), "lp-parity-"));
  const probePath = join(dir, "probe.mjs");
  writeFileSync(probePath, PROBE);

  process.stderr.write("\n── stage 1: value parity (lib/data.ts, both loaders) ──────\n");
  const a = loadValues("jsonl", probePath);
  const b = loadValues("db", probePath);

  process.stderr.write(`  jsonl   problems=${a.counts.problems}  signals=${a.counts.signals}\n`);
  process.stderr.write(`  db      problems=${b.counts.problems}  signals=${b.counts.signals}\n`);

  const ja = JSON.stringify(a.canonical), jb = JSON.stringify(b.canonical);
  if (ja !== jb) {
    process.stderr.write("\nVALUE PARITY FAILED — the two loaders returned different data.\n");
    process.stderr.write("(This is invisible to the HTML stage whenever the field renders nothing.)\n");
    process.stderr.write(`${firstDiffs(a.canonical, b.canonical).join("\n")}\n`);
    process.exit(1);
  }
  // ADVISORY, never a gate: key insertion order is not rendered, so a change
  // here is a fidelity note for whoever is reading the round-trip, not a defect.
  const orderNote = a.keyOrder === b.keyOrder ? "identical" : "DIFFERS (advisory only — not rendered)";
  process.stderr.write(`  values  identical (${sha(ja).slice(0, 8)}…)   key insertion order: ${orderNote}\n`);
}

function htmlFiles(dir, acc = []) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) htmlFiles(p, acc);
    else if (e.name.endsWith(".html")) acc.push(p);
  }
  return acc;
}

/** Build once with LP_SOURCE=<src> and fingerprint every emitted HTML file. */
function buildAndHash(src) {
  // Clean, so nothing can be reused from the other branch. A parity pass that
  // only proves "Next served me its cache" would be worthless.
  rmSync(join(WEB, ".next"), { recursive: true, force: true });

  process.stderr.write(`\n── building with LP_SOURCE=${src} ─────────────────────────\n`);
  const r = spawnSync(NEXT, ["build"], {
    cwd: WEB,
    env: { ...process.env, LP_SOURCE: src },
    encoding: "utf8",
    maxBuffer: 64 * 1024 * 1024,
  });
  const log = `${r.stdout ?? ""}${r.stderr ?? ""}`;
  if (r.status !== 0) {
    process.stderr.write(log);
    throw new Error(`parity: build with LP_SOURCE=${src} exited ${r.status}`);
  }

  // THE CONTROL THAT STOPS THIS BEING A TAUTOLOGY. lib/data.ts prints the
  // branch it actually took, once per build worker. Without this assertion an
  // ignored LP_SOURCE would compile jsonl against jsonl and report a green that
  // means nothing — the single most likely way this gate lies. Fail-safe by
  // construction: if the marker ever stops reaching stderr, this goes red
  // rather than quietly passing.
  const mine = `[lp-data] LP_SOURCE=${src}`;
  const other = `[lp-data] LP_SOURCE=${src === "db" ? "jsonl" : "db"}`;
  if (!log.includes(mine))
    throw new Error(`parity: build never announced '${mine}' — LP_SOURCE did not reach the loader`);
  if (log.includes(other))
    throw new Error(`parity: build with LP_SOURCE=${src} also announced '${other}'`);

  if (!existsSync(OUT)) throw new Error(`parity: no ${OUT} after the ${src} build`);
  const map = new Map();
  for (const f of htmlFiles(OUT)) map.set(relative(OUT, f).split(sep).join("/"), sha(readFileSync(f)));
  if (map.size === 0) throw new Error(`parity: the ${src} build emitted no HTML`);
  return map;
}

// Cheap stage first: a value mismatch is a superset of most HTML mismatches and
// costs seconds, so there is no reason to spend two builds discovering it.
valueParity();

const a = buildAndHash("jsonl");
const b = buildAndHash("db");

const names = [...new Set([...a.keys(), ...b.keys()])].sort();
const diffs = [];
for (const n of names) {
  const x = a.get(n), y = b.get(n);
  if (x === undefined) diffs.push(`  + ${n}   (only in db)`);
  else if (y === undefined) diffs.push(`  - ${n}   (only in jsonl)`);
  else if (x !== y) diffs.push(`  ~ ${n}\n      jsonl ${x}\n      db    ${y}`);
}

const aggregate = (m) => sha([...m.keys()].sort().map((k) => `${k} ${m.get(k)}`).join("\n"));
process.stderr.write("\n── parity ─────────────────────────────────────────────────\n");
process.stderr.write(`  files   jsonl=${a.size}  db=${b.size}\n`);
process.stderr.write(`  jsonl   ${aggregate(a)}\n`);
process.stderr.write(`  db      ${aggregate(b)}\n`);

if (diffs.length) {
  process.stderr.write(`\nPARITY FAILED — ${diffs.length} of ${names.length} files differ:\n`);
  process.stderr.write(`${diffs.join("\n")}\n`);
  process.exit(1);
}
process.stderr.write(`\nPARITY OK — values identical, and all ${names.length} HTML files byte-identical.\n`);
