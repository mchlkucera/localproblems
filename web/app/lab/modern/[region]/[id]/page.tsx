// /lab/modern/[region]/[id] — the record page as a sources-first brief.
// LOCAL ONLY (the /lab layout 404s without LP_ADMIN=1). A design experiment in
// the Linear-like lab language: one font, a gray ramp, hierarchy from size,
// weight and shade. Its signature is the citation: a quiet publisher pill in
// the sentence that PEEKS into the source (who, what, when, why, and the
// source's own words) without leaving the line. See ../../cite.tsx.
//
// Reads exactly what the production record page reads (getProblems, splitBody,
// dimRefs, getSignal, extractDate as "today"); writes nothing.
import type { Metadata } from "next";
import type { CSSProperties, ReactNode } from "react";
import { notFound } from "next/navigation";
import { extractDate, getProblems, getSignal, localHref, priceReceipts, signalHref, urgencySplit, type Problem, type ProblemSource } from "../../../../../lib/data";
import { splitBody, splitLead, capitalize } from "../../../../../lib/sections";
import {
  ENTRY_BUYER_LABELS, ENTRY_INCUMBENT_LABELS, ENTRY_INTEGRATION_LABELS, ENTRY_LEVEL_LABELS,
  ENTRY_MONEY_LABELS, ENTRY_PERMISSION_LABELS, PRICE_BASIS_LABELS, PRICE_UNIT_LABELS,
  categoryLabel, countryName, czk, entryGates, euro, localityLong,
} from "../../../../../lib/format";
import { MAX, SCORE_ROWS, dimRefs, scoreRead, type Dim } from "../../../../../lib/scorecard";
import { EXT, ExtArrow, cite, newCtx, type CiteCtx } from "../../cite";
import { Prose, inline, type ProseOpts } from "../../prose";
import { fmtDate, labSources, typeNote, type LabSource } from "../../sources";
import { PeekHover } from "../../peek-hover";
import { CategoryArt } from "../../../parts/art/category-art";
// The approved figure kit. Every component returns null when its data is
// too thin, so each is CALLED before the JSX and tested before anything is
// drawn around it: no record shows an empty figure or a dangling caption.
import { CompMap, FieldGrid, FieldTimeline, MoneyScale, ProcessAfter, ProcessToday } from "../../../parts/figures/kit";
import "../../problem.css";

export const dynamicParams = false;

/** Read inside functions, never at module scope (see app/sources/page.tsx).
    The /lab layout's notFound() does NOT stop a page from rendering in a
    production build — measured 2026-09-10: the built p-0008.html carried the
    record beside the 404 — so every lab page gates itself, and a build without
    LP_ADMIN generates no params at all. */
const enabled = () => process.env.LP_ADMIN === "1";

export function generateStaticParams() {
  if (!enabled()) return [];
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
  if (!enabled()) return { title: "Record not found" };
  const { region, id } = await params;
  const p = find(region, id);
  if (!p) return { title: "Record not found" };
  // the description is the record's own `brief`, its markers stripped;
  // a record without one falls back to its suggested solution (audit B14)
  const brief = (p as { brief?: string }).brief;
  const description = metaText(typeof brief === "string" && brief.trim() ? brief : p.solution);
  return { title: `${p.title} — localproblems.org`, description };
}

// ---- deadlines (deterministic against extractDate, never the wall clock) ---
const DAY = 86_400_000;
const daysAfter = (iso: string, from: string) => Math.round((Date.parse(iso) - Date.parse(from)) / DAY);
function relativeOut(from: string, to: string): string {
  const days = daysAfter(to, from);
  if (days <= 0) return "now";
  const months = Math.round(days / 30.44);
  if (months < 1) { const w = Math.max(1, Math.round(days / 7)); return `~${w} ${w === 1 ? "week" : "weeks"} out`; }
  if (months < 12) return `~${months} months out`;
  const years = Math.round((months / 12) * 10) / 10;
  return `~${years % 1 === 0 ? years.toFixed(0) : years} years out`;
}
function futureDate(s: ProblemSource, extract: string): string | null {
  if (s.date > extract) return s.date;
  const sig = s.signal ? getSignal(s.signal) : undefined;
  return sig && sig.date > extract ? sig.date : null;
}


