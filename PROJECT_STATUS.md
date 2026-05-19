# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-05-15
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

### 2026-05-19 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 27790-27811) from `candidate_words.json`, all newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Nouns (15)**: {茅葺|かやぶ}き (thatched roof), {娘婿|むすめむこ} (son-in-law), {真夏|まなつ} (midsummer), {涙目|なみだめ} (teary eyes), {空梅雨|からつゆ} (dry rainy season), {谷間|たにま} (valley/gap), {二枚舌|にまいじた} (double-talk), {救世主|きゅうせいしゅ} (savior), {狂気|きょうき} (madness), {強度|きょうど} (strength/intensity), {慰安|いあん} (comfort/recreation), {神業|かみわざ} (superhuman feat), {旗印|はたじるし} (banner/rallying cause), {骨抜|ほねぬ}き (boning; gutting — two senses), {棋士|きし} (professional shogi/go player), {水墨画|すいぼくが} (ink wash painting)
- **Verbs (5)**: {治|おさ}まる (to subside, godan, intransitive), {巣立|すだ}つ (to leave the nest, godan, intransitive), {貯|た}める (to save up money, ichidan, transitive), {慰|なぐさ}む (to be comforted, godan, intransitive), {休|やす}まる (to feel at ease, godan, intransitive)
- **Other (1)**: {細々|ほそぼそ}と (barely/scraping by, adverb)

Two new kanji introduced: {茅|かや} (thatch, ID 02744) and {葺|ふ}く (roofing, ID 02745). All 22 entries validate; furigana check clean.

### 2026-05-18 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch)
Added 25 new dictionary entries (IDs 27765-27789) from `candidate_words.json`, all newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Nouns (16)**: {稼|かせ}ぎ (earnings), {国中|くにじゅう} (the whole country), {雲隠|くもがく}れ (vanishing suddenly), {隠|かく}れ{蓑|みの} (cover/front), {快楽|かいらく} (pleasure), {思|おも}い{付|つ}き (whim), {売|う}れ{残|のこ}り (unsold goods), {揃|そろ}い{踏|ぶ}み (lineup), お{揃|そろ}い (matching items), {足並|あしな}み (acting in unison), {小回|こまわ}り (maneuverability), {能面|のうめん} (Noh mask), {能舞台|のうぶたい} (Noh stage), {占|うらな}い{師|し} (fortune-teller), {皮脂|ひし} (sebum), {手相|てそう} (palmistry)
- **Verbs (7)**: {狩|か}る (to hunt, godan, transitive), {考|かんが}え{付|つ}く (to think up, godan, transitive), {轢|ひ}く (to run over, godan, transitive), {煮出|にだ}す (to brew/boil to extract, godan, transitive), {煮|に}つける (to simmer in seasoned broth, ichidan, transitive), {埋|う}め{立|た}てる (to reclaim land, ichidan, transitive), {言|い}い{及|およ}ぶ (to mention, godan, intransitive)
- **Other (2)**: くんくん (sniff sniff, onomatopoeia), うかうか (carelessly, adverb)

One new kanji introduced: {蓑|みの} (raincoat), assigned kanji ID 02743. All 25 entries validate; furigana check clean.

### 2026-05-18 (Vocabulary Expansion - 25 New Entries, Oldest-Candidate Batch)
Added 25 new dictionary entries (IDs 27740-27764) from `candidate_words.json`. No "seen in entry" candidates remained, so selection fell back to the oldest unprocessed candidates, picking genuine standalone words and skipping the many auto-harvested compound fragments, typos, and numbers. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Geography (4)**: {西|にし}アジア (West Asia), {北|きた}アフリカ (North Africa), {中央|ちゅうおう}アメリカ (Central America), ラテンアメリカ (Latin America)
- **Biology / nature (4)**: {脊椎|せきつい}{動物|どうぶつ} (vertebrate), {節足|せっそく}{動物|どうぶつ} (arthropod), {地衣|ちい}{類|るい} (lichen), {嫌気|けんき}{性|せい} (anaerobic)
- **Medical / anatomy (6)**: {唾液|だえき}{腺|せん} (salivary gland), {良性|りょうせい}{腫瘍|しゅよう} (benign tumor), {夜尿|やにょう}{症|しょう} (bedwetting), {膝|しつ}{関節|かんせつ} (knee joint), {肩|けん}{関節|かんせつ} (shoulder joint), {消化|しょうか}{器官|きかん} (digestive organs)
- **Science / technical (4)**: {気圧|きあつ}{配置|はいち} (pressure pattern), セルロース (cellulose), ゼロエミッション (zero emission), {破擦|はさつ}{音|おん} (affricate)
- **Everyday objects / loanwords (4)**: {防錆|ぼうせい}{剤|ざい} (rust preventative), {裁断|さいだん}{機|き} (cutting machine), スウェットパーカー (hoodie), メモリースティック (memory stick)
- **Other (3)**: {平角|へいかく} (straight angle), オンサイド (onside — sports), {問題|もんだい}をはらむ (to be fraught with problems — expression)

No new kanji introduced. All 25 entries validate; furigana check clean. No verbs or i-adjectives in this batch.

### 2026-05-17 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 27718-27739) from `candidate_words.json`, all "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Nouns (16)**: バスケット (basket; basketball, two senses), {生糸|きいと} (raw silk), {養蚕|ようさん} (sericulture), {見物人|けんぶつにん} (spectator), {重工業|じゅうこうぎょう} (heavy industry), {軽工業|けいこうぎょう} (light industry), {布巾|ふきん} (dish cloth), {麻|あさ} (hemp/linen), {農協|のうきょう} (agricultural cooperative), {自然史|しぜんし} (natural history), {発明品|はつめいひん} (invention), {地上波|ちじょうは} (terrestrial broadcasting), {現在地|げんざいち} (current location), {種目|しゅもく} (event/category), {既存|きそん} (existing), {公会堂|こうかいどう} (public hall)
- **Adjectives (2)**: {文法的|ぶんぽうてき} (grammatical, na-adj), {衛生的|えいせいてき} (sanitary, na-adj)
- **Verb (1)**: {録|と}る (to record audio/video, godan, transitive)
- **Other (3)**: あんた (you, casual pronoun), とっくに (long ago, adverb), {久々|ひさびさ} (after a long time)

Removed stale candidate 坊ちゃん (duplicate of existing 坊っちゃん, 16357). No new kanji introduced. All 22 entries validate; furigana check clean.

### 2026-05-17 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch)
Added 25 new dictionary entries (IDs 27693-27717) from `candidate_words.json`, all "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 3 sections.

