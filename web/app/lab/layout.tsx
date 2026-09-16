// /lab — local design experiments (the paper-sheet prototypes under
// /lab/paper and /lab/deprecated-paper). LOCAL ONLY: gated like the private
// /sources admin page — `npm run dev` sets LP_ADMIN=1, and a build without it
// 404s every /lab route. The public site lives in app/(site); nothing here is
// linked from it (check-site asserts no public page links into /lab).
//
// A layout gate alone does NOT stop a page from rendering in a production build
// (measured 2026-09-10), so every /lab page must also gate itself before it
// reads any data.
import { notFound } from "next/navigation";

export default function LabLayout({ children }: { children: React.ReactNode }) {
  if (process.env.LP_ADMIN !== "1") notFound();
  return <>{children}</>;
}
