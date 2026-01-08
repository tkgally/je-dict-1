#!/usr/bin/env python3
"""
Validation script for je-dict-1 dictionary entries.

Validates all entry files against the JSON schema and checks additional
consistency rules (filename format, directory placement, ID uniqueness).
"""

import json
import sys
import re
from pathlib import Path
from typing import Optional

try:
    import jsonschema
    from jsonschema import Draft7Validator
except ImportError:
    print("Error: jsonschema package required. Install with: pip install jsonschema")
    sys.exit(1)


# Mapping from hiragana to romaji for filename validation
HIRAGANA_TO_ROMAJI = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n',
    # Small kana
    'ゃ': 'ya', 'ゅ': 'yu', 'ょ': 'yo',
    'っ': '',  # Will be handled specially
    'ー': '',  # Long vowel mark - context dependent
}

# Combination mappings (e.g., きゃ -> kya)
COMBO_MAPPINGS = {
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
}

# Directory mapping from first kana
KANA_TO_DIRECTORY = {
    'あ': 'a', 'い': 'a', 'う': 'a', 'え': 'a', 'お': 'a',
    'か': 'ka', 'き': 'ka', 'く': 'ka', 'け': 'ka', 'こ': 'ka',
    'が': 'ka', 'ぎ': 'ka', 'ぐ': 'ka', 'げ': 'ka', 'ご': 'ka',
    'さ': 'sa', 'し': 'sa', 'す': 'sa', 'せ': 'sa', 'そ': 'sa',
    'ざ': 'sa', 'じ': 'sa', 'ず': 'sa', 'ぜ': 'sa', 'ぞ': 'sa',
    'た': 'ta', 'ち': 'ta', 'つ': 'ta', 'て': 'ta', 'と': 'ta',
    'だ': 'ta', 'ぢ': 'ta', 'づ': 'ta', 'で': 'ta', 'ど': 'ta',
    'な': 'na', 'に': 'na', 'ぬ': 'na', 'ね': 'na', 'の': 'na',
    'は': 'ha', 'ひ': 'ha', 'ふ': 'ha', 'へ': 'ha', 'ほ': 'ha',
    'ば': 'ha', 'び': 'ha', 'ぶ': 'ha', 'べ': 'ha', 'ぼ': 'ha',
    'ぱ': 'ha', 'ぴ': 'ha', 'ぷ': 'ha', 'ぺ': 'ha', 'ぽ': 'ha',
    'ま': 'ma', 'み': 'ma', 'む': 'ma', 'め': 'ma', 'も': 'ma',
    'や': 'ya', 'ゆ': 'ya', 'よ': 'ya',
    'ら': 'ra', 'り': 'ra', 'る': 'ra', 'れ': 'ra', 'ろ': 'ra',
    'わ': 'wa', 'を': 'wa', 'ん': 'wa',
}


def hiragana_to_romaji(reading: str) -> str:
    """Convert hiragana reading to romaji."""
    result = []
    i = 0
    while i < len(reading):
        # Check for two-character combinations first
        if i + 1 < len(reading):
            combo = reading[i:i+2]
            if combo in COMBO_MAPPINGS:
                result.append(COMBO_MAPPINGS[combo])
                i += 2
                continue

        char = reading[i]

        # Handle small tsu (gemination)
        if char == 'っ':
            # Double the next consonant
            if i + 1 < len(reading):
                next_char = reading[i + 1]
                if next_char in HIRAGANA_TO_ROMAJI:
                    next_romaji = HIRAGANA_TO_ROMAJI[next_char]
                    if next_romaji:
                        result.append(next_romaji[0])
            i += 1
            continue

        # Handle long vowel mark
        if char == 'ー':
            if result:
                # Repeat the previous vowel
                prev = result[-1]
                if prev and prev[-1] in 'aiueo':
                    result.append(prev[-1])
            i += 1
            continue

        if char in HIRAGANA_TO_ROMAJI:
            result.append(HIRAGANA_TO_ROMAJI[char])
        else:
            # Unknown character, keep as is
            result.append(char)
        i += 1

    return ''.join(result)


