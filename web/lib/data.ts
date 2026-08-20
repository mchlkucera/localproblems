// The data layer: reads ../data at build time, zod-validated.
// Validation failure = build failure = deploy blocked (SPEC.md §5).
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { load as yamlLoad } from "js-yaml";
import { z } from "zod";
import { rows, type SqliteRow } from "./db";

const ROOT = resolve(process.cwd(), "..");
const DATA = join(ROOT, "data");

// ---- the two read paths --------------------------------------------------

/** Which store the loaders read: the working store, or the canonical journal.
 *
 *  `db` — `data/register.db`. **THE DEFAULT, AND WHAT PRODUCTION READS**
 *  (flipped 2026-08-20, after `npm run parity` proved byte-identical HTML).
 *  Gitignored and never committed; `web/scripts/db-gate.mjs` regenerates it
 *  from the journal inside `npm run build`, before `next build` runs, and then
 *  verifies it against the tree — so the store production reads is always a
 *  projection of the commit being deployed.
 *  `jsonl` — `data/signals/**.jsonl` + `data/problems/ ** /*.md`. The
 *  append-only ledger, committed to git, and still the canonical corpus:
 *  the database is derived from it and never the other way round. Selecting it
 *  is now an explicit opt-out, used by `scripts/parity.mjs` as the reference
 *  implementation the db path is measured against.
 *
 *  THE DEFAULT IS `db` PRECISELY SO IT CANNOT BE FORGOTTEN. Carrying the flip
 *  in a build script or a deploy env var instead would mean any build that
 *  missed the setting silently served the journal — a green build that quietly
 *  un-did the migration, which nobody would notice. Here, the only way to read
 *  the journal is to ask for it by name.
 *
 *  AN UNKNOWN VALUE IS A LOUD FAILURE, NOT A FALLBACK. `LP_SOURCE=DB` quietly
 *  taking the jsonl branch would make the parity harness compare jsonl against
 *  jsonl and report a triumphant green — the exact false positive this whole
 *  exercise exists to avoid. Read inside the function, never captured at module
 *  scope, so no bundler can fold it to a constant. */
export function source(): "jsonl" | "db" {
  const v = process.env.LP_SOURCE ?? "db";
  if (v !== "jsonl" && v !== "db")
    throw new Error(`LP_SOURCE must be 'jsonl' or 'db', got '${v}'`);
  return v;
}

/** One line per build worker, on stderr. It is the only externally visible
    evidence of WHICH branch ran, and `scripts/parity.mjs` asserts on it. */
let _announced = false;
function announce(): "jsonl" | "db" {
  const src = source();
  if (!_announced) {
    _announced = true;
    process.stderr.write(`[lp-data] LP_SOURCE=${src}\n`);
  }
  return src;
}

/** UTF-16 code-unit order — byte-for-byte what `Array.prototype.sort()` does to
    strings, and therefore what `readdirSync().sort()` does to filenames. NOT
    `localeCompare` (ICU collation) and NOT SQL `ORDER BY` (SQLite BINARY over
    UTF-8): all three agree on today's ASCII filenames and slugs and diverge
    silently on the first non-ASCII one. */
const cmp = (a: string, b: string) => (a < b ? -1 : a > b ? 1 : 0);

export const CATEGORIES = [
  "fintech", "health", "housing", "energy", "mobility", "govtech",
  "retail-services", "b2b", "legal-compliance", "education", "environment", "other",
] as const;

export const EVIDENCE_TYPES = ["funded", "regulation", "tenders", "demand", "hiring"] as const;
export type EvidenceType = (typeof EVIDENCE_TYPES)[number];

const isoDate = z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "ISO date required");
/** A TIMESTAMP, not a date — a date cannot gate a 3h or 6h cadence (architecture-v3 §4.1). */
const isoTimestamp = z
  .string()
  .regex(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(\.\d+)?(Z|[+-]\d{2}:\d{2})$/, "ISO timestamp required");

/** How a signal was extracted from its payload (architecture-v3 §7.3). The value
    IS the review flag — `llm-fallback` rows are marked on the ledger, never
    silently trusted. An enum fails LOUDLY on an unknown value, by design. */
export const EXTRACTION_METHODS = ["structured", "llm-fallback", "manual"] as const;

// ---- evidence layer ------------------------------------------------------

