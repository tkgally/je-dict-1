#!/usr/bin/env python3
"""Assemble per-category semantic field files into a single semantic_fields.json."""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PARTS_DIR = SCRIPT_DIR / "data" / "semantic_fields"
OUTPUT_FILE = SCRIPT_DIR / "data" / "semantic_fields.json"


def main():
    if not PARTS_DIR.is_dir():
        print(f"Error: {PARTS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    all_fields = []
    category_files = sorted(PARTS_DIR.glob("*.json"))

    if not category_files:
        print(f"Error: no JSON files found in {PARTS_DIR}", file=sys.stderr)
        sys.exit(1)

    for path in category_files:
        with open(path) as f:
            data = json.load(f)
        category_id = data["category"]
        for field in data["fields"]:
            field["category"] = category_id
            all_fields.append(field)

    combined = {
        "version": "1.0",
        "description": "Semantic field definitions for dictionary coverage auditing",
        "fields": all_fields
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)

    total_words = sum(len(f["expected_words"]) for f in all_fields)
    print(f"Assembled {len(all_fields)} fields ({total_words} words) from {len(category_files)} category files")
    print(f"Written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
