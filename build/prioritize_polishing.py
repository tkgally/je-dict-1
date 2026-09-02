#!/usr/bin/env python3
"""Generate polishing priority lists for je-dict-1.

Scores every entry across multiple quality dimensions and generates
priority-ordered lists for each polishing task. Higher priority entries
(worst quality) are listed first.

Each dimension scores 0.0 (worst) to 1.0 (best). A task combines a weighted
mix of dimensions (weights sum to 1) and the priority is
``tier_weight * (1 - weighted quality)``, so basic-tier entries (x3) and
core-tier entries (x2) surface ahead of general-tier entries with the same
gaps.

Dimensions
    note_quality          build/score_note_quality.py score / 100
    furigana_coverage     no bare kanji in notes or examples (inline-link
                          base forms are not displayed and are ignored)
    example_count         examples vs the tier minimum per sense
    cross_refs            number of cross_references + prominent_see_also
    transitivity_info     verbs: notes mention transitivity
    never_modified        metadata.modified differs from metadata.created
                          (an entry never touched since creation scores 0)
    verb_transitivity_tag godan/ichidan verbs carry tags.transitivity
    linkable_unlinked     cross_references is empty although a SIMILAR /
                          RELATED / CONTRAST line names a word that has
                          exactly one entry in build/word_id_lookup.json
                          (graded: 1, 2, 3+ such words)
    politeness_formality  tags.politeness and tags.formality both present
    note_bloat            displayed notes under the bloat threshold
    accuracy_flag         no outstanding cross-model accuracy flag
                          (reviews/accuracy_flags.jsonl minus decisions in
                          reviews/decisions.jsonl dated at/after the review;
                          errors score 0, warnings only 0.5)

Usage:
    python3 build/prioritize_polishing.py              # Generate all priority files
    python3 build/prioritize_polishing.py --summary    # Show statistics only
    python3 build/prioritize_polishing.py --task notes  # One task only
    python3 build/prioritize_polishing.py --dry-run    # Print to stdout
    python3 build/prioritize_polishing.py --limit 100  # Top N per task
"""

import argparse
import json
import os
import sys
from datetime import date, datetime, timezone

# Add build dir to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_note_quality import (  # noqa: E402
    DEFAULT_TEMPLATES_PATH,
    LINK_RE,
    analyze_notes,
    bloat_threshold,
    display_text,
    has_bare_kanji,
    load_headers,
    load_templates,
    score_entry as score_note,
    strip_furigana_text,
    template_key_for_entry,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORD_LOOKUP_PATH = os.path.join(BASE_DIR, 'build', 'word_id_lookup.json')
ACCURACY_FLAGS_PATH = os.path.join(BASE_DIR, 'reviews', 'accuracy_flags.jsonl')
DECISIONS_PATH = os.path.join(BASE_DIR, 'reviews', 'decisions.jsonl')


# ---------------------------------------------------------------------------
# Entry loading
# ---------------------------------------------------------------------------

def load_all_entries(entries_dir):
    """Load all entry JSON files from the entries directory."""
    entries = []
    for range_dir in sorted(os.listdir(entries_dir)):
        range_path = os.path.join(entries_dir, range_dir)
        if not os.path.isdir(range_path):
            continue
        for fname in sorted(os.listdir(range_path)):
            if not fname.endswith('.json'):
                continue
            fpath = os.path.join(range_path, fname)
            try:
                with open(fpath) as f:
                    data = json.load(f)
                entry_id = fname.replace('.json', '')
                entries.append({'id': entry_id, 'data': data})
            except (json.JSONDecodeError, IOError):
                continue
    return entries


# ---------------------------------------------------------------------------
# Shared context: templates, headword lookup, outstanding accuracy flags
# ---------------------------------------------------------------------------

def load_word_lookup(path=WORD_LOOKUP_PATH):
    """Return the by_headword map of build/word_id_lookup.json ({} if missing)."""
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f).get('by_headword', {}) or {}
    except (FileNotFoundError, json.JSONDecodeError, AttributeError):
        return {}


def _parse_ts(value):
    """Parse an ISO-8601 timestamp; returns None when unparseable."""
    if not value or not isinstance(value, str):
        return None
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def _iter_jsonl(path):
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        return


