---
name: find-candidates
description: Guidelines for systematically finding new candidate words to add to candidate_words.json for later dictionary entry creation.
user_invocable: true
invocations:
  - /find-candidates
---

# Finding Candidate Words for the Dictionary

Use this skill when asked to find new words to add to `candidate_words.json` for later addition to the dictionary.

## Workflow Overview

1. Determine the search strategy based on user request (semantic expansion, frequency-based, etc.)
2. Check each word against eligibility criteria
3. Add qualifying words to `candidate_words.json` using the manage_candidates script
4. Report what was added

## Eligibility Criteria (ALL must be met)

Before adding any word, verify:

### 1-1. Not Already in the Dictionary

Check that the word is NOT already in `entries_index.json`:
```bash
grep -i '"reading": "たべる"' entries_index.json
```

### 1-2. Not Already a Candidate

Check that the word is NOT already in `candidate_words.json`:
```bash
grep -i '"reading": "たべる"' candidate_words.json
```

### 1-3. Not a Proper Noun

**EXCLUDE** the following categories:
- Place names (東京, ニューヨーク, 富士山, etc.)
- Personal names (田中, マイク, etc.)
- Company/brand names (トヨタ, ソニー, etc.)
- Other proper nouns (specific event names, specific work titles, etc.)

**Note:** Proper nouns may be added systematically in a future phase.

## Selection Criteria (At least ONE must be met)

A word qualifies for addition if it meets at least one of these criteria:

### 2-1. Similar Frequency/Centrality to Existing Entries

The word should have a usage frequency or centrality to contemporary Japanese similar to words already in `entries_index.json`.

**How to assess:**
- Consider whether the word would appear in JLPT N5-N1 vocabulary lists
- Consider whether an intermediate learner would encounter this word regularly
- Compare to existing entries at similar frequency levels

**Examples:** Core vocabulary missing from the dictionary, words from standard frequency lists (BCCWJ, newspapers, etc.)

### 2-2. Semantic Relation to Existing Entries

The word is a common **synonym**, **antonym**, or **related word** to an entry already in the dictionary.

**Types of semantic relations:**
- **Synonyms:** 美しい ↔ きれい, 言う ↔ 話す
- **Antonyms:** 大きい ↔ 小さい, 始まる ↔ 終わる
- **Semantic groups:** Words belonging to the same category as existing entries

**Common semantic groups to check:**
- Body parts (頭, 手, 足, 目, 耳, 口, 鼻, 首, 肩, 腕, 指, 背中, 腹, 胸, 腰, 膝, etc.)
- Days of the week (月曜, 火曜, etc.)
- Months (一月, 二月, etc.)
- Seasons (春, 夏, 秋, 冬)
- Common foods (米, 肉, 魚, 野菜, 果物, パン, 麺, etc.)
- Common animals (犬, 猫, 鳥, 魚, 虫, etc.)
- Celestial bodies (太陽, 月, 星, 地球, etc.)
- Colors (赤, 青, 黄, 緑, 白, 黒, etc.)
- Family terms (父, 母, 兄, 姉, 弟, 妹, 祖父, 祖母, etc.)
- Counters (〜個, 〜本, 〜枚, 〜匹, 〜冊, etc.)
- Time expressions (朝, 昼, 夜, 今日, 明日, 昨日, etc.)
- Weather terms (晴れ, 雨, 雪, 風, 曇り, etc.)
- Directions (上, 下, 右, 左, 前, 後ろ, 中, 外, etc.)
- Onomatopoeia/Mimesis (ぴかぴか, ふわふわ, どきどき, わくわく, etc.)
- Common verbs by category (motion, communication, perception, etc.)

**Additional categories for systematic coverage:**

1. **Compound verbs (V+V)** - Verbs formed by combining two verbs
   - Examples: 追い出す, 切り離す, 取り出す, 持ち上げる, 引き受ける, 打ち合わせる
   - Common first elements: 追い〜, 切り〜, 取り〜, 持ち〜, 引き〜, 打ち〜, 飛び〜, 押し〜

2. **Reduplication words (畳語)** - Words formed by repeating elements (beyond onomatopoeia)
   - Examples: 人々, 国々, 山々, 木々, 我々, 日々, 時々, 様々, 各々, 次々

3. **Four-character idioms (四字熟語)** - Common yojijukugo for learners
   - Examples: 一石二鳥, 以心伝心, 一期一会, 自業自得, 十人十色, 一生懸命

4. **Proverbs (諺)** - Frequently referenced sayings
   - Examples: 猿も木から落ちる, 七転び八起き, 塵も積もれば山となる, 石の上にも三年

5. **Abbreviated words (略語)** - Modern contractions and shortenings
   - Examples: 就活, 婚活, 終活, リモワ, ワーホリ, コスパ, タイパ, 推し活

6. **Cooking verbs and techniques** - Kitchen and food preparation vocabulary
   - Examples: 炒める, 茹でる, 蒸す, 煮込む, 和える, 漬ける, 焼く, 揚げる, 炊く

7. **Medical/anatomical terms** - Beyond basic body parts
   - Examples: 臓器, 神経, 血管, 細胞, 骨髄, 関節, 筋肉, 内臓, 免疫

8. **Legal/administrative terms** - Forms, procedures, and official vocabulary
   - Examples: 届出, 申請, 認可, 免除, 届け出, 登録, 手続き, 証明

