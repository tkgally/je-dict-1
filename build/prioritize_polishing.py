#!/usr/bin/env python3
"""Generate polishing priority lists for je-dict-1.

Scores every entry across multiple quality dimensions and generates
priority-ordered lists for each polishing task. Higher priority entries
(worst quality) are listed first.

Usage:
    python3 build/prioritize_polishing.py              # Generate all priority files
    python3 build/prioritize_polishing.py --summary    # Show statistics only
    python3 build/prioritize_polishing.py --task notes  # One task only
    python3 build/prioritize_polishing.py --dry-run    # Print to stdout
    python3 build/prioritize_polishing.py --limit 100  # Top N per task
"""

import argparse
import json
import os
import re
import sys
from datetime import date

# Add build dir to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from japanese_utils import FURIGANA_PATTERN, is_kanji

# Try to import the note quality scorer
try:
    from score_note_quality import score_entry as score_note, normalize_pos, load_templates
    _NOTE_SCORER_AVAILABLE = True
except ImportError:
    _NOTE_SCORER_AVAILABLE = False


# ---------------------------------------------------------------------------
# Entry loading
# ---------------------------------------------------------------------------

def load_all_entries(entries_dir):
    """Load all entry JSON files from the entries directory."""
    entries = []
    for range_dir in sorted(os.listdir(entries_dir)):
        range_path = os.path.join(entries_dir, range_dir)
        if not os.path.isdir(range_path):
            continue
        for fname in sorted(os.listdir(range_path)):
            if not fname.endswith('.json'):
                continue
            fpath = os.path.join(range_path, fname)
            try:
                with open(fpath) as f:
                    data = json.load(f)
                entry_id = fname.replace('.json', '')
                entries.append({'id': entry_id, 'data': data})
            except (json.JSONDecodeError, IOError):
                continue
    return entries


# ---------------------------------------------------------------------------
# Quality dimension scorers (each returns 0.0–1.0, where 1.0 = best)
# ---------------------------------------------------------------------------

def _text_has_bare_kanji(text):
    """Check if text has kanji not covered by furigana markup."""
    if not text:
        return False
    stripped = FURIGANA_PATTERN.sub('', text)
    return any(is_kanji(ch) for ch in stripped)


def score_note_quality(entry_data, templates=None):
    """Score note quality from 0.0 (worst) to 1.0 (best)."""
    if _NOTE_SCORER_AVAILABLE and templates is not None:
        pos = entry_data.get('part_of_speech', '')
        template_key = normalize_pos(pos)
        template = templates.get(template_key, templates.get('_default', {}))
        notes = entry_data.get('notes', '') or ''
        raw_score, _ = score_note(entry_data, notes, template)
        return raw_score / 100.0

    # Fallback: simple length heuristic
    notes = entry_data.get('notes', '') or ''
    length = len(notes)
    if length == 0:
        return 0.0
    if length < 50:
        return 0.1
    if length < 100:
        return 0.3
    if length < 200:
        return 0.5
    if length < 400:
        return 0.7
    return 0.9


def score_furigana_coverage(entry_data):
    """Score furigana coverage from 0.0 (bare kanji found) to 1.0 (all covered)."""
    notes = entry_data.get('notes', '') or ''
    examples = entry_data.get('examples', []) or []

    has_text = False
    has_bare = False

    if notes:
        has_text = True
        if _text_has_bare_kanji(notes):
            has_bare = True

    for ex in examples:
        jp = ex.get('japanese', '') or ''
        if jp:
            has_text = True
            if _text_has_bare_kanji(jp):
                has_bare = True
                break

    if not has_text:
        return 0.5  # neutral
    return 0.0 if has_bare else 1.0


def score_example_count(entry_data):
    """Score example count relative to minimum requirement. 0.0–1.0."""
    tier = (entry_data.get('metadata', {}) or {}).get('vocabulary_tier', 'general')
    min_per_sense = 5 if tier in ('basic', 'core') else 3

    senses = entry_data.get('definitions', []) or entry_data.get('senses', []) or []
    sense_count = max(len(senses), 1)
    required = min_per_sense * sense_count

    examples = entry_data.get('examples', []) or []
    count = len(examples)

    if count == 0:
        return 0.0
    return min(1.0, count / required)


def score_cross_refs(entry_data):
    """Score cross-reference count. 0.0–1.0."""
    prominent = entry_data.get('prominent_see_also', []) or []
    xrefs = entry_data.get('cross_references', []) or []
    total = len(prominent) + len(xrefs)

    if total == 0:
        return 0.0
    if total == 1:
        return 0.3
    if total == 2:
        return 0.6
    return 1.0


def score_transitivity_info(entry_data):
    """Score verb transitivity info presence. 0.0 or 1.0 (1.0 for non-verbs)."""
    pos = (entry_data.get('part_of_speech', '') or '').lower()
    if 'verb' not in pos:
        return 1.0  # not applicable

    notes = entry_data.get('notes', '') or ''
    keywords = ['transitive', 'intransitive', '自動詞', '他動詞', 'TRANSITIVITY']
    for kw in keywords:
        if kw.lower() in notes.lower():
            return 1.0
    return 0.0


# ---------------------------------------------------------------------------
# Task definitions
# ---------------------------------------------------------------------------

TASK_DIMENSIONS = {
    'notes': [('note_quality', 0.8), ('cross_refs', 0.2)],
    'furigana': [('furigana_coverage', 1.0)],
    'examples': [('example_count', 0.9), ('note_quality', 0.1)],
    'cross_refs': [('cross_refs', 0.7), ('transitivity_info', 0.3)],
}

TIER_WEIGHTS = {
    'basic': 3.0,
    'core': 2.0,
    'general': 1.0,
}

