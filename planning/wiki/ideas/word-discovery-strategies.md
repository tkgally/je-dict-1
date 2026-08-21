# Word Discovery Strategies

**Last updated**: 2026-04-08

## Overview

A learner's dictionary must actively discover words to add. Unlike a traditional dictionary that draws from a fixed corpus, je-dict-1 uses multiple strategies to find candidate words — with LLM-based brainstorming now serving as the primary method. This page analyzes the strengths and weaknesses of each approach and proposes new ideas for ensuring comprehensive coverage.

## Current primary method: LLM brainstorming

The `brainstorm-new-candidates.md` prompt drives an automated pipeline that:
1. Selects random seed words from the existing dictionary
2. Sends them to an external LLM (via OpenRouter) with prompts to suggest related missing words
3. Filters results through deduplication against existing entries and candidates
4. Adds survivors to `candidate_words.json`

The system explores seven relation types: synonyms/near-synonyms, antonyms, same semantic field, same-kanji compounds, register variants, collocational partners, and situationally related words.

### Strengths

- **High throughput**: Can generate hundreds of candidates per session with minimal human effort
- **Semantic connectivity**: By radiating outward from existing words, it naturally discovers words in the same domains — filling gaps that a learner would notice
- **Register awareness**: The relation types include formal/informal variants, catching words that frequency lists might miss (e.g., humble/honorific pairs)
- **Low cost**: Uses a cost-efficient model (gpt-4.1-mini) via OpenRouter; effectively free at scale
- **Self-improving coverage**: As the dictionary grows, the seed pool becomes richer, which means brainstorming reaches into more diverse territory
- **No external wordlist comparison needed**: Avoids the policy constraint against comparing headwords to existing dictionaries or word lists

### Weaknesses

- **Semantic clustering bias**: Words found by radiating from existing entries tend to cluster in well-represented semantic fields. If a whole domain is missing (e.g., fishing vocabulary, legal terms), brainstorming from unrelated seeds won't discover it
- **LLM knowledge gaps**: The brainstorming LLM may have blind spots — rare but important words that don't surface in LLM training data
- **"More of the same" tendency**: The method excels at filling in gaps near existing coverage but is weak at discovering entirely new categories of words
- **No frequency signal**: Suggestions aren't ranked by how common the word actually is. A rare literary word and an everyday word get equal treatment
- **Seed exhaustion**: Once all entries have been used as seeds (tracked in `checked_seeds.json`), the cycle restarts but may produce diminishing returns

### Mitigation strategies already in place

- Deduplication filters (exact + fuzzy) prevent waste
- Seed tracking ensures broad coverage of the existing dictionary as seeds
- Seven diverse relation types help avoid narrow clustering

## Previous method: Corpus harvesting

The `corpus_harvesting.md` prompt processes frequency-ranked word lists and checks each against the dictionary. This was the initial approach but was largely superseded by brainstorming.

### Strengths
- Frequency-ordered: ensures the most common words are considered first
- Systematic: no word in the list is skipped
- Grounded in real usage data

### Weaknesses
- Slow: each word requires individual checking
- Corpus-dependent: quality of results depends on corpus quality and genre balance
- Many false positives: proper nouns, inflected forms, and function words dominate frequency lists
- Requires manual curation of the frequency source

## Ideas for additional discovery methods

### 1. Scenario-based gap analysis

Instead of starting from words, start from **situations** a learner might encounter: visiting a doctor, renting an apartment, attending a wedding, using public transportation, etc. For each scenario, ask an LLM to list the vocabulary needed — then check which words are missing from the dictionary.

**Why this helps**: It discovers words by communicative need rather than semantic association. A scenario like "reporting a plumbing problem to a landlord" would surface domain-specific vocabulary (水漏れ, 修理, 大家) that brainstorming from unrelated seeds might never reach.

**Implementation**: Create a list of 100-200 common life scenarios. For each, generate a vocabulary list and cross-check against entries. This could be automated similarly to the brainstorming pipeline.

### 2. Textbook and course syllabus mining

Without directly comparing to other dictionaries' wordlists (which is against project policy), we can review the **topic areas** covered by major Japanese textbook series (Genki, Minna no Nihongo, Tobira, etc.) and ensure the dictionary covers vocabulary for those domains. The check is at the topic/domain level, not word-for-word comparison.

**Why this helps**: Textbooks are designed around learner needs. If Genki covers hospital vocabulary in Chapter 12, we should have good coverage of medical terms — even if we don't compare individual words.

### 3. "What would you look up?" user simulation

Prompt an LLM to simulate being a learner at various levels and generate lists of "words I would want to look up while reading/watching/listening to X" — where X is a newspaper article, an anime, a business email, a recipe, etc.

**Why this helps**: Shifts perspective from "what words exist" to "what words do learners need." Can uncover practical vocabulary (e.g., cooking verbs, email closings) that other methods miss.

### 4. Reverse cross-reference mining

Scan all existing entry notes and examples for Japanese words that are mentioned but don't have their own entries and aren't already candidates. The `noentry` inline link detection already does a version of this, but a broader scan of unlinked Japanese text in notes could find more.

**Why this helps**: Words mentioned in notes are often important related vocabulary — if we explain that X is different from Y, but Y has no entry, that's a gap.

### 5. Kanji productivity analysis

For each kanji that appears in multiple entries, generate all common compounds using that kanji and check which ones are missing. For example, if 教 appears in 教える, 教室, 教師, check whether 教育, 教科書, 教会 etc. are also covered.

