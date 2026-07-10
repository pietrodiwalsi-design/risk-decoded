# Qubit — Nano Banana concept prompt set

Use these in the Gemini app (Nano Banana Pro) to explore the character look, then rebuild the chosen direction as a clean SVG rig (the code version is the production asset — generated images are for design exploration only).

## Base style prompt (prepend to all)
> Minimalist flat vector mascot, clean thick outlines, simple geometric shapes, lots of negative space, friendly educational-explainer style (stick-figure charm). Flat colors only, no gradients, no photorealism, no 3D. Palette: teal #18C3B4 accents, off-white #F4F6F9 body, near-black #14171A features, amber #F4A63B highlight. Transparent or plain background.

## 1. Character sheet (identity lock)
> A cute cartoon "qubit" character: a rounded sphere body with a faint Bloch-sphere ring around it, two dot eyes, a friendly smile, and thin stick-figure arms and legs. Show the SAME character in one image from 5 angles: front, 3/4 left, 3/4 right, slight up, slight down. Neutral friendly expression. Consistent proportions.

## 2. Expressions (one image, grid of 5)
> The same qubit character showing five expressions in a grid: neutral, surprised ("plot twist"), concerned (for risk topics), reassuring (for advice), delighted. Same style and proportions throughout.

## 3. Poses (one image, grid)
> The same qubit character in poses: idle, talking (arm open), pointing to the right at an off-screen panel, arms up "aha", worried/slumped, thumbs up. Consistent character.

## 4. Physics demo states (three images)
> a) The qubit spinning — motion blur between two states, to illustrate superposition.
> b) Two identical qubit characters linked by a glowing teal thread, to illustrate entanglement.
> c) The qubit rippling outward like water, some ripples cancelling and one amplifying, to illustrate interference.

## 5. Thumbnail lockup
> The qubit character next to bold large title text, high contrast, designed as a YouTube thumbnail. Leave space for a 3–5 word title. Teal/amber accents on dark.

## Notes
- Keep 14+ reference images consistent by feeding earlier outputs back as reference (Nano Banana Pro supports up to 14 refs).
- Manual generation is covered by Peter's Gemini Pro subscription (~100/day); automation uses the Gemini image API.
- Final host = SVG rig in `src/remotion/Qubit/` (see `qubit-concept-v1.svg`). Images inform the redraw; they are not shipped frame-to-frame.
