# Setup Cross-Reference Links Test Branch

This prompt sets up a test branch for implementing inline cross-reference links in dictionary entries.

## Background

We are adding a feature where Japanese words in example sentences and notes can link to their dictionary entries. This requires:

1. A new JSON format with link markup
2. Build script changes to parse and render the links
3. A toggle button to show/hide links in the UI
4. Testing with a subset of entries before full rollout

## Your Task

Create and set up a test branch for this feature:

### Step 1: Create the branch

```bash
git checkout -b cross-reference-links-test
```

### Step 2: Read the plan

Read the full implementation plan:
```
docs/CROSS_REFERENCE_PLAN.md
```

### Step 3: Implement build script changes

Modify the build scripts to:

1. **Add constants** in `build/constants.py`:
   ```python
   # Cross-reference link delimiters
   LINK_OPEN = '⟦'      # U+27E6
   LINK_CLOSE = '⟧'     # U+27E7
   LINK_ARROW = '→'     # U+2192
   LINK_COLON = '：'    # U+FF1A
   NOENTRY = 'noentry'
   ```

2. **Add processing function** in `build/html_utils.py`:
   - Create `process_word_links(text, entries_dict, relative_path)` function
   - Parse `⟦surface→baseform：entry_id⟧` format
   - Generate `<a class="word-link">` or plain text based on entry existence
   - Integrate with existing `process_furigana()` function

3. **Update `build/build_flat.py`**:
   - Call `process_word_links()` when processing examples and notes
   - Add word-links toggle button to nav header
   - Add CSS for `.word-link` class
   - Add JavaScript for toggle functionality

4. **Add validation** in `build/validate.py`:
   - Check for balanced link brackets
   - Validate link format
   - Warn on missing entry IDs (that aren't `noentry`)

### Step 4: Select test entries

Choose approximately 100 entries for testing. Include:

- **30 basic tier entries** with rich examples
- **50 core tier entries** across different parts of speech
- **20 general tier entries**

Make sure to include:
- Verbs (to test conjugation linking)
- Particles (to test single-character linking)
- Nouns with compound examples
- Entries that cross-reference each other

List the selected entries in:
```
docs/CROSS_REFERENCE_TEST_ENTRIES.md
```

### Step 5: Add links to test entries

For each selected entry, manually add link markup to:
- All example sentences
- Japanese text in notes (where appropriate)

**Format reminder:**
```
⟦{彼|かれ}→彼：01292_kare⟧⟦の→の：00073_no⟧⟦ため→ため：01145_tame⟧
```

**Guidelines:**
- Link every word that has a dictionary entry
- Use `noentry` for words not in the dictionary
- For conjugated forms, use the dictionary form as baseform
- Don't link punctuation
- The headword in its own examples doesn't need to link to itself

### Step 6: Test the build

```bash
python3 build/validate.py
python3 build/update_indexes.py
python3 build/build_flat.py
```

Open the generated HTML files in a browser and verify:
- Links toggle works correctly
- Links are invisible when toggle is off
- Subtle dotted underline appears when toggle is on
- Hovering shows the baseform
- Clicking navigates to the target entry
- No visual spacing artifacts between words

### Step 7: Commit and document

```bash
git add -A
git commit -m "Add cross-reference links feature (test branch)

- New link format: ⟦surface→baseform：entry_id⟧
- Build script processing for word links
- Toggle button for showing/hiding links
- CSS styling for subtle link display
- Test entries: ~100 entries with full linking"
```

### Step 8: Report findings

Document any issues or improvements needed in:
```
docs/CROSS_REFERENCE_TEST_RESULTS.md
```

Include:
- Screenshot descriptions of the UI
- Any parsing edge cases found
- Suggested format improvements
- Performance impact (if any)

## Key Files to Modify

| File | Purpose |
|------|---------|
| `build/constants.py` | Add link delimiter constants |
| `build/html_utils.py` | Add `process_word_links()` function |
| `build/build_flat.py` | Integrate link processing, add toggle |
| `build/validate.py` | Add link validation |

## Key Files to Create

| File | Purpose |
|------|---------|
| `docs/CROSS_REFERENCE_TEST_ENTRIES.md` | List of entries for testing |
| `docs/CROSS_REFERENCE_TEST_RESULTS.md` | Test findings and issues |

## Success Criteria

The test branch is successful when:

1. Build completes without errors
2. Links are completely invisible with toggle off
3. Links have subtle dotted underline with toggle on
4. Hovering shows baseform in tooltip
5. Clicking navigates to correct entry
6. No spacing or layout artifacts
7. All 100 test entries render correctly

## Questions to Answer During Testing

1. Is the `⟦⟧→：` symbol set optimal, or should we adjust?
2. Should particles always be linked?
3. How should `noentry` words be handled visually?
4. Is the toggle default (off) appropriate?
5. What tooltip style works best?