def load_outstanding_flags(flags_path=ACCURACY_FLAGS_PATH, decisions_path=DECISIONS_PATH):
    """Map entry_id -> 'error' | 'warn' for accuracy flags nobody has adjudicated.

    reviews/accuracy_flags.jsonl holds one line per flagged review (the last
    line for an entry_id wins). A flag is outstanding when the entry has no
    reviews/decisions.jsonl line with ts >= reviewed_at. A missing flags file
    means no outstanding flags.
    """
    latest = {}
    for rec in _iter_jsonl(flags_path):
        eid = rec.get('entry_id')
        if eid:
            latest[eid] = rec
    if not latest:
        return {}

    last_decision = {}          # numeric id or full id -> latest decision ts
    for rec in _iter_jsonl(decisions_path):
        key = str(rec.get('entry') or '').strip()
        ts = _parse_ts(rec.get('ts'))
        if not key or ts is None:
            continue
        if key not in last_decision or ts > last_decision[key]:
            last_decision[key] = ts

    outstanding = {}
    for eid, rec in latest.items():
        issues = rec.get('issues') or []
        if not issues:
            continue
        reviewed_at = _parse_ts(rec.get('reviewed_at'))
        numeric = eid.split('_')[0]
        decided = [t for t in (last_decision.get(eid), last_decision.get(numeric)) if t]
        if reviewed_at is not None and any(t >= reviewed_at for t in decided):
            continue
        if reviewed_at is None and decided:
            continue
        severity = 'error' if any((i or {}).get('severity') == 'error' for i in issues) else 'warn'
        outstanding[eid] = severity
    return outstanding


def build_context(base_dir=BASE_DIR):
    """Load everything the dimension scorers need, once."""
    templates_path = os.path.join(base_dir, 'build', 'note_templates.json')
    if not os.path.exists(templates_path):
        templates_path = DEFAULT_TEMPLATES_PATH
    return {
        'templates': load_templates(templates_path),
        'headers': load_headers(),
        'lookup': load_word_lookup(os.path.join(base_dir, 'build', 'word_id_lookup.json')),
        'flags': load_outstanding_flags(
            os.path.join(base_dir, 'reviews', 'accuracy_flags.jsonl'),
            os.path.join(base_dir, 'reviews', 'decisions.jsonl')),
    }


# ---------------------------------------------------------------------------
# Quality dimension scorers (each returns 0.0–1.0, where 1.0 = best)
# ---------------------------------------------------------------------------

def _tags(entry_data):
    meta = entry_data.get('metadata') if isinstance(entry_data.get('metadata'), dict) else {}
    tags = meta.get('tags') if isinstance(meta.get('tags'), dict) else {}
    return meta, tags


def score_note_quality(entry_data, templates=None):
    """Score note quality from 0.0 (worst) to 1.0 (best)."""
    if templates is None:
        templates = load_templates(DEFAULT_TEMPLATES_PATH)
    template_key = template_key_for_entry(entry_data)
    template = templates.get(template_key, templates.get('_default', {}))
    notes = entry_data.get('notes', '') or ''
    raw_score, _ = score_note(entry_data, notes, template)
    return raw_score / 100.0


def score_furigana_coverage(entry_data):
    """Score furigana coverage from 0.0 (bare kanji found) to 1.0 (all covered)."""
    notes = entry_data.get('notes', '') or ''
    examples = entry_data.get('examples', []) or []

    has_text = False
    has_bare = False

    if notes:
        has_text = True
        if has_bare_kanji(notes):
            has_bare = True

    for ex in examples:
        jp = ex.get('japanese', '') or ''
        if jp:
            has_text = True
            if has_bare_kanji(jp):
                has_bare = True
                break

    if not has_text:
        return 0.5  # neutral
    return 0.0 if has_bare else 1.0


