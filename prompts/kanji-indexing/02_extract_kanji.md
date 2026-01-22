# Kanji Index Implementation - Step 2: Extract Kanji Script

## Overview

Create a script that extracts all unique kanji characters from dictionary entry headwords. This script will produce a list of kanji that need to be assigned kanji index IDs.

## Task

Create `build/extract_kanji_from_entries.py`:

### Functionality

1. **Read all entries** from `entries_index.json`
2. **Extract headwords** and strip furigana notation (e.g., `{余|あま}る` → `余る`)
3. **Identify kanji characters** - A character is kanji if its Unicode code point falls within:
   - CJK Unified Ideographs: U+4E00 to U+9FFF
   - CJK Unified Ideographs Extension A: U+3400 to U+4DBF
   - CJK Compatibility Ideographs: U+F900 to U+FAFF
4. **Collect unique kanji** across all headwords
5. **Output a JSON file** listing all unique kanji with placeholder IDs

### Script Structure

```python
#!/usr/bin/env python3
"""
Extract all unique kanji from dictionary entry headwords.

This script scans entries_index.json and identifies all kanji characters
used in headwords, outputting a list that needs kanji index IDs assigned.
"""

import json
import re
from pathlib import Path

# Furigana pattern from japanese_utils.py
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
        (0x4E00 <= code <= 0x9FFF) or    # CJK Unified Ideographs
        (0x3400 <= code <= 0x4DBF) or    # CJK Extension A
        (0xF900 <= code <= 0xFAFF)       # CJK Compatibility
    )

def extract_kanji_from_headword(headword: str) -> set:
    """Extract all kanji characters from a headword."""
    plain = strip_furigana(headword)
    return {char for char in plain if is_kanji(char)}

def main():
    # Load entries index
    with open('entries_index.json', 'r', encoding='utf-8') as f:
        index = json.load(f)

    # Collect all unique kanji
    all_kanji = set()
    kanji_to_entries = {}  # Track which entries use each kanji

    for entry in index['entries']:
        headword = entry.get('headword', '')
        entry_id = entry.get('id', '')
        kanji_chars = extract_kanji_from_headword(headword)

        for kanji in kanji_chars:
            all_kanji.add(kanji)
            if kanji not in kanji_to_entries:
                kanji_to_entries[kanji] = []
            kanji_to_entries[kanji].append(entry_id)

    # Sort kanji by frequency (most common first)
    sorted_kanji = sorted(all_kanji, key=lambda k: -len(kanji_to_entries[k]))

    # Output results
    output = {
        "metadata": {
            "description": "Kanji extracted from entry headwords - needs ID assignment",
            "total_kanji": len(sorted_kanji),
            "total_entries_scanned": len(index['entries'])
        },
        "kanji": [
            {
                "character": k,
                "entry_count": len(kanji_to_entries[k]),
                "kanji_id": None,  # To be assigned
                "onyomi": None,    # To be assigned
                "kunyomi": None,   # To be assigned
                "gloss": None      # To be assigned
            }
            for k in sorted_kanji
        ]
    }

    # Write output
    output_path = Path('kanji/kanji_extracted.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(sorted_kanji)} unique kanji from {len(index['entries'])} entries")
    print(f"Output written to: {output_path}")

    # Show top 20 most common kanji
    print("\nTop 20 most common kanji:")
    for k in sorted_kanji[:20]:
        print(f"  {k}: {len(kanji_to_entries[k])} entries")

if __name__ == '__main__':
    main()
```

### Output Format

The script creates `kanji/kanji_extracted.json`:
```json
{
  "metadata": {
    "description": "Kanji extracted from entry headwords - needs ID assignment",
    "total_kanji": 1234,
    "total_entries_scanned": 7839
  },
  "kanji": [
    {
      "character": "人",
      "entry_count": 245,
      "kanji_id": null,
      "onyomi": null,
      "kunyomi": null,
      "gloss": null
    },
    ...
  ]
}
```

## Verification

After running the script:
1. Check that `kanji/kanji_extracted.json` was created
2. Verify the kanji count is reasonable (expect 1000-2000 unique kanji)
3. Verify the output includes characters like 人, 日, 大, etc.

## Usage

```bash
python3 build/extract_kanji_from_entries.py
```

## Next Step

Proceed to `03_assign_kanji_ids.md` to assign on'yomi, kun'yomi, and glosses to each kanji.
