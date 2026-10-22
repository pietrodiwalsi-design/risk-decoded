# Risk Decoded — Automated Cartoon Video Pipeline
## Requirements Specification v1.1

**Status:** Draft for Peter's approval · 2026-10-02 · **v1.1** (aligned with ROLES-AND-ORCHESTRATION rev 3; changes marked "v1.1")
**Previous:** v1.0 · 2026-07-10
**Product in one sentence:** From a written script, automatically produce a narrated, minimalist stick-figure cartoon explainer on IT-risk / security topics — hosted by "Qubit" — rendered in code, published to YouTube as long-form + Shorts, at near-zero marginal cost.
**Scope rule:** Everything serves the core loop **Script → Voice → Animate → Compose → Publish.** Features that don't are backlog (§H).

**Changes in v1.1:**
1. Orchestrator is no longer "Claude Code" throughout: by hand on Peter's Mac until M2, Moshe (OpenClaw) from M3 (§B, §E).
2. `scenes.json` is a committed artefact; that is how determinism is met (FR-C2, FR-C3).
3. The pipeline stops at an upload-ready package. The YouTube upload happens outside OpenClaw and the token never sits on the Hetzner box (FR-P1, FR-O1, NFR-3, §G).
4. Shorts length: 60 s default target, 180 s platform maximum (FR-S1).
5. Provider-side spend caps added (NFR-4); human-authorship evidence added (NFR-8).

---

## A. Product summary

| | |
|---|---|
| Channel | "Risk Decoded" (working title) — cartoon IT-risk / security explainers |
| Host | **Qubit** — vector/stick-figure mascot, animated in code (Remotion) |
| Formats | Long-form 5–8 min + 2–4 auto-derived Shorts (9:16) per episode |
| Language | English (v1); dual-language a backlog item |
| Differentiator | Real IT-risk expertise + consistent mascot + legible on-screen frameworks + verified accuracy |
| Infra | Self-hosted on Hetzner; open-source-first; minimal vendor lock-in |
| Cadence target | 1 long-form/week once pipeline is stable |

**Design pillars:** (1) code-rendered, not generative-video, for consistency + cost; (2) accuracy is a gate, not an afterthought; (3) reproducible + config-driven; (4) privacy/secret hygiene by default.

---

## B. Actors (v1.1)

