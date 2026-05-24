# Near-Synonym Discrimination in Learner Dictionaries

**Last updated**: 2026-05-12

## Overview

Near-synonyms — words that share a core meaning but differ in nuance, register, collocation, connotation, or grammatical behavior — are one of the most persistent challenges for L2 learners. Dictionaries routinely define near-synonyms with overlapping glosses, leaving learners unable to choose between them in production. The problem is especially acute in Japanese, where the three-stratum vocabulary system (wago/kango/gairaigo) generates systematic near-synonym pairs with register and collocational differences that resist simple explanation.

This page surveys the research on how near-synonyms differ, why learners struggle with them, how dictionaries have tried to help, and what this means for je-dict-1's SIMILAR WORDS sections.

## What makes near-synonyms different from each other

### Dimensions of difference

Inkpen and Hirst (2002, 2006) formalized the dimensions along which near-synonyms diverge in their work on a computational knowledge base of synonym differences. Building on earlier lexicographic tradition — particularly Hayakawa's *Choose the Right Word* (1968) and the synonym essays in Webster's New Dictionary of Synonyms — they identified these recurring axes:

| Dimension | Example (English) | Example (Japanese) |
|-----------|-------------------|---------------------|
| **Denotational scope** | *error* (general) vs. *blunder* (serious, careless) | {間違い\|まちがい} (general) vs. {過ち\|あやまち} (serious, moral) |
| **Register/formality** | *commence* vs. *begin* vs. *start* | {開始\|かいし}する (formal) vs. {始\|はじ}める (neutral) vs. {始\|はじ}まる (intransitive) |
| **Connotation/attitude** | *thrifty* (+) vs. *stingy* (−) | {倹約\|けんやく} (admirable) vs. けち (pejorative) |
| **Collocation** | *strong tea* vs. *powerful engine* (not *\*powerful tea*) | {濃\|こ}い (tea, flavor) vs. {強\|つよ}い (force, wind) |
| **Semantic prosody** | *cause* (typically negative) vs. *bring about* (neutral) | ～てしまう (regrettable nuance) vs. ～おわる (neutral completion) |
| **Syntactic pattern** | *big* (attributive) vs. *great* (attributive + exclamative) | {大\|おお}きい (predicative + attributive) vs. {大\|おお}きな (attributive only) |
| **Geographic/social** | *lift* (BrE) vs. *elevator* (AmE) | {じゃがいも} vs. {馬鈴薯\|ばれいしょ} (written/technical) |

Cruse (1986) distinguished *cognitive synonyms* (same truth-conditional meaning in any context) from *plesionyms* (near-synonyms: same propositional meaning but diverging in expressive, evocative, or collocational properties). True cognitive synonymy is vanishingly rare; nearly all "synonyms" are in fact plesionyms, and the lexicographer's task is to make the plesionymic differences visible.

### The collocational dimension as primary discriminator

Corpus-based research has converged on collocation as the most reliable and teachable dimension for synonym discrimination. Kamiński (2017) demonstrated that collocational preferences can be visualized for sets of near-synonyms using correspondence analysis plots and collocational networks derived from Sketch Engine, making differences visible in ways that prose descriptions struggle to convey. Liu (2010) showed that behavioral profiles — multidimensional collocational portraits — reveal distinctions between near-synonymous adjectives (*chief*, *main*, *major*, *primary*, *principal*) that dictionaries typically obscure with interchangeable glosses.

Xiao and McEnery (2006) established that near-synonyms sharing denotational meaning almost always diverge in semantic prosody — the evaluative colouring they acquire through habitual collocational partners. This prosodic dimension is particularly treacherous for learners because it is invisible in decontextualized definitions. See [Semantic Prosody](semantic-prosody.md) for the full treatment.

## Why learners struggle with near-synonyms

### The synonym avoidance / overuse pattern

Laufer (1990) identified near-synonymy as a significant source of L2 vocabulary difficulty. She argued that gaining *full* knowledge of a synonym — including its collocational restrictions, register constraints, and connotative properties — is harder than initial or partial vocabulary learning. Learners who have learned two near-synonymous words often default to the one acquired first ("ease of activation"), overusing it and avoiding the other, even in contexts where the avoided word would be more natural.

This manifests in two observable error patterns:
1. **Overuse**: A learner defaults to 見る for all visual perception, avoiding 眺める (gaze), 見つめる (stare), 覗く (peek), and 観る (watch performances)
2. **Underdifferentiation**: A learner treats 聞く and 聴く as interchangeable, not recognizing that 聴く implies deliberate, attentive listening

