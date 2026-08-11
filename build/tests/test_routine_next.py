"""Unit tests for the unified Routine mode selector (pipeline/routine_next.py).

Exercises the pure scheduler logic in isolation — no disk writes — by
constructing config/state/signals dicts and calling the module functions
directly. Matches the repo convention (unittest, plain asserts).

Run with:  python3 -m unittest build.tests.test_routine_next
"""
import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path

# Load pipeline/routine_next.py by path (hyphenated dir, not importable normally).
_MOD_PATH = Path(__file__).resolve().parents[2] / "pipeline" / "routine_next.py"
_spec = importlib.util.spec_from_file_location("routine_next", _MOD_PATH)
rn = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rn)


def base_config(enabled=None):
    cfg = deepcopy(rn.DEFAULT_CONFIG)
    if enabled is not None:
        cfg["enabled_modes"] = enabled
    return cfg


def fresh_state():
    return {
        "debt": {m: 0.0 for m in rn.ALL_MODES},
        "history": [],
        "last_run_mode": None,
        "day_tally": {"date": None},
    }


def neutral_signals():
    # candidate_count above the low threshold (80) but below the restock
    # threshold (150) -> no nudges triggered and the candidates mode is
    # active; open_backlog_items > 0 so systemic-fix is active.
    return {
        "candidate_count": 120,
        "seen_in_entry_count": 0,
        "max_entry_id": 29000,
        "comprehensive_next": 5936,
        "cross_model_review_next": 1,
        "unharvested_observations": 0,
        "reviewed_entries": 10,
        "open_backlog_items": 5,
    }


def simulate(config, signals, remaining, n, state=None):
    state = state or fresh_state()
    mult, _ = rn.compute_multipliers(signals, config, remaining)
    tally = {}
    for _ in range(n):
        choice, debt, *_ = rn.select_mode(config, state, mult)
        state["debt"] = debt
        state["last_run_mode"] = choice
        tally[choice] = tally.get(choice, 0) + 1
    return tally, state


class TestScheduler(unittest.TestCase):
    def test_pure_scheduler_converges_to_weights(self):
        # With anti-repeat disabled, the debt scheduler is exact largest-remainder:
        # realized proportions match the normalized weights very tightly.
        cfg = base_config()
        cfg["anti_repeat_modes"] = []
        n = 5000
        tally, _ = simulate(cfg, neutral_signals(), remaining=5.0, n=n)
        norm, enabled = rn.normalized_weights(cfg)
        for m in enabled:
            realized = tally.get(m, 0) / n
            self.assertLess(
                abs(realized - norm[m]), 0.012,
                f"{m}: realized {realized:.3f} vs target {norm[m]:.3f}",
            )

    def test_realconfig_proportions_stay_near_weights(self):
        # The default config's anti-repeat rule perturbs proportions slightly but
        # must never starve a mode: every enabled mode stays within ~4 points of
        # its target weight.
        cfg = base_config()
        n = 5000
        tally, _ = simulate(cfg, neutral_signals(), remaining=5.0, n=n)
        norm, enabled = rn.normalized_weights(cfg)
        for m in enabled:
            realized = tally.get(m, 0) / n
            self.assertLess(
                abs(realized - norm[m]), 0.04,
                f"{m}: realized {realized:.3f} vs target {norm[m]:.3f}",
            )
            self.assertGreater(tally.get(m, 0), 0)

    def test_removed_mode_never_selected(self):
        cfg = base_config(enabled=["polish", "accuracy-review", "new-entries", "wiki"])
        tally, _ = simulate(cfg, neutral_signals(), remaining=5.0, n=2000)
        self.assertNotIn("systemic-fix", tally)

    def test_systemic_fix_suppressed_when_no_backlog(self):
        cfg = base_config()  # systemic-fix enabled
        sig = neutral_signals()
        sig["open_backlog_items"] = 0
        tally, _ = simulate(cfg, sig, remaining=5.0, n=2000)
        self.assertNotIn("systemic-fix", tally)
        for m in ("polish", "new-entries", "wiki"):
            self.assertGreater(tally.get(m, 0), 0)

    def test_systemic_fix_runs_when_backlog_present(self):
        cfg = base_config()
        sig = neutral_signals()
        sig["open_backlog_items"] = 3
        tally, _ = simulate(cfg, sig, remaining=5.0, n=2000)
        self.assertGreater(tally.get("systemic-fix", 0), 0)

    def test_select_backlog_item_picks_highest_priority_open_ready(self):
        queue = {"items": [
            {"id": "low", "priority": 9, "status": "open", "batch_ready": True},
            {"id": "experimental", "priority": 1, "status": "detector-experimental", "batch_ready": False},
            {"id": "top", "priority": 2, "status": "open", "batch_ready": True},
            {"id": "done", "priority": 1, "status": "resolved", "batch_ready": True},
        ]}
        self.assertEqual(rn.select_backlog_item(queue)["id"], "top")
        # Nothing open+ready -> None
        self.assertIsNone(rn.select_backlog_item({"items": [
            {"id": "x", "priority": 1, "status": "detector-experimental", "batch_ready": False},
        ]}))

    def test_budget_suppression_blocks_accuracy_review(self):
        cfg = base_config()
        tally, _ = simulate(cfg, neutral_signals(), remaining=0.0, n=2000)
        self.assertNotIn("accuracy-review", tally)
        for m in ("polish", "new-entries", "wiki"):
            self.assertGreater(tally.get(m, 0), 0)

    def test_anti_repeat_no_back_to_back_heavy_mode(self):
        cfg = base_config(enabled=["new-entries", "wiki"])
        cfg["weights"] = {**cfg["weights"], "new-entries": 0.5, "wiki": 0.5}
        state = fresh_state()
        mult, _ = rn.compute_multipliers(neutral_signals(), cfg, remaining=5.0)
        picks = []
        for _ in range(200):
            choice, debt, *_ = rn.select_mode(cfg, state, mult)
            state["debt"] = debt
            state["last_run_mode"] = choice
            picks.append(choice)
        self.assertFalse(
            any(picks[i] == "new-entries" and picks[i + 1] == "new-entries"
                for i in range(len(picks) - 1)),
            "new-entries was selected twice in a row",
        )
        self.assertIn("new-entries", picks)


