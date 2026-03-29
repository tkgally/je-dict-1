# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-29
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

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 536)
Added 30 new dictionary entries (IDs 20433-20462) from candidate_words.json. A mix of idioms, expressions, practical nouns, and adverbs for intermediate learners.

- **Expressions (8)**: さじを{投|な}げる (to give up), {満面|まんめん}の{笑|え}み (beaming smile), {似|に}たり{寄|よ}ったり (much the same), {胸|むね}が{熱|あつ}くなる (to be deeply moved), {恩|おん}を{仇|あだ}で{返|かえ}す (to repay kindness with evil), {継続|けいぞく}は{力|ちから}なり (persistence pays off)
- **Adverbs (2)**: ともすれば (apt to/tending to), {何度|なんど}も (many times)
- **Nouns (20)**: {紙一重|かみひとえ} (paper-thin difference), {自己責任|じこせきにん} (self-responsibility), {予告編|よこくへん} (trailer/preview), {候補者|こうほしゃ} (candidate), {応募者|おうぼしゃ} (applicant), {責任感|せきにんかん} (sense of responsibility), ひねり (twist/ingenuity), {窓辺|まどべ} (by the window), {冷|ひ}え{込|こ}み (cold snap), {好景気|こうけいき} (economic boom), {自主性|じしゅせい} (independence/initiative), {柑橘|かんきつ} (citrus), {直営店|ちょくえいてん} (company-operated store), {発疹|はっしん} (rash), {分別|ふんべつ} (discretion), {経済成長|けいざいせいちょう} (economic growth), {遠隔操作|えんかくそうさ} (remote operation), {調理法|ちょうりほう} (cooking method), {薄毛|うすげ} (thinning hair), {新参|しんざん} (newcomer), {記入漏|きにゅうも}れ (omission in form), {自己負担|じこふたん} (out-of-pocket expense)
- Removed 30 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 535)
Added 30 new dictionary entries (IDs 20403-20432) from candidate_words.json. A mix of everyday vocabulary, cultural terms, and useful expressions for intermediate learners.

- **Na-adjectives (3)**: {長期的|ちょうきてき} (long-term), {五分五分|ごぶごぶ} (fifty-fifty), {耳寄|みみよ}り (welcome news)
- **Expressions (3)**: {気|き}を{悪|わる}くする (to take offense), やる{気|き}{満々|まんまん} (full of motivation), {殻|から}をむく (to peel/shell)
- **Nouns (24)**: ホチキス (stapler), {試作|しさく} (prototype), {近眼|きんがん} (nearsightedness), {流星群|りゅうせいぐん} (meteor shower), {仮想現実|かそうげんじつ} (virtual reality), {見栄|みえ}っ{張|ぱ}り (show-off), ひっきりなしに (continuously), {上半期|かみはんき} (first half of year), {誤変換|ごへんかん} (incorrect kanji conversion), {指数|しすう} (index/exponent), {新聞紙|しんぶんし} (newspaper material), {減産|げんさん} (production cut), {社会復帰|しゃかいふっき} (return to society), {雑食|ざっしょく} (omnivorous), {再発防止|さいはつぼうし} (recurrence prevention), {携帯番号|けいたいばんごう} (mobile number), {現世|げんせ} (this world), {真綿|まわた} (silk floss), {調合|ちょうごう} (compounding), {屋台骨|やたいぼね} (backbone/foundation), {弥生時代|やよいじだい} (Yayoi period), {目立|めだ}ちたがり{屋|や} (attention seeker), {江戸時代|えどじだい} (Edo period), {通告|つうこく} (formal notice)
- Removed 30 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 22 New Entries, Session 534)
Added 22 new dictionary entries (IDs 20381-20402) from candidate_words.json. A diverse mix of practical vocabulary covering emotions, nature, culture, daily life, and abstract concepts.

