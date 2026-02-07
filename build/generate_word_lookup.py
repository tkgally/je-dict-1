#!/usr/bin/env python3
"""
Generate a word-ID lookup table for inline linking sessions.

Scans all dictionary entries and produces build/word_id_lookup.json,
a mapping from readings to entry IDs with headword and gloss for
disambiguation. This allows Claude to resolve word→entry_id without
running per-word Python search snippets.

Usage:
    python build/generate_word_lookup.py

Output format:
{
  "metadata": { "generated": "...", "total_entries": N, "total_readings": M },
  "by_reading": {
    "ほん": [
      { "id": "00111_hon", "headword": "本", "gloss": "book", "tier": "basic" }
    ],
    ...
  },
  "by_headword": {
    "本": [
      { "id": "00111_hon", "reading": "ほん", "gloss": "book", "tier": "basic" }
    ],
    ...
  }
}
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add build/ to path so we can import project modules
sys.path.insert(0, str(Path(__file__).parent))

from japanese_utils import strip_furigana


def generate_word_lookup():
    """Scan all entries and generate the word-ID lookup table."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'
    output_file = script_dir / 'word_id_lookup.json'

    if not entries_dir.exists():
        print(f"Error: entries directory not found at {entries_dir}")
        return False

    by_reading = {}
    by_headword = {}
    total_entries = 0

    for entry_path in sorted(entries_dir.rglob('*.json')):
        try:
            with open(entry_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: Failed to read {entry_path}: {e}")
            continue

        entry_id = data.get('id', '')
        headword_raw = data.get('headword', '')
        headword = strip_furigana(headword_raw)
        reading = data.get('reading', '')
        gloss = data.get('gloss', '')
        tier = data.get('metadata', {}).get('vocabulary_tier', '')

        if not entry_id or not reading:
            continue

        total_entries += 1

        # Truncate gloss to keep file size manageable
        short_gloss = gloss[:80] if len(gloss) > 80 else gloss

        # Index by reading
        reading_entry = {
            'id': entry_id,
            'headword': headword,
            'gloss': short_gloss,
            'tier': tier
        }
        by_reading.setdefault(reading, []).append(reading_entry)

        # Index by headword (stripped of furigana)
        if headword and headword != reading:
            headword_entry = {
                'id': entry_id,
                'reading': reading,
                'gloss': short_gloss,
                'tier': tier
            }
            by_headword.setdefault(headword, []).append(headword_entry)

    # Sort entries within each reading/headword group by tier priority then ID
    tier_order = {'basic': 0, 'core': 1, 'general': 2, '': 3}
    for entries in by_reading.values():
        entries.sort(key=lambda e: (tier_order.get(e['tier'], 3), e['id']))
    for entries in by_headword.values():
        entries.sort(key=lambda e: (tier_order.get(e['tier'], 3), e['id']))

    lookup = {
        'metadata': {
            'description': 'Word-ID lookup table for inline linking sessions',
            'generated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'total_entries': total_entries,
            'total_readings': len(by_reading),
            'total_headwords': len(by_headword)
        },
        'by_reading': dict(sorted(by_reading.items())),
        'by_headword': dict(sorted(by_headword.items()))
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(lookup, f, ensure_ascii=False, indent=2)

    file_size_kb = output_file.stat().st_size / 1024
    print(f"Generated {output_file} ({file_size_kb:.0f} KB)")
    print(f"  {total_entries} entries, {len(by_reading)} readings, {len(by_headword)} headwords")

    return True


if __name__ == '__main__':
    success = generate_word_lookup()
    sys.exit(0 if success else 1)
