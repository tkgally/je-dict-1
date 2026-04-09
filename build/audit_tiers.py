#!/usr/bin/env python3
"""Analyze vocabulary tier assignments and detect potential misclassifications."""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
INDEX_FILE = PROJECT_DIR / "entries_index.json"
ENTRIES_DIR = PROJECT_DIR / "entries"

# Domain tags that suggest specialized vocabulary (from metadata.tags.domain)
SPECIALIZED_DOMAINS = {
    "legal", "medical", "academic", "technical", "scientific",
    "financial", "military", "religious", "computing", "linguistics",
    "philosophy", "political",
}

# Semantic tags that suggest foundational vocabulary (from metadata.tags.semantic)
FOUNDATIONAL_SEMANTIC = {
    "daily-life", "greeting", "body", "body-part", "family", "food",
    "time", "number", "direction", "color", "weather",
    "clothing", "house", "school",
}

# POS types that tend to be foundational
FOUNDATIONAL_POS = {"particle", "counter", "interjection"}


def load_index():
    """Load entries from entries_index.json."""
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["entries"]


def load_entry_tags(entry_path):
    """Load semantic and domain tags from an individual entry file."""
    full_path = PROJECT_DIR / entry_path
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            entry = json.load(f)
        tags = entry.get("metadata", {}).get("tags", {})
        return {
            "semantic": tags.get("semantic", []),
            "domain": tags.get("domain", []) if isinstance(tags.get("domain"), list)
                      else [tags["domain"]] if tags.get("domain") else [],
        }
    except (json.JSONDecodeError, IOError, KeyError):
        return {"semantic": [], "domain": []}


def load_all_tags(entries):
    """Load tags for all entries. Returns dict of id -> tags."""
    tags_map = {}
    for entry in entries:
        entry_id = entry["id"]
        tags_map[entry_id] = load_entry_tags(entry["path"])
    return tags_map


def filter_entries(entries, tier=None, pos=None):
    """Filter entries by tier and/or POS."""
    result = entries
    if tier:
        result = [e for e in result if e.get("vocabulary_tier") == tier]
    if pos:
        result = [e for e in result if pos in e.get("pos_tags", [])]
    return result


def group_pos(pos_tags):
    """Categorize a POS tag list into major groups for summary display."""
    groups = defaultdict(int)
    for tag in pos_tags:
        if tag.startswith("verb"):
            groups["Verbs"] += 1
            groups[f"  {tag}"] += 1
        elif tag.startswith("adjective"):
            groups["Adjectives"] += 1
            groups[f"  {tag}"] += 1
        elif tag == "noun":
            groups["Nouns"] += 1
        elif tag == "adverb":
            groups["Adverbs"] += 1
        elif tag == "particle":
            groups["Particles"] += 1
        elif tag == "interjection":
            groups["Interjections"] += 1
        elif tag == "expression":
            groups["Expressions"] += 1
        elif tag == "counter":
            groups["Counters"] += 1
        else:
            groups["Other"] += 1
            groups[f"  {tag}"] += 1
    return groups


def print_summary(entries):
    """Print tier summary statistics."""
    tiers = defaultdict(list)
    for e in entries:
        tier = e.get("vocabulary_tier", "unknown")
        tiers[tier].append(e)

    print("=== Vocabulary Tier Summary ===\n")

    for tier_name in ["basic", "core", "general"]:
        tier_entries = tiers.get(tier_name, [])
        count = len(tier_entries)
        print(f"{tier_name.title()} tier: {count:,} entries")

        # Count POS across all entries in this tier
        pos_counter = Counter()
        for e in tier_entries:
            for tag in e.get("pos_tags", []):
                pos_counter[tag] += 1

        # Group into major categories
        verb_tags = {t: c for t, c in pos_counter.items() if t.startswith("verb")}
        adj_tags = {t: c for t, c in pos_counter.items() if t.startswith("adjective")}
        verb_total = sum(verb_tags.values())
        adj_total = sum(adj_tags.values())
        noun_count = pos_counter.get("noun", 0)
        adverb_count = pos_counter.get("adverb", 0)
        particle_count = pos_counter.get("particle", 0)
        expression_count = pos_counter.get("expression", 0)
        interjection_count = pos_counter.get("interjection", 0)
        counter_count = pos_counter.get("counter", 0)

        known_tags = (set(verb_tags) | set(adj_tags) |
                      {"noun", "adverb", "particle", "expression", "interjection", "counter"})
        other_count = sum(c for t, c in pos_counter.items() if t not in known_tags)

        if count > 0:
            print(f"  Nouns:          {noun_count:>5} ({noun_count/count*100:.1f}%)")
            print(f"  Verbs:          {verb_total:>5} ({verb_total/count*100:.1f}%)")
            for tag in sorted(verb_tags):
                print(f"    {tag}: {verb_tags[tag]:>5}")
            print(f"  Adjectives:     {adj_total:>5} ({adj_total/count*100:.1f}%)")
            for tag in sorted(adj_tags):
                print(f"    {tag}: {adj_tags[tag]:>5}")
            print(f"  Adverbs:        {adverb_count:>5} ({adverb_count/count*100:.1f}%)")
            print(f"  Particles:      {particle_count:>5} ({particle_count/count*100:.1f}%)")
            print(f"  Expressions:    {expression_count:>5} ({expression_count/count*100:.1f}%)")
            print(f"  Interjections:  {interjection_count:>5} ({interjection_count/count*100:.1f}%)")
            print(f"  Counters:       {counter_count:>5} ({counter_count/count*100:.1f}%)")
            if other_count:
                print(f"  Other:          {other_count:>5} ({other_count/count*100:.1f}%)")
        print()


