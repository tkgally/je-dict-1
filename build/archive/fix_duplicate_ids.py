#!/usr/bin/env python3
"""
Fix duplicate numeric IDs by reassigning newer entries to new unique IDs.

For each pair of entries sharing a numeric ID, the older entry (by created timestamp)
keeps its ID, and the newer entry gets reassigned to the next available ID.
Also updates cross-references pointing to renamed entries.
"""

import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def get_entry_dir(entry_id: int) -> str:
    """Get the range directory for an entry ID."""
    return f"{(entry_id // 500) * 500:05d}"


def load_json(path: Path) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path: Path, data: dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def find_all_entries(entries_dir: Path) -> dict:
    """Return dict mapping numeric_id -> list of (path, data) tuples."""
    id_pattern = re.compile(r'^(\d{5})_.*\.json$')
    entries_by_num = {}

    for json_file in sorted(entries_dir.rglob('*.json')):
        match = id_pattern.match(json_file.name)
        if match:
            num_id = int(match.group(1))
            data = load_json(json_file)
            entries_by_num.setdefault(num_id, []).append((json_file, data))

    return entries_by_num


def get_created_time(data: dict) -> str:
    """Get the created timestamp from entry metadata."""
    return data.get('metadata', {}).get('created', '9999-99-99T99:99:99Z')


def get_max_id(entries_by_num: dict) -> int:
    """Find the highest numeric ID in use."""
    return max(entries_by_num.keys()) if entries_by_num else 0


def main():
    project_root = Path(__file__).parent.parent
    entries_dir = project_root / 'entries'

    # Find all entries grouped by numeric ID
    entries_by_num = find_all_entries(entries_dir)

    # Find duplicates
    duplicates = {k: v for k, v in entries_by_num.items() if len(v) > 1}

    if not duplicates:
        print("No duplicate IDs found.")
        return

    print(f"Found {len(duplicates)} duplicate ID groups")

    # Track the next available ID
    next_id = get_max_id(entries_by_num) + 1

    # Track all renames: old_id_str -> new_id_str (e.g., "07870" -> "17550")
    id_remap = {}
    # Track full ID renames: old_full_id -> new_full_id (e.g., "07870_chikuji" -> "17550_chikuji")
    full_id_remap = {}

    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    rename_ops = []  # (old_path, new_path, old_full_id, new_full_id, data)

    for num_id in sorted(duplicates.keys()):
        group = duplicates[num_id]
        # Sort by created timestamp - oldest first
        group.sort(key=lambda x: get_created_time(x[1]))

        # First entry keeps its ID; remaining entries get reassigned
        keeper_path, keeper_data = group[0]
        print(f"\n  ID {num_id:05d}: keeping {keeper_path.name}")

        for path, data in group[1:]:
            new_num_id = next_id
            next_id += 1

            old_full_id = data['id']
            # Extract the romaji part from the full ID
            romaji = old_full_id.split('_', 1)[1] if '_' in old_full_id else old_full_id
            new_full_id = f"{new_num_id:05d}_{romaji}"

            # Calculate new directory and path
            new_dir = entries_dir / get_entry_dir(new_num_id)
            new_path = new_dir / f"{new_full_id}.json"

            # Update entry data
            data['id'] = new_full_id

            # Update example IDs
            old_prefix = f"{num_id:05d}_{romaji}"
            new_prefix = new_full_id
            for ex in data.get('examples', []):
                if 'id' in ex and ex['id'].startswith(old_prefix):
                    ex['id'] = ex['id'].replace(old_prefix, new_prefix, 1)

            data['metadata']['modified'] = timestamp

            rename_ops.append((path, new_path, old_full_id, new_full_id, data))
            id_remap[f"{num_id:05d}"] = f"{new_num_id:05d}"
            full_id_remap[old_full_id] = new_full_id

            print(f"    reassigning {path.name} -> {new_full_id}.json (ID {new_num_id:05d})")

    # Execute renames
    print(f"\nExecuting {len(rename_ops)} renames...")
    for old_path, new_path, old_full_id, new_full_id, data in rename_ops:
        new_path.parent.mkdir(parents=True, exist_ok=True)
        save_json(new_path, data)
        old_path.unlink()
        print(f"  {old_path.name} -> {new_path.parent.name}/{new_path.name}")

    # Now update cross-references in ALL entries
    print(f"\nScanning all entries for cross-references to update...")
    update_count = 0
    id_pattern = re.compile(r'^(\d{5})_.*\.json$')

    for json_file in sorted(entries_dir.rglob('*.json')):
        match = id_pattern.match(json_file.name)
        if not match:
            continue

        content = json_file.read_text(encoding='utf-8')
        original_content = content

        # Check if any old IDs are referenced in this file
        needs_update = False
        for old_full_id, new_full_id in full_id_remap.items():
            if old_full_id in content:
                needs_update = True
                break

        if not needs_update:
            continue

        data = load_json(json_file)
        modified = False

        # Update cross_references
        for xref in data.get('cross_references', []):
            if xref.get('target_id') in full_id_remap:
                old_target = xref['target_id']
                xref['target_id'] = full_id_remap[old_target]
                modified = True
                print(f"  Updated xref in {json_file.name}: {old_target} -> {xref['target_id']}")

        # Update inline word links in examples and notes
        # Format: ⟦surface→base：entry_id⟧
        def replace_inline_ids(text):
            nonlocal modified
            if not text:
                return text
            for old_fid, new_fid in full_id_remap.items():
                old_num = old_fid.split('_')[0]
                if old_num in text:
                    new_text = text.replace(old_fid, new_fid)
                    if new_text != text:
                        modified = True
                        text = new_text
            return text

        # Check examples
        for ex in data.get('examples', []):
            if 'japanese' in ex:
                ex['japanese'] = replace_inline_ids(ex['japanese'])
            if 'english' in ex:
                ex['english'] = replace_inline_ids(ex['english'])

        # Check notes
        if 'notes' in data:
            data['notes'] = replace_inline_ids(data['notes'])

        if modified:
            data['metadata']['modified'] = timestamp
            save_json(json_file, data)
            update_count += 1

    print(f"\nUpdated cross-references in {update_count} entries")
    print(f"\nDone! Reassigned {len(rename_ops)} entries to new IDs.")
    print(f"New ID range: 17550 - {next_id - 1}")
    print("\nNext steps:")
    print("  python3 build/validate.py")
    print("  python3 build/update_indexes.py")
    print("  python3 build/build_flat.py")


if __name__ == '__main__':
    main()
