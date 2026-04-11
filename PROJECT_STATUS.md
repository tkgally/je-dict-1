# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-11
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

### 2026-04-11 (Vocabulary Expansion - 20 New Entries)
Added 20 new dictionary entries (IDs 23355-23374) from candidate_words.json. A diverse mix of everyday vocabulary, tech and business terms, a medical word, and formal written-register vocabulary.

- **Nouns (16)**: {翌年|よくねん} (the following year), {血行|けっこう} (blood circulation), {自己|じこ} (the self), お{嬢様|じょうさま} (young lady), {英和辞典|えいわじてん} (English-Japanese dictionary), {電源|でんげん}ボタン (power button), コンシーラー (concealer), {牛|ぎゅう}ひき{肉|にく} (ground beef), {腫瘍|しゅよう} (tumor), {初期値|しょきち} (initial/default value), {交渉力|こうしょうりょく} (negotiating skill / bargaining power), {天性|てんせい} (innate nature), {数百|すうひゃく} (several hundred), {実利|じつり} (practical benefit), {追加|ついか}{予算|よさん} (additional budget), {悲運|ひうん} (tragic fate), {賛同者|さんどうしゃ} (supporter)
- **Noun/suru verb (1)**: {結晶化|けっしょうか} (crystallization; figurative taking form)
- **Expressions (2)**: {唯一|ゆいいつ}の (the only; the sole), {多|おお}くの (many of; a lot of — attributive)

### 2026-04-11 (Vocabulary Expansion - 28 New Entries)
Added 28 new dictionary entries (IDs 23327-23354) from candidate_words.json. A mix of color terms, science and history vocabulary, practical home and business words, formal written vocabulary, and traditional crafts.

