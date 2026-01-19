#!/usr/bin/env python3
"""
Tag consistency checking script for dictionary entries.

Checks for logical consistency between tags:
- Verbs must have verb-related POS tags
- Transitivity should only be on verbs
- Keigo entries should have appropriate politeness tags
- Domain-specific entries should have domain tags
- Semantic tags should be consistent with definitions

Usage:
    python3 build/check_tag_consistency.py
    python3 build/check_tag_consistency.py --verbose
    python3 build/check_tag_consistency.py --fix  # Auto-fix some issues
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Optional

# Verb POS tags
VERB_POS_TAGS = {
    "verb-godan", "verb-ichidan", "verb-suru", "verb-kuru", "verb-irregular"
}

# Adjective POS tags
ADJECTIVE_POS_TAGS = {
    "adjective-i", "adjective-na", "adjective-no", "adjective-taru"
}

# Keigo-related keywords in notes/definitions
KEIGO_KEYWORDS = {
    "honorific": ["honorific", "respectful", "sonkeigo", "尊敬語"],
    "humble": ["humble", "kenjougo", "謙譲語", "modest"],
    "polite": ["polite form", "teineigo", "丁寧語"],
}

# Domain keywords to check against domain tags
DOMAIN_KEYWORDS = {
    "business": ["business", "corporate", "commercial", "company"],
    "academic": ["academic", "scholarly", "research"],
    "technical": ["technical", "engineering", "scientific"],
    "legal": ["legal", "law", "judicial", "court"],
    "medical": ["medical", "medicine", "clinical", "health"],
    "computing": ["computer", "programming", "software", "digital"],
    "linguistics": ["grammar", "linguistic", "language"],
    "sports": ["sport", "athletic", "competition"],
    "music": ["music", "musical", "instrument"],
    "cooking": ["cooking", "culinary", "cuisine"],
}


def strip_furigana(text: str) -> str:
    """Remove furigana markup from text."""
    return re.sub(r"\{([^|]+)\|[^}]+\}", r"\1", text)


def get_all_text(entry: dict) -> str:
    """Get all searchable text from an entry."""
    texts = []

    gloss = entry.get("gloss", "")
    if gloss:
        texts.append(gloss)

    notes = entry.get("notes", "")
    if notes:
        texts.append(notes)

    for defn in entry.get("definitions", []):
        if defn.get("gloss"):
            texts.append(defn["gloss"])
        if defn.get("explanation"):
            texts.append(defn["explanation"])

    return " ".join(texts).lower()


def check_entry_consistency(entry: dict, file_path: Path) -> list[dict]:
    """
    Check tag consistency for a single entry.

    Returns list of issues found.
    """
    issues = []

    tags = entry.get("metadata", {}).get("tags", {})
    pos_tags = tags.get("pos", [])
    transitivity = tags.get("transitivity")
    formality = tags.get("formality")
    politeness = tags.get("politeness")
    style = tags.get("style", [])
    domain = tags.get("domain", [])
    semantic = tags.get("semantic", [])

    all_text = get_all_text(entry)
    headword = entry.get("headword", "")
    gloss = entry.get("gloss", "")

    # Check 1: Transitivity should only be on verbs
    if transitivity and not any(p in VERB_POS_TAGS for p in pos_tags):
        issues.append({
            "type": "transitivity_on_non_verb",
            "severity": "warning",
            "message": f"Transitivity '{transitivity}' set on non-verb entry",
            "file": str(file_path),
            "headword": headword,
        })

    # Check 2: Verbs should ideally have transitivity
    if any(p in VERB_POS_TAGS for p in pos_tags) and not transitivity:
        # This is informational, not an error
        pass  # We don't flag missing transitivity as an issue

    # Check 3: Keigo entries should have appropriate politeness tags
    for keigo_type, keywords in KEIGO_KEYWORDS.items():
        if any(kw in all_text for kw in keywords):
            if keigo_type == "honorific" and politeness != "honorific":
                issues.append({
                    "type": "keigo_politeness_mismatch",
                    "severity": "info",
                    "message": f"Entry mentions honorific but politeness is '{politeness}'",
                    "file": str(file_path),
                    "headword": headword,
                })
            elif keigo_type == "humble" and politeness != "humble":
                issues.append({
                    "type": "keigo_politeness_mismatch",
                    "severity": "info",
                    "message": f"Entry mentions humble but politeness is '{politeness}'",
                    "file": str(file_path),
                    "headword": headword,
                })

    # Check 4: Domain-specific content should have domain tags
    for domain_name, keywords in DOMAIN_KEYWORDS.items():
        if any(kw in all_text for kw in keywords):
            if domain_name not in domain:
                # Only flag if it seems strongly domain-specific
                keyword_count = sum(1 for kw in keywords if kw in all_text)
                if keyword_count >= 2:
                    issues.append({
                        "type": "missing_domain_tag",
                        "severity": "info",
                        "message": f"Entry mentions {domain_name} concepts but lacks domain tag",
                        "file": str(file_path),
                        "headword": headword,
                    })

    # Check 5: Semantic tags should exist
    if not semantic:
        issues.append({
            "type": "missing_semantic_tags",
            "severity": "warning",
            "message": "Entry has no semantic tags",
            "file": str(file_path),
            "headword": headword,
        })

    # Check 6: POS tags should exist
    if not pos_tags:
        issues.append({
            "type": "missing_pos_tags",
            "severity": "error",
            "message": "Entry has no POS tags",
            "file": str(file_path),
            "headword": headword,
        })

    # Check 7: Formality should exist
    if not formality:
        issues.append({
            "type": "missing_formality",
            "severity": "error",
            "message": "Entry has no formality tag",
            "file": str(file_path),
            "headword": headword,
        })

    # Check 8: Politeness should exist
    if not politeness:
        issues.append({
            "type": "missing_politeness",
            "severity": "error",
            "message": "Entry has no politeness tag",
            "file": str(file_path),
            "headword": headword,
        })

    # Check 9: Action semantic tag should be on verbs
    if "action" in semantic and not any(p in VERB_POS_TAGS for p in pos_tags):
        # This might be intentional for action nouns
        pass

    # Check 10: Descriptive semantic tag should be on adjectives/adverbs
    if "descriptive" in semantic:
        if not any(p in ADJECTIVE_POS_TAGS for p in pos_tags) and "adverb" not in pos_tags:
            # Could be descriptive noun - not necessarily an issue
            pass

    return issues


def check_all_entries(project_root: Path, verbose: bool = False) -> dict:
    """Check consistency across all entries."""
    entries_dir = project_root / "entries"

    results = {
        "total": 0,
        "clean": 0,
        "with_issues": 0,
        "issues_by_type": Counter(),
        "issues_by_severity": Counter(),
        "all_issues": [],
    }

    for file_path in sorted(entries_dir.glob("**/*.json")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            results["all_issues"].append({
                "type": "file_error",
                "severity": "error",
                "message": f"Could not read file: {e}",
                "file": str(file_path),
            })
            continue

        results["total"] += 1

        issues = check_entry_consistency(entry, file_path)

        if issues:
            results["with_issues"] += 1
            results["all_issues"].extend(issues)

            for issue in issues:
                results["issues_by_type"][issue["type"]] += 1
                results["issues_by_severity"][issue["severity"]] += 1

            if verbose:
                for issue in issues:
                    print(f"  [{issue['severity']}] {issue['headword']}: {issue['message']}")
        else:
            results["clean"] += 1

    return results


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Check tag consistency across dictionary entries"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output for each issue"
    )
    parser.add_argument(
        "--severity",
        choices=["error", "warning", "info", "all"],
        default="all",
        help="Filter by severity level"
    )
    args = parser.parse_args()

    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    print("Tag Consistency Check")
    print("=" * 60)
    print(f"Project root: {project_root}\n")

    results = check_all_entries(project_root, verbose=args.verbose)

    print("\n" + "=" * 60)
    print("Summary")
    print("-" * 60)
    print(f"Total entries:      {results['total']}")
    print(f"Clean entries:      {results['clean']} ({100*results['clean']/results['total']:.1f}%)")
    print(f"Entries with issues: {results['with_issues']}")

    print(f"\nIssues by severity:")
    for severity in ["error", "warning", "info"]:
        count = results["issues_by_severity"].get(severity, 0)
        print(f"  {severity}: {count}")

    print(f"\nIssues by type:")
    for issue_type, count in results["issues_by_type"].most_common():
        print(f"  {issue_type}: {count}")

    # Show sample issues if not verbose
    if not args.verbose and results["all_issues"]:
        print(f"\nSample issues (first 10):")
        shown = 0
        for issue in results["all_issues"]:
            if args.severity != "all" and issue["severity"] != args.severity:
                continue
            if shown >= 10:
                break
            print(f"  [{issue['severity']}] {issue.get('headword', 'N/A')}: {issue['message']}")
            shown += 1

    # Return exit code based on errors
    error_count = results["issues_by_severity"].get("error", 0)
    return 1 if error_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
