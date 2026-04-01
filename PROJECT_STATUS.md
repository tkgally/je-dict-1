# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-31
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

### 2026-04-01 (Vocabulary Expansion - 27 New Entries, Session 562)
Added 27 new dictionary entries (IDs 21227-21253) from candidate_words.json. A diverse mix of practical vocabulary covering transportation, culture, society, weather, and abstract concepts.

- **Nouns (12)**: {難局|なんきょく} (crisis), {備忘録|びぼうろく} (memorandum), {座椅子|ざいす} (floor chair), {入|い}れ{替|か}え (replacement), {体育祭|たいいくさい} (sports festival), {海賊版|かいぞくばん} (pirated edition), {十二分|じゅうにぶん} (more than enough), {生存者|せいぞんしゃ} (survivor), {中型|ちゅうがた} (medium-sized), {勲章|くんしょう} (medal), {北風|きたかぜ} (north wind), {寒風|かんぷう} (cold wind)
- **Suru verbs (5)**: {乗|の}り{降|お}り (boarding/alighting), {乱闘|らんとう} (brawl), {失火|しっか} (accidental fire), {退却|たいきゃく} (retreat), {憂慮|ゆうりょ} (concern)
- **Na-adjectives (4)**: {自明|じめい} (self-evident), {強大|きょうだい} (powerful), {大|おお}きめ (rather large), {機能的|きのうてき} (functional)
- **Other (6)**: {極楽|ごくらく} (paradise), {所用|しょよう} (business/errand), {市民権|しみんけん} (citizenship), {打|う}つ{手|て}がない (no recourse), いちゃもん (complaint), {詭弁|きべん} (sophistry)
- Added 2 new kanji to index: 勲, 詭
- Removed 3 stale candidates (duplicate readings of existing entries)

### 2026-04-01 (Vocabulary Expansion - 30 New Entries, Session 561)
Added 30 new dictionary entries (IDs 21197-21226) from candidate_words.json. A diverse mix of practical vocabulary covering food, culture, nature, time, emotions, health, and everyday life.

- **Nouns (22)**: {枝豆|えだまめ} (edamame), {落花生|らっかせい} (peanut), {顔文字|かおもじ} (kaomoji), {平常心|へいじょうしん} (composure), {小道|こみち} (path), {日光浴|にっこうよく} (sunbathing), {漁師|りょうし} (fisherman), {翌月|よくげつ} (following month), {前月|ぜんげつ} (previous month), {昔馴染|むかしなじ}み (old acquaintance), {揚|あ}げ{油|あぶら} (frying oil), {日|ひ}の{入|い}り (sunset), {所有者|しょゆうしゃ} (owner), {公私|こうし} (public and private), {小腹|こばら} (slight hunger), {練習問題|れんしゅうもんだい} (practice questions), {品質管理|ひんしつかんり} (quality control), {栄養失調|えいようしっちょう} (malnutrition), ボードゲーム (board game), {蚕|かいこ} (silkworm), {蛹|さなぎ} (pupa)
- **Suru verbs (3)**: {察知|さっち} (sensing), {放心|ほうしん} (absent-mindedness), {酩酊|めいてい} (intoxication)
- **Adverbs (2)**: ちらり (briefly), {瞬|またた}く{間|ま}に (in an instant)
- **Na-adjectives (2)**: {肉厚|にくあつ} (thick/fleshy), {恒常的|こうじょうてき} (constant)
- **Expression (1)**: {我|われ}を{忘|わす}れる (to lose oneself)
- **Other (1)**: {生|う}まれつき (by nature)
- Added 4 new kanji to index: 蚕, 蛹, 酊, 酩
- Removed 30 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 29 New Entries, Session 560)
Added 29 new dictionary entries (IDs 21168-21196) from candidate_words.json. A diverse mix covering time, safety, language, anatomy, nature, culture, fashion, food, and more.

