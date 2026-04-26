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

### 2026-04-26 (Vocabulary Expansion - 30 New Entries, Batch 47)
Added 30 new dictionary entries (IDs 25666-25695) from candidate_words.json. Practical, learner-friendly vocabulary covering daily life, business, environment, sports, food, and communication.

- **Daily life (7)**: {雨降|あめふ}り (rainfall), へこみ (dent/setback), {抜|ぬ}け{毛|げ} (hair loss), {空|あ}き{時間|じかん} (free time), {早歩|はやある}き (brisk walking), シャーペン (mechanical pencil), フロントガラス (windshield)
- **Time/intensity (3)**: {今|いま}すぐ (right now), {急上昇|きゅうじょうしょう} (sharp rise), {急降下|きゅうこうか} (sharp drop)
- **Business/society (6)**: {前金|まえきん} (advance payment), {離席|りせき}する (to step away), {危機|きき}{管理|かんり} (crisis management), {社会|しゃかい}{問題|もんだい} (social problem), {誘致|ゆうち} (attraction/bidding), {連絡係|れんらくがかり} (liaison)
- **Loanwords (5)**: ジェスチャー (gesture), セロリ (celery), リユース (reuse), カヌー (canoe), トラブルメーカー (troublemaker)
- **Other (9)**: {先回|さきまわ}り (preemption), {全速力|ぜんそくりょく} (full speed), {分|わ}け{前|まえ} (share/portion), ビジネスホテル (business hotel), {大中小|だいちゅうしょう} (L/M/S), {強|つよ}さ (strength), {寄付者|きふしゃ} (donor), {仲間|なかま}{意識|いしき} (camaraderie), {守勢|しゅせい} (defensive)
- Conjugation tables auto-generated for 7 suru verb entries
- 30 candidates synced from candidate list

Total entries: 25,458 → 25,488.

### 2026-04-26 (Vocabulary Expansion - 20 New Entries, Batch 46)
Added 20 new dictionary entries (IDs 25646-25665) from candidate_words.json. Mixed batch covering Japanese culture, everyday expressions, business/economics, food/drink, sports, and daily life.

- **Cultural (3)**: {天下|あまくだ}り (amakudari - bureaucratic parachuting), {純米酒|じゅんまいしゅ} (pure rice sake), {大吟醸|だいぎんじょう} (premium ginjo sake)
- **Expressions (3)**: {目|め}を{合|あ}わせる (to make eye contact), {好|す}き{放題|ほうだい} (doing as one pleases), そのままにする (to leave as is)
- **Business/Economics (4)**: {銀行|ぎんこう}{振込|ふりこみ} (bank transfer), {占有率|せんゆうりつ} (market share), {輸出国|ゆしゅつこく} (exporting country), {輸入国|ゆにゅうこく} (importing country)
- **Nouns (6)**: {準々決勝|じゅんじゅんけっしょう} (quarterfinal), {猿芝居|さるしばい} (transparent sham), {工場長|こうじょうちょう} (factory manager), {肉片|にくへん} (piece of meat), {中米|ちゅうべい} (Central America), {拭|ふ}き{取|と}り (wiping off)
- **Verb (1)**: {苛立|いらだ}たせる (to irritate)
- **Other (3)**: {遊歩|ゆうほ} (strolling), ポロシャツ (polo shirt), {満々|まんまん} (brimming with)
- Conjugation tables auto-generated for 4 verb entries (2 ichidan, 2 suru)
- 20 candidates synced from candidate list

Total entries: 25,438 → 25,458.

### 2026-04-26 (Vocabulary Expansion - 30 New Entries, Batch 45)
Added 30 new dictionary entries (IDs 25616-25645) from candidate_words.json. Diverse batch covering education, business, food, daily life, culture, and expressions useful for intermediate learners.

