# Corpus Harvesting Prompt

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

> **DEPRECATED 2026-08-11 — do not run.** Bulk extraction from corpus text
> produced ~970 candidates of which almost none were usable (coinages, free
> phrases, inflected forms, wrong glosses); all were removed in the
> 2026-08-11 queue cleanup (`planning/archive/candidate-cleanup-2026-08-11.json`).
> Candidate discovery is now the verified-restock workflow in
> `prompts/newcandidates.md` (the Routine's `candidates` mode), built on the
> `find-candidates` skill's per-word vetting gates. This file is kept only as
> a record of the old procedure.

Process words from `prompts/corpus_extracted_words.json` to find suitable candidates for the dictionary.

## Instructions

1. **Read the starting point**: Check `prompts/corpus_harvesting_next_entry_number.txt` to find where to start.

2. **Determine batch size**: Use the target number specified by the user. If none is specified, process **500 entries**.

3. **Load the batch and scan for candidates**:
   - Read all entries in the batch from `corpus_extracted_words.json`
   - The example sentence shows how the word appeared in a corpus (web texts and LLM-written texts) — use it as reference for understanding the meaning
   - Rely primarily on your own linguistic knowledge when deciding whether to add the word
   - Scan the full batch first to identify categories (proper nouns, numeric expressions, clearly common words, etc.) before starting to add — this is much more efficient than true one-by-one processing

4. **For each word, evaluate against these criteria**:

   **EXCLUDE if any of these apply:**
   - Is a proper noun (place names, personal names, company names, era names, etc.)
   - Is a number or numeric expression (1人, 2度, 3日, etc.)
   - Is a highly ephemeral slang term
   - Is vulgar or discriminatory
   - Is archaic or dialect-specific
   - Is a technical abbreviation or brand name (JR東日本, ICカード, etc.)
   - Is a single kana character or meaningless fragment
   - Is a predictable compound or inflected form of a more basic word (e.g., skip 決め方 if 決める exists; skip potential forms like 泳げる)
   - Is too specialized for a general learner's dictionary (medical terms, scientific jargon, etc.)

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
   - **Do NOT pre-check with `manage_candidates.py check`** — the `add` command already has built-in duplicate detection that is more thorough (checks both headword and reading against entries and candidates). Pre-checking wastes time.
   - When chaining multiple `add` commands, use `;` (not `&&`) to separate them, since `add` exits with code 1 on duplicates and `&&` would abort the chain

6. **Track progress**: Keep a running count of:
   - Words evaluated
   - Words added to candidates
   - Words skipped (and general reasons)

7. **After finishing the batch**:
   - Update `prompts/corpus_harvesting_next_entry_number.txt` with the next entry number to process
   - Report a summary: total evaluated, added, skipped (with breakdown by reason)

## Efficient Workflow

The corpus is sorted by kanji radical, so entries come in clusters (all 気~ words together, all 水~ words together, etc.). Many will be common words already in the 12,000+ entry dictionary. **Expect roughly 15–25% of evaluated words to be new candidates**; the rest will be proper nouns, duplicates, or otherwise excluded.

### Recommended approach:

1. **Load the full batch** into context
2. **Triage by category** — mentally group entries into: proper nouns (skip), numeric expressions (skip), obvious candidates (add), words that need checking (evaluate)
3. **Batch-add candidates in groups** of 10–20 using `;`-separated commands:
   ```
   python3 build/manage_candidates.py add "word1" "reading1" "gloss1" ; \
   python3 build/manage_candidates.py add "word2" "reading2" "gloss2" ; \
   ...
   ```
4. **Let the `add` command handle duplicate detection** — don't worry about duplicates; the script will reject them and print which entry already exists. This is normal and expected.

### Example:

```
Starting at entry 1, processing 500 entries...

Scanning batch: entries 1-500
- Entries 1-14: numeric expressions (1人, 1度, 1日, ...) → SKIP all
- Entry 15: ああ → common interjection, try to add
- Entry 16: あいだ → common word, try to add
- Entry 17: あいにく → common adverb, try to add
...

Batch adding:
  python3 build/manage_candidates.py add "ああ" "ああ" "ah, oh (interjection)" ; \
  python3 build/manage_candidates.py add "あいにく" "あいにく" "unfortunately, unluckily" ; \
  ...

Results: ああ → duplicate (already exists as entry 00123), あいにく → added as C03500
```

## Important Notes

- Readings must always be in hiragana (e.g., "すきー" not "スキー")
- Be conservative — when in doubt, skip. Quality over quantity.
- Focus on words that intermediate-to-advanced learners would genuinely benefit from knowing
- When a word appears in both kanji and kana variants in the corpus (e.g., 気付く / 気づく), add only the more standard form
