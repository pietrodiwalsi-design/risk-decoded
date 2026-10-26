# Episode 02 — "The Quantum Threat: Harvest Now, Decrypt Later" — DIALOGUE v1 (Qubit + Glitch)

Status: v1.4, 2026-10-25 (final render). v1.3 (2026-10-24) was approved by Peter; v1.4 changes four lines after his final watch (decision 43, `DECISIONS-2026-10-25-c.md`): scene 1 Qubit line, scene 3 Glitch line, scene 6 UK sentence ("advises"), outro next-episode teaser. Accuracy gate: essentially closed (claims 8, 11, 12, 12b–e checked against primary texts; soft by design: 5, 15). Quantum Act as optional line, not in the video; status to re-check (Peter: it is coming). Supersedes `ep02-quantum-threat.md` (old monologue, host "Max"). Format per decision 25 and CHARACTER-BIBLE v0.5. Glitch is female (decision 34, 2026-10-25): pronouns "she/her".

**Cast:** QUBIT (Ep01 voice, host, explains, delivers the "what to do" beat and closes) · GLITCH (voice "Juniper"; opportunistic attacker's viewpoint, conceptual only).
**Runtime:** about 9:09 as built (decision 41; the original target of about 7:15 was superseded) · **Language:** English · **Series:** Quantum (sequel to Ep01).
**Arc:** the threat (harvest now, decrypt later, Q-Day) → who is exposed → the X + Y > Z rule → deadlines → what to do → practical vs not → Plan B → close.
**Rules applied:** no vendors, logos, employer, or named people in narration; eponym "Shor's algorithm" only as a technical term (decision 14); "Mosca's inequality" is named as a technical term (decision 14 extended, Peter 2026-10-24): no biography, portrait or claims about the person; Glitch explains how attackers think, never how to attack; no fear-bait; every step ends with a "what to do".

---

## A. Script (voice master)

> Short lines, one idea each. `[beat]` = pause. `(note)` = production only. Lines prefixed `[QUBIT]:` / `[GLITCH]:`.

**[1 COLD OPEN — QUBIT + GLITCH]**
[QUBIT]: Somewhere right now, someone is copying data they can't read. [beat]
[GLITCH]: Guilty. Locked files. Completely useless to me. Today.
[QUBIT]: And you keep them anyway?
[GLITCH]: Storage is cheap. Patience is cheaper. [beat] One day somebody builds a big enough quantum computer, and I open everything at once.
(Glitch leans in to look at Qubit.)
[QUBIT]: Hey, personal space! If you look at me, I have to pick a side.
[GLITCH]: Relax. I only collect what I can't open yet.
[QUBIT]: This strategy has a name: "harvest now, decrypt later." Security agencies already describe it as a real risk.
[QUBIT]: Last time I explained what a quantum computer is. Today: the threat it creates, and what a smart organisation does about it. This is Glitch. She shows you how attackers think. Not how to attack.
[GLITCH]: I prefer "opportunist."

**[2 TITLE STING]**

**[3 WHAT BREAKS — QUBIT + GLITCH, DIAGRAM: handshake vs scrambling]**
[QUBIT]: First, what actually breaks. [beat] When you open a secure website, two things happen. Your computer and the site agree on a secret key. A handshake. Then they scramble everything with that key.
[GLITCH]: The scrambling is fine. The handshake is the weak spot.
[QUBIT]: Right. The handshake uses public-key encryption, built on maths that is too hard for normal computers. A large enough quantum computer running Shor's algorithm could solve that maths. The scrambling itself, modern AES with a long key, is not broken that way.
[GLITCH]: So I don't attack the scrambling. I record it, and wait for the key.
[QUBIT]: Exactly. If the handshake falls later, traffic recorded earlier can be unlocked later.
[QUBIT]: And "large enough" is shrinking. In 2019, the estimate for breaking RSA-2048 was twenty million noisy qubits. In 2025: under a million. A 2026 preprint, not yet peer-reviewed, claims roughly a hundred thousand, under optimistic assumptions. [beat] Estimates keep falling. But today's machines don't have anything like that many reliable qubits.
[GLITCH]: Yet.
[QUBIT]: When is Q-Day, the day it works? Nobody knows. In a 2025 survey, 26 experts put the chance within ten years at 28 to 49 percent, and within fifteen years at 51 to 70 percent. (on-screen)
[GLITCH]: Q-Day is payday. Today I'm just stocking up. (on-screen bubble: "Q-Day is payday. Today: stocking up.")

**[4 WHO IS EXPOSED — QUBIT + GLITCH, PANEL: shelf-life bars]**
[QUBIT]: So here's the question that matters. How long must your data stay secret? [beat]
A weather forecast? Who cares if it leaks in ten years.
[GLITCH]: Weather. Pass.
[QUBIT]: But health records. Signed contracts. Government files. Financial records. Data that has to stay confidential for decades.
[GLITCH]: Now we're talking.
[QUBIT]: If your data must stay secret past Q-Day, then harvesting it today already works. The clock has started. Long-lived data is the front line, because it outlives the encryption that protects it.

**[5 THE RULE — QUBIT, DIAGRAM: X + Y > Z]**
[QUBIT]: Here's a rule of thumb for whether you're already late. It's called Mosca's inequality. Three numbers. [beat]
X: how many years your data must stay secret.
Y: how many years it takes you to migrate to quantum-resistant encryption.
Z: how many years until Q-Day.
If X plus Y is bigger than Z, you're exposed.
(example, on-screen "illustrative numbers")
Say data must stay secret for fifteen years, migration takes five, and Q-Day turns out to be ten years away. Fifteen plus five is twenty. Twenty is bigger than ten. You're late before you start.
[GLITCH]: I love it when defenders do maths. Usually afterwards.
[QUBIT]: Nobody knows Z. That's the point. You plan with a range, not a date. It's not fear. It's arithmetic.

**[6 THE CLOCK IS ALREADY WRITTEN — QUBIT, DIAGRAM: timeline]**
[QUBIT]: And the tools and deadlines already exist. In August 2024, NIST finalised the first three quantum-resistant standards. In 2025 it picked another algorithm, HQC, as a backup, built on different maths.
Governments around the world are now publishing roadmaps for the move. Most point at 2035. [beat]
NIST's draft plan: RSA and elliptic-curve schemes deprecated after 2030, disallowed after 2035.
The UK's national cyber agency advises: know your cryptography and have a plan by 2028, migrate the highest-priority systems by 2031, finish by 2035.
And in Europe, a joint roadmap for member states: first steps by the end of 2026, high-risk systems by 2030, medium-risk by 2035. It's guidance, not law. And it counts any system whose data must stay secret for ten years or more as high risk.
Don't confuse it with the EU Quantum Act, which is still on its way. That one is about the quantum industry, not about your encryption. (optional line; claim 12f; not in the video)
[GLITCH]: Those dates are for you. I'm not on the roadmap.

**[7 WHAT TO DO — QUBIT, PANEL: numbered 1–4]**
[QUBIT]: The good news: the first steps are boring, cheap, and effective. Four of them. [beat]
One. Inventory. You can't protect what you can't see. Find every system that uses encryption, and every store of long-lived sensitive data. Ask your vendors, too, because encryption hides inside products. EU guidance advises organisations under the NIS2 directive, at a minimum, to build this inventory.
[GLITCH]: Can you list every place you use encryption? [beat] Thought so.
[QUBIT]: Two. Classify by shelf life. Tag data by how long it must stay confidential. Protect the long-life data first.
Three. Build crypto-agility. Design systems so you can swap the encryption method without rebuilding everything. The standards will keep evolving.
Four. Migrate the highest-risk data first, using the new standards. Often in a hybrid mode: old and new side by side, so the keys stay safe as long as at least one of them holds. Parts of the web already do this.

**[8 PRACTICAL VS NOT — QUBIT + GLITCH, PANEL: split]**
[QUBIT]: Now, what's realistic? Practical today: inventory and classification. Crypto-agility. Quantum-resistant encryption for new systems. Hybrid mode where you can. The long-life crown jewels first.
Not practical: replacing every system overnight. That's years of work, not a weekend.
Also not your first move: quantum key distribution everywhere. It's real, but several European security agencies said in a joint 2024 paper that it suits only niche cases, and they favour the new maths-based standards instead.
[GLITCH]: Honestly, perfect cryptography is the part I like least. Why hack the firewall when I can phish the vendor's helpdesk?
[QUBIT]: Which is why the boring controls around the encryption still matter. And the worst move of all is waiting for perfect. The data being collected today is the data you don't protect today.

**[9 PLAN B — QUBIT + GLITCH, DIAGRAM: shrinking target 1–5]**
[QUBIT]: What if you can't migrate yet? Old systems, tight budget, no capacity. Plan B: make yourself a smaller, harder target while you catch up. [beat]
One. Shrink the target. Delete long-life sensitive data you don't need.
[GLITCH]: Data you deleted can't be harvested. That's the one that annoys me.
[QUBIT]: Two. Shorten retention. If it doesn't need to live for forty years, don't let it.
Three. Segment and isolate. Put the crown jewels behind extra walls, away from the open internet.
Four. Use hybrid encryption where it's cheap to do so, starting with your most sensitive traffic.
Five. Start the inventory anyway. Knowing your exposure is what lets you move fast later, and it's what your board and regulator will ask for.
Plan B isn't "do nothing."

**[10 OUTRO — QUBIT + GLITCH]**
[QUBIT]: So. The threat is real, but it isn't magic and it isn't hopeless. For long-lived data, the clock has already started. The rule is arithmetic. And the first steps (see your data, classify it, stay agile, protect the crown jewels first) can start this quarter. [beat]
You don't need to panic. You need to begin.
[GLITCH]: ...Please don't.
[QUBIT]: If this helped, subscribe. Next time: what quantum is actually good for, and what that means for the real world. See you next time.

**[OUTRO CARD]** "RISKDECODED / Next time / What quantum is actually good for" (right half free for YouTube end-screen elements).

---

## B. Scene plan (feeds scenes.json after approval)

| # | Section | Shot | characters_on_screen | Visual idea |
|---|---|---|---|---|
| 1 | Cold open | DIALOGUE | qubit, glitch | Glitch with a vault of padlocked files; leans toward Qubit; Qubit pulses/startles |
| 2 | Title | DIAGRAM | — | Title sting, amber accent (risk episode) |
| 3 | What breaks | DIALOGUE+DIAGRAM | qubit, glitch | Handshake (two keys meet) vs scrambling; recorded-traffic vault; estimate card; survey ranges as text |
| 4 | Who is exposed | DIALOGUE+PANEL | qubit, glitch | Shelf-life bars crossing a red Q-Day line |
| 5 | The rule | DIAGRAM | qubit | X, Y, Z bars stacking past the line; "illustrative numbers" |
| 6 | Dates | DIAGRAM | qubit, glitch (small) | Timeline 2024 / 2025 / 2030 / 2035 with source tags |
| 7 | What to do | PANEL | qubit, glitch (reacting) | Icons: magnifier, tags, swappable lock, shield |
| 8 | Practical vs not | PANEL | qubit, glitch | Split teal/amber; QKD card with "niche" tag |
| 9 | Plan B | DIAGRAM | qubit, glitch | Target shrinking; delete icon |
| 10 | Outro | OUTRO | qubit, glitch | Takeaway list, empty right side for YouTube elements; then end card |

---

## C. Humour register

| # | Where | Gag | Factual risk |
|---|---|---|---|
| 1 | Cold open | "Storage is cheap. Patience is cheaper." | None |
| 2 | Cold open | Qubit, when Glitch leans in: "Hey, personal space! If you look at me, I have to pick a side." (replaced "Don't measure me!" in v1.4, decision 43) | None; consistent with Ep01 (measuring gives one answer) |
| 3 | Cold open | "I prefer 'opportunist.'" | None |
| 4 | Scene 3 | "Yet." | None; consistent with the hedge (nobody knows when) |
| 5 | Scene 3 | "Q-Day is payday. Today I'm just stocking up." (replaced "I don't need Q-Day today…" in v1.4) | None; restates harvest now, decrypt later |
| 6 | Scene 5 | "I love it when defenders do maths. Usually afterwards." | None |
| 7 | Scene 6 | "I'm not on the roadmap." | None |
| 8 | Scene 7 | "Can you list every place you use encryption? Thought so." | A question, not a claim |
| 9 | Scene 8 | Glitch catchphrase (pre-cleared); Qubit turns it into "boring controls still matter" | Conceptual only, no technique |
| 10 | Scene 9 | "Data you deleted can't be harvested. That's the one that annoys me." | None |
| 11 | Outro | "...Please don't." | None |

---

## D. Claim register (accuracy gate)

Status: OK = primary source opened; SOFT = hedged wording or secondary source; OPEN = needs a decision or one more check before sign-off. The four lines changed in v1.4 add no new factual claim; claim 12b is unchanged (only "advises" was added to the lead-in).

| # | Claim in script | Status | Source / note |
|---|---|---|---|
| 1 | Harvest now, decrypt later is a risk described by security agencies | OK | CISA/NSA/NIST quantum-readiness factsheet, 17 Aug 2023: "cyber threat actors could be targeting data today that would still require protection in the future"; "harvest now, decrypt later". https://www.nccoe.nist.gov/sites/default/files/2023-08/quantum-readiness-fact-sheet.pdf · NIST IR 8547 (draft), section 1, 3.1.3 |
| 2 | Public-key handshake is the weak spot; AES with long key is not broken by quantum computers | OK | NIST PQC FAQ: "AES 192 and AES 256 will still be safe for a very long time"; NIST IR 8547 §3.1.3 (session keys). https://csrc.nist.gov/projects/post-quantum-cryptography/faqs |
| 3 | Shor's algorithm could solve the maths behind RSA | OK | Shor, arXiv quant-ph/9508027 (already cleared in Ep01 claim register) |
| 4 | Estimates for breaking RSA-2048 keep falling: 2019 about 20 million noisy qubits (8 hours); 2025 under a million (under a week); a 2026 preprint claims roughly 100,000 under optimistic assumptions | OK (hedged) | 2019 and 2025: Gidney, arXiv 2505.15917 abstract (opened). 2026: arXiv 2602.11457, posted 12 Feb 2026 (eight researchers at a Sydney start-up that designs architectures, not hardware); about 98,000 physical qubits for a one-month run, revised to about 94,000 in May 2026. Caveats (read from two secondary write-ups, preprint itself not opened): **not peer-reviewed**, simulation only, assumes 0.1% gate error and non-local connectivity, real-time decoding out of scope, hardware 100–1,000x short. Script says "claims", "not yet peer-reviewed", "under optimistic assumptions", and names no company or person. https://arxiv.org/abs/2505.15917 · https://scottaaronson.blog/?p=9564 · https://postquantum.com/post-quantum/pinnacle-architecture-break-rsa-2048-critical/ |
| 5 | Today's machines don't have anything like that many reliable qubits | SOFT | Same wording class as Ep01 scene 10 ("only a modest number of reliable qubits"). No new source opened in this pass. |
| 6 | 26 experts, 28–49% within 10 years, 51–70% within 15 years | OK | Global Risk Institute Quantum Threat Timeline Report 2025 (already in Ep01 package). https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/ Note: the survey (2025) predates the 2026 preprints on lower qubit counts; script says "2025 survey". |
| 7 | Data with a long shelf life is the front line; harvesting works if confidentiality must outlast Q-Day | OK | Logic follows claim 1; factsheet step "estimate how long data must stay protected". |
| 8 | The X + Y > Z rule is known as Mosca's inequality | OK | Named as an eponymous technical term (decision 28). Mosca, "Cybersecurity in an era with quantum computers: will we be ready?", IACR ePrint 2015/1075 (full text opened 2026-10-24): x = years data must stay secure, y = years to migrate, z = years until a large quantum computer; "If x + y > z, we have a serious problem today [Mos13]", citing his earlier 2013 work. The paper presents it as a simple decision rule, not a proven theorem, so the script says "rule of thumb" and never "theorem". Example numbers labelled illustrative. https://eprint.iacr.org/2015/1075 The EU roadmap (official text, 11 Jun 2025, section 5) also cites "Mosca's theorem" as the basis of its risk model, which supports using the name. |
| 9 | NIST finalised the first three standards in August 2024 | OK | NIST news 13 Aug 2024 (FIPS 203/204/205), already in Ep01 package |
| 10 | 2025: NIST selected HQC as a backup built on different maths | OK | NIST news, 11 Mar 2025: "a backup standard that is based on a different math approach than ML-KEM". NIST planned a draft about a year later and a final standard in 2027; script makes no claim about either. https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption. Script says "another algorithm" (NIST itself calls it the fifth algorithm; a count is avoided). |
| 11 | NIST's draft plan: RSA/elliptic-curve public-key schemes deprecated after 2030 (112-bit strength), disallowed after 2035 | OK (draft) | NIST IR 8547 initial public draft, 12 Nov 2024, Tables 3–4 (full PDF opened): 112-bit "Deprecated after 2030", "Disallowed after 2035"; 128-bit and above "Disallowed after 2035". Status: NIST's own project page (https://csrc.nist.gov/pubs/ir/8547/ipd) still showed only the initial public draft on 2026-10-25 (comment period closed 10 Jan 2025; no link to a final version; the 2030/2035 wording is in the PDF, not on the page); a dated third-party article (Aug 2026) says it is still a public draft; the EU roadmap FAQ of 15 Apr 2026 (official, read in full) refers to it as the "initial public draft". Script keeps the word "draft". It is guidance on NIST's expected approach, not law. |
| 12 | EU coordinated roadmap (member states): by 31 Dec 2026 all member states complete first steps and set initial national roadmaps; by 31 Dec 2030 high-risk use cases transitioned; by 31 Dec 2035 medium-risk transitioned, low-risk "as much as feasible". Guidance, not law | OK | Official text read in full from the Commission download (document 117507 on the Commission page): "A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography, Part 1, Version 1.1, EU PQC Workstream, 11.06.2025", section 4.1 (timeline box) and 4.1 ("shall not be used stand-alone after the end of 2030 [high-risk] … 2035 [medium-risk]"). Describes itself as the first deliverable of the NIS CG PQC work stream, "a first high-level paper aimed at the Member States"; follows Commission Recommendation of 11 Apr 2024. https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography |
| 12c | EU roadmap risk levels: data that must stay confidential for at least 10 years, where an attack after 10+ years would still have significant impact, is "high" quantum risk | OK | Same document, section 5. Ties directly to the x in the x + y > z rule. |
| 12d | EU guidance: at a minimum, entities in scope of NIS2 should build a cryptographic inventory and dependency map, involve the supply chain, and do a quantum risk analysis; all organisations encouraged | OK | EU roadmap FAQ, 15 Apr 2026, question 7.4 (official file, read). Script says "advises". |
| 12e | Governments worldwide are publishing roadmaps; most point at 2035 (EU, US draft, UK, Canada); Australia earlier (2030) | OK | EU roadmap FAQ question 2.6 summarises ASD (2030), NIST IR 8547 draft (2035), UK NCSC (2035), Canada Cyber Centre (2035). Second-hand summary; the UK page (claim 12b) was opened separately. Script says "most point at 2035", names no country except UK/EU. |
| 12f | An EU Quantum Act is expected; it targets the quantum industry (research investment, industrial capacity, supply-chain security), not users' encryption | OK (status to re-check) | Commission news, 2 Jul 2025: the Quantum Europe Strategy "will be followed by a quantum act proposal, expected in 2026"; European Parliament legislative-train page: work programme "to be released during the second quarter of 2026"; three focus areas: coordinated research and innovation investment, industrial capacity, "security and resilience of quantum supply chains". Neither page mentions post-quantum cryptography. No adopted proposal seen in these sources; Peter confirms it is coming. **Re-check the status on publish day**; the line is not in the video. https://commission.europa.eu/news-and-media/news/eus-plan-become-global-leader-quantum-2030-2025-07-02_en · https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-quantum-act |
| 12b | UK national cyber agency: by 2028 complete discovery and an initial plan; by 2031 complete highest-priority migration; by 2035 complete migration | OK | NCSC "Timelines for migration to post-quantum cryptography", 20 Mar 2025, v1.0 (opened). https://www.ncsc.gov.uk/guidance/pqc-migration-timelines . Applies to "all organisations" as key dates; primarily aimed at large organisations and CNI. Spoken as "advises" (v1.4). |
| 13 | Inventory, classify by shelf life, ask vendors, prioritise long-term-confidentiality systems | OK | Same CISA/NSA/NIST factsheet, listed steps |
| 14 | Hybrid mode: keys stay secure if at least one component holds | OK | NIST PQC FAQ: "derived keys remain secure if at least one of the component schemes is secure" |
| 15 | "Parts of the web already do this" (hybrid key agreement) | SOFT | Cloudflare Radar post-quantum page names X25519MLKEM768 and charts the share over time; no figure retrieved, so no number is spoken. |
| 16 | Several European agencies, joint 2024 paper: QKD suits only niche cases, they favour post-quantum cryptography | OK | ANSSI/BSI/NLNCSA/Swedish authority, 25 Jan 2024. https://cyber.gouv.fr/en/publications/jointly-led-international-publications/position-paper-on-quantum-key-distribution/ |
| 17 | Phishing a helpdesk as an easier route (Glitch catchphrase) | OK (pre-cleared) | CHARACTER-BIBLE §3; conceptual, no technique |
| 18 | Plan B steps (delete, shorten retention, segment, hybrid, inventory) | Advice | Risk-reduction advice, not factual claims; deleting and shorter retention are consistent with data-minimisation practice. |
| 19 | Qubit: "If you look at me, I have to pick a side" (measurement gives one definite result) | OK (analogy) | Consistent with the Ep01 explanation of measurement (scene 7 of Ep01: always a single answer). Gag, not a technical claim. |
| 20 | Outro teaser: "Next time: what quantum is actually good for, and what that means for the real world" | N/A | Announcement only; makes no factual claim and names no title. |

---

## E. Open points for Peter

1. **Glitch voice:** licence per voice (decision 22) still to be documented (plan, ToS date, terms).
2. **Quantum Act:** optional line, not in the video; re-check its status on publish day.
3. **Claim 11:** IR 8547 still an initial public draft in every source seen (NIST page on 2026-10-25). Re-check on publish day.
4. **Ep03 title:** the outro teaser is generic on purpose; add a next-episode line to the description once title and link exist.
5. **Old `ep02-quantum-threat.md`** (monologue, host Max) is superseded by this dialogue.
