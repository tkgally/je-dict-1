"""Metadata classification set: 300 entries with their formality/politeness/POS-family labels and semantic tags,
plus injected wrong semantic tags (a tag from an unrelated domain) for a wrong-category test."""
import json, glob, random, sys, re
from pathlib import Path
sys.path.insert(0, "build")
from validate_tags import VALID_SEMANTIC
S = Path(__file__).parent
random.seed(5)
LINK = re.compile(r"⟦([^⟧]*?)→[^⟧]*⟧"); FURI = re.compile(r"\{([^|{}]+)\|([^}]+)\}")
def plain(t): return FURI.sub(r"\1", LINK.sub(r"\1", t or ""))
paths = sorted(glob.glob("entries/*/*.json")); random.shuffle(paths)
FALLBACK = {"general", "descriptive", "expression", "grammatical", "action", "abstract"}
DOMAIN = sorted(t for t in VALID_SEMANTIC if t not in FALLBACK)
items = []
for p in paths:
    if len(items) >= 300: break
    e = json.load(open(p, encoding="utf-8"))
    tags = (e.get("metadata") or {}).get("tags") or {}
    sem = [t for t in tags.get("semantic") or [] if t in VALID_SEMANTIC]
    if not tags.get("formality") or not tags.get("politeness") or not sem:
        continue
    exs = [{"japanese": plain(x.get("japanese")), "english": x.get("english")} for x in (e.get("examples") or [])[:3]]
    real = [t for t in sem if t not in FALLBACK]
    wrong = random.choice([t for t in DOMAIN if t not in sem])
    items.append({"entry": e["id"], "headword": plain(e.get("headword")), "reading": e.get("reading"),
                  "pos": e.get("part_of_speech"), "gloss": e.get("gloss"),
                  "definitions": [{"gloss": d.get("gloss"), "explanation": d.get("explanation")} for d in (e.get("definitions") or [])[:3]],
                  "examples": exs, "notes_head": plain((e.get("notes") or "")[:400]),
                  "formality": tags["formality"], "politeness": tags["politeness"], "semantic": sem,
                  "transitivity": tags.get("transitivity"), "real_tag": random.choice(real) if real else None,
                  "wrong_tag": wrong})
json.dump(items, open(S / "meta_set.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
import collections
print(len(items), collections.Counter(i["formality"] for i in items), collections.Counter(i["politeness"] for i in items), file=sys.stderr)
print(sum(1 for i in items if i["real_tag"]), "with a domain tag", file=sys.stderr)
