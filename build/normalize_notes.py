#!/usr/bin/env python3
"""Normalize section headers and bullet markers in the ``notes`` field.

The vocabulary is build/data/note_headers.json (authoritative): each canonical
header has a list of legacy aliases. This tool is mechanical and touches ONLY
header lines and bullet markers:

  (a) a header line whose text (trimmed, trailing colon removed, whitespace
      collapsed, case-insensitive, inline links reduced to their surface text)
      equals a canonical header or one of its aliases is rewritten to the
      canonical ``CANONICAL:`` form;
  (b) bullet lines starting with ``・`` or ``•`` (optionally indented; a space
      after the marker is optional) or with ``‐``/``–`` followed by a space are
      rewritten as ``- `` bullets, keeping any indentation;
  (c) when two sections end up under the same canonical header (e.g. an entry
      had both COLLOCATIONS: and COMMON COLLOCATIONS:), the later section's
      lines are appended to the first and the duplicate header dropped;
  (d) runs of three or more consecutive newlines (two or more blank lines) are
      collapsed to a single blank line, which is the corpus convention;
  (e) headers that are neither canonical nor an alias are reported (counts,
      sample entries) and written to ``--unknown-report FILE`` as JSON.

What counts as a header: a line at column 0 that ends with ':' (trailing
spaces ignored), does not begin with a bullet marker, and whose text outside
parentheses / furigana wrappers / inline links is ALL CAPS (A-Z, digits, kana
and light punctuation only). ``NOTE: some prose`` is not a header (no trailing
colon); ``- NHK:`` is not a header (bullet).

Dry run by default. Nothing is written without --apply.

Usage:
    python3 build/normalize_notes.py                       # dry run over the dictionary
    python3 build/normalize_notes.py --unknown-report /tmp/unknown.json --top 50
    python3 build/normalize_notes.py --range 1000 1499 --show 3   # print diffs for 3 entries
    python3 build/normalize_notes.py --entries-dir /path/to/copy --apply
"""
import argparse
import difflib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_common import (  # noqa: E402
    PROJECT_ROOT, add_common_args, resolve_apply, parse_ids, iter_entry_paths,
    load_entry, write_entry, touch_modified, utc_now, entry_label,
)

DEFAULT_VOCAB = PROJECT_ROOT / "build" / "data" / "note_headers.json"

# ⟦surface→base：id⟧ inline links; group 1 is the surface text.
LINK_RE = re.compile(r"⟦([^⟦⟧→]*)→[^⟦⟧]*⟧")
FURIGANA_RE = re.compile(r"\{[^{}]*\}")
PAREN_RE = re.compile(r"\([^()]*\)")
# Characters allowed in the ALL-CAPS core of a header (after stripping
# parentheticals, furigana wrappers and links): capitals, digits, kana, spaces
# and light punctuation. Lowercase ASCII is deliberately absent.
HEADER_CORE_RE = re.compile(r"^[A-Z0-9 /&'’\-\.,:;~〜～・+＋ぁ-ゟ゠-ヿ]+$")
HEADER_HAS_LETTER_RE = re.compile(r"[A-Zぁ-ゟ゠-ヿ]")
HEADER_LINE_RE = re.compile(r"^(?P<body>.*?[^\s:])\s*:\s*$")
# Bullet markers: ・ and • may be followed directly by text; ‐ (U+2010) and
# – (U+2013) only count as bullets when followed by a space.
BULLET_RE = re.compile(r"^(?P<indent>[ \t]*)(?:(?P<dot>[・•])[ \t]*|(?P<dash>[‐–])[ \t]+)(?P<rest>\S.*)$")
DASH_BULLET_RE = re.compile(r"^[ \t]*-\s")
MULTI_NEWLINE_RE = re.compile(r"\n{3,}")


# ---------------------------------------------------------------------------
# Vocabulary
# ---------------------------------------------------------------------------

def normalize_header_text(body: str) -> str:
    """Trim, drop trailing colons, reduce links to surface text, collapse spaces."""
    s = LINK_RE.sub(lambda m: m.group(1), body)
    s = s.strip()
    while s.endswith(":"):
        s = s[:-1].rstrip()
    return re.sub(r"\s+", " ", s)


def header_key(body: str) -> str:
    return normalize_header_text(body).upper()


