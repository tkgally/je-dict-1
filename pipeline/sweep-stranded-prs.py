#!/usr/bin/env python3
"""Close stranded Routine PRs whose entry range is already on main.

A "stranded" PR is one created by a previous Claude Code session
(`claude/*` head branch) that never got merged — typically because
the session ended before reaching the merge step. If a later session
covered the same range and merged successfully, the older PR is
obsolete. This script detects that and cleans up.

Algorithm:
  1. Read polishing/tasks/comprehensive/progress.txt from main via API.
  2. List open PRs in the repo.
  3. For each PR whose head branch matches `claude/*`:
       - List the files it touches.
       - Compute the maximum entry ID among entries/*/NNNNN_*.json files.
       - If that max is strictly less than the next: value on main,
         the PR is fully superseded — comment, close, and delete the branch.
  4. PRs that don't touch entry files, or that include any entry at or
     above the next: cursor, are left untouched.

Designed to be run as the first step of a Routine session so stranded
branches don't accumulate. Idempotent: a second run sees no stranded
PRs left to close.

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
