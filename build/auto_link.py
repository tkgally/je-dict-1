#!/usr/bin/env python3
"""Deterministic inline-link tool: add ``⟦surface→base：entry_id⟧`` links to unlinked Japanese text.

Scope
-----
Touches only ``examples[].japanese`` and ``notes``.  Existing links, furigana
wrappers, punctuation, English prose and everything else are preserved
verbatim; the only change is that some tokens get wrapped in link markup.  The
tool is precision-first: anything ambiguous is left alone and counted in the
report under a reason.  ``noentry`` markers are never emitted.

Resolution rules (in the order they are tried for a span of tokens)
-------------------------------------------------------------------
0. Never link: the entry's own headword (its headword string, reading, and every
   form in its own conjugation table; multi-word headwords are also locked as a
   token sequence so conjugated variants are caught); text already inside a
   ⟦…⟧ link; punctuation; ``〜``/``…`` placeholders; digits and Latin text;
   single hiragana characters that are not table particles; Sudachi
   補助記号/空白 tokens; ALL-CAPS section-header lines in notes (``USAGE:``).
1. Furigana-wrapped kanji word (plus attached okurigana / auxiliary chain):
   the entry whose furigana-stripped headword equals the base form AND whose
   reading equals the base reading (wrapper readings + kana), or whose
   conjugation table generates the exact surface with the same reading.
   Conjugated verbs/adjectives link with the whole auxiliary chain as the
   surface (``{食|た}べさせられました``) and the entry headword as base; the
   base reading is computed by aligning the surface with Sudachi's
   dictionary form (``{書|か}いた`` + ``書く`` -> ``かく``).
2. Katakana run: exact headword match with reading agreement.
3. Function words from the ``inline-word-links`` skill table (kana rows only).
   Particles link individually — ``には`` is ``⟦に→に⟧⟦は→は⟧``, the convention
   of 734 vs 6 hand-linked cases; likewise ``では``/``とは``/``にも``.  The
   combined entries ``でも``/``では`` are used only sentence-initially.  ``に``
   after a na-adjective (``静かに``) is linked (475 vs 13 hand-linked cases);
   copula ``で``/``な``/``だ``/``です`` are not (``--copula`` opts in for
   だ/です/でしょう).  Table verbs (する/いる/ある/なる/できる/…) also cover
   their conjugated forms; Sudachi's normalized form guards against a kanji
   homograph entry of the same reading and word class (``いる`` that Sudachi
   reads as ``要る`` is skipped).
4. Kana content word: exactly one entry with that reading, and that entry's
   headword is itself written in kana.  A kanji-headed single candidate or any
   competition leaves the token unlinked.
5. Conjugated kana form: exactly one entry's conjugation table generates the
   surface (kana version), and rule 4's kana-headword condition holds for the
   base (or the base is a table word).
Compounds and expressions that exist as entries (``お茶``, ``日本語教師``,
``気が置けない``, ``なければならない``, ``について``) are linked as one unit by
longest match; a content word followed only by particles is never merged
(``そこ+で`` stays two links even though a conjunction ``そこで`` exists), the
one exception being indefinite ``何か``/``誰も`` (pronoun + か/も).
する-compounds follow the split convention (1478 vs 830 hand-linked cases):
``⟦{発生|はっせい}→発生⟧⟦した→する⟧``, unless an ``Xする`` entry exists, whose
forms then link the whole verb.

Tokenizer
---------
SudachiPy (``sudachidict_core``) in SplitMode.C, imported lazily; unresolved
nouns are refined into B then A units.  Without SudachiPy (or with
``--no-tokenizer``) the tool runs in a reduced mode that links only
furigana-wrapped words (with their okurigana), katakana runs, and table
function words.

Usage
-----
    python3 build/auto_link.py                       # dry run over all entries
    python3 build/auto_link.py --range 7065 7100     # dry run, one ID range
    python3 build/auto_link.py --ids 07066,07067 --sample 5
    python3 build/auto_link.py --report --quiet      # aggregate statistics only
    python3 build/auto_link.py --apply --entries-dir /path/to/copy --index-dir entries --ids ...
    python3 build/auto_link.py --apply --confirm-real-entries   # the real thing

``--apply`` refuses to write into the repository's own ``entries/`` directory
unless ``--confirm-real-entries`` is also given.  Files are rewritten only when
a field changed; ``metadata.modified`` is then set to the current UTC time.
"""

from __future__ import annotations

import argparse
import bisect
import json
import random
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "entries"

FURI_RE = re.compile(r"\{([^|{}]+)\|([^|{}]+)\}")
LINK_RE = re.compile(r"⟦([^⟧]*)⟧")
LINK_INFO_RE = re.compile(r"^(.+?)→(.+?)：(.+)$")
HEADWORD_ALT_RE = re.compile(r"[／/]")
TILDES = "〜～"
MAX_SPAN = 8

# ---------------------------------------------------------------------------
# Function-word table (kana rows of the inline-word-links skill table)
# ---------------------------------------------------------------------------

_TABLE = """
particle 00051_ga が
particle 00079_ha は
particle 00314_ni に
particle 00422_wo を
particle 00484_mo も
particle 00490_made まで
particle 00502_de で
particle 00504_kara から
particle 00512_to と
particle 02473_he へ
particle 09472_no の
particle 09473_ka か
particle 09474_ne ね
particle 09475_yo よ
particle 09476_yori より
particle 09477_kedo けど
word 00536_itsu いつ
word 00539_doko どこ
word 00543_dou どう
word 00547_dore どれ
word 00551_dono どの
word 00915_ano あの
word 00919_asoko あそこ
word 00961_koko ここ
word 00962_kono この
word 00991_soko そこ
word 00993_sono その
word 00994_sore それ
word 00006_aru ある
word 00392_suru する
word 00495_iru いる
word 00520_morau もらう
word 00546_ageru あげる
word 00557_dekiru できる
word 01970_naru なる
word 00118_ii いい
word 01118_nai ない
word 00593_totemo とても
word 00595_chotto ちょっと
word 00597_takusan たくさん
word 00599_itsumo いつも
word 00601_yoku よく
word 00602_mou もう
word 00603_mada まだ
word 00604_amari あまり
word 00814_sugu すぐ
word 01284_moshi もし
word 00164_kamoshirenai かもしれない
word 01137_tokoro ところ
word 02899_kudasai ください
word 03093_dake だけ
word 00031_daga だが
word 00033_dakedo だけど
word 00379_sokode そこで
word 00382_soredemo それでも
"""

FUNCTION_WORDS: dict[str, str] = {}
PARTICLES: set[str] = set()
for _line in _TABLE.strip().splitlines():
    _kind, _id, _word = _line.split()
    FUNCTION_WORDS[_word] = _id
    if _kind == "particle":
        PARTICLES.add(_word)

