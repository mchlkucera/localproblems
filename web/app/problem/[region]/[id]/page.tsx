// The record page — docket · scorecard · rundowns · prose · sources · claim · provenance.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getProblems, getSignal, type Problem } from "../../../../lib/data";
import { renderBody } from "../../../../lib/md";
import { categoryLabel, localityLong, pad2 } from "../../../../lib/format";
import { DIMS, MAX, VERDICTS, bandWord, criterion, dimRefs, type Dim } from "../../../../lib/scorecard";
import {
  CORRECTIONS_MAILTO, FooterHouseLine, Masthead, RelDatesScript, StatusDot, Tally,
} from "../../../../lib/chrome";

export const dynamicParams = false;

export function generateStaticParams() {
  return getProblems().map((p) => ({ region: p.region, id: p.id }));
}

type Params = { params: Promise<{ region: string; id: string }> };

function find(region: string, id: string): Problem | undefined {
  return getProblems().find((p) => p.region === region && p.id === id);
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { region, id } = await params;
  const p = find(region, id);
  return { title: p ? `${p.id.toUpperCase()} · ${p.title} — localproblems.org` : "Record not found" };
}

const statusLine = (status: string) =>
  status === "claimed" ? "Claimed" :
  status === "solved" ? "Solved" :
  status === "stale" ? "Open — stale" : "Open — unclaimed";

function sourceName(s: Problem["sources"][number]): { label: string; url: string | null } {
  const signal = s.signal ? getSignal(s.signal) : undefined;
  if (signal) return { label: signal.title, url: s.url };
  const host = s.url.startsWith("http") ? new URL(s.url).host.replace(/^www\./, "") : null;
  if (s.type === "gap-check") return { label: `Gap check — ${host ?? "market search (log in record source)"}`, url: s.url.startsWith("http") ? s.url : null };
  return { label: host ? `${s.type} — ${host}` : s.type, url: s.url.startsWith("http") ? s.url : null };
}

export default async function Record({ params }: Params) {
  const { region, id } = await params;
  const p = find(region, id);
  if (!p) notFound();

  const refs = dimRefs(p);
  const idUp = p.id.toUpperCase();
  const dims: { key: Dim | "total"; label: string; num: string; s: number; max: number; verdict: string; zero: boolean }[] = [
    ...DIMS.map((d) => ({
      key: d as Dim | "total",
      label: d.charAt(0).toUpperCase() + d.slice(1),
      num: `${p.scores[d]}/${MAX[d]}`,
      s: p.scores[d],
      max: MAX[d],
      verdict: VERDICTS[d][p.scores[d]],
      zero: p.scores[d] === 0,
    })),
    { key: "total", label: "Total", num: `${pad2(p.score)}/12`, s: p.score, max: 12, verdict: bandWord(p.score), zero: false },
  ];

  const refLinks = (dim: Dim) =>
    refs[dim].length
      ? <>→ {refs[dim].map((n, i) => <span key={n}>{i > 0 && ", "}<a href={`#s${n}`}>S{n}</a></span>)}</>
      : p.scores[dim] === 0
        ? <>—</>
        : <>→ <a href="#sources">see sources</a></>;

  const provenance = p.sources.filter((s) => s.signal).map((s) => s.signal!);

  return (
    <>
      <Masthead />
      <nav className="crumb">
        <a href="/">All problems</a> / {categoryLabel(p.category)} / {idUp} &nbsp;·&nbsp;{" "}
        <a href="/">List</a> · <a href="/signals/funded">Funded</a> ·{" "}
        <a href="/signals/regulation">Regulation</a> · <a href="/signals/tenders">Tenders</a>
      </nav>

      <article>
        <header className="docket">
          <span className="statline"><StatusDot status={p.status} /> <span className="status">{statusLine(p.status)}</span></span>
          <span className="id">{idUp}</span>
          <h1>{p.title}</h1>
          <dl className="facts">
            <div><dt>Category</dt><dd>⚡︎ {categoryLabel(p.category)}</dd></div>
            <div><dt>Locality</dt><dd>⌖ {localityLong(p.geo)}</dd></div>
            <div><dt>Updated</dt><dd><time className="rel" dateTime={p.updated}>{p.updated}</time></dd></div>
            <div><dt>Created</dt><dd><time className="rel" dateTime={p.created}>{p.created}</time></dd></div>
            <div><dt>Sources</dt><dd>{pad2(p.sources.length)}</dd></div>
          </dl>
        </header>

        <section className="scorecard" aria-label="Scorecard — top-line dimensions, each linked to its evidence">
          {dims.map((d) => (
            <button
              key={d.key}
              className={[
                "dim",
                d.key === "total" ? "dim--total" : "",
                d.zero ? "is-zero" : "",
                d.key === "total" && p.score >= 10 ? "score-high" : "",
              ].filter(Boolean).join(" ")}
              popoverTarget={`d-${d.key}`}
            >
              <span className="label">{d.label}</span>
              <span className="num">{d.num}</span>
              <Tally s={d.s} max={d.max} />
              <span className="verdict">{d.verdict}</span>
            </button>
          ))}
        </section>

        <div className="rundowns" aria-label="Score rundown dialogs — click a dimension above">
          {DIMS.map((d) => (
            <div key={d} className="rundown" id={`d-${d}`} popover="auto">
              <span className="verdict">{d.charAt(0).toUpperCase() + d.slice(1)} {p.scores[d]}/{MAX[d]}</span>
              <span>— {criterion(p, d)}</span>
              <span className="t-src">{refLinks(d)}</span>
            </div>
          ))}
          <div className="rundown" id="d-total" popover="auto">
            <span className="verdict">Total {pad2(p.score)}/12 — {bandWord(p.score)}</span>
            <span>· 8+ is newsletter-lead material · bands: PRIME 10–12 · STRONG 8–9 · FAIR 5–7 · FAINT 0–4</span>
          </div>
        </div>

        <h2>The problem</h2>
        <div dangerouslySetInnerHTML={{ __html: renderBody(p.body) }} />

        <h2 id="sources">Sources</h2>
        <ol className="sources">
          {p.sources.map((s, i) => {
            const { label, url } = sourceName(s);
            return (
              <li key={i} id={`s${i + 1}`}>
                {url ? <a href={url}>{label}</a> : <span>{label}</span>}
                <span className="leader"></span>
                <time>{s.date}</time>
              </li>
            );
          })}
        </ol>

        <div className="claim">
          <StatusDot status={p.status} /> <span className="status">{statusLine(p.status)}</span>
          <p>This record is unclaimed. Nobody is working on it. Sources above.</p>
          <a className="btn" href={`mailto:claim@localproblems.org?subject=CLAIM ${idUp}`}>
            Claim this problem →
          </a>
        </div>
      </article>

      <footer>
        Record {idUp} · created <time>{p.created}</time> · updated <time>{p.updated}</time>
        {provenance.length > 0 && (
          <>
            {" "}· source signals:{" "}
            {provenance.map((sid, i) => {
              const sig = getSignal(sid)!;
              return <span key={sid}>{i > 0 && ", "}<a href={`/signals/${sig.type}#${sid}`}>{sid}</a></span>;
            })}
          </>
        )}{" "}
        · <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a>
        <br />
        <FooterHouseLine />
      </footer>

      <RelDatesScript />
    </>
  );
}
