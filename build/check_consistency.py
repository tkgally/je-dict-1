#!/usr/bin/env python3
"""
Check entry consistency across the dictionary.

Detects structural and cross-entry consistency issues:
1. Note structure vs POS templates
2. Cross-reference asymmetry (summary from find_merge_candidates)
3. Note length outliers
4. Verbs missing transitivity labels
5. Entries without collocations
6. Example count gaps

Usage:
    python3 build/check_consistency.py                    # Full report
    python3 build/check_consistency.py --json             # Machine-readable output
    python3 build/check_consistency.py --fix-list         # Entry IDs only
    python3 build/check_consistency.py --issue note-length # Single issue type
    python3 build/check_consistency.py --tier basic       # Filter by tier
"""

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from japanese_utils import strip_furigana


# --- Entry loading ---

def load_all_entries() -> list[dict]:
    """Load all entry JSON files from the entries directory."""
    entries_dir = PROJECT_ROOT / 'entries'
    entries = []
    for file_path in sorted(entries_dir.glob('**/*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entries.append(json.load(f))
        except (json.JSONDecodeError, IOError):
            pass
    return entries


def get_tier(entry: dict) -> str:
    return entry.get('metadata', {}).get('vocabulary_tier', 'general')


def get_pos_tags(entry: dict) -> list[str]:
    return entry.get('metadata', {}).get('tags', {}).get('pos', [])


def get_semantic_tags(entry: dict) -> list[str]:
    return entry.get('metadata', {}).get('tags', {}).get('semantic', [])


def is_verb(entry: dict) -> bool:
    return any(p.startswith('verb') for p in get_pos_tags(entry))


def is_na_adjective(entry: dict) -> bool:
    return 'adjective-na' in get_pos_tags(entry)


def is_noun(entry: dict) -> bool:
    return 'noun' in get_pos_tags(entry)


def headword_display(entry: dict) -> str:
    return strip_furigana(entry.get('headword', ''))


# --- Check 1: Note structure vs POS templates ---

def _load_note_templates() -> dict | None:
    """Load note_templates.json if it exists."""
    path = SCRIPT_DIR / 'note_templates.json'
    if path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return None


# Fallback keyword lists by POS category
VERB_KEYWORDS = [
    'transitiv', 'intransitiv', '自動詞', '他動詞',
    'particle', 'collocation', 'aspect', 'similar',
    'ている', 'COLLOCATION', 'PARTICLE', 'ASPECT',
]
NA_ADJ_KEYWORDS = [
    'usage', 'collocation', 'similar', 'predicate', 'modifier',
    'COLLOCATION', 'USAGE',
]
NOUN_KEYWORDS = [
    'collocation', 'compound', 'similar', 'usage',
    'COLLOCATION', 'COMPOUND', 'USAGE',
]


def check_note_structure(entries: list[dict]) -> list[dict]:
    """Check notes against expected sections for each POS."""
    templates = _load_note_templates()
    issues = []

    for entry in entries:
        notes = entry.get('notes', '') or ''
        if not notes:
            continue  # No notes at all is a different issue

        pos_tags = get_pos_tags(entry)
        notes_lower = notes.lower()

        # Determine which keywords to check
        keywords = None
        pos_category = None
        if any(p.startswith('verb') for p in pos_tags):
            keywords = VERB_KEYWORDS
            pos_category = 'verb'
        elif 'adjective-na' in pos_tags:
            keywords = NA_ADJ_KEYWORDS
            pos_category = 'na-adjective'
        elif 'noun' in pos_tags:
            keywords = NOUN_KEYWORDS
            pos_category = 'noun'

        if keywords is None:
            continue

        # If templates exist, use expected_sections as keywords instead
        if templates:
            for pos_tag in pos_tags:
                tmpl = templates.get(pos_tag)
                if tmpl and 'expected_sections' in tmpl:
                    keywords = tmpl['expected_sections']
                    break

        # Check if notes contain at least one keyword
        has_any = any(kw.lower() in notes_lower for kw in keywords)
        if not has_any:
            issues.append({
                'entry_id': entry['id'],
                'headword': headword_display(entry),
                'tier': get_tier(entry),
                'pos_category': pos_category,
                'detail': f'{pos_category} entry missing expected note sections',
            })

    return issues


# --- Check 2: Cross-reference asymmetry (summary) ---

def check_crossref_asymmetry() -> dict:
    """Get cross-reference asymmetry summary from find_merge_candidates."""
    try:
        result = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / 'find_merge_candidates.py'),
             '--asymmetry-only', '--json'],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode != 0:
            return {'error': 'find_merge_candidates.py returned non-zero'}

        data = json.loads(result.stdout)
        asym_refs = data.get('asymmetric_references', [])
        stats = data.get('asymmetry_stats', {})

        # Collect entry IDs involved
        entry_ids = set()
        for ref in asym_refs:
            entry_ids.add(ref['source_id'])
            entry_ids.add(ref['target_id'])

        return {
            'asymmetric_pairs': len(asym_refs),
            'entry_ids_involved': sorted(entry_ids),
            'stats': stats,
        }
    except FileNotFoundError:
        return {'error': 'find_merge_candidates.py not found'}
    except subprocess.TimeoutExpired:
        return {'error': 'find_merge_candidates.py timed out'}
    except (json.JSONDecodeError, KeyError) as e:
        return {'error': f'Failed to parse output: {e}'}


