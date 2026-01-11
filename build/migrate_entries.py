#!/usr/bin/env python3
"""
Migration script to reorganize entries into prefix-based subdirectories.

Moves entries from:
    entries/{kana}/{entry_id}.json
To:
    entries/{kana}/{prefix}/{entry_id}.json

Where prefix is the first 2 characters of the entry ID (e.g., 'ta' for 'taberu_00001').

This structure prevents any single directory from exceeding GitHub's 1,000 file limit
when the dictionary scales to 10,000+ entries.

Usage:
    python build/migrate_entries.py [--dry-run]
"""

import argparse
import shutil
from pathlib import Path

from path_utils import get_entry_prefix


def migrate_entries(project_root: Path, dry_run: bool = False) -> int:
    """
    Migrate entries to the new prefix-based subdirectory structure.

    Returns the number of files moved.
    """
    entries_dir = project_root / 'entries'

    if not entries_dir.exists():
        print(f"Error: entries directory not found at {entries_dir}")
        return 0

    moved_count = 0

    # Find all JSON files in entries directory
    for json_file in entries_dir.glob('**/*.json'):
        # Skip if already in a prefix subdirectory (3 levels deep: entries/kana/prefix/file.json)
        relative = json_file.relative_to(entries_dir)
        parts = relative.parts

        if len(parts) == 3:
            # Already migrated (entries/kana/prefix/file.json)
            continue

        if len(parts) != 2:
            print(f"Warning: Unexpected path structure: {json_file}")
            continue

        # Current structure: entries/kana/file.json
        kana_dir = parts[0]
        filename = parts[1]
        entry_id = filename.replace('.json', '')

        # Calculate new path
        prefix = get_entry_prefix(entry_id)
        new_dir = entries_dir / kana_dir / prefix
        new_path = new_dir / filename

        if dry_run:
            print(f"Would move: {json_file.relative_to(project_root)} -> {new_path.relative_to(project_root)}")
        else:
            # Create prefix directory if needed
            new_dir.mkdir(parents=True, exist_ok=True)
            # Move the file
            shutil.move(str(json_file), str(new_path))
            print(f"Moved: {json_file.relative_to(project_root)} -> {new_path.relative_to(project_root)}")

        moved_count += 1

    return moved_count


def main():
    parser = argparse.ArgumentParser(description='Migrate entries to prefix-based subdirectories')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Show what would be done without making changes')
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    print("Entry Migration Script")
    print("=" * 50)

    if args.dry_run:
        print("DRY RUN - No changes will be made\n")

    moved = migrate_entries(project_root, dry_run=args.dry_run)

    print("\n" + "=" * 50)
    if args.dry_run:
        print(f"Would move {moved} files")
        print("\nRun without --dry-run to perform the migration.")
    else:
        print(f"Migrated {moved} files")
        if moved > 0:
            print("\nRemember to update entries_index.json by running:")
            print("  python build/update_entries_index.py")


if __name__ == '__main__':
    main()
