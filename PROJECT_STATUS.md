# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-31
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
| Total entries | ~19,088 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,289 (open) |
| Candidate words | ~5,472 |
| Cross-references | ~3,400 |
| Example sentences | ~53,200 |
| Audio files | 1,028 |

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

### 2026-04-02 (Vocabulary Expansion - 20 New Entries, Session 577)
Added 20 new dictionary entries (IDs 21627-21646) from candidate_words.json. A thematic set focused on emotions, states of mind, and expressive vocabulary useful for intermediate learners.

- **Onomatopoeia/suru verbs (6)**: ドキドキする (nervous/excited), ふらふらする (dizzy/wander), おどおどする (timid), びくびくする (apprehensive), うっとりする (entranced), {敬服|けいふく}する (to admire deeply)
- **Ichidan verbs (2)**: うろたえる (to be flustered), {巻|ま}き{込|こ}まれる (to be caught up in)
- **Godan verb (1)**: {立|た}ち{会|あ}う (to be present at)
- **Na-adjectives (2)**: {穏健|おんけん} (moderate), {重篤|じゅうとく} (critical/grave)
- **I-adjective (1)**: {別|わか}れ{惜|お}しい (reluctant to part)
- **Nouns (2)**: {本格|ほんかく} (full-scale/authentic), {原油|げんゆ} (crude oil), {拒否|きょひ}{反応|はんのう} (rejection reaction)
- **Adverb (1)**: {粛然|しゅくぜん} (solemnly)
- **Expressions (3)**: ひょっとしたら (perhaps), {涼|すず}しい{顔|かお} (nonchalant look), {肝|きも}を{冷|ひ}やす (to be terrified), {先|さき}を{越|こ}される (to be beaten to it)

### 2026-04-02 (Vocabulary Expansion - 25 New Entries, Session 576)
Added 25 new dictionary entries (IDs 21602-21626) from candidate_words.json. A practical mix of everyday vocabulary covering transportation, communication, health, education, nature, food, and time expressions.

