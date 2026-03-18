# Add Prominent Cross-References

Scan the dictionary for homophones and easily confused words that should have `prominent_see_also` references — high-visibility links displayed at the top of entry pages.

## What is `prominent_see_also`?

The `prominent_see_also` field is an array of cross-references displayed prominently below the headword, before definitions. Unlike regular `cross_references` (shown at the bottom in "Related Words"), these are immediately visible and help learners who may have landed on the wrong homophone.

## When to Add `prominent_see_also`

Add prominent references when:

1. **Homophones with different kanji that signal different meanings**
   - {聞|き}く (hear) ↔ {聴|き}く (listen attentively)
   - {無|な}くなる (disappear) ↔ {亡|な}くなる (pass away)

2. **Commonly confused word pairs**
   - {初|はじ}めて (for the first time) ↔ {始|はじ}めて (starting from)

3. **Kanji variants where the distinction matters**
   - {匂|にお}い (pleasant smell) ↔ {臭|にお}い (bad smell)

**Do NOT add** `prominent_see_also` for:
- Regular synonyms (use `cross_references` with type `synonym`)
- Transitive/intransitive pairs (use `cross_references` with type `pair`)
- Words that happen to sound similar but aren't confusable

## Session Workflow

### Phase 1: Identify candidates

```bash
python3 build/find_merge_candidates.py --crossref-only
```

Focus on `homophone_pair` entries — these are entries with the same reading but different headwords.

### Phase 2: Evaluate each pair

For each homophone pair, ask:
1. **Would a learner plausibly confuse these?** If a student looks up きく, they might reach {聞|き}く when they meant {聴|き}く.
2. **Is the distinction important for comprehension?** If confusing the two could lead to a misunderstanding, add prominent references.

### Phase 3: Add references

For each entry in the pair, add a `prominent_see_also` field:

```json
"prominent_see_also": [
  {
    "target_id": "00123_kiku_listen",
    "reading": "きく",
    "headword": "{聴|き}く",
    "note": "listen attentively"
  }
]
```

**Requirements:**
- Always include `target_id` when the target entry exists
- Always include a brief `note` explaining the distinction
- The `note` should be in English, concise (2-4 words)
- Add references **bidirectionally** — both entries should point to each other

### Phase 4: Validate and build

```bash
python3 build/validate.py
python3 build/update_indexes.py
python3 build/build_flat.py
```

### Phase 5: Commit

```bash
git add -A && git commit -m "Add prominent cross-references for N homophone pairs"
```

## Batch Size

Process 20-30 pairs per session. Commit after every 10 pairs.

## Session Log

Write a session log to `polishing/sessions/prominent_crossrefs_{date}.md`:

```markdown
## Session: Prominent Cross-References
Date: YYYY-MM-DD

### References Added
- [id1] ↔ [id2]: [reason]
- ...

### Pairs Evaluated (no action needed)
- [id1] / [id2]: [reason not confusable]
- ...

### Statistics
- Pairs evaluated: N
- References added: N
```
