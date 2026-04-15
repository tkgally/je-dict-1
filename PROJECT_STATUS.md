# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-14
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

### 2026-04-15 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 23833-23842) from candidate_words.json. A mixed set covering everyday nouns, technical vocabulary, a na-adjective loanword, and a multi-sense general noun.

- **Nouns (8)**: アスピリン (aspirin), ウェブページ (web page), イタチ (weasel), {花輪|はなわ} (floral wreath; garland), {電磁石|でんじしゃく} (electromagnet), {投稿者|とうこうしゃ} (poster; contributor), {広報活動|こうほうかつどう} (public relations activities), {通知書|つうちしょ} (official notice/notification letter)
- **Na-adjective (1)**: チャーミング (charming; endearing — loanword)
- **Multi-sense noun (1)**: {小口|こぐち} (small-lot; cut end of a log; edge of a book — three senses, 9 examples)
- All entries include progressive-length examples, structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, and full furigana coverage

### 2026-04-15 (Vocabulary Expansion - 8 New Entries)
Added 8 new dictionary entries (IDs 23825-23832) from candidate_words.json. A mixed set covering descriptive modifiers, occupations, biology, transport, tea-ceremony vocabulary, and common verb/phrase expressions.

- **No-adjective (1)**: {等身大|とうしんだい}の (life-size; true-to-life — with figurative sense)
- **Nouns (4)**: {副操縦士|ふくそうじゅうし} (co-pilot; first officer), {軟体動物|なんたいどうぶつ} (mollusk), {豪華客船|ごうかきゃくせん} (luxury cruise ship), {茶筅|ちゃせん} (tea whisk), {茶杓|ちゃしゃく} (tea scoop)
- **Expressions (2)**: {偽|いつわ}りのない (truthful; genuine — set prenominal phrase), {口|くち}を{開|あ}ける (to open one's mouth / to unseal a container — two senses)
- All entries include progressive-length examples, structured notes with USAGE / COLLOCATIONS / SIMILAR WORDS sections, and full furigana coverage
- New kanji 筅 assigned ID 02684_sen_none_whisk for the kanji index

### 2026-04-15 (Vocabulary Expansion - 14 New Entries)
Added 14 new dictionary entries (IDs 23811-23824) from candidate_words.json. A themed set focused on 〜的 na-adjectives (abstract/academic register) plus several nouns.

- **Na-adjectives (9)**: {概念的|がいねんてき} (conceptual; abstract), {派生的|はせいてき} (derivative; derived), {局所的|きょくしょてき} (localized), {先駆的|せんくてき} (pioneering; trailblazing), {非論理的|ひろんりてき} (illogical), {非合理的|ひごうりてき} (irrational), {情緒的|じょうちょてき} (emotional; sentimental), {友好的|ゆうこうてき} (friendly; amicable), {発作的|ほっさてき} (impulsive; fit-like)
- **Nouns (4)**: {現象学|げんしょうがく} (phenomenology), {防護柵|ぼうごさく} (protective fence; guardrail), {来客数|らいきゃくすう} (number of visitors/customers), {写真室|しゃしんしつ} (photo studio — room)
- **Noun+suru verb (1)**: {減水|げんすい} (drop in water level; reservoir-level fall)
- All entries include progressive-length examples, structured notes with USAGE / COLLOCATIONS / SIMILAR WORDS sections (plus RELATED TERMS or CULTURAL CONTEXT where relevant), and full furigana coverage

### 2026-04-14 (Vocabulary Expansion - 13 New Entries)
Added 13 new dictionary entries (IDs 23798-23810) from candidate_words.json. A mix of formal/technical, sexuality-related, legal, and traditional vocabulary.

- **Na-adjectives (3)**: {性的|せいてき} (sexual; erotic), {狭量|きょうりょう} (narrow-minded; petty), {有毒|ゆうどく} (poisonous; toxic — also no-adj)
- **Noun/suru verbs (3)**: {野宿|のじゅく} (sleeping outdoors), {査察|ささつ} (official on-site inspection), {昏睡|こんすい} (coma / comatose state), {作図|さくず} (geometric construction; drafting)
- **Nouns (5)**: {先人|せんじん} (forerunner; predecessor), {論客|ろんきゃく} (pundit; skilled debater), {猥褻|わいせつ} (obscene; indecent — na-adj), {性欲|せいよく} (sexual desire; libido), {多用途|たようと} (multi-purpose), {棒術|ぼうじゅつ} (traditional staff martial art)
- All entries include progressive-length examples, structured notes with USAGE / COLLOCATIONS / SIMILAR WORDS (plus CULTURAL CONTEXT where relevant) sections, and full furigana coverage
- Added new kanji 褻 (ID 02683) to the kanji index

### 2026-04-14 (Vocabulary Expansion - 25 New Entries)
Added 25 new dictionary entries (IDs 23773-23797) from candidate_words.json. A mix of everyday nouns, technical terms, and cultural/scientific vocabulary.

- **Media/Arts**: {映画化|えいがか} (film adaptation, noun+suru-verb), {紅色|べにいろ} (crimson; safflower red), {弓術|きゅうじゅつ} (traditional archery as a martial art)
- **Geography/Location**: {中心部|ちゅうしんぶ} (central part; downtown), {白昼|はくちゅう} (broad daylight; daytime)
- **Work/Social**: {受|う}け{持|も}ち (one's charge or assigned area), {会話力|かいわりょく} (conversational ability), {社交性|しゃこうせい} (sociability), {熟練者|じゅくれんしゃ} (experienced worker; skilled craftsperson), {総務部|そうむぶ} (general affairs department), {送付先|そうふさき} (mailing/shipping address)
- **Nature/Biology**: {動植物|どうしょくぶつ} (flora and fauna), {獣|けもの} (wild beast), {亜種|あしゅ} (subspecies), {同種|どうしゅ} (same kind/species), {脂肪酸|しぼうさん} (fatty acid)
- **Daily life**: {食糧不足|しょくりょうぶそく} (food shortage), {風|かぜ}よけ (windbreak), {食堂車|しょくどうしゃ} (dining car), トイレットペーパー (toilet paper), {公衆|こうしゅう}トイレ (public toilet), {肩掛|かたか}け (shawl/shoulder wrap), {核爆弾|かくばくだん} (nuclear bomb)
- **Abstract**: {先駆|さきが}け (forerunner; pioneer; harbinger), {構成要素|こうせいようそ} (component; constituent element)
- All entries include progressive-length examples, structured notes with USAGE / COLLOCATIONS / SIMILAR WORDS (and in some cases CULTURAL NOTE) sections, and full furigana coverage
- Added new kanji 亜 (ID 02682) to the kanji index

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








