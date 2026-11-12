# Explore groups (Routine mode `explore-groups`)

The Explore page (`explore.html`) shows the dictionary as a word cloud: places,
each a sign with a dozen or so words around it, and lines between words that
cross-reference each other. Every semantic tag is a place to begin with, but a
tag is coarse ("Food & drink" has over 1,600 entries). This mode writes the
finer places: **curated groups** of roughly 6 to 40 entries that a learner
would want to see together, each with its own name.

An entry that is in a curated group leaves the tag-level places; the rest stay
where they were, so the page is complete after every cycle. Nothing in this
mode changes an entry, so §3 (mechanical pass) and §4 (self-check by an
independent model) of `prompts/routine2.md` do not apply. It spends nothing on
OpenRouter.

Files: `explore/groups/<tag>.json` (what you write, through the tool),
`explore/tags.json` (names of the tag-level places; rarely changes). Tool:
`python3 build/explore_groups.py` (its docstring has the plan format).

## One cycle

1. **Pick the tag.** `python3 build/explore_groups.py next` lists the tags that
   still hold ungrouped entries; take the first. A tag already begun comes
   first, then the tags with the most basic and core entries left.
2. **Read its worklist.**
   `python3 build/explore_groups.py worklist <tag> --limit 700 > /tmp/worklist.tsv`
   gives id, headword, reading, gloss, tier, part of speech and up to four
   cross-referenced headwords, basic and core entries first, cross-referenced
   entries next to each other. The header lists the groups the tag already
   has. Read the whole list before naming anything.
3. **Decide the groups** (rules below) and write them as a plan, in pieces of
   a few hundred entries: `/tmp/plan1.txt`, `/tmp/plan2.txt`, …
4. **Apply and check**, piece by piece:
   ```bash
   python3 build/explore_groups.py apply /tmp/plan1.txt
   python3 build/explore_groups.py validate
   python3 build/explore_groups.py show <tag>       # every group with its members' glosses
   ```
   Read the `show` output as a learner would: does every member belong under
   that sign? Move the ones that do not (edit `explore/groups/<tag>.json`
   directly for removals, then `validate` again).
5. **Unit of work**: about `params.approx_entries` (700) entries in a cycle. A
   small tag takes less: when one is finished, start the next. A big tag takes
   several cycles; the next cycle resumes it.
6. **Wrap up** as every cycle does (`routine2.md` §5–§7). Session log: the
   tag or tags, groups written, entries placed, and the `status` totals.
   PR title `routine(explore-groups): <tag>: N entries in M groups`.

## What makes a good group

- **A learner's set.** The members are words someone would study together or
  confuse with each other: kinds of rain; cooking methods; verbs of giving and
  receiving; a transitive verb and its intransitive partner; an idea and its
  opposite; a plain word and its honorific and humble forms; things found at a
  station. Topic, situation and relation are all good reasons. "Nouns" or
  "words that begin with か" are not.
- **Small and specific beats large and vague.** Aim for 6 to 40 members (the
  gate allows 3 to 45). If a group would pass 40, there are usually two groups
  in it.
- **Mix the levels.** Put the basic and core words in the group where the
  general words they anchor are: a learner flying into "Rain" should meet 雨
  next to 梅雨, 夕立 and 土砂降り.
- **Name it the way a sign would.** Japanese first: a natural word or short
  phrase, furigana on every kanji (`{雨|あめ}`), preferably a word the
  dictionary has. English: 28 characters at most, sentence case, plain
  ("Rain", "Getting on and off", "Polite verbs"). A name is unique within its
  tag file.
- **One group is the default; up to three is allowed** when an entry truly
  belongs in each (桜 in "Trees" and in "Spring"). Members do not have to
  carry the file's tag: 傘 may sit in weather's "Rain" even though it is
  tagged as a tool. Find another entry's id with
  `python3 build/check_duplicate.py --skip-candidates "語" "ご"` or in
  `build/word_id_lookup.json`.
- **Use the gloss, and the entry when the gloss is not enough.** A kana
  headword or a short gloss can hide a different word; open the entry before
  placing anything you are not sure of.
- **Leftovers are allowed, in moderation.** An entry that fits no group goes
  under a `== (none)` line in the plan. It stays at tag level, is still shown
  on the page, and is not offered again (the file's `leftover` list). Keep
  leftovers under about one entry in twenty; do not invent a "Miscellaneous"
  group to hide them. Every entry of the worklist ends in a group or under
  `== (none)`: an entry you simply skip comes back next cycle.
- **Extend before you add.** When the tag already has a group the entry fits,
  put it there (`== <group id>` with no names). Later cycles, when new entries
  arrive, are mostly this.

If you notice a wrong gloss, tag or reading while reading the worklist, do not
fix it here: log it as an `[entry]` observation in `polishing/observations.md`.
