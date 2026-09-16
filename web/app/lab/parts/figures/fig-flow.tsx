// Option A — the suggested solution as a before/after flow.
// Top row: today's steps, each read out of the problem prose with its own
// citation. Bottom row: the same columns with the record's suggested solution —
// dashed, teal, uncited (a proposal, not evidence). The tally under it is
// DERIVED from the steps, never authored, so it cannot overstate the change.
import type { ReactNode } from "react";
import type { Flow } from "./hand";

type Cite = (nums: number[]) => ReactNode;

const CHANGE_WORD: Record<Flow["steps"][number]["change"], string> = {
  kept: "stays",
  changed: "changes",
  removed: "goes",
  added: "new",
  merged: "one seller",
};

export function FlowFig({ flow, cite }: { flow: Flow; cite: Cite }) {
  const n = flow.steps.length;
  const cols = { gridTemplateColumns: `repeat(${n}, minmax(0, 1fr))` };
  const merge = flow.merge;
  const inMerge = (i: number) => !!merge && i + 1 >= merge.from && i + 1 <= merge.to;

  // ---- the tally, derived ------------------------------------------------
  let tally: { k: string; a: number; b: number };
  if (flow.shape === "consolidation") {
    const today = new Set(flow.steps.filter((s) => s.supplier).map((s) => s.supplier)).size;
    tally = { k: "Sellers a buyer deals with for these steps", a: today, b: merge ? 1 : today };
  } else {
    tally = {
      k: "Steps that re-enter what someone already wrote",
      a: flow.steps.filter((s) => s.today && s.reentry).length,
      b: flow.steps.filter((s) => s.after && s.afterReentry).length,
    };
  }

  return (
    <div className="fgf">
      <p className="fgf-key">
        <span className="fgf-key-i"><span className="fgf-sw" /> Today, from the problem prose, each step cited</span>
        <span className="fgf-key-i"><span className="fgf-sw fgf-sw--sol" /> The suggested solution: a proposal, uncited</span>
      </p>
      <div className="fgf-grid" style={cols}>
        {/* row 1 — today */}
        {flow.steps.map((s, i) => (
          <div key={`t${i}`} className={s.today ? "fgf-card" : "fgf-card fgf-card--none"}>
            {s.today ? (
              <>
                <span className="fgf-who">{s.who}</span>
                <span className="fgf-what">{s.today}</span>
                <span className="fgf-foot">
                  {s.reentry && <span className="fgf-tag">re-enters</span>}
                  {s.cites.length > 0 && cite(s.cites)}
                </span>
              </>
            ) : (
              <span className="fgf-what fgf-muted">Not done today</span>
            )}
            {i < n - 1 && <span className="fgf-arrow" aria-hidden="true" />}
          </div>
        ))}

        {/* row 2 — what happens to each step */}
        {flow.steps.map((s, i) =>
          inMerge(i) && i + 1 !== merge!.from ? null : (
            <div
              key={`c${i}`}
              className={s.change === "kept" ? "fgf-change" : "fgf-change is-sol"}
              style={inMerge(i) ? { gridColumn: `${i + 1} / span ${merge!.to - merge!.from + 1}` } : undefined}
            >
              <span>{CHANGE_WORD[s.change]}</span>
            </div>
          ),
        )}

        {/* row 3 — with the suggested solution */}
        {flow.steps.map((s, i) => {
          if (inMerge(i)) {
            if (i + 1 !== merge!.from) return null;
            return (
              <div key={`a${i}`} className="fgf-card fgf-card--sol fgf-card--merge" style={{ gridColumn: `${i + 1} / span ${merge!.to - merge!.from + 1}` }}>
                <span className="fgf-who">{merge!.who}</span>
                <span className="fgf-what">{merge!.what}</span>
              </div>
            );
          }
          return (
            <div key={`a${i}`} className={s.change === "kept" ? "fgf-card fgf-card--kept" : "fgf-card fgf-card--sol"}>
              {s.after ? (
                <>
                  <span className="fgf-who">{s.afterWho ?? s.who}</span>
                  <span className="fgf-what">{s.after}</span>
                  {s.afterCites && s.afterCites.length > 0 && <span className="fgf-foot">{cite(s.afterCites)}</span>}
                </>
              ) : (
                <span className="fgf-what fgf-muted">Gone</span>
              )}
            </div>
          );
        })}
      </div>

      <p className="fgf-tally">
        <span className="fgf-tally-k">{tally.k}</span>
        <span className="fgf-tally-v">
          <b>{tally.a}</b> today <span aria-hidden="true">→</span> <b className="fg-sol">{tally.b}</b> with the suggested solution
        </span>
      </p>
    </div>
  );
}
