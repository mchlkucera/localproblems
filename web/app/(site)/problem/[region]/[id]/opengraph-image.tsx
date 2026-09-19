// /problem/[region]/[id]/opengraph-image-… — this problem's own share card:
// its title, its brief, the opportunity score with the five section dots, and
// the entry level. STATIC: every record's card is prerendered at build time
// from the same params as the page (rejected records get neither), and served
// as a PNG file. Drawing: lib/og/card.tsx.
import { ImageResponse } from "next/og";
import { getProblems } from "../../../../../lib/data";
import { categoryLabel } from "../../../../../lib/format";
import { CARD, RecordCard, cardFonts } from "../../../../../lib/og/card";
import { plainText } from "../../../../../lib/og/share";
import { splitLead } from "../../../../../lib/sections";
import { protoScores, protoTotal } from "../../../../../lib/site/score-proto";

export const alt = "The problem’s title, summary, opportunity score and entry level, on localproblems.org";
export const size = CARD;
export const contentType = "image/png";

/** The page's params exactly (page.tsx): one card per public record. */
export function generateStaticParams() {
  return getProblems()
    .filter((p) => p.status !== "rejected")
    .map((p) => ({ region: p.region, id: p.id }));
}

export default async function Image({ params }: { params: Promise<{ region: string; id: string }> }) {
  const { region, id } = await params;
  const p = getProblems().find((r) => r.region === region && r.id === id && r.status !== "rejected");
  if (!p) return new Response("Not found", { status: 404 });
  const proto = protoScores(p);
  // the brief's first sentence (RecordCard cuts it at a word to fit)
  const brief = p.brief?.trim() ? splitLead(plainText(p.brief)).lead : "";
  return new ImageResponse(
    (
      <RecordCard
        title={p.title}
        line={brief || categoryLabel(p.category)}
        category={p.category}
        scores={proto.filter((r) => r.inTotal).map(({ n, max }) => ({ n, max }))}
        total={protoTotal(proto)}
        level={p.entry.level}
      />
    ),
    { ...size, fonts: cardFonts() },
  );
}
