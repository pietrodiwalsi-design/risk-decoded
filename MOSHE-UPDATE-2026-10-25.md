# Update for Moshe — 2026-10-25

From Peter (via Claude). Supersedes the Ep02 and schema parts of `MOSHE-UPDATE-2026-10-24.md`. Full log: `claude/DECISIONS-2026-10-25.md` (items 30–35).

## What changed
1. **Ep02 is a dialogue (Qubit + Glitch).** Script of record: `claude/ep02-dialogue-v1.md` (v1.3, approved). `ep02-quantum-threat.md` (old monologue, host "Max") is reference only: do not use it for scenes, stills or metadata.
2. **Glitch is female (she/her)**, voice chosen by Peter (decision 34). Voices are Peter's choice only: do not select, change or clone any voice.
3. **Ep02 voice clips exist:** 41 clips (Qubit and Glitch) on Peter's Mac in `public/audio-ep02/`. Do not regenerate or replace them.
4. **Concept `claude/scenes-ep02.json`** links scenes to clips. It is a draft for the by-hand build, not input for a Hetzner run.

## What stays the same / what NOT to do
- **Ep02 is built by hand on Peter's Mac** (Whisper timings, loudness, Remotion render), as Ep01. No Hetzner run for Ep02.
- **Do not touch `config/scene.schema.json`** or start the speaker/voices schema work (decision 31). It starts after Ep02 is finished, with Ep01 and Ep02 as test cases, on a `moshe/*` branch, reviewed by Claude, merged by Peter. Spec: `claude/SCHEMA-SPEAKER-v1.md`.
- Phase 2-4 engineering still waits for Peter's explicit M2 sign-off.
- Accuracy and IP checks (including every joke) stay with Claude. Nothing publishes automatically.

## Open items (Peter or Claude)
- Next-episode line for the Ep02 outro waits for the Ep03 title.
- Glitch rig, mouth shapes and desk IP check (Claude).
- Your earlier open items (key location ROLES §8.6, model pinning §8.4) still apply.
