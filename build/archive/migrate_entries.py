#!/usr/bin/env python3
"""
Migration script to reorganize dictionary entries to the new ID and directory format.

Old format:
- Entry ID: romaji_00000 (e.g., taberu_00001)
- Directory: entries/{kana_row}/{romaji_prefix}/ (e.g., entries/ta/ta/)

New format:
- Entry ID: 00000_romaji (e.g., 00001_taberu)
- Directory: entries/{number_range}/ (e.g., entries/00000/)
- Range groups entries by 500 (00000, 00500, 01000, etc.)

This script:
1. Reads all existing entries
2. Converts IDs from old format to new format
3. Updates all internal references (example IDs)
4. Moves files to new directory structure
5. Cleans up old directory structure

Usage:
    python3 build/migrate_entries.py [--dry-run]

Options:
    --dry-run    Show what would be done without making changes
"""

import json
import os
import re
import shutil
import sys
from pathlib import Path
from datetime import datetime, timezone


def convert_entry_id(old_id: str) -> str:
    """
    Convert entry ID from old format to new format.

    Old: romaji_00000 (e.g., taberu_00001)
    Old with suffix: romaji_suffix_00000 (e.g., kagaku_chem_05506)
    New: 00000_romaji (e.g., 00001_taberu)
    New with suffix: 00000_romaji_suffix (e.g., 05506_kagaku_chem)
    """
    parts = old_id.split('_')

    if len(parts) == 2:
        # Standard format: romaji_00000
        romaji = parts[0]
        number = parts[1]
    elif len(parts) == 3:
        # Format with suffix: romaji_suffix_00000 (e.g., kagaku_chem_05506)
        romaji = parts[0]
        suffix = parts[1]
        number = parts[2]
        # Combine romaji and suffix for the new format
        romaji = f"{romaji}_{suffix}"
    else:
        raise ValueError(f"Invalid entry ID format: {old_id}")

    # Verify the number portion
    if not number.isdigit() or len(number) != 5:
        raise ValueError(f"Invalid number portion in ID: {old_id}")

    return f"{number}_{romaji}"


