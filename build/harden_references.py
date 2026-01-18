#!/usr/bin/env python3
"""
Harden Cross-References for je-dict-1

This script scans dictionary entries and adds target_id to resolvable
cross-references. This "hardens" forward references into direct ID-based
references once the target entry exists.

Resolution Logic:
1. If target_id present AND entry exists → already hardened (skip)
2. If target_id present AND entry missing → ERROR (stale reference)
3. If no target_id → attempt to resolve by reading/headword
   - If unique match found → add target_id
   - If multiple matches (ambiguous) → WARN, skip
   - If no match found → skip (legitimate forward ref)

Usage:
    python3 harden_references.py              # Dry run - show what would change
    python3 harden_references.py --apply      # Apply changes to entry files
    python3 harden_references.py --id <id>    # Process single entry
"""

import json
import sys
import argparse
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

from path_utils import get_entry_path


def load_all_entries(entries_dir: Path) -> Tuple[Dict[str, Dict], Dict[str, List[Dict]]]:
    """
    Load all entries and build lookup indexes.

    Returns:
        Tuple of:
        - entries_by_id: Dict mapping entry ID to entry data
        - entries_by_reading: Dict mapping reading to list of entry info
    """
    entries_by_id = {}
    entries_by_reading = defaultdict(list)

    for entry_path in entries_dir.rglob('*.json'):
        try:
            with open(entry_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)

            entry_id = entry.get('id', '')
            reading = entry.get('reading', '')
            headword = entry.get('headword', '')

            entries_by_id[entry_id] = entry
            entries_by_id[entry_id]['_path'] = entry_path

            if reading:
                entries_by_reading[reading].append({
                    'id': entry_id,
                    'headword': headword,
                    'reading': reading
                })
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load {entry_path}: {e}", file=sys.stderr)

    return entries_by_id, dict(entries_by_reading)


def resolve_reference(ref: Dict[str, Any], entries_by_id: Dict, entries_by_reading: Dict) -> Tuple[Optional[str], str]:
    """
    Attempt to resolve a cross-reference to a target_id.

    Returns:
        Tuple of (target_id, status) where status is one of:
        - 'already_hardened': Has target_id pointing to existing entry
        - 'stale': Has target_id but entry doesn't exist (ERROR)
        - 'resolved': Successfully resolved to target_id
        - 'ambiguous': Multiple matches, cannot resolve
        - 'pending': No match found (forward reference)
    """
    existing_target_id = ref.get('target_id')

    # Case 1 & 2: Already has target_id
    if existing_target_id:
        if existing_target_id in entries_by_id:
            return existing_target_id, 'already_hardened'
        else:
            return existing_target_id, 'stale'

    # Case 3: Resolve by reading/headword
    reading = ref.get('reading', '')
    ref_headword = ref.get('headword', '')

    if not reading:
        return None, 'pending'

    candidates = entries_by_reading.get(reading, [])

    if len(candidates) == 0:
        # No entry with this reading - forward reference
        return None, 'pending'

    if len(candidates) == 1:
        # Single candidate
        candidate = candidates[0]
        # If headword specified, verify it matches
        if ref_headword and candidate['headword'] != ref_headword:
            # Headword mismatch - forward reference to different homonym
            return None, 'pending'
        return candidate['id'], 'resolved'

    # Multiple candidates - need headword to disambiguate
    if not ref_headword:
        return None, 'ambiguous'

    # Try to find matching headword
    for candidate in candidates:
        if candidate['headword'] == ref_headword:
            return candidate['id'], 'resolved'

    # No headword match - forward reference to homonym not yet in dictionary
    return None, 'pending'


def process_entry(entry: Dict[str, Any], entries_by_id: Dict, entries_by_reading: Dict) -> Tuple[bool, List[Dict]]:
    """
    Process a single entry's cross-references.

    Returns:
        Tuple of (has_changes, list of change details)
    """
    cross_refs = entry.get('cross_references', [])
    if not cross_refs:
        return False, []

    changes = []
    has_changes = False

    for i, ref in enumerate(cross_refs):
        if isinstance(ref, str):
            # Legacy string format - skip
            continue

        if not isinstance(ref, dict):
            continue

        target_id, status = resolve_reference(ref, entries_by_id, entries_by_reading)

        if status == 'resolved':
            # Can add target_id
            changes.append({
                'index': i,
                'action': 'harden',
                'target_id': target_id,
                'reading': ref.get('reading', ''),
                'headword': ref.get('headword', '')
            })
            has_changes = True
        elif status == 'stale':
            changes.append({
                'index': i,
                'action': 'error_stale',
                'target_id': target_id,
                'reading': ref.get('reading', ''),
                'headword': ref.get('headword', '')
            })
        elif status == 'ambiguous':
            candidates = entries_by_reading.get(ref.get('reading', ''), [])
            changes.append({
                'index': i,
                'action': 'warning_ambiguous',
                'reading': ref.get('reading', ''),
                'candidates': [c['headword'] for c in candidates]
            })

    return has_changes, changes