def get_expected_directory(reading: str) -> Optional[str]:
    """Get the expected directory for an entry based on its reading."""
    if not reading:
        return None
    first_kana = reading[0]
    return KANA_TO_DIRECTORY.get(first_kana)


def load_schema(schema_path: Path) -> dict:
    """Load the JSON schema."""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_entry_file(file_path: Path, schema: dict, all_ids: set) -> list[str]:
    """
    Validate a single entry file.
    Returns a list of error messages (empty if valid).
    """
    errors = []

    # Load the entry
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]

    # Validate against schema
    validator = Draft7Validator(schema)
    schema_errors = list(validator.iter_errors(entry))
    for error in schema_errors:
        path = ' -> '.join(str(p) for p in error.absolute_path) if error.absolute_path else 'root'
        errors.append(f"Schema error at {path}: {error.message}")

    # If schema validation failed, skip additional checks
    if schema_errors:
        return errors

    # Check ID uniqueness
    entry_id = entry['id']
    if entry_id in all_ids:
        errors.append(f"Duplicate ID: {entry_id}")
    all_ids.add(entry_id)

    # Check filename matches ID
    expected_filename = f"{entry_id}.json"
    if file_path.name != expected_filename:
        errors.append(f"Filename mismatch: expected {expected_filename}, got {file_path.name}")

    # Check directory matches reading
    reading = entry['reading']
    expected_dir = get_expected_directory(reading)
    actual_dir = file_path.parent.name
    if expected_dir and actual_dir != expected_dir:
        errors.append(f"Directory mismatch: entry with reading '{reading}' should be in '{expected_dir}/', not '{actual_dir}/'")

    # Check ID romanization matches reading
    id_parts = entry_id.split('_')
    if len(id_parts) == 2:
        id_romaji = id_parts[0]
        expected_romaji = hiragana_to_romaji(reading)
        if id_romaji != expected_romaji:
            errors.append(f"ID romanization mismatch: '{id_romaji}' doesn't match reading '{reading}' (expected '{expected_romaji}')")

    return errors


def check_for_duplicates(entries_data: list[tuple[Path, dict]]) -> list[tuple[Path, str]]:
    """
    Check for duplicate entries (same reading AND same headword).
    Entries with same reading but different headwords (homophones) are allowed.
    Returns a list of (file_path, error_message) for duplicates.
    """
    # Group entries by reading
    by_reading = {}
    for file_path, entry in entries_data:
        reading = entry.get('reading', '')
        headword = entry.get('headword', '')
        key = (reading, headword)
        if key not in by_reading:
            by_reading[key] = []
        by_reading[key].append(file_path)

    # Find duplicates (same reading AND headword)
    duplicates = []
    for (reading, headword), files in by_reading.items():
        if len(files) > 1:
            # Report all but the first as duplicates
            for dup_file in files[1:]:
                duplicates.append((
                    dup_file,
                    f"Duplicate entry: reading '{reading}' with headword '{headword}' already exists in {files[0]}"
                ))

    return duplicates


def check_cross_references(entries_data: list[tuple[Path, dict]], all_ids: set) -> list[tuple[Path, str]]:
    """
    Check that all cross_references point to existing entry IDs.
    Returns a list of (file_path, error_message) for invalid references.
    """
    errors = []
    for file_path, entry in entries_data:
        cross_refs = entry.get('cross_references', [])
        if cross_refs:
            for ref_id in cross_refs:
                if ref_id not in all_ids:
                    errors.append((
                        file_path,
                        f"Invalid cross_reference: '{ref_id}' does not exist"
                    ))
    return errors


