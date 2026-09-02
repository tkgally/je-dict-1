---
name: vocabulary-notes
description: Requirements for formatting and structuring the notes field in je-dict-1 entries. Covers formatting, content organization, and readability standards.
---

# Vocabulary Notes Guidelines

The `notes` field is a critical part of each entry, providing usage information, grammar patterns, cultural context, and other details that help learners deeply understand the word. As the dictionary grows, well-structured notes become increasingly important.

## Length and shape (read first)

Notes are **short and useful, not maximally thorough**. Aim for 2–3 focused sections; four is usually too many, six or more is always too many. The "Content Categories" list below is an **inventory of what notes _can_ cover**, not a checklist to clear. Pick what the entry actually needs, then stop.

Per-field char budgets and the gloss-vs-definition rule live in `prompts/newentries.md` under "Length targets" — defer to those numbers when creating new entries. Single-sense notes typically run ~400–900 chars; multi-sense ~700–1,500 chars; hard ceilings ~1,200 / ~2,000 chars. If you cross a ceiling, cut before continuing.

## Language Requirement (CRITICAL)

**All explanatory text in notes must be in English.** This includes etymology, usage explanations, cultural context, grammar notes, and any other prose. Japanese text should appear only within example phrases, collocations, pattern demonstrations, and headwords — never as explanatory sentences.

This is a bilingual dictionary for English-speaking learners. Japanese prose explanations are too difficult for most target users.

```
✓ CORRECT: Derived from {始終|しじゅう} (from beginning to end).
✗ INCORRECT: {始終|しじゅう}が{変化|へんか}したもの。

✓ CORRECT: The kanji {躾|しつけ} is a kokuji (a kanji created in Japan).
✗ INCORRECT: 「{躾|しつけ}」は{国字|こくじ}（{日本|にほん}で{作|つく}られた{漢字|かんじ}）。
```

## Formatting Requirements (HIGH PRIORITY)

### 1. Line Breaks Between Sections

Notes with multiple topics MUST separate each topic with a blank line:

```
✓ CORRECT:
{知|し}る means to learn or come to know something for the first time.

{知|し}っている (the ている form) means 'to know' - the state of already having that knowledge.

Common mistake: Using {知|し}る when you mean 'I know.'

✗ INCORRECT:
{知|し}る means to learn or come to know something for the first time. {知|し}っている (the ている form) means 'to know' - the state of already having that knowledge. Common mistake: Using {知|し}る when you mean 'I know.'
```

### 2. Bullet Points for Lists

Any list of 2 or more items MUST use bullet points. Use the hyphen-space format (`- `):

```
✓ CORRECT:
Common compounds:
- {案内|あんない}{所|じょ}: information desk
- {道|みち}{案内|あんない}: directions
- ご{案内|あんない}: guidance (polite)

✗ INCORRECT:
Common compounds: {案内|あんない}{所|じょ} (information desk), {道|みち}{案内|あんない} (directions), ご{案内|あんない} (guidance, polite)
```

### 3. Section Headers

Use clear section headers followed by a colon for distinct categories of information.
**Headers come from a closed list** (`build/data/note_headers.json`; CI blocks a new
header outside it, and `build/normalize_notes.py` renames legacy spellings):

| Canonical header | Use it for |
|---|---|
| `USAGE:` | how and when the word is used; nuance; restrictions |
| `COMMON COLLOCATIONS:` | bulleted word combinations with glosses |
| `COMMON PATTERNS:` | grammatical frames: particles, constructions |
| `COMMON EXPRESSIONS:` | fixed phrases and idioms built on the word |
| `COMPOUNDS:` | compound words containing the headword |
| `FORMS:` | inflectional and derived forms (〜く, 〜さ, 〜的, 〜化), variant spellings |
| `SIMILAR WORDS:` | near-synonyms, contrasts, antonyms, each with the distinction |
| `RELATED WORDS:` | thematically connected vocabulary |
| `TRANSITIVITY:` | verbs: 自動詞/他動詞 and the pair |
| `ASPECT (ている):` | verbs: what ている means with this verb |
| `REGISTER:` | formality, politeness, spoken/written |
| `KEIGO:` | honorific and humble equivalents |
| `CULTURAL NOTE:` | cultural, social, or practical background |
| `ETYMOLOGY:` | origin, including a loanword's source word |
| `WATCH OUT:` | pitfalls, confusable words, homophone traps |
| `FUNCTIONS:` | particles and grammar words: each function with a pattern |
| `COUNTING PATTERNS:` | counters: number forms and sound changes |
| `TYPES:` | kinds of the thing named, when the list helps |
| `POSITION IN SENTENCE:` | adverbs and connectives |
| `PRONUNCIATION:` | reading and accent notes when they matter |
| `WRITING:` | kanji versus kana, variant kanji, okurigana |

