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

### 2026-04-04 (Vocabulary Expansion - 30 New Entries, Session 13)
Added 30 new dictionary entries (IDs 22057-22086) from candidate_words.json. A diverse mix covering pronouns, adverbs, nouns, verbs, and expressions spanning daily life, education, business, politics, science, health, and more.

- **Pronoun (1)**: いずれか (one or the other)
- **Adverbs (4)**: {名目上|めいもくじょう} (nominally), {一遍|いっぺん} (once/all at once), {形式上|けいしきじょう} (formally/on paper), {何月|なんがつ} (what month)
- **Verbs (1)**: {走|はし}り{続|つづ}ける (to keep running)
- **Nouns (18)**: {飲|の}みすぎ (overdrinking), {自動|じどう}{引|ひ}き{落|お}とし (automatic withdrawal), {試験|しけん}{問題|もんだい} (exam questions), {反復|はんぷく}{練習|れんしゅう} (drill practice), {全世界|ぜんせかい} (the whole world), {品質|ひんしつ}{保証|ほしょう} (quality assurance), {整形|せいけい}{外科|げか} (orthopedics), {新版|しんぱん} (new edition), {水|みず}ぶくれ (blister), {髪質|かみしつ} (hair texture), {県知事|けんちじ} (prefectural governor), {楽章|がくしょう} (musical movement), {生魚|なまざかな} (raw fish), {補欠|ほけつ}{選挙|せんきょ} (by-election), {設問|せつもん} (question on a test), {走行中|そうこうちゅう} (while driving), {訴求力|そきゅうりょく} (appeal/persuasive power), {水栓|すいせん} (water faucet), マグマ (magma), {昇級|しょうきゅう} (promotion in rank)
- **Expressions (4)**: {一度|いちど}きり (only once), {以前|いぜん}{通|どお}り (as before), {今|いま}まで{通|どお}り (as usual), {着想|ちゃくそう}を{得|え}る (to get an idea)

### 2026-04-04 (Vocabulary Expansion - 30 New Entries, Session 12)
Added 30 new dictionary entries (IDs 22027-22056) from candidate_words.json. A diverse mix covering verbs, adjectives, nouns spanning culture, education, finance, science, and daily life.

