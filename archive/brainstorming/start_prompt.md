# LLM Brainstorming Pipeline for Dictionary Candidates

## About this project

This pipeline is part of **je-dict-1**, a Japanese-English learner's dictionary targeting intermediate learners who can read kana and are building vocabulary. The live site is at [https://www.tkgje.jp/](https://www.tkgje.jp/). It is a completely static site with over 17,500 entries as of March 2026.

The dictionary uses a three-tier vocabulary system:

- **Basic** (~800 entries) — foundational day-one words; tier is closed

- **Core** (~2,000 entries) — essential adult communication words; tier is closed

- **General** (17,000+ entries, growing) — all other vocabulary; all new entries go here

This brainstorming pipeline runs **independently** of the main dictionary repository. Its job is to discover candidate words that may be missing from the dictionary by using LLMs to explore semantic neighborhoods of existing entries.

## How the pipeline works

1. The script selects a batch of **seed words** (default 15) from `entries\_and\_candidates\_for\_LLM\_brainstorming\_new.json` — a flat JSON array of all current dictionary entries and candidate words (19,591 as of March 2026), each with `headword`, `reading`, `gloss`, and `checked` fields.

2. It sends the seed words to an external LLM via **OpenRouter**, asking it to brainstorm related Japanese words.

3. The LLM's suggestions are **programmatically filtered** against the full entries/candidates list (exact match on headword+reading pair) — the LLM never needs to search the list itself.

4. Suggestions are **deduplicated** against previous runs' output.

5. Survivors are saved to `new\_candidates\_by\_\{model\}.json` with provenance (which seed inspired each suggestion, which run produced it).

6. Seed words are marked `"checked": 1` so they won't be selected again.

## Word selection criteria

The LLM prompt asks for words that meet **all** of these:

**Include a word only if:**

- It is a real, commonly used Japanese word (not archaic, dialect-only, or highly technical)

- It would be useful for an intermediate-to-advanced Japanese learner

- It is stable vocabulary (not ephemeral slang or trendy internet terms)

- If it is a proper noun, it is collocationally/semantically rich and known to every Japanese speaker (major place names, canonical historical figures, key organizations — see the find-candidates skill's proper-noun criteria); merely referential names do not qualify

- It is a single lexical item (not a full sentence or long phrase)

**Exclude:**

- Proper nouns of any kind (places, people, brands, specific events or works)

- Highly specialized jargon (medical codes, legal statutes, chemistry nomenclature)

- Archaic or dialect-only terms that most modern Japanese speakers would not know

- Ephemeral slang or internet-only coinages without lasting usage

- Vulgar or discriminatory language

- Long fixed phrases or full sentences (single lexical items only)

**Prefer words that have at least one of these qualities:**

- Similar frequency/centrality to words already in the dictionary

- Semantic relation to existing entries (synonyms, antonyms, same category)

- Modern widespread terms with established, lasting usage

- Informal/colloquial terms commonly encountered in everyday Japanese

**Types of relationships to explore from seed words:**

- Synonyms and near-synonyms (same meaning, different register or nuance)

- Antonyms (direct opposites)

- Same semantic field (words in the same category)

- Same-kanji compounds (other common words using the same kanji)

- Register variants (formal/informal pairs, written/spoken variants)

- Collocational partners (words that naturally pair with the seed)

- Situationally related (words a learner would need in the same context)

**Output format from the LLM:**

- `headword`: the word as normally written (kanji + kana as appropriate)

- `reading`: the full reading in **hiragana** (must be hiragana, never katakana)

- `gloss`: a brief English meaning (2-8 words)

- `seed`: the headword of the seed word that inspired the suggestion

## Prerequisites

Before running, ensure:

1. `entries\_and\_candidates\_for\_LLM\_brainstorming\_new.json` exists in this directory

2. `config.json` exists and has your OpenRouter API key and model name filled in (copy from `config.example.json` if needed)

3. The `requests` Python library is installed (`pip install requests`)

## Steps

### 1. Check current status

```
python3 llm\_brainstorm.py --stats
```

Report the statistics: total entries, checked/unchecked counts, and any existing output files.

### 2. Run the pipeline

Run batches. Start with a small number to verify things work, then scale up:

```
\# Run 5 batches (each batch = 15 seed words, generating ~75-225 candidate suggestions)  
python3 llm\_brainstorm.py -n 5
```

For a longer session:

```
\# Run 20 batches  
python3 llm\_brainstorm.py -n 20
```

Monitor the output. For each batch the script reports:

- Which seed words were selected

- How many candidates the LLM suggested

- How many survived filtering (not already in dictionary/candidates/previous output)

- The new candidates with their glosses and which seed word inspired them

### 3. Review results

After running, check the output file (`new\_candidates\_by\_\{model\}.json`). Look for:

- **False positives**: words that are not real Japanese, are proper nouns, or are too obscure

- **Reading errors**: incorrect hiragana readings

- **Gloss quality**: glosses should be brief and accurate

If the results look problematic, consider adjusting `config.json`:

- Lower `temperature` (e.g., 0.6) for more conservative suggestions

- Increase or decrease `batch\_size`

- Try a different model

### 4. Show final statistics

```
python3 llm\_brainstorm.py --stats
```

### 5. Report to user

Summarize:

- How many batches were run

- How many new candidates were collected

- The overall checked/unchecked ratio

- Any quality observations about the LLM's suggestions

## Configuration reference

`config.json` fields:

| Field | Description |
| - | - |
| `openrouter\_api\_key` | Your OpenRouter API key |
| `model` | OpenRouter model ID (e.g., `google/gemini-2.0-flash-001`) |
| `temperature` | LLM temperature, 0.0-1.0 (default: 0.8) |
| `max\_tokens` | Max response tokens (default: 4096) |
| `batch\_size` | Number of seed words per batch (default: 15) |
| `relation\_types` | Types of word relationships to explore |


## Commands reference

```
python3 llm\_brainstorm.py --stats           \# Show statistics  
python3 llm\_brainstorm.py -n 1              \# Run 1 batch  
python3 llm\_brainstorm.py -n 10             \# Run 10 batches  
python3 llm\_brainstorm.py --reset-checked   \# Reset all checked flags
```

## Later: importing results into candidate\_words.json

The output file is a standalone JSON file. In a separate step (not part of this pipeline), candidates from this file can be reviewed and selectively imported into the main dictionary's `candidate\_words.json` using `python3 build/manage\_candidates.py add`. That import step includes its own duplicate checking.