- **Food / cake nouns (8)**: ショートケーキ (strawberry shortcake), チョコレートケーキ (chocolate cake), モンブラン (Mont Blanc), シフォンケーキ (chiffon cake), ポテトサラダ (potato salad), グリーンサラダ (green salad), マカロニサラダ (macaroni salad), コールスロー (coleslaw)
- **Clothing nouns (9)**: ウールコート (wool coat), トレンチコート (trench coat), レインコート (raincoat), フリーサイズ (one size fits all), ビーチサンダル (flip-flops), ウール (wool), タートルネック (turtleneck), ブリーフ (briefs), トランクス (boxer shorts)
- **Other nouns (8)**: ミリグラム (milligram), カツサンド (pork cutlet sandwich), リサイタル (recital), {銀幕|ぎんまく} (silver screen), モノラル (mono audio), コンポ (component stereo), {発表会|はっぴょうかい} (recital/presentation), {准看護師|じゅんかんごし} (licensed practical nurse)

No new kanji introduced. All 25 entries validate; furigana check clean. No verbs or i-adjectives in this batch.

### 2026-05-16 (Vocabulary Expansion - 20 New Entries, Oldest-Candidate Batch)
Added 20 new dictionary entries (IDs 27673-27692) from `candidate_words.json`. No "seen in entry" candidates remained, so selection fell back to the oldest unprocessed candidates, picking genuine standalone words and skipping the many auto-harvested compound fragments. Per-field budgets followed the reference shape of {もてなし} (27261).

- **Technology nouns (2)**: ハードドライブ (hard drive), ディレクトリ (directory)
- **Loanword verb-suru / na-adjective (3)**: ウォーミングアップ (warm-up), カウントダウン (countdown), エネルギッシュ (energetic)
- **Culture / everyday nouns (6)**: {浮世離|うきよばな}れ (being unworldly), {幕間|まくあい} (intermission), {生|う}まれ{変|か}わり (reincarnation), {冷奴|ひややっこ} (chilled tofu), {草木染|くさきぞ}め (plant dyeing), スウェットシャツ (sweatshirt)
- **Science / nature nouns (5)**: {微生物学|びせいぶつがく} (microbiology), {剥製|はくせい} (taxidermy), {卵殻|らんかく} (eggshell), {渋柿|しぶがき} (astringent persimmon), {平原|へいげん} (plain)
- **Health / society nouns (4)**: {恐怖症|きょうふしょう} (phobia), {神経過敏|しんけいかびん} (oversensitivity), {先駆者|せんくしゃ} (pioneer), {共謀者|きょうぼうしゃ} (co-conspirator)

Removed 1 stale candidate flagged as a duplicate by the batch check: {時代遅|じだいおく}れ (already entry 12719). One new kanji ({奴|やっこ}) introduced and assigned ID 02742. All 20 entries validate; furigana check clean; conjugation tables added to the 3 verb-suru entries.

### 2026-05-16 (Vocabulary Expansion - 21 New Entries, Oldest-Candidate Batch)
Added 21 new dictionary entries (IDs 27652-27672) from `candidate_words.json`. No "seen in entry" candidates remained, so selection fell back to the oldest unprocessed candidates, skipping the many typos and non-words mixed into that range. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Expressions (4)**: を{対象|たいしょう}に (aimed at), {当|あ}てがない (to have no prospect), {私情|しじょう}を{交|まじ}える (to let personal feelings interfere), {白日|はくじつ}の{下|もと}に{晒|さら}す (to bring to light)
- **Counter / adverb (2)**: {着|ちゃく} (counter for suits of clothing), つい{先|さき}ほど (just a moment ago)
- **Science / technical nouns (4)**: {排泄物|はいせつぶつ} (bodily waste), {模式図|もしきず} (schematic diagram), {屈折率|くっせつりつ} (refractive index), {比重|ひじゅう} (specific gravity; relative importance — two senses)
- **Everyday / culture nouns (7)**: {福音書|ふくいんしょ} (Gospel), {牛蒡茶|ごぼうちゃ} (burdock tea), {遠近感|えんきんかん} (sense of depth), {兵隊|へいたい} (soldier), {和牛|わぎゅう} (wagyu), {秒針|びょうしん} (second hand), {稲光|いなびかり} (flash of lightning)
- **Society / education nouns (4)**: {収賄|しゅうわい} (bribery, verb-suru), {談判|だんぱん} (negotiation, verb-suru), {弁舌|べんぜつ} (eloquence), {課外授業|かがいじゅぎょう} (extracurricular lesson)

Removed 2 stale candidates flagged as duplicates by the batch check: を巡って (already entry 27595) and 状/じょう (already entry 09878). No new kanji introduced. All 21 entries validate; furigana check clean; conjugation tables added to the 2 verb-suru entries.

### 2026-05-15 (Vocabulary Expansion - 23 New Entries, "seen in entry" + Oldest-Candidate Batch)
Added 23 new dictionary entries (IDs 27629-27651). The first 19 were "seen in entry" candidates from `candidate_words.json` (words already referenced inside existing entries but not yet defined); the last 4 were drawn from the oldest unprocessed candidates. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264); top-level glosses kept short, notes scoped to 2–4 sections.

- **Loanwords (4)**: グランドホテル (grand hotel), ガット (racket gut/string), ルールブック (rulebook), {巨峰|きょほう} (Kyoho grape variety)
- **Architecture / objects (1)**: {板垣|いたがき} (wooden board fence)
- **Time / calendar (5)**: {十五日|じゅうごにち} (15th of the month), {先年|せんねん} (some years ago, formal), {二時間|にじかん} (two hours), {六十日|ろくじゅうにち} (60 days), {六|ろっ}ヶ{月|げつ} (six months)
- **Cultural / nature (3)**: {中秋|ちゅうしゅう} (mid-autumn), {名月|めいげつ} (harvest moon), {馳走|ちそう} (feast — usually as ご{馳走|ちそう})
- **Grammar / suffix (1)**: {気味|ぎみ} (-ish, somewhat — suffix)
- **Counters (4)**: {一房|ひとふさ} (a bunch), {一粒|ひとつぶ} (a grain/drop), {六本|ろっぽん} (six long objects), {何階|なんかい} (what floor)
- **Adverb / verb / state (3)**: {一度|ひとたび} (literary 'once'), {居残|いのこ}る (to stay behind, godan intransitive), {空|から} (empty — distinguished from {空|そら}/{空|くう})
- **Polite daily-life (1)**: お{迎|むか}え (pickup / welcoming, polite)
- **History / formal (1)**: {戦敗国|せんぱいこく} (defeated nation)

Removed 4 stale candidates: 売り上げ (orthographic variant of existing 04102_uriage), 三階/さんかい (existing 27617_sangai already discusses both readings), グーテンベルク (proper noun, low learner utility), and 多目的に/ためきてきに (typo — correct reading is たもくてきに). No new kanji introduced. All 23 entries validate; furigana check clean.

### 2026-05-15 (Vocabulary Expansion - 22 New Entries, "seen in entry" Internal-Completeness Batch)
Added 22 new dictionary entries (IDs 27607-27628) drawn from the "seen in entry" candidates in `candidate_words.json` — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264); top-level glosses kept short, definitions and notes scoped to 2–4 sections.

