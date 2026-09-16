// /lab/parts/figures — data coverage for each figure option, MEASURED AT RENDER from
// the same loaders the record page reads (getProblems, dimRefs, priceReceipts,
// the figure components' own selectors), so the numbers on the review page
// cannot drift from the data. The two hand counts (process shape, multi-part
// solutions) are imported from hand.ts and labelled as hand counts wherever
// they print.
import { getProblems, type Problem } from "../../../../lib/data";
import { dimRefs } from "../../../../lib/scorecard";
import { splitBody } from "../../../../lib/sections";
import { moneyDots } from "./fig-money";
import { windowItems } from "./fig-window";
import { proofNear } from "./fig-map";
import { MULTI_PART, PROCESS_SHAPE } from "./hand";

/** A size-shaped number in a sentence: grouped thousands, a 3+ digit count,
    a percentage or a spelled-out magnitude. Years and [Sn] markers are
    stripped first. A PROXY for "a size figure could be picked here". */
const SIZE_RE = /\b\d{1,3}(?:,\d{3})+\b|\b\d{3,}\b|\b\d+(?:\.\d+)?\s?(?:%|percent)|\b(?:hundreds?|thousands?|millions?|billions?|bn)\b|\b(?:[Tt]hree|[Ff]our|[Ff]ive|[Ss]ix|[Ss]even|[Ee]ight|[Nn]ine|[Tt]en|[Ee]leven|[Tt]welve|[Tt]wenty|[Ff]ifty)\s+(?:Czech\s+)?(?:firms|companies|workers|hospitals|towns|people|crypto)\b/i;
const hasSize = (s: string) => SIZE_RE.test(s.replace(/\[S[\d,\s]+\]/g, "").replace(/\b(?:19|20)\d{2}\b/g, ""));

export function coverage() {
  const live = getProblems().filter((p) => p.status !== "rejected");
  const n = (f: (p: Problem) => boolean) => live.filter(f).length;
  const comps = (p: Problem) => p.comps ?? [];
  const locals = (p: Problem) => p.locals ?? [];
  const allComps = live.flatMap(comps);
  const allLocals = live.flatMap(locals);
  const money = live.map((p) => ({ p, ...moneyDots(p) }));
  const win = live.map((p) => ({ p, ...windowItems(p) }));
  return {
    N: live.length,
    flow: {
      field: n((p) => "solution_flow" in p),
      strong: PROCESS_SHAPE.strong.length,
      moderate: PROCESS_SHAPE.moderate.length,
      consolidation: PROCESS_SHAPE.consolidation.length,
      none: PROCESS_SHAPE.none.length,
    },
    parts: { field: n((p) => "solution_parts" in p), multi: MULTI_PART.length },
    field: {
      any: n((p) => comps(p).length + locals(p).length > 0),
      both: n((p) => comps(p).length > 0 && locals(p).length > 0),
      locals: allLocals.length,
      localsNoYear: allLocals.filter((l) => l.since === undefined).length,
      comps: allComps.length,
      withLocals: n((p) => locals(p).length > 0),
    },
    map: {
      comps: n((p) => comps(p).length > 0),
      markets: n((p) => comps(p).some((c) => (c.markets ?? []).length > 0)),
      near: n((p) => comps(p).length > 0 && proofNear(p)),
      de: allComps.filter((c) => c.geo === "DE").length,
      us: allComps.filter((c) => c.geo === "US").length,
    },
    money: {
      price: n((p) => p.sources.some((s) => s.type === "price")),
      any: money.filter((m) => m.pay.length + m.pub.length > 0).length,
      two: money.filter((m) => m.pay.length + m.pub.length >= 2).length,
      dupes: money.filter((m) => m.merged.length > 0).length,
      noAmount: money.filter((m) => m.noAmount.length > 0).length,
    },
    window: {
      any: win.filter((w) => w.items.length > 0).length,
      two: win.filter((w) => w.items.length >= 2).length,
      // what the lab page's "Dates on file" list shows: a future date on a
      // source that backs Why now
      urgency: win.filter((w) => w.p.scores.urgency > 0 && dimRefs(w.p).urgency.some((n) => w.items.some((it) => it.n === n))).length,
      footed: win.filter((w) => w.items.some((it) => it.foot)).length,
      refused: win.filter((w) => w.refused.length > 0).length,
    },
    size: {
      lead: n((p) => hasSize(p.body.split(/\n{2,}/)[0] ?? "")),
      title: n((p) => hasSize(p.title)),
    },
    chain: { whoPays: n((p) => splitBody(p.body).dek !== "") },
  };
}
export type Coverage = ReturnType<typeof coverage>;
