// /lab/front — the register as a calm, readable list (owner, 2026-09-10: "just
// thinking about the frontpage, to be easy to consume for users who want to
// read thru"). A Linear-style experiment: one font, grays doing the work, one
// row per problem. LOCAL ONLY — the /lab layout 404s every route without
// LP_ADMIN=1, and this page checks again before any data is read.
//
// THE READING CONTRACT: a reader who reads only the two lines of every row —
// the title and the "Likely solution" under it — has read the whole register.
// Everything else (category, deadline, the peek) is there to be skipped.
//
// Every word on a row is derived, never written for this page, using exactly
// the derivations of the newspaper prototype at app/front/page.tsx: title =
// the record title, the peek's "The problem" = the problem section's run-in
// lead (`splitLead`), "Who pays" = the dek, the scorecard lines = the vetted
// `scoreRead` reads under the public `SCORE_ROWS` labels, and the deadline =
// the earliest future date among the urgency sources, measured against the
// register's own extract date (never the wall clock).
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import "./front.css";
import { extractDate, getSignal, registerRows, type Problem, type ProblemSource } from "../../../lib/data";
import { categoryLabel, countryName, localityLabel } from "../../../lib/format";
import { BANDS, dimRefs, MAX, SCORE_ROWS, scoreRead } from "../../../lib/scorecard";
import { splitBody, splitLead } from "../../../lib/sections";
import { CORRECTIONS_MAILTO } from "../../../lib/chrome";

export const metadata: Metadata = { title: "Front (lab) — localproblems.org" };

const enabled = () => process.env.LP_ADMIN === "1";

// ---- derivations (copied from app/front/page.tsx; only the design differs) --

/** Citation markers and markdown out: a row's one link is the record. */
const plain = (s: string) =>
  s
    .replace(/\s*\[S\d+(?:\s*,\s*S\d+)*\]/g, "")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\s+/g, " ")
    .trim();

/** The record page's buildability vocabulary (CONVENTIONS.md capital ladder). */
const CAPITAL: Record<string, string> = { kiosk: "<€10k", garage: "€10–100k", funded: "€100k–1M", industrial: ">€1M" };
const REVENUE: Record<string, string> = { weeks: "weeks", months: "months", "year-plus": "a year or more" };
const TEAM: Record<string, string> = { solo: "1 person", "small-team": "2–5 people", "funded-team": "a funded team" };

const days = (from: string, to: string) => Math.round((Date.parse(to) - Date.parse(from)) / 86_400_000);

/** Distance to a future date against the extract date — never the wall clock. */
function out(from: string, to: string): string {
  const d = days(from, to);
  const m = Math.round(d / 30.44);
  if (m < 1) { const w = Math.max(1, Math.round(d / 7)); return `${w} wk`; }
  if (m < 12) return `${m} mo`;
  return `${Math.round((m / 12) * 10) / 10} yr`;
}

function futureDate(s: ProblemSource, extract: string): string | null {
  if (s.date > extract) return s.date;
  const sig = s.signal ? getSignal(s.signal) : undefined;
  return sig && sig.date > extract ? sig.date : null;
}

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
/** `2026-12-31` → `31 Dec 2026`. String arithmetic, no Intl, no time zone. */
const shortDate = (iso: string) => `${Number(iso.slice(8, 10))} ${MONTHS[Number(iso.slice(5, 7)) - 1]} ${iso.slice(0, 4)}`;

/** HQ countries of the foreign comparables, in ledger order, spelt out. */
function countries(p: Problem): string {
  const names = [...new Set((p.comps ?? []).map((c) => countryName(c.geo)))];
  return names.length <= 3 ? names.join(", ") : `${names.slice(0, 3).join(", ")} +${names.length - 3}`;
}

type Item = {
  p: Problem;
  href: string;
  peekId: string;
  lede: string;
  dek: string;
  solution: string;
  window: string | null;
};

function item(p: Problem, extract: string): Item {
  const s = splitBody(p.body);
  const window = dimRefs(p).urgency
    .map((n) => futureDate(p.sources[n - 1], extract))
    .filter((d): d is string => d !== null)
    .sort()[0] ?? null;
  return {
    p,
    href: `/lab/problem/${p.region}/${p.id}`,
    peekId: `peek-${p.region}-${p.id}`,
    lede: plain(splitLead(s.problem).lead),
    dek: plain(s.dek),
    solution: plain(p.solution),
    window,
  };
}

// ---- grouping (Linear's "group by", as plain links: works without JS) -------

const GROUPINGS = [
  { key: "opportunity", label: "Opportunity" },
  { key: "category", label: "Category" },
  { key: "deadline", label: "Deadline" },
] as const;
type GroupKey = (typeof GROUPINGS)[number]["key"];
type Group = { id: string; label: string; items: Item[] };

