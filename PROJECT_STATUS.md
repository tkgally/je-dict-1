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

### 2026-04-25 (Vocabulary Expansion - 27 New Entries, Batch 37)
Added 27 new dictionary entries (IDs 25381-25407) from candidate_words.json. Focused on useful suru verbs, an expression, and a noun covering disaster recovery, daily life, school, workplace, and literary vocabulary.

- **Suru verbs (25)**: {復興|ふっこう}する (to reconstruct), {放置|ほうち}する (to leave as is), {変身|へんしん}する (to transform), {仮装|かそう}する (to dress in costume), {反抗|はんこう}する (to rebel), {正座|せいざ}する (to sit formally), {混雑|こんざつ}する (to be crowded), {録音|ろくおん}する (to record audio), {油断|ゆだん}する (to be careless), {直視|ちょくし}する (to look squarely at), {修行|しゅぎょう}する (to undergo training), {追放|ついほう}する (to banish), {降格|こうかく}する (to demote), {熟睡|じゅくすい}する (to sleep soundly), {復帰|ふっき}する (to return), {退治|たいじ}する (to exterminate), {執筆|しっぴつ}する (to author), {介入|かいにゅう}する (to intervene), {削減|さくげん}する (to cut/reduce), {転校|てんこう}する (to transfer schools), {下校|げこう}する (to go home from school), {凝視|ぎょうし}する (to stare at), {敵対|てきたい}する (to be hostile), {軽視|けいし}する (to belittle), {懇願|こんがん}する (to implore)
- **Expression (1)**: {差|さ}し{支|つか}えない (no problem/objection)
- **Noun (1)**: {揺|ゆ}り{戻|もど}し (rebound/backlash)
- 27 candidates synced from candidate list

Total entries: 25,173 → 25,200.

### 2026-04-24 (Vocabulary Expansion - 20 New Entries, Batch 36)
Added 20 new dictionary entries (IDs 25331-25350) from candidate_words.json. Focused on high-frequency, practical vocabulary useful for intermediate learners across daily life, business, science, and personal expression.

- **Suru verbs (10)**: {発展|はってん}する (to develop), {確認|かくにん}する (to confirm), {呼吸|こきゅう}する (to breathe), {化粧|けしょう}する (to put on makeup), {分析|ぶんせき}する (to analyze), {記録|きろく}する (to record), じっとする (to stay still), {我慢|がまん}する (to endure), {強化|きょうか}する (to strengthen), {情報|じょうほう}{共有|きょうゆう} (information sharing)
- **Ichidan verb (1)**: {並|なら}べ{替|か}える (to rearrange)
- **Na-adjectives (3)**: {適切|てきせつ}な (appropriate), {雑|ざつ}な (sloppy), {幻想的|げんそうてき}な (fantastical)
- **Nouns (6)**: {温|あたた}かみ (warmth), {被災者|ひさいしゃ} (disaster victim), {単語帳|たんごちょう} (vocabulary book), {水道水|すいどうすい} (tap water), {軟水|なんすい} (soft water), {雨模様|あまもよう} (rainy weather)
- 19 candidates synced from candidate list

Total entries: 25,123 → 25,143.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
