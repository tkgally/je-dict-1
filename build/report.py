#!/usr/bin/env python3
"""
Dictionary health dashboard for je-dict-1.

Provides a quick summary of the dictionary's current state including
entry counts, type breakdowns, cross-reference stats, example coverage,
inline link usage, furigana coverage, and recent activity.

Usage:
    python3 build/report.py
"""

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from constants import LINK_OPEN
from japanese_utils import FURIGANA_PATTERN, is_kanji, strip_furigana

try:
    import score_note_quality as _snq
    _SCORER_AVAILABLE = True
except ImportError:
    _SCORER_AVAILABLE = False


def load_all_entries(entries_dir: Path) -> list[dict]:
    """Load all entry JSON files from the entries directory."""
    entries = []
    for file_path in sorted(entries_dir.glob('**/*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entries.append(json.load(f))
        except (json.JSONDecodeError, IOError):
            pass
    return entries


def text_has_uncovered_kanji(text: str) -> bool:
    """Check if text contains kanji not wrapped in furigana markup."""
    stripped = FURIGANA_PATTERN.sub('', text)
    return any(is_kanji(ch) for ch in stripped)


def report_tier_breakdown(entries: list[dict]) -> None:
    """Print entry counts by vocabulary tier."""
    tier_counts = Counter()
    for entry in entries:
        tier = entry.get('metadata', {}).get('vocabulary_tier') or 'unset'
        tier_counts[tier] += 1

    print("VOCABULARY TIERS")
    print("-" * 40)
    for tier in ['basic', 'core', 'general', 'unset']:
        count = tier_counts.get(tier, 0)
        if count > 0:
            print(f"  {tier:<12} {count:>6}")
    print(f"  {'TOTAL':<12} {len(entries):>6}")
    print()


def report_pos_breakdown(entries: list[dict]) -> None:
    """Print entry counts by part-of-speech tag."""
    pos_counts = Counter()
    no_pos_count = 0
    for entry in entries:
        tags = entry.get('metadata', {}).get('tags', {})
        pos_list = tags.get('pos', [])
        if not pos_list:
            no_pos_count += 1
        for pos in pos_list:
            pos_counts[pos] += 1

    print("PART OF SPEECH (tags.pos)")
    print("-" * 40)
    for pos, count in pos_counts.most_common():
        print(f"  {pos:<24} {count:>6}")
    if no_pos_count:
        print(f"  {'(no pos tags)':<24} {no_pos_count:>6}")
    print()


def report_cross_references(entries: list[dict]) -> None:
    """Print cross-reference statistics."""
    total_refs = 0
    with_target_id = 0
    without_target_id = 0
    legacy_string = 0
    type_counts = Counter()
    entries_with_refs = 0

    all_ids = {e['id'] for e in entries}

    for entry in entries:
        refs = entry.get('cross_references', [])
        if refs:
            entries_with_refs += 1
        for ref in refs:
            total_refs += 1
            if isinstance(ref, str):
                legacy_string += 1
            elif isinstance(ref, dict):
                ref_type = ref.get('type', 'unknown')
                type_counts[ref_type] += 1
                if ref.get('target_id'):
                    target = ref['target_id']
                    if target in all_ids:
                        with_target_id += 1
                    else:
                        with_target_id += 1  # count as hardened even if stale
                else:
                    without_target_id += 1

    print("CROSS-REFERENCES")
    print("-" * 40)
    print(f"  Total references:      {total_refs:>6}")
    print(f"  Entries with refs:     {entries_with_refs:>6}")
    print(f"  Hardened (target_id):  {with_target_id:>6}")
    print(f"  Unhardened (lookup):   {without_target_id:>6}")
    if legacy_string:
        print(f"  Legacy string format:  {legacy_string:>6}")
    print()
    if type_counts:
        print("  By type:")
        for ref_type, count in type_counts.most_common():
            print(f"    {ref_type:<20} {count:>6}")
        print()


def report_examples(entries: list[dict]) -> None:
    """Print example sentence statistics."""
    total_examples = 0
    entries_with_zero = 0
    example_counts = []

    for entry in entries:
        examples = entry.get('examples', [])
        count = len(examples)
        total_examples += count
        example_counts.append(count)
        if count == 0:
            entries_with_zero += 1

    avg = total_examples / len(entries) if entries else 0

    print("EXAMPLE SENTENCES")
    print("-" * 40)
    print(f"  Total examples:        {total_examples:>6}")
    print(f"  Average per entry:     {avg:>9.1f}")
    print(f"  Entries with 0:        {entries_with_zero:>6}")

    # Distribution
    dist = Counter()
    for c in example_counts:
        if c == 0:
            dist['0'] += 1
        elif c <= 2:
            dist['1-2'] += 1
        elif c <= 4:
            dist['3-4'] += 1
        elif c <= 6:
            dist['5-6'] += 1
        elif c <= 9:
            dist['7-9'] += 1
        else:
            dist['10+'] += 1

    print("  Distribution:")
    for bucket in ['0', '1-2', '3-4', '5-6', '7-9', '10+']:
        count = dist.get(bucket, 0)
        print(f"    {bucket + ' examples':<20} {count:>6}")
    print()


def report_inline_links(entries: list[dict]) -> None:
    """Print inline word link coverage statistics."""
    entries_with_links = 0
    total_links = 0

    for entry in entries:
        entry_has_links = False
        for example in entry.get('examples', []):
            jp = example.get('japanese', '')
            link_count = jp.count(LINK_OPEN)
            if link_count > 0:
                entry_has_links = True
                total_links += link_count
        # Also check notes
        notes = entry.get('notes', '') or ''
        notes_links = notes.count(LINK_OPEN)
        if notes_links > 0:
            entry_has_links = True
            total_links += notes_links

        if entry_has_links:
            entries_with_links += 1

    pct = (entries_with_links / len(entries) * 100) if entries else 0

    print("INLINE WORD LINKS")
    print("-" * 40)
    print(f"  Entries with links:    {entries_with_links:>6} ({pct:.1f}%)")
    print(f"  Total link instances:  {total_links:>6}")
    print()


def report_furigana(entries: list[dict]) -> None:
    """Print furigana coverage statistics."""
    entries_checked = 0
    entries_with_gaps = 0
    gap_locations = Counter()  # which fields have gaps

    for entry in entries:
        entries_checked += 1
        has_gap = False

        # Check headword
        headword = entry.get('headword', '')
        if text_has_uncovered_kanji(headword):
            has_gap = True
            gap_locations['headword'] += 1

        # Check examples
        for example in entry.get('examples', []):
            jp = example.get('japanese', '')
            if text_has_uncovered_kanji(jp):
                has_gap = True
                gap_locations['examples'] += 1
                break  # count once per entry

        # Check notes
        notes = entry.get('notes', '') or ''
        if notes and text_has_uncovered_kanji(notes):
            has_gap = True
            gap_locations['notes'] += 1

        if has_gap:
            entries_with_gaps += 1

    covered = entries_checked - entries_with_gaps
    pct = (covered / entries_checked * 100) if entries_checked else 0

    print("FURIGANA COVERAGE")
    print("-" * 40)
    print(f"  Fully covered:         {covered:>6} ({pct:.1f}%)")
    print(f"  Entries with gaps:     {entries_with_gaps:>6}")
    if gap_locations:
        print("  Gap locations:")
        for loc, count in gap_locations.most_common():
            print(f"    {loc:<20} {count:>6}")
    print()


def report_recent_activity(entries: list[dict], days: int = 7) -> None:
    """Print entries modified in the last N days."""
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)
    recent = []

    for entry in entries:
        modified_str = entry.get('metadata', {}).get('modified', '')
        if not modified_str:
            continue
        try:
            dt = datetime.fromisoformat(modified_str.replace('Z', '+00:00'))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            if dt >= cutoff:
                recent.append((dt, entry['id'], entry.get('headword', '')))
        except (ValueError, AttributeError):
            pass

    recent.sort(key=lambda x: x[0], reverse=True)

    print(f"RECENT ACTIVITY (last {days} days)")
    print("-" * 40)
    print(f"  Entries modified:      {len(recent):>6}")
    if recent:
        shown = recent[:15]
        for dt, entry_id, headword in shown:
            date_str = dt.strftime('%Y-%m-%d')
            print(f"    {date_str}  {entry_id:<24} {headword}")
        if len(recent) > 15:
            print(f"    ... and {len(recent) - 15} more")
    print()


def report_crossref_symmetry(entries: list[dict]) -> None:
    """Print cross-reference symmetry rate."""
    # Build directed-reference map from in-memory entries
    ref_map: dict[str, set[str]] = {}
    for entry in entries:
        eid = entry.get('id', '')
        targets = set()
        for ref in entry.get('cross_references', []):
            if isinstance(ref, dict) and ref.get('target_id'):
                targets.add(ref['target_id'])
        for ref in entry.get('prominent_see_also', []):
            if isinstance(ref, dict) and ref.get('target_id'):
                targets.add(ref['target_id'])
        ref_map[eid] = targets

    total_directed = sum(len(t) for t in ref_map.values())
    symmetric = 0
    asymmetric = 0
    seen = set()
    for src, targets in ref_map.items():
        for tgt in targets:
            pair = tuple(sorted([src, tgt]))
            if pair in seen:
                continue
            seen.add(pair)
            if src in ref_map.get(tgt, set()):
                symmetric += 1
            else:
                asymmetric += 1

    rate = (symmetric / (symmetric + asymmetric) * 100) if (symmetric + asymmetric) else 0

    print("CROSS-REFERENCE SYMMETRY")
    print("-" * 40)
    print(f"  Total directed references: {total_directed:>8}")
    print(f"  Symmetric pairs:           {symmetric:>8}")
    print(f"  Asymmetric references:     {asymmetric:>8}")
    print(f"  Symmetry rate:             {rate:>7.1f}%")
    print()


def report_note_quality(entries: list[dict]) -> None:
    """Print note quality summary — scorer mode if available, else length stats."""
    if _SCORER_AVAILABLE:
        _report_note_quality_scored(entries)
    else:
        _report_note_quality_length(entries)


def _report_note_quality_scored(entries: list[dict]) -> None:
    """Report note quality using the score_note_quality scorer."""
    script_dir = Path(__file__).parent
    templates_path = script_dir / 'note_templates.json'
    if not templates_path.exists():
        _report_note_quality_length(entries)
        return

    templates = _snq.load_templates(str(templates_path))
    buckets = Counter()  # 0-20, 21-40, 41-60, 61-80, 81-100
    pos_scores: dict[str, list[int]] = defaultdict(list)
    total_scored = 0

    for entry in entries:
        pos = entry.get('part_of_speech', '')
        template_key = _snq.normalize_pos(pos)
        template = templates.get(template_key, templates.get('_default', {}))
        notes = entry.get('notes', '') or ''
        score, _ = _snq.score_entry(entry, notes, template)

        total_scored += 1
        pos_scores[template_key].append(score)

        if score <= 20:
            buckets['0-20'] += 1
        elif score <= 40:
            buckets['21-40'] += 1
        elif score <= 60:
            buckets['41-60'] += 1
        elif score <= 80:
            buckets['61-80'] += 1
        else:
            buckets['81-100'] += 1

    print("NOTE QUALITY (scored)")
    print("-" * 40)
    print("  Score distribution:")
    for bucket in ['0-20', '21-40', '41-60', '61-80', '81-100']:
        count = buckets.get(bucket, 0)
        print(f"    {bucket:<10} {count:>6}")
    print()
    print(f"  {'POS':<24} {'Count':>6}  {'Avg':>5}")
    for pos_key in sorted(pos_scores.keys()):
        scores = pos_scores[pos_key]
        avg = sum(scores) / len(scores) if scores else 0
        print(f"    {pos_key:<22} {len(scores):>6}  {avg:>5.1f}")
    print()


def _report_note_quality_length(entries: list[dict]) -> None:
    """Fallback: report note quality by length per POS."""
    pos_stats: dict[str, list[int]] = defaultdict(list)
    without_notes = 0

    for entry in entries:
        notes = entry.get('notes', '') or ''
        if not notes:
            without_notes += 1
            continue
        tags = entry.get('metadata', {}).get('tags', {}).get('pos', [])
        primary_pos = tags[0] if tags else 'unknown'
        pos_stats[primary_pos].append(len(notes))

    print("NOTE QUALITY (by length)")
    print("-" * 40)
    print(f"  {'POS':<24} {'With Notes':>10} {'Avg Length':>11} {'Median':>8}")
    for pos in sorted(pos_stats.keys()):
        lengths = sorted(pos_stats[pos])
        avg = sum(lengths) / len(lengths) if lengths else 0
        median = lengths[len(lengths) // 2] if lengths else 0
        print(f"    {pos:<22} {len(lengths):>10} {avg:>11.0f} {median:>8}")
    print(f"  Entries without notes:  {without_notes:>6}")
    print()


def report_pos_completeness(entries: list[dict]) -> None:
    """Print POS section completeness for verbs and na-adjectives."""
    verb_total = 0
    verb_transitivity = 0
    verb_teiru = 0
    verb_collocations = 0
    verb_conjugation = 0

    na_total = 0
    na_collocations = 0
    na_conjugation = 0

    for entry in entries:
        pos_tags = entry.get('metadata', {}).get('tags', {}).get('pos', [])
        sem_tags = entry.get('metadata', {}).get('tags', {}).get('semantic', [])
        notes = (entry.get('notes', '') or '').lower()

        is_verb = any(p.startswith('verb') for p in pos_tags)
        is_na = 'adjective-na' in pos_tags

        if is_verb:
            verb_total += 1
            if ('transitive' in sem_tags or 'intransitive' in sem_tags or
                    '自動詞' in notes or '他動詞' in notes or
                    'transitive' in notes or 'intransitive' in notes):
                verb_transitivity += 1
            if 'aspect' in notes or 'ている' in notes:
                verb_teiru += 1
            if 'collocation' in notes or '〜' in entry.get('notes', ''):
                verb_collocations += 1
            if entry.get('conjugation'):
                verb_conjugation += 1

        if is_na:
            na_total += 1
            if 'collocation' in notes or '〜' in entry.get('notes', ''):
                na_collocations += 1
            if entry.get('conjugation'):
                na_conjugation += 1

    def pct(n, total):
        return f"{n / total * 100:.1f}%" if total else "N/A"

    print("POS SECTION COMPLETENESS")
    print("-" * 40)
    print(f"  Verbs ({verb_total} total):")
    print(f"    With transitivity:   {verb_transitivity:>6} ({pct(verb_transitivity, verb_total)})")
    print(f"    With ている docs:    {verb_teiru:>6} ({pct(verb_teiru, verb_total)})")
    print(f"    With collocations:   {verb_collocations:>6} ({pct(verb_collocations, verb_total)})")
    print(f"    With conjugation:    {verb_conjugation:>6} ({pct(verb_conjugation, verb_total)})")
    print(f"  Na-adjectives ({na_total} total):")
    print(f"    With collocations:   {na_collocations:>6} ({pct(na_collocations, na_total)})")
    print(f"    With conjugation:    {na_conjugation:>6} ({pct(na_conjugation, na_total)})")
    print()


def report_polishing_progress(project_root: Path) -> None:
    """Print polishing task completion percentages."""
    tasks_dir = project_root / 'polishing' / 'tasks'
    if not tasks_dir.exists():
        return

    # Find max entry ID
    max_id = 0
    entries_dir = project_root / 'entries'
    for f in entries_dir.glob('**/*.json'):
        try:
            num = int(f.stem.split('_')[0])
            if num > max_id:
                max_id = num
        except (ValueError, IndexError):
            pass

    if max_id == 0:
        return

    print("POLISHING PROGRESS")
    print("-" * 40)
    print(f"  {'Task':<28} {'Progress':>8} {'Next Entry':>12}")

    for progress_file in sorted(tasks_dir.glob('*/progress.txt')):
        task_name = progress_file.parent.name
        # Find the last "next: XXXXX" line
        next_id = 0
        try:
            text = progress_file.read_text(encoding='utf-8')
            for line in text.splitlines():
                line = line.strip()
                if line.startswith('next:'):
                    val = line.split(':', 1)[1].strip()
                    try:
                        next_id = int(val)
                    except ValueError:
                        pass
        except IOError:
            continue

        pct = (next_id / max_id * 100) if max_id else 0
        print(f"    {task_name:<26} {pct:>7.1f}% {next_id:>10}")

    print()


def report_candidate_health(project_root: Path) -> None:
    """Print candidate queue statistics."""
    cand_file = project_root / 'candidate_words.json'
    if not cand_file.exists():
        print("CANDIDATE QUEUE")
        print("-" * 40)
        print("  (candidate_words.json not found)")
        print()
        return

    try:
        with open(cand_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        return

    candidates = data.get('candidates', [])
    total = len(candidates)

    print("CANDIDATE QUEUE")
    print("-" * 40)
    print(f"  Total candidates:      {total:>8}")

    # Check for date field to report oldest
    if candidates:
        dates = [c.get('added', '') for c in candidates if c.get('added')]
        if dates:
            oldest = min(dates)
            print(f"  Oldest candidate:      {oldest[:10]}")

    print()


def report_consistency_summary(project_root: Path) -> None:
    """Print one-line summary from check_consistency.py."""
    script = project_root / 'build' / 'check_consistency.py'
    if not script.exists():
        print("CONSISTENCY SUMMARY")
        print("-" * 40)
        print("  (check_consistency.py not available)")
        print()
        return

    try:
        result = subprocess.run(
            [sys.executable, str(script), '--json'],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode != 0:
            print("CONSISTENCY SUMMARY")
            print("-" * 40)
            print(f"  (check_consistency.py failed: exit {result.returncode})")
            print()
            return

        data = json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError) as e:
        print("CONSISTENCY SUMMARY")
        print("-" * 40)
        print(f"  (check_consistency.py error: {e})")
        print()
        return

    print("CONSISTENCY SUMMARY")
    print("-" * 40)

    labels = {
        'note-structure': ('Note structure issues', lambda v: len(v)),
        'crossref-asymmetry': ('Cross-ref asymmetry',
                               lambda v: f"{v.get('asymmetric_pairs', 'N/A')} pairs"
                               if 'error' not in v else 'N/A'),
        'note-length': ('Note length outliers',
                        lambda v: len(v.get('too_short', [])) + len(v.get('too_long', []))),
        'missing-transitivity': ('Missing transitivity', lambda v: len(v)),
        'no-collocations': ('No collocations', lambda v: len(v)),
        'example-count': ('Example count gaps', lambda v: len(v)),
    }

    for key, (label, count_fn) in labels.items():
        if key in data:
            count = count_fn(data[key])
            print(f"  {label + ':':<26} {count:>8}")

    print("  (Full report: python3 build/check_consistency.py)")
    print()


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'

    if not entries_dir.exists():
        print(f"Error: entries directory not found: {entries_dir}")
        return 1

    print("Loading entries...")
    entries = load_all_entries(entries_dir)

    if not entries:
        print("No entries found.")
        return 1

    print(f"Loaded {len(entries)} entries.\n")
    print("=" * 40)
    print("  DICTIONARY HEALTH REPORT")
    print("=" * 40)
    print()

    report_tier_breakdown(entries)
    report_pos_breakdown(entries)
    report_cross_references(entries)
    report_crossref_symmetry(entries)
    report_examples(entries)
    report_inline_links(entries)
    report_furigana(entries)
    report_note_quality(entries)
    report_pos_completeness(entries)
    report_polishing_progress(project_root)
    report_candidate_health(project_root)
    report_consistency_summary(project_root)
    report_recent_activity(entries)

    return 0


if __name__ == '__main__':
    sys.exit(main())
