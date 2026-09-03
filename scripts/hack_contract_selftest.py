#!/usr/bin/env python3
"""
hack_contract_selftest.py — proof that the `hackathon` feed's per-site contracts
refuse a WRONG BODY, accept the RIGHT one, and stage what the spec promises.

WHY A TEST AND NOT A PARAGRAPH
==============================
Every one of the six organizer pages is a 200 with bytes whether it carries
challenges, a login form, a maintenance notice, or another site's page from a
misrouted CDN. The transport receipt says `ok` for all of them. The only thing
that separates data from not-data is the section marker in
scripts/hack_extract.py's rule table — and a guard nobody has watched fail is a
claim, not a control. This file makes each guard fail on purpose, then proves
the good body yields exactly what was measured on 2026-09-03.

The fixtures are TRIMMED REAL HTML from that day's captures (styles, scripts,
svg and the figma blobs cut; the markup the parser keys on left intact), so a
site redesign that breaks the live page will NOT break this test — that is the
fetcher's MODE-A guard's job — but a parser edit that breaks the contract will.
Each fixture also carries the page's own sentence naming its setters, from the
same capture, because the owner is READ from the page (hack_extract `setters`).

The owner decisions of 2026-09-03 are proved here too, each by a case that
would pass under the old code's fallback and fails now: a page that names no
setter yields nothing (never the organizer); a box without its "Zadavatel:"
label is refused; a bare topic line is refused; a row's `urgency_date` is None
however near the event; every staged record carries a top-level `owner` equal
to the institution the page names.

    python3 scripts/hack_contract_selftest.py      # offline, exit 0 = all pass
"""

import contextlib
import datetime as dt
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import hack_extract as hx  # noqa: E402

LOGIN_HTML = (
    "<!DOCTYPE html><html lang=\"cs\"><head><title>Přihlášení</title></head>"
    "<body><h1>Přihlášení do systému</h1><form method=\"post\">"
    "<input name=\"username\"><input name=\"password\" type=\"password\">"
    "<button>Přihlásit</button></form></body></html>"
)

MAINTENANCE_HTML = (
    "<!DOCTYPE html><html><head><title>503 Service Unavailable</title></head>"
    "<body><h1>Probíhá plánovaná odstávka</h1><p>Zkuste to prosím později.</p></body></html>"
)

# The shape extract_nku / extract_ec_hys return, which normalize.py consumes.
REQUIRED_KEYS = ("id", "source", "evidence_type", "url", "date", "title_native",
                 "entity_native", "owner", "sector", "money_eur", "money_note",
                 "urgency_date", "quote_parts", "excerpt")
ID_RE = re.compile(r"^[a-z]{2,10}-[\w.-]+$")

# What each fixture must yield: (rows, first title, first owner, edition, event_date).
# upol is 0: its topic lines are bare titles. aimtec is 1 of 2: "Trénink zraku"
# names no institution. rakathon's owner is the hospital list the page names.
EXPECT = {
    "hackjakbrno":  (2, "StructREP", "Masarykův onkologický ústav", "2025", "2026-11-27"),
    "rakathon":     (2, "Rekurze", "FN Motol, Masarykův onkologický ústav, FN Ostrava", "2025", "2026-10-16"),
    "upol":         (0, "", "", "", ""),
    "idea13":       (2, "Volnočasové aktivity", "MČ Praha 13", "2026", "2026-09-18"),
    "aimtec":       (1, "Elektrické vozíky s DNA motorsportu", "Astrum Mobility", "2026", ""),
    "nakopniprahu": (4, "Mobilita a veřejný prostor · Udržitelný pohyb po městě",
                     "Hlavní město Praha (MHMP), OICT", "2026", "2026-05-27"),
}

