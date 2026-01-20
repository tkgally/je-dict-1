# Furigana Completeness Review Task

This task ensures all kanji in dictionary entries have proper furigana markup.

## Furigana Format

The project uses inline furigana notation: `{kanji|reading}`

Examples:
- `{食|た}べる` - Single kanji
- `{日本語|にほんご}` - Compound
- `{食|た}べ{物|もの}` - Multiple furigana in one word

This is converted to HTML ruby tags during build:
```html
<ruby>食<rt>た</rt></ruby>べる
```

## Fields Requiring Furigana

1. **headword**: The main entry word (REQUIRED)
2. **examples.japanese**: All example sentences
3. **notes**: Any kanji in the notes field
4. **cross_references.headword**: Reference display forms
5. **predicates_requiring**: For particle entries
6. **fixed_patterns**: Pattern examples

## Review Process

### 1. Automated Detection

Check for entries missing furigana:
```bash
python3 build/verify_furigana.py
```

Review `entries_without_furigana.json` for known gaps.

### 2. Manual Verification

For each entry, scan:
- [ ] Headword has furigana on all kanji
- [ ] All examples have complete furigana
- [ ] Notes field has furigana where needed
- [ ] Cross-reference headwords have furigana

### 3. Common Patterns to Watch

Kanji that often miss furigana:
- Counters: 個, 本, 枚, etc.
- Common kanji: 人, 時, 日, 年
- Compound readings: 今日, 昨日, 明日

## Furigana Rules

### Standard Reading
Use the reading as pronounced:
- `{今日|きょう}` (not `{今日|こんにち}` unless that pronunciation)

### Irregular Readings
Maintain the actual pronunciation:
- `{大人|おとな}` (irregular compound reading)
- `{昨日|きのう}` (irregular compound reading)

### Okurigana
Don't include okurigana in the furigana brackets:
- `{食|た}べる` (correct)
- `{食べ|たべ}る` (incorrect)

### Repeated Kanji
Each instance needs furigana:
- `{日|ひ}から{日|ひ}へ`

## Quality Checks

- [ ] Readings are correct (match actual pronunciation)
- [ ] Brackets are properly closed
- [ ] No nested brackets
- [ ] Consistent with other entries using same kanji

## Recording Changes

```json
{
  "entry_id": "00100_example",
  "furigana_changes": [
    {
      "field": "headword",
      "old": "食べる",
      "new": "{食|た}べる"
    },
    {
      "field": "examples[0].japanese",
      "old": "ご飯を食べる",
      "new": "ご{飯|はん}を{食|た}べる"
    }
  ]
}
```

## Batch Processing

1. Start with `entries_without_furigana.json`
2. Process basic tier entries first
3. Focus on headwords, then examples
4. Notes field last (often longest)

## Verification

After adding furigana, verify:
```bash
python3 build/validate.py
python3 build/build_flat.py --dry-run
```

Check that ruby tags render correctly in the built HTML.
