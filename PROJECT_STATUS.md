# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-10-23
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
| Total entries | ~30,764 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,981 (open) |
| Candidate words | ~188 (all vetted; queue cleaned 2026-08-11) |
| Cross-references | ~19,000 |
| Example sentences | ~119,000 |

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

### 2026-10-24 (Routine v3: candidates — 37 words queued, C24709–C24745)

Internal closure found nothing this time: `check_stale_noentry.py` reports no unresolved
missing-word markers left. The brainstorm seeds lens (basic-tier headwords 見る through 時間)
is close to saturation: of 169 proposals from me and two independent models, 153 were already
entries. The seven survivors are 判明する, 周知, 分かり合う, 存じ上げる, それどころか and the
patterns を通して and をはじめ. The field lens (animal-fish, 37 members) was more productive —
30 words, mostly fish a learner meets on a menu or in a classroom (アジ, ブリ, ハマチ, カレイ,
タラ, フグ, ニシン, シシャモ, アナゴ, ホッケ, カンパチ, スズキ, サワラ, メダカ, ドジョウ,
ナマズ, ニジマス, トビウオ, エイ, タツノオトシゴ, シラス, トロ) plus 海水魚, 川魚, 赤身魚,
小骨, 三枚おろし, 魚群, 胸びれ, 浮き袋. Twenty-five proposals were rejected as species beyond
the familiar ones or as trade terms. Queue 95 → 132.

### 2026-10-23 (Routine v3: new-entries — 10 New Entries, IDs 32230–32239)

Five internal-closure candidates (突っ立つ, 粘り, 勤労感謝の日, 酔い止め, 手繰り寄せる) and five brainstorm candidates, each cross-referenced to its seed (ばつが悪い and 二重丸 → ×/バツ, 菓子折り → 菓子, 価格帯 → 価格, だとしても → だけど). A short cycle at the end of a run. Self-check: one translation fixed; two wrong links to として removed from だとしても's notes. Queue 105 → 95.

### 2026-10-23 (Routine v3: new-entries — 25 New Entries, IDs 32205–32229)

Twenty internal-closure candidates (送辞, 立憲君主制, 醸造所, 年俸制, 尺貫法, 濃口醤油, 刀鍛冶, 町奉行, 金目鯛, 芳名帳, 級数, 新生児, 語り明かす, 後ずさり, 憩い, 社交界, 祝い事, 文面, 生え変わる, 見え見え) and the first five brainstorm candidates (菓子パン, ある程度, ごめんください, 数多い, 数少ない), each cross-referenced to its seed entry. The new-entries prompt's filter for brainstorm candidates matched nothing; fixed. The harvester added reciprocal cross-references in 29 existing entries. Self-check: clean. Queue 130 → 105.

### 2026-10-23 (Interactive: assessment, curator rulings, faster new entries)

Tom approved every recommendation in `enhancement/assessment-2026-10-23.md`. The accuracy reviewer is now gpt-6.1-sol (at most $10 of the $15 daily cap). Six headword readings were corrected (軽やか かろやか, 一味違う ひとあじちがう, 役立たず やくたたず, 真っ二つ まっぷたつ, 欲深い よくぶかい, 最後尾 さいこうび); two of them turned out to duplicate correct entries (17975 真っ二つ, 21693 最後尾) and were merged into them. Four entries were retired into others (演習曲 → 練習曲, 文字(もんじ) → 文字(もじ), ため口 → タメ口, 挽肉 → ひき肉), and 参考, 音符, 休符, かける and 冠 were revised. New entries now get about a quarter of the Routine's cycles, and the candidate queue has a second stream, brainstorming from existing headwords and semantic fields (`build/brainstorm_candidates.py`). Its first round added 38 candidates (さえ, すら, あり得る, ある程度, フラミンゴ, 七面鳥 …). Tom approved the readings for examples with digits or Latin letters after rating 30 sample clips correct; readings for the other 2,540 were written and confirmed, and about 2,600 examples now wait for the audio mode. Digits and Latin letters are now half-width everywhere (52 examples converted; validation enforces it), and 31 examples whose furigana misread a number+counter or a word (3日 にち for みっか, 20分 ふん, 返信 へんじ) were corrected. Session log: `polishing/sessions/interactive_2026-10-23_assessment.md`.

### 2026-10-23 (Routine v3: candidates — 60 words queued, C24610–C24669)

Restocked the candidate queue with 60 words the dictionary already uses in example sentences but does not define, each noted with the entry it was seen in. They came from a fresh SudachiPy scan of unlinked example text, read by hand: everyday words (前歯, 春先, 長旅, 体操服, 酔い止め, 立ち仕事, 新生児), verbs (生え変わる, 見計らう, 追いやる, 負け越す, 勝ち上がる, 垣間見える), set phrases and idioms (我を張る, 難攻不落, 異国情緒, 粒揃い), and Labor Thanksgiving Day (勤労感謝の日). Most scan hits were other spellings of existing entries (子ども, 気づく, 怪我, 可愛い …) that the linker does not link; that is logged as a tooling observation. Queue 32 → 92.
