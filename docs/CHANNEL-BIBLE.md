# Channel Bible — "RiskDecoded"

Reusable across every episode. Lock this once; each episode plugs into it.

*Updated 2026-10-02: §4–6 aligned with ROLES-AND-ORCHESTRATION rev 3 and REQUIREMENTS v1.1. §1–3 unchanged.*
*Updated 2026-10-23: channel name RiskDecoded, handle @RiskDecodedHQ; format changed to one narrator + expert cast (see CHARACTER-BIBLE and DECISIONS-2026-10-23); §1, §2, §5, §6 amended.*

---

## 1. Channel positioning

**One line:** Cartoon explainers that make IT risk, security, and emerging-tech threats genuinely understandable — accurate enough for professionals, clear enough for everyone.

**Differentiator vs generic AI channels:** a real IT-risk professional's judgement + a consistent narrator voice and a recurring team of expert characters + legible on-screen frameworks and diagrams. We explain what things *are not* as clearly as what they are. No hype, no fear-bait, no wrong physics.

**Audience:** IT/risk/security professionals + curious generalists (execs, students). English.

**Cadence:** one long-form episode (5–8 min) → auto-cut into 2–4 Shorts. Publishing frequency not fixed yet (decide after the first episodes are live).

**Channel:** RiskDecoded, @RiskDecodedHQ. Description: CHARACTER-BIBLE §8.

---

## 2. Cast — narrator and expert characters

> **Amended 2026-10-23.** The channel has **one narrator (voice only, never on screen)** and **a team of expert characters**, one lead expert per domain. Experts speak (own voices) and may cameo in each other's episodes. Full cast, rules, style direction and build gate: **CHARACTER-BIBLE**. Qubit is the **quantum expert**, not the host of every episode.

### 2.1 Qubit (quantum and crypto expert — built)

> Qubit is a friendly, minimalist qubit character, designed as a simple vector / stick-figure-style figure so it animates entirely in code (Remotion): no generative-video lip-sync, trivial consistency, near-zero per-episode cost. Quantum series: Qubit *is* the thing being explained.

**Form:** a glowing sphere/orb with a simple face (two dot eyes; expressive but minimal) and thin stick-figure limbs for gesturing and pointing. Reads instantly at any size, including tiny Shorts thumbnails.
- **Quantum-native motif:** the body carries a faint Bloch-sphere ring/axis.
- **Re-skinnable per topic:** Qubit holds props or briefly morphs (a padlock shell for crypto episodes, a data-cube for data-risk) while staying recognisably the same character.

**Personality:** calm, sharp, curious, lightly witty; fragile under measurement (running gag: *"Don't measure me! Anything that touches me counts, even stray heat."*). Peer-to-peer — explains *to* you, never *down*.
**Expression via motion, not a mouth:** pulses/bounces in time with the narration, squashes for emphasis, colour-shifts for mood (teal = explaining, amber = caution, red = threat). No lip-sync needed for Qubit.
**Voice:** the narrator voice is one locked ElevenLabs voice ID — warm, measured, mid-pitch, clear, light energy (record the `voice_id` into the config). Other experts get their own voices (voice map, see §5).
**Never:** no real logos, no real-person likeness, no employer references.

**Signature demos (the character embodies the physics — reused as needed):**
- Superposition → Qubit spins/blurs between two states.
- Entanglement → a twin Qubit appears, linked by a glowing thread.
- Interference → Qubit ripples; wrong-answer ripples cancel, the right-answer ripple amplifies.

**Asset set (built once as vector/SVG, reused forever — no AI regen):**
- Base poses: idle, talking (pulsing), pointing left/right, arms-up "aha", slumped/worried, thumbs-up.
- Expressions: neutral, surprised, concerned, reassuring, delighted.
- Demo states: spinning (superposition), twinned+linked (entanglement), rippling (interference).
- Two-limb "stick" rig so poses are parametric in Remotion (swap arm/leg angles — never re-draw).

### 2.2 Other experts

Artie (AI risk), Inspector Clip (DORA/NIS2/regulation), Burt (legacy), Glitch (threats): see CHARACTER-BIBLE §3. Built only when an episode needs them (§5 there). Visual approach decided 2026-10-24: shaded SVG rigs, white limbs, teal hands/feet, shared DNA with Qubit (CHARACTER-BIBLE §2).

---

## 3. Visual style bible

**Overall style:** minimalist vector explainer — clean lines, bold simple shapes, generous negative space, a hand-drawn-adjacent charm. Not anime, not photoreal, not "AI-glossy." Everything for Qubit is drawable as SVG so it renders in code (Remotion). *Amended 2026-10-23:* other characters may carry more body (shading, volume) as long as they keep the shared cast DNA (CHARACTER-BIBLE §2) and sit in the same frame as Qubit.

**Palette (define hex once, reuse everywhere):**
- Background base: deep slate `#0F1E2E` (dark) with a light-panel variant `#F4F6F9` for diagram frames.
- Primary accent (signature + highlights): electric teal `#18C3B4`.
- Secondary accent (risk/alert beats): warm amber `#F4A63B`; danger red `#E4572E` for threats only.
- Text: near-white `#F7FAFC` on dark, near-black `#14171A` on light.

