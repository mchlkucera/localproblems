// Scorecard vocabulary. Verdict words and bands are constants asserted at build
// time against ../SCORING.md — drift breaks the build, not the page (SPEC.md §5).
import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { extractDate, type Problem, type ProblemSource, urgencySplit } from "./data";

export const DIMS = ["proof", "money", "urgency", "demand", "gap"] as const;
export type Dim = (typeof DIMS)[number];

export const MAX: Record<Dim, number> = { proof: 3, money: 2, urgency: 3, demand: 2, gap: 2 };

export const VERDICTS: Record<Dim, string[]> = {
  proof: ["UNPROVEN", "THIN", "PROVEN", "VALIDATED"],
  money: ["UNFUNDED", "NEARBY", "ATTACHED"],
  urgency: ["NONE", "MILD", "BUILDING", "FORCING"],
  demand: ["ASSUMED", "SCATTERED", "DOCUMENTED"],
  gap: ["UNCHECKED", "LIKELY", "CONFIRMED"],
};

export const BANDS: [number, string][] = [
  [10, "PRIME"], [8, "STRONG"], [5, "FAIR"], [0, "FAINT"],
];
export const bandWord = (score: number) => BANDS.find(([min]) => score >= min)![1];

// Rubric criteria, quoted from SCORING.md — the rundown drawers state the
// criterion for the achieved level, never invented prose.
const CRITERIA: Record<Dim, string[]> = {
  proof: [
    "no foreign analog",
    "one weak analog",
    "funded analog in DE/AT/PL/Nordics + no CZ player found",
    "analogs in 2+ markets AND validated CEE-adjacent",
  ],
  money: [
    "no budget attached",
    "relevant tender/grant exists",
    "OPEN tender or grant ≥ ~5M CZK, or recurring annual spend",
  ],
  urgency: [], // composed from the deadline + freshness sub-scores below
  demand: [
    "pain assumed, not documented",
    "scattered complaints",
    "recurring documented complaints, petition, or industry pressure",
  ],
  gap: [
    "CZ incumbent check not done",
    "quick search found no CZ player",
    "absence confirmed or only weak/legacy incumbents (named)",
  ],
};

const DEADLINE_CRITERIA = [
  "no regulatory trigger",
  "compliance date >18mo out",
  "compliance date <18mo (forcing function live)",
];
const FRESHNESS_CRITERION = "newest source < 90 days";

export function criterion(p: Problem, dim: Dim): string {
  if (dim !== "urgency") return CRITERIA[dim][p.scores[dim]];
  const { deadline, freshness } = urgencySplit(p);
  const parts = [`${DEADLINE_CRITERIA[deadline]} (${deadline}/2)`];
  if (freshness) parts.push(`${FRESHNESS_CRITERION} (1/1)`);
  return parts.join("; ");
}

// ---- source refs per dimension (docs/archive/05 §4 rules) ----------------

const TYPE_TO_DIM: Record<string, Dim> = {
  arbitrage: "proof",
  tender: "money", contract: "money", subsidy: "money",
  regulation: "urgency",
  complaint: "demand", news: "demand",
  "gap-check": "gap",
};

/** 1-based S-numbers backing each dimension. Priority: explicit dims: tag,
    then type→dimension mapping (+ the "Demand point" gap-check convention),
    then freshness always refs the newest sub-90-day source. */
export function dimRefs(p: Problem): Record<Dim, number[]> {
  const refs: Record<Dim, number[]> = { proof: [], money: [], urgency: [], demand: [], gap: [] };
  const add = (dim: Dim, n: number) => { if (!refs[dim].includes(n)) refs[dim].push(n); };

  p.sources.forEach((s: ProblemSource, i) => {
    const n = i + 1;
    if (s.dims) {
      for (const d of s.dims) add(d, n);
      return;
    }
    const dim = TYPE_TO_DIM[s.type];
    if (dim) add(dim, n);
    if (s.type === "gap-check" && s.note.includes("Demand point")) add("demand", n);
  });

  const { freshness } = urgencySplit(p);
  if (freshness) {
    const newest = [...p.sources.entries()].sort((a, b) => a[1].date.localeCompare(b[1].date)).at(-1)!;
    add("urgency", newest[0] + 1);
  }
  for (const dim of DIMS) refs[dim].sort((a, b) => a - b);
  return refs;
}

// ---- build-time assertion ------------------------------------------------

let _asserted = false;
export function assertScoringVocabulary(): void {
  if (_asserted) return;
  const scoring = readFileSync(join(resolve(process.cwd(), ".."), "SCORING.md"), "utf8");
  const words = [...Object.values(VERDICTS).flat(), ...BANDS.map(([, w]) => w)];
  const missing = words.filter((w) => !scoring.includes(w));
  if (missing.length)
    throw new Error(`verdict words not found verbatim in SCORING.md: ${missing.join(", ")} — fix the constants, never the page`);
  _asserted = true;
}