- **Places / facilities (3)**: {焼|や}け{跡|あと}, {各部屋|かくへや}, {釣|つ}り{堀|ぼり}
- **Verb / adjective (2)**: {逃|に}げ{回|まわ}る (godan), {滑|すべ}りやすい (i-adj)
- **Daily-life nouns (3)**: {逃|に}げ{道|みち}, {滑|すべ}り{止|ど}め (two senses: anti-slip + backup school), いじめっ{子|こ}
- **Workplace / education (4)**: {企画部|きかくぶ}, {医学部|いがくぶ}, {医学生|いがくせい}, {歯学|しがく}
- **People (2)**: {釣|つ}り{人|びと}, {田舎者|いなかもの}
- **Onomatopoeia / expression (2)**: どしどし, あれから
- **Numbers / counters (3)**: {三階|さんがい}, {二回|にかい}, {合|ごう} (two senses: 180 ml volume + mountain station)
- **Culture / material (3)**: {誠|まこと}, {留袖|とめそで}, {絹糸|きぬいと}

Removed stale candidate C20556 ({一回り} with the wrong reading いっかいり; correct reading ひとまわり already exists as entry 11235). No new kanji introduced. All 22 entries validate; furigana check clean.

### 2026-05-14 (Vocabulary Expansion - 20 New Entries, Mixed "seen in entry" + Oldest-Candidates Batch)
Added 20 new dictionary entries (IDs 27587-27606) from candidate_words.json. Mix of "seen in entry" internal-completeness candidates and oldest unprocessed candidates. Per-field length budgets followed reference shape ({もてなし} 27261, {埃|ほこり}まみれ 27264).

- **Organizations / money (4)**: {日本放送協会|にっぽんほうそうきょうかい} (NHK), {日本銀行券|にっぽんぎんこうけん} (Bank of Japan note), ゆうちょ{銀行|ぎんこう} (Japan Post Bank), {佐藤|さとう} (common surname)
- **Food / drink (4)**: たまり{醤油|じょうゆ}, {南蛮漬|なんばんづ}け, ハイボール, カフェオレ
- **Greetings / expressions (3)**: おかえりなさいませ (very polite welcome back), お{願|ねが}いいたします (very polite please), {始|はじ}め{良|よ}ければ{終|お}わり{良|よ}し (proverb)
- **Grammar patterns (3)**: を{巡|めぐ}って (concerning/over), なければならない (must), なくてはいけない (must)
- **Numbers (2)**: {二億|におく}, {一万|いちまん}
- **Other (4)**: さみしい (variant of 寂しい), こだま (echo / Kodama Shinkansen), {十二支|じゅうにし} (zodiac), {一酸化炭素|いっさんかたんそ} (CO)

No new kanji introduced. All 20 entries validated successfully; furigana checks clean for the session range.

### 2026-05-14 (Vocabulary Expansion - 24 New Entries, "seen in entry" Internal-Completeness Batch)
Added 24 new dictionary entries (IDs 27563-27586) from candidate_words.json, all flagged as "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition. Drawn from low-ID gaps (entries ~00659-01083). No new kanji introduced. Per-field length budgets followed reference shape ({もてなし} 27261, {埃|ほこり}まみれ 27264).

- **Direction / location (2)**: {西側|にしがわ} (west side), {端|はし}っこ (edge, informal)
- **Wallets & money (3)**: {長財布|ながさいふ} (long wallet), がま{口|ぐち} (clasp purse), {釣|つ}り{銭|せん} (change, formal)
- **Food / drink (5)**: {水飴|みずあめ} (starch syrup), {完熟|かんじゅく} (fully ripe, noun + verb-suru), ロゼワイン (rosé wine), スパークリングワイン (sparkling wine), {社食|しゃしょく} (company cafeteria, informal)
- **Materials / nature (1)**: わら (straw)
- **Discourse expressions (3)**: だからこそ (precisely because), そういえば (come to think of it), それはそうと (by the way)
- **Time (2)**: {未明|みめい} (predawn), {学期末|がっきまつ} (end of term)
- **Business / institutions (2)**: {常務|じょうむ} (managing director), {水道局|すいどうきょく} (water bureau)
- **Travel & transport (3)**: メトロ (metro), カプセルホテル (capsule hotel), {乗換案内|のりかえあんない} (transfer guide)
- **Fashion / shopping (2)**: ミニスカート (miniskirt), {特売日|とくばいび} (sale day)
- **Education (1)**: {二年生|にねんせい} (second-year student)

Total entries: 27,354 → 27,378.

### 2026-05-14 (Vocabulary Expansion - 23 New Entries, "seen in entry" Internal-Completeness Batch)
Added 23 new dictionary entries (IDs 27540-27562) from candidate_words.json, all flagged as "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition. Drawn from low-ID gaps (entries ~00612-01090). One new kanji ({燗|かん}) added to the kanji index. Per-field length budgets followed reference shape ({もてなし} 27261, {埃|ほこり}まみれ 27264).

- **Verb (1)**: {譲|ゆず}り{受|う}ける (to inherit / take over, ichidan, transitive)
- **Geography (4)**: {北側|きたがわ} (north side), {南側|みなみがわ} (south side), {南風|みなみかぜ} (south wind), {東北|とうほく} (Tohoku region)
- **Food & drink (5)**: {冷酒|れいしゅ} (cold sake), {熱燗|あつかん} (hot sake — new kanji 燗), {濃口|こいくち} (dark soy sauce), {薄口|うすくち} (light soy sauce), {料理屋|りょうりや} (traditional Japanese restaurant)
- **Home & kitchen (3)**: {野菜室|やさいしつ} (vegetable compartment), {製氷機|せいひょうき} (ice maker), ミトン (mittens / oven mitt)
- **Work & money (3)**: {通勤費|つうきんひ} (commuting expenses), {残業時間|ざんぎょうじかん} (overtime hours), {給料日|きゅうりょうび} (payday)
- **Education (3)**: {小|しょう}テスト (quiz), {一年生|いちねんせい} (first-year student), {三年生|さんねんせい} (third-year student)
- **Other (4)**: うち (my home / my place, colloquial), ストライプ (stripe), {大浴場|だいよくじょう} (large communal bath), {名刺入|めいしい}れ (business card case)

### 2026-05-13 (Vocabulary Expansion - 22 New Entries, "seen in entry" Internal-Completeness Batch)
Added 22 new dictionary entries (IDs 27518-27539) from candidate_words.json, all flagged as "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition. Drawn from low-ID gaps (entries ~00050-00816). Two new kanji ({捌|さば}, {閏|うるう}) added to the kanji index. Per-field length budgets followed reference shape ({もてなし} 27261, {埃|ほこり}まみれ 27264).

