# Accuracy Review Session — 2026-06-10

**Task**: accuracy-review mode of unified Routine v2  
**Entry range reviewed**: 651–1150  
**Session date**: 2026-06-10  
**Model**: claude-sonnet-4-6

## Summary

Ran cross-model accuracy review (`review_accuracy.py`) on entries 651–1150 (500 entries),
producing 500 review files in `reviews/accuracy/`. Also ran furigana screening on entries
651–1011 (368 entries screened, 28 flagged — all false positives).

## Changes Applied (36 entries modified)

### Translation fixes
- **00708_juu**: ex4 translation "hang out with friends" → "read books at the library" (mistranslation of 図書館で本を読む)
- **00768_abunai**: ex8 translation "The test was risky" → "The test was close" (危なかった in test context = close/precarious)
- **00761_tsukeru**: ex5 translation "name this document" → "write your name on this document" (名前を付ける ≠ name; 名前を書く)
- **00701_hareru**: ex3 translation "tomorrow" → "this weekend" (今週の週末 mistranslated)
- **01030_itterasshai**: 7 gloss/translation instances of "have a good trip" → "see you later/take care" (いってらっしゃい is for any departure)

### Furigana fix
- **00794_kyoushitsu**: {三階|さんかい} → {三階|さんがい} in example 2 (さんがい is standard reading)

### Tag fixes — invalid semantic tags (replaced with valid VALID_SEMANTIC values)
- **00771_byouki**: 'health' → 'body-internal'
- **00787_kega**: 'health' → 'body-part'  
- **00879_reji**: 'commerce' → 'tool'
- **01031_jikokuhyou**: 'travel' → 'transportation'
- **01049_ryokan**: 'travel' → 'building'
- **01076_kan**: 'container' → 'food'
- **01122_waku**: 'change-of-state' → 'action'
- **01143_naru**: 'sound' → 'action'
- **00786_kawaku**: 'existence' → 'action'
- **01146_yaseru**: 'existence' → 'body-internal'
- **01118_nai**: 'descriptive' → 'grammatical' (ない is a grammatical negative auxiliary)
- **01114_you**: 'descriptive' → 'grammatical' (よう is primarily grammatical)

### Tag fixes — wrong formality values
- **00779_hontou, 00785_karui, 00797_mondai, 00944_ikutsu**: 'informal' → 'neutral'
- **00813_sobo, 00871_nedan, 00886_shinamono, 00913_achira, 00927_dochira, 00990_sochira, 01065_tesuto, 01068_waishatsu, 01119_subarashii, 01121_utsukushii**: 'formal' → 'neutral'
- **01070_yoroshiku**: 'formal' → 'neutral' (よろしく itself is not formal)

### Tag fixes — wrong politeness values
- **00776_gohan**: formality 'informal' → 'neutral'; politeness 'honorific' → 'polite'
- **00878_otsuri**: politeness 'honorific' → 'polite' (お prefix is beautification, not strict honorific)
- **00913_achira, 00927_dochira**: politeness 'plain' → 'polite'
- **01074_ganbatte**: politeness 'polite' → 'plain' (plain te-form)

## Screener False Positives (28 flagged, all rejected)
All furigana screener flags were false positives:
- Rendaku patterns (百→びゃく, 紙→がみ, 止→ど, etc.)
- Partial readings by design (概→おおむ, 賑→にぎ, etc.)
- Already-corrected issues (三階→さんがい in 00794 already fixed)
- Screener confusion about kanji (肘 vs 膝, 鏡台 vs 兄弟)

## FLAGS (structural issues noted, no immediate fix)
- **00765_yasashii**: Entry conflates 易しい (easy) and 優しい (kind) under same headword; may need split
- **01101_nakunaru**: Headword uses 無 kanji but sense 3 examples use 亡 kanji; structural inconsistency

## OpenRouter Spend
- Accuracy review (500 entries): ~$0.2101
- Furigana screening (368 entries): ~$0.0221
- **Total this run**: ~$0.2322
- **Daily total**: ~$0.7939 (cap: $5.00)

## Next entry for cross-model-review task
`next: 01151`
