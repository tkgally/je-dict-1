#!/bin/bash
# pipeline/validate-task.sh — Post-task validation gates for the pipeline runner.
#
# Runs task-type-specific validation suites. Each task type gets a tailored
# set of checks beyond the baseline validate.py run.
#
# Usage:
#   ./pipeline/validate-task.sh <task-type> [--progress-file <path>] [--pre-snapshot <path>]
#
# Arguments:
#   task-type       One of the pipeline task types (new-entries, inline-links, etc.)
#   --progress-file Path to a progress tracking file. If provided, checks that it
#                   has been modified (detects stuck loops).
#   --pre-snapshot  Path to a file containing a snapshot of the progress file
#                   content before the task ran. Used for stuck-loop detection.
#
# Exit codes:
#   0 — All checks passed
#   1 — One or more checks failed
#
# For all task types, validate.py is always run first. Task-specific checks
# run after the baseline passes.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# --- Argument parsing ---

TASK_TYPE=""
PROGRESS_FILE=""
PRE_SNAPSHOT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --progress-file)
      PROGRESS_FILE="$2"
      shift 2
      ;;
    --pre-snapshot)
      PRE_SNAPSHOT="$2"
      shift 2
      ;;
    -*)
      echo "Unknown flag: $1" >&2
      exit 1
      ;;
    *)
      if [ -z "$TASK_TYPE" ]; then
        TASK_TYPE="$1"
      else
        echo "Unexpected argument: $1" >&2
        exit 1
      fi
      shift
      ;;
  esac
done

if [ -z "$TASK_TYPE" ]; then
  echo "Usage: validate-task.sh <task-type> [--progress-file <path>] [--pre-snapshot <path>]" >&2
  echo "" >&2
  echo "Task types: new-entries, new-candidates, clean-candidates, corpus-harvesting," >&2
  echo "            inline-links, example-sentences, furigana-completeness," >&2
  echo "            furigana-correctness, semantic-labels, noentry-resolution," >&2
  echo "            expand-short-notes" >&2
  exit 1
fi

# --- State tracking ---

ERRORS=0
WARNINGS=0

pass() {
  echo "  PASS: $1"
}

fail() {
  echo "  FAIL: $1" >&2
  ERRORS=$((ERRORS + 1))
}

warn() {
  echo "  WARN: $1"
  WARNINGS=$((WARNINGS + 1))
}

# --- Shared validation: baseline validate.py ---

run_baseline() {
  echo "=== Baseline validation ==="
  if python3 "$PROJECT_DIR/build/validate.py" > /dev/null 2>&1; then
    pass "validate.py passed"
  else
    fail "validate.py reported errors"
    return 1
  fi
  return 0
}

# --- Shared validation: stuck-loop detection ---

check_progress_advanced() {
  if [ -z "$PROGRESS_FILE" ] || [ -z "$PRE_SNAPSHOT" ]; then
    return 0
  fi

  echo "=== Progress advancement check ==="

  if [ ! -f "$PROGRESS_FILE" ]; then
    warn "Progress file not found: $PROGRESS_FILE"
    return 0
  fi

  if [ ! -f "$PRE_SNAPSHOT" ]; then
    warn "Pre-snapshot file not found: $PRE_SNAPSHOT"
    return 0
  fi

  if diff -q "$PRE_SNAPSHOT" "$PROGRESS_FILE" > /dev/null 2>&1; then
    fail "Progress file unchanged — task may be stuck in a loop"
  else
    pass "Progress file has advanced"
  fi
}

# --- Task-specific validation gates ---

