// The gazette routes: pages that still render in the retired gazette design
// (docs/modern-migration.md). This is the only layout that loads web/shared.css,
// the checksum-locked copy of skills/design-language/assets/style.css, and the
// Source Serif + Plex Mono fonts. A route group adds nothing to the URL.
import "../../shared.css";

export default function GazetteLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      <link
        href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap"
        rel="stylesheet"
      />
      {children}
    </>
  );
}
