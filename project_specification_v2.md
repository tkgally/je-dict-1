# je-dict-1: Project Specification v2

*Updated based on multi-model LLM evaluation findings (January 2026)*

---

## Overview

This specification incorporates feedback from a comprehensive evaluation of the je-dict-1 dictionary conducted using three LLM models (Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash) across 4 evaluation rounds. The evaluation reviewed 90 entries total (30 per model) representing all major parts of speech.

**Key Finding**: The dictionary is already strong. These recommendations elevate it from a "good explanatory dictionary" to a best-in-class intermediate learner reference.

---

## 1. Prioritized Task List

### HIGH PRIORITY (Critical for intermediate learner success)

#### 1.1 Add Transitivity Pairs to All Verb Entries
**Task**: Create a dedicated "TRANSITIVITY PAIR" section in every verb entry showing the counterpart form.

**Implementation**:
```
TRANSITIVITY:
• Type: Intransitive (自動詞)
• Pair: 割る (to break something)
• Pattern: Xが割れる (X breaks)
```

**Rationale**: All evaluators identified transitive/intransitive distinction as the #1 learner hurdle.

#### 1.2 Add Common Collocation Patterns
**Task**: Add a "COMMON PATTERNS" section showing what nouns/structures naturally pair with each verb.

**Implementation**:
```
COMMON PATTERNS:
• 時間がかかる (time takes)
• お金がかかる (money costs)
• 手間がかかる (effort takes)
```

**Rationale**: Intermediate learners know words individually but struggle with natural collocations.

#### 1.3 Add Aspect/Actionality Notes
**Task**: Explicitly state whether each verb is telic (has endpoint) or atelic (ongoing), and how it behaves with ている.

**Implementation**:
```
ASPECT NOTE:
• Telic verb (has clear endpoint)
• With ている: expresses resulting state
• Example: 割れている = it is broken (not "is breaking")
```

**Rationale**: Critical for understanding why ている means different things for different verbs.

#### 1.4 Clarify Particle Behavior with Specific Verbs
**Task**: For particle entries (が, に, etc.), add explicit lists of verbs/adjectives that require them.

**Implementation**:
```
VERBS/ADJECTIVES REQUIRING が:
• できる (can do)
• 分かる (understand)
• 好き (like)
• 欲しい (want)
• 得意 (good at)
• 上手 (skilled at)
```

**Rationale**: High-value addition addressing notoriously difficult grammar point.

#### 1.5 Fix Depth Inconsistency Across Entries
**Task**: Audit entry groups and bring weaker entries up to the level of the strongest ones.

**Examples of target consistency**:
- If 知る explains aspect deeply, 割れる and 来る should too
- If に particle has 5 senses with examples, が should match that depth

---

### MEDIUM PRIORITY (Significant improvement to depth and usability)

#### 2.1 Add Register/Pragmatic Tone Labels
**Task**: Mark entries as casual, neutral, formal, or emphatic where relevant.

**Implementation**: Add one-line notation: `[Register: Casual]`

**Affected entries**: すごい (very casual), 親切 (neutral/formal), interjections

#### 2.2 Expand Contrastive Cross-References
**Task**: Add "SIMILAR WORDS" section for semantically overlapping terms.

**Examples**:
- 楽 vs. 簡単 vs. 易しい (all mean "easy" but differ)
- 嬉しい vs. 楽しい (happiness vs. enjoyment)
- 困る vs. 大変 (troubled vs. difficult)

#### 2.3 Add Negative/Constraint Notes
**Task**: Explicitly state when a verb is NOT used or has restricted usage.

**Implementation**:
```
WHEN NOT USED:
• 降る: Only for precipitation, never for objects falling
• Use 落ちる for objects dropping
```

#### 2.4 Standardize Adjective Morphology Information
**Task**: For all adjectives, consistently include:
- Adverbial form (〜く / 〜に)
- Noun form (〜さ) where natural

**Implementation**:
```
FORMS:
• Adverbial: 遠く
• Noun: 遠さ
```

