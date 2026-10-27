# Moshe: generate Ep03 voice clips (budget-safe)

Owner: Peter. Date: 2026-10-27. Read `claude/ep03-clip-list.md` (project doc, script of record for clip texts, settings and pauses). Do not change any text.

## Goal
Generate 57 MP3 clips with ElevenLabs (32 Qubit, 25 Glitch), name them exactly as in the clip list, check each one, and report. Nothing else. Do not start animation, stills, or Remotion work.

## Budget rules (most important)
ElevenLabs credits are the only limit. Your own (OpenClaw) tokens are not a concern; use as many turns as you need to do this well. Total text is about 8,600 characters (Qubit 7,640, Glitch 970). One full pass is about 8,600 credits. We cannot afford more than one full pass plus a few retries.
1. Check the remaining ElevenLabs credit balance first. If it is below 12,000, stop and tell Peter before generating anything.
2. Use a script (Python or Node) that loops over the clip list, so no ElevenLabs call is made by hand or twice by accident. You may think and check freely between calls; just never trigger a generation you did not plan.
3. Never regenerate "to see if it sounds better". A clip is regenerated only when a check below fails, at most ONE retry per clip. After a second failure: stop on that clip, list it, move on, and tell Peter.
4. Never re-run the whole batch. If something fails, re-run only the failed clips (skip files that already exist and pass).
5. Log every call (clip name, characters, result) in `public/audio-ep03/manifest.csv`, with a running credit total.

## Step 1: voice test (3 clips, about 600 credits)
Generate only these three, then run the checks and stop for Peter's OK before the rest:
- `s4-9-qubit` (short Qubit line)
- `s1-3-glitch` (Glitch with a break tag)
- `s7-2-qubit` (Qubit with breaks, medium length)
Peter listens. Only after his explicit OK: Step 2.

## Settings (do not change)
| | Qubit | Glitch |
|---|---|---|
| Voice | Peter, `bTrXJpbeuC5KgriLhQeC` | Juniper, `aMSt68OGf4xUZAnLpTU8` |
| Model | `eleven_multilingual_v2` | same |
| Stability / Similarity / Style | 0.50 / 0.75 / 0 | 0.50 / 0.75 / 0 |
| Speed | 1.0 | 0.95 |
Output MP3 44.1 kHz 192 kbps. Paste the clip text exactly, including the `<break time="..." />` tags. Do not add or remove words, ellipses or punctuation.

## Step 2: the rest (54 clips)
Save to `public/audio-ep03/` only. Never write to `audio14` or `audio-ep02`. Never overwrite an existing passing file.

## Check every clip yourself, before reporting
Run these locally for each file (install Whisper before Step 1, so the three test clips are checked too) and write the result to the manifest:
1. File exists, size greater than 5 KB, decodes (`ffprobe`).
2. Duration is plausible: expected seconds is roughly words / 2.5 plus the sum of the break tags (Qubit) or words / 2.3 plus breaks (Glitch). Flag if more than 35% off.
3. No long silence inside the clip except the planned breaks: `ffmpeg -af silencedetect=noise=-40dB:d=1.0`. Flag any silence over 1.0 s longer than its planned break, and any leading or trailing silence over 0.5 s.
4. No clipping: peak below -1 dBFS (`ffmpeg volumedetect`).
5. Transcript check with a local Whisper. You may install it (for example `faster-whisper`, model `small` or `base.en`, CPU is fine). Peter approves the install. Use it locally only, never a paid transcription API. Transcribe each clip, strip punctuation, and compare with the clip text (break tags removed). Flag a word error rate above 8%; also read the flagged transcript yourself and judge whether it is a real mispronunciation or just a Whisper error (names, numbers, "qubits", "Monte Carlo") before spending a retry.
A clip that fails any check gets its one retry. If it fails again, list it and move on.

## Report to Peter (short)
- Credits at start and end, characters used, number of retries.
- Table: clip, duration, status (pass / retried / failed with the reason).
- Anything odd: mispronounced word, instability in a long clip.
- If `s10-3-qubit` (814 characters, six breaks) sounds unstable, split it after "press releases." and at "Four." (suffix a, b) and tell Peter. This is the only planned exception.

## Rules that still apply
- Do not change any script text. If you think a line is wrong, report it; Peter and Claude decide.
- Normalised copies (`public/audio-ep03-norm/`) are a later step, not now.
- Nothing is published, uploaded or shared. No other project files are changed.
