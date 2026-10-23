# Risk Decoded — Decisions 2026-10-22

Taken by Peter. These supersede the open items in ROLES §8 and REQUIREMENTS §I until the docs are re-issued.

| # | Topic | Decision | Replaces |
|---|---|---|---|
| 1 | Render | On Peter's Mac for now. Revisit at M3 with a measured render time. | ROLES §8.1 |
| 2 | Draft upload | Manual upload in YouTube Studio. No Mac-side script. | ROLES §8.3 |
| 3 | Escalation | Failing schema validation twice: halt and Telegram Peter. | ROLES §8.5 |
| 4 | Channel goal | Credibility first, monetisation second. | ROLES §8.7 |
| 5 | Voice | ElevenLabs. Voice "Peter", `voice_id` `bTrXJpbeuC5KgriLhQeC`. | REQUIREMENTS §I.3 |
| 6 | Qubit look | Current rig and poses approved for the M2 pilot (placeholder look, no Nano Banana concept round). | REQUIREMENTS §I.2 |
| 7 | EP01 script | v4 approved: accuracy rewrite, medium humour, Einstein allowed as a named historical scientist, measurement gag is "snap to 0/1" (no blushing). Runtime about 7:20. | v1 |
| 8 | IP rule | Named historical scientists are allowed in narration (text only, no likeness). Living people, vendors, logos and employer references stay out. | CHANNEL-BIBLE §6.3 clarification |
| 10 | EP01 scene plan | 26-scene `scenes/ep01.json` approved by Peter on 2026-10-23 (timings estimated, to be replaced by real voice durations). | — |
| 11 | ElevenLabs plan | Starter plan (includes commercial licence for speech). Library voice "Peter" (`bTrXJpbeuC5KgriLhQeC`); written confirmation of commercial use requested from ElevenLabs support on 2026-10-23, answer pending. Fallback: shortlist of 2–3 similar voices. | — |
| 12 | Voice settings | Set B locked 2026-10-23: model eleven_multilingual_v2, stability 50, similarity boost 75, style 0, speed 1.00. Pauses via `<break time="0.5s" />` tags. First three clips (cold open) generated and measured. | — |
| 9 | Phase scope | Peter and Claude build EP01 by hand first (scenes.json as data, animatic, voice, render). No Phase 2–4 engineering by Moshe before M2. | unchanged |
| 13 | EP01 accuracy fix (scene 10) | Peter flagged that "small" is wrong for today's quantum computers (physically large machines). Replaced with "only a modest number of reliable qubits" (script v4.1). Clip `s10` to be regenerated with Set B and re-measured; timings for scene 10 and later scenes shift. | CHANNEL-BIBLE accuracy gate |

Still open: key location check (ROLES §8.6), model pinning confirmation (§8.4), channel name, cadence.

Not yet re-issued: ROLES §8/§9 and REQUIREMENTS §I (this log carries the decisions until the next revision).