#: Combined particle entries used only at the start of a sentence.
SENTENCE_INITIAL_COMBOS = {"でも", "では"}
#: Table words that inflect (never split off a kana run in tokenizer-free mode).
TABLE_VERBS = {"ある", "する", "いる", "もらう", "あげる", "できる", "なる", "いい", "ない"}
FALLBACK_CASE_PARTICLES = {"に", "で", "と", "へ", "から", "まで", "より"}
#: Copula forms linked only with ``--copula``.
COPULA = {"です": "09485_desu", "だ": "09496_da", "でしょう": "09887_deshou"}

CONTENT_POS = {"名詞", "代名詞", "副詞", "形状詞", "連体詞", "接続詞", "感動詞", "接尾辞", "接頭辞"}
CHAIN_AUX_LEMMAS = {"た", "ます", "たい", "ない", "ぬ", "られる", "れる", "させる", "せる",
                    "う", "よう", "まい", "たがる"}
CHAIN_ASPECT_VERBS = {"いる", "ある"}
#: Sudachi pos0 -> substrings that mark a compatible entry part_of_speech.
POS_COMPAT = {
    "動詞": ("verb",), "形容詞": ("adjective",), "名詞": ("noun",), "副詞": ("adverb",),
    "代名詞": ("pronoun", "noun"), "接続詞": ("conjunction",), "助詞": ("particle",),
    "感動詞": ("interjection",), "形状詞": ("adjective", "noun"), "連体詞": ("adnominal", "pre-noun"),
}

# ---------------------------------------------------------------------------
# Character helpers
# ---------------------------------------------------------------------------


def is_kanji(ch: str) -> bool:
    o = ord(ch)
    return (0x4E00 <= o <= 0x9FFF) or (0x3400 <= o <= 0x4DBF) or (0xF900 <= o <= 0xFAFF) \
        or ch in "々〆ヶヵ"


def is_hiragana(ch: str) -> bool:
    return "ぁ" <= ch <= "ゖ" or ch == "ー"


def is_katakana(ch: str) -> bool:
    return "ァ" <= ch <= "ヺ" or ch == "ー"


def hira(text: str) -> str:
    """Katakana -> hiragana (ー is kept)."""
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in text)


def has_kanji(s: str) -> bool:
    return any(is_kanji(c) for c in s)


def is_pure_hiragana(s: str) -> bool:
    return bool(s) and all(is_hiragana(c) for c in s)


def is_pure_katakana(s: str) -> bool:
    return bool(s) and all(is_katakana(c) or c == "・" for c in s) \
        and any(is_katakana(c) and c != "ー" for c in s)


def is_japanese_word(s: str) -> bool:
    """True when the string is made only of kana/kanji (a linkable token)."""
    return bool(s) and all(is_kanji(c) or is_hiragana(c) or is_katakana(c) for c in s)


def strip_furigana(text: str) -> str:
    return FURI_RE.sub(lambda m: m.group(1), text)


def furigana_reading(text: str) -> str:
    return FURI_RE.sub(lambda m: m.group(2), text)


def strip_tilde(s: str) -> str:
    return s.strip(TILDES).strip()


def header_line(line: str) -> bool:
    """ALL-CAPS section header ending with ':' (e.g. ``COMMON COLLOCATIONS:``)."""
    stripped = line.rstrip()
    if not stripped.endswith(":"):
        return False
    letters = [c for c in stripped if c.isascii() and c.isalpha()]
    return bool(letters) and all(c.isupper() for c in letters)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Text model: pieces and tokens
# ---------------------------------------------------------------------------


@dataclass
class Piece:
    kind: str             # 'char' | 'wrapper' | 'link'
    ostart: int
    oend: int
    plain: str
    reading: str | None   # reading of this piece (None for bare kanji / non-kana)
    pstart: int = 0


def parse_pieces(text: str) -> list[Piece]:
    pieces: list[Piece] = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "⟦":
            j = text.find("⟧", i)
            if j != -1:
                body = text[i + 1:j]
                info = LINK_INFO_RE.match(body)
                surface = info.group(1) if info else body
                pieces.append(Piece("link", i, j + 1, strip_furigana(surface), None))
                i = j + 1
                continue
        if ch == "{":
            m = FURI_RE.match(text, i)
            if m:
                pieces.append(Piece("wrapper", i, m.end(), m.group(1), hira(m.group(2))))
                i = m.end()
                continue
        reading = hira(ch) if (is_hiragana(ch) or is_katakana(ch)) else None
        pieces.append(Piece("char", i, i + 1, ch, reading))
        i += 1
    pos = 0
    for p in pieces:
        p.pstart = pos
        pos += len(p.plain)
    return pieces


class Layout:
    """Plain (furigana-stripped) rendering of a field plus offset maps."""

    def __init__(self, text: str, lock_strings: tuple[str, ...] = ()):
        self.text = text
        self.pieces = parse_pieces(text)
        self.plain = "".join(p.plain for p in self.pieces)
        self.starts = [p.pstart for p in self.pieces]
        self.boundaries = set(self.starts) | {len(self.plain)}
        self.locked: list[tuple[int, int]] = []
        for s in lock_strings:
            start = 0
            while s:
                pos = self.plain.find(s, start)
                if pos == -1:
                    break
                if self.aligned(pos, pos + len(s)):
                    self.locked.append((pos, pos + len(s)))
                start = pos + 1
        # A '{' that is not part of a furigana wrapper ({たたき{台|だい}}, {ちなむ},
        # {360{度|ど}|reading}) opens a brace group the validator must not see a
        # link inside: lock it up to its closing '}' (or the end of the text).
        open_pos = None
        for p in self.pieces:
            if p.kind != "char":
                continue
            if p.plain == "{" and open_pos is None:
                open_pos = p.pstart
            elif p.plain == "}" and open_pos is not None:
                self.locked.append((open_pos, p.pstart + 1))
                open_pos = None
        if open_pos is not None:
            self.locked.append((open_pos, len(self.plain)))

    def _piece_index(self, pos: int) -> int:
        return max(0, bisect.bisect_right(self.starts, pos) - 1)

    def aligned(self, ps: int, pe: int) -> bool:
        return ps in self.boundaries and pe in self.boundaries and ps < pe

    def span_pieces(self, ps: int, pe: int) -> list[Piece]:
        k = self._piece_index(ps)
        out = []
        while k < len(self.pieces) and self.pieces[k].pstart < pe:
            out.append(self.pieces[k])
            k += 1
        return out

    def free(self, ps: int, pe: int) -> bool:
        if any(ls < pe and ps < le for ls, le in self.locked):
            return False
        return all(p.kind != "link" for p in self.span_pieces(ps, pe))

    def orig_span(self, ps: int, pe: int) -> tuple[int, int]:
        pieces = self.span_pieces(ps, pe)
        return pieces[0].ostart, pieces[-1].oend


