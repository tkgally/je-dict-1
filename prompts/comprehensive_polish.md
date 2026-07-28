# Comprehensive Polish

The **default ongoing-improvement task** for je-dict-1. Each session walks through a small batch of dictionary entries and applies a tiered checklist that unifies the work previously split across the targeted `polish_*` prompts (furigana, examples, inline links, cross-references, semantic labels, transitivity, aspect, expand-short-notes). It also surfaces words and patterns for follow-up so that long-term improvements accumulate over time.

This prompt is designed to be run repeatedly on a schedule. Each invocation picks up where the last one left off.

## Pre-flight: sweep stranded PRs

**Run this as the first step of every session, before you read any entry files or do any other work.** (When this prompt runs as the Routine's `polish` mode, the sweep already happened in `routine2.md` §0 — skip it here.)

Perform the stranded-PR sweep **via MCP**, as described in `CLAUDE.md` → "Sweep stranded PRs via MCP": list open `claude/*` PRs (`mcp__github__list_pull_requests`), and for each, take the maximum entry ID among the `entries/.../NNNNN_*.json` files it touches (`mcp__github__pull_request_read` `method: "get_files"`); if that maximum is strictly less than `polishing/tasks/comprehensive/progress.txt`'s `next:` value, the PR is superseded — comment (`mcp__github__add_issue_comment`) and close it (`mcp__github__update_pull_request` `state: "closed"`). PRs that don't touch entries, or that include any entry at or above the cursor, are left untouched.

This makes the Routine self-healing: if a previous session ended before reaching the merge step, its now-obsolete PR gets cleaned up when the next session starts. Checking is cheap (~1 MCP call per open PR).

**Do not run `pipeline/sweep-stranded-prs.py`** — direct GitHub REST returns HTTP 403 in the Routine/web environment, so the script is a no-op there (it now exits cleanly with a pointer to this MCP procedure). It still works in interactive sessions where a real token + direct REST are available.

## Per-session budget

This prompt **errs on the side of doing more, not less**. Past sessions have stopped at 12% context use, leaving most of the available capacity unused.

- **Target: keep polishing until you've used roughly 60% of your context window**, then start wrapping up. A typical session should process **20–25 entries**, not 3–5. If you've finished 10 entries and context still feels light, keep going.
- **Why 60% and not higher**: the wrap-up phase (build, push, PR creation, up-to-~8-minute MCP CI-poll wait, merge call) consumes a meaningful slice of context, and review-fix-up rounds after opening the PR can eat more. Stranded PRs from previous Routine runs were caused by sessions running out of budget mid-merge. Leaving ~40% headroom is what makes the merge step reliable.
- **Stop earlier than 60% if** tool outputs are getting truncated, you've read several large files, or you've already done a round of post-PR fix-ups. Better to wrap up with one fewer entry than to leave a stranded PR.
- **Take stock every 5 entries.** Briefly note (to yourself) how full context feels and decide: continue at full pace, slow down, or wrap up. Default to wrapping up if you're already past 50%.
- **Hard cap: 25 entries per session.** Wrap up cleanly at 25 even if context is still light.
- **No recursion when checking back-links.** Visit direct neighbors only (entries listed in `cross_references` and `prominent_see_also`). Do **not** follow the neighbors' own links.
- **Don't restructure entries that need major work.** If an entry is broken in a way that would consume a large chunk of the session (wrong POS, fundamentally misclassified, conflated lemmata), make any quick tier-1 fixes, log it as `[entry]` in `polishing/observations.md`, and move on.

## Entry selection

1. Read `polishing/tasks/comprehensive/progress.txt` for the `next:` value.
2. Process entries sequentially from that ID. If a numeric ID has no entry file, advance to the next existing one. (Use `ls entries/{range}/` to find existing IDs.)
3. At session end, update `progress.txt` to point to the entry **after** the last one you processed.

This produces a steady forward sweep through the dictionary. When the sweep wraps around (years from now), we'll add a recency check; for now, sequential is fine.

## Per-entry checklist

For each entry, work through the three tiers below. **Do all of tier 1**, do as much of tier 2 as time allows (prioritizing the highest-impact items for that specific entry), and do tier 3 only if the entry is otherwise in good shape.

### Tier 1 — required for every entry

These items must be true for every entry you touch. Most are mechanical; the inline link work is semi-mechanical (the lookups are mechanical but word-boundary and homograph disambiguation require judgment).

- [ ] **Schema valid**: `python3 build/validate.py --id <entry_id>`
- [ ] **Furigana complete** in headword, examples, AND notes: `python3 build/verify_furigana.py <entry_id>`
- [ ] **Reading is hiragana only** (long-vowel ー allowed)
- [ ] **Romaji matches the full reading**, no internal underscores beyond schema's allowance
- [ ] **All `cross_references` and `prominent_see_also` point to existing entries**
- [ ] **Examples have valid `sense_numbers`**
- [ ] **No obvious typos** in headword, reading, gloss, or English translations of examples
- [ ] **FULL inline link coverage on every Japanese word in examples AND notes** — see the dedicated section below. This is the most labor-intensive tier-1 requirement and the main reason a comprehensive polish session is heavier than a targeted polish session.

If you fix any tier-1 issue, run `python3 build/get_timestamp.py` and update the entry's `modified` timestamp before saving.

#### Full inline link coverage (REQUIRED)

**Goal**: every Japanese word in every example sentence AND every Japanese phrase inside the notes field has either a valid inline link or a `noentry` marker. No naked Japanese words anywhere except the headword itself.

**Format** (from `.claude/skills/inline-word-links/SKILL.md`):
```
⟦{surface|reading}→baseform：entry_id⟧      # word with an entry
⟦{surface|reading}→baseform：noentry⟧       # word without an entry
```

**What to link**:

- **Every content word**: nouns, verbs, adjectives, adverbs
- **Every particle** that has its own entry (は, が, を, に, で, と, から, まで, の, へ, よ, ね, etc.)
- **Every demonstrative, pronoun, and connective**
- **Words inside notes** — collocations, related forms, contrast pairs, fixed phrases. Treat any natural-language Japanese in the notes the same as example sentences.

**What NOT to link**:

- The headword of the entry itself, when it appears unconjugated in its own examples or notes (no self-references)
- Pure punctuation (`。、？！「」『』…`)
- Pattern placeholders (`〜`, `…`, etc.) — but the surrounding Japanese in a pattern like `〜に対して` should still be linked
- Numerals written in arabic digits; counter words attached to them should still be linked

**Workflow**:

1. Use `build/word_id_lookup.json` to look up entry IDs by reading or headword. Open it once per session and grep / search it as you go — re-reading per word is wasteful.
2. For homographs (e.g., きく → 聞く / 効く), pick the entry whose gloss matches the contextual meaning.
3. For conjugated forms, link to the dictionary form (`食べました→食べる：00396_taberu`).
4. For words not in the dictionary: mark `noentry` AND add to `candidate_words.json` (see "Words missing entries" below). Do not skip — every word must end up either linked or marked.
5. Existing entries may already have partial linking; your job is to complete it. Do NOT remove correct links someone else added.

**For new examples you add or new notes you write**: include full link coverage from the start, not as an afterthought.

**Validation after editing**:

```bash
python3 build/validate.py --id <entry_id> 2>&1 | grep -i "word link"
```

This catches malformed links and IDs that don't resolve.

### Tier 2 — should-do (judgment, high-leverage)

- [ ] **Example count meets the tier minimum**: 3 per sense for general, 5 per sense for basic/core. Add examples if short.
- [ ] **Examples follow tier-appropriate vocabulary restrictions** (see `.claude/skills/example-sentences/SKILL.md`)
- [ ] **Examples progress short → long**
- [ ] **Notes are well-formed** per `.claude/skills/vocabulary-notes/SKILL.md` — clear sections, no redundancy, no English-only fluff for a Japanese learner's dictionary, no Japanese explanatory prose
- [ ] **Verb-specific** (when applicable): transitivity tag set; transitivity pair linked in `cross_references` if one exists; aspect/ている behavior documented in notes if non-obvious
- [ ] **Na-adjective specific** (when applicable): notes describe -na vs -ni vs predicate forms
- [ ] **Tags accurate**: `semantic`, `formality`, `politeness` reflect the word's actual character (not template defaults)
- [ ] **Cross-references include obvious neighbors**: synonyms, antonyms, transitivity pairs, register variants. Use one of the types the schema actually accepts — `pair` (transitivity pairs), `synonym`, `antonym`, `related`, `contrast`, `see_also`, `keigo` (register/politeness variants), `homophone` — per the `cross-reference-entry` skill. The authoritative list lives in `build/constants.py`; `transitivity_pair` and `formality_variant` are **not** valid and will fail schema validation.
- [ ] **Back-link symmetry on direct neighbors**: for each entry referenced in `cross_references` and `prominent_see_also`, open the neighbor and confirm a back-link exists when one is appropriate. Add it if missing. Update the neighbor's `modified` timestamp. **Do NOT polish the neighbor further. Do NOT recurse.**

### Tier 3 — nice-to-have (style, polish)

- [ ] Example sentences sound natural and demonstrative; rewrite weak ones
- [ ] Notes appropriately long for entry complexity (expand if too thin, trim if redundant)
- [ ] When rewriting examples or notes, ensure the new content also has full inline link coverage (this is enforced as part of tier 1 — full coverage is required for the entry as a whole regardless of which tier added the text)

## Long-term tracking

While polishing, capture things that go beyond the current entry. These are how the dictionary improves at a higher level over time.

### Words missing entries

When you encounter a word in an example or note that doesn't have an entry yet, add it to candidates immediately:

```bash
python3 build/manage_candidates.py add "word" "reading" "brief gloss; seen in entry XXXXX"
```

Words found this way are the **highest-priority candidates** for new-entry sessions — they create internal completeness in the dictionary's vocabulary. Mention "seen in entry XXXXX" in the note so new-entry sessions know the source.

### Systemic patterns and longer-horizon ideas

Append observations to `polishing/observations.md` using the tag conventions documented at the top of that file:

- `[pattern]` — systemic issue across entries
- `[wiki]` or `[wiki:page-name]` — knowledge-base content
- `[article]` — possible expository article topic
- `[tooling]` — script or tool improvement idea
- `[skill]` — skill update needed
- `[entry]` — entry that needs more work than this session has budget for

The daily wiki-maintenance session harvests this file.

### Wiki consultation

Before starting, glance at `planning/wiki/index.md` for any wiki page relevant to the entries you're about to polish (e.g., transitivity, loanwords, a semantic field). Read the relevant page only if it's directly applicable. **Don't read the whole wiki.**

## Session-end workflow

**Single-build rule.** Run `make build` exactly once per session. If you spot a wrong inline link, wrong homograph entry ID, or any other error after the build has completed, do NOT fix it in this session — append a one-line `[entry]` note to `polishing/observations.md` (e.g., `[entry] 00329 oginau: 合う link points to 09500_au, should be 10466_au`) and continue to the push / PR / merge sequence on the SHA you already built. Fix-up commits are the single biggest cause of stranded PRs: they force a second `make build` (which floods the session with `docs/` diff output), a second push, and a second CI wait, and the merge call usually doesn't survive the resulting context burn.

1. **Update `polishing/tasks/comprehensive/progress.txt`** with the next entry ID:
   ```
   next: XXXXX
   ```
2. **Write a session log** to `polishing/sessions/comprehensive_{YYYY-MM-DD}_{NNN}.md` (use the next available NNN — check `ls polishing/sessions/comprehensive_* 2>/dev/null`):
   ```
   ## Session: Comprehensive Polish
   Date: YYYY-MM-DD
   Entries processed: 12345 through 12372 (24 entries)

   ### Per-entry changes
   - 12345 (word): tier-1 fixes (furigana on note, full inline link coverage in examples and notes); expanded notes; added cross-ref to 67890
   - 12346 (word): added inline links throughout notes (8 new links, 2 noentry); added 2 examples with full link coverage; back-link added on 11111
   - 12347 (word): completed inline link coverage in notes; tier-1 only (entry was otherwise clean)
   - ... (one bullet per entry)

   ### Candidates added
   - "新しい単語" (あたらしいたんご): seen in 12345 examples
   - ... (each candidate added when a noentry marker was used)

   ### Observations logged
   - [pattern] ...
   - [wiki] ...

   ### Next entry
   12373
   ```
3. **Append to `polishing/observations.md`** if you have observations (use the template in that file).
4. **Run the full build**:
   ```bash
   make build
   ```
   This validates entries, updates indexes, and rebuilds the static site.
5. **Commit and push** to the session's feature branch. Stage everything including build artifacts (`git add -A`), commit with a clear message, then `git push -u origin <branch>`. The PR must contain both source changes and rebuilt site files (`docs/`, `entries_index.json`, `build/word_id_lookup.json`, `kanji/`).

6. **Create the PR, wait for CI, then merge it yourself.** This is the step that previously broke the hourly Routine — sessions created PRs but the merge never happened, so progress on `main` never advanced and subsequent sessions redid the same range. **Do not stop after creating the PR.** The full sequence (details in `CLAUDE.md` → "End-of-session PR and merge workflow"):

   **Atomic-tail rule.** After `git push`, the rest of the session is exactly: `mcp__github__create_pull_request` → poll `mcp__github__pull_request_read` (`method: "get_check_runs"`) until green, spacing polls with a backgrounded `sleep 30` → `mcp__github__merge_pull_request` with `merge_method: "squash"`. Do not interleave any other tool. If you find yourself wanting to read an entry file, edit one, or re-run a build script between push and merge, stop — log the concern and proceed to merge instead.

   **Routine / unattended (default — `gh` is not authorized):**
   1. Call `mcp__github__create_pull_request` (`owner: "tkgally"`, `repo: "je-dict-1"`, `head: "<your branch>"`, `base: "main"`, plus title and body). Note the PR number from the response URL.
   2. **Wait for CI by polling check-runs over MCP** (`pipeline/wait-for-pr-checks.sh` returns HTTP 403 in this environment — do not use it; full loop in `CLAUDE.md` → "MCP path" step 5). Call `mcp__github__pull_request_read` with `method: "get_check_runs"` (**not** `get_status`, which is blind to Actions checks and always reads `pending` here). Classify: *green* = `total_count >= 1` and every run `completed` with `conclusion` `success`/`neutral`/`skipped`; *failed* = any other completed conclusion; *pending* = otherwise. While pending, wait with a backgrounded `sleep 30` (Bash `run_in_background: true`, since foreground `sleep` is disabled) and re-poll, up to ~16 times (~8 min — CI often takes 3–6 min just to start, then ~60 s).
   3. **Merge** based on the result:
      - **green**: call `mcp__github__merge_pull_request` with `merge_method: "squash"`. The session is now done.
      - **failed**: leave the PR open, add a brief sentence to the session log naming the failed check, and stop. The curator will investigate.
      - **still pending at the cap**: leave the PR open and stop; the next run's §0a rescue merges it once green.
   4. **Do not** `git checkout main`, **do not** delete the feature branch — the session is running on that branch, and the repo's "Automatically delete head branches" setting handles remote cleanup once the merge fires.

   Do not call `mcp__github__enable_pr_auto_merge` — it requires the PR to already be in a "clean" mergeable state, which is not true immediately after pushing, so it usually rejects. Wait + merge is the reliable path.

   **Interactive (only when `gh` is on PATH):** use the `gh` path documented in `CLAUDE.md` (`gh pr create` → `gh pr checks --watch --fail-fast` → `gh pr merge --squash` → checkout-main cleanup).

## Useful commands

```bash
python3 build/get_timestamp.py             # Run before saving each modified entry
python3 build/verify_furigana.py <id>      # Single-entry furigana check
python3 build/validate.py --id <id>        # Single-entry schema/tag check
python3 build/check_duplicate.py "word" "reading"
python3 build/manage_candidates.py add "word" "reading" "gloss; seen in NNNNN"
python3 build/get_entry_path.py <reading> <id>
make build                                 # End-of-session full build
```

## What this prompt replaces

- `polish_furigana_completeness.md`
- `polish_furigana_correctness.md` (do as part of tier 1 reviews; multi-model review remains separate)
- `polish_example_sentences.md`
- `polish_add_inline_links.md`
- `add_cross-references.md`
- `polish_semantic_labels.md`
- `polish_verb_transitivity.md`
- `polish_aspect_notes.md`
- `expand-short-notes.md`

The targeted prompts above remain in the repository for occasional special-purpose sweeps, but comprehensive polish is now the default ongoing improvement task. The new-entries workflow (`prompts/newentries.md`) is unchanged but should now prefer candidates marked with "seen in entry XXXXX" in their notes.
