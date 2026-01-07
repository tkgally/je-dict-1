# je-dict-1 Project Status

**Last updated**: 2026-01-07
**Current phase**: Phase 3 - Entry Enhancement (Revision to v2 standards)

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 3: Entry Enhancement** - Revising existing entries to meet v2 quality standards before adding new entries.

### Infrastructure Status
- [x] Directory structure created
- [x] JSON schema defined (`build/schema.json`)
- [x] Validation script working (`build/validate.py`)
- [x] Build script working (`build/build.py`)
- [x] Web interface functional with search
- [x] Furigana system with toggle
- [x] Claude Code skills for entry guidelines
- [x] Quality specification v2 from multi-model evaluation

### Content Status
- **Total entries**: 764
- **JLPT N5 coverage**: ~95%
- **Entries needing v2 revision**: Most (see revision priorities below)

### Entry Breakdown by Type
| Type | Count | v2 Status |
|------|-------|-----------|
| Verbs | ~130 | Need transitivity, aspect, collocations |
| Nouns | ~330 | Need collocations |
| Adjectives | ~93 | Need forms, conjugations |
| Adverbs | ~45 | Need register, similar words |
| Particles | 9 | HIGH PRIORITY - Need predicate lists, contrasts |
| Counters | 20 | Need full counting patterns |
| Other | ~137 | Various enhancements |

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

## Next Steps

### Immediate (Entry Revision)
1. Revise all 9 particle entries (HIGH PRIORITY)
2. Add transitivity to all ~130 verb entries
3. Add aspect notes to verbs with non-obvious ている behavior
4. Add collocation patterns to high-frequency entries

### After Revision Complete
1. Resume N4 vocabulary expansion
2. Implement cross-entry linking
3. Add conjugation search

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

### ID Assignment
Next available IDs by directory:
- `/a/`: 00108+
- `/ka/`: 00111+
- `/sa/`: 00111+
- `/ta/`: 00107+
- `/na/`: 00104+
- `/ha/`: 00107+
- `/ma/`: 00104+
- `/ya/`: 00102+
- `/ra/`: 00101+
- `/wa/`: 00100+

## Notes for AI Assistants

### Before Starting Work
1. Read this file to understand current state
2. Check `project_specification_v2.md` for detailed quality standards
3. Invoke relevant skill (e.g., `/verb-entry`) before creating/revising entries

### Entry Requirements
- All kanji must have furigana: `{漢字|かんじ}`
- 2-3 example sentences minimum
- Examples progress from simple to complex
- Include at least one collocation or fixed phrase

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
