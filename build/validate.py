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


def validate_all_entries(project_root: Path) -> tuple[int, int, list[tuple[Path, list[str]]]]:
    """
    Validate all entry files in the project.
    Returns (total_count, valid_count, list of (file, errors) for invalid files).
    """
    schema_path = project_root / 'build' / 'schema.json'
    schema = load_schema(schema_path)

    entries_dir = project_root / 'entries'
    variants_dir = project_root / 'variants'

    all_ids = set()
    total = 0
    valid = 0
    invalid_files = []

    # Collect all JSON files
    entry_files = list(entries_dir.glob('**/*.json'))
    variant_files = list(variants_dir.glob('**/*.json'))

    for file_path in entry_files + variant_files:
        total += 1
        errors = validate_entry_file(file_path, schema, all_ids)
        if errors:
            invalid_files.append((file_path, errors))
        else:
            valid += 1

    return total, valid, invalid_files


def main():
    """Main entry point."""
    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    print(f"Validating entries in {project_root}")
    print("-" * 50)

    total, valid, invalid_files = validate_all_entries(project_root)

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

    print(f"Validation complete: {valid}/{total} entries valid")

    if invalid_files:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
