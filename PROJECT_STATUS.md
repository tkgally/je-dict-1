# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-08
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
- [x] Multiple interface modes (Search, Browse, Compare)
- [x] Sticky header with interface toggle
- [x] Last updated date in footer

### Content Status
- **Total entries**: 1004
- **JLPT N5 coverage**: ~95% complete
- **JLPT N4 coverage**: 243 entries added (~37% of target)
- **N4 vocabulary remaining**: 406 items (see N4_VOCABULARY_TO_ADD.md)

### Entry Breakdown by JLPT Level
| Level | Count | Status |
|-------|-------|--------|
| N5 | ~761 | Complete |
| N4 | 243 | In progress |

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

## Recent Changes

### 2026-01-08 (Web Interface Update)
- Added three interface modes: Search, Browse, Compare
- Sticky header with interface toggle and furigana button
- Browse mode with filters for JLPT level, part of speech, starting kana
- Compare mode for side-by-side word comparisons (particles, transitive pairs, similar words)
- Added last revision date in footer
- Removed "je-dict-1" branding from visible UI

### 2026-01-08 (N4 Entries)
- Added 62 N4 vocabulary entries (adverbs, keigo verbs, nouns, katakana loanwords)
- Total entries now 1004
- Updated N4_VOCABULARY_TO_ADD.md (406 items remaining)
- Removed 3 duplicate entries

### Previous Sessions
- Removed "New" tag functionality from dictionary
- Added vocabulary-notes skill for formatting guidelines
- Updated web interface to handle paragraph breaks and bullet points in notes
- Reformatted 154 entries with proper bullet point formatting
- Fixed furigana display in example sentence notes

## Next Steps

### Immediate (N4 Expansion)
1. Continue adding N4 vocabulary from N4_VOCABULARY_TO_ADD.md
2. Priority: nouns (378 remaining), then other categories
3. Maintain v2 quality standards for all new entries

### After N4 Complete
1. Implement cross-entry linking
2. Add conjugation search
3. Begin N3 vocabulary research

## Technical Notes

### Build Commands
```bash
# Validate entries
python3 build/validate.py

# Build dictionary
python3 build/build.py

# View locally
open docs/index.html
```

### File Naming Convention
- Format: `{romanized_reading}_{5-digit-id}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
- Directory: Based on first kana of reading
- Katakana loanwords: Use hiragana reading (e.g., アルバイト → あるばいと)

### ID Assignment
Next available IDs by directory:
- `/a/`: 00157+
- `/ka/`: 00167+
- `/sa/`: 00178+
- `/ta/`: 00180+
- `/na/`: 00142+
- `/ha/`: 00187+
- `/ma/`: 00147+
- `/ya/`: 00137+
- `/ra/`: 00188+
- `/wa/`: 00100+

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
