# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-23
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
| Total entries | ~18,673 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~15,874 (open) |
| Candidate words | ~5,489 |
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

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 484)
Added 35 new dictionary entries (IDs 18829-18863) from candidate_words.json.

- **Interjection (1)**: いらっしゃいませ (welcome)
- **Nouns (12)**: {仕事場|しごとば} (workplace), {煮付|につ}け (simmered dish), {代休|だいきゅう} (compensatory day off), {入社式|にゅうしゃしき} (company entrance ceremony), {食器洗|しょっきあら}い (dishwashing), {閉塞感|へいそくかん} (sense of stagnation), {震|ふる}え (shiver/tremor), {飢餓|きが} (hunger/famine), {個人情報|こじんじょうほう} (personal information), お{知|し}らせ (notice), {証人|しょうにん} (witness), {入門書|にゅうもんしょ} (introductory book)
- **Nouns/Suru verbs (7)**: {紛失|ふんしつ}する (to lose), {悪化|あっか}する (to worsen), {封鎖|ふうさ} (blockade), {増設|ぞうせつ} (expansion), {習得|しゅうとく}する (to master), {自滅|じめつ} (self-destruction), {閉館|へいかん} (closing of facility)
- **Nouns/Suru verbs (2)**: {休館|きゅうかん} (temporary closure), {処方薬|しょほうやく} (prescription medicine)
- **Na-adjectives (2)**: {簡明|かんめい} (concise and clear), ちぐはぐ (mismatched)
- **Godan verbs (2)**: {飲|の}み{交|か}わす (to drink together), {後|あと}ずさる (to back away)
- **Adverb (1)**: {即刻|そっこく} (immediately)
- **Expressions (5)**: {夢中|むちゅう}になる (to become absorbed), {目|め}が{合|あ}う (to make eye contact), {目|め}をそむける (to avert one's eyes), どうしようもない (helpless/hopeless), {失敬|しっけい} (rude/excuse me)
- **Other nouns (3)**: {流|なが}し (kitchen sink/cruising taxi), {星占|ほしうらな}い (horoscope), {郷里|きょうり} (hometown)
- **Multi-sense entries**: {失敬|しっけい} (2), {流|なが}し (2), どうしようもない (2), {閉館|へいかん} (2)

Total entries: ~18,638 → ~18,673 (approximate)
Remaining candidates: ~5,524 → ~5,489 (35 removed as entries)

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 483)
Added 35 new dictionary entries (IDs 18794-18828) from candidate_words.json.

- **Nouns (16)**: {横顔|よこがお} (profile/side view), {麻薬|まやく} (narcotic), {特価|とっか} (special price), {不作|ふさく} (bad harvest), {車種|しゃしゅ} (car model), {四隅|よすみ} (four corners), {初霜|はつしも} (first frost), {品数|しなかず} (number of items), {機内|きない} (inside aircraft), {中期|ちゅうき} (mid-term), {神殿|しんでん} (temple), {身柄|みがら} (custody), {強権|きょうけん} (authoritative power), {縦縞|たてじま} (vertical stripes), {横縞|よこじま} (horizontal stripes)
- **Nouns/Suru verbs (8)**: {伝播|でんぱ} (propagation), {占拠|せんきょ} (occupation/seizure), {免職|めんしょく} (dismissal from post), {謹慎|きんしん} (suspension), {記帳|きちょう} (bookkeeping), {引率|いんそつ} (leading a group), {敬愛|けいあい} (respect and affection), {調剤|ちょうざい} (dispensing medicine), {自生|じせい} (growing wild), {完勝|かんしょう} (complete victory)
- **Nouns/Na-adjective/Suru verb (1)**: {無心|むしん} (innocence/absorption/begging)
- **Na-adjective (2)**: {辛口|からくち} (dry/spicy/harsh), {立体|りったい} (three-dimensional), {貧相|ひんそう} (poor-looking)
- **Other (2)**: {空咳|からせき} (dry cough), {遅番|おそばん} (late shift), {渋面|じゅうめん} (grimace), {体面|たいめん} (honor/prestige), あざ (bruise/birthmark)
- **Multi-sense entries**: {辛口|からくち} (3), {無心|むしん} (3), {空咳|からせき} (2), {横顔|よこがお} (2), {麻薬|まやく} (2), {立体|りったい} (2), {謹慎|きんしん} (2), {記帳|きちょう} (2), あざ (2)
- **Paired entries**: {縦縞|たてじま}/{横縞|よこじま}, {完勝|かんしょう}/{完敗|かんぱい}

