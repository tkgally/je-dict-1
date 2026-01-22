# Kanji Index Implementation - Step 7: Update Entry Creation/Modification Scripts

## Overview

Modify the workflow scripts to update the kanji index when entries are created or modified.

## Context

When a new entry is added to the dictionary or an existing entry's headword changes, the kanji index needs to be updated. This involves:

1. Adding new kanji to `kanji_list.json` if they don't exist
2. Rebuilding the affected kanji JSON files
3. Rebuilding the affected kanji HTML pages

## Task

### 1. Create `build/update_kanji_index.py`

This script updates the kanji index after entries change:

```python
#!/usr/bin/env python3
"""
Update kanji index after entry changes.

This script:
1. Checks for new kanji that need IDs assigned
2. Rebuilds kanji JSON files for affected kanji
3. Optionally rebuilds kanji HTML pages

Usage:
    python3 build/update_kanji_index.py              # Full update
    python3 build/update_kanji_index.py --check-new  # Only check for new kanji
    python3 build/update_kanji_index.py --rebuild-all  # Rebuild all kanji files
"""

import argparse
import json
import re
from pathlib import Path
from datetime import datetime, timezone

FURIGANA_PATTERN = re.compile(r'\{([^|]+)\|([^}]+)\}')

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

def hiragana_sort_key(reading: str) -> str:
    order = (
        'あいうえおかきくけこがぎぐげご'
        'さしすせそざじずぜぞ'
        'たちつてとだぢづでど'
        'なにぬねの'
        'はひふへほばびぶべぼぱぴぷぺぽ'
        'まみむめも'
        'やゆよ'
        'らりるれろ'
        'わをん'
    )
    return ''.join(chr(order.find(c)) if c in order else c for c in reading)

def check_new_kanji():
    """Check if there are kanji in entries not yet in kanji_list.json."""
    # Load current kanji list
    kanji_list_path = Path('kanji/kanji_list.json')
    if kanji_list_path.exists():
        with open(kanji_list_path, 'r', encoding='utf-8') as f:
            kanji_list = json.load(f)
        known_kanji = set(kanji_list.get('kanji', {}).keys())
    else:
        known_kanji = set()

    # Load entries
    with open('entries_index.json', 'r', encoding='utf-8') as f:
        entries = json.load(f)

    # Find all kanji in entries
    all_kanji = set()
    for entry in entries['entries']:
        headword = entry.get('headword', '')
        all_kanji.update(extract_kanji(headword))

    # Find new kanji
    new_kanji = all_kanji - known_kanji
    return new_kanji

def rebuild_kanji_json(kanji_chars: set = None):
    """Rebuild kanji JSON files for specified kanji (or all if None)."""
    # Load kanji list
    with open('kanji/kanji_list.json', 'r', encoding='utf-8') as f:
        kanji_list = json.load(f)

    # Load entries
    with open('entries_index.json', 'r', encoding='utf-8') as f:
        entries_index = json.load(f)

    # Determine which kanji to rebuild
    if kanji_chars is None:
        kanji_chars = set(kanji_list['kanji'].keys())

    # Build mapping: kanji -> entries
    kanji_to_entries = {k: [] for k in kanji_chars}
    for entry in entries_index['entries']:
        headword = entry.get('headword', '')
        entry_kanji = extract_kanji(headword)
        for k in entry_kanji:
            if k in kanji_to_entries:
                kanji_to_entries[k].append({
                    'id': entry['id'],
                    'headword': entry['headword'],
                    'reading': entry['reading'],
                    'gloss': entry['gloss']
                })

    # Generate JSON files
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    kanji_dir = Path('kanji')

    for k in kanji_chars:
        if k not in kanji_list['kanji']:
            continue

        kanji_info = kanji_list['kanji'][k]
        kanji_id = kanji_info['kanji_id']
        entries = kanji_to_entries.get(k, [])
        entries_sorted = sorted(entries, key=lambda e: hiragana_sort_key(e['reading']))

        output = {
            'metadata': {
                'kanji': k,
                'kanji_id': kanji_id,
                'onyomi': kanji_info['onyomi'],
                'kunyomi': kanji_info['kunyomi'],
                'gloss': kanji_info['gloss'],
                'entry_count': len(entries_sorted),
                'generated': timestamp
            },
            'entries': entries_sorted
        }

        output_path = kanji_dir / f'{kanji_id}.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

    return len(kanji_chars)

def main():
    parser = argparse.ArgumentParser(description='Update kanji index')
    parser.add_argument('--check-new', action='store_true',
                        help='Only check for new kanji needing IDs')
    parser.add_argument('--rebuild-all', action='store_true',
                        help='Rebuild all kanji JSON files')
    args = parser.parse_args()

    if args.check_new:
        new_kanji = check_new_kanji()
        if new_kanji:
            print(f"Found {len(new_kanji)} new kanji needing IDs:")
            for k in sorted(new_kanji):
                print(f"  {k}")
            print("\nRun step 03 (assign_kanji_ids) to assign IDs to these kanji.")
        else:
            print("No new kanji found. All kanji have IDs assigned.")
        return

    # Check for new kanji first
    new_kanji = check_new_kanji()
    if new_kanji:
        print(f"Warning: {len(new_kanji)} kanji need IDs assigned:")
        for k in sorted(new_kanji)[:10]:
            print(f"  {k}")
        if len(new_kanji) > 10:
            print(f"  ... and {len(new_kanji) - 10} more")
        print("\nRun with --check-new to see all, or assign IDs first.")
        return

    # Rebuild kanji JSON files
    if args.rebuild_all:
        count = rebuild_kanji_json()
        print(f"Rebuilt all {count} kanji JSON files")
    else:
        # Smart update: only rebuild kanji that have changed entries
        # For simplicity, rebuild all (can be optimized later)
        count = rebuild_kanji_json()
        print(f"Updated {count} kanji JSON files")

if __name__ == '__main__':
    main()
```

