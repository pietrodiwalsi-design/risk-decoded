# Ep02 clip list (paste list for ElevenLabs)

Source: `claude/ep02-dialogue-v1.md` v1.4 (script of record, decision 30). One block = one clip. File name = `s<scene>-<line>-<speaker>.mp3` (line = position in the scene, both speakers counted, so the playback order is the number order).

**Change log:** 2026-10-25 evening (decision 43): four clips re-recorded with new text: `s1-5-qubit`, `s3-9-glitch`, `s6-1-qubit` (UK sentence), `s10-3-qubit` (next-episode teaser). The distribution of clips over scenes is the one in `claude/ep02-clip-list-v2-delta.md` and `src/Ep02Scenes.ts`; this file lists the texts. Caution: this list is still the v1 set; `s4-3-qubit` and `s4-4-glitch` are obsolete (replaced by `s4-3-glitch`), and the v2 additions (for example `s4-3-glitch`, `s9-4-glitch`, `s9-5-qubit`) are only in the delta file.

**Settings**
| | Qubit | Glitch |
|---|---|---|
| Voice | Peter, `bTrXJpbeuC5KgriLhQeC` | Juniper, `aMSt68OGf4xUZAnLpTU8` |
| Model | `eleven_multilingual_v2` | same |
| Stability / Similarity / Style | 50 / 75 / 0 | 50 / 75 / 0 |
| Speed | 1.0 | 0.95 |

**Rules**
- Paste the text between the backticks, including the `<break .../>` tags. Pauses: 0.6 s after a [beat] or punchline, 0.5 s between list items.
- A pause before the first and after the last word of a clip is not included on purpose: Remotion handles the gaps between clips.
- Output: MP3 44.1 kHz 192 kbps. Save in `public/audio-ep02/` (never in `audio14`). Normalised copies go to `public/audio-ep02-norm/` (`tools/normalise-audio-ep02.py`).
- Optional clip `s6-1-opt-qubit.mp3` (EU Quantum Act line, claim 12f): not used in the video.
- The next-episode teaser is part of `s10-3-qubit.mp3` (no separate clip).
- Re-check on publish day: NIST IR 8547 (s6-1) and Quantum Act (s6-1-opt).
- If a long clip sounds unstable (many breaks), split it at the break tags and keep the same naming with a suffix a, b, c.
- After changing a clip: update its duration in `src/Ep02Scenes.ts` (or `src/Ep02.tsx` for scene 1), update its text in `tools/build-words-ep02.py`, then run `python3 tools/word-times-ep02.py && python3 tools/build-words-ep02.py` in `.venv-ep02`.

# Ep02 clips — QUBIT (25 clips, about 1004 words)

### s1-1-qubit.mp3
```
Somewhere right now, someone is copying data they can't read.
```

### s1-3-qubit.mp3
```
And you keep them anyway?
```

### s1-5-qubit.mp3
```
Hey, personal space! If you look at me, I have to pick a side.
```

### s1-7-qubit.mp3
```
This strategy has a name: "harvest now, decrypt later." Security agencies already describe it as a real risk.
```

### s1-8-qubit.mp3
```
Last time I explained what a quantum computer is. Today: the threat it creates, and what a smart organisation does about it. This is Glitch. She shows you how attackers think. Not how to attack.
```

### s3-1-qubit.mp3
```
First, what actually breaks. <break time="0.6s" /> When you open a secure website, two things happen. Your computer and the site agree on a secret key. A handshake. Then they scramble everything with that key.
```

### s3-3-qubit.mp3
```
Right. The handshake uses public-key encryption, built on maths that is too hard for normal computers. A large enough quantum computer running Shor's algorithm could solve that maths. The scrambling itself, modern AES with a long key, is not broken that way.
```

### s3-5-qubit.mp3
```
Exactly. If the handshake falls later, traffic recorded earlier can be unlocked later.
```

### s3-6-qubit.mp3
```
And "large enough" is shrinking. In 2019, the estimate for breaking RSA-2048 was twenty million noisy qubits. In 2025: under a million. A 2026 preprint, not yet peer-reviewed, claims roughly a hundred thousand, under optimistic assumptions. <break time="0.6s" /> Estimates keep falling. But today's machines don't have anything like that many reliable qubits.
```

### s3-8-qubit.mp3
```
When is Q-Day, the day it works? Nobody knows. In a 2025 survey, 26 experts put the chance within ten years at 28 to 49 percent, and within fifteen years at 51 to 70 percent.
```

### s4-1-qubit.mp3
```
So here's the question that matters. How long must your data stay secret? <break time="0.6s" /> A weather forecast? Who cares if it leaks in ten years.
```

### s4-3-qubit.mp3
```
But health records. Signed contracts. Government files. Financial records. Data that has to stay confidential for decades.
```

### s4-5-qubit.mp3
```
If your data must stay secret past Q-Day, then harvesting it today already works. The clock has started. Long-lived data is the front line, because it outlives the encryption that protects it.
```

### s5-1-qubit.mp3
```
Here's a rule of thumb for whether you're already late. It's called Mosca's inequality. Three numbers. <break time="0.6s" /> X: how many years your data must stay secret. <break time="0.5s" /> Y: how many years it takes you to migrate to quantum-resistant encryption. <break time="0.5s" /> Z: how many years until Q-Day. <break time="0.5s" /> If X plus Y is bigger than Z, you're exposed. <break time="0.5s" /> Say data must stay secret for fifteen years, migration takes five, and Q-Day turns out to be ten years away. Fifteen plus five is twenty. Twenty is bigger than ten. You're late before you start.
```

