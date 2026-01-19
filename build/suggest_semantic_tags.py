#!/usr/bin/env python3
"""
Semi-automated semantic tagging script for dictionary entries.

Uses broader pattern matching on definitions, notes, and glosses to suggest
semantic category tags for entries not caught by auto_semantic_tags.py.

This script analyzes entries more liberally and generates suggestions for
human review rather than applying tags automatically.

Usage:
    python3 build/suggest_semantic_tags.py --output suggestions.json
    python3 build/suggest_semantic_tags.py --apply-high-confidence
    python3 build/suggest_semantic_tags.py --batch-review 100

Options:
    --output FILE           Output suggestions to JSON file
    --apply-high-confidence Apply only high-confidence suggestions
    --batch-review N        Generate review file for N entries
    --verbose               Show detailed output
"""

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# =============================================================================
# KEYWORD-BASED SEMANTIC TAG SUGGESTIONS
# =============================================================================
# These are more liberal patterns that suggest tags based on keywords in
# definitions and notes. They have confidence scores.

# Format: (keywords, semantic_tags, confidence, description)
# confidence: "high" (0.9+), "medium" (0.7-0.9), "low" (0.5-0.7)

DEFINITION_KEYWORDS = [
    # Time
    (["time", "period", "era", "age", "duration"], ["time-general"], "medium", "time concepts"),
    (["schedule", "appointment", "deadline"], ["time-general"], "medium", "scheduling"),
    (["past", "future", "present", "historical"], ["time-general"], "low", "temporal reference"),

    # Nature - Animals
    (["animal", "creature", "beast"], ["animal-general"], "high", "general animal terms"),
    (["mammal", "warm-blooded"], ["animal-mammal"], "high", "mammal classification"),
    (["bird", "avian", "feather"], ["animal-bird"], "medium", "bird-related"),
    (["fish", "aquatic", "marine", "seafood"], ["animal-fish"], "medium", "fish/seafood"),
    (["insect", "bug", "pest", "larva"], ["animal-insect"], "high", "insect-related"),
    (["pet", "livestock", "domestic"], ["animal-general"], "medium", "domesticated animals"),

    # Plants
    (["plant", "vegetation", "flora", "botanical"], ["plant-general"], "high", "plant terms"),
    (["tree", "forest", "wood", "timber", "lumber"], ["plant-tree"], "medium", "tree-related"),
    (["flower", "blossom", "petal", "bloom"], ["plant-flower"], "high", "flower-related"),
    (["grass", "lawn", "weed", "herb"], ["plant-general"], "medium", "ground plants"),
    (["fruit", "berry"], ["plant-general", "food"], "medium", "fruit"),

    # Weather & Geography
    (["weather", "climate", "forecast", "meteorological"], ["weather"], "high", "weather terms"),
    (["rain", "snow", "wind", "storm", "typhoon", "hurricane"], ["weather"], "high", "weather events"),
    (["temperature", "humidity", "pressure"], ["weather"], "medium", "weather conditions"),
    (["mountain", "hill", "peak", "summit", "slope"], ["geography"], "high", "mountain-related"),
    (["river", "stream", "creek", "waterfall"], ["geography"], "high", "water features"),
    (["ocean", "sea", "coast", "beach", "shore", "island"], ["geography"], "high", "coastal features"),
    (["lake", "pond", "swamp", "marsh"], ["geography"], "high", "inland water"),
    (["forest", "jungle", "woods"], ["geography", "plant-tree"], "medium", "forested areas"),
    (["desert", "plain", "valley", "canyon"], ["geography"], "medium", "land features"),

    # Human body
    (["body", "physical", "anatomy", "physiology"], ["body-part"], "medium", "body general"),
    (["organ", "internal", "viscera"], ["body-internal"], "high", "internal organs"),
    (["bone", "skeleton", "joint"], ["body-internal"], "high", "skeletal system"),
    (["muscle", "tendon", "ligament"], ["body-internal"], "medium", "muscular system"),
    (["blood", "vein", "artery", "heart", "cardiovascular"], ["body-internal"], "high", "circulatory"),
    (["brain", "nerve", "neuron", "neural"], ["body-internal"], "high", "nervous system"),
    (["skin", "epidermis", "complexion"], ["body-part"], "medium", "integumentary"),

    # Family & Relations
    (["family", "relative", "relation", "kin", "kinship"], ["family"], "high", "family terms"),
    (["parent", "child", "sibling"], ["family"], "high", "immediate family"),
    (["ancestor", "descendant", "generation"], ["family"], "medium", "lineage"),
    (["marriage", "wedding", "spouse", "married"], ["family"], "medium", "marriage-related"),

    # People & Occupations
    (["person", "individual", "human", "people"], ["person"], "medium", "person terms"),
    (["profession", "occupation", "career", "job", "employment"], ["occupation", "work"], "high", "job terms"),
    (["worker", "employee", "staff", "personnel"], ["occupation", "work"], "high", "worker terms"),
    (["expert", "specialist", "professional"], ["occupation"], "medium", "professionals"),
    (["official", "officer", "administrator"], ["occupation"], "medium", "officials"),

    # Food & Drink
    (["food", "cuisine", "dish", "meal", "diet"], ["food"], "high", "food terms"),
    (["cook", "cooking", "culinary", "chef", "bake", "baking"], ["food"], "high", "cooking"),
    (["drink", "beverage", "liquid"], ["food"], "medium", "beverages"),
    (["ingredient", "seasoning", "spice", "condiment"], ["food"], "high", "ingredients"),
    (["restaurant", "cafe", "diner", "eatery"], ["food", "building"], "high", "eating places"),
    (["taste", "flavor", "delicious", "tasty"], ["food"], "medium", "taste-related"),
    (["vegetable", "veggie", "greens"], ["food"], "high", "vegetables"),

    # Clothing & Accessories
    (["clothing", "clothes", "garment", "apparel", "wear", "attire"], ["clothing"], "high", "clothing terms"),
    (["fashion", "style", "outfit", "dress"], ["clothing"], "medium", "fashion"),
    (["accessory", "jewelry", "ornament"], ["clothing"], "medium", "accessories"),
    (["fabric", "textile", "material", "cloth"], ["clothing"], "medium", "materials"),

    # Buildings & Places
    (["building", "structure", "facility", "establishment"], ["building"], "high", "buildings"),
    (["room", "chamber", "hall", "space"], ["building"], "medium", "rooms"),
    (["architecture", "construction", "built"], ["building"], "medium", "construction"),
    (["residence", "dwelling", "housing", "apartment"], ["building"], "high", "residential"),

    # Transportation
    (["transportation", "transport", "transit", "travel"], ["transportation"], "high", "transport terms"),
    (["vehicle", "automobile", "car", "truck"], ["transportation"], "high", "vehicles"),
    (["train", "railway", "railroad", "station"], ["transportation"], "high", "rail"),
    (["airplane", "aircraft", "aviation", "flight", "airport"], ["transportation"], "high", "aviation"),
    (["ship", "boat", "vessel", "port", "harbor"], ["transportation"], "high", "maritime"),
    (["road", "street", "highway", "path", "route"], ["transportation"], "medium", "roads"),

    # Tools & Objects
    (["tool", "instrument", "implement", "equipment", "device"], ["tool"], "high", "tools"),
    (["machine", "machinery", "apparatus"], ["tool"], "medium", "machines"),
    (["container", "box", "bag", "package"], ["tool"], "low", "containers"),

    # Furniture
    (["furniture", "furnishing"], ["furniture"], "high", "furniture terms"),

    # Electronics
    (["electronic", "electrical", "electric", "power"], ["electronics"], "high", "electronics"),
    (["computer", "digital", "software", "hardware"], ["electronics"], "high", "computing"),
    (["internet", "online", "network", "web"], ["electronics"], "high", "internet"),
    (["phone", "telephone", "mobile", "smartphone"], ["electronics"], "high", "phones"),

    # Emotions & Psychology
    (["emotion", "emotional", "feeling", "mood", "sentiment"], ["emotion"], "high", "emotion terms"),
    (["happy", "happiness", "joy", "pleased", "delighted"], ["emotion"], "high", "positive emotions"),
    (["sad", "sadness", "sorrow", "grief", "unhappy"], ["emotion"], "high", "negative emotions"),
    (["angry", "anger", "rage", "furious", "annoyed"], ["emotion"], "high", "anger"),
    (["fear", "afraid", "scared", "frightened", "anxious", "anxiety"], ["emotion"], "high", "fear"),
    (["love", "affection", "fondness", "attachment"], ["emotion"], "high", "love"),
    (["surprise", "surprised", "shock", "astonishment"], ["emotion"], "medium", "surprise"),
    (["mental", "psychological", "psyche"], ["emotion"], "low", "psychological"),

    # Communication & Language
    (["communication", "communicate", "express", "convey"], ["communication"], "high", "communication"),
    (["language", "linguistic", "speech", "speak"], ["communication"], "high", "language"),
    (["conversation", "dialogue", "discussion", "talk"], ["communication"], "high", "conversation"),
    (["writing", "written", "text", "document"], ["communication"], "medium", "writing"),
    (["reading", "read"], ["communication"], "medium", "reading"),

    # Cognition & Thought
    (["think", "thought", "thinking", "mental"], ["cognition"], "high", "thinking"),
    (["know", "knowledge", "understanding", "comprehend"], ["cognition"], "high", "knowledge"),
    (["memory", "remember", "recall", "memorize"], ["cognition"], "high", "memory"),
    (["learn", "learning", "study", "education"], ["cognition", "education"], "high", "learning"),
    (["decide", "decision", "choice", "choose"], ["cognition"], "medium", "decisions"),
    (["reason", "logic", "rational", "analyze"], ["cognition"], "medium", "reasoning"),

    # Movement & Action
    (["move", "movement", "motion", "moving"], ["movement"], "high", "movement"),
    (["walk", "walking", "step", "stride"], ["movement"], "high", "walking"),
    (["run", "running", "sprint", "dash"], ["movement"], "high", "running"),
    (["jump", "leap", "hop", "bounce"], ["movement"], "high", "jumping"),
    (["climb", "ascending", "descending"], ["movement"], "medium", "vertical movement"),

    # Existence & State
    (["exist", "existence", "being", "presence"], ["existence"], "high", "existence"),
    (["become", "change", "transform", "turn into"], ["existence"], "medium", "change of state"),
    (["remain", "stay", "continue", "persist"], ["existence"], "medium", "continuation"),

    # Consumption
    (["eat", "eating", "consume", "consumption"], ["consumption"], "high", "eating"),
    (["drink", "drinking", "sip", "gulp"], ["consumption"], "high", "drinking"),
    (["buy", "purchase", "acquire", "obtain"], ["consumption"], "medium", "buying"),
    (["use", "utilize", "employ"], ["consumption"], "low", "using"),

    # Work & Business
    (["work", "working", "labor", "effort"], ["work"], "high", "work"),
    (["business", "company", "corporate", "firm"], ["work"], "high", "business"),
    (["office", "workplace", "job"], ["work"], "medium", "workplace"),
    (["meeting", "conference", "assembly"], ["work"], "medium", "meetings"),
    (["project", "task", "assignment"], ["work"], "medium", "tasks"),
    (["economy", "economic", "financial", "commerce"], ["work"], "medium", "economics"),

    # Education
    (["education", "educational", "academic"], ["education"], "high", "education"),
    (["school", "university", "college", "academy"], ["education", "building"], "high", "schools"),
    (["student", "pupil", "learner"], ["education", "person"], "high", "students"),
    (["teacher", "instructor", "professor", "tutor"], ["education", "occupation"], "high", "teachers"),
    (["class", "course", "lesson", "lecture"], ["education"], "high", "classes"),
    (["exam", "examination", "test", "quiz"], ["education"], "high", "tests"),
    (["homework", "assignment", "study"], ["education"], "medium", "homework"),

    # Leisure & Entertainment
    (["leisure", "recreation", "hobby", "pastime"], ["leisure"], "high", "leisure"),
    (["play", "playing", "game", "gaming"], ["leisure"], "high", "games"),
    (["sport", "sports", "athletic", "exercise"], ["leisure"], "high", "sports"),
    (["music", "musical", "song", "melody"], ["leisure"], "high", "music"),
    (["movie", "film", "cinema", "theater"], ["leisure"], "high", "film"),
    (["travel", "trip", "journey", "tour", "vacation"], ["leisure"], "high", "travel"),
    (["art", "artistic", "creative"], ["leisure"], "medium", "art"),

    # Social & Greeting
    (["greeting", "greet", "salutation"], ["greeting"], "high", "greetings"),
    (["polite", "politeness", "courtesy", "manners"], ["greeting"], "medium", "politeness"),
    (["social", "society", "community"], ["person"], "low", "social"),

    # Colors
    (["color", "colour", "hue", "shade", "tint"], ["color"], "high", "color terms"),
    (["red", "crimson", "scarlet"], ["color"], "high", "red shades"),
    (["blue", "azure", "navy"], ["color"], "high", "blue shades"),
    (["green", "emerald", "olive"], ["color"], "high", "green shades"),
    (["yellow", "golden", "amber"], ["color"], "high", "yellow shades"),
    (["white", "pale", "ivory"], ["color"], "medium", "white shades"),
    (["black", "dark", "ebony"], ["color"], "medium", "black shades"),

    # Numbers & Quantity
    (["number", "numerical", "numeral", "digit"], ["number"], "high", "numbers"),
    (["count", "counting", "amount", "quantity"], ["number", "quantity"], "medium", "counting"),
    (["many", "much", "numerous", "plenty"], ["quantity"], "medium", "large quantity"),
    (["few", "little", "scarce", "rare"], ["quantity"], "medium", "small quantity"),

    # Size
    (["size", "dimension", "measurement"], ["size"], "high", "size terms"),
    (["big", "large", "huge", "enormous", "giant"], ["size"], "high", "large size"),
    (["small", "little", "tiny", "miniature"], ["size"], "high", "small size"),
    (["long", "length", "lengthy", "extended"], ["size"], "medium", "length"),
    (["short", "brief", "abbreviated"], ["size"], "medium", "shortness"),
    (["tall", "height", "high", "lofty"], ["size"], "medium", "height"),
    (["wide", "broad", "width"], ["size"], "medium", "width"),
    (["thick", "thin", "depth"], ["size"], "medium", "thickness"),

    # Direction
    (["direction", "directional"], ["direction"], "high", "direction terms"),
    (["north", "south", "east", "west"], ["direction"], "high", "cardinal directions"),
    (["up", "down", "above", "below"], ["direction"], "medium", "vertical"),
    (["left", "right", "side"], ["direction"], "medium", "lateral"),
    (["front", "back", "forward", "backward"], ["direction"], "medium", "forward/back"),
    (["inside", "outside", "interior", "exterior"], ["direction"], "medium", "in/out"),
]

