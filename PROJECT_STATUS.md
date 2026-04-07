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

### 2026-04-07 (Vocabulary Expansion - 15 New Entries, Session 35)
Added 15 new dictionary entries (IDs 22760-22774) from candidate_words.json. A diverse mix of nouns, expressions, and a verb covering culture, daily life, business, communication, medicine, and history.

- **Nouns (8)**: ゴールデンウィーク (Golden Week), {受|う}け{渡|わた}し (handover), {持|も}ち{前|まえ} (natural trait), {救急隊員|きゅうきゅうたいいん} (paramedic), {批判家|ひはんか} (critic), {鑑賞者|かんしょうしゃ} (viewer/appreciator), {過密|かみつ}スケジュール (overcrowded schedule), {忠言|ちゅうげん} (frank advice)
- **Noun/suru verbs (3)**: {自己批判|じこひはん} (self-criticism), {事前予約|じぜんよやく} (advance reservation), {創建|そうけん} (founding/construction)
- **Expressions (2)**: {場合|ばあい}によっては (depending on the case), {予定|よてい}を{立|た}てる (to make plans)
- **Verb (godan) (1)**: {織|お}り{込|こ}む (to weave in/factor in)
- **Adjective-no (1)**: {持|も}ち{前|まえ} (inherent, natural — also noun)

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 34)
Added 30 new dictionary entries (IDs 22730-22759) from candidate_words.json. A diverse mix of nouns, expressions, a verb, and a pre-noun adjectival covering entertainment, society, nature, food, culture, daily life, language, and science.

- **Nouns (21)**: ホラー (horror genre), ミステリー (mystery genre), {発展途上国|はってんとじょうこく} (developing country), {一般人|いっぱんじん} (ordinary person), {田植|たう}え (rice planting), {全面|ぜんめん} (whole surface/all aspects), {一家|いっか}{団|だん}らん (family togetherness), {一覧表|いちらんひょう} (list/table), {交際相手|こうさいあいて} (romantic partner), {作業中|さぎょうちゅう} (work in progress), しめじ (shimeji mushroom), {斜|なな}め{読|よ}み (skimming), さん{付|づ}け (using -san honorific), {左翼|さよく} (left wing), {混雑時間帯|こんざつじかんたい} (peak hours), {散在|さんざい} (scattered), {化学繊維|かがくせんい} (synthetic fiber), {大人数|おおにんずう} (large group), {七草粥|ななくさがゆ} (seven-herb porridge), {事案|じあん} (case/matter), {収容所|しゅうようじょ} (detention center), {沢|さわ} (mountain stream), {季節替|きせつが}わり (seasonal change), {被曝|ひばく} (radiation exposure)
- **Noun/suru verbs (3)**: {越冬|えっとう} (overwintering), {散在|さんざい} (scattered), {被曝|ひばく} (radiation exposure)
- **Verb (1)**: {読|よ}み{流|なが}す (to skim over)
- **Expressions (3)**: {元気|げんき}いっぱい (full of energy), たった{一人|ひとり} (only one person), じゃあまた (see you later)
- **Pre-noun adjectival (1)**: ほんの (just, only, mere)
- **New kanji**: 曝 (expose) — assigned kanji ID 02657

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 33)
Added 30 new dictionary entries (IDs 22700-22729) from candidate_words.json. A diverse mix of nouns and suru verbs covering daily life, society, government, education, environment, science, music, sports, health, and more.