- **Na-adjectives (3)**: {達者|たっしゃ} (skillful/healthy), {有望|ゆうぼう} (promising), {精力的|せいりょくてき} (energetic)
- **Expressions (2)**: {否応|いやおう}なし (whether willing or not), {火気厳禁|かきげんきん} (no open flames)
- **Nouns (17)**: {傍観者|ぼうかんしゃ} (bystander), {安心感|あんしんかん} (sense of security), わだかまり (lingering resentment), {枯|か}れ{葉|は} (dead leaves), {景勝地|けいしょうち} (scenic spot), {砂嵐|すなあらし} (sandstorm), {折|お}り{畳|たた}み{傘|がさ} (folding umbrella), {純喫茶|じゅんきっさ} (traditional coffee shop), {新年会|しんねんかい} (New Year's party), {丘陵|きゅうりょう} (hill), {心意気|こころいき} (spirit/determination), {歌謡曲|かようきょく} (popular song), {路線|ろせん}バス (local bus), {輪|わ}ゴム (rubber band), {基金|ききん} (fund), {自省|じせい} (self-reflection), {波打|なみう}ち{際|ぎわ} (water's edge)
- Added 1 new kanji to index: 陵
- Removed 22 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 533)
Added 30 new dictionary entries (IDs 20351-20380) from candidate_words.json. Diverse mix including cultural terms, common expressions, and practical vocabulary for intermediate learners.

- **I-adjectives (3)**: {飽|あ}きっぽい (easily bored), {申|���う}し{訳|わけ}ない (sorry/inexcusable), {気前|きまえ}がいい (generous)
- **Verbs (2)**: {乱読|らんどく}する (indiscriminate reading), {断|だん}ずる (to conclude decisively)
- **Interjections (2)**: どれどれ (let me see), ううん (no, informal)
- **Cultural/calendar terms (4)**: {弥生|やよい} (March), {如月|きさらぎ} (February), {神無月|かんなづき} (October), {立夏|りっか} (start of summer)
- **Nouns (19)**: {私|わたし}{共|ども} (we, humble), {未知数|みちすう} (unknown quantity), {浪人生|ろうにんせい} (ronin student), {妊婦|にんぷ} (pregnant woman), {手|て}ぶれ (camera shake), {根雪|ねゆき} (lingering snow), {駄賃|だちん} (small reward), {深緑|ふかみどり} (dark green), {今昔|こんじゃく} (past and present), {凶兆|きょうちょう} (bad omen), {球体|きゅうたい} (sphere), {什器|じゅうき} (fixtures), {進物|しんもつ} (formal gift), {空路|くうろ} (air route), {海路|かいろ} (sea route), {写|うつ}り (photo quality), {試写会|ししゃかい} (preview screening), {鍋蓋|なべぶた} (pot lid), {地肌|じはだ} (bare skin/texture)
- Added 2 new kanji to index: 什, 弥
- Removed 30 candidates that now exist as entries

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 532)
Added 30 new dictionary entries (IDs 20321-20350) from candidate_words.json. Diverse mix of practical vocabulary for intermediate learners.

- **Adjectives (7)**: ありきたり (commonplace), {凡庸|ぼんよう} (mediocre), {法外|ほうがい} (outrageous), {無鉄砲|むてっぽう} (reckless), {静粛|せいしゅく} (silent/solemn), {清廉|せいれん} (incorruptible), {底|そこ}なし (bottomless)
- **Verbs (5)**: {持|も}ち{寄|よ}る (to bring and share), {落胆|らくたん}する (to be discouraged), チンする (to microwave), {禿|は}げる (to go bald), {撫|な}で{回|まわ}す (to stroke all over)
- **Adverbs (2)**: さりげなく (casually), {一晩中|ひとばんじゅう} (all night long)
- **Nouns (16)**: {経験談|けいけんだん} (personal account), {耳鳴|みみな}り (tinnitus), {雨粒|あまつぶ} (raindrop), {過不足|かふそく} (excess or deficiency), {助|す}っ{人|と} (helper), {変態|へんたい} (pervert/metamorphosis), {若|わか}さ (youth), {細身|ほそみ} (slim build), {魔除|まよ}け (charm against evil), {台風一過|たいふういっか} (clear skies after typhoon), {水|みず}はけ (drainage), {船便|ふなびん} (sea mail), {所持品|しょじひん} (belongings), {万歩計|まんぽけい} (pedometer), {出場|しゅつじょう}する (to compete), {演奏|えんそう}する (to perform music)
- Added 1 new kanji to index: 禿
- Removed 30 candidates that now exist as entries

- Removed 30 candidates that now exist as entries


---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
