# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-04
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
| Total entries | ~14,924 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,125 (open) |
| Candidate words | ~4,846 |
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

### 2026-03-04 (Vocabulary Expansion - 30 New Entries, Session 369)
Added 30 new dictionary entries (IDs 14839-14868) from candidate_words.json:

- **Noun/suru verbs (7)**: {調整|ちょうせい} (adjustment), {匹敵|ひってき} (rivaling), {検問|けんもん} (checkpoint), {強制終了|きょうせいしゅうりょう} (force quit), {記名|きめい} (signing one's name), {上告|じょうこく} (final appeal), {近縁|きんえん} (closely related)
- **Nouns (14)**: {就職活動|しゅうしょくかつどう} (job hunting), {魔物|まもの} (demon/monster), {光沢|こうたく} (luster), {港町|みなとまち} (port town), {大型連休|おおがたれんきゅう} (long holiday), {通行料|つうこうりょう} (toll), {甘酢|あまず} (sweet vinegar), {固体|こたい} (solid), {人口密度|じんこうみつど} (population density), {車間距離|しゃかんきょり} (following distance), {領主|りょうしゅ} (feudal lord), {領地|りょうち} (territory), {演台|えんだい} (podium), {霊場|れいじょう} (sacred site)
- **Godan verbs (2)**: {香|かお}る (to smell sweet), {取次|とりつ}ぐ (to relay/transfer)
- **Ichidan verb (1)**: {避|よ}ける (to dodge)
- **Na-adjective/noun (2)**: {完全無欠|かんぜんむけつ} (absolute perfection), {高|たか}め (on the high side)
- **Noun (cultural) (3)**: {春夏秋冬|しゅんかしゅうとう} (four seasons), {大和言葉|やまとことば} (native Japanese words), {皇位|こうい} (imperial throne)
- **Noun (academic) (1)**: {音韻|おんいん} (phonology)

Notable features:
- Multi-sense entries: {魔物|まもの} (2: monster + jinx), {取次|とりつ}ぐ (2: relay + transfer call), {近縁|きんえん} (2: biological + familial), {音韻|おんいん} (2: phonology + phoneme)
- Daily life: {調整|ちょうせい}, {就職活動|しゅうしょくかつどう}, {大型連休|おおがたれんきゅう}, {車間距離|しゃかんきょり}, {通行料|つうこうりょう}
- Food: {甘酢|あまず}
- Science: {固体|こたい}, {人口密度|じんこうみつど}
- Culture/history: {領主|りょうしゅ}, {領地|りょうち}, {皇位|こうい}, {霊場|れいじょう}, {春夏秋冬|しゅんかしゅうとう}
- Business: {取次|とりつ}ぐ, {記名|きめい}, {演台|えんだい}

Total entries: 14,894 → 14,924 (approximate)
Remaining candidates: 4,876 → 4,846 (30 removed)

### 2026-03-04 (Vocabulary Expansion - 30 New Entries, Session 368)
Added 30 new dictionary entries (IDs 14809-14838) from candidate_words.json:

- **Nouns (16)**: {英会話|えいかいわ} (English conversation), {目盛|めも}り (scale/graduation), {行商人|ぎょうしょうにん} (peddler), {聞|き}き{書|が}き (oral history transcript), {藻|も} (algae), {葦|あし} (reed), {身辺|しんぺん} (one's surroundings), {自筆|じひつ} (handwriting), {青果|せいか} (fresh produce), {精肉|せいにく} (butchered meat), {長|なが}ねぎ (green onion), {予約席|よやくせき} (reserved seat), {雪見|ゆきみ} (snow viewing), {雛人形|ひなにんぎょう} (hina dolls), {見取|みと}り{図|ず} (floor plan), {断面図|だんめんず} (cross-section)
- **Noun/suru verbs (8)**: {渡米|とべい} (going to America), {周回|しゅうかい} (lap/circuit), {摩耗|まもう} (wear and tear), {休戦|きゅうせん} (ceasefire), {開戦|かいせん} (outbreak of war), {潜水|せんすい} (diving), {水分補給|すいぶんほきゅう} (hydration), {位置情報|いちじょうほう} (location data)
- **Ichidan verb (1)**: {照|て}らし{合|あ}わせる (to check against)
- **Godan verb (1)**: {討|う}つ (to strike down)
- **Na-adjective/noun (1)**: {無関係|むかんけい} (unrelated)
- **Compound nouns (3)**: {得意分野|とくいぶんや} (area of expertise), {連帯責任|れんたいせきにん} (collective responsibility), {過激派|かげきは} (extremists)

Notable features:
- Multi-sense entries: {英会話|えいかいわ} (2: conversation + classes), {周回|しゅうかい} (2: lap + touring), {討|う}つ (2: slay + subjugate)
- Daily life: {水分補給|すいぶんほきゅう}, {予約席|よやくせき}, {長|なが}ねぎ, {目盛|めも}り, {位置情報|いちじょうほう}
- Supermarket: {青果|せいか}, {精肉|せいにく}
- Culture: {雪見|ゆきみ}, {雛人形|ひなにんぎょう}, {葦|あし}, {聞|き}き{書|が}き
- Military/history: {休戦|きゅうせん}, {開戦|かいせん}, {討|う}つ, {過激派|かげきは}
- Technical: {断面図|だんめんず}, {見取|みと}り{図|ず}, {摩耗|まもう}
- New kanji: 2,497 → 2,498 ({葦|い})

Total entries: 14,864 → 14,894 (approximate)
Remaining candidates: 4,906 → 4,876 (30 removed)

### 2026-03-03 (Vocabulary Expansion - 30 New Entries, Session 367)
Added 30 new dictionary entries (IDs 14779-14808) from candidate_words.json:

- **Nouns (14)**: {道連|みちづ}れ (traveling companion), {縁結|えんむす}び (matchmaking), {面識|めんしき} (acquaintance), {挽肉|ひきにく} (ground meat), {身振|みぶ}り (gesture), {欠員|けついん} (vacancy), {先代|せんだい} (predecessor), {長電話|ながでんわ} (long phone call), {重役|じゅうやく} (executive), {空室|くうしつ} (vacant room), {慰謝料|いしゃりょう} (consolation money), {野菜炒|やさいいた}め (stir-fried vegetables), {鍋物|なべもの} (hot pot), {設計図|せっけいず} (blueprint)
- **Noun/suru verbs (8)**: {矯正|きょうせい} (correction), {丸暗記|まるあんき} (rote memorization), {深酒|ふかざけ} (heavy drinking), {転送|てんそう} (forwarding), {報復|ほうふく} (retaliation), {暗唱|あんしょう} (recitation), {釈放|しゃくほう} (release), {世襲|せしゅう} (hereditary succession)
- **I-adjective (1)**: {嘆|なげ}かわしい (deplorable)
- **Na-adjective (1)**: {潜在的|せんざいてき} (potential/latent)
- **Adverb (1)**: {格段|かくだん}に (remarkably)
- **Noun (weather) (1)**: {高気圧|こうきあつ} (high atmospheric pressure)
- **Ichidan verb (1)**: {迎|むか}え{入|い}れる (to welcome in)
- **Godan verbs (2)**: {食|く}い{下|さ}がる (to persist), {立|た}ちくらみ (dizziness upon standing)

Notable features:
- Multi-sense entries: {道連|みちづ}れ (2: companion + dragging down), {迎|むか}え{入|い}れる (compound verb)
- Daily life: {挽肉|ひきにく}, {野菜炒|やさいいた}め, {鍋物|なべもの}, {立|た}ちくらみ, {長電話|ながでんわ}, {空室|くうしつ}
- Legal/formal: {慰謝料|いしゃりょう}, {釈放|しゃくほう}, {報復|ほうふく}, {面識|めんしき}
- Business: {重役|じゅうやく}, {欠員|けついん}, {転送|てんそう}, {設計図|せっけいず}
- Education: {丸暗記|まるあんき}, {暗唱|あんしょう}, {矯正|きょうせい}
- Culture: {縁結|えんむす}び, {鍋物|なべもの}, {世襲|せしゅう}
- New kanji: 2,496 → 2,497 ({矯|きょう})

Total entries: 14,834 → 14,864 (approximate)
Remaining candidates: 4,936 → 4,906 (30 removed)

### 2026-03-03 (Vocabulary Expansion - 30 New Entries, Session 366)
Added 30 new dictionary entries (IDs 14749-14778) from candidate_words.json:

- **Nouns (13)**: {囃子|はやし} (musical accompaniment), {妃|きさき} (empress consort), {具体例|ぐたいれい} (concrete example), {保冷剤|ほれいざい} (ice pack), {色紙|しきし} (autograph board), {港湾|こうわん} (harbor), {魔王|まおう} (demon king), {酒粕|さけかす} (sake lees), {領事館|りょうじかん} (consulate), {外交官|がいこうかん} (diplomat), {招待状|しょうたいじょう} (invitation), {鉄製|てっせい} (made of iron), {身辺|しんぺん} (around oneself)
- **Noun/suru verbs (7)**: {白眼視|はくがんし} (scorn), {遷都|せんと} (capital transfer), {祝賀|しゅくが} (celebration), {入港|にゅうこう} (port entry), {割愛|かつあい} (omitting), {鎮座|ちんざ} (enshrinement), {風靡|ふうび} (sweeping popularity)
- **Na-adjectives (5)**: {荘厳|そうごん} (solemn/sublime), {厳粛|げんしゅく} (grave/solemn), {高尚|こうしょう} (noble/refined), {限定的|げんていてき} (limited), {網羅的|もうらてき} (exhaustive)
- **Noun/na-adjective (1)**: {非道|ひどう} (inhumane)
- **Noun/suru verb (2)**: {現状維持|げんじょういじ} (status quo), {逢瀬|おうせ} (tryst)
- **Ichidan verb (1)**: {盛|も}り{付|つ}ける (to plate food)
- **Noun (ceremony) (1)**: {祝辞|しゅくじ} (congratulatory speech)

Notable features:
- Multi-sense entries: {鎮座|ちんざ} (2: enshrinement + sitting imposingly)
- Paired entries: {荘厳|そうごん}/{厳粛|げんしゅく}, {限定的|げんていてき}/{網羅的|もうらてき}, {領事館|りょうじかん}/{外交官|がいこうかん}
- Cultural: {囃子|はやし}, {妃|きさき}, {逢瀬|おうせ}, {色紙|しきし}, {酒粕|さけかす}, {魔王|まおう}
- Formal/academic: {白眼視|はくがんし}, {遷都|せんと}, {割愛|かつあい}, {風靡|ふうび}, {高尚|こうしょう}
- New kanji: 2,493 → 2,496 ({囃|そう}, {逢|ほう}, {靡|ひ})

Total entries: 14,804 → 14,834 (approximate)
Remaining candidates: 4,966 → 4,936 (30 removed)

### 2026-03-03 (Vocabulary Expansion - 30 New Entries, Session 365)
Added 30 new dictionary entries (IDs 14719-14748) from candidate_words.json:

- **Nouns (15)**: ケチャップ (ketchup), {開港|かいこう} (opening of a port), {冷凍庫|れいとうこ} (freezer), {常温|じょうおん} (room temperature), {穴場|あなば} (hidden gem), {撤去|てっきょ} (removal), {下見|したみ} (preliminary visit), {怪獣|かいじゅう} (monster), {泥酔|でいすい} (dead drunk), {車酔|くるまよ}い (carsickness), {駄菓子|だがし} (cheap sweets), {積雪|せきせつ} (snow cover), {助手席|じょしゅせき} (passenger seat), {鋼|はがね} (steel), {古本|ふるほん} (used book)
- **Nouns (compound)**: {掘|ほ}り{出|だ}し{物|もの} (bargain/lucky find), {鍵盤|けんばん} (keyboard/keys), {犠牲|ぎせい} (sacrifice/victim), {弁償|べんしょう} (compensation), {正反対|せいはんたい} (exact opposite)
- **I-adjectives (2)**: {待|ま}ち{遠|どお}しい (eagerly awaited), {脂|あぶら}っこい (greasy)
- **Na-adjectives (3)**: {割高|わりだか} (relatively expensive), {割安|わりやす} (relatively cheap), {過保護|かほご} (overprotective)
- **Godan verb (1)**: {悔|く}やむ (to regret/mourn)
- **Food/drink (4)**: ケチャップ, おでん, {駄菓子|だがし}, {脂|あぶら}っこい
- **Noun (food)**: おでん (oden stew)

Notable features:
- Multi-sense entries: {悔|く}やむ (2: regret + mourn), {洋画|ようが} (2: Western film + Western painting), {犠牲|ぎせい} (2: sacrifice + victim)
- Paired entries: {割高|わりだか}/{割安|わりやす}, {邦画|ほうが}/{洋画|ようが}
- Daily life: {冷凍庫|れいとうこ}, {常温|じょうおん}, {車酔|くるまよ}い, {助手席|じょしゅせき}, {段差|だんさ}
- Culture: おでん, {駄菓子|だがし}, {怪獣|かいじゅう}, {古本|ふるほん}
- New kanji: 2,490 → 2,493 ({犠|ぎ}, {牲|せい}, {鋼|こう})

Total entries: 14,774 → 14,804 (approximate)
Remaining candidates: 4,996 → 4,966 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
