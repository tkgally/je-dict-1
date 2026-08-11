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
import re
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
    "general", "action", "descriptive", "grammatical", "expression", "onomatopoeia",
    # Established-by-usage categories blessed 2026-06-11 (curator tag-policy
    # decision: each had 100+ uses in the dictionary; see
    # planning/wiki/topics/schema-tag-reliability.md). Out-of-list tags remain
    # warnings; near-duplicates and the long tail are migrated gradually via
    # build/check_tag_drift.py --check unknown-semantic.
    "business", "culture", "abstract", "nature", "daily-life", "society",
    "health", "technology", "science", "politics", "personality", "sports",
    "evaluation", "language", "law", "travel", "religion", "history",
    "finance", "appearance", "money", "music", "cooking", "change",
    "media", "shopping", "entertainment", "art", "military", "economics",
    # Proper-noun categories (curator policy change 2026-08-11: proper nouns
    # that learners should know — collocationally and semantically rich place
    # names, personal names, organizations, works, events, brands — are in
    # scope; see the find-candidates and entry-guidelines skills). Every
    # proper-noun entry carries the "proper-noun" umbrella tag PLUS at least
    # one specific category; validate_entry_tags() enforces the pairing.
    "proper-noun", "place-name", "person-name", "organization-name",
    "work-name", "event-name", "brand-name",
}

