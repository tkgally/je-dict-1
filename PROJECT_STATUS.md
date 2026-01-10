# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-10
**Current phase**: Phase 4 - N4 Vocabulary Expansion & Interface Enhancement

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 4: N4 Vocabulary Expansion & Interface Enhancement** - Adding N4 vocabulary while maintaining v2 quality standards, plus new web interface features.

### Infrastructure Status
- [x] Directory structure created
- [x] JSON schema defined (`build/schema.json`)
- [x] Validation script working (`build/validate.py`)
- [x] Build script working (`build/build.py`)
- [x] Web interface functional with search
- [x] Furigana system with toggle
- [x] Claude Code skills for entry guidelines
- [x] Quality specification v2 from multi-model evaluation
- [x] Vocabulary-notes skill for formatting guidelines
- [x] Notes field supports paragraph breaks and bullet points
- [x] Multiple interface modes (Search, Browse, Recent, Random)
- [x] Sticky header with interface toggle
- [x] Last updated date in footer
- [x] Cross-reference linking system with UI navigation

### Content Status
- **Total entries**: 2,024
- **JLPT N5 coverage**: ~95% complete
- **JLPT N4 coverage**: 392 entries added
- **JLPT N3 vocabulary**: 50+ entries added
- **Candidate words**: ~1,980 words tracked in `candidate_words.json`
- **Cross-references**: 302 resolved links, 159 extractable from existing notes

### Entry Breakdown by JLPT Level
| Level | Count | Status |
|-------|-------|--------|
| N5 | ~761 | Complete |
| N4 | ~392 | In progress |

### Entry Breakdown by Type
| Type | Count | Notes |
|------|-------|-------|
| Verbs | ~220 | Includes 95 N4 verbs with transitivity info |
| Nouns | ~430 | Includes N4 nouns, katakana loanwords |
| Adjectives | ~100 | I-adjectives and na-adjectives |
| Adverbs | ~56 | Includes 11 new N4 adverbs |
| Particles | 9 | Core particles with predicate lists |
| Counters | ~21 | Common counting patterns |
| Keigo verbs | 12 | Honorific and humble forms |
| Other | ~150 | Expressions, suffixes, etc. |

## v2 Quality Standards

Based on multi-model LLM evaluation (Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash), these are the priority enhancements:

### HIGH PRIORITY
1. **Verb transitivity** - Add 自動詞/他動詞 and pair verbs to all verb entries
2. **Aspect notes** - Explain ている behavior for verbs with non-obvious meanings
3. **Particle predicate lists** - List verbs/adjectives requiring each particle
4. **Collocation patterns** - Add common noun-verb pairings

### MEDIUM PRIORITY
1. **Register labels** - Mark casual/neutral/formal for all entries
2. **Similar words** - Add contrastive sections for semantic neighbors
3. **Adjective forms** - Add adverbial (〜く/〜に) and noun forms (〜さ)
4. **Example progression** - Ensure simple → complex ordering

### LOW PRIORITY
1. **Kanji orthography notes** - When to use kanji vs. hiragana
2. **Cultural notes** - Expand where significant
3. **Keigo references** - Link to honorific forms

## Claude Code Skills

Available in `.claude/skills/` (automatically loaded when relevant):

| Skill | Use When |
|-------|----------|
| `entry-guidelines` | Creating any entry |
| `verb-entry` | Creating/revising verb entries |
| `adjective-entry` | Creating/revising adjective entries |
| `particle-entry` | Creating/revising particle entries |
| `other-entries` | Creating nouns, counters, adverbs, expressions |
| `revise-entries` | Revising existing entries to v2 standards |
| `vocabulary-notes` | Formatting notes field content |
| `cross-reference-entry` | Adding cross-references between entries |

## Recent Changes

