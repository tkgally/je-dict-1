# Resume Session

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Resume a polishing task from where the previous session left off.

## Usage

Replace `{TASK}` below with the task name, then follow the instructions.

**Task to resume**: {TASK}

(Examples: `inline-links`, `example-sentences`, `furigana-completeness`, `furigana-correctness`, `semantic-labels`, `add_cross_references`)

## Steps

### 1. Read progress state

```bash
cat polishing/tasks/{TASK}/progress.txt
```

Note the `next:` value — this is where to resume.

If the progress file also contains a `last_session:` line, read that summary.

### 2. Find the most recent session log

```bash
ls -t polishing/sessions/{TASK}_* 2>/dev/null | head -1
```

If a log exists, read it to understand:
- What entry range was processed
- How many entries were modified
- Any unusual cases or decisions noted
- The "Next Entry" value (should match the progress file)

### 3. Summarize context

Before starting work, briefly state:
- **Resuming task**: {TASK}
- **Starting from entry**: (from progress file)
- **Last session processed**: (entry range from log, if available)
- **Notes from last session**: (anything relevant)

### 4. Begin the task

Now read and follow the main task prompt:

```bash
# Map task name to prompt file
```

| Task name | Prompt file |
|-----------|-------------|
| `inline-links` | `prompts/polish_add_inline_links.md` |
| `example-sentences` | `prompts/polish_example_sentences.md` |
| `furigana-completeness` | `prompts/polish_furigana_completeness.md` |
| `furigana-correctness` | `prompts/polish_furigana_correctness.md` |
| `semantic-labels` | `prompts/polish_semantic_labels.md` |
| `add_cross_references` | `prompts/add_cross-references.md` |

Read the corresponding prompt file and follow its instructions, starting from the entry indicated by the progress file.
