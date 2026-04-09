#!/usr/bin/env python3
"""Real-time monitoring dashboard for the orchestration system.

Shows queue status, active sessions, throughput, budget, error rate,
and recent activity.

Usage:
    python3 pipeline/monitor.py          # Formatted terminal report
    python3 pipeline/monitor.py --json   # Machine-readable output
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
QUEUE_FILE = SCRIPT_DIR / "task_queue.json"
BUDGET_FILE = SCRIPT_DIR / "budget.json"
LOCK_FILE = SCRIPT_DIR / "orchestrator.lock"
LOGS_DIR = SCRIPT_DIR / "logs"


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load_json(path: Path) -> dict | None:
    """Load a JSON file, return None on failure."""
    if not path.exists():
        return None
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def get_queue_status() -> dict:
    """Get task queue status by type."""
    data = load_json(QUEUE_FILE)
    if not data:
        return {"available": False}

    tasks = data.get("tasks", [])
    types: dict[str, dict[str, int]] = {}

    for task in tasks:
        tt = task["task_type"]
        if tt not in types:
            types[tt] = {"pending": 0, "in_progress": 0, "completed": 0}
        status = task["status"]
        if status in types[tt]:
            types[tt][status] += 1

    total_pending = sum(t["pending"] for t in types.values())
    total_in_progress = sum(t["in_progress"] for t in types.values())
    total_completed = sum(t["completed"] for t in types.values())

    return {
        "available": True,
        "by_type": types,
        "total_pending": total_pending,
        "total_in_progress": total_in_progress,
        "total_completed": total_completed,
        "total": total_pending + total_in_progress + total_completed,
        "last_populated": data.get("metadata", {}).get("last_populated"),
    }


def get_active_sessions() -> list[dict]:
    """Get currently in-progress sessions from the queue."""
    data = load_json(QUEUE_FILE)
    if not data:
        return []

    sessions: dict[str, dict] = {}
    for task in data.get("tasks", []):
        if task["status"] == "in_progress" and task.get("claimed_by"):
            sid = task["claimed_by"]
            if sid not in sessions:
                sessions[sid] = {
                    "session_id": sid,
                    "entry_ids": [],
                    "claimed_at": task.get("claimed_at"),
                    "task_type": task["task_type"],
                }
            sessions[sid]["entry_ids"].append(task["entry_id"])

    return list(sessions.values())


def get_throughput() -> dict:
    """Calculate entries processed per hour from completed tasks."""
    data = load_json(QUEUE_FILE)
    if not data:
        return {"entries_per_hour": 0.0, "sample_window_hours": 0}

    now = datetime.now(timezone.utc)
    windows = [1, 6, 24]
    rates = {}

    for hours in windows:
        cutoff = now - timedelta(hours=hours)
        count = 0
        for task in data.get("tasks", []):
            if task["status"] == "completed" and task.get("completed_at"):
                try:
                    completed = datetime.fromisoformat(
                        task["completed_at"].replace("Z", "+00:00")
                    )
                    if completed >= cutoff:
                        count += 1
                except (ValueError, AttributeError):
                    pass
        rates[f"{hours}h"] = round(count / hours, 1) if hours else 0

    return rates


def get_budget_status() -> dict:
    """Get current budget information."""
    budget = load_json(BUDGET_FILE)
    if not budget:
        return {"available": False}

    # Reset if new day
    if budget.get("last_reset") != today_str():
        return {
            "available": True,
            "spent_today_usd": 0.0,
            "daily_limit_usd": budget.get("daily_limit_usd", 50.0),
            "sessions_today": 0,
            "remaining_usd": budget.get("daily_limit_usd", 50.0),
        }

    limit = budget.get("daily_limit_usd", 50.0)
    spent = budget.get("spent_today_usd", 0.0)
    sessions = len(budget.get("session_log", []))

    return {
        "available": True,
        "spent_today_usd": spent,
        "daily_limit_usd": limit,
        "sessions_today": sessions,
        "remaining_usd": max(0, limit - spent),
    }


def get_error_rate() -> dict:
    """Calculate error rate from log files."""
    if not LOGS_DIR.exists():
        return {"total_sessions": 0, "failed_sessions": 0, "error_rate": 0.0}

    today = today_str()
    total = 0
    failed = 0

    for log_file in LOGS_DIR.glob(f"*_{today}*.log"):
        if log_file.name.startswith("orchestrator_"):
            continue
        total += 1
        # Check if log contains error indicators
        try:
            content = log_file.read_text(errors="replace")
            if "Error" in content or "FAILED" in content or "exit code" in content:
                failed += 1
        except IOError:
            pass

    rate = (failed / total * 100) if total else 0.0

    return {
        "total_sessions": total,
        "failed_sessions": failed,
        "error_rate": round(rate, 1),
    }


def get_recent_activity() -> list[dict]:
    """Get the last 10 completed session logs."""
    budget = load_json(BUDGET_FILE)
    if not budget:
        return []

    session_log = budget.get("session_log", [])
    return session_log[-10:]


def get_orchestrator_status() -> dict:
    """Check if the orchestrator is running."""
    if not LOCK_FILE.exists():
        return {"running": False}
    try:
        pid = int(LOCK_FILE.read_text().strip())
        os.kill(pid, 0)
        return {"running": True, "pid": pid}
    except (ValueError, ProcessLookupError, PermissionError):
        return {"running": False, "stale_lock": True}


def build_report() -> dict:
    """Build the full monitoring report."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "orchestrator": get_orchestrator_status(),
        "queue": get_queue_status(),
        "active_sessions": get_active_sessions(),
        "throughput": get_throughput(),
        "budget": get_budget_status(),
        "error_rate": get_error_rate(),
        "recent_activity": get_recent_activity(),
    }


