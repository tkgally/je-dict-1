#!/usr/bin/env python3
"""
Migrate cross-references from legacy string format to structured format.

Legacy format: "entry_id" (e.g., "ika_00137")
Structured format: {"type": "see_also", "reading": "いか", "headword": "{以下|いか}", "label": null}

This script:
1. Loads all entries and builds an ID-to-entry lookup
2. Converts all legacy string references to structured format
3. Removes duplicate references (same reading appears both as legacy and structured)
4. Saves updated entries

Usage:
    python build/migrate_cross_references.py [--dry-run]
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Any, Optional

from japanese_utils import romaji_to_hiragana


def load_entries_index(project_root: Path) -> Dict[str, Dict[str, Any]]:
    """Load all entries and build an ID-to-entry lookup."""
    entries_dir = project_root / 'entries'
    id_to_entry = {}

    for entry_file in entries_dir.glob('**/*.json'):
        with open(entry_file, 'r', encoding='utf-8') as f:
            entry = json.load(f)
        entry['_file_path'] = str(entry_file)
        id_to_entry[entry['id']] = entry

    return id_to_entry


def convert_legacy_reference(ref_id: str, id_to_entry: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Convert a legacy string reference to structured format.

    Args:
        ref_id: Legacy reference string (entry ID like "ika_00137")
        id_to_entry: ID to entry lookup dictionary

    Returns:
        Structured cross-reference dictionary
    """
    # Try to find the entry by ID
    if ref_id in id_to_entry:
        entry = id_to_entry[ref_id]
        return {
            'type': 'see_also',
            'reading': entry['reading'],
            'headword': entry['headword'],
            'label': None
        }

    # If not found, try to extract reading from ID
    # ID format: 00000_romaji (e.g., "00001_taberu")
    parts = ref_id.split('_')
    if len(parts) >= 2:
        romaji = parts[1]
        reading = romaji_to_hiragana(romaji)
        return {
            'type': 'see_also',
            'reading': reading,
            'headword': None,
            'label': None
        }

    # Fallback
    return {
        'type': 'see_also',
        'reading': ref_id,
        'headword': None,
        'label': None
    }


def normalize_cross_references(
    refs: List[Any],
    id_to_entry: Dict[str, Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Normalize all cross-references to structured format and remove duplicates.

    Args:
        refs: List of cross-references (mixed legacy and structured)
        id_to_entry: ID to entry lookup dictionary

    Returns:
        List of structured cross-references with duplicates removed
    """
    normalized = []
    seen_keys = set()

    for ref in refs:
        if isinstance(ref, str):
            # Legacy format - convert it
            structured = convert_legacy_reference(ref, id_to_entry)
        else:
            # Already structured
            structured = ref

        # Check for duplicates using composite key (type, reading, headword, label)
        # This preserves refs with same reading but different type/headword/label
        ref_type = structured.get('type', '')
        reading = structured.get('reading', '')
        headword = structured.get('headword') or ''
        label = structured.get('label') or ''
        key = (ref_type, reading, headword, label)

        if key in seen_keys:
            # Skip duplicate
            continue

        seen_keys.add(key)
        normalized.append(structured)

    return normalized


def migrate_entry(
    entry: Dict[str, Any],
    id_to_entry: Dict[str, Dict[str, Any]]
) -> tuple[bool, int, int]:
    """
    Migrate cross-references in a single entry.

    Returns:
        (was_modified, legacy_count, removed_duplicates)
    """
    refs = entry.get('cross_references', [])
    if not refs:
        return False, 0, 0

    # Count legacy refs before migration
    legacy_count = sum(1 for r in refs if isinstance(r, str))
    if legacy_count == 0:
        return False, 0, 0

    original_count = len(refs)

    # Normalize all references
    normalized = normalize_cross_references(refs, id_to_entry)

    removed_duplicates = original_count - len(normalized)

    # Update the entry
    entry['cross_references'] = normalized

    return True, legacy_count, removed_duplicates


def save_entry(entry: Dict[str, Any]) -> None:
    """Save an entry back to its file."""
    file_path = entry.pop('_file_path')

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(entry, f, ensure_ascii=False, indent=2)
        f.write('\n')

    entry['_file_path'] = file_path  # Restore for reporting


def main():
    parser = argparse.ArgumentParser(
        description='Migrate cross-references from legacy to structured format'
    )
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Show what would be done without making changes'
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    print("Cross-Reference Migration")
    print("=" * 60)

    if args.dry_run:
        print("DRY RUN - No changes will be made\n")

    # Load all entries
    print("Loading entries...")
    id_to_entry = load_entries_index(project_root)
    print(f"  Loaded {len(id_to_entry)} entries\n")

    # Process entries
    print("Migrating cross-references...")
    entries_modified = 0
    total_legacy_converted = 0
    total_duplicates_removed = 0

    for entry_id, entry in sorted(id_to_entry.items()):
        was_modified, legacy_count, removed_dups = migrate_entry(entry, id_to_entry)

        if was_modified:
            entries_modified += 1
            total_legacy_converted += legacy_count
            total_duplicates_removed += removed_dups

            if not args.dry_run:
                save_entry(entry)

            # Show progress for modified entries
            if legacy_count > 0 or removed_dups > 0:
                status = []
                if legacy_count > 0:
                    status.append(f"{legacy_count} converted")
                if removed_dups > 0:
                    status.append(f"{removed_dups} duplicates removed")
                print(f"  {entry_id}: {', '.join(status)}")

    print()
    print("=" * 60)
    print("Migration Summary")
    print("=" * 60)
    print(f"  Entries modified: {entries_modified}")
    print(f"  Legacy refs converted: {total_legacy_converted}")
    print(f"  Duplicates removed: {total_duplicates_removed}")

    if args.dry_run:
        print("\nThis was a dry run. Run without --dry-run to apply changes.")
    else:
        print("\nMigration complete!")


if __name__ == '__main__':
    main()
