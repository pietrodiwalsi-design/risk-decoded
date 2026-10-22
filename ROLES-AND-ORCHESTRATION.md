# Risk Decoded — Roles & Orchestration (Moshe / OpenClaw)

**Status:** Draft for Peter's approval · 2026-10-02 · **rev 3** (Sonnet as coding agent inside OpenClaw; Gemini as trigger-only orchestrator; YouTube token excluded from OpenClaw; accuracy gate independent of the build stack)
**Previous:** rev 2 · 2026-07-10 (Moshe = agent, not human; Hetzner topology)
**Companion to:** REQUIREMENTS.md v1.1 · BUILD-EXECUTION-PLAN.md v1.1
**Purpose:** Decide *which executor runs each stage* — routing every task to the cheapest capable executor, keeping high-stakes reasoning on strong models, and keeping the one human (Peter) on the gates.

**Changes in rev 3 (all marked "rev 3" below):**
1. Moshe's stack is now Gemini (orchestrator) + Anthropic Sonnet (coding agent) + Grok (fallback) + Ollama (local).
2. Gemini only *triggers* deterministic pipeline stages; it does not perform them.
3. Pipeline engineering (Phases 2–4) moves to Sonnet inside OpenClaw on `moshe/*` branches; Claude outside OpenClaw reviews.
4. The accuracy + IP gate runs outside the OpenClaw run, so the stack that builds an episode never signs it off.
5. The YouTube credential is kept out of OpenClaw. Telegram is notification-only, not a publish path.
6. Phase 1 (M2 pilot) is done by hand on Peter's Mac before any automation is built.

---

## 0. Who "Moshe" is

**Moshe is the OpenClaw agent runtime on Hetzner** (`ubuntu-4gb-nbg1-1` — **8 GB RAM** despite the hostname, Nürnberg) — not a person. It has its own identity (Gmail `moshe.van.walsem`, Telegram, Drive, Calendar) and its own model stack (rev 3): **Gemini (orchestrator, 1M ctx), Anthropic Sonnet (coding agent), xAI Grok (fallback), Ollama (local)**. ElevenLabs and Nano Banana (Gemini image) links and API keys are already created. "Fable" = the Claude-based agent working outside OpenClaw. **Peter is the only human.**

---

## 1. Principle

Route by *cost-of-being-wrong*, on infrastructure you already run:

1. **Cheapest capable model does the grind** → **Moshe/OpenClaw** on Gemini/Grok/Ollama.
2. **Coding agent builds the pipeline** → **Sonnet inside OpenClaw**, on `moshe/*` branches, with a token budget per task (rev 3).
3. **Independent strong model holds the high-stakes gates** → **Claude (Fable), outside OpenClaw**: accuracy gate, IP gate, Qubit design, code review.
4. **The human holds the gates** → **Peter** approves at each milestone and publishes manually.

Control rules:
- A cheap model may *draft* a title or a scene split; it may **not** be the accuracy or IP gate.
- (rev 3) The stack that builds an episode may not sign it off. The accuracy + IP gate runs outside the OpenClaw run.
- (rev 3) Deterministic steps (voice call, caption sync, render, cut) are plain code. The orchestrator model only triggers them (`make episode EP=…`) and reads the result.

---

## 2. Executors

| Executor | Is | Runs on | Best at |
|---|---|---|---|
| **Moshe / Gemini** | Orchestrator model inside OpenClaw (Grok fallback · Ollama local) | Hetzner `ubuntu-4gb-nbg1-1`, behind Tailscale + Hetzner firewall | Triggering pipeline runs, scene-decomposition drafts, Nano Banana stills, Shorts and metadata drafts, notifications |
| **Moshe / Sonnet** (rev 3) | Coding agent inside OpenClaw | Same box, Anthropic API | Pipeline engineering: stage runners, provider modules, Remotion components, on `moshe/*` branches |
| **Claude (Fable)** | Independent strong model, outside OpenClaw | Cowork / Claude Code on Peter's Mac | Accuracy fact-check gate, IP gate, Qubit design, review of Moshe's pull requests, hard debugging |
| **Peter** | The human | Mac, via Tailscale / Telegram | Creative + accuracy sign-off; merges to `main`; the upload and publish actions |
| **Pipeline code** | Deterministic scripts | Hetzner (+ ephemeral render worker) | ElevenLabs calls, caption sync, Remotion render, ffmpeg cut |

---

## 3. Stage → executor routing (RACI)

R = Runs · A = Approves · C = Consulted · I = Informed