### Dictionary lookup doesn't solve it

Ahmadian and Farahani (2023) tested whether bilingualized dictionaries help learners discriminate near-synonyms in a fill-in-the-blank task. Their experiment with 156 participants found that the bilingualized dictionary was no more useful than a monolingual one for this task — both dictionary types gave insufficient information about the collocational and contextual constraints that govern synonym choice. The problem is not access to definitions but the *quality and specificity* of the discriminating information.

This echoes Nesi and Haill's (2002) broader finding that learners struggle to extract pragmatic and collocational information from dictionary entries, even when it is technically present. See [Dictionary Lookup Behavior](dictionary-lookup-behavior.md) for the research on how learners use (and fail to use) dictionary information.

### Japanese-specific complications

Japanese near-synonym difficulty is compounded by the three-stratum vocabulary system:

**Stratal register pairs.** A wago word and its kango equivalent typically differ in register, collocational range, and sometimes denotational scope — but bilingual glosses often map both to the same English word. Examples:

| Wago | Kango | Shared gloss | Key difference |
|------|-------|-------------|----------------|
| {始\|はじ}める | {開始\|かいし}する | to begin | kango is formal, used in announcements and written language |
| {変\|か}わる | {変化\|へんか}する | to change | kango implies gradual/systematic change; wago is broader |
| {助\|たす}ける | {援助\|えんじょ}する | to help | kango implies organized/institutional aid |
| {選\|えら}ぶ | {選択\|せんたく}する | to choose | kango implies deliberate selection from defined options |
| {壊\|こわ}す | {破壊\|はかい}する | to destroy | kango implies large-scale or systematic destruction |

**Three-way stratal competition.** When gairaigo enters the picture, learners face three-way distinctions: {手伝い\|てつだい} (wago, personal help) vs. {援助\|えんじょ} (kango, institutional aid) vs. サポート (gairaigo, modern/business support). See [Gairaigo: Loanwords in Japanese](gairaigo-loanwords.md) for the acquisition dynamics.

**Transitivity-linked pairs.** Japanese has extensive transitive/intransitive verb pairs ({開\|あ}ける/{開\|あ}く, {決\|き}める/{決\|き}まる) where the English translation is identical ("open", "decide") but the Japanese forms are not synonyms at all — they encode different agency structures. Learners who approach these as synonyms produce fundamental errors. See [Verb Transitivity Pairs](../topics/verb-transitivity.md).

**Politeness-linked variants.** Keigo creates synonym-like relationships where the distinction is purely social: {食\|た}べる / {召\|め}し{上\|あ}がる / いただく all mean "eat" but encode different social positionings. See [Keigo: Honorific Language](keigo-honorifics.md).

## Dictionary presentation strategies

### The synonym essay tradition

The oldest approach is the **synonym discrimination essay** — a prose paragraph or panel that contrasts a cluster of near-synonyms, explaining how each differs. This tradition runs from Crabb's *English Synonymes Explained* (1816) through Hayakawa's *Choose the Right Word* (1968) to modern learner dictionary "Word Choice" boxes.

**Strengths**: Can convey subtle distinctions, provide context, and explain the *why* behind differences.
**Weaknesses**: Long prose is rarely consulted by learners (the "consultation gap" documented by Nesi & Haill 2002); assumes the learner knows to look; and scales poorly to large synonym sets.

### Feature comparison tables

An alternative is the **structured comparison table** that aligns near-synonyms along explicit dimensions (register, collocation, connotation, typical context). This approach is more scannable than prose and makes the discriminating dimensions explicit.

The Longman Language Activator (1993) organized vocabulary by communicative function rather than alphabetically, presenting near-synonyms grouped under meanings with explicit usage labels and example sentences — effectively a production-oriented synonym discrimination tool.

### Contrastive examples

A third strategy is **paired minimal examples** — sentences that are identical except for the near-synonym, making the usage difference concrete:

- ✓ {濃\|こ}いお{茶\|ちゃ} (strong tea) — {濃\|こ}い describes flavor intensity
- ✗ {強\|つよ}いお{茶\|ちゃ} — {強\|つよ}い is for physical/abstract force, not flavor

This approach has the strongest empirical support for retention: Frankenberg-Garcia (2012, 2015) showed that "encoding examples" — examples specifically designed to illustrate a grammatical or collocational distinction — are more effective for learning than authentic corpus examples or dictionary definitions alone. See [Example Sentence Design](example-sentences.md).

