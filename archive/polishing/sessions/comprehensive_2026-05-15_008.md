# Comprehensive Polish Session — 2026-05-15 #008

## Date
2026-05-15

## Entry range processed
01512–01530 (19 entries)

## Changes made

### Inline links added
All 19 entries received inline link additions to notes (and where applicable, examples):

- **01512_minato** (港) — linked 着く, 出る, 町, 空港, 漁港, 港湾; marked 貿易港, 横浜, 神戸, 港区 as noentry
- **01513_mimi** (耳) — linked 痛い, 遠い, 傾ける, 澄ます, 早い, 耳たこ (noentry), できる, 馬, の, 念仏, 目, 鼻, 口
- **01514_mukae** (迎え) — linked 迎える in examples; linked particles/verbs in COMMON EXPRESSIONS/COLLOCATIONS
- **01515_mukashi** (昔) — linked の, から, は; marked 昔々 as noentry; linked 昔話, 大昔, 昔風, 昔馴染み, 以前, 古代, 今
- **01516_mukou** (向こう) — linked 見える, 〜側, 来る, 意見, こちら
- **01517_yakusoku** (約束) — linked 他動詞, を, する, 守る, 破る, 時間, 取り付ける, と, する, ある, 予約, 契約; linked ASPECT example sentence
- **01518_yubi** (指) — linked 足の, 親指, 人差し指, 中指, 薬指, 小指, 切る, 指す (also fixed `{さす|さす}` formatting), 指輪, 指先, 咥える
- **01519_yume** (夢) — linked を見る, が→ある, 悪夢, 中, 叶う, 諦める, 追い掛ける, 夢中; marked 白昼夢 as noentry; linked 初夢, よう
- **01520_youji** (用事) — linked が→ある, を→済ます, を→思い出す; linked COLLOCATIONS: 仕事, 予定
- **01521_yousu** (様子) — linked を→見る, が→おかしい, が→変わる, を→伝える, Xの, 見に→行く, 決める, どんな, ですか
- **01522_yoyaku** (予約) — linked する, 他動詞, を→取る, を→入れる, を→取り消す, レストラン, ホテル, 病院, 予約済み, 予約席, 予約制, 要
- **01523_ryouri** (料理) — linked 他動詞, を, する, 手料理, 家庭料理, 和食, 日本料理, 洋食, 中華料理, 郷土料理, 料理人, 料理教室
- **01524_renraku** (連絡) — linked 自動詞, する, を→取る, が→来る, が→取れない, 連絡先; marked 網 as noentry; linked バス, 良い/悪い, ください
- **01525_wakai** (若い) — linked く→見える, 若さ, 頃, 時, 人, 者, 世代, まだ, 若者, 若返る, 小さい
- **01526_waribiki** (割引) — linked する, に→なる, 学生, 団体, 割引券, 割引価格, セール, 値引き, 半額
- **01527_anime** (アニメ) — linked を→見る, 化, する, 映画, 声優, 漫画, 制作, 会社; marked アニメーション as noentry
- **01528_arubaito** (アルバイト) — linked 自動詞, バイト, を→する, を→探す, 先, 派遣社員, 契約社員, パート; marked 代/料 as noentry
- **01529_oobaa** (オーバー) — linked を→着る, 予算, 時間, 体重, コート
- **01530_konpyuutaa** (コンピューター) — linked を→使う, で→作業→する, が→動く, パソコン, ノートパソコン, デスクトップ, タブレット, ウイルス; marked グラフィックス, 量子 as noentry

### Bug fixes: malformed duplicate conjugation fields removed
Five entries had a malformed first `conjugation` JSON key followed by a correct second one. The malformed first ones were removed:

- **01517_yakusoku** — removed `{"type": "godan", "ending": "く", "stem": ...}`
- **01522_yoyaku** — removed `{"type": "godan", "ending": "く", "stem": ...}`
- **01523_ryouri** — removed `{"type": "suru", "prefix": "..."}`  (non-standard prefix format)
- **01524_renraku** — removed `{"type": "godan", "ending": "く", "stem": ...}`
- **01528_arubaito** — removed `{"type": "suru", "prefix": "アルバイト"}`

### Furigana fix
- **01518_yubi** — fixed `{さす|さす}` (redundant furigana on hiragana word) to plain `⟦さす→指す：02056_sasu⟧`

## Observations
- [entry] たこ (callus meaning, as in 耳にたこができる) has no entry — candidate for nouns with idiomatic uses
- The malformed "godan" conjugation objects with `ending`/`stem` fields appear to be artifacts from an early batch run. They were harmless to json.load (last key wins) but messy. Other entries in this range may have similar duplicates.

## Next entry
01531 (サービス)
