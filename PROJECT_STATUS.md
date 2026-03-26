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

### 2026-03-26 (Vocabulary Expansion - 20 New Entries, Session 506)
Added 20 new dictionary entries (IDs 19606-19625) from candidate_words.json. Focused on useful intermediate-level vocabulary across a range of semantic areas.

- **Nouns (11)**: {鼓動|こどう} (heartbeat), {模範|もはん} (model/exemplar), {威力|いりょく} (power/might), {猟師|りょうし} (hunter), {家路|いえじ} (road home), {画鋲|がびょう} (thumbtack), {赤身|あかみ} (lean meat), {黒糖|こくとう} (brown sugar), {菜園|さいえん} (vegetable garden), {集落|しゅうらく} (village/settlement), {代打|だいだ} (pinch hitter)
- **Nouns/Suru verbs (4)**: {読破|どくは} (reading through), {撲滅|ぼくめつ} (eradication), {一望|いちぼう} (sweeping view), {必読|ひつどく} (must-read)
- **Noun/Na-adj (2)**: {不服|ふふく} (dissatisfaction), {鋭利|えいり} (sharp/keen)
- **Na-adjective (1)**: {雄大|ゆうだい} (grand/magnificent)
- **Season/Time (2)**: {晩夏|ばんか} (late summer), {支流|しりゅう} (tributary)
- 1 new kanji added to index: 鋲

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 505)
Added 30 new dictionary entries (IDs 19576-19605) from candidate_words.json. Focused on verbs, literary terms, and useful vocabulary across a range of domains.

- **Verbs (17)**: {背|そむ}く (defy/betray), {汗|あせ}ばむ (become sweaty), {濁|にご}す (make muddy/speak vaguely), {揺|ゆ}るぐ (shake/waver), {薫|かお}る (be fragrant), {綴|と}じる (bind/staple), {見誤|みあやま}る (misjudge), {挫|くじ}く (sprain/crush spirits), {商|あきな}う (trade), {退|しりぞ}ける (repel/reject), {障|さわ}る (hinder/offend), {投|とう}じる (throw in/invest/cast vote), {下向|したむ}く (look down), {跳|と}ぶ (jump/leap), {治|なお}る (heal/recover), {延|の}びる (be postponed/extended), {禁|きん}ずる (forbid/suppress)
- **Nouns/Suru (3)**: {満喫|まんきつ} (thorough enjoyment), {錯綜|さくそう} (entanglement), {公言|こうげん} (public declaration)
- **Nouns (7)**: {聞|き}き{役|やく} (listener role), {一般論|いっぱんろん} (generalization), {涼感|りょうかん} (cool feeling), {既述|きじゅつ} (already stated), {決算書|けっさんしょ} (financial statement), {余情|よじょう} (lingering feeling), {枯淡|こたん} (refined simplicity)
- **Other (3)**: {米国|べいこく} (United States), {高等教育|こうとうきょういく} (higher education), {虚飾|きょしょく} (vanity/ostentation)
- 1 new kanji added to index: 綜

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 504)
Added 30 new dictionary entries (IDs 19546-19575) from candidate_words.json. Focused on useful words for intermediate learners spanning emotions, daily life, culture, and practical vocabulary.

- **Verbs (7)**: {引|ひ}きこもる (withdraw/shut in), {繁盛|はんじょう}する (prosper), {浮上|ふじょう}する (surface/emerge), {照|て}りつける (blaze down), ひねくれる (become twisted/perverse), {恐縮|きょうしゅく}する (feel obliged), {仕切|しき}り{直|なお}す (start over)
- **Nouns (9)**: クリーニング (dry cleaning), アンテナ (antenna), {連帯感|れんたいかん} (solidarity), {果肉|かにく} (fruit flesh), {涙声|なみだごえ} (tearful voice), {入国審査|にゅうこくしんさ} (immigration), {追|お}っかけ (devoted fan), {円|えん}グラフ (pie chart), {生活習慣|せいかつしゅうかん} (lifestyle habits)
- **Nouns (continued, 5)**: {病原体|びょうげんたい} (pathogen), {良策|りょうさく} (good plan), {思|おも}い{過|す}ごし (overthinking), {果皮|かひ} (fruit peel), {鳥籠|とりかご} (birdcage)
- **Noun/Suru (1)**: {雪辱|せつじょく} (vindication)
- **Expressions (3)**: {呆然|ぼうぜん}とする (be stunned), {度|ど}が{過|す}ぎる (go too far), {感無量|かんむりょう} (deeply moved)
- **Na-adjective (2)**: {不親切|ふしんせつ} (unkind), {背中合|せなかあ}わせ (back to back)
- **Adverbs (3)**: {時々刻々|じじこっこく} (moment by moment), ついうっかり (carelessly), {何|なに}はともあれ (anyway)



---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
