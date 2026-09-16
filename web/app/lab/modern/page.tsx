// /lab/modern — the front page, grouped by opportunity. STATIC: it reads no
// `searchParams`; the category grouping is its own route, ./by-category/.
// Everything else lives in ./front.tsx, which both routes share.
import { FrontPage, frontMetadata } from "./front";

export const metadata = frontMetadata;

export default function LabFront() {
  return <FrontPage group="opportunity" />;
}
