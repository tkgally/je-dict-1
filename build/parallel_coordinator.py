#!/usr/bin/env python3
"""
Coordinate parallel session results into a single clean merge.

After two or more parallel sessions have completed (each on its own branch
with only entry-file changes committed), this script:
1. Validates that the branches modify non-overlapping entry files
2. Merges each branch into the current branch
3. Runs shared-file regeneration (update_indexes, build_flat, etc.)
4. Reports the combined result

Usage:
    python3 build/parallel_coordinator.py branch1 branch2 [branch3 ...]
    python3 build/parallel_coordinator.py --dry-run branch1 branch2
    python3 build/parallel_coordinator.py --validate-only branch1 branch2
"""

import argparse
import subprocess
import sys
from collections import defaultdict


def run_git(args, check=True, capture=True):
    """Run a git command and return the result."""
    cmd = ["git"] + args
    result = subprocess.run(cmd, capture_output=capture, text=True, check=check)
    return result


def get_branch_entry_files(branch):
    """Get list of entry files modified by a branch relative to main."""
    try:
        result = run_git(["diff", "--name-only", f"main...{branch}", "--", "entries/"])
        return [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
    except subprocess.CalledProcessError:
        return None


def get_branch_all_files(branch):
    """Get all files modified by a branch relative to main."""
    try:
        result = run_git(["diff", "--name-only", f"main...{branch}"])
        return [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
    except subprocess.CalledProcessError:
        return None


def check_working_tree_clean():
    """Check that the working tree is clean."""
    result = run_git(["status", "--porcelain"])
    return result.stdout.strip() == ""


def branch_exists(branch):
    """Check if a branch exists locally or as a remote tracking branch."""
    try:
        run_git(["rev-parse", "--verify", branch])
        return True
    except subprocess.CalledProcessError:
        # Try remote
        try:
            run_git(["rev-parse", "--verify", f"origin/{branch}"])
            return True
        except subprocess.CalledProcessError:
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Coordinate parallel session branches."
    )
    parser.add_argument("branches", nargs="+", help="Branch names to merge")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be done without making changes")
    parser.add_argument("--validate-only", action="store_true",
                        help="Check for conflicts without merging")
    parser.add_argument("--skip-build", action="store_true",
                        help="Skip the build step after merging")

    args = parser.parse_args()

    # Step 1: Validate branches
    print("=== STEP 1: Validating branches ===\n")

    branch_files = {}
    missing_branches = []

    for branch in args.branches:
        if not branch_exists(branch):
            print(f"ERROR: Branch '{branch}' does not exist.")
            missing_branches.append(branch)
            continue

        entry_files = get_branch_entry_files(branch)
        if entry_files is None:
            print(f"ERROR: Could not get diff for branch '{branch}'.")
            missing_branches.append(branch)
            continue

        all_files = get_branch_all_files(branch)
        non_entry_files = [
            f for f in (all_files or [])
            if not f.startswith("entries/") and not f.startswith("polishing/sessions/")
        ]
        if non_entry_files:
            print(f"WARNING: Branch '{branch}' modifies files outside entries/ "
                  f"and polishing/sessions/:")
            for f in non_entry_files:
                print(f"  {f}")

        branch_files[branch] = entry_files
        print(f"  {branch}: {len(entry_files)} entry files modified")

    if missing_branches:
        print(f"\nERROR: {len(missing_branches)} branch(es) not found. Aborting.")
        sys.exit(1)

    # Check for overlapping entry files
    file_to_branches = defaultdict(list)
    for branch, files in branch_files.items():
        for f in files:
            file_to_branches[f].append(branch)

    conflicts = {f: branches for f, branches in file_to_branches.items()
                 if len(branches) > 1}

    if conflicts:
        print("\nERROR: Overlapping entry files detected:")
        for f, branches in sorted(conflicts.items()):
            print(f"  {f}: modified by {', '.join(branches)}")
        print("\nAborting — resolve overlaps before coordinating.")
        sys.exit(1)

    print("\nNo overlapping entry files. Safe to merge.")

    if args.validate_only:
        print("\n--validate-only: stopping after validation.")
        sys.exit(0)

    if args.dry_run:
        print("\n--dry-run: would merge the following branches:")
        for branch, files in branch_files.items():
            print(f"  {branch}: {len(files)} entry files")
        total = sum(len(f) for f in branch_files.values())
        print(f"  Total: {total} entry files")
        print("  Then regenerate shared files (indexes, site build).")
        sys.exit(0)

    # Step 2: Merge branches
    print("\n=== STEP 2: Merging branches ===\n")

    if not check_working_tree_clean():
        print("ERROR: Working tree is not clean. Commit or stash changes first.")
        sys.exit(1)

    for branch in args.branches:
        if branch not in branch_files:
            continue
        print(f"Merging {branch}...")
        try:
            run_git(["merge", "--no-ff", branch,
                     "-m", f"Merge parallel session: {branch}"])
            print(f"  Merged successfully.")
        except subprocess.CalledProcessError:
            print(f"\nERROR: Merge conflict while merging '{branch}'.")
            print("Aborting merge. Resolve conflicts manually.")
            run_git(["merge", "--abort"], check=False)
            sys.exit(1)

    # Step 3: Regenerate shared files
    if args.skip_build:
        print("\n--skip-build: skipping shared-file regeneration.")
    else:
        print("\n=== STEP 3: Regenerating shared files ===\n")

        build_steps = [
            (["python3", "build/validate.py"], "Validating entries"),
            (["python3", "build/update_indexes.py"], "Updating indexes"),
            (["python3", "build/update_kanji_index.py", "--check-new"],
             "Checking kanji index"),
            (["python3", "build/build_flat.py"], "Building site"),
        ]

        for cmd, description in build_steps:
            print(f"  {description}...")
            try:
                subprocess.run(cmd, check=True, capture_output=True, text=True)
                print(f"    Done.")
            except subprocess.CalledProcessError as e:
                print(f"\nERROR during '{description}':")
                if e.stdout:
                    print(e.stdout)
                if e.stderr:
                    print(e.stderr)
                print("Fix the error and re-run the build manually.")
                sys.exit(1)

    # Step 4: Report
    total_files = sum(len(f) for f in branch_files.values())
    print(f"\n=== PARALLEL COORDINATION COMPLETE ===")
    print(f"Branches merged: {len(branch_files)}")
    for branch, files in branch_files.items():
        print(f"  - {branch}: {len(files)} entries modified")
    print(f"Total entries modified: {total_files}")
    if not args.skip_build:
        print(f"Shared files regenerated: yes")
    else:
        print(f"Shared files regenerated: no (--skip-build)")

    # Step 5: Stage and instruct
    print()
    run_git(["add", "-A"])
    print("All changes staged. Review with 'git diff --cached' and commit:")
    print(f'  git commit -m "Coordinated merge of {len(branch_files)} parallel sessions"')


if __name__ == "__main__":
    main()
