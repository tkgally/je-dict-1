"""Unit tests for the U+FFFD mojibake guard in build/validate.py.

The guard (find_mojibake_errors) is a hard CI regression check against the
2026-06 batch-creation corruption episode: any entry whose text carries a
U+FFFD replacement character must fail validation. Run with:
    python3 -m unittest build.tests.test_validate_mojibake
"""
import importlib.util
import sys
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_MOD = _BUILD / "validate.py"
_spec = importlib.util.spec_from_file_location("validate", _MOD)
validate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validate)

FFFD = "�"


def _entry(**overrides):
    base = {
        "id": "00001_test",
        "headword": "漢字",
        "reading": "かんじ",
        "examples": [{"japanese": "{漢字|かんじ}を{書|か}く。", "english": "Write kanji."}],
        "notes": "A clean note.",
    }
    base.update(overrides)
    return base


class TestMojibakeGuard(unittest.TestCase):
    def test_clean_entry_has_no_errors(self):
        self.assertEqual(validate.find_mojibake_errors(_entry()), [])

    def test_fffd_in_reading_flagged(self):
        errs = validate.find_mojibake_errors(_entry(reading=f"かん{FFFD}"))
        self.assertEqual(len(errs), 1)
        self.assertIn("reading", errs[0])
        self.assertIn("U+FFFD", errs[0])

    def test_fffd_in_nested_example_flagged_with_path(self):
        ex = [{"japanese": f"{{漢字|かん{FFFD}じ}}を{{書|か}}く。", "english": "x"}]
        errs = validate.find_mojibake_errors(_entry(examples=ex))
        self.assertEqual(len(errs), 1)
        self.assertIn("examples[0].japanese", errs[0])

    def test_count_reported(self):
        errs = validate.find_mojibake_errors(_entry(notes=f"ab{FFFD}{FFFD}{FFFD}cd"))
        self.assertEqual(len(errs), 1)
        self.assertIn("3 replacement char", errs[0])

    def test_multiple_fields_each_flagged(self):
        errs = validate.find_mojibake_errors(
            _entry(headword=f"漢{FFFD}", notes=f"x{FFFD}y")
        )
        self.assertEqual(len(errs), 2)

    def test_allowlist_suppresses(self):
        validate.MOJIBAKE_ALLOWLIST.add("00001_test")
        try:
            errs = validate.find_mojibake_errors(_entry(reading=f"かん{FFFD}"))
            self.assertEqual(errs, [])
        finally:
            validate.MOJIBAKE_ALLOWLIST.discard("00001_test")

    def test_validate_entry_file_reports_mojibake(self):
        """End-to-end: a corrupted on-disk entry fails validate_entry_file."""
        import json
        import tempfile

        schema = validate.load_schema(_MOD.parent / "schema.json")
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "00001_test.json"
            entry = {
                "id": "00001_test",
                "headword": "漢字",
                "reading": "かんじ",
                "part_of_speech": "noun",
                "gloss": "kanji",
                "definitions": [{"sense_number": 1, "gloss": "kanji",
                                 "explanation": "Chinese characters."}],
                "examples": [{"id": "00001_test_ex1",
                              "japanese": f"{{漢字|かん{FFFD}じ}}。",
                              "english": "Kanji.", "sense_numbers": [1]}],
                "metadata": {"created": "2026-01-01T00:00:00Z",
                             "modified": "2026-01-01T00:00:00Z",
                             "vocabulary_tier": "general"},
            }
            p.write_text(json.dumps(entry, ensure_ascii=False), encoding="utf-8")
            errors, _ = validate.validate_entry_file(p, schema, set())
            self.assertTrue(any("U+FFFD" in e for e in errors),
                            f"expected a U+FFFD error, got {errors}")


if __name__ == "__main__":
    unittest.main()
