# Kanji Index Implementation - Step 9: Create Verification Script

## Overview

Create a script that verifies the integrity and accuracy of the kanji index before each website build.

## Task

Create `build/verify_kanji_index.py`:

### Functionality

The verification script checks:

1. **Completeness**: All kanji in entries have IDs assigned
2. **File integrity**: All kanji JSON files exist and are valid
3. **Consistency**: Entry counts match between JSON files and actual entries
4. **ID format**: All kanji IDs follow the correct format
5. **No duplicates**: No duplicate kanji IDs
6. **HTML existence**: All kanji HTML files exist

### Script Structure

```python
#!/usr/bin/env python3
"""
Verify kanji index integrity.

This script checks:
1. All kanji have IDs assigned
2. All kanji JSON files exist and are valid
3. Entry counts are accurate
4. Kanji ID format is correct
5. No duplicate IDs
6. HTML files exist

Run before each build to ensure kanji index is consistent.

Usage:
    python3 build/verify_kanji_index.py           # Full verification
    python3 build/verify_kanji_index.py --quick   # Quick check (no entry counts)
    python3 build/verify_kanji_index.py --fix     # Attempt to fix issues
"""

import argparse
import json
import re
import sys
from pathlib import Path
from collections import Counter

FURIGANA_PATTERN = re.compile(r'\{([^|]+)\|([^}]+)\}')
KANJI_ID_PATTERN = re.compile(r'^(\d{5})_([a-z]+)_([a-z]+)_([a-z]+)$')

class VerificationError:
    def __init__(self, category: str, message: str, fixable: bool = False):
        self.category = category
        self.message = message
        self.fixable = fixable

    def __str__(self):
        fix_marker = " [FIXABLE]" if self.fixable else ""
        return f"[{self.category}] {self.message}{fix_marker}"

def strip_furigana(text: str) -> str:
    if not text:
        return ''
    return FURIGANA_PATTERN.sub(r'\1', text)

def is_kanji(char: str) -> bool:
    code = ord(char)
    return (
        (0x4E00 <= code <= 0x9FFF) or
        (0x3400 <= code <= 0x4DBF) or
        (0xF900 <= code <= 0xFAFF)
    )

def extract_kanji(headword: str) -> set:
    plain = strip_furigana(headword)
    return {char for char in plain if is_kanji(char)}

def verify_kanji_list(kanji_list_path: Path) -> tuple[dict, list]:
    """Verify kanji_list.json structure and content."""
    errors = []

    if not kanji_list_path.exists():
        errors.append(VerificationError("FILE", "kanji_list.json not found"))
        return {}, errors

    try:
        with open(kanji_list_path, 'r', encoding='utf-8') as f:
            kanji_list = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(VerificationError("JSON", f"kanji_list.json invalid: {e}"))
        return {}, errors

    # Check structure
    if 'metadata' not in kanji_list:
        errors.append(VerificationError("STRUCTURE", "kanji_list.json missing 'metadata'"))
    if 'kanji' not in kanji_list:
        errors.append(VerificationError("STRUCTURE", "kanji_list.json missing 'kanji'"))
        return {}, errors

    # Check each kanji entry
    kanji_ids_seen = []
    for kanji_char, data in kanji_list['kanji'].items():
        # Check required fields
        for field in ['kanji_id', 'onyomi', 'kunyomi', 'gloss']:
            if field not in data:
                errors.append(VerificationError(
                    "FIELD",
                    f"Kanji '{kanji_char}' missing field: {field}"
                ))

        if 'kanji_id' in data:
            kanji_id = data['kanji_id']
            kanji_ids_seen.append(kanji_id)

            # Verify ID format
            if not KANJI_ID_PATTERN.match(kanji_id):
                errors.append(VerificationError(
                    "FORMAT",
                    f"Invalid kanji ID format: {kanji_id}"
                ))

    # Check for duplicate IDs
    id_counts = Counter(kanji_ids_seen)
    for kid, count in id_counts.items():
        if count > 1:
            errors.append(VerificationError(
                "DUPLICATE",
                f"Duplicate kanji ID: {kid} (appears {count} times)"
            ))

    return kanji_list, errors

def verify_kanji_json_files(kanji_list: dict, kanji_dir: Path) -> list:
    """Verify individual kanji JSON files exist and are valid."""
    errors = []

    for kanji_char, data in kanji_list.get('kanji', {}).items():
        kanji_id = data.get('kanji_id', '')
        if not kanji_id:
            continue

        json_path = kanji_dir / f'{kanji_id}.json'
        if not json_path.exists():
            errors.append(VerificationError(
                "FILE",
                f"Missing kanji JSON: {json_path}",
                fixable=True
            ))
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                kanji_data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(VerificationError(
                "JSON",
                f"Invalid JSON in {json_path}: {e}"
            ))
            continue

        # Verify metadata
        meta = kanji_data.get('metadata', {})
        if meta.get('kanji') != kanji_char:
            errors.append(VerificationError(
                "MISMATCH",
                f"{json_path}: kanji mismatch (expected '{kanji_char}', got '{meta.get('kanji')}')"
            ))
        if meta.get('kanji_id') != kanji_id:
            errors.append(VerificationError(
                "MISMATCH",
                f"{json_path}: kanji_id mismatch"
            ))

    return errors

def verify_entry_counts(kanji_list: dict, entries_index: dict, kanji_dir: Path, quick: bool = False) -> list:
    """Verify entry counts in kanji JSON files match actual entries."""
    if quick:
        return []

    errors = []

    # Build actual counts
    actual_counts = {}
    for entry in entries_index.get('entries', []):
        headword = entry.get('headword', '')
        for k in extract_kanji(headword):
            actual_counts[k] = actual_counts.get(k, 0) + 1

    # Compare with JSON files
    for kanji_char, data in kanji_list.get('kanji', {}).items():
        kanji_id = data.get('kanji_id', '')
        if not kanji_id:
            continue

        json_path = kanji_dir / f'{kanji_id}.json'
        if not json_path.exists():
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                kanji_data = json.load(f)
        except json.JSONDecodeError:
            continue

        json_count = kanji_data.get('metadata', {}).get('entry_count', 0)
        actual_count = actual_counts.get(kanji_char, 0)

        if json_count != actual_count:
            errors.append(VerificationError(
                "COUNT",
                f"Kanji '{kanji_char}' count mismatch: JSON has {json_count}, actual is {actual_count}",
                fixable=True
            ))

    return errors

def verify_html_files(kanji_list: dict, docs_kanji_dir: Path) -> list:
    """Verify kanji HTML files exist."""
    errors = []

    for kanji_char, data in kanji_list.get('kanji', {}).items():
        kanji_id = data.get('kanji_id', '')
        if not kanji_id:
            continue

        html_path = docs_kanji_dir / f'{kanji_id}.html'
        if not html_path.exists():
            errors.append(VerificationError(
                "FILE",
                f"Missing kanji HTML: {html_path}",
                fixable=True
            ))

    return errors

def verify_completeness(kanji_list: dict, entries_index: dict) -> list:
    """Verify all kanji in entries have IDs assigned."""
    errors = []
    known_kanji = set(kanji_list.get('kanji', {}).keys())

    all_kanji = set()
    for entry in entries_index.get('entries', []):
        headword = entry.get('headword', '')
        all_kanji.update(extract_kanji(headword))

    missing = all_kanji - known_kanji
    if missing:
        errors.append(VerificationError(
            "INCOMPLETE",
            f"{len(missing)} kanji in entries lack IDs: {', '.join(sorted(missing)[:10])}{'...' if len(missing) > 10 else ''}"
        ))

    return errors

def main():
    parser = argparse.ArgumentParser(description='Verify kanji index integrity')
    parser.add_argument('--quick', action='store_true',
                        help='Skip entry count verification (faster)')
    parser.add_argument('--fix', action='store_true',
                        help='Attempt to fix issues by rebuilding')
    args = parser.parse_args()

    kanji_list_path = Path('kanji/kanji_list.json')
    kanji_dir = Path('kanji')
    docs_kanji_dir = Path('docs/kanji')
    entries_index_path = Path('entries_index.json')

    all_errors = []

    print("Verifying kanji index...")

    # 1. Verify kanji_list.json
    print("  Checking kanji_list.json...")
    kanji_list, errors = verify_kanji_list(kanji_list_path)
    all_errors.extend(errors)

    if not kanji_list:
        print("\nCannot continue without valid kanji_list.json")
        for e in all_errors:
            print(f"  {e}")
        sys.exit(1)

    # 2. Load entries index
    if entries_index_path.exists():
        with open(entries_index_path, 'r', encoding='utf-8') as f:
            entries_index = json.load(f)
    else:
        all_errors.append(VerificationError("FILE", "entries_index.json not found"))
        entries_index = {'entries': []}

    # 3. Verify completeness
    print("  Checking kanji completeness...")
    all_errors.extend(verify_completeness(kanji_list, entries_index))

    # 4. Verify kanji JSON files
    print("  Checking kanji JSON files...")
    all_errors.extend(verify_kanji_json_files(kanji_list, kanji_dir))

    # 5. Verify entry counts
    if not args.quick:
        print("  Checking entry counts...")
        all_errors.extend(verify_entry_counts(kanji_list, entries_index, kanji_dir))

    # 6. Verify HTML files
    print("  Checking kanji HTML files...")
    all_errors.extend(verify_html_files(kanji_list, docs_kanji_dir))

    # Report results
    print()
    if all_errors:
        print(f"Found {len(all_errors)} issue(s):")
        for e in all_errors:
            print(f"  {e}")

        fixable = [e for e in all_errors if e.fixable]
        if fixable and args.fix:
            print(f"\nAttempting to fix {len(fixable)} fixable issues...")
            import subprocess
            subprocess.run(['python3', 'build/update_kanji_index.py', '--rebuild-all'], check=True)
            subprocess.run(['python3', 'build/build_kanji_html.py'], check=True)
            print("Rebuild complete. Re-run verification to check.")

        sys.exit(1)
    else:
        kanji_count = len(kanji_list.get('kanji', {}))
        print(f"Kanji index verified: {kanji_count} kanji, no issues found.")
        sys.exit(0)

if __name__ == '__main__':
    main()
```

