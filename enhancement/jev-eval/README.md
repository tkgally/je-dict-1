# Jev evaluation scripts (2026-09-22)

Scripts behind `enhancement/jev-evaluation-2026-09-22.md`. They are an evaluation record,
not project tooling: nothing in the build or the Routine imports them.

Run every script from the repository root with `OPENROUTER_API_KEY` set. The scripts write
their data sets and results next to themselves (large JSON files; they are not committed).

| Script | What it does |
|---|---|
| `jevclient.py` | Minimal client for Jev through OpenRouter's decisions endpoint (`POST /api/alpha/decisions`), with a cost ledger and a thread pool. |
| `analyze.py` | AUC and precision/recall helpers. |
| `build_furigana_set.py` | 320 correct pairs, 150 pairs from entries with earlier false furigana flags, 420 injected wrong readings of six kinds. |
| `run_furigana_jev.py` | One call per pair, with and without sentence context. |
| `run_furigana_fanout.py` | One call per sentence, one question per pair (the realistic mode). |
| `run_fp_rate.py` | False-flag rate on 1,500 presumed-correct sentences (5,574 pairs). |
| `run_reading_choice.py` | Pick the right reading of a kanji string with several dictionary readings. |
| `run_furigana_gemini.py` | Gemini 2.5 Flash on the same furigana set (baseline). |
| `build_link_set.py`, `run_link_jev.py`, `run_link_gemini.py` | Kana-link homophone verdicts against `reviews/link_decisions.jsonl`. |
| `build_error_set.py`, `run_error_jev.py`, `run_error_gemini.py` | Real gloss, translation and notes errors recovered from git history (needs a deep clone: `git fetch --deepen=1500 origin main`). |
| `build_meta_set.py`, `run_meta_jev.py` | Formality, politeness, part-of-speech family, and injected wrong semantic tags. |
| `run_realtag_jev.py` | Semantic tags the reviewer actually flagged, labelled by the curator's decision (set built inline in the report session; see the report). |
| `run_sense_jev.py` | Which numbered sense an example illustrates, against the entry's own `sense_numbers`. |

`metrics.json` holds the headline numbers.
