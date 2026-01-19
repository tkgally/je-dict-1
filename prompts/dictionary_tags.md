# Dictionary Entry Tagging System Implementation

A comprehensive multi-phase workflow for adding grammatical, pragmatic, and semantic tags to all dictionary entries, enabling rich search and export functionality.

## Background

Currently, dictionary entries have minimal metadata:
- `part_of_speech`: Unstructured string with 60+ inconsistent formats
- `vocabulary_tier`: One of "basic", "core", "general"

Users need to search and create lists by multiple criteria including register (formal/informal), semantic category (animals, body parts, days of week), and other attributes. This requires a systematic tagging infrastructure.

---

## Phase 1: Tag Taxonomy Design & Documentation

**Goal**: Define the complete tag vocabulary before implementation.

### 1.1 Grammatical Tags (normalize part_of_speech)

Create a canonical list of part-of-speech values. Map all 60+ current variants to these canonical forms.

**Proposed Canonical Forms**:

| Canonical Value | Current Variants to Map |
|-----------------|-------------------------|
| `noun` | "noun" |
| `verb-godan` | "verb (godan)", "godan verb", "verb (godan, transitive)", "verb (godan, intransitive)", "godan verb, transitive" |
| `verb-ichidan` | "verb (ichidan)", "ichidan verb", "verb (ichidan, transitive)", "verb (ichidan, intransitive)" |
| `verb-suru` | "verb (suru)", "suru-verb" (when standalone) |
| `verb-irregular` | "verb (irregular)" for くる, する |
| `adjective-i` | "i-adjective", "adjective (i-adjective)" |
| `adjective-na` | "na-adjective", "adjective (na-adjective)", "な-adjective" |
| `adverb` | "adverb" |
| `particle` | "particle" |
| `conjunction` | "conjunction" |
| `interjection` | "interjection" |
| `pronoun` | "pronoun" |
| `counter` | "counter" |
| `prefix` | "prefix" |
| `suffix` | "suffix" |
| `expression` | "expression", "expression (proverb)" |
| `pre-noun-adjectival` | "pre-noun adjectival", "no-adjective" |
| `number` | "number" |

**Compound Types** (entries with multiple functions):
- Use arrays for entries with multiple parts of speech
- Example: noun + suru-verb → `["noun", "verb-suru"]`
- Example: na-adjective + noun → `["adjective-na", "noun"]`

### 1.2 Verb Subtype Tags

For verbs, add additional tags:

| Tag | Values | Description |
|-----|--------|-------------|
| `transitivity` | `transitive`, `intransitive`, `both` | Verb transitivity |
| `verb_class` | `godan`, `ichidan`, `suru`, `kuru`, `irregular` | Conjugation class |

### 1.3 Register/Pragmatic Tags

| Tag Category | Possible Values | Description |
|--------------|-----------------|-------------|
| `formality` | `formal`, `neutral`, `informal`, `vulgar` | Speech register |
| `politeness` | `honorific`, `humble`, `polite`, `plain` | Keigo classification |
| `gender` | `masculine`, `feminine`, `neutral` | Gender association |
| `age` | `children`, `youth`, `adult`, `elderly` | Age-associated usage |
| `style` | `written`, `spoken`, `literary`, `archaic` | Style/medium |
| `domain` | `business`, `academic`, `technical`, `legal`, `medical`, `colloquial` | Usage domain |

### 1.4 Semantic Category Tags

Define a hierarchical taxonomy of semantic categories. Examples:

**Time & Calendar**:
- `time-day-of-week` (月曜日, 火曜日, etc.)
- `time-month` (一月, 二月, etc.)
- `time-season` (春, 夏, etc.)
- `time-period` (朝, 昼, 夜, etc.)
- `time-general` (時間, 今, etc.)

