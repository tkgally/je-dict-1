"""Log the subscription's rate-limit utilization (five-hour and seven-day windows), read from the
rate_limit_event that `claude -p --output-format stream-json --verbose` emits. One tiny Haiku call.
python3 usage_probe.py "<note>"   → appends to logs/usage.jsonl"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

p = subprocess.run(["claude", "-p", "--model", "haiku", "--output-format", "stream-json", "--verbose",
                    "--system-prompt", "terse", "--tools", "", "--strict-mcp-config", "--setting-sources", "",
                    "--no-session-persistence"], input="Reply OK", capture_output=True, text=True, cwd="/tmp")
info = None
for line in p.stdout.splitlines():
    if '"rate_limit_event"' in line:
        info = json.loads(line)["rate_limit_info"]
rec = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "note": " ".join(sys.argv[1:]),
       "type": (info or {}).get("rateLimitType"),
       "five_hour": ((info or {}).get("unifiedWindows") or {}).get("five_hour", {}).get("utilization"),
       "seven_day": ((info or {}).get("unifiedWindows") or {}).get("seven_day", {}).get("utilization")}
with open(Path(__file__).parent / "logs/usage.jsonl", "a") as f:
    f.write(json.dumps(rec) + "\n")
print(rec)
