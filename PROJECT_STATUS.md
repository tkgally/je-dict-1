# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-06-16
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

### 2026-06-25 (Routine v2: new-entries — 10 New Entries, IDs 29479–29488 + 猿人 reading fix)
Created the 6 genuine "seen in entry" priority candidates plus 4 hand-curated standalone general-tier nouns; the non-seen-in candidate tail remains heavy corpus-harvest noise (transparent compounds, conjugated fragments, wrong readings — e.g. 強大国 glossed きょうたいこく vs correct きょうだいこく), so picks were vetted individually rather than padded toward 20. **Resolved the long-standing 猿人 reading defect**: existing entry 29452 stored さるじん where the standard anthropology reading is えんじん (confirmed by 29467 原人, which cross-references 猿人/えんじん); corrected reading + headword/example furigana (the headword was also bare/unwrapped) and renamed the file 29452_sarujin→29452_enjin, so 猿人 is no longer created as a duplicate. Skipped candidate 書き替える (替-variant of existing 08225 書き換える) — logged for the curator to fold in as an alternate orthography. §4 cross-model self-check on all 11 changed entries: **9 fully clean; 2 applied** (29479 字数: removed misleading "word count" — 字数 = character count, not 語数 — from the def gloss and fixed the matching example translation); **3 rejected** (in-list tag-narrowness swaps on 29452 science→person and 29485 business→economics; one stylistic gloss trim). $0.0048. Added 文字数 and 二足歩行 as new "seen in entry" candidates.

- **Seen-in-entry (6)**: {字数|じすう} (character count), {頭金|あたまきん} (down payment), {話|はな}し{声|ごえ} (speaking voice), {単打|たんだ} (single, baseball), {旧人|きゅうじん} (archaic humans), {考|かんが}え{詰|つ}める (to brood over; ichidan)
- **Standalone nouns (4)**: {工業製品|こうぎょうせいひん} (industrial product), {発送人|はっそうにん} (sender/shipper), {弱小国|じゃくしょうこく} (minor power), {四輪車|よんりんしゃ} (four-wheeled vehicle)

### 2026-06-24 (Routine v2: new-entries — 16 New Entries, IDs 29463–29478)
Created the 16 priority "seen in entry" candidates remaining in the queue — internal-completeness gaps the dictionary already referenced from polish-frontier entries (06258/06259/06261) and the 29445–29455 financial/legal/baseball cluster. Nine financial/legal/STEM/sports nouns plus seven loanword/slang modifiers (ヘビー, コア, eスポーツ, ストリーマー, エキサイティング, センセーショナル, あざとかわいい). Added 4 referenced contrast words as new "seen in entry" candidates (猿人/えんじん, 旧人, 単打, 頭金). §4 cross-model self-check: **content CLEAN on all 16**; 2 tag-narrowness flags (29468 science→"mathematics" not in-list; 29469 general→action in-list substitution) both REJECTED per the semantic-tag policy. $0.0070. Logged an `[entry]` observation: existing 29452 猿人 carries the non-standard reading さるじん where えんじん is expected (curator to reconcile against the new candidate).

- **Nouns**: {国有地|こくゆうち} (state-owned land), {成功報酬|せいこうほうしゅう} (contingency fee), {手付金|てつけきん} (deposit/earnest money), {長打|ちょうだ} (extra-base hit), {原人|げんじん} (early human/Homo erectus), {対数関数|たいすうかんすう} (logarithmic function), {刻印|こくいん} (engraved mark; verb-suru), {収穫量|しゅうかくりょう} (harvest yield), {貸付金|かしつけきん} (loan, lender side), eスポーツ (esports), ストリーマー (streamer)
- **Na-adjectives / modifiers**: ヘビー (heavy/intense), コア (core; noun+adj-na), エキサイティング (exciting), センセーショナル (sensational)
- **I-adjective (slang)**: あざとかわいい (calculatedly cute)

### 2026-06-24 (Routine v2: new-entries — 20 New Entries, IDs 29443–29462)
Created 20 hand-curated standalone general-tier nouns. The selector reported `seen_in_entry_count` 0, so there was no priority lane; the fallback "oldest unprocessed" candidate pool is heavily polluted (compositional phrases, bare numerals/counters, place-name misglosses, and coinages/wrong glosses — e.g. アンパッサン glossed "ice cream sundae" for *en passant*; 怒燥 for 怒涛), so all 20 were cherry-picked for genuine dictionary-worthiness after surveying ~300 candidates. Removed 2 stale variant candidates (油粕 = variant of existing 油かす 29276; 分速/ぶんそく = wrong-reading dup of 分速/ふんそく 16680). Added 9 referenced words as new "seen in entry" candidates. §4 cross-model self-check: **19 CLEAN; 1 flagged** — 29451 塁打, where the model correctly caught that the entry conflated 塁打 ("total bases") with 安打 ("a hit"); the entry was rewritten and all 4 issues applied. $0.0087.

- **Entries (20)**: {語学力|ごがくりょく} (language ability), {湿地帯|しっちたい} (wetland), {公有地|こうゆうち} (public land), {所有地|しょゆうち} (owned land), {着手金|ちゃくしゅきん} (retainer fee), {虜囚|りょしゅう} (captive), {銘刻|めいこく} (inscription; verb-suru), {講義録|こうぎろく} (lecture notes), {塁打|るいだ} (total bases, baseball), {猿人|さるじん} (early hominid), {指数関数|しすうかんすう} (exponential function), {借入金|かりいれきん} (borrowed money), {漁獲量|ぎょかくりょう} (fish catch), {受水槽|じゅすいそう} (water tank), {速読法|そくどくほう} (speed reading), {末期症状|まっきしょうじょう} (terminal symptoms), {燕尾|えんび} (swallowtail), {預金利率|よきんりりつ} (deposit interest rate), {送信機|そうしんき} (transmitter), {結晶質|けっしょうしつ} (crystalline; adj-no)

