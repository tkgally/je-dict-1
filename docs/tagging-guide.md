# Dictionary Entry Tagging Guide

This guide documents the tagging system for je-dict-1 dictionary entries. Tags enable rich search, filtering, and categorization of vocabulary.

## Overview

Each dictionary entry can have the following tag categories in `metadata.tags`:

| Tag Category | Type | Description |
|--------------|------|-------------|
| `pos` | array | Part of speech (canonical forms) |
| `transitivity` | string | Verb transitivity (verbs only) |
| `formality` | string | Register/formality level |
| `politeness` | string | Keigo classification |
| `style` | array | Style/medium associations |
| `domain` | array | Specialized usage domains |
| `semantic` | array | Semantic categories |

---

## Part of Speech (`pos`)

Canonical part-of-speech values. Entries may have multiple values (e.g., a word that functions as both noun and verb).

### Canonical Values

| Value | Japanese | Description | Examples |
|-------|----------|-------------|----------|
| `noun` | 名詞 | Noun | 本, 学校, 時間 |
| `verb-godan` | 五段動詞 | Godan (consonant-stem) verb | 書く, 話す, 読む |
| `verb-ichidan` | 一段動詞 | Ichidan (vowel-stem) verb | 食べる, 見る, 起きる |
| `verb-suru` | する動詞 | Suru verb (verbal noun + する) | 勉強する, 運動する |
| `verb-kuru` | 来る | Irregular verb 来る | 来る |
| `verb-irregular` | 不規則動詞 | Other irregular verbs | ある |
| `adjective-i` | イ形容詞 | I-adjective | 大きい, 新しい, 楽しい |
| `adjective-na` | ナ形容詞 | Na-adjective | 静か, 元気, きれい |
| `adjective-no` | の形容詞 | No-adjective (prenominal with の) | 本当の, 普通の |
| `adjective-taru` | タルト形容詞 | Taru-adjective (archaic/literary) | 堂々たる |
| `adverb` | 副詞 | Adverb | とても, ゆっくり, すぐ |
| `particle` | 助詞 | Particle | は, が, を, に |
| `conjunction` | 接続詞 | Conjunction | そして, しかし, だから |
| `interjection` | 感動詞 | Interjection | ああ, えっ, おい |
| `pronoun` | 代名詞 | Pronoun | 私, あなた, これ |
| `counter` | 助数詞 | Counter | 人, 本, 匹 |
| `prefix` | 接頭辞 | Prefix | お, ご, 不 |
| `suffix` | 接尾辞 | Suffix | さん, 的, 化 |
| `expression` | 表現 | Expression/phrase/idiom | お疲れ様, よろしく |
| `pre-noun-adjectival` | 連体詞 | Pre-noun adjectival | この, その, 大きな |
| `number` | 数詞 | Number | 一, 二, 三 |
| `auxiliary` | 助動詞 | Auxiliary verb/adjective | ない, たい, らしい |
| `onomatopoeia` | 擬音語・擬態語 | Onomatopoeia/mimetic | ぴかぴか, どんどん |

### Multiple Parts of Speech

Many words function as multiple parts of speech. Use arrays:

```json
"metadata": {
  "tags": {
    "pos": ["noun", "verb-suru"]
  }
}
```

Common combinations:
- `["noun", "verb-suru"]` - Verbal nouns (勉強, 運動)
- `["noun", "adjective-na"]` - Na-adjective nouns (元気, 静か)
- `["adverb", "adjective-na"]` - Adverbs that can modify nouns (本当に/本当な)
- `["noun", "adjective-no"]` - Nouns used prenominally with の

---

## Transitivity (`transitivity`)

**Applies to**: verb-godan, verb-ichidan, verb-suru, verb-kuru, verb-irregular

| Value | Japanese | Description | Examples |
|-------|----------|-------------|----------|
| `transitive` | 他動詞 | Takes direct object with を | 食べる, 見る, 書く |
| `intransitive` | 自動詞 | No direct object | 行く, 来る, 起きる |
| `both` | 両用 | Can be used either way | 開く, 閉まる |

