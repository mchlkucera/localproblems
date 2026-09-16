// /signals — one evidence ledger, one page of it, in the modern
// design. The port of lib/ledger.tsx (the live `/signals/[type]` pages): the
// SAME data (`ledgerRows`, `ledgerPages`), the same 100-row pages
// (`LEDGER_PAGE_SIZE`), the same one-paragraph description per type
// (`DESCRIPTIONS`, imported, never restated), the same row anchors (each row's
// id IS its signal id, because `signalHref` deep links land on it) and the same
// honest empty state. Only the design differs.
//
// DESIGN: the front page's grid (app/(site)/styles/front.css). The rail names the month the
// rows below it were dated in, sticky while they scroll past; the column is a
// ruled list, newest first. A row is three text styles, stepped down for a
// ledger (design-language §2: "rail and ledger text step down to the 13px and
// 12px tokens"): the title 15/24 500, the summary 13/20, one meta line 12px.
// The title is the source and leaves the site, so it is ink blue and ends in ↗
// (§3, §10.12). No table, so nothing scrolls sideways on a phone.
//
// ONE ORDER, NO SORT SCRIPT, for the reason lib/ledger.tsx gives: a page holds
// 100 of thousands of rows, and a client sort over the slice would look like a
// sort of the ledger. The order (date, newest first) is stated for assistive
// tech; the dates show it to everyone else.
import type { Metadata } from "next";
import {
  EVIDENCE_TYPES, extractDate, ledgerPages, ledgerRows,
  type EvidenceType, type Signal,
} from "../data";
import { DESCRIPTIONS, SOURCE_LABELS, TITLES } from "../ledger";
import { categoryLabel, countryName, euro } from "../format";
import { CORRECTIONS_MAILTO } from "../chrome";
import { fmtDate } from "./sources";
import { TopBar } from "./bar";


/** "Funded", from "Funded — companies founded and financed". */
export const shortTitle = (type: EvidenceType) => TITLES[type].split(" — ")[0];

export const BASE = "/signals";
/** Page 1 keeps the bare URL; there is no `/1`, so no document has two addresses. */
const pageHref = (type: EvidenceType, n: number) => (n === 1 ? `${BASE}/${type}` : `${BASE}/${type}/${n}`);

export function ledgerMetadata(type: EvidenceType, page: number): Metadata {
  const pages = ledgerPages(type);
  const where = pages > 1 && page > 1 ? `, page ${page} of ${pages}` : "";
  return {
    title: `${shortTitle(type)} signals${where} — localproblems.org`,
    description: DESCRIPTIONS[type],
  };
}

const MONTHS = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];

/** Consecutive rows that share a month, in ledger order. Parsed from the ISO
    string, never through `Date`, so no time zone can move a row a month. */
function byMonth(rows: Signal[]): { key: string; label: string; rows: Signal[] }[] {
  const groups: { key: string; label: string; rows: Signal[] }[] = [];
  for (const s of rows) {
    const key = s.date.slice(0, 7);
    const last = groups.at(-1);
    if (last && last.key === key) last.rows.push(s);
    else {
      const [y, m] = key.split("-").map(Number);
      groups.push({ key, label: m ? `${MONTHS[m - 1]} ${y}` : key, rows: [s] });
    }
  }
  return groups;
}

/** Where a signal came from: the feed, or the country for a market scan (as the
    live Source column has it), then who asked, for an ask (`owner` is set on
    every asks row and on no other). */
function origin(s: Signal): string {
  const feed = s.source === "arb-scan" ? countryName(s.geo_origin) : SOURCE_LABELS[s.source] ?? s.source;
  return s.owner ? `${feed} · ${s.owner}` : feed;
}

/** §7.3: an llm-fallback row is flagged for review on the ledger, never
    silently trusted; `structured` is the default and earns no mark. */
function extraction(s: Signal): string | null {
  if (!s.extraction || s.extraction === "structured") return null;
  return s.extraction === "llm-fallback" ? "Read by LLM" : "Entered by hand";
}

function Row({ s }: { s: Signal }) {
  const flag = extraction(s);
  return (
    <li className="lg-row" id={s.id}>
      <h3 className="lg-title">
        {/* the verbatim quote rides in the native title, as on the live ledger */}
        <a href={s.url} target="_blank" rel="noopener noreferrer" title={s.quote ? `“${s.quote}”` : undefined}>
          {s.title}
          <span className="lg-ext" aria-hidden="true">{" ↗"}</span>
          <span className="lf-sr"> (another site)</span>
        </a>
      </h3>
      <p className="lg-sum">{s.summary}</p>
      <p className="lg-meta">
        <time dateTime={s.date}>{fmtDate(s.date)}</time>
        <span>{origin(s)}</span>
        <span>{categoryLabel(s.sector)}</span>
        {s.source !== "arb-scan" && <span>{countryName(s.geo_origin)}</span>}
        {s.money_eur != null && <span>{euro(s.money_eur)}</span>}
        {flag && <span>{flag}</span>}
      </p>
    </li>
  );
}

