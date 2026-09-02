from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest


METHOD_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


review_validator = load_module(
    "public_review_validator", METHOD_ROOT / "validate_review_record.py"
)
cost_summary = load_module(
    "public_cost_summary", METHOD_ROOT / "quality_cost_summary.py"
)


class PublicEvaluationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture_path = METHOD_ROOT / "examples" / "review_record.json"
        self.record = json.loads(self.fixture_path.read_text(encoding="utf-8"))

    def test_synthetic_fixture_is_eligible(self) -> None:
        admitted = review_validator.validate_review_record(self.record)
        self.assertEqual(admitted["review_status"], "ELIGIBLE")
        self.assertEqual(admitted["primary_choice"], "A")

    def test_extra_field_is_rejected(self) -> None:
        invalid = copy.deepcopy(self.record)
        invalid["unexpected"] = True
        with self.assertRaises(review_validator.ReviewValidationError):
            review_validator.validate_review_record(invalid)

    def test_placeholder_is_rejected(self) -> None:
        invalid = copy.deepcopy(self.record)
        invalid["concise_choice_reasons"] = ["TODO"]
        with self.assertRaises(review_validator.ReviewValidationError):
            review_validator.validate_review_record(invalid)

    def test_cost_summary_is_explicit_and_non_causal(self) -> None:
        summary = cost_summary.summarize_quality_cost(
            s_task_equalized=0.75,
            co_generation_requests=20,
            generic_generation_requests=10,
            co_mean_wall_time=2.0,
            generic_mean_wall_time=1.0,
            co_mean_output_length=100,
            generic_mean_output_length=100,
            co_nested_requests=5,
            generic_nested_requests=2,
        )
        self.assertEqual(summary["generation_request_ratio"], 2.0)
        self.assertEqual(summary["mean_wall_time_ratio"], 2.0)
        self.assertEqual(summary["extra_nested_requests"], 3)
        self.assertAlmostEqual(
            summary["exploratory_quality_gain_per_10_extra_generation_requests"],
            0.25,
        )
        self.assertEqual(summary["pareto_label"], "trade-off")
        self.assertIn("no ROI inference", summary["interpretation_boundary"])

    def test_missing_cost_input_is_not_imputed(self) -> None:
        summary = cost_summary.summarize_quality_cost(
            s_task_equalized=None,
            co_generation_requests=None,
            generic_generation_requests=None,
            co_mean_wall_time=None,
            generic_mean_wall_time=None,
            co_mean_output_length=None,
            generic_mean_output_length=None,
            co_nested_requests=None,
            generic_nested_requests=None,
        )
        self.assertEqual(summary["pareto_label"], "NA")
        self.assertGreater(len(summary["missing_fields"]), 0)

    def test_protocol_mentions_declared_generic_envelope(self) -> None:
        protocol = (METHOD_ROOT / "protocol.yaml").read_text(encoding="utf-8")
        for skill_name in (
            "research-ideation",
            "hypothesis-generation",
            "scientific-brainstorming",
            "literature-review",
        ):
            self.assertIn(skill_name, protocol)
        self.assertIn("per_request_skill_invocation_recorded: false", protocol)


if __name__ == "__main__":
    unittest.main()