# Trimmed real HTML captured 2026-09-03 — regenerate from .fetch/hackathon/*.html
# when a site is re-measured; keep the markup the rule table keys on intact.
FIXTURES = {
    # hackjakbrno: 4340 bytes
    'hackjakbrno': '<html><body>\n<p>alse" src="https://s.w.org/images/core/emoji/17.0.2/svg/1f552.svg" alt="🕒" />\xa0\xa0<span style="background-color: transparent;">27. &#8211; 29. Listopadu 2026</span></p><p><img class="emoji" draggable="false" src="https://s.w.org/images/core/emoji/17.0.2/svg/1f4cc.svg" alt="📌" /> Místo konání: Fakultní nemocnice u sv. Anny v Brně</p> </p>\nner">\n<h2 class="elementor-heading-title elementor-size-default">Výzvy 2025 </h2> </div>\n</div>\n<div class="elementor-element elementor-element-c436a41 e-flex e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<div class="elementor-element elementor-element-2cb10d04 e-con-full e-flex e-con e-child">\n<div class="elementor-element elementor-element-43446784 e-con-full e-flex e-con e-child">\n<div class="elementor-element elementor-element-519b725b elementor-view-default elementor-position-block-start elementor-mobile-position-block-start elementor-widget elementor-widget-icon-box">\n<div class="elementor-widget-container">\n<div class="elementor-icon-box-wrapper">\n<div class="elementor-icon-box-icon">\n<span class="elementor-icon">\n</span>\n</div>\n<div class="elementor-icon-box-content">\n<h3 class="elementor-icon-box-title">\n<span >\n1. StructREP </span>\n</h3>\n<p class="elementor-icon-box-description">\nVytvořte nástroj, který umožní lékařům jednoduše psát strukturované radiologické nálezy přímo v nemocničním systému pomocí chytrých šablon. Standardizace přinese rychlejší a přesnější zprávy, lepší komunikaci mezi lékaři a zároveň umožní sběr parametrických dat už při tvorbě nálezu. To ušetří čas, sníží chybovost a otevře cestu k efektivní analýze i využití dat pro další medicínský výzkum. </p>\n</div>\n</div>\n</div>\n</div>\n<div class="elementor-element elementor-element-464c095 elementor-widget elementor-widget-heading">\n<div class="elementor-widget-container">\n<h6 class="elementor-heading-title elementor-size-default"><a href="https://www.mou.cz/">Zadavatel: Masarykův onkologický ústav</a></h6> </div>\n</div>\n</div>\n<div class="elementor-element elementor-element-67b3a3b7 e-con-full e-flex e-con e-child">\n<div class="elementor-element elementor-element-725a2de2 elementor-view-default elementor-position-block-start elementor-mobile-position-block-start elementor-widget elementor-widget-icon-box">\n<div class="elementor-widget-container">\n<div class="elementor-icon-box-wrapper">\n<div class="elementor-icon-box-icon">\n<span class="elementor-icon">\n</span>\n</div>\n<div class="elementor-icon-box-content">\n<h3 class="elementor-icon-box-title">\n<span >\n2. AI DocuHelper </span>\n</h3>\n<p class="elementor-icon-box-description">\nExtrakce dat z onkologické dokumentace je dnes pomalá a náročná. Cílem je vytvořit AI asistenta, který dokumentátorům usnadní práci: rychle najde klíčové údaje ve zprávách, nabídne přehledné filtrování a připraví předvyplněné formuláře. Výsledek? Méně chyb, více času pro experty a kvalitní data pro registry, výzkum i klinickou praxi. </p>\n</div>\n</div>\n</div>\n</div>\n<div class="elementor-element elementor-element-3f2f8da elementor-widget elementor-widget-heading">\n<div class="elementor-widget-container">\n<h6 class="elementor-heading-title elementor-size-default"><a href="https://www.mou.cz/">Zadavatel: Masarykův onkologický ústav</a></h6> </div>\n</div>\n</div>\n<div class="elementor-element elementor-element-7c0fd02d e-con-full e-flex e-con e-child">\nget-container">\n<h2 class="elementor-heading-title elementor-size-default">Hlavní ceny</h2> </div>\n</div>\n<div class="elementor-element elementor-element-cc3c369 e-flex e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<div class="elementor-element elementor-element-abfa25c e-grid e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<div class="elementor-element elementor-element-442550e elementor-view-default elementor-position-block-start elementor-mobile-position-block-start elementor-widget elementor-widget-icon-box">\n<div class="elementor-widget-container">\n<div class="elementor-icon-box-wrapper">\n<div class="elementor-icon-box-icon">\n<span class="elementor-icon">\n</span>\n</div>\n<div class="elementor-icon-box-content">\n<h3 class="elementor-icon-box-title">\n<span >\n1. místo:\n25 000 Kč </span>\n</h3>\n</div>\n</div>\n</div>\n</div>\n</body></html>',
    # rakathon: 8215 bytes
    'rakathon': '<html><body>\n<h3 style="text-align:center;white-space:pre-wrap;">16. až 18. října 2026 | Praha-Brno-Ostrava</h3>\n<div class="sqs-html-content" data-sqsp-text-block-content><p class="sqsrte-large" style="white-space:pre-wrap;" data-rte-preserve-empty="true">Hackathon proběhne ve třech městech v ČR: v Praze (FN Motol a Homolka, akademický partner 2. LF UK a ČVUT v Praze), v Brně (MOU, akademický partner MUNI MED a VUT) a v Ostravě (Fakultní nemocnice Ostrava, akademický partner VŠB-TUO).</p></div>\nlass="sqs-text-block-container">\n<div class="sqs-html-content" data-sqsp-text-block-content><h2 style="white-space:pre-wrap;">Výzvy</h2></div>\n</div>\n</div></div></div><div class="fe-block fe-block-f697b1a84f2a3fd47d8c"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block" data-block-type="1337"><div class="sqs-block-content"><div class="sqs-text-block-container">\n<div class="sqs-html-content" data-sqsp-text-block-content><h4 style="white-space:pre-wrap;" data-rte-preserve-empty="true">Příklady výzev z minulého ročníku. Výzvy na ročník 2026 připravujeme. </h4></div>\n</div>\n</div></div></div><div class="fe-block fe-block-d13f76b359290b47b91f"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-image image-block" data-block-type="1337"><div class="sqs-block-content">\n<div\nclass="fluid-image-component-root image-block-outer-wrapper design-layout-fluid image-position-center combination-animation-site-default individual-animation-site-default\n}"\ndata-component-id="d13f76b359290b47b91f"\ndata-test="image-block-fluid-outer-wrapper"\ndata-is-image-stretched="false"\ndata-is-mask-applied="true"\ndata-media-focal-point="0.5,0.5"\ndata-shape-mask="rabbet"\ndata-bpo=""\ndata-breakpoints="[{&quot;id&quot;:&quot;system_desktop&quot;,&quot;name&quot;:&quot;Desktop&quot;},{&quot;id&quot;:&quot;system_mobile&quot;,&quot;name&quot;:&quot;Mobile&quot;,&quot;maxWidth&quot;:&quot;767px&quot;}]"\n>\n<div\nclass="fluid-image-animation-wrapper sqs-image sqs-block-alignment-wrapper"\n>\n<div\nclass="fluid-image-container sqs-image-content js-image-container visitor-mode"\ndata-shape-mask="rabbet"\ndata-sqsp-image-block-image-container\n>\n<div class="js-content-mode-element-wrapper js-content-mode-element-system_desktop">\n<div class="js-content-mode-element content-fill">\n<img data-stretch="false"\ndata-sqsp-image-block-image\nalt=""\ndata-licensed-asset-preview="false"\nelementtiming="system-image-block" src="" width="1024" height="1024" alt="" style="display:block;object-position: var(--image-component-focal-point);object-fit: var(--image-component-object-fit);" data-loader="sqs">\n<div class="fluidImageOverlay"></div>\n</div>\n</div>\n</div>\n</div>\n</div>\n</div></div></div><div class="fe-block fe-block-14d1a8f8cfbea0c65e2d"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block" data-block-type="1337"><div class="sqs-block-content"><div class="sqs-text-block-container">\n<div class="sqs-html-content" data-sqsp-text-block-content><p style="text-align:center;white-space:pre-wrap;" class="sqsrte-large">Vytvořte pokročilý prediktivní model využívající data ÚZIS k odhadu rizika recidivy rakoviny prsu. </p></div>\n</div>\n</div></div></div><div class="fe-block fe-block-6c6db565f6eb69542ca2"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block" data-block-type="1337"><div class="sqs-block-content"><div class="sqs-text-block-container">\n<div class="sqs-html-content" data-sqsp-text-block-content><h3 style="text-align:center;white-space:pre-wrap;">Rekurze</h3></div>\n</div>\n</div></div></div><div class="fe-block fe-block-3e2f1b727a502f116366"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-image image-block" data-block-type="1337"><div class="sqs-block-content">\n<div\nclass="fluid-image-component-root image-block-outer-wrapper design-layout-fluid image-position-center combination-animation-site-default individual-animation-site-default\n}"\ndata-component-id="3e2f1b727a502f116366"\ndata-test="image-block-fluid-outer-wrapper"\ndata-is-image-stretched="false"\ndata-is-mask-applied="true"\ndata-media-focal-point="0.5,0.5"\ndata-shape-mask="diamond"\ndata-bpo=""\ndata-breakpoints="[{&quot;id&quot;:&quot;system_desktop&quot;,&quot;name&quot;:&quot;Desktop&quot;},{&quot;id&quot;:&quot;system_mobile&quot;,&quot;name&quot;:&quot;Mobile&quot;,&quot;maxWidth&quot;:&quot;767px&quot;}]"\n>\n<div\nclass="fluid-image-animation-wrapper sqs-image sqs-block-alignment-wrapper"\n>\n<div\nclass="fluid-image-container sqs-image-content js-image-container visitor-mode"\ndata-shape-mask="diamond"\ndata-sqsp-image-block-image-container\n>\n<div class="js-content-mode-element-wrapper js-content-mode-element-system_desktop">\n<div class="js-content-mode-element content-fill">\n<img data-stretch="false"\ndata-sqsp-image-block-image\nalt=""\ndata-licensed-asset-preview="false"\nelementtiming="system-image-block" src="" width="1024" height="1024" alt="" style="display:block;object-position: var(--image-component-focal-point);object-fit: var(--image-component-object-fit);" data-loader="sqs">\n<div class="fluidImageOverlay"></div>\n</div>\n</div>\n</div>\n</div>\n</div>\n</div></div></div><div class="fe-block fe-block-a86f6b326132028cb3ae"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block" data-block-type="1337"><div class="sqs-block-content"><div class="sqs-text-block-container">\n<div class="sqs-html-content" data-sqsp-text-block-content><p style="text-align:center;white-space:pre-wrap;" class="sqsrte-large">Navrhněte inovativní řešení pro zvýšení kapacity onkologických oddělení, aby více žen dostalo včasnou a kvalitní léčbu.</p><p class="" data-rte-preserve-empty="true" style="white-space:pre-wrap;"></p></div>\n</div>\n</div></div></div><div class="fe-block fe-block-e02f4e1e80ef09e5a4ed"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block" data-block-type="1337"><div class="sqs-block-content"><div class="sqs-text-block-container">\n<div class="sqs-html-content" data-sqsp-text-block-content><h3 style="text-align:center;white-space:pre-wrap;">OnkoCapacity</h3></div>\n</div>\n</div></div></div><div class="fe-block fe-block-0f50ba995fc6a5fa06bc"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-image image-block" data-block-type="1337"><div class="sqs-block-content">\n<div\nclass="fluid-image-component-root image-block-outer-wrapper design-layout-fluid image-position-center combination-animation-site-default individual-animation-site-default\n}"\ndata-component-id="0f50ba995fc6a5fa06bc"\ndata-test="image-block-fluid-outer-wrapper"\ndata-is-image-stretched="false"\ndata-is-mask-applied="true"\ndata-media-focal-point="0.5,0.5"\ndata-shape-mask="stepped-cross"\ndata-bpo=""\ndata-breakpoints="[{&quot;id&quot;:&quot;system_desktop&quot;,&quot;name&quot;:&quot;Desktop&quot;},{&quot;id&quot;:&quot;system_mobile&quot;,&quot;name&quot;:&quot;Mobile&quot;,&quot;maxWidth&quot;:&quot;767px&quot;}]"\n>\n<div\nclass="fluid-image-animation-wrapper sqs-image sqs-block-alignment-wrapper"\n>\n<div\nclass="fluid-image-container sqs-image-content js-image-container visitor-mode"\ndata-shape-mask="stepped-cross"\ndata-sqsp-image-block-image-container\n>\n<div class="js-content-mode-element-wrapper js-content-mode-element-system_desktop">\n<div class="js-content-mode-element content-fill">\n<img data-stretch="false"\ndata-sqsp-image-block-image\nalt=""\ndata-licensed-asset-preview="false"\nelementtiming="system-image-block" src="" width="1024" height="1024" alt="" style="display:block;object-position: var(--image-component-focal-point);object-fit: var(--image-component-object-fit);" data-loader="sqs">\n<div class="fluidImageOverlay"></div>\n</div>\n</div>\n</div>\n</div>\n</div>\n</div></div></div><div class="fe-block fe-block-01c388b9750b343b6631"><div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block" data-block-type="1337"><div class="sqs-block-content"><div class="sqs-text-block-container">\n<div class="sqs-html-content" data-sqsp-text-block-content><p style="text-align:center;white-space:pre-wrap;" class="sqsrte-large">Postavte systém, který pomůže oddělením nukleární medicíny efektivně řídit použití radiofarmak.</p><p class="" data-rte-preserve-empty="true" style="white-space:pre-wrap;"></p></div>\n</div>\n</div></div></div>\n<h2 style="text-align:center;white-space:pre-wrap;">Ceny</h2>\n</body></html>',
    # upol: 4333 bytes
    'upol': '<html><body>\n</div>\n<div class="elementor-element elementor-element-7765da9 e-con-full elementor-hidden-desktop elementor-hidden-tablet elementor-hidden-mobile e-flex e-con e-child">\n<div class="elementor-element elementor-element-5f1548a scroll-animation-from-top elementor-widget elementor-widget-heading">\n<h2 class="elementor-heading-title elementor-size-default">letošní témata k řešení:\u200b</h2> </div>\n<div class="elementor-element elementor-element-e355601 e-grid e-con-full scroll-animation-stagger e-con e-child">\n<div class="elementor-element elementor-element-dcf742d e-con-full scroll-animation-from-bottom e-flex e-con e-child">\n<div class="elementor-element elementor-element-98077d3 elementor-widget elementor-widget-heading">\n<span class="elementor-heading-title elementor-size-default">Monitoring a predikce dostupnosti parkovacích kapacit v Olomouci\u200b</span> </div>\n</div>\n<div class="elementor-element elementor-element-510c011 e-con-full scroll-animation-from-bottom e-flex e-con e-child">\n<div class="elementor-element elementor-element-441104e elementor-widget elementor-widget-heading">\n<span class="elementor-heading-title elementor-size-default">AI dotazování na senzorickými živými daty\u200b</span> </div>\n<div class="elementor-element elementor-element-48097a4 elementor-widget elementor-widget-heading">\n<span class="elementor-heading-title elementor-size-default"><span data-metadata=""></span><span data-buffer=""></span>cena EnCLOD</span> </div>\n</div>\n<div class="elementor-element elementor-element-a057a4a e-con-full scroll-animation-from-bottom e-flex e-con e-child">\n<div class="elementor-element elementor-element-70a8cfd elementor-widget elementor-widget-heading">\n<span class="elementor-heading-title elementor-size-default"><span data-metadata=""></span><span data-buffer=""></span>Digitální nástroj na městské tepelné ostrovy</span> </div>\n<div class="elementor-element elementor-element-9e1503a elementor-widget elementor-widget-heading">\n<span class="elementor-heading-title elementor-size-default"><span data-metadata=""></span><span data-buffer=""></span>cena EnCLOD</span> </div>\n</div>\n<div class="elementor-element elementor-element-e386972 e-con-full scroll-animation-from-bottom e-flex e-con e-child">\n<div class="elementor-element elementor-element-dfbf00d elementor-widget elementor-widget-heading">\n<span class="elementor-heading-title elementor-size-default"><span data-metadata=""></span><span data-buffer=""></span>Vývoj jednoduchého „nabídka × poptávka“ nástroje pro efektivní spolupráci UPOL a města</span> </div>\n</div>\n<div class="elementor-element elementor-element-13f437a e-con-full scroll-animation-from-bottom e-flex e-con e-child">\n<div class="elementor-element elementor-element-cf7f230 elementor-widget elementor-widget-heading">\n<span class="elementor-heading-title elementor-size-default"><span data-metadata=""></span><span data-buffer=""></span>Rozšíření UPlikace o navigaci do školy s integrací dat z pocitových mapování</span> </div>\n</div>\n<div class="elementor-element elementor-element-667fdfa e-con-full scroll-animation-from-bottom e-flex e-con e-child">\n<div class="elementor-element elementor-element-0c09b4e elementor-widget elementor-widget-heading">\n<span class="elementor-heading-title elementor-size-default"><span data-metadata=""></span><span data-buffer=""></span>Vlastní nápad</span> </div>\n</div>\n</div>\n<div class="elementor-element elementor-element-0718f2b elementor-widget elementor-widget-heading">\n<h2 class="elementor-heading-title elementor-size-default">*při řešení projektů podporujeme využítí umělé inteligence (</h2></div></div>\n</div>\n<div class="elementor-element elementor-element-4f1d6d7 e-con-full e-flex e-con e-child">\n<div class="elementor-element elementor-element-880d64c scroll-animation-from-top elementor-widget elementor-widget-heading">\n<h2 class="elementor-heading-title elementor-size-default">letošní témata k řešení:\u200b</h2> </div>\n<div class="elementor-element elementor-element-75cd2d3 elementor-widget elementor-widget-heading">\n<h5 class="elementor-heading-title elementor-size-default">Právě pro vás vymýšlíme nová témata</h5></h5></div></div>\n<h2 class="elementor-heading-title elementor-size-default">20.–22. 11. 2026</h2>\n<div class="elementor-element elementor-element-3253a49 elementor-widget elementor-widget-heading" data-widget_type="heading.default">\n<p class="elementor-heading-title elementor-size-default">Olomoucký kraj</p></div>\n<div class="elementor-element elementor-element-87a2b35 elementor-widget elementor-widget-heading" data-widget_type="heading.default">\n<p class="elementor-heading-title elementor-size-default">Statutární město Olomouc</p></div>\n</body></html>',
    # idea13: 2524 bytes
    'idea13': '<html><body>\n<h3>ainer">\n<h3 class="elementor-heading-title elementor-size-default">Kdy: 18. - 19.9.2026<br>KDE: KD Mlejn</h3> </div</h3>\n<h2 class="elementor-heading-title elementor-size-default">Výzvy</h2> </div>\n</div>\n<div class="elementor-element elementor-element-c9d3adf e-flex e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<div class="elementor-element elementor-element-5971234 e-flex e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<div class="elementor-element elementor-element-78ff650 e-flex e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<div class="elementor-element elementor-element-f7ea75f elementor-widget elementor-widget-heading">\n<div class="elementor-widget-container">\n<h3 class="elementor-heading-title elementor-size-default">Výzva č. 1: Volnočasové aktivity</h3> </div>\n</div>\n<div class="elementor-element elementor-element-fdb15ee elementor-widget elementor-widget-text-editor">\n<div class="elementor-widget-container">\n<p>Jak zpříjemnit volný čas obyvatelům Prahy 13? Navrhněte nové aktivity, služby nebo místa, která propojí sousedy, oživí veřejný prostor a nabídnou smysluplné vyžití dětem, mladým lidem, rodinám i seniorům. Hledáme nápady, které budou dostupné, atraktivní a reálně využitelné v každodenním životě městské části.</p> </div>\n</div>\n</div>\n</div>\n<div class="elementor-element elementor-element-525e239 e-flex e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<div class="elementor-element elementor-element-c708d41 elementor-widget elementor-widget-heading">\n<div class="elementor-widget-container">\n<h3 class="elementor-heading-title elementor-size-default">Výzva č. 2: Rozvoj podnikání</h3> </div>\n</div>\n<div class="elementor-element elementor-element-adb1213 elementor-widget elementor-widget-text-editor">\n<div class="elementor-widget-container">\n<p>Jak vytvořit v Praze 13 lepší podmínky pro podnikatele, živnostníky a nové projekty? Navrhněte služby, nástroje nebo aktivity, které podpoří místní podnikání, propojí podnikatele se zákazníky a pomohou rozvíjet živou a prosperující městskou část.</p> </div>\n</div>\n</div>\n</div>\n</div>\n</div>\n<div class="elementor-element elementor-element-22660af e-flex e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<div class="elementor-element elementor-element-ee3da9d e-flex e-con-boxed e-con e-child">\n<div class="e-con-inner">\n<h2 class="elementor-heading-title elementor-size-default">Časté dotazy</h2>\n<a class="elementor-toggle-title" tabindex="0">Kdo to pořádá?</a>\n<div id="elementor-tab-content-2671" class="elementor-tab-content elementor-clearfix"><p>Ideathon pořádá MČ Praha 13 ve spolupráci s různými partnery.</p></div>\n</body></html>',
    # aimtec: 1550 bytes
    'aimtec': '<html><body>\nh2>\n<p style="text-align: center;">Do kterých výzev se hackeři v roce 2026 pustili?</p>\n<div class="promo">\n<h2></h2>\n<div class="promo__row">\n<div class="promo__col">\n<div class="promo__text">\n<h3>Trénink zraku pro lepší učení</h3>\n<p style="text-align: left;">Práce očí je klíčová pro zvládání čtení, psaní i dalších dovedností u dětí s atypickým vývojem. Naprogramuj hry, které rozvinou zrakové vnímání a schopnost orientace v obraze. Děti se naučí soustředit na konkrétní prvky, rozlišovat tvary, písmena a čísla a sledovat jejich pohyb. Lépe pak zvládnou funkční gramotnost i každodenní motorické úkony.</p>\n</div>\n</div>\n<div class="promo__col promo__col">\n<div class="promo__text">\n<h3>Elektrické vozíky s\xa0DNA motorsportu</h3>\n<p></p>\n<p style="text-align: left;">Spolupracuj na vývoji revolučních sportovních elektrických vozíků. Hardware, testovací prostředí i základní ovládání má <a href="https://www.astrum-mobility.cz/">Astrum Mobility</a> téměř hotové. Přidej software, vylepši ovládání a pomoz zpřístupnit výkon, bezpečnost a zábavu na míru každému uživateli. Pomoz posunout prototyp, který zlepší život lidem na vozíku, do komerční reality.</p>\n</div>\n</div>\n"promo__col promo__col--green">\n<div class="promo__text">\n<h3>Technologie</h3>\n<h3>pro rok 2026</h3>\n<p>Podívej se, jaké technologie můžeš využít v praxi.</p>\n<p><a class="link" href="#technologie">Více o technologiích</a></p>\n<</p></div></div>\n</body></html>',
    # nakopniprahu: 4514 bytes
    'nakopniprahu': '<html><body>\n>\n<h2 class="title points__title animate animate--fall">VÝZVY NAKOPNI PRAHU 2026</h2>\n<div class="points__textbox animate animate--fall">\n<p data-pm-slice="0 0 []">Přidej se k lidem, kteří chtějí Prahu měnit k lepšímu a rozvíjej svůj nápad s podporou města a expertů. Hledáme nápady, které jsou inovativní, proveditelné a přinášejí reálný dopad na město.</p>\n<p><span>Letos se zaměřujeme na tři výzvy: Mobilitu a veřejný prostor, Životní prostředí a Energetiku a budovy. V každé z nich najdeš konkrétní témata, která reflektují aktuální potřeby města. Přihlásit se ale můžeš s jakýmkoliv nápadem, který spadá do jedné z výzev.</span></p>\n<p>Chceš jít víc do hloubky? Využij <span style="text-decoration: underline;"><a style="color: #fff;" href="https://api.golemio.cz/docs/public-openapi/">otevřená městská data</a></span> a postav řešení na reálných informacích o fungování Prahy.</p>\n</div>\n</div>\n<div class="points__list">\n<div class="points-item">\n<h3 class="title points-item__title animate animate--fall">MOBILITA A VEŘEJNÝ PROSTOR</h3>\n<div class="points-item__textbox animate animate--fall">\n<p><strong><span class="TextRun SCXW127654667 BCX0" style="font-size: 22px;"><span class="NormalTextRun SCXW127654667 BCX0">Udržitelný pohyb po městě</span></span></strong></p>\n<p><span style="font-size: 18px;"><span class="TextRun SCXW148074795 BCX0"><span class="NormalTextRun SCXW148074795 BCX0">Každý den se po Praze pohybují miliony lidí – pěšky, na kole, MHD i autem. Jak zajistit, aby byl pohyb po městě plynulý, bezpečný a zároveň šetrný k veřejnému prostoru i životnímu prostředí?</span></span><span class="EOP SCXW148074795 BCX0">\xa0</span></span></p>\n<p><strong><span class="TextRun SCXW66466125 BCX0" style="font-size: 22px;"><span class="NormalTextRun SCXW66466125 BCX0">Městská logistika a udržitelnost</span></span></strong></p>\n<p><span style="font-size: 18px;"><span class="TextRun SCXW229249352 BCX0"><span class="NormalTextRun SCXW229249352 BCX0">Zásobování obchodů, restaurací a dalších podniků je klíčovou tepnou města, která má ideálně zůstat neviditelná. V realitě však často zahlcuje ulice, komplikuje dopravu a zvyšuje emise. Jak dostat zboží do s</span><span class="NormalTextRun SCXW229249352 BCX0">v</span><span class="NormalTextRun SCXW229249352 BCX0">ého cíle bez zbytečných kolon a konfliktů v ulicích?</span></span><span class="EOP SCXW229249352 BCX0">\xa0</span></span></p>\n</div>\n</div>\n<div class="points-item">\n<h3 class="title points-item__title animate animate--fall">ŽIVOTNÍ PROSTŘEDÍ</h3>\n<div class="points-item__textbox animate animate--fall">\n<p><strong><span class="TextRun SCXW233643911 BCX0" style="font-size: 22px;"><span class="NormalTextRun SCXW233643911 BCX0">Město odolné vůči klimatickým změnám</span></span></strong></p>\n<p><span style="font-size: 18px;"><span class="TextRun SCXW247689135 BCX0"><span class="NormalTextRun SCXW247689135 BCX0">Praha se stále častěji potýká s vlnami veder, přehříváním ulic, suchem i extrémními srážkami. Tyto jevy mají přímý dopad na naše zdraví i kvalitu života ve městě.</span></span> <span class="TextRun SCXW247689135 BCX0"><span class="NormalTextRun SCXW247689135 BCX0">Jak zajistit, aby byla Praha odolnější vůči klimatickým výkyvům a dokázala své obyvatele i veřejný prostor lépe chránit?</span></span><span class="EOP SCXW247689135 BCX0">\xa0</span></span></p>\n<p><strong><span class="TextRun SCXW35924600 BCX0" style="font-size: 22px;"><span class="NormalTextRun SCXW35924600 BCX0">Cirkul</span><span class="NormalTextRun SCXW35924600 BCX0">á</span><span class="NormalTextRun SCXW35924600 BCX0">r</span><span class="NormalTextRun SCXW35924600 BCX0">ní město</span></span></strong></p>\n<p><span style="font-size: 18px;"><span class="EOP SCXW45426889 BCX0"><span data-olk-copy-source="MessageBody">Ve městě každý den vzniká velké množství odpadu, přitom mnoho materiálů a výrobků by mohlo zůstat v oběhu a sloužit znovu.\xa0Jak předcházet vzniku odpadu, snížit jeho množství a usnadnit lidem třídění, sdílení a opětovné využívání materiálů a výrobků ve městě?\xa0</span> </span></span></p>\n</div>\n</div>\n<h2 class="title timeline__title">TIMELINE</h2>\n<div><p class="timeline-item__name">27. května 2026</p>\n<p class="timeline-item__subname">Nakopni Finále</p>\n</p></div>\n<article class="faq__item animate animate--fall">\n<div class="faq__item-header">\n<span>11</span>\n<p>Kdo soutěž pořádá?</p>\n</div>\n<div class="faq__item-content">\n<p>Pořadatelem soutěže NAKOPNI PRAHU je Magistrát hlavního města Prahy a jeho městská společnost OICT.</p>\n</div>\n</article>\n</body></html>',
}



