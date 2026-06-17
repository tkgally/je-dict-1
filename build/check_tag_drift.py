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
    unknown-semantic         a semantic tag outside VALID_SEMANTIC (Cleanup P20
                             — migrate to the suggested/best in-list tag)       [warn]

  HIGH-PRECISION (Cleanup P11 — batch-ready slices of the semantic tag drift)
    proverb-idiom-mismatch   a proverb / yojijukugo / set-expression headword
                             tagged with a physical-object/creature domain
                             (furniture, clothing, electronics, food, animal-*)
                             with no keyword support — the 一期一会/四苦八苦/
                             起死回生 → furniture family. Near-deterministic.     [warn]
    concrete-noun-domain-mismatch
                             a non-verb headword carrying TWO OR MORE
                             semantically-distant "hard" physical-object domains
                             (横断歩道 → animal-mammal+clothing+transportation,
                             油絵 → body-part+tool) — the batch garbage multi-tag
                             cluster. Structural, so independent of keyword
                             completeness (unlike semantic-mismatch).            [warn]

  HEURISTIC (review queue — false positives expected, VERIFY each)
    semantic-mismatch        a concrete-domain semantic tag (furniture,
                             transportation, electronics, ...) whose keywords
                             appear nowhere in the gloss/definitions/examples
                             (Cleanup P11 — the pervasive batch tag drift; noisy:
                             flags boat=transportation, school=building. The two
                             high-precision checks above are the batch-ready
                             slices to drive a fix from.)                        [warn]

Optional --cohort restricts the scan to the contaminated batch (entries whose
metadata.ai_model is in the claude-opus-4-5 family — the cohort that dominates
Cleanup P11), to prioritise the highest-density surface.

Usage:
    python3 build/check_tag_drift.py                  # human summary + sample
    python3 build/check_tag_drift.py --summary
    python3 build/check_tag_drift.py --json           # full JSON queue (for systemic-fix)
    python3 build/check_tag_drift.py --check proverb-idiom-mismatch
    python3 build/check_tag_drift.py --check concrete-noun-domain-mismatch --cohort
    python3 build/check_tag_drift.py --range 5700 6340
