# Decisions — 2026-10-23 (continues DECISIONS-2026-10-22, items 1–15)

Owner: Peter. Format: decision · status · notes.

16. **Channel name and handle** — RiskDecoded, @RiskDecodedHQ · DECIDED (Peter). Frequency not fixed (decided to leave open until first episodes are live).
17. **ElevenLabs commercial use** — ElevenLabs support replied that voice use is covered by their general terms; the "Peter" voice stays available indefinitely; Peter holds a standard paid subscription with commercial rights · DECIDED (per Peter; terms not independently read by Claude). Keep audit trail: support reply, plan name/date, ToS version/date. Re-check if the plan is downgraded or cancelled.
18. **Ep01 animatic locked (production state)** · DONE.
    - Word timings measured with local Whisper (`tools/word-times.py`, faster-whisper small.en), mapped onto the script text, then snapped to pauses detected in the audio (replaces the earlier estimated timings, which drifted after pauses).
    - Voice normalised per clip to about −15.5 LUFS, true peak −1.7 dBFS, in `public/audio14/` (originals in `public/audio/` untouched).
    - Music bed: own synthesised ambient track (no third-party material), ducked about −6 dB under speech, fade in/out. Peter approved the level.
    - Animation SFX scaled ×3 to keep the approved balance against the louder voice.
19. **Format** — one narrator (voice only, never on screen) plus a team of expert characters; experts speak (own voices); experts may cameo in each other's episodes · DECIDED. Qubit is the quantum expert, not the host of all episodes; CHANNEL-BIBLE §2 amended.
20. **Cast and renames** — Qubit, Artie (AI risk), Inspector Clip (renamed from "Dora" for IP reasons), Burt (legacy), Glitch (threats). Catchphrases corrected: Qubit's "if you look, I collapse" removed (restates the observer myth that Ep01 scene 14 busts); "pension fund" and "Dave" removed (field/employer implication; named individual) · DECIDED. Build order proposed, not fixed.
21. **Character look** · DECIDED (Peter, 2026-10-24): option D, shaded SVG rigs in Remotion built after the Nano Banana designs; white stick limbs, teal hands and feet; Qubit stays as built. Inspector Clip is an owl (badger dropped). Rationale: simple graphic style suits IT-risk explainers, calmer than painted versions, code-animated, own art. Talking experts need mouth shapes driven by the word timings. IP desk check done 2026-10-24: Burt v2 (mainframe cabinet, tape-reel eyes) and Clip v2 (tawny owl, no glasses, red pen) adopted by Peter; not a trademark search (EUIPO/BOIP search still to do before the Clip/Burt series). Open: poses and mouth shapes, final banner. Qubit-only banner and pfp are ready for channel use. See CHARACTER-BIBLE v0.4 §2.
22. **Voices for the other characters** · OPEN. Per voice: own clone or library; commercial licence check per voice, recorded before first use.
23. **Before the first upload (gates)** · OPEN.
    - Final render without animatic overlays (label, scene ids, chips, progress bar).
    - Accuracy and IP gate with a source line per claim (open SRC items: NIST FIPS 203/204/205 Aug 2024, Nobel Prize in Physics 2022, Einstein phrase, Q-Day survey, Shor 1994/1997).
    - YouTube altered/synthetic content label on.
    - Channel assets redone: banner at 2560×1440 (YouTube minimum, as far as known, 2048×1152; generated file was 1998×1116), neutral pfp, no gibberish formulas or code, tagline without "unfiltered".
    - Channel description revised (see CHARACTER-BIBLE §8).
    - Peter checks his employer's side-activity/social-media policy before going live.
    - Nothing publishes automatically; Peter publishes by hand.

Still open from before: Moshe key-location check (ROLES §8.6), model pinning (§8.4), decision 14 wording for CHANNEL-BIBLE §6.3 (algorithm names as technical terms), ROLES §8/§9 and REQUIREMENTS §I re-issue (must add: speaker field, voices map, word-timing step, loudness and music steps).