- **Nouns (20)**: {幼少期|ようしょうき} (childhood), {防火|ぼうか} (fire prevention), {語法|ごほう} (diction), {気管|きかん} (windpipe), {日照|にっしょう} (sunshine), {見開|みひら}き (two-page spread), {村|むら}おこし (village revitalization), {渡|わた}し{舟|ぶね} (ferryboat), {公有|こうゆう} (public ownership), {兄嫁|あによめ} (sister-in-law), {橙|だいだい} (bitter orange), {柄物|がらもの} (patterned item), {回転|かいてん}ドア (revolving door), {保存|ほぞん}{容器|ようき} (storage container), {当|あ}て{推量|ずいりょう} (guesswork), {忌日|きじつ} (death anniversary), {密告者|みっこくしゃ} (informer), {猛寒|もうかん} (severe cold), {名校|めいこう} (famous school), {間諜|かんちょう} (spy)
- **Suru verbs (2)**: {補水|ほすい} (rehydration), {断煙|だんえん} (quitting smoking)
- **Na-adjectives (2)**: {堅固|けんご} (solid/firm), {儚|はかな}げ (seemingly fragile)
- **Noun/suffix (1)**: {圏|けん} (zone/sphere)
- **Noun/no-adjective (1)**: {対話型|たいわがた} (interactive)
- **Expression (1)**: {一丸|いちがん}となって (as one)
- **Other (2)**: {感謝|かんしゃ}{感激|かんげき} (deeply grateful), {綿入|わたい}れ (padded garment)
- Added 1 new kanji to index: 橙
- Removed 29 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 30 New Entries, Session 559)
Added 30 new dictionary entries (IDs 21138-21167) from candidate_words.json. Practical vocabulary covering verbs, nouns, and adjectives for everyday communication, finance, nature, and more.

- **Suru verbs (8)**: {説得|せっとく} (persuade), {分割|ぶんかつ} (divide), {分配|ぶんぱい} (distribute), {回収|かいしゅう} (collect/recall), {持参|じさん} (bring), {携帯|けいたい} (carry), {相当|そうとう} (correspond to), {匹敵|ひってき} (rival)
- **Godan verb (1)**: {書|か}き{残|のこ}す (leave in writing)
- **Nouns (17)**: {読|よ}み{書|か}き (literacy), {切|き}れ{端|はし} (scrap), {死後|しご} (after death), {自負|じふ} (pride), {休業日|きゅうぎょうび} (closed day), {衣料品|いりょうひん} (clothing), {乗組員|のりくみいん} (crew member), {遠征|えんせい} (expedition), {電話帳|でんわちょう} (phone book), {大群|たいぐん} (swarm), {金融機関|きんゆうきかん} (financial institution), {利率|りりつ} (interest rate), {地滑|じすべ}り (landslide), {同窓|どうそう} (alumnus), {照射|しょうしゃ} (irradiation), {苦慮|くりょ} (agonizing over), お{店|みせ} (shop), {島々|しまじま} (islands), {冒険者|ぼうけんしゃ} (adventurer)
- **Na-adjectives (2)**: {無防備|むぼうび} (defenseless), {敏捷|びんしょう} (agile)
- Added 1 new kanji to index: 捷
- Removed 30 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 30 New Entries, Session 558)
Added 30 new dictionary entries (IDs 21108-21137) from candidate_words.json. A diverse mix covering culture, food, movement, emotions, finance, daily life, and formal/literary vocabulary.

- **Nouns (16)**: {切|き}り{身|み} (fillet), {脳裏|のうり} (one's mind), {白身魚|しろみざかな} (white fish), {民芸品|みんげいひん} (folk craft), {小走|こばし}り (trot), {早足|はやあし} (brisk walk), {出来上|できあ}がり (finished product), {医療保険|いりょうほけん} (medical insurance), {副収入|ふくしゅうにゅう} (side income), サラダ{油|あぶら} (cooking oil), {本館|ほんかん} (main building), {別館|べっかん} (annex), {島民|とうみん} (islander), カイロ (hand warmer), {耐熱|たいねつ} (heat-resistant), {仮設|かせつ} (temporary)
- **Suru verbs (4)**: {検閲|けんえつ} (censorship), {赤面|せきめん} (blushing), {欠落|けつらく} (omission), {常駐|じょうちゅう} (permanent stationing), {処遇|しょぐう} (treatment), {天日干|てんぴぼ}し (sun-drying)
- **Na-adjectives (2)**: {未曾有|みぞう} (unprecedented), {悠長|ゆうちょう} (leisurely)
- **I-adjective (1)**: {変|か}わりやすい (changeable)
- **Ichidan verb (1)**: {積|つ}み{立|た}てる (to save up)
- **Expression (2)**: {口|くち}をつぐむ (to keep silent), {火|ひ}を{見|み}るより{明|あき}らか (obvious beyond doubt)
- **Adverb (1)**: きっかり (exactly)
- **Other**: {荒涼|こうりょう} (desolate)
- Added 1 new kanji to index: 曾
- Removed 30 candidates that now exist as entries



---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
