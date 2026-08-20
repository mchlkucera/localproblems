// The two committed inputs behind /sources: the feeds registry (what we ingest
// from, and are allowed to ingest from) and the health ledger (what is actually
// producing). architecture-v3 §4 and §7.5. Build-time only; never opens the DB —
// the site stays a pure function of ../data (SPEC.md §5).
//
// WHY THIS LIVES HERE AND NOT IN lib/data.ts: §4.3 and §7.5 name lib/data.ts as
// the home for these loaders. It is colocated with its only consumer instead,
// because lib/data.ts is under concurrent edit by other programs and this module
// needs none of its internals beyond two exported reads. Behaviour is identical:
// build-time readFileSync + zod, validation failure = build failure.
import { existsSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { z } from "zod";
import { EVIDENCE_TYPES, extractDate, getSignals } from "../../lib/data";

const ROOT = resolve(process.cwd(), "..");

const isoDate = z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "ISO date required");
const isoTimestamp = z
  .string()
  .regex(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(\.\d+)?(Z|[+-]\d{2}:\d{2})$/, "ISO timestamp required");

// ---- the two vocabularies ------------------------------------------------
// These are DELIBERATELY DISTINCT and must never be merged. `status` is INTENT
// (is this feed supposed to be running?) and lives in data/feeds.json. `state`
// is OBSERVED REALITY (is it actually producing?) and lives in
// data/feed_health.json. A feed can be `active` + `BROKEN`; that combination is
// the entire point of this page (§7.5).
export const FEED_STATUSES = ["active", "blocked", "dead", "planned"] as const;
export const FEED_STATES = ["LIVE", "STALE", "BROKEN", "PENDING"] as const;

const nullish = <T extends z.ZodTypeAny>(s: T) => s.nullable().optional();

// looseObject, not strictObject — the deliberate opposite of SignalSchema.
// feeds.json is jq-read by the shell fetchers (§4), so operational keys we do
// not render are EXPECTED to appear and must not fail the build. Every field
// this page renders is typed below; the rest passes through unvalidated and is
// the writer's business.
const FeedSchema = z.looseObject({
  key: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/, "kebab-case feed key"),
  name: z.string().min(1),
  yields: z.string().min(1),
  // `enrichment` sources (ARES) have their health tracked but produce NO
  // signals, are exempt from AC-F1, and never inflate the feed count (§13.5).
  role: z.enum(["feed", "enrichment"]).optional(),
  signal_source: nullish(z.string().min(1)),
  evidence_type: nullish(z.enum(EVIDENCE_TYPES)),
  cadence: nullish(z.string().min(1)),
  runner: z.enum(["cloud", "local", "attended", "none"]),
  // Nullable: the attended agent harvests (demand-scan, arb-scan, round) are
  // not URL-addressable feeds. The row renders its name as plain text rather
  // than inventing a link to point at (§4.4).
  url: nullish(z.string().url()),
  script: nullish(z.string().min(1)),
  status: z.enum(FEED_STATUSES),
  blocker: nullish(z.string().min(1)),
  last_known_good: nullish(isoTimestamp),
  // ToS / access verdict — LAW. We never build against a source whose terms
  // forbid it (§4.1).
  access: z
    .looseObject({
      verdict: z.enum(["allowed", "conditional", "forbidden", "unknown"]),
      basis: z.string().min(1),
      checked: isoDate,
    })
    .optional(),
});
export type Feed = z.infer<typeof FeedSchema>;

const FeedsFileSchema = z.looseObject({
  version: z.number().int().min(1),
  feeds: z.array(FeedSchema),
});

const HealthFeedSchema = z.looseObject({
  key: z.string().min(1),
  state: z.enum(FEED_STATES),
  last_success: nullish(isoDate),
  items_last_run: nullish(z.number().int().min(0)),
  yield_7d: nullish(z.number().int().min(0)),
  error: nullish(z.string().min(1)),
});
export type FeedHealth = z.infer<typeof HealthFeedSchema>;

const HealthFileSchema = z.looseObject({
  // Relative dates compute against THIS, never wall clock (§7.5).
  generated: isoDate,
  // Nullable: a health export written before any ingest run has completed has
  // no run to name, and says so rather than inventing an id.
  run_id: nullish(z.string().min(1)),
  feeds: z.array(HealthFeedSchema),
});

// ---- loading -------------------------------------------------------------

/** ABSENT vs MALFORMED, treated differently on purpose.
 *
 *  MALFORMED is a build failure, exactly as the law promises (§7.5: "web/lib/
 *  data.ts zod-validates feed_health.json; validation failure = build failure").
 *
 *  ABSENT is not. Both files are written by INGEST and may not have landed yet;
 *  hard-failing on absence would take the whole public site down for every other
 *  program until they do. Instead the absence is STATED — loudly on the page and
 *  as a WARN line in the build log — which is the house rule everywhere else in
 *  this codebase (an empty ledger is a registered fact, absence is stated and
 *  never hidden). The one thing it must never be is a silently empty table. */
