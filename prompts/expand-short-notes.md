# Expand Short Notes

Systematically expand the `notes` field for dictionary entries that currently have inadequate notes (under 300 characters). This is a **semantic task** that requires your knowledge of Japanese vocabulary, grammar, and usage patterns - it cannot be automated because writing comprehensive learner-focused notes requires understanding word meanings, common patterns, and potential learner difficulties.

## Task Focus

**Single focus**: Do the notes provide adequate guidance for learners?

Entries with notes under 300 characters typically contain only:
- A single etymology note (e.g., "From English 'computer'")
- A single related word (e.g., "Related: X")
- A simple antonym/synonym reference

These need to be expanded to include structured, learner-focused content following the vocabulary-notes skill guidelines.

## Reference Skill

Load the skill file for detailed formatting and content requirements:
```
.claude/skills/vocabulary-notes/SKILL.md
```

## Tracking File

Progress is tracked in:
```
prompts/expand-short-notes-tracking.txt
```

Format: `STATUS | ID | HEADWORD | NOTES_LENGTH | TIER | POS`

Status values:
- `pending` - Not yet processed
- `in_progress` - Currently being worked on (should only be one at a time)
- `completed` - Notes have been expanded
- `skipped` - Intentionally skipped (with reason noted in session log)

## Starting Point

```bash
grep "^pending" prompts/expand-short-notes-tracking.txt | head -1
```

This shows the next entry to process (entries are sorted by notes length, shortest first).

## Workflow

1. **Read the tracking file** to find the next pending entry

2. **Load the entry** and read its current content:
   - Headword, reading, part of speech
   - All definitions with explanations
   - Current notes (to understand what's already there)
   - Examples (for context on usage)

3. **Write comprehensive new notes** following the vocabulary-notes skill:

   **For verbs**, include:
   - Core semantic explanation
   - TRANSITIVITY section (type and pair if exists)
   - ASPECT section (what ている means)
   - COMMON PATTERNS (3-5 typical collocations)
   - Any register, formality, or common mistake notes

   **For nouns**, include:
   - Core semantic explanation (scope, meaning beyond gloss)
   - COMMON EXPRESSIONS (typical collocations)
   - Related words if helpful
   - Register or domain notes if applicable

   **For adjectives**, include:
   - Whether i-adjective or na-adjective
   - FORMS (adverbial, noun form)
   - SIMILAR WORDS distinctions if applicable
   - Common collocations

   **For adverbs/other**, include:
   - Core meaning and usage context
   - Contrast with similar words
   - Common patterns or collocations
   - Register notes if applicable

4. **Critical requirements**:
   - **ALL kanji must have furigana**: `{漢字|かな}` format
   - Use blank lines between sections
   - Use bullet points for lists of 2+ items
   - Use UPPERCASE section headers with colons
   - Target 300-600 characters for most entries

5. **Update the entry**:
   - Replace the `notes` field with new content
   - Update the `modified` timestamp:
     ```bash
     python3 build/get_timestamp.py
     ```
   - Save the entry

6. **Verify furigana**:
   ```bash
   python3 build/verify_furigana.py ENTRY_ID
   ```
   Fix any missing furigana before continuing.

7. **Update tracking file**: Change status from `pending` to `completed`

8. **After every 10-15 entries**:
   - Run validation and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Expand short notes: XXXXX-XXXXX"
     ```

9. **When finishing** (end of session or context getting long):
   a. Update tracking file with current progress
   b. Write session log to `polishing/sessions/expand-short-notes_{date}_{nnn}.md`:
      ```
      ## Session: Expand Short Notes
      Date: YYYY-MM-DD
      Entries processed: XXXXX-XXXXX

      ### Entries Expanded
      - [entry_id]: [headword] - [brief note about what was added]

      ### Entries Skipped (if any)
      - [entry_id]: [reason]

      ### Statistics
      - Entries completed this session: N
      - Total remaining: N

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes

## What Good Expanded Notes Look Like

### Before (inadequate - 54 chars):
```
From German "Arbeit" (work). Often abbreviated to バイト.
```

### After (comprehensive - ~400 chars):
```
アルバイト refers to part-time or temporary work, commonly done by students.

ETYMOLOGY:
From German "Arbeit" (work). Often abbreviated to バイト in casual speech.

COMMON EXPRESSIONS:
- アルバイトをする: to work part-time
- アルバイトを{探|さが}す: to look for a part-time job
- アルバイト{先|さき}: part-time workplace

USAGE:
Typically refers to jobs taken by students or as secondary income. For full-time irregular work, {派遣|はけん} or {契約|けいやく}{社員|しゃいん} is more common.
```

### Before (inadequate - 38 chars):
```
Opposite of {最高|さいこう} (highest, best).
```

### After (comprehensive - ~450 chars):
```
{最低|さいてい} can function as a noun, na-adjective, or adverb meaning "lowest" or "minimum."

MEANINGS:
1. Lowest point/degree: {最低|さいてい}{気温|きおん} (lowest temperature)
2. Minimum required: {最低|さいてい}{限度|げんど} (minimum limit)
3. Terrible/awful (colloquial): あいつは{最低|さいてい}だ (He's the worst)

COMMON PATTERNS:
- {最低|さいてい}でも: at the very least
- {最低限|さいていげん}: bare minimum

CONTRAST:
Opposite of {最高|さいこう} (highest, best, maximum).
```

## Why This Cannot Be Automated

Writing good notes requires:
- **Semantic knowledge**: Understanding what a word means and how it's used
- **Learner perspective**: Knowing what causes confusion or mistakes
- **Collocation awareness**: Identifying natural word pairings
- **Register sensitivity**: Knowing formality and context appropriateness
- **Cross-reference awareness**: Linking to related words meaningfully

Only a knowledgeable writer can produce notes that genuinely help learners.

## Priority Order

The tracking file is sorted by notes length (shortest first), so:
- Entries under 100 chars are most urgently in need of expansion
- Entries 100-200 chars likely need substantial additions
- Entries 200-300 chars may need moderate enhancement

## Common Patterns to Add

Based on part of speech, consider adding:

| POS | Essential Content |
|-----|-------------------|
| Verb | Transitivity, aspect (ている), particles, collocations |
| Noun | Scope clarification, compounds, common expressions |
| Adjective | Forms, similar word distinctions, collocations |
| Adverb | Context of use, contrast with synonyms, sentence position |
| Counter | What it counts, alternative readings, common numbers |

## Progress Update Format

Update the tracking file by changing `pending` to `completed`:
```
# Before
pending | 01529_oobaa | オーバー | 26 | general | noun

# After
completed | 01529_oobaa | オーバー | 26 | general | noun
```

## Output at Session End

When stopping, report:
1. Entry range processed
2. Number of entries expanded
3. Number of entries skipped (with reasons)
4. Next entry to continue from
5. Estimated remaining entries