9. **Traditional Japanese items** - Cultural objects and architectural features
   - Examples: 畳, 障子, 床の間, 縁側, 風呂敷, 扇子, 提灯, 暖簾

10. **Japanese cuisine terms** - Food categories and cooking concepts
    - Examples: 出汁, 煮物, 焼き物, 揚げ物, 漬物, 薬味, 惣菜, 珍味

11. **～的 na-adjectives** - Productive Sino-Japanese adjectival pattern
    - Examples: 積極的, 消極的, 具体的, 抽象的, 一般的, 基本的, 個人的, 社会的

12. **Paired antonym compounds** - Two-kanji compounds expressing opposites
    - Examples: 上下, 左右, 前後, 内外, 表裏, 出入り, 売買, 往復, 開閉

13. **Emotional/psychological nouns** - Nominalized feelings and mental states
    - Examples: 焦り, 苛立ち, 戸惑い, 安堵, 憂鬱, 苦悩, 葛藤, 動揺

14. **Set grammatical expressions** - Phrases that function as vocabulary items
    - Examples: ～というわけで, ～に関して, ～において, ～に対して, ～について

15. **Loanwords by domain** - Systematic coverage of borrowed vocabulary by field
    - Sports: ドリブル, シュート, パス, オフサイド
    - Fashion: コーデ, トレンド, ヴィンテージ
    - Music: リフ, ビート, サビ, アレンジ

16. **Ritual/ceremonial terms** - Life events, customs, and traditions
    - Examples: 初詣, 七五三, 還暦, 厄年, 法事, 盆踊り, 初節句

17. **Honorific vocabulary pairs** - Keigo expressions beyond basic verbs
    - Examples: お召し上がり/頂く, ご覧/拝見, お越し/参る, ご存知/存じる

18. **Sound-symbolic words by source** - Onomatopoeia organized by what produces the sound
    - Water: ざぶざぶ, じゃぶじゃぶ, ぽたぽた
    - Fire: めらめら, ぼうぼう, ちろちろ
    - Machines: がたがた, ぶんぶん, カチカチ

19. **Sino-Japanese number compounds** - Number + noun patterns
    - Examples: 一流, 二重, 三角, 四季, 五感, 六法, 七夕, 八方, 九九

20. **Sentence-final expressions** - Pragmatic and modal markers
    - Examples: ～かしら, ～ものか, ～ではないか, ～じゃないか, ～ことか, ～ものだ

**Approach:** When reviewing an existing entry, identify gaps in related vocabulary.

### 2-3. Post-2000 Widespread Terms

Words that have come into widespread usage since approximately 2000.

**Categories to consider:**
- Technology terms (スマホ, アプリ, ダウンロード, etc.)
- Internet/social media (SNS, フォロー, バズる, etc.)
- Modern lifestyle (コンビニ, ペットボトル, エコ, etc.)
- Contemporary culture (推し, 沼, 盛る, etc.)
- Wasei-eigo coinages (リモート, テレワーク, etc.)

**Note:** Include only terms with stable, widespread usage—not fleeting slang.

### 2-4. Informal/Slang Terms Useful for Learners

Well-known informal or colloquial terms that:
- Do not typically appear on formal vocabulary lists
- Are commonly encountered in everyday Japanese
- Would help learners understand natural speech

**Examples:**
- Common contractions (じゃん, っす, etc.)
- Casual expressions (マジ, やばい, ダサい, etc.)
- Colloquial variants (めっちゃ, すげー, etc.)
- Youth slang with staying power (ウザい, キモい, etc.)

**Exclude:** Highly ephemeral slang, vulgar terms, discriminatory language

## Adding Candidates

After identifying qualifying words, add them using:

```bash
python3 build/manage_candidates.py add "漢字表記" "ひらがな読み" "brief English note"
```

**Notes field guidance:**
- Brief English gloss or description
- Can include part of speech hint
- Keep under 50 characters

**Example:**
```bash
python3 build/manage_candidates.py add "推し" "おし" "one's favorite (idol/character); to support"
```

## Search Strategies

When asked to find candidates, consider these approaches:

### Strategy 1: Semantic Gap Analysis
1. Pick a semantic domain (e.g., body parts)
2. List words that should be in that domain
3. Check which are missing from entries_index.json
4. Add missing words as candidates

### Strategy 2: Entry Cross-Reference Expansion
1. Read recent dictionary entries
2. For each entry, identify synonyms, antonyms, and related words mentioned in notes
3. Check if those related words are in the dictionary
4. Add missing ones as candidates

### Strategy 3: Frequency List Comparison
1. Reference standard frequency data (JLPT lists, BCCWJ rankings)
2. Identify high-frequency words not yet in the dictionary
3. Add as candidates

### Strategy 4: Modern Vocabulary Audit
1. Consider common contemporary terms (technology, lifestyle, internet)
2. Verify they have stable, widespread usage
3. Add as candidates

## Output Format

After adding candidates, report:
1. Number of words added
2. Summary of categories/sources
3. Any notable gaps identified for future sessions

## Quality Reminders

- **Breadth over depth:** Aim for broad coverage across semantic domains
- **Learner utility:** Prioritize words an intermediate learner would benefit from knowing
- **Avoid duplicates:** Always check both entries_index.json AND candidate_words.json
- **No proper nouns:** Save those for systematic addition later
- **Stable vocabulary:** Avoid ephemeral slang or highly specialized jargon