#### 2.5 Improve Example Sentence Progression
**Task**: Ensure examples progress from simple to complex.

**Guidelines**:
- First example = maximally simple
- Later examples = natural but more complex
- At least one example should reflect a fixed or high-frequency phrase

---

### LOW PRIORITY (Polish and consistency)

#### 3.1 Add Kanji Orthography Notes
**Task**: For entries with multiple writing systems, clarify when to use kanji vs. hiragana.

**Example**: すごい - Note that 凄い is rarely written in kanji in casual contexts

#### 3.2 Add Cultural/Contextual Notes
**Task**: Expand cultural notes where significant (e.g., bowing culture for 下げる)

#### 3.3 Add Keigo Cross-References (Selectively)
**Task**: For very common verbs, link to honorific alternatives:
- 食べる → 召し上がる / いただく
- 来る → いらっしゃる

---

## 2. Systematic Changes by Entry Type

### For ALL Verb Entries

| Field | Priority | Description |
|-------|----------|-------------|
| Transitivity + Pair | HIGH | Mark 自動詞/他動詞, list pair verb |
| Core Particle Patterns | HIGH | Show A が V, A を V patterns |
| Aspect Behavior | HIGH | ている meaning (state vs. ongoing) |
| Common Collocations | MEDIUM | 2-3 typical noun pairings |
| Negative Usage Notes | MEDIUM | When meaning shifts with ない |
| Register | MEDIUM | Casual/Neutral/Formal |

### For ALL Adjective Entries

| Field | Priority | Description |
|-------|----------|-------------|
| Conjugation Paradigm | MEDIUM | Affirmative, Negative, Te-form, Past |
| Predicate vs. Modifier Bias | MEDIUM | Which form is more common |
| Adverbial Form | MEDIUM | 〜く or 〜に form |
| Noun Form | LOW | 〜さ form where natural |
| Similar Words | MEDIUM | Contrastive distinctions |

### For ALL Particle Entries

| Field | Priority | Description |
|-------|----------|-------------|
| Verbs Requiring This Particle | HIGH | Explicit list with examples |
| Contrast with Similar Particles | HIGH | は vs. が, に vs. へ, etc. |
| New vs. Old Information | HIGH | For は/が specifically |
| Fixed Patterns | MEDIUM | 〜てから, 〜までに, etc. |

### For ALL Counter Entries

| Field | Priority | Description |
|-------|----------|-------------|
| Full Counting Pattern (1-10) | MEDIUM | Table with all readings |
| Irregular Readings | MEDIUM | Highlight exceptions |
| Sound Changes | MEDIUM | Rendaku, sokuon patterns |

### For ALL Noun Entries

| Field | Priority | Description |
|-------|----------|-------------|
| Common Collocations | MEDIUM | Typical verb pairings |
| Counter | LOW | Which counter(s) to use |
| Scope Clarification | LOW | When meaning differs from English |

---

## 3. Schema Additions

### New Fields for Verb Entries

```json
{
  "transitivity": {
    "type": "intransitive|transitive|both",
    "pair": "entry_id of pair verb",
    "pattern": "A が 割れる"
  },
  "aspect": {
    "type": "telic|atelic",
    "teiru_meaning": "resulting state|ongoing action|both",
    "note": "Optional clarification"
  },
  "collocations": [
    {"noun": "時間", "pattern": "時間がかかる", "meaning": "takes time"}
  ],
  "register": "casual|neutral|formal|emphatic",
  "not_used_for": ["Description of when NOT to use this word"]
}
```

### New Fields for Adjective Entries

```json
{
  "forms": {
    "adverbial": "遠く",
    "noun": "遠さ"
  },
  "conjugation": {
    "negative": "遠くない",
    "te_form": "遠くて",
    "past": "遠かった"
  },
  "predicate_vs_modifier": "predicate preferred|modifier preferred|equal",
  "similar_words": [
    {"word": "長い", "distinction": "遠い is for distance, 長い is for length/time"}
  ]
}
```