- **Nouns (27)**: {県民|けんみん} (prefectural resident), {庁舎|ちょうしゃ} (government building), {私有地|しゆうち} (private land), {水道料金|すいどうりょうきん} (water bill), {理科室|りかしつ} (science lab), {文化史|ぶんかし} (cultural history), オーブンレンジ (combination microwave oven), {電波時計|でんぱどけい} (radio-controlled clock), {経理課|けいりか} (accounting dept), {海面上昇|かいめんじょうしょう} (sea level rise), {自然破壊|しぜんはかい} (destruction of nature), グランドピアノ (grand piano), {都市|とし}ガス (city gas), {明朝体|みんちょうたい} (Mincho typeface), {社務所|しゃむしょ} (shrine office), {倍速再生|ばいそくさいせい} (double-speed playback), {成績優秀|せいせきゆうしゅう} (excellent grades), {貸切|かしきり}バス (chartered bus), {工業地帯|こうぎょうちたい} (industrial zone), {共同責任|きょうどうせきにん} (joint responsibility), {慈善事業|じぜんじぎょう} (charitable work), {人権問題|じんけんもんだい} (human rights issue), {開幕戦|かいまくせん} (opening game), {早期診断|そうきしんだん} (early diagnosis), {殺菌剤|さっきんざい} (disinfectant), {乾燥地帯|かんそうちたい} (arid region), {消毒剤|しょうどくざい} (antiseptic)
- **Noun/suru verbs (3)**: {再生産|さいせいさん} (reproduction), {株式公開|かぶしきこうかい} (IPO), {吹奏|すいそう} (wind instrument performance)

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 32)
Added 30 new dictionary entries (IDs 22670-22699) from candidate_words.json. A diverse mix of nouns, expressions, suru verbs, and a na-adjective covering personality, culture, law, business, perception, emotion, and more.

- **Expressions (8)**: {耳|みみ}を{澄|す}ます (to listen carefully), {気味|きみ}が{悪|わる}い (creepy), {暖簾|のれん}に{腕押|うでお}し (futile effort), {愛想|あいそ}が{悪|わる}い (unsociable), {無心|むしん}になる (to become absorbed), {手狭|てぜま}になる (to become cramped), ふと{思|おも}い{出|だ}す (to suddenly remember), {決定的瞬間|けっていてきしゅんかん} (decisive moment — as noun)
- **Suru verbs (2)**: {加入|かにゅう}する (to join), {深刻化|しんこくか}する (to become serious)
- **Na-adjective (1)**: {結果的|けっかてき} (resultant, eventual)
- **Nouns (19)**: {労力|ろうりょく} (labor/effort), {世間知|せけんし}らず (naive), {内密|ないみつ} (confidential), {秀作|しゅうさく} (excellent work), {家族|かぞく}{団|だん}らん (family togetherness), お{盆休|ぼんやす}み (Obon holiday), {半人前|はんにんまえ} (half-fledged), {青二才|あおにさい} (greenhorn), {日和見|ひよりみ} (opportunism), {児童文学|じどうぶんがく} (children's literature), {荷物検査|にもつけんさ} (baggage inspection), {国際協力|こくさいきょうりょく} (international cooperation), {営業利益|えいぎょうりえき} (operating profit), {旅日記|たびにっき} (travel diary), {精神的苦痛|せいしんてきくつう} (emotional distress), {有力候補|ゆうりょくこうほ} (leading candidate), {原子爆弾|げんしばくだん} (atomic bomb), {無期懲役|むきちょうえき} (life imprisonment), {寄稿者|きこうしゃ} (contributor)

### 2026-04-06 (Vocabulary Expansion - 25 New Entries, Session 31)
Added 25 new dictionary entries (IDs 22645-22669) from candidate_words.json. Removed 1 stale candidate (焦れったい, already existed as entry 22590). A diverse mix of nouns, suru verbs, and a na-adjective covering culture, music, medicine, literature, daily life, and more.

- **Nouns (16)**: {口笛|くちぶえ} (whistling), {警笛|けいてき} (warning whistle), {実用性|じつようせい} (practicality), {花札|はなふだ} (hanafuda cards), {本意|ほんい} (real intention), {社員証|しゃいんしょう} (employee ID), {暗黒街|あんこくがい} (underworld), {宿願|しゅくがん} (long-cherished wish), {便覧|べんらん} (handbook), {文壇|ぶんだん} (literary circles), {撮影所|さつえいじょ} (film studio), {縦笛|たてぶえ} (recorder), {旅行記|りょこうき} (travelogue), {紀行文|きこうぶん} (travel essay), {佳作|かさく} (honorable mention), あいこ (tie/draw)
- **Suru verbs (5)**: {流浪|るろう} (wandering), {接種|せっしゅ} (vaccination), {先導|せんどう} (leading), {敬畏|けいい} (awe/reverence), {企図|きと} (plan/scheme)
- **Na-adjective (1)**: {精細|せいさい} (detailed/fine)
- **Household (2)**: {鍋|なべ}つかみ (pot holder), {皇族|こうぞく} (imperial family)
- **Na-adjective (1)**: {演壇|えんだん} (podium)












