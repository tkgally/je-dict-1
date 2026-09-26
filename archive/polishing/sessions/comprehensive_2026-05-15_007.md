# Comprehensive Polish Session — 2026-05-15 (007)

**Date:** 2026-05-15
**Entry range:** 01489–01511
**Next entry:** 01512

## Changes made

### Semantic tag fixes
- **01496_hanashi**: `furniture` → `communication` (話 = talk/story, not furniture)
- **01498_hikidashi**: removed erroneous `emotion` tag; kept `furniture`

### Structural fixes
- **01497_hantai**: removed duplicate `conjugation` stub at top of JSON (full conjugation table already existed at bottom)

### Cross-reference data fix
- **01495_hatsumei**: fixed corrupted headword `{発見|はっけ�}` in cross_references (Unicode replacement character U+FFFD); corrected to `{発見|はっけん}`

### Build script fixes
- **build/verify_furigana.py**: added inline link stripping (`→base：id⟧`) before furigana check to prevent false positives on base forms in notes
- **build/find_missing_furigana.py**: same fix applied to both `contains_unannotated_kanji()` and `extract_unannotated_context()`

### Inline links added
Comprehensive inline link additions throughout notes sections for entries 01489–01511:
- **01489_nuno** (布): COMMON EXPRESSIONS (縫う, 切る, 拭く, 布地), COMPOUNDS (布団, 雑巾, 布巾, 毛布), TYPES (綿, 木綿, 絹, 麻, ウール)
- **01490_nenrei** (年齢): FORMALITY (歳→年, お年), EXPRESSIONS (聞く, 制限, 層, 順), PATTERNS (に関係なく, 重ねる, 相応)
- **01491_nougyou** (農業): EXPRESSIONS (する/営む, 従事), RELATED (農家, 農産物, 農地, 農村, 農協), INDUSTRIES (漁業, 林業, 工業)
- **01492_bai** (倍): EXPRESSIONS (二倍, 三倍, 何倍), PRONUNCIATION (一倍, 二倍, 三倍), CONTRAST (分, パーセント)
- **01493_baiten** (売店): COMMON LOCATIONS (駅, 病院, 学校), ITEMS (新聞, 雑誌, 飲み物, お菓子, 弁当), CONTRAST (店, コンビニ)
- **01494_hakubutsukan** (博物館): TYPES (国立, 歴史, 科学, 自然史), DISTINCTION (美術館), EXPRESSIONS (見学する)
- **01495_hatsumei** (発明): TRANSITIVITY (他動詞), PATTERNS (発明する, 偉大, 新しい), RELATED (発明家, 発明品, 発見, 開発), DISTINCTION (発見)
- **01496_hanashi** (話): PATTERNS (する, 聞く, ある, 長い), EXPRESSIONS (上手, 合う, 変わる, にならない), COMPOUNDS (昔話, 世間話, 身の上話)
- **01497_hantai** (反対): TRANSITIVITY (自動詞), VERBAL USE (する, に+する), MEANINGS (計画, 方向), EXPRESSIONS (意見, 側, 運動, 賛成か反対か), CONTRAST (賛成, 逆)
- **01498_hikidashi** (引き出し): ETYMOLOGY (引き出す), EXPRESSIONS (開ける, 閉める, しまう, の中), RELATED (机, タンス, 棚)
- **01499_bideo** (ビデオ): EXPRESSIONS (見る, 撮る, 送る), COMPOUNDS (カメラ, 通話, ゲーム, 会議), MODERN USAGE (動画)
- **01500_biru** (ビル): EXPRESSIONS (高い, オフィス, 5階, 屋上), COMPARISON (建物, マンション, 高層), NOTE (マンション, アパート)
- **01501_fuben** (不便): FORMS (場所, 感じる), EXPRESSIONS (かける, なく, 交通の), CONTRAST (便利), USAGE (申し訳ありません)
- **01502_futsuu** (普通): ADJECTIVE (人, 生活, 大きさ), ADVERB (7時に起きる), TRAINS (電車, 急行, 特急), SIMILAR (通常, 一般的, 平凡)
- **01503_burashi** (ブラシ): TYPES (歯ブラシ, ヘアブラシ, 洋服, 靴, ペイント), EXPRESSIONS (かける, 磨く, 整える), RELATED (櫛, たわし)
- **01504_bunka** (文化): EXPRESSIONS (日本, 違い, 学ぶ, 交流), COMPOUNDS (文化的, 文化祭, 文化遺産, 異文化), NOTE (文化の日)
- **01505_bungaku** (文学): EXPRESSIONS (専攻する, 作品, 研究する), COMPOUNDS (文学部, 文学賞, 日本文学, 比較文学, 現代文学), RELATED (小説, 詩, 評論)
- **01506_bunpou** (文法): EXPRESSIONS (勉強する, 間違い, 正しい, 合う), RELATED (文法的, 文法書, 文型, 語彙)
- **01507_heiwa** (平和): USAGE (守る, 世界), EXPRESSIONS (世界平和, 時代, 願う, 条約), RELATED (平和的, 平和主義, 戦争)
- **01508_beruto** (ベルト): TYPES (革ベルト, 安全ベルト), EXPRESSIONS (締める, 外す, 緩める), USAGE (帯)
- **01509_hoken** (保険): TYPES (生命, 健康, 自動車, 旅行, 火災), EXPRESSIONS (入る, かける), NOTE (国民健康保険)
- **01510_hoshi** (星): EXPRESSIONS (見る, 出る, 輝く, 流れ星, 星空), COMPOUNDS (星座, 一番星, 北極星), FIGURATIVE (三つ星), SCIENCE (恒星, 惑星)
- **01511_manga** (漫画): TERMS (漫画家, 単行本, 連載, 同人誌), TYPES (週刊, 少年, 少女), EXPRESSIONS (読む, 漫画喫茶)

## Notes

No new candidates added this session.
