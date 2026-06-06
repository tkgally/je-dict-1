# Japanese→Chinese Adaptation Brief

**Last updated**: 2026-06-06

## Overview

This is the **per-language adaptation brief for Chinese**, the first additional target
language in the [Multilingual Dictionary](../ideas/multilingual-dictionary.md) plan. Its
purpose is operational: it is the reference document handed to (a) the LLM translation
pipeline and (b) the native-speaker human advisor so they know, concretely and word-class by
word-class, where a Japanese→Chinese version must do *more* than translate the English notes —
where it must add, replace, or drop content because the learner's L1 is Chinese rather than
English.

The governing principle from the plan's anchor constraints is **"translate the universal
content, replace the L1-contrastive content."** The English notes already encode the
pedagogical decisions (sense splits, register warnings, collocations). Most of that is
universal and should simply be rendered into Chinese. But a Chinese-speaking learner arrives
with a *different set of prior beliefs* about Japanese than an English speaker does — beliefs
driven almost entirely by the **shared hanzi/kanji writing system** — and those beliefs are
where adaptation earns its keep.

This page expands the seed 同形異義語 table in
[§5 of the plan](../ideas/multilingual-dictionary.md#5-how-notes-adapt-per-target-language)
into a fuller, sourced reference. It builds directly on the research backbone in
[L1 Transfer in Japanese L2 Vocabulary](l1-transfer-japanese-vocabulary.md); read that first
for the theoretical framing (Jiang's three-stage model, cognate facilitation vs. false-friend
interference, the wago/kango/gairaigo transfer matrix).

> **Scope note.** This brief is a *plan artifact*, not an implementation. It describes what the
> Chinese notes should contain; it does not modify any entry, schema, or script.

## 1. The structural fact: kanji/hanzi overlap is the whole story

For an English speaker, Japanese orthography is opaque — kanji carry no prior meaning, and the
learner's only cognate bridge is gairaigo (katakana loanwords from English). For a Chinese
speaker the situation is inverted: **kanji are hanzi**, and an estimated 60–70% of the kanji in
Japanese newspaper text have recognizable Chinese counterparts (Koda 2005). This produces a
large receptive head start on Sino-Japanese vocabulary (kango) — and a correspondingly large
*interference* surface, because the learner's confidence in a character compound's meaning is
high even when it is wrong. The Japanese-pedagogy literature calls this the **"homograph
barrier"** (同形語の壁): the very resource that accelerates reading also installs systematic
false beliefs that resist correction (see the negative-transfer findings in Li et al. 2023 and
the lexical-processing literature on Chinese learners).

The adaptation brief is, therefore, mostly a catalogue of **where the hanzi bridge misleads.**

## 2. The 文化庁 S/O/D/N framework

The standard way to classify Japanese-Chinese homographs (日中同形語) comes from the Agency for
Cultural Affairs' *中国語と対応する漢語* (文化庁 1978, compiled by the Waseda University
Language Education Research Institute). It sorts shared two-character kango into four relations
with their Chinese look-alikes:

| Code | Name | Relation | Adaptation need |
|------|------|----------|-----------------|
| **S** | 同形同義語 | Same form, **same** meaning (学生, 図書館, 約束) | **None** — translate normally; the bridge helps |
| **O** | 同形類義語 | Same form, **overlapping/partial** meaning, often with register, scope, or connotation drift (情報, 検討, 結構) | **Subtle** — flag the divergence; the most under-noticed hazard |
| **D** | 同形異義語 | Same form, **different** meaning (手紙, 勉強, 大丈夫) | **High** — lead the Chinese note with the divergence |
| **N** | (欠落) | Exists in only one language, or is opaque across the boundary | Varies — usually treat as ordinary new vocabulary |

A textbook-based survey (≈2,000 words from elementary/intermediate Japanese textbooks) found S
words to be roughly **67%** of shared kango and O words roughly **4%**, i.e. the "safe-ish"
S+O band is around 70%, leaving a substantial minority of genuinely divergent (D) and
language-specific (N) items (文化庁 1978; figures vary by corpus and counting method). The
practical upshot for the pipeline:

- **S words are the silent majority** — the Chinese note can lean on the shared characters and
  needs no false-friend warning. Over-warning here would be noise.
- **D words are the headline cases** — relatively few, but high-impact and memorable; these are
  where the Chinese note must carry content the English note never had.
