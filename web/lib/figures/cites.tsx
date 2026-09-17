// lib/figures — citation helpers for the figure kit. The figures draw no pills
// of their own (the page's sections carry them), so all the kit needs is a way
// to strip `[Sn]` markers from text it shows plainly.

const MARKER = /\[S(\d+)((?:\s*,\s*S?\d+)*)\](?!\()/g;

/** A proposal is never cited: markers are stripped, not rendered. The schema
    (or check-records.py) should refuse them in `summary.after`; the kit
    degrades rather than dress a proposal as evidence. */
export const uncited = (s: string) => s.replace(MARKER, "").replace(/\s+([.,;:])/g, "$1").trim();
