# Polish Semantic Labels

Check dictionary entries one by one for **correct semantic labels**. This is a **semantic task** that requires your knowledge of Japanese vocabulary - it cannot be automated because determining the correct semantic category requires understanding what a word actually means and how it's used.

## Task Focus

**Single focus**: Do the semantic tags in `metadata.tags.semantic` accurately reflect the word's meaning?

For each entry, verify:
- Tags match the word's actual semantic category
- No template artifacts (wrong default tags)
- Appropriate specificity (not too broad, not too narrow)
- Consistency with similar words

## Starting Point

```bash
cat polishing/tasks/semantic-labels/progress.txt
```

Find the first entry file that starts with that number.

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Load the entry** and examine `metadata.tags.semantic`

3. **For each entry**:
   - Read the headword, definitions, and examples to understand the word's meaning
   - Verify the semantic tags match this meaning
   - If tags are wrong: Fix them, update `modified` timestamp, save

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

4. **After every ~50 entries** (or when you make changes):
   - Update `polishing/tasks/semantic-labels/progress.txt`
   - Validate and build:
     ```bash
     python3 build/validate_tags.py
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Semantic labels: check entries XXXXX-XXXXX"
     ```

5. **When finishing** (end of session or context getting long):
   a. Update `polishing/tasks/semantic-labels/progress.txt`
   b. Write session log to `polishing/sessions/semantic-labels_{date}_{nnn}.md`:
      ```
      ## Session: Semantic Labels
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX

      ### Corrections Made
      - [entry_id]: changed [old tags] → [new tags]

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes

## Valid Semantic Tags

### Time
- `time-day-of-week` - Days (Monday, Tuesday...)
- `time-month` - Months (January, February...)
- `time-season` - Seasons (spring, summer...)
- `time-period` - Parts of day (morning, night...)
- `time-general` - Time concepts (now, later, time)

### Nature
- `animal-mammal`, `animal-bird`, `animal-fish`, `animal-insect`, `animal-general`
- `plant-tree`, `plant-flower`, `plant-general`
- `weather` - Rain, snow, wind...
- `geography` - Mountains, rivers, sea...

### Human
- `body-part` - External parts (hand, foot, head...)
- `body-internal` - Internal (heart, lung, bone...)
- `family` - Family terms (father, mother...)
- `occupation` - Jobs (doctor, teacher...)
- `person` - Person terms (man, woman, child...)

### Abstract
- `emotion` - Feelings (happy, sad, angry...)
- `color` - Colors
- `number` - Numbers and counting
- `direction` - North, south, up, down...
- `size` - Big, small, long...
- `quantity` - Many, few, all...

### Objects
- `food` - Food and drinks
- `clothing` - Clothes and accessories
- `building` - Buildings and structures
- `transportation` - Vehicles
- `tool` - Tools and implements
- `furniture` - Furniture and home items
- `electronics` - Electronic devices

### Actions (primarily for verbs)
- `movement` - Physical movement (go, walk, run...)
- `communication` - Speaking, listening, writing...
- `cognition` - Thinking, knowing, remembering...
- `existence` - Being, existing, becoming...
- `creation` - Making, building, drawing...
- `consumption` - Eating, drinking, using...

### Social
- `greeting` - Greetings and social phrases
- `education` - School, study, teacher...
- `work` - Job, company, work...
- `leisure` - Play, movies, travel...

### Linguistic (fallback categories)
- `general` - Nouns without specific category
- `action` - Verbs not fitting other action categories
- `descriptive` - Adjectives and adverbs
- `grammatical` - Particles, conjunctions, prefixes, suffixes
- `expression` - Fixed expressions, interjections
- `onomatopoeia` - Mimetic words

### Special
- `proverb` - Proverbs
- `idiom` - Idiomatic expressions

## Common Error Patterns

### 1. Template Artifacts (Most Common)

Words incorrectly tagged with default categories that don't match their meaning:

**Examples of wrong tags:**
- A verb about emotions tagged `["building"]`
- An abstract noun tagged `["transportation"]`
- A cooking verb tagged `["electronics"]`

**Fix:** Replace with correct category based on actual meaning.

### 2. Verbs with Object Tags

Verbs should use **action categories**, not object categories:

| Wrong | Correct |
|-------|---------|
| `["food"]` for "to eat" | `["consumption"]` |
| `["building"]` for "to build" | `["creation"]` |
| `["body-part"]` for "to choke" | `["action"]` or specific action type |

### 3. Inconsistent Specificity

- Using `general` when a specific category applies
- Using overly specific categories for general words

### 4. Multiple Unrelated Tags

Watch for entries with unrelated tag combinations that suggest template errors:
- `["body-part", "geography"]` - unlikely to both apply
- `["tool", "emotion"]` - usually wrong

### 5. Missing Tags

Some entries may have empty `semantic` arrays. Add appropriate tags.

## Guidelines by Part of Speech

| Part of Speech | Primary Tags |
|----------------|--------------|
| **Nouns** | Specific category (food, tool, etc.) or `general` |
| **Verbs** | Action categories (movement, communication, etc.) or `action` |
| **Adjectives** | `descriptive`, or specific if applicable (color, size, emotion) |
| **Adverbs** | `descriptive` |
| **Particles** | `grammatical` |
| **Conjunctions** | `grammatical` |
| **Prefixes/Suffixes** | `grammatical` |
| **Expressions** | `expression` |
| **Interjections** | `expression` |
| **Onomatopoeia** | `onomatopoeia` |
| **Counters** | `number` or specific category |

## Why This Cannot Be Automated

Correct semantic labeling requires understanding:
- **Word meaning**: What does this word actually refer to?
- **Context of use**: How is the word typically used?
- **Semantic boundaries**: Is "knife" a `tool` or `food` related? (It's `tool`)
- **Primary vs secondary meanings**: Which meaning should drive the tag?
- **Cultural context**: Some words have culturally-specific categorizations

Only a knowledgeable reader can determine the appropriate semantic category.

## Verification Process

For each entry:
1. Read the headword and gloss
2. Check if semantic tags match the primary meaning
3. Look at examples to confirm understanding
4. Verify no template artifacts
5. Check consistency with similar words you've reviewed

## Progress Update Format

Keep the progress file minimal:
```
next: XXXXX
```

## Output at Session End

When stopping (user request or context reset), report:
1. Entry range checked
2. Number of entries corrected
3. Common patterns found
4. Next entry to continue from
