You are the deep-sweep pass for the localproblems repo at
~/Documents/CODE/localproblems. Input: ONE topic, named by whoever launched
you (e.g. "elderly-care capacity"). Output: evidence records about that
topic across ALL FOUR agent streams, in the existing ledgers, at the same
evidence bar as a monthly harvest. Work autonomously; do not ask questions.
If a step fails, note it in data/raw/<today>/manifest.md and continue with
what you have.
Read SPEC.md and data/CONVENTIONS.md before step 1. You do not need
SCORING.md — nothing in this pass touches a problem or a problem score.

WHY THIS FILE EXISTS. On 2026-08-24 a major elderly-care capacity problem
reached the register by founder anecdote, not through the pipeline. The
post-mortem was not that the scans missed it — it is that they could not
have caught it: the monthly passes sweep BROADLY across categories, a
shallow pass over everything, and no mechanism existed to go DEEP on one
topic on demand. There is value in arbitrage looking across categories;
there is separate value in exhausting one topic without aggregating it away.
A sweep is the second thing. Same sources, same ledgers, same bar — pointed
at one topic until the topic, not the calendar, is done.

A SWEEP IS A MODE OF THE SCAN FEEDS, NOT A NEW FEED. It mints records
through the four already-registered agent scan sources and ONLY through
them, into the ledgers they already write:

  arb-scan     -> funded      comps abroad; id prefix = ISO2 of origin
                              (de-, gb-, dk-, ...)
  demand-scan  -> demand      prefix = the reporting body (ombud-, civic-,
                              chamber-, ngo-, consult-, uni-, ...)
  reg-scan     -> regulation  reg-
  dotace-scan  -> tenders     dotace- (source value: dotace)

No new id namespace, no new evidence type, no new ledger, no new feeds.json
row, no schema change. A sweep record is indistinguishable on the ledger
from a monthly-harvest record, and that is the point: PROCESS.md consumes
it with zero new machinery. All four sources are runner: attended, so a
sweep is ATTENDED by definition — a Claude session executing this file.
There is no unattended sweep and none is planned.

WHEN TO LAUNCH — on demand, never on a schedule:
  - the founder names a topic;
  - a problem candidate arrives from OUTSIDE the pipeline (the elderly-care
    case: the anecdote is the trigger, the sweep is what turns it into
    receipts or into a documented dead end);
  - a monthly pass or the register shows a cluster worth exhausting;
  - MATCH holds a single-stream candidate and wants the other streams
    checked before creating a problem (a tier-3-grade signal alone never
    creates one — SPEC §4).
A sweep supplements the monthly broad passes. It never replaces them, never
counts toward their cadence, and a topic having been swept is never a
reason to skip it in the next broad pass.

1. FRAME. mkdir -p data/raw/<today>. Open data/raw/<today>/manifest.md and
   write the sweep header: the topic as given, the date, and the
   decomposition — who is the buyer, who is the user, who regulates it,
   where does the money sit. Then the search vocabulary you will actually
   use, IN BOTH LANGUAGES. Czech is not optional: half of all absence
   claims re-checked on 2026-08-20 were false, and the recurring cause was
   English-only search (CONVENTIONS.md, "Proving a negative"). The manifest
   is the sweep's run record and the one file under data/raw/ that is
   committed; write it as you go, not at the end.