### s5-3-qubit.mp3
```
Nobody knows Z. That's the point. You plan with a range, not a date. It's not fear. It's arithmetic.
```

### s6-1-qubit.mp3
```
And the tools and deadlines already exist. In August 2024, NIST finalised the first three quantum-resistant standards. In 2025 it picked another algorithm, HQC, as a backup, built on different maths. <break time="0.5s" /> Governments around the world are now publishing roadmaps for the move. Most point at 2035. <break time="0.6s" /> NIST's draft plan: RSA and elliptic-curve schemes deprecated after 2030, disallowed after 2035. <break time="0.5s" /> The UK's national cyber agency advises: know your cryptography and have a plan by 2028, migrate the highest-priority systems by 2031, finish by 2035. <break time="0.5s" /> And in Europe, a joint roadmap for member states: first steps by the end of 2026, high-risk systems by 2030, medium-risk by 2035. It's guidance, not law. And it counts any system whose data must stay secret for ten years or more as high risk.
```

### s6-1-opt-qubit.mp3 (optional, not used in the video)
```
Don't confuse it with the EU Quantum Act, which is still on its way. That one is about the quantum industry, not about your encryption.
```

### s7-1-qubit.mp3
```
The good news: the first steps are boring, cheap, and effective. Four of them. <break time="0.6s" /> One. Inventory. You can't protect what you can't see. Find every system that uses encryption, and every store of long-lived sensitive data. Ask your vendors, too, because encryption hides inside products. EU guidance advises organisations under the NIS2 directive, at a minimum, to build this inventory.
```

### s7-3-qubit.mp3
```
Two. Classify by shelf life. Tag data by how long it must stay confidential. Protect the long-life data first. <break time="0.5s" /> Three. Build crypto-agility. Design systems so you can swap the encryption method without rebuilding everything. The standards will keep evolving. <break time="0.5s" /> Four. Migrate the highest-risk data first, using the new standards. Often in a hybrid mode: old and new side by side, so the keys stay safe as long as at least one of them holds. Parts of the web already do this.
```

### s8-1-qubit.mp3
```
Now, what's realistic? Practical today: inventory and classification. Crypto-agility. Quantum-resistant encryption for new systems. Hybrid mode where you can. The long-life crown jewels first. <break time="0.5s" /> Not practical: replacing every system overnight. That's years of work, not a weekend. <break time="0.5s" /> Also not your first move: quantum key distribution everywhere. It's real, but several European security agencies said in a joint 2024 paper that it suits only niche cases, and they favour the new maths-based standards instead.
```

### s8-3-qubit.mp3
```
Which is why the boring controls around the encryption still matter. And the worst move of all is waiting for perfect. The data being collected today is the data you don't protect today.
```

### s9-1-qubit.mp3
```
What if you can't migrate yet? Old systems, tight budget, no capacity. Plan B: make yourself a smaller, harder target while you catch up. <break time="0.6s" /> One. Shrink the target. Delete long-life sensitive data you don't need.
```

### s9-3-qubit.mp3
```
Two. Shorten retention. If it doesn't need to live for forty years, don't let it. <break time="0.5s" /> Three. Segment and isolate. Put the crown jewels behind extra walls, away from the open internet. <break time="0.5s" /> Four. Use hybrid encryption where it's cheap to do so, starting with your most sensitive traffic. <break time="0.5s" /> Five. Start the inventory anyway. Knowing your exposure is what lets you move fast later, and it's what your board and regulator will ask for. <break time="0.5s" /> Plan B isn't "do nothing."
```

### s10-1-qubit.mp3
```
So. The threat is real, but it isn't magic and it isn't hopeless. For long-lived data, the clock has already started. The rule is arithmetic. And the first steps (see your data, classify it, stay agile, protect the crown jewels first) can start this quarter. <break time="0.6s" /> You don't need to panic. You need to begin.
```

### s10-3-qubit.mp3
```
If this helped, subscribe. Next time: what quantum is actually good for, and what that means for the real world. See you next time.
```


# Ep02 clips — GLITCH (16 clips, about 144 words)

### s1-2-glitch.mp3
```
Guilty. Locked files. Completely useless to me. Today.
```

### s1-4-glitch.mp3
```
Storage is cheap. Patience is cheaper. <break time="0.6s" /> One day somebody builds a big enough quantum computer, and I open everything at once.
```

### s1-6-glitch.mp3
```
Relax. I only collect what I can't open yet.
```

### s1-9-glitch.mp3
```
I prefer "opportunist."
```

### s3-2-glitch.mp3
```
The scrambling is fine. The handshake is the weak spot.
```

### s3-4-glitch.mp3
```
So I don't attack the scrambling. I record it, and wait for the key.
```

### s3-7-glitch.mp3
```
Yet.
```

### s3-9-glitch.mp3
```
Q-Day is payday. Today I'm just stocking up.
```

### s4-2-glitch.mp3
```
Weather. Pass.
```

### s4-4-glitch.mp3
```
Now we're talking.
```

### s5-2-glitch.mp3
```
I love it when defenders do maths. <break time="0.6s" /> Usually afterwards.
```

### s6-2-glitch.mp3
```
Those dates are for you. I'm not on the roadmap.
```

### s7-2-glitch.mp3
```
Can you list every place you use encryption? <break time="0.6s" /> Thought so.
```

### s8-2-glitch.mp3
```
Honestly, perfect cryptography is the part I like least. <break time="0.6s" /> Why hack the firewall when I can phish the vendor's helpdesk?
```

### s9-2-glitch.mp3
```
Data you deleted can't be harvested. That's the one that annoys me.
```

### s10-2-glitch.mp3
```
...Please don't.
```
