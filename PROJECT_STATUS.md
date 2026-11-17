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

### 2026-11-17 (22 candidates queued, fourth cycle of the 00:15 UTC run)

Closure 7 (no noentry markers remain; a scan of bare words in examples edited since 2026-11-10): 兵糧, 天女, 民主制, 拾い集める, 生活様式, 修了証書, 睨み合う. Brainstorm 15 (seeds 椅子…不味い, cursor 260–280): 九死に一生を得る, 一日おき, かかりつけ, 当月, 雨靴, ハイソックス, 長椅子, 襲いかかる, 通りかかる, 紙コップ, 紙皿, 声変わり, 心変わり, 綺麗事, 変わり. Of 181 proposals, 151 were already entries; 15 rejected.

### 2026-11-17 (20 new entries, second cycle of the 00:15 UTC run)

33657–33676. Closure: 取っ組む, 居合, 隔世の感, 和洋, こそばゆい, 目的格, 艘. Brainstorm: 二人連れ (seed 二人), 生暖かい (seed 暖かい), 霜月 (seed 十一月), マウンテンバイク (seed 自転車), 山の日, 終戦記念日 (seed 八月), たこ 'callus' (field body-part). ezFurigana: ポテンシャル, 前のめり, 膜, ボヤ, マイ〜, 幕内.
Self-check: 2 notes errors fixed (取っ組む's contrast with 取り組む; a false 幕の内弁当 etymology removed from 幕内); kana links clean. New kanji 艘 added to the kanji list. Candidates added: ロードバイク, 凧.

### 2026-11-16 (20 new entries, second cycle of the 16:15 UTC run)

33637–33656. Closure: 木戸孝允, 大阪万博, 芭蕉, 鳴門, 東証, 井原西鶴, 越後. Brainstorm: 暑苦しい (seed 暑い), 自転車置き場 (seed 自転車), 成人の日 (seed 一月), 隻 (seed 台), 鼻毛, 涙袋 (field body-part), モナリザ (field art). ezFurigana: 弁, 本書, 本島, 本邦, 奔流, ホームルーム. New kanji 允 (02871), 隻 (02872). Candidates 艘, 薩長同盟, 本稿 added.
Self-check: clean; kana links clean. 鳴門's fish-cake examples use ナルト, since the linker reads kana なると as なる + と.

### 2026-11-16 (15 new entries, fifth cycle of the 08:15 UTC run)

33622–33636. Closure: 極まる, 正気, 主格, 合板, 拘束力. Brainstorm: 鼻の下, 首根っこ, 胸毛 (field body-part), 文化の日 (seed 十一月), スポーツの日 (seed 十月). ezFurigana: 矛先, 骨太, 文節, 捕捉, ブレーン.
Self-check: 1 tag fix (33625 合板: tool removed); kana links clean. Candidate 目的格 added (seen in 33624).

### 2026-11-16 (15 new entries, seventh cycle of the 00:15 UTC run)

33607–33621. Closure: 肉眼, 花崗岩, 連合国, 豊洲, 真言宗. Brainstorm: 明るさ (seed 明るい), 二人きり, 二人暮らし, 二人三脚 (seed 二人), 紙飛行機 (seed 飛行機). ezFurigana: 北部, ホクホク, 勉学, ご指導ご鞭撻, 変調. New kanji 洲 (02868), 崗 (02869), 撻 (02870). Candidate 一人ぼっち dropped (entry 19525 独りぼっち is the same word).
Self-check: 1 tag fix (33610 豊洲: food removed); 1 kana link retargeted (33612: どんなに, not どんな).
