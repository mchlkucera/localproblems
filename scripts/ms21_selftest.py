#!/usr/bin/env python3
"""
ms21_selftest.py — proof that the `ms21` lookup refuses a WRONG BODY, reads the
money from the RIGHT financial block, and answers a Czech keyword typed without
diacritics. Offline: every fixture is embedded.

Same doctrine as tacr_contract_selftest.py and nen_sukl_coi_contract_selftest.py:
a 200 carrying a login page or a maintenance notice is bytes with a good
transport receipt, and the only thing separating it from data is a contract
nobody has watched fail. So each guard is made to fail on purpose, and the good
body is then driven through the SAME entry points scripts/fetch_ms21.sh uses
(ms21_index.guard_file, ms21_index.build_index, ms21_query.main).

THE THREE THINGS THAT WOULD BE SILENTLY WRONG WITHOUT A TEST
============================================================
1. THE MONEY BLOCK. Every <PRJ> carries two <PF> blocks distinguished only by
   <T>, and on 553 of the 26,048 public rows the totals DISAGREE. "Take the
   first PF" is not a shortcut, it is 553 wrong prices in a tool whose only job
   is prices. The fixture's two blocks differ by three orders of magnitude, so
   picking the wrong one cannot pass.
2. THE PUBLIC FILTER. It is one `HPF in PUBLIC_FORMS` test, and a company row
   slipping through would be invisible in a 26k-row file. The fixture puts an
   s.r.o. in the middle of the export and asserts its IČO reaches nothing.
3. THE CONTACT CUT. data/lookup/ is committed and public. One live PROBLEM
   field carries a work mailbox (CZ.02.02.02/00/22_005/0004237). The fixture
   carries an email AND a +420 number, and the test greps the WHOLE written
   file, not just the field it expects them in.

    python3 scripts/ms21_selftest.py

Exit 0 = every wrong body refused, every good body accepted, every extraction
and query assertion true.
"""
import io
import json
import os
import sys
import tempfile
from contextlib import redirect_stdout, redirect_stderr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ms21_index  # noqa: E402
import ms21_query  # noqa: E402

NS = "https://ms21xsd.mssf.cz/OpenData/v_1"

# A long PROBLEM: > 600 characters, so the clip is exercised, carrying both a
# mailbox and a +420 number mid-sentence. "kódování" sits near the front so it
# survives the clip and the diacritic query has something to find.
LONG_PROBLEM = (
    "Město nemá jednotné kódování zdravotnické dokumentace a data se přepisují "
    "ručně mezi třemi systémy. " + ("Ruční přepis stojí úvazek navrhované "
    "agendy a plodí chyby v evidenci. " * 12) +
    "Kontaktní osoba: podatelna@mesto-zkouska.cz, tel.: +420 123 456 789."
)