def score_example_count(entry_data):
    """Score example count relative to minimum requirement. 0.0–1.0."""
    tier = (entry_data.get('metadata', {}) or {}).get('vocabulary_tier', 'general')
    min_per_sense = 5 if tier in ('basic', 'core') else 3

    senses = entry_data.get('definitions', []) or entry_data.get('senses', []) or []
    sense_count = max(len(senses), 1)
    required = min_per_sense * sense_count

    examples = entry_data.get('examples', []) or []
    count = len(examples)

    if count == 0:
        return 0.0
    return min(1.0, count / required)


def score_cross_refs(entry_data):
    """Score cross-reference count. 0.0–1.0."""
    prominent = entry_data.get('prominent_see_also', []) or []
    xrefs = entry_data.get('cross_references', []) or []
    total = len(prominent) + len(xrefs)

    if total == 0:
        return 0.0
    if total == 1:
        return 0.3
    if total == 2:
        return 0.6
    return 1.0


def score_transitivity_info(entry_data):
    """Score verb transitivity info presence. 0.0 or 1.0 (1.0 for non-verbs)."""
    pos = (entry_data.get('part_of_speech', '') or '').lower()
    if 'verb' not in pos:
        return 1.0  # not applicable

    notes = entry_data.get('notes', '') or ''
    keywords = ['transitive', 'intransitive', '自動詞', '他動詞', 'TRANSITIVITY']
    for kw in keywords:
        if kw.lower() in notes.lower():
            return 1.0
    return 0.0


def score_never_modified(entry_data):
    """0.0 when the entry has never been modified since creation, else 1.0."""
    meta, _ = _tags(entry_data)
    created = meta.get('created')
    modified = meta.get('modified')
    if created and modified and created == modified:
        return 0.0
    return 1.0


def score_verb_transitivity_tag(entry_data):
    """0.0 for a godan/ichidan verb with no tags.transitivity, else 1.0."""
    _, tags = _tags(entry_data)
    pos = tags.get('pos') or []
    if not any(p in ('verb-godan', 'verb-ichidan') for p in pos):
        return 1.0
    return 1.0 if tags.get('transitivity') else 0.0


def score_politeness_formality(entry_data):
    """1.0 with both tags, 0.5 with one, 0.0 with neither."""
    _, tags = _tags(entry_data)
    present = sum(1 for k in ('politeness', 'formality') if tags.get(k))
    return present / 2.0


def score_note_bloat(entry_data):
    """0.0 when the displayed notes exceed the bloat threshold, else 1.0."""
    notes = entry_data.get('notes', '') or ''
    return 0.0 if len(display_text(notes).strip()) > bloat_threshold(entry_data) else 1.0


def score_accuracy_flag(entry_id, flags):
    """0.0 with an outstanding error flag, 0.5 warnings only, else 1.0."""
    if not flags:
        return 1.0
    sev = flags.get(entry_id)
    if sev is None:
        sev = flags.get(entry_id.split('_')[0])
    if sev == 'error':
        return 0.0
    if sev == 'warn':
        return 0.5
    return 1.0


def _lookup_term(term, lookup):
    """Resolve a contrast-line term to a single entry id via by_headword."""
    m = LINK_RE.match(term)
    if m:
        link_id = (m.group('id') or '').strip()
        if link_id and link_id != 'noentry':
            return link_id
        term = m.group('base') or ''
    plain = strip_furigana_text(term).strip('〜～ 「』』(（)）')
    candidates = [plain]
    if plain.endswith('する') and len(plain) > 2:
        candidates.append(plain[:-2])
    if plain.endswith(('な', 'だ', 'の')) and len(plain) > 2:
        candidates.append(plain[:-1])
    for cand in candidates:
        hits = lookup.get(cand)
        if hits and len(hits) == 1:
            return hits[0].get('id')
    return None


def find_linkable_terms(entry_data, entry_id, lookup, analysis=None):
    """Entry ids of words named on SIMILAR/RELATED/CONTRAST lines with exactly one match."""
    if not lookup:
        return []
    if analysis is None:
        analysis = analyze_notes(entry_data.get('notes', '') or '')
    own_numeric = entry_id.split('_')[0]
    found = []
    for term in analysis.get('contrast_terms', []):
        target = _lookup_term(term, lookup)
        if not target or target == entry_id or target.split('_')[0] == own_numeric:
            continue
        if target not in found:
            found.append(target)
    return found


