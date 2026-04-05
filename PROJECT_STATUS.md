# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-04
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

### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 18)
Added 30 new dictionary entries (IDs 22222-22251) from candidate_words.json. A broad mix of adverbs, expressions, and nouns covering grammar, daily life, politics, culture, finance, and more.

- **Adverbs (4)**: {同時|どうじ}に (at the same time), まっしぐら (headlong), そそくさと (hurriedly), とりたてて (particularly)
- **Expressions (6)**: たびに (every time), あっけにとられる (to be dumbfounded), {具合|ぐあい}が{悪|わる}い (to feel unwell), {失礼|しつれい}ですが (excuse me but), {目|め}を{向|む}ける (to turn attention to), {軌道|きどう}に{乗|の}る (to get on track), {胸|むね}に{秘|ひ}める (to keep in one's heart)
- **Na-adjective (1)**: {進歩的|しんぽてき} (progressive)
- **Nouns (19)**: {値下|ねさ}がり (price drop), {買|か}い{物袋|ものぶくろ} (shopping bag), ごみ{袋|ぶくろ} (trash bag), {転入|てんにゅう} (moving in/transfer), {代案|だいあん} (alternative plan), {被疑者|ひぎしゃ} (suspect), {通達|つうたつ} (official directive), {湯上|ゆあ}がり (after a bath), {自嘲|じちょう} (self-mockery), {休眠|きゅうみん} (dormancy), {岩盤|がんばん} (bedrock), {共和制|きょうわせい} (republic), {表現|ひょうげん}の{自由|じゆう} (freedom of expression), {吟醸酒|ぎんじょうしゅ} (ginjo sake), {枝葉|えだは} (branches and leaves), {鉱石|こうせき} (ore), {貼付|ちょうふ} (affixing), {定期預金|ていきよきん} (time deposit)

### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 17)
Added 30 new dictionary entries (IDs 22192-22221) from candidate_words.json. A diverse mix of nouns, an i-adjective, an adverb, and a loanword covering politics, work culture, religion, environment, language, society, fashion, food, sports, and more.

- **Adverb (1)**: あれこれ (this and that)
- **I-adjective (1)**: みっともない (shameful, embarrassing)
- **Loanword (1)**: フーディー (hoodie)
- **Nouns (27)**: {菜食|さいしょく} (vegetarian diet), {餞別|せんべつ} (farewell gift), {行進|こうしん} (march), {高温多湿|こうおんたしつ} (hot and humid), {労働時間|ろうどうじかん} (working hours), {機長|きちょう} (aircraft captain), {投票率|とうひょうりつ} (voter turnout), {毒性|どくせい} (toxicity), {識者|しきしゃ} (expert), {戒律|かいりつ} (religious precepts), {貨物船|かもつせん} (cargo ship), {新体操|しんたいそう} (rhythmic gymnastics), {人名|じんめい} (personal name), {投票所|とうひょうじょ} (polling place), {期限内|きげんない} (within deadline), {単色|たんしょく} (monochrome), {前記|ぜんき} (aforementioned), {美観|びかん} (scenic beauty), {雲散霧消|うんさんむしょう} (vanishing without trace), {超過勤務|ちょうかきんむ} (overtime work), {霊感|れいかん} (spiritual sensitivity), {共助|きょうじょ} (mutual assistance), {相互扶助|そうごふじょ} (mutual aid), {交通安全|こうつうあんぜん} (traffic safety), {粉|ふん}じん (dust/particulate), {上述|じょうじゅつ} (aforementioned), {注記|ちゅうき} (annotation)
- 1 new kanji (餞) assigned ID 02654

### 2026-04-05 (Vocabulary Expansion - 23 New Entries, Session 16)
Added 23 new dictionary entries (IDs 22169-22191) from candidate_words.json. Focused on useful vocabulary for intermediate learners, with a mix of suru verbs, expressions, and nouns covering everyday life, communication, society, and keigo.

- **Suru verbs (15)**: {帰宅|きたく}する (to return home), {解放|かいほう}する (to release), {矛盾|むじゅん}する (to contradict), {対立|たいりつ}する (to oppose), {連続|れんぞく}する (to continue in succession), {辛抱|しんぼう}する (to be patient), {視聴|しちょう}する (to watch media), {装着|そうちゃく}する (to equip), {美化|びか}する (to beautify), {頻発|ひんぱつ}する (to occur frequently), {突出|とっしゅつ}する (to protrude/excel), {工夫|くふう}する (to devise), {浸透|しんとう}する (to permeate), {普及|ふきゅう}する (to spread), {達成|たっせい}する (to achieve)
- **Nouns (2)**: {古書店|こしょてん} (used bookstore), お{名前|なまえ} (name, polite)
- **Expressions (5)**: {頼|たよ}りにする (to rely on), さよなら (goodbye), {場|ば}を{和|なご}ませる (to lighten the mood), お{会|あ}いする (to meet, humble), {誹謗|ひぼう}する (to slander)
- **Pre-noun adjectival (1)**: ただの (mere, just)

### 2026-04-05 (Vocabulary Expansion - 24 New Entries, Session 15)
Added 24 new dictionary entries (IDs 22145-22168) from candidate_words.json. A diverse mix of verbs, nouns, and adjectives covering daily life, education, personality, society, and culture.

- **Verbs (10)**: {禁止|きんし}する (to prohibit), {実行|じっこう}する (to execute), {通学|つうがく}する (to commute to school), {誇張|こちょう}する (to exaggerate), {完備|かんび}する (to be fully equipped), {登園|とうえん}する (to go to kindergarten), ちゃっかりする (to be shrewd), {発売|はつばい}{開始|かいし}する (start of sales), {臨場|りんじょう}する (to be present at scene), {包摂|ほうせつ}する (inclusion)
- **Nouns (10)**: {受|う}け{入|い}れ (acceptance), {���頭|こうとう}{試験|しけん} (oral exam), {髪染|かみぞ}め (hair dye), {時事|じじ}{問題|もんだい} (current affairs), {後部|こうぶ}{座席|ざせき} (back seat), {研究生|けんきゅうせい} (research student), {屋上|おくじょう}{庭園|ていえん} (rooftop garden), {改良|かいりょう}{型|がた} (improved model), {武勇|ぶゆう} (bravery in battle), {餅肌|もちはだ} (smooth skin)
- **Noun/adjective (4)**: {天真爛漫|てんしんらんまん} (innocent and cheerful), {勇猛|ゆうもう} (brave and fierce), {豪胆|ごうたん} (bold/daring), {狭隘|きょうあい} (narrow/cramped)
- 1 new kanji (隘) assigned ID 02653

### 2026-04-05 (Vocabulary Expansion - 28 New Entries, Session 14)
Added 28 new dictionary entries (IDs 22087-22114) from candidate_words.json. A practical mix covering daily life, education, culture, technology, social behavior, and body-related vocabulary.

- **Nouns (16)**: {施錠|せじょう} (locking), {館内|かんない} (inside the building), {入店|にゅうてん} (entering a store), {紙切|かみき}れ (scrap of paper), {日記帳|にっきちょう} (diary), {胸元|むなもと} (chest area), {喉元|のどもと} (throat), {翻訳者|ほんやくしゃ} (translator), {購読者|こうどくしゃ} (subscriber), {学習者|がくしゅうしゃ} (learner), {文学賞|ぶんがくしょう} (literary prize), {新人賞|しんじんしょう} (newcomer award), {外付|そとづ}け (external), {本場物|ほんばもの} (authentic article), {反目|はんもく} (discord), {型番|かたばん} (model number), {首席|しゅせき} (top rank), {礼拝堂|れいはいどう} (chapel), {選択式|せんたくしき} (multiple-choice), {流転|るてん} (constant change), {走破|そうは} (completing a course), {鑑定士|かんていし} (appraiser), {雨|あま}よけ (rain shelter), マウンティング (one-upmanship)
- **Na-adjective (1)**: ロマンチック (romantic)
- **Verb (1)**: {書|か}き{損|そこ}ねる (to fail to write)
- **Expressions (2)**: {相性|あいしょう}がいい (compatible), {頭|あたま}の{回転|かいてん}が{速|はや}い (quick-witted)

### 2026-04-04 (Vocabulary Expansion - 30 New Entries, Session 13)
Added 30 new dictionary entries (IDs 22057-22086) from candidate_words.json. A diverse mix covering pronouns, adverbs, nouns, verbs, and expressions spanning daily life, education, business, politics, science, health, and more.

- **Pronoun (1)**: いずれか (one or the other)
- **Adverbs (4)**: {名目上|めいもくじょう} (nominally), {一遍|いっぺん} (once/all at once), {形式上|けいしきじょう} (formally/on paper), {何月|なんがつ} (what month)
- **Verbs (1)**: {走|はし}り{続|つづ}ける (to keep running)
- **Nouns (18)**: {飲|の}みすぎ (overdrinking), {自動|じどう}{引|ひ}き{落|お}とし (automatic withdrawal), {試験|しけん}{問題|もんだい} (exam questions), {反復|はんぷく}{練習|れんしゅう} (drill practice), {全世界|ぜんせかい} (the whole world), {品質|ひんしつ}{保証|ほしょう} (quality assurance), {整形|せいけい}{外科|げか} (orthopedics), {新版|しんぱん} (new edition), {水|みず}ぶくれ (blister), {髪質|かみしつ} (hair texture), {県知事|けんちじ} (prefectural governor), {楽章|がくしょう} (musical movement), {生魚|なまざかな} (raw fish), {補欠|ほけつ}{選挙|せんきょ} (by-election), {設問|せつもん} (question on a test), {走行中|そうこうちゅう} (while driving), {訴求力|そきゅうりょく} (appeal/persuasive power), {水栓|すいせん} (water faucet), マグマ (magma), {昇級|しょうきゅう} (promotion in rank)
- **Expressions (4)**: {一度|いちど}きり (only once), {以前|いぜん}{通|どお}り (as before), {今|いま}まで{通|どお}り (as usual), {着想|ちゃくそう}を{得|え}る (to get an idea)



