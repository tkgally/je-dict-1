# Corpus Harvesting Prompt

Process words from `prompts/corpus_extracted_words.json` to find suitable candidates for the dictionary.

## Instructions

1. **Read the starting point**: Check `prompts/corpus_harvesting_next_entry_number.txt` to find where to start.

2. **Determine batch size**: Use the target number specified by the user. If none is specified, process **500 entries**.

3. **Process each entry one by one**:
   - Read the word and its example sentence from `corpus_extracted_words.json`
   - The example sentence shows how the word appeared in a corpus (web texts and LLM-written texts) - use it as reference for understanding the meaning
   - Rely primarily on your own linguistic knowledge when deciding whether to add the word

4. **For each word, evaluate against these criteria**:

   **EXCLUDE if any of these apply:**
   - Already in `entries_index.json` (check using `python3 build/manage_candidates.py check "word" "reading"`)
   - Already in `candidate_words.json`
   - Is a proper noun (place names, personal names, company names, etc.)
   - Is a number or numeric expression (1人, 2度, 3日, etc.)
   - Is a highly ephemeral slang term
   - Is vulgar or discriminatory
   - Is archaic or dialect-specific
   - Is a technical abbreviation or brand name (JR東日本, ICカード, etc.)
   - Is a single kana character or meaningless fragment

   **INCLUDE if it meets eligibility AND at least one of these:**
   - Similar frequency/usefulness to existing dictionary entries
   - Is a common synonym, antonym, or semantically related word to existing entries
   - Is a modern widespread term with stable, lasting usage
   - Is an informal/colloquial term useful for learners to understand natural speech

5. **When adding a candidate**:
   - Determine the canonical form (headword) based on your knowledge
   - Determine the correct reading (in hiragana, even for katakana words)
   - Write a brief English gloss (under 50 characters)
   - Use: `python3 build/manage_candidates.py add "headword" "reading" "gloss"`

6. **Track progress**: Keep a running count of:
   - Words evaluated
   - Words added to candidates
   - Words skipped (and general reasons)

7. **After finishing the batch**:
   - Update `prompts/corpus_harvesting_next_entry_number.txt` with the next entry number to process
   - Report a summary: total evaluated, added, skipped (with breakdown by reason)

## Example Workflow

```
Starting at entry 1, processing 500 entries...

Entry 1: "1人" - SKIP (numeric expression)
Entry 2: "1度" - SKIP (numeric expression)
...
Entry 15: "ああ" - Check if in dictionary... Already exists, SKIP
Entry 16: "あいだ" - Check if in dictionary... Already exists as 間, SKIP
Entry 17: "あいにく" - Check if in dictionary... Not found.
  Evaluating: Common adverb meaning "unfortunately"
  Adding: python3 build/manage_candidates.py add "あいにく" "あいにく" "unfortunately, unluckily"
...
```

## Important Notes

- Use `python3 build/manage_candidates.py check "word" "reading"` to verify duplicates before adding
- The manage_candidates.py script will automatically reject duplicates, but checking first is more efficient
- Readings must always be in hiragana (e.g., "すきー" not "スキー")
- Be conservative - when in doubt, skip. Quality over quantity.
- Focus on words that intermediate-to-advanced learners would genuinely benefit from knowing