### Transitivity Pairs

Many verbs have transitive/intransitive pairs. These should be cross-referenced:

| Transitive | Intransitive | Meaning |
|------------|--------------|---------|
| 開ける (あける) | 開く (あく) | open |
| 閉める (しめる) | 閉まる (しまる) | close |
| 出す (だす) | 出る (でる) | put out / go out |

---

## Formality (`formality`)

Speech register/formality level.

| Value | Description | Usage Context | Examples |
|-------|-------------|---------------|----------|
| `formal` | Formal language | Business, official, academic | ございます, 申し上げる |
| `neutral` | Standard polite | General polite conversation | です, ます forms |
| `informal` | Casual language | Friends, family, close colleagues | だ, plain forms |
| `vulgar` | Crude/vulgar | Very casual, potentially offensive | くそ, slang |

**Default**: Most entries should be tagged `neutral` unless specifically formal/informal.

---

## Politeness (`politeness`)

Keigo (敬語) classification for honorific language.

| Value | Japanese | Description | Examples |
|-------|----------|-------------|----------|
| `honorific` | 尊敬語 | Elevates the subject (other person) | いらっしゃる, おっしゃる, 召し上がる |
| `humble` | 謙譲語 | Lowers the speaker | 申す, 参る, いただく |
| `polite` | 丁寧語 | General politeness (です/ます) | です, ます, ございます |
| `plain` | 普通形 | Plain/dictionary form | だ, 食べる, 行く |

**Default**: Most entries should be tagged `plain` unless specifically keigo.

---

## Style (`style`)

Style or medium associations. Can have multiple values.

| Value | Description | Examples |
|-------|-------------|----------|
| `written` | Primarily written language | である, において, 及び |
| `spoken` | Primarily spoken language | じゃん, っす, ってば |
| `literary` | Literary or poetic | 美し, 愛でる |
| `archaic` | Archaic or obsolete | おる (formal), 候 |
| `slang` | Modern slang | マジ, やばい, 草 |

**Note**: Only tag if there's a clear association. Most words are used in both written and spoken Japanese.

---

## Domain (`domain`)

Specialized usage domains. Can have multiple values.

| Value | Description | Examples |
|-------|-------------|----------|
| `business` | Business/corporate | 取引, 会議, 報告 |
| `academic` | Academic/scholarly | 論文, 研究, 仮説 |
| `technical` | Technical/scientific | プログラム, データ |
| `legal` | Legal/judicial | 契約, 訴訟, 法律 |
| `medical` | Medical/health | 診断, 症状, 治療 |
| `colloquial` | Everyday speech | Common expressions |
| `internet` | Internet/social media | 草, ワロタ, www |

---

## Semantic Categories (`semantic`)

Content classification for vocabulary grouping. Can have multiple values.

### Time & Calendar

| Tag | Description | Examples |
|-----|-------------|----------|
| `time-day-of-week` | Days of the week | 月曜日, 火曜日 |
| `time-month` | Months | 一月, 二月 |
| `time-season` | Seasons | 春, 夏, 秋, 冬 |
| `time-period` | Time periods | 朝, 昼, 夜, 午前 |
| `time-general` | General time concepts | 時間, 今, 後 |

### Nature & Animals

| Tag | Description | Examples |
|-----|-------------|----------|
| `animal-mammal` | Mammals | 犬, 猫, 象 |
| `animal-bird` | Birds | 鳥, 鶴, 雀 |
| `animal-fish` | Fish/sea creatures | 魚, 鯛, 蛸 |
| `animal-insect` | Insects | 虫, 蝶, 蟻 |
| `animal-general` | General animal terms | 動物, 生き物 |
| `plant-tree` | Trees | 木, 桜, 松 |
| `plant-flower` | Flowers | 花, 薔薇, 菊 |
| `plant-general` | General plants | 植物, 草, 葉 |
| `weather` | Weather | 雨, 雪, 風, 晴れ |
| `geography` | Geographic features | 山, 川, 海 |

### Human & Body

