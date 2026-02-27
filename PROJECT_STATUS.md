# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-27
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
| Total entries | ~14,024 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,225 (open) |
| Candidate words | ~5,745 |
| Cross-references | ~3,400 |
| Example sentences | ~48,100 |
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

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 339)
Added 30 new dictionary entries (IDs 13939-13968) from candidate_words.json:

- **Nouns (17)**: {胃袋|いぶくろ} (stomach), {胡桃|くるみ} (walnut), {脇道|わきみち} (side road/digression), {自治体|じちたい} (municipality), {良心|りょうしん} (conscience), {色合|いろあ}い (shade/hue), {美意識|びいしき} (aesthetic sense), {聞|き}き{覚|おぼ}え (familiarity from hearing), {腎臓|じんぞう} (kidney), {色彩|しきさい} (color/coloring), {芸人|げいにん} (entertainer), {花吹雪|はなふぶき} (flurry of petals), {脚本家|きゃくほんか} (screenwriter), {義務教育|ぎむきょういく} (compulsory education), {芋虫|いもむし} (caterpillar), {花形|はながた} (star/leading figure), {色調|しきちょう} (color tone)
- **Noun/suru verbs (3)**: {脱却|だっきゃく} (breaking free), {自律|じりつ} (autonomy), {自作|じさく} (self-made)
- **Nouns with two senses (4)**: {胴体|どうたい} (torso + fuselage), {脇道|わきみち} (side road + digression), {色合|いろあ}い (hue + figurative tinge), {色彩|しきさい} (color + character/tone)
- **Noun/adjective (3)**: {良質|りょうしつ} (good quality), {自家製|じかせい} (homemade), {能動的|のうどうてき} (active/proactive)
- **Na-adjective (1)**: {良好|りょうこう} (good/favorable)
- **I-adjective (1)**: {肌寒|はだざむ}い (chilly)
- **Verbs (3)**: {脅|おびや}かす (to threaten, godan), {腰掛|こしか}ける (to sit down, ichidan), {背|そむ}ける (to turn away, ichidan)
- **Noun (literary) (1)**: {芳香|ほうこう} (fragrance)

Notable features:
- Multi-sense entries: {胴体|どうたい} (2: torso + fuselage), {脅|おびや}かす (2: threaten + challenge), {脇道|わきみち} (2: side road + digression), {色合|いろあ}い (2: hue + figurative tinge), {色彩|しきさい} (2: color + character/tone)
- Body/medical: {胃袋|いぶくろ}, {胴体|どうたい}, {腎臓|じんぞう}
- Art/aesthetics: {色合|いろあ}い, {色彩|しきさい}, {色調|しきちょう}, {美意識|びいしき}
- Cultural: {花吹雪|はなふぶき} (cherry blossoms), {芸人|げいにん} (comedy culture), {義務教育|ぎむきょういく}
- Nature: {胡桃|くるみ}, {芋虫|いもむし}, {肌寒|はだざむ}い, {花吹雪|はなふぶき}
- New kanji: 2,441 → 2,443 ({胴|どう}, {腎|じん})

Total entries: 13,994 → 14,024 (approximate)
Remaining candidates: 5,775 → 5,745 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 338)
Added 30 new dictionary entries (IDs 13909-13938) from candidate_words.json:

- **Nouns (16)**: {肩書|かたが}き (title/credential), {聴覚|ちょうかく} (hearing), {肉体|にくたい} (physical body), {羽毛|うもう} (down/feathers), {義足|ぎそく} (prosthetic leg), {耐性|たいせい} (resistance/tolerance), {聖域|せいいき} (sanctuary), {聞|き}き{込|こ}み (inquiry), {職種|しょくしゅ} (job type), {育|そだ}ち (upbringing), {背筋|せすじ} (spine/posture), {脅威|きょうい} (threat), {脇役|わきやく} (supporting role), {肴|さかな} (appetizer), {自前|じまえ} (self-supplied), {習|なら}わし (custom)
- **Noun/suru verbs (7)**: {美化|びか} (beautification), {肥満|ひまん} (obesity), {翻案|ほんあん} (adaptation), {老朽|ろうきゅう} (dilapidation), {脱出|だっしゅつ} (escape), {膠着|こうちゃく} (stalemate), {自称|じしょう} (self-proclaimed)
- **Noun (two senses, 5)**: {美学|びがく} (aesthetics), {肉食|にくしょく} (meat-eating/aggressive), {背伸|せの}び (tiptoe/overreaching), {育成|いくせい} (development), {習性|しゅうせい} (nature/habit)
- **Adverb/noun (1)**: {至極|しごく} (extremely)
- **Expression (1)**: {老若男女|ろうにゃくなんにょ} (all ages)

