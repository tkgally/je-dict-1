# je-dict-1 — Japanese-English Learner's Dictionary

A dictionary for intermediate learners of Japanese who can read kana and are building vocabulary. The live site is at https://www.tkgje.jp/. It is a completely static site (HTML/CSS/JS, no server) hosted on GitHub Pages. Over 12,000 entries as of early 2026.

## Project structure

```
entries/          # Source dictionary entries as JSON (subdirs by ID range, 500 per dir)
docs/             # Generated static website (do NOT edit by hand — rebuilt by build_flat.py)
build/            # Python build, validation, and utility scripts
  build/templates/    # Standalone CSS and JS templates (styles.css, search.js, tag-search.js)
  build/tests/        # Unit tests (pytest)
  build/archive/      # One-time migration scripts (no longer used in regular operation)
  build/schema.json             # JSON schema for entry validation
  build/entry_renderer.py       # Entry page HTML generation
  build/page_generators.py      # Navigation page generation (index, browse, recent, etc.)
  build/search_index_builder.py # Search index and JS generation
  build/report.py               # Dictionary health dashboard
  build/generate_word_lookup.py # Builds word_id_lookup.json for inline link lookups
  build/manage_candidates.py    # Add/remove/check candidates in candidate_words.json
  build/find_missing_furigana.py # Scan entries for kanji missing furigana
  build/find_missing_transitivity.py # Report on verbs missing transitivity data
  build/update_kanji_index.py   # Rebuild kanji JSON files; --check-new finds new kanji
  build/validate_tags.py        # Validate semantic/POS tag consistency
  build/get_next_id.py          # Get next available entry ID (scans filesystem)
  build/add_conjugations.py      # Add full conjugation tables to verb entries
  build/add_adjective_conjugations.py  # Add conjugation tables to i-adjective entries
  build/find_merge_candidates.py # Detect duplicate/variant entries and missing cross-refs
kanji/            # Kanji index data (JSON files mapping kanji to entries)
pipeline/         # Automated task pipeline (run-pipeline.sh, validation gates, status tracking)
planning/         # Project knowledge base and planning
  planning/wiki/        # LLM-maintained knowledge base (project docs, research, ideas)
  planning/wiki/index.md    # Master catalog of all wiki pages
  planning/wiki/log.md      # Chronological record of wiki maintenance sessions
  planning/maintain-knowledge-base.md  # Session prompt for wiki maintenance (nightly cron)
polishing/        # Progress tracking for entry polishing tasks
  polishing/tasks/{task}/progress.txt  # Next entry ID to process per task
  polishing/sessions/                  # Session logs (what was checked/changed)
prompts/          # Task prompts for interactive sessions
  prompts/batch/      # Shell runner scripts for non-interactive `claude --print` execution
  prompts/refactoring/  # Code refactoring prompts for build scripts
  prompts/expand-short-notes-tracking.txt  # Separate tracking file for expand-short-notes task
enhancement/      # Long-term enhancement plan and implementation prompts
  enhancement/enhancement-plan-2026-04-09.md  # Comprehensive enhancement plan
  enhancement/prompts/                        # Step-by-step implementation prompts (16 phases)
  enhancement/prompts/README.md               # Master guide, metaprompts, and sequencing
candidate_words.json   # Words queued for future entry creation
entries_index.json     # Master index of all entries (rebuilt by update_indexes.py)
build/word_id_lookup.json  # Pre-built word→entry_id map (for inline link lookups)
PROJECT_STATUS.md      # Session continuity notes and recent change log (keep 5 most recent)
PROJECT_CONTEXT_BRIEF.md # Quick-reference counts and rules for session start
.claude/skills/        # Reusable skill prompts for entry creation and maintenance
.github/workflows/     # GitHub Actions CI (validate.yml) and pipeline (pipeline.yml)
.githooks/             # Git hooks (pre-commit entry validation)
Makefile               # Build runner (make validate, make build, make quick, etc.)
```

## Session start

**At session start**: Run `python3 pipeline/update-brief.py` before reading PROJECT_CONTEXT_BRIEF.md to ensure counts are current. (This is also run automatically after each merge to main via GitHub Actions.)

## Entry basics

