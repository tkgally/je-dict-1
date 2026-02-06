#!/usr/bin/env python3
"""
Fix sense_numbers formatting from multi-line to compact format.

Changes:
  "sense_numbers": [
    1
  ]

To:
  "sense_numbers": [1]
"""

import json
import sys
from pathlib import Path


def fix_entry(filepath: Path) -> bool:
    """Fix sense_numbers formatting in a single entry file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse and re-serialize with compact formatting
        data = json.loads(content)

        # Check if file has examples with sense_numbers
        if 'examples' not in data:
            return False

        # Re-serialize with indent=2 but we need custom handling for sense_numbers
        # The simplest approach: serialize, then fix the sense_numbers arrays
        output = json.dumps(data, ensure_ascii=False, indent=2)

        # Fix multi-line sense_numbers arrays to be compact
        import re
        # Match "sense_numbers": [\n    1\n  ] or similar patterns
        pattern = r'"sense_numbers": \[\s*\n\s*(\d+(?:,\s*\d+)*)\s*\n\s*\]'

        def replace_func(match):
            numbers = match.group(1)
            # Clean up the numbers (remove extra whitespace)
            nums = [n.strip() for n in numbers.split(',')]
            return f'"sense_numbers": [{", ".join(nums)}]'

        fixed = re.sub(pattern, replace_func, output)

        # Also handle empty arrays that might be multi-line
        fixed = re.sub(r'"sense_numbers": \[\s*\]', '"sense_numbers": []', fixed)

        # Only write if changed
        if fixed != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed)
                f.write('\n')
            return True
        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_sense_numbers_format.py <directory>")
        sys.exit(1)

    target_dir = Path(sys.argv[1])
    if not target_dir.exists():
        print(f"Error: Directory {target_dir} does not exist")
        sys.exit(1)

    json_files = sorted(target_dir.rglob('*.json'))
    fixed_count = 0

    for filepath in json_files:
        if fix_entry(filepath):
            fixed_count += 1
            print(f"Fixed: {filepath.name}")

    print(f"\nFixed {fixed_count} files")


if __name__ == '__main__':
    main()
