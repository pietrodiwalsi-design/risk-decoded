# src/providers (Phase 3)

One module per external service, behind a common interface so providers are swappable (NFR-10). No secrets in code — read keys from env / secret store outside the tree.

- **elevenlabs** — text → narration audio + word-level timings (FR-V1/V2); applies `config/lexicon.en.yaml`.
- **image (nano_banana)** — Gemini image API for scene art + thumbnails (FR-A4/A5); style-guided by `assets/style/` refs. Automation uses a Gemini **API** key (not Peter's consumer sub).
- **motion (optional)** — Higgsfield Cloud for rare hero clips (FR: SCENE). Default off.
- **youtube** — draft/private upload with metadata, thumbnail, AI-disclosure flag (FR-P1/P2). Never publishes public.

Each provider: typed input/output, retries + backoff, usage/cost reported back to the orchestrator for the run report (NFR-9).
