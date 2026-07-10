# Risk Decoded — Build & Execution Plan v1.0

**Status:** Draft for Peter's approval · 2026-07-10
**Companion to:** REQUIREMENTS.md v1.0
**Goal:** Ship a repeatable, near-zero-marginal-cost pipeline that turns a script into a published-ready Qubit cartoon (long-form + Shorts), running on Hetzner.
**Guiding principle:** Validate the format by hand first, automate second. Never automate a format you haven't proven.

---

## 1. Architecture

```
  ┌────────────┐   script.md (+ config.yaml)
  │  AUTHOR    │───────────────┐
  └────────────┘               ▼
                     ┌────────────────────┐
                     │  ORCHESTRATOR      │  Claude Code
                     │  (build script)    │
                     └─────────┬──────────┘
        ┌──────────────┬───────┼────────────┬───────────────┐
        ▼              ▼       ▼            ▼               ▼
  [QA/accuracy]  [ElevenLabs] [Nano Banana] [Remotion]   [ (opt) Higgsfield ]
   fact-check     voice+timing  stills/thumb  Qubit+comp     hero clip (rare)
        │              │          │            │               │
        └──────────────┴──────────┴─────┬──────┴───────────────┘
                                        ▼
                                  ┌───────────┐
                                  │  ffmpeg   │  render long-form + cut Shorts
                                  └─────┬─────┘
                                        ▼
                                 ┌──────────────┐
                                 │ YouTube API  │  DRAFT/private + disclosure
                                 └──────┬───────┘
                                        ▼
                                  AUTHOR review → manual publish
```
All compute on Hetzner. Only ElevenLabs, Gemini, YouTube (+optional Higgsfield) are contacted externally.

---

## 2. Repo structure

```
risk-decoded/
├─ README.md
├─ REQUIREMENTS.md
├─ BUILD-EXECUTION-PLAN.md
├─ Makefile                      # make episode EP=ep01
├─ config/
│  ├─ channel.yaml               # palette, fonts, defaults
│  ├─ lexicon.en.yaml            # jargon pronunciation
│  └─ episodes/ep01.yaml …       # per-episode config
├─ scripts/                      # source scripts (Markdown)
│  ├─ ep01-quantum-explained.md
│  ├─ ep02-quantum-threat.md
│  └─ ep03-quantum-insurance.md
├─ src/
│  ├─ orchestrator/              # stage runners, caching, cost caps, provenance
│  ├─ providers/                 # elevenlabs.ts, image.ts (nano_banana), motion.ts, youtube.ts  (swappable)
│  └─ remotion/
│     ├─ Qubit/                  # SVG rig, poses, expressions, demos
│     ├─ components/             # lower-third, myth-vs-reality, panel, timeline, captions, intro/outro
│     └─ compositions/           # LongForm.tsx, Short.tsx
├─ assets/
│  ├─ style/                     # style refs, thumbnail templates
│  └─ generated/                 # cached stills (git-ignored)
├─ build/                        # per-episode artefacts (git-ignored)
└─ .githooks/pre-push            # gitleaks
```
**Workflow:** all pipeline work on `fable/*` branches; merge to `main` only after Peter's review. Secrets in env/secret store **outside** the tree; `pre-push` runs gitleaks. (Mirrors your existing hardening.)

---

## 3. Accounts & prerequisites (one-time)

| Need | For | Notes / cost |
|---|---|---|
| Google **Gemini API key** (AI Studio) | Nano Banana stills/thumbnails in automation | Pennies/image; small free daily tier. Your Gemini **Pro sub** covers manual design (~100/day) but is *not* API |
| **ElevenLabs** account + voice_id | Narration | Creator ~$22/mo covers volume |
| **YouTube** channel + Data API OAuth | Draft upload | Free |
| **Node.js + Remotion** on Hetzner | Render | Free (Remotion free for individuals) |
| **ffmpeg** on Hetzner | Encode/cut | Free |
| (Optional) **Higgsfield** key | Rare hero clips | Skip for v1 |
| GitHub repo `risk-decoded` + gitleaks | Source + secret hygiene | Free |

---

## 4. Phased delivery

### Phase 0 — Decide & set up  *(exit: green-lit + repo skeleton)*
- Confirm §I open decisions (name, voice, repo, host, cadence).
- Create repo, branch workflow, secret store, gitleaks hook.
- **Deliverable:** empty scaffolded repo + accounts/keys in place.

### Phase 1 — Design Qubit + prove the format  *(exit: one great pilot, mostly by hand)*
- Nano Banana concept pass → pick Qubit look → rebuild as **SVG rig** with base poses/expressions + the 3 physics demos (FR-A1/A2).
- Lock ElevenLabs voice_id; build the `lexicon`.
- Hand-assemble **Episode 1** in Remotion to lock the template + component set (FR-R1/R2).
- **Deliverable:** finished Episode 1 long-form + 1 Short, rendered on Hetzner. This is the quality bar.
- *Why first:* if the look/voice/pacing aren't right by hand, automation just scales the wrong thing.

### Phase 2 — Templatise  *(exit: episodes are data, not code)*
- Extract the Ep1 template to `risk-decoded-v1`; parameterise components from `scenes.json`.
- Build the scene schema + validator (FR-C2), caption sync from word timings (FR-V2/R1).
- **Deliverable:** re-render Ep1 purely from `config + scenes.json`.

### Phase 3 — Orchestrate  *(exit: one-command build)*
- Stage runners with caching + resumability (FR-O1/O2), cost caps (FR-O3), provenance manifest (FR-O4).
- Provider modules behind interfaces (NFR-10): ElevenLabs, Nano Banana, (opt) Higgsfield.
- Accuracy/IP QA gate (FR-Q1–Q4).
- **Deliverable:** `make episode EP=ep02` builds Episode 2 end-to-end to render.

