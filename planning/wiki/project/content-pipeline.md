# Content Pipeline

**Last updated**: 2026-04-06

## Overview

Entries flow through a multi-stage pipeline from discovery to publication:

```
Candidate Discovery → Candidate Queue → Entry Creation → Validation → Polishing → Publication
```

Each stage has its own tools, prompts, and quality gates.

## Stage 1: Candidate discovery

New words are identified and added to `candidate_words.json`. The primary method is now **LLM-based brainstorming**:

- **LLM brainstorming** (primary) — `prompts/brainstorm-new-candidates.md` runs an automated pipeline that seeds an external LLM (via OpenRouter) with existing dictionary words and asks it to suggest related words that are missing. Explores synonyms, antonyms, same-field words, kanji compounds, register variants, collocational partners, and situationally related words. Produces large batches of candidates efficiently with built-in deduplication. See [Word Discovery Strategies](../ideas/word-discovery-strategies.md) for analysis of this and other approaches.
- **Manual identification** — the curator notices gaps in coverage
- **Corpus harvesting** — processing frequency lists to find missing common words (`prompts/corpus_harvesting.md`); an earlier approach that has been largely superseded by brainstorming
- **Systematic search** — scanning for words in specific semantic domains (`prompts/newcandidates.md`)
- **Cross-reference gaps** — words mentioned in existing entries but lacking their own entry
- **No-entry link detection** — words marked `noentry` in inline links

Candidates are managed via `build/manage_candidates.py` (add, check, sync, stats).

## Stage 2: Entry creation

Entries are created in batch sessions of ~30 entries each, following `prompts/newentries.md`:

1. Duplicate check (`check_duplicate.py`)
2. Get next ID (`get_next_id.py`)
3. Get timestamp (`get_timestamp.py`)
4. Write entry JSON following the appropriate skill (verb-entry, adjective-entry, etc.)
5. Post-batch validation, conjugation generation, index update, site build

## Stage 3: Polishing

Created entries are improved through iterative polishing passes, each tracked with progress files in `polishing/tasks/`:

| Task | Prompt | What it does |
|------|--------|-------------|
| Inline links | `polish_add_inline_links.md` | Add ⟦...⟧ cross-reference links |
| Example sentences | `polish_example_sentences.md` | Check count, quality, tier compliance |
| Furigana completeness | `polish_furigana_completeness.md` | Find and add missing furigana |
| Furigana correctness | `polish_furigana_correctness.md` | Verify readings are correct |
| Semantic labels | `polish_semantic_labels.md` | Verify tags match meanings |
| Short notes | `expand-short-notes.md` | Expand inadequate notes |

Each task resumes where the previous session left off via `polishing/tasks/{task}/progress.txt`.

## Stage 4: Consolidation

Periodic maintenance to keep entries clean:

- **Duplicate detection** — `find_merge_candidates.py` identifies entries that should be merged
- **Cross-reference addition** — `prompts/add_cross-references.md` systematically links related entries
- **Candidate cleanup** — `prompts/clean_up_candidates_list.md` reviews the candidate queue

## Automated pipeline

The `pipeline/` directory contains `run-pipeline.sh` and related scripts for automated batch execution. GitHub Actions (`pipeline.yml`) can trigger pipeline runs.

## Quality gates

Every stage has validation:
- **Schema validation** — `validate.py` checks structure against `build/schema.json`
- **Tag validation** — `validate_tags.py` checks semantic/POS tag consistency
- **Furigana check** — `find_missing_furigana.py` catches unmarked kanji
- **Duplicate check** — `check_duplicate.py` prevents duplicate entries
- **CI** — GitHub Actions runs validation on every push

## Session workflow

A typical entry creation session:
1. Read `PROJECT_CONTEXT_BRIEF.md` for current state
2. Create entries (with duplicate checks and fresh IDs)
3. Run validation sequence (validate → furigana → conjugation → indexes → kanji → build)
4. Update `PROJECT_STATUS.md`
5. Commit, push, PR, CI check, squash-merge, cleanup

## Related pages

- [Architecture and Build System](architecture.md)
- [Quality Standards](quality-standards.md)
- [Entry Design](entry-design.md)
