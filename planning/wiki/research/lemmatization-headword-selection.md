# Lemmatization and Headword Selection

**Last updated**: 2026-05-14

## Overview

Every dictionary must answer two fundamental questions about its macrostructure: *what gets its own entry?* and *in what form is it listed?* The first question is headword selection — choosing which lexical items deserve independent entries. The second is lemmatization — determining the canonical form (the lemma) under which an item is filed. These decisions shape how large a dictionary is, how users find information, and how the dictionary carves up the lexicon into manageable units.

For a Japanese-English learner's dictionary like je-dict-1, both questions are complicated by the morphological and orthographic richness of Japanese: agglutinative verb morphology, multiple writing systems, productive compounding, and the suru-verb construction all make headword selection harder than in English lexicography.

## The lemma: choosing the citation form

### What a lemma is

A lemma is the conventional form chosen to represent a lexical item in a dictionary. It is *not* a theoretical construct — it is a practical convention that varies by language, dictionary tradition, and target audience. The same word may have different lemmas in different dictionaries (Svensén 2009, ch. 5).

Key properties of a good lemma:
- **Predictable**: users can find the form they expect
- **Morphologically basic**: typically the least marked form in the paradigm
- **Unique**: one lemma per lexical unit (modulo homographs)

### Citation form conventions by language

| Language | Citation form | Notes |
|----------|--------------|-------|
| English | Base/infinitive (run, beautiful) | No inflection |
| French | Infinitive (courir), masculine singular (beau) | |
| Latin | 1st person singular present indicative (curro) | |
| Arabic | 3rd person masculine singular past (kataba) | Root-based dictionaries use the three-letter root instead |
| Japanese | Non-past plain form (走る, 美しい, 静かだ) | Verbs in dictionary form (-u ending); adjectives in -い/-だ |

Japanese follows a straightforward convention for verbs (dictionary form = non-past plain) and adjectives (non-past plain). Nouns have no inflection, so the bare form serves as the lemma. The real complexity lies elsewhere: in orthographic variation and in deciding what counts as "one word."

### The word-counting-unit debate

Vocabulary researchers distinguish three granularities (Nation 2001; McLean 2018):

- **Word family**: base + all inflectional and derivational relatives (teach → teaches, teaching, taught, teacher, teachable). Bauer & Nation (1993) define six levels of increasing derivational distance.
- **Lemma**: base + inflectional forms of the same part of speech (teach → teaches, teaching, taught; but *not* teacher).
- **Flemma** (McLean 2018): like lemma but collapsing parts of speech (the noun *run* and the verb *run* share a flemma).

This debate matters for dictionaries because it determines how entries are grouped. A dictionary organized by word families would nest *teacher* under *teach*; one organized by lemmas gives each its own entry. Learner dictionaries overwhelmingly choose **lemma-level entries** — each part of speech gets its own headword — because learners cannot reliably infer derived meanings (Schmitt 2010).

## Headword selection: what gets an entry?

### The core principle

Lehmann (2024) identifies a key criterion: **non-inferability**. If a form's meaning and grammatical behavior can be reliably predicted from its components and the rules of the language, it does not need its own entry. Conversely, if a form is semantically opaque, syntactically irregular, or conventionalized in ways the learner cannot predict, it merits inclusion.

This principle interacts with dictionary type and audience:
- A *comprehensive* dictionary (like OED or Kenkyusha 5th) includes even regular derivatives for documentary completeness
- A *learner's* dictionary is selective: it includes what learners need and cannot infer

### Atkins & Rundell's (2008) framework

*The Oxford Guide to Practical Lexicography* describes headword selection as proceeding in stages:

1. **Initial word list**: drawn from a corpus, typically using frequency cutoffs
2. **Expansion**: adding items below the frequency threshold that learners still need (function words, culturally important terms, productive affixes)
3. **Pruning**: removing proper names (unless culturally essential), highly technical terms, transparent compounds, regular derivatives
4. **Entry-status decisions**: for each item that passes, decide whether it gets a full entry, a run-on (brief treatment appended to a related entry), or a cross-reference

### Entry vs. subentry vs. run-on

Traditional print dictionaries distinguish:

| Type | Description | Example |
|------|-------------|---------|
| **Main entry** | Full treatment with own headword | *beautiful* |
| **Run-on** | Morphologically related derivative appended to a main entry | *beautifully*, *beautifulness* under *beautiful* |
| **Subentry** | Compound or phrase treated within a host entry | *beauty sleep* under *beauty* |
| **Cross-reference** | Pointer to another entry | *See also: gorgeous* |

In digital dictionaries, the physical-ordering constraint that motivated nesting disappears. As Lehmann notes, when records can be sorted dynamically, "the macrostructure loses its importance." Every item can have its own entry without wasting physical space, so the nesting question becomes purely about *user benefit*: does the learner gain from seeing this form in the context of its base?

### Criteria for independent entries

Drawing from Lehmann (2024), Svensén (2009), Atkins & Rundell (2008), and Halpern (2010), the main criteria are:

| Criterion | Gets own entry if... | Treated within host if... |
|-----------|---------------------|--------------------------|
| **Semantic opacity** | Meaning not predictable from parts | Meaning transparently derived |
| **Frequency** | Common enough to be independently useful | Rare |
| **Grammatical difference** | Different POS or argument structure from base | Same POS, predictable syntax |
| **Lookup probability** | User likely to search for this form | User likely to find it from the base |
| **Morphological distance** | Several derivation steps from base | One regular step |
| **Conventionalization** | Has collocations, register restrictions, or cultural associations of its own | Generic |

## Japanese-specific challenges

### 1. Orthographic variation as a lemmatization problem

Japanese words routinely appear in multiple written forms: kanji vs. kana (出来る vs. できる), alternative kanji (障害 vs. 障碍), okurigana variants (行う vs. 行なう), and old vs. new character forms (國 vs. 国). Each written form is a potential lookup key, but only one should be the canonical headword.

Halpern (2010) identifies orthographic variation as "a major challenge" in CJK lexicography because the same lemma maps to multiple surface forms. In Japanese specifically, the interaction of three scripts (hiragana, katakana, kanji) with reading ambiguity (multiple on'yomi and kun'yomi per character) creates a many-to-many relationship between written forms and lemmas.

**Practical consequence for digital dictionaries**: The headword can be the most common written form, with all variants indexed for search. The user finds the entry regardless of which form they type. This is what JMdict does (214,000+ entries with orthographic variants stored in the kanji element), and what je-dict-1 does via `headword_alternatives` and search index normalization.

### 2. The suru-verb problem

Japanese creates verbs from Sino-Japanese nouns by appending する: 勉強する (to study), 運動する (to exercise), 電話する (to telephone). The lexicographic question is whether 勉強 (noun) and 勉強する (verb) should be one entry or two.

Major dictionaries split:
- **JMdict**: single entry tagged as both noun and suru-verb (e.g., `n,vs` for 勉強)
- **Kenkyusha**: typically one entry with the noun as headword, noting the verbal use
- **Wisdom**: single entry with する forms in the example sentences

je-dict-1 follows a **combined entry** approach: the headword is the noun form, but the entry carries `verb-suru` in its POS tags and includes verbal examples and conjugation data. This is practical because the noun and verb share a definition, examples naturally mix both uses, and a separate verb entry would duplicate content.

The edge cases are nouns where the suru-verb use has diverged semantically from the noun (e.g., 遠慮 as a noun means "reserve/restraint" but 遠慮する in practice means "to refrain/decline"), or where the verb use is far more common than the nominal use. These may benefit from extra sense divisions within the combined entry.

### 3. Compound words and the entry-scope boundary

Japanese compounding is extremely productive:

- **Noun + noun**: 駅前 (station-front), 台風 (typhoon), 国際 (international)
- **Verb compounds** (V1 + V2): 飛び込む (jump in), 持ち帰る (take home)
- **Noun + する**: already discussed above
- **Prefix/suffix compounds**: お茶 (tea, polite), 子供たち (-tachi plural), 食べ方 (-kata, way of eating)

The non-inferability principle suggests:
- **Lexicalized compounds** with opaque or specialized meanings → own entry (打ち明ける "to confess" ≠ 打つ + 明ける)
- **Transparent compounds** where the meaning follows from the parts → do not need entries, but may get them for convenience or because they are high-frequency (駅前, while semantically transparent, is common enough to merit an entry)
- **Productive patterns** (V + 始める, V + 過ぎる, V + 方) → the auxiliary/suffix gets its own entry documenting the pattern, but specific instances (食べ始める, 食べ過ぎる) typically do not unless they have idiomatic meanings

NINJAL's Compound Verb Lexicon (2,700+ entries) draws this boundary by including only "lexical" compounds (where V1-V2 combinations are restricted and meanings are somewhat unpredictable) and excluding "syntactic" compounds (where any V1 can combine with the V2 pattern).

### 4. Multi-word expressions

Idioms (猫の手も借りたい "so busy even a cat's paw would help"), fixed collocations (腕を磨く "to hone one's skills"), and grammatical patterns (〜なければならない "must") present the same scope question. Wiktionary applies an **idiomaticity test**: include it if "its full meaning cannot be easily derived from the meaning of its separate components." Learner dictionaries are generally more inclusive than this principle alone would suggest, because even semi-transparent expressions trip up learners who lack native-speaker collocational intuition.

### 5. Inflected forms as lookup keys

In Japanese, verbs inflect heavily (五段/一段 conjugation, て-form, ない-form, passive, causative, etc.), and learners often encounter inflected forms before knowing the dictionary form. A print dictionary can only list the citation form; a digital dictionary can index inflected forms and redirect to the lemma. je-dict-1's conjugation tables serve exactly this function: every conjugated form is stored in the entry JSON and indexed for search, so a learner who encounters 食べられない can find 食べる.

