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

### 2026-10-05 (Routine v3: new-entries — 5 New Entries, IDs 31605–31609)

A short last cycle (started at 112 min): five internal-closure nouns that existing examples already use, 今季, 強豪,
満足度, 両社, 冷戦. No new kanji; no stale markers or newcomer link ambiguities. Self-check skipped (the day's OpenRouter
allowance was spent). 33 internal-closure candidates remain.

### 2026-10-05 (Routine v3: candidates — 31 internal-closure candidates, C24002–C24032)

The noentry-marker source is empty since the markers were retired, so this run scanned the unlinked text of every example
with SudachiPy for content-word lemmas that have no entry, excluding each entry's own headword. Queued 31 words that 2 to 24
examples already use: 今季, 強豪, 満足度, 両社, 賛否両論, 冷戦, 取り調べ, 講習, 臭み, 乗り上げる, 尋問, 国際法, 損害賠償, 和平,
水性, 株主総会, 航行, 選挙戦, 細める, 雪道, 拡充, 忠臣, 飛び交う, 両家, 定食屋, 満塁, 通気性, 浴びせる, 先立つ, 党内, 絶つ.
Variant spellings of existing entries (子ども, 気づく, 引っ越し, 玉ねぎ, 人混み …) were dropped. Queue: 84.

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

