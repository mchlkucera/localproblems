// The data layer: reads ../data at build time, zod-validated.
// Validation failure = build failure = deploy blocked (SPEC.md §5).
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { load as yamlLoad } from "js-yaml";
import { z } from "zod";
import { rows, type SqliteRow } from "./db";

const ROOT = resolve(process.cwd(), "..");
const DATA = join(ROOT, "data");

// ---- the two read paths --------------------------------------------------

/** Which store the loaders read: the working store, or the canonical journal.
 *
 *  `db` — `data/register.db`. **THE DEFAULT, AND WHAT PRODUCTION READS**
 *  (flipped 2026-08-20, after `npm run parity` proved byte-identical HTML).
 *  Gitignored and never committed; `web/scripts/db-gate.mjs` regenerates it
 *  from the journal inside `npm run build`, before `next build` runs, and then
 *  verifies it against the tree — so the store production reads is always a
 *  projection of the commit being deployed.
 *  `jsonl` — `data/signals/**.jsonl` + `data/problems/ ** /*.md`. The
 *  append-only ledger, committed to git, and still the canonical corpus:
 *  the database is derived from it and never the other way round. Selecting it
 *  is now an explicit opt-out, used by `scripts/parity.mjs` as the reference
 *  implementation the db path is measured against.
 *
 *  THE DEFAULT IS `db` PRECISELY SO IT CANNOT BE FORGOTTEN. Carrying the flip
 *  in a build script or a deploy env var instead would mean any build that
 *  missed the setting silently served the journal — a green build that quietly
 *  un-did the migration, which nobody would notice. Here, the only way to read
 *  the journal is to ask for it by name.
 *
 *  AN UNKNOWN VALUE IS A LOUD FAILURE, NOT A FALLBACK. `LP_SOURCE=DB` quietly
 *  taking the jsonl branch would make the parity harness compare jsonl against
 *  jsonl and report a triumphant green — the exact false positive this whole
 *  exercise exists to avoid. Read inside the function, never captured at module
 *  scope, so no bundler can fold it to a constant. */
export function source(): "jsonl" | "db" {
  const v = process.env.LP_SOURCE ?? "db";
  if (v !== "jsonl" && v !== "db")
    throw new Error(`LP_SOURCE must be 'jsonl' or 'db', got '${v}'`);
  return v;
}

/** One line per build worker, on stderr. It is the only externally visible
    evidence of WHICH branch ran, and `scripts/parity.mjs` asserts on it. */
let _announced = false;
function announce(): "jsonl" | "db" {
  const src = source();
  if (!_announced) {
    _announced = true;
    process.stderr.write(`[lp-data] LP_SOURCE=${src}\n`);
  }
  return src;
}

/** UTF-16 code-unit order — byte-for-byte what `Array.prototype.sort()` does to
    strings, and therefore what `readdirSync().sort()` does to filenames. NOT
    `localeCompare` (ICU collation) and NOT SQL `ORDER BY` (SQLite BINARY over
    UTF-8): all three agree on today's ASCII filenames and slugs and diverge
    silently on the first non-ASCII one. */
const cmp = (a: string, b: string) => (a < b ? -1 : a > b ? 1 : 0);

export const CATEGORIES = [
  "fintech", "health", "housing", "energy", "mobility", "govtech",
  "retail-services", "b2b", "legal-compliance", "education", "environment", "other",
] as const;

export const EVIDENCE_TYPES = ["funded", "regulation", "tenders", "demand", "hiring", "asks"] as const;
export type EvidenceType = (typeof EVIDENCE_TYPES)[number];

const isoDate = z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "ISO date required");
/** A TIMESTAMP, not a date — a date cannot gate a 3h or 6h cadence (architecture-v3 §4.1). */
const isoTimestamp = z
  .string()
  .regex(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(\.\d+)?(Z|[+-]\d{2}:\d{2})$/, "ISO timestamp required");

/** How a signal was extracted from its payload (architecture-v3 §7.3). The value
    IS the review flag — `llm-fallback` rows are marked on the ledger, never
    silently trusted. An enum fails LOUDLY on an unknown value, by design. */
export const EXTRACTION_METHODS = ["structured", "llm-fallback", "manual"] as const;

// ---- evidence layer ------------------------------------------------------

// z.strictObject, NOT z.object (architecture-v3 §3, AC-Z2). `z.object` SILENTLY
// STRIPS unknown keys: a new JSONL field would land in the canonical ledgers, be
// dropped at build time, never reach the site — and the "validation failure =
// build failure = deploy blocked" law would never fire. Strict makes an unknown
// key the loud failure that law already promises.
// Measured before the flip: all 6,181 lines in data/signals/** carry only the
// keys below (12 top-level, 4 under `scores`), so this is safe today.
const SignalSchema = z.strictObject({
  id: z.string().regex(/^[a-z]{2,10}-[\w.-]+$/),
  // WIDENED BEFORE ANYTHING APPENDS, and that order is the whole point: this
  // enum is the schema the build validates against, so a ledger line carrying a
  // `source` this list does not know RED-BUILDS and blocks the deploy (SPEC §5).
  // The append is irreversible and the ledger has no quiet cleanup, so the enum
  // must already accept the value on the commit BEFORE the first record lands —
  // never in the same change, and never after.
  //   `coi` `sukl` `nen`      — scripts/{coi,sukl,nen}_extract.py
  //   `smlouvy`               — extract_smlouvy, the official registr smluv dump
  // `mpsv` was already here. `ec-hys`, `nku` and `vestbee` need NO entry: their
  // extractors deliberately reuse the existing `reg-scan` / `demand-scan` /
  // `round` provenances rather than minting a fourth name for the same source.
  //   `dotace`                — dotace-scan agent harvests of grant/subsidy
  //                             calls read from the grantor's own call page
  //                             (registry key dotace-scan, prefix dotace-).
  //                             Widened 2026-08-25, BEFORE the first `dotace`
  //                             ledger line — commit this file ahead of (or.
  //                             at minimum never after) that record.
  //   `veklep`                — scripts/fetch_veklep.sh, the government's
  //                             legislative e-library (ODok VeKLEP) via the
  //                             Hlídač dataset mirror. A new PUBLISHER, not a
  //                             new script for an existing provenance — the
  //                             CONVENTIONS.md test ec-hys/nku fail and this
  //                             passes. Widened 2026-08-25, before the first
  //                             `veklep` ledger line.
  //   `tacr` `hackathon`      — the `asks` ledger: scripts/fetch_tacr.sh and
  //                             scripts/fetch_hackathons.sh. Both are new
  //                             PUBLISHERS — TA ČR's own needs feed, and the
  //                             hackathon organizers' own event sites — not new
  //                             scripts over a provenance the corpus already
  //                             carries, so both pass the same test `veklep`
  //                             did. Widened 2026-09-03, BEFORE the first
  //                             `asks` ledger line.
  source: z.enum(["ted", "hlidac", "yc", "round", "reg-scan", "arb-scan", "feed", "demand-scan", "suggest", "reddit", "mpsv", "coi", "sukl", "nen", "smlouvy", "dotace", "veklep", "tacr", "hackathon", "nen-ptk", "edesky"]),
  url: z.string().url(),
  date: isoDate,
  title: z.string().min(1),
  sector: z.enum(CATEGORIES),
  geo_origin: z.string().regex(/^([A-Z]{2}|EU)$/),
  money_eur: z.number().nullable(),
  money_note: z.string(),
  summary: z.string().min(1),
  // strictObject applies to the TOP LEVEL ONLY — the nested object must be made
  // strict in the same edit or the trap simply moves one level down and a stray
  // `scores.confidence` from a future scorer vanishes silently (§3, AC-Z2).
  scores: z.strictObject({
    scale: z.number().int().min(0).max(3),
    money: z.number().int().min(0).max(3),
    urgency: z.number().int().min(0).max(3),
    recurrence: z.number().int().min(0).max(3),
  }),
  notes: z.string().optional(),
  // `owner` — WHO STATED THE PROBLEM: the institution named as the setter of
  // an ask. REQUIRED on every `asks` record and absent everywhere else
  // (data/CONVENTIONS.md, record schema; owner, 2026-09-03). Optional HERE
  // because this schema does not know which ledger a line came from — `type`
  // is the directory, stamped on after the parse — so the per-ledger rule is
  // enforced where the type is known: scripts/db.py check_owner(), on both
  // write paths, which red-builds through db-gate. Its own field and not a
  // `notes: owner: …` prefix, for the §0 reason: `notes` is free text, and a
  // structured fact riding inside it was read by no validator and rendered on
  // no page (the asks critique, finding 1). min(1): an empty owner is the
  // shape that looks present and says nothing.
  owner: z.string().min(1).optional(),
  // ---- receipt fields (§7.2, §7.3). Optional; written by INGEST. -----------
  // `quote` is a CONTRACT WITH AN EXTERNAL CONSUMER: a flat string on the
  // signal, retrievable by signal id. Do not restructure it into an object,
  // an array, or a nested receipt. min(1) because an empty quote is not a
  // quote — it is the shape that looks present and says nothing; omit the key.
  quote: z.string().min(1).optional(),
  http_status: z.number().int().min(100).max(599).optional(),
  fetched_at: isoTimestamp.optional(),
  extraction: z.enum(EXTRACTION_METHODS).optional(),
});
export type Signal = z.infer<typeof SignalSchema> & { type: EvidenceType };