- **Suru verbs (8)**: {挑戦|ちょうせん}する (to challenge), {感動|かんどう}する (to be moved), {転居|てんきょ}する (to move residence), {服用|ふくよう}する (to take medicine), {復学|ふくがく} (returning to school), {転送|てんそう}する (to forward), {散布|さんぷ}する (to spray), {複写|ふくしゃ}する (to copy)
- **Godan verbs (2)**: {乗|の}り{越|こ}す (to ride past one's stop), {炊|た}き{上|あ}がる (to finish cooking rice)
- **Ichidan verb (1)**: {言|い}いつける (to tell on; to order)
- **Nouns (10)**: {客室|きゃくしつ} (guest room/cabin), {人気|にんき}{商品|しょうひん} (popular product), {普通|ふつう}{列車|れっしゃ} (local train), {乗務員|じょうむいん} (crew member), {航空|こうくう}{会社|がいしゃ} (airline), {山歩|やまある}き (mountain walking), {数週間|すうしゅうかん} (several weeks), {数時間|すうじかん} (several hours), {数分|すうふん} (several minutes), {白銀|はくぎん} (silver/snowy world)
- **Na-adjective (1)**: {鋭利|えいり}な (sharp)
- **Other nouns (3)**: {参拝者|さんぱいしゃ} (shrine visitor), {才人|さいじん} (talented person), {突然|とつぜん}に (suddenly)

### 2026-04-02 (Vocabulary Expansion - 31 New Entries, Session 575)
Added 31 new dictionary entries (IDs 21571-21601) from candidate_words.json. A diverse mix of practical vocabulary for intermediate learners covering law, food, culture, travel, work, and daily life.

- **Godan verb (1)**: {踏|ふ}み{荒|あ}らす (to trample)
- **Suru verbs (2)**: {哀願|あいがん}する (to plead), {改新|かいしん} (reform)
- **Na-adjectives (2)**: {大仰|おおぎょう} (exaggerated), {直截|ちょくさい} (direct/blunt)
- **Noun/verb-suru (6)**: {転任|てんにん} (transfer), {断交|だんこう} (severing relations), {膳立|ぜんだ}て (preparation), {下船|げせん} (disembarkation), {嘆願|たんがん} (petition), {贈賄|ぞうわい} (bribery)
- **Nouns (20)**: {賄賂|わいろ} (bribe), {雪|ゆき}かき (snow shoveling), {替|か}え{歌|うた} (parody song), {途切|とぎ}れ (interruption), {呼|よ}び{鈴|りん} (doorbell), {置|お}き{引|び}き (theft of unattended items), シロップ (syrup), {走者|そうしゃ} (runner), {橙色|だいだいいろ} (orange color), {城壁|じょうへき} (castle wall), {進度|しんど} (rate of progress), パセリ (parsley), {精神科|せいしんか} (psychiatry), お{母|かあ}ちゃん (mom), {宅地|たくち} (residential land), {密偵|みってい} (spy), {仕入|しい}れ{値|ね} (wholesale cost), ジャスミン{茶|ちゃ} (jasmine tea), {振込|ふりこみ}{手数料|てすうりょう} (bank transfer fee), {座|すわ}り{方|かた} (way of sitting)
- Added 3 new kanji to index: 截, 膳, 賂
- Removed 31 candidates that now exist as entries; removed 1 stale candidate (働き甲斐, duplicate of 働きがい)

### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 574)
Added 30 new dictionary entries (IDs 21541-21570) from candidate_words.json. A diverse mix of common, useful vocabulary for intermediate learners.

- **Na-adjectives (2)**: {肝心|かんじん} (essential/crucial), {逆説的|ぎゃくせつてき} (paradoxical)
- **Godan verb (1)**: ほったらかす (to neglect/leave alone)
- **Ichidan verb (1)**: {元気|げんき}づける (to cheer up/encourage)
- **Expression (1)**: {歯|は}を{食|く}いしばる (to clench one's teeth/endure)
- **Noun/verb-suru (7)**: {降下|こうか} (descent), {扶養|ふよう} (support/dependents), {消臭|しょうしゅう} (deodorizing), {精製|せいせい} (refining), {独習|どくしゅう} (self-study), {着服|ちゃくふく} (embezzlement), {間引|まび}き (thinning/reducing service)
- **Nouns (18)**: {赤信号|あかしんごう} (red light), {青信号|あおしんごう} (green light), {口当|くちあ}たり (mouthfeel), {名産|めいさん} (local specialty), {勤|つと}め{先|さき} (workplace), {義務感|ぎむかん} (sense of duty), {全貌|ぜんぼう} (full picture), {大局|たいきょく} (big picture), {新語|しんご} (neologism), {命題|めいだい} (proposition), {賞品|しょうひん} (prize), {安定性|あんていせい} (stability), あがり{症|しょう} (stage fright), {区役所|くやくしょ} (ward office), {花鳥風月|かちょうふうげつ} (beauties of nature), {抗菌|こうきん} (antibacterial), {水位|すいい} (water level), {口伝|くちづた}え (word of mouth)
- Removed 30 candidates that now exist as entries

### 2026-04-02 (Vocabulary Expansion - 19 New Entries, Session 573)
Added 19 new dictionary entries (IDs 21521-21540) from candidate_words.json. A mix of everyday words, verbs, nouns, and expressions useful for intermediate learners.

- **Expressions (2)**: ちょうどいい (just right), {気|き}に{障|さわ}る (to offend/annoy)
- **Godan verbs (4)**: {恥|は}じらう (to be bashful), {悔|くや}しがる (to show frustration), {行|い}き{着|つ}く (to end up at), ふやかす (to soak and soften)
- **Ichidan verb (1)**: もつれる (to become tangled)
- **Nouns (11)**: ありさま (state/condition), {満腹感|まんぷくかん} (feeling full), {先々月|せんせんげつ} (month before last), {共用|きょうよう} (shared use), {使者|ししゃ} (messenger), {圧迫感|あっぱくかん} (feeling of pressure), {胸|むね}の{内|うち} (inner thoughts), {高低|こうてい} (high and low), {中心街|ちゅうしんがい} (city center), {補色|ほしょく} (complementary color), {図柄|ずがら} (design/pattern)
- **Na-adjective/noun (1)**: {過干渉|かかんしょう} (overinvolvement)
- Removed 19 candidates that now exist as entries






---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