| Pipeline stage | Moshe / Gemini | Moshe / Sonnet | Claude (outside) | Peter | Code |
|---|:--:|:--:|:--:|:--:|:--:|
| Topic/script authoring | C | – | R (draft) | **A/R** | – |
| **Accuracy fact-check gate (FR-Q1)** | – | – | **R** | **A** | – |
| **IP hygiene gate (FR-Q3)** | – | – | **R** | **A** | – |
| Scene decomposition → scenes.json | **R** (draft, once) | – | C | A (commit) | validate |
| Nano Banana prompts + stills | **R** | – | C | I | – |
| Voice synthesis (ElevenLabs) | trigger | – | – | I | **R** |
| Caption/timing sync | – | – | – | I | **R** |
| Qubit design (concept → SVG rig) | assist | assist | **R** | **A** | – |
| Episode 1 pilot (M2, by hand) | – | – | **R** | **A/R** | – |
| Remotion composition/render | trigger | – | C | I | **R** (ephemeral worker) |
| Shorts selection + cut | **R** (draft) | – | C | A | R (cut) |
| Metadata (title/desc/tags) | **R** (variants) | – | C | **A** | – |
| Thumbnail generation | **R** (Nano Banana) | – | – | A | – |
| YouTube **draft** upload (rev 3) | notify only | – | – | **R** | optional script outside OpenClaw |
| **Publish to public** (rev 3) | – | – | – | **A/R** (manual, YouTube Studio) | – |
| Per-episode run + monitoring | **R** | – | – | I | R |
| Pipeline build (Phases 2–4) (rev 3) | trigger | **R** (impl) | C (review) | **A** (merge) | – |

**Shape of it:** Peter and Claude prove the format by hand up to M2. From M3, Sonnet inside OpenClaw builds the pipeline and Gemini runs it day to day. Claude outside OpenClaw holds the accuracy and IP gates and reviews Moshe's code. Peter merges, uploads and publishes.

**scenes.json (rev 3):** generated once by the model, reviewed, then committed. Rebuilds read the committed file, which is how FR-C3 (deterministic regeneration) is met; an LLM call is not repeatable byte for byte.

---

## 4. Architecture fit — mapping onto your Hetzner box

Reuse what Moshe already has; add only what's missing.

| Pipeline need | Reuse | Add |
|---|---|---|
| Orchestrator / grind LLM | Gemini (primary) · Grok (fallback) · Ollama (local trivial) | — |
| Coding agent (rev 3) | Anthropic Sonnet (already in use in OpenClaw) | Token budget per task |
| Image stills / thumbnails | Gemini = Nano Banana (link + key created) | Provider-side spend cap |
| Voice (rev 3) | ElevenLabs (link + key created) | Provider-side spend cap; locked `voice_id` |
| Accuracy / IP gate | Claude outside OpenClaw (Cowork / Claude Code) | — |
| Script + asset storage | Google Drive (Docs/Sheets) | `risk-decoded` asset conventions |
| Source repo | GitHub | `risk-decoded` repo + gitleaks on push (done) |
| Notifications | Telegram (bot + channel) | "Upload package ready for review" message; no publish command |
| Video render | — | Remotion + ffmpeg + ephemeral render worker (see §5) |
| YouTube upload (rev 3) | — | **Not on the box.** Manual, or a script on Peter's Mac |

**Access & security:** everything reachable only via **Tailscale** (`100.113.189.75`); Hetzner firewall stays **deny-public-default**; Peter's Mac has no direct public path to OpenClaw. Secrets stay in the box's store **outside** `/root/.openclaw/workspace`; the **daily 02:00 UTC backup → GitHub** must keep the gitleaks pre-push guard.

**Credential scope (rev 3):**

| Credential | In OpenClaw? | Control |
|---|---|---|
| ElevenLabs key | Yes | Project-specific key, provider-side spend cap, outside workspace tree |
| Gemini image key | Yes | Project-specific key, provider-side spend cap, outside workspace tree |
| Anthropic key (Sonnet) | Yes | Budget cap per task |
| GitHub | Yes | `moshe/*` branches only; `main` protected |
| **YouTube OAuth token** | **No** | The one credential that can publish; held by Peter only |

Reason: an upload token can also set a video public, so if Moshe holds it, "nothing publishes automatically" is a convention and not a control. OpenClaw's 2026 security record (several hundred tracked CVEs, malicious skills on ClawHub) makes that the credential to keep away from it. Also: no unverified ClawHub skills on this box, and keep OpenClaw patched.

---

## 5. Capacity (real Hetzner pricing — recommend: **keep CPX32, render ephemerally**)

Current box is **CPX32** — 4 vCPU / **8 GB** / 80 GB / **€42.94/mo** (the `…-4gb-…` hostname is legacy). Rescale options in this project are AMD **CPX** only, and post-June-2026 pricing makes an always-on upsize expensive:

| Plan | vCPU | RAM | Disk | €/mo | €/h |
|---|--:|--:|--:|--:|--:|
| **CPX32 (current)** | 4 | 8 GB | 80 GB | **42.94** | 0.069 |
| CPX42 | 8 | 16 GB | 80 GB | 84.08 | 0.135 |
| CPX52 | 12 | 24 GB | 80 GB | 121.59 | 0.195 |

**Upsizing 8→16 GB permanently costs +€41/mo (~doubles the box)** — for capacity a render uses only minutes/week. Not worth it.

