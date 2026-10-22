# Risk Decoded — Automated Cartoon Explainer Pipeline

Cartoon IT-risk / security explainers hosted by **Qubit**, produced from a written script by an automated pipeline and published to YouTube as long-form + Shorts, at near-zero marginal cost.

**Status:** Phase 1 — format proof, by hand on Peter's Mac (Qubit look, voice, Episode 1 pilot = the M2 gate). Phase 0 scaffold is done; the pipeline is not yet wired to services.
**Owner:** Peter · **Agents:** Moshe (OpenClaw on Hetzner: Gemini triggers and drafts; Sonnet builds the pipeline from M3 on `moshe/*` branches), Claude/Fable (design, accuracy + IP gate, code review — outside OpenClaw).

*Updated 2026-10-22: aligned with ROLES rev 3 / REQUIREMENTS v1.1 / BUILD-EXECUTION-PLAN v1.1. See `MOSHE-UPDATE-2026-10-22.md` for what changed and the decisions taken.*

---

## Documents (read in this order)

1. **REQUIREMENTS.md** (v1.1) — what the pipeline must do (FR/NFR + acceptance criteria, schemas, stack decisions).
2. **BUILD-EXECUTION-PLAN.md** (v1.1) — architecture, repo layout, phased delivery (M1–M6), risks, cost.
3. **ROLES-AND-ORCHESTRATION.md** (rev 3) — who runs each stage (Moshe / Claude / Peter / code), Hetzner topology fit, capacity, governance.
4. **CHANNEL-BIBLE.md** — Qubit character, visual style, Remotion component set, per-episode config schema.
5. **MOSHE-UPDATE-2026-10-22.md** — latest changes and decisions; where it conflicts with the docs above, it wins until they are re-issued.

Scripts live in `scripts/`; the first three episodes (quantum trilogy) are drafted.

---

## Repository layout

```
risk-decoded/
├─ README.md                      ← you are here
├─ REQUIREMENTS.md · BUILD-EXECUTION-PLAN.md · ROLES-AND-ORCHESTRATION.md · CHANNEL-BIBLE.md
├─ MOSHE-HANDOFF.md · MOSHE-UPDATE-2026-10-22.md
├─ Makefile                       ← `make episode EP=ep01` (stubs until Phase 3)
├─ .gitignore · .githooks/pre-push (gitleaks)
├─ config/
│  ├─ channel.yaml                ← palette, fonts, render + provider defaults
│  ├─ lexicon.en.yaml             ← jargon pronunciation for TTS
│  ├─ scene.schema.json           ← schema for generated scenes.json
│  └─ episodes/ep0{1,2,3}.yaml    ← per-episode config
├─ scripts/ep0{1,2,3}-*.md        ← source narration scripts + scene breakdowns
├─ scenes/                        ← committed scenes.json per episode (from M3)
├─ src/
│  ├─ orchestrator/               ← stage runners, caching, cost caps, provenance (Phase 3)
│  ├─ providers/                  ← elevenlabs · image(nano_banana) · motion (Phase 3). No YouTube provider.
│  └─ remotion/                   ← Qubit rig + components + compositions (Phase 1–2)
├─ assets/{style,generated}/      ← style refs (committed) · generated stills (ignored)
└─ build/                         ← per-episode artefacts (ignored)
```

---

## Pipeline (target)

`script.md (+config)` → **accuracy + IP gate (Claude, outside OpenClaw)** → **scenes.json** (drafted once, reviewed, committed) → **voice** (ElevenLabs) → **Nano Banana** stills → **Remotion** (Qubit + panels + captions) → **ffmpeg** render + Shorts → **upload package** (video, title, description, tags, thumbnail, review packet) → Peter uploads as private in YouTube Studio → review → Peter publishes by hand.

Until the M2 pilot is approved the pipeline is assembled by hand on Peter's Mac. From M3, Moshe (Gemini) triggers the stages on the Hetzner CPX32 box; the stages themselves are plain code. Where production renders run is decided at M3 (options: Peter's Mac, CPX32 with low concurrency, ephemeral render server). No YouTube credential is held on the Hetzner box.

---

## Quickstart (once Phase 3 lands)

```bash
make validate EP=ep01     # parse script + validate scenes.json against schema
make voice   EP=ep01      # narration + word timings
make stills  EP=ep01      # Nano Banana scene art / thumbnail (optional)
make render  EP=ep01      # Remotion long-form
make shorts  EP=ep01      # cut vertical Shorts
make package EP=ep01      # upload package + review packet (never uploads)
make episode EP=ep01      # all of the above
```

## Conventions

- Claude/Fable work on `fable/*` branches, Moshe on `moshe/*`; merge to `main` only after Peter's review.
- Code written by Sonnet in OpenClaw is reviewed by Claude outside OpenClaw before Peter merges.
- Secrets live **outside** the repo tree and outside the OpenClaw workspace; `.githooks/pre-push` runs gitleaks. Never commit keys or media.
- Nothing publishes to public automatically — upload and publish are Peter's manual actions. Telegram is notification-only.
- No pipeline engineering (Phases 2–4) by Moshe until the M2 pilot is approved.

## Decisions and open items (see ROLES §8)

Decided 2026-10-22: render on Peter's Mac for now · manual upload in YouTube Studio · channel goal: credibility first, monetisation second · escalation: halt and Telegram Peter after two failed schema validations.
Still open: key location check (ROLES §8.6) · model pinning confirmation (§8.4) · voice provider (ElevenLabs vs a local generator) · channel name · cadence.