// ---- region layer --------------------------------------------------------

const STATUSES = ["candidate", "active", "watching", "stale", "claimed", "solved", "rejected"] as const;

/** Where a gap-check actually looked (architecture-v3 §8.1). Vocabulary is
    closed on purpose: an enum fails loudly on a typo, which is the whole reason
    these keys get typed rather than left to looseObject. */
export const GAP_CHECKED = [
  "ares", "app-stores", "cz-saas-directories", "google-cz", "startupjobs", "own-funded-ledger",
  // A SEPARATE TOKEN, deliberately not a widened `app-stores`. The two name
  // different populations — a consumer app store and a platform add-on
  // catalogue — and a `checked` value whose coverage the reader has to guess
  // fails the one job this vocabulary has. Backed by data/lookup/, built by
  // scripts/fetch_{shoptet,upgates}.sh. See data/CONVENTIONS.md.
  "eshop-addon-marketplaces",
  // Widened 2026-08-25, AFTER the records that use them — a rule violation
  // recorded rather than hidden. Three gap checks recorded surfaces this
  // vocabulary did not know, the build failed on zod, and the fix is forward.
  // Note what it exposes: `scripts/check-records.py` passed all three, so an
  // agent verifying with the checker alone saw a false green. The two
  // validators disagree, and only `npm run build` runs both.
  //   `cz-contract-parties`   — the state contracts register, aggregated by
  //                             supplier in data/lookup/. NOT `own-funded-ledger`:
  //                             that is capital, this is public purchasing, and
  //                             they surface opposite populations — a
  //                             bootstrapped vendor with public buyers appears
  //                             here and never there.
  //   `zivnostensky-rejstrik` — the trade-licence register. Distinct from `ares`:
  //                             it lists WHAT A COMPANY IS LICENSED TO DO, which
  //                             is how p-0033 established that Grason holds no
  //                             employment-agency licence.
  //   `company-job-feed`      — a company's own public job listings, read to
  //                             establish which market it actually serves.
  //                             Deliberately general: it was first written as
  //                             `grason-public-job-feed`, which names one
  //                             investigation rather than a surface anyone could
  //                             check again.
  "cz-contract-parties", "zivnostensky-rejstrik", "company-job-feed",
] as const;
export type GapChecked = (typeof GAP_CHECKED)[number];

/** `sources[].unit` on a price receipt — what one amount buys. A closed enum:
    the page renders each as an English phrase (format.ts PRICE_UNIT_LABELS)
    and an unknown token is a build failure, never a raw slug on the page. */
export const PRICE_UNITS = [
  "per-seat-month", "per-case", "per-year", "per-project", "one-off", "per-hour",
] as const;
export type PriceUnit = (typeof PRICE_UNITS)[number];
/** `sources[].basis` on a price receipt — where the figure comes from. A
    receipt is worth what its basis is worth, so the basis prints beside it:
    `list-price` (the vendor's published price) · `signed-contract` (a contract
    on file) · `tender-line` (a line in a tender or its award) ·
    `buyer-interview` (a named buyer said so, dated) · `manual-equivalent`
    (what the same job costs done by hand — the only way an OPEN field, with no
    incumbent page to read a price from, gets priced at all). */
export const PRICE_BASES = [
  "list-price", "signed-contract", "tender-line", "buyer-interview", "manual-equivalent",
] as const;
export type PriceBasis = (typeof PRICE_BASES)[number];

// NOTE the deliberate contrast with SignalSchema seven lines above: this one is
// z.looseObject, so extra keys on problem `sources[]` already pass untouched.
// That is why the gap-check fields below "already work" — but "already passes"
// means "unvalidated": a typo'd `expiers` would sit in the frontmatter forever,
// rendering nothing. Typed as optionals so the typo is a build failure (§8.1).
const SourceSchema = z.looseObject({
  type: z.string().min(1),
  url: z.string().min(1),
  note: z.string().min(1),
  date: isoDate,
  // PUBLIC-RENDER FIELDS (owner, 2026-08-24). `note` is the internal receipt and
  // no longer renders verbatim on the page; these two are what the reader sees.
  // `name` overrides the ledger display name (so a gap-check reads "Ringil", not
  // "Gap check — host"); `why` is the one plain line saying what it is and why it
  // is cited. Both optional — a source with neither falls back to its signal's
  // title/summary, then to the type. The receipt in `note` is never touched.
  name: z.string().min(1).optional(),
  why: z.string().min(1).optional(),
  // `gist` — the clerk's few-word label for the source, 2–6 words (owner,
  // 2026-08-25: "even the link explanations are too long — a few word
  // explanation and see more on a toggle"). With it the ledger row reads
  // NAME · gist · date and the full `why` sentence moves behind a native
  // <details> "more"; without it the row renders exactly as before — the
  // open why line, no toggle. A first-class column in scripts/db.py
  // (problem_sources.gist, schema_version 8), never looseObject overflow.
  gist: z.string().min(1).optional(),
  signal: z.string().optional(),
  dims: z.array(z.enum(["proof", "money", "urgency", "demand", "gap"])).optional(),
  queries: z.array(z.string().min(1)).optional(),
  checked: z.array(z.enum(GAP_CHECKED)).optional(),
  // date + 90 days, computed once when the gap-check source is written. Decay
  // compares against extractDate(), NEVER the wall clock (§8.2) — display-only,
  // it never moves `scores.gap` and never changes a total.
  expires: isoDate.optional(),
  // PRICE RECEIPT FIELDS (owner ruling, 2026-09-03; docs/who-pays-audit-
  // 2026-09-03.md). MONEY measures proximity to a public budget and was never
  // an answer to "who pays and how much" — six of the eight records at rung 1
  // wrote "adjacent" in their own notes. The answer is a SEPARATE receipt, not
  // a re-score: a `type: price` source records what a named Czech buyer pays
  // for THIS product or its manual equivalent. All four are REQUIRED on a
  // price source and FORBIDDEN on any other type (the check below) — one
  // field, one meaning. Deliberately NOT columns in scripts/db.py: they ride
  // problem_sources.extra_json verbatim and are reassigned on the DB read
  // path, so both loaders agree without a schema bump.
  payer: z.string().min(1).optional(),
  amount_czk: z.number().nonnegative().optional(),
  unit: z.enum(PRICE_UNITS).optional(),
  basis: z.enum(PRICE_BASES).optional(),
}).check((ctx) => {
  const s = ctx.value;
  const fields = ["payer", "amount_czk", "unit", "basis"] as const;
  if (s.type === "price") {
    const missing = fields.filter((k) => s[k] === undefined);
    if (missing.length) {
      ctx.issues.push({
        code: "custom",
        message: `price source ${s.url} is missing ${missing.join(", ")} — a price receipt ` +
          `names who pays, how much, per what and on what basis, or it is not a receipt`,
        input: s,
      });
    }
    // A price is not a budget. It cites money only when tagged, and never
    // proof, gap, urgency or demand — those are other questions (MATCH.md §9).
    const bad = (s.dims ?? []).filter((d) => d !== "money");
    if (bad.length) {
      ctx.issues.push({
        code: "custom",
        message: `price source ${s.url} cites ${bad.join(", ")} — a price receipt may carry ` +
          `dims: [money] only`,
        input: s,
      });
    }
  } else {
    const stray = fields.filter((k) => s[k] !== undefined);
    if (stray.length) {
      ctx.issues.push({
        code: "custom",
        message: `${s.type} source ${s.url} carries ${stray.join(", ")} — price fields render ` +
          `only on a type: price source; change the type or drop them`,
        input: s,
      });
    }
  }
});
export type ProblemSource = z.infer<typeof SourceSchema>;

