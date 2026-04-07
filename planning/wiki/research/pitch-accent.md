# Pitch Accent in Japanese Learner Dictionaries

**Last updated**: 2026-04-07

## Overview

Japanese is a pitch-accent language: the relative pitch (high vs. low) of morae within a word is lexically determined and can distinguish meaning. Unlike stress-accent languages such as English, where stressed syllables are louder, longer, and higher-pitched, Japanese pitch accent primarily involves a contrast between high (H) and low (L) pitch across morae. This suprasegmental feature is critical for natural-sounding Japanese and, in some cases, for basic intelligibility.

Most general-purpose Japanese-English learner dictionaries (Jisho.org, JMdict, Takoboto) either omit pitch accent information entirely or treat it as optional. Dedicated accent dictionaries exist for native speakers, but their use by L2 learners is limited. This page surveys the landscape and considers what, if anything, je-dict-1 should do about pitch accent.

## The four accent patterns

Standard Tokyo Japanese has four basic accent pattern types, classified by the position of the pitch drop:

| Pattern | Japanese | Description | Example |
|---------|----------|-------------|---------|
| **Heiban** (平板) | 平板型 | No drop within the word; pitch rises after mora 1 and stays high. Drop occurs on the first mora of a following particle. | さくら (cherry): L-H-H |
| **Atamadaka** (頭高) | 頭高型 | Drop after the first mora. | いのち (life): H-L-L |
| **Nakadaka** (中高) | 中高型 | Drop somewhere in the middle of the word (after mora 2, 3, etc.). | おとこ (man): L-H-L |
| **Odaka** (尾高) | 尾高型 | Drop after the last mora — identical to heiban in isolation but distinguishable when followed by a particle. | やま (mountain): L-H + が→L |

The accent position is typically noted as a number: [0] = heiban, [1] = atamadaka, [2] = drop after mora 2, etc. A three-mora word like さくら [0] is heiban, while いのち [1] is atamadaka.

Approximately 55–60% of common Japanese words are heiban in Standard Tokyo Japanese, making it the dominant pattern.

## Why pitch accent matters

### Minimal pairs

Some words are distinguished solely by pitch accent:

| Writing | Pitch | Meaning |
|---------|-------|---------|
| 雨 あめ | H-L [1] | rain |
| 飴 あめ | L-H [0] | candy |
| 箸 はし | H-L [1] | chopsticks |
| 橋 はし | L-H [2] | bridge |
| 端 はし | L-H [0] | edge |
| 酒 さけ | L-H [0] | alcohol |
| 鮭 さけ | H-L [1] | salmon |

True minimal pairs are relatively uncommon in Japanese — context resolves most ambiguity. However, incorrect pitch patterns accumulate into a broadly unnatural prosody that native speakers perceive as a strong foreign accent.

### Research on intelligibility

Research consistently shows that pitch accent is a significant predictor of perceived foreign accent and speech intelligibility in L2 Japanese:

- **Muradás-Taylor (2022)** studied English speakers' production of Japanese pitch accent and found low accuracy across experience levels, suggesting that pitch accent is not naturally acquired through exposure alone and may require explicit instruction.
- **Idemaru, Wei & Gubbins (2019)** found that tone (pitch accent and intonation patterns) is a robust predictor of accent rating in L2 Japanese across different L1 backgrounds.
- A UCL study (2020) on English-speaking learners concluded that pitch accent errors contribute to "distorted prosody in larger units, adversely affecting speech intelligibility and processing."

The implication: even if individual pitch accent errors rarely cause misunderstanding, systematic inaccuracy makes the speaker harder to understand and listen to.

## Existing accent resources

### For native speakers

| Resource | Description |
|----------|-------------|
| **NHK日本語発音アクセント辞典** (2016, 2nd ed.) | The gold standard. ~75,000 headwords with accent notation. Audio by NHK announcers. Entirely in Japanese. |
| **新明解日本語アクセント辞典** (Shinmeikai, 2014, 2nd ed.) | Another authoritative native-speaker reference. ~75,000 entries. |

### For learners

| Resource | Description |
|----------|-------------|
| **OJAD** (Online Japanese Accent Dictionary) | Free web tool from the University of Tokyo. Covers ~9,000 nouns and ~3,500 declinable words (~42,300 conjugation patterns). Visual pitch contour displays. Includes "Suzuki-kun" prosody tutor for sentence-level intonation. |
| **Kanshudo** | Displays pitch accent data for dictionary entries. Notation uses visual high/low markers. |
| **Migaku** | Browser extension and learning tool that overlays pitch accent data on Japanese text. |
| **Jisho.org** | Community requests for pitch accent data have been ongoing since 2016+, but it remains unimplemented as of 2026. |

OJAD is the most pedagogically developed tool. Research by Nakamura et al. (2013) and subsequent studies have demonstrated its effectiveness for prosody training, with experiments showing that the tool's accent nucleus assignment to given texts is more accurate than that of native speakers.

## Notation systems

Several notation systems are used across resources:

### Numeric notation
The most common system in dictionaries. A single number indicates the mora after which the pitch drops:
- [0] = heiban (no drop within the word)
- [1] = atamadaka (drop after mora 1)
- [n] = drop after mora n