# --------------------------------------------------------------------------
# the cases — each returns (ok, message)
# --------------------------------------------------------------------------

def case_guard_refuses(key, label, body):
    reason = hx.guard(key, body)
    return reason is not None, (reason or "ACCEPTED a body that is not this page")


def case_guard_accepts(key):
    reason = hx.guard(key, FIXTURES[key])
    return reason is None, (reason or "accepted")


def rows_and_drops(key, body=None):
    """The pure parser: (rows, {reason: [titles]}) — no stderr."""
    return hx.parse_site_report(key, FIXTURES[key] if body is None else body)


def case_parse(key):
    n, title, owner, edition, ev = EXPECT[key]
    rows, _ = rows_and_drops(key)
    if len(rows) != n:
        return False, f"{len(rows)} row(s), expected {n}: {[r['title'] for r in rows]}"
    for row in rows:
        for f in ("site", "owner", "page_url", "title", "text"):
            if not row.get(f):
                return False, f"required payload field {f!r} empty on {row['title']!r}"
        if len(row["text"]) > 1500:
            return False, f"text {len(row['text'])} chars > 1500"
        if not hx.is_statement(row["text"], row["title"]):
            return False, f"a bare title was staged: {row['title']!r}"
    if n == 0:
        return True, "0 row(s), as measured: every topic line is a bare title"
    r = rows[0]
    got = (r["title"], r["owner"], r["edition"], r["event_date"])
    want = (title, owner, edition, ev)
    if got != want:
        return False, f"first row {got} != {want}"
    return True, f"{n} row(s); first {title!r} / {owner!r} / {edition} / {ev or '-'}"


