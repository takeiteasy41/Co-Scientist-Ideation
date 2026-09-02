# Public Evaluation Method

This directory documents how the Co-Scientist Ideation Skill is compared and measured. It is a
public inspection surface, not an installation package and not a runtime dependency of the Skill.
Installers should copy only the co-scientist-ideation/ directory.

The method is designed to answer a bounded question:

> Under the same task and evidence envelope, does a structured ideation workflow produce a more
> decision-useful, evidence-grounded, and falsifiable research package than a strong general prompt?

It does not claim that a single score proves scientific truth, universal superiority, or genuine
novelty.

## Contents

- [PROTOCOL.md](PROTOCOL.md): human-readable claims, arms, task construction, metrics, aggregation,
  fairness controls, leakage boundaries, and known weaknesses.
- [protocol.yaml](protocol.yaml): machine-readable method record.
- [review_record.schema.json](review_record.schema.json): strict review-record schema.
- [validate_review_record.py](validate_review_record.py): standard-library validator for one record.
- [quality_cost_summary.py](quality_cost_summary.py): explicit-input descriptive cost calculator.
- [examples/review_record.json](examples/review_record.json): synthetic, non-scientific example.
- [tests/test_public_evaluation.py](tests/test_public_evaluation.py): deterministic local checks.

## Run the public checks

From the repository root:

```powershell
python evaluation/public-method/validate_review_record.py evaluation/public-method/examples/review_record.json
python -m unittest discover -s evaluation/public-method/tests -p test_public_evaluation.py -q
```

These commands use no network, model, PDF, external database, or real evaluation corpus.

## Current endpoint

The retained exploratory panel contains four fixed tasks, twenty visible predecessor papers, four
hidden later reference mechanisms, two generation arms, twelve anonymous output pairs, and thirty-six
nested AI reviewer decisions. The task is the primary analysis unit.

The descriptive endpoint is:

- 31 of 36 reviewer directions toward Co-Scientist;
- 11 of 12 pair majorities toward Co-Scientist;
- task-equalized score 0.861111;
- one Co-Scientist canonical critical failure and zero Generic canonical critical failures;
- approximately 3.83 times as many generation requests and 1.99 times the mean parent wall time for
  Co-Scientist in the recorded comparison.

One Co-Scientist package contained a substantive source-use error, one pair majority favored Generic,
and the predeclared no-worse-critical-failure gate did not pass. The endpoint is therefore a
heterogeneous AI-only exploratory trade-off, not an unconditional win.

## Generic capability envelope

The retained Generic prompts declared these four research capabilities:

1. research-ideation;
2. hypothesis-generation;
3. scientific-brainstorming;
4. literature-review.

They also declared a host-bundled read-only PDF capability. Network retrieval, project writes, and
subagents were forbidden for that comparison.

Three source links are confirmed:

- [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/hypothesis-generation)
- [scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-brainstorming)
- [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review)

No authoritative upstream GitHub source was confirmed for the exact local research-ideation Skill, so
this package intentionally provides no speculative download link. The four names describe the
declared capability envelope; retained runtime receipts do not record a positive per-request list,
so they do not prove that every request invoked every named Skill.

## How to improve this method

Contributions are most useful when they address:

- stronger, non-straw Generic and structured-single-agent baselines;
- task and domain coverage;
- independent qualified-human review for open-ended tasks;
- reviewer calibration and shared-model bias;
- hidden-reference alignment versus true novelty;
- correct no-finalist and insufficient-evidence controls;
- actual per-request capability logging without private prompt leakage; and
- cost and practical-significance interpretation.

The current method remains intentionally small and inspectable. Real prompts, outputs, hidden targets,
paper PDFs, private mappings, and complete model-run records are not public.
