#!/usr/bin/env python3
"""
Migration script for part_of_speech standardization.

Maps old part_of_speech strings to canonical metadata.tags.pos arrays.
Also extracts transitivity information from verb part_of_speech strings.

Usage:
    python3 build/migrate_pos.py --dry-run    # Show proposed changes
    python3 build/migrate_pos.py --apply      # Write changes to files
    python3 build/migrate_pos.py --analyze    # Analyze current part_of_speech values

Options:
    --dry-run   Show what would be changed without modifying files
    --apply     Apply changes to entry files
    --analyze   List all unique part_of_speech values and their frequencies
    --verbose   Show detailed output for each entry
"""

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# Comprehensive mapping from current part_of_speech strings to canonical pos tags
# This handles all known variations including spacing, punctuation, and word order
POS_MAPPING = {
    # Simple nouns
    "noun": ["noun"],
    "nouns": ["noun"],

    # Noun + suru verb combinations (many variations)
    "noun, suru verb": ["noun", "verb-suru"],
    "noun, suru-verb": ["noun", "verb-suru"],
    "noun/suru verb": ["noun", "verb-suru"],
    "noun/suru-verb": ["noun", "verb-suru"],
    "noun / suru verb": ["noun", "verb-suru"],
    "noun / suru-verb": ["noun", "verb-suru"],
    "noun; suru verb": ["noun", "verb-suru"],
    "noun; suru-verb": ["noun", "verb-suru"],
    "noun (suru verb)": ["noun", "verb-suru"],
    "noun (verbal)": ["noun", "verb-suru"],
    "noun, verb (suru)": ["noun", "verb-suru"],
    "noun; verb (suru)": ["noun", "verb-suru"],
    "noun / verb (suru)": ["noun", "verb-suru"],
    "noun, する-verb": ["noun", "verb-suru"],
    "suru verb": ["verb-suru"],
    "suru-verb": ["verb-suru"],
    "verb (suru)": ["verb-suru"],
    "suru verb, intransitive": ["verb-suru"],
    "suru verb, transitive": ["verb-suru"],
    "verbal noun": ["noun", "verb-suru"],

    # Godan verbs
    "verb (godan)": ["verb-godan"],
    "godan verb": ["verb-godan"],
    "verb (godan, transitive)": ["verb-godan"],
    "verb (godan, intransitive)": ["verb-godan"],
    "godan verb, transitive": ["verb-godan"],
    "godan verb, intransitive": ["verb-godan"],
    "godan verb, intransitive/transitive": ["verb-godan"],
    "verb godan": ["verb-godan"],
    "verb-godan": ["verb-godan"],

    # Ichidan verbs
    "verb (ichidan)": ["verb-ichidan"],
    "ichidan verb": ["verb-ichidan"],
    "verb (ichidan, transitive)": ["verb-ichidan"],
    "verb (ichidan, intransitive)": ["verb-ichidan"],
    "ichidan verb, transitive": ["verb-ichidan"],
    "ichidan verb, intransitive": ["verb-ichidan"],
    "ichidan verb, transitive/intransitive": ["verb-ichidan"],
    "verb ichidan": ["verb-ichidan"],
    "verb-ichidan": ["verb-ichidan"],

    # Irregular verbs
    "verb (irregular)": ["verb-irregular"],
    "irregular verb": ["verb-irregular"],

    # I-adjectives
    "i-adjective": ["adjective-i"],
    "adjective (i-adjective)": ["adjective-i"],
    "i adjective": ["adjective-i"],
    "イ形容詞": ["adjective-i"],

    # Na-adjectives
    "na-adjective": ["adjective-na"],
    "adjective (na-adjective)": ["adjective-na"],
    "な-adjective": ["adjective-na"],
    "na adjective": ["adjective-na"],
    "ナ形容詞": ["adjective-na"],

    # Na-adjective combinations
    "na-adjective, noun": ["adjective-na", "noun"],
    "noun, na-adjective": ["noun", "adjective-na"],
    "na-adjective/noun": ["adjective-na", "noun"],
    "noun/na-adjective": ["noun", "adjective-na"],
    "adverb, na-adjective": ["adverb", "adjective-na"],
    "na-adjective, adverb": ["adjective-na", "adverb"],

    # No-adjective (pre-noun adjectival)
    "no-adjective": ["adjective-no"],
    "pre-noun adjectival": ["pre-noun-adjectival"],
    "pre-noun adjective": ["pre-noun-adjectival"],
    "prenominal": ["pre-noun-adjectival"],
    "noun, no-adjective": ["noun", "adjective-no"],
    "noun / no-adjective": ["noun", "adjective-no"],
    "noun/no-adjective": ["noun", "adjective-no"],
    "noun, の-adjective": ["noun", "adjective-no"],
    "の-adjective": ["adjective-no"],
    "adverb, no-adjective": ["adverb", "adjective-no"],

    # Taru-adjectives
    "taru-adjective": ["adjective-taru"],
    "adjective (taru)": ["adjective-taru"],

    # Generic verb (unspecified type - treat as godan for migration)
    "verb": ["verb-godan"],

    # Adverbs
    "adverb": ["adverb"],
    "adverbs": ["adverb"],
    "adverb, suru verb": ["adverb", "verb-suru"],
    "adverb/suru verb": ["adverb", "verb-suru"],
    "adverb, verb (suru)": ["adverb", "verb-suru"],
    "adverb; verb (suru)": ["adverb", "verb-suru"],
    "adverb / verb (suru)": ["adverb", "verb-suru"],

    # Particles
    "particle": ["particle"],
    "particles": ["particle"],

    # Conjunctions
    "conjunction": ["conjunction"],
    "conjunctions": ["conjunction"],

    # Interjections
    "interjection": ["interjection"],
    "interjections": ["interjection"],

    # Pronouns
    "pronoun": ["pronoun"],
    "pronouns": ["pronoun"],

    # Counters
    "counter": ["counter"],
    "counters": ["counter"],

    # Prefixes and suffixes
    "prefix": ["prefix"],
    "suffix": ["suffix"],

    # Expressions
    "expression": ["expression"],
    "expressions": ["expression"],
    "expression (proverb)": ["expression"],
    "expression, proverb": ["expression"],
    "expression, verb phrase": ["expression"],
    "phrase": ["expression"],
    "four-character idiom": ["expression"],
    "yojijukugo": ["expression"],
    "proverb": ["expression"],
    "grammar pattern": ["expression"],

    # Numbers
    "number": ["number"],
    "numeral": ["number"],

    # Auxiliary
    "auxiliary": ["auxiliary"],
    "auxiliary verb": ["auxiliary"],
    "auxiliary adjective": ["auxiliary"],

    # Generic adjective (unspecified type)
    "adjective": ["adjective-i"],
    "adjectival noun": ["adjective-na"],

    # Onomatopoeia
    "onomatopoeia": ["onomatopoeia"],
    "mimetic": ["onomatopoeia"],
    "adverb; noun (onomatopoeia)": ["adverb", "noun", "onomatopoeia"],

    # Complex combinations
    "noun, suru-verb, no-adjective": ["noun", "verb-suru", "adjective-no"],
    "noun, suru verb, no-adjective": ["noun", "verb-suru", "adjective-no"],
    "noun; particle": ["noun", "particle"],
    "noun, particle": ["noun", "particle"],
    "noun / suru-verb": ["noun", "verb-suru"],
    "noun, adverbial noun": ["noun", "adverb"],
    "noun / noun-prefix": ["noun", "prefix"],
    "interjection, noun, internet slang": ["interjection", "noun"],
    "noun; adverb (と); na-adjective": ["noun", "adverb", "adjective-na"],
    "adverb, たる-adjective, の-adjective": ["adverb", "adjective-taru", "adjective-no"],
}

