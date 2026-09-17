// lib/figures — the record-page figure kit. Import from here:
//
//   import { ProcessToday, ProcessAfter, FieldTimeline, FieldGrid, CompMap, MoneyScale }
//     from "../../../../../lib/figures";   // from web/app/(site)/problem/[region]/[id]/page.tsx
//
// Every component is a plain server function: no hooks, no client code. Each
// returns `null` when its data is too thin, so CALL it before the JSX and test
// the result before drawing any heading or wrapper around it:
//
//   const fieldFig = FieldTimeline({ p });
//   …
//   {fieldFig}
//
// Record-page redesign (docs/record-page-redesign.md §5), the current slots:
//   ProcessSteps   article column 680px   the two-lane process diagram (owner,
//                                          2026-09-16): Today above With the
//                                          suggested solution; the lanes sit side
//                                          by side on a phone. Props {process,
//                                          sources, ctx}; null under 2 steps
//   FieldStrip     article column 680px   head of Who already sells this
//   MaturityDot    inline, 10px           each company row, so strip and rows match
//   LocalMatrix    ~330px or 680px        Competition: the Czech players as a 2x2
//                                          (maturity x competes), one dot each.
//                                          {p, scope?}; null without locals
//   CompMap        ~330px or 680px        Validated abroad: one dot per comparable
//                                          at its country. {p, scope?}; null
//                                          without comps (or none drawable)
//   Every dot is a DotPeek (field.tsx): a popovertarget button with data-peek
//   and an .ls-peek card. Pass a distinct `scope` to each extra copy on one
//   page (the Read more sheet: scope "s"), or popover ids collide.
//   Side by side:  <div className="lk-pair"><div className="lk-pair-in">
//                    {matrix}{map}</div></div>  — two columns at >= 620px of
//                    its own width, stacked under that (a container query)
// ProcessToday, ProcessAfter, FieldTimeline, FieldGrid and MoneyScale
// below are the previous slots, kept until the page stops importing them.
//
// Previous slots and widths (the lab record page's own --ls-main / --ls-rail):
//   ProcessToday   article column 680px   right after The problem prose
//   ProcessAfter   ~630px                 INSIDE the Suggested solution box,
//                                          under the solution sentence
//   FieldTimeline  article column 680px   head of Local competition
//   MoneyScale     article column 680px   Who pays
//   FieldGrid      rail 272px             under the Opportunity card
export { ProcessSteps, ProcessToday, ProcessAfter, reentryTally } from "./process";
export { FieldStrip, MaturityDot, DotPeek, FieldTimeline, FieldGrid, type Maturity } from "./field";
export { CompMap, compNextDoor } from "./comp-map";
export { LocalMatrix } from "./matrix";
export { MoneyScale, moneyDots } from "./money";
// Willing to pay (owner, 2026-09-17): PayDots on the page (article column,
// 680px; {p, scope?}; null under two priced dots), PayTimeline in the section's
// Read more sheet ({p, scope?}; null under three dated contracts or tenders, or
// all in one month). Rationale at the top of pay.tsx.
export { PayDots, PayTimeline } from "./pay";
export type { ProcessField, ProcessStep, ProcessKnown, ProcessChange } from "./types";
