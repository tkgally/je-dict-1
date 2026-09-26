# Note Quality Standardization

**Enhancement plan section**: [1.1.2] Note Quality Standardization

Define POS-specific note templates, build a scoring tool, and update documentation so that note quality can be measured and the weakest entries prioritized for improvement.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `build/note_templates.json` | **Create** | POS-specific note section definitions with required/optional sections and length thresholds |
| `build/score_note_quality.py` | **Create** | Score each entry's notes against its POS template (0-100) |
| `.claude/skills/vocabulary-notes/SKILL.md` | **Modify** | Add POS template reference section |
| `CLAUDE.md` | **Modify** | Document `score_note_quality.py` in essential commands |
| `Makefile` | **Modify** | Add `note-scores` target |

---

## Part A: Define POS Note Templates [1.1.2]

**Goal**: Codify the expected note structure for each major POS into a machine-readable data file that the scorer can use.

### Step A1: Read the current vocabulary-notes skill

```bash
cat .claude/skills/vocabulary-notes/SKILL.md
```

Note the existing "Structure Templates" section (Verb Notes Template, Noun Notes Template, Adjective Notes Template, Simple Entry Template). The new data file formalizes these into a scorable format.

### Step A2: Create `build/note_templates.json`

Create the file at `build/note_templates.json` with the following structure. Each POS key maps to a template object defining required sections, optional sections, and minimum note length.

```json
{
  "_comment": "POS note templates for score_note_quality.py. Sections are matched case-insensitively against section headers in notes (e.g., 'TRANSITIVITY:', 'COMMON PATTERNS:').",
  "verb-ichidan": {
    "required_sections": ["transitivity", "common patterns"],
    "optional_sections": ["aspect", "collocations", "particles", "similar verbs", "register", "negative usage", "keigo"],
    "min_length": 120,
    "expected_order": ["transitivity", "aspect", "common patterns", "similar verbs", "register"]
  },
  "verb-godan": {
    "required_sections": ["transitivity", "common patterns"],
    "optional_sections": ["aspect", "collocations", "particles", "similar verbs", "register", "negative usage", "keigo"],
    "min_length": 120,
    "expected_order": ["transitivity", "aspect", "common patterns", "similar verbs", "register"]
  },
  "verb-suru": {
    "required_sections": ["common patterns"],
    "optional_sections": ["transitivity", "aspect", "collocations", "particles", "similar verbs", "register", "keigo"],
    "min_length": 100,
    "expected_order": ["transitivity", "aspect", "common patterns", "similar verbs", "register"]
  },
  "verb-irregular": {
    "required_sections": ["common patterns"],
    "optional_sections": ["transitivity", "aspect", "collocations", "particles", "similar verbs", "register", "keigo"],
    "min_length": 100,
    "expected_order": ["transitivity", "aspect", "common patterns", "similar verbs", "register"]
  },
  "adjective-na": {
    "required_sections": ["usage"],
    "optional_sections": ["predicate vs. modifier", "collocations", "similar adjectives", "register", "forms"],
    "min_length": 80,
    "expected_order": ["usage", "predicate vs. modifier", "collocations", "similar adjectives", "register"]
  },
  "adjective-i": {
    "required_sections": ["usage"],
    "optional_sections": ["forms", "collocations", "similar adjectives", "register"],
    "min_length": 80,
    "expected_order": ["usage", "forms", "collocations", "similar adjectives", "register"]
  },
  "adjective-no": {
    "required_sections": ["usage"],
    "optional_sections": ["collocations", "similar adjectives", "register"],
    "min_length": 60,
    "expected_order": ["usage", "collocations", "similar adjectives", "register"]
  },
  "noun": {
    "required_sections": [],
    "optional_sections": ["common expressions", "collocations", "compounds", "similar words", "cultural context"],
    "min_length": 60,
    "expected_order": ["common expressions", "compounds", "similar words", "cultural context"]
  },
  "adverb": {
    "required_sections": [],
    "optional_sections": ["collocations", "position in sentence", "similar adverbs", "register"],
    "min_length": 60,
    "expected_order": ["collocations", "position in sentence", "similar adverbs"]
  },
  "particle": {
    "required_sections": ["functions"],
    "optional_sections": ["patterns", "contrasts", "common mistakes"],
    "min_length": 100,
    "expected_order": ["functions", "patterns", "contrasts", "common mistakes"]
  },
  "counter": {
    "required_sections": ["counting patterns"],
    "optional_sections": ["range", "exceptions", "similar counters"],
    "min_length": 80,
    "expected_order": ["counting patterns", "range", "exceptions", "similar counters"]
  },
  "expression": {
    "required_sections": [],
    "optional_sections": ["usage context", "formality", "similar expressions", "cultural context"],
    "min_length": 60,
    "expected_order": ["usage context", "formality", "similar expressions", "cultural context"]
  },
  "_default": {
    "required_sections": [],
    "optional_sections": [],
    "min_length": 40,
    "expected_order": []
  }
}
```

**Design notes**:

