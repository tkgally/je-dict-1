#!/usr/bin/env python3
"""
Find dictionary entries that have kanji without furigana in the notes field.

This script scans all JSON entries and identifies cases where kanji characters
appear outside of the {kanji|furigana} notation pattern.
"""

import json
import os
import re
import sys
from pathlib import Path

# Kanji Unicode ranges
# CJK Unified Ideographs: U+4E00 to U+9FFF
# CJK Unified Ideographs Extension A: U+3400 to U+4DBF
# CJK Unified Ideographs Extension B-F: U+20000 to U+2FA1F
KANJI_PATTERN = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]')

# Pattern to match furigana notation: {kanji|reading}
FURIGANA_PATTERN = re.compile(r'\{[^}|]+\|[^}]+\}')


def contains_unannotated_kanji(text: str) -> tuple[bool, list[str]]:
    """
    Check if text contains kanji that are not within furigana notation.

    Returns:
        Tuple of (has_unannotated_kanji, list_of_unannotated_kanji)
    """
    if not text:
        return False, []

    # Remove all furigana-annotated text
    text_without_furigana = FURIGANA_PATTERN.sub('', text)

    # Find any remaining kanji
    unannotated = KANJI_PATTERN.findall(text_without_furigana)

    return len(unannotated) > 0, list(set(unannotated))


def extract_unannotated_context(text: str) -> list[str]:
    """
    Extract snippets of text showing unannotated kanji in context.
    """
    if not text:
        return []

    contexts = []
    # Split by furigana patterns
    parts = FURIGANA_PATTERN.split(text)

    for part in parts:
        kanji_matches = KANJI_PATTERN.findall(part)
        if kanji_matches:
            # Include the part that contains unannotated kanji
            # Truncate if too long
            snippet = part.strip()
            if len(snippet) > 100:
                # Find a kanji and show context around it
                for match in re.finditer(KANJI_PATTERN, part):
                    start = max(0, match.start() - 20)
                    end = min(len(part), match.end() + 20)
                    snippet = "..." + part[start:end] + "..."
                    break
            if snippet and snippet not in contexts:
                contexts.append(snippet)

    return contexts[:5]  # Limit to 5 contexts


def scan_entries(entries_dir: Path) -> list[dict]:
    """
    Scan all entry files and return those with missing furigana.
    """
    results = []

    for json_file in sorted(entries_dir.rglob('*.json')):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                entry = json.load(f)

            entry_id = entry.get('id', 'unknown')
            headword = entry.get('headword', '')
            reading = entry.get('reading', '')
            notes = entry.get('notes', '')

            has_missing, kanji_list = contains_unannotated_kanji(notes)

            if has_missing:
                # Get relative path from entries directory
                rel_path = json_file.relative_to(entries_dir)
                contexts = extract_unannotated_context(notes)

                results.append({
                    'id': entry_id,
                    'file_path': str(rel_path),
                    'headword': headword,
                    'reading': reading,
                    'unannotated_kanji': kanji_list,
                    'context_snippets': contexts
                })
        except json.JSONDecodeError as e:
            print(f"Error parsing {json_file}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing {json_file}: {e}", file=sys.stderr)

    return results


def main():
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'

    if not entries_dir.exists():
        print(f"Error: entries directory not found at {entries_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning entries in {entries_dir}...", file=sys.stderr)

    results = scan_entries(entries_dir)

    print(f"Found {len(results)} entries with missing furigana in notes", file=sys.stderr)

    # Output JSON for further processing
    output = {
        'description': 'Dictionary entries with kanji lacking furigana in the notes field',
        'total_count': len(results),
        'entries': results
    }

    # Output to stdout (can be redirected to file)
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
