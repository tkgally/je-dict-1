# Vocabulary Tier Realignment Plan

This prompt provides a comprehensive plan for realigning all dictionary entries to the vocabulary tier guidelines in `.claude/skills/vocabulary-tiers/SKILL.md`.

## Current State Analysis

As of this analysis:
- **Basic tier**: 1,120 entries (target: 600-800) — **320-520 over limit**
- **Core tier**: 5,296 entries (target: 1,600-2,000) — **3,296-3,696 over limit**
- **General tier**: 743 entries (no limit)
- **Unassigned**: 200 entries (target: 0)

The dictionary is severely misaligned with the tier guidelines. Most entries currently in "core" need to be reassigned to "general".

---

## Execution Strategy

This realignment is too large for a single session. Execute in phases across multiple sessions.

### Phase 1: Semantic Group Inventory (Session 1)

**Objective**: Create a comprehensive inventory of all semantic groups and their current tier assignments.

**Steps**:

1. **Create analysis infrastructure**:
   ```bash
   mkdir -p build/tier_analysis
   ```

2. **Generate master entry list with tiers**:
   ```bash
   python3 -c "
   import json
   import glob

   entries = []
   for f in glob.glob('entries/**/*.json', recursive=True):
       with open(f) as fp:
           e = json.load(fp)
           entries.append({
               'id': e['id'],
               'headword': e['headword'],
               'reading': e['reading'],
               'pos': e['part_of_speech'],
               'gloss': e['gloss'],
               'tier': e.get('metadata', {}).get('vocabulary_tier'),
               'path': f
           })

   with open('build/tier_analysis/all_entries.json', 'w') as fp:
       json.dump(sorted(entries, key=lambda x: x['reading']), fp, ensure_ascii=False, indent=2)
   print(f'Exported {len(entries)} entries')
   "
   ```

3. **Identify and document all semantic groups** by searching for:
   - Days of week (月曜日-日曜日)
   - Months (一月-十二月)
   - Numbers 1-10, 11-100 by tens
   - Ordinals (一番, 二番, etc.)
   - Counters (つ series, 人, 個, 本, 枚, etc.)
   - Directions (上, 下, 右, 左, 前, 後ろ, 中, 外)
   - Cardinal directions (北, 南, 東, 西)
   - Body parts (頭, 顔, 目, 耳, 口, 鼻, 手, 足, etc.)
   - Family terms (父, 母, 兄, 姉, 弟, 妹, etc.)
   - Colors (赤, 青, 白, 黒, 黄色, 緑, etc.)
   - Question words (何, 誰, どこ, いつ, なぜ, どう, どれ, etc.)
   - Demonstratives (こ/そ/あ/ど series - これ, それ, あれ, どれ, etc.)
   - Pronouns (私, 僕, 俺, あなた, 彼, 彼女, etc.)
   - Seasons (春, 夏, 秋, 冬)
   - Basic existence verbs (いる, ある)
   - Basic movement verbs (行く, 来る, 帰る, 歩く, 走る)
   - Basic daily verbs (食べる, 飲む, 寝る, 起きる)
   - Basic communication verbs (言う, 話す, 聞く, 読む, 書く)
   - Time periods (朝, 昼, 夕方, 夜, 夜中)
   - Relative time (今日, 明日, 昨日, 今週, etc.)

4. **Create semantic group registry**:
   ```bash
   # Create file: build/tier_analysis/semantic_groups.json
   ```

   Format:
   ```json
   {
     "days_of_week": {
       "target_tier": "basic",
       "entries": ["げつようび", "かようび", "すいようび", ...],
       "current_tiers": {"basic": 7},
       "status": "self-contained"
     },
     ...
   }
   ```

5. **Output**: A complete map of semantic groups, their members, and current tier distribution.

---

### Phase 2: Basic Tier Curation (Sessions 2-3)

**Objective**: Reduce basic tier from ~1,120 to 600-800 entries.

**Guiding Principles for Basic Tier**:
- Words needed from the very first days of study
- High-frequency function words (particles, pronouns, basic conjunctions)
- Essential verbs for daily actions
- Core adjectives for basic description
- Numbers, time expressions, basic counters
- Fundamental nouns (person, thing, place, time)
- Basic question words

**Steps**:

1. **List all current basic tier entries**:
   ```bash
   python3 -c "
   import json
   with open('build/tier_analysis/all_entries.json') as f:
       entries = json.load(f)
   basic = [e for e in entries if e['tier'] == 'basic']
   print(f'Basic tier entries: {len(basic)}')
   for e in basic:
       print(f\"{e['reading']}: {e['gloss']} ({e['pos']})\")
   " > build/tier_analysis/basic_tier_current.txt
   ```

2. **Categorize basic entries into KEEP vs DEMOTE**:

   **KEEP in basic** (must be ≤800 total):
   - All particles (は, が, を, に, で, と, も, の, etc.)
   - Core pronouns (私, あなた, demonstratives)
   - Numbers 1-10
   - Days of week (if including, include all 7)
   - Months (if including, include all 12)
   - Seasons (4)
   - Basic question words (何, 誰, どこ, いつ, なぜ, どう)
   - Basic colors (5 core: 赤, 青, 白, 黒, 黄色)
   - Basic body parts (~10)
   - Basic family terms (~10)
   - Essential verbs (~50): existence, movement, communication, daily actions
   - Essential adjectives (~30): いい, 悪い, 大きい, 小さい, 新しい, 古い, etc.
   - Essential nouns (~200): 人, 物, 事, 所, 時, 日, etc.
   - Essential adverbs (~30): とても, もう, まだ, いつも, etc.
   - Basic counters (~20): つ series, 人, 個, 本, 枚, etc.

   **DEMOTE to core or general**:
   - Words that are useful but not survival-essential
   - Extended vocabulary beyond the fundamental sets
   - Words that intermediate learners can reasonably delay

3. **Execute tier changes for demoted entries**:
   For each entry being demoted:
   ```bash
   # Update metadata.vocabulary_tier from "basic" to "core" or "general"
   ```

4. **Verify semantic group integrity** after changes:
   - No partial groups split across tiers
   - Apply exclusion corollary if groups don't fit

5. **Target output**: Basic tier with 600-800 entries, all semantic groups intact.

---

### Phase 3: Core Tier Curation (Sessions 4-10)

**Objective**: Reduce core tier from ~5,500+ to 1,600-2,000 entries.

This is the largest task. After Phase 2 adds demoted basic entries, core will have ~5,600-5,800 entries. Need to move ~3,600-4,000 entries to general.

**Guiding Principles for Core Tier**:
- Words needed for general adult communication
- Would be known by any educated Japanese speaker
- Appears regularly in newspapers, general media
- Used in typical workplace or social situations
- Expansions of basic vocabulary (more specific verbs, more nuanced adjectives)

**NOT Core Tier** (should be general):
- Specialized or technical vocabulary
- Domain-specific terminology (law, medicine, science, etc.)
- Literary or archaic expressions
- Low-frequency words
- Formal alternatives to common words
- Words most adults wouldn't use daily

**Batch Processing Strategy**:

Process entries in batches by part of speech:

| POS Category | Current Core | Target Core | Sessions |
|--------------|--------------|-------------|----------|
| Nouns | ~2,635 | ~800-1,000 | 2-3 |
| Verbs (all types) | ~900 | ~300-400 | 1-2 |
| Adverbs | ~267 | ~80-100 | 1 |
| Adjectives | ~250 | ~100-150 | 1 |
| Other (expressions, etc.) | ~250 | ~150-200 | 1 |

**For each batch**:

1. **Extract entries**:
   ```bash
   python3 -c "
   import json
   with open('build/tier_analysis/all_entries.json') as f:
       entries = json.load(f)
   # Filter by POS and current tier
   batch = [e for e in entries if e['tier'] == 'core' and 'noun' in e['pos'].lower()]
   for e in batch:
       print(f\"{e['id']}: {e['reading']} - {e['gloss']}\")
   "
   ```

2. **Categorize each entry**:
   - **KEEP in core**: Essential for adult communication
   - **DEMOTE to general**: Specialized, technical, low-frequency

3. **Execute tier changes**:
   For each entry being demoted, update `metadata.vocabulary_tier` to `"general"`.

4. **Track counts** after each batch:
   ```bash
   python3 -c "
   import json, glob
   tiers = {'basic': 0, 'core': 0, 'general': 0, 'null': 0}
   for f in glob.glob('entries/**/*.json', recursive=True):
       with open(f) as fp:
           t = json.load(fp).get('metadata', {}).get('vocabulary_tier') or 'null'
           tiers[t] = tiers.get(t, 0) + 1
   print(tiers)
   "
   ```

---

### Phase 4: Assign Unassigned Entries (Session 11)

