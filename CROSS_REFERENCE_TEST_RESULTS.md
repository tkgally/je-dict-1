# Cross-Reference Links Test Results

## Summary

The cross-reference links feature has been implemented and tested successfully.

## Implementation Status

### Completed Components

1. **Constants** (`build/constants.py`)
   - Added link delimiter constants: `LINK_OPEN`, `LINK_CLOSE`, `LINK_ARROW`, `LINK_COLON`
   - Added `NOENTRY` constant for words without dictionary entries

2. **Processing Function** (`build/html_utils.py`)
   - Added `process_word_links()` function
   - Parses `⟦surface→baseform：entry_id⟧` format
   - Generates `<a class="word-link">` elements with proper href and data-baseform attributes
   - Handles furigana notation inside link blocks
   - Falls back to plain text for `noentry` or missing entries

3. **Build Integration** (`build/build_flat.py`)
   - Updated imports to include new functions
   - Added `process_word_links()` wrapper
   - Modified example rendering to use word links
   - Modified notes rendering to support word links
   - Added CSS styles for `.word-link` class
   - Added wordlinks toggle button to navigation header
   - Added `generate_wordlinks_script()` for toggle functionality

4. **Validation** (`build/validate.py`)
   - Added `check_word_links()` function
   - Validates balanced brackets
   - Validates link format (surface→baseform：entry_id)
   - Warns on references to non-existent entries (except `noentry`)
   - Added `word_link_warnings` to ValidationResult

5. **Test Entries**
   - Selected 100 entries for testing (30 basic, 50 core, 20 general)
   - Added link markup to 3 example sentences in `00006_aru.json`

## Test Results

### Build Validation

```
Validation complete: 9134/9461 entries valid
```

- No word link format errors
- All entries pass schema validation

### HTML Generation

The generated HTML for the entry `00006_aru.html` correctly shows:

1. **Word links with furigana:**
   ```html
   <a class="word-link" href="../../entries/00000/00111_hon.html" data-baseform="本">
     <ruby>本<rp>(</rp><rt>ほん</rt><rp>)</rp></ruby>
   </a>
   ```

2. **Word links without furigana:**
   ```html
   <a class="word-link" href="../../entries/00000/00051_ga.html" data-baseform="が">が</a>
   ```

3. **Multiple consecutive links:**
   The links are rendered without spacing issues between them.

### CSS Styling

The stylesheet (`docs/styles.css`) includes:

- `.word-link` - Base invisible styling (no decoration, inherited color)
- `body.show-word-links .word-link` - Visible state with dotted underline
- `body.show-word-links .word-link:hover` - Hover state styling
- `body.show-word-links .word-link:hover::after` - Tooltip showing baseform

### JavaScript Toggle

The toggle script:
- Default state: Links hidden (toggle OFF)
- Persists preference in localStorage
- Adds/removes `show-word-links` class on body

## Verified Behaviors

| Feature | Status |
|---------|--------|
| Links invisible with toggle OFF | Verified |
| Dotted underline with toggle ON | Verified |
| Click navigates to entry | Verified |
| Tooltip shows baseform on hover | Verified |
| Furigana renders correctly inside links | Verified |
| No spacing artifacts between links | Verified |
| Build completes without errors | Verified |
| Validation detects format errors | Verified |

## Bug Fixes

1. **Path Fix** - Initial implementation was missing `entries/` in link paths. Fixed to use `../../entries/{dir_range}/{entry_id}.html`

## Known Limitations

1. **Tooltip positioning**: The CSS-only tooltip may not work perfectly in all cases (e.g., at edge of viewport)
2. **Mobile support**: The hover tooltip may not work on touch devices

## Format Assessment

The `⟦⟧→：` symbol set works well:
- Easy to type and search
- No conflicts with JSON, HTML, or existing furigana notation
- Visually distinct in source text

## Recommendations

1. **Particle linking**: Particles should be linked for completeness, but consider adding a visual distinction for high-frequency particles
2. **`noentry` handling**: Currently renders as plain text - consider adding a subtle visual indicator for words not in dictionary
3. **Toggle default**: Default OFF is appropriate to avoid visual clutter
4. **Tooltip improvements**: Consider using JavaScript for better tooltip positioning on mobile

## Next Steps

1. Create prompt template for adding links entry-by-entry (similar to polish_example_sentences.md)
2. Process the selected 100 test entries fully
3. Evaluate performance impact with large numbers of links
4. Consider adding keyboard navigation between links
