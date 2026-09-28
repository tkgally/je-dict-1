"""A cross-reference must carry a target_id or a label (build/schema.json).

A bare {type, reading, headword} reference passed validation until 2026-09-28
and 46 of them accumulated (tooling backlog 51). Labelled references without a
target_id stay valid: they point at words that have no entry.

Run with:  python3 -m unittest build.tests.test_schema_cross_refs
"""
import json
import unittest
from pathlib import Path

from jsonschema import Draft7Validator

_SCHEMA = json.loads((Path(__file__).resolve().parents[1] / "schema.json").read_text(encoding="utf-8"))
_ITEM = _SCHEMA["properties"]["cross_references"]["items"]


class CrossRefTargetOrLabel(unittest.TestCase):
    def valid(self, ref):
        return Draft7Validator(_ITEM).is_valid(ref)

    def test_bare_reference_rejected(self):
        self.assertFalse(self.valid({"type": "related", "reading": "ほしい", "headword": "ほしい"}))

    def test_target_id_accepted(self):
        self.assertTrue(self.valid({"type": "related", "target_id": "01107_hoshii", "reading": "ほしい"}))

    def test_label_without_target_accepted(self):
        self.assertTrue(self.valid({"type": "homophone", "reading": "こうふ", "label": "laborer (homophone)"}))


if __name__ == "__main__":
    unittest.main()
