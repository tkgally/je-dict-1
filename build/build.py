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
from datetime import datetime, timezone, timedelta
from validate import validate_all_entries, hiragana_to_romaji
from resolve_links import resolve_cross_references, generate_link_report

# Japan Standard Time (UTC+9)
JST = timezone(timedelta(hours=9))


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


def format_jst_datetime(iso_string: str) -> str:
    """
    Format an ISO datetime string to JST format: YYYY.M.D H:MM
    Example: 2026.1.9 14:35
    """
    try:
        dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
        dt_jst = dt.astimezone(JST)
        return f"{dt_jst.year}.{dt_jst.month}.{dt_jst.day} {dt_jst.hour}:{dt_jst.minute:02d}"
    except (ValueError, AttributeError):
        return ''


def build_recent_entries(entries: list[dict], limit: int = 250) -> list[dict]:
    """
    Build a list of recently added or modified entries.

    Returns a list of dicts with:
    - id: entry ID
    - headword: the headword text
    - gloss: the short gloss
    - status: 'NEW' or 'REVISED'
    - date: formatted date string in JST (YYYY.M.D H:MM)
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
        modified = metadata.get('modified', '')

        # Determine if NEW or REVISED
        created = metadata.get('created', '')
        status = 'NEW' if created == modified else 'REVISED'

        # Format date as YYYY.M.D H:MM in JST
        date_str = format_jst_datetime(modified)

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


def extract_audio_files(entries: list[dict], dist_dir: Path) -> int:
    """
    Extract audio data from entries and write to separate JSON files.

    For each example with an 'audio' field, writes a file to docs/audio/
    with format: {entry_id}-ex{number}.json containing {"audio_base64": "..."}

    Returns the number of audio files written.
    """
    audio_dir = dist_dir / 'audio'
    audio_dir.mkdir(exist_ok=True)

    audio_count = 0

    for entry in entries:
        entry_id = entry['id']
        examples = entry.get('examples', [])

        for idx, example in enumerate(examples):
            if 'audio' in example:
                # Write audio to separate file
                audio_filename = f"{entry_id}-ex{idx + 1}.json"
                audio_path = audio_dir / audio_filename

                audio_data = {'audio_base64': example['audio']}
                with open(audio_path, 'w', encoding='utf-8') as f:
                    json.dump(audio_data, f, ensure_ascii=False)

                audio_count += 1

    return audio_count


def strip_audio_from_entries(entries: list[dict]) -> list[dict]:
    """
    Create a copy of entries with audio data stripped from examples.

    Replaces 'audio' field with 'has_audio': true to indicate audio is available.
    This keeps data.js smaller while allowing the UI to know which examples have audio.
    """
    import copy

    stripped = []
    for entry in entries:
        entry_copy = copy.deepcopy(entry)
        examples = entry_copy.get('examples', [])

        for example in examples:
            if 'audio' in example:
                del example['audio']
                example['has_audio'] = True

        stripped.append(entry_copy)

    return stripped


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
    print("\n[1/7] Validating entries...")
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
    print("\n[2/7] Loading entries...")
    entries = []
    entries_dir = project_root / 'entries'

    for file_path in entries_dir.glob('**/*.json'):
        entries.append(load_entry(file_path))

    # Sort entries by reading (gojuon order approximated by romaji)
    entries.sort(key=lambda e: hiragana_to_romaji(e['reading']))

    print(f"  Loaded {len(entries)} entries")

    # Step 3: Resolve cross-references
    print("\n[3/7] Resolving cross-references...")
    entries, pending_links = resolve_cross_references(entries)

    # Count resolved vs pending
    total_refs = 0
    resolved_refs = 0
    for entry in entries:
        for ref in entry.get('cross_references', []):
            total_refs += 1
            if ref.get('resolved'):
                resolved_refs += 1

    if total_refs > 0:
        print(f"  Cross-references: {resolved_refs}/{total_refs} resolved ({resolved_refs * 100 // total_refs}%)")
        if pending_links:
            print(f"  Pending links: {len(pending_links)} unique targets")
    else:
        print("  No cross-references found")

    # Step 4: Build search index
    print("\n[4/7] Building search index...")
    index = build_search_index(entries)

    jp_terms = len(index['japanese'])
    romaji_terms = len(index['romaji'])
    en_terms = len(index['english'])
    print(f"  Indexed: {jp_terms} Japanese, {romaji_terms} romaji, {en_terms} English terms")

    # Step 5: Build recent entries list
    print("\n[5/7] Building recent entries list...")
    recent = build_recent_entries(entries, limit=250)
    print(f"  Found {len(recent)} recent entries")

    # Step 6: Extract audio files
    print("\n[6/7] Extracting audio files...")
    audio_count = extract_audio_files(entries, dist_dir)
    if audio_count > 0:
        print(f"  Extracted {audio_count} audio files to docs/audio/")
    else:
        print("  No audio files to extract")

    # Step 7: Write output files
    print("\n[7/7] Writing output files...")

    # Ensure dist directory exists
    dist_dir.mkdir(exist_ok=True)

    # Copy web files first
    copy_web_files(project_root, dist_dir)
    print(f"  Copied web files to docs/")

    # Strip audio from entries before writing to data.js
    entries_for_output = strip_audio_from_entries(entries)

    # Generate data.js with embedded data (for offline/static use)
    data_js_path = generate_data_js(entries_for_output, index, recent, dist_dir)
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