def get_directory_range(entry_id: str) -> str:
    """
    Get the directory range for an entry ID.
    Expects new format: 00000_romaji
    """
    parts = entry_id.split('_')
    if len(parts) >= 1:
        try:
            num_id = int(parts[0])
            range_start = (num_id // 500) * 500
            return f"{range_start:05d}"
        except ValueError:
            pass
    return "00000"


def migrate_entry(entry_data: dict) -> dict:
    """
    Migrate a single entry's data to the new format.

    Args:
        entry_data: The entry dictionary

    Returns:
        The migrated entry data
    """
    old_id = entry_data['id']
    new_id = convert_entry_id(old_id)

    # Update the entry ID
    entry_data['id'] = new_id

    # Update example IDs
    if 'examples' in entry_data:
        for example in entry_data['examples']:
            if 'id' in example:
                old_ex_id = example['id']
                # Example ID format: romaji_00000_ex1 -> 00000_romaji_ex1
                if old_ex_id.startswith(old_id + '_ex'):
                    ex_suffix = old_ex_id[len(old_id):]  # Gets "_ex1", "_ex2", etc.
                    example['id'] = new_id + ex_suffix

    return entry_data


def migrate_all_entries(project_root: Path, dry_run: bool = False) -> bool:
    """
    Migrate all entries to the new format.

    Args:
        project_root: Path to the project root
        dry_run: If True, show changes without making them

    Returns:
        True on success, False on failure
    """
    entries_dir = project_root / 'entries'
    audio_dir = project_root / 'audio'

    if not entries_dir.exists():
        print(f"Error: entries directory not found: {entries_dir}")
        return False

    # Collect all entry files
    entry_files = list(entries_dir.glob('**/*.json'))
    print(f"Found {len(entry_files)} entry files to migrate")

    if dry_run:
        print("\n[DRY RUN] No changes will be made.\n")

    # Store migration mappings for reference
    migrations = []
    errors = []

    # First pass: Read and convert all entries
    print("\n[1/4] Converting entry data...")
    converted_entries = []

    for file_path in entry_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)

            old_id = entry['id']
            old_path = str(file_path.relative_to(project_root))

            # Migrate the entry data
            migrated = migrate_entry(entry.copy())
            new_id = migrated['id']
            new_dir = get_directory_range(new_id)
            new_path = f"entries/{new_dir}/{new_id}.json"

            converted_entries.append({
                'old_id': old_id,
                'new_id': new_id,
                'old_path': old_path,
                'new_path': new_path,
                'old_file_path': file_path,
                'data': migrated
            })

            migrations.append({
                'old_id': old_id,
                'new_id': new_id,
                'old_path': old_path,
                'new_path': new_path
            })

        except Exception as e:
            errors.append(f"Error processing {file_path}: {e}")
            print(f"  Error processing {file_path}: {e}")

    if errors:
        print(f"\n{len(errors)} errors occurred during conversion.")
        if not dry_run:
            print("Aborting migration due to errors.")
            return False

    print(f"  Converted {len(converted_entries)} entries")

    # Show sample migrations
    print("\n  Sample migrations:")
    for m in migrations[:5]:
        print(f"    {m['old_id']} -> {m['new_id']}")
        print(f"      {m['old_path']} -> {m['new_path']}")

    if dry_run:
        print(f"\n[DRY RUN] Would migrate {len(converted_entries)} entries")
        print("\nTo perform the actual migration, run without --dry-run")
        return True

    # Second pass: Create new directory structure and write files
    print("\n[2/4] Creating new directory structure and writing files...")

    # Create all needed directories
    needed_dirs = set()
    for entry in converted_entries:
        new_dir = Path(entry['new_path']).parent
        needed_dirs.add(entries_dir.parent / new_dir)

    for dir_path in needed_dirs:
        dir_path.mkdir(parents=True, exist_ok=True)

    # Write migrated files to new locations
    for entry in converted_entries:
        new_file_path = entries_dir.parent / entry['new_path']
        with open(new_file_path, 'w', encoding='utf-8') as f:
            json.dump(entry['data'], f, ensure_ascii=False, indent=2)

    print(f"  Created {len(needed_dirs)} directories")
    print(f"  Wrote {len(converted_entries)} entry files")

    # Third pass: Migrate audio files (if they exist)
    print("\n[3/4] Migrating audio files...")
    if audio_dir.exists():
        audio_migrations = 0
        audio_files_to_remove = []

        for entry in converted_entries:
            old_id = entry['old_id']
            new_id = entry['new_id']
            new_dir = get_directory_range(new_id)

            # Find audio files for this entry
            # Audio files are named: {entry_id}-ex{n}.mp3
            for audio_file in audio_dir.glob(f'**/{old_id}-ex*.mp3'):
                # Convert audio filename
                old_audio_name = audio_file.name
                new_audio_name = old_audio_name.replace(old_id, new_id)

                # New audio path uses same range-based structure
                new_audio_dir = audio_dir / new_dir
                new_audio_dir.mkdir(parents=True, exist_ok=True)
                new_audio_path = new_audio_dir / new_audio_name

                # Copy audio file to new location
                shutil.copy2(audio_file, new_audio_path)
                audio_files_to_remove.append(audio_file)
                audio_migrations += 1

        print(f"  Migrated {audio_migrations} audio files")

        # Remove old audio files
        for audio_file in audio_files_to_remove:
            audio_file.unlink()
    else:
        print("  No audio directory found, skipping audio migration")

    # Fourth pass: Clean up old directory structure
    print("\n[4/4] Cleaning up old directory structure...")

    # Remove old entry files
    for entry in converted_entries:
        old_file_path = entry['old_file_path']
        if old_file_path.exists():
            old_file_path.unlink()

    # Remove empty directories in old structure (kana-based directories)
    old_dirs_to_check = set()
    for entry in converted_entries:
        old_file_path = entry['old_file_path']
        old_dirs_to_check.add(old_file_path.parent)
        if old_file_path.parent.parent != entries_dir:
            old_dirs_to_check.add(old_file_path.parent.parent)

    # Sort by depth (deepest first) to remove from bottom up
    sorted_dirs = sorted(old_dirs_to_check, key=lambda p: len(p.parts), reverse=True)

    removed_dirs = 0
    for dir_path in sorted_dirs:
        if dir_path.exists() and dir_path != entries_dir:
            try:
                # Only remove if empty
                if not any(dir_path.iterdir()):
                    dir_path.rmdir()
                    removed_dirs += 1
            except OSError:
                pass  # Directory not empty or other error

    print(f"  Removed {len(converted_entries)} old entry files")
    print(f"  Removed {removed_dirs} empty directories")

    # Also clean up empty audio directories if they exist
    if audio_dir.exists():
        audio_dirs_to_clean = set()
        for dir_path in audio_dir.glob('**/'):
            if dir_path != audio_dir and dir_path.is_dir():
                # Check if this is an old kana-based directory (not numeric)
                if not dir_path.name.isdigit():
                    audio_dirs_to_clean.add(dir_path)

        # Sort by depth (deepest first)
        sorted_audio_dirs = sorted(audio_dirs_to_clean, key=lambda p: len(p.parts), reverse=True)
        for dir_path in sorted_audio_dirs:
            if dir_path.exists():
                try:
                    if not any(dir_path.iterdir()):
                        dir_path.rmdir()
                except OSError:
                    pass

    # Summary
    print("\n" + "=" * 50)
    print("Migration complete!")
    print(f"  Total entries migrated: {len(converted_entries)}")
    print(f"  New directory structure: entries/{{range}}/ where range = 00000, 00500, etc.")
    print(f"  New ID format: {{5-digit-number}}_{{romaji}}")

    return True


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Migrate dictionary entries to new ID and directory format'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    print("Entry Migration Script")
    print("=" * 50)
    print(f"Project root: {project_root}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")

    success = migrate_all_entries(project_root, dry_run=args.dry_run)

    if not args.dry_run and success:
        print("\nNext steps:")
        print("  1. Run: python3 build/update_entries_index.py")
        print("  2. Run: python3 build/validate.py")
        print("  3. Run: python3 build/build_flat.py")

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
