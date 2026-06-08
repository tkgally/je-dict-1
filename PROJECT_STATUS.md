# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-06-08
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

### 2026-06-08 (Maintenance - Spurious Non-Verb Conjugation Cleanup)
One-time deterministic cleanup (`prompts/fix_spurious_conjugations.md`). Stripped fabricated verb conjugation tables and stray `verb_class` tags from **133 non-verb entries** (101 adverbs/onomatopoeia/noun-adverbs/na-adjectives/nouns/auxiliaries + 32 reviewed expressions — idioms, proverbs, adverbial phrases, and two compound-ている forms). Examples of the nonsense removed: ぐつぐつ (adverb) had `ぐつぐたない`/`ぐつぐちます`; 空いている had `空いていらない`/`空いていった`.

- **Root-cause fix**: replaced the guard in `build/add_conjugations.py` (`if not any('verb' in p ...)`) with an exact-enum verb-POS membership test. The old substring check matched `"adverb"` (it contains "verb"), letting adverbs with a stray `verb_class` tag generate godan tables. `add_adjective_conjugations.py` was already correctly guarded.
- **New tool**: built `build/prune_nonverb_conjugations.py` (reusable audit/pruner; dry-runs by default, holds back `expression` entries for review).
- **Verified**: all 28,743 entries valid; re-running both retrofits re-adds nothing; spurious-conjugation and stray-`verb_class` detectors both return 0.
- **Knowledge base**: resolved Cleanup Backlog P6, Tooling Backlog item 5, the Schema Tag Reliability "defense in depth" note, and five Entry Follow-ups sections; logged 02525_suiteiru (resolved) and a curator follow-up for お会いする (22190). Out-of-scope wrong-class/missing-table cases left open.

### 2026-06-07 (Vocabulary Expansion - 22 New Entries, Recent Candidates Batch)
Added 22 new dictionary entries (IDs 28931-28952) from `candidate_words.json`. No "seen in entry" candidates remained in the queue, so the session drew from recent unprocessed candidates favoring concrete everyday vocabulary (citrus varieties, hot-pot dishes, wedding styles, lighting, prefecture). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): top-level glosses 3-8 words, notes scoped to 2-3 focused sections.

- **Citrus / food (7)**: {温州|うんしゅう}みかん (satsuma mandarin), ポンカン (ponkan), デコポン (dekopon / sumo orange), {合|あ}わせ{味噌|みそ} (blended miso), {両手鍋|りょうてなべ} (two-handled pot), もつ{鍋|なべ} (offal hot pot), キムチ{鍋|なべ} (kimchi hot pot)
- **Lighting / clothing (3)**: タンクトップ (tank top), フラッシュライト (flashlight, loanword), ペンライト (penlight — 2 senses incl. idol concert stick, 6 examples)
- **Wedding ceremony set (3)**: {神前式|しんぜんしき} (Shinto), {教会式|きょうかいしき} (Christian), {人前式|じんぜんしき} (secular)
- **People / occupation (2)**: {盗掘者|とうくつしゃ} (grave robber / tomb raider), フォトグラファー (photographer, freelance/commercial register)
- **Daily life / housing (3)**: {本宅|ほんたく} (main residence, formal), ショッピングセンター (shopping center), ガス{料金|りょうきん} (gas bill)
- **Health / geography / culture (4)**: {筋肉量|きんにくりょう} (muscle mass), ペアリング (matching ring / pairing — 2 senses, 6 examples), {国技館|こくぎかん} (sumo arena), {富山県|とやまけん} (Toyama Prefecture)

Two romaji slips fixed pre-build (loanwords ending in ー needed `aa` rather than `a`: フォトグラファー → fotogurafaa, ショッピングセンター → shoppingusentaa); eight bare-kanji slips in notes annotated. Three stale candidates removed during pre-flight (C21493 躱す/かわす — kanji variant of existing 28851_kawasu; C21180 〜主義者 — already entry 28362; C21328 猪突猛進 — already entry 28872). No new kanji. No verbs / i-adjectives in this batch, so no conjugation tables needed. Candidate list synced (1470→1448).

### 2026-06-07 (Vocabulary Expansion - 25 New Entries, Recent Candidates Batch)
Added 25 new dictionary entries (IDs 28906-28930) from `candidate_words.json`. No "seen in entry" candidates remained in the queue, so the session drew from the most recently added candidates. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): top-level glosses 3-8 words, notes scoped to two or three focused sections.