def print_report(report: dict) -> None:
    """Print a formatted terminal report."""
    print("=" * 50)
    print("  ORCHESTRATION MONITOR")
    print("=" * 50)
    print()

    # Orchestrator status
    orch = report["orchestrator"]
    if orch["running"]:
        print(f"Orchestrator: RUNNING (PID {orch['pid']})")
    elif orch.get("stale_lock"):
        print("Orchestrator: NOT RUNNING (stale lock file)")
    else:
        print("Orchestrator: NOT RUNNING")
    print()

    # Queue status
    queue = report["queue"]
    if queue["available"]:
        print("TASK QUEUE")
        print("-" * 50)
        print(f"  Total tasks:       {queue['total']:>8}")
        print(f"  Pending:           {queue['total_pending']:>8}")
        print(f"  In progress:       {queue['total_in_progress']:>8}")
        print(f"  Completed:         {queue['total_completed']:>8}")
        if queue.get("last_populated"):
            print(f"  Last populated:    {queue['last_populated']}")
        print()

        print("  By type:")
        for tt, counts in sorted(queue["by_type"].items()):
            print(
                f"    {tt:15s}  {counts['pending']:>5d} pending / "
                f"{counts['in_progress']:>3d} active / "
                f"{counts['completed']:>5d} done"
            )
        print()
    else:
        print("TASK QUEUE: not available (run `populate` first)")
        print()

    # Active sessions
    sessions = report["active_sessions"]
    print("ACTIVE SESSIONS")
    print("-" * 50)
    if sessions:
        for s in sessions:
            print(
                f"  {s['session_id']}: {len(s['entry_ids'])} entries "
                f"({s['task_type']}) since {s.get('claimed_at', '?')}"
            )
    else:
        print("  (none)")
    print()

    # Throughput
    throughput = report["throughput"]
    print("THROUGHPUT (entries/hour)")
    print("-" * 50)
    for window, rate in sorted(throughput.items()):
        print(f"  Last {window:>3s}: {rate:>8.1f}")
    print()

    # Budget
    budget = report["budget"]
    if budget["available"]:
        print("BUDGET")
        print("-" * 50)
        print(
            f"  Spent today:       ${budget['spent_today_usd']:>7.2f} / "
            f"${budget['daily_limit_usd']:.2f}"
        )
        print(f"  Remaining:         ${budget['remaining_usd']:>7.2f}")
        print(f"  Sessions today:    {budget['sessions_today']:>8}")
    else:
        print("BUDGET: not configured")
    print()

    # Error rate
    errors = report["error_rate"]
    print("ERROR RATE (today)")
    print("-" * 50)
    print(f"  Total sessions:    {errors['total_sessions']:>8}")
    print(f"  Failed:            {errors['failed_sessions']:>8}")
    print(f"  Error rate:        {errors['error_rate']:>7.1f}%")
    print()

    # Recent activity
    recent = report["recent_activity"]
    if recent:
        print("RECENT ACTIVITY")
        print("-" * 50)
        for entry in recent:
            print(
                f"  {entry.get('timestamp', '?')}: "
                f"slot={entry.get('slot_id', '?')}, "
                f"cost=${entry.get('cost_usd', 0):.2f}"
            )
    print()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Monitoring dashboard for the orchestration system"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON instead of formatted text",
    )
    args = parser.parse_args()

    report = build_report()

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_report(report)

    return 0


if __name__ == "__main__":
    sys.exit(main())
