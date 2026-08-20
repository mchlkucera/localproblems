// The feeds registry and the health ledger, in one table (architecture-v3 §4,
// §7.5, §9.6). SOURCES = the feeds we ingest from; SIGNALS = the records they
// produce, which live at /signals/[type].
//
// This is the admin space, and it is deliberately public: a page that admits
// which of its own feeds are broken is the receipt discipline applied to
// ourselves.
import type { Metadata } from "next";
import { CORRECTIONS_MAILTO, FooterHouseLine, Masthead, SiteNav } from "../../lib/chrome";
import { pad2 } from "../../lib/format";
import { since, sourcesView, type Feed } from "./registry";

export const metadata: Metadata = {
  title: "Sources — the feeds this register ingests from — localproblems.org",
  description:
    "Every feed behind the register: what it yields, the terms it is collected under, and whether it is actually producing.",
};

/** The native `title` is the reveal, never a tooltip component; it carries a
    newline exactly as the inline source markers do. Access verdict rides along
    because it is LAW — we never build against a source whose terms forbid it. */
function feedTitle(f: Feed): string {
  const a = f.access;
  return a ? `${f.yields}\n\nAccess: ${a.verdict} — ${a.basis} (checked ${a.checked})` : f.yields;
}

/** null means "not recorded", 0 means "recorded as zero". They are different
    facts and the ledger keeps them different. */
const count = (v: number | null | undefined) => (v == null ? "—" : pad2(v));

export default function Sources() {
  const { rows, unregistered, registryMissing, healthMissing, generated, runId, anchor, feedCount } = sourcesView();
  const blocked = rows.filter((r) => r.feed.status !== "active");
  const errored = rows.filter((r) => r.health?.error);
  // Counted separately and named, so the feed count and the row count differ
  // for a stated reason rather than looking like an arithmetic error (§13.5).
  const enrichment = rows.filter((r) => r.feed.role === "enrichment").length;

  return (
    <>
      <Masthead />
      <SiteNav />

      <p className="crumb">
        Sources · {pad2(feedCount)} feeds on file
        {enrichment > 0 && <> · {pad2(enrichment)} enrichment {enrichment === 1 ? "source" : "sources"} beside them, producing no signals</>}
        {generated && <> · health generated <time>{generated}</time></>}
        {runId && <> · run {runId}</>}
      </p>

      <p>
        Every feed this register ingests from: what it yields, how often it is meant to run,
        and what it is actually doing. Intent and observation are kept in two separate columns
        on purpose — a feed can be registered as active and be producing nothing at all, and
        that pair is the one worth seeing. Silence is the failure that hides best, so it is
        given a column of its own.
      </p>

      {registryMissing ? (
        <p className="absent">
          <span className="urgent">No feeds registry on file.</span>{" "}
          data/feeds.json has not been written yet, so this page can state nothing about the
          feeds except that it cannot state anything. An empty table here would claim there are
          no feeds, which is false. As of <time>{anchor}</time>.
        </p>
      ) : (
        <table className="index">
          <caption>
            The feeds registry joined to the health ledger · status is intent, state is
            observed · dates measured from <time>{anchor}</time>
          </caption>
          <thead>
            <tr>
              <th>Feed</th>
              <th>Type</th>
              {/* "target", never "cadence" alone: the values are recommendations,
                  not measured refresh rates (§4.2). The 7-day yield beside them
                  is the number that will eventually correct them. */}
              <th>Cadence (target) · runner</th>
              <th className="t-num">Yield (run · 7d)</th>
              <th>Status</th>
              <th>State</th>
              <th className="t-num">Last success</th>
            </tr>
          </thead>
          <tbody>
            {rows.map(({ feed: f, health: h }) => (
              <tr key={f.key} id={f.key}>
                <td className="t-title" title={f.url ? undefined : feedTitle(f)}>
                  {f.url ? <a href={f.url} title={feedTitle(f)}>{f.name}</a> : f.name}
                </td>
                <td className="t-cat">{f.role === "enrichment" ? "enrichment" : f.evidence_type ?? "—"}</td>
                <td className="mono">{f.cadence ?? "—"} · {f.runner}</td>
                <td className="t-num mono">{h ? `${count(h.items_last_run)} · ${count(h.yield_7d)}` : "—"}</td>
                {/* INTENT — data/feeds.json */}
                <td><span className="status">{f.status}</span></td>
                {/* OBSERVED REALITY — data/feed_health.json. Never merged with
                    the column to its left; stamp red is the sanctioned alarm. */}
                <td><span className={h?.state === "BROKEN" ? "status urgent" : "status"}>{h?.state ?? "—"}</span></td>
                <td className="t-num t-date">
                  {h == null ? (
                    "—"
                  ) : h.last_success ? (
                    <time dateTime={h.last_success} title={h.last_success}>{since(h.last_success, anchor)}</time>
                  ) : (
                    "never"
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {!registryMissing && healthMissing && (
        <p className="absent">
          <span className="urgent">No health ledger on file.</span>{" "}
          data/feed_health.json is written at the end of every ingest run; until one has run,
          observed state, yield and last success are unknown rather than fine — which is why
          they read “—” above and not “LIVE”. As of <time>{anchor}</time>.
        </p>
      )}

      {!registryMissing && (
        <>
          {/* INTENT: why a feed is not supposed to be running. */}
          <h2>Blockers</h2>
          {blocked.length === 0 ? (
            <p className="absent">Every registered feed is marked active. As of <time>{anchor}</time>.</p>
          ) : (
            <ul className="buildfacts">
              {blocked.map(({ feed: f }) => (
                <li key={f.key}>
                  <span className="label">{f.key}</span>
                  <span className="leader" />
                  <span className="val">
                    {f.blocker}
                    <span className="range"> · {f.status}</span>
                  </span>
                </li>
              ))}
            </ul>
          )}
        </>
      )}

      {!healthMissing && (
        <>
          {/* OBSERVED: what actually went wrong on the last run. */}
          <h2>Errors on last run</h2>
          {errored.length === 0 ? (
            <p className="absent">No feed reported an error on its last run. As of <time>{anchor}</time>.</p>
          ) : (
            <ul className="buildfacts">
              {errored.map(({ feed: f, health: h }) => (
                <li key={f.key}>
                  <span className="label">{f.key}</span>
                  <span className="leader" />
                  <span className="val urgent">
                    {h!.error}
                    <span className="range"> · {h!.state}</span>
                  </span>
                </li>
              ))}
            </ul>
          )}
        </>
      )}

      {unregistered.length > 0 && (
        <>
          {/* A health row naming a feed the registry does not carry is stated,
              never dropped — a dropped row is exactly the silence this page exists
              to make visible. */}
          <h2>Health rows with no registry entry</h2>
          <ul className="buildfacts">
            {unregistered.map((h) => (
              <li key={h.key}>
                <span className="label">{h.key}</span>
                <span className="leader" />
                <span className="val">
                  Reported by the health export, absent from data/feeds.json
                  <span className="range"> · {h.state}</span>
                </span>
              </li>
            ))}
          </ul>
        </>
      )}

      <footer>
        <FooterHouseLine />
        <br />
        <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a> ·{" "}
        <a href="/">problem register</a> · <a href="/signals/funded">signal ledgers</a>
      </footer>
    </>
  );
}
