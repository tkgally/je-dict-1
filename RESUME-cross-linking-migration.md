# Cross-Linking Migration - Resume Instructions

**Last updated**: 2026-01-11 (Session 4)
**Current phase**: Phase 4 - Infrastructure Updated

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

## Session 3 Summary (2026-01-10)

### Completed Tasks

1. **Keigo Cross-References**
   - Added structured cross-references to 8 keigo-related entries:
     - 召し上がる (meshiagaru) → 食べる, 飲む, いただく
     - いただく (itadaku) → もらう, 食べる, 飲む, 召し上がる, くださる
     - いらっしゃる (irassharu) → いる, 来る, 行く, おる, 参る
     - おっしゃる (ossharu) → 言う, 申す, 申し上げる
     - 参る (mairu) → 行く, 来る, いらっしゃる
     - 申す (mousu) → 言う, おっしゃる
     - くださる (kudasaru) → くれる, いただく
     - 食べる (taberu) → 召し上がる, いただく (added honorific/humble refs)

2. **Particle Contrast Cross-References**
   - Updated 4 particle entries from legacy string format to structured:
     - は (ha_00001) → が (contrast)
     - が (ga_00001) → は (contrast)
     - に (ni_00001) → で, へ (contrast)
     - で (de_00008) → に (contrast)

3. **Rebuilt Dictionary**
   - All 2,024 entries validated
   - 469 total cross-references (up from 461)
   - 486 total references, 469 resolved (96%)
   - 17 pending links (targets not yet in dictionary)

### Current State

- **Total cross-references**: 486
- **Resolved**: 469 (96%)
- **Pending**: 17 unique targets
- **Infrastructure**: Complete and stable

### Files Modified

| File | Changes |
|------|---------|
| `entries/ma/me/meshiagaru_00142.json` | Added keigo cross-references |
| `entries/a/it/itadaku_00148.json` | Added keigo cross-references |
| `entries/a/ir/irassharu_00137.json` | Added keigo cross-references |
| `entries/a/os/ossharu_00138.json` | Added keigo cross-references |
| `entries/ma/ma/mairu_00146.json` | Added keigo cross-references |
| `entries/ma/mo/mousu_00145.json` | Added keigo cross-references |
| `entries/ka/ku/kudasaru_00140.json` | Added keigo cross-references |
| `entries/ta/ta/taberu_00001.json` | Added keigo cross-references |
| `entries/ha/ha/ha_00001.json` | Converted to structured format |
| `entries/ka/ga/ga_00001.json` | Converted to structured format |
| `entries/na/ni/ni_00001.json` | Converted to structured format |
| `entries/ta/de/de_00008.json` | Converted to structured format |

**Note**: File paths above use the new prefix-based structure (`entries/{kana}/{prefix}/{id}.json`) introduced in Session 4.

---

## Session 4 Summary (2026-01-11)

### Infrastructure Changes

**IMPORTANT**: The project underwent major reorganization in this session:

1. **SPA Removed** - The single-page application version was removed. The dictionary is now built as flat HTML only.
   - `web/` directory no longer exists
   - `build/build.py` simplified to only run validation and `build_flat.py`
   - Output goes directly to `docs/` (not `docs/flat/`)

2. **Prefix-Based Subdirectories** - Entries and audio reorganized to avoid GitHub's 1,000 file/directory limit:
   - Entry paths changed from `entries/{kana}/{id}.json` to `entries/{kana}/{prefix}/{id}.json`
   - Audio paths changed from `audio/{kana}/{id}-exN.mp3` to `audio/{kana}/{prefix}/{id}-exN.mp3`
   - HTML output changed from `docs/flat/entries/{kana}/{id}.html` to `docs/entries/{kana}/{prefix}/{id}.html`
   - Prefix = first 2 characters of entry ID (e.g., `taberu_00001` → `ta/`)

3. **Files Modified/Created**:
   - `build/build.py` - Simplified (SPA code removed)
   - `build/build_flat.py` - Updated for new paths
   - `build/validate.py` - Added prefix directory validation
   - `build/migrate_entries.py` - New script for migration
   - All 2,074 entry files migrated to new locations

### Impact on Cross-References

- Cross-reference resolution still works (by reading lookup)
- Web display still works (links updated in build_flat.py)
- No changes to cross-reference format or validation

---

## Session 5 Tasks (Next Session)

### Priority 1: Additional Manual Enhancements

1. **N5 Verbs with transitivity pairs** (highest priority)
   - Check all verb entries for pair verb references
   - Use the `cross-reference-entry` skill for guidelines

2. **Additional keigo triplets**
   - Check: 見る, する (if not already linked)
   - Verify bidirectional links are complete

3. **Additional particle contrasts**
   - を (direct object) - add if not done
   - へ (direction) - verify linked to に

### Note: UI Testing Completed

User tested the following entries for cross-reference display in Session 3:
- 食べる, 閉める, いらっしゃる, は, に, いただく, 開ける, 始める, くださる, が

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
7. **CRITICAL: Write each entry individually** - Do NOT create Python scripts to mass-produce entries. Each entry must be crafted by hand using the skills and guidelines. See `entry-guidelines` skill for details.
8. **Entry paths use prefix-based structure**: `entries/{kana}/{prefix}/{id}.json` where prefix is first 2 chars of entry ID
9. **SPA no longer exists** - The dictionary is now flat HTML only. The `web/` directory was removed.
