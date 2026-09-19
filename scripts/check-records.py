#!/usr/bin/env python3
"""
scripts/check-records.py — enforce data/RECORD-TEMPLATE.md.

WHY THIS EXISTS. The site is a template: `web/lib/sections.ts` splits a record's
body on LITERAL lead-ins (`Why now:`, `Who pays:`, …) and the page renders those
slices. A record that misspells a lead-in still builds — the paragraph just
falls silently into the previous section and the page renders wrong. There is no
error anywhere. That silence is the whole reason for this file.

TWO MODES, AND THE DEFAULT IS STILL THE REPORT. Bare, it exits 0 and prints
everything, because most findings are editorial (word counts, marker density)
and a content pass should see them without being blocked. `--strict` exits 1 on
any ERROR, and since 2026-08-25 `--strict` RUNS INSIDE `npm run build`
(web/package.json `prebuild`). That is the change the established-test round was
for: SPEC.md and SCORING.md have forbidden the contradictions below all along,
and until now nothing enforced them, so they shipped twice and were caught by a
reader both times.

    python3 scripts/check-records.py            # report
    python3 scripts/check-records.py --strict   # exit 1 on ERRORs — the build gate
    python3 scripts/check-records.py --body-v2  # list every body-v2 finding (BODY_V2_ENFORCED)
    python3 scripts/check-records.py --strict --enforce p-0036   # a rewrite, checked as enforced
    python3 scripts/check-records.py --scoring-v2   # list every scoring-v2 finding (SCORING_V2_ENFORCED)
    python3 scripts/check-records.py --strict --enforce-scoring p-0008   # a rescore, checked as enforced
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORDS = os.path.join(ROOT, "data", "problems", "cz", "p-*.md")
PARTIES = os.path.join(ROOT, "data", "lookup", "cz-contract-parties.jsonl")

# ---------------------------------------------------------------------------
# PyYAML, or an interpreter that has it. Verbatim in intent from scripts/db.py:
# on this host `python3` resolves to the ONE interpreter without the dependency,
# and the fix is a host-level `pip install pyyaml`, not a worse parser here.
#
# THE FRONTMATTER IS PARSED, NOT PATTERN-MATCHED, and that is a deliberate
# upgrade over this file's first version. The cross-field invariants below read
# INSIDE list items — `comps[i].traction`, `locals[i].competes`,
# `sources[i].queries` — and the corpus writes multi-line folded scalars, so a
# regex would have to re-implement block-sequence grouping to find them. A
# BUILD GATE that mis-groups a record is worse than no gate: it fails an honest
# record, or passes a contradictory one, and either teaches everyone to add
# `|| true`. `prebuild` already requires PyYAML (db-gate.mjs runs db.py
# rebuild), so this adds no dependency the build did not already have.
_REEXEC_GUARD = "LP_CHECK_YAML_REEXEC"
_YAML_CANDIDATES = (
    "/usr/local/bin/python3", "/opt/homebrew/bin/python3.12",
    "/opt/homebrew/bin/python3.11", "/usr/bin/python3",
    "python3.13", "python3.12", "python3.11",
)


def ensure_yaml(argv):
    """Guarantee the running interpreter has PyYAML, re-execing ONCE if not."""
    try:
        import yaml  # noqa: F401,PLC0415
        return
    except ImportError:
        pass
    if os.environ.get(_REEXEC_GUARD):
        raise SystemExit(
            f"check-records: re-exec under {os.environ[_REEXEC_GUARD]} still has no "
            f"PyYAML. Install it: {sys.executable} -m pip install pyyaml")
    me = os.path.realpath(sys.executable)
    for cand in _YAML_CANDIDATES:
        exe = cand if os.path.isabs(cand) else shutil.which(cand)
        if not exe or not os.path.isfile(exe) or os.path.realpath(exe) == me:
            continue
        try:
            probe = subprocess.run([exe, "-c", "import yaml"], capture_output=True, timeout=30)
        except Exception:  # noqa: BLE001 — an unusable candidate is just skipped
            continue
        if probe.returncode != 0:
            continue
        print(f"check-records: {sys.executable} has no PyYAML — re-execing under {exe} "
              f"(install pyyaml for the default python3 to retire this shim)",
              file=sys.stderr)
        env = dict(os.environ)
        env[_REEXEC_GUARD] = exe
        os.execve(exe, [exe, os.path.abspath(__file__)] + list(argv), env)
    raise SystemExit(
        "check-records: PyYAML is required to read data/problems/**/*.md and no "
        "interpreter on this host has it. Install it: python3 -m pip install pyyaml")

# The literal lead-ins sections.ts keys on. Keep in sync with web/lib/sections.ts.
LEAD_INS = ["Why now:", "Who pays:", "Existing non-solutions", "Solved elsewhere:"]

# Prose that is about OUR PROCESS, not about the problem. Banned from rendered
# body text; belongs in `## Revisions`, which the page does not render.
# Phrases that are process jargon in any casing.
JARGON = [
    "de-rank", "gap-check", "gap check", "absence check", "incumbent re-check",
    "re-judgment", "the audit found", "receipted", "materiality",
]

# The retired scorecard verdict labels. Matched CASE-SENSITIVELY and as whole
# words, because the lower-case forms are ordinary English the register is
# entitled to use: "a later market search confirmed it" and "a validated US
# cluster" are not jargon, and flagging them taught readers to ignore the
# checker — which is how a warning stops being a warning.
VERDICTS = ["UNPROVEN", "FAINT", "SCATTERED", "LIKELY", "CONFIRMED", "VALIDATED",
            "STRONG", "PRIME", "THIN", "UNFUNDED", "MILD", "FORCING"]

# THE GLOSS LAW (CONVENTIONS.md, "Body shape and length"): the FIRST use of an
# ALL-CAPS trade term in rendered body prose carries a plain-language appositive
# — an em-dash or parenthetical gloss in the same sentence ("NZÚ — the state
# renovation subsidy"). This check enforces it, WARNING-ONLY by design: the
# corpus predates the law, so the warnings ARE the retrofit worklist and must
# never turn 33 unretrofitted records red. The allowlist names what a builder
# is assumed to know and needs no gloss; [Sn] citation markers are stripped
# before the scan, so a marker's S never reads as a term.
GLOSS_ALLOWLIST = frozenset((
    "EU", "US", "CZ", "IT", "AI", "VAT", "CZK", "EUR", "USD", "GBP", "ISO",
    "SAAS", "YC", "HW", "SW", "API", "PDF", "XLSX", "GDPR", "ICO", "IČO",
))
# A WHOLE word of 2–6 letters (Unicode — IČO and SÚKL are ALL-CAPS too); the
# \b anchors matter: without them an 8-letter caps name is chopped into 6+2
# fragments and flagged twice. Digits and underscores excluded so "B2B" and an
# id fragment never match.
_GLOSS_TOKEN = re.compile(r"\b[^\W\d_]{2,6}\b", re.UNICODE)


def ungloss_terms(prose):
    """ALL-CAPS trade terms whose FIRST use is not glossed in its own sentence."""
    text = re.sub(r"\[S[\d,S]+\]", "", prose)      # citation markers are not prose
    text = re.sub(r"\]\([^)]*\)", "]", text)       # markdown link targets are not prose
    seen, flagged = set(), []
    for sent in re.split(r"(?<=[.!?])\s+", text):
        for m in _GLOSS_TOKEN.finditer(sent):
            tok = m.group(0)
            if not tok.isupper() or tok.upper() in GLOSS_ALLOWLIST or tok in seen:
                continue
            seen.add(tok)                          # first use decides; later uses ride on it
            if "—" not in sent[m.end():] and "(" not in sent[m.end():]:
                flagged.append(tok)
    return flagged


# The register talking about ITSELF. A builder does not care what "this record
# originally judged" or what "would move this record" — that is our bookkeeping
# leaking onto a public page, the same class of tell as the retired verdict
# labels. Facts about the world stay; facts about our filing go to Revisions.
SELF_REF = [
    "this record", "the record's", "in the register because", "this ledger",
    "urgency and rank", "should jump", "would move this", "Honest limits",
]

# A REPO PATH ON A PUBLIC PAGE. `locals[].evidence` and `comps[].traction` are
# RENDERED — they are the note line under every ledger entry — but they are
# frontmatter, so the prose-hygiene pass above, which reads the body only, has
# never looked at them. It shows: live records print sentences like "there is no
# pairing in data/lookup/cz-contract-parties.jsonl" to a builder who has no idea
# what that file is and no way to open it. A filename is the purest form of the
# artifact class the owner keeps striking out — page furniture that exists
# because of how we work. Advisory, and deliberately narrow: only paths and
# repo filenames, never phrasing, because a checker that floods is a checker
# nobody reads.
LEDGER_PATHS = re.compile(
    r"(?i)\b(?:data|scripts|web|skills|pipeline|docs)/[\w./-]+"
    r"|\b[\w-]+\.(?:jsonl|json|md|py|ts|tsx|mjs|db)\b")

# Argument prose only (excludes First moves / Revisions). Calibrated to flag
# genuine bloat rather than the house norm: the owner-approved exemplar p-0010
# runs 529 words, so a 300 target would fail the standard it is meant to enforce
# and produce twenty warnings nobody reads. 450 catches the outliers.
ARG_WORDS_MAX = 450
MARKERS_PER_SENTENCE = 3  # more than this reads as citation clot (the p-0008 lesson)


# ===========================================================================
# THE ESTABLISHED TEST (SCORING.md, owner 2026-08-25)
# ===========================================================================
#
#   A player is ESTABLISHED when it has been selling for >= 3 years AND shows
#   at least one of: named customers or a public customer count · >= 2 distinct
#   public buyers in data/lookup/cz-contract-parties.jsonl · funding at Series A
#   or later · a state certification, attest or framework listing.
#   Otherwise it is EARLY.
#
# IT IS A FUNCTION HERE BECAUSE IT HAS TO BE ONE. The test it replaced — "does a
# company exist?" — could not discriminate: half the signal corpus is "a funded
# foreign company exists", so 81% of records were born passing it. Maturity can
# discriminate, but only if something actually evaluates it; a rubric line no
# machine reads is a rubric line that rots quietly while the register keeps
# printing scores derived from it. Every field this reads is already on the
# record: comps[].since/traction and locals[].since/ico/evidence.
#
# THE SAME FUNCTION SCORES BOTH SIDES, WITH THE SIGN FLIPPED — established
# ABROAD raises proof, established LOCALLY drops gap to TAKEN — so there is
# exactly one definition of "established" in the repo and it cannot drift
# between the two dimensions the way the v1 rubric's gap-condition-inside-proof
# did.
#
# IT IS ONLY HALF THE LOCAL ANSWER, AND THAT IS THE 2026-08-25 CORRECTION.
# Maturity says how proven a player is; it does not say WHETHER IT SELLS THIS.
# `locals[].status` conflated the two for one commit and both content agents
# broke on it: a mature Czech firm selling something ADJACENT had no honest
# spelling, so one agent wrote it `early` (a false maturity claim) and the other
# left it out of the ledger (a false absence). `competes: direct | adjacent` now
# carries the eligibility question and `maturity` carries this test, unchanged.
# GAP READS BOTH: `competes` decides whether a row counts at all, `maturity`
# decides which rung it lands on.

MIN_YEARS_SELLING = 3
LOCAL_COMPETES = ("direct", "adjacent")
LOCAL_MATURITIES = ("established", "early")
# Schema 6 spelling. Named so a half-migrated record fails with the instruction
# rather than with "missing competes", which is true but points at the wrong end.
LOCAL_RETIRED_KEYS = ("status",)

# The three text-readable limbs. EACH PATTERN MATCHES TWO THINGS: the limb as
# SCORING.md words it ("named customers", "state certification") and the fact
# pattern a `traction` string writes without naming any limb at all ("380
# installer customers", "certified by Norway's National Archives"). Both are
# citations — the first is an author answering the test, the second is a
# comparables ledger written years before the test existed — and a checker that
# only understood one of them would either fail honest records or force 82 comp
# entries to be rewritten to satisfy a regex.
_LIMBS = (
    ("named customers or a public customer count", re.compile(
        # the limb by name, as SCORING.md states it …
        r"(?i)\bnamed customers?\b|\bpublic customer count\b"
        # … a counted population ("380 German installer customers", "~123k
        # customers", "500+ hospitals", "30 leading Nordic accounting firms") …
        r"|[~>]?\d[\d\s.,]*\s*(?:k|m|bn|mil|tis)?\+?\s*(?:[\w./-]+\s+){0,3}"
        r"(?:customers?|clients?|buyers?|users?|providers?|agencies|firms?|shops?|"
        r"councils?|members?|organi[sz]ations?|hospitals?|banks?|schools?|advisers?|"
        r"households?|patients?|sites?|z[áa]kazn[íi]k\w*|odb[ěe]ratel\w*|obc[íi]|"
        r"[úu][řr]ad\w*|[šs]kol\w*|nemocnic\w*)\b"
        # … or named ones ("clients incl. N26", "trusted by 15+ UK firms").
        r"|\b(?:customers?|clients?|users?|referen[cs]\w*|z[áa]kazn[íi]\w*)\s+"
        r"(?:incl\.|including|such as)|\b(?:trusted by|used by|used in|deployed at)\b")),
    # Funding at Series A or later. The stage LETTER is the whole test: seed and
    # pre-seed are EARLY by definition, and this is the one limb where a looser
    # reading ("raised", "$3.5M") would re-admit the bare existence test that the
    # established test exists to replace.
    ("funding at Series A or later", re.compile(r"(?i)\bseries\s+[a-k]\b")),
    ("a state certification, attest or framework listing", re.compile(
        r"(?i)\b(?:atest\w*|attest\w*|certifi\w*|akredit\w*|notified body|"
        r"state (?:certification|register)|framework (?:agreement|listing)|"
        r"r[áa]mcov\w+ (?:dohod|smlouv)\w*)\b")),
)
# What a locals[] `evidence` string claims about public buyers, so the claim can
# be measured against the lookup rather than believed.
_CLAIMED_BUYERS = re.compile(r"(?i)(\d+)\s*(?:distinct\s+)?(?:public\s+)?"
                             r"(?:buyers?|payers?|odb[ěe]ratel\w*)")

_BUYERS = None


# THE PRICE RECEIPT (owner ruling, 2026-09-03; docs/who-pays-audit-2026-09-03.md).
# MONEY measures proximity to a public budget, and the audit found six of the
# eight rung-1 records writing "adjacent" in their own notes: the number never
# carried the caveat. The fix is a SPLIT, not a re-score — a `type: price`
# source records what a named Czech buyer pays for THIS product or its manual
# equivalent, and it is a receipt only when it names all five of these.
# Vocabulary mirrors web/lib/data.ts PRICE_UNITS / PRICE_BASES exactly.
PRICE_FIELDS = ("payer", "amount_czk", "unit", "basis", "date")
PRICE_UNITS = ("per-seat-month", "per-case", "per-year", "per-project", "one-off", "per-hour")
PRICE_BASES = ("list-price", "signed-contract", "tender-line", "buyer-interview",
               "manual-equivalent")
# The First-moves threshold: a record worth a builder's quarter. The page prints
# the house absence line below it when no price receipt is on file.
PRICE_EXPECTED_FROM = 7


def buyers_by_ico():
    """IČO -> {distinct public buyer IČO} from data/lookup/cz-contract-parties.jsonl.

    A registr smluv contract has a `payer` and a `recipient`; publication is
    compulsory precisely because one side is a public body, so the distinct
    payer IČOs facing a vendor ARE its distinct public buyers. Built once,
    lazily: 14,918 rows is nothing, but a checker that reads them per record
    would read them 34 times.

    Missing file -> empty map, and the limb simply cannot be evaluated. It is
    never treated as a NEGATIVE: absence of a receipt is not evidence, which is
    the same asymmetry SCORING.md states for gap authority.
    """
    global _BUYERS
    if _BUYERS is not None:
        return _BUYERS
    _BUYERS, by_contract = {}, {}
    if not os.path.isfile(PARTIES):
        return _BUYERS
    with open(PARTIES, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except ValueError:
                continue
            by_contract.setdefault(r.get("signal_id"), []).append(r)
    for parties in by_contract.values():
        payers = {p["ico"] for p in parties if p.get("role") == "payer" and p.get("ico")}
        for p in parties:
            if p.get("role") == "recipient" and p.get("ico"):
                _BUYERS.setdefault(p["ico"], set()).update(payers - {p["ico"]})
    return _BUYERS


# Certainty a "Suggested solution" may not claim (owner, 2026-09-10: "don't try
# to make it like we know everything"; the label read "Likely solution" until
# 2026-09-15). Outcome verbs and superlatives only — a legal "must" describing
# an obligation is a fact, not an overclaim, so it is deliberately absent. The
# same regex holds `entry.why` and the process figure's `summary.after`.
OVERCLAIM = re.compile(
    r"(?i)\b(?:will (?:solve|fix|end|eliminate|remove|stop|save|cut|make)|guarantee\w*|"
    r"the only\b|the answer\b|eliminat\w*|definitely|certainly|clearly|obviously|best\b|"
    r"perfect\w*|always|never\b|solves?\b|the solution\b)")


# ===========================================================================
# DIFFICULTY TO ENTER — the `entry:` contract (owner, 2026-09-15)
# ===========================================================================
#
# It replaces `build:` — capital / first_revenue / builder / note — which the
# owner struck out in one sentence: "CAPITAL €10–100k / TEAM 2–5 people is
# pretty arbitrary, more abstract categories will be more truthful". A euro
# band and a headcount were a prediction about a team nobody has met. These
# five gates are facts about the market the record already carries evidence
# for: who signs the first contract, what an entrant must be ALLOWED before
# selling, who is already here, what the product must plug into, and whether
# the first sale can be reached on the builder's own money.
#
# TWO OF THE SEVEN KEYS ARE DERIVED, AND THAT IS WHY THIS FILE HOLDS THE RULE.
# `incumbents` is read straight off the `locals[]` ledger and `level` is read
# off the five gate weights, so both are checkable without judgment — and a
# derived value an author writes by hand is a value that drifts from its source
# the first time the ledger changes underneath it. The register has shipped
# that defect three times (gap 0, proof 2, locals.status), which is the whole
# reason CLAUDE.md rule 2 exists: a rule enforced by prose is not enforced.

ENTRY_KEYS = ("level", "buyer", "permission", "incumbents", "integration", "money", "why")
ENTRY_LEVELS = ("easy", "moderate", "hard", "very-hard")
ENTRY_VOCAB = {
    "buyer": ("small-firms", "large-firms", "public"),
    "permission": ("none", "registration", "licence"),
    "incumbents": ("open", "adjacent", "direct"),
    "integration": ("software", "national-system", "certified"),
    "money": ("bootstrap", "outside-money"),
}
# THE GATES THAT SET THE LEVEL — four of the five (amendment, 2026-09-15).
# `money` is 0 or 2 and has no middle rung: outside money before the first sale
# is a gate of the same order as a regulator's licence, and there is no half of
# it.
#
# `incumbents` IS NOT HERE, AND ITS ABSENCE IS THE RULE, NOT AN OVERSIGHT.
# Established competition is already priced by the `gap` score (0–2) on the
# scorecard; weighing it here too priced one fact twice, and the measured cost
# was that 20 of 37 records came out hard or very-hard and the owner's own
# canonical easy example — an app for trucking firms — came out `hard`. One
# fact, one place (CLAUDE.md rule 1). The gate stays on the record, still
# derived from locals[], still asserted below, still rendered as the ALREADY
# HERE row; it just does not move the level. Difficulty to enter means the
# DOORS: who buys, what permission, what you must plug into, and money.
ENTRY_LEVEL_GATES = {
    "buyer": {"small-firms": 0, "large-firms": 1, "public": 2},
    "permission": {"none": 0, "registration": 1, "licence": 2},
    "integration": {"software": 0, "national-system": 1, "certified": 2},
    "money": {"bootstrap": 0, "outside-money": 2},
}
# `why` renders as one `p.buildnote` sentence under the ledger. The cap is the
# section's, not a storage limit: a paragraph there is a different device.
ENTRY_WHY_MAX = 320


def entry_level(entry):
    """The level the four weighing gates derive. max 0 -> easy · max 1 ->
    moderate · exactly one 2 -> hard · two or more 2s -> very-hard.
    `incumbents` is not read: gap already prices competition."""
    weights = [ENTRY_LEVEL_GATES[gate][entry[gate]] for gate in ENTRY_LEVEL_GATES]
    twos = sum(1 for w in weights if w == 2)
    if twos >= 2:
        return "very-hard"
    if twos == 1:
        return "hard"
    return "moderate" if max(weights) == 1 else "easy"


def entry_incumbents(locals_):
    """The `incumbents` value the locals[] ledger derives — no judgment.

    A player only closes the field if it SELLS THIS and is ESTABLISHED, which is
    the same asymmetry `gap` reads (SCORING.md): an adjacent player never takes
    the space at any maturity, and an early one never closes it. So the ladder
    is direct+established -> `direct`, else adjacent+established -> `adjacent`,
    else `open` — including the case of no ledger at all, because nobody named
    is nobody established.
    """
    if any(l.get("competes") == "direct" and l.get("maturity") == "established"
           for l in locals_):
        return "direct"
    if any(l.get("competes") == "adjacent" and l.get("maturity") == "established"
           for l in locals_):
        return "adjacent"
    return "open"


def check_entry(doc, locals_):
    """The `entry:` block, asserted. -> [error strings].

    NOT exempt for rejected records, exactly like `solution:`: the block is
    required on every record the owner ruled, and a rejected record still
    answers "how hard would this have been to enter". The derivations are the
    reason it is asserted rather than trusted.
    """
    errors = []
    if "build" in doc:
        errors.append(
            "`build:` was replaced by `entry:` on 2026-09-15 — the capital ladder, the "
            "team band and the time to first revenue are retired. Write the five gates "
            "(buyer, permission, incumbents, integration, money) plus the derived `level` "
            "and a `why`; data/RECORD-TEMPLATE.md has the block")
    entry = doc.get("entry")
    if not isinstance(entry, dict):
        errors.append(
            "no `entry:` — the difficulty-to-enter block is required on every record, "
            "rejected ones included: level, buyer, permission, incumbents, integration, "
            "money, why (data/CONVENTIONS.md, difficulty to enter)")
        return errors
    extra = sorted(set(entry) - set(ENTRY_KEYS))
    if extra:
        errors.append(f"entry carries unknown key(s) {', '.join(extra)} — the block is "
                      f"exactly {', '.join(ENTRY_KEYS)}")
    # THE GATES FIRST. A bad value here makes the level underivable, so the
    # level check below runs only when all five read.
    readable = True          # every gate present and in vocabulary
    incumbents_ok = True
    for gate, vocab in ENTRY_VOCAB.items():
        ok = True
        if gate not in entry:
            errors.append(f"entry is missing `{gate}` — all five gates are required on "
                          f"every record, and four of them derive the level")
            ok = False
        elif entry[gate] not in vocab:
            errors.append(f"entry.{gate} is {entry[gate]!r} — the enum is "
                          f"{' | '.join(vocab)} (data/CONVENTIONS.md, difficulty to enter)")
            ok = False
        if not ok:
            if gate == "incumbents":
                incumbents_ok = False
            else:
                readable = False

    # INCUMBENTS IS NOT A JUDGMENT — it is read off the locals[] ledger, and a
    # hand-written value that disagrees with the ledger is the record telling
    # the reader one thing and its own evidence another.
    if incumbents_ok:
        want = entry_incumbents(locals_)
        if entry["incumbents"] != want:
            named = ", ".join(str(l.get("name")) for l in locals_[:3]) or "no locals[] ledger"
            errors.append(
                f"entry.incumbents is {entry['incumbents']!r} but locals[] derives "
                f"{want!r} ({named}) — the rule is: any local at competes: direct AND "
                f"maturity: established is `direct`; else any at competes: adjacent AND "
                f"maturity: established is `adjacent`; else `open`. Fix the ledger or the "
                f"value, never the value alone")

    if "level" not in entry:
        errors.append("entry is missing `level` — it is derived from buyer, permission, "
                      "integration and money (max 0 easy · max 1 moderate · one gate at 2 "
                      "hard · two or more 2s very-hard) and written down so the index can "
                      "sort on it")
    elif entry["level"] not in ENTRY_LEVELS:
        errors.append(f"entry.level is {entry['level']!r} — the enum is "
                      f"{' | '.join(ENTRY_LEVELS)}")
    elif readable:
        want = entry_level(entry)
        if entry["level"] != want:
            weights = ", ".join(f"{g} {ENTRY_LEVEL_GATES[g][entry[g]]}"
                                for g in ENTRY_LEVEL_GATES)
            errors.append(
                f"entry.level is {entry['level']!r} but the gates derive {want!r} "
                f"({weights}) — the level is not a judgment: max weight 0 is easy, max 1 "
                f"moderate, exactly one gate at 2 hard, two or more at 2 very-hard. "
                f"`incumbents` is NOT weighed — the gap score already prices competition")

    why = entry.get("why")
    if not isinstance(why, str) or not why.strip():
        errors.append("no `entry.why:` — one or two plain sentences naming the gate(s) "
                      "that set the level, or the level is a verdict with no reasoning")
    else:
        if len(why) > ENTRY_WHY_MAX:
            errors.append(f"entry.why is {len(why)} chars (max {ENTRY_WHY_MAX}) — it is one "
                          f"or two sentences under the ledger, not a paragraph")
        for claim in OVERCLAIM.findall(why):
            errors.append(f"entry.why claims certainty ('{claim}') — it names the gates a "
                          f"builder would meet, it does not promise an outcome")
    return errors


# ===========================================================================
# THE PROCESS FIGURE — the `process:` block (owner, 2026-09-15)
# ===========================================================================
#
# OPTIONAL, AND THE OPTION IS THE POINT. It is authored only where the
# record's problem is a workflow somebody performs today. Roughly a dozen of
# the live records describe a new obligation or a one-off decision instead,
# and a process drawn for one of those would be invented rather than read —
# which is the failure this register exists to avoid (MATCH.md §3).
#
# UNCERTAINTY IS A VALUE HERE, NEVER A SILENCE. Owner, 2026-09-15: "be SUPER
# CLEAR about where we're not sure how the process looks, put question marks
# if you don't know." `known` carries that in ONE field — `documented` (stated
# in cited evidence), `inferred` (our reading of the record's own prose) and
# `unknown` (we do not know, and the page draws a "?"). The pairing with
# `cites` is what keeps the three values from shading into one another:
# `documented` with no citation is just a confident sentence, and `unknown`
# with one is a step somebody documented after all. Both are refused below,
# because the whole value of the figure is that a reader can tell which parts
# of it are receipts.
#
# ONE FIELD, ONE MEANING (CLAUDE.md rule 1). The block describes the workflow
# and NOTHING ELSE. A crown figure belongs on a `type: price` receipt, which
# carries the payer, the unit and the basis that make a number checkable; a
# competitor belongs on `comps[]` or `locals[]`, which carry the maturity test
# and the derivations that read off them. Restating either inside a figure is
# the same fact in two places, and it is the defect this register has already
# shipped four separate times (MATCH.md §0).
#
# `web/lib/data.ts` types the same shape in zod, and the redundancy is
# deliberate: zod dies on the first bad record inside the site build, this
# runs in `prebuild` ahead of it and reports every record at once. `scripts/
# db.py` validates none of it — `process` rides `problems.extra_json`
# verbatim — so this file is the only gate the DB loader has.

PROCESS_KEYS = ("summary", "steps")
PROCESS_SUMMARY_KEYS = ("today", "after")
PROCESS_STEP_KEYS = ("who", "today", "known", "cites", "reenters", "change", "after")
PROCESS_KNOWN = ("documented", "inferred", "unknown")
PROCESS_CHANGES = ("stays", "changes", "goes", "new")
# Two steps is a process; one is a sentence, and the record already has one of
# those in `solution:`.
PROCESS_MIN_STEPS = 2
# The same cap `entry.why` carries, for the same reason: these are single
# lines on the page, and a paragraph there is a different device.
PROCESS_SUMMARY_MAX = 320

_MARKER_ANY = re.compile(r"\[S[\d,S]+\]")


def markers(text):
    r"""Every S-number a field's [Sn] markers name. -> {int}.

    The compound form is the reason this is a function. `[S2,S7,S16]` is one
    marker naming three sources, and the `\[S(\d+)` pattern the body check
    uses reads only the first of them — which is survivable on body prose,
    where a dead S7 renders as literal text a reader can see, and is not
    survivable here, where the page turns each number into a link.
    """
    return {int(n) for m in _MARKER_ANY.findall(text) for n in re.findall(r"\d+", m)}

# A CROWN FIGURE INSIDE THE FIGURE. Broader than the `price_search` pattern
# above because a process line writes money the way prose does ("~9M CZK",
# "€3,000 a year"), and narrower than "any number": a count of steps, a count
# of towns and a date are what a process legitimately says.
PROCESS_MONEY = re.compile(
    r"(?i)\d[\d\s.,]*\s?(?:m|bn|k|mil|tis)?\s?(?:CZK|Kč|EUR|€|USD|GBP)"
    r"|[€$£]\s?\d|\b\d{1,3}(?:[ .]\d{3}){1,}\b")

# The banned-word style checks are CASE-SENSITIVE and whole-word: these are
# proper names, and the lower-case forms are ordinary English the register is
# entitled to use — the same lesson VERDICTS above was written for.
_NAME_WORD = "[^\\W]"


def process_texts(proc):
    """Every rendered string inside a process block, with a label for each."""
    out = []
    summary = proc.get("summary")
    if isinstance(summary, dict):
        for key in PROCESS_SUMMARY_KEYS:
            if isinstance(summary.get(key), str):
                out.append((f"summary.{key}", summary[key]))
    steps = proc.get("steps")
    for i, s in enumerate(steps if isinstance(steps, list) else (), 1):
        if not isinstance(s, dict):
            continue
        for key in ("who", "today", "after"):
            if isinstance(s.get(key), str):
                out.append((f"steps[{i}].{key}", s[key]))
    return out


def ledger_name_candidates(comps, locals_):
    """Distinctive comps[]/locals[] names — the one-fact-one-place matcher.

    DISTINCTIVE ONLY, AND THE NARROWING IS DELIBERATE. This register's own
    ledgers carry companies called Better, Enter, Figures and Florence, and a
    build gate that failed the honest sentence "Enter the codes" would be a
    gate everyone learns to skip. A name earns a match by LOOKING like one:
    more than one word, an internal capital or digit, a punctuation mark, or
    ALL CAPS. A plain Capitalised single word is left through on purpose; the
    check catches the common case and never cries wolf.
    """
    out = set()
    for item in list(comps) + list(locals_):
        raw = str(item.get("name") or "")
        for piece in [re.sub(r"\([^)]*\)", " ", raw)] + re.findall(r"\(([^)]*)\)", raw):
            for cand in re.split(r"\s*[/|]\s*", piece):
                cand = cand.strip(" ,.-—·")
                if len(cand) < 3:
                    continue
                if (" " in cand or cand.isupper() or re.search(r"[^\w\s]", cand)
                        or re.search(r"(?<=.)[A-Z0-9]", cand)):
                    out.add(cand)
    return sorted(out, key=len, reverse=True)


# Sentence ends that a one-sentence field may not contain. A terminator only
# counts when a CAPITAL follows it, and an abbreviation or a single-letter
# initial before it does not count at all — "s.r.o." and "J. Novák" are not
# sentence breaks, and a checker that said they were would be wrong on the
# records most likely to carry them.
_SENT_ABBREV = frozenset((
    "s.r.o.", "a.s.", "spol.", "č.", "no.", "e.g.", "i.e.", "cf.", "sb.",
    "resp.", "tj.", "atd.", "apod.", "mj.", "tzv.",
))


def extra_sentences(text):
    """How many sentence breaks a field carries beyond its first sentence."""
    t = _MARKER_ANY.sub("", text)
    n = 0
    for m in re.finditer(r"(\S*[.!?])\s+(\S)", t):
        head, nxt = m.group(1), m.group(2)
        if not nxt[0].isupper():
            continue
        if head.lower() in _SENT_ABBREV or re.fullmatch(r"[^\W\d_]\.", head):
            continue
        n += 1
    return n


# PROCESS STEP TEXT IS A SHORT PHRASE (owner, 2026-09-18: "the texts could be
# shorter, it's kinda long now, too wide"). The hub figure (lib/figures/
# process.tsx) prints each drawn step's `today` and `after` VERBATIM beside its
# person, so each is a phrase of about 4-8 words; detail belongs in
# `summary.today` / `summary.after` (the Read more sheet) or the body. Counted
# on what the hub draws: `today` of a step with a known actor, `after` of a step
# the solution changes or adds. A '?' step's `today` is the open question, a
# sentence under the figure, and is exempt. An ERROR on a record in
# PROCESS_PHRASE_ENFORCED (shortened already); a WARNING on every other one.
# A record joins the set in the same change that shortens its steps.
PROCESS_STEP_WORDS_MAX = 10
PROCESS_PHRASE_ENFORCED = frozenset({"p-0002", "p-0003", "p-0004", "p-0005", "p-0007", "p-0009", "p-0010", "p-0025", "p-0027", "p-0031", "p-0032", "p-0033", "p-0036", "p-0038", "p-0040", "p-0041", "p-0042", "p-0044", "p-0046"})


def check_process_phrases(doc):
    """Drawn process step text over PROCESS_STEP_WORDS_MAX words. -> [messages]."""
    proc = doc.get("process")
    if not isinstance(proc, dict) or not isinstance(proc.get("steps"), list):
        return []
    out = []
    for i, s in enumerate(proc["steps"], 1):
        if not isinstance(s, dict):
            continue
        who = str(s.get("who") or "").strip()
        drawn = []
        if who != "?" and isinstance(s.get("today"), str):
            drawn.append(("today", s["today"]))
        if s.get("change") in ("changes", "new") and isinstance(s.get("after"), str):
            drawn.append(("after", s["after"]))
        for key, text in drawn:
            n = len(_MARKER_ANY.sub("", text).split())
            if n > PROCESS_STEP_WORDS_MAX:
                out.append(f"process step {i} '{who}' `{key}` is {n} words (max "
                           f"{PROCESS_STEP_WORDS_MAX}; aim for 4-8) — the hub prints it "
                           f"verbatim beside its person; move detail to `summary.{key}` "
                           f"or the body (data/RECORD-TEMPLATE.md, Writing the body)")
    return out


def check_process(doc, n_sources, comps, locals_):
    """The `process:` figure, asserted. -> [error strings].

    Absent is the normal case and is never an error: a record with no workflow
    to draw carries no block, and "not drawn" is not a score (MATCH.md §7).
    """
    proc = doc.get("process")
    if proc is None:
        return []
    if not isinstance(proc, dict):
        return ["`process:` is not a block — it is a `summary` (today, and an optional "
                "after) plus an ordered `steps:` list of at least two steps "
                "(data/RECORD-TEMPLATE.md, Figures)"]
    errors = []
    extra = sorted(set(proc) - set(PROCESS_KEYS))
    if extra:
        errors.append(f"process carries unknown key(s) {', '.join(extra)} — the block is "
                      f"exactly {', '.join(PROCESS_KEYS)}")

    # ---- the summary: the line a reader gets without reading the diagram ---
    summary = proc.get("summary")
    if not isinstance(summary, dict):
        errors.append(
            "process has no `summary:` — `summary.today` is REQUIRED whenever a process "
            "is drawn. The steps are the diagram; this is the one plain sentence a reader "
            "gets who does not read it, and a figure with no sentence under it is a "
            "picture the page cannot caption")
        summary = {}
    else:
        extra = sorted(set(summary) - set(PROCESS_SUMMARY_KEYS))
        if extra:
            errors.append(f"process.summary carries unknown key(s) {', '.join(extra)} — it "
                          f"is `today` (required) and `after` (optional)")
        today = summary.get("today")
        if not isinstance(today, str) or not today.strip():
            errors.append(
                "no `process.summary.today:` — one plain sentence saying how the work runs "
                "today, required on every process block. Where part of it is unknown, the "
                "sentence says so; 'not known' is a thing to write down, never a thing to "
                "leave out (MATCH.md §7)")
        else:
            if len(today) > PROCESS_SUMMARY_MAX:
                errors.append(f"process.summary.today is {len(today)} chars (max "
                              f"{PROCESS_SUMMARY_MAX}) — it is one line above the figure, "
                              f"not a paragraph")
            if extra_sentences(today):
                errors.append("process.summary.today runs to more than one sentence — the "
                              "steps carry the detail; this line carries the shape")
            dead = sorted(n for n in markers(today) if n > n_sources)
            if dead:
                errors.append(f"process.summary.today cites "
                              f"{', '.join('S%d' % n for n in dead)} — {n_sources} sources "
                              f"on file; an unresolved marker renders as literal text")
        after = summary.get("after")
        if after is not None:
            if not isinstance(after, str) or not after.strip():
                errors.append("process.summary.after is present but empty — it is one "
                              "sentence on the process with the suggested solution "
                              "applied, or the key is absent")
            else:
                if len(after) > PROCESS_SUMMARY_MAX:
                    errors.append(f"process.summary.after is {len(after)} chars (max "
                                  f"{PROCESS_SUMMARY_MAX}) — one line inside the Suggested "
                                  f"solution box, not a paragraph")
                if extra_sentences(after):
                    errors.append("process.summary.after runs to more than one sentence — "
                                  "it is the proposal in a line; the steps carry the rest")
                if _MARKER_ANY.search(after):
                    errors.append(
                        "process.summary.after carries an [Sn] marker — the after half is "
                        "the SUGGESTED solution, a proposal of ours, and no source on this "
                        "record is evidence for it. Citing one dresses our proposal as "
                        "somebody's finding")
                for claim in OVERCLAIM.findall(after):
                    errors.append(f"process.summary.after claims certainty ('{claim}') — it "
                                  f"sits under a box labelled SUGGESTED; describe the "
                                  f"process, never promise the outcome")

    # ---- the steps --------------------------------------------------------
    steps = proc.get("steps")
    if not isinstance(steps, list) or not steps:
        errors.append("process has no `steps:` — the block is a summary plus an ORDERED "
                      "list of steps, each saying who does it today and what the suggested "
                      "solution does to it")
        steps = []
    elif len(steps) < PROCESS_MIN_STEPS:
        errors.append(f"process draws {len(steps)} step(s) — a process is at least "
                      f"{PROCESS_MIN_STEPS}. One step is a sentence, and the record "
                      f"already has one of those in `solution:`")

    for i, s in enumerate(steps, 1):
        where = f"process step {i}"
        if not isinstance(s, dict):
            errors.append(f"{where} is not a block — every step is who / today / known / "
                          f"cites / change / after")
            continue
        who = s.get("who")
        where = f"process step {i} '{who}'" if isinstance(who, str) and who.strip() else where
        extra = sorted(set(s) - set(PROCESS_STEP_KEYS))
        if extra:
            errors.append(f"{where} carries unknown key(s) {', '.join(extra)} — a step is "
                          f"exactly {', '.join(PROCESS_STEP_KEYS)} (`reenters` optional)")
        if not isinstance(who, str) or not who.strip():
            errors.append(f"{where} has no `who:` — name who performs it in plain words, "
                          f"or '?' where the record does not say")

        known, change = s.get("known"), s.get("change")
        if known not in PROCESS_KNOWN:
            errors.append(
                f"{where} has known {known!r} — the enum is {' | '.join(PROCESS_KNOWN)}. It "
                f"says how the TODAY column is known: `documented` is stated in cited "
                f"evidence, `inferred` is our reading of this record's prose, `unknown` is "
                f"that we do not know and the page draws a '?'")
        if change not in PROCESS_CHANGES:
            errors.append(
                f"{where} has change {change!r} — the enum is {' | '.join(PROCESS_CHANGES)}. "
                f"It says what the suggested solution does to the step: `stays` untouched, "
                f"`changes` shape, `goes` away, or is `new`")

        # NULLABILITY IS NOT A STYLE QUESTION — the renderer draws a missing
        # column from it. A step with no `today` that is not `new` is a step
        # whose left-hand cell the page has nothing to put in.
        if change in PROCESS_CHANGES:
            today = s.get("today")
            if change == "new" and today is not None:
                errors.append(f"{where} is change: new but writes a `today` — a step the "
                              f"suggested solution ADDS has no today; set today: null, or "
                              f"the change is `changes`, not `new`")
            elif change != "new" and (not isinstance(today, str) or not today.strip()):
                errors.append(f"{where} is change: {change} but has no `today` — only a "
                              f"`new` step may set today: null. Every other step exists "
                              f"today and the page prints it")
            after = s.get("after")
            if change == "goes" and after is not None:
                errors.append(f"{where} is change: goes but writes an `after` — a step the "
                              f"suggested solution REMOVES has no after; set after: null, "
                              f"or the change is `changes`, not `goes`")
            elif change != "goes" and (not isinstance(after, str) or not after.strip()):
                errors.append(f"{where} is change: {change} but has no `after` — only a "
                              f"`goes` step may set after: null. Every other step survives "
                              f"into the Suggested solution box and the page prints it")

        # KNOWN AND CITES ARE ONE PAIRING, AND EACH HALF WITHOUT THE OTHER
        # MEANS SOMETHING ELSE ENTIRELY.
        cites = s.get("cites")
        if not isinstance(cites, list) or any(
                isinstance(n, bool) or not isinstance(n, int) or n < 1 for n in cites):
            errors.append(f"{where} has cites {cites!r} — a list of 1-based S-numbers into "
                          f"sources[] ([] when none, never absent)")
        else:
            dead = sorted(n for n in cites if n > n_sources)
            if dead:
                errors.append(f"{where} cites {', '.join('S%d' % n for n in dead)} — "
                              f"{n_sources} sources on file; the page draws each cite as a "
                              f"link into the Sources ledger and these link nowhere")
            if known == "documented" and not cites:
                errors.append(
                    f"{where} is known: documented with no cites — a step stated in "
                    f"evidence names the evidence. Without one it is `inferred`, which is "
                    f"an honest value and costs the figure nothing but a dashed line")
            if known == "unknown" and cites:
                errors.append(
                    f"{where} is known: unknown but cites "
                    f"{', '.join('S%d' % n for n in cites)} — a source that describes the "
                    f"step makes it documented or inferred. `unknown` is for a step we "
                    f"cannot describe at all, and the page prints a '?' for it")

        # A `new` step has no today, so there is nothing for it to re-enter.
        if s.get("reenters") is not None and not isinstance(s.get("reenters"), bool):
            errors.append(f"{where} has reenters {s.get('reenters')!r} — true or false; "
                          f"omit the key where the step enters nothing twice")
        elif s.get("reenters") is True and s.get("today") is None:
            errors.append(f"{where} sets reenters on a step with no today — re-entry is a "
                          f"property of the work as it runs NOW, and a step the suggested "
                          f"solution adds has no now")

        if isinstance(s.get("after"), str) and _MARKER_ANY.search(s["after"]):
            errors.append(
                f"{where} writes an [Sn] marker into `after` — the after column is the "
                f"suggested solution, and the record holds no evidence for what it "
                f"proposes. `cites` backs the TODAY column only")

    # ---- ONE FIELD, ONE MEANING: money and competitors live elsewhere ------
    names = ledger_name_candidates(comps, locals_)
    for label, text in process_texts(proc):
        for amount in PROCESS_MONEY.findall(text):
            errors.append(
                f"process.{label} states a crown figure ('{amount.strip()}') — money is a "
                f"`type: price` receipt, which names the payer, the unit, the basis and the "
                f"date that make a number checkable. A figure repeating it carries the "
                f"number without any of them (CLAUDE.md rule 1)")
        for name in names:
            if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text):
                errors.append(
                    f"process.{label} names '{name}', which is on this record's comps[] or "
                    f"locals[] ledger — who sells what is the ledgers' question, and they "
                    f"carry the maturity test that makes the claim mean something. Name the "
                    f"ROLE the step belongs to instead ('the dispatch software', 'a "
                    f"compliance-documents seller')")
                break
    return errors


# ===========================================================================
# THE HEADLINE BLOCK — `brief:` and `good_for:` (owner, 2026-09-16)
# ===========================================================================
#
# A general builder reads a record top-down as: a short, urgent, concrete
# `title` → a `brief` of at most TWO sentences telling what is happening and
# why it is urgent now → the `solution` as a call to action → `good_for`, who
# it suits. The
# owner's cap is "3 bullets at most" per problem — brief, Suggested, Good for —
# which is why `brief` is a single string and not a list (it was briefly a
# list of 1–3 on the same day). Both fields are OPTIONAL; absent is never an
# error.
#
# ONE FIELD, ONE MEANING (CLAUDE.md rule 1), and these two sit right beside the
# fields they are most likely to bleed into:
#   brief    — FACTS ABOUT THE SITUATION ONLY: who is affected, the date, the
#              penalty, the shortage. It is the one place on the headline that
#              asserts things about the world, so every number and date in it
#              is cited, and it may not propose (that is `solution`), name a
#              ledger company (that is comps[]/locals[]) or claim certainty.
#   good_for — A PERSON, never a market: skills and interests. The moment it
#              carries a number, a citation or a market adjective it has become
#              a second, uncited brief — the same fact in two places, one of
#              them without its receipt.
#
# `web/lib/data.ts` types both and resolves the brief's markers; this file owns
# every other rule. `scripts/db.py` validates neither (both ride extra_json).

# The cap was one sentence and 25 words when the field landed. The owner's
# approved copy for p-0008 and p-0036 (2026-09-16) tells the situation as a
# short story — who is stuck, and what forces it now — which took two sentences
# and up to 39 words every time, so the cap moved to what the approved copy
# needs and no further. A third sentence is a paragraph, and the card has no
# room for one.
BRIEF_MAX_SENTENCES = 2
BRIEF_MAX_WORDS = 40
GOOD_FOR_MAX_WORDS = 15

# A card that carries a `brief` shows `solution:` as "Suggested", read as a call
# to action, and every approved one opens with the verb (owner, 2026-09-16:
# "Build a small security agency…", "Build report templates inside…"). Records
# with no brief still carry the older descriptive sentence, so the rule binds
# only where the card does.
SOLUTION_OPENER = "Build "

# Where `solution:` points abroad, it says HOW MANY companies and WHERE, counted
# off this record's own comps[] (owner, 2026-09-16: fill "do abroad" with "X
# companies do in Y countries"). "As companies already do abroad" read as proof
# on nine records while p-0031 held one comparable and p-0035 none that sold the
# thing, and "as in Germany" did not parse at all. The count is the author's
# judgment (only comps that sell THIS count); the checker holds the ceiling: a
# count can never exceed the comps on file, nor a country be one no comp is
# based in. Y >= 2 is counted, Y = 1 is named:
#   "…, as 4 companies already do in 3 other countries."
#   "…, as 3 companies already do in Germany."   "…, as 1 company already does in the Netherlands."
SOLUTION_VAGUE_ABROAD = re.compile(r"(?i)\babroad\b|\bas in [A-Z]\w*")
SOLUTION_COUNT_ANY = re.compile(
    r"(?i)\b(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten)\s+compan(?:y|ies)\b")
SOLUTION_ABROAD_COUNT = re.compile(
    r"\bas (?P<n>\d+) (?P<noun>company|companies) already (?P<verb>does|do) in "
    r"(?:(?P<m>\d+) other countries|(?:the )?(?P<country>[A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+)*))"
    r"\.\s*$")
# The names a solution may use, mapped to the comps[] `geo` code. English short
# names as web/lib/format.ts COUNTRY_NAMES prints them, plus "Britain", which the
# records' own prose uses. A name missing here fails loudly rather than passing.
COUNTRY_CODES = {
    "Austria": "AT", "Belgium": "BE", "Britain": "GB", "Canada": "CA", "Denmark": "DK",
    "Estonia": "EE", "Finland": "FI", "France": "FR", "Germany": "DE", "Iceland": "IS",
    "Ireland": "IE", "Israel": "IL", "Italy": "IT", "Lithuania": "LT", "Netherlands": "NL",
    "Norway": "NO", "Poland": "PL", "Slovakia": "SK", "Slovenia": "SI", "Spain": "ES",
    "Sweden": "SE", "Switzerland": "CH", "Ukraine": "UA", "United Kingdom": "GB",
    "United States": "US",
}


def _comp_geo(comp):
    """A comp's `geo` as an ISO code. YAML 1.1 reads a bare `NO` as False, so
    Norway (p-0027 Audun, p-0029 Documaster) arrives as a boolean."""
    geo = comp.get("geo")
    if geo is False:
        return "NO"
    return str(geo or "").strip().upper()


def check_solution_abroad(solution, comps):
    """The abroad clause of `solution:` against comps[]. -> [error strings]."""
    errors = []
    if not isinstance(solution, str):
        return errors
    for m in SOLUTION_VAGUE_ABROAD.finditer(solution):
        errors.append(
            f"`solution:` points abroad vaguely ('{m.group(0)}') — say how many comparables "
            f"do this and where they are based: \"as 3 companies already do in Germany\", "
            f"\"as 4 companies already do in 3 other countries\", counted from comps[] "
            f"(RECORD-TEMPLATE.md, the headline block)")
    if not SOLUTION_COUNT_ANY.search(solution):
        return errors
    m = SOLUTION_ABROAD_COUNT.search(solution)
    if not m:
        errors.append(
            "`solution:` counts companies outside the one approved closing clause — end it "
            "\"…, as N companies already do in M other countries.\" or \"…, as N companies "
            "already do in <Country>.\", so the checker can hold the count against comps[]")
        return errors
    n = int(m.group("n"))
    if n < 1:
        errors.append("`solution:` counts 0 companies abroad — with none, drop the clause")
        return errors
    if (n == 1) != (m.group("noun") == "company") or (n == 1) != (m.group("verb") == "does"):
        errors.append(f"`solution:` says '{m.group(0).strip()}' — write \"1 company already "
                      f"does\" and \"N companies already do\"")
    foreign = [g for g in (_comp_geo(c) for c in comps) if g and g != "CZ"]
    if n > len(foreign):
        errors.append(
            f"`solution:` claims {n} companies abroad, but comps[] holds {len(foreign)} "
            f"outside Czechia — the count is taken from the ledger, and only comps that sell "
            f"this thing count")
    if m.group("m") is not None:
        k = int(m.group("m"))
        if k < 2:
            errors.append("`solution:` says 'in 1 other countries' — with one country, name "
                          "it: \"as 3 companies already do in Germany\"")
        if k > len(set(foreign)):
            errors.append(
                f"`solution:` claims {k} countries, but comps[] is based in "
                f"{len(set(foreign))} outside Czechia ({', '.join(sorted(set(foreign))) or 'none'}) "
                f"— count the countries the counted comps are BASED in (`geo`), not their markets")
        if k > n:
            errors.append(f"`solution:` claims {n} companies in {k} countries — a company is "
                          f"based in one country")
    else:
        name = m.group("country")
        code = COUNTRY_CODES.get(name)
        if code is None:
            errors.append(
                f"`solution:` names '{name}' as the country abroad, which COUNTRY_CODES in "
                f"scripts/check-records.py does not know — add it there if it is a country")
        elif n > foreign.count(code):
            errors.append(
                f"`solution:` claims {n} {'company' if n == 1 else 'companies'} in {name}, but "
                f"comps[] has {foreign.count(code)} based there (geo {code}) — name the country "
                f"the counted comps are BASED in, or count the countries instead")
    return errors

# Digits, not words, for a number in a headline that sits over a brief card
# (owner, 2026-09-16: "6,000 Czech towns", never "Six thousand Czech firms").
# Cardinals two to ninety, and a bare singular magnitude ("a thousand"), are
# numbers a digit writes better. Deliberately NOT here: "one", which is
# ordinary prose far more often than a count ("one-man firms", "one by one",
# "the one place"), and the plurals "hundreds"/"thousands", which are vague
# quantities no digit expresses. "twice" and "double" are not cardinals.
TITLE_NUMBER_WORD = re.compile(
    r"(?i)\b(?:two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|"
    r"forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion)\b")

# A claim that needs a receipt: any digit, a spelled-out magnitude, or a month.
# Deliberately NOT "most"/"many" — quantity words without a figure are judged
# by the author against MATCH.md §3, not pattern-matched here. "May" and
# "March" are left out of the months because they are also English verbs
# ("fines may reach"); a real date carries a digit anyway.
NUMERIC_CLAIM = re.compile(
    r"\d|(?i:\b(?:hundreds?|thousands?|millions?|billions?|percent|per cent|dozens?|"
    r"half|twice|double|triple|january|february|april|june|july|august|"
    r"september|october|november|december)\b)")

# Proposal language in a situation sentence. Narrow on purpose (the VERDICTS
# lesson): it catches a brief that has started pitching, not every sentence
# containing "build". A bare "should" is left out: a legal duty ("towns
# should have registered by …") is a fact, the same reason OVERCLAIM omits
# "must".
BRIEF_PROPOSAL = re.compile(
    r"(?i)\b(?:suggest\w*|solutions?|opportunit\w*|start-?ups?|build (?:a|an|the)|"
    r"you (?:can|could|should)|a product that|a service that|sell to)\b")

# Market claims in a line that is meant to describe a person.
# good_for opens with the PERSON (owner, 2026-09-16: "Good for should always
# start with a person" — "Mapping and aerial-photo people…" rendered as "Good
# for mapping…"). The card prints the label "Good for" straight before this
# line, so its first word must name who: a pronoun-like opener or a role noun.
# Extend the list when a real role needs it; never loosen it to a pattern.
GOOD_FOR_PERSON_OPENERS = frozenset((
    "someone", "anyone", "people", "builders", "developers", "engineers",
    "founders", "accountants", "lawyers", "designers", "operators", "nurses",
    "doctors", "teachers", "researchers", "consultants", "teams"))

GOOD_FOR_MARKET = re.compile(
    r"(?i)\b(?:markets?|demand|growing|growth|booming|huge|lucrative|profitable|"
    r"underserved|untapped|wide open|no competition|buyers? (?:are|is)|customers (?:are|is))\b")


def _words(text):
    # A token counts only if it holds a letter or digit. Stripping a marker
    # that sits before the full stop ("late 2026 [S1,S2].") leaves a lone "."
    # behind, and counting it made the approved 39-word p-0008 brief read as 41.
    return sum(1 for tok in _MARKER_ANY.sub(" ", text).split() if re.search(r"\w", tok))


def check_headline(doc, n_sources, comps, locals_):
    """`brief:` and `good_for:`, plus the `solution:` opener and the title's
    digits on records that carry a brief, asserted. -> [error strings]."""
    errors = check_solution_abroad(doc.get("solution"), comps)

    brief = doc.get("brief")
    if brief is not None:
        if not isinstance(brief, str) or not brief.strip():
            errors.append(
                f"`brief:` is {'empty' if isinstance(brief, str) else type(brief).__name__} — "
                f"it is ONE string of at most two sentences, or the key is absent. The "
                f"owner's cap is three lines per problem (brief, Suggested, Good for), so "
                f"a list here is a second and third line the page has no room for")
        else:
            n = _words(brief)
            if n > BRIEF_MAX_WORDS:
                errors.append(f"brief is {n} words (max {BRIEF_MAX_WORDS}) — at most two "
                              f"short sentences; the detail belongs in the dek")
            if "\n" in brief.strip():
                errors.append("brief carries a line break — it is one short story under the "
                              "headline, written as running text")
            n_sent = 1 + extra_sentences(brief)
            if n_sent > BRIEF_MAX_SENTENCES:
                errors.append(f"brief runs to {n_sent} sentences (max {BRIEF_MAX_SENTENCES}) "
                              f"— who is stuck and what forces it now; a third sentence is "
                              f"a paragraph the card has no room for")
            nums = markers(brief)
            if re.sub(r"\[S[\d,S]+\]", "", brief).find("[S") != -1:
                errors.append("brief carries a malformed [S…] marker — write [S1] or "
                              "[S1,S19]")
            dead = sorted(x for x in nums if x < 1 or x > n_sources)
            if dead:
                errors.append(f"brief cites {', '.join('S%d' % x for x in dead)} — "
                              f"{n_sources} sources on file; the page links each marker "
                              f"into the Sources ledger and these link nowhere")
            if NUMERIC_CLAIM.search(_MARKER_ANY.sub(" ", brief)) and not nums:
                errors.append(
                    "brief states a number or a date with no [Sn] marker — it is the "
                    "headline's only claim about the world, and a figure in it without a "
                    "receipt is exactly the plausibility this register refuses (MATCH.md "
                    "§9: every numeric claim carries an [Sn])")
            for claim in OVERCLAIM.findall(brief):
                errors.append(f"brief claims certainty ('{claim}') — state the fact, not "
                              f"how sure we are of it")
            for word in BRIEF_PROPOSAL.findall(brief):
                errors.append(
                    f"brief proposes ('{word}') — it is the SITUATION only. What to build "
                    f"is `solution:`, and who should build it is `good_for:` (one field, "
                    f"one meaning)")
            for name in ledger_name_candidates(comps, locals_):
                if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", brief):
                    errors.append(
                        f"brief names '{name}', which is on this record's comps[] or "
                        f"locals[] ledger — competition is the ledgers' question and "
                        f"carries its maturity test there; the brief states the situation")
                    break

    good_for = doc.get("good_for")
    if good_for is not None:
        if not isinstance(good_for, str) or not good_for.strip():
            errors.append("`good_for:` is present but empty or not a string — one line "
                          "naming who this suits by skills and interests, or the key is "
                          "absent")
        else:
            n = _words(good_for)
            if n > GOOD_FOR_MAX_WORDS:
                errors.append(f"good_for is {n} words (max {GOOD_FOR_MAX_WORDS}) — one "
                              f"line describing a person")
            if "\n" in good_for.strip() or extra_sentences(good_for):
                errors.append("good_for runs past one line — it is a single description "
                              "of who this suits")
            if re.search(r"\[S", good_for):
                errors.append(
                    "good_for carries an [Sn] marker — it describes a person, and no "
                    "source is evidence for who should build this. A line that needs a "
                    "citation is a fact, and facts go in `brief:`")
            if NUMERIC_CLAIM.search(_MARKER_ANY.sub(" ", good_for)):
                errors.append(
                    "good_for states a number — figures are claims and belong, cited, "
                    "in `brief:`. This line names skills and interests only")
            for claim in OVERCLAIM.findall(good_for):
                errors.append(f"good_for claims certainty ('{claim}') — describe who it "
                              f"suits, never promise it works for them")
            for word in GOOD_FOR_MARKET.findall(good_for):
                errors.append(
                    f"good_for makes a market claim ('{word}') — the size and state of the "
                    f"market are scored and receipted elsewhere; this line describes a "
                    f"person")
            first = re.match(r"\s*([A-Za-z'-]+)", good_for)
            if not first or first.group(1).lower() not in GOOD_FOR_PERSON_OPENERS:
                errors.append(
                    f"good_for opens with '{first.group(1) if first else good_for[:20]}', not a "
                    f"person — the card reads \"Good for <this line>\", so start with who: "
                    f"Someone / People / Engineers / Developers … (GOOD_FOR_PERSON_OPENERS)")

    # ---- rules that bind only where the card is drawn (owner, 2026-09-16) --
    # A record with a `brief` renders the three-line card, and the framing
    # rules in RECORD-TEMPLATE.md apply to it. These two are the mechanical
    # ones; the rest (plain, not abstract, not oddly specific) are judged.
    if isinstance(brief, str) and brief.strip():
        solution = doc.get("solution")
        if isinstance(solution, str) and solution.strip() and \
                not solution.lstrip().startswith(SOLUTION_OPENER):
            errors.append(
                f"`solution:` opens '{solution.strip()[:24]}…' — on a record with a brief it "
                f"is the card's call to action and starts with \"{SOLUTION_OPENER.strip()}\", "
                f"then names the plain business form, where it lives and what it does "
                f"(RECORD-TEMPLATE.md, the headline block)")
        title = doc.get("title")
        if isinstance(title, str):
            spelled = sorted({m.lower() for m in TITLE_NUMBER_WORD.findall(title)})
            if spelled:
                errors.append(
                    f"title spells a number out ({', '.join(spelled)}) — write the digits: "
                    f"\"6,000 Czech towns\", not \"Six thousand\" (RECORD-TEMPLATE.md, the "
                    f"headline block)")
    return errors


# ===========================================================================
# THE DRAFT-LAW BADGE — `draft_law:` (owner, 2026-09-16)
# ===========================================================================
#
# Owner: "Add some badge to all problems that are 'probably': based on a law
# that's not yet released." The page prints a "Draft law" badge, with this
# line on hover. OPTIONAL, and ONE MEANING ONLY: the record's MAIN pain or
# opportunity depends on a law that is not yet passed or published — a bill in
# parliament, a government draft, a planned law, or an EU directive not yet
# transposed where the pain depends on the Czech law. NOT a law in force
# however weakly enforced, NOT a published directly applicable EU regulation
# (a future application date is still released), and NOT a record whose pain
# AND dated change both exist today regardless of a pending bill. Where a
# present pain meets a draft, Why now decides (owner, 2026-09-19): p-0028's
# fines stand under current law, but its Why now rests on the green-claims
# bill alone, so it carries the key.
#
# WHICH records carry it is judged, so no regex attempts that. What is gated is
# the claim itself: "this law is not passed yet" is a statement about the
# world, so it carries a receipt, and the receipt is the legal text or a bill
# tracker — a `regulation` source, the only source type on the ledger that
# holds statutes, drafts, VeKLEP entries, infringement notices and law-firm
# readings of a bill. A news item, a gap check or a price cannot be the status
# receipt of a law.
DRAFT_LAW_MAX_WORDS = 12
DRAFT_LAW_SOURCE_TYPES = frozenset(("regulation",))


def check_draft_law(doc, sources):
    """`draft_law:` asserted. -> [error strings]."""
    errors = []
    if "draft_law" not in doc:
        return errors
    line = doc.get("draft_law")
    if not isinstance(line, str) or not line.strip():
        errors.append(
            f"`draft_law:` is {'empty' if isinstance(line, str) else type(line).__name__} — "
            f"write one plain line naming the unpassed law and its status with an [Sn] "
            f"marker, or leave the key out: absent means the record is not a draft-law "
            f"record (RECORD-TEMPLATE.md, `draft_law:`)")
        return errors
    n = _words(line)
    if n > DRAFT_LAW_MAX_WORDS:
        errors.append(f"draft_law is {n} words (max {DRAFT_LAW_MAX_WORDS}) — it is a hover "
                      f"line under a badge: the law's name and its status, nothing more")
    if "\n" in line.strip():
        errors.append("draft_law carries a line break — it is one line under the badge")
    if _MARKER_ANY.sub("", line).find("[S") != -1:
        errors.append("draft_law carries a malformed [S…] marker — write [S1] or [S1,S2]")
    nums = markers(line)
    if not nums:
        errors.append("draft_law has no [Sn] marker — the badge says a law is not yet "
                      "passed, and that status needs its receipt")
    dead = {x for x in nums if x < 1 or x > len(sources)}
    if dead:
        errors.append(f"draft_law cites {', '.join('S%d' % x for x in sorted(dead))} — "
                      f"{len(sources)} sources on file")
    for x in sorted(nums - dead):
        typ = sources[x - 1].get("type")
        if typ not in DRAFT_LAW_SOURCE_TYPES:
            errors.append(
                f"draft_law cites S{x}, a `type: {typ}` source — a law's status is receipted "
                f"by the legal text or a bill tracker "
                f"(`type: {'|'.join(sorted(DRAFT_LAW_SOURCE_TYPES))}`)")
    for claim in OVERCLAIM.findall(line):
        errors.append(f"draft_law claims certainty ('{claim}') — name the law and where it "
                      f"stands, not what it will do")
    return errors


def established(since, evidence, year, ico=None):
    """The established test, as one function. -> (bool, [limbs passed], [why not]).

    `since` is the year it started selling THIS product; `year` is the
    register's own newest `updated`, NEVER the wall clock — the same
    reproducibility law extractDate() enforces on the site, because a record
    that is established on Tuesday and early on Wednesday is not a test.
    """
    limbs, blockers = [], []
    text = evidence or ""

    # THE ONE LIMB A MACHINE SETTLES BY ITSELF. Every other limb is read off a
    # string a human wrote; this one is counted out of the contract ledger, which
    # is why the IČO is "strongly preferred" on locals[] — it is what turns the
    # claim into a lookup.
    if ico:
        n = len(buyers_by_ico().get(ico, ()))
        if n >= 2:
            limbs.append(f"{n} distinct public buyers in registr smluv")
    for label, pattern in _LIMBS:
        if pattern.search(text):
            limbs.append(label)

    years = None if since is None else year - since
    if years is None:
        blockers.append("no `since` year on file")
    elif years < MIN_YEARS_SELLING:
        blockers.append(f"selling for {years} year(s), the test requires "
                        f">= {MIN_YEARS_SELLING}")
    if not limbs:
        blockers.append("no limb of the test is cited")
    return (not blockers), limbs, blockers


# ===========================================================================
# BODY V2 — the owner-approved writing rules for the body (2026-09-16/17)
# ===========================================================================
#
# data/RECORD-TEMPLATE.md "Writing the body" carries the rules and the reasons;
# pipeline/REWRITE.md carries the procedure. This block holds the ones a
# machine can check without guessing (CLAUDE.md rule 2: a rule enforced by
# prose is not enforced).
#
# THE SWITCH. The 28 records written before these rules fail most of them, and
# turning 28 records red at once would teach everyone to skip this output. So:
#
#   * a record in BODY_V2_ENFORCED gets every GATE finding below as an ERROR,
#     which fails `npm run build`;
#   * every other live record gets ONE summary warning naming its finding
#     counts (its rewrite worklist); `--body-v2` prints each finding in full.
#
# A rewritten record JOINS BODY_V2_ENFORCED IN THE SAME CHANGE as its rewrite
# (pipeline/REWRITE.md, "Done"). When every live record is in the set, delete
# the set and make the gates unconditional.
#
# BODY_V2_WAIVERS: a known, reported defect on an enforced record, printed as a
# warning until it is fixed. It is a debt list, never a way to pass a rewrite:
# a new entry needs the owner's say-so, recorded in that record's Revisions.
# every live record, rewritten to the body rules by 2026-09-18
BODY_V2_ENFORCED = frozenset({
    "p-0001", "p-0002", "p-0003", "p-0004", "p-0005", "p-0006", "p-0007", "p-0008", "p-0009", "p-0010", "p-0011", "p-0017", "p-0018", "p-0022", "p-0023", "p-0024", "p-0025", "p-0026", "p-0027", "p-0028", "p-0029", "p-0030", "p-0031", "p-0032", "p-0033", "p-0034", "p-0035", "p-0036", "p-0037", "p-0038", "p-0040", "p-0041", "p-0042", "p-0044", "p-0045", "p-0046",
})
BODY_V2_WAIVERS: dict[str, frozenset[str]] = {
    # Empty. p-0008's three waivers (ANSWER_WORDS, MOVE_EVIDENCE, PRICE_RESTATED)
    # were cleared by content on 2026-09-17; see its Revisions entry.
}
BODY_V2_DETAIL = False          # set by `--body-v2`

ANSWER_MAX_WORDS = 25           # the rule says "about 20"; the gate allows the "about"
PAGE_ITEMS = 3                  # web/app/(site)/problem/[region]/[id]/page.tsx PAGE_CAP
PAGE_ITEM_MAX_WORDS = 14        # advice only: an item the page shows
MOVE_LEAD_MAX_WORDS = 25        # advice only: the one sentence the page shows per move
MOVES_MIN, MOVES_MAX = 3, 5
ENTRY_ITEM_MIN_WORDS = 3        # a shorter Easier/Harder item is a list split by its own commas

# The anchors the record page emits (page.tsx `Section id` + `alias`). Canonical
# first; the aliases are kept so older links still land. `first-moves` exists
# only on a record with moves, `how-it-works` only with a process figure, and
# `s1…sN` are the rows of the sources drawer.
ANCHORS_CANONICAL = ("opportunity", "solution", "why-now", "willing-to-pay",
                     "validated-abroad", "competition", "execution-difficulty",
                     "first-moves", "sources")
ANCHORS_ALIAS = ("problem", "how-it-works", "who-pays", "how-big", "proven-abroad",
                 "who-sells-this", "local-competition", "difficulty-to-enter")

# "the record" / "this record" said to a reader (owner, 2026-09-17: "The page
# we're looking at is the record isn't it?"). Singular only: "the records" is
# ordinary English about somebody else's files.
SELF_RECORD = re.compile(r"(?i)\b(?:the|this)\s+record(?:'s|’s)?\b(?!s)")

# `- **Key:** value` — the two-column row the owner retired ("should be bullets
# not columns"). No live record uses one since the p-0008 rewrite.
KEYED_BULLET = re.compile(r"^\s*- \*\*[^*]{1,40}?:\*\*", re.M)

# Why now's first items are the pain; a law date there is the old shape
# ("Now it's just explaining laws"). A date-led item: "On 1 November 2025 …",
# "By 17 July 2026 …", "In late 2026 …", "17 Dec 2026: …", "Mid 2027 …".
_MONTH = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|"
          r"Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
DATE_LED = re.compile(
    r"^(?:(?:On|By|In|From|Since|Until|Before|After|Between)\s+)?"
    r"(?:\d{1,2}\s+" + _MONTH + r"|" + _MONTH + r"|(?:early|mid|late)|Q[1-4]|H[12])"
    r"\s+\d{4}\b|^\d{4}\s*:", re.I)

FLUFF = re.compile(
    r"\b(?:demonstrably|notably|crucially|essentially|robust|leverag(?:e|es|ed|ing)|"
    r"landscape|ecosystem|seamless(?:ly)?|game[- ]chang\w*|cutting[- ]edge)\b", re.I)

# lib/sections.ts splitLead, ported: the page's own sentence boundary. ". " at
# bracket depth 0, not inside the first 40 characters, not after an initial or
# a stock abbreviation. A boundary this misses is a boundary the page misses.
_LEAD_ABBR = re.compile(r"(?:(?:^|[\s(])(?:[A-Za-z]|e\.g|i\.e|vs|cf|approx|No|Sb|St|Dr|Mr|"
                        r"Ms|Mrs|Inc|Ltd|Co|Corp|Jr|Sr|cca|tzv|resp|např|tj)|\.[A-Za-z])$")
_LIST_LINE = re.compile(r"^(?:- |\d+\.\s)")


def split_lead(s, floor=40):
    depth = 0
    for i in range(len(s) - 1):
        ch = s[i]
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth = max(0, depth - 1)
        elif depth == 0 and ch == "." and s[i + 1] == " ":
            if i + 1 < floor or _LEAD_ABBR.search(s[:i]):
                continue
            return s[: i + 1], s[i + 2:].strip()
    return s, ""


def reader_words(text):
    """Words a reader sees: no [Sn] markers, link targets or emphasis marks."""
    t = re.sub(r"\[S[\d,\sS]+\]", "", text)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    return len(t.replace("**", "").split())


def body_sections(arg):
    """The body routed the way lib/sections.ts routes it. -> {name: markdown}."""
    out = {"The opportunity": [], "Market gap": [], "Why now": [],
           "Willing to pay": [], "Validated abroad": []}
    cur = out["The opportunity"]
    leads = (("Why now", r"Why now:\s*"), ("Willing to pay", r"Who pays:\s*"),
             ("Market gap", r"Existing non-solutions[^:\n]*:\s*"),
             ("Validated abroad", r"Solved elsewhere[^:\n]*:\s*"))
    for block in re.split(r"\n{2,}", arg):
        p = block.strip()
        if not p or re.fullmatch(r"-{3,}", p):
            continue
        for name, lead in leads:
            if re.match(lead, p, re.I):
                cur = out[name]
                p = re.sub("^" + lead, "", p, flags=re.I)
                break
        cur.append(p)
    return {k: "\n\n".join(v) for k, v in out.items() if v}


def outline(md):
    """page.tsx outline(): the answer paragraph and the first list the page shows.
    -> (first_paragraph, is_one_sentence, list_items)."""
    blocks = [[l.strip() for l in b.split("\n") if l.strip() and l.strip() != "---"]
              for b in re.split(r"\n{2,}", md)]
    blocks = [b for b in blocks if b]
    if not blocks:
        return "", False, []
    b0, k, para = blocks[0], 0, []
    while k < len(b0) and not _LIST_LINE.match(b0[k]):
        para.append(b0[k])
        k += 1
    tail = b0[k:]
    mixed = any(not _LIST_LINE.match(l) for l in tail)
    lst = tail[: next(i for i, l in enumerate(tail) if not _LIST_LINE.match(l))] if mixed else tail
    used = 1
    if not lst and not mixed and len(blocks) > 1 and all(_LIST_LINE.match(l) for l in blocks[1]):
        lst, used = blocks[1], 2
    while not mixed and lst and used < len(blocks) and all(_LIST_LINE.match(l) for l in blocks[used]):
        lst, used = lst + blocks[used], used + 1
    text = " ".join(para)
    return text, bool(text) and split_lead(text)[1] == "", [_LIST_LINE.sub("", l) for l in lst]


def entry_why_items(t):
    """page.tsx splitItems(): one Easier/Harder half -> its items."""
    semi = ";" in re.sub(r"\[[^\]]*\]|\([^)]*\)", "", t)
    out, depth, start = [], 0, 0
    for i, ch in enumerate(t):
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth = max(0, depth - 1)
        elif depth == 0 and (ch == ";" if semi else (ch == "," and t[i + 1:i + 2] == " ")):
            if not semi and re.match(r"(?i)(?:so|which|who|because|but|while|though|since|as|or|"
                                     r"when|where|until)\b", t[i + 1:].lstrip()):
                continue
            out.append(t[start:i])
            start = i + 1
    out.append(t[start:])
    items = [re.sub(r"[.;,\s]+$", "", re.sub(r"(?i)^and\s+", "", x.strip())) for x in out]
    return [x for x in items if x]


def check_body_v2(doc, arg, firstmoves, sources, comps, locals_):
    """The body-v2 rules. -> [(code, gate: bool, message)].

    `gate` findings become ERRORs on a BODY_V2_ENFORCED record; advice
    findings (word targets a page can live with) never fail a build.
    """
    out = []
    add = lambda code, gate, msg: out.append((code, gate, msg))  # noqa: E731
    sections = body_sections(arg)

    # 1. Every section opens with ONE answer sentence the page can set alone.
    for name, md in sections.items():
        para, one, items = outline(md)
        if not para:
            add("ANSWER_SENTENCE", True, f"{name}: no answer sentence — the section opens "
                f"with a list, so the page has no answer line to show")
            continue
        if not one:
            add("ANSWER_SENTENCE", True, f"{name}: the first paragraph is more than one "
                f"sentence (\"{para[:70]}…\") — the page shows only its first sentence; "
                f"end the paragraph there and move the rest into the detail")
        first = split_lead(para)[0]
        if reader_words(first) > ANSWER_MAX_WORDS:
            add("ANSWER_WORDS", True, f"{name}: the answer sentence is {reader_words(first)} "
                f"words (max {ANSWER_MAX_WORDS}, aim for about 20)")
        # 3. The first three items are what the page shows: short.
        for i, item in enumerate(items[:PAGE_ITEMS], 1):
            n = reader_words(item)
            if n > PAGE_ITEM_MAX_WORDS:
                add("PAGE_ITEM_WORDS", False, f"{name}: list item {i} is {n} words and shows "
                    f"on the page (aim ≤{PAGE_ITEM_MAX_WORDS}): \"{item[:60]}…\"")
        # 7. Why now leads with the pain; law dates come after the first three.
        if name == "Why now":
            for i, item in enumerate(items[:PAGE_ITEMS], 1):
                if DATE_LED.match(item):
                    add("WHY_NOW_DATE_FIRST", True, f"Why now: page item {i} opens on a date "
                        f"(\"{item[:50]}…\") — the first three items say who loses what time "
                        f"or money; law dates go after them")

    # 6. Plain bullets, never keyed two-column rows.
    if KEYED_BULLET.search(arg + "\n" + firstmoves):
        add("KEYED_LIST", True, "a `- **Key:** text` row in the body — lists are plain bullet "
            "sentences that start with the number or the subject")

    # 1. Fluff words.
    for w in sorted({m.group(0).lower() for m in FLUFF.finditer(arg + "\n" + firstmoves)}):
        add("FLUFF", True, f"fluff word '{w}' in the body — say the plain thing")

    # 1. No stacked parentheticals: at most one (…) per sentence, never nested.
    plain = re.sub(r"\]\([^)]*\)", "]", re.sub(r"\[S[\d,\sS]+\]", "", arg + "\n" + firstmoves))
    for sent in re.split(r"(?<=[.!?])\s+|\n", plain):
        opens = len(re.findall(r"(?<!\w)\(", sent))   # "AV(D)" is a term, not an aside
        nested = re.search(r"(?<!\w)\([^)]*(?<!\w)\(", sent)
        if opens > 1 or nested:
            add("PARENS_STACKED", True, f"{opens} parentheticals in one sentence: "
                f"\"{sent.strip()[:60]}…\" — one aside per sentence at most; make the rest "
                f"its own sentence")

    # 11. Never "the record" / "this record" where a reader sees it.
    fields = [("body", arg), ("moves", firstmoves)]
    for key in ("title", "brief", "solution", "good_for", "draft_law", "price_search"):
        if isinstance(doc.get(key), str):
            fields.append((key, doc[key]))
    entry = doc.get("entry") if isinstance(doc.get("entry"), dict) else {}
    if isinstance(entry.get("why"), str):
        fields.append(("entry.why", entry["why"]))
    if isinstance(doc.get("process"), dict):
        fields += [(f"process.{k}", v) for k, v in process_texts(doc["process"])]
    fields += [(f"comps[{i}].traction", str(c.get("traction") or "")) for i, c in enumerate(comps, 1)]
    fields += [(f"locals[{i}].evidence", str(l.get("evidence") or "")) for i, l in enumerate(locals_, 1)]
    for i, s in enumerate(sources, 1):
        fields += [(f"S{i}.{k}", s[k]) for k in ("name", "gist", "why") if isinstance(s.get(k), str)]
    for where, text in fields:
        m = SELF_RECORD.search(text)
        if m:
            add("SELF_RECORD", True, f"'{m.group(0)}' in {where} — the reader is on the page; "
                f"say \"this problem\", or just say the thing")

    # 5. Say each fact once: a company lives in its row, a price in its receipt.
    say_once = arg + "\n" + firstmoves
    for name in ledger_name_candidates(comps, locals_):
        if re.search(r"(?<![\w])" + re.escape(name) + r"(?![\w])", say_once):
            add("LEDGER_NAME", True, f"'{name}' is named in the body — a company lives in its "
                f"comps[]/locals[] row; link [Market gap](#competition) or "
                f"[Validated abroad](#validated-abroad) instead")
    prices = {i for i, s in enumerate(sources, 1) if s.get("type") == "price"}
    cited = markers(say_once) & prices
    if cited:
        add("PRICE_RESTATED", True, f"the body cites price receipt(s) "
            f"{', '.join(f'S{n}' for n in sorted(cited))} — a price lives in its receipt; "
            f"link [Willing to pay](#willing-to-pay) instead of restating it")

    # 5. In-page links land.
    anchors = set(ANCHORS_CANONICAL) | set(ANCHORS_ALIAS) | {f"s{i}" for i in range(1, len(sources) + 1)}
    if not firstmoves.strip():
        anchors.discard("first-moves")
    if not isinstance(doc.get("process"), dict):
        anchors.discard("how-it-works")
    for a in sorted(set(re.findall(r"\]\(#([^)\s]+)\)", arg + "\n" + firstmoves))):
        if a not in anchors:
            add("ANCHOR", True, f"in-page link #{a} lands nowhere — use one of "
                f"{', '.join('#' + x for x in ANCHORS_CANONICAL)}")

    # 9. Suggested first moves.
    moves = [re.sub(r"^\d+\.\s+", "", l.strip()) for l in firstmoves.split("\n")
             if re.match(r"^\s*\d+\.\s", l)]
    if firstmoves.strip():
        if not MOVES_MIN <= len(moves) <= MOVES_MAX:
            add("MOVES_COUNT", True, f"{len(moves)} first moves (write {MOVES_MIN}–{MOVES_MAX}, "
                f"each on ONE line)")
        if moves and re.match(r"(?i)(?:sell|pitch)\b", moves[0]):
            add("MOVE1_SELL", True, "move 1 sells — it BUILDS something or CONTACTS someone "
                "specific")
        heavy = [str(i) for i, mv in enumerate(moves, 1)
                 if _MARKER_ANY.search(mv) or re.search(r"\d", re.sub(r"\]\([^)]*\)", "]", mv))]
        if heavy:
            add("MOVE_EVIDENCE", True, f"move(s) {', '.join(heavy)} carry a [Sn] marker or a "
                f"figure — moves link to the section holding the evidence and restate none of it")
        for i, mv in enumerate(moves, 1):
            lead = split_lead(mv)[0]
            if reader_words(lead) > MOVE_LEAD_MAX_WORDS:
                add("MOVE_LEAD_WORDS", False, f"move {i}'s first sentence is "
                    f"{reader_words(lead)} words, and it is all the page shows "
                    f"(aim ≤{MOVE_LEAD_MAX_WORDS})")

    # 10. Execution difficulty: "Easier: … Harder: …", items that survive the split.
    why = entry.get("why") if isinstance(entry.get("why"), str) else ""
    e = re.search(r"(?:^|\s)Easier:\s*([\s\S]*?)(?=\s+Harder:|$)", why)
    h = re.search(r"(?:^|\s)Harder:\s*([\s\S]*?)(?=\s+Easier:|$)", why)
    if not (e and h):
        add("ENTRY_WHY_SIDES", True, "entry.why is not written as \"Easier: a, b, and c. "
            "Harder: x, and y.\" — the page reads the two lists from those two labels")
    for label, m in (("Easier", e), ("Harder", h)):
        for item in entry_why_items(m.group(1)) if m else ():
            if len(item.split()) < ENTRY_ITEM_MIN_WORDS:
                add("ENTRY_WHY_ITEM", True, f"entry.why {label} item \"{item}\" — the page split "
                    f"an item at its own comma; separate the items with semicolons instead")
    return out


# ===========================================================================
# SCORING V2 — the owner-approved money and urgency ladders (2026-09-19)
# ===========================================================================
#
# SCORING.md carries the ladders and the reasons. Two fields each carried two
# meanings (CLAUDE.md rule 1): `urgency` counted "we looked recently" (the
# freshness point, held by every live record) as if it were a deadline, and
# `money` counted "public money moves nearby" under a section named Willing to
# pay. These are the halves of the new rungs a machine can check without
# judging (CLAUDE.md rule 2). Whether a price buys THIS job, whether a law
# binds THIS buyer and whether it has teeth stay MATCH's judgement.
#
#   URGENCY_NO_INSTRUMENT  urgency >= 1 with no `regulation` source backing
#                          urgency. Freshness never earns a point, so a Why now
#                          score with no dated instrument under it is the
#                          freshness point by another name.
#   URGENCY_DRAFT          urgency >= 2 on a record carrying `draft_law:`. A
#                          bill is not enacted, so it fails REAL: rung 1 at most.
#   MONEY_NO_RECEIPT       money >= 1 with no `type: price` source tagged
#                          `dims: [money]`. Public money nearby alone caps money
#                          at 0: tenders, grants and adjacent contracts never
#                          earn a point on their own.
#   MONEY_NOT_PAID         money 2 with no PAID receipt (a money-tagged price at
#                          basis signed-contract or tender-line, dated within 24
#                          months of `updated`) and no lift (a money-tagged price
#                          plus a tender, contract or subsidy backing money).
#   MARKET_GAP_LINK        the body or the moves still link `[Competition](#competition)`.
#                          The section is named Market gap since 2026-09-19; the
#                          anchor is unchanged, the words the reader clicks are not.
#
# THE SWITCH, exactly like BODY_V2_ENFORCED: a record in SCORING_V2_ENFORCED
# gets every finding as an ERROR, which fails `npm run build`; the rest are
# counted in ONE summary line (`--scoring-v2` lists them), because 34 records
# scored before the ladders changed would otherwise flood the report. A record
# JOINS THE SET IN THE SAME CHANGE AS ITS RESCORE
# (docs/scoring-v2/rescore-2026-09-19.md), and joins web/lib/scoring-v2.ts in
# the same change: the page reads a record's two scores on the new ladders only
# when it is there, and SCORING_V2_MIRROR below fails the build when the two
# lists differ. When every live record is in the set, delete the set, the
# mirror and the v1 branches, and make these checks unconditional.
# every live record, rescored to the 2026-09-19 ladders
SCORING_V2_ENFORCED = frozenset({
    "p-0001", "p-0002", "p-0003", "p-0004", "p-0005", "p-0006", "p-0007", "p-0008", "p-0009", "p-0010", "p-0011", "p-0017", "p-0018", "p-0022", "p-0023", "p-0024", "p-0025", "p-0026", "p-0027", "p-0028", "p-0029", "p-0030", "p-0031", "p-0032", "p-0033", "p-0034", "p-0035", "p-0036", "p-0037", "p-0038", "p-0040", "p-0041", "p-0042", "p-0044", "p-0045", "p-0046",
})
SCORING_V2_DETAIL = False       # set by `--scoring-v2`
SCORING_V2_PENDING: dict[str, list[str]] = {}   # not-yet-rescored findings, per record
SCORING_V2_MIRROR = os.path.join(ROOT, "web", "lib", "scoring-v2.ts")
MONEY_PAID_BASES = ("signed-contract", "tender-line")
MONEY_PAID_WINDOW_DAYS = 730    # "within 24 months of `updated`"
MONEY_PUBLIC_TYPES = ("tender", "contract", "subsidy")   # TYPE_TO_DIM -> money


def _iso(d):
    """A YAML date (parsed or quoted) -> datetime.date, or None."""
    import datetime  # noqa: PLC0415
    if isinstance(d, datetime.date):
        return d
    try:
        return datetime.date.fromisoformat(str(d)[:10])
    except ValueError:
        return None


def _backs(s, dim, type_map):
    """scorecard.ts dimRefs for one source: a present `dims` key decides alone
    (an empty list backs nothing — the JS early return); otherwise the type map."""
    dims = s.get("dims")
    if dims is not None:
        return dim in [d for d in dims if isinstance(d, str)]
    return s.get("type") in type_map


def check_scoring_v2(doc, sources, text=""):
    """-> [(code, message)] under the 2026-09-19 money and urgency ladders.
    `text` is the rendered body plus the first moves."""
    out = []
    n_links = len(re.findall(r"\[Competition\]\(#competition\)", text))
    if n_links:
        out.append(("MARKET_GAP_LINK",
                    f"{n_links} link(s) read [Competition](#competition) — the section is "
                    f"named Market gap since 2026-09-19; write [Market gap](#competition)"))
    scores = doc.get("scores") or {}
    urgency, money = scores.get("urgency"), scores.get("money")

    if isinstance(urgency, int) and urgency >= 1:
        if not any(s.get("type") == "regulation" and _backs(s, "urgency", ("regulation",))
                   for s in sources):
            out.append(("URGENCY_NO_INSTRUMENT",
                        f"urgency {urgency} with no `regulation` source backing it — Why now "
                        f"scores a dated instrument only; the freshness point is retired "
                        f"(SCORING.md URGENCY). Cite the law or lower urgency to 0"))
        if urgency >= 2 and doc.get("draft_law"):
            out.append(("URGENCY_DRAFT",
                        f"urgency {urgency} on a record carrying `draft_law:` — a bill is not "
                        f"enacted, so it fails REAL and stops at rung 1 (SCORING.md URGENCY)"))

    if isinstance(money, int) and money >= 1:
        tagged = [s for s in sources if s.get("type") == "price" and _backs(s, "money", ())]
        if not tagged:
            public = sum(1 for s in sources
                         if s.get("type") != "price" and _backs(s, "money", MONEY_PUBLIC_TYPES))
            what = (f"the {public} money source(s) on file are public money nearby, which "
                    f"never earns a point on its own" if public else "nothing on file backs money")
            out.append(("MONEY_NO_RECEIPT",
                        f"money {money} with no `type: price` receipt tagged `dims: [money]` — "
                        f"{what}. Willing to pay is read from price receipts only "
                        f"(SCORING.md MONEY); tag the receipt, restate a contract or awarded "
                        f"tender for this job as one, or lower money to 0"))
        elif money >= 2:
            updated = _iso(doc.get("updated"))
            paid = [s for s in tagged if s.get("basis") in MONEY_PAID_BASES
                    and updated and _iso(s.get("date"))
                    and 0 <= (updated - _iso(s.get("date"))).days <= MONEY_PAID_WINDOW_DAYS]
            # The lift is PUBLIC MONEY: a tender, contract or subsidy backing
            # money. A statistic or a news item tagged money is not a programme.
            lift = any(s.get("type") in MONEY_PUBLIC_TYPES and _backs(s, "money", MONEY_PUBLIC_TYPES)
                       for s in sources)
            if not paid and not lift:
                out.append(("MONEY_NOT_PAID",
                            f"money 2 needs a PAID receipt (a money-tagged price at basis "
                            f"{' or '.join(MONEY_PAID_BASES)}, dated within 24 months of "
                            f"`updated`) or the public-money lift on top of a price; neither is "
                            f"on file, so the evidence supports rung 1 (SCORING.md MONEY)"))
    return out


def check_scoring_v2_mirror():
    """The page's switch (web/lib/scoring-v2.ts) must list exactly SCORING_V2_ENFORCED.

    ONE LIST IN TWO LANGUAGES IS TWO LISTS, and the failure is silent: a record
    rescored here but missing there renders its new scores with the retired
    ladder's words, or the reverse. So the drift is an ERROR, not a warning."""
    try:
        src = open(SCORING_V2_MIRROR, encoding="utf-8").read()
    except OSError:
        return [f"{os.path.relpath(SCORING_V2_MIRROR, ROOT)} is missing — the page's copy of "
                f"SCORING_V2_ENFORCED lives there"]
    m = re.search(r"SCORING_V2[^=]*=\s*new Set(?:<[^>]*>)?\(\[(.*?)\]\)", src, re.S)
    if not m:
        return [f"{os.path.relpath(SCORING_V2_MIRROR, ROOT)} has no `SCORING_V2 = new Set([...])` "
                f"this checker can read"]
    web = set(re.findall(r"p-\d{4}", re.sub(r"//[^\n]*", "", m.group(1))))
    if web == set(SCORING_V2_ENFORCED):
        return []
    return [f"SCORING_V2 in web/lib/scoring-v2.ts and SCORING_V2_ENFORCED here disagree — "
            f"only here: {', '.join(sorted(set(SCORING_V2_ENFORCED) - web)) or 'none'}; only "
            f"there: {', '.join(sorted(web - set(SCORING_V2_ENFORCED))) or 'none'}. A rescored "
            f"record joins both in the same change (SCORING.md, THE SWITCH)"]


