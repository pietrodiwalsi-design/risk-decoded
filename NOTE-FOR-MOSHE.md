NOTE FOR MOSHE

Hi Moshe. This is the shared repo for Risk Decoded: automated cartoon IT-risk and security explainers hosted by Qubit, our minimalist vector mascot. Peter created it. The full design docs and the three episode scripts are staged on Peter's machine under Downloads/risk-decoded-channel and will be pushed here shortly.

YOUR ROLE, from ROLES-AND-ORCHESTRATION
You are the orchestrator and grinder: scene decomposition, Nano Banana stills through your Gemini link, Shorts drafts, metadata, and running the per-episode pipeline on the Hetzner box. Claude and Fable handle design, accuracy fact-checking, and hard engineering. Peter approves every gate and is the only one who publishes.

HOW THE FULL PROJECT ARRIVES
The complete scaffold - README, REQUIREMENTS, BUILD-EXECUTION-PLAN, ROLES-AND-ORCHESTRATION, CHANNEL-BIBLE, config, and pipeline stubs - is on Peter's machine and will be pushed with git. This repo already has an initial commit, so reconcile with: git pull --allow-unrelated-histories origin main, then add the files and push. Or clone this repo and copy the files in.

CONVENTIONS
Work on branches named fable/* for Claude work and moshe/* for your work. Merge to main only after Peter reviews. Keep all secrets outside the repo tree and keep the gitleaks pre-push guard on the daily backup. Never commit keys or media. After any credential rotation, run each dependent pipeline once end to end before the next scheduled run.

FIRST DISCUSSION POINTS - the open decisions in ROLES section 8
Render capacity: keep CPX32 plus an ephemeral render server, or upsize. How you invoke the pipeline: CLI, HTTP, or a job queue. Model pinning: accuracy and IP checks stay on Claude, never Gemini or Grok. Escalation when your output fails validation twice.

Start from the README once the docs land. Open an issue for questions, or put proposals on a moshe/* branch.

- Peter