# Patterns to extract transitivity from part_of_speech
TRANSITIVITY_PATTERNS = [
    (r"\btransitive\b", "transitive"),
    (r"\bintransitive\b", "intransitive"),
    (r"\b他動詞\b", "transitive"),
    (r"\b自動詞\b", "intransitive"),
]


def normalize_pos_string(pos: str) -> str:
    """Normalize a part_of_speech string for matching."""
    # Convert to lowercase
    normalized = pos.lower().strip()
    # Normalize whitespace
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


def extract_transitivity(pos: str) -> Optional[str]:
    """Extract transitivity from part_of_speech string."""
    pos_lower = pos.lower()
    for pattern, value in TRANSITIVITY_PATTERNS:
        if re.search(pattern, pos_lower):
            return value
    return None


def map_pos_to_tags(pos: str) -> tuple[list[str], Optional[str], bool]:
    """
    Map a part_of_speech string to canonical tags.

    Returns:
        Tuple of (pos_tags, transitivity, mapped)
        - pos_tags: List of canonical POS tags
        - transitivity: Extracted transitivity or None
        - mapped: Whether the mapping was found (False = needs manual review)
    """
    normalized = normalize_pos_string(pos)
    transitivity = extract_transitivity(pos)

    # Try exact match first
    if normalized in POS_MAPPING:
        return POS_MAPPING[normalized], transitivity, True

    # Try without parenthetical content
    simplified = re.sub(r"\s*\([^)]*\)\s*", " ", normalized).strip()
    simplified = re.sub(r"\s+", " ", simplified)
    if simplified in POS_MAPPING:
        return POS_MAPPING[simplified], transitivity, True

    # Try matching individual components
    # Split on common separators
    components = re.split(r"[,;/]", normalized)
    components = [c.strip() for c in components if c.strip()]

    if len(components) > 1:
        result_tags = []
        all_mapped = True
        for component in components:
            if component in POS_MAPPING:
                for tag in POS_MAPPING[component]:
                    if tag not in result_tags:
                        result_tags.append(tag)
            else:
                all_mapped = False

        if result_tags and all_mapped:
            return result_tags, transitivity, True

    return [], transitivity, False


