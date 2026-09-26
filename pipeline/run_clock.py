#!/usr/bin/env python3
"""Keep a scheduled run to about two hours: record its start, then say whether
another cycle may begin.

    python3 pipeline/run_clock.py start    # first command of the run; a repeat keeps the first time
    python3 pipeline/run_clock.py          # elapsed minutes, "next cycle: yes|no", "wrap up now" once due

A Routine run is a series of cycles (select a mode, do it, merge its PR). The
schedule fires every three hours, so a run must end well before the next one
starts. A new cycle may begin until NEW_CYCLE_UNTIL minutes have passed; from
WRAP_UP_AT minutes the cycle in progress stops its content work and wraps up.
The start time is kept outside the repository (it survives a compacted
conversation, never a new container); a start file older than STALE_AFTER
minutes belongs to an earlier run in the same container and is replaced.
"""
import argparse
import sys
import time
from pathlib import Path

START_FILE = Path("/tmp") / f"{Path(__file__).resolve().parents[1].name}-run-start"
NEW_CYCLE_UNTIL = 105
WRAP_UP_AT = 130
STALE_AFTER = 240


def read_start(path: Path, now: float):
    try:
        start = float(path.read_text().strip())
    except (OSError, ValueError):
        return None
    if now - start > STALE_AFTER * 60 or start > now + 60:
        return None
    return start


def report(elapsed_min: float, new_cycle_until: int, wrap_up_at: int) -> list:
    lines = [f"elapsed: {elapsed_min:.0f} min"]
    if elapsed_min < new_cycle_until:
        lines.append(f"next cycle: yes (a new cycle may start until {new_cycle_until} min)")
    else:
        lines.append(f"next cycle: no (past {new_cycle_until} min): finish this cycle and end the run")
    if elapsed_min >= wrap_up_at:
        lines.append(f"wrap up now: past {wrap_up_at} min, stop content work and go to the wrap-up")
    else:
        lines.append(f"content work may continue until {wrap_up_at} min")
    return lines


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Run clock for multi-cycle Routine runs.")
    ap.add_argument("action", nargs="?", choices=["start", "check"], default="check")
    ap.add_argument("--reset", action="store_true", help="with start: replace an existing start time")
    ap.add_argument("--new-cycle-until", type=int, default=NEW_CYCLE_UNTIL)
    ap.add_argument("--wrap-up-at", type=int, default=WRAP_UP_AT)
    ap.add_argument("--file", type=Path, default=START_FILE, help=argparse.SUPPRESS)
    args = ap.parse_args(argv)

    now = time.time()
    start = read_start(args.file, now)
    if args.action == "start":
        if start is None or args.reset:
            args.file.write_text(f"{now:.0f}\n")
            start = now
            print(f"run clock started {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(now))}")
        else:
            print(f"run clock already running since "
                  f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(start))}; kept")
    elif start is None:
        args.file.write_text(f"{now:.0f}\n")
        start = now
        print("no start time recorded: the clock starts now")
    for line in report((now - start) / 60, args.new_cycle_until, args.wrap_up_at):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
