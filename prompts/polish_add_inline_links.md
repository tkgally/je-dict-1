# Add Inline Word Links

Add cross-reference links to example sentences and notes, allowing users to click any word to navigate to its dictionary entry. This is a **semantic task** that requires your knowledge of Japanese - it cannot be automated.

## Task Focus

**Single focus**: Add inline word links to example sentences and notes.

For each entry, you will:
1. Read each example sentence and note carefully
2. Identify each word and its grammatical function
3. Look up or verify the correct entry ID for each word
4. Add link markup, ensuring semantic correctness
5. Save the updated entry

Load the skill file for detailed requirements and the common words reference table:
```
.claude/skills/inline-word-links/SKILL.md
```

## Starting Point

```bash
cat polishing/tasks/inline-links/progress.txt
```

Find the first entry file that starts with that number.

## Link Format

```
⟦{surface|reading}→baseform：entry_id⟧
```

**Example:**
```
⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧⟦{読|よ}む→読む：00426_yomu⟧。
```

## CRITICAL: Semantic Verification

**Every link MUST be verified semantically.**

This means:
- Reading the full sentence to understand context
- Confirming each word's meaning matches the target entry
- Verifying correct word boundaries
- NOT blindly matching by reading alone

### Common Mistakes to Avoid

| Mistake | Example | Correct Approach |
|---------|---------|------------------|
| Wrong homograph | の → 野 (field) | の is usually the particle (09472_no), not 野 (03535_no) |
| Wrong word | ある as noun | Verify: is this the verb ある (00006_aru) or a different word? |
| Bad boundaries | もの + です | Consider if ものです is a grammatical pattern |

## Workflow

1. **Read the progress file** to find the next entry

2. **Load and examine the entry**:
   - Read each example sentence fully
   - Read the notes section if present

3. **For each example sentence**:
   a. Identify every word (content words and particles)
   b. For each word:
      - Determine its meaning in this context
      - Look up the entry ID (use skill reference table or search)
      - Verify the gloss matches the intended meaning
   c. Add link markup to the japanese field
   d. Do NOT link the entry's own headword (no self-reference)
   e. Do NOT link punctuation

4. **For notes with Japanese text**:
   - Apply the same process to Japanese phrases in notes
   - Skip section headers and non-sentence text

5. **Update timestamp and save**:
   ```bash
   python3 build/get_timestamp.py
   ```
   Use this timestamp for the `modified` field.

6. **After every 30 entries** (or when you make changes):
   - Update `polishing/tasks/inline-links/progress.txt`
   - Run validation:
     ```bash
     python3 build/validate.py
     python3 build/update_indexes.py
     python3 build/build_flat.py
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Inline links: add links to entries XXXXX-XXXXX"
     ```

7. **Check remaining context** using `/context`:
   - **30% or more**: Continue to next batch
   - **Less than 30%**: Perform context reset (step 8)

8. **Context Reset Procedure**:
   a. Update `polishing/tasks/inline-links/progress.txt`
   b. Write session log to `polishing/sessions/inline-links_{date}_{nnn}.md`:
      ```
      ## Session: Inline Links
      Date: YYYY-MM-DD
      Entries processed: XXXXX-XXXXX

      ### Entries Modified
      - [entry_id]: [number of examples linked]

      ### Notes
      - Any unusual cases or decisions made

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes
   d. Use `/compact` to reset context
   e. Re-read this prompt and continue from step 1

## Looking Up Entry IDs

### For Common Words
Use the reference table in the skill file. Key entries:

**Particles:**
- が: 00051_ga
- は: 00079_ha
- を: 00422_wo
- に: 00314_ni
- で: 00502_de
- の: 09472_no (possessive particle, NOT 野)
- と: 00512_to
- も: 00484_mo
- から: 00504_kara
- まで: 00490_made
- か: 09473_ka
- ね: 09474_ne
- よ: 09475_yo

**Common Verbs:**
- する: 00392_suru
- ある: 00006_aru
- いる: 00495_iru
- 行く: 00119_iku
- 来る: 00254_kuru
- 見る: 00283_miru
- 食べる: 00396_taberu

### For Other Words
Search the dictionary:
```bash
python3 -c "
import json
from pathlib import Path
for f in Path('entries').glob('**/*.json'):
    with open(f) as fp:
        e = json.load(fp)
        if e['reading'] == 'TARGET_READING':
            print(f\"{e['id']}: {e['headword']} - {e['gloss'][:50]}\")
"
```

Replace `TARGET_READING` with the hiragana reading.

## Example Transformation

**Before:**
```json
"japanese": "{私|わたし}は{日本語|にほんご}を{勉強|べんきょう}しています。"
```

**After:**
```json
"japanese": "⟦{私|わたし}→私：00651_watashi⟧⟦は→は：00079_ha⟧⟦{日本語|にほんご}→日本語：00614_nihongo⟧⟦を→を：00422_wo⟧⟦{勉強|べんきょう}しています→勉強する：00527_benkyousuru⟧。"
```

Note:
- Punctuation (。) is NOT linked
- Conjugated form (しています) links to dictionary form (勉強する)
- Each word verified semantically

## Using `noentry`

For words not in the dictionary:
```
⟦{矍鑠|かくしゃく}→矍鑠：noentry⟧
```

## Quality Checklist

Before saving each entry:
- [ ] All words semantically verified
- [ ] No self-references (headword not linked in own examples)
- [ ] Punctuation not linked
- [ ] Conjugations link to dictionary forms
- [ ] Entry IDs are valid
- [ ] Furigana preserved within links

## Progress Update Format

Keep the progress file minimal:
```
next: XXXXX
```

## Output at Session End

When stopping, report:
1. Entry range processed
2. Number of entries modified
3. Any unusual cases encountered
4. Next entry to continue from