/** Page numbers to show: the first, the last, and the current page with one
    either side; `null` marks a gap. Seven slots at most. */
function pageWindow(page: number, pages: number): (number | null)[] {
  const want = new Set([1, pages, page - 1, page, page + 1].filter((n) => n >= 1 && n <= pages));
  const sorted = [...want].sort((a, b) => a - b);
  const out: (number | null)[] = [];
  sorted.forEach((n, i) => {
    if (i > 0 && n - sorted[i - 1] > 1) out.push(null);
    out.push(n);
  });
  return out;
}

/** The quiet pager: Previous · numbers · Next. On a phone the numbers give way
    to "Page n of N". A one-page ledger has nothing to page. */
function Pager({ type, page, pages }: { type: EvidenceType; page: number; pages: number }) {
  if (pages < 2) return null;
  return (
    <nav className="lg-pager" aria-label="Ledger pages">
      {page > 1
        ? <a className="lg-step" rel="prev" href={pageHref(type, page - 1)}>← Previous</a>
        : <span className="lg-step is-off" aria-hidden="true">← Previous</span>}
      <ol className="lg-pages">
        {pageWindow(page, pages).map((n, i) =>
          n === null
            ? <li key={`gap-${i}`} className="lg-gap" aria-hidden="true">…</li>
            : (
              <li key={n}>
                <a href={pageHref(type, n)} aria-current={n === page ? "page" : undefined}>
                  <span className="lf-sr">Page </span>{n}
                </a>
              </li>
            ),
        )}
      </ol>
      <span className="lg-pos" aria-hidden="true">Page {page} of {pages}</span>
      {page < pages
        ? <a className="lg-step" rel="next" href={pageHref(type, page + 1)}>Next →</a>
        : <span className="lg-step is-off" aria-hidden="true">Next →</span>}
    </nav>
  );
}

/** The six ledgers, as the front page's tabs: plain links, the current one
    underlined. They wrap rather than scroll, so a phone never scrolls sideways. */
function LedgerTabs({ current }: { current: EvidenceType }) {
  return (
    <nav className="lg-tabs" aria-label="Signal ledgers">
      {EVIDENCE_TYPES.map((t) => (
        <a key={t} href={pageHref(t, 1)} aria-current={t === current ? "page" : undefined}>
          {shortTitle(t)}
        </a>
      ))}
    </nav>
  );
}

export function LedgerPage({ type, page }: { type: EvidenceType; page: number }) {
  const pages = ledgerPages(type);
  const rows = ledgerRows(type, page);

  return (
    <div className="lab lf lg">
      {/* bar.tsx has no "signals" page value yet, so no link is marked current */}
      <TopBar current="signals" />

      <main className="lf-wrap">
        <header className="lg-head">
          <h1>{shortTitle(type)}</h1>
          <p className="lg-lede">{DESCRIPTIONS[type]}</p>
        </header>

        <LedgerTabs current={type} />

        {rows.length === 0 ? (
          <p className="lg-empty">
            Nothing in this ledger as of <time dateTime={extractDate()}>{fmtDate(extractDate())}</time>.
            The feed is registered but not yet producing.
          </p>
        ) : (
          <>
            <p className="lf-sr">
              Sorted by date, newest first{pages > 1 && `, page ${page} of ${pages}`}.
            </p>
            {byMonth(rows).map((g) => (
              <section key={g.key} className="lf-sec lg-sec" aria-labelledby={`m-${g.key}`}>
                <header className="lf-sec-h">
                  <h2 id={`m-${g.key}`}>{g.label}</h2>
                  {/* a count of the rows beside it, never of the month: a
                      month can run on across a page break */}
                  <p>{g.rows.length} {pages > 1 ? "on this page" : g.rows.length === 1 ? "signal" : "signals"}</p>
                </header>
                <ol className="lg-rows">
                  {g.rows.map((s) => <Row key={s.id} s={s} />)}
                </ol>
              </section>
            ))}
          </>
        )}

        <Pager type={type} page={page} pages={pages} />
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
