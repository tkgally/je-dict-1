## Session: Migrate Pair-Type Cross-References to prominent_see_also
Date: 2026-04-11

### Mode
Migration task, not asymmetry fix. Scanned the entire dictionary for
`cross_references` entries with `type: "pair"` and migrated all of them to
`prominent_see_also` per the deprecation rule in the cross-reference skill
and `prompts/add_cross-references.md` Step 4.

### Scope
- **67 pair-type references** across 67 source entries (the task description
  mentioned 21 asymmetric ones; a full scan found 67 total, including 46
  already-symmetric bidirectional pairs).
- **93 entries modified**: 67 source entries (with pair refs) and 26
  target-only entries (existing entries that received a new back-link because
  they had no pre-existing back-reference to the source).

### Approach
A text-based migration was used (not json.load/json.dump round-tripping) to
preserve the exact file structure of unchanged fields. A prior JSON-based
attempt inadvertently collapsed pre-existing duplicate `conjugation` keys
(an unrelated data-quality issue affecting 4,015 entries in the repo) into
a single key, producing 100-200 line diffs per entry. The text-based script
does targeted regex/string edits on `cross_references`, `prominent_see_also`,
and `metadata.modified`, leaving everything else byte-identical.

For each pair-type reference:
1. Removed the `pair` entry from `cross_references` on the source.
2. Added a corresponding `prominent_see_also` entry on the source with a
   brief 2-4 word note.
3. On the target, if a reciprocal pair-type reference existed it was
   removed too; if no back-link existed in any form, a reciprocal
   `prominent_see_also` entry was added with the opposite note.
4. Updated `metadata.modified` on both sides.

Existing `prominent_see_also` entries on either side were preserved; new
entries were appended (with duplicate detection by target_id).

