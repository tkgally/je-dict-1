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

### 2026-05-03 (Vocabulary Expansion - 20 New Entries, Batch 83)
Added 20 new dictionary entries (IDs 26591-26610) from candidate_words.json. Mix of essential grammar patterns, cultural vocabulary, sports terminology, and practical words across diverse domains.

- **Grammar patterns/expressions (6)**: はずだ (should be/expected to), べきだ (should/ought to), ようだ (seems/like/so that), {問題|もんだい}ない (no problem), どれぐらい (how much/long), ごとし (like/as if — literary)
- **Sports/baseball (2)**: {先発|せんぱつ}{投手|とうしゅ} (starting pitcher), {首位|しゅい}{打者|だしゃ} (batting champion)
- **Culture/history (3)**: {縄文|じょうもん}{土器|どき} (Jomon pottery), {民俗|みんぞく}{芸能|げいのう} (folk performing arts), {記念|きねん}アルバム (commemorative album)
- **Academic/education (3)**: {環境学|かんきょうがく} (environmental studies), {授業案|じゅぎょうあん} (lesson plan), {接続|せつぞく}{助詞|じょし} (conjunctive particle)
- **Science (1)**: {古生物|こせいぶつ} (fossil organism)
- **Entertainment (1)**: {名|めい}{脇役|わきやく} (great supporting actor)
- **Physical description (1)**: {高身長|こうしんちょう} (tall stature)
- **Food/cooking (1)**: {拍子木|ひょうしぎ}{切|ぎ}り (baton cut)
- **Politics (1)**: {核拡散|かくかくさん} (nuclear proliferation)
- **Legal (1)**: {在留権|ざいりゅうけん} (right of residence)
- 20 candidates synced from candidate list

Total entries: 26,383 → 26,403.

### 2026-05-03 (Vocabulary Expansion - 18 New Entries, Batch 82)
Added 18 new dictionary entries (IDs 26573-26590) from candidate_words.json. Diverse vocabulary covering spatial terms, education, lifestyle, politics, history, crafts, culture, and technology.

- **Spatial/direction (2)**: {下側|したがわ} (lower side), {隣側|となりがわ} (neighboring side)
- **Education (1)**: {退園|たいえん} (leaving kindergarten/nursery)
- **Lifestyle (1)**: {昼型|ひるがた} (daytime-type person)
- **Statistics/data (1)**: {地域別|ちいきべつ} (by region)
- **Nature/science (2)**: {軟体|なんたい} (soft-bodied), {水柱|すいちゅう} (water column)
- **Psychology (1)**: {記銘|きめい} (memorization/encoding)
- **History/politics (2)**: {虐政|ぎゃくせい} (tyrannical rule), {衆議院議員|しゅうぎいんぎいん} (House of Representatives member)
- **Textiles (1)**: {綿糸|めんし} (cotton yarn)
- **Skills/actions (2)**: {早技|はやわざ} (quick technique), {擦|す}り{寄|よ}せる (to bring close; reconcile)
- **Administration (1)**: {呼名|こめい} (roll call; designation)
- **Character/behavior (1)**: {自由勝手|じゆうかって} (acting selfishly)
- **Technology (1)**: {常時稼働|じょうじかどう} (continuous operation)
- **Infrastructure (1)**: {水道工事|すいどうこうじ} (plumbing work)
- **Culture (1)**: {風車小屋|ふうしゃごや} (windmill house)
- Conjugation tables auto-generated for 5 verb entries (4 suru, 1 ichidan)
- 3 stale duplicate candidates removed; 17 candidates synced

Total entries: 26,365 → 26,383.

### 2026-05-03 (Vocabulary Expansion - 20 New Entries, Batch 81)
Added 20 new dictionary entries (IDs 26553-26572) from candidate_words.json. Focus on practical expressions, proverbs, daily-life vocabulary, and useful standalone words.

