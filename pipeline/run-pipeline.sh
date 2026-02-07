#!/bin/bash
# pipeline/run-pipeline.sh — Reads pipeline-config.json and executes tasks sequentially.
#
# For each task invocation:
#   1. Checks git working tree is clean
#   2. Invokes claude --print with the appropriate prompt
#   3. Runs make validate as a quality gate
#   4. If validation passes, commits to the configured branch
#   5. If validation fails, logs the error and stops or skips based on config
#   6. Updates pipeline/pipeline-status.json with results
#
# At the end, generates a summary report to pipeline/pipeline-report.txt.
#
# Usage:
#   ./pipeline/run-pipeline.sh                     # run with default config
#   ./pipeline/run-pipeline.sh my-config.json      # run with custom config
#   ./pipeline/run-pipeline.sh --dry-run            # show what would run without executing
#   ./pipeline/run-pipeline.sh --create-pr          # create a PR after completion

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE=""
DRY_RUN=false
CREATE_PR=false
LOG_FILE="$SCRIPT_DIR/pipeline-$(date +%Y%m%d-%H%M%S).log"
STATUS_FILE="$SCRIPT_DIR/pipeline-status.json"
REPORT_FILE="$SCRIPT_DIR/pipeline-report.txt"

# Parse arguments
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    --create-pr) CREATE_PR=true ;;
    -*) echo "Unknown flag: $arg" >&2; exit 1 ;;
    *) CONFIG_FILE="$arg" ;;
  esac
done

# Default config file if none specified
if [ -z "$CONFIG_FILE" ]; then
  CONFIG_FILE="$SCRIPT_DIR/pipeline-config.json"
fi

# --- Logging ---

log() {
  local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $1"
  echo "$msg" | tee -a "$LOG_FILE"
}

log_error() {
  local msg="[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $1"
  echo "$msg" | tee -a "$LOG_FILE" >&2
}

# --- JSON helpers (use python3 for portability) ---

# Read a value from the config JSON.
# Usage: config_query <python_expression_using_d>
# The expression receives d = parsed JSON. Use sys.argv for dynamic values.
config_query() {
  python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    d = json.load(f)
print($1)
" "$CONFIG_FILE"
}

task_count() {
  config_query "len(d['tasks'])"
}

task_field() {
  # task_field <task_index> <field> <default>
  local index="$1" field="$2" default="$3"
  python3 - "$CONFIG_FILE" "$index" "$field" "$default" << 'PYEOF'
import json, sys
config_file, index, field, default = sys.argv[1:5]
with open(config_file) as f:
    d = json.load(f)
val = d['tasks'][int(index)].get(field)
print(val if val is not None else default)
PYEOF
}

task_param() {
  # task_param <task_index> <param> <default>
  local index="$1" param="$2" default="$3"
  python3 - "$CONFIG_FILE" "$index" "$param" "$default" << 'PYEOF'
import json, sys
config_file, index, param, default = sys.argv[1:5]
with open(config_file) as f:
    d = json.load(f)
val = d['tasks'][int(index)].get('parameters', {}).get(param)
print(val if val is not None else default)
PYEOF
}

# --- Task type → prompt file mapping ---

prompt_file_for_type() {
  local task_type="$1"
  case "$task_type" in
    corpus-harvesting)       echo "prompts/corpus_harvesting.md" ;;
    new-entries)             echo "prompts/newentries.md" ;;
    new-candidates)          echo "prompts/newcandidates.md" ;;
    clean-candidates)        echo "prompts/clean_up_candidates_list.md" ;;
    inline-links)            echo "prompts/polish_add_inline_links.md" ;;
    example-sentences)       echo "prompts/polish_example_sentences.md" ;;
    furigana-completeness)   echo "prompts/polish_furigana_completeness.md" ;;
    furigana-correctness)    echo "prompts/polish_furigana_correctness.md" ;;
    semantic-labels)         echo "prompts/polish_semantic_labels.md" ;;
    noentry-resolution)      echo "prompts/polish_add_entries_for_noentry_example_words.md" ;;
    expand-short-notes)      echo "prompts/expand-short-notes.md" ;;
    *)
      log_error "Unknown task type: $task_type"
      return 1
      ;;
  esac
}