PRIORITY_FILES = {
    'notes': 'polishing/priority/notes.txt',
    'furigana': 'polishing/priority/furigana.txt',
    'examples': 'polishing/priority/examples.txt',
    'cross_refs': 'polishing/priority/cross_refs.txt',
}


# ---------------------------------------------------------------------------
# Priority computation
# ---------------------------------------------------------------------------

def compute_dimension_scores(entry_data, templates=None):
    """Compute all quality dimension scores for an entry."""
    return {
        'note_quality': score_note_quality(entry_data, templates),
        'furigana_coverage': score_furigana_coverage(entry_data),
        'example_count': score_example_count(entry_data),
        'cross_refs': score_cross_refs(entry_data),
        'transitivity_info': score_transitivity_info(entry_data),
    }


def compute_task_priority(dimension_scores, tier, task):
    """Compute priority score for a specific task. Higher = more urgent."""
    dimensions = TASK_DIMENSIONS[task]
    quality = sum(dimension_scores[dim] * weight for dim, weight in dimensions)
    tier_weight = TIER_WEIGHTS.get(tier, 1.0)
    return tier_weight * (1.0 - quality)


def compute_all_priorities(entries, templates=None):
    """Compute priority scores for all entries across all tasks.

    Returns dict: task -> list of (entry_id, priority, tier, dimension_scores)
    sorted by priority descending.
    """
    tasks = list(TASK_DIMENSIONS.keys())
    results = {task: [] for task in tasks}

    for entry in entries:
        data = entry['data']
        entry_id = entry['id']
        tier = (data.get('metadata', {}) or {}).get('vocabulary_tier', 'general') or 'general'
        dim_scores = compute_dimension_scores(data, templates)

        for task in tasks:
            priority = compute_task_priority(dim_scores, tier, task)
            if priority > 0:
                results[task].append((entry_id, priority, tier, dim_scores))

    # Sort each task by priority descending
    for task in tasks:
        results[task].sort(key=lambda x: (-x[1], x[0]))

    return results


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_priority_file(task, entries_list, total_entries, base_dir, limit=None):
    """Write a priority file for a task."""
    filepath = os.path.join(base_dir, PRIORITY_FILES[task])
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    items = entries_list[:limit] if limit else entries_list

    with open(filepath, 'w') as f:
        f.write(f"# Generated by prioritize_polishing.py on {date.today().isoformat()}\n")
        f.write(f"# Task: {task}\n")
        f.write(f"# Total entries: {total_entries}\n")
        f.write(f"# Entries with priority > 0: {len(entries_list)}\n")
        for entry_id, _priority, _tier, _scores in items:
            f.write(f"{entry_id}\n")

    return filepath


def print_dry_run(task, entries_list, limit=None):
    """Print priority list to stdout."""
    items = entries_list[:limit] if limit else entries_list
    print(f"# Task: {task}")
    print(f"# Entries with priority > 0: {len(entries_list)}")
    for entry_id, priority, tier, scores in items:
        primary_dim = TASK_DIMENSIONS[task][0][0]
        print(f"{entry_id}  (score: {priority:.2f}, tier: {tier}, {primary_dim}: {scores[primary_dim]:.2f})")
    print()


def print_summary(results, total_entries, base_dir):
    """Print priority statistics."""
    print("POLISHING PRIORITIES")
    print("====================")
    print()

    for task in TASK_DIMENSIONS:
        entries_list = results[task]
        print(f"Task: {task}")
        print(f"  Total entries: {total_entries:,}")
        print(f"  Entries needing work (priority > 0): {len(entries_list):,}")

        if entries_list:
            top_id, top_score, top_tier, top_scores = entries_list[0]
            primary_dim = TASK_DIMENSIONS[task][0][0]
            print(f"  Top priority: {top_id} (score: {top_score:.2f}, tier: {top_tier}, {primary_dim}: {top_scores[primary_dim]:.2f})")

        filepath = os.path.join(base_dir, PRIORITY_FILES[task])
        if os.path.exists(filepath):
            print(f"  Written to: {PRIORITY_FILES[task]}")
        print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Generate polishing priority lists.')
    parser.add_argument('--task', choices=list(TASK_DIMENSIONS.keys()),
                        help='Generate priority list for one task only')
    parser.add_argument('--limit', type=int, metavar='N',
                        help='Limit output to top N entries per task (default: all)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print priorities to stdout instead of writing files')
    parser.add_argument('--summary', action='store_true',
                        help='Show priority statistics without writing files')
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    entries_dir = os.path.join(base_dir, 'entries')

    # Load note templates if scorer is available
    templates = None
    if _NOTE_SCORER_AVAILABLE:
        templates_path = os.path.join(script_dir, 'note_templates.json')
        if os.path.exists(templates_path):
            templates = load_templates(templates_path)

    print("Loading entries...", file=sys.stderr)
    entries = load_all_entries(entries_dir)
    total = len(entries)
    print(f"Loaded {total:,} entries.", file=sys.stderr)

    print("Computing priorities...", file=sys.stderr)
    results = compute_all_priorities(entries, templates)

    # Filter to one task if requested
    if args.task:
        results = {args.task: results[args.task]}

    if args.summary:
        print_summary(results, total, base_dir)
        return

    if args.dry_run:
        for task in results:
            print_dry_run(task, results[task], args.limit)
        return

    # Write priority files
    for task in results:
        filepath = write_priority_file(task, results[task], total, base_dir, args.limit)
        count = len(results[task])
        if args.limit:
            count = min(count, args.limit)
        print(f"  {task}: {count:,} entries -> {PRIORITY_FILES[task]}", file=sys.stderr)

    print(file=sys.stderr)
    print_summary(results, total, base_dir)


if __name__ == '__main__':
    main()
