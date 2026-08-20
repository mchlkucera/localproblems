import type { NextConfig } from "next";

// Pure SSG. No middleware, no API routes — SPEC.md §5.
const nextConfig: NextConfig = {
  // The v2 route `/sources/[type]` became `/signals/[type]`: SIGNALS are the
  // records, SOURCES are the feeds we ingest from (architecture-v3 §9).
  // The site is publicly deployed, so the retired route must not 404.
  async redirects() {
    return [
      // ONE SEGMENT (`:type`), deliberately — this pattern does NOT match
      // `/sources` itself, which is now the feeds + health page (§4, §7.5).
      // A bare `/sources/:path*` would swallow it.
      //
      // NO FRAGMENT IN THE DESTINATION. Browsers re-apply the original
      // fragment across a 308 when the Location header carries none, so
      // `/sources/tenders#dotace-…` lands on `/signals/tenders#dotace-…`
      // intact. Writing a fragment here would override the incoming one and
      // break the 9 in-body deep links in the record bodies (§9.3, §9.4).
      { source: "/sources/:type", destination: "/signals/:type", permanent: true },
    ];
  },
};

export default nextConfig;