def split_record(text):
    """→ (frontmatter, argument, firstmoves, revisions)."""
    parts = text.split("---\n")
    fm = parts[1] if len(parts) > 2 else ""
    body = "---\n".join(parts[2:]) if len(parts) > 2 else text
    rev = ""
    m = re.search(r"^##\s*Revisions\s*$", body, re.M)
    if m:
        rev, body = body[m.end():], body[: m.start()]
    fmv = ""
    m2 = re.search(r"^##\s*First moves\s*$", body, re.M)
    if m2:
        fmv, body = body[m2.end():], body[: m2.start()]
    return fm, body.strip(), fmv, rev


def frontmatter(fm_text, path):
    """The frontmatter as data. A record this cannot parse is a build failure —
    the site's own loader would reject it too, so there is nothing to lint."""
    import yaml  # noqa: PLC0415 — past ensure_yaml()
    try:
        doc = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:  # noqa: PERF203
        raise SystemExit(f"check-records: {os.path.basename(path)}: unparseable "
                         f"frontmatter — {e}") from e
    return doc if isinstance(doc, dict) else {}


def check(path, year):
    text = open(path, encoding="utf-8").read()
    fm, arg, firstmoves, revisions = split_record(text)
    pid = os.path.basename(path)[:6]
    errors, warns = [], []

    # values the cross-field invariants below are asserted against
    doc = frontmatter(fm, path)
    scores = {k: v for k, v in (doc.get("scores") or {}).items() if isinstance(v, int)}
    comps = [c for c in (doc.get("comps") or []) if isinstance(c, dict)]
    raw_locals = doc.get("locals")
    locals_ = [l for l in (raw_locals or []) if isinstance(l, dict)]
    sources = [s for s in (doc.get("sources") or []) if isinstance(s, dict)]
    gapchecks = [s for s in sources if s.get("type") == "gap-check"]
    status = str(doc.get("status") or "")
    live = status != "rejected"

    # ---- STRUCTURE: the silent-failure class this file exists for ----------
    # Rejected records are EXEMPT, for the same reason the cross-field
    # invariants below exempt them: they are never rendered, so a missing
    # lead-in cannot produce the empty-section failure this check exists to
    # catch. Before this exemption, 8 of the checker's 11 errors were rejected
    # records — noise that makes a real error invisible and trains everyone to
    # skip the output. A check that cries wolf gets ignored.
    if status != "rejected":
        for lead in LEAD_INS:
            if lead not in arg:
                errors.append(f"missing lead-in '{lead}' — its section renders empty "
                              f"or the text falls into the section above")

    # A near-miss lead-in is worse than a missing one: it looks written.
    for near in re.findall(r"^(Why it'?s urgent|Why this now|Who buys|Who pays for|"
                           r"Existing solutions|Already solved|Solved abroad)[:,]",
                           arg, re.M | re.I):
        errors.append(f"lead-in lookalike '{near}:' — sections.ts matches literally")

    # ---- score arithmetic (the page prints the sum) ------------------------
    total = doc.get("score")
    if len(scores) == 5 and isinstance(total, int):
        s = sum(scores.values())
        if s != total:
            errors.append(f"score {total} != sum of dimensions {s}")

    # ---- the likely solution (owner, 2026-09-10) ---------------------------
    # "Make sure everyone has one" — REQUIRED on every record, rejected ones
    # included, because it answers "what would likely solve this?", which every
    # record can answer; whether that answer is still open to an entrant is the
    # gap score's question, never this field's (one field, one meaning). And
    # "don't try to make it like we know everything": the page always labels it
    # "Likely solution", so the sentence may not claim certainty the label
    # disowns. The word list was run over all 37 sentences when it was written
    # and matched none — it catches drift, it does not police existing prose.
    if "fix" in doc:
        errors.append("`fix:` was renamed `solution:` on 2026-09-10 — rename the key")
    solution = doc.get("solution")
    if not isinstance(solution, str) or not solution.strip():
        errors.append("no `solution:` — one plain sentence stating the likely solution is "
                      "required on every record (RECORD-TEMPLATE.md)")
    else:
        for claim in OVERCLAIM.findall(solution):
            errors.append(f"`solution:` claims certainty ('{claim}') — it is always shown as "
                          f"the LIKELY solution; describe the product, not the outcome")

    # ---- difficulty to enter (owner, 2026-09-15) ---------------------------
    # Required on every record, rejected ones included, and asserted rather
    # than trusted: two of its seven keys are DERIVED — `incumbents` from the
    # locals[] ledger, `level` from the five gate weights — and a derived value
    # written by hand drifts from its source the first time the ledger moves.
    errors.extend(check_entry(doc, locals_))

    # ---- the process figure (owner, 2026-09-15) ---------------------------
    # OPTIONAL — drawn only where the problem is a workflow someone performs
    # today. Asserted rather than trusted for the reason every figure on this
    # site is: a diagram reads as settled fact whatever the prose beside it
    # says, so the one thing it may never do is look certain about a step
    # nobody checked. `known` is where that uncertainty lives, and these are
    # the rules that stop it collapsing back into confidence.
    errors.extend(check_process(doc, len(sources), comps, locals_))
    for msg in check_process_phrases(doc):
        (errors if pid in PROCESS_PHRASE_ENFORCED else warns).append(msg)

    # ---- the headline block (owner, 2026-09-16) ---------------------------
    # OPTIONAL `brief:` (at most two sentences) and `good_for:` line. The brief
    # is the only part of the headline that asserts facts, so it is held to
    # receipts; the good_for line describes a person and is held to carrying
    # none. Where a brief is drawn, `solution:` opens with "Build" and the
    # title writes its numbers in digits.
    errors.extend(check_headline(doc, len(sources), comps, locals_))

    # ---- the draft-law badge (owner, 2026-09-16) --------------------------
    # OPTIONAL `draft_law:` — present only where the main pain depends on a
    # law not yet passed. The line is a status claim, so it is held to a
    # resolving marker on a `regulation` source, a word cap and OVERCLAIM.
    errors.extend(check_draft_law(doc, sources))

    # ---- body v2: the writing rules (owner, 2026-09-16/17) -----------------
    # ERRORs on a BODY_V2_ENFORCED record (a rewritten one); on every other live
    # record ONE summary warning, its rewrite worklist, so 28 unrewritten
    # records do not bury everything else this file prints. Rejected records
    # never render and are exempt.
    if live:
        v2 = check_body_v2(doc, arg, firstmoves, sources, comps, locals_)
        waived = BODY_V2_WAIVERS.get(pid, frozenset())
        if pid in BODY_V2_ENFORCED:
            for code, gate, msg in v2:
                if gate and code not in waived:
                    errors.append(f"[body-v2 {code}] {msg}")
                else:
                    tag = "waived, reported debt" if gate else "advice"
                    warns.append(f"[body-v2 {code}, {tag}] {msg}")
        elif v2 and BODY_V2_DETAIL:
            warns.extend(f"[body-v2 {code}{'' if gate else ', advice'}] {msg}"
                         for code, gate, msg in v2)
        elif v2:
            counts = {}
            for code, _gate, _msg in v2:
                counts[code] = counts.get(code, 0) + 1
            warns.append(f"body v2: not rewritten yet ({sum(counts.values())} findings: "
                         f"{', '.join(f'{c} {n}' for c, n in sorted(counts.items()))}) — "
                         f"pipeline/REWRITE.md; `--body-v2` lists them")

    # ---- scoring v2: the money and urgency ladders (owner, 2026-09-19) ------
    # ERRORs on a SCORING_V2_ENFORCED record (a rescored one). Every other live
    # record is counted into ONE summary line printed at the end, and listed in
    # full by `--scoring-v2`. Rejected records never render and are exempt.
    if live:
        sv2 = check_scoring_v2(doc, sources, arg + "\n" + firstmoves)
        if pid in SCORING_V2_ENFORCED:
            errors.extend(f"[scoring-v2 {code}] {msg}" for code, msg in sv2)
        elif sv2:
            SCORING_V2_PENDING[pid] = [code for code, _msg in sv2]
            if SCORING_V2_DETAIL:
                warns.extend(f"[scoring-v2 {code}, not rescored yet] {msg}" for code, msg in sv2)

    # ---- citation integrity ------------------------------------------------
    n_sources = len(sources)
    for n in {int(x) for x in re.findall(r"\[S(\d+)", arg + firstmoves)}:
        if n > n_sources:
            errors.append(f"[S{n}] does not resolve — {n_sources} sources on file")

    # ---- public-prose hygiene ---------------------------------------------
    low = arg.lower()
    for j in JARGON:
        if j.lower() in low:
            warns.append(f"process jargon in rendered prose: '{j}'")
    for v in VERDICTS:
        if re.search(r"\b" + v + r"\b", arg):
            warns.append(f"retired verdict label in rendered prose: '{v}'")
    for r in SELF_REF:
        if r.lower() in low:
            warns.append(f"register self-reference in rendered prose: '{r}'")

    # THE GLOSS LAW (CONVENTIONS.md): first use of an ALL-CAPS trade term
    # carries a plain-language appositive. WARNING-ONLY, permanently — the
    # corpus predates the law and these warnings are its retrofit worklist.
    # Rejected records are exempt: their prose never renders, so an ungloss'd
    # term on one can confuse nobody (the same flood lesson as above).
    if live:
        for tok in ungloss_terms(arg + "\n" + firstmoves):
            warns.append(f"ungloss'd trade term '{tok}' — first use carries no "
                         f"em-dash or parenthetical gloss in its sentence; add a "
                         f"plain-language appositive or allowlist it "
                         f"(CONVENTIONS.md, the gloss law)")

    # THE LEDGER NOTES ARE RENDERED PROSE TOO, and until now nothing read them.
    # `comps[].traction` and `locals[].evidence` print under every entry on the
    # record page; being frontmatter rather than body is a fact about our
    # storage, not about who sees them.
    #
    # ONE WARNING PER RECORD, NOT ONE PER ENTRY. The offence is uniform — the
    # same filename pasted into every ledger note — so thirty separate lines
    # would bury the record's other findings under one repeated sentence, and a
    # checker that floods is a checker nobody reads (the same lesson the
    # rejected-record exemption above was written for).
    if live:
        hits, paths = [], set()
        for label, items, key in (("comps", comps, "traction"),
                                  ("locals", locals_, "evidence")):
            for i, item in enumerate(items, 1):
                found = LEDGER_PATHS.findall(str(item.get(key) or ""))
                if found:
                    hits.append(f"{label}[{i}] {item.get('name')}")
                    paths.update(found)
        if hits:
            more = f" (+{len(hits) - 3} more)" if len(hits) > 3 else ""
            warns.append(
                f"{len(hits)} rendered ledger note(s) print a repo path to the reader "
                f"({', '.join(sorted(paths)[:3])}): {'; '.join(hits[:3])}{more} — these "
                f"lines render under the entry on the record page; say what was checked in "
                f"words a builder can act on, not where we keep it")

    # ---- CROSS-FIELD INVARIANTS -------------------------------------------
    # The class of defect that shipped twice and was caught by a reader, not by
    # us: a SCORE that contradicts the record's own EVIDENCE. Prose review does
    # not catch these — both halves read fine alone — so they are asserted, and
    # since 2026-08-25 they are asserted INSIDE `npm run build`.
    #
    # Rejected records are exempt throughout: they never render, so a
    # contradiction on one can mislead nobody.

    # -- the locals[] ledger itself ----------------------------------------
    if live and raw_locals is not None and not locals_:
        errors.append("locals is present but empty — omit the key. problem_locals is a "
                      "child table and cannot tell `locals: []` from an absent key, so "
                      "the two loaders would disagree about this record")
    # TWO ORTHOGONAL FIELDS, COUNTED SEPARATELY. `direct_established` is the
    # only list `gap: 0` may rest on; `direct` is what rungs 1 and 2 turn on;
    # `adjacent` is recorded, rendered, and moves NOTHING. Keeping three lists
    # rather than one is the whole fix — the single `established_locals` list
    # this replaces is what made an adjacent firm indistinguishable from a
    # competitor once it had been written down.
    direct_established, direct, adjacent = [], [], []
    unreadable_locals = 0   # entries this pass could not classify (see below)
    for i, l in enumerate(locals_ if live else (), 1):
        who = l.get("name") or f"locals[{i}]"
        retired = [k for k in LOCAL_RETIRED_KEYS if k in l]
        if retired:
            unreadable_locals += 1
            errors.append(
                f"locals[{i}] '{who}' still carries the RETIRED key "
                f"{', '.join(retired)} — `status` was split into `competes: "
                f"direct|adjacent` (does it sell THIS record's product to THIS "
                f"record's buyer?) plus `maturity: established|early` (the established "
                f"test, unchanged). One field cannot answer both, which is why a mature "
                f"ADJACENT firm had no honest spelling. data/RECORD-TEMPLATE.md")
            continue
        ico = l.get("ico")
        if ico is not None and not (isinstance(ico, str) and re.fullmatch(r"\d{8}", ico)):
            errors.append(f"locals[{i}] '{who}' has ico {ico!r} — an IČO is 8 digits as a "
                          f"QUOTED string; unquoted YAML eats a leading zero")
            ico = None
        # One identifier at least. `url` went optional under the no-exclude
        # ruling — a real player with no product page is linked to its ARES
        # record instead of being dropped or given an invented URL — but a row
        # with neither links nowhere, and a ledger row a reader cannot follow is
        # an assertion, not evidence.
        if not l.get("url") and not l.get("ico"):
            errors.append(f"locals[{i}] '{who}' has neither url nor ico — one is required. "
                          f"With only an IČO the page links the ARES record "
                          f"(ares.gov.cz/ekonomicke-subjekty?ico=…); never invent a URL")
        if l.get("competes") not in LOCAL_COMPETES:
            unreadable_locals += 1
            errors.append(f"locals[{i}] '{who}' has competes {l.get('competes')!r} — the "
                          f"enum is {' | '.join(LOCAL_COMPETES)}. `direct` sells THIS "
                          f"record's product to THIS record's buyer; `adjacent` is a real "
                          f"player nearby that sells something else. It is the only field "
                          f"gap reads for eligibility")
            continue
        if l.get("maturity") not in LOCAL_MATURITIES:
            errors.append(f"locals[{i}] '{who}' has maturity {l.get('maturity')!r} — the "
                          f"enum is {' | '.join(LOCAL_MATURITIES)} (SCORING.md, the "
                          f"established test). It sets the RUNG; competes decides whether "
                          f"the row counts at all")
            continue
        since = l.get("since") if isinstance(l.get("since"), int) else None
        ok, limbs, blockers = established(since, str(l.get("evidence") or ""), year,
                                          ico if isinstance(ico, str) else None)
        if l["maturity"] == "established":
            # THE TEST IS APPLIED, NOT TRUSTED. `maturity` is a claim; these are
            # its receipts, and the whole point of structuring locals[] was that
            # a machine could ask for them. It is asked of ADJACENT players too:
            # the claim "this firm is established" is the same claim whichever
            # side of the counter it sells on, and an unreceipted one is the
            # same defect.
            if not ok:
                errors.append(f"locals[{i}] '{who}' is marked established but fails the "
                              f"established test: {'; '.join(blockers)}. SCORING.md: "
                              f">= {MIN_YEARS_SELLING} years selling AND one of — named "
                              f"customers or a public customer count · >= 2 distinct "
                              f"public buyers in cz-contract-parties.jsonl · Series A or "
                              f"later · a state certification, attest or framework listing")
        elif ok:
            # NO LONGER A CLAIM ABOUT GAP. Before the split, "early but passes
            # the test" meant "the space may be taken"; now it means only "this
            # maturity looks wrong", and whether that touches gap depends on
            # `competes`. Saying so keeps the warning from teaching the reader
            # to re-label an adjacent firm to protect a score — the exact
            # workaround the split exists to remove.
            tail = ("— if that is right, and it really sells this, the space is taken "
                    "and gap is 0" if l["competes"] == "direct"
                    else "— it is adjacent, so gap is unaffected either way; fix the "
                         "maturity, not the score")
            warns.append(f"locals[{i}] '{who}' is marked early but PASSES the established "
                         f"test ({'; '.join(limbs)}) {tail}")
        if l["competes"] == "direct":
            direct.append(l)
            if l["maturity"] == "established":
                direct_established.append(l)
        else:
            adjacent.append(l)
            # AN ADJACENT ENTRY EARNS ITS PLACE WITH ONE SENTENCE: what it
            # actually sells, and why that is not this. Without it the row reads
            # as a competitor the record failed to score against — which is
            # worse than the exclusion the no-exclude rule replaced. A regex
            # cannot judge the sentence, so this is advisory and says so.
            ev = str(l.get("evidence") or "")
            if not re.search(r"(?i)\b(sell\w*|sold|offer\w*|provid\w*|suppl\w*|serv\w*|"
                             r"build\w*|run\w*|prodáv\w*|nabíz\w*|dodáv\w*|posky\w*)\b", ev):
                warns.append(f"locals[{i}] '{who}' is adjacent but its evidence never says "
                             f"what it DOES sell — an adjacent entry is market intelligence "
                             f"only if the line states the product and why it is not this")
        # A claimed buyer count the lookup does not support is a receipt that
        # does not exist. Advisory: the lookup covers registr smluv only.
        claim = _CLAIMED_BUYERS.search(str(l.get("evidence") or ""))
        if claim and isinstance(ico, str):
            n = len(buyers_by_ico().get(ico, ()))
            if int(claim.group(1)) > n:
                warns.append(f"locals[{i}] '{who}' evidence claims {claim.group(1)} public "
                             f"buyers; cz-contract-parties.jsonl carries {n} for IČO {ico}")

    # -- PROOF vs the comps ledger, on the NEW ladder ----------------------
    # Replaces the v1 "proof 0 + a comp records a raise" invariant, which tested
    # EXISTENCE and therefore could not discriminate. The rungs now read: 0 no
    # foreign solution on file · 1 EARLY foreign players only · 2+ at least one
    # ESTABLISHED foreign player. Each rung contradicts its ledger differently,
    # so at most one of these fires and it names which rung is wrong.
    proof = scores.get("proof")
    if live and isinstance(proof, int):
        est_comps = []
        for c in comps:
            since = c.get("since") if isinstance(c.get("since"), int) else None
            ok, limbs, _ = established(since, str(c.get("traction") or ""), year)
            if ok:
                est_comps.append((c.get("name") or "?", limbs))
        if proof == 0 and comps:
            errors.append(f"proof 0 means no foreign solution on file, but comps names "
                          f"{len(comps)} — raise proof or empty the ledger")
        elif proof == 1 and est_comps:
            named = ", ".join(n for n, _ in est_comps[:3])
            errors.append(f"proof 1 means EARLY foreign players only, but {named} "
                          f"pass{'' if len(est_comps) > 1 else 'es'} the established test "
                          f"({'; '.join(est_comps[0][1])}) — rung 2 starts at one "
                          f"established player")
        elif proof >= 2 and comps and not est_comps:
            errors.append(f"proof {proof} needs an ESTABLISHED foreign player, but none of "
                          f"the {len(comps)} comp(s) passes the established test — the "
                          f"ladder puts early-only players at 1")

    # -- ASK: a direct ask cites DEMAND and nothing else (MATCH.md §11) -------
    # An `ask` source is a signal from the `asks` ledger: an owner stating a
    # problem before money is attached. A prize is not a budget and a research
    # need's budget arrives with the later tender, so the rule is "never money";
    # TYPE_TO_DIM already routes an untagged ask to demand, and this is the
    # check behind the prose for the tagged case (CLAUDE.md rule 2).
    if live:
        for s in sources:
            if s.get("type") != "ask":
                continue
            dims = [d for d in (s.get("dims") or []) if isinstance(d, str)]
            bad = sorted(set(dims) & {"money", "proof", "gap", "urgency"})
            if bad:
                errors.append(f"ask source {s.get('signal') or s.get('url')} cites "
                              f"{', '.join(bad)} — a direct ask cites demand only "
                              f"(MATCH.md §11); drop the tag or change the type")
            if not s.get("signal"):
                errors.append(f"ask source {s.get('url')} has no `signal:` — an ask is "
                              f"a ledger record, cite its asks id")

    # -- PRICE: the receipt for "who pays and how much" (owner, 2026-09-03) --
    # MONEY is "is public budget nearby?" — a tender, a grant, a recurring line
    # near the problem — and never asks whose pocket the money leaves or
    # whether it buys this. A `type: price` source is the field that does. It
    # is a receipt only when it names who pays, how much, per what and on what
    # basis, dated, so a price source missing any of them FAILS the build; the
    # same fields on any other type render nothing and fail too (one field,
    # one meaning — CLAUDE.md rule 1). It cites money only when tagged
    # `dims: [money]` and never another dimension: a price is not proof, is
    # not demand, and says nothing about gap (MATCH.md §9). Rejected records
    # are NOT exempt here — zod in web/lib/data.ts refuses a malformed price
    # source on every record, so this reports what the build will fail on.
    prices = [s for s in sources if s.get("type") == "price"]
    for i, s in enumerate(sources, 1):
        where = f"sources[{i}] ({s.get('url') or s.get('signal') or '?'})"
        if s.get("type") == "price":
            # `url` IS PART OF THE RECEIPT, and it is checked here because the
            # two validators disagreed on 2026-09-04: this file accepted 17
            # price sources that carried no url, `scripts/db.py rebuild`
            # refused the first one, and only `npm run build` runs both — the
            # exact split CONVENTIONS.md warns about. A price with no url is a
            # number nobody can check, which is the one thing this register
            # does not publish.
            missing = [k for k in ("url",) + PRICE_FIELDS
                       if s.get(k) is None or s.get(k) == ""]
            if missing:
                errors.append(f"price source {where} is missing {', '.join(missing)} — a "
                              f"price receipt names who pays, how much, per what and on "
                              f"what basis, dated, or it is not a receipt")
            amt = s.get("amount_czk")
            if amt is not None and (isinstance(amt, bool)
                                    or not isinstance(amt, (int, float)) or amt < 0):
                errors.append(f"price source {where} amount_czk is {amt!r} — an unquoted, "
                              f"non-negative number of crowns (0 is a real receipt where "
                              f"a free incumbent sets the price)")
            unit = s.get("unit")
            if unit is not None and unit not in PRICE_UNITS:
                errors.append(f"price source {where} unit {unit!r} — one of "
                              f"{', '.join(PRICE_UNITS)}")
            basis = s.get("basis")
            if basis is not None and basis not in PRICE_BASES:
                errors.append(f"price source {where} basis {basis!r} — one of "
                              f"{', '.join(PRICE_BASES)}")
            d = s.get("date")
            ds = d.isoformat() if hasattr(d, "isoformat") else d
            if d is not None and (not isinstance(ds, str)
                                  or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", ds)):
                errors.append(f"price source {where} date {d!r} — an ISO YYYY-MM-DD string")
            dims = [x for x in (s.get("dims") or []) if isinstance(x, str)]
            bad = sorted(set(dims) - {"money"})
            if bad:
                errors.append(f"price source {where} cites {', '.join(bad)} — a price "
                              f"receipt may carry dims: [money] only (MATCH.md §9)")
        else:
            stray = [k for k in PRICE_FIELDS[:-1] if k in s]
            if stray:
                errors.append(f"{s.get('type')} source {where} carries {', '.join(stray)} — "
                              f"price fields render only on a type: price source; change "
                              f"the type to price or drop them")
    # WARNING-ONLY, permanently: the corpus predates the field, and these lines
    # are its retrofit worklist, exactly as the gloss law's are. The page prints
    # the house line in place of the ledger, which is honest.
    hint = doc.get("price_search")
    if hint is not None and not (isinstance(hint, str) and hint.strip()):
        errors.append("price_search is present but empty — it is one sentence naming WHERE "
                      "to look, or the key is absent")
    # AN ESTIMATE OF WHERE, NEVER OF HOW MUCH (owner, 2026-09-04). A number in
    # the hint is a price with no receipt, printed beside the line that says
    # no receipt exists — the exact contradiction this file exists to catch.
    # Years and act numbers pass; a crown figure (digits followed by CZK/Kč, or
    # a thousands-grouped amount) does not.
    if isinstance(hint, str) and re.search(
            r"\d[\d\s.,]*\s?(?:CZK|Kč|EUR|€)|\b\d{1,3}(?:[ .]\d{3}){1,}\b", hint):
        errors.append(f"price_search carries an amount — it names WHERE to look, never how "
                      f"much; a figure belongs on a type: price source with a url, or nowhere")
    if live and isinstance(total, int) and total >= PRICE_EXPECTED_FROM and not prices and not hint:
        warns.append(f"score {total} with no type: price source and no price_search — the "
                     f"page prints 'No price paid by a Czech buyer is on file yet.'; add a `type: price` "
                     f"receipt, or say WHERE to look in `price_search:` (CONVENTIONS.md, "
                     f"price receipts)")

    # -- GAP: keyed on BOTH fields, and the check is a receipt, never a score --
    # v1 rung 0 literally meant "check not done", so a de-ranked record and an
    # unchecked one rendered the same verdict above a printed list of
    # competitors. Rung 0 now means TAKEN and only TAKEN; the missing check is
    # caught HERE and fails the build instead of being expressed as a number.
    #
    # SINCE 2026-08-25 EVERY RUNG READS `competes` FIRST. The ladder is:
    #   0 TAKEN      >= 1 local with competes: direct AND maturity: established
    #   1 CONTESTED  locals sell this (direct) but all are early
    #   2 OPEN       checked, and NO local sells this
    # An ADJACENT player never moves this score, at any maturity — that is the
    # entire point of the split, and it is why rung 2 no longer contradicts a
    # populated ledger. Before the split, recording a mature-but-adjacent firm
    # forced gap to 0, so the only ways to stay honest were to mislabel it
    # `early` or to leave it out. Both shipped. Neither is needed now.
    gap = scores.get("gap")
    if live and isinstance(gap, int):
        if gap == 0 and not direct_established:
            near = ("; the ledger's established entries are all `competes: adjacent`, "
                    "and an adjacent player never takes the space"
                    if any(l["maturity"] == "established" for l in adjacent) else "")
            errors.append(f"gap 0 means TAKEN — it requires at least one locals[] entry "
                          f"with competes: direct AND maturity: established, naming the "
                          f"player that closed the space{near}. 'not checked' is not a "
                          f"score on this ladder")
        if not gapchecks:
            errors.append(f"gap {gap} with NO gap-check source — every gap score is a "
                          f"claim about the local field and needs the check that backs it")
        elif not any(s.get("queries") for s in gapchecks):
            errors.append(f"gap {gap} but no gap-check source records queries[] — a bare "
                          f"negative is worth what its coverage is worth (CONVENTIONS.md, "
                          f"'Proving a negative')")
        if gap >= 1 and direct_established:
            named = ", ".join(str(l.get("name")) for l in direct_established[:3])
            errors.append(f"gap {gap} but locals[] names an ESTABLISHED player that SELLS "
                          f"THIS ({named}) — competes: direct + maturity: established is "
                          f"rung 0, TAKEN")
        elif gap == 2 and direct:
            named = ", ".join(str(l.get("name")) for l in direct[:3])
            errors.append(f"gap 2 means checked and NO local sells this, but locals[] names "
                          f"{len(direct)} at competes: direct ({named}) — an early player "
                          f"that sells this is rung 1, CONTESTED, not rung 2")
        # Rung 1 with nothing at `competes: direct` is an UNDERSTATEMENT, not a
        # contradiction, so it warns and never fails: gap authority is
        # asymmetric (SCORING.md) — finding nobody never raises the score on its
        # own, only a check with queries[] and a passing positive control does.
        # It is worth saying out loud because the commonest way to arrive here is
        # converting a record's adjacent players and forgetting the score moved
        # with them.
        if gap == 1 and not direct and not unreadable_locals:
            # …and only when every entry was READABLE. During the schema-7
            # migration a record whose locals still carry `status` classifies as
            # neither direct nor adjacent, and warning "the ledger is empty"
            # above a ledger of five names is the checker crying wolf — which is
            # how a warning stops being a warning (see the rejected-record
            # exemption above, same lesson).
            what = (f"{len(adjacent)} adjacent player(s) are on file, and adjacent never "
                    f"moves gap" if adjacent else "the ledger is empty")
            warns.append(f"gap 1 means locals sell this but are all early — no locals[] "
                         f"entry has competes: direct ({what}). If the check really found "
                         f"nobody selling this, rung 2 is the honest score, but only on a "
                         f"gap-check with a passing positive control")

    # Not on a body-v2 record: its page shows an answer line and three items a
    # section, and the owner's rule is "Dont remove content" — the detail's
    # length lives in the Read more sheet, where it is meant to be.
    words = len(re.sub(r"\[S[\d,S]+\]", "", arg).split())
    if words > ARG_WORDS_MAX and pid not in BODY_V2_ENFORCED:
        warns.append(f"argument {words} words (target ≤{ARG_WORDS_MAX})")

    # citation clot — the measured difference between p-0010 and p-0008
    for sent in re.split(r"(?<=[.!?])\s+", arg):
        n = len(re.findall(r"\[S[\d,S]+\]", sent))
        if n > MARKERS_PER_SENTENCE:
            warns.append(f"{n} citation markers in one sentence: "
                         f"\"{sent.strip()[:60]}…\"")

    # ---- public source fields ---------------------------------------------
    missing = sum(1 for s in sources if not s.get("name"))
    if missing > 0:
        warns.append(f"{missing} of {n_sources} sources lack a public name:/why: "
                     f"(falls back to the signal summary)")

    return pid, errors, warns


def register_year(files):
    """The register's own newest `updated`, as a year — the clock the established
    test runs against.

    NEVER `datetime.now()`. `web/lib/data.ts` extractDate() already fixes the
    site's notion of "now" to this same value so a commit renders identically on
    any day it is built; a build GATE that drifted with the wall clock would be
    strictly worse — the same tree would pass today and fail in January, with no
    commit in between to blame.
    """
    newest = ""
    for path in files:
        with open(path, encoding="utf-8") as fh:
            for m in re.finditer(r"^updated: '?(\d{4}-\d{2}-\d{2})", fh.read(), re.M):
                newest = max(newest, m.group(1))
    return int(newest[:4]) if newest else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any ERROR is found — this is the build gate")
    ap.add_argument("--body-v2", action="store_true",
                    help="list every body-v2 finding on records not yet rewritten "
                         "(default: one summary line each)")
    ap.add_argument("--enforce", metavar="IDS",
                    help="treat these record ids (comma-separated) as BODY_V2_ENFORCED for "
                         "this run only — how a rewrite agent proves its record passes "
                         "without editing this shared file (pipeline/REWRITE.md)")
    ap.add_argument("--scoring-v2", action="store_true",
                    help="list every scoring-v2 finding on records not yet rescored "
                         "(default: one summary line for the register)")
    ap.add_argument("--enforce-scoring", metavar="IDS",
                    help="treat these record ids (comma-separated) as SCORING_V2_ENFORCED for "
                         "this run only — how a rescoring agent proves its record passes "
                         "before it joins the set (docs/scoring-v2/rescore-2026-09-19.md)")
    args = ap.parse_args()
    global BODY_V2_DETAIL, BODY_V2_ENFORCED, SCORING_V2_DETAIL, SCORING_V2_ENFORCED
    BODY_V2_DETAIL = args.body_v2
    if args.enforce:
        BODY_V2_ENFORCED = BODY_V2_ENFORCED | {x.strip() for x in args.enforce.split(",") if x.strip()}
    ensure_yaml(sys.argv[1:])

    # The mirror is compared BEFORE --enforce-scoring widens the set: a trial
    # run is not a change to either list.
    mirror_errors = check_scoring_v2_mirror()
    SCORING_V2_DETAIL = args.scoring_v2
    if args.enforce_scoring:
        SCORING_V2_ENFORCED = SCORING_V2_ENFORCED | {
            x.strip() for x in args.enforce_scoring.split(",") if x.strip()}

    files = sorted(glob.glob(RECORDS))
    year = register_year(files)
    n_err = n_warn = clean = 0
    if mirror_errors:
        print("\nscoring-v2 switch")
        for e in mirror_errors:
            print(f"  ERROR  {e}")
        n_err += len(mirror_errors)
    for path in files:
        pid, errors, warns = check(path, year)
        if not errors and not warns:
            clean += 1
            continue
        print(f"\n{pid}")
        for e in errors:
            print(f"  ERROR  {e}")
        for w in warns:
            print(f"  warn   {w}")
        n_err += len(errors)
        n_warn += len(warns)

    if SCORING_V2_PENDING and not SCORING_V2_DETAIL:
        counts = {}
        for codes in SCORING_V2_PENDING.values():
            for c in codes:
                counts[c] = counts.get(c, 0) + 1
        print(f"\nscoring v2: {len(SCORING_V2_ENFORCED)} record(s) rescored; "
              f"{len(SCORING_V2_PENDING)} not yet rescored would fail "
              f"({', '.join(f'{c} {n}' for c, n in sorted(counts.items()))}) — "
              f"docs/scoring-v2/rescore-2026-09-19.md; `--scoring-v2` lists them")

    print(f"\nrecords: {len(files)} · clean: {clean} · "
          f"errors: {n_err} · warnings: {n_warn}  (established test run against {year})")
    if args.strict and n_err:
        print("FAIL — an ERROR is a record contradicting itself or rendering wrong, "
              "and neither produces a build error on its own. That is why this runs "
              "inside `npm run build`.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
