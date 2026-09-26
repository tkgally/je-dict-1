#!/usr/bin/env python3
"""Set each example's has_audio from the audio manifest.

has_audio is true exactly when audio/manifest/ holds a valid recording of the
example: one made from its current text and furigana (audio_manifest.valid_record).
An edited example therefore goes back to false until the audio mode re-records it.
The field is derived data, like the indexes: metadata.modified is not touched, and
only files whose flags change are rewritten.

Runs in `audio_pipeline.py publish` (the entries just recorded) and in
`make index` (every entry, which catches examples edited since they were recorded).

    python3 build/sync_audio_flags.py              # every entry
    python3 build/sync_audio_flags.py --ids 00426,00006
    python3 build/sync_audio_flags.py --check      # exit 1 if any flag is wrong; change nothing
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audio_manifest import valid_record  # noqa: E402
from normalize_common import write_entry  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "entries"


def sync_entry(entry):
    """Set has_audio on the entry's examples in place; return how many changed.
    An example without the field gets it only when it has a recording."""
    changed = 0
    for ex in entry.get("examples") or []:
        want = valid_record(ex) is not None
        if ex.get("has_audio", False) != want or (want and "has_audio" not in ex):
            ex["has_audio"] = want
            changed += 1
    return changed


def entry_paths(ids=None):
    if not ids:
        return sorted(ENTRIES.glob("*/*.json"))
    out = []
    for i in ids:
        num = f"{int(str(i)[:5]):05d}"
        out += sorted(ENTRIES.glob(f"{int(num) // 500 * 500:05d}/{num}_*.json"))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ids", help="comma-separated entry IDs (default: every entry)")
    ap.add_argument("--check", action="store_true", help="report wrong flags, change nothing")
    args = ap.parse_args()
    ids = [x.strip() for x in args.ids.split(",") if x.strip()] if args.ids else None
    files = examples = 0
    now_true = 0
    for path in entry_paths(ids):
        raw = path.read_text(encoding="utf-8")
        entry = json.loads(raw)
        n = sync_entry(entry)
        now_true += sum(1 for ex in entry.get("examples") or [] if ex.get("has_audio"))
        if n:
            files += 1
            examples += n
            if args.check:
                print(f"  {path.relative_to(ROOT)}: {n} has_audio flag(s) out of date")
            else:
                write_entry(path, entry, raw)
    verb = "out of date" if args.check else "updated"
    print(f"has_audio: {examples} flag(s) in {files} file(s) {verb}; "
          f"{now_true} example(s) have a valid recording")
    return 1 if args.check and files else 0


if __name__ == "__main__":
    sys.exit(main())