/** A `type: price` source with its four receipt fields narrowed to present. */
export type PriceReceipt = ProblemSource & {
  payer: string; amount_czk: number; unit: PriceUnit; basis: PriceBasis;
};

/** The price receipts on a record, in S-number order, each with its 1-based
 *  S-number. SourceSchema's check guarantees the four fields on every price
 *  source, so the narrowing below never drops a row in practice; it is written
 *  as a filter anyway because "undefined pays undefined CZK" is exactly the
 *  class of rendered sentence the schema exists to prevent. */
export function priceReceipts(p: Problem): { n: number; s: PriceReceipt }[] {
  return p.sources
    .map((s, i) => ({ n: i + 1, s }))
    .filter((x): x is { n: number; s: PriceReceipt } =>
      x.s.type === "price" && x.s.payer !== undefined && x.s.amount_czk !== undefined &&
      x.s.unit !== undefined && x.s.basis !== undefined);
}

// DIFFICULTY TO ENTER — the gates an entrant must pass before it can sell
// (owner, 2026-09-15; CONVENTIONS.md, "`entry` — difficulty to enter"). It
// REPLACES the `build` scorecard, whose capital ladder and team band the owner
// struck out as "pretty arbitrary": a euro range and a headcount were a
// prediction about a team nobody has met, where these five are facts about the
// market the record already carries evidence for.
//
// `level` is DERIVED from the other five, and `incumbents` is DERIVED from
// `locals[]` — both mechanically, both asserted in scripts/check-records.py,
// which is where the derivation lives. This schema types the vocabulary; it
// does not re-implement the rule, because a rule stated twice is a rule that
// can disagree with itself.
export const ENTRY_LEVELS = ["easy", "moderate", "hard", "very-hard"] as const;
export const ENTRY_BUYERS = ["small-firms", "large-firms", "public"] as const;
export const ENTRY_PERMISSIONS = ["none", "registration", "licence"] as const;
export const ENTRY_INCUMBENTS = ["open", "adjacent", "direct"] as const;
export const ENTRY_INTEGRATIONS = ["software", "national-system", "certified"] as const;
export const ENTRY_MONEY = ["bootstrap", "outside-money"] as const;
export type EntryLevel = (typeof ENTRY_LEVELS)[number];
export type EntryBuyer = (typeof ENTRY_BUYERS)[number];
export type EntryPermission = (typeof ENTRY_PERMISSIONS)[number];
export type EntryIncumbents = (typeof ENTRY_INCUMBENTS)[number];
export type EntryIntegration = (typeof ENTRY_INTEGRATIONS)[number];
export type EntryMoney = (typeof ENTRY_MONEY)[number];

const EntrySchema = z.object({
  level: z.enum(ENTRY_LEVELS),
  buyer: z.enum(ENTRY_BUYERS),
  permission: z.enum(ENTRY_PERMISSIONS),
  incumbents: z.enum(ENTRY_INCUMBENTS),
  integration: z.enum(ENTRY_INTEGRATIONS),
  money: z.enum(ENTRY_MONEY),
  // One or two plain sentences naming the gate(s) that set the level. The cap
  // is the section's, not a database limit: it renders as one `p.buildnote`
  // under the ledger and a paragraph there is a different device.
  why: z.string().min(1).max(320),
});
export type Entry = z.infer<typeof EntrySchema>;

// Foreign comparables — who runs this model elsewhere, with public traction on file.
const CompSchema = z.object({
  name: z.string().min(1),
  url: z.string().url(),
  geo: z.string().regex(/^[A-Z]{2}$/, "ISO2 country code"),
  since: z.number().int().min(1980).max(2100),
  traction: z.string().min(1),
  signal: z.string().optional(),
  // Operating countries beyond the HQ — recorded only when sourced (CONVENTIONS.md).
  markets: z.array(z.string().regex(/^[A-Z]{2}$/)).optional(),
});

// Local incumbents — who already sells this HERE. The mirror of `comps`, and it
// exists because the asymmetry between the two was what let a bug ship: 69
// foreign comparables carried structured `since` + `traction`, while every
// local player lived as PROSE inside a gap-check `note:`. A machine could read
// the foreign half of the register and not the local half, so `gap` could not
// be audited and `gap: 0` silently meant two opposite things.
//
// TWO ORTHOGONAL FIELDS, BECAUSE ONE FIELD CARRIED TWO MEANINGS. `status:
// established | early` shipped for exactly one commit and both content agents
// hit the same wall independently: a mature Czech firm that sells something
// ADJACENT — the other side of the counter, a different segment, a service
// rather than a product — is not "early", but calling it `established` forced
// `gap: 0` and de-ranked a record over a company that does not sell this. One
// agent wrote those firms down as `early` (a false maturity claim); the other
// left them out of the ledger entirely (a false absence). Two halves of the
// register encoding the same situation two different ways is the defect this
// line of work has already fixed three times — PROOF rung 2, GAP rung 0, the
// SPEC de-rank rule — so it is split rather than worked around a fourth time.
//
//   `competes` — DOES IT SELL THIS? direct = this product to this buyer.
//                adjacent = a real player in the neighbourhood that sells
//                something else. THE ONLY FIELD `gap` READS FOR ELIGIBILITY.
//   `maturity` — HOW OLD AND HOW PROVEN? the ESTABLISHED test from SCORING.md,
//                unchanged and machine-checked. Sets the RUNG once `competes`
//                has decided the entry counts at all.
//
// An `adjacent` player NEVER moves gap, at any maturity. That is the whole
// point of the split. It is still RECORDED — the owner's ruling, 2026-08-25:
// "Never exclude — the goal is to inform the builder properly." A builder
// needs to see who else is in the room; the adjacent half of the ledger is
// market intelligence, not noise, and dropping it to protect a score is how
// the register would start lying by omission.
const LocalSchema = z.strictObject({
  name: z.string().min(1),
  // OPTIONAL — but only against an `ico` (see the refinement below). It became
  // optional under the no-exclude ruling: AML solutions s.r.o. (IČO 10691766)
  // is a real player on p-0006 with no product URL anywhere in the corpus, and
  // the choice was to drop a real firm or invent a link. Both are forbidden, so
  // the third option is the one taken — the page links its ARES record, which
  // is verifiable and real. See `localHref`.
  url: z.string().url().optional(),
  // IČO — optional but strongly preferred: it is the only key that makes the
  // claim verifiable without a human. With it, the distinct-public-buyer limb
  // of the established test runs against data/lookup/cz-contract-parties.jsonl;
  // without it, that limb simply cannot be evaluated for this player.
  ico: z.string().regex(/^\d{8}$/, "IČO is 8 digits, quoted (leading zeros are real)").optional(),
  // The year it started selling THIS product, else its founding year. Unquoted
  // integer, exactly like comps[].since — the site reads it as a number.
  //
  // OPTIONAL, AND ONLY IN THE EARLY DIRECTION (see the refinement below). The
  // established test's first limb is ">= 3 years selling", so `established`
  // without a year is a claim with no receipt and is refused. An EARLY player
  // may have no discoverable founding year — small Czech SMB vendors routinely
  // do not publish one — and the house rule there is the same as for a comp's
  // headcount: state what is verifiable, NEVER invent the rest. Forcing a year
  // into this field would buy schema tidiness with a fabricated fact.
  since: z.number().int().min(1980).max(2100).optional(),
  competes: z.enum(["direct", "adjacent"]),
  maturity: z.enum(["established", "early"]),
  // At `direct`: which limb(s) of the established test this player passes,
  // stated so a reader can check it. At `adjacent`: WHAT IT ACTUALLY SELLS and
  // why that is not this — the sentence that turns an entry a reader would
  // otherwise read as a competitor into the thing it is, intelligence about the
  // neighbourhood. Enforced as a required sentence by scripts/check-records.py.
  evidence: z.string().min(1),
}).check((ctx) => {
  const l = ctx.value;
  if (l.maturity === "established" && l.since === undefined) {
    ctx.issues.push({
      code: "custom",
      message: `local '${l.name}' is established but has no 'since' — the established ` +
        `test's first limb is ">= 3 years selling" and cannot be evaluated without it`,
      input: l,
    });
  }
  // A ledger row a reader cannot follow is an assertion, not evidence. One of
  // the two identifiers must be present so every entry links somewhere real.
  if (l.url === undefined && l.ico === undefined) {
    ctx.issues.push({
      code: "custom",
      message: `local '${l.name}' has neither 'url' nor 'ico' — one is required so the ` +
        `entry links to something verifiable (the site falls back to the ARES record)`,
      input: l,
    });
  }
});
export type Local = z.infer<typeof LocalSchema>;

