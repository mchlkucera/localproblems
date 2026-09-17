// lib/figures — the process a record describes, told in sequence.
//
// ProcessSteps is the one process figure on the record page: a two-lane
// diagram inside the Suggested solution box (details below). It carries no
// section heading and returns null without `process` or with < 2 steps.
//
// THE OWNER'S HARD RULE: "be SUPER CLEAR about where we're not sure how the
// process looks." Every step in the data states what we know about it
// (documented, inferred, unknown); the figure draws each unknown step's open
// question as a muted line under the diagram.
import type { CSSProperties, ReactNode } from "react";
import type { ProblemSource } from "../data";
import type { CiteCtx } from "../site/cite";
import { uncited } from "./cites";
import type { ProcessField, ProcessStep } from "./types";

type Props = {
  /** The record's `process` field; absent → the component renders nothing. */
  process?: ProcessField | null;
  /** `p.sources` — kept for a uniform call site. */
  sources: readonly ProblemSource[];
  /** The record page's citation context — kept for a uniform call site. */
  ctx?: CiteCtx;
};

// ---- HOW IT WORKS: ONE FIGURE, TWO LANES (owner, 2026-09-16) --------------
//
// One figure, two lanes on the same step
// columns: "Today" above "With the suggested solution", so the change reads at
// a glance. On a phone the axes swap: steps run down, the lanes side by side.
//
//   Today lane      one small node per step, labelled with WHO does it (plain
//                   `who`, leading article dropped). A step nobody does
//                   ("Nobody …") or a step the solution adds (`today: null`) is
//                   an EMPTY dashed slot. A step whose actor is "?" gets no
//                   column at all (owner, 2026-09-17), unless the teal band
//                   spans it; its question is the line under the figure.
//   Solution lane   every step the solution changes or adds (and any it
//                   removes in between) sits under ONE teal band, from the
//                   first to the last such step: many sellers → one box. A step
//                   that stays inside that span is drawn on top of the band.
//                   The band carries the main clause of `summary.after`, else
//                   a count ("3 steps change").
//   Open questions  each unknown step's own sentence, one muted line under the
//                   figure. No legend, no pills, no "our reading" badge: that
//                   nuance lives in the section's detail.
//
// Teal only for what the solution changes in the builder's favour. The grid is
// aria-hidden; a visually hidden list carries every step's full text.
// `null` without process or with < 2 steps. `sources` / `ctx` are kept for a
// uniform call site: the figure draws no pills.

const NOBODY = /^(nobody|no one)\b/i;

/** "A consultant who writes…" → "Consultant who writes…". */
function shortWho(who: string): string {
  const w = who.trim().replace(/^(a|an|the)\s+/i, "");
  return w.charAt(0).toUpperCase() + w.slice(1);
}

/** The main clause of `summary.after`, if it is short enough to label the
    band: cut before ", so", ";", " — " or ":"; at most 14 words. */
function bandLabel(after: string | null | undefined): string | null {
  if (!after) return null;
  const main = uncited(after).split(/,\s+so\s|;\s|\s[—–]\s|:\s/)[0].trim().replace(/[.!]$/, "");
  const words = main.split(/\s+/).filter(Boolean).length;
  return words >= 2 && words <= 14 ? main : null;
}