- **Proverbs (2)**: {二兎|にと}を{追|お}う{者|もの}は{一兎|いっと}をも{得|え}ず (don't chase two goals), {急|せ}いては{事|こと}を{仕損|しそん}じる (haste makes waste)
- **Polite expressions/greetings (4)**: お{先|さき}に (excuse me for going first), お{大事|だいじ}に (take care), おかげさまで (thanks to you), ご{覧|らん}いただく (please look — humble keigo)
- **Grammar/formal patterns (1)**: に{先立|さきだ}って (prior to)
- **Verbs (2)**: {溶|と}く (to dissolve/mix), {噴|ふ}く (to spout/erupt)
- **Money/currency (2)**: {五千円札|ごせんえんさつ}, {一万円札|いちまんえんさつ}
- **Time/scheduling (2)**: {所要時間|しょようじかん} (required time), {時間外|じかんがい} (after hours)
- **Food/drink (2)**: {食|た}べ{頃|ごろ} (ready to eat), {飲|の}み{頃|ごろ} (ready to drink)
- **Signs/rules (1)**: {撮影禁止|さつえいきんし} (no photography)
- **Seasons/time (1)**: {真|ま}っ{盛|さか}り (at peak)
- **Language study (1)**: {偏|へん} (kanji left-side radical)
- **Counting (1)**: {一箇所|いっかしょ} (one place)
- **Daily expression (1)**: {気|き}を{配|くば}る (to be attentive)
- Conjugation tables auto-generated for 2 godan verbs
- 43+ stale candidates removed during session cleanup
- 5 candidates synced (now exist as entries)

Total entries: 26,345 → 26,365.

### 2026-05-02 (Vocabulary Expansion - 18 New Entries, Batch 80)
Added 18 new dictionary entries (IDs 26535-26552) from candidate_words.json. Diverse vocabulary spanning medical, business, technology, food culture, martial arts, and family terminology.

- **Medical (2)**: {既往歴|きおうれき} (medical history), {瘢痕|はんこん} (scar tissue)
- **Business/economics (2)**: {製造原価|せいぞうげんか} (manufacturing cost), {通貨流通|つうかりゅうつう} (currency circulation)
- **Technology/media (3)**: {中継局|ちゅうけいきょく} (relay station), {再生画面|さいせいがめん} (playback screen), {内燃機関|ないねんきかん} (internal combustion engine)
- **Food/drink culture (2)**: {四合瓶|よんごうびん} (720ml sake bottle), {焙煎度|ばいせんど} (coffee roast level)
- **Society/politics (2)**: {癒着関係|ゆちゃくかんけい} (collusive relationship), {標準世帯|ひょうじゅんせたい} (standard household)
- **Publishing (1)**: {商業出版|しょうぎょうしゅっぱん} (commercial publishing)
- **Music (1)**: {演奏技術|えんそうぎじゅつ} (performance technique)
- **Martial arts (1)**: {組み技|くみわざ} (grappling technique)
- **Shopping (1)**: {新品未使用|しんぴんみしよう} (brand new, unused)
- **Entertainment (1)**: {席種|せきしゅ} (seat category)
- **Gardening (1)**: {追い肥|おいごえ} (additional fertilizer)
- **Family (1)**: {長孫|ちょうそん} (eldest grandchild)
- Conjugation tables auto-generated for 2 suru-verb entries
- 1 new kanji added to index: 瘢 (ID 02728)
- 18 candidates synced from candidate list

Total entries: 26,327 → 26,345.

### 2026-05-02 (Vocabulary Expansion - 20 New Entries, Batch 79)
Added 20 new dictionary entries (IDs 26515-26534) from candidate_words.json. Focused on practical vocabulary spanning business, technology, daily life, culture, and language.

- **Business/legal (4)**: {実績主義|じっせきしゅぎ} (meritocracy), {秘密保持|ひみつほじ} (confidentiality), リスク{管理|かんり} (risk management), {危険管理|きけんかんり} (hazard management)
- **Daily life (3)**: {不用品回収|ふようひんかいしゅう} (junk removal), {自宅学習|じたくがくしゅう} (home study), {貸し会議室|かしかいぎしつ} (rental conference room)
- **Language/honorifics (1)**: お{召し上がり|めしあがり} (please help yourself — honorific)
- **Technology (1)**: {薄型化|うすがたか} (making thinner — electronics)
- **Character/personality (3)**: {我勝手|わがかって} (selfishness), {不忠実|ふちゅうじつ} (unfaithful), {正直一途|しょうじきいちず} (earnestly honest)
- **Entertainment/culture (2)**: {完成披露|かんせいひろう} (premiere), {終わりよければすべてよし|おわりよければすべてよし} (all's well that ends well)
- **Crafts/media (1)**: {嵌め込み|はめこみ} (inlay; compositing)
- **Cognition (1)**: {読み過ぎる|よみすぎる} (to overinterpret)
- **Society (2)**: {過密都市|かみつとし} (overcrowded city), {同胞愛|どうほうあい} (brotherly love)
- **Psychology (1)**: {舞台恐怖症|ぶたいきょうふしょう} (stage fright)
- **Agriculture (1)**: {有機肥料|ゆうきひりょう} (organic fertilizer)
- Conjugation tables auto-generated for 1 ichidan verb and 1 suru-verb
- 19 candidates synced; 4 stale duplicate candidates removed

Total entries: 26,307 → 26,327.

### 2026-05-02 (Vocabulary Expansion - 15 New Entries, Batch 78)
Added 15 new dictionary entries (IDs 26500-26514) from candidate_words.json. Mixed vocabulary spanning civil engineering, linguistics, medicine, business, photography, cultural traditions, and daily life.

- **Civil engineering (1)**: {法面|のりめん} (embankment slope)
- **Linguistics (1)**: {廃語|はいご} (obsolete word)
- **Medical/pharmaceutical (2)**: {満量|まんりょう} (full dose), {術前|じゅつぜん} (preoperative)
- **Business/formal (3)**: {返答書|へんとうしょ} (written reply), {如上|じょじょう} (as stated above), {遅答|ちとう} (delayed reply)
- **Photography/optics (1)**: {合焦|ごうしょう} (focusing)
- **Daily life/products (2)**: {浴用|よくよう} (for bathing use), {箱|はこ}ティッシュ (box tissues)
- **Culture/food (2)**: {春|はる}の{七草|ななくさ} (seven spring herbs), {米粉|こめこ}パン (rice flour bread)
- **Games (1)**: {場札|ばふだ} (table card)
- **Language/formal (2)**: {称辞|しょうじ} (words of praise), {荷受人|にうけにん} (consignee)
- Conjugation tables auto-generated for 2 suru-verb entries
- 15 candidates synced from candidate list

Total entries: 26,292 → 26,307.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
