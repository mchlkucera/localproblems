// /problem/[region]/[id] — the record page as a sources-first brief, in the
// modern design: one font, a gray ramp, hierarchy from size,
// weight and shade. Its signature is the citation: a quiet publisher pill in
// the sentence that PEEKS into the source (who, what, when, why, and the
// source's own words) without leaving the line. See lib/site/cite.tsx.
//
// Reads exactly what the production record page reads (getProblems, splitBody,
// dimRefs, getSignal, extractDate as "today"); writes nothing.
import type { Metadata } from "next";
import type { CSSProperties, ReactNode } from "react";
import { notFound } from "next/navigation";
import { extractDate, getProblems, getSignal, localHref, priceReceipts, signalHref, type PriceUnit, type Problem, type ProblemSource } from "../../../../../lib/data";
import { splitBody, splitLead, capitalize } from "../../../../../lib/sections";
import {
  ENTRY_BUYER_LABELS, ENTRY_INTEGRATION_LABELS, ENTRY_LEVEL_LABELS,
  ENTRY_MONEY_LABELS, ENTRY_PERMISSION_LABELS, PRICE_BASIS_LABELS,
  categoryLabel, countryName, czk, entryGates, euro,
} from "../../../../../lib/format";
import { dimRefs, type Dim } from "../../../../../lib/scorecard";
import { protoScores, protoTotal, type ProtoKey, type ProtoScore } from "../../../../../lib/site/score-proto";
import { EXT, ExtArrow, cite, newCtx, type CiteCtx } from "../../../../../lib/site/cite";
import { Prose, inline, type ProseOpts } from "../../../../../lib/site/prose";
import { fmtDate, labSources, typeNote, type LabSource } from "../../../../../lib/site/sources";
import { PeekHover } from "../../../../../lib/site/peek-hover";
import { CORRECTIONS_MAILTO } from "../../../../../lib/chrome";
import { CategoryArt } from "../../../../../lib/art/category-art";
// The figure kit, imported by name so every use is visible to grep and tsc.
import { CompMap, LocalMatrix, MaturityDot, PayDots, PayTimeline, ProcessSteps, type Maturity } from "../../../../../lib/figures";
import "../../../styles/kit.css";
import "../../../styles/problem.css";

/** The head's category drawing: the owner kept it, smaller (2026-09-16). */
const SHOW_HEAD_ART = true;

/** THE ONE DRILL-DOWN: THE SECTION SHEET (owner, 2026-09-16: "Easy to scan -
    read more into paper like modal with heading that presents"; "Make the
    without modal really short and scannable, all detail goes in the modal
    which is in-depth"). The page shows each section's outline; its "Read
    more" opens a sheet of paper holding the WHOLE section, the outline
    included. Native `popover="auto"` opened by `popovertarget`, so it works
    with every script stripped; Escape and an outside click close it. A
    section with nothing beyond its outline gets no sheet. There is no deep
    link: a closed popover cannot be opened from a URL without script. */
/** ABOUT THIS SECTION (owner, 2026-09-17: "Under Read more … there should be
    explanation about the section and why is it relevant for builders — should
    be below each read more of each section"). One constant map, the same copy
    on every record: what the section shows, why it matters to a builder, and
    for a scored section how its number reads. The wording simplifies DIM_INFO
    and the prototype words in lib/site/score-proto.ts; it restates their rungs
    and adds none. Willing to pay says plainly that its points still come from
    public money nearby (SCORING.md MONEY), not from a price paid. */
type About = { shows: string; why: string; score?: string };
const SECTION_ABOUT: Record<"opportunity" | "solution" | "why-now" | "willing-to-pay" | "validated-abroad" | "competition" | "execution-difficulty" | "first-moves", About> = {
  opportunity: {
    shows: "The problem as it is today: what goes wrong, and who it costs.",
    why: "Documented pain means you will not have to convince buyers the problem exists before you can sell them the fix.",
    score: "2/2 means clear, recurring pain: documented complaints, a petition or industry pressure. Scattered complaints make it 1/2.",
  },
  solution: {
    shows: "One way to solve the problem, and how the work would run with it.",
    why: "It is a starting point to test with buyers, not a plan. The sections below are the evidence for and against it.",
  },
  "why-now": {
    shows: "The dated rules and events that push buyers to act, soonest first.",
    why: "A dated rule turns “nice to have” into “must buy by”, and tells you how long the window stays open.",
    score: "A compliance date within 18 months gives 2 points, one further out 1, and evidence under 90 days old adds 1 more, up to 3/3.",
  },
  "willing-to-pay": {
    shows: "Who already spends money on this problem, how much, and how they buy.",
    why: "If people already pay for this, even by hand or through a consultant, you are replacing a spend, not creating a budget.",
    score: "2/2 means already paying. For now the points come from public money moving nearby, which shows a budget, not a buyer for this product.",
  },
  "validated-abroad": {
    shows: "Companies abroad that already sell a solution, and how far along they are.",
    why: "Established companies selling it in other markets show that buyers will pay, so you are not betting on an untested idea.",
    score: "3/3 means established in two or more markets, one of them near Czechia. 2/3 is one established company, 1/3 only early players.",
  },
  competition: {
    shows: "Czech companies that already sell this, and firms nearby that sell something else.",
    why: "A mature Czech seller means taking customers from an incumbent. Firms nearby still matter: the buyer may already pay them.",
    score: "More points mean less competition. 2/2 means no Czech company sells this, 1/2 only early ones do, 0/2 a mature one does.",
  },
  "execution-difficulty": {
    shows: "What stands between you and the first sale: who buys, what permission selling needs, what it must plug into, and whether it needs outside money.",
    why: "It tells you whether a small team can start selling soon, or needs a licence, a certification or funding first.",
    score: "More points mean easier to enter: 3/3 is easy, 0/3 very hard. It is not added to the Opportunity total, and competition does not count here.",
  },
  "first-moves": {
    shows: "A few concrete steps to start with.",
    why: "They are cheap ways to learn whether buyers will pay, before you build much.",
  },
};

function AboutSection({ about, id }: { about: About; id: string }) {
  return (
    <section className="ls-about" aria-labelledby={`${id}-about`}>
      <h3 className="ls-about-h" id={`${id}-about`}>About this section</h3>
      <dl className="ls-about-dl">
        <div><dt>What this shows</dt><dd>{about.shows}</dd></div>
        <div><dt>Why it matters to a builder</dt><dd>{about.why}</dd></div>
        {about.score && <div><dt>How to read the score</dt><dd>{about.score}</dd></div>}
      </dl>
    </section>
  );
}

function Sheet({ id, title, rec, about, children }: { id: string; title: string; rec: string; about: About; children: ReactNode }) {
  const sid = `sheet-${id}`;
  return (
    <>
      <button type="button" className="ls-readmore" popoverTarget={sid} aria-label={`Read more: ${title}`}>
        Read more
      </button>
      <div id={sid} popover="auto" role="dialog" aria-labelledby={`${sid}-h`} className="ls-sheet">
        <div className="ls-sheet-bar">
          <p className="ls-sheet-mini" aria-hidden="true">{title}</p>
          <button type="button" className="ls-x" popoverTarget={sid} popoverTargetAction="hide" aria-label="Close">×</button>
        </div>
        <div className="ls-sheet-page">
          <header className="ls-sheet-hd">
            <p className="ls-sheet-rec">{rec}</p>
            <h2 id={`${sid}-h`} className="ls-sheet-t">{title}</h2>
          </header>
          <AboutSection about={about} id={sid} />
          <div className="ls-sheet-body">{children}</div>
        </div>
      </div>
    </>
  );
}

/** THE PAGE CAP (owner, 2026-09-16: "the page never shows a list longer than
    3 items"). Page code only; the data is never trimmed. */
const PAGE_CAP = 3;
const LIST_LINE = /^(?:- |\d+\.\s)/;

/** A section's markdown → its outline for the page: the first sentence of
    the first paragraph (the answer line), then the first list after it,
    capped at PAGE_CAP items. `list` hands the list lines to a caller that
    picks its own rows (Why now); `more` says the sheet holds anything else. */
