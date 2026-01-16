#!/usr/bin/env python3
"""
Clean up candidate_words.json:
1. Remove internal duplicates (same word+reading)
2. Remove candidates that already exist in entries_index.json
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Calculate paths relative to script location
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
CANDIDATES_FILE = PROJECT_ROOT / 'candidate_words.json'
ENTRIES_INDEX_FILE = PROJECT_ROOT / 'entries_index.json'


def load_json(filepath):
    """Load JSON file with error handling."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {filepath}: {e}")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied reading {filepath}")
        sys.exit(1)


def save_json(filepath, data):
    """Save JSON file with error handling."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except PermissionError:
        print(f"Error: Permission denied writing to {filepath}")
        sys.exit(1)
    except OSError as e:
        print(f"Error: Could not write to {filepath}: {e}")
        sys.exit(1)

def normalize_reading(reading):
    """Normalize reading for comparison - convert to hiragana lowercase."""
    # Convert katakana to hiragana
    result = []
    for char in reading:
        code = ord(char)
        # Katakana range: 0x30A0-0x30FF -> Hiragana: 0x3040-0x309F
        if 0x30A1 <= code <= 0x30F6:
            result.append(chr(code - 0x60))
        else:
            result.append(char)
    return ''.join(result).lower()

def main():
    # Load data
    candidates_data = load_json(CANDIDATES_FILE)
    entries_data = load_json(ENTRIES_INDEX_FILE)

    original_count = len(candidates_data['candidates'])
    print(f"Original candidates: {original_count}")

    # Build set of existing entry readings
    existing_readings = set()
    for entry in entries_data['entries']:
        reading = normalize_reading(entry['reading'])
        existing_readings.add(reading)
    print(f"Existing entries: {len(existing_readings)} unique readings")

    # Track removals
    removed_duplicates = []
    removed_existing = []

    # First pass: remove candidates that exist in entries
    seen_candidates = {}  # (word, reading) -> first candidate with that combo
    filtered_candidates = []

    for candidate in candidates_data['candidates']:
        reading = normalize_reading(candidate['reading'])
        word = candidate.get('word', '')

        # Check if already in entries (by reading only - entries may have different kanji)
        if reading in existing_readings:
            removed_existing.append({
                'id': candidate['id'],
                'word': word,
                'reading': candidate['reading']
            })
            continue

        # Check for internal duplicate (same word AND reading)
        # This allows homophones with different kanji to coexist
        key = (word, reading)
        if key in seen_candidates:
            removed_duplicates.append({
                'id': candidate['id'],
                'word': word,
                'reading': candidate['reading'],
                'duplicate_of': seen_candidates[key]['id']
            })
            continue

        # Keep this candidate
        seen_candidates[key] = candidate
        filtered_candidates.append(candidate)

    # Report results
    print(f"\n=== Removal Summary ===")
    print(f"Removed as existing entries: {len(removed_existing)}")
    print(f"Removed as internal duplicates: {len(removed_duplicates)}")
    print(f"Remaining candidates: {len(filtered_candidates)}")

    if removed_existing:
        print(f"\n=== Candidates removed (already in dictionary) ===")
        for item in removed_existing[:20]:
            print(f"  {item['id']}: {item['word']} ({item['reading']})")
        if len(removed_existing) > 20:
            print(f"  ... and {len(removed_existing) - 20} more")

    if removed_duplicates:
        print(f"\n=== Internal duplicates removed ===")
        for item in removed_duplicates[:20]:
            print(f"  {item['id']}: {item['word']} ({item['reading']}) - duplicate of {item['duplicate_of']}")
        if len(removed_duplicates) > 20:
            print(f"  ... and {len(removed_duplicates) - 20} more")

    # Update and save
    candidates_data['candidates'] = filtered_candidates
    candidates_data['metadata']['total_candidates'] = len(filtered_candidates)
    candidates_data['metadata']['last_updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    save_json(CANDIDATES_FILE, candidates_data)
    print(f"\nSaved updated {CANDIDATES_FILE}")
    print(f"Total removed: {original_count - len(filtered_candidates)}")

if __name__ == '__main__':
    main()
