#!/usr/bin/env python3
"""Close stranded Routine PRs and sweep orphan claude/* branches.

A "stranded" PR is one created by a previous Claude Code session
(`claude/*` head branch) that never got merged — typically because
the session ended before reaching the merge step. If a later session
covered the same range and merged successfully, the older PR is
obsolete. This script detects that and cleans up.

An "orphan" branch is a pushed `claude/*` branch with no open PR at
all — either its session died before create_pull_request (the
2026-08-07 GitHub-API outage produced exactly this), or its PR was
closed unmerged and the branch lingered (branch auto-delete only fires
on merge). Orphans are invisible to any PR-based check, so they are
swept separately, by content:

  - "absorbed" — every durable file the branch changed is byte-identical
    on main now, or its exact blob appeared somewhere in main's history
    (carried over by a later run's squash-merge, evolved since). The
    branch is a dead leftover: delete it.
  - otherwise — the branch holds real unmerged work. Never delete it;
    print an ACTION-REQUIRED line telling the curator to either open a
    rescue PR for it (never-PR'd work) or make a call on it (a
    closed-unmerged PR is a decision someone already took once).

Durability is defined by the GENERATED_*/VOLATILE_* constants below:
build artifacts are rebuilt by `make build` and per-run state files are
superseded by every later merge, so neither blocks deletion. These
constants are the authoritative path lists — the MCP-path instructions
in CLAUDE.md ("Sweep orphan claude/* branches via MCP") defer to them.
The absorption test needs a local git clone (run from the repo).

Stranded-PR algorithm:
  1. Read polishing/tasks/comprehensive/progress.txt from main via API.
  2. List open PRs in the repo.
  3. For each PR whose head branch matches `claude/*`:
       - List the files it touches.
       - Compute the maximum entry ID among entries/*/NNNNN_*.json files.
       - If that max is strictly less than the next: value on main,
         the PR is fully superseded — comment, close, and delete the branch.
  4. PRs that don't touch entry files, or that include any entry at or
     above the next: cursor, are left untouched.
  5. Then the orphan-branch sweep described above.

Designed to be run as the first step of a Routine session so stranded
branches don't accumulate. Idempotent: a second run sees no stranded
PRs left to close. When run from inside an active session, that
session's own not-yet-PR'd branch will show up as an orphan with live
work — an ACTION-REQUIRED report line, never a deletion.

Requires GITHUB_TOKEN and direct api.github.com access. In the Routine / web
execution environment direct REST is blocked (HTTP 403 "GitHub access is not
enabled for this session"); there this script is a clean no-op and the Routine
sweeps via the GitHub MCP server instead (CLAUDE.md -> "Sweep stranded PRs via
MCP", routine2.md §0b). It still works in interactive sessions where a real
token + direct REST are available.

Usage:
  python3 pipeline/sweep-stranded-prs.py            # close + delete
  python3 pipeline/sweep-stranded-prs.py --dry-run  # report only

Exit codes:
  0  ran to completion (zero or more PRs closed), OR direct REST is blocked here
     (no-op — message on stderr)
  3  GITHUB_TOKEN missing or progress.txt unreadable
"""

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

REPO = "tkgally/je-dict-1"
API = f"https://api.github.com/repos/{REPO}"
ENTRY_PATH_RE = re.compile(r"^entries/\d+/(\d{5})_[a-z_]+\.json$")
PROGRESS_PATH = "polishing/tasks/comprehensive/progress.txt"
PROGRESS_RE = re.compile(r"^\s*next:\s*(\d{5})\s*$", re.MULTILINE)
HEAD_PREFIX = "claude/"


class DirectApiBlocked(Exception):
    """The agent proxy refused a direct GitHub REST call (HTTP 403 policy).

    In the Routine / web execution environment, direct api.github.com access is
    not provided — the proxy returns 403 "GitHub access is not enabled for this
    session". Only the GitHub MCP server reaches GitHub there, so the Routine
    runs this sweep via MCP instead (CLAUDE.md → "Sweep stranded PRs via MCP").
    """


def gh_api(path, method="GET", data=None):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("error: GITHUB_TOKEN is not set", file=sys.stderr)
        sys.exit(3)
    url = f"{API}{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    body = json.dumps(data).encode() if data is not None else None
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            text = resp.read().decode()
            if resp.status == 204 or not text:
                return None
            return json.loads(text)
    except urllib.error.HTTPError as e:
        if e.code == 403:
            err_body = ""
            try:
                err_body = e.read().decode()
            except Exception:
                pass
            if "access is not enabled" in err_body:
                raise DirectApiBlocked(err_body) from None
        raise