def case_nakopni_span_join():
    rows, _ = rows_and_drops("nakopniprahu")
    titles = [r["title"] for r in rows]
    want = "Životní prostředí · Cirkulární město"
    return want in titles, (f"{want!r} present" if want in titles
                            else f"split-span title not re-joined: {titles}")


def case_rakathon_owner_is_the_hospital_list():
    rows, drops = rows_and_drops("rakathon")
    want = "FN Motol, Masarykův onkologický ústav, FN Ostrava"
    owners = sorted({r["owner"] for r in rows})
    return owners == [want] and not drops, f"owners {owners}; drops {drops}"


def case_no_organizer_fallback():
    """The same rakathon page with the hospital sentence blanked: under the old
    code every row came out owned by 'Rakathon (…)'. Now none comes out."""
    body = re.sub(r"FN Motol a Homolka|\bMOU\b|Fakultní nemocnice Ostrava", "—", FIXTURES["rakathon"])
    rows, drops = rows_and_drops("rakathon", body)
    if rows:
        return False, f"staged with owner(s) {sorted({r['owner'] for r in rows})} — a fallback is back"
    ok = drops.get(hx.NO_OWNER) == ["Rekurze", "OnkoCapacity"] and hx.BARE_TITLE not in drops
    return ok, f"0 staged; refused {drops}"


