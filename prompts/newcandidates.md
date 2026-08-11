# Candidate Restock Prompt (the Routine's `candidates` mode)

Restock `candidate_words.json` with individually vetted headwords so the
`new-entries` mode always has real material. This is the **verified-restock
playbook**: every word is generated from lexical knowledge, passes explicit
vetting gates, and is batch-added with automatic duplicate checking. Proper
nouns are in scope (policy adopted 2026-08-11).

Run standalone or as the unified Routine's `candidates` mode
(`prompts/routine2.md` §2). The selector schedules this mode only while the
queue holds fewer than `candidate_restock_threshold` (150) words, and passes
`params.approx_new` (40–60) as the target.

## Quick context

- The queue holds **only vetted words** since the 2026-08-11 cleanup — keep it
  that way. History and rationale: `find-candidates` skill ("Design
  principle"); the removed corpus-harvest junk is archived in
  `planning/archive/candidate-cleanup-2026-08-11.json`.
- Check the queue: `python3 build/manage_candidates.py stats`

## Workflow

1. **Load the `find-candidates` skill** — it defines the vetting gates
   (G1–G7), the proper-noun richness criteria, and the discovery lenses.
   Everything below assumes it.

2. **Read the gap data** (cheap, aims the generation):
   ```bash
   python3 build/manage_candidates.py stats
   python3 build/audit_semantic_field.py --below 60 --summary
   python3 build/analyze_scenarios.py --top-gaps 20
   ```
   Also glance at the last restock session log (`polishing/sessions/`) for
   which lenses it used, so this run rotates to different ones.

3. **Choose 3–5 discovery lenses** from the skill's list. Include the
   proper-noun lens in most runs (target roughly 20–40% of the batch) while
   major gaps remain — famous places, canonical historical/literary figures,
   key organizations, culturally central works, events, and brands.

4. **Generate ~1.5× the target as proposals**, then **vet each against the
   gates** (real word, lemma form, headword-worthy, correct reading, correct
   gloss, learner value; richness for proper nouns). Drop anything uncertain
   — when in doubt, skip. Aim to land near `params.approx_new` (default ~50)
   survivors.

5. **Write the survivors to a scratch JSON file** (NOT in the repo —
   use the session scratchpad or /tmp):
   ```json
   [
     {"word": "渋谷", "reading": "しぶや",
      "notes": "Shibuya — Tokyo youth-culture hub; proper noun (place)"},
     {"word": "腑に落ちる", "reading": "ふにおちる",
      "notes": "to make sense, to click (usu. negative); idiom"}
   ]
   ```

6. **Batch-add with automatic duplicate checking:**
   ```bash
   python3 build/manage_candidates.py add-batch <scratch-file>.json
   ```
   Duplicates are skipped and reported — that is normal, not an error.

7. **Second-pass self-check.** Re-read the added list once
   (`git diff candidate_words.json` shows exactly what was added), re-testing
   the gates with fresh eyes. Remove any slip:
   ```bash
   python3 build/manage_candidates.py remove C22950
   ```
   One pass, then stop — no ping-pong.

8. **Wrap up** (standalone runs; Routine runs follow routine2.md §5–7):
   - Update `PROJECT_STATUS.md` Recent Changes (count added, lenses used).
   - `make build` (the queue feeds `docs/pending.html`), commit, push, PR.

## Quality bar (summary — the skill has the full gates)

- **Must be**: real, stable, lemma-form headwords with correct hiragana
  readings and correct glosses; useful to intermediate-to-advanced learners;
  general tier.
- **Proper nouns must be collocationally/semantically rich** — fixed
  expressions, metonymy, cultural-literacy weight, or practical navigation
  value — not merely referential. Mark them: `proper noun (place | person |
  organization | work | event | brand)`.
- **Must NOT be**: bulk-extracted from text, uncertain of existence,
  conjugated/derived forms, free phrases, number+counter combinations,
  ephemeral slang, vulgar/discriminatory terms, archaic/dialect items, or
  hyper-specialized jargon.

## Output format

Report at the end of the run:
1. Words proposed / added / skipped as duplicates
2. Lenses used with per-lens counts (note the proper-noun share)
3. Queue total after the run
4. Lenses that look exhausted or fertile for next time