function outline(md: string): { answer: string; list: string[]; more: boolean; toMd: (rows: string[]) => string } {
  const blocks = md.split(/\n{2,}/)
    .map((b) => b.split("\n").map((l) => l.trim()).filter((l) => l && l !== "---"))
    .filter((b) => b.length);
  let answer = "";
  const toMd = (rows: string[]) => [answer, rows.join("\n")].filter(Boolean).join("\n\n");
  if (!blocks.length) return { answer, list: [], more: false, toMd };
  const b0 = blocks[0];
  let k = 0;
  const para: string[] = [];
  while (k < b0.length && !LIST_LINE.test(b0[k])) para.push(b0[k++]);
  const tail = b0.slice(k);
  let mixed = tail.some((l) => !LIST_LINE.test(l));
  let list = mixed ? tail.slice(0, tail.findIndex((l) => !LIST_LINE.test(l))) : tail;
  let used = 1;
  if (!list.length && !mixed && blocks[1]?.every((l) => LIST_LINE.test(l))) { list = blocks[1]; used = 2; }
  // Prose joins list-only blocks that follow into the same list
  while (!mixed && list.length && blocks[used]?.every((l) => LIST_LINE.test(l))) { list = [...list, ...blocks[used]]; used++; }
  const { lead, rest } = para.length ? splitLead(para.join(" ")) : { lead: "", rest: "" };
  answer = lead;
  if (rest) mixed = true;
  return { answer, list, more: mixed || blocks.length > used || list.length > PAGE_CAP, toMd };
}

/** A section's markdown → its first sentence and everything after it (the
    rest of that paragraph, then any list or later paragraph), for the answer
    line and the "More detail" fold. */
function splitAnswer(md: string): { first: string; rest: string } {
  if (!md.trim()) return { first: "", rest: "" };
  const blocks = md.split(/\n{2,}/);
  const lines = blocks[0].split("\n");
  const para: string[] = [];
  let i = 0;
  while (i < lines.length && !/^\s*(?:- |\d+\.\s)/.test(lines[i])) para.push(lines[i++].trim());
  const tail = [lines.slice(i).join("\n"), ...blocks.slice(1)].filter((s) => s.trim()).join("\n\n");
  if (!para.length) return { first: "", rest: md };
  const { lead, rest } = splitLead(para.join(" "));
  return { first: lead, rest: [rest, tail].filter(Boolean).join("\n\n") };
}

/** Page-local unit words for the "What one buyer pays" table. */
const UNIT_SHORT: Record<PriceUnit, string> = {
  "one-off": "once", "per-seat-month": "a month", "per-year": "a year",
  "per-case": "per case", "per-project": "per project", "per-hour": "an hour",
};
const MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const monthLabel = (iso: string) => {
  const [y, m] = iso.split("-").map(Number);
  return y && m ? `${MON[m - 1]} ${y}` : iso;
};

/** A Why now key as a period: `17 Dec 2026` (one day) or `Dec 2026` (the
    month). Anything else (`Late 2026`, `Since July 2026`) is not a date. */
const MONTH_NAMES = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"];
function keyPeriod(key: string): { start: number; end: number } | null {
  const m = key.trim().match(/^(?:(\d{1,2})\s+)?([A-Za-z]{3,9})\.?\s+(\d{4})$/);
  if (!m) return null;
  const w = m[2].toLowerCase();
  const mi = MONTH_NAMES.findIndex((n) => n.startsWith(w) && (w.length === 3 || w === n));
  if (mi < 0) return null;
  const y = Number(m[3]);
  if (m[1]) { const t = Date.UTC(y, mi, Number(m[1])); return { start: t, end: t }; }
  return { start: Date.UTC(y, mi, 1), end: Date.UTC(y, mi + 1, 0) };
}

/** For picking the page's Why now rows only: a season of a year (`Late
    2026`) as its third of the year, on top of keyPeriod. Never used for the
    warm dot, which stays on exact months and days. */
const SEASONS: Record<string, [number, number]> = { early: [0, 3], mid: [4, 7], late: [8, 11] };
function loosePeriod(key: string): { start: number; end: number } | null {
  const exact = keyPeriod(key);
  if (exact) return exact;
  const m = key.trim().match(/^(early|mid|late)\s+(\d{4})$/i);
  if (!m) return null;
  const [a, b] = SEASONS[m[1].toLowerCase()];
  const y = Number(m[2]);
  return { start: Date.UTC(y, a, 1), end: Date.UTC(y, b + 1, 0) };
}
/** A keyed bullet, as lib/site/prose.tsx reads one. */
const KEYED_LINE = /^- \*\*([^*]{1,40}?):\*\*\s+/;

export const dynamicParams = false;

/** REJECTED RECORDS GET NO PAGE (owner, 2026-09-16; SPEC §5): they are left out
    of the params and out of find(), so their URLs 404. check-site asserts it
    against the emitted HTML. */
export function generateStaticParams() {
  return getProblems()
    .filter((p) => p.status !== "rejected")
    .map((p) => ({ region: p.region, id: p.id }));
}

type Params = { params: Promise<{ region: string; id: string }> };

const find = (region: string, id: string): Problem | undefined =>
  getProblems().find((p) => p.region === region && p.id === id && p.status !== "rejected");

/** Markdown to one plain line for <meta>: no [Sn] markers, links reduced to
    their words, no emphasis. */
const metaText = (s: string) =>
  s
    .replace(/\s*\[S\d+(?:\s*,\s*S?\d+)*\](?!\()/g, "")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\s+/g, " ")
    .trim();

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { region, id } = await params;
  const p = find(region, id);
  if (!p) return { title: "Problem not found" };
  // the description is the record's own `brief`, its markers stripped;
  // a record without one falls back to its suggested solution (audit B14)
  const brief = (p as { brief?: string }).brief;
  const description = metaText(typeof brief === "string" && brief.trim() ? brief : p.solution);
  return { title: `${p.title} — localproblems.org`, description };
}

// ---- deadlines (deterministic against extractDate, never the wall clock) ---
const DAY = 86_400_000;

/** `alias`: an older anchor for the same section, so deep links written
    against the live record page still land (audit B5: `#how-big` → Who pays).
    No count beside the title (redesign §3.2). */
function Section({ id, alias, title, score, children }: { id: string; alias?: string | string[]; title: string; score?: ProtoScore; children: ReactNode }) {
  const aliases = alias === undefined ? [] : Array.isArray(alias) ? alias : [alias];
  return (
    <section className="ls-sec" id={id} aria-labelledby={`${id}-h`}>
      {aliases.map((a) => <span key={a} id={a} className="ls-alias" aria-hidden="true" />)}
      {/* PROTOTYPE score badge (lib/site/score-proto.ts): beside the heading
          (owner, 2026-09-17: "try putting the badges next to the heading"),
          a quiet pill: a faint tint and the dot in the score's tone, the text
          gray. A sibling of the h2, so it stays out of the heading's name;
          it wraps under the title where the line is too narrow. */}
      {score ? (
        <div className="ls-h2-row">
          <h2 className="ls-h2" id={`${id}-h`}>{title}</h2>
          <p className={`ls-h2-chip is-${scoreTone(score.n, score.max)}`}>
            <ScoreDot n={score.n} max={score.max} />
            <span>{score.n}/{score.max} · {score.word}</span>
          </p>
        </div>
      ) : (
        <h2 className="ls-h2" id={`${id}-h`}>{title}</h2>
      )}
      {children}
    </section>
  );
}

/** A score's tone, one rule everywhere (owner-approved 2026-09-17): full
    marks good, at least half medium, under half (0 included) bad. */
function scoreTone(n: number, max: number): "good" | "mid" | "bad" {
  if (max > 0 && n >= max) return "good";
  return max > 0 && n / max >= 0.5 ? "mid" : "bad";
}

/** A solid dot in the score's tone (owner, 2026-09-17: "lets use dots
    instead of the circles"). Decorative: n/max text always sits beside it. */
function ScoreDot({ n, max }: { n: number; max: number }) {
  return <span className={`ls-sdot is-${scoreTone(n, max)}`} aria-hidden="true" />;
}

/** Each opportunity check as a builder needs it (owner, round 3: "expand on
    the tooltips in the scoring"): what it asks, why it matters, and what earns
    the points. Every ladder line restates SCORING.md's rungs in plain words —
    PROOF, GAP, DEMAND, MONEY, URGENCY — and nothing more. MONEY is worded as
    PROXIMITY to public budget, as SCORING.md insists; URGENCY is two parts
    (deadline 0–2 plus 1 for fresh evidence), so its ladder has two lines. */
