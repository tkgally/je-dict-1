---
name: cross-reference-entry
description: Guidelines for adding and maintaining cross-references between dictionary entries. Covers reference types, format requirements, and extraction from notes.
---

# Cross-Reference Entry Guidelines

When creating or revising entries, add cross-references to related vocabulary. This improves navigation and helps learners understand word relationships.

## Cross-Reference Types

### 1. `pair` - Transitivity Pairs (HIGH PRIORITY)
Use for verb transitivity pairs ({自動詞|じどうし}/{他動詞|たどうし}).

```json
{
  "type": "pair",
  "reading": "しまる",
  "headword": "{閉|し}まる",
  "label": "intransitive"
}
```

**Labels:** `intransitive` or `transitive`

**Common pairs:**
- 開く/開ける, 閉まる/閉める, 始まる/始める
- 出る/出す, 入る/入れる, 付く/付ける
- 決まる/決める, 変わる/変える, 上がる/上げる

### 2. `antonym` - Opposites (HIGH PRIORITY)
Use for direct opposites.

```json
{
  "type": "antonym",
  "reading": "あける",
  "headword": "{開|あ}ける",
  "label": "to open"
}
```

**Label:** Brief gloss of target word

### 3. `keigo` - Honorific/Humble Forms (HIGH PRIORITY)
Use for formal speech equivalents.

```json
{
  "type": "keigo",
  "reading": "めしあがる",
  "headword": "{召|め}し{上|あ}がる",
  "label": "honorific"
}
```

**Labels:** `honorific` or `humble`

**Common keigo links:**
- 食べる → 召し上がる (hon.), いただく (hum.)
- 行く → いらっしゃる (hon.), 参る (hum.)
- 言う → おっしゃる (hon.), 申す (hum.)
- 見る → ご覧になる (hon.), 拝見する (hum.)

### 4. `synonym` - Similar Meaning (MEDIUM PRIORITY)
Use for words with similar meaning but different nuance.

```json
{
  "type": "synonym",
  "reading": "りかいする",
  "headword": "{理解|りかい}する",
  "label": "formal"
}
```

**Label:** Distinguishing characteristic (e.g., "formal", "written", "casual")

### 5. `contrast` - Easily Confused (MEDIUM PRIORITY)
Use for words learners often confuse.

```json
{
  "type": "contrast",
  "reading": "が",
  "headword": "が",
  "label": "subject marking"
}
```

Especially important for:
- Particles: は vs が, に vs で, に vs へ
- Similar verbs: 聞く vs 聴く, 見る vs 見える vs 見せる

### 6. `related` - Semantically Connected (LOW PRIORITY)
Use for derived words, compounds, or thematically related vocabulary.

```json
{
  "type": "related",
  "reading": "たべもの",
  "headword": "{食|た}べ{物|もの}",
  "label": "food (noun)"
}
```

### 7. `see_also` - General Reference (LOW PRIORITY)
Use for general cross-references that don't fit other categories.

```json
{
  "type": "see_also",
  "reading": "しょくじ",
  "headword": "{食事|しょくじ}",
  "label": null
}
```

## Format Requirements

Each cross-reference object requires:

| Field | Required | Description |
|-------|----------|-------------|
| `type` | Yes | One of: pair, synonym, antonym, keigo, related, see_also, contrast |
| `reading` | Yes | Hiragana reading (primary lookup key) |
| `headword` | No* | Display form with furigana (recommended) |
| `label` | No | Short descriptor |

*Headword is optional but strongly recommended for display purposes.

## Priority Order

When adding references to entries, prioritize:

1. **HIGH** - Always add if applicable:
   - Transitivity pairs (pair)
   - Keigo equivalents (keigo)
   - Direct antonyms (antonym)

2. **MEDIUM** - Add when natural:
   - Close synonyms with clear distinction (synonym)
   - Particle contrasts (contrast)
   - Related compounds (related)

3. **LOW** - Add sparingly:
   - Thematic groupings
   - General see_also references

## Extracting from Notes

The notes field often contains vocabulary that should be cross-referenced. Look for:

### Patterns to Extract

1. **Pair verbs:**
   - "Pair: {閉|し}まる" or "PAIR VERB: ..."
   - "The intransitive counterpart is ..."

2. **Antonyms:**
   - "Opposite: {開|あ}ける"
   - "Antonym: ..."

3. **Keigo:**
   - "{召|め}し{上|あ}がる (honorific)"
   - "Humble form: いただく"

4. **Related words:**
   - Words in furigana notation within COMMON PATTERNS
   - Nouns derived from verbs: 食べる → 食べ物

### Automated Extraction

Run the extraction script to find potential references:

```bash
# Dry run - see proposed changes
python3 build/extract_references.py

# Apply changes
python3 build/extract_references.py --apply

# Single entry
python3 build/extract_references.py --id taberu_00001
```

## Handling Non-Existent Entries

**Important:** You can add references to entries that don't exist yet.

- Use `reading` as the primary key (required)
- Include `headword` for display purposes
- The link will be marked as "pending" in the web interface
- When the target entry is created, the link automatically becomes active

This allows you to:
- Plan future entries
- Track vocabulary relationships before full coverage
- Show learners related vocabulary even if not yet in dictionary

## Validation

After adding references, validate:

```bash
python3 build/validate.py --id {entry_id}
```

The validator checks:
- Required fields present (type, reading)
- Valid type values
- Reading is valid hiragana
- No self-references

## Example Entry

Before:
```json
{
  "id": "shimeru_00005",
  "cross_references": []
}
```

After:
```json
{
  "id": "shimeru_00005",
  "cross_references": [
    {
      "type": "pair",
      "reading": "しまる",
      "headword": "{閉|し}まる",
      "label": "intransitive"
    },
    {
      "type": "antonym",
      "reading": "あける",
      "headword": "{開|あ}ける",
      "label": "to open"
    }
  ]
}
```

## Quality Checklist

- [ ] Transitivity pair linked (for verbs)
- [ ] Keigo forms linked (for common verbs)
- [ ] Antonyms linked (if obvious opposite exists)
- [ ] References in notes are also in cross_references
- [ ] Each reference has correct type
- [ ] Reading is valid hiragana
- [ ] Headword uses proper furigana notation
- [ ] Labels are concise and consistent
