#!/usr/bin/env python3
import os
import sys
import re
import json
import csv
import subprocess
import urllib.request
import urllib.error

CLIPS_FILE = "/root/repos/risk-decoded/claude/ep03-clip-list.md"
OUTPUT_DIR = "/root/repos/risk-decoded/public/audio-ep03"
MANIFEST_FILE = os.path.join(OUTPUT_DIR, "manifest.csv")
TOKEN_FILE = "/root/.elevenlabs_token"

VOICES = {
    "qubit": {
        "voice_id": "bTrXJpbeuC5KgriLhQeC",
        "speed": 1.0,
        "stability": 0.50,
        "similarity_boost": 0.75,
        "style": 0.0,
        "words_per_sec": 2.5
    },
    "glitch": {
        "voice_id": "aMSt68OGf4xUZAnLpTU8",
        "speed": 0.95,
        "stability": 0.50,
        "similarity_boost": 0.75,
        "style": 0.0,
        "words_per_sec": 2.3
    }
}

TEST_CLIPS = ["s4-9-qubit", "s1-3-glitch", "s7-2-qubit"]

def get_api_key():
    if "ELEVENLABS_API_KEY" in os.environ:
        return os.environ["ELEVENLABS_API_KEY"]
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE) as f:
            return f.read().strip()
    return ""

def parse_clips():
    with open(CLIPS_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Matches ### s<scene>-<line>-<speaker>.mp3 followed by code block
    pattern = re.compile(r'###\s+(s\d+-\d+-(qubit|glitch))\.mp3\s+```(?:[a-zA-Z]*)\s*\n(.*?)\n```', re.DOTALL)
    clips = {}
    for match in pattern.finditer(content):
        clip_id = match.group(1)
        speaker = match.group(2)
        text = match.group(3).strip()
        clips[clip_id] = {
            "id": clip_id,
            "speaker": speaker,
            "text": text,
            "chars": len(text)
        }
    return clips

def calculate_expected_duration(text, speaker):
    cfg = VOICES[speaker]
    # Breaks sum
    breaks = re.findall(r'<break\s+time=["\']([\d\.]+)s?["\']\s*/>', text)
    break_sum = sum(float(b) for b in breaks)
    # Words without break tags
    clean_text = re.sub(r'<break\s+[^>]*/>', '', text)
    words = len(clean_text.split())
    expected_sec = (words / cfg["words_per_sec"]) + break_sum
    return expected_sec, break_sum

def call_elevenlabs(text, speaker, output_path, api_key):
    cfg = VOICES[speaker]
    voice_id = cfg["voice_id"]
    # ElevenLabs API endpoint - attempt mp3_44100_192, fallback to mp3_44100_128 if tier requires
    base_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": cfg["stability"],
            "similarity_boost": cfg["similarity_boost"],
            "style": cfg["style"],
            "speed": cfg["speed"],
            "use_speaker_boost": True
        }
    }
    
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }
    
    for fmt in ["mp3_44100_192", "mp3_44100_128"]:
        url = f"{base_url}?output_format={fmt}"
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                with open(output_path, "wb") as f:
                    f.write(data)
                return True, None
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8", errors="replace")
            if "output_format_not_allowed" in err and fmt != "mp3_44100_128":
                continue
            return False, f"HTTPError {e.code}: {err}"
        except Exception as e:
            return False, str(e)
    return False, "Failed all output formats"