/** Where a local-competition entry links.
 *
 *  The product site when there is one; otherwise the company's ARES record,
 *  which is a public state register page keyed by the IČO the entry already
 *  carries. NOT a fallback of convenience — it is what makes the no-exclude
 *  rule honest. A real player with no discoverable product page (they exist:
 *  s.r.o. compliance shops that sell through partners and publish nothing) can
 *  now be recorded and still be checked by a reader in one click, instead of
 *  being dropped from the ledger or given an invented URL.
 *
 *  LocalSchema guarantees one of the two exists, so this is total. */
export function localHref(l: Local): string {
  return l.url ?? `https://ares.gov.cz/ekonomicke-subjekty?ico=${l.ico}`;
}

// THE PROCESS — how the work runs TODAY, and how it would run with the
// suggested solution (owner, 2026-09-15). OPTIONAL: authored only where the
// problem is a workflow someone performs today; a new obligation or a one-off
// decision has no current process and carries no block. The page reads it in
// SEQUENCE: `summary.today` and the steps' today column under the problem,
// then the Suggested solution box, which holds the steps with the solution
// applied (and `summary.after` when the author wrote one).
//
// UNCERTAINTY IS DATA HERE, NOT A FOOTNOTE — owner: "be SUPER CLEAR about
// where we're not sure how the process looks, put question marks if you don't
// know". So every step says how its TODAY column is known, in one field:
//   `documented` — stated in cited evidence; `cites` non-empty, every S-number
//                  resolving into sources[]
//   `inferred`   — our reading of the record's prose, not stated in evidence;
//                  drawn with a "?"; `cites` may name where the reading comes from
//   `unknown`    — we do not know how this step happens; `cites` empty and
//                  `today` states the open question ("Who files the claim is not
//                  documented"); `who` may be '?'
// On a `change: new` step there is no today to describe, so `known` says how
// sure we are that nobody does the step today — usually `inferred`.
// `after` is ALWAYS the proposal, never evidence: it carries no citations of
// any kind and the page labels it uncited.
//
// ONE FIELD, ONE MEANING (CLAUDE.md rule 1): the block describes the workflow
// and nothing else. Scores, money and competition have their own fields, and
// scripts/check-records.py refuses a crown figure or a comps[]/locals[] name
// inside it. That file owns every rule below in full; this schema types the
// shape and carries the refinements the renderer relies on (nullability per
// `change`, the known-vs-cites pairing), so neither loader can hand the page a
// step it would have to guess about.
//
// NOT A COLUMN in scripts/db.py: it rides problems.extra_json verbatim (key-
// sorted there) and comes back through the Object.assign in problemsFromDb.
// Safe for `npm run parity` because zod emits object keys in SHAPE order, not
// input order — measured on zod 4.4, 2026-09-15.
export const PROCESS_KNOWN = ["documented", "inferred", "unknown"] as const;
export const PROCESS_CHANGES = ["stays", "changes", "goes", "new"] as const;
export type ProcessKnown = (typeof PROCESS_KNOWN)[number];
export type ProcessChange = (typeof PROCESS_CHANGES)[number];

const ProcessStepSchema = z.strictObject({
  /** Who does the step TODAY, in plain words ('?' when unknown). On a
      `change: new` step, who would do it with the suggested solution. */
  who: z.string().min(1),
  /** Today's step. null ONLY on `change: new` — the solution adds it. */
  today: z.string().min(1).nullable(),
  known: z.enum(PROCESS_KNOWN),
  /** S-numbers into sources[] (S1 = sources[0]) backing `today`. Always
      present; `[]` when none. Never cites `after`. */
  cites: z.array(z.number().int().positive()),
  /** Today's step re-types or re-reads what someone already wrote. */
  reenters: z.boolean().optional(),
  change: z.enum(PROCESS_CHANGES),
  /** The step with the suggested solution applied — a proposal, uncited.
      null ONLY on `change: goes` — the solution removes it. */
  after: z.string().min(1).nullable(),
}).check((ctx) => {
  const s = ctx.value;
  const issue = (message: string) => ctx.issues.push({ code: "custom", message, input: s });
  if (s.change === "new" ? s.today !== null : s.today === null)
    issue(`process step '${s.who}': today must be null exactly when change is 'new' ` +
      `(a step the solution adds has no today; every other step does)`);
  if (s.change === "goes" ? s.after !== null : s.after === null)
    issue(`process step '${s.who}': after must be null exactly when change is 'goes' ` +
      `(a step the solution removes has no after; every other step does)`);
  if (s.known === "documented" && s.cites.length === 0)
    issue(`process step '${s.who}': known 'documented' needs cites — a step stated in ` +
      `evidence names the evidence; without it, it is 'inferred'`);
  if (s.known === "unknown" && s.cites.length > 0)
    issue(`process step '${s.who}': known 'unknown' carries cites — a source that ` +
      `describes the step makes it documented or inferred, not unknown`);
  if (s.reenters === true && s.today === null)
    issue(`process step '${s.who}': reenters on a 'new' step — there is no today to re-enter`);
});
export type ProcessStep = z.infer<typeof ProcessStepSchema>;

const ProcessSchema = z.strictObject({
  summary: z.strictObject({
    /** One plain sentence: the process today. May carry [Sn] markers; where
        part of it is unknown, the sentence says so. REQUIRED. */
    today: z.string().min(1),
    /** One plain sentence on the process with the solution applied — OPTIONAL,
        written only when it adds what the `solution` sentence does not say.
        Uncited, no certainty words. */
    after: z.string().min(1).optional(),
  }),
  steps: z.array(ProcessStepSchema).min(2),
});
export type Process = z.infer<typeof ProcessSchema>;

