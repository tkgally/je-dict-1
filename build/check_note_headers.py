#!/usr/bin/env python3
"""CI ratchet for notes section headers (read-only).

Lists every non-canonical header (after alias normalization against
build/data/note_headers.json) per entry, and gates new drift the same way
build/validate_tags.py --check-no-new-unknown gates off-vocabulary semantic tags:

  --summary          counts: entries with unknown headers, distinct headers, top N
  --list             one line per entry: id and its unknown headers
  --write-baseline   write build/data/unknown_header_baseline.json mapping entry id ->
                     sorted list of unknown headers it currently carries. Run this
                     AFTER the normalize_notes.py sweep so the baseline is as small
                     as possible.
  --gate             exit 1 if any entry has an unknown header not tolerated by the
                     baseline for that entry (new drift); print the offenders.
                     Exit 0 otherwise. Missing baseline -> exit 3.

The header definition and alias matching are shared with build/normalize_notes.py.
``--ids``, ``--range`` and ``--entries-dir`` restrict the scan; ``--changed-only``
restricts it to entry files changed vs origin/main (like validate.py).

Usage:
    python3 build/check_note_headers.py --summary
    python3 build/check_note_headers.py --write-baseline               # after the sweep
    python3 build/check_note_headers.py --gate                         # CI
    python3 build/check_note_headers.py --gate --changed-only          # faster CI variant
    python3 build/check_note_headers.py --entries-dir COPY --baseline /tmp/b.json --write-baseline
"""
import argparse
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_common import (  # noqa: E402
    PROJECT_ROOT, DEFAULT_ENTRIES_DIR, parse_ids, iter_entry_paths, load_entry,
    entry_label, utc_now,
)
from normalize_notes import DEFAULT_VOCAB, load_header_vocab, unknown_headers  # noqa: E402

DEFAULT_BASELINE = PROJECT_ROOT / "build" / "data" / "unknown_header_baseline.json"


def changed_entry_paths(project_root: Path, entries_dir: Path):
    """Entry files changed vs origin/main (fallback HEAD~1), mirroring validate.py."""
    for base in ("origin/main...HEAD", "HEAD~1"):
        try:
            res = subprocess.run(["git", "diff", "--name-only", base, "--", "entries/"],
                                 capture_output=True, text=True, cwd=project_root)
        except Exception:
            continue
        files = [f for f in res.stdout.strip().split("\n") if f.endswith(".json")]
        if files:
            out = []
            for rel in files:
                p = entries_dir / Path(rel).relative_to("entries")
                if p.exists():
                    out.append(p)
            return sorted(out)
    return []


def collect_unknown(paths, vocab) -> dict:
    """Map entry id -> sorted unknown headers (only entries that have any)."""
    out = {}
    for path in paths:
        try:
            entry, _ = load_entry(path)
        except (json.JSONDecodeError, OSError):
            continue
        notes = entry.get("notes")
        if not isinstance(notes, str) or not notes:
            continue
        unknown = unknown_headers(notes, vocab)
        if unknown:
            out[entry_label(entry, path)] = unknown
    return out


