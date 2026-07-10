# src/remotion (Phase 1–2)

The code-rendered heart of the channel. Everything on screen is React/SVG → deterministic, consistent, near-free.

- **Qubit/** — the host rig: parametric SVG (two-limb "stick" rig), poses/expressions, and the physics demos (spin=superposition, twin=entanglement, ripple=interference). Audio-reactive pulse; mood-driven palette (FR-A1/A2/A3).
- **components/** — lower-third, Myth-vs-Reality card, framework panel, term pop-up, timeline, progress dots, intro/outro, caption layer (FR-R2). All data-driven props.
- **compositions/** — `LongForm.tsx` (drives from scenes.json + timings) and `Short.tsx` (9:16, safe-area, burned captions, CTA) (FR-R1/S1/S2).

Build order (Phase 1): design Qubit → base components → hand-assemble Episode 1 to lock `risk-decoded-v1` template → then parameterise (Phase 2). This is the M2 quality gate.