const ProblemSchema = z.looseObject({
  id: z.string().regex(/^p-\d{4}$/),
  region: z.string().regex(/^[a-z]{2}$/),
  title: z.string().min(1),
  // `solution` — the SUGGESTED solution in ONE plain sentence, rendered directly
  // under the dek and ALWAYS labelled "Suggested solution" (owner, 2026-09-10:
  // "don't try to make it like we know everything"; labelled "Likely solution"
  // until 2026-09-15, when "Suggested" took over because it owns the sentence
  // as our proposal and the box now also carries the proposed process). A FIRST-CLASS FIELD, not
  // derived prose: the dek is compressed out of the who-pays paragraph, this is
  // authored. REQUIRED since 2026-09-10 (was the optional `fix`, 2026-08-25):
  // it answers "what would likely solve this problem?", which every record can
  // answer — whether that answer is still open to an entrant is the gap
  // score's question, never this field's. Carried as a NOT NULL column in
  // scripts/db.py (`problems.solution`), so it cannot vanish on the DB path.
  solution: z.string().min(1),
  // `brief` — THE HEADLINE'S SITUATION LINE (owner, 2026-09-16). OPTIONAL.
  // The page reads title → brief → solution ("Suggested") → good_for, and the
  // owner's cap is "3 bullets at most" per problem: brief, Suggested, Good for.
  // So `brief` is ONE STRING, one sentence of about 25 words at most, saying
  // WHAT IS HAPPENING and WHY IT IS URGENT NOW: who is affected, the date, the
  // penalty, the shortage. Facts only — one field, one meaning: no solution
  // talk (that is `solution`), no competitor names (that is comps[]/locals[]),
  // no certainty words. Every numeric claim or date carries an [Sn] marker
  // resolving into sources[]; the marker check is below, the full rule set
  // (one sentence, word cap, cite-on-number, OVERCLAIM, ledger names) is in
  // scripts/check-records.py.
  //
  // NOT A COLUMN in scripts/db.py: rides problems.extra_json exactly like
  // `process` and comes back through the Object.assign in problemsFromDb.
  brief: z.string().min(1).optional(),
  // `good_for` — WHO THE OPPORTUNITY SUITS, by skills and interests, in one
  // line (owner, 2026-09-16). OPTIONAL. "Cybersecurity people interested in
  // grants and public-sector sales." A description of a person, never of the
  // market: no numbers, no [Sn] markers, no certainty words (check-records.py).
  // Rides problems.extra_json, like `brief`.
  good_for: z.string().min(1).optional(),
  // `price_search` — WHERE TO LOOK for the price when no Czech buyer has yet
  // priced this (owner, 2026-09-04: "we don't need to answer where the money
  // is where we don't know it; we can give an estimate of where to search").
  // One sentence naming the surfaces and the keyword — a registr smluv
  // query, an MS2021+ index keyword, a named buyer to ask. It is an
  // ESTIMATE OF WHERE, never an estimate of HOW MUCH: a number belongs on a
  // `type: price` source with a url, or nowhere. Renders beside the absence
  // line only; absent when a price receipt exists.
  price_search: z.string().min(1).optional(),
  category: z.enum(CATEGORIES),
  geo: z.string().min(1),
  score: z.number().int().min(0).max(12),
  scores: z.object({
    proof: z.number().int().min(0).max(3),
    money: z.number().int().min(0).max(2),
    urgency: z.number().int().min(0).max(3),
    demand: z.number().int().min(0).max(2),
    gap: z.number().int().min(0).max(2),
  }),
  status: z.enum(STATUSES),
  // Required since the 2026-08 product upgrade — no record may skip the
  // difficulty-to-enter block or the comparables ledger (SPEC.md §4). Every
  // key inside `entry` is required too, rejected records included: a gate with
  // no value is the shape that looks present and says nothing.
  entry: EntrySchema,
  comps: z.array(CompSchema),
  // `locals` — the local-incumbent ledger, rendered under "Local competition"
  // the way `comps` renders under "Proven abroad". OPTIONAL, and the two
  // absences are NOT the same fact: an absent key means no named local player
  // is on file, which is legitimate at `gap: 1` and `gap: 2`; at `gap: 0` it is
  // a MISSING RECEIPT, and scripts/check-records.py fails the build on it.
  // WRITE THE KEY ABSENT, NEVER `locals: []` — a child table cannot tell an
  // empty list from a missing key, so db.py refuses the empty form outright
  // rather than let the two loaders disagree (see `problem_locals`).
  locals: z.array(LocalSchema).optional(),
  // `process` — the before/after workflow figure (2026-09-15). OPTIONAL; see
  // ProcessSchema above. Absent means the record describes no workflow.
  process: ProcessSchema.optional(),
  sources: z.array(SourceSchema).min(1),
  created: isoDate,
  updated: isoDate,
}).check((ctx) => {
  const p = ctx.value;
  const sum = p.scores.proof + p.scores.money + p.scores.urgency + p.scores.demand + p.scores.gap;
  if (sum !== p.score) {
    ctx.issues.push({ code: "custom", message: `score ${p.score} != sum(scores) ${sum}`, input: p });
  }
  // A brief marker is a link the page draws into the Sources ledger, and the
  // compound form `[S1,S19]` names several — read every number, not the first.
  if (p.brief !== undefined) {
    const nums = (p.brief.match(/\[S[\d,S]+\]/g) ?? []).flatMap((m) => (m.match(/\d+/g) ?? []).map(Number));
    const dead = nums.filter((n) => n < 1 || n > p.sources.length);
    if (dead.length) {
      ctx.issues.push({
        code: "custom",
        message: `brief cites ${dead.map((n) => `S${n}`).join(", ")} — ` +
          `${p.sources.length} sources on file`,
        input: p,
      });
    }
  }
  // A process cite is a link the page draws into the Sources ledger; one that
  // points past the end of sources[] would link nowhere.
  for (const s of p.process?.steps ?? []) {
    const dead = s.cites.filter((n) => n > p.sources.length);
    if (dead.length) {
      ctx.issues.push({
        code: "custom",
        message: `process step '${s.who}' cites ${dead.map((n) => `S${n}`).join(", ")} — ` +
          `${p.sources.length} sources on file`,
        input: p,
      });
    }
  }
  // proof >= 1 asserts a foreign analog exists — the comps ledger must name at least one.
  if (p.comps && p.scores.proof >= 1 && p.comps.length === 0) {
    ctx.issues.push({ code: "custom", message: `proof ${p.scores.proof} >= 1 but comps is empty — name the analog or justify proof 0`, input: p });
  }
});
export type Problem = z.infer<typeof ProblemSchema> & { body: string; slug: string };

// ---- loaders (module-level cache; build-time only) -----------------------

function parseFrontmatter(raw: string, file: string): { fm: unknown; body: string } {
  if (!raw.startsWith("---\n")) throw new Error(`${file}: missing frontmatter`);
  const end = raw.indexOf("\n---\n", 4);
  if (end === -1) throw new Error(`${file}: unterminated frontmatter`);
  return { fm: yamlLoad(raw.slice(4, end)), body: raw.slice(end + 5).trim() };
}

function fail(file: string, error: z.ZodError): never {
  throw new Error(`${file}: ${error.issues.map((i) => `${i.path.join(".")}: ${i.message}`).join("; ")}`);
}

function problemsFromJsonl(): Problem[] {
  const problems: Problem[] = [];
  const problemsDir = join(DATA, "problems");
  for (const region of readdirSync(problemsDir, { withFileTypes: true })) {
    if (!region.isDirectory()) continue;
    for (const f of readdirSync(join(problemsDir, region.name)).sort()) {
      if (!f.endsWith(".md")) continue;
      const file = `data/problems/${region.name}/${f}`;
      const { fm, body } = parseFrontmatter(readFileSync(join(problemsDir, region.name, f), "utf8"), file);
      const parsed = ProblemSchema.safeParse(fm);
      if (!parsed.success) fail(file, parsed.error);
      if (parsed.data.region !== region.name)
        throw new Error(`${file}: region '${parsed.data.region}' != directory '${region.name}'`);
      problems.push({ ...parsed.data, body, slug: f.replace(/\.md$/, "") });
    }
  }
  return problems;
}

