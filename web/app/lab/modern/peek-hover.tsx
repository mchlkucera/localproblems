"use client";
// /lab/modern — hover-intent and focus-to-open for the citation peeks.
//
// PROGRESSIVE ONLY. Without this file every pill still opens its card on
// click/tap/Enter (native `popovertarget`), Escape and an outside click still
// close it, and every link still works. What this adds:
//   · mouse: rest on a pill ~140ms → the card opens; move into the card and it
//     stays; leave both → it closes after a short grace.
//   · keyboard: Tab onto a pill → the card opens (Tab again moves into it).
//   · click on a card opened by hover/focus PINS it instead of toggling it
//     shut, so "hover, then click to keep it" behaves the way Perplexity does.
// One document-level listener set; no per-pill hydration.
import { useEffect } from "react";

type Mode = "hover" | "focus" | "pinned";

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
      if (e.pointerType !== "mouse") return;
      if (pillOf(e.target)) window.clearTimeout(openT);
      if (cur && !inside(e.relatedTarget) && (inside(e.target))) hideSoon();
    };
    const onFocusIn = (e: FocusEvent) => {
      const btn = pillOf(e.target);
      if (btn && btn.matches(":focus-visible")) show(btn, "focus");
    };
    const onFocusOut = (e: FocusEvent) => {
      if (cur && cur.mode === "focus" && inside(e.target) && !inside(e.relatedTarget)) hide();
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

    document.addEventListener("pointerover", onOver);
    document.addEventListener("pointerout", onOut);
    document.addEventListener("focusin", onFocusIn);
    document.addEventListener("focusout", onFocusOut);
    document.addEventListener("click", onClick, true);
    document.addEventListener("toggle", onToggle, true);
    return () => {
      document.removeEventListener("pointerover", onOver);
      document.removeEventListener("pointerout", onOut);
      document.removeEventListener("focusin", onFocusIn);
      document.removeEventListener("focusout", onFocusOut);
      document.removeEventListener("click", onClick, true);
      document.removeEventListener("toggle", onToggle, true);
      window.clearTimeout(openT);
      window.clearTimeout(closeT);
    };
  }, []);
  return null;
}
