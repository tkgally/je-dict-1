# Cross-Reference Links Plan

## Overview

This document describes the plan for adding inline cross-reference links from example sentences and notes to dictionary entries. Every Japanese word appearing in an entry can link to its main entry (if one exists), enabling users to click through to related vocabulary.

## Symbol Selection

After analyzing conflicts with JSON, HTML, Python, and the existing furigana format `{kanji|reading}`, the following Unicode characters are selected:

### Delimiters

| Symbol | Unicode | Name | Purpose |
|--------|---------|------|---------|
| `⟦` | U+27E6 | Mathematical left white square bracket | Word boundary open |
| `⟧` | U+27E7 | Mathematical right white square bracket | Word boundary close |
| `→` | U+2192 | Rightwards arrow | Separator between surface form and link info |
| `：` | U+FF1A | Fullwidth colon | Separator between base form and entry ID |

### Why These Symbols?

1. **⟦ ⟧** - Mathematical white square brackets are:
   - Not used in Japanese prose
   - Not used in JSON syntax
   - Not used in HTML
   - Visually distinct from regular brackets `[ ]` and Japanese brackets `【 】`
   - Easy to search for in code

2. **→** - The rightwards arrow is:
   - Visually intuitive (pointing to the target)
   - Rare in Japanese prose (usually「→」is used for directions)
   - Not a JSON or HTML special character

3. **：** - The fullwidth colon is:
   - Distinct from ASCII colon `:` used in JSON
   - Used naturally in Japanese contexts
   - Clear visual separator

## Format Specification

### Basic Format

```
⟦surface_form→baseform：entry_id⟧
```

Where:
- `surface_form` - The text as it appears in the sentence (may include furigana notation)
- `baseform` - The dictionary headword form (kanji only, no furigana)
- `entry_id` - The target entry ID (e.g., `01292_kare`) or `noentry`

### Examples

**Original sentence:**
```
{彼|かれ}のために{尽|つ}くした。
```

**With cross-reference links:**
```
⟦{彼|かれ}→彼：01292_kare⟧⟦の→の：00073_no⟧⟦ため→ため：01145_tame⟧⟦に→に：00314_ni⟧⟦{尽|つ}くした→尽くす：02077_tsukusu⟧。
```

### Special Cases

#### 1. Word not in dictionary
```
⟦{矍鑠|かくしゃく}→矍鑠：noentry⟧
```

#### 2. Compound expressions that are one entry
```
⟦{食|た}べ{物|もの}→食べ物：00450_tabemono⟧
```

#### 3. Conjugated forms
```
⟦{食|た}べました→食べる：00396_taberu⟧
⟦{走|はし}っている→走る：00234_hashiru⟧
⟦{美|うつく}しかった→美しい：00567_utsukushii⟧
```

#### 4. Particles with same form as headword
```
⟦が→が：00051_ga⟧
⟦を→を：00056_wo⟧
```

#### 5. Multiple readings/homographs (same written form, different entries)
The baseform disambiguates:
```
⟦{上|あ}げる→上げる：01234_ageru⟧  (to raise)
⟦{上|あ}げる→揚げる：01235_ageru⟧  (to fry)
```

### What NOT to Link

1. **Punctuation** - 。、？！ etc. should remain outside brackets
2. **Numbers** - Unless they're vocabulary entries (e.g., 一、二)
3. **Foreign words in katakana** - Link only if the word has an entry
4. **The headword itself** - In an entry's own examples, the headword being demonstrated should typically not be linked to itself (optional)

## Processing Pipeline

### Parse Order

1. Find all `⟦...⟧` blocks
2. For each block, split by `→` to separate surface form and link info
3. Split link info by `：` to get baseform and entry_id
4. Process furigana `{kanji|reading}` within surface form
5. Generate HTML with or without link wrapper

### Regex Patterns

```python
# Link block pattern
LINK_BLOCK_PATTERN = re.compile(r'⟦([^⟧]+)⟧')

# Link info pattern (applied to content inside ⟦...⟧)
LINK_INFO_PATTERN = re.compile(r'^(.+?)→(.+?)：(.+)$')
```

### HTML Output

**When links are enabled (toggle ON):**
```html
<a class="word-link" href="../01292_kare.html" data-baseform="彼">
  <ruby>彼<rp>(</rp><rt>かれ</rt><rp>)</rp></ruby>
</a>
```

