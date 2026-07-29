#!/usr/bin/env python3
"""Read-only detector for inline word links whose target entry ID does not exist.

Inline links use the markup ``⟦surface→baseform：entry_id⟧`` (see the
``inline-word-links`` skill).  ``build/html_utils.py:process_word_links`` drops
the link *silently* when ``entry_id`` is not a real entry, so a dead target is
invisible on the live site and invisible in CI.  This script sweeps every entry
file, reports each link whose ``entry_id`` is neither ``noentry`` nor an
existing entry basename, and proposes a replacement by re-resolving the link's
baseform (and, failing that, its surface form) through
``build/word_id_lookup.json``.

The script never modifies entries.

Usage:
    python3 build/check_link_targets.py                 # human-readable report
    python3 build/check_link_targets.py --summary        # counts only
    python3 build/check_link_targets.py --json           # machine-readable queue
    python3 build/check_link_targets.py --count          # single integer (for the ratchet)
    python3 build/check_link_targets.py --by-target      # group by dead target ID
    python3 build/check_link_targets.py --resolvable     # only links with a unique proposal
    python3 build/check_link_targets.py --ambiguous      # only links needing curator judgment
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "entries"
LOOKUP_PATH = ROOT / "build" / "word_id_lookup.json"

NOENTRY = "noentry"

LINK_BLOCK_PATTERN = re.compile(r"⟦([^⟧]+)⟧")
LINK_INFO_PATTERN = re.compile(r"^(.+?)→(.+?)：(.+)$")
FURIGANA_PATTERN = re.compile(r"\{([^|{}]+)\|([^|{}]+)\}")


def strip_furigana(text: str) -> str:
    """``{漢字|かんじ}語`` -> ``漢字語`` (keep the kanji, drop the readings)."""
    return FURIGANA_PATTERN.sub(lambda m: m.group(1), text)


def furigana_reading(text: str) -> str:
    """``{漢字|かんじ}語`` -> ``かんじ語`` (keep the readings)."""
    return FURIGANA_PATTERN.sub(lambda m: m.group(2), text)


def existing_entry_ids() -> set[str]:
    """Every entry basename, e.g. ``00347_de``."""
    return {p.stem for p in ENTRIES_DIR.glob("*/*.json")}


def load_lookup() -> tuple[dict, dict]:
    if not LOOKUP_PATH.exists():
        print(
            f"error: {LOOKUP_PATH.relative_to(ROOT)} not found — run "
            "`make word-lookup` first.",
            file=sys.stderr,
        )
        sys.exit(2)
    data = json.loads(LOOKUP_PATH.read_text(encoding="utf-8"))
    return data.get("by_headword", {}), data.get("by_reading", {})


def iter_text_fields(obj, path: str = ""):
    """Yield ``(json_path, string)`` for every string in a nested structure."""
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for key, value in obj.items():
            yield from iter_text_fields(value, f"{path}.{key}" if path else key)
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            yield from iter_text_fields(value, f"{path}[{index}]")


def propose(baseform: str, surface: str, by_headword: dict, by_reading: dict) -> list[dict]:
    """Candidate replacement entries for a dead link, best key first.

    Tries, in order: baseform as headword (kanji stripped of furigana),
    baseform as reading, then the same two for the surface form.  Returns the
    first non-empty hit list, annotated with the key that matched.
    """
    base_kanji = strip_furigana(baseform)
    base_kana = furigana_reading(baseform)
    surf_kanji = strip_furigana(surface)
    surf_kana = furigana_reading(surface)

    attempts = [
        ("baseform-headword", by_headword, base_kanji),
        ("baseform-reading", by_reading, base_kana),
        ("baseform-reading", by_reading, base_kanji),
        ("baseform-headword", by_headword, base_kana),
        ("surface-headword", by_headword, surf_kanji),
        ("surface-reading", by_reading, surf_kana),
    ]
    seen_keys = set()
    for how, table, key in attempts:
        if not key or (how, key) in seen_keys:
            continue
        seen_keys.add((how, key))
        hits = table.get(key)
        if hits:
            return [dict(hit, matched_by=how, matched_key=key) for hit in hits]
    return []


def scan() -> list[dict]:
    valid_ids = existing_entry_ids()
    by_headword, by_reading = load_lookup()
    findings: list[dict] = []

    for path in sorted(ENTRIES_DIR.glob("*/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:  # pragma: no cover
            print(f"warning: could not read {path}: {exc}", file=sys.stderr)
            continue

        entry_id = data.get("id") or path.stem.split("_")[0]
        for field_path, text in iter_text_fields(data):
            if "⟦" not in text:
                continue
            for block in LINK_BLOCK_PATTERN.finditer(text):
                info = LINK_INFO_PATTERN.match(block.group(1))
                if not info:
                    continue
                surface, baseform, target = (g.strip() for g in info.groups())
                if target == NOENTRY or target in valid_ids:
                    continue

                candidates = propose(baseform, surface, by_headword, by_reading)
                findings.append(
                    {
                        "entry_id": entry_id,
                        "file": str(path.relative_to(ROOT)),
                        "field": field_path,
                        "link": block.group(0),
                        "surface": surface,
                        "baseform": baseform,
                        "dead_target": target,
                        "proposal": candidates[0]["id"] if len(candidates) == 1 else None,
                        "candidates": candidates,
                        "status": (
                            "resolvable"
                            if len(candidates) == 1
                            else "ambiguous"
                            if candidates
                            else "unresolvable"
                        ),
                    }
                )

    return findings


def report(findings: list[dict], by_target: bool) -> None:
    if not findings:
        print("No dead inline-link targets found.")
        return

    if by_target:
        groups: dict[str, list[dict]] = {}
        for f in findings:
            groups.setdefault(f["dead_target"], []).append(f)
        for target, items in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            first = items[0]
            proposals = sorted({i["proposal"] or "?" for i in items})
            print(
                f"{target:<24} {len(items):>4} link(s)  "
                f"base={first['baseform']}  -> {', '.join(proposals)}"
            )
            print(
                "     entries: "
                + ", ".join(sorted({i["entry_id"] for i in items}))
            )
        return

    current = None
    for f in findings:
        if f["entry_id"] != current:
            current = f["entry_id"]
            print(f"\n{f['entry_id']}  ({f['file']})")
        detail = f["proposal"] or ", ".join(c["id"] for c in f["candidates"]) or "no match"
        print(f"  [{f['status']:<12}] {f['field']}")
        print(f"      {f['link']}")
        print(f"      dead: {f['dead_target']}  ->  {detail}")


def summarize(findings: list[dict]) -> None:
    entries = {f["entry_id"] for f in findings}
    targets = {f["dead_target"] for f in findings}
    counts = {"resolvable": 0, "ambiguous": 0, "unresolvable": 0}
    for f in findings:
        counts[f["status"]] += 1
    print("Dead inline-link targets")
    print(f"  links:              {len(findings)}")
    print(f"  entries affected:   {len(entries)}")
    print(f"  distinct dead IDs:  {len(targets)}")
    print(f"  resolvable (1 hit): {counts['resolvable']}")
    print(f"  ambiguous (>1 hit): {counts['ambiguous']}")
    print(f"  unresolvable:       {counts['unresolvable']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--summary", action="store_true", help="counts only")
    parser.add_argument("--count", action="store_true", help="print the link count only")
    parser.add_argument("--by-target", action="store_true", help="group by dead target ID")
    parser.add_argument("--resolvable", action="store_true", help="only unique-proposal links")
    parser.add_argument("--ambiguous", action="store_true", help="only links needing judgment")
    parser.add_argument("--entry-ids", action="store_true", help="affected entry IDs only")
    args = parser.parse_args()

    findings = scan()
    if args.resolvable:
        findings = [f for f in findings if f["status"] == "resolvable"]
    if args.ambiguous:
        findings = [f for f in findings if f["status"] != "resolvable"]

    if args.count:
        print(len(findings))
    elif args.entry_ids:
        for entry_id in sorted({f["entry_id"] for f in findings}):
            print(entry_id)
    elif args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    elif args.summary:
        summarize(findings)
    else:
        report(findings, args.by_target)
        print()
        summarize(findings)

    return 0


if __name__ == "__main__":
    sys.exit(main())
