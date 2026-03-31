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

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 553)
Added 30 new dictionary entries (IDs 20939-20968) from candidate_words.json. A diverse mix covering social behavior, transportation, culture, nature, food, politics, history, law, arts, and daily life.

- **Nouns (19)**: {普通車|ふつうしゃ} (standard car/regular train car), {若年層|じゃくねんそう} (younger generation), {毒蛇|どくへび} (venomous snake), ポニーテール (ponytail), {祝儀袋|しゅうぎぶくろ} (gift money envelope), {豆板醤|とうばんじゃん} (chili bean paste), {雑穀|ざっこく} (mixed grains), {国会議員|こっかいぎいん} (Diet member), {左官|さかん} (plasterer), {控|ひか}え{選手|せんしゅ} (substitute player), {二輪車|にりんしゃ} (two-wheeled vehicle), {市外局番|しがいきょくばん} (area code), {正誤表|せいごひょう} (errata), {練習曲|れんしゅうきょく} (etude), {写本|しゃほん} (manuscript), {相談役|そうだんやく} (advisor), {遠隔地|えんかくち} (remote area), {絶景|ぜっけい}スポット (scenic viewpoint), {放物線|ほうぶつせん} (parabola)
- **Suru verbs (3)**: {依怙贔屓|えこひいき} (favoritism), {天下統一|てんかとういつ} (national unification), {成敗|せいばい} (punishment)
- **Na-adjectives (3)**: {草食|そうしょく} (herbivorous/passive), {合憲|ごうけん} (constitutional), {苦労性|くろうしょう} (worrywart)
- **Expressions (2)**: {眼鏡|めがね}をかける (to wear glasses), {何事|なにごと}も (everything)
- **Other (3)**: こら (hey!/stop that!), {自然遺産|しぜんいさん} (natural heritage), {宵|よい}の{明星|みょうじょう} (evening star)
- Added 1 new kanji to index: 怙


---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
