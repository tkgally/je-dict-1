#!/usr/bin/env bash
# Poll GitHub for completion of CI check-runs on a PR's head SHA.
# Designed to be invoked via the Monitor tool from a Routine session: stdout
# emits one status line per poll, and the exit code reports the final state.
#
# Usage: wait-for-pr-checks.sh <pr_number> [interval_seconds] [timeout_seconds]
#
# Exit codes:
#   0  all check-runs completed successfully (or with neutral/skipped)
#   1  at least one check-run failed
#   2  timed out before all checks completed
#   3  auth or API error (no token, bad SHA, etc.)
#   4  no checks ever appeared on the head SHA within the timeout
#
# The session should:
#   - run this via Monitor after pushing and creating the PR
#   - on exit code 0, call mcp__github__merge_pull_request with squash
#   - on any non-zero, leave the PR open for the curator and log why

set -uo pipefail

PR="${1:?usage: $0 <pr_number> [interval] [timeout]}"
INTERVAL="${2:-15}"
TIMEOUT="${3:-600}"
REPO="tkgally/je-dict-1"
API="https://api.github.com/repos/$REPO"

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "error: GITHUB_TOKEN is not set in the environment" >&2
  exit 3
fi

curl_gh() {
  curl -fsSL \
       -H "Authorization: Bearer $GITHUB_TOKEN" \
       -H "Accept: application/vnd.github+json" \
       -H "X-GitHub-Api-Version: 2022-11-28" \
       "$@"
}

SHA=$(curl_gh "$API/pulls/$PR" | jq -r '.head.sha')
if [[ -z "$SHA" || "$SHA" == "null" ]]; then
  echo "error: could not resolve PR #$PR head SHA" >&2
  exit 3
fi
echo "PR #$PR head=$SHA polling every ${INTERVAL}s (timeout ${TIMEOUT}s)"

START=$(date +%s)
ever_saw_check=0

while :; do
  ELAPSED=$(( $(date +%s) - START ))
  if (( ELAPSED > TIMEOUT )); then
    if (( ever_saw_check == 0 )); then
      echo "timeout after ${TIMEOUT}s with no check-runs ever reported"
      exit 4
    fi
    echo "timeout after ${TIMEOUT}s"
    exit 2
  fi

  RUNS=$(curl_gh "$API/commits/$SHA/check-runs?per_page=100" 2>/dev/null) || {
    echo "[${ELAPSED}s] api error fetching check-runs, will retry"
    sleep "$INTERVAL"
    continue
  }

  TOTAL=$(jq -r '.total_count // 0' <<<"$RUNS")
  PENDING=$(jq -r '[.check_runs[]? | select(.status != "completed")] | length' <<<"$RUNS")
  FAILED=$(jq -r '[.check_runs[]? | select(.status == "completed" and (.conclusion // "") != "success" and (.conclusion // "") != "neutral" and (.conclusion // "") != "skipped")] | length' <<<"$RUNS")

  printf '[%4ds] checks: total=%s pending=%s failed=%s\n' "$ELAPSED" "$TOTAL" "$PENDING" "$FAILED"

  if (( TOTAL > 0 )); then
    ever_saw_check=1
  fi

  if (( FAILED > 0 )); then
    jq -r '.check_runs[]? | select(.status == "completed" and (.conclusion // "") != "success" and (.conclusion // "") != "neutral" and (.conclusion // "") != "skipped") | "  failed: \(.name) (\(.conclusion // "no-conclusion"))  \(.html_url)"' <<<"$RUNS"
    exit 1
  fi

  if (( TOTAL > 0 && PENDING == 0 )); then
    echo "all $TOTAL check(s) completed successfully"
    exit 0
  fi

  sleep "$INTERVAL"
done