### 2026-01-10 (Cross-Reference Linking System)
- Implemented structured cross-reference schema (type, reading, headword, label)
- Added link resolution in build pipeline (`build/resolve_links.py`)
- Added "Related Words" section to entry display in web interface
- Created extraction script (`build/extract_references.py`) to populate from notes
- Added validation for cross-reference format
- Created `cross-reference-entry` skill for systematic additions
- Reference types: pair, synonym, antonym, keigo, related, see_also, contrast
- Supports pending links (references to entries not yet created)

### 2026-01-09 (N3 Vocabulary Expansion)
- Added 50 new N3 vocabulary entries from candidate_words.json
- New entries include: na-adjectives (完全, 様々, 正直, 真剣, 深刻, 地味, 重要, 清潔, 積極的, 適切, 奇妙, 公平), nouns (完成, 区別, 現在, 種類, 事件, 状況, 人類, 専攻, 当時, 昼食, 残り, 維持, 一種, 差別, 財産, 使用, 性質, 重大), adverbs (じっと, 既に, 相当, 当然, 常に, 非常, ますます, 主に, 大いに, さて, ただ, 多少, のんびり), verbs (まとまる, 見かける), and other types
- Updated entries_index.json (1,880 entries total)
- Removed 49 added words from candidate_words.json (2,117 remaining)

### 2026-01-08 (Entry Tracking System)
- Created `entries_index.json` listing all 1,153 entries with key metadata
- Created `candidate_words.json` with 1,992 candidate words for future addition
- Added build scripts: `update_entries_index.py`, `manage_candidates.py`, `update_indexes.py`
- Removed N3_VOCABULARY_TO_ADD.md and N4_VOCABULARY_TO_ADD.md (data now in candidate_words.json)

### 2026-01-08 (N4 Vocabulary Expansion)
- Added 183 new N4 vocabulary entries (nouns, katakana loanwords, adverbs, counters, suffixes)
- Total entries now 1,153
- Removed 34 duplicate entries from N3 vocabulary list

### 2026-01-09 (Interface Refinements)
- Removed Compare mode
- Added Recent mode showing most recently added/revised entries (250 entries)
- Added Random mode with word cloud display
- Fixed Browse mode display on narrow screens

### 2026-01-08 (Web Interface Update)
- Added multiple interface modes: Search, Browse
- Sticky header with interface toggle and furigana button
- Browse mode with filters for JLPT level, part of speech, starting kana

### Previous Sessions
- Added 62 N4 vocabulary entries (adverbs, keigo verbs, nouns, katakana loanwords)
- Removed "New" tag functionality from dictionary
- Added vocabulary-notes skill for formatting guidelines
- Updated web interface to handle paragraph breaks and bullet points in notes
- Reformatted 154 entries with proper bullet point formatting

## Next Steps

### Immediate (Cross-Reference Migration)
1. Run extraction script to populate cross-references from existing notes
2. Review and apply extracted references in batches
3. Manually add cross-references for high-priority entries (N5 verbs)

### Ongoing (Vocabulary Expansion)
1. Continue adding vocabulary from `candidate_words.json` (see workflow below)
2. Maintain v2 quality standards for all new entries
3. Add cross-references when creating new entries

### Future Enhancements
1. Add conjugation search
2. Add audio pronunciation
3. Export to Anki format

## Workflow: Adding Entries from Candidates

Follow this step-by-step process when adding new dictionary entries from `candidate_words.json`:

### Step 1: Select Candidates
1. Review `candidate_words.json` to choose words to add
2. Prioritize by JLPT level (N5 → N4 → N3) or thematic groups
3. Check that the candidate hasn't already been added to the dictionary

### Step 2: Create Entry Files
1. Create the JSON entry file following the schema (`build/schema.json`)
2. Use the appropriate Claude skill based on entry type:
   - Verbs: `verb-entry` skill
   - Adjectives: `adjective-entry` skill
   - Particles: `particle-entry` skill
   - Others: `other-entries` skill
3. Follow `vocabulary-notes` skill for notes formatting
4. Place file in correct directory based on reading's first kana:
   - あ行 → `entries/a/`, か行 → `entries/ka/`, etc.
