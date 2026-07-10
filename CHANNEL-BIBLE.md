# Channel Bible — "Risk Decoded" (working title)

Reusable across every episode. Lock this once; each episode plugs into it.

---

## 1. Channel positioning

**One line:** Cartoon explainers that make IT risk, security, and emerging-tech threats genuinely understandable — accurate enough for professionals, clear enough for everyone.

**Differentiator vs generic AI channels:** a real IT-risk professional's judgement + a consistent host + legible on-screen frameworks and diagrams. We explain what things *are not* as clearly as what they are. No hype, no fear-bait, no wrong physics.

**Audience:** IT/risk/security professionals + curious generalists (execs, students). English.

**Cadence:** one long-form episode (5–8 min) → auto-cut into 2–4 Shorts.

---

## 2. Host character — "Qubit" (the mascot)

> The host is a character, not a human: **Qubit** — a friendly, minimalist qubit who narrates every episode. Designed as a simple vector / stick-figure-style figure so it animates entirely in code (Remotion): no generative-video lip-sync, trivial consistency, near-zero per-episode cost. Topic-agnostic — Qubit hosts *all* IT-risk episodes, not just quantum.

**Form:** a glowing sphere/orb with a simple face (two dot eyes; expressive but minimal) and thin stick-figure limbs for gesturing and pointing. Reads instantly at any size, including tiny Shorts thumbnails.
- **Quantum-native motif:** the body carries a faint Bloch-sphere ring/axis — for the quantum series, Qubit *is* the thing being explained.
- **Re-skinnable per topic:** Qubit holds props or briefly morphs (a padlock shell for crypto episodes, a data-cube for data-risk) while staying recognisably the same character.

**Personality:** calm, sharp, curious, lightly witty. Peer-to-peer — explains *to* you, never *down*.
**Expression via motion, not a mouth:** pulses/bounces in time with the narration, squashes for emphasis, colour-shifts for mood (teal = explaining, amber = caution, red = threat). **No lip-sync needed — the single biggest production win.**
**Voice:** one locked ElevenLabs voice ID — warm, measured, mid-pitch, clear, light energy. Pick once; it becomes brand. (Record the `voice_id` into the config.)
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

---

## 3. Visual style bible

**Overall style:** minimalist vector / stick-figure explainer — clean lines, bold simple shapes, generous negative space, a hand-drawn-adjacent charm (the whiteboard/stick-figure explainer look referenced). Not anime, not photoreal, not "AI-glossy." Everything is drawable as SVG so it renders in code (Remotion), which is what makes Qubit consistent and near-free to animate.

**Palette (define hex once, reuse everywhere):**
- Background base: deep slate `#0F1E2E` (dark) with a light-panel variant `#F4F6F9` for diagram frames.
- Primary accent (host signature + highlights): electric teal `#18C3B4`.
- Secondary accent (risk/alert beats): warm amber `#F4A63B`; danger red `#E4572E` for threats only.
- Text: near-white `#F7FAFC` on dark, near-black `#14171A` on light.

**Typography:** one geometric sans for headings (e.g. Inter/Poppins-style), same for captions. Big, legible, high-contrast. Captions always on (accessibility + silent autoplay on Shorts).

**Recurring motion-graphic components (built once in Remotion):**
- Intro sting (2–3s) + logo.
- Lower-third name/topic bar.
- "Framework panel" — a titled box for diagrams, bullet reveals, tables.
- "Myth vs Reality" split card (used constantly on this channel).
- Term pop-up (glossary chip when a jargon word appears).
- Progress dots / chapter markers.
- Outro card (subscribe + next-episode teaser).

**Shot vocabulary (each scene is tagged one of these):**
- `QUBIT` — Qubit narrating on screen (Remotion vector animation, audio-reactive pulse — no generative video, no lip-sync).
- `QUBIT+PANEL` — Qubit to the side, framework panel fills the rest (all Remotion).
- `DIAGRAM` — full-screen motion graphic, voiceover only (pure Remotion — cheapest, most legible).
- `SCENE` — illustrated metaphor beat; usually still Remotion vector (Qubit acting it out). Reserve optional generated art/motion for rare hero flourishes only.

**Cost rule of thumb:** the whole episode — Qubit included — renders in Remotion. Generative tools (Higgsfield / image models) become *optional*, used for at most 0–2 hero flourishes or scene art. This drops per-episode AI cost close to zero.

---

## 4. Production pipeline (per episode)

```
script.md
  └─ Claude: split into scenes → scenes.json (narration + shot tag + prompts + on-screen text)
      ├─ ElevenLabs API        → narration.mp3 + word-level timestamps
      ├─ (optional) image gen  → scene art / thumbnails only (Nano Banana / etc.)
      ├─ (optional) Higgsfield → 0–2 hero flourish clips only, if any
      └─ Remotion (React)      → animates Qubit + panels + diagrams + captions (the whole episode)
           └─ ffmpeg render   → episode.mp4  (+ auto-cut shorts_*.mp4)
                └─ YouTube Data API → upload draft (title, desc, thumb, tags)
```
Orchestrated by Claude Code from a per-episode config; runs on your Hetzner box; git-tracked.

---

## 5. Per-episode config schema

```yaml
episode:
  id: "ep01"
  title: "Quantum Computers, Explained (Without the Hype)"
  language: "en"
  target_runtime_sec: 380
voice:
  provider: "elevenlabs"
  voice_id: "REPLACE_WITH_LOCKED_HOST_VOICE"
  model: "eleven_multilingual_v2"
host:
  character: "qubit"        # animated in Remotion (SVG) — no generative video
  # soul_id only if you use optional Higgsfield hero clips
render:
  template: "risk-decoded-v1"
  captions: true
  resolution: "1920x1080"
outputs:
  long_form: true
  shorts: ["short_a", "short_b", "short_c"]
publish:
  youtube: false   # set true when ready to auto-upload as draft
```

---

## 6. Guardrails (every episode passes these)

1. **Accuracy gate** — Claude fact-checks the script before any asset is generated. IT-risk credibility is the whole brand.
2. **Myth-busting is a feature** — actively state common misconceptions and correct them.
3. **IP hygiene** — original characters only; no real vendor logos, no named individuals, employer name absent.
4. **YouTube synthetic-content disclosure** — enable the "altered/AI content" label; lean on genuine expertise + accuracy so we're on the right side of monetization policy.
5. **No fear-bait** — risks stated soberly with a "what to do" beat. This matches a professional-risk voice.