def case_label_missing_refused():
    """A hackjakbrno box whose 'Zadavatel:' heading is gone has no owner —
    the organizer's own name is not one."""
    body = FIXTURES["hackjakbrno"].replace("Zadavatel: Masarykův onkologický ústav",
                                           "Partner: Masarykův onkologický ústav", 1)
    rows, drops = rows_and_drops("hackjakbrno", body)
    titles = [r["title"] for r in rows]
    ok = titles == ["AI DocuHelper"] and drops.get(hx.NO_OWNER) == ["StructREP"]
    return ok, f"staged {titles}; refused {drops}"


def case_aimtec_owner_from_paragraph_or_refused():
    rows, drops = rows_and_drops("aimtec")
    owners = [r["owner"] for r in rows]
    refused = drops.get(hx.NO_OWNER, [])
    ok = owners == ["Astrum Mobility"] and refused == ["Trénink zraku pro lepší učení"]
    return ok, f"staged owners {owners}; refused as {hx.NO_OWNER!r}: {refused}"


def case_upol_bare_titles():
    rows, drops = rows_and_drops("upol")
    refused = drops.get(hx.BARE_TITLE, [])
    if rows:
        return False, f"bare topic lines staged: {[r['title'] for r in rows]}"
    if any(t.startswith("cena EnCLOD") or t == "Vlastní nápad" for t in refused):
        return False, f"prize badge or 'Vlastní nápad' counted as a challenge: {refused}"
    if len(refused) != 5 or hx.NO_OWNER in drops:
        return False, f"drops {drops}"
    return True, f"0 staged; 5 refused as {hx.BARE_TITLE!r} (the page names its setters, so not {hx.NO_OWNER!r})"


