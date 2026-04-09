#!/usr/bin/env python3
"""Analyze dictionary coverage for learner scenarios.

Cross-checks scenario vocabulary against the dictionary and identifies
the highest-impact missing words based on cross-scenario frequency.
"""

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

from coverage_utils import load_entry_index, load_candidates, word_in_dictionary

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
SCENARIOS_FILE = SCRIPT_DIR / "data" / "learner_scenarios.json"

PRIORITY_WEIGHTS = {"high": 3, "medium": 2, "low": 1}


def load_scenarios(scenarios_file=SCENARIOS_FILE):
    """Load learner scenario definitions."""
    with open(scenarios_file) as f:
        return json.load(f)


def audit_scenario(scenario, entry_lookup, reading_only, priority_filter=None):
    """Check coverage for a single scenario. Returns dict with results."""
    expected = scenario["expected_vocabulary"]
    if priority_filter:
        expected = [w for w in expected if w["priority"] == priority_filter]

    found = []
    missing = []

    for word_entry in expected:
        word = word_entry["word"]
        reading = word_entry["reading"]

        if word_in_dictionary(word, reading, entry_lookup, reading_only):
            found.append(word_entry)
        else:
            missing.append(word_entry)

    total = len(expected)
    found_count = len(found)
    coverage = (found_count / total * 100) if total > 0 else 100.0

    return {
        "id": scenario["id"],
        "name": scenario["name"],
        "category": scenario.get("category", ""),
        "total": total,
        "found": found_count,
        "coverage_percent": round(coverage, 1),
        "missing": missing
    }


def compute_impact_scores(results):
    """Compute cross-scenario impact for each missing word.

    Returns a list of dicts sorted by impact score (descending).
    """
    # Track missing words across scenarios
    word_info = {}  # key: (word, reading)

    for r in results:
        for w in r["missing"]:
            key = (w["word"], w["reading"])
            if key not in word_info:
                word_info[key] = {
                    "word": w["word"],
                    "reading": w["reading"],
                    "gloss": w["gloss"],
                    "scenarios": [],
                    "priorities": [],
                }
            word_info[key]["scenarios"].append(r["id"])
            word_info[key]["priorities"].append(w["priority"])

    # Compute impact scores
    impact_list = []
    for key, info in word_info.items():
        scenario_count = len(info["scenarios"])
        # Use the highest priority weight across all scenarios
        max_weight = max(PRIORITY_WEIGHTS[p] for p in info["priorities"])
        max_priority = [p for p in info["priorities"]
                        if PRIORITY_WEIGHTS[p] == max_weight][0]
        impact_score = scenario_count * max_weight

        impact_list.append({
            "word": info["word"],
            "reading": info["reading"],
            "gloss": info["gloss"],
            "scenarios": info["scenarios"],
            "scenario_count": scenario_count,
            "max_priority": max_priority,
            "impact_score": impact_score
        })

    impact_list.sort(key=lambda x: (-x["impact_score"], -x["scenario_count"],
                                     x["word"]))
    return impact_list


def print_scenario_report(result, show_missing=True):
    """Print human-readable report for one scenario."""
    print(f"\n--- {result['id']} ({result['name']}) [{result['category']}] ---")
    print(f"Coverage: {result['found']}/{result['total']} ({result['coverage_percent']}%)")

    if show_missing and result["missing"]:
        by_priority = {"high": [], "medium": [], "low": []}
        for w in result["missing"]:
            by_priority[w["priority"]].append(w)

        for priority in ("high", "medium", "low"):
            words = by_priority[priority]
            if words:
                print(f"  Missing ({priority}):")
                for w in words:
                    print(f"    {w['word']} ({w['reading']}) - {w['gloss']}")


def print_top_gaps(impact_list, top_n):
    """Print the top N highest-impact missing words."""
    print(f"\n=== Top {top_n} Highest-Impact Gaps ===")
    print(f"{'Rank':>4}  {'Word':<16} {'Reading':<14} {'Scenarios':>9}  "
          f"{'Impact':>6}  {'Gloss'}")
    for i, item in enumerate(impact_list[:top_n], 1):
        print(f"{i:>4}.  {item['word']:<16} {item['reading']:<14} "
              f"{item['scenario_count']:>9}  {item['impact_score']:>6}  "
              f"{item['gloss']}")


