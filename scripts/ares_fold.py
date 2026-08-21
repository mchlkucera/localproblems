#!/usr/bin/env python3
"""
ares_fold.py — turn raw ARES subject documents into the enrichment payload, and
fold the resolved identities into the MPSV hiring aggregate.

CALLED BY scripts/fetch_ares.sh, which does the transport. This file does the
two things that are not transport: the ARES FIELD ALLOWLIST, and the NAMEABILITY
RULE that decides whether an IČO's registered name may appear on a public ledger
at all.

ARES IS AN ENRICHMENT SOURCE, NOT A FEED (docs/architecture-v3.md §13.5). It
produces zero signals. `ares-lookups-<month>.json` exists so the lookup has a
receipt and a health row like anything else — scripts/normalize.py maps it to the
registry key `ares`, finds no extractor, and stages nothing. That is the intended
outcome, not a gap.

Usage:
  ares_fold.py --work DIR --month YYYY-MM --lookups FILE --aggregate FILE
               --max-records N
Exit codes: 0 ok · 2 a privacy gate refused · 3 bad input.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normalize import collapse  # noqa: E402
from db import valid_ico        # noqa: E402  — ONE mod-11 implementation, not two
from mpsv_reduce import content_violations, key_violations  # noqa: E402

# ==========================================================================
# THE ARES FIELD ALLOWLIST
# ==========================================================================
# ARES returns 17 top-level keys about a subject. Only these are read.
#
# DELIBERATELY ABSENT: `sidlo` beyond the REGION. The registered seat carries
# `nazevUlice`, `cisloDomovni`, `psc` and a pre-formatted `textovaAdresa`, and for
# a sole trader that is a HOME ADDRESS — measured: five IČOs sampled out of the
# July increments whose employer name is a two-word personal name all resolve to
# pravniForma 101, each with a full street address in `sidlo`. The region is the
# analytical unit this register uses (NUTS-3), so the street is cost with no
# benefit. Also absent: `adresaDorucovaci`, `dic`, `financniUrad`,
# `seznamRegistraci`, `dalsiUdaje` (which carries statutory-body personal names).
ARES_ALLOWLIST = ("ico", "obchodniJmeno", "pravniForma", "datumVzniku", "czNace")
ARES_SIDLO_ALLOWLIST = ("kodKraje", "nazevKraje")

# ==========================================================================
# THE NAMEABILITY RULE — an allowlist, so it fails closed
# ==========================================================================
# A record naming an employer publishes that employer's name. For a legal person
# that is a public register fact. For a SOLE TRADER the registered name IS a
# natural person's name, and publishing it on an append-only public ledger is a
# disclosure no licence covers.
#
# The ČSÚ legal-form codelist puts the whole "podnikající fyzická osoba" family
# in 100-110 (101 = fyzická osoba podnikající dle živnostenského zákona, the code
# every sampled sole trader returned). Legal persons start at 111 (veřejná
# obchodní společnost) and run up through the public-body forms in the 300s-900s.
#
# Written as a RANGE THAT MUST BE MATCHED rather than a list of forbidden codes:
# a missing, non-numeric or unrecognised `pravniForma` is NOT nameable. A denylist
# would name every subject whose code MPSV or ARES invents next year.
LEGAL_PERSON_MIN = 111
LEGAL_PERSON_MAX = 999


def die(msg, code=3):
    print(f"ares_fold: {msg}", file=sys.stderr)
    sys.exit(code)


def nameable(pravni_forma):
    try:
        n = int(str(pravni_forma).strip())
    except (TypeError, ValueError):
        return False
    return LEGAL_PERSON_MIN <= n <= LEGAL_PERSON_MAX


def reduce_subject(doc):
    """The allowlisted view of one ARES subject, or None if it is not one."""
    if not isinstance(doc, dict) or not doc.get("ico"):
        return None
    out = {k: doc.get(k) for k in ARES_ALLOWLIST if doc.get(k) not in (None, "", [])}
    if isinstance(out.get("obchodniJmeno"), str):
        out["obchodniJmeno"] = collapse(out["obchodniJmeno"])
    if isinstance(out.get("czNace"), list):
        # The head of the NACE list is the subject's primary activity; the tail
        # is every registered activity and runs to 20+ codes on a large company.
        out["czNace"] = [str(c) for c in out["czNace"][:6]]
    sidlo = doc.get("sidlo") or {}
    region = {k: sidlo.get(k) for k in ARES_SIDLO_ALLOWLIST if sidlo.get(k) not in (None, "")}
    if region:
        out["region"] = region
    out["nameable"] = nameable(out.get("pravniForma"))
    if not out["nameable"]:
        # A NON-NAMEABLE SUBJECT LOSES ITS NAME HERE, not later. The enrichment
        # payload lands in data/raw/, which is gitignored and pruned at 28 days —
        # but that is not the same as absent, and the whole MPSV increment is
        # kept out of the repo tree for exactly this reason. Carrying a sole
        # trader's personal name in a file we then choose not to publish would be
        # the denylist mistake in a different costume: safe only for as long as
        # every downstream reader remembers why.
        out.pop("obchodniJmeno", None)
    return out


def refuse(where, bad_keys, bad_content):
    print(f"AC-GDPR1 REFUSED — nothing written to {where}", file=sys.stderr)
    for k in bad_keys[:10]:
        print(f"  contact-shaped key : {k}", file=sys.stderr)
    for kind, snip in bad_content[:10]:
        print(f"  contact content    : {kind}: {snip}", file=sys.stderr)
    sys.exit(2)


def gate(payload, where):
    text = json.dumps(payload, ensure_ascii=False, indent=1)
    bad_keys = key_violations(payload)
    bad_content = content_violations(text)
    if bad_keys or bad_content:
        refuse(where, bad_keys, bad_content)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--month", required=True)
    ap.add_argument("--lookups", required=True)
    ap.add_argument("--aggregate", required=True)
    ap.add_argument("--max-records", type=int, default=6)
    a = ap.parse_args()

    subjects, misses = [], []
    for name in sorted(os.listdir(a.work)):
        if not name.endswith(".json"):
            continue
        ico = name[:-5]
        try:
            doc = json.load(open(os.path.join(a.work, name), "r", encoding="utf-8"))
        except (OSError, ValueError) as e:
            misses.append({"ico": ico, "reason": f"unreadable: {type(e).__name__}"})
            continue
        red = reduce_subject(doc)
        if red is None:
            misses.append({"ico": ico, "reason": "not a subject document"})
            continue
        if red["ico"] != ico:
            # A 200 carrying SOMEONE ELSE'S subject is Mode A wearing a suit.
            misses.append({"ico": ico, "reason": f"payload is for {red['ico']}"})
            continue
        subjects.append(red)

    resolved = {s["ico"]: s for s in subjects}

    # ---- the enrichment payload (health only, produces no signals) --------
    lookups = {
        "generated_at": None,
        "source": "ares",
        "role": "enrichment",
        "month": a.month,
        "lookups_requested": len(subjects) + len(misses),
        "lookups_resolved": len(subjects),
        "nameable": sum(1 for s in subjects if s["nameable"]),
        "misses": misses,
        "items": subjects,
    }
    from datetime import datetime, timezone
    lookups["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    text = gate(lookups, a.lookups)
    with open(a.lookups, "w", encoding="utf-8") as fh:
        fh.write(text)

    # ---- fold into the MPSV aggregate ------------------------------------
    try:
        agg = json.load(open(a.aggregate, "r", encoding="utf-8"))
    except (OSError, ValueError) as e:
        die(f"aggregate {a.aggregate}: {e}")

    kept, dropped = [], []
    named = 0
    for it in agg.get("items") or []:
        if it.get("kind") != "employer":
            kept.append(it)
            continue
        ico = str(it.get("ico") or "")
        s = resolved.get(ico)
        # FAIL CLOSED, THREE WAYS. No ARES answer, a checksum-invalid IČO, or a
        # legal form outside the legal-person range -> the employer record is
        # DROPPED, not published with a null name. Its postings are still counted
        # inside the theme aggregate, so nothing is lost from the evidence — only
        # the naming is withheld.
        if s is None:
            dropped.append({"ico": ico, "reason": "unresolved by ARES"})
            continue
        if not valid_ico(ico):
            dropped.append({"ico": ico, "reason": "IČO fails the mod-11 checksum"})
            continue
        if not s["nameable"]:
            dropped.append({"ico": ico, "reason": f"pravniForma {s.get('pravniForma')} "
                                                  f"is outside the legal-person range"})
            continue
        if named >= a.max_records:
            dropped.append({"ico": ico, "reason": "below the employer-record cap"})
            continue
        it["employer"] = s.get("obchodniJmeno")
        it["employer_cleared"] = True
        it["employer_legal_form"] = s.get("pravniForma")
        it["employer_founded"] = s.get("datumVzniku")
        it["employer_nace"] = s.get("czNace")
        it["employer_region"] = (s.get("region") or {}).get("nazevKraje")
        named += 1
        kept.append(it)

    agg["items"] = kept
    agg["ares"] = {
        "lookups_requested": lookups["lookups_requested"],
        "lookups_resolved": lookups["lookups_resolved"],
        "employers_named": named,
        "employers_dropped": dropped,
        "payload": os.path.basename(a.lookups),
    }
    text = gate(agg, a.aggregate)
    with open(a.aggregate, "w", encoding="utf-8") as fh:
        fh.write(text)

    print(f"ares_fold: {len(subjects)} resolved / {len(misses)} missed; "
          f"{named} employer record(s) named, {len(dropped)} dropped "
          f"({sum(1 for d in dropped if 'legal-person' in d['reason'])} as natural persons)")
    print(f"ares_fold: privacy gates PASSED on both {os.path.basename(a.lookups)} "
          f"and {os.path.basename(a.aggregate)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
