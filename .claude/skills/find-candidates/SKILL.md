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

1. Determine the search strategy based on user request and dictionary maturity
2. Check each word against eligibility criteria (MANDATORY duplicate checks)
3. Add qualifying words to `candidate_words.json` using the manage_candidates script
4. Report what was added

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
  Exact match in dictionary: 00001_taberu (食べる / たべる)

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

### Near-Duplicate Patterns to Watch

The automatic check catches exact matches. You should still watch for:
- **Verb forms**: する verbs may exist as standalone nouns (勉強 vs 勉強する)
- **Kanji variants**: 見る/観る, 聞く/聴く - check if one already covers the meaning
- **Okurigana variations**: 行なう/行う, 現われる/現れる
- **Prefix/suffix forms**: Check if 大～ or ～的 forms exist as part of other entries
- **Reading variations**: Long vowels (おう vs おお), particles in readings

## Eligibility Criteria (ALL must be met)

### 1-1. Not Already in the Dictionary

Check that the word is NOT already in `entries_index.json` (by reading AND headword).

### 1-2. Not Already a Candidate

Check that the word is NOT already in `candidate_words.json` (by reading AND word).

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
- Evaluate words based on the three-tier vocabulary system (see vocabulary-tiers skill): basic (fundamental 600-800 words), core (1600-2000 words for adult communication), or general (all other useful vocabulary)
- Consider whether an intermediate learner would encounter this word regularly
- Compare to existing entries at similar frequency levels

### 2-2. Semantic Relation to Existing Entries

The word is a common **synonym**, **antonym**, or **related word** to an entry already in the dictionary.

**Types of semantic relations:**
- **Synonyms:** 美しい ↔ きれい, 言う ↔ 話す
- **Antonyms:** 大きい ↔ 小さい, 始まる ↔ 終わる
- **Semantic groups:** Words belonging to the same category as existing entries

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

---

## Search Strategies

The dictionary now has ~5,900 entries plus ~970 candidates. Basic vocabulary is largely covered. Prioritize strategies that find remaining gaps.

### HIGH PRIORITY Strategies (Use These First)

#### Strategy A: Corpus-Driven Gap Analysis
Use corpus frequency data to find common words still missing.

**Method:**
1. Consider the top 10,000 words in corpora like BCCWJ (Balanced Corpus of Contemporary Written Japanese)
2. Compare against entries_index.json
3. Words in the top 10,000 by frequency that aren't in the dictionary are high-priority candidates

**Why effective:** Guarantees discovered words are genuinely common.

#### Strategy B: Collocational Mining
Find words that commonly appear with existing entries but aren't in the dictionary.

**Method:**
1. Take existing entries, especially verbs and adjectives
2. Consider their most common collocates (words they frequently appear with)
3. Check if those collocates are in the dictionary

**Examples:**
- If 約束 exists, check: 守る, 破る, 果たす (promise-related verbs)
- If 責任 exists, check: 取る, 負う, 問う, 逃れる (responsibility-related verbs)
- If 注意 exists, check: 払う, 向ける, 引く (attention-related verbs)

**Why effective:** Finds words learners need to use existing vocabulary naturally.

#### Strategy C: Productive Pattern Completion
Systematically complete morphological patterns already partially in the dictionary.

**Patterns to check:**
1. **Compound verbs** - For each V1 element (追い-, 取り-, 引き-, 切り-, etc.), list all common V1+V2 combinations
2. **～的 adjectives** - Check which common ～的 words are missing
3. **Paired compounds** - Check 上下, 左右, 前後 pattern for gaps
4. **Nominalized verbs** - 動詞 → ～み, ～さ, ～り forms (悲しみ, 高さ, 眠り)

**Why effective:** These patterns are productive and predictable; gaps are easy to identify systematically.

#### Strategy D: Register/Formality Pairs
For existing entries, find their register variants (formal ↔ informal, written ↔ spoken).

**Method:**
1. Take informal words in the dictionary, find their formal equivalents
2. Take formal/written words, find their colloquial equivalents
3. Check keigo (honorific) variants of common verbs

**Examples:**
- If いる exists, check: おる, いらっしゃる, おいでになる
- If 食べる exists, check: 召し上がる, 頂く, 食う
- If でも exists, check: しかし, しかしながら, けれども, だけど

**Why effective:** Learners need multiple registers; dictionaries often have gaps here.

#### Strategy E: Domain-Specific Systematic Sweeps
Pick a semantic domain and exhaustively check for gaps.

**Underexplored domains to investigate:**
1. **Cooking/food preparation**: 下ごしらえ, 味付け, 盛り付け, 火加減, etc.
2. **Health/medical**: 症状, 診察, 処方, 副作用, 通院, etc.
3. **Housing/real estate**: 間取り, 敷金, 礼金, 更新, 退去, etc.
4. **Employment/work**: 採用, 昇進, 異動, 退職, 有給, etc.
5. **Finance/money**: 振込, 引き落とし, 残高, 利息, 手数料, etc.
6. **Transportation**: 乗り換え, 運賃, 定期, 遅延, 運休, etc.
7. **Education**: 入学, 卒業, 進学, 留年, 履修, etc.
8. **Legal/administrative**: 届出, 申請, 届け, 届ける, 認可, etc.

**Why effective:** Practical vocabulary in these domains is essential for living in Japan but often missing from learner dictionaries.

#### Strategy F: Written vs Spoken Japanese Gap Analysis
Find words common in one medium but potentially missing from the dictionary.

**Written Japanese gaps:**
- Newspaper/news vocabulary: 懸念, 是正, 遺憾, 謝罪, 声明
- Academic/essay words: 考察, 検討, 概要, 結論, 要旨
- Literary expressions: ～ざるを得ない, ～にほかならない, ～といえども