Total entries: ~18,603 → ~18,638 (approximate)
Remaining candidates: ~5,559 → ~5,524 (35 removed as entries)

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 482)
Added 35 new dictionary entries (IDs 18759-18793) from candidate_words.json.

- **Nouns (18)**: {区間|くかん} (section/segment), {検知|けんち} (detection), {力量|りきりょう} (ability/competence), {非常食|ひじょうしょく} (emergency food), {罰金|ばっきん} (fine/penalty), {犠牲者|ぎせいしゃ} (victim/casualty), {純度|じゅんど} (purity), {戦艦|せんかん} (battleship), {動力|どうりょく} (power/motive force), {数人|すうにん} (several people), {焦燥感|しょうそうかん} (feeling of impatience), {報奨金|ほうしょうきん} (reward money), {暑気|しょき} (summer heat), {操作性|そうさせい} (operability/usability), {地酒|じざけ} (local sake), {祝宴|しゅくえん} (celebration banquet), {交代制|こうたいせい} (shift system), {伸長|しんちょう} (growth/extension)
- **Nouns/Suru verbs (6)**: {墜落|ついらく} (crash/fall), {軽視|けいし}する (to make light of), {登校|とうこう}する (to go to school), {論述|ろんじゅつ} (exposition), {追従|ついじゅう} (following blindly), {共催|きょうさい} (co-hosting)
- **Nouns/Na-adjectives (2)**: {仮装|かそう} (costume/disguise), {見当違|けんとうちが}い (off the mark)
- **Pre-noun adjectival (1)**: {特大|とくだい} (extra-large)
- **Adjective-na (2)**: {邪悪|じゃあく} (evil/wicked), {鷹揚|おうよう} (generous/magnanimous)
- **Adjective-i (1)**: {執念深|しゅうねんぶか}い (persistent/vindictive)
- **Adverb (1)**: {粉々|こなごな} (in pieces/smashed)
- **Verb (1)**: {肥|こ}える (to grow fat/become refined)
- **Expression (1)**: {犬猿|けんえん}の{仲|なか} (like cats and dogs)
- **Multi-sense entries**: {肥|こ}える (3 senses), {仮装|かそう} (2 senses)
- New kanji added: 墜 (ID 02585)

Total entries: ~18,568 → ~18,603 (approximate)
Remaining candidates: ~5,592 → ~5,559 (33 removed as entries)

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 481)
Added 35 new dictionary entries (IDs 18724-18758) from candidate_words.json.

- **Godan verbs (7)**: {搾|しぼ}る (squeeze/extract), {見破|みやぶ}る (see through), {貫|つらぬ}く (pierce/carry through), {物語|ものがた}る (narrate/indicate), {謹|つつし}む (humbly do), {締|し}まる (tighten), {見通|みとお}す (see through/foresee)
- **Ichidan verbs (3)**: {縮|ちぢ}まる (shrink), {朽|く}ちる (decay), {隔|へだ}てる (separate), {低|ひく}める (lower)
- **Nouns (11)**: {見習|みなら}い (apprentice), {占|うらな}い (fortune-telling), お{使|つか}い (errand), {払|はら}い (payment), {不名誉|ふめいよ} (disgrace), {収入源|しゅうにゅうげん} (income source), {腹持|はらも}ち (filling food), {誤作動|ごさどう} (malfunction), {局所|きょくしょ} (local area), {球根|きゅうこん} (bulb), {成虫|せいちゅう} (adult insect), {決定打|けっていだ} (decisive blow), {分析家|ぶんせきか} (analyst), {腐|くさ}れ{縁|えん} (inseparable bond), {高学歴|こうがくれき} (highly educated), {健康体|けんこうたい} (healthy body), {共食|ともぐ}い (cannibalism/infighting)
- **Adjectives (2)**: {表面的|ひょうめんてき} (superficial), {堅|かた}い (firm/strict)
- **Adverbs (3)**: {著|いちじる}しく (remarkably), すごく (very), {多|おお}く (many/mostly)
- **Expressions (2)**: {飴|あめ}と{鞭|むち} (carrot and stick), {瞬時|しゅんじ}に (in an instant)

