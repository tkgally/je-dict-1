#!/usr/bin/env python3
"""
Build script for flat HTML version of je-dict-1 dictionary.

Generates static HTML pages for each dictionary entry, plus navigation pages.
This version works without JavaScript and is SEO-friendly.
"""

import json
import shutil
import html
import sys
import subprocess
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone

from path_utils import get_directory_range
from japanese_utils import (
    hiragana_to_romaji,
    strip_furigana
)
from entry_renderer import (
    generate_entry_html,
    process_furigana,
    JST,
)
from page_generators import (
    generate_index_page,
    generate_advanced_page,
    generate_browse_page,
    generate_recent_page,
    generate_random_page,
    generate_pending_page,
    build_recent_entries,
)

# Canonical CNAME for GitHub Pages custom domain
# This ensures the CNAME file is always restored even if accidentally deleted
GITHUB_PAGES_CNAME = "www.tkgje.jp"


def generate_search_index(entries: list) -> str:
    """Generate the compact search index JavaScript file."""
    # Build index using sets for O(1) duplicate detection
    # Sets are converted to lists at the end for JSON serialization
    index_sets = {
        'japanese': {},
        'romaji': {},
        'english': {}
    }

    # Build entries lookup with minimal data
    entries_data = {}

    for entry in entries:
        entry_id = entry['id']
        headword = entry['headword']
        reading = entry['reading']
        gloss = entry.get('gloss', '')
        dir_range = get_directory_range(entry_id)

        # Get tags
        tags = entry.get('metadata', {}).get('tags', {})
        tier = entry.get('metadata', {}).get('vocabulary_tier', 'general')

        # Store minimal entry data for display
        # Note: headword is HTML-escaped by process_furigana(); gloss and reading
        # are escaped here to prevent XSS when rendered via innerHTML in search.js
        entries_data[entry_id] = {
            'id': entry_id,
            'headword': process_furigana(headword),
            'reading': html.escape(reading),
            'romaji': hiragana_to_romaji(reading),
            'gloss': html.escape(gloss),
            'dirRange': dir_range,
            'tier': tier,
            'tags': {
                'pos': tags.get('pos', []),
                'formality': tags.get('formality'),
                'politeness': tags.get('politeness'),
                'transitivity': tags.get('transitivity'),
                'semantic': tags.get('semantic', []),
                'style': tags.get('style', []),
                'domain': tags.get('domain', [])
            }
        }

        # Index headword (stripped)
        headword_clean = strip_furigana(headword)
        if headword_clean not in index_sets['japanese']:
            index_sets['japanese'][headword_clean] = set()
        index_sets['japanese'][headword_clean].add(entry_id)

        # Index reading
        if reading not in index_sets['japanese']:
            index_sets['japanese'][reading] = set()
        index_sets['japanese'][reading].add(entry_id)

        # Index romaji
        romaji = hiragana_to_romaji(reading)
        if romaji not in index_sets['romaji']:
            index_sets['romaji'][romaji] = set()
        index_sets['romaji'][romaji].add(entry_id)

        # Index English gloss words
        glosses = [gloss]
        for defn in entry.get('definitions', []):
            if 'gloss' in defn:
                glosses.append(defn['gloss'])

        for g in glosses:
            words = g.lower().replace(',', ' ').replace(';', ' ').split()
            for word in words:
                word = word.strip('()[].')
                if len(word) < 2:
                    continue
                if word not in index_sets['english']:
                    index_sets['english'][word] = set()
                index_sets['english'][word].add(entry_id)

    # Convert sets to lists for JSON serialization
    index = {
        'japanese': {k: list(v) for k, v in index_sets['japanese'].items()},
        'romaji': {k: list(v) for k, v in index_sets['romaji'].items()},
        'english': {k: list(v) for k, v in index_sets['english'].items()}
    }

    # Generate JavaScript
    js_content = f'''// Auto-generated search index - do not edit manually
// Generated: {datetime.now(timezone.utc).isoformat()}

window.SEARCH_INDEX = {json.dumps(index, ensure_ascii=False)};

window.SEARCH_ENTRIES = {json.dumps(entries_data, ensure_ascii=False)};
'''

    return js_content


def generate_search_js() -> str:
    """Generate the search.js JavaScript file."""
    js_path = Path(__file__).parent / 'templates' / 'search.js'
    return js_path.read_text(encoding='utf-8')


def generate_tag_search_js() -> str:
    """Generate the tag-search.js JavaScript file for tag-based filtering."""
    js_path = Path(__file__).parent / 'templates' / 'tag-search.js'
    return js_path.read_text(encoding='utf-8')