- Section names are lowercase and matched against note text case-insensitively. A section is considered present if the note contains a header like `TRANSITIVITY:`, `Common Patterns:`, or `## Transitivity` (the matcher should be flexible about header formatting).
- The `_default` template is a fallback for any POS not explicitly listed.
- `min_length` is measured in characters after stripping furigana markup and whitespace.
- `expected_order` is advisory only (the scorer gives a small bonus for correct ordering, not a penalty for wrong ordering).

### Step A3: Verify the template covers all POS values

Read the schema to find all valid `part_of_speech` values:

```bash
python3 -c "
import json
with open('build/schema.json') as f:
    schema = json.load(f)
pos_enum = schema['properties']['part_of_speech']['enum']
print('\n'.join(sorted(pos_enum)))
"
```

Cross-check that every POS value in the schema either has an explicit template key in `note_templates.json` or is covered by `_default`. If a POS is missing a template but has a natural note structure (e.g., `prefix`, `suffix`, `conjunction`), it is fine for it to fall through to `_default`.

---

## Part B: Build Note Quality Scorer [1.1.2]

**Goal**: Create a script that scores every entry's notes against its POS template and outputs actionable data.

### Step B1: Create `build/score_note_quality.py`

Create the script at `build/score_note_quality.py`. It should:

1. **Load entries** from `entries_index.json` and individual entry files (for notes content).
2. **Load templates** from `build/note_templates.json`.
3. **Determine the template** for each entry based on `part_of_speech`. Map the POS value to the template key:
   - Direct match first (e.g., `verb-godan` -> `verb-godan`)
   - If no direct match, try prefix match (e.g., `verb-godan-u` -> `verb-godan` if that existed)
   - Fall back to `_default`
4. **Score each entry's notes** (0-100 points) using this rubric:

| Criterion | Points | How to check |
|-----------|--------|--------------|
| Notes field exists and is non-empty | 10 | `notes` is not null/empty |
| Meets minimum length | 15 | Character count of notes (stripped of furigana markup) >= `min_length` |
| Has section headers | 10 | At least one line matching `^[A-Z][A-Z /()-]+:` or `^### ` pattern |
| Has bullet points for lists | 10 | Contains `\n- ` pattern |
| Has paragraph breaks | 5 | Contains `\n\n` (blank line separations) |
| Contains required sections | 30 (split evenly) | Each required section header found = `30 / len(required_sections)` points. If no required sections defined, award full 30. |
| Contains optional sections | 15 (split evenly) | Each optional section found = `15 / len(optional_sections)` points, capped at 15. |
| Furigana on kanji in notes | 5 | No bare kanji detected in notes text |

**Total possible: 100 points.**

For entries with no notes field at all, score = 0.

5. **Parse section headers flexibly**: Match both `SECTION_NAME:` (uppercase with colon) and natural text mentions. The matcher should:
   - Normalize to lowercase
   - Strip punctuation
   - Match against each required/optional section name
   - Accept variants: "TRANSITIVITY:" matches "transitivity", "TRANSITIVE/INTRANSITIVE:" matches "transitivity", "COMMON PATTERNS:" matches "common patterns"

6. **Command-line interface**:

```
usage: score_note_quality.py [-h] [--tier TIER] [--pos POS] [--below N]
                              [--above N] [--json] [--summary] [--id ID]

Options:
  --tier TIER    Filter by vocabulary tier (basic, core, general)
  --pos POS      Filter by part of speech (e.g., verb-godan, noun)
  --below N      Show only entries scoring below N
  --above N      Show only entries scoring above N
  --json         Output as JSON (array of {id, headword, pos, tier, score, breakdown})
  --summary      Show summary statistics only (no individual entries)
  --id ID        Score a single entry by ID
```

7. **Default output** (no flags): Print each entry on one line, sorted by score ascending (worst first):

```
Score  ID                    POS            Tier     Headword
  12   00234_ageru           verb-ichidan   basic    {上|あ}げる
  18   00567_ookii           adjective-i    basic    {大|おお}きい
  23   01234_sanpo           verb-suru      core     {散歩|さんぽ}する
...
```

8. **Summary mode** (`--summary`): Print aggregated statistics:

```
NOTE QUALITY SUMMARY
====================

Total entries scored: 23,456
Average score: 47.3

Score Distribution:
  0-19:    2,345 entries (10.0%)
  20-39:   5,678 entries (24.2%)
  40-59:   8,901 entries (37.9%)
  60-79:   4,567 entries (19.5%)
  80-100:  1,965 entries  (8.4%)

Average by POS:
  verb-ichidan:    52.1  (1,234 entries)
  verb-godan:      48.7  (2,345 entries)
  noun:            41.2  (8,765 entries)
  ...

Average by Tier:
  basic:    62.4  (801 entries)
  core:     55.1  (1,982 entries)
  general:  44.8  (20,673 entries)

Lowest-Scoring Entries (bottom 10):
  00234_ageru            12   verb-ichidan   basic
  ...
```

### Step B2: Make the script executable and test it

