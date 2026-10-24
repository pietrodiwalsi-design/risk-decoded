#!/usr/bin/env python3
"""Exact word timestamps for the Ep01 voice clips (local Whisper, no API key, nothing leaves the Mac).
Usage (from the project folder):
  python3 -m venv .venv-asr && source .venv-asr/bin/activate
  pip install faster-whisper
  python3 tools/word-times.py
Output: out/word-times.json  ->  {"1":[{"w":"Hello","s":0.12,"e":0.40}, ...], ...}
"""
import glob, json, os, re
from faster_whisper import WhisperModel

AUDIO = "public/audio"
OUT = "out/word-times.json"
model = WhisperModel("small.en", device="cpu", compute_type="int8")

res = {}
for f in sorted(glob.glob(f"{AUDIO}/s*.mp3"), key=lambda p: int(re.search(r"s(\d+)\.mp3$", p).group(1)) if re.search(r"s(\d+)\.mp3$", p) else 0):
    m = re.search(r"/s(\d+)\.mp3$", f)
    if not m:            # skips s25-with-joke.mp3 and other backups
        continue
    n = m.group(1)
    segs, _ = model.transcribe(f, language="en", word_timestamps=True, vad_filter=False, beam_size=5, condition_on_previous_text=False)
    words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)} for s in segs for w in s.words]
    res[n] = words
    print(f"s{n}: {len(words)} words, ends {words[-1]['e'] if words else 0}s")
os.makedirs("out", exist_ok=True)
json.dump(res, open(OUT, "w"), indent=1)
print("written", OUT)