// z.strictObject, NOT z.object (architecture-v3 §3, AC-Z2). `z.object` SILENTLY
// STRIPS unknown keys: a new JSONL field would land in the canonical ledgers, be
// dropped at build time, never reach the site — and the "validation failure =
// build failure = deploy blocked" law would never fire. Strict makes an unknown
// key the loud failure that law already promises.
// Measured before the flip: all 6,181 lines in data/signals/** carry only the
// keys below (12 top-level, 4 under `scores`), so this is safe today.
const SignalSchema = z.strictObject({
  id: z.string().regex(/^[a-z]{2,10}-[\w.-]+$/),
  source: z.enum(["ted", "hlidac", "yc", "round", "reg-scan", "arb-scan", "feed", "demand-scan", "suggest", "reddit", "mpsv"]),
  url: z.string().url(),
  date: isoDate,
  title: z.string().min(1),
  sector: z.enum(CATEGORIES),
  geo_origin: z.string().regex(/^([A-Z]{2}|EU)$/),
  money_eur: z.number().nullable(),
  money_note: z.string(),
  summary: z.string().min(1),
  // strictObject applies to the TOP LEVEL ONLY — the nested object must be made
  // strict in the same edit or the trap simply moves one level down and a stray
  // `scores.confidence` from a future scorer vanishes silently (§3, AC-Z2).
  scores: z.strictObject({
    scale: z.number().int().min(0).max(3),
    money: z.number().int().min(0).max(3),
    urgency: z.number().int().min(0).max(3),
    recurrence: z.number().int().min(0).max(3),
  }),
  notes: z.string().optional(),
  // ---- receipt fields (§7.2, §7.3). Optional; written by INGEST. -----------
  // `quote` is a CONTRACT WITH AN EXTERNAL CONSUMER: a flat string on the
  // signal, retrievable by signal id. Do not restructure it into an object,
  // an array, or a nested receipt. min(1) because an empty quote is not a
  // quote — it is the shape that looks present and says nothing; omit the key.
  quote: z.string().min(1).optional(),
  http_status: z.number().int().min(100).max(599).optional(),
  fetched_at: isoTimestamp.optional(),
  extraction: z.enum(EXTRACTION_METHODS).optional(),
});
export type Signal = z.infer<typeof SignalSchema> & { type: EvidenceType };

// ---- region layer --------------------------------------------------------

const STATUSES = ["candidate", "active", "watching", "stale", "claimed", "solved", "rejected"] as const;

/** Where a gap-check actually looked (architecture-v3 §8.1). Vocabulary is
    closed on purpose: an enum fails loudly on a typo, which is the whole reason
    these keys get typed rather than left to looseObject. */
export const GAP_CHECKED = [
  "ares", "app-stores", "cz-saas-directories", "google-cz", "startupjobs", "own-funded-ledger",
] as const;
export type GapChecked = (typeof GAP_CHECKED)[number];

// NOTE the deliberate contrast with SignalSchema seven lines above: this one is
// z.looseObject, so extra keys on problem `sources[]` already pass untouched.
// That is why the gap-check fields below "already work" — but "already passes"
// means "unvalidated": a typo'd `expiers` would sit in the frontmatter forever,
// rendering nothing. Typed as optionals so the typo is a build failure (§8.1).
const SourceSchema = z.looseObject({
  type: z.string().min(1),
  url: z.string().min(1),
  note: z.string().min(1),
  date: isoDate,
  signal: z.string().optional(),
  dims: z.array(z.enum(["proof", "money", "urgency", "demand", "gap"])).optional(),
  queries: z.array(z.string().min(1)).optional(),
  checked: z.array(z.enum(GAP_CHECKED)).optional(),
  // date + 90 days, computed once when the gap-check source is written. Decay
  // compares against extractDate(), NEVER the wall clock (§8.2) — display-only,
  // it never moves `scores.gap` and never changes a total.
  expires: isoDate.optional(),
});
export type ProblemSource = z.infer<typeof SourceSchema>;

// Buildability scorecard — who can build this, with what, how fast (CONVENTIONS.md).
// The stánek→továrna capital ladder: <€10k | €10–100k | €100k–1M | >€1M.
export const CAPITAL_LADDER = ["kiosk", "garage", "funded", "industrial"] as const;
export const FIRST_REVENUE = ["weeks", "months", "year-plus"] as const;
export const BUILDER_PROFILES = ["solo", "small-team", "funded-team"] as const;

