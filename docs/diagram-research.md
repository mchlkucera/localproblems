# Process figure: icon and diagram research (2026-09-18)

This is what we looked at before shipping the hub as `ProcessSteps` (`web/lib/figures/process.tsx`),
with its glyphs in `web/lib/figures/role-icons.tsx`. Mockups were built on a throwaway route and then removed.

## Icon sets

| Set | Style | Covers our roles and objects? | Licence | Build-time use |
|---|---|---|---|---|
| [Phosphor](https://phosphoricons.com) (regular, fill, duotone) | solid in the fill weight | all of them: stethoscope, barcode, folder, headset, truck, bank, briefcase, storefront, file, phone, envelope, database, receipt, table, app window | MIT | inline SVG, per-icon files, tree-shakes |
| [Tabler Icons](https://tabler.io/icons) (outline, filled) | the filled subset is small | patchy: no barcode or database in filled | MIT | inline SVG |
| [Lucide](https://lucide.dev) | outline only | broad | ISC | inline SVG. Banned: an outlined stock set |
| [Material Symbols](https://fonts.google.com/icons) | outline, filled | broad | Apache-2.0 | inline SVG. Generic, reads as Google |
| [Iconoir](https://iconoir.com) | outline only | broad | MIT | Banned: outline |
| [Healthicons](https://healthicons.org) | filled 48px figures | doctor, nurse, call centre, truck driver, officer, phone, register book, spreadsheet, desktop app; **no** coder, documentarian, consultant or e-mail | icons CC0, repo MIT | inline SVG |
| [Open Peeps](https://openpeeps.com) / [Humaaans](https://humaaans.com) | illustrated people | faces and poses only; nothing says "doctor" or "coder" | CC0 | SVG export ([DiceBear](https://dicebear.com) `open-peeps` renders heads) |
| [unDraw](https://undraw.co) | spot illustrations | scenes, not roles | unDraw licence (free, no redistribution as a set) | SVG |
| [Streamline](https://streamlinehq.com) free sets | line and flat | broad | mostly CC BY 4.0 (attribution) | SVG |
| OpenMoji / Noto Emoji | emoji | broad | CC BY-SA 4.0 / Apache-2.0 | Banned: emoji |

**Verdict.** The house rule is §10 rule 9: small glyphs are solid and drawn for this site. We drew our own
glyphs on the category icons' 16-unit grid. The set is 13 role glyphs, 8 object glyphs and a plain-bust
fallback, and it looked at least as clear as Phosphor Fill. Healthicons are strong for clinical roles and
empty everywhere else. Illustrated people were the most charming, but they carry no role and pull the eye
off the data.

## Diagram engines (build-time SVG, no client runtime)

| Engine | Packages | Browser? | Install | Time per diagram | Theming toward the site |
|---|---|---|---|---|---|
| Mermaid 11 (MIT) | `@mermaid-js/mermaid-cli` (puppeteer) | **yes**, headless Chrome | ~480 MB node_modules + ~188 MB Chrome | ~3 s browser start, then 20–50 ms | closest: Inter, grays, teal via `classDef`/`linkStyle`; a single sequence message can't be coloured |
| D2 (MPL-2.0) | `@terrastruct/d2` (wasm) | no | 59 MB | ~1 s (the Inter font passed each call) | exact colours; bold drops to regular with Inter; ELK reads better than dagre; sketch mode is messy |
| Graphviz (EPL; `@hpcc-js/wasm-graphviz` Apache-2.0) | `@hpcc-js/wasm-graphviz` | no | 3 MB | 1–14 ms | worst: its text metrics don't fit Inter, labels spill out of boxes |

Findings:
- At 680px, every engine's text renders smaller than the page's type.
- Icons render in both Mermaid and D2, but badly: Mermaid stacks a tiny icon over the label, and D2 makes icons large.
- The Mermaid **hub** read best of the engine layouts, followed by its sequence diagram.
- Hand-built HTML/CSS won. It uses the page's own type and needs no browser in the build. It also reflows to 375px.

## Role vocabulary

The live records' `process:` blocks name these 12 actors (p-0008, p-0010 and p-0036):

- Doctor, Coder, Documentarian
- Dispatcher, The office, The back office
- A consultant who checks what the law requires
- A consultant who writes grant applications
- A seller of ready-made compliance documents
- The town or care home
- Nobody in-house
- `?` (unknown: never drawn as a person)

The after lines add two more: the driver and the provider.

The record bodies name about 25 more roles, which the same glyphs can cover. They include nurse, pharmacist,
accountant, payroll/HR, installer, engineer, town official, ministry, regulator/inspector, care-home manager,
carer, family, patient, supplier, distributor, bank/lender, insurer, broker and lawyer.

`ROLE_TABLE` maps a `who` to a glyph by keyword, and the first match wins. For example, nurse and physician
share the doctor glyph, adviser and lawyer share the consultant glyph, and any organisation gets the civic
building. Anything unmatched draws the plain bust.

## Adding a role or an object

1. Draw its **one detail** on the 16-unit grid in `role-icons.tsx`: a hole in the chest, or a small badge that
   `badge: true` cuts free of the bust with a ground-coloured stroke. Keep it solid, even-odd, and give the
   detail at least 1px of negative space.
2. Add it to `ROLE_GLYPH` and one keyword row to `ROLE_TABLE`. For an object, add it to `OBJ_GLYPH` and one
   row to `PLACE_TABLE`. The matched text becomes the label, so the figure only ever uses the record's own
   words.
3. Check the glyph at 22px and 20px (phone), both on the gray ground and inside the teal box.
