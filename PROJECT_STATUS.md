# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-27
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
| Total entries | ~19,058 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,259 (open) |
| Candidate words | ~5,099 |
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

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 522)
Added 30 new dictionary entries (IDs 20038-20067) from candidate_words.json. Mix of useful vocabulary including adverbs, adjectives, verbs, and nouns covering personality, business, culture, and daily life.

- **Nouns (10)**: {吐息|といき} (sigh), {影響力|えいきょうりょく} (influence), {耐久性|たいきゅうせい} (durability), {悪評|あくひょう} (bad reputation), {劇団|げきだん} (theater troupe), {裏目|うらめ} (backfire), {受領|じゅりょう} (receipt), {封書|ふうしょ} (sealed letter), {熱量|ねつりょう} (caloric value/passion), {可動|かどう} (movable)
- **Na-adjectives (3)**: {楽天的|らくてんてき} (optimistic), {奔放|ほんぽう} (uninhibited), {有難迷惑|ありがためいわく} (unwelcome favor)
- **Adverbs (4)**: {少|すこ}しずつ (little by little), {見事|みごと}に (splendidly), {巧|たく}みに (skillfully), えっと (um)
- **Verbs (7)**: {対処|たいしょ}する (to deal with), {反復|はんぷく}する (to repeat), {了承|りょうしょう}する (to consent), {許可|きょか}する (to permit), {承認|しょうにん}する (to approve), {吹|ふ}き{出|で}る (to gush out), {削|けず}り{取|と}る (to scrape off)
- **Other (6)**: {洗礼|せんれい} (baptism/ordeal), {同人|どうじん} (doujin/coterie), {行灯|あんどん} (paper lantern), {堂々|どうどう}たる (imposing), {規則正|きそくただ}しい (regular), {変|か}わった (unusual)
- Removed 30 candidates that now exist as entries

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 521)
Added 30 new dictionary entries (IDs 20008-20037) from candidate_words.json. Diverse vocabulary for intermediate learners covering emotions, culture, food, work, travel, and everyday life.

- **Nouns (14)**: {眺望|ちょうぼう} (view/panorama), {綿毛|わたげ} (down/fluff), {金品|きんぴん} (money and valuables), {局長|きょくちょう} (bureau chief), {介護士|かいごし} (care worker), {到着口|とうちゃくぐち} (arrival gate), {入門者|にゅうもんしゃ} (beginner), {舞茸|まいたけ} (maitake mushroom), ミンチ (minced meat), {古典芸能|こてんげいのう} (classical performing arts), {練|ね}り{物|もの} (fish paste products), {戦友|せんゆう} (comrade-in-arms), インディーズ (indie), {恩義|おんぎ} (debt of gratitude)
- **Noun/Suru verbs (7)**: {破滅|はめつ} (ruin), {色落|いろお}ち (color fading), {予行演習|よこうえんしゅう} (rehearsal), {勤続|きんぞく} (continuous service), {貸付|かしつけ} (lending), {熱愛|ねつあい} (passionate love), {転写|てんしゃ} (transcription)
- **Na-adjectives (3)**: {険悪|けんあく} (hostile), {全国的|ぜんこくてき} (nationwide), {先進的|せんしんてき} (advanced)
- **Verbs (2)**: {依存|いぞん}する (to depend on), {尋問|じんもん}する (to interrogate)
- **Other (4)**: {弱虫|よわむし} (coward/wimp), {作|つく}りたて (freshly made), {恋|こい}に{落|お}ちる (to fall in love), {二足|にそく}のわらじ (wearing two hats)
- Removed 30 candidates that now exist as entries

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 520)
Added 30 new dictionary entries (IDs 19978-20007) from candidate_words.json. Practical vocabulary for intermediate learners covering daily life, business, culture, and general knowledge.

