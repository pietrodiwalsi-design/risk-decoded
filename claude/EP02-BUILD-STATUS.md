# Ep02 build status (2026-10-26)

Built by hand on Peter's Mac (`~/Documents/07 Qubit-test`); Claude writes code, Peter runs and approves. Moshe/schema implementation waits until after Ep02 sign-off (decision 31).

## State
**Ep02 long-form and Short A re-rendered and re-uploaded as unlisted on 2026-10-25 (evening); Short C and Ep01 unchanged. Not yet public.** URLs and details: `DECISIONS-2026-10-25-c.md` (item 47).

## Done
- Audio: 42 clips in use (`public/audio-ep02/`), normalised copy `public/audio-ep02-norm/` (-20 LUFS + limiter, v2). Option A (Glitch speaks more) done. On 2026-10-25 evening four clips were re-recorded: `s1-5-qubit`, `s3-9-glitch`, `s6-1-qubit`, `s10-3-qubit` (decision 43). Old versions: `public/audio-ep02-prev-2026-10-25/`.
- Word timings: `src/words-ep02.ts` (regenerated after the four clips).
- Glitch rig v1 (approved): `Glitch.tsx`, `GlitchSheet.tsx`, `GlitchRoot.tsx`, `glitch-index.ts`.
- Animatic code: `Ep02Stage.tsx` (corners layout, captions, visemes), `Ep02.tsx` (scenes 1–2), `Ep02Scenes.ts` (scene data), `Ep02Anim.tsx` (animations scenes 3–10), `Ep02Full.tsx` (composition, music ducking, end card), `Ep02Shorts.tsx`, `Ep02Root.tsx`, `ep02-index.ts`.
- Compositions: `Ep02Proof` (scenes 1–2), `Ep02Full` (all, 549.3 s = about 9:09 incl. gaps, 3.5 s title, 8 s end card), `Ep02ShortA`, `Ep02ShortC` (1080x1920).
- Scenes 1–2 stay in the original large-character layout on purpose (Peter); scenes 3–10 use the corner layout with one animation per scene, triggered by spoken words.
- Delivery files (Peter's Mac, `out/`): `ep02-final-loud.mp4` (-14.1 LUFS, TP -1.4), `ep02-short-a-loud.mp4` (53.8 s, -14.1, -1.4), `ep02-short-c-loud.mp4` (54.4 s, -14.1, -1.5); thumbnails `riskdecoded-ep02-thumbnail-1280x720.png`, `riskdecoded-ep02-short-a-thumbnail-1080x1920.png`, `riskdecoded-ep02-short-c-thumbnail-1080x1920.png`. Previous renders: `out/prev-2026-10-25/`.
- Placeholders removed (decision 45): debug watermark and end-card placeholder text. End card now: "Next time / What quantum is actually good for".
- Upload packages: `UPLOAD-PACKAGE-EP02.md` (v2, chapters for 9:09), `UPLOAD-PACKAGE-EP02-SHORTS.md`.

## Open
- Peter, in YouTube Studio: finish descriptions and links (see decision 48), end screens/cards, AI disclosure and "Not made for kids" on all four uploads, delete the superseded uploads, then choose the publication mode. Publishing is always Peter's manual action.
- Glitch voice licence table (plan, ToS date, terms) still open.
- EUIPO/BOIP trademark search raccoon+hoodie before the first public upload; employer side-activity policy check.
- Re-check on publish day: NIST IR 8547 (claim 11, still an initial public draft per NIST's project page on 2026-10-25), EU Quantum Act (claim 12f; the optional clip `s6-1-opt-qubit` is not in the video).
- `claude/scenes-ep02.json` and `claude/ep02-clip-list-v2-delta.md` still describe the earlier distribution and old timings; regenerate the JSON when the schema is implemented (the four changed lines are patched in `ep02-clip-list.md` and `ep02-dialogue-v1.md`).
- Ep01 Shorts were never built (candidate: Short C "Hackers are stealing your data today to crack it later"); optional Ep02 Shorts B (who is exposed, 36 s) and D (Plan B, 58 s).
- Ep03 title and script (older draft with host Max, needs rework to Qubit and Glitch).
- Leftover temp files in `out/` (`shorts-check.html`, `thumbv-check.html`): remove with Peter's OK.

## Pre-upload checklist (new, decision 45)
1. `grep -n -i "placeholder\|animatic" src/*.tsx` returns nothing relevant.
2. Look at the first, a middle and the last frame of the final file at full size.
3. Loudness: `*-loud.mp4` at about -14 LUFS, true peak below -1.0.
4. Chapter times match the final length; links in descriptions point to the current URLs.

## Tooling notes
- Render: `npx remotion render src/ep02-index.ts Ep02Full out/ep02-final.mp4` (Shorts: `Ep02ShortA`, `Ep02ShortC`); then a two-pass ffmpeg loudnorm (I=-14, TP=-1.5, LRA=11, linear) to `*-loud.mp4`.
- Word timings: `.venv-ep02` (faster-whisper): `python3 tools/word-times-ep02.py && python3 tools/build-words-ep02.py`.
- First `device_commit_files` after rewriting a file often does not take; verify on the Mac and re-commit with force.
