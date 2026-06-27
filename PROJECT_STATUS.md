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

### 2026-06-27 (Routine v2: new-entries — 10 New Entries, IDs 29507–29516)
Created the 4 genuine "seen in entry" priority candidates plus 6 hand-curated standalone general-tier words. The non-seen candidate tail is still overwhelmingly corpus-harvest noise (transparent compounds, bare numerals/counters, dialect fragments, misglosses — e.g. アンパッサン "ice cream sundae"), so the 6 standalone picks were vetted individually for genuine dictionary-worthiness rather than padded from the oldest queue; logged a `[pattern]` observation requesting curator restock/pruning. **Created 書き替える** (替-variant of existing 08225 書き換える) — the prior two runs deferred it to the curator, but as a real "seen in entry" candidate (referenced from 06270) it is now a single-sense v2.0 entry cross-referenced to 08225 as alternate orthography. Conjugation table added to the one verb; no new kanji. §4 cross-model self-check on all 10 changed entries: **9 fully clean; 0 applied; 1 rejected** (29515 脱色剤: model flagged semantic `daily-life`→`health`, but `health` is wrong for a household/hair bleach and `daily-life` is in `VALID_SEMANTIC` — in-list breadth nit, rejected per the semantic-tag policy). $0.0043. Captured 巻積雲 (けんせきうん) as a new "seen in entry" candidate referenced from the new 高積雲 entry.

- **Seen-in-entry (4)**: {書|か}き{替|か}える (to rewrite/transfer a registration; ichidan), {雌|め}しべ (pistil), そうは{言|い}っても (having said that; expression), {兵|へい} (soldier)
- **Standalone words (6)**: リスナー (listener/audience), そっち{側|がわ} (that side; your side), {肘関節|ひじかんせつ} (elbow joint), {高積雲|こうせきうん} (altocumulus), {脱色剤|だっしょくざい} (decolorizing agent; hair bleach), {鮭缶|さけかん} (canned salmon)

### 2026-06-26 (Routine v2: new-entries — 18 New Entries, IDs 29489–29506)
Created the 4 remaining genuine "seen in entry" priority candidates (文字数, 二足歩行, 短慮, 篤実 — internal-completeness gaps referenced from 29479/29483/06278/06279) plus 14 hand-curated standalone general-tier words. The non-seen candidate tail is still heavy corpus-harvest noise (place names, bare numerals/counters, misglosses — e.g. アンパッサン "ice cream sundae", 怒燥), so the 14 were vetted individually for genuine dictionary-worthiness rather than padded from the oldest queue. Skipped candidate 書き替える (替-variant of existing 08225 書き換える, kept for the curator as alternate orthography). Conjugation tables added to the 6 noun+verb-suru entries; no new kanji (used the kana orthography 雄しべ to avoid the rare 蕊/葯). §4 cross-model self-check on all 18 changed entries: **17 fully clean; 0 applied; 1 rejected** (29498 歌集: model flagged semantic `art`→`literature`, but `literature` is not in `VALID_SEMANTIC` and `art` is the best in-list home for a poetry anthology — narrowness substitution, rejected per the semantic-tag policy). $0.0078. Added 雌しべ (めしべ, pistil) as a new "seen in entry" candidate pairing with the new 雄しべ entry.

- **Seen-in-entry (4)**: {文字数|もじすう} (character count), {二足歩行|にそくほこう} (bipedal walking; verb-suru), {短慮|たんりょ} (rashness; noun/adj-na), {篤実|とくじつ} (sincere, faithful; adj-na/noun)
- **Nouns (9)**: {博覧会|はくらんかい} (exposition), {借家|しゃくや} (rented house), {散髪屋|さんぱつや} (barbershop), {議事堂|ぎじどう} (assembly hall), {所有物|しょゆうぶつ} (belongings), {歌集|かしゅう} (poetry anthology), {本論|ほんろん} (main argument), {雪山|ゆきやま} (snowy mountain), {雄|お}しべ (stamen)
- **Noun+verb-suru (5)**: {受精|じゅせい} (fertilization), {整合|せいごう} (consistency), {偶発|ぐうはつ} (chance occurrence), {近接|きんせつ} (proximity), {発布|はっぷ} (promulgation)

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

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
