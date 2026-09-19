// Build gate for the public site's static contract (SPEC.md §5, CLAUDE.md
// rule 2: a rule enforced by prose is not enforced). Two halves:
//
//   node scripts/check-site.mjs pages    (prebuild) — reads web/app + web/lib
//   node scripts/check-site.mjs html     (postbuild) — reads .next/server/app
//
// SOURCE
//   S1  no `searchParams`, `cookies(` or `headers(` in any page or lib file:
//       any of them turns a route into a serverless function with no ../data.
//   S2  "use client" only in the sanctioned islands (design-language SKILL §9,
//       SPEC §5): small, for comprehension, never content, and the page reads
//       fully with scripts off. Each is named in ISLANDS WITH ITS JOB; a new
//       one needs the owner's sign-off AND an entry there. An entry whose file
//       is gone, or that names no job, fails too, so the list stays the truth.
// HTML
//   H1  no public page links into /lab (`href="/lab/`).
//   H2  every non-rejected record has a page; NO rejected record has one
//       (owner, 2026-09-16). Statuses come from data/problems, never a list.
//   H3  every record page carries `id="sources"` and `id="s1"…id="sN"` for its
//       N sources, so old `#sN` deep links keep landing.
//   H4  without LP_ADMIN, anything emitted under /lab is the 404, never a page.
//
// Each check was proven able to fail by planting a violation (2026-09-16).
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join, relative, resolve, sep } from "node:path";
import { load as yamlLoad } from "js-yaml";

const WEB = resolve(import.meta.dirname, "..");
const ROOT = resolve(WEB, "..");
/** The client islands, each with its one job (owner, 2026-09-18: small islands
    that clearly improve comprehension, never content). */
const ISLANDS = new Map([
  ["lib/site/peek-hover.tsx", "record page: hover-intent and click-to-pin for the citation peeks, Escape for rail tooltips, #sN opens the sources drawer"],
]);

const walk = (dir, keep, acc = []) => {
  if (!existsSync(dir)) return acc;
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) { if (e.name !== "node_modules" && !e.name.startsWith(".")) walk(p, keep, acc); }
    else if (keep(e.name)) acc.push(p);
  }
  return acc;
};
const rel = (p) => relative(WEB, p).split(sep).join("/");
const errors = [];

/** Code without comments, so prose that names a banned API is not a hit. */
const code = (src) =>
  src.replace(/\/\*[\s\S]*?\*\//g, "").replace(/(^|[^:"'`])\/\/.*$/gm, "$1");

function pagesCheck() {
  const files = [...walk(join(WEB, "app"), (n) => /\.(t|j)sx?$/.test(n)), ...walk(join(WEB, "lib"), (n) => /\.(t|j)sx?$/.test(n))];
  for (const f of files) {
    const src = readFileSync(f, "utf8");
    const c = code(src);
    for (const [re, what] of [[/\bsearchParams\b/, "searchParams"], [/\bcookies\s*\(/, "cookies("], [/\bheaders\s*\(/, "headers("]])
      if (re.test(c)) errors.push(`S1 ${rel(f)}: reads ${what} — pages must stay static (SPEC §5)`);
    if (/^\s*["']use client["']/m.test(src) && !ISLANDS.has(rel(f)))
      errors.push(`S2 ${rel(f)}: "use client" outside the sanctioned islands (${[...ISLANDS.keys()].join(", ")})`);
  }
  for (const [f, job] of ISLANDS) {
    if (!existsSync(join(WEB, f))) errors.push(`S2 ${f}: on the island list but the file is gone — remove the entry`);
    else if (!/^\s*["']use client["']/m.test(readFileSync(join(WEB, f), "utf8"))) errors.push(`S2 ${f}: on the island list but not a client component`);
    if (!job?.trim()) errors.push(`S2 ${f}: an island must name its job`);
  }
  return `${files.length} source files, ${ISLANDS.size} client islands`;
}

function records() {
  const out = [];
  for (const f of walk(join(ROOT, "data", "problems"), (n) => n.endsWith(".md"))) {
    const m = readFileSync(f, "utf8").match(/^---\n([\s\S]*?)\n---/);
    if (!m) { errors.push(`H2 ${relative(ROOT, f)}: no frontmatter`); continue; }
    const fm = yamlLoad(m[1]);
    out.push({ id: fm.id, region: fm.region, status: fm.status, sources: (fm.sources ?? []).length });
  }
  return out;
}

function html() {
  const APP = join(WEB, ".next", "server", "app");
  if (!existsSync(APP)) { errors.push(`no ${APP}: run next build first`); return "0"; }
  const pages = walk(APP, (n) => n.endsWith(".html"));
  for (const f of pages) {
    const h = readFileSync(f, "utf8");
    const r = relative(APP, f).split(sep).join("/");
    if (h.includes('href="/lab/') || h.includes('href="/lab"')) errors.push(`H1 ${r}: links into /lab`);
    if (r.startsWith("lab/") && process.env.LP_ADMIN !== "1" && !h.includes("lnf-body"))
      errors.push(`H4 ${r}: a /lab page was emitted without LP_ADMIN`);
  }
  const recs = records();
  for (const p of recs) {
    const f = join(APP, "problem", p.region, `${p.id}.html`);
    const exists = existsSync(f);
    if (p.status === "rejected") {
      if (exists) errors.push(`H2 problem/${p.region}/${p.id}: rejected record has a public page`);
      continue;
    }
    if (!exists) { errors.push(`H2 problem/${p.region}/${p.id}: record has no page`); continue; }
    const h = readFileSync(f, "utf8");
    const missing = ["sources", ...Array.from({ length: p.sources }, (_, i) => `s${i + 1}`)].filter((id) => !h.includes(` id="${id}"`));
    if (missing.length) errors.push(`H3 problem/${p.region}/${p.id}: missing anchors ${missing.slice(0, 6).join(", ")}${missing.length > 6 ? " …" : ""}`);
  }
  return `${pages.length} HTML files, ${recs.length} records (${recs.filter((p) => p.status === "rejected").length} rejected)`;
}

const mode = process.argv[2];
const summary = mode === "pages" ? pagesCheck() : mode === "html" ? html() : (errors.push("usage: check-site.mjs pages|html"), "");
if (errors.length) {
  console.error(`check-site (${mode}) FAILED:\n  ${errors.join("\n  ")}`);
  process.exit(1);
}
console.log(`check-site (${mode}): OK — ${summary}`);
