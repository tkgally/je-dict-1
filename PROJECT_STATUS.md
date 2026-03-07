# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-07
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
| Total entries | ~15,644 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,845 (open) |
| Candidate words | ~4,127 |
| Cross-references | ~3,400 |
| Example sentences | ~49,000 |
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

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 393)
Added 30 new dictionary entries (IDs 15559-15588) from candidate_words.json:

- **Nouns (20)**: {芥川賞|あくたがわしょう} (Akutagawa Prize), {直木賞|なおきしょう} (Naoki Prize), {処女作|しょじょさく} (debut work), {占星術|せんせいじゅつ} (astrology), {久遠|くおん} (eternity), {血圧計|けつあつけい} (blood pressure monitor), {酷寒|こっかん} (severe cold), {美人画|びじんが} (bijin-ga), {五線譜|ごせんふ} (musical staff), {毛織物|けおりもの} (woolen fabric), {静止画|せいしが} (still image), {接近戦|せっきんせん} (close-quarters combat), {病熱|びょうねつ} (fever from illness), {貯水槽|ちょすいそう} (water tank), {汚泥|おでい} (sludge), {補正予算|ほせいよさん} (supplementary budget), {高山植物|こうざんしょくぶつ} (alpine plants), {不在連絡票|ふざいれんらくひょう} (missed delivery notice), {百聞|ひゃくぶん} (hearing a hundred times), {瞬間接着剤|しゅんかんせっちゃくざい} (super glue)
- **Noun/verb-suru (3)**: {誤嚥|ごえん} (aspiration), {起案|きあん} (drafting), {急接近|きゅうせっきん} (rapid approach)
- **Noun/na-adjective (3)**: {至高|しこう} (supreme), {超一流|ちょういちりゅう} (world-class), {電気自動車|でんきじどうしゃ} (electric vehicle)
- **Noun (2)**: {公使|こうし} (diplomatic minister), {少数民族|しょうすうみんぞく} (ethnic minority)
- **Noun (1)**: {真|ま}っ{向|こう}{勝負|しょうぶ} (head-on contest)
- **Expression (1)**: {機嫌|きげん}をとる (to humor someone)

Notable features:
- Literary prizes pair: {芥川賞|あくたがわしょう}/{直木賞|なおきしょう}
- Daily life vocabulary: {不在連絡票|ふざいれんらくひょう}, {瞬間接着剤|しゅんかんせっちゃくざい}, {血圧計|けつあつけい}
- Technical/modern: {電気自動車|でんきじどうしゃ}, {静止画|せいしが}, {補正予算|ほせいよさん}
- Cultural: {美人画|びじんが}, {占星術|せんせいじゅつ}, {久遠|くおん}
- Multi-sense entry: {急接近|きゅうせっきん} (2: physical approach + relationship)
- New kanji: 2,516 → 2,517 ({芥|かい})

Total entries: ~15,614 → ~15,644 (approximate)
Remaining candidates: ~4,157 → ~4,127 (30 removed)

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 392)
Added 30 new dictionary entries (IDs 15529-15558) from candidate_words.json:

- **Nouns (12)**: {屁理屈|へりくつ} (quibble), {魔法使|まほうつか}い (wizard), {心当|こころあ}たり (having an idea), {新入社員|しんにゅうしゃいん} (new employee), {街角|まちかど} (street corner), {必需品|ひつじゅひん} (necessities), {和太鼓|わだいこ} (Japanese drum), {低地|ていち} (lowland), {望遠|ぼうえん} (telephoto), {巡|めぐ}り{合|あ}い (chance encounter), {雨|あま}だれ (raindrops from eaves), {刹那|せつな} (moment/instant)
- **Noun/verb-suru (5)**: {脱走|だっそう} (escape/desertion), {暴動|ぼうどう} (riot), {絶交|ぜっこう} (breaking off friendship), {哀悼|あいとう} (condolence), {抗争|こうそう} (conflict/feud)
- **Noun/na-adjective (3)**: {不変|ふへん} (unchanging), {印象的|いんしょうてき} (impressive), {隠密|おんみつ} (secrecy/spy)
- **Noun/verb-suru (2)**: {夏|なつ}バテ (summer heat fatigue), {留守番|るすばん} (house-sitting)
- **Expression (2)**: {根|ね}に{持|も}つ (to hold a grudge), {二|ふた}つ{返事|へんじ} (ready consent)
- **Noun (2)**: {二刀流|にとうりゅう} (dual-wielding), {破談|はだん} (broken deal)
- **Verb-godan (1)**: {近寄|ちかよ}る (to approach)
- **Verb-ichidan (1)**: {買|か}い{占|し}める (to buy up/hoard)
- **I-adjective (1)**: {男|おとこ}らしい (manly)
- **Four-character idiom (1)**: {盛者必衰|じょうしゃひっすい} (the prosperous must decline)