# --- Status tracking ---

init_status() {
  local timestamp
  timestamp="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  python3 - "$STATUS_FILE" "$CONFIG_FILE" "$timestamp" << 'PYEOF'
import json, sys
status_file, config_file, timestamp = sys.argv[1:4]
status = {
    'started': timestamp,
    'finished': None,
    'config_file': config_file,
    'results': []
}
with open(status_file, 'w') as f:
    json.dump(status, f, indent=2, ensure_ascii=False)
    f.write('\n')
PYEOF
}

record_result() {
  # record_result <task_type> <task_index> <invocation> <status> <message>
  local task_type="$1"
  local task_index="$2"
  local invocation="$3"
  local status="$4"
  local message="$5"
  local timestamp
  timestamp="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  python3 - "$STATUS_FILE" "$task_type" "$task_index" "$invocation" "$status" "$message" "$timestamp" << 'PYEOF'
import json, sys
status_file = sys.argv[1]
task_type, task_index, invocation, status, message, timestamp = sys.argv[2:8]
with open(status_file) as f:
    data = json.load(f)
data['results'].append({
    'task_type': task_type,
    'task_index': int(task_index),
    'invocation': int(invocation),
    'status': status,
    'message': message,
    'timestamp': timestamp
})
with open(status_file, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')
PYEOF
}

finalize_status() {
  local timestamp
  timestamp="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  python3 - "$STATUS_FILE" "$timestamp" << 'PYEOF'
import json, sys
status_file, timestamp = sys.argv[1:3]
with open(status_file) as f:
    data = json.load(f)
data['finished'] = timestamp
with open(status_file, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')
PYEOF
}

# --- Git helpers ---

check_clean_tree() {
  if [ -n "$(git -C "$PROJECT_DIR" status --porcelain)" ]; then
    return 1
  fi
  return 0
}

commit_changes() {
  local branch="$1"
  local task_type="$2"
  local invocation="$3"

  cd "$PROJECT_DIR"

  # Stage entry changes and any modified build artifacts
  git add entries/ entries_index.json candidate_words.json 2>/dev/null || true
  git add kanji/ 2>/dev/null || true

  # Only commit if there are staged changes
  if git diff --cached --quiet; then
    log "No changes to commit for $task_type invocation $invocation"
    return 0
  fi

  git commit -m "pipeline: $task_type (invocation $invocation)

Automated commit by run-pipeline.sh"
}

# --- Main execution ---

main() {
  cd "$PROJECT_DIR"

  # Validate config file exists
  if [ ! -f "$CONFIG_FILE" ]; then
    log_error "Config file not found: $CONFIG_FILE"
    exit 1
  fi

  # Read top-level config
  local default_branch
  default_branch=$(config_query "d.get('branch', 'main')")
  local default_on_failure
  default_on_failure=$(config_query "d.get('on_failure', 'stop')")
  local num_tasks
  num_tasks=$(task_count)
  local description
  description=$(config_query "d.get('description', '')")

  log "Pipeline starting"
  log "Config: $CONFIG_FILE"
  log "Description: $description"
  log "Tasks: $num_tasks"
  log "Default branch: $default_branch"
  log "Default on_failure: $default_on_failure"
  log "Dry run: $DRY_RUN"
  log ""

  if [ "$DRY_RUN" = true ]; then
    log "=== DRY RUN — showing planned execution ==="
    log ""
    for (( t=0; t<num_tasks; t++ )); do
      local task_type
      task_type=$(task_field "$t" "type" "")
      local count
      count=$(task_field "$t" "count" "1")
      local branch
      branch=$(task_field "$t" "branch" "$default_branch")
      local on_failure
      on_failure=$(task_field "$t" "on_failure" "$default_on_failure")
      local prompt
      prompt=$(prompt_file_for_type "$task_type") || exit 1

      log "Task $((t+1))/$num_tasks: $task_type"
      log "  Prompt: $prompt"
      log "  Count: $count invocations"
      log "  Branch: $branch"
      log "  On failure: $on_failure"
      log ""
    done
    log "=== DRY RUN complete ==="
    exit 0
  fi

  # Initialize status tracking
  init_status

  local pipeline_failed=false
  local total_passed=0
  local total_failed=0
  local total_skipped=0

  for (( t=0; t<num_tasks; t++ )); do
    local task_type
    task_type=$(task_field "$t" "type" "")
    local count
    count=$(task_field "$t" "count" "1")
    local branch
    branch=$(task_field "$t" "branch" "$default_branch")
    local on_failure
    on_failure=$(task_field "$t" "on_failure" "$default_on_failure")
    local prompt_path
    prompt_path=$(prompt_file_for_type "$task_type") || exit 1
    local full_prompt_path="$PROJECT_DIR/$prompt_path"

    log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    log "Task $((t+1))/$num_tasks: $task_type ($count invocations)"
    log "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if [ ! -f "$full_prompt_path" ]; then
      log_error "Prompt file not found: $full_prompt_path"
      record_result "$task_type" "$t" 0 "failed" "Prompt file not found: $prompt_path"
      total_failed=$((total_failed + count))
      if [ "$on_failure" = "stop" ]; then
        log_error "Stopping pipeline (on_failure=stop)"
        pipeline_failed=true
        break
      fi
      continue
    fi

    for (( i=1; i<=count; i++ )); do
      log ""
      log "--- $task_type: invocation $i/$count ---"

      # Step 1: Check git working tree is clean
      if ! check_clean_tree; then
        log_error "Git working tree is not clean. Stash or commit changes first."
        record_result "$task_type" "$t" "$i" "failed" "Dirty working tree"
        total_failed=$((total_failed + 1))
        if [ "$on_failure" = "stop" ]; then
          log_error "Stopping pipeline (on_failure=stop)"
          pipeline_failed=true
          break 2
        fi
        continue
      fi

      # Step 2: Switch to task branch if needed
      local current_branch
      current_branch=$(git -C "$PROJECT_DIR" branch --show-current)
      if [ "$current_branch" != "$branch" ]; then
        log "Switching to branch: $branch"
        if ! git -C "$PROJECT_DIR" checkout "$branch" 2>>"$LOG_FILE"; then
          log_error "Failed to switch to branch: $branch"
          record_result "$task_type" "$t" "$i" "failed" "Branch checkout failed: $branch"
          total_failed=$((total_failed + 1))
          if [ "$on_failure" = "stop" ]; then
            pipeline_failed=true
            break 2
          fi
          continue
        fi
      fi

      # Step 3: Build the prompt with parameters
      local prompt_content
      prompt_content=$(cat "$full_prompt_path")

      # Append parameters if present
      local batch_size
      batch_size=$(task_param "$t" "batch_size" "")
      local tier
      tier=$(task_param "$t" "tier" "")
      local pos
      pos=$(task_param "$t" "pos" "")
      local entry_ids
      entry_ids=$(task_param "$t" "entry_ids" "")

      local param_suffix=""
      if [ -n "$batch_size" ]; then
        param_suffix="${param_suffix}\n\nBatch size for this session: $batch_size"
      fi
      if [ -n "$tier" ]; then
        param_suffix="${param_suffix}\nTarget tier: $tier"
      fi
      if [ -n "$pos" ]; then
        param_suffix="${param_suffix}\nTarget part of speech: $pos"
      fi
      if [ -n "$entry_ids" ]; then
        param_suffix="${param_suffix}\nTarget entry IDs: $entry_ids"
      fi

      if [ -n "$param_suffix" ]; then
        prompt_content="${prompt_content}$(echo -e "$param_suffix")"
      fi

      # Step 4: Invoke claude --print
      log "Invoking claude --print with prompt: $prompt_path"
      local claude_exit_code=0
      claude --print "$prompt_content" 2>&1 | tee -a "$LOG_FILE" || claude_exit_code=$?

      if [ "$claude_exit_code" -ne 0 ]; then
        log_error "claude --print exited with code $claude_exit_code"
        record_result "$task_type" "$t" "$i" "failed" "claude exited with code $claude_exit_code"
        total_failed=$((total_failed + 1))
        # Discard any partial changes
        git -C "$PROJECT_DIR" checkout -- . 2>/dev/null || true
        if [ "$on_failure" = "stop" ]; then
          log_error "Stopping pipeline (on_failure=stop)"
          pipeline_failed=true
          break 2
        fi
        continue
      fi

      # Step 5: Run make validate as quality gate
      log "Running validation..."
      local validate_exit_code=0
      make -C "$PROJECT_DIR" validate 2>&1 | tee -a "$LOG_FILE" || validate_exit_code=$?

      if [ "$validate_exit_code" -ne 0 ]; then
        log_error "Validation failed for $task_type invocation $i"
        record_result "$task_type" "$t" "$i" "failed" "Validation failed"
        total_failed=$((total_failed + 1))
        # Discard changes that failed validation
        git -C "$PROJECT_DIR" checkout -- . 2>/dev/null || true
        git -C "$PROJECT_DIR" clean -fd entries/ 2>/dev/null || true
        if [ "$on_failure" = "stop" ]; then
          log_error "Stopping pipeline (on_failure=stop)"
          pipeline_failed=true
          break 2
        fi
        continue
      fi

      # Step 6: Commit successful changes
      log "Validation passed. Committing..."
      commit_changes "$branch" "$task_type" "$i"
      record_result "$task_type" "$t" "$i" "passed" "OK"
      total_passed=$((total_passed + 1))
      log "Committed $task_type invocation $i"
    done

    if [ "$pipeline_failed" = true ]; then
      break
    fi
  done

  # Finalize
  finalize_status

  # Generate report
  python3 - "$STATUS_FILE" "$REPORT_FILE" << 'PYEOF' 2>&1 | tee -a "$LOG_FILE"
import json, sys

status_file, report_file = sys.argv[1], sys.argv[2]

with open(status_file) as f:
    data = json.load(f)

results = data["results"]
total = len(results)
passed = sum(1 for r in results if r["status"] == "passed")
failed = sum(1 for r in results if r["status"] == "failed")
skipped = sum(1 for r in results if r["status"] == "skipped")

lines = []
lines.append("=" * 60)
lines.append("Pipeline Report")
lines.append("=" * 60)
lines.append(f"Started:  {data['started']}")
lines.append(f"Finished: {data['finished']}")
lines.append(f"Config:   {data['config_file']}")
lines.append("")
lines.append(f"Total invocations: {total}")
lines.append(f"  Passed:  {passed}")
lines.append(f"  Failed:  {failed}")
lines.append(f"  Skipped: {skipped}")
lines.append("")
lines.append("-" * 60)
lines.append(f"{'#':>3}  {'Task Type':<25} {'Status':<10} {'Message'}")
lines.append("-" * 60)

for i, r in enumerate(results, 1):
    inv = f"{r['task_type']}[{r['invocation']}]"
    lines.append(f"{i:>3}  {inv:<25} {r['status']:<10} {r['message']}")

lines.append("-" * 60)
lines.append("")

report = "\n".join(lines)
print(report)

with open(report_file, "w") as f:
    f.write(report)
PYEOF

  log ""
  log "Pipeline complete. Results: $total_passed passed, $total_failed failed, $total_skipped skipped"
  log "Status: $STATUS_FILE"
  log "Report: $REPORT_FILE"
  log "Log: $LOG_FILE"

  # Optionally create PR
  if [ "$CREATE_PR" = true ] && [ "$total_passed" -gt 0 ]; then
    log "Creating pull request..."
    local current_branch
    current_branch=$(git -C "$PROJECT_DIR" branch --show-current)
    if command -v gh &>/dev/null; then
      git -C "$PROJECT_DIR" push -u origin "$current_branch" 2>&1 | tee -a "$LOG_FILE"
      gh pr create \
        --title "Pipeline: $description" \
        --body "Automated pipeline run. See pipeline-report.txt for details.

Passed: $total_passed | Failed: $total_failed | Skipped: $total_skipped" \
        2>&1 | tee -a "$LOG_FILE"
    else
      log_error "gh CLI not found — cannot create PR. Push manually."
    fi
  fi

  if [ "$pipeline_failed" = true ]; then
    exit 1
  fi
}

main
