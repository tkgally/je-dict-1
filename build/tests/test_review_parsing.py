"""Tests for review_runner.py response parsing hardening (2026-06-10).

Covers the failure modes observed in production Routine runs:
- null message content (gemini, 2026-06-09 crash)
- text delivered in 'reasoning' with empty content (gemini-2.5-pro, 2026-06-10)
- arrays wrapped in an object despite instructions
"""
import importlib.util
import unittest
from pathlib import Path

_MOD = Path(__file__).resolve().parent.parent / "review_runner.py"
_spec = importlib.util.spec_from_file_location("review_runner", _MOD)
rr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rr)


def resp(content=None, reasoning=None):
    msg = {"content": content}
    if reasoning is not None:
        msg["reasoning"] = reasoning
    return {"choices": [{"message": msg}]}


class TestExtractMessageText(unittest.TestCase):
    def test_none_response(self):
        self.assertIsNone(rr.extract_message_text(None))

    def test_missing_choices(self):
        self.assertIsNone(rr.extract_message_text({}))

    def test_null_content_no_crash(self):
        self.assertIsNone(rr.extract_message_text(resp(content=None)))

    def test_empty_content_falls_back_to_reasoning(self):
        out = rr.extract_message_text(resp(content="", reasoning='[{"index": 1}]'))
        self.assertEqual(out, '[{"index": 1}]')

    def test_content_preferred_over_reasoning(self):
        out = rr.extract_message_text(resp(content="[]", reasoning="ignored"))
        self.assertEqual(out, "[]")


class TestParseModelResponse(unittest.TestCase):
    def test_bare_array(self):
        out = rr.parse_model_response(resp(content='[{"index": 1, "correct": true}]'))
        self.assertEqual(out, [{"index": 1, "correct": True}])

    def test_fenced_array(self):
        out = rr.parse_model_response(resp(content='```json\n[{"index": 2}]\n```'))
        self.assertEqual(out, [{"index": 2}])

    def test_object_wrapped_results(self):
        out = rr.parse_model_response(resp(content='{"results": [{"index": 3}]}'))
        self.assertEqual(out, [{"index": 3}])

    def test_null_content_returns_none(self):
        self.assertIsNone(rr.parse_model_response(resp(content=None)))

    def test_array_in_reasoning_field(self):
        out = rr.parse_model_response(resp(content="", reasoning='[{"index": 4}]'))
        self.assertEqual(out, [{"index": 4}])


class TestParseScreeningResponse(unittest.TestCase):
    def test_normal_object(self):
        out = rr.parse_screening_response(
            resp(content='{"flagged": false, "concerns": [], "confidence": 1.0}'))
        self.assertEqual(out["flagged"], False)

    def test_null_content_returns_none(self):
        self.assertIsNone(rr.parse_screening_response(resp(content=None)))

    def test_object_in_reasoning_field(self):
        out = rr.parse_screening_response(
            resp(content=None, reasoning='{"flagged": true, "concerns": ["x"], "confidence": 0.8}'))
        self.assertEqual(out["flagged"], True)


if __name__ == "__main__":
    unittest.main()
