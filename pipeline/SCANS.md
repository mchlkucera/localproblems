You are the monthly broad-scan pass for the localproblems repo at
~/Documents/CODE/localproblems. This file governs the FOUR attended scan
feeds — demand-scan, reg-scan, dotace-scan, arb-scan — when they run their
monthly BROAD pass. It does not govern deep sweeps: a topic-scoped deep dive
is pipeline/SWEEP.md's job and stays there. Work autonomously; do not ask
questions. If a step fails, note it in data/raw/<today>/manifest.md and
continue with what you have.
Read SPEC.md and data/CONVENTIONS.md before starting. You do not need
SCORING.md — nothing in a scan touches a problem or a problem score.

WHY THIS FILE EXISTS. Post-mortem, 2026-08-24/25: the attended scans missed
in-scope events — not because the sources were unknown, but because NOTHING
FORCED EACH PASS THROUGH EACH SOURCE IN ITS REMIT. A scan was a prompt and a
memory; whichever sources the session happened to open got read, and the rest
were skipped without anything anywhere saying so. A skipped source is
indistinguishable from a quiet source, which is this repo's named failure
shape (the `ok=1 items_kept=0` silence, the fetcher that "works" while zero
records land) wearing an attended harvest's clothes. The fix is the same fix
it always is: make the unmeasured thing a first-class, named output.

THE CHECKLIST LAW. Every scan pass MUST walk EVERY source on its feed's
checklist below. For each source the pass records in the run manifest either
(a) what it found — including "nothing new this pass", stated with what was
checked — or (b) a NAMED COVERAGE GAP: the source, why it was not visited,
and what a future pass owes it. Silence is forbidden: a manifest for a scan
pass that does not mention every checklist source by name is an incomplete
run, not a lean one. The checklist is a floor, never a ceiling — a pass may
always read beyond it, and SWEEP.md sweeps still never count toward it.

Everything else about a scan is unchanged and lives where it always did:
records go through data/raw/<today>/staged.jsonl and
`normalize.py --complete`, at the monthly-harvest evidence bar (SWEEP.md
step 4 states it; it is the same bar), under the id prefixes each feed's
data/feeds.json row claims. A scan NEVER commits (the INGEST hand-off law).

THE CHECKLISTS. Every URL below was re-verified to resolve on 2026-08-25.
A URL that stops resolving is itself a manifest entry, not a silent skip.

demand-scan (evidence_type demand):
  1. NKÚ kontrolní závěry — PARSE THE ZÁVĚR PDFs, NOT JUST RSS HEADLINES.
     The scripted `nku` feed already lands headline records; this pass reads
     the conclusions themselves for the quantified failure and the body
     responsible. Věstník: https://www.nku.cz/cz/publikace-a-dokumenty/vestnik/
     beside the existing RSS (https://nku.cz/cz/rss.xml).
  2. European Semester CZ package — the Country Report (June) and the
     Council CSR (July), one cycle per year. Current cycle:
     https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages-including-country-reports/country-report-czechia_en
     (the older .../country-pages/country-report-czechia_en 301s there).
  3. MPSV Statistická ročenka, chapter 5 "Sociální služby" XLSX — annual,
     lands ~September; until the year's edition exists the manifest entry is
     "not yet published", which is an expected absence, not a gap.
     https://mpsv.gov.cz/statisticka-rocenka-z-oblasti-prace-a-socialnich-veci-archiv
  4. Ombudsman ESO — systematic-visit reports and the quarterly reports.
     NO RSS EXISTS: this is an HTML walk of https://www.ochrance.cz/eso/zpravy/
     and "no feed" is why it is on a mandatory checklist at all.

reg-scan (evidence_type regulation):
  1. Programové prohlášení vlády + its SEMI-ANNUAL fulfilment evaluations —
     each evaluation dates the government's own stated intent.
     https://vlada.gov.cz/cz/vlada/programove-prohlaseni/programove-prohlaseni-vlady-224629/
  2. Plán legislativních prací vlády — annual; what is scheduled to become
     law and when.
     https://vlada.gov.cz/cz/ppov/lrv/dokumenty/plan-legislativnich-praci-vlady-na-rok-2026-226017/
  3. e-Sbírka and EUR-Lex, exactly as already practiced (the feed's
     feeds.json row names them).
  4. VeKLEP RIA problem definitions — the ITEM-LEVEL WATCH IS NOW THE
     SCRIPTED `veklep` FEED (registered 2026-08-25, scripts/fetch_veklep.sh):
     the script surfaces every new/updated draft as a regulation signal, and
     THIS PASS READS THE RIA "Definice problému" SECTIONS for the items the
     feed surfaced. The scan never re-fetches what the script fetched; it
     reads the state's own problem statements the metadata points at.

dotace-scan (evidence_type tenders, prefix dotace-):
  1. MS2021+ open-data call list — nightly XML; the pass DIFFS IT for calls
     newly opened since the last pass (keep the previous pass's snapshot or
     its call-id list in the manifest so the diff has a left-hand side).
     https://ms21opendata.mssf.cz/SeznamVyzev_21_27.xml
  2. The existing portals the feed's feeds.json row already names (IROP,
     OPZP, OPJAK, SFZP, TACR, NPO, CINEA/HaDEA) — unchanged, and each one
     visited is each one named in the manifest.

arb-scan (evidence_type funded):
  THE CATEGORY-ROTATION DUTY. The register's category list is the complete
  taxonomy in data/CONVENTIONS.md — fintech, health, housing, energy,
  mobility, govtech, retail-services, b2b, legal-compliance, education,
  environment, other (12) — and over N monthly passes the scan MUST cover
  every one of them: no sector goes unswept indefinitely because no pass was
  ever forced to look at it. Each pass records in the manifest which
  categories it covered THIS pass and the rotation state (per category, the
  date it was last swept); the next pass starts from the longest-unswept.
  Depth per category stays the pass's judgment; going deep on one topic
  remains SWEEP.md's job, and a sweep never advances the rotation.

HAND OFF: exactly as INGEST.md and SWEEP.md — stage, `--complete`, run the
printed `db.py upsert` lines, STOP. No commits, ever. End by printing a
5-line pass summary: feed / checklist sources visited vs total / records
staged / coverage gaps named / rotation state (arb-scan only).
