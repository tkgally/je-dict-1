#!/usr/bin/env python3
"""
Build script for flat HTML version of je-dict-1 dictionary.

Generates static HTML pages for each dictionary entry, plus navigation pages.
This version works without JavaScript and is SEO-friendly.

Build performance profile (10,306 entries, measured 2026-02-06):
--------------------------------------------------------------
  Load entries                                    4.1s   (10%)
  Setup directories (copy preserved dirs)         3.7s   ( 9%)
  Entry HTML generation (entry_renderer.py)       6.8s   (17%)
  Navigation pages (page_generators.py)           0.2s   (<1%)
  Search index (search_index_builder.py)          0.5s   ( 1%)
  Stylesheet                                      0.0s   (<1%)
  Atomic swap (shutil.move + rmtree)             23.1s   (57%)
  Kanji index rebuild (build_kanji_*.py)          1.9s   ( 5%)
  Sitemap generation (build_sitemap.py)           0.1s   (<1%)
  TOTAL                                          40.4s

Key observations:
  - The atomic swap (shutil.move of ~12k HTML files + rmtree of backup) dominates
    at 57% of build time. This is filesystem I/O overhead from moving and deleting
    the docs/ directory tree containing 10k+ entry pages plus kanji pages.
  - Entry HTML generation is the second-largest phase at 17%. This involves
    rendering 10,306 entries through entry_renderer.generate_entry_html(), each
    with furigana processing, cross-reference resolution, and inline word links.
  - Loading entries (10%) involves reading and parsing 10,306 JSON files from disk.
  - Directory setup (9%) copies preserved dirs (flat/, kanji/) to the temp build dir.

Potential optimization strategies:
  - Incremental build: only regenerate changed entries (see 01_code_prompt_19).
    This would avoid the full atomic swap and reduce entry generation proportionally.
  - In-place build: write directly to docs/ instead of temp dir + swap. Faster but
    risks leaving docs/ in a broken state if build fails mid-way.
  - Parallel entry generation: entry pages are independent; multiprocessing could
    speed up the entry_renderer phase.
  - Reduce swap overhead: instead of moving entire directory trees, use symlinks
    or rename individual files.
"""

import argparse
import json
import os
import shutil
import sys
import subprocess
import time
from collections import defaultdict
from pathlib import Path
from datetime import datetime

from path_utils import get_directory_range
from entry_renderer import (
    generate_entry_html,
    JST,
)
from search_index_builder import (
    generate_search_index,
    generate_search_js,
    generate_tag_search_js,
)
from page_generators import (
    generate_index_page,
    generate_advanced_page,
    generate_browse_page,
    generate_recent_page,
    generate_random_page,
    generate_pending_page,
    generate_kanji_list_page,
    build_recent_entries,
)

# Canonical CNAME for GitHub Pages custom domain
# This ensures the CNAME file is always restored even if accidentally deleted
GITHUB_PAGES_CNAME = "www.tkgje.jp"


def generate_stylesheet() -> str:
    """Generate the shared CSS stylesheet for the flat site."""
    css_path = Path(__file__).parent / 'templates' / 'styles.css'
    try:
        return css_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: Template file not found: {css_path}")
        sys.exit(1)


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


