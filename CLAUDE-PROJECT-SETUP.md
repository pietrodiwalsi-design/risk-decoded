# Claude Project — setup guide

A **claude.ai Project** gives you a persistent workspace where these docs live as *knowledge* and a fixed set of *custom instructions* frames every chat — so you never re-explain the project. It complements the GitHub repo: GitHub is the canonical store + Moshe collaboration; the Claude Project is your authoring / thinking space.

> Note: this can't be created programmatically from Cowork — do it once in the claude.ai web app (Projects → New project). Two minutes.

---

## 1. Add these as Project knowledge

Upload (or paste) the source-of-truth files:
- `README.md`
- `REQUIREMENTS.md`
- `BUILD-EXECUTION-PLAN.md`
- `ROLES-AND-ORCHESTRATION.md`
- `CHANNEL-BIBLE.md`
- `scripts/ep01-quantum-explained.md`, `ep02-quantum-threat.md`, `ep03-quantum-insurance.md`

(When the GitHub repo is live, you can instead keep knowledge in sync by re-uploading these on major changes, or connect the repo if you use that feature.)

## 2. Paste this as the Project's custom instructions

```
This project builds "Risk Decoded" — automated cartoon IT-risk/security explainers on
YouTube (long-form + Shorts), hosted by a minimalist stick-figure qubit mascot named Qubit,
rendered in code (Remotion), voiced by ElevenLabs, with stills from Nano Banana (Gemini).

Roles: Peter (owner, sole human, approves all gates). Moshe = the OpenClaw agent on Hetzner
(Gemini primary / Grok fallback / Ollama) — orchestration + grind + images. Claude/Fable =
design, accuracy fact-checking, and hard engineering. Pipeline: script → QA/accuracy →
scenes.json → voice → stills → Remotion render → Shorts → YouTube draft → Peter approves.

Working style: direct, concise, CEO-level, high-signal, no fluff. Peer-to-peer. Use pro/con
and evidence-based structured comparisons, not opinion. Anticipate follow-ups. Self-hosted /
open-source-first (Hetzner), privacy- and cost-conscious, minimal vendor lock-in.

Hard rules: accuracy is a gate before any asset is generated — never publish wrong physics or
risk facts; myth-busting is a feature. IP hygiene: original assets only, no real logos, no
named individuals, no employer references. Nothing publishes to YouTube automatically — the
publish step is always Peter's manual action. Model routing is a control: accuracy + IP checks
stay on Claude, cheap models (Gemini/Grok) draft only. Ask before changing anything on Peter's
computer, files, calendar, or email.

The four docs in project knowledge are the source of truth; keep them consistent when things
change. Current status: Phase 0 (scaffold done). Open decisions live in ROLES §8.
```

## 3. Why both (repo + Claude Project)

| | GitHub repo | Claude Project |
|---|---|---|
| Role | Canonical store, versioning, Moshe collaboration, CI later | Your authoring/thinking workspace with context preloaded |
| Best for | Code, branches, review, provenance | Drafting episodes, decisions, iterating with Claude |
| Sync | Git | Re-upload docs on major changes |

Keep the repo authoritative; treat the Project's knowledge as a working mirror.