def span_reading(pieces: list[Piece]) -> str | None:
    """Furigana reading of a span; None when a bare kanji has no reading."""
    out = []
    for p in pieces:
        if p.reading is None:
            return None
        out.append(p.reading)
    return "".join(out)


def base_reading(pieces: list[Piece], base: str) -> str | None:
    """Reading of ``base`` given the (possibly inflected) surface pieces.

    ``{書|か}いた`` with base ``書く`` -> ``かく``: the common prefix of surface
    and base supplies wrapper readings, the base's kana suffix supplies the rest.
    Returns None when the prefix ends inside a wrapper, the base suffix contains
    kanji, or nothing aligns (irregular 来る is handled by the forms map).
    """
    plain = "".join(p.plain for p in pieces)
    n = 0
    while n < len(plain) and n < len(base) and plain[n] == base[n]:
        n += 1
    if n == 0:
        return None
    suffix = base[n:]
    if has_kanji(suffix):
        return None
    out, consumed = [], 0
    for p in pieces:
        if consumed == n:
            break
        if consumed + len(p.plain) > n or p.reading is None:
            return None          # prefix cuts inside an atomic wrapper / bare kanji
        out.append(p.reading)
        consumed += len(p.plain)
    if consumed != n:
        return None
    return "".join(out) + hira(suffix)


@dataclass
class Tok:
    surface: str
    ps: int
    pe: int
    dict_form: str = ""
    norm_form: str = ""
    pos: tuple = ()
    morpheme: object = None
    offset: int = 0
    refined: bool = False

    @property
    def pos0(self) -> str:
        return self.pos[0] if self.pos else ""

    @property
    def pos1(self) -> str:
        return self.pos[1] if len(self.pos) > 1 else ""

    @property
    def infl(self) -> str:
        return self.pos[5] if len(self.pos) > 5 else ""

    @property
    def is_particle(self) -> bool:
        return self.pos0 == "助詞"

    @property
    def is_aux(self) -> bool:
        return self.pos0 == "助動詞"

    @property
    def is_inflecting(self) -> bool:
        return self.pos0 in ("動詞", "形容詞")

    @property
    def is_content(self) -> bool:
        return self.pos0 in CONTENT_POS

    @property
    def skippable(self) -> bool:
        if self.pos0 in ("補助記号", "空白", "記号"):
            return True
        return not is_japanese_word(self.surface)


# ---------------------------------------------------------------------------
# Tokenizer wrappers
# ---------------------------------------------------------------------------


class SudachiTokenizer:
    def __init__(self):
        from sudachipy import dictionary, tokenizer  # lazy import

        self._tok = dictionary.Dictionary().create()
        self.C = tokenizer.Tokenizer.SplitMode.C
        self.B = tokenizer.Tokenizer.SplitMode.B
        self.A = tokenizer.Tokenizer.SplitMode.A

    def tokenize(self, text: str, offset: int = 0) -> list[Tok]:
        return [self._tok_from(m, offset) for m in self._tok.tokenize(text, self.C)]

    def refine(self, tok: Tok) -> list[Tok] | None:
        """Split a C-unit into B (then A) units; None when it does not split."""
        if tok.morpheme is None or tok.refined:
            return None
        for mode in (self.B, self.A):
            parts = tok.morpheme.split(mode)
            if len(parts) > 1:
                out = [self._tok_from(m, tok.offset) for m in parts]
                for t in out:
                    t.refined = True
                return out
        return None

    @staticmethod
    def _tok_from(m, offset: int) -> Tok:
        return Tok(m.surface(), offset + m.begin(), offset + m.end(), m.dictionary_form(),
                   m.normalized_form(), tuple(m.part_of_speech()), m, offset)


def load_tokenizer(disabled: bool = False):
    if disabled:
        return None
    try:
        return SudachiTokenizer()
    except Exception as exc:  # ImportError or dictionary problems
        print(f"note: SudachiPy unavailable ({exc}); running in tokenizer-free mode",
              file=sys.stderr)
        return None


def fallback_tokens(layout: Layout, ls: int, le: int) -> list[Tok]:
    """Tokenizer-free tokens: each wrapper/link is a token; kana runs are grouped."""
    toks: list[Tok] = []
    k = layout._piece_index(ls)
    cur_kind, cur_start, pos = None, ls, ls

    def flush(end: int) -> None:
        if cur_kind is not None and end > cur_start:
            toks.append(Tok(layout.plain[cur_start:end], cur_start, end, pos=("FB-" + cur_kind,)))

    while k < len(layout.pieces) and layout.pieces[k].pstart < le:
        p = layout.pieces[k]
        if p.kind in ("wrapper", "link"):
            kind = p.kind
        elif is_hiragana(p.plain):
            kind = "hira"
        elif is_katakana(p.plain) or p.plain == "・":
            kind = "kata"
        else:
            kind = "other"
        if kind in ("wrapper", "link") or kind != cur_kind:
            flush(pos)
            cur_kind, cur_start = kind, pos
        pos += len(p.plain)
        if kind in ("wrapper", "link"):
            flush(pos)
            cur_kind, cur_start = None, pos
        k += 1
    flush(pos)
    return toks


# ---------------------------------------------------------------------------
# Resolver
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Cand:
    id: str
    base: str
    how: str


@dataclass
class EntryCtx:
    own_id: str
    own_seqs: list          # dictionary-form token sequences of multi-token headwords
    own_strings: tuple = () # plain headword strings (>= 2 chars) locked wherever they occur