**When links are disabled (toggle OFF) or entry doesn't exist:**
```html
<ruby>彼<rp>(</rp><rt>かれ</rt><rp>)</rp></ruby>
```

## CSS Styling

```css
/* Base word-link style - invisible by default */
.word-link {
  text-decoration: none;
  color: inherit;
}

/* When links toggle is OFF (default state) */
body:not(.show-word-links) .word-link {
  pointer-events: none;
  cursor: text;
}

/* When links toggle is ON */
body.show-word-links .word-link {
  text-decoration: underline dotted;
  text-decoration-color: rgba(0, 102, 204, 0.4);
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
  cursor: pointer;
}

body.show-word-links .word-link:hover {
  text-decoration-color: rgba(0, 102, 204, 0.8);
}

/* Tooltip on hover showing baseform */
body.show-word-links .word-link[data-baseform]:hover::after {
  content: attr(data-baseform);
  position: absolute;
  /* tooltip styling... */
}
```

## JavaScript Toggle

Add a third toggle button alongside existing Furigana and Examples toggles:

```javascript
(function() {
    var btn = document.getElementById('wordlinks-toggle');
    if (!btn) return;

    var hidden = localStorage.getItem('wordLinksHidden') !== 'false'; // Default OFF

    function updateState() {
        document.body.classList.toggle('show-word-links', !hidden);
        btn.setAttribute('aria-pressed', !hidden);
        btn.classList.toggle('active', !hidden);
    }

    updateState();

    btn.addEventListener('click', function() {
        hidden = !hidden;
        localStorage.setItem('wordLinksHidden', hidden);
        updateState();
    });
})();
```

## Implementation Phases

### Phase 1: Test Branch (Current)
- Create test branch with ~100 entries
- Implement JSON format in selected entries
- Update build scripts to parse new format
- Add CSS and JavaScript for toggle
- Verify HTML output quality
- Iterate on format if needed

### Phase 2: Polish Prompt
- Create prompt template for adding links entry-by-entry
- Similar structure to `polish_example_sentences.md`
- Progress tracking via `polishing/tasks/cross-references/progress.txt`

### Phase 3: Gradual Rollout
- Process entries batch by batch
- Prioritize basic/core vocabulary first
- Track completion percentage

### Phase 4: Maintenance
- New entries get links added during creation
- Update links when entries are renamed or deleted

## Entry Selection for Testing

For the test branch, select entries that cover:

1. **Various parts of speech** - verbs, nouns, adjectives, particles
2. **Conjugated forms** - te-form, past tense, negative, etc.
3. **Compound words** - to test linking behavior
4. **Entries with rich examples** - 5+ examples to test thoroughly
5. **Entries with notes containing Japanese** - to test notes linking
6. **Cross-references** - entries that reference each other

Suggested test entries (100 entries):
- Basic tier: 30 entries
- Core tier: 50 entries
- General tier: 20 entries

## Validation

Add validation checks for:

1. **Balanced brackets** - Every `⟦` has matching `⟧`
2. **Valid format** - Content matches `surface→base：id` pattern
3. **Entry existence** - Warn if entry_id doesn't exist (unless `noentry`)
4. **Consistent baseform** - The baseform should match target entry's headword

## Backward Compatibility

- Entries without link markup continue to work normally
- Links can be added incrementally
- Build script processes both linked and unlinked text

## File Changes Summary

| File | Changes |
|------|---------|
| `build/html_utils.py` | Add `process_word_links()` function |
| `build/build_flat.py` | Integrate link processing, add toggle button |
| `build/validate.py` | Add link format validation |
| `build/constants.py` | Add link-related constants |
| `prompts/add_cross_reference_links.md` | New prompt for gradual linking |
| CSS (inline in build) | Add `.word-link` styles |
| JS (inline in build) | Add toggle script |

## Questions to Resolve During Testing

1. Should the headword in its own examples be linked (to itself)?
2. How to handle words that could link to multiple entries (homographs)?
3. Should particles always be linked, or only in particle-focused entries?
4. What's the best tooltip behavior for the baseform display?
5. Should `noentry` words be visually distinguishable (to identify gaps)?