def load_header_vocab(path: Path = DEFAULT_VOCAB) -> dict:
    """Return {key -> canonical header} for canonical names and every alias."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    lookup = {}
    canonical = data.get("canonical", {})
    for canon, info in canonical.items():
        lookup.setdefault(header_key(canon), canon)
        for alias in (info or {}).get("aliases", []) or []:
            lookup.setdefault(header_key(alias), canon)
    return lookup


# ---------------------------------------------------------------------------
# Line classification
# ---------------------------------------------------------------------------

def header_body(line: str):
    """Return the header text (without the colon) if `line` is a header, else None."""
    if not line or line[0].isspace():
        return None
    if DASH_BULLET_RE.match(line) or BULLET_RE.match(line):
        return None
    m = HEADER_LINE_RE.match(line)
    if not m:
        return None
    body = m.group("body")
    core = LINK_RE.sub(" ", body)
    core = FURIGANA_RE.sub(" ", core)
    core = PAREN_RE.sub(" ", core)
    core = core.strip()
    if not core or not HEADER_CORE_RE.match(core) or not HEADER_HAS_LETTER_RE.search(core):
        return None
    return body


def is_header_line(line: str) -> bool:
    return header_body(line) is not None


def convert_bullet(line: str):
    """Return the ``- `` form of a ・/•/‐/– bullet line, or None if not one."""
    m = BULLET_RE.match(line)
    if not m:
        return None
    return f"{m.group('indent')}- {m.group('rest')}"


# ---------------------------------------------------------------------------
# Notes transformation
# ---------------------------------------------------------------------------

@dataclass
class NotesChange:
    renamed: Counter = field(default_factory=Counter)      # (from, to) -> count
    bullets: int = 0
    merged: Counter = field(default_factory=Counter)       # canonical -> merges
    blank_runs: int = 0
    unknown: Counter = field(default_factory=Counter)      # normalized header text -> count

    @property
    def changed(self) -> bool:
        return bool(self.renamed or self.bullets or self.merged or self.blank_runs)


@dataclass
class _Section:
    header: str            # canonical/unknown header text, or None for the preamble
    canonical: bool
    lines: list


def _trim_trailing_blank(lines: list) -> list:
    out = list(lines)
    while out and out[-1].strip() == "":
        out.pop()
    return out


def normalize_notes(notes: str, vocab: dict) -> tuple:
    """Return (new_notes, NotesChange). Only header lines and bullet markers move."""
    change = NotesChange()
    if not notes:
        return notes, change

    lines = notes.split("\n")
    sections = [_Section(None, False, [])]
    for line in lines:
        body = header_body(line)
        if body is not None:
            key = header_key(body)
            canon = vocab.get(key)
            if canon is not None:
                new_line = f"{canon}:"
                if new_line != line:
                    change.renamed[(normalize_header_text(body), canon)] += 1
                sections.append(_Section(canon, True, []))
            else:
                change.unknown[normalize_header_text(body)] += 1
                sections.append(_Section(body, False, []))
            continue
        converted = convert_bullet(line)
        if converted is not None and converted != line:
            change.bullets += 1
            line = converted
        sections[-1].lines.append(line)

    # (c) merge duplicate canonical sections into the first occurrence
    first_by_canon = {}
    merged_sections = []
    for sec in sections:
        if sec.canonical and sec.header in first_by_canon:
            target = first_by_canon[sec.header]
            body_lines = _trim_trailing_blank(sec.lines)
            target_had_blank = bool(target.lines) and target.lines[-1].strip() == ""
            target.lines = _trim_trailing_blank(target.lines) + body_lines
            if target_had_blank:
                target.lines.append("")
            change.merged[sec.header] += 1
            continue
        if sec.canonical:
            first_by_canon[sec.header] = sec
        merged_sections.append(sec)

    out_lines = []
    for sec in merged_sections:
        if sec.header is not None:
            out_lines.append(f"{sec.header}:")
        out_lines.extend(sec.lines)
    new_notes = "\n".join(out_lines)

    # (d) collapse 3+ consecutive newlines (2+ blank lines) to one blank line
    collapsed, n = MULTI_NEWLINE_RE.subn("\n\n", new_notes)
    if n:
        change.blank_runs += n
        new_notes = collapsed
    # a merge can leave a dangling separator at the very end; never add one
    if not notes.endswith("\n"):
        new_notes = new_notes.rstrip("\n")

    if new_notes == notes:
        # nothing actually moved (e.g. a rename that produced identical text)
        change.renamed.clear()
        change.bullets = 0
        change.merged.clear()
        change.blank_runs = 0
    return new_notes, change


def find_headers(notes: str, vocab: dict):
    """Yield (line_number, header_text, canonical_or_None) for each header line."""
    if not notes:
        return
    for i, line in enumerate(notes.split("\n"), 1):
        body = header_body(line)
        if body is None:
            continue
        yield i, normalize_header_text(body), vocab.get(header_key(body))


def unknown_headers(notes: str, vocab: dict) -> list:
    """Sorted, de-duplicated list of non-canonical headers in `notes`."""
    return sorted({text for _, text, canon in find_headers(notes, vocab) if canon is None})


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(ap)
    ap.add_argument("--vocab", type=Path, default=DEFAULT_VOCAB,
                    help=f"Header vocabulary JSON (default: {DEFAULT_VOCAB})")
    ap.add_argument("--unknown-report", type=Path, default=None,
                    help="Write unknown headers (counts + sample entries) to this JSON file")
    ap.add_argument("--top", type=int, default=30, help="How many unknown headers / renames to print")
    ap.add_argument("--show", type=int, default=0, help="Print unified diffs for the first N changed entries")
    ap.add_argument("--quiet", action="store_true", help="Only print the summary")
    args = ap.parse_args(argv)
    apply = resolve_apply(args)

    vocab = load_header_vocab(args.vocab)
    ids = parse_ids(args.ids)
    total = 0
    changed_entries = []
    renamed = Counter()
    bullets = 0
    merged = Counter()
    blank_runs = 0
    unknown = Counter()
    unknown_samples = defaultdict(list)
    shown = 0
    timestamp = utc_now()

    for path in iter_entry_paths(args.entries_dir, ids, args.range):
        try:
            entry, raw = load_entry(path)
        except (json.JSONDecodeError, OSError) as e:
            print(f"warning: skipping {path}: {e}", file=sys.stderr)
            continue
        total += 1
        notes = entry.get("notes")
        if not isinstance(notes, str) or not notes:
            continue
        new_notes, ch = normalize_notes(notes, vocab)
        label = entry_label(entry, path)
        for h, c in ch.unknown.items():
            unknown[h] += c
            if len(unknown_samples[h]) < 5:
                unknown_samples[h].append(label)
        if not ch.changed:
            continue
        changed_entries.append(label)
        renamed.update(ch.renamed)
        bullets += ch.bullets
        merged.update(ch.merged)
        blank_runs += ch.blank_runs
        if shown < args.show:
            shown += 1
            diff = difflib.unified_diff(notes.split("\n"), new_notes.split("\n"),
                                        fromfile=f"{label} (before)", tofile=f"{label} (after)", lineterm="")
            print("\n".join(diff))
            print()
        if apply:
            entry["notes"] = new_notes
            touch_modified(entry, timestamp)
            write_entry(path, entry, raw)

    mode = "APPLIED" if apply else "DRY RUN"
    print(f"[{mode}] normalize_notes: {total} entries scanned, {len(changed_entries)} would change"
          if not apply else f"[{mode}] normalize_notes: {total} entries scanned, {len(changed_entries)} rewritten")
    print(f"  header lines renamed: {sum(renamed.values())} ({len(renamed)} distinct from->to pairs)")
    print(f"  bullet markers converted to '- ': {bullets}")
    print(f"  duplicate sections merged: {sum(merged.values())} "
          + (f"({', '.join(f'{k}={v}' for k, v in merged.most_common())})" if merged else ""))
    print(f"  blank-line runs collapsed: {blank_runs}")
    print(f"  unknown headers: {len(unknown)} distinct, {sum(unknown.values())} lines")
    if not args.quiet:
        if renamed:
            print(f"\nTop {args.top} renames:")
            for (src, dst), c in renamed.most_common(args.top):
                print(f"  {c:6d}  {src}:  ->  {dst}:")
        if unknown:
            print(f"\nTop {args.top} unknown headers (not canonical, not an alias):")
            for h, c in unknown.most_common(args.top):
                print(f"  {c:6d}  {h}:   e.g. {', '.join(unknown_samples[h][:3])}")
    if args.unknown_report:
        payload = {
            "generated": timestamp,
            "entries_scanned": total,
            "distinct_unknown_headers": len(unknown),
            "unknown_header_lines": sum(unknown.values()),
            "unknown_headers": [
                {"header": h, "count": c, "sample_entries": unknown_samples[h]}
                for h, c in unknown.most_common()
            ],
        }
        args.unknown_report.parent.mkdir(parents=True, exist_ok=True)
        with open(args.unknown_report, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"\nUnknown-header report written to {args.unknown_report}")
    if not apply and changed_entries:
        print("\nDry run — nothing written. Re-run with --apply to write "
              f"({'--entries-dir ' + str(args.entries_dir) if args.entries_dir != PROJECT_ROOT / 'entries' else 'the live entries/ tree'}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
