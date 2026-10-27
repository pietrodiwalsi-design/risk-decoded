# Ep03 clip list (paste list for ElevenLabs)

Source: `claude/ep03-dialogue-v2.md` (script v2, approved by Peter 2026-10-27; script of record for this episode). One block = one clip. File name = `s<scene>-<line>-<speaker>.mp3` (line = position in the scene, both speakers counted, so the playback order is the number order). Scene 2 is the title sting: no voice.

**Settings** (same as Ep02; Glitch voice per `claude/GLITCH-VOICE-BRIEF.md`)
| | Qubit | Glitch |
|---|---|---|
| Voice | Peter, `bTrXJpbeuC5KgriLhQeC` | Juniper, `aMSt68OGf4xUZAnLpTU8` |
| Model | `eleven_multilingual_v2` | same |
| Stability / Similarity / Style | 50 / 75 / 0 | 50 / 75 / 0 |
| Speed | 1.0 | 0.95 |

**Rules**
- Paste the text between the backticks, including the `<break .../>` tags. Pauses: 0.6 s after a [beat] or punchline, 0.5 s between list items.
- No pause before the first or after the last word of a clip: Remotion handles the gaps between clips.
- Output: MP3 44.1 kHz 192 kbps. Save in `public/audio-ep03/` (never in `audio14` or `audio-ep02`). Normalised copies go to `public/audio-ep03-norm/` (adapt `tools/normalise-audio-ep02.py`).
- If a long clip sounds unstable (many breaks), split it at the break tags and keep the same naming with a suffix a, b, c.
- Pronunciation to check when listening: "qubits", "Monte Carlo", "amplitude estimation", "ultracold", "ammonia", "error-corrected". If one sounds off, re-record with a slight rewrite, not a phonetic respelling.
- Facts to re-check on publish day (claims 20, 21, 27): wording of the 2026 advantage claims and the "no industrial use" line in scene 9.
- Scene 11 teaser (AI series) is inside `s11-1-qubit` and `s11-3-qubit`; change only if Peter changes the teaser.
- After recording: add durations to `src/Ep03Scenes.ts`, texts to `tools/build-words-ep03.py`, then run the word-time scripts (clone the Ep02 versions). Not started; build gate applies.

**Longer gaps for Remotion (beats that fell at the end of a clip)**
A [beat] at the end of a line is not baked into the clip (rule above). Give the gap before the next clip about 0.6 s instead of the normal gap in these places:
| After clip | Before clip | Why |
|---|---|---|
| `s5-1-qubit` ("Portfolios.") | `s5-2-glitch` | Setup for her "try every option" line |
| `s11-1-qubit` | `s11-2-glitch` | Beat before the mug line |

**Pause review (2026-10-27)**
- Added: 0.5 s before "One." in `s10-3` (as Ep02 `s7-1`); 0.5 s before "It's prepared" in `s11-1` and before "The tests are real" in `s8-5` (punch / turn).
- Removed: the 0.5 s paragraph break in `s7-2` (it stacked next to a 0.6 s beat, so the explanation would sound chopped); the double pause in `s8-4` (break plus leading ellipsis; the ellipsis is dropped, the 0.6 s break stays).
- Kept on purpose: leading ellipsis only in `s10-4` (same wording and effect as the accepted Ep02 clip).
- Listen-check: `s10-3` has six breaks; if it sounds stiff, split it after "Three. ... press releases." and at "Four." (suffix a, b).

Totals: 57 clips; Qubit 32 clips, about 1212 words; Glitch 25 clips, about 165 words.

# Ep03 clips — QUBIT (32 clips, about 1212 words)

### s1-2-qubit.mp3
```
Who told you that?
```

### s1-4-qubit.mp3
```
Fair question. Last time I explained the threat. Today: the upside. And an honest look at how far away it is.
```

### s1-6-qubit.mp3
```
The short answer: a few specific kinds of problems. Not everything. Let's find out which.
```

### s3-1-qubit.mp3
```
Here's a test for whether a problem is quantum-friendly. Three questions. <break time="0.6s" /> One. Does the problem itself follow quantum rules? Molecules. Materials. Magnets. Nature is quantum, so a quantum computer can imitate it directly. <break time="0.5s" /> Two. Is the input small and the answer small, with a huge tangle in between? Quantum computers are bad at swallowing big piles of data. They shine where a few numbers go in, and a few come out. <break time="0.5s" /> Three. Do ordinary computers already struggle? Because ordinary computers are very good, and they keep getting better.
```

### s3-3-qubit.mp3
```
Close. Most problems fail at least one of the three.
```

