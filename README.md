# Mindworks website (draft)

A single self-contained static page (`index.html`): no build step, so it can be hosted anywhere (Netlify, Cloudflare Pages, GitHub Pages, or your current host).

## Design system ("Atmosphere")
- **Type:** Fraunces (light display, italics for emphasis) + Inter Tight (body) + JetBrains Mono (small labels).
- **Colour:** warm cream `#F5F0E8` and sand `#EAE1D3`, moss ink `#1F2A24`; a slow canvas mesh gradient (apricot, sage, lilac, sky) under fine grain. One accent: deep moss `#2F4A3A`, used only for the primary action.
- **Motif:** liquid glass. A glass lens drifts over the hero gradient and follows the cursor; the nav is a floating glass capsule.
- **Motion:** blur-to-sharp reveals, and one pinned scroll scene ("a day in the life of a signal") where an orb travels the six stack layers while the background moves from dawn to night. Everything respects `prefers-reduced-motion`, and canvases pause when off screen.

## Files
- `index.html`: the site
- `logo.svg`, `logo-dark.svg`: vector logo (light and dark backgrounds), redrawn in Marcellus from the original PNG
- `favicon.svg`: browser tab icon
- `fonts/`: self-hosted, Latin-subset web fonts, so the site makes no third-party requests and sets no cookies

## Status
All content is filled in. Optional later additions: Companies House number in the footer, dates on the case studies.