- **Nouns (18)**: {吟醸|ぎんじょう} (ginjo sake), {体験談|たいけんだん} (personal experience story), {業務連絡|ぎょうむれんらく} (business notice), {自己都合|じこつごう} (personal reasons), {時間管理|じかんかんり} (time management), {食品添加物|しょくひんてんかぶつ} (food additive), {料理店|りょうりてん} (restaurant), {交替勤務|こうたいきんむ} (shift work), {勤続年数|きんぞくねんすう} (years of service), {落書|らくが}き{帳|ちょう} (doodle notebook), {備蓄品|びちくひん} (emergency supplies), {悪戯好|いたずらず}き (prankster), {使|つか}い (errand/messenger), {単語力|たんごりょく} (vocabulary ability), {電動工具|でんどうこうぐ} (power tool), {敗者復活戦|はいしゃふっかつせん} (repechage), {水彩絵具|すいさいえのぐ} (watercolor paint), {平方根|へいほうこん} (square root)
- **Academic disciplines (3)**: {地理学|ちりがく} (geography), {気象学|きしょうがく} (meteorology), {地質学|ちしつがく} (geology)
- **Na-adjective (1)**: {無感情|むかんじょう} (emotionless)
- **Adjective-no (1)**: {���身|なまみ}の (flesh-and-blood)
- **Expressions (4)**: {一夜漬|いちやづ}け (cramming/overnight pickling), {仲|なか}が{悪|わる}い (on bad terms), {小言|こごと}を{言|い}う (to nag), {避|さ}けられない (unavoidable)
- **Other (3)**: {走馬灯|そうまとう}のよう (life flashing before eyes), {平和活動|へいわかつどう} (peace activities), {一緒|いっしょ}に (together)
- 30 candidates synced from candidate list

Total entries: 25,408 → 25,438.

### 2026-04-26 (Vocabulary Expansion - 30 New Entries, Batch 44)
Added 30 new dictionary entries (IDs 25586-25615) from candidate_words.json. Diverse batch covering verbs, adjectives, nouns, expressions, and a pronoun across daily life, culture, business, health, nature, and more.

- **Verbs (1)**: {形作|かたちづく}る (to form/shape)
- **Suru verbs (3)**: {予約確認|よやくかくにん}する (reservation confirmation), {予約変更|よやくへんこう}する (reservation change), {詐称|さしょう}する (to misrepresent)
- **Na-adjective (1)**: {自動的|じどうてき} (automatic)
- **I-adjective (1)**: {薄明|うすあか}るい (dimly lit)
- **Pronoun (1)**: {誰|だれ}しも (everyone/anybody)
- **Nouns (17)**: {優|やさ}しさ (kindness), {韓国料理|かんこくりょうり} (Korean cuisine), ジュエリー (jewelry), {午前零時|ごぜんれいじ} (midnight), {反射神経|はんしゃしんけい} (reflexes), {鏡開|かがみびら}き (New Year mochi/sake barrel opening), {競合他社|きょうごうたしゃ} (competitor), {決定要素|けっていようそ} (decisive factor), {省資源|しょうしげん} (resource conservation), {探検者|たんけんしゃ} (explorer), {麻酔薬|ますいやく} (anesthetic), {帽子屋|ぼうしや} (hat shop), {落成式|らくせいしき} (completion ceremony), {薄明|はくめい} (twilight), {伝道師|でんどうし} (evangelist/missionary), {評伝|ひょうでん} (critical biography), {神域|しんいき} (sacred precinct), {農閑期|のうかんき} (farming off-season), {鏡面|きょうめん} (mirror surface), {警部補|けいぶほ} (assistant inspector)
- **Expressions (4)**: くしゃみが{出|で}る (to sneeze), {心|こころ}が{狭|せま}い (narrow-minded), {価値|かち}ある (valuable/worthy)
- Conjugation tables auto-generated for 4 verb entries (1 godan, 3 suru) and 1 i-adjective
- 30 candidates synced from candidate list