- **Verbs (6)**: {照|て}り{返|かえ}す (to reflect light/heat), {尖|とが}らせる (to sharpen / purse lips / set nerves on edge), {乞|こ}う (literary "to beg"), {潰|つい}える (dreams/plans collapse), {屈|かが}める (to bend one's body), {苦悶|くもん}する (to writhe in agony, noun + suru)
- **Food / cooking (6)**: {湯割|ゆわ}り (spirits cut with hot water), {薄皮|うすかわ} (thin skin/peel), {白味噌|しろみそ} (white miso), {赤味噌|あかみそ} (red miso), {水炊|みずた}き (mizutaki hot pot), {片手鍋|かたてなべ} (saucepan)
- **People / family (3)**: {子息|しそく} (another's son, formal), {一人息子|ひとりむすこ} (only son), {武者|むしゃ} (warrior, samurai)
- **Daily life / society (5)**: タワーマンション (high-rise condo), {積立金|つみたてきん} (reserve fund / installment savings), {等級|とうきゅう} (grade/rank), {内地|ないち} (Japanese mainland, 2 senses, 6 examples), {両足|りょうあし} (both feet/legs)
- **Other (5)**: {恨|うら}み{言|ごと} (words of resentment), {酸性雨|さんせいう} (acid rain), {弱酸性|じゃくさんせい} (mildly acidic), {手前味噌|てまえみそ} (self-praise idiom), {大志|たいし} (great ambition, Clark quote)

Conjugation tables added by `add_conjugations.py` for all six verb entries. All 25 entries validated, no missing furigana, no new kanji needed indexing.

### 2026-06-07 (Vocabulary Expansion - 21 New Entries, "seen in entry" + Backlog Batch)
Added 21 new dictionary entries (IDs 28885-28905) from `candidate_words.json`. The first 18 cleared the full "seen in entry" internal-completeness backlog (words already referenced inside existing entries 02217 and 05294-05554 but not yet defined); the final 3 came from recent unprocessed candidates. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Math / geometry (6)**: {球|きゅう} (sphere), {角錐|かくすい} (pyramid solid), {表面積|ひょうめんせき} (surface area), {角柱|かくちゅう} (prism / square pillar), {六角形|ろっかくけい} (hexagon), {内角|ないかく} (interior angle / inside corner — 2 senses, 6 examples)
- **Tech / loanwords (5)**: アイコン (icon / profile picture), {長押|なが}し (long press), シュノーケリング (snorkeling), コーン (cone — geometric / ice cream / traffic), キャンドル (decorative candle)
- **Geography / culture (3)**: ギリシャ (Greece), {他国|たこく} (other country), {洋|よう} (Western-style prefix)
- **Other (7)**: {多生|たしょう} (Buddhist many-rebirths, in 袖振り合うも多生の縁), ひら (flat side / palm), {美|び} (abstract beauty / aesthetic), お{決|き}まり (the usual / standard order), {一例|いちれい} (one example), {多肉植物|たにくしょくぶつ} (succulent plant), ステープラー (formal-register stapler)

All 21 entries validate on first pass; furigana clean. No verbs / i-adjectives, so no conjugation tables needed. No new kanji. Candidate list synced (1519→1498).

### 2026-06-06 (Vocabulary Expansion - 24 New Entries, "seen in entry" + Backlog Batch)
Added 24 new dictionary entries (IDs 28861-28884) from `candidate_words.json`. The first three filled "seen in entry" internal-completeness gaps (referenced in 03477, 03792, 03417); the rest came from the oldest-unprocessed and recent backlog. Per-field budgets followed the reference shape of {もてなし} (27261) — short top-level glosses (3-8 words), 2-3 focused note sections.

- **Time-period set (4)**: {三年間|さんねんかん} (three years), {二年|にねん} (two years, 2 senses), {一年間|いちねんかん} (one year), {二年間|にねんかん} (two years)
- **Government / academic (4)**: {文部科学|もんぶかがく} (MEXT prefix), {四則|しそく} (four arithmetic operations), {線形|せんけい} (linear), {理学|りがく} (natural science)
- **Martial arts (2)**: {小手|こて} (kendo gauntlet / strike, 2 senses), {組|く}み{手|て} (sparring)
- **Daily life (5)**: {失|な}くし{物|もの} (lost item), {湯加減|ゆかげん} (bath temperature), リビングルーム (living room), {両側|りょうがわ} (both sides), {式場|しきじょう} (ceremony hall)
- **Hobbies / culture (3)**: {藤棚|ふじだな} (wisteria trellis), {珠算|しゅざん} (abacus calculation), {塗|ぬ}り{絵|え} (coloring page)
- **Other (6)**: むちゃくちゃ (na-adj / adverb, 2 senses), {猪突猛進|ちょとつもうしん} (charging recklessly), {各紙|かくし} (each newspaper), {大喜|おおよろこ}び (great joy), お{詫|わ}びする (to apologize, polite), {真|しん} (truth / true prefix, 2 senses)

Also removed one stale candidate (C21676 打ち明ける/ぶちあける — duplicates 04230_uchiakeru).

### 2026-06-06 (Vocabulary Expansion - 23 New Entries, "seen in entry" + Backlog Batch)
Added 23 new dictionary entries (IDs 28838-28860) from `candidate_words.json`. The first 9 came from the most recent "seen in entry" internal-completeness candidates referenced inside existing entries 05259-05389; the next 14 are higher-quality oldest-unprocessed candidates from May/early June. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **School / health / first aid (5)**: {出席停止|しゅっせきていし} (school attendance suspension), {季節性|きせつせい} (seasonality), {三角巾|さんかくきん} (triangular bandage / cooking head scarf — 2 senses, 6 examples), {傷薬|きずぐすり} (wound medicine), ボクサー (boxer — athlete)
- **Outdoor recreation (2)**: {磯遊|いそあそ}び (tide pool exploration), {磯釣|いそづ}り (rock fishing)
- **Cooking / kitchen (3)**: {包丁|ほうちょう}さばき (knife skills), {蒸籠|せいろ} (bamboo steamer), {切|き}り{方|かた} (way of cutting)
- **Verbs (2)**: かわす (godan, dodge / deflect — 2 senses, 6 examples), {擦|す}れる (ichidan, rub / wear thin / become jaded — 3 senses, 9 examples)
- **Nature / culture (3)**: {水草|みずくさ} (water plant), {笹団子|ささだんご} (Niigata mugwort dumpling), {笹飾|ささかざ}り (Tanabata bamboo decoration)
- **Society / politics (4)**: {仕事人|しごとにん} (dedicated professional), {税制|ぜいせい} (tax system), ステレオタイプ (stereotype), {総辞職|そうじしょく} (cabinet en bloc resignation — also suru)
- **Other (4)**: よけ (suffix, repellent / guard), {思|おも}い{入|い}れ (emotional attachment), {両輪|りょうりん} (two essential elements — 2 senses, 4 examples), {単機能|たんきのう} (single-function appliance)

All 23 entries validate after a fix-up round: one romaji slip on {磯釣|いそづ}り (`isodzuri` → `isozuri` per the validator's づ→z mapping) and one bare-kanji 水草 → {水草|みずくさ} in {水草|みずくさ}'s SIMILAR WORDS section. Conjugation tables added: 1 godan (かわす), 1 ichidan ({擦|す}れる), 1 suru ({総辞職|そうじしょく}). No new kanji. Candidate list synced (1523→1501). C21676 打ち明ける/ぶちあける skipped pre-flight as a reading variant of existing 04230_uchiakeru.

### 2026-06-06 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch)
Added 25 new dictionary entries (IDs 28813-28837) from `candidate_words.json`, all drawn from "seen in entry" internal-completeness candidates (words referenced inside existing entries 05272-05389 but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Loanwords / tech (4)**: ドラッグ (drag — computing, also suru), ショッピング (shopping, also suru), クリアファイル (clear plastic folder, wasei-eigo), ガーゼ (gauze, from German)
- **Mimetics / adverbs (4)**: ひやっとする (sudden chill, suru-verb), つぶつぶ (grainy bumps), よたよた (tottering), ぺたんと (with a flat plop)
- **Measurement (2)**: ミリ (millimeter / milli- prefix — 2 senses, 6 examples), ヘクタール (hectare)
- **Food / daily life (3)**: {春巻|はるま}き (spring roll), {食|た}べ{過|す}ぎ (overeating), {風呂場|ふろば} (bathroom)
- **School clubs / governance (5)**: {運動部|うんどうぶ} (sports club), {文化部|ぶんかぶ} (cultural club), {児童会|じどうかい} (elementary student council), {学生会|がくせいかい} (university student government), {養護教諭|ようごきょうゆ} (school nurse)
- **Health / medical (4)**: {便秘薬|べんぴやく} (consumer term for laxative), {下剤|げざい} (medical-register laxative — pair with 28831), お{通|つう}じ (polite term for bowel movement), {喚起|かんき} (arousing attention; formal, also suru)
- **Other (3)**: {眉唾|まゆつば} (fishy / dubious story), {最寄|もよ}り (nearest — esp. station), {押|お}し{花|ばな} (pressed flower)

All 25 entries validate after a fix-up round: one initial `formality: "polite"` value on お{通|つう}じ corrected to `"neutral"` (polite isn't in the enum); one ミリ reading fixed from katakana to hiragana per project rules; one typo in ミリ ex3 ({部品|ひんぶん} → {部品|ぶひん}); one bare-kanji 部 in {文化部|ぶんかぶ} notes given furigana. Four suru-verbs (ひやっとする, ドラッグ, ショッピング, {喚起|かんき}) received full conjugation tables via add_conjugations.py. No new kanji. Candidate list synced (1548→1523).

### 2026-06-05 (Vocabulary Expansion - 20 New Entries, "seen in entry" + Food Batch)
Added 20 new dictionary entries (IDs 28793-28812) from `candidate_words.json`. The first 15 came from the most recent "seen in entry" internal-completeness candidates (words referenced inside existing entries 02213-05249 but not yet defined); the final 5 are oldest unprocessed food/education candidates. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Place / proper noun (1)**: {東照宮|とうしょうぐう} (Toshogu Shrine)
- **Animals / nature (1)**: {朱鷺|とき} (Japanese crested ibis)
- **Arts / music (2)**: コンクール (competition), {混声|こんせい} (mixed voices, choral)
- **Household / appliances (2)**: スチーム (steam, appliance function), テラス (terrace)
- **Medical / health (4)**: {副反応|ふくはんのう} (vaccine side effect), {風疹|ふうしん} (rubella), コロナ (COVID), {救急病院|きゅうきゅうびょういん} (emergency hospital)
- **Public services (2)**: {出動|しゅつどう} (dispatch, suru-verb), パトロールカー (patrol car)
- **Tech / communication (1)**: ビデオチャット (video chat)
- **Food (5)**: {春|はる}キャベツ (spring cabbage), わけぎ (wakegi/bunching onion), パンケーキ (pancakes), {肉|にく}まん (steamed pork bun), {蒸|む}しパン (steamed cake)
- **Counting / measurement (1)**: {件数|けんすう} (number of cases)
- **Education (1)**: {短大|たんだい} (junior college)

All 20 entries validate. One initial schema slip on 28796_konsei (`domain: "music"` not in enum) fixed by clearing the domain. One suru-verb (28803_shutsudou) received its full conjugation table via add_conjugations.py. Two stale candidates removed during pre-flight (C21523 洗濯機/せんたっき is the colloquial reading of existing 04969_sentakuki せんたくき; C21640 長葱/ながねぎ is a kanji variant of existing 14827_naganegi 長ねぎ). No new kanji. Candidate list synced (1533→1513).

### 2026-06-05 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28771-28792) from `candidate_words.json`, drawn from the most recent "seen in entry" internal-completeness candidates (words referenced inside existing entries 05071-05249 but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Loanwords / tech (7)**: オゾン (ozone), ウェットスーツ (wetsuit), タッチスクリーン (touchscreen), フリック (flick gesture), ショートカット (2 senses: keyboard shortcut + women's short hair, 6 examples), ツーリング (motorcycle touring, also suru), ヘアアイロン (hair iron / straightener)
- **Nature / science (5)**: {鉱脈|こうみゃく} (ore vein), {葉脈|ようみゃく} (leaf vein), {円周率|えんしゅうりつ} (pi), {対数|たいすう} (logarithm), {不織布|ふしょくふ} (non-woven fabric)
- **Food / daily life (4)**: メロンパン (melon bread), {紅生姜|べにしょうが} (pickled red ginger), かっぱ{巻|ま}き (cucumber sushi roll), {飴色|あめいろ} (amber / caramel color)
- **Society / abstract (4)**: {原語|げんご} (original / source language), {記録的|きろくてき} (record-breaking — na-adj), {皺寄|しわよ}せ (burden shifted onto others), {矛|ほこ} (spear — chiefly historical/idiomatic)
- **Animal / adjective (2)**: たてがみ (mane of a lion or horse), ぼろい (i-adj, shabby / worn out)

All 22 entries validate after a fix-up round: one romaji slip (`tatchisukuriin` → `tacchisukuriin`, since っち uses cch). One i-adjective (28785_boroi) and one suru verb (28790_tsuuringu) received full conjugation tables. No new kanji. Two unrelated false-positive add_conjugations.py modifications on adverb entries 05173/05175 were reverted before commit. Candidate list synced.

### 2026-06-05 (Vocabulary Expansion - 24 New Entries, "seen in entry" Batch)
Added 24 new dictionary entries (IDs 28747-28770) from `candidate_words.json`, drawn from "seen in entry" internal-completeness candidates referenced inside existing entries 05051-05246 (astronomy, traditional/Western music, sports, environment, plus a few onomatopoeia and one verb). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Astronomy / science (4)**: ブラックホール (black hole), {海王星|かいおうせい} (Neptune), {冥王星|めいおうせい} (Pluto, now dwarf planet), フロンガス (CFCs)
- **Society / abstract (3)**: {都市伝説|としでんせつ} (urban legend), {正義感|せいぎかん} (sense of justice), {世代間|せだいかん} (intergenerational)
- **Onomatopoeia / adverbs (3)**: てんでんばらばら (each going their own way, na-adj), ぐしゃぐしゃ (crumpled/soggy — 2 senses, 6 examples), ごろん (with a thud, single action)
- **Food / daily life (3)**: そうめん (thin wheat noodles), ワックス (wax — floor/car/hair), {河原|かわら} (riverbed/dry riverside area)
- **Traditional/Western music (5)**: {笙|しょう} (sho, gagaku mouth organ), {篠笛|しのぶえ} (shinobue bamboo flute), {洋楽器|ようがっき} (Western instruments — antonym link to 05231_wagakki), オペラ (opera), {重唱|じゅうしょう} (vocal ensemble)
- **Sports (5)**: リング (boxing/wrestling ring; ring shape — 2 senses, 6 examples), プロレス (pro wrestling), サーファー (surfer), サーフボード (surfboard), ダイバー (diver)
- **Verb (1)**: くたびれる (ichidan, to get tired/be worn out — 2 senses, 6 examples)

All 24 entries validate after a fix-up round: 2 invalid `domain: "traditional"` values cleared on the two traditional-instrument entries (28760, 28761); 1 bare-kanji furigana fix in 28755 explanation (raw 疲れる → {疲|つか}れる). One ichidan verb (28755_kutabireru) received its conjugation table. Two new kanji assigned readings and indexed: {笙|しょう} (ID 02766, gloss "sho") and {篠|しの} (ID 02767, gloss "bamboo"). One stale candidate removed during pre-flight (C21614 大規模/おおきぼ — incorrect reading; 大規模 is だいきぼ, already entry 12185). Candidate list synced (1581→1557).

### 2026-06-04 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch)
Added 25 new dictionary entries (IDs 28722-28746) from `candidate_words.json`, drawn from "seen in entry" internal-completeness candidates referenced inside existing entries 04918-05045. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Cooking ingredients / techniques (10)**: {本|ほん}みりん (true mirin), {回|まわ}しかける (to drizzle in a circular motion — ichidan), {太白|たいはく}ごま{油|あぶら} (unroasted sesame oil), {中力粉|ちゅうりきこ} (all-purpose flour), {揚|あ}がる (to be deep-fried — godan), {餡|あん}かけ (ankake sauce), {素|もと} (base/mix, e.g. だしの素), {天|てん}つゆ (tempura dipping sauce), {上新粉|じょうしんこ} (non-glutinous rice flour), ペッパー (pepper)
- **Wagashi (2)**: {練|ね}り{切|き}り (shaped white-bean-paste wagashi), {半生菓子|はんなまがし} (semi-dry wagashi)
- **Animals (4)**: コガネムシ (scarab beetle), ゲンゴロウ (diving beetle), {白鷺|しらさぎ} (white egret), {青鷺|あおさぎ} (grey heron)
- **Plants (3)**: {唐松|からまつ} (Japanese larch), {杜若|かきつばた} (rabbitear iris), {花菖蒲|はなしょうぶ} (Japanese iris)
- **Place / proper noun (2)**: {水戸|みと} (Mito city), インド (India)
- **Body part / idiom (4)**: {脚|あし} (leg, 2 senses: limb / furniture leg), {奮迅|ふんじん} (furious energy, in 獅子奮迅), {子|こ}{落|お}とし (tough love, in 獅子の子落とし), こやけ (afterglow, in 夕焼けこやけ)

All 25 entries validate after a fix-up round: 8 bare-kanji furigana slips in notes were annotated (e.g., 本みりん, 中力粉, 青鷺 と 白鷺, 四字熟語, 半生菓子, 練り切り, 花菖蒲, plus rice-flour terms). Two verbs (1 godan + 1 ichidan) received full conjugation tables. No new kanji. Three stale candidates removed during pre-flight (蝦蟇/がま duplicate of 28705_gama, 鰓/えら duplicate of 28708_era, 一頭/いっとう just 一+counter). Candidate list synced (1545→1517).

### 2026-06-04 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch)
Added 25 new dictionary entries (IDs 28697-28721) from `candidate_words.json`, drawn from "seen in entry" internal-completeness candidates referenced inside existing entries 04885-04949. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Loanwords / household (4)**: ドアホン (door phone), アクリル (acrylic), テラバイト (terabyte), ミリリットル (milliliter)
- **Animals / nature (7)**: {変温動物|へんおんどうぶつ} (cold-blooded animal), ガマ (toad), {山椒魚|さんしょううお} (salamander), おたまじゃくし (tadpole — 2 senses: animal + musical note), えら (gills), {淡水魚|たんすいぎょ} (freshwater fish), サバンナ (savanna)
- **Cooking / food (8)**: ふるい (sieve), とろみ (sauce thickness), {馬鈴薯|ばれいしょ} (formal: potato), エビフライ (fried shrimp), からし (Japanese mustard), シナモン (cinnamon), ししとう (shishito pepper), {竜田|たつた}{揚|あ}げ (tatsuta-age), {貫|かん} (sushi counter)
- **Plants (1)**: {松|まつ}ぼっくり (pine cone)
- **Verbs (2)**: {肥|こ}やす (godan, 3 senses: enrich soil / fatten livestock / 私腹を肥やす), {捕|と}る (godan, to catch a moving target)
- **Other (3)**: {小便|しょうべん} (urine — 2 senses incl. slang "backing out"), {何百|なんびゃく} (hundreds of — expression)

All 25 entries validate after a fix-up round: 3 invalid tag values corrected (`domain: science`/`computing` → `academic`/`technical`; `formality: casual` → `informal`); 4 bare-kanji furigana slips fixed in notes (五段, 百, 貫); romaji on {変温動物} corrected (hen-ondoubutsu → henondoubutsu, no hyphens allowed); headword on {竜田|たつた}{揚|あ}げ split into clean kanji-by-kanji pairs. Two godan verbs received full conjugation tables. No new kanji. Candidate list synced (1568→1545).

### 2026-06-04 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28675-28696) from `candidate_words.json`, all drawn from "seen in entry" internal-completeness candidates referenced inside existing entries 04939-05047. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Nature / scenery (6)**: {月夜|つきよ} (moonlit night), {流木|りゅうぼく} (driftwood), {良港|りょうこう} (good harbor), {石浜|いしはま} (pebble beach), {夕顔|ゆうがお} (moonflower / bottle gourd), {昼顔|ひるがお} (bindweed)
- **Plants / animals (4)**: {鈴虫|すずむし} (bell cricket), {葛|くず} (kudzu — 2 senses, plant + starch), もずく (mozuku seaweed), {小魚|こざかな} (small fish)
- **Health / medical (4)**: {歯周病|ししゅうびょう} (periodontal disease), {睡眠薬|すいみんやく} (sleeping pill), つわり (morning sickness), {重度|じゅうど} (severe degree)
- **Food / culture (5)**: {日本茶|にほんちゃ} (Japanese green tea), {茶漉|ちゃこ}し (tea strainer), {酢味噌|すみそ} (vinegar-miso dressing), {端午|たんご} (Tango Festival, May 5), {昆虫採集|こんちゅうさいしゅう} (insect collecting)
- **Verbs (2)**: {黄昏|たそが}れる (ichidan, 3 senses: dusk / decline / look pensive), {打|う}ち{寄|よ}せる (ichidan, waves wash up)
- **Other (1)**: {豆鉄砲|まめでっぽう} (peashooter — survives in idiom {鳩|はと}が{豆鉄砲|まめでっぽう}を{食|く}ったよう)

All 22 entries validate. Furigana fix-up round corrected ~11 bare-kanji slips in note/explanation prose (e.g., raw 暗くなる → {暗|くら}くなる, 鳩が豆鉄砲を食ったよう → fully annotated). Two ichidan verbs received full conjugation tables. No new kanji. Candidate list synced (1590→1568).

### 2026-06-03 (Vocabulary Expansion - 18 New Entries, Common Expressions Batch)
Added 18 new dictionary entries (IDs 28657-28674) from `candidate_words.json`, focusing on common expressions, particles, prefixes, and colloquial vocabulary that had accumulated as older candidates. One initial attempt at {超|ちょう}〜 was discarded mid-session as a duplicate of 28619 (created earlier the same day). Per-field budgets followed the reference shape of {もてなし} (27261) — short top-level glosses, notes scoped to 2-3 focused sections.

- **Prefixes / conjunctions (3)**: {既|き}〜 (pre-/already-), ましては (let alone — formal), 〜だけで (just by; merely from)
- **Adverbs / postpositions (2)**: {先|さき}に (first; earlier — 2 senses, 6 examples), {向|む}かって (facing; toward)
- **Expressions (5)**: やってしまう (to finish / to mess up — 2 senses, 6 examples), {山|やま}のよう (a mountain of), オチがつく (to come to a punchline), ぎこちなくなる (to turn awkward), {尾|お}ひれをつける (to embellish a story)
- **Casual / colloquial (4)**: おっしゃ (Alright! — masculine interjection), {腹|はら}{痛|いた}い (stomachache / so funny it hurts — 2 senses, 6 examples), どっちでもいい (either is fine — casual), どちらか (either one of two)
- **Verbs (2)**: {習|なら}い{慣|な}れる (ichidan, to grow accustomed through practice), {間抜|まぬ}ける (ichidan, to be silly / vacant-witted)
- **Nouns (2)**: うつむき{加減|かげん} (head slightly bowed), {癖字|くせじ} (idiosyncratic handwriting)

All 18 entries validate after a fix-up round: five `formality: "casual"` values corrected to `"informal"`; one romaji corrected (mashitewa → mashiteha for ましては); one furigana fix ({自分|じぶん} in 28663). Two ichidan verbs and one i-adjective received full conjugation tables. No new kanji. Eight stale candidates removed during pre-flight duplicate scan (七 suffix-duplicates plus 〜つつ, 注ぐ, 超 which already existed as 28619).

### 2026-06-03 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch)
Added 25 new dictionary entries (IDs 28631-28655) from `candidate_words.json`, drawn from "seen in entry" internal-completeness candidates referenced inside existing entries 04417-04856. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses, notes scoped to 2-3 focused sections.

- **Tech / loanwords (7)**: {実装|じっそう} (implementation, also suru), ブロードバンド, インスタントカメラ, コストパフォーマンス, {内課金|ないかきん} (in-app purchase), ハイパーインフレ, デフレーション
- **Sports / leisure (5)**: フットサル, フットボール, ホットヨガ, ヨガウェア, {打|う}ちっ{放|ぱな}し (2 senses: driving range / exposed concrete), {会員権|かいいんけん} (membership), {正捕手|せいほしゅ} (starting catcher)
- **Medical (3)**: {弁膜症|べんまくしょう} (valvular heart disease), {痴呆症|ちほうしょう} (old/offensive term for dementia), {見当識|けんとうしき} (orientation)
- **Economics / formal (3)**: {年利|ねんり} (annual interest rate), {恐慌|きょうこう} (depression / panic, 2 senses), {高層建|こうそうだ}て (high-rise building)
- **Philosophy / emotion (3)**: {虚無主義|きょむしゅぎ} (nihilism), {虚無的|きょむてき} (nihilistic, na-adj), {屈辱的|くつじょくてき} (humiliating, na-adj)
- **Verbs (2)**: {苛|さいな}む (godan, to torment), {脱|だっ}する (suru, to escape from)

All 25 entries validate. One romaji fix-up pre-build (yogauea → yogawea, since ウェ → we). Two `domain: ["computing"]` tags corrected to `"technical"`. Conjugation tables added to 2 verbs (1 godan + 1 suru) plus 28631_jissou's suru pattern. No new kanji. Candidate list synced (1560→1535).

### 2026-06-03 (Vocabulary Expansion - 19 New Entries, Internal-Completeness Batch)
Added 19 new entries (IDs 28612-28630) filling internal-completeness gaps — words that already appeared in other entries' examples or notes but lacked their own entries. Concise per-field budgets following {もてなし} (27261) shape.

- **People / appearance (3)**: {美女|びじょ}, {塩顔|しおがお}, {戦略家|せんりゃくか}
- **Tax / commerce suffixes (4)**: {込|こ}み, {税率|ぜいりつ}, {税別|ぜいべつ}, {超|ちょう}〜
- **Society / time (3)**: {現代的|げんだいてき}, {少子|しょうし}, {戦時中|せんじちゅう}
- **Chemistry (2)**: {酸|さん}, アルカリ
- **Onomatopoeia / sensation (5)**: むっつり, むっとする, ぷるぷる, ぷにぷに, ばさばさ
- **Verbs / adjectives (2)**: とろける, {未練|みれん}たらしい

Cross-references added between 酸 ↔ アルカリ, 税別 → 税込, 戦時中 ↔ 戦前/戦後, 現代的 ↔ 伝統的, 未練たらしい ↔ 未練がましい. Also removed 2 stale candidates (感, 士) that already existed as suffix entries.

### 2026-06-02 (Vocabulary Expansion - 24 New Entries, Everyday/Commerce Batch)
Added 24 new dictionary entries (IDs 28588-28611) from `candidate_words.json`. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264). Concise glosses, 2–3 note sections each.

- **Work and commerce (5)**: {教|おし}え{方|かた}, {月給制|げっきゅうせい}, {週給|しゅうきゅう}, {取締役会|とりしまりやくかい}, {義務化|ぎむか}
- **Clothing and household (5)**: {晴雨兼用|せいうけんよう}, {厚手|あつで}, {膝下|ひざした}, {伝線|でんせん}, {追|お}いかけっこ
- **Food (4)**: {無塩|むえん}, {有塩|ゆうえん}, スムージー, {七輪|しちりん}
- **Vehicles (4)**: ボンネット, ホイール, {前輪|ぜんりん}, {後輪|こうりん}
- **Other (6)**: {国際会議|こくさいかいぎ}, {有田焼|ありたやき}, ワイヤー, {予備軍|よびぐん} (2 senses), マウスパッド, {垂|た}れ{下|さ}がる (verb)

### 2026-06-02 (Vocabulary Expansion - 15 New Entries, "seen in entry" Batch)
Added 15 new dictionary entries (IDs 28573-28587) from `candidate_words.json`, covering all remaining "seen in entry" internal-completeness candidates (words already referenced inside existing entries 04535-04650 but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264).

- **Loanword nouns (4)**: グラサン (sunglasses, casual slang), ホットスポット (hotspot — biodiversity/Wi-Fi/figurative), スポットライト (spotlight, literal + figurative), 〜{感|かん} (sense/feel suffix)
- **Native nouns (8)**: {戦|いくさ} (war, classical/literary), {式|しき} (formula; ceremony — 2 senses, 6 examples), {古今|ここん} (all ages, literary), {東大|とうだい} (Tokyo University abbreviation), {来賓|らいひん} (guest of honor), {旅行中|りょこうちゅう} (during a trip), {地熱|ちねつ} (geothermal heat), {栄養分|えいようぶん} (nutrients), {種|しゅ} (species, biology)
- **Other (2)**: {躁鬱病|そううつびょう} (bipolar disorder), にほかならない (is nothing but — expression)

All 15 entries validate on first pass; one furigana fix-up ({躁|そう}/{鬱|うつ} in 28587's explanation). One new kanji ({躁|そう}, ID 02765, gloss "manic") assigned readings and indexed. Candidate list synced (1570→1556).

### 2026-06-02 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28551-28572) from `candidate_words.json`, drawn from "seen in entry" internal-completeness candidates in the C2141x-C2144x range (words referenced inside existing entries 04533-04632 but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Loanword nouns (7)**: ショール (shawl), ネックウォーマー (neck warmer, wasei-eigo), スマートウォッチ (smartwatch), チョーカー (choker), ライフル (rifle), スコア (score), タイムカード (time card)
- **Native nouns (8)**: {偏光|へんこう} (polarization), {内輪|うちわ} (insider/private), {上皇|じょうこう} (Emperor Emeritus), {打刻|だこく} (clock-in/out — also suru), {退職願|たいしょくねがい} (resignation request letter), {通行人|つうこうにん} (passerby), {老廃物|ろうはいぶつ} (metabolic waste), {檻|おり} (cage)
- **Verbs (5)**: {取|と}り{押|お}さえる (ichidan, to restrain/apprehend), {果|は}てる (ichidan, to come to an end — 2 senses), {閉|し}め{切|き}る (godan, to keep closed), {揺|ゆ}り{起|お}こす (godan, to shake awake), {知|し}らしめる (ichidan, to make widely known)
- **Adverbs (2)**: {頑|がん}として (stubbornly), {軽々|かるがる}と (effortlessly)

All 22 entries validate after a fix-up round: 28554 romaji corrected (sumaatowotchi→sumaatowocchi); two invalid domain tags fixed (physics→technical, medicine→medical); three furigana fixes ({対|たい}, {押|お}, {終|お}). Five verbs received conjugation tables. One new kanji ({檻|かん}/おり, ID 02764, gloss "cage") assigned readings and indexed. Candidate list synced (1592→1570).

### 2026-06-01 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28529-28550) from `candidate_words.json`, prioritizing "seen in entry" internal-completeness candidates (C21349-C21412) — words already referenced inside existing entries 04417-04524 but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Clothing/fabric (6)**: アイロンがけ (ironing — also suru-verb), シルク (silk), スウェット (sweatshirt/sweats), ブレザー (blazer), カットソー (cut-and-sewn knit top), フード (hood; food — 2 senses)
- **Tech/cameras (4)**: フェーズ (project phase), デジカメ (digital camera, casual abbrev), デジタルカメラ (digital camera), ビデオカメラ (video camera/camcorder), 写メ (phone photo, casual/dated)
- **Society/news (3)**: 外出先 (place when out), 行方不明者 (missing person), 警察犬 (police dog)
- **Health/medical (5)**: アルツハイマー (Alzheimer's), グループホーム (group home), 心電図 (ECG), 心不全 (heart failure), 狭心症 (angina)
- **Other (3)**: エース (ace — sports + card, 2 senses), 美術品 (work of art), 非常用 (for emergency use)

All 22 entries validate after a fix-up round: アイロンがけ romaji corrected (`aironkake` → `airongake`); three `formality: "casual"` values fixed to `"informal"`; one invalid `domain: ["news"]` cleared; one bare 和製 in カットソー notes given furigana. アイロンがけ received a suru conjugation table. No new kanji. Candidate list synced (1559→1537).

### 2026-06-01 (Vocabulary Expansion - 20 New Entries, "seen in entry" Batch)
Added 20 new dictionary entries (IDs 28509-28528) from `candidate_words.json`, all drawn from "seen in entry" internal-completeness candidates (C21381-C21405). These are words already referenced by existing entries 04462-04524 but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Nouns (16)**: フルーティスト (flutist), {義太夫|ぎだゆう} (gidayū chanting for bunraku), {長唄|ながうた} (nagauta shamisen genre), {虚無僧|こむそう} (komusō shakuhachi monk), フィルハーモニー (philharmonic), {器械体操|きかいたいそう} (artistic gymnastics), {泡立|あわだ}ち (lathering/foaming), {雑菌|ざっきん} (germs/bacteria), {打|う}ち{水|みず} (sprinkling water for cooling), {濡|ぬ}れ{縁|えん} (uncovered veranda), {老木|ろうぼく} (old tree), {御神木|ごしんぼく} (sacred shrine tree), シャワールーム (shower stall), バスローブ (bathrobe), {音姫|おとひめ} (toilet sound-masking device), {名手|めいしゅ} (master/virtuoso), {短編集|たんぺんしゅう} (short story collection)
- **Suru-verb nouns (2)**: {閉山|へいざん} (end of climbing season / mine closure, 2 senses, 6 examples), {洗浄|せんじょう} (washing/cleansing)
- **Godan verb (1)**: {切|き}り{倒|たお}す (to fell a tree)

All 20 entries validate; furigana fixed pre-build for two entries (吹禅 and 雑 in explanatory prose). Three verbs received full conjugation tables. One new kanji ({唄|うた}, ID 02763, gloss "song") assigned readings and indexed. Candidate list synced (1579→1559); one stale candidate (バスローブ with typo reading ばするおーぶ) removed before sync. Three traditional-arts entries (28510, 28511, 28512) had invalid `domain: ["traditional-arts"]` / `["history"]` tags corrected to `domain: []`.

### 2026-06-01 (Vocabulary Expansion - 24 New Entries, "seen in entry" Batch)
Added 24 new dictionary entries (IDs 28485-28508) from `candidate_words.json`, drawn from "seen in entry" internal-completeness candidates in the C2132x–C2138x range (words already referenced inside existing entries 04355, 04371, 04372, 04377-04395, 04457-04466 but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Nouns (21)**: {和暦|われき} (Japanese era calendar), {禁止令|きんしれい} (ban/prohibition order), {飛散量|ひさんりょう} (pollen dispersal amount), {無洗米|むせんまい} (no-wash rice), {銀杏|ぎんなん} (ginkgo nut, different reading from existing 04379_いちょう), {個人情報流出|こじんじょうほうりゅうしゅつ} (personal data leak), {白桃|はくとう} (white peach), {甘栗|あまぐり} (sweet roasted chestnuts), {毬栗|いがぐり} (chestnut burr / buzz cut — 2 senses), きんとん (sweetened chestnut paste), {芍薬|しゃくやく} (peony — herbaceous), {一箱|ひとはこ} (one box; also counter), {落語家|らくごか} (rakugo performer), コント (sketch comedy), {掛|か}け{合|あ}い (banter / call-and-response), {面白|おもしろ}さ (fun/appeal — さ-derived), ギタリスト (guitarist), {弾|ひ}き{語|がた}り (solo play-and-sing), ピッコロ (piccolo), リコーダー (recorder), {室内楽|しつないがく} (chamber music), ドラマー (drummer), {交響楽団|こうきょうがくだん} (symphony orchestra)
- **Adverb (1)**: ぴょんぴょん (hop-hop, mimetic)

All 24 entries validate; furigana clean (10 entries had bare-kanji references in notes — fixed pre-build); one formality value fixed (`casual` → `informal` on 28488). No verbs / i-adjectives. One new kanji ({芍|しゃく}, ID 02762, gloss "peony") assigned readings and indexed. Candidate list synced (1603→1579).

### 2026-05-31 (Vocabulary Expansion - 19 New Entries, "seen in entry" Batch)
Added 19 new dictionary entries (IDs 28466-28484) from `candidate_words.json`, drawn from "seen in entry" internal-completeness candidates in the C2064x–C2131x range. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 sections.

- **Suffixes (7)**: 〜{系|けい} (lineage/-type/-style), 〜{書|しょ} (document/written record), 〜{展|てん} (exhibition), 〜{間|かん} (duration of), 〜{引|び}き (off/discount of), 〜{史|し} (history of), 〜{編|へん} (volume/section)
- **Nouns (8)**: {平屋|ひらや}{建|だ}て (single-story house), {五階建|ごかいだ}て (five-story building), {十|じゅう}{人|にん} (ten people), {三猿|さんざる} (the three wise monkeys), {縁|へり} (edge/border/trim), {土地代|とちだい} (land price), {三文|さんもん} (three mon / a pittance), {致傷|ちしょう} (causing injury — legal)
- **Expression (1)**: じゃない (informal negative copula; tag question, 2 senses)
- **Verbs (2)**: {交|ま}ざる (intransitive godan, kanji variant of 02420 混ざる for mingling), {交|ま}ぜる (transitive ichidan, kanji variant of 02423 混ぜる)
- **Noun (1 katakana)**: オール (oar; all — 2 senses)

Also removed 5 stale candidates that already exist as entries (C20937 化→28335, C21039 年目→28359, C21176 純→28361, C21005 とお→28376, C20646 矢理 fragment). All 19 entries validate; furigana clean (one fix on 28482 致傷 notes pre-build); conjugation tables added to {交|ま}ざる and {交|ま}ぜる. No new kanji. Candidate list synced.

### 2026-05-31 (Vocabulary Expansion - 23 New Entries, "seen in entry" Batch)
Added 23 new dictionary entries (IDs 28443-28465) from `candidate_words.json`, drawn from the "seen in entry" internal-completeness candidates in the C2068x-C2131x range (words referenced inside existing entries 01763, 01767, 02000, 02216, 02220, 02228, 02594, 03716, 04066, 04209, 04210, 04215, 04227, 04229 but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Nouns (22)**: {杭|くい} (stake/pile/post), ゴルフボール (golf ball), {弁当屋|べんとうや} (bento shop), レプリカ (replica), {診断書|しんだんしょ} (medical certificate), {縁者|えんじゃ} (relatives/connections), {新案|しんあん} (new idea / utility model), {複文|ふくぶん} (complex sentence — grammar), {主文|しゅぶん} (main clause; operative part of ruling — 2 senses), {再販制度|さいはんせいど} (resale price maintenance system), {青竹|あおだけ} (green bamboo), {竹|たけ}ざお (bamboo pole), {日本製|にほんせい} (made in Japan), {中国製|ちゅうごくせい} (made in China), {金属製|きんぞくせい} (made of metal), {中央|ちゅうおう}アジア (Central Asia), {三倍|さんばい} (triple/threefold), {五日|いつか} (5th of month / five days — 2 senses), {西洋式|せいようしき} (Western-style), {日本式|にほんしき} (Japanese-style), {威|い} (authority/prestige — literary), {天|てん} (heaven/sky / Heaven as fate — 2 senses), {竹取|たけとり} (bamboo cutter)

Also removed 1 stale candidate (C21316 ひびわれる — kana variant of existing 28425 ひび{割|わ}れる). All 23 entries validate; furigana clean (four entries had missing furigana in notes — 28448 親戚/身内, 28453 竹, 28454 売り, 28460 何時 — fixed pre-build). No verbs/i-adjectives. One new kanji ({杭|くい}, ID 02761) assigned readings (kou/kui) and gloss (stake) and indexed. Candidate list synced.

### 2026-05-31 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28421-28442) from `candidate_words.json`, drawing primarily from the "seen in entry" internal-completeness candidates in the C21309–C21325 range plus a handful of recent unprocessed candidates. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Nouns (15)**: {多|おお}め (a bit more, also adjective-na), {恥|は}ずかしさ (embarrassment, さ-derived), ツボ (pressure point / key point, two senses), ハイヒール (high heels), {歩|ある}き{方|かた} (way of walking), {噛|か}み{合|あ}わせ (bite / gear meshing, two senses), {上巻|じょうかん} (first volume), {下巻|げかん} (second volume), {皮革|ひかく} (leather, formal), {参列者|さんれつしゃ} (ceremony attendee), スクリーンショット (screenshot), {出没|しゅつぼつ} (sudden appearances — also verb-suru), {卑怯者|ひきょうもの} (coward), {飲食物|いんしょくぶつ} (food and drink), {大部屋|おおべや} (large/shared room), {砂鉄|さてつ} (iron sand)
- **Verbs (6)**: {歪|ゆが}める (to distort, transitive ichidan), ひび{割|わ}れる (to crack, intransitive ichidan), {擦|こす}れる (to chafe/be worn, intransitive ichidan), ひそめる (to furrow brows, transitive ichidan), {描|か}く (to draw, transitive godan — colloquial reading of 描く, distinct from 02013 えがく), {波立|なみだ}つ (to ripple / be disturbed, intransitive godan, two senses)

All 22 entries validate; furigana clean (one missing furigana on 顰 in 28429 fixed pre-build); conjugation tables added to all 6 verbs. No new kanji. Candidate list synced (1581→1560).

### 2026-05-30 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch)
Added 25 new dictionary entries (IDs 28396-28420) from `candidate_words.json`, drawn from the "seen in entry" / "noentry in" internal-completeness candidates in the C20xxx-C21xxx range (words already referenced inside existing entries but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Nouns (12)**: {古人|こじん} (people of old / sages), {二軒隣|にけんどなり} (two doors down), {農学部|のうがくぶ} (faculty of agriculture), {百年|ひゃくねん} (a hundred years), {恐|おそ}ろしさ (fearfulness, さ-derived), {可愛|かわい}らしさ (cuteness, さ-derived), {日本文化|にほんぶんか} (Japanese culture), {術語|じゅつご} (technical term), {裏表紙|うらびょうし} (back cover), {法学|ほうがく} (jurisprudence), {戸外|こがい} (outdoors, literary), {犬種|いぬしゅ} (dog breed), {出生率|しゅっせいりつ} (birth rate), {非|ひ} (fault/wrong), {著述|ちょじゅつ} (writing/authorship — also verb-suru)
- **Expressions (4)**: うちに (while/before), につれて (as/in proportion to), ようになる (come to / become able to, 2 senses), そういうことで (well, that being the case), いらない (don't need, informal)
- **Adjective-na (1)**: {超巨大|ちょうきょだい} (super-huge)
- **Adjective-i (1)**: {大人|おとな}げない (childish, unbecoming of an adult)
- **Verbs (3)**: {論|ろん}ずる (to discuss, zuru-class), {読|よ}み{比|くら}べる (read and compare), {張|は}り{替|か}える (re-cover, re-paper)

Also removed 1 stale candidate (C21006 ぶり — already covered by 28358_buri). All 25 entries validate; furigana clean; conjugation tables added to verbs and i-adjective. No new kanji. Candidate list synced (1576→1550).

### 2026-05-30 (Vocabulary Expansion - 19 New Entries, "seen in entry" Batch)
Added 19 new dictionary entries (IDs 28377-28395) from `candidate_words.json`, fully working through the "seen in entry" internal-completeness candidates in the C0xxx block (words referenced inside existing entries 02615, 03179, and 04032-04193 but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 focused sections.

- **Nouns (17)**: {数十億円|すうじゅうおくえん} (several billion yen), {安定所|あんていじょ} (employment office / Hello Work), {死骸|しがい} (carcass), {整備士|せいびし} (licensed mechanic), {日本舞踊|にほんぶよう} (traditional Japanese dance), {数種類|すうしゅるい} (several kinds), {町中|まちじゅう} (throughout the town — contrasted with まちなか), {今月末|こんげつまつ} (end of this month), {惨事|さんじ} (catastrophe), カメラマン (photographer/cameraman, wasei-eigo), {感染者|かんせんしゃ} (infected person), {木工芸|もっこうげい} (woodcraft), {国有|こくゆう} (state-owned, noun + adjective-no), {角材|かくざい} (square lumber), {材木商|ざいもくしょう} (lumber merchant), {浅草|あさくさ} (Asakusa), {上野|うえの} (Ueno), {両国|りょうごく} (Ryōgoku)
- **Verb-godan (1)**: {降|ふ}りかかる (to fall onto / to befall — two senses, intransitive)

All 19 entries validate; furigana clean (one missing furigana on a section header in 28392 fixed pre-build); conjugation table added to {降|ふ}りかかる. No new kanji. Candidate list synced (1595→1576).

### 2026-05-29 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28355-28376) from `candidate_words.json`, drawn primarily from the "seen in entry" internal-completeness candidates in the C20xxx-C21xxx range. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 sections.

- **Nouns (12)**: {遊園|ゆうえん} (pleasure garden), {派|は} (faction/school), {対人|たいじん} (interpersonal), {無根|むこん} (groundless), {節回|ふしまわ}し (melodic style), {入賞者|にゅうしょうしゃ} (prize winner), {三密|さんみつ} (three Cs, COVID), {死火山|しかざん} (extinct volcano), {差損|さそん} (exchange loss), {色鉛筆|いろえんぴつ} (colored pencil), {睡眠時間|すいみんじかん} (sleep duration), ブロック{塀|べい} (concrete block wall), {石塀|いしべい} (stone wall)
- **Suffixes (3)**: 〜ぶり (first time in), 〜{年目|ねんめ} (Nth year), 〜{主義者|しゅぎしゃ} (-ist)
- **Prefix (1)**: {純|じゅん}〜 (pure/net)
- **Pronoun (1)**: いくつか (several)
- **Adverb (1)**: うっそうと (densely, of vegetation)
- **Number (1)**: {十|とお} (ten, native counting)
- **Verb-godan (1)**: {走|はし}り{切|き}る (run all the way through)
- **Verb-ichidan (1)**: {縛|しば}り{付|つ}ける (to tie down)

Also removed 6 stale candidates that already existed as entries (C20637 カセットテープ, C20955 性, C20988 全, C21120 賃, C21175 士, C21224 材 — covered by suffix/prefix entries 27932/28334/28337/28343/28352/28347). All 22 entries validate; furigana clean; conjugation tables added to the 2 verbs. No new kanji. Candidate list synced.

### 2026-05-29 (Vocabulary Expansion - 24 New Entries, Bound Morphemes & Grammar)
Added 24 new dictionary entries (IDs 28331-28354) from `candidate_words.json`, drawn from the "seen in entry" internal-completeness candidates. This batch focused on bound morphemes (productive suffixes/prefixes) and grammar expressions that the dictionary already referenced without defining. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264).

- **Suffixes (9)**: 〜{代|だい} (fee/bill), 〜{性|しょう} (personal disposition), 〜{化|か} (-ification), 〜{物|ぶつ} (object/substance), 〜{家|か} (expert/-ist), 〜{賃|ちん} (fare/wage), 〜{戦|せん} (match/tournament), 〜{材|ざい} (material/talent), 〜{士|し} (licensed professional)
- **Prefix (1)**: {全|ぜん}〜 (all/total)
- **Pronouns (3)**: {我|わ} (oneself, literary), {己|おのれ} (oneself, literary), {私|わたし}たち (we/us)
- **Expressions (4)**: ために (for the sake of / because of), だけに (precisely because), による (due to / by means of / according to), からこそ (precisely because)
- **Adverb (1)**: {誠|まこと}に (truly/sincerely, formal)
- **Particle (1)**: とも (both/all of a small group)
- **Nouns (4)**: {百戦|ひゃくせん} (a hundred battles, literary), {実|じつ} (real/biological, in 実の〜), {幸|さち} (blessing / mountain-sea bounty, two senses), {背景|はいけい} (background/context, two senses), {不能|ふのう} (impossibility/unable)

Also removed 4 stale candidates (C20642 カセットテープ, C21010 〜目, C21054 〜費, C21118 かしわで) that already existed as entries under variant readings or kanji forms.

### 2026-05-29 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28309-28330) from `candidate_words.json`, drawn from the "seen in entry" internal-completeness candidates in the C21xxx block (words already referenced inside existing entries). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (18)**: {温泉地|おんせんち} (hot spring resort area), くぐり{戸|ど} (low doorway/wicket door), {耳元|みみもと} (right next to the ear), {農耕|のうこう} (farming/agriculture), ダイヤル (dial — also verb-suru), {干|ほ}し{柿|がき} (dried persimmon), クリスマスツリー (Christmas tree), {血痕|けっこん} (bloodstain), {盗品|とうひん} (stolen goods, legal domain), {蕎麦殻|そばがら} (buckwheat hulls), {高枕|たかまくら} (high pillow / sleeping in peace — two senses), {紙垂|しで} (Shinto paper streamers), {変更線|へんこうせん} (International Date Line), {電磁場|でんじば} (electromagnetic field), {重力場|じゅうりょくば} (gravitational field), {指示器|しじき} (turn signal/indicator), {爆発音|ばくはつおん} (explosion sound), {銃声|じゅうせい} (gunshot), ばらつき (variation/scatter), {休火山|きゅうかざん} (dormant volcano)
- **Verb-godan (1)**: {売|う}りさばく (to sell off — transitive)
- **Expression (1)**: {抜|ぬ}け{目|め}がない (shrewd, not missing a trick)

All 22 entries validate; furigana clean; conjugation tables added to the godan verb and the suru-noun ダイヤル. No new kanji. Removed 1 stale candidate (タバコ, katakana variant of existing 02909_tabako). Candidate list synced (1626→1604).

### 2026-05-28 (Vocabulary Expansion - 20 New Entries, "seen in entry" Batch)
Added 20 new dictionary entries (IDs 28289-28308) from `candidate_words.json`, drawn from the "seen in entry" internal-completeness candidates. Length followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Verbs (6)**: {載|の}せる (kanji variant of 乗せる — load/publish), {延|の}ばす (kanji variant of 伸ばす — postpone/extend), {計|はか}る (measure time / plan), {量|はか}る (weigh / volume), {全否定|ぜんひてい}する (deny completely), {自己否定|じこひてい}する (self-denial)
- **Nouns (11)**: {荷|に} (load/burden), {禁|きん} (ban/prohibition), {乳|にゅう} (milk on'yomi), {米|べい} (US prefix), {中国|ちゅうごく} (China / Chugoku region), {永劫|えいごう} (eternity), そり (sled), {否定文|ひていぶん} (negative sentence), {保護活動|ほごかつどう} (conservation activities), {色紙|いろがみ} (craft paper), {帰|かえ}り{先|さき} (return destination)
- **Other (3)**: ロング (long-style modifier), {人的|じんてき} (na-adjective, personnel/human), かどうか (whether-or-not expression)

Many entries cross-reference existing same-kanji or homophone entries (e.g. 計る↔測る↔図る; 米べい↔米こめ; 色紙いろがみ↔色紙しきし).

### 2026-05-28 (Vocabulary Expansion - 23 New Entries, "seen in entry" Batch)
Added 23 new dictionary entries (IDs 28266-28288) from `candidate_words.json`, drawn from the "seen in entry" internal-completeness candidates in the C20xxx-C21xxx range (words already referenced inside existing entries but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (16)**: {十姉妹|じゅうしまつ} (society finch), {四年生|よねんせい} (fourth-year student), {琴棋書画|きんきしょが} (four classical arts), {首紐|くびひも} (neck strap), {右足|みぎあし} (right foot/leg), {家庭内|かていない} (within the home), {数百万円|すうひゃくまんえん} (several million yen), {五段|ごだん} (fifth dan / godan verb, 2 senses), LP (vinyl record), {男優|だんゆう} (male actor), {一丸|いちがん} (unity), {柏手|かしわで} (Shinto ritual clapping), {上|あ}げ{幅|はば} (range of increase), {爆発物|ばくはつぶつ} (explosives), イギリス (UK/Britain), {時制|じせい} (grammatical tense), {命令文|めいれいぶん} (imperative sentence), {希少種|きしょうしゅ} (rare species), {公案|こうあん} (Zen koan), {盆休|ぼんやす}み (Obon holidays)
- **Number (1)**: {千万|せんまん} (ten million)
- **Expression (1)**: {異存|いぞん}ない (no objection)
- **Prefix (1)**: サイバー (cyber-)

All 23 entries validate; furigana clean. No verbs/i-adjectives, no new kanji. Candidate list synced (1647→1624).

### 2026-05-28 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28244-28265) from `candidate_words.json`, drawn from the "seen in entry" internal-completeness candidates in the C21xxx block (words already referenced inside existing entries). Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): short top-level glosses (3-8 words), notes scoped to 2-3 sections.

- **Verb-ichidan (3)**: はぐれる (to get separated from), {赤|あか}らめる (to blush) — linked to intransitive pair {赤|あか}らむ (20843), {貼|は}り{合|あ}わせる (to paste together)
- **Verb-godan (4)**: {切|き}り{替|か}わる (to switch over) — linked to transitive pair {切|き}り{替|か}える (04239), とかす (to comb hair) — homophone link to {溶|と}かす (08264), {伝|つた}う (to run/flow along a surface), {蹴|け}り{込|こ}む (to kick into)
- **Na-adjectives (3)**: {聡明|そうめい} (wise/clear-headed), {厳正|げんせい} (strict/impartial), {涼|すず}しげ (cool-looking)
- **Adverbs (2)**: ふっくら (plump/soft), {余儀|よぎ}なく (unavoidably)
- **Nouns (10)**: {米粒|こめつぶ} (grain of rice), {虹色|にじいろ} (rainbow colors), {枕元|まくらもと} (bedside), {風呂釜|ふろがま} (bath heater), {杉林|すぎばやし} (cedar forest), {土俵入|どひょうい}り (sumo ring-entering ceremony), {招待客|しょうたいきゃく} (invited guest), {注射針|ちゅうしゃばり} (injection needle), {板塀|いたべい} (wooden fence), {危惧種|きぐしゅ} (endangered species)

All 22 entries validate; furigana clean; conjugation tables added to the 7 verbs. Reciprocal `prominent_see_also` back-links added to pair entries 04239 and 20843. One new kanji (聡, ID 02760) assigned readings/gloss and indexed. Candidate list synced (1669→1647).

### 2026-05-27 (Vocabulary Expansion - 20 New Entries)
Added 20 new dictionary entries (IDs 28224-28243) from `candidate_words.json`. No "seen in entry" candidates remained, so words were drawn from the older unprocessed list, skipping the heavy corpus noise (fragments, dubious compounds) in favor of clean, useful standalone vocabulary. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264): top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (13)**: {国防|こくぼう} (national defense), {審査員|しんさいん} (judge/examiner), {髪飾|かみかざ}り (hair ornament), {改札機|かいさつき} (ticket gate), {避難訓練|ひなんくんれん} (evacuation drill), {古典文学|こてんぶんがく} (classical literature), {流行歌|りゅうこうか} (popular song), {空想家|くうそうか} (dreamer), {抱|だ}き{合|あ}わせ (bundling/tie-in sale), {植生|しょくせい} (vegetation), {畜産業|ちくさんぎょう} (livestock industry), {命中率|めいちゅうりつ} (hit rate)
- **Noun+verb-suru (4)**: {減額|げんがく} (reduction in amount), {再評価|さいひょうか} (reevaluation), {発動|はつどう} (activation/invoking), {再審理|さいしんり} (retrial, legal)
- **Noun+adjective-no (1)**: {最優秀|さいゆうしゅう} (best/most excellent)
- **Verb-godan (1)**: {飲|の}み{尽|つ}くす (to drink up entirely)
- **Verb-ichidan (1)**: {書|か}き{忘|わす}れる (to forget to write)
- **Na-adjective (1)**: {夢想的|むそうてき} (dreamy/visionary)

All 20 entries validate; furigana clean; conjugation tables added to the 4 suru-verbs, the godan verb, and the ichidan verb. No new kanji. Candidate list synced.

### 2026-05-27 (Vocabulary Expansion - 25 New Entries)
Added 25 new dictionary entries (IDs 28199-28223) from `candidate_words.json`, drawn from the newest "seen in entry" candidates (words already referenced inside existing entries). The earlier candidate ranges are dominated by corpus noise; the recent C21xxx block is the cleanest source. Per-field budgets followed the reference shape of {もてなし} (27261): short top-level glosses, notes scoped to 2-3 sections.

- **Nouns (20)**: カエル (frog), {大敵|たいてき} (great enemy/nemesis), {働|はたら}き{盛|ざか}り (prime working years), {働|はたら}き{過|す}ぎ (overwork), {悪気|わるぎ} (ill will), パーマ (perm), {数年|すうねん} (several years), {振|ふ}り{幅|はば} (range of swing), {値幅|ねはば} (price range), {縫|ぬ}い{針|ばり} (sewing needle), {編|あ}み{針|ばり} (knitting needle), {釣|つ}り{針|ばり} (fishhook), {範囲外|はんいがい} (out of range/scope), {反省点|はんせいてん} (areas for improvement), {最多|さいた} (the most), {四|よ}つ{子|ご} (quadruplets), {持|も}ち{方|かた} (way of holding), {今年度|こんねんど} (this fiscal year), {来年度|らいねんど} (next fiscal year), {陸路|りくろ} (overland route), はやり (fad/trend)
- **Na-adjectives (2)**: {不順|ふじゅん} (unsettled/irregular), {悲劇的|ひげきてき} (tragic)
- **Noun+adjective-no (1)**: {放射性|ほうしゃせい} (radioactive)
- **Verb-ichidan (1)**: {振|ふ}り{切|き}れる (to go off the scale) — linked to its transitive pair {振|ふ}り{切|き}る (06703) with reciprocal `prominent_see_also`

All 25 entries validate; furigana clean; conjugation table added to the ichidan verb. No new kanji. Candidate list synced (1671→1646).

### 2026-05-27 (Vocabulary Expansion - 24 New Entries, "seen in entry" Batch)
Added 24 new dictionary entries (IDs 28175-28198) from `candidate_words.json`, drawn from the "seen in entry" internal-completeness candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261): top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (15)**: {宇宙飛行士|うちゅうひこうし} (astronaut), {宝石店|ほうせきてん} (jewelry store), {殺|ころ}し{文句|もんく} (killer line), {名場面|めいばめん} (famous scene), {人波|ひとなみ} (wave of people), {三|み}つ{子|ご} (triplets/three-year-old, 2 senses), {双生児|そうせいじ} (twins, formal), {利器|りき} (useful device), {方向性|ほうこうせい} (direction/orientation), {反省会|はんせいかい} (review meeting), {反抗心|はんこうしん} (rebellious spirit), {真犯人|しんはんにん} (real culprit), {白票|はくひょう} (blank/white ballot, 2 senses), {旅行先|りょこうさき} (travel destination), {風景画|ふうけいが} (landscape painting), {張力|ちょうりょく} (tension), {農法|のうほう} (farming method)
- **Na-adjectives (2)**: {凶悪|きょうあく} (atrocious/heinous), {奇跡的|きせきてき} (miraculous)
- **Noun+na-adjective (1)**: {不精|ぶしょう} (laziness/not bothering)
- **Verb-ichidan (1)**: かき{分|わ}ける (to push through a crowd)
- **Noun+verb-suru (3)**: {換金|かんきん} (conversion to cash), {廃絶|はいぜつ} (abolition/eradication), {家庭訪問|かていほうもん} (home visit by a teacher)

All 24 entries validate; furigana clean; conjugation tables added to the ichidan verb and 3 suru-verbs. No new kanji. Candidate list synced (1695→1671).

### 2026-05-26 (Vocabulary Expansion - 20 New Entries, "seen in entry" Batch)
Added 20 new dictionary entries (IDs 28155-28174) from `candidate_words.json`, drawn from the "seen in entry" internal-completeness candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261): top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (16)**: タオルハンカチ (towel handkerchief), ブラインドタッチ (touch typing), {薬学部|やくがくぶ} (faculty of pharmacy), {教育学部|きょういくがくぶ} (faculty of education), {特別区|とくべつく} (special ward), {便|びん} (flight/scheduled service), {過払|かはら}い{金|きん} (overpayment), {単位制|たんいせい} (credit system), {代金引換|だいきんひきかえ} (cash on delivery), {官房長官|かんぼうちょうかん} (Chief Cabinet Secretary), {外相|がいしょう} (Foreign Minister), {全校|ぜんこう} (whole school), {百円玉|ひゃくえんだま} (100-yen coin), {感動作|かんどうさく} (moving work), {業|ごう} (karma), {座|ざ} (seat/position)
- **Suffix (1)**: {料|りょう} (fee/charge; 手数料, 使用料)
- **Noun/suffix (1)**: {級|きゅう} (grade/rank)
- **Bound nouns (2)**: {不全|ふぜん} (failure/insufficiency; 心不全), {相乗|そうじょう} (synergy; 相乗効果)

All 20 entries validate; furigana clean (verify_furigana OK; find_missing_furigana's flag on the 代金引換 headword is a known false positive for set compounds with omitted okurigana). No verbs/i-adjectives, no new kanji. Removed 1 stale candidate (トナカイ, duplicate of 28135). Candidate list synced (1635→1614).

### 2026-05-26 (Vocabulary Expansion - 23 New Entries, "seen in entry" Batch)
Added 23 new dictionary entries (IDs 28132-28154) from `candidate_words.json`, drawn from the newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264); top-level glosses kept short, notes scoped to 2-3 sections.

- **Nouns (12)**: {籾殻|もみがら} (rice husk), {貝塚|かいづか} (shell mound), {横浜|よこはま} (Yokohama), {札幌|さっぽろ} (Sapporo), {自民党|じみんとう} (LDP), {青森県|あおもりけん} (Aomori Prefecture), オーストラリア (Australia), トナカイ (reindeer), ばあちゃん (granny), おとうちゃん (dad), {冷|ひ}や (cold water / room-temp sake), スプレッド (food spread), {大発見|だいはっけん} (great discovery)
- **Noun pair w/ antonym cross-refs**: {旧式|きゅうしき} (old-style) ↔ {新式|しんしき} (new-style)
- **Noun+verb-suru (1)**: ペイント (paint; ペイントする)
- **Noun/prefix (1)**: {万年|まんねん} (perpetual; 万年雪, 万年筆)
- **Pronoun (1)**: あたし (casual female "I")
- **Interjections (2)**: うーん (hmm), あっ (oh!/oops!)
- **Pre-noun adjectival (1)**: どういう (what kind of)
- **Expressions (2)**: ここだけ (just between us), おいくつ (how old?, polite)

All 23 entries validate; furigana check clean; conjugation table added to ペイント (suru). Two new kanji assigned IDs: 塚 (02758_chou_tsuka_mound), 幌 (02759_kou_horo_canopy). Candidate list synced.

### 2026-05-26 (Vocabulary Expansion - 20 New Entries, "seen in entry" Batch)
Added 20 new dictionary entries (IDs 28112-28131) from `candidate_words.json`, drawn from the newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (14)**: {満潮|みちしお} (high tide, native reading), {飛行機雲|ひこうきぐも} (contrail), {歯痛|しつう} (toothache), {部隊|ぶたい} (military unit), {弾|たま} (bullet/ammunition), {陽子|ようし} (proton), {中性子|ちゅうせいし} (neutron), {常習|じょうしゅう} (habitual practice), {賜物|たまもの} (gift/fruits of effort), {道端|みちばた} (roadside), {漢数字|かんすうじ} (kanji numerals), {初段|しょだん} (first dan), {華氏|かし} (Fahrenheit), {体育着|たいいくぎ} (gym clothes)
- **Verbs (5)**: {逝|い}く (to pass away, godan), かざす (to hold up/tap a card, godan), {決意|けつい}する (to resolve, suru), {語|かた}りかける (to speak to, ichidan), {入力|にゅうりょく}する (to input, suru)
- **Interjection (1)**: いざ (now; come on; いざという時)

All 20 entries validate; furigana check clean; conjugation tables added to the 5 verbs (逝く correctly received the irregular て-form 逝って). No new kanji needed. Removed 4 stale candidates (イルカ/クジラ/バラ duplicate existing kanji entries 海豚/鯨/薔薇; 気持ちよい duplicates 気持ちいい 09583). Candidate list synced (1681→1677).

### 2026-05-25 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 28090-28111) from `candidate_words.json`, drawn from the newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (17)**: {登竜門|とうりゅうもん} (gateway to success), {一等|いっとう} (first prize/class), エリート (elite), とんかつ (breaded pork cutlet), もも (thigh), {切|き}り{花|ばな} (cut flowers), {黒板|こくばん}{拭|ふ}き (blackboard eraser), {辛|つら}さ (hardship), {手玉|てだま} (beanbag; 手玉に取る), {筒|つつ} (tube/cylinder), お{湯|ゆ}{割|わ}り (drink with hot water), {眼|まなこ} (eye, literary), {腰紐|こしひも} (kimono waist cord), {国字|こくじ} (Japanese-made kanji), {地所|じしょ} (plot of land), {藺草|いぐさ} (rush for tatami), {四畳半|よじょうはん} (4.5-mat room), {玉|たま}{入|い}れ (ball-toss game), {五行|ごぎょう} (the five elements)
- **Pre-noun-adjectival (1)**: {明|あ}くる (the following/next)
- **Onomatopoeia/adverb (2)**: ぐーぐー (snoring soundly), ころっと (suddenly/completely)

Added one new kanji to the index: {藺|い} (02757). All 22 entries validate; furigana check clean; no verbs/i-adjectives needing conjugation tables. Removed 3 stale candidates (reading-format variants of words created this session). Candidate list synced (1674→1651).

### 2026-05-25 (Vocabulary Expansion - 21 New Entries)
Added 21 new dictionary entries (IDs 28069-28089) from `candidate_words.json`. No "seen in entry" candidates remained, so candidates were drawn from the older unprocessed list, skipping the many noisy fragments and dubious-gloss entries in favor of clean, useful words. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (14)**: ご{迷惑|めいわく} (trouble/inconvenience, polite), {速|はや}さ (speed), {話|はな}し{手|て} (speaker), ドイツ{語|ご} (German language), {老人|ろうじん}ホーム (nursing home), {介護|かいご}{施設|しせつ} (care facility), {推理|すいり}{小説|しょうせつ} (detective novel), {広告|こうこく}{代理店|だいりてん} (advertising agency), {昭和|しょうわ} (Showa era), {明治|めいじ}{時代|じだい} (Meiji period), {残|のこ}り{時間|じかん} (remaining time), つり{手|て} (train strap), {経過|けいか}{時間|じかん} (elapsed time), {飲|の}み{歩|ある}き (bar-hopping), {見送|みおく}り{人|にん} (well-wisher at a departure)
- **Noun + verb-suru (2)**: {立体視|りったいし} (stereoscopic vision), {経歴|けいれき}{詐称|さしょう} (resume fraud)
- **Adverb (1)**: {楽|らく}に (easily/comfortably)
- **Adjective-i (1)**: エロい (erotic/lewd, slang)
- **Expressions (2)**: チャックを{閉|し}める (to zip up), {見返|みかえ}りを{求|もと}める (to expect something in return)

Added one new kanji to the index: {昭|しょう} (02756). All 21 entries validate; furigana check clean; conjugation tables added to the 2 suru-verbs and 1 i-adjective. Candidate list synced (1695→1674).

### 2026-05-25 (Vocabulary Expansion - 24 New Entries, "seen in entry" Batch)
Added 24 new dictionary entries (IDs 28045-28068) from `candidate_words.json`, drawn from the newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261) and {埃|ほこり}まみれ (27264); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (16)**: {日本中|にほんじゅう} (all over Japan), {冷暖房|れいだんぼう} (climate control), {滑|すべ}り{出|だ}し (start/outset), {神経科|しんけいか} (neurology dept), {水物|みずもの} (matter of chance), {男児|だんじ} (male child), {商売人|しょうばいにん} (businessperson), {新薬|しんやく} (new drug), {女児|じょじ} (female child), ハローワーク (Hello Work), {夏場|なつば} (summertime), メリーゴーランド (carousel), テーマパーク (theme park), {思想家|しそうか} (thinker), {劇作家|げきさっか} (playwright), トレッキング (trekking), {一行|いっこう} (party/group), {立法権|りっぽうけん} (legislative power)
- **Noun/adjective-no (1)**: {無症状|むしょうじょう} (asymptomatic)
- **Na-adjectives (2)**: {誇大|こだい} (exaggerated), {尚早|しょうそう} (premature)
- **Verbs (3)**: {惑|まど}わす (to mislead — godan), {高|たか}ぶる (to get worked up — godan), {負傷|ふしょう}する (to be injured — suru)

Removed stale candidate (シミ, orthographic variant of existing {染|し}み, 05426). All 24 entries validate; furigana check clean; no new kanji; conjugation tables added to the 3 verbs. Candidate list synced.

### 2026-05-24 (Vocabulary Expansion - 22 New Entries)
Added 22 new dictionary entries (IDs 28023-28044) from `candidate_words.json`. No "seen in entry" candidates remained, so candidates were drawn from the older unprocessed list, skipping the many noisy fragments and dubious-gloss entries in favor of clean, useful words. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (19)**: ギリシャヨーグルト (Greek yogurt), インフルエンザワクチン (flu vaccine), タクシー{運転手|うんてんしゅ} (taxi driver), バイキング{形式|けいしき} (buffet style), エネルギー{資源|しげん} (energy resources), {必需物資|ひつじゅぶっし} (essential supplies), {先発隊|せんぱつたい} (advance party), {戦前派|せんぜんは} (prewar generation), クロロフィル (chlorophyll), {艦載機|かんさいき} (carrier-based aircraft), {幾何平均|きかへいきん} (geometric mean), {杖術|じょうじゅつ} (jojutsu/staff fighting), {窃視|せっし} (voyeurism), {横断面|おうだんめん} (cross section), {美肌効果|びはだこうか} (skin-beautifying effect), {美白剤|びはくざい} (skin-whitening agent), {発生頻度|はっせいひんど} (frequency of occurrence), {通算成績|つうさんせいせき} (career stats), {燃料油|ねんりょうゆ} (fuel oil)
- **Expressions (3)**: {一瞬|いっしゅん}で (in an instant), {遠|とお}い{将来|しょうらい} (the distant future), つい{昨日|きのう} (just yesterday)

All 22 entries validate; furigana check clean; no new kanji; no verbs/i-adjectives needing conjugation tables. Candidate list synced.

### 2026-05-24 (Vocabulary Expansion - 23 New Entries, "seen in entry" Batch)
Added 23 new dictionary entries (IDs 28000-28022) from `candidate_words.json`, drawn from the newest candidates (most flagged "seen in entry" — words already referenced inside existing entries but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (21)**: {食事券|しょくじけん} (meal voucher), {旅行券|りょこうけん} (travel voucher), {赤旗|あかはた} (red flag), {犬猿|けんえん} (dog and monkey — bitter enemies), {赤土|あかつち} (red clay/soil), {足長蜂|あしながばち} (paper wasp), かゆみ{止|ど}め (anti-itch medicine), {母性愛|ぼせいあい} (maternal love), インスタ (Instagram), {脇芽|わきめ} (side shoot), {絵描|えか}き (painter), {閉所|へいしょ} (enclosed space), {梵鐘|ぼんしょう} (temple bell), {軽度|けいど} (mild — noun/adjective-no), {煙霧|えんむ} (haze/smog), {公用|こうよう} (official use), {国語力|こくごりょく} (Japanese language ability), {会期|かいき} (legislative session), {最中|もなか} (monaka sweet), {白地図|はくちず} (blank map), {自由研究|じゆうけんきゅう} (independent study project)
- **Noun + verb-suru (2)**: {授受|じゅじゅ} (giving and receiving), {全治|ぜんち} (complete recovery)

Removed stale candidate C20998 ({農作物|のうさくもつ}), a variant-reading duplicate of the existing entry {農作物|のうさくぶつ} (15271). Added one new kanji to the index: {梵|ぼん} (02755). All 23 entries validate; furigana check clean (no verbs/i-adjectives needing conjugation tables). Candidate list synced (1729→1705).

### 2026-05-24 (Vocabulary Expansion - 24 New Entries)
Added 24 new dictionary entries (IDs 27976-27999) from `candidate_words.json`, drawn from the newest candidates (many flagged "seen in entry" — words already referenced inside existing entries but not yet defined). Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (17)**: {天国|てんごく} (heaven/paradise), {半日|はんにち} (half a day), {生姜焼|しょうがや}き (ginger pork), エキスパート (expert), {空域|くういき} (airspace), {海沿|うみぞ}い (along the coast), {冊数|さっすう} (number of books), {毎週末|まいしゅうまつ} (every weekend), {一昨夜|いっさくや} (the night before last), {都立|とりつ} (metropolitan-run), {夫婦喧嘩|ふうふげんか} (marital quarrel), {将校|しょうこう} (military officer), {自衛官|じえいかん} (SDF member), {私事|わたくしごと} (private matter), ディナー (dinner), {平方|へいほう} (square), {筆|ふで}ペン (brush pen)
- **Counter (1)**: {坪|つぼ} (tsubo, unit of area ~3.3 m²)
- **Na-adjective (1)**: {遅|おそ}め (somewhat late)
- **Pre-noun adjectival (1)**: {見知|みし}らぬ (unfamiliar/unknown)
- **Verbs (4)**: {降|ふ}り{止|や}む (to stop raining, godan, intransitive), ぎょっとする (to be startled, suru), {更新|こうしん}する (to update/renew/break a record, suru), {着火|ちゃっか}する (to ignite, suru)

Added one new kanji to the index: {坪|つぼ} (02754). All 24 entries validate; furigana check clean; conjugations added to the four verbs. Candidate list synced (1753→1729).

### 2026-05-23 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch — third run)
Added 22 new dictionary entries (IDs 27954-27975) from `candidate_words.json`, drawn from "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (21)**: ヘアブラシ (hairbrush), スポーツタオル (sports towel), ユーロ (euro), ポンド (British pound / pound weight — two senses), キャスター (newscaster / caster — two senses), レポーター (on-scene reporter), コメンテーター (commentator), ナレーター (narrator), {単車|たんしゃ} (motorcycle), {企画案|きかくあん} (project proposal), {改善案|かいぜんあん} (improvement proposal), キャリーバッグ (wheeled bag), ハンバーガー (hamburger), {飽|あ}き{飽|あ}き (being fed up, noun + verb-suru), {籾|もみ} (unhulled rice), {水稲|すいとう} (paddy rice), {鋤|すき} (spade/plow), スーパーコンピュータ (supercomputer), グラフィックス (graphics), {商学部|しょうがくぶ} (faculty of commerce), {二人乗|ふたりの}り (riding double)
- **Verb (1)**: {怒|いか}る (to be angry — literary reading of 怒る, godan, intransitive)

Removed stale candidate C20687 (細工 ざいく), a typo-reading duplicate of the existing entry {細工|さいく} (13790). Added two new kanji to the index: {籾|もみ} (02752) and {鋤|すき} (02753). All 22 entries validate; furigana check clean; conjugations added to {怒|いか}る and {飽|あ}き{飽|あ}きする.

### 2026-05-23 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch — later run)
Added 25 new dictionary entries (IDs 27929-27953) from `candidate_words.json`, drawn from "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (23)**: サービス{料|りょう} (service charge), ハンドタオル (hand towel), セロテープ (cellophane tape), カセットテープ (cassette tape), マスキングテープ (masking/washi tape), ケーブルテレビ (cable TV), {薄型|うすがた}テレビ (flat-screen TV), {園長|えんちょう} (kindergarten principal), {文鳥|ぶんちょう} (Java sparrow), {作|つく}り{方|かた} (way of making), {柔道着|じゅうどうぎ} (judo uniform), ステーション (station/hub), {治療法|ちりょうほう} (treatment method), {報知器|ほうちき} (alarm device), {犬|いぬ}かき (dog paddle), {善玉|ぜんだま} (good guy / good bacteria — two senses), {悪玉|あくだま} (bad guy / bad bacteria — two senses), {貸|か}し{借|か}り (lending and borrowing), {生殖|せいしょく} (reproduction), {計算式|けいさんしき} (calculation formula), {投票権|とうひょうけん} (right to vote), {歴史劇|れきしげき} (historical drama), ギプス (plaster cast), {探検家|たんけんか} (explorer)
- **Verb (1)**: {合格|ごうかく}する (to pass an exam, verb-suru, intransitive)

No new kanji introduced. All 25 entries validate; furigana check clean; conjugation added to {合格|ごうかく}する.

### 2026-05-23 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 27907-27928) from `candidate_words.json`, drawn from "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short (3-8 words), notes scoped to 2-3 sections.

- **Nouns (21)**: ソフトドリンク (soft drink), ソフトボール (softball), ブルーベリー (blueberry), あんず (apricot), カフェイン (caffeine), {子牛|こうし} (calf), {渦巻|うずま}き (spiral/swirl), {渦潮|うずしお} (tidal whirlpool), {雑木林|ぞうきばやし} (mixed-tree thicket), {松林|まつばやし} (pine grove), {科学館|かがくかん} (science museum), {喫煙者|きつえんしゃ} (smoker), {創造力|そうぞうりょく} (creativity), {鵜飼|うか}い (cormorant fishing), はとこ (second cousin), {美|うつく}しさ (beauty), ゴシップ (gossip), りんご{狩|が}り (apple picking), {弱|よわ}さ (weakness), {幼|おさな}さ (childishness/youthfulness), カナリア (canary)
- **Verb (1)**: ぬかる (to become muddy, godan, intransitive)

Removed stale candidate C20695 (親父), a kanji variant of the existing kana entry おやじ (10249). No new kanji introduced. All 22 entries validate; furigana check clean; conjugation added to ぬかる.

### 2026-05-22 (Vocabulary Expansion - 25 New Entries, "seen in entry" Batch)
Added 25 new dictionary entries (IDs 27882-27906) from `candidate_words.json`, drawn from the newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Verbs (9)**: {載|の}る (to appear in print, godan, intransitive), {患|わずら}う (to suffer from illness, godan, transitive), {転|ころ}げる (to roll/tumble, ichidan, intransitive), {断|た}つ (to sever/cut off, godan, transitive), {押|お}し{迫|せま}る (to be imminent, godan, intransitive), {害|がい}する (to harm, verb-suru, transitive), {煙|けむ}たがる (to find bothersome, godan, transitive), {挙|あ}げる (to cite / hold a ceremony — two senses, ichidan, transitive), {指摘|してき}する (to point out, verb-suru, transitive)
- **Nouns (15)**: {因習|いんしゅう} (old custom), {金塊|きんかい} (gold bar), {安息|あんそく} (rest/repose), {遭難者|そうなんしゃ} (person in distress), {助教|じょきょう} (assistant professor), {源|みなもと} (source/origin), {労使|ろうし} (labor and management), {議場|ぎじょう} (assembly chamber), {大腸|だいちょう} (large intestine), {乳酸|にゅうさん} (lactic acid), {透析|とうせき} (dialysis, noun + verb-suru), {民事|みんじ} (civil law/affairs), コンビ (duo/pair), {出納|すいとう} (receipts and disbursements), {縞|しま} (stripes)
- **Adverb (1)**: {常々|つねづね} (always/habitually)

No new kanji introduced. All 25 entries validate; furigana check clean; conjugations added to the 10 verb forms (5 godan, 2 ichidan, 3 suru).

### 2026-05-21 (Vocabulary Expansion - 24 New Entries, "seen in entry" Batch — second run)
Added 24 new dictionary entries (IDs 27858-27881) from `candidate_words.json`, drawn from the newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Nouns (18)**: ルーキー (rookie), ロープ (rope), {暴行|ぼうこう} (assault, noun + verb-suru), シャボン{玉|だま} (soap bubble), {蒸|む}し{焼|や}き (steam-baking), {瞳孔|どうこう} (pupil of the eye), {小判|こばん} (Edo gold coin), {黒猫|くろねこ} (black cat), {寅年|とらどし} (Year of the Tiger), {隼|はやぶさ} (peregrine falcon), {鳶|とび} (black kite), {鷹狩|たかが}り (falconry), {日本猿|にほんざる} (Japanese macaque), {桐|きり} (paulownia), {現代詩|げんだいし} (modern poetry), モップ (mop), {栄養学|えいようがく} (nutrition science), {満面|まんめん} (the whole face / beaming)
- **Adjectives (2)**: ぐうたら (lazy, na-adj + noun), {機械的|きかいてき} (mechanical/perfunctory, na-adj)
- **Verb (1)**: {梳|と}く (to comb hair, godan, transitive)
- **Adverb (1)**: {虎視眈々|こしたんたん} (watching vigilantly for a chance, four-character idiom)
- **Expressions (2)**: こんばんは (good evening), ようこそ (welcome)

Five new kanji introduced: {寅|とら} (02747), {桐|きり} (02748), {眈|たん} (02749), {隼|はやぶさ} (02750), {鳶|とび} (02751). All 24 entries validate; furigana check clean; conjugations added to {梳|と}く and {暴行|ぼうこう}する.

### 2026-05-21 (Vocabulary Expansion - 24 New Entries, "seen in entry" Batch)
Added 24 new dictionary entries (IDs 27834-27857) from `candidate_words.json`, all newest "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Verbs (9)**: {雇|やと}い{入|い}れる (to hire, ichidan, transitive), {譲|ゆず}り{合|あ}う (to yield mutually, godan, transitive), {割|わ}り{切|き}れる (to be divisible / settle one's feelings — two senses, ichidan, intransitive), {満|み}ち{足|た}りる (to be content, ichidan, intransitive), {惹|ひ}く (to attract, godan, transitive), {修|おさ}める (to study/master, ichidan, transitive), {詰|つ}む (to be cornered/checkmated, godan, intransitive), {講|こう}じる (to take measures, ichidan, transitive), {混|ま}ぜ{合|あ}わせる (to blend, ichidan, transitive)
- **Adjectives (4)**: {妬|ねた}ましい (enviably galling, i-adj), {物凄|ものすご}い (tremendous, i-adj), {悩|なや}ましい (vexing/seductive — two senses, i-adj), {温和|おんわ} (gentle/mild, na-adj)
- **Nouns (11)**: {離|はな}れ{離|ばな}れ (separated), クラクション (car horn), {町外|まちはず}れ (outskirts of town), {違反者|いはんしゃ} (offender), {災|わざわ}い (disaster/misfortune), {靴磨|くつみが}き (shoeshine), {西日|にしび} (afternoon sun), ゆりかご (cradle), {体当|たいあ}たり (body slam / all-out effort — two senses, noun + verb-suru), {蛍狩|ほたるが}り (firefly viewing), {温泉|おんせん}{卵|たまご} (onsen egg)

One new kanji introduced: {惹|ひ} (attract), assigned kanji ID 02746. All 24 entries validate; furigana check clean; conjugations added to the 9 verbs, the verb-suru noun, and the 3 i-adjectives.

### 2026-05-19 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch)
Added 22 new dictionary entries (IDs 27812-27833) from `candidate_words.json`, all "seen in entry" candidates — words already referenced inside existing entries but not yet defined. Per-field budgets followed the reference shape of {もてなし} (27261); top-level glosses kept short, notes scoped to 2-3 sections.

- **Nouns (18)**: {民放|みんぽう} (commercial broadcasting), {夕|ゆう}ご{飯|はん} (dinner), {濁点|だくてん} (voicing mark), {詩歌|しいか} (poetry), {巣窟|そうくつ} (den/hideout), {貝柱|かいばしら} (scallop adductor muscle), {県庁|けんちょう} (prefectural government office), {県内|けんない} (within the prefecture), {新札|しんさつ} (crisp banknote), {水牛|すいぎゅう} (water buffalo), {本箱|ほんばこ} (bookcase), {肩幅|かたはば} (shoulder width), {良|よ}さ (goodness/merit), {洋酒|ようしゅ} (Western liquor), {猿真似|さるまね} (blind imitation), {山里|やまざと} (mountain village), {袖丈|そでたけ} (sleeve length), {竹刀|しない} (bamboo sword)
- **Verbs (4)**: {言|い}い{尽|つ}くす (to express fully, godan, transitive), {使|つか}い{尽|つ}くす (to use up completely, godan, transitive), {薦|すす}める (to recommend, ichidan, transitive), {煎|せん}じる (to decoct herbs, ichidan, transitive)

No new kanji introduced. All 22 entries validate; furigana check clean; conjugations added to the 4 verbs.

### 2026-05-19 (Vocabulary Expansion - 22 New Entries, "seen in entry" Batch — earlier run)
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