**Nature & Animals**:
- `animal-mammal` (犬, 猫, 象, etc.)
- `animal-bird` (鳥, 鶴, etc.)
- `animal-fish` (魚, 鯛, etc.)
- `animal-insect` (虫, 蝶, etc.)
- `plant-tree` (木, 桜, etc.)
- `plant-flower` (花, 薔薇, etc.)
- `weather` (雨, 雪, etc.)

**Human & Body**:
- `body-part` (手, 足, 頭, etc.)
- `body-internal` (心臓, 肺, etc.)
- `family` (父, 母, 兄, etc.)
- `occupation` (医者, 先生, etc.)

**Abstract**:
- `emotion` (嬉しい, 悲しい, etc.)
- `color` (赤, 青, etc.)
- `number` (一, 二, etc.)
- `direction` (北, 南, etc.)
- `size` (大きい, 小さい, etc.)

**Objects & Places**:
- `food` (ご飯, パン, etc.)
- `clothing` (服, 靴, etc.)
- `building` (家, 学校, etc.)
- `transportation` (車, 電車, etc.)
- `tool` (ペン, 鋏, etc.)

**Actions & States**:
- `movement` (行く, 来る, etc.)
- `communication` (話す, 聞く, etc.)
- `cognition` (思う, 知る, etc.)
- `existence` (ある, いる, etc.)

### 1.5 Deliverables for Phase 1

1. **Create `build/tag_taxonomy.json`**: Complete tag definitions with descriptions
2. **Create `docs/tagging-guide.md`**: Human-readable documentation
3. **Create mapping table**: Current part_of_speech → canonical forms

---

## Phase 2: Schema & Infrastructure Updates

**Goal**: Update the technical infrastructure to support tags.

### 2.1 Update `build/schema.json`

Add new metadata fields:

```json
"metadata": {
  "type": "object",
  "required": ["created", "modified"],
  "properties": {
    "created": { ... },
    "modified": { ... },
    "ai_model": { ... },
    "vocabulary_tier": { ... },
    "tags": {
      "type": "object",
      "description": "Structured tags for search and categorization",
      "properties": {
        "pos": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": ["noun", "verb-godan", "verb-ichidan", "verb-suru", "verb-irregular", "adjective-i", "adjective-na", "adverb", "particle", "conjunction", "interjection", "pronoun", "counter", "prefix", "suffix", "expression", "pre-noun-adjectival", "number"]
          },
          "description": "Part of speech (canonical forms)"
        },
        "transitivity": {
          "type": "string",
          "enum": ["transitive", "intransitive", "both", null],
          "description": "Verb transitivity (verbs only)"
        },
        "formality": {
          "type": "string",
          "enum": ["formal", "neutral", "informal", "vulgar", null],
          "description": "Register/formality level"
        },
        "politeness": {
          "type": "string",
          "enum": ["honorific", "humble", "polite", "plain", null],
          "description": "Keigo classification"
        },
        "style": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": ["written", "spoken", "literary", "archaic", "slang"]
          },
          "description": "Style/medium associations"
        },
        "domain": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Usage domains (business, academic, etc.)"
        },
        "semantic": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Semantic categories"
        }
      }
    }
  }
}
```

### 2.2 Create `build/validate_tags.py`

New script to validate tag consistency:
- Check all tags are from valid taxonomy
- Warn on missing tags (entries without any semantic tags)
- Check transitivity only on verbs
- Check for conflicting tags

### 2.3 Create `build/migrate_pos.py`

Migration script for part_of_speech standardization:
- `--dry-run`: Show proposed changes
- `--apply`: Write changes to files
- Maps old `part_of_speech` strings to canonical `metadata.tags.pos` arrays
- Preserves original `part_of_speech` field for reference during transition

### 2.4 Create `build/tag_statistics.py`

Reporting script:
- Count entries by each tag category
- Identify untagged entries
- Generate coverage reports

### 2.5 Deliverables for Phase 2

1. Updated `build/schema.json`
2. New `build/validate_tags.py`
3. New `build/migrate_pos.py`
4. New `build/tag_statistics.py`

---

