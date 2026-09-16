// /lab/parts/figures — REVIEW PAGE: one figure per record page, the options.
// The owner (2026-09-15): "A map? Image? Illustration? Graph? … It must add
// some content value to what's there, like in a scientific paper presenting
// something crucial. Present me options, let me make judgement. Maybe we could
// somehow illustrate the suggested solution?"
//
// Every option is drawn for real records from real data. Options A, B, G and H
// need content no record carries yet; their mock content is hand-extracted in
// ./hand.ts and labelled as such on the page. Coverage figures are measured at
// render (./coverage.ts). LOCAL ONLY: the /lab layout 404s without
// LP_ADMIN=1, and this page checks again. Writes nothing.
import type { Metadata } from "next";
import type { ReactNode } from "react";
import { notFound } from "next/navigation";
import { extractDate, getProblems, type Problem } from "../../../../lib/data";
import { ENTRY_LEVEL_LABELS } from "../../../../lib/format";
import { cite, newCtx, type CiteCtx } from "../../modern/cite";
import { labSources } from "../../modern/sources";
import { PeekHover } from "../../modern/peek-hover";
import { coverage, type Coverage } from "./coverage";
import { CHAINS, FLOWS, PARTS, SIZES } from "./hand";
import { FlowFig } from "./fig-flow";
import { PartsFig } from "./fig-parts";
import { FieldStrip, RoomMatrix } from "./fig-field";
import { ProofDistance, WhereMap } from "./fig-map";
import { MoneyScale } from "./fig-money";
import { WindowLine } from "./fig-window";
import { SizeFig } from "./fig-size";
import { ChainFig } from "./fig-chain";
import { dayLabel } from "./kit/text";
import "../../modern/problem.css";
import "./figures.css";

export const metadata: Metadata = { title: "Figure options (lab) — localproblems.org" };

const MAIN = ["p-0036", "p-0008", "p-0010"];
const GAP_WORD = ["taken", "contested", "open"];

type Panel = { id: string; node: ReactNode; note: string; hand?: string };
type Option = {
  key: string;
  rank: number;
  title: string;
  slot: string;
  slotKind: "main" | "rail";
  colour: string;
  what: string;
  why: ReactNode;
  coverage: ReactNode;
  covShort: string;
  needs: ReactNode;
  needsShort: string;
  risks: ReactNode;
  rec: string;
  recShort: string;
  panels: Panel[];
  variant?: { title: string; slot: string; slotKind: "main" | "rail"; note: string; panels: Panel[] };
};

function FigFrame({ p, panel, kind, label }: { p: Problem; panel: Panel; kind: "main" | "rail"; label: string }) {
  return (
    <figure className={`fg-fig fg-fig--${kind}`}>
      <header className="fg-fig-hd">
        <span className="fg-fig-id">{p.id.toUpperCase()}</span>
        <span className="fg-fig-t" title={p.title}>{p.title}</span>
      </header>
      <div className="fg-fig-body">{panel.node}</div>
      <figcaption className="fg-fig-cap">
        <span className="fg-fig-n">{label}</span> {panel.note}
        {panel.hand && <span className="fg-hand">Hand-extracted for the mock; production needs field <code>{panel.hand}</code>.</span>}
      </figcaption>
    </figure>
  );
}

