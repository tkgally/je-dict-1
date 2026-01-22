# Kanji Index Implementation - Step 1: Create Directory Structure

## Overview

This is the first step in implementing the kanji index feature for the dictionary. The kanji index allows users to click on any kanji in a headword to find all other entries containing that same kanji.

## Task

Create the directory structure for the kanji index feature:

### 1. Create the `kanji/` directory (data storage)

Create the directory at the project root:
```
kanji/
```

This directory will contain:
- `kanji_list.json` - Master list mapping kanji characters to their kanji index IDs
- Individual JSON files for each kanji (e.g., `00001_kou_taka_tall.json`)

### 2. Create the `docs/kanji/` directory (built HTML)

Create the directory:
```
docs/kanji/
```

This directory will hold the built HTML pages for each kanji index page.

### 3. Create placeholder files

Create an empty `kanji_list.json` with this structure:
```json
{
  "metadata": {
    "description": "Index mapping kanji characters to their kanji index IDs",
    "generated": null,
    "total_kanji": 0
  },
  "kanji": {}
}
```

The `kanji` object will eventually contain entries like:
```json
{
  "高": {
    "kanji_id": "00001_kou_taka_tall",
    "onyomi": "kou",
    "kunyomi": "taka",
    "gloss": "tall"
  }
}
```

## Kanji Index ID Format

Each kanji receives a unique identifier in this format:
```
{5-digit-number}_{onyomi}_{kunyomi}_{gloss}
```

Examples:
- `00001_kou_taka_tall` for 高
- `00002_dai_oo_big` for 大
- `00003_shoku_ta_eat` for 食

Notes:
- The 5-digit number is sequential (00001, 00002, etc.)
- `onyomi` is the most common on'yomi reading in romaji (lowercase)
- `kunyomi` is the most common kun'yomi reading in romaji (lowercase, without okurigana)
- `gloss` is a single English word summarizing a primary meaning
- If a kanji has no on'yomi, use `none` (e.g., `00100_none_hatake_field` for 畑)
- If a kanji has no kun'yomi, use `none` (e.g., `00050_cha_none_tea` for 茶)

## Verification

After completing this step:
1. Verify `kanji/` directory exists
2. Verify `docs/kanji/` directory exists
3. Verify `kanji/kanji_list.json` exists with proper initial structure

## Next Step

Proceed to `02_extract_kanji.md` to create the script that extracts all kanji from entry headwords.
