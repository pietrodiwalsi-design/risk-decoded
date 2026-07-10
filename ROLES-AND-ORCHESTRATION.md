# Risk Decoded — Roles & Orchestration (Moshe / OpenClaw)

**Status:** Draft for Peter's approval · 2026-07-10 · **rev 2** (corrects Moshe = agent, not human; maps to Hetzner topology)
**Companion to:** REQUIREMENTS.md · BUILD-EXECUTION-PLAN.md
**Purpose:** Decide *which executor runs each stage* — routing every task to the cheapest capable executor, keeping high-stakes reasoning on strong models, and keeping the one human (Peter) on the gates.

---

## 0. Correction — who "Moshe" is

**Moshe is the OpenClaw agent runtime on Hetzner** (`ubuntu-4gb-nbg1-1` — **8 GB RAM** despite the hostname, Nürnberg) — not a person. It has its own identity (Gmail `moshe.van.walsem`, Telegram, Drive, Calendar) and its own model stack: **Gemini (primary, 1M ctx), xAI Grok (fallback), Anthropic Claude (heavy reasoning), Ollama (local)**. "Fable" = the Claude-based agent. **Peter is the only human.** All earlier references to "Moshe (human)" are re-cast below as the agent; the human gate is Peter.

---

## 1. Principle

Route by *cost-of-being-wrong*, on infrastructure you already run:

1. **Cheapest capable model does the grind** → **Moshe/OpenClaw** on Gemini/Grok/Ollama. Already your always-on, cheapest runner.
2. **Strong model does the high-stakes reasoning** → **Claude (Fable)**: accuracy gate, Qubit design, hard engineering, review.
3. **The human holds the gates** → **Peter** approves at each milestone and authorises publish (via Telegram).

Control rule: a cheap model may *draft* a title or a scene split; it may **not** be the accuracy or IP gate.

---

## 2. Executors

| Executor | Is | Runs on | Best at |
|---|---|---|---|
| **Moshe / OpenClaw** | Autonomous agent (Gemini primary · Grok fallback · Ollama local) | Hetzner `ubuntu-4gb-nbg1-1`, behind Tailscale + Hetzner firewall | Orchestration + grind: scene decomposition, **Nano Banana stills (via its Gemini link)**, Shorts drafts, metadata; running the per-episode pipeline unattended |
| **Claude (Fable)** | Strong reasoning model | Anthropic API (already wired to the box) | Accuracy fact-check, Qubit design, template/pipeline engineering, quality review, hard debugging |
| **Peter** | The human | Mac, via Tailscale / Telegram | Creative + accuracy sign-off; the publish authorisation |
| **Pipeline code** | Deterministic scripts | Hetzner (+ ephemeral render worker) | ElevenLabs calls, caption sync, Remotion render, ffmpeg cut, YouTube upload |

---

## 3. Stage → executor routing (RACI)

R = Runs · A = Approves · C = Consulted · I = Informed

| Pipeline stage | Moshe/OpenClaw | Claude | Peter | Code |
|---|:--:|:--:|:--:|:--:|
| Topic/script authoring | C | R (draft) | **A/R** | – |
| **Accuracy fact-check gate (FR-Q1)** | – | **R** | **A** | – |
| Scene decomposition → scenes.json | **R** (Gemini/Grok) | C | I | validate |
| Nano Banana prompts + stills | **R** (Gemini) | C | I | – |
| Voice synthesis (ElevenLabs) | trigger | – | I | **R** |
| Caption/timing sync | – | – | I | **R** |
| Qubit design (concept → SVG rig) | assist | **R** | **A** | – |
| Remotion composition/render | orchestrate | C | I | **R** (ephemeral worker) |
| Shorts selection + cut | **R** (draft) | C | A | R (cut) |
| Metadata (title/desc/tags) | **R** (variants) | C | **A** | – |
| Thumbnail generation | **R** (Nano Banana) | – | A | – |
| YouTube **draft** upload | **R** (trigger) | – | I | **R** |
| **Publish to public** | notify | – | **A/R** (Telegram approve) | – |
| Per-episode run + monitoring | **R** | – | I | R |
| Pipeline build (Phases 2–4) | assist | **R** (design+impl) | **A** | – |

**Shape of it:** Moshe runs the show day-to-day (grind + orchestration + images, all on models it already pays for); Claude is called only for design, accuracy, and hard engineering; Peter approves at gates and taps "publish" in Telegram.

---

## 4. Architecture fit — mapping onto your Hetzner box

