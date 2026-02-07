#!/usr/bin/env python3
"""
Pipeline status update and reporting tool.

Reads and updates pipeline-status.json with task results, and generates
human-readable summary reports. Complements build/report.py (dictionary
health) by tracking pipeline run progress.

Usage:
    # Record a task result
    python3 pipeline/update-status.py record \
        --type new-entries --index 0 --invocation 1 \
        --status passed --message "OK" \
        --duration 45

    # Generate a human-readable report from pipeline-status.json
    python3 pipeline/update-status.py report

    # Generate report and append dictionary health snapshot
    python3 pipeline/update-status.py report --include-health

    # Show a brief one-line summary
    python3 pipeline/update-status.py summary
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
STATUS_FILE = SCRIPT_DIR / "pipeline-status.json"
REPORT_FILE = SCRIPT_DIR / "pipeline-report.txt"


def load_status() -> dict:
    """Load pipeline-status.json, returning empty structure if missing."""
    if not STATUS_FILE.exists():
        return {"started": None, "finished": None, "config_file": None, "results": []}
    with open(STATUS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_status(data: dict) -> None:
    """Write pipeline-status.json."""
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def cmd_init(args: argparse.Namespace) -> int:
    """Initialize a new pipeline-status.json."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = {
        "started": timestamp,
        "finished": None,
        "config_file": args.config_file or str(SCRIPT_DIR / "pipeline-config.json"),
        "results": [],
    }
    save_status(data)
    print(f"Initialized {STATUS_FILE}")
    return 0


def cmd_record(args: argparse.Namespace) -> int:
    """Record a task result into pipeline-status.json."""
    data = load_status()
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    result = {
        "task_type": args.type,
        "task_index": args.index,
        "invocation": args.invocation,
        "status": args.status,
        "message": args.message or "",
        "timestamp": timestamp,
    }
    if args.duration is not None:
        result["duration_seconds"] = args.duration

    data["results"].append(result)
    save_status(data)
    print(f"Recorded: {args.type}[{args.invocation}] = {args.status}")
    return 0


def cmd_finalize(args: argparse.Namespace) -> int:
    """Mark the pipeline run as finished."""
    data = load_status()
    data["finished"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    save_status(data)
    print(f"Finalized pipeline run at {data['finished']}")
    return 0


def format_duration(seconds: int) -> str:
    """Format seconds as human-readable duration."""
    if seconds < 60:
        return f"{seconds}s"
    minutes = seconds // 60
    secs = seconds % 60
    if minutes < 60:
        return f"{minutes}m{secs}s" if secs else f"{minutes}m"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h{mins}m" if mins else f"{hours}h"


def generate_report(data: dict, include_health: bool = False) -> str:
    """Generate a human-readable report from status data."""
    results = data.get("results", [])
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "passed")
    failed = sum(1 for r in results if r["status"] == "failed")
    skipped = sum(1 for r in results if r["status"] == "skipped")

    # Calculate total duration if available
    total_duration = sum(r.get("duration_seconds", 0) for r in results)

    # Group by task type for summary
    by_type: dict[str, dict] = {}
    for r in results:
        tt = r["task_type"]
        if tt not in by_type:
            by_type[tt] = {"passed": 0, "failed": 0, "skipped": 0, "duration": 0}
        by_type[tt][r["status"]] = by_type[tt].get(r["status"], 0) + 1
        by_type[tt]["duration"] += r.get("duration_seconds", 0)

    lines = []
    lines.append("=" * 64)
    lines.append("  PIPELINE REPORT")
    lines.append("=" * 64)
    lines.append("")
    lines.append(f"  Started:   {data.get('started', 'N/A')}")
    lines.append(f"  Finished:  {data.get('finished', 'N/A')}")
    lines.append(f"  Config:    {data.get('config_file', 'N/A')}")
    if total_duration:
        lines.append(f"  Duration:  {format_duration(total_duration)}")
    lines.append("")
    lines.append(f"  Total invocations: {total}")
    lines.append(f"    Passed:  {passed}")
    lines.append(f"    Failed:  {failed}")
    lines.append(f"    Skipped: {skipped}")
    lines.append("")

    # Per-type summary
    if by_type:
        lines.append("-" * 64)
        lines.append(f"  {'Task Type':<25} {'Pass':>5} {'Fail':>5} {'Skip':>5} {'Time':>8}")
        lines.append("-" * 64)
        for tt, counts in sorted(by_type.items()):
            dur = format_duration(counts["duration"]) if counts["duration"] else "-"
            lines.append(
                f"  {tt:<25} {counts['passed']:>5} "
                f"{counts['failed']:>5} {counts['skipped']:>5} {dur:>8}"
            )
        lines.append("")

    # Detailed results
    lines.append("-" * 64)
    lines.append(f"  {'#':>3}  {'Task':>25}  {'Status':<8}  {'Message'}")
    lines.append("-" * 64)
    for i, r in enumerate(results, 1):
        label = f"{r['task_type']}[{r['invocation']}]"
        dur_str = ""
        if r.get("duration_seconds"):
            dur_str = f" ({format_duration(r['duration_seconds'])})"
        lines.append(f"  {i:>3}  {label:>25}  {r['status']:<8}  {r['message']}{dur_str}")
    lines.append("-" * 64)
    lines.append("")

    # Optionally append dictionary health snapshot
    if include_health:
        lines.append("")
        lines.append("=" * 64)
        lines.append("  DICTIONARY HEALTH SNAPSHOT")
        lines.append("=" * 64)
        lines.append("")
        try:
            health_output = subprocess.run(
                [sys.executable, str(PROJECT_DIR / "build" / "report.py")],
                capture_output=True,
                text=True,
                cwd=str(PROJECT_DIR / "build"),
                timeout=120,
            )
            if health_output.returncode == 0:
                lines.append(health_output.stdout)
            else:
                lines.append("  (report.py failed — see stderr)")
                if health_output.stderr:
                    lines.append(f"  {health_output.stderr.strip()}")
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            lines.append(f"  (Could not run report.py: {e})")
        lines.append("")

    return "\n".join(lines)


