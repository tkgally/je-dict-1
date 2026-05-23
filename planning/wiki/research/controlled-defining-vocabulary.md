# Controlled Defining Vocabulary

**Last updated**: 2026-05-16

## Overview

A **controlled defining vocabulary** (CDV) is a deliberately restricted list of words that a learner's dictionary uses to write all of its definitions. The idea is simple: if every definition draws on the same small, high-frequency core, a learner who knows that core can read any definition in the book without hitting an unknown word that forces a secondary lookup. CDV is one of the most distinctive innovations of the "learner-dictionary tradition" that began with the Oxford Advanced Learner's Dictionary (OALD) and matured in the Longman Dictionary of Contemporary English (LDOCE) and the Collins COBUILD English Dictionary. It bears directly on je-dict-1's tier system and its "self-containment" principle.

## Historical origins

### Ogden's Basic English (1930)

Charles Kay Ogden's *Basic English* (1930) proposed 850 words chosen so that the rest of English vocabulary could be paraphrased using them. Basic English was not a dictionary defining vocabulary per se but established the conceptual precedent: a small, carefully chosen word list can serve as a universal paraphrase medium. Its weaknesses — most famously, its heavy reliance on periphrastic verb-plus-noun constructions ("give a push" rather than "push") — showed that a defining vocabulary cannot be chosen by frequency alone; it must also support idiomatic, natural paraphrase.

### West's General Service List (1953)

Michael West's *A General Service List of English Words* (1953) selected roughly 2,000 word families by combining raw frequency with pedagogical criteria: range across text types, ease of learning, and what West called "necessity" — whether a word had any near-synonym that could replace it. The GSL became the de facto basis for controlled English in pedagogy and, crucially, for later learner-dictionary defining vocabularies. Most modern CDVs can be traced back to West by one or two steps of revision.

### Learner-dictionary CDV (1978–1987)

- The **Longman Dictionary of Contemporary English** (Procter, ed., 1978; 1st ed.) introduced a formally controlled ~2,000-word defining vocabulary, descended from the GSL. The back matter listed the defining words explicitly — an accountability mechanism that let reviewers verify compliance.
- The **Oxford Advanced Learner's Dictionary** adopted a similar (though slightly larger, ~3,000-word) defining vocabulary in subsequent editions.
- The **Collins COBUILD English Language Dictionary** (Sinclair, ed., 1987) took a different route: instead of publishing a fixed defining list, it committed to writing **full-sentence definitions** in natural, corpus-attested English. The COBUILD editorial guidelines still effectively controlled vocabulary (Sinclair 1987), but the discipline came from corpus frequency and from consistency of definition style rather than from a closed list.

These three approaches — OALD's list, Longman's list, and COBUILD's corpus-driven style — define the spectrum of controlled-definition practice.

## What a CDV does

### 1. Non-circularity

The central promise of a CDV is that the set of headwords fully explained by the CDV covers the entire dictionary without creating lookup loops. Formally: if the learner knows the ~2,000 CDV words, then reading the definition of any headword yields no unfamiliar defining word; reading the definitions of any intermediate lookups likewise stays within the CDV. Without this property, even a modest unknown word in a definition can trigger a cascade of lookups that frustrates or misleads the learner.

### 2. Reading-level control

Because CDV words are themselves high-frequency and denotationally central, definitions written in a CDV tend to fall at a predictable reading level. This matters for lower-intermediate learners who can follow a 2,000-word core but stall in front of formal synonyms like *impose*, *endeavour*, *commence*. Definitions written in CDV look plainer and are easier to memorise.

### 3. Stylistic consistency

CDVs push lexicographers toward a uniform register and syntactic style across thousands of definitions. Without a CDV, different editors working on different letters of the alphabet drift apart: one favours abstract noun paraphrases, another uses full-clause definitions, a third uses synonym stacks. A CDV (coupled with a definition style guide) reduces that drift.

### 4. Computational tractability

As Hanks and others noted in the 1990s, a CDV makes the dictionary machine-readable in a non-trivial sense: you can parse every definition against a known closed vocabulary, which supports dependency analysis, sense-disambiguation research, and cross-linguistic alignment. This is why LDOCE's CDV became a staple resource in computational lexicography through the 1990s.

## Criticisms and limits