# --- Check 3: Note length outliers ---

def check_note_length(entries: list[dict]) -> dict:
    """Flag notes that are too short or too long."""
    too_short = []
    too_long = []

    for entry in entries:
        notes = entry.get('notes', '') or ''
        if not notes:
            continue
        length = len(notes)
        info = {
            'entry_id': entry['id'],
            'headword': headword_display(entry),
            'tier': get_tier(entry),
            'length': length,
        }
        if length < 50:
            too_short.append(info)
        elif length > 2000:
            too_long.append(info)

    return {'too_short': too_short, 'too_long': too_long}


# --- Check 4: Verbs missing transitivity ---

def check_missing_transitivity(entries: list[dict]) -> list[dict]:
    """Flag verb entries missing transitivity information."""
    issues = []
    transitivity_keywords = ['自動詞', '他動詞', 'transitive', 'intransitive']

    for entry in entries:
        if not is_verb(entry):
            continue

        # Check semantic tags
        sem_tags = get_semantic_tags(entry)
        has_tag = 'transitive' in sem_tags or 'intransitive' in sem_tags

        # Check notes
        notes = (entry.get('notes', '') or '').lower()
        has_notes = any(kw.lower() in notes for kw in transitivity_keywords)

        if not has_tag and not has_notes:
            issues.append({
                'entry_id': entry['id'],
                'headword': headword_display(entry),
                'tier': get_tier(entry),
            })

    return issues


# --- Check 5: Entries without collocations ---

COLLOCATION_PATTERNS = re.compile(
    r'COLLOCATION|collocation|〜|[ぁ-ゖァ-ヴー\u4e00-\u9fff]を[、。\s]|'
    r'[ぁ-ゖァ-ヴー\u4e00-\u9fff]が[、。\s]|'
    r'[ぁ-ゖァ-ヴー\u4e00-\u9fff]に[、。\s]',
    re.IGNORECASE,
)


def check_no_collocations(entries: list[dict]) -> list[dict]:
    """Flag verb/na-adj/noun entries with no collocations in notes."""
    issues = []

    for entry in entries:
        if not (is_verb(entry) or is_na_adjective(entry) or is_noun(entry)):
            continue

        notes = entry.get('notes', '') or ''
        if not notes:
            issues.append({
                'entry_id': entry['id'],
                'headword': headword_display(entry),
                'tier': get_tier(entry),
            })
            continue

        if not COLLOCATION_PATTERNS.search(notes):
            issues.append({
                'entry_id': entry['id'],
                'headword': headword_display(entry),
                'tier': get_tier(entry),
            })

    return issues


# --- Check 6: Example count gaps ---

