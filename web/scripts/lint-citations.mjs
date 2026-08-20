// Citation lint: reports how well problem bodies carry `[Sn]` ledger markers.
//
// WARNING-ONLY, NEVER A GATE. This script exits 0 in every circumstance,
// including on its own internal errors. The real build gate is the zod
// validation in web/lib/data.ts; this pass only informs. Every line it prints
// is prefixed `citations: ` so it stays greppable in build output.
//
// A marker is `[S3]`, `[S3,S5]` or `[S3, S5]` written in the prose (uppercase
// S only). The Nth entry of the record's `sources:` list renders as ledger row
// `S<N>`, so a marker resolves iff 1 <= n <= sources.length.
//
// LP_DATA_ROOT overrides the problems root (the directory holding the region
// dirs) — used to point the lint at a fixture corpus without editing this file.
import { readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";

// One console line per call, always prefixed. A thrown message can carry
// newlines — js-yaml quotes the offending snippet back at you — and an
// unprefixed continuation line would leak into build output ungreppable.
const say = (s) =>
  console.log(`citations: ${String(s).replace(/\s*[\r\n]+\s*/g, " ").slice(0, 400).trim()}`);
const pad = (n) => String(n).padStart(2, "0");

try {
  // Loaded dynamically on purpose: a static top-level import that fails to
  // resolve (js-yaml absent from a half-installed node_modules) throws BEFORE
  // this try and exits non-zero — turning the lint into the build gate it must
  // never be. In here, that failure is just another warning line.
  const { load } = await import("js-yaml");

  const root = process.env.LP_DATA_ROOT
    ? resolve(process.env.LP_DATA_ROOT)
    : resolve(import.meta.dirname, "../../data/problems");

  // ---- grammar ------------------------------------------------------------

  // `[` S digits (`,` optional-S digits)* `]`, but a `]` followed by `(` is a
  // markdown link target, not a citation.
  const MARKER = /\[S\d+(?:\s*,\s*S?\d+)*\](?!\()/g;
  const numbersIn = (marker) =>
    marker
      .slice(1, -1)
      .split(",")
      .map((t) => Number(t.trim().replace(/^S/, "")));

  // Numeric noise. Digits surviving these are treated as a claim.
  // Chars that, glued to an integer, make it a measurement rather than a score.
  const GLUE = /[\w%$€£\-–—+/×~]/;
  // `.` and `,` glue only between digits (1,100 / 1.5M); as sentence
  // punctuation they leave the integer bare ("demand 2, gap 2").
  const glued = (s, i, step) => {
    const c = s[i];
    if (c === undefined) return false;
    if (c === "." || c === ",") return /\d/.test(s[i + step] ?? "");
    return GLUE.test(c);
  };
  const UNIT =
    /^(?:%|percent|days?|weeks?|months?|years?|hours?|minutes?|mins?|dn[íůi]|t[ýy]dn\w*|m[ěe]s[íi]c\w*|let|rok\w*|firms?|companies|people|persons?|employees|staff|customers?|users?|clients?|municipalities|obc[íe]|respondents?|contracts?|cases?|tenders?|million|billion|thousand|mil|mld|tis|bn|czk|eur|usd|mw|gwh?|kwh?|ks)$/iu;
  const isYear = (s) => /^(?:19|20)\d{2}$/.test(s);

  const stripNoise = (text) =>
    text
      .replace(MARKER, " ") // the citation markers themselves
      .replace(/^\s*\d+\.\s+/gm, " ") // "1. " ordered-list markers
      .replace(/\b\d{4}-\d{2}-\d{2}\b/g, " ") // ISO dates
      .replace(/\bp-\d{4}\b/gi, " ") // problem ids
      // law/regulation citations — 424/2023, 2023/1115
      .replace(/\b\d{1,5}\/\d{1,5}\b/g, (m) => (m.split("/").some(isYear) ? " " : m))
      .replace(/\bS\d+\b/g, " ") // bare S-tokens
      .replace(/(?<![\d$€£])(?:19|20)\d{2}(?![\d%])/g, " ") // standalone years
      // bare score integers 0-12 with nothing glued to them and no unit after
      .replace(/\d{1,2}/g, (m, i, s) => {
        if (glued(s, i - 1, -1) || glued(s, i + m.length, +1)) return m;
        if (Number(m) > 12) return m;
        const next = s.slice(i + m.length).match(/^\s+([\p{L}%]+)/u);
        return next && UNIT.test(next[1]) ? m : " ";
      });

  const hasNumericClaim = (block) => /\d/.test(stripNoise(block));

  // ---- corpus -------------------------------------------------------------

  let records = 0;
  let totalMarkers = 0;
  let totalUncited = 0;
  let unresolvableMarkers = 0;
  let recordsWithUnresolvable = 0;

  const regions = readdirSync(root, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .sort();

  for (const region of regions) {
    for (const file of readdirSync(join(root, region)).sort()) {
      if (!file.endsWith(".md")) continue;
      const label = `${region}/${file.replace(/\.md$/, "").replace(/^(p-\d+).*$/, "$1")}`;
      try {
        const raw = readFileSync(join(root, region, file), "utf8");
        if (!raw.startsWith("---\n")) throw new Error("missing frontmatter");
        const end = raw.indexOf("\n---\n", 4);
        if (end === -1) throw new Error("unterminated frontmatter");
        const fm = load(raw.slice(4, end)) ?? {};
        const body = raw.slice(end + 5).trim(); // markers live in the body only
        const sourceCount = Array.isArray(fm.sources) ? fm.sources.length : 0;

        // 1 + 2. resolve markers
        const found = body.match(MARKER) ?? [];
        const numbers = found.flatMap(numbersIn);
        const unresolvable = [...new Set(numbers.filter((n) => n < 1 || n > sourceCount))].sort(
          (a, b) => a - b,
        );

        // 3 + 4. paragraph coverage and uncited numeric claims
        const blocks = body.split(/\n{2,}/).filter((b) => {
          const lines = b.split("\n").map((l) => l.trim()).filter(Boolean);
          if (!lines.length) return false;
          if (lines.every((l) => l === "---")) return false; // correction separator
          if (lines.length === 1 && /^#{1,6}\s/.test(lines[0])) return false; // heading
          return true;
        });
        let cited = 0;
        let uncitedNumeric = 0;
        for (const b of blocks) {
          MARKER.lastIndex = 0;
          if (MARKER.test(b)) cited++;
          else if (hasNumericClaim(b)) uncitedNumeric++;
        }

        // 5. per-record line
        say(
          `${label}  markers ${pad(numbers.length)}  paras ${pad(cited)}/${pad(blocks.length)} cited  ` +
            `uncited-numeric ${pad(uncitedNumeric)}`,
        );
        for (const n of unresolvable) {
          say(
            `WARN ${label} — marker [S${n}] does not resolve (${sourceCount} source${sourceCount === 1 ? "" : "s"} on file)`,
          );
        }

        records++;
        totalMarkers += numbers.length;
        totalUncited += uncitedNumeric;
        unresolvableMarkers += unresolvable.length;
        if (unresolvable.length) recordsWithUnresolvable++;
      } catch (e) {
        say(`WARN ${label} — skipped, unreadable (${e?.message ?? e})`);
      }
    }
  }

  // 6. register-wide summary — printed LAST, so the one line a reader or a
  // downstream grep looks for is the one that ends the block.
  if (unresolvableMarkers) {
    say(
      `${unresolvableMarkers} unresolvable marker${unresolvableMarkers === 1 ? "" : "s"} across ` +
        `${recordsWithUnresolvable} record${recordsWithUnresolvable === 1 ? "" : "s"}`,
    );
  }
  say(
    `${totalMarkers} markers across ${records} records; ` +
      `${totalUncited} paragraphs with numeric claims and no citation`,
  );
} catch (e) {
  say(`lint error — ${e?.message ?? e}`);
}

// HARD LAW: this lint never gates the build.
process.exitCode = 0;