### 2. Modify `build/update_indexes.py`

Add kanji index update to the existing index update script:

```python
# Add to the end of update_indexes.py main():

# Update kanji index
import subprocess
result = subprocess.run(
    ['python3', 'build/update_kanji_index.py', '--check-new'],
    capture_output=True, text=True
)
if 'new kanji' in result.stdout.lower():
    print("\n" + result.stdout)
```

### 3. Modify `build/build_flat.py`

Add kanji HTML rebuilding to the main build script. At the end of `main()`:

```python
# Rebuild kanji index HTML pages
print("Rebuilding kanji index pages...")
import subprocess
subprocess.run(['python3', 'build/build_kanji_json.py'], check=True)
subprocess.run(['python3', 'build/build_kanji_html.py'], check=True)
print("Kanji index pages rebuilt.")
```

### 4. Update Workflow in `prompts/newentries.md`

Add kanji index check to the entry creation workflow:

```markdown
3. **After all 30 entries**:
   ```bash
   python3 build/validate.py
   python3 build/update_indexes.py
   python3 build/update_kanji_index.py --check-new  # NEW: Check for new kanji
   python3 build/build_flat.py
   ```

   **If new kanji are found**: New kanji need on'yomi, kun'yomi, and gloss assigned.
   Run the kanji ID assignment process before building.
```

## Integration Points

### When Entries Are Created

1. New entry is written to `entries/`
2. `validate.py` runs
3. `update_indexes.py` runs (updates `entries_index.json`)
4. `update_kanji_index.py --check-new` checks for new kanji
5. If new kanji found: assign IDs (manual Claude step)
6. `build_flat.py` rebuilds everything including kanji pages

### When Entry Headwords Change

Same flow as creation - the kanji JSON files are rebuilt to reflect the change.

### During Full Site Build

`build_flat.py` automatically:
1. Rebuilds all entry HTML pages
2. Calls `build_kanji_json.py` to rebuild kanji JSON files
3. Calls `build_kanji_html.py` to rebuild kanji HTML pages

## Handling New Kanji

When a new entry introduces a kanji not in `kanji_list.json`:

1. `update_kanji_index.py --check-new` reports the new kanji
2. Human/Claude assigns the on'yomi, kun'yomi, and gloss
3. The new kanji is added to `kanji_list.json`
4. Build continues normally

This is necessary because readings cannot be determined programmatically.

## Verification

```bash
# Check for new kanji
python3 build/update_kanji_index.py --check-new

# Rebuild all kanji JSON files
python3 build/update_kanji_index.py --rebuild-all

# Full build (includes kanji pages)
python3 build/build_flat.py
```

## Next Step

Proceed to `08_create_skill.md` to create the kanji-index Claude skill.
