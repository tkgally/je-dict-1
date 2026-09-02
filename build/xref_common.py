#!/usr/bin/env python3
"""Shared helpers for the cross-reference tools.

Used by build/harvest_crossrefs.py and build/review_transitivity.py (and their
tests). Provides:

- a light in-memory index of every entry (id, headword, reading, gloss, POS,
  transitivity, existing references, file path, trailing-newline convention)
  built by scanning an entries directory — so a copy under --entries-dir is
  self-consistent and never mixes with the real dictionary;
- reading derivation from furigana-annotated text (`{漢字|かんじ}する` -> かんじする);
- entry writing that preserves each file's own trailing-newline convention
  (about 11% of entry files end without a newline) and stamps metadata.modified.

Nothing here modifies files unless write_entry() is called explicitly.
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from japanese_utils import FURIGANA_PATTERN, strip_furigana, normalize_reading  # noqa: F401

VERB_POS = {"verb-godan", "verb-ichidan", "verb-suru", "verb-kuru", "verb-irregular"}

# ⟦surface→base：id⟧ (surface may contain furigana wrappers)
LINK_RE = re.compile(r"⟦([^⟧→]*)→([^⟧：]*)：([^⟧]*)⟧")
KANA_CHAR = "ぁ-ゖァ-ヺーゝゞヽヾ"
KANJI_CHAR = "㐀-䶿一-鿿豈-﫿々〆ヶヵ〇"
JAPANESE_CHAR_RE = re.compile(f"[{KANA_CHAR}{KANJI_CHAR}]")
KANA_ONLY_RE = re.compile(f"^[{KANA_CHAR}]+$")
KANJI_CHAR_RE = re.compile(f"[{KANJI_CHAR}]")


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def numeric_id(entry_id):
    m = re.match(r"(\d{5})", str(entry_id or ""))
    return int(m.group(1)) if m else None


def links_to_surface(text):
    """Replace every inline link with its surface text (furigana kept)."""
    if not text:
        return ""
    return LINK_RE.sub(r"\1", text)


def plain_text(text):
    """Strip inline links and furigana wrappers: `⟦{速記|そっき}→速記：09668_sokki⟧する` -> 速記する."""
    return strip_furigana(links_to_surface(text or ""))


def is_kana_only(text):
    return bool(text) and bool(KANA_ONLY_RE.match(text))


def derive_reading(surface):
    """Derive the hiragana reading of a furigana-annotated term.

    Furigana wrapper readings are concatenated with any kana outside the
    wrappers (katakana normalised to hiragana). Returns None when the surface
    contains kanji that carry no furigana (reading unknowable) or non-Japanese
    characters such as fullwidth letters.
    """
    surface = links_to_surface(surface or "")
    out = []
    pos = 0
    for m in FURIGANA_PATTERN.finditer(surface):
        gap = surface[pos:m.start()]
        if gap:
            if not KANA_ONLY_RE.match(gap):
                return None
            out.append(normalize_reading(gap))
        out.append(normalize_reading(m.group(2)))
        pos = m.end()
    tail = surface[pos:]
    if tail:
        if not KANA_ONLY_RE.match(tail):
            return None
        out.append(normalize_reading(tail))
    reading = "".join(out)
    return reading or None


def first_gloss(gloss):
    """First semicolon-separated item of a gloss string, trimmed."""
    if not gloss:
        return ""
    return gloss.split(";")[0].strip()


def get_tags(entry):
    meta = entry.get("metadata") or {}
    tags = meta.get("tags") or {}
    return tags if isinstance(tags, dict) else {}


def is_verb_pos(pos_list):
    return any(p in VERB_POS for p in (pos_list or []))


class EntryInfo:
    """Light record for one entry (everything the xref tools need without the full JSON)."""

    __slots__ = ("id", "path", "headword", "headword_plain", "reading", "reading_norm",
                 "gloss", "pos", "transitivity", "refs", "notes", "trailing_newline",
                 "tier")

    def __init__(self, entry, path, trailing_newline, keep_notes=False):
        tags = get_tags(entry)
        self.id = entry.get("id", "")
        self.path = Path(path)
        self.headword = entry.get("headword", "") or ""
        self.headword_plain = strip_furigana(self.headword)
        self.reading = entry.get("reading", "") or ""
        self.reading_norm = normalize_reading(self.reading)
        self.gloss = entry.get("gloss", "") or ""
        self.pos = list(tags.get("pos") or [])
        self.transitivity = tags.get("transitivity")
        self.tier = (entry.get("metadata") or {}).get("vocabulary_tier")
        self.trailing_newline = trailing_newline
        self.notes = (entry.get("notes") or "") if keep_notes else None
        self.refs = []
        for kind in ("cross_references", "prominent_see_also"):
            lst = entry.get(kind) or []
            if not isinstance(lst, list):
                continue
            for ref in lst:
                if not isinstance(ref, dict):
                    continue
                self.refs.append({
                    "kind": kind,
                    "type": ref.get("type"),
                    "target_id": ref.get("target_id"),
                    "reading": normalize_reading(ref.get("reading") or ""),
                    "headword_plain": strip_furigana(ref.get("headword") or ""),
                    "note": ref.get("note"),
                })

    @property
    def is_verb(self):
        return is_verb_pos(self.pos)

    def references(self, target):
        """True if this entry already has any cross_reference or prominent_see_also
        pointing at `target` (an EntryInfo): by target_id, or — for un-hardened
        forward references — by reading plus (when given) headword."""
        for ref in self.refs:
            if ref["target_id"]:
                if ref["target_id"] == target.id:
                    return True
                continue
            if ref["reading"] and ref["reading"] == target.reading_norm:
                if not ref["headword_plain"] or ref["headword_plain"] == target.headword_plain:
                    return True
        return False

    def psa_targets(self):
        return {r["target_id"] for r in self.refs
                if r["kind"] == "prominent_see_also" and r["target_id"]}


class EntryIndex:
    """All entries of one entries directory, with headword/reading lookups."""

    def __init__(self):
        self.entries = {}       # id -> EntryInfo
        self.by_headword = {}   # plain headword -> [ids]
        self.by_reading = {}    # normalised reading -> [ids]
        self.errors = []

    def add(self, info):
        self.entries[info.id] = info
        self.by_headword.setdefault(info.headword_plain, []).append(info.id)
        self.by_reading.setdefault(info.reading_norm, []).append(info.id)

    def get(self, entry_id):
        return self.entries.get(entry_id)

    def headword_matches(self, plain, reading=None):
        """Entries whose plain headword equals `plain` (and reading equals
        `reading` when given). Returns a list of EntryInfo."""
        out = []
        for eid in self.by_headword.get(plain, []):
            info = self.entries[eid]
            if reading is not None and info.reading_norm != normalize_reading(reading):
                continue
            out.append(info)
        return out

    def kana_matches(self, term):
        """Entries whose plain headword OR reading equals a kana-only term."""
        norm = normalize_reading(term)
        ids = []
        for eid in self.by_headword.get(term, []) + self.by_headword.get(norm, []):
            if eid not in ids:
                ids.append(eid)
        for eid in self.by_reading.get(norm, []):
            if eid not in ids:
                ids.append(eid)
        return [self.entries[e] for e in ids]


def iter_entry_files(entries_dir):
    entries_dir = Path(entries_dir)
    for path in sorted(entries_dir.glob("*/*.json")):
        yield path


def read_entry(path):
    """Return (entry_dict, trailing_newline_flag)."""
    raw = Path(path).read_bytes()
    entry = json.loads(raw.decode("utf-8"))
    return entry, raw.endswith(b"\n")


def load_index(entries_dir, keep_notes_for=None):
    """Scan an entries directory into an EntryIndex.

    keep_notes_for: None (keep no notes), True (keep all), or a callable
    taking the numeric id and returning whether to keep that entry's notes.
    """
    index = EntryIndex()
    for path in iter_entry_files(entries_dir):
        try:
            entry, nl = read_entry(path)
        except (json.JSONDecodeError, OSError, UnicodeDecodeError) as exc:
            index.errors.append(f"{path}: {exc}")
            continue
        if not isinstance(entry, dict) or not entry.get("id"):
            index.errors.append(f"{path}: no id")
            continue
        if keep_notes_for is True:
            keep = True
        elif callable(keep_notes_for):
            keep = bool(keep_notes_for(numeric_id(entry["id"])))
        else:
            keep = False
        index.add(EntryInfo(entry, path, nl, keep_notes=keep))
    return index


def insert_key_before_metadata(entry, key, value):
    """Set entry[key] = value; when the key is new, place it just before
    'metadata' so the file layout stays tidy (json.dump keeps insertion order)."""
    if key in entry:
        entry[key] = value
        return entry
    if "metadata" not in entry:
        entry[key] = value
        return entry
    items = list(entry.items())
    entry.clear()
    for k, v in items:
        if k == "metadata":
            entry[key] = value
        entry[k] = v
    return entry


def write_entry(path, entry, trailing_newline=True, modified=None):
    """Write an entry with the project's json.dump conventions, stamping
    metadata.modified and matching the file's original trailing-newline state."""
    meta = entry.setdefault("metadata", {})
    meta["modified"] = modified or utc_now()
    text = json.dumps(entry, ensure_ascii=False, indent=2)
    if trailing_newline:
        text += "\n"
    Path(path).write_text(text, encoding="utf-8")