const BuildSchema = z.object({
  capital: z.enum(CAPITAL_LADDER),
  first_revenue: z.enum(FIRST_REVENUE),
  builder: z.enum(BUILDER_PROFILES),
  note: z.string().min(1),
});
export type Build = z.infer<typeof BuildSchema>;

// Foreign comparables — who runs this model elsewhere, with public traction on file.
const CompSchema = z.object({
  name: z.string().min(1),
  url: z.string().url(),
  geo: z.string().regex(/^[A-Z]{2}$/, "ISO2 country code"),
  since: z.number().int().min(1980).max(2100),
  traction: z.string().min(1),
  signal: z.string().optional(),
  // Operating countries beyond the HQ — recorded only when sourced (CONVENTIONS.md).
  markets: z.array(z.string().regex(/^[A-Z]{2}$/)).optional(),
});

const ProblemSchema = z.looseObject({
  id: z.string().regex(/^p-\d{4}$/),
  region: z.string().regex(/^[a-z]{2}$/),
  title: z.string().min(1),
  category: z.enum(CATEGORIES),
  geo: z.string().min(1),
  score: z.number().int().min(0).max(12),
  scores: z.object({
    proof: z.number().int().min(0).max(3),
    money: z.number().int().min(0).max(2),
    urgency: z.number().int().min(0).max(3),
    demand: z.number().int().min(0).max(2),
    gap: z.number().int().min(0).max(2),
  }),
  status: z.enum(STATUSES),
  // Required since the 2026-08 product upgrade — no record may skip the
  // buildability scorecard or the comparables ledger (SPEC.md §4).
  build: BuildSchema,
  comps: z.array(CompSchema),
  sources: z.array(SourceSchema).min(1),
  created: isoDate,
  updated: isoDate,
}).check((ctx) => {
  const p = ctx.value;
  const sum = p.scores.proof + p.scores.money + p.scores.urgency + p.scores.demand + p.scores.gap;
  if (sum !== p.score) {
    ctx.issues.push({ code: "custom", message: `score ${p.score} != sum(scores) ${sum}`, input: p });
  }
  // proof >= 1 asserts a foreign analog exists — the comps ledger must name at least one.
  if (p.comps && p.scores.proof >= 1 && p.comps.length === 0) {
    ctx.issues.push({ code: "custom", message: `proof ${p.scores.proof} >= 1 but comps is empty — name the analog or justify proof 0`, input: p });
  }
});
export type Problem = z.infer<typeof ProblemSchema> & { body: string; slug: string };

// ---- loaders (module-level cache; build-time only) -----------------------

function parseFrontmatter(raw: string, file: string): { fm: unknown; body: string } {
  if (!raw.startsWith("---\n")) throw new Error(`${file}: missing frontmatter`);
  const end = raw.indexOf("\n---\n", 4);
  if (end === -1) throw new Error(`${file}: unterminated frontmatter`);
  return { fm: yamlLoad(raw.slice(4, end)), body: raw.slice(end + 5).trim() };
}

function fail(file: string, error: z.ZodError): never {
  throw new Error(`${file}: ${error.issues.map((i) => `${i.path.join(".")}: ${i.message}`).join("; ")}`);
}

function problemsFromJsonl(): Problem[] {
  const problems: Problem[] = [];
  const problemsDir = join(DATA, "problems");
  for (const region of readdirSync(problemsDir, { withFileTypes: true })) {
    if (!region.isDirectory()) continue;
    for (const f of readdirSync(join(problemsDir, region.name)).sort()) {
      if (!f.endsWith(".md")) continue;
      const file = `data/problems/${region.name}/${f}`;
      const { fm, body } = parseFrontmatter(readFileSync(join(problemsDir, region.name, f), "utf8"), file);
      const parsed = ProblemSchema.safeParse(fm);
      if (!parsed.success) fail(file, parsed.error);
      if (parsed.data.region !== region.name)
        throw new Error(`${file}: region '${parsed.data.region}' != directory '${region.name}'`);
      problems.push({ ...parsed.data, body, slug: f.replace(/\.md$/, "") });
    }
  }
  return problems;
}

/** `null` in SQLite means "the key was absent from the frontmatter"; the schemas
    want the key gone, not present-and-null. Assigns only when there is a value. */
