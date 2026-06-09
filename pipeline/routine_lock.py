#!/usr/bin/env python3
"""Advisory single-run lock for the unified improvement Routine.

Guards against two Routine runs overlapping (e.g. a long scheduled run still
going when the next trigger fires, or a manual run launched alongside a
scheduled one). The lock is advisory and self-expiring: a lock older than the
timeout (default 2 h) is treated as stale and overwritten.

Usage:
    python3 pipeline/routine_lock.py acquire --session <id>   # exit 0 ok, 1 if held
    python3 pipeline/routine_lock.py release --session <id>
    python3 pipeline/routine_lock.py status
    python3 pipeline/routine_lock.py clean                    # remove if stale

Exit codes for `acquire`: 0 = acquired (or stale lock reclaimed), 1 = a fresh
lock is held by another run (caller should stop).
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

LOCK_FILE = Path(__file__).resolve().parent / "routine.lock"
DEFAULT_TIMEOUT = 7200  # seconds (2 hours)


def _read():
    try:
        return json.loads(LOCK_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _age(lock):
    return time.time() - float(lock.get("acquired_at", 0))


def acquire(session, timeout, force):
    existing = _read()
    if existing and not force and _age(existing) < timeout:
        print(f"BLOCKED: routine.lock held by session "
              f"{existing.get('session')!r}, age {_age(existing):.0f}s "
              f"(< timeout {timeout}s). Another run appears active.")
        return 1
    if existing and _age(existing) >= timeout:
        print(f"Reclaiming stale lock (age {_age(existing):.0f}s "
              f">= timeout {timeout}s).")
    LOCK_FILE.write_text(json.dumps({
        "session": session,
        "pid": os.getpid(),
        "acquired_at": time.time(),
        "acquired_at_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }, indent=2) + "\n", encoding="utf-8")
    print(f"ACQUIRED routine.lock for session {session!r}.")
    return 0


def release(session):
    existing = _read()
    if not existing:
        print("No lock to release.")
        return 0
    if session and existing.get("session") not in (session, None):
        print(f"WARNING: lock held by {existing.get('session')!r}, not "
              f"{session!r}; releasing anyway.")
    LOCK_FILE.unlink(missing_ok=True)
    print("RELEASED routine.lock.")
    return 0


def status():
    existing = _read()
    if not existing:
        print("No active lock.")
        return 0
    print(f"Lock held by session {existing.get('session')!r}, "
          f"pid {existing.get('pid')}, age {_age(existing):.0f}s "
          f"(acquired {existing.get('acquired_at_iso')}).")
    return 0


def clean(timeout):
    existing = _read()
    if existing and _age(existing) >= timeout:
        LOCK_FILE.unlink(missing_ok=True)
        print(f"Removed stale lock (age {_age(existing):.0f}s).")
    else:
        print("No stale lock to remove.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Advisory single-run Routine lock.")
    ap.add_argument("action", choices=["acquire", "release", "status", "clean"])
    ap.add_argument("--session", default="routine", help="Session id (e.g. branch name).")
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                    help="Stale-lock timeout in seconds (default 7200).")
    ap.add_argument("--force", action="store_true", help="Overwrite any existing lock.")
    args = ap.parse_args()

    if args.action == "acquire":
        return acquire(args.session, args.timeout, args.force)
    if args.action == "release":
        return release(args.session)
    if args.action == "status":
        return status()
    if args.action == "clean":
        return clean(args.timeout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
