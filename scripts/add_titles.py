#!/usr/bin/env python3
"""One-off: add a `title:` field to every normalized signal's frontmatter.
The weekly pipeline writes `title:` for new signals from now on (see CONVENTIONS.md)."""
import os, sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "data", "normalized")

TITLES = {
    # market scans
    "de-exnaton": "Exnaton — white-label energy-community billing",
    "de-conmeet": "conmeet — AI-native OS for construction SMBs",
    "de-fuchs-eule": "Fuchs & Eule — AI building-retrofit analytics",
    "de-jupus": "JUPUS — AI secretarial layer for law firms",
    "de-skalar": "Skalar — AI-native tax & accounting firm",
    "de-varm": "VARM — tech-enabled insulation installer",
    "dk-festina": "Festina Finance — pension & life-insurance platform",
    "pl-sunbay": "sunbay.io — AI receivables & dunning automation",
    # regulatory triggers
    "reg-ai-act-milestones": "EU AI Act — Art 50 transparency obligations",
    "reg-ppwr-packaging": "PPWR — packaging requirements apply",
    "reg-cra-reporting": "Cyber Resilience Act — 24-hour vulnerability reporting",
    "reg-eudr-deforestation": "EUDR — due-diligence statements due",
    "reg-nis2-cz-zkb": "Cybersecurity Act 264/2025 — NIS2 transposition",
    "reg-eidas2-eudi-wallet": "eIDAS 2.0 — EU Digital Identity Wallet due",
    "reg-instant-payments-cz": "Instant Payments Regulation — receive instant EUR",
    "reg-machinery-2023-1230": "Machinery Regulation — hard cutover, no transition",
    "reg-amlr-single-rulebook": "EU AML Regulation — single rulebook applies",
    "reg-cbam-definitive": "CBAM definitive regime — first annual declaration",
    "reg-csrd-post-omnibus": "CSRD post-Omnibus — FY2027 reporting cycle",
    "reg-accessibility-act-cz": "Accessibility Act — first full enforcement year",
    "reg-accounting-act-cz": "New Accounting Act — IFRS-aligned rewrite",
    "reg-battery-passport": "Battery Regulation — digital battery passport",
    "reg-cer-zakon-266": "CER Act 266/2025 — critical-entity resilience",
    "reg-data-act-waves": "EU Data Act — access by design, cloud switching",
    "reg-efti-freight": "eFTI Regulation — electronic freight information",
    "reg-epbd-recast": "EPBD recast — building performance obligations",
    "reg-forced-labour": "Forced Labour Regulation — product ban",
    "reg-green-claims-ecgt": "Green claims (ECGT) — substantiate or strip",
    "reg-pay-transparency-cz": "Pay Transparency — pay-gap reporting",
    "reg-pld-software-liability": "Product Liability Directive — software strict liability",
    "reg-right-to-repair": "Right to Repair — repair obligations live",
    # accelerator batch
    "yc-autarc": "autarc — OS for heat-pump & solar installers",
    "yc-mercura": "Mercura — AI quote & order processing for distributors",
    "yc-permitportal": "PermitPortal — AI pre-construction & permits",
    "yc-oma-care": "Oma Care — family caregivers, trained and paid",
    "yc-gale": "Gale — corporate work-visa automation",
    "yc-hammr": "Hammr — construction payroll, HR & compliance",
    "yc-cocrafter": "CoCrafter — contractor-to-subcontractor marketplace",
    "yc-hemut": "Hemut — AI back office for trucking",
    "yc-sagecare": "Sage Care — AI ops for home-care agencies",
    "yc-saturn": "Saturn — compliance OS for wealth managers",
    "yc-sanvivo": "Sanvivo — e-commerce layer for independent pharmacies",
    "yc-autositu": "Autositu — AI workspace for plan reviews",
    "yc-legalos": "LegalOS — AI-native immigration law firm",
    "yc-takecareos": "TakeCareOS — OS for long-term care providers",
    "yc-ventura": "Ventura — AI workforce for distributors",
    # funding rounds
    "round-oxylabs": "Oxylabs — web intelligence infrastructure",
    "round-ominimo": "Ominimo — AI digital car insurance",
    "round-pstryk": "Pstryk — dynamic electricity pricing",
    "round-foractive": "ForActive — fitness business management",
    "round-cthings-co": "CTHINGS.CO — IoT device management",
    "round-trueengage": "TrueEngage — omnichannel customer engagement",
    "round-sigvi": "Sigvi — AI car rental platform",
    "round-trinity-robotics": "Trinity Robotics — autonomous ground vehicles",
    "round-display-dev": "Display.dev — AI document collaboration",
    "round-htg-medical": "HTG Medical — ICU urine-output monitoring",
    # public tenders (TED)
    "ted-372049-2026": "Kroměříž water utility — smart-metering system",
    "ted-373331-2026": "Motol + Homolka hospitals — cyber threat detection",
    "ted-385664-2026": "Petrovice u Karviné — community energy installation",
    "ted-402149-2026": "Ministry of Labour — IT delivery III framework",
    "ted-430180-2026": "Ivančice water association — smart-metering installation",
    "ted-443904-2026": "Bata regional hospital Zlín — hospital information system",
    "ted-453265-2026": "Digital agency — national EU identity wallet build",
    "ted-472636-2026": "City of Prague — SIEM security-event platform",
    "ted-476712-2026": "Plzeň region hospitals — NIS delivery & integrations",
    "ted-542109-2026": "City of Prague — central cyber platform for districts",
    "ted-549134-2026": "Uherské Hradiště hospital — eHealth platform",
    # contract registry
    "hlidac-38551596": "Karlovy Vary regional hospital — information system",
    "hlidac-38899662": "Františkov senior home — electricity-sharing contract",
    "hlidac-39041762": "Židlochovicko water utility — smart metering",
    "hlidac-39084314": "Český Brod — municipal cyber-security package",
}

changed, missing = 0, []
for src in sorted(os.listdir(ROOT)):
    d = os.path.join(ROOT, src)
    if not os.path.isdir(d):
        continue
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"):
            continue
        p = os.path.join(d, fn)
        lines = open(p).read().splitlines(keepends=True)
        sid = None
        for l in lines:
            if l.startswith("id:"):
                sid = l.split(":", 1)[1].strip()
                break
        if any(l.startswith("title:") for l in lines):
            continue
        if sid not in TITLES:
            missing.append(sid or fn)
            continue
        out = []
        for l in lines:
            out.append(l)
            if l.startswith("id:"):
                out.append('title: "%s"\n' % TITLES[sid])
        open(p, "w").write("".join(out))
        changed += 1

print("titled:", changed, "missing:", missing or "none")
sys.exit(1 if missing else 0)
