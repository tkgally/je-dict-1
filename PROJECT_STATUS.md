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

### 2026-04-08 (Vocabulary Expansion - 24 New Entries, Session 43)
Added 24 new dictionary entries (IDs 22964-22987) from candidate_words.json. A diverse mix of nouns, verbs, adjectives, and expressions covering politics, culture, food, geography, competition, and language.

- **Nouns (11)**: {導入部|どうにゅうぶ} (introduction/opening section), {何倍|なんばい} (how many fold), {素案|そあん} (rough draft), {燭台|しょくだい} (candlestick), {第二言語|だいにげんご} (second language), ごま{塩|しお} (sesame salt), {在野|ざいや} (out of office/independent), {中距離|ちゅうきょり} (medium distance), {無党派|むとうは} (nonpartisan), {南欧|なんおう} (Southern Europe), {下方|かほう} (lower part/downward)
- **Nouns with adjective-no usage (3)**: {異国風|いこくふう} (foreign/exotic style), {無党派|むとうは} (nonpartisan), {中距離|ちゅうきょり}
- **Noun/suru verbs (3)**: {和睦|わぼく} (reconciliation), {策謀|さくぼう} (plot/intrigue), {身|み}じろぎ (stirring/fidgeting)
- **Verbs (3)**: かじりつく (to bite into/cling to), {勝|か}ち{抜|ぬ}く (to win through), {並外|なみはず}れる (to be exceptional)
- **Na-adjectives (3)**: {急進的|きゅうしんてき} (radical/progressive), {概括的|がいかつてき} (general/broad), {不徹底|ふてってい} (incomplete/halfhearted)
- **Other (2)**: {誰彼|だれかれ} (anyone and everyone), {折|おり}を{見|み}て (when the time comes)
- Removed 1 stale candidate (いとしむ — duplicate of 愛しむ, ID 22360)

### 2026-04-08 (Vocabulary Expansion - 30 New Entries, Session 42)
Added 30 new dictionary entries (IDs 22934-22963) from candidate_words.json. A diverse mix of nouns, expressions, and an adverb covering grammar, food, culture, business, color, and daily life.

