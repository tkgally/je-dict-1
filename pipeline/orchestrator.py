#!/usr/bin/env python3
"""Orchestrator for parallel Claude CLI sessions.

Launches and monitors multiple Claude CLI sessions that draw from the task
queue, process dictionary entries, and commit results. Includes budget
enforcement, error circuit breaker, and graceful shutdown.

Usage:
    python3 pipeline/orchestrator.py start          # Begin orchestration loop
    python3 pipeline/orchestrator.py start --dry-run # Show what would happen
    python3 pipeline/orchestrator.py stop            # Signal graceful shutdown
    python3 pipeline/orchestrator.py status          # Show running sessions
"""

import argparse
import json
import logging
import os
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
CONFIG_FILE = SCRIPT_DIR / "pipeline-config.json"
BUDGET_FILE = SCRIPT_DIR / "budget.json"
LOCK_FILE = SCRIPT_DIR / "orchestrator.lock"
LOGS_DIR = SCRIPT_DIR / "logs"

# Ensure logs directory exists
LOGS_DIR.mkdir(exist_ok=True)


def utcnow() -> str:
    """Return current UTC time as ISO 8601 string."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_str() -> str:
    """Return today's date as YYYY-MM-DD."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def setup_logging() -> logging.Logger:
    """Configure logging to file and stderr."""
    logger = logging.getLogger("orchestrator")
    logger.setLevel(logging.INFO)

    # Console handler
    console = logging.StreamHandler(sys.stderr)
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(console)

    # File handler
    log_file = LOGS_DIR / f"orchestrator_{today_str()}.log"
    file_handler = logging.FileHandler(str(log_file))
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    )
    logger.addHandler(file_handler)

    return logger


def load_config() -> dict:
    """Load pipeline configuration."""
    with open(CONFIG_FILE) as f:
        return json.load(f)


def load_budget() -> dict:
    """Load budget data, resetting daily spend if needed."""
    if not BUDGET_FILE.exists():
        return {
            "daily_limit_usd": 50.0,
            "spent_today_usd": 0.0,
            "last_reset": today_str(),
            "session_log": [],
            "estimated_cost_per_session_usd": 2.0,
        }

    with open(BUDGET_FILE) as f:
        data = json.load(f)

    # Reset daily spend at midnight UTC
    if data.get("last_reset") != today_str():
        data["spent_today_usd"] = 0.0
        data["last_reset"] = today_str()
        data["session_log"] = []
        save_budget(data)

    return data


def save_budget(data: dict) -> None:
    """Write budget data to disk."""
    with open(BUDGET_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def check_budget(budget: dict, config: dict) -> bool:
    """Return True if budget allows launching another session."""
    limit = config.get("schedule", {}).get(
        "daily_budget_usd", budget.get("daily_limit_usd", 50.0)
    )
    estimated = budget.get("estimated_cost_per_session_usd", 2.0)
    return budget["spent_today_usd"] + estimated <= limit


def record_session_cost(budget: dict, slot_id: str, estimated_cost: float) -> None:
    """Record a session's estimated cost in the budget."""
    budget["spent_today_usd"] += estimated_cost
    budget["session_log"].append(
        {"slot_id": slot_id, "cost_usd": estimated_cost, "timestamp": utcnow()}
    )
    save_budget(budget)


def check_daily_run_limit(budget: dict, config: dict) -> bool:
    """Return True if we haven't exceeded max_runs_per_day."""
    max_runs = config.get("schedule", {}).get("max_runs_per_day", 10)
    return len(budget.get("session_log", [])) < max_runs


# --- Lock file management ---


def acquire_lock(logger: logging.Logger) -> bool:
    """Create lock file. Returns False if another orchestrator is running."""
    if LOCK_FILE.exists():
        # Check if the PID is still alive
        try:
            pid = int(LOCK_FILE.read_text().strip())
            os.kill(pid, 0)  # Check if process exists
            logger.error(f"Another orchestrator is running (PID {pid})")
            return False
        except (ValueError, ProcessLookupError, PermissionError):
            # Stale lock file — remove it
            logger.warning("Removing stale lock file")
            LOCK_FILE.unlink(missing_ok=True)

    LOCK_FILE.write_text(str(os.getpid()))
    return True


def release_lock() -> None:
    """Remove the lock file."""
    LOCK_FILE.unlink(missing_ok=True)


# --- Task queue interaction ---


def claim_tasks(task_type: str, count: int, session_id: str) -> list[str]:
    """Claim tasks from the queue, return list of entry IDs."""
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT_DIR / "task_queue.py"),
            "claim",
            "--task-type",
            task_type,
            "--count",
            str(count),
            "--session-id",
            session_id,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    # Each line of stdout is an entry ID
    return [line.strip() for line in result.stdout.strip().split("\n") if line.strip()]


