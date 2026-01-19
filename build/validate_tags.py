#!/usr/bin/env python3
"""
Validation script for dictionary entry tags.

Validates tag consistency across all entries:
- Checks all tags are from valid taxonomy
- Warns on missing tags (entries without semantic tags)
- Checks transitivity only appears on verbs
- Checks for conflicting tags
- Validates verb_class matches pos

Usage:
    python3 build/validate_tags.py [--verbose] [--strict]

Options:
    --verbose    Show all warnings, not just errors
    --strict     Treat warnings as errors (non-zero exit code)
"""

import json
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# Valid tag values from taxonomy
VALID_POS = {
    "noun", "verb-godan", "verb-ichidan", "verb-suru", "verb-kuru",
    "verb-irregular", "adjective-i", "adjective-na", "adjective-no",
    "adjective-taru", "adverb", "particle", "conjunction", "interjection",
    "pronoun", "counter", "prefix", "suffix", "expression",
    "pre-noun-adjectival", "number", "auxiliary", "onomatopoeia"
}

VERB_POS = {"verb-godan", "verb-ichidan", "verb-suru", "verb-kuru", "verb-irregular"}

VALID_TRANSITIVITY = {"transitive", "intransitive", "both", None}

VALID_VERB_CLASS = {
    "godan-u", "godan-ku", "godan-gu", "godan-su", "godan-tsu",
    "godan-nu", "godan-bu", "godan-mu", "godan-ru",
    "ichidan", "suru", "kuru", "irregular", None
}

VALID_FORMALITY = {"formal", "neutral", "informal", "vulgar", None}

VALID_POLITENESS = {"honorific", "humble", "polite", "plain", None}

VALID_STYLE = {"written", "spoken", "literary", "archaic", "slang"}

VALID_DOMAIN = {"business", "academic", "technical", "legal", "medical", "colloquial", "internet"}

# Valid semantic categories from taxonomy
VALID_SEMANTIC = {
    # Time
    "time-day-of-week", "time-month", "time-season", "time-period", "time-general",
    # Nature
    "animal-mammal", "animal-bird", "animal-fish", "animal-insect", "animal-general",
    "plant-tree", "plant-flower", "plant-general", "weather", "geography",
    # Human
    "body-part", "body-internal", "family", "occupation", "person",
    # Abstract
    "emotion", "color", "number", "direction", "size", "quantity",
    # Objects
    "food", "clothing", "building", "transportation", "tool", "furniture", "electronics",
    # Actions
    "movement", "communication", "cognition", "existence", "creation", "consumption",
    # Social
    "greeting", "education", "work", "leisure",
    # Special
    "proverb", "idiom",
    # Linguistic fallback categories (Phase 5)
    "general", "action", "descriptive", "grammatical", "expression", "onomatopoeia"
}

# Verb class must match POS
VERB_CLASS_POS_MAPPING = {
    "godan-u": "verb-godan",
    "godan-ku": "verb-godan",
    "godan-gu": "verb-godan",
    "godan-su": "verb-godan",
    "godan-tsu": "verb-godan",
    "godan-nu": "verb-godan",
    "godan-bu": "verb-godan",
    "godan-mu": "verb-godan",
    "godan-ru": "verb-godan",
    "ichidan": "verb-ichidan",
    "suru": "verb-suru",
    "kuru": "verb-kuru",
    "irregular": "verb-irregular",
}


@dataclass
class TagValidationResult:
    """Result of tag validation."""
    total_entries: int = 0
    entries_with_tags: int = 0
    errors: list[tuple[Path, str]] = field(default_factory=list)
    warnings: list[tuple[Path, str]] = field(default_factory=list)


def validate_entry_tags(entry: dict, file_path: Path) -> tuple[list[str], list[str]]:
    """
    Validate tags for a single entry.

    Returns:
        Tuple of (errors, warnings)
    """
    errors = []
    warnings = []

    metadata = entry.get("metadata", {})
    tags = metadata.get("tags")

    if tags is None:
        # No tags yet - this is expected during migration
        return errors, warnings

    # Validate pos
    pos_tags = tags.get("pos", [])
    if pos_tags:
        for pos in pos_tags:
            if pos not in VALID_POS:
                errors.append(f"Invalid pos tag: '{pos}'")

    # Check if entry has verb POS
    has_verb_pos = any(p in VERB_POS for p in pos_tags)

    # Validate transitivity
    transitivity = tags.get("transitivity")
    if transitivity is not None:
        if transitivity not in VALID_TRANSITIVITY:
            errors.append(f"Invalid transitivity value: '{transitivity}'")
        if not has_verb_pos:
            errors.append(f"transitivity '{transitivity}' specified but entry has no verb POS tags")
    elif has_verb_pos:
        # Verb without transitivity - this is a warning, not error
        warnings.append("Verb entry missing transitivity tag")

    # Validate verb_class
    verb_class = tags.get("verb_class")
    if verb_class is not None:
        if verb_class not in VALID_VERB_CLASS:
            errors.append(f"Invalid verb_class value: '{verb_class}'")
        elif not has_verb_pos:
            errors.append(f"verb_class '{verb_class}' specified but entry has no verb POS tags")
        else:
            # Check verb_class matches POS
            expected_pos = VERB_CLASS_POS_MAPPING.get(verb_class)
            if expected_pos and expected_pos not in pos_tags:
                errors.append(
                    f"verb_class '{verb_class}' doesn't match POS tags {pos_tags} "
                    f"(expected '{expected_pos}')"
                )

    # Validate formality
    formality = tags.get("formality")
    if formality is not None and formality not in VALID_FORMALITY:
        errors.append(f"Invalid formality value: '{formality}'")

    # Validate politeness
    politeness = tags.get("politeness")
    if politeness is not None and politeness not in VALID_POLITENESS:
        errors.append(f"Invalid politeness value: '{politeness}'")

    # Validate style
    style = tags.get("style", [])
    if style:
        for s in style:
            if s not in VALID_STYLE:
                errors.append(f"Invalid style tag: '{s}'")

    # Validate domain
    domain = tags.get("domain", [])
    if domain:
        for d in domain:
            if d not in VALID_DOMAIN:
                errors.append(f"Invalid domain tag: '{d}'")

    # Validate semantic
    semantic = tags.get("semantic", [])
    if semantic:
        for s in semantic:
            if s not in VALID_SEMANTIC:
                warnings.append(f"Unknown semantic tag: '{s}' (may be valid, check taxonomy)")
    else:
        # No semantic tags - this is a warning for concrete entries
        pos_types = set(pos_tags)
        if pos_types & {"noun", "counter"}:
            warnings.append("Noun/counter entry missing semantic tags")

    # Check for conflicting tags
    if formality == "vulgar" and politeness in ("honorific", "humble", "polite"):
        errors.append(f"Conflicting tags: formality='vulgar' with politeness='{politeness}'")

    if formality == "formal" and politeness == "plain":
        warnings.append("Unusual combination: formality='formal' with politeness='plain'")

    return errors, warnings