Notable features:
- Multi-sense entries: {美化|びか} (2: beautification + glorification), {美学|びがく} (2: academic + personal), {肉食|にくしょく} (2: carnivorous + aggressive dating), {聖域|せいいき} (2: sacred place + untouchable area), {背伸|せの}び (2: tiptoe + overreaching), {育|そだ}ち (2: upbringing + growth), {肴|さかな} (2: appetizer + conversation topic), {自前|じまえ} (2: self-owned + self-funded), {習性|しゅうせい} (2: animal instinct + ingrained habit)
- Body/medical: {聴覚|ちょうかく}, {肉体|にくたい}, {義足|ぎそく}, {背筋|せすじ}, {肥満|ひまん}, {耐性|たいせい}
- Work/business: {肩書|かたが}き, {職種|しょくしゅ}, {育成|いくせい}, {自前|じまえ}
- Cultural: {肴|さかな} (sake culture), {老若男女|ろうにゃくなんにょ} (Buddhist reading), {習|なら}わし (traditions)
- New kanji: 2,439 → 2,441 ({脅|きょう}, {膠|こう})

Total entries: 13,964 → 13,994 (approximate)
Remaining candidates: 5,805 → 5,775 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 337)
Added 30 new dictionary entries (IDs 13879-13908) from candidate_words.json:

- **Noun/suru verbs (11)**: {総称|そうしょう} (general term), {結合|けつごう} (combination), {結集|けっしゅう} (rally), {続投|ぞくとう} (continuing in position), {編入|へんにゅう} (incorporation), {編纂|へんさん} (compilation), {緊縮|きんしゅく} (austerity), {罵倒|ばとう} (verbal abuse), {習得|しゅうとく} (mastery), {老化|ろうか} (aging), {考案|こうあん} (devising)
- **Nouns (9)**: {総裁|そうさい} (party president), {素地|そじ} (groundwork), {種族|しゅぞく} (race/tribe), {簡体字|かんたいじ} (simplified Chinese character), {繁体字|はんたいじ} (traditional Chinese character), {美徳|びとく} (virtue), {聴衆|ちょうしゅう} (audience), {職務|しょくむ} (duties), {習|なら}い{事|ごと} (lessons)
- **Na-adjective (1)**: {絶大|ぜつだい} (immense)
- **Godan verbs (5)**: {練|ね}り{歩|ある}く (to parade), {繰|く}り{出|だ}す (to sally forth), {祓|はら}う (to exorcise), {羽|は}ばたく (to flap wings), {羽織|はお}る (to throw on)
- **Intransitive verb (1)**: {翻|ひるがえ}る (to flutter/be reversed)
- **Expression (1)**: {百歩譲|ひゃっぽゆず}って (even granting that)
- **Other nouns (2)**: {置|お}いてけぼり (being left behind), {置|お}き{手紙|てがみ} (note left behind)

Notable features:
- Multi-sense entries: {繰|く}り{出|だ}す (2: go out + unleash), {素地|そじ} (2: groundwork + raw material), {続投|ぞくとう} (2: baseball + politics), {羽|は}ばたく (2: flap wings + spread wings figuratively), {翻|ひるがえ}る (2: flutter + be reversed)
- Cross-reference pairs: {簡体字|かんたいじ}↔{繁体字|はんたいじ}, {祓|はら}う↔{払|はら}う
- Cultural: {祓|はら}う (Shinto purification), {百歩譲|ひゃっぽゆず}って (Chinese idiom origin)
- Sports/politics: {続投|ぞくとう} (baseball → politics), {総裁|そうさい} (party leadership)
- New kanji: 2,436 → 2,439 ({祓|ふつ}, {纂|さん}, {罵|ば})

Total entries: 13,934 → 13,964 (approximate)
Remaining candidates: 5,835 → 5,805 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 336)
Added 30 new dictionary entries (IDs 13849-13878) from candidate_words.json:

- **Nouns (14)**: {素行|そこう} (conduct), {終身雇用|しゅうしんこよう} (lifetime employment), {結界|けっかい} (spiritual barrier), {白|しろ} (white/innocence), {総会|そうかい} (general meeting), {総理|そうり} (prime minister), {粉雪|こなゆき} (powder snow), {繭|まゆ} (cocoon), {紅|べに} (rouge/crimson), {紋|もん} (crest/pattern), {絵文字|えもじ} (emoji), {絵柄|えがら} (design/art style), {罫線|けいせん} (ruled line), {絵師|えし} (illustrator)
- **Noun/suru verbs (10)**: {納付|のうふ} (payment), {終結|しゅうけつ} (conclusion), {続出|ぞくしゅつ} (appearing in succession), {線引|せんび}き (drawing a line/distinction), {統率|とうそつ} (leadership), {締結|ていけつ} (signing of treaty), {累積|るいせき} (accumulation), {粉砕|ふんさい} (pulverization), {総括|そうかつ} (summary/review), {続報|ぞくほう} (follow-up report)
- **Nouns (other) (5)**: {維新|いしん} (restoration/reform), {縦書|たてが}き (vertical writing), {絶好|ぜっこう} (best/ideal), {素性|すじょう} (origin/identity), {繊維|せんい} (fiber/textile)
- **Ichidan verb (1)**: {経|へ}る (to pass through/elapse)

