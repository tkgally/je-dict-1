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

### 2026-04-24 (Vocabulary Expansion - 30 New Entries, Batch 35)
Added 30 new dictionary entries (IDs 25301-25330) from candidate_words.json. Focused on useful two-kanji compounds and common vocabulary across science, politics, food, culture, and daily life.

- **Nouns (18)**: {重力|じゅうりょく} (gravity), {自伝|じでん} (autobiography), {範疇|はんちゅう} (category), {内情|ないじょう} (inside story), {室温|しつおん} (room temperature), {純愛|じゅんあい} (pure love), {氷河|ひょうが} (glacier), {苦難|くなん} (hardship), {炭火|すみび} (charcoal fire), {酢豚|すぶた} (sweet and sour pork), {錠前|じょうまえ} (lock), {翌週|よくしゅう} (following week), {長屋|ながや} (row house)
- **Suru verbs (8)**: {従属|じゅうぞく}する (to be subordinate), {倒壊|とうかい}する (to collapse), {退陣|たいじん}する (to step down), {討議|とうぎ}する (to discuss), {湾曲|わんきょく}する (to curve), {発育|はついく}する (to grow), {始業|しぎょう}する (to start work), {出頭|しゅっとう}する (to turn oneself in)
- **Adverb (1)**: {俄然|がぜん} (suddenly/dramatically)
- **Na-adjectives (2)**: {変則|へんそく} (irregular), {早熟|そうじゅく} (precocious)
- **Other (1)**: {食用|しょくよう} (edible), {儀礼|ぎれい} (ceremony/etiquette), {沸点|ふってん} (boiling point), {思慮|しりょ} (prudence), {平常|へいじょう} (normal), {造語|ぞうご} (coined word)
- 1 new kanji added: 疇
- 30 candidates synced from candidate list

Total entries: 25,093 → 25,123.

### 2026-04-24 (Vocabulary Expansion - 30 New Entries, Batch 34)
Added 30 new dictionary entries (IDs 25271-25300) from candidate_words.json. Diverse batch covering culture, daily life, science, work, food, and more.

- **Nouns (18)**: かぶれ (skin rash), {挑戦者|ちょうせんしゃ} (challenger), {引力|いんりょく} (gravity), {大空|おおぞら} (vast sky), {重病|じゅうびょう} (serious illness), バレンタインデー (Valentine's Day), ホワイトデー (White Day), {製鉄所|せいてつじょ} (steel mill), {芸名|げいめい} (stage name), {床暖房|ゆかだんぼう} (floor heating), {夏疲|なつづか}れ (summer fatigue), サービス{業|ぎょう} (service industry), {透明度|とうめいど} (transparency), {返却期限|へんきゃくきげん} (return deadline), {図画工作|ずがこうさく} (arts and crafts), {市場経済|しじょうけいざい} (market economy), {有用性|ゆうようせい} (usefulness), {鶏卵|けいらん} (chicken egg)
- **Suru verbs (5)**: {攻略|こうりゃく}する (to capture/to clear a game), {慰労|いろう}する (to appreciate effort), {奪取|だっしゅ}する (to seize), {内職|ないしょく}する (to do side jobs), {配備|はいび}する (to deploy)
- **Other (7)**: くすくす{笑|わら}う (to giggle), {横入|よこい}り (cutting in line), {未処理|みしょり} (unprocessed), {休暇明|きゅうかあ}け (post-vacation), もも{肉|にく} (thigh meat), {顧客対応|こきゃくたいおう} (customer service), {鳥|とり}のさえずり (birdsong)
- 30 candidates synced from candidate list

Total entries: 25,063 → 25,093.


_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
