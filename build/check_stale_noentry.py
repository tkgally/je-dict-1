#!/usr/bin/env python3
"""Detect `noentry` inline links whose word now has an entry.

Read-only review-queue generator for the Routine's systemic-fix mode
(Cleanup Backlog P35, formerly Tooling 19). Never modifies entries.

A polishing session that meets a word with no entry writes
`⟦{水草|みずくさ}→水草：noentry⟧`. The marker is correct when written. A later
`new-entries` run creates 水草, and nothing sweeps back — so the reader sees
plain text where a working link now exists. 85% of the resolving markers point
at entries in bands 26000+, i.e. the population grows with every new-entries
run; this detector is the standing measurement of that leak.

Classes (the stratification measured by the 2026-08-01/02 wiki harvests):

  A1  headword match, multi-character, exactly one candidate  → mechanical
  A2  same, katakana headword (no reading ambiguity)          → mechanical
  A3  headword match, multi-character, several candidates     → per-entry
  B   headword match, single character                        → per-entry
  C   reading-only match, multi-character                     → per-entry
  D   reading-only match, single character                    → reject by default
  R   would be A1/A2, but the surface furigana contradicts
      the target entry's reading                              → per-entry

Only A1+A2 are safe to fix mechanically: the evidence is entirely inside the
link (a full headword match with exactly one candidate entry). B/C/D match on a
single character or on a reading alone and are as likely to be a homograph as
the word — 角 → 02158_tsuno (つの) when the link's 角 is かど; ば → 03699_ba (場)
when the link's ば is the conditional particle.

Each record also carries `wrong_when_written`: true when the target entry was
created *before* the entry the marker sits in, i.e. the marker was never
correct rather than having gone stale. Such a marker needs no "does the sense
still match" check.

Usage:
    python3 build/check_stale_noentry.py                # summary + samples
    python3 build/check_stale_noentry.py --summary      # counts only
    python3 build/check_stale_noentry.py --json         # full review queue
    python3 build/check_stale_noentry.py --class A1 A2  # mechanical batch only
    python3 build/check_stale_noentry.py --range 1 6999 --limit 40
"""
import argparse
import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"
LOOKUP_PATH = PROJECT_ROOT / "build" / "word_id_lookup.json"

# ⟦surface→base：target⟧ — the separator before the target is a full-width colon.
LINK_RE = re.compile(r"⟦([^⟧→]*)→([^⟧：]*)：([^⟧]*)⟧")
KATAKANA_RE = re.compile(r"^[ァ-ヶーヽヾ・]+$")
FURIGANA_RE = re.compile(r"\{[^|{}]+\|([^}]+)\}")
KANA_ONLY_RE = re.compile(r"^[ぁ-ゖァ-ヶーヽヾ・ 　]+$")

MECHANICAL = ("A1", "A2")

VERIFY = ("A1/A2 are mechanical: replace `noentry` with the target id in place, "
          "leaving the surface and base untouched. B/C/D need the entry open — "
          "confirm the linked token really is that word (single characters and "
          "reading-only matches are usually homographs or bound morphemes) "
          "before touching anything. Update the modified timestamp of every "
          "entry changed.")


def to_hiragana(text):
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in text)


def surface_reading(surface):
    """Reading of a link's surface form, from its furigana; None if undecidable."""
    reading = FURIGANA_RE.sub(r"\1", surface)
    if not KANA_ONLY_RE.match(reading):
        return None          # bare kanji with no furigana — cannot check
    return to_hiragana(reading).replace(" ", "").replace("　", "")


def reading_agrees(surface, target_reading):
    """False only when the surface's own furigana contradicts the target entry.

    Catches the two mechanically-detectable false-positive families: a marker
    on a homograph read differently (⟦{臭|にお}い→臭い⟧ pointing at くさい) and
    a marker on a bound, rendaku'd compound element (⟦{張|ば}る→張る⟧ pointing
    at はる). Conjugated surfaces are accepted via the prefix test.
    """
    got = surface_reading(surface)
    if not got or not target_reading:
        return True
    want = to_hiragana(target_reading)
    if got == want:
        return True
    if len(got) > len(want) and got.endswith(want):
        return True          # honorific prefix: ご子息 → 子息, お喜び → 喜び
    if want.endswith("する") and got.startswith(want[:-2]):
        return True          # suru-verb inflection: 負傷した → 負傷する
    shared = 0
    for a, b in zip(got, want):
        if a != b:
            break
        shared += 1
    # An inflected surface diverges only in its final mora (のって/のる,
    # 割り切れない/割り切れる); a different word diverges earlier.
    return shared >= 1 and shared >= min(len(got), len(want)) - 1


def load_lookup():
    data = json.loads(LOOKUP_PATH.read_text(encoding="utf-8"))
    return data.get("by_headword", {}), data.get("by_reading", {})


def numeric_id(stem):
    m = re.match(r"(\d+)", stem)
    return int(m.group(1)) if m else None