def run_checks(clip_id, speaker, text, audio_path, whisper_model=None):
    issues = []
    
    # 1. File exists, size > 5KB, decodes ffprobe
    if not os.path.exists(audio_path):
        return False, ["File not found"], {}
    size_kb = os.path.getsize(audio_path) / 1024.0
    if size_kb < 5.0:
        issues.append(f"Size too small: {size_kb:.1f} KB (< 5 KB)")
        
    ffprobe_cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", audio_path
    ]
    try:
        probe_res = subprocess.run(ffprobe_cmd, capture_output=True, text=True, check=True)
        duration = float(probe_res.stdout.strip())
    except Exception as e:
        issues.append(f"ffprobe decode failed: {e}")
        duration = 0.0

    # 2. Duration plausible (within 35%)
    expected_dur, break_sum = calculate_expected_duration(text, speaker)
    dur_diff_pct = abs(duration - expected_dur) / expected_dur if expected_dur > 0 else 1.0
    if dur_diff_pct > 0.35:
        issues.append(f"Duration anomaly: actual={duration:.2f}s, expected={expected_dur:.2f}s (diff {dur_diff_pct*100:.1f}%)")

    # 3. Silence detection: ffmpeg -af silencedetect=noise=-40dB:d=1.0
    sil_cmd = ["ffmpeg", "-i", audio_path, "-af", "silencedetect=noise=-40dB:d=1.0", "-f", "null", "-"]
    sil_res = subprocess.run(sil_cmd, capture_output=True, text=True)
    # Check silence durations in stderr
    silence_starts = [float(x) for x in re.findall(r'silence_start:\s*([\d\.]+)', sil_res.stderr)]
    silence_durations = [float(x) for x in re.findall(r'silence_duration:\s*([\d\.]+)', sil_res.stderr)]
    
    for s_dur in silence_durations:
        if s_dur > (break_sum + 1.0):
            issues.append(f"Unplanned long silence: {s_dur:.2f}s")
            
    # Check leading/trailing silence
    if silence_starts and silence_starts[0] < 0.1 and silence_durations and silence_durations[0] > 0.5:
        issues.append(f"Leading silence too long: {silence_durations[0]:.2f}s")

    # 4. Clipping check: peak below -1 dBFS
    vol_cmd = ["ffmpeg", "-i", audio_path, "-af", "volumedetect", "-f", "null", "-"]
    vol_res = subprocess.run(vol_cmd, capture_output=True, text=True)
    max_vol_match = re.search(r'max_volume:\s*([-\d\.]+)\s*dB', vol_res.stderr)
    max_vol = float(max_vol_match.group(1)) if max_vol_match else 0.0
    if max_vol > -1.0:
        issues.append(f"Clipping risk: max_volume={max_vol} dB (> -1.0 dBFS)")

    # 5. Whisper transcription check
    wer = 0.0
    transcription = ""
    if whisper_model is not None:
        try:
            segments, info = whisper_model.transcribe(audio_path, language="en")
            transcription = " ".join([seg.text for seg in segments]).strip()
            
            # Simple WER calculation
            clean_ref = re.sub(r'<[^>]+>', '', text).lower()
            clean_ref = re.sub(r'[^\w\s]', '', clean_ref)
            clean_hyp = re.sub(r'[^\w\s]', '', transcription.lower())
            
            ref_words = clean_ref.split()
            hyp_words = clean_hyp.split()
            
            # Levenshtein distance on words
            d = [[0] * (len(hyp_words) + 1) for _ in range(len(ref_words) + 1)]
            for i in range(len(ref_words) + 1): d[i][0] = i
            for j in range(len(hyp_words) + 1): d[0][j] = j
            for i in range(1, len(ref_words) + 1):
                for j in range(1, len(hyp_words) + 1):
                    cost = 0 if ref_words[i-1] == hyp_words[j-1] else 1
                    d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + cost)
            
            wer = d[len(ref_words)][len(hyp_words)] / max(1, len(ref_words))
            if wer > 0.08:
                # Flag if WER > 8%
                issues.append(f"Whisper WER={wer*100:.1f}% (> 8%). Transcribed: '{transcription}'")
        except Exception as e:
            issues.append(f"Whisper transcription failed: {e}")

    stats = {
        "duration": duration,
        "expected_duration": expected_dur,
        "max_volume_db": max_vol,
        "transcription": transcription,
        "wer": wer
    }
    
    passed = len(issues) == 0
    return passed, issues, stats

def init_manifest():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp", "clip_id", "speaker", "chars", "duration_sec",
                "max_vol_db", "status", "retries", "cumulative_chars", "issues", "transcription"
            ])

def append_manifest(clip_id, speaker, chars, duration, max_vol, status, retries, cum_chars, issues, transcript):
    import datetime
    now = datetime.datetime.utcnow().isoformat()
    with open(MANIFEST_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            now, clip_id, speaker, chars, f"{duration:.2f}",
            f"{max_vol:.2f}", status, retries, cum_chars, "; ".join(issues), transcript
        ])

