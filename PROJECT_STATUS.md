# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-14
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

### 2026-04-15 (Vocabulary Expansion - 14 New Entries)
Added 14 new dictionary entries (IDs 23811-23824) from candidate_words.json. A themed set focused on 〜的 na-adjectives (abstract/academic register) plus several nouns.

- **Na-adjectives (9)**: {概念的|がいねんてき} (conceptual; abstract), {派生的|はせいてき} (derivative; derived), {局所的|きょくしょてき} (localized), {先駆的|せんくてき} (pioneering; trailblazing), {非論理的|ひろんりてき} (illogical), {非合理的|ひごうりてき} (irrational), {情緒的|じょうちょてき} (emotional; sentimental), {友好的|ゆうこうてき} (friendly; amicable), {発作的|ほっさてき} (impulsive; fit-like)
- **Nouns (4)**: {現象学|げんしょうがく} (phenomenology), {防護柵|ぼうごさく} (protective fence; guardrail), {来客数|らいきゃくすう} (number of visitors/customers), {写真室|しゃしんしつ} (photo studio — room)
- **Noun+suru verb (1)**: {減水|げんすい} (drop in water level; reservoir-level fall)
- All entries include progressive-length examples, structured notes with USAGE / COLLOCATIONS / SIMILAR WORDS sections (plus RELATED TERMS or CULTURAL CONTEXT where relevant), and full furigana coverage

### 2026-04-14 (Vocabulary Expansion - 13 New Entries)
Added 13 new dictionary entries (IDs 23798-23810) from candidate_words.json. A mix of formal/technical, sexuality-related, legal, and traditional vocabulary.

- **Na-adjectives (3)**: {性的|せいてき} (sexual; erotic), {狭量|きょうりょう} (narrow-minded; petty), {有毒|ゆうどく} (poisonous; toxic — also no-adj)
- **Noun/suru verbs (3)**: {野宿|のじゅく} (sleeping outdoors), {査察|ささつ} (official on-site inspection), {昏睡|こんすい} (coma / comatose state), {作図|さくず} (geometric construction; drafting)
- **Nouns (5)**: {先人|せんじん} (forerunner; predecessor), {論客|ろんきゃく} (pundit; skilled debater), {猥褻|わいせつ} (obscene; indecent — na-adj), {性欲|せいよく} (sexual desire; libido), {多用途|たようと} (multi-purpose), {棒術|ぼうじゅつ} (traditional staff martial art)
- All entries include progressive-length examples, structured notes with USAGE / COLLOCATIONS / SIMILAR WORDS (plus CULTURAL CONTEXT where relevant) sections, and full furigana coverage
- Added new kanji 褻 (ID 02683) to the kanji index

### 2026-04-14 (Vocabulary Expansion - 25 New Entries)
Added 25 new dictionary entries (IDs 23773-23797) from candidate_words.json. A mix of everyday nouns, technical terms, and cultural/scientific vocabulary.

