#!/usr/bin/env python3
"""
Build script for je-dict-1 dictionary.

Compiles all entry files into optimized format for the web application:
- entries.json: All entry data
- index.json: Search index for quick lookups
"""

import json
import sys
import shutil
from pathlib import Path
from datetime import datetime
from validate import validate_all_entries, hiragana_to_romaji


def load_entry(file_path: Path) -> dict:
    """Load a single entry file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_new_entries_list(project_root: Path) -> list[str]:
    """
    Load list of entry IDs marked as 'new' from new_entries.txt.
    Returns a list of entry IDs.
    """
    new_entries_file = project_root / 'build' / 'new_entries.txt'
    new_ids = []

    if new_entries_file.exists():
        with open(new_entries_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith('#'):
                    new_ids.append(line)

    return new_ids


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

        # Index headword
        headword = entry['headword']
        if headword not in index['japanese']:
            index['japanese'][headword] = []
        index['japanese'][headword].append(entry_id)

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


def copy_web_files(project_root: Path, dist_dir: Path):
    """Copy web application files to dist directory."""
    web_dir = project_root / 'web'

    for file in web_dir.glob('*'):
        if file.is_file():
            shutil.copy(file, dist_dir / file.name)


def generate_data_js(entries: list[dict], index: dict, new_entries: list[str], dist_dir: Path) -> Path:
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

const NEW_ENTRIES = {json.dumps(new_entries, ensure_ascii=False)};
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
    print("\n[1/4] Validating entries...")
    total, valid, invalid_files = validate_all_entries(project_root)

    if invalid_files:
        print(f"  ERROR: {len(invalid_files)} invalid file(s) found")
        print("  Run validate.py for details")
        return 1

    if total == 0:
        print("  WARNING: No entry files found")
        # Continue anyway to create empty dictionary

    print(f"  OK: {valid} entries validated")

    # Step 2: Load all entries
    print("\n[2/4] Loading entries...")
    entries = []
    entries_dir = project_root / 'entries'
    variants_dir = project_root / 'variants'

    for file_path in list(entries_dir.glob('**/*.json')) + list(variants_dir.glob('**/*.json')):
        entries.append(load_entry(file_path))

    # Sort entries by reading (gojuon order approximated by romaji)
    entries.sort(key=lambda e: hiragana_to_romaji(e['reading']))

    print(f"  Loaded {len(entries)} entries")

    # Load new entries list
    new_entries = load_new_entries_list(project_root)
    if new_entries:
        print(f"  Marked as new: {len(new_entries)} entries")

    # Step 3: Build search index
    print("\n[3/4] Building search index...")
    index = build_search_index(entries)

    jp_terms = len(index['japanese'])
    romaji_terms = len(index['romaji'])
    en_terms = len(index['english'])
    print(f"  Indexed: {jp_terms} Japanese, {romaji_terms} romaji, {en_terms} English terms")

    # Step 4: Write output files
    print("\n[4/4] Writing output files...")

    # Ensure dist directory exists
    dist_dir.mkdir(exist_ok=True)

    # Copy web files first
    copy_web_files(project_root, dist_dir)
    print(f"  Copied web files to docs/")

    # Generate data.js with embedded data (for offline/static use)
    data_js_path = generate_data_js(entries, index, new_entries, dist_dir)
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
