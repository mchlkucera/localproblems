# The who-pays audit

**Register:** localproblems.org, `data/problems/cz/` · 34 records · read in full 2026-09-03
**Against:** *"pokud tam není jasná odpověď na otázku 'kdo a kolik je za to ochotný zaplatit', tak je to z velké části wishful thinking."*
**Read first:** `CLAUDE.md`, `SCORING.md`, `data/CONVENTIONS.md` (body shape, `build`, `comps`, MONEY), `pipeline/MATCH.md` §9, `SPEC.md` §3.
**No repo file was edited.**

---

# PART 1 — THE WHO-PAYS AUDIT

## How each record was graded

Two questions, asked separately, then combined into one letter.

**(a) WHO.** Is a specific buyer named — a segment with a receipted size, or named institutions — or is it "firms" / "municipalities" / "the companies themselves"?

**(b) HOW MUCH.** Is there a receipted willingness to pay: a price the record cites, a contract the buyer signed, a tender the buyer issued, a subsidy allocation, a comparable's public pricing? Or is the money only *nearby* — a regulation exists, a fine ceiling exists, somebody adjacent spends?

| grade | test |
|---|---|
| **A** | named/sized buyer **and** money moving *from that buyer* for *this product or its manual equivalent* |
| **B** | named/sized buyer, money receipt indirect — a subsidy that funds them, a foreign price, an adjacent contract, a market-size figure |
| **C** | buyer vague or unsized, **or** every money receipt is explicitly for a different product |
| **D** | wishful — no real payer and no amount |

## The table

