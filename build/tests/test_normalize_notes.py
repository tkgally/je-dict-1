"""Unit tests for build/normalize_notes.py — header detection, alias renaming,
bullet conversion, duplicate-section merging and the "touch nothing else" rule.
Run with:
    python3 -m unittest build.tests.test_normalize_notes
"""
import importlib.util
import sys
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_spec = importlib.util.spec_from_file_location("normalize_notes", _BUILD / "normalize_notes.py")
nn = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(nn)

VOCAB = nn.load_header_vocab()


class TestHeaderDetection(unittest.TestCase):
    def test_plain_headers(self):
        self.assertEqual(nn.header_body("USAGE:"), "USAGE")
        self.assertEqual(nn.header_body("COMMON COLLOCATIONS: "), "COMMON COLLOCATIONS")
        self.assertEqual(nn.header_body("ASPECT (ている):"), "ASPECT (ている)")
        self.assertEqual(nn.header_body("TRANSITIVE/INTRANSITIVE:"), "TRANSITIVE/INTRANSITIVE")
        self.assertEqual(nn.header_body("DON'T CONFUSE:"), "DON'T CONFUSE")
        self.assertEqual(nn.header_body("ている:"), "ている")

    def test_qualified_and_decorated_headers_are_headers(self):
        self.assertEqual(nn.header_body("COMMON COLLOCATIONS (sense 1):"), "COMMON COLLOCATIONS (sense 1)")
        self.assertEqual(nn.header_body("RELATED ～{力|りょく} COMPOUNDS:"), "RELATED ～{力|りょく} COMPOUNDS")
        self.assertEqual(nn.header_body("ASPECT (⟦ている→ている：noentry⟧):"), "ASPECT (⟦ている→ている：noentry⟧)")

    def test_non_headers(self):
        self.assertIsNone(nn.header_body("NOTE: this verb is transitive"))   # no trailing colon
        self.assertIsNone(nn.header_body("- NHK:"))                          # bullet
        self.assertIsNone(nn.header_body("・NHK:"))
        self.assertIsNone(nn.header_body(" USAGE:"))                         # not at column 0
        self.assertIsNone(nn.header_body("Important:"))                      # lowercase
        self.assertIsNone(nn.header_body("2024:"))                           # no letters
        self.assertIsNone(nn.header_body(":"))
        self.assertIsNone(nn.header_body(""))
        self.assertIsNone(nn.header_body("使い方:"))                          # kanji outside wrappers

    def test_alias_lookup(self):
        self.assertEqual(VOCAB[nn.header_key("collocations")], "COMMON COLLOCATIONS")
        self.assertEqual(VOCAB[nn.header_key("Usage   Note:")], "USAGE")
        self.assertEqual(VOCAB[nn.header_key("ASPECT (⟦ている→ている：noentry⟧)")], "ASPECT (ている)")
        self.assertEqual(VOCAB[nn.header_key("CULTURAL NOTE:")], "CULTURAL NOTE")
        self.assertNotIn(nn.header_key("ZZZ UNKNOWN SECTION"), VOCAB)


class TestBullets(unittest.TestCase):
    def test_dot_bullets(self):
        self.assertEqual(nn.convert_bullet("・{犬|いぬ}: dog"), "- {犬|いぬ}: dog")
        self.assertEqual(nn.convert_bullet("・ spaced"), "- spaced")
        self.assertEqual(nn.convert_bullet("  ・indented"), "  - indented")
        self.assertEqual(nn.convert_bullet("• bullet"), "- bullet")

    def test_dash_bullets_need_a_space(self):
        self.assertEqual(nn.convert_bullet("– en dash"), "- en dash")
        self.assertEqual(nn.convert_bullet("‐ hyphen"), "- hyphen")
        self.assertIsNone(nn.convert_bullet("–3 degrees"))

    def test_not_bullets(self):
        self.assertIsNone(nn.convert_bullet("- already fine"))
        self.assertIsNone(nn.convert_bullet("・"))
        self.assertIsNone(nn.convert_bullet("plain ・ inside"))


