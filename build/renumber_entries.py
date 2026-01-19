#!/usr/bin/env python3
"""
Renumber Dictionary Entry IDs to Unique Five-Digit Indices

This script renumbers all dictionary entries so that each five-digit numeric
prefix is unique. Currently, many entries share the same prefix (e.g., 438
entries all have prefix 00001).

The renumbering process:
1. Assigns new sequential numeric indices based on filename sort order
2. Updates the 'id' field in each entry
3. Updates all example IDs (e.g., 00001_word_ex1 -> 00042_word_ex1)
4. Updates all cross-reference target_id fields pointing to renamed entries
5. Moves files to correct directories based on new numeric prefix
6. Regenerates index files

Usage:
    python3 build/renumber_entries.py                    # Dry run - show changes
    python3 build/renumber_entries.py --apply            # Apply changes
    python3 build/renumber_entries.py --create-mapping   # Only create mapping file

The mapping is saved to id_migration_map.json for reference and reversibility.
"""

import json
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
from collections import defaultdict

# Add build directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from path_utils import get_directory_range, get_entry_path


def find_all_entries(entries_dir: Path) -> List[Path]:
    """Find all entry JSON files, sorted by path."""
    entries = []
    for subdir in sorted(entries_dir.iterdir()):
        if subdir.is_dir() and subdir.name.isdigit():
            for entry_file in sorted(subdir.glob("*.json")):
                entries.append(entry_file)
    return entries


def extract_id_from_path(path: Path) -> str:
    """Extract entry ID from file path."""
    return path.stem  # filename without .json


def get_romaji_part(entry_id: str) -> str:
    """Extract the romaji part from an entry ID (everything after the first underscore)."""
    parts = entry_id.split('_', 1)
    if len(parts) >= 2:
        return parts[1]
    return entry_id


def create_new_id(new_number: int, romaji: str) -> str:
    """Create a new entry ID with the given number and romaji."""
    return f"{new_number:05d}_{romaji}"


def build_id_mapping(entries_dir: Path, start_number: int = 1) -> Dict[str, str]:
    """
    Build a mapping from old IDs to new sequential IDs.

    Returns:
        Dict mapping old_id -> new_id
    """
    entries = find_all_entries(entries_dir)
    mapping = {}

    for i, entry_path in enumerate(entries):
        old_id = extract_id_from_path(entry_path)
        romaji = get_romaji_part(old_id)
        new_number = start_number + i
        new_id = create_new_id(new_number, romaji)
        mapping[old_id] = new_id

    return mapping


def update_entry_content(entry_data: Dict[str, Any], old_id: str, new_id: str) -> bool:
    """
    Update entry content with new ID.

    Returns:
        True if changes were made, False otherwise
    """
    changed = False

    # Update main ID
    if entry_data.get('id') == old_id:
        entry_data['id'] = new_id
        changed = True

    # Update example IDs
    if 'examples' in entry_data:
        for example in entry_data['examples']:
            if 'id' in example:
                old_example_id = example['id']
                # Example IDs are like "00001_word_ex1"
                if old_example_id.startswith(old_id + '_ex'):
                    suffix = old_example_id[len(old_id):]  # Gets "_ex1", "_ex2", etc.
                    example['id'] = new_id + suffix
                    changed = True

    return changed


def update_cross_references(entry_data: Dict[str, Any], id_mapping: Dict[str, str]) -> Tuple[bool, List[str]]:
    """
    Update cross-reference target_ids based on the mapping.

    Returns:
        Tuple of (changed: bool, list of updated target_ids)
    """
    changed = False
    updated_refs = []

    if 'cross_references' not in entry_data:
        return False, []

    for xref in entry_data['cross_references']:
        if 'target_id' in xref:
            old_target = xref['target_id']
            if old_target in id_mapping:
                new_target = id_mapping[old_target]
                if old_target != new_target:
                    xref['target_id'] = new_target
                    updated_refs.append(f"{old_target} -> {new_target}")
                    changed = True

    return changed, updated_refs


