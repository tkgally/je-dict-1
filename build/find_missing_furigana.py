#!/usr/bin/env python3
"""
Find dictionary entries that have kanji without furigana in text fields.

This script scans all JSON entries and identifies cases where kanji characters
appear outside of the {kanji|furigana} notation pattern. It checks:
- notes (entry-level)
- definitions[].explanation
- examples[].japanese
- examples[].notes
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

from japanese_utils import FURIGANA_PATTERN

# Kanji Unicode ranges
# CJK Unified Ideographs: U+4E00 to U+9FFF
# CJK Unified Ideographs Extension A: U+3400 to U+4DBF
# CJK Unified Ideographs Extension B-F: U+20000 to U+2FA1F
KANJI_PATTERN = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]')


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

    Scans these text fields:
    - notes (entry-level)
    - definitions[].explanation
    - examples[].japanese
    - examples[].notes
    """
    results = []

    for json_file in sorted(entries_dir.rglob('*.json')):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                entry = json.load(f)

            entry_id = entry.get('id', 'unknown')
            headword = entry.get('headword', '')
            reading = entry.get('reading', '')

            # Collect all text fields to scan with their field names
            fields_to_scan = []

            # Entry-level notes
            notes = entry.get('notes', '')
            if notes:
                fields_to_scan.append(('notes', notes))

            # Definition explanations
            for i, defn in enumerate(entry.get('definitions', [])):
                explanation = defn.get('explanation', '')
                if explanation:
                    fields_to_scan.append((f'definitions[{i}].explanation', explanation))

            # Example sentences and notes
            for i, example in enumerate(entry.get('examples', [])):
                japanese = example.get('japanese', '')
                if japanese:
                    fields_to_scan.append((f'examples[{i}].japanese', japanese))
                example_notes = example.get('notes', '')
                if example_notes:
                    fields_to_scan.append((f'examples[{i}].notes', example_notes))

            # Check all fields for missing furigana
            all_kanji = set()
            all_contexts = []
            fields_with_issues = []

            for field_name, text in fields_to_scan:
                has_missing, kanji_list = contains_unannotated_kanji(text)
                if has_missing:
                    all_kanji.update(kanji_list)
                    contexts = extract_unannotated_context(text)
                    all_contexts.extend(contexts)
                    fields_with_issues.append(field_name)

            if all_kanji:
                # Get relative path from entries directory
                rel_path = json_file.relative_to(entries_dir)

                results.append({
                    'id': entry_id,
                    'file_path': str(rel_path),
                    'headword': headword,
                    'reading': reading,
                    'unannotated_kanji': list(all_kanji),
                    'context_snippets': all_contexts[:5],  # Limit total contexts
                    'fields': fields_with_issues
                })
        except json.JSONDecodeError as e:
            print(f"Error parsing {json_file}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing {json_file}: {e}", file=sys.stderr)

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Find dictionary entries with kanji lacking furigana in text fields'
    )
    parser.add_argument(
        '-o', '--output',
        type=Path,
        default=None,
        help='Output file path (default: stdout). Using this flag prevents stderr contamination.'
    )
    args = parser.parse_args()

    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'

    if not entries_dir.exists():
        print(f"Error: entries directory not found at {entries_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning entries in {entries_dir}...", file=sys.stderr)

    results = scan_entries(entries_dir)

    print(f"Found {len(results)} entries with missing furigana", file=sys.stderr)

    # Output JSON for further processing
    output = {
        'description': 'Dictionary entries with kanji lacking furigana in text fields',
        'total_count': len(results),
        'entries': results
    }

    json_output = json.dumps(output, ensure_ascii=False, indent=2)

    if args.output:
        # Write directly to file (prevents stderr contamination)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(json_output)
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        # Output to stdout (can be redirected to file)
        print(json_output)


if __name__ == '__main__':
    main()
