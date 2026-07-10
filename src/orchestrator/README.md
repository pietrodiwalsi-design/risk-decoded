# src/orchestrator (Phase 3)

Drives the episode pipeline stage-by-stage from `config/episodes/<ep>.yaml`.

Responsibilities:
- **Stage runners:** validate → voice → stills → render → shorts → draft (mirrors the Makefile).
- **Scene decomposition:** script.md → `build/<ep>/scenes.json`, validated against `config/scene.schema.json` (FR-C2). Routed to Moshe (Gemini/Grok); Claude on hard cases.
- **Caching + resumability (FR-O2):** skip completed, unchanged stages.
- **Cost caps (FR-O3):** enforce `image.max_images`, TTS char budget, optional video credits; stop cleanly on breach.
- **Provenance (FR-O4):** write a manifest per artefact — `executor: moshe|claude|code`, model, version, config + script hashes.
- **QA gate (FR-Q):** call the accuracy + IP checks (Claude) before any asset spend; block on unresolved flags.

Keep all logic here (not in the agent) so Moshe *or* Claude Code can invoke the same stages via a stable CLI/JSON contract (NFR-10).
