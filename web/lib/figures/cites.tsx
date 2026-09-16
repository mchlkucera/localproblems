// lib/figures — citation plumbing, borrowed read-only from the record
// page (../../problem/cite.tsx, ../../problem/prose.tsx).
//
// PASS THE PAGE'S `CiteCtx` WHEREVER YOU CAN. Every pill owns a popover whose
// id comes from `ctx.seq` ("ls-c1", "ls-c2" …); a second context counting from
// zero on the same page would mint the same ids and break the peeks. With the
// page's ctx the kit's pills share its counter, and — if the kit component is
// CALLED before the page's JSX, as every other section is — its citations are
// recorded in `ctx.cited`, so the sources drawer's "Cited in" lines include it.
// Without one, the kit builds its own context counting from 90,000: safe for a
// single kit figure on a page, and nothing more.
import type { ReactNode } from "react";
import { signalHref, type ProblemSource } from "../data";
import { cite, newCtx, type CiteCtx } from "../site/cite";
import { inline } from "../site/prose";
import { labSource } from "../site/sources";

export function kitCtx(sources: readonly ProblemSource[], ctx?: CiteCtx): CiteCtx {
  if (ctx) return ctx;
  return { ...newCtx(sources.map(labSource)), seq: { n: 90_000 } };
}

/** Only the S-numbers that resolve (S1 = sources[0]); an unresolvable number is
    dropped, never drawn as a pill pointing at nothing. */
export const validCites = (nums: readonly number[] | undefined, sources: readonly ProblemSource[]): number[] =>
  [...new Set((nums ?? []).filter((n) => Number.isInteger(n) && n >= 1 && n <= sources.length))];

export function pills(nums: readonly number[] | undefined, sources: readonly ProblemSource[], ctx: CiteCtx): ReactNode {
  const ok = validCites(nums, sources);
  return ok.length ? cite(ok, ctx) : null;
}

const MARKER = /\[S(\d+)((?:\s*,\s*S?\d+)*)\](?!\()/g;

/** A sentence with `[Sn]` markers → text with the record page's pills.
    Markers are sanitised first: numbers that do not resolve are removed (the
    page's tokenizer would otherwise index past the source list). */
export function citedText(s: string, sources: readonly ProblemSource[], ctx: CiteCtx, key: string): ReactNode[] {
  const clean = s.replace(MARKER, (_m, first: string, rest: string) => {
    const nums = [first, ...(rest.match(/\d+/g) ?? [])].map(Number);
    const ok = validCites(nums, sources);
    return ok.length ? `[${ok.map((n) => `S${n}`).join(",")}]` : "";
  }).replace(/\s+([.,;:])/g, "$1");
  return inline(clean, ctx, { resolveLedger: signalHref }, key);
}

/** A proposal is never cited: markers are stripped, not rendered. The schema
    (or check-records.py) should refuse them in `summary.after`; the kit
    degrades rather than dress a proposal as evidence. */
export const uncited = (s: string) => s.replace(MARKER, "").replace(/\s+([.,;:])/g, "$1").trim();
