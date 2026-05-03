# Knowledge Base Log

Chronological record of wiki maintenance sessions. Each entry records what was done.

## [2026-05-03] maintenance | Register and formality marking research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **register and formality marking in learner dictionaries** and created `research/register-formality-marking.md`. Covers Hausmann's (1989) diasystematic label taxonomy (diachronic, diatopic, diastratic, diaphasic, diatechnical, diafrequential, diaconnotative, dianormative, diaintegrative); comparative label inventories across the Big Four English learner dictionaries (OALD ~17 labels, LDOCE ~12, COBUILD ~10, MED ~13), noting that "formal"/"informal" are the only consistent labels; the consistency problem (Ojo 2011 on five dictionaries assigning five different labels to the same word); the consultation gap (Nesi & Haill 2002, Tono 2001, Vrbinc & Vrbinc 2015 showing learners largely ignore metalinguistic labels); the bilingual gap (register asymmetry in translation equivalents); Japanese-specific register dimensions including the stratal system (wago everyday → kango formal/written → gairaigo modern/technical) and the keigo axis (sonkeigo/kenjōgo/teineigo); Ide's (1989) wakimae ("discernment") model of sociopragmatically obligatory register selection; JMdict's comprehensive entity code system for register (hon/hum/pol/fam/col/sl/vulg/arch/obs plus gender and dialect codes); Maebo's (2012) finding that Japanese learner and native-speaker dictionaries use different label sets from different perspectives and that synonym-in-context presentation is more useful than isolated labels; four encoding strategies beyond labels (natural-language notes, register-contrastive examples, structured fields, cross-references); corpus-based register assignment via BCCWJ genre-tagged subcorpora; and quantitative analysis of je-dict-1's current state (9,294 entries = 35.1% with register-relevant prose notes, 45 entries with usage tags, 35 entries with register tags including data integrity issues, 0% structured register field coverage). Six priority actions recommended. Cited Atkins & Rundell 2008, Biber 1988, Brown & Levinson 1987, Burkhanov 1998, Frankenberg-Garcia 2014, Halliday 1978, Hausmann 1989, Ide 1989, Maebo 2012, Nesi & Haill 2002, Ojo 2011, Svensén 2009, Tono 2001, Verkuyl et al. 2003, Vrbinc & Vrbinc 2015.
- [A] Updated entry counts across 10 wiki pages to reflect 2026-05-03 `report.py` output (26,446 entries / 23,663 general / 13,619 cross-references / 105,577 examples / 1,070 candidates / 41.9% symmetry / 6,562 asymmetric refs / 2,847 entries with inline links at 10.8%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`, `research/vocabulary-size-coverage.md`, `research/sense-relations-semantic-networks.md`.
- [E] Ran cross-reference link checker across all wiki pages (537 internal links checked, 0 broken). Checked for orphan pages (0 found across 57 total pages). Added the new register-formality-marking page to `index.md` and as a related page on `topics/register.md`, `research/pragmatics-speech-acts.md`, `research/translation-equivalence.md`, `research/gairaigo-loanwords.md`, `research/learner-lexicography.md`, `research/example-sentences.md`, `research/definition-strategies.md`, `research/corpus-linguistics.md`, `research/error-analysis-japanese-l2.md`, `research/sense-relations-semantic-networks.md`, and `research/semantic-prosody.md`. Updated "Last updated" dates on all modified pages.

## [2026-05-02] maintenance | Japanese aspect research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **Japanese aspect and the ている construction** and created `research/japanese-aspect-teiru.md`. Covers Kindaichi Haruhiko's (1950) four-class verb classification (状態動詞/継続動詞/瞬間動詞/第四種), Kudo Mayumi's (1995) temporal-modal refinements (outer vs. inner aspect, adverbial coercion, discourse-level aspect), mapping to Vendler's (1957) states/activities/accomplishments/achievements; the four ている readings (progressive, resultative, habitual, experiential) with disambiguation criteria; L2 acquisition research including Andersen & Shirai's (1994) Aspect Hypothesis, Shirai & Kurono's (1998) developmental sequence study (progressive ている before resultative), Sugaya & Shirai's (2007) finding that learners acquire ている meanings verb-by-verb supporting per-entry documentation, common English L1 transfer errors (progressive interpretation of resultative); related constructions (てある agent-marked resultative, ていく/てくる directional aspect, てしまう completive, ておく preparatory, ているところ); current dictionary treatment gap (no major JE dictionary systematically documents ている per verb); and detailed implications for je-dict-1 including the ASPECT note system (969 of 7,313 verbs = 13.3% have notes, polishing at entry 02317), priority classification (resultative > ambiguous > てある contrasts > obvious progressives), alignment with SLA research, and coverage targets (~2,000–2,500 verbs needing documentation). Cited Andersen 1991, Andersen & Shirai 1994, Fujii 1966, Kindaichi 1950, Kudo 1995, Okuda 1978, Shibatani 1990, Shirai 2000, Shirai & Kurono 1998, Sugaya & Shirai 2007, Vendler 1957.
- [A] Updated entry counts across 10 wiki pages to reflect 2026-05-02 `report.py` output (26,345 entries / 23,562 general / 13,371 cross-references / 105,220 examples / 1,221 candidates / 42.2% symmetry / 6,405 asymmetric refs / 2,847 entries with inline links at 10.8%). Noted that **cross-references per entry have reached the ≥ 0.5 target** (0.51). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`, `research/vocabulary-size-coverage.md`, `research/sense-relations-semantic-networks.md`.
- [E] Ran cross-reference link checker across all wiki pages (525 internal links checked, 0 broken). Checked for orphan pages (0 found across 56 total pages). Added the new aspect page to `index.md` and as a related page on `grammar-in-dictionaries.md`, `error-analysis-japanese-l2.md`, `vocabulary-acquisition.md`, `japanese-lexicography.md`, `learner-lexicography.md`, `example-sentences.md`, `polysemy-sense-discrimination.md`, and `topics/verb-transitivity.md`. Updated "Last updated" dates on all modified pages.

## [2026-05-01] maintenance | Kanji learning research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **kanji learning and dictionary treatment** and created `research/kanji-learning-dictionaries.md`. Covers the Japanese writing system's orthographic depth (kana as shallow, kanji as deep orthography), the dual-route processing model and neuroimaging evidence (Ijuin & Wydell 2018), on'yomi/kun'yomi reading assignment heuristics and compound word formation patterns (modifier+head, coordinate, verb+object, negation+stem); L1 background effects on kanji acquisition (Koda 2005 on procedural divergence between Chinese-background and alphabetic-background learners, Chikamatsu 1996 on false-friend characters); Toyoda's (2009) four-stage developmental model for component/radical awareness (position → semantic function → phonetic function → limitation awareness); Miwa, Libben, & Baayen (2011) on radical processing units; learning order debate (frequency-based vs. component-based/Heisig vs. grade-based/Kyōiku kanji); the jōyō kanji framework (2,136 characters, 1,026 kyōiku kanji across grades 1-6); Mori & Nagy's (1999) landmark study on compound word inferencing from multiple information sources and Mori's (2007) extension on learner beliefs and component analysis orientation; the kanji lookup problem and historical/modern methods (radical, reading, stroke count, SKIP, four-corner, multi-radical, handwriting, copy-paste); Breen's (2004) WWWJDIC usage data showing multi-radical search (24.8%) and reading search (24.1%) dominating while traditional radical lookup fell to 1.4%; Halpern's core meaning concept; furigana as a learning scaffold (dual coding, incidental acquisition, self-testing), the scaffolding removal debate, and the jōyō-based annotation convention; and detailed implications for je-dict-1 including the kanji index's 2,726 characters, enrichment opportunities (radical, stroke count, grade level, frequency rank), semantic radical grouping for browsing, compound analysis support, and the furigana toggle concept. Cited Breen 2004, Chikamatsu 1996, Halpern 2013, Heisig 1977/2011, Ijuin & Wydell 2018, Katz & Frost 1992, Koda 2005, Miwa et al. 2011, Mori 2007, Mori & Nagy 1999, Tamaoka & Kiyama 2013, Toyoda 2009.
- [A] Updated entry counts across 10 wiki pages to reflect 2026-05-01 `report.py` output (26,242 entries / 23,459 general / 12,974 cross-references / 104,895 examples / 1,327 candidates / 42.5% symmetry / 6,193 asymmetric refs / 2,847 entries with inline links at 10.8%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`, `research/vocabulary-size-coverage.md`, `research/sense-relations-semantic-networks.md`.
- [E] Ran cross-reference link checker across all wiki pages (509 internal links checked, 0 broken). Checked for orphan pages (0 found across 55 total pages). Added the new kanji learning page to `index.md` and as a related page on `topics/furigana-strategy.md`, `research/japanese-lexicography.md`, `research/vocabulary-acquisition.md`, `research/digital-dictionary-ux.md`, `research/dictionary-lookup-behavior.md`, `research/word-formation.md`, `topics/homographs.md`, and `research/gairaigo-loanwords.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-30] maintenance | Sense relations research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **sense relations and semantic networks in learner dictionaries** and created `research/sense-relations-semantic-networks.md`. Covers the taxonomy of paradigmatic sense relations (synonymy, antonymy, hyponymy, meronymy, co-hyponymy) from Cruse (1986), Lyons (1977), and Murphy (2003); subtypes of antonymy (gradable, complementary, converse, directional) and synonymy (register split, connotational split, partial overlap, cross-stratal); dictionary presentation strategies (cross-references, synonym discrimination notes, thesaurus sections, production dictionaries like the Longman Language Activator); WordNet and the Japanese WordNet (日本語ワードネット) as computational sense relation models; the mental lexicon as semantic network (Aitchison 1987/2012, the paradigmatic-to-syntagmatic developmental shift, Jiang 2000 on L2 lexical parasitism); the semantic clustering debate (Tinkham 1993/1997, Waring 1997 showing interference from co-hyponym sets, Hoshino 2010 and Ishii 2015 showing facilitation or null effects, Nation 2000 resolving the debate as introduction-vs-consolidation); Japanese-specific semantic networks (kanji as visual semantic connectors, stratal synonymy between wago/kango/gairaigo, transitivity pairs as a unique sense relation type); and implications for je-dict-1 including cross-reference enrichment priorities (co-hyponym clusters, hypernym links, stratal synonym links), synonym discrimination as a polishing priority, and the clustering lesson for browsing design (optimize for consolidation, keep cluster sizes small, make dimensions of difference explicit). Cited Aitchison 1987/2012, Bond et al. 2009, Cruse 1986, Fellbaum 1998, Hoshino 2010, Ishii 2015, Jiang 2000, Lyons 1977, Miller 1995, Murphy 2003, Nation 2000/2001, Read 2004, Tinkham 1993/1997, Waring 1997.
- [A] Updated entry counts across 12 wiki pages to reflect 2026-04-30 `report.py` output (26,133 entries / 23,350 general / 12,604 cross-references / 104,538 examples / 1,440 candidates / 42.7% symmetry / 5,998 asymmetric refs / 2,847 entries with inline links at 10.9%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`, `research/vocabulary-size-coverage.md`, `research/pragmatics-speech-acts.md`.
- [E] Ran cross-reference link checker across all wiki pages (490 internal links checked, 0 broken). Checked for orphan pages (0 found across 54 total pages). Added the new sense relations page to `index.md` and as a related page on `vocabulary-acquisition.md`, `translation-equivalence.md`, `definition-strategies.md`, `polysemy-sense-discrimination.md`, `collocations.md`, `semantic-prosody.md`, `learner-lexicography.md`, `gairaigo-loanwords.md`, `topics/cross-references.md`, and `topics/verb-transitivity.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-29] maintenance | Pragmatics and speech acts research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **pragmatics and speech acts in bilingual learner dictionaries** and created `research/pragmatics-speech-acts.md`. Covers pragmatic information encoding in dictionaries (usage labels, notes, COBUILD-style definitions, example sentences); the Austin/Searle speech act taxonomy mapped to Japanese examples; Japanese speech acts that resist translation (断り refusals, 依頼 requests, 相槌 back-channeling, culturally untranslatable expressives like よろしくお願いします and お疲れ様); Japanese pragmatics challenges for L2 learners (indirectness with ちょっと and 〜んですが, sentence-final particles ね/よ/な/さ, honorific pragmatics beyond grammar including uchi/soto switching and wakimae, discourse markers and hedging); the well-documented gap between grammatical and pragmatic competence (Bardovi-Harlig 1998/2013 on pragmatic awareness, Thomas 1983 on pragmalinguistic vs. sociopragmatic failure, Schmidt 1993's Noticing Hypothesis applied to pragmatics, Kasper & Rose 2002 on pragmatic development); how major dictionaries handle pragmatics (COBUILD, LDOCE, Kenkyusha, Wisdom — strengths and common shortcomings); and detailed implications for je-dict-1 including discourse function notes for particles/markers, speech act labels and cross-references, indirect speech act marking, pragmatic failure warnings, contextual framing in examples, and priority candidates for pragmatic enrichment. Cited Atkins & Rundell 2008, Austin 1962, Bardovi-Harlig 1998/2013, Blum-Kulka & Olshtain 1984, Brown & Levinson 1987, Ide 1989, Ishihara & Cohen 2010/2021, Kasper & Rose 2002, Kiyama et al. 2012, Matsumoto 1989, McCready & Davis 2020, Schmidt 1993, Searle 1979, Takahashi & Beebe 1987, Thomas 1983, Yong & Peng 2007, Zgusta 1988.
- [A] Updated entry counts across 12 wiki pages to reflect 2026-04-29 `report.py` output (25,978 entries / 23,195 general / 12,091 cross-references / 104,013 examples / 1,594 candidates / 43.5% symmetry / 5,668 asymmetric refs / 2,847 entries with inline links at 11.0%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`, `research/vocabulary-size-coverage.md`.
- [E] Ran cross-reference link checker across all wiki pages (465 internal links checked, 0 broken). Checked for orphan pages (0 found across 53 total pages). Added the new pragmatics page to `index.md` and as a related page on `register.md`, `learner-lexicography.md`, `example-sentences.md`, `definition-strategies.md`, `translation-equivalence.md`, `error-analysis-japanese-l2.md`, `semantic-prosody.md`, `vocabulary-acquisition.md`, `japanese-lexicography.md`, and `grammar-in-dictionaries.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-28] maintenance | Gairaigo loanwords research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **gairaigo (loanwords) in Japanese and their treatment in learner dictionaries** and created `research/gairaigo-loanwords.md`. Covers phonological adaptation processes (vowel epenthesis rules with /u/ default >70% of cases, consonant substitution, mora obstruent insertion, truncation); semantic change taxonomy (narrowing as the most common type, with tables of false friends like マンション/mansion, スマート/smart, ナイーブ/naive); register and stylistic effects of gairaigo vs. wago/kango equivalents (Rebuck 2002's three functions: gap-filling, special effect, euphemism); the NINJAL loanword replacement initiative (2002–2006, 176 problem words) and government survey data showing 78.5%→83.5% public comprehension difficulty; wasei-eigo (和製英語) as pseudo-loanwords with examples (サラリーマン, スキンシップ, ジェットコースター); the cognate advantage (Daulton 2008: 45.5% of top 3,000 BNC families have gairaigo correspondences, 54.8% of top 1,000) and its five key limitations (phonological distance, semantic false friends, L1 asymmetry, production difficulty, overreliance); dictionary treatment approaches in JMdict, Kenkyusha, and Wisdom; quantitative analysis of je-dict-1's 1,588 pure katakana entries (6.1%) plus 337 mixed katakana entries (total ~1,925, 7.5%); and six specific implications for je-dict-1 including semantic shift notes, source language metadata, false-friend annotation, cognate-aware features, and expansion priorities. Cited Daulton 1998/2008, Hatanaka & Pannell 2016, Irwin 2011, Kay 1995, Loveday 1996, Nakao 2020, NINJAL 2003–2006/2006/2017, Olah 2007, Rebuck 2002, Simon-Maeda 2002, Stanlaw 2004.
- [A] Updated entry counts across 12 wiki pages to reflect 2026-04-28 `report.py` output (25,827 entries / 23,044 general / 11,677 cross-references / 103,512 examples / 1,754 candidates / 43.3% symmetry / 5,496 asymmetric refs / 2,847 entries with inline links at 11.0%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`, `research/vocabulary-size-coverage.md`.
- [E] Ran cross-reference link checker across all wiki pages (443 internal links checked, 0 broken). Checked for orphan pages (0 found across 52 total pages). Added the new gairaigo page to `index.md` and as a related page on `word-formation.md`, `japanese-lexicography.md`, `vocabulary-acquisition.md`, `translation-equivalence.md`, `error-analysis-japanese-l2.md`, `definition-strategies.md`, and `topics/register.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-26] maintenance | Vocabulary size research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **vocabulary size and text coverage thresholds** and created `research/vocabulary-size-coverage.md`. Covers the text coverage model and the 95%/98% lexical thresholds (Laufer 1989, Hu & Nation 2000); Nation's (2006) word-family counts for different text types (novels, newspapers, spoken English, graded readers); the diminishing-returns curve from 2,000 WF (~80–85% coverage) to 8,000–9,000 WF (~98%); vocabulary size measurement instruments (VST by Nation & Beglar 2007, VLT, Yes/No tests); Japanese-specific challenges (word family definition problems, script barriers, Sino-Japanese compound productivity); JLPT vocabulary benchmarks; Japanese text coverage studies (Tono et al. 2013, Matsushita 2012, Sato 2014); major learner dictionary sizes (OALD 60,000+ headwords, LDOCE ~80,000, Cambridge ~140,000) and the gap between comprehension vocabulary needs and dictionary reference needs; the "lookup disappointment" problem (Bogaards 1996); and detailed implications for je-dict-1 including tier alignment with coverage thresholds, expansion priority implications, and the self-containment–coverage connection. Cited Beglar 2010, Bogaards 1996, Hu & Nation 2000, Kremmel & Schmitt 2023, Laufer 1989/1998/2013, Laufer & Ravenhorst-Kalovski 2010, Matsushita 2012, Nation 2001/2006, Nation & Beglar 2007, Sato 2014, Schmitt et al. 2001/2011, Tono et al. 2013, Webb & Nation 2017.
- [A] Updated entry counts across 10 wiki pages to reflect 2026-04-26 `report.py` output (25,518 entries / 22,735 general / 11,050 cross-references / 102,407 examples / 2,056 candidates / 43.8% symmetry / 5,160 asymmetric refs / 2,847 entries with inline links at 11.2%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `project/open-issues.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`.
- [E] Ran cross-reference link checker across all wiki pages (408 internal links checked, 0 broken). Checked for orphan pages (0 found across 50 total pages). Added the new vocabulary size page to `index.md` and as a related page on `vocabulary-acquisition.md`, `corpus-linguistics.md`, `learner-lexicography.md`, `vocabulary-tiers.md`, `dictionary-growth.md`, `corpus-prioritization.md`, and `controlled-defining-vocabulary.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-25] maintenance | Error analysis research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **error analysis and learner corpora for Japanese L2** and created `research/error-analysis-japanese-l2.md`. Covers major Japanese learner corpora (I-JAS, KY Corpus, C-JAS, B-JAS, LARP at SCU, Teramura Database, NAIST Goyo Corpus, Lang-8/TEC-JL); five common error categories at the intermediate level with detailed analysis (particle errors including は/が, に/で, を usage; verb form and conjugation errors including て-form, conditional selection, ている aspect misuse; register and politeness errors including keigo avoidance and hypercorrection; lexical and collocational errors including Chinese false friends and near-synonym confusion; sentence structure errors including relative clause difficulties); L1 transfer effects for Chinese, Korean, and English-speaking learners with specific error pattern differences; error analysis methodology evolution (contrastive analysis → error analysis → interlanguage analysis); and seven specific implications for je-dict-1 (particle information prioritization, ている polysemy documentation, near-synonym contrastive notes, Chinese false friend warnings, register consistency in examples, error-preempting example design, error-frequency-informed polishing priorities). Cited Corder 1967, Gabriele & McClure 2011, Ichikawa 1997, Koyama et al. 2020, Lado 1957, Noda & Sakoda 2020, Oyama 2010, Sakoda & Kawaguchi 2023, Selinker 1972, Shirai & Kurono 1998, Teramura 1990.
- [A] Updated entry counts across 10 wiki pages to reflect 2026-04-25 `report.py` output (25,348 entries / 22,565 general / 10,735 cross-references / 101,840 examples / 2,226 candidates / 44.6% symmetry / 4,933 asymmetric refs / 2,847 entries with inline links at 11.2%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`.
- [E] Ran cross-reference link checker across all wiki pages (386 internal links checked, 0 broken). Checked for orphan pages (0 found across 49 total pages). Added the new error analysis page to `index.md` and as a related page on `vocabulary-acquisition.md`, `collocations.md`, `grammar-in-dictionaries.md`, `example-sentences.md`, `japanese-lexicography.md`, `learner-lexicography.md`, `verb-transitivity.md`, and `register.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-23] maintenance | Multiword expressions research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **multiword expressions (MWEs) in learner dictionaries** and created `research/multiword-expressions.md`. Covers the MWE taxonomy by compositionality (free combinations → collocations → figurative idioms → pure idioms, following Cowie 1998 / Vinogradov) and by Japanese grammatical structure (compound verbs, 慣用句, 四字熟語, proverbs, greetings, grammar patterns, light-verb constructions); the dictionary placement problem (5 strategies from Atkins & Rundell 2008, subentry vs. independent entry trade-offs); MWE types and acquisition challenges (Nesselhauf 2005 on collocation errors, Yamashita & Jiang 2010 on L1 influence); Wray's (2002) holistic storage/retrieval model; the 気 cluster problem and particle-as-part-of-expression design; quantitative analysis of je-dict-1's ~745 expression entries (233 verb-object, 113 subject-predicate, 100 location/goal, 15 proverbs, 7 grammar patterns, 277 other); inclusion criteria decision table; Siepmann's (2005) finding that dictionaries neglect compositional routine formulae; Palmer & Hornby's historical connection to Japanese MWE lexicography; and detailed implications for je-dict-1 (cross-reference density, metaphorical motivation notes, collocation fields, grammar pattern coverage expansion, body-part idiom cluster auditing). Cited Atkins & Rundell 2008, Biber et al. 1999, Cowie 1998, Erman & Warren 2000, Granger & Meunier 2008, Moon 1998, Nesselhauf 2005, Pawley & Syder 1983, Siepmann 2005, Wray 2002, Yamashita & Jiang 2010.
- [A] Updated entry counts across 8 wiki pages to reflect 2026-04-23 `report.py` output (24,908 entries / 22,125 general / 9,413 cross-references / 100,247 examples / 1,432 candidates / 45.3% symmetry / 4,280 asymmetric refs / 2,847 entries with inline links at 11.4%). Noted the **100,000 example sentence milestone** in the retrospective page. Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `ideas/dictionary-growth.md`, `research/controlled-defining-vocabulary.md`, `research/grammar-in-dictionaries.md`.
- [E] Ran cross-reference link checker across all wiki pages (385 internal links checked, 0 broken). Added the new MWE page to `index.md` and as a related page on `collocations.md`, `compound-verbs.md`, `learner-lexicography.md`, `word-formation.md`, `grammar-in-dictionaries.md`, and `definition-strategies.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-22] maintenance | Grammar information research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **grammar information in learner dictionaries** and created `research/grammar-in-dictionaries.md`. Covers four encoding strategies (opaque codes, semi-transparent codes, natural-language descriptions, grammar-through-examples), the historical trend from Hornby's verb tables to COBUILD's definitions; the consultation gap (Nesi & Haill 2002, Tono 2001, Herbst 1989) showing learners largely ignore coded grammar; Frankenberg-Garcia's (2012–2015) encoding examples concept; Japanese-specific challenges (particle-verb dependencies, transitivity pairs, conjugation complexity, ている aspect polysemy, keigo); the Makino & Tsutsui grammar dictionary model; Herbst's valency dictionary approach; and detailed implications for je-dict-1 including what the dictionary already does well (natural-language notes, conjugation tables, transitivity marking) and five areas for improvement (particle templates, encoding-optimized examples, contrastive grammar notes, structured particle fields, grammar-entry cross-references). Cited Atkins & Rundell 2008, Frankenberg-Garcia 2012/2014/2015, Herbst 1989/2004, Hornby 1942, Makino & Tsutsui 1986/1995, Nesi & Haill 2002, Sinclair 1987, Tono 2001, Wekker 1992.
- [A] Updated entry counts across 15 wiki pages to reflect 2026-04-22 `report.py` output (24,760 entries / 21,977 general / 8,801 cross-references / 99,747 examples / 1,584 candidates / 45.0% symmetry / 4,062 asymmetric refs / 2,847 entries with inline links at 11.5%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `project/entry-design.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `topics/compound-verbs.md`, `ideas/audio-expansion.md`, `ideas/dictionary-growth.md`, `ideas/multi-model-proofreading.md`, `ideas/parallel-agent-architecture.md`, `ideas/word-discovery-strategies.md`, `research/controlled-defining-vocabulary.md`, `research/digital-dictionary-ux.md`, `research/pitch-accent.md`.
- [E] Ran cross-reference link checker across all wiki pages (359+ internal links checked, 0 broken). Added the new grammar page to `index.md` and as a related page on `learner-lexicography.md`, `example-sentences.md`, `entry-design.md`, `verb-transitivity.md`, `dictionary-lookup-behavior.md`, `definition-strategies.md`, and `collocations.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-17] maintenance | Polysemy research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **polysemy and sense discrimination** in learner dictionaries and created `research/polysemy-sense-discrimination.md`. Covers the ontological debate (Kilgarriff 1997), lumping vs. splitting trade-offs (with bilingual dictionary considerations), three sense-ordering approaches (historical, frequency, logical/core-first), Bond et al. (2024) models of polysemy structure (prototype, progenitor, nearest-neighbor chaining, local chaining), cognitive linguistics and prototype theory, Japanese-specific challenges (extreme polysemy in basic verbs, kanji as sense disambiguator, compound verb extensions), Hoshino & Shimizu (2018) on learner mental lexicon organization, and detailed implications for je-dict-1 including quantitative analysis of the current sense distribution (19,005 single-definition entries, 4,504 with 2 definitions, 478 with 3+, none with example-to-sense linking). Recommendations include documenting a sense-ordering convention, adding example-sense linking, reviewing high-polysemy entries, and adding sense relationship markers. Cited Atkins & Rundell 2008, Bond et al. 2024, Geeraerts 2006, Hoshino & Shimizu 2018, Kilgarriff 1997, Lew 2013, Lu & Geng 2024, McCrae et al. 2022, Nesi 1999.
- [A] Updated entry counts across 12 wiki pages to reflect 2026-04-17 `report.py` output (23,987 entries / 21,204 general / 7,787 cross-references / 97,124 examples / 2,366 candidates / 44.9% symmetry / 3,660 asymmetric refs). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `project/open-issues.md`, `research/controlled-defining-vocabulary.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `topics/compound-verbs.md`, `ideas/audio-expansion.md`, `ideas/dictionary-growth.md`, `ideas/multi-model-proofreading.md`, `ideas/parallel-agent-architecture.md`, `ideas/word-discovery-strategies.md`, `research/digital-dictionary-ux.md`, `research/pitch-accent.md`.
- [E] Ran cross-reference link checker across all 40+ wiki pages (350 internal links checked, 0 broken). Added the new polysemy page to `index.md` and as a related page on `definition-strategies.md`, `vocabulary-acquisition.md`, `homographs.md`, and `learner-lexicography.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-15] maintenance | Controlled defining vocabulary research, stats sync, tier-system cross-link

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **controlled defining vocabulary** (CDV) and created `research/controlled-defining-vocabulary.md`. Covers the historical arc from Ogden's Basic English (1930) through West's General Service List (1953) to LDOCE's explicit ~2,000-word defining vocabulary (Procter 1978) and COBUILD's full-sentence definition style (Sinclair 1987); what a CDV accomplishes (non-circularity, reading-level control, stylistic consistency, computational tractability); its criticisms (naturalness trade-offs, intra-CDV circularity, polysemy within defining words, L2-specific pragmatics); treatment in bilingual and Japanese-English dictionaries; and a detailed analysis of how je-dict-1's closed basic+core tiers plus the inline-word-link system function as an analogue of the CDV tradition. Concrete recommendations include keeping the closed-tier policy as a hard constraint, adding an automated self-containment linter, and adopting soft-CDV discipline for the English notes field. Cited Adamska-Sałaciak 2016, Hanks, Herbst 1996, Nation 2001/2013, Ogden 1930, Procter 1978, Rundell 2008, Sinclair 1987, West 1953.
- [C] Expanded `project/vocabulary-tiers.md` self-containment section to explicitly frame the tier system as a CDV analogue and link to the new research page, and added the new page to the vocabulary-tiers related-pages list.
- [A] Refreshed entry counts with end-of-day `report.py` output (23,841 entries / 21,058 general / 7,427 cross-references / 96,585 examples / 2,513 candidates / 45.5% symmetry / 3,463 asymmetric refs) across `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, and the retrospective page. The earlier 2026-04-15 session had used morning snapshot values (23,609 / 20,826 / 2,747); today's second session catches the wiki up to the 24027-24042 and 24013-24026 entry batches merged since then.
- [E] Added the new page to `index.md`. Existing "Last updated" dates on all touched pages were already 2026-04-15 so no date changes were required.

## [2026-04-15] maintenance | Semantic prosody research, stats sync, retrospective refresh

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **semantic prosody** — the evaluative colouring that attaches to words through habitual collocation — and created `research/semantic-prosody.md`. Covers the Sinclair/Louw/Stubbs/Partington theoretical tradition, distinctions between connotation / semantic preference / semantic prosody, the Hunston/Whitsitt critiques, Japanese examples organised by adverbs (ろくに, なかなか, いちいち, いかにも, わざわざ, せっかく, まさか), verbs and auxiliaries (〜てしまう, benefactives, 〜がる, 〜ぶる), and noun-modifiers (とんでもない, 〜くさい, 〜っぽい). Includes L2 acquisition findings (Xiao & McEnery 2006, Hoey 2005, Wei & Li 2014), five dictionary treatment strategies, and concrete recommendations for how je-dict-1's existing USAGE and SIMILAR WORDS blocks can carry prosody information explicitly. Full reference list: Hoey 2005, Hunston 2007, Louw 1993, Partington 1998/2004, Sinclair 1991/1996, Stubbs 1995/2001, Wei & Li 2014, Whitsitt 2005, Xiao & McEnery 2006.
- [A] Synced entry counts with `report.py` output (23,609 entries / 20,826 general / 7,423 cross-references / 95,784 examples / 2,747 candidates / 45.5% symmetry rate) across `project/overview.md`, `project/vocabulary-tiers.md`, `project/open-issues.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, and the retrospective page.
- [C/E] Refreshed `topics/enhancement-plan-retrospective.md` metrics table to the 2026-04-15 numbers, flagging that **cross-reference symmetry has drifted downward** (3,461 asymmetric refs, up ~500 from two days earlier) as new entries add unreciprocated links faster than the symmetry pass processes them. Noted this as a suggested next sprint target.
- [E] Added cross-references from `research/collocations.md`, `research/definition-strategies.md`, and `research/translation-equivalence.md` into the new semantic prosody page; added the new page to `index.md`. Ran a Python-based link-checker across the whole wiki (0 broken links).
- [E] Updated "Last updated" dates on all pages touched this session.

## [2026-04-13] maintenance | Post-enhancement architecture update, retrospective page, stats sync

**Session type**: Nightly maintenance

**Activities**:
- [C] Substantially rewrote `project/architecture.md` to document the post-Enhancement-Plan infrastructure: task queue, orchestrator, monitor, multi-model review pipeline, entry locking, priority polishing, semantic fields, learner scenarios, expository articles, consistency checker, and the full current build-script inventory. Previous version only described the core build (validate → update_indexes → build_flat).
- [A] Updated `project/content-pipeline.md` to reflect coexisting progress-file and queue-based polishing modes, priority ordering, and the orchestrator/monitor layer. Added verb transitivity, aspect notes, and cross-model review to the polishing task list.
- [D/F] Created `topics/enhancement-plan-retrospective.md` — synthesis of what the 16-phase Enhancement Plan (2026-04-09) built, which wiki hypotheses it validated, which it under-specified, and progress against the plan's targets measured on 2026-04-13. Draws on `enhancement/enhancement-plan-2026-04-09.md`, `enhancement/tracking.md`, and `build/report.py` output.
- [A/E] Added implementation-status banners to `ideas/parallel-agent-architecture.md` and `ideas/multi-model-proofreading.md` linking to the retrospective page and current architecture page — these design docs were written as proposals and the wiki now signals that they've shipped.
- [A] Updated entry counts across core pages: 23,000→23,418 total, 20,200→20,600+ general, 6,000→6,600+ cross-references, 93,500→95,000+ examples, 3,200→2,900 candidates; noted ~48% cross-reference symmetry from the updated `report.py`.
- [E] Updated "Last updated" dates on all pages modified this session; updated `index.md` with the new retrospective page; updated `planning/maintain-knowledge-base.md` to note that the `enhancement/` folder is now a closed project and to point future sessions at the retrospective for catching up.

## [2026-04-08] maintenance | Dictionary lookup behavior research, homographs deepening, stats sync

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched dictionary lookup behavior and skills — Nesi's (1999) lookup process model (5 stages), Lew's (2013) revision for electronic dictionaries, common lookup errors (failure to lemmatize, first-fit sense selection, ignoring context), Atkins & Varantola (1997) monitoring study, Tono (2001) eye-tracking research, Thumb (2004) bilingualised dictionary strategies, Japanese-specific challenges (kanji barrier, homophone density, kun-yomi near-synonyms); created research/dictionary-lookup-behavior.md citing Atkins & Varantola (1997), Lew (2004, 2013), Nesi (1999), Thumb (2004), Tono (2001), Halpern, CJK Dictionary Institute
- [C] Substantially expanded topics/homographs.md from ~250 words to ~1,500 — added concrete data from the dictionary (117 homographic headwords, 1,372 homophone readings), detailed analysis of five homograph types with tables and examples, in-depth treatment of homographic heterophones (角, 追従), dense homophone clusters (けん×7, かく×6), kun-yomi near-synonyms (かえる×5), search result disambiguation strategies, split-vs-merge design principles table
- [A] Updated entry counts across 14 wiki pages: entries 22,700→23,000, general tier 19,900→20,200, cross-references 5,700→6,000, examples 92,500→93,500, candidates 3,470→3,200; updated audio expansion storage estimates, parallel architecture, multi-model proofreading, compound verbs, pitch accent, LLMs-as-corpora, entry consistency, and word discovery pages accordingly
- Added cross-references from vocabulary-acquisition.md, learner-lexicography.md, and digital-dictionary-ux.md to the new dictionary-lookup-behavior page; added dictionary-lookup-behavior.md as a related page on homographs.md
- Updated index.md with 1 new page entry

## [2026-04-07] maintenance | Definition strategies research, learner lexicography deepening, stats sync

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched definition and gloss writing strategies for bilingual learner dictionaries — Adamska-Sałaciak's equivalence typology (translational, cognitive, explanatory, functional), Zgusta's degrees of equivalence, sense ordering approaches, Japanese-English specific challenges; created research/definition-strategies.md citing Adamska-Sałaciak (2010), Atkins & Rundell (2008), Zgusta (1971), Lew (2004)
- [C] Substantially expanded research/learner-lexicography.md — added sections on the monolingual vs. bilingual debate (Laufer & Hadar 1997, Laufer & Kimmel 1997, Lew 2004), bilingualised dictionaries, dictionary structure terminology (macrostructure/microstructure/mediostructure/access structure), frame semantics and prototype theory foundations, production vs. reception comparison table; expanded references and related pages
- [A] Updated entry counts across 14 wiki pages: entries 22,400→22,700, general tier 19,600→19,900, cross-references 5,400→5,700, candidates 3,750→3,470; updated audio expansion estimates, parallel architecture, multi-model proofreading, compound verbs, pitch accent, LLMs-as-corpora, and word discovery pages accordingly
- Added cross-references from translation-equivalence.md and learner-lexicography.md to the new definition-strategies page
- Updated index.md with 1 new page entry

## [2026-04-06] maintenance | Word formation research, stats sync, lint check

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched Japanese word formation and morphology for learner dictionaries — vocabulary strata (wago/kango/gairaigo), compounding patterns, productive affixes, derivation, abbreviation, morphological awareness research (Kondo-Brown 2006, Mori & Nagy 1999); created research/word-formation.md citing Kageyama (2016), Halpern, CJK Dictionary Institute, Ito & Mester (2015)
- [A] Updated entry counts across 7 wiki pages: entries 22,200→22,400, general tier 19,400→19,600, candidates 4,000→3,750, cross-references 5,300→5,400, examples 90,800→91,700; updated audio expansion estimates accordingly
- [E] Audited all cross-references across 40 wiki pages — no broken links, no orphan pages, all "Last updated" dates current (2026-04-04 or later)
- Added cross-references from japanese-lexicography.md, vocabulary-acquisition.md, and compound-verbs.md to the new word-formation page
- Updated index.md with 1 new page entry

## [2026-04-06] maintenance | Deterministic vs. semantic task analysis

**Session type**: Manual session (curator-directed)

**Activities**:
- [D] Created topics/deterministic-vs-semantic-tasks.md — comprehensive analysis of which editorial tasks can be automated deterministically and which require LLM semantic judgment. Covers: historical context (early project experience with Claude writing scripts), the two-layer architecture, complete taxonomy of all 22+ deterministic scripts and 12+ semantic tasks, detailed analysis of hybrid tasks, deep dives into why specific tasks (furigana, cross-references, examples, semantic labels) resist automation, the "trend toward the mean" advantage for lexicographic work, automatable components within semantic tasks, design principles distilled from project experience, and implications for future development
- [F] Synthesized information across prompts, skills, and build scripts to document the project's hard-won lessons about the boundary between programmatic and editorial work
- Updated index.md with 1 new page entry

## [2026-04-06] maintenance | Onomatopoeia research, UX deepening, cross-ref additions

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched Japanese onomatopoeia and mimetic words — classification system, morphological patterns, phonosemantics (Hamano 1998), L2 acquisition challenges, dictionary treatment approaches; created research/onomatopoeia-mimetics.md citing Hamano, Iwasaki & Yoshioka, Feng, and Inose
- [C] Substantially expanded research/digital-dictionary-ux.md — added detailed analysis of je-dict-1's current search architecture (three parallel indexes, match strategies, tag-based browsing), documented 8 specific improvement opportunities with implementation notes, added inflected form search as a high-value opportunity using existing conjugation data, added entry page UX section
- [E] Added cross-references from japanese-lexicography.md, translation-equivalence.md, and expository-articles.md to the new onomatopoeia page; checked all wiki cross-references for broken links
- Updated index.md with 1 new page entry

## [2026-04-06] maintenance | Cross-check accuracy, word discovery strategies, growth vision, cross-ref expansion

**Session type**: Manual session (curator-directed)

**Activities**:
- [E] Fixed outdated audio references in open-issues.md and audio-expansion.md — audio files were removed in early 2026 but wiki still referenced ~1,028 entries with audio
- [E] Updated outdated counts: cross-references (3,400→5,300+), candidates (5,400→4,000), general tier (16,000→19,400+) across multiple pages
- [A] Updated content-pipeline.md to reflect LLM brainstorming as the primary candidate discovery method
- [D] Created ideas/word-discovery-strategies.md — comprehensive analysis of brainstorming pros/cons, 7 proposed alternative discovery methods (scenario-based, textbook mining, user simulation, reverse cross-ref mining, kanji productivity, semantic field audits, learner error analysis), safeguards against missing basic vocabulary
- [D] Created ideas/dictionary-growth.md — no maximum size policy, three growth phases, proper names/encyclopedia entry design discussion, long-term dictionary identity
- [C] Substantially expanded topics/cross-references.md — added sections on why cross-refs matter for browsing (vocabulary networks, serendipitous learning, disambiguation), improvement ideas (higher coverage targets, automated suggestions, quality review, navigational improvements, typed browsing paths, completeness metrics)
- [C] Added tier reassessment section to project/vocabulary-tiers.md — noting that basic/core assignments need rechecking since they were made early in the project
- [C] Added proper names design question to project/open-issues.md
- Updated index.md with 2 new page entries

## [2026-04-06] maintenance | Major expansion — proofreading, articles, consistency, parallelism, word variants

**Session type**: Manual session (curator-directed)

**Activities**:
- [D] Created ideas/multi-model-proofreading.md — comprehensive plan for systematic cross-model entry verification via OpenRouter, covering furigana, glosses, examples, notes; two-pass review architecture; implementation roadmap in three phases; cost estimates
- [D] Created ideas/expository-articles.md — proposal for standalone articles on vocabulary topics (counters, keigo, onomatopoeia families, etc.) to support browsing and serendipitous discovery; article types, format options, implementation plan, prioritization
- [D] Created topics/entry-consistency.md — analysis of consistency problems in note structure, cross-references, glosses, and examples across similar entries; proposed standard note structures by POS; strategies including template-driven revision and cluster-based review
- [D] Created ideas/parallel-agent-architecture.md — design for autonomous parallel agent system; four architecture options analyzed (file-based, task-based, claim-based, branch-per-agent) with hybrid recommendation; three-phase transition plan; quality safeguards
- [D] Created topics/word-variants.md — policy framework for handling words with multiple written forms (kanji variants, okurigana, kanji vs. kana, reading variants); when to create separate entries vs. consolidate; search index implications; data model considerations
- [C] Expanded ideas/ai-review.md — added links to new multi-model proofreading and parallel architecture pages; reorganized into review strategies and implementation approaches sections
- [C] Updated project/open-issues.md — added new design questions (word variants, entry consistency, expository articles) and process issues (sequential bottleneck, single-model risk); expanded related pages
- [E] Updated index.md with 5 new page entries (2 topics, 3 ideas)
- All new pages incorporate insights from the curator's about.html blog entries and respond to specific curator priorities communicated in this session

## [2026-04-05] maintenance | Counters research, audio expansion deepening, stats sync

**Session type**: Nightly maintenance

**Activities**:
- [A] Updated project/overview.md with current stats (22,200+ entries, 90,800+ examples, 5,200+ cross-refs, 19,400+ general tier)
- [B] Researched Japanese counters and classifiers in learner dictionaries — semantic categories, sound changes, acquisition challenges, dictionary treatment approaches; created research/counters-classifiers.md citing Downing (1996), Yamamoto & Keil, and Tofugu's tiered classification
- [C] Substantially expanded ideas/audio-expansion.md — added 2026 TTS landscape comparison (cloud and open-source), detailed implementation plan in 3 phases, storage/format considerations, cost estimates, quality assurance notes; updated entry count and audio coverage percentage
- Added cross-references from japanese-lexicography.md and vocabulary-acquisition.md to the new counters page

## [2026-04-05] maintenance | LLMs beyond flat corpora, LLMs as corpus replacements

**Session type**: Manual session (curator-directed)

**Activities**:
- [B] Researched LLM applications in lexicography — Rundell (2024), eLex 2025 proceedings, pragmatics surveys, Sydney Corpus Lab synthesis
- [D] Created research/beyond-flat-corpora.md — how LLMs enable semantic-pragmatic analysis that flat corpora cannot provide, covering word sense disambiguation in context, pragmatic function identification, register assessment, and discourse-level analysis
- [D] Created topics/llms-replacing-corpora.md — whether LLMs can replace traditional corpora in dictionary production, synthesizing Rundell's skepticism, the "trend toward the mean" argument, eLex 2025 consensus, a comparative strengths table, and implications for je-dict-1's LLM-primary workflow
- Both pages written in response to curator observations about LLM capabilities in this project

## [2026-04-05] maintenance | Collocations research, vocabulary acquisition deepening, stats update

**Session type**: Nightly maintenance

**Activities**:
- [A] Updated project/overview.md with current stats (nearly 22,000 entries, 90,000+ examples, 5,200+ cross-references)
- [A] Updated project/open-issues.md with corrected audio coverage percentage
- [B] Researched collocations in learner dictionaries — L1 transfer effects, Japanese-specific patterns, statistical measures, dictionary presentation approaches; created research/collocations.md
- [C] Substantially deepened research/vocabulary-acquisition.md — added sections on receptive vs. productive knowledge, formulaic sequences, dictionary lookup and retention research, and expanded implications
- [E] Checked all 107 cross-references across 27 wiki pages — no broken links found
- Added cross-references from corpus-linguistics.md, quality-standards.md, and vocabulary-acquisition.md to the new collocations page

## [2026-04-05] maintenance | Pitch accent research, register deepening, compound verbs

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched pitch accent in Japanese learner dictionaries; created research/pitch-accent.md covering accent patterns, notation systems, intelligibility research, existing resources (OJAD, NHK dictionary), and implications for je-dict-1
- [C] Substantially expanded topics/register.md — added sections on the two-axis register system (formality vs. politeness), schema field documentation, gendered language, keigo handling patterns, register in example sentences, register challenges for learner dictionaries, and an implementation roadmap
- [D] Created topics/compound-verbs.md — new page covering lexical vs. syntactic compound verbs, V2 auxiliary patterns, the entry-vs-pattern design decision, current je-dict-1 practice, the NINJAL Compound Verb Lexicon, and recommended approach

## [2026-04-05] initial | Knowledge Base Creation

**Session type**: Initial setup

Created the knowledge base structure:
- Directory layout: `project/`, `research/`, `topics/`, `ideas/`
- Index file with page catalog
- 7 project pages covering overview, architecture, entry design, tiers, pipeline, quality, and open issues
- 7 research pages synthesizing external knowledge on lexicography, SLA, corpus linguistics, etc.
- 5 topic pages on specific design decisions (furigana, cross-refs, homographs, transitivity, register)
- 4 idea pages for future directions
- Maintenance session prompt at `planning/maintain-knowledge-base.md`