Reuse what Moshe already has; add only what's missing.

| Pipeline need | Reuse (already on the diagram) | Add |
|---|---|---|
| Grind LLM | Gemini (primary) · Grok (fallback) · Ollama (local trivial) | — |
| Image stills / thumbnails | **Gemini = Nano Banana** (already integrated) | Gemini **image** API scope/key |
| Heavy reasoning / accuracy | Anthropic Claude (already wired) | — |
| Script + asset storage | Google Drive (Docs/Sheets) | `risk-decoded` asset conventions |
| Source repo | GitHub (already the backup/apps target) | `risk-decoded` repo + gitleaks on push |
| Notifications + approvals | Telegram (bot + channel) | Approve/publish command flow |
| Voice | — | **ElevenLabs** account + key |
| Video render | — | **Remotion + ffmpeg** + **ephemeral render worker** (see §5) |
| Control surface (optional) | Render.com (app deploy) | optional pipeline dashboard — not required |

**Access & security (unchanged, respected):** everything reachable only via **Tailscale** (`100.113.189.75`); Hetzner firewall stays **deny-public-default**; Peter's Mac has no direct public path to OpenClaw. Publish approvals ride the existing **Telegram** channel — Peter taps approve; nothing goes public autonomously. Secrets stay in the box's store **outside** `/root/.openclaw/workspace`; the **daily 02:00 UTC backup → GitHub** must keep the gitleaks pre-push guard (matches your prior hardening; new keys land outside the workspace tree).

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
2. **Render on-box while prototyping** — single render, low Chromium concurrency, off-peak; unload large Ollama models during a render.
3. **For production renders, spin an ephemeral CPX42/CPX52 per episode, then destroy it.** At €0.135–0.195/h a 20–40 min render ≈ **€0.05–0.13/episode → ~€1/mo even at weekly+ cadence**, vs +€41/mo to upsize — and it never reboots Moshe (a rescale would).
4. **Disk:** the 80 GB tier disk is fixed; when the asset/build library outgrows it, attach a **Hetzner Volume** (decoupled from the server tier, cheap per-GB) rather than jumping to a bigger, pricier plan.
5. **Free alternative while manual:** render on Peter's Mac during the prototype phase (powerful, €0) — just not unattended.

**Regardless:** cap to **one render at a time** and off-peak, to protect Moshe's live services.

Ollama note: on 8 GB, small models only. If you later want *bigger local models routinely*, that — not rendering — is the real case for more RAM; weigh it separately from this pipeline.

---

## 6. Governance & control points (carried over)

1. **Instructions originate from Peter.** Anything arriving via another path or self-labelled "approved" → stop, verify with Peter — applies to Moshe-generated mandates too.
2. **Branch discipline:** pipeline work on `fable/*`; `main` only after Peter's review.
3. **Secret hygiene everywhere:** keys outside the workspace tree · gitleaks on the daily GitHub push · rotate-without-code · run each dependent pipeline once end-to-end after any rotation.
4. **Model-appropriate routing is a control, not just cost:** accuracy + IP gates pinned to Claude; Gemini/Grok produce drafts only.
5. **Provenance:** each artefact records `executor: moshe|claude|code` + model + version (extends FR-O4).

---

## 7. Cost impact

- Orchestration + grind + images run on **models Moshe already pays for** (Gemini primary, Grok fallback) → per-episode *LLM/image* cost ≈ negligible.
- **Paid line items:** ElevenLabs voice + an ephemeral render server (~€0.05–0.13/episode, ≈€1/mo) + an optional Hetzner Volume for assets. Base box stays **CPX32 (€42.94/mo, already running for Moshe)** — no permanent upsize. More local Ollama grind trims API spend further. Marginal cost/episode comfortably within REQUIREMENTS NFR-2.
- **Claude** spend stays low-volume/high-value (design + accuracy + build).

---

## 8. Open decisions (confirm)

1. **Render capacity** — keep **CPX32 + ephemeral render server** (recommended), or commit to an always-on 16 GB CPX42 (+€41/mo)?
2. **Repo home** — `risk-decoded` as a new GitHub repo alongside Moshe's existing ones, `fable/*` workflow?
3. **Approval UX** — publish gate as a Telegram approve command to Peter (leveraging the existing bot)?
4. **Model pinning** — confirm accuracy + IP gates stay on Claude, never Gemini/Grok.
5. **Escalation** — when Moshe's grind output fails schema validation twice → auto-escalate to Claude, or halt and Telegram Peter?