2. MINE THE CORPUS FIRST. Before any web search, grep the committed ledgers
   for the topic vocabulary:
     grep -il 'pattern' data/signals/*/*.jsonl        # then read the hits
   and grep data/problems/<region>/*.md — the register has contradicted its
   own absence claims before (Softlink was a named incumbent on p-0026
   while p-0001 asserted the niche empty). What the corpus already holds is
   COVERAGE, not something to re-mint: list the existing signal ids per
   stream in the manifest. This is also where the scripted tenders feeds
   contribute — ted- and hlidac- records about the topic are already
   flowing in daily; a sweep READS them, it never re-fetches them.

3. HARVEST, one stream at a time. Every stream gets a pass and every pass
   gets a manifest entry, including the empty ones — an evidence stream
   with nothing to say about the topic is a finding, stated with the
   searches that were run, not a row silently missing.

   3a. FUNDED via arb-scan — the arbitrage leg. Companies running a proven
       model for this topic abroad: who funded them, since when, what
       traction is public. One record per company, id <iso2>-<slug> from
       the ORIGIN country, source arb-scan, evidence_type funded. Each
       carries a CZ ABSENCE CHECK in notes — see the evidence bar in
       step 4; an arb record without one is a comp, not an arbitrage
       signal.
       ID PREFIX LAW: the prefix must be claimed by arb-scan's
       id_prefixes in data/feeds.json. A comp from a country not yet
       listed there (US is currently NOT listed) means widening that
       array IN THE SAME CHANGE that stages the record — registry before
       record, the same order CONVENTIONS.md demands for the source enum.
       NEVER mint a prefix another registry row claims: two capable
       claimants send every record in the prefix to UNATTRIBUTED
       (db.py AC-F3 — see the coi and sukl blockers in feeds.json for the
       precedent).
   3b. TENDERS via dotace-scan — the top-down money leg. Open grant and
       subsidy calls funding work on the topic: allocation, deadline,
       administering programme. Id dotace-<slug>, source dotace,
       evidence_type tenders. Public CONTRACTS on the topic are the
       scripted feeds' job and were mined in step 2 — THE SCRIPTED-PREFIX
       PROHIBITION: a sweep never hand-mints ted-, hlidac-, nen- or
       smlouvy- records. `source` is fetch provenance, and a hand-written
       record wearing a fetcher's name is a false receipt (CONVENTIONS.md
       on smlouvy vs hlidac). If the ledger plainly misses contracts you
       can see on the registers — the baked-in query lists don't cover the
       topic — record that as a COVERAGE GAP in the manifest, naming the
       queries the fetcher would need. Widening a fetcher is owner work,
       not sweep work.
   3c. DEMAND via demand-scan — the bottom-up leg. Ombudsman reports, NKÚ
       findings, civic complaint data, chamber/NGO surveys, consultations,
       state statistics documenting unmet need on the topic. Prefix = the
       reporting body, per the demand-scan id_prefixes list. THE mpsv-
       TRAP: `mpsv-` is claimed by the hiring feed, so a ministry
       yearbook or statistics record must NOT mint it — file state-body
       statistics under civic- (and say so in notes). Pain language rules
       hold: complaints, failures, waiting lists, workarounds; engagement
       metrics never justify a record.
   3d. REGULATION via reg-scan — the deadline leg. Acts, amendments and
       transposition waves touching the topic, each with its DATES:
       adopted, in force, compliance deadline. Id reg-<slug>, source
       reg-scan, evidence_type regulation. A regulation record without a
       date is not a regulation record.

4. EVIDENCE BAR — identical to a monthly harvest. Depth means MORE
   records, never a lower bar; a sweep that lowers the bar to fill its
   streams has manufactured the aggregation problem it exists to avoid.
   Per record: url + native ISO date; title "Thing — what it is"; <=2
   sentence EN summary; sector from the fixed list; geo_origin = where the
   signal comes FROM; money_eur + money_note saying how derived (null when
   nothing is published — never estimate); objective scores per the
   CONVENTIONS.md rubric, region-blind; extraction: manual; a verbatim
   quote <=300 chars where the source text supports one (for agent
   harvests an unverifiable quote degrades to a manifest warning — the
   stated asymmetry, not a loophole).
   ABSENCE CLAIMS ARE THE EXPENSIVE PART AND THE REASON SWEEPS EXIST.
   Every "no CZ player" note states its own coverage: the queries run
   (Czech included), the surfaces checked (use the `checked` vocabulary
   from CONVENTIONS.md), and a POSITIVE CONTROL — the same method run at a
   company known to exist (Wultra, Softlink, Ringil are the register's
   standing controls). A method that cannot find the control has found a
   broken method, not an absence: say so in the manifest and write no
   absence. A negative with no stated searches is a vibe, and vibes do not
   enter an append-only ledger. On a transient error (HTTP 529, overload):
   sleep and retry, never record a skipped check as "not found".

5. STAGE + COMPLETE — never append by hand. Write every harvested record
   as one JSON object per line to data/raw/<today>/staged.jsonl, each
   carrying its full field set plus `evidence_type` (routing only — the
   append-time allowlist strips it from the ledger line). Then:
     python3 scripts/normalize.py --raw data/raw/<today> --complete --dry-run
     python3 scripts/normalize.py --raw data/raw/<today> --complete
   and run the `db.py upsert` lines --complete prints. This is the same
   gate every fetched record passes: the materiality filter, the id-keyed
   dedup against seen.txt, the identity-key dedup against the whole
   corpus, the ISO-date and sector checks, and the AC-GDPR1 allowlist.
   Hand-appending to a ledger skips all five and is forbidden — the
   ledgers are append-only and a wrong append has no quiet cleanup. A
   record --complete refuses stays staged and is listed in the manifest as
   pending; never invent a value to clear a refusal.

6. HAND OFF: STOP. Do not run git add, git commit, git push, the web
   build, or a deploy. Leave the new JSONL lines, seen.txt, manifest and
   any feeds.json prefix widening uncommitted in the working tree;
   pipeline/PROCESS.md commits them alongside whatever problems they
   produce. End by printing a 5-line sweep summary: topic / records staged
   per stream / appended after materiality / absence checks run (with
   controls passed) / coverage gaps recorded.

WHAT A SWEEP DOES NOT DO. No problem files, no SCORING.md scores, no
match, no de-rank, no gap edits — a sweep's absence check is evidence
COLLECTION (what a search found, recorded in notes), and what it MEANS for
any problem's `gap` stays with MATCH under the asymmetric-authority law in
CONVENTIONS.md. No commits, ever (step 6). No new feeds, types, schemas or
scripts; no hand-minted scripted prefixes (3b); no re-running scripted
fetchers to "top up" a stream. No judgment about whether the topic IS a
problem worth solving — a sweep can end with four thin streams and a
manifest that says so, and that null result is a legitimate, useful output.

WORKED EXAMPLE — the elderly-care sweep (the post-mortem case, run as this
file describes it):

  FRAME  topic: elderly-care capacity. Buyer: families, municipalities,
  kraje; user: seniors and family caregivers; regulator: MPSV under zákon
  108/2006 Sb.; money: NPO and kraj subsidy programmes, private pay.
  Vocabulary: "domov pro seniory", "pečovatelská služba", "kapacita
  sociálních služeb", "čekací doba", "dlouhodobá péče"; EN: senior care
  marketplace, care home comparison, care staffing.

  MINE  grep the tenders ledgers for the Czech vocabulary — the ted- and
  hlidac- care contracts already committed are the contract leg, listed by
  id in the manifest; grep data/problems/cz/ for prior claims about care.

  3a  arb-scan: A Place for Mom (US — senior-care referral marketplace),
  Lottie (GB — care-home marketplace and comparison), ShiftKey (US — care
  staffing shift marketplace). Three funded records under their origin
  prefixes — which for the two US comps means adding "us" to arb-scan's
  id_prefixes in the SAME change (3a). Each with traction from public
  sources only, and a CZ absence check in notes: the Czech queries run,
  checked: [google-cz, ares, own-funded-ledger], and the positive control
  the method was proven on.

  3b  dotace-scan: NPO call 31_24_138 (social-services capacity) — one
  dotace- record with the call's published allocation and deadline,
  money_note naming the call page. Contract coverage came from MINE; if
  the fetchers' baked-in queries miss care contracts visible on the
  registers, that is a named coverage gap in the manifest, not a
  hand-minted ted- record.

  3c  demand-scan: the ombudsman's report on care capacity -> ombud-
  record quoting its findings; MPSV yearbook capacity and waiting-list
  statistics -> a civic- record (NOT mpsv- — that prefix belongs to the
  hiring feed), quote carrying the yearbook's own numbers.

  3d  reg-scan: novela 92/2026 — one reg- record with its in-force date
  and what obligation it creates for providers.

  STAGE + COMPLETE, hand off. Result: one topic, four streams, every
  record carrying its receipt, every absence carrying its searches — the
  evidence a founder anecdote should have been able to meet in the
  register instead of preceding it.
