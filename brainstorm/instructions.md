# LLM Brainstorming Pipeline — Setup & Usage Instructions

## Files in `brainstorm/`

| File | Purpose |
|------|---------|
| `llm_brainstorm.py` | Main pipeline script — seed selection, LLM calls, filtering, dedup |
| `config.example.json` | Template config — fill in API key and model, save as `config.json` |
| `start_prompt.md` | Instructions for future Claude Code sessions to run the pipeline |
| `.gitignore` | Keeps `config.json` (with API key) and the large data JSON out of git |

## To set up for use

1. Copy the config template: `cp brainstorm/config.example.json brainstorm/config.json`
2. Edit `brainstorm/config.json` — fill in your OpenRouter API key and model name (e.g., `google/gemini-2.0-flash-001`)
3. Ensure `brainstorm/entries_and_candidates_for_LLM_brainstorming.json` exists (copy from `prompts/` if needed; it's gitignored so it stays local)

## To run in future sessions

Point Claude Code to the prompt: "Read brainstorm/start_prompt.md and follow the instructions"

Or run the script directly:
```bash
python3 brainstorm/llm_brainstorm.py --stats    # Check status
python3 brainstorm/llm_brainstorm.py -n 5       # Run 5 batches
```

## Key design decisions

- **LLM generates freely, script filters programmatically** — the LLM never has to search the 15K-entry list
- **15 seed words per batch** — efficient use of each LLM call, configurable in config.json
- **Retry with exponential backoff** on network/server errors
- **Deduplication** across runs — the output file tracks everything, no repeated suggestions
- **Seeds marked as checked** after processing so they won't be selected again
- **Output includes provenance** — each candidate records which seed word inspired it and which run produced it
