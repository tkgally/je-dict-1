---
name: verb-entry
description: Requirements for creating or revising verb entries in je-dict-1. Covers transitivity, aspect/ている behavior, particle patterns, and collocations.
---

# Verb Entry Requirements

**Reminder:** Write each entry individually by hand. Do not use scripts to mass-produce entries. See `entry-guidelines` skill.

When creating or revising VERB entries, include all of the following:

## Required Sections (HIGH PRIORITY)

### 1. Transitivity Information
Every verb MUST specify transitivity and its pair:

```
TRANSITIVITY:
- Type: Intransitive ({自動詞|じどうし}) / Transitive ({他動詞|たどうし})
- Pair: [pair verb with reading] (if exists)
- Pattern: Xが[verb] / Xを[verb]
```

**Common pairs to know:**
- 開く/開ける, 閉まる/閉める, 始まる/始める, 終わる/終える
- 出る/出す, 入る/入れる, 付く/付ける, 消える/消す
- 割れる/割る, 壊れる/壊す, 決まる/決める, 変わる/変える

### 2. Aspect/ている Behavior
Explicitly state what ている means for this verb:

```
ASPECT:
- Type: Telic (has endpoint) / Atelic (ongoing)
- ている meaning: Resulting state / Ongoing action / Both
- Example: [verb]ている = [meaning]
```

**Critical verbs needing aspect notes:**
- 知る → 知っている means "know" (state), not "is learning"
- 結婚する → 結婚している means "is married" (state)
- 死ぬ → 死んでいる means "is dead" (state)
- 持つ → 持っている means "have" (state)

### 3. Core Particle Patterns
Show which particles the verb takes:

```
PARTICLE PATTERNS:
- [noun]が[verb] - [meaning]
- [noun]を[verb] - [meaning]
- [noun]に[verb] - [meaning]
```

### 4. Common Collocations
List 2-3 typical noun pairings:

```
COMMON PATTERNS:
- {時間|じかん}がかかる (takes time)
- {手間|てま}がかかる (takes effort)
- {お金|おかね}がかかる (costs money)
```

## Medium Priority Sections

### 5. Register Label
Mark as: Casual / Neutral / Formal

### 6. Negative Usage Notes
State when the verb is NOT used:

```
WHEN NOT USED:
- {降|ふ}る: Only for precipitation, never for objects falling
- Use {落|お}ちる for objects dropping
```

### 7. Keigo Cross-References (for common verbs)
Link to honorific alternatives:
- {食|た}べる → {召|め}し{上|あ}がる / いただく
- {来|く}る → いらっしゃる

## Template for Notes Section

**Important:** Follow the formatting guidelines in the `vocabulary-notes` skill for proper structure.

```
[Verb] is [transitivity type]. The transitive/intransitive pair is [pair verb].

ASPECT (ている):
[explanation of aspect behavior]

COMMON PATTERNS:
- [collocation 1]
- [collocation 2]
- [collocation 3]

[Any register notes, negative usage, or keigo references]
```

## Sense Numbers in Examples

For verbs with multiple senses (e.g., different meanings or usages), each example must include a `sense_numbers` field:

```json
"examples": [
  {
    "id": "verb_00001_ex1",
    "japanese": "...",
    "english": "...",
    "sense_numbers": [1]
  }
]
```

**Guidelines for verb entries:**
- Each example should clearly demonstrate the sense it's tagged with
- Transitivity-related examples typically share the same sense
- Figurative vs. literal uses often require different sense numbers
- Idiomatic expressions may warrant their own sense

## Quality Checklist for Verbs

- [ ] **All kanji have furigana** (headword, examples, AND notes)
- [ ] Verify: `python3 build/verify_furigana.py <entry_id>` shows "✓ OK"
- [ ] Transitivity clearly marked (自動詞/他動詞)
- [ ] Pair verb identified (if exists)
- [ ] Aspect/ている behavior explained
- [ ] Core particle patterns shown
- [ ] At least 2 collocations listed
- [ ] Examples show the verb in natural contexts
- [ ] Irregular conjugations noted (行く→行って, etc.)
- [ ] All examples have valid sense_numbers