/** `alias`: an older anchor for the same section, so deep links written
    against the live record page still land (audit B5: `#how-big` → Who pays). */
function Section({ id, alias, title, count, children }: { id: string; alias?: string; title: string; count?: ReactNode; children: ReactNode }) {
  return (
    <section className="ls-sec" id={id} aria-labelledby={`${id}-h`}>
      {alias && <span id={alias} className="ls-alias" aria-hidden="true" />}
      <h2 className="ls-h2" id={`${id}-h`}>
        {title}
        {count != null && <span className="ls-h2-count">{count}</span>}
      </h2>
      {children}
    </section>
  );
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
    why: "A dated rule, such as a new regulation or a compliance deadline, turns “nice to have” into “must buy by”; recent evidence shows the problem is live now.",
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
    why: "Tenders, grants and budget lines show buyers with budgets nearby. It is not proof they will buy this; what a buyer actually pays is under Who pays.",
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

/** The total's bands, in plain words — SCORING.md's four bands without the
    verdict words, which render nowhere but the production scorecard. */
const BANDS: { min: number; range: string; text: string }[] = [
  { min: 10, range: "10–12", text: "backed on nearly every check" },
  { min: 8, range: "8–9", text: "strong enough to lead with" },
  { min: 5, range: "5–7", text: "a real case with open gaps" },
  { min: 0, range: "0–4", text: "thin evidence so far" },
];

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
  if (!enabled()) notFound();
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

  const problemNode = prose("The problem", sections.problem);
  // Built HERE, while ctx.section is still "The problem": the step pills
  // share the page's citation counter, so their peeks cannot collide and
  // the drawer's "Cited in" lines name this section. Null until a record
  // carries the new `process` field.
  const processTodayFig = ProcessToday({ process: p.process, sources: p.sources, ctx });
  ctx.section = "Suggested solution";
  const solutionNode = inline(p.solution, ctx, opts, "sol");
  // The proposal half is never cited (kit/process.tsx strips markers), so
  // it takes no ctx. compact: it sits inside the Suggested solution box.
  const processAfterFig = ProcessAfter({ process: p.process, sources: p.sources });

  const solvedNode = prose("Proven abroad", sections.solved);
  // Where the comparables are based and sell. Null with no drawable country.
  const compMapFig = CompMap({ p });
  // ---- companies: one row each, sources on the row, the long text behind
  //      "Details" in a modal. Built here, in reading order, so every pill
  //      and every [Sn] in the modal text is recorded like any citation.
  const entity = (o: {
    id: string; group: string; name: string; href: string; tag?: string;
    meta: string[]; text: string; mode: "sentence" | "clause"; back: Backing;
  }) => {
    const { lead, rest } = splitLead(o.text, o.mode);
    const plain = stripMarkers(rest ? lead : o.text);
    const needsDetails = !!rest || plain.length > 150;
    const mid = `ls-m-${o.id}`;
    const pills = o.back.tier === "none"
      ? <span className="ls-nosrc">No source on file</span>
      : cite(o.back.ns, ctx);
    const srcList = o.back.ns.map((n) => sources[n - 1]);
    return (
      <li key={o.id} className="ls-ent">
        <div className="ls-ent-id">
          <a className="ls-ent-name" href={o.href} {...EXT}>{o.name}<ExtArrow /></a>
          {o.tag && <span className="ls-tag ls-tag--cap">{o.tag}</span>}
          {o.meta.length > 0 && <span className="ls-ent-meta">{o.meta.join(" · ")}</span>}
        </div>
        <div className="ls-ent-src">{pills}</div>
        <p className="ls-ent-sum">{capitalize(plain)}</p>
        {needsDetails && (
          <button type="button" className="ls-ent-more" popoverTarget={mid} aria-label={`Details: ${o.name}`}>
            Details
          </button>
        )}
        {needsDetails && (
          <div id={mid} popover="auto" role="dialog" aria-labelledby={`${mid}-h`} className="ls-modal">
            <div className="ls-modal-hd">
              <p className="ls-modal-k">{o.group}</p>
              <button type="button" className="ls-x" popoverTarget={mid} popoverTargetAction="hide" aria-label="Close">×</button>
            </div>
            <div className="ls-modal-body">
              <h3 id={`${mid}-h`} className="ls-modal-t">
                <a href={o.href} {...EXT}>{o.name}<ExtArrow /></a>
              </h3>
              <p className="ls-modal-meta">
                {o.tag && <span className="ls-tag ls-tag--cap">{o.tag}</span>}
                {o.meta.length > 0 && <span>{o.meta.join(" · ")}</span>}
              </p>
              <p className="ls-modal-text">{inline(o.text, ctx, opts, `${mid}-t`)}</p>
              <p className="ls-modal-k ls-modal-k--src">
                {o.back.tier === "found" ? "Found by the register’s market check" : o.back.tier === "none" ? "Sources" : o.back.ns.length === 1 ? "Source" : `Sources · ${o.back.ns.length}`}
              </p>
              {srcList.length ? (
                <ul className="ls-modal-srcs">
                  {srcList.map((s) => (
                    <li key={s.n}>
                      <span className="ls-mono" aria-hidden="true">{s.mono}</span>
                      <span className="ls-modal-src">
                        <span className="ls-modal-src-top">{s.publisher} · {s.dateLabel}</span>
                        {s.url
                          ? <a className="ls-modal-src-t" href={s.url} {...EXT}>{s.title}<ExtArrow /></a>
                          : <span className="ls-modal-src-t">{s.title}</span>}
                        {s.why && <span className="ls-modal-src-why">{s.why}</span>}
                      </span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="ls-modal-none">No source on file for this entry. The line above is the register’s own note.</p>
              )}
            </div>
          </div>
        )}
      </li>
    );
  };

  const compRows = comps.map((c, i) => entity({
    id: `c${i}`, group: "Proven abroad", name: c.name, href: c.url,
    meta: [countryName(c.geo), `since ${c.since}`],
    text: c.traction, mode: "clause",
    back: backing(p.sources, { name: c.name, url: c.url, signal: c.signal, text: c.traction }, false),
  }));

  // The field on one year axis — it bridges Proven abroad and Local
  // competition, so it opens the section. Null with fewer than two dated
  // players, where an axis would carry a single dot.
  const fieldFig = FieldTimeline({ p });
  const competitionNode = prose("Local competition", sections.competition);
  const localGroups = (["direct", "adjacent"] as const).map((competes) => {
    const group = locals.filter((l) => l.competes === competes);
    if (!group.length) return null;
    const label = competes === "direct" ? "Sells this" : "Nearby";
    const count = competes === "direct"
      ? `${group.length} ${group.length === 1 ? "player" : "players"}`
      : `${group.length} selling something else`;
    return (
      <div key={competes} className="ls-grp">
        <div className="ls-grp-h"><p className="ls-grp-t">{label}</p><p className="ls-grp-n">{count}</p></div>
        <ul className="ls-ents">
          {group.map((l, i) => entity({
            id: `l${competes[0]}${i}`, group: `Local competition · ${label}`, name: l.name, href: localHref(l),
            tag: l.maturity,
            meta: [l.since && `since ${l.since}`, l.ico && `IČO ${l.ico}`].filter(Boolean) as string[],
            text: l.evidence, mode: "sentence",
            back: backing(p.sources, { name: l.name, url: l.url, text: l.evidence }, true),
          }))}
        </ul>
      </div>
    );
  });

  const whoPaysMd = [sections.dek, sections.howbig].filter(Boolean).join(" ");
  const whoPaysNode = prose("Who pays", whoPaysMd);
  // One log scale for both ledgers below. Null with fewer than two marks.
  const moneyFig = MoneyScale({ p });
  const priceRows = [
    ...prices.map(({ n, s }) => (
      <li key={`pr${n}`} className="ls-receipt">
        <span className="ls-receipt-main">
          <span className="ls-receipt-fig">{czk(s.amount_czk)}</span>{" "}
          <span className="ls-receipt-unit">{PRICE_UNIT_LABELS[s.unit]}</span>
          <span className="ls-receipt-who">{s.payer}</span>
        </span>
        <span className="ls-receipt-meta">{PRICE_BASIS_LABELS[s.basis]} · {fmtDate(s.date)}</span>
        <span className="ls-row-end">{cite([n], ctx)}</span>
      </li>
    )),
  ];
  const moneyRowNodes = [
    ...moneyRows.map((n) => {
      const s = sources[n - 1];
      const sig = p.sources[n - 1].signal ? getSignal(p.sources[n - 1].signal!) : undefined;
      return (
        <li key={`m${n}`} className="ls-receipt">
          <span className="ls-receipt-main">
            {sig?.money_eur ? <span className="ls-receipt-fig">{euro(sig.money_eur)}</span> : null}
            <span className="ls-receipt-who">{s.gist ? capitalize(s.gist) : s.title}</span>
          </span>
          <span className="ls-receipt-meta">{s.typeLabel} · {s.dateLabel}</span>
          <span className="ls-row-end">{cite([n], ctx)}</span>
        </li>
      );
    }),
  ];

  const windowNode = prose("Why now", sections.window);
  const deadlineRows = refs.urgency
    .map((n) => ({ n, d: futureDate(p.sources[n - 1], extract) }))
    .filter((x): x is { n: number; d: string } => x.d !== null)
    .sort((a, b) => a.d.localeCompare(b.d))
    .map(({ n, d }) => {
      const s = sources[n - 1];
      return (
        <li key={`d${n}`} className="ls-receipt">
          <span className="ls-receipt-main">
            <span className="ls-receipt-fig">{fmtDate(d)}</span>
            <span className="ls-receipt-who">{s.gist ? capitalize(s.gist) : s.title}</span>
          </span>
          <span className="ls-receipt-meta">{s.typeLabel}</span>
          <span className="ls-row-end">{cite([n], ctx)}</span>
        </li>
      );
    });
  const windowFact = refs.urgency
    .map((n) => futureDate(p.sources[n - 1], extract))
    .filter((d): d is string => d !== null)
    .sort()[0];

  const movesNode = prose("First moves", sections.firstmoves);

  const hasCompetition = locals.length > 0 || !!sections.competition;
  const anchors: Record<Dim, string> = {
    proof: "#proven-abroad",
    gap: hasCompetition ? "#local-competition" : "#problem",
    demand: "#problem",
    money: "#who-pays",
    urgency: "#why-now",
  };

  // ---- opportunity: most filled bars first, then the LONGER bar (its max),
  //      then the fixed order (owner, round 3: "Why now should be mentioned
  //      second — it has 3 bars max; longer bars are first"). Never the ratio.
  const dimRows = SCORE_ROWS.map((r, i) => ({ ...r, i }))
    .sort((a, b) => p.scores[b.dim] - p.scores[a.dim] || MAX[b.dim] - MAX[a.dim] || a.i - b.i);
  const uSplit = urgencySplit(p);
  const band = BANDS.find((b) => p.score >= b.min)!;
  // rail, under the Opportunity card: who is in the room, as the gap rule
  // reads it. Null when no local player is on file.
  const fieldGridFig = FieldGrid({ p });

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
  // "Close" is the owner's "under ~6 months": the only time Window is tinted.
  const windowSoon = windowFact ? daysAfter(windowFact, extract) < 183 : false;

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

  const typeGroups = mix.map(([t]) => ({ t, list: sources.filter((s) => s.typeLabel === t) }));

  return (
    <div className="lab ls">
      <header className="ls-bar">
        <nav className="ls-crumbs" aria-label="Breadcrumb">
          <a href="/lab/modern">Problems</a>
          <span className="ls-sep" aria-hidden="true">/</span>
          <span className="ls-crumb-id">{p.id.toUpperCase()}</span>
        </nav>
      </header>

      <div className="ls-shell">
        {/* The head: art, title, and every record fact — each stated once. */}
        <header className="ls-head">
          <CategoryArt category={p.category} className="ls-art" />
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
            <div><dt>Locality</dt><dd>{localityLong(p.geo)}</dd></div>
            {/* A brief states why it is urgent by definition, so beside one the
                Window would say the same thing twice; without one, it stays. */}
            {windowFact && !brief && (
              <div>
                <dt>Window</dt>
                <dd>
                  <time
                    className={windowSoon ? "ls-soon" : undefined}
                    dateTime={windowFact}
                    title={`Nearest deadline: ${fmtDate(windowFact)}${windowSoon ? " — under six months away" : ""}`}
                  >
                    {relativeOut(extract, windowFact)}
                  </time>
                </dd>
              </div>
            )}
            <div>
              <dt>Entry</dt>
              <dd>
                <a className="ls-facts-link ls-level" data-level={entry.level} href="#difficulty-to-enter">
                  {ENTRY_LEVEL_LABELS[entry.level]}
                </a>
              </dd>
            </div>
            <div><dt>Verified</dt><dd><time dateTime={p.updated}>{fmtDate(p.updated)}</time></dd></div>
          </dl>
        </header>

        {/* THE RAIL BEFORE MAIN IN THE SOURCE (audit B13): a keyboard reaches
            the scorecard right after the head, not after every section.
            Grid areas keep it drawn in the right column; in one column
            (problem.css ≤1080px) reading-flow puts it back after main. */}
        <aside className="ls-rail" aria-label="Opportunity and evidence">
          {/* the card carries the total's anchor: its tip hangs off the card's
              edge, level with the header, never over the rows */}
          <section className="ls-card" aria-labelledby="ls-opp-h" style={{ anchorName: "--ls-t-total" } as CSSProperties}>
            <div className="ls-card-hd">
              <h2 id="ls-opp-h" className="ls-eyebrow">Opportunity</h2>
              <span className="ls-score ls-tip-host" tabIndex={0} aria-describedby="ls-tip-total">
                <b>{p.score}</b>/12
                <span className="ls-tip" id="ls-tip-total" aria-hidden="true" style={{ positionAnchor: "--ls-t-total" } as CSSProperties}>
                  <span className="ls-tip-t">Opportunity</span>
                  <span className="ls-tip-p">The sum of five checks, each point backed by a source.</span>
                  <span className="ls-ladder ls-ladder--bands">
                    {BANDS.map((b) => (
                      <span key={b.range} className={b === band ? "ls-rung is-here" : "ls-rung"}>
                        <span className="ls-rung-n">{b.range}</span>{b.text}
                      </span>
                    ))}
                  </span>
                  <span className="ls-tip-here">This record: {p.score} of 12.</span>
                </span>
              </span>
            </div>
            <ul className="ls-dims">
              {dimRows.map(({ dim, label: l }) => {
                const info = DIM_INFO[dim];
                const n = p.scores[dim];
                // urgency's rung is its deadline part; freshness is its own line
                const rung = dim === "urgency" ? uSplit.deadline : n;
                return (
                  <li key={dim}>
                    <a
                      href={anchors[dim]}
                      className={n === 0 ? "ls-dim ls-tip-host is-zero" : "ls-dim ls-tip-host"}
                      aria-describedby={`ls-tip-${dim}`}
                      style={{ anchorName: `--ls-t-${dim}` } as CSSProperties}
                    >
                      <span className="ls-dim-l">{l}</span>
                      <span className="ls-pips" aria-hidden="true">
                        {Array.from({ length: MAX[dim] }, (_, i) => (
                          <span key={i} className={i < n ? "on" : undefined} />
                        ))}
                      </span>
                      <span className="ls-dim-n">{n}/{MAX[dim]}</span>
                      <span className="ls-tip" id={`ls-tip-${dim}`} aria-hidden="true" style={{ positionAnchor: `--ls-t-${dim}` } as CSSProperties}>
                        <span className="ls-tip-t">{l}</span>
                        <span className="ls-tip-p"><b>{info.ask}</b> {info.why}</span>
                        <span className="ls-ladder">
                          {info.ladder.map((text, i) => (
                            <span key={i} className={i === rung ? "ls-rung is-here" : "ls-rung"}>
                              <span className="ls-rung-n">{i}</span>{text}
                            </span>
                          ))}
                          {dim === "urgency" && (
                            <span className={uSplit.freshness ? "ls-rung is-here" : "ls-rung"}>
                              <span className="ls-rung-n">+1</span>the newest evidence is under 90 days old
                            </span>
                          )}
                        </span>
                        <span className="ls-tip-here">This record: {sentence(scoreRead(p, dim))} {n} of {MAX[dim]}.</span>
                      </span>
                    </a>
                  </li>
                );
              })}
            </ul>
          </section>

          {fieldGridFig && (
            <section className="ls-card" aria-labelledby="ls-field-h">
              <div className="ls-card-hd">
                <h2 id="ls-field-h" className="ls-eyebrow">Who is here</h2>
              </div>
              {fieldGridFig}
            </section>
          )}

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
          <Section id="problem" title="The problem">
            {problemNode}
            {processTodayFig && <div className="ls-fig">{processTodayFig}</div>}
          </Section>

          <aside className="ls-solution" aria-label="Suggested solution">
            <p className="ls-solution-k">Suggested solution</p>
            <p className="ls-solution-v">{solutionNode}</p>
            {processAfterFig}
          </aside>

          <Section id="proven-abroad" title="Proven abroad" count={comps.length || undefined}>
            {solvedNode}
            {compMapFig && <div className="ls-fig">{compMapFig}</div>}
            {comps.length > 0 ? (
              <div className="ls-grp">
                <div className="ls-grp-h">
                  <p className="ls-grp-t">Abroad</p>
                  <p className="ls-grp-n">{comps.length} {comps.length === 1 ? "company" : "companies"}</p>
                </div>
                <ul className="ls-ents">{compRows}</ul>
              </div>
            ) : <p className="ls-absent">No verified foreign comparable on file.</p>}
          </Section>

          {hasCompetition && (
            <Section id="local-competition" title="Local competition" count={locals.length || undefined}>
              {fieldFig && <div className="ls-fig ls-fig--head">{fieldFig}</div>}
              {competitionNode}
              {localGroups}
            </Section>
          )}

          <Section id="who-pays" alias="how-big" title="Who pays">
            {whoPaysNode}
            {moneyFig && <div className="ls-fig">{moneyFig}</div>}
            {priceRows.length > 0 && (
              <div className="ls-group">
                <p className="ls-group-h">What buyers pay</p>
                <ul className="ls-receipts">{priceRows}</ul>
              </div>
            )}
            {moneyRowNodes.length > 0 && (
              <details className="ls-group ls-more">
                <summary className="ls-group-h">
                  Public money nearby <span className="ls-count">{moneyRowNodes.length}</span>
                </summary>
                <ul className="ls-receipts">{moneyRowNodes}</ul>
              </details>
            )}
            {priceRows.length === 0 && moneyRowNodes.length === 0 && (
              <p className="ls-absent">No sized figure on file.</p>
            )}
            {prices.length === 0 && p.score >= 7 && (
              <p className="ls-absent">
                No Czech buyer has priced this yet.{p.price_search && ` Where to look: ${p.price_search}`}
              </p>
            )}
          </Section>

          <Section id="why-now" title="Why now">
            {windowNode}
            {p.scores.urgency > 0 && deadlineRows.length > 0 && (
              <div className="ls-group">
                <p className="ls-group-h">Dates on file</p>
                <ul className="ls-receipts">{deadlineRows}</ul>
              </div>
            )}
          </Section>

          {/* A LEVEL DECIDED BY FOUR GATES — answer first, then what sets it,
              then the gates with their weights, then the one gate that is
              context only, then the record's own reasoning. */}
          <Section id="difficulty-to-enter" title="Difficulty to enter">
            <p className="ls-entry-level ls-level" data-level={entry.level}>{ENTRY_LEVEL_LABELS[entry.level]}</p>
            <p className="ls-entry-why">{entryReason}</p>
            <p className="ls-entry-note">
              Already here: {ENTRY_INCUMBENT_LABELS[entry.incumbents]}. That counts under{" "}
              {hasCompetition ? <a className="ls-link" href="#local-competition">Local competition</a> : "Local opportunity"}, not in this level.
            </p>
          </Section>

          {movesNode && <Section id="first-moves" title="First moves">{movesNode}</Section>}
        </main>

      </div>

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
            <div key={t} className="ls-drawer-group">
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