**Typography:** one geometric sans for headings (e.g. Inter/Poppins-style), same for captions. Big, legible, high-contrast. Captions always on (accessibility + silent autoplay on Shorts); captions colour-coded per speaker.

**Recurring motion-graphic components (built once in Remotion):**
- Intro sting (2–3s) + logo.
- Lower-third name/topic bar.
- "Framework panel" — a titled box for diagrams, bullet reveals, tables.
- "Myth vs Reality" split card (used constantly on this channel).
- Term pop-up (glossary chip when a jargon word appears).
- Progress dots / chapter markers.
- Outro card (subscribe + next-episode teaser).

**Shot vocabulary (each scene is tagged one of these):**
- `QUBIT` — an expert character on screen (Remotion animation, audio-reactive pulse — no generative video). Tag stays `QUBIT` for Qubit; other experts use their own name as tag.
- `QUBIT+PANEL` — expert to the side, framework panel fills the rest (all Remotion).
- `DIAGRAM` — full-screen motion graphic, voiceover only (pure Remotion — cheapest, most legible).
- `SCENE` — illustrated metaphor beat; usually still Remotion vector (character acting it out). Reserve optional generated art/motion for rare hero flourishes only.

**Cost rule of thumb:** the whole episode — characters included — renders in Remotion. Generative tools (Higgsfield / image models) become *optional*, used for at most 0–2 hero flourishes or scene art, plus one-off character design art. This drops per-episode AI cost close to zero.

---

## 4. Production pipeline (per episode)

```
script.md  (written/approved by Peter)
  └─ Claude, outside OpenClaw: accuracy + IP gate
      └─ Moshe/Gemini: draft scenes.json → reviewed → committed
          ├─ ElevenLabs API        → narration/character clips (per speaker)
          ├─ Whisper (local)       → exact word timestamps → captions + animation timing
          ├─ ffmpeg                → per-clip loudness normalisation (about −15 LUFS)
          ├─ (optional) image gen  → scene art / thumbnails only (Nano Banana)
          ├─ (optional) Higgsfield → 0–2 hero flourish clips only, if any
          └─ Remotion (React)      → animates characters + panels + diagrams + captions + music bed (ducked)
               └─ ffmpeg render   → episode.mp4  (+ auto-cut shorts_*.mp4)
                    └─ upload package (video, title, desc, tags, thumb, review packet)
                         └─ Peter: upload as private → review → publish by hand
```
Until the Episode 1 pilot is approved (M2), this is assembled by hand on Peter's Mac. From M3, Moshe (OpenClaw on Hetzner) triggers the stages from a per-episode config; the stages themselves are plain code, git-tracked. The YouTube upload and the publish step stay with Peter, and no YouTube credential sits on the Hetzner box. Full routing: ROLES-AND-ORCHESTRATION §3.

---

## 5. Per-episode config schema

The authoritative schema is REQUIREMENTS §F. Summary:

```yaml
episode:
  id: "ep01"
  title: "Quantum Computers, Explained (Without the Hype)"
  language: "en"
  target_runtime_sec: 380
voices:                      # amended 2026-10-23: one voice per speaker
  narrator:
    provider: "elevenlabs"
    voice_id: "bTrXJpbeuC5KgriLhQeC"
    model: "eleven_multilingual_v2"
  # qubit / artie / ... : voice_id per expert, commercial licence checked per voice
cast:
  lead: "qubit"              # animated in Remotion — no generative video
  cameo: []
render:
  template: "risk-decoded-v1"
  captions: true
  resolution: "1920x1080"
  music: "ambient-bed-v1"    # own synthesised track, ducked under speech
outputs:
  long_form: true
  shorts: ["short_a", "short_b", "short_c"]
  short_max_sec: 60         # platform maximum is 180
publish:
  youtube: "package"        # package|off — the pipeline never uploads or publishes
  ai_disclosure: true
```
scenes.json carries a `speaker` per scene or line (`narrator` | expert id) and `characters_on_screen`.

---

## 6. Guardrails (every episode passes these)

1. **Accuracy gate** — Claude, outside OpenClaw, fact-checks the script before any asset is generated. IT-risk credibility is the whole brand. This includes the jokes and catchphrases of every character: a gag may exaggerate, it may not state or imply a wrong fact.
2. **Myth-busting is a feature** — actively state common misconceptions and correct them.
3. **IP hygiene** — original characters only; no real vendor logos, no named individuals, employer name absent; no resemblance to known characters or mascots (e.g. no "Dora").
4. **YouTube synthetic-content disclosure** — enable the "altered/AI content" label on every upload; the channel description says narration and character voices are AI-generated.
5. **No fear-bait** — risks stated soberly with a "what to do" beat. This matches a professional-risk voice. The threat character (Glitch) stays conceptual: no operational attack instructions.
6. **Human authorship is visible** — every episode starts from Peter's own script, gets a recorded human review, and varies visually from the last one. This keeps the channel clear of YouTube's inauthentic-content policy, which targets templated, synthetic-voice, fully automated channels.
7. **Voice licensing** — commercial use confirmed for the narrator voice (ElevenLabs reply, 2026-10-23, see DECISIONS-2026-10-23 #17); every additional voice is checked per voice and recorded before first use.
