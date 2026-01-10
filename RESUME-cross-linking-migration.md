# Cross-Linking Migration - Resume Instructions

**Last updated**: 2026-01-10 (Session 2)
**Current phase**: Phase 3 - Ongoing Maintenance

## Session 1 Summary (2026-01-10)

### Completed Tasks

1. **Schema Enhancement** (`build/schema.json`)
   - Added structured cross_references format with type, reading, headword, label
   - Supports both legacy string format and new structured format (backward compatible)

2. **Build Pipeline**
   - Created `build/resolve_links.py` for link resolution at build time
   - Modified `build/build.py` to integrate link resolution (step 3/6)
   - Links are resolved by reading → entry lookup
   - Pending links (target doesn't exist) are tracked separately

3. **Validation** (`build/validate.py`)
   - Added `validate_structured_cross_reference()` function
   - Validates type, reading (hiragana), prevents self-references
   - Handles both legacy and new formats

4. **Web Interface**
   - Added `renderCrossReferences()` to `web/app.js`
   - Added "Related Words" section with clickable links
   - Pending links shown in gray with "(not yet in dictionary)" label
   - Added CSS styling in `web/styles.css`

5. **Extraction Script** (`build/extract_references.py`)
   - Parses notes field to extract pair verbs, antonyms, keigo, see_also
   - Handles compound furigana words correctly
   - Dry run mode shows proposed changes
   - --apply flag to update entry files

6. **Claude Skill** (`.claude/skills/cross-reference-entry/`)
   - Guidelines for adding and maintaining cross-references
   - Reference type documentation
   - Priority order for different reference types

### Current State

- **Infrastructure**: Complete and tested
- **Existing cross-references**: 302 resolved (from legacy format)
- **Extractable from notes**: 159 new references (143 entries)
- **Total entries**: 2,024

### Files Modified/Created

| File | Status |
|------|--------|
| `build/schema.json` | Modified |
| `build/resolve_links.py` | Created |
| `build/build.py` | Modified |
| `build/validate.py` | Modified |
| `build/extract_references.py` | Created |
| `web/app.js` | Modified |
| `web/styles.css` | Modified |
| `.claude/skills/cross-reference-entry/SKILL.md` | Created |
| `PROJECT_STATUS.md` | Modified |

---

## Session 2 Summary (2026-01-10)

### Completed Tasks

1. **Applied Automated Extraction**
   - Ran `python3 build/extract_references.py --apply`
   - 143 entries updated with 159 new cross-references
   - Fixed 4 entries with `label: null` validation errors
   - Fixed extraction script to exclude null labels

2. **Verified Extraction Quality**
   - Spot-checked shimeru, taberu, akeru entries
   - All cross-references correctly extracted
   - Pair verbs and antonyms properly identified

3. **Rebuilt Dictionary**
   - All 2,024 entries validated
   - 461 total cross-references (up from 302)
   - 445 resolved (96%)
   - 16 pending links (targets not yet in dictionary)

### Current State

- **Total cross-references**: 461
- **Resolved**: 445 (96%)
- **Pending**: 16 unique targets
- **Infrastructure**: Complete and stable

### Files Modified

| File | Changes |
|------|---------|
| `build/extract_references.py` | Fixed null label handling |
| 143 entry files | Added extracted cross-references |

---

## Session 3 Tasks (Next Session)

### Priority 1: Manual Enhancement for High-Priority Entries

After automated extraction, manually add cross-references to:

1. **N5 Verbs with transitivity pairs** (highest priority)
   - Check all verb entries for pair verb references
   - Use the `cross-reference-entry` skill for guidelines

2. **Keigo triplets** (plain → honorific/humble)
   - 食べる, 飲む, 行く, 来る, いる, 見る, 言う, する, etc.

3. **Particle contrasts**
   - は ↔ が, に ↔ で, に ↔ へ

### Priority 2: Test UI Navigation

1. Open `docs/index.html` in browser
2. Search for "閉める" (shimeru)
3. Verify "Related Words" section appears
4. Click on cross-reference links
5. Verify navigation works correctly
6. Check pending links display correctly

---

## Ongoing Maintenance & Future Enhancements

### Ongoing Maintenance

When adding new entries:
1. Include cross-references at creation time
2. Use `cross-reference-entry` skill for guidelines
3. Run extraction script periodically to catch any missed references

### Enhancement Ideas

1. **Bidirectional Links**: Automatically add reverse references
   - If A → B, also add B → A
   - Script to detect and add missing reverse links

2. **Link Statistics**: Add reporting
   - Entries with no cross-references
   - Most-referenced entries
   - Pending link targets (vocabulary to prioritize adding)

3. **UI Improvements**
   - Show reference count in search results
   - Filter by entries with/without cross-references
   - Group references by type in display

4. **Extraction Improvements**
   - Detect more patterns (e.g., "Similar to:", "Compare with:")
   - Extract related words from COMMON PATTERNS sections
   - Detect compound word relationships

---

## Quick Reference

### Cross-Reference Types

| Type | Use For | Label |
|------|---------|-------|
| `pair` | Verb transitivity pairs | "intransitive"/"transitive" |
| `antonym` | Direct opposites | Brief gloss |
| `keigo` | Honorific/humble forms | "honorific"/"humble" |
| `synonym` | Similar meaning | Distinguishing trait |
| `contrast` | Easily confused | Usage context |
| `related` | Semantic connection | Relationship |
| `see_also` | General reference | null |

### Commands

```bash
# Extraction
python3 build/extract_references.py          # Dry run
python3 build/extract_references.py --apply  # Apply
python3 build/extract_references.py --id X   # Single entry

# Build & Validate
python3 build/build.py
python3 build/validate.py

# Check a specific entry
python3 build/validate.py --id shimeru_00005
```

### Schema Format

```json
{
  "cross_references": [
    {
      "type": "pair",
      "reading": "しまる",
      "headword": "{閉|し}まる",
      "label": "intransitive"
    }
  ]
}
```

---

## Notes for AI Assistants

1. The cross-reference system is fully operational
2. Extraction script handles compound furigana correctly
3. Both legacy (string) and new (object) formats are supported
4. Links to non-existent entries are allowed (shown as pending)
5. The `cross-reference-entry` skill provides detailed guidelines
6. Always rebuild (`python3 build/build.py`) after modifications