def generate_stylesheet() -> str:
    """Generate the shared CSS stylesheet for the flat site."""
    css_path = Path(__file__).parent / 'templates' / 'styles.css'
    return css_path.read_text(encoding='utf-8')


def load_entry(file_path: Path) -> dict:
    """Load a single entry file.

    Raises:
        ValueError: If the JSON file is malformed, with the file path included in the error message.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {file_path}: {e}") from e


def build_flat(project_root: Path) -> int:
    """
    Build the flat HTML version of the dictionary.
    Returns 0 on success, 1 on failure.
    """
    docs_dir = project_root / 'docs'
    entries_dir = project_root / 'entries'

    print("\nFlat HTML Build")
    print("=" * 50)

    # Step 1: Load all entries
    print("\n[1/6] Loading entries...")
    entries = []
    for file_path in entries_dir.glob('**/*.json'):
        entry = load_entry(file_path)
        entry['_source_file'] = str(file_path)
        entries.append(entry)

    # Sort entries by reading
    entries.sort(key=lambda e: e['reading'])
    print(f"  Loaded {len(entries)} entries")

    # Check for duplicate IDs before creating dictionary
    seen_ids = {}
    for e in entries:
        entry_id = e['id']
        if entry_id in seen_ids:
            print(f"  ERROR: Duplicate entry ID '{entry_id}' found!")
            print(f"    First occurrence: {seen_ids[entry_id]}")
            print(f"    Second occurrence: {e.get('_source_file', 'unknown')}")
            sys.exit(1)
        else:
            seen_ids[entry_id] = e.get('_source_file', 'unknown')

    # Create entries dictionary for cross-reference lookups
    entries_dict = {e['id']: e for e in entries}

    # Create reading-to-entries mapping for resolving cross-references
    # Maps reading -> list of {id, headword} for deterministic resolution
    readings_to_entries = defaultdict(list)
    for e in entries:
        readings_to_entries[e['reading']].append({
            'id': e['id'],
            'headword': e.get('headword', '')
        })

    # Step 2: Create output directories (atomic build pattern)
    print("\n[2/6] Creating output directories...")

    # Build to a temporary directory first, then swap atomically
    # This ensures a failed build doesn't leave docs/ in a broken state
    temp_dir = project_root / 'docs_build_temp'
    backup_dir = project_root / 'docs_backup'
    preserved_dirs = {'flat', 'kanji'}  # Directories to preserve
    preserved_files = {'about.html', 'CNAME'}  # Files to preserve (not overwritten by build)

    # Clean up any leftover temp/backup dirs from previous failed builds
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    if backup_dir.exists():
        shutil.rmtree(backup_dir)

    temp_dir.mkdir(parents=True, exist_ok=True)

    # Copy preserved directories from existing docs/ to temp build dir
    if docs_dir.exists():
        for preserved in preserved_dirs:
            src = docs_dir / preserved
            if src.exists():
                shutil.copytree(src, temp_dir / preserved)
        # Copy preserved files
        for preserved_file in preserved_files:
            src = docs_dir / preserved_file
            if src.exists():
                shutil.copy2(src, temp_dir / preserved_file)

    # Ensure about.html exists with content (manually-edited file, not generated)
    # If missing or empty, try to restore from git history
    about_path = temp_dir / 'about.html'
    if not about_path.exists() or about_path.stat().st_size == 0:
        print(f"  WARNING: about.html is missing or empty - attempting git restore")
        try:
            # Get about.html from the most recent commit where it had content
            result = subprocess.run(
                ['git', 'log', '--oneline', '--diff-filter=M', '-1', '--', 'docs/about.html'],
                capture_output=True, text=True, cwd=project_root
            )
            if result.returncode == 0 and result.stdout.strip():
                commit_hash = result.stdout.strip().split()[0]
                # Try to get content from parent of deletion commit
                restore_result = subprocess.run(
                    ['git', 'show', f'{commit_hash}:docs/about.html'],
                    capture_output=True, text=True, cwd=project_root
                )
                if restore_result.returncode == 0 and restore_result.stdout.strip():
                    with open(about_path, 'w', encoding='utf-8') as f:
                        f.write(restore_result.stdout)
                    print(f"  Restored about.html from git commit {commit_hash}")
                else:
                    print(f"  ERROR: Could not restore about.html from git - file may need manual restoration")
            else:
                print(f"  ERROR: Could not find about.html in git history - file may need manual restoration")
        except Exception as e:
            print(f"  ERROR: Git restore failed for about.html: {e}")

    # Always ensure CNAME file exists with canonical content
    # This protects against accidental deletion of the custom domain config
    cname_path = temp_dir / 'CNAME'
    if not cname_path.exists():
        print(f"  WARNING: CNAME file was missing - restoring from canonical value")
        with open(cname_path, 'w', encoding='utf-8') as f:
            f.write(GITHUB_PAGES_CNAME + '\n')
    else:
        # Verify CNAME has correct content
        with open(cname_path, 'r', encoding='utf-8') as f:
            current_cname = f.read().strip()
        if current_cname != GITHUB_PAGES_CNAME:
            print(f"  WARNING: CNAME had unexpected content '{current_cname}' - fixing")
            with open(cname_path, 'w', encoding='utf-8') as f:
                f.write(GITHUB_PAGES_CNAME + '\n')

    # Use temp_dir for all build output (reassign docs_dir for the build)
    original_docs_dir = docs_dir
    docs_dir = temp_dir

    # Entry directories will be created dynamically with range subdirectories
    entries_output_dir = docs_dir / 'entries'

    print(f"  Created {docs_dir}")

    # Step 3: Generate entry pages
    print("\n[3/6] Generating entry pages...")
    for entry in entries:
        dir_range = get_directory_range(entry['id'])
        entry_html = generate_entry_html(entry, entries_dict, readings_to_entries)
        # Create directory structure: entries/{range}/
        output_dir = entries_output_dir / dir_range
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{entry['id']}.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(entry_html)
    print(f"  Generated {len(entries)} entry pages")

    # Count vocabulary tiers
    tier_counts = {'basic': 0, 'core': 0, 'general': 0, 'unassigned': 0}
    for entry in entries:
        tier = entry.get('metadata', {}).get('vocabulary_tier', '')
        if tier in ('basic', 'core', 'general'):
            tier_counts[tier] += 1
        else:
            tier_counts['unassigned'] += 1

    # Generate build timestamp in JST
    build_time = datetime.now(JST)
    build_time_jst = f"{build_time.year}.{build_time.month}.{build_time.day} {build_time.hour}:{build_time.minute:02d}"

    # Step 4: Generate navigation pages
    print("\n[4/6] Generating navigation pages...")

    # Index page (with search form)
    with open(docs_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(generate_index_page(len(entries), tier_counts, build_time_jst))

    # Advanced search page (tag-based)
    with open(docs_dir / 'advanced.html', 'w', encoding='utf-8') as f:
        f.write(generate_advanced_page())

    # Browse page
    with open(docs_dir / 'browse.html', 'w', encoding='utf-8') as f:
        f.write(generate_browse_page(entries, entries_dict))

    # Recent page
    recent_entries = build_recent_entries(entries)
    with open(docs_dir / 'recent.html', 'w', encoding='utf-8') as f:
        f.write(generate_recent_page(recent_entries, entries_dict))

    # Random page
    with open(docs_dir / 'random.html', 'w', encoding='utf-8') as f:
        f.write(generate_random_page(entries))

    # Pending page (candidate words)
    candidate_file = project_root / 'candidate_words.json'
    if candidate_file.exists():
        with open(candidate_file, 'r', encoding='utf-8') as f:
            candidate_data = json.load(f)
            candidates = candidate_data.get('candidates', [])
        with open(docs_dir / 'pending.html', 'w', encoding='utf-8') as f:
            f.write(generate_pending_page(candidates))

    print("  Generated index.html, advanced.html, browse.html, recent.html, random.html, pending.html")

    # Step 5: Generate search index and JavaScript
    print("\n[5/6] Generating search index...")
    with open(docs_dir / 'search-index.js', 'w', encoding='utf-8') as f:
        f.write(generate_search_index(entries))

    with open(docs_dir / 'search.js', 'w', encoding='utf-8') as f:
        f.write(generate_search_js())

    with open(docs_dir / 'tag-search.js', 'w', encoding='utf-8') as f:
        f.write(generate_tag_search_js())

    print("  Generated search-index.js, search.js, tag-search.js")

    # Step 6: Generate stylesheet
    print("\n[6/6] Generating stylesheet...")
    with open(docs_dir / 'styles.css', 'w', encoding='utf-8') as f:
        f.write(generate_stylesheet())
    print("  Generated styles.css")

    # Atomic swap: replace original docs/ with newly built temp_dir
    # Use shutil.move() instead of Path.rename() to handle cross-device moves
    print("\n[Swap] Atomically replacing output directory...")
    try:
        # Move original docs/ to backup (if it exists)
        if original_docs_dir.exists():
            shutil.move(str(original_docs_dir), str(backup_dir))

        # Move temp build to docs/
        shutil.move(str(docs_dir), str(original_docs_dir))

        # Remove backup after successful swap
        if backup_dir.exists():
            shutil.rmtree(backup_dir)

        print("  Swap complete")
    except OSError as e:
        print(f"  ERROR: Failed to swap directories: {e}")
        print(f"  Build output remains in: {temp_dir}")
        # Try to restore backup if swap failed midway
        if backup_dir.exists() and not original_docs_dir.exists():
            shutil.move(str(backup_dir), str(original_docs_dir))
        return 1

    # Final about.html verification (safety check after swap)
    final_about_path = original_docs_dir / 'about.html'
    if not final_about_path.exists() or final_about_path.stat().st_size == 0:
        print("\n[about.html] WARNING: about.html is missing or empty after build!")
        print("  This is a manually-edited file. Please restore it from git:")
        print("  git show HEAD~1:docs/about.html > docs/about.html")
    else:
        print("\n[about.html] Verified: About page file intact")

    # Final CNAME verification (safety check after swap)
    final_cname_path = original_docs_dir / 'CNAME'
    if not final_cname_path.exists():
        print("\n[CNAME] ERROR: CNAME file missing after build - restoring!")
        with open(final_cname_path, 'w', encoding='utf-8') as f:
            f.write(GITHUB_PAGES_CNAME + '\n')
        print(f"  Restored CNAME with: {GITHUB_PAGES_CNAME}")
    else:
        with open(final_cname_path, 'r', encoding='utf-8') as f:
            final_cname = f.read().strip()
        if final_cname != GITHUB_PAGES_CNAME:
            print(f"\n[CNAME] WARNING: CNAME has wrong content - fixing!")
            with open(final_cname_path, 'w', encoding='utf-8') as f:
                f.write(GITHUB_PAGES_CNAME + '\n')
            print(f"  Fixed CNAME: '{final_cname}' -> '{GITHUB_PAGES_CNAME}'")
        else:
            print("\n[CNAME] Verified: GitHub Pages custom domain file intact")

    # Rebuild kanji index HTML pages
    print("\n[Kanji] Rebuilding kanji index pages...")
    kanji_json_script = project_root / 'build' / 'build_kanji_json.py'
    kanji_html_script = project_root / 'build' / 'build_kanji_html.py'
    if kanji_json_script.exists() and kanji_html_script.exists():
        try:
            subprocess.run([sys.executable, str(kanji_json_script)], check=True, cwd=str(project_root))
            subprocess.run([sys.executable, str(kanji_html_script)], check=True, cwd=str(project_root))
            print("  Kanji index pages rebuilt.")
        except subprocess.CalledProcessError as e:
            print(f"  ERROR: Kanji rebuild failed: {e}")
            print("  Build cannot continue without kanji index pages.")
            return 1
    else:
        print("  ERROR: Kanji build scripts not found!")
        print("  Build cannot continue without kanji index pages.")
        return 1

    # Verify kanji HTML files were created
    kanji_html_dir = original_docs_dir / 'kanji'
    if not kanji_html_dir.exists():
        print("  ERROR: docs/kanji/ directory was not created!")
        return 1
    kanji_html_count = len(list(kanji_html_dir.glob('*.html')))
    kanji_list_path = project_root / 'kanji' / 'kanji_list.json'
    if kanji_list_path.exists():
        with open(kanji_list_path, 'r', encoding='utf-8') as f:
            expected_count = len(json.load(f).get('kanji', {}))
        if kanji_html_count != expected_count:
            print(f"  ERROR: Expected {expected_count} kanji HTML files but found {kanji_html_count}")
            return 1
        print(f"  Verified: {kanji_html_count} kanji HTML files created")

    # Generate sitemap and robots.txt
    from build_sitemap import build_sitemap
    sitemap_result = build_sitemap(project_root)
    if sitemap_result != 0:
        print("  WARNING: Sitemap generation had issues")

    # Summary
    print("\n" + "=" * 50)
    print("Build complete!")
    print(f"  Total entries: {len(entries)}")
    print(f"  Output: {original_docs_dir}")
    print("\nTo view the dictionary:")
    print(f"  Open {original_docs_dir / 'index.html'} in your browser")

    return 0


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Verify kanji index before building
    print("Verifying kanji index...")
    result = subprocess.run(
        [sys.executable, str(script_dir / 'verify_kanji_index.py'), '--quick'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("Kanji index verification failed:")
        print(result.stdout)
        print(result.stderr)
        print("\nFix issues before building.")
        sys.exit(1)

    sys.exit(build_flat(project_root))


if __name__ == '__main__':
    main()