### Corpus-driven visualizations

Kamiński (2017) proposed a fourth approach: visual representations of collocational profiles (correspondence analysis plots, collocational networks) that show at a glance which collocates cluster with which synonym. While this is impractical for a traditional dictionary, digital formats can support interactive exploration of collocational profiles.

## Treatment in major dictionaries

### English learner dictionaries

The Big Four English learner dictionaries have developed distinct approaches:

| Dictionary | Feature | Format |
|-----------|---------|--------|
| **OALD** | "Which Word?" boxes | Prose panel comparing 3–6 synonyms with examples; appears at the entry for the most common word in the set |
| **LDOCE** | "Word Choice" boxes | Tabular comparison with register labels and contrastive examples |
| **COBUILD** | Full-sentence definitions + "Word Partnership" boxes | Definitions embed collocational context; partnership boxes show common combinations |
| **MED** | "Thesaurus" boxes | Cross-references to synonym groups with brief usage notes |

All four place synonym discrimination information at the entry for one member of the set (usually the most frequent), with cross-references from the others. This means a learner looking up the less common synonym must follow a link to find the discrimination panel — an extra step that many learners skip (Tono 2001).

### Japanese-English dictionaries

JMdict/Jisho.org provides no synonym discrimination. Kenkyusha's fifth edition includes occasional synonym notes (類語) but they are unsystematic. The Wisdom JE dictionary (Sanseidō) has "Communication" boxes comparing related expressions but these focus on pragmatic functions rather than lexical synonymy.

Dedicated Japanese synonym discrimination resources exist in Japanese: Morita Yoshiyuki's (森田良行) work on synonym expressions and the various 使い分け (tsukaiiwake, "usage distinction") guides aimed at native speakers and advanced learners. These resources are comprehensive but Japanese-only, making them inaccessible to the English-speaking intermediate learner that je-dict-1 targets.

## Implications for je-dict-1

### Current state

je-dict-1 has a SIMILAR WORDS section in entry notes, typically structured as a bulleted list of near-synonyms with one-sentence explanations of the difference. This is present in many entries but coverage is uneven — older entries often lack it, and the discriminating information varies in specificity. Cross-references (both `cross_references` and `prominent_see_also`) provide navigational links but carry no discriminating content themselves.

### Recommendations

**1. Make the discriminating dimension explicit.** Each SIMILAR WORDS bullet should name the axis of difference: "Register: {開始\|かいし}する is formal/written" rather than just "{開始\|かいし}する is similar." The research consistently shows that learners need the *dimension* of difference, not just the fact of difference.

**2. Prioritize collocational evidence.** Following Kamiński (2017) and Liu (2010), collocation is the most reliable and teachable discriminator. SIMILAR WORDS bullets should include representative collocations where possible: "Used with flavors: {濃\|こ}いコーヒー, {濃\|こ}い{味\|あじ} — compare {強\|つよ}い, which is used with forces: {強\|つよ}い{風\|かぜ}, {強\|つよ}い{力\|ちから}."

**3. Design contrastive examples.** Following Frankenberg-Garcia's encoding-examples research, example sentences in SIMILAR WORDS sections should be designed to illustrate the *contrast*, not just the individual word. A pair of sentences differing only in the near-synonym — one natural, one marked as unnatural or register-inappropriate — is maximally informative.

**4. Flag stratal register systematically.** Every entry for a kango word that has a wago near-synonym (and vice versa) should note the stratal relationship and its register implication. This is the single most productive source of near-synonym confusion for Japanese learners and the one most amenable to systematic treatment. The existing register and vocabulary-strata information in notes often exists but is not structured consistently.

**5. Use bidirectional discrimination.** Following OALD's model, place the discrimination panel at the most common word in the set, but ensure that every other member of the set has a cross-reference that carries enough information for the learner to decide whether to follow the link. A cross-reference saying "See also {始\|はじ}める" is less useful than "See also {始\|はじ}める (neutral register equivalent)."

**6. Consider polishing-task scoping.** A dedicated "synonym discrimination" polishing task that walks through entries with SIMILAR WORDS sections — checking for named dimensions, collocational evidence, contrastive examples, and bidirectional links — would be a natural addition to the polishing infrastructure. It could draw on the note quality scorer to identify entries with thin or missing synonym notes.

### Priority clusters for synonym discrimination work

Based on the research, the highest-value synonym clusters for Japanese learners are:

