# Moshe update — 2026-10-26 (Ep02 final fixes)

For Moshe (OpenClaw), from Peter and Claude. Put the files of this bundle in the repo at the same relative paths (folder `claude/`); each replaces the file with the same name, except `DECISIONS-2026-10-25-c.md` and this note, which are new.

## What changed since MOSHE-UPDATE-2026-10-25
1. Peter's final watch of Ep02 led to four re-recorded clips (`s1-5-qubit`, `s3-9-glitch`, `s6-1-qubit`, `s10-3-qubit`), a real next-episode teaser and end card, and removal of two leftover placeholders (a debug watermark in the whole video and the end-card placeholder text). Details: `claude/DECISIONS-2026-10-25-c.md` (items 43–48).
2. Ep02 and Short A were re-rendered (Ep02 now 549.3 s, 9:09) and re-uploaded as unlisted, so they have new URLs. Short C and Ep01 are unchanged. All four are unlisted; publishing is Peter's manual action and the mode (all at once, staggered, scheduled) is still his choice.
3. New rule (decision 45): before any upload, grep `src/` for "placeholder" and "animatic" and look at the first, a middle and the last frame of the final file.

## URLs (all unlisted on 2026-10-25)
- Ep01: https://youtu.be/lymoZCijf6g
- Ep02 (current): https://youtu.be/lMsw8tRcY3w
- Short A (current): https://youtube.com/shorts/GIFVX-p6c1U
- Short C: not recorded yet (Peter to add)
- Superseded, to delete after checking: old Ep02 https://youtu.be/WGrU-bnIdys and the old Short A upload

## Files in this bundle (all under `claude/`)
- `DECISIONS-2026-10-25-c.md` (new)
- `EP02-BUILD-STATUS.md` (replaces)
- `UPLOAD-PACKAGE-EP02.md` (replaces; v2 with chapters for 9:09)
- `UPLOAD-PACKAGE-EP02-SHORTS.md` (replaces)
- `ep02-dialogue-v1.md` (replaces; v1.4, script of record)
- `ep02-clip-list.md` (replaces; four clips patched)

## Not done, for you (after Ep02 sign-off)
- `claude/scenes-ep02.json` is still the v1 distribution with old timings and old text for the four clips; regenerate it with the schema work. Do not touch `config/scene.schema.json` until M2 sign-off.
- Ep01 Shorts were never built; Ep03 needs a rewrite for Qubit and Glitch.
- Nothing in this bundle publishes anything.