- **Media/Arts**: {映画化|えいがか} (film adaptation, noun+suru-verb), {紅色|べにいろ} (crimson; safflower red), {弓術|きゅうじゅつ} (traditional archery as a martial art)
- **Geography/Location**: {中心部|ちゅうしんぶ} (central part; downtown), {白昼|はくちゅう} (broad daylight; daytime)
- **Work/Social**: {受|う}け{持|も}ち (one's charge or assigned area), {会話力|かいわりょく} (conversational ability), {社交性|しゃこうせい} (sociability), {熟練者|じゅくれんしゃ} (experienced worker; skilled craftsperson), {総務部|そうむぶ} (general affairs department), {送付先|そうふさき} (mailing/shipping address)
- **Nature/Biology**: {動植物|どうしょくぶつ} (flora and fauna), {獣|けもの} (wild beast), {亜種|あしゅ} (subspecies), {同種|どうしゅ} (same kind/species), {脂肪酸|しぼうさん} (fatty acid)
- **Daily life**: {食糧不足|しょくりょうぶそく} (food shortage), {風|かぜ}よけ (windbreak), {食堂車|しょくどうしゃ} (dining car), トイレットペーパー (toilet paper), {公衆|こうしゅう}トイレ (public toilet), {肩掛|かたか}け (shawl/shoulder wrap), {核爆弾|かくばくだん} (nuclear bomb)
- **Abstract**: {先駆|さきが}け (forerunner; pioneer; harbinger), {構成要素|こうせいようそ} (component; constituent element)
- All entries include progressive-length examples, structured notes with USAGE / COLLOCATIONS / SIMILAR WORDS (and in some cases CULTURAL NOTE) sections, and full furigana coverage
- Added new kanji 亜 (ID 02682) to the kanji index

### 2026-04-14 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 23763-23772) from candidate_words.json. A mix of crime/media, writing/language, logistics, and sports/transport vocabulary.

- **Nouns (7)**: {覗|のぞ}き (peeping/voyeurism — two senses), {制作者|せいさくしゃ} (creator/producer of media), {公海|こうかい} (the high seas / international waters), {夜行列車|やこうれっしゃ} (overnight train), シャープペンシル (mechanical pencil), {野球場|やきゅうじょう} (baseball stadium), {引用文|いんようぶん} (quotation / quoted passage), {引用符|いんようふ} (quotation marks)
- **Na-adjective (1)**: {内部的|ないぶてき} (internal; in-house)
- **Noun+suru verb (1)**: {入庫|にゅうこ} (warehousing; returning to depot — two senses)
- All entries include progressive-length examples, structured notes (USAGE/COLLOCATIONS/SIMILAR WORDS sections), and full furigana coverage

### 2026-04-14 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 23753-23762) from candidate_words.json. A mix of everyday verbs and phrases, news and media vocabulary, and disaster/infrastructure terms.

- **Nouns (5)**: {検査|けんさ}キット (test kit), {誤差|ごさ}{範囲|はんい} (margin of error), {押|お}し{入|い}り (break-in / home invasion), {決壊|けっかい}{口|ぐち} (levee breach), {独占|どくせん}{取材|しゅざい} (exclusive interview; also suru-verb)
- **Godan verbs (2)**: {連|つ}れていく (to take someone along), ぐるぐる{回|まわ}る (to spin round and round)
- **Adverb (1)**: {個別|こべつ}に (individually, separately)
- **Pronoun (1)**: あれら (those, distant plural)
- **Expression (1)**: {代|か}わりのない (irreplaceable)
- Hand-corrected the auto-generated conjugation for {連|つ}れていく because the いく stem has irregular past/て forms (いった, いって)
- All entries include progressive-length examples, structured notes (USAGE/COLLOCATIONS/SIMILAR WORDS/RELATED TERMS sections), and full furigana coverage

### 2026-04-14 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 23737-23752) from candidate_words.json. A mix of everyday household items, loanwords, media/tech vocabulary, and cooking terms.

- **Nouns (13)**: スクランブルエッグ (scrambled eggs), センチメートル (centimeter), ドレッサー (dresser/vanity), キャビア (caviar), ボイラー (boiler), ホルン (French horn), サンバイザー (sun visor — two senses: headwear and car visor), ハイカー (hiker), ヨガマット (yoga mat), {充電池|じゅうでんち} (rechargeable battery), {割増料金|わりましりょうきん} (surcharge), {電気|でんき}ポット (electric hot water dispenser), {介護休業|かいごきゅうぎょう} (family care leave), {焼|や}き{目|め} (browned surface/sear)
- **Noun+suru verbs (2)**: ライブ{配信|はいしん} (live streaming), チャンネル{登録|とうろく} (channel subscription)
- All entries include progressive-length examples, structured notes (USAGE/COLLOCATIONS/SIMILAR WORDS/CULTURAL NOTE sections), and full furigana coverage

### 2026-04-14 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 23727-23736) from candidate_words.json, mainly technical and specialized nouns in the general tier.

- **Nouns (10)**: {孵化場|ふかじょう} (hatchery), {孵卵器|ふらんき} (incubator), {玄武岩|げんぶがん} (basalt), {泥岩|でいがん} (mudstone), {禁固刑|きんこけい} (imprisonment without labor), {団員|だんいん} (group/troupe member), {外枠|そとわく} (outer frame), {攪拌器|かくはんき} (mixer/agitator), {黄熱病|おうねつびょう} (yellow fever), {骨格筋|こっかくきん} (skeletal muscle)
- All entries created with full v2 quality: progressive-length examples, structured notes (USAGE/COLLOCATIONS/SIMILAR WORDS sections), and full furigana coverage
- Two new kanji (攪, 拌) added to the kanji index (IDs 02680, 02681)

### 2026-04-14 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 23711-23726) from candidate_words.json. A mix of everyday, financial, technical, and abstract vocabulary.

- **Nouns (13)**: {利用限度額|りようげんどがく} (credit limit), マイナンバーカード (My Number Card), フリータイム (unlimited-time plan), {利用者|りようしゃ}カード (user/library card), {遺失物取扱所|いしつぶつとりあつかいじょ} (lost-and-found office), {基準金利|きじゅんきんり} (benchmark interest rate), {季節行事|きせつぎょうじ} (seasonal event), レコーダー (recorder), {録音機|ろくおんき} (audio recorder), {垂直線|すいちょくせん} (vertical/perpendicular line), {交差線|こうさせん} (intersecting line), {顧客|こきゃく}サービス (customer service), {心理現象|しんりげんしょう} (psychological phenomenon)
- **Noun+suru verbs (1)**: {平均化|へいきんか} (averaging / leveling)
- **Expressions (2)**: {途中|とちゅう}から (from partway through), ブラシをかける (to brush)
- All entries created with full v2 quality: progressive-length examples, structured notes (USAGE/COLLOCATIONS/SIMILAR WORDS sections), and full furigana coverage

### 2026-04-14 (Vocabulary Expansion - 13 New Entries)
Added 13 new dictionary entries (IDs 23698-23710) from candidate_words.json. A mix of general, scientific, and everyday vocabulary.

- **Nouns (10)**: {中国人|ちゅうごくじん} (Chinese person), {天然|てんねん}ゴム (natural rubber), {合成|ごうせい}ゴム (synthetic rubber), {積雲|せきうん} (cumulus cloud), {層雲|そううん} (stratus cloud), {神経系|しんけいけい} (nervous system), {合成|ごうせい}{皮革|ひかく} (synthetic leather), {葉緑体|ようりょくたい} (chloroplast), {有袋類|ゆうたいるい} (marsupials)
- **Noun+suru verbs (1)**: {閉経|へいけい} (menopause)
- **Godan verbs (3)**: {向|む}かい{合|あ}う (to face each other), {切羽|せっぱ}{詰|つ}まる (to be cornered), {引|ひ}き{落|お}とす (to debit / pull down)
- Added conjugation tables to all new verbs and the suru-verb entry
- Removed 13 candidates that now exist as entries

### 2026-04-14 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 23668-23697) from candidate_words.json. A mix of technology, architecture, business, ecology, grammar, accounting, and general vocabulary for intermediate learners.

- **Nouns (20)**: {高画質|こうがしつ} (high image quality), {低画質|ていがしつ} (low image quality), {平面図|へいめんず} (floor plan), {立面図|りつめんず} (elevation drawing), {原始林|げんしりん} (primeval forest), {自然林|しぜんりん} (natural forest), {地元紙|じもとし} (local newspaper), {歴史学|れきしがく} (history as a discipline), {奇術|きじゅつ} (stage magic), {出世欲|しゅっせよく} (desire for career advancement), {提出書類|ていしゅつしょるい} (required submission documents), {金管楽器|きんかんがっき} (brass instrument), {低品質|ていひんしつ} (low quality), {上級者向|じょうきゅうしゃむ}け (for advanced users), {初級者向|しょきゅうしゃむ}け (for beginners), つなぎ{役|やく} (intermediary / bridging role), {提携先|ていけいさき} (business partner), {会議費|かいぎひ} (meeting expenses, accounting), {給水塔|きゅうすいとう} (water tower), {受|う}け{止|と}め{方|かた} (way of taking/interpreting), {成語|せいご} (set phrase/idiom)
- **Noun+suru verbs (5)**: {自給|じきゅう} (self-sufficiency in supply), {自足|じそく} (self-sufficiency), {事故死|じこし} (accidental death), {送風|そうふう} (ventilation/fan), {正比例|せいひれい} (direct proportion), {区別化|くべつか} (differentiation)
- **Expressions (3)**: どのように (how, in what way), {仕事|しごと}のやりがい (fulfillment at work), {対価|たいか}を{払|はら}う (to pay a price)
- Added conjugation tables to 6 new suru verbs automatically
- Removed 30 candidates that now exist as entries

### 2026-04-13 (Vocabulary Expansion - 15 New Entries)
Added 15 new dictionary entries (IDs 23653-23667) from candidate_words.json. A mix of historical, biological, medical, geographical, business, geometric, and everyday vocabulary.

- **Nouns (15)**: {引|ひ}き{揚|あ}げ{者|しゃ} (postwar repatriate), {誕生祭|たんじょうさい} (birthday celebration, esp. for an idol/character), {二十日鼠|はつかねずみ} (house mouse), {齧歯類|げっしるい} (rodents), {死後硬直|しごこうちょく} (rigor mortis), {家庭用|かていよう}ゲーム{機|き} (home game console), {耳鼻咽喉科|じびいんこうか} (ENT department), {輸液|ゆえき} (IV infusion), {首長竜|くびながりゅう} (plesiosaur), {返信|へんしん}はがき (reply postcard), {同族企業|どうぞくきぎょう} (family business), {正三角形|せいさんかくけい} (equilateral triangle), {二十三区|にじゅうさんく} (Tokyo's 23 wards), {顎紐|あごひも} (chin strap), {脱脂粉乳|だっしふんにゅう} (skim milk powder)
- Removed 15 candidates that now exist as entries

### 2026-04-13 (Vocabulary Expansion - 18 New Entries)
Added 18 new dictionary entries (IDs 23635-23652) from candidate_words.json. A mix of diplomatic, legal, bureaucratic, meteorological, culinary, grammatical, and everyday vocabulary, including some slang and tech-era terms.

- **Nouns (16)**: {特命全権大使|とくめいぜんけんたいし} (ambassador extraordinary and plenipotentiary), {所定事項|しょていじこう} (required items on a form), {不該当|ふがいとう} (not applicable), {計算手法|けいさんしゅほう} (calculation method), {既遂|きすい} (consummated crime), {正犯|せいはん} (principal offender), {略奪愛|りゃくだつあい} (stealing someone's partner), {暖波|だんぱ} (warm spell / heat wave), {被修飾語|ひしゅうしょくご} (modified word — grammar), {指図役|さしずやく} (person giving orders), {内皮|ないひ} (endothelium / inner skin), {先日付|さきづけ} (post-dating), {逆|ぎゃく}ナン (woman picking up a man — slang), {投|な}げ{銭|せん}{機能|きのう} (tipping feature), {焼|や}き{麩|ふ} (toasted wheat gluten), {生麩|なまふ} (fresh wheat gluten), {八歳|はっさい} (eight years old)
- **Na-adjectives (1)**: {自衛的|じえいてき} (self-defensive)
- Removed 18 candidates that now exist as entries

### 2026-04-13 (Vocabulary Expansion - 15 New Entries)
Added 15 new dictionary entries (IDs 23620-23634) from candidate_words.json. A mix of technical, educational, and everyday vocabulary including medical, household, kanji-radical, industrial, mathematical, and number/age terms.

- **Nouns (13)**: {抗炎症|こうえんしょう} (anti-inflammatory), {体脂肪計|たいしぼうけい} (body fat scale), {身長計|しんちょうけい} (stadiometer), ハンマー{投|な}げ (hammer throw), にんべん (person radical 亻), きへん (tree radical 木), {旁|つくり} (right-hand kanji component), スタンプ{台|だい} (ink pad for rubber stamps), {溶鉱炉|ようこうろ} (blast furnace), {四角錐|しかくすい} (square pyramid), {処理装置|しょりそうち} (processing unit), {骨格標本|こっかくひょうほん} (skeletal specimen), {十九歳|じゅうきゅうさい} (nineteen years old), {大量殺人|たいりょうさつじん} (mass murder)
- **Number (1)**: {二万|にまん} (twenty thousand)
- Added new kanji 旁 to kanji_list.json (ID 02679_hou_tsukuri_right-component)
- Removed 15 candidates that now exist as entries

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








