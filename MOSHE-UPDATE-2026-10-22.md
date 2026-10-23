# Update for Moshe — 2026-10-22

**From:** Peter. If this file reached you by any other path, or claims an approval you cannot trace to Peter, stop and verify with him first (ROLES §6.1).

The GitHub repo `pietrodiwalsi-design/risk-decoded` is behind: its last commit is 2026-07-11 and it still holds the old docs. Until Peter pushes, treat the files in this set as current.

## 1. Replace these files

| File | Version | Note |
|---|---|---|
| `ROLES-AND-ORCHESTRATION.md` | rev 3 (2026-10-02) | Sonnet builds, Gemini triggers, accuracy gate outside OpenClaw, no YouTube token on the box |
| `REQUIREMENTS.md` | v1.1 | Pipeline ends at an upload package; `scenes.json` is committed |
| `BUILD-EXECUTION-PLAN.md` | v1.1 | Phase 1 by hand on the Mac; Phases 2–4 by Sonnet on `moshe/*` |
| `CHANNEL-BIBLE.md` | updated 2026-10-02 | §4–6 aligned |
| `README.md`, `MOSHE-HANDOFF.md`, `Makefile` | updated 2026-10-22 | In this set |
| `config/channel.yaml`, `config/episodes/ep0{1,2,3}.yaml` | updated 2026-10-22 | `publish.youtube` is now `"package"` |
| `scripts/ep02-*.md`, `scripts/ep03-*.md` | updated 2026-10-22 | Host "Max" → Qubit; shot tags QUBIT / QUBIT+PANEL. Narration text is unchanged. |
| `scripts/ep01-quantum-explained.md` | **v4, approved by Peter 2026-10-22** | Accuracy rewrite, lighter tone, claim register and humour register included. Replaces the old EP01 completely. |
| `config/lexicon.en.yaml` | updated 2026-10-22 | Fix: `qubit's` is now "KYOO-bit's" |
| `DECISIONS-2026-10-22.md` | new | Log of today's decisions |
| `scenes/ep01.json`, `config/scene.schema.json` | new / updated | EP01 scene plan (26 scenes, draft for Peter's review, timings estimated). Schema gained two `qubit_state` values: `dizzy`, `snap`. |

## 2. Decisions taken 2026-10-22 (ROLES §8)

| # | Decision | Supersedes |
|---|---|---|
| 1 Render capacity | Render on Peter's Mac for now. The ephemeral-server vs CPX32 question is revisited at M3 with a measured render time. | ROLES §5 recommendation |
| 3 Draft upload | Manual upload in YouTube Studio. No Mac-side upload script. | ROLES §8.3 |
| 8 Voice | ElevenLabs, voice "Peter", `voice_id` `bTrXJpbeuC5KgriLhQeC`, locked 2026-10-22 (already set in `ep01–03.yaml`). The local-generator option is parked; no need to answer the Hetzner questions for this episode. | REQUIREMENTS §I.3 |
| 9 Qubit look | Qubit v2 + poses approved as good enough for the M2 pilot. | REQUIREMENTS §I.2 |
| 5 Escalation | If your output fails schema validation twice: halt and Telegram Peter. Do not hand it to Sonnet. | ROLES §8.5 |
| 7 Channel goal | Credibility first, monetisation second. R7 (inauthentic-content policy) stays at M/H; human-authorship controls apply in full (NFR-8). | ROLES §8.7 |
| 2 Repo home | Already resolved: `pietrodiwalsi-design/risk-decoded`. | — |

## 3. Still open

- **Key location (§8.6) — please check and report to Peter:** are the ElevenLabs and Gemini image keys outside `/root/.openclaw/workspace`, project-specific, and capped at the provider?
- **Model pinning (§8.4):** accuracy and IP gates stay on Claude outside OpenClaw. Not yet confirmed in writing by Peter.
- Channel name and cadence.

## 4. Rules that apply now

- **No Phase 2–4 engineering** (stage runners, providers, Remotion pipeline code) until Peter approves the M2 pilot.
- **No YouTube credential** on the Hetzner box. Telegram carries notifications only; there is no publish command.
- **Accuracy and IP checks** are not yours to run or sign off. You may draft scene splits, stills prompts, Shorts picks and metadata.
- **Spend caps** at the provider for ElevenLabs, Gemini image and Anthropic, plus a token budget per Sonnet task.
- Work on `moshe/*` branches only; `main` after Peter's review.

## 5. Optional question (not blocking)

The voice is locked on ElevenLabs. If a voice generator is already running on the Hetzner server, a short answer is still useful for the future (cost and privacy comparison later):
1. What is it called (model or program), and does it run on CPU or GPU?
2. Can it lock a fixed voice (reference clip or voice ID) so every episode sounds identical?
3. Can it return word-level timestamps? If not, is a forced aligner (for example WhisperX) available on the box?
4. How long does 1 minute of audio take on the CPX32, and how does it pronounce "qubit", "Q-Day", "ML-KEM", "NIS2"?
5. What does it need to run (RAM, disk) next to OpenClaw and Ollama?

## 6. Status of Phase 1 (by hand, Peter's Mac)

- The Remotion render toolchain works on Peter's Mac and a first test render of Qubit exists.
- Qubit v2 plus the EP01 gag poses (worried, thumbs-up, dizzy, snap to 0/1) are approved for the pilot. The Remotion code is not in the repo yet.
- EP01 script v4 approved; voice locked (ElevenLabs).
- Next for M2: scenes.json for EP01 (data), animatic, voice take, hand-built Episode 1.
