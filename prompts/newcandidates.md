# New Candidate Words Prompt

Add 100 new candidates to candidate_words.json using the find-candidates skill.

## Quick Context

- Check current state: `head -10 candidate_words.json` (shows total_candidates and next_id)
- Check entry count: `head -5 entries_index.json` (shows total_entries in metadata)

## Workflow

1. Load the find-candidates skill for detailed guidelines
2. Use a variety of search strategies to find balanced, diverse candidates
3. Add candidates using: `python3 build/manage_candidates.py add "漢字" "ひらがな" "brief English note"`

4. After adding all candidates, update PROJECT_STATUS.md:
   - Update "Candidate words" count in Content Status section
   - Add a brief session note under Recent Changes

5. Finally, build the website:
   ```bash
   python3 build/build_flat.py        # REQUIRED for live site update
   ```

## Duplicate Prevention (AUTOMATIC)

**The `manage_candidates.py add` command AUTOMATICALLY checks for duplicates.**

The script will:
1. Check `entries_index.json` for matching reading or headword
2. Check `candidate_words.json` for matching reading or word
3. **REFUSE to add the word if any match is found**

### Near-Duplicates to Watch For
The automatic check catches exact matches. You should still watch for:
- **Verb forms**: する verbs may exist as standalone nouns (勉強 vs 勉強する)
- **Kanji variants**: 見る and 観る, 聞く and 聴く
- **Okurigana variations**: 行なう vs 行う, 現われる vs 現れる
- **Prefix/suffix forms**: Check if 大～ or ～的 forms exist separately

## Selection Approach

### Priority 1: Basic and Core Vocabulary Completeness

Before adding specialized vocabulary, ensure the basic and core tiers are complete:
- **Basic tier (600-800 words):** Fundamental vocabulary every learner needs
- **Core tier (1600-2000 words):** Vocabulary expected of any adult using Japanese

Check for missing function words, demonstratives, numbers, counters, time expressions, body parts, family terms, colors, directions, core verbs, essential adjectives, and common adverbs.

### Priority 2: Balanced Coverage

Use a variety of strategies from the find-candidates skill:
- Corpus-driven gap analysis (frequency-based)
- Collocational mining (words that go with existing entries)
- Register/formality pairs
- Semantic domain exploration (choose domains creatively)
- Productive pattern completion
- Cross-reference expansion
- Written vs spoken balance

### Key Principles

- **Breadth over depth:** Cover many domains rather than going deep in a few
- **Creative variety:** Each session should explore different areas
- **Learner utility:** Focus on words intermediate learners would benefit from
- **Stable vocabulary:** Avoid ephemeral slang or highly specialized jargon

## Selection Criteria

**Must NOT be:**
- Proper nouns (place names, personal names, brand names)
- Highly ephemeral slang
- Vulgar or discriminatory language
- Extremely specialized technical jargon

**Should BE:**
- Words appropriate for the three-tier vocabulary system (basic, core, or general tier)
- Semantically related to existing entries
- Modern terms with widespread, stable usage
- Useful informal expressions learners need to understand

## Output Format

After adding candidates, report:
1. Number of words added
2. Summary of categories/sources covered (emphasize variety)
3. Notable gaps identified for future sessions
