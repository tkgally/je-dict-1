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

### 2026-11-04 (20 new entries, first cycle of the 00:15 run)

32761–32780. Closure: 南極線 (paired with 北極線), 環境庁, 昭和基地, 熟年離婚, 協議離婚, 離婚届, 噛み合わせる, 戦時下. Brainstorm (animal-mammal field): 肉牛, カモシカ, ジャガー, ジュゴン, ビーバー, レッサーパンダ. ezFurigana lookups: られる (passive, potential, honorific), 入り (〜入り; 客の入り), 般若心経 (shown as 心経 too), 極まりない, 急ピッチ, 規格外.
Self-check: clean (0 flags from the reviewer; 1 kana link kept, ころ in 子どものころ).

### 2026-11-03 (18 new entries, fifth cycle of the 12:15 run)

32743–32760. Closure: 疑義照会, 青票 (contrasted with 白票), 告知義務, 環境大臣, 国民宿舎, 就業者. Brainstorm: せる (causative after godan verbs, paired with させる), フェレット, ムササビ, モモンガ, ヒョウ, ヤマネコ. ezFurigana lookups: 寒色, 勘当, 雁 (new kanji 2838), 眼下, 忌引き, 急ブレーキ.
Self-check: 1 flag applied (待たせる can be permissive in context; WATCH OUT softened).

### 2026-11-03 (20 new entries, second cycle of the 12:15 run)

32723–32742. Closure: 申告書, 待ち受け画面, 参院, 衆院選, 最新型, 就業率, 他人任せ. Brainstorm: させる (causative auxiliary), 飛んで火に入る夏の虫, ハイエナ, ハリネズミ, ヒグマ, モグラ, サイ. ezFurigana lookups: 舵, 活動家, かなぐり捨てる, 〜かねない, 紙パック, 川面.
Self-check: 4 flags applied (2 on new entries: ハリネズミ do live wild in parts of Japan; 猫の写真 translation; 2 pre-existing in neighbours: 海抜 is not a synonym of 海面, 型落ち means superseded).

### 2026-11-03 (6 new entries, eighth cycle of the 05:50 run)

32717–32722. Closure: 国士無双 (peerless; the mahjong hand), 在外公館. Brainstorm (animal-mammal field): アルパカ, ツキノワグマ. ezFurigana lookups: 禍根, 頭文字.
Self-check: clean (0 accuracy flags, kana links confirmed).

### 2026-11-03 (12 new entries, fifth cycle of the 05:50 run)

32705–32716. Closure: 効能書き, サブタイトル, 落札者, 天下無双. Brainstorm (animal-mammal field): カワウソ (cross-referenced to ラッコ), セイウチ, チーター, ナマケモノ (contrasted with 怠け者). ezFurigana lookups: 思える (seem; can believe), 過言, 関わり, 勝ち組.
Self-check: 2 flags applied (サブタイトル can also mean film subtitles; 関わり is not a person tag).

