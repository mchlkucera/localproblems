// The field strip's one judgment: is a foreign comparable ESTABLISHED?
//
// A PORT, NOT A SECOND DEFINITION — and a prototype's debt. The established
// test lives in scripts/check-records.py `established()`, where it scores both
// proof (abroad) and gap (at home) with the sign flipped. Locals carry the
// verdict as a field (`maturity`), so the strip reads it straight; comps do
// not, so this reads `traction` with the checker's three limbs, verbatim.
// Checked 2026-09-10: all 91 comps in the corpus agree with the checker. If the
// strip is adopted, the checker should write the verdict into the projection
// (a `comps[].maturity` column) and this file goes away — one test, one place.

const MIN_YEARS_SELLING = 3;

const LIMBS: RegExp[] = [
  new RegExp(
    String.raw`\bnamed customers?\b|\bpublic customer count\b` +
      String.raw`|[~>]?\d[\d\s.,]*\s*(?:k|m|bn|mil|tis)?\+?\s*(?:[\p{L}\p{N}_./-]+\s+){0,3}` +
      String.raw`(?:customers?|clients?|buyers?|users?|providers?|agencies|firms?|shops?|` +
      String.raw`councils?|members?|organi[sz]ations?|hospitals?|banks?|schools?|advisers?|` +
      String.raw`households?|patients?|sites?|z[áa]kazn[íi]k\p{L}*|odb[ěe]ratel\p{L}*|obc[íi]|` +
      String.raw`[úu][řr]ad\p{L}*|[šs]kol\p{L}*|nemocnic\p{L}*)(?![\p{L}\p{N}_])` +
      String.raw`|\b(?:customers?|clients?|users?|referen[cs]\p{L}*|z[áa]kazn[íi]\p{L}*)\s+` +
      String.raw`(?:incl\.|including|such as)|\b(?:trusted by|used by|used in|deployed at)\b`,
    "iu",
  ),
  /\bseries\s+[a-k]\b/i,
  new RegExp(
    String.raw`\b(?:atest\p{L}*|attest\p{L}*|certifi\p{L}*|akredit\p{L}*|notified body|` +
      String.raw`state (?:certification|register)|framework (?:agreement|listing)|` +
      String.raw`r[áa]mcov\p{L}+ (?:dohod|smlouv)\p{L}*)(?![\p{L}\p{N}_])`,
    "iu",
  ),
];

/** `year` is the register's extract year — never the wall clock. */
export function compEstablished(since: number | undefined, traction: string, year: number): boolean {
  if (since === undefined || year - since < MIN_YEARS_SELLING) return false;
  return LIMBS.some((re) => re.test(traction ?? ""));
}
