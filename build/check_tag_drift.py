#!/usr/bin/env python3
"""Detect tag drift — entries whose metadata tags don't match their content.

READ-ONLY review-queue generator for the Routine's systemic-fix mode; it never
modifies entries. Addresses Tooling Backlog item 6 and Cleanup Backlog
Priorities 7, 11, and 13. Two confidence tiers:

  DETERMINISTIC (high confidence)
    conjugation-no-verb-pos  has a `conjugation` field but no verb/adjective-i POS
                             (Cleanup P6 — the onomatopoeia/adverb case)        [error]
    politeness-unsupported   politeness humble/honorific but notes contain none
                             of the supporting keywords (Cleanup P7)            [warn]
    sole-general             semantic == ["general"] (under-specified, P13)     [info]

  HEURISTIC (review queue — false positives expected, VERIFY each)
    semantic-mismatch        a concrete-domain semantic tag (furniture,
                             transportation, electronics, ...) whose keywords
                             appear nowhere in the gloss/definitions/examples
                             (Cleanup P11 — the pervasive batch tag drift)      [warn]

Usage:
    python3 build/check_tag_drift.py                  # human summary + sample
    python3 build/check_tag_drift.py --summary
    python3 build/check_tag_drift.py --json           # full JSON queue (for systemic-fix)
    python3 build/check_tag_drift.py --check semantic-mismatch
    python3 build/check_tag_drift.py --range 5000 5500
"""
import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"

VERB_OR_IADJ = {"verb-godan", "verb-ichidan", "verb-suru", "verb-kuru",
                "verb-irregular", "adjective-i"}

POLITENESS_SUPPORT = ["humble", "honorific", "polite", "keigo", "respectful",
                      "deferential", "in-group", "out-group", "uchi", "soto",
                      "bikago", "beautifying", "sonkeigo", "kenjougo", "teineigo"]

# Concrete physical-domain tags repeatedly misapplied in batch creation
# (per Cleanup Backlog P11). If one of these is present but none of its keywords
# appear in the entry's English text, it is flagged for verification.
CONCRETE_TAG_KEYWORDS = {
    "transportation": ["train", "car", "bus", "vehicle", "transport", "drive",
                       "traffic", "railway", "station", "flight", "ride",
                       "bicycle", "ship", "road", "travel", "subway", "airplane"],
    "furniture": ["furniture", "chair", "table", "desk", "shelf", "bed", "sofa",
                  "drawer", "cabinet", "cupboard", "stool", "couch"],
    "electronics": ["electronic", "device", "computer", "phone", "screen",
                    "battery", "digital", "appliance", "gadget", "machine",
                    "electric", "camera", "monitor", "circuit"],
    "clothing": ["cloth", "clothing", "wear", "garment", "shirt", "dress",
                 "fabric", "textile", "sleeve", "jacket", "coat", "shoe", "hat",
                 "trousers", "skirt", "sock", "glove"],
    "body-part": ["body", "hand", "arm", "leg", "foot", "head", "eye", "ear",
                  "nose", "mouth", "finger", "skin", "bone", "muscle", "organ",
                  "neck", "shoulder", "chest", "back", "hair", "tooth", "knee",
                  "stomach", "throat", "lip"],
    "tool": ["tool", "instrument", "utensil", "knife", "hammer", "blade",
             "equipment", "wrench", "scissors", "needle"],
    "weather": ["weather", "rain", "snow", "wind", "cloud", "storm",
                "temperature", "climate", "sunny", "humid", "forecast", "fog",
                "thunder", "frost"],
    "animal-mammal": ["animal", "mammal", "dog", "cat", "horse", "cow", "bear",
                      "beast", "pig", "sheep", "monkey", "rabbit", "deer", "fox"],
    "animal-insect": ["insect", "bug", "beetle", "ant", "fly", "mosquito",
                      "butterfly", "larva", "moth", "bee", "cricket", "spider"],
    "food": ["food", "eat", "dish", "meal", "cook", "taste", "flavor",
             "ingredient", "cuisine", "edible", "sweet", "drink", "sauce",
             "rice", "meat", "vegetable", "fruit", "soup", "snack", "noodle"],
    "building": ["building", "house", "room", "wall", "roof", "floor",
                 "structure", "architecture", "hall", "facility", "gate",
                 "tower", "bridge"],
    "geography": ["region", "area", "land", "mountain", "river", "sea",
                  "island", "geography", "terrain", "coast", "valley", "lake",
                  "forest", "field", "plain", "continent"],
}


