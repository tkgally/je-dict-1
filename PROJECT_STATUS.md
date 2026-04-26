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

### 2026-04-25 (Vocabulary Expansion - 30 New Entries, Batch 41)
Added 30 new dictionary entries (IDs 25496-25525) from candidate_words.json. Focused on useful vocabulary across business, law, government, food, medicine, and daily life.

- **Suru verbs (15)**: {優勝|ゆうしょう}する (to win championship), {成立|せいりつ}する (to be established), {執行|しっこう}する (to execute/enforce), {解任|かいにん}する (to dismiss from office), {予言|よげん}する (to prophesy), メモする (to take notes), {焙煎|ばいせん}する (to roast beans), {潜伏|せんぷく}する (to lie hidden), {充血|じゅうけつ}する (to become bloodshot), {戦慄|せんりつ}する (to shudder), {扇動|せんどう}する (to agitate/incite), {咀嚼|そしゃく}する (to chew/digest mentally), {妄信|もうしん}する (to believe blindly), {報連相|ほうれんそう}する (report-contact-consult), {抗弁|こうべん} (objection/plea)
- **Na-adjectives (3)**: {重大|じゅうだい}な (serious/grave), {十分|じゅうぶん}な (sufficient), {構造的|こうぞうてき}な (structural)
- **Verbs (3)**: {撮|と}り{直|なお}す (to retake photo), {困|こま}らせる (to cause trouble), {爪|つめ}を{噛|か}む (to bite nails)
- **Nouns (9)**: {機能性|きのうせい} (functionality), {市場調査|しじょうちょうさ} (market research), {慰霊碑|いれいひ} (memorial monument), {白色|はくしょく} (white color), {登記簿|とうきぼ} (registry), {秘書官|ひしょかん} (executive secretary), {卸売|おろしうり}{市場|しじょう} (wholesale market), {捧|ささ}げ{物|もの} (offering), {世渡|よわた}り{下手|べた} (social ineptness)
- Conjugation tables auto-generated for all 17 verb entries
- 29 candidates synced from candidate list

Total entries: 25,288 → 25,318.

### 2026-04-25 (Vocabulary Expansion - 30 New Entries, Batch 40)
Added 30 new dictionary entries (IDs 25466-25495) from candidate_words.json. Diverse batch covering everyday vocabulary, modern slang, medical/scientific terms, cultural items, and practical expressions.