def score_linkable_unlinked(entry_data, entry_id, lookup, analysis=None):
    """0.0 when cross_references is empty but the notes name 3+ linkable words.

    1 linkable word -> 0.67, 2 -> 0.33, 3 or more -> 0.0. Words already in
    prominent_see_also do not count. 1.0 whenever cross_references exist.
    """
    if entry_data.get('cross_references'):
        return 1.0
    linkable = find_linkable_terms(entry_data, entry_id, lookup, analysis)
    if not linkable:
        return 1.0
    already = {(x or {}).get('target_id') for x in (entry_data.get('prominent_see_also') or [])
               if isinstance(x, dict)}
    missing = [t for t in linkable if t not in already]
    return max(0.0, 1.0 - min(len(missing), 3) / 3.0)


# ---------------------------------------------------------------------------
# Task definitions
# ---------------------------------------------------------------------------

TASK_DIMENSIONS = {
    'notes': [
        ('note_quality', 0.45),
        ('never_modified', 0.20),
        ('verb_transitivity_tag', 0.10),
        ('accuracy_flag', 0.10),
        ('note_bloat', 0.05),
        ('politeness_formality', 0.05),
        ('cross_refs', 0.05),
    ],
    'furigana': [('furigana_coverage', 1.0)],
    'examples': [('example_count', 0.9), ('note_quality', 0.1)],
    'cross_refs': [
        ('cross_refs', 0.5),
        ('linkable_unlinked', 0.3),
        ('transitivity_info', 0.2),
    ],
}

TIER_WEIGHTS = {
    'basic': 3.0,
    'core': 2.0,
    'general': 1.0,
}

PRIORITY_FILES = {
    'notes': 'polishing/priority/notes.txt',
    'furigana': 'polishing/priority/furigana.txt',
    'examples': 'polishing/priority/examples.txt',
    'cross_refs': 'polishing/priority/cross_refs.txt',
}


# ---------------------------------------------------------------------------
# Priority computation
# ---------------------------------------------------------------------------

def compute_dimension_scores(entry_data, templates=None, context=None, entry_id=''):
    """Compute all quality dimension scores for an entry."""
    context = context or {}
    if templates is None:
        templates = context.get('templates')
    lookup = context.get('lookup') or {}
    flags = context.get('flags') or {}
    analysis = analyze_notes(entry_data.get('notes', '') or '') if lookup else None
    return {
        'note_quality': score_note_quality(entry_data, templates),
        'furigana_coverage': score_furigana_coverage(entry_data),
        'example_count': score_example_count(entry_data),
        'cross_refs': score_cross_refs(entry_data),
        'transitivity_info': score_transitivity_info(entry_data),
        'never_modified': score_never_modified(entry_data),
        'verb_transitivity_tag': score_verb_transitivity_tag(entry_data),
        'linkable_unlinked': score_linkable_unlinked(entry_data, entry_id, lookup, analysis),
        'politeness_formality': score_politeness_formality(entry_data),
        'note_bloat': score_note_bloat(entry_data),
        'accuracy_flag': score_accuracy_flag(entry_id, flags),
    }


def compute_task_priority(dimension_scores, tier, task):
    """Compute priority score for a specific task. Higher = more urgent."""
    dimensions = TASK_DIMENSIONS[task]
    quality = sum(dimension_scores[dim] * weight for dim, weight in dimensions)
    tier_weight = TIER_WEIGHTS.get(tier, 1.0)
    return tier_weight * (1.0 - quality)


