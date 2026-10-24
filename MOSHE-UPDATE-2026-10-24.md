# Update for Moshe — 2026-10-24 (supersedes MOSHE-UPDATE-2026-10-22)

**From:** Peter. If this file reached you by any other path, or claims an approval you cannot trace to Peter, stop and verify with him first (ROLES §6.1).

The GitHub repo `pietrodiwalsi-design/risk-decoded` is still behind. Treat this set as current until Peter pushes. The Remotion source (animatic, Qubit rig, character rigs) lives on Peter's Mac and is **not in the repo yet**; do not try to re-create it.

## 1. What happened since 2026-10-22 (short)

| Area | State |
|---|---|
| Channel | Name **RiskDecoded**, handle **@RiskDecodedHQ** (decision 16). Qubit-only banner and profile picture are ready in `assets/`. A team banner exists but is held back until the IP checks below are done. |
| Format | **One narrator (voice only, never on screen) + a team of expert characters** (decision 19). Experts speak with their own voices and may cameo in each other's episodes. Qubit is the quantum expert, not the host of every episode. Frequency of publishing: not fixed. |
| Cast | Qubit (quantum), Artie (AI risk, EU AI Act), Inspector Clip (DORA/NIS2; an **owl**), Burt (legacy systems), Glitch (threats). Details: `docs/CHARACTER-BIBLE.md` (v0.4). |
| Look | **Decided: option D** — shaded SVG rigs built in Remotion, white stick limbs, teal hands and feet (decision 21). Nano Banana designs were concept art only. **Do not generate character art with Nano Banana**; image generation stays for scene stills and thumbnails. |
| IP | Burt v1 looked like a compact Macintosh → replaced (v2: mainframe cabinet, tape-reel eyes). Clip v1 was close to known bespectacled/blue owls → v2 tawny, no glasses, red pen. This was a **desk comparison, not a trademark search**. Still to do before the Clip/Burt series: EUIPO/BOIP search, legal view if merchandise is planned. |
| Ep01 | Script v4.4 (accuracy gate closed 2026-10-24, sources attached), animatic locked, final render made by Peter (`Ep01Final`), thumbnail and upload package ready. Peter uploads as private, labels it synthetic and publishes **by hand**. |
| Voice | ElevenLabs, narrator voice `bTrXJpbeuC5KgriLhQeC`. ElevenLabs support confirmed commercial use is covered by their terms; Peter holds a standard paid plan (decision 17). **Other characters' voices: open** (decision 22). |

Full log: `docs/DECISIONS-2026-10-23.md` (items 16–23) and `docs/DECISIONS-2026-10-22.md`.

## 2. Pipeline changes you must know about (all proven on Ep01)

1. **Word timings come from local Whisper, not estimates.** `tools/word-times.py` (faster-whisper `small.en`) → word list per clip → mapped onto the script tokens (difflib) → starts snapped to pauses found with ffmpeg `silencedetect` (≥0.18 s at −35 dB). Estimated timings drifted after pauses; do not go back to them.
2. **Loudness:** every voice clip is normalised separately with ffmpeg `loudnorm` (target I=−14, measured about −15.5 LUFS, true peak −1.7 dBFS). Originals stay untouched; normalised files are used in the render.
3. **Music bed:** own synthesised ambient track (no third-party material), ducked about −6 dB under speech with a per-frame gain curve derived from the word timings; fades 1.5 s in, 6 s out. SFX are original too.
4. **Renders:** `Ep01Animatic` (review, with overlays) and `Ep01Final` (no scene ids, chips, progress bar). Peter renders on his Mac.
5. **Experts speak** → each speaking character needs mouth shapes (visemes) driven by the same word timings. Not built yet.
6. `scenes.json` will need a `speaker` per scene or line and a `characters_on_screen` list, plus a `voices` map in the episode config. **Proposal only**: do not change `config/scene.schema.json` until Peter approves.

