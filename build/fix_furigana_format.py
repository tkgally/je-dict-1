#!/usr/bin/env python3
"""Fix the mechanically-safe classes of malformed furigana wrappers.

Companion to build/check_furigana_format.py (the read-only detector). Only
fixes whose correctness follows from the wrapper itself are applied:

  (a) kana-only wrapper: ``{X}`` or ``{X|Y}`` where the surface X is entirely
      kana -> plain ``X``. With a pipe this happens only when Y is empty, equals
      X, or is X's hiragana reading ({コンビニ|こんびに}); any other Y (e.g. the
      reversed {ところ|所}) is left alone and reported.
  (b) over-wrapped okurigana: the surface ends with hiragana and the reading
      ends with exactly those same kana -> the maximal common trailing kana
      move outside: {痛み|いたみ} -> {痛|いた}み, {食べる|たべる} -> {食|た}べる.
      Skipped when the remaining surface would have no kanji or the remaining
      reading would be empty.
  (c) fused honorific prefix: ``{お茶|おちゃ}`` -> ``お{茶|ちゃ}``, ``{ご飯|ごはん}``
      -> ``ご{飯|はん}``. Only when the surface starts with お/ご immediately
      followed by a kanji, the reading starts with the same kana, and the
      remainder still contains kanji (so {ごみ箱|ごみばこ} is NOT touched).
  (d) inline-link base forms — the part after → up to ： inside ⟦…⟧ — are
      never modified; only link surfaces and plain text are.
  (e) nested outer wrapper: an outer brace pair enclosing proper inner
      wrappers is dropped — ``{お{正月|しょうがつ}}`` -> ``お{正月|しょうがつ}``,
      ``{{誇|ほこ}}り`` -> ``{誇|ほこ}り``, ``{ガス{代|だい}|がすだい}`` -> ``ガス{代|だい}``
      (an outer reading is dropped only when every kanji inside already has
      its own wrapper; ``{教{室|しつ}|きょうしつ}`` is left for a human because
      教 would lose its reading). Outer groups spanning a newline or more than
      120 characters are left alone too.

Strings with unbalanced braces (a stray ``{`` or ``}``) are skipped entirely
(reported as "skipped-unbalanced"); those need a human. Applied to every text field that
can carry furigana: headword, definitions, examples, notes, cross-reference
and prominent-see-also headwords, conjugation forms, fixed patterns, common
mistakes, particle data. ``id``, ``reading`` and ``metadata`` are never touched.

Dry run by default; nothing is written without --apply.

Usage:
    python3 build/fix_furigana_format.py                    # dry run, counts per fix type
    python3 build/fix_furigana_format.py --show 40           # also list sample fixes
    python3 build/fix_furigana_format.py --range 1000 1499
    python3 build/fix_furigana_format.py --entries-dir COPY --apply
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_common import (  # noqa: E402
    add_common_args, resolve_apply, parse_ids, iter_entry_paths, load_entry,
    write_entry, touch_modified, utc_now, entry_label,
)
from japanese_utils import normalize_reading  # noqa: E402

WRAPPER_RE = re.compile(r"\{([^{}|]*)(?:\|([^{}]*))?\}")
KANA_ONLY_RE = re.compile(r"^[ぁ-ゟ゠-ヿゝゞヽヾ]+$")
HIRAGANA_CHAR_RE = re.compile(r"[ぁ-ゖ]")
KANJI_RE = re.compile(r"[一-鿿㐀-䶿豈-﫿々〆]")
LINK_RE = re.compile(r"⟦([^⟦⟧]*?)→([^⟦⟧]*?)⟧")
SKIP_TOP_LEVEL = {"id", "reading", "metadata", "schema_version"}
SKIP_KEYS = {"id", "target_id", "sense_numbers", "has_audio"}


def is_unbalanced(text: str) -> bool:
    """True if a `}` has no opener or a `{` is never closed (nesting is fine here)."""
    depth = 0
    for ch in text:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                return True
    return depth != 0


def _top_level_groups(text: str):
    """Yield (start, end_exclusive, content) for every outermost {...} group."""
    depth = 0
    start = None
    for i, ch in enumerate(text):
        if ch == "{":
            depth += 1
            if depth == 1:
                start = i
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                yield start, i + 1, text[start + 1:i]
                start = None


def _base_form_spans(text: str):
    """Character spans of ⟦…→BASE：id⟧ tails that must never be edited."""
    spans = []
    for m in LINK_RE.finditer(text):
        arrow = text.index("→", m.start())
        spans.append((arrow, m.end()))
    return spans


def unwrap_nested(text: str, fixes: Counter, holds: Counter) -> str:
    """Fix (e): drop outer brace pairs that enclose inner wrappers."""
    for _ in range(5):   # {a{b{c|d}}} needs one pass per level
        protected = _base_form_spans(text)
        out = []
        pos = 0
        changed = False
        for start, end, content in _top_level_groups(text):
            if "{" not in content:
                continue
            if any(a <= start < b or a <= end - 1 < b for a, b in protected):
                continue   # the outer braces sit inside a link base form
            depth = 0
            pipe = None
            for j, ch in enumerate(content):
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                elif ch == "|" and depth == 0:
                    pipe = j
                    break
            inner = content if pipe is None else content[:pipe]
            reading = None if pipe is None else content[pipe + 1:]
            if "\n" in inner or len(inner) > 120:
                holds["nested-outer-too-long"] += 1
                continue
            if reading:
                bare = re.sub(r"\{[^{}]*\}", "", inner)
                if KANJI_RE.search(bare):
                    holds["nested-outer-reading-needed"] += 1
                    continue
            out.append(text[pos:start])
            out.append(inner)
            pos = end
            fixes["nested-outer"] += 1
            changed = True
        out.append(text[pos:])
        text = "".join(out)
        if not changed:
            break
    return text


def fix_wrapper(surface: str, reading):
    """Return (replacement_text, [fix_types], hold_reason).

    reading is None for a pipe-less ``{X}`` group. When nothing applies the
    replacement is the original wrapper text and fix_types is empty.
    """
    original = f"{{{surface}|{reading}}}" if reading is not None else f"{{{surface}}}"
    if not surface:
        return original, [], "empty-surface"
    if KANA_ONLY_RE.match(surface):
        if reading is None or reading == "" or normalize_reading(reading) == normalize_reading(surface):
            return surface, ["kana-only"], None
        return original, [], "kana-only-reading-mismatch"
    if reading is None:
        return original, [], "no-pipe-with-kanji" if KANJI_RE.search(surface) else "no-pipe-symbol"
    if not KANJI_RE.search(surface):
        return original, [], "symbol-surface"   # {3|さん}, {〇|まる}: deliberate readings

    fixes = []
    prefix = ""
    if (len(surface) > 1 and surface[0] in "おご" and KANJI_RE.match(surface[1])
            and len(reading) > 1 and reading[0] == surface[0]):
        prefix, surface, reading = surface[0], surface[1:], reading[1:]
        fixes.append("o-go-prefix")

    trailing = ""
    m = re.search(r"[ぁ-ゖ]+$", surface)
    if m:
        run = m.group(0)
        for k in range(len(run), 0, -1):
            tail = run[-k:]
            if reading.endswith(tail) and len(reading) > k and KANJI_RE.search(surface[:-k]):
                trailing, surface, reading = tail, surface[:-k], reading[:-k]
                fixes.append("over-wrapped")
                break
    if not fixes:
        return original, [], None
    return f"{prefix}{{{surface}|{reading}}}{trailing}", fixes, None


def fix_text(text: str):
    """Apply fix_wrapper to every wrapper in `text` outside link base forms.

    Returns (new_text, Counter(fix_type), Counter(hold_reason))."""
    fixes = Counter()
    holds = Counter()
    if not text or "{" not in text:
        return text, fixes, holds
    if is_unbalanced(text):
        holds["skipped-unbalanced"] += 1
        return text, fixes, holds
    text = unwrap_nested(text, fixes, holds)

    def fix_segment(seg: str) -> str:
        def repl(m):
            new, kinds, hold = fix_wrapper(m.group(1), m.group(2))
            for k in kinds:
                fixes[k] += 1
            if hold:
                holds[hold] += 1
            return new
        return WRAPPER_RE.sub(repl, seg)

    out = []
    pos = 0
    for m in LINK_RE.finditer(text):
        out.append(fix_segment(text[pos:m.start()]))
        out.append(f"⟦{fix_segment(m.group(1))}→{m.group(2)}⟧")   # base form untouched
        pos = m.end()
    out.append(fix_segment(text[pos:]))
    return "".join(out), fixes, holds


def fix_entry(entry: dict):
    """Fix all furigana-bearing fields in place. Returns (fixes, holds, fields_changed)."""
    fixes = Counter()
    holds = Counter()
    changed_fields = []

    def walk(obj, path):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in SKIP_KEYS:
                    continue
                if isinstance(v, str):
                    new, f, h = fix_text(v)
                    fixes.update(f)
                    holds.update(h)
                    if new != v:
                        obj[k] = new
                        changed_fields.append(f"{path}.{k}" if path else k)
                else:
                    walk(v, f"{path}.{k}" if path else k)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                if isinstance(v, str):
                    new, f, h = fix_text(v)
                    fixes.update(f)
                    holds.update(h)
                    if new != v:
                        obj[i] = new
                        changed_fields.append(f"{path}[{i}]")
                else:
                    walk(v, f"{path}[{i}]")

    for key, value in list(entry.items()):
        if key in SKIP_TOP_LEVEL:
            continue
        if isinstance(value, str):
            new, f, h = fix_text(value)
            fixes.update(f)
            holds.update(h)
            if new != value:
                entry[key] = new
                changed_fields.append(key)
        else:
            walk(value, key)
    return fixes, holds, changed_fields


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(ap)
    ap.add_argument("--show", type=int, default=0, help="Print up to N sample before/after wrappers")
    ap.add_argument("--report", type=Path, default=None, help="Write per-entry fix details to this JSON file")
    args = ap.parse_args(argv)
    apply = resolve_apply(args)

    scanned = 0
    changed_entries = []
    fixes = Counter()
    holds = Counter()
    field_counts = Counter()
    samples = []
    details = []
    timestamp = utc_now()
    for path in iter_entry_paths(args.entries_dir, parse_ids(args.ids), args.range):
        try:
            entry, raw = load_entry(path)
        except (json.JSONDecodeError, OSError) as e:
            print(f"warning: skipping {path}: {e}", file=sys.stderr)
            continue
        scanned += 1
        before = json.dumps(entry, ensure_ascii=False) if args.show else None
        f, h, changed_fields = fix_entry(entry)
        fixes.update(f)
        holds.update(h)
        label = entry_label(entry, path)
        if changed_fields:
            changed_entries.append(label)
            for cf in changed_fields:
                field_counts[cf.split(".")[0].split("[")[0]] += 1
            details.append({"id": label, "fields": changed_fields, "fixes": dict(f)})
            if args.show and len(samples) < args.show:
                after = json.dumps(entry, ensure_ascii=False)
                # find the first differing wrapper for a readable sample
                for m in WRAPPER_RE.finditer(before):
                    new, kinds, _ = fix_wrapper(m.group(1), m.group(2))
                    if kinds:
                        samples.append(f"  {label}: {m.group(0)} -> {new}  ({'+'.join(kinds)})")
                        break
                del after
            if apply:
                touch_modified(entry, timestamp)
                write_entry(path, entry, raw)

    mode = "APPLIED" if apply else "DRY RUN"
    print(f"[{mode}] fix_furigana_format: {scanned} entries scanned, {len(changed_entries)} "
          f"{'rewritten' if apply else 'would change'}")
    print("  fixes by type: " + (", ".join(f"{k}={v}" for k, v in sorted(fixes.items())) or "none"))
    print("  changed fields: " + (", ".join(f"{k}={v}" for k, v in field_counts.most_common()) or "none"))
    print("  left alone (needs a human): " + (", ".join(f"{k}={v}" for k, v in sorted(holds.items())) or "none"))
    if samples:
        print("\nSamples:")
        print("\n".join(samples))
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with open(args.report, "w", encoding="utf-8") as fp:
            json.dump({"generated": timestamp, "fixes": dict(fixes), "holds": dict(holds),
                       "entries": details}, fp, ensure_ascii=False, indent=2)
            fp.write("\n")
        print(f"\nReport written to {args.report}")
    if not apply and changed_entries:
        print("\nDry run — nothing written. Re-run with --apply to write.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