# POS-based tag suggestions
POS_TAG_SUGGESTIONS = {
    "verb-godan": ["action"],
    "verb-ichidan": ["action"],
    "verb-suru": ["action"],
    "counter": ["number"],
    "interjection": ["communication", "greeting"],
    "conjunction": ["grammar"],
    "particle": ["grammar"],
}


def strip_furigana(text: str) -> str:
    """Remove furigana markup from text."""
    return re.sub(r"\{([^|]+)\|[^}]+\}", r"\1", text)


def get_all_text(entry: dict) -> str:
    """Get all searchable text from an entry."""
    texts = []

    # Gloss
    gloss = entry.get("gloss", "")
    if gloss:
        texts.append(gloss)

    # Definitions
    for defn in entry.get("definitions", []):
        if defn.get("gloss"):
            texts.append(defn["gloss"])
        if defn.get("explanation"):
            texts.append(defn["explanation"])

    # Notes
    notes = entry.get("notes", "")
    if notes:
        texts.append(notes)

    return " ".join(texts).lower()


def suggest_tags_for_entry(entry: dict) -> list[tuple[list[str], str, str]]:
    """
    Suggest semantic tags for an entry.

    Returns list of (tags, confidence, reason) tuples.
    """
    suggestions = []
    all_text = get_all_text(entry)

    # Check keyword patterns
    for keywords, tags, confidence, description in DEFINITION_KEYWORDS:
        for keyword in keywords:
            if keyword.lower() in all_text:
                suggestions.append((tags, confidence, f"keyword '{keyword}' ({description})"))
                break  # Only match once per pattern group

    # Check POS-based suggestions
    pos_tags = entry.get("metadata", {}).get("tags", {}).get("pos", [])
    for pos in pos_tags:
        if pos in POS_TAG_SUGGESTIONS:
            suggestions.append((POS_TAG_SUGGESTIONS[pos], "low", f"POS-based ({pos})"))

    # Deduplicate and prioritize
    seen_tags = {}
    for tags, confidence, reason in suggestions:
        for tag in tags:
            conf_order = {"high": 3, "medium": 2, "low": 1}
            if tag not in seen_tags or conf_order[confidence] > conf_order[seen_tags[tag][0]]:
                seen_tags[tag] = (confidence, reason)

    # Convert back to list format, grouped by confidence
    result = []
    for tag, (confidence, reason) in seen_tags.items():
        result.append(([tag], confidence, reason))

    return result


