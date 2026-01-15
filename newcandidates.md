# New Candidate Words Prompt

Add 200 new candidates to candidate_words.json using the find-candidates skill.

## Quick Context

- Check current state: `head -10 candidate_words.json` (shows total_candidates and next_id)
- Check entry count: `head -5 entries_index.json` (shows total_entries in metadata)

## Workflow

1. Load the find-candidates skill for detailed guidelines
2. Choose search strategies appropriate for the dictionary's current size (see below)
3. **Before adding each word, verify it doesn't already exist** (MANDATORY):
   ```bash
   # Check dictionary entries (search BOTH reading and headword)
   grep -r '"reading": "たべる"' entries/
   grep -r '食べる' entries/

   # Check existing candidates
   grep -i '"reading": "たべる"' candidate_words.json
   grep -i '食べる' candidate_words.json
   ```
   **If ANY of these return results, DO NOT add the word.** Move to next candidate.

4. Add candidates using: `python3 build/manage_candidates.py add "漢字" "ひらがな" "brief English note"`

5. After adding all candidates, update PROJECT_STATUS.md:
   - Update "Candidate words" count in Content Status section
   - Add a brief session note under Recent Changes

6. Finally, build the website:
   ```bash
   python3 build/build_flat.py        # REQUIRED for live site update
   ```

## Selection Strategy: Balanced Coverage

As the dictionary approaches 10,000 entries, use a **balanced approach** that includes:

### Tier 1: Core Vocabulary Gaps (40-50 candidates)
Check for missing **fundamental words** that may have been overlooked:
- Basic verbs: する, なる, ある, いる, 行く, 来る, 見る, 聞く, 言う, 思う, 知る, 分かる
- Basic adjectives: いい/良い, 悪い, 新しい, 古い, 大きい, 小さい, 高い, 安い, 近い, 遠い
- Basic nouns: 人, 物, 事, 所, 時, 日, 年, 月, 名前, 言葉, 意味, 気持ち, 考え
- Common adverbs: とても, もっと, まだ, もう, よく, すぐ, 本当に, 多分, 全然, 絶対
- Essential particles and conjunctions: しかし, でも, だから, そして, または, それに
- Numbers, counters, time words: basic gaps in these systematic categories

**Method**: Check JLPT N5-N4 word lists against entries_index.json systematically.

### Tier 2: Semantic Domain Completion (60-80 candidates)
Fill gaps in **semantic categories** already partially covered:
- If 猫 exists but not 犬, add 犬
- If 春 and 夏 exist but not 秋 and 冬, add those
- Check body parts, family terms, colors, directions, weather, days/months

**Method**: Read existing entries in a domain, list what's missing.

### Tier 3: Related Word Networks (40-50 candidates)
Expand from existing entries by adding:
- Antonyms of existing words (始まる → 終わる)
- Synonyms at different registers (食べる → 召し上がる, 頂く)
- Transitive/intransitive pairs (開ける → 開く)
- Word families (教える → 教育, 教室, 教師)

**Method**: Review recent entries' notes sections for mentioned related words.

### Tier 4: Productive Patterns (30-40 candidates)
Add words from systematic patterns:
- Compound verbs: 追い出す, 取り出す, 持ち上げる, etc.
- ～的 adjectives: 積極的, 消極的, 具体的, etc.
- Reduplication: 人々, 日々, 時々, etc.
- Common four-character idioms: 一石二鳥, 十人十色, etc.

### Tier 5: Modern & Informal Vocabulary (20-30 candidates)
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
- Words a JLPT N5-N1 learner would encounter
- Semantically related to existing entries
- Modern terms with widespread, stable usage
- Useful informal expressions learners need to understand

## Priority Guidance

At the current dictionary size (~5000 entries, goal 10,000):
- **High priority**: Core vocabulary gaps, completing semantic domains
- **Medium priority**: Related word networks, productive patterns
- **Lower priority**: Specialized vocabulary, rare expressions

The goal is comprehensive coverage of common vocabulary before expanding into specialized domains.

## Output Format

After adding candidates, report:
1. Number of words added
2. Breakdown by tier/category
3. Notable gaps identified for future sessions
