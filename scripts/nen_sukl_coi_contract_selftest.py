#!/usr/bin/env python3
"""
nen_sukl_coi_contract_selftest.py — proof that the `nen`, `sukl` and `coi` source
contracts reject a WRONG BODY, not just a bad status code.

WHY A TEST AND NOT A PARAGRAPH
==============================
Mode A is "a good transfer carrying the wrong body": a 200 serving a login page,
an error document, a maintenance notice, an empty result set that looks like a
result. Every one of those is a 200 with bytes, so the transport receipt says
`ok` and the byte counter says `fine`. The ONLY thing that separates them from
data is a contract, and a contract nobody has watched fail is a claim, not a
control. This file makes each contract fail on purpose and prints the reason.

It builds its wrong bodies from REAL captured error responses where it can:
`--live` re-fetches the two error documents these hosts actually serve —
isvz.nipez.cz's 404 (158 kB of text/html) and opendata.sukl.cz's 403 on a
directory index — and saves them into the fixtures. Without `--live` it uses the
checked-in miniature equivalents, so the test runs offline in CI.

    python3 scripts/nen_sukl_contract_selftest.py            # offline
    python3 scripts/nen_sukl_contract_selftest.py --live     # + real error bodies

Exit 0 = every wrong body was refused AND every good body was accepted. A wrong
body that PASSES and a good body that FAILS are both failures here; a contract
that refuses everything is not a control either.
"""

import argparse
import io
import json
import os
import subprocess
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import coi_extract   # noqa: E402
import nen_extract   # noqa: E402
import sukl_extract  # noqa: E402

LOGIN_HTML = (
    "<!DOCTYPE html><html lang=\"cs\"><head><title>Přihlášení</title></head>"
    "<body><h1>Přihlášení do systému</h1><form method=\"post\">"
    "<input name=\"username\"><input name=\"password\" type=\"password\">"
    "<button>Přihlásit</button></form></body></html>"
).encode("utf-8")

MAINTENANCE_HTML = (
    "<!DOCTYPE html><html><head><title>503 Service Unavailable</title></head>"
    "<body><h1>Probíhá plánovaná odstávka</h1></body></html>"
).encode("utf-8")


# --------------------------------------------------------------------------
# fixture builders
# --------------------------------------------------------------------------

