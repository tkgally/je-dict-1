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
| Total entries | ~18,568 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~15,769 (open) |
| Candidate words | ~5,592 |
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

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 479)
Added 35 new dictionary entries (IDs 18654-18688) from candidate_words.json.

- **Nouns (19)**: お{酢|す} (vinegar), インコ (parakeet), {査証|さしょう} (visa), {中高生|ちゅうこうせい} (jr/sr high school students), {体脂肪|たいしぼう} (body fat), {利回|りまわ}り (yield), {聖堂|せいどう} (cathedral), {経験者|けいけんしゃ} (experienced person), {賭|か}け{事|ごと} (gambling), {埴輪|はにわ} (haniwa clay figure), {夏野菜|なつやさい} (summer vegetables), {煮浸|にびた}し (simmered dish), {混血|こんけつ} (mixed heritage), {白金|はっきん} (platinum), {水深|すいしん} (water depth), {坑道|こうどう} (mine tunnel), {胴元|どうもと} (bookmaker), {日勤|にっきん} (day shift), {拡大鏡|かくだいきょう} (magnifying glass)
- **Nouns/Suru verbs (4)**: {希釈|きしゃく} (dilution), {差別化|さべつか} (differentiation), {続伸|ぞくしん} (continued rise), {共和|きょうわ} (republic)
- **Na-adjectives/Nouns (4)**: {安楽|あんらく} (comfortable), {利発|りはつ} (clever), {姑息|こそく} (stopgap/cowardly), {耽美|たんび} (aestheticism)
- **Adjective-no/Noun (1)**: {多機能|たきのう} (multi-function)
- **Nouns (business pair) (2)**: {上期|かみき} (first half of fiscal year), {下期|しもき} (second half of fiscal year)
- **Noun (2 senses) (3)**: {外装|がいそう} (exterior/packaging), {原画|げんが} (original art/key animation), {煙管|きせる} (kiseru pipe/fare evasion)
- **Noun (2 senses) (2)**: {舎弟|しゃてい} (younger brother/underling), {姑息|こそく} (stopgap/cowardly)

Notable features:
- Multi-sense entries: {外装|がいそう} (2), {原画|げんが} (2), {煙管|きせる} (2), {姑息|こそく} (2), {舎弟|しゃてい} (2)
- Business/Finance: {利回|りまわ}り, {上期|かみき}, {下期|しもき}, {差別化|さべつか}, {続伸|ぞくしん}
- Food/Cooking: お{酢|す}, {夏野菜|なつやさい}, {煮浸|にびた}し
- Culture/History: {埴輪|はにわ}, {煙管|きせる}, {睦月|むつき}, {耽美|たんび}
- New kanji added: 埴 (ID 02583), 耽 (ID 02584)

Total entries: ~18,463 → ~18,498 (approximate)
Remaining candidates: ~5,701 → ~5,666 (35 removed as entries)

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 478)
Added 35 new dictionary entries (IDs 18619-18653) from candidate_words.json.

- **Nouns (22)**: {洋楽|ようがく} (Western music), {新製品|しんせいひん} (new product), {付属品|ふぞくひん} (accessories), {別売|べつう}り (sold separately), {買|か}い{値|ね} (purchase price), {理事会|りじかい} (board of directors), {生命|せいめい}{保険|ほけん} (life insurance), {産業|さんぎょう}{革命|かくめい} (Industrial Revolution), {百貨店|ひゃっかてん} (department store), {裏門|うらもん} (back gate), {小心者|しょうしんもの} (coward), {正真正銘|しょうしんしょうめい} (genuine), お{化|ば}け{屋敷|やしき} (haunted house), {受験生|じゅけんせい} (exam student), くちばし (beak), {人事|じんじ}{異動|いどう} (personnel reshuffle), {撮|と}り{直|なお}し (retake), {予断|よだん} (prejudgment), {患部|かんぶ} (affected area), {微塵|みじん} (tiny particle / not at all), {序列|じょれつ} (hierarchy), {再利用|さいりよう} (reuse)
- **Nouns/Suru verbs (7)**: {激変|げきへん} (drastic change), {分散|ぶんさん} (dispersion), {気疲|きづか}れ (mental fatigue), {介助|かいじょ} (caregiving), {切|き}り{盛|も}り (managing), {熱望|ねつぼう} (ardent desire), {除草|じょそう} (weeding)
- **Nouns/Na-adjectives (4)**: {無知|むち} (ignorance), {軽|かる}はずみ (rashness), {気弱|きよわ} (timid), {半透明|はんとうめい} (translucent)
- **Na-adjective (1)**: {体系的|たいけいてき} (systematic)
- **Noun (1)**: {単身|たんしん}{赴任|ふにん} (living away from family for work)