def analyze_untagged_entries(project_root: Path) -> dict:
    """Analyze entries without semantic tags and generate suggestions."""
    entries_dir = project_root / "entries"

    results = {
        "total": 0,
        "tagged": 0,
        "untagged": 0,
        "suggestions": [],
        "by_confidence": {"high": [], "medium": [], "low": []},
        "no_suggestion": [],
    }

    for file_path in sorted(entries_dir.glob("**/*.json")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        results["total"] += 1

        # Check existing semantic tags
        existing = entry.get("metadata", {}).get("tags", {}).get("semantic", [])
        if existing:
            results["tagged"] += 1
            continue

        results["untagged"] += 1

        # Get suggestions
        suggestions = suggest_tags_for_entry(entry)

        if suggestions:
            # Collect all unique tags and their best confidence
            tag_confidence = {}
            for tags, confidence, reason in suggestions:
                for tag in tags:
                    conf_order = {"high": 3, "medium": 2, "low": 1}
                    if tag not in tag_confidence or conf_order[confidence] > conf_order[tag_confidence[tag][0]]:
                        tag_confidence[tag] = (confidence, reason)

            # Determine overall confidence (highest among all tags)
            best_confidence = max(tag_confidence.values(), key=lambda x: {"high": 3, "medium": 2, "low": 1}[x[0]])[0]

            suggestion_entry = {
                "file": str(file_path.relative_to(project_root)),
                "id": entry.get("id", ""),
                "headword": entry.get("headword", ""),
                "gloss": entry.get("gloss", ""),
                "suggested_tags": list(tag_confidence.keys()),
                "confidence": best_confidence,
                "reasons": {tag: reason for tag, (conf, reason) in tag_confidence.items()},
            }

            results["suggestions"].append(suggestion_entry)
            results["by_confidence"][best_confidence].append(suggestion_entry)
        else:
            results["no_suggestion"].append({
                "file": str(file_path.relative_to(project_root)),
                "id": entry.get("id", ""),
                "headword": entry.get("headword", ""),
                "gloss": entry.get("gloss", ""),
            })

    return results


def apply_high_confidence_tags(
    project_root: Path,
    dry_run: bool = True,
    verbose: bool = False
) -> dict:
    """Apply only high-confidence tag suggestions."""
    entries_dir = project_root / "entries"

    stats = {
        "total": 0,
        "tagged": 0,
        "skipped": 0,
        "errors": 0,
        "tag_counts": Counter(),
    }

    for file_path in sorted(entries_dir.glob("**/*.json")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading {file_path}: {e}")
            stats["errors"] += 1
            continue

        stats["total"] += 1

        # Skip if already has semantic tags
        existing = entry.get("metadata", {}).get("tags", {}).get("semantic", [])
        if existing:
            stats["skipped"] += 1
            continue

        # Get high-confidence suggestions
        suggestions = suggest_tags_for_entry(entry)
        high_conf_tags = set()
        for tags, confidence, reason in suggestions:
            if confidence == "high":
                high_conf_tags.update(tags)

        if not high_conf_tags:
            stats["skipped"] += 1
            continue

        stats["tagged"] += 1
        tags_list = sorted(list(high_conf_tags))

        for tag in tags_list:
            stats["tag_counts"][tag] += 1

        if verbose or dry_run:
            hw = entry.get("headword", "")
            gl = entry.get("gloss", "")
            print(f"  {file_path.name}: {hw} ({gl}) -> {tags_list}")

        if not dry_run:
            # Initialize metadata.tags if needed
            if "metadata" not in entry:
                entry["metadata"] = {}
            if "tags" not in entry["metadata"]:
                entry["metadata"]["tags"] = {}

            entry["metadata"]["tags"]["semantic"] = tags_list
            entry["metadata"]["modified"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(entry, f, ensure_ascii=False, indent=2)

    return stats


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Suggest semantic tags for dictionary entries"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output suggestions to JSON file"
    )
    parser.add_argument(
        "--apply-high-confidence",
        action="store_true",
        help="Apply only high-confidence suggestions"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output"
    )
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    if args.apply_high_confidence:
        mode = "DRY RUN" if args.dry_run else "APPLY"
        print(f"High-Confidence Tag Application ({mode})")
        print("=" * 60)

        stats = apply_high_confidence_tags(
            project_root,
            dry_run=args.dry_run,
            verbose=args.verbose
        )

        print("\n" + "=" * 60)
        print("Summary")
        print("-" * 60)
        print(f"Total entries:  {stats['total']}")
        print(f"Tagged:         {stats['tagged']}")
        print(f"Skipped:        {stats['skipped']}")
        print(f"Errors:         {stats['errors']}")

        if stats["tag_counts"]:
            print(f"\nTag distribution:")
            for tag, count in stats["tag_counts"].most_common(20):
                print(f"  {tag}: {count}")

        if args.dry_run and stats["tagged"] > 0:
            print(f"\nTo apply, run without --dry-run")

        return 0

    # Default: analyze and output suggestions
    print("Analyzing entries for semantic tag suggestions...")
    print("=" * 60)

    results = analyze_untagged_entries(project_root)

    print(f"\nTotal entries: {results['total']}")
    print(f"Already tagged: {results['tagged']}")
    print(f"Untagged: {results['untagged']}")
    print(f"\nSuggestion breakdown:")
    print(f"  High confidence: {len(results['by_confidence']['high'])}")
    print(f"  Medium confidence: {len(results['by_confidence']['medium'])}")
    print(f"  Low confidence: {len(results['by_confidence']['low'])}")
    print(f"  No suggestion: {len(results['no_suggestion'])}")

    # Calculate potential coverage
    potential_tagged = results['tagged'] + len(results['suggestions'])
    potential_coverage = potential_tagged / results['total'] * 100 if results['total'] > 0 else 0
    print(f"\nPotential coverage with all suggestions: {potential_coverage:.1f}%")

    high_conf_tagged = results['tagged'] + len(results['by_confidence']['high'])
    high_conf_coverage = high_conf_tagged / results['total'] * 100 if results['total'] > 0 else 0
    print(f"Potential coverage with high-confidence only: {high_conf_coverage:.1f}%")

    if args.output:
        output_path = Path(args.output)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nSuggestions written to: {output_path}")

    if args.verbose:
        print("\n" + "-" * 60)
        print("Sample high-confidence suggestions:")
        for entry in results["by_confidence"]["high"][:10]:
            print(f"  {entry['headword']} ({entry['gloss'][:40]}...)")
            print(f"    Tags: {entry['suggested_tags']}")

        if results["no_suggestion"]:
            print("\n" + "-" * 60)
            print("Sample entries with no suggestions:")
            for entry in results["no_suggestion"][:10]:
                print(f"  {entry['headword']} ({entry['gloss'][:60]})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
