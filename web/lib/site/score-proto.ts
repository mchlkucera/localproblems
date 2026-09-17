// PROTOTYPE (2026-09-17): the record page's scores as sections, for an owner
// decision. NOT the rubric. Every value is derived deterministically from the
// record's existing fields, and nothing here is stored or checked. The final
// rungs, words and the "willing to pay" field are being worked out elsewhere;
// replace this module when they land.
//
//   Opportunity          = scores.demand                  /2
//   Why now              = scores.urgency                 /3  (deadline + freshness, as
//                          SCORING.md has it; the word reads the deadline part only)
//   Willing to pay       = scores.money                   /2  (still public-money proximity)
//   Validated abroad     = scores.proof                   /3
//   Competition          = scores.gap                     /2  (more points = less competition)
//   Execution difficulty = entry.level Easy 3 … Very hard 0 /3 (more points = easier),
//                          shown beside the total, never summed into it
//   Total                = the five rubric checks = scores total /12, so the record page
//                          and the front page never disagree (deployed 2026-09-17)
import { priceReceipts, urgencySplit, type EntryLevel, type Problem } from "../data";
import { dimRefs } from "../scorecard";
import { entryGates } from "../format";

export type ProtoKey = "opportunity" | "why-now" | "willing-to-pay" | "validated-abroad" | "competition" | "execution-difficulty";

export type ProtoScore = {
  key: ProtoKey;
  /** the section's name, as the TOC and the heading say it */
  label: string;
  /** a level word appended to the label in the TOC ("Competition · Low") */
  labelSuffix?: string;
  n: number;
  max: number;
  /** the judgement word for this rung */
  word: string;
  /** one line from the data: counts, never company names */
  reason: string;
  /** false for a score shown beside the total but not summed into it */
  inTotal: boolean;
};

const WORDS: Record<ProtoKey, string[]> = {
  opportunity: ["Unclear pain", "Some pain", "Clear, recurring pain"],
  "why-now": ["No deadline", "Deadline later", "Deadline soon"],
  "willing-to-pay": ["No sign yet", "Some buyers", "Already paying"],
  "validated-abroad": ["Not yet", "Early abroad", "Proven once", "Proven in 2+ markets"],
  competition: ["Crowded", "Early rivals only", "Open"],
  "execution-difficulty": ["Very hard", "Hard", "Moderate", "Easy"],
};

const LEVEL_POINTS: Record<EntryLevel, number> = { easy: 3, moderate: 2, hard: 1, "very-hard": 0 };
const COMPETITION_LEVEL = ["High", "Medium", "Low"];

const count = (k: number, one: string, many: string) => `${k} ${k === 1 ? one : many}`;
const clamp = (n: number, max: number) => Math.max(0, Math.min(max, n));

export function protoScores(p: Problem): ProtoScore[] {
  const refs = dimRefs(p);
  const comps = p.comps ?? [];
  const locals = p.locals ?? [];

  const demand = clamp(p.scores.demand, 2);
  const deadline = clamp(urgencySplit(p).deadline, 2);
  const urgency = clamp(p.scores.urgency, 3);
  const money = clamp(p.scores.money, 2);
  const proof = clamp(p.scores.proof, 3);
  const gap = clamp(p.scores.gap, 2);
  const ease = LEVEL_POINTS[p.entry.level] ?? 0;

  const nDemand = refs.demand.length;
  const nUrgency = refs.urgency.length;
  const prices = priceReceipts(p).length;
  const publicMoney = refs.money.filter((n) => p.sources[n - 1]?.type !== "price").length;
  const countries = new Set(comps.map((c) => c.geo)).size;
  const direct = locals.filter((l) => l.competes === "direct");
  const directEst = direct.filter((l) => l.maturity === "established").length;
  const adjacent = locals.length - direct.length;

  const reasons: Record<ProtoKey, string> = {
    opportunity: nDemand
      ? `${count(nDemand, "source documents", "sources document")} the pain`
      : "No complaint or request on file yet",
    "why-now": deadline === 2
      ? `A compliance date within 18 months · ${count(nUrgency, "source", "sources")}`
      : deadline === 1
        ? `A compliance date more than 18 months away · ${count(nUrgency, "source", "sources")}`
        : "No dated rule forces buyers to act",
    // (the +1 for evidence under 90 days old is appended below)
    "willing-to-pay": [
      prices ? count(prices, "price paid on file", "prices paid on file") : "No price paid on file",
      publicMoney ? count(publicMoney, "public contract or grant nearby", "public contracts or grants nearby") : "",
    ].filter(Boolean).join(" · "),
    "validated-abroad": comps.length
      ? `${count(comps.length, "company", "companies")} abroad, in ${count(countries, "country", "countries")}`
      : "No company abroad on file",
    competition: direct.length
      ? `${count(direct.length, "Czech seller", "Czech sellers")}, ${directEst ? `${directEst} established` : "all early"}${adjacent ? ` · ${adjacent} nearby` : ""}`
      : `No Czech seller on file${adjacent ? ` · ${adjacent} nearby sell something else` : ""}`,
    "execution-difficulty": `Set by ${entryGates(p.entry).toLowerCase()}`,
  };

  if (urgencySplit(p).freshness) reasons["why-now"] += " · +1 for evidence under 90 days old";

  const row = (key: ProtoKey, label: string, n: number, max: number, labelSuffix?: string, wordAt = n, inTotal = true): ProtoScore =>
    ({ key, label, labelSuffix, n, max, word: WORDS[key][wordAt], reason: reasons[key], inTotal });

  return [
    row("opportunity", "The opportunity", demand, 2),
    row("why-now", "Why now", urgency, 3, undefined, deadline),
    row("willing-to-pay", "Willing to pay", money, 2),
    row("validated-abroad", "Validated abroad", proof, 3),
    row("competition", "Competition", gap, 2, COMPETITION_LEVEL[gap]),
    row("execution-difficulty", "Execution difficulty", ease, 3, undefined, ease, false),
  ];
}

export const protoTotal = (rows: ProtoScore[]) => {
  const summed = rows.filter((r) => r.inTotal);
  return { n: summed.reduce((s, r) => s + r.n, 0), max: summed.reduce((s, r) => s + r.max, 0) };
};
