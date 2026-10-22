# Risk Decoded — Build & Execution Plan v1.1

**Status:** Draft for Peter's approval · 2026-10-02 · **v1.1** (aligned with ROLES-AND-ORCHESTRATION rev 3 and REQUIREMENTS v1.1; changes marked "v1.1")
**Previous:** v1.0 · 2026-07-10
**Companion to:** REQUIREMENTS.md v1.1
**Goal:** Ship a repeatable, near-zero-marginal-cost pipeline that turns a script into a published-ready Qubit cartoon (long-form + Shorts), running on Hetzner.
**Guiding principle:** Validate the format by hand first, automate second. Never automate a format you haven't proven.

**Changes in v1.1:**
1. Phase 0 is done; Phase 1 runs by hand on Peter's Mac (§4).
2. Phases 2–4 are built by Sonnet inside OpenClaw on `moshe/*` branches, reviewed by Claude outside OpenClaw (§4).
3. The pipeline ends at an upload package; the YouTube upload is Peter's action and the token stays off the Hetzner box (§1, §4).
4. R7 raised to M/H; R11 (OpenClaw compromise) and R12 (coding-agent spend) added (§7).
5. Cost model includes the one-off Sonnet build cost (§8).

---

## 1. Architecture (v1.1)

```
  ┌────────────┐   script.md (+ config.yaml)
  │  AUTHOR    │───────────────┐
  └────────────┘               ▼
                     ┌────────────────────┐
                     │  ACCURACY + IP     │  Claude, outside OpenClaw
                     │  GATE              │
                     └─────────┬──────────┘
                               ▼
                     ┌────────────────────┐
                     │  ORCHESTRATOR      │  until M2: by hand on the Mac
                     │  (make episode)    │  from M3: Moshe/Gemini triggers
                     └─────────┬──────────┘
        ┌──────────────┬───────┴────┬───────────────┐
        ▼              ▼            ▼               ▼
  [ElevenLabs]   [Nano Banana]  [Remotion]   [ (opt) Higgsfield ]
  voice+timing   stills/thumb   Qubit+comp     hero clip (rare)
        │              │            │               │
        └──────────────┴─────┬──────┴───────────────┘
                             ▼
                       ┌───────────┐
                       │  ffmpeg   │  render long-form + cut Shorts
                       └─────┬─────┘
                             ▼
                    ┌─────────────────┐
                    │ UPLOAD PACKAGE  │  video + metadata + thumbnail + review packet
                    └────────┬────────┘
                             ▼   (leaves the Hetzner box here)
              AUTHOR: upload as private → review → manual publish
```
Compute on Hetzner from M3 (Mac in Phase 1). The Hetzner box contacts only ElevenLabs, Gemini and Anthropic (+ optional Higgsfield). YouTube is reached from Peter's side only.

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
├─ scenes/                       # v1.1 — committed scenes.json per episode
├─ src/
│  ├─ orchestrator/              # stage runners, caching, cost caps, provenance
│  ├─ providers/                 # elevenlabs.ts, image.ts (nano_banana), motion.ts  (swappable)
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
**Workflow:** Claude/Fable work on `fable/*`, Moshe on `moshe/*`; merge to `main` only after Peter's review. Secrets in env/secret store **outside** the tree; `pre-push` runs gitleaks. An optional YouTube upload script, if chosen (ROLES §8.3), lives on Peter's Mac and not in the pipeline's provider set.

---

## 3. Accounts & prerequisites (one-time)

| Need | For | Status / notes |
|---|---|---|
| Google **Gemini API key** (AI Studio) | Nano Banana stills/thumbnails in automation | **Created** (v1.1). Set a spend cap. Your Gemini **Pro sub** covers manual design but is *not* API |
| **ElevenLabs** account + key | Narration | **Created** (v1.1). Creator ~$22/mo covers volume. Set a spend cap. `voice_id` still to lock |
| **YouTube** channel | Draft upload + publish | Free. OAuth only needed if the Mac-side upload script is chosen (ROLES §8.3) |
| **Node.js + Remotion** | Render | Free for a solo user. Mac in Phase 1; Hetzner from M3 |
| **ffmpeg** | Encode/cut | Free |
| (Optional) **Higgsfield** key | Rare hero clips | Skip for v1 |
| GitHub repo `risk-decoded` + gitleaks | Source + secret hygiene | **Done** |

---

## 4. Phased delivery

