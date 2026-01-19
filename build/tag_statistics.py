#!/usr/bin/env python3
"""
Reporting script for dictionary entry tag statistics.

Generates reports on:
- Count of entries by each tag category
- Identification of untagged entries
- Coverage reports for tagging progress

Usage:
    python3 build/tag_statistics.py                    # Basic summary
    python3 build/tag_statistics.py --full-report      # Detailed report
    python3 build/tag_statistics.py --untagged         # List untagged entries
    python3 build/tag_statistics.py --by-tag pos       # Distribution by specific tag
    python3 build/tag_statistics.py --json             # Output as JSON

Options:
    --full-report    Generate comprehensive report
    --untagged       List entries without tags
    --uncategorized  List entries without semantic tags
    --by-tag TAG     Show distribution for a specific tag category
    --json           Output results as JSON
    --limit N        Limit output (for --untagged, default 50)
"""

import json
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class TagStatistics:
    """Statistics about dictionary tags."""
    total_entries: int = 0
    entries_with_tags: int = 0
    entries_with_pos: int = 0
    entries_with_transitivity: int = 0
    entries_with_verb_class: int = 0
    entries_with_formality: int = 0
    entries_with_politeness: int = 0
    entries_with_style: int = 0
    entries_with_domain: int = 0
    entries_with_semantic: int = 0

    # Counters for individual tag values
    pos_counts: Counter = field(default_factory=Counter)
    transitivity_counts: Counter = field(default_factory=Counter)
    verb_class_counts: Counter = field(default_factory=Counter)
    formality_counts: Counter = field(default_factory=Counter)
    politeness_counts: Counter = field(default_factory=Counter)
    style_counts: Counter = field(default_factory=Counter)
    domain_counts: Counter = field(default_factory=Counter)
    semantic_counts: Counter = field(default_factory=Counter)

    # Lists for tracking
    untagged_entries: list = field(default_factory=list)
    entries_without_semantic: list = field(default_factory=list)
    verbs_without_transitivity: list = field(default_factory=list)