Example: たべる [0] = heiban, あたま [3] = drop after mora 3 (L-H-H-L with particle)

### Binary pitch marks
Visual notation showing H/L on each mora. Common in textbooks and some online tools:
- あ↓め (rain): HL
- あめ (candy): LH

### Line/curve notation
OJAD and some tools draw a pitch contour line above or through the word, visually showing the rise and fall. This is intuitive but requires graphical rendering.

### Color coding
Some tools (Migaku, certain Anki add-ons) color-code morae: red for the accented mora, blue for heiban, etc.

## The case for including pitch accent in learner dictionaries

**Arguments for:**
1. **Pronunciation accuracy** — Without pitch information, learners have no way to know the correct pitch pattern except by hearing each word individually.
2. **Minimal pairs** — A small but meaningful set of words are distinguished only by pitch.
3. **Natural prosody** — Correct word-level pitch contributes to natural sentence-level intonation.
4. **Conjugation affects pitch** — Verb and adjective conjugation changes pitch patterns in systematic but non-obvious ways. OJAD's conjugation tables demonstrate this complexity.

**Arguments against:**
1. **Cognitive load** — Intermediate learners already manage kanji, grammar, and vocabulary. Adding pitch accent notation may overwhelm.
2. **Limited functional impact** — Context resolves almost all pitch-accent ambiguities. Unlike Chinese tones, Japanese pitch accent rarely causes true misunderstanding.
3. **Regional variation** — Pitch patterns vary significantly across dialects. Kansai Japanese has substantially different patterns from Standard Tokyo Japanese. Teaching "the" pitch accent implies Tokyo is the only correct variety.
4. **Data availability** — No open, comprehensive, machine-readable pitch accent dataset exists that could be easily integrated into a dictionary build pipeline.
5. **Display complexity** — Numeric notation is compact but opaque to beginners; visual notation requires custom rendering.

## Implications for je-dict-1

### Current status

je-dict-1 does not include pitch accent data. The entry schema has no field for accent notation.

### Assessment

Adding pitch accent to je-dict-1 would be a significant undertaking:

1. **Data sourcing** — There is no freely available, comprehensive pitch accent database in a format suitable for bulk integration. OJAD covers a subset of vocabulary. The NHK and Shinmeikai dictionaries are copyrighted. Manual annotation of 22,700+ entries is impractical.

2. **Schema changes** — A new field (e.g., `"pitch_accent": [0]` or `"pitch_accent": "LHH"`) would need to be added to `build/schema.json` and rendered by `entry_renderer.py`.

3. **Display design** — The most learner-friendly display (visual pitch contour) requires additional CSS/SVG rendering. Numeric notation is simpler but less intuitive.

4. **Conjugation complexity** — Pitch accent changes with conjugation. Verbs alone would need accent data for dozens of conjugated forms, significantly expanding the conjugation tables.

5. **Priority** — Given that je-dict-1 focuses on vocabulary building for intermediate learners, and that pitch accent errors rarely impede comprehension at this level, pitch accent is a lower priority than completing the current quality initiatives (transitivity marking, collocation patterns, cross-references, furigana coverage).

### Recommendation

Pitch accent is best left as a **future enhancement** rather than a current priority. If pursued:
- Start with a `pitch_accent` field in the schema accepting numeric notation (e.g., `[0]`, `[1]`, `[3]`)
- Populate it incrementally, starting with basic-tier entries where minimal pairs exist
- Display as a simple numeric indicator initially, with visual rendering as a later refinement
- Consider linking to OJAD as an external resource for users who want accent data

A more immediate step would be to **mention pitch accent in the notes field** of entries that form well-known minimal pairs (雨/飴, 橋/箸, etc.), alerting learners to the distinction without requiring a full-scale accent data integration.

## References

- Muradás-Taylor, B. (2022). "Accuracy and Stability in English Speakers' Production of Japanese Pitch Accent." *Language and Speech*, 65(2).
- Idemaru, K., Wei, P., & Gubbins, L. (2019). "Acoustic Sources of Accent in Second Language Japanese Speech." *Language and Speech*, 62(3).
- Nakamura, M., et al. (2013). "Development of a web framework for teaching and learning Japanese prosody: OJAD." *Interspeech 2013*.
- Hirano, T., et al. (2013). "OJAD: a free online accent and intonation dictionary for teachers and learners of Japanese." *SLaTE 2013*.
- NHK Broadcasting Culture Research Institute (2016). *NHK日本語発音アクセント辞典* (2nd ed.).
- Kindaichi, H. & Akinaga, K. (2014). *新明解日本語アクセント辞典* (2nd ed.). Sanseido.

## Related pages

- [Japanese Lexicography](japanese-lexicography.md) — broader challenges in Japanese dictionary-making
- [Learner Lexicography](learner-lexicography.md) — principles of pedagogical dictionary design
- [Digital Dictionary UX](digital-dictionary-ux.md) — interface design considerations
- [Vocabulary Acquisition](vocabulary-acquisition.md) — how L2 learners acquire vocabulary
- [Audio Coverage Expansion](../ideas/audio-expansion.md) — related audio enhancement strategies
