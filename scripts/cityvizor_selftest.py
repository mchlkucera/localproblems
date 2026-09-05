#!/usr/bin/env python3
"""
cityvizor_selftest.py — proof that the `cityvizor` lookup refuses a WRONG BODY,
keeps only lines that are a PRICE FOR A THING, cuts contact data, gives
identical ledger lines distinct STABLE ids, and answers a Czech keyword typed
without diacritics. Offline: every fixture is embedded.

Same doctrine as ms21_selftest.py: a 200 carrying the Angular shell, an error
object or a reshaped view is bytes with a good transport receipt, and the only
thing separating it from data is a contract nobody has watched fail. So each
guard is made to fail on purpose, and the good body is then driven through the
SAME entry points scripts/fetch_cityvizor.sh uses (cityvizor_index.guard_file,
guard_profiles_file, bodies, years/months/days, build_index,
cityvizor_query.main).

THE FOUR THINGS THAT WOULD BE SILENTLY WRONG WITHOUT A TEST
===========================================================
1. THE ITEM FILTER. "51xx and 61xx" would silently drop 5042, where a software
   licence renewal is booked. The fixture puts a 5042 line beside a 5331
   transfer and a 5011 payroll line and asserts exactly the right ones survive.
2. THE SIGN. A ledger holds income lines and credit notes in the same table as
   purchases; a -4,195 Kč line pasted as `amount_czk` is a negative price.
3. IDENTICAL LINES. The ledgers really hold them (one invoice split across two
   events). Content-hash dedupe would delete a real payment; no suffix would
   give two rows one id. The fixture carries two identical lines and asserts
   two rows, two ids, one with `-2`.
4. THE CEILING. data/lookup/ is committed and never pruned. The fixture is
   built under a ceiling too small for both months and asserts the OLDEST
   month is the one that goes, and that the summary says so.

    python3 scripts/cityvizor_selftest.py

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

import cityvizor_index as ci  # noqa: E402
import cityvizor_query as cq  # noqa: E402

# A long description: > 300 characters so the clip is exercised, carrying an
# email AND a +420 number mid-sentence. "kódování" sits near the front so it
# survives the clip and the diacritic query has something to find.
LONG_DESC = (
    "Licence systému pro kódování zdravotnické dokumentace, roční podpora. "
    + ("Součástí je migrace dat a školení uživatelů. " * 6)
    + "Kontakt: podatelna@mesto-zkouska.cz, tel.: +420 123 456 789."
)

# ── FIXTURE 1 — the profiles list ────────────────────────────────────────────
#   1   visible + payments, has IČO          -> WALKED
#   2   visible, no payments                 -> not walked
#   46  pending test profile WITH payments   -> not walked (status)
#   63  visible + payments, NO IČO (obvod)   -> walked, body_ico omitted
PROFILES = [
    {"id": 1, "status": "visible", "url": "mesto-zkouska", "name": "Město Zkouška",
     "ico": "00000001", "type": "municipality", "parent": None, "hasPayments": True},
    {"id": 2, "status": "visible", "url": "bez-faktur", "name": "Obec Bez Faktur",
     "ico": "00000002", "type": "municipality", "parent": None, "hasPayments": False},
    {"id": 46, "status": "pending", "url": "testiiicek", "name": "Testicek",
     "ico": None, "type": "municipality", "parent": None, "hasPayments": True},
    {"id": 63, "status": "visible", "url": "ostrava-poruba-5Gh249kW", "name": "Ostrava - Poruba ",
     "ico": None, "type": "municipality", "parent": 37, "hasPayments": True},
]


def line(**kw):
    base = {"profileId": 1, "year": 2024, "paragraph": 6171, "item": 5169, "unit": None,
            "event": None, "incomeAmount": 0, "expenditureAmount": 0,
            "date": "2024-03-05T00:00:00.000Z", "counterpartyId": "",
            "counterpartyName": "", "description": ""}
    base.update(kw)
    return base


# ── FIXTURE 2 — one month of Město Zkouška, nine lines ───────────────────────
GOOD_PAYMENTS = [
    # a  software (5172), contact data inside, long -> KEPT, cut, clipped
    line(item=5172, expenditureAmount=1234567.89, counterpartyId="12345678",
         counterpartyName="Softwarová firma s.r.o.", description=LONG_DESC, event="12"),
    # b  income line -> SKIPPED
    line(item=2133, incomeAmount=10890, expenditureAmount=0,
         description="pronájem sloupů VO za 4. čtvrtletí"),
    # c  credit note -> SKIPPED
    line(item=5172, expenditureAmount=-4195.17, counterpartyName="Softwarová firma s.r.o.",
         counterpartyId="12345678", description="dobropis k licenci"),
    # d  transfer to own PBO (5331) -> SKIPPED as non-purchase
    line(item=5331, paragraph=3111, expenditureAmount=5000000, counterpartyId="70000001",
         counterpartyName="Mateřská škola Zkouška, p.o.", description="neinvestiční příspěvek 3/2024"),
    # e  software licence renewal booked at 5042 -> KEPT (the 504x rule)
    line(item=5042, expenditureAmount=12000, counterpartyId="87654321",
         counterpartyName="ESET software spol. s r.o.", description="prodloužení licence ESET PROTECT, 2 roky",
         date="2024-03-12T00:00:00.000Z"),
    # f  payroll (5011) -> SKIPPED
    line(item=5011, expenditureAmount=45000, counterpartyName="Fyzická osoba", description="platy 2/2024"),
    # g1, g2  two IDENTICAL lines -> BOTH kept, ids differ by -2
    line(item=5136, expenditureAmount=1740, counterpartyId="27493091", event="124",
         counterpartyName="Acha obec účtuje s.r.o.", description="publikace Rozpočtová skladba 2024 4 ks",
         date="2024-03-01T00:00:00.000Z"),
    line(item=5136, expenditureAmount=1740, counterpartyId="27493091", event="124",
         counterpartyName="Acha obec účtuje s.r.o.", description="publikace Rozpočtová skladba 2024 4 ks",
         date="2024-03-01T00:00:00.000Z"),
    # h  rounds to 0 Kč -> SKIPPED, never written as amount_czk: 0
    line(item=5169, expenditureAmount=0.3, counterpartyName="CCS", counterpartyId="27916693",
         description="zaokrouhlení"),
    # i  capital software (6111) -> KEPT
    line(item=6111, paragraph=6171, expenditureAmount=520300, counterpartyId="11111111",
         counterpartyName="HRDLIČKA spol.s r.o.", description="Digitální technická mapa - pořízení dat",
         date="2024-03-20T00:00:00.000Z"),
]

# ── FIXTURE 3 — one line of Ostrava-Poruba (no IČO in its profile), April ────
PORUBA_PAYMENTS = [
    line(profileId=63, item=5169, expenditureAmount=580, counterpartyId="22222222",
         counterpartyName="VAVS s.r.o.", description="Seminář quot Velká novela zákona o matrikách quot",
         date="2024-04-02T00:00:00.000Z"),
]

# ── FIXTURE 4 — the Angular shell, served as 200 text/html for any path ──────
SHELL_PAGE = """<!doctype html>
<html lang="cs" data-beasties-container><head><title>Cityvizor</title></head>
<body><app-root></app-root><script src="main.js"></script></body></html>
"""

# ── FIXTURE 5 — an error object: JSON, 200, not an array ─────────────────────
ERROR_OBJECT = '{"error":"Internal Server Error","statusCode":500}'

# ── FIXTURE 6 — right container, WRONG view: the CSV export's field names ────
# Parses, is an array of objects, has a date and an amount — but `amount` is
# not `expenditureAmount`, so every row would index to "no amount" and the
# index would read as a healthy empty month.
WRONG_SHAPE = [
    {"profileId": 1, "year": 2024, "paragraph": 6171, "item": 5169, "amount": 117.37,
     "date": "2024-03-05T00:00:00.000Z", "counterpartyId": "27916693",
     "counterpartyName": "CCS", "description": "provozní poplatek"},
]

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
        fh.write(text if isinstance(text, str) else json.dumps(text, ensure_ascii=False))
    return p


def main():
    with tempfile.TemporaryDirectory(prefix="cityvizor-selftest.") as d:
        profiles = write(d, "profiles.json", PROFILES)
        good = write(d, "1_2024-03-01_2024-04-01.json", GOOD_PAYMENTS)
        poruba = write(d, "63_2024-04-01_2024-05-01.json", PORUBA_PAYMENTS)
        shell = write(d, "shell.html", SHELL_PAGE)
        errobj = write(d, "error.json", ERROR_OBJECT)
        wrong = write(d, "wrong.json", WRONG_SHAPE)
        emptyarr = write(d, "empty-array.json", "[]")
        empty = write(d, "empty.json", "")
        windows = write(d, "windows.tsv",
                        "1\t2024-03-01\t2024-04-01\t%s\t0\n63\t2024-04-01\t2024-05-01\t%s\t0\n"
                        % (good, poruba))
        out = os.path.join(d, "index.jsonl")

        # ── 1. MODE A ────────────────────────────────────────────────────────
        print("\nMODE A — the source contract")
        check("a good payments response passes the guard", ci.guard_file(good) is None,
              str(ci.guard_file(good)))
        check("an EMPTY ARRAY passes — a month with no invoices is a real answer",
              ci.guard_file(emptyarr) is None, str(ci.guard_file(emptyarr)))
        r = ci.guard_file(shell)
        check("the Angular shell served as 200 is REFUSED", r is not None)
        check("…and the refusal says it is HTML", bool(r) and "HTML" in r, str(r))
        r = ci.guard_file(errobj)
        check("an error OBJECT (JSON, not an array) is REFUSED", r is not None)
        check("…and the refusal says so", bool(r) and "not a JSON array" in r, str(r))
        r = ci.guard_file(wrong)
        check("a reshaped view (CSV field names) is REFUSED", r is not None)
        check("…and the refusal names the missing field",
              bool(r) and "expenditureAmount" in r, str(r))
        check("an empty body is REFUSED", ci.guard_file(empty) is not None)

        check("the profiles list passes its guard", ci.guard_profiles_file(profiles) is None,
              str(ci.guard_profiles_file(profiles)))
        check("the shell is refused as a profiles list too",
              ci.guard_profiles_file(shell) is not None)
        check("an empty array is refused as a profiles list (338 expected)",
              ci.guard_profiles_file(emptyarr) is not None)

        # ── 2. THE POPULATION ────────────────────────────────────────────────
        print("\nTHE POPULATION — visible AND hasPayments, nothing else")
        bd = ci.bodies(PROFILES)
        check("exactly the two visible bodies with payments are walked",
              [b["id"] for b in bd] == [1, 63], str([b["id"] for b in bd]))
        check("the pending test profile with payments is NOT walked",
              all(b["id"] != 46 for b in bd))
        check("names are whitespace-collapsed ('Ostrava - Poruba ' -> no trailing space)",
              bd[1]["name"] == "Ostrava - Poruba", repr(bd[1]["name"]))
        check("a null IČO becomes an empty string, not 'None'", bd[1]["ico"] == "", repr(bd[1]["ico"]))

        # ── 3. THE WINDOWS ───────────────────────────────────────────────────
        print("\nTHE WINDOWS — disjoint, [from, to) with `to` EXCLUSIVE")
        check("years clip to the range", ci.years("2024-09-01", "2026-09-06")
              == [("2024-09-01", "2025-01-01"), ("2025-01-01", "2026-01-01"), ("2026-01-01", "2026-09-06")],
              str(ci.years("2024-09-01", "2026-09-06")))
        check("months clip to the range and chain without a gap or overlap",
              ci.months("2024-11-15", "2025-02-03")
              == [("2024-11-15", "2024-12-01"), ("2024-12-01", "2025-01-01"),
                  ("2025-01-01", "2025-02-01"), ("2025-02-01", "2025-02-03")],
              str(ci.months("2024-11-15", "2025-02-03")))
        check("days cross a leap day", ci.days("2024-02-28", "2024-03-01")
              == [("2024-02-28", "2024-02-29"), ("2024-02-29", "2024-03-01")],
              str(ci.days("2024-02-28", "2024-03-01")))
        check("an empty range yields no window", ci.months("2025-01-01", "2025-01-01") == [])

        # ── 4. THE INDEX ─────────────────────────────────────────────────────
        print("\nTHE INDEX — eleven lines in, six rows out")
        stats = ci.build_index(profiles, windows, out)
        rows = [json.loads(l) for l in open(out, encoding="utf-8")]
        by_desc = {}
        for r in rows:
            by_desc.setdefault(r.get("description", "")[:20], []).append(r)

        check("11 ledger lines seen across 2 windows",
              stats["lines"] == 11 and stats["windows"] == 2, str((stats["lines"], stats["windows"])))
        check("exactly 6 rows written (5 Zkouška + 1 Poruba)", len(rows) == 6, "got %d: %s" % (len(rows), [r["id"] for r in rows]))
        check("the income line is skipped and counted", stats["income_skipped"] == 1, str(stats["income_skipped"]))
        check("the credit note is skipped and counted", stats["negative_skipped"] == 1, str(stats["negative_skipped"]))
        check("the 0.3 Kč line is skipped, never written as amount_czk: 0",
              stats["zero_skipped"] == 1 and all(r["amount_czk"] > 0 for r in rows))
        check("the 5331 transfer and the 5011 payroll are skipped as non-purchases",
              stats["non_purchase_skipped"] == {"53xx": 1, "50xx": 1}, str(stats["non_purchase_skipped"]))
        check("the 5042 licence renewal IS kept (the 504x rule)",
              any(r["budget_item"] == 5042 for r in rows))
        check("the 6111 capital software IS kept", any(r["budget_item"] == 6111 for r in rows))
        check("no row carries a non-purchase item",
              all(ci.is_purchase(r["budget_item"]) for r in rows))
        check("is_purchase: 5042 yes, 5041 yes, 5011 no, 5331 no, 5811 no, 6121 yes, None no",
              (ci.is_purchase(5042), ci.is_purchase(5041), ci.is_purchase(5011), ci.is_purchase(5331),
               ci.is_purchase(5811), ci.is_purchase(6121), ci.is_purchase(None))
              == (True, True, False, False, False, True, False))

        a = next((r for r in rows if r["budget_item"] == 5172), {})
        check("software row: body + body_ico + profile slug",
              (a.get("body"), a.get("body_ico"), a.get("profile")) == ("Město Zkouška", "00000001", "mesto-zkouska"),
              str(a))
        check("software row: amount is whole crowns, rounded (1234567.89 -> 1234568), an int",
              a.get("amount_czk") == 1234568 and isinstance(a.get("amount_czk"), int), str(a.get("amount_czk")))
        check("software row: date is the ISO day only", a.get("date") == "2024-03-05", str(a.get("date")))
        check("software row: year is the ledger's budget year", a.get("year") == 2024)
        check("software row: counterparty + IČO",
              (a.get("counterparty"), a.get("counterparty_ico")) == ("Softwarová firma s.r.o.", "12345678"))
        check("software row: budget paragraph + item", (a.get("budget_paragraph"), a.get("budget_item")) == (6171, 5172))
        check("a long description is clipped to <= 300 chars + the ellipsis",
              len(a.get("description", "")) <= ci.DESCRIPTION_MAX + 1, str(len(a.get("description", ""))))
        check("…and the clip is MARKED, so nobody quotes it as complete", a.get("description", "").endswith("…"))

        p = next((r for r in rows if r.get("profile", "").startswith("ostrava-poruba")), {})
        check("a body with no IČO in its profile gets NO body_ico key (omitted, not '')",
              p and "body_ico" not in p, str(p))
        check("…and the summary counts it", stats["no_body_ico"] == 1, str(stats["no_body_ico"]))
        check("…and its name is collapsed", p.get("body") == "Ostrava - Poruba", repr(p.get("body")))

        # ── 5. IDENTICAL LINES ───────────────────────────────────────────────
        print("\nIDENTICAL LINES — two rows, two ids, one suffix")
        g = [r for r in rows if r["budget_item"] == 5136]
        check("both identical lines survive", len(g) == 2, str(len(g)))
        check("their ids differ", len(g) == 2 and g[0]["id"] != g[1]["id"], str([r["id"] for r in g]))
        check("one of them carries the -2 suffix and shares the stem",
              len(g) == 2 and sorted(r["id"] for r in g)[1] == sorted(r["id"] for r in g)[0] + "-2",
              str([r["id"] for r in g]))
        check("the summary counts one duplicate line", stats["duplicate_lines"] == 1, str(stats["duplicate_lines"]))
        check("ids are cv-<profileId>-<12 hex>",
              all(r["id"].startswith("cv-%s-" % (1 if r["profile"] == "mesto-zkouska" else 63))
                  and len(r["id"].split("-")[2]) == 12 for r in rows), str([r["id"] for r in rows]))

        # ── 6. STABILITY ─────────────────────────────────────────────────────
        print("\nSTABILITY — a rebuild over the same bytes is byte-identical")
        out2 = os.path.join(d, "index2.jsonl")
        ci.build_index(profiles, windows, out2)
        check("two builds produce identical files",
              open(out, "rb").read() == open(out2, "rb").read())
        check("rows are sorted by (date, profile, id)",
              [r["date"] for r in rows] == sorted(r["date"] for r in rows))
        # The id is over RAW source values: re-scrubbing must not move it.
        raw_line = GOOD_PAYMENTS[0]
        check("row_key ignores nothing the source carries and nothing it does not",
              ci.row_key(1, raw_line) == ci.row_key(1, dict(raw_line))
              and ci.row_key(1, raw_line) != ci.row_key(1, dict(raw_line, expenditureAmount=1234567.88)))

        # ── 7. NO CONTACT DATA SURVIVES ──────────────────────────────────────
        print("\nGDPR — the whole written file, not just the field we expect")
        blob = open(out, encoding="utf-8").read()
        check("no email anywhere in the index", ci.EMAIL_RE.search(blob) is None, str(ci.EMAIL_RE.search(blob)))
        check("no phone anywhere in the index", ci.PHONE_RE.search(blob) is None, str(ci.PHONE_RE.search(blob)))
        check("the fixture really did carry both (so this test can fail)",
              ci.EMAIL_RE.search(LONG_DESC) is not None and ci.PHONE_RE.search(LONG_DESC) is not None)
        check("the summary counted the cut", stats["contact_cut"] == 1, str(stats["contact_cut"]))

        # ── 8. THE CEILING ───────────────────────────────────────────────────
        print("\nTHE CEILING — the OLDEST month goes first, and the summary says so")
        out3 = os.path.join(d, "index3.jsonl")
        # ~400 bytes: room for the one April row, not for the four March ones.
        s3 = ci.build_index(profiles, windows, out3, max_mb=400 / 1048576.0)
        rows3 = [json.loads(l) for l in open(out3, encoding="utf-8")]
        check("under a tiny ceiling only the newest month survives",
              len(rows3) == 1 and rows3[0]["date"] == "2024-04-02", str([r["date"] for r in rows3]))
        check("the summary names the trimmed month", s3["months_trimmed"] == ["2024-03"], str(s3["months_trimmed"]))
        check("kept_from / kept_to describe the surviving window",
              (s3["kept_from"], s3["kept_to"]) == ("2024-04-01", "2024-04-02"), str((s3["kept_from"], s3["kept_to"])))
        check("under the default ceiling nothing is trimmed",
              stats["months_trimmed"] == [] and stats["kept_from"] == "2024-03-01", str(stats["months_trimmed"]))
        check("fetched_from / fetched_to come from the window list",
              (stats["fetched_from"], stats["fetched_to"]) == ("2024-03-01", "2024-05-01"))

        # ── 9. THE QUERY TOOL ────────────────────────────────────────────────
        print("\nTHE QUERY TOOL — a Czech word typed without diacritics")

        def q(argv):
            buf, err = io.StringIO(), io.StringIO()
            with redirect_stdout(buf), redirect_stderr(err):
                rc = cq.main(argv + ["--index", out, "--json"])
            return rc, json.loads(buf.getvalue() or "[]")

        rc, hits = q(["--keyword", "kodovani"])
        check("'kodovani' finds 'kódování'", rc == 0 and len(hits) == 1, "rc=%s hits=%d" % (rc, len(hits)))
        check("…and it is the software row", bool(hits) and hits[0]["budget_item"] == 5172)
        rc, hits2 = q(["--keyword", "KÓDOVÁNÍ"])
        check("uppercase with diacritics finds the same row", len(hits2) == 1)
        rc, hits3 = q(["--keyword", "softwarova firma"])
        check("a keyword only in the COUNTERPARTY name matches", len(hits3) == 1 and hits3[0]["budget_item"] == 5172)
        rc, hits4 = q(["--keyword", "licence"])
        check("'licence' finds both licence rows (5172 + 5042), largest first",
              [h["budget_item"] for h in hits4] == [5172, 5042], str([h["budget_item"] for h in hits4]))
        rc, hits5 = q(["--keyword", "licence", "--min-czk", "100000"])
        check("--min-czk drops the 12,000 Kč renewal", [h["budget_item"] for h in hits5] == [5172])
        rc, hits6 = q(["--body", "poruba"])
        check("--body is diacritic-insensitive and selects the obvod", len(hits6) == 1 and hits6[0]["amount_czk"] == 580)
        rc, hits7 = q(["--body", "zkouška", "--year", "2024"])
        check("--body + --year together (5172, 5042, 5136 x2, 6111)", len(hits7) == 5, str(len(hits7)))
        rc, hits8 = q(["--ico", "27493091"])
        check("--ico selects by COUNTERPARTY IČO and keeps both identical lines", len(hits8) == 2)
        rc, hits9 = q([])
        check("no filter at all is refused rather than dumping the file", rc == 2)

        # ── 10. THE CITATION ─────────────────────────────────────────────────
        print("\nTHE CITATION — the five required price fields, and a url per body per month")
        cite = cq.citation(a)
        check("type is price", cite["type"] == "price")
        check("url is the body's invoice page for THAT month (matrix params, as the site's own picker builds)",
              cite["url"] == "https://cityvizor.cz/mesto-zkouska/faktury;rok=2024;mesic=3", cite["url"])
        check("note carries the row id", a["id"] in cite["note"])
        check("note explains the shared url so nobody 'fixes' it",
              "no per-invoice permalink" in cite["note"] and "CONVENTIONS.md" in cite["note"])
        check("note names the counterparty and the amount",
              "Softwarová firma s.r.o. (IČO 12345678)" in cite["note"] and "1 234 568 Kč" in cite["note"])
        check("payer is the body", cite["payer"] == "Město Zkouška")
        check("amount_czk is the int amount", cite["amount_czk"] == 1234568 and isinstance(cite["amount_czk"], int))
        check("unit is one-off", cite["unit"] == "one-off")
        check("basis is signed-contract", cite["basis"] == "signed-contract")
        check("date is the booking date", cite["date"] == "2024-03-05")
        check("the citation is STABLE across builds",
              cq.citation(a) == cq.citation(json.loads(open(out2, encoding="utf-8").readlines()[
                  [json.loads(l)["id"] for l in open(out2, encoding="utf-8")].index(a["id"])])))
        check("a same-month row of the same body shares the url (by design)",
              cq.citation(g[0])["url"] == cite["url"])
        check("a different month gets a different url",
              cq.citation(p)["url"] == "https://cityvizor.cz/ostrava-poruba-5Gh249kW/faktury;rok=2024;mesic=4",
              cq.citation(p)["url"])
        buf = io.StringIO()
        with redirect_stdout(buf):
            cq.main(["--keyword", "licence", "--index", out])
        n_warn = buf.getvalue().count("NEŽ TOHLE POUŽIJETE")
        check("the human output prints the subject-test warning on EVERY hit (2 hits, 2 warnings)",
              n_warn == 2, str(n_warn))
        check("…and it is the SAME warning ms21_query.py prints",
              "Stavba pavilonu není cena za software" in buf.getvalue())
        check("the footer prints total AND median", "median" in buf.getvalue() and "v total" in buf.getvalue()
              or "in total, median" in buf.getvalue())

    print("\n%d checks, %d failure(s)" % (CHECKS[0], len(FAILURES)))
    if FAILURES:
        for f in FAILURES:
            print("  FAILED: %s" % f)
        return 1
    print("cityvizor_selftest: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