/** `null` in SQLite means "the key was absent from the frontmatter"; the schemas
    want the key gone, not present-and-null. Assigns only when there is a value. */
function put(o: Record<string, unknown>, key: string, v: unknown): void {
  if (v !== null && v !== undefined) o[key] = v;
}

/** Same as `put`, but the stored value is a JSON document.
 *
 *  THE THREE STATES ARE ALL LOAD-BEARING and this is the only place they are
 *  told apart: `NULL` = key absent (fall through to the type map in
 *  scorecard.ts `dimRefs`), `'[]'` = key present and empty — the deliberate
 *  "attach to nothing" opt-out carried by 4 live sources — and `'["money"]'` =
 *  an explicit override. `dimRefs` early-returns on ANY present `dims` key, so
 *  collapsing absent and empty into one state re-attaches those 4 sources to
 *  Demand and changes /problem/cz/p-0018. A join table cannot represent this;
 *  the JSON column can. */
function putJson(o: Record<string, unknown>, key: string, v: unknown): void {
  if (v !== null && v !== undefined) o[key] = JSON.parse(String(v));
}

function problemsFromDb(): Problem[] {
  const srcRows = rows(
    "SELECT region, problem_id, position, type, url, note, date, name, why, gist, signal_id," +
    " dims_json, queries_json, checked_json, expires, extra_json FROM problem_sources"
  );
  const compRows = rows(
    "SELECT region, problem_id, position, name, url, geo, since, traction," +
    " signal_id, markets_json FROM problem_comps"
  );
  const localRows = rows(
    "SELECT region, problem_id, position, name, url, ico, since, competes," +
    " maturity, evidence FROM problem_locals"
  );

  // Group children by their parent, then order each group by `position` — which
  // IS the S-number and is never reassigned (480 live [Sn] citation markers key
  // off array position). Numeric sort: no collation is involved.
  const byParent = (rs: SqliteRow[]) => {
    const m = new Map<string, SqliteRow[]>();
    for (const r of rs) {
      const k = `${String(r.region)}/${String(r.problem_id)}`;
      (m.get(k) ?? m.set(k, []).get(k)!).push(r);
    }
    for (const g of m.values()) g.sort((a, b) => Number(a.position) - Number(b.position));
    return m;
  };
  const sourcesFor = byParent(srcRows);
  const compsFor = byParent(compRows);
  const localsFor = byParent(localRows);

  const problems: Problem[] = [];
  for (const r of rows(
    "SELECT region, id, slug, title, solution, category, geo, status, score," +
    " s_proof, s_money, s_urgency, s_demand, s_gap," +
    " entry_level, entry_buyer, entry_permission, entry_incumbents," +
    " entry_integration, entry_money, entry_why," +
    " created, updated, body, extra_json, md_file FROM problems"
  )) {
    const key = `${String(r.region)}/${String(r.id)}`;
    const file = String(r.md_file);

    const fm: Record<string, unknown> = {
      id: String(r.id),
      region: String(r.region),
      title: String(r.title),
      category: String(r.category),
      geo: String(r.geo),
      score: Number(r.score),
      scores: {
        proof: Number(r.s_proof), money: Number(r.s_money), urgency: Number(r.s_urgency),
        demand: Number(r.s_demand), gap: Number(r.s_gap),
      },
      status: String(r.status),
      entry: {
        level: String(r.entry_level), buyer: String(r.entry_buyer),
        permission: String(r.entry_permission), incumbents: String(r.entry_incumbents),
        integration: String(r.entry_integration), money: String(r.entry_money),
        why: String(r.entry_why),
      },
      comps: (compsFor.get(key) ?? []).map((c) => {
        const comp: Record<string, unknown> = {
          name: String(c.name), url: String(c.url), geo: String(c.geo),
          // YAML wrote this unquoted, so it MUST come back a JS number, not the
          // string SQLite would happily coerce. `since: "2020"` fails z.number().
          since: Number(c.since),
          traction: String(c.traction),
        };
        put(comp, "signal", c.signal_id === null ? null : String(c.signal_id));
        putJson(comp, "markets", c.markets_json);
        return comp;
      }),
      sources: (sourcesFor.get(key) ?? []).map((s) => {
        const src: Record<string, unknown> = {
          type: String(s.type), url: String(s.url), note: String(s.note), date: String(s.date),
        };
        put(src, "name", s.name === null ? null : String(s.name));
        put(src, "why", s.why === null ? null : String(s.why));
        put(src, "gist", s.gist === null ? null : String(s.gist));
        put(src, "signal", s.signal_id === null ? null : String(s.signal_id));
        putJson(src, "dims", s.dims_json);
        putJson(src, "queries", s.queries_json);
        putJson(src, "checked", s.checked_json);
        put(src, "expires", s.expires === null ? null : String(s.expires));
        // SourceSchema is looseObject: any key the frontmatter carried that db.py
        // has no column for survives the round trip verbatim. Since 2026-09-03
        // this is how the four price-receipt fields (payer, amount_czk, unit,
        // basis) travel — typed above, validated by the check, stored here.
        if (s.extra_json !== null) Object.assign(src, JSON.parse(String(s.extra_json)));
        return src;
      }),
      created: String(r.created),
      updated: String(r.updated),
    };
    // `solution` is required: a NOT NULL column, so it is always present.
    put(fm, "solution", String(r.solution));

    // `locals` is optional too, and a CHILD TABLE cannot represent the
    // difference between an absent key and an empty list — zero rows is the
    // only spelling of both. So the key is set ONLY when rows exist, and db.py
    // refuses `locals: []` in the frontmatter outright, which is what makes
    // this branch total rather than lossy: the state it cannot round-trip is
    // the one state the journal is not allowed to contain.
    const locals = (localsFor.get(key) ?? []).map((l) => {
      const loc: Record<string, unknown> = {
        name: String(l.name),
        competes: String(l.competes), maturity: String(l.maturity),
        evidence: String(l.evidence),
      };
      // `url` is optional against an `ico` (LocalSchema): NULL means the key was
      // absent in the frontmatter, and it must come back ABSENT, not
      // present-and-null — the JSONL loader would never produce `url: null`, so
      // neither may this one, and the site links the ARES record instead.
      put(loc, "url", l.url === null ? null : String(l.url));
      // The IČO is TEXT and stays TEXT: '04903783' is a real IČO and Number()
      // would eat its leading zero.
      put(loc, "ico", l.ico === null ? null : String(l.ico));
      // `since` is an unquoted YAML integer, exactly as with comps[].since:
      // SQLite would hand back a string just as happily, and `since: "1993"`
      // fails zod. NULL stays ABSENT — an early player with no discoverable
      // year has no year, not a year of null.
      put(loc, "since", l.since === null ? null : Number(l.since));
      return loc;
    });
    if (locals.length) fm.locals = locals;
    if (r.extra_json !== null) Object.assign(fm, JSON.parse(String(r.extra_json)));

    const parsed = ProblemSchema.safeParse(fm);
    if (!parsed.success) fail(file, parsed.error);

    // The JSONL path gets frontmatter-vs-path agreement for free from the
    // directory walk. Re-derive it here from `md_file` rather than let the
    // check go vacuous — the `region` column and `fm.region` are the same value
    // by construction, so comparing them would prove nothing.
    const m = /^data\/problems\/([^/]+)\/(.+)\.md$/.exec(file);
    if (!m) throw new Error(`${file}: md_file is not data/problems/<region>/<slug>.md`);
    if (m[1] !== parsed.data.region)
      throw new Error(`${file}: region '${parsed.data.region}' != directory '${m[1]}'`);
    if (m[2] !== String(r.slug))
      throw new Error(`${file}: slug '${String(r.slug)}' != filename '${m[2]}'`);

    problems.push({ ...parsed.data, body: String(r.body), slug: String(r.slug) });
  }

  // Mirrors the JSONL walk: regions outer, then `readdirSync().sort()` over the
  // filenames — which is what `slug` is. (With one region today the region key
  // is inert; the JSONL path leaves region order to the filesystem, so a SECOND
  // region is a parity risk on that path, not this one. Noted, not fixed here.)
  return problems.sort((a, b) => cmp(a.region, b.region) || cmp(a.slug, b.slug));
}

