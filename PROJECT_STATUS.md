# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-17
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

### 2026-05-01 (Vocabulary Expansion - 20 New Entries, Batch 74)
Added 20 new dictionary entries (IDs 26430-26449) from candidate_words.json. Diverse batch covering transport, business, technology, daily life, and more.

- **Transport (2)**: {降車口|こうしゃぐち} (exit door on vehicles), {軽車両|けいしゃりょう} (light vehicle/bicycle category)
- **Business/industry (3)**: {個人客|こじんきゃく} (individual customer), {半製品|はんせいひん} (semi-finished product), {純正部品|じゅんせいぶひん} (genuine OEM parts)
- **Technology/audio (3)**: {計測器|けいそくき} (measuring instrument), {受信|じゅしん}メール (received email), {雑音除去|ざつおんじょきょ} (noise cancellation)
- **Daily life (4)**: {海外在住|かいがいざいじゅう} (living abroad), {卓上鏡|たくじょうきょう} (tabletop mirror), カーボン{紙|し} (carbon paper), {人数分|にんずうぶん} (enough for the group)
- **Geography/science (2)**: {海水面|かいすいめん} (sea level), {先史時代|せんしじだい} (prehistoric era)
- **Communication/work (2)**: {連絡板|れんらくばん} (message board), {資格証明|しかくしょうめい} (proof of qualification)
- **Education/family (1)**: {幼児向|ようじむ}け (for young children)
- **Policy/strategy (1)**: {路線変更|ろせんへんこう} (route change/policy shift)
- **Expression (1)**: {生身|なまみ}の{人間|にんげん} (flesh-and-blood human being)
- **Safety (1)**: {衝撃吸収|しょうげききゅうしゅう} (shock absorption)
- Conjugation tables auto-generated for 2 suru-verb entries
- 20 candidates synced from candidate list

Total entries: 26,222 → 26,242.

### 2026-05-01 (Vocabulary Expansion - 20 New Entries, Batch 73)
Added 20 new dictionary entries (IDs 26410-26429) from candidate_words.json. Diverse batch spanning life stages, transport, sports, linguistics, arts, science, business, and more.

