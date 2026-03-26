# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-25
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
| Total entries | ~19,058 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,259 (open) |
| Candidate words | ~5,099 |
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

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 511)
Added 30 new dictionary entries (IDs 19729-19758) from candidate_words.json. Mixed vocabulary including particles, expressions, business terms, and cultural vocabulary.

- **Particles (2)**: くせに (despite/critical tone), ものの (although/even though)
- **Expressions (4)**: {言|い}うまでもなく (it goes without saying), どっちにしろ (either way), {首|くび}を{横|よこ}に{振|ふ}る (to shake one's head), {居|い}ても{立|た}っても{居|い}られない (unable to sit still)
- **Nouns (20)**: ピンボケ (out of focus), {許容範囲|きょようはんい} (acceptable range), {親会社|おやがいしゃ} (parent company), {更|さら}には (furthermore), {度数|どすう} (frequency/alcohol content), お{門違|かどちが}い (barking up the wrong tree), {建|た}て{替|か}え (rebuilding), {勧善懲悪|かんぜんちょうあく} (poetic justice), マーガリン (margarine), {迷惑行為|めいわくこうい} (nuisance behavior), {油性|ゆせい}ペン (permanent marker), {掛|か}け{時計|どけい} (wall clock), {都市計画|としけいかく} (urban planning), {四半世紀|しはんせいき} (quarter century), {手順書|てじゅんしょ} (procedure manual), {草食動物|そうしょくどうぶつ} (herbivore), {産出|さんしゅつ} (production/yield), {着色料|ちゃくしょくりょう} (coloring agent), {祭礼|さいれい} (religious festival), {関連会社|かんれんがいしゃ} (affiliated company)
- **Other (4)**: {不健全|ふけんぜん} (unhealthy/na-adj), {碁石|ごいし} (Go stone), {壮年|そうねん} (prime of life), {予定|よてい}が{詰|つ}まる (packed schedule)
- Removed 3 stale candidates (雑な, 滑らかな, 無数の — already exist as entries)

### 2026-03-26 (Vocabulary Expansion - 14 New Entries, Session 509)
Added 14 new dictionary entries (IDs 19686-19699) from candidate_words.json. Diverse mix of daily-life vocabulary, verbs, and cultural terms.

- **Nouns (10)**: {部屋着|へやぎ} (loungewear), {一戸建|いっこだ}て (detached house), {学園祭|がくえんさい} (school festival), {仕事仲間|しごとなかま} (work colleague), {懇談会|こんだんかい} (informal meeting), {体臭|たいしゅう} (body odor), {内勤|ないきん} (desk work), {大家族|だいかぞく} (large family), {第一志望|だいいちしぼう} (first choice), {図工|ずこう} (arts and crafts)
- **Verbs (4)**: {遠|とお}ざける (to keep away), ちらつく (to flicker), {埋|うず}もれる (to be buried in), {持|も}ち{運|はこ}ぶ (to carry around)
- Removed 1 stale candidate ({間取|まど}り — already exists as entry 06078)

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 508)
Added 30 new dictionary entries (IDs 19656-19685) from candidate_words.json. Diverse mix of useful intermediate vocabulary including expressions, cultural terms, and formal language.

- **Expressions (6)**: かしこまりました (understood/humble), {口|くち}を{滑|すべ}らせる (let something slip), {先見|せんけん}の{明|めい} (foresight), {羽振|はぶ}りがいい (prosperous), {白紙|はくし}に{戻|もど}す (go back to square one), {信|しん}じ{難|がた}い (hard to believe)
- **Nouns (15)**: {結婚祝|けっこんいわ}い (wedding gift), {秋分|しゅうぶん} (autumnal equinox), {若葉|わかば} (young leaves), {顔|かお}つき (facial expression), {施術|しじゅつ} (medical procedure), {支柱|しちゅう} (pillar/support), {流域|りゅういき} (river basin), {石器|せっき} (stone tool), {飼料|しりょう} (animal feed), {道幅|みちはば} (road width), {年俸|ねんぽう} (annual salary), {石垣|いしがき} (stone wall), {岸壁|がんぺき} (quay wall), {再出発|さいしゅっぱつ} (fresh start), {案内状|あんないじょう} (invitation letter)
- **Nouns/Verbal nouns (4)**: {屈服|くっぷく} (submission), {併合|へいごう} (annexation), {退廃|たいはい} (decadence), {準拠|じゅんきょ}する (conform to)
- **Adjectives (3)**: {寒冷|かんれい} (cold/frigid), {耐|た}え{難|がた}い (unbearable), {受|う}け{身|み} (passive)
- **Other (2)**: {何卒|なにとぞ} (please/formal), {生身|なまみ} (flesh and blood)
- 1 new kanji added to index: 俸
- Removed 1 stale candidate (活発 — already exists as entry 13272)

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 507)
Added 30 new dictionary entries (IDs 19626-19655) from candidate_words.json. Focused on common する verbs and practical nouns useful for intermediate learners.

