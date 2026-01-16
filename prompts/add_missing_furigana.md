# Add Missing Furigana to Dictionary Entries

This prompt guides you through systematically adding furigana to dictionary entries that have kanji without annotation in any text field (notes, examples, definitions, and explanations).

## Important: Furigana Assignment Requires Semantic Understanding

**Assigning furigana to kanji cannot be done entirely programmatically.**

Many kanji have multiple possible readings depending on context:
- 上 can be read as うえ, かみ, あ(がる), のぼ(る), じょう, etc.
- 生 can be read as せい, しょう, い(きる), う(まれる), なま, etc.
- 行 can be read as い(く), ゆ(く), こう, ぎょう, おこな(う), etc.

You must use your understanding of:
1. **The phrase's meaning** - What does this idiom/collocation mean?
2. **The headword's meaning** - How does this entry's word relate?
3. **Common readings** - What reading is most natural in this context?
4. **Compound word conventions** - How are jukugo typically read?

## Workflow

### 1. Load a Batch of Entries

Read `entries_without_furigana.json` to get the list of entries needing attention.

```bash
# View the first 10 entries
python3 -c "import json; data=json.load(open('entries_without_furigana.json')); [print(f\"{e['id']}: {e['unannotated_kanji']}\") for e in data['entries'][:10]]"
```

Work in batches of 10-20 entries per session to maintain focus and accuracy.

### 2. For Each Entry

1. **Read the full entry** to understand context:
   ```
   Read /home/user/je-dict-1/entries/{file_path}
   ```

2. **Identify unannotated kanji** in all text fields (notes, definitions, examples, explanation)

3. **Determine correct readings** based on:
   - The meaning of the phrase/collocation
   - Standard readings for that compound or idiom
   - Consistency with how the headword is used

4. **Edit the entry** using the Edit tool:
   - Add furigana notation `{kanji|reading}` to all unannotated kanji
   - For compound words, use compound readings: `{安堵|あんど}` not `{安|あん}{堵|ど}`
   - For single kanji with okurigana, annotate the kanji part: `{広|ひろ}げる`

### 3. Verify the Batch

After editing a batch, verify that all furigana has been added:

```bash
# Verify specific entries
python3 build/verify_furigana.py entry_id1 entry_id2 entry_id3

# Or verify a list of entries
echo "entry_id1
entry_id2
entry_id3" | python3 build/verify_furigana.py
```

All entries should show "✓ OK" before proceeding.

### 4. Update entries_without_furigana.json

After verifying a batch is complete, remove those entries from the tracking file:

```python
# Example: Remove processed entries
import json

with open('entries_without_furigana.json', 'r') as f:
    data = json.load(f)

# List of entry IDs that have been fixed
fixed_ids = ['noren_05893', 'ando_05901', 'furoshiki_05891']

# Remove fixed entries
data['entries'] = [e for e in data['entries'] if e['id'] not in fixed_ids]
data['total_count'] = len(data['entries'])

with open('entries_without_furigana.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

### 5. Run Validation and Commit

After completing a batch:

```bash
# Validate all entries
python3 build/validate.py

# Commit changes
git add entries/
git commit -m "Add missing furigana to notes field (batch N)"
```

## Examples of Correct Furigana Addition

### Example 1: Idiom in notes

**Before:**
```
IDIOM:
- 暖簾に腕押し: wasted effort
```

**After:**
```
IDIOM:
- {暖簾|のれん}に{腕押|うでお}し: wasted effort
```

### Example 2: Collocations

**Before:**
```
COMMON COLLOCATIONS:
- 安堵の息をつく: sigh with relief
- 安堵の表情: relieved expression
- 安堵感: feeling of relief
```

**After:**
```
COMMON COLLOCATIONS:
- {安堵|あんど}の{息|いき}をつく: sigh with relief
- {安堵|あんど}の{表情|ひょうじょう}: relieved expression
- {安堵感|あんどかん}: feeling of relief
```

### Example 3: Kanji form note

**Before:**
```
KANJI: Sometimes written as 家鴨 (domestic duck).
```

**After:**
```
KANJI: Sometimes written as {家鴨|あひる} (domestic duck).
```

## Session Progress Tracking

At the end of each session:
1. Note how many entries were fixed
2. Update `entries_without_furigana.json` to remove fixed entries
3. Commit with a descriptive message

## Remaining Entries Count

Check remaining entries:
```bash
python3 -c "import json; data=json.load(open('entries_without_furigana.json')); print(f'Remaining: {data[\"total_count\"]} entries')"
```

The goal is to reduce this to 0 across multiple sessions.
