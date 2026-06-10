#!/usr/bin/env python3
"""Remove [Register: ...] legacy trailers from entry notes fields.

The register information is already captured in the metadata.tags.formality field.
This script removes the redundant [Register: ...] text from notes.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REGISTER_RE = re.compile(r'\s*\[Register:[^\]]+\]')

def fix_notes(notes: str) -> str:
    """Remove [Register: ...] from notes, cleaning up orphaned blank lines."""
    result = REGISTER_RE.sub('', notes)
    # Collapse triple+ newlines to double
    result = re.sub(r'\n{3,}', '\n\n', result)
    # Trim trailing whitespace
    result = result.rstrip()
    return result

def main():
    data_file = Path('/tmp/register_trailer_entries.json')
    if not data_file.exists():
        print("ERROR: /tmp/register_trailer_entries.json not found", file=sys.stderr)
        sys.exit(1)

    flagged = json.loads(data_file.read_text(encoding='utf-8'))
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    changed = 0
    skipped = 0
    for item in flagged:
        path = Path(item['file'])
        if not path.exists():
            print(f"  SKIP (not found): {item['entry_id']}")
            skipped += 1
            continue

        entry = json.loads(path.read_text(encoding='utf-8'))
        notes = entry.get('notes', '')

        if not REGISTER_RE.search(notes):
            skipped += 1
            continue

        new_notes = fix_notes(notes)
        if new_notes == notes:
            skipped += 1
            continue

        entry['notes'] = new_notes
        # Update modified timestamp
        if 'metadata' in entry:
            entry['metadata']['modified'] = timestamp

        path.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + '\n',
                        encoding='utf-8')
        print(f"  FIXED: {item['entry_id']}")
        changed += 1

    print(f"\nDone: {changed} fixed, {skipped} skipped.")

if __name__ == '__main__':
    main()