def get_entries_needing_move(entries_dir: Path, id_mapping: Dict[str, str]) -> List[Tuple[Path, Path]]:
    """
    Determine which entries need to be moved to a different directory.

    Returns:
        List of (old_path, new_path) tuples
    """
    moves = []

    for old_id, new_id in id_mapping.items():
        old_path = get_entry_path(entries_dir, old_id)
        new_path = get_entry_path(entries_dir, new_id)

        if old_path != new_path:
            moves.append((old_path, new_path))

    return moves


def analyze_changes(entries_dir: Path, id_mapping: Dict[str, str]) -> Dict[str, Any]:
    """Analyze what changes would be made without applying them."""
    stats = {
        'total_entries': len(id_mapping),
        'entries_with_id_change': 0,
        'entries_with_example_changes': 0,
        'entries_needing_move': 0,
        'cross_references_updated': 0,
        'entries_with_xref_updates': 0,
        'directories_to_create': set(),
        'directories_to_remove': set(),
    }

    # Count ID changes (where old != new)
    for old_id, new_id in id_mapping.items():
        if old_id != new_id:
            stats['entries_with_id_change'] += 1

    # Analyze moves
    moves = get_entries_needing_move(entries_dir, id_mapping)
    stats['entries_needing_move'] = len(moves)

    for old_path, new_path in moves:
        stats['directories_to_create'].add(new_path.parent)

    # Analyze cross-reference updates
    entries = find_all_entries(entries_dir)
    for entry_path in entries:
        with open(entry_path, 'r', encoding='utf-8') as f:
            entry_data = json.load(f)

        changed, refs = update_cross_references(dict(entry_data), id_mapping)
        if changed:
            stats['entries_with_xref_updates'] += 1
            stats['cross_references_updated'] += len(refs)

    stats['directories_to_create'] = sorted([str(d) for d in stats['directories_to_create']])

    return stats


def dry_run(entries_dir: Path, id_mapping: Dict[str, str]) -> None:
    """Show what changes would be made without applying them."""
    print("=" * 70)
    print("DRY RUN - No changes will be made")
    print("=" * 70)
    print()

    # Analyze
    stats = analyze_changes(entries_dir, id_mapping)

    print(f"Total entries: {stats['total_entries']}")
    print(f"Entries with ID change: {stats['entries_with_id_change']}")
    print(f"Entries needing file move: {stats['entries_needing_move']}")
    print(f"Entries with cross-reference updates: {stats['entries_with_xref_updates']}")
    print(f"Total cross-references to update: {stats['cross_references_updated']}")
    print()

    # Show sample changes
    print("Sample ID changes (first 20):")
    count = 0
    for old_id, new_id in id_mapping.items():
        if old_id != new_id:
            print(f"  {old_id} -> {new_id}")
            count += 1
            if count >= 20:
                remaining = stats['entries_with_id_change'] - 20
                if remaining > 0:
                    print(f"  ... and {remaining} more")
                break
    print()

    # Show entries that stay the same (first few)
    print("Entries keeping same ID (first 10):")
    count = 0
    for old_id, new_id in id_mapping.items():
        if old_id == new_id:
            print(f"  {old_id}")
            count += 1
            if count >= 10:
                break
    print()

    # Show directories that need to be created
    if stats['directories_to_create']:
        print(f"Directories to create/ensure exist: {len(stats['directories_to_create'])}")
        for d in stats['directories_to_create'][:10]:
            print(f"  {d}")
        if len(stats['directories_to_create']) > 10:
            print(f"  ... and {len(stats['directories_to_create']) - 10} more")
    print()

    print("To apply these changes, run with --apply")