def check_example_count(entries: list[dict]) -> list[dict]:
    """Flag entries with fewer examples than their tier minimum."""
    issues = []

    for entry in entries:
        tier = get_tier(entry)
        min_per_sense = 5 if tier in ('basic', 'core') else 3

        definitions = entry.get('definitions', [])
        examples = entry.get('examples', [])
        num_senses = max(len(definitions), 1)

        # Count examples per sense
        sense_counts = defaultdict(int)
        for ex in examples:
            sense_nums = ex.get('sense_numbers', [])
            if sense_nums:
                for sn in sense_nums:
                    sense_counts[sn] += 1
            else:
                # No sense_numbers: count toward sense 1
                sense_counts[1] += 1

        # Check each sense
        short_senses = []
        for sense_num in range(1, num_senses + 1):
            count = sense_counts.get(sense_num, 0)
            if count < min_per_sense:
                short_senses.append((sense_num, count))

        if short_senses:
            issues.append({
                'entry_id': entry['id'],
                'headword': headword_display(entry),
                'tier': tier,
                'total_examples': len(examples),
                'min_per_sense': min_per_sense,
                'num_senses': num_senses,
                'short_senses': short_senses,
            })

    return issues


# --- Output formatting ---

def print_human_report(results: dict, issue_filter: str | None) -> None:
    """Print human-readable consistency report."""
    print("=== CONSISTENCY REPORT ===\n")
    total_issues = 0

    # 1. Note structure
    if 'note-structure' in results:
        items = results['note-structure']
        total_issues += len(items)
        print(f"Note Structure Issues ({len(items)} entries)")
        by_cat = defaultdict(list)
        for item in items:
            by_cat[item['pos_category']].append(item)
        for cat, cat_items in sorted(by_cat.items()):
            print(f"  {cat.title()}s missing expected note sections:")
            for item in cat_items[:20]:
                print(f"    {item['entry_id']}  {item['headword']}")
            if len(cat_items) > 20:
                print(f"    ... and {len(cat_items) - 20} more")
        print()

    # 2. Cross-ref asymmetry
    if 'crossref-asymmetry' in results:
        info = results['crossref-asymmetry']
        if 'error' in info:
            print(f"Cross-Reference Asymmetry (unavailable: {info['error']})\n")
        else:
            count = info['asymmetric_pairs']
            total_issues += count
            print(f"Cross-Reference Asymmetry ({count} asymmetric pairs)")
            print("  (Details available via: python3 build/find_merge_candidates.py --asymmetry-only)")
            print()

    # 3. Note length
    if 'note-length' in results:
        info = results['note-length']
        short = info['too_short']
        long_ = info['too_long']
        total_issues += len(short) + len(long_)
        print("Note Length Outliers")
        print(f"  Too short (< 50 chars): {len(short)} entries")
        for item in short[:10]:
            print(f"    {item['entry_id']}  {item['headword']}  ({item['length']} chars)")
        if len(short) > 10:
            print(f"    ... and {len(short) - 10} more")
        print(f"  Too long (> 2000 chars): {len(long_)} entries")
        for item in long_[:10]:
            print(f"    {item['entry_id']}  {item['headword']}  ({item['length']} chars)")
        if len(long_) > 10:
            print(f"    ... and {len(long_) - 10} more")
        print()

    # 4. Missing transitivity
    if 'missing-transitivity' in results:
        items = results['missing-transitivity']
        total_issues += len(items)
        print(f"Verbs Missing Transitivity ({len(items)} entries)")
        for item in items[:20]:
            print(f"    {item['entry_id']}  {item['headword']}")
        if len(items) > 20:
            print(f"    ... and {len(items) - 20} more")
        print()

    # 5. No collocations
    if 'no-collocations' in results:
        items = results['no-collocations']
        total_issues += len(items)
        print(f"Entries Without Collocations ({len(items)} entries)")
        for item in items[:20]:
            print(f"    {item['entry_id']}  {item['headword']}")
        if len(items) > 20:
            print(f"    ... and {len(items) - 20} more")
        print()

    # 6. Example count gaps
    if 'example-count' in results:
        items = results['example-count']
        total_issues += len(items)
        print(f"Example Count Gaps ({len(items)} entries)")
        for item in items[:20]:
            print(f"    {item['entry_id']}  {item['headword']}  "
                  f"({item['tier']}, {item['total_examples']} examples, "
                  f"needs {item['min_per_sense']}/sense)")
        if len(items) > 20:
            print(f"    ... and {len(items) - 20} more")
        print()

    # Summary
    print("=== SUMMARY ===")
    labels = {
        'note-structure': 'Note structure',
        'crossref-asymmetry': 'Cross-ref asymmetry',
        'note-length': 'Note length outliers',
        'missing-transitivity': 'Missing transitivity',
        'no-collocations': 'No collocations',
        'example-count': 'Example count gaps',
    }
    for key, label in labels.items():
        if key not in results:
            continue
        val = results[key]
        if key == 'crossref-asymmetry':
            if 'error' in val:
                count = 'N/A'
            else:
                count = f"{val['asymmetric_pairs']} pairs"
        elif key == 'note-length':
            count = f"{len(val['too_short']) + len(val['too_long'])} entries"
        elif isinstance(val, list):
            count = f"{len(val)} issues"
        else:
            count = str(val)
        print(f"  {label + ':':<26} {count}")
    print(f"  {'TOTAL:':<26} {total_issues} issues")