**Spoken Japanese gaps:**
- Conversational fillers: えーと, あのー, なんか, ほら, ねえ
- Sentence-final particles beyond basics: さ, ぜ, わ, かな, もん
- Contracted forms: ～ちゃう, ～とく, ～てる, ～なきゃ

**Why effective:** Dictionaries often skew toward one medium; this ensures balanced coverage.

#### Strategy G: Loanword Systematic Coverage
Methodically cover loanwords by domain, as these are often underrepresented.

**Domains with heavy loanword use:**
1. **IT/Computing**: アプリ, ブラウザ, サーバー, クラウド, ストレージ
2. **Business**: プレゼン, ミーティング, アジェンダ, フィードバック
3. **Sports**: specific to each sport beyond basics
4. **Fashion**: コーデ, トレンド, アイテム, ブランド
5. **Music**: ライブ, フェス, サビ, アレンジ, カバー
6. **Food service**: テイクアウト, デリバリー, ドリンクバー

**Method:** Pick a domain, list common loanwords used in that context, check dictionary.

**Why effective:** Loanwords are essential for modern Japanese but often treated inconsistently.

### MEDIUM PRIORITY Strategies

#### Strategy H: Semantic Gap Analysis
*Still useful but many obvious gaps are filled.*

1. Pick a semantic domain (e.g., body parts)
2. List words that should be in that domain
3. Check which are missing from entries_index.json
4. Add missing words as candidates

**Common semantic groups:**
- Body parts, days/months, seasons, foods, animals, colors, family terms, counters, time expressions, weather, directions, onomatopoeia

#### Strategy I: Entry Cross-Reference Expansion
*Useful for incremental expansion.*

1. Read recent dictionary entries
2. For each entry, identify synonyms, antonyms, and related words mentioned in notes
3. Check if those related words are in the dictionary
4. Add missing ones as candidates

#### Strategy J: Four-Character Idioms and Proverbs
*Many common ones may already be covered; check systematically.*

**Yojijukugo categories:**
- Describing personality: 誠心誠意, 温厚篤実, 軽挙妄動
- Describing situations: 一触即発, 暗中模索, 危機一髪
- Describing actions: 試行錯誤, 取捨選択, 創意工夫

**Proverbs:** Focus on those frequently referenced in modern contexts.

### LOWER PRIORITY Strategies
*Basic coverage is largely complete; use these only for spot-checking.*

#### Strategy K: Frequency List Comparison
*Most high-frequency words are now covered.*

1. Reference standard frequency data (JLPT lists, BCCWJ rankings)
2. Identify high-frequency words not yet in the dictionary
3. Add as candidates

**Note:** At nearly 6,000 entries, most JLPT N5-N2 vocabulary should be covered. Focus on finding remaining gaps rather than systematic sweeps.

#### Strategy L: Basic Vocabulary Audit
*Diminishing returns at current dictionary size.*

Spot-check for overlooked basics:
- Basic verbs, adjectives, nouns
- Essential particles and conjunctions
- Core adverbs

---

## Extended Category Reference

### Compound verbs (V+V)
Common first elements: 追い～, 切り～, 取り～, 持ち～, 引き～, 打ち～, 飛び～, 押し～, 差し～, 突き～, 振り～, 掛け～, 落ち～, 受け～

### Reduplication words (畳語)
人々, 国々, 山々, 木々, 我々, 日々, 時々, 様々, 各々, 次々, 徐々, 段々, 益々, 偶々

### ～的 na-adjectives
積極的, 消極的, 具体的, 抽象的, 一般的, 基本的, 個人的, 社会的, 精神的, 物理的, 心理的, 論理的, 感情的, 効果的, 現実的, 理想的

### Paired antonym compounds
上下, 左右, 前後, 内外, 表裏, 出入り, 売買, 往復, 開閉, 増減, 加減, 遠近, 高低, 大小, 長短, 強弱, 明暗, 善悪, 正誤, 生死

### Emotional/psychological nouns
焦り, 苛立ち, 戸惑い, 安堵, 憂鬱, 苦悩, 葛藤, 動揺, 羨望, 嫉妬, 後悔, 悔しさ, 寂しさ, 切なさ, 懐かしさ

### Set grammatical expressions
～というわけで, ～に関して, ～において, ～に対して, ～について, ～によって, ～として, ～にとって, ～をもって, ～に際して

### Sino-Japanese number compounds
一流, 二重, 三角, 四季, 五感, 六法, 七夕, 八方, 九九, 十分, 百科, 千差万別, 万全

### Onomatopoeia by source
- Water: ざぶざぶ, じゃぶじゃぶ, ぽたぽた, しとしと, ざあざあ
- Fire: めらめら, ぼうぼう, ちろちろ
- Machines: がたがた, ぶんぶん, カチカチ
- Movement: すたすた, のろのろ, ばたばた, ふらふら

---

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

## Output Format

After adding candidates, report:
1. Number of words added
2. Summary of categories/sources
3. Any notable gaps identified for future sessions

## Quality Reminders

- **Duplicates are blocked automatically:** The `manage_candidates.py add` command will refuse to add duplicates
- **Watch for near-duplicates:** The automatic check catches exact matches; manually verify for verb forms, kanji variants, etc.
- **Breadth over depth:** Aim for broad coverage across semantic domains
- **Learner utility:** Prioritize words an intermediate learner would benefit from knowing
- **No proper nouns:** Save those for systematic addition later
- **Stable vocabulary:** Avoid ephemeral slang or highly specialized jargon
- **Use batch checks:** When planning which words to add: `python3 build/check_duplicate.py --batch "word1:reading1" ...`
