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
| Total entries | ~14,114 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,315 (open) |
| Candidate words | ~5,655 |
| Cross-references | ~3,400 |
| Example sentences | ~48,400 |
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

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 342)
Added 30 new dictionary entries (IDs 14029-14058) from candidate_words.json:

- **Noun/suru verbs (9)**: {蘇生|そせい} (resuscitation), {衰弱|すいじゃく} (debilitation), {融合|ゆうごう} (fusion), {補充|ほじゅう} (replenishment), {落下|らっか} (fall/drop), {表明|ひょうめい} (declaration), {補給|ほきゅう} (supply), {行|い}き{来|き} (coming and going), {落書|らくが}き (graffiti)
- **Nouns (11)**: {裏話|うらばなし} (behind-the-scenes story), {薬草|やくそう} (medicinal herb), {血縁|けつえん} (blood relation), {製法|せいほう} (manufacturing method), {街道|かいどう} (highway), {菜|な}の{花|はな} (rapeseed flower), {蜂蜜|はちみつ} (honey), {装束|しょうぞく} (costume), {衛生|えいせい} (hygiene), {薬物|やくぶつ} (drug), {英気|えいき} (vigor)
- **Noun/na-adjective (4)**: {裏腹|うらはら} (contrary), {行方不明|ゆくえふめい} (missing), {蒼白|そうはく} (pale/pallid), {裏返|うらがえ}し (inside out)
- **Na-adjective (1)**: {裕福|ゆうふく} (wealthy)
- **Noun (literary) (1)**: {装|よそお}い (attire/appearance)
- **Noun/suru verb (formal, 1)**: {虚偽|きょぎ} (falsehood)
- **Noun/suru verb (social, 1)**: {虐待|ぎゃくたい} (abuse)
- **Ichidan verb (1)**: {裏付|うらづ}ける (to substantiate)
- **Godan verb (1)**: {荒|あ}らす (to devastate)

Notable features:
- Multi-sense entries: {裏返|うらがえ}し (2: inside out + flip side), {装|よそお}い (2: attire + guise), {荒|あ}らす (2: devastate + ransack)
- Medical/health: {蘇生|そせい} (CPR), {衰弱|すいじゃく}, {衛生|えいせい}, {薬物|やくぶつ}, {薬草|やくそう}
- Legal/formal: {虚偽|きょぎ}, {虐待|ぎゃくたい}, {表明|ひょうめい}, {裏付|うらづ}ける
- Cultural: {街道|かいどう} (Edo highways), {装束|しょうぞく} (traditional costumes), {菜|な}の{花|はな} (spring tradition)
- Food: {蜂蜜|はちみつ}, {菜|な}の{花|はな}, {製法|せいほう}
- New kanji: 2,445 → 2,447 ({蒼|そう}, {虐|ぎゃく})

Total entries: 14,084 → 14,114 (approximate)
Remaining candidates: 5,685 → 5,655 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 341)
Added 30 new dictionary entries (IDs 13999-14028) from candidate_words.json:

- **Godan verbs (5)**: {興|おこ}す (to start/revive), {舞|ま}い{戻|もど}る (to come back), {聞|き}かす (to tell/let hear), {若返|わかがえ}る (to rejuvenate), {行|い}き{交|か}う (to come and go)
- **Ichidan verb (1)**: {聞|き}きつける (to hear about)
- **Nouns (14)**: {脇腹|わきばら} (flank), {舶来|はくらい} (imported goods), {航空機|こうくうき} (aircraft), {肉団子|にくだんご} (meatball), {至上|しじょう} (supreme), {苗字|みょうじ} (surname), {自国|じこく} (one's own country), {美貌|びぼう} (beauty), {老女|ろうじょ} (old woman), {花鳥|かちょう} (flowers and birds), {茶屋|ちゃや} (teahouse), {裏技|うらわざ} (secret trick/hack), {著作権|ちょさくけん} (copyright), {街灯|がいとう} (streetlight)
- **Noun/suru verbs (5)**: {肉薄|にくはく} (closing in on), {自戒|じかい} (self-admonition), {蓄積|ちくせき} (accumulation), {補強|ほきょう} (reinforcement), {薄着|うすぎ} (light clothing)
- **Nouns (literary/cultural) (3)**: {義憤|ぎふん} (righteous indignation), {苦渋|くじゅう} (anguish), {花道|はなみち} (kabuki runway/glorious exit)
- **Nouns (other) (2)**: {荒波|あらなみ} (rough waves), {血統|けっとう} (lineage)

Notable features:
- Multi-sense entries: {興|おこ}す (2: start + revive), {花道|はなみち} (2: kabuki runway + glorious exit)
- Verbs: Good mix of godan and ichidan with transitivity/aspect notes
- Cultural: {舶来|はくらい} (Meiji import culture), {花道|はなみち} (kabuki), {茶屋|ちゃや} (traditional teahouse), {花鳥|かちょう} (classical aesthetics)
- Modern/practical: {裏技|うらわざ} (life hack), {著作権|ちょさくけん} (copyright law), {航空機|こうくうき}
- Body: {脇腹|わきばら}
- Food: {肉団子|にくだんご}
- New kanji: 2,444 → 2,445 ({舶|はく})

Total entries: 14,054 → 14,084 (approximate)
Remaining candidates: 5,715 → 5,685 (30 removed)

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

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 340)
Added 30 new dictionary entries (IDs 13969-13998) from candidate_words.json:

- **Nouns (14)**: {航路|こうろ} (sea/air route), {花言葉|はなことば} (language of flowers), {腹心|ふくしん} (confidant), {自室|じしつ} (one's own room), {致命傷|ちめいしょう} (fatal wound), {義弟|ぎてい} (brother-in-law), {純文学|じゅんぶんがく} (literary fiction), {罪人|ざいにん} (criminal/sinner), {船頭|せんどう} (boatman), {花|はな}びら (flower petal), {蔵|くら} (storehouse), {蓄|たくわ}え (savings), {蓮根|れんこん} (lotus root), {落|お}ち{目|め} (decline)
- **Noun/suru verbs (5)**: {自白|じはく} (confession), {自立|じりつ} (independence), {脱帽|だつぼう} (hats off), {苦戦|くせん} (hard fight), {興行|こうぎょう} (public performance)
- **Noun/no-adjective (3)**: {臨床|りんしょう} (clinical), {自主|じしゅ} (independent/voluntary), {若手|わかて} (young talent)
- **Na-adjective (2)**: {艶|あで}やか (gorgeous/elegant), {著名|ちょめい} (famous/renowned)
- **I-adjectives (2)**: {色|いろ}っぽい (sexy/alluring), {荒々|あらあら}しい (rough/wild)
- **Verbs (2)**: {興|きょう}じる (to enjoy, ichidan), {芽吹|めぶ}く (to bud/sprout, godan)
- **Noun (pioneering) (1)**: {草分|くさわ}け (pioneer/trailblazer)

Notable features:
- Multi-sense entries: {脱帽|だつぼう} (2: removing hat + admiration), {致命傷|ちめいしょう} (2: fatal wound + decisive damage), {罪人|ざいにん} (2: criminal + sinner)
- Nature/plants: {花|はな}びら, {花言葉|はなことば}, {芽吹|めぶ}く, {蓮根|れんこん}, {荒々|あらあら}しい
- Cultural: {船頭|せんどう} (proverb), {純文学|じゅんぶんがく} (Akutagawa/Naoki Prizes), {蔵|くら} (traditional architecture), {花言葉|はなことば}
- Legal/formal: {自白|じはく}, {罪人|ざいにん}, {臨床|りんしょう}
- Social/career: {若手|わかて}, {自立|じりつ}, {自主|じしゅ}, {落|お}ち{目|め}, {草分|くさわ}け
- New kanji: 2,443 → 2,444 ({蓮|れん})

Total entries: 14,024 → 14,054 (approximate)
Remaining candidates: 5,745 → 5,715 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
