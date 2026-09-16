// Build gate: each locked stylesheet must be a verbatim copy of its
// design-language skill asset. The skill is the single design source (SPEC §5).
//
//   1. MODERN TOKENS (the public site): web/app/(site)/styles/tokens.css ==
//      skills/design-language/assets/tokens.css. Only the tokens are locked —
//      the gray ramp, type scale, grid, radius and shadow every page builds on.
//      The per-page sheets (front, problem, signals, …) are not: their rules
//      live in the skill and web/app/(site)/DESIGN.md.
//   2. GAZETTE (the private /sources admin page only): web/shared.css ==
//      skills/design-language/assets/style.css, for as long as a route under
//      app/(gazette) loads it. Delete this clause with the last gazette route.
import { createHash } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";

const sha = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");
const web = (p) => resolve(import.meta.dirname, "..", p);
const repo = (p) => resolve(import.meta.dirname, "../..", p);

const LOCKS = [
  { app: web("app/(site)/styles/tokens.css"), skill: repo("skills/design-language/assets/tokens.css") },
  { app: web("shared.css"), skill: repo("skills/design-language/assets/style.css") },
];

let failed = false;
for (const { app, skill } of LOCKS) {
  const a = app.slice(resolve(import.meta.dirname, "../..").length + 1);
  const s = skill.slice(resolve(import.meta.dirname, "../..").length + 1);
  if (!existsSync(app) || !existsSync(skill) || sha(app) !== sha(skill)) {
    console.error(
      `check-css: ${a} != ${s}\n` +
      "The skill asset is the single design source. Edit the skill asset, then re-copy it:\n" +
      `  cp '${s}' '${a}'`
    );
    failed = true;
  } else console.log(`check-css: ${a} matches ${s}`);
}
if (failed) process.exit(1);