### s4-1-qubit.mp3
```
Start with the best case: chemistry and materials. <break time="0.6s" /> To predict how a molecule behaves, you have to track how its electrons interact. Doing that exactly on an ordinary computer gets out of hand fast. The memory you need roughly doubles with every extra particle.
```

### s4-3-qubit.mp3
```
Chemists do, and for many molecules the shortcuts work well. The hard cases are where the electrons interact strongly. A famous one sits at the heart of an enzyme that bacteria use to turn nitrogen from the air into ammonia, a key ingredient of fertiliser. <break time="0.6s" /> Better batteries, better catalysts, better medicines. That's the dream list.
```

### s4-5-qubit.mp3
```
One published estimate for that molecule, in a simplified model: thousands of error-corrected qubits, and billions of operations.
```

### s4-7-qubit.mp3
```
In 2024, an experiment showed the key trick works. Make the error-correcting code bigger, and the errors drop, by about half with each step. A real milestone. But today's devices still slip about once in a thousand operations. Long calculations need error rates that are orders of magnitude lower.
```

### s4-9-qubit.mp3
```
I wouldn't put a date on it. Nobody can. Right idea, hardware not here yet.
```

### s5-1-qubit.mp3
```
Next, the one you hear most: optimisation. Routes. Schedules. Portfolios.
```

### s5-3-qubit.mp3
```
It is. We busted it in the first episode. A quantum computer doesn't try every answer at once. For some search problems there is a proven speedup, but it's a quadratic one. A million steps become a thousand. <break time="0.6s" /> Sounds great.
```

### s5-5-qubit.mp3
```
The catch is overhead. Error-corrected quantum steps are far slower than ordinary ones. One analysis, in 2021, by a quantum research team, found that quadratic speedups are unlikely to beat ordinary computers on early machines. Speedups bigger than quadratic look far more promising.
```

### s5-7-qubit.mp3
```
That's the honest headline. Not very clickable. I know.
```

### s6-1-qubit.mp3
```
Now finance and insurance, because they run on exactly this kind of maths. <break time="0.6s" /> Pricing, risk, and capital models lean on Monte Carlo simulation: run thousands of what-ifs, and look at the spread. A quantum method called amplitude estimation can, on paper, do that with a quadratic speedup.
```

### s6-3-qubit.mp3
```
We did. One well-known estimate, for pricing a complex derivative: around eight thousand error-corrected qubits, tens of millions of sequential steps, and operations roughly a thousand times faster than the rate designers were targeting at the time. So: promising, not proven, and far beyond today's machines.
```

### s6-5-qubit.mp3
```
Probably among the first to try, because a small edge is worth a lot when the answer is worth millions. But "first to try" still comes after the hardware exists. <break time="0.6s" /> And one trap. A quantum computer doesn't fix bad data. If your data is thin, biased, or out of date, you just get a faster wrong answer. And getting big datasets into a quantum computer is hard in itself. It can eat the speedup.
```

### s6-7-qubit.mp3
```
Exactly. For banks and insurers the lasting lesson isn't "buy quantum." It's clean, well-governed data, and a clear list of the few problems that might ever be worth the price. For most organisations, quantum time will be rented in the cloud, not owned.
```

### s7-2-qubit.mp3
```
Not quite. I'm not a faster brain. <break time="0.6s" /> Think of me as a specialist in a classical team. Ordinary computers prepare the problem, run the whole show, and clean up the answer. I do one narrow step in the middle. And AI helps me: it shrinks the problem to fit, picks circuits that cope with noise, and filters errors out of the result.
```

### s7-4-qubit.mp3
```
Mostly, yes. Quantum machine learning is a real research field, but nobody has shown a practical advantage yet, and getting big data in is the bottleneck.
```

### s7-6-qubit.mp3
```
Nothing today points that way. Hybrid is the realistic path: classical and AI doing most of the work, quantum as a specialist.
```

### s8-1-qubit.mp3
```
Now the surprise. The nearest real payoff may not be a computer at all. It's quantum sensing. <break time="0.6s" /> Quantum systems are extremely sensitive. For computing, that's a nightmare: stray heat ruins the calculation. For measuring, sensitivity is the whole point. Atomic clocks, which rely on quantum physics, already keep time for navigation and networks.
```

### s8-3-qubit.mp3
```
A newer example: navigation without satellites. A sensor using ultracold atoms measures acceleration and rotation very precisely. Start from a known position, and it can work out where you are, without any outside signal.
```

### s8-5-qubit.mp3
```
Not so fast. <break time="0.5s" /> The tests are real: a university and a navy team trialled one aboard a research ship in 2023, and again in the Arctic in late 2025. But the developers still call it early. It has to be made tough enough for life at sea.
```

