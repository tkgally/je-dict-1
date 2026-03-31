# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-31
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

### 2026-03-31 (Vocabulary Expansion - 30 New Entries, Session 556)
Added 30 new dictionary entries (IDs 21048-21077) from candidate_words.json. A practical mix covering emotions, food, family, places, daily life, and formal/business vocabulary.

- **Nouns (22)**: {感慨|かんがい} (deep emotion), {論点|ろんてん} (point of argument), {金賞|きんしょう} (gold prize), {里親|さとおや} (foster parent), {心残|こころのこ}り (lingering regret), {裏路地|うらろじ} (back alley), {酒類|しゅるい} (alcoholic beverages), {急務|きゅうむ} (urgent task), {粉|こな}ミルク (powdered milk), {練乳|れんにゅう} (condensed milk), {残雪|ざんせつ} (lingering snow), {人生観|じんせいかん} (view of life), {恥知|はじし}らず (shameless person), {固定費|こていひ} (fixed costs), {病室|びょうしつ} (hospital room), {凱旋|がいせん} (triumphal return), {養女|ようじょ} (adopted daughter), {実子|じっし} (biological child), {出入|でい}り{口|ぐち} (entrance/exit), {食生活|しょくせいかつ} (eating habits), {完全主義|かんぜんしゅぎ} (perfectionism), {人当|ひとあ}たり (manner with people)
- **Suru verbs (5)**: {失速|しっそく} (to stall/lose momentum), {散布|さんぷ} (to spray), {寄港|きこう} (to call at port), {子守|こも}り (babysitting), {駐車違反|ちゅうしゃいはん} (parking violation)
- **Godan verb (1)**: {聞|き}き{落|お}とす (to miss hearing)
- **I-adjective (1)**: {味気|あじけ}ない (dull/dreary)
- **Adverb (1)**: {後程|のちほど} (later on)
- Added 1 new kanji to index: 凱
- Removed 30 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 30 New Entries, Session 555)
Added 30 new dictionary entries (IDs 21018-21047) from candidate_words.json. A mix of adjectives, verbs, nouns, and expressions covering evaluation, cognition, action, culture, and formal language.

- **Na-adjectives (6)**: {私的|してき}な (private/personal), {公的|こうてき}な (official/public), {公正|こうせい}な (fair/impartial), {主観的|しゅかんてき}な (subjective), {理性的|りせいてき}な (rational), {筋違|すじちが}い (misplaced/misdirected)
- **I-adjectives (4)**: {比類|ひるい}ない (peerless), {格式高|かくしきたか}い (prestigious), {田舎臭|いなかくさ}い (countrified), {疑|うたが}いない (undoubted)
- **Godan verbs (7)**: {折|お}り{返|かえ}す (to fold back/call back), {刈|か}り{取|と}る (to harvest), {考|かんが}え{出|だ}す (to think up), {写|うつ}り{込|こ}む (to appear in photo), かき{乱|みだ}す (to stir up), {抜|ぬ}き{取|と}る (to extract), {刈|か}り{込|こ}む (to trim)
- **Suru verbs (7)**: {決定|けってい}する (to decide), {実在|じつざい}する (to actually exist), {発射|はっしゃ}する (to fire/launch), {連発|れんぱつ}する (to repeat in succession), {続発|ぞくはつ}する (to occur in succession), {透過|とうか}する (to pass through), {発進|はっしん}する (to depart), {帰属|きぞく}する (to belong to)
- **Nouns (4)**: {主|おも}な (main/major), {第一言語|だいいちげんご} (first language), サンデー (sundae), {腐女子|ふじょし} (fujoshi), {抜擢人事|ばってきじんじ} (merit-based promotion)
- Removed 3 stale candidates (duplicates of existing entries)
- Removed 29 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 19 New Entries)
Added 19 new dictionary entries (IDs 20999-21017) from candidate_words.json. A diverse mix covering language, medicine, law, science, culture, daily life, and modern society.

- **Nouns (13)**: {言|い}い{換|か}え (paraphrase), {改名|かいめい} (name change), {外科医|げかい} (surgeon), {病棟|びょうとう} (hospital ward), {消音|しょうおん} (mute/silencing), {処罰|しょばつ} (punishment), {海水浴場|かいすいよくじょう} (swimming beach), {退部|たいぶ} (leaving a club), {病状|びょうじょう} (patient's condition), {抵抗力|ていこうりょく} (resistance/immunity), {化粧台|けしょうだい} (dressing table), {即金|そっきん} (spot cash), {電流|でんりゅう} (electric current)
- **Na-adjectives (2)**: {計画的|けいかくてき} (planned/deliberate), {突発的|とっぱつてき} (sudden/unexpected)
- **I-adjective (1)**: ろくでもない (good-for-nothing/worthless)
- **Adverb (1)**: そこかしこ (here and there)
- **Cultural (2)**: {恋活|こいかつ} (dating activities), しめ{飾|かざ}り (New Year rope decoration)

### 2026-03-31 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 20969-20998) from candidate_words.json. A diverse mix covering people, relationships, culture, food, health, martial arts, society, finance, and common verbs.

- **Nouns (16)**: クラスメート (classmate), {別|わか}れ{話|ばなし} (breakup talk), {熱|あつ}さ (heat/hotness), あごひげ (chin beard), {金言|きんげん} (wise saying), {出席者|しゅっせきしゃ} (attendee), {美術家|びじゅつか} (artist), {必読書|ひつどくしょ} (must-read book), {連載小説|れんさいしょうせつ} (serialized novel), {入居者|にゅうきょしゃ} (resident), {治療院|ちりょういん} (clinic), {接骨院|せっこついん} (bone-setting clinic), {継父|ままちち} (stepfather), {正月飾|しょうがつかざ}り (New Year decorations), {澄|す}まし{汁|じる} (clear soup), {免震|めんしん} (seismic isolation), {人権侵害|じんけんしんがい} (human rights violation), {逃走者|とうそうしゃ} (fugitive), {非正規雇用|ひせいきこよう} (non-regular employment), {地方創生|ちほうそうせい} (regional revitalization), {柔術|じゅうじゅつ} (jujutsu)
- **Suru verbs (8)**: イメージする (to visualize), {停止|ていし}する (to stop/halt), {潜水|せんすい}する (to dive underwater), {潜入|せんにゅう}する (to infiltrate), {憎悪|ぞうお}する (to hate/detest), {着金|ちゃっきん}する (to receive payment), {変化|へんか}する (to change), {計画|けいかく}する (to plan)
- **Expression (1)**: {心|こころ}が{広|ひろ}い (broad-minded)
- Removed 30 candidates that now exist as entries

### 2026-03-31 (Cross-Reference System Overhaul)
Created a new systematic cross-reference review system and updated related documentation.

- **New prompt**: `prompts/add_cross-references.md` — systematically reviews entries and adds/verifies both `prominent_see_also` and `cross_references` links
- **New tracking file**: `prompts/add-cross-references-tracking.txt` — pre-populated with all 2,783 basic and core tier entries
- **Updated skill**: `.claude/skills/cross-reference-entry/SKILL.md` — expanded `prominent_see_also` guidance to cover transitive/intransitive pairs, N/Nする pairs, informal/formal pairs, and other closely related word groups; deprecated `pair` type in `cross_references` (transitive/intransitive pairs now use `prominent_see_also`)
- **Deleted**: `prompts/add_prominent_crossrefs.md` (superseded by new prompt)
- **Updated**: CLAUDE.md, README.md, metaprompt_list.md references


---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
