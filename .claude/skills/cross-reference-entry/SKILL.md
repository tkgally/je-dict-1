---
name: cross-reference-entry
description: Guidelines for adding and maintaining cross-references between dictionary entries. Covers reference types, format requirements, and extraction from notes.
---

# Cross-Reference Entry Guidelines

When creating or revising entries, add cross-references to related vocabulary. This improves navigation and helps learners understand word relationships.

## Two Cross-Reference Mechanisms

The dictionary has two structured cross-reference systems (plus inline word links, which are handled separately):

### 1. `prominent_see_also` — Top-of-entry links (HIGH VISIBILITY)

Displayed immediately below the headword, before definitions. These are the first thing a learner sees after the headword. Use for word pairs and groups that are **closely related** and which learners are likely to want to navigate between.

**When to use `prominent_see_also`:**

- **Homophones with different kanji** — learners may have landed on the wrong entry
  - {聞|き}く (hear) ↔ {聴|き}く (listen attentively)
  - {無|な}くなる (disappear) ↔ {亡|な}くなる (pass away)
- **Transitive/intransitive verb pairs** — always use `prominent_see_also`, NOT `cross_references`
  - {閉|し}まる (intransitive) ↔ {閉|し}める (transitive)
  - {始|はじ}まる (intransitive) ↔ {始|はじ}める (transitive)
- **N/Nする pairs** — noun form and verb form of the same word
  - {発揮|はっき} (noun) ↔ {発揮|はっき}する (verb)
  - {挨拶|あいさつ} (noun) ↔ {挨拶|あいさつ}する (verb)
- **Informal/formal pairs** — different register forms of the same concept
  - うまい (informal: tasty/skilled) ↔ {美味|おい}しい (standard: tasty)
- **Other closely related pairs/groups** — words that learners are likely to want to learn together
  - {制作|せいさく} (artistic creation) ↔ {製作|せいさく} (manufacturing)
  - {人口|じんこう} (population) ↔ {人工|じんこう} (artificial)

**When NOT to use `prominent_see_also`:**
- Regular synonyms (use `cross_references` with type `synonym`)
- Words that happen to sound similar but aren't confusable in practice
- Words with different POS that a learner wouldn't confuse
- Words in very different registers or domains that wouldn't be confused in practice

**Format:**
```json
"prominent_see_also": [
  {
    "target_id": "00754_shimaru",
    "reading": "しまる",
    "headword": "{閉|し}まる",
    "note": "intransitive"
  }
]
```

- Always include `target_id` when the target entry exists
- Always include a brief `note` in English (2-4 words) explaining the relationship
- Add references **bidirectionally** — both entries should point to each other
- For N/Nする pairs, use notes like "verb form" / "noun form"
- For transitive/intransitive pairs, use notes like "transitive" / "intransitive"
- For homophones, use a brief gloss distinguishing the words

### 2. `cross_references` — "Related Words" box at the bottom (STRUCTURED)

A structured array displayed in a "Related Words" box at the bottom of the entry page. These express **lexicographic relationships** between entries. Two-way linking is encouraged but not as critical as for `prominent_see_also`.

## Cross-Reference Types (for `cross_references`)

### `antonym` — Opposites (HIGH PRIORITY)
Use for direct opposites.

```json
{
  "type": "antonym",
  "reading": "あける",
  "headword": "{開|あ}ける",
  "label": "to open"
}
```

**Label:** Brief gloss of target word

### `keigo` — Honorific/Humble Forms (HIGH PRIORITY)
Use for formal speech equivalents.

```json
{
  "type": "keigo",
  "reading": "めしあがる",
  "headword": "{召|め}し{上|あ}がる",
  "label": "honorific"
}
```

**Labels:** `honorific` or `humble`

**Common keigo links:**
- 食べる → 召し上がる (hon.), いただく (hum.)
- 行く → いらっしゃる (hon.), 参る (hum.)
- 言う → おっしゃる (hon.), 申す (hum.)
- 見る → ご覧になる (hon.), 拝見する (hum.)

### `synonym` — Similar Meaning (MEDIUM PRIORITY)
Use for words with similar meaning but different nuance.

```json
{
  "type": "synonym",
  "reading": "りかいする",
  "headword": "{理解|りかい}する",
  "label": "formal"
}
```

**Label:** Distinguishing characteristic (e.g., "formal", "written", "casual")

### `contrast` — Easily Confused (MEDIUM PRIORITY)
Use for words learners often confuse.

```json
{
  "type": "contrast",
  "reading": "が",
  "headword": "が",
  "label": "subject marking"
}
```

Especially important for:
- Particles: は vs が, に vs で, に vs へ
- Similar verbs: 聞く vs 聴く, 見る vs 見える vs 見せる

### `homophone` — Same Reading, Different Meaning (MEDIUM PRIORITY)
Use for words that share a reading. Note: if the homophones are easily confused, prefer `prominent_see_also` instead.

### `related` — Semantically Connected (LOW PRIORITY)
Use for derived words, compounds, or thematically related vocabulary.

