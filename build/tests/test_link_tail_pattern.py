"""Unit tests for the inline-link tail pattern shared by the furigana checkers.

The tail of a link (``→baseform：id⟧``) is stripped before furigana checks. The old
pattern ``→[^⟧]*⟧`` also matched from a plain arrow in prose (``食べる → 食べます``)
up to the next link's ``⟧``, swallowing the text between them. Run with:
    python3 -m unittest build.tests.test_link_tail_pattern
"""
import importlib.util
import sys
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))


def _load(name):
    spec = importlib.util.spec_from_file_location(name, _BUILD / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cff = _load("check_furigana_format")
fmf = _load("find_missing_furigana")

TEXT = "{食|た}べる → {食|た}べます: 本 ⟦{本|ほん}→本：00111_hon⟧"


class TestLinkTailPattern(unittest.TestCase):
    def test_prose_arrow_survives_and_link_tail_is_stripped(self):
        self.assertEqual(cff.LINK_TAIL_RE.sub("", TEXT), "{食|た}べる → {食|た}べます: 本 ⟦{本|ほん}")

    def test_bare_kanji_after_prose_arrow_is_still_found(self):
        found, kanji = fmf.contains_unannotated_kanji(TEXT)
        self.assertTrue(found)
        self.assertEqual(kanji, ["本"])

    def test_link_base_form_is_not_counted_as_bare(self):
        self.assertEqual(fmf.contains_unannotated_kanji("⟦{本|ほん}→本：00111_hon⟧"), (False, []))


if __name__ == "__main__":
    unittest.main()
