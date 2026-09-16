// /lab/parts/figures — HAND-EXTRACTED MOCK CONTENT, 2026-09-15.
//
// Nothing in this file exists in data/. Each block below was read out of one
// record's own prose, ledgers and `solution` sentence, strictly: every
// "today" step, part, figure and flow carries the S-numbers the record itself
// cites for that sentence, and nothing was added that the record does not
// say. Where a record states a fact with NO citation, the mock keeps it and
// marks it `uncited` rather than dropping it or lending it a source — that
// gap is part of what the owner is judging.
//
// The "after" half of every flow is the record's LIKELY SOLUTION — a proposal,
// never evidence. It carries no citation of its own (only a fact inside it,
// such as a legal date, may), and the figures draw it dashed and labelled.
//
// A production version would move each block into the record's frontmatter
// under the field named in `field`, validated by zod in web/lib/data.ts and
// asserted by scripts/check-records.py (rule 2: a rule enforced by prose is
// not enforced).

// ---- A. the suggested solution as a before/after flow ------------------------

export type FlowStep = {
  /** Who does this step today (or, for an added step, nobody). */
  who: string;
  /** Today's step, from the problem prose. null ⇒ the solution adds it. */
  today: string | null;
  cites: number[];
  /** Today's step re-enters information someone already wrote down. */
  reentry?: boolean;
  /** Who does it with the suggested solution. */
  afterWho?: string;
  /** The step with the suggested solution. null ⇒ the solution removes it. */
  after: string | null;
  /** A sourced FACT inside the after text (a legal date) — not the effect. */
  afterCites?: number[];
  /** The after step still re-enters information. */
  afterReentry?: boolean;
  change: "kept" | "changed" | "removed" | "added" | "merged";
  /** Consolidation shape: who is paid for this step today. */
  supplier?: string;
};

export type Flow = {
  id: string;
  shape: "re-entry" | "consolidation";
  steps: FlowStep[];
  /** Consolidation: the after row spans steps [from, to] (1-based). */
  merge?: { from: number; to: number; who: string; what: string };
  extractedFrom: string;
};

export const FLOWS: Flow[] = [
  {
    id: "p-0036",
    shape: "re-entry",
    extractedFrom: "The problem ¶1 [S1,S3], ¶2 [S1,S2]; the solution sentence",
    steps: [
      {
        who: "Doctor",
        today: "Writes the radiology finding or discharge summary as free text",
        cites: [1, 3],
        afterWho: "Doctor",
        after: "Writes it into a report template in the hospital system; the report is data as it is written",
        change: "changed",
      },
      {
        who: "Coder",
        today: "Reads it again to produce the codes the insurer pays on",
        cites: [1, 3],
        reentry: true,
        afterWho: "Coder",
        after: "Confirms the insurer codes proposed from the report’s data",
        change: "changed",
      },
      {
        who: "Documentarian",
        today: "Reads it a third time to fill the cancer registry",
        cites: [1, 2],
        reentry: true,
        afterWho: "Coder",
        after: "Confirms the registry entry proposed from the same data",
        change: "changed",
      },
    ],
  },
  {
    id: "p-0010",
    shape: "re-entry",
    extractedFrom: "The problem ¶1 [S2]; Why now [S3]; the solution sentence",
    steps: [
      {
        who: "Dispatcher",
        today: "Arranges each load by phone",
        cites: [2],
        afterWho: "Dispatcher",
        after: "Unchanged: the suggested solution does not take the call",
        change: "kept",
      },
      {
        who: "Office",
        today: "Someone re-types the delivery note and the CMR consignment note",
        cites: [2],
        reentry: true,
        afterWho: "Software",
        after: "Reads the delivered load’s own delivery note and CMR",
        change: "changed",
      },
      {
        who: "Office",
        today: "Invoices, and the factoring paperwork, chased by hand",
        cites: [2],
        reentry: true,
        afterWho: "Software",
        after: "Turns those same documents into the invoice",
        change: "changed",
      },
      {
        who: "—",
        today: null,
        cites: [],
        afterWho: "Software",
        after: "Keeps the documents in the electronic form authorities must accept from 9 July 2027",
        afterCites: [3],
        change: "added",
      },
    ],
  },
  {
    id: "p-0008",
    shape: "consolidation",
    extractedFrom: "The problem [S2,S13,S19]; Who pays [S8]; First moves 1, 4 and 6 [S7,S16]; the solution sentence",
    steps: [
      {
        who: "The town or care home",
        today: "Registers with NÚKIB, the cyber agency: 4,825 of about 6,000 had by 8 February 2026",
        cites: [13],
        afterWho: "The town or care home",
        after: "Unchanged: its own duty",
        change: "kept",
      },
      {
        who: "A scope-analysis seller",
        today: "Works out whether the law applies and what it owes; Týn nad Vltavou paid for exactly that",
        cites: [7],
        change: "merged",
        after: null,
        supplier: "scope analysis",
      },
      {
        who: "A grant consultant",
        today: "Writes the IROP subsidy application: about 121,000 CZK for the application alone",
        cites: [8],
        change: "merged",
        after: null,
        supplier: "grant consultant",
      },
      {
        who: "A documents seller",
        today: "Sells the compliance paperwork as a package, about 91,000 CZK; nobody on file does the security work itself",
        cites: [7, 16, 19],
        change: "merged",
        after: null,
        supplier: "documents seller",
      },
    ],
    merge: {
      from: 2,
      to: 4,
      who: "One provider, one fixed price",
      what: "Checks what the town owes before its deadline, writes the EU subsidy application where one applies, then does the security work itself, not only the documents",
    },
  },
];

