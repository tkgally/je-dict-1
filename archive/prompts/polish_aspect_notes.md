# Polish Aspect/ている Notes

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Add ている documentation to verb entries where the ている form has non-obvious meaning. This is a **semantic task** that requires your knowledge of Japanese aspect — it cannot be automated because determining whether a verb's ている meaning is "obvious" (ongoing action) or requires explanation (resultative state, experiential, habitual, etc.) demands native-level judgment.

## Task Focus

**Single focus**: Does the verb entry document its ている behavior when that behavior is non-obvious?

For each verb entry, determine:
1. Is ている usage non-obvious for this verb?
2. If yes, is it already documented in the notes?
3. If not documented, add an ASPECT section explaining the ている meaning.

## Starting Point

```bash
cat polishing/tasks/aspect-notes/progress.txt
```

Find the first entry file that starts with that number.

## Which Verbs Need ている Documentation

### ALWAYS document (non-obvious ている meaning):

**Resultative state** — ている indicates a state resulting from a completed action, not an ongoing action:
- {結婚|けっこん}する → {結婚|けっこん}している = "is married" (not "is marrying")
- {死|し}ぬ → {死|し}んでいる = "is dead" (not "is dying")
- {座|すわ}る → {座|すわ}っている = "is seated" (not "is sitting down")
- {立|た}つ → {立|た}っている = "is standing" (not "is standing up")
- {持|も}つ → {持|も}っている = "has/possesses" (not "is picking up")
- {着|き}る → {着|き}ている = "is wearing" (not "is putting on")
- {住|す}む → {住|す}んでいる = "lives (somewhere)" (not "is moving in")
- {知|し}る → {知|し}っている = "knows" (not "is learning")
- {太|ふと}る → {太|ふと}っている = "is fat" (not "is getting fat")
- {痩|や}せる → {痩|や}せている = "is thin" (not "is getting thin")
- {開|あ}く → {開|あ}いている = "is open" (not "is opening")
- {閉|し}まる → {閉|し}まっている = "is closed" (not "is closing")
- {壊|こわ}れる → {壊|こわ}れている = "is broken" (not "is breaking")
- {決|き}まる → {決|き}まっている = "is decided" (not "is being decided")
- {似|に}る → {似|に}ている = "resembles" (not "is becoming similar")
- {慣|な}れる → {慣|な}れている = "is accustomed" (not "is getting used to")
- {疲|つか}れる → {疲|つか}れている = "is tired" (not "is tiring")
- {落|お}ちる → {落|お}ちている = "is lying on the ground" (not "is falling")
- {並|なら}ぶ → {並|なら}んでいる = "is lined up" (not "is lining up")
- {曲|ま}がる → {曲|ま}がっている = "is bent/curved" (not "is bending")
- {混|こ}む → {混|こ}んでいる = "is crowded" (not "is getting crowded")

**Knowledge/cognitive state** — ている indicates a current mental state:
- {知|し}る → {知|し}っている = "knows"
- {覚|おぼ}える → {覚|おぼ}えている = "remembers"
- {信|しん}じる → {信|しん}じている = "believes"

**Experience/record** — ている indicates past experience with current relevance:
- {行|い}く → {行|い}ったことがある is the standard experiential, but {行|い}っている can mean "has gone (and is still there)"
- {読|よ}む → {読|よ}んでいる can mean "has read (and retains the knowledge)" in some contexts

**Habitual** — ている indicates habitual/repeated action (document when this is the primary meaning):
- {勤|つと}める → {勤|つと}めている = "works at / is employed at" (habitual, not in-progress)
- {通|かよ}う → {通|かよ}っている = "commutes to / attends regularly"

### SKIP (obvious ている meaning — ongoing action):
- {食|た}べている = "is eating" — obvious progressive
- {走|はし}っている = "is running" — obvious progressive
- {書|か}いている = "is writing" — obvious progressive
- {話|はな}している = "is talking" — obvious progressive

**Rule of thumb**: If an intermediate learner would naturally guess "is doing X" and be correct, skip it. If they would guess "is doing X" but the real meaning is "is in state X" or "has done X," document it.

## ASPECT Note Format

Add an ASPECT section to the notes field. If the entry already has notes, append the ASPECT section. If the entry has no notes, create notes with an introductory sentence followed by the ASPECT section.

**Format when notes already exist** — append after existing content:

```
[existing notes content]

ASPECT (ている):
- [verb]ている: [meaning in English] ([aspect type])
- [Additional ている forms if relevant, e.g., ていた, ていない]
- Note: [any important clarification for learners]
```

**Format when creating new notes** — include an introductory line:

```
[Brief introductory sentence about the verb.]

ASPECT (ている):
- [verb]ている: [meaning in English] ([aspect type])
- Note: [any important clarification for learners]
```

### Example ASPECT Sections

**For 結婚する:**
```
ASPECT (ている):
- {結婚|けっこん}している: is married (resultative state, not ongoing action)
- {結婚|けっこん}していない: is not married / is single
- Note: The {結婚|けっこん}している form describes the current state of being married, not the act of getting married. To describe the wedding event in progress, use {結婚|けっこん}{式|しき}をしている.
```

**For 知る:**
```
ASPECT (ている):
- {知|し}っている: knows (state of knowledge)
- {知|し}らない: does not know (negative uses plain form, NOT {知|し}っていない)
- Note: {知|し}る in plain form means "to come to know / to find out" (punctual). The ている form is far more common in everyday speech. The negative is irregular: use {知|し}らない, not {知|し}っていない.
```

**For 死ぬ:**
```
ASPECT (ている):
- {死|し}んでいる: is dead (resultative state)
- Note: Describes the state of being dead, not the process of dying. For "is dying," use {死|し}にかけている or {死|し}にそう.
```

