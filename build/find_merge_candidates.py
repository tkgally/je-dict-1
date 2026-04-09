#!/usr/bin/env python3
"""
Find entries that may need to be merged or cross-referenced.

This script identifies potential issues deterministically:
1. Same reading, different headwords (potential merges or cross-references needed)
2. Noun + する verb pairs that should cross-reference each other
3. Duplicate numeric IDs (different entries sharing the same 5-digit number)

The script produces a report; actual merge/cross-reference decisions require
semantic judgment and should not be automated.

Usage:
    python3 build/find_merge_candidates.py                    # Full report
    python3 build/find_merge_candidates.py --merge-only       # Only potential merges
    python3 build/find_merge_candidates.py --crossref-only    # Only missing cross-refs
    python3 build/find_merge_candidates.py --dupid-only       # Only duplicate numeric IDs
    python3 build/find_merge_candidates.py --json             # Machine-readable output
"""

import json
import sys
import re
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from japanese_utils import strip_furigana

ENTRIES_DIR = PROJECT_ROOT / 'entries'
ENTRIES_INDEX = PROJECT_ROOT / 'entries_index.json'
CANDIDATES_FILE = PROJECT_ROOT / 'candidate_words.json'


def load_entries_index():
    """Load entries_index.json."""
    with open(ENTRIES_INDEX, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_candidates():
    """Load candidate_words.json."""
    if not CANDIDATES_FILE.exists():
        return {'candidates': []}
    with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_numeric_id(entry_id: str) -> str:
    """Extract the 5-digit numeric prefix from an entry ID."""
    return entry_id.split('_')[0]


def find_potential_merges(entries):
    """
    Find entries with the same reading that might be the same word
    written differently (e.g., kana vs kanji forms).

    Returns groups of entries sharing a reading where at least one
    headword is a kana-only form or a different kanji spelling of
    what appears to be the same word.
    """
    by_reading = defaultdict(list)
    for entry in entries:
        reading = entry.get('reading', '')
        by_reading[reading].append(entry)

    candidates = []
    for reading, group in sorted(by_reading.items()):
        if len(group) < 2:
            continue

        # Group by stripped headword to find true homophones vs spelling variants
        headwords = {}
        for e in group:
            hw = strip_furigana(e.get('headword', ''))
            headwords.setdefault(hw, []).append(e)

        # Check if any headword is a pure kana form of another
        kana_entries = [e for e in group if strip_furigana(e['headword']) == reading]
        kanji_entries = [e for e in group if strip_furigana(e['headword']) != reading]

        # Case 1: Kana-only entry exists alongside kanji entry with same reading
        if kana_entries and kanji_entries:
            candidates.append({
                'type': 'kana_kanji_variant',
                'reading': reading,
                'entries': [
                    {'id': e['id'], 'headword': strip_furigana(e['headword']),
                     'gloss': e.get('gloss', '')}
                    for e in group
                ]
            })
            continue

        # Case 2: Multiple entries with same reading, same POS, overlapping glosses
        # Group by part_of_speech
        by_pos = defaultdict(list)
        for e in group:
            pos = e.get('part_of_speech', '')
            by_pos[pos].append(e)

        for pos, pos_group in by_pos.items():
            if len(pos_group) < 2:
                continue
            # Check for overlapping glosses (suggests same word, different kanji)
            for i in range(len(pos_group)):
                for j in range(i + 1, len(pos_group)):
                    e1, e2 = pos_group[i], pos_group[j]
                    hw1 = strip_furigana(e1['headword'])
                    hw2 = strip_furigana(e2['headword'])
                    if hw1 == hw2:
                        continue  # Already detected as duplicates by validate.py
                    g1 = set(e1.get('gloss', '').lower().split(', '))
                    g2 = set(e2.get('gloss', '').lower().split(', '))
                    overlap = g1 & g2
                    if overlap:
                        candidates.append({
                            'type': 'overlapping_meaning',
                            'reading': reading,
                            'pos': pos,
                            'shared_glosses': list(overlap),
                            'entries': [
                                {'id': e1['id'], 'headword': hw1,
                                 'gloss': e1.get('gloss', '')},
                                {'id': e2['id'], 'headword': hw2,
                                 'gloss': e2.get('gloss', '')}
                            ]
                        })

    return candidates


def _load_entry_refs():
    """Load cross-reference and prominent_see_also targets from actual entry files.

    Returns a dict mapping entry_id -> set of target IDs/readings that the entry
    references (via cross_references or prominent_see_also).
    """
    entry_refs = {}
    for entry_dir in sorted(ENTRIES_DIR.iterdir()):
        if not entry_dir.is_dir():
            continue
        for entry_file in sorted(entry_dir.glob('*.json')):
            try:
                with open(entry_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except (json.JSONDecodeError, IOError):
                continue
            refs = set()
            # Check cross_references
            cr = data.get('cross_references', [])
            if isinstance(cr, list):
                for ref in cr:
                    if isinstance(ref, dict):
                        if ref.get('target_id'):
                            refs.add(ref['target_id'])
                        if ref.get('reading'):
                            refs.add(ref['reading'])
            # Check prominent_see_also
            psa = data.get('prominent_see_also', [])
            if isinstance(psa, list):
                for ref in psa:
                    if isinstance(ref, dict):
                        if ref.get('target_id'):
                            refs.add(ref['target_id'])
                        if ref.get('reading'):
                            refs.add(ref['reading'])
            entry_refs[data.get('id', '')] = refs
    return entry_refs


def find_missing_crossrefs(entries):
    """
    Find entry pairs that should cross-reference each other but don't.

    Detects:
    - Noun + する verb pairs (e.g., 喧嘩 and けんかする)
    - Same reading, different kanji (homophones like 無くなる / 亡くなる)

    Checks both cross_references and prominent_see_also from actual entry files.
    """
    missing = []

    # Build lookup structures
    by_reading = defaultdict(list)
    by_id = {}
    for entry in entries:
        reading = entry.get('reading', '')
        by_reading[reading].append(entry)
        by_id[entry['id']] = entry

    # Load actual entry files for cross-reference checking
    entry_crossrefs = _load_entry_refs()

    # Detect noun + する verb pairs
    suru_pattern = re.compile(r'する$')
    for entry in entries:
        reading = entry.get('reading', '')
        headword = strip_furigana(entry.get('headword', ''))

        # Check if this is a する verb
        if reading.endswith('する') and ('verb' in entry.get('part_of_speech', '').lower()
                                          or 'suru' in entry.get('part_of_speech', '').lower()):
            base_reading = reading[:-2]  # Remove する
            base_headword = suru_pattern.sub('', headword)

            # Look for the noun form
            for other in by_reading.get(base_reading, []):
                other_hw = strip_furigana(other.get('headword', ''))
                if other_hw == base_headword and 'noun' in other.get('part_of_speech', '').lower():
                    # Check if they already cross-reference each other
                    has_forward = (other['id'] in entry_crossrefs.get(entry['id'], set()) or
                                   other['reading'] in entry_crossrefs.get(entry['id'], set()))
                    has_backward = (entry['id'] in entry_crossrefs.get(other['id'], set()) or
                                    entry['reading'] in entry_crossrefs.get(other['id'], set()))
                    if not has_forward or not has_backward:
                        missing.append({
                            'type': 'noun_suru_pair',
                            'noun': {'id': other['id'], 'headword': other_hw,
                                     'gloss': other.get('gloss', '')},
                            'verb': {'id': entry['id'], 'headword': headword,
                                     'gloss': entry.get('gloss', '')},
                            'has_forward_ref': has_forward,
                            'has_backward_ref': has_backward
                        })

        # Check if this is a noun and a する verb exists
        if 'noun' in entry.get('part_of_speech', '').lower():
            suru_reading = reading + 'する'
            for other in by_reading.get(suru_reading, []):
                other_hw = strip_furigana(other.get('headword', ''))
                if other_hw == headword + 'する':
                    # Already covered by the する verb check above
                    pass

    # Detect same-reading entries that should cross-reference each other
    for reading, group in by_reading.items():
        if len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                e1, e2 = group[i], group[j]
                hw1 = strip_furigana(e1['headword'])
                hw2 = strip_furigana(e2['headword'])
                if hw1 == hw2:
                    continue  # Same headword = potential duplicate, not cross-ref

                # Check if they reference each other
                has_forward = (e2['id'] in entry_crossrefs.get(e1['id'], set()) or
                               e2['reading'] in entry_crossrefs.get(e1['id'], set()))
                has_backward = (e1['id'] in entry_crossrefs.get(e2['id'], set()) or
                                e1['reading'] in entry_crossrefs.get(e2['id'], set()))

                if not has_forward or not has_backward:
                    missing.append({
                        'type': 'homophone_pair',
                        'reading': reading,
                        'entry1': {'id': e1['id'], 'headword': hw1,
                                   'gloss': e1.get('gloss', '')},
                        'entry2': {'id': e2['id'], 'headword': hw2,
                                   'gloss': e2.get('gloss', '')},
                        'has_forward_ref': has_forward,
                        'has_backward_ref': has_backward
                    })

    return missing


def find_duplicate_numeric_ids(entries):
    """
    Find entries that share the same 5-digit numeric ID prefix.
    """
    by_num = defaultdict(list)
    for entry in entries:
        num = get_numeric_id(entry['id'])
        by_num[num].append(entry)

    duplicates = []
    for num, group in sorted(by_num.items()):
        if len(group) > 1:
            duplicates.append({
                'numeric_id': num,
                'entries': [
                    {'id': e['id'], 'headword': strip_furigana(e.get('headword', '')),
                     'reading': e.get('reading', ''), 'gloss': e.get('gloss', '')}
                    for e in group
                ]
            })

    return duplicates


def _load_entry_full_refs():
    """Load full cross-reference and prominent_see_also details from entry files.

    Returns a dict mapping entry_id -> {
        'headword': str,
        'reading': str,
        'refs': [{'target_id': str, 'ref_type': str, 'ref_detail': str|None}, ...]
    }
    """
    entry_data = {}
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
            headword = strip_furigana(data.get('headword', ''))
            reading = data.get('reading', '')
            refs = []
            # Collect prominent_see_also refs
            psa = data.get('prominent_see_also', [])
            if isinstance(psa, list):
                for ref in psa:
                    if isinstance(ref, dict) and ref.get('target_id'):
                        refs.append({
                            'target_id': ref['target_id'],
                            'ref_type': 'prominent_see_also',
                            'ref_detail': None
                        })
            # Collect cross_references refs
            cr = data.get('cross_references', [])
            if isinstance(cr, list):
                for ref in cr:
                    if isinstance(ref, dict) and ref.get('target_id'):
                        refs.append({
                            'target_id': ref['target_id'],
                            'ref_type': 'cross_references',
                            'ref_detail': ref.get('type')
                        })
            entry_data[entry_id] = {
                'headword': headword,
                'reading': reading,
                'refs': refs
            }
    return entry_data


def find_asymmetric_references():
    """
    Find cross-references where A->B exists but B->A does not.

    Checks both prominent_see_also and cross_references for directional
    asymmetry. Only considers references with target_id (hardened references).

    Returns a tuple of (asymmetric_list, stats_dict).
    """
    entry_data = _load_entry_full_refs()

    # Build a set of (source_id, target_id) for quick back-reference lookup
    all_ref_pairs = set()
    for source_id, data in entry_data.items():
        for ref in data['refs']:
            all_ref_pairs.add((source_id, ref['target_id']))

    asymmetric = []
    total_refs_with_target = 0
    symmetric_count = 0
    asymmetric_count = 0
    seen_pairs = set()

    for source_id, data in sorted(entry_data.items()):
        for ref in data['refs']:
            target_id = ref['target_id']
            total_refs_with_target += 1

            # Normalize pair to avoid double-counting
            pair_key = tuple(sorted([source_id, target_id]))
            if pair_key in seen_pairs:
                continue

            has_back = (target_id, source_id) in all_ref_pairs

            if has_back:
                symmetric_count += 1
            else:
                asymmetric_count += 1
                target_data = entry_data.get(target_id, {})
                asymmetric.append({
                    'source_id': source_id,
                    'source_headword': data['headword'],
                    'target_id': target_id,
                    'target_headword': target_data.get('headword', '(unknown)'),
                    'ref_type': ref['ref_type'],
                    'ref_detail': ref['ref_detail']
                })

            seen_pairs.add(pair_key)

    stats = {
        'total_refs_with_target_id': total_refs_with_target,
        'symmetric_pairs': symmetric_count,
        'asymmetric_one_way': asymmetric_count
    }

    return asymmetric, stats


def find_candidate_duplicates(entries, candidates):
    """
    Find candidates that are essentially duplicates of existing entries
    (same reading, different headword spelling - potential kana/kanji variants).
    """
    issues = []
    entry_readings = defaultdict(list)
    for entry in entries:
        reading = entry.get('reading', '')
        hw = strip_furigana(entry.get('headword', ''))
        entry_readings[reading].append({'id': entry['id'], 'headword': hw,
                                         'gloss': entry.get('gloss', '')})

    for cand in candidates.get('candidates', []):
        reading = cand.get('reading', '')
        word = cand.get('word', '')
        if reading in entry_readings:
            for existing in entry_readings[reading]:
                # If the candidate word is the kana form of an existing kanji entry
                # or vice versa, flag it
                if word == reading and existing['headword'] != reading:
                    issues.append({
                        'type': 'candidate_is_kana_variant',
                        'candidate': {'word': word, 'reading': reading,
                                      'id': cand.get('id', '')},
                        'existing_entry': existing
                    })
                elif existing['headword'] == reading and word != reading:
                    issues.append({
                        'type': 'entry_is_kana_variant',
                        'candidate': {'word': word, 'reading': reading,
                                      'id': cand.get('id', '')},
                        'existing_entry': existing
                    })

    return issues


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Find entries needing merge or cross-reference.')
    parser.add_argument('--merge-only', action='store_true', help='Only show potential merges')
    parser.add_argument('--crossref-only', action='store_true', help='Only show missing cross-references')
    parser.add_argument('--dupid-only', action='store_true', help='Only show duplicate numeric IDs')
    parser.add_argument('--asymmetry-only', action='store_true',
                        help='Only show asymmetric cross-reference report')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    args = parser.parse_args()

    show_all = not (args.merge_only or args.crossref_only or args.dupid_only or args.asymmetry_only)

    data = load_entries_index()
    entries = data.get('entries', [])
    candidates = load_candidates()

    results = {}

    if show_all or args.merge_only:
        merges = find_potential_merges(entries)
        results['potential_merges'] = merges

    if show_all or args.crossref_only:
        crossrefs = find_missing_crossrefs(entries)
        results['missing_crossrefs'] = crossrefs

    if show_all or args.dupid_only:
        dup_ids = find_duplicate_numeric_ids(entries)
        results['duplicate_numeric_ids'] = dup_ids

    if show_all or args.merge_only:
        cand_dups = find_candidate_duplicates(entries, candidates)
        results['candidate_duplicates'] = cand_dups

    if show_all or args.asymmetry_only:
        asymmetric, asym_stats = find_asymmetric_references()
        results['asymmetric_references'] = asymmetric
        results['asymmetry_stats'] = asym_stats

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    # Human-readable output
    if 'potential_merges' in results:
        merges = results['potential_merges']
        print(f"=== POTENTIAL MERGES ({len(merges)} found) ===")
        print("These entries may be the same word with different spellings.")
        print("Semantic judgment required to decide if they should be merged.\n")
        for m in merges:
            print(f"  Reading: {m['reading']}  Type: {m['type']}")
            if 'shared_glosses' in m:
                print(f"  Shared glosses: {', '.join(m['shared_glosses'])}")
            for e in m['entries']:
                print(f"    {e['id']}  {e['headword']}  \"{e['gloss']}\"")
            print()

    if 'candidate_duplicates' in results:
        cand_dups = results['candidate_duplicates']
        if cand_dups:
            print(f"=== CANDIDATE DUPLICATES ({len(cand_dups)} found) ===")
            print("Candidates that appear to be spelling variants of existing entries.\n")
            for cd in cand_dups:
                print(f"  Candidate: {cd['candidate']['word']} ({cd['candidate']['reading']}) [{cd['candidate']['id']}]")
                print(f"  Existing:  {cd['existing_entry']['headword']} ({cd['existing_entry']['id']})")
                print(f"  Type: {cd['type']}")
                print()

    if 'missing_crossrefs' in results:
        crossrefs = results['missing_crossrefs']
        print(f"=== MISSING CROSS-REFERENCES ({len(crossrefs)} found) ===")
        print("Entry pairs that should reference each other.\n")
        for cr in crossrefs:
            if cr['type'] == 'noun_suru_pair':
                print(f"  Noun/する pair:")
                print(f"    Noun: {cr['noun']['id']}  {cr['noun']['headword']}  \"{cr['noun']['gloss']}\"")
                print(f"    Verb: {cr['verb']['id']}  {cr['verb']['headword']}  \"{cr['verb']['gloss']}\"")
                print(f"    Refs: noun→verb={cr['has_forward_ref']}, verb→noun={cr['has_backward_ref']}")
            elif cr['type'] == 'homophone_pair':
                print(f"  Homophones ({cr['reading']}):")
                print(f"    {cr['entry1']['id']}  {cr['entry1']['headword']}  \"{cr['entry1']['gloss']}\"")
                print(f"    {cr['entry2']['id']}  {cr['entry2']['headword']}  \"{cr['entry2']['gloss']}\"")
                fwd = 'yes' if cr['has_forward_ref'] else 'NO'
                bwd = 'yes' if cr['has_backward_ref'] else 'NO'
                print(f"    Refs: 1→2={fwd}, 2→1={bwd}")
            print()

    if 'duplicate_numeric_ids' in results:
        dup_ids = results['duplicate_numeric_ids']
        print(f"=== DUPLICATE NUMERIC IDs ({len(dup_ids)} found) ===")
        print("Entries sharing the same 5-digit number prefix.\n")
        for d in dup_ids:
            print(f"  Numeric ID: {d['numeric_id']}")
            for e in d['entries']:
                print(f"    {e['id']}  {e['headword']}  ({e['reading']})  \"{e['gloss']}\"")
            print()

    if 'asymmetric_references' in results:
        asym = results['asymmetric_references']
        asym_stats = results['asymmetry_stats']
        print(f"=== ASYMMETRIC CROSS-REFERENCES ({len(asym)} found) ===")
        print("References where A\u2192B exists but B\u2192A does not.\n")
        for a in asym:
            detail = f": {a['ref_detail']}" if a['ref_detail'] else ''
            print(f"  {a['source_id']} \u2192 {a['target_id']}  ({a['ref_type']}{detail})")
            print(f"    Source has link to target, but target has no link back.")
            print()
        print("Summary:")
        print(f"  Total references with target_id: {asym_stats['total_refs_with_target_id']}")
        print(f"  Symmetric pairs: {asym_stats['symmetric_pairs']}")
        print(f"  Asymmetric (one-way): {asym_stats['asymmetric_one_way']}")
        print()

    # Summary
    total_issues = sum(len(v) for v in results.values() if isinstance(v, list))
    print(f"Total issues found: {total_issues}")


if __name__ == '__main__':
    main()
