# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-09
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
| Total entries | ~10,716 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~7,917 (open) |
| Candidate words | ~163 |
| Cross-references | ~3,332 |
| Example sentences | ~41,450 |
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

### 2026-02-09 (Vocabulary Expansion - 30 New Entries, Session 231)
Added 30 new dictionary entries (IDs 10695-10724) from candidate_words.json:

- **Nouns (20)**: アウトドア (outdoor), アトリエ (studio), アボカド (avocado), アラーム (alarm), アリーナ (arena), アルファベット (alphabet), アワビ (abalone), アーモンド (almond), イクラ (salmon roe), イチオシ (top pick), イラスト (illustration), イワシ (sardine), インパクト (impact), {鱗|うろこ} (scale), エキス (extract), エッセイ (essay)
- **Nouns + suru verb (5)**: アクセス (access), アナウンス (announcement), アピール (appeal), アプローチ (approach), アーカイブ (archive)
- **Nouns + na-adjective (2)**: アホ (fool/stupid), インスタント (instant)
- **Nouns (2 senses) (3)**: アクセント (accent/highlight), アプローチ (method/outreach), アクセス (transport/computing)
- **Other nouns (3)**: アドバイス (advice), アーティスト (artist), アート (art), アラサー (around 30), アラフォー (around 40), インバウンド (inbound tourism)

Notable features:
- Primarily katakana loanwords filling gaps in the dictionary's coverage of common borrowed vocabulary
- Food vocabulary: アボカド, アワビ, イクラ, イワシ, アーモンド, エキス, インスタント
- Cultural/modern Japanese: アラサー/アラフォー (age-related wasei-eigo), インバウンド (tourism buzzword), イチオシ (fan/recommendation culture)
- Arts/media: アトリエ, アート, アーティスト, イラスト, エッセイ, アーカイブ
- One native Japanese word with new kanji: {鱗|うろこ} (scale)
- Cross-references: アラサー↔アラフォー
- New kanji: 2,278 → 2,279 ({鱗|りん})

Total entries: 10,686 → 10,716
Remaining candidates: 193 → 163

### 2026-02-09 (Vocabulary Expansion - 30 New Entries, Session 230)
Added 30 new dictionary entries (IDs 10665-10694) from candidate_words.json:

- **Nouns (25)**: しじみ (freshwater clam), ちまき (rice dumpling), ちょんまげ (topknot), ふるさと{納税|のうぜい} (hometown tax), {書|か}き{入|い}れ{時|どき} (busy season), {合気道|あいきどう} (aikido), {居合道|いあいどう} (iaido), {雹|ひょう} (hail), {空手道|からてどう} (karate), {偏差|へんさ} (deviation), {幻覚|げんかく} (hallucination), {威厳|いげん} (dignity), {利便性|りべんせい} (convenience), {素振|そぶ}り (behavior/pretense), {嫌気|いやけ} (disgust/aversion), {顔合|かおあ}わせ (meeting), {水際|みずぎわ} (water's edge/border control), {口添|くちぞ}え (putting in a good word), アイデンティティ (identity), {三男|さんなん} (third son), {三女|さんじょ} (third daughter), くノ{一|いち} (female ninja), {義理|ぎり}の{親|おや} (parent-in-law), ネット{回線|かいせん} (internet connection), てにをは (particles/fine points)
- **Nouns (suru verb) (1)**: {一任|いちにん} (entrusting entirely)
- **Nouns (2 senses) (3)**: ちゃんぽん (chanpon/mixing), {触媒|しょくばい} (catalyst), {水際|みずぎわ} (shore/border control)
- **Verb (1)**: かまける (to be preoccupied with)
- **Adjective (1)**: ねむたい (sleepy)

Notable features:
- Multi-sense entries: ちゃんぽん (noodle dish/mixing), てにをは (particles/wording), {触媒|しょくばい} (chemical/figurative), {水際|みずぎわ} (shore/border), {素振|そぶ}り (behavior/sign), {義理|ぎり}の{親|おや} (in-law/step-parent)
- Martial arts cluster: {合気道|あいきどう}, {居合道|いあいどう}, {空手道|からてどう} (with cross-references)
- Cultural vocabulary: ちまき ({端午|たんご}の{節句|せっく}), ちょんまげ (sumo/samurai), くノ{一|いち} (ninja), {顔合|かおあ}わせ (wedding custom)
- Modern/practical: ふるさと{納税|のうぜい}, ネット{回線|かいせん}, アイデンティティ, {利便性|りべんせい}
- Family terms: {三男|さんなん}, {三女|さんじょ}, {義理|ぎり}の{親|おや} (with cross-references)
- Academic/scientific: {偏差|へんさ} ({偏差|へんさ}{値|ち}), {触媒|しょくばい}, {幻覚|げんかく}
- New kanji: 2,277 → 2,278 ({雹|ひょう})

Total entries: 10,641 → 10,671
Remaining candidates: 167 → 137

### 2026-02-08 (Vocabulary Expansion - 30 New Entries, Session 229)
Added 30 new dictionary entries (IDs 10635-10664) from candidate_words.json:

- **Verbs (6)**: もてなす (to entertain), もてはやす (to lavish praise on), {過|よぎ}る (to cross one's mind), {寄越|よこ}す (to send), {跨|また}がる (to straddle), くびれる (to be constricted)
- **Nouns (17)**: ものづくり (craftsmanship), {物|もの}の{怪|け} (evil spirit), もやし (bean sprouts), {櫓|やぐら} (tower/turret), やらせ (staged event), {幽霊|ゆうれい} (ghost), ゆかり (connection), ゆで{卵|たまご} (boiled egg), ゆとり (room/composure), わかめ (wakame seaweed), {侘|わ}び (wabi aesthetic), {引|ひ}き{出物|でもの} (wedding favor), {手筈|てはず} (arrangements), {脱力|だつりょく} (loss of strength), {茶|ちゃ}の{間|ま} (living room), {名乗|なの}り (self-introduction), {巡礼|じゅんれい} (pilgrimage), {墓参|はかまい}り (visiting a grave), もち{米|ごめ} (glutinous rice)
- **Adjectives (2)**: おっかない (scary), {気味悪|きみわる}い (creepy)
- **Adverbs (2)**: {故|ゆえ} (reason/because of), {余程|よほど} (considerably)
- **Noun (formal)**: {便宜|べんぎ} (convenience/accommodation)

Notable features:
- Multi-sense entries: {過|よぎ}る (mind/vision), {寄越|よこ}す (send/demand), {跨|また}がる (straddle/span), {幽霊|ゆうれい} (ghost/phantom), {故|ゆえ} (reason/because), {余程|よほど} (considerably/nearly), {便宜|べんぎ} (convenience/accommodation), {脱力|だつりょく} (physical/comedic style), {茶|ちゃ}の{間|ま} (room/public), {名乗|なの}り (introduce/volunteer), {巡礼|じゅんれい} (religious/anime), ゆとり (margin/composure)
- Cultural vocabulary: {侘|わ}び (wabi aesthetic), {引|ひ}き{出物|でもの} (wedding custom), {茶|ちゃ}の{間|ま} (traditional home), {巡礼|じゅんれい} (Shikoku/anime pilgrimage), {墓参|はかまい}り (grave visiting), {物|もの}の{怪|け} (folklore), {櫓|やぐら} (castle/festival)
- Food vocabulary: もやし, わかめ, ゆで{卵|たまご}, もち{米|ごめ}
- New kanji: 2,272 → 2,275 ({宜|ぎ}, {櫓|ろ}, {筈|かつ})

Total entries: 10,611 → 10,641
Remaining candidates: 178 → 167

### 2026-02-08 (Vocabulary Expansion - 30 New Entries, Session 228)
Added 30 new dictionary entries (IDs 10605-10634) from candidate_words.json:

- **Nouns (18)**: {神輿|みこし} (portable shrine), {暇潰|ひまつぶ}し (killing time), かみさん (wife), {紙芝居|かみしばい} (kamishibai), {縁日|えんにち} (temple festival), {肝試|きもだめ}し (test of courage), {取|と}り{越|こ}し{苦労|くろう} (unnecessary worry), {名義|めいぎ} (name on title), {境目|さかいめ} (boundary), {足取|あしど}り (gait/trail), {寝癖|ねぐせ} (bed hair), {腕組|うでぐ}み (folding arms), {折|お}り{返|かえ}し (return call/turnaround), {見|み}どころ (highlight), {婿|むこ} (bridegroom), {読|よ}み{聞|き}かせ (reading aloud), {飛|と}び{火|ひ} (spreading fire/impetigo), {参拝|さんぱい} (shrine visit)
- **Verbs (6)**: {漕|こ}ぎ{着|つ}ける (to manage to reach), なぞらえる (to liken), {引|ひ}っ{掛|か}ける (to hook/trick), ぶら{下|さ}げる (to hang), {触|ふ}れ{合|あ}う (to interact), {見|み}なす (to regard as), {目論|もくろ}む (to scheme)
- **I-adjectives (3)**: ひもじい (hungry), {晴|は}れ{晴|ば}れしい (bright/cheerful), {神々|こうごう}しい (divine/sublime)
- **Adverb/onomatopoeia (1)**: くちゃくちゃ (noisily chewing/crumpled)
- **Prefix (1)**: {初|はつ} (first)

Notable features:
- Cultural vocabulary cluster: {神輿|みこし}, {縁日|えんにち}, {肝試|きもだめ}し, {紙芝居|かみしばい}, {参拝|さんぱい}
- Multi-sense entries: {引|ひ}っ{掛|か}ける (3 senses), {飛|と}び{火|ひ} (3 senses), {足取|あしど}り (2 senses), {折|お}り{返|かえ}し (2 senses), くちゃくちゃ (2 senses), {見|み}どころ (2 senses), {婿|むこ} (2 senses), {触|ふ}れ{合|あ}う (2 senses)
- New kanji: 2,270 → 2,272 ({婿|せい}, {輿|よ})

Total entries: 10,581 → 10,611
Remaining candidates: 208 → 178

### 2026-02-08 (Vocabulary Expansion - 30 New Entries, Session 227)
Added 30 new dictionary entries (IDs 10575-10604) from candidate_words.json:

- **Nouns (18)**: {証拠|しょうこ} (evidence), {起訴|きそ} (indictment), {和解|わかい} (reconciliation/settlement), {弁護|べんご} (defense), {点滴|てんてき} (IV drip), {麻酔|ますい} (anesthesia), {版画|はんが} (printmaking), {織物|おりもの} (textile), {秩序|ちつじょ} (order), {逆説|ぎゃくせつ} (paradox), {心境|しんきょう} (state of mind), {胸騒|むなさわ}ぎ (foreboding), {仕返|しかえ}し (retaliation), {出来心|できごころ} (sudden impulse), {修羅場|しゅらば} (carnage/confrontation), {権限|けんげん} (authority), お{裾分|すそわ}け (sharing gifts), {機転|きてん} (quick wit), {所作|しょさ} (demeanor)
- **Verbs (6)**: {付|つ}き{添|そ}う (to accompany), {噛|か}み{合|あ}う (to mesh), {寄|よ}り{添|そ}う (to stay close), {入|い}り{浸|びた}る (to frequent), {投|な}げ{出|だ}す (to give up), そそのかす (to instigate)
- **I-adjectives (3)**: {何気|なにげ}ない (casual), {初々|ういうい}しい (fresh/innocent), {目|め}まぐるしい (dizzying)
- **Noun + suru verbs (1)**: {赴任|ふにん} (taking up a new post)
- **Noun (cultural)**: {漆|うるし} (lacquer/lacquerware)

Notable features:
- Multi-sense entries: {和解|わかい} (reconciliation/legal settlement), {漆|うるし} (lacquer/lacquerware), {噛|か}み{合|あ}う (mesh/in sync), {投|な}げ{出|だ}す (stretch out/give up), {修羅場|しゅらば} (battle/confrontation), {寄|よ}り{添|そ}う (physical/emotional)
- Legal vocabulary cluster: {証拠|しょうこ}, {起訴|きそ}, {和解|わかい}, {弁護|べんご}
- Medical vocabulary: {点滴|てんてき}, {麻酔|ますい}
- Cultural context: {漆|うるし} (lacquerware tradition), お{裾分|すそわ}け (sharing custom), {修羅場|しゅらば} (Buddhist origin), {所作|しょさ} (tea ceremony)
- Cross-references: {起訴|きそ}↔{弁護|べんご}, {付|つ}き{添|そ}う↔{寄|よ}り{添|そ}う

Total entries: 10,551 → 10,581
Remaining candidates: 238 → 208
New kanji: 2,267 → 2,270 ({漆|しつ}, {秩|ちつ}, {赴|ふ})

### 2026-02-08 (Vocabulary Expansion - 31 New Entries, Session 226)
Added 31 new dictionary entries (IDs 10544-10574) from candidate_words.json:

- **Verbs (7)**: ひっくり{返|かえ}る (to topple over), もたらす (to bring about), {真似|まね}る (to imitate), {免|まぬが}れる (to escape), {纏|まつ}わる (to be associated with), {纏|まと}う (to be clad in)
- **Nouns (20)**: {屋台|やたい} (food stall), {猫舌|ねこじた} (can't handle hot food), {朝飯前|あさめしまえ} (a piece of cake), {正座|せいざ} (formal sitting), {波紋|はもん} (ripple), {瀬戸際|せとぎわ} (brink), {土壇場|どたんば} (last moment), {先手|せんて} (initiative), {後手|ごて} (reactive position), {転売|てんばい} (resale), {内訳|うちわけ} (breakdown), {余韻|よいん} (afterglow), {感銘|かんめい} (deep impression), {手柄|てがら} (feat), {手本|てほん} (model), {手探|てさぐ}り (trial and error), {見通|みとお}し (outlook), {実態|じったい} (actual conditions), {名誉|めいよ} (honor), {奥行|おくゆ}き (depth), {貫禄|かんろく} (gravitas), {掛|か}け{声|ごえ} (rallying cry), {抹茶|まっちゃ} (matcha)
- **Adverb (1)**: {丸|まる}ごと (whole, entirely)
- **Na-adjective (1)**: {場違|ばちが}い (out of place)

Notable features:
- Multi-sense entries: ひっくり{返|かえ}る (physical/figurative), {屋台|やたい} (food stall/festival float), {波紋|はもん} (ripple/repercussions), {先手|せんて}/{後手|ごて} (strategy/board games), {手探|てさぐ}り (physical/figurative), {見通|みとお}し (forecast/visibility), {余韻|よいん} (sound/impression), {纏|まつ}わる (associated/cling)
- Cross-references: {先手|せんて}↔{後手|ごて} (antonym pair), {土壇場|どたんば}→{瀬戸際|せとぎわ}, {纏|まと}う→{纏|まつ}わる
- Cultural vocabulary: {屋台|やたい} (Fukuoka food stalls), {猫舌|ねこじた}, {正座|せいざ}, {抹茶|まっちゃ} (tea ceremony)
- Strategy/business: {先手|せんて}, {後手|ごて}, {転売|てんばい}, {内訳|うちわけ}, {見通|みとお}し, {実態|じったい}

Total entries: 10,520 → 10,551
Remaining candidates: 269 → 238
New kanji: 2,263 → 2,267 ({瀬|せ}, {禄|ろく}, {誉|よ}, {韻|いん})

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