### Note conventions
- **Transitive/intransitive verb pairs** (55 pairs, the vast majority):
  notes are exactly `"transitive"` / `"intransitive"`. Labels like
  "transitive, to break something" from the original `cross_references`
  were normalized to just `"transitive"` (the gloss fragment belongs in
  the target's own gloss, not in a cross-reference note).
- **Noun/verb form pairs** (4 pairs): `"noun form"` / `"verb form"`.
  Examples: 負け (noun) ↔ 負ける (verb), 試し (noun) ↔ 試す (verb),
  乱れ (noun) ↔ 乱す (verb).
- **Semantic opposites** (8 pairs): short descriptive notes.
  Examples: 被告 ↔ 原告 (`"plaintiff"` / `"defendant"`), 新郎 ↔ 新婦
  (`"bride"` / `"groom"`), 簡体字 ↔ 繁体字 (`"traditional characters"` /
  `"simplified characters"`), 年末 ↔ 年始 (`"new year period"` /
  `"year-end period"`), 春分 → 秋分 (`"autumnal equinox"` /
  `"vernal equinox"`), 下半期 ↔ 上半期 (`"first half"` / `"second half"`),
  ヒーロー ↔ ヒロイン (`"female counterpart"` / `"male counterpart"`).

### Forward-reference resolution
Ten pair-type references had no `target_id` (the target was either missing
from the dictionary or was a forward reference). Three of these were
resolved to existing entries during migration:

- `06048_haritsuku` → `06855_haritsukeru` (bridging the 張り付く → 貼り付ける
  kanji difference; 06855 is the closest existing transitive counterpart;
  headword on the source's new link corrected to `{貼|は}り{付|つ}ける` to
  match the target)
- `07384_kojireru` → `22115_kojiraseru` (target entry existed all along,
  just lacked a target_id in the original pair reference)
- `19925_shimohanki` → `20412_kamihanki` (target entry existed)

The remaining seven forward references could not be resolved (no matching
entry exists) and were migrated as forward-reference `prominent_see_also`
entries without a `target_id`:

- `00097_hekomu` → へこます (no entry exists)
- `00405_togaru` → とがらせる (no entry exists)
- `03922_kezuru` → けずれる (no entry exists)
- `06797_toritsukeru` → とりつく (only 11969_toritsuku 取り憑く exists,
  but that's "to be possessed," a different meaning; the expected
  intransitive pair 取り付く does not exist as a separate entry)
- `07005_makiokoru` → まきおこす (no entry exists)
- `07009_hanekaeru` → はねかえす (no entry exists)
- `07417_hikkomu` → ひっこめる (no entry exists)

These will auto-harden once the target entries are created.

### Edge cases
- **13167_kakeru / 13166_kaku**: The original pair reference on 13167
  lacked a `headword` field (it had only `target_id`, `reading`, `type`,
  and `description`). The migration script falls back to looking up the
  target's actual headword from its entry file, producing a valid
  `prominent_see_also` entry with `headword: "{欠|か}く"`.
- **01263_oru / 01266_oreru**: 01263 already had a `prominent_see_also`
  entry for 04373_oru (織る, "to weave"); the new back-link to 01266_oreru
  is appended after it.
- **01231_tsuzukeru**: Already had two `prominent_see_also` entries for
  suffix forms 02004_tsuzukeru and 02457_tsuzukeru; the new back-link
  to 00903_tsuzuku is appended.
- **11718_kawaru**: Already had a `prominent_see_also` entry for 00714_kawaru
  (変わる homophone); the new back-link to 11717_kaeru is appended.

### Verification
- `build/validate.py`: 23021/23021 entries valid. Pre-existing warning
  counts unchanged (3 cross-reference, 23 homonym mismatch, 28 hardenable,
  545 POS consistency).
- Scan for `type: "pair"` in `cross_references`: **0** (was 67).
- `build/find_merge_candidates.py --asymmetry-only`:
  - After migration: 2745 asymmetric pairs (unchanged from 2745 before,
    because all 67 pairs were migrated bilaterally — the 21 previously
    one-way `pair` asymmetries are replaced by 21 symmetric
    `prominent_see_also` bidirectional pairs, so no net change).
- `make build`: clean rebuild of the static site.

### Modified entries (93 total)
Source entries (67) with their migrations:

| Source | Target | Note (source → target) | Back-link needed? |
|--------|--------|------------------------|-------------------|
| 00046_fusagu (塞ぐ) | 14872_fusagaru (塞がる) | intransitive | yes |
| 00097_hekomu (凹む) | へこます (forward ref) | transitive | n/a |
| 00405_togaru (尖る) | とがらせる (forward ref) | transitive | n/a |
| 00791_kowareru (壊れる) | 01241_kowasu (壊す) | transitive | already symmetric |
| 00800_nureru (濡れる) | 02386_nurasu (濡らす) | transitive | yes |
| 00903_tsuzuku (続く) | 01231_tsuzukeru (続ける) | transitive | already symmetric |
| 00904_ugoku (動く) | 01885_ugokasu (動かす) | transitive | yes |
| 00907_wareru (割れる) | 02334_waru (割る) | transitive | yes |
| 01117_modoru (戻る) | 02317_modosu (戻す) | transitive | yes |
| 01134_makeru (負ける) | 02569_make (負け) | noun form | yes |
| 01154_hieru (冷える) | 02403_hiyasu (冷やす) | transitive | yes |
| 01192_katazukeru (片付ける) | 02041_katazuku (片付く) | intransitive | yes |
| 01220_tsutaeru (伝える) | 01961_tsutawaru (伝わる) | intransitive | yes |
| 01231_tsuzukeru (続ける) | 00903_tsuzuku (続く) | intransitive | already symmetric |
| 01241_kowasu (壊す) | 00791_kowareru (壊れる) | intransitive | already symmetric |
| 01243_tooru (通る) | 02300_toosu (通す) | transitive | yes |
| 01263_oru (折る) | 01266_oreru (折れる) | intransitive | already symmetric |
| 01266_oreru (折れる) | 01263_oru (折る) | transitive | already symmetric |
| 02130_tamesu (試す) | 03410_tameshi (試し) | noun form | yes |
| 02569_make (負け) | 01134_makeru (負ける) | verb form | yes |
| 03410_tameshi (試し) | 02130_tamesu (試す) | verb form | yes |
| 03922_kezuru (削る) | けずれる (forward ref) | intransitive | n/a |
| 05541_burasagaru (ぶら下がる) | 10613_burasageru (ぶら下げる) | transitive | yes |
| 06048_haritsuku (張り付く) | 06855_haritsukeru (貼り付ける) | transitive | yes |
| 06088_tsukisasu (突き刺す) | 20293_tsukisasaru (突き刺さる) | intransitive | yes |
| 06193_hikisageru (引き下げる) | 05873_hikisagaru (引き下がる) | intransitive | yes |
| 06235_tsumikasaneru (積み重ねる) | 19542_tsumikasanaru (積み重なる) | intransitive | already symmetric |
| 06344_moriagaru (盛り上がる) | 07895_moriageru (盛り上げる) | transitive | yes |
| 06419_awadateru (泡立てる) | 17096_awadatsu (泡立つ) | intransitive | yes |
| 06624_amaeru (甘える) | 06625_amayakasu (甘やかす) | transitive | already symmetric |
| 06625_amayakasu (甘やかす) | 06624_amaeru (甘える) | intransitive | already symmetric |
| 06677_kogasu (焦がす) | 05344_kogeru (焦げる) | intransitive | yes |
| 06721_bareru (ばれる) | 11114_barasu (ばらす) | transitive | yes |
| 06797_toritsukeru (取り付ける) | とりつく (forward ref) | intransitive | n/a |
| 06980_omoiukaberu (思い浮かべる) | 07603_omoiukabu (思い浮かぶ) | intransitive | already symmetric |
| 07005_makiokoru (巻き起こる) | まきおこす (forward ref) | transitive | n/a |
| 07009_hanekaeru (跳ね返る) | はねかえす (forward ref) | transitive | n/a |
| 07382_nitsumaru (煮詰まる) | 09031_nitsumeru (煮詰める) | transitive | yes |
| 07384_kojireru (こじれる) | 22115_kojiraseru (こじらせる) | transitive | yes |
| 07417_hikkomu (引っ込む) | ひっこめる (forward ref) | transitive | n/a |
| 07600_yusaburu (揺さぶる) | 07601_yuragu (揺らぐ) | intransitive | already symmetric |
| 07601_yuragu (揺らぐ) | 07600_yusaburu (揺さぶる) | transitive | already symmetric |
| 07603_omoiukabu (思い浮かぶ) | 06980_omoiukaberu (思い浮かべる) | transitive | already symmetric |
| 07610_sebamaru (狭まる) | 07611_sebameru (狭める) | transitive | already symmetric |
| 07611_sebameru (狭める) | 07610_sebamaru (狭まる) | intransitive | already symmetric |
| 07896_yawaragu (和らぐ) | 07897_yawarageru (和らげる) | transitive | already symmetric |
| 07897_yawarageru (和らげる) | 07896_yawaragu (和らぐ) | intransitive | already symmetric |
| 08249_uruosu (潤おす) | 08181_uruou (潤う) | intransitive | yes |
| 10305_kabuseru (被せる) | 00709_kaburu (被る) | intransitive | yes |
| 10317_kuttsuku (くっつく) | 10331_kuttsukeru (くっつける) | transitive | yes |
| 10415_todomaru (留まる) | 10416_todomeru (留める) | transitive | already symmetric |
| 10416_todomeru (留める) | 10415_todomaru (留まる) | intransitive | already symmetric |
| 10496_hogusu (ほぐす) | 10503_hogureru (ほぐれる) | intransitive | yes |
| 11080_hikoku (被告) | 11085_genkoku (原告) | plaintiff | yes |
| 11262_hiiroo (ヒーロー) | 11278_hiroin (ヒロイン) | female counterpart | yes |
| 11412_midasu (乱す) | 11413_midare (乱れ) | noun form | already symmetric |
| 11413_midare (乱れ) | 11412_midasu (乱す) | verb form | already symmetric |
| 11718_kawaru (代わる) | 11717_kaeru (代える) | transitive | yes |
| 12982_shinrou (新郎) | 12981_shinpu (新婦) | bride | yes |
| 13167_kakeru (欠ける) | 13166_kaku (欠く) | transitive | yes |
| 13332_horobosu (滅ぼす) | 10881_horobiru (滅びる) | intransitive | yes |
| 13894_kantaiji (簡体字) | 13895_hantaiji (繁体字) | traditional characters | already symmetric |
| 13895_hantaiji (繁体字) | 13894_kantaiji (簡体字) | simplified characters | already symmetric |
| 15895_tayasu (絶やす) | 13814_taeru (絶える) | intransitive | yes |
| 17688_nenmatsu (年末) | 17689_nenshi (年始) | new year period | already symmetric |
| 17689_nenshi (年始) | 17688_nenmatsu (年末) | year-end period | already symmetric |
| 19542_tsumikasanaru (積み重なる) | 06235_tsumikasaneru (積み重ねる) | transitive | already symmetric |
| 19925_shimohanki (下半期) | 20412_kamihanki (上半期) | first half | yes |
| 19942_shunbun (春分) | 19657_shuubun (秋分) | autumnal equinox | yes |

Target-only entries that received a new back-link (26):

00709_kaburu, 01134_makeru (also a source above), 01885_ugokasu,
01961_tsutawaru, 02041_katazuku, 02130_tamesu (also a source above),
02300_toosu, 02317_modosu, 02334_waru, 02386_nurasu, 02403_hiyasu,
02569_make (also a source above), 03410_tameshi (also a source above),
05344_kogeru, 05873_hikisagaru, 06855_haritsukeru, 07895_moriageru,
08181_uruou, 09031_nitsumeru, 10331_kuttsukeru, 10503_hogureru,
10613_burasageru, 10881_horobiru, 11085_genkoku, 11114_barasu, 11278_hiroin,
11717_kaeru, 12981_shinpu, 13166_kaku, 13814_taeru, 14872_fusagaru,
17096_awadatsu, 19657_shuubun, 20293_tsukisasaru, 20412_kamihanki,
22115_kojiraseru.

### Notes
- The schema still allows `type: "pair"` in `cross_references`, but after
  this session there are 0 uses of it anywhere in the corpus. A future
  enhancement could remove `pair` from the allowed types in
  `build/constants.py` and the schema to prevent regressions.
- Pre-existing duplicate `conjugation` keys in 4,015 entry files remain
  untouched; they are a separate data-quality issue orthogonal to this
  migration. This was deliberately left alone to keep the migration
  commit focused.

### Next Entry
N/A — this was a migration session, not sequential.
