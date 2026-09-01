# Evaluation

This directory separates a small public result summary from the local endpoint-recomputation closure.

## Public surface

- [`EVALUATION_SUMMARY.yaml`](EVALUATION_SUMMARY.yaml) records the frozen aggregate endpoint, analysis
  unit, limitations and subtree receipts.
- [`../docs/EVALUATION_BASELINE.md`](../docs/EVALUATION_BASELINE.md) explains the method, dependency
  graph, checks and claim boundary.

## Local ignored surface

`comparative-efficacy/` contains the retained endpoint-recomputation closure:

```text
evaluation-method-v1
v4-ai-followup-1.0
v4-ai-followup-1.1
v4-ai-followup-1.2
v4-ai-followup-1.3
v4-ai-followup-1.4
```

The closure is `431 files / 44,396,408 bytes`. Its paper corpus is `36 files / 42,400,715 bytes`.
Both are excluded by the root `.gitignore`.

The retained set supports deterministic recomputation of the final descriptive endpoint and integrity
checking of its effective records. It is not a complete rerun package for every historical model call,
pilot, task-selection decision, disjointness proof or host snapshot.

## Endpoint

Evidence tier: `AI_ONLY_EXPLORATORY_RECOVERY`  
Terminal class: `AI_ONLY_EXPLORATORY_HETEROGENEOUS`

The fixed panel contains four tasks, three anonymous pairs per task and three AI reviewer decisions per
pair. Effective results are `31/36` reviewer directions, `11/12` pair majorities and task-equalized
score `0.861111` toward Co-Scientist. One Co-Scientist source-misuse failure and one Generic-direction
pair are part of the endpoint.

This is a local exploratory signal under fixed tasks, packages, prompts and models. It does not
establish universal quality, human preference, scientific truth, confirmatory efficacy, causal impact
or deployment ROI.

## Local checks

From the repository root:

```powershell
python .\evaluation\comparative-efficacy\evaluation-method-v1\test_evaluation_method.py -q
```

The finalized local copy also contains
`internal/finalization/RETAINED_EVALUATION_SHA256SUMS`, which binds every retained leaf and the six
canonical subtree receipts. That file is intentionally not public.

Do not publish downloaded papers, raw pair mappings or private evaluation artifacts without a separate
source-license, copyright, privacy and provenance audit.
