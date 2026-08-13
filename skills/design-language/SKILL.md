---
name: design-language
description: Binding design system for the localproblems.org website. Use whenever generating, editing, or reviewing ANY page, layout, CSS, or HTML for the problems repository site — index pages, problem record pages, category pages, newsletter web versions. Enforces the gazette × land-registry × issue-tracker aesthetic and prevents generic AI design. The weekly pipeline task MUST follow this skill and may never modify assets/style.css or invent new visual elements.
---

# The localproblems.org design language

You are rendering a **state gazette that a very good contemporary designer redesigned in 2026** — official, dense, trustworthy, quietly witty. You are NOT designing a SaaS product, a startup landing page, or a blog.

## Why this file exists

LLMs converge on generic design. The first generation of AI slop was purple gradients, Inter, icon cards, emoji bullets. The second generation — documented by Anthropic's own frontend-design skill — is *fake editorial*: cream paper + high-contrast serif + terracotta accent, or broadsheet layouts with hairline rules used as decoration. **This site is genuinely gazette-derived, which puts it one step from generic-broadsheet slop. The difference is specificity.** Every visual device here encodes something true about the content: rules mark document boundaries, stamps mark lifecycle events, zero-padding marks registry entries, dot leaders join a label to its recorded value. If you add a device that encodes nothing, you have produced slop. Remove it.

The design is fully decided. Your job is to APPLY it, never to reinterpret it. When in doubt between plain and fancy, choose plain. When in doubt between stating a number and describing it, state the number.

## The two voices (the fundamental rule)

**If a human wrote it, it is serif. If a clerk recorded it, it is mono.** No third case.

- **Source Serif 4** (400/600/700): problem titles, body prose, section headings, masthead.
- **IBM Plex Mono** (400/500/600): IDs, dates, sums, scores, deadlines, table cells, labels, buttons, nav, breadcrumbs, footer — anything that could appear in a ledger.
- Both loaded from Google Fonts with `latin-ext` (Czech diacritics ř ě š č ů verified).
- Never any other font family. Not system-ui. Not Inter, Roboto, Space Grotesk, Geist, Instrument Serif.

## The seven colors (there is no eighth)

```
--paper:     #F8F6F1   page background (the only background)
--paper-2:   #EFECE5   row hover, thead, panels
--ink:       #1A1814   text, strong rules
--ink-muted: #6E6A5F   secondary text, timestamps
--rule:      #CBC6B9   hairlines, dotted leaders
--stamp:     #BB271A   úřední razítko red — stamps, urgency, scores 10-12. Max ~5% of any viewport.
--signal:    #1A7A3C   status lifecycle ONLY (dot, claim affordance, VYŘEŠENO)
```

**No dark mode.** A gazette is printed on paper; the paper is the brand. `color-scheme: light only`. The site must photocopy beautifully — there is a `@media print` block and it matters.

## Data formatting (data always looks like evidence)

- Money: mono, Czech convention, `1 250 000 Kč`; ranges `3–8 mil. Kč`. Never `1.25M`.
- Dates in data positions: ISO `2026-08-13` in `<time>`. Czech long dates only inside serif prose.
- Deadlines: `do 2026-09-30 · T−48`; when T < 14, class `.urgent` (stamp red).
- IDs: `{CITY3}-{NNN}` zero-padded: `BRN-041`. Scores `09/12`. Issue `č. 33`. **Zero-padding is the house tic** — everything countable is padded.
- Scores render as the **12-tick tally** (survey chain marks) + zero-padded fraction. Never progress bars, gauges, stars, or rings.

## Page anatomy

- **Masthead on every page**: 4px ink bar, then `localproblems.org` (serif 700) with `ročník {YYYY} · č. {ISO-week}` (mono) right-aligned, then 1px rule. The weekly build IS a publication issue — the automation is the brand.
- **Index = a register table**, not cards: 7 columns max (dot / ID / title / category / locality / score right-aligned / updated right-aligned). Title is the ONLY serif cell. ~20–24 rows per viewport. Pre-sorted by score desc at build time; caption states the sort and extract date. **Zero JavaScript** — filtering is pre-generated category pages.
- **Problem page**: docket header (3px double rule, ID + status dot + tally, serif title, 3-column facts grid) → Shrnutí (serif prose, max 62ch) → Rozklad skóre (signals table with 2px-rule total row) → **Doklady** (numbered exhibit chips "Doklad A/B/C…" in 1px ink boxes, dotted leader from source to date, quote in serif italic) → Vyřešeno jinde (dot-leader lines) → claim block (1px ink border, 4px green left edge, `PŘEVZÍT PROBLÉM →` button that inverts on hover) → footer with record provenance.

## The five signature moves (the only permitted flourishes)

