# Polish Example Sentences — Low-Index Catch-Up (One-Time Task)

These entries were missed by the regular example-sentences polishing pass and need their examples brought up to the minimum 3-per-sense standard. Follow the same procedures as `prompts/polish_example_sentences.md` but **only for the specific entries listed below**.

## Task Focus

**Single focus**: Bring every sense in each listed entry up to the minimum example count, applying all quality checks along the way.

For each entry, check:
1. **Count**: Minimum 3 examples per sense (or 5 for basic/core tier entries)
2. **Vocabulary levels**: Tier restrictions for basic and core entries
3. **Appropriateness**: Natural, useful examples with progressive length

Load the skill file for detailed requirements:
```
.claude/skills/example-sentences/SKILL.md
```

## Target Entries

Work through the following entries **in the order listed**. Every one of these has at least one sense with fewer than 3 examples.

```
00001_amaru
00002_amu
00003_anmari
00004_aogu
00005_appu
00007_auto
00013_benchi
00014_biyou
00016_booi
00022_bureeki
00027_chijimu
00029_chikajika
00030_chikau
00032_daiya
00035_daun
00042_fugou
00053_gakka
00056_gakunen
00065_genni
00073_gomu
00075_gurando
00081_hagasu
00094_hau
00098_hibiki
00099_hibiku
00102_hineru
00103_hiniku
00105_hirosa
00113_hoomu
00114_horu
00115_hosu
00117_igi
00124_jikani
00132_kadai
00133_kagiri
00141_kaiten
00145_kaizou
00149_kakine
00156_kakudo
00160_kakuu
00161_kamisama
00166_kanban
00185_kantoku
00187_kanzume
00200_katamuku
00202_katsuji
00206_kehai
00211_keishiki
00268_mainasu
00305_nao
00312_nerai
00315_nibui
00321_niwaka
00325_noudo
00326_nuu
00328_ogamu
00329_oginau
00338_paipu
00339_pairotto
00340_pasu
00344_pin
00345_puran
00346_purasu
00350_raitaa
00352_reberu
00353_roketto
00357_sakari
00358_sakasa
00360_setsu
00394_sutando
00408_toreeningu
00410_tsubusu
00413_uku
00414_urami
00416_uwa
00417_uyamau
00421_wata
00423_yakume
00424_yo
00425_yomi
00430_yurui
00431_yuu
00435_zettai
00439_arai
00440_bu
00442_horu
00452_nan
00460_shuushoku
00462_tomo
00466_arai
00472_shiyou
01138_yakeru
01139_hou
01229_kikoeru
01274_asai
```

Total: 94 entries.

## Workflow

1. **Read each entry** from the list above in order

2. **For each entry**:
   - Count examples per sense against tier requirements
   - For basic/core entries, verify vocabulary restrictions
   - Check progressive length (shorter to longer)
   - Evaluate naturalness and usefulness

   If issues found: Fix or add examples, update `modified` timestamp, save

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

3. **After every ~20 entries** (or when you make changes):
   - Validate and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Example sentences: fix low-index entries XXXXX-XXXXX"
     ```

4. **When finishing** (end of session or context getting long):
   a. Write session log to `polishing/sessions/example-sentences_{date}_{nnn}.md`:
      ```
      ## Session: Example Sentences — Low-Index Catch-Up
      Date: YYYY-MM-DD
      Entries checked: (list or range)

      ### Changes Made
      - [entry_id]: [issue type] - [brief description]

      ### Remaining
      (list any entries not yet processed, or "All 94 entries complete")
      ```
   b. Commit all changes

## Progress Tracking

This is a one-time task with a fixed list. Do **not** update `polishing/tasks/example-sentences/progress.txt` — that file tracks the regular sequential polishing pass.

Instead, track progress within this prompt: cross off entries as you go by noting where you stopped in your session log. If the task spans multiple sessions, each session should pick up from where the previous session's log says it left off.

## Requirements Summary

Refer to `prompts/polish_example_sentences.md` for the full requirements tables:
- Minimum counts by tier (3 for general, 5 for basic/core)
- Vocabulary restrictions by tier
- Progressive length targets
- Example format (`{entry_id}_ex{N}`, furigana on all kanji, valid sense_numbers)

## Reminders

- Do NOT add inline word links (⟦...⟧) in this task. Links are added separately.
- All kanji must have furigana: `{漢字|かんじ}`
- Run `python3 build/get_timestamp.py` immediately before saving each modified entry
- Delete this prompt file once all 94 entries are complete — it is not needed after that.