def zip_of(members, path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in members.items():
            z.writestr(name, data)
    return path


def nen_json(period="2026-07", verze="2.10.1", n=2000, tool="NEN", omit_verze=False):
    head = {"obdobi_od": f"{period}-01T00:00:00", "obdobi_do": f"{period}-28T23:59:59"}
    if not omit_verze:
        head["verze"] = verze
    body = io.StringIO()
    body.write(json.dumps(head, ensure_ascii=False)[:-1])
    body.write(',"data":[')
    for i in range(n):
        if i:
            body.write(",")
        body.write(json.dumps({"verejna_zakazka": {
            "identifikator_NIPEZ": f"RVZ26{i:08d}",
            "identifikatory_v_elektronickem_nastroji": (
                [{"kod_nastroje": tool, "identifikator": f"N006/26/V{i:08d}"}] if tool else []),
            "nazev_verejne_zakazky": f"Testovací zakázka {i}",
            "typ_verejne_zakazky_dle_vyse_predpokladane_hodnoty": "Veřejná zakázka malého rozsahu",
            "predmet": {"popis_predmetu": "Popis předmětu.", "hlavni_kod_CPV": "72000000"},
            "casova_znacka": f"{period}-15T10:00:00",
            "zadavaci_postupy": [{
                "stav": "Aktivní/Neukončen",
                "datum_zahajeni_zadavaciho_postupu": f"{period}-10T09:00:00",
                "zadavatel_zadavaciho_postupu": {"zadavatele": [
                    {"subjekt": {"nazev_subjektu": "Testovací zadavatel", "ico": "00000000"}}]},
            }],
        }}, ensure_ascii=False))
    body.write("]}")
    return body.getvalue().encode("utf-8")


SUKL_HEADER = ";".join(f'"{c}"' for c in sukl_extract.REQUIRED_COLUMNS)


def sukl_csv(n=60000, typ="preruseni", header=SUKL_HEADER, delim=";"):
    out = [header]
    for i in range(n):
        out.append(delim.join('"%s"' % v for v in (
            "ANO", f"{i:07d}", "TESTOVACÍ PŘÍPRAVEK", "10MG TBL NOB 30", "R",
            "N02BA51", typ, "01.08.2026", "01.08.2026", "", "",
            "Výrobní důvody", "")))
    return "\n".join(out).encode("cp1250")


SUKL_VALIDITY = '"PLATNOST"\n"21.08.2026"\n'.encode("cp1250")


# --------------------------------------------------------------------------
# the cases
# --------------------------------------------------------------------------

def nen_cases(tmp, live_404):
    yield ("nen", "REAL 404 error document served as the zip", True,
           zip_path(tmp, "nen-404.zip", live_404 or LOGIN_HTML, raw=True))
    yield ("nen", "login page served as the zip", True,
           zip_path(tmp, "nen-login.zip", LOGIN_HTML, raw=True))
    yield ("nen", "maintenance notice served as the zip", True,
           zip_path(tmp, "nen-503.zip", MAINTENANCE_HTML, raw=True))
    yield ("nen", "valid zip, but the JSON declares no interface version", True,
           zip_of({"VZ-07-2026.json": nen_json(omit_verze=True)},
                  os.path.join(tmp, "nen-noverze.zip")))
    yield ("nen", "valid zip, but it is LAST month's file (period mismatch)", True,
           zip_of({"VZ-06-2026.json": nen_json(period="2026-06")},
                  os.path.join(tmp, "nen-wrongmonth.zip")))
    yield ("nen", "valid zip, well-formed JSON, EMPTY result set", True,
           zip_of({"VZ-07-2026.json": nen_json(n=0)},
                  os.path.join(tmp, "nen-empty.zip")))
    yield ("nen", "valid zip, 2,000 contracts, none of them from NEN", True,
           zip_of({"VZ-07-2026.json": nen_json(tool="TA")},
                  os.path.join(tmp, "nen-notnen.zip")))
    yield ("nen", "valid zip, two JSON members (ambiguous payload)", True,
           zip_of({"VZ-07-2026.json": nen_json(), "VZ-06-2026.json": nen_json()},
                  os.path.join(tmp, "nen-two.zip")))
    yield ("nen", "THE GOOD BODY — 2,000 NEN contracts for the month we asked for", False,
           zip_of({"VZ-07-2026.json": nen_json()}, os.path.join(tmp, "nen-good.zip")))


def sukl_cases(tmp, live_403):
    yield ("sukl", "REAL 403 error document served as the zip", True,
           zip_path(tmp, "sukl-403.zip", live_403 or LOGIN_HTML, raw=True))
    yield ("sukl", "login page served as the zip", True,
           zip_path(tmp, "sukl-login.zip", LOGIN_HTML, raw=True))
    yield ("sukl", "valid zip, but the CSV member is a login page", True,
           zip_of({"mr_hlaseni.csv": LOGIN_HTML}, os.path.join(tmp, "sukl-htmlcsv.zip")))
    yield ("sukl", "valid zip, right columns, COMMA-delimited instead of ;", True,
           zip_of({"mr_hlaseni.csv": sukl_csv(delim=",",
                                              header=SUKL_HEADER.replace(";", ","))},
                  os.path.join(tmp, "sukl-comma.zip")))
    yield ("sukl", "valid zip, but a column was renamed upstream", True,
           zip_of({"mr_hlaseni.csv": sukl_csv(
               header=SUKL_HEADER.replace('"DUVOD_PRERUSENI_UKONCENI"', '"DUVOD"'))},
               os.path.join(tmp, "sukl-renamed.zip")))
    yield ("sukl", "valid zip, well-formed CSV, only 100 rows (truncated transfer)", True,
           zip_of({"mr_hlaseni.csv": sukl_csv(n=100)},
                  os.path.join(tmp, "sukl-short.zip")))
    yield ("sukl", "valid zip, 60,000 rows, an UNKNOWN notice type", True,
           zip_of({"mr_hlaseni.csv": sukl_csv(typ="pozastaveni")},
                  os.path.join(tmp, "sukl-newtype.zip")))
    yield ("sukl", "valid zip, 60,000 rows, NO interruption notices at all", True,
           zip_of({"mr_hlaseni.csv": sukl_csv(typ="zahajeni")},
                  os.path.join(tmp, "sukl-nopreruseni.zip")))
    yield ("sukl", "THE GOOD BODY — 60,000 rows, right columns, right vocabulary", False,
           zip_of({"mr_hlaseni.csv": sukl_csv(),
                   "mr_hlaseni_platnost.csv": SUKL_VALIDITY},
                  os.path.join(tmp, "sukl-good.zip")))


def zip_path(tmp, name, data, raw=False):
    p = os.path.join(tmp, name)
    with open(p, "wb") as fh:
        fh.write(data)
    return p


# ---- ČOI ------------------------------------------------------------------
# Two CSVs, so a case is a (sankce_path, kontroly_path) pair. The interesting
# wrong bodies here are the ones every byte-count and status check would pass:
# a WordPress error page (valid UTF-8, parses as a one-column CSV), a renamed
# column after an upstream schema change, and a SILENTLY RE-SCOPED EXPORT that
# still looks big but no longer carries the history the growth rates need.

def coi_csv(cols, n, first_date="01.01.2015", law="Zák. 634/1992"):
    out = [",".join(cols)]
    for i in range(n):
        # Bulk rows land in 2025-H2 so the positive control actually EMITS. A
        # "good body accepted, 0 items" would pass this test while proving
        # nothing about yield — the completeness rule would be holding the only
        # period back, and a control that cannot produce is not a control.
        d = first_date if i == 0 else "20.12.2025"
        out.append(",".join([str(i), str(1000000 + i), "3000", law, "§12", d][:len(cols)]))
    return "﻿".join(["", "\n".join(out)]).encode("utf-8")


def coi_kontroly(n):
    cols = list(coi_extract.KONTROLY_COLUMNS)
    out = [",".join(cols)]
    for i in range(n):
        out.append(",".join([str(1000000 + i), "15.03.2026", f"{27000000 + i}",
                             "CZ010", "Hlavní město Praha", "CZ010D", "Praha 13",
                             "539635", "Praha"]))
    return ("﻿" + "\n".join(out)).encode("utf-8")


def coi_cases(tmp, live_404):
    def write(name, data):
        p = os.path.join(tmp, name)
        with open(p, "wb") as fh:
            fh.write(data)
        return p

    good_s = write("coi-sankce-good.csv",
                   coi_csv(list(coi_extract.SANKCE_COLUMNS), 120_000))
    good_k = write("coi-kontroly-good.csv", coi_kontroly(160_000))
    err = live_404 or LOGIN_HTML

    yield ("coi", "REAL error document served as sankce.csv", True,
           (write("coi-sankce-err.csv", err), good_k))
    yield ("coi", "cookie/consent page served as kontroly.csv", True,
           (good_s, write("coi-kontroly-login.csv", LOGIN_HTML)))
    yield ("coi", "valid CSV, but a sanction column was renamed upstream", True,
           (write("coi-sankce-renamed.csv",
                  coi_csv([c if c != "Vyse pokuty" else "Castka"
                           for c in coi_extract.SANKCE_COLUMNS], 120_000)), good_k))
    yield ("coi", "valid CSV, well-formed, 1,000 rows (truncated transfer)", True,
           (write("coi-sankce-short.csv",
                  coi_csv(list(coi_extract.SANKCE_COLUMNS), 1_000)), good_k))
    yield ("coi", "valid CSV, full size, but the export was re-scoped to 2020+", True,
           (write("coi-sankce-rescoped.csv",
                  coi_csv(list(coi_extract.SANKCE_COLUMNS), 120_000,
                          first_date="01.01.2020")), good_k))
    yield ("coi", "THE GOOD BODY — 120,000 fines / 160,000 inspections since 2015", False,
           (good_s, good_k))


# --------------------------------------------------------------------------

def run_case(feed, path, tmp):
    """Return (rejected, message). Exercises the SAME entry point the fetchers use."""
    out = os.path.join(tmp, "out.json")
    try:
        if feed == "nen":
            doc = nen_extract.read_zip(path, out, want_period="2026-07",
                                       since="2026-06-01")
        elif feed == "coi":
            doc = coi_extract.read_files(path[0], path[1], out, since="2025-07-01")
        else:
            doc = sukl_extract.read_zip(path, out)
        return False, f"accepted, {doc.get('fetched')} items"
    except (nen_extract.ContractViolation, sukl_extract.ContractViolation,
            coi_extract.ContractViolation) as e:
        return True, str(e)


def fetch_live():
    """The two error documents these hosts really serve. Best-effort."""
    got = {}
    for key, url in (
        ("nen", "https://isvz.nipez.cz/sites/default/files/content/opendata-rvz/VZ-01-1999.zip"),
        ("sukl", "https://opendata.sukl.cz/soubory/MR/"),
        ("coi", "https://coi.gov.cz/userdata/files/dokumenty-ke-stazeni/open-data/neexistuje.csv"),
    ):
        try:
            r = subprocess.run(["curl", "-sSL", "-m", "30", url],
                               capture_output=True, timeout=45)
            if r.stdout:
                got[key] = r.stdout
                print(f"  live error body for {key}: {len(r.stdout):,} bytes")
        except Exception as e:  # noqa: BLE001
            print(f"  live fetch for {key} failed ({e}) — using the offline fixture")
    return got


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--live", action="store_true",
                    help="also pull the hosts' real error documents as fixtures")
    a = ap.parse_args()

    live = fetch_live() if a.live else {}
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        cases = (list(nen_cases(tmp, live.get("nen")))
                 + list(sukl_cases(tmp, live.get("sukl")))
                 + list(coi_cases(tmp, live.get("coi"))))
        width = max(len(c[1]) for c in cases)
        for feed, label, must_reject, path in cases:
            rejected, msg = run_case(feed, path, tmp)
            ok = (rejected == must_reject)
            bad += 0 if ok else 1
            verdict = "REFUSED" if rejected else "accepted"
            mark = "ok  " if ok else "FAIL"
            print(f"[{mark}] {feed:5s} {label:<{width}}  -> {verdict}: {msg[:110]}")
    print()
    if bad:
        print(f"SELFTEST FAILED — {bad} case(s) did not behave as the contract promises")
        return 1
    print(f"SELFTEST PASSED — {len(cases)} cases: every wrong body refused, "
          "every good body accepted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
