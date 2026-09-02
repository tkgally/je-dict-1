"""Unit tests for build/backfill_register.py — politeness/formality/tier
backfill decisions and hold-out rules. Run with:
    python3 -m unittest build.tests.test_backfill_register
"""
import importlib.util
import sys
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_spec = importlib.util.spec_from_file_location("backfill_register", _BUILD / "backfill_register.py")
br = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(br)


def _entry(notes="", pos=("noun",), headword="{犬|いぬ}", tags=None, tier="general", gloss="dog", defs=None):
    t = {"pos": list(pos)}
    if tags:
        t.update(tags)
    md = {"created": "2026-01-01T00:00:01Z", "modified": "2026-01-01T00:00:01Z", "tags": t}
    if tier is not None:
        md["vocabulary_tier"] = tier
    return {"id": "00001_inu", "headword": headword, "reading": "いぬ", "part_of_speech": "noun",
            "gloss": gloss, "definitions": defs or [], "notes": notes, "metadata": md}


class TestPoliteness(unittest.TestCase):
    def test_plain_by_default(self):
        self.assertEqual(br.politeness_decision(_entry("A common animal.")), ("set", "plain"))

    def test_existing_value_skipped(self):
        self.assertEqual(br.politeness_decision(_entry(tags={"politeness": "polite"})), ("skip", None))

    def test_keyword_holds(self):
        for text in ("This is the HONORIFIC form.", "a humble verb", "used in keigo", "the polite form is",
                     "polite forms:", "敬語です", "尊敬語", "謙譲語", "丁寧語"):
            kind, reasons = br.politeness_decision(_entry(text))
            self.assertEqual(kind, "hold", text)
            self.assertTrue(reasons, text)

    def test_keyword_in_definition_counts(self):
        e = _entry(defs=[{"sense_number": 1, "gloss": "x", "explanation": "Humble equivalent of 言う."}])
        self.assertEqual(br.politeness_decision(e)[0], "hold")

    def test_masu_headword_holds_only_for_expressions(self):
        e = _entry(pos=("expression",), headword="お{疲|つか}れ{様|さま}でございます")
        kind, reasons = br.politeness_decision(e)
        self.assertEqual(kind, "hold")
        self.assertIn("headword contains ます/ございます", reasons)
        e = _entry(pos=("noun",), headword="ます")   # a plain noun spelled ます is not a marker
        self.assertEqual(br.politeness_decision(e), ("set", "plain"))


class TestFormality(unittest.TestCase):
    def test_neutral_by_default(self):
        self.assertEqual(br.formality_decision(_entry("A common animal.")), ("set", "neutral"))

    def test_keyword_holds(self):
        for text in ("Formal.", "informal speech", "quite casual", "slang", "vulgar", "literary word",
                     "mostly written", "colloquial", "sounds rough", "書き言葉", "話し言葉", "formality varies"):
            self.assertEqual(br.formality_decision(_entry(text))[0], "hold", text)

    def test_false_friends_do_not_hold(self):
        for text in ("through the door", "roughly 3 km", "thoroughly", "casualty count", "unwritten"):
            self.assertEqual(br.formality_decision(_entry(text)), ("set", "neutral"), text)

    def test_style_tag_holds(self):
        kind, reasons = br.formality_decision(_entry(tags={"style": ["literary"]}))
        self.assertEqual(kind, "hold")
        self.assertIn("tags.style=['literary']", reasons)

    def test_existing_value_skipped(self):
        self.assertEqual(br.formality_decision(_entry(tags={"formality": "formal"})), ("skip", None))


class TestProcessEntry(unittest.TestCase):
    def test_sets_both_and_keeps_key_order(self):
        e = _entry()
        e["metadata"]["tags"] = {"pos": ["noun"], "semantic": ["animal-mammal"]}
        changed, holds = br.process_entry(e, {"politeness", "formality"})
        self.assertEqual(sorted(changed), ["formality", "politeness"])
        self.assertEqual(holds, [])
        self.assertEqual(list(e["metadata"]["tags"].keys()), ["pos", "formality", "politeness", "semantic"])
        self.assertEqual(e["metadata"]["tags"]["politeness"], "plain")
        self.assertEqual(e["metadata"]["tags"]["formality"], "neutral")

    def test_null_values_are_filled(self):
        e = _entry(tags={"politeness": None, "formality": None})
        changed, _ = br.process_entry(e, {"politeness", "formality"})
        self.assertEqual(sorted(changed), ["formality", "politeness"])

    def test_holds_leave_value_untouched(self):
        e = _entry("honorific form; formal")
        changed, holds = br.process_entry(e, {"politeness", "formality"})
        self.assertEqual(changed, [])
        self.assertEqual({h[0] for h in holds}, {"politeness", "formality"})
        self.assertNotIn("politeness", e["metadata"]["tags"])

    def test_only_selected_fields(self):
        e = _entry()
        changed, _ = br.process_entry(e, {"politeness"})
        self.assertEqual(changed, ["politeness"])
        self.assertNotIn("formality", e["metadata"]["tags"])

    def test_tier_backfill(self):
        e = _entry(tier=None)
        changed, _ = br.process_entry(e, {"tier"})
        self.assertEqual(changed, ["vocabulary_tier"])
        self.assertEqual(e["metadata"]["vocabulary_tier"], "general")
        e = _entry(tier="core")
        self.assertEqual(br.process_entry(e, {"tier"})[0], [])
        self.assertEqual(e["metadata"]["vocabulary_tier"], "core")


if __name__ == "__main__":
    unittest.main()