| id | title (short) | score | grade | the payer (≤8 words) | the amount receipt (≤10 words) | what would move it to A |
|---|---|---|---|---|---|---|
| p-0001 | Energy-community billing | 9 | **A** | Named communities, care homes, hospitals, agencies | 1.0M CZK Františkov; 200k CZK Pardubice hospital [S6,S10] | — (add one CZ vendor's published SaaS price; five sell it, none publishes one) |
| p-0002 | Installer back-office | 6 | **B** | "Hundreds of small installation firms" | Wue 650 Kč/seat/mo + 200 Kč heat-pump module [S6] | A receipted count of CZ heat-pump/PV installer firms; one firm's admin-hours |
| p-0003 | Building-permit navigation | 7 | **A** | 36,300 authorised engineers and architects [S9] | Manual 16,000–42,000 CZK; Průvodka 12,900 CZK [S7,S10] | — (money score 1 understates it; the price receipts are the strongest private ones on file) |
| p-0004 | Care-allowance navigation | 7 | **B** | 374,000 allowance recipients' families [S5] | 41.3bn CZK benefit pot — flows *to* buyer [S5] | One family paying a fee for this; the priced field is 0 CZK today |
| p-0005 | Distributor quote/order entry | 3 | **D** | "Distributors and suppliers" — no count | none | A named wholesaler's re-typing cost, or any CZ vendor price |
| p-0006 | Investment-intermediary compliance | 7 | **B** | Broker Consulting, Partners + "thousands" | AML Proof from 25 CZK/credit — the other half [S4] | ČNB's own register count of intermediaries; one network's consultant retainer |
| p-0007 | Construction subcontractor crews | 6 | **D** | "General contractors and mid-sized firms" | none | A staffing agency's per-hour margin; a contractor's crew-sourcing spend |
| p-0008 | NIS2 implementation capacity | 11 | **A** | ~6,000 entities; 4,825 registered with NÚKIB [S13] | Lexnova 91k CZK ×2; Český Brod 9M CZK; 3,000 CZK/mo [S6,S7,S16] | — (but see caveat: €33M buys implementation, not the compliance product) |
| p-0009 | Employment-card automation | 7 | **C** | Employers hiring abroad — no count | None; record states no provider publishes a fee [S4,S7] | One agency's per-case fee, or one employer's annual immigration spend |
| p-0010 | Trucking back-office | 6 | **B** | ~40,000 hauliers (harvest note, no primary source) | Datatruck $99–500/mo — US, flagged "not a receipt" [S10] | A ČSÚ/ministry carrier count; TruckManager's price (700+ firms, unpublished) |
| p-0011 | Home-care agency ops | 6 | **C** | "Hundreds of agencies" — no count, none named | ÚZIS KOMPAS €5.4M — "state project money" [S7] | One agency's spend on Cygnus DP / VeruApp, or an intake-hours cost |
| p-0012 | EUDR due diligence | 2 | **D** | Wood/coffee/rubber importers — no count | none | Customs count above threshold; any CZ spend |
| p-0013 | Instant payments readiness | 2 | **D** | "Banks, payment and e-money institutions" | none | One institution's SEPA Instant build budget |
| p-0014 | Machinery Regulation cutover | 2 | **D** | Makers, importers, integrators — no count | none | A notified body's fee schedule; one integrator's conformity spend |
| p-0015 | CBAM definitive regime | 2 | **D** | Importers >50 t/yr — no count | none | The customs count the record's own next-move asks for |
| p-0016 | CRA vulnerability reporting | 3 | **D** | Device makers, software houses — no count | None (a €15m fine ceiling is a penalty) | A CZ PSIRT retainer price; one vendor's CRA budget |
| p-0017 | EUDI wallet acceptance | 6 | **C** | Banks, telcos, e-shops — "not published" how many | DIA €78M + MONET+ €8.85M — **the state, not the buyer** [S3,S5] | Bank iD's or Wultra's relying-party price; a count of obliged parties |
| p-0018 | Pay-transparency reporting | 6 | **B** | "150+ employees — thousands of firms" | TREXIMA 79,000 CZK/yr; FORUM 8,499 CZK/yr [S5] | ČSÚ count of 150+ employers; and price against a free state tool (Logib) |
| p-0019 | Battery passport / DPP | 3 | **D** | Carmakers, plants, importers; Škoda named | none | Škoda's supplier-mandate spend, or an AutoSAP statement |
| p-0020 | E-shop accessibility | 4 | **D** | "E-shops, banks, digital services" | None; the enforcement claim failed verification | ČOI accessibility fines; one merchant's remediation quote |
| p-0021 | Data Act compliance | 3 | **D** | Device makers and SaaS vendors — no count | none | One manufacturer's data-access engineering budget |
| p-0022 | Hospital eHealth interoperability | 8 | **A** | 8+ named hospitals and regions [S1–S5] | €7.7M, €5.8M open, €2.8M, 70.9M CZK, €11.7M [S1–S5,S9] | — (money is impeccable; the field is taken, gap 0) |
| p-0023 | AI accounting capacity | 4 | **B** | "Small firms that cannot find an accountant" | Účtárna.ai from 5,000 CZK/mo + 300 CZK/employee [S9] | A count of the CZ accounting profession — the record twice says none exists |
| p-0024 | EPBD retrofit analytics | 7 | **C** | 11 public buyers, named-ish | €58M EPC — "buy the delivery, not the ranking" [S4] | One owner's spend on portfolio triage; Predium/Deepki list price |
| p-0025 | Insulation retrofit execution | 5 | **B** | Homeowners, then SVJ/družstva — unsized | VARM ~€5k (DE); dotacenarenovace 10k+40k CZK [S1,S6] | NZÚ application volume and average grant; a CZ fixed-price quote |
| p-0026 | Water-utility smart metering | 3 | **A** | 7+ named VaK utilities and svazky | €1.2M open, 21.4M CZK, 8.4M CZK, €5,987 pilot [S1–S5,S8] | — (best-receipted money in the register relative to its score) |
| p-0027 | Consumer-credit dispute flood | 7 | **C** | Non-bank lenders and banks — none named | None; money 0, no CZ price anywhere | ČNB's register of non-bank lenders; one lender's outside-counsel cost per case |
| p-0028 | E-shop consumer-law compliance | 9 | **A** | ~30,000 Shoptet merchants [S5] | Hlídač Slev ~19 Kč/mo; Slevy správně 200 Kč/mo; Pravoid 199–499 CZK [S8,S10] | — (harden the 30k merchant count; it rests on a gap-check note) |
| p-0029 | eSSL attestation wave | 7 | **A** | ~19 named public bodies (SÚKL, MV, Lesy ČR…) | €17M/10 weeks; €1.4M open, €3.3M, €642k [S2–S6] | — |
| p-0030 | MiCA CASP wind-down | 4 | **C** | ~175 firms exiting + 11 licensees [S2,S5] | None; record states no CZ price is published [S6] | One wind-down engagement quote; one licensee's compliance-ops budget |
| p-0031 | Municipal PV procurement | 7 | **C** | 53 public buyers, several named | €60M — **buys the panels, not the pooling** [S1] | eCENTRE's or SMS ČR's fee for a pooled purchase; iChoosr's take rate |
| p-0032 | Residential care placement | 8 | **C** | Care homes + families — neither named nor counted | 9.5bn CZK — **construction, not placement** [S8,S9,S10] | A CZ home's referral fee, or a family's willingness at a stated price |
| p-0033 | Care-workforce shift marketplace | 8 | **C** | 625 facilities, 262 employers [S3,S4] | €10.8M — **the buyers' wage bill, not a fee** [S4] | A staffing agency's per-shift rate and mark-up (quotable; not on file) |
| p-0034 | AI Act adaptation gap | 5 | **D** | "Czech companies using AI" — no count | None; record states no budget is claimed | PwC / AIshield / Brain list prices; one firm's audit invoice |

## The distribution

| grade | all 34 | live 26 (excl. 8 rejected) |
|---|---|---|
| A | 7 | 7 |
| B | 7 | 7 |
| C | 9 | 9 |
| D | 11 | 3 |

All eight `status: rejected` records are D. That is the quality gate working — the 2026-08-24 rejection pass removed exactly the records the critique would have removed. The live corpus is not the problem the critic is describing.

But: **only 7 of 26 live records answer both halves of the question.** Nine are C — a named or sized buyer attached to money that is demonstrably in someone else's pocket, or a defensible buyer attached to no amount at all.

---

## The register's honest weakness

### 1. MONEY does not measure willingness to pay. It measures proximity to a public budget.

The ladder reads, in full:

> 0: none · 1: relevant tender/grant exists · 2: OPEN tender or grant >= ~5M CZK, or recurring annual spend

Nothing on that ladder asks *whose pocket* the money leaves, or whether it buys *this product*. `SCORING.md` names the dimension "is budget attached?" — and budget-attached and buyer-will-pay are two different questions.

The evidence that this is a real defect, not a semantic one, is in the register's own source notes. Of the **eight** records at `money: 1`, **six say "adjacent" in their own notes**:

- p-0003 — "adjacent spend, held below 2 (not an open tender a navigation vendor can win)"
- p-0004 — "Adjacent spend: kept at money=1, not 2"
- p-0011 — "held below 2 because it is state project money, not an open tender a builder can win or agency purchasing budget"
- p-0024 — "adjacent execution spend… the tenders buy EPC delivery, not the portfolio-analytics layer this record is about"
- p-0032 — "Adjacent capacity spend, not budget for a placement product"
- p-0033 — "adjacent to a staffing product, so money held at 1"

`money: 1` means, in six of eight cases, **money is near this problem** — which is precisely the phrase the critic used. The register knows it, writes it down, and then prints a number that does not carry the caveat.

And it is not confined to rung 1. Two records at `money: 2` score there on spend by a party who is not their buyer:

- **p-0017** — €78M (DIA's wallet client tender) + €8.85M (MONET+'s ICS contract). Both are the state building the wallet that the record's buyer will be obliged to accept. No relying party has paid anyone anything on this record, and the record admits it cannot even size them: *"How many businesses the acceptance duty covers is not published."*
- **p-0031** — €60M across ~80 rooftop-solar procurements. Every crown of it buys panels. The record proposes a *pooling operator*, and its who-pays paragraph is honest to the point of self-refutation: *"municipalities pay in procurement overhead and failed procedures."* They pay in officer-hours. There is no line item, and no fee is on file from either company shaped like the answer (eCENTRE, SMS ČR).

Meanwhile **p-0028 — the best bottom-up money argument in the register — scores `money: 0`**, because three published Czech prices, a German price band, an explicit revenue calculation and 13.0M CZK of realised fines are none of them a public tender.

**By this register's own rule #1 — one field, one meaning — MONEY is carrying two questions and should be two fields.** This is the same defect class already fixed three times: the gap condition inside PROOF rung 2, "not checked" inside GAP rung 0, and `locals[].status`. The critic found the fourth instance, from outside, in one paragraph.

### 2. The best willingness-to-pay receipts in the register are filed in the wrong column.

Fourteen Czech price points sit in the corpus right now:

| record | price on file |
|---|---|
| p-0001 | 1.0M CZK / ~200k CZK per sharing-administration contract |
| p-0002 | Wue 650 Kč/seat/mo + 200 Kč heat-pump module |
| p-0003 | permit engineering 16,000–42,000 CZK; Průvodka 12,900 CZK / 29,900 CZK per month |
| p-0006 | AML Proof from 25 CZK/credit |
| p-0008 | Lexnova ~91k CZK; NIS2 Průvodce 3,000 CZK/mo; Compligen 29,900 CZK; NIS2 Doku 4,900 CZK |
| p-0018 | TREXIMA 79,000 CZK/yr (55,000 benchmarking only); FORUM 8,499 CZK/yr |
| p-0023 | Účtárna.ai 5,000 CZK/mo + 300 CZK/employee |
| p-0025 | dotacenarenovace.cz 10k CZK deposit + 40k on approval |
| p-0028 | Hlídač Slev ~19 Kč/mo/1,000 products; Slevy správně 200 Kč/mo; Pravoid 199–499 CZK |

**Every single one was found by a gap check.** And `data/CONVENTIONS.md` maps `gap-check` → `gap`. So a Czech vendor's published price — the most direct answer to "kolik je někdo ochotný zaplatit" that this register possesses — backs the *local-competition* score and contributes nothing to *money*.

The answer to the critique is already in the building, in the wrong column, and no ladder reads it.

### 3. The register's open fields are exactly its unpriced fields — and that is structural.

Six records carry `gap: 2` (checked, and nobody local sells this): **p-0004, p-0007, p-0009, p-0027, p-0031, p-0033.**

Their grades: **B, D, C, C, C, C.** Not one of the six carries a Czech price for the product it proposes.

This is not sloppiness. It is arithmetic. A gap check learns a price only when it *fails* to find an absence — the price comes off the incumbent's own page. So:

> **The register can only learn what a Czech buyer pays in markets it has just discovered are occupied.**

Where the field is open, the corpus is mute on money by construction. Where it is closed, the corpus has the price and the record scores `gap: 0` or `1`. The critic's question and the register's best score are in tension by design.

There is a way out and two records already demonstrate it: **price the manual equivalent.** p-0001 does it (1.0M CZK for a sharing administration done by hand); p-0003 does it (16,000–42,000 CZK for permit engineering done by hand). Both are grade A on this axis and neither needed an incumbent SaaS to get there. Every other record could do the same and does not:

- p-0033: what a Czech staffing agency charges a care home per shift, and its mark-up — quotable in a phone call, and MPSV licenses the agencies.
- p-0027: what a non-bank lender's outside counsel bills per financial-arbiter case.
- p-0009: what a relocation agency charges per employee card — nine providers, none publishing, all reachable.
- p-0031: the officer-hours cost of one failed municipal solar tender at Špindlerův Mlýn, which has now run four procurement actions on one site.
- p-0032: what a private Czech care home would pay per move-in.

That is five phone calls, not a new feed.

### 4. Two records have a documented price of zero — and no field can say so.

- **p-0004.** Registered social counselling (Rodinný průvodce) writes care-allowance appeals **free**; Moravskoslezský kruh runs a free legal line; pece.cz is a free insurer-run calculator. A free, state-registered incumbent is affirmative evidence *against* willingness to pay, not merely absence of evidence. The record scores `gap: 2` — OPEN — because none of them sells this, which is correct on the gap ladder and misleading on the money one. Its `build.first_revenue: weeks` is the most optimistic claim in the register.
- **p-0018.** MPSV and the labour inspectorate distribute the Logib self-audit tool **free**, and SÚIP inspects with it. A competitor priced at zero *and* holding the enforcement instrument. The record has excellent price receipts (79,000 CZK, 8,499 CZK) and a free substitute, and the score cannot net them.

p-0029 has the same structure at the bottom of the market (OSS Alliance, free, Interior-Ministry-backed) but survives it, because the paid tier is receipted at ~€17M in ten weeks.

### 5. `build.first_revenue` is a willingness-to-pay claim judged from vibes.

Six records claim `first_revenue: weeks`. Two have prices (p-0002, p-0028). Three do not:

- **p-0004** — `weeks`, against a field that gives the service away free.
- **p-0030** — `weeks`, against the record's own sentence: *"No Czech firm publishes a price for either job [S6], so no revenue figure is claimed."*
- **p-0032** — `weeks`/`kiosk`, with no price from either of its two proposed payers, in either currency.

`first_revenue` is the only field in the schema that *is* an answer to "how soon will someone pay", and `data/CONVENTIONS.md` requires it to be "judged honestly from the record's own evidence, never aspirationally." On these three it is not.

### 6. The pipeline can only see money that moves through the state.

`ted`, `hlidac`, `smlouvy`, `nen`, `dotace` — every feed in the `tenders` evidence type is public procurement. `bootstrapped` is RESERVED and empty. There is no feed anywhere in `data/feeds.json` that observes a private price.

This is the *same* corpus blindness `data/CONVENTIONS.md` already documents for competitors — "the corpus cannot see the competition… they never raised, so no funding feed carries them; they sell to private buyers, so no tender names them" — transposed onto money. The register cannot see a Czech SMB paying 650 Kč a month. It only ever learns that number by accident, during a Czech-language search, in a market it must then mark as taken.

---

## Where the critique lands hardest

Ranked, worst first.

**1. p-0032 — Residential care placement · score 8 (STRONG, newsletter-lead material) · grade C.**
Two proposed payers. Neither is named. Neither is counted. Neither is priced. The 70,209 + 37,849 unmet applications are a demand index the record itself insists is not a headcount. The receipted money — Brno's 5.17bn CZK concession, Praha 14's 4.37bn CZK, the 1bn CZK NPO call inside a 9.5bn CZK component — is **construction**, and the record says so: *"Adjacent capacity spend, not budget for a placement product."* Both foreign comps are provider-paid and neither's fee is on the record. The one direct local player, SrovnejPéči.cz, monetises provider listings at an undisclosed price. And it carries `first_revenue: weeks`. On the critic's question this record has no answer at all, and it is scored one point above p-0003, which has two.

**2. p-0033 — Care-workforce shift marketplace · score 8 (STRONG) · grade C.**
Same sweep, same date of creation, same defect. The demand receipts are excellent (3,000+ missing workers across 625 surveyed facilities; 262 employers, 380 nurse vacancies in one month). The money receipt is **the buyers' own payroll**: "an annualised wage floor of €10.8 million… a matching fee on a fraction of that flow is the business." That is a take rate on someone else's wage bill, asserted. The record's own gap check states that sestrycz.eu and the agencies publish "no per-shift price… anywhere". Královéhradecký kraj's €2.19M is personal-assistance capacity, "adjacent to a staffing product". The whole revenue model rests on an agency mark-up nobody has measured — and it is measurable in an afternoon.

**3. p-0031 — Municipal PV procurement · score 7 · grade C.**
€60M receipted across 53 named public buyers, and not one crown of it for the product. The buyers pay in staff time and failed procedures. Three gap checks were run to establish that nobody sells the pooling, and the only company shaped like the answer (eCENTRE, pooling electricity and gas for hundreds of towns since 2006) does not disclose what it charges for the commodity it *does* pool. Getting that number would move the record from C to A in one call.

**4. p-0027 — Consumer-credit dispute flood · score 7 · grade C.**
The finest demand receipt in the register — 2,660 → 5,683 → 12,050 filings, 8,200 more by May 2026, 167-day proceedings, 83% settling, corroborated by two independent official sources — attached to nothing on the money side. `money: 0`. No lender named. No count of non-bank lenders (ČNB publishes one). No price anywhere: aCompliance publishes none, ten Czech law-office vendors publish none, Casap and ClaimSorted are foreign with no pricing on file. Pain is proven; payment is assumed.

**5. p-0007 — Construction subcontractor crews · score 6 · grade D.**
The only live `candidate` graded D. The who-pays paragraph is two clauses of assumed pricing — "charged per crew hired and per worker paid… the marketplace side earns on the match and the document check; the payroll side is a monthly fee per worker" — with a receipt behind neither. `money: 0`. No count of general contractors. Nine local players recorded, all adjacent, none priced. It reads better than it is because `gap: 2` was earned on a genuinely well-run controlled check, and gap 2 renders as OPEN.

**6. p-0017 — EUDI wallet acceptance · score 6 · grade C.**
€87M of receipted state spend, none of it from a relying party, and the record cannot size its own buyer. The clearest single illustration that `money: 2` measures the wrong thing.

---

## Do the top-scored records survive? (p-0008, p-0001, p-0028, p-0022, p-0032, p-0033)

**Four survive. Two do not — and the two are the newest.**

**p-0008 (11, PRIME) — survives, grade A, with one caveat printed.** Named buyers at every size (Domov pro seniory Napajedla, Český Brod at 7,000 inhabitants, Boskovice, FN Motol, ČEZ Distribuce, Česká televize, NAKIT, Mendelova univerzita); the smallest tier ordering a productised 91k CZK package **twice in weeks**; four Czech products with published prices from 4,900 CZK to 3,000 CZK a month; a €99.6M subsidy pot with a 17 December 2026 deadline; and towns paying 121k CZK just to write the grant application. This is the register at its best.
*Caveat the record should print:* the ~€33M of public awards buys SIEM, EDR and monitoring **implementation**, not compliance software — the record's own first move says "sell the doing, not the documents." The 91k CZK package and the 3,000 CZK subscription price the *proposed* product, and they are two orders of magnitude smaller. "Who pays" currently sets both figures in one paragraph without separating the two markets.

**p-0001 (9) — survives, grade A, the cleanest example in the register.** A named buyer paid a named price (1.0M CZK) for the *manual version of exactly this product*, and a second named buyer paid ~200k CZK for the same, inside a wave of 37 filed contracts, with a 1bn CZK fund behind the buyers until 2027. The First moves even instruct the builder to price under it. This is the template the other 25 live records should copy.
*Honest limit:* the 1.0M CZK is a services contract, so the service-to-SaaS conversion is an assumption; and five Czech vendors sell the software with no published price between them.

**p-0028 (9) — survives, grade A, and it is the register's best bottom-up money argument.** A sized buyer base (~30,000 Shoptet merchants), three published Czech prices for adjacent slices of exactly this product, a German price band from twenty-year-old businesses, an explicit revenue estimate (~€430k/yr at €12 × 10%), and 13.0M CZK of realised ČOI fines as the cost of not buying. It scores `money: 0`.
*Two things to print:* the 30,000 merchant count is cited to a gap-check note, and the record's own 2026-08-20 audit cut a Shoptet merchant count for having no receipt. And the enforcement expected-value is thin — 751 inspections against ~30,000 merchants is roughly a 2.5% chance per year per shop, which is why "most of them already ignore the risk" is in first move 2. The record says so, to its credit.

**p-0022 (8) — survives, grade A, on the strongest procurement evidence in the register.** Eleven separate award or tender values, from ~€206K to ~€11.7M, from named hospitals and regions, for exactly this layer, inside a single summer. Nothing about the critique touches it.
*What does touch it:* `gap: 0` with seven established direct sellers, and the money is already spoken for.

**p-0032 (8) — does not survive.** See above.

**p-0033 (8) — does not survive.** See above.

**The pattern is not random.** p-0032 and p-0033 were both `created: 2026-08-25`, both minted from the elder-care deep sweep, and both fail the same way: a large, real, receipted *public* spend on a *different* product, plus a revenue model — per move-in, per shift filled — that nobody in Czechia has priced. The sweep produced excellent demand evidence and skipped the money question entirely, and the scoring ladder had no way to notice, because `money: 1` is exactly what "adjacent spend" earns.

---

## The one-sentence version

> The register is rigorous about *whether the problem is real* and rigorous about *whether the field is open*, and it has no instrument at all for *whether the buyer will pay* — so it scores public-budget proximity instead, calls it MONEY, and files the fourteen Czech prices it does hold under GAP.

---
---

# PART 2 — THE "GRAVEYARD" SIGNAL

## (1) What these sources contain, and whether they are fetchable

### startupgraveyard.io — **rich, and closed to us in writing**

- WordPress, server-rendered, ~234KB homepage, `wp-sitemap.xml` published. Community-submitted with a pending-review moderation step. Returns **HTTP 200** to a browser user-agent; `WebFetch` gets **403** (Cloudflare UA filtering).
- **`robots.txt` is decisive.** It carries a Cloudflare-managed content-signal block:
  - `User-agent: *` → `Content-Signal: search=yes, ai-train=no, use=reference`
  - and then explicit `Disallow: /` for **`ClaudeBot`**, `GPTBot`, `CCBot`, `Google-Extended`, `Applebot-Extended`, `Amazonbot`, `Bytespider`, `meta-externalagent`, `CloudflareBrowserRenderingCrawler`.
  - Plus: *"ANY RESTRICTIONS EXPRESSED VIA CONTENT SIGNALS ARE EXPRESS RESERVATIONS OF RIGHTS UNDER ARTICLE 4 OF … DIRECTIVE 2019/790"* — an explicit EU text-and-data-mining opt-out.
- `data/feeds.json` requires an `access` verdict (`allowed` / `conditional` / `unknown` are the values in use). The honest verdict here is **none of those** — it is refused, by name, for the agent that would run the scan. A human reading the site in a browser is fine; an ingest script is not.
- No API, no dataset, no RSS beyond WordPress defaults.

### failory.com — **the one that actually works**

- `robots.txt`: `Allow: /`, with only `/author/`, `/get/`, `/startup/` disallowed. **`/cemetery/` is permitted.**
- No terms-of-service page exists: `/terms`, `/terms-of-service`, `/legal`, `/privacy-policy` all return **404**; only `/privacy` returns 200. So there is no explicit contractual prohibition — only robots, which permits it.
- Entries are **server-rendered HTML at `/cemetery/<slug>`** and genuinely structured. Pulled live from `/cemetery/beepi`, the labelled fields are:
  `Category · Country · Started · Business Failure Outcome (Acquired | Bankruptcy | Shut Down | Still Active) · Cause (closed 16-value vocabulary) · Closed · Number of Founders · Names of Founders · Number of Employees (banded) · Number of Funding Rounds · Total Funding Amount · Number of Investors`, plus narrative "What was X?" and "Why did it fail?" sections.
- Scale: `/cemetery` ≈ 120 entries, `/failures` "+400", `/graveyard` "+200 analyses". Coverage is overwhelmingly US/UK consumer internet, 2010–2020. **Czech entries: effectively none.**
- Third parties already sell scrapers for it (e.g. a Thunderbit template). That is a signal about ease, not a permission.

### CB Insights post-mortem list — **authoritative, gated**

- 483 post-mortems through May 2024, actively maintained; the most recent instalment covers Oct 2023 – May 2024 and includes Olive ($850M), Convoy ($836M), Hyperloop One ($472M).
- Full detail requires a CB Insights login or free trial. No CSV/Excel export. Usable as a **human reading list**, not as a feed.

### Crunchbase closed companies — **paywalled, as expected**

`operating_status: closed` is a paid-tier facet and the API is commercial. Noted and excluded.

### Others found

| source | what it is | usable? |
|---|---|---|
| `mentalium.me` — 542 dead mental-health companies, 2000–2026, 18 coded fields, CSV + JSON | the *shape* that would work: narrow, coded, downloadable | 403 to WebFetch; described from search results only, unverified |
| `github.com/brookr/Startup-Graveyard` — `tombstones.csv` | small, stale | marginal |
| `autopsy.io` | 1KB response — effectively dead / JS shell | no |
| `loot-drop.io` — "1100+ failed startup case studies" | commercial product | no |
| `startupgraveyard.africa`, `.co`, `thestartupgraveyard.com` | unrelated projects sharing the name | no |

**Summary of (1):** the famous source is robots-blocked to us and its data is unaudited community submissions; the authoritative source is paywalled; the one that is both structured and permitted is Failory, and it is ~120–400 US/UK companies from the 2010s with essentially zero Czech coverage.

## (2) How it would fit the evidence architecture in `SPEC.md` §3

**Not `funded`.** That type is "companies founded/financed", and `arbitrage` → `proof`. A dead company is the *negation* of the proof signal. Filing a shutdown under `funded` would let a death lift `proof` — the exact one-field-two-meanings defect the register has already fixed three times.

**Not the reserved `bootstrapped`.** `CONVENTIONS.md` reserves it for "indie-hacker/revenue signals" — a *living* revenue observation. A graveyard record is neither funded nor bootstrapped; it is a *former* company.

So it needs a **new evidence type**, and the 8-step checklist applies in full:

| step | what it costs here |
|---|---|
| 1. `data/CONVENTIONS.md` | add `graveyard` to the type list, name its feed, add the id-prefix rule |
| 2. `data/feeds.json` | one entry with `evidence_type: graveyard`, an `access` verdict and a `contract`. **Build-enforced** — every `source` value in `data/signals/**` must be claimed by a registry row |
| 3. `data/signals/graveyard/` | nothing — created on first append |
| 4. `web/lib/data.ts` `EVIDENCE_TYPES` | one line, lights up the route |
| 5. `web/app/signals/[type]/page.tsx` | `TITLES` + `DESCRIPTIONS`. **TypeScript-enforced** — step 4 without step 5 fails the build |
| 6. `SignalSchema.source` enum | widen **in a commit before the first record lands**, never in the same one |
| 7. `SPEC.md` §3 layout, §5 route table, §5 nav; the design skill | prose |
| 8. `data/feed_health.json` | nothing — appears PENDING on first health export |

**id prefix:** `grave-<company-slug>`, e.g. `grave-yeloha`, `grave-homejoy`. Native id, stable, and keyed on the *company* rather than the URL — the same reasoning that gave `mpsv-` an aggregate key rather than a posting hash. One dead company appears in Failory, CB Insights and startupgraveyard under three URLs and one name; keying on the company defeats the triple-count, and the identity-key dedup axis in `scripts/normalize.py` handles the rest.

**`source` value:** **`failory`**, not `graveyard`. `CONVENTIONS.md` is explicit that `source` is *fetch provenance* and that "a new value is for a new publisher, not a new script" — and the register has already burned itself on exactly this (`smlouvy` kept its own prefix rather than reusing `hlidac`, because "a record pulled from data.smlouvy.gov.cz that says `hlidac` is a false receipt"). If a second publisher is ever added it takes its own value.

**`dims` mapping — and this is where the type earns or loses its place.** A graveyard record backs **nothing on the scorecard**:

- not `proof` — a dead company is not "an established solution running elsewhere", and PROOF has no negative rung;
- not `demand` — a company having existed is not documented pain (the register already killed the v1 proof test for precisely this: *"Existence is not information. Maturity is."*);
- not `money` — a shutdown is not a budget;
- not `urgency` — if a date exists, it belongs to the *why-now* source, not to the graveyard record;
- not `gap`.

So a `graveyard` signal is `dims: []` — a **context receipt**, exactly like the register's existing VeKLEP drafts, EC consultations and republished tenders. It renders and moves no number. That is not a defect (the register has that category and uses it well), but it must be said out loud when the type is introduced: **this buys reading, not rank.**

## (3) Receipting "the times moved" objectively rather than as vibes

The register already owns the machinery: this is the `urgency` deadline sub-score, and its discipline is that a date must come from an instrument. So the rule should mirror the two invariants already in `scripts/check-records.py` (`gap` needs a `gap-check` with `queries[]`; `proof >= 1` needs a comp):

> **Proposed invariant.** A record citing a `graveyard` source must carry at least one other source of type `regulation`, `tender`, `contract`, `subsidy` or `statistic`, **dated after the cited company's shutdown year**, whose note names the changed condition. A `graveyard` source standing alone fails the build.

Admissible shapes of "what changed", each with a citable form:

| the shift | what a receipt looks like | already in this register |
|---|---|---|
| a rule changed | a dated instrument in e-Sbírka / EUR-Lex, with the article | `reg-eru-sdileni-132-2026`, `reg-efti-freight`, `reg-eidas2-eudi-wallet` |
| a closed market opened | the state register or data hub that did not exist then | EDC opening to electricity sharing, Aug 2024 |
| a platform or API now exists | the vendor's own dated launch or spec version | OIDC4VCI / SD-JWT in the EU wallet reference framework |
| a cost curve crossed | two dated observations of the same series | **none — the one shape the register cannot currently receipt** |
| penetration crossed a threshold | a dated official statistic | NÚKIB's 4,825 registrations; ČSÚ's 80+ projection |
| public money now pays for it | a call with an allocation and a deadline | IROP 120 (€99.6M, 17 Dec 2026), KOMUNERG (1bn CZK), RES+ |

**And the clause that matters most:** the changed condition must be *the one that killed the company*. Yeloha died of two things — project financiers would not fund third-party-owned residential solar, and every US state was a separate regulatory build. A Czech "why now" citing the 2024 legalisation of sharing answers the second and is silent on the first. So the why-now note must state **which recorded cause it answers and which it does not**. Failory's `Cause` field is a closed 16-value vocabulary, so the *shape* of that claim is machine-checkable even where its truth is not.

## (4) The failure mode, and the filter that keeps it from being noise

**The failure mode.** Most dead startups died of causes that have not changed and never will: no market, unit economics that scaled linearly, a founder split, a funding winter. Failory's own cause vocabulary is dominated by *Multiple Reasons*, *Bad Business Model*, *Lack of Funds*, *Mismanagement of Funds*. A feed ingesting those produces a stream of plausible-sounding ideas with a built-in survivorship story — and the materiality filter (`money <= 1 AND scale <= 1 AND urgency == 0`) would then drop nearly all of them while appearing to run correctly, which is the exact failure `CONVENTIONS.md` predicts for a per-posting `hiring` feed.

There is a second, worse problem, specific to this register. Every other feed is an **observation** — a notice, a contract, a statute, a vacancy count. A graveyard record is an **inference**: a company in another country a decade ago, plus a narrative about why now. "The times have moved" is the single easiest sentence in the world to write without a receipt, and this register's own error log is a list of exactly that failure mode: 40 corrections, half its absence claims false on re-check, invented product names, an invented "Lex OZE III". Adopting an inference-shaped source is the highest-variance thing it could do.

**The filter, as rules rather than judgment:**

1. **Cause must be exogenous and dated.** Admit only shutdowns whose recorded cause is a condition *outside the company* — regulation forbade it, infrastructure did not exist, an input cost was prohibitive, the platform was absent. Reject *bad business model*, *mismanagement*, *lack of funds*, *founder conflict*, *competition*, *poor product-market fit*. On Failory's vocabulary that whitelists perhaps 3–4 of 16 causes and cuts the corpus by an order of magnitude. Good.
2. **The changed condition must be named, dated, and post-date the shutdown.** Build-enforced per §3 above.
3. **The changed condition must be Czech, or carry a Czech instrument.** "Mobile penetration rose" is not a receipt. "vyhláška 132/2026 Sb. removes the three-ORP limit from 1 September 2026" is.
4. **The buyer must be re-derived, never inherited.** The dead company's buyer is not evidence about the Czech buyer. A graveyard record supplies **neither WHO nor HOW MUCH** — see Part 1. It supplies a hypothesis and a list of causes to test.
5. **A gap check still costs what it costs.** If the times moved for you they moved for everyone, and a local vendor probably noticed the same statute. On p-0001, five Czech vendors appeared within two years of the rule change; on p-0034, three appeared within *weeks* of the duty landing.
6. **Cap the volume.** The register's own rule for `suggest` / `reddit` — no single feed may dominate a ledger. A graveyard scan producing more than a handful of records a month would be manufacturing, not finding.

## (5) Five concrete dead ideas, three lines each

**1. Yeloha** — Boston, 2014 – May 2016; $3.5M Series A, April 2015.
- *What it was:* a peer-to-peer "solar sharing network" — hosts lent their roofs, subscribers without suitable roofs bought the output.
- *Why it died then:* it could not get banks or solar funds to project-finance third-party-owned hosted systems; each new US state was a fresh regulator; and the 2016 VC retreat from solar after SunEdison's bankruptcy closed the equity route. (Founder's own post-mortem, "Lights Out for Yeloha".)
- *What changed by 2026:* sharing electricity between unrelated parties became legal in Czechia only in 2024 under Lex OZE II, over the state EDC data hub; from **1 September 2026** vyhláška **132/2026 Sb.** removes the three-ORP territorial limit and extends allocation to groups of up to 100 supply points; **Modernizační fond KOMUNERG 1/2025 holds 1bn CZK** for communities until **31 December 2027**. Two of three killers answered by Czech instruments — but not the financing one, and p-0001 already shows five Czech vendors in the space.

