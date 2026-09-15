#!/usr/bin/env python3
"""Block for N seconds, then print how long was actually waited.

    python3 pipeline/wait.py 60

Used between CI polls at a Routine run's wrap-up. A Bash ``sleep`` started
with ``run_in_background`` returns immediately, so a loop built on it polls
sixteen times in about two minutes while the ``validate`` check takes five to
seven; this call is a foreground wait and the printed elapsed time is the
evidence that it happened.
"""
import sys
import time


def main() -> int:
    try:
        seconds = float(sys.argv[1]) if len(sys.argv) > 1 else 60.0
    except ValueError:
        print(f"usage: {sys.argv[0]} SECONDS")
        return 2
    seconds = max(0.0, min(seconds, 600.0))
    start = time.monotonic()
    time.sleep(seconds)
    print(f"waited {time.monotonic() - start:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
