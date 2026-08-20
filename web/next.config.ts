import type { NextConfig } from "next";

// Pure SSG. No middleware, no API routes — SPEC.md §5.
const nextConfig: NextConfig = {
  // A PINNED BUILD ID IS WHAT MAKES THE BUILD REPRODUCIBLE, and reproducibility
  // is the precondition for the byte-identity parity gate (web/scripts/parity.mjs).
  //
  // MEASURED, not assumed: with the default (a random 21-char id) two consecutive
  // builds of an UNCHANGED tree emit different HTML — aggregate sha over all 55
  // .next/server/**/*.html went 11682db4… -> 3c701c90… because the id is embedded
  // in every page's flight payload. The parity acceptance test would have been red
  // before a single line of loader code changed, and no diff could be read.
  //
  // Safe because the site is pure SSG with no runtime server: the build id's real
  // job is cache-busting a deployed .next between deploys, and a fresh prebuilt
  // upload replaces the whole directory anyway.
  generateBuildId: () => "lp-build",

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
