---
name: verb-entry
description: Requirements for creating or revising verb entries in je-dict-1. Covers transitivity, aspect/ている behavior, particle patterns, and collocations.
---

# Verb Entry Requirements

**Reminder:** Write each entry individually by hand. Do not use scripts to mass-produce entries. See `entry-guidelines` skill.

When creating or revising VERB entries, include all of the following:

## Conjugation Field (REQUIRED)

Every verb entry must include a `conjugation` field with the full set of conjugated forms. See the `verb-conjugations` skill for the complete specification.

After creating a verb entry, run `python3 build/add_conjugations.py` to generate the conjugation data, or include it directly. Also ensure `metadata.tags.verb_class` is set (e.g., `"godan-ku"`, `"ichidan"`, `"suru"`).

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

**Pair linking**: Use `prominent_see_also` (NOT `cross_references`) to link transitive/intransitive pair verbs. The `note` field should indicate what the *target* entry is ("transitive" or "intransitive"). Always verify the back-link exists on the pair entry.

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

**Reference list of verbs with non-obvious ている behavior:**

Resultative state (ている = "is in the state of having done X"):
- {結婚|けっこん}する → {結婚|けっこん}している = is married
- {死|し}ぬ → {死|し}んでいる = is dead
- {座|すわ}る → {座|すわ}っている = is seated
- {立|た}つ → {立|た}っている = is standing
- {持|も}つ → {持|も}っている = has/possesses
- {着|き}る → {着|き}ている = is wearing
- {住|す}む → {住|す}んでいる = lives (at)
- {太|ふと}る → {太|ふと}っている = is fat/overweight
- {痩|や}せる → {痩|や}せている = is thin
- {開|あ}く → {開|あ}いている = is open
- {閉|し}まる → {閉|し}まっている = is closed
- {壊|こわ}れる → {壊|こわ}れている = is broken
- {決|き}まる → {決|き}まっている = is decided
- {似|に}る → {似|に}ている = resembles
- {慣|な}れる → {慣|な}れている = is accustomed
- {疲|つか}れる → {疲|つか}れている = is tired
- {落|お}ちる → {落|お}ちている = is on the ground (has fallen)
- {並|なら}ぶ → {並|なら}んでいる = is lined up
- {曲|ま}がる → {曲|ま}がっている = is bent/curved
- {混|こ}む → {混|こ}んでいる = is crowded
- {起|お}きる → {起|お}きている = is awake
- {売|う}れる → {売|う}れている = is popular / sells well
- {届|とど}く → {届|とど}いている = has arrived (is there)
- {始|はじ}まる → {始|はじ}まっている = has started (is underway)
- {終|お}わる → {終|お}わっている = is over/finished

Knowledge/cognitive state (ている = current mental state):
- {知|し}る → {知|し}っている = knows (negative: {知|し}らない, NOT {知|し}っていない)
- {覚|おぼ}える → {覚|おぼ}えている = remembers
- {信|しん}じる → {信|しん}じている = believes
- {分|わ}かる → {分|わ}かっている = understands (already)

Habitual (ている = regularly does X):
- {勤|つと}める → {勤|つと}めている = works at / is employed at
- {通|かよ}う → {通|かよ}っている = attends regularly / commutes to
- {付|つ}き{合|あ}う → {付|つ}き{合|あ}っている = is dating / is in a relationship

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

- [ ] **All kanji have furigana** (headword, examples, AND notes)
- [ ] Verify: `python3 build/verify_furigana.py <entry_id>` shows "✓ OK"
- [ ] **Tags complete**: pos, transitivity, verb_class, formality, politeness, semantic
- [ ] **Conjugation field present** with full forms (see `verb-conjugations` skill)
- [ ] Transitivity clearly marked (自動詞/他動詞)
- [ ] Pair verb identified (if exists)
- [ ] Aspect/ている behavior explained
- [ ] Core particle patterns shown
- [ ] At least 2 collocations listed
- [ ] Examples show the verb in natural contexts
- [ ] Irregular conjugations noted (行く→行って, etc.)
- [ ] All examples have valid sense_numbers
