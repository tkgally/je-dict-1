# Manual Prompts for Claude Code for the Web

Copy-paste any of these prompts to start a task. Each one tells Claude to read the detailed instructions from the corresponding prompt file.

---

## Dictionary Building Tasks

### Create new entries (from candidates)
```
Read prompts/newentries.md and follow the instructions to create 30 new dictionary entries from candidate_words.json.
```

### Find new candidate words
```
Read prompts/newcandidates.md and follow the instructions to add new candidate words to candidate_words.json.
```

### Harvest candidates from corpus
```
Read prompts/corpus_harvesting.md and follow the instructions to process the next batch of words from the corpus extraction file.
```

### Clean up candidate list
```
Read prompts/clean_up_candidates_list.md and follow the instructions to review and clean candidate_words.json.
```

### Create entries for noentry words
```
Read prompts/polish_add_entries_for_noentry_example_words.md and follow the instructions to create entries for words marked noentry in inline links.
```

---

## Polishing Tasks

### Add inline word links
```
Read prompts/polish_add_inline_links.md and follow the instructions to add cross-reference links to example sentences and notes.
```

### Polish example sentences
```
Read prompts/polish_example_sentences.md and follow the instructions to check and improve example sentence quality.
```

### Check furigana completeness
```
Read prompts/polish_furigana_completeness.md and follow the instructions to check for missing furigana on kanji.
```

### Check furigana correctness
```
Read prompts/polish_furigana_correctness.md and follow the instructions to verify that existing furigana readings are correct.
```

### Check semantic labels
```
Read prompts/polish_semantic_labels.md and follow the instructions to verify semantic tags are accurate.
```

### Expand short notes
```
Read prompts/expand-short-notes.md and follow the instructions to expand the notes field for entries with inadequate notes.
```

---

## Project Health & Planning

### Get task recommendations
```
Run python3 pipeline/recommend-tasks.py and show me the output. This tells us what the dictionary needs most right now.
```

### Run health dashboard
```
Run make report and show me the output. This gives an overview of dictionary statistics and quality metrics.
```

### Validate all entries
```
Run make validate and show me the results.
```

### Full site build
```
Run make build to validate entries, update indexes, and rebuild the static site.
```

### Incremental site build
```
Run make quick to validate entries, update indexes, and rebuild only changed entries.
```

### Check project context
```
Read PROJECT_CONTEXT_BRIEF.md and summarize the current state of the dictionary.
```

---

## Maintenance & Review

### Review a specific entry
```
Read the entry file for [WORD] (use python3 build/check_duplicate.py "WORD" "READING" to find it) and evaluate its quality against the entry-guidelines skill. Suggest improvements if needed.
```

### Check for duplicates
```
Run python3 build/check_duplicate.py "WORD" "READING" to check whether a word already exists in the dictionary or candidate list.
```

### Verify furigana for one entry
```
Run python3 build/verify_furigana.py ENTRY_ID and show me the results.
```

### Update indexes after manual edits
```
Run python3 build/update_indexes.py to sync entries_index.json, candidate_words.json, and the word lookup table.
```

---

## Notes

- **One task per session** works best for polishing tasks — they use context tracking files to resume across sessions.
- **Entry creation** can be done in batches of 30 per session (the default).
- After any task that modifies entries, always run `make build` or `make quick` before finishing.
- The polishing tasks track progress in `polishing/tasks/{task-name}/progress.txt` — they automatically pick up where the previous session left off.
