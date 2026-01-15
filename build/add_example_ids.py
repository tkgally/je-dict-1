#!/usr/bin/env python3
"""
Add unique IDs and sense_numbers to all example sentences.

ID Format: {entry_id}_ex{number} where number is 1-indexed position
sense_numbers: Initially set to empty array []

Field order in examples: id, japanese, english, notes, has_audio, sense_numbers
"""

import json
import glob
import os
from collections import OrderedDict


def reorder_example(example, entry_id, index):
    """Reorder example fields and add id and sense_numbers."""
    # Create new example with proper field order
    new_example = OrderedDict()

    # Add id first
    new_example['id'] = f"{entry_id}_ex{index + 1}"

    # Add existing fields in order
    if 'japanese' in example:
        new_example['japanese'] = example['japanese']
    if 'english' in example:
        new_example['english'] = example['english']
    if 'notes' in example:
        new_example['notes'] = example['notes']
    if 'has_audio' in example:
        new_example['has_audio'] = example['has_audio']

    # Add sense_numbers last
    new_example['sense_numbers'] = []

    return new_example


def process_entry(filepath):
    """Process a single entry file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    entry_id = data.get('id')
    if not entry_id:
        print(f"Warning: No id found in {filepath}")
        return False

    examples = data.get('examples', [])
    if not examples:
        return False  # No examples to update

    # Check if already processed (first example has 'id' field)
    if examples and 'id' in examples[0]:
        return False  # Already processed

    # Update examples
    new_examples = []
    for i, example in enumerate(examples):
        new_example = reorder_example(example, entry_id, i)
        new_examples.append(new_example)

    data['examples'] = new_examples

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

    return True


def main():
    entries_dir = os.path.join(os.path.dirname(__file__), '..', 'entries')

    # Find all JSON files
    pattern = os.path.join(entries_dir, '*', '*.json')
    files = glob.glob(pattern)

    # Also check for files in nested subdirectories (like entries/n/na/)
    pattern2 = os.path.join(entries_dir, '*', '*', '*.json')
    files.extend(glob.glob(pattern2))

    updated_count = 0
    total_examples = 0

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        examples_before = len(data.get('examples', []))

        if process_entry(filepath):
            updated_count += 1
            total_examples += examples_before

    print(f"Updated {updated_count} files with {total_examples} examples")
    print(f"Total files scanned: {len(files)}")


if __name__ == '__main__':
    main()