Legacy names such as `GRAMMAR:`, `COLLOCATIONS:`, `SIMILAR VERBS:`, `USAGE NOTES:`,
`CONTRAST:`, `CULTURAL CONTEXT:`, `COMMON MISTAKES:` map to the canonical ones above
and are renamed by the normalizer. Do not invent a topical header ("PET ADOPTION:");
put that material under `USAGE:` or `CULTURAL NOTE:`.

Example:

```
TRANSITIVITY:
- Type: {自動詞|じどうし} (intransitive)
- Pair: {上|あ}げる (transitive)

COMMON PATTERNS:
- {値段|ねだん}が{上|あ}がる (prices rise)
- {気温|きおん}が{上|あ}がる (temperature rises)
```

### 4. Single-Topic Notes

For entries with only one note or a simple explanation, a single paragraph is acceptable:

```
✓ ACCEPTABLE:
この is a demonstrative that refers to things near the speaker. It always modifies a noun and cannot stand alone.
```

## Content Categories

Notes should draw from this inventory — **not all of them, not even most of them**. A typical entry uses two or three. Pick categories that add something the gloss and examples don't already convey.

### For All Entries (in approximate order of priority)

1. **Core semantic explanation** - What the word fundamentally means beyond the gloss. Skip if the gloss already captures it.
2. **Common collocations** - Typical word pairings that aid natural usage. Usually 3–6 bulleted items, not exhaustive.
3. **Similar word distinctions** - How this word differs from near-synonyms. Include only when learners would otherwise confuse them.
4. **Register notes** - Formality level and situational appropriateness. Include only when the register is non-obvious or markedly different from neutral.
5. **Common mistakes** - What learners typically get wrong. Include only when a specific, frequent error exists.
6. **Cultural context** - When cultural background aids understanding. Include only when it's load-bearing for the meaning.

Adding categories that aren't needed (e.g., a generic "USAGE NOTES" or "TYPICAL CONTEXTS" block that restates the gloss) makes notes worse, not better.

### Entry-Type-Specific Content

See the corresponding skill for type-specific requirements:
- **Verbs**: See `verb-entry` skill (transitivity, aspect, particle patterns)
- **Adjectives**: See `adjective-entry` skill (forms, similar words)
- **Particles**: See `particle-entry` skill (predicate lists, contrasts)
- **Nouns/Adverbs/Expressions**: See `other-entries` skill

## Structure Templates

### Verb Notes Template

```
[One-sentence summary of the verb's core meaning.]

TRANSITIVITY:
- Type: {自動詞|じどうし}/{他動詞|たどうし}
- Pair: [pair verb] (if exists)

ASPECT (ている):
[Explanation of what ている means for this verb]

COMMON PATTERNS:
- [pattern 1]
- [pattern 2]
- [pattern 3]

[Additional notes: register, negative usage, keigo, etc.]
```

### Noun Notes Template

```
[One-sentence explanation of the noun's scope or meaning.]

COMMON EXPRESSIONS:
- [collocation 1]
- [collocation 2]

[Scope clarification if different from English]

[Related words if helpful]
```

### Adjective Notes Template

```
[Adjective] is an [i-adjective/na-adjective].

FORMS:
- Adverbial: [form]
- Noun form: [form] (if natural)

SIMILAR WORDS:
- [word 1] vs. [word 2]: [distinction]

[Register or special usage notes]
```

### Simple Entry Template

For entries that don't need extensive notes:

```
[Core explanation in 1-2 sentences.]

[One optional list of 2-3 related items if helpful.]
```

## Formatting Technical Details

### Newlines in JSON

In the JSON `notes` field, use `\n` for line breaks and `\n\n` for paragraph breaks:

```json
"notes": "First paragraph here.\n\nSecond paragraph here.\n\nBullet list:\n- Item one\n- Item two"
```

### Furigana (CRITICAL)

**All kanji in notes MUST have furigana** using the `{漢字|かな}` notation.

This is a common source of errors. Every kanji - in idioms, collocations, cultural notes, alternative kanji forms, etc. - must be annotated:

```
✓ {案内|あんない}する means to guide.
✗ 案内する means to guide.

✓ IDIOM: {暖簾|のれん}に{腕押|うでお}し
✗ IDIOM: 暖簾に腕押し

✓ KANJI: Sometimes written as {家鴨|あひる}
✗ KANJI: Sometimes written as 家鴨
```

**Verify with:**
```bash
python3 build/verify_furigana.py <entry_id>
```

### Punctuation

- Use Japanese punctuation (。、) within Japanese text
- Use English punctuation in English explanations
- Colons after section headers: `COMMON PATTERNS:`
- Hyphens for bullet points: `- item`

## Quality Checklist

Before finalizing notes:

- [ ] **All explanatory prose is in English** - no Japanese-language explanations
- [ ] Multiple topics are separated by blank lines
- [ ] Lists of 2+ items use bullet points
- [ ] **All kanji have furigana** - including idioms, collocations, kanji variants
- [ ] Verify: `python3 build/verify_furigana.py <entry_id>` shows "✓ OK"
- [ ] Section headers are clear and consistent
- [ ] Information is ordered by usefulness to learners
- [ ] No run-on paragraphs mixing unrelated information
- [ ] Length is appropriate (not too sparse, not overwhelming)

## Examples of Well-Formatted Notes

### Example 1: Verb Entry

```
{開|あ}く is an intransitive verb meaning something opens by itself or becomes open.

TRANSITIVITY:
- Type: {自動詞|じどうし} (intransitive)
- Pair: {開|あ}ける (transitive, to open something)

ASPECT (ている):
- {開|あ}いている means 'is open' (resulting state), not 'is opening'
- Example: {店|みせ}が{開|あ}いている = The store is open

COMMON PATTERNS:
- {ドア|どあ}が{開|あ}く (door opens)
- {店|みせ}が{開|あ}く (store opens)
- {花|はな}が{開|あ}く (flower blooms)
- {穴|あな}が{開|あ}く (hole opens/forms)
```

### Example 2: Noun Entry

```
{電話|でんわ} refers to both the telephone device and the act of calling.

COMMON EXPRESSIONS:
- {電話|でんわ}をかける: to make a call
- {電話|でんわ}に{出|で}る: to answer the phone
- {電話|でんわ}を{切|き}る: to hang up
- {電話|でんわ}{番号|ばんごう}: phone number

Note: {携帯|けいたい}{電話|でんわ} (mobile phone) is often shortened to {携帯|けいたい} or ケータイ in casual speech.
```

### Example 3: Simple Entry

```
ここ refers to a location near the speaker. It's part of the ko-so-a-do demonstrative system.

Related words:
- そこ: there (near listener)
- あそこ: over there (far from both)
- どこ: where (question)
```

## Notes on Web Display

The web interface renders notes with line break support. To ensure proper display:

1. Use `\n\n` (double newline) between paragraphs/sections
2. Use `\n` (single newline) before each bullet point
3. Bullet points with `- ` will display as a list

The rendering converts newlines appropriately, so focus on logical structure in the JSON.

## POS Note Templates (Machine-Readable)

The expected note structure for each POS is defined in `build/note_templates.json`. This file is used by `build/score_note_quality.py` to score note quality. The minimums below are floors, not targets — most well-written notes sit comfortably above the minimum but well under the ceiling.

| POS | Required Sections | Min Length | Typical Length | Hard Ceiling |
|-----|-------------------|------------|----------------|--------------|
| verb-ichidan, verb-godan | transitivity, common patterns | 120 chars | 500–1,000 | 1,500 |
| verb-suru, verb-irregular | common patterns | 100 chars | 400–900 | 1,200 |
| adjective-na, adjective-i | usage | 80 chars | 400–800 | 1,200 |
| adjective-no | usage | 60 chars | 300–700 | 1,000 |
| noun | (none required) | 60 chars | 400–900 | 1,200 |
| adverb | (none required) | 60 chars | 300–700 | 1,000 |
| particle | functions | 100 chars | 500–1,200 | 1,800 |
| counter | counting patterns | 80 chars | 400–900 | 1,200 |
| expression | (none required) | 60 chars | 300–700 | 1,000 |

Multi-sense entries can run roughly twice as long as single-sense entries of the same POS, capped at ~2,000 chars total. If you're near a hard ceiling, cut a section before continuing.

Optional sections that may appear when they earn their place: collocations, similar words, register, cultural context, forms, aspect. **Optional does not mean "include all of them."** See `build/note_templates.json` for the complete list per POS.

To check an entry's note quality score:
```bash
python3 build/score_note_quality.py --id ENTRY_ID
```