def complete_tasks(session_id: str) -> None:
    """Mark all tasks claimed by session_id as completed."""
    subprocess.run(
        [
            sys.executable,
            str(SCRIPT_DIR / "task_queue.py"),
            "complete",
            "--session-id",
            session_id,
        ],
        capture_output=True,
        text=True,
    )


def release_tasks(session_id: str) -> None:
    """Release tasks claimed by session_id back to pending."""
    subprocess.run(
        [
            sys.executable,
            str(SCRIPT_DIR / "task_queue.py"),
            "release",
            "--session-id",
            session_id,
        ],
        capture_output=True,
        text=True,
    )


# --- Session management ---


def make_branch_name(slot_id: str) -> str:
    """Generate a unique branch name for a session."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"auto/{slot_id}-{timestamp}"


def launch_session(
    slot: dict,
    entry_ids: list[str],
    branch_name: str,
    logger: logging.Logger,
    dry_run: bool = False,
) -> subprocess.Popen | None:
    """Launch a Claude CLI session for the given slot and entries.

    Returns the Popen object, or None if dry_run.
    """
    prompt_file = PROJECT_ROOT / slot["prompt"]
    entry_list = ", ".join(entry_ids)

    prompt_text = (
        f"Read {prompt_file} and process these specific entries: {entry_list}. "
        f"Commit results to branch {branch_name}. "
        f"Do NOT run make build or update_indexes.py."
    )

    if dry_run:
        logger.info(
            f"[DRY RUN] Would launch slot {slot['id']}: "
            f"{len(entry_ids)} entries on branch {branch_name}"
        )
        return None

    # Create the branch
    subprocess.run(
        ["git", "checkout", "-b", branch_name],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
    )
    subprocess.run(
        ["git", "checkout", "main"],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
    )

    log_file = LOGS_DIR / f"{slot['id']}_{today_str()}_{utcnow().replace(':', '')}.log"

    cmd = ["claude", "-p", prompt_text, "--verbose"]

    logger.info(
        f"Launching slot {slot['id']}: {len(entry_ids)} entries, branch {branch_name}"
    )

    with open(log_file, "w") as lf:
        proc = subprocess.Popen(
            cmd,
            stdout=lf,
            stderr=subprocess.STDOUT,
            cwd=str(PROJECT_ROOT),
        )

    return proc


def validate_branch(branch_name: str, logger: logging.Logger) -> bool:
    """Validate entries on a session branch."""
    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "build" / "validate.py"), "--changed-only"],
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
    )
    if result.returncode != 0:
        logger.error(f"Validation failed for {branch_name}: {result.stderr[:500]}")
        return False
    return True


# --- Main orchestration loop ---


class Orchestrator:
    """Manages parallel Claude CLI sessions."""

    def __init__(self, logger: logging.Logger, dry_run: bool = False):
        self.logger = logger
        self.dry_run = dry_run
        self.running: dict[str, dict] = {}  # slot_id -> session info
        self.shutdown_requested = False
        self.consecutive_failures = 0
        self.max_consecutive_failures = 3

    def handle_signal(self, signum, frame):
        """Handle SIGINT/SIGTERM for graceful shutdown."""
        self.logger.info(
            f"Received signal {signum}, finishing current sessions and shutting down..."
        )
        self.shutdown_requested = True

    def run(self) -> int:
        """Main orchestration loop. Returns exit code."""
        config = load_config()
        budget = load_budget()

        slots = config.get("parallel_slots", [])
        enabled_slots = [s for s in slots if s.get("enabled")]
        max_concurrent = config.get("schedule", {}).get("max_concurrent", 2)
        cooldown = config.get("schedule", {}).get("cooldown_minutes", 5)

        if not enabled_slots:
            self.logger.error("No enabled parallel slots in configuration")
            return 1

        self.logger.info(
            f"Starting orchestrator: {len(enabled_slots)} enabled slots, "
            f"max {max_concurrent} concurrent"
        )

        if self.dry_run:
            self._dry_run_report(enabled_slots, budget, config)
            return 0

        # Install signal handlers
        signal.signal(signal.SIGINT, self.handle_signal)
        signal.signal(signal.SIGTERM, self.handle_signal)

        slot_index = 0

        while not self.shutdown_requested:
            # Check circuit breaker
            if self.consecutive_failures >= self.max_consecutive_failures:
                self.logger.error(
                    f"Circuit breaker: {self.consecutive_failures} consecutive "
                    f"failures, pausing orchestrator"
                )
                break

            # Reload budget (may have been reset)
            budget = load_budget()

            # Check budget
            if not check_budget(budget, config):
                self.logger.info("Daily budget exhausted, stopping")
                break

            # Check run limit
            if not check_daily_run_limit(budget, config):
                self.logger.info("Daily run limit reached, stopping")
                break

            # Check and reap completed sessions
            self._reap_completed(config)

            # Launch new sessions if we have capacity
            while (
                len(self.running) < max_concurrent
                and not self.shutdown_requested
                and check_budget(budget, config)
                and check_daily_run_limit(budget, config)
            ):
                slot = enabled_slots[slot_index % len(enabled_slots)]
                slot_index += 1

                if slot["id"] in self.running:
                    # This slot is already running
                    if slot_index >= len(enabled_slots) * 2:
                        break  # Avoid infinite loop
                    continue

                session_id = f"{slot['id']}-{utcnow().replace(':', '').replace('-', '')}"
                entry_ids = claim_tasks(
                    slot["task_type"], slot["batch_size"], session_id
                )

                if not entry_ids:
                    self.logger.info(
                        f"No pending tasks for slot {slot['id']} "
                        f"(type: {slot['task_type']})"
                    )
                    # Try next slot
                    if slot_index >= len(enabled_slots) * 2:
                        break
                    continue

                branch_name = make_branch_name(slot["id"])
                proc = launch_session(
                    slot, entry_ids, branch_name, self.logger, self.dry_run
                )

                estimated_cost = budget.get("estimated_cost_per_session_usd", 2.0)
                record_session_cost(budget, slot["id"], estimated_cost)

                self.running[slot["id"]] = {
                    "process": proc,
                    "session_id": session_id,
                    "branch": branch_name,
                    "slot": slot,
                    "entry_ids": entry_ids,
                    "started_at": utcnow(),
                }

                self.logger.info(
                    f"Session started: slot={slot['id']}, "
                    f"entries={len(entry_ids)}, branch={branch_name}"
                )

            if not self.running:
                self.logger.info("No sessions running and no tasks available, exiting")
                break

            # Wait before checking again
            time.sleep(30)

        # Wait for remaining sessions to complete
        self._wait_for_remaining()

        return 0

    def _dry_run_report(
        self, enabled_slots: list[dict], budget: dict, config: dict
    ) -> None:
        """Print what the orchestrator would do."""
        self.logger.info("=== DRY RUN REPORT ===")
        self.logger.info(f"Budget: ${budget['spent_today_usd']:.2f} / "
                         f"${budget.get('daily_limit_usd', 50.0):.2f}")
        self.logger.info(
            f"Sessions today: {len(budget.get('session_log', []))} / "
            f"{config.get('schedule', {}).get('max_runs_per_day', 10)}"
        )

        for slot in enabled_slots:
            # Check how many tasks are available
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT_DIR / "task_queue.py"),
                    "status",
                    "--task-type",
                    slot["task_type"],
                ],
                capture_output=True,
                text=True,
            )
            self.logger.info(
                f"Slot {slot['id']} ({slot['task_type']}): "
                f"batch_size={slot['batch_size']}, prompt={slot['prompt']}"
            )
            if result.stdout:
                for line in result.stdout.strip().split("\n"):
                    if "Pending" in line or "pending" in line:
                        self.logger.info(f"  {line.strip()}")

    def _reap_completed(self, config: dict) -> None:
        """Check for completed sessions and handle results."""
        completed = []
        for slot_id, info in self.running.items():
            proc = info["process"]
            if proc is not None and proc.poll() is not None:
                completed.append(slot_id)

        for slot_id in completed:
            info = self.running.pop(slot_id)
            proc = info["process"]
            session_id = info["session_id"]
            branch_name = info["branch"]

            if proc.returncode == 0:
                self.logger.info(
                    f"Session completed: slot={slot_id}, branch={branch_name}"
                )

                # Validate the branch
                valid = validate_branch(branch_name, self.logger)
                if valid:
                    complete_tasks(session_id)
                    self.consecutive_failures = 0

                    auto_merge = config.get("coordinator", {}).get(
                        "auto_merge", False
                    )
                    if auto_merge:
                        self.logger.info(
                            f"Auto-merge enabled: merging {branch_name} to main"
                        )
                        # Merge would happen here — but default is off
                    else:
                        self.logger.info(
                            f"Auto-merge disabled: branch {branch_name} "
                            f"ready for curator review"
                        )
                else:
                    self.logger.error(
                        f"Validation failed for {branch_name}, "
                        f"releasing tasks back to queue"
                    )
                    release_tasks(session_id)
                    self.consecutive_failures += 1
            else:
                self.logger.error(
                    f"Session failed: slot={slot_id}, "
                    f"exit_code={proc.returncode}, releasing tasks"
                )
                release_tasks(session_id)
                self.consecutive_failures += 1

    def _wait_for_remaining(self) -> None:
        """Wait for all running sessions to finish."""
        if not self.running:
            return

        self.logger.info(
            f"Waiting for {len(self.running)} remaining session(s) to complete..."
        )
        for slot_id, info in list(self.running.items()):
            proc = info["process"]
            if proc is not None:
                proc.wait()
                self.logger.info(f"Session for slot {slot_id} finished")


# --- Subcommands ---


def cmd_start(args: argparse.Namespace) -> int:
    """Start the orchestration loop."""
    logger = setup_logging()

    if not args.dry_run:
        if not acquire_lock(logger):
            return 1

    try:
        orchestrator = Orchestrator(logger, dry_run=args.dry_run)
        return orchestrator.run()
    finally:
        if not args.dry_run:
            release_lock()


def cmd_stop(args: argparse.Namespace) -> int:
    """Signal the orchestrator to stop gracefully."""
    if not LOCK_FILE.exists():
        print("No orchestrator is running (no lock file found)")
        return 1

    try:
        pid = int(LOCK_FILE.read_text().strip())
        os.kill(pid, signal.SIGTERM)
        print(f"Sent SIGTERM to orchestrator (PID {pid})")
        return 0
    except (ValueError, ProcessLookupError):
        print("Orchestrator process not found, removing stale lock file")
        LOCK_FILE.unlink(missing_ok=True)
        return 1


def cmd_status(args: argparse.Namespace) -> int:
    """Show orchestrator and session status."""
    # Lock file status
    if LOCK_FILE.exists():
        try:
            pid = int(LOCK_FILE.read_text().strip())
            os.kill(pid, 0)
            print(f"Orchestrator: RUNNING (PID {pid})")
        except (ValueError, ProcessLookupError):
            print("Orchestrator: NOT RUNNING (stale lock file)")
    else:
        print("Orchestrator: NOT RUNNING")

    print()

    # Budget status
    budget = load_budget()
    limit = budget.get("daily_limit_usd", 50.0)
    spent = budget.get("spent_today_usd", 0.0)
    sessions_today = len(budget.get("session_log", []))
    print(f"Budget: ${spent:.2f} / ${limit:.2f} ({sessions_today} sessions today)")

    # Recent session log
    session_log = budget.get("session_log", [])
    if session_log:
        print("\nRecent sessions:")
        for entry in session_log[-10:]:
            print(
                f"  {entry.get('timestamp', '?')}: "
                f"slot={entry.get('slot_id', '?')}, "
                f"cost=${entry.get('cost_usd', 0):.2f}"
            )

    print()

    # Task queue summary
    result = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "task_queue.py"), "status"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Task queue: unavailable (run `populate` first)")

    # Recent log files
    log_files = sorted(LOGS_DIR.glob("*.log"), key=lambda p: p.stat().st_mtime)
    if log_files:
        print("Recent log files:")
        for lf in log_files[-5:]:
            size = lf.stat().st_size
            print(f"  {lf.name} ({size} bytes)")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Orchestrator for parallel Claude CLI sessions"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # start
    p_start = subparsers.add_parser("start", help="Begin orchestration loop")
    p_start.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without launching sessions",
    )

    # stop
    subparsers.add_parser("stop", help="Gracefully stop the orchestrator")

    # status
    subparsers.add_parser("status", help="Show running sessions and budget")

    args = parser.parse_args()

    if not args.command:
        # Default to status if no command given
        args.command = "status"

    commands = {
        "start": cmd_start,
        "stop": cmd_stop,
        "status": cmd_status,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