let _problems: Problem[] | null = null;
export function getProblems(): Problem[] {
  if (_problems) return _problems;
  const problems = announce() === "db" ? problemsFromDb() : problemsFromJsonl();
  const ids = new Set<string>();
  for (const p of problems) {
    const key = `${p.region}/${p.id}`;
    if (ids.has(key)) throw new Error(`duplicate problem id ${key}`);
    ids.add(key);
  }
  _problems = problems;
  // comp signal refs must resolve into the evidence layer — a broken provenance link is a build failure.
  for (const p of problems) {
    for (const c of p.comps ?? []) {
      if (c.signal && !getSignal(c.signal)) {
        throw new Error(`${p.region}/${p.id}: comp '${c.name}' refs unknown signal '${c.signal}'`);
      }
    }
  }
  return problems;
}

function signalsFromJsonl(): Signal[] {
  const signals: Signal[] = [];
  for (const type of EVIDENCE_TYPES) {
    const dir = join(DATA, "signals", type);
    if (!existsSync(dir)) continue; // a pending feed is a registered fact — its page renders empty
    for (const f of readdirSync(dir).sort()) {
      if (!f.endsWith(".jsonl")) continue;
      const lines = readFileSync(join(dir, f), "utf8").split("\n").filter(Boolean);
      for (const [n, line] of lines.entries()) {
        const parsed = SignalSchema.safeParse(JSON.parse(line));
        if (!parsed.success) fail(`data/signals/${type}/${f}:${n + 1}`, parsed.error);
        signals.push({ ...parsed.data, type });
      }
    }
  }
  return signals;
}

function signalsFromDb(): Signal[] {
  // `raw` is the VERBATIM ledger line and it is the only signal payload this
  // loader reads (`owner` is selected beside it, but only to be checked against
  // it — see below). Not the derived entity keys, not `dup_of`, and above all not
  // data/errata.jsonl — the corrections ledger is real, committed, and consumed
  // by db.py's money aggregates, but the web build has never rendered it.
  // Picking it up here would silently restate EUR 10000M on /signals/tenders as
  // something else: a genuine improvement, an instant parity failure, and a
  // content change nobody reviewed.
  const rs = rows("SELECT id, type, jsonl_file, jsonl_line, raw, owner FROM signals");

  // Reproduces the JSONL walk exactly: EVIDENCE_TYPES order (the outer loop),
  // then filename (`readdirSync().sort()`), then line number. In JS, never as
  // ORDER BY — see the note on `cmp` and on `rows` in ./db.
  const rank = (t: string) => {
    const i = (EVIDENCE_TYPES as readonly string[]).indexOf(t);
    // The JSONL path only ever walks the EVIDENCE_TYPES directories, so a row
    // of some other type is invisible there and would be a silent divergence
    // here. Refuse it instead.
    if (i === -1) throw new Error(`register.db: signal type '${t}' is not in EVIDENCE_TYPES`);
    return i;
  };
  rs.sort((a, b) =>
    rank(String(a.type)) - rank(String(b.type)) ||
    cmp(String(a.jsonl_file), String(b.jsonl_file)) ||
    Number(a.jsonl_line) - Number(b.jsonl_line)
  );

  const signals: Signal[] = [];
  for (const r of rs) {
    const parsed = SignalSchema.safeParse(JSON.parse(String(r.raw)));
    if (!parsed.success) fail(`${String(r.jsonl_file)}:${Number(r.jsonl_line)} (via register.db)`, parsed.error);
    // `owner` IS a projected column (schema_version 9), and it is read back
    // here — as a WITNESS, not as the value. The record is still built from
    // `raw` alone, so parity with the journal cannot be moved by this read;
    // what the read adds is a second copy of one fact, cut by db.py at write
    // time, that must agree with the line it was cut from. A disagreement
    // means the projection and the ledger have parted — the class of defect
    // the seen.txt check below exists to catch — and it is a build failure,
    // never a silent preference for one side.
    const projected = r.owner === null ? undefined : String(r.owner);
    if (projected !== parsed.data.owner)
      throw new Error(
        `${String(r.jsonl_file)}:${Number(r.jsonl_line)} (via register.db): signals.owner is ` +
        `${JSON.stringify(projected)} but the ledger line carries ${JSON.stringify(parsed.data.owner)}.\n` +
        "The working store disagrees with the journal it projects — rebuild it:  python3 scripts/db.py rebuild"
      );
    signals.push({ ...parsed.data, type: String(r.type) as EvidenceType });
  }
  return signals;
}

let _signals: Signal[] | null = null;
export function getSignals(): Signal[] {
  if (_signals) return _signals;
  const src = announce();
  const signals = src === "db" ? signalsFromDb() : signalsFromJsonl();
  // READ FROM DISK IN BOTH PATHS, DELIBERATELY. Deriving seen.txt from the same
  // database the signals came from would make this check assert a table against
  // itself. It is one of the few checks in this file with a demonstrated
  // ability to fail, and it only has that because the two sides are independent.
  const seen = new Set(readFileSync(join(DATA, "signals", "seen.txt"), "utf8").split("\n").filter(Boolean));
  const ids = new Set<string>();
  for (const s of signals) {
    if (ids.has(s.id)) throw new Error(`duplicate signal id ${s.id}`);
    ids.add(s.id);
    if (!seen.has(s.id)) throw new Error(`signal ${s.id} missing from data/signals/seen.txt`);
  }
  // ...AND THE CONVERSE, ON THE DB PATH ONLY. The loop above asserts
  // loaded-implies-seen; it says NOTHING about a record that failed to arrive.
  // On the JSONL path that gap is harmless — the ledger files ARE the corpus,
  // so nothing can go missing without a visible ledger edit. On the DB path the
  // corpus is a projection, and a projection can come up short: MEASURED, a
  // single `DELETE FROM signals` built GREEN and shipped 6,180 of 6,181 records.
  // `db.py rebuild` does assert jsonl_lines == signals_count, but that is the
  // writer vouching for itself at write time and it is not re-checked at read
  // time — the store was already once found 7+ commits stale while reporting
  // success. seen.txt is the independent on-disk witness: architecture-v3 §
  // "seen.txt is written only on append" makes it exactly the committed id set,
  // measured today as 6,181 == 6,181 with an empty symmetric difference.
  //
  // DB PATH ONLY, deliberately: this must not be able to newly fail the
  // reference implementation mid-migration. Its one failure mode — the working
  // store holding fewer records than the committed dedup index — is, under the
  // append-only law, always a real defect.
  if (src === "db" && ids.size !== seen.size) {
    const missing = [...seen].filter((id) => !ids.has(id));
    throw new Error(
      `register.db holds ${ids.size} signals but data/signals/seen.txt lists ${seen.size}` +
      `${missing.length ? ` — missing: ${missing.slice(0, 5).join(", ")}${missing.length > 5 ? ` (+${missing.length - 5} more)` : ""}` : ""}.\n` +
      "The working store is short of the committed ledgers — rebuild it:  python3 scripts/db.py rebuild"
    );
  }
  _signals = signals;
  return signals;
}

export function getSignal(id: string): Signal | undefined {
  return getSignals().find((s) => s.id === id);
}

// ---- derived views -------------------------------------------------------

/** Extract date = newest `updated` across the register (deterministic, no wall clock). */
export function extractDate(): string {
  return getProblems().map((p) => p.updated).sort().at(-1) ?? "1970-01-01";
}

const dayMs = 86_400_000;
const daysBetween = (a: string, b: string) => Math.round((Date.parse(b) - Date.parse(a)) / dayMs);