def print_tags(entries, tier=None, tags_map=None):
    """Print semantic tag distribution for entries."""
    if tags_map is None:
        tags_map = load_all_tags(entries)

    tiers = defaultdict(list)
    for e in entries:
        t = e.get("vocabulary_tier", "unknown")
        tiers[t].append(e)

    tier_list = [tier] if tier else ["basic", "core", "general"]

    for tier_name in tier_list:
        tier_entries = tiers.get(tier_name, [])
        if not tier_entries:
            continue

        print(f"=== {tier_name.title()} Tier Semantic Tags ===\n")

        semantic_counter = Counter()
        domain_counter = Counter()
        for e in tier_entries:
            entry_tags = tags_map.get(e["id"], {"semantic": [], "domain": []})
            for tag in entry_tags["semantic"]:
                semantic_counter[tag] += 1
            for tag in entry_tags["domain"]:
                domain_counter[tag] += 1

        print("Semantic tags (top 30):")
        for tag, count in semantic_counter.most_common(30):
            print(f"  {tag}: {count}")

        if domain_counter:
            print(f"\nDomain tags:")
            for tag, count in domain_counter.most_common(20):
                print(f"  {tag}: {count}")
        print()


def find_outliers(entries, tags_map=None):
    """Flag entries that may be misclassified based on heuristics."""
    if tags_map is None:
        tags_map = load_all_tags(entries)

    tiers = defaultdict(list)
    for e in entries:
        tiers[e.get("vocabulary_tier", "unknown")].append(e)

    results = {
        "basic_specialized": [],
        "core_specialized": [],
        "general_undertied": [],
    }

    # Basic tier: flag entries with specialized domain tags
    for e in tiers.get("basic", []):
        entry_tags = tags_map.get(e["id"], {"semantic": [], "domain": []})
        domains = set(entry_tags["domain"])
        specialized_matches = domains & SPECIALIZED_DOMAINS
        if specialized_matches:
            results["basic_specialized"].append({
                "entry": e,
                "reason": f"specialized domain: {', '.join(sorted(specialized_matches))}",
            })

    # Core tier: flag entries with specialized domain tags
    for e in tiers.get("core", []):
        entry_tags = tags_map.get(e["id"], {"semantic": [], "domain": []})
        domains = set(entry_tags["domain"])
        specialized_matches = domains & SPECIALIZED_DOMAINS
        if specialized_matches:
            results["core_specialized"].append({
                "entry": e,
                "reason": f"specialized domain: {', '.join(sorted(specialized_matches))}",
            })

    # General tier: flag entries that seem foundational
    for e in tiers.get("general", []):
        entry_tags = tags_map.get(e["id"], {"semantic": [], "domain": []})
        semantics = set(entry_tags["semantic"])
        pos_tags = set(e.get("pos_tags", []))

        foundational_matches = semantics & FOUNDATIONAL_SEMANTIC
        foundational_pos_matches = pos_tags & FOUNDATIONAL_POS

        reasons = []
        if foundational_matches:
            reasons.append(f"foundational semantic: {', '.join(sorted(foundational_matches))}")
        if foundational_pos_matches:
            reasons.append(f"foundational POS: {', '.join(sorted(foundational_pos_matches))}")

        if reasons:
            results["general_undertied"].append({
                "entry": e,
                "reason": "; ".join(reasons),
            })

    return results


def format_entry_line(entry, reason=None):
    """Format an entry for display."""
    e = entry
    pos = e.get("part_of_speech", "")
    line = f"  ID {e['id']}: {e['headword']} ({e['reading']}) [{pos}] - {e['gloss']}"
    if reason:
        line += f"\n    → {reason}"
    return line