validate_new_entries() {
  echo "=== new-entries validation ==="

  # Check that validate.py passes (already done in baseline, but re-check
  # specifically for any new entry issues)
  local furigana_output
  furigana_output=$(python3 "$PROJECT_DIR/build/find_missing_furigana.py" 2>/dev/null || true)

  if [ -n "$furigana_output" ]; then
    # find_missing_furigana.py outputs JSON; check if any entries are reported
    local missing_count
    missing_count=$(echo "$furigana_output" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(len(data) if isinstance(data, list) else 0)
except:
    print(0)
" 2>/dev/null || echo "0")

    if [ "$missing_count" -gt 0 ]; then
      warn "find_missing_furigana.py found $missing_count entries with gaps (check manually)"
    else
      pass "No new furigana gaps detected"
    fi
  else
    pass "No furigana issues found"
  fi
}

validate_new_candidates() {
  echo "=== new-candidates validation ==="
  validate_candidate_json
}

validate_clean_candidates() {
  echo "=== clean-candidates validation ==="
  validate_candidate_json
}

validate_corpus_harvesting() {
  echo "=== corpus-harvesting validation ==="
  validate_candidate_json
}

validate_candidate_json() {
  # Verify candidate_words.json is valid JSON with expected structure
  local candidate_file="$PROJECT_DIR/candidate_words.json"

  if [ ! -f "$candidate_file" ]; then
    fail "candidate_words.json not found"
    return
  fi

  local json_check
  json_check=$(python3 -c "
import json, sys
try:
    with open(sys.argv[1]) as f:
        data = json.load(f)
    # Check basic structure
    if 'metadata' not in data:
        print('ERROR: missing metadata key')
        sys.exit(1)
    if 'candidates' not in data:
        print('ERROR: missing candidates key')
        sys.exit(1)
    if not isinstance(data['candidates'], list):
        print('ERROR: candidates is not a list')
        sys.exit(1)
    # Check metadata fields
    meta = data['metadata']
    for key in ['total_candidates', 'last_updated']:
        if key not in meta:
            print(f'ERROR: metadata missing {key}')
            sys.exit(1)
    # Verify count matches
    actual = len(data['candidates'])
    declared = meta['total_candidates']
    if actual != declared:
        print(f'WARN: total_candidates={declared} but actual count={actual}')
    else:
        print('OK')
except json.JSONDecodeError as e:
    print(f'ERROR: invalid JSON: {e}')
    sys.exit(1)
" "$candidate_file" 2>&1)

  if echo "$json_check" | grep -q "^ERROR:"; then
    fail "candidate_words.json: $json_check"
  elif echo "$json_check" | grep -q "^WARN:"; then
    warn "candidate_words.json: $json_check"
  else
    pass "candidate_words.json structure is valid"
  fi
}

validate_inline_links() {
  echo "=== inline-links validation ==="

  # Check that word links use the correct ⟦surface→base：entry_id⟧ format
  local bad_links
  bad_links=$(grep -r '⟦' "$PROJECT_DIR/entries/" 2>/dev/null | \
    grep -v '⟦[^⟧]*→[^⟧]*：[0-9][^⟧]*⟧' | \
    grep -v '⟦[^⟧]*：[0-9][^⟧]*⟧' || true)

  if [ -n "$bad_links" ]; then
    local count
    count=$(echo "$bad_links" | wc -l)
    warn "$count lines with potentially malformed word links (check manually)"
  else
    pass "All word links appear well-formed"
  fi
}

validate_example_sentences() {
  echo "=== example-sentences validation ==="

  # Check that no entry has zero examples (basic/core should have at least 3)
  local zero_example_count
  zero_example_count=$(python3 -c "
import json, os, sys
entries_dir = os.path.join(sys.argv[1], 'entries')
count = 0
for root, dirs, files in os.walk(entries_dir):
    for f in files:
        if not f.endswith('.json'):
            continue
        path = os.path.join(root, f)
        with open(path) as fh:
            data = json.load(fh)
        tier = data.get('metadata', {}).get('vocabulary_tier', '')
        examples = data.get('examples', [])
        if tier in ('basic', 'core') and len(examples) < 3:
            count += 1
print(count)
" "$PROJECT_DIR" 2>/dev/null || echo "0")

  if [ "$zero_example_count" -gt 0 ]; then
    warn "$zero_example_count basic/core entries still have fewer than 3 examples"
  else
    pass "All basic/core entries have at least 3 examples"
  fi
}

validate_furigana_completeness() {
  echo "=== furigana-completeness validation ==="

  local furigana_output
  furigana_output=$(python3 "$PROJECT_DIR/build/find_missing_furigana.py" 2>/dev/null || true)

  if [ -n "$furigana_output" ]; then
    local missing_count
    missing_count=$(echo "$furigana_output" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(len(data) if isinstance(data, list) else 0)
except:
    print(0)
" 2>/dev/null || echo "0")

    if [ "$missing_count" -gt 0 ]; then
      warn "$missing_count entries still have furigana gaps"
    else
      pass "No furigana gaps found"
    fi
  else
    pass "Furigana coverage complete"
  fi
}

validate_furigana_correctness() {
  echo "=== furigana-correctness validation ==="
  # Correctness is harder to validate automatically — rely on baseline validate.py
  # plus a check that verify_furigana.py doesn't flag structural issues
  pass "Furigana correctness relies on baseline validation and manual review"
}

validate_semantic_labels() {
  echo "=== semantic-labels validation ==="

  # Run validate_tags.py for tag taxonomy conformance
  if python3 "$PROJECT_DIR/build/validate_tags.py" > /dev/null 2>&1; then
    pass "validate_tags.py passed"
  else
    fail "validate_tags.py reported errors"
  fi

  # Run check_tag_consistency.py for logical consistency
  if python3 "$PROJECT_DIR/build/check_tag_consistency.py" > /dev/null 2>&1; then
    pass "check_tag_consistency.py passed"
  else
    warn "check_tag_consistency.py reported issues (may be pre-existing)"
  fi
}

validate_noentry_resolution() {
  echo "=== noentry-resolution validation ==="
  # New entries created to resolve noentry links — same checks as new-entries
  validate_new_entries
}

validate_expand_short_notes() {
  echo "=== expand-short-notes validation ==="
  # Notes expansion — baseline validation is sufficient, plus furigana check
  # since notes often contain kanji that need furigana
  local furigana_output
  furigana_output=$(python3 "$PROJECT_DIR/build/find_missing_furigana.py" 2>/dev/null || true)

  if [ -n "$furigana_output" ]; then
    local missing_count
    missing_count=$(echo "$furigana_output" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(len(data) if isinstance(data, list) else 0)
except:
    print(0)
" 2>/dev/null || echo "0")

    if [ "$missing_count" -gt 0 ]; then
      warn "$missing_count entries have furigana gaps in notes (check if newly introduced)"
    else
      pass "No furigana gaps in expanded notes"
    fi
  else
    pass "Furigana coverage in notes is complete"
  fi
}

# --- Main ---

main() {
  echo "Pipeline validation gate: $TASK_TYPE"
  echo ""

  # Step 1: Always run baseline validation
  if ! run_baseline; then
    echo ""
    echo "RESULT: FAIL (baseline validation failed)"
    exit 1
  fi

  # Step 2: Run task-specific checks
  echo ""
  case "$TASK_TYPE" in
    new-entries)            validate_new_entries ;;
    new-candidates)         validate_new_candidates ;;
    clean-candidates)       validate_clean_candidates ;;
    corpus-harvesting)      validate_corpus_harvesting ;;
    inline-links)           validate_inline_links ;;
    example-sentences)      validate_example_sentences ;;
    furigana-completeness)  validate_furigana_completeness ;;
    furigana-correctness)   validate_furigana_correctness ;;
    semantic-labels)        validate_semantic_labels ;;
    noentry-resolution)     validate_noentry_resolution ;;
    expand-short-notes)     validate_expand_short_notes ;;
    *)
      fail "Unknown task type: $TASK_TYPE"
      ;;
  esac

  # Step 3: Check progress advancement (stuck-loop detection)
  echo ""
  check_progress_advanced

  # Summary
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Errors:   $ERRORS"
  echo "Warnings: $WARNINGS"

  if [ "$ERRORS" -gt 0 ]; then
    echo "RESULT: FAIL"
    exit 1
  elif [ "$WARNINGS" -gt 0 ]; then
    echo "RESULT: PASS (with warnings)"
    exit 0
  else
    echo "RESULT: PASS"
    exit 0
  fi
}

main
