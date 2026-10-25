"""Unit tests for build/claude_backend.py and the claude: model routing (no real calls).

Run with:  python3 -m unittest build.tests.test_claude_backend
"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

BUILD = Path(__file__).resolve().parents[2] / "build"
sys.path.insert(0, str(BUILD))
import claude_backend as cb  # noqa: E402
import review_runner as rr  # noqa: E402
import review_accuracy as ra  # noqa: E402


def stream(text="[]", five_hour=0.10, seven_day=0.20, status="allowed", is_error=False):
    lines = [
        {"type": "system", "subtype": "init"},
        {"type": "rate_limit_event", "rate_limit_info": {
            "status": status, "unifiedWindows": {"five_hour": {"utilization": five_hour},
                                                 "seven_day": {"utilization": seven_day}}}},
        {"type": "result", "is_error": is_error, "result": text, "total_cost_usd": 0.04,
         "usage": {"input_tokens": 2, "cache_creation_input_tokens": 4000,
                   "cache_read_input_tokens": 100, "output_tokens": 300},
         "modelUsage": {"claude-opus-5-5": {}}},
    ]
    return "\n".join(json.dumps(x) for x in lines) + "\n"


class FakeRunner:
    def __init__(self, stdout):
        self.stdout, self.calls = stdout, []

    def __call__(self, cmd, **kw):
        self.calls.append((cmd, kw))
        return subprocess.CompletedProcess(cmd, 0, stdout=self.stdout, stderr="")


class Base(unittest.TestCase):
    def setUp(self):
        self.saved = dict(cb._state)
        self.saved_which = cb.shutil.which
        self.saved_limits = cb.limits
        cb.shutil.which = lambda name: "/usr/bin/claude"
        cb.limits = lambda: dict(cb.DEFAULT_LIMITS)
        cb._state.update(stopped=None, five_hour=None, seven_day=None, calls=0, failed=0,
                         tokens_in=0, tokens_out=0, list_usd=0.0)

    def tearDown(self):
        cb._state.clear()
        cb._state.update(self.saved)
        cb.shutil.which = self.saved_which
        cb.limits = self.saved_limits


class TestCall(Base):
    def test_model_ids(self):
        self.assertTrue(cb.is_claude("claude:opus"))
        self.assertFalse(cb.is_claude("openai/gpt-6.1-sol"))
        self.assertFalse(cb.is_claude(None))
        self.assertEqual(cb.cli_model("claude:haiku"), "haiku")

    def test_reply_has_openrouter_shape(self):
        run = FakeRunner(stream('[{"dimension": "gloss"}]'))
        resp = cb.call("prompt", "claude:opus", runner=run)
        self.assertEqual(rr.parse_model_response(resp), [{"dimension": "gloss"}])
        self.assertEqual(resp["usage"]["prompt_tokens"], 4102)
        self.assertEqual(resp["usage"]["completion_tokens"], 300)
        cmd, kw = run.calls[0]
        self.assertEqual(cmd[cmd.index("--model") + 1], "opus")
        self.assertEqual(cmd[cmd.index("--tools") + 1], "")
        self.assertIn("--no-session-persistence", cmd)
        self.assertEqual(kw["input"], "prompt")
        self.assertIn("calls=1", cb.usage_line())
        self.assertIn("five-hour window 10%", cb.usage_line())

    def test_error_result_returns_none(self):
        run = FakeRunner(stream("boom", is_error=True))
        self.assertIsNone(cb.call("p", "claude:opus", runner=run, retries=0))
        self.assertIn("failed=1", cb.usage_line())


class TestGuard(Base):
    def test_full_window_stops_later_calls(self):
        run = FakeRunner(stream("[]", five_hour=0.75))
        self.assertIsNotNone(cb.call("p", "claude:opus", runner=run))  # this reply still counts
        self.assertIn("five-hour window at 75%", cb.stopped_reason())
        self.assertIsNone(cb.call("p", "claude:opus", runner=run))
        self.assertEqual(len(run.calls), 1)  # the second call never started a process
        self.assertFalse(cb.available()[0])
        self.assertIn("STOPPED", cb.usage_line())

    def test_seven_day_and_status(self):
        cb.note_rate_limit({"status": "allowed", "unifiedWindows": {"seven_day": {"utilization": 0.9}}})
        self.assertIn("seven-day", cb.stopped_reason())
        cb._state["stopped"] = None
        cb.note_rate_limit({"status": "rejected", "unifiedWindows": {}})
        self.assertIn("rejected", cb.stopped_reason())

    def test_below_limits_keeps_going(self):
        cb.note_rate_limit({"status": "allowed", "unifiedWindows": {
            "five_hour": {"utilization": 0.5}, "seven_day": {"utilization": 0.5}}})
        self.assertIsNone(cb.stopped_reason())

    def test_missing_cli(self):
        cb.shutil.which = lambda name: None
        ok, why = cb.available()
        self.assertFalse(ok)
        self.assertIn("not installed", why)

    def test_limits_read_from_config(self):
        cb.limits = self.saved_limits
        lim = cb.limits()
        self.assertTrue(0 < lim["five_hour_max"] <= 1 and 0 < lim["seven_day_max"] <= 1)


class TestRouting(Base):
    def test_call_openrouter_routes_claude_ids(self):
        seen = []
        orig = cb.call
        cb.call = lambda prompt, model, timeout=600: seen.append((prompt, model)) or {"choices": []}
        try:
            rr.call_openrouter(None, "claude:haiku", "hello")
        finally:
            cb.call = orig
        self.assertEqual(seen, [("hello", "claude:haiku")])

    def test_claude_costs_no_money(self):
        self.assertEqual(rr.estimate_cost("claude:opus", 5000, 500), 0.0)
        self.assertGreater(rr.estimate_cost("openai/gpt-4.1", 5000, 500), 0.0)


ENTRY = {"id": "05747_kirisuteru", "headword": "{切|き}り{捨|す}てる", "reading": "きりすてる",
         "metadata": {"tags": {"pos": ["verb-ichidan"], "semantic": ["action"]}},
         "gloss": "to cut down", "definitions": [], "examples": [],
         "notes": "USAGE:\nUsed only in writing."}
DIMS = ("gloss", "translation", "tags", "notes")


class TestAccuracySecondReviewer(Base):
    def test_claude_prompt_adds_error_classes(self):
        self.assertNotIn("What counts as WRONG", ra.build_prompt(ENTRY, DIMS, "openai/gpt-6.1-sol"))
        self.assertIn("What counts as WRONG", ra.build_prompt(ENTRY, DIMS, "claude:opus"))

    def test_claude_review_file_and_warn_kept(self):
        self.assertEqual(ra.review_path("05747_x", "claude:opus").name, "05747_x.claude.json")
        self.assertEqual(ra.review_path("05747_x", "openai/gpt-6.1-sol").name, "05747_x.json")
        warn = [{"dimension": "notes", "location": "notes", "severity": "warn",
                 "concern": "not only in writing", "quote": "Used only in writing."}]
        orig = ra.call_openrouter
        ra.call_openrouter = lambda *a, **k: {"choices": [{"message": {"content": json.dumps(warn)}}]}
        try:
            sol, _, _ = ra.review_entry(ENTRY, "k", "openai/gpt-6.1-sol", DIMS)
            opus, _, _ = ra.review_entry(ENTRY, None, "claude:opus", DIMS)
        finally:
            ra.call_openrouter = orig
        self.assertEqual(sol, [])
        self.assertEqual(len(opus), 1)

    def test_planned_out_lists_entries_sent(self):
        orig = (ra.review_entry, ra.save_review, ra.get_api_key, ra.estimate_cost)
        ra.review_entry = lambda *a, **k: ([], {}, "")
        ra.save_review = lambda *a, **k: None
        ra.get_api_key = lambda: "k"
        ra.estimate_cost = lambda *a, **k: 0.01
        try:
            entries = [(dict(ENTRY, id=f"{i:05d}_x"), None) for i in range(5)]
            planned = []
            ra.run_review(entries, "m", DIMS, 0.035, False, planned_out=planned)
        finally:
            ra.review_entry, ra.save_review, ra.get_api_key, ra.estimate_cost = orig
        self.assertEqual([e["id"] for e, _ in planned], ["00000_x", "00001_x", "00002_x"])

    def test_claude_review_skipped_when_unavailable(self):
        cb.shutil.which = lambda name: None
        self.assertEqual(ra.run_review([(ENTRY, None)], "claude:opus", DIMS, None, False), 0.0)


if __name__ == "__main__":
    unittest.main()