function put(o: Record<string, unknown>, key: string, v: unknown): void {
  if (v !== null && v !== undefined) o[key] = v;
}

/** Same as `put`, but the stored value is a JSON document.
 *
 *  THE THREE STATES ARE ALL LOAD-BEARING and this is the only place they are
 *  told apart: `NULL` = key absent (fall through to the type map in
 *  scorecard.ts `dimRefs`), `'[]'` = key present and empty — the deliberate
 *  "attach to nothing" opt-out carried by 4 live sources — and `'["money"]'` =
 *  an explicit override. `dimRefs` early-returns on ANY present `dims` key, so
 *  collapsing absent and empty into one state re-attaches those 4 sources to
 *  Demand and changes /problem/cz/p-0018. A join table cannot represent this;
 *  the JSON column can. */
function putJson(o: Record<string, unknown>, key: string, v: unknown): void {
  if (v !== null && v !== undefined) o[key] = JSON.parse(String(v));
}

function problemsFromDb(): Problem[] {
  const srcRows = rows(
    "SELECT region, problem_id, position, type, url, note, date, signal_id," +
    " dims_json, queries_json, checked_json, expires, extra_json FROM problem_sources"
  );
  const compRows = rows(
    "SELECT region, problem_id, position, name, url, geo, since, traction," +
    " signal_id, markets_json FROM problem_comps"
  );

  // Group children by their parent, then order each group by `position` — which
  // IS the S-number and is never reassigned (480 live [Sn] citation markers key
  // off array position). Numeric sort: no collation is involved.
  const byParent = (rs: SqliteRow[]) => {
    const m = new Map<string, SqliteRow[]>();
    for (const r of rs) {
      const k = `${String(r.region)}/${String(r.problem_id)}`;
      (m.get(k) ?? m.set(k, []).get(k)!).push(r);
    }
    for (const g of m.values()) g.sort((a, b) => Number(a.position) - Number(b.position));
    return m;
  };
  const sourcesFor = byParent(srcRows);
  const compsFor = byParent(compRows);

  const problems: Problem[] = [];
  for (const r of rows(
    "SELECT region, id, slug, title, category, geo, status, score," +
    " s_proof, s_money, s_urgency, s_demand, s_gap," +
    " build_capital, build_first_revenue, build_builder, build_note," +
    " created, updated, body, extra_json, md_file FROM problems"
  )) {
    const key = `${String(r.region)}/${String(r.id)}`;
    const file = String(r.md_file);

    const fm: Record<string, unknown> = {
      id: String(r.id),
      region: String(r.region),
      title: String(r.title),
      category: String(r.category),
      geo: String(r.geo),
      score: Number(r.score),
      scores: {
        proof: Number(r.s_proof), money: Number(r.s_money), urgency: Number(r.s_urgency),
        demand: Number(r.s_demand), gap: Number(r.s_gap),
      },
      status: String(r.status),
      build: {
        capital: String(r.build_capital), first_revenue: String(r.build_first_revenue),
        builder: String(r.build_builder), note: String(r.build_note),
      },
      comps: (compsFor.get(key) ?? []).map((c) => {
        const comp: Record<string, unknown> = {
          name: String(c.name), url: String(c.url), geo: String(c.geo),
          // YAML wrote this unquoted, so it MUST come back a JS number, not the
          // string SQLite would happily coerce. `since: "2020"` fails z.number().
          since: Number(c.since),
          traction: String(c.traction),
        };
        put(comp, "signal", c.signal_id === null ? null : String(c.signal_id));
        putJson(comp, "markets", c.markets_json);
        return comp;
      }),
      sources: (sourcesFor.get(key) ?? []).map((s) => {
        const src: Record<string, unknown> = {
          type: String(s.type), url: String(s.url), note: String(s.note), date: String(s.date),
        };
        put(src, "signal", s.signal_id === null ? null : String(s.signal_id));
        putJson(src, "dims", s.dims_json);
        putJson(src, "queries", s.queries_json);
        putJson(src, "checked", s.checked_json);
        put(src, "expires", s.expires === null ? null : String(s.expires));
        // SourceSchema is looseObject: any key the frontmatter carried that the
        // schema does not name survives the round trip verbatim. NULL today.
        if (s.extra_json !== null) Object.assign(src, JSON.parse(String(s.extra_json)));
        return src;
      }),
      created: String(r.created),
      updated: String(r.updated),
    };
    if (r.extra_json !== null) Object.assign(fm, JSON.parse(String(r.extra_json)));

    const parsed = ProblemSchema.safeParse(fm);
    if (!parsed.success) fail(file, parsed.error);

    // The JSONL path gets frontmatter-vs-path agreement for free from the
    // directory walk. Re-derive it here from `md_file` rather than let the
    // check go vacuous — the `region` column and `fm.region` are the same value
    // by construction, so comparing them would prove nothing.
    const m = /^data\/problems\/([^/]+)\/(.+)\.md$/.exec(file);
    if (!m) throw new Error(`${file}: md_file is not data/problems/<region>/<slug>.md`);
    if (m[1] !== parsed.data.region)
      throw new Error(`${file}: region '${parsed.data.region}' != directory '${m[1]}'`);
    if (m[2] !== String(r.slug))
      throw new Error(`${file}: slug '${String(r.slug)}' != filename '${m[2]}'`);

    problems.push({ ...parsed.data, body: String(r.body), slug: String(r.slug) });
  }

  // Mirrors the JSONL walk: regions outer, then `readdirSync().sort()` over the
  // filenames — which is what `slug` is. (With one region today the region key
  // is inert; the JSONL path leaves region order to the filesystem, so a SECOND
  // region is a parity risk on that path, not this one. Noted, not fixed here.)
  return problems.sort((a, b) => cmp(a.region, b.region) || cmp(a.slug, b.slug));
}