- **Orthographic / structural (1)**: {付属|ふぞく} (more common spelling of {附属|ふぞく}; noun, verb-suru, no-adjective)
- **Verbs (2)**: {洗|あら}い{出|だ}す (to identify / uncover, godan, two senses), {捌|さば}く (to dress fish / handle skillfully, godan, two senses — new kanji 捌)
- **Adjective (1)**: ユーモラス (humorous, na-adjective)
- **Time (3)**: {来学期|らいがっき} (next semester), {来春|らいしゅん} (next spring, formal), {閏年|うるうどし} (leap year — new kanji 閏)
- **Geography (1)**: {西日本|にしにほん} (western Japan)
- **Loanwords — drinking and dining (2)**: バーベキュー (BBQ — also verb-suru), スナック (snack / Japanese-style hostess bar, two senses)
- **Loanwords — other (5)**: マイクロプラスチック (microplastics), ゴーストライター (ghostwriter), カーポート (carport), カーブ (curve / curveball, two senses), パブ (pub)
- **Transportation slang (3)**: チャリ (bike, informal), ママチャリ (utility bicycle with basket), ハイヤー (chauffeured hire car)
- **Daily / cultural (3)**: {難易度|なんいど} (difficulty level), {秋田犬|あきたいぬ} (Akita dog breed — cross-references {柴犬|しばいぬ} 27503), {土用|どよう} (doyō / 18-day seasonal period)
- **Weather / science (1)**: {零度|れいど} (zero degrees)

Total entries: 27,309 → 27,331. Two new kanji ({捌|さば} → 02739_hachi_saba_handle, {閏|うるう} → 02740_jun_uruu_intercalary) assigned.

### 2026-05-13 (Vocabulary Expansion - 25 New Entries, "seen in entry" Internal-Completeness Batch)
Added 25 new dictionary entries (IDs 27493-27517) from candidate_words.json, all flagged as "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition. Drawn from low-ID gaps (entries ~00513-00806). One new kanji ({柴|しば}) added to the kanji index. Per-field length budgets followed reference shape ({もてなし} 27261, {埃|ほこり}まみれ 27264).