- Each entry is a JSON file at `entries/{range}/{id}_{romaji}.json`
- Range directory = ID rounded down to nearest 500 (e.g., ID 01186 → `entries/01000/`)
- Use `python3 build/get_entry_path.py <id> <romaji>` to get the correct path
- **Romaji in IDs must be the full reading concatenated** — no internal underscores. Examples: `ketteisuru` (not `kettei_suru`), `kaowodasu` (not `kao_wo_dasu`), `fushizenna` (not `fushizen_na`). Schema regex: `^[0-9]{5}_[a-z]+(_[a-z]+)?$`
- **POS tags use hyphenated names**: `verb-suru`, `verb-godan`, `adjective-na`, `adjective-no` (not `suru-verb`, `godan-verb`, `na-adjective`, etc.). See `entry-guidelines` skill for the full list.
- Entries must validate against `build/schema.json`
- All kanji must have furigana: `{漢字|かんじ}` — in headwords, examples, AND notes
- Readings are always hiragana, never katakana
- All new entries go in the **general** vocabulary tier
- New entries should include `"schema_version": "2.0"` in their metadata
- All explanations must be in English — Japanese text appears only in example phrases, collocations, and patterns
- Never add inline word links (⟦...⟧) during entry creation — those are added in a separate polishing step
- **Verb entries must include a `conjugation` field** with all conjugated forms hard-coded in the JSON (see `verb-conjugations` skill). Use `python3 build/add_conjugations.py` to generate conjugation data after creating verb entries.
- **I-adjective entries must include a `conjugation` field** with all conjugated forms. Use `python3 build/add_adjective_conjugations.py` to generate conjugation data after creating i-adjective entries.
- **Entry IDs must be unique.** Always run `python3 build/get_next_id.py` before creating each new entry to get the next available ID. This script scans the filesystem, so it is accurate even mid-session. Do not read `entries_index.json` or `PROJECT_CONTEXT_BRIEF.md` for the next ID — those may be stale. Do not reuse a previous result of `get_next_id.py` — run it fresh each time.
- **Never renumber existing entries.** The five-digit IDs form part of the entry's URL on the live site. Changing an ID would break external links and search-engine indexes.

## Essential commands

```bash
# Validation and building
python3 build/validate.py                 # Validate all entries against schema
python3 build/validate_tags.py            # Validate semantic/POS tag consistency
python3 build/update_indexes.py           # Update entries_index.json, candidate list, word lookup
python3 build/build_flat.py               # Full rebuild of the static site
python3 build/build_flat.py --quick       # Incremental build — only changed entries

# Entry creation helpers
python3 build/get_next_id.py                                     # Get next available entry ID (ALWAYS run before each new entry)
python3 build/check_duplicate.py "word" "reading"                # Check before creating an entry
python3 build/check_duplicate.py --skip-candidates "word" "reading"  # When creating FROM candidates
python3 build/get_entry_path.py <id> <romaji>       # Get correct file path for an entry
python3 build/get_timestamp.py            # Get current UTC timestamp for metadata

# Verb conjugation
python3 build/add_conjugations.py                    # Add conjugation to all verbs (skips existing)
python3 build/add_conjugations.py --start N --end M  # Process specific ID range
python3 build/add_conjugations.py --dry-run          # Preview without writing
python3 build/add_conjugations.py --force            # Overwrite existing conjugation data

# I-adjective conjugation
python3 build/add_adjective_conjugations.py                    # Add conjugation to all i-adjectives
python3 build/add_adjective_conjugations.py --start N --end M  # Process specific ID range
python3 build/add_adjective_conjugations.py --dry-run          # Preview without writing
python3 build/add_adjective_conjugations.py --force            # Overwrite existing conjugation data

# Furigana and kanji
python3 build/verify_furigana.py <id>     # Check furigana coverage for one entry
python3 build/find_missing_furigana.py    # Scan all entries for missing furigana (pipe to head)
python3 build/update_kanji_index.py --check-new  # Check for new kanji needing IDs after entry creation

# Candidate management
python3 build/manage_candidates.py add "word" "reading" "gloss"   # Add a candidate
python3 build/manage_candidates.py check "word" "reading"         # Check if word exists as entry or candidate
python3 build/manage_candidates.py sync                           # Remove candidates that now exist as entries
python3 build/manage_candidates.py stats                          # Show candidate list statistics

# Entry consolidation
python3 build/find_merge_candidates.py              # Full report: merges, cross-refs, dup IDs
python3 build/find_merge_candidates.py --merge-only # Only potential merges
python3 build/find_merge_candidates.py --json       # Machine-readable output

# Verb transitivity
python3 build/find_missing_transitivity.py              # Report on verbs missing transitivity data
python3 build/find_missing_transitivity.py --tier basic  # Filter to one tier
python3 build/find_missing_transitivity.py --json        # Machine-readable output

# Reports
python3 build/report.py                   # Dictionary health dashboard
python3 pipeline/update-brief.py          # Refresh PROJECT_CONTEXT_BRIEF.md from current data

# Makefile shortcuts (recommended)
make build                                # validate + update_indexes + full build
make quick                                # validate + update_indexes + incremental build
make validate                             # validate only
make validate-changed                     # Validate only entries changed vs. main (fast)
python3 build/validate.py --range 10000 10499  # Validate a specific ID range
make report                               # health dashboard
make check-furigana                       # find_missing_furigana scan
make check-kanji                          # verify kanji index integrity
make stats                                # tag statistics
make word-lookup                          # rebuild word_id_lookup.json
```