def print_outliers(entries, tags_map=None):
    """Print potential misclassification report."""
    results = find_outliers(entries, tags_map)

    print("=== Potential Tier Outliers ===\n")

    basic = results["basic_specialized"]
    print(f"Basic tier — potentially too specialized ({len(basic)} entries):")
    if basic:
        for item in sorted(basic, key=lambda x: x["entry"]["id"]):
            print(format_entry_line(item["entry"], item["reason"]))
    else:
        print("  (none found)")
    print()

    core = results["core_specialized"]
    print(f"Core tier — potentially too specialized ({len(core)} entries):")
    if core:
        for item in sorted(core, key=lambda x: x["entry"]["id"]):
            print(format_entry_line(item["entry"], item["reason"]))
    else:
        print("  (none found)")
    print()

    general = results["general_undertied"]
    print(f"General tier — potentially under-tiered ({len(general)} entries):")
    if general:
        for item in sorted(general, key=lambda x: x["entry"]["id"])[:100]:
            print(format_entry_line(item["entry"], item["reason"]))
        if len(general) > 100:
            print(f"  ... and {len(general) - 100} more (use --json for full list)")
    else:
        print("  (none found)")
    print()


def print_list(entries):
    """Print detailed entry list."""
    header = f"{'ID':<12} {'Word':<16} {'Reading':<16} {'POS':<24} {'Gloss'}"
    print(header)
    print("-" * len(header))
    for e in sorted(entries, key=lambda x: x["id"]):
        pos = ", ".join(e.get("pos_tags", []))
        gloss = e.get("gloss", "")
        if len(gloss) > 50:
            gloss = gloss[:47] + "..."
        print(f"{e['id']:<12} {e['headword']:<16} {e['reading']:<16} {pos:<24} {gloss}")


def output_json(entries, tier=None, outliers=False, tags=False, tags_map=None):
    """Output results in JSON format."""
    if outliers:
        results = find_outliers(entries, tags_map)
        output = {
            "basic_specialized": [
                {**item["entry"], "reason": item["reason"]}
                for item in results["basic_specialized"]
            ],
            "core_specialized": [
                {**item["entry"], "reason": item["reason"]}
                for item in results["core_specialized"]
            ],
            "general_undertied": [
                {**item["entry"], "reason": item["reason"]}
                for item in results["general_undertied"]
            ],
        }
    elif tags:
        if tags_map is None:
            tags_map = load_all_tags(entries)
        tiers = defaultdict(list)
        for e in entries:
            tiers[e.get("vocabulary_tier", "unknown")].append(e)
        output = {}
        tier_list = [tier] if tier else ["basic", "core", "general"]
        for tier_name in tier_list:
            semantic_counter = Counter()
            domain_counter = Counter()
            for e in tiers.get(tier_name, []):
                entry_tags = tags_map.get(e["id"], {"semantic": [], "domain": []})
                for tag in entry_tags["semantic"]:
                    semantic_counter[tag] += 1
                for tag in entry_tags["domain"]:
                    domain_counter[tag] += 1
            output[tier_name] = {
                "semantic_tags": dict(semantic_counter.most_common()),
                "domain_tags": dict(domain_counter.most_common()),
            }
    else:
        filtered = filter_entries(entries, tier)
        output = {
            "total": len(filtered),
            "entries": [
                {
                    "id": e["id"],
                    "headword": e["headword"],
                    "reading": e["reading"],
                    "pos_tags": e.get("pos_tags", []),
                    "gloss": e.get("gloss", ""),
                    "vocabulary_tier": e.get("vocabulary_tier", ""),
                }
                for e in filtered
            ],
        }

    json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Analyze vocabulary tier assignments and detect potential misclassifications."
    )
    parser.add_argument("--tier", choices=["basic", "core", "general"],
                        help="Filter to a specific tier")
    parser.add_argument("--pos", help="Filter to a specific POS tag")
    parser.add_argument("--tags", action="store_true",
                        help="Show semantic tag distribution per tier")
    parser.add_argument("--outliers", action="store_true",
                        help="Flag statistical outliers")
    parser.add_argument("--json", action="store_true", dest="json_output",
                        help="Output in JSON format")
    parser.add_argument("--list", action="store_true",
                        help="List all entries in the filtered tier")
    parser.add_argument("--ids-only", action="store_true",
                        help="Output only entry IDs")
    args = parser.parse_args()

    entries = load_index()

    # For --tags and --outliers, we need to load tags from entry files
    tags_map = None
    if args.tags or args.outliers:
        subset = filter_entries(entries, args.tier, args.pos)
        if args.outliers:
            # Outliers need all entries (checks across tiers)
            print("Loading tags from entry files...", file=sys.stderr)
            tags_map = load_all_tags(entries)
        else:
            print("Loading tags from entry files...", file=sys.stderr)
            tags_map = load_all_tags(subset)

    # Apply filters
    filtered = filter_entries(entries, args.tier, args.pos)

    if args.json_output:
        output_json(filtered if not args.outliers else entries,
                    tier=args.tier, outliers=args.outliers,
                    tags=args.tags, tags_map=tags_map)
    elif args.ids_only:
        for e in sorted(filtered, key=lambda x: x["id"]):
            print(e["id"])
    elif args.outliers:
        print_outliers(entries, tags_map)
    elif args.tags:
        print_tags(filtered, tier=args.tier, tags_map=tags_map)
    elif args.list:
        print_list(filtered)
    else:
        print_summary(entries)


if __name__ == "__main__":
    main()