const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`;

type Cell = { lane: 1 | 2; c: number; c2?: number; cls: string; text?: string };

export function ProcessSteps({ process, sources, ctx }: Props): ReactNode {
  if (!process || process.steps.length < 2) return null;
  void sources; void ctx;
  const all = process.steps;

  const inBand = (s: ProcessStep) => s.change === "changes" || s.change === "new";
  const bandFirst = all.findIndex(inBand);
  const bandLast = all.length - 1 - [...all].reverse().findIndex(inBand);
  // A step whose actor is "?" gets NO column (owner, 2026-09-17: the dangling
  // "Not known" boxes go): the open-question line under the figure already
  // says it. The one exception is a "?" step inside the teal band, whose
  // column keeps the band continuous; it draws nothing over the band.
  const steps = all.filter((s, i) => s.who.trim() !== "?" || (bandFirst !== -1 && i >= bandFirst && i <= bandLast));
  const n = steps.length;
  if (n < 2) return null;

  const first = steps.findIndex(inBand);
  const last = steps.length - 1 - [...steps].reverse().findIndex(inBand);
  const hasBand = first !== -1;

  const cells: Cell[] = [];
  steps.forEach((s, i) => {
    const c = i + 1;
    const who = s.who.trim();
    const unknownWho = who === "?";
    // today
    if (!s.today?.trim()) cells.push({ lane: 1, c, cls: "is-empty", text: "Not done today" });
    else if (NOBODY.test(who)) cells.push({ lane: 1, c, cls: "is-empty", text: "Nobody does this" });
    else if (!unknownWho) cells.push({ lane: 1, c, cls: "", text: shortWho(who) });
    // with the suggested solution
    const covered = hasBand && i >= first && i <= last;
    if (inBand(s)) return;                      // drawn by the band
    if (s.change === "goes") {
      if (!covered) cells.push({ lane: 2, c, cls: "is-unknown", text: "No longer needed" });
      return;
    }
    if (unknownWho) return;                     // inside the band: nothing over it
    // stays: echo today's actor, quietly; on top of the band when inside it
    const echo = NOBODY.test(who) ? "Still nobody" : shortWho(who);
    cells.push({ lane: 2, c, cls: `is-stays${covered ? " is-over" : ""}`, text: echo });
  });

  let label: string | null = null;
  let run: [number, number] = [first + 1, last + 2];
  if (hasBand) {
    const covered = steps.slice(first, last + 1);
    const changed = covered.filter((s) => s.change === "changes").length;
    const added = covered.filter((s) => s.change === "new").length;
    label = bandLabel(process.summary?.after) ??
      [changed && plural(changed, "step changes", "steps change"), added && plural(added, "step added", "steps added")]
        .filter(Boolean).join(", ");
    // the label sits on the longest stretch of the band with nothing drawn over it
    let best: [number, number] = [first, first];
    let start = -1;
    for (let i = first; i <= last + 1; i++) {
      const open = i <= last && (steps[i].change !== "stays" || steps[i].who.trim() === "?");
      if (open && start === -1) start = i;
      if (!open && start !== -1) {
        if (i - start > best[1] - best[0]) best = [start, i];
        start = -1;
      }
    }
    run = [best[0] + 1, best[1] + 1];
  }

  const questions = all.filter((s) => s.known === "unknown" && s.today?.trim()).map((s) => uncited(s.today!));
  const pos = (c: number, c2: number) => ({ "--c": c, "--c2": c2, "--r": c + 1, "--r2": c2 + 1 }) as CSSProperties;

  return (
    <figure className="lk lk-pd" style={{ "--n": n } as CSSProperties}>
      <div className="lk-pd-grid" aria-hidden="true">
        <span className="lk-pd-lane is-l1">Today</span>
        <span className="lk-pd-lane is-l2">With the suggested solution</span>
        <span className="lk-pd-rule is-l1" />
        <span className="lk-pd-rule is-l2" />
        {hasBand && <span className="lk-pd-band is-l2" style={pos(first + 1, last + 2)} />}
        {hasBand && label && (
          <span className="lk-pd-bandlabel is-l2" style={pos(run[0], Math.max(run[1], run[0] + 1))}>{label}</span>
        )}
        {cells.map((k, j) => (
          <span key={j} className={`lk-pd-node is-l${k.lane} ${k.cls}`} style={pos(k.c, (k.c2 ?? k.c) + 1)}>
            {k.text}
          </span>
        ))}
      </div>
      <ol className="lk-sr">
        {all.map((s, i) => (
          <li key={i}>
            {s.who.trim() === "?" ? "Who does this is not known" : s.who}.{" "}
            Today: {s.today?.trim() ? uncited(s.today) : "not done"}.{" "}
            With the suggested solution: {s.change === "goes" ? "no longer needed" : s.after ? uncited(s.after) : "same as today"}.
          </li>
        ))}
      </ol>
      {questions.length > 0 && (
        <div className="lk-pd-q">
          {questions.map((q, i) => <p key={i}>{q.replace(/[.]?$/, ".")}</p>)}
        </div>
      )}
    </figure>
  );
}