def cmd_report(args: argparse.Namespace) -> int:
    """Generate and display a pipeline report."""
    data = load_status()
    if not data.get("results"):
        print("No results recorded yet.")
        return 0

    report = generate_report(data, include_health=args.include_health)
    print(report)

    # Also write to file
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport written to {REPORT_FILE}")
    return 0


def cmd_summary(args: argparse.Namespace) -> int:
    """Print a one-line pipeline status summary."""
    data = load_status()
    results = data.get("results", [])
    if not results:
        print("No pipeline results.")
        return 0

    passed = sum(1 for r in results if r["status"] == "passed")
    failed = sum(1 for r in results if r["status"] == "failed")
    skipped = sum(1 for r in results if r["status"] == "skipped")
    total_duration = sum(r.get("duration_seconds", 0) for r in results)

    status = "RUNNING" if not data.get("finished") else "DONE"
    dur_str = f" in {format_duration(total_duration)}" if total_duration else ""
    print(f"Pipeline {status}: {passed} passed, {failed} failed, {skipped} skipped{dur_str}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Pipeline status tracking and reporting"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init
    init_parser = subparsers.add_parser("init", help="Initialize pipeline-status.json")
    init_parser.add_argument("--config-file", help="Path to config file being used")

    # record
    record_parser = subparsers.add_parser("record", help="Record a task result")
    record_parser.add_argument("--type", required=True, help="Task type")
    record_parser.add_argument("--index", type=int, required=True, help="Task index")
    record_parser.add_argument(
        "--invocation", type=int, required=True, help="Invocation number"
    )
    record_parser.add_argument(
        "--status",
        required=True,
        choices=["passed", "failed", "skipped"],
        help="Result status",
    )
    record_parser.add_argument("--message", default="", help="Result message")
    record_parser.add_argument(
        "--duration", type=int, default=None, help="Duration in seconds"
    )

    # finalize
    subparsers.add_parser("finalize", help="Mark pipeline run as finished")

    # report
    report_parser = subparsers.add_parser(
        "report", help="Generate pipeline report"
    )
    report_parser.add_argument(
        "--include-health",
        action="store_true",
        help="Append dictionary health snapshot from build/report.py",
    )

    # summary
    subparsers.add_parser("summary", help="One-line status summary")

    args = parser.parse_args()

    commands = {
        "init": cmd_init,
        "record": cmd_record,
        "finalize": cmd_finalize,
        "report": cmd_report,
        "summary": cmd_summary,
    }
    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