// ---- B. the suggested solution, in parts: who already sells each part --------

export type Seller = {
  name: string;
  note: string;
  cites: number[];
  /** Where the seller sits: on the comps/locals ledgers, or named only in prose. */
  ledger: "comp" | "direct" | "adjacent" | "off-ledger";
  maturity?: "established" | "early";
};
export type Part = {
  part: string;
  abroad: Seller[];
  here: Seller[];
  /** sold: an established seller here · early: only early sellers here ·
      open: the market check found nobody here selling this part. */
  verdict: "sold" | "early" | "open";
  /** For `open`: the gap-check that found nobody (it ran a positive control). */
  verdictCites: number[];
  verdictNote?: string;
};
export const PARTS: { id: string; extractedFrom: string; parts: Part[] }[] = [
  {
    id: "p-0036",
    extractedFrom: "the solution sentence split at its clauses; players from comps[] and locals[]; verdicts from Local competition [S16] and First moves 1",
    parts: [
      {
        part: "The report written as data, from templates, at the moment of writing",
        abroad: [{ name: "Jacobian (Smart Reporting)", note: "structured radiology and pathology reporting, 16,000 physicians", cites: [10], ledger: "comp" }],
        here: [{ name: "Medicalc", note: "says its AI turns a dictated ward round into a structured report; not shown running anywhere", cites: [16], ledger: "direct", maturity: "early" }],
        verdict: "open",
        verdictCites: [16],
        verdictNote: "No seller of structured radiology templates found",
      },
      {
        part: "Insurer codes proposed for a coder to confirm",
        abroad: [
          { name: "ID Berlin (ID DIACOS)", note: "coding software in 1,200+ hospitals", cites: [12], ledger: "comp" },
          { name: "Tiplu (MOMO)", note: "AI-assisted coding in 80+ hospitals", cites: [13], ledger: "comp" },
        ],
        here: [
          { name: "STAPRO", note: "AI coding assistant, a free pilot in 23 hospitals", cites: [4], ledger: "direct", maturity: "early" },
          { name: "ICZ", note: "AV(D) proposes diagnoses to bill; no named buyer since 2023", cites: [16], ledger: "direct", maturity: "early" },
        ],
        verdict: "early",
        verdictCites: [16],
      },
      {
        part: "Registry entries filled from the same data",
        abroad: [],
        here: [{ name: "ÚZIS (the state)", note: "AI completing the cancer registry from the registry’s own data, not the hospital record", cites: [17], ledger: "off-ledger" }],
        verdict: "open",
        verdictCites: [16],
        verdictNote: "No vendor found; the state works the registry side only",
      },
    ],
  },
  {
    id: "p-0010",
    extractedFrom: "the solution sentence, and what TruckManager’s own pages say it does and does not do [S11]",
    parts: [
      {
        part: "Delivery papers captured where the load is delivered",
        abroad: [{ name: "Hemut", note: "document ingestion", cites: [1], ledger: "comp" }],
        here: [{ name: "TruckManager", note: "drivers scan the papers into the load from the cab", cites: [11], ledger: "direct", maturity: "established" }],
        verdict: "sold",
        verdictCites: [11],
      },
      {
        part: "The invoice raised without a person",
        abroad: [{ name: "Hemut", note: "automated accounting", cites: [1], ledger: "comp" }],
        here: [
          { name: "TruckManager", note: "raises it from the GPS kilometres and weight", cites: [11], ledger: "direct", maturity: "established" },
          { name: "Transfer Manager", note: "a PDF invoice sent to the customer", cites: [11], ledger: "direct", maturity: "early" },
        ],
        verdict: "sold",
        verdictCites: [11],
      },
      {
        part: "The invoice built by reading the delivery note and CMR",
        abroad: [{ name: "Hemut", note: "reads the documents, then accounts", cites: [1], ledger: "comp" }],
        here: [],
        verdict: "open",
        verdictCites: [11],
        verdictNote: "TruckManager builds its invoice from telematics, not from the document",
      },
      {
        part: "Documents on the electronic footing accepted from 9 July 2027",
        abroad: [],
        here: [{ name: "OLTIS Group (LORI)", note: "electronic consignment notes (e-CMR) inside dispatch software", cites: [8], ledger: "adjacent", maturity: "established" }],
        verdict: "open",
        verdictCites: [11],
        verdictNote: "Nobody claims a certified platform for 2027",
      },
    ],
  },
  {
    id: "p-0008",
    extractedFrom: "the solution sentence; locals[] and the sellers First moves 6 names [S7,S8,S16]",
    parts: [
      {
        part: "Check what each town owes before its deadline",
        abroad: [],
        here: [{ name: "Institut kybernetické bezpečnosti", note: "sold Týn nad Vltavou a scope analysis", cites: [7], ledger: "off-ledger" }],
        verdict: "sold",
        verdictCites: [7],
        verdictNote: "By a firm not on the local ledger; its maturity was never checked",
      },
      {
        part: "Write the EU subsidy application",
        abroad: [],
        here: [{ name: "enovation", note: "writes IROP applications, about 121k CZK each", cites: [8], ledger: "off-ledger" }],
        verdict: "sold",
        verdictCites: [8],
        verdictNote: "By a consultancy not on the local ledger",
      },
      {
        part: "The compliance documents",
        abroad: [
          { name: "Secfix", note: "compliance automation for small firms", cites: [11], ledger: "comp" },
          { name: "Copla", note: "NIS2/DORA/ISO 27001 compliance automation", cites: [12], ledger: "comp" },
        ],
        here: [
          { name: "NIS2 Průvodce", note: "3,000 CZK a month", cites: [16], ledger: "direct", maturity: "early" },
          { name: "Compligen", note: "29,900 CZK once", cites: [16], ledger: "direct", maturity: "early" },
          { name: "NIS2 Doku", note: "from 4,900 CZK", cites: [16], ledger: "direct", maturity: "early" },
          { name: "Lexnova Energy", note: "about 91k CZK a package", cites: [7], ledger: "direct", maturity: "early" },
        ],
        verdict: "early",
        verdictCites: [16],
      },
      {
        part: "The security work itself",
        abroad: [],
        here: [{ name: "ICZ Risk*Guide", note: "a security programme bought as a project, at the enterprise end", cites: [16], ledger: "adjacent", maturity: "established" }],
        verdict: "open",
        verdictCites: [16],
        verdictNote: "The four products sell the paperwork, not the work",
      },
    ],
  },
];