function readJson<T>(rel: string, schema: z.ZodType<T>): T | null {
  const abs = resolve(ROOT, rel);
  if (!existsSync(abs)) {
    console.warn(`sources: WARN ${rel} not found — /sources states the absence instead of rendering empty (architecture-v3 §4, §7.5)`);
    return null;
  }
  let raw: unknown;
  try {
    raw = JSON.parse(readFileSync(abs, "utf8"));
  } catch (e) {
    throw new Error(`${rel}: not valid JSON — ${(e as Error).message}`);
  }
  const parsed = schema.safeParse(raw);
  if (!parsed.success) {
    throw new Error(`${rel}: ${parsed.error.issues.map((i) => `${i.path.join(".")}: ${i.message}`).join("; ")}`);
  }
  return parsed.data;
}

/** The two build-time assertions of §4.3. They only run once the registry
    exists — there is nothing to assert about a registry that is not there. */
function assertRegistry(feeds: Feed[]): void {
  const keys = new Set<string>();
  for (const f of feeds) {
    if (keys.has(f.key)) throw new Error(`data/feeds.json: duplicate feed key '${f.key}'`);
    keys.add(f.key);
    // AC-F2 — no orphan links: every non-null `script` path must exist on disk.
    if (f.script && !existsSync(join(ROOT, f.script))) {
      throw new Error(`data/feeds.json: feed '${f.key}' names script '${f.script}', which does not exist on disk (AC-F2)`);
    }
    if (f.status !== "active" && !f.blocker) {
      throw new Error(`data/feeds.json: feed '${f.key}' is '${f.status}' but records no blocker — a non-active feed must say why (§4.1)`);
    }
  }
  // AC-F1 — totality: every distinct `source` present in data/signals/** must be
  // claimed by at least one registry entry's `signal_source`, or /sources
  // silently under-explains the corpus. Enrichment rows produce no signals and
  // are exempt (§13.5).
  const claimed = new Set(
    feeds.filter((f) => f.role !== "enrichment").map((f) => f.signal_source).filter((s): s is string => !!s)
  );
  const unclaimed = [...new Set(getSignals().map((s) => s.source))].filter((s) => !claimed.has(s)).sort();
  if (unclaimed.length) {
    throw new Error(
      `data/feeds.json: no registry entry claims signal source(s) ${unclaimed.join(", ")} — /sources would under-explain the corpus (AC-F1)`
    );
  }
}

export type SourceRow = { feed: Feed; health: FeedHealth | null };

export type SourcesView = {
  rows: SourceRow[];
  /** Health rows naming a key the registry does not carry — stated, not dropped. */
  unregistered: FeedHealth[];
  registryMissing: boolean;
  healthMissing: boolean;
  generated: string | null;
  runId: string | null;
  /** The date every relative date on this page is measured from: the health
      file's own `generated`, falling back to extractDate(). NEVER wall clock —
      a build must be reproducible from a commit (§7.5, §8.2). */
  anchor: string;
  /** `enrichment` rows never inflate the feed count (§13.5). */
  feedCount: number;
};

let _view: SourcesView | null = null;
export function sourcesView(): SourcesView {
  if (_view) return _view;
  const registry = readJson("data/feeds.json", FeedsFileSchema);
  const health = readJson("data/feed_health.json", HealthFileSchema);
  const feeds = registry?.feeds ?? [];
  if (registry) assertRegistry(feeds);

  const byKey = new Map((health?.feeds ?? []).map((h) => [h.key, h]));
  const rows: SourceRow[] = feeds.map((feed) => ({ feed, health: byKey.get(feed.key) ?? null }));
  const registered = new Set(feeds.map((f) => f.key));
  const unregistered = (health?.feeds ?? []).filter((h) => !registered.has(h.key));

  _view = {
    rows,
    unregistered,
    registryMissing: registry === null,
    healthMissing: health === null,
    generated: health?.generated ?? null,
    runId: health?.run_id ?? null,
    anchor: health?.generated ?? extractDate(),
    feedCount: feeds.filter((f) => f.role !== "enrichment").length,
  };
  return _view;
}

/** The house relative-date ladder, computed SERVER-SIDE against `anchor`.
 *
 *  Deliberately NOT the `time.rel` client script (sanctioned exception 2): that
 *  one measures against the browser's wall clock, which is exactly what §7.5
 *  forbids here. Rendering the relative text at build time and omitting the
 *  `rel` class keeps the script's hands off these dates and keeps the page
 *  reproducible from a commit. The ISO date stays in `datetime` + `title`. */
export function since(date: string, anchor: string): string {
  const days = Math.round((Date.parse(anchor) - Date.parse(date)) / 86_400_000);
  if (days <= 0) return "today";
  if (days === 1) return "yesterday";
  if (days < 7) return `${days} days ago`;
  if (days < 30) {
    const w = Math.round(days / 7);
    return `${w} ${w === 1 ? "week" : "weeks"} ago`;
  }
  if (days < 365) {
    const m = Math.round(days / 30);
    return `${m} ${m === 1 ? "month" : "months"} ago`;
  }
  const y = Math.round(days / 365);
  return `${y} ${y === 1 ? "year" : "years"} ago`;
}