def build_flat(project_root: Path, quick: bool = False) -> int:
    """
    Build the flat HTML version of the dictionary.
    Returns 0 on success, 1 on failure.

    If quick=True, only regenerates entry pages whose source JSON is newer
    than the corresponding HTML file. Writes directly to docs/ (no atomic swap).
    """
    docs_dir = project_root / 'docs'
    entries_dir = project_root / 'entries'

    mode_label = "Flat HTML Build (quick/incremental)" if quick else "Flat HTML Build"
    print(f"\n{mode_label}")
    print("=" * 50)

    build_start = time.time()
    timings = {}

    # Step 1: Load all entries
    print("\n[1/6] Loading entries...")
    phase_start = time.time()
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

    timings['1_load_entries'] = time.time() - phase_start

    if quick:
        # Quick mode: write directly to docs/ (no temp dir, no atomic swap)
        print("\n[2/6] Preparing output directories (quick mode)...")
        phase_start = time.time()

        original_docs_dir = docs_dir
        docs_dir.mkdir(parents=True, exist_ok=True)
        entries_output_dir = docs_dir / 'entries'
        entries_output_dir.mkdir(parents=True, exist_ok=True)

        print(f"  Using existing {docs_dir}")
        timings['2_setup_directories'] = time.time() - phase_start

        # Step 3: Generate only changed entry pages
        print("\n[3/6] Generating entry pages (incremental)...")
        phase_start = time.time()
        regenerated = 0
        skipped = 0
        for entry in entries:
            dir_range = get_directory_range(entry['id'])
            output_dir = entries_output_dir / dir_range
            output_path = output_dir / f"{entry['id']}.html"
            source_path = Path(entry['_source_file'])

            # Compare mtimes: regenerate if HTML missing or JSON is newer
            if output_path.exists():
                source_mtime = os.path.getmtime(source_path)
                html_mtime = os.path.getmtime(output_path)
                if source_mtime <= html_mtime:
                    skipped += 1
                    continue

            # Regenerate this entry
            entry_html = generate_entry_html(entry, entries_dict, readings_to_entries)
            output_dir.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(entry_html)
            regenerated += 1

        print(f"  Regenerated {regenerated} entry pages, skipped {skipped} unchanged")
    else:
        # Full mode: atomic build pattern (temp dir + swap)
        # Step 2: Create output directories
        print("\n[2/6] Creating output directories...")
        phase_start = time.time()

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

        timings['2_setup_directories'] = time.time() - phase_start

        # Step 3: Generate all entry pages
        print("\n[3/6] Generating entry pages...")
        phase_start = time.time()
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

    # Count vocabulary tiers and examples
    tier_counts = {'basic': 0, 'core': 0, 'general': 0, 'unassigned': 0}
    total_examples = 0
    for entry in entries:
        tier = entry.get('metadata', {}).get('vocabulary_tier', '')
        if tier in ('basic', 'core', 'general'):
            tier_counts[tier] += 1
        else:
            tier_counts['unassigned'] += 1
        total_examples += len(entry.get('examples', []))

    # Generate build timestamp in JST
    build_time = datetime.now(JST)
    build_time_jst = f"{build_time.year}.{build_time.month}.{build_time.day} {build_time.hour}:{build_time.minute:02d}"

    timings['3_entry_pages'] = time.time() - phase_start

    # Step 4: Generate navigation pages
    print("\n[4/6] Generating navigation pages...")
    phase_start = time.time()

    # Index page (with search form)
    with open(docs_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(generate_index_page(len(entries), tier_counts, total_examples, build_time_jst))

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

    # Kanji list page (kanji by headword frequency)
    kanji_list_file = project_root / 'kanji' / 'kanji_list.json'
    if kanji_list_file.exists():
        with open(kanji_list_file, 'r', encoding='utf-8') as f:
            kanji_list_data = json.load(f)
        with open(docs_dir / 'kanji.html', 'w', encoding='utf-8') as f:
            f.write(generate_kanji_list_page(entries, kanji_list_data))

    print("  Generated index.html, advanced.html, browse.html, recent.html, random.html, pending.html, kanji.html")

    timings['4_navigation_pages'] = time.time() - phase_start

    # Step 5: Generate search index and JavaScript
    print("\n[5/6] Generating search index...")
    phase_start = time.time()
    with open(docs_dir / 'search-index.js', 'w', encoding='utf-8') as f:
        f.write(generate_search_index(entries))

    with open(docs_dir / 'search.js', 'w', encoding='utf-8') as f:
        f.write(generate_search_js())

    with open(docs_dir / 'tag-search.js', 'w', encoding='utf-8') as f:
        f.write(generate_tag_search_js())

    print("  Generated search-index.js, search.js, tag-search.js")

    timings['5_search_index'] = time.time() - phase_start

    # Step 6: Generate stylesheet
    print("\n[6/6] Generating stylesheet...")
    phase_start = time.time()
    with open(docs_dir / 'styles.css', 'w', encoding='utf-8') as f:
        f.write(generate_stylesheet())
    print("  Generated styles.css")

    timings['6_stylesheet'] = time.time() - phase_start

    if quick:
        # Quick mode: no swap needed, already wrote to docs/ directly
        print("\n[Swap] Skipped (quick mode — wrote directly to docs/)")
        timings['7_atomic_swap'] = 0
    else:
        # Atomic swap: replace original docs/ with newly built temp_dir
        # Use shutil.move() instead of Path.rename() to handle cross-device moves
        print("\n[Swap] Atomically replacing output directory...")
        phase_start = time.time()
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

        timings['7_atomic_swap'] = time.time() - phase_start

    # Rebuild kanji index HTML pages
    print("\n[Kanji] Rebuilding kanji index pages...")
    phase_start = time.time()
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

    timings['8_kanji_rebuild'] = time.time() - phase_start

    # Generate sitemap and robots.txt
    phase_start = time.time()
    from build_sitemap import build_sitemap
    sitemap_result = build_sitemap(project_root)
    if sitemap_result != 0:
        print("  WARNING: Sitemap generation had issues")

    timings['9_sitemap'] = time.time() - phase_start
    total_time = time.time() - build_start

    # Summary
    print("\n" + "=" * 50)
    print("Build complete!")
    print(f"  Total entries: {len(entries)}")
    print(f"  Output: {original_docs_dir}")

    # Timing breakdown
    print("\n" + "-" * 50)
    print("Build timing breakdown:")
    print("-" * 50)
    phase_labels = {
        '1_load_entries': 'Load entries',
        '2_setup_directories': 'Setup directories',
        '3_entry_pages': 'Entry HTML generation (entry_renderer)',
        '4_navigation_pages': 'Navigation pages (page_generators)',
        '5_search_index': 'Search index (search_index_builder)',
        '6_stylesheet': 'Stylesheet',
        '7_atomic_swap': 'Atomic swap',
        '8_kanji_rebuild': 'Kanji index rebuild',
        '9_sitemap': 'Sitemap generation',
    }
    for key, label in phase_labels.items():
        elapsed = timings.get(key, 0)
        pct = (elapsed / total_time * 100) if total_time > 0 else 0
        print(f"  {label:<45s} {elapsed:6.2f}s  ({pct:5.1f}%)")
    print(f"  {'TOTAL':<45s} {total_time:6.2f}s")
    print("-" * 50)

    print("\nTo view the dictionary:")
    print(f"  Open {original_docs_dir / 'index.html'} in your browser")

    return 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Build flat HTML dictionary site')
    parser.add_argument('--quick', action='store_true',
                        help='Incremental build: only regenerate entries whose JSON is newer than HTML')
    args = parser.parse_args()

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

    sys.exit(build_flat(project_root, quick=args.quick))


if __name__ == '__main__':
    main()
