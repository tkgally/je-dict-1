# je-dict-1 command catalog

Every maintained script, grouped by job. CLAUDE.md holds only the essentials;
this file is the reference. Run everything from the repository root.

## Validation, indexes, site

```bash
python3 build/validate.py                          # Validate all entries against schema
python3 build/validate.py --id 01234               # One entry (links and cross-refs checked against the whole dictionary)
python3 build/validate.py --range 10000 10499      # An ID range
python3 build/validate.py --changed-only           # Entries changed vs origin/main (fast)
python3 build/validate.py --changed-only --ratchet # CI gate: register tags, verb transitivity, furigana braces on changed entries (baseline: build/data/ratchet_baseline.json)
python3 build/validate.py --write-ratchet-baseline   # Regenerate the ratchet baseline (only right after a mechanical sweep)
python3 build/validate_tags.py                     # Semantic/POS tag consistency
python3 build/validate_tags.py --check-no-new-unknown   # CI ratchet: no new off-vocabulary semantic tag
python3 build/validate_tags.py --write-unknown-baseline # Regenerate build/data/unknown_semantic_baseline.json
python3 build/check_note_headers.py --summary      # Non-canonical notes headers
python3 build/check_note_headers.py --gate         # CI ratchet: no new non-canonical header
python3 build/check_note_headers.py --write-baseline    # Regenerate build/data/unknown_header_baseline.json
python3 build/check_link_targets.py                # Inline links whose target entry does not exist
python3 build/check_link_baseform.py --gate        # CI ratchet: link target is the entry for its own base form
python3 build/check_link_homophones.py --gate      # CI gate: block-tier kana links need a keep decision; unlinked links stay gone
python3 build/validate_articles.py                 # CI gate: articles/*.json — schema, furigana, link targets, related entries
make gate                                          # Exactly the CI checks on a PR (tests, validation, ratchet gates); run before every push
python3 build/update_indexes.py                    # entries_index.json, candidate sync, word lookup
python3 build/update_kanji_index.py                # Rebuild kanji JSON; --check-new lists kanji needing IDs
python3 build/build_flat.py                        # Full site build into docs/ (CI does this on merge)
python3 build/build_flat.py --quick                # Incremental site build (local preview)
make index                                         # validate + indexes + kanji JSON (the wrap-up step)
make build                                         # index + full site build (local preview only)
make test                                          # unit tests (build/tests)
make install-hooks                                 # activate .githooks/pre-commit
make priorities                                    # regenerate polishing/priority/*.txt
make metrics-page                                  # regenerate planning/wiki/topics/quality-metrics.md
```

## Mechanical passes (safe, deterministic; --dry-run by default)

```bash
python3 build/auto_link.py --ids 01234,01235 --apply        # Inline links for unambiguous tokens (honours the kana homophone list and the link ledger)
python3 build/auto_link.py --range 20000 20499 --report     # Dry-run statistics for a block
python3 build/review_links.py --apply-decisions --ids 01234 # Strip links the ledger says to unlink, then re-link the entry
python3 build/link_articles.py --ids keigo --apply          # Inline links in article bodies (auto_link.py rules); --list reviews them, --unlinked lists bare words, --strip re-links from scratch
python3 build/harvest_crossrefs.py --ids 01234 --apply      # Cross-references from SIMILAR/RELATED bullets
python3 build/normalize_notes.py --ids 01234 --apply        # Canonical headers, '- ' bullets
python3 build/normalize_pos.py --range 1 30999 --apply      # Canonical part_of_speech display strings
python3 build/backfill_register.py --range 1 30999 --apply  # politeness/formality defaults with guards
python3 build/fix_furigana_format.py --range 1 30999 --apply # Safe furigana wrapper repairs
python3 build/add_conjugations.py                            # Conjugation tables for verbs (skips existing)
python3 build/add_adjective_conjugations.py                  # Conjugation tables for i-adjectives
```

## Detectors (read-only review queues)

```bash
python3 build/check_link_newcomers.py --since 2026-09-01 --json  # Links whose word gained a homograph
python3 build/check_link_homophones.py                  # Kana-base links by tier (unique / verify / block / unscreened)
python3 build/check_link_homophones.py --unscreened     # Kana bases the curated list does not know yet
python3 build/check_link_homophones.py --json --tier verify --sample 60   # Occurrence queue for review_links.py
python3 build/check_link_homophones.py --retier --write # Re-derive tiers from reviews/link_decisions.jsonl
python3 build/check_link_homophones.py --json --kanji-base --sample 40    # Hand links きて→来る (kana surface, kanji base)
python3 build/review_links.py --screen --budget 1.00    # Model screen of unscreened kana bases -> build/data/kana_link_homophones.json
python3 build/review_links.py --ids 01234,01235 --skip-decided --budget 0.10   # Model check of an entry's kana links in context (self-check)
python3 build/review_links.py --tier verify --sample 60 --budget 2.00     # Sweep: occurrences of ambiguous bases
python3 build/review_links.py --ledger-from reviews/links/review_<stamp>.jsonl   # keep lines for model-confirmed links
python3 build/check_stale_noentry.py --summary          # noentry markers whose word now has an entry
python3 build/check_stale_noentry.py --class A1 A2 --json   # The mechanical classes
python3 build/check_furigana_format.py --summary        # Malformed furigana wrappers
python3 build/check_artifacts.py --summary              # Batch-creation artifacts
python3 build/check_tag_drift.py --summary              # sole-general, off-vocabulary, semantic mismatch
python3 build/check_example_headword.py --summary       # Noun examples that never contain the headword
python3 build/check_consistency.py                      # Note structure, transitivity, example counts
python3 build/check_semantic_clusters.py --summary      # Transitivity/antonym/keigo cluster completeness
python3 build/find_missing_furigana.py                  # Kanji lacking furigana (JSON)
python3 build/verify_furigana.py 01234                  # One entry's furigana coverage
python3 build/find_missing_transitivity.py              # Verbs missing transitivity
python3 build/find_merge_candidates.py --asymmetry-only # One-way cross-references
python3 build/score_note_quality.py --summary           # Note score distribution; --rubric prints the rubric
python3 build/report.py                                 # Health dashboard
```

