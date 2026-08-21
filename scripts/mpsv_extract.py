#!/usr/bin/env python3
"""
mpsv_extract.py — the mechanical extractor for one MPSV hiring AGGREGATE.

THIS IS THE HAND-OFF ARTEFACT. scripts/normalize.py is not owned by this work, so
the change it needs is deliberately two lines and no more:

    from mpsv_extract import extract_mpsv          # near the other imports
    EXTRACTORS = { ..., "mpsv": extract_mpsv }     # scripts/normalize.py:698

Nothing else in normalize.py moves. `FILE_FEED_TOKENS` ALREADY carries
("mpsv", "mpsv") and ("ares", "ares") (normalize.py:97), and `parse_payload`
already recognises a top-level `items` list, which is why the reducer writes that
key. The aggregate payload therefore needs no parser change at all.

DELIBERATELY IMPORTS NOTHING FROM THE REPO. scripts/mpsv_reduce.py imports
normalize.py (for the one shared definition of what personal data looks like), so
putting this function there and importing it back into normalize would close an
import cycle. A standalone file cannot. If a reviewer prefers no new file, the
function body pastes into normalize.py unchanged.

ONE ITEM IN, ONE RECORD OUT — exactly like every other extractor. All the
aggregation already happened in mpsv_reduce.py, upstream of the materiality
filter, which is where `data/CONVENTIONS.md` and architecture §13.4 require it:
a per-posting feed scores money 1 on every row and is filtered out of existence
while looking like it ran correctly.
"""
import re

_WS = re.compile(r"\s+")


def _collapse(s):
    return _WS.sub(" ", str(s or "")).strip()


def extract_mpsv(item, payload_key, today):
    """One `mpsv-hiring-<YYYY-MM>.json` aggregate -> one mechanical record."""
    sid = item.get("id")
    if not sid or not str(sid).startswith("mpsv-"):
        return None
    theme = item.get("theme") or ""
    label = _collapse(item.get("theme_label"))
    top = (item.get("isco_top") or [{}])[0]
    native = _collapse(top.get("label"))          # official Czech occupation name
    regions = item.get("regions") or []
    # 9% of postings carry no workplace region, so an aggregate can legitimately
    # have none. Say nothing rather than emitting "Regions: ." — a model reading
    # `excerpt` should never have to guess whether an empty clause means "no
    # regions" or "the extractor broke".
    region_txt = ", ".join(
        f"{_collapse(r.get('label'))} {r.get('postings')}" for r in regions[:3])
    region_clause = f" Regions: {region_txt}." if region_txt else " No workplace region recorded."
    tz = item.get("typZmenyOpenData") or {}

    if item.get("kind") == "employer":
        # entity_native stays EMPTY unless fetch_ares.sh cleared the name. An
        # uncleared employer record never reaches here — ares_fold.py drops it —
        # but the guard is kept because "the upstream always filters it" is how a
        # personal name eventually gets published.
        entity = _collapse(item.get("employer")) if item.get("employer_cleared") else ""
        excerpt = (f"{item.get('postings')} new vacancies ({item.get('seats')} seats) "
                   f"posted in {item.get('month')} by IČO {item.get('ico')}"
                   f"{' (' + entity + ')' if entity else ''} in the {label.lower()} "
                   f"group; annualised wage floor EUR {item.get('money_eur'):,}."
                   f"{region_clause}")
    else:
        entity = ""
        excerpt = (f"{item.get('postings')} new Czech Labour Office vacancies "
                   f"({item.get('seats')} seats) across {item.get('employers')} employers "
                   f"in {item.get('month')}, {label.lower()}; annualised wage floor "
                   f"EUR {item.get('money_eur'):,}.{region_clause}")

    return {
        # THE ID IS THE AGGREGATE KEY, NEVER DERIVED FROM A POSTING. The same
        # vacancy is reposted for months, so a url or content hash would defeat
        # data/signals/seen.txt entirely (CONVENTIONS.md, id-prefix rules).
        "id": sid,
        "source": "mpsv",
        "evidence_type": "hiring",
        "url": item.get("url") or "",
        # The last day of the aggregated month — the day the window closed.
        "date": str(item.get("date") or "")[:10],
        # The native handle is the official Czech name of the aggregate's
        # most-posted occupation. The English `title` stays model debt.
        "title_native": native,
        "entity_native": entity,
        # Mechanical, from the CZ-ISCO -> theme -> sector table in
        # mpsv_reduce.py. Same class of derivation as TED's CPV_SECTOR: a
        # published classification code read through a declared mapping, not a
        # judgement. `geo_origin` is NOT set here — it stays a model field by law,
        # even though for this feed it is trivially CZ.
        "sector": item.get("sector"),
        "money_eur": item.get("money_eur"),
        "money_note": _collapse(item.get("money_note")),
        # urgency_date is None ON PURPOSE: a closed month's hiring aggregate is
        # not a dated future event. score_urgency(None) is 0 — not pending — so
        # no model is asked to rule on an urgency this feed does not have.
        # Materiality is carried by `money` alone, which for these aggregates is
        # 2 or 3.
        "urgency_date": None,
        # ONE CONTIGUOUS VERBATIM SPAN (architecture §7.8: "Never join fields").
        # It is the codelist's own Czech occupation name, which is a literal
        # substring of the payload on disk, so normalize's substring check
        # verifies it instead of waving it through.
        "quote_parts": [_collapse(item.get("quote"))],
        "excerpt": _collapse(excerpt),
        # The audit trail for the two numbers a reader is most likely to
        # challenge: how much of the month we actually saw, and how the changelog
        # was branched on.
        "notes": _collapse(
            f"MPSV volna-mista-prirustek changelog, {item.get('month')}: "
            f"{tz.get('novy')} novy / {tz.get('zmeneny')} zmeneny / "
            f"{tz.get('zruseny')} zruseny rows; only novy counted. "
            f"{item.get('employers')} distinct IČO; "
            f"{item.get('unpriced_postings')} posting(s) without a usable wage floor. "
            f"Theme {theme} from CZ-ISCO."),
    }