def compute_all_priorities(entries, templates=None, context=None):
    """Compute priority scores for all entries across all tasks.

    Returns dict: task -> list of (entry_id, priority, tier, dimension_scores)
    sorted by priority descending.
    """
    if context is None:
        context = {'templates': templates}
    tasks = list(TASK_DIMENSIONS.keys())
    results = {task: [] for task in tasks}

    for entry in entries:
        data = entry['data']
        entry_id = entry['id']
        tier = (data.get('metadata', {}) or {}).get('vocabulary_tier', 'general') or 'general'
        dim_scores = compute_dimension_scores(data, templates, context, entry_id)

        for task in tasks:
            priority = compute_task_priority(dim_scores, tier, task)
            if priority > 1e-9:
                results[task].append((entry_id, priority, tier, dim_scores))

    # Sort each task by priority descending
    for task in tasks:
        results[task].sort(key=lambda x: (-x[1], x[0]))

    return results


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_priority_file(task, entries_list, total_entries, base_dir, limit=None):
    """Write a priority file for a task."""
    filepath = os.path.join(base_dir, PRIORITY_FILES[task])
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    items = entries_list[:limit] if limit else entries_list

    with open(filepath, 'w') as f:
        f.write(f"# Generated by prioritize_polishing.py on {date.today().isoformat()}\n")
        f.write(f"# Task: {task}\n")
        f.write(f"# Total entries: {total_entries}\n")
        f.write(f"# Entries with priority > 0: {len(entries_list)}\n")
        for entry_id, _priority, _tier, _scores in items:
            f.write(f"{entry_id}\n")

    return filepath


def print_dry_run(task, entries_list, limit=None):
    """Print priority list to stdout."""
    items = entries_list[:limit] if limit else entries_list
    print(f"# Task: {task}")
    print(f"# Entries with priority > 0: {len(entries_list)}")
    dims = [d for d, _w in TASK_DIMENSIONS[task]]
    for entry_id, priority, tier, scores in items:
        detail = ", ".join(f"{d}: {scores[d]:.2f}" for d in dims)
        print(f"{entry_id}  (score: {priority:.2f}, tier: {tier}, {detail})")
    print()


def print_summary(results, total_entries, base_dir):
    """Print priority statistics."""
    print("POLISHING PRIORITIES")
    print("====================")
    print()

    for task in TASK_DIMENSIONS:
        if task not in results:
            continue
        entries_list = results[task]
        print(f"Task: {task}")
        print(f"  Total entries: {total_entries:,}")
        print(f"  Entries needing work (priority > 0): {len(entries_list):,}")

        if entries_list:
            top_id, top_score, top_tier, top_scores = entries_list[0]
            primary_dim = TASK_DIMENSIONS[task][0][0]
            print(f"  Top priority: {top_id} (score: {top_score:.2f}, tier: {top_tier}, {primary_dim}: {top_scores[primary_dim]:.2f})")

        filepath = os.path.join(base_dir, PRIORITY_FILES[task])
        if os.path.exists(filepath):
            print(f"  Written to: {PRIORITY_FILES[task]}")
        print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Generate polishing priority lists.')
    parser.add_argument('--task', choices=list(TASK_DIMENSIONS.keys()),
                        help='Generate priority list for one task only')
    parser.add_argument('--limit', type=int, metavar='N',
                        help='Limit output to top N entries per task (default: all)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print priorities to stdout instead of writing files')
    parser.add_argument('--summary', action='store_true',
                        help='Show priority statistics without writing files')
    args = parser.parse_args()

    base_dir = BASE_DIR
    entries_dir = os.path.join(base_dir, 'entries')

    context = build_context(base_dir)
    if context['flags']:
        print(f"Outstanding accuracy flags: {len(context['flags']):,}", file=sys.stderr)

    print("Loading entries...", file=sys.stderr)
    entries = load_all_entries(entries_dir)
    total = len(entries)
    print(f"Loaded {total:,} entries.", file=sys.stderr)

    print("Computing priorities...", file=sys.stderr)
    results = compute_all_priorities(entries, context['templates'], context)

    # Filter to one task if requested
    if args.task:
        results = {args.task: results[args.task]}

    if args.summary:
        print_summary(results, total, base_dir)
        return

    if args.dry_run:
        for task in results:
            print_dry_run(task, results[task], args.limit)
        return

    # Write priority files
    for task in results:
        filepath = write_priority_file(task, results[task], total, base_dir, args.limit)
        count = len(results[task])
        if args.limit:
            count = min(count, args.limit)
        print(f"  {task}: {count:,} entries -> {PRIORITY_FILES[task]}", file=sys.stderr)

    print(file=sys.stderr)
    print_summary(results, total, base_dir)


if __name__ == '__main__':
    main()
