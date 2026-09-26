# Dictionary Polishing System

This directory contains the polishing framework for je-dict-1. The default ongoing task is **comprehensive polish** (`prompts/comprehensive_polish.md`), which walks entries one at a time and applies all quality dimensions in a single session. Several **targeted polish prompts** also exist for special-purpose sweeps.

## Design Philosophy

- **Comprehensive polish is the default scheduled workflow**: each session works on up to 5 entries with a tiered checklist (must-do / should-do / nice-to-have) and logs longer-term observations for follow-up.
- **Targeted polish tasks remain available**: each targets one quality dimension (furigana, examples, inline links, etc.) and is useful for focused sweeps.
- **Minimal progress tracking**: only the next entry to process is recorded per task.
- **Long-term observations**: comprehensive polish appends `[pattern]`, `[wiki]`, `[article]`, `[tooling]`, `[skill]`, and `[entry]` notes to `polishing/observations.md` for the daily wiki-maintenance session to harvest.

## Directory Structure

```
polishing/
├── README.md                           # This file
├── observations.md                     # Long-term observations harvested by wiki maintenance
├── tasks/                              # Task-specific progress tracking
│   ├── comprehensive/
│   │   ├── progress.txt                # Next entry for comprehensive polish (DEFAULT TASK)
│   │   └── README.md
│   ├── furigana-completeness/
│   │   └── progress.txt                # Targeted task
│   ├── furigana-correctness/
│   │   └── progress.txt                # Targeted task
│   ├── example-sentences/
│   │   └── progress.txt                # Targeted task
│   └── semantic-labels/
│       └── progress.txt                # Targeted task
├── priority/                           # Priority-ordered entry lists for targeted tasks
│   ├── cross_refs.txt
│   ├── examples.txt
│   ├── furigana.txt
│   └── notes.txt
└── sessions/                           # Session logs for context continuation
    └── {task}_{date}_{nnn}.md          # Session continuation notes
```

## Available Tasks

### 0. Comprehensive Polish — DEFAULT (`prompts/comprehensive_polish.md`)

Unified ongoing-improvement task. Each session processes up to 5 entries with a tiered checklist covering all quality dimensions and logs observations for long-term improvements. **This is the task to use unless you have a specific reason to run a targeted sweep.**

**What it covers:**
- Tier 1 (must-do): schema validity, furigana completeness, link/cross-ref resolution, sense_numbers, typo check
- Tier 2 (should-do): example count and quality, note quality, tags, transitivity/aspect, cross-reference symmetry on direct neighbors
- Tier 3 (nice-to-have): sentence naturalness, note expansion, inline word links

**Side effects:**
- Words found in examples/notes without entries → added to `candidate_words.json` (highest priority for new-entry sessions)
- Systemic patterns and longer-horizon ideas → appended to `polishing/observations.md`

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

### 4. Semantic Labels (`polish_semantic_labels.md`)

Checks whether semantic tags in `metadata.tags.semantic` accurately reflect each word's meaning. This is a **semantic task** that requires understanding Japanese vocabulary - it cannot be automated.

**What it checks:**
- Tags match the word's actual semantic category
- No template artifacts (wrong default tags like "building" on unrelated words)
- Appropriate specificity
- Verbs use action categories, not object categories
- Consistency with similar words

**Common issues:**
- Template artifacts: Words with irrelevant default tags
- Verbs tagged with object categories instead of action categories
- Multiple unrelated tags suggesting copy-paste errors

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

## Long-Term Observations

`polishing/observations.md` is an append-only log used by the comprehensive polish workflow. Sessions add tagged observations (`[pattern]`, `[wiki]`, `[article]`, `[tooling]`, `[skill]`, `[entry]`) about issues that go beyond a single entry. The daily wiki-maintenance session (`planning/maintain-knowledge-base.md`) harvests this file: actionable items get filed into the wiki or scheduled as concrete work, and processed entries are pruned.

## Related Files

- **Prompts**: `prompts/polish_*.md`
- **Skills**: `.claude/skills/example-sentences/SKILL.md`, `.claude/skills/vocabulary-notes/SKILL.md`
- **Validation**: `build/verify_furigana.py`, `build/validate.py`, `build/validate_tags.py`
- **Tag taxonomy**: `build/tag_taxonomy.json`