### Phase 0 — Decide & set up  *(done, v1.1)*
- Repo, branch workflow and gitleaks hook are in place; scaffold is on `main`.
- **Still open:** the decisions in ROLES §8 and REQUIREMENTS §I.

### Phase 1 — Design Qubit + prove the format  *(exit: one great pilot, by hand on the Mac)*
- Nano Banana concept pass → pick Qubit look → rebuild as **SVG rig** with base poses/expressions + the 3 physics demos (FR-A1/A2).
- Lock ElevenLabs voice_id; build the `lexicon`.
- Hand-assemble **Episode 1** in Remotion to lock the template + component set (FR-R1/R2).
- **Who (v1.1):** Peter + Claude, on Peter's Mac. Moshe does not build pipeline code in this phase.
- **Deliverable:** finished Episode 1 long-form + 1 Short. This is the quality bar.
- *Why first:* if the look/voice/pacing aren't right by hand, automation just scales the wrong thing.

### Phase 2 — Templatise  *(exit: episodes are data, not code)*
- Extract the Ep1 template to `risk-decoded-v1`; parameterise components from `scenes.json`.
- Build the scene schema + validator (FR-C2), caption sync from word timings (FR-V2/R1).
- **Who (v1.1):** Sonnet inside OpenClaw on `moshe/*`, with a token budget per task; Claude outside OpenClaw reviews; Peter merges.
- **Deliverable:** re-render Ep1 purely from `config + committed scenes.json`.

### Phase 3 — Orchestrate  *(exit: one-command build)*
- Stage runners with caching + resumability (FR-O1/O2), cost caps (FR-O3), provenance manifest (FR-O4).
- Provider modules behind interfaces (NFR-10): ElevenLabs, Nano Banana, (opt) Higgsfield.
- Hook for the external accuracy/IP gate (FR-Q1–Q4): the build refuses to run without a recorded pass.
- **Who (v1.1):** as Phase 2.
- **Deliverable:** `make episode EP=ep02` builds Episode 2 end-to-end to render.

### Phase 4 — Shorts + upload package  *(exit: draft-on-YouTube by Peter's action)*
- Auto Shorts derivation + vertical safe-area reframe (FR-S1/S2).
- Upload package per asset: video, metadata, thumbnail (FR-P1). Pre-publish review packet (FR-Q4).
- Peter uploads as private with AI disclosure set (FR-P2/P3), by hand or via the Mac-side script.
- **Deliverable:** Episode 2 + its Shorts as private drafts in YouTube Studio, with review packet.

### Phase 5 — Harden & scale  *(exit: weekly cadence sustainable)*
- Run report/observability (NFR-9), performance tuning (NFR-6), docs/runbook.
- Produce Episode 3 as a pure pipeline run (regression proof).
- **Deliverable:** 3 episodes live-ready; a runbook; a repeatable weekly loop.

---

## 5. Milestones

| M | Milestone | Gate |
|---|---|---|
| M1 | Repo + accounts ready | Phase 0 done — **reached** |
| M2 | Qubit approved + Episode 1 pilot rendered | Phase 1 done — **the go/no-go quality gate** |
| M3 | Ep1 rebuildable from config | Phase 2 done |
| M4 | One-command Ep2 build | Phase 3 done |
| M5 | Ep2 draft on YouTube + Shorts | Phase 4 done |
| M6 | Ep3 via pipeline + runbook | Phase 5 done — v1 complete |

*(Effort is expressed as sequenced gates, not calendar dates — you set the pace. M2 is the bulk of the human effort; M3–M6 are largely engineering Moshe/Sonnet can drive under review.)*

---

## 6. Task backlog (maps to phases)

**P0 (done):** repo skeleton · branch/hook setup · accounts + keys. **Open:** confirm decisions · confirm key location and spend caps.
**P1:** Nano Banana concept prompts · pick look · SVG Qubit rig · pose/expression set · 3 physics demos · lock voice · lexicon · hand-build Ep1 template · render Ep1.
**P2:** extract template · scene schema + validator · caption sync · re-render Ep1 from data.
**P3:** stage runners + cache · cost caps · provenance manifest · provider interfaces · gate hook.
**P4:** Shorts cutter · vertical reframe · upload package · thumbnail export · review packet · (optional) Mac-side upload script.
**P5:** run report · perf tune · runbook/docs · Ep3 pipeline run · regression check.

---

