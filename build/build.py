#!/usr/bin/env python3
"""
Build script for je-dict-1 dictionary.

Compiles all entry files into optimized format for the web application:
- entries.json: All entry data
- index.json: Search index for quick lookups
- recent entries list: Most recently added/modified entries
"""

import json
import sys
import shutil
import re
from pathlib import Path
from datetime import datetime
from validate import validate_all_entries, hiragana_to_romaji


# Pattern to match furigana notation: {kanji|reading}
FURIGANA_PATTERN = re.compile(r'\{([^|]+)\|[^}]+\}')


def strip_furigana(text: str) -> str:
    """
    Strip furigana notation from text, keeping only the kanji.
    Example: {学校|がっこう} -> 学校
    """
    return FURIGANA_PATTERN.sub(r'\1', text)


def load_entry(file_path: Path) -> dict:
    """Load a single entry file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_search_index(entries: list[dict]) -> dict:
    """
    Build a search index mapping searchable terms to entry IDs.

    Index keys:
    - Japanese headword (kanji)
    - Reading (hiragana)
    - Romaji
    - English glosses
    """
    index = {
        'japanese': {},   # headword/reading -> [entry_ids]
        'romaji': {},     # romaji -> [entry_ids]
        'english': {},    # lowercase english words -> [entry_ids]
    }

    for entry in entries:
        entry_id = entry['id']

        # Index headword (strip furigana for clean kanji matching)
        headword = entry['headword']
        headword_clean = strip_furigana(headword)
        if headword_clean not in index['japanese']:
            index['japanese'][headword_clean] = []
        index['japanese'][headword_clean].append(entry_id)

        # Index reading
        reading = entry['reading']
        if reading not in index['japanese']:
            index['japanese'][reading] = []
        if entry_id not in index['japanese'][reading]:
            index['japanese'][reading].append(entry_id)

        # Index romaji
        romaji = hiragana_to_romaji(reading)
        if romaji not in index['romaji']:
            index['romaji'][romaji] = []
        index['romaji'][romaji].append(entry_id)

        # Index English glosses
        glosses = [entry['gloss']]
        if 'definitions' in entry and entry['definitions']:
            for defn in entry['definitions']:
                if 'gloss' in defn:
                    glosses.append(defn['gloss'])

        for gloss in glosses:
            # Split into words and index each
            words = gloss.lower().replace(',', ' ').replace(';', ' ').split()
            for word in words:
                # Remove common punctuation
                word = word.strip('()[].')
                if len(word) < 2:
                    continue
                if word not in index['english']:
                    index['english'][word] = []
                if entry_id not in index['english'][word]:
                    index['english'][word].append(entry_id)

    return index


def build_recent_entries(entries: list[dict], limit: int = 250) -> list[dict]:
    """
    Build a list of recently added or modified entries.

    Returns a list of dicts with:
    - id: entry ID
    - headword: the headword text
    - gloss: the short gloss
    - status: 'NEW' or 'REVISED'
    - date: formatted date string (YYYY.M.D)
    """
    # Sort entries by modified date, most recent first
    def get_modified_date(entry):
        try:
            return datetime.fromisoformat(entry['metadata']['modified'].replace('Z', '+00:00'))
        except (KeyError, ValueError):
            return datetime.min.replace(tzinfo=None)

    sorted_entries = sorted(entries, key=get_modified_date, reverse=True)

    recent = []
    for entry in sorted_entries[:limit]:
        metadata = entry.get('metadata', {})
        created = metadata.get('created', '')
        modified = metadata.get('modified', '')

        # Determine if NEW or REVISED
        status = 'NEW' if created == modified else 'REVISED'

        # Format date as YYYY.M.D
        try:
            dt = datetime.fromisoformat(modified.replace('Z', '+00:00'))
            date_str = f"{dt.year}.{dt.month}.{dt.day}"
        except (ValueError, AttributeError):
            date_str = ''

        recent.append({
            'id': entry['id'],
            'headword': entry['headword'],
            'gloss': entry['gloss'],
            'status': status,
            'date': date_str
        })

    return recent


def copy_web_files(project_root: Path, dist_dir: Path):
    """Copy web application files to dist directory, including nested directories."""
    web_dir = project_root / 'web'

    for item in web_dir.iterdir():
        dest = dist_dir / item.name
        if item.is_file():
            shutil.copy(item, dest)
        elif item.is_dir():
            # Use copytree with dirs_exist_ok=True to handle existing directories
            shutil.copytree(item, dest, dirs_exist_ok=True)


def generate_data_js(entries: list[dict], index: dict, recent: list[dict], dist_dir: Path) -> Path:
    """
    Generate a data.js file with embedded dictionary data.
    This allows the app to work without a server (pure file:// access).
    """
    data_js_path = dist_dir / 'data.js'

    entries_dict = {e['id']: e for e in entries}

    content = f"""// Auto-generated dictionary data - do not edit manually
// Generated: {datetime.utcnow().isoformat()}Z

const DICTIONARY_DATA = {{
  version: '1.0',
  count: {len(entries)},
  entries: {json.dumps(entries_dict, ensure_ascii=False, indent=2)}
}};

const DICTIONARY_INDEX = {{
  version: '1.0',
  index: {json.dumps(index, ensure_ascii=False, indent=2)}
}};

const DICTIONARY_RECENT = {json.dumps(recent, ensure_ascii=False, indent=2)};
"""

    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return data_js_path


def build(project_root: Path) -> int:
    """
    Main build process.
    Returns 0 on success, 1 on failure.
    """
    dist_dir = project_root / 'docs'

    print("je-dict-1 Build")
    print("=" * 50)

    # Step 1: Validate all entries
    print("\n[1/5] Validating entries...")
    total, valid, invalid_files, cross_ref_warnings = validate_all_entries(project_root)

    if invalid_files:
        print(f"  ERROR: {len(invalid_files)} invalid file(s) found")
        print("  Run validate.py for details")
        return 1

    if cross_ref_warnings:
        print(f"  WARNING: {len(cross_ref_warnings)} cross-reference issue(s) found")
        print("  Run validate.py for details")

    if total == 0:
        print("  WARNING: No entry files found")
        # Continue anyway to create empty dictionary

    print(f"  OK: {valid} entries validated")

    # Step 2: Load all entries
    print("\n[2/5] Loading entries...")
    entries = []
    entries_dir = project_root / 'entries'

    for file_path in entries_dir.glob('**/*.json'):
        entries.append(load_entry(file_path))

    # Sort entries by reading (gojuon order approximated by romaji)
    entries.sort(key=lambda e: hiragana_to_romaji(e['reading']))

    print(f"  Loaded {len(entries)} entries")

    # Step 3: Build search index
    print("\n[3/5] Building search index...")
    index = build_search_index(entries)

    jp_terms = len(index['japanese'])
    romaji_terms = len(index['romaji'])
    en_terms = len(index['english'])
    print(f"  Indexed: {jp_terms} Japanese, {romaji_terms} romaji, {en_terms} English terms")

    # Step 4: Build recent entries list
    print("\n[4/5] Building recent entries list...")
    recent = build_recent_entries(entries, limit=250)
    print(f"  Found {len(recent)} recent entries")

    # Step 5: Write output files
    print("\n[5/5] Writing output files...")

    # Ensure dist directory exists
    dist_dir.mkdir(exist_ok=True)

    # Copy web files first
    copy_web_files(project_root, dist_dir)
    print(f"  Copied web files to docs/")

    # Generate data.js with embedded data (for offline/static use)
    data_js_path = generate_data_js(entries, index, recent, dist_dir)
    print(f"  Written: {data_js_path.relative_to(project_root)}")

    # Summary
    print("\n" + "=" * 50)
    print("Build complete!")
    print(f"  Total entries: {len(entries)}")
    print(f"  Output: {dist_dir}")
    print("\nTo view the dictionary:")
    print(f"  Open {dist_dir / 'index.html'} in your browser")

    return 0


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    sys.exit(build(project_root))


if __name__ == '__main__':
    main()
