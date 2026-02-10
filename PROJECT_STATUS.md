# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-10
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
| Total entries | ~10,836 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,037 (open) |
| Candidate words | ~121 |
| Cross-references | ~3,332 |
| Example sentences | ~41,570 |
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

### 2026-02-10 (Vocabulary Expansion - 30 New Entries, Session 235)
Added 30 new dictionary entries (IDs 10815-10844) from candidate_words.json:

- **Nouns (22)**: キッチン (kitchen), カウンター (counter), カテゴリー (category), キャンパス (campus), キリスト教 (Christianity), ギフト (gift), クレジット (credit), グランプリ (grand prix), オプション (option), オーナー (owner), キーワード (keyword), ギャラリー (gallery), ガイドライン (guideline), キャッシュカード (ATM card), キャラメル (caramel), キムチ (kimchi), オーディション (audition), オープニング (opening), ガイダンス (guidance), カーボン (carbon), カルチャー (culture)
- **Nouns + suru verb (3)**: カット (cut), キープ (keep), クリア (clear)
- **Nouns + na-adjective (3)**: カオス (chaos), オープン (open), カラー (color)
- **Nouns + no-adjective (1)**: オリジナル (original)
- **Onomatopoeia (1)**: ガタゴト (rumbling, clattering)

Notable features:
- Primarily katakana loanwords filling major gaps in common everyday vocabulary
- Multi-sense entries: カウンター (service desk/counterattack), カラー (color/hair coloring), キャリア (career/phone carrier), クリア (clear/pass/transparent), クレジット (payment/attribution), ギャラリー (art gallery/spectators), カット (haircut/deletion), キープ (maintain/bottle keep), オープン (grand opening/open-minded), オリジナル (unique creation/source version)
- Japan-specific concepts: ボトルキープ (bottle keep at bars), カルチャースクール (hobby classes), システムキッチン (built-in kitchen units), キャッシュカード (ATM-only bank card)
- Cross-reference: キッチン↔台所

Total entries: 10,806 → 10,836
Remaining candidates: 151 → 121

### 2026-02-10 (Vocabulary Expansion - 30 New Entries, Session 234)
Added 30 new dictionary entries (IDs 10785-10814) from candidate_words.json:

- **Nouns (21)**: おんぼろ (shabby), {牡蠣|かき} (oyster), カステラ (castella cake), {蕪|かぶ} (turnip), {干瓢|かんぴょう} (dried gourd), がらくた (junk), カニカマ (imitation crab), キクラゲ (wood ear mushroom), キャッチコピー (catchphrase), クッキー (cookie), クッション (cushion), グッズ (merchandise), カクテル (cocktail), カタログ (catalog), オムレツ (omelette), オリーブ (olive), キャンペーン (promotion), ギャグ (gag/joke), ギャンブル (gambling), グラウンド (playing field), クローン (clone)
- **Onomatopoeia/mimetic (4)**: かんかん (furious/scorching/clanging), ガクガク (shaking), ギザギザ (jagged), ぐず (slowpoke)
- **Na-adjectives (2)**: カラフル (colorful), カチューシャ (headband)
- **Multi-sense (3)**: {肝|きも} (key point/liver), クッション (cushion/buffer), クラブ (club/nightclub)

Notable features:
- Food and ingredients cluster: {牡蠣|かき}, カステラ, {蕪|かぶ}, {干瓢|かんぴょう}, カニカマ, キクラゲ, クッキー, オムレツ, オリーブ, カクテル
- Japanese food culture: regional specialties ({長崎|ながさき}カステラ, {広島|ひろしま}{牡蠣|かき}, {小豆島|しょうどしま}オリーブ)
- Wasei-eigo: キャッチコピー (catch + copy), カニカマ (crab + kamaboko)
- Onomatopoeia: かんかん (3 senses), ガクガク, ギザギザ
- New kanji: 2,281 → 2,284 (瓢, 蕪, 蠣)

Total entries: 10,776 → 10,806
Remaining candidates: 104 → 151

### 2026-02-10 (Vocabulary Expansion - 30 New Entries, Session 233)
Added 30 new dictionary entries (IDs 10755-10784) from candidate_words.json:

- **Expressions (13)**: 空気読む (read the room), なんでもいい (anything's fine), ということで (so then), だよね (right?), でしょ (right?), でもさ (but you know), まあね (well yeah), てことは (so that means), なにそれ (what's that?), いいよ (it's okay), ノリが悪い (being a killjoy), やばっ (oh no!/wow!), くそ (damn)
- **Adjectives (4)**: かっこわるい (uncool), おもろい (funny, Kansai), たるい (sluggish), ブサイク (ugly)
- **Verbs (3)**: ポチる (order online), やんちゃする (act up), おちゃらける (joke around)
- **Nouns (7)**: ごろつき (thug), 二項対立 (binary opposition), 三和土 (entrance floor), 赤字国債 (deficit bonds), 上がりがまち (entrance step), エンターテインメント (entertainment), タメ語 (casual speech)
- **Adverb (1)**: ほんまに (really, Kansai)
- **Pronoun (1)**: やつ (guy/thing)
- **Suffix (1)**: みたい (like, similar to)

Notable features:
- Heavy focus on conversational expressions and casual vocabulary useful for media comprehension
- Kansai dialect: ほんまに, おもろい
- Cultural concepts: 空気読む (KY culture), タメ語 (speech level switching), ノリが悪い (group participation norms)
- Traditional architecture: 三和土 (tataki), 上がりがまち (entrance step)
- Modern internet culture: ポチる (online impulse buying)
- Multi-sense entries: みたい (resemblance/conjecture), かっこわるい (uncool/embarrassing), でしょ (confirmation/vindication), なにそれ (curiosity/disbelief), やばっ (alarm/excitement), ブサイク (ugly/clumsy), やんちゃする (childhood/teenage), いいよ (permission/reassurance), やつ (person/thing), くそ (expletive/prefix), ということで (transition/wrap-up)
- Cross-references: だよね↔だよな, だよね↔でしょ, てことは↔ということで, かっこわるい↔かっこいい
- New kanji: 2,280 → 2,281 (框)

Total entries: 10,746 → 10,776
Remaining candidates: 133 → 104

### 2026-02-09 (Vocabulary Expansion - 30 New Entries, Session 232)
Added 30 new dictionary entries (IDs 10725-10754) from candidate_words.json:

- **Nouns (14)**: エプロン (apron), エリア (area), エビデンス (evidence), アスファルト (asphalt), アラート (alert), オイル (oil), アマチュア (amateur), アカデミー (academy), アシスタント (assistant), イラストレーター (illustrator), データ{通信|つうしん} (data communication), {雄|おす} (male animal)
- **Nouns + suru verb (4)**: エスカレート (escalate), アウトプット (output), インプット (input), エントリー (entry/registration), フォロバ (follow back)
- **Nouns (2+ senses) (3)**: エピソード (anecdote/episode), アクション (action step/action genre), エージェント (agent/spy), オフ (off/day off/discount)
- **Particles (2)**: っけ (memory-confirming), かも (maybe)
- **Interjections (3)**: よし (alright!), そうそう (yeah yeah), あのさ (hey, listen), よっしゃ (yes!)
- **Adverbs (2)**: いまひとつ (not quite), ちょい (a bit)
- **Expression (1)**: どうしよう (what should I do)

Notable features:
- Mix of loanwords, conversational particles, and interjections
- Multi-sense entries: エピソード (anecdote/episode), アクション (concrete step/entertainment genre), エージェント (representative/spy), オフ (off/day off/discount)
- Cross-references: アウトプット↔インプット, よし↔よっしゃ
- Conversational vocabulary: っけ, かも, そうそう, あのさ, どうしよう, よし, よっしゃ
- Business/tech: エビデンス, アウトプット/インプット, エントリー, エージェント, データ{通信|つうしん}
- Internet/social media: フォロバ (follow back)
- New kanji: 2,279 → 2,280 ({雄|ゆう})

Total entries: 10,716 → 10,746
Remaining candidates: 163 → 133

### 2026-02-09 (Vocabulary Expansion - 30 New Entries, Session 231)
Added 30 new dictionary entries (IDs 10695-10724) from candidate_words.json:

- **Nouns (20)**: アウトドア (outdoor), アトリエ (studio), アボカド (avocado), アラーム (alarm), アリーナ (arena), アルファベット (alphabet), アワビ (abalone), アーモンド (almond), イクラ (salmon roe), イチオシ (top pick), イラスト (illustration), イワシ (sardine), インパクト (impact), {鱗|うろこ} (scale), エキス (extract), エッセイ (essay)
- **Nouns + suru verb (5)**: アクセス (access), アナウンス (announcement), アピール (appeal), アプローチ (approach), アーカイブ (archive)
- **Nouns + na-adjective (2)**: アホ (fool/stupid), インスタント (instant)
- **Nouns (2 senses) (3)**: アクセント (accent/highlight), アプローチ (method/outreach), アクセス (transport/computing)
- **Other nouns (3)**: アドバイス (advice), アーティスト (artist), アート (art), アラサー (around 30), アラフォー (around 40), インバウンド (inbound tourism)

Notable features:
- Primarily katakana loanwords filling gaps in the dictionary's coverage of common borrowed vocabulary
- Food vocabulary: アボカド, アワビ, イクラ, イワシ, アーモンド, エキス, インスタント
- Cultural/modern Japanese: アラサー/アラフォー (age-related wasei-eigo), インバウンド (tourism buzzword), イチオシ (fan/recommendation culture)
- Arts/media: アトリエ, アート, アーティスト, イラスト, エッセイ, アーカイブ
- One native Japanese word with new kanji: {鱗|うろこ} (scale)
- Cross-references: アラサー↔アラフォー
- New kanji: 2,278 → 2,279 ({鱗|りん})

Total entries: 10,686 → 10,716
Remaining candidates: 193 → 163

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