### Integration with Build Process

Add verification to `build/build_flat.py`:

```python
# At the start of main(), add:
import subprocess

# Verify kanji index before building
print("Verifying kanji index...")
result = subprocess.run(
    ['python3', 'build/verify_kanji_index.py', '--quick'],
    capture_output=True, text=True
)
if result.returncode != 0:
    print("Kanji index verification failed:")
    print(result.stdout)
    print(result.stderr)
    print("\nFix issues before building.")
    sys.exit(1)
```

## Usage

```bash
# Full verification
python3 build/verify_kanji_index.py

# Quick check (skip entry counts)
python3 build/verify_kanji_index.py --quick

# Attempt automatic fixes
python3 build/verify_kanji_index.py --fix
```

## Verification Checks

| Check | Description | Fixable |
|-------|-------------|---------|
| FILE | Files exist | Some |
| JSON | JSON is valid | No |
| STRUCTURE | Required fields present | No |
| FORMAT | Kanji ID format correct | No |
| DUPLICATE | No duplicate IDs | No |
| MISMATCH | Metadata matches | No |
| COUNT | Entry counts accurate | Yes |
| INCOMPLETE | All kanji have IDs | No |

## Exit Codes

- `0`: All checks passed
- `1`: One or more issues found

## Example Output

```
Verifying kanji index...
  Checking kanji_list.json...
  Checking kanji completeness...
  Checking kanji JSON files...
  Checking entry counts...
  Checking kanji HTML files...

Kanji index verified: 1500 kanji, no issues found.
```

Or with errors:

```
Found 3 issue(s):
  [COUNT] Kanji '食' count mismatch: JSON has 45, actual is 47 [FIXABLE]
  [FILE] Missing kanji HTML: docs/kanji/00123_new_atara_new.html [FIXABLE]
  [INCOMPLETE] 2 kanji in entries lack IDs: 鬱, 躊
```

## Next Step

Proceed to `10_initial_generation.md` for the one-time script to generate the complete kanji index.
