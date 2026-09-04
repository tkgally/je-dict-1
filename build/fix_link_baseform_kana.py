#!/usr/bin/env python3
"""Fix inline-link base forms written in kana where the target entry is kanji.

Cleanup Backlog Priority 32 (planning/wiki/ideas/cleanup-backlog.md), backlog
item ``link-baseform-kana``. Inline links use ``⟦surface→baseform：entry_id⟧``;
``docs/styles.css`` renders the base-form segment as the hover tooltip
(``content: attr(data-baseform)``). When the base form is written in kana equal
to the target entry's ``reading`` while the target's ``headword`` is kanji, the
tooltip shows the learner the pronunciation they can already see in the
furigana instead of the dictionary form they would need to look the word up.

Fix: replace the base-form segment with the target entry's furigana-stripped
headword. The target_id is already declared on the link and untouched by this
script -- there is no lookup ambiguity, only a text substitution.

Skipped (left untouched):
  - ``target == noentry``
  - a target id that does not resolve to a real entry (``check_link_targets.py``
    owns that population)
  - the base form does not exactly equal the target's ``reading`` (a different
    kind of disagreement; ``build/check_link_baseform.py`` owns wrong-target
    links)
  - the target's furigana-stripped headword IS kana (no kanji in it) -- the
    base form is already the correct dictionary form
  - the target's headword lists multiple variants (``優しい／優しい``) -- which
    one is right depends on the sentence; left for per-entry judgment

The script never touches the surface or target_id slots, and it changes no
Japanese text outside the base-form slot of a link that already exists.

Dry run by default; nothing is written without --apply.

Usage:
    python3 build/fix_link_baseform_kana.py                  # dry run, counts
    python3 build/fix_link_baseform_kana.py --show 40         # list sample fixes
    python3 build/fix_link_baseform_kana.py --range 1000 1499
    python3 build/fix_link_baseform_kana.py --apply
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_common import (  # noqa: E402
    add_common_args, resolve_apply, parse_ids, iter_entry_paths, load_entry,
    write_entry, touch_modified, entry_label,
)

LINK_BLOCK_RE = re.compile(r"⟦([^⟧]+)⟧")
LINK_INFO_RE = re.compile(r"^(.+?)→(.+?)：(.+)$")
FURIGANA_RE = re.compile(r"\{([^|{}]+)\|([^|{}]+)\}")
KANJI_RE = re.compile(r"[一-鿿々〆]")
MULTI_VARIANT_RE = re.compile(r"[／/、,]")
NOENTRY = "noentry"


def strip_furigana(text: str) -> str:
    return FURIGANA_RE.sub(lambda m: m.group(1), text)


def load_forms(entries_dir: Path) -> dict:
    """Map every entry's full id (e.g. ``00229_kikan``) -> (headword, reading).

    Link targets are declared as the full ``NNNNN_romaji`` stem, matching the
    entry's own ``id`` field and its file's stem -- both are indexed here since
    a handful of legacy entries carry an ``id`` that drifted from the filename.
    """
    forms = {}
    for path in sorted(Path(entries_dir).glob("**/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        pair = (data.get("headword", ""), data.get("reading", ""))
        forms[path.stem] = pair
        entry_id = data.get("id")
        if entry_id:
            forms[str(entry_id)] = pair
    return forms


def fix_text(text: str, forms: dict, counts: Counter) -> str:
    def repl(m: re.Match) -> str:
        info = LINK_INFO_RE.match(m.group(1))
        if not info:
            return m.group(0)
        surface, base, target = (g.strip() for g in info.groups())
        if target == NOENTRY:
            return m.group(0)
        headword, reading = forms.get(target, ("", ""))
        if not headword:
            counts["dead-target"] += 1
            return m.group(0)
        if base != reading:
            counts["not-reading-match"] += 1
            return m.group(0)
        hw_stripped = strip_furigana(headword)
        if hw_stripped == base:
            counts["already-correct"] += 1
            return m.group(0)
        if not KANJI_RE.search(hw_stripped):
            counts["kana-headword"] += 1
            return m.group(0)
        if MULTI_VARIANT_RE.search(hw_stripped):
            counts["multi-variant"] += 1
            return m.group(0)
        counts["fixed"] += 1
        return f"⟦{surface}→{hw_stripped}：{target}⟧"

    return LINK_BLOCK_RE.sub(repl, text)


def fix_value(value, forms: dict, counts: Counter):
    """Recursively rewrite links inside strings/dicts/lists. Returns (value, changed)."""
    if isinstance(value, str):
        if "⟦" not in value:
            return value, False
        new = fix_text(value, forms, counts)
        return new, new != value
    if isinstance(value, dict):
        changed = False
        for k, v in value.items():
            nv, c = fix_value(v, forms, counts)
            if c:
                value[k] = nv
                changed = True
        return value, changed
    if isinstance(value, list):
        changed = False
        for i, v in enumerate(value):
            nv, c = fix_value(v, forms, counts)
            if c:
                value[i] = nv
                changed = True
        return value, changed
    return value, False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    add_common_args(parser)
    parser.add_argument("--show", type=int, default=0, help="list N sample fixed entries")
    args = parser.parse_args()
    apply = resolve_apply(args)

    forms = load_forms(args.entries_dir)
    ids = parse_ids(args.ids) if args.ids else None
    id_range = tuple(args.range) if args.range else None

    counts: Counter = Counter()
    touched: list[str] = []
    samples: list[str] = []
    for path in iter_entry_paths(args.entries_dir, ids=ids, id_range=id_range):
        entry, raw = load_entry(path)
        _, changed = fix_value(entry, forms, counts)
        if not changed:
            continue
        touched.append(entry_label(entry, path))
        if len(samples) < args.show:
            samples.append(f"{entry_label(entry, path)}  {path}")
        if apply:
            touch_modified(entry)
            write_entry(path, entry, raw)

    for s in samples:
        print("changed:", s)
    print(dict(counts))
    print(f"entries touched: {len(touched)}  ({'applied' if apply else 'dry run'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