Notable features:
- Multi-sense entries: {搾|しぼ}る (2), {貫|つらぬ}く (2), {隔|へだ}てる (2), {物語|ものがた}る (2), {締|し}まる (2), {見通|みとお}す (2), {払|はら}い (2), {共食|ともぐ}い (2), {多|おお}く (2)
- Homophone distinctions: {搾|しぼ}る vs {絞|しぼ}る, {堅|かた}い vs {固|かた}い vs {硬|かた}い, {謹|つつし}む vs {慎|つつし}む, {締|し}まる vs {閉|し}まる
- Cultural/Japanese life: {占|うらな}い, お{使|つか}い, {飴|あめ}と{鞭|むち}, {腐|くさ}れ{縁|えん}

Total entries: ~18,533 → ~18,568 (approximate)
Remaining candidates: ~5,627 → ~5,592 (35 removed as entries)

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 480)
Added 35 new dictionary entries (IDs 18689-18723) from candidate_words.json.

- **Verbs (11)**: {拭|ふ}き{取|と}る (wipe off), {追|お}い{返|かえ}す (send away), {焦|じ}らす (tease), {慣|な}れ{親|した}しむ (become familiar), {解|ほど}ける (come untied), やり{過|す}ごす (let pass), {消|き}え{失|う}せる (vanish), {充|あ}てる (allocate), {履|は}き{違|ちが}える (misinterpret), {追|お}い{落|お}とす (oust), {立|た}ちすくむ (stand frozen)
- **Suru verbs (3)**: {推奨|すいしょう}する (recommend), {不自由|ふじゆう}する (lack), {東奔西走|とうほんせいそう} (rush about)
- **Ichidan verb with 2 senses (3)**: {空|あ}ける (empty/vacate), {解|ほど}ける (untie/relax), やり{過|す}ごす (let pass/overdo)
- **Expressions (8)**: {契約|けいやく}を{結|むす}ぶ (sign contract), {高|たか}を{括|くく}る (underestimate), {職|しょく}に{就|つ}く (get a job), {足|あし}がすくむ (frozen with fear), {時間|じかん}を{割|さ}く (spare time), {共|とも}にする (share), {正体|しょうたい}を{現|あらわ}す (reveal true colors), {窮地|きゅうち}に{陥|おちい}る (fall into predicament)
- **Nouns (6)**: {小分|こわ}け (small portions), {安産|あんざん} (easy delivery), {丸焦|まるこ}げ (burnt to a crisp), {発信力|はっしんりょく} (communication power), {差|さ}し{水|みず} (adding water), {安置|あんち} (enshrinement)
- **Adjective-na (1)**: {多角的|たかくてき} (multilateral)
- **Adverbs (2)**: {毎秒|まいびょう} (every second), {常日頃|つねひごろ} (always)
- **Other (2)**: {僅少|きんしょう} (very small amount), {数多|かずおお}くの (numerous)
- **身を寄せる (1)**: {身|み}を{寄|よ}せる (take shelter with)

Notable features:
- Multi-sense entries: {空|あ}ける (2), {解|ほど}ける (2), やり{過|す}ごす (2), {履|は}き{違|ちが}える (2), {安置|あんち} (2)
- Idioms/Expressions: {高|たか}を{括|くく}る, {正体|しょうたい}を{現|あらわ}す, {東奔西走|とうほんせいそう}, {窮地|きゅうち}に{陥|おちい}る
- Daily life/Cooking: {小分|こわ}け, {差|さ}し{水|みず}, {丸焦|まるこ}げ
- Body/Emotion pairs: {足|あし}がすくむ / {立|た}ちすくむ
- Removed 4 stale candidates (個, 枚, 冊 as counter duplicates; 捲り上げる as kanji variant of existing めくり上げる)

Total entries: ~18,498 → ~18,533 (approximate)
Remaining candidates: ~5,666 → ~5,627 (35 removed as entries + 4 stale removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
