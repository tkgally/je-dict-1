# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-03
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
| Total entries | ~14,834 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,035 (open) |
| Candidate words | ~4,936 |
| Cross-references | ~3,400 |
| Example sentences | ~49,000 |
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

### 2026-03-03 (Vocabulary Expansion - 30 New Entries, Session 366)
Added 30 new dictionary entries (IDs 14749-14778) from candidate_words.json:

- **Nouns (13)**: {囃子|はやし} (musical accompaniment), {妃|きさき} (empress consort), {具体例|ぐたいれい} (concrete example), {保冷剤|ほれいざい} (ice pack), {色紙|しきし} (autograph board), {港湾|こうわん} (harbor), {魔王|まおう} (demon king), {酒粕|さけかす} (sake lees), {領事館|りょうじかん} (consulate), {外交官|がいこうかん} (diplomat), {招待状|しょうたいじょう} (invitation), {鉄製|てっせい} (made of iron), {身辺|しんぺん} (around oneself)
- **Noun/suru verbs (7)**: {白眼視|はくがんし} (scorn), {遷都|せんと} (capital transfer), {祝賀|しゅくが} (celebration), {入港|にゅうこう} (port entry), {割愛|かつあい} (omitting), {鎮座|ちんざ} (enshrinement), {風靡|ふうび} (sweeping popularity)
- **Na-adjectives (5)**: {荘厳|そうごん} (solemn/sublime), {厳粛|げんしゅく} (grave/solemn), {高尚|こうしょう} (noble/refined), {限定的|げんていてき} (limited), {網羅的|もうらてき} (exhaustive)
- **Noun/na-adjective (1)**: {非道|ひどう} (inhumane)
- **Noun/suru verb (2)**: {現状維持|げんじょういじ} (status quo), {逢瀬|おうせ} (tryst)
- **Ichidan verb (1)**: {盛|も}り{付|つ}ける (to plate food)
- **Noun (ceremony) (1)**: {祝辞|しゅくじ} (congratulatory speech)

Notable features:
- Multi-sense entries: {鎮座|ちんざ} (2: enshrinement + sitting imposingly)
- Paired entries: {荘厳|そうごん}/{厳粛|げんしゅく}, {限定的|げんていてき}/{網羅的|もうらてき}, {領事館|りょうじかん}/{外交官|がいこうかん}
- Cultural: {囃子|はやし}, {妃|きさき}, {逢瀬|おうせ}, {色紙|しきし}, {酒粕|さけかす}, {魔王|まおう}
- Formal/academic: {白眼視|はくがんし}, {遷都|せんと}, {割愛|かつあい}, {風靡|ふうび}, {高尚|こうしょう}
- New kanji: 2,493 → 2,496 ({囃|そう}, {逢|ほう}, {靡|ひ})

Total entries: 14,804 → 14,834 (approximate)
Remaining candidates: 4,966 → 4,936 (30 removed)

### 2026-03-03 (Vocabulary Expansion - 30 New Entries, Session 365)
Added 30 new dictionary entries (IDs 14719-14748) from candidate_words.json:

- **Nouns (15)**: ケチャップ (ketchup), {開港|かいこう} (opening of a port), {冷凍庫|れいとうこ} (freezer), {常温|じょうおん} (room temperature), {穴場|あなば} (hidden gem), {撤去|てっきょ} (removal), {下見|したみ} (preliminary visit), {怪獣|かいじゅう} (monster), {泥酔|でいすい} (dead drunk), {車酔|くるまよ}い (carsickness), {駄菓子|だがし} (cheap sweets), {積雪|せきせつ} (snow cover), {助手席|じょしゅせき} (passenger seat), {鋼|はがね} (steel), {古本|ふるほん} (used book)
- **Nouns (compound)**: {掘|ほ}り{出|だ}し{物|もの} (bargain/lucky find), {鍵盤|けんばん} (keyboard/keys), {犠牲|ぎせい} (sacrifice/victim), {弁償|べんしょう} (compensation), {正反対|せいはんたい} (exact opposite)
- **I-adjectives (2)**: {待|ま}ち{遠|どお}しい (eagerly awaited), {脂|あぶら}っこい (greasy)
- **Na-adjectives (3)**: {割高|わりだか} (relatively expensive), {割安|わりやす} (relatively cheap), {過保護|かほご} (overprotective)
- **Godan verb (1)**: {悔|く}やむ (to regret/mourn)
- **Food/drink (4)**: ケチャップ, おでん, {駄菓子|だがし}, {脂|あぶら}っこい
- **Noun (food)**: おでん (oden stew)

