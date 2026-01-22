# Kanji Index Implementation - Step 10: Initial Generation

## Overview

This is the one-time process to generate the complete kanji index from all existing dictionary entries. After this initial generation, the index is maintained incrementally.

## Prerequisites

All previous steps must be complete:
- [x] Directories created (`kanji/`, `docs/kanji/`)
- [x] `extract_kanji_from_entries.py` created
- [x] Kanji IDs assigned to all kanji in `kanji_list.json`
- [x] `build_kanji_json.py` created
- [x] `build_kanji_html.py` created
- [x] `build_flat.py` modified for kanji links
- [x] `update_kanji_index.py` created
- [x] `verify_kanji_index.py` created
- [x] Skill created

## Initial Generation Steps

### Step 1: Final Verification of kanji_list.json

Ensure all kanji have been assigned IDs:

```bash
python3 build/update_kanji_index.py --check-new
```

Expected output:
```
No new kanji found. All kanji have IDs assigned.
```

If new kanji are reported, go back to Step 3 and assign IDs.

### Step 2: Generate Kanji JSON Files

```bash
python3 build/build_kanji_json.py
```

Expected output:
```
Generated 1500 kanji JSON files in kanji/
```

Verify:
```bash
ls kanji/*.json | wc -l  # Should match kanji count + 2 (list and extracted)
```

### Step 3: Generate Kanji HTML Pages

```bash
python3 build/build_kanji_html.py
```

Expected output:
```
Generated 1500 kanji HTML pages in docs/kanji/
```

Verify:
```bash
ls docs/kanji/*.html | wc -l  # Should match kanji count
```

### Step 4: Rebuild Entry Pages with Kanji Links

```bash
python3 build/build_flat.py
```

This rebuilds all entry HTML pages with kanji links in headwords.

### Step 5: Run Full Verification

```bash
python3 build/verify_kanji_index.py
```

Expected output:
```
Verifying kanji index...
  Checking kanji_list.json...
  Checking kanji completeness...
  Checking kanji JSON files...
  Checking entry counts...
  Checking kanji HTML files...

Kanji index verified: 1500 kanji, no issues found.
```

### Step 6: Manual Testing

1. **Test entry page kanji links**:
   - Open `docs/entries/00000/00001_amaru.html` in browser
   - Hover over 余 in headword - should show "Other words with this kanji"
   - Click on 余 - should navigate to kanji index page

2. **Test kanji index page**:
   - Verify kanji displays correctly (large character)
   - Verify readings display (on'yomi in katakana, kun'yomi in hiragana)
   - Verify entry list is sorted by reading
   - Click an entry - should navigate to entry page

3. **Test several kanji**:
   - Common kanji (人, 日, 大)
   - Kanji with only on'yomi (茶)
   - Kanji with only kun'yomi (畑)
   - Rare kanji (one with few entries)

### Step 7: Add CSS to docs/styles.css

If not already done, add the kanji index CSS:

```css
/* Kanji Index Link Styles */
.kanji-link {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
}

.entry-headword .kanji-link:hover {
    background: rgba(0, 0, 0, 0.05);
    border-radius: 2px;
}

/* Kanji Index Page Styles */
.kanji-index-page {
    max-width: 900px;
    margin: 0 auto;
    padding: 1rem;
}

.kanji-header {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
}

.kanji-display-box {
    width: 120px;
    height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    border: 2px solid #dee2e6;
    border-radius: 8px;
    flex-shrink: 0;
}

.kanji-large {
    font-size: 72px;
    font-family: "Noto Sans JP", "Hiragino Kaku Gothic Pro", sans-serif;
    line-height: 1;
}

.kanji-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.kanji-readings {
    margin-bottom: 0.5rem;
}

.reading-row {
    margin-bottom: 0.25rem;
}

.reading-label {
    font-weight: bold;
    margin-right: 0.5rem;
}

.kanji-gloss {
    font-size: 1.25rem;
    color: #495057;
}

.kanji-entries-section h2 {
    margin-bottom: 1rem;
    font-size: 1.25rem;
}

.kanji-entry-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.kanji-entry-item {
    border-bottom: 1px solid #dee2e6;
}

.kanji-entry-item a {
    display: flex;
    gap: 1rem;
    padding: 0.75rem 0;
    text-decoration: none;
    color: inherit;
}

.kanji-entry-item a:hover {
    background: #f8f9fa;
}

.kanji-entry-item .entry-headword {
    font-weight: bold;
    min-width: 120px;
}

.kanji-entry-item .entry-reading {
    color: #6c757d;
    min-width: 100px;
}

.kanji-entry-item .entry-gloss {
    color: #495057;
    flex: 1;
}

/* Responsive adjustments */
@media (max-width: 600px) {
    .kanji-header {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .kanji-entry-item a {
        flex-wrap: wrap;
    }

    .kanji-entry-item .entry-gloss {
        width: 100%;
        margin-top: 0.25rem;
    }
}
```

### Step 8: Commit and Push

```bash
git add kanji/ docs/kanji/ build/
git add .claude/skills/kanji-index/
git add docs/styles.css
git commit -m "Add kanji index feature

- Create kanji directory structure
- Add scripts: extract_kanji_from_entries.py, build_kanji_json.py,
  build_kanji_html.py, update_kanji_index.py, verify_kanji_index.py
- Modify build_flat.py for kanji links in headwords
- Add kanji-index skill
- Generate initial kanji index for all entries"

git push
```

## Post-Implementation Maintenance

After initial generation, the kanji index is maintained automatically:

1. **New entries**: `update_kanji_index.py --check-new` detects new kanji
2. **Building**: `build_flat.py` regenerates kanji JSON and HTML
3. **Verification**: `verify_kanji_index.py` runs before builds

## Troubleshooting

### "X kanji need IDs assigned"

Return to Step 3 and assign IDs to the new kanji.

### Entry count mismatches

Run:
```bash
python3 build/verify_kanji_index.py --fix
```

### Missing HTML files

Run:
```bash
python3 build/build_kanji_html.py
```

### Links not appearing

Rebuild entry pages:
```bash
python3 build/build_flat.py
```

## Completion Checklist

- [ ] `kanji/kanji_list.json` contains all kanji with IDs
- [ ] `kanji/*.json` files exist for each kanji
- [ ] `docs/kanji/*.html` files exist for each kanji
- [ ] Entry headwords have kanji links (hover shows tooltip)
- [ ] Kanji index pages load correctly
- [ ] Entry links on kanji pages work
- [ ] `verify_kanji_index.py` passes
- [ ] CSS added for kanji pages
- [ ] Changes committed and pushed

## Summary

The kanji index is now complete! Users can:
1. Hover over any kanji in a headword to see the tooltip
2. Click to see all other entries with that kanji
3. Navigate from kanji page back to entries

The system automatically maintains itself as new entries are added.
