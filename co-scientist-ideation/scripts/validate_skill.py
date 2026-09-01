#!/usr/bin/env python3
"""Validate only the local Skill package and activation boundary."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "RELEASE_MANIFEST.yaml",
    "agents/openai.yaml",
    "references/workflow.md",
    "references/roles.md",
    "references/contracts.md",
    "references/safety.md",
    "references/localization.md",
    "references/paper-basis.md",
    "scripts/validate_skill.py",
    "tests/test_scripts.py",
    "tests/behavior_contract_cases.json",
    "tests/trigger_cases.json",
]
RETIRED = [
    "references/schema-1.6-design.md",
    "scripts/init_run.py",
    "scripts/score_tournament.py",
    "scripts/validate_run.py",
]
BLOCK_HEADINGS = [
    "## Block 1 — Goal + Evidence Map",
    "## Block 2 — Multi-strategy Generation",
    "## Block 3 — Reflection + Deep Verification",
    "## Block 4 — Proximity + Ranking (conditional)",
    "## Block 5 — Evolution + Fresh Reflection",
    "## Block 6 — Meta-review + Human Selection",
]


def activation_gate(text: str) -> bool:
    normalized = text.casefold()
    no_go_markers = (
        "不要", "别", "勿", "禁止", "不启用", "不使用", "do not", "don't", "not use",
        "only discuss", "只讨论", "只写代码", "只解释", "仅解释",
    )

    def phrase_negated(phrase: str) -> bool:
        start = 0
        while True:
            position = normalized.find(phrase.casefold(), start)
            if position < 0:
                return False
            window = normalized[max(0, position - 32) : position + len(phrase) + 48]
            if any(marker in window for marker in no_go_markers):
                return True
            start = position + len(phrase)

    def phrase_quoted(phrase: str) -> bool:
        quote_chars = '"\'“”‘’「」『』'
        phrase_lower = phrase.casefold()
        start = 0
        while True:
            position = normalized.find(phrase_lower, start)
            if position < 0:
                return False
            left = normalized[:position].rstrip()
            right = normalized[position + len(phrase):].lstrip()
            if left and right and left[-1] in quote_chars and right[0] in quote_chars:
                return True
            start = position + len(phrase)

    if "$co-scientist-ideation" in normalized and phrase_negated("$co-scientist-ideation"):
        return False
    if "$co-scientist-ideation" in normalized:
        without_token = normalized.replace("$co-scientist-ideation", " ")
        return any(
            token in without_token
            for token in ("假设", "研究方向", "研究问题", "想点子", "hypothesis", "research idea")
        )
    for shortcut in ("多智能体科研构思", "科研搭档想点子"):
        if shortcut in text:
            if phrase_negated(shortcut):
                return False
            context = normalized.replace(shortcut.casefold(), " ")
            goal = any(
                token in context
                for token in (
                    "假设", "研究方向", "研究问题", "课题", "机制", "围绕", "针对", "关于",
                    "hypothesis", "research idea",
                )
            )
            action = any(
                token in context
                for token in (
                    "开启", "启用", "运行", "进入", "作为", "筛选", "辩论", "比较", "提出", "生成",
                    "演化", "propose", "screen", "run",
                )
            )
            if phrase_quoted(shortcut) and not action:
                return False
            return goal and action
    ideation = any(
        token in normalized
        for token in ("hypothes", "research idea", "假设", "研究方向", "想点子", "科研构思")
    )
    if "co-scientist" in normalized:
        activation = any(
            token in normalized
            for token in ("run", "use", "imitate", "mode", "启用", "开启", "进入", "像")
        )
        return activation and ideation
    multi_role = any(
        token in normalized
        for token in ("multiple scientific", "multiple research", "多个科研", "多角色科研")
    )
    screening = any(
        token in normalized
        for token in ("screen", "rank", "debate", "compare", "筛选", "排序", "辩论", "比较")
    )
    return multi_role and ideation and screening


def package_files() -> set[str]:
    files: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file() or "__pycache__" in path.parts or ".pytest_cache" in path.parts:
            continue
        files.add(path.relative_to(ROOT).as_posix())
    return files


def validate_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        target_path = (path.parent / target).resolve()
        if not target_path.exists():
            errors.append(f"broken Markdown link in {path.relative_to(ROOT)}: {target}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    required = set(REQUIRED)
    actual = package_files()

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")
    for relative in RETIRED:
        if (ROOT / relative).exists():
            errors.append(f"retired platform file remains: {relative}")
    extras = sorted(actual - required)
    if extras:
        errors.append(f"unexpected package files: {extras}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", skill, re.DOTALL)
        if not match:
            errors.append("SKILL.md frontmatter is invalid")
        else:
            frontmatter = match.group(1)
            if "name: co-scientist-ideation" not in frontmatter:
                errors.append("frontmatter name is not co-scientist-ideation")
            for token in (
                "Use only when",
                "Do not trigger",
                "Merely mentioning Co-Scientist or subagents",
                "software development",
            ):
                if token not in frontmatter:
                    errors.append(f"frontmatter description missing trigger boundary: {token}")
        line_count = len(skill.splitlines())
        word_count = len(re.findall(r"\S+", skill))
        if line_count > 96:
            errors.append(f"SKILL.md exceeds 96-line entrypoint cap: {line_count}")
        if word_count > 813:
            errors.append(f"SKILL.md exceeds 813-token entrypoint cap: {word_count}")
        if "Execution is not authorized by this Skill output." not in skill:
            errors.append("SKILL.md is missing the execution-authorization boundary")
        for retired in RETIRED:
            if retired in skill:
                errors.append(f"SKILL.md references retired file: {retired}")

    workflow_path = ROOT / "references" / "workflow.md"
    if workflow_path.is_file():
        workflow = workflow_path.read_text(encoding="utf-8")
        for heading in BLOCK_HEADINGS:
            if heading not in workflow:
                errors.append(f"workflow missing block heading: {heading}")

    core_paths = [
        ROOT / "references" / "workflow.md",
        ROOT / "references" / "roles.md",
        ROOT / "references" / "contracts.md",
    ]
    if all(path.is_file() for path in core_paths) and skill_path.is_file():
        reference_tokens = sum(
            len(re.findall(r"\S+", path.read_text(encoding="utf-8"))) for path in core_paths
        )
        core_tokens = reference_tokens + len(re.findall(r"\S+", skill_path.read_text(encoding="utf-8")))
        if reference_tokens > 6067:
            errors.append(f"core references exceed 6067-token cap: {reference_tokens}")
        if core_tokens > 6881:
            errors.append(f"combined core exceeds 6881-token cap: {core_tokens}")

    for relative in REQUIRED:
        path = ROOT / relative
        if path.suffix == ".md" and path.is_file():
            validate_markdown_links(path, errors)

    cases_path = ROOT / "tests" / "trigger_cases.json"
    if cases_path.is_file():
        try:
            cases = json.loads(cases_path.read_text(encoding="utf-8"))
            for case in cases:
                actual_result = activation_gate(case["prompt"])
                if actual_result != case["activate"]:
                    errors.append(
                        f"trigger case {case['id']} expected {case['activate']} got {actual_result}"
                    )
        except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
            errors.append(f"trigger cases invalid: {exc}")

    behavior_cases_path = ROOT / "tests" / "behavior_contract_cases.json"
    if behavior_cases_path.is_file():
        try:
            cases = json.loads(behavior_cases_path.read_text(encoding="utf-8"))
            ids = [case["id"] for case in cases]
            expected_ids = [
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
            ]
            if ids != expected_ids or len(ids) != len(set(ids)):
                errors.append(f"behavior case IDs/order mismatch: {ids}")
            for case in cases:
                if "$co-scientist-ideation" not in case["prompt"]:
                    errors.append(f"behavior case {case['id']} lacks explicit skill invocation")
                if not isinstance(case["expected"], list) or len(case["expected"]) < 2:
                    errors.append(f"behavior case {case['id']} lacks observable expectations")
            for case in cases[4:]:
                if not isinstance(case.get("required_invariants"), list) or len(case["required_invariants"]) < 3:
                    errors.append(f"behavior case {case['id']} lacks required invariants")
        except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
            errors.append(f"behavior contract cases invalid: {exc}")

    openai_path = ROOT / "agents" / "openai.yaml"
    if openai_path.is_file():
        openai_text = openai_path.read_text(encoding="utf-8")
        for token in (
            'display_name: "Co-Scientist Ideation RC"',
            'default_prompt: "Use $co-scientist-ideation',
            "allow_implicit_invocation: false",
        ):
            if token not in openai_text:
                errors.append(f"agents/openai.yaml missing required RC field: {token}")

    release_path = ROOT / "RELEASE_MANIFEST.yaml"
    if release_path.is_file():
        release_text = release_path.read_text(encoding="utf-8")
        for token in (
            "version: 1.9-rc1",
            "parent_version: 1.8-rc1",
            "status: RELEASE_CANDIDATE",
            "allow_implicit_invocation: false",
        ):
            if token not in release_text:
                errors.append(f"release manifest missing required field: {token}")

    validator_path = ROOT / "scripts" / "validate_skill.py"
    if validator_path.is_file():
        try:
            compile(validator_path.read_text(encoding="utf-8"), str(validator_path), "exec")
        except (OSError, SyntaxError) as exc:
            errors.append(f"compile failed for validate_skill.py: {exc}")

    result = {
        "valid": not errors,
        "scope": "structural_only",
        "errors": errors,
        "warnings": warnings,
        "checked_files": len(actual),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