const DIM_INFO: Record<Dim, { ask: string; why: string; ladder: string[] }> = {
  proof: {
    ask: "Does this already work somewhere else?",
    why: "Established companies selling it in other markets show that buyers will pay, so you are not betting on an untested idea.",
    ladder: [
      "no foreign company on file",
      "only early players abroad: prototype, pre-customer, seed",
      "one established company abroad",
      "established in two or more markets, one of them near Czechia",
    ],
  },
  urgency: {
    ask: "Is something forcing buyers to act soon?",
    why: "A dated rule, such as a new regulation or a compliance deadline, turns “nice to have” into “must buy by”.",
    ladder: [
      "no dated rule forcing action",
      "a compliance date more than 18 months away",
      "a compliance date within 18 months",
    ],
  },
  demand: {
    ask: "Are people visibly complaining about this, or asking for it?",
    why: "Documented pain means you will not have to convince buyers the problem exists before you can sell them the fix.",
    ladder: [
      "assumed: nothing documented",
      "scattered complaints",
      "recurring documented complaints, a petition, or industry pressure",
    ],
  },
  money: {
    ask: "Is public money already moving near this problem?",
    why: "Tenders, grants and budget lines show buyers with budgets nearby. It is not proof they will buy this; what a buyer actually pays is under Willing to pay.",
    ladder: [
      "no public money nearby",
      "a relevant tender or grant exists",
      "an open tender or grant of about 5M CZK or more, or recurring yearly spend",
    ],
  },
  gap: {
    ask: "Is the Czech market still open?",
    why: "A mature Czech company already selling this means fighting an incumbent. Early players, or firms selling something nearby, still leave room to enter.",
    ladder: [
      "a mature Czech company already sells this",
      "Czech companies sell this, but all are still early",
      "checked, and no Czech company sells this",
    ],
  },
};

/** The four gates that SET the entry level and their weights, restated from
    SCORING.md ("DIFFICULTY TO ENTER IS NOT A SCORE"). web/lib/format.ts holds
    the same table unexported; the level itself is never derived here — the
    record carries it and scripts/check-records.py asserts it. This only says
    which gate weighs what, so the page can show it. `incumbents` has no row by
    rule: the gap score already prices competition. */
const ENTRY_WEIGHTS = {
  buyer: { "small-firms": 0, "large-firms": 1, public: 2 },
  permission: { none: 0, registration: 1, licence: 2 },
  integration: { software: 0, "national-system": 1, certified: 2 },
  money: { bootstrap: 0, "outside-money": 2 },
} as const;

/** The gates as clauses of ONE plain sentence (owner, round 3: "difficulty
    to enter is needlessly complex now"). Only the gates carrying the top
    weight speak — the same selection `entryGates` makes — and an easy record
    names its four open gates instead. Phrases wrap the format.ts labels; they
    add no fact the record does not hold. */
const GATE_CLAUSE = {
  buyer: { "small-firms": "small firms buy it", "large-firms": "the buyers are large firms", public: "the buyers are the public sector" },
  permission: { none: "no permission is needed", registration: "it needs a registration", licence: "it needs a licence" },
  integration: { software: "it is plain software", "national-system": "it must plug into a national system or hardware", certified: "it must be a certified product" },
  money: { bootstrap: "it can be bootstrapped", "outside-money": "it needs outside money before the first sale" },
} as const;

/** WHAT MAKES ENTRY EASIER, AND WHAT HARDER (owner, 2026-09-17: "explain
    more … which is making it easier and which harder"). Each gate value in
    plain words, short for the page and whole for the sheet. A gate at weight
    0 opens the door; any weight above 0 narrows it. The words restate
    data/CONVENTIONS.md's definitions of each value and add nothing; the level
    is still the record's own, never re-derived. `incumbents` is not a gate
    here by rule (SCORING.md): competition is priced under Who already sells
    this. */
const GATE_WORDS = {
  buyer: {
    "small-firms": ["Small firms buy it", "Small firms buy it, with no public tender to win first."],
    "large-firms": ["The buyers are large firms", "The first contract is with a large firm, not a small one."],
    public: ["The buyers are public bodies", "The buyers are public bodies, so the first sale goes through public procurement."],
  },
  permission: {
    none: ["No licence is needed", "Nothing beyond a trade licence is needed to start selling."],
    registration: ["It needs a registration first", "Selling needs a registration or certification first, usually a matter of weeks."],
    licence: ["It needs a licence to sell", "The law requires a licence to sell the product itself."],
  },
  integration: {
    software: ["It is plain software", "It is plain software, with no state system or hardware to plug into."],
    "national-system": ["It must plug into a state system or hardware", "It cannot work without connecting to a state or EU system, or without hardware or crews in the field."],
    certified: ["The product must be certified", "The product itself must pass a certification or audit before anyone can use it."],
  },
  money: {
    bootstrap: ["It can start on your own money", "A small team can reach its first paying customer on its own money."],
    "outside-money": ["It needs outside money first", "It needs outside money before the first sale."],
  },
} as const;

/** Public money rows (owner, 2026-09-17: "make it explanatory: these are the
    towns that already paid in this date"). The kinds of buyer are read from
    each row's own words; a row naming none counts as "other public bodies". */
const BUYER_KINDS: [string, RegExp][] = [
  ["hospitals", /hospital|nemocnic/i],
  ["towns", /\b(?:city|cities|town|towns|municipal\w*|region\w*|village)\b|měst|obec|kraj/i],
  ["state agencies", /\b(?:agency|agencies|ministry|authority)\b|ministerstv|úřad/i],
  ["utilities", /\butilit\w*|ČEZ|vodárn|water compan/i],
  ["schools", /universit|school|škol/i],
  ["care homes", /care home|social[- ]care|domov/i],
];
/** A free-text entry reason written as "Easier: a, b, and c. Harder: x, and
    y." (the p-0008 rewrite, 2026-09-17) → its two lists, split at top-level
    semicolons, else at ", and " and at commas that start a new item (never at
    ", so …", ", which …": those continue the item). Null when the reason is
    plain prose, which then reads as one paragraph in the sheet. */
function splitItems(t: string): string[] {
  const out: string[] = [];
  const semi = /;/.test(t.replace(/\[[^\]]*\]|\([^)]*\)/g, ""));
  let depth = 0, from = 0;
  for (let i = 0; i < t.length; i++) {
    const ch = t[i];
    if (ch === "[" || ch === "(") depth++;
    else if (ch === "]" || ch === ")") depth = Math.max(0, depth - 1);
    else if (depth === 0 && (semi ? ch === ";" : ch === "," && t[i + 1] === " ")) {
      const next = t.slice(i + 1).trimStart();
      if (!semi && /^(?:so|which|who|because|but|while|though|since|as|or|when|where|until)\b/i.test(next)) continue;
      out.push(t.slice(from, i));
      from = i + 1;
    }
  }
  out.push(t.slice(from));
  return out.map((x) => x.trim().replace(/^and\s+/i, "").replace(/[.;,\s]+$/, "")).filter(Boolean);
}
function parseEntryWhy(why: string): { easier: string[]; harder: string[] } | null {
  const e = why.match(/(?:^|\s)Easier:\s*([\s\S]*?)(?=\s+Harder:|$)/);
  const h = why.match(/(?:^|\s)Harder:\s*([\s\S]*?)(?=\s+Easier:|$)/);
  if (!e && !h) return null;
  return { easier: e ? splitItems(e[1]) : [], harder: h ? splitItems(h[1]) : [] };
}
/** The page's compact form of one reason: up to its first continuing clause. */
const compactItem = (t: string) => t.split(/,\s+(?=(?:so|which|who|because|but|while)\b)/i)[0];

