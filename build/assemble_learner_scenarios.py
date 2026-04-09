#!/usr/bin/env python3
"""Assemble per-category learner scenario files into a single learner_scenarios.json."""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PARTS_DIR = SCRIPT_DIR / "data" / "learner_scenarios"
OUTPUT_FILE = SCRIPT_DIR / "data" / "learner_scenarios.json"


def main():
    if not PARTS_DIR.is_dir():
        print(f"Error: {PARTS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    all_scenarios = []
    categories = {}
    category_files = sorted(PARTS_DIR.glob("*.json"))

    if not category_files:
        print(f"Error: no JSON files found in {PARTS_DIR}", file=sys.stderr)
        sys.exit(1)

    for path in category_files:
        with open(path) as f:
            data = json.load(f)
        category_id = data["category"]
        categories[category_id] = data["category_name"]
        for scenario in data["scenarios"]:
            scenario["category"] = category_id
            all_scenarios.append(scenario)

    combined = {
        "version": "1.0",
        "description": "Learner scenario definitions for vocabulary gap analysis",
        "categories": categories,
        "scenarios": all_scenarios
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)

    total_words = sum(len(s["expected_vocabulary"]) for s in all_scenarios)
    unique = set()
    for s in all_scenarios:
        for w in s["expected_vocabulary"]:
            unique.add((w["word"], w["reading"]))
    print(f"Assembled {len(all_scenarios)} scenarios ({total_words} vocab items, {len(unique)} unique) from {len(category_files)} category files")
    print(f"Written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