- **Basic concepts and grammar (3)**: {会|かい} (meeting/association, two senses), {面白|おもしろ}そう (looks interesting — -そう evidential form), どうやって (how, by what method)
- **Time / life-stage (2)**: {晩年|ばんねん} (one's later years), {先行|さきゆ}き (future prospects, business outlook)
- **Seasons / weather (2)**: {冬物|ふゆもの} (winter clothing), {春風|はるかぜ} (spring breeze)
- **Business / law (1)**: {有限会社|ゆうげんがいしゃ} (limited liability company — note 2006 reform)
- **Body / family (2)**: {左足|ひだりあし} (left foot/leg), {片親|かたおや} (single parent — modern preference noted)
- **Travel / transport (2)**: {国内線|こくないせん} (domestic flight), {国際線|こくさいせん} (international flight)
- **Animals (2)**: {柴犬|しばいぬ} (Shiba Inu — new kanji 柴), {愛犬|あいけん} (beloved pet dog)
- **Holiday / culture (2)**: ハロウィン (Halloween), {勤労感謝|きんろうかんしゃ} (Labor Thanksgiving)
- **Objects / household (5)**: ブリーフケース (briefcase), {引|ひ}き{戸|ど} (sliding door), {砂時計|すなどけい} (hourglass), {一階|いっかい} (first floor), {二階|にかい} (second floor)
- **Food / health / sound (4)**: {甘辛|あまから}い (sweet-and-savory, i-adj), {音楽家|おんがくか} (musician), {温水|おんすい} (warm/heated water), {粉薬|こなぐすり} (powdered medicine)

Total entries: 27,284 → 27,309. One new kanji ({柴|しば} → 02738_sai_shiba_brushwood) assigned.

### 2026-05-12 (Vocabulary Expansion - 20 New Entries, Mixed "seen in entry" + Older Candidates)
Added 20 new dictionary entries (IDs 27473-27492) from candidate_words.json. The first 10 are "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition (drawn from low-ID gaps ~00416-00868). The remaining 10 are older standing candidates: a formal idiom, technical/medical nouns, an everyday loanword, sports/dieting nouns, and one verb-phrase expression. No new kanji introduced. Per-field length budgets followed reference shape ({もてなし} 27261, {埃|ほこり}まみれ 27264).

- **"Seen in entry" — household / scissors / scenery (10)**: {上棚|うわだな} (upper shelf), {吸|す}い{物|もの}{椀|わん} (clear soup bowl), {末広|すえひろ}がり (auspicious widening shape), {裁|た}ちばさみ (fabric scissors), {爪切|つめき}りばさみ (nail scissors), {岩場|いわば} (rocky area), {岩肌|いわはだ} (rock face), {岩登|いわのぼ}り (rock climbing), {音波|おんぱ} (sound wave), {畔|ほとり} (water's edge — literary)
- **Formal / set expressions (2)**: {病魔|びょうま}と{闘|たたか}う (to battle illness — formal/obituary register), {二|ふた}つに{割|わ}る (to split in two — literal and figurative)
- **Technical / scientific nouns (3)**: ろ{過器|かき} (filter device), {末梢神経|まっしょうしんけい} (peripheral nerve), {含水量|がんすいりょう} (water content)
- **Dining / sports / health (4)**: テーブルナプキン (table napkin — distinct from sanitary ナプキン), {一塁手|いちるいしゅ} (first baseman), ヨーヨー{現象|げんしょう} (yo-yo dieting effect), {着地地点|ちゃくちちてん} (landing point — literal and figurative)
- **Transportation (1)**: {給水車|きゅうすいしゃ} (water tanker truck — disaster-relief context)

Total entries: 27,264 → 27,284.

### 2026-05-12 (Vocabulary Expansion - 23 New Entries, "seen in entry" Internal-Completeness Batch)
Added 23 new dictionary entries (IDs 27450-27472) from candidate_words.json, all flagged as "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition. Drawn from low-ID gaps (entries ~00149-00587). No new kanji introduced. Per-field length budgets followed reference shape ({もてなし} 27261, {埃|ほこり}まみれ 27264).

- **Prefectures (3)**: {兵庫|ひょうご} (Hyogo), {奈良|なら} (Nara), {新潟|にいがた} (Niigata)
- **Time — formal variants (2)**: {明日|みょうにち} (tomorrow, formal), {昨日|さくじつ} (yesterday, formal)
- **Currency / international (2)**: {日本円|にっぽんえん} (Japanese yen), ワールドカップ (World Cup)
- **うわ- compounds and similar (4)**: うわべ (outward appearance), {上手|うわて} (upper hand / upstream — two senses, distinct reading from じょうず), {上向|うわむ}き (upward / upward trend — two senses), {外履|そとば}き (outdoor shoes)
- **Adverb (1)**: わりかし (fairly, informal variant of {割|わり}と)
- **Sailing loanwords (2)**: ヨットレース (yacht race), ヨットハーバー (marina)
- **School (1)**: {吹奏楽部|すいそうがくぶ} (brass / wind ensemble club)
- **Counters / quantifiers (5)**: {何位|なんい} (what place), {二位|にい} (second place), {幾日|いくにち} (how many days), {幾人|いくにん} (how many people), {全問|ぜんもん} (all questions)
- **Geography / culture (3)**: {火口原|かこうげん} (caldera floor), {豪雪地帯|ごうせつちたい} (heavy snowfall region), {白無垢|しろむく} (white wedding kimono)
- **Stale candidates removed (2)**: お父さま (duplicate of お父様 27446); ぞくぞくする (covered by ぞくぞく 27435)

Total entries: 27,241 → 27,264.

### 2026-05-12 (Vocabulary Expansion - 20 New Entries, "seen in entry" Internal-Completeness Batch)
Added 20 new dictionary entries (IDs 27430-27449) from candidate_words.json, all flagged as "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition. Drawn from low-ID polish gaps (entries ~00255-00595). No new kanji introduced. Per-field length budgets tightened (target shape: {作|さく} or {埃|ほこり}まみれ, not the verbose 27386-27421 range).

- **Verbs (2)**: {持|も}っていく (to take with one, godan; auxiliary {行|い}く is irregular — past forms fixed by hand), {誤|あやま}る (to err/misjudge, godan, formal register)
- **Nouns — body / medical (1)**: {胸部|きょうぶ} (chest, thoracic region — clinical register)
- **Nouns — society / society-adjacent (4)**: {被災地|ひさいち} (disaster-stricken area), {税法|ぜいほう} (tax law), {作|さく} (creative work, often as suffix), {食|た}べ{方|かた} (way of eating)
- **School / company "{部|ぶ}" compounds (4)**: {野球部|やきゅうぶ}, {美術部|びじゅつぶ}, {文芸部|ぶんげいぶ} (school clubs), {開発部|かいはつぶ} (R&D department)
- **Family — polite terms (3)**: お{父様|とうさま}, {弟|おとうと}さん, {妹|いもうと}さん
- **Transportation (1)**: {各駅|かくえき} (each station; {各駅停車|かくえきていしゃ})
- **Food (1)**: {青|あお}りんご (green apple)
- **Adverbs / mimetics (1)**: ぞくぞく (shivering / thrilled — two-sense mimetic; auto-conjugator incorrectly tagged it as a godan-ku verb on the romaji-ending fallback; fixed by hand)
- **Expressions / adnominals (2)**: そのもの (X itself, emphatic), ちょっとした (slight / quite a — two-sense adnominal)
- **Stale candidate removed (1)**: 潰す (つぶす) was a duplicate of existing 00410_tsubusu; removed from candidate list during sync.

Total entries: 27,221 → 27,241.

### 2026-05-11 (Vocabulary Expansion - 20 New Entries, "seen in entry" Internal-Completeness Batch)
Added 20 new dictionary entries (IDs 27410-27429) from candidate_words.json, all flagged as "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition. This batch focuses on formal business correspondence vocabulary, fashion/swimwear loanwords, food loanwords, and several missing nouns. Two new kanji (憺, 欅) added to the kanji index.

- **Formal business correspondence (3)**: {高配|こうはい} (kind consideration/patronage), {引|ひ}き{立|た}て (patronage/support), {業務上|ぎょうむじょう} (professional/occupational)
- **Fashion / swimwear loanwords (4)**: ファー (fur), フェイクファー (faux fur), ビキニ (bikini), ラッシュガード (rash guard)
- **Food loanwords (2)**: ミルクティー (milk tea), コンデンスミルク (condensed milk)
- **Performance/evaluation loanwords (2)**: ケアレスミス (careless mistake), ノーミス (flawless run)
- **Nouns (8)**: {惨憺|さんたん} (wretched, taru-adj), {協同|きょうどう} (cooperation), もみほぐす (to massage thoroughly, godan), {欅|けやき} (zelkova), ナット (nut fastener), {狙|ねら}い{目|め} (sweet spot/opportunity), {水仙|すいせん} (narcissus), フィギュアスケート (figure skating), クロス (cloth / cross, two-sense)

### 2026-05-11 (Vocabulary Expansion - 24 New Entries, Internal-Completeness "seen in entry" Batch)
Added 24 new dictionary entries (IDs 27386-27409) from candidate_words.json, all flagged as "seen in entry" candidates — words referenced by existing entries' examples or notes but lacking their own definition. This batch closes early-ID (entries ~00049-00275) cross-reference gaps surfaced by comprehensive-polish runs. One new kanji (尉) added to the kanji index.

- **Loanwords for daily/commercial life (10)**: ガムテープ (packing tape), ガムシロップ (gum syrup), ショッピングモール (shopping mall), グランドオープン (grand opening), シャンパン (champagne), ジョッキ (beer mug), ロックグラス (rocks glass), クレーム (complaint), スーパーマーケット (supermarket), マイクロフォン (microphone)
- **Plants/nature (1)**: つる (vine, tendril)
- **Verbs (2)**: {這|は}いつくばる (to prostrate oneself, godan), {申|もう}し{立|た}てる (to lodge a complaint, ichidan)
- **Traditional culture / craft (3)**: {竹垣|たけがき} (bamboo fence), {干|ほ}し{菓子|がし} (dried sweets), ガリ (pickled ginger for sushi)
- **Health / body (2)**: {指圧|しあつ} (shiatsu), {整体|せいたい} (chiropractic-style body adjustment)
- **Legal / technical / formal (4)**: {重過失|じゅうかしつ} (gross negligence), {大尉|たいい} (captain rank), {係数|けいすう} (coefficient), {許|ゆる}し (forgiveness/permission)
- **Expression (1)**: ついてない (out of luck, colloquial)
- **Other (1)**: {部員|ぶいん} (club/department member)

Total entries: 27,177 → 27,201. Candidates: 1,679 → 1,655.

### 2026-05-10 (Vocabulary Expansion - 22 New Entries, Internal-Completeness "seen in entry" Batch)
Added 22 new dictionary entries (IDs 27364-27385) from candidate_words.json, all flagged as "seen in entry" candidates — words that already appeared in existing entries' examples or notes but had no entry of their own. This batch addresses early-ID (entries ~00138-00205) cross-reference gaps surfaced by comprehensive-polish runs.

- **Loanwords for media/design (8)**: コメンタリー (commentary), スピン (spin / spin-off), モダン (modern, stylish), カスタム (custom, customize), アングル (camera angle), モニタリング (monitoring), スイーツ (sweets/desserts), ポップ (pop / shelf-talker — three senses)
- **Music & arts (2)**: {歌曲|かきょく} (art song), シンガーソングライター (singer-songwriter)
- **Daily life / housing (2)**: {持|も}ち{家|いえ} (owned home), {金魚鉢|きんぎょばち} (goldfish bowl, with figurative sense)
- **End-of-life planning (1)**: {終活|しゅうかつ} (end-of-life preparations)
- **Weather & meteorology (3)**: {大気圧|たいきあつ} (atmospheric pressure), {気圧計|きあつけい} (barometer), {気象病|きしょうびょう} (weather-related illness)
- **Verbs (1)**: {立|た}ち{返|かえ}る (to return to a starting point/principle — godan, intransitive)
- **Finance / forms (5)**: {累進|るいしん} (progressive/graduated, esp. taxation), {一定額|いっていがく} (a fixed amount), {希望額|きぼうがく} (desired amount), {希望日|きぼうび} (preferred date), {水温|すいおん} (water temperature)

All entries follow v2 quality standards: structured notes with bulleted sections (collocations, similar words, usage notes), 3+ examples per sense with progressive length, explicit similar-word distinctions, and full furigana coverage. Verb and suru-verb entries received full conjugation tables.

### 2026-05-10 (Vocabulary Expansion - 15 New Entries, Internal-Completeness "seen in entry" Batch)
Added 15 new dictionary entries (IDs 27349-27363) from candidate_words.json, all flagged as "seen in entry" candidates — words that already appeared in existing entries' examples or notes but had no entry of their own. Filling these closes internal-completeness gaps so cross-references can resolve.

- **Volcano / disaster (3)**: {噴火口|ふんかこう} (volcanic crater/vent), {大噴火|だいふんか} (major eruption — noun + suru-verb), {見舞|みま}われる (to be struck by — passive verb of misfortune)
- **Workplace / business (2)**: {部外|ぶがい} (outside the department; in {部外者|ぶがいしゃ}, {部外秘|ぶがいひ}), {銀行印|ぎんこういん} (bank-registered personal seal)
- **Education (1)**: {教習|きょうしゅう} (instruction, esp. driving school)
- **Culture / music (1)**: {雅楽|ががく} (gagaku, traditional Japanese court music)
- **Time (1)**: {月|つき}{半|なか}ば (middle of the month)
- **Math (1)**: {小数|しょうすう} (decimal number — distinct from homophone {少数|しょうすう} "minority")
- **Astronomy (2)**: {自転|じてん} (rotation on its own axis), {公転|こうてん} (orbital revolution) — cross-referenced as a contrast pair
- **Weather / atmosphere (1)**: {気流|きりゅう} (air current; in {乱気流|らんきりゅう} "turbulence")
- **Health statistics (1)**: {患者数|かんじゃすう} (number of patients)
- **Building / HVAC (2)**: {空調|くうちょう} (air conditioning, HVAC), {通気|つうき} (passive ventilation, breathability)
- 15 candidates synced (removed from candidate list)
- All 15 entries pass validation; 5 verbs received conjugation tables (4 suru + 1 ichidan); no new kanji introduced

Total entries: 27,140 → 27,155.

### 2026-05-09 (Vocabulary Expansion - 20 New Entries, Internal-Completeness "seen in entry" Batch)
Added 20 new dictionary entries (IDs 27329-27348) from candidate_words.json, all flagged as "seen in entry" candidates — words that already appeared in existing entries' examples or notes but had no entry of their own. Filling these closes internal-completeness gaps.

- **Slang / people (1)**: バツニ (divorced twice — slang sibling of バツイチ)
- **Sports / leisure (4)**: ベンチプレス (bench press), フォアボール (baseball walk / base on balls), スリーボール (3-ball count), ツーストライク (2-strike count)
- **Clothing (2)**: カウボーイハット (cowboy hat), ウェディングドレス (wedding dress)
- **Transportation / leisure (1)**: {手漕|てこ}ぎ (rowing by hand; rowboat-related)
- **Kanji-radical names (2)**: てへん ({扌|てへん} hand radical), くさかんむり ({艹|くさかんむり} grass-crown radical)
- **Food (3)**: パルメザンチーズ (Parmesan cheese), チーズフォンデュ (cheese fondue), デザートメニュー (dessert menu)
- **Conjunctions (2)**: だけども (but, more emphatic variant of だけど), だけれど (but, slightly more formal than だけど)
- **Counters / coins (3)**: {円玉|えんだま} (yen coin, used after a denomination), {二歩|にほ} (two steps; also the shogi nifu foul), {何歩|なんぽ} (how many steps)
- **Technical (2)**: {符号化|ふごうか} (encoding — math/computing/info-theory term), {句読符号|くとうふごう} (punctuation marks — formal collective term)
- 1 stale candidate removed (たち, kana variant of existing entry 01551 達/たち); 20 candidates synced
- All 20 entries pass validation; 1 suru-verb received conjugation table; no new kanji introduced

Total entries: 27,120 → 27,140.

### 2026-05-09 (Vocabulary Expansion - 46 New Entries, Internal-Completeness Batch)
Added 46 new dictionary entries (IDs 27283-27328) from candidate_words.json. Prioritized "seen in entry" candidates — words referenced by existing entries' examples or notes but not yet defined. This closes internal-completeness gaps and lets cross-references resolve correctly.

- **Verbs (3)**: {余|あま}す (to leave over — transitive pair of {余|あま}る), {凹|へこ}ます (to dent / dishearten — transitive of {凹|へこ}む), {響|ひび}かせる (to make resound — transitive of {響|ひび}く)
- **Suru-verbs / nouns (3)**: ドレスアップ (dressing up), ホームステイ (homestay), {治水|ちすい} (flood control)
- **Na-adjective (1)**: {地理的|ちりてき} (geographical)
- **Adverb / noun (1)**: {通常|つうじょう} (normally; the regular state)
- **Sports / leisure (8)**: バッター (batter), ダッグアウト (dugout), サッカーボール (soccer ball), カウボーイ (cowboy), プレイボーイ (playboy), ボーイフレンド (boyfriend), ボーイスカウト (Boy Scouts), {開会式|かいかいしき} (opening ceremony)
- **Transportation (6)**: モーターボート (motorboat), ゴムボート (rubber dinghy), カヤック (kayak), サイドブレーキ (parking brake), フットブレーキ (foot brake), エンジンブレーキ (engine braking)
- **Cards / shapes (2)**: ハート (heart — shape, suit, mental strength), スペード (spade — card suit)
- **Food (4)**: クリームチーズ (cream cheese), ナチュラルチーズ (natural cheese), チーズバーガー (cheeseburger), タルト (tart)
- **Clothing (4)**: ダウンコート (down coat), ダウンジャケット (down jacket), ドレスコード (dress code), ペンダント (pendant)
- **Building / home (4)**: {理容院|りよういん} (barbershop), マイホーム (one's own home), {墓石|ぼせき} (gravestone), ボストンバッグ (Boston bag)
- **Tools / objects (3)**: コイル (electrical coil), ノブ (knob), {頬紅|ほほべに} (blush)
- **Communication / events (2)**: ドアチャイム (door chime), {時報|じほう} (time signal)
- **Other (4)**: バイオリニスト (violinist), {古銭|こせん} (old coin), {暴風雪|ぼうふうせつ} (blizzard), {普段使|ふだんづか}い (everyday use), {彫|ほ}り{物|もの} (carving / tattoo)
- 46 candidates synced (removed from candidate list)
- All 46 entries pass validation; 6 verbs received conjugation tables; no new kanji introduced

Total entries: 27,074 → 27,120.

### 2026-05-08 (Vocabulary Expansion - 22 New Entries, Batch 109)
Added 22 new dictionary entries (IDs 27261-27282) from candidate_words.json. Focused on culturally significant concepts, useful expressions, and practical vocabulary for intermediate learners.

- **Expressions (3)**: お{待|ま}たせ (sorry for the wait), {楽|らく}にする (to relax/make easy), {表|おもて}に{出|だ}す (to bring to light/expose)
- **Cultural (2)**: もてなし (hospitality), {趣味|しゅみ}{嗜好|しこう} (tastes and preferences)
- **Business/Formal (3)**: {経営|けいえい}{破綻|はたん} (business failure), {膠着|こうちゃく}{状態|じょうたい} (stalemate), {消除|しょうじょ}する (to eliminate/remove)
- **Travel/Transport (3)**: {出張先|しゅっちょうさき} (business trip destination), {乗車口|じょうしゃぐち} (boarding entrance), {個人|こじん}{旅行|りょこう} (independent travel)
- **Nature/Place (1)**: {向|む}こう{岸|ぎし} (far shore)
- **Food/Drink (2)**: そば{粉|こ} (buckwheat flour), {無味|むみ} (tastelessness)
- **Health/Medical (2)**: {快癒|かいゆ} (recovery/healing), {色素|しきそ}{沈着|ちんちゃく} (pigmentation)
- **Daily Life (3)**: {埃|ほこり}まみれ (covered in dust), お{姉|ねえ}ちゃん (older sister, informal), {換気口|かんきこう} (ventilation opening)
- **Other (3)**: {先導者|せんどうしゃ} (leader/guide), フラッシュバック (flashback), {名言集|めいげんしゅう} (book of quotations)

Total entries: 27,052 → 27,074.

### 2026-05-07 (Vocabulary Expansion - 30 New Entries, Batch 107)
### 2026-05-08 (Vocabulary Expansion - 30 New Entries, Batch 108)
Added 30 new dictionary entries (IDs 27231-27260) from candidate_words.json. Mix of culturally significant concepts, practical vocabulary, adverbs, and compound nouns for intermediate learners.

- **Cultural/Psychology (2)**: {甘|あま}え (dependence on indulgence), {学者肌|がくしゃはだ} (scholarly temperament)
- **Adverbs/Expressions (8)**: {永遠|えいえん}に (forever), {永久|えいきゅう}に (permanently), こうやって (like this), どこにも (nowhere/everywhere), {自然|しぜん}に (naturally), {無料|むりょう}で (for free), {十分|じゅうぶん}に (sufficiently), なかなかない (rare/hard to find)
- **Work/Business (3)**: {情報|じょうほう}{収集|しゅうしゅう} (information gathering), {職歴書|しょくれきしょ} (resume/CV), {登録済|とうろくず}み (registered)
- **Status/Condition (3)**: {完了済|かんりょうず}み (completed), {耐|た}えられない (unbearable), {普通|ふつう}でない (unusual)
- **Body/Posture (2)**: {身構|みがま}え (defensive stance), {前傾姿勢|ぜんけいしせい} (forward-leaning posture)
- **Food/Culture (1)**: {回転焼|かいてんや}き (regional name for imagawayaki)
- **Science/Education (3)**: {天王星|てんのうせい} (Uranus), {消化液|しょうかえき} (digestive fluid), {就学前|しゅうがくまえ} (preschool age)
- **Places/Things (4)**: {中央部|ちゅうおうぶ} (central part), {映写機|えいしゃき} (projector), {宝物庫|ほうもつこ} (treasure house), {現像所|げんぞうじょ} (photo developing lab)
- **Society (3)**: {無関心|むかんしん}さ (indifference), {口|くち}コミ{評判|ひょうばん} (word-of-mouth reputation), {農繁期|のうはんき} (busy farming season)
- **Other (1)**: {眠|ねむ}りにつく (to fall asleep)

Total entries: 27,022 → 27,052.

### 2026-05-07 (Vocabulary Expansion - 30 New Entries, Batch 107)
Added 30 new dictionary entries (IDs 27201-27230) targeting common words missing from the dictionary. Focus on culturally rich vocabulary, useful expressions, and everyday concepts for intermediate learners.

- **Infrastructure/Nature (3)**: {信号機|しんごうき} (traffic light), {大潮|おおしお} (spring tide), {蓮|はす} (lotus)
- **Crime/Law (4)**: {脅迫|きょうはく} (threat/intimidation), {脅|おど}す (to threaten), {恐喝|きょうかつ} (blackmail/extortion), {恩赦|おんしゃ} (amnesty/pardon)
- **Education (1)**: {課外|かがい} (extracurricular)
- **Time (1)**: {宵|よい} (evening/early night)
- **Health (1)**: {水虫|みずむし} (athlete's foot)
- **Personality/Character (5)**: お{人好|ひとよ}し (pushover), {下心|したごころ} (ulterior motive), {魂胆|こんたん} (scheme), {思|おも}い{上|あ}がり (arrogance), {鵜呑|うの}み (accepting uncritically)
- **Actions/Behavior (4)**: {横取|よこど}り (snatching), つまみ{食|ぐ}い (sneaking a taste), {居留守|いるす} (pretending to be out), {居候|いそうろう} (freeloading)
- **Expressions/Proverbs (3)**: {水|みず}の{泡|あわ} (all for nothing), {身|み}から{出|で}た{錆|さび} (reaping what you sow), しっぺ{返|がえ}し (retaliation)
- **Daily Life/General (8)**: {手違|てちが}い (mix-up), {見切|みき}る (to give up on), {行|い}き{当|あ}たりばったり (haphazard), {豆知識|まめちしき} (trivia), {口火|くちび} (trigger/spark), {引|ひ}き{延|の}ばし (stalling), {見当外|けんとうはず}れ (off the mark), {丸腰|まるごし} (unarmed/unprepared)

Total entries: 26,992 → 27,022.

### 2026-05-07 (Vocabulary Expansion - 20 New Entries, Batch 106)
Added 20 new dictionary entries (IDs 27181-27200) from candidate_words.json. Mix of workplace, weather, news, food, cultural, and daily life vocabulary.

- **Workplace/Business (5)**: {無給休暇|むきゅうきゅうか} (unpaid leave), {臨時会議|りんじかいぎ} (emergency meeting), {定期会議|ていきかいぎ} (regular meeting), {内部情報|ないぶじょうほう} (insider information), {経済効果|けいざいこうか} (economic effect)
- **Weather (3)**: {雷雲|らいうん} (thundercloud), {積乱雲|せきらんうん} (cumulonimbus), {秋雨前線|あきさめぜんせん} (autumn rain front)
- **News/Disaster (2)**: {死傷者|ししょうしゃ} (casualties), {爆風|ばくふう} (blast wind)
- **People/Culture (3)**: {創始者|そうししゃ} (founder), {口伝|くちづて} (word of mouth), {経済大国|けいざいたいこく} (economic superpower)
- **Expressions/Verbs (2)**: {格好|かっこう}つける (to show off), {声|こえ}が{枯|か}れる (to become hoarse)
- **Description (1)**: {最重要|さいじゅうよう} (most important)
- **Daily Life (3)**: {向|む}かい{合|あ}わせ (facing each other), {防火扉|ぼうかとびら} (fire door), {野菜料理|やさいりょうり} (vegetable dish)
- **Education (1)**: {学校制度|がっこうせいど} (school system)
- 2 stale candidates removed; 20 candidates synced

Total entries: 26,972 → 26,992.

### 2026-05-07 (Vocabulary Expansion - 22 New Entries, Batch 104)
Added 22 new dictionary entries (IDs 27141-27162) from candidate_words.json. Diverse vocabulary covering geography, law, arts, nature, linguistics, and abstract concepts.

- **Geography/Nature (2)**: {祖国|そこく} (homeland), {湖面|こめん} (lake surface)
- **Animals (2)**: {雄鹿|おじか} (stag), {雌鹿|めじか} (doe)
- **Law/Politics (2)**: {罰則|ばっそく} (penal provisions), {非暴力|ひぼうりょく} (nonviolence)
- **Arts (1)**: {油彩|ゆさい} (oil painting)
- **Linguistics/Education (2)**: {旧字体|きゅうじたい} (old-form kanji), {新字体|しんじたい} (new-form kanji)
- **Abstract/Formal (5)**: {錯誤|さくご} (error), {贈与|ぞうよ} (gift/donation), {取捨|しゅしゃ} (selection), {困苦|こんく} (hardship), {無策|むさく} (lack of policy)
- **Culture/Sports (2)**: {構|かま}え (stance/posture), {稽古場|けいこば} (practice hall)
- **Science/Technical (2)**: {気泡|きほう} (air bubble), {波形|はけい} (waveform)
- **Description (2)**: まだら (mottled/spotted), {無毒|むどく} (nontoxic)
- **Plants (1)**: {果樹|かじゅ} (fruit tree)
- **Honorific (1)**: {閣下|かっか} (Your Excellency)
- 22 candidates synced

Total entries: 26,932 → 26,954.

### 2026-05-07 (Vocabulary Expansion - 17 New Entries, Batch 105)
Added 17 new dictionary entries (IDs 27163-27180) from candidate_words.json. Mix of useful vocabulary spanning adverbs, na-adjectives, cultural terms, and formal/academic nouns.

- **Adverb (1)**: {一|ひと}つ{一|ひと}つ (one by one)
- **Na-adjectives (5)**: {通俗的|つうぞくてき} (popular/lowbrow), {組織的|そしきてき} (organized), {実際的|じっさいてき} (practical), {習慣的|しゅうかんてき} (habitual), {非効率的|ひこうりつてき} (inefficient), {地域的|ちいきてき} (regional)
- **Cultural/Food (2)**: {大判焼|おおばんや}き (filled cake), {粋人|すいじん} (sophisticate)
- **Language/Linguistics (2)**: {定型句|ていけいく} (set phrase), {美化語|びかご} (beautifying language)
- **Emotion/Social (2)**: {敵対心|てきたいしん} (hostility), {障害者|しょうがいしゃ} (person with disability)
- **Formal/News (2)**: {負傷者|ふしょうしゃ} (injured person), {諸条件|しょじょうけん} (various conditions)
- **Other (2)**: せどり (retail arbitrage), {突破力|とっぱりょく} (breakthrough ability), {可動式|かどうしき} (movable type)
- 1 stale candidate removed (均一化する — already existed)
- 18 candidates synced

Total entries: 26,954 → 26,972.

### 2026-05-07 (Vocabulary Expansion - 30 New Entries, Batch 103)
Added 30 new dictionary entries (IDs 27111-27140) from candidate_words.json. Diverse vocabulary covering cultural terms, daily life, food, travel, and workplace vocabulary.

- **Verbs (2)**: {華|はな}やぐ (to brighten/become festive), {掘|ほ}り{出|だ}す (to dig out/discover)
- **Food/Cooking (4)**: {焼|や}き{方|かた} (way of grilling), {魚市場|うおいちば} (fish market), {厚焼|あつや}き (thick omelette), {和食屋|わしょくや} (Japanese restaurant)
- **Culture/Religion (4)**: {戦国|せんごく} (warring states), {口伝|くでん} (oral tradition), {慰霊祭|いれいさい} (memorial service), {作務|さむ} (temple work)
- **People/Society (3)**: {学友|がくゆう} (school friend), {文筆家|ぶんぴつか} (writer), {草食系|そうしょくけい} (passive/herbivore type)
- **Work/Business (4)**: {係員|かかりいん} (attendant), {経歴書|けいれきしょ} (CV/resume), {配達先|はいたつさき} (delivery destination), {文章化|ぶんしょうか} (putting into writing)
- **Travel/Places (3)**: {途中下車|とちゅうげしゃ} (stopover), {展望所|てんぼうじょ} (viewing platform), {再入国|さいにゅうこく} (re-entry)
- **Daily life (3)**: {常備|じょうび} (keeping on hand), {遅寝|おそね} (going to bed late), {閲覧室|えつらんしつ} (reading room)
- **Communication/Language (2)**: {発話|はつわ} (speech/utterance), {対比的|たいひてき} (contrasting)
- **Description (3)**: {局地的|きょくちてき} (localized), {美文字|びもじ} (beautiful handwriting), {普及率|ふきゅうりつ} (adoption rate)
- **Other (2)**: {似顔|にがお} (likeness/portrait), {焼|や}き{印|いん} (branding mark)
- 29 candidates synced

Total entries: 26,902 → 26,932.

### 2026-05-07 (Vocabulary Expansion - 26 New Entries, Batch 102)
Added 26 new dictionary entries (IDs 27085-27110) from candidate_words.json. Focus on broadly useful vocabulary for intermediate learners: everyday expressions, cultural terms, and workplace vocabulary.

- **Adverb/Onomatopoeia (1)**: こつこつ (steadily; with tapping sound)
- **Expressions (3)**: {昔々|むかしむかし} (once upon a time), {上|うえ}から{目線|めせん} (condescending attitude), {取|と}るに{足|た}らない (insignificant)
- **Workplace/Business (3)**: {辞表|じひょう} (resignation letter), {勤務形態|きんむけいたい} (work arrangement), {準備不足|じゅんびぶそく} (lack of preparation)
- **Pronoun (1)**: {自分自身|じぶんじしん} (oneself)
- **Texture/Sensory (1)**: ざらつく (to feel rough)
- **Health/Body (1)**: {血色|けっしょく} (complexion)
- **Geography/Nature (2)**: {沼地|ぬまち} (swamp), {村落|そんらく} (village)
- **Military/News (2)**: {銃撃|じゅうげき} (shooting), {隊列|たいれつ} (formation)
- **Education (1)**: {短期大学|たんきだいがく} (junior college)
- **Life/Society (2)**: {身辺整理|しんぺんせいり} (putting affairs in order), {福音|ふくいん} (gospel/good news)
- **Culture (3)**: {五月人形|ごがつにんぎょう} (Boys' Day doll), ゲームセンター (arcade), {無法|むほう} (lawless)
- **Abstract (2)**: {才覚|さいかく} (resourcefulness), {潔|いさぎよ}さ (integrity)
- **Technology (1)**: インストールする (to install)
- **Psychology (1)**: {心的外傷|しんてきがいしょう} (psychological trauma)
- 20 stale duplicate candidates removed; 26 candidates synced

Total entries: 26,876 → 26,902.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