Notable features:
- Multi-sense entries: {悔|く}やむ (2: regret + mourn), {洋画|ようが} (2: Western film + Western painting), {犠牲|ぎせい} (2: sacrifice + victim)
- Paired entries: {割高|わりだか}/{割安|わりやす}, {邦画|ほうが}/{洋画|ようが}
- Daily life: {冷凍庫|れいとうこ}, {常温|じょうおん}, {車酔|くるまよ}い, {助手席|じょしゅせき}, {段差|だんさ}
- Culture: おでん, {駄菓子|だがし}, {怪獣|かいじゅう}, {古本|ふるほん}
- New kanji: 2,490 → 2,493 ({犠|ぎ}, {牲|せい}, {鋼|こう})

Total entries: 14,774 → 14,804 (approximate)
Remaining candidates: 4,996 → 4,966 (30 removed)

### 2026-03-03 (Vocabulary Expansion - 30 New Entries, Session 364)
Added 30 new dictionary entries (IDs 14689-14718) from candidate_words.json:

- **Nouns (16)**: {重要文化財|じゅうようぶんかざい} (Important Cultural Property), {陸地|りくち} (land), {顔面|がんめん} (face), {食育|しょくいく} (food education), {音源|おんげん} (sound source/audio track), {高まり|たかまり} (rise/heightening), {高値|たかね} (high price), {高額|こうがく} (large sum), {高温|こうおん} (high temperature), {魚介|ぎょかい} (seafood), {鯛|たい} (sea bream), {黒船|くろふね} (black ships), {黎明期|れいめいき} (dawn of an era), {騎士|きし} (knight), {風当|かぜあ}たり (wind exposure/criticism), {食|く}い{倒|だお}れ (eating oneself into ruin)
- **Noun/suru verb (1)**: {鼓舞|こぶ} (encouragement)
- **Godan verbs (2)**: {陣取|じんど}る (to take up position), {駆|か}る (to drive/compel)
- **Ichidan verbs (2)**: {駆|か}ける (to run/dash), {魅|み}せる (to fascinate)
- **Na-adjectives (4)**: {風流|ふうりゅう} (elegant), {鬱|うつ} (depression), {高らか|たからか} (resounding), {露|あらわ} (exposed/undisguised)
- **Adverb (1)**: {黙々|もくもく} (silently/diligently)
- **Multi-POS (4)**: {風俗|ふうぞく} (customs/entertainment), {雛形|ひながた} (model/template), {鞘|さや} (sheath/pod), {風水|ふうすい} (feng shui)

Notable features:
- Multi-sense entries: {風俗|ふうぞく} (2: customs + adult entertainment), {雛形|ひながた} (2: model + template), {鞘|さや} (2: sheath + pod), {鬱|うつ} (2: depression + gloom), {黒船|くろふね} (2: historical + figurative disruptor), {音源|おんげん} (2: sound source + audio track), {風当|かぜあ}たり (2: wind exposure + criticism), {駆|か}る (2: drive/spur + compel), {駆|か}ける (2: run + gallop), {露|あらわ} (2: exposed + undisguised), {食|く}い{倒|だお}れ (2: spending ruin + Osaka culture)
- Culture: {重要文化財|じゅうようぶんかざい}, {黒船|くろふね}, {風水|ふうすい}, {風流|ふうりゅう}, {鯛|たい}, {食|く}い{倒|だお}れ
- Daily life: {高温|こうおん}, {魚介|ぎょかい}, {顔面|がんめん}, {食育|しょくいく}, {音源|おんげん}
- Finance: {高値|たかね}, {高額|こうがく}
- New kanji: 2,488 → 2,490 ({雛|すい}, {鞘|しょう})

Total entries: 14,744 → 14,774 (approximate)
Remaining candidates: 5,025 → 4,996 (29 removed)

### 2026-03-02 (Vocabulary Expansion - 30 New Entries, Session 363)
Added 30 new dictionary entries (IDs 14659-14688) from candidate_words.json:

- **Nouns (14)**: {防具|ぼうぐ} (protective gear), {陣営|じんえい} (camp/faction), {雪景色|ゆきげしき} (snowy scenery), {霊|れい} (spirit/ghost), {露天|ろてん} (open air), {顔|かお}ぶれ (lineup), {風紀|ふうき} (public morals), {風貌|ふうぼう} (appearance), {食塩|しょくえん} (table salt), {餅|もち}つき (rice cake pounding), {首位|しゅい} (first place), {香料|こうりょう} (spices/fragrance), {高台|たかだい} (elevated ground), {顔立|かおだ}ち (facial features)
- **Noun/suru verbs (7)**: {開国|かいこく} (opening of a country), {陳情|ちんじょう} (petition), {集約|しゅうやく} (consolidation), {集結|しゅうけつ} (gathering), {頻発|ひんぱつ} (frequent occurrence), {駆使|くし} (full command), {魅了|みりょう} (fascination)
- **Noun/suru verb (1)**: {高望|たかのぞ}み (aiming too high)
- **Noun/adjective-no (1)**: {非日常|ひにちじょう} (extraordinary)
- **Godan verbs (2)**: {霞|かす}む (to become hazy), {駆|か}け{寄|よ}る (to rush over to)
- **Na-adjective (1)**: {鮮明|せんめい} (vivid/clear)
- **Noun (time) (1)**: {頃合|ころあ}い (suitable time)
- **Noun (cultural) (3)**: {金魚|きんぎょ}すくい (goldfish scooping), {開国|かいこく} (opening of country), {餅|もち}つき (mochi pounding)

Notable features:
- Multi-sense entries: {防具|ぼうぐ} (2: sports gear + armor), {霊|れい} (2: spirit + ghost), {香料|こうりょう} (2: spice + fragrance), {霞|かす}む (2: become hazy + be overshadowed), {頃合|ころあ}い (2: suitable time + moderate degree), {陣営|じんえい} (2: faction + military camp), {集約|しゅうやく} (2: consolidation + intensive)
- Culture: {金魚|きんぎょ}すくい, {餅|もち}つき, {露天|ろてん}, {開国|かいこく}
- Daily life: {食塩|しょくえん}, {高台|たかだい}, {顔立|かおだ}ち, {顔|かお}ぶれ
- Formal/written: {類似|るいじ}, {鮮明|せんめい}, {風貌|ふうぼう}, {陳情|ちんじょう}, {駆使|くし}
- New kanji: 2,487 → 2,488 ({陣|じん})

Total entries: 14,714 → 14,744 (approximate)
Remaining candidates: 5,055 → 5,025 (30 removed)

### 2026-03-02 (Vocabulary Expansion - 30 New Entries, Session 362)
Added 30 new dictionary entries (IDs 14629-14658) from candidate_words.json:

- **Verbs (4)**: {面|めん}する (to face), {静|しず}まり{返|かえ}る (to fall completely silent), {馴染|なじ}む (to become familiar), {駆|か}けつける (to rush to)
- **Nouns (17)**: {風呂|ふろ} (bath), {食|しょく}パン (sliced bread), {首輪|くびわ} (collar), {馬車|ばしゃ} (carriage), {魂|たましい} (soul), {魔法|まほう} (magic), {魔女|まじょ} (witch), {魚屋|さかなや} (fish shop), {鮮度|せんど} (freshness), {麺|めん} (noodles), {黄金|おうごん} (gold), {髪型|かみがた} (hairstyle), {高熱|こうねつ} (high fever), {駄々|だだ} (tantrum), {馬力|ばりき} (horsepower), {騒動|そうどう} (commotion), {驚異|きょうい} (wonder)
- **Noun/suru verbs (4)**: {高騰|こうとう} (soaring prices), {集会|しゅうかい} (assembly), {養成|ようせい} (training), {高揚|こうよう} (elation)
- **Nouns (other) (2)**: {頼|たよ}り (reliance), {高齢|こうれい} (old age)
- **I-adjectives (2)**: {頼|たよ}りない (unreliable), {青白|あおじろ}い (pale)
- **Noun (weather) (1)**: {風向|かざむ}き (wind direction)

Notable features:
- Multi-sense entries: {馴染|なじ}む (2: get used to + fit in), {黄金|おうごん} (2: gold + golden/prime), {魂|たましい} (2: soul + spirit/passion), {風向|かざむ}き (2: wind direction + trend), {青白|あおじろ}い (2: pale + bluish-white), {馬力|ばりき} (2: horsepower + vigor)
- Daily life: {風呂|ふろ}, {食|しょく}パン, {首輪|くびわ}, {髪型|かみがた}, {麺|めん}, {魚屋|さかなや}
- Culture/pop culture: {魔法|まほう}, {魔女|まじょ}, {黄金|おうごん}, {魂|たましい}
- Economy/society: {高騰|こうとう}, {高齢|こうれい}, {集会|しゅうかい}, {養成|ようせい}
- New kanji: 2,486 → 2,487 ({魂|こん})

Total entries: 14,684 → 14,714 (approximate)
Remaining candidates: 5,085 → 5,055 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
