#!/usr/bin/env python3
"""
scripts/check-records.py — enforce data/RECORD-TEMPLATE.md.

WHY THIS EXISTS. The site is a template: `web/lib/sections.ts` splits a record's
body on LITERAL lead-ins (`Why now:`, `Who pays:`, …) and the page renders those
slices. A record that misspells a lead-in still builds — the paragraph just
falls silently into the previous section and the page renders wrong. There is no
error anywhere. That silence is the whole reason for this file.

It is a LINT, not a gate: it exits 0 unless --strict, because most findings are
editorial (word counts, marker density) and a content pass should see them
without being blocked. The build's own zod validation stays the hard gate.

    python3 scripts/check-records.py            # report
    python3 scripts/check-records.py --strict   # exit 1 on STRUCTURE errors
"""
import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORDS = os.path.join(ROOT, "data", "problems", "cz", "p-*.md")

# The literal lead-ins sections.ts keys on. Keep in sync with web/lib/sections.ts.
LEAD_INS = ["Why now:", "Who pays:", "Existing non-solutions", "Solved elsewhere:"]

# Prose that is about OUR PROCESS, not about the problem. Banned from rendered
# body text; belongs in `## Revisions`, which the page does not render.
JARGON = [
    "de-rank", "gap-check", "gap check", "absence check", "incumbent re-check",
    "re-judgment", "the audit found", "receipted", "materiality",
    "UNPROVEN", "FAINT", "SCATTERED", "LIKELY", "CONFIRMED", "VALIDATED",
]

ARG_WORDS_MAX = 300      # argument prose only (excludes First moves / Revisions)
MARKERS_PER_SENTENCE = 3  # more than this reads as citation clot (the p-0008 lesson)


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


def check(path):
    text = open(path, encoding="utf-8").read()
    fm, arg, firstmoves, revisions = split_record(text)
    pid = os.path.basename(path)[:6]
    errors, warns = [], []

    # ---- STRUCTURE: the silent-failure class this file exists for ----------
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
    sc = dict(re.findall(r"^  (proof|money|urgency|demand|gap): (\d+)", fm, re.M))
    total = re.search(r"^score: (\d+)", fm, re.M)
    if sc and total and len(sc) == 5:
        s = sum(int(v) for v in sc.values())
        if s != int(total.group(1)):
            errors.append(f"score {total.group(1)} != sum of dimensions {s}")

    # ---- citation integrity ------------------------------------------------
    n_sources = len(re.findall(r"^- type:", fm, re.M))
    for n in {int(x) for x in re.findall(r"\[S(\d+)", arg + firstmoves)}:
        if n > n_sources:
            errors.append(f"[S{n}] does not resolve — {n_sources} sources on file")

    # ---- public-prose hygiene ---------------------------------------------
    low = arg.lower()
    for j in JARGON:
        if j.lower() in low:
            warns.append(f"process jargon in rendered prose: '{j}'")

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
    missing = n_sources - len(re.findall(r"^  name:", fm, re.M))
    if missing > 0:
        warns.append(f"{missing} of {n_sources} sources lack a public name:/why: "
                     f"(falls back to the signal summary)")

    return pid, errors, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any STRUCTURE error is found")
    args = ap.parse_args()

    files = sorted(glob.glob(RECORDS))
    n_err = n_warn = clean = 0
    for path in files:
        pid, errors, warns = check(path)
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
          f"structure errors: {n_err} · warnings: {n_warn}")
    if args.strict and n_err:
        print("FAIL — a structure error means a section renders wrong with no build error.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