let _problems: Problem[] | null = null;
export function getProblems(): Problem[] {
  if (_problems) return _problems;
  const problems = announce() === "db" ? problemsFromDb() : problemsFromJsonl();
  const ids = new Set<string>();
  for (const p of problems) {
    const key = `${p.region}/${p.id}`;
    if (ids.has(key)) throw new Error(`duplicate problem id ${key}`);
    ids.add(key);
  }
  _problems = problems;
  // comp signal refs must resolve into the evidence layer — a broken provenance link is a build failure.
  for (const p of problems) {
    for (const c of p.comps ?? []) {
      if (c.signal && !getSignal(c.signal)) {
        throw new Error(`${p.region}/${p.id}: comp '${c.name}' refs unknown signal '${c.signal}'`);
      }
    }
  }
  return problems;
}

function signalsFromJsonl(): Signal[] {
  const signals: Signal[] = [];
  for (const type of EVIDENCE_TYPES) {
    const dir = join(DATA, "signals", type);
    if (!existsSync(dir)) continue; // a pending feed is a registered fact — its page renders empty
    for (const f of readdirSync(dir).sort()) {
      if (!f.endsWith(".jsonl")) continue;
      const lines = readFileSync(join(dir, f), "utf8").split("\n").filter(Boolean);
      for (const [n, line] of lines.entries()) {
        const parsed = SignalSchema.safeParse(JSON.parse(line));
        if (!parsed.success) fail(`data/signals/${type}/${f}:${n + 1}`, parsed.error);
        signals.push({ ...parsed.data, type });
      }
    }
  }
  return signals;
}

function signalsFromDb(): Signal[] {
  // `raw` is the VERBATIM ledger line and it is the only signal payload this
  // loader reads. Not the derived entity keys, not `dup_of`, and above all not
  // data/errata.jsonl — the corrections ledger is real, committed, and consumed
  // by db.py's money aggregates, but the web build has never rendered it.
  // Picking it up here would silently restate EUR 10000M on /signals/tenders as
  // something else: a genuine improvement, an instant parity failure, and a
  // content change nobody reviewed.
  const rs = rows("SELECT id, type, jsonl_file, jsonl_line, raw FROM signals");

  // Reproduces the JSONL walk exactly: EVIDENCE_TYPES order (the outer loop),
  // then filename (`readdirSync().sort()`), then line number. In JS, never as
  // ORDER BY — see the note on `cmp` and on `rows` in ./db.
  const rank = (t: string) => {
    const i = (EVIDENCE_TYPES as readonly string[]).indexOf(t);
    // The JSONL path only ever walks the EVIDENCE_TYPES directories, so a row
    // of some other type is invisible there and would be a silent divergence
    // here. Refuse it instead.
    if (i === -1) throw new Error(`register.db: signal type '${t}' is not in EVIDENCE_TYPES`);
    return i;
  };
  rs.sort((a, b) =>
    rank(String(a.type)) - rank(String(b.type)) ||
    cmp(String(a.jsonl_file), String(b.jsonl_file)) ||
    Number(a.jsonl_line) - Number(b.jsonl_line)
  );

  const signals: Signal[] = [];
  for (const r of rs) {
    const parsed = SignalSchema.safeParse(JSON.parse(String(r.raw)));
    if (!parsed.success) fail(`${String(r.jsonl_file)}:${Number(r.jsonl_line)} (via register.db)`, parsed.error);
    signals.push({ ...parsed.data, type: String(r.type) as EvidenceType });
  }
  return signals;
}

