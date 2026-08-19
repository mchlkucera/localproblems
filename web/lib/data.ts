// The data layer: reads ../data at build time, zod-validated.
// Validation failure = build failure = deploy blocked (SPEC.md §5).
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { load as yamlLoad } from "js-yaml";
import { z } from "zod";

const ROOT = resolve(process.cwd(), "..");
const DATA = join(ROOT, "data");

export const CATEGORIES = [
  "fintech", "health", "housing", "energy", "mobility", "govtech",
  "retail-services", "b2b", "legal-compliance", "education", "environment", "other",
] as const;

export const EVIDENCE_TYPES = ["funded", "regulation", "tenders", "demand"] as const;
export type EvidenceType = (typeof EVIDENCE_TYPES)[number];

const isoDate = z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "ISO date required");

// ---- evidence layer ------------------------------------------------------

const SignalSchema = z.object({
  id: z.string().regex(/^[a-z]{2,10}-[\w.-]+$/),
  source: z.enum(["ted", "hlidac", "yc", "round", "reg-scan", "arb-scan", "feed", "demand-scan", "suggest", "reddit"]),
  url: z.string().url(),
  date: isoDate,
  title: z.string().min(1),
  sector: z.enum(CATEGORIES),
  geo_origin: z.string().regex(/^([A-Z]{2}|EU)$/),
  money_eur: z.number().nullable(),
  money_note: z.string(),
  summary: z.string().min(1),
  scores: z.object({
    scale: z.number().int().min(0).max(3),
    money: z.number().int().min(0).max(3),
    urgency: z.number().int().min(0).max(3),
    recurrence: z.number().int().min(0).max(3),
  }),
  notes: z.string().optional(),
});
export type Signal = z.infer<typeof SignalSchema> & { type: EvidenceType };

// ---- region layer --------------------------------------------------------

const STATUSES = ["candidate", "active", "watching", "stale", "claimed", "solved", "rejected"] as const;

const SourceSchema = z.looseObject({
  type: z.string().min(1),
  url: z.string().min(1),
  note: z.string().min(1),
  date: isoDate,
  signal: z.string().optional(),
  dims: z.array(z.enum(["proof", "money", "urgency", "demand", "gap"])).optional(),
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
export type Comp = z.infer<typeof CompSchema>;

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

let _problems: Problem[] | null = null;
export function getProblems(): Problem[] {
  if (_problems) return _problems;
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

let _signals: Signal[] | null = null;
export function getSignals(): Signal[] {
  if (_signals) return _signals;
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
  const seen = new Set(readFileSync(join(DATA, "signals", "seen.txt"), "utf8").split("\n").filter(Boolean));
  const ids = new Set<string>();
  for (const s of signals) {
    if (ids.has(s.id)) throw new Error(`duplicate signal id ${s.id}`);
    ids.add(s.id);
    if (!seen.has(s.id)) throw new Error(`signal ${s.id} missing from data/signals/seen.txt`);
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
    Freshness is mechanical: newest source < 90 days before the extract date. */
export function urgencySplit(p: Problem): { deadline: number; freshness: number } {
  if (p.scores.urgency === 0) return { deadline: 0, freshness: 0 };
  const newest = p.sources.map((s) => s.date).sort().at(-1)!;
  const fresh = daysBetween(newest, extractDate()) < 90 ? 1 : 0;
  const freshness = Math.min(fresh, p.scores.urgency);
  return { deadline: Math.min(p.scores.urgency - freshness, 2), freshness };
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
  return {
    open: problems.length,
    sourcesOnFile: problems.reduce((n, p) => n + p.sources.length, 0),
    signalCount: signals.length,
    byType: Object.fromEntries(EVIDENCE_TYPES.map((t) => [t, signals.filter((s) => s.type === t).length])) as Record<EvidenceType, number>,
    deadlinesTracked: signals.filter((s) => s.type === "regulation").length,
    nextDeadline: deadlines[0],
  };
}