### New Fields for Particle Entries

```json
{
  "requires_particle": [
    {"predicate": "できる", "example": "日本語ができる"},
    {"predicate": "分かる", "example": "意味が分かる"}
  ],
  "contrast": [
    {"particle": "は", "distinction": "が marks new information, は marks topic"}
  ],
  "fixed_patterns": [
    {"pattern": "〜てから", "meaning": "after doing"}
  ]
}
```

---

## 4. Feature Recommendations

### 4.1 Learner Pitfall Callout Boxes
Add highlighted warnings for common mistakes:
```
⚠️ LEARNER PITFALL:
知る = learning a fact for the first time
知っている = already knowing
→ Use 知っている for "I know"
```

### 4.2 Pattern Highlight Boxes
Visually separate grammar patterns:
```
PATTERN: 時間がかかる
```

### 4.3 Natural Conversation Mini-Dialogues
Add 2-3 line exchanges for high-frequency words:
```
A: 何か困ったことはありますか？
B: 実は、日本語の文法で困っています。
```

### 4.4 Cross-Entry Linking
Implement clickable links between:
- Transitive/intransitive pairs
- Semantic neighbors (思う ↔ 考える)
- Related word families

### 4.5 Semantic Spectrum Diagrams
For overlapping adjectives:
```
EASY (難度スペクトラム):
楽 ←→ 簡単 ←→ 易しい
(comfortable) (straightforward) (gentle/simple)
```

---

## 5. Quality Guidelines for Future Entries

### Content Guidelines

1. **Explain before exemplifying** - Definition first, then examples
2. **One meaning = one example minimum** - Every sense needs illustration
3. **Show grammatical connections** - Always demonstrate how words connect
4. **Prefer natural Japanese** - Avoid textbook stiffness
5. **Highlight non-obvious distinctions** - Focus on what learners cannot infer from English

### Consistency Guidelines

1. **Consistent depth across similar entries** - Don't over-explain one verb while under-explaining another
2. **Consistent structure within entry types** - All verbs should have same sections
3. **Consistent terminology** - Use same labels throughout (USAGE NOTES, not sometimes Notes)

### Example Sentence Guidelines

1. **First example should be simple** - Demonstrate the word clearly without complexity
2. **Progress to natural complexity** - Later examples can show real-world usage
3. **Include at least one fixed phrase** - High-frequency collocations aid memory
4. **Annotate non-obvious grammar** - Use [Note: ...] for grammatical explanations

---

## 6. Implementation Roadmap

### Phase 1: High Priority Fixes (Immediate)
- [ ] Add transitivity information to all verb entries
- [ ] Add aspect notes to verbs with non-obvious ている behavior
- [ ] Expand particle entries with predicate requirements
- [ ] Add core collocation patterns to high-frequency verbs

### Phase 2: Medium Priority Enhancements
- [ ] Add register labels to all entries
- [ ] Create contrastive sections for semantic neighbors
- [ ] Standardize adjective morphology information
- [ ] Add conjugation paradigms to adjectives

### Phase 3: Schema Updates
- [ ] Implement new schema fields
- [ ] Migrate existing entries to new format
- [ ] Update validation scripts

### Phase 4: Feature Implementation
- [ ] Add learner pitfall callout styling
- [ ] Implement cross-entry linking
- [ ] Add pattern highlight boxes

---

## Appendix: Evaluation Summary

- **Models Used**: Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash Preview
- **Entries Evaluated**: 90 (30 per model, non-overlapping)
- **Rounds Conducted**: 4 (Fresh Eyes → Informed → Deep Analysis → Synthesis)
- **Key Themes Across All Models**:
  1. Transitivity/intransitivity is critical for intermediate learners
  2. Aspect behavior with ている needs explicit explanation
  3. Particle usage with specific predicates should be explicit
  4. Collocations and patterns are as important as definitions
  5. Consistency across entries matters more than individual excellence

---

*Specification version: 2.0*
*Based on multi-model evaluation completed: January 2026*