This is a major advantage of digital lemmatization over print. It effectively eliminates the lookup-failure problem that Tono (2001) identified as one of the main barriers to dictionary use.

## How je-dict-1 handles these decisions

### Current practice

| Decision point | je-dict-1 approach |
|---------------|-------------------|
| Citation form | Non-past plain form (verb/adj); bare noun; kana for grammar patterns |
| Suru-verbs | Combined entry (noun + verb-suru) |
| Orthographic variants | Single entry with `headword_alternatives` for alternate written forms |
| Compound verbs | Lexicalized compounds get entries; productive patterns documented under the V2 auxiliary |
| Derived forms | Each derivative gets its own entry if semantically distinct or high-frequency |
| Multi-word expressions | Idioms and fixed patterns get entries; transparent collocations go in the base word's notes |
| Inflected forms | Conjugation tables index all forms for search; only the citation form is the headword |

### Where this works well

The flat, one-entry-per-concept model suits a digital dictionary. There is no physical space constraint, so there is no penalty for giving even a transparent compound its own entry if it is useful. The search index handles inflected-form lookup automatically. The cross-reference system connects related entries without requiring physical nesting.

### Known tensions

1. **Scope creep in compound coverage**: With 27,000+ entries and no maximum, should every transparent compound get an entry? Entries like 駅前, 食べ方, and 国内線 are useful but borderline on non-inferability. The current practice is to include them if they appear as candidate words or are needed as cross-reference targets.

2. **Expression entries vs. notes**: Some "entries" are really grammatical patterns (なければならない, を巡って) that sit awkwardly in a word-level dictionary. They exist because learners look them up, but their scope and sense-division differ from lexical entries.

3. **Where to put collocational information**: A collocation like 腕を磨く could be an entry, a note in 腕, a note in 磨く, or all three. Currently je-dict-1 favors putting collocations in notes and creating entries only for truly lexicalized expressions.

## Implications for je-dict-1

1. **The non-inferability test is the right primary criterion**, but a digital learner dictionary should be more inclusive than it alone would suggest. High-frequency transparent compounds are worth including because they save the learner a mental composition step.

2. **Suru-verb combined entries are the right default.** The noun and verb are one conceptual unit for the learner. Only split when meanings have truly diverged.

3. **Productive suffix patterns** (〜方, 〜始める, 〜過ぎる) should be documented thoroughly in the suffix/auxiliary entry and not proliferated into hundreds of specific-combination entries unless the combination is lexicalized.

4. **Conjugation-based search eliminates the inflected-form problem** that plagued print JE dictionaries. This is one of je-dict-1's strongest structural advantages.

5. **The candidate pipeline should apply a lightweight non-inferability screen**: before adding a candidate, check whether its meaning is fully predictable from existing entries. This prevents the candidate queue from filling with transparent derivatives.

## Key references

- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press. — Chapters 6.4–6.5 on building and organizing the headword list.
- Bauer, L. & Nation, P. (1993). "Word families." *International Journal of Lexicography*, 6(4), 253–279.
- Halpern, J. (2010). "Headword Selection in Arabic Lexicography." CJK Dictionary Institute. — Discusses orthographic variation challenges shared with Japanese.
- Lehmann, C. (2024). "Lemma selection" and "Macrostructure." *Lexicography* (web resource). — Seven criteria for lemma inclusion including non-inferability.
- McLean, S. (2018). "Is the Lemma More Appropriate than the Flemma as a Word Counting Unit?" *Applied Linguistics*, 41(4), 601–622.
- Nation, I. S. P. (2001). *Learning Vocabulary in Another Language*. Cambridge University Press.
- Schmitt, N. (2010). *Researching Vocabulary: A Vocabulary Research Manual*. Palgrave Macmillan.
- Svensén, B. (2009). *A Handbook of Lexicography: The Theory and Practice of Dictionary-Making*. Cambridge University Press. — Chapter 5 on the lemma; Chapter 8 on morphological information.
- Tono, Y. (2001). *Research on Dictionary Use in the Context of Foreign Language Learning*. Max Niemeyer Verlag.

## Related pages

- [Word Formation and Morphology](word-formation.md) — compounding, derivation, and vocabulary strata
- [Compound Verb Representation](../topics/compound-verbs.md) — entry-vs-pattern decisions for V1+V2 compounds
- [Handling Words with Multiple Written Forms](../topics/word-variants.md) — orthographic variation policy
- [Multiword Expressions](multiword-expressions.md) — taxonomy, placement, and inclusion criteria
- [Vocabulary Size and Text Coverage](vocabulary-size-coverage.md) — word families vs. lemmas in size estimates
- [Dictionary Lookup Behavior](dictionary-lookup-behavior.md) — how users find entries
- [Controlled Defining Vocabulary](controlled-defining-vocabulary.md) — tier system as an analogue to CDV
- [Digital Dictionary UX](digital-dictionary-ux.md) — how digital format changes macrostructure constraints
- [Grammar Information in Learner Dictionaries](grammar-in-dictionaries.md) — conjugation tables and lookup