Total entries: 25,378 → 25,408.

### 2026-04-26 (Vocabulary Expansion - 30 New Entries, Batch 43)
Added 30 new dictionary entries (IDs 25556-25585) from candidate_words.json. Diverse batch covering adjectives, adverbs, expressions, nouns, and a verb across emotions, weather, sports, media, food, and daily life.

- **Na-adjectives (4)**: {残酷|ざんこく}な (cruel), {悲惨|ひさん}な (tragic), {哀|あわ}れな (pitiful/poignant), {緊密|きんみつ}な (close/tight)
- **Nouns (15)**: {屈伸|くっしん} (bending and stretching), {発表者|はっぴょうしゃ} (presenter), {降水確率|こうすいかくりつ} (chance of rain), {初婚|しょこん} (first marriage), さやえんどう (snow pea), {山野|さんや} (mountains and fields), {投稿欄|とうこうらん} (letters column), {気象予報|きしょうよほう} (weather forecast), {水風船|みずふうせん} (water balloon), {得点者|とくてんしゃ} (scorer), {先取点|せんしゅてん} (opening goal), {抜|ぬ}き{書|が}き (excerpt), {再婚者|さいこんしゃ} (remarried person), {投稿記事|とうこうきじ} (submitted article), {名人芸|めいじんげい} (masterful skill)
- **Nouns cont'd (5)**: {学徒|がくと} (student/scholar), {細口|ほそぐち} (narrow opening), ご{機嫌|きげん} (mood/good spirits), {事前準備|じぜんじゅんび} (advance preparation), {開店準備|かいてんじゅんび} (preparation for opening), {準備完了|じゅんびかんりょう} (preparation complete)
- **Verb (1)**: {紐付|ひもづ}ける (to link/associate)
- **Adverbs (2)**: {婉曲|えんきょく}に (indirectly/euphemistically), {偶然|ぐうぜん}に (by chance)
- **Expressions (2)**: {胸|むね}が{痛|いた}む (to feel heartache), {仲良|なかよ}くする (to get along well)
- Conjugation tables auto-generated for 5 verb entries (1 ichidan, 4 suru)
- 30 candidates synced from candidate list

Total entries: 25,348 → 25,378.

### 2026-04-25 (Vocabulary Expansion - 30 New Entries, Batch 42)
Added 30 new dictionary entries (IDs 25526-25555) from candidate_words.json. Focused on common suru verbs across diverse semantic domains, plus one na-adjective.

- **Suru verbs (29)**: {計算|けいさん}する (to calculate), {修正|しゅうせい}する (to correct/revise), {完成|かんせい}する (to complete), {発生|はっせい}する (to occur), {注目|ちゅうもく}する (to pay attention), {処理|しょり}する (to handle/process), {再開|さいかい}する (to resume), {要求|ようきゅう}する (to demand), {支援|しえん}する (to support), {制作|せいさく}する (to produce/create), {保管|ほかん}する (to store), {廃棄|はいき}する (to discard), {隔離|かくり}する (to isolate), {切断|せつだん}する (to cut off), {作用|さよう}する (to act on), {配分|はいぶん}する (to allocate), {変装|へんそう}する (to disguise), {改心|かいしん}する (to reform), {値|あたい}する (to deserve), {洗練|せんれん}する (to refine), {類似|るいじ}する (to be similar), {得点|とくてん}する (to score), {適合|てきごう}する (to conform), {奔走|ほんそう}する (to hustle), {完食|かんしょく}する (to finish eating), {多様化|たようか}する (to diversify), {撲滅|ぼくめつ}する (to eradicate), {消火|しょうか}する (to extinguish), {融解|ゆうかい}する (to melt)
- **Na-adjective (1)**: {巨大|きょだい}な (huge/gigantic)
- Conjugation tables auto-generated for all 29 suru verb entries
- 30 candidates synced from candidate list

Total entries: 25,318 → 25,348.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
