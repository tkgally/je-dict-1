#!/usr/bin/env python3
"""
Extract register/pragmatic tags from dictionary entry notes.

Scans the notes field for keywords indicating:
- Formality (formal, neutral, informal, vulgar)
- Politeness (honorific, humble, polite, plain)
- Style (written, spoken, literary, archaic, slang)
- Domain (business, academic, technical, legal, medical, colloquial, internet)

Usage:
    python3 build/extract_register_tags.py --analyze          # Show extraction statistics
    python3 build/extract_register_tags.py --output FILE      # Export suggestions to JSON
    python3 build/extract_register_tags.py --apply            # Apply tags to entries
    python3 build/extract_register_tags.py --apply-defaults   # Apply default tags to untagged entries

Options:
    --analyze         Analyze entries and show statistics
    --output FILE     Export suggested tags to JSON file
    --apply           Apply extracted tags to entries
    --apply-defaults  Apply default formality/politeness to entries without register info
    --verbose         Show detailed output
"""

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


# Patterns for extracting register information from notes
# Each pattern has: (regex, tag_category, tag_value, confidence)

REGISTER_PATTERNS = [
    # Explicit register tags in notes
    (r'\[Register:\s*Formal\]', 'formality', 'formal', 1.0),
    (r'\[Register:\s*Neutral\]', 'formality', 'neutral', 1.0),
    (r'\[Register:\s*Neutral to Formal\]', 'formality', 'formal', 0.8),
    (r'\[Register:\s*Informal\]', 'formality', 'informal', 1.0),
    (r'\[Register:\s*Casual\]', 'formality', 'informal', 1.0),
    (r'\[Register:\s*Vulgar\]', 'formality', 'vulgar', 1.0),

    # Formality keywords
    (r'\bvery formal\b', 'formality', 'formal', 0.9),
    (r'\bmore formal\b', 'formality', 'formal', 0.8),
    (r'\bslightly more formal\b', 'formality', 'formal', 0.7),
    (r'\bformal\b(?!\s*equivalent)', 'formality', 'formal', 0.7),
    (r'\binformal\b', 'formality', 'informal', 0.8),
    (r'\bcasual\b', 'formality', 'informal', 0.7),
    (r'\bvulgar\b', 'formality', 'vulgar', 0.9),
    (r'\bcrude\b', 'formality', 'vulgar', 0.8),
    (r'\boffensive\b', 'formality', 'vulgar', 0.7),

    # Keigo patterns - politeness
    (r'謙譲語|humble\s*(verb|form|language)', 'politeness', 'humble', 0.95),
    (r'尊敬語|honorific\s*(verb|form|language)', 'politeness', 'honorific', 0.95),
    (r'丁寧語|polite\s*(verb|form|language)', 'politeness', 'polite', 0.9),
    (r'\bhumble\b', 'politeness', 'humble', 0.8),
    (r'\bhonorific\b', 'politeness', 'honorific', 0.8),
    (r'\bkeigo\b', 'politeness', 'polite', 0.7),

    # Style patterns
    (r'\bwritten\s*(language|form|Japanese)\b', 'style', 'written', 0.8),
    (r'\bspoken\s*(language|form|Japanese)\b', 'style', 'spoken', 0.8),
    (r'\bliterary\b', 'style', 'literary', 0.8),
    (r'\barchaic\b', 'style', 'archaic', 0.8),
    (r'\bold[- ]fashioned\b', 'style', 'archaic', 0.7),
    (r'\bslang\b', 'style', 'slang', 0.9),
    (r'\byouth\s*slang\b', 'style', 'slang', 0.9),
    (r'\binternet\s*slang\b', 'style', 'slang', 0.9),

    # Domain patterns
    (r'\bbusiness\s*(setting|context|Japanese|term)?\b', 'domain', 'business', 0.8),
    (r'\bacademic\b', 'domain', 'academic', 0.8),
    (r'\btechnical\b', 'domain', 'technical', 0.7),
    (r'\blegal\b', 'domain', 'legal', 0.8),
    (r'\bmedical\b', 'domain', 'medical', 0.8),
    (r'\bcolloquial\b', 'domain', 'colloquial', 0.8),
    (r'\binternet\b(?!\s*slang)', 'domain', 'internet', 0.7),
    (r'\bSNS\b', 'domain', 'internet', 0.7),
    (r'\bonline\b', 'domain', 'internet', 0.6),
]

