# Evaluation Baseline

## Claim boundary

The retained evidence supports one deterministic descriptive statement about a fixed AI-only panel.
It does not support generic superiority, human preference, confirmatory efficacy, scientific truth,
causal effect, or deployment ROI.

Terminal class: `AI_ONLY_EXPLORATORY_HETEROGENEOUS`.

## Final analysis unit and aggregation

The primary unit is the task, not an individual reviewer vote.

1. Each anonymous pair has three eligible AI reviewer choices.
2. Map each reviewer choice to Co-Scientist as `1`, Generic as `0`, and an allowed tie as `0.5`; the
   pair score is the mean of the three mapped values under the frozen tie rule.
3. Each task mean averages its three pair scores.
4. `S_task_equalized` averages the four fixed task means with equal task weight.

The effective panel contains 4 tasks × 3 pairs × 3 reviewers = 36 reviewer decisions. Those 36
decisions are nested observations, not 36 independent scientific replicates; no binomial or
reviewer-level significance claim is promoted.

## Recovered endpoint

| Quantity | Value |
|---|---:|
| Effective reviewer directions toward Co-Scientist | `31/36` |
| Pair majorities toward Co-Scientist | `11/12` |
| `S_task_equalized` | `0.861111` |
| Task means above `0.5` | `4/4` |
| Minimum leave-one-task-out value | `0.814815` |
| Co-Scientist canonical critical failures | `1` |
| Generic canonical critical failures | `0` |

All numeric direction gates passed, but the predeclared “no worse critical/integrity failure” gate
failed because one Co-Scientist package contained unsupported source-specific quantification. One
replicate pair also had a Generic majority. The final label is therefore heterogeneous.

## What the 1.0–1.4 chain preserves

```text
evaluation-method-v1
  └─ review schema, validator, metric and quality–cost contract
v4-ai-followup-1.0
  └─ frozen prompts, task registry, paper custody and base runtime evidence
v4-ai-followup-1.1
  └─ isolation smoke custody
v4-ai-followup-1.2
  └─ trace-capture smoke custody
v4-ai-followup-1.3
  └─ 24 frozen generation packages, anonymous packages and R1/R3 evidence
v4-ai-followup-1.4
  └─ 12 fresh structured R2 records, locks, unblinded pair results and final report
```

Round 1.4 recovered the R2 structured-review seam only. It reused 1.3 generation packages and R1/R3
records, so it is not a fully independent replication. It changed the endpoint from incomplete to
computable without rerunning generation.

## Local custody receipts

All retained trees stay at `evaluation/comparative-efficacy/` so project-root-relative receipts,
`../../../` authority references and sibling links keep their original meaning.

| Relative tree | Files | Bytes | Canonical tree SHA-256 |
|---|---:|---:|---|
| `evaluation-method-v1` | 5 | 43,463 | `e59b0e34758c301c2228a51f94b338704ef088ab01cd402ed3ff9f02a6996bf3` |
| `v4-ai-followup-1.0` | 78 | 42,644,224 | `86e38dcefe76aad292772922c637925177326f6d4a71f09900adde5ee536e4ea` |
| `v4-ai-followup-1.1` | 8 | 52,772 | `d22a6b229fe4eeef5e27c75749f32fedb75dfcfaaac13f388943ea1bc5e58523` |
| `v4-ai-followup-1.2` | 8 | 45,514 | `b58910d74d00a84cde1fca4ce638b0a3785991dc8834cefa37745cab606729b8` |
| `v4-ai-followup-1.3` | 284 | 1,474,571 | `0d328654b34448750dda2255f70e55f38a8414888a50c30ad5fc4439f1629ef7` |
| `v4-ai-followup-1.4` | 48 | 135,864 | `8f578b1ac23d8b17489737e40e0639602cd877e4a76e4df53c604e3340d65e42` |

Combined closure: `431 files / 44,396,408 bytes`.

The 1.0 paper corpus is `36 files / 42,400,715 bytes / canonical SHA-256
44dc80911fc16383d573a4c5926f5f644ccb75ce02d040127628744107a59880`.

## Integrity and endpoint checks

From the repository root, the method tests are read-only:

```powershell
python .\evaluation\comparative-efficacy\evaluation-method-v1\test_evaluation_method.py -q
```

Validate an individual frozen review record with:

```powershell
python .\evaluation\comparative-efficacy\evaluation-method-v1\validate_review_record.py <review.json>
```

Compare the six canonical tree receipts and the paper-corpus receipt against
`internal/finalization/RETAINED_EVALUATION_SHA256SUMS` in a local finalized copy. That manifest is
ignored by Git. The canonical algorithm is ordinal-sorted forward-slash relative paths with UTF-8 LF
`path<TAB>bytes<TAB>sha256<LF>` records.

The public `evaluation/EVALUATION_SUMMARY.yaml` contains enough aggregate data to recompute
`31/36`, `11/12`, and the published task-equalized value. Detailed private pair mappings and papers are
not part of the public surface.

## Reproducibility limit

The closure recomputes the final descriptive endpoint and checks the retained record bytes. It does not
preserve every historical pilot, task-selection proof, disjointness artifact, host snapshot, model
session, or execution dependency needed to rerun the entire study or audit all upstream provenance.
New model calls or selective reruns would create a new experiment and require a separately frozen plan.

## Publication boundary

The complete closure is Git-ignored. Downloaded papers and raw private evaluation artifacts require a
source-license, copyright, privacy and provenance audit before publication. Aggregate results should
always retain the AI-only, fixed-task, recovery-not-replication and critical-failure limitations.