- **O words are the trap for an automated pipeline** — they *look* safe (the meanings
  "basically match"), so naive machine translation passes them through, but they carry register,
  frequency, or connotation differences that a Chinese learner will get subtly wrong. The
  advisor's time is best spent here and on D, not on S.

## 3. 同形異義語 (D): the false-friend table

These are the highest-value additions to the Chinese notes. For each, the Chinese learner's
prior belief (the Chinese meaning) is confidently wrong for Japanese. The Chinese note for these
words should **lead with the contrast** ("注意：与中文「X」意义不同"), not bury it. None of these
warnings appear in the English notes, because they are irrelevant to an English speaker — this
is the clearest case of "largely the same, plus a Chinese-only warning."

| Japanese (kanji) | Japanese meaning | Chinese look-alike | Chinese meaning |
|------------------|------------------|--------------------|-----------------|
| 勉強 | study; (also) discount | 勉强 (miǎnqiǎng) | reluctantly; to force; barely manage |
| 手紙 | letter (postal) | 手纸 (shǒuzhǐ) | toilet paper |
| 大丈夫 | all right; OK; safe | 大丈夫 (dàzhàngfu) | a real man; man of character |
| 丈夫 | sturdy; durable; healthy | 丈夫 (zhàngfu) | husband |
| 新聞 | newspaper | 新闻 (xīnwén) | news (reports) |
| 経理 | accounting; bookkeeping | 经理 (jīnglǐ) | manager |
| 愛人 | lover; mistress (illicit) | 爱人 (àirén) | spouse (husband or wife) |
| 汽車 | (steam) train | 汽车 (qìchē) | automobile; car |
| 人参 | carrot | 人参 (rénshēn) | ginseng |
| 階段 | stairs; staircase | 阶段 (jiēduàn) | phase; stage |
| 天井 | ceiling | 天井 (tiānjǐng) | courtyard; skywell |
| 文句 | complaint; grumble | 文句 (wénjù) | wording; phrasing of a text |
| 怪我 | injury (ケガ) | 怪我 (guài wǒ) | "blame me"; my fault |
| 約束 | promise; appointment | 约束 (yuēshù) | to restrict; to bind |
| 結構 | fine; quite; "no thank you" | 结构 (jiégòu) | structure |
| 検討 | examination; consideration | 检讨 (jiǎntǎo) | self-criticism; (self-)review |
| 娘 | daughter; young woman | 娘 (niáng) | mother; ma |
| 湯 | hot water; bath | 汤 (tāng) | soup |
| 先生 | teacher; doctor | 先生 (xiānsheng) | Mr.; sir |
| 私 | I; me | 私 (sī) | private; personal; selfish |

Sources for the pairs: the homograph-pedagogy literature (文化庁 1978; Li et al. 2023) plus the
curated reference lists at Wiktionary's *Appendix: False friends between Chinese and Japanese*
and the Wikipedia *List of Chinese–Japanese false friends*, cross-checked against the worked
examples in Fordham (2017). Each pair should still be advisor-verified before shipping, because
some (e.g. 結構, 文句) are polysemous and the "false" sense is only one reading.

### Two sub-patterns worth special handling

- **Reading interference (phonological, not semantic).** Even for S words where the meaning
  matches, the *reading* does not: 人 is *rén* in Mandarin but ひと／じん／にん in Japanese.
  Chinese learners must actively suppress hanzi pronunciations (Koda 2005; Mori 1998 found L1
  phonology measurably slows cognate recognition). je-dict-1's furigana policy already supplies
  the Japanese reading on every kanji, so the Chinese note rarely needs to *say* this — but for
  high-frequency S words the note can lean on the shared character meaning while letting furigana
  carry the (unrelated) reading. **Do not** add per-word "the reading is different from Mandarin"
  boilerplate; furigana makes it redundant.
