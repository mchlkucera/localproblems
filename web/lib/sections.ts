// Body splitter — carves the record body's fixed paragraph grammar into page
// sections (SPEC.md §5). Total function: it never throws, absent sections come
// back empty, and any paragraph without a known lead-in stays with the bucket
// that is currently open. Buckets:
//   lead paragraph(s) + "Existing non-solutions…"  → problem
//   "Why now: …"                                    → window   (lead-in stripped)
//   "Who pays: …"        → dek (first sentence) + howbig (the remainder)
//   "Solved elsewhere: …"                           → solved   (lead-in stripped)
//   "## First moves" section                        → firstmoves
//   "Updated YYYY-MM-DD: …" tails + "**CORRECTION…" → updates  (kept verbatim)

export type Sections = {
  problem: string;
  window: string;
  dek: string;
  howbig: string;
  solved: string;
  firstmoves: string;
  updates: string[];
};

const capitalize = (s: string) => (s ? s.charAt(0).toUpperCase() + s.slice(1) : s);

/** First sentence of a paragraph: ends at the first ". " or the final ".". */
export function splitFirstSentence(s: string): { first: string; rest: string } {
  const i = s.indexOf(". ");
  if (i === -1) return { first: s, rest: "" };
  return { first: s.slice(0, i + 1), rest: s.slice(i + 2).trim() };
}

const stripLead = (p: string, lead: RegExp) => capitalize(p.replace(lead, "").trim());

export function splitBody(body: string): Sections {
  const problem: string[] = [];
  const win: string[] = [];
  const whoPays: string[] = [];
  const solved: string[] = [];
  const firstmoves: string[] = [];
  const updates: string[] = [];
  let current = problem;
  let inMoves = false;

  for (const raw of body.split(/\n{2,}/)) {
    // The correction separator may sit alone or share a block with the
    // paragraph it introduces ("---\n**CORRECTION…") — drop it either way.
    const p = raw.trim().replace(/^(?:-{3,}\n+)+/, "");
    if (!p || /^-{3,}$/.test(p)) continue;

    const moves = p.match(/^##\s*First moves[^\n]*\n?/i);
    if (moves) {
      inMoves = true;
      current = firstmoves;
      const rest = p.slice(moves[0].length).trim();
      if (rest) firstmoves.push(rest);
      continue;
    }
    // Updates and corrections route to their bucket wherever they appear.
    if (/^Updated \d{4}-\d{2}-\d{2}/.test(p) || p.startsWith("**CORRECTION")) {
      updates.push(p);
      current = updates;
      continue;
    }
    if (!inMoves) {
      if (/^Why now:/i.test(p)) { win.push(stripLead(p, /^Why now:\s*/i)); current = win; continue; }
      if (/^Who pays:/i.test(p)) { whoPays.push(stripLead(p, /^Who pays:\s*/i)); current = whoPays; continue; }
      // Loose prefixes: the corpus writes "Existing non-solutions and the incumbent:",
      // "Solved elsewhere, weakly:" — variants keep their full wording.
      if (/^Existing non-solutions/i.test(p)) { problem.push(p); current = problem; continue; }
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
    window: win.join("\n\n"),
    dek: first,
    howbig: [rest, ...whoPays.slice(1)].filter(Boolean).join("\n\n"),
    solved: solved.join("\n\n"),
    firstmoves: firstmoves.join("\n\n"),
    updates,
  };
}