def get_progress_next_from_main():
    data = gh_api(f"/contents/{PROGRESS_PATH}?ref=main")
    text = base64.b64decode(data["content"]).decode()
    m = PROGRESS_RE.search(text)
    if not m:
        print(f"error: cannot parse next: from {PROGRESS_PATH} on main", file=sys.stderr)
        sys.exit(3)
    return int(m.group(1))


def list_open_prs():
    prs = []
    page = 1
    while True:
        chunk = gh_api(f"/pulls?state=open&per_page=100&page={page}")
        if not chunk:
            break
        prs.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1
    return prs


def list_pr_files(pr_number):
    files = []
    page = 1
    while True:
        chunk = gh_api(f"/pulls/{pr_number}/files?per_page=100&page={page}")
        if not chunk:
            break
        files.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1
    return files


def pr_max_entry_id(pr_number):
    ids = []
    for f in list_pr_files(pr_number):
        m = ENTRY_PATH_RE.match(f["filename"])
        if m:
            ids.append(int(m.group(1)))
    return max(ids) if ids else None


def close_pr(pr_number, comment):
    gh_api(f"/issues/{pr_number}/comments", method="POST", data={"body": comment})
    gh_api(f"/pulls/{pr_number}", method="PATCH", data={"state": "closed"})


def delete_branch(branch):
    gh_api(f"/git/refs/heads/{branch}", method="DELETE")


# --- Orphan-branch sweep -----------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Authoritative durability lists (the MCP-path sweep in CLAUDE.md defers here).
# Generated paths are rebuilt from source by `make build`; volatile paths are
# per-run state or append streams that every later merge to main supersedes.
# Everything else — entries, articles, build code and data, prompts, planning,
# session logs, workflows, skills, root docs — is durable: a branch may only be
# deleted when all of its durable changes are provably on main.
GENERATED_PREFIXES = ("docs/", "kanji/")
GENERATED_EXACT = {"entries_index.json", "build/word_id_lookup.json"}
VOLATILE_PREFIXES = ("pipeline/logs/", "polishing/tasks/", "polishing/priority/", "reviews/")
VOLATILE_EXACT = {
    "candidate_words.json",
    "polishing/observations.md",
    "pipeline/routine-state.json",
    "pipeline/openrouter-ledger.json",
    "pipeline/metrics-history.jsonl",
    "pipeline/budget.json",
    "pipeline/task_queue.json",
    "PROJECT_CONTEXT_BRIEF.md",
    "PROJECT_STATUS.md",
}


def is_durable(path):
    if path.startswith(GENERATED_PREFIXES) or path in GENERATED_EXACT:
        return False
    if path.startswith(VOLATILE_PREFIXES) or path in VOLATILE_EXACT:
        return False
    return True


def _git(*args):
    return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True)


def branch_absorption(branch):
    """Classify a branch's durable content against main.

    Returns (verdict, residue): verdict is "absorbed" (safe to delete),
    "live" (residue lists durable files whose branch content never reached
    main), or "unverifiable" (no usable local clone — never delete).
    """
    if _git("rev-parse", "--is-inside-work-tree").returncode != 0:
        return "unverifiable", []
    if _git("fetch", "origin", "main", branch).returncode != 0:
        return "unverifiable", []
    ref = f"origin/{branch}"
    mb = _git("merge-base", "origin/main", ref)
    if mb.returncode != 0:
        return "unverifiable", []
    changed = _git("diff", "--name-status", mb.stdout.strip(), ref)
    residue = []
    for line in changed.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status, path = parts[0], parts[-1]
        if not is_durable(path):
            continue
        if status.startswith(("D", "R")):
            # Deletions/renames of durable files: never auto-judge.
            residue.append(f"{path} ({status})")
            continue
        # Identical on main right now?
        if _git("diff", "--quiet", "origin/main", ref, "--", path).returncode == 0:
            continue
        # Or did this exact blob land on main at some point (absorbed by a
        # later run's squash, evolved further since)?
        blob = _git("rev-parse", f"{ref}:{path}")
        if blob.returncode == 0:
            seen = _git("log", "-n", "1", "--format=%H",
                        f"--find-object={blob.stdout.strip()}", "origin/main")
            if seen.returncode == 0 and seen.stdout.strip():
                continue
        residue.append(path)
    return ("absorbed" if not residue else "live"), residue