- **Author (Peter):** writes/approves scripts, approves character + style, approves each episode, uploads and publishes.
- **Phase 1 builder (Claude, on Peter's Mac):** designs Qubit and hand-builds the Episode 1 pilot with Peter up to M2.
- **Orchestrator from M3 (Moshe / OpenClaw on Hetzner):** Gemini triggers the pipeline stages and drafts scene splits, stills, Shorts picks and metadata. Sonnet inside OpenClaw builds the pipeline code on `moshe/*` branches.
- **Independent gate (Claude, outside OpenClaw):** accuracy and IP checks; review of Moshe's code before Peter merges.
- **Services:** ElevenLabs (voice), Gemini/Nano Banana API (stills), optional Higgsfield (hero clips). YouTube is reached from Peter's side only.

Full routing: ROLES-AND-ORCHESTRATION §3.

---

## C. Functional requirements — core loop

### Script & scene planning (FR-C)
- **FR-C1 — Script intake.** System accepts a Markdown script per the episode template (narration lines, `[beat]` pauses, section tags).
  *AC:* a valid script parses without manual cleanup; malformed scripts fail with a line-referenced error.
- **FR-C2 — Scene decomposition (v1.1).** The orchestrator model drafts an ordered `scenes.json` from the script: each scene has narration text, shot tag (`QUBIT` / `QUBIT+PANEL` / `DIAGRAM` / `SCENE`), on-screen text, asset/prompt references, and target timing. The draft is reviewed and committed.
  *AC:* every narration line maps to exactly one scene; every scene has a valid shot tag; output validates against the scene schema (§F).
- **FR-C3 — Deterministic regeneration (v1.1).** `scenes.json` is a committed artefact. A rebuild reads the committed file and does not call the model again; a new decomposition is an explicit, reviewed action.
  *AC:* rebuilding an episode makes no scene-decomposition model call; the committed `scenes.json` hash is recorded in the manifest (FR-O4).

### Voice (FR-V)
- **FR-V1 — Narration synthesis.** Generate narration audio from scene text via ElevenLabs, using the locked host `voice_id`.
  *AC:* one `narration.mp3` (or per-scene stems) produced; a locked voice_id is used; a missing/invalid voice_id fails fast.
- **FR-V2 — Word-level timing.** Capture word/sentence timestamps for caption + animation sync.
  *AC:* a timing map (per word) is emitted and aligns to audio within ≤80 ms drift on a test clip.
- **FR-V3 — Pronunciation control.** Support a per-channel lexicon for jargon (e.g. "qubit", "ML-KEM", "NIS2").
  *AC:* terms in the lexicon are pronounced per override in a spot-check.

### Character & visual assets (FR-A)
- **FR-A1 — Qubit as code.** The host is a parametric SVG rig animated in Remotion (no generative video for the host).
  *AC:* the same Qubit renders identically across episodes; pose/expression are parameters, not redrawn art.
- **FR-A2 — Expression & motion set.** Qubit supports the defined poses/expressions and the physics demos (spin=superposition, twin+thread=entanglement, ripple=interference).
  *AC:* each named state is renderable via a prop/param; a demo reel exercises all states.
- **FR-A3 — Audio-reactive animation.** Qubit pulses/bounces in time with narration; colour-shifts by mood tag (teal/amber/red).
  *AC:* motion visibly tracks the audio envelope; mood tag changes the palette on cue.
- **FR-A4 — Scene stills (optional layer).** Generate scene art / props / thumbnails via Nano Banana (Gemini image API), style-guided by reference images.
  *AC:* generated stills match the style bible on review; generation is skippable (episode still renders without it).
- **FR-A5 — Thumbnail generation.** Produce a titled 1280×720 thumbnail per episode.
  *AC:* thumbnail includes legible title text and Qubit; exported at YouTube spec.

### Composition & render (FR-R)
- **FR-R1 — Remotion composition.** A reusable template composes audio + Qubit + panels + diagrams + captions into a timeline driven by `scenes.json` + timing map.
  *AC:* feeding a valid scene set yields a continuous video with no gaps/overlaps; captions are on by default.
- **FR-R2 — Framework/diagram components.** Reusable components for: lower-third, "Myth vs Reality" card, framework panel, term pop-up, timeline, progress dots, intro/outro.
  *AC:* each component renders from data props; adding a bullet is a data change, not a re-layout.
- **FR-R3 — Deterministic render.** Same inputs ⇒ same output video (excluding audio-encoder nondeterminism).
  *AC:* two renders of the same episode are frame-identical on a sampled hash.
- **FR-R4 — Long-form output.** Export 1920×1080 H.264 MP4 at channel spec.
  *AC:* file plays in standard players; loudness normalised to a target LUFS.

### Shorts derivation (FR-S)
- **FR-S1 — Auto cut-downs (v1.1).** From the long-form, derive the Shorts defined in the episode file (scene ranges → 9:16, burned-in captions, end card). Default target ≤60 s; the platform maximum is 180 s.
  *AC:* each configured short renders as a standalone 1080×1920 MP4 with captions and CTA, within the configured length and never above 180 s.
- **FR-S2 — Safe-area reframe.** Qubit + key text stay within the vertical safe area.
  *AC:* no critical element is cropped in a vertical spot-check.

### Publishing (FR-P)
- **FR-P1 — Upload package and draft upload (v1.1).** The pipeline produces an upload-ready package per asset: video file, title, description, tags, thumbnail. The upload to YouTube as **private** is done by Peter in YouTube Studio, or by a small script on Peter's Mac that hard-codes `private` (ROLES §8.3). The YouTube credential never sits on the Hetzner box or inside OpenClaw.
  *AC:* the package is complete per asset; after upload, assets appear in YouTube Studio as private; no YouTube credential exists on the Hetzner box.
- **FR-P2 — AI-content disclosure.** Set the "altered/synthetic content" disclosure on every uploaded asset.
  *AC:* the disclosure is set on every uploaded asset; the review packet (FR-Q4) lists it as a check.
- **FR-P3 — Human publish gate.** No video goes public without explicit author action in YouTube Studio.
  *AC:* publishing is a separate, manual step; default state is private.

### Orchestration & config (FR-O)
- **FR-O1 — One-command episode build (v1.1).** A single command runs script → … → upload package, driven by a per-episode config (§F).
  *AC:* `make episode EP=ep01` (or equiv.) produces render + shorts + upload package + review packet.
- **FR-O2 — Resumable stages.** Each stage caches output; re-runs skip completed, unchanged stages.
  *AC:* re-running after the voice stage does not re-synthesise unchanged audio.
- **FR-O3 — Cost guardrails.** Per-run caps on paid API calls (image count, TTS characters, optional video credits).
  *AC:* exceeding a cap stops cleanly with a partial-artefact report; no silent overspend.
- **FR-O4 — Provenance.** Every artefact records config hash, input script hash, tool + model versions, and executor (`moshe-gemini|moshe-sonnet|claude|code`).
  *AC:* a manifest ties each output back to its exact inputs.

### Accuracy & QA gate (FR-Q)
- **FR-Q1 — Accuracy pass (v1.1).** Before any asset is generated, Claude outside OpenClaw fact-checks the script; claims needing sources are flagged. The stack that builds an episode does not sign it off.
  *AC:* the build refuses to proceed past a script with unresolved `[[CHECK]]` flags unless overridden with a logged acknowledgement.
- **FR-Q2 — Myth-busting check.** Flag common misconceptions on the topic and confirm the script addresses or avoids them.
  *AC:* a myth checklist is attached to the episode.
- **FR-Q3 — IP hygiene scan.** Flag real logos, named individuals, or employer references in script/assets. Run by Claude outside OpenClaw.
  *AC:* flagged items block publish until resolved.
- **FR-Q4 — Pre-publish review packet.** Produce a one-page review (runtime, captions on, disclosure set, accuracy notes, thumbnail) for author sign-off.
  *AC:* packet generated per episode; sign-off recorded.

---

## D. Non-functional requirements

- **NFR-1 — Reproducibility.** Every episode is rebuildable from `config + script + committed scenes.json`; assets are regenerable. *AC:* deleting `/build` and rebuilding yields an equivalent episode.
- **NFR-2 — Cost.** Target marginal cost/episode ≤ ~€10 (voice + a few stills); host + composition are free (code). *AC:* the cost report per episode stays under target for a standard episode.
- **NFR-3 — Self-hosting & privacy (v1.1).** Pipeline runs on Hetzner; only the configured external APIs are contacted. *AC:* documented egress from the Hetzner box = ElevenLabs, Gemini, Anthropic (+ optional Higgsfield). YouTube is contacted from Peter's Mac only.
- **NFR-4 — Secret hygiene (v1.1).** API keys live outside the repo tree and outside the OpenClaw workspace; a gitleaks pre-push hook blocks credential leaks; keys are rotatable without code change; keys are project-specific with provider-side spend caps. *AC:* gitleaks passes; no secret in git history; keys read from env/secret store; a spend cap is set at each paid provider.
- **NFR-5 — Maintainability.** Config-driven; adding an episode touches data, not code; components documented. *AC:* a new episode requires no changes under `/src` for standard formats.
- **NFR-6 — Performance.** A standard episode renders within an acceptable wall-clock budget (target ≤ ~30 min unattended). *AC:* measured on the reference episode.
- **NFR-7 — Accessibility.** Captions on by default; AA colour contrast; ≥ readable min font size. *AC:* contrast + caption checks pass on the reference episode.
- **NFR-8 — Compliance (v1.1).** YouTube synthetic-content disclosure always set; no fear-bait; sober risk framing. Each episode carries evidence of human authorship (Peter's script, a recorded review, visual variation between episodes) so the channel stays clear of YouTube's inauthentic-content policy. *AC:* FR-P2 + editorial checklist enforced; sign-off recorded per episode.
- **NFR-9 — Observability.** Each run logs stage timings, API usage, costs, and a pass/fail summary. *AC:* a run report is written per build.
- **NFR-10 — Portability.** No hard dependency on a single generative vendor; image/video providers are swappable behind an interface. *AC:* swapping the image provider touches one module.

---

## E. Tech stack decisions

| Layer | Choice | Rationale |
|---|---|---|
| Orchestration (v1.1) | By hand on the Mac until M2; Moshe / OpenClaw (Gemini triggers, Sonnet builds) from M3 | Prove the format first; then reuse the always-on runner |
| Accuracy + IP gate (v1.1) | Claude outside OpenClaw | Build and sign-off stay separate |
| Voice | ElevenLabs API (`eleven_multilingual_v2`; audition v3 when locking the voice) | Strong TTS + word timings; EN now, NL later |
| Host + composition | **Remotion (React/TS)** | Deterministic, code-rendered, free for a solo user, perfect consistency |
| Stills / thumbnails | **Nano Banana (Gemini image API)** | Cheap, strong consistency + text rendering; free manual tier via Peter's Gemini Pro sub |
| Optional motion | Higgsfield Cloud API | Only if a rare hero clip is wanted; otherwise unused |
| Render | Remotion + ffmpeg (Mac in Phase 1; ephemeral Hetzner worker in production) | Self-hosted, no per-render fee |
| Publish (v1.1) | Manual upload in YouTube Studio, or a Mac-side script | Publish credential stays with Peter |
| Source control | Git, `fable/*` and `moshe/*` branch workflow | Review before `main` |
| Secrets | env / secret store outside tree + gitleaks pre-push + provider spend caps | Peter's existing hardening pattern |

---

## F. Config & data schema (per episode)

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
  lexicon: "config/lexicon.en.yaml"
host:
  character: "qubit"            # Remotion SVG rig — no generative video
image:
  provider: "nano_banana"       # gemini image api; used for stills/thumbnails only
  max_images: 8                 # FR-O3 cost cap
  style_refs: ["assets/style/qubit_ref_*.png"]
video_motion:
  provider: "none"              # or "higgsfield"; 0–2 hero clips max
render:
  template: "risk-decoded-v1"
  captions: true
  resolution: "1920x1080"
  loudness_lufs: -14
outputs:
  long_form: true
  shorts: ["short_a", "short_b", "short_c"]
  short_max_sec: 60             # v1.1 — platform maximum is 180
publish:
  youtube: "package"            # v1.1 — package|off; the pipeline never uploads or publishes
  ai_disclosure: true
qa:
  require_accuracy_pass: ***
  block_on_ip_flags: true
```

`scenes.json` (per scene, committed): `id, order, shot ∈ {QUBIT,QUBIT+PANEL,DIAGRAM,SCENE}, narration, on_screen_text, assets[], qubit_state, mood ∈ {calm,caution,threat}, t_start, t_end`.

---

## G. Acceptance — "definition of done" for v1 (v1.1)

The pipeline is v1-complete when: a new episode is produced from `config + script + committed scenes.json` via one command; Qubit is consistent and audio-synced; captions on; long-form + 3 Shorts render; an upload package with thumbnail is produced and uploaded as a **private** YouTube draft with AI disclosure by Peter's own action; the QA packet is generated; total marginal cost is within NFR-2; no secret is in the repo; and no YouTube credential is on the Hetzner box.

---

## H. Backlog (explicitly out of scope for v1)

Dual-language (NL) tracks · auto music selection/scoring · B-roll library · A/B thumbnail testing · analytics feedback loop into topic selection · comment triage · multi-host/guest characters · full auto-publish (stays manual by policy) · web dashboard for the pipeline.

---

## I. Open decisions (confirm before build)

1. **Channel name** — "Risk Decoded" placeholder; confirm or replace.
2. **Qubit final look** — approve after the concept pass (Nano Banana → SVG).
3. **Voice** — lock one ElevenLabs voice_id (accent/energy).
4. **Repo location** — resolved: `pietrodiwalsi-design/risk-decoded`.
5. **Render host** — see ROLES §8.1.
6. **Cadence** — weekly long-form target confirmed?
7. **(v1.1)** Draft upload method, key location, and channel goal — see ROLES §8.3, §8.6, §8.7.