const PURCHASE_TYPES = new Set(["contract", "tender", "tenders"]);
const MONEY_KIND: Record<string, string> = { contract: "Signed contract", tender: "Tender", tenders: "Tender", subsidy: "Grant call" };
const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`;

const joinClauses = (c: string[]) =>
  c.length <= 1 ? c.join("") : `${c.slice(0, -1).join(", ")}, and ${c[c.length - 1]}`;

/** WHICH SOURCES BACK A COMPANY (owner, round 4: "isn't it connected to
    sources? … why isn't it mentioned?"). The record links an entry to its
    ledger in five ways, and every one is read — strongest first:
      · comps[].signal = a source's `signal` (the evidence-layer id)
      · the entry's url on the ledger (same url, or same site)
      · a source NAMED for it (the ledger row "Secfix", "Registr smluv —
        Lexnova …"; a money receipt may name a vendor by its first word)
      · `[Sn]` markers written inside its evidence / traction line
    A local player with none of those falls back to the market check whose
    note names it — the search that found it, labelled as such. Anything left
    says "no source on file", never nothing. Measured across the 29 live
    records (2026-09-15): comps 45 of 78 backed, locals 116 direct + 39 by the
    market check of 159. */
const GENERIC_HOSTS = new Set(["github.com", "linkedin.com", "apps.apple.com", "play.google.com", "youtube.com", "facebook.com", "ares.gov.cz"]);
const normUrl = (u: string) => u.replace(/\/+$/, "");
const hostOf = (u: string) => { try { return new URL(u).host.replace(/^www\./, ""); } catch { return ""; } };
const nameKey = (name: string) => name.split(/\s*[(/]/)[0].trim().toLowerCase();
const MARKERS = /\[S(\d+)((?:\s*,\s*S?\d+)*)\]/g;
const stripMarkers = (t: string) => t.replace(/\s*\[S\d+(?:\s*,\s*S?\d+)*\](?!\()/g, "");

type Backing = { tier: "direct" | "found" | "none"; ns: number[] };
function backing(
  srcs: ProblemSource[],
  e: { name: string; url?: string; signal?: string; text: string },
  local: boolean,
): Backing {
  const found = new Set<number>();
  const k = nameKey(e.name);
  const first = k.split(/\s+/)[0];
  const word = first.length >= 6 && !/\d/.test(first) ? first : null;
  srcs.forEach((s, i) => {
    const n = i + 1, nm = (s.name ?? "").toLowerCase(), h = hostOf(s.url);
    if (e.signal && s.signal === e.signal) found.add(n);
    if (e.url && (normUrl(s.url) === normUrl(e.url) || (h && h === hostOf(e.url) && !GENERIC_HOSTS.has(h)))) found.add(n);
    if (s.type !== "gap-check" && nm.includes(k)) found.add(n);
    if (word && ["price", "contract", "tender"].includes(s.type) && nm.includes(word)) found.add(n);
  });
  for (const m of e.text.matchAll(MARKERS)) {
    [m[1], ...m[2].split(",")].map((x) => Number(x.trim().replace(/^S/, "")))
      .filter((n) => Number.isInteger(n) && n >= 1 && n <= srcs.length).forEach((n) => found.add(n));
  }
  if (found.size) return { tier: "direct", ns: [...found].sort((a, b) => a - b) };
  if (local) {
    const g = srcs.map((s, i) => ({ s, n: i + 1 }))
      .filter((x) => x.s.type === "gap-check" && `${x.s.note} ${x.s.why ?? ""}`.toLowerCase().includes(k));
    if (g.length) return { tier: "found", ns: g.map((x) => x.n) };
  }
  return { tier: "none", ns: [] };
}

const sentence = (s: string) => (/[.!?…]$/.test(s) ? s : `${s}.`);

export default async function LabRecord({ params }: Params) {
  const { region, id } = await params;
  const p = find(region, id);
  if (!p) notFound();

  const sources = labSources(p);
  const ctx: CiteCtx = newCtx(sources);
  const opts: ProseOpts = { resolveLedger: signalHref };
  const sections = splitBody(p.body);
  const extract = extractDate();
  const refs = dimRefs(p);
  const comps = p.comps ?? [];
  const locals = p.locals ?? [];
  const prices = priceReceipts(p);
  const moneyRows = refs.money.filter((n) => p.sources[n - 1].type !== "price");

  // EVERY SECTION IS BUILT BEFORE THE JSX, IN READING ORDER: building one
  // records its citations into ctx, and the drawer's "Cited in" lines need the
  // finished record before they can be drawn.
  const prose = (section: string, md: string) => {
    ctx.section = section;
    return md ? Prose(md, ctx, { ...opts, lead: true }) : null;
  };

  // HEADLINE COPY (owner, 2026-09-16: "put it to site"): the record's own
  // optional `brief` — ONE sentence on what is happening and why it is urgent
  // (owner: "3 bullets at most"), its [Sn] markers as the page's citation
  // pills — and `good_for`, one line on who it suits. The solution has its own
  // box below, so the head carries the story and "Good for" only. They follow
  // the front page's card rules (DESIGN.md "Row card", "Labels"): the story a
  // plain paragraph, "Good for" a meta label on its own line with the words
  // under it — no bullets, no run-in label. Read through a local structural
  // type until lib/data.ts carries the fields. Built first: it is the first
  // thing the page reads.
  const headline = p as { brief?: string; good_for?: string; draft_law?: string };
  const brief = typeof headline.brief === "string" && headline.brief.trim() ? headline.brief.trim() : null;
  const goodFor = typeof headline.good_for === "string" && headline.good_for.trim() ? headline.good_for.trim() : null;
  ctx.section = "Summary";
  const briefNode = brief ? inline(brief, ctx, opts, "brief") : null;
  const goodForNode = goodFor ? inline(goodFor, ctx, opts, "goodfor") : null;
  // `draft_law` (2026-09-16): the main pain depends on a law not passed yet.
  // The head carries the "Draft law" badge with the record's line under it,
  // its [Sn] as the usual source pill, and the one plain sentence.
  const draftLaw = typeof headline.draft_law === "string" && headline.draft_law.trim() ? headline.draft_law.trim() : null;
  // the line is a phrase ("…, still a draft [S1]"); it closes with a full
  // stop before its marker so the plain sentence after it reads as a new one
  const closeLine = (t: string) => {
    const m = t.match(/^(.*?)(\s*\[S\d+(?:\s*,\s*S?\d+)*\])?$/)!;
    return (/[.!?]$/.test(m[1]) ? m[1] : `${m[1]}.`) + (m[2] ?? "");
  };
  const draftLawNode = draftLaw ? inline(closeLine(draftLaw), ctx, opts, "draftlaw") : null;

  // THE PAGE IS THE OUTLINE, THE SHEET IS THE SECTION (owner, 2026-09-16).
  // A section with a sheet is built twice, outline then whole section, in
  // reading order, so both halves' pills are recorded against the section
  // before the drawer's "Cited in" lines are drawn.
  const rec = `${p.id.toUpperCase()} · ${p.title}`;
  const leadProse = (md: string) => (md ? Prose(md, ctx, { ...opts, lead: true }) : null);

  // ---- 1. The problem: page = answer line + the first list (capped); sheet =
  //      the whole section
  const probOut = outline(sections.problem);
  ctx.section = "The opportunity";
  const problemPage = leadProse(probOut.toMd(probOut.list.slice(0, PAGE_CAP)));
  const problemFull = prose("The opportunity", sections.problem);
  const problemMore = probOut.more;

  // ---- 2. Suggested solution: page = the sentence and the process figure;
  //      the "after" paragraph (never cited: markers stripped) is sheet-only
  ctx.section = "Suggested solution";
  const solutionNode = inline(p.solution, ctx, opts, "sol");
  const afterLine = p.process?.summary?.after ? stripMarkers(p.process.summary.after).trim() : "";
  // the one two-lane ProcessSteps diagram (owner, 2026-09-16) is this box's
  // scan block on the page, and How it works is not a section of its own;
  // the today summary and the after paragraph are sheet-only
  const stepsFig = ProcessSteps({ process: p.process, sources: p.sources, ctx });
  const todayMd = p.process?.summary?.today ? p.process.summary.today.trim() : "";
  const solutionMore = !!afterLine || !!todayMd;
  const solutionSheet = solutionMore ? (
    <>
      <p className="ls-answer">{inline(p.solution, ctx, opts, "sol-s")}</p>
      {todayMd && <p className="ls-p">{inline(todayMd, ctx, opts, "sol-today")}</p>}
      {afterLine && <p className="ls-p">{afterLine}</p>}
      {(() => { const f = ProcessSteps({ process: p.process, sources: p.sources, ctx }); return f ? <div className="ls-fig">{f}</div> : null; })()}
    </>
  ) : null;

  // ---- 3. Why now: page = answer line + at most three dated rows, the
  //      nearest still ahead of extractDate() (never the wall clock), soonest
  //      first; sheet = the whole keyed list. A date inside the next six
  //      months carries the warm dot in both.
  const fromMs = Date.parse(extract);
  const keyedSoon = (key: string) => {
    const per = keyPeriod(key);
    return !!per && per.end >= fromMs && per.start <= fromMs + 183 * DAY;
  };
  const nowOut = outline(sections.window);
  let nowRows = nowOut.list.slice(0, PAGE_CAP);
  if (nowOut.list.length && nowOut.list.every((l) => KEYED_LINE.test(l))) {
    const dated = nowOut.list.map((l, i) => ({ l, i, per: loosePeriod(l.match(KEYED_LINE)![1]) }));
    const ahead = dated.filter((d) => d.per && d.per.end >= fromMs).sort((x, y) => x.per!.start - y.per!.start || x.i - y.i);
    nowRows = (ahead.length ? ahead : dated.slice(-PAGE_CAP)).slice(0, PAGE_CAP).map((d) => d.l);
  }
  const nowMore = nowOut.more || nowRows.length < nowOut.list.length;
  ctx.section = "Why now";
  const windowPage = sections.window ? Prose(nowOut.toMd(nowRows), ctx, { ...opts, lead: true, keyedSoon }) : null;
  const windowNode = sections.window && nowMore ? Prose(sections.window, ctx, { ...opts, lead: true, keyedSoon }) : null;

  // ---- 4. Willing to pay (was Who pays): page = answer line + the keyed money facts (capped);
  //      sheet = all of it, the buyer table, where to look, public money
  const whoPaysMd = sections.dek && sections.howbig
    ? `${sections.dek}${/^\s*(?:- |\d+\.\s)/.test(sections.howbig) ? "\n" : " "}${sections.howbig}`
    : sections.dek || sections.howbig;
  const payOut = outline(whoPaysMd);
  ctx.section = "Willing to pay";
  const whoPaysPage = leadProse(payOut.toMd(payOut.list.slice(0, PAGE_CAP)));
  const whoPaysNode = prose("Willing to pay", whoPaysMd);
  const priceRows = [...prices].sort((a, b) => a.s.amount_czk - b.s.amount_czk).map(({ n, s }) => (
    <div key={`pr${n}`} className="ls-keyed-row">
      <dt className="ls-keyed-k">{czk(s.amount_czk)} {UNIT_SHORT[s.unit]}</dt>
      <dd className="ls-keyed-v">
        {capitalize(s.payer)}<span className="ls-row-meta"> · {PRICE_BASIS_LABELS[s.basis]} · {monthLabel(s.date)}</span>{" "}
        {cite([n], ctx)}
      </dd>
    </div>
  ));
  // PUBLIC MONEY NEARBY, EXPLAINED (owner, 2026-09-17): a heading that says
  // what the rows are and how many, one intro line computed from them (who
  // bought, between which months), and each row as one plain sentence: who
  // paid, for what, then how much (the key) and when (the meta). Purchases
  // (contracts, tenders) first, then grant calls, each largest first.
  const moneyData = moneyRows.map((n) => {
    const src = p.sources[n - 1];
    const sig = src.signal ? getSignal(src.signal) : undefined;
    const s = sources[n - 1];
    return { n, eur: sig?.money_eur ?? null, type: src.type, date: src.date, s };
  });
  const purchases = moneyData.filter((m) => PURCHASE_TYPES.has(m.type));
  const grants = moneyData.filter((m) => m.type === "subsidy");
  const otherMoney = moneyData.length - purchases.length - grants.length;
  function rowSentence(s: LabSource) {
    const src = s.why ?? s.gist ?? s.title;
    const first = splitLead(stripMarkers(src).replace(/~\s?/g, "about ")).lead.split(/\s+[—–]\s+/)[0].replace(/[\s,;:]+$/, "");
    return sentence(capitalize(first));
  }
  // the kinds of buyer are read from the row's own title, gist and sentence
  const wordsOf = (s: LabSource) => `${s.title} ${s.gist ?? ""} ${rowSentence(s)}`;
  const moneyHead = (() => {
    const nC = purchases.filter((m) => m.type === "contract").length;
    const nT = purchases.length - nC;
    const parts: string[] = [];
    if (nC && nT) parts.push(`${purchases.length} public contracts and tenders`);
    else if (nC) parts.push(plural(nC, "signed public contract", "signed public contracts"));
    else if (nT) parts.push(plural(nT, "public tender", "public tenders"));
    if (grants.length) parts.push(plural(grants.length, "grant call", "grant calls"));
    if (otherMoney) parts.push(plural(otherMoney, "other sign of public money", "other signs of public money"));
    const head = parts.length > 1 ? `${parts.slice(0, -1).join(", ")}, plus ${parts[parts.length - 1]}` : parts[0] ?? "";
    return capitalize(head.replace(/^1 /, "One "));
  })();
  const moneyIntro = (() => {
    const lines: string[] = [];
    if (purchases.length) {
      const counts = BUYER_KINDS.map(([kind, re]) => ({ kind, n: purchases.filter((m) => re.test(wordsOf(m.s))).length }))
        .filter((k) => k.n > 0).sort((a, b) => b.n - a.n);
      const unmatched = purchases.filter((m) => !BUYER_KINDS.some(([, re]) => re.test(wordsOf(m.s)))).length;
      const kinds = counts.slice(0, 3).map((k) => k.kind);
      const others = unmatched > 0 || counts.length > 3;
      if (!kinds.length) kinds.push("public bodies");
      else if (others) kinds.push("other public bodies");
      const hasC = purchases.some((m) => m.type === "contract");
      const hasT = purchases.some((m) => m.type !== "contract");
      const verb = hasC && hasT ? "signed or tendered" : hasC ? "signed contracts" : "put work out to tender";
      const months = purchases.map((m) => m.date.slice(0, 7)).sort();
      const [a, b] = [monthLabel(months[0]), monthLabel(months[months.length - 1])];
      const when = a === b ? `in ${a}` : a.slice(-4) === b.slice(-4) ? `between ${a.slice(0, 3)} and ${b}` : `between ${a} and ${b}`;
      const who = kinds.length <= 1 ? kinds.join("") : `${kinds.slice(0, -1).join(", ")} and ${kinds[kinds.length - 1]}`;
      lines.push(`${capitalize(who)} that ${verb} ${when}.`);
    }
    if (grants.length) lines.push(grants.length === 1 ? "The grant call can pay for this work." : "The grant calls can pay for this work.");
    return lines.join(" ");
  })();
  const moneyRow = ({ n, eur, type, date, s }: (typeof moneyData)[number]) => (
    <div key={`m${n}`} className="ls-keyed-row">
      <dt className="ls-keyed-k">{eur ? euro(eur) : ""}</dt>
      <dd className="ls-keyed-v">
        {rowSentence(s)}<span className="ls-row-meta"> · {MONEY_KIND[type] ?? s.typeLabel} · {monthLabel(date)}</span>{" "}
        {cite([n], ctx)}
      </dd>
    </div>
  );
  const byEur = (a: { eur: number | null }, b: { eur: number | null }) => (b.eur ?? -1) - (a.eur ?? -1);
  const moneyRowNodes = [
    ...[...purchases].sort(byEur),
    ...[...grants].sort(byEur),
    ...moneyData.filter((m) => !PURCHASE_TYPES.has(m.type) && m.type !== "subsidy").sort(byEur),
  ].map(moneyRow);
  const payMore = payOut.more || priceRows.length > 0 || moneyRowNodes.length > 0 || !!p.price_search;

  // ---- 5 and 6. Validated abroad, then Competition (owner, 2026-09-17:
  //      "separate abroad and in Czechia"): each section its own answer line,
  //      its own figure and its own sheet, and no company in both.
  const comp = splitAnswer(sections.competition);
  const solved = splitAnswer(sections.solved);
  const matrixFig = LocalMatrix({ p });
  const mapFig = CompMap({ p });
  // the sheet copies take their own scope, so the dots' popover ids never collide
  const matrixFigS = LocalMatrix({ p, scope: "s" });
  const mapFigS = CompMap({ p, scope: "s", list: false });
  // Willing to pay: what buyers already pay (page) and when they bought (sheet)
  const payDots = PayDots({ p });
  const payDotsS = PayDots({ p, scope: "s" });
  const payTimeline = PayTimeline({ p, scope: "s" });

  const entity = (o: {
    id: string; name: string; href: string; m: Maturity;
    meta: string[]; text: string; back: Backing;
  }) => (
    <li key={o.id} className="ls-ent">
      <div className="ls-ent-id">
        <MaturityDot m={o.m} />
        {o.m && <span className="ls-sr">{o.m === "established" ? "Established: " : "Early: "}</span>}
        <a className="ls-ent-name" href={o.href} {...EXT}>{o.name}<ExtArrow /></a>
        {o.meta.length > 0 && <span className="ls-ent-meta">{o.meta.join(" · ")}</span>}
      </div>
      <div className="ls-ent-src">
        {o.back.tier === "none" ? <span className="ls-nosrc">No source on file</span> : cite(o.back.ns, ctx)}
      </div>
      <p className="ls-ent-sum">{inline(capitalize(o.text), ctx, opts, `ent-${o.id}`)}</p>
      {o.back.tier === "found" && <p className="ls-ent-note">Found by the register’s market check</p>}
    </li>
  );

  ctx.section = "Validated abroad";
  const abroadAnswer = solved.first ? inline(solved.first, ctx, opts, "abroad") : null;
  const abroadSheetAnswer = solved.first ? inline(solved.first, ctx, opts, "abroad-s") : null;
  const compRows = comps.map((c, i) => entity({
    id: `c${i}`, name: c.name, href: c.url, m: null,
    meta: [countryName(c.geo), `since ${c.since}`],
    text: c.traction,
    back: backing(p.sources, { name: c.name, url: c.url, signal: c.signal, text: c.traction }, false),
  }));
  const solvedRest = solved.rest ? Prose(solved.rest, ctx, opts) : null;
  const abroadMore = comps.length > 0 || !!solvedRest;

  ctx.section = "Competition";
  const compAnswer = comp.first ? inline(comp.first, ctx, opts, "comp") : null;
  const compSheetAnswer = comp.first ? inline(comp.first, ctx, opts, "comp-s") : null;
  const localGroups = (["direct", "adjacent"] as const).map((competes) => {
    const group = locals.filter((l) => l.competes === competes);
    if (!group.length) return null;
    return (
      <div key={competes} className="ls-sheet-group">
        <h3 className="ls-sheet-h3">
          {competes === "direct" ? "Sells this" : "Sells something nearby"} <span className="ls-count">{group.length}</span>
        </h3>
        <ul className="ls-ents">
          {group.map((l, i) => entity({
            id: `l${competes[0]}${i}`, name: l.name, href: localHref(l), m: l.maturity,
            meta: [l.since && `since ${l.since}`, l.ico && `IČO ${l.ico}`].filter(Boolean) as string[],
            text: l.evidence,
            back: backing(p.sources, { name: l.name, url: l.url, text: l.evidence }, true),
          }))}
        </ul>
      </div>
    );
  });
  const compRest = comp.rest ? Prose(comp.rest, ctx, opts) : null;
  const compMore = locals.length > 0 || !!compRest;

  // ---- 7 and 8 (Difficulty to enter, Suggested first moves) are built after
  //      the entry level below, still in reading order

  // ---- the scores as a table of contents (PROTOTYPE, lib/site/score-proto.ts)
  const proto = protoScores(p);
  const protoBy = Object.fromEntries(proto.map((r) => [r.key, r])) as Record<ProtoKey, ProtoScore>;
  const protoSum = protoTotal(proto);
  // ---- evidence mix — what KIND of sources hold this record up ------------
  const mix = [...sources.reduce((m, s) => {
    const row = m.get(s.typeLabel) ?? { n: 0, type: s.type };
    row.n += 1;
    return m.set(s.typeLabel, row);
  }, new Map<string, { n: number; type: string }>())].sort((a, b) => b[1].n - a[1].n);

  // ---- difficulty to enter: the level, and one sentence saying why -------
  const entry = p.entry;
  const gates = (["buyer", "permission", "integration", "money"] as const).map((g) => ({
    g,
    w: (ENTRY_WEIGHTS[g] as Record<string, number>)[entry[g]],
    clause: (GATE_CLAUSE[g] as Record<string, string>)[entry[g]],
  }));
  const topW = Math.max(...gates.map((x) => x.w));
  const setters = gates.filter((x) => x.w === topW);
  // The sentence must name exactly the gates entryGates() names; if the two
  // ever disagree, the page falls back to the canonical line, never guesses.
  const label = { buyer: ENTRY_BUYER_LABELS, permission: ENTRY_PERMISSION_LABELS, integration: ENTRY_INTEGRATION_LABELS, money: ENTRY_MONEY_LABELS };
  const mirrors = topW === 0
    || setters.map((x) => (label[x.g] as Record<string, string>)[entry[x.g]]).join(" · ") === entryGates(entry);
  const entryReason = !mirrors
    ? `Set by ${entryGates(entry)}.`
    : capitalize(topW === 0
      ? `nothing gates it: ${joinClauses(gates.map((x) => x.clause))}.`
      : `${joinClauses(setters.map((x) => x.clause))}.`);

  // ---- 7. Difficulty to enter: page = the level, then what makes entry
  //      easier and what harder, in short words; sheet = the level, the
  //      problem's own reason (else the one sentence naming the gates that set
  //      the level), the same two lists in whole sentences, and where
  //      competition is counted instead. The warm hue is the level's dot only.
  ctx.section = "Execution difficulty";
  const entryWhy = typeof entry.why === "string" && entry.why.trim() ? entry.why.trim() : "";
  const factors = gates
    .map((x) => ({ ...x, words: (GATE_WORDS[x.g] as Record<string, readonly [string, string]>)[entry[x.g]] }))
    .filter((x) => !!x.words);
  // the problem's own reason, when it is written as the two lists, IS the two
  // lists (said once); otherwise the gates speak and the reason is a paragraph
  const whyLists = entryWhy ? parseEntryWhy(entryWhy) : null;
  const groups = (full: boolean): [string, { k: string; node: ReactNode }[]][] => {
    if (whyLists) {
      const item = (t: string, i: number, side: string) => {
        const text = sentence(capitalize(full ? t : stripMarkers(compactItem(t))));
        return { k: `${side}${i}`, node: full ? inline(text, ctx, opts, `entry-${side}${i}`) : text };
      };
      return [
        ["Makes it easier", whyLists.easier.slice(0, full ? undefined : PAGE_CAP).map((t, i) => item(t, i, "e"))],
        ["Makes it harder", whyLists.harder.slice(0, full ? undefined : PAGE_CAP).map((t, i) => item(t, i, "h"))],
      ];
    }
    const pick = (list: typeof factors) => list.map((x) => ({ k: x.g, node: full ? x.words[1] : `${x.words[0]}.` }));
    return [
      ["Makes it easier", pick(factors.filter((x) => x.w === 0))],
      ["Makes it harder", pick(factors.filter((x) => x.w > 0).sort((a, b) => b.w - a.w))],
    ];
  };
  const factorLists = (full: boolean) => (
    <div className="ls-factors">
      {groups(full).map(([h, list]) => (
        <div key={h} className="ls-factor-col">
          <p className="ls-block-h">{h}</p>
          {list.length
            ? <ul className="ls-ul">{list.map((x) => <li key={x.k}>{x.node}</li>)}</ul>
            : <p className="ls-absent">Nothing.</p>}
        </div>
      ))}
    </div>
  );
  // page first, then sheet: reading order for the pills
  const entryPage = factorLists(false);
  const entrySheet = (
    <>
      <p className="ls-entry-level ls-level" data-level={entry.level}>{ENTRY_LEVEL_LABELS[entry.level]}</p>
      {!whyLists && <p className="ls-entry-why">{entryWhy ? inline(entryWhy, ctx, opts, "entry-why") : entryReason}</p>}
      {factorLists(true)}
      <p className="ls-absent">
        Competition does not change this level. It is covered under Competition.
      </p>
    </>
  );

  // ---- 8. Suggested first moves: page = each move's lead sentence (capped);
  //      sheet = the whole list, every explanation and link
  const movesOut = outline(sections.firstmoves);
  const moveLeads = movesOut.list.slice(0, PAGE_CAP).map((l) => {
    const m = l.match(/^(- |\d+\.\s+)(.*)$/)!;
    return `${m[1]}${splitLead(m[2]).lead}`;
  });
  const movesMore = movesOut.more || movesOut.list.some((l) => !!splitLead(l.replace(LIST_LINE, "")).rest);
  ctx.section = "Suggested first moves";
  const movesPage = leadProse(movesOut.toMd(moveLeads));
  const movesNode = movesMore ? prose("Suggested first moves", sections.firstmoves) : null;

  // one row of the full list — it lives only in the drawer now. Its id is the
  // live record's `s1…sN`, the same index as `sources[]` (audit B5), so an
  // old `#s12` link opens the drawer on that row (peek-hover.tsx).
  const ledgerRow = (s: LabSource) => {
    const where = [...new Set(ctx.cited.get(s.n) ?? [])];
    return (
      <li key={s.n} id={`s${s.n}`} className="ls-src">
        <span className="ls-mono ls-mono--md" aria-hidden="true">{s.mono}</span>
        <div className="ls-src-body">
          <div className="ls-src-top">
            <span className="ls-src-pub">{s.publisher}</span>
            {s.host && s.host !== s.publisher && <span className="ls-src-host">{s.host}</span>}
            <span className="ls-src-date"><time dateTime={s.date}>{s.dateLabel}</time></span>
          </div>
          {s.url ? (
            <a className="ls-src-title" href={s.url} {...EXT}>
              {s.title}<ExtArrow />
            </a>
          ) : (
            <span className="ls-src-title">{s.title}</span>
          )}
          {s.why && <p className="ls-src-why">{s.why}</p>}
          {s.quote && (
            <details className="ls-fold ls-src-quote">
              <summary>In the source’s words</summary>
              <blockquote>“{s.quote}”</blockquote>
            </details>
          )}
          <p className="ls-src-meta">
            {where.length ? `Cited in ${where.join(", ")}` : "On file, not cited in the text"}
          </p>
        </div>
      </li>
    );
  };

  // the rail's table of contents, in page order; the ladders are DIM_INFO's,
  // and Execution difficulty's is the four entry levels, easiest scoring most
  const EXEC_INFO = {
    ask: "How hard is it to start selling?",
    why: "Set by who buys, what permission selling needs, what it must plug into, and whether it needs outside money before the first sale.",
    ladder: ["very hard to enter", "hard to enter", "moderate to enter", "easy to enter"],
  };
  const toc: { id: string; title: string; score?: ProtoScore; info?: { ask: string; why: string; ladder: string[] } }[] = [
    { id: "opportunity", title: "The opportunity", score: protoBy.opportunity, info: DIM_INFO.demand },
    { id: "solution", title: "Suggested solution" },
    { id: "why-now", title: "Why now", score: protoBy["why-now"], info: DIM_INFO.urgency },
    { id: "willing-to-pay", title: "Willing to pay", score: protoBy["willing-to-pay"], info: DIM_INFO.money },
    { id: "validated-abroad", title: "Validated abroad", score: protoBy["validated-abroad"], info: DIM_INFO.proof },
    { id: "competition", title: "Competition", score: protoBy.competition, info: DIM_INFO.gap },
    { id: "execution-difficulty", title: "Execution difficulty", score: protoBy["execution-difficulty"], info: EXEC_INFO },
    ...(movesPage ? [{ id: "first-moves", title: "Suggested first moves" }] : []),
  ];
  const typeGroups = mix.map(([t]) => ({ t, list: sources.filter((s) => s.typeLabel === t) }));

  return (
    <div className="lab ls">
      <header className="ls-bar">
        <nav className="ls-crumbs" aria-label="Breadcrumb">
          <a href="/">Problems</a>
          <span className="ls-sep" aria-hidden="true">/</span>
          {/* one register per country; Czechia is the only one with data, so
              its list is the front page (owner, 2026-09-16: "Problems /
              Czechia / P-…") */}
          <a href="/">Czechia</a>
          <span className="ls-sep" aria-hidden="true">/</span>
          <span className="ls-crumb-id">{p.id.toUpperCase()}</span>
        </nav>
      </header>

      <div className="ls-shell">
        {/* The head: art, title, and every record fact — each stated once, all on
            the main column's left edge. */}
        <header className="ls-head">
          {SHOW_HEAD_ART && <CategoryArt category={p.category} className="ls-art" />}
          {/* a long title is marked so a phone can wrap it `pretty` instead of
              `balance` — see .ls-h1--long in problem.css */}
          <h1 className={p.title.length > 120 ? "ls-h1 ls-h1--long" : "ls-h1"}>{p.title}</h1>
          {(briefNode || goodForNode || draftLawNode) && (
            <div className="ls-brief">
              {briefNode && <p className="ls-brief-story">{briefNode}</p>}
              {goodForNode && (
                <p className="ls-brief-item">
                  <span className="ls-brief-k">Good for</span> <span className="ls-brief-v">{goodForNode}</span>
                </p>
              )}
              {/* the badge stands where a label would, over its line: the
                  same outlined gray pill as the front page's */}
              {draftLawNode && (
                <p className="ls-brief-item ls-draft">
                  <span className="ls-badge">Draft law</span>{" "}
                  <span className="ls-brief-v">
                    {draftLawNode}{" "}
                    <span className="ls-draft-note">Based on a law that is not passed yet, so this may change.</span>
                  </span>
                </p>
              )}
            </div>
          )}
          <dl className="ls-facts-row">
            <div><dt>Category</dt><dd>{categoryLabel(p.category)}</dd></div>
            <div>
              <dt>Entry</dt>
              <dd>
                <a className="ls-facts-link ls-level" data-level={entry.level} href="#execution-difficulty">
                  {ENTRY_LEVEL_LABELS[entry.level]}
                </a>
              </dd>
            </div>
            <div><dt>Verified</dt><dd><time dateTime={p.updated}>{fmtDate(p.updated)}</time></dd></div>
          </dl>
          {/* PHONE ONLY (≤640px): the scores in brief, right after the facts,
              each a link to its section; the full table of contents follows main */}
          <nav className="ls-toc-mini" aria-label="Scores">
            <p className="ls-toc-mini-hd"><span>Opportunity</span><span className="ls-score"><b>{protoSum.n}</b>/{protoSum.max}</span></p>
            <ul>
              {proto.map((r) => (
                <li key={r.key}>
                  <a href={`#${r.key}`}>
                    <span className="ls-toc-mini-l">{r.label}{r.labelSuffix ? ` · ${r.labelSuffix}` : ""}</span>
                    <span className="ls-toc-mini-w">{r.word}</span>
                    <span className="ls-dim-n">{r.n}/{r.max}</span>
                    <ScoreDot n={r.n} max={r.max} />
                  </a>
                </li>
              ))}
            </ul>
          </nav>
        </header>

        {/* THE RAIL BEFORE MAIN IN THE SOURCE (audit B13): a keyboard reaches
            the scorecard right after the head, not after every section.
            Grid areas keep it drawn in the right column; in one column
            (problem.css ≤1080px) reading-flow puts it back after main. */}
        <aside className="ls-rail" aria-label="Opportunity and evidence">
          {/* THE TABLE OF CONTENTS WITH SCORES (owner, 2026-09-17): every
              section in page order; a scored row carries its judgement word
              and a dot in its tone, with n/max shown on hover or focus. A stepper runs down its left edge: a hairline
              with one dot per section. The section in view fills its dot and
              darkens its label, sections already read keep a gray dot, all
              from CSS scroll-driven animations only (problem.css "toc");
              where they are unsupported every dot stays hollow. */}
          <section className="ls-card ls-toc" aria-labelledby="ls-opp-h" style={{ anchorName: "--ls-t-total" } as CSSProperties}>
            <div className="ls-card-hd">
              <h2 id="ls-opp-h" className="ls-eyebrow">Opportunity</h2>
              <span className="ls-score ls-tip-host" tabIndex={0} aria-describedby="ls-tip-total">
                <b>{protoSum.n}</b>/{protoSum.max}
                <span className="ls-tip" id="ls-tip-total" aria-hidden="true" style={{ positionAnchor: "--ls-t-total" } as CSSProperties}>
                  <span className="ls-tip-t">Opportunity</span>
                  <span className="ls-tip-p">The sum of five scored sections below: The opportunity, Why now, Willing to pay, Validated abroad and Competition. Execution difficulty is shown beside it, never added in. Each point is read from the evidence in that section.</span>
                  <span className="ls-tip-here">This problem: {protoSum.n} of {protoSum.max}.</span>
                </span>
              </span>
            </div>
            <ul className="ls-dims ls-toc-list">
              {toc.map(({ id: sid, title, score, info }) => {
                const tid = `ls-tip-toc-${sid}`;
                if (!score) {
                  return (
                    <li key={sid}>
                      <a href={`#${sid}`} className="ls-toc-row" data-toc={sid}>
                        <span className="ls-toc-dot" aria-hidden="true" />
                        <span className="ls-dim-l">{title}</span>
                      </a>
                    </li>
                  );
                }
                return (
                  <li key={sid}>
                    <a
                      href={`#${sid}`}
                      className={score.n === 0 ? "ls-toc-row is-scored ls-tip-host is-zero" : "ls-toc-row is-scored ls-tip-host"}
                      data-toc={sid}
                      aria-describedby={info ? tid : undefined}
                      style={{ anchorName: `--ls-t-${sid}` } as CSSProperties}
                    >
                      <span className="ls-toc-dot" aria-hidden="true" />
                      <span className="ls-dim-l">{title}{score.labelSuffix && <span className="ls-toc-suf"> · {score.labelSuffix}</span>}</span>
                      <span className="ls-toc-word">{score.word}</span>
                      {/* n/max stays in the DOM for screen readers; it shows on hover or focus */}
                      <span className="ls-dim-n">{score.n}/{score.max}</span>
                      <ScoreDot n={score.n} max={score.max} />
                      {info && (
                        <span className="ls-tip" id={tid} aria-hidden="true" style={{ positionAnchor: `--ls-t-${sid}` } as CSSProperties}>
                          <span className="ls-tip-t">{title}</span>
                          <span className="ls-tip-p"><b>{info.ask}</b> {info.why}</span>
                          <span className="ls-ladder">
                            {info.ladder.map((text, i) => (
                              <span key={i} className={i === score.n ? "ls-rung is-here" : "ls-rung"}>
                                <span className="ls-rung-n">{i}</span>{text}
                              </span>
                            ))}
                          </span>
                          <span className="ls-tip-here">This problem: {sentence(score.reason)} {score.n} of {score.max}.</span>
                        </span>
                      )}
                    </a>
                  </li>
                );
              })}
            </ul>
          </section>

          <section className="ls-card" aria-labelledby="ls-ev-h">
            <div className="ls-card-hd">
              <h2 id="ls-ev-h" className="ls-eyebrow">Evidence</h2>
              <span className="ls-card-n">{sources.length} sources</span>
            </div>
            <ul className="ls-mix">
              {mix.map(([t, { n, type }]) => {
                const note = typeNote(type);
                const tid = `ls-tip-ev-${type}`;
                return (
                  <li key={t}>
                    <button
                      type="button"
                      className="ls-mixrow ls-tip-host"
                      popoverTarget="sources"
                      data-src-group={`src-type-${t.toLowerCase().replace(/[^a-z0-9]+/g, "-")}`}
                      aria-describedby={note ? tid : undefined}
                      style={{ anchorName: `--ls-t-ev-${type}` } as CSSProperties}
                    >
                      <span className="ls-mix-l">{t}</span>
                      <span className="ls-mix-bar" aria-hidden="true"><span style={{ width: `${(n / mix[0][1].n) * 100}%` }} /></span>
                      <span className="ls-mix-n">{n}</span>
                      {note && (
                        <span className="ls-tip" id={tid} aria-hidden="true" style={{ positionAnchor: `--ls-t-ev-${type}` } as CSSProperties}>
                          <span className="ls-tip-t">{t}</span>
                          <span className="ls-tip-p">{note}</span>
                        </span>
                      )}
                    </button>
                  </li>
                );
              })}
            </ul>
            <button type="button" className="ls-all-link" popoverTarget="sources">
              View all {sources.length} sources<span aria-hidden="true"> →</span>
            </button>
          </section>
        </aside>

        <main className="ls-main">
          {/* THE PAGE IS THE OUTLINE: heading → answer line → one short scan
              block (never more than PAGE_CAP rows) → "Read more". The sheet
              beside each is the whole section. Order and names: owner,
              2026-09-17; every older anchor stays as an alias. */}
          <Section id="opportunity" alias="problem" title="The opportunity" score={protoBy.opportunity}>
            {problemPage}
            {problemMore && (
              <Sheet id="problem" title="The opportunity" rec={rec} about={SECTION_ABOUT.opportunity}>
                {problemFull}
              </Sheet>
            )}
          </Section>

          {/* a real section heading, the same h2 as every section (owner,
              2026-09-17: "Suggested solution could use a bigger heading") */}
          <section className="ls-solution" id="solution" aria-labelledby="solution-h">
            <span id="how-it-works" className="ls-alias" aria-hidden="true" />
            <h2 className="ls-h2" id="solution-h">Suggested solution</h2>
            <p className="ls-solution-v">{solutionNode}</p>
            {stepsFig && <div className="ls-fig">{stepsFig}</div>}
            {solutionSheet && <Sheet id="solution" title="Suggested solution" rec={rec} about={SECTION_ABOUT.solution}>{solutionSheet}</Sheet>}
          </section>

          <Section id="why-now" title="Why now" score={protoBy["why-now"]}>
            {windowPage ?? <p className="ls-absent">No dated rule on file.</p>}
            {windowNode && <Sheet id="why-now" title="Why now" rec={rec} about={SECTION_ABOUT["why-now"]}>{windowNode}</Sheet>}
          </Section>

          <Section id="willing-to-pay" alias={["who-pays", "how-big"]} title="Willing to pay" score={protoBy["willing-to-pay"]}>
            {whoPaysPage}
            {payDots}
            {!payMore && <p className="ls-absent">No price paid by a Czech buyer is on file yet.</p>}
            {payMore && (
              <Sheet id="who-pays" title="Willing to pay" rec={rec} about={SECTION_ABOUT["willing-to-pay"]}>
                {whoPaysNode}
                {payDotsS}
                {priceRows.length > 0 ? (
                  <div className="ls-block">
                    <p className="ls-block-h">What one buyer pays</p>
                    <dl className="ls-keyed ls-keyed--table">{priceRows}</dl>
                  </div>
                ) : (
                  <p className="ls-absent">No price paid by a Czech buyer is on file yet.</p>
                )}
                {priceRows.length === 0 && p.price_search && (
                  <div className="ls-block">
                    <p className="ls-block-h">Where to look</p>
                    <p className="ls-p">{p.price_search}</p>
                  </div>
                )}
                {moneyRowNodes.length > 0 && (
                  <div className="ls-block">
                    <p className="ls-block-h">{moneyHead}</p>
                    {payTimeline}
                    {moneyIntro && <p className="ls-block-intro">{moneyIntro}</p>}
                    <dl className="ls-keyed ls-keyed--table">{moneyRowNodes}</dl>
                  </div>
                )}
              </Sheet>
            )}
          </Section>

          {/* ONE home per company: abroad here, Czechia under Competition */}
          <Section id="validated-abroad" alias={["proven-abroad", "who-sells-this"]} title="Validated abroad" score={protoBy["validated-abroad"]}>
            {abroadAnswer && <p className="ls-answer">{abroadAnswer}</p>}
            {mapFig && <div className="ls-fig">{mapFig}</div>}
            {!abroadMore && <p className="ls-absent">No verified foreign comparable on file.</p>}
            {abroadMore && (
              <Sheet id="validated-abroad" title="Validated abroad" rec={rec} about={SECTION_ABOUT["validated-abroad"]}>
                {abroadSheetAnswer && <p className="ls-answer">{abroadSheetAnswer}</p>}
                {mapFigS && <div className="ls-fig">{mapFigS}</div>}
                {comps.length > 0
                  ? <ul className="ls-ents ls-ents--sheet">{compRows}</ul>
                  : <p className="ls-absent">No verified foreign comparable on file.</p>}
                {solvedRest && <div className="ls-grp-rest">{solvedRest}</div>}
              </Sheet>
            )}
          </Section>

          <Section id="competition" alias="local-competition" title="Competition" score={protoBy.competition}>
            {compAnswer && <p className="ls-answer">{compAnswer}</p>}
            {matrixFig && <div className="ls-fig">{matrixFig}</div>}
            {!compMore && <p className="ls-absent">No Czech seller on file.</p>}
            {compMore && (
              <Sheet id="competition" title="Competition" rec={rec} about={SECTION_ABOUT.competition}>
                {compSheetAnswer && <p className="ls-answer">{compSheetAnswer}</p>}
                {matrixFigS && <div className="ls-fig">{matrixFigS}</div>}
                {localGroups}
                {compRest && <div className="ls-grp-rest">{compRest}</div>}
              </Sheet>
            )}
          </Section>

          {/* The level, then what makes entry easier and what harder. */}
          <Section id="execution-difficulty" alias="difficulty-to-enter" title="Execution difficulty" score={protoBy["execution-difficulty"]}>
            {/* the level word is already in the score line under the heading */}
            {entryPage}
            <Sheet id="difficulty-to-enter" title="Execution difficulty" rec={rec} about={SECTION_ABOUT["execution-difficulty"]}>{entrySheet}</Sheet>
          </Section>

          {movesPage && (
            <Section id="first-moves" title="Suggested first moves">
              <div className="ls-moves-page">{movesPage}</div>
              {movesNode && <Sheet id="first-moves" title="Suggested first moves" rec={rec} about={SECTION_ABOUT["first-moves"]}>{movesNode}</Sheet>}
            </Section>
          )}
        </main>

      </div>

      {/* the front page's footer line, so a reader who finds a wrong source
          on the record can say so from the record (audit B7) */}
      <footer className="ls-foot">
        <div className="ls-foot-in">
          <span>localproblems.org · Czechia</span>
          <a href={CORRECTIONS_MAILTO}>Report a correction</a>
        </div>
      </footer>

      {/* The one full list of sources, grouped by kind. `id="sources"` is the
          live record's anchor for its sources list (audit B5); a `#sources`
          link opens the drawer (peek-hover.tsx). */}
      <div id="sources" popover="auto" className="ls-drawer" role="dialog" aria-labelledby="sources-h">
        <div className="ls-drawer-hd">
          <h2 id="sources-h" className="ls-drawer-t">Sources <span className="ls-count">{sources.length}</span></h2>
          <button type="button" className="ls-x" popoverTarget="sources" popoverTargetAction="hide" aria-label="Close">×</button>
        </div>
        <div className="ls-drawer-body">
          {typeGroups.map(({ t, list }) => (
            <div key={t} id={`src-type-${t.toLowerCase().replace(/[^a-z0-9]+/g, "-")}`} className="ls-drawer-group">
              <p className="ls-group-h">{t} <span className="ls-count">{list.length}</span></p>
              <ol className="ls-srcs ls-srcs--compact">
                {list.map((s) => ledgerRow(s))}
              </ol>
            </div>
          ))}
        </div>
      </div>

      <PeekHover />
    </div>
  );
}