def apply_changes(entries_dir: Path, id_mapping: Dict[str, str]) -> None:
    """Apply all changes to the entries."""
    print("=" * 70)
    print("APPLYING CHANGES")
    print("=" * 70)
    print()

    # Phase 1: Update all entry content (IDs, example IDs, cross-references)
    # We do this first while files are still at their original locations
    print("Phase 1: Updating entry content...")

    entries = find_all_entries(entries_dir)
    entries_updated = 0
    xrefs_updated = 0

    for entry_path in entries:
        old_id = extract_id_from_path(entry_path)
        new_id = id_mapping.get(old_id, old_id)

        with open(entry_path, 'r', encoding='utf-8') as f:
            entry_data = json.load(f)

        # Update the entry's own ID and examples
        id_changed = update_entry_content(entry_data, old_id, new_id)

        # Update cross-references to other entries
        xref_changed, refs = update_cross_references(entry_data, id_mapping)

        if id_changed or xref_changed:
            with open(entry_path, 'w', encoding='utf-8') as f:
                json.dump(entry_data, f, ensure_ascii=False, indent=2)
                f.write('\n')
            entries_updated += 1
            xrefs_updated += len(refs)

    print(f"  Updated {entries_updated} entries")
    print(f"  Updated {xrefs_updated} cross-references")
    print()

    # Phase 2: Move files to new locations
    print("Phase 2: Moving files to new locations...")

    moves = get_entries_needing_move(entries_dir, id_mapping)

    # Create all necessary directories first
    dirs_created = set()
    for _, new_path in moves:
        if new_path.parent not in dirs_created:
            new_path.parent.mkdir(parents=True, exist_ok=True)
            dirs_created.add(new_path.parent)

    # Move files (we need to be careful about ordering to avoid conflicts)
    # Strategy: First move all files to a temp location, then move to final location
    temp_dir = entries_dir / '_temp_migration'
    temp_dir.mkdir(exist_ok=True)

    # Move to temp
    temp_mapping = {}
    for old_path, new_path in moves:
        if old_path.exists():
            temp_path = temp_dir / old_path.name
            shutil.move(str(old_path), str(temp_path))
            temp_mapping[temp_path] = new_path

    # Move from temp to final location with new filename
    files_moved = 0
    for temp_path, new_path in temp_mapping.items():
        if temp_path.exists():
            shutil.move(str(temp_path), str(new_path))
            files_moved += 1

    # Clean up temp directory
    if temp_dir.exists():
        temp_dir.rmdir()

    print(f"  Moved {files_moved} files")
    print()

    # Phase 3: Clean up empty directories
    print("Phase 3: Cleaning up empty directories...")

    dirs_removed = 0
    for subdir in entries_dir.iterdir():
        if subdir.is_dir() and subdir.name.isdigit():
            try:
                if not any(subdir.iterdir()):
                    subdir.rmdir()
                    dirs_removed += 1
            except OSError:
                pass

    print(f"  Removed {dirs_removed} empty directories")
    print()

    print("=" * 70)
    print("MIGRATION COMPLETE")
    print("=" * 70)
    print()
    print("Next steps:")
    print("  1. Run: python3 build/update_entries_index.py")
    print("  2. Run: python3 build/harden_references.py")
    print("  3. Verify entries with: find entries -name '*.json' | wc -l")


def save_mapping(mapping: Dict[str, str], output_path: Path) -> None:
    """Save the ID mapping to a JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f"Mapping saved to {output_path}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Renumber dictionary entry IDs')
    parser.add_argument('--apply', action='store_true',
                        help='Apply changes (default is dry run)')
    parser.add_argument('--create-mapping', action='store_true',
                        help='Only create the mapping file, do not preview changes')
    parser.add_argument('--start', type=int, default=1,
                        help='Starting number for new IDs (default: 1)')
    args = parser.parse_args()

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'
    mapping_path = project_root / 'id_migration_map.json'

    if not entries_dir.exists():
        print(f"Error: entries directory not found at {entries_dir}")
        sys.exit(1)

    print("Building ID mapping...")
    id_mapping = build_id_mapping(entries_dir, args.start)
    print(f"  Found {len(id_mapping)} entries")
    print()

    # Always save the mapping
    save_mapping(id_mapping, mapping_path)
    print()

    if args.create_mapping:
        print("Mapping file created. Use --apply to execute the migration.")
        return

    if args.apply:
        apply_changes(entries_dir, id_mapping)
    else:
        dry_run(entries_dir, id_mapping)


if __name__ == '__main__':
    main()
