# New Candidate Words Prompt

Add 100 new candidates to candidate_words.json using the find-candidates skill.

## Quick Context

- Check current state: `head -10 candidate_words.json` (shows total_candidates and next_id)
- Check entry count: `head -5 entries_index.json` (shows total_entries in metadata)

## Workflow

1. Load the find-candidates skill for detailed guidelines
2. Choose search strategies appropriate for the dictionary's current size (see below)
3. Add candidates using: `python3 build/manage_candidates.py add "漢字" "ひらがな" "brief English note"`

4. After adding all candidates, update PROJECT_STATUS.md:
   - Update "Candidate words" count in Content Status section
   - Add a brief session note under Recent Changes

5. Finally, build the website:
   ```bash
   python3 build/build_flat.py        # REQUIRED for live site update
   ```

## Duplicate Prevention (AUTOMATIC)

**The `manage_candidates.py add` command now AUTOMATICALLY checks for duplicates.**

When you run:
```bash
python3 build/manage_candidates.py add "食べる" "たべる" "to eat"
```

The script will:
1. Check `entries_index.json` for matching reading or headword
2. Check `candidate_words.json` for matching reading or word
3. **REFUSE to add the word if any match is found**
4. Display the existing match so you know why it was rejected

### Example of Automatic Rejection
```
$ python3 build/manage_candidates.py add "食べる" "たべる" "to eat"
ERROR: Duplicate detected!
  Exact match in dictionary: taberu_00001 (食べる / たべる)

This word already exists. NOT adding to candidates.
```

### Pre-Check Command (Optional)
If you want to check a word before attempting to add it:
```bash
python3 build/manage_candidates.py check "漢字" "かんじ"
```

### Batch Checking (Optional)
To check multiple words at once before adding:
```bash
python3 build/check_duplicate.py --batch "食べる:たべる" "飲む:のむ" "書く:かく"
```

### Near-Duplicates to Watch For
The automatic check catches exact matches. You should still watch for:
- **Verb forms**: する verbs may exist as standalone nouns (勉強 vs 勉強する)
- **Kanji variants**: 見る and 観る, 聞く and 聴く
- **Okurigana variations**: 行なう vs 行う, 現われる vs 現れる
- **Prefix/suffix forms**: Check if 大～ or ～的 forms exist separately

## Selection Strategy: Balanced Coverage

As the dictionary approaches 6,000+ entries, basic vocabulary gaps become rarer. Use a **balanced approach** that emphasizes harder-to-find vocabulary:

### Tier 1: Core Vocabulary Gaps (20-30 candidates)
*De-emphasized: Most basic vocabulary is already covered at this dictionary size.*

Check for missing **fundamental words** that may have been overlooked:
- Basic verbs, adjectives, nouns, adverbs
- Essential particles and conjunctions
- Numbers, counters, time words

**Method**: Spot-check basic vocabulary lists. Most will already exist, but occasional gaps may remain.

### Tier 2: Semantic Domain Completion (50-70 candidates)
Fill gaps in **semantic categories** already partially covered:
- If 猫 exists but not 犬, add 犬
- If 春 and 夏 exist but not 秋 and 冬, add those
- Check body parts, family terms, colors, directions, weather, days/months

**Method**: Read existing entries in a domain, list what's missing.

### Tier 3: Related Word Networks (50-60 candidates)
Expand from existing entries by adding:
- Antonyms of existing words (始まる → 終わる)
- Synonyms at different registers (食べる → 召し上がる, 頂く)
- Transitive/intransitive pairs (開ける → 開く)
- Word families (教える → 教育, 教室, 教師)

**Method**: Review recent entries' notes sections for mentioned related words.

### Tier 4: Productive Patterns (40-50 candidates)
Add words from systematic patterns:
- Compound verbs: 追い出す, 取り出す, 持ち上げる, etc.
- ～的 adjectives: 積極的, 消極的, 具体的, etc.
- Reduplication: 人々, 日々, 時々, etc.
- Common four-character idioms: 一石二鳥, 十人十色, etc.

### Tier 5: Modern & Informal Vocabulary (30-40 candidates)
Add contemporary terms with stable usage:
- Technology: アプリ, ダウンロード, 検索, etc.
- Social media/internet: フォロー, 投稿, バズる, etc.
- Lifestyle: コスパ, タイパ, リモート, etc.
- Colloquial expressions: マジ, やばい, めっちゃ, etc.

## Selection Criteria

**Must NOT be:**
- Proper nouns (place names, personal names, brand names)
- Highly ephemeral slang
- Vulgar or discriminatory language
- Extremely specialized technical jargon

**Should BE:**
- Words appropriate for the three-tier vocabulary system (basic, core, or general tier)
- Semantically related to existing entries
- Modern terms with widespread, stable usage
- Useful informal expressions learners need to understand

## Priority Guidance

At the current dictionary size (~6000 entries, goal 10,000):
- **High priority**: Semantic domain completion, related word networks, productive patterns
- **Medium priority**: Modern vocabulary, specialized but common terms
- **Lower priority**: Basic vocabulary gaps (mostly filled), rare expressions

The goal is comprehensive coverage of common vocabulary before expanding into specialized domains.

## Output Format

After adding candidates, report:
1. Number of words added
2. Breakdown by tier/category
3. Notable gaps identified for future sessions
