# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-28
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
| Total entries | ~14,174 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,375 (open) |
| Candidate words | ~5,595 |
| Cross-references | ~3,400 |
| Example sentences | ~48,600 |
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

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 344)
Added 30 new dictionary entries (IDs 14089-14118) from candidate_words.json:

- **Nouns (17)**: {草木|くさき} (plants/vegetation), {製菓|せいか} (confectionery making), {街路|がいろ} (street), {群像|ぐんぞう} (group portrait/ensemble), {表題|ひょうだい} (title/heading), {薬剤|やくざい} (pharmaceutical), {苦味|にがみ} (bitterness), {衣装|いしょう} (costume), {被害者|ひがいしゃ} (victim), {落|お}ち{葉|ば} (fallen leaves), {見|み}た{目|め} (appearance), {見|み}せ{場|ば} (highlight), {覇権|はけん} (hegemony), {褐色|かっしょく} (brown), {茶会|ちゃかい} (tea gathering), {英雄|えいゆう} (hero), {薪|まき} (firewood)
- **Noun/suru verbs (5)**: {装備|そうび} (equipment/equipping), {装飾|そうしょく} (decoration), {補助|ほじょ} (assistance/subsidy), {要望|ようぼう} (request/demand), {複合|ふくごう} (compound/composite)
- **Na-adjective (2)**: {荒唐無稽|こうとうむけい} (absurd), {美麗|びれい} (beautiful/gorgeous)
- **Noun (2 senses, 4)**: {裏打|うらう}ち (backing + substantiation), {群像|ぐんぞう} (art + ensemble), {要領|ようりょう} (knack + gist), {補助|ほじょ} (assistance + subsidy)
- **Ichidan verb (1)**: {薄|うす}れる (to fade/weaken)
- **Noun (other, 3)**: {薄給|はっきゅう} (low salary), {蒸|む}し{風呂|ぶろ} (steam bath), {絵巻|えまき} (picture scroll)

Notable features:
- Multi-sense entries: {裏打|うらう}ち (2: lining + substantiation), {装備|そうび} (2: equipment + equipping), {補助|ほじょ} (2: assistance + subsidy), {薄|うす}れる (2: physical fading + abstract weakening), {要領|ようりょう} (2: knack + gist)
- Four-character compound: {荒唐無稽|こうとうむけい}
- Food/taste: {苦味|にがみ}, {製菓|せいか}
- Arts/culture: {絵巻|えまき}, {群像|ぐんぞう}, {茶会|ちゃかい}, {美麗|びれい}
- Work/society: {薄給|はっきゅう}, {被害者|ひがいしゃ}, {覇権|はけん}, {要望|ようぼう}
- Nature/seasons: {草木|くさき}, {落|お}ち{葉|ば}
- New kanji: 2,449 → 2,451 ({薪|しん}, {褐|かつ})

Total entries: 14,144 → 14,174 (approximate)
Remaining candidates: 5,625 → 5,595 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 343)
Added 30 new dictionary entries (IDs 14059-14088) from candidate_words.json:

- **Godan verbs (3)**: {花開|はなひら}く (to bloom/flourish), {脱|ぬ}がす (to undress someone), {薄|うす}まる (to become diluted)
- **Ichidan verb (1)**: {舞|ま}い{降|お}りる (to swoop down)
- **Nouns (14)**: {神髄|しんずい} (essence), {禅宗|ぜんしゅう} (Zen Buddhism), {能楽|のうがく} (noh theater), {神事|しんじ} (Shinto ritual), {群青|ぐんじょう} (ultramarine blue), {肉筆|にくひつ} (handwriting), {習俗|しゅうぞく} (customs), {老年|ろうねん} (old age), {艦隊|かんたい} (fleet), {背徳|はいとく} (immorality), {神楽|かぐら} (kagura), {蘊蓄|うんちく} (extensive knowledge), {著書|ちょしょ} (written work), {蜜|みつ} (honey/nectar)
- **Noun/suru verbs (2)**: {補完|ほかん} (supplementation), {行使|こうし} (exercise of power)
- **Noun/na-adjectives (4)**: {美形|びけい} (good-looking), {縦横無尽|じゅうおうむじん} (freely in all directions), {荒削|あらけず}り (rough-hewn), {表裏一体|ひょうりいったい} (two sides of same coin)
- **Noun/verb-suru (1)**: {膝枕|ひざまくら} (lap pillow)
- **Noun/prefix (1)**: {自家|じか} (one's own/home-made)
- **Noun (business) (1)**: {自社|じしゃ} (one's own company)
- **Noun (cultural) (2)**: {茶室|ちゃしつ} (tea room), {茶|ちゃ}の{湯|ゆ} (tea ceremony)
- **Noun (political) (1)**: {草|くさ}の{根|ね} (grassroots)

Notable features:
- Multi-sense entries: {花開|はなひら}く (2: bloom + flourish), {荒削|あらけず}り (2: rough-hewn + unpolished talent)
- Japanese culture: {禅宗|ぜんしゅう}, {能楽|のうがく}, {神事|しんじ}, {神楽|かぐら}, {茶室|ちゃしつ}, {茶|ちゃ}の{湯|ゆ}
- Four-character compounds: {縦横無尽|じゅうおうむじん}, {表裏一体|ひょうりいったい}
- Arts/writing: {肉筆|にくひつ}, {群青|ぐんじょう}, {著書|ちょしょ}
- New kanji: 2,447 → 2,449 ({艦|かん}, {蘊|うん})

Total entries: 14,114 → 14,144 (approximate)
Remaining candidates: 5,655 → 5,625 (30 removed)

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
