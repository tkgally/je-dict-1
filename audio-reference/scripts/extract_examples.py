"""Parse every example sentence in the dictionary into data/all_examples.jsonl
and build a furigana reading index (data/reading_index.json) used to find
heteronyms (same kanji spelling, different readings)."""
import collections
import glob
import json

from common import DATA, parse_example

entries = sorted(glob.glob(str(DATA / "je-dict-1/entries/*/*.json")))
readings = collections.defaultdict(collections.Counter)
n = 0
with open(DATA / "all_examples.jsonl", "w") as out:
    for f in entries:
        d = json.load(open(f))
        tier = (d.get("metadata") or {}).get("vocabulary_tier")
        for e in d.get("examples") or []:
            p = parse_example(e["japanese"])
            for base, rd in p["segments"]:
                readings[base][rd] += 1
            out.write(json.dumps({
                "id": e["id"], "entry": d["id"], "headword": d["headword"],
                "entry_reading": d.get("reading"), "tier": tier,
                "raw": e["japanese"], "english": e["english"], **p,
            }, ensure_ascii=False) + "\n")
            n += 1

multi = {b: dict(c) for b, c in readings.items() if len(c) > 1}
json.dump(multi, open(DATA / "reading_index.json", "w"), ensure_ascii=False, indent=0)
print(f"{n} examples from {len(entries)} entries; {len(multi)} spellings with >1 reading")
