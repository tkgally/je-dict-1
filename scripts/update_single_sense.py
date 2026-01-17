#!/usr/bin/env python3
"""
Automatically update sense_numbers for single-sense dictionary entries.

For entries with only one definition, all examples should have sense_numbers: [1].
This script finds such entries and updates them automatically.
"""

import json
import sys
from pathlib import Path


def process_entry(filepath: Path) -> tuple[bool, str]:
    """
    Process a single entry file.

    Returns:
        (was_modified, status_message)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        return False, f"Error reading: {e}"

    # Check if single-sense entry
    definitions = data.get('definitions', [])
    if len(definitions) != 1:
        return False, f"Multi-sense ({len(definitions)} senses)"

    # Check examples
    examples = data.get('examples', [])
    if not examples:
        return False, "No examples"

    # Check if any examples need updating
    needs_update = False
    for ex in examples:
        if ex.get('sense_numbers') == []:
            needs_update = True
            break

    if not needs_update:
        return False, "Already processed"

    # Update all examples to [1]
    for ex in examples:
        if ex.get('sense_numbers') == []:
            ex['sense_numbers'] = [1]

    # Write back with compact sense_numbers formatting
    try:
        import re
        output = json.dumps(data, ensure_ascii=False, indent=2)
        # Fix multi-line sense_numbers arrays to be compact
        pattern = r'"sense_numbers": \[\s*\n\s*(\d+(?:,\s*\d+)*)\s*\n\s*\]'
        def replace_func(match):
            numbers = match.group(1)
            nums = [n.strip() for n in numbers.split(',')]
            return f'"sense_numbers": [{", ".join(nums)}]'
        output = re.sub(pattern, replace_func, output)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(output)
            f.write('\n')
    except IOError as e:
        return False, f"Error writing: {e}"

    return True, f"Updated {len(examples)} examples"


def main():
    if len(sys.argv) < 2:
        print("Usage: python update_single_sense.py <directory>")
        print("Example: python update_single_sense.py entries/00000/")
        sys.exit(1)

    target_dir = Path(sys.argv[1])
    if not target_dir.exists():
        print(f"Error: Directory {target_dir} does not exist")
        sys.exit(1)

    # Find all JSON files
    json_files = sorted(target_dir.rglob('*.json'))

    updated_count = 0
    multi_sense_files = []

    for filepath in json_files:
        was_modified, status = process_entry(filepath)

        if was_modified:
            updated_count += 1
            print(f"✓ {filepath.name}: {status}")
        elif "Multi-sense" in status:
            multi_sense_files.append((filepath, status))

    print(f"\n--- Summary ---")
    print(f"Single-sense entries updated: {updated_count}")
    print(f"Multi-sense entries (need manual review): {len(multi_sense_files)}")

    if multi_sense_files:
        print(f"\nMulti-sense entries:")
        for filepath, status in multi_sense_files:
            print(f"  {filepath}: {status}")


if __name__ == '__main__':
    main()