After creating or revising entries, always run: `make build` (or validate → update_indexes → build_flat).

## Post-creation validation sequence

After creating new entries (used by newentries prompts):

```bash
python3 build/validate.py                                # Fix any errors first
python3 build/find_missing_furigana.py | head -60        # Check for missing furigana
python3 build/add_conjugations.py                        # Add conjugation to any new verbs
python3 build/add_adjective_conjugations.py              # Add conjugation to any new i-adjectives
python3 build/update_indexes.py                          # Sync indexes and candidate list
python3 build/update_kanji_index.py --check-new          # Check for new kanji needing IDs
python3 build/build_flat.py                              # Rebuild the static site
```

If `find_missing_furigana.py` shows entries from the current session, fix them before building. If new kanji are found, assign on'yomi, kun'yomi, and gloss before building.

## Vocabulary tiers

- **Basic** (~800 entries) — foundational words; closed, do not add
- **Core** (~2,000 entries) — essential adult communication; closed, do not add
- **General** (9,000+ entries, growing) — all other vocabulary; all new entries go here

## Task prompts

The `prompts/` directory contains detailed instructions for each type of session task. Start a task by reading the prompt file (e.g., "Read prompts/newentries.md and follow the instructions"). Shell runner scripts in `prompts/batch/` automate tasks for non-interactive `claude --print` execution. `prompts/metaprompt_list.md` is a reference listing all available prompts with usage examples.

**Dictionary building:**
- `newentries.md` — create 30 entries from candidate_words.json
- `newcandidates.md` — find new candidate words to add
- `corpus_harvesting.md` — process corpus words into candidates (progress tracked in `corpus_harvesting_next_entry_number.txt`)
- `clean_up_candidates_list.md` — review and clean candidate_words.json
- `polish_add_entries_for_noentry_example_words.md` — create entries for words marked `noentry` in inline links

**Entry consolidation:**
- `consolidate_entries.md` — find and merge duplicate/variant entries
- `add_cross-references.md` — systematically review and add cross-references (`prominent_see_also` and `cross_references`) to entries
- `fix_duplicate_ids.md` — resolve entries sharing the same 5-digit numeric ID

**Polishing (progress-tracked):**
- `polish_add_inline_links.md` — add ⟦...⟧ cross-reference links to examples/notes
- `polish_example_sentences.md` — check example count, quality, and vocabulary tier compliance
- `polish_furigana_completeness.md` — find and add missing furigana
- `polish_furigana_correctness.md` — verify existing furigana readings are correct
- `polish_semantic_labels.md` — verify semantic tags match word meanings
- `polish_verb_transitivity.md` — add transitivity tags, notes, and pair links to verbs
- `expand-short-notes.md` — expand inadequate notes (tracking in `prompts/expand-short-notes-tracking.txt`)
- `polish_aspect_notes.md` — add ている documentation to verb entries with non-obvious aspect behavior

Polishing tasks track progress in `polishing/tasks/{task-name}/progress.txt` (format: `next: XXXXX`). They automatically resume where the previous session left off. Each session should commit in batches and write a session log to `polishing/sessions/`. Use `prompts/resume-session.md` to resume a polishing task with full context from the previous session.