def collect_statistics(project_root: Path) -> TagStatistics:
    """Collect tag statistics from all entries."""
    entries_dir = project_root / "entries"
    stats = TagStatistics()

    for file_path in sorted(entries_dir.glob("**/*.json")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        stats.total_entries += 1

        entry_id = entry.get("id", file_path.stem)
        metadata = entry.get("metadata", {})
        tags = metadata.get("tags", {})

        if not tags:
            stats.untagged_entries.append({
                "id": entry_id,
                "headword": entry.get("headword", ""),
                "part_of_speech": entry.get("part_of_speech", ""),
            })
            continue

        stats.entries_with_tags += 1

        # POS tags
        pos_tags = tags.get("pos", [])
        if pos_tags:
            stats.entries_with_pos += 1
            for pos in pos_tags:
                stats.pos_counts[pos] += 1

        # Check for verbs
        has_verb = any(p.startswith("verb-") for p in pos_tags)

        # Transitivity
        transitivity = tags.get("transitivity")
        if transitivity:
            stats.entries_with_transitivity += 1
            stats.transitivity_counts[transitivity] += 1
        elif has_verb:
            stats.verbs_without_transitivity.append({
                "id": entry_id,
                "headword": entry.get("headword", ""),
                "pos": pos_tags,
            })

        # Verb class
        verb_class = tags.get("verb_class")
        if verb_class:
            stats.entries_with_verb_class += 1
            stats.verb_class_counts[verb_class] += 1

        # Formality
        formality = tags.get("formality")
        if formality:
            stats.entries_with_formality += 1
            stats.formality_counts[formality] += 1

        # Politeness
        politeness = tags.get("politeness")
        if politeness:
            stats.entries_with_politeness += 1
            stats.politeness_counts[politeness] += 1

        # Style
        style = tags.get("style", [])
        if style:
            stats.entries_with_style += 1
            for s in style:
                stats.style_counts[s] += 1

        # Domain
        domain = tags.get("domain", [])
        if domain:
            stats.entries_with_domain += 1
            for d in domain:
                stats.domain_counts[d] += 1

        # Semantic
        semantic = tags.get("semantic", [])
        if semantic:
            stats.entries_with_semantic += 1
            for s in semantic:
                stats.semantic_counts[s] += 1
        else:
            # Track entries without semantic tags (for nouns mainly)
            if "noun" in pos_tags or "counter" in pos_tags:
                stats.entries_without_semantic.append({
                    "id": entry_id,
                    "headword": entry.get("headword", ""),
                    "pos": pos_tags,
                })

    return stats


def format_percentage(count: int, total: int) -> str:
    """Format a count as a percentage."""
    if total == 0:
        return "0.0%"
    return f"{count / total * 100:.1f}%"


def print_summary(stats: TagStatistics):
    """Print a summary of tag statistics."""
    print("=" * 60)
    print("DICTIONARY TAG STATISTICS")
    print("=" * 60)

    print(f"\nTotal entries: {stats.total_entries}")
    print(f"Entries with tags: {stats.entries_with_tags} ({format_percentage(stats.entries_with_tags, stats.total_entries)})")
    print(f"Untagged entries: {len(stats.untagged_entries)}")

    print("\n" + "-" * 60)
    print("TAG COVERAGE")
    print("-" * 60)

    coverage = [
        ("pos", stats.entries_with_pos, stats.entries_with_tags),
        ("transitivity", stats.entries_with_transitivity, sum(stats.pos_counts[p] for p in stats.pos_counts if p.startswith("verb-"))),
        ("verb_class", stats.entries_with_verb_class, sum(stats.pos_counts[p] for p in stats.pos_counts if p.startswith("verb-"))),
        ("formality", stats.entries_with_formality, stats.entries_with_tags),
        ("politeness", stats.entries_with_politeness, stats.entries_with_tags),
        ("style", stats.entries_with_style, stats.entries_with_tags),
        ("domain", stats.entries_with_domain, stats.entries_with_tags),
        ("semantic", stats.entries_with_semantic, stats.entries_with_tags),
    ]

    for name, count, total in coverage:
        pct = format_percentage(count, total) if total > 0 else "N/A"
        print(f"  {name:15} {count:5d} / {total:5d} ({pct})")


def print_full_report(stats: TagStatistics):
    """Print a comprehensive tag report."""
    print_summary(stats)

    print("\n" + "-" * 60)
    print("POS TAG DISTRIBUTION")
    print("-" * 60)
    for pos, count in stats.pos_counts.most_common():
        print(f"  {pos:25} {count:5d}")

    if stats.transitivity_counts:
        print("\n" + "-" * 60)
        print("TRANSITIVITY DISTRIBUTION")
        print("-" * 60)
        for trans, count in stats.transitivity_counts.most_common():
            print(f"  {trans:15} {count:5d}")

    if stats.verb_class_counts:
        print("\n" + "-" * 60)
        print("VERB CLASS DISTRIBUTION")
        print("-" * 60)
        for vc, count in stats.verb_class_counts.most_common():
            print(f"  {vc:15} {count:5d}")

    if stats.formality_counts:
        print("\n" + "-" * 60)
        print("FORMALITY DISTRIBUTION")
        print("-" * 60)
        for form, count in stats.formality_counts.most_common():
            print(f"  {form:15} {count:5d}")

    if stats.politeness_counts:
        print("\n" + "-" * 60)
        print("POLITENESS DISTRIBUTION")
        print("-" * 60)
        for pol, count in stats.politeness_counts.most_common():
            print(f"  {pol:15} {count:5d}")

    if stats.style_counts:
        print("\n" + "-" * 60)
        print("STYLE DISTRIBUTION")
        print("-" * 60)
        for style, count in stats.style_counts.most_common():
            print(f"  {style:15} {count:5d}")

    if stats.domain_counts:
        print("\n" + "-" * 60)
        print("DOMAIN DISTRIBUTION")
        print("-" * 60)
        for domain, count in stats.domain_counts.most_common():
            print(f"  {domain:15} {count:5d}")

    if stats.semantic_counts:
        print("\n" + "-" * 60)
        print("SEMANTIC CATEGORY DISTRIBUTION")
        print("-" * 60)
        # Group by parent category
        by_parent = defaultdict(list)
        for sem, count in stats.semantic_counts.most_common():
            parent = sem.split("-")[0] if "-" in sem else sem
            by_parent[parent].append((sem, count))

        for parent in sorted(by_parent.keys()):
            print(f"\n  {parent.upper()}")
            for sem, count in by_parent[parent]:
                print(f"    {sem:25} {count:5d}")


def print_untagged(stats: TagStatistics, limit: int = 50):
    """Print list of untagged entries."""
    print("=" * 60)
    print(f"UNTAGGED ENTRIES ({len(stats.untagged_entries)} total)")
    print("=" * 60)

    for entry in stats.untagged_entries[:limit]:
        print(f"  {entry['id']:30} {entry['headword']:15} [{entry['part_of_speech']}]")

    if len(stats.untagged_entries) > limit:
        print(f"\n  ... and {len(stats.untagged_entries) - limit} more")


def print_uncategorized(stats: TagStatistics, limit: int = 50):
    """Print list of entries without semantic tags."""
    print("=" * 60)
    print(f"ENTRIES WITHOUT SEMANTIC TAGS ({len(stats.entries_without_semantic)} total)")
    print("=" * 60)

    for entry in stats.entries_without_semantic[:limit]:
        pos_str = ", ".join(entry["pos"])
        print(f"  {entry['id']:30} {entry['headword']:15} [{pos_str}]")

    if len(stats.entries_without_semantic) > limit:
        print(f"\n  ... and {len(stats.entries_without_semantic) - limit} more")


def print_by_tag(stats: TagStatistics, tag_name: str):
    """Print distribution for a specific tag category."""
    counters = {
        "pos": stats.pos_counts,
        "transitivity": stats.transitivity_counts,
        "verb_class": stats.verb_class_counts,
        "formality": stats.formality_counts,
        "politeness": stats.politeness_counts,
        "style": stats.style_counts,
        "domain": stats.domain_counts,
        "semantic": stats.semantic_counts,
    }

    if tag_name not in counters:
        print(f"Error: Unknown tag category '{tag_name}'")
        print(f"Valid categories: {', '.join(counters.keys())}")
        return

    counter = counters[tag_name]

    print("=" * 60)
    print(f"{tag_name.upper()} DISTRIBUTION")
    print("=" * 60)

    if not counter:
        print("  No entries with this tag")
        return

    total = sum(counter.values())
    for value, count in counter.most_common():
        pct = format_percentage(count, total)
        print(f"  {value:30} {count:5d} ({pct})")

    print(f"\n  Total: {total}")


def output_json(stats: TagStatistics):
    """Output statistics as JSON."""
    data = {
        "total_entries": stats.total_entries,
        "entries_with_tags": stats.entries_with_tags,
        "coverage": {
            "pos": stats.entries_with_pos,
            "transitivity": stats.entries_with_transitivity,
            "verb_class": stats.entries_with_verb_class,
            "formality": stats.entries_with_formality,
            "politeness": stats.entries_with_politeness,
            "style": stats.entries_with_style,
            "domain": stats.entries_with_domain,
            "semantic": stats.entries_with_semantic,
        },
        "distributions": {
            "pos": dict(stats.pos_counts),
            "transitivity": dict(stats.transitivity_counts),
            "verb_class": dict(stats.verb_class_counts),
            "formality": dict(stats.formality_counts),
            "politeness": dict(stats.politeness_counts),
            "style": dict(stats.style_counts),
            "domain": dict(stats.domain_counts),
            "semantic": dict(stats.semantic_counts),
        },
        "untagged_count": len(stats.untagged_entries),
        "entries_without_semantic_count": len(stats.entries_without_semantic),
        "verbs_without_transitivity_count": len(stats.verbs_without_transitivity),
    }
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate tag statistics report")
    parser.add_argument(
        "--full-report",
        action="store_true",
        help="Generate comprehensive report"
    )
    parser.add_argument(
        "--untagged",
        action="store_true",
        help="List entries without any tags"
    )
    parser.add_argument(
        "--uncategorized",
        action="store_true",
        help="List entries without semantic tags"
    )
    parser.add_argument(
        "--by-tag",
        type=str,
        metavar="TAG",
        help="Show distribution for a specific tag category"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Limit output for list modes (default: 50)"
    )
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Collect statistics
    stats = collect_statistics(project_root)

    # Output based on mode
    if args.json:
        output_json(stats)
    elif args.untagged:
        print_untagged(stats, args.limit)
    elif args.uncategorized:
        print_uncategorized(stats, args.limit)
    elif args.by_tag:
        print_by_tag(stats, args.by_tag)
    elif args.full_report:
        print_full_report(stats)
    else:
        print_summary(stats)

    return 0


if __name__ == "__main__":
    sys.exit(main())
