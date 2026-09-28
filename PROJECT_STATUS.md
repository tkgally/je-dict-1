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

### 2026-09-26 (Routine v3: new-entries — 3 New Entries, IDs 31074–31076)

A short end-of-run cycle. 柴刈り (gathering brushwood, the Momotarō しばかり), the one internal-closure
candidate, added after the 芝刈り polish; 無印良品 and 朝日新聞 from the curated proper-noun queue. Two old
`noentry` markers (01639 新聞社, 03990 無地) now link to them. Self-check clean. Candidate queue stands at 113.

### 2026-09-26 (Routine v3: new-entries — 20 New Entries, IDs 31054–31073)

Five internal-closure words that earlier entries mentioned without defining: 立ち飲み, 既成,
滑り込み, 申し送る, 濡れ衣. Fifteen proper nouns and cultural terms from the curated queue:
the classics 竹取物語, 平家物語, 徒然草, 方丈記, 奥の細道, 忠臣蔵; the historical figures 源頼朝,
武田信玄, 上杉謙信, 千利休, 世阿弥, 渋沢栄一; 道頓堀, 祇園祭, and 大河ドラマ. Five old `noentry`
markers in four entries (03735 祭り, 04314 随筆, 04455, 04768) now link to the new entries.
Self-check: 3 flags, 1 applied, 2 rejected. Candidate queue stands at 115.

### 2026-09-25 (Interactive: recorded audio for example sentences)

Example sentences can now carry recorded readings. Each MP3 is made by Gemini TTS and is
accepted only when four AI checkers from three companies agree it follows the furigana; a failed
take is regenerated up to five times. The recordings live in a separate repository,
`tkgally/je-dict-audio-1`, served by GitHub Pages, so no audio enters this repository. On
an entry page, an example with a valid recording gets a play button for the MP3. The recording
counts as valid while the example's text and furigana are unchanged; every other example keeps
the browser-speech button.

**First recordings: 308 examples from the first 33 basic-tier entries** (00006 ある to 00422 を),
voices Kore and Charon, $0.76. 292 passed on the first take. The batch also found a furigana
error, 00111 本 {少|すこ}なくとも → すく, which is now fixed.

**Then 800 more** (00426 読む to 00560 口), after Tom chose four voices (Kore, Charon, Erinome,
Iapetus), 32 kbps, and a budget of $4.80 per audio run within a $7.50 daily cap: all 800
accepted, 761 on the first take, $1.94. 1,108 examples now have recordings.

**The Routine has a new `audio` mode (a quarter of runs, $4.80 each).** It works through
stale recordings first, then the basic, core and general tiers. It runs maintenance checks
before recording: a regression suite of 163 clips with known answers, voice pilots, model
checks, and monthly spot-check pages for Tom. Examples with digits, Latin letters or symbols
(about 2,500), or with kanji lacking furigana (90), are skipped for now. Workflow, evidence and
changelog: `AUDIO_WORKFLOW.md`.