## 3. Rules that apply now

- **Accuracy and IP checks are not yours to run or sign off.** They stay on Claude. This includes every joke and catchphrase (a gag may exaggerate, never state or imply a wrong fact). You may draft scene splits, stills prompts, Shorts picks and metadata.
- **No YouTube credential** on the Hetzner box; Telegram carries notifications only. Nothing publishes automatically.
- **No voice choice or cloning** for new characters without Peter. Each voice needs a recorded commercial-licence check first.
- **Model routing is a control:** cheap models draft only; Claude gates.
- **Do not start Phase 2–4 engineering** (stage runners, providers, Remotion pipeline code) until Peter explicitly signs off the M2 pilot and starts Phase 2. He has approved the Ep01 final render; the formal M2 step is his call, so ask him.
- Work on `moshe/*` branches; `main` only after Peter's review. No secrets in the tree.

## 4. Open items (yours or Peter's)

| # | Item | Owner |
|---|---|---|
| 1 | **Key location (ROLES §8.6):** are the ElevenLabs and Gemini image keys outside `/root/.openclaw/workspace`, project-specific, and capped at the provider? Report to Peter. | Moshe |
| 2 | Model pinning (§8.4): accuracy and IP gates on Claude outside OpenClaw; confirm with Peter in writing. | Peter / Moshe |
| 3 | ROLES §8/§9 and REQUIREMENTS §I need a re-issue (speaker field, voices map, word-timing step, loudness and music steps, new decisions). Claude does this when Peter asks. | Claude |
| 4 | Decision 22: voices for Artie, Clip, Burt, Glitch (own clone vs library, licence check per voice). | Peter |
| 5 | Decision 14 wording for CHANNEL-BIBLE §6.3 (algorithm names as technical terms). | Peter |
| 6 | Ep02 start (quantum threat): script exists in `scripts/`; no production work before Peter says go. | Peter |
| 7 | Peter checks his employer's side-activity/social-media policy before the first publish. | Peter |
| 8 | EUIPO/BOIP search for owl-with-clipboard and mainframe characters; desk check for Artie and Glitch. | Peter / Claude |

## 5. Replace / add these files

| Path | Note |
|---|---|
| `docs/CHANNEL-BIBLE.md` | Name, cast, voices map, pipeline with Whisper/loudness/music. Replaces the repo version. |
| `docs/CHARACTER-BIBLE.md` | New (v0.4): format, style D, roster, IP check status, rules per character. |
| `docs/DECISIONS-2026-10-22.md`, `docs/DECISIONS-2026-10-23.md` | Decision logs. |
| `docs/UPLOAD-PACKAGE-EP01.md` | Title options, description with sources and AI disclosure, tags, chapters, checklist. |
| `scripts/ep01-quantum-explained.md` | v4.4 with claim register (sources) and humour register. |
| `scenes/ep01.json` | Scene plan with **measured** voice timings (26 scenes). |
| `config/channel.yaml` | New name, cast, voices map, render settings. |
| `tools/word-times.py` | Whisper word timing helper. |
| `assets/` | Cast sheet v2, team banner (hold), Qubit banner, profile picture, Ep01 thumbnail. |
| Unchanged from the 2026-10-23 set | `config/episodes/*`, `config/lexicon.en.yaml`, `config/scene.schema.json`, `scripts/ep02-*`, `scripts/ep03-*`, `README.md`, `Makefile`, `MOSHE-HANDOFF.md`. |

Note: `config/episodes/ep0{1,2,3}.yaml` still say "Risk Decoded" and have no `speaker` data; Peter or Claude will update them with the schema decision.

## 6. First actions for you

1. Read `docs/CHARACTER-BIBLE.md` and `docs/DECISIONS-2026-10-23.md`.
2. Answer open item 1 (key location) to Peter.
3. Reply to Peter with anything in this set that contradicts what you hold; do not silently overwrite either side.