# ── FIXTURE 1 — a good export, three projects ────────────────────────────────
#   PRJ 1  obec (HPF 801)  — PUBLIC, indexed. Two PF blocks that DISAGREE.
#   PRJ 2  s.r.o. (HPF 112) — a company, must never reach the index.
#   PRJ 3  příspěvková organizace (HPF 331) — PUBLIC, indexed, but its PROBLEM
#          is the live placeholder "nerelevantní", so the row keeps the money
#          and drops the `problem` key.
GOOD_EXPORT = """<?xml version = '1.0' encoding = 'UTF-8'?>
<EXPORT xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \
LICENCE="Creative Commons (CC BY 4.0)" AUTOR="Ministerstvo pro místní rozvoj" \
DATE="2026-09-03T18:55:00.000+02:00" FILE="SeznamOperaci_21_27.xml" \
xmlns="%(ns)s">
   <PRJ>
      <ID>110000001</ID>
      <ID_VYZVA>56002187</ID_VYZVA>
      <KOD>CZ.06.01.01/00/22_001/0000001</KOD>
      <NAZ>Elektronizace zdravotnické dokumentace města Zkouška</NAZ>
      <POPIS>Popis, který index nečte.</POPIS>
      <PROBLEM>%(long_problem)s</PROBLEM>
      <CIL>Cílem je jednotné kódování a konec ručního přepisu.</CIL>
      <DZRSKUT>2024-02-28T00:00:00.000+01:00</DZRSKUT>
      <DURPRED>2027-12-31T00:00:00.000+01:00</DURPRED>
      <DURSKUT>2025-04-30T00:00:00.000+02:00</DURSKUT>
      <ZAD>
         <NAZ>Město Zkouška</NAZ>
         <IC>00000001</IC>
         <HPF>801</HPF>
         <ADR>
            <KNAZEV>Jihomoravský kraj</KNAZEV>
            <OKNAZEV>Brno-venkov</OKNAZEV>
            <OBNAZEV>Zkouška</OBNAZEV>
         </ADR>
      </ZAD>
      <PF>
         <T>0</T>
         <CZV>999999999.00</CZV>
         <EU>999999999.00</EU>
         <S>999999999.00</S>
         <CV>999999999.00</CV>
      </PF>
      <PF>
         <T>1</T>
         <CZV>1000000.00</CZV>
         <EU>850000.40</EU>
         <S>150000.60</S>
         <CV>1234567.89</CV>
      </PF>
      <OI>
         <KK>021</KK>
         <KN>Digitalizace veřejné správy</KN>
      </OI>
   </PRJ>
   <PRJ>
      <ID>110000002</ID>
      <ID_VYZVA>80317532</ID_VYZVA>
      <KOD>CZ.01.02.01/01/23_026/0000002</KOD>
      <NAZ>Páteřní síť soukromé firmy</NAZ>
      <PROBLEM>Firma řeší bezpečnost dat a kódování v interní síti.</PROBLEM>
      <CIL>Nová páteřní síť.</CIL>
      <DZRSKUT>2024-01-01T00:00:00.000+01:00</DZRSKUT>
      <ZAD>
         <NAZ>NEVEŘEJNÁ FIRMA s.r.o.</NAZ>
         <IC>99999999</IC>
         <HPF>112</HPF>
         <ADR>
            <KNAZEV>Jihomoravský kraj</KNAZEV>
            <OKNAZEV>Brno-město</OKNAZEV>
            <OBNAZEV>Brno</OBNAZEV>
         </ADR>
      </ZAD>
      <PF>
         <T>1</T>
         <CZV>2000000.00</CZV>
         <EU>1000000.00</EU>
         <S>1000000.00</S>
         <CV>2000000.00</CV>
      </PF>
      <OI><KK>021</KK><KN>Rozvoj malých a středních podniků</KN></OI>
   </PRJ>
   <PRJ>
      <ID>110000003</ID>
      <ID_VYZVA>19536812</ID_VYZVA>
      <KOD>CZ.05.01.01/01/23_038/0000003</KOD>
      <NAZ>Energetické úspory nemocnice</NAZ>
      <PROBLEM>nerelevantní</PROBLEM>
      <CIL>Snížení provozních nákladů budovy.</CIL>
      <ZAD>
         <NAZ>Nemocnice Zkouška, příspěvková organizace</NAZ>
         <IC>00000003</IC>
         <HPF>331</HPF>
         <ADR>
            <KNAZEV>Zlínský kraj</KNAZEV>
            <OKNAZEV>Vsetín</OKNAZEV>
            <OBNAZEV>Zkouška nad Bečvou</OBNAZEV>
         </ADR>
      </ZAD>
      <PF><T>1</T><CZV>500000.00</CZV><EU>400000.00</EU><CNV>100000.00</CNV><CV>600000.00</CV></PF>
      <OI><KK>045</KK><KN>Energeticky účinná renovace veřejné infrastruktury</KN></OI>
   </PRJ>
</EXPORT>
""" % {"ns": NS, "long_problem": LONG_PROBLEM}