### 2026-06-23 (Routine v2: new-entries — 14 New Entries, IDs 29429–29442)
Created the 6 remaining priority "seen in entry" candidates (internal-completeness gaps referenced from polish-frontier entries 06239/06240/06243/06244) plus 8 hand-curated, lexicalized standalone nouns. §4 cross-model self-check came back **CLEAN on all 14** (0 issues, $0.0061). Logged a `[pattern]` observation: candidate_words.json is now largely exhausted of genuine standalone gaps — ~600 surveyed + ~25 extracted base words probed, and nearly every common base word (曖昧, 無難, ぎこちない, 巧み, 速やか, 潔い, 仲良し, 無邪気…) already exists as an entry; remaining pool is mostly transparent compounds, inflected fragments, numeral/counter compounds, and rare coinages. Recommend a curator clean_up_candidates pass + quality restock.

- **Seen-in-entry (6)**: {社風|しゃふう} (company culture), {能率的|のうりつてき} (efficient; na-adj), {守備的|しゅびてき} (defensive; na-adj), プレー (play, sports; noun+suru), {書|か}き{続|つづ}ける (to keep writing; ichidan), {仲良|なかよ}い (on good terms; i-adj)
- **Standalone nouns (8)**: アクション{映画|えいが} (action movie), {走行距離計|そうこうきょりけい} (odometer), {冷却材|れいきゃくざい} (coolant), {肉体労働者|にくたいろうどうしゃ} (manual laborer), {国語教育|こくごきょういく} (Japanese-language education), {加盟団体|かめいだんたい} (member organization), {輸送機関|ゆそうきかん} (means of transport), {糖尿病患者|とうにょうびょうかんじゃ} (diabetic patient)

### 2026-06-22 (Routine v2: new-entries — 20 New Entries, IDs 29409–29428)
Created the 5 remaining priority "seen in entry" candidates (反対語, 襖絵, 茶席, けんちん汁, 骨子 — internal-completeness gaps referenced from entries 06231/06233/29399/29405/29406) plus 15 hand-curated standalone general-tier nouns. The fallback "oldest unprocessed" candidate lane stays largely corpus-harvest noise (bare numerals/counters, transparent 〜化/〜性 compounds, OCR artifacts), so standalone picks were curated for genuine dictionary-worthiness rather than padding from the raw queue. No new kanji. §4 self-check: all 20 CLEAN (0 issues), $0.0086.

- **Seen-in-entry (5)**: {反対語|はんたいご} (antonym), {襖絵|ふすまえ} (fusuma painting), {茶席|ちゃせき} (tea gathering), けんちん{汁|じる} (kenchin soup), {骨子|こっし} (gist/outline)
- **Standalone nouns (15)**: {段|だん}ボール{箱|ばこ} (cardboard box), {速度計|そくどけい} (speedometer), {文例|ぶんれい} (model sentence), {定型表現|ていけいひょうげん} (fixed expression), {控除額|こうじょがく} (deduction amount), {黄褐色|おうかっしょく} (yellowish brown), {音楽理論|おんがくりろん} (music theory), {展望塔|てんぼうとう} (observation tower), {尾翼|びよく} (aircraft tail), {舗装道路|ほそうどうろ} (paved road), {工業団地|こうぎょうだんち} (industrial park), {共同研究|きょうどうけんきゅう} (joint research), {職務経歴|しょくむけいれき} (work history), {挨拶文|あいさつぶん} (greeting message), {保護具|ほごぐ} (protective gear)

### 2026-06-22 (Routine v2: new-entries — 19 New Entries, IDs 29390–29408)
Created all 19 priority "seen in entry" candidates (C22013–C22031) — internal-completeness gaps the dictionary already referenced from polish-frontier entries (06222, 06226–06229, 06797, 17173, 17276, 17278, 17755, etc.). New kanji 罷 (from 罷免) was assigned ID 02775. §4 self-check (cross-model accuracy review of all 19) came back clean except 29401 取り付く, where "to set about" was demoted from the headline gloss to the explanation as an extended sense (1 applied). Added 3 new candidates encountered in notes (反対語, 襖絵, 茶席).

- **Nouns**: {制震|せいしん} (seismic damping), {欠礼|けつれい} (omission of courtesy), {罷免|ひめん} (dismissal from office), {悪者|わるもの} (villain), {対義語|たいぎご} (antonym), {年賀状|ねんがじょう}じまい (ending one's New Year's card custom), {金屏風|きんびょうぶ}/{銀屏風|ぎんびょうぶ} (gold/silver folding screen), {屏風絵|びょうぶえ} (folding-screen painting), {風炉先屏風|ふろさきびょうぶ} (tea-ceremony screen), ちゃぶ{台|だい}{返|がえ}し (table-flip reversal), {頑固親父|がんこおやじ} (stubborn old man)
- **Suru-verbs**: {妊娠|にんしん}する (to become pregnant), {創造|そうぞう}する (to create), {肯定|こうてい}する (to affirm), {推薦|すいせん}する (to recommend), {企画|きかく}する (to plan)
- **Other verbs**: {鎮|しず}める (to quell; ichidan, paired with {鎮|しず}まる), {取|と}り{付|つ}く (to cling to; godan)

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
