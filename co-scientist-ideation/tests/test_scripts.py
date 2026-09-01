#!/usr/bin/env python3
"""Focused deterministic checks for the six-block Skill package."""

from __future__ import annotations

import importlib.util
import io
import json
import unittest
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_validator():
    path = ROOT / "scripts" / "validate_skill.py"
    spec = importlib.util.spec_from_file_location("co_scientist_validate_skill", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALIDATE_SKILL = load_validator()


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


SKILL = read("SKILL.md")
WORKFLOW = read("references/workflow.md")
ROLES = read("references/roles.md")
CONTRACTS = read("references/contracts.md")
SAFETY = read("references/safety.md")
LOCALIZATION = read("references/localization.md")
BEHAVIOR_CASES = json.loads(read("tests/behavior_contract_cases.json"))


class ScriptTests(unittest.TestCase):
    def test_activation_cases(self) -> None:
        cases = json.loads(read("tests/trigger_cases.json"))
        for case in cases:
            self.assertEqual(
                VALIDATE_SKILL.activation_gate(case["prompt"]),
                case["activate"],
                case["id"],
            )

    def test_packaging_validator(self) -> None:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = VALIDATE_SKILL.main()
        payload = json.loads(stdout.getvalue())
        self.assertEqual(exit_code, 0, payload)
        self.assertTrue(payload["valid"], payload)
        self.assertEqual(payload["scope"], "structural_only")
        self.assertEqual(payload["checked_files"], 13)

    def test_quantitative_evidence_gate_contract(self) -> None:
        skill_flat = " ".join(SKILL.split())
        workflow_flat = " ".join(WORKFLOW.split())
        roles_flat = " ".join(ROLES.split())
        contracts_flat = " ".join(CONTRACTS.split())
        safety_flat = " ".join(SAFETY.split())
        for token in (
            "Quantitative and citation admission gate",
            "exact number, percentage, range, date, rank, count",
            "Wrong-source attribution",
            "fact-closed over admitted evidence",
            "prohibit finalist use",
        ):
            self.assertIn(token.casefold(), contracts_flat.casefold())
        self.assertIn("must not add a new factual, quantitative", skill_flat)
        self.assertIn("Before synthesis, close the fact set", workflow_flat)
        self.assertIn("wrong-source or unsupported decisive", roles_flat.casefold())
        self.assertIn("project memory, prior chat, and agent agreement", safety_flat)

    def test_behavior_contract_cases(self) -> None:
        self.assertEqual(
            [case["id"] for case in BEHAVIOR_CASES],
            [
                "unsupported_exact_percentage",
                "wrong_source_attribution",
                "supervisor_fact_closure",
                "design_threshold_provenance",
                "stage_value_skip_with_mandatory_review",
                "record_authority_and_blinding",
                "capacity_attempt_exhaustion",
                "executive_decision_projection_optional",
                "run_scoped_web_retrieval",
                "domain_neutral_component_isolation",
            ],
        )
        for case in BEHAVIOR_CASES:
            self.assertIn("$co-scientist-ideation", case["prompt"])
            self.assertGreaterEqual(len(case["expected"]), 2)
        for case in BEHAVIOR_CASES[4:]:
            self.assertGreaterEqual(len(case["required_invariants"]), 3)

    def test_run_scoped_retrieval_and_domain_neutrality(self) -> None:
        skill_flat = " ".join(SKILL.split())
        workflow_flat = " ".join(WORKFLOW.split())
        roles_flat = " ".join(ROLES.split())
        self.assertIn("authorized and decision-relevant", skill_flat)
        self.assertIn("run-scoped offline/web policy", workflow_flat)
        self.assertIn("When Web retrieval is authorized", WORKFLOW)
        self.assertIn("source identity, location, scope, relation, and limitation", workflow_flat)
        self.assertIn("unpublished or private query content abstract", workflow_flat)
        for token in (
            "multi-component claim",
            "genuinely separable components",
            "decision-relevant quality and resource conditions",
            "component-isolation discriminator",
            "component-local falsifier",
            "isolated component success does not prove the joint claim",
        ):
            self.assertIn(token.casefold(), (workflow_flat + " " + roles_flat).casefold())
        self.assertEqual(
            [case["id"] for case in BEHAVIOR_CASES[-2:]],
            ["run_scoped_web_retrieval", "domain_neutral_component_isolation"],
        )

    def test_block_1_goal_evidence_map(self) -> None:
        self.assertIn("## Block 1 — Goal + Evidence Map", WORKFLOW)
        for token in (
            "Progressive retrieval",
            "supporting, contradictory, limiting, negative, null, and unresolved evidence",
            "Each claim has one canonical evidence binding",
            "corpus absence is not evidence of novelty",
            "there is no usable anchor",
        ):
            self.assertIn(token.casefold(), WORKFLOW.casefold())
        self.assertIn("Goal–Evidence Map", CONTRACTS)
        self.assertIn("source identity | specific claim | location/anchor", CONTRACTS)

    def test_block_2_generation(self) -> None:
        workflow_flat = " ".join(WORKFLOW.split())
        roles_flat = " ".join(ROLES.split())
        contracts_flat = " ".join(CONTRACTS.split())
        self.assertIn("normally 2–4 total candidates", WORKFLOW)
        self.assertIn("never backfill quota", workflow_flat.casefold())
        self.assertIn("Admit cards independently", WORKFLOW)
        self.assertIn("name-removal, functional-replacement, and single-spine", WORKFLOW)
        self.assertIn("Formal and dimensional validity is Reviewer-owned", WORKFLOW)
        self.assertIn("Propose any base/candidate/off condition as an\nunverified claim", ROLES)
        self.assertIn("Before an optional call", WORKFLOW)
        self.assertIn("root and fresh reviews remain mandatory", workflow_flat.casefold())
        self.assertIn("peer drafts", roles_flat)
        for token in (
            "object/state",
            "invariant",
            "update or propagation rule",
            "complexity, memory, or precision",
            "proof obligation or minimum counterexample",
            "nearest implementation",
            "source-backed",
            "pilot-calibrated",
            "human-utility choice",
            "placeholder",
        ):
            self.assertIn(token.casefold(), contracts_flat.casefold())
        self.assertIn("ordinary biological, cognitive, observational, or empirical claims", contracts_flat)
        self.assertIn("only when the live candidate has genuinely separable components", workflow_flat)
        self.assertIn("decision-relevant quality and resource conditions matched", workflow_flat)
        self.assertIn("component-isolation discriminator", workflow_flat)
        self.assertIn("component-local falsifier", workflow_flat)
        self.assertIn("isolated component success does not prove the joint claim", workflow_flat)
        self.assertIn("cannot promote a finalist", contracts_flat)

    def test_block_3_reflection(self) -> None:
        workflow_flat = " ".join(WORKFLOW.split())
        roles_flat = " ".join(ROLES.split())
        self.assertIn("one independent Review Record", WORKFLOW)
        self.assertIn("admit each Review Record\nindependently", WORKFLOW)
        self.assertIn("continue / revise / reject / insufficient evidence", WORKFLOW)
        self.assertIn("one killer objection", WORKFLOW)
        self.assertIn("formal and\ndimensional validity is owned here", ROLES)
        self.assertIn("If zero authoritative Reviews exist", WORKFLOW)
        self.assertIn("Supervisor synthesis cannot substitute", WORKFLOW)
        self.assertIn("root and fresh reviews remain mandatory", workflow_flat.casefold())
        self.assertIn("verify the proposed state, invariant, update or propagation rule", roles_flat)
        self.assertIn("isolated component success", roles_flat)

    def test_block_4_conditional_comparison(self) -> None:
        self.assertIn("Run Block 4 only when", WORKFLOW)
        for token in ("tie", "reject_both", "insufficient_evidence", "order_unstable"):
            self.assertIn(token, WORKFLOW)
        self.assertIn("No total order is required", WORKFLOW)
        self.assertIn("unranked repair-target alternatives", WORKFLOW)
        self.assertIn("send every eligible candidate", WORKFLOW)
        self.assertFalse((ROOT / "scripts" / "score_tournament.py").exists())

    def test_block_5_evolution(self) -> None:
        self.assertIn("exact killer objection", WORKFLOW)
        self.assertIn("material scientific change", WORKFLOW)
        self.assertIn("Fresh independent review", WORKFLOW)
        self.assertIn("No-repair", WORKFLOW)
        self.assertIn("Descendant-review failure", WORKFLOW)
        self.assertIn("diverged descendant", WORKFLOW)
        self.assertIn("must not perform the descendant's fresh Review", ROLES)

    def test_block_6_human_selection(self) -> None:
        workflow_flat = " ".join(WORKFLOW.split())
        skill_flat = " ".join(SKILL.split())
        self.assertIn("current admitted independent `continue` Review", WORKFLOW)
        self.assertIn("must not assign primary/reserve\norder or truncate", WORKFLOW)
        self.assertIn("Present every eligible candidate", WORKFLOW)
        self.assertIn("Block 6 ends the current run", WORKFLOW)
        self.assertIn("canonical evidence binding once", workflow_flat)
        self.assertIn("Remove literature retelling and workflow narration", workflow_flat)
        self.assertIn("no-finalist", SKILL)
        self.assertIn("next human decision", skill_flat)
        self.assertIn("Execution is not authorized by this Skill output.", SKILL)
        self.assertIn("code, training, data collection, experiments", SKILL.casefold())

    def test_record_access_and_blinding(self) -> None:
        contracts_flat = " ".join(CONTRACTS.split())
        roles_flat = " ".join(ROLES.split())
        for token in (
            "SOURCE_EVIDENCE",
            "PRACTICE_OBSERVATION",
            "PRIOR_CANDIDATE",
            "REVIEW_DISPOSITION",
            "HUMAN_DECISION",
            "UNVERIFIED_NOTE",
            "use the narrowest authority",
        ):
            self.assertIn(token.casefold(), contracts_flat.casefold())
        self.assertIn("prior formulas, rank, preference, and dispositions", contracts_flat)
        self.assertIn("candidate's prior disposition", roles_flat)
        self.assertIn("author/generation lens", roles_flat)

    def test_capacity_failure_lineage(self) -> None:
        workflow_flat = " ".join(WORKFLOW.split())
        roles_flat = " ".join(ROLES.split())
        for token in (
            "finite role attempts",
            "consumes one",
            "retry must be preallocated",
            "never backfill quota",
            "same authority lineage",
        ):
            self.assertIn(token.casefold(), workflow_flat.casefold())
        self.assertIn("do not backfill candidate quota", roles_flat.casefold())
        self.assertIn("auto-retry/switch provider", roles_flat)

    def test_optional_executive_decision(self) -> None:
        contracts_flat = " ".join(CONTRACTS.split())
        self.assertIn("Executive Decision", CONTRACTS)
        self.assertIn("optional", contracts_flat)
        self.assertIn("contains only", contracts_flat)
        self.assertIn("No other field enters", CONTRACTS)
        self.assertIn("fact-closed projection", contracts_flat)
        self.assertIn("full package remains authoritative", contracts_flat)
        self.assertIn("creates no evidence, verdict, rank", contracts_flat)

    def test_no_platform_runtime_files(self) -> None:
        for relative in (
            "references/schema-1.6-design.md",
            "scripts/init_run.py",
            "scripts/score_tournament.py",
            "scripts/validate_run.py",
        ):
            self.assertFalse((ROOT / relative).exists(), relative)
        self.assertEqual(VALIDATE_SKILL.package_files(), set(VALIDATE_SKILL.REQUIRED))

    def test_protected_scientific_content(self) -> None:
        self.assertIn("Use only when", SKILL)
        self.assertIn("Do not trigger", SKILL)
        self.assertIn("Candidate-local versus whole-run scope", SAFETY)
        self.assertIn("Preserve contradictory, limiting, negative, null", SAFETY)
        self.assertIn("source location and limitation", SAFETY)
        self.assertIn("Anti-stitching", WORKFLOW)
        self.assertIn("Reviewer-owned", WORKFLOW)
        self.assertIn("one killer objection", WORKFLOW)
        self.assertIn("material scientific change", WORKFLOW)
        self.assertIn("Every created descendant receives a complete non-author Block 3 review", WORKFLOW)
        self.assertIn("complete fresh independent `continue` Review", WORKFLOW)
        self.assertIn("human decision", WORKFLOW.casefold())
        self.assertIn("Block 6 ends with a human decision", SAFETY)
        self.assertIn("at most 3 concurrent subagents", SKILL.casefold())
        self.assertIn("Moving from the Decision\nPackage", LOCALIZATION)


if __name__ == "__main__":
    unittest.main()
