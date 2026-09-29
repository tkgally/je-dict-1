"""Tests for the deep pass's wall-clock guards in review_runner.py (backlog item 141).

A slow model is dropped while another remains, and the pass stops at its time
limit and returns the entries it did not reach.
"""
import importlib.util
import unittest
from pathlib import Path
from unittest import mock

_MOD = Path(__file__).resolve().parent.parent / "review_runner.py"
_spec = importlib.util.spec_from_file_location("review_runner", _MOD)
rr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rr)

ENTRY = {"headword": "{猫|ねこ}", "reading": "ねこ", "examples": []}
FAST, SLOW = "fast/model", "slow/model"


class FakeClock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t


class TestDeepPassGuards(unittest.TestCase):
    def setUp(self):
        self.clock = FakeClock()
        self.calls = []
        cost = {FAST: 5.0, SLOW: 200.0}

        def fake_call(api_key, model, prompt, **kw):
            self.calls.append(model)
            self.clock.t += cost[model]
            return {"choices": [{"message": {"content": "[]"}}]}

        patches = [
            mock.patch.object(rr, "call_openrouter", side_effect=fake_call),
            mock.patch.object(rr, "find_entry_file", return_value=Path("x.json")),
            mock.patch.object(rr, "load_entry", return_value=ENTRY),
            mock.patch.object(rr, "save_report"),
            mock.patch.object(rr.time, "sleep"),
            mock.patch("builtins.print"),
        ]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)

    def run_pass(self, ids, models, max_minutes=None):
        return rr.run_deep_pass(ids, "key", models, max_minutes=max_minutes,
                                slow_seconds=90, clock=self.clock)

    def test_slow_model_dropped_after_first_entry(self):
        self.run_pass(["00001", "00002", "00003"], [FAST, SLOW])
        self.assertEqual(self.calls, [FAST, SLOW, FAST, FAST])

    def test_last_model_never_dropped(self):
        self.run_pass(["00001", "00002"], [SLOW])
        self.assertEqual(self.calls, [SLOW, SLOW])

    def test_time_limit_returns_unreached(self):
        # each entry costs 200s with the slow model alone: 5 min limit → 2 entries
        left = self.run_pass(["00001", "00002", "00003", "00004"], [SLOW], max_minutes=5)
        self.assertEqual(self.calls, [SLOW, SLOW])
        self.assertEqual(left, ["00003", "00004"])

    def test_no_limit_reviews_all(self):
        left = self.run_pass(["00001", "00002"], [FAST], max_minutes=None)
        self.assertEqual(left, [])
        self.assertEqual(len(self.calls), 2)


if __name__ == "__main__":
    unittest.main()