5. File naming: `{romaji}_{5-digit-id}.json`

### Step 3: Validate Entry
```bash
python3 build/validate.py --id {entry_id}
# Or validate all:
python3 build/validate.py
```

### Step 4: Update Indexes
**IMPORTANT: Run this after adding ANY entries:**
```bash
python3 build/update_indexes.py
```
This will:
- Update `entries_index.json` with the new entry
- Remove added words from `candidate_words.json` (sync)

### Step 5: Build and Test
```bash
python3 build/build.py
# Then open docs/index.html to verify
```

### Step 6: Add Cross-References
1. Use the `cross-reference-entry` skill for guidelines
2. Add structured references for:
   - Transitivity pairs (for verbs)
   - Keigo equivalents
   - Antonyms/opposites
   - Related vocabulary mentioned in notes
3. References can point to entries that don't exist yet

### Step 7: Commit Changes
Commit the new entry files, updated indexes, and rebuilt docs/

## Workflow: Adding Cross-References to Existing Entries

### Automated Extraction
```bash
# See proposed changes
python3 build/extract_references.py

# Apply changes
python3 build/extract_references.py --apply

# Then rebuild
python3 build/build.py
```

### Cross-Reference Format
```json
"cross_references": [
  {
    "type": "pair",
    "reading": "しまる",
    "headword": "{閉|し}まる",
    "label": "intransitive"
  }
]
```

### Reference Types
| Type | Use For | Example |
|------|---------|---------|
| `pair` | Transitivity pairs | 閉める → 閉まる |
| `antonym` | Opposites | 大きい → 小さい |
| `keigo` | Honorific/humble | 食べる → 召し上がる |
| `synonym` | Similar meaning | 分かる → 理解する |
| `contrast` | Easily confused | は → が |
| `related` | Semantically connected | 食べる → 食べ物 |
| `see_also` | General reference | - |

## Technical Notes

### Build Commands
```bash
# Validate entries
python3 build/validate.py

# Build dictionary
python3 build/build.py

# Update index files (after adding/removing entries)
python3 build/update_indexes.py

# Manage candidate words
python3 build/manage_candidates.py stats    # Show statistics
python3 build/manage_candidates.py add "漢字" "かんじ" "notes"  # Add candidate

# Cross-reference extraction
python3 build/extract_references.py          # Dry run - show proposed changes
python3 build/extract_references.py --apply  # Apply changes to entry files
python3 build/extract_references.py --id taberu_00001  # Single entry

# View locally
open docs/index.html
```

### File Naming Convention
- Format: `{romanized_reading}_{5-digit-id}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
- Directory: Based on first kana of reading
- Katakana loanwords: Use hiragana reading (e.g., アルバイト → あるばいと)

### Entry and Candidate Tracking
- **entries_index.json**: Auto-generated index of all dictionary entries
- **candidate_words.json**: Words to potentially add (each has unique ID like C00001)
- Run `python build/update_indexes.py` after modifying entries to keep indexes in sync

## Notes for AI Assistants

### Before Starting Work
1. Read this file to understand current state
2. Check `project_specification_v2.md` for detailed quality standards
3. Relevant skills will be auto-loaded based on task type

### Entry Requirements
- All kanji must have furigana: `{漢字|かんじ}`
- 2-3 example sentences minimum
- Examples progress from simple to complex
- Include at least one collocation or fixed phrase
- Katakana loanwords use hiragana in reading field

### Quality Standards
See `project_specification_v2.md` for comprehensive guidelines. Key points:
- **Verbs**: Transitivity type, pair verb, aspect/ている behavior, collocations
- **Particles**: Predicates requiring particle, contrast with similar particles
- **Adjectives**: Forms (adverbial, noun), similar word distinctions
- **All entries**: Consistent depth with similar entries

### After Each Session
Update this file with:
- Entries added/revised
- Any issues encountered
- Next steps
