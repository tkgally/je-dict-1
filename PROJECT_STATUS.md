# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-09-21
**Current phase**: Phase 6 - Continued Expansion & Polish

**Live site**: https://www.tkgje.jp/

> **Full history**: Older change logs are archived in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
> **Quick reference**: See [PROJECT_CONTEXT_BRIEF.md](PROJECT_CONTEXT_BRIEF.md) for a concise session-start overview.
> **Project setup**: See [CLAUDE.md](CLAUDE.md) for commands, file placement, and skills.

## Current State

**Phase 6: Continued Expansion & Polish** — Adding vocabulary while maintaining v2 quality standards, with an automated pipeline for batch maintenance tasks. The dictionary uses an original three-tier vocabulary classification (basic, core, general) instead of JLPT levels.

### Content Status

These counts are approximate. Run `make report` for accurate, up-to-date numbers.

| Metric | Value |
|--------|-------|
| Total entries | ~30,764 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,981 (open) |
| Candidate words | ~188 (all vetted; queue cleaned 2026-08-11) |
| Cross-references | ~19,000 |
| Example sentences | ~119,000 |

## v2 Quality Standards

Based on multi-model LLM evaluation (Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash), these are the priority enhancements:

### HIGH PRIORITY
1. **Verb transitivity** - Add 自動詞/他動詞 and pair verbs to all verb entries
2. **Aspect notes** - Explain ている behavior for verbs with non-obvious meanings
3. **Particle predicate lists** - List verbs/adjectives requiring each particle
4. **Collocation patterns** - Add common noun-verb pairings

### MEDIUM PRIORITY
1. **Register labels** - Mark casual/neutral/formal for all entries
2. **Similar words** - Add contrastive sections for semantic neighbors
3. **Adjective forms** - Add adverbial (〜く/〜に) and noun forms (〜さ)
4. **Example progression** - Ensure simple → complex ordering

### LOW PRIORITY
1. **Kanji orthography notes** - When to use kanji vs. hiragana
2. **Cultural notes** - Expand where significant
3. **Keigo references** - Link to honorific forms

## Recent Changes

### 2026-10-05 (Routine v3: new-entries — 12 New Entries, IDs 31593–31604)

No internal-closure candidates were queued, so twelve vetted idioms and proverbs from the queue: 腕が鳴る, 拍車をかける,
白羽の矢が立つ, 太鼓判を押す, 血も涙もない, 覆水盆に返らず, 転ばぬ先の杖, 備えあれば憂いなし, 住めば都, 鶴の一声,
火に油を注ぐ, 泣きっ面に蜂. No new kanji. Self-check clean. Seven words their notes use were queued as candidates
(後悔先に立たず, 弱り目に祟り目, 踏んだり蹴ったり, 石橋を叩いて渡る, 腕が上がる, 物価高, 活字離れ); くちばし and ひつまぶし screened.

### 2026-10-04 (Routine v3: new-entries — 20 New Entries, IDs 31573–31592)

Eight words older entries already used: 〜末 (まつ), 雷サージ, 角 (かく), 〜棟 (とう), 保証会社, 現金書留, 炊ける, 飯台.
With the internal-closure queue then empty, twelve vetted idioms from the queue: 虫がいい, 首を突っ込む, 気が引ける,
襟を正す, 気が滅入る, 気を許す, 目を疑う, 目に余る, 手を尽くす, 口を揃える, 焼け石に水, 後の祭り. No new kanji.
45 existing links to 角 (かど) checked against the new 角 (かく): all read かど, unchanged. Self-check skipped (daily
OpenRouter budget spent); くちばし and ひつまぶし still await kana screening.

### 2026-10-04 (Routine v3: new-entries — 20 New Entries, IDs 31553–31572)

Twenty words that older entries already used: 道路交通法, 無失点, ぞろ目, 面取り, 水温計, 烏天狗, 差し押さえる,
頭角を現す, 返り点, 開幕式, 球審, 成績証明書, 遠距離恋愛, ギガバイト, タイピング, 汚す (けがす), 同位体, 決選投票,
神経衰弱 (two senses: nervous exhaustion; the card game), 一皿. No new kanji. Candidate 焼印 dropped (= 焼き印 27135).
Self-check skipped (daily OpenRouter budget spent); くちばし and ひつまぶし await kana screening.

### 2026-10-04 (Routine v3: new-entries — 20 New Entries, IDs 31533–31552)

Twenty words that older entries already used: 抑うつ, 財務省, 院内感染, 機能障害, 動脈瘤, 静脈瘤, 四角四面, フレイル,
闇バイト, うな重, うな丼, ひつまぶし, 白焼き, 戻りガツオ, 表装, 文房四宝, されど, 追い抜き, 共同浴場, 新快速. No new
kanji. The harvester added back-links in 15 neighbours. Two stale candidates removed (許しがたい and そうはいっても
duplicate 許し難い and そうは言っても). Self-check skipped (daily OpenRouter budget spent); ひつまぶし awaits kana screening.

### 2026-10-04 (Routine v3: new-entries — 14 New Entries, IDs 31519–31532)

Fourteen words that older entries already used: 軍勢, 疼痛, 着水, 巡航, 配当金, 提供者, 銃弾, 論理学, 無礼者, 前年比,
使用済み, スペアタイヤ, 地方裁判所, 精白米. One new kanji (疼, kanji ID 02821). The linker connected them where they
were first seen, and the harvester added back-links in 18 neighbours. Self-check: clean (no issues on 32 entries); one
kana link checked and kept.