let _signals: Signal[] | null = null;
export function getSignals(): Signal[] {
  if (_signals) return _signals;
  const src = announce();
  const signals = src === "db" ? signalsFromDb() : signalsFromJsonl();
  // READ FROM DISK IN BOTH PATHS, DELIBERATELY. Deriving seen.txt from the same
  // database the signals came from would make this check assert a table against
  // itself. It is one of the few checks in this file with a demonstrated
  // ability to fail, and it only has that because the two sides are independent.
  const seen = new Set(readFileSync(join(DATA, "signals", "seen.txt"), "utf8").split("\n").filter(Boolean));
  const ids = new Set<string>();
  for (const s of signals) {
    if (ids.has(s.id)) throw new Error(`duplicate signal id ${s.id}`);
    ids.add(s.id);
    if (!seen.has(s.id)) throw new Error(`signal ${s.id} missing from data/signals/seen.txt`);
  }
  // ...AND THE CONVERSE, ON THE DB PATH ONLY. The loop above asserts
  // loaded-implies-seen; it says NOTHING about a record that failed to arrive.
  // On the JSONL path that gap is harmless — the ledger files ARE the corpus,
  // so nothing can go missing without a visible ledger edit. On the DB path the
  // corpus is a projection, and a projection can come up short: MEASURED, a
  // single `DELETE FROM signals` built GREEN and shipped 6,180 of 6,181 records.
  // `db.py rebuild` does assert jsonl_lines == signals_count, but that is the
  // writer vouching for itself at write time and it is not re-checked at read
  // time — the store was already once found 7+ commits stale while reporting
  // success. seen.txt is the independent on-disk witness: architecture-v3 §
  // "seen.txt is written only on append" makes it exactly the committed id set,
  // measured today as 6,181 == 6,181 with an empty symmetric difference.
  //
  // DB PATH ONLY, deliberately: this must not be able to newly fail the
  // reference implementation mid-migration. Its one failure mode — the working
  // store holding fewer records than the committed dedup index — is, under the
  // append-only law, always a real defect.
  if (src === "db" && ids.size !== seen.size) {
    const missing = [...seen].filter((id) => !ids.has(id));
    throw new Error(
      `register.db holds ${ids.size} signals but data/signals/seen.txt lists ${seen.size}` +
      `${missing.length ? ` — missing: ${missing.slice(0, 5).join(", ")}${missing.length > 5 ? ` (+${missing.length - 5} more)` : ""}` : ""}.\n` +
      "The working store is short of the committed ledgers — rebuild it:  python3 scripts/db.py rebuild"
    );
  }
  _signals = signals;
  return signals;
}

export function getSignal(id: string): Signal | undefined {
  return getSignals().find((s) => s.id === id);
}

// ---- derived views -------------------------------------------------------

/** Extract date = newest `updated` across the register (deterministic, no wall clock). */
export function extractDate(): string {
  return getProblems().map((p) => p.updated).sort().at(-1) ?? "1970-01-01";
}

const dayMs = 86_400_000;
const daysBetween = (a: string, b: string) => Math.round((Date.parse(b) - Date.parse(a)) / dayMs);