def list_claude_branches():
    names = []
    page = 1
    while True:
        chunk = gh_api(f"/branches?per_page=100&page={page}")
        if not chunk:
            break
        names.extend(b["name"] for b in chunk)
        if len(chunk) < 100:
            break
        page += 1
    return [n for n in names if n.startswith(HEAD_PREFIX)]


def branch_pr_history(branch):
    owner = REPO.split("/")[0]
    return gh_api(f"/pulls?head={owner}:{branch}&state=all&per_page=10") or []


def sweep_orphan_branches(open_prs, dry_run):
    open_heads = {pr["head"]["ref"] for pr in open_prs}
    orphans = [b for b in list_claude_branches() if b not in open_heads]
    print(f"{len(orphans)} claude/* branch(es) without an open PR")
    deleted = 0
    for branch in orphans:
        verdict, residue = branch_absorption(branch)
        if verdict == "unverifiable":
            print(f"  ?? {branch}: no usable local clone to verify absorption — leaving alone")
            continue
        if verdict == "absorbed":
            print(f"  absorbed {branch}: every durable file it changed is on main — deleting")
            if dry_run:
                continue
            try:
                delete_branch(branch)
                deleted += 1
            except urllib.error.HTTPError as e:
                print(f"    failed to delete {branch}: HTTP {e.code}", file=sys.stderr)
            continue
        shown = ", ".join(residue[:5]) + ("…" if len(residue) > 5 else "")
        history = branch_pr_history(branch)
        if history:
            print(f"  ACTION-REQUIRED {branch}: durable content not on main, but PR #{history[0]['number']} "
                  f"was already closed unmerged — that decision is the curator's to revisit. Residue: {shown}")
        else:
            print(f"  ACTION-REQUIRED {branch}: pushed but never had a PR, and its durable content is not "
                  f"on main — open a rescue PR for it or delete it deliberately. Residue: {shown}")
    print(f"deleted {deleted} absorbed orphan branch(es)")
    return deleted


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--dry-run", action="store_true", help="report what would be closed without modifying anything")
    args = parser.parse_args()

    next_id = get_progress_next_from_main()
    print(f"main progress.txt next: {next_id:05d}")

    prs = list_open_prs()
    candidate_prs = [pr for pr in prs if pr["head"]["ref"].startswith(HEAD_PREFIX)]
    print(f"{len(prs)} open PR(s) total, {len(candidate_prs)} on {HEAD_PREFIX}* branches")

    closed = 0
    for pr in candidate_prs:
        head_ref = pr["head"]["ref"]
        number = pr["number"]
        title = pr["title"]
        max_id = pr_max_entry_id(number)
        if max_id is None:
            print(f"  skip #{number} ({head_ref}): no entry files touched — {title}")
            continue
        if max_id >= next_id:
            print(f"  keep #{number} ({head_ref}): max_id={max_id:05d} >= next={next_id:05d}")
            continue
        print(f"  stranded #{number} ({head_ref}): max_id={max_id:05d} < next={next_id:05d} — {title}")
        if args.dry_run:
            continue
        comment = (
            f"Superseded — main has advanced past this PR's entry range "
            f"(`progress.txt` next: `{next_id:05d}`, max entry ID in this PR: `{max_id:05d}`). "
            f"Closing automatically and deleting the branch. "
            f"Reopen and rebase if any change here should be reapplied."
        )
        try:
            close_pr(number, comment)
            delete_branch(head_ref)
            closed += 1
        except urllib.error.HTTPError as e:
            print(f"    failed to clean up #{number}: HTTP {e.code} {e.read().decode()[:200]}", file=sys.stderr)
    print(f"closed {closed} stranded PR(s)")

    sweep_orphan_branches(prs, args.dry_run)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except DirectApiBlocked:
        print(
            "sweep-stranded-prs.py: direct GitHub REST is blocked here (HTTP 403 "
            "'GitHub access is not enabled for this session'); this script is a "
            "no-op in this environment, not an error.\n"
            "The Routine sweeps stranded PRs via the GitHub MCP server instead — "
            "see CLAUDE.md → 'Sweep stranded PRs via MCP' and routine2.md §0b. "
            "No action taken.",
            file=sys.stderr,
        )
        sys.exit(0)
