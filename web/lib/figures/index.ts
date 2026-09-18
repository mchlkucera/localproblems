// lib/figures — the record-page figure kit. Import by name from here:
//
//   import { ProcessSteps, MaturityDot, LocalMatrix, CompMap, PayDots, PayTimeline }
//     from "../../../../../lib/figures";   // from web/app/(site)/problem/[region]/[id]/page.tsx
//
// Every component is a plain server function: no hooks, no client code. Each
// returns `null` when its data is too thin, so CALL it before the JSX and test
// the result before drawing any heading or wrapper around it:
//
//   const stepsFig = ProcessSteps({ process: p.process, sources: p.sources, ctx });
//   …
//   {stepsFig && <div className="ls-fig">{stepsFig}</div>}
//
// The slots on the record page (skills/design-language/SKILL.md §7):
//   ProcessSteps   article column 680px   Suggested solution: THE HUB (owner,
//                                          2026-09-18). Today, each person
//                                          wired to their own place; with the
//                                          solution, everyone wired into ONE
//                                          teal box. Two stacked blocks at
//                                          every width; role and object glyphs
//                                          from role-icons.tsx. Props {process,
//                                          sources, ctx}; null under 2 drawable
//                                          steps
//   MaturityDot    inline, 10px           each company row, so figures and rows match
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
export { ProcessSteps } from "./process";
export { MaturityDot, DotPeek, type Maturity } from "./field";
export { CompMap, compNextDoor } from "./comp-map";
export { LocalMatrix } from "./matrix";
// Willing to pay (owner, 2026-09-17): PayDots on the page (article column,
// 680px; {p, scope?}; null under two priced dots), PayTimeline in the section's
// Read more sheet ({p, scope?}; null under three dated contracts or tenders, or
// all in one month). Rationale at the top of pay.tsx.
export { PayDots, PayTimeline } from "./pay";
export type { ProcessField, ProcessStep, ProcessKnown, ProcessChange } from "./types";
