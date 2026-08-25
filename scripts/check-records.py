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

    words = len(re.sub(r"\[S[\d,S]+\]", "", arg).split())
    if words > ARG_WORDS_MAX:
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
    args = ap.parse_args()
    ensure_yaml(sys.argv[1:])

    files = sorted(glob.glob(RECORDS))
    year = register_year(files)
    n_err = n_warn = clean = 0
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
