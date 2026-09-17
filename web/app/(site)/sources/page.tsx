// /sources — the feeds registry beside the health ledger (architecture-v3 §4,
// §7.5, §9.6), in the modern design. SOURCES = the feeds we ingest from;
// SIGNALS = the records they produce, which live at /signals/[type].
//
// THIS IS THE ADMIN SPACE AND IT IS PRIVATE (owner, 2026-08-21). It was public
// on the argument that a page admitting which of its own feeds are broken is the
// receipt discipline applied to ourselves. The owner overrode that: it carries
// operational internals — blockers, access verdicts, per-feed yields, which
// sources are dry — that are ours to read and nobody else's.
//
// PRIVATE MEANS NOT BUILT, not hidden. A page that renders and merely goes
// unlinked is still fetchable by anyone who guesses the path, and "unlisted" is
// the weakest possible privacy. `notFound()` before any data is read means the
// production bundle never contains the feed registry at all.
//
// It stays fully available locally, where it is genuinely useful: `npm run dev`
// sets LP_ADMIN=1 (see web/package.json), so http://localhost:3000/sources works.
// Set LP_ADMIN=1 on a build to emit it deliberately. Nothing links here.
//
// The `/sources/:type` -> `/signals/:type` redirect in next.config.ts is
// UNAFFECTED and must stay: it serves old deep links in record bodies, and those
// point at the public signal ledgers, not at this page.
//
// DESIGN (2026-09-17, the last gazette page moved to the modern design): the
// signal ledgers' compact ledger (`signals.css`, DESIGN.md "Signals ledgers"),
// one line per feed in fixed columns, with everything the gazette hid in a
// native `title` (what it yields, the access verdict, the blocker, the last
// error) one native `<details>` away. No hue beyond ink blue for a feed you can
// open: the design has no alarm colour, so a BROKEN state is set in weight.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import "../styles/front.css";
import "../styles/signals.css";
import "../styles/sources.css";
import { CORRECTIONS_MAILTO } from "../../../lib/chrome";
import { TopBar } from "../../../lib/site/bar";
import { fmtDate } from "../../../lib/site/sources";
import { since, sourcesView, type Feed, type FeedHealth } from "./registry";

/** Read inside the component, never at module scope: a module-scope constant can
    be folded by the bundler, and this is the only thing standing between the
    feed registry and the public internet. */
function adminEnabled(): boolean {
  return process.env.LP_ADMIN === "1";
}

export const metadata: Metadata = {
  title: "Sources — the feeds this register ingests from — localproblems.org",
  description:
    "Every feed behind the register: what it yields, the terms it is collected under, and whether it is actually producing.",
};

/** null means "not recorded", 0 means "recorded as zero". They are different
    facts and the ledger keeps them different. */
const count = (v: number | null | undefined) => (v == null ? "—" : String(v));

const cap = (s: string) => s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();

/** Short date for an ISO date or timestamp; the full value rides in `title`. */
const day = (iso: string) => fmtDate(iso.slice(0, 10));

