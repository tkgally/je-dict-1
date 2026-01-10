#!/usr/bin/env python3
"""
Merge audio files into dictionary entries.

Reads JSON files from audio_files_to_add/ directory and adds audio_base64
field to corresponding examples in entry files.

Filename format: {entry_id}-ex{number}.json
Example: a_00412-ex1.json -> entry a_00412, example index 0
"""

import json
import re
import sys
from pathlib import Path


def parse_audio_filename(filename: str) -> tuple[str, int] | None:
    """
    Parse audio filename to extract entry_id and example number.

    Format: {entry_id}-ex{number}.json
    Returns (entry_id, example_index) or None if invalid.
    """
    # Match pattern like "a_00412-ex1.json" or "taberu_00001-ex2.json"
    match = re.match(r'^(.+)-ex(\d+)\.json$', filename)
    if not match:
        return None

    entry_id = match.group(1)
    example_num = int(match.group(2))
    # Convert to 0-based index
    example_index = example_num - 1

    return entry_id, example_index


def find_entry_file(entries_dir: Path, entry_id: str) -> Path | None:
    """Find the entry file for a given entry_id."""
    # Search all subdirectories for the entry file
    for file_path in entries_dir.glob(f'**/{entry_id}.json'):
        return file_path
    return None


def merge_audio_files(project_root: Path) -> int:
    """
    Merge audio files into entries.
    Returns the number of audio files successfully merged.
    """
    audio_dir = project_root / 'audio_files_to_add'
    entries_dir = project_root / 'entries'

    if not audio_dir.exists():
        print(f"Error: Audio directory not found: {audio_dir}")
        return 0

    # Collect all audio files grouped by entry
    audio_by_entry: dict[str, list[tuple[int, str]]] = {}

    print("Scanning audio files...")
    audio_files = list(audio_dir.glob('*.json'))
    print(f"Found {len(audio_files)} audio files")

    for audio_file in audio_files:
        result = parse_audio_filename(audio_file.name)
        if not result:
            print(f"  Warning: Could not parse filename: {audio_file.name}")
            continue

        entry_id, example_index = result

        # Read the audio data
        with open(audio_file, 'r', encoding='utf-8') as f:
            audio_data = json.load(f)

        audio_base64 = audio_data.get('audio_base64')
        if not audio_base64:
            print(f"  Warning: No audio_base64 in {audio_file.name}")
            continue

        if entry_id not in audio_by_entry:
            audio_by_entry[entry_id] = []
        audio_by_entry[entry_id].append((example_index, audio_base64))

    # Process each entry
    merged_count = 0
    entries_updated = 0

    print(f"\nMerging audio into {len(audio_by_entry)} entries...")

    for entry_id, audio_list in audio_by_entry.items():
        entry_file = find_entry_file(entries_dir, entry_id)
        if not entry_file:
            print(f"  Warning: Entry file not found for {entry_id}")
            continue

        # Read the entry
        with open(entry_file, 'r', encoding='utf-8') as f:
            entry = json.load(f)

        examples = entry.get('examples', [])
        if not examples:
            print(f"  Warning: No examples in entry {entry_id}")
            continue

        # Add audio to each example
        modified = False
        for example_index, audio_base64 in audio_list:
            if example_index >= len(examples):
                print(f"  Warning: Example index {example_index + 1} out of range for {entry_id} (has {len(examples)} examples)")
                continue

            examples[example_index]['audio'] = audio_base64
            merged_count += 1
            modified = True

        # Write the updated entry
        if modified:
            with open(entry_file, 'w', encoding='utf-8') as f:
                json.dump(entry, f, ensure_ascii=False, indent=2)
                f.write('\n')
            entries_updated += 1

    print(f"\nMerge complete!")
    print(f"  Audio files merged: {merged_count}")
    print(f"  Entries updated: {entries_updated}")

    return merged_count


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    merged = merge_audio_files(project_root)
    sys.exit(0 if merged > 0 else 1)


if __name__ == '__main__':
    main()