# Known keigo words for automatic tagging
KEIGO_WORDS = {
    # Honorific verbs (尊敬語)
    'いらっしゃる': ('politeness', 'honorific'),
    'おっしゃる': ('politeness', 'honorific'),
    'なさる': ('politeness', 'honorific'),
    'ご覧になる': ('politeness', 'honorific'),
    'ごらんになる': ('politeness', 'honorific'),
    '召し上がる': ('politeness', 'honorific'),
    'めしあがる': ('politeness', 'honorific'),
    'お越しになる': ('politeness', 'honorific'),
    'おいでになる': ('politeness', 'honorific'),
    'くださる': ('politeness', 'honorific'),

    # Humble verbs (謙譲語)
    '申す': ('politeness', 'humble'),
    'もうす': ('politeness', 'humble'),
    '参る': ('politeness', 'humble'),
    'まいる': ('politeness', 'humble'),
    'いただく': ('politeness', 'humble'),
    '頂く': ('politeness', 'humble'),
    '存じる': ('politeness', 'humble'),
    'ぞんじる': ('politeness', 'humble'),
    '存ずる': ('politeness', 'humble'),
    '伺う': ('politeness', 'humble'),
    'うかがう': ('politeness', 'humble'),
    '承る': ('politeness', 'humble'),
    'うけたまわる': ('politeness', 'humble'),
    '拝見する': ('politeness', 'humble'),
    '拝読する': ('politeness', 'humble'),
    '頂戴する': ('politeness', 'humble'),
    'ちょうだいする': ('politeness', 'humble'),
    '差し上げる': ('politeness', 'humble'),
    'さしあげる': ('politeness', 'humble'),
    '申し上げる': ('politeness', 'humble'),
    'もうしあげる': ('politeness', 'humble'),

    # Polite forms (丁寧語)
    'ございます': ('politeness', 'polite'),
    'でございます': ('politeness', 'polite'),
}

# Words that indicate formal register
FORMAL_WORDS = {
    '敬語', 'けいご', '尊敬', '謙譲', '丁寧',
}


def extract_tags_from_notes(notes: str) -> dict:
    """
    Extract register tags from the notes field.

    Returns:
        Dict with keys: formality, politeness, style, domain
        Each value is a list of (tag_value, confidence) tuples
    """
    if not notes:
        return {}

    results = defaultdict(list)
    notes_lower = notes.lower()

    for pattern, category, value, confidence in REGISTER_PATTERNS:
        if re.search(pattern, notes, re.IGNORECASE):
            results[category].append((value, confidence))

    # Deduplicate and keep highest confidence for each category-value pair
    final_results = {}
    for category, items in results.items():
        # Group by value and keep highest confidence
        by_value = {}
        for value, conf in items:
            if value not in by_value or conf > by_value[value]:
                by_value[value] = conf
        final_results[category] = list(by_value.items())

    return final_results


def extract_tags_from_entry(entry: dict) -> dict:
    """
    Extract register tags from an entry.

    Checks:
    1. Notes field for keywords
    2. Headword/reading for known keigo words
    3. Cross-references for keigo type

    Returns:
        Dict with suggested tags and confidence scores
    """
    suggestions = defaultdict(list)

    # Extract from notes
    notes = entry.get('notes', '')
    if notes:
        notes_tags = extract_tags_from_notes(notes)
        for category, items in notes_tags.items():
            suggestions[category].extend(items)

    # Check for known keigo words
    headword = entry.get('headword', '')
    reading = entry.get('reading', '')

    # Clean headword of furigana markup
    clean_headword = re.sub(r'\{([^|]+)\|[^}]+\}', r'\1', headword)

    for word, (category, value) in KEIGO_WORDS.items():
        if word in clean_headword or word in reading:
            suggestions[category].append((value, 0.95))
            # Keigo words are typically formal
            suggestions['formality'].append(('formal', 0.9))

    # Check cross-references for keigo type
    cross_refs = entry.get('cross_references', [])
    for ref in cross_refs:
        if isinstance(ref, dict):
            ref_type = ref.get('type', '')
            label = ref.get('label', '').lower()
            if ref_type == 'keigo':
                if 'humble' in label:
                    suggestions['politeness'].append(('humble', 0.9))
                    suggestions['formality'].append(('formal', 0.85))
                elif 'honorific' in label:
                    suggestions['politeness'].append(('honorific', 0.9))
                    suggestions['formality'].append(('formal', 0.85))

    # Consolidate results - keep highest confidence per value
    final = {}
    for category, items in suggestions.items():
        by_value = {}
        for value, conf in items:
            if value not in by_value or conf > by_value[value]:
                by_value[value] = conf

        # For formality/politeness, keep only the highest confidence single value
        if category in ('formality', 'politeness'):
            if by_value:
                best = max(by_value.items(), key=lambda x: x[1])
                final[category] = {'value': best[0], 'confidence': best[1]}
        else:
            # For style/domain, can have multiple values
            if by_value:
                final[category] = [{'value': v, 'confidence': c} for v, c in by_value.items()]

    return final


