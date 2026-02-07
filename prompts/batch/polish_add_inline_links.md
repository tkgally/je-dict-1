# Add Inline Word Links — Batch Mode

Add cross-reference links to example sentences and notes, allowing users to click any word to navigate to its dictionary entry. This is a **semantic task** that requires knowledge of Japanese.

**This prompt is optimized for non-interactive (`claude --print`) execution.**

## Parameters

- `batch_size`: Number of entries to process (default: 15)
- `tier`: Vocabulary tier to focus on (optional)

## Task Focus

**Single focus**: Add inline word links to example sentences and notes.

For each entry:
1. Read each example sentence and note carefully
2. Identify each word and its grammatical function
3. Look up or verify the correct entry ID for each word
4. Add link markup, ensuring semantic correctness
5. Save the updated entry

Load the skill file for detailed requirements:
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

- Read the full sentence to understand context
- Confirm each word's meaning matches the target entry
- Verify correct word boundaries
- Do NOT blindly match by reading alone

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

6. **After processing all entries in the batch**:
   - Update `polishing/tasks/inline-links/progress.txt`
   - Validate and build:
     ```bash
     make validate
     python3 build/update_indexes.py
     python3 build/build_flat.py --quick
     ```

7. **Commit** (do NOT push — the pipeline handles pushing):
   ```bash
   git add entries/ polishing/
   git commit -m "Inline links: add links to entries XXXXX-XXXXX"
   git add docs/
   git commit -m "Rebuild site with inline link updates"
   ```

8. **Exit cleanly**: After committing, stop. Do not start additional work.

## Looking Up Entry IDs

### Word-ID Lookup Table

A pre-built lookup table is available at `build/word_id_lookup.json`. Load it at the start of your session to resolve words to entry IDs without running per-word searches:

```bash
# Look up a word by reading
python3 -c "
import json
with open('build/word_id_lookup.json') as f:
    data = json.load(f)
reading = 'きく'
for e in data['by_reading'].get(reading, []):
    print(f\"{e['id']}: {e['headword']} - {e['gloss']}\")
"
```

The table has two indexes:
- `by_reading` — maps hiragana readings to entries (use for most lookups)
- `by_headword` — maps kanji/surface forms to entries (use when you know the written form)

Each entry includes `id`, `headword`/`reading`, `gloss`, and `tier` for disambiguation.

### Common Words Quick Reference

**Particles:**
- が: 00051_ga, は: 00079_ha, を: 00422_wo, に: 00314_ni
- で: 00502_de, の: 09472_no, と: 00512_to, も: 00484_mo
- から: 00504_kara, まで: 00490_made, か: 09473_ka
- ね: 09474_ne, よ: 09475_yo

**Common Verbs:**
- する: 00392_suru, ある: 00006_aru, いる: 00495_iru
- 行く: 00119_iku, 来る: 00254_kuru, 見る: 00283_miru
- 食べる: 00396_taberu

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