## Phase 3: Part of Speech Standardization

**Goal**: Normalize all 7,359 entries to canonical part-of-speech tags.

### 3.1 Create Part of Speech Mapping

Create `build/pos_mapping.json` with explicit mappings:

```json
{
  "noun": ["noun"],
  "noun, suru-verb": ["noun", "verb-suru"],
  "noun / suru-verb": ["noun", "verb-suru"],
  "noun, suru verb": ["noun", "verb-suru"],
  "noun/suru verb": ["noun", "verb-suru"],
  "noun; suru-verb": ["noun", "verb-suru"],
  "noun; suru verb": ["noun", "verb-suru"],
  "noun/suru-verb": ["noun", "verb-suru"],
  "verb (godan)": ["verb-godan"],
  "godan verb": ["verb-godan"],
  "verb (godan, transitive)": ["verb-godan"],
  "verb (godan, intransitive)": ["verb-godan"],
  "godan verb, transitive": ["verb-godan"],
  "verb (ichidan)": ["verb-ichidan"],
  "ichidan verb": ["verb-ichidan"],
  "verb (ichidan, transitive)": ["verb-ichidan"],
  "verb (ichidan, intransitive)": ["verb-ichidan"],
  "i-adjective": ["adjective-i"],
  "adjective (i-adjective)": ["adjective-i"],
  "na-adjective": ["adjective-na"],
  "adjective (na-adjective)": ["adjective-na"],
  "な-adjective": ["adjective-na"],
  "na-adjective, noun": ["adjective-na", "noun"],
  "noun, na-adjective": ["noun", "adjective-na"],
  "adverb": ["adverb"],
  "adverb, na-adjective": ["adverb", "adjective-na"],
  "adverb, suru verb": ["adverb", "verb-suru"],
  "particle": ["particle"],
  "conjunction": ["conjunction"],
  "interjection": ["interjection"],
  "pronoun": ["pronoun"],
  "counter": ["counter"],
  "prefix": ["prefix"],
  "suffix": ["suffix"],
  "expression": ["expression"],
  "expression (proverb)": ["expression"],
  "expression, proverb": ["expression"],
  "pre-noun adjectival": ["pre-noun-adjectival"],
  "no-adjective": ["pre-noun-adjectival"],
  "noun, no-adjective": ["noun", "pre-noun-adjectival"],
  "noun / no-adjective": ["noun", "pre-noun-adjectival"],
  "noun/no-adjective": ["noun", "pre-noun-adjectival"],
  "number": ["number"]
}
```

### 3.2 Extract Transitivity from Current part_of_speech

For verbs, extract transitivity information:
- "verb (godan, transitive)" → transitivity: "transitive"
- "verb (godan, intransitive)" → transitivity: "intransitive"
- "godan verb, transitive" → transitivity: "transitive"

### 3.3 Run Migration

```bash
# Preview changes
python3 build/migrate_pos.py --dry-run

# Apply changes
python3 build/migrate_pos.py --apply

# Verify
python3 build/validate.py
python3 build/tag_statistics.py
```

### 3.4 Handle Unmapped Variants

If `migrate_pos.py` encounters unknown part_of_speech values:
1. Log them for manual review
2. Add mappings to `pos_mapping.json`
3. Re-run migration

### 3.5 Deliverables for Phase 3

1. `build/pos_mapping.json` - Complete mapping table
2. All 7,359 entries updated with `metadata.tags.pos`
3. Verb entries include `metadata.tags.transitivity` where known

---

## Phase 4: Register & Pragmatic Tags

**Goal**: Add formality, politeness, style, and domain tags.

### 4.1 Automated Extraction from Notes

Create `build/extract_register_tags.py`:
- Scan `notes` field for register keywords
- Pattern matching for: "formal", "informal", "polite", "humble", "honorific", "casual", "spoken", "written", "literary", "business", "academic"
- Generate suggested tags with confidence scores

