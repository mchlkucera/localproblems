// /lab — design experiments that deliberately step OUTSIDE the gazette design
// language (owner, 2026-09-10: "a completely separate page … just as Linear
// does: simple, streamlined, one font, various gray shades"). LOCAL ONLY: gated
// like the private /sources admin page — `npm run dev` sets LP_ADMIN=1, and a
// build without it 404s every /lab route before any data is read, so nothing
// here can ship by accident.
//
// The root layout loads no stylesheet (web/shared.css is the gazette group's);
// tokens.css sets the page ground under `body:has(.lab)` and states the lab's
// own tokens. Every /lab page wraps its content in <div className="lab">.
import { notFound } from "next/navigation";
import "./tokens.css";

export default function LabLayout({ children }: { children: React.ReactNode }) {
  if (process.env.LP_ADMIN !== "1") notFound();
  return (
    <>
      <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap"
      />
      {children}
    </>
  );
}