class Resolver:
    """Word -> entry resolution over the whole dictionary."""

    def __init__(self, entries):
        self.headword_of: dict[str, str] = {}
        self.reading_of: dict[str, str] = {}
        self.pos_of: dict[str, str] = {}
        self.kana_headed: dict[str, bool] = {}
        self.katakana_headed: dict[str, bool] = {}
        self.by_key: dict[str, list[tuple[str, str]]] = defaultdict(list)
        self.by_reading: dict[str, list[str]] = defaultdict(list)
        self.forms: dict[str, set[str]] = defaultdict(set)
        self.forms_kana: dict[str, set[str]] = defaultdict(set)
        self.form_reading: dict[tuple[str, str], str] = {}
        for entry in entries:
            self._add(entry)

    def _add(self, entry: dict) -> None:
        eid = entry.get("id") or ""
        hw_raw = entry.get("headword") or ""
        reading = hira(entry.get("reading") or "")
        if not eid or not hw_raw or not reading:
            return
        hw = strip_furigana(hw_raw).replace("～", "〜")
        self.headword_of[eid] = hw
        self.reading_of[eid] = reading
        self.pos_of[eid] = str(entry.get("part_of_speech") or "").lower()
        self.kana_headed[eid] = not has_kanji(hw)
        self.katakana_headed[eid] = is_pure_katakana(strip_tilde(hw))
        for variant in HEADWORD_ALT_RE.split(hw):
            key = strip_tilde(variant)
            if not key or any(t in key for t in TILDES):
                continue
            self.by_key[key].append((eid, variant.strip()))
        rkey = strip_tilde(reading)
        if rkey:
            self.by_reading[rkey].append(eid)
        conj = entry.get("conjugation") or {}
        forms = conj.get("forms") if isinstance(conj, dict) else None
        if not forms:
            return
        # Split convention for する-compounds: a noun entry's suru forms are not
        # used (the noun links, then する links to 00392_suru); an entry whose
        # headword itself ends in する links the whole verb.
        if conj.get("type") == "suru" and not hw.endswith("する"):
            return
        for form in forms:
            if not isinstance(form, dict):
                continue
            for key in ("affirmative", "negative"):
                text = form.get(key)
                if not isinstance(text, str) or not text:
                    continue
                fs = strip_tilde(strip_furigana(text).replace("～", "〜"))
                fk = strip_tilde(hira(furigana_reading(text)))
                if not fs:
                    continue
                self.forms[fs].add(eid)
                self.forms_kana[fk].add(eid)
                self.form_reading[(eid, fs)] = fk

    # -- candidate lookups -------------------------------------------------

    def lookup_headword(self, surface: str, reading: str | None) -> list[Cand]:
        """Kanji/katakana surface: headword or conjugation form with matching reading."""
        if reading is None:
            return []
        out: dict[str, Cand] = {}
        for eid, base in self.by_key.get(surface, ()):
            if self.reading_of.get(eid) == reading:
                out.setdefault(eid, Cand(eid, base, "headword"))
        for eid in sorted(self.forms.get(surface, ())):
            if self.form_reading.get((eid, surface)) == reading:
                out.setdefault(eid, Cand(eid, self.headword_of[eid], "forms"))
        return list(out.values())

    def lookup_kana(self, surface: str, ignore_katakana: bool = False) -> tuple[list[Cand], str]:
        """Hiragana surface (rules 4/5): returns (candidates, reason-if-empty).

        A katakana-headed entry with the same reading counts as a competitor
        (まま "rice" vs ママ vs 〜まま) unless ``ignore_katakana`` is set.
        """
        ids = [eid for eid in self.by_reading.get(surface, ())
               if not (ignore_katakana and self.katakana_headed.get(eid))]
        if ids:
            if len(ids) > 1:
                return [], "ambiguous-kana"
            eid = ids[0]
            if not self.kana_headed[eid]:
                return [], "kanji-headed-single"
            return [Cand(eid, self.headword_of[eid], "kana-word")], ""
        gen = sorted(self.forms_kana.get(surface, ()))
        if gen:
            if len(gen) > 1:
                return [], "ambiguous-kana"
            eid = gen[0]
            if not (self.kana_headed[eid] or self.headword_of[eid] in FUNCTION_WORDS):
                return [], "kanji-headed-single"
            return [Cand(eid, self.headword_of[eid], "kana-conjugated")], ""
        return [], "no-entry"

    def table_cand(self, word: str, norm_form: str = "", pos0: str = "") -> Cand | None:
        """Fixed-table resolution with the Sudachi kanji-homograph guard."""
        eid = FUNCTION_WORDS.get(word)
        if not eid or eid not in self.headword_of:
            return None
        if norm_form and has_kanji(norm_form) and norm_form != self.headword_of[eid]:
            wanted = POS_COMPAT.get(pos0)
            for other, _base in self.by_key.get(norm_form, ()):
                if other == eid or self.reading_of.get(other) != word:
                    continue
                if wanted is None or any(w in self.pos_of.get(other, "") for w in wanted):
                    return None   # Sudachi read it as a kanji homograph that has its own entry
        hw = self.headword_of[eid]
        base = hw if self.kana_headed[eid] else word
        return Cand(eid, base, "table")

    def entry_ctx(self, entry: dict, tokenizer) -> EntryCtx:
        eid = entry.get("id") or ""
        seqs, strings = [], []
        hw = strip_furigana(entry.get("headword") or "").replace("～", "〜")
        for variant in HEADWORD_ALT_RE.split(hw):
            key = strip_tilde(variant)
            if not key or any(t in key for t in TILDES):
                continue
            if len(key) >= 2:
                strings.append(key)
            if tokenizer is not None:
                toks = [t for t in tokenizer.tokenize(key) if not t.skippable]
                if len(toks) > 1:
                    seqs.append([t.dict_form for t in toks])
        return EntryCtx(eid, seqs, tuple(strings))


# ---------------------------------------------------------------------------
# Linker
# ---------------------------------------------------------------------------


@dataclass
class Link:
    ostart: int
    oend: int
    surface: str
    base: str
    id: str
    how: str


@dataclass
class Stats:
    tokens: int = 0
    linked: Counter = field(default_factory=Counter)
    unlinked: Counter = field(default_factory=Counter)

    def merge(self, other: "Stats") -> None:
        self.tokens += other.tokens
        self.linked.update(other.linked)
        self.unlinked.update(other.unlinked)


AMBIGUOUS = ("multi-candidate-kanji", "ambiguous-kana", "self-headword", "kanji-headed-single")