/** Display-only split of urgency into deadline (0-2) + freshness (0-1), per SCORING.md.
    Freshness is mechanical: newest OBSERVED source < 90 days before the extract date.
 *
 *  "OBSERVED" IS LOAD-BEARING, and this is the second time this repo has been bitten
 *  by the same shape. A source `date` is the signal's own native date, and for a
 *  regulation or a subsidy call that date is a FUTURE compliance deadline — the AML
 *  Regulation sits at 2027-07-10, an NZÚ call at 2029-10-31. The previous version took
 *  the newest date of any kind, so `daysBetween(newest, extractDate())` went NEGATIVE,
 *  and negative is trivially `< 90`. Freshness was therefore incapable of returning 0
 *  for any record holding a forward-dated source: 18 of 31 records scored a free
 *  freshness point, p-0015 on a source 406 days in the future.
 *
 *  A check that cannot fail measures nothing. Freshness is supposed to answer "have we
 *  looked at this recently", so only sources we could actually have read — dated at or
 *  before the extract — count as observations. A record whose sources are ALL forward
 *  dated has made no recent observation at all and correctly scores 0.
 *
 *  This is display-only: it splits `scores.urgency` for the scorecard and never changes
 *  it. Where the split now reads deadline-heavy with no freshness, the underlying
 *  urgency score may deserve MATCH's attention — but that is a judgment, not a render. */
export function urgencySplit(p: Problem): { deadline: number; freshness: number } {
  if (p.scores.urgency === 0) return { deadline: 0, freshness: 0 };
  const observed = p.sources.map((s) => s.date).filter((d) => d <= extractDate()).sort().at(-1);
  const fresh = observed !== undefined && daysBetween(observed, extractDate()) < 90 ? 1 : 0;
  const freshness = Math.min(fresh, p.scores.urgency);
  return { deadline: Math.min(p.scores.urgency - freshness, 2), freshness };
}

/** Has a source's recorded `expires` horizon been reached? DISPLAY ONLY.
 *
 *  THE LAW (data/CONVENTIONS.md, SPEC.md §4): an expired gap-check flags
 *  staleness on the rendered page and NOTHING else. It never changes
 *  `scores.gap`, never changes `score`, never changes `status` — the SPEC §4
 *  de-rank rule stays the only mechanism that moves `gap`. Nothing in this
 *  module may feed this boolean into a number; grep its call sites before
 *  changing that.
 *
 *  It decays against `extractDate()` — the register's own newest `updated` —
 *  and NEVER against `new Date()`. A wall-clock read here would make the same
 *  commit render differently on two different days, which is a build-
 *  reproducibility bug, not a styling preference. */
export function sourceExpired(s: ProblemSource): boolean {
  return s.expires !== undefined && s.expires <= extractDate();
}

/** Register order: score desc, then deadline desc, then money desc, then id (SPEC §4).
    `stale` sinks to the bottom; `rejected` is excluded. */
export function registerRows(): Problem[] {
  const rows = getProblems().filter((p) => p.status !== "rejected");
  return rows.sort((a, b) =>
    Number(a.status === "stale") - Number(b.status === "stale") ||
    b.score - a.score ||
    urgencySplit(b).deadline - urgencySplit(a).deadline ||
    b.scores.money - a.scores.money ||
    a.id.localeCompare(b.id)
  );
}

/** Category page rows: the register order, filtered. Slug == category id (CONVENTIONS.md). */
export function categoryRows(category: string): Problem[] {
  return registerRows().filter((p) => p.category === category);
}

/** Register counts per category (rejected excluded, stale counted — mirrors registerRows). */
export function categoryCounts(): Record<string, number> {
  const counts = Object.fromEntries(CATEGORIES.map((c) => [c, 0])) as Record<string, number>;
  for (const p of registerRows()) counts[p.category] += 1;
  return counts;
}

export function signalsByType(type: EvidenceType): Signal[] {
  return getSignals()
    .filter((s) => s.type === type)
    .sort((a, b) => b.date.localeCompare(a.date) || a.id.localeCompare(b.id));
}

export function stats() {
  const problems = getProblems().filter((p) => p.status !== "rejected");
  const signals = getSignals();
  const today = extractDate();
  const deadlines = signals
    .filter((s) => s.type === "regulation" && s.date > today)
    .sort((a, b) => a.date.localeCompare(b.date));
  // Four fields, all of them rendered. `sourcesOnFile` and `deadlinesTracked`
  // were computed here and read by nobody — a count with no reader is a claim
  // no one can check, so they are gone rather than left to rot.
  return {
    open: problems.length,
    signalCount: signals.length,
    byType: Object.fromEntries(EVIDENCE_TYPES.map((t) => [t, signals.filter((s) => s.type === t).length])) as Record<EvidenceType, number>,
    nextDeadline: deadlines[0],
  };
}
