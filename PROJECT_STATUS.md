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

### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 21)
Added 30 new dictionary entries (IDs 22310-22339) from candidate_words.json. A diverse mix covering daily life, culture, sports, food, business, geography, and more.

- **Verb (1)**: {語|かた}り{継|つ}ぐ (to pass down orally)
- **Adverb (1)**: {思|おも}う{存分|ぞんぶん} (to one's heart's content)
- **Nouns (28)**: {切|き}り{口|くち} (perspective/cross-section), {追加|ついか}{料金|りょうきん} (additional fee), {停学|ていがく} (school suspension), {社会|しゃかい}{貢献|こうけん} (social contribution), {駆|か}け{足|あし} (running/quick pace), {懸垂|けんすい} (pull-up), {案内|あんない}{板|ばん} (information board), {彫像|ちょうぞう} (statue), {空前|くうぜん} (unprecedented), {馬券|ばけん} (horse racing ticket), {知力|ちりょく} (intellect), {年代物|ねんだいもの} (vintage item), {鼻筋|はなすじ} (bridge of nose), {取|と}り{壊|こわ}し (demolition), {建設中|けんせつちゅう} (under construction), {営業|えいぎょう}スマイル (customer-service smile), {豚丼|ぶたどん} (pork bowl), {百人一首|ひゃくにんいっしゅ} (Hyakunin Isshu), {懸賞金|けんしょうきん} (prize money), {講談|こうだん} (storytelling), {喫煙席|きつえんせき} (smoking seat), {宝飾品|ほうしょくひん} (jewelry), {躍動感|やくどうかん} (sense of dynamism), インテリア (interior), {急坂|きゅうざか} (steep slope), {平均台|へいきんだい} (balance beam), {跳|と}び{箱|ばこ} (vaulting box), {酪農家|らくのうか} (dairy farmer)

### 2026-04-05 (Vocabulary Expansion - 26 New Entries, Session 21)
Added 26 new dictionary entries (IDs 22340-22365) from candidate_words.json. Removed 3 stale duplicate candidates. A mix of nouns, verbs, and onomatopoeia covering business, sports, culture, health, and daily life.

- **Godan verbs (5)**: {愛|いと}しむ (to cherish), {浅|あさ}まる (to become shallow), {苔|こけ}むす (to become mossy), {拭|ふ}き{消|け}す (to wipe away), {取|と}り{越|こ}す (to worry in advance)
- **Suru verbs (7)**: {厄払|やくばら}い (purification), {通算|つうさん}する (to total up), {評論|ひょうろん}する (to critique), {滅菌|めっきん}する (to sterilize), {画一化|かくいつか} (standardization), {恒常化|こうじょうか} (becoming permanent), {注油|ちゅうゆ}する (to lubricate)
- **Nouns (13)**: {財界|ざいかい} (business world), {秘密|ひみつ}{兵器|へいき} (secret weapon), {銀|ぎん}メダル (silver medal), {銅|どう}メダル (bronze medal), {使用人|しようにん} (servant), {執筆者|しっぴつしゃ} (author), {村民|そんみん} (villagers), {歴史|れきし}{学者|がくしゃ} (historian), {他殺|たさつ} (homicide), {病原菌|びょうげんきん} (pathogenic bacteria), マメ (blister), {整腸剤|せいちょうざい} (digestive medicine), ギャンブラー (gambler)
- **Onomatopoeia (1)**: ごうごう (roaring sound)

### 2026-04-05 (Vocabulary Expansion - 28 New Entries, Session 20)
Added 28 new dictionary entries (IDs 22282-22309) from candidate_words.json. A diverse mix covering daily life, culture, business, sports, food, and language.