/** Opportunity bands at the SCORING.md band thresholds, stated as numbers —
    the band words themselves are rubric vocabulary the public pages retired. */
function byOpportunity(items: Item[]): Group[] {
  const mins = BANDS.map(([min]) => min); // [10, 8, 5, 0]
  return mins.map((min, i) => {
    const max = i === 0 ? 12 : mins[i - 1] - 1;
    return {
      id: `score-${min}`,
      label: `Opportunity ${min}–${max}`,
      items: items.filter((it) => it.p.score >= min && it.p.score <= max),
    };
  }).filter((g) => g.items.length > 0);
}

/** Categories in the order their best problem appears in the register. */
function byCategory(items: Item[]): Group[] {
  const order: string[] = [];
  for (const it of items) if (!order.includes(it.p.category)) order.push(it.p.category);
  return order.map((c) => ({ id: `cat-${c}`, label: categoryLabel(c), items: items.filter((it) => it.p.category === c) }));
}

/** Soonest first; a record with no dated deadline says so rather than hiding. */
function byDeadline(items: Item[], extract: string): Group[] {
  const dated = items.filter((it) => it.window !== null).sort((a, b) => a.window!.localeCompare(b.window!));
  const within = (lo: number, hi: number) => dated.filter((it) => { const d = days(extract, it.window!); return d > lo && d <= hi; });
  return [
    { id: "due-3", label: "Within 3 months", items: within(-Infinity, 92) },
    { id: "due-12", label: "Within a year", items: within(92, 366) },
    { id: "due-later", label: "Later", items: within(366, Infinity) },
    { id: "due-none", label: "No dated deadline on file", items: items.filter((it) => it.window === null) },
  ].filter((g) => g.items.length > 0);
}

// ---- pieces ------------------------------------------------------------------

/** Opportunity as a gray tier: the stronger the score, the darker the number. */
const tier = (score: number) => (score >= 10 ? "t1" : score >= 8 ? "t2" : score >= 5 ? "t3" : "t4");

function Meter({ value, max }: { value: number; max: number }) {
  return (
    <span className="lf-meter" role="img" aria-label={`${value} of ${max}`}>
      {Array.from({ length: max }, (_, i) => <i key={i} className={i < value ? "on" : undefined} />)}
    </span>
  );
}

function Peek({ it, extract }: { it: Item; extract: string }) {
  const { p } = it;
  const titleId = `${it.peekId}-title`;
  return (
    <div popover="auto" id={it.peekId} className="lf-peek" role="dialog" aria-labelledby={titleId}>
      <div className="lf-pk-bar">
        <span>{categoryLabel(p.category)}</span>
        <span className="sep">/</span>
        <span>{localityLabel(p.geo)}</span>
        <span className="sep">/</span>
        <span className="id">{p.id.toUpperCase()}</span>
        <button type="button" className="lf-btn lf-pk-close" popoverTarget={it.peekId} popoverTargetAction="hide">
          Close
        </button>
      </div>

      <div className="lf-pk-body">
        <h2 id={titleId} className="lf-pk-title">{p.title}</h2>

        <div className="lf-pk-sol">
          <p className="k">Likely solution</p>
          <p>{it.solution}</p>
        </div>

        <dl className="lf-pk-prose">
          {it.lede && (<><dt>The problem</dt><dd>{it.lede}</dd></>)}
          {it.dek && (<><dt>Who pays</dt><dd>{it.dek}</dd></>)}
        </dl>

        <h3 className="lf-pk-h">
          Opportunity <span className="num">{p.score}<span className="of">/12</span></span>
        </h3>
        <ul className="lf-props">
          {SCORE_ROWS.map(({ dim, label }) => (
            <li key={dim}>
              <span className="lbl">{label}</span>
              <span className="val">
                {scoreRead(p, dim)}
                {dim === "proof" && (p.comps?.length ?? 0) > 0 && <span className="sub">{countries(p)}</span>}
                {dim === "urgency" && it.window && (
                  <span className="sub">
                    Deadline <time dateTime={it.window}>{shortDate(it.window)}</time> · {out(extract, it.window)} out
                  </span>
                )}
              </span>
              <Meter value={p.scores[dim]} max={MAX[dim]} />
            </li>
          ))}
        </ul>

        <h3 className="lf-pk-h">What you need</h3>
        <ul className="lf-props lf-props--plain">
          <li><span className="lbl">Capital</span><span className="val">{CAPITAL[p.build.capital]}</span></li>
          <li><span className="lbl">Team</span><span className="val">{TEAM[p.build.builder]}</span></li>
          <li><span className="lbl">First revenue</span><span className="val">in {REVENUE[p.build.first_revenue]}</span></li>
        </ul>
      </div>

      <div className="lf-pk-foot">
        <span className="count">{p.sources.length} source{p.sources.length === 1 ? "" : "s"} on the record</span>
        <a className="lf-btn lf-btn--primary" href={it.href}>Open full record</a>
      </div>
    </div>
  );
}

