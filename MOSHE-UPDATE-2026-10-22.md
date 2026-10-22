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
| `scripts/ep0{1,2,3}-*.md` | updated 2026-10-22 | Host "Max" → Qubit; shot tags QUBIT / QUBIT+PANEL. Narration text is unchanged. |

## 2. Decisions taken 2026-10-22 (ROLES §8)

| # | Decision | Supersedes |
|---|---|---|
| 1 Render capacity | Render on Peter's Mac for now. The ephemeral-server vs CPX32 question is revisited at M3 with a measured render time. | ROLES §5 recommendation |
| 3 Draft upload | Manual upload in YouTube Studio. No Mac-side upload script. | ROLES §8.3 |
| 5 Escalation | If your output fails schema validation twice: halt and Telegram Peter. Do not hand it to Sonnet. | ROLES §8.5 |
| 7 Channel goal | Credibility first, monetisation second. R7 (inauthentic-content policy) stays at M/H; human-authorship controls apply in full (NFR-8). | ROLES §8.7 |
| 2 Repo home | Already resolved: `pietrodiwalsi-design/risk-decoded`. | — |

## 3. Still open

- **Key location (§8.6) — please check and report to Peter:** are the ElevenLabs and Gemini image keys outside `/root/.openclaw/workspace`, project-specific, and capped at the provider?
- **Model pinning (§8.4):** accuracy and IP gates stay on Claude outside OpenClaw. Not yet confirmed in writing by Peter.
- **Voice provider:** Peter is weighing ElevenLabs against a local generator. See the questions in section 5.
- Channel name and cadence.

## 4. Rules that apply now

- **No Phase 2–4 engineering** (stage runners, providers, Remotion pipeline code) until Peter approves the M2 pilot.
- **No YouTube credential** on the Hetzner box. Telegram carries notifications only; there is no publish command.
- **Accuracy and IP checks** are not yours to run or sign off. You may draft scene splits, stills prompts, Shorts picks and metadata.
- **Spend caps** at the provider for ElevenLabs, Gemini image and Anthropic, plus a token budget per Sonnet task.
- Work on `moshe/*` branches only; `main` after Peter's review.

## 5. Questions for you

Peter mentioned that a voice generator is already running on the Hetzner server. Please answer:
1. What is it called (model or program), and does it run on CPU or GPU?
2. Can it lock a fixed voice (reference clip or voice ID) so every episode sounds identical?
3. Can it return word-level timestamps? If not, is a forced aligner (for example WhisperX) available on the box?
4. How long does 1 minute of audio take on the CPX32, and how does it pronounce "qubit", "Q-Day", "ML-KEM", "NIS2"?
5. What does it need to run (RAM, disk) next to OpenClaw and Ollama?

## 6. Status of Phase 1 (by hand, Peter's Mac)

- The Remotion render toolchain works on Peter's Mac and a first test render of Qubit exists.
- Qubit v2 (look, poses, moods) is approved as a starting point and not final. It is not in the repo yet.
- Open for M2: Episode 1 script review, voice choice, hand-built Episode 1.
