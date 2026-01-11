#!/usr/bin/env python3
"""
Migrate audio files from flat kana structure to kana/prefix structure.

Old structure: audio/{kana}/{entry_id}-ex{n}.mp3
New structure: audio/{kana}/{prefix}/{entry_id}-ex{n}.mp3

Where {prefix} is the first 2 characters of the entry_id.
"""

import shutil
from pathlib import Path

from path_utils import get_audio_prefix


def migrate_audio_files(project_root: Path) -> int:
    """
    Migrate audio files from old flat structure to new prefix structure.
    Returns the number of files migrated.
    """
    audio_dir = project_root / 'audio'

    if not audio_dir.exists():
        print("No audio directory found.")
        return 0

    migrated_count = 0
    errors = []

    # Process each kana directory
    for kana_dir in sorted(audio_dir.iterdir()):
        if not kana_dir.is_dir():
            continue

        kana_name = kana_dir.name
        print(f"\nProcessing {kana_name}/...")

        # Find all MP3 files directly in the kana directory (old structure)
        mp3_files = list(kana_dir.glob('*.mp3'))

        if not mp3_files:
            print(f"  No MP3 files to migrate in {kana_name}/")
            continue

        print(f"  Found {len(mp3_files)} files to migrate")

        for audio_file in mp3_files:
            try:
                # Get the prefix from the filename
                prefix = get_audio_prefix(audio_file.name)

                # Create the new prefix directory
                prefix_dir = kana_dir / prefix
                prefix_dir.mkdir(exist_ok=True)

                # Move the file to the new location
                new_path = prefix_dir / audio_file.name
                shutil.move(str(audio_file), str(new_path))
                migrated_count += 1

            except Exception as e:
                errors.append(f"{audio_file}: {e}")

    print(f"\n{'=' * 50}")
    print(f"Migration complete!")
    print(f"  Files migrated: {migrated_count}")

    if errors:
        print(f"  Errors: {len(errors)}")
        for error in errors[:10]:  # Show first 10 errors
            print(f"    - {error}")
        if len(errors) > 10:
            print(f"    ... and {len(errors) - 10} more")

    return migrated_count


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    print("Audio File Migration")
    print("=" * 50)
    print("Migrating from: audio/{kana}/*.mp3")
    print("To:             audio/{kana}/{prefix}/*.mp3")

    migrate_audio_files(project_root)


if __name__ == '__main__':
    main()
