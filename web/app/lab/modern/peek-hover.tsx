"use client";
// /lab/modern — hover-intent for the citation peeks, Escape for the rail's
// tooltips, and old `#sources` / `#sN` links opening the sources drawer.
//
// PROGRESSIVE ONLY. Without this file every pill still opens its card on
// click/tap/Enter/Space (native `popovertarget`), Escape and an outside click
// still close it, and every link still works. What this adds:
//   · mouse: rest on a pill ~140ms → the card opens; move into the card and it
//     stays; leave both → it closes after a short grace.
//   · keyboard: FOCUS ALONE OPENS NOTHING (audit B13: opening on focus pulled
//     the next Tab into the card, so every pill cost three stops). Tab onto a
//     pill just focuses it; Enter or Space opens the card natively, and only
//     then does Tab walk into its links.
//   · click on a card opened by hover PINS it instead of toggling it shut, so
//     "hover, then click to keep it" behaves the way Perplexity does.
//   · Escape hides a rail tooltip (`.ls-tip`) that is showing for hover or
//     focus, without moving either (WCAG 1.4.13). It stays hidden until the
//     pointer leaves that row or focus moves off it.
//   · a URL fragment naming the drawer (`#sources`) or a row inside it
//     (`#s12`, the live record's anchors) opens the drawer on that row, on
//     load and on every hash change — a closed popover cannot be scrolled to.
// One document-level listener set; no per-pill hydration.
import { useEffect } from "react";

type Mode = "hover" | "pinned";