```bash
chmod +x build/score_note_quality.py
python3 build/score_note_quality.py --summary
python3 build/score_note_quality.py --tier basic --below 30
python3 build/score_note_quality.py --id 00001_au
python3 build/score_note_quality.py --json --below 20 | python3 -m json.tool | head -40
```

Verify the output is sensible. Check a few entries manually to confirm the scores align with actual note quality. Adjust the scoring weights if the results seem systematically wrong (e.g., if most entries with decent notes score below 30, the weights may need rebalancing).

### Step B3: Handle edge cases

- Entries with `notes: null` or `notes: ""` should score 0
- Entries where `part_of_speech` is missing or unrecognized should use the `_default` template
- The script should handle entries with very long notes gracefully (no truncation)
- Furigana check: use the same `is_kanji` / `FURIGANA_PATTERN` utilities from `build/japanese_utils.py` if available
- If `note_templates.json` cannot be loaded, print an error and exit 1

---

## Part C: Update vocabulary-notes Skill [1.1.2]

**Goal**: Add a POS template reference to the skill so that future entry creation and note-writing sessions are aware of the expected structure.

### Step C1: Read the current skill

```bash
cat .claude/skills/vocabulary-notes/SKILL.md
```

### Step C2: Add a POS template reference section

At the end of the skill file (before the closing section or at the very bottom), add a new section:

```markdown
## POS Note Templates (Machine-Readable)

The expected note structure for each POS is defined in `build/note_templates.json`. This file is used by `build/score_note_quality.py` to score note quality. When writing notes, aim to include the required sections for the entry's POS:

| POS | Required Sections | Min Length |
|-----|-------------------|------------|
| verb-ichidan, verb-godan | transitivity, common patterns | 120 chars |
| verb-suru, verb-irregular | common patterns | 100 chars |
| adjective-na, adjective-i | usage | 80 chars |
| adjective-no | usage | 60 chars |
| noun | (none required) | 60 chars |
| adverb | (none required) | 60 chars |
| particle | functions | 100 chars |
| counter | counting patterns | 80 chars |
| expression | (none required) | 60 chars |

Optional sections (bonus quality): collocations, similar words, register, cultural context, forms, aspect, etc. See `build/note_templates.json` for the complete list per POS.

To check an entry's note quality score:
```bash
python3 build/score_note_quality.py --id ENTRY_ID
```
```

**Important**: Do not restructure the existing content of the skill file. Only append the new section.

---

## Part D: Update CLAUDE.md and Makefile [1.1.2]

### Step D1: Update CLAUDE.md essential commands

In the "Essential commands" section of CLAUDE.md, in the "Reports" sub-area (near `python3 build/report.py`), add:

```bash
python3 build/score_note_quality.py --summary   # Note quality score distribution
python3 build/score_note_quality.py --below 30   # Entries with worst notes
```

### Step D2: Update the Makefile

Add a new target to the Makefile:

```makefile
note-scores:
	python3 build/score_note_quality.py --summary
```

Add `note-scores` to the `.PHONY` line at the top.

### Step D3: Update CLAUDE.md Makefile shortcuts

In the "Essential commands" section where Makefile shortcuts are listed, add:

```bash
make note-scores                          # note quality score distribution
```

---

## Verification

After all parts are complete, run these checks:

```bash
# Verify the template file is valid JSON
python3 -c "import json; json.load(open('build/note_templates.json')); print('OK: note_templates.json is valid')"

# Verify the scorer runs
python3 build/score_note_quality.py --summary

# Verify scoring for specific tiers
python3 build/score_note_quality.py --tier basic --summary
python3 build/score_note_quality.py --tier core --summary

# Verify single-entry scoring
python3 build/score_note_quality.py --id 00001_au

# Verify JSON output
python3 build/score_note_quality.py --json --below 10 | python3 -m json.tool | head -20

# Verify the skill file still renders cleanly (no syntax errors in markdown)
head -5 .claude/skills/vocabulary-notes/SKILL.md

# Full validation still passes
make validate
```

Fix any issues found during verification.

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Run `make build`** to ensure all build artifacts are up to date
2. **Stage and commit all changes**:
   ```bash
   git add -A
   git commit -m "Add note quality scoring system [1.1.2]

   - Create build/note_templates.json with POS-specific note section definitions
   - Create build/score_note_quality.py to score notes 0-100 against POS templates
   - Update vocabulary-notes skill with POS template reference table
   - Add make note-scores target and CLAUDE.md documentation"
   ```
3. **Push** to the feature branch
4. **Create a PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "Note quality scoring system [1.1.2]" --body "..."`
5. **Poll CI status** every 60 seconds: `gh pr checks <number> --repo tkgally/je-dict-1` (allow up to 10 minutes)
6. **Squash-merge** once CI is green: `gh pr merge <number> --repo tkgally/je-dict-1 --squash`
7. **If CI fails**: read the error with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat
8. **Post-merge cleanup**:
   ```bash
   git checkout main && git pull origin main
   git status  # Should show nothing to commit
   git branch -d <branch-name>
   git push origin --delete <branch-name>
   ```

**CRITICAL**: The PR must include rebuilt `docs/` files from `make build`. If you commit source changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