**Why this helps**: Kanji compounds are highly productive in Japanese. Learners who know one compound with a kanji often look up others. This ensures the dictionary provides good coverage of common compound families.

### 6. Semantic field audits

Periodically audit specific semantic fields for completeness. Pick a domain (colors, body parts, weather, emotions, family terms, etc.) and systematically verify that all words a learner would expect are present. This can be done without comparing to other dictionaries — just by reasoning about what belongs in the field.

**Why this helps**: Directly addresses the fear of missing "obvious" words. If the colors section is missing 灰色 (grey), that's embarrassing regardless of what any other dictionary contains.

### 7. Learner error analysis

Review common learner mistakes documented in SLA research and teaching materials. Words that learners frequently confuse, misuse, or fail to distinguish are high-priority dictionary entries. For example, if learners commonly confuse 届ける and 届く, both should have entries with contrastive notes.

**Why this helps**: Aligns the dictionary with actual learning difficulties rather than abstract completeness.

## Ensuring no basic or core vocabulary is missed

The user's concern about overlooking fundamental words is valid. The brainstorming method is good at finding related words but could miss isolated "obvious" ones. Recommended safeguards:

1. **Semantic field audits** (method 6 above) — systematically review basic domains
2. **Scenario-based checks** (method 1) — ensure coverage for common life situations
3. **Tier self-check**: Periodically review the basic and core tiers to verify they are genuinely complete — and check whether any general-tier entries should be promoted (see [Vocabulary Tier System](../project/vocabulary-tiers.md) for the tier reassessment note)
4. **"What's missing?" prompts**: Occasionally ask an LLM directly, "Given a dictionary of 25,000+ Japanese entries for intermediate learners, what common everyday words might still be missing?" — without providing the actual wordlist. The LLM can brainstorm based on its knowledge of what intermediate learners need
5. **Example sentence scanning**: Review example sentences across the dictionary for words used naturally but lacking entries

## Policy note: No wordlist comparison

The project policy is to avoid comparing the headword list against existing dictionaries or published word lists. This preserves the dictionary's originality and avoids copyright concerns. All discovery methods above respect this constraint by working from communicative needs, semantic reasoning, or internal dictionary analysis rather than external wordlists.

## Vetting findings from the queue itself (2026-08-21)

Three observations from the 2026-08-20 `new-entries` run all concern what should and should not
survive candidate vetting. Each was measured against the live queue during the 2026-08-21 wiki
harvest, and the measurements point in different directions.

### Technical compounds harvested from a parent entry's SIMILAR WORDS list — not a class

The run left **脂漏** (しろう, seborrhea) unclaimed, harvested from 06951 湿疹, on the grounds
that a technical dermatology term serves a learner poorly as a standalone headword. It proposed
a vetting rule skipping medical compounds harvested from a parent entry unless they stand alone
in ordinary use.

Measured: the queue holds **163 words, of which 13 carry a "seen in entry" provenance note, and
exactly one** — 脂漏 itself (C23183) — has a technical-medical gloss. There is no class here to
write a rule for; the 2026-08-11 cleanup and the current per-word gates are already keeping this
population near zero.

The single instance is still worth a decision. 脂漏 is a reasonable *entry* for a dictionary this
size, but a poor use of a `new-entries` slot while 150+ ordinary words wait. Leaving it queued
and unclaimed, as the run did, is the right handling; a rule would cost more than it saves.

### Proper-noun entries pull in a supporting tail — worth doing deliberately

The same run noted that proper-noun place entries drag in a predictable tail of ordinary
vocabulary (駅伝, 異人館, コンソメ) and that queuing those during the same run "keeps the
dictionary closing in on itself."

This is the strongest argument yet for the 2026-08-11 proper-noun policy, and it generalises
beyond place names: a proper noun is dense in collocations precisely because it sits inside a
web of ordinary words, so entering one exposes several. It belongs in the discovery-method list
above as a deliberate technique rather than a side effect — **enter a proper noun, then harvest
its supporting vocabulary in the same pass, while the context is loaded.**

### Okurigana variants keep reaching the queue

C23204 耐えがたい was claimed, found to be the kana-okurigana variant of existing entry
19680 耐え難い, removed, and the alternative spelling recorded in 19680's notes instead. This is
the recurrence of a known mechanism, already described in
[Tooling Backlog](tooling-backlog.md): candidate vetting compares (surface, reading) pairs, and
okurigana variation is exactly the case where a different surface does not imply a different
word. `check_duplicate.py` cannot see it without okurigana normalisation.

Handling it the way this run did — delete the candidate, add an orthography line to the existing
entry — is the correct outcome and is worth stating as the house rule, because it also stops the
variant being re-proposed later. The same fix closed a re-proposal loop for 04165 先程/先ほど.

## Related pages

- [Content Pipeline](../project/content-pipeline.md) — how candidates flow through the system
- [Corpus-Driven Entry Prioritization](corpus-prioritization.md) — frequency-based approaches
- [Vocabulary Tier System](../project/vocabulary-tiers.md) — tier definitions and reassessment plans
- [LLMs as Lexicographic Corpus Replacements](../topics/llms-replacing-corpora.md) — broader context for LLM use in lexicography
- [Dictionary Growth and Long-Term Vision](dictionary-growth.md) — no maximum size, future expansion plans