export default function FiguresPage() {
  if (process.env.LP_ADMIN !== "1") notFound();

  const all = getProblems();
  const rec = (id: string) => {
    const p = all.find((x) => x.id === id);
    if (!p) throw new Error(`/lab/parts/figures: record ${id} not found`);
    return p;
  };
  const today = extractDate();
  const cov: Coverage = coverage();
  const N = cov.N;

  // One citation context per record, sharing ONE counter so every pill's
  // popover id is unique across the whole page.
  const seq = { n: 0 };
  const ctxs = new Map<string, CiteCtx>();
  const citer = (p: Problem) => (nums: number[]) => {
    let c = ctxs.get(p.id);
    if (!c) { c = { ...newCtx(labSources(p)), seq }; ctxs.set(p.id, c); }
    return nums.length ? cite(nums, c) : null;
  };

  const flowOf = (id: string) => FLOWS.find((f) => f.id === id)!;
  const partsOf = (id: string) => PARTS.find((f) => f.id === id)!;
  const sizeOf = (id: string) => SIZES.find((f) => f.id === id)!;
  const chainOf = (id: string) => CHAINS.find((f) => f.id === id)!;
  const of = (n: number) => `${n} of ${N}`;

  const options: Option[] = [
    {
      key: "a", rank: 1,
      title: "The suggested solution, before and after",
      slot: "Article column, 680px, directly under the Suggested solution box",
      slotKind: "main",
      colour: "Teal (in the builder’s favour) marks the bottom row: what the suggested solution would take over. Dashed, because it is a proposal, not evidence.",
      what: "Today’s process as the problem prose describes it, step by step with its sources, and what the suggested solution does to each step: which re-reading or re-typing goes, which step stays, which is new.",
      why: <>The prose states the process in one sentence and the solution in another, and leaves the reader to map one onto the other. The figure does the mapping, and makes the solution’s claim checkable step by step. p-0010 shows the honesty it forces: the phone call stays, because the suggested solution does not take it.</>,
      coverage: <>
        <b>{of(cov.flow.field)}</b> records carry the data today. By hand, reading every lead paragraph: <b>{cov.flow.strong + cov.flow.moderate}</b> of {N} describe a process ({cov.flow.strong} clearly, {cov.flow.moderate} partly), and <b>{cov.flow.consolidation}</b> more are “every buyer buys alone” and fit the consolidation shape drawn for p-0008. The other <b>{cov.flow.none}</b> describe a new obligation or a decision with no process today; a before row there would be invented.
      </>,
      covShort: `0 of ${N} now; ~${cov.flow.strong + cov.flow.moderate + cov.flow.consolidation} of ${N} could have it`,
      needs: <>A new authored field, <code>solution_flow</code>: steps of <code>{"{who, today, cites, after, change}"}</code>. Invariants for <code>check-records.py</code>: every today step cites; an after step carries no citation except for a dated fact inside it; the tally is derived, never written; an absent key means no figure. About 20–30 minutes per record. <b>It cannot be generated from the prose reliably:</b> the prose names steps without their boundaries, the actor is often implicit (“someone re-typing”), and the after-state is one sentence for the whole process. A model could draft the field, but the draft needs the same review as any claim.</>,
      needsShort: "New authored field solution_flow",
      risks: <>The after row is a proposal and must never read as evidence: dashed, teal, uncited, labelled. Step boundaries are editorial; splitting one step into three inflates the change. Some process sentences carry no citation (p-0033’s “Providers cover the holes with overtime, agency staff and word of mouth” has none), so the invariant would block them, correctly.</>,
      rec: "Recommended where a record has a process. It answers the owner’s question most directly and adds the most. It needs the field, and it cannot appear on all records.",
      recShort: "Yes, with a new field; on about half the records",
      panels: MAIN.map((id) => ({
        id,
        node: <FlowFig flow={flowOf(id)} cite={citer(rec(id))} />,
        note: `${flowOf(id).shape === "consolidation" ? "Consolidation shape: the steps stay, the sellers merge." : "Re-entry shape: the steps stay, the re-reading goes."} Top row from ${flowOf(id).extractedFrom}.`,
        hand: "solution_flow",
      })),
    },
    {
      key: "c", rank: 2,
      title: "The field, by the year each player started",
      slot: "Article column, 680px, at the head of Local competition (it bridges Proven abroad and Local competition)",
      slotKind: "main",
      colour: "None, except teal when nobody on file sells this here (the builder’s favour). Ink dots are Czech players: filled means established, hollow means early, and faint means it sells something else. Gray dots are abroad.",
      what: "Every comparable abroad and every Czech player on one year axis: how long abroad has been selling, how new the Czech sellers are, which of them are established, and who is nearby selling something else.",
      why: <>Proof and gap both turn on maturity, and the strip shows the age gap at a glance. On p-0036 the comparables abroad have sold for a median of 11 years and the Czech sellers for 0. On p-0010 it shows why gap is 0: TruckManager has sold this since 2007. On p-0033 it shows why gap is 2: the “sells this” lane is empty.</>,
      coverage: <><b>{of(cov.field.any)}</b> records have at least one player; {of(cov.field.both)} have players both abroad and at home. {cov.field.localsNoYear} of {cov.field.locals} Czech players publish no year and sit in a gutter, never at a guessed position. The {cov.field.comps} comparables carry no maturity field, so all of them are drawn alike.</>,
      covShort: `${cov.field.any} of ${N}`,
      needs: <>Nothing new. It reads <code>comps[].since</code>, <code>locals[].since</code>, <code>competes</code> and <code>maturity</code>. One optional data fix (see risks).</>,
      needsShort: "Nothing",
      risks: <><code>locals[].since</code> means “the year it started selling this, <i>else</i> its founding year”: one field, two meanings (rule 1). ICZ sits at 2023, the year of its product, though the firm has traded since 1997, while ID Berlin sits at 1985, the company’s founding. A start year is not traction. A figure that puts 11 Czech names on a line can read as “crowded” even when every one sells something else (p-0033).</>,
      rec: "Recommended as the default. It covers every record, ships with no new data, and shows the two scores the rail can only state.",
      recShort: "Yes. The default everywhere, no new data",
      panels: [...MAIN, "p-0033"].map((id) => ({
        id,
        node: <FieldStrip p={rec(id)} today={today} />,
        note: "Drawn from comps[] and locals[]; nothing authored. Position is the year selling began (or founding year); height within a lane means nothing.",
      })),
      variant: {
        title: "Rail variant: who is in the room",
        slot: "Rail, 272px, under the Opportunity card",
        slotKind: "rail",
        note: "The gap rule drawn as a 2×2: does it sell this × how proven. Only the top-right cell takes the space. It restates the ledger rather than adding to it; compact, but it adds less than the strip.",
        panels: [...MAIN, "p-0033"].map((id) => ({ id, node: <RoomMatrix p={rec(id)} />, note: "Drawn from locals[] competes × maturity." })),
      },
    },
    {
      key: "b", rank: 3,
      title: "The suggested solution, in parts: who already sells each",
      slot: "Article column, 680px, under the Suggested solution box or at the head of Local competition",
      slotKind: "main",
      colour: "Teal (in the builder’s favour) marks the parts the Czech market check found nobody selling: where the suggested solution has room.",
      what: "The suggested solution split into its parts. For each part: who sells it abroad, who sells it here and how mature they are, and whether the Czech market check found anyone.",
      why: <>The gap score is one number for the whole record; this shows <i>which part</i> is taken and which is open. p-0010 scores “taken” (gap 0), yet two of its four parts are open, which is exactly why its solution was narrowed. p-0036’s first move, “build the report, not the coder”, becomes visible as a teal row above a contested one.</>,
      coverage: <><b>{of(cov.parts.field)}</b> records carry the mapping. By hand, <b>{cov.parts.multi}</b> of {N} solution sentences split into two or more parts.</>,
      covShort: `0 of ${N} now; ${cov.parts.multi} of ${N} could have it`,
      needs: <>A new authored field, <code>solution_parts</code>: <code>{"{part, abroad[], here[], verdict, cites}"}</code>, with every name resolving to a <code>comps[]</code> or <code>locals[]</code> entry. p-0008’s two sellers, Institut kybernetické bezpečnosti and enovation, are not on the ledger; they would have to join <code>locals[]</code> first. An “open” verdict must cite a gap-check that ran a positive control. About 30–45 minutes per record.</>,
      needsShort: "New authored field solution_parts",
      risks: <>Per-part absence claims are the riskiest thing on this page. Gap authority is asymmetric, and a part can be carved narrowly enough to manufacture an open cell. Verdicts are judgment calls: whether Medicalc’s AI structuring counts as “templates” is an editor’s decision, not a fact.</>,
      rec: "Strongest insight for a builder, and the costliest to author honestly. Worth it for the top-scoring records if the owner accepts per-part verdicts as a new kind of claim.",
      recShort: "Maybe: top records only",
      panels: MAIN.map((id) => ({
        id,
        node: <PartsFig parts={partsOf(id).parts} cite={citer(rec(id))} />,
        note: `Parts from ${partsOf(id).extractedFrom}.`,
        hand: "solution_parts",
      })),
    },
    {
      key: "e", rank: 4,
      title: "The money, on one scale",
      slot: "Article column, 680px, in Who pays, above the two receipt lists",
      slotKind: "main",
      colour: "None. Gray only: dark dots are one buyer’s price, gray dots are public awards, hollow squares are shared pots.",
      what: "What one buyer pays (price receipts) and the public money nearby (awards, contracts, grant pots), on one logarithmic CZK axis.",
      why: <>The prose lists figures that differ by orders of magnitude, and a list hides the spread. On p-0008 the same obligation is bought for 3,000 CZK a month, 91,000 once, 9M for a whole town, next to a €99.6M pot. The spread is the market’s segmentation.</>,
      coverage: <><b>{of(cov.money.any)}</b> records have at least one figure; <b>{of(cov.money.two)}</b> have two or more (one dot is not a chart). p-0036 has none: its open 1.14bn CZK grant is stated in prose, with no structured amount. {cov.money.dupes} records carry a price receipt drawn from the same document as a money source, which would be drawn twice without the dedupe built here. {cov.money.noAmount} records have a Money-nearby source with no readable amount.</>,
      covShort: `${cov.money.any} of ${N}; ${cov.money.two} with 2+ figures`,
      needs: <>The dedupe rule (same url, drawn once; built here). An amount on money sources whose signal has none (p-0036’s IROP 79), for example <code>amount_czk</code> allowed on subsidy sources. That breaks today’s rule that price fields are forbidden off a price source, so it would be a new field name.</>,
      needsShort: "Dedupe rule; amounts on grant sources",
      risks: <>Units differ: a month, a one-off, a year, a pot shared by hundreds. The figure never sums or normalises them. Log scales understate differences to a lay reader. 25 CZK/EUR is flat. Without the dedupe the same money appears twice (p-0008 S6/S24, S7/S23; p-0033 S4/S12). One field reads wrong: a grant call’s signal says <code>source: hlidac</code>, the mirror it came through, so only its <code>dotace-</code> id prefix marks it as a pot. That is rule 1 again.</>,
      rec: `Good where a record has two or more figures (${of(cov.money.two)}). Ship only with the dedupe, and hide it below two marks.`,
      recShort: `Yes, on ${cov.money.two} records; hide below 2 marks`,
      panels: [...MAIN, "p-0033"].map((id) => ({
        id,
        node: <MoneyScale p={rec(id)} />,
        note: "Drawn from price receipts and the signals behind Money nearby; nothing authored.",
      })),
    },
    {
      key: "f", rank: 5,
      title: "The window: dated triggers against today",
      slot: "Article column, 680px, in Why now, replacing the “Dates on file” list",
      slotKind: "main",
      colour: `Warm (time pressure) marks the run from today (the register’s extract date, ${dayLabel(today)}) to the first date, but only when it is under six months, the record page’s own rule. Otherwise gray.`,
      what: "The future deadlines on file, rules and money, on a time axis from today, with the stretch to the first one.",
      why: <>Sequence matters, and the prose scatters dates across three sections. On p-0008 the grant call closes on 17 Dec 2026, two weeks before the law’s measures fall due, so the order to sell in is application first. On p-0036 there is a four-year gap between the grant and the European deadline.</>,
      coverage: <><b>{of(cov.window.any)}</b> records have a future-dated rule, grant or tender (the brief’s 16); {of(cov.window.urgency)} already list one under “Dates on file” on the lab page, whose Why now sources include the freshest one; only <b>{of(cov.window.two)}</b> have two or more dates, and a timeline of one dot is thin. {cov.window.footed} records have a drawn date whose record and signal disagree (footnoted automatically).</>,
      covShort: `${cov.window.any} of ${N}; ${cov.window.two} with 2+ dates`,
      needs: <>A field saying what a date <i>is</i>, e.g. <code>{"deadline: {date, kind: in-force | due | opens | closes}"}</code>. Today the date on a source means different things. p-0010’s grant is dated the day it opens on the record and the day it closes on its signal. p-0008’s complaint carries the law’s deadline as its own date.</>,
      needsShort: "A deadline-kind field",
      risks: <>Past dates are unsafe (the audit found 77% are ingest dates), so they are listed, never plotted. Approximate deadlines (p-0008 S1, “most deadlines land Q4 2026–H1 2027”) are drawn as sharp points. The figure is only as good as the source dates, and those have the known ambiguity.</>,
      rec: "Useful, but only after the deadline-kind field exists; until then the footnotes do the work the data should.",
      recShort: "Later, after a deadline-kind field",
      panels: MAIN.map((id) => ({
        id,
        node: <WindowLine p={rec(id)} />,
        note: "Drawn from future-dated regulation, subsidy and tender sources; footnotes generated from the data.",
      })),
    },
    {
      key: "g", rank: 6,
      title: "The size of the problem, as one number",
      slot: "Rail, 272px, above the Opportunity card (or the top of The problem)",
      slotKind: "rail",
      colour: "None. The dark fill is the part of the whole the source states.",
      what: "The one number that sizes the problem, with a part of the whole where the sources give one.",
      why: <>Titles already lead with a number in {cov.size.title} of {N}; the number is the hook. With its part (4,825 of about 6,000 registered) it becomes a finding.</>,
      coverage: <><b>{of(cov.size.lead)}</b> records have a size-shaped number in their lead paragraph (a regex proxy); {of(cov.size.title)} in the title; 0 of {N} have a field.</>,
      covShort: `0 of ${N} now; ~${cov.size.lead} of ${N} could`,
      needs: <>A new authored field, <code>size</code>: <code>{"{figure, counts, cites, part?}"}</code>, with an invariant that part and whole come from one source or render flagged.</>,
      needsShort: "New authored field size",
      risks: <>The pull toward the most dramatic number. Ratios across sources: p-0010’s 700 TruckManager firms over 40,000 hauliers is two sources and two populations, flagged on the figure. “3×” counts steps; it does not measure anything.</>,
      rec: "A good lead, weak discipline. Only with the same-source invariant.",
      recShort: "Maybe, with a same-source rule",
      panels: [...MAIN, "p-0033"].map((id) => ({
        id,
        node: <SizeFig s={sizeOf(id)} cite={citer(rec(id))} />,
        note: "From the lead paragraph’s own figures.",
        hand: "size",
      })),
    },
    {
      key: "h", rank: 7,
      title: "Who pays whom",
      slot: "Article column, 680px, in Who pays",
      slotKind: "main",
      colour: "Teal (in the builder’s favour) marks the suggested solution’s place in the chain, dashed.",
      what: "Where the money comes from, who buys, who is paid today, and which pocket the suggested solution’s revenue would come out of.",
      why: <>“Who pays” is the section the record states least structurally. A chain shows a grant’s role (p-0008: IROP pays half) and the pocket the solution competes for (p-0033: the agency’s cut).</>,
      coverage: <><b>{of(cov.chain.whoPays)}</b> records have a Who pays paragraph to extract from; 0 of {N} have structured flows.</>,
      covShort: `0 of ${N} now; ${cov.chain.whoPays} of ${N} could`,
      needs: <>A new authored field, <code>money_flow</code>, with every node citing or rendering flagged.</>,
      needsShort: "New authored field money_flow",
      risks: <>p-0033’s two central sentences, “money already going to agencies” and “overtime, agency staff and word of mouth”, carry no citation, so the figure would promote uncited prose into a diagram (flagged here). It overlaps A (the process) and E (the amounts).</>,
      rec: "Not as its own figure. Its best parts belong in A and E.",
      recShort: "No: fold into A and E",
      panels: ["p-0036", "p-0008", "p-0033"].map((id) => ({
        id,
        node: <ChainFig c={chainOf(id)} cite={citer(rec(id))} />,
        note: `From ${chainOf(id).extractedFrom}.`,
        hand: "money_flow",
      })),
    },
    {
      key: "d", rank: 8,
      title: "Where it already works",
      slot: "D1: article column in Proven abroad, 448px (as production has it). D2: rail, 272px",
      slotKind: "main",
      colour: "None. Czechia is outlined in ink; gray fills are HQs and sourced markets.",
      what: "D1: the comparables’ HQs and sourced markets on the production map, restyled. D2: how close the proof is, in the PROOF ladder’s own bands.",
      why: <>The one geographic fact a Czech builder needs is whether it is proven next door, and the ladder’s rung 3 turns on exactly that. D2 says it in one line; D1 spends a map on it.</>,
      coverage: <><b>{of(cov.map.comps)}</b> records have comparables; {of(cov.map.markets)} record any market beyond the HQ; {of(cov.map.near)} have a comparable next door (HQ or sourced market in the ladder’s CEE-adjacent set). Of the {cov.field.comps} comparables, {cov.map.de} are German and {cov.map.us} American, so most maps shade Germany and an inset.</>,
      covShort: `${cov.map.comps} of ${N}`,
      needs: <>Nothing; D1 exists in production.</>,
      needsShort: "Nothing",
      risks: <>Maps weight by land area. An HQ is not where a company sells. Markets are recorded only when sourced, so an unshaded country means “unknown”, not “absent”. Low information for the space it takes. D2 has a sharper trap: <code>comps[]</code> does not record whether a comparable sells <i>this</i>. p-0010’s German comparable, cargo.one, sells air-cargo booking to forwarders, which is why that record’s proof is 2, not 3. So D2 can say “a comparable next door”, never “proven next door”.</>,
      rec: "Keep it off the lab page. If geography must show, use D2 in the rail.",
      recShort: "No; D2 if anything",
      panels: MAIN.map((id) => ({ id, node: <WhereMap p={rec(id)} />, note: "D1, drawn from comps[] geo and markets by the production component." })),
      variant: {
        title: "D2: how close is the proof",
        slot: "Rail, 272px",
        slotKind: "rail",
        note: "Bands are SCORING.md’s own: rung 3 needs a market “CEE-adjacent (DE/AT/PL/Nordics/Baltics/SI/SK/HU)”.",
        panels: [...MAIN, "p-0033"].map((id) => ({ id, node: <ProofDistance p={rec(id)} />, note: "Drawn from comps[]." })),
      },
    },
  ];

  const ranked = [...options].sort((a, b) => a.rank - b.rank);
  const letter = (o: Option) => o.key.toUpperCase();

  return (
    // `ls` as well as `lab`: the record page's round-3 colour tokens (and its
    // citation pills) are scoped to `.ls`, and the figures borrow them.
    <div className="lab ls fg">
      <header className="fg-bar">
        <nav className="ls-crumbs" aria-label="Breadcrumb">
          <a href="/lab/modern">Lab</a><span className="ls-sep" aria-hidden="true">/</span><span className="ls-crumb-id">Figures</span>
        </nav>
      </header>

      <main className="fg-sheet">
        <header className="fg-intro">
          <p className="fg-kicker">Review page · local only · not linked from anywhere</p>
          <h1 className="fg-h1">One figure per record: the options</h1>
          <p className="fg-lede">
            The brief: one visual on each record page that breaks the text and adds content, “like in a scientific paper presenting something crucial”, and perhaps an illustration of the suggested solution.
            Below are eight options, each drawn from real record data for p-0036, p-0008 and p-0010 (p-0033 where it shows a different shape), at the width of the slot it would take.
            They are ranked by my recommendation. The judgment is yours.
          </p>
          <dl className="fg-meta">
            <div><dt>Measured against</dt><dd>{N} live records (rejected excluded)</dd></div>
            <div><dt>Today, on every figure</dt><dd>{dayLabel(today)}, the register’s extract date, never the wall clock</dd></div>
            <div><dt>Hand-extracted content</dt><dd>Options A, B, G, H, labelled on every figure</dd></div>
          </dl>
          <div className="fg-legend">
            <p className="fg-legend-h">No new colours: the figures borrow the record page’s own</p>
            <p><span className="fg-chip fg-chip--sol" /> <b>Teal: in the builder’s favour</b>, as on the Opportunity pips. Here it marks what the suggested solution would take over (dashed, because it is a proposal and never cited as evidence) and a part of the market nobody here sells.</p>
            <p><span className="fg-chip fg-chip--soon" /> <b>Warm: time pressure</b>, as on the header’s Window fact. Here it is used only for a deadline under six months.</p>
            <p><span className="fg-chip fg-chip--ink" /> <b>Blue: a source you can open.</b> It stays reserved for the pills, which are the record page’s own and peek into the source on hover.</p>
            <p className="fg-legend-n">These tokens are being restyled in parallel on the record page. The figures read them rather than copy them, so a change there carries through. Everything else is the lab gray ramp.</p>
          </div>
        </header>

        <section className="fg-rank" aria-labelledby="fg-rank-h">
          <h2 id="fg-rank-h" className="fg-h2">Ranked</h2>
          <div className="fg-table-wrap">
            <table className="fg-table">
              <thead>
                <tr><th>#</th><th>Option</th><th>What it shows</th><th>Coverage</th><th>Needs</th><th>Recommendation</th></tr>
              </thead>
              <tbody>
                {ranked.map((o) => (
                  <tr key={o.key}>
                    <td className="fg-td-n">{o.rank}</td>
                    <td><a className="fg-td-opt" href={`#opt-${o.key}`}><span className="fg-letter">{letter(o)}</span>{o.title}</a></td>
                    <td className="fg-td-what">{o.what}</td>
                    <td className="fg-td-cov">{o.covShort}</td>
                    <td>{o.needsShort}</td>
                    <td className="fg-td-rec">{o.recShort}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        {ranked.map((o) => (
          <section key={o.key} id={`opt-${o.key}`} className="fg-opt" aria-labelledby={`opt-${o.key}-h`}>
            <header className="fg-opt-hd">
              <span className="fg-opt-rank">#{o.rank}</span>
              <h2 id={`opt-${o.key}-h`} className="fg-h2"><span className="fg-letter fg-letter--lg">{letter(o)}</span>{o.title}</h2>
            </header>
            <div className="fg-cap">
              <dl className="fg-cap-dl">
                <div><dt>What it shows</dt><dd>{o.what}</dd></div>
                <div><dt>Why it matters</dt><dd>{o.why}</dd></div>
                <div><dt>Coverage</dt><dd>{o.coverage}</dd></div>
                <div><dt>What it needs</dt><dd>{o.needs}</dd></div>
                <div><dt>Honesty risks</dt><dd>{o.risks}</dd></div>
              </dl>
              <aside className="fg-cap-side">
                <p className="fg-side-k">Slot</p><p className="fg-side-v">{o.slot}</p>
                <p className="fg-side-k">Colour</p><p className="fg-side-v">{o.colour}</p>
                <p className="fg-side-k">Recommendation</p><p className="fg-side-v fg-side-rec">{o.rec}</p>
              </aside>
            </div>
            <div className={`fg-grid fg-grid--${o.slotKind}`}>
              {o.panels.map((panel, i) => (
                <FigFrame key={panel.id} p={rec(panel.id)} panel={panel} kind={o.slotKind} label={`Fig. ${letter(o)}${i + 1}`} />
              ))}
            </div>
            {o.variant && (
              <div className="fg-variant">
                <h3 className="fg-h3">{o.variant.title} <span className="fg-h3-slot">{o.variant.slot}</span></h3>
                <p className="fg-variant-n">{o.variant.note}</p>
                <div className={`fg-grid fg-grid--${o.variant.slotKind}`}>
                  {o.variant.panels.map((panel, i) => (
                    <FigFrame key={panel.id} p={rec(panel.id)} panel={panel} kind={o.variant!.slotKind} label={`Fig. ${letter(o)}′${i + 1}`} />
                  ))}
                </div>
              </div>
            )}
          </section>
        ))}

        <section className="fg-opt fg-rejected" aria-labelledby="fg-rej-h">
          <h2 id="fg-rej-h" className="fg-h2">Considered and not drawn</h2>
          <ul className="fg-ul">
            <li><b>A timeline or trend of the record’s own source dates.</b> The earlier audit found 77% of source dates are the day the register ingested them, not a market event; it would chart our reading habits.</li>
            <li><b>Google Trends.</b> Rejected in the audit: not evidence, and thin for Czech B2B terms.</li>
            <li><b>A score radar.</b> Restates the Opportunity card, and radar areas exaggerate differences.</li>
            <li><b>Photographs or generated images.</b> No content value; the category drawing already carries the decorative role.</li>
            <li><b>Evidence-type bars.</b> Already in the rail’s Evidence card.</li>
          </ul>
        </section>

        <section className="fg-opt fg-decide" aria-labelledby="fg-dec-h">
          <h2 id="fg-dec-h" className="fg-h2">Decisions for the owner</h2>
          <ol className="fg-ol">
            <li><b>Does the likely-solution illustration get a new authored field?</b> It cannot be generated from the prose reliably. If yes: <code>solution_flow</code> with the invariants under A, authored first for the {cov.flow.strong + cov.flow.moderate} process-shaped records. If no, drop A and B and use C.</li>
            <li><b>One figure type everywhere, or the best figure per record?</b> Consistency says C on every page. Content says A where a process exists and C elsewhere, which needs a way to choose (the presence of <code>solution_flow</code> is enough).</li>
            <li><b>The slot.</b> A and B belong directly under the Suggested solution box. C belongs at the head of Local competition. Only G and the C and D variants fit the rail.</li>
            <li><b>Colour.</b> The figures add no hue of their own. They borrow the record page’s round-3 teal (in the builder’s favour) and warm (under six months), and leave blue to the source pills. The alternative is strictly gray, with the same meanings carried by dashes and fills.</li>
            <li><b>Split <code>locals[].since</code>?</b> It carries “started selling this” with a fallback to the founding year, one field with two meanings. C is honest only once they are two fields.</li>
            <li><b>Money:</b> adopt the same-url dedupe as a rule, and allow a structured amount on grant sources that have no signal amount (p-0036’s 1.14bn CZK call is invisible to any figure today).</li>
            <li><b>Dates:</b> add what a date <i>is</i> (in force, due, opens, closes) before any timeline ships; and decide whether p-0008 S2, a complaint dated at the law’s deadline, should keep that date.</li>
            <li><b>Per-part verdicts (B) and part-of-whole ratios (G)</b> are new kinds of claim. Allow them only with invariants: an “open” part cites a controlled gap-check; a ratio’s part and whole share one source or render flagged.</li>
          </ol>
          <p className="fg-foot-n">The earlier data audit (visual-ideas.md) was not on disk at the path given; its findings are used as quoted in the brief (77% ingest dates, Trends rejected, the field strip at 29 of 29).</p>
        </section>

        <section className="fg-records" aria-labelledby="fg-recs-h">
          <h2 id="fg-recs-h" className="fg-h3">Records drawn</h2>
          <ul className="fg-recs">
            {[...MAIN, "p-0033"].map((id) => {
              const p = rec(id);
              return (
                <li key={id}>
                  <a href={`/lab/modern/${p.region}/${p.id}`}>{p.id.toUpperCase()}</a>
                  <span>{p.title}</span>
                  <span className="fg-recs-m">{p.score}/12 · gap {GAP_WORD[p.scores.gap]} · {ENTRY_LEVEL_LABELS[p.entry.level].toLowerCase()} to enter</span>
                </li>
              );
            })}
          </ul>
        </section>
      </main>
      <PeekHover />
    </div>
  );
}
