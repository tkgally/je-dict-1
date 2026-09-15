#!/usr/bin/env python3
"""Absorb a stranded ``claude/*`` branch into the current branch.

A Routine run that ends with a red or un-merged PR leaves its work on a
branch that later runs cannot merge with a plain ``git merge``: every run
regenerates the same indexes, ledgers, cursors, and session logs, so the
merge conflicts on those files even when the real content (entries, code)
merges cleanly. This tool does the merge with a per-file policy so that a
mid-size model can absorb such a branch mechanically::

    python3 pipeline/absorb_branch.py --residue <branch>   # read-only report
    python3 pipeline/absorb_branch.py <branch> [--pr N] [--no-commit]

``--residue`` lists the durable files the branch changed that still differ
from the current branch (generated files ignored). An empty list means the
branch is fully absorbed and can be pruned.

Absorbing merges ``origin/<branch>`` into HEAD and resolves conflicts like this:

* generated and per-run state (``entries_index.json``, ``build/word_id_lookup.json``,
  ``kanji/``, ``pipeline/routine-state.json``, ``pipeline/openrouter-ledger.json``,
  cursors, ``PROJECT_CONTEXT_BRIEF.md``, ``reviews/queue.txt``, screening status):
  keep ours — ``make index`` regenerates what matters;
* append-only ledgers (``reviews/*.jsonl``, ``pipeline/metrics-history.jsonl``,
  ``reviews/needs_curator.txt``, ``polishing/observations.md``): union — ours plus
  the lines the branch added;
* a session log that collides by name: keep both, the branch's copy renamed to
  the next free number for its date;
* ``candidate_words.json``: keep ours, drop the candidates the branch turned into
  entries, re-queue the candidates it added (fresh IDs, duplicate-checked);
* ``PROJECT_STATUS.md``: keep ours, insert the branch's new "Recent Changes"
  sections in date order, keep five;
* anything else in conflict (an entry, code, a prompt, a wiki page): abort the
  whole merge and list the files — that needs a person.

Entries the branch changed are never resolved by policy: a clean auto-merge
stands, a conflict aborts. A new kanji the branch registered in
``kanji/kanji_list.json`` is dropped with the generated files; ``make index``
reports it and it is re-added with the next free ID (the branch's ID may since
have gone to another kanji on main). Entries changed on both sides since the branch
diverged are listed at the end so the caller can validate and read them.
After a successful absorb run ``make gate`` and fix what it reports.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GENERATED_PREFIXES = (
    "entries_index.json",
    "build/word_id_lookup.json",
    "kanji/",
    "pipeline/routine-state.json",
    "pipeline/openrouter-ledger.json",
    "PROJECT_CONTEXT_BRIEF.md",
    "reviews/queue.txt",
    "reviews/screening/",
    "polishing/tasks/comprehensive/progress.txt",
    "polishing/tasks/comprehensive/priority-cursor.txt",
    "polishing/tasks/cross-model-review/progress.txt",
    "docs/",
)

UNION_FILES = (
    "reviews/decisions.jsonl",
    "reviews/accuracy_flags.jsonl",
    "reviews/link_decisions.jsonl",
    "reviews/link_flags.jsonl",
    "reviews/needs_curator.txt",
    "pipeline/metrics-history.jsonl",
    "polishing/observations.md",
)

SESSION_LOG_RE = re.compile(r"^polishing/sessions/routine_(\d{4}-\d{2}-\d{2})_(\d{3})\.md$")
ENTRY_RE = re.compile(r"^entries/\d{5}/(\d{5})_[^/]+\.json$")
CANDIDATES = "candidate_words.json"
STATUS = "PROJECT_STATUS.md"


# --- git helpers -----------------------------------------------------------

def git(*args: str, check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, check=check,
                          capture_output=capture, text=True)


def git_out(*args: str) -> str:
    return git(*args).stdout.strip()


def show(ref: str, path: str) -> str | None:
    """Content of ``path`` at ``ref``; None if the file does not exist there."""
    r = git("show", f"{ref}:{path}", check=False)
    return r.stdout if r.returncode == 0 else None


def fetch_branch(branch: str) -> bool:
    """Fetch origin/<branch>; False (with a message) if it no longer exists on origin."""
    r = git("fetch", "origin", branch, check=False)
    if r.returncode != 0:
        print(f"{branch}: not on origin (already deleted?) — nothing to do.")
        return False
    return True


def changed_files(a: str, b: str) -> list[str]:
    out = git_out("diff", "--name-only", a, b)
    return [ln for ln in out.splitlines() if ln]


def is_generated(path: str) -> bool:
    return any(path == p or (p.endswith("/") and path.startswith(p)) for p in GENERATED_PREFIXES)


def differs(a: str, b: str, path: str) -> bool:
    return git("diff", "--quiet", a, b, "--", path, check=False).returncode != 0


# --- residue ---------------------------------------------------------------

def residue(theirs: str, ours: str = "HEAD") -> list[str]:
    """Durable files the branch changed (since it diverged) whose change ours still lacks.

    A ledger that differs only because ours has appended more lines since is
    not residue; nor is a candidate queue whose consumed and added candidates
    ours already reflects, nor a status file whose sections ours already has.
    """
    base = git_out("merge-base", ours, theirs)
    out = []
    for path in changed_files(base, theirs):
        if is_generated(path):
            continue
        if not differs(ours, theirs, path):
            continue
        ours_txt, theirs_txt, base_txt = show(ours, path), show(theirs, path), show(base, path)
        if ours_txt is not None and theirs_txt is not None:
            if path in UNION_FILES:
                if union_lines(base_txt, ours_txt, theirs_txt) == (ours_txt if ours_txt.endswith("\n") else ours_txt + "\n"):
                    continue
            elif path == CANDIDATES:
                _d, removed, to_add = reconcile_candidates(base_txt, ours_txt, theirs_txt)
                if not removed and not to_add:
                    continue
            elif path == STATUS:
                _m, new_secs = merge_status(base_txt, ours_txt, theirs_txt)
                if not new_secs:
                    continue
        out.append(path)
    return out


def entry_ids(paths: list[str]) -> list[str]:
    ids = sorted({m.group(1) for p in paths if (m := ENTRY_RE.match(p))})
    return ids


# --- per-file policies ------------------------------------------------------

def union_lines(base: str | None, ours: str, theirs: str) -> str:
    """Ours plus the lines the branch added relative to base (order kept, no duplicates)."""
    base_lines = (base or "").splitlines()
    theirs_lines = theirs.splitlines()
    ours_lines = ours.splitlines()
    added: list[str] = []
    sm = difflib.SequenceMatcher(a=base_lines, b=theirs_lines, autojunk=False)
    for tag, _i1, _i2, j1, j2 in sm.get_opcodes():
        if tag in ("insert", "replace"):
            added.extend(theirs_lines[j1:j2])
    present = set(ln for ln in ours_lines if ln.strip())
    new = [ln for ln in added if not ln.strip() or ln not in present]
    # Drop a leading blank run if ours already ends blank, and trailing blanks.
    while new and not new[0].strip() and (not ours_lines or not ours_lines[-1].strip()):
        new.pop(0)
    while new and not new[-1].strip():
        new.pop()
    if not any(ln.strip() for ln in new):
        return ours if ours.endswith("\n") or not ours else ours + "\n"
    body = ours_lines + new
    return "\n".join(body) + "\n"


def sort_metrics(text: str) -> str:
    """Keep pipeline/metrics-history.jsonl in timestamp order after a union."""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    try:
        keyed = [(json.loads(ln)["ts"], ln) for ln in lines]
    except (json.JSONDecodeError, KeyError, TypeError):
        return text
    keyed.sort(key=lambda kv: kv[0])
    return "\n".join(ln for _ts, ln in keyed) + "\n"


def next_free_log(date: str, taken: set[str]) -> str:
    existing = {p.name for p in (ROOT / "polishing" / "sessions").glob(f"routine_{date}_*.md")}
    n = 1
    while f"routine_{date}_{n:03d}.md" in existing or f"polishing/sessions/routine_{date}_{n:03d}.md" in taken:
        n += 1
    return f"polishing/sessions/routine_{date}_{n:03d}.md"


def cand_key(c: dict) -> tuple[str, str]:
    return ((c.get("word") or "").strip(), (c.get("reading") or "").strip())


def reconcile_candidates(base: str | None, ours: str, theirs: str) -> tuple[dict, list[dict], list[dict]]:
    """Ours minus the candidates the branch consumed, plus the ones it added (to re-add)."""
    base_d = json.loads(base) if base else {"candidates": []}
    ours_d = json.loads(ours)
    theirs_d = json.loads(theirs)
    base_keys = {cand_key(c) for c in base_d["candidates"]}
    theirs_keys = {cand_key(c) for c in theirs_d["candidates"]}
    consumed = base_keys - theirs_keys
    removed = [c for c in ours_d["candidates"] if cand_key(c) in consumed]
    ours_d["candidates"] = [c for c in ours_d["candidates"] if cand_key(c) not in consumed]
    ours_keys = {cand_key(c) for c in ours_d["candidates"]}
    to_add = [c for c in theirs_d["candidates"]
              if cand_key(c) not in base_keys and cand_key(c) not in ours_keys]
    ours_d["metadata"]["total_candidates"] = len(ours_d["candidates"])
    return ours_d, removed, to_add


STATUS_SECTION_RE = re.compile(r"^### (\d{4}-\d{2}-\d{2})\b")


def _recent_sections(text: str) -> tuple[list[str], list[tuple[str, str, list[str]]], list[str]]:
    """Split PROJECT_STATUS.md into (head lines, [(date, heading, lines)], tail lines)."""
    lines = text.splitlines()
    try:
        start = next(i for i, ln in enumerate(lines) if ln.strip() == "## Recent Changes")
    except StopIteration:
        return lines, [], []
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    head = lines[: start + 1]
    tail = lines[end:]
    sections: list[tuple[str, str, list[str]]] = []
    cur: list[str] | None = None
    for ln in lines[start + 1:end]:
        m = STATUS_SECTION_RE.match(ln)
        if m:
            cur = [ln]
            sections.append((m.group(1), ln, cur))
        elif cur is not None:
            cur.append(ln)
    return head, sections, tail


def merge_status(base: str | None, ours: str, theirs: str, keep: int = 5) -> tuple[str, list[str]]:
    head, ours_secs, tail = _recent_sections(ours)
    _h, theirs_secs, _t = _recent_sections(theirs)
    _h, base_secs, _t = _recent_sections(base or "")
    known = {h for _d, h, _l in ours_secs} | {h for _d, h, _l in base_secs}
    new = [s for s in theirs_secs if s[1] not in known]
    if not new:
        return ours if ours.endswith("\n") else ours + "\n", []
    merged = list(ours_secs)
    for sec in new:
        # Newest first; an absorbed run of the same date goes after main's own.
        idx = next((i for i, s in enumerate(merged) if s[0] < sec[0]), len(merged))
        merged.insert(idx, sec)
    merged = merged[:keep]
    body: list[str] = []
    for _d, _h, sec_lines in merged:
        block = list(sec_lines)
        while block and not block[-1].strip():
            block.pop()
        body.extend([""] + block)
    body.append("")
    out = head + body + tail
    return "\n".join(out).rstrip("\n") + "\n", [s[1] for s in new]


# --- main absorb ------------------------------------------------------------

def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def absorb(branch: str, pr: int | None, commit: bool) -> int:
    theirs = f"origin/{branch}"
    if git_out("status", "--porcelain"):
        print("ERROR: working tree is not clean; commit or stash first.")
        return 1
    if not fetch_branch(branch):
        return 0
    if git("merge-base", "--is-ancestor", "origin/main", "HEAD", check=False).returncode != 0:
        print("WARNING: HEAD is behind origin/main; merge origin/main first for a clean absorb.")
    base = git_out("merge-base", "HEAD", theirs)
    res = residue(theirs)
    if not res:
        print(f"{branch}: no residue against HEAD — nothing to absorb (branch can be pruned).")
        return 0
    print(f"Absorbing {branch} ({len(res)} durable files differ):")
    for p in res:
        print(f"  {p}")

    ours_entries = set(changed_files(base, "HEAD")) & set(changed_files(base, theirs))
    both_sides = sorted(p for p in ours_entries if ENTRY_RE.match(p))

    merge = git("merge", "--no-commit", "--no-ff", theirs, check=False)
    conflicted = [ln for ln in git_out("diff", "--name-only", "--diff-filter=U").splitlines() if ln]
    if merge.returncode != 0 and not conflicted:
        print(merge.stdout, merge.stderr)
        git("merge", "--abort", check=False)
        print("ERROR: merge failed for a reason other than conflicts; aborted.")
        return 1

    unresolvable: list[str] = []
    renamed: list[tuple[str, str]] = []
    taken: set[str] = set()
    notes: list[str] = []

    for path in conflicted:
        ours_txt = show("HEAD", path)
        theirs_txt = show(theirs, path)
        base_txt = show(base, path)
        if is_generated(path):
            git("checkout", "--ours", "--", path)
            git("add", "--", path)
        elif path in UNION_FILES and ours_txt is not None and theirs_txt is not None:
            merged = union_lines(base_txt, ours_txt, theirs_txt)
            if path == "pipeline/metrics-history.jsonl":
                merged = sort_metrics(merged)
            write(path, merged)
            git("add", "--", path)
            notes.append(f"union: {path}")
        elif (m := SESSION_LOG_RE.match(path)) and ours_txt is not None and theirs_txt is not None:
            new_path = next_free_log(m.group(1), taken)
            taken.add(new_path)
            header = (f"> Absorbed from branch `{branch}`"
                      + (f" (PR #{pr})" if pr else "")
                      + f" on {datetime.now(timezone.utc).strftime('%Y-%m-%d')}; "
                      + f"originally `{path}`, renamed because that number was taken on main.\n\n")
            write(new_path, header + theirs_txt)
            git("checkout", "--ours", "--", path)
            git("add", "--", path, new_path)
            renamed.append((path, new_path))
        elif path == CANDIDATES:
            # Reconciled below from ours regardless of conflict state.
            git("checkout", "--ours", "--", path)
            git("add", "--", path)
        elif path == STATUS and ours_txt is not None and theirs_txt is not None:
            merged, new_secs = merge_status(base_txt, ours_txt, theirs_txt)
            write(path, merged)
            git("add", "--", path)
            for h in new_secs:
                notes.append(f"PROJECT_STATUS.md: inserted section {h!r}")
        else:
            unresolvable.append(path)

    if unresolvable:
        git("merge", "--abort", check=False)
        print("\nABORTED: these conflicts need a person (the merge was undone):")
        for p in unresolvable:
            print(f"  {p}")
        return 2

    # Never carry the branch's stale generated files, even when they auto-merged.
    for path in changed_files(base, theirs):
        if is_generated(path) and (ROOT / path).exists() and show("HEAD", path) is not None:
            git("checkout", "HEAD", "--", path)
            git("add", "--", path)

    # Candidate queue: always rebuilt from ours.
    ours_c = show("HEAD", CANDIDATES)
    theirs_c = show(theirs, CANDIDATES)
    if ours_c and theirs_c and differs(base, theirs, CANDIDATES):
        data, removed, to_add = reconcile_candidates(show(base, CANDIDATES), ours_c, theirs_c)
        data["metadata"]["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        write(CANDIDATES, json.dumps(data, ensure_ascii=False, indent=2))
        if removed:
            notes.append("candidates removed (the branch made them entries): "
                         + ", ".join(c["word"] for c in removed))
        if to_add:
            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tf:
                json.dump([{"word": c["word"], "reading": c.get("reading", ""),
                            "notes": c.get("notes", "")} for c in to_add], tf, ensure_ascii=False)
                batch = tf.name
            r = subprocess.run([sys.executable, "build/manage_candidates.py", "add-batch", batch],
                               cwd=ROOT, capture_output=True, text=True)
            Path(batch).unlink(missing_ok=True)
            notes.append("candidates re-queued from the branch (fresh IDs):\n    "
                         + r.stdout.strip().replace("\n", "\n    "))
        git("add", "--", CANDIDATES)

    # A colliding session log can also arrive without a conflict when the name is
    # free on ours but another absorbed branch already took it; nothing to do then.

    if commit:
        subject = git_out("log", "-1", "--format=%s", theirs).split("\n")[0]
        msg = f"absorb {branch}" + (f" (PR #{pr})" if pr else "") + f": {subject}"
        git("commit", "--no-verify", "-m", msg)
        print(f"\nCommitted: {msg}")
    else:
        print("\nMerge staged but not committed (--no-commit).")

    for old, new in renamed:
        print(f"session log renamed: {old} -> {new}")
    for n in notes:
        print(n)
    ids = entry_ids(res)
    if ids:
        print(f"\nEntries the branch brings ({len(ids)}): {' '.join(ids)}")
    if both_sides:
        print(f"Entries changed on BOTH sides since the branch diverged ({len(both_sides)}) — "
              f"auto-merged, read and validate them:")
        for p in both_sides:
            print(f"  {p}")
    print("\nNext: make gate; fix what it reports. Then make index: if it reports a kanji needing an ID,"
          " the branch introduced a new kanji — add it to kanji/kanji_list.json with the next free ID"
          " (the branch's own assignment was discarded with its generated files) and rerun.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("branch", help="branch name without the origin/ prefix, e.g. claude/trusting-mendel-o9cv7c")
    ap.add_argument("--residue", action="store_true", help="only report durable files that differ from HEAD")
    ap.add_argument("--pr", type=int, help="the branch's PR number, for the commit message and log header")
    ap.add_argument("--no-commit", action="store_true", help="leave the resolved merge staged, uncommitted")
    args = ap.parse_args()
    branch = args.branch.removeprefix("origin/")
    if args.residue:
        if not fetch_branch(branch):
            return 0
        res = residue(f"origin/{branch}")
        if not res:
            print(f"{branch}: no residue (fully absorbed).")
        else:
            print(f"{branch}: {len(res)} durable file(s) differ from HEAD:")
            for p in res:
                print(f"  {p}")
            ids = entry_ids(res)
            if ids:
                print(f"entries: {' '.join(ids)}")
        return 0
    return absorb(branch, args.pr, not args.no_commit)


if __name__ == "__main__":
    sys.exit(main())