def case_refusals_reported():
    """The fetcher's summary is a heredoc that calls only parse_site(); the
    count must reach it, and it does so on stderr in the summary's indent."""
    buf = io.StringIO()
    with contextlib.redirect_stderr(buf):
        rows = hx.parse_site("upol", FIXTURES["upol"])
    line = buf.getvalue()
    ok = rows == [] and line.startswith("    upol") and f"refused 5: {hx.BARE_TITLE}" in line
    return ok, (line.strip()[:110] if line else "nothing printed")


def case_contacts_cut():
    """A garant line injected into a real paragraph must not survive staging."""
    # Synthetic on purpose: .invalid cannot resolve and +420 000… is not allocated.
    poison = (" Garant: Jan Novák, jan.novak@example.invalid, tel: +420 000 000 000."
              " Kontakt – Petra Svobodová.")
    body = FIXTURES["idea13"].replace("v každodenním životě městské části.",
                                      "v každodenním životě městské části." + poison, 1)
    rows = hx.parse_site("idea13", body)
    text = rows[0]["text"]
    leaked = [t for t in ("Novák", "@", "+420", "Svobodová", "Garant", "Kontakt") if t in text]
    if leaked:
        return False, f"leaked {leaked} into staged text"
    if hx.EMAIL_RE.search(text) or hx.PHONE_RE.search(text):
        return False, "EMAIL_RE/PHONE_RE still match the staged text"
    return True, "garant, email, phone and contact lines cut; challenge text kept"