**Objective**: Assign all ~200 entries with `vocabulary_tier: null`.

**Steps**:

1. **List all unassigned entries**:
   ```bash
   python3 -c "
   import json
   with open('build/tier_analysis/all_entries.json') as f:
       entries = json.load(f)
   unassigned = [e for e in entries if e['tier'] is None]
   for e in unassigned:
       print(f\"{e['id']}: {e['reading']} - {e['gloss']} ({e['pos']})\")
   "
   ```

2. **For each entry**, apply tier decision criteria:
   - Basic: Needed immediately, high-frequency, fundamental
   - Core: General adult communication, common
   - General: Specialized, technical, low-frequency

3. **Check semantic group membership**:
   - If the word belongs to an existing group, use that group's tier
   - If it's standalone, apply individual criteria

4. **Execute tier assignments**.

---

### Phase 5: Validation and Finalization (Session 12)

**Objective**: Verify the realignment is complete and consistent.

**Steps**:

1. **Verify tier counts**:
   ```bash
   python3 -c "
   import json, glob
   tiers = {'basic': 0, 'core': 0, 'general': 0, 'null': 0}
   for f in glob.glob('entries/**/*.json', recursive=True):
       with open(f) as fp:
           t = json.load(fp).get('metadata', {}).get('vocabulary_tier') or 'null'
           tiers[t] = tiers.get(t, 0) + 1
   print('Tier counts:')
   print(f\"  Basic: {tiers['basic']} (target: 600-800)\")
   print(f\"  Core: {tiers['core']} (target: 1600-2000)\")
   print(f\"  General: {tiers['general']} (no limit)\")
   print(f\"  Unassigned: {tiers['null']} (target: 0)\")
   "
   ```

2. **Verify semantic group integrity**:
   - Re-run semantic group analysis from Phase 1
   - Ensure all groups are self-contained

3. **Run full validation**:
   ```bash
   python3 build/validate.py
   python3 build/update_indexes.py
   python3 build/build_flat.py
   ```

4. **Update PROJECT_STATUS.md** with final tier counts.

5. **Commit and document** the realignment.

---

## Session Execution Guide

### Starting a Session

1. Read this prompt and note which phase/batch you're working on
2. Run current tier counts to verify starting state
3. If Phase 1 is complete, read `build/tier_analysis/semantic_groups.json`

### During a Session

1. Process entries in manageable chunks (50-100 at a time)
2. For each tier change:
   - Read the entry file
   - Update `metadata.vocabulary_tier`
   - Update `metadata.modified` timestamp using `python3 build/get_timestamp.py`
   - Write the updated entry
3. Track progress and counts

### Ending a Session

1. Run validation: `python3 build/validate.py`
2. Run tier count check
3. Commit changes with message describing what was done
4. Note progress for next session

---

## Tier Decision Quick Reference

### Basic (600-800 words)
✓ Particles, pronouns, demonstratives
✓ Numbers 1-10, basic counters (つ, 人, 個, 本, 枚)
✓ Days, months, seasons, basic time words
✓ Basic question words
✓ Existence verbs (いる, ある), movement verbs (行く, 来る)
✓ Daily action verbs (食べる, 飲む, 寝る, 見る)
✓ Communication verbs (言う, 話す, 聞く, 読む, 書く)
✓ Core adjectives (いい, 悪い, 大きい, 小さい, 新しい)
✓ Fundamental nouns (人, 物, 事, 所, 時, 日, 年, 名前)
✓ Basic family, body parts, colors, directions

### Core (1,600-2,000 words)
✓ General adult vocabulary
✓ Workplace and social situation words
✓ Common but not survival-essential words
✓ Extended verb vocabulary
✓ Nuanced adjectives
✓ Standard counters beyond basics
✓ Abstract concepts for opinions/emotions

### General (unlimited)
✓ Specialized/technical vocabulary
✓ Domain-specific (law, medicine, science, business jargon)
✓ Literary/archaic expressions
✓ Low-frequency words
✓ Formal alternatives to common words
✓ Words requiring specific domain knowledge

---

## Important Reminders

1. **Self-containment is critical**: Never split a semantic group across tiers
2. **When in doubt, demote to general**: Better to have a well-curated core than an inflated one
3. **Track your counts**: Run tier counts frequently during execution
4. **Timestamp updates**: Always update `metadata.modified` when changing an entry
5. **Validate after each session**: Run `validate.py` before committing
