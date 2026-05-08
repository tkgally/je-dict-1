# Comprehensive Polish

The **default ongoing-improvement task** for je-dict-1. Each session walks through a small batch of dictionary entries and applies a tiered checklist that unifies the work previously split across the targeted `polish_*` prompts (furigana, examples, inline links, cross-references, semantic labels, transitivity, aspect, expand-short-notes). It also surfaces words and patterns for follow-up so that long-term improvements accumulate over time.

This prompt is designed to be run repeatedly on a schedule. Each invocation picks up where the last one left off.

## Per-session budget (hard limits)

- **Process up to 5 entries per session.** Stop early if context starts getting tight; doing 3 entries thoroughly is better than 5 superficially.
- **No recursion when checking back-links.** Visit direct neighbors only (the entries listed in `cross_references` and `prominent_see_also`). Do **not** follow the neighbors' own links.
- **Don't restructure entries that need major work.** If an entry is broken in a way that would consume the whole session (e.g., wrong POS, fundamentally misclassified), make any quick tier-1 fixes, log it as `[entry]` in `polishing/observations.md`, and move on.

## Entry selection

1. Read `polishing/tasks/comprehensive/progress.txt` for the `next:` value.
2. Process entries sequentially from that ID. If a numeric ID has no entry file, advance to the next existing one. (Use `ls entries/{range}/` to find existing IDs.)
3. At session end, update `progress.txt` to point to the entry **after** the last one you processed.

This produces a steady forward sweep through the dictionary. When the sweep wraps around (years from now), we'll add a recency check; for now, sequential is fine.

## Per-entry checklist

For each entry, work through the three tiers below. **Do all of tier 1**, do as much of tier 2 as time allows (prioritizing the highest-impact items for that specific entry), and do tier 3 only if the entry is otherwise in good shape.

### Tier 1 — must-do (mostly mechanical)

- [ ] **Schema valid**: `python3 build/validate.py --id <entry_id>`
- [ ] **Furigana complete** in headword, examples, AND notes: `python3 build/verify_furigana.py <entry_id>`
- [ ] **Reading is hiragana only** (long-vowel ー allowed)
- [ ] **Romaji matches the full reading**, no internal underscores beyond schema's allowance
- [ ] **All inline links `⟦…⟧` resolve** to real entries — check IDs against `build/word_id_lookup.json`
- [ ] **All `cross_references` and `prominent_see_also` point to existing entries**
- [ ] **Examples have valid `sense_numbers`**
- [ ] **No obvious typos** in headword, reading, gloss, or English translations of examples

If you fix any tier-1 issue, run `python3 build/get_timestamp.py` and update the entry's `modified` timestamp before saving.

### Tier 2 — should-do (judgment, high-leverage)

- [ ] **Example count meets the tier minimum**: 3 per sense for general, 5 per sense for basic/core. Add examples if short.
- [ ] **Examples follow tier-appropriate vocabulary restrictions** (see `.claude/skills/example-sentences/SKILL.md`)
- [ ] **Examples progress short → long**
- [ ] **Notes are well-formed** per `.claude/skills/vocabulary-notes/SKILL.md` — clear sections, no redundancy, no English-only fluff for a Japanese learner's dictionary, no Japanese explanatory prose
- [ ] **Verb-specific** (when applicable): transitivity tag set; transitivity pair linked in `cross_references` if one exists; aspect/ている behavior documented in notes if non-obvious
- [ ] **Na-adjective specific** (when applicable): notes describe -na vs -ni vs predicate forms
- [ ] **Tags accurate**: `semantic`, `formality`, `politeness` reflect the word's actual character (not template defaults)
- [ ] **Cross-references include obvious neighbors**: synonyms, antonyms, transitivity pairs, register variants. Use `synonym`, `antonym`, `related`, `contrast`, `formality_variant`, `transitivity_pair` per the `cross-reference-entry` skill.
- [ ] **Back-link symmetry on direct neighbors**: for each entry referenced in `cross_references` and `prominent_see_also`, open the neighbor and confirm a back-link exists when one is appropriate. Add it if missing. Update the neighbor's `modified` timestamp. **Do NOT polish the neighbor further. Do NOT recurse.**

### Tier 3 — nice-to-have (style, polish)

- [ ] Example sentences sound natural and demonstrative; rewrite weak ones
- [ ] Notes appropriately long for entry complexity (expand if too thin, trim if redundant)
- [ ] **Inline word links** `⟦surface→base：entry_id⟧` added to interesting words in examples and notes — only when the linked entry already exists. Words that should have entries but don't go to candidates instead (see below).

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

1. **Update `polishing/tasks/comprehensive/progress.txt`** with the next entry ID:
   ```
   next: XXXXX
   ```
2. **Write a session log** to `polishing/sessions/comprehensive_{YYYY-MM-DD}_{NNN}.md` (use the next available NNN — check `ls polishing/sessions/comprehensive_* 2>/dev/null`):
   ```
   ## Session: Comprehensive Polish
   Date: YYYY-MM-DD
   Entries processed: ID1, ID2, ID3, ID4, ID5

   ### Per-entry changes
   - 12345 (word): tier-1 fixes (furigana on note); expanded notes; added cross-ref to 67890
   - 12346 (word): added 2 examples; back-link added on 11111
   - ...

   ### Candidates added
   - "新しい単語" (あたらしいたんご): seen in 12345 examples
   - ...

   ### Observations logged
   - [pattern] ...
   - [wiki] ...

   ### Next entry
   12350
   ```
3. **Append to `polishing/observations.md`** if you have observations (use the template in that file).
4. **Run the full build**:
   ```bash
   make build
   ```
   This validates entries, updates indexes, and rebuilds the static site.
5. **Commit and push** following the **End-of-session PR and merge workflow** in `CLAUDE.md` (commit including `docs/` and other build artifacts, push to the feature branch, create a PR with `gh pr create --repo tkgally/je-dict-1 ...`, wait for CI with `--watch --fail-fast`, squash-merge, then clean up the local and remote branch).

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
