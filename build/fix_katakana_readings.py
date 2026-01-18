#!/usr/bin/env python3
"""
Script to fix katakana readings in dictionary entries.
1. Identifies entries with katakana readings
2. Removes duplicates (where a hiragana version exists)
3. Converts remaining katakana readings to hiragana
4. Updates cross-references to deleted entries
5. Updates candidate_words.json similarly
"""

import json
import os
import re
import sys
from pathlib import Path

def is_katakana_reading(reading):
    """Check if reading has more katakana than hiragana."""
    katakana = len(re.findall(r'[\u30A0-\u30FF]', reading))
    hiragana = len(re.findall(r'[\u3040-\u309F]', reading))
    return katakana > hiragana

def katakana_to_hiragana(text):
    """Convert katakana characters to hiragana.

    Note: The long vowel mark ー (U+30FC) is kept as-is since there's no
    hiragana equivalent and it's commonly used in loanword readings.
    """
    result = []
    for char in text:
        code = ord(char)
        # Katakana range is U+30A0 to U+30FF
        # But we need to exclude special characters:
        # - U+30FC (ー) - long vowel mark, keep as-is
        # - U+30FD (ヽ) - iteration mark
        # - U+30FE (ヾ) - voiced iteration mark
        # - U+30FF (ヿ) - digraph
        if 0x30A1 <= code <= 0x30F6:  # Standard katakana (ァ to ヶ)
            result.append(chr(code - 0x60))
        elif code == 0x30F7:  # ヷ -> わ゛ (but rare, just use わ)
            result.append('わ')
        elif code == 0x30F8:  # ヸ -> ゐ゛ (but rare)
            result.append('ゐ')
        elif code == 0x30F9:  # ヹ -> ゑ゛ (but rare)
            result.append('ゑ')
        elif code == 0x30FA:  # ヺ -> を゛ (but rare)
            result.append('を')
        elif code == 0x30A0:  # ゠ (double hyphen)
            result.append('=')
        else:
            # Keep ー, ヽ, ヾ, etc. as-is
            result.append(char)
    return ''.join(result)

def load_entries_index():
    """Load entries index."""
    with open('entries_index.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def find_duplicates_and_convert(entries):
    """Find duplicates and entries to convert."""
    # Group entries by headword
    by_headword = {}
    for entry in entries:
        hw = entry['headword']
        if hw not in by_headword:
            by_headword[hw] = []
        by_headword[hw].append(entry)

    to_delete = []  # Entries to delete (katakana duplicates)
    to_convert = []  # Entries to convert (katakana readings, no duplicate)

    for hw, entry_list in by_headword.items():
        if len(entry_list) == 1:
            # Only one entry - check if it needs conversion
            entry = entry_list[0]
            if is_katakana_reading(entry['reading']):
                to_convert.append(entry)
        else:
            # Multiple entries - find katakana/hiragana pairs
            katakana_entries = [e for e in entry_list if is_katakana_reading(e['reading'])]
            hiragana_entries = [e for e in entry_list if not is_katakana_reading(e['reading'])]

            if katakana_entries and hiragana_entries:
                # We have both - delete katakana entries
                to_delete.extend(katakana_entries)
            elif katakana_entries:
                # Only katakana - convert them
                to_convert.extend(katakana_entries)

    return to_delete, to_convert

def delete_entry_files(entries, dry_run=False):
    """Delete entry JSON files."""
    deleted = []
    for entry in entries:
        path = entry['path']
        if os.path.exists(path):
            if not dry_run:
                os.remove(path)
            deleted.append(entry)
            print(f"  Deleted: {path}")
        else:
            print(f"  Not found: {path}")
    return deleted

def convert_entry_reading(entry, dry_run=False):
    """Convert katakana reading to hiragana in entry file."""
    path = entry['path']
    if not os.path.exists(path):
        print(f"  Not found: {path}")
        return False

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    old_reading = data['reading']
    new_reading = katakana_to_hiragana(old_reading)

    if old_reading == new_reading:
        return False

    print(f"  {path}: {old_reading} -> {new_reading}")

    if not dry_run:
        data['reading'] = new_reading
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

    return True

def update_cross_references(deleted_entries, dry_run=False):
    """Update cross-references to deleted entries."""
    # Build map of deleted entry IDs to their hiragana replacements
    id_map = {}
    for entry in deleted_entries:
        # Find the hiragana version
        # For now, we'll just note that the reference needs to be removed
        id_map[entry['id']] = None

    # Scan all entry files for cross-references
    updated = 0
    for root, dirs, files in os.walk('entries'):
        for filename in files:
            if not filename.endswith('.json'):
                continue
            filepath = os.path.join(root, filename)

            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if 'cross_references' not in data or not data['cross_references']:
                continue

            new_refs = []
            changed = False
            for ref in data['cross_references']:
                if 'target_id' in ref and ref['target_id'] in id_map:
                    print(f"  Removing reference to {ref['target_id']} in {filepath}")
                    changed = True
                    # Don't add this reference
                else:
                    new_refs.append(ref)

            if changed:
                updated += 1
                if not dry_run:
                    data['cross_references'] = new_refs
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                        f.write('\n')

    return updated

def fix_candidates(dry_run=False):
    """Fix katakana readings in candidate_words.json."""
    with open('candidate_words.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    converted = 0
    duplicates_removed = 0

    # Track readings to find duplicates
    seen_readings = {}
    new_candidates = []

    for candidate in data['candidates']:
        reading = candidate['reading']

        # Convert katakana to hiragana
        if is_katakana_reading(reading):
            new_reading = katakana_to_hiragana(reading)
            print(f"  Candidate {candidate['word']}: {reading} -> {new_reading}")
            candidate['reading'] = new_reading
            converted += 1
            reading = new_reading

        # Check for duplicates by (word, reading)
        key = (candidate['word'], reading)
        if key in seen_readings:
            print(f"  Removing duplicate candidate: {candidate['word']} ({reading})")
            duplicates_removed += 1
        else:
            seen_readings[key] = True
            new_candidates.append(candidate)

    if not dry_run:
        data['candidates'] = new_candidates
        data['metadata']['total_candidates'] = len(new_candidates)
        with open('candidate_words.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

    return converted, duplicates_removed

def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    # Load entries index
    print("Loading entries index...")
    index = load_entries_index()

    # Find duplicates and entries to convert
    print("\nAnalyzing entries...")
    to_delete, to_convert = find_duplicates_and_convert(index['entries'])

    print(f"\nFound {len(to_delete)} duplicate entries to delete")
    print(f"Found {len(to_convert)} entries to convert\n")

    # Delete duplicates
    if to_delete:
        print("Deleting duplicate entries:")
        delete_entry_files(to_delete, dry_run)

    # Convert remaining katakana readings
    if to_convert:
        print("\nConverting katakana readings to hiragana:")
        for entry in to_convert:
            convert_entry_reading(entry, dry_run)

    # Update cross-references
    print("\nChecking cross-references to deleted entries:")
    updated = update_cross_references(to_delete, dry_run)
    print(f"Updated {updated} files with cross-references")

    # Fix candidates
    print("\nFixing candidate_words.json:")
    converted, removed = fix_candidates(dry_run)
    print(f"Converted {converted} readings, removed {removed} duplicates")

    print("\nDone!")
    if dry_run:
        print("(This was a dry run - no files were modified)")

if __name__ == '__main__':
    main()