class TestNormalizeNotes(unittest.TestCase):
    def test_rename_and_bullets(self):
        notes = "Intro prose.\n\nCOLLOCATIONS:\n・{本|ほん}を{読|よ}む: read a book\n・{読|よ}み{方|かた}: how to read"
        out, ch = nn.normalize_notes(notes, VOCAB)
        self.assertEqual(out, "Intro prose.\n\nCOMMON COLLOCATIONS:\n- {本|ほん}を{読|よ}む: read a book\n- {読|よ}み{方|かた}: how to read")
        self.assertEqual(ch.renamed[("COLLOCATIONS", "COMMON COLLOCATIONS")], 1)
        self.assertEqual(ch.bullets, 2)
        self.assertTrue(ch.changed)

    def test_merge_duplicate_sections(self):
        notes = ("COMMON PATTERNS:\n- A が B\n\nUSAGE:\nSome prose.\n\nPARTICLE PATTERNS:\n- ～に C\n\nETYMOLOGY:\nOld.")
        out, ch = nn.normalize_notes(notes, VOCAB)
        self.assertEqual(out, "COMMON PATTERNS:\n- A が B\n- ～に C\n\nUSAGE:\nSome prose.\n\nETYMOLOGY:\nOld.")
        self.assertEqual(ch.merged["COMMON PATTERNS"], 1)

    def test_merge_when_duplicate_is_last_section(self):
        notes = "USAGE:\nFirst.\n\nSIMILAR WORDS:\n- x\n\nNOTE:\nSecond."
        out, _ = nn.normalize_notes(notes, VOCAB)
        self.assertEqual(out, "USAGE:\nFirst.\nSecond.\n\nSIMILAR WORDS:\n- x")

    def test_unknown_headers_reported_not_renamed(self):
        notes = "ZZZ UNKNOWN SECTION:\n- {日|にち}: sun\n\nUSAGE:\nx"
        out, ch = nn.normalize_notes(notes, VOCAB)
        self.assertEqual(out, notes)
        self.assertEqual(ch.unknown["ZZZ UNKNOWN SECTION"], 1)
        self.assertFalse(ch.changed)
        self.assertEqual(nn.unknown_headers(notes, VOCAB), ["ZZZ UNKNOWN SECTION"])

    def test_unknown_duplicates_are_not_merged(self):
        notes = "ZZZ UNKNOWN SECTION:\na\n\nZZZ UNKNOWN SECTION:\nb"
        out, ch = nn.normalize_notes(notes, VOCAB)
        self.assertEqual(out, notes)

    def test_blank_run_collapse(self):
        notes = "USAGE:\na\n\n\n\nCOMMON COLLOCATIONS:\n- b"
        out, ch = nn.normalize_notes(notes, VOCAB)
        self.assertEqual(out, "USAGE:\na\n\nCOMMON COLLOCATIONS:\n- b")
        self.assertEqual(ch.blank_runs, 1)

    def test_prose_and_inline_headers_untouched(self):
        notes = ("NOTE: this line is prose, not a header.\nThe word COLLOCATIONS: appears mid-line? no, at start but with text.\n"
                 "- NHK: broadcaster\n・ bullet with ・ inside ・ stays")
        out, ch = nn.normalize_notes(notes, VOCAB)
        self.assertEqual(out, notes.replace("・ bullet with", "- bullet with"))
        self.assertEqual(ch.bullets, 1)
        self.assertEqual(ch.renamed, {})

    def test_link_in_header_reduced_to_canonical(self):
        notes = "ASPECT (⟦ている→ている：noentry⟧):\n{走|はし}っている = running."
        out, ch = nn.normalize_notes(notes, VOCAB)
        self.assertEqual(out, "ASPECT (ている):\n{走|はし}っている = running.")

    def test_idempotent_and_trailing_newline_policy(self):
        notes = "Intro.\n\nNOTE:\n・a\n\nUSAGE NOTES:\n・b\n"
        once, ch1 = nn.normalize_notes(notes, VOCAB)
        twice, ch2 = nn.normalize_notes(once, VOCAB)
        self.assertEqual(once, twice)
        self.assertFalse(ch2.changed)
        self.assertEqual(once, "Intro.\n\nUSAGE:\n- a\n- b\n")
        no_nl, _ = nn.normalize_notes(notes.rstrip("\n"), VOCAB)
        self.assertFalse(no_nl.endswith("\n"))

    def test_empty_notes(self):
        self.assertEqual(nn.normalize_notes("", VOCAB), ("", nn.NotesChange()))


if __name__ == "__main__":
    unittest.main()
