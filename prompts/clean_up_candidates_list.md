# Clean Up Candidates List Prompt

Review candidate_words.json by evaluating each entry one at a time to determine whether it would be suitable for adding to this Japanese-English dictionary.

## Background

The file `candidate_words.json` contains a list of candidate words that may be added to the dictionary in the future. Some entries are legitimate dictionary words, while others are problematic (verb stems, incomplete compounds, extraction artifacts, etc.). Your task is to evaluate each entry using your knowledge of Japanese to determine its suitability.

## Workflow

### Step 1: Read Candidates

Read the candidate list and start from the beginning (or continue from where you left off, if the user specifies):

```bash
python3 -c "
import json
with open('candidate_words.json') as f:
    d = json.load(f)
print(f'Total candidates: {d[\"metadata\"][\"total_candidates\"]}')
for c in d['candidates'][:20]:
    print(f'  {c[\"id\"]}: {c[\"word\"]} ({c[\"reading\"]}) — {c.get(\"notes\", \"\")[:50]}')
"
```

### Step 2: Evaluate Each Entry

For each candidate, evaluate:

1. **Is this a complete, standalone Japanese word?**
   - Can it appear independently in a sentence?
   - Would a standard Japanese dictionary include it as a headword?

2. **Is the reading correct and complete?**
   - Does the reading match the word?
   - Is it a complete reading, not truncated?

3. **Is the word/reading combination valid?**
   - Does this kanji actually have this reading in standard usage?
   - Is this a legitimate word form, not just a stem?

4. **Would this be useful in a Japanese-English dictionary?**
   - Is it a word learners would look up?
   - Does it have meaningful content to define?

### Step 3: Categorize and Act

For each entry, decide:

- **KEEP**: Valid dictionary word with correct reading — leave it in the list
- **REMOVE**: Problematic entry — remove by candidate ID:
  ```bash
  python3 build/manage_candidates.py remove C00123 C00456
  ```
- **UNCERTAIN**: Note it for human review at the end

**Note (2026-08-11):** the queue was fully cleaned on this date (the
corpus-harvest junk was archived to
`planning/archive/candidate-cleanup-2026-08-11.json`) and now holds only
words vetted by the `find-candidates` gates, so this prompt should rarely
find anything to remove. It remains useful as an occasional audit.

### Examples of Evaluation Reasoning

**Example 1: 不 (ふ)**
- Evaluation: This is the negative prefix un-/non-. It's a productive prefix that learners need to understand.
- Decision: KEEP

**Example 2: 伝 (つた)**
- Evaluation: This is the verb stem of 伝える (つたえる) or 伝わる (つたわる). It cannot stand alone as a word.
- Decision: REMOVE

**Example 3: お土産 (おみやげ)**
- Evaluation: Complete noun meaning "souvenir." Standard dictionary word.
- Decision: KEEP

**Example 4: お互 (おたが)**
- Evaluation: Incomplete form of お互い (おたがい). The い is missing.
- Decision: REMOVE

## Decision Guidelines

When evaluating each entry, ask yourself:

1. **Standalone test**: Can this word appear alone in a Japanese sentence with this reading?
2. **Dictionary test**: Would you expect to find this as a headword in a published Japanese-English dictionary?
3. **Completeness test**: Is the word complete? (Not a verb stem missing okurigana, not a compound missing its ending)
4. **Reading validity test**: Is this a real, standard reading for this word?
5. **Usefulness test**: Would a Japanese learner benefit from having this entry?

## When to Stop

Process all candidates, or stop when the user requests. Before stopping, always:
1. Report how many entries you evaluated
2. Report your decisions (how many kept, removed, uncertain)
3. List uncertain entries for human review

## Reporting

At the end, report:
1. Number of entries evaluated
2. Breakdown: kept / removed / uncertain
3. List of entries removed with brief reasons
4. List of uncertain entries for human review