Notable features:
- Multi-sense entries: {結界|けっかい} (2: sacred boundary + magical barrier), {白|しろ} (2: white + innocence), {紅|べに} (2: rouge + crimson color), {紋|もん} (2: family crest + pattern), {絵柄|えがら} (2: design + art style), {線引|せんび}き (2: drawing lines + making distinctions), {粉砕|ふんさい} (2: physical crushing + figurative destruction), {繊維|せんい} (2: biological fiber + textile), {経|へ}る (2: pass through + time elapses), {絵師|えし} (2: traditional painter + digital illustrator)
- Cultural: {終身雇用|しゅうしんこよう} (Japanese employment culture), {維新|いしん} (Meiji Restoration), {縦書|たてが}き (Japanese writing direction), {紋|もん} (family crests), {繭|まゆ} (silk industry), {結界|けっかい} (Buddhist/anime term)
- Modern: {絵文字|えもじ} (emoji origin), {絵師|えし} (digital art culture), {絵柄|えがら} (manga/anime discussion)
- Business/legal: {納付|のうふ}, {総会|そうかい}, {総理|そうり}, {締結|ていけつ}, {累積|るいせき}, {総括|そうかつ}
- New kanji: 2,434 → 2,436 ({繭|けん}, {罫|けい})

Total entries: 13,904 → 13,934 (approximate)
Remaining candidates: 5,865 → 5,835 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 335)
Added 30 new dictionary entries (IDs 13819-13848) from candidate_words.json:

- **Na-adjectives (2)**: {穏和|おんわ} (gentle/mild), {粗野|そや} (crude/boorish)
- **Nouns (16)**: {精霊|せいれい} (spirit), {紀元|きげん} (era/epoch), {紀行|きこう} (travelogue), {看板娘|かんばんむすめ} (poster girl), {紋章|もんしょう} (coat of arms), {秘宝|ひほう} (hidden treasure), {系譜|けいふ} (genealogy), {紀元前|きげんぜん} (B.C.), {箇条|かじょう} (item/clause), {真骨頂|しんこっちょう} (true worth), {禊|みそぎ} (purification ritual), {祠|ほこら} (small shrine), {縛|しば}り (binding/restriction), {絶頂|ぜっちょう} (peak/summit), {縁談|えんだん} (marriage proposal), {系列|けいれつ} (series/keiretsu)
- **Noun/suru verbs (10)**: {直送|ちょくそう} (direct delivery), {管轄|かんかつ} (jurisdiction), {直立|ちょくりつ} (standing upright), {直轄|ちょっかつ} (direct control), {終焉|しゅうえん} (end/demise), {絶賛|ぜっさん} (high praise), {継承|けいしょう} (succession), {統治|とうち} (governance), {緩和|かんわ} (alleviation), {給付|きゅうふ} (benefit payment)
- **Adverb (1)**: {総|そう}じて (generally)
- **Noun (literary) (1)**: {発露|はつろ} (manifestation)

Notable features:
- Multi-sense entries: {精霊|せいれい} (2: nature spirit + Obon spirit), {紀元|きげん} (2: epoch + A.D.), {禊|みそぎ} (2: ritual + political atonement), {縛|しば}り (2: physical binding + restriction/rule), {絶頂|ぜっちょう} (2: mountain summit + zenith)
- Cultural: {禊|みそぎ} (Shinto purification, political usage), {祠|ほこら} (wayside shrines), {看板娘|かんばんむすめ} (Edo-era concept), {精霊|しょうりょう} (Obon), {紋章|もんしょう} (heraldry)
- Business/legal: {管轄|かんかつ}, {直轄|ちょっかつ}, {系列|けいれつ} (keiretsu corporate groups), {給付|きゅうふ} (government benefits), {統治|とうち}
- Historical: {紀元|きげん}/{紀元前|きげんぜん} (calendar systems), {継承|けいしょう}, {終焉|しゅうえん}
- New kanji: 2,430 → 2,434 ({焉|えん}, {祠|し}, {禊|けい}, {轄|かつ})

Total entries: 13,874 → 13,904 (approximate)
Remaining candidates: 5,895 → 5,865 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
