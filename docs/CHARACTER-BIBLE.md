# Character Bible — "Risk Decoded" expert team (v0.2, 2026-10-23)

Status: v0.4 (2026-10-24, Burt and Clip redesigned for IP distance). Format, cast, renames approved 2026-10-23. **Visual style DECIDED: option D, shaded SVG rigs built in Remotion, white stick limbs + teal hands/feet** (Peter, 2026-10-24). Inspector Clip is an **owl**. Supersedes CHANNEL-BIBLE §2 ("Qubit hosts all episodes").

---

## 1. Format

**One narrator + a team of expert characters.**
- **Narrator:** voice only (the locked "Peter" ElevenLabs voice). Never on screen. Opens and closes every episode, frames the question, delivers the "what to do" beat. The narrator voice is the constant of the channel.
- **Experts:** one lead expert per domain, recurring across that domain's episodes. Experts also **speak** (own ElevenLabs voice each) and carry the gags and catchphrases. The narrator explains; the expert embodies the problem.
- **Cameos:** experts may appear briefly in each other's episodes (Qubit in an AI episode, Inspector Clip in a quantum-risk episode) — builds the franchise without extra cost.
- **Series:** one playlist per domain, named after the expert domain (e.g. "Quantum", "AI Risk", "Regulation").

## 2. Visual style — DECIDED (option D)

**Decision (Peter, 2026-10-24):** after side-by-side tests (flat vector, Nano Banana painted, shaded SVG), Peter chose **D: shaded SVG rigs built in Remotion, designed after the Nano Banana concepts**. Reason: simple graphic look fits explaining IT risk, calmer than the painted versions ("te levendig"), fully code-animated, own authorship of the art, no per-episode generation cost. Limbs are **white (off-white) sticks**; hands and feet teal.

**Shared cast DNA (all characters, Qubit included):**
1. Dot eyes with white glint (scleral eyes on masked/owl characters); calm expressions, expressive brows.
2. Thin off-white stick limbs; **teal hands and feet** (`#18C3B4`) as family mark.
3. Ink contour; one signature accent colour per character besides teal (Artie metal/blue, Clip owl brown/olive, Burt olive/beige, Glitch purple).
4. Soft top-left key light via SVG gradients plus a shade overlay; teal rim. No texture, no grain.
5. IP check: original design, no resemblance to a known character or mascot, no real names, logos or employer.

**IP check status (2026-10-24, desk comparison only, not a trademark search):**
- Clip: v1 (blue, round glasses) was closest to Owly (*Oswald*, calm blue owl), Professor Owl (Disney) and Mr. Owl (Tootsie Pop, bespectacled). Changed to v2: tawny plumage, no glasses, red pen. Residual risk low. Before launch of the Clip series: search EUIPO/BOIP for owl-with-clipboard marks; legal review if the channel monetises merchandise.
- Burt: v1 read as a compact Macintosh. Replaced by v2 (tall cabinet, reel eyes).
- Qubit, Artie, Glitch: no match found in this pass; Artie (robot with antenna bulb) and Glitch (masked raccoon in hoodie) are common archetypes; run the same desk check before their first episode.

**Qubit** stays as built (vector with halo/gradient, teal Bloch ring); only the limb colour parameter is shared.

**Build implications**
- Rigs are React/SVG components with parametric limbs; poses = angles, never redrawn.
- Experts speak, so each needs mouth shapes (visemes) driven by the Whisper word timings (`words-ep01.ts` pipeline).
- Build gate per character: base pose set, 5 expressions, mouth shapes, side-by-side frame with Qubit, IP check.
- Superseded options: A (flat vector), B (painted cut-out), C (hybrid). Nano Banana remains concept art and optional scene stills.

---


## 3. Roster