function Row({ it, extract, showCategory }: { it: Item; extract: string; showCategory: boolean }) {
  const { p } = it;
  return (
    <li className="lf-row">
      <span className={`lf-score ${tier(p.score)}`}>
        <span className="sr">Opportunity </span>{p.score}<span className="of">/12</span>
      </span>
      <div className="lf-main">
        <h3 className="lf-title"><a href={it.href}>{p.title}</a></h3>
        <p className="lf-sol"><span className="k">Likely solution</span> {it.solution}</p>
      </div>
      {showCategory && <span className="lf-cat">{categoryLabel(p.category)}</span>}
      <span className="lf-due">
        {it.window && (
          <>
            <span className="sr">Deadline </span>
            <time dateTime={it.window}>{shortDate(it.window)}</time>
            <span className="rel">{out(extract, it.window)}</span>
          </>
        )}
      </span>
      <button type="button" className="lf-btn lf-peek-btn" popoverTarget={it.peekId} aria-label={`Preview: ${p.title}`}>
        Preview
      </button>
      <Peek it={it} extract={extract} />
    </li>
  );
}

// ---- page ----------------------------------------------------------------------

export default async function LabFront({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  if (!enabled()) notFound();
  const q = (await searchParams).group;
  const group: GroupKey = GROUPINGS.some((g) => g.key === q) ? (q as GroupKey) : "opportunity";

  const extract = extractDate();
  const items = registerRows().map((p) => item(p, extract));
  const groups =
    group === "category" ? byCategory(items) : group === "deadline" ? byDeadline(items, extract) : byOpportunity(items);
  const showCategory = group !== "category";

  const dated = items.filter((it) => it.window !== null).length;
  const sources = new Set(items.flatMap((it) => it.p.sources.map((s) => s.url))).size;
  const checks = SCORE_ROWS.map((r) => r.label.toLowerCase());
  const checkList = `${checks.slice(0, -1).join(", ")} and ${checks.at(-1)}`;

  return (
    <div className="lab lf">
      <header className="lf-bar">
        <div className="lf-bar-in">
          <a className="lf-brand" href="/">localproblems.org</a>
          <span className="lf-crumb">Czechia</span>
          <nav className="lf-nav" aria-label="Site">
            <a href="/lab/front" aria-current="page">Problems</a>
            <a href="/signals/funded">Signals</a>
            <a href="/about">About</a>
          </nav>
        </div>
      </header>

      <main className="lf-wrap">
        <section className="lf-intro">
          <h1>Czech problems worth solving</h1>
          <p className="lf-lede">
            A public register distilled from tenders, regulations, funding rounds and documented complaints.
            Each problem is paired with its likely solution, and every claim links to its source.
          </p>
          <p className="lf-stats">
            <span><b>{items.length}</b> problems</span>
            <span><b>{dated}</b> with a dated deadline</span>
            <span><b>{sources}</b> sources</span>
          </p>
        </section>

        <div className="lf-tools">
          <nav className="lf-seg" aria-label="Group problems by">
            <span className="lf-seg-label">Group by</span>
            <span className="lf-seg-track">
              {GROUPINGS.map((g) => (
                <a
                  key={g.key}
                  href={g.key === "opportunity" ? "/lab/front" : `/lab/front?group=${g.key}`}
                  aria-current={g.key === group ? "true" : undefined}
                >
                  {g.label}
                </a>
              ))}
            </span>
          </nav>
          <p className="lf-legend">
            Opportunity is scored out of 12 from five checks: {checkList}.
          </p>
        </div>

        <div className={showCategory ? "lf-list" : "lf-list lf-list--nocat"}>
          <div className="lf-head" aria-hidden="true">
            <span>Score</span>
            <span>Problem and likely solution</span>
            {showCategory && <span>Category</span>}
            <span>Deadline</span>
          </div>

          {groups.map((g) => (
            <section key={g.id} className="lf-group" aria-labelledby={`${g.id}-h`}>
              <h2 id={`${g.id}-h`} className="lf-group-h">
                {g.label}<span className="n">{g.items.length}</span>
              </h2>
              <ol className="lf-rows">
                {g.items.map((it) => (
                  <Row key={it.p.id} it={it} extract={extract} showCategory={showCategory} />
                ))}
              </ol>
            </section>
          ))}
        </div>
      </main>

      <footer className="lf-foot">
        <div className="lf-wrap lf-foot-in">
          <span>localproblems.org · Czechia</span>
          <a href={CORRECTIONS_MAILTO}>Report a correction</a>
        </div>
      </footer>
    </div>
  );
}
