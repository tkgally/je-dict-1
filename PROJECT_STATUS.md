# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-10-26
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

### 2026-11-22 (candidates: 30 added, seventh cycle of the 00:15 UTC run)

Brainstorm only (no closure markers or noted words were waiting; no ezFurigana rows pending). Field communication: 手話, 歓談, 誤訳, 念を押す, 言いふらす, 話が弾む, 釘を刺す. Seeds 00783–00805: インスタントコーヒー, ブラックコーヒー, 缶コーヒー, エスプレッソ (コーヒー), おじちゃん, おじさま, おばさま, お腹が空く, お腹を壊す, 薄汚い, 音楽室, 口が重い, 悲しげ, 答え合わせ, 長風呂. Field consumption: がぶ飲み, 食べ残し, 食べ残す, お冷, 断食, 飲ん兵衛, 食べかけ, 飲みかけ. Most proposals (334 of 383) were already entries. 15 rejected (spellings of existing entries, a derived form, a transparent compound). Model spend about $0.22.

### 2026-11-22 (20 new entries, first cycle of the 00:15 UTC run)

33900–33919. Closure: 平賀源内, 長針, 短針, 背番号, 気付け (named in the last run's entries). Brainstorm: 手広い (related to 広い), 添え状 (手紙), 被り物 (帽子), 門扉 (field building), 社内報, 御用納め, 寿退社 (field business), サスペンダー, キャミソール, ショートパンツ, パンプス, スパッツ, ローファー, 丸首, 半纏 (field clothing). No ezFurigana candidates were queued. No new kanji. 4 candidates added (永久欠番, 御用始め, エレキテル, クルーネック).
Self-check: 3 flags from gpt-6.1-sol, all applied (送り状 can mean a covering note; 御用納め date not fixed by law; スパッツ 'never gaiters' softened); 9 kana links judged, 0 flagged.

### 2026-11-21 (18 new entries, fifth cycle of the 12:15 UTC run)

33882–33899. Closure: 綿菓子, 発火点, 引火, 宮崎駿 (named in the first cycle's entries). Brainstorm: 土用の丑の日 (related to 七月), 駄目押し (だめ), ニット帽 (帽子), 文字盤 (時計), 社員旅行 (field business), ペイペイ (field brand-name), 毛玉, 裾上げ, ほつれる, 腹巻き, ユニフォーム, ジャージ, 短パン, 着付け (field clothing). No ezFurigana candidates were queued. New kanji 駿 (02879). 5 candidates added (平賀源内, 長針, 短針, 背番号, 気付け).
Self-check: 2 flags from gpt-6.1-sol, both applied (短パン etymology; 発火点 note softened); 21 kana links judged, 0 flagged.

### 2026-11-21 (20 new entries, first cycle of the 12:15 UTC run)

33862–33881. Closure: わけではない, 基軸, キロワット, アンペア, 消費電力, ライフワーク, 橋梁, 引火点 (石榴 dropped: a spelling of the existing 柘榴). Brainstorm: アマゾン, ディズニー (field brand-name), 渡り廊下, 縁の下, 間仕切り (field building), 〜巻 (related to 〜冊), 卯月 (四月), 海の日 (七月), 綿飴 (飴), 一番乗り (一). ezFurigana: トトロ, れる. New kanji 卯 (02878). 4 candidates added (綿菓子, 発火点, 引火, 宮崎駿).
Self-check: 1 flag from gpt-6.1-sol (アマゾン explanation), applied; 1 link unlinked (縁 'fate' where the note means the veranda).

### 2026-11-21 (20 new entries, third cycle of the 00:15 UTC run)

33842–33861. Closure: 隠し撮り, 烙印, 袖の下, 御霊, 枢軸, 頭字語, 点鼻薬, 榴弾. Brainstorm: 北国 (compound of 北), 梁, スロープ, フロア, プレハブ, ユニットバス (field building). ezFurigana: ライフ, 歴訪, 連綿, わけがない, ワット, リーチ. New kanji 烙 (02877). 8 candidates added from the new notes (わけではない, 基軸, キロワット, …).
Self-check: 3 flags from gpt-6.1-sol on 隠し撮り and 御霊, all applied; 1 kana link unlinked (ことがある in そんなことがあるわけがない).