class Linker:
    def __init__(self, resolver: Resolver, tokenizer=None, copula: bool = False):
        self.r = resolver
        self.tok = tokenizer
        self.copula = copula

    # -- public entry point ---------------------------------------------------

    def link_text(self, text: str, ctx: EntryCtx, stats: Stats | None = None,
                  skip_headers: bool = False) -> str:
        if stats is None:
            stats = Stats()
        if not text or not any(is_kanji(c) or is_hiragana(c) or is_katakana(c) for c in text):
            return text
        layout = Layout(text, ctx.own_strings)
        links: list[Link] = []
        plain = layout.plain
        ls = 0
        while ls <= len(plain):
            le = plain.find("\n", ls)
            if le == -1:
                le = len(plain)
            line = plain[ls:le]
            if line and not (skip_headers and header_line(line)):
                if self.tok is not None:
                    toks = self.tok.tokenize(line, ls)
                else:
                    toks = fallback_tokens(layout, ls, le)
                links.extend(self._link_tokens(toks, layout, ctx, stats))
            ls = le + 1
        if not links:
            return text
        links.sort(key=lambda l: l.ostart)
        out, pos = [], 0
        for l in links:
            out.append(text[pos:l.ostart])
            out.append(f"⟦{l.surface}→{l.base}：{l.id}⟧")
            pos = l.oend
        out.append(text[pos:])
        return "".join(out)

    # -- token loop -----------------------------------------------------------

    def _link_tokens(self, toks: list[Tok], layout: Layout, ctx: EntryCtx, stats: Stats) -> list[Link]:
        links: list[Link] = []
        i = 0
        while i < len(toks):
            t = toks[i]
            if t.skippable or t.ps not in layout.boundaries or not layout.free(t.ps, t.pe):
                i += 1               # a token starting inside a wrapper is covered by the wrapper's first token
                continue
            if self.tok is None:
                i += self._fallback_step(toks, i, layout, ctx, stats, links)
                continue
            stats.tokens += 1
            seq_len = self._own_sequence_len(toks, i, ctx)
            if seq_len:
                stats.unlinked["self-headword"] += 1
                i += seq_len
                continue
            consumed = self._sentence_initial_combo(toks, i, layout, ctx, stats, links)
            if consumed:
                i += consumed
                continue
            if t.is_inflecting:
                consumed = self._inflecting(toks, i, layout, ctx, stats, links)
                i += consumed
                continue
            consumed, reason = self._plain_token(toks, i, layout, ctx, stats, links)
            if consumed:
                i += consumed
                continue
            refined = self.tok.refine(t) if t.pos0 == "名詞" else None
            if refined:
                toks[i:i + 1] = refined
                stats.tokens -= 1
                continue
            stats.unlinked[reason] += 1
            i += 1
        return links

    # -- helpers --------------------------------------------------------------

    def _make_link(self, layout: Layout, ps: int, pe: int, cand: Cand) -> Link:
        os_, oe = layout.orig_span(ps, pe)
        return Link(os_, oe, layout.text[os_:oe], cand.base, cand.id, cand.how)

    def _emit(self, layout, toks, i, k, cand, stats, links) -> int:
        links.append(self._make_link(layout, toks[i].ps, toks[k - 1].pe, cand))
        stats.linked[self._rule_name(cand, k - i, layout.plain[toks[i].ps:toks[k - 1].pe])] += 1
        return k - i

    @staticmethod
    def _sentence_initial(toks: list[Tok], i: int) -> bool:
        j = i - 1
        while j >= 0 and toks[j].pos0 == "空白":
            j -= 1
        return j < 0 or toks[j].skippable

    def _sentence_initial_combo(self, toks, i, layout, ctx, stats, links) -> int:
        """Sentence-initial でも/では link to their combined entries."""
        t = toks[i]
        if t.surface != "で" or not t.is_particle or i + 1 >= len(toks):
            return 0
        nxt = toks[i + 1]
        combo = t.surface + nxt.surface
        if combo not in SENTENCE_INITIAL_COMBOS or not nxt.is_particle or not self._sentence_initial(toks, i):
            return 0
        if not layout.aligned(t.ps, nxt.pe) or not layout.free(t.ps, nxt.pe):
            return 0
        cands, _ = self.r.lookup_kana(combo, ignore_katakana=True)   # でも vs デモ
        cands = [c for c in cands if c.id != ctx.own_id]
        if len(cands) != 1:
            return 0
        return self._emit(layout, toks, i, i + 2, cands[0], stats, links)

    def _own_sequence_len(self, toks: list[Tok], i: int, ctx: EntryCtx) -> int:
        for seq in ctx.own_seqs:
            k, j = 0, i
            while k < len(seq) and j < len(toks) and not toks[j].skippable and toks[j].dict_form == seq[k]:
                k += 1
                j += 1
            if k == len(seq):
                return j - i
        return 0

    def _span_ok(self, toks: list[Tok], i: int, k: int, layout: Layout, dictionary: bool = True,
                 stops: set | frozenset = frozenset()) -> bool:
        """Span is linkable: no punctuation, aligned with wrappers, not locked.

        ``dictionary`` spans (headword/forms lookups) must also pass the merge
        rule and must not cross a grammar-pattern start in ``stops``; a verb +
        auxiliary chain is validated with ``dictionary=False``.
        """
        span = toks[i:k]
        if any(t.skippable for t in span):
            return False
        if not layout.aligned(toks[i].ps, toks[k - 1].pe) or not layout.free(toks[i].ps, toks[k - 1].pe):
            return False
        if dictionary and k - i > 1 and not self._merge_allowed(span):
            return False
        if dictionary and any(i < j < k for j in stops):
            return False          # 説明しなければ must not swallow the start of なければならない
        return True

    def _grammar_starts(self, toks: list[Tok], i: int, layout: Layout, ctx: EntryCtx) -> set[int]:
        """Positions after i where a kana grammar pattern with its own entry starts."""
        out: set[int] = set()
        for j in range(i + 1, min(len(toks), i + MAX_SPAN)):
            t = toks[j]
            if t.skippable:
                break
            if (t.is_aux or t.pos0 == "形容詞") and self._grammar_span_at(toks, j, layout, ctx):
                out.add(j)
        return out

    @staticmethod
    def _merge_allowed(span: list[Tok]) -> bool:
        """Multi-token spans: compounds/expressions yes, word + particles no."""
        functional = [t.is_particle or t.is_aux for t in span]
        if all(functional):
            return False
        if span[0].is_particle and span[0].pos1 == "接続助詞" and span[0].surface in ("て", "で"):
            return False         # て belongs to the preceding verb: {食|た}べて⟦いる⟧, not ⟦ている⟧
        if span[0].is_content and all(functional[1:]):
            # only indefinite pronouns: 何か, 誰か, いつか, どこか, 何も, 誰も
            return len(span) == 2 and span[0].pos0 == "代名詞" and span[1].surface in ("か", "も")
        if span[0].is_inflecting and all(functional[1:]):
            return False         # する+と is not the conjunction すると; the chain owns auxiliaries
        if span[0].is_aux and not any(t.is_inflecting for t in span):
            return False
        return True

    @staticmethod
    def _particle_ok(t: Tok) -> bool:
        if t.is_particle:
            if t.surface == "で":
                return t.pos1 == "格助詞"
            return True
        if t.surface == "に" and t.is_aux and t.dict_form == "だ":
            return True          # 静かに: adverbial に after a na-adjective
        return False

    def _resolve_span(self, toks: list[Tok], i: int, k: int, layout: Layout, ctx: EntryCtx,
                      forms_only: bool = False) -> tuple[list[Cand], str]:
        """Candidates for the span toks[i:k] by its surface (rules 1-4)."""
        ps, pe = toks[i].ps, toks[k - 1].pe
        surface = layout.plain[ps:pe]
        pieces = layout.span_pieces(ps, pe)
        reading = span_reading(pieces)
        if len(surface) == 1 and is_hiragana(surface) and surface not in PARTICLES:
            return [], "single-kana"
        t = toks[i]
        if k - i == 1 and surface in FUNCTION_WORDS and not forms_only:
            if surface in PARTICLES:
                if not self._particle_ok(t):
                    return [], "particle-pos"
            elif t.is_aux:
                return [], "aux-pos"      # e.g. the auxiliary ない after a locked verb
            cand = self.r.table_cand(surface, t.norm_form, t.pos0)
            if cand is None:
                return [], "table-guard"
            if cand.id == ctx.own_id:
                return [], "self-headword"
            return [cand], ""
        if k - i == 1 and self.copula and surface in COPULA and t.is_aux and not forms_only:
            eid = COPULA[surface]
            if eid in self.r.headword_of and eid != ctx.own_id:
                return [Cand(eid, surface, "copula")], ""
        if k - i == 1 and t.is_aux:
            return [], "aux-pos"          # です/ます/たい/… are never content words (rule 4)
        if is_pure_hiragana(surface):
            if forms_only:
                gen = sorted(self.r.forms_kana.get(surface, ()))
                cands = [Cand(e, self.r.headword_of[e], "kana-conjugated") for e in gen
                         if self.r.kana_headed[e] or self.r.headword_of[e] in FUNCTION_WORDS]
                reason = "no-entry" if not gen else ("ambiguous-kana" if len(gen) > 1 else "kanji-headed-single")
            else:
                cands, reason = self.r.lookup_kana(surface)
        else:
            if reading is None:
                return [], "no-furigana"
            cands = self.r.lookup_headword(surface, reading)
            reason = "reading-mismatch" if (not cands and self.r.by_key.get(surface)) else "no-entry"
            if forms_only:
                cands = [c for c in cands if c.how == "forms"]
        own = [c for c in cands if c.id == ctx.own_id]
        cands = [c for c in cands if c.id != ctx.own_id]
        if not cands:
            return [], ("self-headword" if own else reason)
        if len(cands) > 1:
            return [], ("ambiguous-kana" if is_pure_hiragana(surface) else "multi-candidate-kanji")
        return cands, ""

    def _plain_token(self, toks, i, layout, ctx, stats, links) -> tuple[int, str]:
        """Non-inflecting token: longest dictionary match starting at i."""
        n = len(toks)
        last_reason = "no-entry"
        stops = self._grammar_starts(toks, i, layout, ctx)
        for k in range(min(n, i + MAX_SPAN), i, -1):
            if not self._span_ok(toks, i, k, layout, stops=stops):
                continue
            cands, reason = self._resolve_span(toks, i, k, layout, ctx)
            if len(cands) == 1:
                return self._emit(layout, toks, i, k, cands[0], stats, links), ""
            if reason in AMBIGUOUS and k - i > 1:
                stats.unlinked[reason] += 1       # an ambiguous compound is not split into parts
                return k - i, reason
            if k - i == 1:
                last_reason = reason
        if last_reason == "no-entry" and toks[i].pos0 == "名詞" and not toks[i].refined:
            return 0, last_reason                 # caller may refine the unit
        stats.unlinked[last_reason] += 1
        return 1, last_reason

    def _grammar_span_at(self, toks: list[Tok], j: int, layout: Layout, ctx: EntryCtx) -> bool:
        """True when a kana grammar pattern with its own entry starts at token j.

        ``しなければならない`` must not become ``⟦しなければ⟧⟦ならない⟧`` when the
        dictionary has ``なければならない``; the chain stops before it instead.
        """
        n = len(toks)
        for k in range(min(n, j + MAX_SPAN), j + 1, -1):
            if not self._span_ok(toks, j, k, layout):
                continue
            if not any(t.is_inflecting for t in toks[j:k]):
                continue          # ません/ました are plain auxiliaries, not patterns
            surface = layout.plain[toks[j].ps:toks[k - 1].pe]
            if not is_pure_hiragana(surface):
                continue
            cands, _ = self.r.lookup_kana(surface)
            if len(cands) == 1 and cands[0].id != ctx.own_id:
                return True
        return False

    def _chain_end(self, toks: list[Tok], i: int, layout: Layout, ctx: EntryCtx) -> int:
        """End index of the verb/adjective + auxiliary chain starting at i."""
        j = i + 1
        n = len(toks)
        after_te = False
        while j < n:
            t = toks[j]
            if t.skippable or not layout.free(t.ps, t.pe) or t.pe not in layout.boundaries:
                break
            prev = toks[j - 1]
            if (t.is_aux or t.pos0 == "形容詞") and self._grammar_span_at(toks, j, layout, ctx):
                break
            if t.is_aux and (t.dict_form in CHAIN_AUX_LEMMAS or t.norm_form in CHAIN_AUX_LEMMAS):
                after_te = False          # 読んだ: Sudachi lemmatizes だ as だ/た inconsistently
            elif t.pos0 == "形容詞" and t.pos1 == "非自立可能" and t.dict_form == "ない":
                after_te = False
            elif t.is_particle and t.pos1 == "接続助詞" and t.surface in ("て", "で"):
                after_te = True
            elif t.is_particle and t.pos1 == "接続助詞" and t.surface == "ば" and prev.infl.startswith("仮定形"):
                after_te = False
            elif after_te and t.pos0 == "動詞" and t.dict_form in CHAIN_ASPECT_VERBS:
                after_te = False
            else:
                break
            j += 1
        return j

    def _inflecting(self, toks, i, layout, ctx, stats, links) -> int:
        """Verb/adjective token: compounds beyond the chain, then the chain itself."""
        t = toks[i]
        n = len(toks)
        if t.infl.startswith("語幹"):
            stats.unlinked["stem-form"] += 1
            return 1
        j = self._chain_end(toks, i, layout, ctx)
        stops = self._grammar_starts(toks, i, layout, ctx)
        # 1. dictionary spans longer than the chain (食べ物, 気が置けない, お願いします)
        for k in range(min(n, i + MAX_SPAN), j, -1):
            if not self._span_ok(toks, i, k, layout, stops=stops):
                continue
            cands, reason = self._resolve_span(toks, i, k, layout, ctx)
            if len(cands) == 1:
                return self._emit(layout, toks, i, k, cands[0], stats, links)
            if reason in ("multi-candidate-kanji", "ambiguous-kana"):
                stats.unlinked[reason] += 1
                return k - i
        # 2. the chain, resolved through its base form
        while j > i + 1 and not self._span_ok(toks, i, j, layout, dictionary=False):
            j -= 1
        if not self._span_ok(toks, i, j, layout, dictionary=False):
            stats.unlinked["misaligned"] += 1
            return 1
        cands, reason = self._resolve_chain(toks, i, j, layout, ctx)
        if len(cands) == 1:
            return self._emit(layout, toks, i, j, cands[0], stats, links)
        # 3. exact conjugation-table forms, longest first (irregular 来た etc.)
        for k in range(j, i, -1):
            if not self._span_ok(toks, i, k, layout, dictionary=False):
                continue
            fc, _ = self._resolve_span(toks, i, k, layout, ctx, forms_only=True)
            if len(fc) == 1:
                return self._emit(layout, toks, i, k, fc[0], stats, links)
        stats.unlinked[reason or "no-entry"] += 1
        return 1

    def _resolve_chain(self, toks, i, j, layout, ctx) -> tuple[list[Cand], str]:
        t = toks[i]
        ps, pe = t.ps, toks[j - 1].pe
        surface = layout.plain[ps:pe]
        pieces = layout.span_pieces(ps, pe)
        if len(surface) == 1 and is_hiragana(surface):
            return [], "single-kana"
        if surface in FUNCTION_WORDS:          # ください -> 02899_kudasai, not the lemma くださる
            cand = self.r.table_cand(surface, t.norm_form, t.pos0)
            if cand is None:
                return [], "table-guard"
            if cand.id == ctx.own_id:
                return [], "self-headword"
            return [Cand(cand.id, cand.base, "chain")], ""
        reason = "no-entry"
        bases = [t.dict_form]
        if t.norm_form and t.norm_form != t.dict_form and has_kanji(t.norm_form):
            bases.append(t.norm_form)          # potential-form lemma: 置ける -> 置く
        for base in bases:
            if not base:
                continue
            if base in FUNCTION_WORDS:
                cand = self.r.table_cand(base, t.norm_form, t.pos0)
                if cand is None:
                    return [], "table-guard"
                if cand.id == ctx.own_id:
                    return [], "self-headword"
                return [Cand(cand.id, cand.base, "chain")], ""
            if has_kanji(base):
                if is_pure_hiragana(surface):
                    reason = "kanji-headed-single" if self.r.by_key.get(base) else "no-entry"
                    continue
                rd = base_reading(pieces, base)
                if rd is None:
                    reason = "reading-mismatch" if self.r.by_key.get(base) else "no-entry"
                    continue
                cands = [Cand(eid, bs, "chain") for eid, bs in self.r.by_key.get(base, ())
                         if self.r.reading_of.get(eid) == rd]
                if not cands:
                    reason = "reading-mismatch" if self.r.by_key.get(base) else "no-entry"
                    continue
            else:
                if not is_pure_hiragana(surface):
                    reason = "kana-base-kanji-surface"
                    continue
                cands, reason = self.r.lookup_kana(base)
                if not cands:
                    continue
                cands = [Cand(c.id, c.base, "chain") for c in cands]
            own = [c for c in cands if c.id == ctx.own_id]
            cands = [c for c in cands if c.id != ctx.own_id]
            if own and not cands:
                return [], "self-headword"
            if len(cands) == 1:
                return cands, ""
            if len(cands) > 1:
                return [], "multi-candidate-kanji"
        return [], reason

    @staticmethod
    def _rule_name(cand: Cand, ntok: int, surface: str) -> str:
        if cand.how == "table":
            return "function-word"
        if cand.how == "copula":
            return "copula"
        if cand.how == "chain":
            return "verb-chain"
        if is_pure_katakana(surface):
            return "katakana"
        if cand.how in ("kana-word", "kana-conjugated"):
            return cand.how
        if ntok > 1 and cand.how == "headword":
            return "compound-headword"
        return "furigana-kanji" if cand.how == "headword" else "forms-map"

    # -- tokenizer-free mode --------------------------------------------------

    def _fallback_step(self, toks, i, layout, ctx, stats, links) -> int:
        t = toks[i]
        kind = t.pos0
        n = len(toks)
        stats.tokens += 1
        if kind == "FB-wrapper":
            # gather the alternating wrapper/hiragana run after this wrapper
            k = i
            while k + 1 < n and toks[k + 1].pos0 in ("FB-wrapper", "FB-hira") \
                    and layout.free(toks[k + 1].ps, toks[k + 1].pe):
                k += 1
            run_end = toks[k].pe
            best = None
            for cut in range(run_end, t.pe - 1, -1):      # longest surface first
                if cut not in layout.boundaries:
                    continue
                surface = layout.plain[t.ps:cut]
                rd = span_reading(layout.span_pieces(t.ps, cut))
                cands = [c for c in self.r.lookup_headword(surface, rd) if c.id != ctx.own_id]
                if len(cands) == 1:
                    best = (cut, cands[0])
                    break
                if len(cands) > 1:
                    stats.unlinked["multi-candidate-kanji"] += 1
                    return 1
            if best is None:
                stats.unlinked["no-entry"] += 1
                return 1
            cut, cand = best
            links.append(self._make_link(layout, t.ps, cut, cand))
            stats.linked["furigana-kanji" if cand.how == "headword" else "forms-map"] += 1
            # whatever is left of the run is re-queued as fresh tokens
            rest = [tt for tt in toks[i + 1:k + 1] if tt.pe > cut]
            if rest and rest[0].ps < cut:
                rest[0] = Tok(layout.plain[cut:rest[0].pe], cut, rest[0].pe, pos=(rest[0].pos0,))
            toks[i + 1:k + 1] = rest
            return 1
        if kind == "FB-kata":
            cands = [c for c in self.r.lookup_headword(t.surface, hira(t.surface)) if c.id != ctx.own_id]
            if len(cands) == 1:
                links.append(self._make_link(layout, t.ps, t.pe, cands[0]))
                stats.linked["katakana"] += 1
            else:
                stats.unlinked["multi-candidate-kanji" if cands else "no-entry"] += 1
            return 1
        if kind == "FB-hira":
            run = t.surface
            prev = toks[i - 1] if i > 0 else None
            at_start = prev is None or prev.pos0 == "FB-other"
            if run in SENTENCE_INITIAL_COMBOS and at_start:
                cands, _ = self.r.lookup_kana(run, ignore_katakana=True)
                cands = [c for c in cands if c.id != ctx.own_id]
                if len(cands) == 1:
                    links.append(self._make_link(layout, t.ps, t.pe, cands[0]))
                    stats.linked["function-word"] += 1
                else:
                    stats.unlinked["ambiguous-kana"] += 1
                return 1
            words = self._split_kana_run(run)
            if not words:
                stats.unlinked["no-entry"] += 1
                return 1
            pos = t.ps
            for w in words:
                cand = self.r.table_cand(w)
                if cand is not None and cand.id != ctx.own_id:
                    links.append(self._make_link(layout, pos, pos + len(w), cand))
                    stats.linked["function-word"] += 1
                pos += len(w)
            return 1
        return 1

    @staticmethod
    def _split_kana_run(run: str) -> list[str] | None:
        """Tokenizer-free split of a hiragana run into table words, or None.

        Accepts a whole table word, a case particle + は/も/の (には, では, との),
        or a particle + a non-verb table word (をください, はこの).  Anything
        else stays unlinked — without a tokenizer, にはいる could be に+は+いる
        or 入る, so verbs are never split off.
        """
        if run in FUNCTION_WORDS and (len(run) > 1 or run in PARTICLES):
            return [run]
        for a in range(1, len(run)):
            first, rest = run[:a], run[a:]
            if first not in PARTICLES:
                continue
            if rest in PARTICLES:
                if first in FALLBACK_CASE_PARTICLES and rest in ("は", "も", "の"):
                    return [first, rest]
                continue
            if rest in FUNCTION_WORDS and rest not in TABLE_VERBS and len(rest) > 1:
                return [first, rest]
        return None


