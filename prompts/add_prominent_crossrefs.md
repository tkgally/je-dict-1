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
- Words with different POS that a learner wouldn't confuse (e.g., 木 tree / 気 spirit / 〜機 machine — all different concepts and POS)
- Words in very different registers or domains that wouldn't be confused in practice

## Session Workflow

### Phase 1: Get candidate pairs

```bash
python3 build/find_merge_candidates.py --crossref-only --json > /tmp/crossrefs.json
```

The script checks both `cross_references` and `prominent_see_also` on the actual entry files. Pairs that already have references in either field are excluded from the output, so the output only shows pairs that still need work.

The JSON output contains objects with `type` being either `noun_suru_pair` or `homophone_pair`.

### Phase 2: Filter to remaining work

Use a Python script to parse the JSON and filter to pairs that still need `prominent_see_also`. Group by reading for efficient evaluation.

```python
import json

with open('/tmp/crossrefs.json') as f:
    data = json.load(f)

crossrefs = data.get('missing_crossrefs', [])
noun_suru = [cr for cr in crossrefs if cr['type'] == 'noun_suru_pair']
homophones = [cr for cr in crossrefs if cr['type'] == 'homophone_pair']

print(f"Noun/する pairs remaining: {len(noun_suru)}")
print(f"Homophone pairs remaining: {len(homophones)}")
```

### Phase 3: Process noun/する pairs first

**Always add prominent references for noun/する pairs** — no evaluation needed. Process all remaining pairs in one batch using a script:

```python
# For each noun/suru pair, add prominent_see_also bidirectionally:
# - On noun: {"target_id": "...", "reading": "...", "headword": "...", "note": "verb form"}
# - On verb: {"target_id": "...", "reading": "...", "headword": "...", "note": "noun form"}
```

### Phase 4: Evaluate homophone pairs

For each homophone pair, ask:
1. **Would a learner plausibly confuse these?** If a student looks up きく, they might reach {聞|き}く when they meant {効|き}く.
2. **Is the distinction important for comprehension?** If confusing the two could lead to a misunderstanding, add prominent references.

**Efficient evaluation**: Process homophones in reading order. For each reading, evaluate all pairs with that reading together. Many can be quickly skipped (different POS, different domains). Write a script to add references in bulk rather than editing files one at a time.

**Common patterns to skip** (not confusable):
- Different POS (noun vs verb vs counter vs prefix)
- Very different domains (e.g., 木 tree vs 気 spirit)
- One word is archaic/rare and the other is common
- Loanword vs native Japanese word with same reading

**Common patterns to add** (confusable):
- Same POS, similar domain (e.g., 制作/製作, 決済/決裁)
- Kanji variants of same word (e.g., 希少/稀少, 戦い/闘い)
- Both are common verbs with same reading (e.g., 切る/着る, 効く/聞く)
- Both are common nouns that learners genuinely mix up (e.g., 人口/人工, 地震/自信)

### Phase 5: Add references via script

Use a Python script to add `prominent_see_also` in bulk. The script should:
- Load entry files
- Add `prominent_see_also` entries bidirectionally
- Skip pairs that already have the reference
- Write updated files

Example helper pattern:

```python
import json, glob

entries = {}
entry_files = {}
for f in glob.glob('entries/*/*.json'):
    with open(f) as fh:
        e = json.load(fh)
        entries[e['id']] = e
        entry_files[e['id']] = f

def add_psa(entry_id, target_id, note):
    """Add a prominent_see_also entry if not already present."""
    e = entries[entry_id]
    t = entries[target_id]
    psa = e.get('prominent_see_also', [])
    if any(p.get('target_id') == target_id for p in psa):
        return False
    psa.append({
        'target_id': target_id,
        'reading': t['reading'],
        'headword': t['headword'],
        'note': note
    })
    e['prominent_see_also'] = psa
    with open(entry_files[entry_id], 'w') as f:
        json.dump(e, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return True

# Define pairs: (id1, id2, note_on_1_pointing_to_2, note_on_2_pointing_to_1)
pairs = [
    ('id1', 'id2', 'note about id2', 'note about id1'),
    # ...
]

for id1, id2, note1, note2 in pairs:
    add_psa(id1, id2, note1)
    add_psa(id2, id1, note2)
```

### Phase 6: Validate and build

```bash
python3 build/validate.py
python3 build/update_indexes.py
python3 build/build_flat.py
```

### Phase 7: Commit

Commit after every 20-30 pairs:

```bash
git add -A && git commit -m "Add prominent cross-references for N homophone/noun-する pairs"
```

## Reference Format

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

## Batch Size

Process 20-30 pairs per commit. A session should process as many batches as context allows.

## Progress Tracking

Progress is tracked automatically by the script — pairs that already have `prominent_see_also` or `cross_references` are excluded from the output. No separate progress file is needed.

Check the most recent session log in `polishing/sessions/prominent_crossrefs_*.md` to see what reading ranges have been covered, so you can continue from where the previous session left off.

## Session Log

Write a session log to `polishing/sessions/prominent_crossrefs_{date}.md`:

```markdown
## Session: Prominent Cross-References
Date: YYYY-MM-DD

### Noun/する Pair References Added
- [noun_id] ↔ [verb_id]: [headword]
- ...

### Homophone References Added
- [id1] ↔ [id2]: [reason]
- ...

### Pairs Evaluated (no action needed)
- [id1] / [id2]: [reason not confusable]
- ...

### Statistics
- Pairs evaluated: N
- References added: N
- Reading range covered: [start] through [end]
```