- **Suru verbs (2)**: {遅刻|ちこく}する (to be late), {欠席|けっせき}する (to be absent)
- **Ichidan verbs (3)**: {抜|ぬ}きん{出|で}る (to excel), しゃれる (to be stylish), {洗練|せんれん}される (to be refined)
- **Na-adjective (1)**: {艶|つや}やか (glossy, lustrous)
- **Expression (1)**: {納得|なっとく}がいく (to be convinced)
- **Nouns (21)**: {努力家|どりょくか} (hard worker), {逆境|ぎゃっきょう} (adversity), {人|ひと}だかり (crowd), {水差|みずさ}し (pitcher), プライド (pride), {町家|まちや} (townhouse), {快適|かいてき}さ (comfort), {冷凍室|れいとうしつ} (freezer), {数|かぞ}え{年|どし} (traditional age), {茶道具|さどうぐ} (tea utensils), サビ (chorus), {朝会|ちょうかい} (morning meeting), {利益率|りえきりつ} (profit margin), {安全地帯|あんぜんちたい} (safety zone), {不戦敗|ふせんぱい} (forfeit loss), {舞台挨拶|ぶたいあいさつ} (stage greeting), {反則負|はんそくま}け (foul loss), {七分咲|ななぶざ}き (70% bloom), {蒸|む}し{菓子|がし} (steamed sweet), {敬白|けいはく} (respectfully yours), {謹啓|きんけい} (respectfully)

### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 19)
Added 30 new dictionary entries (IDs 22252-22281) from candidate_words.json. A diverse mix of expressions, nouns, adverbs, and verbs covering communication, daily life, culture, education, science, sports, finance, and more.

- **Expressions (10)**: ��の{通|とお}り (exactly right), どちらかといえば (if anything, rather), {明|あき}らかにする (to make clear), {小馬鹿|こばか}にする (to belittle), {豪快|ごうかい}に{笑|わら}う (to laugh heartily), {立場|たちば}がない (to lose face), {鼻|はな}を{利|き}かせる (to have a keen nose), {肘|ひじ}をつく (to rest elbows on table), {水|みず}に{浸|ひた}す (to soak in water), {情熱|じょうねつ}を{傾|かたむ}ける (to pour passion into)
- **Nouns (13)**: {届|とど}���{物|もの} (delivery), {一門|いちもん} (clan/school), {三拍子|さんびょうし} (triple time), {透明化|とうめいか} (transparency), {取|と}り{立|た}て (debt collection/freshness), {疑問形|ぎもんけい} (interrogative form), {写真機|しゃしんき} (camera), {負|ふ}の{数|すう} (negative number), {書|か}き{下|くだ}し{文|ぶん} (kanbun rendering), {自分専用|じぶんせんよう} (for personal use), {冷|ひ}ややかさ (coldness), {技能者|ぎのうしゃ} (skilled worker), やり{投|な}げ (javelin throw), {合成繊維|ごうせいせんい} (synthetic fiber), {債務者|さいむしゃ} (debtor), {中等|ちゅうとう} (secondary level), {可視|かし} (visible)
- **Adverb (1)**: ぴたり (exactly, suddenly stopping)
- **Verbs (2)**: なびかせる (to let flutter), {書|か}き{始|はじ}める (to begin writing)

### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 18)
Added 30 new dictionary entries (IDs 22222-22251) from candidate_words.json. A broad mix of adverbs, expressions, and nouns covering grammar, daily life, politics, culture, finance, and more.

- **Adverbs (4)**: {同時|どうじ}に (at the same time), まっしぐら (headlong), そそくさと (hurriedly), とりたてて (particularly)
- **Expressions (6)**: たびに (every time), あっけにとられる (to be dumbfounded), {具合|ぐあい}が{悪|わる}い (to feel unwell), {失礼|しつれい}ですが (excuse me but), {目|め}を{向|む}ける (to turn attention to), {軌道|きどう}に{乗|の}る (to get on track), {胸|むね}に{秘|ひ}める (to keep in one's heart)
- **Na-adjective (1)**: {進歩的|しんぽてき} (progressive)
- **Nouns (19)**: {値下|ねさ}がり (price drop), {買|か}い{物袋|ものぶくろ} (shopping bag), ごみ{袋|ぶくろ} (trash bag), {転入|てんにゅう} (moving in/transfer), {代案|だいあん} (alternative plan), {被疑者|ひぎしゃ} (suspect), {通達|つうたつ} (official directive), {湯上|ゆあ}がり (after a bath), {自嘲|じちょう} (self-mockery), {休眠|きゅうみん} (dormancy), {岩盤|がんばん} (bedrock), {共和制|きょうわせい} (republic), {表現|ひょうげん}の{自由|じゆう} (freedom of expression), {吟醸酒|ぎんじょうしゅ} (ginjo sake), {枝葉|えだは} (branches and leaves), {鉱石|こうせき} (ore), {貼付|ちょうふ} (affixing), {定期預金|ていきよきん} (time deposit)