def validate_all_entries(project_root: Path) -> tuple[int, int, list[tuple[Path, list[str]]]]:
    """
    Validate all entry files in the project.
    Returns (total_count, valid_count, list of (file, errors) for invalid files).
    """
    schema_path = project_root / 'build' / 'schema.json'
    schema = load_schema(schema_path)

    entries_dir = project_root / 'entries'

    all_ids = set()
    total = 0
    valid = 0
    invalid_files = []
    entries_data = []  # Store (file_path, entry_data) for duplicate checking

    # Collect all JSON files
    entry_files = list(entries_dir.glob('**/*.json'))

    for file_path in entry_files:
        total += 1
        errors = validate_entry_file(file_path, schema, all_ids)
        if errors:
            invalid_files.append((file_path, errors))
        else:
            valid += 1
            # Load entry data for duplicate checking
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    entry = json.load(f)
                    entries_data.append((file_path, entry))
            except (json.JSONDecodeError, IOError, OSError):
                pass  # Entry already flagged as invalid by validate_entry_file

    # Check for duplicates among valid entries
    duplicate_errors = check_for_duplicates(entries_data)
    for file_path, error_msg in duplicate_errors:
        # Find if this file is already in invalid_files
        existing = next((i for i, (fp, _) in enumerate(invalid_files) if fp == file_path), None)
        if existing is not None:
            invalid_files[existing][1].append(error_msg)
        else:
            invalid_files.append((file_path, [error_msg]))
            valid -= 1

    # Check cross_references point to existing IDs
    # These are tracked separately as warnings (don't prevent build)
    cross_ref_errors = check_cross_references(entries_data, all_ids)

    return total, valid, invalid_files, cross_ref_errors


def validate_single_entry(entry_path: Path, project_root: Path) -> int:
    """
    Validate a single entry file.
    Returns 0 on success, 1 on failure.
    """
    schema_path = project_root / 'build' / 'schema.json'
    schema = load_schema(schema_path)

    # Get all existing IDs for cross-reference checking
    entries_dir = project_root / 'entries'
    all_ids = set()
    for file_path in entries_dir.glob('**/*.json'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)
                all_ids.add(entry.get('id', ''))
        except (json.JSONDecodeError, IOError):
            pass

    print(f"Validating: {entry_path}")
    print("-" * 50)

    errors = validate_entry_file(entry_path, schema, set())  # Don't check ID uniqueness for single entry

    # Check cross-references
    try:
        with open(entry_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)
            cross_refs = entry.get('cross_references', [])
            for ref_id in cross_refs:
                if ref_id not in all_ids:
                    errors.append(f"Invalid cross_reference: '{ref_id}' does not exist")
    except (json.JSONDecodeError, IOError):
        pass  # Already caught by validate_entry_file

    if errors:
        print("Errors found:")
        for error in errors:
            print(f"  - {error}")
        return 1
    else:
        print("Entry is valid!")
        return 0


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Validate dictionary entries')
    parser.add_argument('--entry', '-e', type=str, help='Path to a single entry file to validate')
    parser.add_argument('--id', type=str, help='Entry ID to validate (e.g., taberu_00001)')
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Single entry validation mode
    if args.entry:
        entry_path = Path(args.entry)
        if not entry_path.is_absolute():
            entry_path = project_root / entry_path
        if not entry_path.exists():
            print(f"Error: File not found: {entry_path}")
            return 1
        return validate_single_entry(entry_path, project_root)

    if args.id:
        # Find entry by ID
        entries_dir = project_root / 'entries'
        entry_path = None
        for file_path in entries_dir.glob(f'**/{args.id}.json'):
            entry_path = file_path
            break
        if not entry_path:
            print(f"Error: No entry found with ID: {args.id}")
            return 1
        return validate_single_entry(entry_path, project_root)

    # Full validation mode
    print(f"Validating entries in {project_root}")
    print("-" * 50)

    total, valid, invalid_files, cross_ref_errors = validate_all_entries(project_root)

    if total == 0:
        print("No entry files found.")
        return 0

    # Report results
    if invalid_files:
        print(f"\nFound {len(invalid_files)} invalid file(s):\n")
        for file_path, errors in invalid_files:
            rel_path = file_path.relative_to(project_root)
            print(f"  {rel_path}:")
            for error in errors:
                print(f"    - {error}")
            print()

    # Report cross-reference warnings
    if cross_ref_errors:
        print(f"\nCross-reference warnings ({len(cross_ref_errors)} issues):\n")
        for file_path, error_msg in cross_ref_errors:
            rel_path = file_path.relative_to(project_root)
            print(f"  {rel_path}:")
            print(f"    - {error_msg}")
        print()

    print(f"Validation complete: {valid}/{total} entries valid")
    if cross_ref_errors:
        print(f"  ({len(cross_ref_errors)} cross-reference warnings)")

    if invalid_files:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
