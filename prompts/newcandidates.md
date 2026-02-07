# New Candidate Words Prompt

Add new candidates to candidate_words.json using the find-candidates skill.

## Quick Context

- The dictionary currently has ~9,000 entries
- Check candidate count: `head -10 candidate_words.json` (shows total_candidates)
- The candidate list may be empty or small as we are rebuilding it from scratch

## Workflow

1. Load the find-candidates skill for detailed guidelines
2. Use a variety of search strategies to find balanced, diverse candidates
3. Add candidates using: `python3 build/manage_candidates.py add "漢字" "ひらがな" "brief English note"`

4. After adding all candidates, update PROJECT_STATUS.md Recent Changes section:
   - Update "Candidate words" count in Content Status section
   - Add a brief session note under Recent Changes

5. Finally, build the website:
   ```bash
   python3 build/build_flat.py        # REQUIRED for live site update
   ```

## Duplicate Prevention (AUTOMATIC)

**The `manage_candidates.py add` command AUTOMATICALLY checks for duplicates.**

### Duplicate Definition

**A word is a duplicate ONLY if BOTH the headword AND reading match exactly.**

- **Homophones** (same reading, different headword) are **NOT duplicates**
  - Example: 線香 (せんこう) and 先行 (せんこう) are different words
- **Homographs** (same headword, different reading) are **NOT duplicates**
  - Example: 行く (いく) and 行く (ゆく) are different readings

The script will:
1. Check `entries_index.json` for exact match (both headword AND reading)
2. Check `candidate_words.json` for exact match (both word AND reading)
3. **REFUSE to add ONLY if an exact match is found**
4. Display informational notes about homophones/homographs (not blocks)

### Near-Duplicates (Editorial Consideration)
These patterns require editorial judgment - the automatic check won't catch them:
- **Verb forms**: する verbs may exist as standalone nouns (勉強 vs 勉強する)
- **Kanji variants**: 見る and 観る, 聞く and 聴く - may share an entry
- **Okurigana variations**: 行なう vs 行う, 現われる vs 現れる - same word, different spellings
- **Prefix/suffix forms**: Check if 大～ or ～的 forms warrant separate entries

## Selection Approach

### Quality Over Quantity

The basic and core vocabulary tiers are complete. Focus on finding high-quality candidates for the general tier:
- **Individually vet each candidate** - avoid bulk extraction approaches
- **Use verified sources** - frequency lists, JLPT vocabulary, textbook lists
- **When in doubt, skip** - better to miss a word than add an inappropriate one

### Balanced Coverage

Use a variety of strategies from the find-candidates skill:
- External vocabulary list cross-reference (JLPT, textbooks, frequency dictionaries)
- Practical situation vocabulary
- Media and cultural vocabulary
- Corpus-driven gap analysis (frequency-based)
- Collocational mining (words that go with existing entries)
- Register/formality pairs
- Semantic domain exploration (choose domains creatively)
- Productive pattern completion
- Written vs spoken balance

### Key Principles

- **Quality over quantity:** Each candidate should be carefully evaluated
- **Breadth over depth:** Cover many domains rather than going deep in a few
- **Creative variety:** Each session should explore different areas
- **Learner utility:** Focus on words intermediate-to-advanced learners would benefit from
- **Stable vocabulary:** Avoid ephemeral slang, archaic terms, or highly specialized jargon

## Selection Criteria

**Must NOT be:**
- Proper nouns (place names, personal names, brand names)
- Highly ephemeral slang
- Vulgar or discriminatory language
- Extremely specialized technical jargon

**Should BE:**
- Words appropriate for the general tier (intermediate-to-advanced vocabulary)
- Semantically related to existing entries
- Modern terms with widespread, stable usage
- Useful informal expressions learners need to understand
- Vocabulary that fills genuine gaps in the dictionary's coverage

## Output Format

After adding candidates, report:
1. Number of words added
2. Summary of categories/sources covered (emphasize variety)
3. Notable gaps identified for future sessions