- **The 〜的 register/POS gap.** Mandarin 的 (de) is an all-purpose modifier marker; Japanese 的
  attaches to a restricted set of kango to form na/no-adjectives. This mismatch drives a
  documented production error — see [§5](#5-l1-specific-common-mistakes).

## 4. 同形類義語 (O) and calque pitfalls: the productive-error layer

D words mostly cause *comprehension* errors (the learner misreads Japanese). O words and calques
mostly cause *production* errors (the learner writes/speaks bad Japanese by back-translating from
Chinese). Because je-dict-1 aspires to be a production-support (encoding) dictionary, not just a
decoding one (see [Productive Vocabulary and Encoding Support](productive-vocabulary-encoding.md)),
these matter.

### Partial-overlap (O) drift to flag

- **Scope narrowing/widening.** 情報 in Japanese is everyday "information"; 情报 in Chinese
  skews toward "intelligence" (espionage). A Chinese learner under-uses 情報 for ordinary
  information.
- **Register/frequency drift.** Many O pairs share a core meaning but sit at different
  frequencies or registers in the two languages — a word that is neutral and common in Chinese
  may be stiff or literary in Japanese, or vice versa. These are exactly the cases a fluent
  Chinese-reading translation model will wave through. The O-word notes should say "用法/语感与
  中文略有不同" and give the Japanese collocational range.
- **Connotation flip.** 検討 (neutral "examine/consider") vs. 检讨 (self-critical "review one's
  faults") is an O/D borderline where the connotation, not the denotation, is the trap.

### Calque pitfalls (Sino-Chinese → Japanese)

Chinese learners productively coin Japanese-looking compounds by mapping Chinese two-character
words onto kanji. Some land on a real Japanese word with a *different* meaning (the D table
above, used in reverse: a learner writes 愛人 intending "spouse"); others land on a compound that
**does not exist** in Japanese or is markedly less idiomatic. The Chinese `common_mistakes`
content should pre-empt the high-frequency ones:

- Using 汽車 for "car" (should be 車／自動車), 愛人 for "spouse" (should be 妻／夫／配偶者),
  手紙 for "toilet paper" (should be トイレットペーパー).
- Coining kango that is grammatical Chinese but non-idiomatic Japanese, where Japanese prefers a
  wago verb or a different compound. The translation pipeline cannot enumerate all of these per
  entry, but the *advisor* can flag the recurrent ones for the highest-frequency entries.

### Part-of-speech mismatch

A shared two-character compound can be the same meaning but a **different word class** in the two
languages — e.g. usable as a verb directly in Chinese but only as a noun (requiring する) in
Japanese, or differing in whether it takes 的 to modify a noun. The POS correspondence of
Japanese-Chinese homographs has been studied quantitatively (熊・玉岡 2014); the practical point
for the brief is that the **invariant POS tag is correct for Japanese**, and the Chinese note
should not let the learner assume the Chinese word class transfers. This is a frequent source of
"missing する," "extra 的," and transitivity errors.

## 5. L1-specific common mistakes

The `common_mistakes` field is, per the plan, **fully L1-specific** — it must be *replaced*,
not translated, for each L1. The English-oriented mistake notes (which often target article use,
or English-specific particle confusions) are simply wrong for a Chinese learner. Documented
Chinese-L1 error patterns to seed the replacement content:

- **の overgeneralization from 的.** Chinese learners over-insert の in noun-modifying positions
  by transfer from the all-purpose Mandarin modifier 的. Chan (2014) found Chinese-L1 learners
  performed significantly worse than Korean- and English-L1 learners at rejecting misused の,
  specifically in the verbal-modifier category, and attributed this to negative transfer from 的.
  The Chinese notes on adjectives and verbal modifiers are the right place to warn against
  「形容詞＋の＋名詞」 overuse.
- **Transitivity-pair confusion.** Japanese morphologically distinguishes self-/other-movement
  verb pairs (開く／開ける, 始まる／始める); Mandarin does not encode this contrast the same way
  and leans on word order and 把. Chinese learners under-use the distinction. je-dict-1 already
  documents transitivity richly (see [Verb Transitivity Pairs](../topics/verb-transitivity.md));
  the Chinese version should keep that scaffolding and can lean on it *more* than the English
  version does, since the contrast is a known Chinese-L1 weak point.
- **Reading errors on cognates.** Producing an on'yomi by guessing from Mandarin phonology, or
  defaulting to the wrong on'yomi/kun'yomi split — a direct consequence of the homograph barrier.
- **Register over-formality.** Because kango feels "default" to a hanzi reader, Chinese learners
  can over-produce stiff Sino-Japanese vocabulary where a wago word is more natural — the mirror
  image of the English learner's gairaigo over-reliance.

The acquisition literature confirms that particle error profiles differ by L1 (Korean > English
> Chinese for case-marker difficulty; see
[Japanese Particles in L2 Acquisition](japanese-particles-l2.md)), which is the empirical reason
the field treats per-L1 mistake notes as non-interchangeable.

## 6. What to drop from the English notes

Adaptation is subtractive as well as additive. Content that earns its place for an English
reader is dead weight — or actively patronizing — for a Chinese reader:

| Content in the English note | Chinese treatment |
|-----------------------------|-------------------|
| Gairaigo false-friend warnings (マンション ≠ "mansion", ナイーブ ≠ "naive") | **Lower priority / often drop.** These loanwords are from English, so the warning is English-specific. A Chinese learner who doesn't know the English source word doesn't have the false belief. Keep only where the loanword is genuinely common. |
| Per-character morphemic gloss of kango (図書館 = "diagram + book + building") | **Usually drop.** A hanzi reader already parses the compound natively; spelling it out is redundant. The English note needs it to build the compound-inferencing strategy English speakers lack (see [Lexical Inferencing](lexical-inferencing.md)); the Chinese reader has it for free. |
| "Like the English word X / unlike English Y" framings | **Replace, do not translate.** A literal 「像英语单词…」 is useless to a Chinese learner. Detect these and rewrite against Chinese, or cut them. (Flagged as a specific risk in the plan's [§10](../ideas/multilingual-dictionary.md#10-open-questions-and-risks).) |
| English-specific article/countability notes | **Drop.** Mandarin lacks articles too, but for different reasons; the English-framed note doesn't transfer. |

What to **keep unchanged**: the core semantic explanation, the embedded Japanese collocations and
type-lists (preserved byte-for-byte with their furigana and `⟦…⟧` links), cultural/encyclopedic
background (with framing tweaks), and most register/keigo guidance (largely universal — see
[Keigo: Honorific Language](keigo-honorifics.md)).

## 7. Simplified vs. traditional (zh-Hans / zh-Hant)

This brief is written script-neutrally on purpose. The false-friend *phenomena* are the same for
mainland and Taiwan learners, but the **rendering** is not: the Chinese glosses above appear here
in simplified, and several diverge in traditional (经理→經理, 检讨→檢討) and in vocabulary norms
(软件/軟體, 信息/資訊).

**The script question is now resolved: Simplified Chinese (`zh-Hans`) ships first**, because the
native-speaker advisor works in simplified script and Putonghua norms (curator decision, 2026-06).
The simplified glosses in the tables above are therefore the live form. Traditional (`zh-Hant`) is
deferred; when it ships it will be **seeded by assisted conversion + human review** (OpenCC
`s2twp`, which handles both the one-to-many character merges and the 软件→軟體 vocabulary norms),
**not** mechanical character substitution. The adaptation *content* in this brief is shared across
both variants — which is exactly why keeping it script-neutral pays off: `zh-Hant` inherits all
the editorial decisions and pays only for surface conversion plus a lighter review. The full
worked design is in
[Chinese Simplified/Traditional Handling](../topics/chinese-simplified-traditional.md).

## How the pipeline should consume this brief

Mapping back to the [translation pipeline](../ideas/multilingual-dictionary.md#4-how-the-ai-translation-should-be-done):

1. **Hand this brief to the model as the per-language adaptation context** alongside the Japanese
   entry and the English fields, exactly as §4 of the plan prescribes.
2. **Pre-flag D-table and O-table entries.** A simple headword match against the tables here lets
   the pipeline route those entries to the higher-quality (deep/advisor) pass, since they are the
   ones that need *added* Chinese-only content rather than straight translation.
3. **Replace `common_mistakes` wholesale** for Chinese; do not translate the English version.
4. **Run the "English-contrast detector"** ([§10](../ideas/multilingual-dictionary.md#10-open-questions-and-risks))
   to catch "like the English word…" framings for rewrite-or-cut.
5. **Prioritize the advisor's time** on the O-band (subtle, easy for the model to miss) and the
   D-band (high-impact), not on the S-majority that translates cleanly.

This brief is the per-language analogue of `reviews/calibration_report.md`: a living document the
advisor and the pipeline both read from, expanded as the calibration sample surfaces new
recurrent patterns.

## Implications for je-dict-1

- The Chinese version is **not** a translation of the English version for the D and O word
  classes — it carries content the English version never had (false-friend warnings) and drops
  content the English version needs (morphemic glosses, gairaigo warnings). This is the concrete
  meaning of the curator's "largely the same, with targeted adaptation."
- The single highest-leverage Chinese-specific feature is the **同形異義語 lead-with-the-contrast
  warning** on the D-table words. It is cheap (a finite list), high-impact (memorable, frequent
  errors), and invisible to the English pipeline.
- The brief gives the pipeline a **routing signal**: headword ∈ D/O tables → deep/advisor pass;
  otherwise → bulk pass. That makes the advisor's scarce time scale.
- Everything here is reusable in shape for later languages: Korean gets its own brief
  (Sino-Korean correspondences, fewer false friends, closer grammar), Vietnamese its own
  (Hán-Việt partial cognates without the character bridge). The *structure* — S/O/D/N triage,
  L1-specific mistakes, what-to-drop table — generalizes; only the contents change.

## Related pages

- [Multilingual Dictionary](../ideas/multilingual-dictionary.md) — the hub plan this brief serves; see §5 (note adaptation) and §4 (pipeline)
- [Chinese Simplified/Traditional Handling](../topics/chinese-simplified-traditional.md) — the script-variant design that consumes this (script-neutral) brief: simplified-first decision, OpenCC-seed path for traditional
- [Translation Sidecar Design](../ideas/translation-sidecar-design.md) — how the pipeline consumes this brief as a routing signal (D/O headwords → deep/advisor pass) and preserves the *added* false-friend Japanese fragments
- [LLM Translation Quality for Japanese Language Pairs](llm-translation-quality-japanese-pairs.md) — the MT-eval evidence that the false friends this brief targets are exactly where LLMs are weakest, justifying the deep/advisor routing
- [Japanese-Learner Demand by L1](japanese-learner-demand-by-l1.md) — the demand data (JF 2021) that makes Chinese the highest-priority first language
- [L1 Transfer in Japanese L2 Vocabulary](l1-transfer-japanese-vocabulary.md) — the research backbone (Jiang's model, the wago/kango/gairaigo transfer matrix, the seed false-friend table)
- [Gairaigo: Loanwords in Japanese](gairaigo-loanwords.md) — the English-side false friends this brief mostly *drops* for Chinese
- [Japanese Particles in L2 Acquisition](japanese-particles-l2.md) — why `common_mistakes` are L1-specific (の/的 transfer, case-marker difficulty by L1)
- [Verb Transitivity Pairs](../topics/verb-transitivity.md) — the transitivity scaffolding Chinese learners lean on more than English learners
- [Productive Vocabulary and Encoding Support](productive-vocabulary-encoding.md) — why production (calque) errors matter for an encoding dictionary
- [Lexical Inferencing and Guessing from Context](lexical-inferencing.md) — the compound-inferencing strategy Chinese readers already have (so the morphemic gloss is droppable)
- [Cultural Content in Bilingual Dictionaries](cultural-content-dictionaries.md) — encyclopedic content whose framing shifts by audience

## References

- 文化庁 (1978). 『中国語と対応する漢語』. 早稲田大学語学教育研究所編. (The S/O/D/N classification of Japanese-Chinese homographs.)
- 熊可欣・玉岡賀津雄 (2014). 「日中同形二字漢字語の品詞性の対応関係に関する考察」. 『ことばの科学』27. (Part-of-speech correspondence between Japanese-Chinese homographs.)
- Chan, S. (2014). The Effects of Prior Language Knowledge in Japanese Acquisition as a Foreign Language: The Case of the Japanese Noun Modifier No. *New Voices in Japanese Studies*, 6, 27–50. doi:10.21159/nv.06.02. (の overgeneralization from Chinese 的.)
- Koda, K. (2005). *Insights into Second Language Reading: A Cross-Linguistic Approach*. Cambridge University Press. (Kanji/hanzi overlap proportions; L1 phonological suppression.)
- Li, X., Wang, J., & Chen, L. (2023). The lexical processing of Japanese collocations by Chinese Japanese-as-a-Foreign-Language learners. *Frontiers in Psychology*, 14, 1142411. (Translational congruency and negative transfer.)
- Mori, Y. (1998). Effects of first language and phonological accessibility on kanji recognition. *Modern Language Journal*, 82(1), 69–82.
- Fordham, C. G. (2017). "35 Common False Friends in Chinese and Japanese." carlgene.com. (Curated false-friend list, advisor-verifiable.)
- *Appendix: False friends between Chinese and Japanese*, Wiktionary; *List of Chinese–Japanese false friends*, Wikipedia. (Reference lists for the pairs, not primary research.)