**Session log standard**: All polishing sessions should write a structured log to `polishing/sessions/{task}_{date}_{nnn}.md` when finishing. The log should include: date, entry range processed, list of changes made, any notes, and the next entry number. See existing logs in `polishing/sessions/` for examples.

**Knowledge base:**
- `planning/maintain-knowledge-base.md` — maintain and expand the project knowledge base wiki (nightly cron or manual)

The knowledge base at `planning/wiki/` is an LLM-maintained wiki covering project documentation, external research (lexicography, SLA, corpus linguistics), design decisions, and future ideas. It is updated incrementally by dedicated maintenance sessions and can be consulted during any session for background knowledge. See `planning/wiki/index.md` for the full page catalog.

**Enhancement plan:**
- `enhancement/enhancement-plan-2026-04-09.md` — comprehensive plan for content quality, workflow, and infrastructure improvements
- `enhancement/prompts/README.md` — master guide with 16 step-by-step implementation prompts, metaprompts, and sequencing instructions
- Enhancement prompts cover: infrastructure, verb transitivity, aspect/ている, note quality, cross-references, polishing priority, semantic fields, scenarios, tier reassessment, consistency checking, parallel execution, multi-model review, task queues, expository articles, and orchestration

## Skills (detailed guidelines)

Detailed instructions for specific tasks live in `.claude/skills/`. Key ones:

- `entry-guidelines` — quality standards, file placement, metadata, tags (start here)
- `verb-entry` — transitivity, aspect/ている, particle patterns
- `verb-conjugations` — full conjugation table specification, form categories, generation rules
- `adjective-entry` — forms, conjugations, predicate vs. modifier usage
- `particle-entry` — predicate lists, particle contrasts, fixed patterns
- `other-entries` — nouns, counters, adverbs, expressions
- `example-sentences` — minimum counts, progressive length, tier vocabulary restrictions
- `vocabulary-notes` — formatting and structure for the notes field
- `cross-reference-entry` — adding and maintaining cross-references
- `inline-word-links` — `⟦surface→base：entry_id⟧` links in examples and notes
- `find-candidates` — discovering new words to add to candidate_words.json
- `vocabulary-tiers` — tier criteria, word counts, self-containment principles
- `kanji-index` — kanji ID assignment, index updates
- `revise-entries` / `polish-entries` — improving existing entries
- `consolidate-entries` — identifying and merging duplicate/variant entries
- `delete-entry` / `resolve-duplicates` — safe removal and deduplication

Invoke a skill with `/<skill-name>` (e.g., `/verb-entry`) to load its full instructions.

## End-of-session PR and merge workflow (CRITICAL)

All task prompts that create a PR must follow this complete workflow. The goal is to leave main in a fully clean state so the next session can start fresh.

### Before creating the PR

1. **Run `make build`** — this generates `docs/`, `entries_index.json`, and other build artifacts
2. **Commit ALL changes including build artifacts**: `git add -A && git commit -m "..."`
   - This must include `docs/`, `entries_index.json`, `build/word_id_lookup.json`, `kanji/`, etc.
   - The PR must contain both source changes AND rebuilt site files
3. **Push** to the feature branch

### PR, CI, and merge

Use the `gh` CLI for GitHub operations. The git remote uses a local proxy, so **always pass `--repo tkgally/je-dict-1`** to `gh` commands. If GitHub MCP tools (`mcp__github__*`) are available, those work too.

4. **Create the PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "..." --body "..."`
5. **Poll CI** every 60 seconds: `gh pr checks <number> --repo tkgally/je-dict-1` (up to 10 minutes)
6. **Squash-merge** once CI is green: `gh pr merge <number> --repo tkgally/je-dict-1 --squash`
7. If CI fails: read logs with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat from step 5

### Post-merge cleanup (MANDATORY)

8. **Switch to main and pull**: `git checkout main && git pull origin main`
9. **Verify clean state**: `git status` should show nothing to commit
10. **Delete the feature branch locally**: `git branch -d <branch-name>`
11. **Delete the feature branch remotely**: `git push origin --delete <branch-name>`

If `git status` on main shows uncommitted changes after pulling (this should not happen if build artifacts were included in the PR), run `make build`, commit, and push to main directly.

**Why this matters**: The `docs/` directory is deployed via GitHub Pages. If build artifacts are not in the PR, the live site won't update after merge, and the next session starts with a dirty repository.