/** Display-only split of urgency into deadline (0-2) + freshness (0-1), per SCORING.md.
    Freshness is mechanical: newest OBSERVED source < 90 days before the extract date.
 *
 *  "OBSERVED" IS LOAD-BEARING, and this is the second time this repo has been bitten
 *  by the same shape. A source `date` is the signal's own native date, and for a
 *  regulation or a subsidy call that date is a FUTURE compliance deadline — the AML
 *  Regulation sits at 2027-07-10, an NZÚ call at 2029-10-31. The previous version took
 *  the newest date of any kind, so `daysBetween(newest, extractDate())` went NEGATIVE,
 *  and negative is trivially `< 90`. Freshness was therefore incapable of returning 0
 *  for any record holding a forward-dated source: 18 of 31 records scored a free
 *  freshness point, p-0015 on a source 406 days in the future.
 *
 *  A check that cannot fail measures nothing. Freshness is supposed to answer "have we
 *  looked at this recently", so only sources we could actually have read — dated at or
 *  before the extract — count as observations. A record whose sources are ALL forward
 *  dated has made no recent observation at all and correctly scores 0.
 *
 *  This is display-only: it splits `scores.urgency` for the scorecard and never changes
 *  it. Where the split now reads deadline-heavy with no freshness, the underlying
 *  urgency score may deserve MATCH's attention — but that is a judgment, not a render. */
export function urgencySplit(p: Problem): { deadline: number; freshness: number } {
  if (p.scores.urgency === 0) return { deadline: 0, freshness: 0 };
  const observed = p.sources.map((s) => s.date).filter((d) => d <= extractDate()).sort().at(-1);
  const fresh = observed !== undefined && daysBetween(observed, extractDate()) < 90 ? 1 : 0;
  const freshness = Math.min(fresh, p.scores.urgency);
  return { deadline: Math.min(p.scores.urgency - freshness, 2), freshness };
}

/** Has a source's recorded `expires` horizon been reached? DISPLAY ONLY.
 *
 *  THE LAW (data/CONVENTIONS.md, SPEC.md §4): an expired gap-check flags
 *  staleness on the rendered page and NOTHING else. It never changes
 *  `scores.gap`, never changes `score`, never changes `status` — the SPEC §4
 *  de-rank rule stays the only mechanism that moves `gap`. Nothing in this
 *  module may feed this boolean into a number; grep its call sites before
 *  changing that.
 *
 *  It decays against `extractDate()` — the register's own newest `updated` —
 *  and NEVER against `new Date()`. A wall-clock read here would make the same
 *  commit render differently on two different days, which is a build-
 *  reproducibility bug, not a styling preference. */
export function sourceExpired(s: ProblemSource): boolean {
  return s.expires !== undefined && s.expires <= extractDate();
}

/** Register order: score desc, then deadline desc, then money desc, then id (SPEC §4).
    `stale` sinks to the bottom; `rejected` is excluded. */
export function registerRows(): Problem[] {
  const rows = getProblems().filter((p) => p.status !== "rejected");
  return rows.sort((a, b) =>
    Number(a.status === "stale") - Number(b.status === "stale") ||
    b.score - a.score ||
    urgencySplit(b).deadline - urgencySplit(a).deadline ||
    b.scores.money - a.scores.money ||
    a.id.localeCompare(b.id)
  );
}

/** Category page rows: the register order, filtered. Slug == category id (CONVENTIONS.md). */
export function categoryRows(category: string): Problem[] {
  return registerRows().filter((p) => p.category === category);
}

/** Register counts per category (rejected excluded, stale counted — mirrors registerRows). */
export function categoryCounts(): Record<string, number> {
  const counts = Object.fromEntries(CATEGORIES.map((c) => [c, 0])) as Record<string, number>;
  for (const p of registerRows()) counts[p.category] += 1;
  return counts;
}

export function signalsByType(type: EvidenceType): Signal[] {
  return getSignals()
    .filter((s) => s.type === type)
    .sort((a, b) => b.date.localeCompare(a.date) || a.id.localeCompare(b.id));
}

// ---- ledger paging -------------------------------------------------------

/** Rows per ledger page.
 *
 *  MEASURED, not guessed. At 9,273 signals the one-document ledgers emitted
 *  7,755,218 bytes for /signals/funded and 5,653,351 for /signals/tenders —
 *  1.4–2.0 kB per row, of which 65% is the RSC flight payload Next inlines
 *  beside the markup. 100 rows puts every ledger document between 120 kB and
 *  215 kB, which is the band the site's own record pages already occupy
 *  (108–171 kB) and therefore the site's own evidence that the weight reads.
 *
 *  It is also the printed-ledger page: a broadsheet ledger column holds ~50
 *  entries, two columns ~100. And it keeps every page id two digits today
 *  (01…54), so the zero-padding house tic holds without widening.
 *
 *  THE PAGE SIZE IS NOT A DISPLAY DETAIL — it decides which document holds a
 *  given row, and `signalHref` resolves in-body deep links against the SAME
 *  index that lays the pages out (below). One constant, one index: a link and
 *  the page it points at cannot disagree. */
export const LEDGER_PAGE_SIZE = 100;

/** id -> `/signals/<type>[/<page>]#<id>`, built once from the sorted ledgers.
 *  Page 1 keeps the bare `/signals/<type>` URL — it is the canonical entry,
 *  the target the retired `/sources/:type` 308 lands on, and giving it a
 *  second `/1` spelling would publish the same document at two addresses. */
let _rowHref: Map<string, string> | null = null;
function rowHrefIndex(): Map<string, string> {
  if (_rowHref) return _rowHref;
  const m = new Map<string, string>();
  for (const t of EVIDENCE_TYPES) {
    signalsByType(t).forEach((s, i) => {
      const page = Math.floor(i / LEDGER_PAGE_SIZE) + 1;
      m.set(s.id, `/signals/${t}${page > 1 ? `/${page}` : ""}#${s.id}`);
    });
  }
  _rowHref = m;
  return m;
}

/** How many pages a ledger is. An empty ledger is one (empty) page — a pending
    feed is a registered fact, so it keeps a document to be registered on. */
export function ledgerPages(type: EvidenceType): number {
  return Math.max(1, Math.ceil(signalsByType(type).length / LEDGER_PAGE_SIZE));
}

/** The rows of one ledger page, 1-based. */
export function ledgerRows(type: EvidenceType, page: number): Signal[] {
  return signalsByType(type).slice((page - 1) * LEDGER_PAGE_SIZE, page * LEDGER_PAGE_SIZE);
}

/** Where a signal's row actually lives, fragment included.
 *
 *  EVERY LINK INTO A LEDGER MUST GO THROUGH HERE. A fragment only scrolls if
 *  the row is in the document the URL names, so once the ledgers are paged an
 *  un-resolved `/signals/tenders#dotace-…` silently lands on page 1 and stops
 *  pointing at anything. Record bodies, the comps ledger's evidence refs, the
 *  record footer's provenance list and the register's next-deadline link all
 *  resolve through this index.
 *
 *  An unknown id keeps the unpaged href rather than inventing a page: the
 *  reader still reaches the right ledger, which is exactly what happened
 *  before paging. */
export function signalHref(id: string, fallbackType: EvidenceType | string): string {
  return rowHrefIndex().get(id) ?? `/signals/${fallbackType}#${id}`;
}

export function stats() {
  const problems = getProblems().filter((p) => p.status !== "rejected");
  const signals = getSignals();
  const today = extractDate();
  const deadlines = signals
    .filter((s) => s.type === "regulation" && s.date > today)
    .sort((a, b) => a.date.localeCompare(b.date));
  // Four fields, all of them rendered. `sourcesOnFile` and `deadlinesTracked`
  // were computed here and read by nobody — a count with no reader is a claim
  // no one can check, so they are gone rather than left to rot.
  return {
    open: problems.length,
    signalCount: signals.length,
    byType: Object.fromEntries(EVIDENCE_TYPES.map((t) => [t, signals.filter((s) => s.type === t).length])) as Record<EvidenceType, number>,
    nextDeadline: deadlines[0],
  };
}
