---
name: verb-entry
description: Requirements for creating or revising verb entries in je-dict-1. Covers transitivity, aspect/ている behavior, particle patterns, and collocations.
---

# Verb Entry Requirements

**Reminder:** Write each entry individually by hand. Do not use scripts to mass-produce entries. See `entry-guidelines` skill.

When creating or revising VERB entries, include all of the following:

## Conjugation Field (REQUIRED)

Every verb entry must include a `conjugation` field in the entry JSON. See the `verb-conjugations` skill for the full specification.

**Place the field after `gloss` and before `definitions`.**

Quick examples by verb class:

```json
// Godan: 書く
"conjugation": { "type": "godan", "ending": "く", "stem": "{書|か}" }

// Ichidan: 食べる
"conjugation": { "type": "ichidan", "stem": "{食|た}べ" }

// する verb: 勉強する
"conjugation": { "type": "suru", "prefix": "{勉強|べんきょう}" }

// 来る
"conjugation": { "type": "kuru", "prefix": "" }

// ある
"conjugation": { "type": "aru" }
```

**Determining the stem**: The stem is everything before the conjugating ending, with furigana. For 話す, stem is `{話|はな}` and ending is `す`. For 食べる (ichidan), stem is `{食|た}べ`. For する verbs, prefix is the noun part.

**Irregular verbs**: Add `"overrides": {...}` for non-standard forms (e.g., 行く has irregular て/た forms). See verb-conjugations skill for override keys.

**Also set `verb_class` tag**: When adding conjugation, ensure `metadata.tags.verb_class` is set (e.g., `"godan-ku"`, `"ichidan"`, `"suru"`).

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

## Example Sentences

**See the `example-sentences` skill for complete requirements including:**
- Minimum counts: 5 examples per sense (basic/core) or 3 (general)
- Progressive length: Examples should get longer from first to last
- Vocabulary restrictions by tier
- Quality standards and formatting

### Sense Numbers in Examples

For verbs with multiple senses, each example must include a `sense_numbers` field:

```json
"examples": [
  {
    "id": "00001_verb_ex1",
    "japanese": "...",
    "english": "...",
    "sense_numbers": [1]
  }
]
```

**Verb-specific guidelines:**
- Each example should clearly demonstrate the sense it's tagged with
- Transitivity-related examples typically share the same sense
- Figurative vs. literal uses often require different sense numbers
- Idiomatic expressions may warrant their own sense
- Show particle patterns ({noun}を{verb}, {noun}に{verb}, etc.)
- Demonstrate ている usage where relevant

## Required Tags for Verbs

All verb entries must include these tags in `metadata.tags`:

```json
"metadata": {
  "tags": {
    "pos": ["verb-godan"],           // verb-godan, verb-ichidan, verb-suru, verb-kuru, verb-irregular
    "transitivity": "transitive",    // REQUIRED for verbs: transitive, intransitive, or both
    "formality": "neutral",          // formal, neutral, informal, vulgar
    "politeness": "plain",           // honorific, humble, polite, plain
    "semantic": ["movement"]         // Choose appropriate category
  }
}
```

**Transitivity tag values:**
- `transitive`: Takes a direct object (他動詞) - Xを[verb]
- `intransitive`: No direct object (自動詞) - Xが[verb]
- `both`: Can be used both ways (rare, e.g., 増える/増やす patterns in one verb)

**Semantic categories for verbs:**
- `movement`: 行く, 来る, 歩く, 走る, 泳ぐ
- `communication`: 話す, 聞く, 言う, 読む, 書く
- `cognition`: 思う, 知る, 考える, 覚える, 忘れる
- `existence`: ある, いる, なる, できる
- `consumption`: 食べる, 飲む, 使う, 買う
- `action`: Fallback for verbs not fitting other categories

## Quality Checklist for Verbs

- [ ] **Conjugation field present** with correct type, stem/ending/prefix
- [ ] **verb_class tag set** in metadata.tags (e.g., godan-ku, ichidan, suru)
- [ ] **All kanji have furigana** (headword, examples, AND notes)
- [ ] Verify: `python3 build/verify_furigana.py <entry_id>` shows "✓ OK"
- [ ] **Tags complete**: pos, transitivity, formality, politeness, semantic
- [ ] Transitivity clearly marked (自動詞/他動詞)
- [ ] Pair verb identified (if exists)
- [ ] Aspect/ている behavior explained
- [ ] Core particle patterns shown
- [ ] At least 2 collocations listed
- [ ] Examples show the verb in natural contexts
- [ ] Irregular conjugations noted (行く→行って, etc.)
- [ ] All examples have valid sense_numbers