def main():
    api_key = get_api_key()
    if not api_key:
        print("ERROR: No ElevenLabs API key found!")
        sys.exit(1)
        
    clips = parse_clips()
    print(f"Loaded {len(clips)} clips from {CLIPS_FILE}")
    
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    target_ids = TEST_CLIPS if mode == "test" else list(clips.keys())
    
    print(f"Mode: {mode}. Target clips: {len(target_ids)}")
    init_manifest()

    print("Loading faster-whisper base.en model for checks...")
    from faster_whisper import WhisperModel
    whisper_model = WhisperModel("base.en", device="cpu", compute_type="int8")
    print("Whisper model loaded successfully.")

    cum_chars = 0
    results = []

    for clip_id in target_ids:
        if clip_id not in clips:
            print(f"WARNING: {clip_id} not in clip list!")
            continue
            
        clip = clips[clip_id]
        speaker = clip["speaker"]
        text = clip["text"]
        chars = clip["chars"]
        audio_path = os.path.join(OUTPUT_DIR, f"{clip_id}.mp3")
        
        # Check if file already exists and passes checks
        if os.path.exists(audio_path):
            passed, issues, stats = run_checks(clip_id, speaker, text, audio_path, whisper_model)
            if passed:
                print(f"\n[{clip_id}] ({speaker}): Already exists and passes checks! Skipping generation to save credits.")
                results.append({
                    "clip_id": clip_id,
                    "speaker": speaker,
                    "status": "already_passed",
                    "duration": stats.get("duration", 0),
                    "expected_duration": stats.get("expected_duration", 0),
                    "chars": chars,
                    "retries": 0,
                    "issues": [],
                    "transcription": stats.get("transcription", "")
                })
                continue

        print(f"\n[{clip_id}] ({speaker}, {chars} chars): generating...")
        
        # Generation attempt 1
        cum_chars += chars
        ok, err = call_elevenlabs(text, speaker, audio_path, api_key)
        retries = 0
        if not ok:
            print(f"  FAILED to generate: {err}")
            append_manifest(clip_id, speaker, chars, 0.0, 0.0, "failed_api", 0, cum_chars, [str(err)], "")
            results.append({"clip_id": clip_id, "status": "failed", "reason": err, "duration": 0.0})
            continue

        # Checks
        passed, issues, stats = run_checks(clip_id, speaker, text, audio_path, whisper_model)
        
        # If failed and retry budget allows: 1 retry max
        if not passed:
            print(f"  Attempt 1 failed checks: {issues}. Performing 1 retry as allowed by budget rules...")
            retries = 1
            cum_chars += chars
            ok_retry, err_retry = call_elevenlabs(text, speaker, audio_path, api_key)
            if ok_retry:
                passed, issues, stats = run_checks(clip_id, speaker, text, audio_path, whisper_model)
                status = "pass_after_retry" if passed else "failed_checks"
            else:
                status = "failed_retry_api"
                issues.append(f"Retry error: {err_retry}")
        else:
            status = "pass"
            
        print(f"  Result: {status} | Duration: {stats.get('duration', 0):.2f}s | Vol: {stats.get('max_volume_db', 0):.1f} dB")
        if issues:
            print(f"  Notes/Issues: {issues}")
            
        append_manifest(
            clip_id, speaker, chars, stats.get("duration", 0), stats.get("max_volume_db", 0),
            status, retries, cum_chars, issues, stats.get("transcription", "")
        )
        
        results.append({
            "clip_id": clip_id,
            "speaker": speaker,
            "status": status,
            "duration": stats.get("duration", 0),
            "expected_duration": stats.get("expected_duration", 0),
            "chars": chars,
            "retries": retries,
            "issues": issues,
            "transcription": stats.get("transcription", "")
        })

    print("\n" + "="*50)
    print("STEP 1 VOICE TEST SUMMARY:")
    print("="*50)
    print(f"Total characters consumed: {cum_chars}")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