class TestNudges(unittest.TestCase):
    def test_multiplier_clamped_to_max(self):
        cfg = base_config()
        cfg["nudges"]["max_multiplier"] = 1.2
        sig = neutral_signals()
        sig["seen_in_entry_count"] = 999
        sig["candidate_count"] = 99999
        mult, _ = rn.compute_multipliers(sig, cfg, remaining=5.0)
        self.assertEqual(mult["new-entries"], 1.2)

    def test_candidates_low_downnudges_new_entries(self):
        cfg = base_config()
        sig = neutral_signals()
        sig["candidate_count"] = 10  # below low threshold (80)
        mult, reasons = rn.compute_multipliers(sig, cfg, remaining=5.0)
        self.assertLess(mult["new-entries"], 1.0)
        self.assertTrue(any("candidates low" in r for r in reasons["new-entries"]))

    def test_candidates_mode_suppressed_when_queue_stocked(self):
        cfg = base_config()
        sig = neutral_signals()
        sig["candidate_count"] = 500  # above restock threshold (150)
        tally, _ = simulate(cfg, sig, remaining=5.0, n=2000)
        self.assertNotIn("candidates", tally)
        for m in ("polish", "new-entries", "wiki"):
            self.assertGreater(tally.get(m, 0), 0)

    def test_candidates_mode_runs_when_queue_below_restock(self):
        cfg = base_config()
        sig = neutral_signals()
        sig["candidate_count"] = 100  # below restock threshold, above low
        tally, _ = simulate(cfg, sig, remaining=5.0, n=2000)
        self.assertGreater(tally.get("candidates", 0), 0)

    def test_candidates_mode_boosted_when_queue_nearly_empty(self):
        cfg = base_config()
        sig = neutral_signals()
        sig["candidate_count"] = 20  # below low threshold (80)
        mult, reasons = rn.compute_multipliers(sig, cfg, remaining=5.0)
        self.assertEqual(mult["candidates"], 1.5)
        self.assertTrue(any("restock" in r for r in reasons["candidates"]))


class TestForceAndParams(unittest.TestCase):
    def test_force_mode_does_not_mutate_debt(self):
        cfg = base_config()
        state = fresh_state()
        state["debt"] = {m: 1.234 for m in rn.ALL_MODES}
        mult, _ = rn.compute_multipliers(neutral_signals(), cfg, remaining=5.0)
        choice, debt, *_ = rn.select_mode(cfg, state, mult, forced="wiki")
        self.assertEqual(choice, "wiki")
        self.assertEqual(debt, state["debt"])  # unchanged

    def test_params_carry_session_budget_capped(self):
        cfg = base_config()
        cfg["openrouter"]["per_session_cap_usd"] = 1.5
        p = rn.build_params("accuracy-review", neutral_signals(), cfg, remaining=0.40)
        self.assertEqual(p["openrouter_session_budget_usd"], 0.40)
        p = rn.build_params("accuracy-review", neutral_signals(), cfg, remaining=4.0)
        self.assertEqual(p["openrouter_session_budget_usd"], 1.5)

    def test_params_candidates_scale_to_queue_deficit(self):
        cfg = base_config()
        sig = neutral_signals()
        sig["candidate_count"] = 20
        p = rn.build_params("candidates", sig, cfg, remaining=5.0)
        self.assertEqual(p["queue_count"], 20)
        # deficit 150+20-20 = 150, capped at 60
        self.assertEqual(p["approx_new"], 60)
        sig["candidate_count"] = 140
        p = rn.build_params("candidates", sig, cfg, remaining=5.0)
        # deficit 30, floored at 40
        self.assertEqual(p["approx_new"], 40)


if __name__ == "__main__":
    unittest.main()