# Specific proper-noun categories. Entries with any of these must also carry
# the "proper-noun" umbrella tag (hard error); "proper-noun" without a
# specific category is a warning. An entry may carry more than one category
# when genuinely appropriate (e.g. 甲子園 is both a place and, by metonymy,
# the event held there).
PROPER_NOUN_SUBTAGS = {
    "place-name", "person-name", "organization-name",
    "work-name", "event-name", "brand-name",
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
        # Proper-noun pairing: a specific category requires the umbrella tag,
        # and the umbrella tag should name a specific category.
        sem_set = set(semantic)
        subcats = sem_set & PROPER_NOUN_SUBTAGS
        if subcats and "proper-noun" not in sem_set:
            errors.append(
                f"Proper-noun category tag(s) {sorted(subcats)} require the "
                f"'proper-noun' umbrella tag"
            )
        if "proper-noun" in sem_set and not subcats:
            warnings.append(
                "'proper-noun' tag has no specific category "
                "(place-name, person-name, organization-name, work-name, "
                "event-name, brand-name)"
            )
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


# ---------------------------------------------------------------------------
# Off-vocabulary semantic-tag ratchet
#
# VALID_SEMANTIC is a controlled vocabulary, but ~6,700 legacy entries carry
# semantic tags outside it (1,100+ distinct values). Per the 2026-06-11 tag
# policy these stay warnings and are migrated gradually (build/check_tag_drift.py
# --check unknown-semantic). That left a gap: a NEW entry or edit could introduce
# yet another off-vocab tag and nothing — not validate.py, not CI — would fail.
#
# The ratchet closes that gap without forcing a mass migration. A baseline file
# records every off-vocab tag each entry already carries; `--check-no-new-unknown`
# (run in CI) fails only when an entry gains an off-vocab tag absent from the
# baseline. The tolerated set can therefore only shrink (via migration), never
# grow. Regenerate the baseline after a migration with `--write-unknown-baseline`.
# ---------------------------------------------------------------------------

DEFAULT_UNKNOWN_BASELINE = "build/data/unknown_semantic_baseline.json"


def _id_from_relpath(relpath: str) -> str:
    """Pull the 5-digit entry ID out of an entries/.../NNNNN_*.json path."""
    m = re.search(r"/(\d{5})_", "/" + relpath.replace("\\", "/"))
    return m.group(1) if m else relpath


def collect_unknown_semantic(project_root: Path) -> dict:
    """Map entry file (relative path) -> sorted off-vocabulary semantic tags.

    Keyed by file path rather than entry ID so duplicate-ID entries are tracked
    independently. Only entries with at least one off-vocab semantic tag appear.
    """
    entries_dir = project_root / "entries"
    out = {}
    for file_path in sorted(entries_dir.glob("**/*.json")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue
        semantic = ((entry.get("metadata") or {}).get("tags") or {}).get("semantic") or []
        unknown = sorted({s for s in semantic if s not in VALID_SEMANTIC})
        if unknown:
            out[str(file_path.relative_to(project_root))] = unknown
    return out


def write_unknown_baseline(project_root: Path, baseline_path: Path) -> int:
    """Regenerate the off-vocab semantic-tag baseline from the current entries."""
    data = collect_unknown_semantic(project_root)
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "_comment": (
            "Ratchet baseline for off-vocabulary (not-in-VALID_SEMANTIC) semantic "
            "tags. Maps entry file path -> the off-vocab semantic tags it already "
            "carried when generated. `build/validate_tags.py --check-no-new-unknown` "
            "(run in CI) fails if any entry gains an off-vocab tag absent from its "
            "list here, so the off-vocab set can only shrink via gradual migration, "
            "never grow. Regenerate after a migration: "
            "python3 build/validate_tags.py --write-unknown-baseline"
        ),
        "tags": data,
    }
    with open(baseline_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    total = sum(len(v) for v in data.values())
    print(f"Wrote {baseline_path.relative_to(project_root)}: "
          f"{len(data)} entries, {total} tolerated off-vocab semantic-tag use(s).")
    return 0


def check_no_new_unknown(project_root: Path, baseline_path: Path) -> int:
    """CI gate: fail if any entry carries an off-vocab tag not in the baseline."""
    if not baseline_path.exists():
        print(f"error: baseline not found: {baseline_path}", file=sys.stderr)
        print("Generate it with: python3 build/validate_tags.py --write-unknown-baseline",
              file=sys.stderr)
        return 3
    try:
        with open(baseline_path, "r", encoding="utf-8") as f:
            baseline = (json.load(f) or {}).get("tags", {})
    except (json.JSONDecodeError, IOError) as e:
        print(f"error: cannot read baseline {baseline_path}: {e}", file=sys.stderr)
        return 3

    current = collect_unknown_semantic(project_root)
    violations = []  # (relpath, tag)
    for relpath, tags in sorted(current.items()):
        tolerated = set(baseline.get(relpath, []))
        for tag in tags:
            if tag not in tolerated:
                violations.append((relpath, tag))

    if not violations:
        print(f"No new off-vocabulary semantic tags. ({len(current)} entries still "
              "carry baselined off-vocab tags — migrate with "
              "build/check_tag_drift.py --check unknown-semantic.)")
        return 0

    # Optional 1:1 migration hints, reusing check_tag_drift's map if importable.
    try:
        from check_tag_drift import TAG_MIGRATION
    except Exception:
        TAG_MIGRATION = {}

    print(f"ERROR: {len(violations)} off-vocabulary semantic tag(s) not in the "
          "baseline (introduced by this change):\n")
    for relpath, tag in violations:
        suggested = TAG_MIGRATION.get(tag)
        hint = f"  (try '{suggested}')" if suggested else ""
        print(f"  {_id_from_relpath(relpath)} ({relpath}): "
              f"semantic tag '{tag}' is not in VALID_SEMANTIC{hint}")
    print("\nSemantic tags must come from VALID_SEMANTIC in build/validate_tags.py.")
    print("Fix one of these ways:")
    print("  - use an in-list tag, or migrate via build/check_tag_drift.py "
          "(--check unknown-semantic prints 1:1 targets); or")
    print("  - if the curator has blessed a new tag, add it to VALID_SEMANTIC and "
          "regenerate the baseline (python3 build/validate_tags.py --write-unknown-baseline).")
    return 1


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
    parser.add_argument(
        "--write-unknown-baseline",
        action="store_true",
        help="Regenerate build/data/unknown_semantic_baseline.json from the current entries and exit"
    )
    parser.add_argument(
        "--check-no-new-unknown",
        action="store_true",
        help="Fail (exit 1) if any entry carries an off-vocabulary semantic tag absent from the baseline (regression gate; run in CI)"
    )
    parser.add_argument(
        "--baseline",
        type=str,
        default=None,
        help=f"Path to the off-vocab semantic-tag baseline (default: {DEFAULT_UNKNOWN_BASELINE})"
    )
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Off-vocabulary semantic-tag ratchet (independent of the schema/tag checks
    # below, so it stays green even while pre-existing verb_class errors exist).
    baseline_path = (Path(args.baseline) if args.baseline
                     else project_root / DEFAULT_UNKNOWN_BASELINE)
    if args.write_unknown_baseline:
        return write_unknown_baseline(project_root, baseline_path)
    if args.check_no_new_unknown:
        return check_no_new_unknown(project_root, baseline_path)

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