# ── FIXTURE 2 — a login page served as 200 ───────────────────────────────────
LOGIN_PAGE = """<!DOCTYPE html>
<html lang="cs"><head><title>Přihlášení — MS2021+</title></head>
<body><form action="/login" method="post">
<input name="user"><input name="pass" type="password">
<button>Přihlásit</button></form></body></html>
"""

# ── FIXTURE 3 — right root element, WRONG namespace ──────────────────────────
# The nastiest of the three: it parses, it has <PRJ> children, and every field
# name matches. Only the namespace says it is a different dataset — v_2, a
# sibling export, a staging host. Without the namespace check this body would
# index to zero rows and read as a healthy empty dataset.
WRONG_NS = """<?xml version = '1.0' encoding = 'UTF-8'?>
<EXPORT LICENCE="Creative Commons (CC BY 4.0)" AUTOR="Ministerstvo pro místní rozvoj" \
xmlns="https://ms21xsd.mssf.cz/OpenData/v_2">
   <PRJ><KOD>CZ.06.01.01/00/22_001/0000001</KOD><NAZ>Jiný dataset</NAZ>
   <ZAD><NAZ>Město Zkouška</NAZ><IC>00000001</IC><HPF>801</HPF></ZAD></PRJ>
</EXPORT>
"""

# ── FIXTURE 4 — a public project whose only PF block is T=0 ──────────────────
# Defensive: the reader must write NO money rather than fall back to T=0.
NO_T1 = """<?xml version = '1.0' encoding = 'UTF-8'?>
<EXPORT LICENCE="Creative Commons (CC BY 4.0)" xmlns="%s">
   <PRJ><KOD>CZ.06.01.01/00/22_001/0000009</KOD><NAZ>Bez skutečného plánu</NAZ>
   <PROBLEM>Obec řeší chybějící chodník.</PROBLEM><CIL>Chodník.</CIL>
   <ZAD><NAZ>Obec Bezpeněz</NAZ><IC>00000009</IC><HPF>801</HPF>
   <ADR><KNAZEV>Kraj Vysočina</KNAZEV><OKNAZEV>Jihlava</OKNAZEV><OBNAZEV>Bezpeněz</OBNAZEV></ADR></ZAD>
   <PF><T>0</T><CZV>111.00</CZV><EU>111.00</EU><CV>111.00</CV></PF></PRJ>
</EXPORT>
""" % NS

FAILURES = []
CHECKS = [0]


def check(label, cond, detail=""):
    CHECKS[0] += 1
    if cond:
        print("  ok   %s" % label)
    else:
        print("  FAIL %s%s" % (label, ("  — " + detail) if detail else ""))
        FAILURES.append(label)


def write(d, name, text):
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text)
    return p


