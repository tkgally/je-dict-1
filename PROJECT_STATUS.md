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

### 2026-11-04 (candidate restock, first cycle of the 12:15 run)

70 candidates queued (C25668–C25737), queue 479 → 549. Closure (13, from a tokenizer scan of example sentences for words with no entry): 天皇陛下, 両論併記, 腸内細菌, 素因, 立憲主義, 〜周忌, カツオのたたき, 子々孫々, 待ち焦がれる, 脱原発, 来季, 修行僧, 革命家. Brainstorm (appearance field, 57): えくぼ, 丸顔, 面長, 童顔, 垂れ目, 切れ長, くせ毛, 枝毛, 坊主頭, 二重あご, 無精ひげ, アイシャドウ, つけまつげ, イメチェン, 様になる, 見違える and others.

### 2026-11-04 (6 new entries, seventh cycle of the 00:15 run)

32801–32806. Closure: 直角三角形, 東側 (also the Cold War East), 火口湖. Brainstorm: シロナガスクジラ. ezFurigana lookups: 教皇 (with the 2019 switch from 法王), 教祖.
Self-check: clean (0 flags on 12 entries, 4 kana links confirmed).

### 2026-11-04 (20 new entries, fourth cycle of the 00:15 run)

32781–32800. Closure: ヒキガエル, 文化系 and 体育会系 (paired as antonyms), ガチャ, 湯取り法, 苦言, 思考回路, 感謝祭. Brainstorm (animal-mammal field): ロバ, アルマジロ, バイソン, シロクマ, カピバラ, シマリス. ezFurigana lookups: 甲 (party A; shell; back of the hand), 主 (main; the Lord), イエス, 関連付け, 貴公子, 肝いり.
Self-check: clean (0 flags on the 20 new entries and 10 neighbours that gained cross-references).

### 2026-11-04 (20 new entries, first cycle of the 00:15 run)

32761–32780. Closure: 南極線 (paired with 北極線), 環境庁, 昭和基地, 熟年離婚, 協議離婚, 離婚届, 噛み合わせる, 戦時下. Brainstorm (animal-mammal field): 肉牛, カモシカ, ジャガー, ジュゴン, ビーバー, レッサーパンダ. ezFurigana lookups: られる (passive, potential, honorific), 入り (〜入り; 客の入り), 般若心経 (shown as 心経 too), 極まりない, 急ピッチ, 規格外.
Self-check: clean (0 flags from the reviewer; 1 kana link kept, ころ in 子どものころ).

### 2026-11-03 (18 new entries, fifth cycle of the 12:15 run)

32743–32760. Closure: 疑義照会, 青票 (contrasted with 白票), 告知義務, 環境大臣, 国民宿舎, 就業者. Brainstorm: せる (causative after godan verbs, paired with させる), フェレット, ムササビ, モモンガ, ヒョウ, ヤマネコ. ezFurigana lookups: 寒色, 勘当, 雁 (new kanji 2838), 眼下, 忌引き, 急ブレーキ.
Self-check: 1 flag applied (待たせる can be permissive in context; WATCH OUT softened).