### Phase 4 — Shorts + publish  *(exit: draft-on-YouTube)*
- Auto Shorts derivation + vertical safe-area reframe (FR-S1/S2).
- YouTube draft upload with metadata, thumbnail, AI disclosure (FR-P1–P3).
- Pre-publish review packet (FR-Q4).
- **Deliverable:** Episode 2 + its Shorts as private drafts in YouTube Studio, with review packet.

### Phase 5 — Harden & scale  *(exit: weekly cadence sustainable)*
- Run report/observability (NFR-9), performance tuning (NFR-6), docs/runbook.
- Produce Episode 3 as a pure pipeline run (regression proof).
- **Deliverable:** 3 episodes live-ready; a runbook; a repeatable weekly loop.

---

## 5. Milestones

| M | Milestone | Gate |
|---|---|---|
| M1 | Repo + accounts ready | Phase 0 done |
| M2 | Qubit approved + Episode 1 pilot rendered | Phase 1 done — **the go/no-go quality gate** |
| M3 | Ep1 rebuildable from config | Phase 2 done |
| M4 | One-command Ep2 build | Phase 3 done |
| M5 | Ep2 draft on YouTube + Shorts | Phase 4 done |
| M6 | Ep3 via pipeline + runbook | Phase 5 done — v1 complete |

*(Effort is deliberately expressed as sequenced gates, not calendar dates — you set the pace. Realistically M2 is the bulk of the human effort; M3–M6 are largely engineering that Claude Code can drive.)*

---

## 6. Task backlog (maps to phases)

**P0:** repo skeleton · branch/hook setup · secret store · accounts + keys · confirm open decisions.
**P1:** Nano Banana concept prompts · pick look · SVG Qubit rig · pose/expression set · 3 physics demos · lock voice · lexicon · hand-build Ep1 template · render Ep1.
**P2:** extract template · scene schema + validator · caption sync · re-render Ep1 from data.
**P3:** stage runners + cache · cost caps · provenance manifest · provider interfaces · QA/accuracy gate · IP scan.
**P4:** Shorts cutter · vertical reframe · YouTube uploader · disclosure flag · thumbnail export · review packet.
**P5:** run report · perf tune · runbook/docs · Ep3 pipeline run · regression check.

---

## 7. Risk register

| # | Risk | L | I | Mitigation |
|---|---|---|---|---|
| R1 | Qubit look/voice underwhelms → whole channel feels generic | M | H | **Phase 1 by hand** and gate at M2 before any automation spend |
| R2 | Over-engineering the pipeline before proving content | M | H | Strict phase gates; no Phase 3 until M2 passes |
| R3 | Generative-image inconsistency creeps into the host | L | M | Host is **code/SVG**, not generated — consistency by construction |
| R4 | API cost creep (stills, TTS, credits) | L | M | Cost caps (FR-O3) + run report; favour Remotion diagrams; use Gemini Pro sub for manual stills |
| R5 | Secret leak (repeat of prior key exposure) | M | H | Keys outside tree · gitleaks pre-push · rotate-without-code · run pipeline once end-to-end after any rotation |
| R6 | Factual error damages professional credibility | M | H | Accuracy gate (FR-Q1) blocks build; sources logged; your expert review at M-gates |
| R7 | YouTube demonetises "AI mass-content" | M | M | Genuine expertise + accuracy + consistent host + AI disclosure; not faceless slop |
| R8 | Vendor lock-in / model deprecation | M | L | Provider interface (NFR-10); swap image/voice/motion behind one module |
| R9 | Consumer Gemini sub mistaken for API in automation | M | L | Documented: sub = manual only; automation uses Gemini API key |
| R10 | IP/compliance slip (logo, employer, named person) | L | H | IP scan (FR-Q3) blocks publish; original assets only |

---

## 8. Cost model

**One-time / setup:** €0 cash beyond time (Remotion free, repo free, Hetzner already yours). Qubit design uses your Gemini Pro sub (free capacity).

**Per standard episode (long-form + 3 Shorts):**
| Item | Cost |
|---|---|
| ElevenLabs voice (~7 min + regens) | fraction of ~$22/mo sub |
| Nano Banana stills/thumbnail (automation, ~5–10 imgs) | ~$0.20–1.30 (API) or free via Pro sub if done manually |
| Qubit + composition + render (Remotion/Hetzner) | €0 |
| Optional Higgsfield hero clip | €0 (skipped v1) |
| **Marginal total** | **≈ €1–10 / episode** |

**Monthly (weekly cadence, ~4 episodes):** ≈ **ElevenLabs $22 + a few $ of image API ≈ $25–35/mo all-in.** The three quantum episodes together: **well under $25.**

---

## 9. Success metrics (v1)

- **Production:** an episode goes script→draft in one command, unattended, within the render budget (NFR-6).
- **Cost:** marginal cost/episode within NFR-2.
- **Consistency:** Qubit identical across all 3 episodes (visual hash / eyeball).
- **Quality gate:** each episode passes the accuracy + IP + accessibility checks before draft.
- **Cadence:** a sustainable weekly loop demonstrated by Ep3 being a pure pipeline run.

---

## 10. First-week concrete actions

1. Approve §I open decisions (name, voice direction, repo, host, cadence).
2. I generate the **Nano Banana concept-prompt set for Qubit** + a first **SVG Qubit** you can see move.
3. Lock the **ElevenLabs voice** (I'll shortlist 2–3 voices to audition).
4. Stand up the **repo skeleton** (branches, gitleaks, config, folders) and drop the 3 existing scripts in.
5. Hand-build the **Episode 1 pilot** to lock the template — the M2 quality gate.

Everything after M2 is largely engineering I can drive with Claude Code from the config + templates.
