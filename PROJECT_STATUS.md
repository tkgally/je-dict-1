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
| Total entries | ~10,776 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~7,977 (open) |
| Candidate words | ~104 |
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

### 2026-02-09 (Vocabulary Expansion - 30 New Entries, Session 230)
Added 30 new dictionary entries (IDs 10665-10694) from candidate_words.json:

- **Nouns (25)**: しじみ (freshwater clam), ちまき (rice dumpling), ちょんまげ (topknot), ふるさと{納税|のうぜい} (hometown tax), {書|か}き{入|い}れ{時|どき} (busy season), {合気道|あいきどう} (aikido), {居合道|いあいどう} (iaido), {雹|ひょう} (hail), {空手道|からてどう} (karate), {偏差|へんさ} (deviation), {幻覚|げんかく} (hallucination), {威厳|いげん} (dignity), {利便性|りべんせい} (convenience), {素振|そぶ}り (behavior/pretense), {嫌気|いやけ} (disgust/aversion), {顔合|かおあ}わせ (meeting), {水際|みずぎわ} (water's edge/border control), {口添|くちぞ}え (putting in a good word), アイデンティティ (identity), {三男|さんなん} (third son), {三女|さんじょ} (third daughter), くノ{一|いち} (female ninja), {義理|ぎり}の{親|おや} (parent-in-law), ネット{回線|かいせん} (internet connection), てにをは (particles/fine points)
- **Nouns (suru verb) (1)**: {一任|いちにん} (entrusting entirely)
- **Nouns (2 senses) (3)**: ちゃんぽん (chanpon/mixing), {触媒|しょくばい} (catalyst), {水際|みずぎわ} (shore/border control)
- **Verb (1)**: かまける (to be preoccupied with)
- **Adjective (1)**: ねむたい (sleepy)

Notable features:
- Multi-sense entries: ちゃんぽん (noodle dish/mixing), てにをは (particles/wording), {触媒|しょくばい} (chemical/figurative), {水際|みずぎわ} (shore/border), {素振|そぶ}り (behavior/sign), {義理|ぎり}の{親|おや} (in-law/step-parent)
- Martial arts cluster: {合気道|あいきどう}, {居合道|いあいどう}, {空手道|からてどう} (with cross-references)
- Cultural vocabulary: ちまき ({端午|たんご}の{節句|せっく}), ちょんまげ (sumo/samurai), くノ{一|いち} (ninja), {顔合|かおあ}わせ (wedding custom)
- Modern/practical: ふるさと{納税|のうぜい}, ネット{回線|かいせん}, アイデンティティ, {利便性|りべんせい}
- Family terms: {三男|さんなん}, {三女|さんじょ}, {義理|ぎり}の{親|おや} (with cross-references)
- Academic/scientific: {偏差|へんさ} ({偏差|へんさ}{値|ち}), {触媒|しょくばい}, {幻覚|げんかく}
- New kanji: 2,277 → 2,278 ({雹|ひょう})

Total entries: 10,641 → 10,671
Remaining candidates: 167 → 137


### 2026-02-08 (Vocabulary Expansion - 30 New Entries, Session 228)
Added 30 new dictionary entries (IDs 10605-10634) from candidate_words.json:

- **Nouns (18)**: {神輿|みこし} (portable shrine), {暇潰|ひまつぶ}し (killing time), かみさん (wife), {紙芝居|かみしばい} (kamishibai), {縁日|えんにち} (temple festival), {肝試|きもだめ}し (test of courage), {取|と}り{越|こ}し{苦労|くろう} (unnecessary worry), {名義|めいぎ} (name on title), {境目|さかいめ} (boundary), {足取|あしど}り (gait/trail), {寝癖|ねぐせ} (bed hair), {腕組|うでぐ}み (folding arms), {折|お}り{返|かえ}し (return call/turnaround), {見|み}どころ (highlight), {婿|むこ} (bridegroom), {読|よ}み{聞|き}かせ (reading aloud), {飛|と}び{火|ひ} (spreading fire/impetigo), {参拝|さんぱい} (shrine visit)
- **Verbs (6)**: {漕|こ}ぎ{着|つ}ける (to manage to reach), なぞらえる (to liken), {引|ひ}っ{掛|か}ける (to hook/trick), ぶら{下|さ}げる (to hang), {触|ふ}れ{合|あ}う (to interact), {見|み}なす (to regard as), {目論|もくろ}む (to scheme)
- **I-adjectives (3)**: ひもじい (hungry), {晴|は}れ{晴|ば}れしい (bright/cheerful), {神々|こうごう}しい (divine/sublime)
- **Adverb/onomatopoeia (1)**: くちゃくちゃ (noisily chewing/crumpled)
- **Prefix (1)**: {初|はつ} (first)

Notable features:
- Cultural vocabulary cluster: {神輿|みこし}, {縁日|えんにち}, {肝試|きもだめ}し, {紙芝居|かみしばい}, {参拝|さんぱい}
- Multi-sense entries: {引|ひ}っ{掛|か}ける (3 senses), {飛|と}び{火|ひ} (3 senses), {足取|あしど}り (2 senses), {折|お}り{返|かえ}し (2 senses), くちゃくちゃ (2 senses), {見|み}どころ (2 senses), {婿|むこ} (2 senses), {触|ふ}れ{合|あ}う (2 senses)
- New kanji: 2,270 → 2,272 ({婿|せい}, {輿|よ})

Total entries: 10,581 → 10,611
Remaining candidates: 208 → 178

### 2026-02-08 (Vocabulary Expansion - 30 New Entries, Session 227)
Added 30 new dictionary entries (IDs 10575-10604) from candidate_words.json:

- **Nouns (18)**: {証拠|しょうこ} (evidence), {起訴|きそ} (indictment), {和解|わかい} (reconciliation/settlement), {弁護|べんご} (defense), {点滴|てんてき} (IV drip), {麻酔|ますい} (anesthesia), {版画|はんが} (printmaking), {織物|おりもの} (textile), {秩序|ちつじょ} (order), {逆説|ぎゃくせつ} (paradox), {心境|しんきょう} (state of mind), {胸騒|むなさわ}ぎ (foreboding), {仕返|しかえ}し (retaliation), {出来心|できごころ} (sudden impulse), {修羅場|しゅらば} (carnage/confrontation), {権限|けんげん} (authority), お{裾分|すそわ}け (sharing gifts), {機転|きてん} (quick wit), {所作|しょさ} (demeanor)
- **Verbs (6)**: {付|つ}き{添|そ}う (to accompany), {噛|か}み{合|あ}う (to mesh), {寄|よ}り{添|そ}う (to stay close), {入|い}り{浸|びた}る (to frequent), {投|な}げ{出|だ}す (to give up), そそのかす (to instigate)
- **I-adjectives (3)**: {何気|なにげ}ない (casual), {初々|ういうい}しい (fresh/innocent), {目|め}まぐるしい (dizzying)
- **Noun + suru verbs (1)**: {赴任|ふにん} (taking up a new post)
- **Noun (cultural)**: {漆|うるし} (lacquer/lacquerware)

Notable features:
- Multi-sense entries: {和解|わかい} (reconciliation/legal settlement), {漆|うるし} (lacquer/lacquerware), {噛|か}み{合|あ}う (mesh/in sync), {投|な}げ{出|だ}す (stretch out/give up), {修羅場|しゅらば} (battle/confrontation), {寄|よ}り{添|そ}う (physical/emotional)
- Legal vocabulary cluster: {証拠|しょうこ}, {起訴|きそ}, {和解|わかい}, {弁護|べんご}
- Medical vocabulary: {点滴|てんてき}, {麻酔|ますい}
- Cultural context: {漆|うるし} (lacquerware tradition), お{裾分|すそわ}け (sharing custom), {修羅場|しゅらば} (Buddhist origin), {所作|しょさ} (tea ceremony)
- Cross-references: {起訴|きそ}↔{弁護|べんご}, {付|つ}き{添|そ}う↔{寄|よ}り{添|そ}う

Total entries: 10,551 → 10,581
Remaining candidates: 238 → 208
New kanji: 2,267 → 2,270 ({漆|しつ}, {秩|ちつ}, {赴|ふ})

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