def analyze_pos_values(project_root: Path) -> dict:
    """Analyze all unique part_of_speech values in the dictionary."""
    entries_dir = project_root / "entries"
    pos_counter = Counter()
    unmapped = defaultdict(list)

    for file_path in entries_dir.glob("**/*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        pos = entry.get("part_of_speech", "")
        if pos:
            pos_counter[pos] += 1

            # Check if it maps
            tags, _, mapped = map_pos_to_tags(pos)
            if not mapped:
                unmapped[pos].append(file_path.name)

    return {
        "counts": pos_counter,
        "unmapped": unmapped,
    }


def migrate_entry(entry: dict) -> tuple[dict, dict]:
    """
    Migrate a single entry's part_of_speech to tags.

    Returns:
        Tuple of (modified_entry, changes_dict)
    """
    changes = {}
    pos = entry.get("part_of_speech", "")

    if not pos:
        return entry, changes

    # Map to tags
    pos_tags, transitivity, mapped = map_pos_to_tags(pos)

    if not mapped:
        changes["unmapped"] = pos
        return entry, changes

    # Initialize metadata.tags if needed
    if "metadata" not in entry:
        entry["metadata"] = {}
    if "tags" not in entry["metadata"]:
        entry["metadata"]["tags"] = {}

    # Set pos tags
    if pos_tags:
        entry["metadata"]["tags"]["pos"] = pos_tags
        changes["pos"] = pos_tags

    # Set transitivity for verbs
    has_verb = any(p.startswith("verb-") for p in pos_tags)
    if has_verb and transitivity:
        entry["metadata"]["tags"]["transitivity"] = transitivity
        changes["transitivity"] = transitivity

    # Update modified timestamp
    entry["metadata"]["modified"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    return entry, changes


def migrate_all_entries(
    project_root: Path,
    dry_run: bool = True,
    verbose: bool = False
) -> dict:
    """
    Migrate all entries to use canonical POS tags.

    Returns:
        Dictionary with migration statistics
    """
    entries_dir = project_root / "entries"

    stats = {
        "total": 0,
        "migrated": 0,
        "already_tagged": 0,
        "unmapped": 0,
        "errors": 0,
        "unmapped_values": defaultdict(list),
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

        # Check if already has pos tags
        existing_tags = entry.get("metadata", {}).get("tags", {})
        if existing_tags.get("pos"):
            stats["already_tagged"] += 1
            if verbose:
                print(f"  Skip (already tagged): {file_path.name}")
            continue

        # Migrate
        migrated_entry, changes = migrate_entry(entry)

        if "unmapped" in changes:
            stats["unmapped"] += 1
            stats["unmapped_values"][changes["unmapped"]].append(file_path.name)
            if verbose:
                print(f"  Unmapped: {file_path.name} - '{changes['unmapped']}'")
            continue

        if not changes:
            continue

        stats["migrated"] += 1

        if verbose or dry_run:
            rel_path = file_path.relative_to(project_root)
            print(f"  {rel_path}: {entry.get('part_of_speech')} -> {changes}")

        # Write if not dry run
        if not dry_run:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(migrated_entry, f, ensure_ascii=False, indent=2)

    return stats


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Migrate part_of_speech to canonical tags"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes to entry files"
    )
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="Analyze current part_of_speech values"
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

    # Validate arguments
    if not (args.dry_run or args.apply or args.analyze):
        print("Error: Must specify --dry-run, --apply, or --analyze")
        parser.print_help()
        return 1

    if args.analyze:
        print("Analyzing part_of_speech values...")
        print("-" * 50)

        analysis = analyze_pos_values(project_root)

        print(f"\nUnique part_of_speech values ({len(analysis['counts'])} total):\n")

        # Sort by frequency
        for pos, count in analysis["counts"].most_common():
            tags, trans, mapped = map_pos_to_tags(pos)
            status = "✓" if mapped else "✗"
            tag_str = f" -> {tags}" if mapped else " [UNMAPPED]"
            trans_str = f" (trans={trans})" if trans else ""
            print(f"  {status} [{count:4d}] {pos}{tag_str}{trans_str}")

        if analysis["unmapped"]:
            print(f"\n\nUnmapped values ({len(analysis['unmapped'])} unique):")
            for pos, files in sorted(analysis["unmapped"].items()):
                print(f"\n  '{pos}' ({len(files)} entries)")
                for f in files[:3]:
                    print(f"    - {f}")
                if len(files) > 3:
                    print(f"    ... and {len(files) - 3} more")

        return 0

    # Migration mode
    mode = "DRY RUN" if args.dry_run else "APPLY"
    print(f"POS Migration Script ({mode})")
    print("=" * 50)
    print(f"Project root: {project_root}\n")

    stats = migrate_all_entries(
        project_root,
        dry_run=args.dry_run,
        verbose=args.verbose
    )

    print("\n" + "=" * 50)
    print("Migration Summary")
    print("-" * 50)
    print(f"Total entries:     {stats['total']}")
    print(f"Already tagged:    {stats['already_tagged']}")
    print(f"Migrated:          {stats['migrated']}")
    print(f"Unmapped:          {stats['unmapped']}")
    print(f"Errors:            {stats['errors']}")

    if stats["unmapped_values"]:
        print(f"\nUnmapped part_of_speech values ({len(stats['unmapped_values'])} unique):")
        for pos, files in sorted(stats["unmapped_values"].items()):
            print(f"  '{pos}' ({len(files)} entries)")

        print("\nTo fix, add mappings to POS_MAPPING in this script.")

    if args.dry_run and stats["migrated"] > 0:
        print(f"\nTo apply these changes, run: python3 {sys.argv[0]} --apply")

    return 0 if stats["unmapped"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
