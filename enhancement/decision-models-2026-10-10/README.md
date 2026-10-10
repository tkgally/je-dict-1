# Decision-model evaluation, 10 October 2026

Material behind `enhancement/decision-models-2026-10-10.html`: can the decision models on
OpenRouter (typed yes/no and choice answers via `POST /api/alpha/decisions`) take over any of
je-dict-1's checking tasks?

| File | What it is |
|---|---|
| `sets/*.jsonl` | Test items. `screen` is the 48-item screening battery; the other seven are the task sets (furigana, links, flags, conjugation, translation, sense, transitivity). Each line has `state` (what the model sees), `label` (the right answer) and `sub` (item kind). |
| `drop.json` | Items excluded from scoring after hand-checking (acceptable "wrong" readings and translations, disputed transitivity tags). |
| `trans_disputed.json` | The nine transitivity tags all three strong LLMs disagreed with. Worth a curator look. |
| `summary.json` | Every score in the report. |
| `build_sets.py` | Builds the sets from the entries and review ledgers. `perturb.py` made the altered translations (one Gemini 3.8 Flash call). |
| `run.py` | Runs a decision model (`dec`) or a batched LLM (`llm`) over a set; results go to `results/` (not committed, ~9 MB). |
| `score.py`, `analyze.py` | Scoring, cross-validated cut-offs, cascade simulation; writes `summary.json`. |
| `charts.py`, `gen_report.py`, `report_template.html` | Build the HTML report. |

Re-run, from this directory, with `OPENROUTER_API_KEY` set:

```bash
python3 build_sets.py            # rewrites sets/ (seeded; translation perturbations need perturb.py again)
python3 run.py dec openai/gpt-6-luna-decisions furigana,links,conjugation,translation,sense,transitivity,flags
python3 run.py llm anthropic/claude-haiku-5.5 furigana,links,conjugation,translation,sense,transitivity,flags --batch 20
python3 analyze.py && python3 gen_report.py
```

The full run (16 decision models, 4 LLMs, 1,444 items each) cost about $1.50.