Notable features:
- Multi-sense entries: {分散|ぶんさん} (2 senses), {微塵|みじん} (2 senses)
- Cultural: {単身|たんしん}{赴任|ふにん}, {受験生|じゅけんせい}, {百貨店|ひゃっかてん}, お{化|ば}け{屋敷|やしき}
- Business/Finance: {生命|せいめい}{保険|ほけん}, {買|か}い{値|ね}, {理事会|りじかい}, {人事|じんじ}{異動|いどう}, {序列|じょれつ}
- Medical/Health: {患部|かんぶ}, {介助|かいじょ}
- Homophone cross-references added for: {無知|むち}/{無恥|むち}, {予断|よだん}/{余談|よだん}, {除草|じょそう}/{助走|じょそう}/{女装|じょそう}, {患部|かんぶ}/{幹部|かんぶ}

Total entries: ~18,428 → ~18,463 (approximate)
Remaining candidates: ~5,736 → ~5,701 (35 removed as entries)

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 477)
Added 35 new dictionary entries (IDs 18584-18618) from candidate_words.json.

- **Expressions (13)**: に{違|ちが}いない (must be), {面目|めんぼく}ない (ashamed), {運|うん}が{良|い}い (lucky), {場|ば}を{盛|も}り{上|あ}げる (liven up), {喉|のど}を{鳴|な}らす (to purr), {本音|ほんね}を{吐|は}く (speak one's mind), {腰|こし}がある (chewy/firm), {変化|へんか}に{富|と}む (varied), {付|つ}き{合|あ}いがいい (sociable), {熱|ねつ}を{冷|さ}ます (cool down), {危険|きけん}を{孕|はら}む (fraught with danger), ページを{繰|く}る (leaf through pages), {発給|はっきゅう}する (to issue)
- **Verbs (9)**: {書|か}き{損|そん}じる (writing mistake), {曲|ま}がりくねる (twist and turn), {叩|たた}きのめす (thrash), {立|た}ち{回|まわ}る (maneuver), {走|はし}り{去|さ}る (run away), {動|うご}き{出|だ}す (start moving), {滑|すべ}り{出|だ}す (get underway), めくり{上|あ}げる (roll up), そぎ{落|お}とす (strip away), {教|おし}え{導|みちび}く (mentor)
- **Adjectives (5)**: {格好|かっこう}いい (cool), {小汚|こぎたな}い (scruffy), くすぐったい (ticklish), {疑|うたが}い{深|ぶか}い (distrustful), {理屈|りくつ}っぽい (argumentative)
- **Nouns (3)**: {斜|なな}め{向|む}かい (diagonally opposite), {目利|めき}き (connoisseur), {身|み}の{上|うえ} (one's circumstances)
- **Pronouns (2)**: {誰|だれ}も (nobody/everyone), どいつ (which one - rude)
- **Adverb (1)**: {静|しず}かに (quietly)
- **Noun/Suru verb (1)**: {更生|こうせい}する (rehabilitate)

Notable features:
- Multi-sense entries: くすぐったい (2), {立|た}ち{回|まわ}る (2), {滑|すべ}り{出|だ}す (2), {喉|のど}を{鳴|な}らす (2), {静|しず}かに (2), {誰|だれ}も (2), {熱|ねつ}を{冷|さ}ます (2)
- Grammar/Patterns: に{違|ちが}いない, {誰|だれ}も, {静|しず}かに
- Social/Cultural: {付|つ}き{合|あ}いがいい, {場|ば}を{盛|も}り{上|あ}げる, {本音|ほんね}を{吐|は}く, {腰|こし}がある
- Compound verbs: {曲|ま}がりくねる, {叩|たた}きのめす, {走|はし}り{去|さ}る, {動|うご}き{出|だ}す, {滑|すべ}り{出|だ}す
- Removed 4 stale candidates (duplicates: {挑戦|ちょうせん}, ～だらけ, ～だけでなく, ～がち)

Total entries: ~18,393 → ~18,428 (approximate)
Remaining candidates: ~5,773 → ~5,736 (33 removed as entries + 4 stale removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
