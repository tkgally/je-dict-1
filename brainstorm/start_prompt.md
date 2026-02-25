# LLM Brainstorming Pipeline for Dictionary Candidates

Run the brainstorming pipeline to discover candidate words for the dictionary using an external LLM via OpenRouter.

## How it works

The pipeline selects batches of seed words from `brainstorm/entries_and_candidates_for_LLM_brainstorming.json`, sends them to an LLM, and collects related word suggestions. Suggestions are programmatically filtered against all existing entries and candidates, deduplicated against previous runs, and saved to an output file.

## Prerequisites

Before running, ensure:
1. `brainstorm/entries_and_candidates_for_LLM_brainstorming.json` exists (copy from `prompts/` if needed)
2. `brainstorm/config.json` exists and has your OpenRouter API key and model name filled in (copy from `config.example.json` if needed)

## Steps

### 1. Check current status

```bash
python3 brainstorm/llm_brainstorm.py --stats
```

Report the statistics: total entries, checked/unchecked counts, and any existing output files.

### 2. Run the pipeline

Run batches. Start with a small number to verify things work, then scale up:

```bash
# Run 5 batches (each batch = 15 seed words, generating ~75-225 candidate suggestions)
python3 brainstorm/llm_brainstorm.py -n 5
```

For a longer session:

```bash
# Run 20 batches
python3 brainstorm/llm_brainstorm.py -n 20
```

Monitor the output. For each batch the script reports:
- Which seed words were selected
- How many candidates the LLM suggested
- How many survived filtering (not already in dictionary/candidates/previous output)
- The new candidates with their glosses and which seed word inspired them

### 3. Review results

After running, check the output file (`brainstorm/new_candidates_by_{model}.json`). Look for:
- **False positives**: words that are not real Japanese, are proper nouns, or are too obscure
- **Reading errors**: incorrect hiragana readings
- **Gloss quality**: glosses should be brief and accurate

If the results look problematic, consider adjusting `config.json`:
- Lower `temperature` (e.g., 0.6) for more conservative suggestions
- Increase or decrease `batch_size`
- Try a different model

### 4. Show final statistics

```bash
python3 brainstorm/llm_brainstorm.py --stats
```

### 5. Report to user

Summarize:
- How many batches were run
- How many new candidates were collected
- The overall checked/unchecked ratio
- Any quality observations about the LLM's suggestions

## Configuration reference

`brainstorm/config.json` fields:

| Field | Description |
|-------|-------------|
| `openrouter_api_key` | Your OpenRouter API key |
| `model` | OpenRouter model ID (e.g., `MODEL_NAME_HERE`) |
| `temperature` | LLM temperature, 0.0-1.0 (default: 0.8) |
| `max_tokens` | Max response tokens (default: 4096) |
| `batch_size` | Number of seed words per batch (default: 15) |
| `relation_types` | Types of word relationships to explore |

## Commands reference

```bash
python3 brainstorm/llm_brainstorm.py --stats           # Show statistics
python3 brainstorm/llm_brainstorm.py -n 1              # Run 1 batch
python3 brainstorm/llm_brainstorm.py -n 10             # Run 10 batches
python3 brainstorm/llm_brainstorm.py --reset-checked   # Reset all checked flags
```

## Later: importing results into candidate_words.json

The output file is a standalone JSON file. In a separate step (not part of this pipeline), candidates from this file can be reviewed and selectively imported into `candidate_words.json` using `python3 build/manage_candidates.py add`. That import step includes its own duplicate checking.