def load_entries():
    """Return {file_stem: (path, entry_dict)} for every entry."""
    entries = {}
    for path in sorted(ENTRIES_DIR.glob("*/*.json")):
        try:
            entries[path.stem] = (path, json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue
    return entries


def created_of(entry):
    return ((entry.get("metadata") or {}).get("created") or "")


def link_fields(entry):
    """Yield (field_label, text) for every field that can carry inline links."""
    for key in ("notes", "usage_notes"):
        value = entry.get(key)
        if isinstance(value, str):
            yield key, value
    for i, ex in enumerate(entry.get("examples") or []):
        if isinstance(ex, dict):
            for key in ("japanese", "translation", "note"):
                value = ex.get(key)
                if isinstance(value, str):
                    yield f"examples[{i}].{key}", value
    for key in ("collocations", "patterns", "senses"):
        for item in entry.get(key) or []:
            if isinstance(item, str):
                yield key, item
            elif isinstance(item, dict):
                for sub, value in item.items():
                    if isinstance(value, str):
                        yield f"{key}.{sub}", value


def classify(base, by_headword, by_reading, source_id):
    """Return (class, candidates) for a noentry link's base form."""
    if "{" in base or "|" in base:
        return "base-has-furigana", []
    if not base:
        return "empty-base", []
    hits = [c for c in by_headword.get(base, []) if c.get("id") != source_id]
    if hits:
        if len(base) == 1:
            return "B", hits
        if len(hits) > 1:
            return "A3", hits
        return ("A2" if KATAKANA_RE.match(base) else "A1"), hits
    hits = [c for c in by_reading.get(base, []) if c.get("id") != source_id]
    if hits:
        return ("D" if len(base) == 1 else "C"), hits
    return "unresolved", []


def scan(id_range=None):
    by_headword, by_reading = load_lookup()
    entries = load_entries()
    created = {stem: created_of(e) for stem, (_p, e) in entries.items()}

    records = []
    for stem, (path, entry) in entries.items():
        num = numeric_id(stem)
        if num is None:
            continue
        if id_range and not (id_range[0] <= num <= id_range[1]):
            continue
        seen = {}
        for field, text in link_fields(entry):
            if "noentry" not in text:
                continue
            for surface, base, target in LINK_RE.findall(text):
                if target != "noentry":
                    continue
                key = (base, surface)
                if key in seen:
                    seen[key]["instances"] += 1
                    if field not in seen[key]["fields"]:
                        seen[key]["fields"].append(field)
                    continue
                klass, hits = classify(base, by_headword, by_reading, stem)
                target_id = hits[0].get("id") if len(hits) == 1 else None
                if klass in MECHANICAL and not reading_agrees(
                        surface, (hits[0] or {}).get("reading")):
                    klass = "R"     # surface furigana contradicts the target
                rec = {
                    "entry_id": stem.split("_")[0],
                    "entry_stem": stem,
                    "file": str(path.relative_to(PROJECT_ROOT)),
                    "class": klass,
                    "marker": f"⟦{surface}→{base}：noentry⟧",
                    "surface": surface,
                    "base": base,
                    "fields": [field],
                    "instances": 1,
                    "target_id": target_id,
                    "candidates": [
                        {"id": c.get("id"),
                         "headword": c.get("headword"),
                         "reading": c.get("reading"),
                         "gloss": c.get("gloss")}
                        for c in hits[:5]
                    ],
                    "wrong_when_written": bool(
                        target_id
                        and created.get(target_id)
                        and created.get(stem)
                        and created[target_id] < created[stem]),
                    "mechanical": klass in MECHANICAL,
                }
                seen[key] = rec
                records.append(rec)
    records.sort(key=lambda r: (r["entry_id"], r["base"]))
    return records


def main():
    ap = argparse.ArgumentParser(
        description="Find `noentry` inline links whose word now has an entry (read-only).")
    ap.add_argument("--summary", action="store_true", help="Counts only.")
    ap.add_argument("--json", action="store_true", help="Full JSON review queue.")
    ap.add_argument("--class", dest="classes", nargs="+", metavar="CLASS",
                    help="Filter to one or more classes (A1 A2 A3 B C D ...).")
    ap.add_argument("--mechanical", action="store_true",
                    help="Shorthand for --class A1 A2.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--limit", type=int, default=25, help="Sample size (default 25).")
    args = ap.parse_args()

    records = scan(tuple(args.range) if args.range else None)
    if args.mechanical:
        records = [r for r in records if r["mechanical"]]
    elif args.classes:
        wanted = set(args.classes)
        records = [r for r in records if r["class"] in wanted]

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    by_class, instances = {}, {}
    for r in records:
        by_class[r["class"]] = by_class.get(r["class"], 0) + 1
        instances[r["class"]] = instances.get(r["class"], 0) + r["instances"]
    total_inst = sum(instances.values())
    entries = {r["entry_stem"] for r in records}
    mech = [r for r in records if r["mechanical"]]
    wrong = [r for r in mech if r["wrong_when_written"]]
    print(f"noentry markers examined: {total_inst} instances "
          f"({len(records)} distinct base/surface pairs) in {len(entries)} entries")
    for klass in sorted(by_class):
        print(f"  {klass:17} {by_class[klass]:5} pairs  {instances[klass]:5} instances")
    print(f"  mechanical (A1+A2): {len(mech)} pairs, "
          f"{sum(r['instances'] for r in mech)} instances "
          f"({len(wrong)} wrong when written)")
    if not args.summary:
        print()
        for r in records[:args.limit]:
            tail = r["target_id"] or f"{len(r['candidates'])} candidates"
            print(f"  [{r['class']}] {r['entry_stem']}: {r['marker']} -> {tail}")
        if len(records) > args.limit:
            print(f"  ... and {len(records) - args.limit} more (use --json for all)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
