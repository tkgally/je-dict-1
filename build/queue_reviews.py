#!/usr/bin/env python3
"""Add this branch's changed entries to reviews/queue.txt.

reviews/queue.txt lists the entry files changed since their last cross-model
review; the accuracy-review mode removes the ranges it reviews (routine2.md §A).
Entries are queued here, by `make index`, from the branch's own changes: every
entry file that differs from the merge base with origin/main (committed or not).
An entry whose only change is its examples' has_audio flags is not queued, since
its text did not change. Deleted entries are not queued.

    python3 build/queue_reviews.py            # append and report
    python3 build/queue_reviews.py --dry-run  # report only
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / "reviews" / "queue.txt"


def git(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def text_changed(diff: str) -> bool:
    """True if a file's diff changes any line other than a has_audio flag."""
    return any(line[:1] in "+-" and not line.startswith(("+++", "---"))
               and '"has_audio": ' not in line
               for line in diff.splitlines())


def changed_entries(base: str) -> list[str]:
    names = git("diff", "--name-only", "--diff-filter=d", base, "--", "entries/") or ""
    new = git("ls-files", "--others", "--exclude-standard", "entries/") or ""
    out = [f for f in new.split() if f.endswith(".json")]
    for f in names.split():
        if f.endswith(".json") and text_changed(git("diff", base, "--", f) or ""):
            out.append(f)
    return sorted(set(out))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    base = (git("merge-base", "origin/main", "HEAD") or "").strip()
    if not base:
        print("queue_reviews: origin/main not available (git fetch origin main); queue unchanged")
        return 0
    files = changed_entries(base)
    queued = set(QUEUE.read_text(encoding="utf-8").split()) if QUEUE.exists() else set()
    new = [f for f in files if f not in queued]
    if new and not args.dry_run:
        QUEUE.write_text("".join(f + "\n" for f in sorted(queued | set(new))), encoding="utf-8")
    print(f"queue_reviews: {len(files)} changed entr{'y' if len(files) == 1 else 'ies'} on this branch, "
          f"{len(new)} newly queued ({len(queued | set(new))} in reviews/queue.txt)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
