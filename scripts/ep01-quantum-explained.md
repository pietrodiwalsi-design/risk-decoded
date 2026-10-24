# Episode 01 — "Quantum Computers, Explained (Without the Hype)"

**Version:** v4.4 · 2026-10-24 (accuracy gate closed, sources attached; no script change) · v4.3 · 2026-10-23 (scene 25: "fifty percent grateful" gag cut) · v4.2 · 2026-10-23 (scene 22: Shor's algorithm named, hedged) · v4.1 · 2026-10-23 (scene 10: "small" replaced by "only a modest number of reliable qubits", accuracy fix) · v4 · 2026-10-22 · (v3 + measurement gag changed from blushing to "snap into 0/1") · accuracy rewrite + lighter tone ("medium" humour level). Script approved by Peter 2026-10-22 (runtime ~7:20 accepted; measurement gag changed to a "snap into 0/1"). Accuracy gate closed 2026-10-24; sources in section D go into the YouTube description.
**Runtime target:** ~7:20 (v1 was ~6:20; caveats and jokes add ~60 s — estimate, confirm against the real voice take) · **Host:** Qubit · **Language:** English
**Arc:** What it is → What it is *not* → the 3 principles → how it affects society
**Series note:** Episode 2 picks up the security threat (HNDL / Q-Day) in depth.

---

## 0. What changed vs v1 (for Peter)

| # | Where | Problem in v1 | Fix in v2 |
|---|---|---|---|
| 1 | Cold open + society | "Crack the encryption protecting your bank account, medical records, your entire digital life" and "break the encryption that protects almost everything" overstate it. Quantum computers threaten **public-key** crypto (RSA, elliptic curves). Symmetric encryption (AES) and hashes are only weakened, and larger keys fix that. | Say "public-key encryption", name what it does (set up secure connections, verify identity), and add one line that other encryption is not broken. |
| 2 | Cold open | "Almost everything you've heard is wrong" and "a handful of labs" are hyperbole. | "A lot of what you've heard"; "labs and companies". |
| 3 | Superposition | The spinning coin is secretly heads or tails the whole time (ordinary ignorance). A qubit is not. The v1 wording blurs the very thing that makes it quantum. "Until you look" also invites the "consciousness" myth. | Explicit "imperfect picture" caveat, amplitudes introduced (they can cancel, which sets up interference), "measure" instead of "look". |
| 4 | Entanglement | "Instantly know something about the other" suggests faster-than-light signalling. "Entanglement lets them tackle problems separate bits never could" overstates. | No message travels; you only see the link when you compare results. Entanglement is "a key ingredient", not the whole story. |
| 5 | Entanglement | Named individual (Einstein) vs the no-named-individuals rule. | **Decided by Peter 2026-10-22:** a historical scientist is allowed. Einstein is back, referred to as a physicist, in an accurate role (the quote, and time dilation for the joke). |
| 6 | Society | "Cracks optimisation problems in logistics, energy and finance" is not established. | "May help… still being tested." |
| 7 | Society | "Most put Q-Day in the 2030s" is firmer than the evidence. Expert surveys spread widely. | "Many experts expect… nobody knows exactly." "Quantum-proof" becomes "quantum-resistant". |
| 8 | Tone | v1/v2 were nearly joke-free. | **Medium humour level (Peter's choice):** 8 spoken gags + 2 visual gags, listed in section E. Every gag is outside the factual claims or checked against them. |

Narration length: caveats and gags make it longer; the structure is unchanged.

---

## A. Narration script (voiceover master)

> Written for text-to-speech: short sentences, natural pauses, one idea per line. `[beat]` = short pause. Bracketed notes are for production, not narration.

**[COLD OPEN — QUBIT]**
Right now, in labs and companies around the world, engineers are building a machine that could one day break the encryption that keeps much of the internet secure. [beat]
The kind that protects your logins, your payments, your online banking. [beat]
Don't panic. Well — panic a little. Productively. [beat]
It's called a quantum computer. [beat]
And a lot of what you've heard about it… is wrong.
Let's fix that.

**[TITLE STING]**

**[WHAT IT IS — QUBIT → DIAGRAM]**
So what actually *is* a quantum computer? [beat]
A normal computer — your laptop, your phone — stores everything as bits. Tiny switches, each either a zero or a one. Every photo, every message, every video: just huge strings of zeros and ones.
A quantum computer doesn't use ordinary switches. It uses *qubits* — and qubits follow the strange rules of quantum physics, the physics of the very, very small.
That's the whole idea: a machine that computes using the laws of the quantum world.
It is *not* science fiction, and it is *not* magic. It's physics — put to work.

**[WHAT IT IS NOT — QUBIT+PANEL, "Myth vs Reality"]**
But before the three big ideas, let's kill the myths. Because this is where most people go wrong. [beat]
Myth one: "A quantum computer is just a much faster laptop." [beat] No. It will *not* replace your PC. For email, spreadsheets, video — an ordinary computer is better, and that's not going to change. Besides, many quantum chips need to be kept colder than outer space. Good luck fitting that in your backpack.
Myth two: "It tries every possible answer at the same time and instantly picks the best one." [beat] Also no. If it really tried every answer at once, I'd have picked winning lottery numbers by now. [beat] It's the myth that sounds clever and is just… wrong. It doesn't hand you all the answers. Getting a *useful* answer out is the hard part — and we'll see why in a second.
Myth three: "It's good at everything." No. A quantum computer only wins at a *specific* set of problems. For almost everything else, it's slower and more expensive than what you already own.
And myth four: "It's here." [beat] Not really. Today's machines have only a modest number of reliable qubits, and they're noisy and error-prone. The powerful version is still years away. But — and this matters — the *risk* it creates is already here. Hold that thought.

**[THE 3 PRINCIPLES — DIAGRAM intro]**
So if it's not magic, what makes it special? Three ideas. Just three. [beat] Superposition, entanglement, and interference.

**[PRINCIPLE 1: SUPERPOSITION — SCENE + DIAGRAM]**
One. Superposition. [beat]
Picture a spinning coin. While it's spinning, it's neither heads nor tails — you just can't call it yet. Not heads. Not tails. Slightly nauseous. [beat]
A qubit is a bit like that. Instead of being locked to zero *or* one, it holds a *combination* of zero and one.
But it's an imperfect picture. A real coin is secretly heads or tails the whole time — you just don't know which. A qubit really is a blend. Physicists describe it with numbers called amplitudes — and amplitudes can cancel each other out. Remember that. It matters in a minute.
And no, this does not mean it's in two places, or living in parallel universes. When you *measure* a qubit, you always get a single answer: a zero or a one. No consciousness required — any measurement does it.

**[PRINCIPLE 2: ENTANGLEMENT — SCENE + DIAGRAM]**
Two. Entanglement. [beat]
Now imagine two of those coins, linked. Measure one, and the result tells you what you'll find when you measure the other — even if it's on the far side of the planet.
Einstein called this "spooky action at a distance." And he's the man who told us time slows down when you move fast — so when *he* finds something weird, that's saying something. [beat] But it's real. Experiments have confirmed it again and again, and it earned a Nobel Prize in 2022.
Careful, though: nothing travels between them. No message is sent. You only notice the link when you compare results afterwards. And it's not like a pair of gloves split into two boxes — the gloves were left and right all along. Here, experiments show the outcomes aren't settled in advance.
In a quantum computer, entanglement ties qubits into one shared state that separate bits can't copy. It's a key ingredient — not the whole recipe.

**[PRINCIPLE 3: INTERFERENCE — SCENE + DIAGRAM]**
Three. Interference. And this is the one everyone forgets. [beat]
Think of ripples on a pond. Where two waves meet, they can add up — a bigger wave — or cancel out to nothing.
Those amplitudes I mentioned work the same way. A quantum computer is built so that the *wrong* answers cancel each other out, and the *right* answer adds up and stands out. Think of a committee where everyone politely vetoes everything — except one proposal.
That's the secret. It doesn't magically pick the best answer — it arranges the physics so the best answer is the one you're most likely to measure.
No interference? You'd just get random noise. Interference is how you get a real answer *out*. And it only works for certain kinds of problems — which is why myth three is a myth.

**[HOW IT AFFECTS SOCIETY — QUBIT → DIAGRAM]**
Okay — superposition, entanglement, interference. So what does this actually *change* for the rest of us? Two sides. [beat]
The upside could be big. Quantum computers should be good at simulating nature itself — molecules, materials, chemistry. That could mean new medicines, better batteries, cleaner fertiliser. They may also help with some optimisation problems in logistics, energy, and finance — though that part is still being tested.
But there's a sharp edge. [beat] A quantum algorithm from 1994, called Shor's algorithm, shows that a large enough quantum computer could break the public-key encryption that sets up secure connections and verifies who you're talking to. Your bank. Your messages. Software updates.
It does not break everything. The encryption that scrambles your actual data holds up much better — bigger keys are enough. The weak spot is how we agree on keys in the first place.
The good news: the powerful machine isn't here yet. The bad news: attackers don't need it yet. They can steal encrypted data *today*, store it, and wait to unlock it later. The most patient burglars in history. [beat] That matters most for secrets that must last for years.
Experts call the day this becomes possible "Q-Day." Many expect it in the 2030s or later — nobody knows exactly. Which is why governments and banks are *already* starting to move to new, quantum-resistant encryption.

**[OUTRO — QUBIT]**
So — a quantum computer isn't a faster laptop, it isn't magic, and it isn't here at full strength yet. It's a machine that turns three strange rules of physics into a new kind of power — one that could help, *and* one we have to defend against.
Next episode, we go deep on that threat: "harvest now, decrypt later," Q-Day, and exactly what a smart organisation should be doing about it right now. [beat]
If this made quantum click for you, subscribe — that's the whole point of this channel. See you in the next one.

**[OUTRO CARD]**

---

## B. Scene breakdown (production spec → feeds scenes.json)

| # | Time | Shot | On-screen text | Visual / prompt | Narration cue |
|---|------|------|----------------|-----------------|---------------|
| 1 | 0:00–0:26 | QUBIT | Lower-third: *Public-key encryption* (on that line) | Qubit, concerned→intrigued mood. Dark-teal backdrop. On "panic a little": Qubit worried pose, small sweat drop, then a thumbs-up. | "Right now, in labs and companies…" |
| 2 | 0:26–0:30 | DIAGRAM | Title: *Quantum Computers, Explained* | Title sting, logo, teal accent. | (music) |
| 3 | 0:30–1:09 | QUBIT+PANEL | Panel: bits `0/1` switches vs qubit | Left: laptop turning photos into 0/1 streams. Right: glowing qubit. | "A normal computer stores everything as bits…" |
| 4 | 1:09–1:29 | QUBIT | Lower-third: *It's physics — not magic* | Qubit reassuring, arm open. | "That's the whole idea…" |
| 5 | 1:29–2:50 | QUBIT+PANEL | "Myth vs Reality" ×4 cards | Each myth crossed out in red, reality in teal. Myth 1 card: tiny fridge icon, "colder than outer space". Myth 2 card: lottery ticket with a red cross. | "Let's kill the myths…" |
| 6 | 2:50–3:05 | DIAGRAM | Big text: *3 ideas — Superposition · Entanglement · Interference* | Three glowing nodes appear. | "Three ideas. Just three." |
| 7 | 3:05–4:05 | SCENE→DIAGRAM | Chip: *Superposition* | Spinning coin, motion-blurred. Then split: left, a real coin with a hidden face ("secretly heads or tails"); right, a qubit with a 0/1 blend and the word *amplitudes* (waves with +/− signs). Gag: Qubit spins itself like a coin, gets dizzy, stars circle its head. Measurement beat on "you always get a single answer": Qubit abruptly snaps rigid and straight, a big 0 or 1 slams onto its body, dry mechanical click (original SFX). Repeat 3× with random results (1, 0, 0) to show the outcome is a single value each time. | "Picture a spinning coin…" |
| 8 | 4:05–5:10 | SCENE→DIAGRAM | Chip: *Entanglement* | Two linked coins, glowing thread across a globe; caption *"spooky action at a distance"*. Then a "no message sent" badge on the thread, and a gloves-in-boxes icon crossed out. Gag: a small clock on Einstein's line runs slow. | "Now imagine two of those coins, linked…" |
| 9 | 5:10–6:00 | SCENE→DIAGRAM | Chip: *Interference* | Pond ripples; amplitudes as waves; wrong answers cancel (fade), right answer amplifies (glows). Gag: committee table with many red "veto" stamps and one green "approved". | "Think of ripples on a pond…" |
| 10 | 6:00–7:00 | QUBIT+PANEL | Split panel: *Upside* (teal) / *Risk* (amber) | Left icons: pill, battery, leaf, logistics (tagged *still being tested*). Right: padlock cracking, labelled *public-key*; a second padlock stays intact, labelled *your data (AES)*. | "So what does this change for us?…" |
| 11 | 7:00–7:10 | DIAGRAM | Timeline: *Q-Day: unknown — many expect 2030s or later* | Horizon timeline with a range band (not a single date); "harvest now, decrypt later" tag. | "Experts call it Q-Day…" |
| 12 | 7:10–7:22 | QUBIT → OUTRO | Outro card: subscribe + *Next: The Quantum Threat* | Qubit happy, splits into two identical half-transparent copies as the line is spoken; outro card slides in. | "Subscribe — see you in the next one." |

**Hero SCENE shots (optional Higgsfield hero clips, default off; otherwise Remotion vector):** #7 spinning coin, #8 linked coins across globe, #9 pond-ripple interference. Everything else = Remotion diagrams + the Qubit rig (no lip-sync needed).

---

## C. Shorts cut-downs (auto-generated from long-form)

- **Short A — "A lot of what you've heard about quantum is wrong" (45s):** cold-open hook + the 4 myths (scenes 1, 5). Strong stopper.
- **Short B — "Superposition in 45 seconds" (scene 7):** the spinning-coin explainer including the "imperfect picture" caveat. Standalone. Add "Part 1 of 3 — follow for entanglement."
- **Short C — "Hackers are stealing your data today to crack it later" (scenes 10–11):** the HNDL/Q-Day hook — highest-intent for the IT-risk audience, and a direct funnel into Episode 2. Must keep the "public-key only" line.

Each Short: 9:16 vertical, captions burned in, host framed centre, 3–5s "subscribe / watch the full breakdown" end card.

---

## D. Accuracy gate — claim register

Status: **OK** = consistent with the established physics/standards. **OK + source** = checked against a primary or authoritative source on 2026-10-24; link goes in the description. Rows 1, 6 and the unmarked OK rows rest on established physics, not re-fetched.

| # | Claim in script | Status | Note / source to attach |
|---|---|---|---|
| 1 | Quantum computers threaten public-key crypto (RSA, elliptic-curve), not all encryption | OK / SRC | NIST post-quantum cryptography project; Grover's algorithm only gives a quadratic speed-up against symmetric keys (so AES with large keys remains fine) |
| 2 | Shor's algorithm (1994) shows a large enough quantum computer could break public-key encryption (RSA, elliptic-curve) | OK + source | Named 2026-10-23 at Peter's request: algorithm name used as a technical term, no biography or likeness. Hedged: needs a large, error-corrected machine that does not exist yet. Source: Shor, FOCS 1994 (conference); journal version SIAM J. Comput. 1997, arXiv quant-ph/9508027, DOI 10.1137/S0097539795293172 (arXiv page opened 2026-10-24) |
| 3 | Superposition = weighted combination (amplitudes) of 0 and 1, not "two places" or "parallel universes" | OK | The coin is an analogy; the caveat is spoken in the script |
| 4 | Measurement gives one definite 0 or 1; no consciousness needed | OK | |
| 5 | "Tries all answers at once" is a myth; interference is what makes the right answer likely | OK | Most important correction in the episode |
| 6 | Entanglement: correlations stronger than any classical hidden-variable explanation allows; no signalling | OK | Bell-type experiments, including loophole-free tests (2015). **Known simplification (scene 17, "outcomes aren't settled in advance"):** strictly, Bell tests rule out *local* hidden variables; non-local ones (e.g. Bohm) remain. Peter decided 2026-10-24 to keep the line as is. Do not make stronger claims ("nature is non-local", "definitive proof") in descriptions, Shorts or replies to comments |
| 7 | Nobel Prize in Physics 2022 for entanglement experiments | OK + source | https://www.nobelprize.org/prizes/physics/2022/summary/ (opened 2026-10-24): Aspect, Clauser, Zeilinger, 1/3 each, "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science". Script claims only "confirmed by experiments, Nobel 2022" |
| 8 | Einstein called entanglement "spooky action at a distance" | OK / SRC | Einstein's phrase (German: spukhafte Fernwirkung), from his correspondence in the 1940s (letter to Max Born, 1947). Accepted by Peter 2026-10-24; cite a secondary source in the description if wanted |
| 8b | Einstein is the man who told us time slows down when you move fast | OK | Special relativity, time dilation (moving clocks run slow; confirmed experimentally) |
| 9 | Entanglement is a key ingredient of quantum advantage but not sufficient alone | OK | |
| 10 | Interference: amplitudes add or cancel, enabling the right answer to be amplified | OK | |
| 11 | Many quantum chips run colder than outer space | OK | Superconducting qubits operate at about 10–20 millikelvin; outer space is about 2.7 K. Not true for every platform (trapped-ion, photonic), hence "many" |
| 12 | Quantum computers should be good at simulating molecules and materials | OK | "Should", not "will" |
| 13 | May help with some optimisation problems, still being tested | OK | Evidence for practical advantage is unsettled; wording is intentionally hedged |
| 14 | Today's machines have a modest number of reliable qubits and are noisy and error-prone; powerful fault-tolerant machines are years away | OK | Check for any major announcement before upload. "Small" removed 2026-10-23: today's machines are physically large (cryostats, racks); the limit is the number of reliable qubits, not physical size |
| 15 | Harvest now, decrypt later is a present-day risk | OK | |
| 16 | Q-Day: many expect 2030s or later, nobody knows | OK + source | Global Risk Institute, Quantum Threat Timeline Report 2025 (26 experts): cryptographically relevant quantum computer within 10 years 28–49% ("quite possible"), within 15 years 51–70% ("likely"). https://globalriskinstitute.org/publication/quantum-threat-timeline-report-2025b/ . Description wording: "experts see a real chance within 10–15 years". Spoken line unchanged |
| 17 | Governments and banks are starting to migrate to quantum-resistant encryption | OK + source | NIST finalised its first three standards on 13 Aug 2024 (FIPS 203 ML-KEM, 204 ML-DSA, 205 SLH-DSA): https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards (found via search, page itself not opened) |

**IP check (FR-Q3):** no real logos, no vendors, no employer reference. One historical scientist named (Einstein), approved by Peter on 2026-10-22; no likeness is drawn, only a text mention. Qubit is an original character.

---

## E. Humour register (medium level)

| # | Where | Gag | Factual risk |
|---|---|---|---|
| 1 | Cold open | "Don't panic. Well — panic a little. Productively." | None |
| 2 | Myth 1 | Colder than outer space / backpack | Covered by claim 11 ("many") |
| 3 | Myth 2 | Lottery numbers | None; reinforces the myth correction |
| 4 | Superposition | "Slightly nauseous", dizzy Qubit | None |
| 5 | Entanglement | Einstein / time slows down | Claim 8b |
| 7 | Interference | Committee that vetoes everything but one proposal | None; the analogy supports "wrong answers cancel" |
| 8 | Society | "The most patient burglars in history" | Supports HNDL (claim 15) |
| 10 | Outro | ~~"Fifty percent grateful, fifty percent grateful"~~ cut 2026-10-23 (repeat added no value, not funny) | — |
| V1 | Scene 7 | Qubit snaps into a rigid pose with a big 0 or 1 and a dry click when measured (replaces the blushing idea, which implied "being watched") | Visual only. Supports "always a single answer, no consciousness needed". Show the result as 0 or 1 at random, never as a chosen answer |
| V2 | Scene 25 | ~~Qubit splits in two on "fifty percent"~~ cut with gag 10 | — |

**Decided:** (a) ~7:20 runtime accepted, (b) visual gag V1 changed on 2026-10-22: no blushing; Qubit snaps rigid with a big 0 or 1 and a click, placed at the measurement line in scene 7.