# ---------------------------------------------------------------------------
# Entry processing
# ---------------------------------------------------------------------------


def iter_entry_paths(entries_dir: Path, ids: set[str] | None, id_range: tuple[int, int] | None):
    for path in sorted(entries_dir.glob("*/*.json")):
        stem = path.stem
        num = stem[:5]
        if not num.isdigit():
            continue
        if ids and stem not in ids and num not in ids:
            continue
        if id_range and not (id_range[0] <= int(num) <= id_range[1]):
            continue
        yield path


def iter_entries(entries_dir: Path):
    for path in sorted(entries_dir.glob("*/*.json")):
        try:
            yield json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"warning: could not read {path}: {exc}", file=sys.stderr)


def process_entry(entry: dict, linker: Linker, resolver: Resolver, stats: Stats) -> list[tuple[str, str, str]]:
    """Link the entry in place; return [(field, before, after)] for changed fields."""
    ctx = resolver.entry_ctx(entry, linker.tok)
    changes = []
    for idx, ex in enumerate(entry.get("examples") or []):
        if not isinstance(ex, dict):
            continue
        text = ex.get("japanese")
        if not isinstance(text, str) or not text:
            continue
        new = linker.link_text(text, ctx, stats)
        if new != text:
            ex["japanese"] = new
            changes.append((f"examples[{idx}].japanese", text, new))
    notes = entry.get("notes")
    if isinstance(notes, str) and notes:
        new = linker.link_text(notes, ctx, stats, skip_headers=True)
        if new != notes:
            entry["notes"] = new
            changes.append(("notes", notes, new))
    return changes


