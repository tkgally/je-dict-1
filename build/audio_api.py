"""OpenRouter calls and MP3 encoding for the example-audio workflow.

- OpenRouter.tts(model, prompt, voice)      → raw 24 kHz mono 16-bit PCM + generation id
- OpenRouter.ask_audio(model, prompt, mp3)  → (reply text, billed cost)
- OpenRouter.generation_cost(gen_id)        → billed cost of a TTS call (looked up afterwards)
- encode_mp3(pcm, kbps)                     → MP3 bytes (lameenc, or ffmpeg if lameenc is missing)

Every call's cost is added to `OpenRouter.spent` (thread-safe), so callers can
stop at a budget. TTS responses carry no usage; until the generation lookup
answers, a TTS call is charged at `tts_estimate_usd` and corrected afterwards.
"""
import base64
import os
import shutil
import subprocess
import threading
import time

import requests

API = "https://openrouter.ai/api/v1"
SAMPLE_RATE = 24000


class OpenRouter:
    def __init__(self, key=None, tts_estimate_usd=0.0012, timeout=120):
        self.key = key or os.environ.get("OPENROUTER_API_KEY")
        if not self.key:
            raise RuntimeError("OPENROUTER_API_KEY is not set")
        self.timeout = timeout
        self.tts_estimate = tts_estimate_usd
        self.spent = 0.0
        self.calls = 0
        self._lock = threading.Lock()
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {self.key}"

    def _add(self, usd):
        with self._lock:
            self.spent += float(usd or 0.0)
            self.calls += 1

    def post(self, path, payload, tries=4):
        last = None
        for i in range(tries):
            try:
                r = self.session.post(f"{API}{path}", json=payload, timeout=self.timeout)
                if r.status_code in (408, 429, 500, 502, 503, 504):
                    last = f"{r.status_code} {r.text[:200]}"
                    time.sleep(3 * (i + 1))
                    continue
                return r
            except requests.RequestException as e:
                last = repr(e)
                time.sleep(3 * (i + 1))
        raise RuntimeError(f"request failed after {tries} tries: {last}")

    # ------------------------------------------------------------------ TTS
    def tts(self, model, prompt, voice):
        """Return (pcm_bytes, generation_id). Raises on failure."""
        r = self.post("/audio/speech", {"model": model, "input": prompt, "voice": voice,
                                        "response_format": "pcm"})
        if not r.ok or not r.headers.get("content-type", "").startswith("audio"):
            raise RuntimeError(f"TTS {r.status_code}: {r.text[:300]}")
        self._add(self.tts_estimate)
        return r.content, r.headers.get("x-generation-id")

    def generation_cost(self, gen_id, tries=8):
        """Billed cost of a generation; corrects the TTS estimate in `spent`."""
        for i in range(tries):
            try:
                r = self.session.get(f"{API}/generation", params={"id": gen_id}, timeout=30)
                if r.ok:
                    d = r.json()["data"]
                    cost = float(d.get("total_cost") or 0.0)
                    with self._lock:
                        self.spent += cost - self.tts_estimate
                    return cost
            except (requests.RequestException, ValueError, KeyError):
                pass
            time.sleep(2 + 2 * i)
        return None

    # ------------------------------------------------------------------ audio-input chat
    def ask_audio(self, model, prompt, mp3, fmt="mp3"):
        """Send a prompt plus an audio clip; return (text, cost)."""
        b64 = base64.b64encode(mp3).decode()
        r = self.post("/chat/completions", {
            "model": model, "temperature": 0, "reasoning": {"effort": "low"},
            "messages": [{"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "input_audio", "input_audio": {"data": b64, "format": fmt}}]}]})
        try:
            d = r.json()
        except ValueError:
            raise RuntimeError(f"{model} {r.status_code}: {r.text[:200]}")
        if "choices" not in d:
            raise RuntimeError(f"{model}: {str(d)[:300]}")
        cost = float((d.get("usage") or {}).get("cost") or 0.0)
        self._add(cost)
        return (d["choices"][0]["message"].get("content") or "").strip(), cost

    def key_usage(self):
        """Total spend on this key so far (USD), or None."""
        try:
            r = self.session.get(f"{API}/key", timeout=30)
            return float(r.json()["data"]["usage"])
        except Exception:  # noqa: BLE001
            return None


# ---------------------------------------------------------------------- encoding
def encode_mp3(pcm, kbps=48, rate=SAMPLE_RATE):
    """16-bit mono PCM → MP3 at `kbps` (constant bit rate)."""
    try:
        import lameenc
    except ImportError:
        lameenc = None
    if lameenc is not None:
        enc = lameenc.Encoder()
        enc.set_bit_rate(kbps)
        enc.set_in_sample_rate(rate)
        enc.set_channels(1)
        enc.set_quality(2)
        return bytes(enc.encode(pcm) + enc.flush())
    if shutil.which("ffmpeg"):
        return subprocess.run(
            ["ffmpeg", "-v", "error", "-f", "s16le", "-ar", str(rate), "-ac", "1", "-i", "pipe:0",
             "-codec:a", "libmp3lame", "-b:a", f"{kbps}k", "-f", "mp3", "pipe:1"],
            input=pcm, capture_output=True, check=True).stdout
    raise RuntimeError("no MP3 encoder: pip install lameenc (or install ffmpeg)")


def pcm_duration(pcm, rate=SAMPLE_RATE):
    return round(len(pcm) / (2 * rate), 2)
