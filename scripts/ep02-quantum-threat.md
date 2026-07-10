# Episode 02 — "The Quantum Threat: Harvest Now, Decrypt Later"

**Runtime target:** ~6:50 · **Host:** Max · **Language:** English
**Arc:** The threat (HNDL / Q-Day) → why it's urgent *now* → what to do (practical vs not) → Plan B if you're not ready
**Series note:** Sequel to Episode 1. Opens with a 10-second recap bridge.

---

## A. Narration script (voiceover master)

> TTS-friendly: short lines, one idea each. `[beat]` = pause. Bracketed notes = production only.

**[COLD OPEN — HOST]**
Somewhere right now, someone is stealing data they can't even read yet. [beat]
Encrypted files. Locked. Useless to them… today.
They're storing it anyway — betting that in a few years, they'll have the key.
This isn't science fiction. Intelligence agencies say it's already happening. It has a name: *harvest now, decrypt later.*
Last time we explained what a quantum computer *is*. Today: the threat it creates — and what a smart organisation actually does about it.

**[TITLE STING]**

**[THE THREAT — HOST → DIAGRAM]**
Here's the problem in one sentence. [beat]
Almost all the encryption protecting the internet today relies on math that's too hard for normal computers — like factoring enormous numbers.
A powerful quantum computer, one day, could solve that math quickly. And when it can, today's encryption falls.
We call that moment "Q-Day." [beat]
Now — Q-Day probably isn't tomorrow. Expert consensus puts it in the 2030s. So why panic now?
Because of *harvest now, decrypt later.* An attacker doesn't need the quantum computer today. They only need your encrypted data today. They copy it, store it, and wait for Q-Day to unlock it.

**[WHO ACTUALLY GETS HURT — HOST+PANEL]**
So ask yourself one question: how long does *your* data need to stay secret? [beat]
A one-day weather forecast? Who cares if it leaks in 2035.
But a medical record. A life-insurance or pension file that lives for forty years. A signed contract. State secrets. Banking details. [beat]
If your data must stay confidential *past* Q-Day, then harvesting it today already works. The clock already started.
This is why long-life industries — insurance, healthcare, government, finance — are the front line. Their data outlives the encryption protecting it.