| Character | Domain | Archetype | Personality | Catchphrase (accuracy-corrected) | Build order |
|---|---|---|---|---|---|
| **Qubit** | Quantum computing, crypto | Glowing orb, Bloch ring, minimalist | Fragile, curious, easily stressed — but explains calmly | "Don't measure me! Anything that touches me counts, even stray heat." | Done (Ep01–03) |
| **Artie** | AI risk, hallucinations, prompt injection, EU AI Act | Over-eager intern robot, big smile, mismatched wires | Pathologically confident, gullible | "I have absolutely no idea if this is true, but I made a gorgeous slide deck about it." | Proposed #2 |
| **Inspector Clip** (renamed from "Dora") | DORA, NIS2, regulatory compliance | Owl (renamed from badger): warm tawny plumage, navy vest, **no glasses**, stern brows, clipboard, stopwatch, red pen behind the ear tuft | Zero patience for excuses; wants evidence | "Show me the testing logs, or it didn't happen." | Proposed #3 |
| **Burt** | Legacy systems, patching, architecture debt | Tall grimy mainframe cabinet held together with duct tape: vent drawers, status LEDs, hanging cable, **two tape reels as eyes** (no single-screen box) | Exhausted survivor, terrified of change tickets | "Touch that COBOL line and payments stop." (generic; no pension/insurance reference) | Proposed #4 |
| **Glitch** | Cyber threats, supply chain | Shadowy raccoon/chameleon in a hoodie | Opportunistic, pragmatic | "Why hack the firewall when I can phish the vendor's helpdesk?" (no personal names) | Proposed #5 |

