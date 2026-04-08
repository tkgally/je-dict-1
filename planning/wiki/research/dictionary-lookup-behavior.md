# Dictionary Lookup Behavior

**Last updated**: 2026-04-08

## Overview

How learners actually use dictionaries — what they look up, what strategies they employ, what errors they make, and what information they extract — is central to designing an effective learner dictionary. Research on dictionary use behavior spans several decades and has evolved significantly with the shift from paper to digital dictionaries. Understanding these patterns helps je-dict-1 make better decisions about entry structure, search design, and information presentation.

## The lookup process model

Nesi (1999) proposed the most comprehensive taxonomy of dictionary skills, organized into stages that model the full consultation process. Lew (2013) later revised this for the electronic dictionary context. The stages are:

| Stage | Description | Key skills |
|-------|-------------|------------|
| **Before study** | Deciding which dictionary to use and understanding its conventions | Knowing dictionary types, evaluating quality |
| **Before consultation** | Deciding whether to look something up at all | Weighing lookup cost vs. benefit; using context clues first |
| **Locating information** | Finding the right entry and the right part of the entry | Lemmatization, choosing among homonyms, finding multi-word units |
| **Interpreting information** | Making sense of what the entry says | Distinguishing relevant from irrelevant information, reading codes and abbreviations |
| **Recording information** | Deciding what to note down and how | Selecting which information to retain, choosing format |

Lew (2013) notes that electronic dictionaries substantially change the balance between stages. The "locating" stage becomes easier (search replaces alphabetical scanning), but "interpreting" remains equally challenging — learners still struggle to select the right sense from a polysemous entry.

## Common lookup errors and difficulties

### Failure to lemmatize

One of the most documented lookup failures is attempting to look up an inflected form directly. Learners search for conjugated verbs, pluralized nouns, or derived forms without reducing them to the dictionary headword. This is particularly acute in Japanese, where verb and adjective conjugation is complex — a learner encountering 食べられなかった needs to recognize this as a form of 食べる before looking it up.

Electronic dictionaries can mitigate this through inflected-form search. The WWWJDIC system (Breen) demonstrated that inverse stemming can correctly identify inflected Japanese forms in over 95% of cases. je-dict-1 already stores full conjugation tables for verbs and i-adjectives, which could power similar functionality.

### Selecting the wrong sense

Atkins and Varantola (1997), in their foundational monitoring study of 71 dictionary users across 15 language communities, found that learners frequently select the first sense that seems plausible rather than reading through all available senses. This "first-fit" strategy is fast but error-prone, particularly for polysemous words.

Thumb (2004) found that Chinese university students using bilingualised dictionaries did scan all available senses, but this behavior was not universal — it correlated with proficiency level and task type. Lower-proficiency learners were more likely to stop at the first match.

### Ignoring context

Research consistently shows that learners often fail to consider the surrounding context when selecting a meaning from a dictionary entry. They look up a word, find a meaning that seems right in isolation, and apply it without checking whether it fits the original sentence. This is especially problematic with homographs and near-synonyms.

### Missing multi-word units

Learners tend to look up individual words rather than recognizing multi-word expressions, collocations, or fixed phrases. A learner encountering 気に入る might look up 気 and 入る separately rather than searching for the compound expression. Dictionary design can help by surfacing multi-word units prominently in search results.

### Underusing entry information

Tono's (2001) eye-tracking research on dictionary microstructure revealed that lookup processes are complex and interactive, influenced by the position of target information within the entry, the function of supporting devices (labels, examples), and the user's proficiency level. Crucially, learners often skip information that could help them — usage notes, example sentences, register labels — going straight for the gloss and ignoring everything else.

This aligns with Nesi's observation that learners treat dictionary consultation as a quick translation task rather than a learning opportunity. The implication is that the most carefully crafted usage notes are worthless if the entry layout doesn't guide the reader's eye to them.

## Paper vs. electronic dictionary behavior

The shift from paper to electronic dictionaries has changed lookup behavior in several ways:

### What changed

- **Speed**: Electronic lookups are dramatically faster, reducing the "cost" of consultation and encouraging more frequent lookups
- **Access structure**: Alphabetical scanning is replaced by search, eliminating the need for certain traditional skills (knowing alphabetical order, using guide words)
- **Inflected form handling**: Electronic dictionaries can match inflected forms to lemmas automatically
- **Cross-reference following**: Hyperlinks make it trivial to follow cross-references, whereas paper dictionary users rarely did so

### What didn't change

- **Sense selection difficulty**: Learners still struggle to pick the right meaning from multiple senses, regardless of format
- **Tendency to skip supplementary information**: Usage notes, examples, and labels are still underused
- **First-fit strategy**: The tendency to stop at the first plausible meaning persists in electronic contexts
- **Multi-word unit blindness**: Learners still tend to look up individual words rather than phrases

### New challenges

- **Over-reliance on search**: Learners may not develop the ability to browse or explore related entries, missing the serendipitous learning that comes from flipping through a paper dictionary
- **Shallow engagement**: The speed and ease of electronic lookup can reduce depth of processing, potentially harming retention (the "desirable difficulty" hypothesis suggests that some effort in lookup may aid memory)
- **Tab switching**: With dictionaries available in browser tabs or apps, learners are more likely to consult the dictionary briefly and return to their primary task, spending less time with each entry

## Japanese-specific lookup challenges

### The kanji barrier

Japanese presents unique lookup challenges because of its writing system. A learner encountering an unfamiliar kanji compound has multiple hurdles:

1. **Identifying the word boundaries** — Japanese text lacks spaces, so the learner must first segment the text correctly
2. **Determining the reading** — kanji typically have multiple on'yomi and kun'yomi readings; without knowing the reading, search is difficult
3. **Choosing the right homophone** — the CJK Dictionary Institute notes that common readings like こうき and きこう each represent approximately a dozen different words, distinguishable only by kanji

Traditional lookup methods (radical-based, stroke-count) are slow. The SKIP system (Halpern) classifies kanji by visual pattern, which is faster but still requires learning the system. Modern solutions include handwriting recognition, OCR on smartphone cameras, and copy-paste from digital text.

### Homograph density

Japanese has an unusually high density of homophones and homographs due to its small phoneme inventory. The word はし maps to 橋 (bridge), 箸 (chopsticks), and 端 (edge). The word かける maps to dozens of kanji combinations (掛ける, 欠ける, 架ける, 駆ける, etc.). This makes disambiguation a critical function of any Japanese dictionary — and a significant source of lookup errors.

### Kun-yomi synonyms

Many native Japanese (kun'yomi) homophones are near-synonymous, creating additional confusion. The readings for のぼる (上る, 登る, 昇る) all involve upward movement but with different nuances. Authors sometimes avoid making fine distinctions by writing such words in hiragana alone, which further complicates the learner's task of understanding when to use which kanji.

## Dictionary skills instruction

Research consistently supports the value of explicit dictionary skills training:

- Lew (2013) demonstrated that formal training measurably improves learner performance with dictionaries
- Studies in Hong Kong (tertiary level) and Poland (primary school) both showed that integrated dictionary skills instruction improved lookup accuracy and vocabulary retention
- The key teachable skills include: lemmatization, sense selection using context, reading example sentences, and interpreting usage labels

For a digital dictionary like je-dict-1, this suggests value in providing "how to use this dictionary" guidance, though the primary approach should be designing the interface so that effective behavior is the path of least resistance.

## Implications for je-dict-1

### Search design

- **Inflected form search** is a high-value feature. je-dict-1 already has conjugation data for verbs and i-adjectives; indexing these conjugated forms in the search index would catch a major category of lookup failures
- **Multi-word expression surfacing**: When a search query matches part of a multi-word expression entry, that entry should appear prominently in results
- **Disambiguation in results**: Search results for words with multiple entries (homographs) should show the reading and a brief gloss, not just the headword, to help users select the right entry before clicking through

### Entry layout

- **Front-loading the most useful information**: Since learners tend to grab the first plausible meaning and leave, the gloss and primary sense should be immediately visible. Detailed notes, collocations, and cross-references should be present but should not push the core meaning below the fold
- **Example sentences as disambiguation aids**: Examples are more effective than abstract definitions for helping learners select the correct sense. je-dict-1's practice of including 3+ examples per sense directly serves this function
- **Visual hierarchy**: Register labels, transitivity markers, and usage notes need clear visual styling so they register even during quick lookups. Information that is present but visually undifferentiated from surrounding text will be ignored

### Cross-references and browsing

- **Lowering the cost of following cross-references**: Electronic dictionaries make cross-reference following trivial, and je-dict-1's `prominent_see_also` field already supports this. Research suggests learners in electronic contexts are more willing to follow links than paper dictionary users were — so investing in cross-reference quality pays dividends
- **Compensating for lost browsing**: Paper dictionaries offered accidental discovery through adjacent entries. Digital dictionaries should provide alternative browsing paths — tag-based browsing, "related entries" sections, and semantic field groupings can serve this function

### Retention and engagement

- **Encouraging deeper engagement**: Features like example sentences, usage notes, and "similar words" sections give learners reasons to spend more time with each entry, potentially improving retention
- **Recording support**: Integration with SRS tools (see [Sentence Mining Integration](../ideas/sentence-mining.md)) would address the "recording" stage of the lookup process, helping learners capture and review dictionary information systematically

## Key references

- Atkins, B. T. S. & Varantola, K. (1997). Monitoring dictionary use. *International Journal of Lexicography*, 10(1), 1-45.
- Lew, R. (2004). *Which dictionary for whom? Receptive use of bilingual, monolingual and semi-bilingual dictionaries by Polish learners of English*. Motivex.
- Lew, R. (2013). From paper to electronic dictionaries: Evolving dictionary skills. In D. A. Kwary et al. (Eds.), *Lexicography and Dictionaries in the Information Age*. Airlangga University Press.
- Nesi, H. (1999). The specification of dictionary reference skills in higher education. In R. R. K. Hartmann (Ed.), *Dictionaries in Language Learning*. Thematic Network Project in the Area of Languages, Sub-project 9: Dictionaries.
- Thumb, J. (2004). *Dictionary Look-up Strategies and the Bilingualised Learner's Dictionary*. Max Niemeyer Verlag.
- Tono, Y. (2001). *Research on Dictionary Use in the Context of Foreign Language Learning*. Max Niemeyer Verlag.
- Halpern, J. (Ed.). *The Kodansha Kanji Learner's Dictionary*. Kodansha International.
- CJK Dictionary Institute. The complexities of Japanese homophones. Retrieved from cjki.org.

## Related pages

- [Digital Dictionary UX](digital-dictionary-ux.md) — interface design and current search architecture
- [Vocabulary Acquisition](vocabulary-acquisition.md) — how L2 learners acquire vocabulary
- [Learner Lexicography](learner-lexicography.md) — principles of pedagogical dictionary design
- [Handling Homographs](../topics/homographs.md) — disambiguation strategies for identical-writing words
- [Cross-Reference Design](../topics/cross-references.md) — linking related entries
- [Sentence Mining Integration](../ideas/sentence-mining.md) — SRS/Anki workflow integration
- [Example Sentence Design](example-sentences.md) — what makes effective dictionary examples
