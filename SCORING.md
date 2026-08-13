score = arbitrage + money + deadline + demand + gap + freshness    (0-12)

arbitrage (0-3)  0: no foreign analog · 1: one weak analog · 2: funded analog in
                 DE/AT/PL/Nordics + no CZ player found · 3: analogs in 2+ markets
                 AND validated CEE-adjacent
money (0-2)      0: none · 1: relevant tender/grant exists · 2: OPEN tender/grant
                 >= ~5M CZK or recurring annual spend
deadline (0-2)   0: no regulatory trigger · 1: compliance date >18mo out ·
                 2: compliance date <18mo (forcing function live)
demand (0-2)     0: assumed · 1: scattered complaints · 2: recurring documented
                 complaints, petition, or industry pressure
gap (0-2)        0: CZ incumbent check not done · 1: quick search found no CZ
                 player · 2: absence confirmed or only weak/legacy incumbents (named)
freshness (0-1)  1: newest receipt < 90 days

Rules: every point must be justified by a receipts[] entry - no receipt, no point.
Tie-break by (deadline, money). Tier-3 sources can never lift arbitrage or demand
above 1 on their own. Score >= 8 = newsletter-lead material.
