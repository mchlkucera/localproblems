// /lab/modern/signals/[type] — a signal ledger, page 1, in the modern design.
// Page 1 keeps the bare URL, as the live `/signals/[type]` does; pages 2…N live
// at ./[page]. STATIC: six params at build time, nothing at request time.
// LOCAL ONLY until the migration: no params and a 404 without LP_ADMIN=1.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import "../../front.css";
import "../signals.css";
import { EVIDENCE_TYPES, type EvidenceType } from "../../../../../lib/data";
import { LedgerPage, enabled, ledgerMetadata } from "../ledger";

export const dynamicParams = false;

export function generateStaticParams() {
  if (!enabled()) return [];
  return EVIDENCE_TYPES.map((type) => ({ type }));
}

type Params = { params: Promise<{ type: EvidenceType }> };

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  if (!enabled()) return { title: "Not found" };
  const { type } = await params;
  return ledgerMetadata(type, 1);
}

export default async function ModernSignals({ params }: Params) {
  if (!enabled()) notFound();
  const { type } = await params;
  if (!(EVIDENCE_TYPES as readonly string[]).includes(type)) notFound();
  return <LedgerPage type={type} page={1} />;
}
