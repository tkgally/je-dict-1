# Interactive session 2026-10-23: assessment, Tom's rulings, faster new entries

Follows `enhancement/assessment-2026-10-23.md` (PR #4010). Tom approved every recommendation in
its §4, asked to keep OpenRouter spending at $15 a day at most with two Routine runs a day, and
asked for more new entries plus a brainstorming process for finding candidates.

## D1 accuracy reviewer
- `build/review_accuracy.py` default model → `openai/gpt-6.1-sol` (self-check too).
- Budget split: accuracy-review at most $10 a day (`accuracy_daily_cap_usd`) and $5 a cycle;
  `pipeline/routine_next.py` reads the ledger's accuracy-review calls and suppresses the mode
  when the allowance is spent. Audio cycles capped at $2. routine2.md §A sizes ranges to
  `budget / 0.0065` (about 770 entries at $5).

## D2 headword readings (retire_entry.py rename, then furigana and notes fixed everywhere)
- 14297 軽やか かるやか → かろやか (14297_karoyaka)
- 20142 一味違う いちみちがう → ひとあじちがう (20142_hitoajichigau); the note no longer links 一味 (いちみ, "gang")
- 20226 役立たず やくだたず → やくたたず (20226_yakutatazu)
- 20732 真っ二つ まふたつ → まっぷたつ (20732_mapputatsu); "can also be written 真二つ" removed
- 20854 欲深い よくふかい → よくぶかい (20854_yokubukai), よくふかい noted
- 24323 最後尾 さいごび → さいこうび (24323_saikoubi); etymology corrected (最 + 後尾)
- Two renames collided with entries that already had the right reading: 17975 真っ二つ (まっぷたつ)
  and 21693 最後尾 (さいこうび), and CI rejects duplicate entries. As pure duplicates (same word,
  spelling, reading) they fall under the standing rule (routine2.md §E): 20732's sense 2 and two
  examples were merged into 17975, 24323's reading note into 21693, and 20732 and 24323 retired
  into them (`retire_entry.py retire --duplicate`); every old URL redirects.

## D3 content rulings
- 02828 参考: noun only (verb-suru, transitivity, conjugation removed); three fragment examples
  replaced with full sentences; notes teach 参考にする / 参考になる / ご参考までに.
- 25822 演習曲 retired into 20962 練習曲.
- 00290 文字 (もんじ) retired into 03632 文字 (もじ); its self-link removed, もんじ noted as an older reading.
- 09352 ため口 retired into 16740 タメ口 (ため口 noted under WRITING); 10777 タメ語 kept, cross-referenced.
- 14783 挽肉 retired into 17241 ひき肉 (spellings under WRITING; base forms of two links fixed).
- 06988 音符 / 07538 休符: しぶ-, はちぶ-, じゅうろくぶ-, にぶ- readings; link from 二分 to にぶん removed.
- 00854 かける: sense 10 "to multiply" with two examples.
- 03906 冠: sense 2 ("top of the head") and examples 5–7 deleted; sense 3 renumbered 2.
- Candidate C23197 そうでないと removed.
- `build/retire_entry.py` now also repoints or drops `prominent_see_also` (it left stale IDs in
  16740 and 17241, and two older ones in 05153 and 13385, fixed here); test added.
- Self-check (gpt-6.1-sol, 14 entries): 2 flags, both applied (06988 English note names; 14297
  かるやか is also heard). Link check: one flag, kept (これ in これから in 00854 ex31).

## D5 conventions and the standing rule
- Rulings written into the skills: auxiliary verbs in kana (example-sentences), no line-initial ・
  bullets and no conjugation preambles (vocabulary-notes), kana base for ください links
  (inline-word-links); grammar terms take `language` (already in entry-guidelines).
- Backlog items opened: kanji-written-auxiliary-verbs, notes-bullet-nakaguro,
  inline-link-kudasai-baseform-split, tag-grammar-terminology-convention, tag-interrogative-family,
  compound-verb-conjugation-preamble, entry-pair-consolidation; reviewer-flag-rate-carve-out
  resolved (routine2.md §A step 4).
- Standing rule: routine2.md §E — conventions and pure spelling duplicates are the Routine's to
  settle; reading renames, other retirements and content questions stay with Tom.

## New entries faster, and brainstorming
- Weights: new-entries 0.08 → 0.16, candidates 0.04 → 0.06, polish 0.26, accuracy-review 0.24,
  systemic-fix 0.18 (audio 0.10, gated). Candidates restock below 200 (was 100). Simulated: about
  a quarter of cycles are new-entries, roughly 60 entries a day at two runs a day (about 20 before).
- `build/brainstorm_candidates.py` (next / ask / filter / record): seeds lens (20 headwords in tier
  order) and field lens (one semantic field with its members), proposals from the Routine model and
  from gpt-6.1-sol and gemini-3.8-flash, filtered against entries, candidates, retired IDs and
  earlier verdicts, variant spellings flagged; spend recorded in the ledger (mode candidates).
- `prompts/newcandidates.md` rewritten for the two streams; `prompts/newentries.md` takes half
  closure, half brainstorm candidates and cross-references each brainstorm entry to its seed.
- First round: seeds 00006 ある … 00254 来る and the field animal-bird. 38 candidates added
  (さえ, すら, あり得る, ある程度, ばつが悪い, 二重丸, 数多い, 数少ない, 菓子折り, ごめんください …;
  フラミンゴ, ペリカン, 七面鳥, ダチョウ, キツツキ, カワセミ, オシドリ, コウノトリ, 鳥インフルエンザ, 孵る …).
  Queue 92 → 129.

## D4 digit and Latin readings
- `build/audio_digit_readings.py` and `audio/digit_readings.json`; `spoken_example()` uses a
  confirmed reading as a hand-written one once `method_approved` is true.
- Sample: 120 examples spread over the dictionary, 116 stored, 114 confirmed, 2 disputed; 30
  recorded, all accepted. Listening page for Tom: https://claude.ai/artifact/Fox2wSbfn4DWbhXXz8pQpQ
- Backlog item `audio-digit-readings` (blocked until `approve`).

## Spend
Today's ledger: the assessment calibration ($5.74), the self-check, brainstorming test and round,
the digit readings and the sample; see pipeline/openrouter-ledger.json.

## Later the same day: digit readings approved, half-width digits

- Tom rated all 30 sample clips correct (ratings read from the page's store) and asked for the
  rest to be recorded. `audio_digit_readings.py approve` run; the tool now sends batches in
  parallel (`--workers`).
- Tom asked for half-width digits throughout (３月 vs 3月). Ruling written into entry-guidelines
  and example-sentences; `validate.py` now rejects full-width digits and Latin letters
  (`find_fullwidth_alnum_errors`, test `test_validate_fullwidth.py`). Converted: 52 examples and 6
  notes in 49 entries, plus 自己ＰＲ → 自己PR (19316: headword, examples, notes, conjugation; the
  cross-reference in 12331). Every changed field was checked to differ only in width, except three
  handled by hand: 28699 {１|いち}テラバイト / {２|に}テラバイト → 1テラバイト / 2テラバイト, 28710
  {３本|さんぼん} → 3{本|ぼん}. No article had full-width digits.
- Readings written and confirmed for the remaining examples: 2,571 confirmed in all, 3 disputed
  (00421 綿100% uses the めん word in the わた entry; 07560 IPA（アイピーエー） is read twice;
  17946 中火 headword なかび vs ちゅうび → needs_curator), 1 left without (06910 えーと 090の…).
  Spot check of 40 random confirmed readings plus every hard case: all right.
- The run exposed furigana errors that learners see, fixed by hand (31 examples):
  - Counter after a digit given the bare reading (24): 3{日|にち} → {3日|みっか} (01487, 01724,
    02744, 05135, 08593), {2日|ふつか} (07262), {10日|とおか} (03293, 25761), {1日|ついたち} (07907,
    31243), {3日分|みっかぶん} (07589), {3日間|みっかかん} (22509), {1人|ひとり} / {2人|ふたり} (02856,
    04409, 17094), 20/30/10/90/23{分|ぷん} (02749, 03521, 05736, 08291, 17596), 46/1/200{本|ぽん}
    (05243, 08293, 11150), 第3{版|ぱん} (03698), 3{泊|ぱく} (07049), 3{棟|とう} (17094).
    Convention in entry-guidelines; detector `audio_digit_readings.py counter-furigana` (now 0).
  - Other: 01923 {お金|かね} → お{金|かね}; 08137 {一|いち}{箱|はこ} → {一箱|ひとはこ} (linked to
    28497); 08851 {何|なに}です → {何|なん}; 08969 PA{外|そと} → PA{外|がい} (link to the prefix 外〜
    removed; candidate 〜外 added); 24275 B{組|くみ} → B{組|ぐみ}; 29159 {返信|へんじ} → {返信|へんしん}.
- Self-check on the 33 edited entries (gpt-6.1-sol): 4 flags, all on older text. Applied: 02744
  施行 "came into force" (not "was enacted"); 02856 大人しい derives from 大人. Flagged: 01923 降ろす
  teaches 降ろす for withdrawing money (下ろす); logged as an observation with the fix for polish.
- Audio: 2,629 examples now wait to be recorded; the selector doubles audio (large backlog), so
  about four audio cycles at $2 each.

## 中火

Tom ruled: 中火 is ちゅうび, なかび a variant. 08169 中火 (ちゅうび) already existed, so instead of a rename (which would have duplicated it) 17946 中火 (なかび) was retired into 08169 (`retire_entry.py retire --duplicate`; the old URL redirects). 08169 now notes なかび as a less common reading and took 17946's example 中火にして5分煮る. Self-check on 08169: clean.
