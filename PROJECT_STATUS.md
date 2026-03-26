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

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 503)
Added 30 new dictionary entries (IDs 19516-19545) from candidate_words.json. Focused on practical, high-utility words for intermediate learners — emotions, social behavior, common expressions, and everyday verbs.

- **Expressions (7)**: {機嫌|きげん}が{悪|わる}い (in a bad mood), {納得|なっとく}がいかない (can't accept), {気|き}が{気|き}でない (anxious), {気|き}が{楽|らく} (at ease), {愛想|あいそ}を{尽|つ}かす (fed up with), {後|うし}ろ{髪|がみ}を{引|ひ}かれる (reluctant to leave), {丁重|ていちょう}に{断|ことわ}る (politely decline)
- **Verbs (7)**: {面白|おもしろ}がる (find amusing), {遠慮|えんりょ}する (refrain), {謝罪|しゃざい}する (apologize formally), {拒絶|きょぜつ}する (reject), {変色|へんしょく}する (discolor), {波及|はきゅう}する (spread/ripple out), {絞|しぼ}り{出|だ}す (squeeze out)
- **Nouns (5)**: {侵入者|しんにゅうしゃ} (intruder), {積極性|せっきょくせい} (proactiveness), {利害関係|りがいかんけい} (interests/stakes), {感想文|かんそうぶん} (book report), {習慣化|しゅうかんか} (habituation)
- **Adjectives (2)**: {心細|こころぼそ}い (anxious/helpless), {心|こころ}もとない (uncertain/uneasy)
- **Na-adjectives/Nouns (3)**: {高慢|こうまん} (arrogant), {独|ひと}りぼっち (all alone), ハイテンション (excited/hyper)
- **Other (4)**: でございます (polite copula), お{天気屋|てんきや} (moody person), {入会|にゅうかい}する (join/enroll), {侵|おか}す (invade/violate)
- **Verbs with cross-refs**: {積|つ}み{重|かさ}なる (pile up, with transitive pair), {移|うつ}り{変|か}わる (change gradually), {侵|おか}す (with homophone cross-refs to {犯|おか}す and {冒|おか}す)

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 502)
Added 30 new dictionary entries (IDs 19486-19515) from candidate_words.json. A diverse mix of expressions, nouns, and adverbs covering daily life, culture, health, nature, and abstract concepts.

- **Expressions (10)**: {折|おり}に{触|ふ}れて (on occasion), {元気|げんき}がない (listless), {落|お}ち{着|つ}かない (restless), {口火|くちび}を{切|き}る (to start things off), {心|こころ}ここにあらず (absentminded), {期限|きげん}が{切|き}れる (to expire), {言葉|ことば}を{交|か}わす (to exchange words), {役割|やくわり}を{果|は}たす (to fulfill a role)
- **Nouns (15)**: {勝手口|かってぐち} (kitchen door), {因果関係|いんがかんけい} (causal relationship), {血糖値|けっとうち} (blood sugar level), {炭酸飲料|たんさんいんりょう} (carbonated beverage), {徳利|とっくり} (sake bottle), {豆類|まめるい} (legumes), {虚空|こくう} (void), {音漏|おとも}れ (sound leakage), {通信簿|つうしんぼ} (report card), {夕映|ゆうば}え (sunset glow), {青菜|あおな} (leafy greens), {後頭部|こうとうぶ} (back of the head), {生|は}え{際|ぎわ} (hairline), ご{祝儀袋|しゅうぎぶくろ} (gift money envelope), {適者生存|てきしゃせいぞん} (survival of the fittest)
- **Noun/Suru verbs (3)**: {沈静化|ちんせいか} (calming down), バトンタッチ (handover), {品種改良|ひんしゅかいりょう} (selective breeding)
- **Adverbs (2)**: {急|いそ}いで (hurriedly), {皆目|かいもく} (not at all)
- **Na-adjective (1)**: {自分勝手|じぶんかって} (selfish)
- **Other (1)**: {一切合切|いっさいがっさい} (absolutely everything)



---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
