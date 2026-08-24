// Body splitter — carves the record body's fixed paragraph grammar into page
// sections (SPEC.md §5). Total function: it never throws, absent sections come
// back empty, and any paragraph without a known lead-in stays with the bucket
// that is currently open. Buckets:
//   lead paragraph(s) + "Existing non-solutions…"  → problem
//   "Why now: …"                                    → window   (lead-in stripped)
//   "Who pays: …"        → dek (first sentence) + howbig (the remainder)
//   "Solved elsewhere: …"                           → solved   (lead-in stripped)
//   "## First moves" section                        → firstmoves
//   "## Revisions" section                          → revisions
//
// REVISIONS (v3, 2026-08-21). The register prints its corrections — that is the
// whole claim it has over an LLM guess — but printing them is not the same as
// leading with them. Up to 2026-08-20 each correction was appended as its own
// `**CORRECTION (date, tag):**` block with a 4px ink rule, and 40 of them had
// accumulated across 31 records: on p-0026 the audit trail outweighed the
// argument 441 words to 181. The trail now collects under one `## Revisions`
// heading at the foot, ONE ENTRY PER DATE, in the quiet register of a ledger:
//
//   2026-08-20 · evidence audit — Removed three uncited "Why now" claims…
//
// The meta half (`date · tag`) is lifted out so the page can set it as the
// exhibit reference line it is; the rest stays prose. Nothing is deleted by
// this move — a merge folds facts together, it never drops one.
//
// The two legacy spellings — `**CORRECTION (…)` blocks and `Updated <date>`
// tails — still route here from anywhere in the body. They are how the corpus
// was written before this pass, and a stray one must land in the revision list
// rather than leak into the argument.

export type Revision = {
  /** `2026-08-20 · evidence audit` — empty for a legacy block that states no
      date-and-tag head of its own. */
  meta: string;
  /** The revision prose, rendered through the same markdown/citation pass as
      the body — a revision cites its receipts exactly as an argument does. */
  text: string;
};

export type Sections = {
  problem: string;
  /** The "Existing non-solutions…" paragraph(s) — who already sells into this
      market locally. Split out of `problem` so the page can head it plainly as
      "Local competition" (owner, 2026-08-24); empty when a record states none. */
  competition: string;
  window: string;
  dek: string;
  howbig: string;
  solved: string;
  firstmoves: string;
  revisions: Revision[];
};

const capitalize = (s: string) => (s ? s.charAt(0).toUpperCase() + s.slice(1) : s);

/** First sentence of a paragraph: ends at the first ". " or the final ".". */
export function splitFirstSentence(s: string): { first: string; rest: string } {
  const i = s.indexOf(". ");
  if (i === -1) return { first: s, rest: "" };
  return { first: s.slice(0, i + 1), rest: s.slice(i + 2).trim() };
}

const stripLead = (p: string, lead: RegExp) => capitalize(p.replace(lead, "").trim());

/** `2026-08-20 · evidence audit — <prose>` → its two halves. The tag is capped
    at 40 characters and may not contain an em dash, so a revision whose prose
    opens with a dashed clause can never be mistaken for a very long tag. */
const REV_HEAD = /^(\d{4}-\d{2}-\d{2})\s*·\s*([^—\n]{1,40}?)\s*—\s*([\s\S]+)$/;

function revision(p: string): Revision {
  const m = p.match(REV_HEAD);
  return m ? { meta: `${m[1]} · ${m[2]}`, text: m[3] } : { meta: "", text: p };
}

export function splitBody(body: string): Sections {
  const problem: string[] = [];
  const competition: string[] = [];
  const win: string[] = [];
  const whoPays: string[] = [];
  const solved: string[] = [];
  const firstmoves: string[] = [];
  const revisions: Revision[] = [];
  let current = problem;
  let mode: "body" | "moves" | "revisions" = "body";

  for (const raw of body.split(/\n{2,}/)) {
    // The legacy correction separator may sit alone or share a block with the
    // paragraph it introduces ("---\n**CORRECTION…") — drop it either way.
    const p = raw.trim().replace(/^(?:-{3,}\n+)+/, "");
    if (!p || /^-{3,}$/.test(p)) continue;

    const heading = p.match(/^##\s*(First moves|Revisions)[^\n]*\n?/i);
    if (heading) {
      const rest = p.slice(heading[0].length).trim();
      if (/^r/i.test(heading[1])) {
        mode = "revisions";
        if (rest) revisions.push(revision(rest));
      } else {
        mode = "moves";
        current = firstmoves;
        if (rest) firstmoves.push(rest);
      }
      continue;
    }
    // Legacy update tails and CORRECTION blocks route to the revision list
    // wherever they appear, and stay verbatim — they carry no date-tag head.
    if (/^Updated \d{4}-\d{2}-\d{2}/.test(p) || p.startsWith("**CORRECTION")) {
      revisions.push({ meta: "", text: p });
      mode = "revisions";
      continue;
    }
    if (mode === "revisions") { revisions.push(revision(p)); continue; }
    if (mode === "body") {
      if (/^Why now:/i.test(p)) { win.push(stripLead(p, /^Why now:\s*/i)); current = win; continue; }
      if (/^Who pays:/i.test(p)) { whoPays.push(stripLead(p, /^Who pays:\s*/i)); current = whoPays; continue; }
      // Loose prefixes: the corpus writes "Existing non-solutions and the incumbent:",
      // "Solved elsewhere, weakly:" — variants keep their full wording.
      if (/^Existing non-solutions/i.test(p)) { competition.push(stripLead(p, /^Existing non-solutions[^:]*:\s*/i)); current = competition; continue; }
      if (/^Solved elsewhere:/i.test(p)) { solved.push(stripLead(p, /^Solved elsewhere:\s*/i)); current = solved; continue; }
      if (/^Solved elsewhere/i.test(p)) { solved.push(p); current = solved; continue; }
    }
    current.push(p);
  }

  let { first, rest } = splitFirstSentence(whoPays[0] ?? "");
  // Punch openers ("Who pays: twice over.") cannot stand as a dek alone —
  // absorb following sentences until it can (deterministic 40-char floor).
  while (first && first.length < 40 && rest) {
    const next = splitFirstSentence(rest);
    first = `${first} ${next.first}`;
    rest = next.rest;
  }
  return {
    problem: problem.join("\n\n"),
    competition: competition.join("\n\n"),
    window: win.join("\n\n"),
    dek: first,
    howbig: [rest, ...whoPays.slice(1)].filter(Boolean).join("\n\n"),
    solved: solved.join("\n\n"),
    firstmoves: firstmoves.join("\n\n"),
    revisions,
  };
}