export function PeekHover() {
  useEffect(() => {
    const fine = window.matchMedia("(hover: hover) and (pointer: fine)");
    let openT = 0;
    let closeT = 0;
    let cur: { btn: HTMLElement; pop: HTMLElement; mode: Mode } | null = null;

    const popFor = (btn: HTMLElement) => {
      const id = btn.getAttribute("popovertarget");
      return id ? document.getElementById(id) : null;
    };
    const isOpen = (el: HTMLElement) => el.matches(":popover-open");
    const pillOf = (t: EventTarget | null) =>
      t instanceof Element ? (t.closest("[data-peek]") as HTMLElement | null) : null;
    const peekOf = (t: EventTarget | null) =>
      t instanceof Element ? (t.closest(".ls-peek") as HTMLElement | null) : null;

    const show = (btn: HTMLElement, mode: Mode) => {
      const pop = popFor(btn);
      if (!pop) return;
      window.clearTimeout(closeT);
      if (!isOpen(pop)) {
        try {
          // `source` wires the implicit anchor + focus return where supported
          (pop as HTMLElement & { showPopover(o?: { source?: HTMLElement }): void }).showPopover({ source: btn });
        } catch {
          return;
        }
      }
      cur = { btn, pop, mode: cur?.pop === pop && cur.mode === "pinned" ? "pinned" : mode };
    };
    const hide = () => {
      if (cur && cur.mode !== "pinned" && isOpen(cur.pop)) cur.pop.hidePopover();
    };
    const hideSoon = () => {
      window.clearTimeout(closeT);
      closeT = window.setTimeout(hide, 180);
    };
    const inside = (t: EventTarget | null) =>
      !!cur && t instanceof Node && (cur.btn.contains(t) || cur.pop.contains(t));

    // ---- rail tooltips: Escape, and the reset when pointer or focus leaves --
    const DISMISSED = "data-tip-dismissed";
    const release = (host: Element, to: EventTarget | null) => {
      if (!(to instanceof Node && host.contains(to))) host.removeAttribute(DISMISSED);
    };
    const onKey = (e: KeyboardEvent) => {
      if (e.key !== "Escape") return;
      document.querySelectorAll(".ls-tip-host:hover, .ls-tip-host:focus-visible").forEach((host) => {
        if (host.querySelector(":scope > .ls-tip")) host.setAttribute(DISMISSED, "");
      });
    };

    const onOver = (e: PointerEvent) => {
      if (e.pointerType !== "mouse" || !fine.matches) return;
      const btn = pillOf(e.target);
      if (btn) {
        window.clearTimeout(openT);
        window.clearTimeout(closeT);
        if (cur?.btn === btn && isOpen(cur.pop)) return;
        openT = window.setTimeout(() => show(btn, "hover"), 140);
      } else if (peekOf(e.target) && cur && peekOf(e.target) === cur.pop) {
        window.clearTimeout(closeT);
      }
    };
    const onOut = (e: PointerEvent) => {
      const host = e.target instanceof Element ? e.target.closest(`.ls-tip-host[${DISMISSED}]`) : null;
      if (host) release(host, e.relatedTarget);
      if (e.pointerType !== "mouse") return;
      if (pillOf(e.target)) window.clearTimeout(openT);
      if (cur && !inside(e.relatedTarget) && (inside(e.target))) hideSoon();
    };
    const onFocusOut = (e: FocusEvent) => {
      const host = e.target instanceof Element ? e.target.closest(`.ls-tip-host[${DISMISSED}]`) : null;
      if (host) release(host, e.relatedTarget);
    };
    // capture: runs before the button's native popovertarget toggle
    const onClick = (e: MouseEvent) => {
      const btn = pillOf(e.target);
      if (btn && cur?.btn === btn && isOpen(cur.pop) && cur.mode !== "pinned") {
        e.preventDefault(); // keep it open — pin instead of toggling shut
        cur.mode = "pinned";
        return;
      }
      if (btn) {
        window.clearTimeout(openT);
        const pop = popFor(btn);
        if (pop && !isOpen(pop)) cur = { btn, pop, mode: "pinned" };
      }
      // following an in-page link out of a card or the drawer closes it
      const a = e.target instanceof Element ? e.target.closest("[data-peek-close]") : null;
      const host = a?.closest("[popover]") as HTMLElement | null;
      if (host) window.setTimeout(() => isOpen(host) && host.hidePopover(), 0);
    };
    const onToggle = (e: Event) => {
      const el = e.target as HTMLElement;
      if ((e as ToggleEvent).newState === "closed" && cur?.pop === el) cur = null;
    };

    // ---- `#sources` and `#sN`: open the drawer that holds the target -------
    const onHash = () => {
      let id = "";
      try {
        id = decodeURIComponent(window.location.hash.slice(1));
      } catch {
        return;
      }
      const el = id ? document.getElementById(id) : null;
      const pop = el?.closest("[popover]") as HTMLElement | null;
      if (!el || !pop || !pop.classList.contains("ls-drawer")) return;
      if (!isOpen(pop)) {
        try {
          pop.showPopover();
        } catch {
          return;
        }
      }
      // scroll only the drawer's own list: scrollIntoView would also scroll
      // the drawer box (overflow hidden) and push its header off the top
      const list = el.closest(".ls-drawer-body");
      if (el !== pop && list) {
        list.scrollTop += el.getBoundingClientRect().top - list.getBoundingClientRect().top - 12;
      }
    };

    document.addEventListener("pointerover", onOver);
    document.addEventListener("pointerout", onOut);
    document.addEventListener("focusout", onFocusOut);
    document.addEventListener("keydown", onKey);
    document.addEventListener("click", onClick, true);
    document.addEventListener("toggle", onToggle, true);
    window.addEventListener("hashchange", onHash);
    onHash();
    return () => {
      document.removeEventListener("pointerover", onOver);
      document.removeEventListener("pointerout", onOut);
      document.removeEventListener("focusout", onFocusOut);
      document.removeEventListener("keydown", onKey);
      document.removeEventListener("click", onClick, true);
      document.removeEventListener("toggle", onToggle, true);
      window.removeEventListener("hashchange", onHash);
      window.clearTimeout(openT);
      window.clearTimeout(closeT);
    };
  }, []);
  return null;
}
