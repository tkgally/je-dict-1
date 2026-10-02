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

### 2026-10-02 (Routine v3: new-entries — 8 New Entries, IDs 31429–31436)

Eight words that older entries already used: アイスティー, レフェリー, 筏, 開場, 際どい, 弟子入り, 連邦, 紛らす.
One new kanji (筏, ID 02818). Self-check: clean.

### 2026-10-02 (Routine v3: new-entries — 12 New Entries, IDs 31417–31428)

Twelve words that older entries already used: 裏庭, 歴然, 箱入り娘, 伊勢海老, 角煮, 丸損, 女帝, 就職難, 泥試合, 点字,
偉業, 別状. No new kanji. Also fixed five example errors found by the audio checks (でははない in 安易, お願います,
使い過ぎ read しい, 屈しない read くしない, 決まり台詞 without rendaku). Self-check: one tag fix (伊勢海老 is not a fish).

### 2026-10-01 (Routine v3: new-entries — 20 New Entries, IDs 31397–31416)

Twenty more words that older entries already used: 見せかける, 預言, 量子, 脱兎, 大穴, 平和主義, 輸出入, へそくり, カプチーノ,
三毛猫, 世界史, 日本史, 二世帯, 吊り橋, 国歌, 日本刀, 村八分, 枯山水, 枝葉末節, 無益. No new kanji.
Self-check skipped: the day's OpenRouter budget was spent.

### 2026-10-01 (Routine v3: new-entries — 20 New Entries, IDs 31377–31396)

Twenty words that older entries already used: お母様, おばあさま, ふくよか, ファーストクラス, リチウム, 操り人形, ハイオク,
ワインセラー, たまり, 塗り箸, 低まる, 朽ち果てる, カウンセラー, アニメーション, ノンアルコール, 店子, 白昼夢, 耐火, 薄型, 化繊.
Self-check: one notes flag, rejected; the ファーストクラス gloss tightened to air travel.

### 2026-10-01 (Interactive: curator backlog cleared — 42 rulings, old URLs now redirect)

Tom worked through reviews/needs_curator.txt (439 lines). About 380 lines were stale: every semantic-tag
item (no entry carries an off-list tag), branch and PR notes, and flags later runs had already fixed. The
rest were ruled on and done. **Retiring entries is now possible**: `build/retire_entry.py` deletes or
renames an entry, repoints its links, and records the old id in `build/data/retired_entries.json`; the
site build writes a redirect page at the old URL. Retired: 格上 (かくじょう, invented), 車席, 解像, 罪犯, 紆余,
the combined 易しい／優しい, a second 礼拝堂, and one of each duplicate pair 幸せ, 気持ち, 若い, 向こう, 近く, 〜軒.
Readings corrected (URL renamed, old one redirects): 犬種 けんしゅ, 長財布 ながざいふ, 我 が (now "ego,
self-will"). かける, かかる and つける are now full nine-sense entries; 付ける covers only 付ける. 優しい and 易しい
are split. Senses added to 〜代, 形, 時, スマート, 馳せる, 末端, ポーチ, 半切り, 水切り; senses removed or merged
in 現す, 確かに, 訓読, 今日 (こんにち), 人事. Tags: new semantic tags `sense` and `place`, a `dialect` domain,
`existence` narrowed, grammar terms on `language`, question words on `grammatical`. Smaller fixes to about
twenty entries' examples and notes. Session log: polishing/sessions/curator_2026-10-01.md.