Example patterns:
- "is formal and academic" → formality: "formal", domain: ["academic"]
- "more common in casual speech" → formality: "informal", style: ["spoken"]
- "polite form of" → politeness: "polite"
- "humble form" → politeness: "humble"
- "honorific" → politeness: "honorific"

### 4.2 Manual Review Workflow

1. Run extraction script: `python3 build/extract_register_tags.py --output register_suggestions.json`
2. Review suggestions in batches of 50-100 entries
3. Accept, modify, or reject each suggestion
4. Apply accepted tags

### 4.3 Default Values

For entries without explicit register information:
- `formality`: "neutral" (default for most entries)
- `politeness`: "plain" (default for non-keigo entries)
- `style`: null (no default; only tag if specifically written/spoken/literary)
- `domain`: null (only tag if domain-specific)

### 4.4 Keigo Entries

Special handling for keigo (敬語):
- Identify honorific forms (いらっしゃる, おっしゃる, etc.)
- Identify humble forms (申す, 参る, etc.)
- Tag both the keigo word and link to plain equivalent via cross-references

### 4.5 Deliverables for Phase 4

1. `build/extract_register_tags.py`
2. All entries tagged with appropriate `formality`, `politeness`, `style`, `domain`
3. Updated cross-references for keigo pairs

---

## Phase 5: Semantic Category Tags

**Goal**: Add semantic category tags to all entries.

### 5.1 High-Confidence Automated Tagging

Create `build/auto_semantic_tags.py` for clear-cut cases:

**By cross-reference pattern**:
- Entries cross-referenced as `type: "pair"` → tag as verbs
- Entries cross-referenced as `type: "keigo"` → link to plain form

**By gloss/definition pattern**:
- Gloss contains "Monday/Tuesday/..." → `time-day-of-week`
- Gloss contains "January/February/..." → `time-month`
- Gloss contains color words → `color`
- Definition mentions "animal" → appropriate animal subcategory
- Definition mentions "body part" → `body-part`

**By headword pattern**:
- Entries ending in 曜日 → `time-day-of-week`
- Entries ending in 月 (months) → `time-month`
- Entries with counter suffix → `counter`

### 5.2 Semi-Automated Categorization

Create `build/suggest_semantic_tags.py`:
- Uses definition analysis to suggest categories
- Groups similar entries for batch review
- Outputs to `semantic_suggestions.json`

### 5.3 Manual Categorization Workflow

For entries requiring human judgment:

1. **Generate uncategorized list**: `python3 build/tag_statistics.py --uncategorized`
2. **Process by part of speech**: Start with concrete categories (nouns) before abstract
3. **Batch by similarity**: Group semantically similar entries
4. **Apply tags**: Use edit script or direct entry modification

### 5.4 Multiple Semantic Tags

Many entries belong to multiple categories:
- 朝ご飯 (breakfast) → `food`, `time-period`
- 医者 (doctor) → `occupation`, `medical`
- 泳ぐ (swim) → `movement`, `sport`

Allow arrays of semantic tags and encourage comprehensive tagging.

### 5.5 Deliverables for Phase 5

1. `build/auto_semantic_tags.py`
2. `build/suggest_semantic_tags.py`
3. All 7,359 entries with semantic category tags
4. Complete semantic taxonomy in `build/tag_taxonomy.json`

---

## Phase 6: Verification & Quality Assurance

**Goal**: Ensure completeness, consistency, and accuracy.

### 6.1 Coverage Verification

Run comprehensive coverage report:

```bash
python3 build/tag_statistics.py --full-report
```

Expected output:
- % of entries with pos tags: 100%
- % of entries with semantic tags: >95%
- % of verbs with transitivity: >90%
- % of entries with formality: 100%
- Distribution by category

### 6.2 Consistency Checks

Create `build/check_tag_consistency.py`:
- Verbs must have verb-related pos tags
- Transitivity only on verbs
- Keigo entries should have politeness tags
- Domain-specific entries should have domain tags
- Cross-check semantic tags with definitions