"""
import argparse
import itertools
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_tags import VALID_SEMANTIC  # noqa: E402

# 1:1 migrations for the common out-of-taxonomy tags that were NOT blessed in
# the 2026-06-11 taxonomy expansion (near-duplicates of existing tags). Tags
# absent from this map need a per-entry choice of the best VALID_SEMANTIC tag.
TAG_MIGRATION = {
    "time": "time-general",
    "people": "person",
    "social": "society",
    "description": "descriptive",
    "medical": "health",
    "medicine": "health",
    "transport": "transportation",
    "animals": "animal-general",
    "economy": "economics",
}

VERB_OR_IADJ = {"verb-godan", "verb-ichidan", "verb-suru", "verb-kuru",
                "verb-irregular", "adjective-i"}
VERB_POS = {"verb-godan", "verb-ichidan", "verb-suru", "verb-kuru",
            "verb-irregular"}

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

# --- High-precision P11 signals (added 2026-06-17) ------------------------
#
# These two checks carve the *batch-ready* slices out of the noisy
# semantic-mismatch heuristic. Both were calibrated against the 5700-6340 dense
# block (the highest-density P11 pocket; see cleanup-backlog.md P11 update
# 2026-06-17) before shipping — see prompts/fix_semantic_tag_drift.md for the
# measured precision/recall.

# Physical-object / creature domains that essentially never apply to an abstract
# proverb, yojijukugo, or set expression. Deliberately EXCLUDES tool, geography,
# weather, building, transportation, and body-part: those DO legitimately apply
# to compositional four-kanji compounds (懐中電灯=tool, 都道府県=geography,
# 直射日光=weather, 横断歩道=transportation) and to body idioms, and including them
# is what pushed the early drafts below the noise floor. Keeping the set to
# artifacts + creatures is what makes proverb-idiom-mismatch near-deterministic.
PROVERB_OBJECT_DOMAINS = {"furniture", "clothing", "electronics", "food",
                          "animal-mammal", "animal-insect", "animal-bird",
                          "animal-fish"}

# Markers that an entry is ITSELF a proverb / idiom / yojijukugo. Checked in the
# GLOSS only (never the notes): concrete nouns such as 顔 / 猫 routinely list
# idioms in a "Common Idioms" notes section, so a notes-level marker test floods
# the queue with correctly-tagged body-part/animal nouns. A gloss reads "face",
# "cat", … — only a genuine idiom entry says "proverb"/"idiom"/"figuratively".
IDIOM_GLOSS_MARKERS = ("proverb", "idiom", "yojijukugo", "four-character",
                       "four character", "set phrase", "figuratively")

# "Hard" physical-object / creature domains: a single concrete noun belongs to AT
# MOST one of these. Two or more *semantically distant* ones on one headword is
# the batch garbage multi-tag signature (a random tag set copied from an
# unrelated entry). Structural — does not depend on the (necessarily incomplete)
# per-tag keyword lists above, so it sidesteps the semantic-mismatch noise floor.
HARD_OBJECT_DOMAINS = {"furniture", "clothing", "electronics", "transportation",
                       "building", "tool", "animal-mammal", "animal-insect",
                       "animal-bird", "animal-fish", "body-part"}

# Pairs of hard domains that DO legitimately co-occur on one headword
# (infrastructure: building↔transportation; devices: electronics↔tool; fixtures:
# building↔furniture; worn items: clothing↔body-part; food animals: animal↔food).
# Excluded so the detector flags only genuinely distant clusters.
ADJACENT_OBJECT_DOMAINS = {
    frozenset(pair) for pair in [
        ("building", "transportation"), ("building", "furniture"),
        ("building", "tool"), ("electronics", "tool"),
        ("electronics", "furniture"), ("furniture", "tool"),
        ("transportation", "tool"), ("clothing", "body-part"),
        ("animal-fish", "food"), ("animal-mammal", "food"),
        ("animal-bird", "food"),
    ]
}

# Models in the contaminated batch (Cleanup P11): claude-opus-4-5, opus-4-5,
# claude-opus-4-5-20251101. Matched as a substring of metadata.ai_model.
COHORT_MODEL_MARKER = "opus-4-5"

FURIGANA_RE = re.compile(r"\{([^|}]+)\|[^}]*\}")
YOJIJUKUGO_RE = re.compile(r"[一-鿿]{4}\Z")


def base_headword(headword):
    """Strip furigana wrappers: {一期一会|いちごいちえ} -> 一期一会."""
    return FURIGANA_RE.sub(r"\1", headword or "")


def looks_idiomatic(data, pos):
    """True if the entry is a proverb / yojijukugo / set expression."""
    bh = base_headword(data.get("headword"))
    if YOJIJUKUGO_RE.fullmatch(bh):
        return True
    if "expression" in pos:
        return True
    gloss_lc = (data.get("gloss") or "").lower()
    return any(m in gloss_lc for m in IDIOM_GLOSS_MARKERS)


def distant_object_domains(semantic):
    """Distant 'hard' physical-object domain pairs on one headword.

    Returns the list of (a, b) pairs of HARD_OBJECT_DOMAINS present in the
    semantic list that are NOT a whitelisted adjacent (legitimately
    co-occurring) pair. A non-empty result is the batch garbage multi-tag
    signature for concrete-noun-domain-mismatch.
    """
    hard = sorted({s for s in semantic if s in HARD_OBJECT_DOMAINS})
    return [(a, b) for a, b in itertools.combinations(hard, 2)
            if frozenset((a, b)) not in ADJACENT_OBJECT_DOMAINS]


def numeric_id(entry_id):
    m = re.match(r"(\d+)", str(entry_id))
    return int(m.group(1)) if m else None


def iter_entries(id_range=None, cohort=False):
    for path in sorted(ENTRIES_DIR.glob("**/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        nid = numeric_id(data.get("id", path.stem))
        if id_range and nid is not None and not (id_range[0] <= nid <= id_range[1]):
            continue
        if cohort:
            model = (data.get("metadata") or {}).get("ai_model") or ""
            if COHORT_MODEL_MARKER not in model:
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


def scan(id_range=None, only=None, cohort=False):
    records = []

    def add(eid, rel, check, detail, severity, verify, tag=None):
        records.append({"entry_id": eid, "file": rel, "check": check, "tag": tag,
                        "detail": detail, "severity": severity, "verify": verify})

    for data, path in iter_entries(id_range, cohort=cohort):
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

        if only in (None, "unknown-semantic"):
            for tag in semantic:
                if tag not in VALID_SEMANTIC:
                    target = TAG_MIGRATION.get(tag)
                    add(eid, rel, "unknown-semantic",
                        f"semantic tag {tag!r} is not in VALID_SEMANTIC"
                        + (f" (suggested: {target!r})" if target else ""),
                        "warn",
                        "Replace with the suggested 1:1 migration target, or "
                        "choose the best VALID_SEMANTIC tag for this headword.",
                        tag=tag)

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

        if only in (None, "proverb-idiom-mismatch"):
            if (set(semantic) & PROVERB_OBJECT_DOMAINS
                    and not (set(semantic) & {"proverb", "idiom"})
                    and looks_idiomatic(data, pos)):
                etext = english_text(data)
                for tag in semantic:
                    if tag not in PROVERB_OBJECT_DOMAINS:
                        continue
                    kws = CONCRETE_TAG_KEYWORDS.get(tag, [])
                    if kws and not any(k in etext for k in kws):
                        add(eid, rel, "proverb-idiom-mismatch",
                            f"proverb/yojijukugo/set-expression headword tagged "
                            f"{tag!r} (physical-object domain) with no keyword support",
                            "warn",
                            "Confirm the headword is a proverb/yojijukugo/set "
                            "phrase, then replace the object-domain tag with "
                            "'proverb' or 'idiom' (or 'expression').",
                            tag=tag)

        if only in (None, "concrete-noun-domain-mismatch"):
            if not (set(pos) & VERB_POS):
                distant = distant_object_domains(semantic)
                if distant:
                    a, b = distant[0]
                    hard = sorted({s for s in semantic if s in HARD_OBJECT_DOMAINS})
                    add(eid, rel, "concrete-noun-domain-mismatch",
                        f"carries distant physical-object domains {hard} "
                        f"({a!r} and {b!r} do not co-occur on one headword)",
                        "warn",
                        "Decide the single object domain the headword "
                        "belongs to; drop the unrelated object-domain tag(s).",
                        tag=a)

    return records


def main():
    ap = argparse.ArgumentParser(description="Detect tag drift (read-only).")
    ap.add_argument("--json", action="store_true", help="Emit the full JSON review queue.")
    ap.add_argument("--summary", action="store_true", help="Print counts only.")
    ap.add_argument("--check", choices=["conjugation-no-verb-pos", "politeness-unsupported",
                                        "sole-general", "semantic-mismatch",
                                        "unknown-semantic", "proverb-idiom-mismatch",
                                        "concrete-noun-domain-mismatch"],
                    help="Filter to one check.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--cohort", action="store_true",
                    help="Restrict to the claude-opus-4-5 batch cohort (Cleanup P11).")
    ap.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()

    records = scan(tuple(args.range) if args.range else None, only=args.check,
                   cohort=args.cohort)

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    by_check, entries = {}, set()
    for r in records:
        by_check[r["check"]] = by_check.get(r["check"], 0) + 1
        entries.add(r["entry_id"])
    print(f"Tag drift: {len(records)} flags across {len(entries)} entries")
    for chk in ("conjugation-no-verb-pos", "proverb-idiom-mismatch",
                "concrete-noun-domain-mismatch", "politeness-unsupported",
                "semantic-mismatch", "unknown-semantic", "sole-general"):
        if chk in by_check:
            print(f"  {chk:30} {by_check[chk]}")
    if not args.summary and records:
        print(f"\nSample (first {args.limit}, errors first):")
        order = {"error": 0, "warn": 1, "info": 2}
        for r in sorted(records, key=lambda r: order[r["severity"]])[:args.limit]:
            print(f"  [{r['severity']:5}] {r['entry_id']} {r['check']}: {r['detail']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