- **Life stages/society (2)**: {壮年期|そうねんき} (middle age/prime of life), {隠居人|いんきょにん} (retired person/recluse)
- **Transport (3)**: {牽引車|けんいんしゃ} (tow truck/tractor), {定期運行|ていきうんこう} (regular service), {副機長|ふくきちょう} (copilot)
- **Sports (1)**: {交代選手|こうたいせんしゅ} (substitute player)
- **Linguistics (3)**: {有声音|ゆうせいおん} (voiced sound), {無声音|むせいおん} (voiceless sound), {五七調|ごしっちょう} (five-seven meter)
- **Arts/music (1)**: {指揮台|しきだい} (conductor's podium)
- **Science/chemistry (1)**: {塩化物|えんかぶつ} (chloride)
- **Urban/environment (1)**: {都市景観|としけいかん} (urban landscape/cityscape)
- **History/politics (1)**: {植民地主義|しょくみんちしゅぎ} (colonialism)
- **Business (1)**: {社内秘|しゃないひ} (confidential/internal use only)
- **Publishing (1)**: {編纂者|へんさんしゃ} (compiler/editor of reference works)
- **Medicine (1)**: {前立腺|ぜんりつせん} (prostate gland)
- **Material (1)**: {磁器製|じきせい} (made of porcelain)
- **Measurement (1)**: {中間点|ちゅうかんてん} (midpoint/halfway point)
- **Nature (1)**: {造園士|ぞうえんし} (landscape gardener)
- **Forensics (1)**: {掌紋|しょうもん} (palm print)
- 20 candidates synced from candidate list

Total entries: 26,202 → 26,222.

### 2026-05-01 (Vocabulary Expansion - 12 New Entries, Batch 72)
Added 12 new dictionary entries (IDs 26398-26409) from candidate_words.json. Focus on practical vocabulary covering media, daily life, business, politics, and industry.

- **Media/entertainment (2)**: {連続|れんぞく}ドラマ (serial drama/TV series), {原作家|げんさくか} (original author)
- **Leisure (1)**: {絶叫|ぜっきょう}マシン (thrill ride)
- **Daily life/food (2)**: {白砂糖|しろざとう} (white sugar), {調乳|ちょうにゅう} (preparing formula)
- **Business/real estate (2)**: {立地|りっち}{条件|じょうけん} (location conditions), {利害|りがい}{調整|ちょうせい} (coordination of interests)
- **Politics (1)**: {国務大臣|こくむだいじん} (minister of state)
- **Education (1)**: {出題者|しゅつだいしゃ} (question setter)
- **Industry/technology (2)**: {電子|でんし}{部品|ぶひん} (electronic components), {水産|すいさん}{加工|かこう} (seafood processing)
- **Insurance (1)**: {自動車|じどうしゃ}{保険|ほけん} (car insurance)
- Conjugation table auto-generated for 1 suru-verb entry (調乳する)
- 12 candidates synced from candidate list; 1 stale duplicate removed

Total entries: 26,190 → 26,202.

### 2026-05-01 (Vocabulary Expansion - 20 New Entries, Batch 71)
Added 20 new dictionary entries (IDs 26378-26397) from candidate_words.json. Focus on modern life, technology, culture, and daily practical vocabulary.

- **Technology/digital (4)**: ダブルクリック (double-click), {相互|そうご}フォロー (mutual follow), カスタマーサポート (customer support), {番号通知|ばんごうつうち} (caller ID)
- **Modern life (3)**: プロフィール{写真|しゃしん} (profile photo), ノマドワーカー (digital nomad), {自己出版|じこしゅっぱん} (self-publishing)
- **Household/daily (4)**: {洗濯物干|せんたくものほ}し (drying rack/hanging laundry), {電子|でんし}レンジ{可|か} (microwave-safe), ランドリールーム (laundry room), {爪磨|つめみが}き (nail buffing)
- **Health/admin (2)**: {接種券|せっしゅけん} (vaccination voucher), {届出書|とどけでしょ} (notification form)
- **Culture/academic (3)**: {歳神様|としがみさま} (New Year deity), {文化人類学|ぶんかじんるいがく} (cultural anthropology), {近況文|きんきょうぶん} (status update message)
- **Events/sports (2)**: {開始式|かいししき} (opening ceremony), {体操競技|たいそうきょうぎ} (artistic gymnastics)
- **Commerce (2)**: {販売機|はんばいき} (vending machine), シャワーを{浴|あ}びる (to take a shower)
- Conjugation tables auto-generated for 3 suru-verb entries
- 19 candidates synced from candidate list

Total entries: 26,170 → 26,190.

### 2026-05-01 (Vocabulary Expansion - 17 New Entries, Batch 70)
Added 17 new dictionary entries (IDs 26361-26377) from candidate_words.json. Mixed batch covering food, clothing, transportation, environment, language, and daily life.

- **Food (3)**: {粕|かす} (dregs/residue/lees), カマンベール (camembert cheese), バニラアイス (vanilla ice cream)
- **Clothing/fashion (4)**: ルームウェア (loungewear), ナイトウェア (nightwear), ポリエステル (polyester), ペディキュア (pedicure)
- **Transportation (1)**: ドアミラー (side mirror, wasei-eigo)
- **Environment (1)**: リデュース (reduce, 3R movement)
- **Business (2)**: {全品|ぜんぴん} (all items), {送付状|そうふじょう} (cover letter/transmittal)
- **Language/education (1)**: {和文英訳|わぶんえいやく} (Japanese-to-English translation)
- **Geography (1)**: メキシコ (Mexico)
- **Body/movement (1)**: のけぞり (bending backward)
- **Sound (1)**: ばたんばたん (repeated banging/slamming)
- **Verbs (1)**: {立|た}ち{入|い}る (to enter/trespass)
- Conjugation tables auto-generated for 2 verb entries
- 15 candidates synced; 6 stale candidates removed

Total entries: 26,153 → 26,170.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
