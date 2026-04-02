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

### 2026-04-02 (Vocabulary Expansion - 20 New Entries, Session 570)
Added 20 new dictionary entries (IDs 21451-21470) from candidate_words.json. A diverse mix of verbs, adjectives, adverbs, expressions, and nouns useful for intermediate learners.

- **Suru verbs (5)**: {感心|かんしん}する (to be impressed), {徹底|てってい}する (to be thorough), {干渉|かんしょう}する (to interfere), しっかりする (to be steady/firm), ぽかんとする (to look blank)
- **I-adjectives (2)**: {憎|にく}たらしい (detestable), {腹立|はらだ}たしい (infuriating)
- **Godan verb (1)**: {上|のぼ}る (to go up/amount to)
- **Adverb (1)**: みるみる (rapidly, before one's eyes)
- **Na-adjective (2)**: わんぱくな (naughty/mischievous), {平均的|へいきんてき}な (average/typical)
- **Expressions (2)**: ため{息|いき}をつく (to sigh), {肩|かた}を{落|お}とす (to be dejected)
- **Nouns (5)**: ファイト (fighting spirit/go for it!), {混入|こんにゅう} (contamination), {平均点|へいきんてん} (average score), {最大級|さいだいきゅう} (largest-class), {宣伝文句|せんでんもんく} (advertising slogan)
- **Loanwords (2)**: トレーナー (sweatshirt/trainer), アウター (outerwear)
- Removed 11 stale candidates (suru-verb duplicates of existing noun+verb-suru entries)
- Removed 19 candidates that now exist as entries

### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 569)
Added 30 new dictionary entries (IDs 21421-21450) from candidate_words.json. A diverse mix of vocabulary covering verbs, nouns, adjectives, and adverbs useful for intermediate learners.

- **Suru verbs (8)**: {中継|ちゅうけい}する (to relay/broadcast), {墜落|ついらく}する (to crash), {活用|かつよう}する (to utilize), {同行|どうこう}する (to accompany), {失墜|しっつい} (loss of reputation), {悲嘆|ひたん} (grief), {在籍|ざいせき} (enrollment), {成功|せいこう}する (to succeed)
- **Ichidan verb (1)**: {特徴|とくちょう}づける (to characterize)
- **Suru verb nouns (2)**: {夢想|むそう} (daydream), {失墜|しっつい} (loss of reputation)
- **Na-adjective (2)**: {荘厳|そうごん}な (majestic), {無秩序|むちつじょ} (disorder/chaos)
- **I-adjective (1)**: {慈悲深|じひぶか}い (compassionate)
- **Adverbs (2)**: {楽々|らくらく} (easily), ちらりと (briefly/at a glance)
- **Nouns (14)**: {泡沫|ほうまつ} (foam/ephemeral), {内緒話|ないしょばなし} (secret talk), {盗|ぬす}み{聞|ぎ}き (eavesdropping), {流|なが}し{読|よ}み (skimming), ご{褒美|ほうび} (reward), {決|き}まり{文句|もんく} (set phrase), {楽勝|らくしょう} (easy victory), {高級品|こうきゅうひん} (luxury goods), {交流会|こうりゅうかい} (exchange meeting), {略|りゃく} (abbreviation), {養父母|ようふぼ} (adoptive parents), {四国|しこく} (Shikoku), {恒常性|こうじょうせい} (homeostasis), {超高層|ちょうこうそう}ビル (skyscraper), {骨密度|こつみつど} (bone density)
- Added 1 new kanji to index: 沫
- Removed 30 candidates that now exist as entries





---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