**2. Microsoft HealthVault** — 2007 – **20 November 2019**.
- *What it was:* a patient-held personal health record with an app-and-device ecosystem writing into it.
- *Why it died then:* no obligation on any provider to put data in it, no viable business model, and device integrations (Fitbit) fell away — a network good with neither a mandate nor a payer.
- *What changed by 2026:* **EHDS, Regulation (EU) 2025/327**, makes exchangeable records a legal end state — cross-border patient summaries and ePrescription from **March 2029**, imaging/labs/discharge from **2031**, implementing acts due **March 2027**, with conformity duties landing on the vendor ecosystem. Czech hospitals are buying the plumbing one at a time: 8+ public buyers, ~€17M+ in a single summer (p-0022). The "no mandate" cause is genuinely answered by a dated instrument — and the Czech field already has seven established direct sellers and `gap: 0`.

**3. uPort (ConsenSys)** — 2016 – 2021; libraries deprecated **1 May 2021**, hosted infrastructure switched off **1 June 2021**; the framework survives as Veramo, donated to DIF.
- *What it was:* self-sovereign identity — an Ethereum identity contract, a mobile wallet, and JWT verifiable credentials.
- *Why it died then:* it shipped issuance and a wallet before any relying party had a reason to ask for a credential; every integration cost the user a consumer app download; and it lived on ConsenSys funding with no P&L to defend when the group reorganised around MetaMask and Infura.
- *What changed by 2026:* **eIDAS 2.0, Regulation (EU) 2024/1183**, creates the reason to ask — every member state offers a wallet by end-2026 and regulated sectors must **accept** it during 2027; the Czech state is paying for the rails (DIA's ~€78M client tender, MONET+'s 221M CZK ICS contract). The demand-side cause is answered by statute, exactly — which is why the Czech position closed fast: p-0017 records Bank iD (5.3M users) and Wultra already selling it.

