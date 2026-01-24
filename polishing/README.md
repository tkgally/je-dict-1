# Dictionary Polishing System

This directory contains the task-based polishing framework for je-dict-1. Each polishing task focuses on a single aspect of entry quality, allowing thorough review without overlooking issues.

## Design Philosophy

- **One task, one focus**: Each polishing workflow checks only one specific feature per entry
- **Semantic tasks**: These tasks require human/AI knowledge and cannot be automated
- **Minimal progress tracking**: Only the next entry to process is recorded
- **Nonstop workflow**: Uses context reset procedure to work continuously

## Directory Structure

```
polishing/
├── README.md                           # This file
├── tasks/                              # Task-specific progress tracking
│   ├── furigana-completeness/
│   │   └── progress.txt                # Next entry to check
│   ├── furigana-correctness/
│   │   └── progress.txt                # Next entry to check
│   └── example-sentences/
│       └── progress.txt                # Next entry to check
└── sessions/                           # Session logs for context continuation
    └── {task}_{date}_{nnn}.md          # Session continuation notes
```

## Available Tasks

### 1. Furigana Completeness (`polish_furigana_completeness.md`)

Checks whether all kanji in an entry have furigana markup. This is a **semantic task** that requires knowledge of Japanese readings - it cannot be automated.

**What it checks:**
- Headword furigana
- Example sentence furigana
- Notes field furigana
- Cross-reference furigana

### 2. Furigana Correctness (`polish_furigana_correctness.md`)

Checks whether existing furigana readings are correct. This is a **semantic task** that requires knowledge of Japanese readings - it cannot be automated.

**What it checks:**
- Correct readings for all kanji
- Proper rendaku/compound readings
- Context-appropriate readings (e.g., 今日 as きょう vs こんにち)

### 3. Example Sentences (`polish_example_sentences.md`)

Checks example sentence count, vocabulary level compliance, and appropriateness. This is a **semantic task** (except counting) that requires language knowledge.

**What it checks:**
- Minimum example counts per sense (5 for basic/core, 3 for general)
- Vocabulary tier restrictions for basic and core entries
- Progressive length requirement
- Natural and appropriate examples

## Progress Tracking

Each task has a minimal `progress.txt` file containing only:

```
next: 00001
```

This allows quick context loading. When starting a task, read this file to find where to continue.

## Session Logs

When context runs low, write a session log to `sessions/` before resetting:

```
sessions/{task-name}_{YYYYMMDD}_{NNN}.md
```

Include:
- Last entry reviewed
- Next entry to process
- Any patterns or issues discovered
- Brief notes for continuation

## Adding New Tasks

1. Create a directory in `tasks/{task-name}/`
2. Create `progress.txt` with `next: 00001`
3. Create prompt at `prompts/polish_{task_name}.md`
4. Add task description to this README

## Related Files

- **Prompts**: `prompts/polish_*.md`
- **Skills**: `.claude/skills/example-sentences/SKILL.md`, `.claude/skills/vocabulary-notes/SKILL.md`
- **Validation**: `build/verify_furigana.py`, `build/validate.py`