- **Nouns (25)**: {赤色|あかいろ} (red color), {電子|でんし}メール (email), {赤茶色|あかちゃいろ} (reddish brown), {多面体|ためんたい} (polyhedron), {対流圏|たいりゅうけん} (troposphere), {古墳|こふん}{時代|じだい} (Kofun period), {分電盤|ぶんでんばん} (distribution board), {釉薬|ゆうやく} (ceramic glaze), {轆轤|ろくろ} (potter's wheel/lathe), {株分|かぶわ}け (plant division), {有酸素|ゆうさんそ}{運動|うんどう} (aerobic exercise), {真冬日|まふゆび} (day below freezing), {委細|いさい} (full particulars), コスチューム (costume), アナログ{時計|どけい} (analog clock), {家電|かでん}{量販店|りょうはんてん} (big-box electronics retailer), {論旨|ろんし} (main thrust of an argument), {立替|たてか}え{払|ばら}い (out-of-pocket payment), {感嘆詞|かんたんし} (interjection), {真珠色|しんじゅいろ} (pearly white), {守護霊|しゅごれい} (guardian spirit), {練習場|れんしゅうじょう} (practice range), {不起訴|ふきそ} (non-indictment), {堆積岩|たいせきがん} (sedimentary rock), {凝縮感|ぎょうしゅくかん} (sense of density)
- **Noun/suru verbs (2)**: {再検査|さいけんさ} (reexamination), {鍵|かぎ}{交換|こうかん} (lock replacement)
- **Pronoun (1)**: {彼女|かのじょ}たち (they - female)
- Added 3 new kanji to index: 釉 (glaze), 轆 (pulley), 轤 (pulley)

### 2026-04-11 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 23297-23326) from candidate_words.json. A mix of common everyday vocabulary, practical tech/web terms, health and medical terms, legal/tax vocabulary, and contemporary social keywords.

- **Nouns (18)**: ベジタリアン (vegetarian), {血液検査|けつえきけんさ} (blood test), {尿検査|にょうけんさ} (urine test), {料理教室|りょうりきょうしつ} (cooking class), {持久走|じきゅうそう} (endurance run), {反復横跳|はんぷくよことび}び (side-to-side jumping fitness test), {二次元|にじげん}コード (QR code), {即日|そくじつ}{配送|はいそう} (same-day delivery), {人間|にんげん}ドック (comprehensive medical checkup), ブラック{企業|きぎょう} (exploitative company), {働|はたら}き{方|かた}{改革|かいかく} (work-style reform), フレックス (flextime), {論文審査|ろんぶんしんさ} (thesis examination), {医療費|いりょうひ}{控除|こうじょ} (medical expense deduction), {扶養|ふよう}{控除|こうじょ} (dependent deduction), {間引|まび}き{運転|うんてん} (reduced service), {折返|おりかえ}し{運転|うんてん} (shuttle operation), {口頭試問|こうとうしもん} (oral examination), {寸志|すんし} (small token of gratitude)
- **Noun/suru verbs (5)**: ログインする (to log in), ログアウトする (to log out), {示談|じだん} (out-of-court settlement), {供述|きょうじゅつ} (testimony), {原状回復|げんじょうかいふく} (restoration to original condition), {盗用|とうよう} (plagiarism)
- **Adverbs (2)**: {正|ただ}しく (correctly), {元気|げんき}よく (energetically)
- **Expressions (3)**: {最初|さいしょ}から (from the start), {途中|とちゅう}で (halfway; on the way), {底知|そこし}れない (unfathomable)

### 2026-04-11 (Vocabulary Expansion - 20 New Entries)
Added 20 new dictionary entries (IDs 23277-23296) from candidate_words.json. All nouns — a mix of professional roles, institutional and social vocabulary, finance, military/politics, and everyday practical terms.

- **Nouns (20)**: {国語辞典|こくごじてん} (Japanese dictionary), {調理場|ちょうりば} (commercial kitchen), {研修会|けんしゅうかい} (training session), {相談会|そうだんかい} (consultation session), {担当医|たんとうい} (attending physician), {団体行動|だんたいこうどう} (group action), {発明者|はつめいしゃ} (inventor), {設計者|せっけいしゃ} (designer/architect), {産油国|さんゆこく} (oil-producing country), {開拓者|かいたくしゃ} (pioneer), {戦闘機|せんとうき} (fighter plane), {倹約家|けんやくか} (frugal person), {軍事力|ぐんじりょく} (military strength), {季節労働|きせつろうどう} (seasonal labor), {自己資金|じこしきん} (personal funds), {優待券|ゆうたいけん} (preferential voucher), {調理用具|ちょうりようぐ} (cooking utensils), {視力矯正|しりょくきょうせい} (vision correction), {人数制限|にんずうせいげん} (headcount limit), {防護壁|ぼうごへき} (protective wall)

### 2026-04-11 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 23261-23276) from candidate_words.json. A mix of formal, technical, and everyday vocabulary covering food, international politics, security, business, linguistics, body/beauty, and materials science.

- **Nouns (13)**: {一口|ひとくち}サイズ (bite-sized), {核弾頭|かくだんとう} (nuclear warhead), {国交断絶|こっこうだんぜつ} (severance of diplomatic relations), {主力商品|しゅりょくしょうひん} (flagship product), {暗号鍵|あんごうかぎ} (encryption key), {不透明度|ふとうめいど} (opacity), {一重|ひとえ}まぶた (single eyelid), {二重|ふたえ}まぶた (double eyelid), {平和維持活動|へいわいじかつどう} (peacekeeping operations), {摩擦音|まさつおん} (fricative), {競争原理|きょうそうげんり} (principle of competition), {合成樹脂|ごうせいじゅし} (synthetic resin)
- **Noun/suru verbs (2)**: {非核化|ひかくか} (denuclearization), {水耕栽培|すいこうさいばい} (hydroponics)
- **Expressions (2)**: {関係者各位|かんけいしゃかくい} (to whom it may concern), {詳細不明|しょうさいふめい} (details unknown)
- Removed 1 stale candidate (多角形/たかっけい — variant reading duplicate of existing 05553 多角形/たかくけい)

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








