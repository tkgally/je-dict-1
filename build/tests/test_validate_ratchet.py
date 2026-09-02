"""Unit tests for the furigana-brace checks and the --ratchet checks added to
build/validate.py. Run with:
    python3 -m unittest build.tests.test_validate_ratchet
"""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_spec = importlib.util.spec_from_file_location("validate", _BUILD / "validate.py")
validate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validate)


def _entry(**overrides):
    base = {
        "id": "00001_test",
        "headword": "{漢字|かんじ}",
        "reading": "かんじ",
        "part_of_speech": "noun",
        "gloss": "kanji",
        "definitions": [{"sense_number": 1, "gloss": "kanji", "explanation": "Chinese characters."}],
        "examples": [{"id": "00001_test_ex1", "japanese": "{漢字|かんじ}を{書|か}く。",
                      "english": "Write kanji.", "sense_numbers": [1]}],
        "notes": "A clean note.",
        "metadata": {"created": "2026-01-01T00:00:01Z", "modified": "2026-01-01T00:00:01Z",
                     "vocabulary_tier": "general",
                     "tags": {"pos": ["noun"], "formality": "neutral", "politeness": "plain"}},
    }
    base.update(overrides)
    return base


class TestBraceErrors(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(validate.find_furigana_brace_errors(_entry()), [])

    def test_unbalanced_and_nested(self):
        errs = validate.find_furigana_brace_errors(_entry(notes="{チームに{残|のこ}る"))
        self.assertEqual(len(errs), 1)
        self.assertIn("Unbalanced", errs[0])
        self.assertIn("'notes'", errs[0])
        errs = validate.find_furigana_brace_errors(
            _entry(examples=[{"id": "00001_test_ex1", "japanese": "{{誇|ほこ}}り", "english": "x"}]))
        self.assertEqual(len(errs), 1)
        self.assertIn("Nested", errs[0])
        self.assertIn("examples[0].japanese", errs[0])

    def test_metadata_ignored(self):
        e = _entry()
        e["metadata"]["ai_model"] = "{weird"
        self.assertEqual(validate.find_furigana_brace_errors(e), [])

    def test_nested_without_double_brace(self):
        errs = validate.find_furigana_brace_errors(_entry(notes="called {あご{ひも}} sometimes"))
        self.assertEqual(len(errs), 1)
        self.assertIn("Nested", errs[0])
        self.assertEqual(validate.furigana_brace_problem("}{"), "unbalanced")
        self.assertIsNone(validate.furigana_brace_problem("{a|b} and {c|d}"))

    def test_baseline_tolerates_only_listed_fields_unless_ratchet(self):
        old = validate.FURIGANA_BRACE_BASELINE_DATA
        validate.FURIGANA_BRACE_BASELINE_DATA = {"00001_test": ["notes"]}
        try:
            broken = _entry(notes="{未閉")
            self.assertEqual(validate.find_furigana_brace_errors(broken), [])
            self.assertEqual(len(validate.find_furigana_brace_errors(broken, ignore_allowlist=True)), 1)
            # a different broken field in the same entry is still an error
            broken2 = _entry(notes="{未閉", headword="{漢字|かんじ")
            self.assertEqual(len(validate.find_furigana_brace_errors(broken2)), 1)
        finally:
            validate.FURIGANA_BRACE_BASELINE_DATA = old

    def test_collect_and_write_brace_baseline(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "entries" / "00000").mkdir(parents=True)
            good = _entry()
            bad = dict(_entry(notes="{壊れ|こわ"), id="00002_kowa")
            for e in (good, bad):
                (root / "entries" / "00000" / f"{e['id']}.json").write_text(
                    json.dumps(e, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(validate.collect_brace_problems(root / "entries"), {"00002_kowa": ["notes"]})
            out = root / "baseline.json"
            self.assertEqual(validate.write_brace_baseline(root, out), 0)
            self.assertEqual(json.loads(out.read_text(encoding="utf-8"))["entries"], {"00002_kowa": ["notes"]})


class TestBraceWarnings(unittest.TestCase):
    def test_no_pipe_kanji_warns(self):
        w = validate.find_furigana_brace_warnings(_entry(notes="Compare {稀} and {希|まれ}."))
        self.assertEqual(len(w), 1)
        self.assertIn("{稀}", w[0])

    def test_kana_only_or_placeholders_do_not_warn_here(self):
        self.assertEqual(validate.find_furigana_brace_warnings(_entry(notes="{ている} and {verb stem}")), [])


class TestRatchet(unittest.TestCase):
    def test_complete_entry_passes(self):
        self.assertEqual(validate.find_ratchet_errors(_entry()), [])
        self.assertEqual(validate.find_ratchet_warnings(_entry()), [])

    def test_missing_register(self):
        e = _entry()
        e["metadata"]["tags"] = {"pos": ["noun"], "formality": None}
        errs = validate.find_ratchet_errors(e)
        self.assertEqual(len(errs), 2)
        self.assertTrue(any("politeness" in m for m in errs))
        self.assertTrue(any("formality" in m for m in errs))

    def test_transitivity_only_for_godan_ichidan(self):
        e = _entry()
        e["metadata"]["tags"] = {"pos": ["verb-godan"], "formality": "neutral", "politeness": "plain"}
        errs = validate.find_ratchet_errors(e)
        self.assertEqual(len(errs), 1)
        self.assertIn("transitivity", errs[0])
        e["metadata"]["tags"]["pos"] = ["noun", "verb-suru"]
        self.assertEqual(validate.find_ratchet_errors(e), [])
        e["metadata"]["tags"]["pos"] = ["verb-ichidan"]
        e["metadata"]["tags"]["transitivity"] = "transitive"
        self.assertEqual(validate.find_ratchet_errors(e), [])

    def test_kana_only_braces(self):
        errs = validate.find_ratchet_errors(_entry(notes="use {ている} or {どんどん|どんどん}"))
        self.assertEqual(len(errs), 2)
        self.assertIn("{ている}", errs[0])
        # unbalanced strings are the brace-error check's job, not the ratchet's
        self.assertEqual(validate.find_ratchet_errors(_entry(notes="{ている")), [])

    def test_pos_warning(self):
        e = _entry(part_of_speech="godan verb")
        e["metadata"]["tags"]["pos"] = ["verb-godan"]
        e["metadata"]["tags"]["transitivity"] = "transitive"
        w = validate.find_ratchet_warnings(e)
        self.assertEqual(len(w), 1)
        self.assertIn("'verb (godan)'", w[0])
        e["part_of_speech"] = "verb (godan)"
        self.assertEqual(validate.find_ratchet_warnings(e), [])
        e["part_of_speech"] = "noun (proper)"
        e["metadata"]["tags"]["pos"] = ["noun"]
        self.assertIn("reconcile by hand", validate.find_ratchet_warnings(e)[0])

    def test_entry_warnings_respects_flag(self):
        e = _entry(part_of_speech="godan verb", notes="{稀}")
        e["metadata"]["tags"]["pos"] = ["verb-godan"]
        old = validate.RATCHET
        try:
            validate.RATCHET = False
            self.assertEqual(len(validate.entry_warnings(e)), 1)
            validate.RATCHET = True
            self.assertEqual(len(validate.entry_warnings(e)), 2)
        finally:
            validate.RATCHET = old


class TestValidateEntryFileIntegration(unittest.TestCase):
    def _validate(self, entry, ratchet):
        schema = validate.load_schema(_BUILD / "schema.json")
        old = validate.RATCHET
        old_baseline = validate.FURIGANA_BRACE_BASELINE_DATA
        validate.RATCHET = ratchet
        validate.FURIGANA_BRACE_BASELINE_DATA = {}
        try:
            with tempfile.TemporaryDirectory() as d:
                # id/dir/romaji must be self-consistent or validate_entry_file
                # reports placement errors unrelated to what is being tested
                entry = dict(entry, id="00001_kanji")
                for ex in entry.get("examples", []):
                    ex["id"] = ex["id"].replace("00001_test", "00001_kanji")
                sub = Path(d) / "00000"
                sub.mkdir()
                p = sub / "00001_kanji.json"
                p.write_text(json.dumps(entry, ensure_ascii=False), encoding="utf-8")
                errors, _ = validate.validate_entry_file(p, schema, set())
                return errors
        finally:
            validate.RATCHET = old
            validate.FURIGANA_BRACE_BASELINE_DATA = old_baseline

    def test_unbalanced_is_always_an_error(self):
        errors = self._validate(_entry(notes="{壊れ|こわ"), ratchet=False)
        self.assertTrue(any("Unbalanced" in e for e in errors), errors)

    def test_ratchet_errors_only_with_flag(self):
        e = _entry()
        e["metadata"]["tags"] = {"pos": ["noun"]}
        self.assertEqual(self._validate(e, ratchet=False), [])
        errors = self._validate(e, ratchet=True)
        self.assertEqual(len(errors), 2)


if __name__ == "__main__":
    unittest.main()