**4. Convoy** — Seattle, 2015 – **19 October 2023**; ~$900M raised, ~$3.8bn peak valuation; technology and IP acquired by Flexport, November 2023.
- *What it was:* digital freight brokerage — algorithmic matching of shippers to carriers.
- *Why it died then:* an "unprecedented freight market collapse" plus dramatic monetary tightening, in a brokerage take-rate business whose margin evaporated with spot rates, and no acquirer at scale after four months of trying.
- *What changed by 2026:* **not the freight cycle.** The *document* layer changed — **eFTI, Regulation (EU) 2020/1056**, obliges authorities EU-wide to accept electronic freight information including e-CMR from **9 July 2027**. **This one fails the filter, and it is the useful negative:** the eFTI date is a real receipt (it is already on p-0010) and it touches none of Convoy's causes. Pairing them would be precisely the hand-wave the critic is warning about — a true date attached to the wrong cause.

**5. Homejoy** — 2012 – **31 July 2015**; $38–40M raised (First Round, Redpoint, Google Ventures); 35 cities.
- *What it was:* an on-demand home-cleaning marketplace matching households to independent cleaners.
- *Why it died then:* the stated deciding factor was **four worker-misclassification lawsuits**, which killed the funding round; behind that, poor retention on both sides.
- *What changed by 2026: the wrong way.* **Directive (EU) 2024/2831 on platform work** entered into force 1 December 2024 and must be transposed by **2 December 2026**; its central mechanism is a **legal presumption of employment** where the platform directs and controls the work. **This is the single most valuable output of the whole exercise:** p-0033 (score 8, STRONG) proposes exactly a marketplace where carers pick up shifts at facilities, and its `build.note` flags "a clean worker-status answer" as a precondition with **no source and no date behind it**. The Platform Work Directive is a source and a date, and it runs against the record.

