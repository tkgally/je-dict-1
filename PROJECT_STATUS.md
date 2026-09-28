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

### 2026-09-28 (Routine v3: new-entries — 20 New Entries, IDs 31135–31154)

All twenty are internal-closure words from the restock earlier today, each one already used by older entries:
連体詞, 期する, 厚生, 一次, 二次, 胴, 無機, 借主, 遺志, 対称, 転じる, 与る, 辞する, かしこまる, ケースバイケース,
民主的, 北緯, and the proper nouns 東京都, 姫路城, 東日本大震災. 47 old `noentry` markers in 30 entries now link to
them. Self-check skipped (daily review budget spent). Candidate queue stands at 113.

### 2026-09-28 (Routine v3: candidates — 61 words queued, C23538–C23598)

Internal-closure restock from `check_stale_noentry.py`'s unresolved class: every word is one an existing entry
already uses but the dictionary does not define (期する, 連体詞, 厚生, 一次/二次, 胴, 無機, 借主, 遺志, 対称, 転じる,
与る, 辞する, かしこまる, ピンとくる, ケースバイケース, ゴールイン …), plus places and events those entries name
(東京都, 山梨県, 伊豆, 知床, 姫路城, 大阪城, 歌舞伎座, 東日本大震災, 文部科学省). Affixes, number+counter strings and
variant spellings of existing entries (湯呑み, 箸置き, 売上, 和歌山県 …) were skipped. Queue: 72 → 133.

### 2026-09-28 (Routine v3: new-entries — 20 New Entries, IDs 31115–31134)

One internal-closure word, 言い過ぎ (found in 08680 誇張, whose SIMILAR WORDS bullet now links to it). The
queue had no other "seen in entry" words, so the rest came from the vetted proper-noun stream: people 村上春樹,
黒澤明, 空海, 宮本武蔵, 西郷隆盛, 伊藤博文; organizations and brands トヨタ, ソニー, ユニクロ, 早稲田, 慶応, ジブリ;
works ドラえもん, サザエさん, ポケモン; places 高野山, 吉祥寺, 難波, 梅田. Old `noentry` markers for 高野山 (02168)
and 早稲田 (03221) now link. New kanji 澤 added to the index. Self-check: clean. Candidate queue stands at 72.

### 2026-09-28 (Routine v3: new-entries — 22 New Entries, IDs 31093–31114)

Three internal-closure words first: 窺う (to peer at, to gauge — distinct from humble 伺う; 03714's 様子を窺った
now links to it), そうする, 独楽回し. Then from the vetted queue: 厚生年金, 食品ロス, 上棟式, 竣工式, 施主, 感謝状,
丹精; four-character idioms 温故知新, 一挙両得, 十中八九, 千載一遇; idioms 目が高い, 頭が下がる, 気が置けない,
水に流す, 馬が合う, 雀の涙, 音を上げる, 棚に上げる. New kanji 窺 added to the index. 04764's old 一挙両得
`noentry` marker now links. Self-check: one reviewer flag rejected, one gloss fixed. Candidate queue stands at 91.

### 2026-09-27 (Routine v3: new-entries — 16 New Entries, IDs 31077–31092)

All sixteen are internal-closure words that polish runs found used but undefined: the sports terms
先制, 決勝点, 追加点, 四球; 聞き違い, 言い間違える, 燃え尽きる, 文字起こし, 明朝; and workplace words
介護離職, 産業医, 長時間労働, 追い出し部屋, 業務委託, 正規雇用, 組替え. 下茹で was dropped from the queue as a
duplicate of 下ゆで. Harvest added reciprocal cross-references on 22 neighbouring entries. Self-check: one
flag on a neighbour, rejected. Candidate queue stands at 113.