- **Nouns (18)**: {保証人|ほしょうにん} (guarantor), {靴|くつ}べら (shoehorn), {既製服|きせいふく} (ready-made clothing), {三輪車|さんりんしゃ} (tricycle), {中高年|ちゅうこうねん} (middle-aged/older), {忍耐力|にんたいりょく} (perseverance), {色素|しきそ} (pigment), {建具|たてぐ} (fittings), {拡声器|かくせいき} (loudspeaker), {電圧|でんあつ} (voltage), {借家|しゃっか} (rented house), フレーズ (phrase), コレクター (collector), {縫|ぬ}い{物|もの} (sewing), {根絶|ねだ}やし (eradication), {取|と}りまとめ (compilation), {隔年|かくねん} (every other year), {終幕|しゅうまく} (final act)
- **Noun/Suru verbs (3)**: {総動員|そうどういん} (full mobilization), {援護|えんご} (support/cover), {裁断|さいだん} (cutting fabric)
- **Verbs (3)**: {据|す}え{付|つ}ける (to install), {叩|たた}きつける (to slam), {同伴|どうはん}する (to accompany)
- **Noun/No-adjective (3)**: {不屈|ふくつ} (indomitable), {自信満々|じしんまんまん} (full of confidence), {加糖|かとう} (sweetened)
- **Adverb (1)**: {戦々恐々|せんせんきょうきょう} (trembling with fear)
- **Expression (1)**: {雲泥|うんでい}の{差|さ} (world of difference)
- **Other (1)**: {法令遵守|ほうれいじゅんしゅ} (legal compliance)
- Removed 30 candidates that now exist as entries

### 2026-03-27 (Vocabulary Expansion - 30 New Entries, Session 519)
Added 30 new dictionary entries (IDs 19948-19977) from candidate_words.json. Diverse mix of useful vocabulary for intermediate learners covering society, culture, food, nature, and everyday life.

- **Nouns (26)**: {存在感|そんざいかん} (presence), {闘病|とうびょう} (fighting illness), {対談|たいだん} (dialogue), {休講|きゅうこう} (cancelled class), {鍋料理|なべりょうり} (hot pot), {線香花火|せんこうはなび} (sparkler), {記者会見|きしゃかいけん} (press conference), {完成度|かんせいど} (level of polish), {安堵感|あんどかん} (sense of relief), {強敵|きょうてき} (formidable enemy), {田舎暮|いなかぐ}らし (country living), {逆流|ぎゃくりゅう} (backflow), {準備万端|じゅんびばんたん} (fully prepared), {船旅|ふなたび} (boat trip), {格差社会|かくさしゃかい} (stratified society), {親|した}しみ (affection), {兵役|へいえき} (military service), {大流行|だいりゅうこう} (huge craze), {着脱|ちゃくだつ} (putting on/taking off), {振袖|ふりそで} (long-sleeved kimono), {小鉢|こばち} (small bowl/side dish), {密林|みつりん} (jungle), {弾|はず}み (momentum), {偏向|へんこう} (bias), {砂丘|さきゅう} (sand dune), {退位|たいい} (abdication)
- **Nouns/Verbal nouns (2)**: {独走|どくそう} (running alone), {仕入先|しいれさき} (supplier)
- **Na-adjective (1)**: {視覚的|しかくてき} (visual)
- **Noun/Na-adjective (1)**: {非効率|ひこうりつ} (inefficient)
- Removed 30 candidates that now exist as entries

### 2026-03-27 (Vocabulary Expansion - 30 New Entries, Session 518)
Added 30 new dictionary entries (IDs 19918-19947) from candidate_words.json. Diverse mix of useful vocabulary for intermediate learners including adjectives, onomatopoeia, cultural terms, and common nouns/expressions.

- **Na-adjectives (2)**: {大|おお}げさ (exaggerated), {奇抜|きばつ} (outlandish)
- **Nouns (13)**: {河口|かこう} (river mouth), {通行止|つうこうど}め (road closure), {下半期|しもはんき} (second half of year), {大衆|たいしゅう}{文化|ぶんか} (pop culture), {望郷|ぼうきょう} (homesickness), {根源|こんげん} (root/source), {書|か}き{初|ぞ}め (New Year's calligraphy), {食券|しょっけん} (meal ticket), {大詰|おおづ}め (final stage), {地声|じごえ} (natural voice), {高波|たかなみ} (high waves), {高音|こうおん} (high pitch), {写真集|しゃしんしゅう} (photo book)
- **Noun/Suru verbs (5)**: {率先|そっせん} (taking initiative), {気絶|きぜつ} (fainting), {堂々巡|どうどうめぐ}り (going in circles), {酷似|こくじ} (striking resemblance), {一新|いっしん} (complete renewal)
- **Expressions (2)**: {目|め}が{回|まわ}る (dizzy/swamped), {要領|ようりょう}がいい (resourceful)
- **Onomatopoeia/Adverbs (3)**: ぱらぱら (scattered), {続|つづ}けざま (in succession), がっしり (solidly built)
- **Other (5)**: {甘|あま}えん{坊|ぼう} (spoiled child), {市立|しりつ} (municipal), {春分|しゅんぶん} (spring equinox), {未亡人|みぼうじん} (widow)
- Removed 30 candidates that now exist as entries

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