function FeedRow({ f, h, anchor }: { f: Feed; h: FeedHealth | null; anchor: string }) {
  const tid = `${f.key}-t`;
  const type = f.role === "enrichment" ? "Enrichment" : f.evidence_type ? cap(f.evidence_type) : "—";
  const broken = h?.state === "BROKEN";
  return (
    <li className="lg-row" id={f.key}>
      <div className="lg-line">
        <h3 className="lg-title" id={tid}>
          {f.url ? (
            <a href={f.url} target="_blank" rel="noopener noreferrer" title={f.name}>
              <span className="lg-t">{f.name}</span>
              <span className="lg-ext" aria-hidden="true">{" ↗"}</span>
              <span className="lf-sr"> (another site)</span>
            </a>
          ) : (
            // the attended harvests are not URL-addressable: plain text, no link invented
            <span className="lsr-plain" title={f.name}><span className="lg-t">{f.name}</span></span>
          )}
        </h3>
        <span className="lg-c lsr-c-type"><span className="lf-sr">Type: </span>{type}</span>
        {/* "target", never "cadence" alone: recommendations, not measured
            refresh rates (§4.2). The 7-day yield will eventually correct them. */}
        <span className="lg-c lsr-c-cad"><span className="lf-sr">Cadence (target) · runner: </span>{f.cadence ?? "—"} · {f.runner}</span>
        <span className="lg-c lsr-c-num"><span className="lsr-k">Last run </span>{h ? count(h.items_last_run) : "—"}</span>
        <span className="lg-c lsr-c-num"><span className="lsr-k">7 days </span>{h ? count(h.yield_7d) : "—"}</span>
        {/* INTENT — data/feeds.json */}
        <span className="lg-c lsr-c-status"><span className="lsr-k">Status </span>{cap(f.status)}</span>
        {/* OBSERVED REALITY — data/feed_health.json. Never merged with the
            column to its left. */}
        <span className={broken ? "lg-c lsr-c-state lsr-broken" : "lg-c lsr-c-state"}>
          <span className="lsr-k">State </span>{h ? cap(h.state) : "—"}
        </span>
        <span className="lg-c lg-c-date">
          <span className="lf-sr">Last success: </span>
          {h == null ? "—" : h.last_success ? (
            <time dateTime={h.last_success} title={fmtDate(h.last_success)}>{since(h.last_success, anchor)}</time>
          ) : "never"}
        </span>
      </div>
      <details className="lg-more">
        <summary aria-describedby={tid}>
          <span className="lf-sr">Details</span>
          <svg className="lg-caret" viewBox="0 0 16 16" width="12" height="12" fill="currentColor" aria-hidden="true">
            <path d="M4.5 6h7L8 10.5Z" />
          </svg>
        </summary>
        <div className="lg-sum">
          <p>{f.yields}</p>
          <dl className="lsr-dl">
            {/* ToS / access verdict — LAW: we never build against a source
                whose terms forbid it (§4.1). */}
            {f.access && (
              <div><dt>Access</dt><dd>{cap(f.access.verdict)}: {f.access.basis} <span className="lsr-quiet">(checked {fmtDate(f.access.checked)})</span></dd></div>
            )}
            {f.blocker && <div><dt>Blocker</dt><dd>{f.blocker}</dd></div>}
            {h?.error && <div><dt>Last run</dt><dd>{h.error}</dd></div>}
            {f.script && <div><dt>Script</dt><dd><code>{f.script}</code></dd></div>}
            {f.last_known_good && (
              <div><dt>Last known good</dt><dd><time dateTime={f.last_known_good}>{day(f.last_known_good)}</time></dd></div>
            )}
          </dl>
        </div>
      </details>
    </li>
  );
}

/** A short keyed list: the feed key (an in-page link to its row), what is
    stated about it, and the status or state it carries. */
function Facts({ items }: { items: { key: string; text: string; tag: string; linked: boolean }[] }) {
  return (
    <ul className="lsr-facts">
      {items.map((it) => (
        <li key={it.key}>
          <span className="lsr-fk">{it.linked ? <a href={`#${it.key}`}>{it.key}</a> : it.key}</span>
          <span className="lsr-ft">{it.text}</span>
          <span className="lsr-fs">{it.tag}</span>
        </li>
      ))}
    </ul>
  );
}