1. **Wago/kango stratal pairs** — hundreds of these exist in the dictionary; the register distinction is the most systematic and teachable
2. **Visual perception verbs** — 見る/眺める/見つめる/覗く/観る/拝見する (5–6 way distinctions, high frequency)
3. **Thinking/knowing verbs** — 思う/考える/感じる/信じる (distinct in degree of deliberation and certainty)
4. **Speaking verbs** — 言う/話す/述べる/伝える/告げる/おっしゃる (frequency, register, directionality)
5. **Movement verbs** — 行く/向かう/参る/伺う (direction, register, keigo layer)
6. **Giving/receiving verbs** — あげる/くれる/もらう/差し上げる/いただく (directional benefactive + keigo)

## Related pages

- [Sense Relations and Semantic Networks](sense-relations-semantic-networks.md) — the broader taxonomy of paradigmatic relations (synonymy is one type)
- [Semantic Prosody](semantic-prosody.md) — how evaluative colouring distinguishes near-synonyms
- [Translation Equivalence](translation-equivalence.md) — the bilingual mapping problem, of which near-synonymy is a special case
- [Definition and Gloss Strategies](definition-strategies.md) — how glosses inadvertently obscure synonym differences
- [Collocations in Learner Dictionaries](collocations.md) — collocational evidence as a discriminating tool
- [Register and Formality Marking](register-formality-marking.md) — register as a dimension of synonym difference
- [Gairaigo: Loanwords in Japanese](gairaigo-loanwords.md) — the third stratum in three-way synonym competition
- [Keigo: Honorific Language](keigo-honorifics.md) — politeness-linked synonym variants
- [Verb Transitivity Pairs](../topics/verb-transitivity.md) — transitivity pairs that look like synonyms to learners
- [Example Sentence Design](example-sentences.md) — encoding examples for teaching synonym distinctions
- [Dictionary Lookup Behavior](dictionary-lookup-behavior.md) — why learners fail to extract discrimination information
- [Vocabulary Learning Strategies](vocabulary-learning-strategies.md) — how synonym knowledge fits into broader VLS taxonomies
- [L1 Transfer in Japanese L2 Vocabulary](l1-transfer-japanese-vocabulary.md) — why English speakers confuse wago near-synonyms that map to a single English word
- [Productive Vocabulary and Encoding Support](productive-vocabulary-encoding.md) — near-synonym discrimination as a quintessential encoding task

## References

- Ahmadian, M., & Farahani, E. (2023). How useful are bilingualized dictionaries in discriminating between near-synonyms? *International Journal of Lexicography*, 36(4), 486–509.
- Atkins, B. T. S., & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Crabb, G. (1816). *English Synonymes Explained*. Baldwin, Cradock, and Joy.
- Cruse, D. A. (1986). *Lexical Semantics*. Cambridge University Press.
- Frankenberg-Garcia, A. (2012). Raising teachers' awareness of corpora. *Language Teaching*, 45(4), 475–489.
- Frankenberg-Garcia, A. (2015). Dictionaries and encoding examples to support language production. *International Journal of Lexicography*, 28(4), 490–512.
- Hayakawa, S. I. (1968). *Choose the Right Word: A Modern Guide to Synonyms*. Harper & Row.
- Inkpen, D., & Hirst, G. (2002). Near-synonymy and lexical choice. *Computational Linguistics*, 28(2), 105–144.
- Inkpen, D., & Hirst, G. (2006). Building and using a lexical knowledge base of near-synonym differences. *Computational Linguistics*, 32(2), 223–262.
- Kamiński, M. (2017). Visualisation of collocational preferences for near-synonym discrimination. *Lexikos*, 27, 237–251.
- Laufer, B. (1990). Ease and difficulty in vocabulary learning: Some teaching implications. *Foreign Language Annals*, 23(2), 147–155.
- Liu, D. (2010). Is it a chief, main, major, primary, or principal concern? A corpus-based behavioral profile study of the near-synonyms. *International Journal of Corpus Linguistics*, 15(1), 56–87.
- Nesi, H., & Haill, R. (2002). A study of dictionary use by international students at a British university. *International Journal of Lexicography*, 15(4), 277–305.
- Summers, D. (Ed.). (1993). *Longman Language Activator*. Longman.
- Tono, Y. (2001). *Research on Dictionary Use in the Context of Foreign Language Learning*. Niemeyer.
- Xiao, R., & McEnery, T. (2006). Collocation, semantic prosody, and near synonymy: A cross-linguistic perspective. *Applied Linguistics*, 27(1), 103–129.
