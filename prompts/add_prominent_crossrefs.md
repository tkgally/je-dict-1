# Add Prominent Cross-References

Scan the dictionary for homophones, noun/Nする pairs, and easily confused words that should have `prominent_see_also` references — high-visibility links displayed at the top of entry pages.

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

4. **Noun + Nする verb pairs**
   - {発揮|はっき} (noun: display/demonstration) ↔ {発揮|はっき}する (verb: to demonstrate/exhibit)
   - {挨拶|あいさつ} (noun: greeting) ↔ {挨拶|あいさつ}する (verb: to greet)
   - A learner looking up the noun form should easily find the verb form, and vice versa

**Do NOT add** `prominent_see_also` for:
- Regular synonyms (use `cross_references` with type `synonym`)
- Transitive/intransitive pairs (use `cross_references` with type `pair`)
- Words that happen to sound similar but aren't confusable

## Session Workflow

### Phase 1: Identify candidates

```bash
python3 build/find_merge_candidates.py --crossref-only
```

The output contains two relevant types:

- **`homophone_pair`** — entries with the same reading but different headwords (e.g., {聞|き}く vs. {聴|き}く).
- **`noun_suru_pair`** — a noun N and a corresponding Nする verb where readings differ only by the する suffix (e.g., {発揮|はっき} reading はっき vs. {発揮|はっき}する reading はっきする). These are detected by the script even though the readings are not identical — one is a prefix of the other.

Process both types in each session.

### Phase 2: Evaluate each pair

**For homophone pairs**, ask:
1. **Would a learner plausibly confuse these?** If a student looks up きく, they might reach {聞|き}く when they meant {聴|き}く.
2. **Is the distinction important for comprehension?** If confusing the two could lead to a misunderstanding, add prominent references.

**For noun/する pairs**, always add prominent references. A learner who finds the noun should be able to quickly navigate to the verb form, and vice versa. The `note` should identify the related form:
- On the noun entry: note says "verb form" (or similar)
- On the verb entry: note says "noun form" (or similar)

### Phase 3: Add references

For each entry in the pair, add a `prominent_see_also` field.

**Homophone example:**

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

**Noun/する pair example** (on the noun entry):

```json
"prominent_see_also": [
  {
    "target_id": "17267_hakkisuru",
    "reading": "はっきする",
    "headword": "{発揮|はっき}する",
    "note": "verb form"
  }
]
```

**Requirements:**
- Always include `target_id` when the target entry exists
- Always include a brief `note` explaining the distinction
- The `note` should be in English, concise (2-4 words)
- Add references **bidirectionally** — both entries should point to each other
- For noun/する pairs, use notes like "verb form" / "noun form"

### Phase 4: Validate and build

```bash
python3 build/validate.py
python3 build/update_indexes.py
python3 build/build_flat.py
```

### Phase 5: Commit

```bash
git add -A && git commit -m "Add prominent cross-references for N homophone/noun-する pairs"
```

## Batch Size

Process 20-30 pairs per session. Commit after every 10 pairs.

## Session Log

Write a session log to `polishing/sessions/prominent_crossrefs_{date}.md`:

```markdown
## Session: Prominent Cross-References
Date: YYYY-MM-DD

### Homophone References Added
- [id1] ↔ [id2]: [reason]
- ...

### Noun/する Pair References Added
- [noun_id] ↔ [verb_id]: [headword]
- ...

### Pairs Evaluated (no action needed)
- [id1] / [id2]: [reason not confusable]
- ...

### Statistics
- Pairs evaluated: N
- References added: N
```
