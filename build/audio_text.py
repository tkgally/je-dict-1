"""Deterministic text side of the example-audio workflow (AUDIO_WORKFLOW.md §3–§4, §6).

Everything here is pure computation: no network, no files except the reading
index. MeCab (fugashi + unidic-lite) is imported lazily, so the site build can
import `text_hash` and `parse_example` without the audio dependencies.

- parse_example(raw)          markup → displayed text, expected reading, tokens, flags
- undetermined_reason(p)      why an example cannot be recorded yet (or None)
- text_hash(raw)              the hash a recording is valid for
- phonetic_kana(s)            expected reading with particles は/へ/を as わ/え/お
- kana_substituted(s, major)  prompt E transcript: rare-reading words in hiragana
- build_tts_prompt(s, major)  the full TTS prompt (strategy E, "kanadict")
- norm_kana / loose / distance / to_kana   normalization used by the scoring

Ported from audio-reference/scripts/{common,evaluate,verify,prompts}.py; the
logic is unchanged unless AUDIO_WORKFLOW.md's changelog says otherwise.
"""
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------- markup
# Link markup:     ⟦display→lemma：entry_id⟧   (display may itself hold furigana)
# Furigana markup: {base|reading}
LINK_INNER = re.compile(r"⟦([^⟦⟧]*?)→[^⟦⟧]*?⟧")
FURI = re.compile(r"\{([^{}|]+)\|([^{}|]+)\}")
KANJI = re.compile(r"[㐀-鿿豈-﫿々〆ヶ]")
DIGITS = re.compile(r"[0-9０-９]")
LATIN = re.compile(r"[A-Za-zＡ-Ｚａ-ｚ]")


def strip_links(s):
    """Replace every link ⟦display→lemma：id⟧ by its display text (nested links too)."""
    prev = None
    while prev != s:
        prev, s = s, LINK_INNER.sub(lambda m: m.group(1), s)
    return s


def text_hash(raw):
    """SHA-256 (hex) of the example with link markup removed and furigana kept.

    A recording is valid while this hash is unchanged. Links are excluded
    because the linker adds and removes them without changing what is said;
    furigana are included because they decide the reading.
    """
    return hashlib.sha256(strip_links(raw or "").encode("utf-8")).hexdigest()


def parse_example(raw):
    """Parse a dictionary example into the fields the pipeline needs.

    Returns plain (displayed text), kana (expected reading), tokens
    ([base, reading-or-None], in order), segments ((base, reading) furigana
    pairs), and flags malformed / bare_kanji / has_digits / has_latin.
    """
    s = strip_links(raw)
    malformed = any(c in s for c in "⟦⟧→")
    segs = [(m.group(1), m.group(2)) for m in FURI.finditer(s)]
    plain = FURI.sub(lambda m: m.group(1), s)
    kana = FURI.sub(lambda m: m.group(2), s)
    tokens, pos = [], 0
    for m in FURI.finditer(s):
        if m.start() > pos:
            tokens.append([s[pos:m.start()], None])
        tokens.append([m.group(1), m.group(2)])
        pos = m.end()
    if pos < len(s):
        tokens.append([s[pos:], None])
    malformed = malformed or "{" in plain or "}" in plain or "|" in plain
    return {
        "plain": plain,
        "kana": kana,
        "alt_kana": [],
        "segments": segs,
        "tokens": tokens,
        "malformed": malformed,
        "bare_kanji": bool(KANJI.search(kana)),
        "has_digits": bool(DIGITS.search(plain)),
        "has_latin": bool(LATIN.search(plain)),
        "manual_reading": False,
    }


def undetermined_reason(p):
    """Why the expected reading of a parsed example is not fully determined,
    or None when it is. Order matters: the first problem found is reported."""
    if p["malformed"]:
        return "malformed"
    if p["bare_kanji"]:
        return "bare-kanji"
    if p["has_digits"]:
        return "digits"
    if p["has_latin"]:
        return "latin"
    if not p["plain"].strip():
        return "empty"
    return None


# --------------------------------------------------------------------------- normalization
def kata2hira(s):
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)


def norm_text(s):
    """NFKC; keep letters and digits only (drops punctuation, spaces, symbols)."""
    s = unicodedata.normalize("NFKC", s)
    return "".join(c for c in s if unicodedata.category(c)[0] in "LN")


VOWEL = {c: v for row, v in (("あかさたなはまやらわがざだばぱぁゃ", "あ"),
                              ("いきしちにひみりぎじぢびぴぃ", "い"),
                              ("うくすつぬふむゆるぐずづぶぷぅゅ", "う"),
                              ("えけせてねへめれげぜでべぺぇ", "え"),
                              ("おこそとのほもよろをごぞどぼぽぉょ", "お")) for c in row}


