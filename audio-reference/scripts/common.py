"""Shared helpers: dictionary markup parsing, OpenRouter calls, cost logging."""
import json
import os
import re
import threading
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
AUDIO = ROOT / "audio"
COST_LOG = DATA / "cost_log.jsonl"
API = "https://openrouter.ai/api/v1"

TTS_MODELS = {
    "flash": "google/gemini-3.8-flash-tts",
    "lite": "google/gemini-3.8-flash-lite-tts",
}
VOICES = {"female": "Kore", "male": "Charon"}


def api_key():
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        for line in (ROOT / ".env").read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"')
    return key


# ---------------------------------------------------------------- markup parsing
# Link markup:     ⟦display→lemma：entry_id⟧   (occasionally nested / malformed)
# Furigana markup: {base|reading}
LINK_INNER = re.compile(r"⟦([^⟦⟧]*?)→[^⟦⟧]*?⟧")
FURI = re.compile(r"\{([^{}|]+)\|([^{}|]+)\}")
KANJI = re.compile(r"[㐀-鿿豈-﫿々〆ヶ]")


def strip_links(s):
    prev = None
    while prev != s:
        prev, s = s, LINK_INNER.sub(lambda m: m.group(1), s)
    return s


def parse_example(raw):
    """Return dict with plain text, full kana reading, furigana segments, flags."""
    s = strip_links(raw)
    malformed = any(c in s for c in "⟦⟧→")
    segs = [(m.group(1), m.group(2)) for m in FURI.finditer(s)]
    plain = FURI.sub(lambda m: m.group(1), s)
    kana = FURI.sub(lambda m: m.group(2), s)
    # tokens: list of [base, reading-or-None] for building annotated prompts
    tokens, pos = [], 0
    for m in FURI.finditer(s):
        if m.start() > pos:
            tokens.append([s[pos:m.start()], None])
        tokens.append([m.group(1), m.group(2)])
        pos = m.end()
    if pos < len(s):
        tokens.append([s[pos:], None])
    malformed = malformed or "{" in plain or "}" in plain or "|" in plain
    return {
        "plain": plain,
        "kana": kana,
        "segments": segs,
        "tokens": tokens,
        "malformed": malformed,
        "bare_kanji": bool(KANJI.search(kana)),       # kanji without furigana
        "has_digits": bool(re.search(r"[0-9０-９]", plain)),
        "has_latin": bool(re.search(r"[A-Za-zＡ-Ｚａ-ｚ]", plain)),
    }


# ---------------------------------------------------------------- normalization
def kata2hira(s):
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)


def norm_text(s):
    """NFKC, drop punctuation/whitespace/symbols for text comparison."""
    s = unicodedata.normalize("NFKC", s)
    return "".join(c for c in s if unicodedata.category(c)[0] in "LN")


# ---------------------------------------------------------------- cost log
_lock = threading.Lock()


def log_cost(phase, model, cost, **extra):
    rec = {"time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "phase": phase, "model": model, "cost": cost, **extra}
    with _lock, open(COST_LOG, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def generation_cost(gen_id, tries=8):
    """Look up the billed cost of a generation (TTS responses carry no usage)."""
    for i in range(tries):
        r = requests.get(f"{API}/generation", params={"id": gen_id},
                         headers={"Authorization": f"Bearer {api_key()}"}, timeout=30)
        if r.ok:
            d = r.json()["data"]
            return d.get("total_cost", d.get("usage")), d
        time.sleep(2 + 2 * i)
    return None, None


def post(path, payload, timeout=120, tries=4):
    last = None
    for i in range(tries):
        try:
            r = requests.post(f"{API}{path}", json=payload, timeout=timeout,
                              headers={"Authorization": f"Bearer {api_key()}"})
            if r.status_code in (429, 500, 502, 503, 504):
                last = f"{r.status_code} {r.text[:200]}"
                time.sleep(3 * (i + 1))
                continue
            return r
        except requests.RequestException as e:
            last = str(e)
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"request failed after {tries} tries: {last}")
