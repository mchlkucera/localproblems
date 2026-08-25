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
# INSIDE list items — `comps[i].traction`, `locals[i].status`,
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

# The register talking about ITSELF. A builder does not care what "this record
# originally judged" or what "would move this record" — that is our bookkeeping
# leaking onto a public page, the same class of tell as the retired verdict
# labels. Facts about the world stay; facts about our filing go to Revisions.
SELF_REF = [
    "this record", "the record's", "in the register because", "this ledger",
    "urgency and rank", "should jump", "would move this", "Honest limits",
]

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

MIN_YEARS_SELLING = 3

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
    established_locals = []
    for i, l in enumerate(locals_ if live else (), 1):
        who = l.get("name") or f"locals[{i}]"
        ico = l.get("ico")
        if ico is not None and not (isinstance(ico, str) and re.fullmatch(r"\d{8}", ico)):
            errors.append(f"locals[{i}] '{who}' has ico {ico!r} — an IČO is 8 digits as a "
                          f"QUOTED string; unquoted YAML eats a leading zero")
            ico = None
        if l.get("status") not in ("established", "early"):
            errors.append(f"locals[{i}] '{who}' has status {l.get('status')!r} — the enum "
                          f"is established | early, and it IS the gap score")
            continue
        since = l.get("since") if isinstance(l.get("since"), int) else None
        ok, limbs, blockers = established(since, str(l.get("evidence") or ""), year,
                                          ico if isinstance(ico, str) else None)
        if l["status"] == "established":
            established_locals.append(l)
            # THE TEST IS APPLIED, NOT TRUSTED. `status` is a claim; these are
            # its receipts, and the whole point of structuring locals[] was that
            # a machine could ask for them.
            if not ok:
                errors.append(f"locals[{i}] '{who}' is marked established but fails the "
                              f"established test: {'; '.join(blockers)}. SCORING.md: "
                              f">= {MIN_YEARS_SELLING} years selling AND one of — named "
                              f"customers or a public customer count · >= 2 distinct "
                              f"public buyers in cz-contract-parties.jsonl · Series A or "
                              f"later · a state certification, attest or framework listing")
        elif ok:
            warns.append(f"locals[{i}] '{who}' is marked early but PASSES the established "
                         f"test ({'; '.join(limbs)}) — if that is right the space is "
                         f"taken and gap is 0")
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

    # -- GAP: the check is a receipt, never a score ------------------------
    # v1 rung 0 literally meant "check not done", so a de-ranked record and an
    # unchecked one rendered the same verdict above a printed list of
    # competitors. Rung 0 now means TAKEN and only TAKEN; the missing check is
    # caught HERE and fails the build instead of being expressed as a number.
    gap = scores.get("gap")
    if live and isinstance(gap, int):
        if gap == 0 and not established_locals:
            errors.append("gap 0 means TAKEN — it requires at least one locals[] entry "
                          "with status: established, naming the player that closed the "
                          "space. 'not checked' is not a score on this ladder")
        if not gapchecks:
            errors.append(f"gap {gap} with NO gap-check source — every gap score is a "
                          f"claim about the local field and needs the check that backs it")
        elif not any(s.get("queries") for s in gapchecks):
            errors.append(f"gap {gap} but no gap-check source records queries[] — a bare "
                          f"negative is worth what its coverage is worth (CONVENTIONS.md, "
                          f"'Proving a negative')")
        if gap >= 1 and established_locals:
            named = ", ".join(str(l.get("name")) for l in established_locals[:3])
            errors.append(f"gap {gap} but locals[] names an ESTABLISHED local player "
                          f"({named}) — an established local player is rung 0, TAKEN")
        elif gap == 2 and locals_:
            errors.append(f"gap 2 means checked and NO local player found, but locals[] "
                          f"names {len(locals_)} — an early local player is rung 1, "
                          f"CONTESTED, not rung 2")

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