---

## Recommendation

**Reject as a feed. Adopt as a one-off human reading exercise. Adopt its *inverse* as a standing checklist item.**

**Why reject as a feed:**

1. **The named source is closed to us in writing.** startupgraveyard.io's robots.txt disallows `ClaudeBot` by name, sets `ai-train=no`, and asserts an Article 4 DSM reservation of rights. `data/feeds.json` demands an honest `access` verdict and the honest verdict is "refused" — a value the schema does not even have. The only rich, permitted alternative is Failory: ~120–400 US/UK consumer-internet companies from the 2010s, with no Czech coverage. CB Insights is paywalled; Crunchbase closed-company data is paywalled.
2. **A graveyard record scores nothing.** `dims: []` on every dimension. Eight steps of schema work, a new route, a widened `z.enum` and a new checker invariant, to add a ledger that moves no number and answers neither of the two questions the critic asked. Part 1 is where WHO and HOW MUCH live, and no dead American startup helps with either.
3. **It is the register's highest-risk source class.** Every other feed is an observation; this one is an inference, and the inference is the exact sentence a language model writes best and verifies worst. Given this register's own error history, that is the wrong thing to industrialise.
4. **The idea is right; the direction is backwards.** The valuable move is not "find a dead idea and argue its time has come." It is: **for every live record, ask what killed the last people who tried this, and whether that cause has been removed — citing the instrument that removed it, or saying plainly that nothing has.** Run that way, in one afternoon, it produced one immediately actionable finding (Platform Work Directive vs p-0033) and three confirmations that the register's existing why-now instruments are the right ones.

