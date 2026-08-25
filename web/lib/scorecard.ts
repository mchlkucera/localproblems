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

// ---- the PUBLIC scorecard: plain labels + plain reads (owner, 2026-08-24) ---
// The record page no longer shows the SCORING.md verdict words (UNPROVEN, FAINT,
// LIKELY …) — "who are you impressing with the jargon". Each dimension is stated
// with a plain, builder-facing label and one plain line, and the whole card is
// headed "Opportunity {sum}/12". Polarity is consistent: on EVERY row more is
// better (gap high = the field is open, not "more competition"). The Build line
// is separate — it is feasibility, not opportunity. VERDICTS/criterion above
// stay in the module: they remain the vocabulary the build asserts against
// SCORING.md (lib layout.tsx `assertScoringVocabulary`), just not rendered.

/** Dimension order and plain label on the public card — proof first, urgency
    ("why now") last, exactly as the owner's exemplar reads. */
export const SCORE_ROWS: { dim: Dim; label: string }[] = [
  { dim: "proof", label: "Validated abroad" },
  { dim: "gap", label: "Local opportunity" },
  { dim: "demand", label: "Demand signal" },
  { dim: "money", label: "Money available" },
  { dim: "urgency", label: "Why now" },
];

/** One plain line per dimension level. Indexed by the raw sub-score; higher is
    always the better reading. No verdict words, no rubric jargon. */
const READS: Record<Dim, string[]> = {
  proof: [
    "no funded example found abroad",
    "one example abroad, still thin",
    "funded companies build this elsewhere",
    "funded and proven across several markets",
  ],
  gap: [
    "local competitors not yet checked",
    "no local player found — field open",
    "field open — only legacy or adjacent players",
  ],
  demand: [
    "demand assumed, not yet shown",
    "documented, not yet loud",
    "recurring, documented demand",
  ],
  money: [
    "no funding receipt on file",
    "an adjacent grant or tender nearby",
    "funding attached to this",
  ],
  urgency: [
    "no dated trigger",
    "a trigger, but over a year out",
    "a dated trigger, closing in",
    "a dated deadline is forcing the change",
  ],
};

/** The plain read for a dimension. Proof folds in the real comps count when
    there are analogs on file ("4 funded companies build this elsewhere"), so
    the strongest row states its own evidence; everything else is the level
    phrase. Total is a pure function of the sub-score — safe for every record. */
/** The one-line read under each score.
 *
 *  IT IS DERIVED FROM THE DATA, NOT ONLY FROM THE NUMBER, and that is the whole
 *  point: a read that contradicts what the reader can see two inches below it
 *  destroys more trust than a missing read ever would. Two score values are
 *  ambiguous and both were rendering falsehoods on live records:
 *
 *  `gap: 0` means TWO OPPOSITE THINGS. SCORING.md defines it as "CZ incumbent
 *  check not done", but the SPEC §4 de-rank rule ALSO sets it to 0 when a local
 *  player IS found. Twelve live records — every de-ranked one — printed "local
 *  competitors not yet checked" directly above the competitors that had been
 *  found. The presence of a gap-check source is what separates the two, so the
 *  read asks the sources, not the integer.
 *
 *  `proof: 0` reads "no funded example found abroad", which is a lie whenever
 *  comps are listed under it — p-0008 printed it above two companies with
 *  €10.2M and €6M Series A rounds on file. Where comps exist the read states
 *  the count and lets "Proven abroad" speak; whether the score itself is right
 *  is a MATCH judgment this function must not pre-empt. */
export function scoreRead(p: Problem, dim: Dim): string {
  const n = p.comps?.length ?? 0;
  if (dim === "proof") {
    if (n > 0 && p.scores.proof >= 3) return `${n} funded companies, proven across markets`;
    if (n > 0 && p.scores.proof === 2) return `${n} funded companies build this elsewhere`;
    if (n > 0 && p.scores.proof <= 1)
      return `${n} comparable${n === 1 ? "" : "s"} on file — see Proven abroad`;
  }
  if (dim === "gap" && p.scores.gap === 0) {
    const checked = p.sources.some((s) => s.type === "gap-check");
    return checked
      ? "local players already sell this — see Local competition"
      : "the local market has not been checked";
  }
  return READS[dim][p.scores[dim]];
}

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