### s9-1-qubit.mp3
```
So where are we, really? <break time="0.6s" /> There are demonstrations where a quantum machine beats every known classical method at a task.
```

### s9-3-qubit.mp3
```
On tasks chosen because they are hard for ordinary computers. Not tasks anyone needs. Some of the newest claims, from 2026, are preprints that haven't been peer reviewed yet, and the community treats them as candidates until others try to beat them. Some are being tested on real problems. But as far as I can find, no quantum application has reached everyday industrial use yet.
```

### s9-5-qubit.mp3
```
Some of it. And some of it is real progress. Error correction really is improving. The skill is telling the two apart.
```

### s10-1-qubit.mp3
```
Here's how. Three questions for any quantum pitch. <break time="0.6s" /> One. Is there a known algorithm with a speedup for this exact problem, or just a hope? Ask to see it. <break time="0.5s" /> Two. Is the speedup big enough to survive error-correction overhead, compared with the best ordinary method? <break time="0.5s" /> Three. Can the data get in, and the answer get out, cheaply?
```

### s10-3-qubit.mp3
```
Then it's marketing. <break time="0.6s" /> Then four steps for you. <break time="0.5s" /> One. Know your hard problems. List the few heavy computations that really hurt: long simulations, big optimisations. Most won't be quantum problems, and that's fine. <break time="0.5s" /> Two. Fix the fuel. Data quality and governance pay off with or without quantum. <break time="0.5s" /> Three. Watch cheaply. Small experiments on rented machines, and follow peer-reviewed results, not press releases. <break time="0.5s" /> Four. Do the one thing that isn't optional. <break time="0.6s" /> The benefits depend on hardware nobody can date. But the threat to today's encryption already has a clock running, because data can be collected today. That was last time's lesson. Plan your move to quantum-resistant encryption now.
```

### s11-1-qubit.mp3
```
So. Quantum is good for a few things: simulating nature, a few kinds of heavy maths, and very sensitive measurement. Not for everything, and not yet for much. The right stance isn't hype, and it isn't "never." <break time="0.5s" /> It's prepared, and sceptical.
```

### s11-3-qubit.mp3
```
If this helped, subscribe. And next time: AI, and what can go wrong with it. Someone new is joining the team.
```

### s11-5-qubit.mp3
```
See you next time.
```


# Ep03 clips — GLITCH (25 clips, about 165 words)

### s1-1-glitch.mp3
```
Quantum computers will cure disease, fix the climate, and optimise your commute. Right?
```

### s1-3-glitch.mp3
```
Every headline I've ever skimmed. <break time="0.6s" /> So. What is it actually good for?
```

### s1-5-glitch.mp3
```
Honest. On a quantum channel. Bold.
```

### s3-2-glitch.mp3
```
Miss one, and it's an expensive fridge.
```

### s4-2-glitch.mp3
```
So use shortcuts.
```

### s4-4-glitch.mp3
```
And the price?
```

### s4-6-glitch.mp3
```
And today?
```

### s4-8-glitch.mp3
```
Right idea, wrong decade.
```

### s5-2-glitch.mp3
```
Try every option at once, pick the best. You told me that was a myth.
```

### s5-4-glitch.mp3
```
Sounds great.
```

### s5-6-glitch.mp3
```
So the headline is: quantum optimisation, maybe, eventually, for some problems.
```

### s6-2-glitch.mp3
```
Quadratic. We covered that.
```

### s6-4-glitch.mp3
```
So the industry with the most money for computers waits like everyone else.
```

### s6-6-glitch.mp3
```
Garbage in, faster garbage out.
```

### s7-1-glitch.mp3
```
One more. Everyone says quantum will make AI smarter.
```

### s7-3-glitch.mp3
```
So AI helps quantum. Not the other way round.
```

### s7-5-glitch.mp3
```
So, no quantum chatbot.
```

### s8-2-glitch.mp3
```
Sensitive. Like me.
```

### s8-4-glitch.mp3
```
No signal. Nothing to jam. <break time="0.6s" /> I'm going to need a new hobby.
```

### s9-2-glitch.mp3
```
So it's here!
```

### s9-4-glitch.mp3
```
Hype with a lab coat.
```

### s10-2-glitch.mp3
```
And if the answer is "trust us"?
```

### s10-4-glitch.mp3
```
...Please don't.
```

### s11-2-glitch.mp3
```
"Prepared and sceptical." Put it on a mug.
```

### s11-4-glitch.mp3
```
A colleague? Finally.
```

