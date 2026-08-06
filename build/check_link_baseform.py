#!/usr/bin/env python3
"""Read-only detector for inline links that resolve, but not to their own base form.

Inline links use the markup ``⟦surface→baseform：entry_id⟧`` (see the
``inline-word-links`` skill).  ``build/check_link_targets.py`` catches links
whose ``entry_id`` names no entry at all.  This script catches the other half:
links whose ``entry_id`` names a *real* entry that is **not** the entry for the
link's own base form.  Those render and work on the live site — they simply
take the reader to a different word (``立てる`` linked to ``建てる``,
``性格`` linked to ``正確``), which makes them strictly harder to notice than a
dead target.

Detection: resolve the base form through ``build/word_id_lookup.json``
(``by_headword`` first, then ``by_reading``) and compare the resulting candidate
set against the declared target.  A link is reported only when the base form
resolves somewhere and the declared target is not among the hits.

Three normalizations run before anything is reported, because without them the
signal drowns in indexing artifacts:

* **affix headwords** — ``的`` / ``者`` / ``中`` are stored as ``〜的``,
  ``〜者``, ``〜中``, so a bare-affix base form never matches by string;
* **する-verb bases** — ``確認する`` legitimately links to the noun entry
  ``00158_kakunin``;
* **headword identity** — the declared entry's own headword (or reading, or one
  alternative of a ``優しい／易しい`` style headword) *is* the base form, so the
  link is correct and only the lookup table indexes it differently.

A fourth acceptance path is the curated allowlist in
``build/data/link_baseform_allowlist.json``: ``(base form, entry id)`` pairs that
are the **same word** under a different spelling or a kana headword
(``頃``/``〜ころ``, ``羽``/``羽根``, ``いい``/``良い``).  String comparison cannot
see that they are one word, and no normalization generalizes them safely, so each
pair carries a written reason and was verified in context before being listed.
The allowlist is only for same-word pairs; a link that points at a *different*
word gets repaired, never allowlisted.

The script never modifies entries.

Usage:
    python3 build/check_link_baseform.py                 # human-readable report
    python3 build/check_link_baseform.py --summary        # counts only
    python3 build/check_link_baseform.py --json           # machine-readable queue
    python3 build/check_link_baseform.py --count          # single integer (ratchet)
    python3 build/check_link_baseform.py --gate           # CI ratchet: exit 1 over gate_max
    python3 build/check_link_baseform.py --no-allowlist   # raw queue, allowlist ignored
    python3 build/check_link_baseform.py --by-base        # group by base form
    python3 build/check_link_baseform.py --resolvable     # only unique-proposal links
    python3 build/check_link_baseform.py --ambiguous      # only links needing judgment
    python3 build/check_link_baseform.py --range 5000 5999
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
ALLOWLIST_PATH = ROOT / "build" / "data" / "link_baseform_allowlist.json"

NOENTRY = "noentry"

LINK_BLOCK_PATTERN = re.compile(r"⟦([^⟧]+)⟧")
LINK_INFO_PATTERN = re.compile(r"^(.+?)→(.+?)：(.+)$")
FURIGANA_PATTERN = re.compile(r"\{([^|{}]+)\|([^|{}]+)\}")

#: Headwords may list alternatives (``優しい／易しい``); any one of them counts.
HEADWORD_SPLIT_PATTERN = re.compile(r"[／/、,]")

#: Affix markers stripped before comparing a base form with a headword.
AFFIX_CHARS = "〜～"


def strip_furigana(text: str) -> str:
    """``{漢字|かんじ}語`` -> ``漢字語`` (keep the kanji, drop the readings)."""
    return FURIGANA_PATTERN.sub(lambda m: m.group(1), text)


def furigana_reading(text: str) -> str:
    """``{漢字|かんじ}語`` -> ``かんじ語`` (keep the readings)."""
    return FURIGANA_PATTERN.sub(lambda m: m.group(2), text)


def normalize(text: str) -> str:
    """Drop affix markers and whitespace so ``〜ころ`` compares equal to ``ころ``."""
    return "".join(c for c in text if c not in AFFIX_CHARS).strip()


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


def resolve(base: str, by_headword: dict, by_reading: dict) -> list[dict]:
    """Candidate entries for a base form, headword table first, then readings."""
    base_kanji = strip_furigana(base)
    base_kana = furigana_reading(base)
    for table, key in (
        (by_headword, base_kanji),
        (by_reading, base_kanji),
        (by_headword, base_kana),
        (by_reading, base_kana),
    ):
        if not key:
            continue
        hits = table.get(key)
        if hits:
            return hits
    return []


def load_allowlist() -> tuple[dict[tuple[str, str], dict], int]:
    """Return ``{(normalized base, target id): pair}`` and the gate threshold."""
    if not ALLOWLIST_PATH.exists():
        return {}, 0
    data = json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8"))
    pairs = {
        (normalize(strip_furigana(p["base"])), p["target"]): p
        for p in data.get("pairs", [])
    }
    return pairs, int(data.get("gate_max", 0))


def accepted_by_normalization(
    base: str, target: str, forms: dict, by_headword: dict, by_reading: dict
) -> str | None:
    """Return the normalization that vindicates this link, or ``None``.

    ``forms`` maps entry id -> ``(headword, reading)`` for every real entry.
    """
    base_kanji = normalize(strip_furigana(base))
    base_kana = normalize(furigana_reading(base))

    # 1. The declared entry's own headword/reading IS the base form; only the
    #    lookup table indexes it under a different key (〜ころ, 優しい／易しい).
    headword, reading = forms.get(target, ("", ""))
    variants = {normalize(v) for v in HEADWORD_SPLIT_PATTERN.split(strip_furigana(headword))}
    variants.add(normalize(reading))
    variants.discard("")
    if base_kanji in variants or base_kana in variants:
        return "headword-identity"

    # 2. Bare affix base form against an 〜affix headword (的 -> 〜的).
    for marker in AFFIX_CHARS:
        for key in (marker + base_kanji, base_kanji + marker):
            for table in (by_headword, by_reading):
                if any(hit["id"] == target for hit in table.get(key, [])):
                    return "affix-headword"

    # 3. する-verb base form pointing at its noun entry (確認する -> 00158_kakunin).
    if base_kanji.endswith("する"):
        stem = base_kanji[:-2]
        for table in (by_headword, by_reading):
            if any(hit["id"] == target for hit in table.get(stem, [])):
                return "suru-noun"

    return None


def scan(
    id_range: tuple[int, int] | None = None, use_allowlist: bool = True
) -> tuple[list[dict], dict]:
    by_headword, by_reading = load_lookup()
    allowlist = load_allowlist()[0] if use_allowlist else {}

    paths = sorted(ENTRIES_DIR.glob("*/*.json"))
    entries: dict[str, dict] = {}
    forms: dict[str, tuple[str, str]] = {}
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:  # pragma: no cover
            print(f"warning: could not read {path}: {exc}", file=sys.stderr)
            continue
        entries[path.stem] = data
        forms[path.stem] = (data.get("headword", ""), data.get("reading", ""))

    findings: list[dict] = []
    stats = {
        "links": 0,
        "noentry": 0,
        "dead-target": 0,
        "no-lookup-hit": 0,
        "agree": 0,
        "headword-identity": 0,
        "affix-headword": 0,
        "suru-noun": 0,
        "allowlist": 0,
        "disagree": 0,
    }

    for path in paths:
        stem = path.stem
        data = entries.get(stem)
        if data is None:
            continue
        entry_id = data.get("id") or stem.split("_")[0]
        if id_range and not (id_range[0] <= int(entry_id) <= id_range[1]):
            continue

        for field_path, text in iter_text_fields(data):
            if "⟦" not in text:
                continue
            for block in LINK_BLOCK_PATTERN.finditer(text):
                info = LINK_INFO_PATTERN.match(block.group(1))
                if not info:
                    continue
                surface, base, target = (g.strip() for g in info.groups())
                stats["links"] += 1
                if target == NOENTRY:
                    stats["noentry"] += 1
                    continue
                if target not in forms:
                    # check_link_targets.py owns this population.
                    stats["dead-target"] += 1
                    continue

                candidates = resolve(base, by_headword, by_reading)
                if not candidates:
                    stats["no-lookup-hit"] += 1
                    continue
                if any(hit["id"] == target for hit in candidates):
                    stats["agree"] += 1
                    continue

                why = accepted_by_normalization(
                    base, target, forms, by_headword, by_reading
                )
                if why:
                    stats[why] += 1
                    continue

                if (normalize(strip_furigana(base)), target) in allowlist:
                    stats["allowlist"] += 1
                    continue

                stats["disagree"] += 1
                target_headword, target_reading = forms[target]
                findings.append(
                    {
                        "entry_id": entry_id,
                        "file": str(path.relative_to(ROOT)),
                        "field": field_path,
                        "link": block.group(0),
                        "surface": surface,
                        "baseform": base,
                        "declared_target": target,
                        "declared_headword": strip_furigana(target_headword),
                        "declared_reading": target_reading,
                        "proposal": candidates[0]["id"] if len(candidates) == 1 else None,
                        "candidates": [
                            {
                                "id": hit["id"],
                                "headword": hit.get("headword", ""),
                                "reading": hit.get("reading", ""),
                                "gloss": hit.get("gloss", ""),
                            }
                            for hit in candidates
                        ],
                        "status": "resolvable" if len(candidates) == 1 else "ambiguous",
                    }
                )

    return findings, stats


def report(findings: list[dict], by_base: bool) -> None:
    if not findings:
        print("No base-form disagreements found.")
        return

    if by_base:
        groups: dict[tuple[str, str], list[dict]] = {}
        for f in findings:
            groups.setdefault((f["baseform"], f["declared_target"]), []).append(f)
        for (base, target), items in sorted(
            groups.items(), key=lambda kv: (-len(kv[1]), kv[0])
        ):
            first = items[0]
            proposals = sorted({i["proposal"] or "?" for i in items})
            print(
                f"{len(items):>4}  {base:<12} -> {target:<20} "
                f"[{first['declared_headword']} / {first['declared_reading']}]"
                f"  proposal: {', '.join(proposals)}"
            )
            print("        entries: " + ", ".join(sorted({i["entry_id"] for i in items})))
        return

    current = None
    for f in findings:
        if f["entry_id"] != current:
            current = f["entry_id"]
            print(f"\n{f['entry_id']}  ({f['file']})")
        print(f"  [{f['status']:<10}] {f['field']}")
        print(f"      {f['link']}")
        print(
            f"      base {f['baseform']} -> declared {f['declared_target']} "
            f"= {f['declared_headword']} ({f['declared_reading']})"
        )
        for c in f["candidates"]:
            print(f"      lookup: {c['id']}  {c['headword']} ({c['reading']})  {c['gloss']}")


def summarize(findings: list[dict], stats: dict) -> None:
    entries = {f["entry_id"] for f in findings}
    resolvable = sum(1 for f in findings if f["status"] == "resolvable")
    print("Inline links whose target is not their own base form")
    print(f"  links scanned:       {stats['links']}")
    print(f"  noentry:             {stats['noentry']}")
    print(f"  dead target:         {stats['dead-target']}  (check_link_targets.py)")
    print(f"  no lookup hit:       {stats['no-lookup-hit']}")
    print(f"  agree:               {stats['agree']}")
    print(f"  accepted (headword): {stats['headword-identity']}")
    print(f"  accepted (affix):    {stats['affix-headword']}")
    print(f"  accepted (suru):     {stats['suru-noun']}")
    print(f"  accepted (allowlist):{stats['allowlist']}")
    print(f"  DISAGREE:            {len(findings)}")
    print(f"    entries affected:  {len(entries)}")
    print(f"    resolvable (1 hit):{resolvable}")
    print(f"    ambiguous (>1 hit):{len(findings) - resolvable}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--summary", action="store_true", help="counts only")
    parser.add_argument("--count", action="store_true", help="print the link count only")
    parser.add_argument(
        "--gate",
        action="store_true",
        help="CI ratchet: exit 1 if the queue exceeds gate_max in the allowlist file",
    )
    parser.add_argument(
        "--no-allowlist",
        action="store_true",
        help="ignore build/data/link_baseform_allowlist.json (raw queue)",
    )
    parser.add_argument("--by-base", action="store_true", help="group by base form")
    parser.add_argument("--resolvable", action="store_true", help="only unique-proposal links")
    parser.add_argument("--ambiguous", action="store_true", help="only links needing judgment")
    parser.add_argument("--entry-ids", action="store_true", help="affected entry IDs only")
    parser.add_argument(
        "--range", nargs=2, type=int, metavar=("START", "END"), help="limit to an ID range"
    )
    args = parser.parse_args()

    findings, stats = scan(
        tuple(args.range) if args.range else None, use_allowlist=not args.no_allowlist
    )
    if args.resolvable:
        findings = [f for f in findings if f["status"] == "resolvable"]
    if args.ambiguous:
        findings = [f for f in findings if f["status"] != "resolvable"]

    if args.gate:
        gate_max = load_allowlist()[1]
        if len(findings) > gate_max:
            report(findings, by_base=True)
            print(
                f"\nFAIL: {len(findings)} inline link(s) resolve to an entry that is not "
                f"their own base form (allowed: {gate_max}).\n"
                "Repair the link's entry_id, or — only if the base form and the declared "
                "entry are the SAME word under a different spelling — add the pair with a "
                "reason to build/data/link_baseform_allowlist.json."
            )
            return 1
        print(f"OK: base-form disagreements {len(findings)} <= {gate_max}")
        return 0

    if args.count:
        print(len(findings))
    elif args.entry_ids:
        for entry_id in sorted({f["entry_id"] for f in findings}):
            print(entry_id)
    elif args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    elif args.summary:
        summarize(findings, stats)
    else:
        report(findings, args.by_base)
        print()
        summarize(findings, stats)

    return 0


if __name__ == "__main__":
    sys.exit(main())