```json
{
  "type": "related",
  "reading": "たべもの",
  "headword": "{食|た}べ{物|もの}",
  "label": "food (noun)"
}
```

### `see_also` — General Reference (LOW PRIORITY)
Use for general cross-references that don't fit other categories.

```json
{
  "type": "see_also",
  "reading": "しょくじ",
  "headword": "{食事|しょくじ}",
  "label": null
}
```

### `pair` — DEPRECATED
**Do not use.** Transitive/intransitive verb pairs should use `prominent_see_also` instead. Existing `pair`-type entries in `cross_references` should be migrated to `prominent_see_also` when entries are revised. The type remains technically valid in the schema but should not appear in new entries.

## Format Requirements

Each `cross_references` entry requires:

| Field | Required | Description |
|-------|----------|-------------|
| `type` | Yes | One of: synonym, antonym, keigo, related, see_also, contrast, homophone (avoid `pair`) |
| `target_id` | No | Hard-coded entry ID for direct resolution (takes priority over reading/headword) |
| `reading` | Yes | Hiragana reading (fallback lookup key when no target_id) |
| `headword` | Yes* | Display form with furigana (required for homonym disambiguation) |
| `label` | No | Short descriptor |

*Headword is **required** for proper resolution. Without it, cross-references cannot be disambiguated between homonyms.

Each `prominent_see_also` entry requires:

| Field | Required | Description |
|-------|----------|-------------|
| `target_id` | No | Hard-coded entry ID for direct resolution |
| `reading` | Yes | Hiragana reading |
| `headword` | Yes | Display form with furigana |
| `note` | Yes | Brief English description of the relationship (2-4 words) |

**Note:** Valid cross-reference types are defined centrally in `build/constants.py` and shared across the schema, validation, and build scripts.

## Hybrid Cross-Reference System

The dictionary uses a **hybrid system** that supports both:
1. **Hard-coded `target_id`** — Direct reference to an entry ID (unambiguous)
2. **Forward references** — References by reading/headword to entries that may not exist yet

### Resolution Priority

