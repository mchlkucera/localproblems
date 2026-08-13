#!/usr/bin/env python3
"""filter_ted.py — shortlist raw TED fetches for the normalize step.

Usage: python3 scripts/filter_ted.py data/sources/<today>
Reads ted-*.json, dedups by publication-number, keeps notices that either
(a) keyword-match a tracked problem domain, or (b) are open competitions with
estimated value >= EUR_MIN. Prints a ranked markdown shortlist to stdout.
"""
import json, sys, glob, re
from pathlib import Path

EUR_MIN = 200_000        # ~5M CZK — SCORING.md money=2 threshold
CZK_PER_EUR = 24.5

# problem-domain keyword map (czech titles dominate; lowercase substring match)
DOMAINS = {
    "p-0001 energy-communities": ["komunitní energ", "sdílení elektř", "energetické společenství", "eneko"],
    "p-0002 installers-nzu": ["tepeln", "fotovoltaick", "solární"],
    "p-0003 building-permit": ["stavební řízení", "stavebního řízení", "povolování staveb", "stavební úřad", "dsř", "portál stavebníka"],
    "p-0004 care-allowance": ["příspěvek na péči", "sociáln"],
    "p-0008 nis2-security": ["kybernetick", "nis2", "bezpečnostní dohled", "soc ", "siem", "zákon o kybernetické"],
    "p-0009 employment-cards": ["zaměstnaneck", "cizinc", "azyl", "migrac"],
    "p-0011 home-care": ["domácí péč", "pečovatelsk", "terénní služ"],
    "p-0013 instant-payments": ["okamžit", "platební styk"],
    "p-0017 eudi-wallet": ["eidas", "elektronická identita", "identita občana", "digitální identit"],
    "govtech-general": ["digitalizac", "informační systém", "portál", "registr", "agendov", "elektronizac", "spisov"],
    "health-it": ["nemocniční informační", "emedicín", "ehealth", "elektronické zdravotnict"],
    "energy-utilities": ["distribuční soustav", "smart meter", "aim ", "chytré měřen", "dispečink"],
}

def get_text(v):
    """TED multilingual fields: {'cs': [..], 'eng': [..]} or str/list."""
    if v is None: return ""
    if isinstance(v, str): return v
    if isinstance(v, list): return " | ".join(get_text(x) for x in v)
    if isinstance(v, dict):
        for k in ("cs", "eng", "en", "deu"):
            if k in v: return get_text(v[k])
        return get_text(next(iter(v.values()), ""))
    return str(v)

def get_value_eur(n):
    """Best-effort max value in EUR across estimated/total value fields."""
    best = 0.0
    for vf, cf in (("estimated-value-glo", "estimated-value-cur-glo"),
                   ("estimated-value-lot", "estimated-value-cur-lot"),
                   ("total-value", "total-value-cur")):
        vals, curs = n.get(vf), n.get(cf)
        if vals is None: continue
        if not isinstance(vals, list): vals = [vals]
        if not isinstance(curs, list): curs = [curs] * len(vals)
        for v, c in zip(vals, curs or ["EUR"] * len(vals)):
            try: x = float(str(v).replace(",", ""))
            except (ValueError, TypeError): continue
            cur = (str(c) or "EUR").upper()
            if "CZK" in cur: x /= CZK_PER_EUR
            elif "EUR" not in cur: continue
            best = max(best, x)
    return best

def main(srcdir):
    seen, rows = {}, []
    for f in glob.glob(f"{srcdir}/ted-*.json"):
        group = Path(f).stem.replace("ted-", "")
        for n in json.load(open(f)).get("notices", []):
            pn = n.get("publication-number")
            if not pn or pn in seen: continue
            seen[pn] = True
            title = get_text(n.get("notice-title")).strip()
            buyer = get_text(n.get("buyer-name")).strip()
            lt = (title + " " + buyer).lower()
            hits = [d for d, kws in DOMAINS.items() if any(k in lt for k in kws)]
            eur = get_value_eur(n)
            ft = get_text(n.get("form-type"))
            is_open = "competition" in ft
            deadline = get_text(n.get("deadline-receipt-tender-date-lot"))[:10]
            if not hits and not (is_open and eur >= EUR_MIN): continue
            rows.append({
                "pn": pn, "date": get_text(n.get("publication-date"))[:10],
                "title": title[:160], "buyer": buyer[:80],
                "domains": hits, "eur": round(eur), "open": is_open,
                "deadline": deadline, "group": group,
                "cpv": get_text(n.get("classification-cpv"))[:60],
            })
    # rank: domain-matched first, then by value
    rows.sort(key=lambda r: (-len(r["domains"]), -r["eur"]))
    print(f"# TED shortlist — {len(rows)} of {len(seen)} notices kept\n")
    for r in rows:
        od = "OPEN" if r["open"] else "closed/award"
        dl = f" deadline {r['deadline']}" if r["deadline"] else ""
        print(f"- **{r['pn']}** ({r['date']}, {od}{dl}, ~€{r['eur']:,}) "
              f"[{', '.join(r['domains']) or 'value-only'}] {r['title']} — {r['buyer']} (cpv {r['cpv']})")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/sources/2026-08-13")