**Concretely:**

- **Do not** create a `graveyard` evidence type, a feed, an id prefix or a `source` value. Leave `bootstrapped` reserved.
- **Do** add one line to `pipeline/MATCH.md` §9 or the monthly checklist in `pipeline/SCANS.md`: *before a record reaches score ≥ 7, name the last comparable that **failed** at this, state its recorded cause of death, and say which dated Czech instrument removes that cause and which causes nothing removes.* Cite the instrument, never the failure. If nothing removes the cause, the record says so — the same discipline `gap` already applies to an absence.
- **Do** file **Directive (EU) 2024/2831** against **p-0033** now, as a `regulation` source with the 2 December 2026 transposition date. Whether it takes `dims: []` (context) or `dims: [urgency]` (a forcing function running *against* the record) is a MATCH judgment, not an audit one.
- **If a source is still wanted**, use **`failory.com/cemetery/`** — robots-permitted, server-rendered, closed-vocabulary `Cause` field — as a **human reading list for the monthly scan**, not as an ingest. Zero schema change, zero enum, zero route, zero maintenance.

**And the larger point:** the critic's second sentence ("I'd rather look at startupgraveyard.io for inspiration") is the weaker half of his message. The strong half is the first sentence, and it is answered not by a new feed but by the five phone calls in Part 1 §3 — what a Czech buyer pays *today*, by hand, for each of the six open fields the register cannot price.