### Naturalness trade-offs

The most persistent critique (Herbst 1996; Rundell 2008; and see the 2016 ResearchGate critique of LDOCE's CDV by Adamska-Sałaciak and others) is that a strictly closed list forces awkward paraphrase. If the only available verb for "to confiscate" is "to take", the definition loses the legal-register precision that matters. The standard response is that a CDV is a **guideline**, not an absolute constraint: editors may use out-of-CDV words when they add precision, provided those words are themselves glossed or flagged.

### Definition circularity within the CDV

Even within a CDV, circularity can creep in: *begin = to start; start = to begin.* Longman's second and later editions explicitly hunted for such loops, but small undirected cycles among near-synonyms are hard to eliminate entirely. Corpus-driven full-sentence definitions (the COBUILD line) partially sidestep this because the "definition" embeds the headword in a syntactic pattern rather than equating it to a synonym.

### Polysemy within the CDV itself

CDV words are themselves polysemous. LDOCE addressed this by committing to use only the **central senses** of CDV words in definitions. That requires the CDV's own entries to mark which sense is "defining-vocabulary usable," which adds editorial overhead. Without that discipline, a learner reading "hold" in a definition cannot tell which of its many senses is active.

### L2-specific pragmatics

A CDV derived from English frequency lists assumes a roughly generic adult learner. It can miss vocabulary that is frequent in L2 learner interaction (classroom, travel, immigration) but infrequent in corpora of native text. Nation (2001, *Learning Vocabulary in Another Language*) argues that for pedagogical purposes, the defining vocabulary should be **informed by** frequency but **validated for** learner use, which requires piloting.

## Controlled vocabulary in bilingual and Japanese-English dictionaries

Bilingual learner dictionaries have less of a CDV tradition than monolingual ones, because the "definition" is often a translation equivalent and the controlling vocabulary is the L1 of the learner. But the principle carries over to the **English-language gloss** and to **usage notes**:

- The Oxford Japanese-English Learner's Dictionary and similar works maintain an internal defining vocabulary for usage notes, largely inherited from OALD.
- Kenkyusha's *New Japanese-English Dictionary* (5th ed.) does not use a CDV; its glosses draw on formal English freely, which is part of why it works as a translator's tool but not a beginner's dictionary.
- Japanese monolingual learner dictionaries (e.g., 日本語学習者用基本語用例辞典, the Sanseido Kokugo series in its learner variants) use a CDV of roughly 2,000–3,000 Japanese headwords, typically those in the 基本語 (kihongo) or 日本語能力試験 N5–N4 bands.

## Defining vocabulary vs. tier system: je-dict-1's analogue

je-dict-1 does not have a formal CDV because its glosses are **English translations**, not English paraphrases. What it has instead is a **three-tier vocabulary classification** (basic 801, core 1,982, general 24,700) that plays a structurally similar role in two ways:

1. **Self-containment**. The guideline that higher-tier entries' examples and notes should draw their Japanese vocabulary from the same tier or below (basic entries should use basic words; core entries should use core-or-below words) is the direct analogue of CDV discipline. It ensures that a learner who has mastered the basic tier can read any basic-tier entry end-to-end without a secondary lookup.

2. **Closed lower tiers**. Basic and core tiers are closed — new entries go only into general — which keeps the "defining corpus" stable. This is more rigid than LDOCE's CDV (which revises across editions) and more rigid than COBUILD's corpus-driven style (which floats with the corpus), and it has a documentation benefit: a learner who learns the basic tier today learns exactly the vocabulary that underlies all basic-tier examples and notes indefinitely.

The **inline word link system** (`⟦surface→base：entry_id⟧`) extends this idea further. Even when an example sentence in a general-tier entry uses words above the basic tier, every non-basic word is hyperlinked to its own entry. The learner does not need to guess what the word means or go to an external dictionary — the dictionary defines itself through its own hyperlinks. This is functionally equivalent to a CDV but with an explicit escape hatch: instead of forcing the writer to paraphrase with basic words, it permits any word and links it. The cost is that the writer still has to produce that inline link (currently 10.5% of entries have any links at all — see `build/report.py`).

## Implications for je-dict-1

### Keep the closed-tier policy

Allowing new entries into basic or core would break the self-containment guarantee. The closed-tier policy should be treated as a hard constraint comparable to LDOCE's commitment to its defining vocabulary list. (See `project/vocabulary-tiers.md` for the existing rationale.)

### Strengthen the self-containment check

The wiki already notes that examples in basic entries should use only basic words, but there is no automated linter for this. A simple check — for each entry, scan all Japanese example tokens and flag any token whose entry is higher-tier than the current entry — would operationalise the self-containment principle the same way LDOCE's compliance-checking did for its CDV. The project's existing inline-link infrastructure already maps surface forms to entry IDs; the check is a natural extension of `build/check_consistency.py`.

### Write notes in controlled English

The English **notes** field has no formal CDV discipline, and note quality varies (`build/score_note_quality.py` shows avg scores per POS from 62 to 98). Adopting a soft CDV for the notes — e.g., "write using vocabulary a B1-level English reader knows; prefer Germanic over Latinate verbs; avoid technical linguistic jargon" — would bring je-dict-1's notes closer to LDOCE's defining style. This is a stylistic polishing task rather than a structural change; see `project/quality-standards.md` and the `expand-short-notes` polishing task.

### Do not adopt a fixed English-word CDV for glosses

The bilingual gloss is a translation, not a definition, and its job is to match the register, part-of-speech, and connotation of the Japanese headword. Restricting glosses to a closed English word list would hurt more than help — *carnal* is the right gloss for 愛欲 even though it is not in any CDV. The CDV discipline belongs in the **notes**, not the gloss.

### Consider a "defining Japanese vocabulary" for future expository articles

The pilot **expository articles** feature (see `ideas/expository-articles.md`) will produce standalone prose articles in Japanese and English. For the Japanese portion of those articles, a CDV of the basic + core tiers (roughly 2,800 Japanese words, plus bridging grammar) would match LDOCE's scale and gives the articles a guaranteed readability floor. This is more feasible than a CDV for the whole dictionary because articles are a bounded, slower-moving corpus.

## References

- Adamska-Sałaciak, A., and others (2016). *A Critique of the Controlled Defining Vocabulary in Longman Dictionary of Contemporary English*. ResearchGate.
- Hanks, P. (ed.) (1979, 2004). Work on the Collins English Dictionary and dictionary computing.
- Herbst, T. (1996). "On the way to the perfect learner's dictionary." *International Journal of Lexicography* 9(4).
- Nation, I. S. P. (2001, 2013). *Learning Vocabulary in Another Language*. Cambridge University Press.
- Ogden, C. K. (1930). *Basic English: A General Introduction with Rules and Grammar.* Paul Treber & Co.
- Procter, P. (ed.) (1978). *Longman Dictionary of Contemporary English*, 1st edition. Longman.
- Rundell, M. (2008). "More than one way to skin a cat: why full-sentence definitions have not been universally adopted." *Proceedings of EURALEX 2008.*
- Sinclair, J. M. (ed.) (1987). *Collins COBUILD English Language Dictionary.* Collins.
- West, M. (1953). *A General Service List of English Words.* Longman.

## Related pages

- [Vocabulary Tier System](../project/vocabulary-tiers.md) — je-dict-1's tiered analogue of a defining vocabulary
- [Learner Lexicography](learner-lexicography.md) — the broader tradition of pedagogical dictionary design
- [Definition and Gloss Strategies](definition-strategies.md) — equivalence types and gloss-writing techniques
- [Vocabulary Acquisition](vocabulary-acquisition.md) — the receptive/productive thresholds that CDVs target
- [Vocabulary Size and Text Coverage](vocabulary-size-coverage.md) — the text coverage thresholds that CDVs target
- [Corpus Linguistics](corpus-linguistics.md) — frequency-based word selection, which underlies all modern CDVs
- [Entry Design](../project/entry-design.md) — the required-fields structure into which notes (and thus CDV-controlled prose) fit
- [Vocabulary Learning Strategies](vocabulary-learning-strategies.md) — how the tier system supports selective attention and planning strategies
- [History of Japanese-English Dictionaries](je-dictionary-history.md) — historical context for the CDV approach in JE lexicography
- [Bilingual vs. Monolingual Dictionary Debate](bilingual-monolingual-debate.md) — the CDV as an inherently monolingual concept, and why bilingual dictionaries don't need one