def write_entry(path: Path, entry: dict, original_text: str) -> None:
    payload = json.dumps(entry, ensure_ascii=False, indent=2)
    if original_text.endswith("\n"):
        payload += "\n"
    path.write_text(payload, encoding="utf-8")


def parse_ids(spec: str | None) -> set[str] | None:
    if not spec:
        return None
    ids: set[str] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if part.startswith("@"):
            for line in Path(part[1:]).read_text(encoding="utf-8").splitlines():
                if line.strip():
                    ids.add(line.strip())
        else:
            ids.add(part)
    return ids


def print_report(stats: Stats, entries_seen: int, entries_changed: int, links_total: int) -> None:
    print("\n== auto_link report ==")
    print(f"entries processed:      {entries_seen}")
    print(f"entries with new links: {entries_changed}")
    per = f"  ({links_total / entries_seen:.1f} per entry)" if entries_seen else ""
    print(f"links added:            {links_total}{per}")
    print(f"content tokens seen:    {stats.tokens}")
    if stats.tokens:
        print(f"share of tokens linked: {sum(stats.linked.values()) / stats.tokens:.1%}")
    print("linked by rule:")
    for k, v in stats.linked.most_common():
        print(f"  {k:<24}{v:>8}")
    print("left unlinked by reason:")
    for k, v in stats.unlinked.most_common():
        print(f"  {k:<24}{v:>8}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="report only (default)")
    mode.add_argument("--apply", action="store_true", help="rewrite changed entry files")
    ap.add_argument("--ids", help="comma-separated entry IDs/stems, or @file with one per line")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--entries-dir", type=Path, default=ENTRIES_DIR,
                    help="entries to process (default: the repository's entries/)")
    ap.add_argument("--index-dir", type=Path, default=None,
                    help="entries used to build the resolver index (default: --entries-dir)")
    ap.add_argument("--report", action="store_true", help="print aggregate statistics")
    ap.add_argument("--sample", type=int, default=0, metavar="N",
                    help="print N random before/after examples")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--no-tokenizer", action="store_true", help="force tokenizer-free mode")
    ap.add_argument("--copula", action="store_true", help="also link だ/です/でしょう")
    ap.add_argument("--quiet", action="store_true", help="no per-entry lines")
    ap.add_argument("--confirm-real-entries", action="store_true",
                    help="allow --apply to write into the repository's own entries/")
    args = ap.parse_args()

    entries_dir = args.entries_dir.resolve()
    index_dir = (args.index_dir or args.entries_dir).resolve()
    real_entries = ENTRIES_DIR.resolve()
    if args.apply and entries_dir == real_entries and not args.confirm_real_entries:
        print("refusing to --apply on the repository's entries/ without --confirm-real-entries",
              file=sys.stderr)
        return 2

    tokenizer = load_tokenizer(args.no_tokenizer)
    resolver = Resolver(iter_entries(index_dir))
    linker = Linker(resolver, tokenizer, copula=args.copula)
    ids = parse_ids(args.ids)
    id_range = tuple(args.range) if args.range else None

    stats = Stats()
    samples: list[tuple[str, str, str, str]] = []
    entries_seen = entries_changed = links_total = 0
    for path in iter_entry_paths(entries_dir, ids, id_range):
        original = path.read_text(encoding="utf-8")
        try:
            entry = json.loads(original)
        except json.JSONDecodeError as exc:
            print(f"warning: skipping {path}: {exc}", file=sys.stderr)
            continue
        entries_seen += 1
        changes = process_entry(entry, linker, resolver, stats)
        added = sum(after.count("⟦") - before.count("⟦") for _f, before, after in changes)
        links_total += added
        if changes:
            entries_changed += 1
            for f, before, after in changes:
                samples.append((entry.get("id", path.stem), f, before, after))
        if not args.quiet:
            print(f"{path.stem}: +{added} links in {len(changes)} field(s)")
        if args.apply and changes:
            real_target = path.resolve()
            if real_target.is_relative_to(real_entries) and not args.confirm_real_entries:
                print(f"refusing to write into the real entries/ (symlink?): {path}", file=sys.stderr)
                continue
            entry.setdefault("metadata", {})["modified"] = utc_now()
            write_entry(path, entry, original)

    if args.sample and samples:
        rng = random.Random(args.seed)
        for eid, f, before, after in rng.sample(samples, min(args.sample, len(samples))):
            print(f"\n--- {eid} {f}\nBEFORE: {before}\nAFTER:  {after}")
    if args.report or args.sample or not args.quiet:
        print_report(stats, entries_seen, entries_changed, links_total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