def print_fix_list(results: dict) -> None:
    """Print entry IDs only, one per line."""
    seen = set()
    for key, val in results.items():
        if key == 'crossref-asymmetry':
            if isinstance(val, dict) and 'entry_ids_involved' in val:
                for eid in val['entry_ids_involved']:
                    if eid not in seen:
                        seen.add(eid)
                        print(eid)
        elif key == 'note-length':
            for item in val.get('too_short', []) + val.get('too_long', []):
                eid = item['entry_id']
                if eid not in seen:
                    seen.add(eid)
                    print(eid)
        elif isinstance(val, list):
            for item in val:
                eid = item['entry_id']
                if eid not in seen:
                    seen.add(eid)
                    print(eid)


def filter_by_tier(results: dict, tier: str) -> dict:
    """Filter all results to only include entries matching the given tier."""
    filtered = {}
    for key, val in results.items():
        if key == 'crossref-asymmetry':
            filtered[key] = val  # Cannot filter by tier easily
        elif key == 'note-length':
            filtered[key] = {
                'too_short': [i for i in val['too_short'] if i['tier'] == tier],
                'too_long': [i for i in val['too_long'] if i['tier'] == tier],
            }
        elif isinstance(val, list):
            filtered[key] = [i for i in val if i.get('tier') == tier]
        else:
            filtered[key] = val
    return filtered


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description='Check entry consistency across the dictionary.')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--issue', choices=[
        'note-structure', 'crossref-asymmetry', 'note-length',
        'missing-transitivity', 'no-collocations', 'example-count',
    ], help='Filter to a single issue type')
    parser.add_argument('--tier', choices=['basic', 'core', 'general'],
                        help='Filter to a single vocabulary tier')
    parser.add_argument('--fix-list', action='store_true',
                        help='Output entry IDs only (one per line)')
    args = parser.parse_args()

    # Load entries once
    entries = load_all_entries()
    if not entries:
        print("No entries found.", file=sys.stderr)
        return 1

    # Run selected checks
    run_all = args.issue is None
    results = {}

    if run_all or args.issue == 'note-structure':
        results['note-structure'] = check_note_structure(entries)

    if run_all or args.issue == 'crossref-asymmetry':
        results['crossref-asymmetry'] = check_crossref_asymmetry()

    if run_all or args.issue == 'note-length':
        results['note-length'] = check_note_length(entries)

    if run_all or args.issue == 'missing-transitivity':
        results['missing-transitivity'] = check_missing_transitivity(entries)

    if run_all or args.issue == 'no-collocations':
        results['no-collocations'] = check_no_collocations(entries)

    if run_all or args.issue == 'example-count':
        results['example-count'] = check_example_count(entries)

    # Apply tier filter
    if args.tier:
        results = filter_by_tier(results, args.tier)

    # Output
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    elif args.fix_list:
        print_fix_list(results)
    else:
        print_human_report(results, args.issue)

    return 0


if __name__ == '__main__':
    sys.exit(main())