- **Suru verbs (27)**: {限定|げんてい}する (to limit), {抽出|ちゅうしゅつ}する (to extract), {把握|はあく}する (to grasp), {特化|とっか}する (to specialize), {密集|みっしゅう}する (to be densely packed), {告白|こくはく}する (to confess), {促進|そくしん}する (to promote), {稼働|かどう}する (to operate), {実施|じっし}する (to implement), {規制|きせい}する (to regulate), {制限|せいげん}する (to restrict), {加熱|かねつ}する (to heat), {誤解|ごかい}する (to misunderstand), {共有|きょうゆう}する (to share), {共感|きょうかん}する (to empathize), {緩和|かんわ}する (to ease), {特定|とくてい}する (to identify), {配達|はいたつ}する (to deliver), {提出|ていしゅつ}する (to submit), {通知|つうち}する (to notify), {追加|ついか}する (to add), {固定|こてい}する (to fix), {一致|いっち}する (to match), {空想|くうそう}する (to fantasize), {反射|はんしゃ}する (to reflect), {予測|よそく}する (to predict), {阻止|そし}する (to prevent)
- **Nouns (3)**: {密閉|みっぺい} (airtight seal), {転校生|てんこうせい} (transfer student), {想定内|そうていない} (within expectations)

### 2026-03-26 (Vocabulary Expansion - 29 New Entries, Session 510)
Added 29 new dictionary entries (IDs 19700-19728) from candidate_words.json. Mixed vocabulary including adjectives, expressions, compass directions, and formal nouns.

- **Nouns (14)**: {無機質|むきしつ} (inorganic/cold), {垢|あか} (grime), {略図|りゃくず} (rough sketch), {学区|がっく} (school district), {医薬品|いやくひん} (pharmaceutical), {護身|ごしん} (self-defense), {北東|ほくとう} (northeast), {南西|なんせい} (southwest), {安打|あんだ} (base hit), {多方面|たほうめん} (many fields), {食糧難|しょくりょうなん} (food shortage), {印字|いんじ} (printing), {細断|さいだん} (shredding), {裁定|さいてい} (ruling)
- **Suru verbs (6)**: {絶食|ぜっしょく}する (to fast), {包囲|ほうい}する (to surround), {献身|けんしん}する (to devote oneself), {激賞|げきしょう}する (high praise), {慶祝|けいしゅく}する (to celebrate), {傾注|けいちゅう}する (to devote effort)
- **Verbs (1)**: {化|ば}かす (to trick/bewitch)
- **Adjectives (2)**: ねちっこい (persistent/clingy), {多面的|ためんてき} (multifaceted)
- **Expressions (2)**: {伊達眼鏡|だてめがね} (fashion glasses), {自縄自縛|じじょうじばく} (caught in one's own trap), {心|こころ}に{銘|めい}じる (to take to heart), {少|すこ}しでも (even a little), {入職|にゅうしょく} (entering employment), {着岸|ちゃくがん} (docking)
- 2 new kanji added to index: 伊, 慶
- Removed 1 stale candidate (身の上話 — already exists as entry 19137)
- **Nouns/Suru (3)**: {満喫|まんきつ} (thorough enjoyment), {錯綜|さくそう} (entanglement), {公言|こうげん} (public declaration)
- **Nouns (7)**: {聞|き}き{役|やく} (listener role), {一般論|いっぱんろん} (generalization), {涼感|りょうかん} (cool feeling), {既述|きじゅつ} (already stated), {決算書|けっさんしょ} (financial statement), {余情|よじょう} (lingering feeling), {枯淡|こたん} (refined simplicity)
- **Other (3)**: {米国|べいこく} (United States), {高等教育|こうとうきょういく} (higher education), {虚飾|きょしょく} (vanity/ostentation)
- 1 new kanji added to index: 綜



---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