def expand_choon(s):
    """ー → the vowel of the preceding kana (こーひー → こおひい)."""
    out = ""
    for c in s:
        out += VOWEL.get(out[-1], "") if c == "ー" and out else c
    return out


def norm_kana(s):
    """Katakana → hiragana, NFKC, ー expanded, ぢ/づ → じ/ず, letters and digits only."""
    s = kata2hira(unicodedata.normalize("NFKC", s))
    s = expand_choon(s).replace("ぢ", "じ").replace("づ", "ず")
    return "".join(c for c in s if unicodedata.category(c)[0] in "LN")


def loose(k):
    """Pronunciation-level folding applied to both sides of a comparison:
    particles は/へ/を as わ/え/お, ゔ as ぶ, and long vowels spelled う/い after
    o-/e-row kana (こう→こお, けい→けえ)."""
    k = k.replace("を", "お").replace("は", "わ").replace("へ", "え").replace("ゔ", "ぶ")
    out = ""
    for c in k:
        v = VOWEL.get(out[-1]) if out else None
        out += "お" if c == "う" and v == "お" else "え" if c == "い" and v == "え" else c
    return out


def distance(a, b):
    """Levenshtein distance."""
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


# --------------------------------------------------------------------------- digits, Latin letters
LETTERS = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                   "エー ビー シー ディー イー エフ ジー エイチ アイ ジェー ケー エル エム "
                   "エヌ オー ピー キュー アール エス ティー ユー ブイ ダブリュー エックス ワイ ゼット".split()))
SPECIAL = {"Wi-Fi": "ワイファイ", "WiFi": "ワイファイ", "wifi": "ワイファイ",
           "%": "パーセント", "％": "パーセント"}
DIG = "〇一二三四五六七八九"


def num2kanji(n):
    """Integer → kanji numerals (1234 → 千二百三十四)."""
    if n == 0:
        return "零"
    out = ""
    for unit, size in (("兆", 10**12), ("億", 10**8), ("万", 10**4), ("", 1)):
        g, n = divmod(n, size)
        if not g:
            continue
        s = ""
        for u, v in (("千", 1000), ("百", 100), ("十", 10)):
            d, g = divmod(g, v)
            if d:
                s += ("" if d == 1 else DIG[d]) + u
        if g:
            s += DIG[g]
        out += s + unit
    return out


def norm_numbers(s):
    """NFKC; thousands separators dropped; % → パーセント; digits → kanji numerals."""
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    s = s.replace("%", "パーセント")
    return re.sub(r"\d+", lambda m: num2kanji(int(m.group())), s)


def latin_to_kana(text):
    for k, v in SPECIAL.items():
        text = text.replace(k, v)
    return re.sub(r"[A-Za-z]{1,6}",
                  lambda m: "".join(LETTERS.get(c.upper(), c) for c in m.group()), text)


# --------------------------------------------------------------------------- MeCab
_TAGGER = None


def tagger():
    """The shared MeCab tagger (fugashi + unidic-lite), created on first use."""
    global _TAGGER
    if _TAGGER is None:
        import fugashi  # noqa: WPS433 (lazy: only the audio pipeline needs it)
        _TAGGER = fugashi.Tagger()
    return _TAGGER


def mecab_available():
    try:
        tagger()
        return True
    except Exception:  # ImportError, or unidic-lite missing
        return False


def to_kana(text):
    """Kana reading of arbitrary text by MeCab/UniDic (digits and Latin letters converted)."""
    text = norm_numbers(text)
    for k, v in SPECIAL.items():
        text = text.replace(k, v)
    out = []
    for w in tagger()(text):
        kana = w.feature.kana
        if kana:
            out.append(kana)
        elif re.fullmatch(r"[A-Z]{1,6}", w.surface):
            out.append("".join(LETTERS[c] for c in w.surface))
        else:
            out.append(w.surface)
    return norm_kana("".join(out))


# --------------------------------------------------------------------------- phonetic reading
PARTICLE_SOUND = {"は": "わ", "へ": "え", "を": "お"}


