# Conventions
Categories (exactly one per signal): fintech, health, housing, energy, mobility, govtech, retail-services, b2b, legal-compliance, education, environment, other
Signal tiers: 1 = arbitrage/regulatory trigger, 2 = tender/grant/complaint, 3 = diagnostic/VC garnish
Normalized signal file: normalized/<source>/<source>-<nativeid>.md — one directory per source key (yc, reg, round; country codes like de for foreign-market arbitrage scans). Frontmatter:
  id, source, url, date (ISO), category, tier, geo (CZ-national | CZ-<region> | <ISO2>-... | EU), summary_en (2 sentences max), money_eur (number|null), money_note
Problem file: problems/p-NNNN-<slug>.md with frontmatter per the template in TASK docs:
  id, title, category, geo, score, signals{arbitrage0-3,money0-2,deadline0-2,demand0-2,gap0-2,freshness0-1}, status: candidate, receipts[{type,url,note,date}], created, updated
Scoring: every point must be justified by a receipt. Tier-3 alone never creates a problem.