export default function Sources() {
  // FIRST STATEMENT, before sourcesView() reads the registry. The guard is
  // worth nothing if the data is already loaded when it fires.
  if (!adminEnabled()) notFound();
  const { rows, unregistered, registryMissing, healthMissing, generated, runId, anchor, feedCount } = sourcesView();
  const blocked = rows.filter((r) => r.feed.status !== "active");
  const errored = rows.filter((r) => r.health?.error);
  // Counted separately and named, so the feed count and the row count differ
  // for a stated reason rather than looking like an arithmetic error (§13.5).
  const enrichment = rows.filter((r) => r.feed.role === "enrichment").length;

  return (
    <div className="lab lf lg lsr">
      <TopBar />

      <main className="lf-wrap">
        <header className="lg-head">
          <h1>Sources</h1>
          <p className="lg-lede">
            Every feed this register ingests from: what it yields, how often it is meant to run,
            and what it is actually doing. Intent and observation are kept in two separate columns
            on purpose. A feed can be registered as active and be producing nothing at all, and
            that pair is the one worth seeing. Silence is the failure that hides best, so it is
            given a column of its own.
          </p>
          <p className="lsr-meta">
            {feedCount} {feedCount === 1 ? "feed" : "feeds"} on file
            {enrichment > 0 && <> · {enrichment} enrichment {enrichment === 1 ? "source" : "sources"} beside them, producing no signals</>}
            {generated && <> · health generated <time dateTime={generated}>{fmtDate(generated)}</time></>}
            {runId && <> · run {runId}</>}
          </p>
        </header>

        {registryMissing ? (
          <p className="lg-empty">
            <strong>No feeds registry on file.</strong>{" "}
            data/feeds.json has not been written yet, so this page can state nothing about the
            feeds except that it cannot state anything. An empty table here would claim there are
            no feeds, which is false. As of <time dateTime={anchor}>{fmtDate(anchor)}</time>.
          </p>
        ) : (
          <>
            <p className="lf-sr">
              The feeds registry joined to the health ledger. Status is intent, state is observed.
              Dates are measured from {fmtDate(anchor)}.
            </p>
            <div className="lg-cols" aria-hidden="true">
              <span>Feed</span><span className="lsr-c-type">Type</span><span className="lsr-c-cad">Cadence · runner</span>
              <span className="lsr-c-num">Last run</span><span className="lsr-c-num">7 days</span>
              <span>Status</span><span>State</span><span className="lg-c-date">Last success</span>
            </div>
            <ol className="lg-rows">
              {rows.map(({ feed, health }) => <FeedRow key={feed.key} f={feed} h={health} anchor={anchor} />)}
            </ol>
            <p className="lsr-note">
              Status is intent (data/feeds.json); state is observed (data/feed_health.json). Cadence is a target, not a measured refresh rate.
              Relative dates are measured from <time dateTime={anchor}>{fmtDate(anchor)}</time>, never the clock.
            </p>
          </>
        )}

        {!registryMissing && healthMissing && (
          <p className="lg-empty">
            <strong>No health ledger on file.</strong>{" "}
            data/feed_health.json is written at the end of every ingest run; until one has run,
            observed state, yield and last success are unknown rather than fine, which is why
            they read “—” above and not “Live”. As of <time dateTime={anchor}>{fmtDate(anchor)}</time>.
          </p>
        )}

        {!registryMissing && (
          <section className="lsr-sec" aria-labelledby="blockers">
            {/* INTENT: why a feed is not supposed to be running. */}
            <h2 id="blockers">Blockers</h2>
            {blocked.length === 0 ? (
              <p className="lsr-none">Every registered feed is marked active.</p>
            ) : (
              <Facts items={blocked.map(({ feed: f }) => ({ key: f.key, text: f.blocker ?? "", tag: cap(f.status), linked: true }))} />
            )}
          </section>
        )}

        {!healthMissing && (
          <section className="lsr-sec" aria-labelledby="errors">
            {/* OBSERVED: what actually went wrong on the last run. */}
            <h2 id="errors">Errors on last run</h2>
            {errored.length === 0 ? (
              <p className="lsr-none">No feed reported an error on its last run.</p>
            ) : (
              <Facts items={errored.map(({ feed: f, health: h }) => ({ key: f.key, text: h!.error!, tag: cap(h!.state), linked: true }))} />
            )}
          </section>
        )}

        {unregistered.length > 0 && (
          <section className="lsr-sec" aria-labelledby="unregistered">
            {/* A health row naming a feed the registry does not carry is stated,
                never dropped — a dropped row is exactly the silence this page
                exists to make visible. */}
            <h2 id="unregistered">Health rows with no registry entry</h2>
            <Facts
              items={unregistered.map((h) => ({
                key: h.key, text: "Reported by the health export, absent from data/feeds.json", tag: cap(h.state), linked: false,
              }))}
            />
          </section>
        )}
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
