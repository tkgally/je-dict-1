"""The TTS prompting strategies (A–C as planned; D added after the first results).

plain     – the sentence exactly as displayed in the dictionary, no instructions.
furigana  – structured "director's notes" prompt (the format Google recommends
            for Gemini TTS) whose transcript has every furigana reading inserted
            in parentheses after its kanji, e.g. 今日（こんにち）.
guided    – the same structured prompt, but the transcript is the sentence as
            displayed and the full hiragana reading is given in a READING line.
kana      – (added after the first results) as guided, but in the transcript
            every word whose furigana reading differs from what MeCab/UniDic
            would read is written in hiragana (今日→こんにち).  The words are
            chosen automatically, so this scales to the whole dictionary.
Second round, aiming at near-zero errors:
kanadict        – E: as D, but a word is also written in kana when its reading
                  is not the most common reading of that spelling in the
                  dictionary's own furigana (私→わたくし, 年月→としつき).
kanadict_noread – F: E's transcript and director's notes, no READING line
                  (C and D occasionally read the sentence twice).
allkana         – G: director's notes; the whole transcript in kana.
kanadict_bare   – H: E's transcript alone, no instructions.
"""

STRATEGIES = ["plain", "furigana", "guided", "kana"]
# second round (aiming at near-zero errors): E–H
STRATEGIES_2 = ["kanadict", "kanadict_noread", "allkana", "kanadict_bare"]

STRATEGY_LABELS = {
    "plain": "A. Plain text",
    "furigana": "B. Inline readings",
    "guided": "C. Director's notes + full reading",
    "kana": "D. As C + rare readings in kana",
    "kanadict": "E. As D, kana chosen by dictionary",
    "kanadict_noread": "F. As E without READING line",
    "allkana": "G. Whole sentence in kana",
    "kanadict_bare": "H. E's transcript, no instructions",
}

# First pilot version of strategy B.  Both models read these instructions aloud
# in all 6 pilot clips, so B was moved into the same structured format as C.
UNSTRUCTURED_FURIGANA_INSTRUCTION = (
    "Read the following Japanese sentence aloud, clearly and naturally, as a "
    "narrator for a Japanese learner's dictionary. The hiragana in parentheses "
    "after kanji shows how those kanji must be pronounced. Do not read the "
    "parenthesized hiragana as extra words; use it only as the pronunciation of "
    "the kanji before it. Say only the sentence.\n\n"
)

HEADER = """# AUDIO PROFILE: Narrator for a Japanese-English learner's dictionary
## DIRECTOR'S NOTES
Style: Clear, natural, neutral standard Japanese (Tokyo accent) at a moderate pace suitable for learners. Read the transcript exactly once, adding and omitting nothing.
"""

FURIGANA_TEMPLATE = HEADER + """Pronunciation: In the transcript, the hiragana in parentheses after kanji shows how those kanji are pronounced. Do not read the parenthesized hiragana aloud as separate words.
## TRANSCRIPT
{annotated}"""

GUIDED_TEMPLATE = HEADER + """Pronunciation: Pronounce every word exactly as written in the READING line below. The READING line is only a pronunciation guide; do not speak it separately.
READING: {kana}
## TRANSCRIPT
{plain}"""


NOREAD_TEMPLATE = HEADER + """## TRANSCRIPT
{plain}"""


def annotated(tokens):
    return "".join(b if r is None else f"{b}（{r}）" for b, r in tokens)


def build_prompt(strategy, s):
    if strategy == "plain":
        return s["plain"]
    if strategy == "furigana":
        return FURIGANA_TEMPLATE.format(annotated=annotated(s["tokens"]).strip())
    if strategy == "kana":
        from evaluate import kana_substituted
        return GUIDED_TEMPLATE.format(kana=s["kana"], plain=kana_substituted(s))
    if strategy in ("kanadict", "kanadict_noread", "kanadict_bare"):
        from evaluate import kana_substituted
        t = kana_substituted(s, dict_rule=True)
        if strategy == "kanadict":
            return GUIDED_TEMPLATE.format(kana=s["kana"], plain=t)
        return NOREAD_TEMPLATE.format(plain=t) if strategy == "kanadict_noread" else t
    if strategy == "allkana":
        return NOREAD_TEMPLATE.format(plain=s["kana"])
    if strategy == "furigana_unstructured":
        return UNSTRUCTURED_FURIGANA_INSTRUCTION + annotated(s["tokens"]).strip()
    if strategy == "guided":
        return GUIDED_TEMPLATE.format(kana=s["kana"], plain=s["plain"])
    raise ValueError(strategy)