### 6.3 Random Sampling Audit

Manual audit of random samples:
1. Select 100 random entries
2. Verify all tags are accurate
3. Identify systematic errors
4. Correct and re-run validation

### 6.4 Deliverables for Phase 6

1. `build/check_tag_consistency.py`
2. Coverage report showing >95% tagging
3. Audit documentation

---

## Phase 7: Integration & Documentation

**Goal**: Integrate tags into workflow and document system.

### 7.1 Update Entry Creation Skills

Update `.claude/skills/` to require tags on new entries:

**entry-guidelines/SKILL.md**:
- Add tags section to required fields
- Document tag selection process
- Provide examples

**verb-entry/SKILL.md**:
- Require transitivity tag
- Document verb-specific tags

**adjective-entry/SKILL.md**:
- Document adjective-i vs adjective-na tagging

**other-entries/SKILL.md**:
- Document semantic category selection
- Domain-specific tagging guidelines

### 7.2 Update Validation

Update `build/validate.py`:
- Check for presence of metadata.tags
- Validate tags against taxonomy
- Warn on missing recommended tags

### 7.3 Update Index Generation

Update `build/update_entries_index.py`:
- Include tags in index for search
- Generate tag-based statistics

### 7.4 Search & Export Integration

Update `build/build_flat.py`:
- Add tag-based filtering UI
- Generate tag index page
- Enable export by tag selection

### 7.5 Documentation

Create comprehensive documentation:
- `docs/tagging-system.md`: System overview
- `docs/tag-taxonomy.md`: Complete tag reference
- `docs/tagging-workflow.md`: How to tag entries

### 7.6 Deliverables for Phase 7

1. Updated skill files in `.claude/skills/`
2. Updated build scripts
3. Documentation in `docs/`
4. Functional tag-based search/export

---

## Implementation Schedule

### Recommended Order

1. **Phase 1** (Tag Taxonomy Design): Do this first to establish vocabulary
2. **Phase 2** (Infrastructure): Build tools before migration
3. **Phase 3** (POS Standardization): Most mechanical, good starting point
4. **Phase 4** (Register Tags): Requires notes analysis
5. **Phase 5** (Semantic Tags): Most labor-intensive
6. **Phase 6** (Verification): Quality assurance
7. **Phase 7** (Integration): Final integration

### Session Workflow

For each working session:

1. **Start**: Read PROJECT_STATUS.md for context
2. **Choose phase/task**: Based on current progress
3. **Execute**: Follow phase-specific instructions
4. **Validate**: Run validation scripts after changes
5. **Document**: Update PROJECT_STATUS.md
6. **Commit**: Commit changes with clear messages

### Batch Processing Guidelines

When processing entries in batches:
- Process 50-100 entries per session
- Run validation after each batch
- Commit frequently (every 50 entries)
- Track progress in PROJECT_STATUS.md

---

## Success Criteria

The tagging system is complete when:

1. **Schema**: `build/schema.json` includes complete tag definitions
2. **Taxonomy**: `build/tag_taxonomy.json` documents all valid tags
3. **Coverage**: All 7,359 entries have:
   - `metadata.tags.pos` (100%)
   - `metadata.tags.formality` (100%, even if "neutral")
   - `metadata.tags.semantic` (>95%)
   - `metadata.tags.transitivity` (all verbs)
4. **Validation**: `python3 build/validate.py` passes with no tag errors
5. **Skills**: All entry creation skills require appropriate tags
6. **Documentation**: Complete docs in `docs/` directory
7. **Search**: Tag-based search functional in built site

---

## Notes

### Backward Compatibility

- Keep original `part_of_speech` field during transition
- Add tags to `metadata.tags` (new field)
- Eventually deprecate `part_of_speech` in favor of `metadata.tags.pos`

### Performance Considerations

- Tag arrays should be small (typically 1-5 items)
- Index tags for search performance
- Consider tag inheritance for compounds