1. **The razítko**: mono 600 uppercase, 2px border, `rotate(-2deg)`, `mix-blend-mode: multiply`. Overlay variant (`rotate(-8deg)`, centered) ONLY for PŘEVZATO / VYŘEŠENO / UZAVŘENO. Max one overlay per page.
2. **Cadastral rules**: exactly three meanings — 4px solid = page begins; 3px double = major boundary; 1px solid = row hairline. No other border weights (2px reserved for buttons/stamps).
3. **Gazette numbering**: `ročník 2026 · č. 33` in masthead, echoed in breadcrumbs.
4. **The status dot**: the ONLY circle and ONLY icon on the site. Hollow green = open, filled = claimed, filled + outline ring = solved, hollow grey = closed.
5. **Dot leaders**: any label→value or source→date pair joined by 1px dotted leader, like a form.

## Spacing and rhythm (v1.1)

- **One 4px scale**: `--sp-1…--sp-8` = 4 / 8 / 16 / 24 / 32 / 48 / 64px (with 12px as `--sp-3`). Every margin, padding, and gap is a step on this scale — no ad-hoc values. Sole exceptions: optical micro-padding inside the stamp and exhibit chip, and the 7.5rem receipts indent column.
- **Sections breathe from above**: `h2` carries 48px above, 16px below — roughly 3:1. Air binds a heading to what follows, not to what precedes.
- **The docket is the title block**: it gets the most air on the site — 24px above the ID, 24px around the title, 48px clearance before the prose begins.
- **Ledger density**: register and signals rows sit at 8px vertical padding; 12px cell gutters; 24px page gutter; 32px facts-grid column gap. Dense is fine, squeezed is not.

## The anti-slop rulebook (hard NEVERs)

1. NEVER any font beyond Source Serif 4 + IBM Plex Mono.
2. NEVER center text (numeric columns right-align; dot cell centers; nothing else).
3. NEVER `box-shadow` or blur — elevation does not exist on paper.
4. NEVER `border-radius` except the status dot. Corners are square. Zero, not 2px.
5. NEVER gradients as color (sole exception: the hard-stop tick pattern inside `.tally`).
6. NEVER icons, emoji, or SVG decoration. Text `→` and `·` are permitted.
7. NEVER a color outside the seven tokens. No hover tints, no rgba improvisation.
8. NEVER animate. No transitions. Hover changes are instant.
9. NEVER set a figure, date, ID, or sum in serif.
10. NEVER progress bars, gauges, star ratings, percentage rings.
11. NEVER marketing adjectives in chrome ("amazing", "🔥"). No doklad, no claim.
12. NEVER more than one overlay stamp per page; never spend stamp red on >5% of a viewport.
13. NEVER JavaScript. Sorting/filtering are build-time concerns.
14. NEVER more than 7 index columns; titles truncate with ellipsis, never wrap.
15. NEVER cards or section backgrounds beyond `--paper-2`. There are no cards; there are ruled records.
16. NEVER modify `assets/style.css` during a content run. Invent no classes, colors, or sizes — if a needed class doesn't exist, flag it in the run summary instead of improvising.

## Copy for UI chrome (exact strings)

| Slot | CZ | EN |
|---|---|---|
| Claim button | `PŘEVZÍT PROBLÉM →` | `CLAIM THIS PROBLEM →` |
| Open record | `Tento záznam je volný. Nikdo na problému nepracuje. Doklady výše.` | `This record is unclaimed. Nobody is working on it. Receipts above.` |
| Claimed stamp | `PŘEVZATO · 2026-08-02 · @handle` | `CLAIMED · 2026-08-02 · @handle` |
| Empty category | `V této kategorii není evidován žádný otevřený problém. Stav k {date}.` | `No open problems on record in this category. As of {date}.` |
| Table caption | `Řazení: skóre sestupně · výpis pořízen {date}` | `Sorted by score, descending · extract generated {date}` |
| Corrections | `Nesouhlasí doklad? Opravy →` | `Receipt wrong? Corrections →` |
| Footer | `Údaje bez záruky. Doklady s odkazy. Výpis č. {NN}/{YYYY}, pořízen automaticky.` | `Data as recorded, no warranty. Receipts with links. Extract no. {NN}/{YYYY}, generated automatically.` |
| 404 | `Záznam nenalezen. Buď nikdy neexistoval, nebo byl vyřešen tak důkladně, že zmizel.` | `Record not found. Either it never existed, or it was solved so thoroughly it disappeared.` |

Buttons: uppercase mono, verb-first, one verb. Never an exclamation mark in chrome. "Problém" is never softened to "výzva".

## Implementation

The complete reference stylesheet is in `assets/style.css` (part of this skill). It implements every token and component above and is the ONLY stylesheet the site uses. Copy it into the repo once; content runs never touch it.

Weekly build rules: compute `č. NN` as zero-padded ISO week; compute `T−n` from deadlines; sort index by score desc then updated desc; set tally fill via inline `style="--s:9"`; verify every page against the NEVER list before committing.

## Quality gate (optional but recommended)

After generating HTML, run `npx impeccable detect` (59 deterministic anti-slop rules, no API key) and treat any finding as a build failure to fix before commit.
