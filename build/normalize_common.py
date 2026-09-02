"""Shared plumbing for the mechanical normalization tools.

Used by normalize_notes.py, normalize_pos.py, backfill_register.py and
fix_furigana_format.py so they all behave the same way:

- every tool is a DRY RUN by default and only writes with ``--apply``
  (``--dry-run`` always wins if both are given);
- ``--ids``, ``--range START END`` and ``--entries-dir`` restrict which files are
  considered (``--entries-dir`` lets you rehearse ``--apply`` on a copy);
- files are only rewritten when the parsed entry actually changed, and a
  rewritten file keeps its own trailing-newline convention (the corpus is mixed:
  most files end with a newline, some do not);
- a changed entry gets ``metadata.modified`` set to the current UTC time in the
  same format as build/get_timestamp.py (YYYY-MM-DDTHH:MM:SSZ).
"""
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ENTRIES_DIR = PROJECT_ROOT / "entries"

_ID_PREFIX_RE = re.compile(r"^(\d{5})_")


def add_common_args(parser: argparse.ArgumentParser) -> None:
    """Add the --apply/--dry-run/--ids/--range/--entries-dir options."""
    parser.add_argument("--apply", action="store_true",
                        help="Write the changes. Without this the tool only reports "
                             "what it would do (dry run).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Report only (the default). If given together with "
                             "--apply, --dry-run wins.")
    parser.add_argument("--ids", type=str, default=None,
                        help="Comma-separated entry IDs to restrict to "
                             "(5-digit numbers or full IDs, e.g. 01000,01186_tekubi)")
    parser.add_argument("--range", nargs=2, type=int, metavar=("START", "END"),
                        help="Restrict to numeric entry IDs START..END inclusive")
    parser.add_argument("--entries-dir", type=Path, default=DEFAULT_ENTRIES_DIR,
                        help=f"Entries directory to scan (default: {DEFAULT_ENTRIES_DIR}). "
                             "Point this at a copy to rehearse --apply safely.")


def resolve_apply(args) -> bool:
    """True only when --apply was given without --dry-run."""
    return bool(getattr(args, "apply", False)) and not bool(getattr(args, "dry_run", False))


def parse_ids(spec) -> set:
    """Turn '01000,1186_tekubi, 30001' into {'01000', '01186', '30001'}."""
    if not spec:
        return set()
    out = set()
    for token in str(spec).split(","):
        token = token.strip()
        if not token:
            continue
        m = re.match(r"^(\d+)", token)
        if not m:
            raise ValueError(f"Bad entry ID in --ids: {token!r}")
        out.add(f"{int(m.group(1)):05d}")
    return out


def numeric_id_of(path: Path):
    """Numeric ID from an entries/.../NNNNN_romaji.json path (None if unparsable)."""
    m = _ID_PREFIX_RE.match(path.name)
    return int(m.group(1)) if m else None


def iter_entry_paths(entries_dir: Path, ids=None, id_range=None):
    """Sorted entry file paths under entries_dir, honoring --ids / --range."""
    wanted = set(ids or ())
    lo, hi = (id_range if id_range else (None, None))
    for path in sorted(Path(entries_dir).glob("**/*.json")):
        nid = numeric_id_of(path)
        if nid is None:
            continue
        if wanted and f"{nid:05d}" not in wanted:
            continue
        if lo is not None and not (lo <= nid <= hi):
            continue
        yield path


def load_entry(path: Path):
    """Return (entry_dict, raw_text). Raises on invalid JSON."""
    raw = Path(path).read_text(encoding="utf-8")
    return json.loads(raw), raw


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def touch_modified(entry: dict, timestamp: str = None) -> None:
    """Set metadata.modified (creating metadata if somehow absent)."""
    md = entry.setdefault("metadata", {})
    md["modified"] = timestamp or utc_now()


def write_entry(path: Path, entry: dict, raw_text: str = None) -> None:
    """Serialize like the rest of the build (indent=2, ensure_ascii=False).

    The trailing newline follows the file's existing convention: kept if the
    original text ended with one, omitted if it did not. New files get one.
    """
    text = json.dumps(entry, ensure_ascii=False, indent=2)
    if raw_text is None or raw_text.endswith("\n"):
        text += "\n"
    Path(path).write_text(text, encoding="utf-8")


def entry_label(entry: dict, path: Path) -> str:
    return str(entry.get("id") or path.stem)
