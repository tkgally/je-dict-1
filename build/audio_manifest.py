"""Read side of the example-audio manifest, for the site build.

    recording_url(example) → URL of the example's MP3, or None
    latest_recording_at(entry) → when its newest valid recording was published

An example has a valid recording when audio/manifest/<range>.jsonl holds a
line for its id whose "h" equals the first 16 hex digits of
audio_text.text_hash(example["japanese"]). A changed example (new text or new
furigana) therefore falls back to browser speech until it is re-recorded.
The URL is the store's base_url (audio/config.json) plus the file path, so the
audio can move to another host by editing the config alone.
"""
import json
from pathlib import Path

from audio_text import text_hash

ROOT = Path(__file__).resolve().parent.parent
AUDIO = ROOT / "audio"
HASH_LEN = 16

_CACHE = None


def _load():
    global _CACHE
    if _CACHE is not None:
        return _CACHE
    stores = {}
    try:
        cfg = json.loads((AUDIO / "config.json").read_text(encoding="utf-8"))
        stores = {s["id"]: s["base_url"] for s in cfg.get("stores", [])}
    except (OSError, ValueError, KeyError):
        pass
    records = {}
    for f in sorted((AUDIO / "manifest").glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    r = json.loads(line)
                    records[r["ex"]] = r
                except (ValueError, KeyError):
                    continue
    _CACHE = (stores, records)
    return _CACHE


def reset_cache():
    global _CACHE
    _CACHE = None


def valid_record(example):
    """The manifest record of a valid recording for this example (a dict with id
    and japanese), or None when there is none or the text changed since."""
    stores, records = _load()
    r = records.get(example.get("id"))
    if not r or r.get("s") not in stores:
        return None
    if r.get("h") != text_hash(example.get("japanese", ""))[:HASH_LEN]:
        return None
    return r


def recording_url(example):
    """URL of a valid recording for this example, or None."""
    r = valid_record(example)
    return _load()[0][r["s"]] + r["f"] if r else None


def latest_recording_at(entry):
    """When the newest valid recording of any of this entry's examples was
    published (the record's "at", an ISO UTC timestamp), or None."""
    times = [r.get("at", "") for r in (valid_record(ex) for ex in entry.get("examples") or [])
             if r and r.get("at")]
    return max(times) if times else None


def stats():
    """(records in the manifest, stores configured)."""
    stores, records = _load()
    return len(records), len(stores)
