# Risk Decoded — Automated Cartoon Explainer Pipeline

Cartoon IT-risk / security explainers hosted by **Qubit**, produced from a written script by an automated pipeline and published to YouTube as long-form + Shorts, at near-zero marginal cost.

**Status:** Phase 0 (project skeleton). Not yet wired to services.
**Owner:** Peter · **Agents:** Moshe (OpenClaw, orchestration + grind), Claude/Fable (design + accuracy + engineering).

---

## Documents (read in this order)

1. **REQUIREMENTS.md** — what the pipeline must do (FR/NFR + acceptance criteria, schemas, stack decisions).
2. **BUILD-EXECUTION-PLAN.md** — architecture, repo layout, phased delivery (M1–M6), risks, cost.
3. **ROLES-AND-ORCHESTRATION.md** — who runs each stage (Moshe / Claude / Peter / code), Hetzner topology fit, capacity decision.
4. **CHANNEL-BIBLE.md** — Qubit character, visual style, Remotion component set, per-episode config schema.

Scripts live in `scripts/`; the first three episodes (quantum trilogy) are ready.

---

## Repository layout

```
risk-decoded/
├─ README.md                      ← you are here
├─ REQUIREMENTS.md · BUILD-EXECUTION-PLAN.md · ROLES-AND-ORCHESTRATION.md · CHANNEL-BIBLE.md
├─ Makefile                       ← `make episode EP=ep01` (stubs until Phase 3)
├─ .gitignore · .githooks/pre-push (gitleaks)
├─ config/
│  ├─ channel.yaml                ← palette, fonts, render + provider defaults
│  ├─ lexicon.en.yaml             ← jargon pronunciation for TTS
│  ├─ scene.schema.json           ← schema for generated scenes.json
│  └─ episodes/ep0{1,2,3}.yaml    ← per-episode config
├─ scripts/ep0{1,2,3}-*.md        ← source narration scripts + scene breakdowns
├─ src/
│  ├─ orchestrator/               ← stage runners, caching, cost caps, provenance (Phase 3)
│  ├─ providers/                  ← elevenlabs · image(nano_banana) · motion · youtube (Phase 3)
│  └─ remotion/                   ← Qubit rig + components + compositions (Phase 1–2)
├─ assets/{style,generated}/      ← style refs (committed) · generated stills (ignored)
└─ build/                         ← per-episode artefacts (ignored)
```

---

## Pipeline (target)

`script.md (+config)` → **QA/accuracy** → **scenes.json** → **ElevenLabs** voice → **Nano Banana** stills → **Remotion** (Qubit + panels + captions) → **ffmpeg** render + Shorts → **YouTube draft** → Peter approves (Telegram) → publish.

Orchestrated by **Moshe** (Gemini/Grok) on the Hetzner CPX32 box; heavy renders on an **ephemeral** instance; accuracy + design on **Claude**.

---

## Quickstart (once Phase 3 lands)

```bash
make validate EP=ep01     # parse script + validate scenes.json against schema
make voice   EP=ep01      # ElevenLabs narration + timings
make stills  EP=ep01      # Nano Banana scene art / thumbnail (optional)
make render  EP=ep01      # Remotion long-form + Shorts
make draft   EP=ep01      # upload private draft to YouTube
make episode EP=ep01      # all of the above
```

## Conventions

- All pipeline work on `fable/*` branches; merge to `main` only after Peter's review.
- Secrets live **outside** the repo tree (env / secret store); `.githooks/pre-push` runs gitleaks. Never commit keys or media.
- Nothing publishes to public automatically — the publish step is a human (Peter) action.

## Open decisions (see ROLES §8)

Render capacity (keep CPX32 + ephemeral vs upsize) · repo home on GitHub · Telegram approval UX · model pinning (accuracy/IP on Claude) · escalation path.