def main():
    with tempfile.TemporaryDirectory(prefix="ms21-selftest.") as d:
        good = write(d, "good.xml", GOOD_EXPORT)
        login = write(d, "login.html", LOGIN_PAGE)
        wrongns = write(d, "wrongns.xml", WRONG_NS)
        not1 = write(d, "not1.xml", NO_T1)
        empty = write(d, "empty.xml", "")
        out = os.path.join(d, "index.jsonl")

        # ── 1. MODE A ────────────────────────────────────────────────────────
        print("\nMODE A — the source contract")
        check("a good export passes the guard",
              ms21_index.guard_file(good) is None,
              str(ms21_index.guard_file(good)))

        r = ms21_index.guard_file(login)
        check("a login page served as 200 is REFUSED", r is not None)
        check("…and the refusal says it is HTML", bool(r) and "HTML" in r, str(r))

        r = ms21_index.guard_file(wrongns)
        check("a wrong-namespace export is REFUSED", r is not None)
        check("…and the refusal names the namespace",
              bool(r) and "OpenData/v_1" in r, str(r))

        check("an empty body is REFUSED", ms21_index.guard_file(empty) is not None)

        meta = ms21_index.root_meta(good)
        check("the guard reads the licence off the root tag",
              meta.get("licence") == "Creative Commons (CC BY 4.0)", str(meta))

        # ── 2. THE INDEX ─────────────────────────────────────────────────────
        print("\nTHE INDEX — three projects in, two rows out")
        stats = ms21_index.build_index(good, out)
        rows = [json.loads(l) for l in open(out, encoding="utf-8")]
        by_kod = {r["kod"]: r for r in rows}

        check("3 projects seen", stats["projects"] == 3, str(stats["projects"]))
        check("exactly 2 public rows written", len(rows) == 2,
              "got %d: %s" % (len(rows), list(by_kod)))
        check("the s.r.o. (HPF 112) is NOT in the index",
              "99999999" not in open(out, encoding="utf-8").read())

        a = by_kod.get("CZ.06.01.01/00/22_001/0000001", {})
        check("obec row: beneficiary", a.get("beneficiary") == "Město Zkouška", str(a.get("beneficiary")))
        check("obec row: IČO", a.get("ico") == "00000001")
        check("obec row: legal_form kept", a.get("legal_form") == "801")
        check("obec row: region/district/municipality",
              (a.get("region"), a.get("district"), a.get("municipality"))
              == ("Jihomoravský kraj", "Brno-venkov", "Zkouška"), str(a))
        check("obec row: call_id", a.get("call_id") == "56002187")
        check("obec row: theme", a.get("theme") == "Digitalizace veřejné správy")
        check("obec row: start is the ACTUAL start, date only",
              a.get("start") == "2024-02-28", str(a.get("start")))
        check("obec row: end is DURSKUT, not the planned DURPRED 2027",
              a.get("end") == "2025-04-30", str(a.get("end")))

        # ── 3. THE MONEY IS THE T=1 BLOCK ────────────────────────────────────
        print("\nTHE MONEY — T=1 and nothing else")
        check("total_czk is the T=1 CV, rounded (1234567.89 -> 1234568)",
              a.get("total_czk") == 1234568, str(a.get("total_czk")))
        check("total_czk is NOT the T=0 CV (999999999)",
              a.get("total_czk") != 999999999)
        check("eu_czk is the T=1 EU", a.get("eu_czk") == 850000, str(a.get("eu_czk")))
        check("own_czk is the T=1 S", a.get("own_czk") == 150001, str(a.get("own_czk")))

        out2 = os.path.join(d, "not1.jsonl")
        ms21_index.build_index(not1, out2)
        b = json.loads(open(out2, encoding="utf-8").read().strip())
        check("a project with no T=1 block gets NO money, not the T=0 fallback",
              "total_czk" not in b and "eu_czk" not in b, str(b))
        check("…and the row still exists, with its problem statement",
              b.get("problem", "").startswith("Obec řeší"), str(b.get("problem")))

        # ── 4. THE PROBLEM FIELD ─────────────────────────────────────────────
        print("\nTHE PROBLEM FIELD — a placeholder is not a statement")
        c = by_kod.get("CZ.05.01.01/01/23_038/0000003", {})
        check("a 'nerelevantní' problem is OMITTED, not written as text",
              "problem" not in c, str(c.get("problem")))
        check("…but the row survives and keeps the money",
              c.get("total_czk") == 600000, str(c.get("total_czk")))
        check("…and the summary counts it",
              stats["placeholder_problem"] == 1, str(stats["placeholder_problem"]))
        check("a real statement is kept", bool(a.get("problem")))
        check("a long problem is clipped to <= 600 chars + the ellipsis",
              len(a.get("problem", "")) <= ms21_index.PROBLEM_MAX + 1,
              str(len(a.get("problem", ""))))
        check("…and the clip is MARKED, so nobody quotes it as complete",
              a.get("problem", "").endswith("…"))
        check("goal is clipped to <= 300", len(a.get("goal", "")) <= ms21_index.GOAL_MAX + 1)

        # ── 5. NO CONTACT DATA SURVIVES ──────────────────────────────────────
        print("\nGDPR — the whole written file, not just the field we expect")
        blob = open(out, encoding="utf-8").read()
        check("no email anywhere in the index",
              ms21_index.EMAIL_RE.search(blob) is None,
              str(ms21_index.EMAIL_RE.search(blob)))
        check("no phone anywhere in the index",
              ms21_index.PHONE_RE.search(blob) is None,
              str(ms21_index.PHONE_RE.search(blob)))
        check("the fixture really did carry both (so this test can fail)",
              ms21_index.EMAIL_RE.search(LONG_PROBLEM) is not None
              and ms21_index.PHONE_RE.search(LONG_PROBLEM) is not None)
        check("the summary counted the cut", stats["contact_cut"] == 1,
              str(stats["contact_cut"]))

        # ── 6. THE QUERY TOOL ────────────────────────────────────────────────
        print("\nTHE QUERY TOOL — a Czech word typed without diacritics")
        def q(argv):
            buf, err = io.StringIO(), io.StringIO()
            with redirect_stdout(buf), redirect_stderr(err):
                rc = ms21_query.main(argv + ["--index", out, "--json"])
            return rc, json.loads(buf.getvalue() or "[]")

        rc, hits = q(["--keyword", "kodovani"])
        check("'kodovani' finds 'kódování'", rc == 0 and len(hits) == 1,
              "rc=%s hits=%d" % (rc, len(hits)))
        check("…and it is the obec project",
              bool(hits) and hits[0]["kod"] == "CZ.06.01.01/00/22_001/0000001")

        rc, hits2 = q(["--keyword", "KÓDOVÁNÍ"])
        check("uppercase with diacritics finds the same row", len(hits2) == 1)

        rc, hits3 = q(["--keyword", "renovace"])
        check("a keyword only in `theme` matches (the haystack is name+problem+goal+theme)",
              len(hits3) == 1 and hits3[0]["kod"] == "CZ.05.01.01/01/23_038/0000003",
              str([h["kod"] for h in hits3]))

        rc, hits4 = q(["--keyword", "kodovani", "--min-czk", "2000000"])
        check("--min-czk drops a project below the floor", hits4 == [])

        rc, hits5 = q(["--keyword", "kodovani", "--region", "jihomoravsky"])
        check("--region is diacritic-insensitive too", len(hits5) == 1)
        rc, hits6 = q(["--keyword", "kodovani", "--region", "Zlínský"])
        check("--region excludes the wrong kraj", hits6 == [])

        rc, hits7 = q(["--ico", "00000003"])
        check("--ico selects one beneficiary",
              len(hits7) == 1 and hits7[0]["ico"] == "00000003")

        rc, hits8 = q([])
        check("no filter at all is refused rather than dumping the file", rc == 2)

        # ── 7. THE CITATION ──────────────────────────────────────────────────
        print("\nTHE CITATION — the five required price fields")
        cite = ms21_query.citation(a)
        check("type is price", cite["type"] == "price")
        check("url is the constant dataset url",
              cite["url"] == "https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml")
        check("note carries the project KOD", a["kod"] in cite["note"])
        check("note explains the constant url so nobody 'fixes' it",
              "constant dataset url" in cite["note"] and "CONVENTIONS.md" in cite["note"])
        check("payer is the beneficiary", cite["payer"] == "Město Zkouška")
        check("amount_czk is total_czk, unquoted",
              cite["amount_czk"] == 1234568 and isinstance(cite["amount_czk"], int))
        check("unit is one-off", cite["unit"] == "one-off")
        check("basis is signed-contract", cite["basis"] == "signed-contract")
        check("date is the project start", cite["date"] == "2024-02-28")
        check("a dateless project gets an EMPTY date, not a substituted one",
              ms21_query.citation({"beneficiary": "x"})["date"] == "")

    print("\n%d checks, %d failure(s)" % (CHECKS[0], len(FAILURES)))
    if FAILURES:
        for f in FAILURES:
            print("  FAILED: %s" % f)
        return 1
    print("ms21_selftest: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
