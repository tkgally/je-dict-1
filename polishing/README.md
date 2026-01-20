# Dictionary Polishing System

This directory contains the infrastructure for systematic review, improvement, and quality assurance of dictionary entries. The system is designed to support ongoing refinement as the dictionary grows and evolves.

## Overview

The polishing system provides:
1. **Systematic review** - Methodical checking of entries by category, field, or criteria
2. **Progress tracking** - Records of what has been reviewed and when
3. **Issue management** - Documentation of problems found and their resolutions
4. **Session continuity** - Notes and context for resuming work across conversations
5. **Task prompts** - Specific review procedures for different aspects of entries

## Directory Structure

```
polishing/
├── README.md              # This file
├── config.json            # System configuration and review criteria
├── progress.json          # Master tracking of review status by entry
├── issues.json            # Problems found, solutions, and patterns
├── queue.json             # Prioritized review queue
├── sessions/              # Individual session logs
│   └── session_YYYYMMDD_NNN.json
└── tasks/                 # Review task prompts
    ├── full-review.md           # Complete entry review checklist
    ├── cross-references.md      # Cross-reference validation
    ├── examples.md              # Example quality review
    ├── notes-consistency.md     # Notes field standardization
    ├── definitions.md           # Definition clarity review
    ├── tags.md                  # Tag accuracy review
    └── furigana.md              # Furigana completeness check
```

## How to Use

### Starting a Polishing Session

1. Point Claude to the appropriate task prompt in `tasks/`
2. Claude will check `progress.json` to find entries needing review
3. Claude will systematically review entries, recording changes
4. At session end, Claude updates all tracking files and summarizes work

### Invoking the Polishing Skill

Use the `/polish` skill to start a polishing session:
```
/polish                    # Start with default settings (next batch from queue)
/polish --task full-review # Run a specific review task
/polish --entries 100-150  # Review specific entry range
/polish --category verbs   # Focus on a specific part of speech
```

### Understanding the Tracking Files

#### progress.json
Tracks the review status of every entry:
- `last_reviewed`: When the entry was last fully reviewed
- `review_count`: How many times it has been reviewed
- `status`: current | needs_review | flagged | skip
- `notes`: Any reviewer notes about this entry

#### issues.json
Tracks patterns and problems:
- `open`: Issues that need attention
- `resolved`: Issues that have been fixed (with solutions)
- `patterns`: Recurring problems to watch for
- `improvements`: Suggestions for better practices

#### queue.json
Maintains a prioritized list of entries to review:
- Entries flagged for issues
- Entries never reviewed
- Entries with stale reviews (older than threshold)
- Randomly sampled entries for spot-checking

## Review Criteria

Each review checks entries against these quality standards:

### Required Fields
- [ ] Valid ID format matching filename
- [ ] Headword with proper furigana on all kanji
- [ ] Reading in hiragana only
- [ ] Appropriate part_of_speech
- [ ] Clear, accurate gloss
- [ ] Complete metadata with all required tags

### Content Quality
- [ ] Definitions are clear and distinguish senses
- [ ] Examples illustrate actual usage
- [ ] Notes provide genuinely helpful information
- [ ] Cross-references point to valid, related entries
- [ ] No redundant or contradictory information

### Consistency
- [ ] Formatting matches project conventions
- [ ] Tag usage aligns with taxonomy
- [ ] Similar entries are structured similarly
- [ ] Terminology is consistent across entries

### Accuracy
- [ ] Japanese text is correct
- [ ] English translations are accurate
- [ ] Grammar explanations are correct
- [ ] Cultural notes are appropriate

## Session Workflow

1. **Load context** - Read progress.json and queue.json
2. **Select batch** - Choose entries to review based on task
3. **Review entries** - Apply checklist, make improvements
4. **Record changes** - Log all modifications with timestamps
5. **Update tracking** - Mark entries as reviewed, update issues
6. **Summarize** - Report changes to user for approval

## Integration with Existing Systems

This system complements the existing validation tools:
- `build/validate.py` - Structural validation (run before/after polishing)
- `build/validate_tags.py` - Tag consistency checking
- `.claude/skills/revise-entries/` - Guidelines for revising entries

The polishing system focuses on content quality and consistency that automated validation cannot fully check.

## Scalability

The system is designed to handle the growing dictionary:
- Entries are reviewed in manageable batches
- Progress tracking enables resumption across sessions
- Issues are categorized for efficient batch fixing
- Random sampling ensures ongoing quality monitoring
