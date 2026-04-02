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

### 2026-04-02 (Vocabulary Expansion - 20 New Entries, Session 572)
Added 20 new dictionary entries (IDs 21501-21520) from candidate_words.json. A mix of literary, formal, and cultural vocabulary.

- **Nouns (17)**: {邂逅|かいこう} (chance meeting), {寸分|すんぶん} (a tiny bit), {夜涼|よすず}み (evening cool), {融点|ゆうてん} (melting point), {前文|ぜんぶん} (preamble), あとがき (afterword), {試料|しりょう} (sample), {懇親|こんしん} (friendly relations), {虚実|きょじつ} (truth and falsehood), {名店|めいてん} (famous shop), {旧家|きゅうか} (old family), {本年|ほんねん} (this year), {離別|りべつ} (separation), {死活|しかつ} (life and death), ルビ (ruby text), {季節風|きせつふう} (seasonal wind), {大|おお}ぼら (tall tale), {虚言|きょげん} (lie)
- **Na-adjective (1)**: {陰鬱|いんうつ} (gloomy)
- **Adverb (1)**: {露|あらわ}に (openly)
- Added 2 new kanji to index: 邂, 逅
- Removed 19 candidates that now exist as entries

### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 571)
Added 30 new dictionary entries (IDs 21471-21500) from candidate_words.json. A diverse mix of verbs, expressions, adjectives, adverbs, onomatopoeia, and nouns useful for intermediate learners.

- **Expressions (2)**: {口|くち}にする (to say/to eat), {目|め}にする (to come across)
- **Godan verbs (4)**: {飲|の}み{干|ほ}す (to drain a drink), {言|い}い{合|あ}う (to argue/exchange words), {受|う}け{渡|わた}す (to hand over), ふらつく (to stagger/wander)
- **Ichidan verbs (3)**: {振|ふ}りかける (to sprinkle), かき{消|き}える (to vanish), よろける (to stumble)
- **Suru verb (1)**: {没|ぼっ}する (to sink/die/be absorbed)
- **Noun/verb-suru (6)**: {助成|じょせい} (subsidy), {敢行|かんこう} (bold execution), {敬服|けいふく} (deep admiration), {離反|りはん} (defection), {見聞|みき}き (things seen and heard), {散乱|さんらん} (scattering)
- **Adjectives (5)**: {清楚|せいそ} (neat and pure), あっぱれ (splendid), {朧|おぼろ}げ (faint/vague), {自在|じざい} (free/flexible), あったかい (warm, colloquial)
- **Adverbs (2)**: やみくもに (blindly/recklessly), ぜいぜい (wheezing)
- **Onomatopoeia (1)**: へなへな (weak/flimsy)
- **Nouns (4)**: ほっぺた (cheek), {熱戦|ねっせん} (fierce match), {絶|た}え{間|ま} (pause/gap), {高潮|こうちょう} (climax)
- **Other (2)**: こういう (this kind of), はいはい (yes yes/baby crawling)
- Removed 57 stale candidates (suru-verb duplicates, wrong readings, entries already existing)





---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
