#!/usr/bin/env python3
"""
Check semantic clusters for missing internal cross-references.

Lints transitivity pairs, antonym pairs, and keigo groups to ensure
all expected bidirectional links are present.

Usage:
    python3 build/check_semantic_clusters.py                     # Full report
    python3 build/check_semantic_clusters.py --type transitivity  # One cluster type
    python3 build/check_semantic_clusters.py --type antonym
    python3 build/check_semantic_clusters.py --type keigo
    python3 build/check_semantic_clusters.py --summary            # Counts only
    python3 build/check_semantic_clusters.py --json               # Machine-readable
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from japanese_utils import strip_furigana

ENTRIES_DIR = PROJECT_ROOT / 'entries'


def load_all_entries():
    """Load all entry files from disk.

    Returns a dict mapping entry_id -> full entry data.
    """
    entries = {}
    for entry_dir in sorted(ENTRIES_DIR.iterdir()):
        if not entry_dir.is_dir():
            continue
        for entry_file in sorted(entry_dir.glob('*.json')):
            try:
                with open(entry_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (json.JSONDecodeError, IOError):
                continue
            entry_id = data.get('id', '')
            if entry_id:
                entries[entry_id] = data
    return entries


def _get_psa_target_ids(entry):
    """Get set of target_ids from prominent_see_also."""
    targets = set()
    psa = entry.get('prominent_see_also', [])
    if isinstance(psa, list):
        for ref in psa:
            if isinstance(ref, dict) and ref.get('target_id'):
                targets.add(ref['target_id'])
    return targets


def _get_cr_targets(entry, ref_type=None):
    """Get list of cross_references matching a type (or all if None).

    Returns list of dicts with target_id and type.
    """
    targets = []
    cr = entry.get('cross_references', [])
    if isinstance(cr, list):
        for ref in cr:
            if not isinstance(ref, dict):
                continue
            if ref_type and ref.get('type') != ref_type:
                continue
            if ref.get('target_id'):
                targets.append({
                    'target_id': ref['target_id'],
                    'type': ref.get('type', ''),
                    'label': ref.get('label', '')
                })
    return targets


def _has_any_ref_to(entry, target_id):
    """Check if entry has any reference (psa or cr) pointing to target_id."""
    psa = entry.get('prominent_see_also', [])
    if isinstance(psa, list):
        for ref in psa:
            if isinstance(ref, dict) and ref.get('target_id') == target_id:
                return True
    cr = entry.get('cross_references', [])
    if isinstance(cr, list):
        for ref in cr:
            if isinstance(ref, dict) and ref.get('target_id') == target_id:
                return True
    return False


def check_transitivity_pairs(entries):
    """Check transitivity pairs for missing links.

    Looks for:
    1. Entries whose notes mention transitivity but have no prominent_see_also to pair
    2. Entries with prominent_see_also where the target has no reciprocal link
    """
    gaps = []
    pair_pattern = re.compile(
        r'Pair:\s*(.+?)(?:\s*\(|$)', re.MULTILINE
    )
    transitivity_pattern = re.compile(
        r'(?:{自動詞\|じどうし}|{他動詞\|たどうし}|intransitive|transitive)',
        re.IGNORECASE
    )

    checked_pairs = set()
    complete_pairs = 0
    incomplete_pairs = 0
    unlinked_mentions = 0

    for entry_id, entry in sorted(entries.items()):
        pos = entry.get('part_of_speech', '')
        if 'verb' not in pos.lower():
            continue

        notes = entry.get('notes', '')
        if not notes:
            continue

        # Check if notes mention transitivity
        trans_match = transitivity_pattern.search(notes)
        if not trans_match:
            continue

        # Determine transitivity type
        if '{自動詞|じどうし}' in notes or (
            'intransitive' in notes.lower() and 'transitive' not in notes.lower().replace('intransitive', '')
        ):
            trans_type = 'intransitive'
        elif '{他動詞|たどうし}' in notes or 'transitive' in notes.lower():
            trans_type = 'transitive'
        else:
            trans_type = 'unknown'

        headword = strip_furigana(entry.get('headword', ''))

        # Check if there's a pair mentioned in notes
        pair_match = pair_pattern.search(notes)
        pair_word = strip_furigana(pair_match.group(1).strip()) if pair_match else None

        # Get prominent_see_also targets
        psa_targets = _get_psa_target_ids(entry)

        # Check if any psa target is annotated as transitive/intransitive pair
        has_pair_psa = False
        pair_target_id = None
        psa = entry.get('prominent_see_also', [])
        if isinstance(psa, list):
            for ref in psa:
                if not isinstance(ref, dict):
                    continue
                note = ref.get('note', '')
                if any(kw in note.lower() for kw in ['transitive', 'intransitive']):
                    has_pair_psa = True
                    pair_target_id = ref.get('target_id')
                    break

        if has_pair_psa and pair_target_id:
            # Check reciprocal
            pair_key = tuple(sorted([entry_id, pair_target_id]))
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            target = entries.get(pair_target_id)
            if target:
                has_back = False
                target_psa = target.get('prominent_see_also', [])
                if isinstance(target_psa, list):
                    for ref in target_psa:
                        if isinstance(ref, dict) and ref.get('target_id') == entry_id:
                            has_back = True
                            break

                if has_back:
                    complete_pairs += 1
                else:
                    incomplete_pairs += 1
                    target_hw = strip_furigana(target.get('headword', ''))
                    gaps.append({
                        'type': 'missing_reciprocal',
                        'source_id': entry_id,
                        'source_headword': headword,
                        'source_transitivity': trans_type,
                        'target_id': pair_target_id,
                        'target_headword': target_hw,
                        'detail': f'Target {pair_target_id} has no reciprocal link back'
                    })
            else:
                incomplete_pairs += 1
                gaps.append({
                    'type': 'missing_target',
                    'source_id': entry_id,
                    'source_headword': headword,
                    'source_transitivity': trans_type,
                    'target_id': pair_target_id,
                    'target_headword': '(entry not found)',
                    'detail': f'Target entry {pair_target_id} does not exist'
                })
        elif pair_word and not has_pair_psa:
            # Notes mention a pair but no prominent_see_also link
            unlinked_mentions += 1
            gaps.append({
                'type': 'unlinked_pair',
                'source_id': entry_id,
                'source_headword': headword,
                'source_transitivity': trans_type,
                'target_id': None,
                'target_headword': pair_word,
                'detail': f'Notes mention transitivity pair but no prominent_see_also link'
            })

    stats = {
        'complete_pairs': complete_pairs,
        'incomplete_missing_link': incomplete_pairs,
        'mentioned_but_unlinked': unlinked_mentions
    }

    return gaps, stats


def check_antonym_pairs(entries):
    """Check antonym cross-references for symmetry."""
    gaps = []
    checked_pairs = set()
    symmetric = 0
    asymmetric = 0

    for entry_id, entry in sorted(entries.items()):
        antonym_refs = _get_cr_targets(entry, 'antonym')
        for ref in antonym_refs:
            target_id = ref['target_id']
            pair_key = tuple(sorted([entry_id, target_id]))
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            target = entries.get(target_id)
            if not target:
                asymmetric += 1
                gaps.append({
                    'source_id': entry_id,
                    'source_headword': strip_furigana(entry.get('headword', '')),
                    'target_id': target_id,
                    'target_headword': '(entry not found)',
                    'detail': f'Target entry {target_id} does not exist'
                })
                continue

            # Check if target has antonym back to source
            target_antonyms = _get_cr_targets(target, 'antonym')
            has_back = any(a['target_id'] == entry_id for a in target_antonyms)

            if has_back:
                symmetric += 1
            else:
                asymmetric += 1
                gaps.append({
                    'source_id': entry_id,
                    'source_headword': strip_furigana(entry.get('headword', '')),
                    'target_id': target_id,
                    'target_headword': strip_furigana(target.get('headword', '')),
                    'detail': 'Target has no reciprocal antonym link back'
                })

    stats = {
        'symmetric': symmetric,
        'asymmetric': asymmetric
    }

    return gaps, stats


def check_keigo_groups(entries):
    """Check keigo cross-reference groups for completeness.

    A keigo group consists of a plain form and its honorific/humble equivalents.
    All members should link to each other.
    """
    gaps = []

    # Build keigo groups: find all entries with keigo cross-references
    # and cluster them into groups
    keigo_edges = defaultdict(set)  # entry_id -> set of target_ids via keigo
    for entry_id, entry in entries.items():
        keigo_refs = _get_cr_targets(entry, 'keigo')
        for ref in keigo_refs:
            keigo_edges[entry_id].add(ref['target_id'])

    # Build connected components (keigo groups)
    visited = set()
    groups = []

    def dfs(node, component):
        if node in visited:
            return
        visited.add(node)
        component.add(node)
        for neighbor in keigo_edges.get(node, set()):
            dfs(neighbor, component)
        # Also check reverse edges
        for other_id, targets in keigo_edges.items():
            if node in targets:
                dfs(other_id, component)

    for entry_id in keigo_edges:
        if entry_id not in visited:
            component = set()
            dfs(entry_id, component)
            if len(component) >= 2:
                groups.append(sorted(component))

    fully_linked = 0
    partially_linked = 0

    for group in groups:
        group_gaps = []
        # Check all pairs within the group
        for i, src_id in enumerate(group):
            for j, tgt_id in enumerate(group):
                if i == j:
                    continue
                src_entry = entries.get(src_id)
                if not src_entry:
                    continue
                # Check if src has keigo ref to tgt
                has_link = any(
                    r['target_id'] == tgt_id
                    for r in _get_cr_targets(src_entry, 'keigo')
                )
                # Also check prominent_see_also
                if not has_link:
                    has_link = tgt_id in _get_psa_target_ids(src_entry)

                if not has_link:
                    src_hw = strip_furigana(src_entry.get('headword', ''))
                    tgt_entry = entries.get(tgt_id)
                    tgt_hw = strip_furigana(tgt_entry.get('headword', '')) if tgt_entry else '(unknown)'
                    group_gaps.append({
                        'source_id': src_id,
                        'source_headword': src_hw,
                        'target_id': tgt_id,
                        'target_headword': tgt_hw,
                        'status': 'MISSING'
                    })

        if group_gaps:
            partially_linked += 1
            # Build group display
            group_headwords = []
            for member_id in group:
                member = entries.get(member_id)
                if member:
                    group_headwords.append(strip_furigana(member.get('headword', member_id)))
                else:
                    group_headwords.append(member_id)

            gaps.append({
                'group_members': group,
                'group_headwords': group_headwords,
                'missing_links': group_gaps
            })
        else:
            fully_linked += 1

    stats = {
        'fully_linked': fully_linked,
        'partially_linked': partially_linked
    }

    return gaps, stats


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Check semantic clusters for missing internal cross-references.')
    parser.add_argument('--type', choices=['transitivity', 'antonym', 'keigo'],
                        help='Check only one cluster type (default: all)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--summary', action='store_true', help='Show counts only')
    args = parser.parse_args()

    entries = load_all_entries()

    results = {}

    check_types = [args.type] if args.type else ['transitivity', 'antonym', 'keigo']

    if 'transitivity' in check_types:
        trans_gaps, trans_stats = check_transitivity_pairs(entries)
        results['transitivity'] = {'gaps': trans_gaps, 'stats': trans_stats}

    if 'antonym' in check_types:
        ant_gaps, ant_stats = check_antonym_pairs(entries)
        results['antonym'] = {'gaps': ant_gaps, 'stats': ant_stats}

    if 'keigo' in check_types:
        keigo_gaps, keigo_stats = check_keigo_groups(entries)
        results['keigo'] = {'gaps': keigo_gaps, 'stats': keigo_stats}

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    # Human-readable output
    if 'transitivity' in results:
        trans = results['transitivity']
        gaps = trans['gaps']
        stats = trans['stats']
        print(f"TRANSITIVITY PAIR GAPS ({len(gaps)} found)")
        print()
        if not args.summary:
            for g in gaps:
                src = f"{g['source_id']} ({g['source_headword']}, {g['source_transitivity']})"
                if g['type'] == 'missing_reciprocal':
                    print(f"  {g['source_id']} \u2192 {g['target_id']} (prominent_see_also)")
                    print(f"    {g['detail']}")
                elif g['type'] == 'missing_target':
                    print(f"  {g['source_id']} \u2192 {g['target_id']} (prominent_see_also)")
                    print(f"    {g['detail']}")
                elif g['type'] == 'unlinked_pair':
                    print(f"  {g['source_id']} ({g['source_headword']}, {g['source_transitivity']})")
                    print(f"    {g['detail']}")
                    print(f"    Pair mentioned in notes: {g['target_headword']}")
                print()

        checked = stats['complete_pairs'] + stats['incomplete_missing_link']
        print(f"  Transitivity pairs checked: {checked}")
        print(f"    Complete pairs: {stats['complete_pairs']}")
        print(f"    Incomplete (missing link): {stats['incomplete_missing_link']}")
        print(f"    Mentioned in notes but unlinked: {stats['mentioned_but_unlinked']}")
        print()

    if 'antonym' in results:
        ant = results['antonym']
        gaps = ant['gaps']
        stats = ant['stats']
        print(f"ANTONYM PAIR GAPS ({len(gaps)} found)")
        print()
        if not args.summary:
            for g in gaps:
                print(f"  {g['source_id']} \u2192 {g['target_id']} (antonym)")
                print(f"    {g['detail']}")
                print()

        checked = stats['symmetric'] + stats['asymmetric']
        print(f"  Antonym pairs checked: {checked}")
        print(f"    Symmetric: {stats['symmetric']}")
        print(f"    Asymmetric: {stats['asymmetric']}")
        print()

    if 'keigo' in results:
        keigo = results['keigo']
        gaps = keigo['gaps']
        stats = keigo['stats']
        print(f"KEIGO GROUP GAPS ({len(gaps)} found)")
        print()
        if not args.summary:
            for g in gaps:
                group_display = ' / '.join(g['group_headwords'])
                print(f"  Group: {group_display}")
                for link in g['missing_links']:
                    print(f"    {link['source_id']} \u2192 {link['target_id']} (keigo) {link['status']}")
                print()

        total = stats['fully_linked'] + stats['partially_linked']
        print(f"  Keigo groups checked: {total}")
        print(f"    Fully linked: {stats['fully_linked']}")
        print(f"    Partially linked: {stats['partially_linked']}")
        print()

    if not args.summary and not args.json:
        # Print overall summary
        print("SEMANTIC CLUSTER SUMMARY")
        print("=" * 24)
        for check_type in check_types:
            if check_type in results:
                stats = results[check_type]['stats']
                gap_count = len(results[check_type]['gaps'])
                print(f"  {check_type.title()}: {gap_count} gaps found")
        print()


if __name__ == '__main__':
    main()
