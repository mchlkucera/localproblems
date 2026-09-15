// /lab/problem/[region]/[id] — the record page as a sources-first brief.
// LOCAL ONLY (the /lab layout 404s without LP_ADMIN=1). A design experiment in
// the Linear-like lab language: one font, a gray ramp, hierarchy from size,
// weight and shade. Its signature is the citation: a quiet publisher pill in
// the sentence that PEEKS into the source (who, what, when, why, and the
// source's own words) without leaving the line. See ../../cite.tsx.
//
// Reads exactly what the production record page reads (getProblems, splitBody,
// dimRefs, getSignal, extractDate as "today"); writes nothing.
import type { Metadata } from "next";
import type { ReactNode } from "react";
import { notFound } from "next/navigation";
import { extractDate, getProblems, getSignal, localHref, priceReceipts, signalHref, type Problem, type ProblemSource } from "../../../../../lib/data";
import { splitBody, splitLead, capitalize } from "../../../../../lib/sections";
import {
  ENTRY_BUYER_LABELS, ENTRY_INCUMBENT_LABELS, ENTRY_INTEGRATION_LABELS, ENTRY_LEVEL_LABELS,
  ENTRY_MONEY_LABELS, ENTRY_PERMISSION_LABELS, PRICE_BASIS_LABELS, PRICE_UNIT_LABELS,
  categoryLabel, countryName, czk, euro, localityLabel, localityLong,
} from "../../../../../lib/format";
import { MAX, SCORE_ROWS, dimRefs, scoreRead, type Dim } from "../../../../../lib/scorecard";
import { cite, newCtx, peekParts, type CiteCtx } from "../../cite";
import { Prose, inline, type ProseOpts } from "../../prose";
import { fmtDate, labSources, type LabSource } from "../../sources";
import { PeekHover } from "../../peek-hover";
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

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  if (!enabled()) return { title: "Record not found" };
  const { region, id } = await params;
  const p = find(region, id);
  return { title: p ? `${p.title} — lab` : "Record not found" };
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


/** A ledger note as scan-then-dive: first sentence/clause, the rest folds. */
function Note({ text, mode }: { text: string; mode: "sentence" | "clause" }) {
  const { lead, rest } = splitLead(text, mode);
  if (!rest) return <p className="ls-note">{text}</p>;
  return (
    <details className="ls-fold">
      <summary className="ls-note">{lead}</summary>
      <p className="ls-note ls-note--rest">{capitalize(rest)}</p>
    </details>
  );
}

