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

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 524)
Added 30 new dictionary entries (IDs 20088-20117) from candidate_words.json. Diverse vocabulary covering academic, cultural, nature, daily life, and abstract concepts. Also removed 25 stale candidates (する forms of existing entries).

- **Academic/Technical (4)**: {考古学|こうこがく} (archaeology), {含有|がんゆう} (containing), {内包|ないほう} (encompassing), {微小|びしょう} (minute)
- **Nature/Color (4)**: {青葉|あおば} (fresh green leaves), {藍|あい} (indigo), {朱色|しゅいろ} (vermillion), {火炎|かえん} (flame)
- **Communication (4)**: {談話|だんわ} (conversation/statement), {書簡|しょかん} (letter), {交信|こうしん} (radio contact), {歌声|うたごえ} (singing voice)
- **Work/Society (4)**: {後継|こうけい} (successor), {前任|ぜんにん} (predecessor), {苦境|くきょう} (predicament), {総力|そうりょく} (total effort)
- **Safety/Military (3)**: {退避|たいひ} (evacuation), {弾薬|だんやく} (ammunition), {投棄|とうき} (dumping)
- **Daily Life/Materials (5)**: {布地|ぬのじ} (fabric), {綿花|めんか} (raw cotton), {綿棒|めんぼう} (cotton swab), {飲茶|やむちゃ} (dim sum), {熱々|あつあつ} (piping hot)
- **Abstract (3)**: {一線|いっせん} (front line/boundary), {腹立|はらだ}ち (anger), {平面|へいめん} (flat surface)
- **Other (3)**: {醜態|しゅうたい} (disgraceful behavior), {加護|かご} (divine protection), {直射|ちょくしゃ} (direct rays)

### 2026-03-28 (Vocabulary Expansion - 20 New Entries, Session 523)
Added 20 new dictionary entries (IDs 20068-20087) from candidate_words.json. Focus on practical expressions, useful verbs, and common words for intermediate learners.

- **Expressions (7)**: {心|こころ}を{打|う}つ (to move deeply), {耳|みみ}を{貸|か}す (to lend an ear), {身|み}を{引|ひ}く (to step aside), {鼻|はな}をかむ (to blow one's nose), {手|て}を{繋|つな}ぐ (to hold hands), {元|もと}に{戻|もど}る (to return to original state), {弁|べん}が{立|た}つ (to be eloquent)
- **Nouns (3)**: {衰|おとろ}え (decline), {様相|ようそう} (aspect), {初志|しょし} (original intention), {露見|ろけん} (exposure)
- **Verbs (4)**: {上下|じょうげ}する (to rise and fall), {仕分|しわ}ける (to sort), {割|わ}り{振|ふ}る (to assign), ぶち{込|こ}む (to throw in), もぎ{取|と}る (to pluck off)
- **Adverbs (2)**: あれほど (that much), {多少|たしょう}とも (to some extent)
- **Other (1)**: {渡米|とべい}する (to go to America)
- Removed 20 candidates that now exist as entries

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