## Entry creation helpers

```bash
python3 build/get_next_id.py                                    # Next free ID (run before EACH new entry)
python3 build/check_duplicate.py "word" "reading"               # Duplicate check (add --skip-candidates when creating from the queue)
python3 build/check_duplicate.py --batch 'w1:r1' 'w2:r2'        # Bulk probe
python3 build/get_entry_path.py <id> <romaji>                   # File path for an entry
python3 build/get_timestamp.py                                  # UTC timestamp for metadata
python3 build/manage_candidates.py add "word" "reading" "gloss; seen in entry NNNNN"
python3 build/manage_candidates.py add-batch proposed.json      # Many, duplicate-checked
python3 build/manage_candidates.py remove C00123
python3 build/manage_candidates.py sync                         # Drop candidates that now exist
python3 build/manage_candidates.py stats
```

## External review (requires OPENROUTER_API_KEY)

```bash
python3 build/review_accuracy.py --range 5800 5900 --budget 1.00   # gloss, translation, tags, notes
python3 build/review_accuracy.py --ids 05907 --budget 0.40         # self-check of specific entries
python3 build/review_accuracy.py --ids 05907 --dimensions notes --dry-run
python3 build/review_accuracy.py --report
python3 build/review_transitivity.py --all-missing --budget 1.00   # transitivity proposals for untagged verbs
python3 build/review_runner.py --pass screening --range 1 100      # furigana screener (manual use only; 2% precision)
```

## Example audio (requires OPENROUTER_API_KEY; AUDIO_WORKFLOW.md)

```bash
make audio-deps                                        # fugashi + unidic-lite (MeCab), lameenc, miniaudio
python3 build/audio_pipeline.py status                 # coverage by tier, stale, undetermined, needs-human, store use
python3 build/audio_pipeline.py plan --budget 2.30     # choose examples in priority order → audio_work/plan.json
python3 build/audio_pipeline.py run --workers 12       # generate → check → regenerate; stage accepted MP3s in audio_work/
python3 build/audio_pipeline.py publish                # push MP3s to the audio repository, then write audio/manifest/
python3 build/audio_pipeline.py testset --voice Aoede  # voice pilot on the 100-sentence test set
python3 build/audio_pipeline.py undetermined --reason bare-kanji malformed   # examples whose reading is not determined
python3 build/audio_regression.py                      # the 163 regression clips; required before any workflow change
python3 build/check_no_binaries.py                     # CI gate: no audio files in je-dict-1
```

## Routine and pipeline

```bash
python3 pipeline/routine_next.py --explain          # Why the next run would pick a mode
python3 pipeline/routine_next.py --simulate 60      # Mode mix over 60 runs
python3 pipeline/routine_next.py --force-mode polish
python3 pipeline/metrics_snapshot.py --mode polish --changed 16
python3 pipeline/metrics_report.py                  # Regenerate the quality-metrics page
python3 pipeline/update-brief.py                    # Refresh PROJECT_CONTEXT_BRIEF.md
python3 pipeline/absorb_branch.py <branch> --pr N   # Merge a stranded Routine branch with the per-file policy (entries/code merge, indexes keep main, ledgers union)
python3 pipeline/absorb_branch.py --residue <branch> # What a claude/* branch still holds that main lacks (empty = safe to prune)
#   pipeline/absorbed-branches.jsonl records every absorbed branch tip; a recorded branch never reports residue
python3 pipeline/wait.py 60                         # Foreground wait between CI polls (a backgrounded sleep does not wait)
```

## Coverage analysis

```bash
python3 build/audit_semantic_field.py --summary
python3 build/analyze_scenarios.py --summary
python3 build/audit_tiers.py --outliers
make audit-fields / make audit-scenarios / make audit-tiers
```

## Parallel sessions (interactive only)

```bash
python3 build/entry_lock.py lock --range 10000 10499 --session "s1"
python3 build/parallel_coordinator.py branch1 branch2
python3 pipeline/task_queue.py status
python3 pipeline/orchestrator.py status
```
