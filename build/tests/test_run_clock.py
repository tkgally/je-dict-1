"""Unit tests for pipeline/run_clock.py (the multi-cycle Routine run clock).

Run with:  python3 -m unittest build.tests.test_run_clock
"""
import importlib.util
import io
import tempfile
import time
import unittest
from contextlib import redirect_stdout
from pathlib import Path

_MOD_PATH = Path(__file__).resolve().parents[2] / "pipeline" / "run_clock.py"
_spec = importlib.util.spec_from_file_location("run_clock", _MOD_PATH)
rc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rc)


def run(*argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc.main(list(argv))
    return buf.getvalue()


class RunClockTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.file = Path(self.tmp.name) / "start"

    def tearDown(self):
        self.tmp.cleanup()

    def test_start_then_check_allows_a_cycle(self):
        out = run("start", "--file", str(self.file))
        self.assertIn("run clock started", out)
        self.assertIn("next cycle: yes", out)
        self.assertNotIn("wrap up now", out)

    def test_repeat_start_keeps_first_time(self):
        self.file.write_text(f"{time.time() - 30 * 60:.0f}\n")
        out = run("start", "--file", str(self.file))
        self.assertIn("kept", out)
        self.assertIn("elapsed: 30 min", out)

    def test_past_new_cycle_limit(self):
        self.file.write_text(f"{time.time() - 110 * 60:.0f}\n")
        out = run("--file", str(self.file))
        self.assertIn("next cycle: no", out)
        self.assertNotIn("wrap up now", out)

    def test_past_wrap_up_limit(self):
        self.file.write_text(f"{time.time() - 131 * 60:.0f}\n")
        out = run("--file", str(self.file))
        self.assertIn("next cycle: no", out)
        self.assertIn("wrap up now", out)

    def test_stale_start_file_is_replaced(self):
        self.file.write_text(f"{time.time() - 300 * 60:.0f}\n")
        out = run("start", "--file", str(self.file))
        self.assertIn("run clock started", out)
        self.assertIn("elapsed: 0 min", out)

    def test_check_without_start_starts_now(self):
        out = run("--file", str(self.file))
        self.assertIn("clock starts now", out)
        self.assertTrue(self.file.exists())


if __name__ == "__main__":
    unittest.main()