def analyze_entries(project_root: Path) -> dict:
    """Analyze all entries and return statistics."""
    entries_dir = project_root / 'entries'

    stats = {
        'total': 0,
        'with_formality': 0,
        'with_politeness': 0,
        'with_style': 0,
        'with_domain': 0,
        'formality_dist': Counter(),
        'politeness_dist': Counter(),
        'style_dist': Counter(),
        'domain_dist': Counter(),
        'entries_with_suggestions': [],
    }

    for file_path in sorted(entries_dir.glob('**/*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        stats['total'] += 1

        suggestions = extract_tags_from_entry(entry)

        if suggestions:
            entry_info = {
                'id': entry.get('id'),
                'headword': entry.get('headword'),
                'suggestions': suggestions,
            }
            stats['entries_with_suggestions'].append(entry_info)

            if 'formality' in suggestions:
                stats['with_formality'] += 1
                stats['formality_dist'][suggestions['formality']['value']] += 1

            if 'politeness' in suggestions:
                stats['with_politeness'] += 1
                stats['politeness_dist'][suggestions['politeness']['value']] += 1

            if 'style' in suggestions:
                stats['with_style'] += 1
                for item in suggestions['style']:
                    stats['style_dist'][item['value']] += 1

            if 'domain' in suggestions:
                stats['with_domain'] += 1
                for item in suggestions['domain']:
                    stats['domain_dist'][item['value']] += 1

    return stats


def apply_tags_to_entry(entry: dict, suggestions: dict, confidence_threshold: float = 0.7) -> tuple[dict, bool]:
    """
    Apply suggested tags to an entry.

    Returns:
        Tuple of (modified_entry, was_modified)
    """
    modified = False

    # Ensure tags structure exists
    if 'metadata' not in entry:
        entry['metadata'] = {}
    if 'tags' not in entry['metadata']:
        entry['metadata']['tags'] = {}

    tags = entry['metadata']['tags']

    # Apply formality if confidence is high enough
    if 'formality' in suggestions:
        if suggestions['formality']['confidence'] >= confidence_threshold:
            if tags.get('formality') != suggestions['formality']['value']:
                tags['formality'] = suggestions['formality']['value']
                modified = True

    # Apply politeness if confidence is high enough
    if 'politeness' in suggestions:
        if suggestions['politeness']['confidence'] >= confidence_threshold:
            if tags.get('politeness') != suggestions['politeness']['value']:
                tags['politeness'] = suggestions['politeness']['value']
                modified = True

    # Apply style tags
    if 'style' in suggestions:
        new_styles = [item['value'] for item in suggestions['style']
                      if item['confidence'] >= confidence_threshold]
        if new_styles:
            existing = set(tags.get('style', []))
            combined = sorted(existing | set(new_styles))
            if combined != tags.get('style', []):
                tags['style'] = combined
                modified = True

    # Apply domain tags
    if 'domain' in suggestions:
        new_domains = [item['value'] for item in suggestions['domain']
                       if item['confidence'] >= confidence_threshold]
        if new_domains:
            existing = set(tags.get('domain', []))
            combined = sorted(existing | set(new_domains))
            if combined != tags.get('domain', []):
                tags['domain'] = combined
                modified = True

    if modified:
        entry['metadata']['modified'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    return entry, modified


def apply_default_tags(entry: dict) -> tuple[dict, bool]:
    """
    Apply default register tags to entries without explicit register info.

    Defaults:
    - formality: "neutral"
    - politeness: "plain"

    Returns:
        Tuple of (modified_entry, was_modified)
    """
    modified = False

    # Ensure tags structure exists
    if 'metadata' not in entry:
        entry['metadata'] = {}
    if 'tags' not in entry['metadata']:
        entry['metadata']['tags'] = {}

    tags = entry['metadata']['tags']

    # Apply default formality if not set
    if not tags.get('formality'):
        tags['formality'] = 'neutral'
        modified = True

    # Apply default politeness if not set
    if not tags.get('politeness'):
        tags['politeness'] = 'plain'
        modified = True

    if modified:
        entry['metadata']['modified'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    return entry, modified


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Extract register tags from notes')
    parser.add_argument('--analyze', action='store_true', help='Analyze and show statistics')
    parser.add_argument('--output', type=str, help='Export suggestions to JSON file')
    parser.add_argument('--apply', action='store_true', help='Apply extracted tags to entries')
    parser.add_argument('--apply-defaults', action='store_true', help='Apply default tags to untagged entries')
    parser.add_argument('--confidence', type=float, default=0.7, help='Minimum confidence threshold (default: 0.7)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'

    if args.analyze:
        print("Analyzing entries for register tags...")
        print("-" * 60)

        stats = analyze_entries(project_root)

        print(f"\nTotal entries: {stats['total']}")
        print(f"Entries with formality suggestions: {stats['with_formality']}")
        print(f"Entries with politeness suggestions: {stats['with_politeness']}")
        print(f"Entries with style suggestions: {stats['with_style']}")
        print(f"Entries with domain suggestions: {stats['with_domain']}")

        print("\nFormality distribution:")
        for value, count in stats['formality_dist'].most_common():
            print(f"  {value}: {count}")

        print("\nPoliteness distribution:")
        for value, count in stats['politeness_dist'].most_common():
            print(f"  {value}: {count}")

        print("\nStyle distribution:")
        for value, count in stats['style_dist'].most_common():
            print(f"  {value}: {count}")

        print("\nDomain distribution:")
        for value, count in stats['domain_dist'].most_common():
            print(f"  {value}: {count}")

        if args.verbose:
            print("\nSample entries with suggestions:")
            for entry in stats['entries_with_suggestions'][:20]:
                print(f"\n  {entry['id']}: {entry['headword']}")
                for cat, val in entry['suggestions'].items():
                    print(f"    {cat}: {val}")

        return 0

    if args.output:
        print(f"Extracting register tags and saving to {args.output}...")

        stats = analyze_entries(project_root)
        output_data = {
            'generated': datetime.now(timezone.utc).isoformat(),
            'total_entries': stats['total'],
            'entries_with_suggestions': len(stats['entries_with_suggestions']),
            'suggestions': stats['entries_with_suggestions'],
        }

        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"Saved {len(stats['entries_with_suggestions'])} suggestions to {args.output}")
        return 0

    if args.apply:
        print("Applying extracted register tags to entries...")
        print(f"Confidence threshold: {args.confidence}")
        print("-" * 60)

        applied_count = 0
        error_count = 0

        for file_path in sorted(entries_dir.glob('**/*.json')):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    entry = json.load(f)

                suggestions = extract_tags_from_entry(entry)
                if suggestions:
                    modified_entry, was_modified = apply_tags_to_entry(
                        entry, suggestions, args.confidence
                    )
                    if was_modified:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            json.dump(modified_entry, f, ensure_ascii=False, indent=2)
                        applied_count += 1
                        if args.verbose:
                            print(f"  Updated: {entry.get('id')}")

            except (json.JSONDecodeError, IOError) as e:
                print(f"Error processing {file_path}: {e}")
                error_count += 1

        print(f"\nApplied tags to {applied_count} entries")
        if error_count:
            print(f"Errors: {error_count}")
        return 0

    if args.apply_defaults:
        print("Applying default register tags to entries...")
        print("-" * 60)

        applied_count = 0
        error_count = 0

        for file_path in sorted(entries_dir.glob('**/*.json')):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    entry = json.load(f)

                modified_entry, was_modified = apply_default_tags(entry)
                if was_modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(modified_entry, f, ensure_ascii=False, indent=2)
                    applied_count += 1
                    if args.verbose:
                        print(f"  Updated: {entry.get('id')}")

            except (json.JSONDecodeError, IOError) as e:
                print(f"Error processing {file_path}: {e}")
                error_count += 1

        print(f"\nApplied default tags to {applied_count} entries")
        if error_count:
            print(f"Errors: {error_count}")
        return 0

    # Default: show help
    parser.print_help()
    return 1


if __name__ == '__main__':
    sys.exit(main())
