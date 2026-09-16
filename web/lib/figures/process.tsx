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