def case_ordinal_stable_id():
    """Re-numbering a challenge between editions must not mint a new id."""
    a = rows_and_drops("hackjakbrno")[0][0]
    b = rows_and_drops("hackjakbrno", FIXTURES["hackjakbrno"].replace("1. StructREP", "7. StructREP"))[0][0]
    today = dt.date(2026, 9, 3)
    ia, ib = hx.extract_hack(a, "hack", today)["id"], hx.extract_hack(b, "hack", today)["id"]
    return ia == ib, f"{ia} vs {ib}"


def case_extract_shape():
    today = dt.date(2026, 9, 3)
    item = rows_and_drops("hackjakbrno")[0][0]
    rec = hx.extract_hack(item, "hack", today)
    if rec is None:
        return False, "extract_hack returned None for a good row"
    missing = [k for k in REQUIRED_KEYS if k not in rec]
    if missing:
        return False, f"missing keys {missing}"
    if not ID_RE.match(rec["id"]) or not rec["id"].startswith("hack-"):
        return False, f"id {rec['id']!r} fails ^[a-z]{{2,10}}-[\\w.-]+$ or the hack- prefix"
    if rec["source"] != "hackathon" or rec["evidence_type"] != "asks":
        return False, f"source/evidence_type {rec['source']}/{rec['evidence_type']}"
    if rec["date"] != "2026-09-03" or rec["urgency_date"] is not None:
        return False, f"date {rec['date']} urgency {rec['urgency_date']!r} — an event date is not urgency"
    if rec["quote_parts"][0] != item["title"] or len(rec["excerpt"]) > 400:
        return False, "quote_parts[0] must be the title; excerpt ≤ 400"
    # WHO ASKED: a top-level field equal to the institution the page names.
    if rec["owner"] != "Masarykův onkologický ústav" or rec["entity_native"] != rec["owner"]:
        return False, f"owner {rec['owner']!r} must be the named institution"
    if "notes" in rec:
        return False, "nothing rides on notes: owner is the top-level field (2026-09-03)"
    if rec["sector"] is not None or rec["money_eur"] is not None or rec["money_note"] != "":
        return False, "sector/money must be None/None/'' — a prize is not a budget"
    return True, f"{rec['id']} · owner {rec['owner']} · urgency {rec['urgency_date']!r}"


