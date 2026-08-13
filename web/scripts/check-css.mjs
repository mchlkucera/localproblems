// Build gate: web/shared.css must be a verbatim copy of the design-language
// skill stylesheet. The skill is the single design source (SPEC.md §5).
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";

const sha = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");

const app = resolve(import.meta.dirname, "../shared.css");
const skill = resolve(import.meta.dirname, "../../skills/design-language/assets/style.css");

if (sha(app) !== sha(skill)) {
  console.error(
    "shared.css drift: web/shared.css != skills/design-language/assets/style.css\n" +
    "The skill stylesheet is the single design source. Re-copy it:\n" +
    "  cp skills/design-language/assets/style.css web/shared.css"
  );
  process.exit(1);
}
console.log("check-css: shared.css matches the design-language stylesheet");
