#!/usr/bin/env python3
"""
Merge audio files into dictionary entries.

Reads MP3 files from audio-to-add/ directory:
- Copies them to the audio/{kana}/{prefix}/ directory
  - {kana}: kana row folder (a, ka, sa, etc.) based on reading
  - {prefix}: first 2 characters of entry_id for scalable subdirectories
- Updates corresponding entry files to set has_audio: true on examples

Filename format: {entry_id}-ex{number}.mp3
Example: ittai_00493-ex1.mp3 -> audio/a/it/ittai_00493-ex1.mp3
"""

import json
import re
import shutil
import sys
from pathlib import Path

from validate import get_expected_directory


def parse_audio_filename(filename: str) -> tuple[str, int] | None:
    """
    Parse audio filename to extract entry_id and example number.

    Format: {entry_id}-ex{number}.mp3
    Returns (entry_id, example_index) or None if invalid.
    """
    # Match pattern like "a_00412-ex1.mp3" or "taberu_00001-ex2.mp3"
    match = re.match(r'^(.+)-ex(\d+)\.mp3$', filename)
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


def get_audio_prefix(entry_id: str) -> str:
    """
    Get the 2-character prefix for audio file organization.

    This creates a subdirectory structure to avoid GitHub's 1,000 file limit.
    Example: 'ittai_00493' -> 'it'
    """
    return entry_id[:2].lower()


def merge_audio_files(project_root: Path) -> int:
    """
    Merge audio files into entries.
    Returns the number of audio files successfully merged.
    """
    audio_input_dir = project_root / 'audio-to-add'
    audio_output_dir = project_root / 'audio'
    entries_dir = project_root / 'entries'

    if not audio_input_dir.exists():
        print(f"Error: Audio input directory not found: {audio_input_dir}")
        return 0

    # Collect all audio files grouped by entry
    audio_by_entry: dict[str, list[tuple[int, Path]]] = {}

    print("Scanning audio files...")
    audio_files = list(audio_input_dir.glob('*.mp3'))
    print(f"Found {len(audio_files)} MP3 files")

    if not audio_files:
        print("No audio files to process.")
        return 0

    for audio_file in audio_files:
        result = parse_audio_filename(audio_file.name)
        if not result:
            print(f"  Warning: Could not parse filename: {audio_file.name}")
            continue

        entry_id, example_index = result

        if entry_id not in audio_by_entry:
            audio_by_entry[entry_id] = []
        audio_by_entry[entry_id].append((example_index, audio_file))

    # Process each entry
    merged_count = 0
    entries_updated = 0

    print(f"\nProcessing {len(audio_by_entry)} entries...")

    for entry_id, audio_list in audio_by_entry.items():
        entry_file = find_entry_file(entries_dir, entry_id)
        if not entry_file:
            print(f"  Warning: Entry file not found for {entry_id}")
            continue

        # Read the entry
        with open(entry_file, 'r', encoding='utf-8') as f:
            entry = json.load(f)

        # Determine the kana subfolder from the entry's reading
        reading = entry.get('reading', '')
        kana_folder = get_expected_directory(reading)
        if not kana_folder:
            print(f"  Warning: Could not determine folder for {entry_id} (reading: {reading})")
            continue

        # Get the 2-character prefix for the subdirectory
        prefix = get_audio_prefix(entry_id)

        # Create the kana/prefix subfolder structure
        audio_prefix_dir = audio_output_dir / kana_folder / prefix
        audio_prefix_dir.mkdir(parents=True, exist_ok=True)

        examples = entry.get('examples', [])
        if not examples:
            print(f"  Warning: No examples in entry {entry_id}")
            continue

        # Process each audio file for this entry
        modified = False
        for example_index, audio_file in audio_list:
            if example_index >= len(examples):
                print(f"  Warning: Example index {example_index + 1} out of range for {entry_id} (has {len(examples)} examples)")
                continue

            # Copy audio file to the kana/prefix subfolder
            dest_path = audio_prefix_dir / audio_file.name
            shutil.copy2(audio_file, dest_path)

            # Mark example as having audio (remove any old embedded audio)
            if 'audio' in examples[example_index]:
                del examples[example_index]['audio']
            examples[example_index]['has_audio'] = True

            merged_count += 1
            modified = True

        # Write the updated entry
        if modified:
            with open(entry_file, 'w', encoding='utf-8') as f:
                json.dump(entry, f, ensure_ascii=False, indent=2)
                f.write('\n')
            entries_updated += 1

    print(f"\nMerge complete!")
    print(f"  Audio files copied: {merged_count}")
    print(f"  Entries updated: {entries_updated}")
    print(f"  Audio files stored in: {audio_output_dir}")

    return merged_count


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    merged = merge_audio_files(project_root)
    sys.exit(0 if merged > 0 else 1)


if __name__ == '__main__':
    main()