**For 持つ:**
```
ASPECT (ている):
- {持|も}っている: has, possesses, is holding (resultative state)
- Note: {持|も}っている is the standard way to express possession in Japanese, equivalent to English "have." The plain form {持|も}つ emphasizes the act of picking up or grabbing.
```

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Process entries sequentially by ID**:
   - Read the entry file
   - Check `metadata.tags.pos` — skip if not a verb (`verb-godan`, `verb-ichidan`, `verb-suru`, `verb-kuru`, `verb-irregular`)
   - If it is a verb, determine if ている behavior is non-obvious
   - If non-obvious and not already documented: add ASPECT section to notes
   - If already documented (entry already contains "ASPECT" in notes) or behavior is obvious: skip

3. **For each modified entry**:

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```
   Update the `modified` field in `metadata` with this timestamp.

   **CRITICAL - Furigana requirement**:
   All kanji in the ASPECT section must have furigana: `{漢字|かんじ}`.

4. **After every ~25 entries checked** (or when you accumulate changes):
   - Update `polishing/tasks/aspect-notes/progress.txt` with the next entry number
   - Validate and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Aspect notes: check entries XXXXX-XXXXX"
     ```
     **In parallel mode**: Replace `git add -A` with `git add entries/ polishing/sessions/` to avoid staging shared files.

5. **When finishing** (end of session or context getting long):
   a. Update `polishing/tasks/aspect-notes/progress.txt`
   b. Write session log to `polishing/sessions/aspect-notes_{date}_{nnn}.md`:
      ```
      ## Session: Aspect/ている Notes
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX
      Verbs checked: N
      Verbs modified: M

      ### Changes Made
      - [entry_id] [headword]: Added ASPECT section — [brief description]

      ### Skipped (already documented)
      - [entry_id] [headword]: Already has ASPECT section

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes

## Why This Cannot Be Automated

Determining aspect behavior requires deep knowledge of Japanese:
- **Telic vs. atelic**: Whether a verb has an inherent endpoint determines ている meaning
- **Context sensitivity**: Some verbs have different ている meanings depending on context (e.g., {着|き}る: "is wearing" vs. "is putting on" depending on aspect interpretation)
- **Learner confusion potential**: Judging which verbs will confuse learners requires pedagogical awareness
- **Note quality**: Writing clear, accurate explanations requires understanding both languages
- **Existing documentation check**: Recognizing whether aspect is already adequately covered in existing notes requires reading comprehension

## Quality Checklist

Before saving each modified entry:
- [ ] ASPECT section follows the standard format
- [ ] ている meaning is accurately described
- [ ] Aspect type is correctly identified (resultative, habitual, experiential, etc.)
- [ ] All kanji have furigana in the ASPECT section
- [ ] Negative forms noted where irregular (e.g., {知|し}らない)
- [ ] Explanations are clear for intermediate learners
- [ ] `modified` timestamp updated
- [ ] Existing notes content preserved (ASPECT section appended, not replacing)

## Progress Update Format

Keep the progress file minimal:
```
next: XXXXX
```

## Parallel Execution Mode

This task supports parallel execution when given an explicit ID range. Two or more sessions can run this task simultaneously on non-overlapping ID ranges.

### How to invoke

When starting the session, specify a range:
> "Process entries 10000-10499 only."

### Behavior in parallel mode

When an ID range is given:
1. **Ignore** `progress.txt` — do not read it or update it
2. **Process only** entry files whose numeric ID falls within the given range (inclusive)
3. **Skip shared-file updates**: do NOT run `update_indexes.py`, `build_flat.py`, or `update_kanji_index.py`
4. **Commit entry changes only**: `git add entries/ polishing/sessions/ && git commit -m "..."`
5. **Do NOT run `make build`** — a coordinator will do this after all parallel sessions complete
6. **Do NOT push to main** — push to a feature branch and create a PR, but do NOT merge it. The coordinator will handle merging.

### After parallel sessions complete

A coordinator step (run manually or via `build/parallel_coordinator.py`) will:
1. Merge all parallel session branches
2. Run `update_indexes.py`, `build_flat.py`, and other shared-file regeneration
3. Create a single combined PR

### When NO range is given

Operate in **legacy sequential mode**: read `progress.txt`, process entries sequentially from that point, update `progress.txt`, and run `make build` as usual. This is the default behavior.

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow." The key points:

1. **Run `make build` BEFORE the final commit** so that `docs/` and all build artifacts are included
2. **`git add -A`** to stage everything (entries, docs, indexes, progress file, session log, etc.)
3. **Commit and push** to the feature branch
4. **Create a PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "Polish: aspect/ている notes for entries XXXXX-XXXXX" --body "..."`
5. **Wait for CI** with a single blocking call: `gh pr checks <number> --repo tkgally/je-dict-1 --watch --fail-fast` (exits 0 on success, non-zero on failure). Do NOT wrap this in a `while`/`sleep`/`curl` polling loop — `--watch` already waits, and hand-rolled streaming loops get routed through the `Monitor` tool (separate permission grant) which will deadlock an unattended session.
6. **Squash-merge the PR** once all checks are green
7. **If CI fails**: read the error, fix the issue, push again, and repeat from step 5
8. **Post-merge cleanup**: switch to main, pull, verify clean state, delete feature branch locally and remotely

**CRITICAL**: The PR must include rebuilt `docs/` files. If you commit entry changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.

## Output at Session End

When stopping (user request or context reset), report:
1. Entry range checked
2. Number of verb entries examined
3. Number of entries modified with ASPECT notes
4. Summary of aspect types documented
5. Next entry to continue from
