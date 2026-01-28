# Clean Up Candidates List Prompt

Review candidate_words.json by evaluating each entry one at a time to determine whether it would be suitable for adding to this Japanese-English dictionary.

## Background

The file `candidate_words.json` contains a list of candidate words that may be added to the dictionary in the future. Some entries are legitimate dictionary words, while others are problematic (verb stems, incomplete compounds, extraction artifacts, etc.). Your task is to evaluate each entry using your knowledge of Japanese to determine its suitability.

## Evaluation Process

### Step 1: Load and Track Progress

First, check the current state of your progress file:

```bash
cat cleanup_progress.json 2>/dev/null || echo '{"last_evaluated_index": 0, "removed": [], "kept": [], "uncertain": []}'
```

If starting fresh, create the progress file:

```python
import json

progress = {
    "last_evaluated_index": 0,
    "removed": [],
    "kept": [],
    "uncertain": []
}

with open('cleanup_progress.json', 'w') as f:
    json.dump(progress, f, indent=2)
```

### Step 2: Entry-by-Entry Evaluation

Go through the candidates array starting from where you left off. For each entry, evaluate:

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

### Step 3: Categorize Each Entry

For each entry, decide:

- **KEEP**: Valid dictionary word with correct reading
- **REMOVE**: Problematic entry (stem, fragment, error, duplicate concept)
- **UNCERTAIN**: Needs human review

### Examples of Evaluation Reasoning

**Example 1: 不 (ふ)**
- Evaluation: This is the negative prefix un-/non-. It's a productive prefix that learners need to understand.
- Decision: KEEP

**Example 2: 伝 (つた)** (if present)
- Evaluation: This is the verb stem of 伝える (つたえる) or 伝わる (つたわる). It cannot stand alone as a word.
- Decision: REMOVE

**Example 3: お土産 (おみやげ)**
- Evaluation: Complete noun meaning "souvenir." Standard dictionary word.
- Decision: KEEP

**Example 4: お互 (おたが)** (if present)
- Evaluation: Incomplete form of お互い (おたがい). The い is missing.
- Decision: REMOVE

### Step 4: Process Entries

For each entry you evaluate, record your decision in the progress file. Continue evaluating entries one by one until your remaining context falls below 20%.

Use this structure to track decisions:

```python
import json

# Load current state
with open('candidate_words.json', 'r') as f:
    data = json.load(f)

with open('cleanup_progress.json', 'r') as f:
    progress = json.load(f)

# Get next entry to evaluate
idx = progress['last_evaluated_index']
entry = data['candidates'][idx]

print(f"Entry {idx}: {entry['word']} ({entry['reading']})")
print(f"Notes: {entry.get('notes', 'none')}")
print(f"ID: {entry['id']}")
```

After evaluating, update progress:

```python
# After deciding on an entry
progress['last_evaluated_index'] = idx + 1

# Record decision (use appropriate list)
progress['kept'].append(entry['id'])  # or 'removed' or 'uncertain'

with open('cleanup_progress.json', 'w') as f:
    json.dump(progress, f, indent=2)
```

### Step 5: Apply Removals

When ready to apply changes, remove entries marked for removal:

```python
import json
from datetime import datetime, timezone

with open('candidate_words.json', 'r') as f:
    data = json.load(f)

with open('cleanup_progress.json', 'r') as f:
    progress = json.load(f)

# Get IDs to remove
remove_ids = set(progress['removed'])

# Filter candidates
original_count = len(data['candidates'])
data['candidates'] = [c for c in data['candidates'] if c['id'] not in remove_ids]
new_count = len(data['candidates'])

# Update metadata
data['metadata']['total_candidates'] = new_count
data['metadata']['last_updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

# Save
with open('candidate_words.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Removed {original_count - new_count} entries")
print(f"New total: {new_count} candidates")
```

### Step 6: Validate JSON

After editing, verify the file is valid:

```bash
python3 -c "import json; json.load(open('candidate_words.json'))" && echo "Valid JSON"
```

## Decision Guidelines

When evaluating each entry, ask yourself:

1. **Standalone test**: Can this word appear alone in a Japanese sentence with this reading?

2. **Dictionary test**: Would you expect to find this as a headword in a published Japanese-English dictionary?

3. **Completeness test**: Is the word complete? (Not a verb stem missing okurigana, not a compound missing its ending)

4. **Reading validity test**: Is this a real, standard reading for this word?

5. **Usefulness test**: Would a Japanese learner benefit from having this entry?

## When to Stop

Continue evaluating entries one by one until:
- Your remaining context drops below 20%, OR
- You complete all entries

Before stopping, always:
1. Save your progress to cleanup_progress.json
2. Report how many entries you evaluated in this session
3. Report your decisions (how many kept, removed, uncertain)

## Reporting

At the end of each session, report:
1. Starting index and ending index for this session
2. Number of entries evaluated
3. Breakdown: kept / removed / uncertain
4. List of entries marked for removal with brief reasons
5. List of uncertain entries for human review
6. Next steps (continue from index X, or apply removals if done)
