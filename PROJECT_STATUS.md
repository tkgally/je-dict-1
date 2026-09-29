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

### 2026-09-29 (Routine v3: new-entries — 10 New Entries, IDs 31290–31299)

Ten words that older entries used inside stripped `noentry` markers: お古, どっちつかず, 大損, 出し合う, 勤め人, 印紙,
司法試験, 形容動詞, 語幹, 空豆. Reciprocal cross-references added on eleven neighbours (活用, 会社員, 弁護士, 中古, 損失,
サラリーマン, 曖昧, 中途半端, 語尾, 自営業, 枝豆). No new kanji. Kept to ten because the run clock was near its end.
Self-check skipped: the day's OpenRouter budget was spent.

### 2026-09-29 (Routine v3: new-entries — 15 New Entries, IDs 31275–31289)

Fifteen words that older entries used inside stripped `noentry` markers: テロ, ミュージカル, カップラーメン, 器用貧乏,
改憲, 空輸, 逆輸入, 遠洋, 米屋, 明晩, 活気づく, 追い求める, 無駄死に, 細心, 自費. Reciprocal cross-references added on
eight neighbours (八百屋, 輸送, 追求, 酒屋, 魚屋, 追いかける, 多才, 沖合). No new kanji. Self-check skipped: the day's
OpenRouter budget was spent.

### 2026-09-29 (Routine v3: new-entries — 10 New Entries, IDs 31265–31274)

Ten words that this day's earlier entries and notes named: 曽祖母, 曽孫, 県道, 有償, 訃報, 朗報, 潜める (with its pair
潜む now cross-linked), 巧遅, 期日, 合鍵. New kanji 訃 added to the kanji index. Kept to ten because the run clock
was near its end. Self-check skipped: the day's OpenRouter budget was spent.

### 2026-09-29 (Routine v3: new-entries — 20 New Entries, IDs 31245–31264)

Twenty internal-closure words that older entries already used: 頼み, 国道, 郵便番号, 曽祖父, 社会科, 副社長, 末裔,
随行, 回送, 方便, 無償, 満場, 埋蔵, 半期, 膝小僧, 暑中, 速力, レース (race; lace), マイル (mile; airline miles), 悲報.
Two old `noentry` markers for 暑中 (in 夏 and 見舞い) now link. New kanji 曽 and 裔 added to the kanji index. Six
words named in the new notes queued as candidates (曽祖母, 曽孫, 県道, 有償, 訃報, 朗報). Self-check skipped: the
day's OpenRouter budget was spent.

### 2026-09-29 (Routine v3: new-entries — 20 New Entries, IDs 31225–31244)

Twenty internal-closure words that older entries already used: 暮れる, 女の人, 割れ目, ほのか, じきに, ギャップ,
漁村, 秋祭り, 石橋, 編集部, 訳文, 福利, 従事者, 血中, 手縫い, 縫い付ける, 最敬礼, 競馬場, 大震災, 潜り抜ける.
Seventeen old `noentry` markers in fourteen entries now link to them. The newcomer check found no kana くれる link that
means 暮れる, but eight old くれる links were wrong (くん the name suffix, くれない "crimson") and were unlinked.
Self-check skipped: the day's OpenRouter budget was spent.