- **Nouns (17)**: {泊|とま}まり (overnight stay), {青色|あおいろ} (blue color), {修正案|しゅうせいあん} (amendment), {総決算|そうけっさん} (final reckoning), {色|いろ}づけ (coloring), {平滑|へいかつ} (smooth), {具象|ぐしょう} (concrete/figurative art), {編|あ}み{髪|がみ} (braided hair), {元請|もとう}け (main contractor), {肯定形|こうていけい} (affirmative form), {命令形|めいれいけい} (imperative form), {他人丼|たにんどん} (beef-egg bowl), {三色丼|さんしょくどん} (three-color bowl), {掛|か}け{捨|す}て (term insurance), {依頼者|いらいしゃ} (client), {椿油|つばきあぶら} (camellia oil), {置屋|おきや} (geisha house), {瑠璃色|るりいろ} (lapis blue), {賛成者|さんせいしゃ} (supporter), {看板店|かんばんてん} (flagship store), {同族経営|どうぞくけいえい} (family management)
- **Expressions (7)**: どれも (all of them), にあたって (on the occasion of), {余程|よほど}の{事|こと} (something extraordinary), {意|い}のまま (at one's will), {一生|いっしょう}{一度|いちど} (once in a lifetime), {一言|ひとこと}{断|ことわ}る (to give a heads-up), をもちまして (as of)
- **Pronouns/Adverbs (2)**: どれも (pronoun), どこにでも (everywhere), {御方|おかた} (person, honorific)
- Removed 7 stale candidates (duplicates: 切り抜き, 上書き保存, 熟す, 何方, 邪魔をする, ましだ, 激高)

### 2026-04-07 (Vocabulary Expansion - 20 New Entries, Session 41)
Added 20 new dictionary entries (IDs 22914-22933) from candidate_words.json. A diverse mix of nouns, expressions, and an adverb covering culture, biology, food, business, law, medicine, and daily life.

- **Nouns (14)**: {生誕|せいたん} (birth/nativity), {被験者|ひけんしゃ} (test subject), {館長|かんちょう} (museum director), {歯科医院|しかいいん} (dental clinic), {特賞|とくしょう} (special prize), {違法駐車|いほうちゅうしゃ} (illegal parking), {事業計画|じぎょうけいかく} (business plan), {旅行者|りょこうしゃ} (traveler), {応募書類|おうぼしょるい} (application documents), {氷砂糖|こおりざとう} (rock sugar), {自然環境|しぜんかんきょう} (natural environment), カプセル (capsule)
- **Noun/suru verbs (3)**: {発刊|はっかん} (publishing), {交尾|こうび} (mating), {増改築|ぞうかいちく} (renovation and expansion)
- **Expressions (2)**: {看板倒|かんばんだお}れ (all show no substance), {面|つら}の{皮|かわ}が{厚|あつ}い (shameless)
- **Adverb (1)**: {暫時|ざんじ} (for a while)
- **Expression (verb-like) (1)**: {息|いき}を{切|き}らす (to be out of breath)

### 2026-04-07 (Vocabulary Expansion - 25 New Entries, Session 40)
Added 25 new dictionary entries (IDs 22889-22913) from candidate_words.json. A practical mix of expressions, nouns, and an adverb covering daily life, culture, business, health, society, and more.

- **Nouns (17)**: {詰|つ}め{替|か}え{用|よう} (refill), {稼|かせ}ぎ{頭|がしら} (top earner), {髭剃|ひげそ}り (razor), {観衆|かんしゅう} (spectators), {卓上|たくじょう} (tabletop), {大入|おおい}り (full house), {会員証|かいいんしょう} (membership card), {経過|けいか}{報告|ほうこく} (progress report), こげ{茶色|ちゃいろ} (dark brown), {共働|ともばたら}き{世帯|せたい} (dual-income household), {汗|あせ}まみれ (soaked in sweat), {健康|けんこう}{増進|ぞうしん} (health promotion), {自虐|じぎゃく}ネタ (self-deprecating joke), {家|いえ}ごもり (staying home), {修正|しゅうせい}テープ (correction tape), {業務|ぎょうむ}{提携|ていけい} (business alliance), {加入者|かにゅうしゃ} (subscriber)
- **Noun/suru verbs (3)**: {初出演|はつしゅつえん} (debut appearance), {新生|しんせい} (rebirth), {読経|どきょう} (sutra chanting)
- **Nouns with legal/medical usage (1)**: {傷害|しょうがい} (injury/assault)
- **Expressions (2)**: {切|き}りがない (endless), {糠|ぬか}に{釘|くぎ} (futile effort)
- **Adverb/onomatopoeia (1)**: しゃきっと (crisply/alertly)
- **Other (1)**: {家族|かぞく}ぐるみ (whole-family involvement)
- Removed 3 stale candidates (duplicates: ブレ, 詰問, 口伝え)
- New kanji: 髭 (beard, ID 02663)

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 39)
Added 30 new dictionary entries (IDs 22859-22888) from candidate_words.json. A diverse mix of nouns, verbs, adverbs, and expressions covering culture, military, communication, grammar, medicine, food, and more.

- **Nouns (21)**: {葉月|はづき} (August, traditional), {一月|ひとつき} (one month), {実父|じっぷ} (biological father), {祝電|しゅくでん} (congratulatory telegram), {弔電|ちょうでん} (condolence telegram), {末梢|まっしょう} (periphery/trivial), {軽業|かるわざ} (acrobatics), {補語|ほご} (complement, grammar), {五七五|ごしちご} (haiku meter), マグ (mug), ガード (guard/overpass), {脱衣|だつい} (undressing), {美男|びなん} (handsome man), {耳鼻科|じびか} (ENT department), {出回|でまわ}り (market availability), {不定|ふてい} (indefinite), {受章|じゅしょう} (receiving a decoration), {助教授|じょきょうじゅ} (associate professor), {一派|いっぱ} (faction), {造幣|ぞうへい} (minting), {拝承|はいしょう} (acknowledged, humble)
- **Noun/suru verbs (7)**: {駐屯|ちゅうとん} (stationing), {屈曲|くっきょく} (bending), {従軍|じゅうぐん} (military service), {除隊|じょたい} (military discharge), {打電|だでん} (telegraphing)
- **Verb (godan) (1)**: {隈取|くまど}る (to apply kumadori makeup)
- **Adverb (1)**: {猛然|もうぜん} (fiercely)
- **Expressions (2)**: {後塵|こうじん}を{拝|はい}する (to fall behind), {命|いのち}を{絶|た}つ (to end one's life)
- Removed 14 stale candidates (duplicates of existing entries)
- New kanji: 屯 (camp, ID 02661), 梢 (treetop, ID 02662)










