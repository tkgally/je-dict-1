# Kanji Index Implementation - Step 3: Assign Kanji Index IDs

## Overview

This step assigns the on'yomi, kun'yomi, and English gloss to each kanji extracted in Step 2. Since kanji readings cannot be determined programmatically, this step uses Claude's knowledge of Japanese.

## Prerequisites

- `kanji/kanji_extracted.json` must exist (created in Step 2)

## Task

Process `kanji/kanji_extracted.json` and assign readings/glosses to each kanji, then generate `kanji/kanji_list.json`.

### Process

1. **Read** `kanji/kanji_extracted.json`
2. **For each kanji**, determine:
   - **Most common on'yomi** in romaji (e.g., "kou" for 高, "jin/nin" for 人)
   - **Most common kun'yomi** in romaji without okurigana (e.g., "taka" for 高, "hito" for 人)
   - **Single-word English gloss** (e.g., "tall" for 高, "person" for 人)
3. **Assign sequential 5-digit IDs** starting from 00001
4. **Write** the complete `kanji/kanji_list.json`

### Batch Processing

Due to the number of kanji (likely 1000-2000), process in batches of 50-100 kanji per session:

**Session 1**: Process kanji 1-100
**Session 2**: Process kanji 101-200
...and so on

Each session should:
1. Read current progress from `kanji/kanji_list.json`
2. Process the next batch
3. Update `kanji/kanji_list.json` with new entries
4. Commit progress

### Kanji ID Format Rules

Format: `{5-digit}_{onyomi}_{kunyomi}_{gloss}`

**On'yomi rules:**
- Use most common reading in romaji lowercase
- Use `none` if kanji has no on'yomi (e.g., 畑 → "none")
- For multiple common readings, pick the most frequent (e.g., 人: "jin" and "nin" → use "jin")
- Long vowels: use "ou" not "ō" (e.g., 高 → "kou")
- Voiced sounds: "ga", "za", "da", "ba" (e.g., 学 → "gaku")

**Kun'yomi rules:**
- Use most common reading in romaji lowercase
- **Omit okurigana** (e.g., 高い → "taka", not "takai"; 食べる → "ta", not "taberu")
- Use `none` if kanji has no kun'yomi (e.g., 茶 → "none")
- For multiple readings, pick the most frequent

**Gloss rules:**
- Single English word only
- Lowercase
- Pick the most central/common meaning
- Avoid articles (a, the)
- Examples: "person", "day", "big", "eat", "see"

### Output Format

Update `kanji/kanji_list.json`:
```json
{
  "metadata": {
    "description": "Index mapping kanji characters to their kanji index IDs",
    "generated": "2026-01-22T10:30:00Z",
    "total_kanji": 1500
  },
  "kanji": {
    "人": {
      "kanji_id": "00001_jin_hito_person",
      "onyomi": "jin",
      "kunyomi": "hito",
      "gloss": "person"
    },
    "日": {
      "kanji_id": "00002_nichi_hi_day",
      "onyomi": "nichi",
      "kunyomi": "hi",
      "gloss": "day"
    },
    "大": {
      "kanji_id": "00003_dai_oo_big",
      "onyomi": "dai",
      "kunyomi": "oo",
      "gloss": "big"
    },
    "高": {
      "kanji_id": "00004_kou_taka_tall",
      "onyomi": "kou",
      "kunyomi": "taka",
      "gloss": "tall"
    },
    "食": {
      "kanji_id": "00005_shoku_ta_eat",
      "onyomi": "shoku",
      "kunyomi": "ta",
      "gloss": "eat"
    }
  }
}
```

### Example Assignments

| Kanji | On'yomi | Kun'yomi | Gloss | Kanji ID |
|-------|---------|----------|-------|----------|
| 人 | jin | hito | person | 00001_jin_hito_person |
| 日 | nichi | hi | day | 00002_nichi_hi_day |
| 大 | dai | oo | big | 00003_dai_oo_big |
| 山 | san | yama | mountain | 00004_san_yama_mountain |
| 川 | sen | kawa | river | 00005_sen_kawa_river |
| 畑 | none | hatake | field | 00006_none_hatake_field |
| 茶 | cha | none | tea | 00007_cha_none_tea |
| 学 | gaku | mana | learn | 00008_gaku_mana_learn |

### Workflow for Each Batch

```python
# Pseudocode for processing a batch
import json
from datetime import datetime, timezone

# Load current state
with open('kanji/kanji_list.json', 'r') as f:
    kanji_list = json.load(f)

# Load extracted kanji
with open('kanji/kanji_extracted.json', 'r') as f:
    extracted = json.load(f)

# Find unprocessed kanji
unprocessed = [
    k for k in extracted['kanji']
    if k['character'] not in kanji_list['kanji']
]

# Process next batch (e.g., first 50 unprocessed)
batch = unprocessed[:50]
next_id = len(kanji_list['kanji']) + 1

for item in batch:
    char = item['character']
    # Claude provides these based on knowledge:
    onyomi = "..."   # e.g., "jin"
    kunyomi = "..."  # e.g., "hito"
    gloss = "..."    # e.g., "person"

    kanji_id = f"{next_id:05d}_{onyomi}_{kunyomi}_{gloss}"

    kanji_list['kanji'][char] = {
        "kanji_id": kanji_id,
        "onyomi": onyomi,
        "kunyomi": kunyomi,
        "gloss": gloss
    }
    next_id += 1

# Update metadata
kanji_list['metadata']['generated'] = datetime.now(timezone.utc).isoformat()
kanji_list['metadata']['total_kanji'] = len(kanji_list['kanji'])

# Save
with open('kanji/kanji_list.json', 'w') as f:
    json.dump(kanji_list, f, ensure_ascii=False, indent=2)
```

## Verification

After each batch:
1. Verify `kanji/kanji_list.json` has correct structure
2. Check that kanji IDs follow the format
3. Verify no duplicate IDs exist
4. Ensure on'yomi/kun'yomi are valid romaji

## Progress Tracking

Keep track of progress in commit messages:
- "Assign kanji IDs 00001-00050"
- "Assign kanji IDs 00051-00100"
- etc.

## Next Step

Once ALL kanji have been assigned IDs, proceed to `04_build_kanji_json.md` to create the individual kanji entry list JSON files.
