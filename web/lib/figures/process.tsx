// lib/figures — the process a record describes, told in sequence.
//
// The record page reads: The problem → HOW IT WORKS TODAY (so the builder can
// picture it) → the Suggested solution box, which CONTAINS the process with the
// solution applied. So there are two pieces, placed apart by the page:
//
//   <ProcessToday process sources ctx />  right after The problem prose
//   <ProcessAfter process sources compact />  inside the Suggested solution box,
//                                             under the solution sentence
//
// Neither carries a section heading. Both return null without `process`.
//
// THE OWNER'S HARD RULE: "be SUPER CLEAR about where we're not sure how the
// process looks." Every step states what we know about it:
//   documented — backed by cited sources: a solid card with source pills.
//   inferred   — our reading of the prose, no direct source: a dashed card, a
//                visible "?" and "not documented, our reading".
//   unknown    — we do not know this step: a "?" card that states the open
//                question. The actor may itself be "?".
// A documented step whose citations do not resolve is DRAWN AS INFERRED — the
// kit never shows a solid card it cannot back with a pill. (The schema should
// refuse such a step; this is the fallback, not the rule.)
//
// The after half is always a proposal: uncited, dashed, teal. Inside the
// Suggested solution box that box's own label already says so, so the compact
// form adds no "proposal" chrome of its own.
import type { CSSProperties, ReactNode } from "react";
import type { ProblemSource } from "../data";
import type { CiteCtx } from "../site/cite";
import { citedText, kitCtx, pills, uncited, validCites } from "./cites";
import type { ProcessField, ProcessKnown, ProcessStep } from "./types";

type Props = {
  /** The record's `process` field; absent → the component renders nothing. */
  process?: ProcessField | null;
  /** `p.sources` — S-numbers resolve against it (S1 = sources[0]). */
  sources: readonly ProblemSource[];
  /** The record page's citation context. Strongly recommended: see ./cites.tsx. */
  ctx?: CiteCtx;
};

/** What the page may show for a step, after checking its citations. */
function stateOf(s: ProcessStep, sources: readonly ProblemSource[]): ProcessKnown {
  if (s.known === "documented" && validCites(s.cites, sources).length === 0) return "inferred";
  return s.known;
}

/** Columns for a horizontal run: one row up to four steps, two rows beyond. */
// 4 steps wrap to 2×2 rather than four ~150px columns: at 680px a four-up row
// squeezed a long "open question" card to two words per line (owner review,
// 2026-09-16). 5 and 6 steps are unchanged (3 up, then the remainder).
const colsFor = (n: number) => (n <= 3 ? n : Math.ceil(n / 2));

const Q = ({ big }: { big?: boolean }) => (
  <span className={big ? "lk-q lk-q--big" : "lk-q"} aria-hidden="true">?</span>
);

function Who({ who }: { who: string }) {
  if (who.trim() === "?") {
    return <span className="lk-who lk-who--q"><Q /> Who does this is not documented</span>;
  }
  return <span className="lk-who">{who}</span>;
}

// ---- HOW IT WORKS TODAY ---------------------------------------------------

export function ProcessToday({ process, sources, ctx }: Props): ReactNode {
  if (!process) return null;
  const steps = process.steps.filter((s) => s.today);
  const summary = process.summary?.today?.trim();
  if (steps.length === 0 && !summary) return null;
  const c = kitCtx(sources, ctx);
  const cols = colsFor(steps.length);
  const states = steps.map((s) => stateOf(s, sources));
  const unsure = states.some((st) => st !== "documented") || steps.some((s) => s.who.trim() === "?");

  return (
    <figure className="lk lk-proc" aria-label="How it works today">
      <figcaption className="lk-lead">How it works today</figcaption>
      {summary && <p className="lk-sum">{citedText(summary, sources, c, "pt")}</p>}
      {steps.length > 0 && (
        <ol className="lk-steps" style={{ "--lk-cols": cols } as CSSProperties}>
          {steps.map((s, i) => {
            const st = states[i];
            const rowEnd = (i + 1) % cols === 0 || i === steps.length - 1;
            return (
              <li key={i} className={`lk-step is-${st}${rowEnd ? " is-rowend" : ""}`}>
                {st === "unknown" ? (
                  <>
                    <span className="lk-step-hd">
                      <span className="lk-n">{i + 1}</span>
                      <Who who={s.who} />
                    </span>
                    <span className="lk-open"><Q big /><span className="lk-open-t">{s.today}</span></span>
                    <span className="lk-step-ft"><span className="lk-flag">Open question</span></span>
                  </>
                ) : (
                  <>
                    <span className="lk-step-hd">
                      <span className="lk-n">{i + 1}</span>
                      <Who who={s.who} />
                      {st === "inferred" && <span className="lk-corner"><Q /></span>}
                    </span>
                    <span className="lk-what">{s.today}</span>
                    <span className="lk-step-ft">
                      {s.reenters && <span className="lk-tag">re-enters</span>}
                      {st === "inferred" && <span className="lk-flag">Not documented, our reading</span>}
                      {pills(s.cites, sources, c)}
                    </span>
                  </>
                )}
              </li>
            );
          })}
        </ol>
      )}
      {unsure && (
        <p className="lk-key">
          <Q /> marks what the sources do not show: a dashed card is our reading of the prose, a gray card an open question.
        </p>
      )}
    </figure>
  );
}