**[WHY IT'S URGENT NOW — DIAGRAM, "Mosca's inequality"]**
Here's the piece most people miss. There's a simple rule of thumb for whether you're already late. [beat]
Take three numbers.
X — how many years your data must stay secret.
Y — how many years it'll take you to migrate to new, quantum-safe encryption.
Z — how many years until Q-Day.
The rule: if X plus Y is greater than Z… you're already exposed. [beat]
Think about it. If your data must stay secret for fifteen years, and migrating takes you five, that's twenty years of runway you need — but Q-Day might be ten years out. The math doesn't work. You're late *before you start.*
That's the whole argument for acting now. Not fear — arithmetic.

**[WHAT TO DO — PRACTICAL — HOST+PANEL, numbered]**
Good news: the fix is known, and the first steps are boring, cheap, and effective. Four of them. [beat]
One — *inventory.* You cannot protect what you can't see. Find every system using encryption, and every store of long-life sensitive data. Most organisations have no idea where it all lives. Start there.
Two — *classify by shelf-life.* Tag data by how long it must stay confidential. A fifty-year pension file and a one-week quote are not the same risk. Protect the long-life data first.
Three — *build crypto-agility.* Design systems so you can swap the encryption method without rebuilding everything. This is the single most valuable engineering investment — because the standards will keep evolving.
Four — *migrate the highest-risk data first,* using the new standards. In 2024 the US standards body, NIST, finalised the first quantum-safe encryption algorithms — with names like ML-KEM and ML-DSA. They're real, they're published, and you can start deploying them now, especially on new systems.

**[PRACTICAL vs NOT — HOST+PANEL, split]**
Now — let's be honest about what's realistic, because there's a lot of noise. [beat]
What's practical *today*: inventory and classification. Crypto-agility. Turning on quantum-safe encryption for *new* systems and internet traffic — often in a "hybrid" mode that runs old and new side by side, so you lose nothing if one has a flaw. Prioritising your long-life crown jewels.
What's *not* practical — and don't let a vendor tell you otherwise: ripping out and replacing every system overnight. That's years of work, not a weekend. [beat]
Also not practical for most organisations: exotic hardware like quantum key distribution everywhere. It's real, but it's niche, expensive, and not your first move.
And the worst move of all — *waiting for perfect.* Waiting for the final standard, the final product, the certainty of a date. The data you're harvesting-protected today is the data being stolen today.

**[PLAN B — IF YOU'RE NOT READY — HOST → DIAGRAM]**
But what if you genuinely can't migrate yet? Old systems, tight budget, no capacity. You're not alone. Here's Plan B — reduce the blast radius while you catch up. [beat]
One — *shrink the target.* Delete long-life sensitive data you don't actually need to keep. Data you don't hold can't be harvested.
Two — *shorten retention.* If it doesn't need to live for forty years, don't let it.
Three — *segment and isolate.* Put your crown jewels behind extra walls, off the open internet, so harvesting them is harder in the first place.
Four — *hybrid where you cheaply can.* Even turning on quantum-safe encryption for your most sensitive traffic buys real protection.
Five — *start the inventory anyway.* Even if you can't migrate this year, knowing your exposure is what lets you move fast the moment you can — and it's what your regulator and your board will ask for.
Plan B isn't "do nothing." It's "make yourself a smaller, harder target while you get ready."

**[OUTRO — HOST]**
So — the threat is real, but it's not magic and it's not hopeless. Harvest now, decrypt later means the clock already started for long-life data. The rule is simple arithmetic. And the first steps — see your data, classify it, stay agile, protect the crown jewels first — are things you can start this quarter. [beat]
You don't need to panic. You need to begin.
If this was useful, subscribe — next time we tackle another risk everyone's getting wrong. See you then.

**[OUTRO CARD]**

---

## B. Scene breakdown (production spec → scenes.json)

| # | Time | Shot | On-screen text | Visual / prompt | Narration cue |
|---|------|------|----------------|-----------------|---------------|
| 1 | 0:00–0:28 | HOST | — | Max, lean-in, conspiratorial. A shadowy figure copying glowing locked files in b-roll inset. | "Someone is stealing data they can't read yet…" |
| 2 | 0:28–0:32 | DIAGRAM | Title: *The Quantum Threat* | Title sting, amber/red accent (risk episode). | (music) |
| 3 | 0:32–1:20 | HOST+PANEL | Panel: padlock → cracked; label *Q-Day* | Encryption as a padlock built from a giant number; quantum bolt cracks it. | "Almost all encryption relies on hard math…" |
| 4 | 1:20–1:55 | DIAGRAM | *Harvest Now → store → Decrypt Later* | Timeline: steal (today) → vault → unlock (Q-Day). | "They only need your data today…" |
| 5 | 1:55–2:45 | HOST+PANEL | Panel: data shelf-life bars | Bars: weather (1 day) vs pension/medical/contract (40 yrs) crossing the Q-Day line in red. | "How long must YOUR data stay secret?" |
| 6 | 2:45–3:45 | DIAGRAM | *X + Y > Z → you're exposed* | Mosca's inequality animated: three labelled bars (secrecy, migration, time-to-Q-Day) stacking past the line. | "Take three numbers…" |
| 7 | 3:45–4:50 | HOST+PANEL | Numbered list 1–4 | Icons: magnifier (inventory), tags (classify), swappable-lock (agility), shield+ML-KEM (migrate). | "Four steps. Boring, cheap, effective." |
| 8 | 4:50–5:45 | HOST+PANEL | Split: *Practical* (teal) / *Not practical* (amber) | Left: inventory, hybrid, new systems. Right: rip-and-replace, QKD everywhere, "wait for perfect" crossed out. | "Let's be honest about what's realistic…" |
| 9 | 5:45–6:35 | HOST → DIAGRAM | *Plan B: shrink the blast radius* 1–5 | Icons: delete, clock-down, walls/segment, hybrid, magnifier. Target shrinking. | "What if you can't migrate yet?…" |
| 10 | 6:35–6:50 | HOST → OUTRO | Outro card: subscribe + *Next episode* | Max steady, reassuring; outro card. | "You don't need to panic. You need to begin." |

**Hero SCENE shots for Higgsfield:** #3 padlock-from-a-number cracking, #4 harvest→vault→unlock timeline, #6 Mosca's inequality stack. Rest = Remotion + host lip-sync.

---

## C. Shorts cut-downs

- **Short A — "Hackers are stealing data they can't even read yet" (scene 1 + 4):** the HNDL hook. Pairs with Episode 1's Short C — cross-link them.
- **Short B — "Are you already too late? The 3-number test" (scene 6):** Mosca's inequality as a punchy self-check. Highly shareable with risk/security pros.
- **Short C — "What to actually do about the quantum threat (and what's a waste of money)" (scene 8):** practical vs not — decision-maker catnip.

---

## D. Accuracy notes (verified July 2026)

- **NIST standards:** first three PQC standards finalised **Aug 2024** — ML-KEM (FIPS 203, key exchange), ML-DSA (FIPS 204, signatures), SLH-DSA (FIPS 205, backup signatures); **HQC** selected 2025 as a backup KEM (draft standard to follow). Script uses plain-language names only. ✔
- **Q-Day:** expert consensus ~2030s (commonly 2030 ±a few years; surveys ~50% chance of breaking RSA-2048 within ~15 years). Script says "2030s," which is defensible. ✔
- **HNDL:** intelligence agencies have publicly warned it is already underway; threat is greatest for long-lived data. ✔
- **Mosca's inequality (X + Y > Z):** standard, widely-cited PQC risk heuristic — correctly stated. ✔
- **Hybrid PQC:** running classical + post-quantum together is the mainstream deployment pattern (e.g. in TLS) — correctly characterised. ✔
- **QKD caveat:** correctly framed as niche/expensive and not the first step for most orgs. ✔
- Tone: sober, "begin don't panic" — consistent with a professional-risk voice and YouTube policy. ✔

---

## Sources (for your reference, not on-screen)
- NIST, "First 3 Finalized Post-Quantum Encryption Standards" (Aug 2024)
- NIST FIPS 203 / 204 / 205; HQC selection (2025)
- Expert Q-Day timeline surveys (2030s consensus)
- Public "harvest now, decrypt later" agency warnings
