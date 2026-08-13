# Conventions
Categories (exactly one per signal): fintech, health, housing, energy, mobility, govtech, retail-services, b2b, legal-compliance, education, environment, other
Signal tiers: 1 = arbitrage/regulatory trigger, 2 = tender/grant/complaint, 3 = diagnostic/VC garnish
Normalized signal file: normalized/<source>/<source>-<nativeid>.md — one directory per source key (yc, reg, round; country codes like de for foreign-market arbitrage scans). Frontmatter:
  id, title (short English display name, "Thing — what it is"), source, url, date (ISO), category, tier, geo (CZ-national | CZ-<region> | <ISO2>-... | EU), summary_en (2 sentences max), money_eur (number|null), money_note
Problem file: problems/p-NNNN-<slug>.md with frontmatter per the template in TASK docs:
  id, title, category, geo, score, signals{arbitrage0-3,money0-2,deadline0-2,demand0-2,gap0-2,freshness0-1}, status: candidate, receipts[{type,url,note,date}], created, updated
Scoring: every point must be justified by a receipt. Tier-3 alone never creates a problem.
Receipt→dimension conventions (rendered by the v2 app, docs/05): receipt `type` maps to a scorecard dimension (arbitrage→proof, tender/contract/subsidy→money, regulation→urgency, complaint/news→demand, gap-check→gap). When a receipt's evidence justifies an extra dimension, either include the literal marker "Demand point" in a gap-check note (demand) or set an explicit `dims: [..]` list on the receipt — a demand/money/etc. point without a resolvable receipt ref degrades the rendered scorecard.