When resolving a cross-reference:
1. If `target_id` present AND entry exists → **resolved** (use ID directly)
2. If `target_id` present AND entry missing → **ERROR** (stale reference)
3. If no `target_id` → resolve by reading/headword (may be pending if target doesn't exist)

### When to Use `target_id`

**Use `target_id` when:**
- The target entry exists in the dictionary
- You want guaranteed, unambiguous resolution

**Don't manually add `target_id` when:**
- Creating forward references to entries that don't exist yet
- You're unsure which homonym is correct

Instead, use the `harden_references.py` script to automatically add `target_id` to resolvable references.

### Example with target_id

```json
{
  "type": "antonym",
  "target_id": "00754_shimaru",
  "reading": "しまる",
  "headword": "{閉|し}まる",
  "label": "intransitive"
}
```

### Example forward reference (no target_id)

```json
{
  "type": "antonym",
  "reading": "ひらく",
  "headword": "{開|ひら}く",
  "label": "to open"
}
```

## Homonym Disambiguation

**CRITICAL**: Many Japanese words share the same reading but have different kanji (homonyms). The headword field is essential for correct resolution.

Example: The reading かんじょう has multiple entries:
- {感情|かんじょう} — emotion, feeling
- {勘定|かんじょう} — bill, calculation

**Always include the headword** to ensure cross-references link to the correct entry.

```json
// CORRECT — specifies headword for disambiguation
{
  "type": "synonym",
  "reading": "かんじょう",
  "headword": "{勘定|かんじょう}",
  "label": "bill, calculation"
}

// INCORRECT — no headword, may link to wrong homonym
{
  "type": "synonym",
  "reading": "かんじょう",
  "label": "bill, calculation"
}
```

## When Creating New Entries

When creating new entries (e.g., via `prompts/newentries.md`), add cross-references as part of entry creation:

1. **Always add `prominent_see_also`** for:
   - Transitive/intransitive pair (if both entries exist)
   - N/Nする pair (if both entries exist)
   - Obvious homophones that learners would confuse

2. **Add `cross_references`** for:
   - Direct antonyms
   - Keigo equivalents
   - Close synonyms with clear distinctions
   - Other relevant relationships

3. **Check if the target entry exists** using `check_duplicate.py` or the entries index:
   - If yes: include `target_id` and add a back-link on the target entry
   - If no: create a forward reference (reading + headword only)

4. **For back-links on existing entries**: When you add a cross-reference pointing to an existing entry, also add a reciprocal reference on that target entry pointing back to the new entry.

## Priority Order

When adding references to entries, prioritize:

1. **HIGH** — Always add if applicable:
   - Transitive/intransitive pairs → `prominent_see_also`
   - N/Nする pairs → `prominent_see_also`
   - Easily confused homophones → `prominent_see_also`
   - Keigo equivalents → `cross_references` (keigo)
   - Direct antonyms → `cross_references` (antonym)

2. **MEDIUM** — Add when natural:
   - Close synonyms with clear distinction (synonym)
   - Particle contrasts (contrast)
   - Related compounds (related)

3. **LOW** — Add sparingly:
   - Thematic groupings
   - General see_also references

## Extracting from Notes

The notes field often contains vocabulary that should be cross-referenced. Look for:

### Patterns to Extract

1. **Pair verbs:**
   - "Pair: {閉|し}まる" or "PAIR VERB: ..."
   - "The intransitive counterpart is ..."

2. **Antonyms:**
   - "Opposite: {開|あ}ける"
   - "Antonym: ..."

3. **Keigo:**
   - "{召|め}し{上|あ}がる (honorific)"
   - "Humble form: いただく"

4. **Related words:**
   - Words in furigana notation within COMMON PATTERNS
   - Nouns derived from verbs: 食べる → 食べ物

### Automated Extraction

Run the extraction script to find potential references:

```bash
# Dry run — see proposed changes
python3 build/harvest_crossrefs.py --ids <id,id>   # dry run by default

# Apply changes
python3 build/harvest_crossrefs.py --ids <id,id> --apply

# Single entry
python3 build/harvest_crossrefs.py --ids 00396 --report
```

**Note:** The extraction script now performs immediate resolution. When a target entry exists, the extracted reference automatically includes `target_id`.

### Hardening References

The `harden_references.py` script scans entries and adds `target_id` to resolvable cross-references. This "hardens" forward references into direct ID-based references once the target entry exists.

```bash
# Dry run — see what would change
python3 build/harden_references.py

# Apply changes
python3 build/harden_references.py --apply

# Single entry
python3 build/harden_references.py --id 00485_shimeru
```

**When to run:**
- After adding new entries that are targets of existing forward references
- Periodically to ensure all resolvable references have `target_id`
- Before releases to maximize resolution coverage

## Handling Non-Existent Entries

**Important:** You can add references to entries that don't exist yet.

- Use `reading` as the primary key (required)
- Include `headword` for display purposes
- The link will be marked as "pending" in the web interface
- When the target entry is created, the link automatically becomes active

This allows you to:
- Plan future entries
- Track vocabulary relationships before full coverage
- Show learners related vocabulary even if not yet in dictionary

## Validation

After adding references, validate:

```bash
python3 build/validate.py --id {entry_id}
```

The validator checks:
- Required fields present (type, reading)
- Valid type values
- Reading is valid hiragana
- No self-references
- **Homonym mismatches** — warns when a headword is specified but doesn't match any existing entry with that reading
- **Stale target_id** — ERRORS when `target_id` points to a non-existent entry
- **Hardenable references** — warns when a reference could be hardened (target exists but no `target_id`)

### Validation Messages

| Type | Meaning | Action |
|------|---------|--------|
| ERROR: Stale target_id | `target_id` points to deleted entry | Remove or update `target_id` |
| WARNING: Hardenable | Reference resolvable but missing `target_id` | Run `harden_references.py --apply` |
| WARNING: Homonym mismatch | Headword doesn't match any entry with that reading | Verify correct homonym or wait for entry creation |

## Quality Checklist

- [ ] Transitive/intransitive pair linked via `prominent_see_also` (for verbs)
- [ ] N/Nする pair linked via `prominent_see_also` (if applicable)
- [ ] Homophones linked via `prominent_see_also` (if easily confused)
- [ ] Keigo forms linked (for common verbs)
- [ ] Antonyms linked (if obvious opposite exists)
- [ ] References in notes are also in cross_references
- [ ] Each reference has correct type
- [ ] Reading is valid hiragana
- [ ] Headword uses proper furigana notation
- [ ] Labels/notes are concise and consistent
- [ ] No `pair` type in `cross_references` (use `prominent_see_also` instead)

## Symmetry Requirements

Cross-references should be **bidirectional** for most relationship types. The table below summarizes when back-links are required vs. optional:

| Relationship | Back-link Required? | Via |
|-------------|--------------------|----|
| Transitive/intransitive pair | **Always** | `prominent_see_also` both ways |
| N/Nする pair | **Always** | `prominent_see_also` both ways |
| Homophones (confusable) | **Always** | `prominent_see_also` both ways |
| Antonym | **Usually** | `cross_references` (antonym) both ways |
| Keigo | **Usually** | `cross_references` (keigo) both ways within group |
| Synonym | Case-by-case | `cross_references` (synonym) — add back-link if genuinely helpful |
| Contrast | Case-by-case | `cross_references` (contrast) |
| Related | Optional | `cross_references` (related) |
| See also | Optional | `cross_references` (see_also) |

### Checking symmetry

Use the asymmetry report to find one-way references:
```bash
python3 build/find_merge_candidates.py --asymmetry-only
```

Use the cluster linter to find incomplete semantic groups:
```bash
python3 build/check_semantic_clusters.py
```

### Cluster processing

When fixing symmetry issues, process related entries together as a cluster rather than one at a time. This ensures both sides of a relationship are updated in the same session. See the "Cluster Mode" section in `prompts/add_cross-references.md` for the detailed workflow.
