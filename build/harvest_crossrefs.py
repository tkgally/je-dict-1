#!/usr/bin/env python3
"""Harvest structured cross-references from the bulleted note sections.

Entries' notes carry sections headed by ALL-CAPS lines ending in a colon
(build/data/note_headers.json is the canonical vocabulary; aliases are accepted).
Under SIMILAR WORDS (incl. CONTRAST / SYNONYMS / ANTONYMS …), RELATED WORDS,
KEIGO and TRANSITIVITY, bullets look like

    - {援助|えんじょ}する: to aid — often implies …
    - {応援|おうえん}する — to cheer on
    - けれども — although …
    - ⟦{援助|えんじょ}する→援助する：08123_enjosuru⟧: …      (already inline-linked)
    - Pair: {固|かた}まる (intransitive, to harden)              (TRANSITIVITY)

This tool reads the Japanese term at the start of each bullet, resolves it to
exactly one existing entry (by furigana-stripped headword + reading; by
headword-or-reading for kana-only terms; by the link id for inline-linked
terms) and proposes a structured `cross_references` item — or, under
TRANSITIVITY, a `prominent_see_also` pair link. It never edits any text: it
only appends structured items, at most MAX_NEW_REFS_PER_ENTRY per entry per run.

Type by header: SIMILAR WORDS / SYNONYMS -> synonym; CONTRAST / COMPARED WITH /
DISTINCTION / VS -> contrast; ANTONYMS / OPPOSITES -> antonym (a bullet whose
gloss starts with "opposite"/"antonym" is an antonym wherever it sits);
RELATED WORDS -> related; KEIGO -> keigo (label honorific/humble); TRANSITIVITY
-> prominent_see_also with note transitive/intransitive (only when the bullet
says which). With --reciprocal (default) the back-link is added on the target
for synonym/antonym/contrast/related (and the reverse pair link); keigo
reverses are reported, not written (direction is not inferable).

Default is a dry run. Usage:

    python3 build/harvest_crossrefs.py --report                 # totals only
    python3 build/harvest_crossrefs.py --range 20000 20499      # per-entry proposals
    python3 build/harvest_crossrefs.py --sample 40 --seed 1     # random proposals + bullets
    python3 build/harvest_crossrefs.py --ids 26317,26711 --apply
    python3 build/harvest_crossrefs.py --entries-dir /tmp/copy/entries --apply
    python3 build/harvest_crossrefs.py --json out.json --report
"""
import argparse
import json
import random
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from constants import CROSS_REF_TYPES  # noqa: E402
from japanese_utils import strip_furigana, normalize_reading  # noqa: E402
from xref_common import (  # noqa: E402
    JAPANESE_CHAR_RE, KANJI_CHAR_RE, LINK_RE, is_kana_only, derive_reading, plain_text,
    first_gloss, load_index, numeric_id, read_entry, write_entry,
    insert_key_before_metadata, utc_now,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"
NOTE_HEADERS_FILE = PROJECT_ROOT / "build" / "data" / "note_headers.json"

MAX_NEW_REFS_PER_ENTRY = 8
MAX_LABEL_LEN = 60
HARVEST_FAMILIES = ("SIMILAR WORDS", "RELATED WORDS", "KEIGO", "TRANSITIVITY")
RECIPROCAL_TYPES = {"synonym", "antonym", "contrast", "related", "homophone"}

# Kana-only bullets that name particles are skipped (unless the entry itself
# is a particle); single-kana tokens are skipped outright.
PARTICLES = {"から", "まで", "より", "など", "でも", "しか", "だけ", "ほど", "くらい", "ぐらい",
             "ばかり", "さえ", "こそ", "って", "とか", "なら", "ても", "のに", "ので", "けど",
             "とも", "やら", "だの", "なり", "きり", "のみ", "ずつ", "って", "たり", "つつ",
             "ながら", "ものの", "ところ"}
# Grammatical metalanguage that appears as the "term" of TRANSITIVITY/KEIGO bullets.
METALANGUAGE = {"自動詞", "他動詞", "自他動詞", "自動", "他動", "動詞", "名詞", "形容詞",
                "副詞", "助詞", "尊敬語", "謙譲語", "丁寧語", "敬語", "自他"}

PROSE_PREFIXES = {"note", "notes", "nb", "n.b.", "tip", "tips", "caution", "warning", "remember",
                  "example", "examples", "e.g.", "eg", "cf", "cf.", "see", "see also", "also", "usage",
                  "meaning", "literally", "literal", "etymology", "origin", "pattern", "patterns",
                  "form", "forms", "type", "aspect", "transitivity", "pronunciation", "reading",
                  "spelling", "important", "hint", "exception", "exceptions", "difference",
                  "distinction", "key difference", "key point", "summary", "context", "register",
                  "formality", "politeness", "nuance", "tone", "history", "background", "comparison",
                  "but", "however", "unlike", "compare", "contrast with", "vs", "vs."}
PAIR_NOTATION_RE = re.compile(r"^\s*(?:↔|⇔|⟷|<->|<=>|vs\.?\s|versus\s|or\s)")
POS_CLASSES = {
    "noun": "n", "pronoun": "n", "counter": "n", "number": "n", "suffix": "n", "prefix": "n",
    "verb-godan": "v", "verb-ichidan": "v", "verb-suru": "v", "verb-kuru": "v", "verb-irregular": "v",
    "adjective-i": "a", "adjective-na": "a", "adjective-no": "a", "adjective-taru": "a",
    "pre-noun-adjectival": "a", "adverb": "d", "onomatopoeia": "d",
    "particle": "g", "conjunction": "g", "auxiliary": "g", "interjection": "g", "expression": "x",
}
SURU_TAIL_RE = re.compile(r"(?:する|します|した|して)$")
NA_TAIL_RE = re.compile(r"(?:な|に|だ)$")
GRAMMATICAL_SOURCE_POS = {"particle", "conjunction", "auxiliary", "suffix"}

HEADER_LINE_RE = re.compile(r"^\s*([A-Z]{2,}[^\n]{0,70}?)\s*:\s*$")
HEADER_INLINE_RE = re.compile(r"^\s*([A-Z]{2,}[A-Z0-9 /().〜ているー・&'’\-]*?)\s*:\s+\S")
BULLET_MARK_RE = re.compile(r"^\s*(?:[-–—*•・●○◦▪‣]|\d+[.)])\s*")
PREFIX_LABEL_RE = re.compile(r"^([A-Za-z][A-Za-z /'’\-]{0,40}?)\s*[:：]\s*")
TERM_TOKEN_RE = re.compile(
    r"⟦[^⟧]*⟧"                                  # inline link
    r"|\{[^{}|]+\|[^{}]+\}"                      # furigana wrapper
    r"|[ぁ-ゖァ-ヺーゝゞヽヾ㐀-䶿一-鿿豈-﫿々〆ヶヵ〇〜～…]+"   # kana / kanji run (〜 marks an affix)
    r"|[Ａ-Ｚａ-ｚ０-９]+"                         # fullwidth alnum
)
ASCII_GLUED_RE = re.compile(r"[A-Za-z0-9]+")
SEP_RE = re.compile(r"\s*(?:(?P<colon>[:：])|(?P<dash>[—–―]|-(?=\s))|(?P<paren>[(（]))\s*")
MULTI_SEP_RE = re.compile(r"\s*[、,，/／・]\s*")
AFFIX_MARK_RE = re.compile(r"[〜～…]|^[-‐－]|[-‐－]$")
NON_JAPANESE_RE = re.compile(r"[぀-ヿ㐀-䶿一-鿿豈-﫿　-〿｀-ﾟ！-～々〆ヶヵ]+")
_OPP = r"(?:opposite|antonym)s?(?=\s*(?:of\b|in meaning|word|term|concept|case|sense|meaning|[—–:;,.)]|$))"
_QUAL = r"(?:the |its |a |an |direct |exact |near |rough |formal |casual |polar |standard )*"
ANTONYM_HINT_RE = re.compile(
    "^" + _QUAL + _OPP
    + r"|[(（]" + _QUAL + r"(?:opposite|antonym)s?(?: of [^)）]{0,30})?[)）]"
    + r"|\b(?:direct|exact|polar) " + _OPP
    + r"|[—–:;,]\s*" + _QUAL + _OPP,
    re.IGNORECASE)
# A bullet that explicitly calls the word a synonym, or an entry whose own gloss is "antonym"/"synonym"
# (対義語, 反対語, 同義語 …), must not trigger the antonym cue.
SYNONYM_CUE_RE = re.compile(r"\bsynonym", re.IGNORECASE)
META_WORD_RE = re.compile(r"\b(?:synonym|antonym|opposite word|opposite term|word with the opposite)", re.IGNORECASE)
CONTRAST_HINT_RE = re.compile(
    r"\b(?:not to be confused|don'?t confuse|do not confuse|unlike|whereas|as opposed to|"
    r"different (?:kanji|word|meaning|sense)|same reading|homophone|homonym|not the same|"
    r"distinct from|in contrast|by contrast|easily confused|often confused|"
    r"(?:female|male|feminine|masculine|opposite|negative|positive) counterpart)\b", re.IGNORECASE)
TRAILING_STOPWORD_RE = re.compile(
    r"(?:\s+(?:of|the|a|an|to|for|with|than|as|and|or|in|on|by|from|at|into|about|vs\.?|versus|like|unlike|e\.g\.|i\.e\.))+$",
    re.IGNORECASE)
TRANS_KEYWORD_RE = re.compile(r"自動詞|他動詞|\b(intransitive|transitive)\b", re.IGNORECASE)
NON_WORD_HEADER_RE = re.compile(
    r"PATTERN|COLLOCATION|\bFORM|COMPOUND|KANJI|GRAMMAR|PHRASE|CONJUGATION|COUNTER|READING"
    r"|PARTICLE|EXAMPLE|USAGE|STRUCTURE|CONSTRUCTION|SPELLING|WRITING|IDIOM|PROVERB")


# --------------------------------------------------------------------------- #
# Header classification
# --------------------------------------------------------------------------- #
def _load_alias_map(path=NOTE_HEADERS_FILE):
    alias_map = {}
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        data = {"canonical": {c: {"aliases": []} for c in HARVEST_FAMILIES}}
    for canonical, spec in data.get("canonical", {}).items():
        alias_map[_norm_header(canonical)] = canonical
        for alias in spec.get("aliases", []):
            alias_map.setdefault(_norm_header(alias), canonical)
    return alias_map


def _norm_header(text):
    text = (text or "").strip().upper().rstrip(":").strip()
    return re.sub(r"\s+", " ", text)


ALIAS_MAP = _load_alias_map()

_STARTS_CONTRAST = ("CONTRAST", "COMPAR", "DISTINCT", "DIFFEREN", "VS", "VERSUS")
_STARTS_ANTONYM = ("ANTONYM", "OPPOSITE")
_HAS_SYNONYM = ("SYNONYM", "NEAR")
_HAS_CONTRAST = ("CONTRAST", "COMPAR", "DISTINCT", "DIFFEREN", "VERSUS", "VS")
_HAS_ANTONYM = ("ANTONYM", "OPPOSITE")


def type_for_header(family, header_norm):
    """Cross-reference type implied by a harvestable header."""
    if family == "RELATED WORDS":
        return "related"
    if family == "KEIGO":
        return "keigo"
    if family == "TRANSITIVITY":
        return "transitivity"   # pseudo-type: handled as a prominent_see_also pair
    h = header_norm
    if h.startswith(_STARTS_CONTRAST):
        return "contrast"
    if h.startswith(_STARTS_ANTONYM):
        return "antonym"
    if JAPANESE_CHAR_RE.search(h) or "〜" in h or "～" in h:
        return "related"        # "SIMILAR ～種 WORDS": a morphological family, not synonyms
    if any(k in h for k in _HAS_SYNONYM):
        return "synonym"
    if any(k in h for k in _HAS_CONTRAST):
        return "contrast"
    if any(k in h for k in _HAS_ANTONYM):
        return "antonym"
    # A SIMILAR WORDS section in this dictionary discriminates near-synonyms,
    # co-hyponyms, and confusables; measured 2026-09-02, about one bullet in
    # ten under it is not a synonym at all. "contrast" (the skill's "easily
    # confused / compare with" type) is right for the whole family, so it is
    # the default; only an explicit SYNONYMS header yields "synonym".
    return "contrast"


def _fuzzy_family(h):
    if h.startswith(("SIMILAR", "SYNONYM", "NEAR", "ALTERNATIVE") + _STARTS_CONTRAST + _STARTS_ANTONYM):
        return "SIMILAR WORDS"
    if h.startswith(("RELATED", "SEE ALSO", "ASSOCIATED")):
        return "RELATED WORDS"
    if h.startswith(("KEIGO", "HONORIFIC", "HUMBLE", "POLITE", "RESPECTFUL")):
        return "KEIGO"
    if h.startswith(("TRANSITIV", "INTRANSITIV", "PAIR", "PAIRED")):
        return "TRANSITIVITY"
    return None


def classify_header(raw):
    """Return (family, type, how) for a raw header line; family None when the
    section is not harvested. `how` is canonical/alias/fuzzy or the skip reason."""
    h = _norm_header(raw)
    canonical = ALIAS_MAP.get(h)
    if canonical is None:
        stripped = re.sub(r"\s*[(（].*[)）]\s*$", "", h).strip()
        canonical = ALIAS_MAP.get(stripped)
        if canonical is not None:
            h = stripped
    if canonical is not None:
        if canonical not in HARVEST_FAMILIES:
            return None, None, "other-canonical"
        how = "canonical" if h == canonical else "alias"
        return canonical, type_for_header(canonical, h), how
    if NON_WORD_HEADER_RE.search(h):
        return None, None, "non-word"
    family = _fuzzy_family(h)
    if family is None:
        return None, None, "unknown"
    return family, type_for_header(family, h), "fuzzy"


# --------------------------------------------------------------------------- #
# Note sectioning and bullet parsing
# --------------------------------------------------------------------------- #
def iter_sections(notes):
    """Yield (header_raw, [lines]) for each headed section of a notes string."""
    header = None
    lines = []
    for line in (notes or "").split("\n"):
        m = HEADER_LINE_RE.match(line)
        if m:
            if header is not None:
                yield header, lines
            header, lines = m.group(1), []
            continue
        m = HEADER_INLINE_RE.match(line)
        if m:
            if header is not None:
                yield header, lines
            header, lines = m.group(1), []
            continue   # the rest of the line is prose
        if header is not None:
            lines.append(line)
    if header is not None:
        yield header, lines


class Term:
    """One Japanese term found at the start of a bullet."""

    __slots__ = ("raw", "surface", "plain", "reading", "link_id", "link_noentry")

    def __init__(self, raw):
        self.raw = raw
        self.surface = LINK_RE.sub(r"\1", raw)
        self.plain = strip_furigana(self.surface)
        self.reading = derive_reading(self.surface)
        self.link_id = None
        self.link_noentry = False
        links = LINK_RE.findall(raw)
        if len(links) == 1 and LINK_RE.fullmatch(raw):
            target = links[0][2].strip()
            if target == "noentry":
                self.link_noentry = True
            elif re.match(r"^\d{5}_", target):
                self.link_id = target
        if is_kana_only(self.plain):
            self.reading = normalize_reading(self.plain)

    def __repr__(self):
        return f"Term({self.plain!r}, {self.reading!r}, link={self.link_id})"


def _parse_term_at(text, pos):
    """Parse a term starting at `pos`; return (Term|None, new_pos)."""
    start = pos
    while True:
        m = TERM_TOKEN_RE.match(text, pos)
        if m:
            pos = m.end()
            continue
        if pos > start:
            m = ASCII_GLUED_RE.match(text, pos)     # {自己|じこ}PR
            if m and not text[pos - 1].isspace():
                pos = m.end()
                continue
        break
    raw = text[start:pos]
    if not raw or not JAPANESE_CHAR_RE.search(plain_text(raw)):
        return None, start
    return Term(raw), pos


def parse_bullet(line):
    """Parse one section line. Returns None for prose, else a dict:
    {marked, prefix, terms, sep, gloss, text} where gloss is the English part."""
    m = BULLET_MARK_RE.match(line)
    marked = bool(m and m.end() > 0 and m.group(0).strip())
    body = line[m.end():] if m else line
    body = body.strip()
    if not body:
        return None
    prefix = None
    pm = PREFIX_LABEL_RE.match(body)
    if pm:
        prefix = pm.group(1).strip()
        if prefix.lower() in PROSE_PREFIXES or len(prefix.split()) > 3:
            return None        # "Note: …", "Compare: …" — prose, not a term bullet
        body = body[pm.end():]
    terms = []
    term, pos = _parse_term_at(body, 0)
    if term is None:
        return None
    terms.append(term)
    while len(terms) < 4:
        ms = MULTI_SEP_RE.match(body, pos)
        if not ms:
            break
        nxt, npos = _parse_term_at(body, ms.end())
        if nxt is None:
            break
        terms.append(nxt)
        pos = npos
    rest = body[pos:]
    if PAIR_NOTATION_RE.match(rest):
        return None            # "A ↔ B (gloss)" / "A vs B": the gloss belongs to neither term alone
    sm = SEP_RE.match(rest)
    sep = None
    gloss = ""
    if sm and sm.end() > 0 and (sm.group("colon") or sm.group("dash") or sm.group("paren")):
        gloss = rest[sm.end():]
        if sm.group("paren"):
            sep = "paren"
            close = re.search(r"[)）]", gloss)
            if close:
                inner, after = gloss[:close.start()], gloss[close.end():]
                after = re.sub(r"^\s*[:：—–―\-]\s*", " ", after).strip()
                gloss = inner.strip() + (f" — {after}" if after else "")
        else:
            sep = "colon" if sm.group("colon") else "dash"
    elif not rest.strip():
        sep = "none"
    elif marked and re.match(r"\s+[A-Za-z\"'‘“(\[]", rest):
        sep = "space"          # "- けれども although ..." — marked bullet, gloss follows directly
        gloss = rest.strip()
    else:
        return None            # prose, or a malformed term continuation ({貯水|ちょすい}{タンク})
    return {"marked": marked, "prefix": prefix, "terms": terms, "sep": sep,
            "gloss": gloss.strip(), "text": line.strip()}


# --------------------------------------------------------------------------- #
# Labels
# --------------------------------------------------------------------------- #
def clean_label(text, max_len=MAX_LABEL_LEN):
    """English-only label: links/furigana/Japanese removed, trimmed, truncated
    at a word boundary (with an ellipsis when truncated)."""
    if not text:
        return ""
    t = LINK_RE.sub(r"\1", text)
    t = strip_furigana(t)
    t = NON_JAPANESE_RE.sub(" \x00 ", t)
    # drop a preposition/article left dangling by the removed Japanese ("kind of 筆記" -> "kind")
    t = re.sub(r"\b(?:of|the|a|an|to|for|with|than|as|in|on|by|from|like|unlike|e\.g\.|i\.e\.)\s+(?=\x00)",
               "", t, flags=re.IGNORECASE)
    t = t.replace("\x00", " ")
    t = re.sub(r"\s+([,;.)])", r"\1", t)
    t = re.sub(r"([,;])(?:\s*[,;])+", r"\1", t)
    t = re.sub(r"\(\s*\)|\[\s*\]|「\s*」", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"^[\s,;:—–\-/·•]+|[\s,;:—–\-/·•(]+$", "", t).strip()
    if TRAILING_STOPWORD_RE.fullmatch(" " + t):
        return ""
    if len(t) > max_len:
        cut = t[:max_len]
        if " " in cut:
            cut = cut[:cut.rfind(" ")]
        cut = TRAILING_STOPWORD_RE.sub("", cut)
        cut = re.sub(r"[\s,;:—–\-/(]+$", "", cut)
        t = cut + "…"
    return t


def short_label(text, max_len=40):
    """House-style label: the gloss part of the bullet only (before the first
    dash/semicolon/colon explanation, trailing parenthetical dropped), then the
    usual cleaning and truncation."""
    if not text:
        return ""
    t = LINK_RE.sub(r"\1", text)
    head = re.split(r"\s+[—–-]\s+|;|:\s", t, maxsplit=1)[0].strip()
    head = re.sub(r"\s*[(（][^)）]*[)）]\s*$", "", head).strip()
    if len(head) < 2:
        head = t
    return clean_label(head, max_len=max_len)


def keigo_label(bullet_text):
    low = bullet_text.lower()
    if "humble" in low or "謙譲" in bullet_text:
        return "humble"
    if "honorific" in low or "respectful" in low or "尊敬" in bullet_text:
        return "honorific"
    if "polite" in low or "丁寧" in bullet_text:
        return "polite"
    return None


def pair_note_from_bullet(bullet, term):
    """'transitive'/'intransitive' the bullet assigns to the pair verb, or None.
    The first keyword after the term wins; a keyword in the prefix label
    ("Intransitive counterpart: …") is the fallback."""
    text = bullet["text"]
    after = text
    idx = text.find(term.raw)
    if idx >= 0:
        after = text[idx + len(term.raw):]
    for chunk in (after, bullet.get("prefix") or ""):
        m = TRANS_KEYWORD_RE.search(chunk)
        if m:
            kw = m.group(0).lower()
            if kw in ("自動詞", "intransitive"):
                return "intransitive"
            return "transitive"
    return None


OPPOSITE = {"transitive": "intransitive", "intransitive": "transitive"}


# --------------------------------------------------------------------------- #
# Resolution
# --------------------------------------------------------------------------- #
def is_affix_of(term_plain, head_plain):
    """True when the term is the headword plus/minus a short affix (〜的, 発揮する …)."""
    if not head_plain or term_plain == head_plain:
        return False
    if AFFIX_MARK_RE.search(term_plain):
        return True
    longer, shorter = (term_plain, head_plain) if len(term_plain) > len(head_plain) else (head_plain, term_plain)
    diff = len(longer) - len(shorter)
    if 0 < diff <= 2 and (longer.startswith(shorter) or longer.endswith(shorter)):
        return True
    return False


def resolve_term(term, source, index):
    """Resolve a Term to exactly one EntryInfo. Returns (info|None, reason)."""
    plain = term.plain
    if not plain:
        return None, "no-term"
    if AFFIX_MARK_RE.search(plain) or is_affix_of(plain, source.headword_plain):
        return None, "suffix"
    if plain == source.headword_plain or (term.link_id and term.link_id == source.id):
        return None, "self"
    if plain in METALANGUAGE:
        return None, "metalanguage"
    if len(plain) == 1 and is_kana_only(plain):
        return None, "single-kana"
    if is_kana_only(plain) and normalize_reading(plain) in PARTICLES \
            and not (GRAMMATICAL_SOURCE_POS & set(source.pos)):
        return None, "particle"
    if term.link_noentry:
        return None, "noentry-link"
    if term.link_id:
        info = index.get(term.link_id)
        if info is not None:
            if info.id == source.id:
                return None, "self"
            return info, "link"
        # stale link id: fall through to text resolution
    if is_kana_only(plain):
        cands = index.kana_matches(plain)
        how = "kana"
    else:
        cands = index.headword_matches(plain, term.reading)
        how = "headword"
        if not cands:
            # 解消する listed but only the noun 解消 exists (or 有能な -> 有能)
            for tail_re, tag in ((SURU_TAIL_RE, "headword-suru"), (NA_TAIL_RE, "headword-na")):
                m = tail_re.search(plain)
                if m and len(plain) > len(m.group(0)):
                    base = plain[:m.start()]
                    if KANJI_CHAR_RE.search(base) and base != source.headword_plain:
                        reading = term.reading[:len(term.reading) - len(m.group(0))] if term.reading else None
                        cands = index.headword_matches(base, reading)
                        if cands:
                            how = tag
                            break
    if not cands:
        return None, "no-entry"
    if len(cands) > 1:
        return None, "ambiguous"
    if cands[0].id == source.id:
        return None, "self"
    return cands[0], how


def pos_compatible(a_pos, b_pos):
    """Loose part-of-speech agreement (noun-ish, verb, adjective, adverb, grammatical)."""
    ca = {POS_CLASSES.get(p) for p in (a_pos or []) if p in POS_CLASSES}
    cb = {POS_CLASSES.get(p) for p in (b_pos or []) if p in POS_CLASSES}
    if not ca or not cb or "x" in ca or "x" in cb:
        return True
    return bool(ca & cb)


# --------------------------------------------------------------------------- #
# Proposals
# --------------------------------------------------------------------------- #
class Proposal:
    __slots__ = ("kind", "source_id", "target_id", "type", "label", "note", "header",
                 "family", "bullet", "how", "reciprocal_of", "dropped")

    def __init__(self, kind, source_id, target_id, ref_type, label=None, note=None,
                 header=None, family=None, bullet=None, how=None, reciprocal_of=None):
        self.kind = kind                # "cr" (cross_references) or "psa" (prominent_see_also)
        self.source_id = source_id
        self.target_id = target_id
        self.type = ref_type            # cross-reference type, or "pair" for psa
        self.label = label
        self.note = note
        self.header = header
        self.family = family
        self.bullet = bullet
        self.how = how
        self.reciprocal_of = reciprocal_of
        self.dropped = None

    def to_item(self, index):
        target = index.get(self.target_id)
        if self.kind == "psa":
            return {"target_id": target.id, "reading": target.reading,
                    "headword": target.headword, "note": self.note}
        item = {"type": self.type, "target_id": target.id, "reading": target.reading,
                "headword": target.headword}
        if self.label:
            item["label"] = self.label
        return item

    def to_dict(self):
        return {k: getattr(self, k) for k in self.__slots__}


class Harvest:
    """Result of a harvesting pass."""

    def __init__(self):
        self.proposals = []             # accepted Proposal objects (direct + reciprocal)
        self.skipped = Counter()        # reason -> count
        self.skip_examples = {}         # reason -> [(entry_id, header, bullet)]
        self.header_how = Counter()     # canonical/alias/fuzzy/other-canonical/non-word/unknown
        self.headers_seen = Counter()   # raw normalised header -> count (harvested only)
        self.entries_scanned = 0
        self.entries_with_sections = 0
        self.bullets = 0
        self.terms = 0
        self.keigo_reverse_skipped = []
        self.over_cap = {}              # entry_id -> dropped count
        self.per_entry = OrderedDict()  # entry_id -> [Proposal]

    def skip(self, reason, entry_id=None, header=None, bullet=None):
        self.skipped[reason] += 1
        ex = self.skip_examples.setdefault(reason, [])
        if len(ex) < 5 and entry_id:
            ex.append((entry_id, header, bullet))


def harvest_entry(source, index, harvest):
    """Direct proposals for one entry (source.notes must be loaded)."""
    out = []
    seen_targets = set()
    notes = source.notes or ""
    if not notes:
        return out
    had_section = False
    for header_raw, lines in iter_sections(notes):
        family, ref_type, how = classify_header(header_raw)
        harvest.header_how[how] += 1
        if family is None:
            continue
        had_section = True
        harvest.headers_seen[_norm_header(header_raw)] += 1
        for line in lines:
            bullet = parse_bullet(line)
            if bullet is None:
                continue
            harvest.bullets += 1
            if family == "TRANSITIVITY":
                prefix = (bullet.get("prefix") or "").lower()
                if prefix and not re.search(r"pair|counterpart|partner|equivalent|opposite|form|version", prefix):
                    harvest.skip("transitivity-other-bullet", source.id, header_raw, bullet["text"])
                    continue
            for term in bullet["terms"]:
                harvest.terms += 1
                target, reason = resolve_term(term, source, index)
                if target is None:
                    harvest.skip(reason, source.id, header_raw, bullet["text"])
                    continue
                if target.id in seen_targets:
                    harvest.skip("duplicate-in-notes", source.id, header_raw, bullet["text"])
                    continue
                if source.references(target):
                    harvest.skip("exists", source.id, header_raw, bullet["text"])
                    continue
                if family == "TRANSITIVITY":
                    note = pair_note_from_bullet(bullet, term)
                    if note is None:
                        harvest.skip("transitivity-no-keyword", source.id, header_raw, bullet["text"])
                        continue
                    if not target.is_verb:
                        harvest.skip("transitivity-not-a-verb", source.id, header_raw, bullet["text"])
                        continue
                    if (source.transitivity in OPPOSITE and source.transitivity == note) or \
                       (target.transitivity in OPPOSITE and target.transitivity != note):
                        harvest.skip("transitivity-conflict", source.id, header_raw, bullet["text"])
                        continue
                    seen_targets.add(target.id)
                    out.append(Proposal("psa", source.id, target.id, "pair", note=note,
                                        header=header_raw, family=family,
                                        bullet=bullet["text"], how=reason))
                    continue
                # A morphological transitivity pair (固める/固まる) listed under SIMILAR/RELATED
                # belongs in prominent_see_also, not cross_references.
                if source.is_verb and target.is_verb and source.transitivity in OPPOSITE \
                        and target.transitivity == OPPOSITE[source.transitivity] \
                        and "verb-suru" not in source.pos and "verb-suru" not in target.pos \
                        and source.headword_plain[:1] == target.headword_plain[:1]:
                    harvest.skip("transitivity-pair", source.id, header_raw, bullet["text"])
                    continue
                this_type = ref_type
                if this_type in ("synonym", "contrast", "related", "antonym") \
                        and source.reading_norm == target.reading_norm:
                    this_type = "homophone"     # 人名 / 人命: same reading, different word
                if this_type == "keigo" and keigo_label(bullet["text"]) is None:
                    harvest.skip("keigo-no-keyword", source.id, header_raw, bullet["text"])
                    continue
                if reason == "kana" and this_type in ("synonym", "contrast", "antonym") \
                        and not pos_compatible(source.pos, target.pos):
                    harvest.skip("kana-pos-mismatch", source.id, header_raw, bullet["text"])
                    continue
                gloss_text = bullet["gloss"]
                gloss_plain = clean_label(gloss_text, max_len=10_000)
                if this_type in ("synonym", "contrast", "related") and ANTONYM_HINT_RE.search(gloss_plain) \
                        and not SYNONYM_CUE_RE.search(gloss_plain) \
                        and not META_WORD_RE.search(first_gloss(target.gloss) + " " + first_gloss(source.gloss)):
                    this_type = "antonym"
                elif this_type == "synonym" and CONTRAST_HINT_RE.search(gloss_plain):
                    this_type = "contrast"
                elif this_type == "synonym" and (
                        (target.headword_plain in source.headword_plain
                         and len(source.headword_plain) - len(target.headword_plain) > 2)
                        or (source.headword_plain in target.headword_plain
                            and len(target.headword_plain) - len(source.headword_plain) > 2)):
                    this_type = "related"        # 見返りを求める -> 見返り: a phrase and its component word
                if this_type == "keigo":
                    label = keigo_label(bullet["text"])
                else:
                    label = short_label(gloss_text)
                if not label:
                    label = first_gloss(target.gloss)
                assert this_type in CROSS_REF_TYPES, this_type
                seen_targets.add(target.id)
                out.append(Proposal("cr", source.id, target.id, this_type, label=label,
                                    header=header_raw, family=family, bullet=bullet["text"],
                                    how=reason))
    if had_section:
        harvest.entries_with_sections += 1
    return out


def add_reciprocals(direct, index, harvest):
    """Back-links on targets that have no reference to the source yet."""
    planned = {(p.source_id, p.target_id) for p in direct}
    recips = []
    for p in direct:
        if (p.target_id, p.source_id) in planned:
            continue
        target = index.get(p.target_id)
        source = index.get(p.source_id)
        if target.references(source):
            continue
        if p.kind == "psa":
            back_note = source.transitivity if source.transitivity in OPPOSITE else OPPOSITE[p.note]
            recips.append(Proposal("psa", target.id, source.id, "pair", note=back_note,
                                   header=p.header, family=p.family, bullet=p.bullet,
                                   how="reciprocal", reciprocal_of=p.source_id))
        elif p.type in RECIPROCAL_TYPES:
            recips.append(Proposal("cr", target.id, source.id, p.type,
                                   label=first_gloss(source.gloss) or None,
                                   header=p.header, family=p.family, bullet=p.bullet,
                                   how="reciprocal", reciprocal_of=p.source_id))
        elif p.type == "keigo":
            harvest.keigo_reverse_skipped.append((p.source_id, p.target_id))
        planned.add((p.target_id, p.source_id))
    return recips


def apply_cap(proposals, harvest, cap=MAX_NEW_REFS_PER_ENTRY):
    """Group by source entry; keep at most `cap` new cross_references each
    (direct proposals first, then reciprocals). psa items are not capped."""
    per_entry = OrderedDict()
    for p in proposals:
        per_entry.setdefault(p.source_id, []).append(p)
    kept = []
    for eid, plist in per_entry.items():
        ordered = [p for p in plist if p.how != "reciprocal"] + [p for p in plist if p.how == "reciprocal"]
        n_cr = 0
        for p in ordered:
            if p.kind == "cr":
                n_cr += 1
                if n_cr > cap:
                    p.dropped = "cap"
                    harvest.over_cap[eid] = harvest.over_cap.get(eid, 0) + 1
                    harvest.skip("cap")
                    continue
            kept.append(p)
    return kept


def run_harvest(index, source_ids, reciprocal=True):
    harvest = Harvest()
    direct = []
    for eid in source_ids:
        info = index.get(eid)
        if info is None:
            continue
        harvest.entries_scanned += 1
        direct.extend(harvest_entry(info, index, harvest))
    proposals = list(direct)
    if reciprocal:
        proposals.extend(add_reciprocals(direct, index, harvest))
    proposals = apply_cap(proposals, harvest)
    harvest.proposals = proposals
    for p in proposals:
        harvest.per_entry.setdefault(p.source_id, []).append(p)
    return harvest


# --------------------------------------------------------------------------- #
# Applying
# --------------------------------------------------------------------------- #
def apply_proposals(harvest, index, modified=None):
    """Append the accepted items to their entry files. Returns list of changed ids."""
    changed = []
    stamp = modified or utc_now()
    for eid, plist in harvest.per_entry.items():
        info = index.get(eid)
        entry, nl = read_entry(info.path)
        cr = entry.get("cross_references")
        psa = entry.get("prominent_see_also")
        cr = list(cr) if isinstance(cr, list) else []
        psa = list(psa) if isinstance(psa, list) else []
        added = False
        for p in plist:
            item = p.to_item(index)
            if p.kind == "cr":
                if any(isinstance(x, dict) and x.get("target_id") == item["target_id"] for x in cr):
                    continue
                cr.append(item)
            else:
                if any(isinstance(x, dict) and x.get("target_id") == item["target_id"] for x in psa):
                    continue
                psa.append(item)
            added = True
        if not added:
            continue
        if any(p.kind == "cr" for p in plist):
            insert_key_before_metadata(entry, "cross_references", cr)
        if any(p.kind == "psa" for p in plist):
            insert_key_before_metadata(entry, "prominent_see_also", psa)
        write_entry(info.path, entry, trailing_newline=nl, modified=stamp)
        changed.append(eid)
    return changed


# --------------------------------------------------------------------------- #
# Output
# --------------------------------------------------------------------------- #
def describe(p, index):
    s, t = index.get(p.source_id), index.get(p.target_id)
    tag = p.type if p.kind == "cr" else f"psa:{p.note}"
    extra = f' label="{p.label}"' if p.kind == "cr" and p.label else ""
    rec = " (reciprocal)" if p.how == "reciprocal" else ""
    return (f"[{tag}] {s.id} {s.headword_plain} → {t.id} {t.headword_plain} "
            f"({t.reading}; {first_gloss(t.gloss)}){extra}{rec}")


def print_proposals(harvest, index):
    for eid, plist in harvest.per_entry.items():
        info = index.get(eid)
        print(f"\n{eid} {info.headword_plain} ({info.reading})")
        for p in plist:
            print("  + " + describe(p, index))


def print_sample(harvest, index, n, seed):
    pool = [p for p in harvest.proposals if p.how != "reciprocal"]
    rng = random.Random(seed)
    sample = rng.sample(pool, min(n, len(pool)))
    print(f"\n=== Sample of {len(sample)} direct proposals (seed {seed}) ===")
    for i, p in enumerate(sample, 1):
        s, t = index.get(p.source_id), index.get(p.target_id)
        print(f"\n#{i} {describe(p, index)}")
        print(f"    source gloss: {s.gloss}")
        print(f"    header: {p.header}   via: {p.how}")
        print(f"    bullet: {p.bullet}")


def print_report(harvest, index, applied=None):
    print("\n=== Cross-reference harvest report ===")
    print(f"Entries scanned: {harvest.entries_scanned}  "
          f"(with harvestable sections: {harvest.entries_with_sections})")
    print(f"Bullets parsed: {harvest.bullets}  terms: {harvest.terms}")
    direct = [p for p in harvest.proposals if p.how != "reciprocal"]
    recip = [p for p in harvest.proposals if p.how == "reciprocal"]
    print(f"Proposals accepted: {len(harvest.proposals)} "
          f"(direct {len(direct)}, reciprocal {len(recip)}) on {len(harvest.per_entry)} entries")
    by_type = Counter((p.type if p.kind == "cr" else "psa-pair") for p in harvest.proposals)
    print("  by type: " + ", ".join(f"{k} {v}" for k, v in by_type.most_common()))
    by_family = Counter(p.family for p in direct)
    print("  by header family (direct): " + ", ".join(f"{k} {v}" for k, v in by_family.most_common()))
    by_how = Counter(p.how for p in direct)
    print("  resolved via (direct): " + ", ".join(f"{k} {v}" for k, v in by_how.most_common()))
    print("  top headers: " + ", ".join(f"{k} {v}" for k, v in harvest.headers_seen.most_common(12)))
    print("  header classification: " + ", ".join(f"{k} {v}" for k, v in harvest.header_how.most_common()))
    print("Skipped by reason: " + ", ".join(f"{k} {v}" for k, v in harvest.skipped.most_common()))
    print(f"Keigo reverse links not written (direction unknown): {len(harvest.keigo_reverse_skipped)}")
    if harvest.over_cap:
        worst = sorted(harvest.over_cap.items(), key=lambda kv: -kv[1])
        print(f"Entries over the cap of {MAX_NEW_REFS_PER_ENTRY} new cross_references: {len(worst)}"
              " — " + ", ".join(f"{e} (+{n} dropped)" for e, n in worst[:15]))
    if index.errors:
        print(f"Unreadable entry files: {len(index.errors)}")
    if applied is not None:
        print(f"APPLIED: {len(applied)} entry files rewritten")
    else:
        print("DRY RUN: no files changed (use --apply)")


def harvest_to_json(harvest, index):
    return {
        "generated": utc_now(),
        "entries_scanned": harvest.entries_scanned,
        "proposals": [dict(p.to_dict(), item=p.to_item(index)) for p in harvest.proposals],
        "skipped": dict(harvest.skipped),
        "skip_examples": {k: v for k, v in harvest.skip_examples.items()},
        "over_cap": harvest.over_cap,
        "keigo_reverse_skipped": harvest.keigo_reverse_skipped,
    }


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def parse_id_list(text):
    ids = set()
    for tok in re.split(r"[,\s]+", text or ""):
        tok = tok.strip()
        if not tok:
            continue
        n = numeric_id(tok) if not tok.isdigit() else int(tok)
        if n is not None:
            ids.add(n)
    return ids


def select_sources(index, ids=None, id_range=None):
    out = []
    for eid, info in index.entries.items():
        n = numeric_id(eid)
        if ids is not None and n not in ids:
            continue
        if id_range is not None and not (id_range[0] <= n <= id_range[1]):
            continue
        out.append(eid)
    return sorted(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Harvest cross-references from note bullets (dry run by default).")
    ap.add_argument("--apply", action="store_true", help="Write the proposals into the entry files.")
    ap.add_argument("--dry-run", action="store_true", help="(default) Show proposals without writing.")
    ap.add_argument("--ids", help="Comma-separated entry IDs (5-digit or full id) to harvest from.")
    ap.add_argument("--ids-file", help="File with one entry ID per line.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--entries-dir", default=str(ENTRIES_DIR),
                    help="Entries directory to read AND write (use a copy for testing).")
    ap.add_argument("--reciprocal", dest="reciprocal", action="store_true", default=True,
                    help="(default) Also add back-links on target entries.")
    ap.add_argument("--no-reciprocal", dest="reciprocal", action="store_false")
    ap.add_argument("--report", action="store_true", help="Print totals only (no per-entry listing).")
    ap.add_argument("--sample", type=int, metavar="N", help="Print N random direct proposals with their bullets.")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--json", metavar="PATH", help="Dump all proposals and skip counts as JSON.")
    args = ap.parse_args(argv)

    if args.apply and args.dry_run:
        ap.error("--apply and --dry-run are mutually exclusive")

    ids = None
    if args.ids:
        ids = parse_id_list(args.ids)
    if args.ids_file:
        ids = (ids or set()) | parse_id_list(Path(args.ids_file).read_text(encoding="utf-8"))
    id_range = tuple(args.range) if args.range else None

    entries_dir = Path(args.entries_dir)
    if not entries_dir.is_dir():
        print(f"Not a directory: {entries_dir}", file=sys.stderr)
        return 1

    def keep_notes(n):
        if ids is not None and n not in ids:
            return False
        if id_range is not None and not (id_range[0] <= n <= id_range[1]):
            return False
        return True

    print(f"Loading index from {entries_dir} …", file=sys.stderr)
    index = load_index(entries_dir, keep_notes_for=keep_notes)
    sources = select_sources(index, ids, id_range)
    print(f"  {len(index.entries)} entries indexed; harvesting {len(sources)} source entries",
          file=sys.stderr)

    harvest = run_harvest(index, sources, reciprocal=args.reciprocal)

    if not args.report and not args.sample:
        print_proposals(harvest, index)
    if args.sample:
        print_sample(harvest, index, args.sample, args.seed)
    applied = None
    if args.apply:
        applied = apply_proposals(harvest, index)
    if args.json:
        Path(args.json).write_text(json.dumps(harvest_to_json(harvest, index), ensure_ascii=False, indent=1),
                                   encoding="utf-8")
        print(f"JSON written to {args.json}", file=sys.stderr)
    print_report(harvest, index, applied)
    return 0


if __name__ == "__main__":
    sys.exit(main())