def print_summary(results, impact_list):
    """Print overall summary statistics."""
    total_expected = sum(r["total"] for r in results)
    total_found = sum(r["found"] for r in results)
    overall_pct = (total_found / total_expected * 100) if total_expected > 0 else 100.0

    # Count unique words
    all_words = set()
    missing_words = set()
    for r in results:
        for w in r.get("_all_expected", []):
            all_words.add((w["word"], w["reading"]))
    # We don't have _all_expected, compute from impact_list + found
    unique_missing = len(impact_list)
    in_3_plus = sum(1 for i in impact_list if i["scenario_count"] >= 3)
    in_5_plus = sum(1 for i in impact_list if i["scenario_count"] >= 5)

    print(f"\n=== Summary ===")
    print(f"Total scenarios: {len(results)}")
    print(f"Total vocabulary items: {total_expected:,}")
    print(f"Found in dictionary: {total_found:,} ({overall_pct:.1f}%)")
    print(f"Missing unique words: {unique_missing}")
    print(f"  In 3+ scenarios: {in_3_plus}")
    print(f"  In 5+ scenarios: {in_5_plus}")

    # Categories breakdown
    cat_results = defaultdict(list)
    for r in results:
        cat_results[r["category"]].append(r)

    if len(cat_results) > 1:
        print(f"\nPer-category coverage:")
        for cat in sorted(cat_results):
            cat_total = sum(r["total"] for r in cat_results[cat])
            cat_found = sum(r["found"] for r in cat_results[cat])
            cat_pct = (cat_found / cat_total * 100) if cat_total > 0 else 100.0
            print(f"  {cat}: {cat_found}/{cat_total} ({cat_pct:.1f}%)")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze dictionary coverage for learner scenarios.")
    parser.add_argument("--scenario", metavar="SCENARIO_ID",
                        help="Analyze a single scenario")
    parser.add_argument("--category", help="Analyze all scenarios in a category")
    parser.add_argument("--below", type=float, metavar="N",
                        help="Show only scenarios with coverage below N%%")
    parser.add_argument("--priority", choices=["high", "medium", "low"],
                        help="Filter vocabulary by priority")
    parser.add_argument("--top-gaps", type=int, metavar="N", default=50,
                        help="Show the N highest-impact missing words (default: 50)")
    parser.add_argument("--json", action="store_true", dest="json_output",
                        help="Output in JSON format")
    parser.add_argument("--candidates", action="store_true",
                        help="Output missing words in candidate format")
    parser.add_argument("--add-candidates", action="store_true",
                        help="Directly add missing words as candidates")
    parser.add_argument("--summary", action="store_true",
                        help="Show only summary, not per-scenario details")
    args = parser.parse_args()

    # Load data
    if not SCENARIOS_FILE.exists():
        print(f"Error: {SCENARIOS_FILE} not found. "
              f"Run build/assemble_learner_scenarios.py first.",
              file=sys.stderr)
        sys.exit(1)

    scenario_data = load_scenarios()
    entry_lookup, reading_only = load_entry_index()

    # Filter scenarios
    scenarios = scenario_data["scenarios"]
    if args.scenario:
        scenarios = [s for s in scenarios if s["id"] == args.scenario]
        if not scenarios:
            print(f"Error: scenario '{args.scenario}' not found", file=sys.stderr)
            sys.exit(1)
    elif args.category:
        scenarios = [s for s in scenarios if s.get("category") == args.category]
        if not scenarios:
            print(f"Error: category '{args.category}' not found", file=sys.stderr)
            sys.exit(1)

    # Audit each scenario
    results = []
    for scenario in scenarios:
        result = audit_scenario(scenario, entry_lookup, reading_only,
                                priority_filter=args.priority)
        results.append(result)

    # Filter by coverage threshold
    if args.below is not None:
        results = [r for r in results if r["coverage_percent"] < args.below]

    # Compute impact scores
    impact_list = compute_impact_scores(results)

    # Output
    if args.json_output:
        total_expected = sum(r["total"] for r in results)
        total_found = sum(r["found"] for r in results)
        overall_pct = (total_found / total_expected * 100) if total_expected > 0 else 100.0
        output = {
            "audit_date": str(date.today()),
            "total_scenarios": len(results),
            "total_expected": total_expected,
            "total_found": total_found,
            "coverage_percent": round(overall_pct, 1),
            "scenarios": results,
            "top_gaps": impact_list[:args.top_gaps]
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))

    elif args.candidates:
        for item in impact_list[:args.top_gaps]:
            scenario_note = f"needed in {item['scenario_count']} scenario"
            if item['scenario_count'] > 1:
                scenario_note += "s"
            print(f"\"{item['word']}\" \"{item['reading']}\" "
                  f"\"{item['gloss']} ({scenario_note})\"")

    elif args.add_candidates:
        # Determine which priorities to include
        if args.priority:
            include_priorities = {args.priority}
        else:
            include_priorities = {"high", "medium"}

        candidate_lookup = load_candidates()
        added = 0
        already_existed = 0
        errors = 0

        for item in impact_list[:args.top_gaps]:
            if item["max_priority"] not in include_priorities:
                continue

            # Check if already a candidate
            if (item["word"], item["reading"]) in candidate_lookup:
                print(f"  Already candidate: {item['word']} ({item['reading']})")
                already_existed += 1
                continue

            # Add via manage_candidates.py
            gloss = f"{item['gloss']} (needed in {item['scenario_count']} scenarios)"
            cmd = [
                sys.executable,
                str(SCRIPT_DIR / "manage_candidates.py"),
                "add",
                item["word"],
                item["reading"],
                gloss
            ]
            try:
                result_proc = subprocess.run(cmd, capture_output=True, text=True)
                if result_proc.returncode == 0:
                    if "already exists" in result_proc.stdout.lower():
                        print(f"  Already exists: {item['word']} ({item['reading']})")
                        already_existed += 1
                    else:
                        print(f"  Added: {item['word']} ({item['reading']}) - "
                              f"{item['gloss']}")
                        added += 1
                else:
                    print(f"  Error adding {item['word']}: "
                          f"{result_proc.stderr.strip()}")
                    errors += 1
            except Exception as e:
                print(f"  Error adding {item['word']}: {e}")
                errors += 1

        print(f"\nSummary: Added {added} new candidates, "
              f"{already_existed} already existed, {errors} errors")

    else:
        print("=== Scenario Coverage Report ===")
        for r in sorted(results, key=lambda x: x["coverage_percent"]):
            print_scenario_report(r, show_missing=not args.summary)

        if not args.summary:
            print_top_gaps(impact_list, args.top_gaps)

        print_summary(results, impact_list)


if __name__ == "__main__":
    main()