**Recommended instead:**
1. **Keep CPX32** as the always-on Moshe box.
2. **Render on Peter's Mac during Phase 1** (powerful, €0, not unattended).
3. **For production renders, spin an ephemeral CPX42/CPX52 per episode, then destroy it.** At €0.135–0.195/h a 20–40 min render ≈ **€0.05–0.13/episode → ~€1/mo even at weekly+ cadence**, vs +€41/mo to upsize — and it never reboots Moshe (a rescale would).
4. **Disk:** the 80 GB tier disk is fixed; when the asset/build library outgrows it, attach a **Hetzner Volume** rather than jumping to a bigger plan.
5. If rendering on the CPX32 itself: single render, low Chromium concurrency, off-peak; unload large Ollama models during a render.

**Regardless:** cap to **one render at a time** and off-peak, to protect Moshe's live services.

Ollama note: on 8 GB, small models only. If you later want *bigger local models routinely*, that — not rendering — is the real case for more RAM; weigh it separately from this pipeline.

---

## 6. Governance & control points

1. **Instructions originate from Peter.** Anything arriving via another path or self-labelled "approved" → stop, verify with Peter — applies to Moshe-generated mandates too.
2. **Branch discipline:** Claude/Fable work on `fable/*`, Moshe on `moshe/*`; `main` only after Peter's review.
3. **Secret hygiene everywhere:** keys outside the workspace tree · gitleaks on the daily GitHub push · rotate-without-code · run each dependent pipeline once end-to-end after any rotation.
4. **Model-appropriate routing is a control, not just cost:** accuracy + IP gates pinned to Claude outside OpenClaw; Gemini/Grok produce drafts only.
5. **Provenance:** each artefact records `executor: moshe-gemini|moshe-sonnet|claude|code` + model + version (extends FR-O4).
6. **(rev 3) Separation of build and sign-off:** code written by Sonnet in OpenClaw is reviewed by Claude outside OpenClaw before Peter merges; episodes built by Moshe pass the external accuracy + IP gate.
7. **(rev 3) Publish credential stays with Peter.** No YouTube token on the Hetzner box. Telegram carries notifications only.
8. **(rev 3) Spend caps at the provider** for ElevenLabs, Gemini image and Anthropic, in addition to the pipeline's own caps (FR-O3).
9. **(rev 3) Format before automation:** no Phase 2–4 engineering by Moshe until the M2 pilot is approved.

---

## 7. Cost impact

- Orchestration + grind + images run on **models Moshe already pays for** → per-episode LLM/image cost ≈ negligible.
- **Paid line items:** ElevenLabs voice + an ephemeral render server (~€0.05–0.13/episode, ≈€1/mo) + an optional Hetzner Volume. Base box stays **CPX32 (€42.94/mo, already running for Moshe)**.
- **(rev 3) Sonnet coding agent:** a one-off build cost during Phases 2–4, not a per-episode cost. Coding-agent loops use far more tokens than chat, so set a budget per task and review spend at each milestone.
- **Claude outside OpenClaw** stays low-volume/high-value (design + gates + review).
- Marginal cost/episode remains within REQUIREMENTS NFR-2.

---

## 8. Open decisions (confirm)

1. **Render capacity** — keep **CPX32 + ephemeral render server** (recommended), or commit to an always-on 16 GB CPX42 (+€41/mo)?
2. **Repo home** — resolved: `pietrodiwalsi-design/risk-decoded`, `fable/*` + `moshe/*` workflow.
3. **Draft upload (rev 3)** — Peter uploads by hand in YouTube Studio (about two minutes a week), or a small upload script on Peter's Mac that hard-codes `private`? Either way the token stays off the Hetzner box. Replaces the earlier Telegram-approve design.
4. **Model pinning** — confirm accuracy + IP gates stay on Claude outside OpenClaw, never Gemini/Grok/Sonnet-in-OpenClaw.
5. **Escalation** — when Moshe's output fails schema validation twice → hand to Sonnet, or halt and Telegram Peter?
6. **(rev 3) Key location** — confirm the ElevenLabs and Gemini image keys sit outside `/root/.openclaw/workspace`, are project-specific, and have provider-side spend caps.
7. **(rev 3) Channel goal** — monetisation or professional credibility? This sets how much weight YouTube's inauthentic-content policy (BUILD-EXECUTION-PLAN R7) gets and how much "unattended" automation is worth building.

---

## 9. Consistency status (2026-10-02)

Aligned with this revision: REQUIREMENTS v1.1, BUILD-EXECUTION-PLAN v1.1, CHANNEL-BIBLE (§4–6).

Not yet aligned:
- The copies of these docs in the GitHub repo (`pietrodiwalsi-design/risk-decoded`).
- The Claude Project instructions (role description and pipeline line).
- MOSHE-HANDOFF.md §4 still points at "five open decisions"; §8 now lists seven.