// ---- THE PROCESS WITH THE LIKELY SOLUTION ---------------------------------

const CHANGE_MARK: Record<ProcessStep["change"], string> = {
  stays: "stays",
  changes: "changes",
  goes: "goes",
  new: "new",
};

/** Re-entry, measured from the flags: today = steps flagged `reenters`; after
    = those of them the solution leaves in place (`change: stays`). Derived,
    never authored, so it cannot overstate the change. */
export function reentryTally(process: ProcessField | null | undefined) {
  const flagged = (process?.steps ?? []).filter((s) => s.today && s.reenters);
  return {
    today: flagged.length,
    after: flagged.filter((s) => s.change === "stays").length,
    ourReading: flagged.filter((s) => s.known !== "documented").length,
  };
}

export function ProcessAfter({ process, sources, compact = true }: Props & {
  /** true (default): the block that sits INSIDE the page's Suggested solution
      box, under the solution sentence — no heading, no proposal chrome.
      false: standalone, with its own lead-in and proposal frame. */
  compact?: boolean;
}): ReactNode {
  if (!process || process.steps.length === 0) return null;
  void sources; // the after half is never cited; kept for a uniform call site
  const summary = process.summary?.after ? uncited(process.summary.after) : "";
  const steps = process.steps;
  const cols = colsFor(steps.length);
  // number each step as ProcessToday does; a step the solution adds gets "+"
  let k = 0;
  const nums = steps.map((s) => (s.today ? String(++k) : "+"));
  const tally = reentryTally(process);

  const body = (
    <>
      {summary && <p className="lk-sum lk-sum--after">{summary}</p>}
      <p className="lk-inlabel">The process with it</p>
      <ol className="lk-steps lk-steps--after" style={{ "--lk-cols": cols } as CSSProperties}>
        {steps.map((s, i) => {
          const rowEnd = (i + 1) % cols === 0 || i === steps.length - 1;
          const unknownToday = s.known === "unknown";
          const text =
            s.change === "goes" ? s.today :
            s.change === "stays" ? (s.after ?? s.today) :
            s.after;
          return (
            <li key={i} className={`lk-astep is-${s.change}${rowEnd ? " is-rowend" : ""}`}>
              <span className="lk-step-hd">
                <span className={s.today ? "lk-n" : "lk-n lk-n--new"}>{nums[i]}</span>
                <span className={`lk-mark lk-mark--${s.change}`}>{CHANGE_MARK[s.change]}</span>
              </span>
              {(s.change === "stays" || s.change === "goes") && s.who.trim() !== "?" && (
                <span className="lk-awho">{s.who}</span>
              )}
              <span className="lk-atext">
                {unknownToday && s.change === "stays" && <Q />}
                {s.change === "goes" ? <s>{text}</s> : text}
              </span>
            </li>
          );
        })}
      </ol>
      {tally.today > 0 && (
        <p className="lk-tally">
          <span>Steps that re-enter what someone already wrote</span>
          <span className="lk-tally-v">
            <b>{tally.today}</b> today <span aria-hidden="true">→</span> <b className="lk-teal">{tally.after}</b> with it
            {tally.ourReading > 0 && <span className="lk-tally-n"> ({tally.ourReading} of today’s our reading)</span>}
          </span>
        </p>
      )}
    </>
  );

  if (compact) return <div className="lk lk-after">{body}</div>;
  return (
    <figure className="lk lk-after lk-after--solo" aria-label="How it could work: a proposal">
      <figcaption className="lk-lead">How it could work <span className="lk-proposal">a proposal, uncited</span></figcaption>
      {body}
    </figure>
  );
}

// ---- HOW IT WORKS: ONE FIGURE, TWO LANES (owner, 2026-09-16) --------------
//
// Replaces the rejected D5 step table. One figure, two lanes on the same step
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
