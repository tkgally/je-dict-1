#!/usr/bin/env python3
"""Read-only detector for links that were never judged against a newer homograph.

An inline link ``⟦surface→base：entry_id⟧`` (or a ``cross_references`` /
``prominent_see_also`` item) is chosen among the entries that existed when the
containing entry was last edited.  When a *new* entry with the same base form
(and, for kanji bases, the same reading) is created later, the old link was
never weighed against it — the target may be the wrong homograph, or simply the
less specific of two now-available entries.  This script lists exactly those
links: the base form resolves to more than one entry, and at least one
competitor's ``metadata.created`` is later than the containing entry's
``metadata.modified``.

Resolution mirrors ``check_link_baseform.py`` / ``check_stale_noentry.py``:
``by_headword`` for bases with kanji (reading agreement is required, using the
surface's furigana), ``by_reading`` for kana bases; ``〜`` affix markers are
ignored on both sides.  Cross-references are resolved by stripped headword +
reading.

The script never modifies entries and always exits 0 (it is a queue generator).

Usage:
    python3 build/check_link_newcomers.py                 # report + summary
    python3 build/check_link_newcomers.py --summary        # counts only
    python3 build/check_link_newcomers.py --json           # machine-readable queue
    python3 build/check_link_newcomers.py --range 7000 7999
    python3 build/check_link_newcomers.py --since 2026-08-01   # competitors created since
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "entries"
LOOKUP_PATH = ROOT / "build" / "word_id_lookup.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_stale_noentry import reading_agrees, to_hiragana  # noqa: E402

NOENTRY = "noentry"
LINK_BLOCK_PATTERN = re.compile(r"⟦([^⟧]+)⟧")
LINK_INFO_PATTERN = re.compile(r"^(.+?)→(.+?)：(.+)$")
FURIGANA_PATTERN = re.compile(r"\{([^|{}]+)\|([^|{}]+)\}")
KANJI_PATTERN = re.compile(r"[一-鿿㐀-䶿豈-﫿々〆]")
TILDES = "〜～"


def strip_furigana(text: str) -> str:
    return FURIGANA_PATTERN.sub(lambda m: m.group(1), text)


def normalize(text: str) -> str:
    return "".join(c for c in text if c not in TILDES).strip()


def iter_text_fields(obj, path: str = ""):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for key, value in obj.items():
            yield from iter_text_fields(value, f"{path}.{key}" if path else key)
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            yield from iter_text_fields(value, f"{path}[{index}]")


def load_lookup(path: Path = LOOKUP_PATH) -> tuple[dict, dict]:
    if not path.exists():
        print(f"error: {path} not found — run `make word-lookup` first.", file=sys.stderr)
        return {}, {}
    data = json.loads(path.read_text(encoding="utf-8"))
    by_headword: dict[str, list] = defaultdict(list)
    by_reading: dict[str, list] = defaultdict(list)
    for key, hits in data.get("by_headword", {}).items():
        by_headword[normalize(key)].extend(hits)
    for key, hits in data.get("by_reading", {}).items():
        by_reading[normalize(key)].extend(hits)
    return by_headword, by_reading


def load_entries(entries_dir: Path = ENTRIES_DIR) -> dict[str, tuple[Path, dict]]:
    entries = {}
    for path in sorted(entries_dir.glob("*/*.json")):
        try:
            entries[path.stem] = (path, json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"warning: could not read {path}: {exc}", file=sys.stderr)
    return entries


def candidates_for_link(surface: str, base: str, by_headword: dict, by_reading: dict) -> list[dict]:
    """Entries the base form could name (kanji: headword + reading agreement; kana: reading)."""
    key = normalize(strip_furigana(base))
    if not key:
        return []
    if KANJI_PATTERN.search(key):
        hits = by_headword.get(key, [])
        return [h for h in hits if reading_agrees(surface, h.get("reading"))]
    hits = by_reading.get(to_hiragana(key), [])
    return list(hits)


def scan(id_range=None, since: str | None = None, entries_dir: Path = ENTRIES_DIR,
         lookup_path: Path = LOOKUP_PATH) -> tuple[list[dict], dict]:
    by_headword, by_reading = load_lookup(lookup_path)
    entries = load_entries(entries_dir)
    created = {stem: ((e.get("metadata") or {}).get("created") or "") for stem, (_p, e) in entries.items()}
    headword_of = {stem: strip_furigana(e.get("headword") or "") for stem, (_p, e) in entries.items()}
    reading_of = {stem: e.get("reading") or "" for stem, (_p, e) in entries.items()}
    gloss_of = {stem: e.get("gloss") or "" for stem, (_p, e) in entries.items()}
    by_hw_reading: dict[tuple[str, str], list[str]] = defaultdict(list)
    for stem in entries:
        by_hw_reading[(normalize(headword_of[stem]), to_hiragana(reading_of[stem]))].append(stem)

    findings: list[dict] = []
    stats = {"links": 0, "noentry": 0, "dead-target": 0, "single-candidate": 0,
             "multi-old": 0, "multi-newcomer": 0, "xrefs": 0, "xref-newcomer": 0}

    def newer_competitors(ids: list[str], target: str, modified: str) -> list[dict]:
        out = []
        for cid in ids:
            if cid == target:
                continue
            c_created = created.get(cid, "")
            if not c_created or not modified or c_created <= modified:
                continue
            if since and c_created[:10] < since:
                continue
            out.append({"id": cid, "headword": headword_of.get(cid, ""),
                        "reading": reading_of.get(cid, ""), "gloss": gloss_of.get(cid, ""),
                        "created": c_created})
        return out

    for stem, (path, entry) in entries.items():
        num = int(stem[:5]) if stem[:5].isdigit() else None
        if num is None or (id_range and not (id_range[0] <= num <= id_range[1])):
            continue
        modified = (entry.get("metadata") or {}).get("modified") or ""
        entry_id = entry.get("id") or stem
        for field_path, text in iter_text_fields(entry):
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
                if target not in entries:
                    stats["dead-target"] += 1
                    continue
                # Particles and other function words are fixed by the linker's
                # table (は is 00079_ha whatever 派 or 歯 exist), so a new kanji
                # homograph of a one- or two-kana function word is not a real
                # ambiguity for the link.
                t_pos = set(((entries[target][1].get("metadata") or {}).get("tags") or {}).get("pos") or [])
                base_key = normalize(strip_furigana(base))
                if (not KANJI_PATTERN.search(base_key) and len(base_key) <= 2
                        and t_pos & {"particle", "auxiliary", "conjunction"}):
                    stats["function-word"] = stats.get("function-word", 0) + 1
                    continue
                cands = candidates_for_link(surface, base, by_headword, by_reading)
                ids = [c["id"] for c in cands]
                if len(ids) <= 1:
                    stats["single-candidate"] += 1
                    continue
                newer = newer_competitors(ids, target, modified)
                if not newer:
                    stats["multi-old"] += 1
                    continue
                stats["multi-newcomer"] += 1
                findings.append({
                    "kind": "inline-link",
                    "entry_id": entry_id,
                    "file": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                    "field": field_path,
                    "link": block.group(0),
                    "surface": surface,
                    "baseform": base,
                    "target": target,
                    "target_headword": headword_of.get(target, ""),
                    "entry_modified": modified,
                    "competitors": newer,
                    "all_candidates": ids,
                })
        for key in ("cross_references", "prominent_see_also"):
            for index, ref in enumerate(entry.get(key) or []):
                if not isinstance(ref, dict):
                    continue
                target = ref.get("target_id") or ""
                if not target or target not in entries:
                    continue
                stats["xrefs"] += 1
                hw = normalize(strip_furigana(ref.get("headword") or ""))
                rd = to_hiragana(ref.get("reading") or "")
                if not hw or not rd:
                    continue
                ids = by_hw_reading.get((hw, rd), [])
                if len(ids) <= 1:
                    continue
                newer = newer_competitors(ids, target, modified)
                if not newer:
                    continue
                stats["xref-newcomer"] += 1
                findings.append({
                    "kind": key,
                    "entry_id": entry_id,
                    "file": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
                    "field": f"{key}[{index}]",
                    "link": f"{ref.get('headword', '')} ({ref.get('reading', '')}) -> {target}",
                    "surface": ref.get("headword", ""),
                    "baseform": hw,
                    "target": target,
                    "target_headword": headword_of.get(target, ""),
                    "entry_modified": modified,
                    "competitors": newer,
                    "all_candidates": ids,
                })
    findings.sort(key=lambda f: (f["entry_id"], f["field"]))
    return findings, stats


def report(findings: list[dict], limit: int) -> None:
    if not findings:
        print("No links with newer homograph competitors found.")
        return
    current = None
    for f in findings[:limit]:
        if f["entry_id"] != current:
            current = f["entry_id"]
            print(f"\n{f['entry_id']}  ({f['file']})  modified {f['entry_modified']}")
        print(f"  [{f['kind']}] {f['field']}")
        print(f"      {f['link']}  -> {f['target']} ({f['target_headword']})")
        for c in f["competitors"]:
            print(f"      newer: {c['id']}  {c['headword']} ({c['reading']})  {c['gloss']}  created {c['created']}")
    if len(findings) > limit:
        print(f"\n... and {len(findings) - limit} more (use --json for all)")


def summarize(findings: list[dict], stats: dict) -> None:
    entries = {f["entry_id"] for f in findings}
    print("Links never judged against a newer homograph")
    print(f"  inline links scanned:   {stats['links']}")
    print(f"  noentry:                {stats['noentry']}")
    print(f"  dead target:            {stats['dead-target']}  (check_link_targets.py)")
    print(f"  single candidate:       {stats['single-candidate']}")
    print(f"  multi, all older:       {stats['multi-old']}")
    print(f"  multi, NEWCOMER:        {stats['multi-newcomer']}")
    print(f"  cross-refs scanned:     {stats['xrefs']}")
    print(f"  cross-ref NEWCOMER:     {stats['xref-newcomer']}")
    print(f"  findings total:         {len(findings)}  in {len(entries)} entries")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--summary", action="store_true", help="counts only")
    ap.add_argument("--json", action="store_true", help="machine-readable queue")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--since", metavar="YYYY-MM-DD",
                    help="only competitors created on or after this date")
    ap.add_argument("--limit", type=int, default=50, help="findings to print (default 50)")
    ap.add_argument("--entries-dir", type=Path, default=ENTRIES_DIR)
    ap.add_argument("--lookup", type=Path, default=LOOKUP_PATH)
    args = ap.parse_args()

    findings, stats = scan(tuple(args.range) if args.range else None, args.since,
                           args.entries_dir, args.lookup)
    if args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    elif args.summary:
        summarize(findings, stats)
    else:
        report(findings, args.limit)
        print()
        summarize(findings, stats)
    return 0


if __name__ == "__main__":
    sys.exit(main())