// ---- G. the size of the problem, as one number -----------------------------

export type Size = {
  id: string;
  figure: string;
  counts: string;
  cites: number[];
  /** Optional part of the whole, drawn as a bar. */
  part?: { share: number; atLeast?: boolean; label: string; rest: string; cites: number[]; crossSource?: string };
  /** Segmented variant (a count of steps rather than a share). */
  segments?: { label: string; on: boolean }[];
  segLabel?: string;
};
export const SIZES: Size[] = [
  {
    id: "p-0036",
    figure: "3×",
    counts: "readings of every report: the doctor who writes it, then a coder, then a documentarian",
    cites: [1, 3],
    segments: [
      { label: "Writes", on: false },
      { label: "Reads again", on: true },
      { label: "Reads again", on: true },
    ],
    segLabel: "2 of 3 readings re-read what is already written",
  },
  {
    id: "p-0008",
    figure: "~6,000",
    counts: "organisations under the new cybersecurity law",
    cites: [13],
    part: { share: 4825 / 6000, label: "4,825 registered by 8 Feb 2026", rest: "over a thousand not yet", cites: [13] },
  },
  {
    id: "p-0010",
    figure: "~40,000",
    counts: "haulier firms, most under ten trucks",
    cites: [2],
    part: {
      share: 700 / 40000,
      atLeast: true,
      label: "700+ firms run TruckManager",
      rest: "the rest of the base",
      cites: [11],
      crossSource: "Part and whole come from two different sources (S11 over S2), and S11 counts transport firms, not only hauliers",
    },
  },
  {
    id: "p-0033",
    figure: "3,000+",
    counts: "workers missing from Czech social services",
    cites: [3],
    part: { share: 0.5, atLeast: true, label: "over half of 625 surveyed facilities report unfilled posts", rest: "", cites: [3] },
  },
];

