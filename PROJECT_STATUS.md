# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-27
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
| Total entries | ~19,058 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,259 (open) |
| Candidate words | ~5,099 |
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

### 2026-03-27 (Vocabulary Expansion - 30 New Entries, Session 517)
Added 30 new dictionary entries (IDs 19888-19917) from candidate_words.json. Diverse mix of useful vocabulary for intermediate learners including adverbs, verbs, expressions, and nouns.

- **Adverbs (9)**: {着実|ちゃくじつ}に (steadily), {意外|いがい}に (surprisingly), {大幅|おおはば}に (drastically), {大量|たいりょう}に (in large quantities), {無意識|むいしき}に (unconsciously), {事細|ことこま}かに (in great detail), {近|ちか}いうちに (in the near future), {第二|だいに}に (secondly)
- **Verbs (6)**: {交付|こうふ}する (to issue officially), {通読|つうどく}する (to read through), {突|つ}き{刺|ささ}る (to pierce), {執|と}り{行|おこな}う (to conduct ceremony), {悔|く}い{改|あらた}める (to repent), {植|う}え{付|つ}ける (to implant)
- **Expressions (3)**: {気|き}のせい (one's imagination), {何|なん}でもない (nothing special), {落|お}ち{着|つ}ける (to calm/relax)
- **Nouns (7)**: {子分|こぶん} (follower), {微糖|びとう} (low sugar), {氷解|ひょうかい} (clearing of doubts), {板場|いたば} (kitchen/chef), {山札|やまふだ} (draw pile), {解釈違|かいしゃくちが}い (misinterpretation), {眼識|がんしき} (discerning eye)
- **Adjectives/Other (5)**: {用意周到|よういしゅうとう} (thoroughly prepared), {忍|しの}び{難|がた}い (unbearable), {切|き}り{立|た}った (steep), {目立|めだ}たない (inconspicuous), かつ (and/moreover), {追随|ついずい}する (to follow/emulate)
- Removed 29 candidates that now exist as entries

### 2026-03-27 (Vocabulary Expansion - 15 New Entries, Session 516)
Added 15 new dictionary entries (IDs 19873-19887) from candidate_words.json. Mix of common vocabulary useful for intermediate learners including cultural items, everyday nouns, and verbs.

- **Nouns (12)**: {真珠|しんじゅ} (pearl), {焼酎|しょうちゅう} (shochu), {内戦|ないせん} (civil war), {敬礼|けいれい} (salute), {手仕事|てしごと} (handicraft), {内職|ないしょく} (side work), {休校|きゅうこう} (school closure), {水辺|みずべ} (waterside), {木立|こだち} (grove), {効|き}き{目|め} (effect), {置物|おきもの} (ornament), {人気者|にんきもの} (popular person)
- **Na-adjective (1)**: {不都合|ふつごう} (inconvenient/improper)
- **Noun with two senses (1)**: {火力|かりょく} (heat output/firepower)
- **Verb (1)**: {案|あん}じる (to worry about)
- New kanji added: 酎 (sake)
- Removed 1 stale candidate (子守唄 — variant of existing 子守歌 entry)

### 2026-03-27 (Vocabulary Expansion - 24 New Entries, Session 515)
Added 24 new dictionary entries (IDs 19849-19872) from candidate_words.json. Practical vocabulary for intermediate learners including daily life terms, academic titles, grammar points, and cultural vocabulary.

- **Nouns (14)**: {雨傘|あまがさ} (rain umbrella), {遮光|しゃこう} (light blocking), {通信料|つうしんりょう} (communication charges), {口座振替|こうざふりかえ} (direct debit), {時間指定|じかんしてい} (time-slot delivery), {保安検査|ほあんけんさ} (security screening), {化学物質|かがくぶっしつ} (chemical substance), {非常|ひじょう}ベル (emergency bell), {明治|めいじ} (Meiji era), {准教授|じゅんきょうじゅ} (associate professor), お{祝|いわ}い{金|きん} (congratulatory money), {下方修正|かほうしゅうせい} (downward revision), {荷札|にふだ} (luggage tag), {筆先|ふでさき} (brush tip/writing style), {中間層|ちゅうかんそう} (middle class)
- **Na-adjectives (4)**: {世俗的|せぞくてき} (secular/worldly), {無機質|むきしつ}な (cold/inorganic), {情緒不安定|じょうちょふあんてい} (emotionally unstable), {物欲|ものほ}しげ (wistful/longing)
- **Other (5)**: {無課金|むかきん} (free-to-play), {鵜|う} (cormorant), どなたか (someone/polite), だけれども (although/but), といった (such as)
- New kanji added: 准 (quasi), 鵜 (cormorant)

### 2026-03-27 (Vocabulary Expansion - 30 New Entries, Session 514)
Added 30 new dictionary entries (IDs 19819-19848) from candidate_words.json. Mix of useful vocabulary for intermediate learners including cultural terms, abstract nouns, and adjectives.

- **Nouns (20)**: {夏至|げし} (summer solstice), {士気|しき} (morale), {予知|よち} (foreknowledge), {補佐|ほさ} (assistant), {孤児|こじ} (orphan), {模擬|もぎ} (mock), {機知|きち} (wit), {次期|じき} (next term), {帰化|きか} (naturalization), {遺棄|いき} (abandonment), ミニ (mini), {孵化|ふか} (hatching), ぶれ (shake/wavering), {図示|ずし} (illustration), {地場|じば} (local), {飲|の}み{食|く}い (eating and drinking), {冷|ひ}え (chill), {飢|う}え (hunger), {伸|の}び (growth), {慣|な}れ (familiarity)
- **I-adjectives (3)**: {弱々|よわよわ}しい (frail), {義理堅|ぎりがた}い (dutiful), {芳|かんば}しい (fragrant/favorable)
- **Na-adjectives (2)**: {奇異|きい} (strange), {美味|びみ} (delicious)
- **Other (5)**: {岐路|きろ} (crossroads), {賭|か}け (bet/gamble), {下戸|げこ} (non-drinker), {既知|きち} (known), {尾根|おね} (ridge)
- New kanji added: 孵 (hatch)
- Removed 1 stale candidate (湿気/しけ — variant reading of existing entry)

### 2026-03-27 (Vocabulary Expansion - 30 New Entries, Session 513)
Added 30 new dictionary entries (IDs 19789-19818) from candidate_words.json. Diverse mix including weather terms, causative verbs, cultural vocabulary, and business/legal terms.

- **Nouns (18)**: {盗|ぬす}み (theft), {転落|てんらく} (fall/decline), {洋式|ようしき} (Western-style), {聞|き}き{手|て} (listener), {実演|じつえん} (live demonstration), {熱波|ねっぱ} (heat wave), {顔料|がんりょう} (pigment), {長兄|ちょうけい} (eldest brother), {登記|とうき} (registration), {退団|たいだん} (leaving a group), {大容量|だいようりょう} (large capacity), {白地|しろじ} (white background), {美術室|びじゅつしつ} (art room), {司令塔|しれいとう} (control tower/playmaker), {妻子持|さいしも}ち (family man), {楽観視|らっかんし} (optimistic view), {炎暑|えんしょ} (scorching heat), {保有者|ほゆうしゃ} (holder/owner), {年次報告|ねんじほうこく} (annual report), {性自認|せいじにん} (gender identity), {沙汰止|さたや}み (abandoned/dropped), {社員食堂|しゃいんしょくどう} (employee cafeteria)
- **Verbs (3)**: たわむ (to bend/warp), {悩|なや}ませる (to trouble), {怒|おこ}らせる (to make angry)
- **Suru verbs (4)**: {踏破|とうは} (to traverse), {通読|つうどく} (to read through), {中座|ちゅうざ} (to leave midway)
- **Adverbs (3)**: {不覚|ふかく}にも (unwittingly), つい{先日|せんじつ} (just the other day)
- Removed 5 stale candidates (受理する, 同行する, 遂行する, 逆上する, 包括する — already exist as entries)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
