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

### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 568)
Added 30 new dictionary entries (IDs 21391-21420) from candidate_words.json. A diverse mix of practical vocabulary covering verbs, expressions, nouns, and adjectives useful for intermediate learners.

- **Suru verbs (5)**: {加速|かそく}する (to accelerate), {下車|げしゃ}する (to alight), {反省|はんせい}する (to reflect/feel remorse), {組織化|そしきか} (systematization), {充足|じゅうそく} (sufficiency)
- **Godan verbs (2)**: {込|こ}み{合|あ}う (to be crowded), {連|つ}れ{去|さ}る (to take away forcibly)
- **Expressions (4)**: {声|こえ}を{出|だ}す (to speak up), {手|て}をつく (to place hands on ground), {息|いき}を{止|と}める (to hold one's breath), {申|もう}し{訳|わけ}ありません (I'm very sorry)
- **Nouns (13)**: {朝方|あさがた} (early morning), {引|ひ}っ{張|ぱ}りだこ (in great demand), {辛|から}さ (spiciness), {数十|すうじゅう} (several tens), {自家用|じかよう} (private use), {新学年|しんがくねん} (new school year), モラル (morals), {東南|とうなん} (southeast), {孤立感|こりつかん} (feeling of isolation), {大盤振|おおばんぶ}る{舞|ま}い (lavish spending), お{得意様|とくいさま} (valued customer), {度量|どりょう} (magnanimity), {解析力|かいせきりょく} (analytical ability)
- **Counter/noun (1)**: {一着|いっちゃく} (first place/one suit)
- **Na-adjective (1)**: {不自然|ふしぜん}な (unnatural)
- **Other nouns (4)**: {零点|れいてん} (zero points), {混合物|こんごうぶつ} (mixture), {拘留|こうりゅう} (detention), {感覚神経|かんかくしんけい} (sensory nerve)

### 2026-04-02 (Vocabulary Expansion - 17 New Entries, Session 567)
Added 17 new dictionary entries (IDs 21374-21390) from candidate_words.json. Focused on practical verbs and expressions useful for intermediate learners.

- **Suru verbs (10)**: {加速|かそく} (to accelerate), {公表|こうひょう} (to announce publicly), {依頼|いらい} (to request), {対面|たいめん} (to meet face-to-face), {白状|はくじょう} (to confess), {仲介|ちゅうかい} (to mediate), {流入|りゅうにゅう} (to flow in), {追及|ついきゅう} (to press for answers), {詰問|きつもん} (to interrogate), {出力|しゅつりょく} (to output), {習熟|しゅうじゅく} (to become proficient), {注文|ちゅうもん} (to order)
- **Godan verbs (3)**: {沸|わ}き{立|た}つ (to boil up/surge), {連|つ}れ{込|こ}む (to bring someone in), {誘|さそ}い{出|だ}す (to lure out)
- **Ichidan verb (1)**: {見下|みさ}げる (to look down on)
- **Expression (1)**: {後|あと}を{追|お}う (to follow after)
- Removed 1 stale candidate (軽視する — already existed as entry 18776)
- Removed 5 candidates that now exist as entries


### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 565)
Added 30 new dictionary entries (IDs 21314-21343) from candidate_words.json. A practical mix of common verbs, adjectives, nouns, and expressions useful for intermediate learners.

- **Suru verbs (12)**: {駆除|くじょ} (extermination), {分解|ぶんかい} (disassembly/decomposition), {撤去|てっきょ} (removal), {返金|へんきん} (refund), {返却|へんきゃく} (returning), {解消|かいしょう} (resolution), {停車|ていしゃ} (stopping), {回復|かいふく} (recovery), {拒否|きょひ} (refusal), {容認|ようにん} (tolerance), {離婚|りこん} (divorce), {湯煎|ゆせん} (water bath)
- **Na-adjectives (4)**: {謙虚|けんきょ} (humble), {控|ひか}えめ (reserved), {高圧的|こうあつてき} (overbearing), {威圧的|いあつてき} (intimidating)
- **Nouns (9)**: {表現力|ひょうげんりょく} (expressive ability), {未使用|みしよう} (unused), {断面|だんめん} (cross-section), {登山者|とざんしゃ} (mountaineer), {王座|おうざ} (throne), {愚|おろ}か{者|もの} (fool), {基本給|きほんきゅう} (base salary), {植|う}え{付|つ}け (planting), {収穫期|しゅうかくき} (harvest season)
- **Godan verb (1)**: {取|と}り{逃|のが}す (to miss catching)
- **Adverb (1)**: {一般的|いっぱんてき}に (generally)
- **Expression (1)**: {構|かま}わない (don't mind)
- **Other nouns (2)**: {作務衣|さむえ} (samue work clothes), {成長期|せいちょうき} (growth period)
- Removed 30 candidates that now exist as entries




---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