**Why the changes vs the Gemini draft**
- Qubit: the original catchphrase ("If you look, I collapse") restates the observer myth that Ep01 scene 14 busts. Corrected to measurement/interaction.
- "Dora" evokes Dora the Explorer (Nickelodeon) → IP hygiene → renamed.
- Burt/Glitch lines: removed "pension fund" (reads as a statement about real pension systems and the author's own field) and "Dave" (a named individual).

## 4. Character rules

- **Accuracy gate applies to jokes too.** A gag may exaggerate, it may not state or imply a wrong fact. The catchphrases above are pre-cleared; new ones go through the gate.
- **Artie** hallucination gags are always followed by the real mechanism and the mitigation (no "AI is dumb" without the "what to do" beat).
- **Glitch** stays conceptual: explains how attacks work at the level of risk understanding, never operational instructions. No fear-bait.
- **Inspector Clip** regulatory claims are cited at the gate. To verify against primary text: DORA = Regulation (EU) 2022/2554; NIS2 = Directive (EU) 2022/2555; EU AI Act = Regulation (EU) 2024/1689. Scope statements (who is in scope) are claims and need a source line each.
- **Burt** jokes target the systems and the change process, never named vendors or products.
- Each expert may only speak inside their own domain; outside it they defer ("Ask Inspector Clip").

## 5. Build gate (cost control)

A character is built **only when an episode needs it**, not on a roadmap alone. Definition of done:
1. Rig (shaded SVG, option D) with the base pose set (idle, talking, pointing L/R, aha, worried, thumbs-up) and 5 expressions.
2. 1–2 signature gags (like Qubit's coin/snap).
3. Contact sheet render (like `QubitSheet`) approved by Peter.
4. Voice chosen, license for commercial use checked **per voice** (library voices can differ from own-clone terms) and recorded.
5. Added to the voice map in config.
6. **Talking:** experts speak, so each needs 4–6 mouth shapes (or an equivalent speech animation) driven by the word timings (Whisper pipeline already in place). Qubit's motion-only speech is not enough for characters with faces.

## 6. Pipeline impact (for Moshe, after approval)

- `scenes.json`: add `speaker` per scene or per line (`narrator` | `qubit` | `artie` | …) and `characters_on_screen`.
- Config: `voices:` map `speaker → voice_id`; ElevenLabs TTS per speaker; captions colour-coded by speaker.
- Script format: dialogue lines prefixed `[ARTIE]:`; narrator lines unprefixed.
- Word-timing (Whisper) per clip as in Ep01; mix: music ducking unchanged.
- Remotion: shared `Character` base component (rig + moods) so a new expert is data + art, not new engineering.

## 7. Channel branding assets (concept → production)

| Asset | Recommendation | Why |
|---|---|---|
| **Profile picture** | Neutral brand mark ("RD" lettering or a stylised decoder/lens mark), flat vector, teal on slate | A single character (Qubit) ties the channel to quantum |
| **Banner** | Ensemble: only characters that exist or are scheduled; Qubit prominent; safe zone centre | Promise only what you deliver |
| **Banner size** | 2560×1440 (YouTube minimum, as far as I know, 2048×1152), key content inside the centre safe area | The generated 1998×1116 file is below the minimum |
| **Style** | Follow option D (§2). Current glossy Gemini versions = concept art for now | One look across channel and videos |
| **Formulas/code on the banner** | Remove gibberish, or use correct ones (e.g. |0⟩ + |1⟩) | Accuracy-first channel |

## 8. Channel text (to apply to CHANNEL-BIBLE §1)

Name: **RiskDecoded** · Handle: **@RiskDecodedHQ** · Cadence: not fixed yet.

Proposed description:
> Serious tech risk, explained with cartoons.
>
> From quantum threats to AI failures, DORA and NIS2: RiskDecoded turns complex IT risk, security and operational resilience into clear, accurate explainers for leaders and practitioners. Meet the expert team.
>
> 🔔 Subscribe to stay ahead of the technical and regulatory curve.
>
> Educational content, not legal or professional advice. Narration and character voices are AI-generated; visuals are AI-assisted. Independent channel, not affiliated with any company or organisation.

("Unfiltered" and "from the inside out" removed: accuracy-first brand; no insider/employer implication.)

## 9. Nano Banana prompts (concept art only; rebuild as SVG)

Prepend the base style prompt from `qubit-nano-banana-prompts.md`, then:

**Profile picture (neutral mark)**
> Flat vector circular brand mark for a channel called "RiskDecoded": bold geometric letters "RD" inside a stylised magnifying-lens/decoder ring, thick near-black outline, teal #18C3B4 and amber #F4A63B accents on deep slate #0F1E2E, centred, lots of negative space, no gradients, no glow, no photorealism, no tiny text. Must stay readable at 48×48 px.

**Banner (ensemble)**
> Wide YouTube channel banner, 2560×1440, illustrated cartoon explainer style with thick near-black outlines and soft shading (not photorealistic, not glossy 3D). Deep slate background #0F1E2E with faint circuit/grid lines. Centre: bold title "RiskDecoded" in a geometric sans with teal #18C3B4 "Decoded", tagline underneath "Serious tech risk. Clear explanations." All text and key characters inside the centre safe area (about 1546×423). Left: a friendly glowing orb character with a thin ring, two dot eyes with white glints, stick limbs, teal hands and feet. Right: a small robot intern and a badger inspector with a clipboard, same style and lighting, teal hands and feet. No code, no equations, no logos.

**Character sheets (one per expert, same template as Qubit §1–3)**
> [Base style]. A cartoon <ROBOT INTERN / OWL INSPECTOR WITH CLIPBOARD / GRIMY 1990s MAINFRAME / HOODED RACCOON>, <style per chosen approach>, thick near-black outline, two dot eyes with white glint, teal #18C3B4 hands and feet, one signature accent colour <amber / red / olive / purple>. Show the SAME character from 5 angles, neutral expression, consistent proportions. Then: grid of 5 expressions and a grid of poses (idle, talking, pointing right, arms-up "aha", worried, thumbs-up).

## 10. Open decisions

1. ~~Visual approach~~ DECIDED: option D (§2). Next: mouth shapes, IP checks (owl, Burt), banner and pfp redo.
2. Frequency (not fixed).
3. Voices for Artie, Inspector Clip, Burt, Glitch (own clones? library? commercial licence check per voice).
4. Banner/pfp: neutral pfp, ensemble banner at 2560×1440, style per §2.
5. CHANNEL-BIBLE §1–2, §5, §6.3 and ROLES/REQUIREMENTS wording to be updated after approval.
