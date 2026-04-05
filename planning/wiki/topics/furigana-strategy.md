# Furigana Strategy

**Last updated**: 2026-04-05

## Current approach

je-dict-1 annotates **all kanji with furigana in all fields** — headwords, example sentences, and notes. The format is `{漢字|かんじ}` which the build system renders as ruby text on the website.

This is a deliberate design choice for the target audience: intermediate learners who can read kana fluently but are still building kanji knowledge.

## Why annotate everything?

### For the learner
- Removes the frustration of encountering unknown kanji in example sentences meant to teach a different word
- Allows learners to focus on vocabulary and grammar rather than kanji decoding
- Supports reading practice — learners can try to read the kanji first, then check against the furigana

### Against selective annotation
Some dictionaries only annotate "difficult" kanji, but:
- What counts as "difficult" varies enormously between learners
- A learner at N3 level might know 常用漢字 for one semantic domain but not another
- Inconsistency in annotation creates worse UX than consistent full annotation

## Implementation

- **Format**: `{漢字|かんじ}` in JSON source → `<ruby>漢字<rt>かんじ</rt></ruby>` in HTML
- **Readings are always hiragana**, never katakana (even for katakana words)
- **Compound words**: each kanji group gets its own annotation: `{飛行|ひこう}{機|き}`
- **Enforcement**: `find_missing_furigana.py` scans for unannotated kanji; run after every entry creation session

## Edge cases

- **Words normally written in kana**: する, ある, いる — no furigana needed (no kanji)
- **Words with kanji and kana forms**: 沢山/たくさん — if using kanji form, annotate; if using kana form, no annotation needed
- **Okurigana**: Only the kanji portion gets annotated: `{食|た}べる` not `{食べる|たべる}`
- **Repeated kanji in examples**: Annotate every occurrence (the rendering handles deduplication gracefully)

## Future considerations

- Could a "furigana toggle" let advanced users hide readings?
- Should there be a "kanji mode" that shows readings on hover only?
- Can furigana data be extracted to build kanji learning features?

## Related pages

- [Entry Design](../project/entry-design.md)
- [Japanese Lexicography](../research/japanese-lexicography.md)
