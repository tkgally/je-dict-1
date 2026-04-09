#!/usr/bin/env python3
"""
Advisory entry-level locking for parallel dictionary sessions.

Provides a lightweight mechanism to signal which entry ranges are being
worked on by active sessions. Locks are advisory — they help prevent
accidental overlap but do not block execution.

Usage:
    python3 build/entry_lock.py lock --range 10000 10499 --session "inline-links-session-1"
    python3 build/entry_lock.py unlock --range 10000 10499 --session "inline-links-session-1"
    python3 build/entry_lock.py check --range 10000 10499
    python3 build/entry_lock.py status
    python3 build/entry_lock.py clean
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

LOCKS_DIR = Path("polishing/locks")
LOCK_EXPIRY_MINUTES = 30


def get_lock_path(range_start, range_end, session_id):
    return LOCKS_DIR / f"{range_start}_{range_end}_{session_id}.lock"


def parse_lock_file(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def is_expired(lock_data):
    expires_at = datetime.fromisoformat(lock_data["expires_at"])
    return datetime.now(timezone.utc) > expires_at


def ranges_overlap(a_start, a_end, b_start, b_end):
    return a_start <= b_end and b_start <= a_end


def get_all_locks():
    """Return list of (path, lock_data) for all lock files."""
    if not LOCKS_DIR.exists():
        return []
    locks = []
    for f in LOCKS_DIR.glob("*.lock"):
        data = parse_lock_file(f)
        if data:
            locks.append((f, data))
    return locks


def get_active_locks():
    """Return list of (path, lock_data) for non-expired locks."""
    return [(p, d) for p, d in get_all_locks() if not is_expired(d)]


def format_time_remaining(lock_data):
    expires_at = datetime.fromisoformat(lock_data["expires_at"])
    remaining = expires_at - datetime.now(timezone.utc)
    if remaining.total_seconds() <= 0:
        return "expired"
    minutes = int(remaining.total_seconds() // 60)
    seconds = int(remaining.total_seconds() % 60)
    return f"{minutes}m {seconds}s remaining"


def cmd_lock(args):
    LOCKS_DIR.mkdir(parents=True, exist_ok=True)

    range_start, range_end = args.range
    session_id = args.session

    # Check for overlapping active locks
    for _, lock_data in get_active_locks():
        if ranges_overlap(range_start, range_end,
                          lock_data["range_start"], lock_data["range_end"]):
            print(f"WARNING: Overlapping lock found — "
                  f"session '{lock_data['session_id']}' holds "
                  f"{lock_data['range_start']}-{lock_data['range_end']} "
                  f"({format_time_remaining(lock_data)})")

    now = datetime.now(timezone.utc)
    lock_data = {
        "range_start": range_start,
        "range_end": range_end,
        "session_id": session_id,
        "locked_at": now.isoformat(),
        "expires_at": (now + timedelta(minutes=LOCK_EXPIRY_MINUTES)).isoformat(),
    }

    lock_path = get_lock_path(range_start, range_end, session_id)
    with open(lock_path, "w") as f:
        json.dump(lock_data, f, indent=2)
        f.write("\n")

    print(f"Locked range {range_start}-{range_end} for session '{session_id}' "
          f"(expires in {LOCK_EXPIRY_MINUTES} minutes)")


def cmd_unlock(args):
    range_start, range_end = args.range
    session_id = args.session

    lock_path = get_lock_path(range_start, range_end, session_id)
    if lock_path.exists():
        lock_path.unlink()
        print(f"Unlocked range {range_start}-{range_end} for session '{session_id}'")
    else:
        print(f"WARNING: No matching lock found for range {range_start}-{range_end} "
              f"session '{session_id}'")


def cmd_check(args):
    range_start, range_end = args.range
    overlaps = []

    for _, lock_data in get_active_locks():
        if ranges_overlap(range_start, range_end,
                          lock_data["range_start"], lock_data["range_end"]):
            overlaps.append(lock_data)

    if overlaps:
        print(f"Active locks overlapping with {range_start}-{range_end}:")
        for lock_data in overlaps:
            print(f"  Session '{lock_data['session_id']}': "
                  f"{lock_data['range_start']}-{lock_data['range_end']} "
                  f"({format_time_remaining(lock_data)})")
        sys.exit(1)
    else:
        print(f"No active locks overlapping with {range_start}-{range_end}")
        sys.exit(0)


def cmd_status(args):
    active = get_active_locks()
    if not active:
        print("No active locks.")
        return

    print(f"Active locks ({len(active)}):")
    for _, lock_data in sorted(active, key=lambda x: x[1]["range_start"]):
        print(f"  {lock_data['range_start']}-{lock_data['range_end']}: "
              f"session '{lock_data['session_id']}' "
              f"({format_time_remaining(lock_data)})")


def cmd_clean(args):
    all_locks = get_all_locks()
    cleaned = 0
    for path, lock_data in all_locks:
        if is_expired(lock_data):
            path.unlink()
            cleaned += 1

    print(f"Cleaned {cleaned} expired lock(s).")


def main():
    parser = argparse.ArgumentParser(
        description="Advisory entry-level locking for parallel dictionary sessions."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # lock
    lock_parser = subparsers.add_parser("lock", help="Lock an entry range")
    lock_parser.add_argument("--range", nargs=2, type=int, required=True,
                             metavar=("START", "END"),
                             help="Entry ID range (inclusive)")
    lock_parser.add_argument("--session", required=True,
                             help="Session identifier")

    # unlock
    unlock_parser = subparsers.add_parser("unlock", help="Unlock an entry range")
    unlock_parser.add_argument("--range", nargs=2, type=int, required=True,
                               metavar=("START", "END"),
                               help="Entry ID range (inclusive)")
    unlock_parser.add_argument("--session", required=True,
                               help="Session identifier")

    # check
    check_parser = subparsers.add_parser("check",
                                         help="Check for overlapping locks")
    check_parser.add_argument("--range", nargs=2, type=int, required=True,
                              metavar=("START", "END"),
                              help="Entry ID range to check")

    # status
    subparsers.add_parser("status", help="List all active locks")

    # clean
    subparsers.add_parser("clean", help="Remove expired lock files")

    args = parser.parse_args()

    commands = {
        "lock": cmd_lock,
        "unlock": cmd_unlock,
        "check": cmd_check,
        "status": cmd_status,
        "clean": cmd_clean,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
