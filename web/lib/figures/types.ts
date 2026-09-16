// lib/figures — the `process` contract, as a LOCAL STRUCTURAL TYPE.
//
// The frontmatter field is being added to the schema (web/lib/data.ts) in
// parallel. These types mirror the contract exactly and are deliberately
// loose in one direction only: every array is `readonly` and the keys the
// contract lets an author omit are optional, so whatever zod infers for the
// real field (mutable arrays, required-but-nullable keys) is assignable here
// without a cast. The enums are NOT loosened: an unknown `known` or `change`
// value should fail to compile at the call site, not render as a guess.
//
//   process:
//     summary:
//       today: 'A doctor writes … [S1,S3]'   # plain words; [Sn] markers → pills
//       after: 'The report is written …'      # a proposal: never cited
//     steps:                                  # in order, left to right
//       - who: Doctor                         # plain words; '?' if unknown
//         today: Writes the finding …         # null for a step the solution ADDS
//         known: documented                   # documented | inferred | unknown
//         cites: [1, 3]                       # REQUIRED for documented, allowed
//                                             # for inferred, empty for unknown
//         reenters: false                     # re-types/re-reads what someone wrote
//         change: changes                     # stays | changes | goes | new
//         after: Writes it into a template …  # null when change is goes

export type ProcessKnown = "documented" | "inferred" | "unknown";
export type ProcessChange = "stays" | "changes" | "goes" | "new";

export type ProcessStep = {
  readonly who: string;
  readonly today?: string | null;
  readonly known: ProcessKnown;
  readonly cites?: readonly number[];
  readonly reenters?: boolean;
  readonly change: ProcessChange;
  readonly after?: string | null;
};

export type ProcessField = {
  readonly summary?: {
    readonly today?: string | null;
    readonly after?: string | null;
  } | null;
  readonly steps: readonly ProcessStep[];
};