- **Nouns (21)**: {故郷|ふるさと} (hometown), {顔色|かおいろ} (complexion/expression), お{昼寝|ひるね} (afternoon nap), {映|ば}え (photogenic/Instagram-worthy), {子豚|こぶた} (piglet), {塩味|しおみ} (salty flavor), {空色|そらいろ} (sky blue), {器量|きりょう} (looks/caliber), {秘策|ひさく} (secret plan), {物品|ぶっぴん} (goods), {心拍|しんぱく} (heartbeat), {本編|ほんぺん} (main story), {牧草|ぼくそう} (pasture grass), {親鳥|おやどり} (parent bird), {胃炎|いえん} (gastritis), {柄杓|ひしゃく} (ladle/dipper), {石灰|せっかい} (lime), {瞬|またた}き (blink/twinkle), {利己主義|りこしゅぎ} (egoism), {住処|すみか} (dwelling/habitat), {気球|ききゅう} (hot-air balloon)
- **Na-adjective (1)**: {無害|むがい} (harmless)
- **Suru verbs (5)**: {誘惑|ゆうわく}する (to tempt), {再婚|さいこん}する (to remarry), {算定|さんてい}する (to calculate), {密会|みっかい}する (to meet secretly), {離席|りせき}する (to leave one's seat)
- **Noun/Verb-suru (2)**: {隆起|りゅうき} (uplift), {分泌|ぶんぴつ} (secretion)
- **Expression (1)**: あっという{間|ま}に (in the blink of an eye)
- Cross-references added for variant readings ({故郷|ふるさと}↔{故郷|こきょう}, {塩味|しおみ}↔{塩味|しおあじ}, {瞬|またた}き↔まばたき)
- 1 new kanji added to kanji index: {泌|ぴつ}
- 30 candidates synced from candidate list

Total entries: 25,258 → 25,288.

### 2026-04-25 (Vocabulary Expansion - 28 New Entries, Batch 39)
Added 28 new dictionary entries (IDs 25438-25465) from candidate_words.json. Diverse batch covering practical vocabulary across work/society, health, commerce, culture, science, law, and daily life.

- **Nouns (24)**: {人手|ひとで} (manpower), {働|はたら}き{方|かた} (work style), {育児|いくじ}{休業|きゅうぎょう} (childcare leave), {偏頭痛|へんずつう} (migraine), {購入者|こうにゅうしゃ} (purchaser), {生産者|せいさんしゃ} (producer), {追加|ついか}{費用|ひよう} (additional cost), {予防法|よぼうほう} (prevention method), {深夜|しんや}バス (night bus), スヌーズ (snooze), {主流派|しゅりゅうは} (mainstream faction), {力学|りきがく} (mechanics/dynamics), {筆名|ひつめい} (pen name), ペンネーム (pen name), {報復|ほうふく}{措置|そち} (retaliatory measures), {著作権|ちょさくけん}{侵害|しんがい} (copyright infringement), {和食店|わしょくてん} (Japanese restaurant), {金封|きんぷう} (gift envelope), {度付|どつ}き (prescription glasses), {解剖学|かいぼうがく} (anatomy), {犯罪学|はんざいがく} (criminology), {粘着性|ねんちゃくせい} (adhesiveness), {床材|ゆかざい} (flooring material), {床板|ゆかいた} (floorboard), {電磁気|でんじき} (electromagnetism), {遠征隊|えんせいたい} (expedition)
- **Expressions (2)**: {愚痴|ぐち}を{言|い}う (to complain), {不平|ふへい}を{言|い}う (to express dissatisfaction)
- Cross-references added between synonym/related pairs
- 28 candidates synced from candidate list

Total entries: 25,230 → 25,258.

### 2026-04-25 (Vocabulary Expansion - 30 New Entries, Batch 38)
Added 30 new dictionary entries (IDs 25408-25437) from candidate_words.json. Diverse batch covering everyday verbs, common expressions, nouns, adverbs, and an adjective across business, education, culture, and daily life.

- **Suru verbs (4)**: {参加|さんか}する (to participate), {入社|にゅうしゃ}する (to join a company), {泣|な}き{寝入|ねい}りする (to accept defeat silently), {社会参加|しゃかいさんか} (social participation)
- **Expressions (4)**: お{世話|せわ}になる (to be indebted to), {身|み}を{捧|ささ}げる (to devote oneself), これ{以上|いじょう} (any more/further), {大|たい}したことない (not a big deal)
- **Nouns (14)**: {実験室|じっけんしつ} (laboratory), {判断基準|はんだんきじゅん} (judgment criteria), {経験不足|けいけんぶそく} (lack of experience), {宿泊先|しゅくはくさき} (accommodation), {大波|おおなみ} (big wave), {研究会|けんきゅうかい} (study group), {大枠|おおわく} (broad outline), {韓国語|かんこくご} (Korean language), あぐら (sitting cross-legged), {冷|つめ}たさ (coldness), {演奏者|えんそうしゃ} (performer), {差分|さぶん} (difference), {家族愛|かぞくあい} (family love), {音訓|おんくん} (on/kun readings)
- **Noun/Na-adjective (1)**: {親不孝|おやふこう} (unfilial conduct)
- **Na-adjective (1)**: リズミカル (rhythmic)
- **Adverbs (2)**: {変|か}わらず (unchanged), たやすく (easily)
- **Nouns (additional, meetings)**: {討論会|とうろんかい} (debate forum), {範囲内|はんいない} (within range), {感情表現|かんじょうひょうげん} (emotional expression), {機関車|きかんしゃ} (locomotive)
- 30 candidates synced from candidate list

Total entries: 25,200 → 25,230.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
