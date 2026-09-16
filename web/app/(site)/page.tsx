// / — the front page, grouped by opportunity. STATIC: it reads no
// `searchParams`; the category grouping is its own route, ./by-category/.
// Everything else lives in lib/site/front.tsx, which both routes share.
import "./styles/front.css";
import { FrontPage, frontMetadata } from "../../lib/site/front";

export const metadata = frontMetadata;

export default function LabFront() {
  return <FrontPage group="opportunity" />;
}