## 7. Risk register

| # | Risk | L | I | Mitigation |
|---|---|---|---|---|
| R1 | Qubit look/voice underwhelms → whole channel feels generic | M | H | **Phase 1 by hand** and gate at M2 before any automation spend |
| R2 | Over-engineering the pipeline before proving content | **H** (v1.1) | H | Strict phase gates; no Phase 2–4 work by Moshe until M2 passes. Three months at Phase 0 show this risk is live |
| R3 | Generative-image inconsistency creeps into the host | L | M | Host is **code/SVG**, not generated — consistency by construction |
| R4 | API cost creep (stills, TTS, credits) | L | M | Pipeline cost caps (FR-O3) + provider-side spend caps + run report |
| R5 | Secret leak (repeat of prior key exposure) | M | H | Keys outside tree and outside the OpenClaw workspace · gitleaks pre-push · rotate-without-code |
| R6 | Factual error damages professional credibility | M | H | Accuracy gate (FR-Q1) run outside OpenClaw blocks build; sources logged; Peter's review at M-gates |
| R7 | YouTube treats the channel as "inauthentic content" (templated, synthetic voice, automated) and demonetises or removes it | M | **H** (v1.1) | Peter-authored scripts · recorded human review per episode · visual variation between episodes · AI disclosure · no "unattended publish" (NFR-8). Impact drops if the goal is credibility, not monetisation (ROLES §8.7) |
| R8 | Vendor lock-in / model deprecation | M | L | Provider interface (NFR-10); swap image/voice/motion behind one module |
| R9 | Consumer Gemini sub mistaken for API in automation | M | L | Documented: sub = manual only; automation uses Gemini API key |
| R10 | IP/compliance slip (logo, employer, named person) | L | H | IP scan (FR-Q3) blocks publish; original assets only |
| R11 (v1.1) | OpenClaw compromise (vulnerability or malicious skill) abuses credentials held on the box | M | H | No YouTube token on the box · project-specific keys with spend caps · no unverified skills · keep OpenClaw patched · `main` protected |
| R12 (v1.1) | Coding-agent token spend runs away during Phases 2–4 | M | M | Token budget per task · spend review at each milestone |

---

## 8. Cost model

**One-time / setup:** Remotion free, repo free, Hetzner already yours. Qubit design uses your Gemini Pro sub. **(v1.1)** Sonnet coding-agent tokens for Phases 2–4 are a one-off build cost; set a budget per task and measure it, since no estimate exists yet.

**Per standard episode (long-form + 3 Shorts):**
| Item | Cost |
|---|---|
| ElevenLabs voice (~7 min + regens) | fraction of ~$22/mo sub |
| Nano Banana stills/thumbnail (automation, ~5–10 imgs) | ~$0.30–1.00 (API) or free via Pro sub if done manually |
| Qubit + composition + render (Remotion; ephemeral Hetzner worker) | ~€0.05–0.13 |
| Optional Higgsfield hero clip | €0 (skipped v1) |
| **Marginal total** | **≈ €1–10 / episode** |

**Monthly (weekly cadence, ~4 episodes):** ≈ **ElevenLabs $22 + a few $ of image API ≈ $25–35/mo**, on top of the Hetzner box that already runs for Moshe.

---

## 9. Success metrics (v1)

- **Production:** an episode goes script→upload package in one command, unattended, within the render budget (NFR-6).
- **Cost:** marginal cost/episode within NFR-2.
- **Consistency:** Qubit identical across all 3 episodes (visual hash / eyeball).
- **Quality gate:** each episode passes the external accuracy + IP + accessibility checks before upload.
- **Cadence:** a sustainable weekly loop demonstrated by Ep3 being a pure pipeline run.

---

## 10. Next concrete actions (v1.1)

1. Confirm the open decisions (ROLES §8, REQUIREMENTS §I): name, voice direction, cadence, upload method, channel goal.
2. Confirm the ElevenLabs and Gemini keys sit outside the OpenClaw workspace, are project-specific, and have spend caps.
3. Nano Banana concept pass for Qubit → pick a look → first **SVG Qubit** that moves.
4. Lock the **ElevenLabs voice** (shortlist 2–3 voices to audition).
5. Hand-build the **Episode 1 pilot** on the Mac — the M2 quality gate.

Everything after M2 is engineering Moshe/Sonnet can drive from the config + templates, under Claude's review and Peter's merge.
