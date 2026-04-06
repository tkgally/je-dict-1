# Handling Words with Multiple Written Forms

**Last updated**: 2026-04-06

## Overview

Many Japanese words can be written in multiple ways: different kanji, different okurigana, kanji vs. kana, old vs. new character forms, or katakana vs. hiragana. This creates significant challenges for a dictionary that needs to be both searchable and authoritative. This page analyzes the types of variation, current handling in je-dict-1, and proposes policies for when to create separate entries vs. consolidating variants into a single entry.

## Types of variation

### 1. Kanji variants (異体字・異字体)

The same word written with different kanji characters:
- 障害 / 障碍 / 障礙 (しょうがい — disability/obstacle)
- 叶う / 適う (かなう — to come true)
- 匂い / 臭い (におい — smell; though these have shifted to connote different things)

Some of these reflect genuine meaning differences that have evolved; others are purely orthographic alternatives.

### 2. Okurigana variants (送り仮名の揺れ)

Different trailing kana after the same kanji:
- 行う / 行なう (おこなう — to carry out)
- 表す / 表わす (あらわす — to express)
- 落とす / 落す (おとす — to drop)

The Japanese government's official okurigana guidelines (送り仮名の付け方) specify preferred forms, but both forms are commonly seen.

### 3. Kanji vs. kana writing (漢字・かな書き分け)

Words that can be written either in kanji or in kana:
- 出来る / できる (dekiru — can do)
- 有る / ある (aru — to exist)
- 沢山 / たくさん (takusan — many)
- 綺麗 / きれい (kirei — pretty)
- 所謂 / いわゆる (iwayuru — so-called)

Convention varies by word: some are almost always in kana (できる), some in kanji (綺麗 is common in either), some depend on register.

### 4. New vs. old kanji forms (新字体・旧字体)

Modern simplified forms vs. traditional forms:
- 国 / 國 (kuni — country)
- 学 / 學 (gaku — learning)
- 体 / 體 (tai — body)

je-dict-1 uses new forms in headwords, but learners may encounter old forms in proper names, traditional texts, or signage.

### 5. Katakana vs. hiragana

Some words can be written in either script:
- うどん / ウドン (udon)
- すし / スシ / 寿司 (sushi)
- おにぎり / オニギリ (onigiri)
- ケチ / けち (kechi — stingy)

### 6. Reading variants (読みの揺れ)

Same kanji, different accepted readings:
- 世論: せろん / よろん (public opinion)
- 早急: さっきゅう / そうきゅう (urgent)
- 重複: ちょうふく / じゅうふく (duplication)

These are especially tricky because the correct reading may be debated.

## Current handling in je-dict-1

### What exists now

- The `headword` field typically lists one primary form
- The `reading` field gives the hiragana reading
- `alternate_forms` can list variant spellings
- The search index indexes the primary headword and reading
- `find_merge_candidates.py` detects potential duplicates including variants

### Known issues

- Some variants were created as separate entries during early expansion (before duplicate checking was robust)
- The search index doesn't consistently index all alternate forms
- No systematic policy exists for when a variant deserves its own entry vs. being listed in `alternate_forms`
- The blog (February 7, 2026) notes: "I have noticed cases in which minor okurigana or kanji variations led Claude to create separate entries for what are usually regarded as the same word"

## Proposed policy: One entry or two?

### Single entry (preferred for most cases)

Consolidate into one entry when the variants are:
- **Purely orthographic**: Same pronunciation, same meaning, different writing (行う / 行なう)
- **Conventional alternatives**: One form is standard, the other is acceptable but less common (出来る / できる)
- **Script alternatives**: Katakana vs. hiragana of the same word (うどん / ウドン)

The primary headword should be the most standard/common written form. All variants go in `alternate_forms`. The notes should explain the orthographic variation if learners need to know (e.g., "Usually written in kana as できる rather than 出来る").

### Separate entries when:

- **Meaning has diverged**: 匂い (pleasant smell) vs. 臭い (bad smell) — even though historically the same word, modern usage has differentiated them
- **Reading differs significantly**: 世論(せろん) vs. 世論(よろん) could warrant a note in a single entry, but words with completely different readings for different meanings are clearly separate entries
- **Part of speech differs**: Some kanji compounds function as both nouns and na-adjectives with slightly different nuances depending on usage
- **Register or domain differs sharply**: If one form is used exclusively in legal/technical contexts and another in everyday speech, separate entries may help learners

### Edge cases requiring judgment

- **Reading variants of the same word** (世論 せろん/よろん): Generally one entry with a note about the reading variation
- **Kanji vs. kana where meaning shifts subtly**: Sometimes the kanji form implies a more literal/specific meaning and the kana form is more general/abstract. One entry with a note is usually sufficient.
- **Compound words with variant kanji** (e.g., different kanji for one component): Usually one entry unless the variant implies a different meaning

## Search index implications

For variants to work well, the search index must:

1. **Index all forms**: Every `alternate_form` must be searchable, not just the primary headword
2. **Index common kana-only forms**: If a word is frequently searched in kana (e.g., きれい for 綺麗), that search must find the entry
3. **Handle romaji variants**: Different romanization conventions (ou vs. ō vs. o for long vowels) should all work
4. **Cross-reference variant entries**: If separate entries exist for closely related variants, search results should show both

### Current search index architecture

The search index (`build/search_index_builder.py`) generates a JavaScript search index loaded client-side. It currently indexes:
- Headword (kanji form)
- Reading (hiragana)
- Romaji
- English glosses

**Needed additions**:
- Index `alternate_forms` with the same weight as headwords
- Index common kana-only spellings for words usually written in kanji
- Consider indexing the `reading` field for kanji-headword entries more prominently

## Implementation roadmap

### Phase 1: Policy documentation (immediate)
- Establish the one-entry-vs-two policy above as the official guideline
- Add guidance to the entry-guidelines skill
- Document in the consolidate-entries skill

### Phase 2: Search index enhancement (near-term)
- Modify `search_index_builder.py` to index `alternate_forms`
- Test that variant searches find the right entries
- Add romaji variant handling

### Phase 3: Systematic variant audit (medium-term)
- Run `find_merge_candidates.py` with enhanced variant detection
- Review all entries flagged as potential duplicates due to variant forms
- Merge entries that should be consolidated; add cross-references where separate entries are warranted
- Ensure all consolidated entries have complete `alternate_forms` lists

### Phase 4: Ongoing maintenance
- Duplicate checking during entry creation should catch variant forms (already partially implemented)
- Cross-model proofreading could flag inconsistent variant handling
- The consistency checking system ([entry-consistency.md](entry-consistency.md)) should verify that similar types of variants are handled the same way

## Data model considerations

The current `alternate_forms` field is a simple array of strings. It may need enhancement:

```json
{
  "alternate_forms": [
    {"form": "行なう", "type": "okurigana_variant", "note": "also common"},
    {"form": "おこなう", "type": "kana_writing", "note": "sometimes written in kana"}
  ]
}
```

This structured format would enable:
- Type-specific search indexing
- Display of variant type on the entry page
- Programmatic analysis of variant patterns across the dictionary

However, this is a schema change that would need migration for existing entries. The simpler approach is to keep `alternate_forms` as strings and add variant-type information in the notes.

## Open questions

- Should the entry page display alternate forms prominently (near the headword) or only in the notes?
- How should the kanji index handle variants? If a word has 障害 and 障碍 as variants, should both appear in the kanji index?
- For reading variants (せろん/よろん), should both readings be listed at the top of the entry or explained in notes?
- Should there be a "redirects" system where searching for a variant headword shows "Did you mean [primary form]?"

## Related pages

- [Handling Homographs](homographs.md) — the related problem of same writing, different readings/meanings
- [Cross-Reference Design](cross-references.md) — linking variant entries when they're kept separate
- [Entry Design](../project/entry-design.md) — the `alternate_forms` field
- [Entry Consistency](entry-consistency.md) — ensuring variants are handled consistently across the dictionary
- [Open Issues](../project/open-issues.md) — loanword handling, homograph disambiguation