def case_extract_idempotent():
    today = dt.date(2026, 9, 3)
    item = rows_and_drops("rakathon")[0][0]
    a = hx.extract_hack(dict(item), "hack", today)["id"]
    b = hx.extract_hack(dict(item), "hack", today)["id"]
    return a == b, f"{a} == {b}" if a == b else f"{a} != {b}"


def case_extract_refuses_incomplete():
    today = dt.date(2026, 9, 3)
    item = rows_and_drops("idea13")[0][0]
    bad = [hx.extract_hack({**item, k: ""}, "hack", today) for k in ("site", "title", "owner", "page_url")]
    return all(b is None for b in bad), "site/title/owner/page_url each gate the record; an empty owner is refused, not defaulted"


def case_extract_refuses_bare():
    """A payload row is a file anyone can edit: the extractor re-checks it."""
    today = dt.date(2026, 9, 3)
    item = rows_and_drops("idea13")[0][0]
    same = hx.extract_hack({**item, "text": item["title"]}, "hack", today)
    short = hx.extract_hack({**item, "text": "x" * (hx.MIN_STATEMENT - 1)}, "hack", today)
    edge = hx.extract_hack({**item, "text": "y" * hx.MIN_STATEMENT}, "hack", today)
    ok = same is None and short is None and edge is not None
    v = lambda r: "staged" if r else "refused"  # noqa: E731
    return ok, f"text == title -> {v(same)}; {hx.MIN_STATEMENT - 1} chars -> {v(short)}; {hx.MIN_STATEMENT} chars -> {v(edge)}"


def case_event_date_is_not_urgency():
    """Dated (hackjakbrno, 2026-11-27) and undated (aimtec) alike: the event
    date stays on the payload row as context and never becomes urgency_date."""
    today = dt.date(2026, 9, 3)
    dated = rows_and_drops("hackjakbrno")[0][0]
    undated = rows_and_drops("aimtec")[0][0]
    a = hx.extract_hack(dated, "hack", today)
    b = hx.extract_hack(undated, "hack", today)
    ok = (dated["event_date"] == "2026-11-27" and undated["event_date"] == ""
          and a["urgency_date"] is None and b["urgency_date"] is None)
    return ok, f"event_date {dated['event_date']!r} kept on the row; urgency_date {a['urgency_date']!r} / {b['urgency_date']!r}"


# --------------------------------------------------------------------------

def main():
    cases = []
    for key in hx.SITES:
        cases.append((key, "login page served as the page", lambda k=key: case_guard_refuses(k, "login", LOGIN_HTML)))
        cases.append((key, "maintenance notice served as the page", lambda k=key: case_guard_refuses(k, "503", MAINTENANCE_HTML)))
        cases.append((key, "empty body", lambda k=key: case_guard_refuses(k, "empty", "")))
        # A misrouted CDN serves ANOTHER organizer's page with a 200: every
        # other fixture must be refused by this site's guard, not just one.
        for other in hx.SITES:
            if other != key:
                cases.append((key, f"another organizer's page ({other}) served as this one",
                              lambda k=key, o=other: case_guard_refuses(k, o, FIXTURES[o])))
        cases.append((key, "THE GOOD BODY passes the guard", lambda k=key: case_guard_accepts(k)))
        cases.append((key, "THE GOOD BODY yields what was measured", lambda k=key: case_parse(k)))
    cases += [
        ("nakopni", "title split across inline spans is re-joined", case_nakopni_span_join),
        ("rakathon", "owner is the hospital list the page names", case_rakathon_owner_is_the_hospital_list),
        ("rakathon", "page naming no setter yields nothing — no organizer fallback", case_no_organizer_fallback),
        ("hackjakbrno", "box without a 'Zadavatel:' label is refused", case_label_missing_refused),
        ("aimtec", "owner from the paragraph; no institution named -> refused", case_aimtec_owner_from_paragraph_or_refused),
        ("upol", "bare topic lines refused; badge and own-idea never counted", case_upol_bare_titles),
        ("upol", "parse_site reports refusals on stderr, fetcher-summary shaped", case_refusals_reported),
        ("idea13", "garant / email / phone / contact sentences are cut", case_contacts_cut),
        ("extract", "re-numbered challenge keeps its id", case_ordinal_stable_id),
        ("extract", "extract_hack shape, id pattern, owner, values", case_extract_shape),
        ("extract", "same input, same id, twice", case_extract_idempotent),
        ("extract", "incomplete row is refused (owner included)", case_extract_refuses_incomplete),
        ("extract", "text == title or < MIN_STATEMENT chars is refused", case_extract_refuses_bare),
        ("extract", "event date is never urgency_date", case_event_date_is_not_urgency),
    ]
    width = max(len(c[1]) for c in cases)
    bad = 0
    for feed, label, fn in cases:
        try:
            ok, msg = fn()
        except Exception as e:  # noqa: BLE001 — a crash is a failed case, not a skipped one
            ok, msg = False, f"raised {type(e).__name__}: {e}"
        bad += 0 if ok else 1
        print(f"[{'ok  ' if ok else 'FAIL'}] {feed:12s} {label:<{width}}  -> {msg[:120]}")
    print()
    if bad:
        print(f"SELFTEST FAILED — {bad} case(s) did not behave as the contract promises")
        return 1
    print(f"SELFTEST PASSED — {len(cases)} cases: every wrong body refused, "
          "every good body accepted and staged as measured")
    return 0


if __name__ == "__main__":
    sys.exit(main())