def numeric_id(entry_id):
    m = re.match(r"(\d+)", str(entry_id))
    return int(m.group(1)) if m else None


def iter_entries(id_range=None):
    for path in sorted(ENTRIES_DIR.glob("**/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        nid = numeric_id(data.get("id", path.stem))
        if id_range and nid is not None and not (id_range[0] <= nid <= id_range[1]):
            continue
        yield data, path


def english_text(data):
    parts = [data.get("gloss") or ""]
    for d in data.get("definitions", []) or []:
        parts.append(d.get("gloss") or "")
        parts.append(d.get("explanation") or "")
    for ex in data.get("examples", []) or []:
        parts.append(ex.get("english") or "")
    return " ".join(parts).lower()


def scan(id_range=None, only=None):
    records = []

    def add(eid, rel, check, detail, severity, verify, tag=None):
        records.append({"entry_id": eid, "file": rel, "check": check, "tag": tag,
                        "detail": detail, "severity": severity, "verify": verify})

    for data, path in iter_entries(id_range):
        eid = data.get("id", path.stem)
        rel = str(path.relative_to(PROJECT_ROOT))
        tags = (data.get("metadata") or {}).get("tags", {}) or {}
        pos = tags.get("pos", []) or []
        semantic = tags.get("semantic", []) or []
        politeness = tags.get("politeness")
        notes_lc = (data.get("notes") or "").lower()

        if only in (None, "conjugation-no-verb-pos"):
            if data.get("conjugation") and not (set(pos) & VERB_OR_IADJ):
                add(eid, rel, "conjugation-no-verb-pos",
                    f"pos={pos} has a conjugation field", "error",
                    "Remove the spurious conjugation field and any stray verb_class tag.")

        if only in (None, "politeness-unsupported"):
            if politeness in ("humble", "honorific"):
                if not any(k in notes_lc for k in POLITENESS_SUPPORT):
                    add(eid, rel, "politeness-unsupported",
                        f"politeness={politeness!r} but notes lack supporting wording",
                        "warn",
                        "Verify uchi/soto vs. true keigo; fix the tag or add a notes explanation.",
                        tag=politeness)

        if only in (None, "sole-general"):
            if semantic == ["general"]:
                add(eid, rel, "sole-general", "semantic == ['general']", "info",
                    "Replace with a specific semantic tag if one clearly applies.",
                    tag="general")

        if only in (None, "semantic-mismatch"):
            etext = None
            for tag in semantic:
                kws = CONCRETE_TAG_KEYWORDS.get(tag)
                if not kws:
                    continue
                if etext is None:
                    etext = english_text(data)
                if not any(k in etext for k in kws):
                    add(eid, rel, "semantic-mismatch",
                        f"semantic tag {tag!r} has no keyword match in the English text",
                        "warn",
                        "Confirm the tag is wrong for this headword (batch drift), then correct it.",
                        tag=tag)

    return records


def main():
    ap = argparse.ArgumentParser(description="Detect tag drift (read-only).")
    ap.add_argument("--json", action="store_true", help="Emit the full JSON review queue.")
    ap.add_argument("--summary", action="store_true", help="Print counts only.")
    ap.add_argument("--check", choices=["conjugation-no-verb-pos", "politeness-unsupported",
                                        "sole-general", "semantic-mismatch"],
                    help="Filter to one check.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()

    records = scan(tuple(args.range) if args.range else None, only=args.check)

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    by_check, entries = {}, set()
    for r in records:
        by_check[r["check"]] = by_check.get(r["check"], 0) + 1
        entries.add(r["entry_id"])
    print(f"Tag drift: {len(records)} flags across {len(entries)} entries")
    for chk in ("conjugation-no-verb-pos", "politeness-unsupported",
                "semantic-mismatch", "sole-general"):
        if chk in by_check:
            print(f"  {chk:26} {by_check[chk]}")
    if not args.summary and records:
        print(f"\nSample (first {args.limit}, errors first):")
        order = {"error": 0, "warn": 1, "info": 2}
        for r in sorted(records, key=lambda r: order[r["severity"]])[:args.limit]:
            print(f"  [{r['severity']:5}] {r['entry_id']} {r['check']}: {r['detail']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