def write_baseline(data: dict, baseline_path: Path) -> None:
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "_comment": (
            "Ratchet baseline for notes section headers that are neither canonical "
            "nor an alias in build/data/note_headers.json. Maps entry id -> the "
            "unknown headers it already carried when generated. "
            "`build/check_note_headers.py --gate` (run in CI) fails if any entry gains "
            "an unknown header absent from its list here, so the set can only shrink. "
            "Regenerate after a normalization sweep: "
            "python3 build/check_note_headers.py --write-baseline"
        ),
        "generated": utc_now(),
        "headers": data,
    }
    with open(baseline_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")


def load_baseline(baseline_path: Path):
    with open(baseline_path, "r", encoding="utf-8") as f:
        return (json.load(f) or {}).get("headers", {})


def gate(current: dict, baseline: dict) -> list:
    """Return [(entry_id, header)] for unknown headers not tolerated by the baseline."""
    violations = []
    for eid, headers in sorted(current.items()):
        tolerated = set(baseline.get(eid, []))
        for h in headers:
            if h not in tolerated:
                violations.append((eid, h))
    return violations


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--summary", action="store_true", help="Print counts (default action)")
    ap.add_argument("--list", action="store_true", help="List unknown headers per entry")
    ap.add_argument("--write-baseline", action="store_true",
                    help=f"Write the baseline (default path: {DEFAULT_BASELINE})")
    ap.add_argument("--gate", action="store_true",
                    help="Exit 1 on unknown headers not in the baseline (CI regression gate)")
    ap.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE,
                    help="Baseline JSON path (read by --gate, written by --write-baseline)")
    ap.add_argument("--vocab", type=Path, default=DEFAULT_VOCAB, help="Header vocabulary JSON")
    ap.add_argument("--ids", type=str, default=None, help="Comma-separated entry IDs to restrict to")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"), help="Numeric ID range")
    ap.add_argument("--entries-dir", type=Path, default=DEFAULT_ENTRIES_DIR,
                    help="Entries directory to scan (point at a copy to rehearse)")
    ap.add_argument("--changed-only", action="store_true",
                    help="Only entry files changed vs origin/main (falls back to HEAD~1)")
    ap.add_argument("--top", type=int, default=30, help="Rows to print in --summary")
    args = ap.parse_args(argv)

    vocab = load_header_vocab(args.vocab)
    if args.changed_only:
        paths = changed_entry_paths(PROJECT_ROOT, args.entries_dir)
        if not paths:
            print("No changed entry files found.")
            return 0
    else:
        paths = list(iter_entry_paths(args.entries_dir, parse_ids(args.ids), args.range))
    current = collect_unknown(paths, vocab)

    if args.write_baseline:
        if args.changed_only or args.ids or args.range:
            print("error: --write-baseline must cover the whole entries directory "
                  "(drop --changed-only/--ids/--range)", file=sys.stderr)
            return 2
        write_baseline(current, args.baseline)
        total = sum(len(v) for v in current.values())
        print(f"Wrote {args.baseline}: {len(current)} entries, {total} tolerated unknown header(s).")
        return 0

    if args.gate:
        if not args.baseline.exists():
            print(f"error: baseline not found: {args.baseline}", file=sys.stderr)
            print("Generate it with: python3 build/check_note_headers.py --write-baseline",
                  file=sys.stderr)
            return 3
        try:
            baseline = load_baseline(args.baseline)
        except (json.JSONDecodeError, OSError) as e:
            print(f"error: cannot read baseline {args.baseline}: {e}", file=sys.stderr)
            return 3
        violations = gate(current, baseline)
        if not violations:
            print(f"No new unknown notes headers ({len(paths)} entries checked; "
                  f"{len(current)} still carry baselined unknown headers).")
            return 0
        print(f"ERROR: {len(violations)} notes header(s) are neither canonical nor an alias "
              "and are not in the baseline (introduced by this change):\n")
        for eid, h in violations:
            print(f"  {eid}: '{h}:'")
        print("\nSection headers must come from build/data/note_headers.json (canonical names; "
              "aliases are auto-normalized by build/normalize_notes.py).")
        print("Fix one of these ways:")
        print("  - rename the header to a canonical one (see the 'description' of each in note_headers.json); or")
        print("  - if the curator has blessed a new header/alias, add it to note_headers.json and "
              "regenerate the baseline (python3 build/check_note_headers.py --write-baseline).")
        return 1

    if args.list:
        for eid, headers in sorted(current.items()):
            print(f"{eid}: " + " | ".join(f"{h}:" for h in headers))
        print(f"\n{len(current)} entries with unknown headers")
        return 0

    counts = Counter()
    samples = defaultdict(list)
    for eid, headers in current.items():
        for h in headers:
            counts[h] += 1
            if len(samples[h]) < 3:
                samples[h].append(eid)
    print(f"Entries scanned: {len(paths)}")
    print(f"Entries with unknown headers: {len(current)}")
    print(f"Distinct unknown headers: {len(counts)}; total occurrences (per entry): {sum(counts.values())}")
    if counts:
        print(f"\nTop {args.top}:")
        for h, c in counts.most_common(args.top):
            print(f"  {c:6d}  {h}:   e.g. {', '.join(samples[h])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
