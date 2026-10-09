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

### 2026-10-09 (Routine v3: new-entries — 20 New Entries, IDs 31785–31804)

Twenty internal-closure candidates that existing entries already use: 漁 (りょう; reading note for 漁業/漁師), 必要事項, 聴取 (two senses: official questioning; radio listening), 清潔感, 執る (WRITING vs 取る), 戦地 (vs 戦場), 外務大臣 (外相), 打球, 販路, 風合い (vs 手触り, 質感), 振り下ろす, 政治犯, 大はしゃぎ, 学び直す (学び直し), 後進 (WATCH OUT 後進国 dated), 松の内 (Jan 7 / Jan 15, 寒中見舞い), 本尊 (humorous ご本尊), 宮内庁 (proper noun; 御用達), 繰り越す, 腫れ. Self-check skipped (daily OpenRouter cap spent); one wrong link (指導にあたって → the grammar entry) unlinked by decision.

### 2026-10-09 (Routine v3: candidates — 25 internal-closure candidates, C24234–C24258)

A scan of example sentences for furigana-marked words with no entry and no link found 25 real words the dictionary already uses but has not defined, each with its source entry: 懐石料理, 過去最高, 点差, 山間部, 互換, 薄手, 大軍, 華族, 商家, 来航, 汁粉, 遍路, 私腹を肥やす, 白物家電, 知的財産権, 最大公約数, 日経平均, 不要不急, 首脳会談, 日本列島, and the proper nouns 第二次世界大戦, 国会議事堂, 屋久島, 日本国憲法, 本能寺の変. Variant spellings of existing entries (怪我, 入口, 人混み, 綺麗, 名字, …), free compounds (〜後, 〜中, 技術力, 生産量) and seven existing idioms were dropped. The noentry-marker source is empty. Queue: 80 → 105.

### 2026-10-09 (Routine v3: new-entries — 10 New Entries, IDs 31775–31784)

Ten internal-closure candidates that existing entries already use: 聞き入る (used in 22792, 25882, 27922, though not in its listed source 04586), そびえ立つ (ASPECT note), 寝込む (two senses: laid up in bed; fall fast asleep), 積み重ね (two senses), 過ぎ去る, 窯元, 冬場 (with 冬季), 歩数 (counter 歩), 心拍数 (with 脈拍), 金箔 (new kanji 箔 added to the kanji index; WATCH OUT 緊迫). Conjugation tables added for the four verbs. Source entries relinked (10 new inline links). No stale markers or newcomer link ambiguities. Self-check: no issues on the 28 new and touched entries; one on a relinked entry (22792 耳を聞き澄ます, ungrammatical, example replaced). One kana link checked and kept.

### 2026-10-08 (Routine v3: new-entries — 11 New Entries, IDs 31764–31774)

Eleven internal-closure candidates that existing entries already use: 一手 (two senses: a move in shogi or go; 一手に "single-handedly"), 神前 (contrasted with 仏前), 岩壁 (WATCH OUT 岸壁), 家中 (two senses; かちゅう noted), 米作り (with 稲作), 常任理事国, 川幅 (related 道幅, 肩幅), 日常生活, 保守派 (〜派 words), にじみ出る (two senses; ichidan, table added), 無病息災 (四字熟語). 聞き入る was skipped: its source, 04586, uses 聞き入れる, so the candidate came from a tokenizer misreading. The source entries were relinked (10 new links to the new entries). No new kanji; no stale markers or newcomer link ambiguities. Self-check skipped: the day's OpenRouter cap was spent.

### 2026-10-08 (Routine v3: new-entries — 16 New Entries, IDs 31748–31763)

Sixteen internal-closure candidates that existing entries already use: 弄する and 課する (する verbs; 課する contrasted with 科する), 転ずる (ずる verb, cross-referenced with 転じる), 射る and 捕らえる (ichidan; 捕らえる contrasted with 捉える and 捕まえる), 帰還 and 被爆 (noun + する; 被爆 contrasted with 被曝), 生理 (two senses), 称号, 陽性, 一節, 文系, 鮎 (new kanji, added to the kanji index), 赤み, 急ぎ, 宗教的 (na-adjective). Conjugation tables added for the six verbs. The source entries were relinked (21 new inline links); one, 転じた in 29845, was retargeted from the new 転ずる to 転じる. The newcomer check listed 6,209 kana いる links now sharing a reading with 射る; none means 射る, so none moved. Self-check skipped: the day's OpenRouter cap was spent.