| Tag | Description | Examples |
|-----|-------------|----------|
| `body-part` | External body parts | 手, 足, 頭, 目 |
| `body-internal` | Internal organs | 心臓, 肺, 骨 |
| `family` | Family relationships | 父, 母, 兄, 姉 |
| `occupation` | Jobs/professions | 医者, 先生, 警察 |
| `person` | General person terms | 人, 男, 女, 子供 |

### Abstract Concepts

| Tag | Description | Examples |
|-----|-------------|----------|
| `emotion` | Emotions/feelings | 嬉しい, 悲しい, 怒り |
| `color` | Colors | 赤, 青, 白, 黒 |
| `number` | Numbers | 一, 二, 三, 百 |
| `direction` | Directions | 北, 南, 上, 下 |
| `size` | Size/dimension | 大きい, 小さい, 長い |
| `quantity` | Quantity/amount | 多い, 少ない, 全部 |

### Objects & Places

| Tag | Description | Examples |
|-----|-------------|----------|
| `food` | Food/drinks | ご飯, パン, 水, 酒 |
| `clothing` | Clothing | 服, 靴, 帽子 |
| `building` | Buildings | 家, 学校, 駅 |
| `transportation` | Vehicles | 車, 電車, 飛行機 |
| `tool` | Tools | ペン, 鋏, 鍵 |
| `furniture` | Furniture | 机, 椅子, ベッド |
| `electronics` | Electronics | 電話, テレビ, パソコン |

### Actions

| Tag | Description | Examples |
|-----|-------------|----------|
| `movement` | Physical movement | 行く, 来る, 歩く |
| `communication` | Communication | 話す, 聞く, 書く |
| `cognition` | Mental actions | 思う, 知る, 考える |
| `existence` | Existence/presence | ある, いる, なる |
| `creation` | Creating/making | 作る, 建てる, 描く |
| `consumption` | Consuming | 食べる, 飲む, 使う |

### Social

| Tag | Description | Examples |
|-----|-------------|----------|
| `greeting` | Greetings | おはよう, こんにちは |
| `education` | Education | 勉強, 学校, 先生 |
| `work` | Work/employment | 仕事, 会社, 働く |
| `leisure` | Leisure/entertainment | 遊ぶ, 映画, 旅行 |

### Special Categories

| Tag | Description | Examples |
|-----|-------------|----------|
| `proverb` | Proverbs/sayings | 猿も木から落ちる |
| `idiom` | Four-character idioms | 一石二鳥, 以心伝心 |

---

## Example Entry with Tags

```json
{
  "id": "00001_taberu",
  "headword": "食べる",
  "reading": "たべる",
  "part_of_speech": "verb (ichidan, transitive)",
  "gloss": "to eat",
  "metadata": {
    "created": "2025-01-01T00:00:00Z",
    "modified": "2025-01-01T00:00:00Z",
    "vocabulary_tier": "basic",
    "tags": {
      "pos": ["verb-ichidan"],
      "transitivity": "transitive",
      "formality": "neutral",
      "politeness": "plain",
      "semantic": ["consumption", "food"]
    }
  }
}
```

---

## Tagging Guidelines

### Required Tags

Every entry MUST have:
1. `pos` - At least one part of speech

### Recommended Tags

- **Verbs**: Should have `transitivity`
- **All entries**: Should have `formality` (default to "neutral")
- **All entries**: Should have `politeness` (default to "plain")
- **Concrete nouns**: Should have relevant `semantic` categories

### Multiple Tags

- Use arrays for entries with multiple functions
- Order by primary/most common usage first
- Include all relevant semantic categories (a word can be both `food` and `time-period`)

### When NOT to Tag

- Don't add `style` unless clearly written-only/spoken-only
- Don't add `domain` unless domain-specific
- Don't over-tag semantic categories - stick to clear, primary meanings

---

## Reference Files

- **Tag Taxonomy**: `build/tag_taxonomy.json` - Complete tag definitions
- **POS Mapping**: `build/pos_mapping.json` - Legacy part_of_speech to canonical mapping
- **Schema**: `build/schema.json` - JSON schema including tag fields