Notable features:
- Mix of practical daily vocabulary ({心当|こころあ}たり, {必需品|ひつじゅひん}, {留守番|るすばん}, {買|か}い{占|し}める) and cultural/literary words ({刹那|せつな}, {盛者必衰|じょうしゃひっすい}, {隠密|おんみつ})
- Social/relationship words: {絶交|ぜっこう}, {根|ね}に{持|も}つ, {巡|めぐ}り{合|あ}い
- Modern usage: {二刀流|にとうりゅう} (Ohtani), {夏|なつ}バテ, {男|おとこ}らしい
- Multi-sense entry: {二刀流|にとうりゅう} (2: swordsmanship + excelling in two fields), {隠密|おんみつ} (2: secrecy + spy)
- New kanji: 2,514 → 2,516 ({刹|せつ}, {屁|へ})

Total entries: ~15,584 → ~15,614 (approximate)
Remaining candidates: ~4,187 → ~4,157 (30 removed)

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 391)
Added 30 new dictionary entries (IDs 15499-15528) from candidate_words.json:

- **Nouns (13)**: {茶葉|ちゃば} (tea leaves), {球場|きゅうじょう} (baseball stadium), {暗室|あんしつ} (darkroom), {編|あ}み{棒|ぼう} (knitting needle), {長袖|ながそで} (long sleeves), {半袖|はんそで} (short sleeves), {藍色|あいいろ} (indigo blue), {住職|じゅうしょく} (chief temple priest), {週明|しゅうあ}け (beginning of the week), {車窓|しゃそう} (train window), {切|き}り{株|かぶ} (tree stump), {茶器|ちゃき} (tea utensils), {例|たと}え{話|ばなし} (parable)
- **Noun/verb-suru (8)**: {剥奪|はくだつ} (deprivation), {召喚|しょうかん} (summons), {助走|じょそう} (approach run), {逆戻|ぎゃくもど}り (reversal), {投球|とうきゅう} (pitching), {抹消|まっしょう} (erasure), {応戦|おうせん} (fighting back), {守備|しゅび} (defense)
- **Noun/na-adjective (4)**: {不摂生|ふせっせい} (unhealthy lifestyle), {空虚|くうきょ} (emptiness), {不可避|ふかひ} (unavoidable), {無意味|むいみ} (meaningless)
- **Noun (2)**: {徒労|とろう} (wasted effort), {背信|はいしん} (betrayal)
- **Noun (body) (1)**: {胃腸|いちょう} (stomach and intestines)
- **Noun (social) (1)**: {人付|ひとづ}き{合|あ}い (socializing)
- **Verb-ichidan (1)**: {垢抜|あかぬ}ける (to become sophisticated)

Notable features:
- Sports cluster: {守備|しゅび}, {投球|とうきゅう}, {球場|きゅうじょう}, {助走|じょそう}
- Clothing pair: {長袖|ながそで}/{半袖|はんそで}
- Cultural/traditional: {茶器|ちゃき}, {住職|じゅうしょく}, {藍色|あいいろ}
- Formal/legal: {剥奪|はくだつ}, {召喚|しょうかん}, {抹消|まっしょう}, {背信|はいしん}
- Multi-sense entries: {召喚|しょうかん} (2: legal summons + fantasy summoning), {守備|しゅび} (2: military defense + sports fielding), {応戦|おうせん} (2: counterattack + accepting a challenge)
- New kanji: 2,512 → 2,514 ({腸|ちょう}, {藍|あい})

Total entries: ~15,554 → ~15,584 (approximate)
Remaining candidates: ~4,217 → ~4,187 (30 removed)

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 390)
Added 30 new dictionary entries (IDs 15469-15498) from candidate_words.json:

- **Nouns (11)**: {道草|みちくさ} (dawdling on the way), {各駅停車|かくえきていしゃ} (local train), {平熱|へいねつ} (normal body temperature), {黒幕|くろまく} (mastermind), {蔵書|ぞうしょ} (book collection), {競泳|きょうえい} (competitive swimming), {靴底|くつぞこ} (shoe sole), {満車|まんしゃ} (parking lot full), {頭髪|とうはつ} (head hair), {五十音|ごじゅうおん} (Japanese syllabary), {出版物|しゅっぱんぶつ} (publication)
- **Noun/verb-suru (3)**: {日焼|ひや}け (sunburn/suntan), {積|つ}ん{読|どく} (buying books and not reading them), {研鑽|けんさん} (diligent study)
- **Expressions (4)**: {宝|たから}の{持|も}ち{腐|ぐさ}れ (wasted talent), {万事休|ばんじきゅう}す (all is lost), {重箱|じゅうばこ}の{隅|すみ}をつつく (to nitpick), {否|いな}めない (undeniable)
- **Na-adjectives (3)**: {罰当|ばちあ}たり (sacrilegious), {盛|も}りだくさん (packed with content), {恩知|おんし}らず (ungrateful)
- **I-adjective (1)**: {思慮深|しりょぶか}い (thoughtful, prudent)
- **Nouns (other) (5)**: {神頼|かみだの}み (praying as last resort), {打開策|だかいさく} (breakthrough measure), {立|た}ち{居振|いふ}る{舞|ま}い (deportment), {音律|おんりつ} (melody/tuning), {異聞|いぶん} (strange tale)
- **Adverb/noun (1)**: {数多|あまた} (many, numerous)
- **Noun (1)**: {洗|あら}い{場|ば} (washing area)
- **Time noun (1)**: {一昨年|いっさくねん} (year before last)

Notable features:
- Mix of practical daily vocabulary ({日焼|ひや}け, {各駅停車|かくえきていしゃ}, {満車|まんしゃ}, {靴底|くつぞこ}) and literary/cultural words ({数多|あまた}, {異聞|いぶん}, {万事休|ばんじきゅう}す)
- Multiple proverbs and set expressions: {宝|たから}の{持|も}ち{腐|ぐさ}れ, {重箱|じゅうばこ}の{隅|すみ}をつつく
- Book/reading theme: {積|つ}ん{読|どく}, {蔵書|ぞうしょ}, {出版物|しゅっぱんぶつ}
- Multi-sense entries: {日焼|ひや}け (2: skin + materials), {音律|おんりつ} (2: melody + tuning system), {異聞|いぶん} (2: strange tale + variant account)
- New kanji: 2,511 → 2,512 ({鑽|さん})

Total entries: ~15,524 → ~15,554 (approximate)
Remaining candidates: ~4,247 → ~4,217 (30 removed)

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 389)
Added 30 new dictionary entries (IDs 15439-15468) from candidate_words.json:

- **Expressions (9)**: {意地|いじ}を{張|は}る (to be stubborn), {腰|こし}を{下|お}ろす (to sit down), {手|て}に{負|お}えない (unmanageable), {目|め}を{輝|かがや}かせる (eyes light up), {腰|こし}を{抜|ぬ}かす (frozen with shock), {満員御礼|まんいんおんれい} (full house), {火|ひ}の{用心|ようじん} (beware of fire), {命|いのち}に{関|かか}わる (life-threatening), {首|くび}を{縦|たて}に{振|ふ}る (to nod yes)
- **Nouns (7)**: {非対面|ひたいめん} (non-face-to-face), {発送済|はっそうず}み (shipped), {永住権|えいじゅうけん} (permanent residency), {鎮痛剤|ちんつうざい} (painkiller), {老夫婦|ろうふうふ} (elderly couple), {名著|めいちょ} (masterpiece book), {新年度|しんねんど} (new fiscal year)
- **Noun/verb-suru (3)**: {精通|せいつう} (being well-versed), {熟達|じゅくたつ} (proficiency), {抑止力|よくしりょく} (deterrent force)
- **Verbs (3)**: {引|ひ}き{連|つ}れる (to take along), {奪|うば}い{合|あ}う (to scramble for), {踏|ふ}みにじる (to trample)
- **Na-adjective (1)**: {全般的|ぜんぱんてき} (overall)
- **Adverb (1)**: {従来通|じゅうらいどお}り (as before)
- **Other nouns (4)**: {下|した}の{名前|なまえ} (given name), {開発者|かいはつしゃ} (developer), {免状|めんじょう} (diploma), {雨乞|あまご}い (praying for rain)
- **Verb-ichidan (1)**: {取|と}り{留|と}める (to save a life)
- **Multi-sense verb (1)**: {踏|ふ}みにじる (2: literal trampling + figurative violation)

Notable features:
- Strong emphasis on expressions and idioms (9 entries)
- Practical daily life: {発送済|はっそうず}み, {非対面|ひたいめん}, {鎮痛剤|ちんつうざい}, {開発者|かいはつしゃ}
- Culture: {満員御礼|まんいんおんれい}, {火|ひ}の{用心|ようじん}, {雨乞|あまご}い
- Immigration/legal: {永住権|えいじゅうけん}
- New kanji: 2,510 → 2,511 ({乞|こ})

Total entries: ~15,494 → ~15,524 (approximate)
Remaining candidates: ~4,277 → ~4,247 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