- **Verbs (4)**: {貫徹|かんてつ}する (to carry out thoroughly), {貫|つらぬ}き{通|とお}す (to persist with), {退役|たいえき}する (to retire from military), {祈祷|きとう}する (to pray/invoke)
- **I-adjective (1)**: {秩序正|ちつじょただ}しい (orderly/well-disciplined)
- **Nouns (25)**: {悲観主義|ひかんしゅぎ} (pessimism), {漫才師|まんざいし} (manzai comedian), {茜色|あかねいろ} (madder red), {緋色|ひいろ} (scarlet), {謝金|しゃきん} (honorarium), {謝恩会|しゃおんかい} (thank-you party), {定常|ていじょう} (steady/stable), {敷地内|しきちない} (inside the premises), {作業台|さぎょうだい} (workbench), {底面|ていめん} (bottom surface), {多層|たそう} (multi-layered), {各部|かくぶ} (each section), {編入生|へんにゅうせい} (transfer student), {下校時間|げこうじかん} (school dismissal time), {女子校|じょしこう} (girls' school), {使用期限|しようきげん} (use-by date), {自然選択|しぜんせんたく} (natural selection), {慰労金|いろうきん} (consolation money), {歩合給|ぶあいきゅう} (commission pay), {水上|すいじょう}バス (water bus), {出願書類|しゅつがんしょるい} (application documents), {不戦条約|ふせんじょうやく} (non-aggression pact), {編入試験|へんにゅうしけん} (transfer exam), {最高値|さいこうね} (highest price), {最高額|さいこうがく} (highest amount)
- 2 new kanji (緋, 茜) assigned IDs 02651-02652
- Removed 2 stale candidates (極寒 ごくかん — variant of existing ごっかん, 共存 きょうそん — variant of existing きょうぞん)

### 2026-04-04 (Vocabulary Expansion - 28 New Entries, Session 11)
Added 28 new dictionary entries (IDs 21999-22026) from candidate_words.json. A diverse mix of nouns covering food culture, geography, military/politics, science, traditional culture, and daily life.

- **Nouns (28)**: {突|つ}き{出|だ}し (appetizer at izakaya), {祟|たた}り (curse/divine punishment), {兵力|へいりょく} (military strength), {極地|きょくち} (polar region), {青物|あおもの} (green vegetables), {終発|しゅうはつ} (last departure), {同盟国|どうめいこく} (allied nation), {病死|びょうし} (death from illness), {白髪染|しらがぞ}め (gray hair dye), {落下物|らっかぶつ} (falling object), {冥土|めいど} (the underworld), {餌|えさ}やり (feeding animals), {軍備|ぐんび} (armaments), {微粒子|びりゅうし} (fine particle), {宗家|そうけ} (head family/founding school), {溶媒|ようばい} (solvent), {伝令|でんれい} (messenger), {棒状|ぼうじょう} (rod-shaped), {利他主義|りたしゅぎ} (altruism), {一升|いっしょう} (one shou/1.8L), {術策|じゅっさく} (stratagem), {斜|なな}め{前|まえ} (diagonally in front), {週例|しゅうれい} (weekly), {野外活動|やがいかつどう} (outdoor activities), {造幣局|ぞうへいきょく} (the mint), {鼎談|ていだん} (three-person discussion), {藻類|そうるい} (algae), {観賞用|かんしょうよう} (ornamental)
- 2 new kanji (祟, 鼎) assigned IDs 02649-02650
- Removed 2 stale candidates (はしご — duplicate of 梯子, 打消し — variant of 打ち消し)

### 2026-04-04 (Vocabulary Expansion - 15 New Entries, Session 10)
Added 15 new dictionary entries (IDs 21984-21998) from candidate_words.json. All are commonly used する verbs covering everyday activities and professional contexts.

- **Suru verbs (15)**: {交差|こうさ}する (to intersect), {沸騰|ふっとう}する (to boil), {監督|かんとく}する (to supervise/direct), {運営|うんえい}する (to operate/run), {応援|おうえん}する (to cheer/support), {観察|かんさつ}する (to observe), {撮影|さつえい}する (to photograph/film), {編集|へんしゅう}する (to edit), {了解|りょうかい}する (to understand/acknowledge), {批判|ひはん}する (to criticize), {指揮|しき}する (to command/conduct), {渡航|とこう}する (to travel overseas), {経過|けいか}する (to pass/elapse), {箱詰|はこづ}めする (to pack in a box), ノックする (to knock)
- Removed 15 candidates that now exist as entries
- Skipped 極寒 (ごくかん, variant of existing ごっかん) and 共存 (きょうそん, variant of existing きょうぞん)

### 2026-04-04 (Vocabulary Expansion - 30 New Entries, Session 9)
Added 30 new dictionary entries (IDs 21954-21983) from candidate_words.json. A diverse mix of nouns, adjectives, verbs, adverbs, and expressions useful for intermediate learners.

- **Nouns (14)**: {水面下|すいめんか} (below the surface), {諸事情|しょじじょう} (various circumstances), {距離感|きょりかん} (sense of distance), {心底|しんそこ} (bottom of one's heart), {幻影|げんえい} (phantom/illusion), {外圧|がいあつ} (external pressure), {攻略法|こうりゃくほう} (strategy/walkthrough), {防止策|ぼうしさく} (preventive measure), {顛末|てんまつ} (full account), {内幕|うちまく} (inside story), {真実味|しんじつみ} (truthfulness), {善行|ぜんこう} (good deed), {包|つつ}み{紙|がみ} (wrapping paper), {風刺画|ふうしが} (satirical cartoon), {巻末|かんまつ} (end of book), {独自性|どくじせい} (originality)
- **Na-adjectives (3)**: {善良|ぜんりょう} (good-natured), {秀逸|しゅういつ} (excellent), {漸進的|ぜんしんてき} (gradual), {珍妙|ちんみょう} (odd/bizarre)
- **Verbs (4)**: よろよろする (to totter), {書|か}き{間違|まちが}える (to write incorrectly), {振|ふ}り{回|まわ}される (to be bossed around), {素潜|すもぐ}り (free diving)
- **Noun/verb-suru (3)**: {無理強|むりじ}い (forcing/coercion), {配置換|はいちが}え (reassignment)
- **Other (3)**: {果|は}てしない (boundless — i-adj), {順々|じゅんじゅん}に (in turn — adverb), {尾|お}ひれがつく (to be exaggerated — expression), かるた (karuta card game)
- 1 new kanji (顛) assigned ID 02648
- Removed 6 stale candidates (duplicates of existing entries)