function Section({ id, title, count, children }: { id: string; title: string; count?: ReactNode; children: ReactNode }) {
  return (
    <section className="ls-sec" id={id} aria-labelledby={`${id}-h`}>
      <h2 className="ls-h2" id={`${id}-h`}>
        {title}
        {count != null && <span className="ls-h2-count">{count}</span>}
      </h2>
      {children}
    </section>
  );
}

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
  const bySignal = new Map<string, number>();
  p.sources.forEach((s, i) => s.signal && !bySignal.has(s.signal) && bySignal.set(s.signal, i + 1));

  // EVERY SECTION IS BUILT BEFORE THE JSX, IN READING ORDER: building one
  // records its citations into ctx, and the strip at the top of the page needs
  // the finished counts ("most cited") before it can be drawn.
  const prose = (section: string, md: string) => {
    ctx.section = section;
    return md ? Prose(md, ctx, { ...opts, lead: true }) : null;
  };

  const problemNode = prose("The problem", sections.problem);
  ctx.section = "Likely solution";
  const solutionNode = inline(p.solution, ctx, opts, "sol");

  const solvedNode = prose("Proven abroad", sections.solved);
  const compRows = comps.map((c) => {
    const n = c.signal ? bySignal.get(c.signal) : undefined;
    return (
      <li key={c.name} className="ls-row">
        <div className="ls-row-line">
          <a className="ls-row-name" href={c.url} target="_blank" rel="noopener noreferrer">{c.name}</a>
          <span className="ls-row-meta">{countryName(c.geo)} · since {c.since}</span>
          <span className="ls-row-end">{n ? cite([n], ctx) : null}</span>
        </div>
        <Note text={c.traction} mode="clause" />
      </li>
    );
  });

  const competitionNode = prose("Local competition", sections.competition);
  const localGroups = (["direct", "adjacent"] as const).map((competes) => {
    const group = locals.filter((l) => l.competes === competes);
    if (!group.length) return null;
    const heading = competes === "direct"
      ? `${group.length} sell${group.length === 1 ? "s" : ""} this`
      : `${group.length} nearby, selling something else`;
    return (
      <div key={competes} className="ls-group">
        <p className="ls-group-h">{heading}</p>
        <ul className="ls-rows">
          {group.map((l) => (
            <li key={l.name} className="ls-row">
              <div className="ls-row-line">
                <a className="ls-row-name" href={localHref(l)} target="_blank" rel="noopener noreferrer">{l.name}</a>
                <span className="ls-row-meta">{[l.ico && `IČO ${l.ico}`, l.since && `since ${l.since}`].filter(Boolean).join(" · ")}</span>
                <span className="ls-row-end"><span className="ls-tag ls-tag--cap">{l.maturity}</span></span>
              </div>
              <Note text={l.evidence} mode="sentence" />
            </li>
          ))}
        </ul>
      </div>
    );
  });

  const whoPaysMd = [sections.dek, sections.howbig].filter(Boolean).join(" ");
  const whoPaysNode = prose("Who pays", whoPaysMd);
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
          <span className="ls-receipt-meta">{relativeOut(extract, d)}</span>
          <span className="ls-row-end">{cite([n], ctx)}</span>
        </li>
      );
    });
  const windowFact = refs.urgency
    .map((n) => futureDate(p.sources[n - 1], extract))
    .filter((d): d is string => d !== null)
    .sort()[0];

  const movesNode = prose("First moves", sections.firstmoves);

  // ---- the strip: most-cited first, then S-order --------------------------
  const count = (n: number) => ctx.cited.get(n)?.length ?? 0;
  const ranked = [...sources].sort((a, b) => count(b.n) - count(a.n) || a.n - b.n);
  const top = ranked.slice(0, 3);
  const rest = sources.length - top.length;
  const stripCards = top.map((s) => {
    const { pill, peek } = peekParts([s.n], ctx, {
      record: false,
      className: "ls-scard",
      children: (
        <>
          <span className="ls-scard-title">{s.title}</span>
          <span className="ls-scard-foot">
            <span className="ls-mono" aria-hidden="true">{s.mono}</span>
            <span className="ls-scard-pub">{s.publisher}</span>
          </span>
        </>
      ),
    });
    return <li key={s.n} className="ls-strip-item">{pill}{peek}</li>;
  });

  // evidence mix for the rail — what KIND of sources hold this record up
  const mix = [...sources.reduce((m, s) => m.set(s.typeLabel, (m.get(s.typeLabel) ?? 0) + 1), new Map<string, number>())]
    .sort((a, b) => b[1] - a[1]);

  const anchors: Record<Dim, string> = {
    proof: "#proven-abroad",
    gap: locals.length || sections.competition ? "#local-competition" : "#sources",
    demand: "#problem",
    money: "#who-pays",
    urgency: "#why-now",
  };

  const entry = p.entry;
  const label = p.id.toUpperCase();

  // one row of the full list — used at the foot (with anchors) and in the drawer
  const ledgerRow = (s: LabSource, anchor: boolean) => {
    const where = [...new Set(ctx.cited.get(s.n) ?? [])];
    return (
      <li key={s.n} className="ls-src" id={anchor ? `s${s.n}` : undefined}>
        <span className="ls-src-n">{s.n}</span>
        <span className="ls-mono ls-mono--md" aria-hidden="true">{s.mono}</span>
        <div className="ls-src-body">
          <div className="ls-src-top">
            <span className="ls-src-pub">{s.publisher}</span>
            {s.host && s.host !== s.publisher && <span className="ls-src-host">{s.host}</span>}
            <span className="ls-src-date"><time dateTime={s.date}>{s.dateLabel}</time></span>
          </div>
          {s.url ? (
            <a className="ls-src-title" href={s.url} target="_blank" rel="noopener noreferrer">
              {s.title}<span className="ls-ext" aria-hidden="true">↗</span>
            </a>
          ) : (
            <span className="ls-src-title">{s.title}</span>
          )}
          {s.why && <p className="ls-src-why">{s.why}</p>}
          {anchor && s.quote && (
            <details className="ls-fold ls-src-quote">
              <summary>In the source’s words</summary>
              <blockquote>“{s.quote}”</blockquote>
            </details>
          )}
          <p className="ls-src-meta">
            <span className="ls-tag">{s.typeLabel}</span>
            <span>{where.length ? `Cited in ${where.join(", ")}` : "On file, not cited in the text"}</span>
          </p>
        </div>
      </li>
    );
  };

  const typeGroups = [...new Set(sources.map((s) => s.typeLabel))].map((t) => ({
    t,
    list: sources.filter((s) => s.typeLabel === t),
  })).sort((a, b) => b.list.length - a.list.length);

  return (
    <div className="lab ls">
      <header className="ls-bar">
        <nav className="ls-crumbs" aria-label="Breadcrumb">
          <a href="/lab/front">Problems</a>
          <span className="ls-sep" aria-hidden="true">/</span>
          <span>{countryName(p.region.toUpperCase())}</span>
          <span className="ls-sep" aria-hidden="true">/</span>
          <span>{categoryLabel(p.category)}</span>
          <span className="ls-sep" aria-hidden="true">/</span>
          <span className="ls-crumb-id">{label}</span>
        </nav>
        <span className="ls-bar-meta">Verified <time dateTime={p.updated}>{fmtDate(p.updated)}</time></span>
      </header>

      <div className="ls-shell">
        <main className="ls-main">
          <header className="ls-head">
            <h1 className="ls-h1">{p.title}</h1>
            <p className="ls-sub">
              <span>{label}</span>
              <span>{categoryLabel(p.category)}</span>
              <span>{localityLabel(p.geo)}</span>
              <span className="ls-sub-score">Opportunity {p.score}/12</span>
            </p>
          </header>

          <section className="ls-strip" aria-labelledby="ls-strip-h">
            <div className="ls-strip-hd">
              <h2 id="ls-strip-h" className="ls-eyebrow">Sources <span className="ls-count">{sources.length}</span></h2>
              <span className="ls-strip-hint">Most cited on this page</span>
            </div>
            <ul className="ls-strip-row">
              {stripCards}
              {rest > 0 && (
                <li className="ls-strip-item">
                  <button type="button" className="ls-scard ls-scard--all" popoverTarget="ls-all">
                    <span className="ls-stack" aria-hidden="true">
                      {ranked.slice(3, 7).map((s) => <span key={s.n} className="ls-mono">{s.mono}</span>)}
                    </span>
                    <span className="ls-scard-title">View all {sources.length}</span>
                    <span className="ls-scard-foot"><span className="ls-scard-pub">+{rest} more</span></span>
                  </button>
                </li>
              )}
            </ul>
          </section>

          <Section id="problem" title="The problem">{problemNode}</Section>

          <aside className="ls-solution" aria-label="Likely solution">
            <p className="ls-solution-k">Likely solution</p>
            <p className="ls-solution-v">{solutionNode}</p>
          </aside>

          <Section id="proven-abroad" title="Proven abroad" count={comps.length || undefined}>
            {solvedNode}
            {comps.length > 0 ? <ul className="ls-rows">{compRows}</ul> : <p className="ls-absent">No verified foreign comparable on file.</p>}
          </Section>

          {(locals.length > 0 || sections.competition) && (
            <Section id="local-competition" title="Local competition" count={locals.length || undefined}>
              {competitionNode}
              {localGroups}
            </Section>
          )}

          <Section id="who-pays" title="Who pays">
            {whoPaysNode}
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

          <Section id="difficulty-to-enter" title="Difficulty to enter">
            <dl className="ls-facts">
              <div><dt>Level</dt><dd>{ENTRY_LEVEL_LABELS[entry.level]}</dd></div>
              <div><dt>Who buys</dt><dd>{ENTRY_BUYER_LABELS[entry.buyer]}</dd></div>
              <div><dt>Permission</dt><dd>{ENTRY_PERMISSION_LABELS[entry.permission]}</dd></div>
              <div><dt>Already here</dt><dd>{ENTRY_INCUMBENT_LABELS[entry.incumbents]}</dd></div>
              <div><dt>Plug into</dt><dd>{ENTRY_INTEGRATION_LABELS[entry.integration]}</dd></div>
              <div><dt>Money</dt><dd>{ENTRY_MONEY_LABELS[entry.money]}</dd></div>
            </dl>
            <p className="ls-p ls-p--quiet">{entry.why}</p>
          </Section>

          {movesNode && <Section id="first-moves" title="First moves">{movesNode}</Section>}

          <section className="ls-sec ls-ledger" id="sources" aria-labelledby="sources-h">
            <h2 className="ls-h2" id="sources-h">Sources<span className="ls-h2-count">{sources.length}</span></h2>
            <p className="ls-ledger-intro">Every source on file for this record, in citation order. Each pill in the text above opens a preview of the source it cites.</p>
            <ol className="ls-srcs">
              {sources.map((s) => ledgerRow(s, true))}
            </ol>
          </section>
        </main>

        <aside className="ls-rail" aria-label="Record properties">
          <div className="ls-card">
            <div className="ls-card-hd">
              <span className="ls-eyebrow">Opportunity</span>
              <span className="ls-score"><b>{p.score}</b>/12</span>
            </div>
            <ul className="ls-dims">
              {SCORE_ROWS.map(({ dim, label: l }) => (
                <li key={dim}>
                  <a href={anchors[dim]} className={p.scores[dim] === 0 ? "ls-dim is-zero" : "ls-dim"} title={scoreRead(p, dim)}>
                    <span className="ls-dim-l">{l}</span>
                    <span className="ls-pips" aria-hidden="true">
                      {Array.from({ length: MAX[dim] }, (_, i) => (
                        <span key={i} className={i < p.scores[dim] ? "on" : undefined} />
                      ))}
                    </span>
                    <span className="ls-dim-n">{p.scores[dim]}/{MAX[dim]}</span>
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <dl className="ls-props">
            <div><dt>Category</dt><dd>{categoryLabel(p.category)}</dd></div>
            <div><dt>Locality</dt><dd>{localityLong(p.geo)}</dd></div>
            {windowFact && <div><dt>Window</dt><dd><time dateTime={windowFact} title={`by ${fmtDate(windowFact)}`}>{relativeOut(extract, windowFact)}</time></dd></div>}
            <div><dt>Entry</dt><dd>{ENTRY_LEVEL_LABELS[entry.level]}</dd></div>
            <div><dt>Verified</dt><dd><time dateTime={p.updated}>{fmtDate(p.updated)}</time></dd></div>
          </dl>

          <div className="ls-mix">
            <p className="ls-eyebrow">Evidence <span className="ls-count">{sources.length}</span></p>
            <ul>
              {mix.map(([t, n]) => (
                <li key={t}>
                  <span className="ls-mix-l">{t}</span>
                  <span className="ls-mix-bar" aria-hidden="true"><span style={{ width: `${(n / mix[0][1]) * 100}%` }} /></span>
                  <span className="ls-mix-n">{n}</span>
                </li>
              ))}
            </ul>
            <button type="button" className="ls-btn" popoverTarget="ls-all">View all sources</button>
          </div>
        </aside>
      </div>

      {/* The "view all" drawer — the strip's expansion, grouped by kind. */}
      <div id="ls-all" popover="auto" className="ls-drawer" role="dialog" aria-labelledby="ls-all-h">
        <div className="ls-drawer-hd">
          <h2 id="ls-all-h" className="ls-drawer-t">Sources <span className="ls-count">{sources.length}</span></h2>
          <button type="button" className="ls-x" popoverTarget="ls-all" popoverTargetAction="hide" aria-label="Close">×</button>
        </div>
        <div className="ls-drawer-body">
          {typeGroups.map(({ t, list }) => (
            <div key={t} className="ls-drawer-group">
              <p className="ls-group-h">{t} <span className="ls-count">{list.length}</span></p>
              <ol className="ls-srcs ls-srcs--compact">
                {list.map((s) => ledgerRow(s, false))}
              </ol>
            </div>
          ))}
          <a className="ls-drawer-foot" href="#sources" data-peek-close="">Go to the full list at the foot of the page ↓</a>
        </div>
      </div>

      <PeekHover />
    </div>
  );
}

