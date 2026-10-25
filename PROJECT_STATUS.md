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

### 2026-10-25 (Routine v3: new-entries — 16 New Entries, IDs 32250–32265)

Eight internal-closure candidates: ぬるま{湯|ゆ} (lukewarm water and, figuratively, complacency),
{振|ふ}り{子|こ}, {素養|そよう} (contrasted with {教養|きょうよう} and {素質|そしつ}), {我|が}を{張|は}る
(with {意地|いじ}を{張|は}る), {脅|おど}し, {警戒心|けいかいしん}, {難攻不落|なんこうふらく} and
{持|も}ち{越|こ}し (with {繰|く}り{越|こ}し). Eight brainstorm candidates: あり{得|え}る (ありうる /
ありえる and the negative ありえない), the particles さえ (including 〜さえ〜ば) and すら, the idiom
{御免|ごめん}{被|こうむ}る, and four birds (キツツキ, カワセミ, カッコウ with {閑古鳥|かんこどり}が{鳴|な}く,
ヒバリ). Self-check: one fix (Japan's commonest woodpecker is コゲラ). Queue 127 → 111.

### 2026-10-24 (Routine v3: new-entries — 6 New Entries, IDs 32244–32249)

Another short closing cycle (about half an hour left on the run clock). Three internal-closure
candidates: {政局|せいきょく} (the contest over who governs, with the 政策より政局 contrast),
{享年|きょうねん} (age at death, with the traditional omission of 歳 and the 数え年 count) and
{前歯|まえば} (with 奥歯, 門歯, 八重歯). Three brainstorm candidates from the animal-bird field:
{七面鳥|しちめんちょう} (with ターキー and a warning that the country is トルコ), ウズラ (mostly
the eggs) and ダチョウ. Self-check clean. One wrong link (the は in "は → ば" linked to the
particle) was removed by rewording. Queue 133 → 127.

### 2026-10-24 (Routine v3: new-entries — 4 New Entries, IDs 32240–32243)

A short closing cycle with half an hour left on the run clock, so four entries rather than the
usual twenty. Two internal-closure candidates: {石段|いしだん} (stone steps, the flights that lead
up to a shrine; cross-referenced to 階段 and 坂) and {絶版|ぜっぱん} (out of print, with the
contrast to 品切れ that learners need — a book out of stock may be reprinted, an 絶版 one will
not). Two brainstorm candidates from the animal-bird field, フラミンゴ and ペリカン, both counted
with 羽. Self-check clean on all four. Queue 132 → 128.

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
