// /lab/parts/figures/kit — the record-page figure kit. Import from here:
//
//   import { ProcessToday, ProcessAfter, FieldTimeline, FieldGrid, CompMap, MoneyScale }
//     from "../../../../figures/kit";   // from web/app/lab/modern/[region]/[id]/page.tsx
//
// Every component is a plain server function: no hooks, no client code. Each
// returns `null` when its data is too thin, so CALL it before the JSX and test
// the result before drawing any heading or wrapper around it:
//
//   const fieldFig = FieldTimeline({ p });
//   …
//   {fieldFig}
//
// Slots and widths (the lab record page's own --ls-main / --ls-rail):
//   ProcessToday   article column 680px   right after The problem prose
//   ProcessAfter   ~630px                 INSIDE the Suggested solution box,
//                                          under the solution sentence
//   FieldTimeline  article column 680px   head of Local competition
//   CompMap        article column 680px   Proven abroad
//   MoneyScale     article column 680px   Who pays
//   FieldGrid      rail 272px             under the Opportunity card
export { ProcessToday, ProcessAfter, reentryTally } from "./process";
export { FieldTimeline, FieldGrid } from "./field";
export { CompMap, compNextDoor } from "./comp-map";
export { MoneyScale, moneyDots } from "./money";
export type { ProcessField, ProcessStep, ProcessKnown, ProcessChange } from "./types";