def phonetic_kana(s):
    """The expected reading with the particles は/へ/を written as pronounced (わ/え/お).

    Particles are MeCab tokens with pos1 助詞 in the displayed text. They never
    carry furigana, so they map one-to-one onto the reading. For hand-written
    readings (manual_reading: digits, Latin letters) each particle is placed at
    the occurrence nearest to where the reading of the preceding text ends.
    """
    plain = "".join(b for b, _ in s["tokens"])
    ppos, pos = set(), 0
    for w in tagger()(plain):
        start = plain.index(w.surface, pos)
        pos = start + len(w.surface)
        if w.feature.pos1 == "助詞" and w.surface in PARTICLE_SOUND:
            ppos.add(start)
    if s.get("manual_reading"):
        kana = s["kana"]
        for j in sorted(ppos):
            ch, est = plain[j], len(to_kana(plain[:j]))
            hits = [k for k, c in enumerate(kana) if c == ch]
            if hits:
                k = min(hits, key=lambda k: abs(k - est))
                kana = kana[:k] + PARTICLE_SOUND[ch] + kana[k + 1:]
        return kana
    out, pos = "", 0
    for base, reading in s["tokens"]:
        if reading:
            out += reading
        else:
            out += "".join(PARTICLE_SOUND[c] if pos + i in ppos else c
                           for i, c in enumerate(base))
        pos += len(base)
    return out


# --------------------------------------------------------------------------- reading index
def build_reading_index(examples_raw):
    """Spelling → Counter(reading) over the furigana of the given example texts."""
    readings = defaultdict(Counter)
    for raw in examples_raw:
        for base, rd in parse_example(raw)["segments"]:
            readings[base][rd] += 1
    return readings


def majority_readings(index):
    """Spelling → its most frequent reading, for spellings with more than one reading."""
    return {b: max(c, key=c.get) for b, c in index.items() if len(c) > 1}


def load_majority(path=None):
    """Majority readings from a saved reading index (spelling → {reading: count})."""
    idx = json.loads(Path(path).read_text(encoding="utf-8"))
    return {b: max(c, key=c.get) for b, c in idx.items() if len(c) > 1}


def minority_reading(base, reading, majority):
    """True if the dictionary's furigana give this spelling another reading more often."""
    return base in majority and majority[base] != reading


# --------------------------------------------------------------------------- prompt E
def kana_substituted(s, majority=None):
    """The displayed sentence with every word whose intended reading is not its
    usual one written in hiragana: (a) its furigana reading differs from what
    MeCab/UniDic reads in context, or (b) with `majority` given, its reading is
    a minority reading of that spelling in the dictionary (私＝わたくし).

    Regions are the smallest spans on which furigana groups and MeCab tokens
    align, so okurigana stay with their word. A word right after a digit
    (1泊, 3本) is left to the TTS.
    """
    segs, pos, plain = [], 0, ""
    for base, reading in s["tokens"]:
        segs.append((pos, pos + len(base), reading))
        pos += len(base)
        plain += base
    tokens, tpos = [], 0
    for w in tagger()(plain):
        start = plain.index(w.surface, tpos)
        tokens.append((start, start + len(w.surface), w.feature.kana or ""))
        tpos = start + len(w.surface)
    bounds_s = {0, len(plain)} | {a for a, _, _ in segs} | {b for _, b, _ in segs}
    bounds_t = {0, len(plain)} | {a for a, _, _ in tokens} | {b for _, b, _ in tokens}
    cuts = sorted(bounds_s & bounds_t)
    out = ""
    for lo, hi in zip(cuts, cuts[1:]):
        inside = [x for x in segs if x[0] >= lo and x[1] <= hi]
        if not any(r for _, _, r in inside):
            out += plain[lo:hi]
            continue
        fur = "".join(r if r else plain[a:b] for a, b, r in inside)
        ana = "".join(k for a, b, k in tokens if a >= lo and b <= hi)
        after_digit = lo > 0 and plain[lo - 1].isdigit()
        differs = loose(norm_kana(fur)) != loose(norm_kana(ana))
        if majority is not None:
            differs = differs or any(r and minority_reading(plain[a:b], r, majority)
                                     for a, b, r in inside)
        out += fur if differs and not after_digit else plain[lo:hi]
    return out


PROMPT_E = """# AUDIO PROFILE: Narrator for a Japanese-English learner's dictionary
## DIRECTOR'S NOTES
Style: Clear, natural, neutral standard Japanese (Tokyo accent) at a moderate pace suitable for learners. Read the transcript exactly once, adding and omitting nothing.
Pronunciation: Pronounce every word exactly as written in the READING line below. The READING line is only a pronunciation guide; do not speak it separately.
READING: {kana}
## TRANSCRIPT
{transcript}"""


def build_tts_prompt(s, majority):
    """Prompt strategy E ("kanadict"): director's notes, READING line, and the
    transcript with rare-reading words in hiragana."""
    return PROMPT_E.format(kana=s["kana"], transcript=kana_substituted(s, majority))
