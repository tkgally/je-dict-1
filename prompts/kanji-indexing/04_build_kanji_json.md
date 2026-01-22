# Kanji Index Implementation - Step 4: Build Kanji Entry List JSON Files

## Overview

Create a script that generates individual JSON files for each kanji, containing the list of all dictionary entries that include that kanji in their headword.

## Prerequisites

- `kanji/kanji_list.json` must be complete (all kanji assigned IDs)
- `entries_index.json` contains all entry metadata

## Task

Create `build/build_kanji_json.py`:

### Functionality

1. **Load** `kanji/kanji_list.json` (kanji → kanji_id mapping)
2. **Load** `entries_index.json` (all entry metadata)
3. **For each kanji**:
   - Find all entries where the headword contains this kanji
   - Sort entries by reading (hiragana order)
   - Create a JSON file with the entry list
4. **Output** individual JSON files to `kanji/` directory

### Script Structure

```python
#!/usr/bin/env python3
"""
Build kanji index JSON files.

For each kanji in kanji_list.json, creates a JSON file listing all
dictionary entries that contain that kanji in their headword.
"""

import json
import re
from pathlib import Path
from datetime import datetime, timezone

# Furigana pattern
FURIGANA_PATTERN = re.compile(r'\{([^|]+)\|([^}]+)\}')

def strip_furigana(text: str) -> str:
    """Strip furigana notation, keeping only kanji."""
    if not text:
        return ''
    return FURIGANA_PATTERN.sub(r'\1', text)

def is_kanji(char: str) -> bool:
    """Check if a character is a kanji."""
    code = ord(char)
    return (
        (0x4E00 <= code <= 0x9FFF) or
        (0x3400 <= code <= 0x4DBF) or
        (0xF900 <= code <= 0xFAFF)
    )

def hiragana_sort_key(reading: str) -> str:
    """Generate a sort key for hiragana ordering."""
    # Standard hiragana ordering (gojuon order)
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
        'ゃゅょっ'
    )
    return ''.join(
        chr(order.find(c)) if c in order else c
        for c in reading
    )

def main():
    # Load kanji list
    with open('kanji/kanji_list.json', 'r', encoding='utf-8') as f:
        kanji_list = json.load(f)

    # Load entries index
    with open('entries_index.json', 'r', encoding='utf-8') as f:
        entries_index = json.load(f)

    # Build reverse mapping: kanji → list of entries
    kanji_to_entries = {k: [] for k in kanji_list['kanji']}

    for entry in entries_index['entries']:
        headword = entry.get('headword', '')
        plain_headword = strip_furigana(headword)

        for char in plain_headword:
            if char in kanji_to_entries:
                kanji_to_entries[char].append({
                    'id': entry['id'],
                    'headword': entry['headword'],
                    'reading': entry['reading'],
                    'gloss': entry['gloss']
                })

    # Generate JSON files for each kanji
    kanji_dir = Path('kanji')
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    for kanji_char, kanji_data in kanji_list['kanji'].items():
        kanji_id = kanji_data['kanji_id']
        entries = kanji_to_entries.get(kanji_char, [])

        # Sort by reading (hiragana order)
        entries_sorted = sorted(entries, key=lambda e: hiragana_sort_key(e['reading']))

        output = {
            'metadata': {
                'kanji': kanji_char,
                'kanji_id': kanji_id,
                'onyomi': kanji_data['onyomi'],
                'kunyomi': kanji_data['kunyomi'],
                'gloss': kanji_data['gloss'],
                'entry_count': len(entries_sorted),
                'generated': timestamp
            },
            'entries': entries_sorted
        }

        output_path = kanji_dir / f'{kanji_id}.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Generated {len(kanji_list['kanji'])} kanji JSON files in kanji/")

if __name__ == '__main__':
    main()
```

### Output Format

Each kanji gets a JSON file named `{kanji_id}.json`:

Example: `kanji/00001_jin_hito_person.json`
```json
{
  "metadata": {
    "kanji": "人",
    "kanji_id": "00001_jin_hito_person",
    "onyomi": "jin",
    "kunyomi": "hito",
    "gloss": "person",
    "entry_count": 245,
    "generated": "2026-01-22T10:30:00Z"
  },
  "entries": [
    {
      "id": "01234_akunin",
      "headword": "{悪|あく}{人|にん}",
      "reading": "あくにん",
      "gloss": "villain, bad person"
    },
    {
      "id": "02345_gaikokujin",
      "headword": "{外国|がいこく}{人|じん}",
      "reading": "がいこくじん",
      "gloss": "foreigner"
    },
    ...
  ]
}
```

The entries are sorted by reading in hiragana order (gojuon).

## Usage

```bash
python3 build/build_kanji_json.py
```

## Verification

After running:
1. Check that JSON files were created in `kanji/`
2. Verify file count matches total kanji count
3. Spot-check a few files to ensure:
   - Entries are sorted by reading
   - Entry counts are accurate
   - Metadata is complete

## Git Ignore

Add to `.gitignore` if kanji JSON files should be generated rather than committed:
```
# If treating as build artifacts:
kanji/*.json
!kanji/kanji_list.json
!kanji/kanji_extracted.json
```

Or commit them if they should be tracked (recommended for faster builds).

## Next Step

Proceed to `05_build_kanji_html.md` to create the script that generates HTML pages from the kanji JSON files.