def validate_all_tags(project_root: Path) -> TagValidationResult:
    """
    Validate tags for all entries.

    Returns:
        TagValidationResult with counts and issues
    """
    entries_dir = project_root / "entries"
    result = TagValidationResult()

    for file_path in entries_dir.glob("**/*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            result.errors.append((file_path, f"Failed to read entry: {e}"))
            continue

        result.total_entries += 1

        # Check if entry has tags
        metadata = entry.get("metadata", {})
        if metadata.get("tags"):
            result.entries_with_tags += 1

        # Validate tags
        errors, warnings = validate_entry_tags(entry, file_path)

        for error in errors:
            result.errors.append((file_path, error))
        for warning in warnings:
            result.warnings.append((file_path, warning))

    return result


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate dictionary entry tags")
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show all warnings, not just errors"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (non-zero exit code)"
    )
    parser.add_argument(
        "--entry", "-e",
        type=str,
        help="Validate a single entry by path or ID"
    )
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Single entry mode
    if args.entry:
        entry_path = Path(args.entry)
        if not entry_path.is_absolute():
            # Try as ID first
            entries_dir = project_root / "entries"
            found = list(entries_dir.glob(f"**/{args.entry}.json"))
            if found:
                entry_path = found[0]
            else:
                entry_path = project_root / args.entry

        if not entry_path.exists():
            print(f"Error: Entry not found: {args.entry}")
            return 1

        try:
            with open(entry_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading entry: {e}")
            return 1

        errors, warnings = validate_entry_tags(entry, entry_path)

        if errors:
            print(f"Errors in {entry_path.name}:")
            for error in errors:
                print(f"  - {error}")

        if warnings and args.verbose:
            print(f"Warnings in {entry_path.name}:")
            for warning in warnings:
                print(f"  - {warning}")

        if not errors and not warnings:
            print(f"Tags are valid in {entry_path.name}")

        if errors or (args.strict and warnings):
            return 1
        return 0

    # Full validation mode
    print(f"Validating tags in {project_root}")
    print("-" * 50)

    result = validate_all_tags(project_root)

    # Summary
    print(f"\nTotal entries: {result.total_entries}")
    print(f"Entries with tags: {result.entries_with_tags}")
    print(f"Tag coverage: {result.entries_with_tags / result.total_entries * 100:.1f}%")

    # Report errors
    if result.errors:
        print(f"\nErrors ({len(result.errors)}):")
        # Group by file
        by_file = defaultdict(list)
        for file_path, error in result.errors:
            by_file[file_path].append(error)

        for file_path, errors in sorted(by_file.items()):
            rel_path = file_path.relative_to(project_root)
            print(f"\n  {rel_path}:")
            for error in errors:
                print(f"    - {error}")

    # Report warnings if verbose
    if args.verbose and result.warnings:
        print(f"\nWarnings ({len(result.warnings)}):")
        # Group by file, but limit output
        by_file = defaultdict(list)
        for file_path, warning in result.warnings:
            by_file[file_path].append(warning)

        shown = 0
        for file_path, warnings in sorted(by_file.items()):
            if shown >= 20:
                remaining = len(by_file) - 20
                print(f"\n  ... and {remaining} more files with warnings")
                break
            rel_path = file_path.relative_to(project_root)
            print(f"\n  {rel_path}:")
            for warning in warnings[:3]:
                print(f"    - {warning}")
            if len(warnings) > 3:
                print(f"    ... and {len(warnings) - 3} more warnings")
            shown += 1
    elif result.warnings:
        print(f"\nWarnings: {len(result.warnings)} (use --verbose to see details)")

    print(f"\nValidation complete.")

    if result.errors or (args.strict and result.warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