def apply_changes(entry: Dict[str, Any], changes: List[Dict]) -> Dict[str, Any]:
    """
    Apply hardening changes to an entry's cross-references.

    Returns the modified entry.
    """
    cross_refs = entry.get('cross_references', [])

    for change in changes:
        if change['action'] == 'harden':
            idx = change['index']
            if idx < len(cross_refs) and isinstance(cross_refs[idx], dict):
                cross_refs[idx]['target_id'] = change['target_id']

    entry['cross_references'] = cross_refs
    entry['metadata']['modified'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    return entry


def save_entry(entry: Dict[str, Any], entry_path: Path):
    """Save an entry to its file."""
    # Remove internal tracking field
    entry_to_save = {k: v for k, v in entry.items() if not k.startswith('_')}

    with open(entry_path, 'w', encoding='utf-8') as f:
        json.dump(entry_to_save, f, ensure_ascii=False, indent=2)
        f.write('\n')


def process_all_entries(project_root: Path, dry_run: bool = True, entry_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Process all entries (or a single entry) for hardening.

    Returns a report dictionary.
    """
    entries_dir = project_root / 'entries'

    print("Loading entries...")
    entries_by_id, entries_by_reading = load_all_entries(entries_dir)
    print(f"  Loaded {len(entries_by_id)} entries")

    report = {
        'total_entries': 0,
        'entries_with_changes': 0,
        'hardened_refs': 0,
        'stale_refs': 0,
        'ambiguous_refs': 0,
        'details': []
    }

    # Determine which entries to process
    if entry_id:
        if entry_id not in entries_by_id:
            print(f"Error: Entry not found: {entry_id}", file=sys.stderr)
            return report
        entries_to_process = [(entry_id, entries_by_id[entry_id])]
    else:
        entries_to_process = list(entries_by_id.items())

    for eid, entry in entries_to_process:
        report['total_entries'] += 1

        has_changes, changes = process_entry(entry, entries_by_id, entries_by_reading)

        if not changes:
            continue

        entry_path = entry.get('_path')
        rel_path = entry_path.relative_to(project_root) if entry_path else eid

        entry_detail = {
            'id': eid,
            'path': str(rel_path),
            'changes': []
        }

        for change in changes:
            if change['action'] == 'harden':
                report['hardened_refs'] += 1
                entry_detail['changes'].append({
                    'type': 'harden',
                    'reading': change['reading'],
                    'headword': change.get('headword', ''),
                    'target_id': change['target_id']
                })
            elif change['action'] == 'error_stale':
                report['stale_refs'] += 1
                entry_detail['changes'].append({
                    'type': 'error',
                    'message': f"Stale target_id '{change['target_id']}' - entry no longer exists"
                })
            elif change['action'] == 'warning_ambiguous':
                report['ambiguous_refs'] += 1
                candidates = change.get('candidates', [])
                entry_detail['changes'].append({
                    'type': 'warning',
                    'message': f"Ambiguous reference '{change['reading']}' - add headword to disambiguate",
                    'candidates': candidates
                })

        if has_changes:
            report['entries_with_changes'] += 1

            if not dry_run:
                updated_entry = apply_changes(entry, changes)
                save_entry(updated_entry, entry_path)

        report['details'].append(entry_detail)

    return report


def print_report(report: Dict[str, Any], dry_run: bool = True):
    """Print a formatted report."""
    print()
    print("=" * 60)
    print("Cross-Reference Hardening Report")
    print("=" * 60)
    print(f"Mode: {'DRY RUN (no changes made)' if dry_run else 'APPLIED'}")
    print(f"Total entries scanned: {report['total_entries']}")
    print(f"Entries with changes: {report['entries_with_changes']}")
    print()
    print(f"References that can be hardened: {report['hardened_refs']}")
    print(f"Stale references (ERROR): {report['stale_refs']}")
    print(f"Ambiguous references (WARNING): {report['ambiguous_refs']}")
    print()

    if report['details']:
        print("Details:")
        print("-" * 60)

        for entry_detail in report['details']:
            print(f"\n{entry_detail['path']}:")

            for change in entry_detail['changes']:
                if change['type'] == 'harden':
                    headword = change.get('headword', change['reading'])
                    print(f"  + HARDEN: {headword} → {change['target_id']}")
                elif change['type'] == 'error':
                    print(f"  ! ERROR: {change['message']}")
                elif change['type'] == 'warning':
                    candidates = change.get('candidates', [])
                    print(f"  ? WARNING: {change['message']}")
                    if candidates:
                        print(f"    Candidates: {', '.join(candidates)}")

    if dry_run and report['hardened_refs'] > 0:
        print()
        print("To apply these changes, run:")
        print("  python3 build/harden_references.py --apply")

    if report['stale_refs'] > 0:
        print()
        print("ERRORS FOUND: Stale target_id references point to non-existent entries.")
        print("These should be fixed manually (update or remove the target_id).")


def main():
    parser = argparse.ArgumentParser(
        description='Harden cross-references by adding target_id to resolvable references'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply changes to entry files (default is dry run)'
    )
    parser.add_argument(
        '--id',
        type=str,
        help='Process only the entry with this ID'
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    report = process_all_entries(project_root, dry_run=not args.apply, entry_id=args.id)
    print_report(report, dry_run=not args.apply)

    # Exit with error if stale references found
    if report['stale_refs'] > 0:
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