// ---- H. who pays whom -----------------------------------------------------

export type Node = { text: string; cites: number[]; uncited?: boolean };
export type Chain = {
  id: string;
  funders: Node[];
  buyer: Node;
  paidToday: Node[];
  solution: { text: string; cites: number[] };
  extractedFrom: string;
};
export const CHAINS: Chain[] = [
  {
    id: "p-0036",
    extractedFrom: "Who pays [S3,S8]; Local competition [S4,S16]; the solution sentence",
    funders: [
      { text: "Health insurers, paying on the codes", cites: [3] },
      { text: "IROP call 79: up to 28M CZK per provider for documentation systems, to 2 Dec 2026", cites: [8] },
    ],
    buyer: { text: "The hospital", cites: [3] },
    paidToday: [
      { text: "A doctor’s time to write each report, then a coder’s time to read it back into codes; no source states what that costs", cites: [3] },
      { text: "Hospital-system vendors (STAPRO, ICZ, Medicalc), whose coding assistants are pilots", cites: [4, 16] },
    ],
    solution: { text: "Report templates inside the hospital system, bought by the hospital; the open grant funds exactly this kind of system", cites: [8] },
  },
  {
    id: "p-0008",
    extractedFrom: "Who pays [S1,S8,S9,S13]; price receipts [S23,S24,S25]; the solution sentence",
    funders: [
      { text: "The organisation’s own budget, compelled by law", cites: [1, 13] },
      { text: "IROP call 120: €99.6M at a 50% rate for towns, regions and hospitals, to 17 Dec 2026", cites: [9] },
    ],
    buyer: { text: "A small town or care home, one of about 6,000", cites: [13] },
    paidToday: [
      { text: "About 121,000 CZK to a consultant for the grant application alone", cites: [8] },
      { text: "About 91,000 CZK for a compliance package, or 3,000 CZK a month for a platform", cites: [23, 25] },
      { text: "About 9M CZK for the whole job (Český Brod, 7,000 people)", cites: [24] },
    ],
    solution: { text: "One fixed-price provider for the check, the application and the work; half of it payable from IROP 120", cites: [9] },
  },
  {
    id: "p-0033",
    extractedFrom: "Who pays; Existing non-solutions [S9]; the price receipt [S12]; the solution sentence",
    funders: [
      { text: "The provider’s own staffing budget, money already going to agencies", cites: [], uncited: true },
    ],
    buyer: { text: "A care home or other provider", cites: [3] },
    paidToday: [
      { text: "Overtime, agency staff and word of mouth", cites: [], uncited: true },
      { text: "Agencies such as sestrycz.eu, broking people into posts by phone; no per-shift price published", cites: [9] },
      { text: "A nurse wage bill of about 271M CZK a year across the 262 employers hiring in July 2026", cites: [12] },
    ],
    solution: { text: "A fee on every shift filled; a vetted nurse or carer picks the shift", cites: [] },
  },
];

/** Hand classification of all 29 live records' problem prose (2026-09-15):
    does it describe a process a before/after flow could be drawn from? Read
    from each record's lead paragraphs and `solution` sentence only. */
export const PROCESS_SHAPE = {
  strong: ["p-0002", "p-0005", "p-0010", "p-0036"],
  moderate: ["p-0001", "p-0004", "p-0007", "p-0008", "p-0009", "p-0011", "p-0025", "p-0032", "p-0033"],
  consolidation: ["p-0022", "p-0026", "p-0031", "p-0035"],
  none: ["p-0003", "p-0006", "p-0017", "p-0018", "p-0023", "p-0024", "p-0027", "p-0028", "p-0029", "p-0030", "p-0034", "p-0037"],
} as const;

/** Hand count: `solution` sentences that split into two or more parts. */
export const MULTI_PART = [
  "p-0001", "p-0002", "p-0003", "p-0004", "p-0005", "p-0006", "p-0007", "p-0008", "p-0009", "p-0010",
  "p-0017", "p-0018", "p-0023", "p-0024", "p-0025", "p-0026", "p-0027", "p-0028", "p-0030", "p-0032",
  "p-0036", "p-0037",
] as const;
